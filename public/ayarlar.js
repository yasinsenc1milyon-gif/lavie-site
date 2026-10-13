// ===== LAVIE AYARLARI =====
// Kurulumdan sonra sadece bu dosyayı düzenlemen yeterli.

window.LAVIE_AYAR = {
  // Sitenin kendi sunucu adresi (değiştirme)
  API_URL: "/api",

  // Siparişlerin geleceği WhatsApp numarası: başında 90, boşluksuz
  WHATSAPP: "905051782155",

  // Paketler ve fiyatlar
  PAKETLER: [
    { id: "site", ad: "Davetiye sitesi", aciklama: "Size özel link, geri sayım, program, konum ve katılım formu", fiyat: 500 }
  ],

  // Müşterilerin izniyle eklenen gerçek yorumlar (sadece baş harfler)
  MUSTERI_YORUMLARI: [
    { ad: "B. & Ö.", kaynak: "Instagram yorumu", puan: 5, yorum: "Çok teşekkür ederiz, ilginiz ve nezaketiniz için. Sayenizde davetiyemiz harika oldu." },
    { ad: "A. K.", kaynak: "WhatsApp mesajı", puan: 5, yorum: "Davetiyemize herkes bayılıyor. Sizi öneriyorum." },
    { ad: "A. & R.", kaynak: "Instagram yorumu", puan: 5, yorum: "Çok çok beğendim, her şey için teşekkürler." },
    { ad: "K. & A.", kaynak: "Instagram yorumu", puan: 5, yorum: "İyi ki sen, iyi ki!" }
  ],

  // Instagram kullanıcı adın (@ olmadan)
  INSTAGRAM: "la.viecreative"
};

// Ortaklık kodu: ?ref=fotoahmet ile gelen ziyaretçi 60 gün boyunca bu ortağa sayılır
(function () {
  try {
    const r = new URLSearchParams(location.search).get("ref");
    if (r && /^[a-z0-9_-]{2,40}$/i.test(r)) localStorage.setItem("lavie_ref", JSON.stringify({ k: r.toLowerCase(), t: Date.now() }));
    const v = JSON.parse(localStorage.getItem("lavie_ref") || "null");
    window.LAVIE_REF = v && Date.now() - v.t < 60 * 864e5 ? v.k : "";
  } catch (_) { window.LAVIE_REF = ""; }
})();

// Ziyaret sayacı: çerez yok, kişisel veri yok; yalnızca sayfa, kaynak (Google, Instagram...) ve cihaz türü sayılır
(function () {
  window.lavieOlay = function () {};
  try {
    if (navigator.webdriver || window.top !== window || !navigator.sendBeacon) return;
    let yol = location.pathname.replace(/\.html$/, "").replace(/\/+$/, "") || "/";
    if (/^\/(yonetim|panel)/.test(yol)) return;
    const q = new URLSearchParams(location.search);
    if (yol === "/d") yol = q.get("c") === "ornek" ? "/ornek" : "/d";
    let k = sessionStorage.getItem("lavie_k");
    if (!k) {
      const r = (q.get("ref") || "").toLowerCase(), u = (q.get("utm_source") || "").toLowerCase();
      let h = ""; try { h = new URL(document.referrer).hostname; } catch (_) {}
      if (h === location.hostname) h = "";
      const x = u + " " + h;
      k = /^d-/.test(r) ? "davetiye" : r ? "ortak" : /instagram/.test(x) ? "instagram" : /google/.test(x) ? "google" : /bing/.test(x) ? "bing"
        : /yandex/.test(x) ? "yandex" : /facebook|fb\./.test(x) ? "facebook" : /tiktok/.test(x) ? "tiktok" : /pinterest/.test(x) ? "pinterest"
        : /whatsapp|wa\.me/.test(x) ? "whatsapp" : h ? "diger" : yol === "/d" ? "davetiye" : "dogrudan";
      sessionStorage.setItem("lavie_k", k);
    }
    const bugun = new Date().toDateString(); let n = 0;
    try { if (localStorage.getItem("lavie_g") !== bugun) { localStorage.setItem("lavie_g", bugun); n = 1; } } catch (_) {}
    const m = /Mobi|Android|iPhone/i.test(navigator.userAgent) ? 1 : 0;
    const gonder = (o, yeni) => { try { navigator.sendBeacon("/api/ziyaret", JSON.stringify({ y: yol, k, o, n: yeni ? 1 : 0, m })); } catch (_) {} };
    const bir = {};
    window.lavieOlay = o => { try { if (bir[o] || sessionStorage.getItem("lavie_o_" + o)) return; bir[o] = 1; sessionStorage.setItem("lavie_o_" + o, "1"); } catch (_) {} gonder(o, 0); };
    gonder("g", n);
  } catch (_) {}
})();
