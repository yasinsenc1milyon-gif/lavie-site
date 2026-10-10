// Çiftin misafir paneli: şifreli linkle yanıt listesi
import { ciftGetir, json, yanitlariGetir } from "../lib/ortak.mjs";

export default async (req) => {
  const p = new URL(req.url).searchParams;
  const c = await ciftGetir(p.get("c"));
  if (!c || c.durum === "bekliyor") return json({ ok: false, hata: "bulunamadi" }, 404);
  if (!p.get("k") || p.get("k") !== c.anahtar) return json({ ok: false, hata: "anahtar" }, 403);
  const yanitlar = await yanitlariGetir(c.slug);
  const { anahtar, telefon, olusturma, durum, ...acik } = c;
  return json({ ok: true, cift: acik, yanitlar });
};

export const config = { path: "/api/panel" };
