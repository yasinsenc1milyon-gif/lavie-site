/**
 * LAVIE · Google E-Tablolar arka ucu
 * Bu kodu E-Tablo > Uzantılar > Apps Script içine yapıştır.
 * Önce "kurulum" fonksiyonunu bir kez çalıştır, sonra Web uygulaması olarak dağıt.
 */
const CIFTLER = "Ciftler";
const YANITLAR = "Yanitlar";
const SUTUNLAR = ["slug", "anahtar", "tasarim", "tur", "gelin", "damat", "tarih", "saat", "mekan", "adres", "konum", "aile", "not", "program", "aktif"];

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
    if (o.slug.toLowerCase() === slug && o.aktif.toUpperCase() !== "HAYIR") return o;
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

function doPost(e) {
  let d;
  try { d = JSON.parse(e.postData.contents); } catch (_) { return cikti({ ok: false, hata: "veri" }); }
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
