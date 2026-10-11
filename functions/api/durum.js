// Kurulum kontrolü: veritabanı bağlı mı, yönetim şifresi tanımlı mı (gizli bilgi göstermez)
import { json, veritabani } from "../../lib/ortak.js";

export async function onRequestGet({ env }) {
  const sonuc = { veritabani_tanimli: !!(env && env.DB), sifre_tanimli: !!(env && env.ADMIN_SIFRE), veritabani_calisiyor: false, hata: null };
  try {
    const db = await veritabani(env);
    const r = await db.prepare("SELECT COUNT(*) AS n FROM ciftler").first();
    sonuc.veritabani_calisiyor = true;
    sonuc.cift_sayisi = r ? r.n : 0;
  } catch (e) {
    sonuc.hata = String((e && e.message) || e).slice(0, 300);
  }
  return json({ ok: sonuc.veritabani_calisiyor && sonuc.sifre_tanimli, ...sonuc });
}
