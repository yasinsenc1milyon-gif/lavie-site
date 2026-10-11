// Hatıra defteri: misafir çifte mesaj bırakır
import { ciftGetir, govde, json, ornekMi, uc } from "../../lib/ortak.js";

export const onRequestPost = uc(async ({ request, db }) => {
  const d = await govde(request);
  if (!d) return json({ ok: false, hata: "veri" }, 400);
  const c = await ciftGetir(db, d.c);
  if (!c || c.durum !== "aktif") return json({ ok: false, hata: "bulunamadi" }, 404);
  const isim = String(d.isim || "").trim().slice(0, 60);
  const mesaj = String(d.mesaj || "").trim().slice(0, 400);
  if (!isim || !mesaj) return json({ ok: false, hata: "eksik" }, 400);
  const kayit = { isim, mesaj, zaman: new Date().toISOString() };
  // örnek davetiyede mesajlar saklanmaz
  if (!ornekMi(c.slug)) {
    await db.prepare("INSERT INTO mesajlar (slug, isim, mesaj, zaman) VALUES (?, ?, ?, ?)").bind(c.slug, isim, mesaj, kayit.zaman).run();
  }
  return json({ ok: true, mesaj: kayit });
});
