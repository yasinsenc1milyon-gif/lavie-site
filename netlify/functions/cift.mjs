// Misafirin gördüğü davetiye bilgileri (yalnızca onaylı çiftler)
import { ciftGetir, json } from "../lib/ortak.mjs";

export default async (req) => {
  const c = await ciftGetir(new URL(req.url).searchParams.get("c"));
  if (!c || c.durum !== "aktif") return json({ ok: false, hata: "bulunamadi" }, 404);
  const { anahtar, durum, telefon, paket, olusturma, ...acik } = c;
  return json({ ok: true, cift: acik });
};

export const config = { path: "/api/cift" };
