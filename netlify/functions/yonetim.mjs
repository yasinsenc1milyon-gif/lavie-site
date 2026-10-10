// Yönetim sayfası: siparişleri listele, onayla, düzenle, sil; çift yorumlarını onayla
import { ALANLAR, DURUMLAR, ciftStore, ciftVerisiniSil, govde, json, linkler, ortam, temizle, yanitStore, yorumStore } from "../lib/ortak.mjs";

export default async (req) => {
  const sifre = ortam("ADMIN_SIFRE");
  if (!sifre) return json({ ok: false, hata: "sifre_ayarlanmamis" }, 503);
  if (req.headers.get("x-sifre") !== sifre) return json({ ok: false, hata: "sifre" }, 401);

  const store = ciftStore();

  if (req.method === "GET") {
    const { blobs } = await store.list();
    const ciftler = (await Promise.all(blobs.map(b => store.get(b.key, { type: "json" })))).filter(Boolean);
    const sayac = {};
    const { blobs: yanitlar } = await yanitStore().list();
    for (const y of yanitlar) { const s = y.key.split("/")[0]; sayac[s] = (sayac[s] || 0) + 1; }
    const liste = ciftler
      .map(c => ({ ...c, linkler: linkler(req, c), yanitSayisi: sayac[c.slug] || 0 }))
      .sort((a, b) => String(b.olusturma).localeCompare(String(a.olusturma)));
    const ys = yorumStore();
    const { blobs: yb } = await ys.list();
    const yorumlar = (await Promise.all(yb.map(b => ys.get(b.key, { type: "json" })))).filter(Boolean)
      .sort((a, b) => String(b.zaman).localeCompare(String(a.zaman)));
    return json({ ok: true, ciftler: liste, yorumlar });
  }

  if (req.method === "POST") {
    const d = await govde(req);
    if (!d || !d.slug) return json({ ok: false, hata: "veri" }, 400);

    if (d.islem === "yorum-onay" || d.islem === "yorum-sil") {
      const ys = yorumStore();
      const y = await ys.get(d.slug, { type: "json" });
      if (!y) return json({ ok: false, hata: "bulunamadi" }, 404);
      if (d.islem === "yorum-sil") { await ys.delete(d.slug); return json({ ok: true }); }
      y.onay = !!d.onay;
      await ys.setJSON(d.slug, y);
      return json({ ok: true, yorum: y });
    }

    const c = await store.get(d.slug, { type: "json" });
    if (!c) return json({ ok: false, hata: "bulunamadi" }, 404);

    if (d.islem === "durum") {
      if (!DURUMLAR.includes(d.durum)) return json({ ok: false, hata: "durum" }, 400);
      c.durum = d.durum;
    } else if (d.islem === "guncelle") {
      const yeni = temizle({ ...c, ...d.alanlar });
      for (const k of ALANLAR) c[k] = yeni[k];
    } else if (d.islem === "sil") {
      await store.delete(d.slug);
      await ciftVerisiniSil(d.slug);
      return json({ ok: true });
    } else {
      return json({ ok: false, hata: "islem" }, 400);
    }
    await store.setJSON(c.slug, c);
    return json({ ok: true, cift: { ...c, linkler: linkler(req, c) } });
  }

  return json({ ok: false, hata: "yontem" }, 405);
};

export const config = { path: "/api/yonetim" };
