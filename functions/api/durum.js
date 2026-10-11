// Kurulum kontrolü: veritabanı bağlı mı, yönetim şifresi tanımlı mı (gizli bilgi göstermez)
import { json, mesajlariGetir, veritabani } from "../../lib/ortak.js";

export async function onRequestGet({ env }) {
  const sonuc = { veritabani_tanimli: !!(env && env.DB), sifre_tanimli: !!(env && env.ADMIN_SIFRE), shopier_tanimli: !!(env && env.SHOPIER_PAT), veritabani_calisiyor: false, hata: null };
  try {
    const db = await veritabani(env);
    const r = await db.prepare("SELECT COUNT(*) AS n FROM ciftler").first();
    sonuc.veritabani_calisiyor = true;
    sonuc.cift_sayisi = r ? r.n : 0;
    // tabloları tek tek dene
    sonuc.tablolar = {};
    for (const [ad, q] of [["mesajlar", "SELECT id, isim, mesaj, zaman FROM mesajlar WHERE slug = ? ORDER BY zaman DESC, id DESC"], ["yanitlar", "SELECT id, isim, kisi, durum, zaman FROM yanitlar WHERE slug = ? ORDER BY zaman DESC, id DESC"], ["yorumlar", "SELECT puan, yorum, onay FROM yorumlar WHERE slug = ?"]]) {
      try { const x = await db.prepare(q).bind("ornek").all(); sonuc.tablolar[ad] = "ok:" + (x.results || []).length; }
      catch (e) { sonuc.tablolar[ad] = "hata: " + String((e && e.message) || e).slice(0, 200); }
    }
    try { const l = await mesajlariGetir(db, "ornek"); sonuc.mesajlariGetir = "ok:" + l.length; }
    catch (e) { sonuc.mesajlariGetir = "hata: " + String((e && e.message) || e).slice(0, 200); }
  } catch (e) {
    sonuc.hata = String((e && e.message) || e).slice(0, 300);
  }
  return json({ ok: sonuc.veritabani_calisiyor && sonuc.sifre_tanimli, ...sonuc });
}
