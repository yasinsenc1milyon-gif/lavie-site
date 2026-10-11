// Misafirin katılım yanıtını kaydeder
import { ciftGetir, govde, json, ornekMi, uc } from "../../lib/ortak.js";

export const onRequestPost = uc(async ({ request, db }) => {
  const d = await govde(request);
  if (!d) return json({ ok: false, hata: "veri" }, 400);
  const c = await ciftGetir(db, d.c);
  if (!c || c.durum !== "aktif") return json({ ok: false, hata: "bulunamadi" }, 404);
  const isim = String(d.isim || "").trim().slice(0, 80);
  if (!isim) return json({ ok: false, hata: "isim" }, 400);
  const katilacak = d.durum === "Katılacak";
  const kisi = katilacak ? Math.min(Math.max(parseInt(d.kisi, 10) || 1, 1), 20) : 0;
  // örnek davetiyedeki yanıtlar saklanmaz
  if (!ornekMi(c.slug)) {
    await db.prepare("INSERT INTO yanitlar (slug, isim, kisi, durum, zaman) VALUES (?, ?, ?, ?, ?)")
      .bind(c.slug, isim, kisi, katilacak ? "Katılacak" : "Katılamayacak", new Date().toISOString()).run();
  }
  return json({ ok: true });
});
