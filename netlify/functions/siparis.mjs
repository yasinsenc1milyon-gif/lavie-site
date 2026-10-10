// Vitrinden gelen sipariş: çiftin davetiyesini "bekliyor" durumunda oluşturur
import { anahtarYap, ciftStore, govde, json, slugYap, temizle } from "../lib/ortak.mjs";

export default async (req) => {
  if (req.method !== "POST") return json({ ok: false, hata: "yontem" }, 405);
  const d = await govde(req);
  if (!d) return json({ ok: false, hata: "veri" }, 400);
  const a = temizle(d);
  if (!a.gelin || !a.damat || !a.tarih) return json({ ok: false, hata: "eksik" }, 400);

  const store = ciftStore();
  const kok = slugYap(`${a.gelin}-${a.damat}`) || "davetiye";
  let slug = kok;
  for (let n = 2; slug === "ornek" || slug === "elif-burak" || (await store.get(slug)) !== null; n++) {
    slug = `${kok}-${n}`;
    if (n > 200) return json({ ok: false, hata: "dolu" }, 500);
  }
  await store.setJSON(slug, { ...a, slug, anahtar: anahtarYap(), durum: "bekliyor", olusturma: new Date().toISOString() });
  return json({ ok: true, slug });
};

export const config = { path: "/api/siparis" };
