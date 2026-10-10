// Çiftin galerisindeki bir fotoğrafı gösterir
import { ciftGetir, fotoStore } from "../lib/ortak.mjs";

export default async (req) => {
  const p = new URL(req.url).searchParams;
  const c = await ciftGetir(p.get("c"));
  const id = String(p.get("id") || "");
  if (!c || c.durum !== "aktif" || !/^[\w-]{1,80}$/.test(id)) return new Response("Bulunamadı", { status: 404 });
  const sonuc = await fotoStore().getWithMetadata(`${c.slug}/${id}`, { type: "arrayBuffer" });
  if (!sonuc) return new Response("Bulunamadı", { status: 404 });
  return new Response(sonuc.data, {
    headers: { "content-type": sonuc.metadata?.tur || "image/jpeg", "cache-control": "public, max-age=86400" }
  });
};

export const config = { path: "/api/foto" };
