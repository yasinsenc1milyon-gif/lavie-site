// Vitrinden gelen sipariş: çiftin davetiyesini "bekliyor" durumunda oluşturur
import { anahtarYap, govde, json, slugYap, temizle, uc } from "../../lib/ortak.js";

export const onRequestPost = uc(async ({ request, db }) => {
  const d = await govde(request);
  if (!d) return json({ ok: false, hata: "veri" }, 400);
  const a = temizle(d);
  if (!a.gelin || !a.damat || !a.tarih) return json({ ok: false, hata: "eksik" }, 400);

  const kok = slugYap(`${a.gelin}-${a.damat}`) || "davetiye";
  for (let n = 1; n <= 200; n++) {
    const slug = n === 1 ? kok : `${kok}-${n}`;
    if (slug === "ornek" || slug === "elif-burak") continue;
    const c = { ...a, slug, anahtar: anahtarYap(), durum: "bekliyor", olusturma: new Date().toISOString() };
    const r = await db.prepare("INSERT OR IGNORE INTO ciftler (slug, durum, veri, olusturma) VALUES (?, ?, ?, ?)")
      .bind(slug, c.durum, JSON.stringify(c), c.olusturma).run();
    if (r.meta && r.meta.changes === 1) return json({ ok: true, slug });
  }
  return json({ ok: false, hata: "dolu" }, 500);
});
