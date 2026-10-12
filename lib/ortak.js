// Lavie API ortak yardımcıları (Cloudflare Pages Functions + D1)

export const TASARIMLAR = ["zeytin", "pamuk", "papatya", "gece", "seftali", "lavanta", "gul", "nane", "ege", "mono"];
export const TURLER = ["Düğün", "Nişan", "Kına", "Söz"];
export const DURUMLAR = ["bekliyor", "aktif", "kapali"];
export const MUZIKLER = ["piyano", "kirlar", "yok"];
export const YAZILAR = ["", "el", "zarif", "klasik", "modern", "bodoni", "sade"];
export const ALANLAR = ["tasarim", "tur", "gelin", "damat", "tarih", "saat", "mekan", "adres", "konum", "aile", "not", "program", "telefon", "paket", "muzik", "yazi", "katilimNotu"];
export const CIFT_DUZENLER = ALANLAR.filter(k => k !== "telefon" && k !== "paket");

export const json = (o, status = 200) =>
  new Response(JSON.stringify(o), { status, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" } });

export async function govde(req) {
  try { const d = await req.json(); return d && typeof d === "object" ? d : null; } catch { return null; }
}

// Her uç noktayı sarar: veritabanını hazırlar, beklenmeyen hatada JSON döner
export function uc(fn) {
  return async (ctx) => {
    try {
      const db = await veritabani(ctx.env);
      // Cloudflare bağlam nesnesinin alanları yayılarak (...) kopyalanamıyor; tek tek aktarılır
      return await fn({ request: ctx.request, env: ctx.env, params: ctx.params, next: ctx.next, waitUntil: ctx.waitUntil, db });
    } catch (e) {
      console.error("lavie", e && (e.stack || e.message || e));
      return json({ ok: false, hata: e && e.message === "db_yok" ? "veritabani_bagli_degil" : "sunucu" }, 500);
    }
  };
}

// --- Veritabanı (D1) ---
const SEMA = [
  `CREATE TABLE IF NOT EXISTS ciftler (slug TEXT PRIMARY KEY, durum TEXT NOT NULL, veri TEXT NOT NULL, olusturma TEXT NOT NULL)`,
  `CREATE TABLE IF NOT EXISTS yanitlar (id INTEGER PRIMARY KEY AUTOINCREMENT, slug TEXT NOT NULL, isim TEXT NOT NULL, kisi INTEGER NOT NULL, durum TEXT NOT NULL, zaman TEXT NOT NULL)`,
  `CREATE INDEX IF NOT EXISTS yanitlar_slug ON yanitlar(slug)`,
  `CREATE TABLE IF NOT EXISTS mesajlar (id INTEGER PRIMARY KEY AUTOINCREMENT, slug TEXT NOT NULL, isim TEXT NOT NULL, mesaj TEXT NOT NULL, zaman TEXT NOT NULL)`,
  `CREATE INDEX IF NOT EXISTS mesajlar_slug ON mesajlar(slug)`,
  `CREATE TABLE IF NOT EXISTS yorumlar (slug TEXT PRIMARY KEY, ad TEXT NOT NULL, tur TEXT NOT NULL, puan INTEGER NOT NULL, yorum TEXT NOT NULL, onay INTEGER NOT NULL DEFAULT 0, zaman TEXT NOT NULL)`,
  `CREATE TABLE IF NOT EXISTS odemeler (siparis_id TEXT PRIMARY KEY, slug TEXT NOT NULL, tutar TEXT, zaman TEXT NOT NULL)`,
  `CREATE TABLE IF NOT EXISTS ayarlar (anahtar TEXT PRIMARY KEY, deger TEXT NOT NULL)`
];
let hazir = null;
export async function veritabani(env) {
  const db = env && env.DB;
  if (!db) throw new Error("db_yok");
  if (!hazir) hazir = db.batch(SEMA.map(s => db.prepare(s))).catch(e => { hazir = null; throw e; });
  await hazir;
  return db;
}

export function temizle(d) {
  const o = {};
  for (const k of ALANLAR) {
    const sinir = k === "not" || k === "program" ? 600 : k === "katilimNotu" ? 240 : 200;
    o[k] = String(d?.[k] ?? "").trim().slice(0, sinir);
  }
  if (!TASARIMLAR.includes(o.tasarim)) o.tasarim = "zeytin";
  if (!TURLER.includes(o.tur)) o.tur = "Düğün";
  if (o.muzik === "kutu" || !MUZIKLER.includes(o.muzik)) o.muzik = "piyano";
  if (!YAZILAR.includes(o.yazi)) o.yazi = "";
  return o;
}

// "Ayşe & Çağrı" -> "ayse-cagri"
export function slugYap(s) {
  const harf = { "Ç": "c", "ç": "c", "Ğ": "g", "ğ": "g", "I": "i", "ı": "i", "İ": "i", "Ö": "o", "ö": "o", "Ş": "s", "ş": "s", "Ü": "u", "ü": "u", "Â": "a", "â": "a", "Î": "i", "î": "i", "Û": "u", "û": "u" };
  return String(s || "").replace(/[ÇçĞğIıİÖöŞşÜüÂâÎîÛû]/g, c => harf[c]).toLowerCase()
    .replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 40);
}

export const anahtarYap = () => crypto.randomUUID().replace(/-/g, "").slice(0, 12);

// Vitrinde ve tanıtımda gösterilen örnek davetiye (veritabanında tutulmaz)
export const ORNEK = {
  slug: "ornek", anahtar: "ornek", durum: "aktif", tasarim: "zeytin", tur: "Düğün",
  gelin: "Elif", damat: "Burak", tarih: "2027-06-12", saat: "19:30",
  mekan: "Dragos Kır Bahçesi", adres: "Orhantepe Mah., Kartal / İstanbul", konum: "",
  aile: "Yılmaz ve Demir aileleri",
  not: "Hayatımızın en güzel gününde sizleri de aramızda görmekten mutluluk duyarız.",
  program: "19:30 Karşılama\n20:00 Nikâh töreni\n20:30 Akşam yemeği\n22:00 Eğlence",
  telefon: "", paket: "site-gorsel", muzik: "piyano", yazi: "", katilimNotu: ""
};
export const ornekMi = slug => slug === "ornek";
export const slugOku = v => String(v || "").toLowerCase().trim().slice(0, 60);

export async function ciftGetir(db, slug) {
  slug = slugOku(slug);
  if (!slug) return null;
  if (slug === "ornek" || slug === "elif-burak") return { ...ORNEK };
  const r = await db.prepare("SELECT veri, durum FROM ciftler WHERE slug = ?").bind(slug).first();
  if (!r) return null;
  const c = JSON.parse(r.veri);
  c.durum = r.durum;
  if (!c.muzik || c.muzik === "kutu") c.muzik = "piyano";
  return c;
}

export async function ciftKaydet(db, c) {
  await db.prepare("INSERT INTO ciftler (slug, durum, veri, olusturma) VALUES (?, ?, ?, ?) ON CONFLICT(slug) DO UPDATE SET durum = excluded.durum, veri = excluded.veri")
    .bind(c.slug, c.durum, JSON.stringify(c), c.olusturma || new Date().toISOString()).run();
}

export async function yanitlariGetir(db, slug) {
  const { results } = await db.prepare("SELECT id, isim, kisi, durum, zaman FROM yanitlar WHERE slug = ? ORDER BY zaman DESC, id DESC").bind(slug).all();
  return results || [];
}
export async function mesajlariGetir(db, slug) {
  const { results } = await db.prepare("SELECT id, isim, mesaj, zaman FROM mesajlar WHERE slug = ? ORDER BY zaman DESC, id DESC").bind(slug).all();
  return (results || []).map(m => ({ ...m, id: String(m.id) }));
}

export async function ciftVerisiniSil(db, slug) {
  await db.batch([
    db.prepare("DELETE FROM ciftler WHERE slug = ?").bind(slug),
    db.prepare("DELETE FROM yanitlar WHERE slug = ?").bind(slug),
    db.prepare("DELETE FROM mesajlar WHERE slug = ?").bind(slug),
    db.prepare("DELETE FROM yorumlar WHERE slug = ?").bind(slug)
  ]);
}

export function linkler(req, c) {
  const kok = new URL(req.url).origin;
  return { davetiye: `${kok}/d?c=${c.slug}`, panel: `${kok}/panel?c=${c.slug}&k=${c.anahtar}` };
}

export const yorumSatiri = y => y && ({ ...y, onay: !!y.onay });
