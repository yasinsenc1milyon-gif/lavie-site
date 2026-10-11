// Çiftin paneli: yanıtlar, hatıra defteri, bilgi düzenleme ve yorum
import { CIFT_DUZENLER, ciftGetir, ciftKaydet, govde, json, mesajlariGetir, ornekMi, temizle, uc, yanitlariGetir } from "../../lib/ortak.js";

const gecerliId = id => /^\d{1,12}$/.test(String(id || ""));

export const onRequest = uc(async ({ request, db }) => {
  const p = new URL(request.url).searchParams;
  let d = null;
  if (request.method === "POST") { d = await govde(request); if (!d) return json({ ok: false, hata: "veri" }, 400); }
  else if (request.method !== "GET") return json({ ok: false, hata: "yontem" }, 405);
  const c = await ciftGetir(db, d ? d.c : p.get("c"));
  const k = d ? d.k : p.get("k");
  if (!c || c.durum === "bekliyor") return json({ ok: false, hata: "bulunamadi" }, 404);
  if (!k || k !== c.anahtar) return json({ ok: false, hata: "anahtar" }, 403);

  if (request.method === "GET") {
    const [yanitlar, mesajlar, yorum] = await Promise.all([
      ornekMi(c.slug) ? [] : yanitlariGetir(db, c.slug),
      ornekMi(c.slug) ? [] : mesajlariGetir(db, c.slug),
      db.prepare("SELECT puan, yorum, onay FROM yorumlar WHERE slug = ?").bind(c.slug).first()
    ]);
    const { anahtar, telefon, olusturma, durum, ...acik } = c;
    return json({
      ok: true, cift: acik, yanitlar, mesajlar,
      yorum: yorum ? { puan: yorum.puan, yorum: yorum.yorum, onay: !!yorum.onay } : null,
      ornek: ornekMi(c.slug)
    });
  }

  if (ornekMi(c.slug)) return json({ ok: false, hata: "ornek" }, 400);
  if (d.islem === "guncelle" && d.alanlar && typeof d.alanlar === "object") {
    const izinli = Object.fromEntries(CIFT_DUZENLER.filter(x => x in d.alanlar).map(x => [x, d.alanlar[x]]));
    const yeni = temizle({ ...c, ...izinli });
    if (!yeni.gelin || !yeni.damat || !yeni.tarih) return json({ ok: false, hata: "eksik" }, 400);
    for (const x of CIFT_DUZENLER) c[x] = yeni[x];
    await ciftKaydet(db, c);
    const { anahtar, telefon, olusturma, durum, ...acik } = c;
    return json({ ok: true, cift: acik });
  }
  if (d.islem === "mesaj-sil" && gecerliId(d.id)) {
    await db.prepare("DELETE FROM mesajlar WHERE slug = ? AND id = ?").bind(c.slug, Number(d.id)).run();
    return json({ ok: true });
  }
  if (d.islem === "yorum") {
    const puan = Math.min(Math.max(parseInt(d.puan, 10) || 5, 1), 5);
    const yorum = String(d.yorum || "").trim().slice(0, 500);
    if (yorum.length < 5) return json({ ok: false, hata: "eksik" }, 400);
    const ad = `${String(c.gelin).split(" ")[0]} & ${String(c.damat).split(" ")[0]}`;
    await db.prepare("INSERT INTO yorumlar (slug, ad, tur, puan, yorum, onay, zaman) VALUES (?, ?, ?, ?, ?, 0, ?) ON CONFLICT(slug) DO UPDATE SET ad = excluded.ad, tur = excluded.tur, puan = excluded.puan, yorum = excluded.yorum, onay = 0, zaman = excluded.zaman")
      .bind(c.slug, ad, c.tur, puan, yorum, new Date().toISOString()).run();
    return json({ ok: true });
  }
  return json({ ok: false, hata: "islem" }, 400);
});
