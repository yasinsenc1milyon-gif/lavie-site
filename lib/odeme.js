// Shopier ile kartla ödeme: müşteri tek bir Shopier ürününden öder; site Shopier'deki
// siparişleri okuyup telefon numarasıyla eşleştirir ve davetiyeyi otomatik yayına alır.
import { shopier } from "./shopier.js";
import { ciftKaydet } from "./ortak.js";

export const urunId = env => (String(env.SHOPIER_URUN_URL || "").match(/(\d{4,})\/?(?:[?#].*)?$/) || [])[1] || null;
export const odemeAcik = env => !!(env.SHOPIER_PAT && env.SHOPIER_URUN_URL);
const tel10 = s => String(s || "").replace(/\D/g, "").slice(-10);
const listele = v => Array.isArray(v) ? v : (v && (v.data || v.items || v.orders)) || [];

function siparisTelefonlari(o) {
  return [o.billingInfo, o.shippingInfo, o.customer, o.buyer].filter(Boolean)
    .map(x => tel10(x.phone || x.phoneNumber || x.gsm)).filter(t => t.length === 10);
}
function bizimUrun(o, id) {
  const kalemler = o.lineItems || [];
  if (!id) return true;
  return kalemler.some(k => String(k.productId) === String(id));
}
const odendi = o => !o.paymentStatus || o.paymentStatus === "paid";

// Son siparişleri getirir (Shopier tarih filtresi olmadan boş liste döndürür)
async function sonSiparisler(env, baslangic) {
  const id = urunId(env);
  const dateStart = new Date(baslangic).toISOString().replace(/\.\d+Z$/, "Z");
  let r = await shopier(env, "/orders", { query: { dateStart, limit: 50, ...(id ? { productId: id } : {}) } });
  if (r.status >= 400 && id) r = await shopier(env, "/orders", { query: { dateStart, limit: 50 } });
  if (r.status !== 200) throw new Error("shopier_" + r.status);
  return listele(r.veri).filter(o => odendi(o) && bizimUrun(o, id));
}

async function kullanilmis(db, ids) {
  if (!ids.length) return new Set();
  const r = await db.prepare(`SELECT siparis_id FROM odemeler WHERE siparis_id IN (${ids.map(() => "?").join(",")})`).bind(...ids).all();
  return new Set((r.results || []).map(x => x.siparis_id));
}

async function etkinlestir(db, c, o) {
  const id = String(o.id);
  const r = await db.prepare("INSERT OR IGNORE INTO odemeler (siparis_id, slug, tutar, zaman) VALUES (?, ?, ?, ?)")
    .bind(id, c.slug, String((o.totals && o.totals.total) || ""), new Date().toISOString()).run();
  if (!r.meta || r.meta.changes !== 1) return false; // başka bir davetiyeye eşleşmiş
  c.durum = "aktif";
  c.odeme = { yontem: "shopier", siparis: id, tutar: (o.totals && o.totals.total) || null, zaman: new Date().toISOString() };
  await ciftKaydet(db, c);
  return true;
}

// Bekleyen bir davetiye için Shopier'de ödeme arar. Bulursa yayına alır.
export async function odemeAra(env, db, c) {
  if (!c || c.durum === "aktif") return c && c.durum === "aktif";
  if (!odemeAcik(env)) return false;
  const bas = Date.parse(c.kartZaman || c.olusturma || 0) - 15 * 60e3;
  const siparisler = await sonSiparisler(env, Math.max(bas, Date.now() - 7 * 864e5));
  const kul = await kullanilmis(db, siparisler.map(o => String(o.id)));
  const bos = siparisler.filter(o => !kul.has(String(o.id)) && (o.dateCreated ? Date.parse(o.dateCreated) : Date.now()) >= bas);
  const tel = tel10(c.telefon);
  const kod = String(c.slug).toLowerCase();
  const esles = bos.find(o => String(o.note || "").toLowerCase().includes(kod))
    || (tel.length === 10 && bos.find(o => siparisTelefonlari(o).includes(tel)));
  if (esles) return etkinlestir(db, c, esles);
  // Telefon farklı yazılmışsa: aynı zaman aralığında tek bekleyen kart ödemesi ve tek boş sipariş varsa eşleştir
  if (bos.length === 1 && c.kartZaman) {
    const r = await db.prepare("SELECT COUNT(*) AS n FROM ciftler WHERE durum = 'bekliyor' AND json_extract(veri, '$.kartZaman') >= ?")
      .bind(new Date(bas).toISOString()).first();
    if (r && r.n === 1) return etkinlestir(db, c, bos[0]);
  }
  return false;
}

// Shopier bildirimi geldiğinde: kartla ödeme bekleyen tüm davetiyeleri kontrol et
export async function bekleyenleriKontrolEt(env, db) {
  const gun = new Date(Date.now() - 3 * 864e5).toISOString();
  const r = await db.prepare("SELECT veri, durum FROM ciftler WHERE durum = 'bekliyor' AND json_extract(veri, '$.kartZaman') >= ?").bind(gun).all();
  let n = 0;
  for (const row of r.results || []) {
    const c = { ...JSON.parse(row.veri), durum: row.durum };
    try { if (await odemeAra(env, db, c)) n++; } catch (e) { console.error("odemeAra", e.message); }
  }
  return n;
}

// Bildirim imzası: gövdenin HMAC-SHA256'sı (hex ya da base64)
export async function imzaDogru(govdeMetni, imza, token) {
  if (!imza || !token) return false;
  const k = await crypto.subtle.importKey("raw", new TextEncoder().encode(token), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const sum = new Uint8Array(await crypto.subtle.sign("HMAC", k, new TextEncoder().encode(govdeMetni)));
  const hex = [...sum].map(b => b.toString(16).padStart(2, "0")).join("");
  const b64 = btoa(String.fromCharCode(...sum));
  const esit = (a, b) => { if (a.length !== b.length) return false; let x = 0; for (let i = 0; i < a.length; i++) x |= a.charCodeAt(i) ^ b.charCodeAt(i); return x === 0; };
  return esit(imza.trim().toLowerCase(), hex) || esit(imza.trim(), b64);
}

// Yönetimden tek seferlik: order.created bildirimini bu siteye bağlar, imza anahtarını saklar
export async function bildirimBagla(env, db, origin) {
  const url = origin + "/api/odeme/bildirim";
  const liste = await shopier(env, "/webhooks");
  for (const w of listele(liste.veri)) if (w.url === url && w.id) await shopier(env, "/webhooks/" + encodeURIComponent(w.id), { method: "DELETE" });
  const r = await shopier(env, "/webhooks", { method: "POST", body: { event: "order.created", url } });
  const token = r.veri && (r.veri.token || r.veri.secret);
  if (r.status >= 300 || !token) return { ok: false, durum: r.status, hata: (r.veri && (r.veri.message || r.veri.error)) || r.metin || "token_yok" };
  await db.prepare("INSERT INTO ayarlar (anahtar, deger) VALUES ('webhook_token', ?) ON CONFLICT(anahtar) DO UPDATE SET deger = excluded.deger").bind(token).run();
  return { ok: true, url };
}
