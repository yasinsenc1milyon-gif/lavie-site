// Çiftin paneli: yanıtlar, hatıra defteri, fotoğraflar ve yorum
import { CIFT_DUZENLER, FOTO_SINIR, ciftStore, temizle, ciftGetir, fotoListesi, fotoStore, fotoUrl, govde, json, mesajStore, mesajlariGetir, ornekMi, yanitlariGetir, yorumStore } from "../lib/ortak.mjs";

const gecerliId = id => /^[\w-]{1,80}$/.test(String(id || ""));

export default async (req) => {
  let p = new URL(req.url).searchParams, d = null;
  if (req.method === "POST") { d = await govde(req); if (!d) return json({ ok: false, hata: "veri" }, 400); }
  const slug = d ? d.c : p.get("c"), k = d ? d.k : p.get("k");
  const c = await ciftGetir(slug);
  if (!c || c.durum === "bekliyor") return json({ ok: false, hata: "bulunamadi" }, 404);
  if (!k || k !== c.anahtar) return json({ ok: false, hata: "anahtar" }, 403);

  if (req.method === "GET") {
    const [yanitlar, mesajlar, fotolar, yorum] = await Promise.all([
      yanitlariGetir(c.slug), mesajlariGetir(c.slug), fotoListesi(c.slug), yorumStore().get(c.slug, { type: "json" })
    ]);
    const { anahtar, telefon, olusturma, durum, ...acik } = c;
    return json({
      ok: true, cift: acik, yanitlar, mesajlar,
      fotolar: fotolar.map(id => ({ id, url: fotoUrl(c.slug, id) })), fotoSiniri: FOTO_SINIR,
      yorum: yorum ? { puan: yorum.puan, yorum: yorum.yorum, onay: yorum.onay } : null,
      ornek: ornekMi(c.slug)
    });
  }

  if (req.method === "POST") {
    if (ornekMi(c.slug)) return json({ ok: false, hata: "ornek" }, 400);
    if (d.islem === "guncelle" && d.alanlar && typeof d.alanlar === "object") {
      const izinli = Object.fromEntries(CIFT_DUZENLER.filter(k => k in d.alanlar).map(k => [k, d.alanlar[k]]));
      const yeni = temizle({ ...c, ...izinli });
      if (!yeni.gelin || !yeni.damat || !yeni.tarih) return json({ ok: false, hata: "eksik" }, 400);
      for (const k of CIFT_DUZENLER) c[k] = yeni[k];
      await ciftStore().setJSON(c.slug, c);
      const { anahtar, telefon, olusturma, durum, ...acik } = c;
      return json({ ok: true, cift: acik });
    }
    if (d.islem === "mesaj-sil" && gecerliId(d.id)) { await mesajStore().delete(`${c.slug}/${d.id}`); return json({ ok: true }); }
    if (d.islem === "foto-sil" && gecerliId(d.id)) { await fotoStore().delete(`${c.slug}/${d.id}`); return json({ ok: true }); }
    if (d.islem === "yorum") {
      const puan = Math.min(Math.max(parseInt(d.puan, 10) || 5, 1), 5);
      const yorum = String(d.yorum || "").trim().slice(0, 500);
      if (yorum.length < 5) return json({ ok: false, hata: "eksik" }, 400);
      await yorumStore().setJSON(c.slug, {
        slug: c.slug, ad: `${String(c.gelin).split(" ")[0]} & ${String(c.damat).split(" ")[0]}`, tur: c.tur,
        puan, yorum, onay: false, zaman: new Date().toISOString()
      });
      return json({ ok: true });
    }
    return json({ ok: false, hata: "islem" }, 400);
  }
  return json({ ok: false, hata: "yontem" }, 405);
};

export const config = { path: "/api/panel" };
