// Misafirin gördüğü davetiye bilgileri (yalnızca onaylı çiftler) ve hatıra defteri
import { ciftGetir, json, mesajlariGetir } from "../lib/ortak.mjs";

export default async (req) => {
  const c = await ciftGetir(new URL(req.url).searchParams.get("c"));
  if (!c || c.durum !== "aktif") return json({ ok: false, hata: "bulunamadi" }, 404);
  const { anahtar, durum, telefon, paket, olusturma, ...acik } = c;
  const mesajlar = await mesajlariGetir(c.slug);
  return json({ ok: true, cift: acik, mesajlar: mesajlar.slice(0, 100).map(({ isim, mesaj, zaman }) => ({ isim, mesaj, zaman })) });
};

export const config = { path: "/api/cift" };
