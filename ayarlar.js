// ===== LAVIE AYARLARI =====
// Kurulumdan sonra sadece bu dosyayı düzenlemen yeterli.

window.LAVIE_AYAR = {
  // Google Apps Script "Web uygulaması" adresi (KURULUM.txt, 2. adım)
  API_URL: "https://script.google.com/macros/s/AKfycbxaxE5lCN8DYyB_-JFqfVmIOhNwvgQFyZxtkswmkpy7Kc3GKzbD3wDyM8gEABXKRmMYew/exec",

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
