// Vitrinden gelen sipariş: çiftin davetiyesini "bekliyor" durumunda oluşturur
import { anahtarYap, govde, json, slugYap, temizle, uc } from "../../lib/ortak.js";

import { odemeAcik } from "../../lib/odeme.js";

export const onRequestPost = uc(async ({ request, env, db }) => {
  const d = await govde(request);
  if (!d) return json({ ok: false, hata: "veri" }, 400);
  const a = temizle(d);
  const ref = /^[a-z0-9_-]{2,40}$/i.test(String(d.ref || "")) ? String(d.ref).toLowerCase() : "";
  if (!a.gelin || !a.damat || !a.tarih) return json({ ok: false, hata: "eksik" }, 400);

  const kok = slugYap(`${a.gelin}-${a.damat}`) || "davetiye";
  for (let n = 1; n <= 200; n++) {
    const slug = n === 1 ? kok : `${kok}-${n}`;
    if (slug === "ornek" || slug === "elif-burak") continue;
    const c = { ...a, slug, anahtar: anahtarYap(), durum: "bekliyor", olusturma: new Date().toISOString(), ...(ref ? { ref } : {}) };
    const r = await db.prepare("INSERT OR IGNORE INTO ciftler (slug, durum, veri, olusturma) VALUES (?, ?, ?, ?)")
      .bind(slug, c.durum, JSON.stringify(c), c.olusturma).run();
    if (r.meta && r.meta.changes === 1) return json({ ok: true, slug, k: c.anahtar, kart: odemeAcik(env) ? env.SHOPIER_URUN_URL : null });
  }
  return json({ ok: false, hata: "dolu" }, 500);
});
