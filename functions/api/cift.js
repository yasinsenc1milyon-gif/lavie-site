// Misafirin gördüğü davetiye bilgileri (yalnızca onaylı çiftler) ve hatıra defteri
import { ciftGetir, json, mesajlariGetir, uc } from "../../lib/ortak.js";

export const onRequestGet = uc(async ({ request, db }) => {
  const c = await ciftGetir(db, new URL(request.url).searchParams.get("c"));
  if (!c || c.durum !== "aktif") return json({ ok: false, hata: "bulunamadi" }, 404);
  const { anahtar, durum, telefon, paket, olusturma, ...acik } = c;
  const mesajlar = await mesajlariGetir(db, c.slug);
  return json({ ok: true, cift: acik, mesajlar: mesajlar.slice(0, 100).map(({ isim, mesaj, zaman }) => ({ isim, mesaj, zaman })) });
});
