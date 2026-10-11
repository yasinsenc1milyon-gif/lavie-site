// Yönetim sayfası: siparişleri listele, onayla, düzenle, sil; çift yorumlarını onayla
import { ALANLAR, DURUMLAR, ciftGetir, ciftKaydet, ciftVerisiniSil, govde, json, linkler, temizle, uc, yorumSatiri } from "../../lib/ortak.js";

export const onRequest = uc(async ({ request, env, db }) => {
  const sifre = env.ADMIN_SIFRE;
  if (!sifre) return json({ ok: false, hata: "sifre_ayarlanmamis" }, 503);
  if (request.headers.get("x-sifre") !== sifre) return json({ ok: false, hata: "sifre" }, 401);

  if (request.method === "GET") {
    const [cr, sr, yr] = await db.batch([
      db.prepare("SELECT veri, durum FROM ciftler ORDER BY olusturma DESC"),
      db.prepare("SELECT slug, COUNT(*) AS n FROM yanitlar GROUP BY slug"),
      db.prepare("SELECT * FROM yorumlar ORDER BY zaman DESC")
    ]);
    const sayac = Object.fromEntries((sr.results || []).map(r => [r.slug, r.n]));
    const ciftler = (cr.results || []).map(r => {
      const c = { ...JSON.parse(r.veri), durum: r.durum };
      return { ...c, linkler: linkler(request, c), yanitSayisi: sayac[c.slug] || 0 };
    });
    return json({ ok: true, ciftler, yorumlar: (yr.results || []).map(yorumSatiri) });
  }

  if (request.method !== "POST") return json({ ok: false, hata: "yontem" }, 405);
  const d = await govde(request);
  if (!d || !d.slug) return json({ ok: false, hata: "veri" }, 400);
  const slug = String(d.slug);

  if (d.islem === "yorum-onay" || d.islem === "yorum-sil") {
    const y = await db.prepare("SELECT * FROM yorumlar WHERE slug = ?").bind(slug).first();
    if (!y) return json({ ok: false, hata: "bulunamadi" }, 404);
    if (d.islem === "yorum-sil") { await db.prepare("DELETE FROM yorumlar WHERE slug = ?").bind(slug).run(); return json({ ok: true }); }
    await db.prepare("UPDATE yorumlar SET onay = ? WHERE slug = ?").bind(d.onay ? 1 : 0, slug).run();
    return json({ ok: true, yorum: yorumSatiri({ ...y, onay: d.onay ? 1 : 0 }) });
  }

  const c = slug === "ornek" ? null : await ciftGetir(db, slug);
  if (!c) return json({ ok: false, hata: "bulunamadi" }, 404);

  if (d.islem === "durum") {
    if (!DURUMLAR.includes(d.durum)) return json({ ok: false, hata: "durum" }, 400);
    c.durum = d.durum;
  } else if (d.islem === "guncelle") {
    const yeni = temizle({ ...c, ...d.alanlar });
    for (const k of ALANLAR) c[k] = yeni[k];
  } else if (d.islem === "sil") {
    await ciftVerisiniSil(db, c.slug);
    return json({ ok: true });
  } else {
    return json({ ok: false, hata: "islem" }, 400);
  }
  await ciftKaydet(db, c);
  return json({ ok: true, cift: { ...c, linkler: linkler(request, c) } });
});
