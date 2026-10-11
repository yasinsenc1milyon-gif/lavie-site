// Vitrindeki gerçek sayılar: yayındaki davetiye ve toplanan katılım yanıtı (örnek davetiye hariç)
import { json, uc } from "../../lib/ortak.js";

export const onRequestGet = uc(async ({ db }) => {
  const a = await db.prepare("SELECT COUNT(*) AS n FROM ciftler WHERE durum = 'aktif' AND slug <> 'ornek'").first();
  const y = await db.prepare("SELECT COUNT(*) AS n, COALESCE(SUM(CASE WHEN kisi > 0 THEN kisi ELSE 1 END), 0) AS k FROM yanitlar WHERE slug <> 'ornek'").first();
  return json({ ok: true, davetiye: a ? a.n : 0, yanit: y ? y.n : 0, misafir: y ? y.k : 0 });
});
