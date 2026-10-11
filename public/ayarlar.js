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
