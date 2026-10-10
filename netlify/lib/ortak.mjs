// Lavie API ortak yardımcıları
import { getStore } from "@netlify/blobs";

export const ciftStore = () => getStore({ name: "ciftler", consistency: "strong" });
export const yanitStore = () => getStore({ name: "yanitlar", consistency: "strong" });

export const TASARIMLAR = ["zeytin", "gece", "gul", "mono", "ege"];
export const TURLER = ["Düğün", "Nişan", "Kına", "Söz"];
export const DURUMLAR = ["bekliyor", "aktif", "kapali"];
export const ALANLAR = ["tasarim", "tur", "gelin", "damat", "tarih", "saat", "mekan", "adres", "konum", "aile", "not", "program", "telefon", "paket"];

export const json = (o, status = 200) =>
  new Response(JSON.stringify(o), { status, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" } });

export async function govde(req) {
  try { const d = await req.json(); return d && typeof d === "object" ? d : null; } catch { return null; }
}

export function temizle(d) {
  const o = {};
  for (const k of ALANLAR) {
    const sinir = k === "not" || k === "program" ? 600 : 200;
    o[k] = String(d?.[k] ?? "").trim().slice(0, sinir);
  }
  if (!TASARIMLAR.includes(o.tasarim)) o.tasarim = "zeytin";
  if (!TURLER.includes(o.tur)) o.tur = "Düğün";
  return o;
}

// "Ayşe & Çağrı" -> "ayse-cagri"
export function slugYap(s) {
  const harf = { "Ç": "c", "ç": "c", "Ğ": "g", "ğ": "g", "I": "i", "ı": "i", "İ": "i", "Ö": "o", "ö": "o", "Ş": "s", "ş": "s", "Ü": "u", "ü": "u", "Â": "a", "â": "a", "Î": "i", "î": "i", "Û": "u", "û": "u" };
  return String(s || "").replace(/[ÇçĞğIıİÖöŞşÜüÂâÎîÛû]/g, c => harf[c]).toLowerCase()
    .replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 40);
}

export const anahtarYap = () => crypto.randomUUID().replace(/-/g, "").slice(0, 12);

// Vitrinde ve Instagram'da gösterilecek örnek davetiye
export const ORNEK = {
  slug: "ornek", anahtar: "ornek", durum: "aktif", tasarim: "zeytin", tur: "Düğün",
  gelin: "Elif", damat: "Burak", tarih: "2027-06-12", saat: "19:30",
  mekan: "Dragos Kır Bahçesi", adres: "Orhantepe Mah., Kartal / İstanbul", konum: "",
  aile: "Yılmaz ve Demir aileleri",
  not: "Hayatımızın en güzel gününde sizleri de aramızda görmekten mutluluk duyarız.",
  program: "19:30 Karşılama\n20:00 Nikâh töreni\n20:30 Akşam yemeği\n22:00 Eğlence",
  telefon: "", paket: "site"
};

export function slugOku(v) { return String(v || "").toLowerCase().trim().slice(0, 60); }

export async function ciftGetir(slug) {
  slug = slugOku(slug);
  if (!slug) return null;
  if (slug === "ornek" || slug === "elif-burak") return ORNEK;
  return await ciftStore().get(slug, { type: "json" });
}

export async function yanitlariGetir(slug) {
  const s = yanitStore();
  const { blobs } = await s.list({ prefix: slug + "/" });
  const liste = await Promise.all(blobs.map(b => s.get(b.key, { type: "json" })));
  return liste.filter(Boolean).sort((a, b) => String(b.zaman).localeCompare(String(a.zaman)));
}

export function linkler(req, c) {
  const kok = new URL(req.url).origin;
  return { davetiye: `${kok}/d.html?c=${c.slug}`, panel: `${kok}/panel.html?c=${c.slug}&k=${c.anahtar}` };
}

export function ortam(ad) {
  try { if (globalThis.Netlify?.env) return Netlify.env.get(ad); } catch {}
  return process.env[ad];
}
