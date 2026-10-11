// Kartla ödeme durumu: müşteri sayfası birkaç saniyede bir sorar; ödeme bulunursa linkler döner.
import { ciftGetir, ciftKaydet, govde, json, linkler, uc } from "../../lib/ortak.js";
import { odemeAcik, odemeAra } from "../../lib/odeme.js";

const sonKontrol = new Map(); // aynı davetiye için Shopier'e en fazla 6 saniyede bir sor

async function yetkili(db, slug, k) {
  const c = await ciftGetir(db, slug);
  if (!c || c.slug === "ornek" || !k || c.anahtar !== k) return null;
  return c;
}

export const onRequestGet = uc(async ({ request, env, db }) => {
  const q = new URL(request.url).searchParams;
  const c = await yetkili(db, q.get("c"), q.get("k"));
  if (!c) return json({ ok: false, hata: "bulunamadi" }, 404);
  if (c.durum !== "aktif" && odemeAcik(env) && Date.now() - (sonKontrol.get(c.slug) || 0) > 6000) {
    sonKontrol.set(c.slug, Date.now());
    try { await odemeAra(env, db, c); } catch (e) { console.error("odeme", e.message); }
  }
  return json({ ok: true, durum: c.durum, ...(c.durum === "aktif" ? { linkler: linkler(request, c) } : {}) });
});

// Müşteri "Kartla öde"ye bastığında işaretlenir (eşleştirme bu zamandan sonrasına bakar)
export const onRequestPost = uc(async ({ request, env, db }) => {
  const d = await govde(request);
  const c = d && await yetkili(db, d.c, d.k);
  if (!c) return json({ ok: false, hata: "bulunamadi" }, 404);
  if (!odemeAcik(env)) return json({ ok: false, hata: "kapali" }, 503);
  if (c.durum === "bekliyor") { c.kartZaman = new Date().toISOString(); await ciftKaydet(db, c); }
  return json({ ok: true, url: env.SHOPIER_URUN_URL });
});
