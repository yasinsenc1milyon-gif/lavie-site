// WhatsApp/Instagram link önizlemesi: davetiye sayfasına çiftin adı, tarihi ve tasarım görseli eklenir.
import { TASARIMLAR, ciftGetir, veritabani } from "./ortak.js";

const BASLIK = { "Düğün": "Düğün Davetiyesi", "Nişan": "Nişan Davetiyesi", "Kına": "Kına Gecesi Davetiyesi", "Söz": "Söz Töreni Davetiyesi" };
const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

function tarihYaz(t) {
  let s = String(t || "").trim();
  const m = s.match(/^(\d{1,2})[./-](\d{1,2})[./-](\d{4})$/);
  if (m) s = `${m[3]}-${m[2].padStart(2, "0")}-${m[1].padStart(2, "0")}`;
  const d = new Date(s + "T12:00:00");
  if (isNaN(d.getTime())) return "";
  try { return d.toLocaleDateString("tr-TR", { day: "numeric", month: "long", year: "numeric", weekday: "long" }); } catch { return s; }
}

// Statik d.html dosyasını getirir (temiz adres yönlendirmelerini takip eder)
async function sayfaGetir(env, url) {
  let u = new URL("/d", url);
  for (let i = 0; i < 3; i++) {
    const r = await env.ASSETS.fetch(new Request(u.toString()));
    if (r.status >= 300 && r.status < 400 && r.headers.get("location")) { u = new URL(r.headers.get("location"), u); continue; }
    return r;
  }
  return env.ASSETS.fetch(new Request(new URL("/d.html", url).toString()));
}

export async function davetiyeSayfasi({ request, env }) {
  const url = new URL(request.url);
  const res = await sayfaGetir(env, url);
  let meta = "", baslik = "";
  try {
    const db = await veritabani(env);
    const c = await ciftGetir(db, url.searchParams.get("c"));
    if (!c || c.durum !== "aktif") return res;
    // Örnek davetiye: vitrinde yazılan isimler ve seçilen tasarım önizlemeye de yansısın
    if (c.slug === "ornek" || url.searchParams.get("c") === "ornek") {
      const temiz = v => (v || "").replace(/\s+/g, " ").trim().slice(0, 20);
      const g = temiz(url.searchParams.get("gelin")), d = temiz(url.searchParams.get("damat")), t = url.searchParams.get("t");
      if (g) c.gelin = g;
      if (d) c.damat = d;
      if (t && TASARIMLAR.includes(t)) c.tasarim = t;
    }
    baslik = `${c.gelin} & ${c.damat} · ${BASLIK[c.tur] || "Davetiye"}`;
    const aciklama = [tarihYaz(c.tarih), c.mekan].filter(Boolean).join(" · ") + ". Davetiyemizi açmak için dokunun.";
    const gorsel = `${url.origin}/og/${TASARIMLAR.includes(c.tasarim) ? c.tasarim : "zeytin"}.jpg`;
    meta = `
<meta name="description" content="${esc(aciklama)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="LaVie Davetiye">
<meta property="og:title" content="${esc(baslik)}">
<meta property="og:description" content="${esc(aciklama)}">
<meta property="og:image" content="${esc(gorsel)}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="${esc(url.href)}">
<meta name="twitter:card" content="summary_large_image">`;
  } catch (e) {
    console.error("onizleme", e && (e.message || e));
    return res;
  }
  let html = await res.text();
  html = html.replace(/<title>[^<]*<\/title>/, `<title>${esc(baslik)}</title>`)
             .replace(/<!--og-->[\s\S]*?<!--\/og-->/, "")
             .replace("</head>", meta + "\n</head>");
  const h = new Headers(res.headers);
  h.delete("content-length");
  h.set("cache-control", "public, max-age=0, must-revalidate");
  return new Response(html, { status: 200, headers: h });
}
