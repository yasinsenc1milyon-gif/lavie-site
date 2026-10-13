// Basit, çerezsiz ziyaret sayacı: sayfalardan gelen işaretleri gün/sayfa/kaynak bazında toplar.
// Kişisel veri (IP, isim, davetiye adresi) saklanmaz; yalnızca sayılar tutulur.
import { uc, json } from "../../lib/ortak.js";

const KAYNAKLAR = ["google", "bing", "yandex", "instagram", "facebook", "tiktok", "pinterest", "whatsapp", "davetiye", "ortak", "diger", "dogrudan"];
const OLAYLAR = ["g", "dene", "olustur"];
const BOT = /bot|crawl|spider|slurp|facebookexternalhit|whatsapp|preview|headless|lighthouse/i;

export const gunAnahtari = (t = Date.now()) => new Date(t + 3 * 3600e3).toISOString().slice(0, 10); // İstanbul günü

export const onRequestPost = uc(async ({ request, db }) => {
  if (BOT.test(request.headers.get("user-agent") || "")) return new Response(null, { status: 204 });
  let d = null;
  try { d = JSON.parse((await request.text()).slice(0, 500)); } catch {}
  if (!d || typeof d !== "object") return json({ ok: false }, 400);
  let yol = String(d.y || "/").toLowerCase();
  if (!/^\/[a-z0-9\-/]{0,70}$/.test(yol)) yol = "/diger";
  const kaynak = KAYNAKLAR.includes(d.k) ? d.k : "diger";
  const olay = OLAYLAR.includes(d.o) ? d.o : null;
  if (!olay) return json({ ok: false }, 400);
  await db.prepare(`INSERT INTO ziyaretler (gun, yol, kaynak, olay, yeni, mobil, adet) VALUES (?, ?, ?, ?, ?, ?, 1)
    ON CONFLICT(gun, yol, kaynak, olay, yeni, mobil) DO UPDATE SET adet = adet + 1`)
    .bind(gunAnahtari(), yol, kaynak, olay, d.n ? 1 : 0, d.m ? 1 : 0).run();
  return new Response(null, { status: 204 });
});

// Yönetim paneli için özet
export async function trafikOzeti(db, gun) {
  gun = [1, 7, 30].includes(Number(gun)) ? Number(gun) : 7;
  const bas = gunAnahtari(Date.now() - (gun - 1) * 864e5), bas30 = gunAnahtari(Date.now() - 29 * 864e5);
  const basIso = new Date(Date.now() - gun * 864e5).toISOString();
  const [gunluk, sayfalar, kaynaklar, olaylar, cihaz, sip] = await db.batch([
    db.prepare(`SELECT gun, SUM(CASE WHEN olay='g' THEN adet ELSE 0 END) AS g, SUM(CASE WHEN olay='g' AND yeni=1 THEN adet ELSE 0 END) AS z,
      SUM(CASE WHEN olay='g' AND yeni=1 AND yol<>'/d' THEN adet ELSE 0 END) AS v FROM ziyaretler WHERE gun >= ? GROUP BY gun ORDER BY gun`).bind(bas30),
    db.prepare(`SELECT yol, SUM(adet) AS g FROM ziyaretler WHERE olay='g' AND gun >= ? GROUP BY yol ORDER BY g DESC LIMIT 12`).bind(bas),
    db.prepare(`SELECT kaynak, SUM(adet) AS z FROM ziyaretler WHERE olay='g' AND yeni=1 AND yol<>'/d' AND gun >= ? GROUP BY kaynak ORDER BY z DESC`).bind(bas),
    db.prepare(`SELECT olay, SUM(adet) AS n FROM ziyaretler WHERE olay<>'g' AND gun >= ? GROUP BY olay`).bind(bas),
    db.prepare(`SELECT mobil, SUM(adet) AS z FROM ziyaretler WHERE olay='g' AND yeni=1 AND gun >= ? GROUP BY mobil`).bind(bas),
    db.prepare(`SELECT durum, COUNT(*) AS n FROM ciftler WHERE slug <> 'ornek' AND olusturma >= ? GROUP BY durum`).bind(basIso)
  ]);
  const r = x => x.results || [];
  return {
    gun, bugun: gunAnahtari(),
    gunluk: r(gunluk), sayfalar: r(sayfalar), kaynaklar: r(kaynaklar),
    olaylar: Object.fromEntries(r(olaylar).map(o => [o.olay, o.n])),
    mobil: Object.fromEntries(r(cihaz).map(o => [o.mobil ? "mobil" : "masaustu", o.z])),
    siparis: Object.fromEntries(r(sip).map(o => [o.durum, o.n]))
  };
}
