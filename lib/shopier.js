// Shopier REST API (v1) yardımcıları. Anahtar Cloudflare'de SHOPIER_PAT gizli değişkeninde durur.
const TABAN = "https://api.shopier.com/v1";

export async function shopier(env, yol, { method = "GET", body, query } = {}) {
  if (!env.SHOPIER_PAT) return { status: 0, hata: "anahtar_yok" };
  const u = new URL(TABAN + yol);
  if (query) for (const [k, v] of Object.entries(query)) if (v != null) u.searchParams.set(k, String(v));
  const r = await fetch(u, {
    method,
    headers: { authorization: "Bearer " + env.SHOPIER_PAT, accept: "application/json", ...(body ? { "content-type": "application/json" } : {}) },
    body: body ? JSON.stringify(body) : undefined
  });
  const metin = await r.text();
  let veri = null; try { veri = metin ? JSON.parse(metin) : null; } catch { veri = null; }
  return { status: r.status, veri, metin: veri ? null : metin.slice(0, 300) };
}

// Bağlantı testi: hangi uç noktalara erişebildiğimizi gösterir (gizli bilgi döndürmez)
export async function shopierTest(env) {
  const ozet = r => ({ durum: r.status, hata: r.hata || (r.status >= 400 ? (r.veri && (r.veri.message || r.veri.error || r.veri.title)) || r.metin : null) });
  const gecen = new Date(Date.now() - 30 * 864e5).toISOString().replace(/\.\d+Z$/, "Z");
  const [shop, urunler, siparisler, webhooklar] = await Promise.all([
    shopier(env, "/shop"), shopier(env, "/products", { query: { limit: 1 } }),
    shopier(env, "/orders", { query: { dateStart: gecen, limit: 1 } }), shopier(env, "/webhooks")
  ]);
  const s = shop.veri || {};
  return {
    anahtar: !!env.SHOPIER_PAT,
    magaza: { ...ozet(shop), ad: s.name || s.title || null, adres: s.url || s.slug || s.username || null },
    urunler: { ...ozet(urunler), adet: Array.isArray(urunler.veri) ? urunler.veri.length : null },
    siparisler: { ...ozet(siparisler), adet: Array.isArray(siparisler.veri) ? siparisler.veri.length : null },
    webhooklar: { ...ozet(webhooklar), adet: Array.isArray(webhooklar.veri) ? webhooklar.veri.length : null },
    magazaAlanlari: Object.keys(s).slice(0, 25)
  };
}
