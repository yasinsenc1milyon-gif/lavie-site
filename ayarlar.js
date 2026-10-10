// ===== LAVIE AYARLARI =====
// Kurulumdan sonra sadece bu dosyayı düzenlemen yeterli.

window.LAVIE_AYAR = {
  // Google Apps Script "Web uygulaması" adresi (KURULUM.txt, 2. adım)
  API_URL: "BURAYA_APPS_SCRIPT_LINKI",

  // Siparişlerin geleceği WhatsApp numarası: başında 90, boşluksuz
  WHATSAPP: "905XXXXXXXXX",

  // Paketler ve fiyatlar
  PAKETLER: [
    { id: "site", ad: "Davetiye sitesi", aciklama: "Size özel link, geri sayım, program, konum ve katılım formu", fiyat: 549 },
    { id: "site-gorsel", ad: "Site + paylaşım görseli", aciklama: "Siteye ek olarak WhatsApp/Instagram için davetiye görseli", fiyat: 699 }
  ],

  // Instagram kullanıcı adın (@ olmadan)
  INSTAGRAM: "lavie.davetiye"
};
