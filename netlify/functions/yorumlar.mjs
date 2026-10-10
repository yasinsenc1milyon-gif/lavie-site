// Ana sayfada gösterilen, yönetimde onaylanmış gerçek çift yorumları
import { json, yorumStore } from "../lib/ortak.mjs";

export default async () => {
  const s = yorumStore();
  const { blobs } = await s.list();
  const hepsi = await Promise.all(blobs.map(b => s.get(b.key, { type: "json" })));
  const yorumlar = hepsi.filter(y => y && y.onay)
    .sort((a, b) => String(b.zaman).localeCompare(String(a.zaman)))
    .slice(0, 12)
    .map(({ ad, tur, puan, yorum, zaman }) => ({ ad, tur, puan, yorum, zaman }));
  return json({ ok: true, yorumlar });
};

export const config = { path: "/api/yorumlar" };
