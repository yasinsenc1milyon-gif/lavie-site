/**
 * LAVIE · Google E-Tablolar arka ucu
 * Bu kodu E-Tablo > Uzantılar > Apps Script içine yapıştır.
 * Önce "kurulum" fonksiyonunu bir kez çalıştır, sonra Web uygulaması olarak dağıt.
 */
const CIFTLER = "Ciftler";
const YANITLAR = "Yanitlar";
const SUTUNLAR = ["slug", "anahtar", "tasarim", "tur", "gelin", "damat", "tarih", "saat", "mekan", "adres", "konum", "aile", "not", "program", "aktif"];
const EK_SUTUNLAR = ["davetiye_linki", "panel_linki", "siparis_zamani"];
const SITE = "https://laviedavetiye.netlify.app";
const TASARIMLAR = ["zeytin", "gece", "gul", "mono", "ege"];
const TURLER = ["Düğün", "Nişan", "Kına", "Söz"];

function kurulum() {
  const ss = SpreadsheetApp.getActive();
  const c = ss.getSheetByName(CIFTLER) || ss.insertSheet(CIFTLER);
  if (c.getLastRow() === 0) {
    c.appendRow(SUTUNLAR);
    c.getRange("G:H").setNumberFormat("@"); // tarih ve saat düz metin kalsın
    c.appendRow(["elif-burak", yeniAnahtar(), "zeytin", "Düğün", "Elif", "Burak", "2027-06-12", "19:30",
      "Dragos Kır Bahçesi", "Orhantepe Mah., Kartal / İstanbul", "", "Yılmaz ve Demir aileleri",
      "Hayatımızın en güzel gününde sizleri de aramızda görmekten mutluluk duyarız.",
      "19:30 Karşılama\n20:00 Nikâh töreni\n20:30 Akşam yemeği\n22:00 Eğlence", "EVET"]);
    c.setFrozenRows(1);
  }
  const y = ss.getSheetByName(YANITLAR) || ss.insertSheet(YANITLAR);
  if (y.getLastRow() === 0) { y.appendRow(["zaman", "slug", "isim", "kisi", "durum"]); y.setFrozenRows(1); }
}

// Yeni çift eklerken "anahtar" sütununa yazmak için: Çalıştır > yeniAnahtarGoster
function yeniAnahtarGoster() { Logger.log(yeniAnahtar()); }
function yeniAnahtar() { return Utilities.getUuid().replace(/-/g, "").slice(0, 12); }

function bicim(v, ad) {
  if (v instanceof Date) return Utilities.formatDate(v, Session.getScriptTimeZone(), ad === "saat" ? "HH:mm" : "yyyy-MM-dd");
  return String(v == null ? "" : v).trim();
}

function ciftBul(slug) {
  slug = String(slug || "").toLowerCase().trim();
  if (!slug) return null;
  const v = SpreadsheetApp.getActive().getSheetByName(CIFTLER).getDataRange().getValues();
  const h = v.shift().map(x => String(x).trim());
  for (const r of v) {
    const o = {};
    h.forEach((k, i) => o[k] = bicim(r[i], k));
    const durum = o.aktif.toUpperCase();
    if (o.slug.toLowerCase() === slug && durum !== "HAYIR" && durum !== "BEKLIYOR") return o;
  }
  return null;
}

function cikti(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }

function doGet(e) {
  const p = (e && e.parameter) || {};
  const c = ciftBul(p.c);
  if (!c) return cikti({ ok: false, hata: "bulunamadi" });

  if (p.islem === "panel") {
    if (!p.k || p.k !== c.anahtar) return cikti({ ok: false, hata: "anahtar" });
    const v = SpreadsheetApp.getActive().getSheetByName(YANITLAR).getDataRange().getValues();
    v.shift();
    const yanitlar = v.filter(r => String(r[1]).toLowerCase() === c.slug.toLowerCase()).map(r => ({
      zaman: r[0] instanceof Date ? r[0].toISOString() : String(r[0]),
      isim: String(r[2]).replace(/^'/, ""), kisi: Number(r[3]) || 0, durum: String(r[4])
    }));
    return cikti({ ok: true, cift: { gelin: c.gelin, damat: c.damat }, yanitlar: yanitlar });
  }

  const acik = Object.assign({}, c);
  delete acik.anahtar; delete acik.aktif;
  return cikti({ ok: true, cift: acik });
}

// Türkçe isimlerden link adı üretir: "Ayşe & Çağrı" -> "ayse-cagri"
function slugYap(s) {
  const harf = { "Ç": "c", "ç": "c", "Ğ": "g", "ğ": "g", "I": "i", "ı": "i", "İ": "i", "Ö": "o", "ö": "o", "Ş": "s", "ş": "s", "Ü": "u", "ü": "u", "Â": "a", "â": "a", "Î": "i", "î": "i", "Û": "u", "û": "u" };
  return String(s || "").replace(/[ÇçĞğIıİÖöŞşÜüÂâÎîÛû]/g, c => harf[c]).toLowerCase()
    .replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 40);
}

