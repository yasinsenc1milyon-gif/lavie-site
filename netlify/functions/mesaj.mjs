// Hatıra defteri: misafir çifte mesaj bırakır
import { ciftGetir, govde, json, kimlikYap, mesajStore, ornekMi } from "../lib/ortak.mjs";

export default async (req) => {
  if (req.method !== "POST") return json({ ok: false, hata: "yontem" }, 405);
  const d = await govde(req);
  if (!d) return json({ ok: false, hata: "veri" }, 400);
  const c = await ciftGetir(d.c);
  if (!c || c.durum !== "aktif") return json({ ok: false, hata: "bulunamadi" }, 404);
  const isim = String(d.isim || "").trim().slice(0, 60);
  const mesaj = String(d.mesaj || "").trim().slice(0, 400);
  if (!isim || !mesaj) return json({ ok: false, hata: "eksik" }, 400);
  const kayit = { isim, mesaj, zaman: new Date().toISOString() };
  // örnek davetiyede mesajlar kalıcı olarak saklanmaz
  if (!ornekMi(c.slug)) await mesajStore().setJSON(`${c.slug}/${kimlikYap()}`, kayit);
  return json({ ok: true, mesaj: kayit });
};

export const config = { path: "/api/mesaj" };
