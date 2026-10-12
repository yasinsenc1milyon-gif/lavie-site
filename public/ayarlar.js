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