// Vitrindeki siparişten çiftin satırını oluşturur (aktif = BEKLIYOR)
function siparisOlustur(d) {
  const gelin = String(d.gelin || "").trim(), damat = String(d.damat || "").trim();
  if (!gelin || !damat) return { ok: false, hata: "isim" };
  const sayfa = SpreadsheetApp.getActive().getSheetByName(CIFTLER);
  const temiz = (v, n) => { v = String(v == null ? "" : v).trim().slice(0, n || 120); return /^[=+\-@]/.test(v) ? "'" + v : v; };
  const kilit = LockService.getScriptLock();
  kilit.waitLock(10000);
  try {
    // başlık satırında ek sütunlar yoksa ekle
    const baslik = sayfa.getRange(1, 1, 1, sayfa.getLastColumn()).getValues()[0].map(x => String(x).trim());
    EK_SUTUNLAR.forEach((ad, i) => { if (baslik[SUTUNLAR.length + i] !== ad) sayfa.getRange(1, SUTUNLAR.length + i + 1).setValue(ad); });

    const son = sayfa.getLastRow();
    const mevcut = new Set(son > 1 ? sayfa.getRange(2, 1, son - 1, 1).getValues().map(r => String(r[0]).toLowerCase()) : []);
    const kok = slugYap(gelin + "-" + damat) || "davetiye";
    let slug = kok, n = 2;
    while (mevcut.has(slug)) slug = kok + "-" + n++;
    const anahtar = yeniAnahtar();
    const davetiye = SITE + "/d.html?c=" + slug;
    const panel = SITE + "/panel.html?c=" + slug + "&k=" + anahtar;

    const satir = SUTUNLAR.map(k => {
      if (k === "slug") return slug;
      if (k === "anahtar") return anahtar;
      if (k === "tasarim") return TASARIMLAR.indexOf(d.tasarim) >= 0 ? d.tasarim : "zeytin";
      if (k === "tur") return TURLER.indexOf(d.tur) >= 0 ? d.tur : "Düğün";
      if (k === "aktif") return "BEKLIYOR";
      return temiz(d[k], k === "not" || k === "program" ? 600 : 200);
    }).concat([davetiye, panel, new Date()]);
    sayfa.appendRow(satir);
    return { ok: true, slug: slug };
  } finally { kilit.releaseLock(); }
}

function doPost(e) {
  let d;
  try { d = JSON.parse(e.postData.contents); } catch (_) { return cikti({ ok: false, hata: "veri" }); }
  if (d.islem === "siparis") return cikti(siparisOlustur(d));
  const c = ciftBul(d.c);
  if (!c) return cikti({ ok: false, hata: "bulunamadi" });
  let isim = String(d.isim || "").trim().slice(0, 80);
  if (!isim) return cikti({ ok: false, hata: "isim" });
  if (/^[=+\-@]/.test(isim)) isim = "'" + isim; // formül olarak çalışmasın
  const katilacak = d.durum === "Katılacak";
  const kisi = katilacak ? Math.min(Math.max(parseInt(d.kisi, 10) || 1, 1), 20) : 0;
  const kilit = LockService.getScriptLock();
  kilit.waitLock(10000);
  try {
    SpreadsheetApp.getActive().getSheetByName(YANITLAR)
      .appendRow([new Date(), c.slug, isim, kisi, katilacak ? "Katılacak" : "Katılamayacak"]);
  } finally { kilit.releaseLock(); }
  return cikti({ ok: true });
}
