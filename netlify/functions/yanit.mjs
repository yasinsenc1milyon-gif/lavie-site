// Misafirin katılım yanıtını kaydeder
import { ciftGetir, govde, json, yanitStore } from "../lib/ortak.mjs";

export default async (req) => {
  if (req.method !== "POST") return json({ ok: false, hata: "yontem" }, 405);
  const d = await govde(req);
  if (!d) return json({ ok: false, hata: "veri" }, 400);
  const c = await ciftGetir(d.c);
  if (!c || c.durum !== "aktif") return json({ ok: false, hata: "bulunamadi" }, 404);
  const isim = String(d.isim || "").trim().slice(0, 80);
  if (!isim) return json({ ok: false, hata: "isim" }, 400);
  const katilacak = d.durum === "Katılacak";
  const kisi = katilacak ? Math.min(Math.max(parseInt(d.kisi, 10) || 1, 1), 20) : 0;
  const zaman = new Date().toISOString();
  const anahtar = `${c.slug}/${zaman}-${crypto.randomUUID().slice(0, 8)}`;
  await yanitStore().setJSON(anahtar, { isim, kisi, durum: katilacak ? "Katılacak" : "Katılamayacak", zaman });
  return json({ ok: true });
};

export const config = { path: "/api/yanit" };
