// Anı albümü: misafirler fotoğraf/video yükler (parça parça), yalnızca çift görür
import { ALBUM, ALBUM_TURLER, albumListesi, albumStore, albumVeriStore, ciftGetir, govde, json, kimlikYap, ornekMi } from "../lib/ortak.mjs";

const gecerliId = id => /^[\w-]{1,80}$/.test(String(id || ""));
const ozetAnahtar = slug => `_ozet/${slug}`;

async function ozetGetir(slug) { return (await albumStore().get(ozetAnahtar(slug), { type: "json" })) || { adet: 0, boyut: 0 }; }
async function ozetYaz(slug, o) { await albumStore().setJSON(ozetAnahtar(slug), { adet: Math.max(0, o.adet), boyut: Math.max(0, o.boyut) }); }

export default async (req) => {
  const p = new URL(req.url).searchParams;
  const islemQ = p.get("islem");

  // --- Misafir: dosya parçası yükleme (ham veri)
  if (req.method === "POST" && islemQ === "parca") {
    const c = await ciftGetir(p.get("c"));
    if (!c || c.durum !== "aktif") return json({ ok: false, hata: "bulunamadi" }, 404);
    const id = p.get("id"), i = parseInt(p.get("i"), 10);
    if (!gecerliId(id) || !(i >= 0)) return json({ ok: false, hata: "veri" }, 400);
    const meta = await albumStore().get(`${c.slug}/${id}`, { type: "json" });
    if (!meta || meta.tamam || i >= meta.parca) return json({ ok: false, hata: "veri" }, 400);
    const veri = await req.arrayBuffer();
    if (!veri.byteLength || veri.byteLength > ALBUM.parca) return json({ ok: false, hata: "boyut" }, 400);
    await albumVeriStore().set(`${c.slug}/${id}/${i}`, veri);
    return json({ ok: true });
  }

  if (req.method === "POST") {
    const d = await govde(req);
    if (!d) return json({ ok: false, hata: "veri" }, 400);
    const c = await ciftGetir(d.c);
    if (!c || c.durum !== "aktif") return json({ ok: false, hata: "bulunamadi" }, 404);

    // --- Misafir: yüklemeyi başlat
    if (d.islem === "baslat") {
      if (ornekMi(c.slug)) return json({ ok: false, hata: "ornek" }, 400);
      const tur = d.tur === "video" ? "video" : "foto";
      const mime = String(d.mime || "").toLowerCase();
      const boyut = Number(d.boyut) || 0;
      if (!ALBUM_TURLER[tur].includes(mime)) return json({ ok: false, hata: "tur" }, 400);
      if (boyut <= 0 || boyut > (tur === "video" ? ALBUM.videoMaks : ALBUM.fotoMaks)) return json({ ok: false, hata: "boyut" }, 400);
      const oz = await ozetGetir(c.slug);
      if (oz.adet >= ALBUM.adetMaks || oz.boyut + boyut > ALBUM.toplamMaks) return json({ ok: false, hata: "dolu" }, 400);
      const id = kimlikYap();
      const meta = { id, tur, mime, boyut, parca: Math.ceil(boyut / ALBUM.parca), isim: String(d.isim || "").trim().slice(0, 60), zaman: new Date().toISOString(), tamam: false };
      await albumStore().setJSON(`${c.slug}/${id}`, meta);
      await ozetYaz(c.slug, { adet: oz.adet + 1, boyut: oz.boyut + boyut });
      return json({ ok: true, id, parcaBoyutu: ALBUM.parca, parca: meta.parca });
    }

    // --- Misafir: yüklemeyi bitir
    if (d.islem === "bitir") {
      if (!gecerliId(d.id)) return json({ ok: false, hata: "veri" }, 400);
      const s = albumStore(), k = `${c.slug}/${d.id}`;
      const meta = await s.get(k, { type: "json" });
      if (!meta) return json({ ok: false, hata: "bulunamadi" }, 404);
      const { blobs } = await albumVeriStore().list({ prefix: k + "/" });
      if (blobs.length !== meta.parca) return json({ ok: false, hata: "eksik" }, 400);
      meta.tamam = true;
      await s.setJSON(k, meta);
      return json({ ok: true });
    }

    // --- Çift: dosya sil
    if (d.islem === "sil") {
      if (!d.k || d.k !== c.anahtar || !gecerliId(d.id)) return json({ ok: false, hata: "anahtar" }, 403);
      const k = `${c.slug}/${d.id}`;
      const meta = await albumStore().get(k, { type: "json" });
      if (meta) {
        const vs = albumVeriStore();
        const { blobs } = await vs.list({ prefix: k + "/" });
        await Promise.all(blobs.map(b => vs.delete(b.key)));
        await albumStore().delete(k);
        const oz = await ozetGetir(c.slug);
        await ozetYaz(c.slug, { adet: oz.adet - 1, boyut: oz.boyut - meta.boyut });
      }
      return json({ ok: true });
    }
    return json({ ok: false, hata: "islem" }, 400);
  }

  if (req.method === "GET") {
    const c = await ciftGetir(p.get("c"));
    if (!c || c.durum === "bekliyor") return json({ ok: false, hata: "bulunamadi" }, 404);
    if (!p.get("k") || p.get("k") !== c.anahtar) return json({ ok: false, hata: "anahtar" }, 403);

    // --- Çift: albüm listesi
    if (islemQ === "liste") {
      const liste = await albumListesi(c.slug);
      const oz = await ozetGetir(c.slug);
      return json({ ok: true, ogeler: liste.map(({ id, tur, mime, boyut, parca, isim, zaman }) => ({ id, tur, mime, boyut, parca, isim, zaman })), ozet: oz, sinir: { toplam: ALBUM.toplamMaks } });
    }
    // --- Çift: dosya parçası indir
    if (islemQ === "dosya") {
      const id = p.get("id"), i = parseInt(p.get("i") || "0", 10);
      if (!gecerliId(id) || !(i >= 0)) return new Response("Bulunamadı", { status: 404 });
      const meta = await albumStore().get(`${c.slug}/${id}`, { type: "json" });
      if (!meta) return new Response("Bulunamadı", { status: 404 });
      const veri = await albumVeriStore().get(`${c.slug}/${id}/${i}`, { type: "arrayBuffer" });
      if (!veri) return new Response("Bulunamadı", { status: 404 });
      return new Response(veri, { headers: { "content-type": meta.parca === 1 ? meta.mime : "application/octet-stream", "cache-control": "private, max-age=86400" } });
    }
  }
  return json({ ok: false, hata: "yontem" }, 405);
};

export const config = { path: "/api/album" };
