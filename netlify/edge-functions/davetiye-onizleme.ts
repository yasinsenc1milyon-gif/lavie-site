// WhatsApp/Instagram link önizlemesi: davetiye sayfasına çiftin adı, tarihi ve tasarım görseli eklenir.
import { getStore } from "@netlify/blobs";

const TASARIMLAR = ["zeytin", "gece", "gul", "mono", "ege"];
const BASLIK: Record<string, string> = { "Düğün": "Düğün Davetiyesi", "Nişan": "Nişan Davetiyesi", "Kına": "Kına Gecesi Davetiyesi", "Söz": "Söz Töreni Davetiyesi" };
const ORNEK = { durum: "aktif", tasarim: "zeytin", tur: "Düğün", gelin: "Elif", damat: "Burak", tarih: "2027-06-12", mekan: "Dragos Kır Bahçesi" };

const esc = (s: unknown) => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c] as string));

function tarihYaz(t: string) {
  let s = String(t || "").trim();
  const m = s.match(/^(\d{1,2})[./-](\d{1,2})[./-](\d{4})$/);
  if (m) s = `${m[3]}-${m[2].padStart(2, "0")}-${m[1].padStart(2, "0")}`;
  const d = new Date(s + "T12:00:00");
  if (isNaN(d.getTime())) return "";
  try { return d.toLocaleDateString("tr-TR", { day: "numeric", month: "long", year: "numeric", weekday: "long" }); } catch { return s; }
}

export default async (req: Request, context: { next: () => Promise<Response> }) => {
  const res = await context.next();
  let meta = "", baslik = "";
  try {
    const url = new URL(req.url);
    const slug = (url.searchParams.get("c") || "").toLowerCase().trim().slice(0, 60);
    if (!slug) return res;
    let c: any = null;
    if (slug === "ornek" || slug === "elif-burak") c = ORNEK;
    else c = await getStore({ name: "ciftler", consistency: "strong" }).get(slug, { type: "json" });
    if (!c || c.durum !== "aktif") return res;

    baslik = `${c.gelin} & ${c.damat} · ${BASLIK[c.tur] || "Davetiye"}`;
    const aciklama = [tarihYaz(c.tarih), c.mekan].filter(Boolean).join(" · ") + ". Davetiyemizi açmak için dokunun.";
    const gorsel = `${url.origin}/og/${TASARIMLAR.includes(c.tasarim) ? c.tasarim : "zeytin"}.jpg`;
    meta = `
<meta name="description" content="${esc(aciklama)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Lavie">
<meta property="og:title" content="${esc(baslik)}">
<meta property="og:description" content="${esc(aciklama)}">
<meta property="og:image" content="${esc(gorsel)}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="${esc(url.href)}">
<meta name="twitter:card" content="summary_large_image">`;
  } catch {
    return res;
  }
  let html = await res.text();
  html = html.replace(/<title>[^<]*<\/title>/, `<title>${esc(baslik)}</title>`)
             .replace(/<!--og-->[\s\S]*?<!--\/og-->/, "")
             .replace("</head>", meta + "\n</head>");
  const h = new Headers(res.headers);
  h.delete("content-length");
  h.set("cache-control", "public, max-age=0, must-revalidate");
  return new Response(html, { status: res.status, headers: h });
};

export const config = { path: "/d.html" };
