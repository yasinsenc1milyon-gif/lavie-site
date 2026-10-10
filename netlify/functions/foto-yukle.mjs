// Çift panelinden galeriye fotoğraf yükleme (tarayıcı fotoğrafı önceden küçültür)
import { FOTO_SINIR, ciftGetir, fotoListesi, fotoStore, json, kimlikYap, ornekMi } from "../lib/ortak.mjs";

const TURLER = ["image/jpeg", "image/png", "image/webp"];
const MAKS = 3 * 1024 * 1024;

export default async (req) => {
  if (req.method !== "POST") return json({ ok: false, hata: "yontem" }, 405);
  const p = new URL(req.url).searchParams;
  const c = await ciftGetir(p.get("c"));
  if (!c || c.durum === "bekliyor") return json({ ok: false, hata: "bulunamadi" }, 404);
  if (!p.get("k") || p.get("k") !== c.anahtar) return json({ ok: false, hata: "anahtar" }, 403);
  if (ornekMi(c.slug)) return json({ ok: false, hata: "ornek" }, 400);
  const tur = (req.headers.get("content-type") || "").split(";")[0].trim();
  if (!TURLER.includes(tur)) return json({ ok: false, hata: "tur" }, 400);
  const veri = await req.arrayBuffer();
  if (!veri.byteLength || veri.byteLength > MAKS) return json({ ok: false, hata: "boyut" }, 400);
  if ((await fotoListesi(c.slug)).length >= FOTO_SINIR) return json({ ok: false, hata: "sinir" }, 400);
  const id = kimlikYap();
  await fotoStore().set(`${c.slug}/${id}`, veri, { metadata: { tur } });
  return json({ ok: true, id });
};

export const config = { path: "/api/foto-yukle" };
