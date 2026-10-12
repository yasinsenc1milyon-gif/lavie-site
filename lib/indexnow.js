// IndexNow: Bing, Yandex ve diğer arama motorlarına site haritasındaki sayfaları bildirir.
const ANAHTAR = "9852646d7514d145e196d9e4fba5ce6b";

export async function indexNowGonder(env, origin) {
  const r = await env.ASSETS.fetch(new Request(origin + "/sitemap.xml"));
  const xml = await r.text();
  const urller = [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map(m => m[1].replace(/^https?:\/\/[^/]+/, origin));
  if (!urller.length) return { ok: false, hata: "site_haritasi_bos" };
  const host = new URL(origin).host;
  const cevap = await fetch("https://api.indexnow.org/indexnow", {
    method: "POST",
    headers: { "content-type": "application/json; charset=utf-8" },
    body: JSON.stringify({ host, key: ANAHTAR, keyLocation: origin + "/" + ANAHTAR + ".txt", urlList: urller })
  });
  return { ok: cevap.status < 300, durum: cevap.status, adet: urller.length };
}
