# Davet türü sayfalarını üretir: python3 araclar/tur_sayfalari.py  (public/ içine yazar)
import json, html, os
U = "https://www.laviedavetiye.workers.dev"
KOK = os.path.join(os.path.dirname(__file__), "..", "public")
def og_gorsel(slug):
    """Sayfaya özel paylaşım görseli varsa onu, yoksa genel LaVie görselini döndürür."""
    return f"{U}/og/{slug}.jpg" if os.path.exists(os.path.join(KOK, "og", slug + ".jpg")) else f"{U}/og/lavie.jpg"

TASARIM_AD = {"zeytin": "Zeytin Gölgesi", "pamuk": "Pamuk Şeker", "papatya": "Papatya Sabahı", "gece": "Yıldızlı Gece", "seftali": "Şeftali Çiçeği", "lavanta": "Lavanta Rüzgârı", "gul": "Pudra Gülü", "nane": "Nane Şekeri", "ege": "Ege Çinisi", "mono": "Siyah İnci"}

SAYFALAR = [
 dict(slug="dijital-dugun-davetiyesi", tur="Düğün", kisa="düğün", baslik="Dijital Düğün Davetiyesi",
  title="Dijital Düğün Davetiyesi Hazırla · Online, LCV Takipli | LaVie",
  desc="Dijital düğün davetiyesi: zarfı açılan, müzikli, geri sayımlı davetiye sitesi. LCV takibi, konum ve program dahil; WhatsApp'tan tek link. 500 TL tek sefer.",
  cta_baslik="Düğün davetiyenizi bugün hazırlayın",
  cta_metin="Tasarımınızı seçin, nikâh ve düğün bilgilerinizi girin, canlı önizlemede görün. Beğenirseniz 500 TL tek seferlik ödemeyle linkiniz genellikle aynı gün açılır; katılım listeniz panelinizde birikmeye başlar.",
  cta_dugme="Düğün davetiyemi oluştur",
  rehber_baslik="Düğün hazırlığınız için ücretsiz rehber ve araçlar",
  rehberler=[("dugun-davetiyesi-sozleri","Düğün davetiyesi sözleri","Resmi, samimi, kısa ve dini örneklerle kopyalayıp kullanabileceğiniz davet metinleri."),
             ("davetiye-sozu-olusturucu","Davetiye sözü oluşturucu","İsimlerinizi ve tarihinizi yazın, size özel düğün davetiyesi sözü hazırlansın."),
             ("dijital-davetiye-nasil-yapilir","Dijital davetiye nasıl yapılır?","Bilgileri hazırlamaktan WhatsApp'ta paylaşıma ve LCV takibine kadar adım adım anlatım."),
             ("davetiye-ne-zaman-gonderilir","Davetiye ne zaman gönderilir?","Düğün davetiyesini kaç hafta önce göndermeniz gerektiğini ve hatırlatma zamanlamasını öğrenin."),
             ("lcv-nedir","LCV nedir?","Davetiyedeki LCV ifadesinin anlamı ve katılım yanıtlarını toplamanın kolay yolu."),
             ("davetli-listesi","Davetli listesi aracı","Misafirlerinizi gruplara ayırın, kişi sayısını hesaplayın, listeyi Excel'e aktarın."),
             ("dugun-butcesi-hesaplama","Düğün bütçesi hesaplama","Salon, yemek, kıyafet ve diğer kalemleri tek ekranda planlayın."),
             ("dijital-davetiye-fiyatlari","Dijital davetiye fiyatları","Dijital davetiyenin fiyatını neyin belirlediği, görsel davetiye ile davetiye sitesi farkı ve gizli maliyetler."),
             ("2027-dugun-takvimi","2027 düğün takvimi","Bayramlar, Ramazan ve uzun hafta sonlarıyla düğün tarihi seçerken nelere dikkat etmeli."),
             ("dugun-hashtag-olusturucu","Düğün hashtag oluşturucu","Misafirlerinizin fotoğraf paylaşırken kullanacağı size özel Instagram etiketi."),
             ("dugun-geri-sayim","Düğün geri sayım","Düğününüze kaç gün kaldığını canlı görün, paylaşılabilir geri sayım linkinizi oluşturun.")],
  tasarim="zeytin", oneri=["zeytin","papatya","gece","mono"],
  lead="Düğününüz için size özel bir davetiye sitesi: misafirleriniz zarfı açar, müziğinizi dinler, nikâh saatini ve yol tarifini tek dokunuşla bulur. Kimin geleceğini de siz panelinizden canlı takip edersiniz.",
  neden=[("Masa düzenini kolaylaştırır","Kaç kişinin geleceği panelinizde anlık görünür; salona ve catering firmasına net sayı verirsiniz."),
         ("Baskı ve dağıtım derdi yok","Yüzlerce kişiye adres adres davetiye götürmek yerine tek bir linki WhatsApp'tan gönderirsiniz."),
         ("Son dakika değişikliği sorun değil","Saat ya da salon değişirse panelden düzeltirsiniz; herkesin elindeki link aynı kalır, bilgi anında güncellenir."),
         ("Uzaktaki misafirlere de ulaşır","Yurt dışındaki ya da başka şehirdeki yakınlarınız davetiyenizi aynı gün alır.")],
  metinler=["Hayatımızın en güzel gününde, mutluluğumuzu sizlerle paylaşmak istiyoruz. Düğünümüzde sizleri de aramızda görmekten onur duyarız.",
            "Bir ömür boyu sürecek yolculuğumuzun ilk adımına tanıklık etmeniz dileğiyle, düğün törenimize davetlisiniz.",
            "İki ayrı hayat bu akşam tek bir hikâyede buluşuyor. Bu mutlu günümüzde sizleri de yanımızda görmek istiyoruz.",
            "Ailelerimizin hayır duaları ve sizlerin katılımıyla evleniyoruz. Mutluluğumuza ortak olmanızı dileriz.",
            "Sevgimizi bir ömre taşıyacağımız bu özel günde, varlığınız bizim için en güzel hediye olacak."],
  sss=[("Dijital düğün davetiyesi kâğıt davetiyenin yerini tutar mı?","Evet. Tasarım, aile isimleri, tarih, saat ve mekân gibi kâğıt davetiyedeki her bilgi dijital davetiyede de yer alır. Üstüne konum, program akışı, müzik ve katılım formu eklenir. İsterseniz yaşlı büyükleriniz için birkaç kâğıt davetiye bastırıp diğer herkese linki gönderebilirsiniz."),
       ("Nikâh ve düğün aynı gün değilse ne yapmalıyım?","Program bölümüne her etkinliği saatiyle ayrı satır olarak yazabilirsiniz. Nikâh başka bir gün ya da yerdeyse bunu davet notunda belirtebilir ya da her biri için ayrı bir davetiye sipariş edebilirsiniz."),
       ("Kaç kişinin geleceğini nasıl görürüm?","Misafirleriniz davetiyedeki katılım formundan geleceğini ve kaç kişi olacağını bildirir. Size özel panelde gelecek ve gelemeyecek kişi sayıları ile isim listesi anlık görünür; listeyi Excel'e aktarabilirsiniz."),
       ("Düğün davetiyesi ne zaman gönderilmeli?","Genellikle düğünden 4-6 hafta önce gönderilir. Dijital davetiye anında ulaştığı için daha geç de gönderebilirsiniz; ancak katılım sayısını erken öğrenmek için erken göndermek işinizi kolaylaştırır."),
       ("Dijital düğün davetiyesini kaç kişiye gönderebilirim?","Sınır yok. Aynı linki aile ve arkadaş WhatsApp gruplarına, SMS ile ya da sosyal medyadan dilediğiniz kadar kişiye gönderebilirsiniz. Davetli sayınız artsa da ücret değişmez."),
       ("Ödemeyi ne zaman yapıyorum, davetiyem ne zaman hazır olur?","Önce davetiyenizi sitemizde canlı önizlemede görürsünüz. Beğenirseniz siparişinizi oluşturup 500 TL'yi tek seferde kartla (Shopier güvencesiyle) ya da IBAN ile havaleyle ödersiniz. Kartla ödemede davetiyeniz otomatik açılır; linkiniz genellikle aynı gün hazır olur. Abonelik yoktur."),
       ("Düğünümüze özel bir tasarım yaptırabilir miyim?","Evet. Profesyonel Tasarım paketinde WhatsApp'tan düğününüzün konseptini ve renklerini konuşuyor, size özel bir tasarım hazırlıyor ve onayınıza kadar revize ediyoruz. Fiyat, tasarımın kapsamına göre 2.000 TL'den başlar.")]),
 dict(slug="dijital-nisan-davetiyesi", tur="Nişan", kisa="nişan", baslik="Dijital Nişan Davetiyesi",
  title="Dijital Nişan Davetiyesi Hazırla · Online, LCV Takipli | LaVie",
  desc="Dijital nişan davetiyesi: zarfı açılan, müzikli, geri sayımlı davetiye sitesi. Konum, program ve katılım takibi dahil; WhatsApp'tan tek link. 500 TL tek sefer.",
  cta_baslik="Nişan davetiyenizi bugün hazırlayın",
  cta_metin="Tasarımınızı seçin, nişan tarihini, saatini ve adresi girin, canlı önizlemede görün. Beğenirseniz 500 TL tek seferlik ödemeyle linkiniz genellikle aynı gün açılır; ev nişanında da salonda da kaç kişinin geleceğini panelinizden izlersiniz.",
  cta_dugme="Nişan davetiyemi oluştur",
  rehber_baslik="Nişan hazırlığınız için ücretsiz rehber ve araçlar",
  rehberler=[("nisan-davetiyesi-sozleri","Nişan davetiyesi sözleri","Resmi, samimi, kısa ve aile ağzından kopyalayıp kullanabileceğiniz nişan davet metinleri."),
             ("davetiye-sozu-olusturucu","Davetiye sözü oluşturucu","Nişan türünü seçip isimlerinizi yazın, size özel davet cümleleri hazırlansın."),
             ("dijital-davetiye-nasil-yapilir","Dijital davetiye nasıl yapılır?","Tasarım seçiminden WhatsApp'ta paylaşıma kadar adım adım dijital davetiye hazırlama."),
             ("davetiye-ne-zaman-gonderilir","Davetiye ne zaman gönderilir?","Söz, nişan ve düğün davetiyelerini kaç hafta önce göndermeniz gerektiği."),
             ("lcv-nedir","LCV nedir?","Davetiyedeki LCV ifadesinin anlamı ve nişana kimlerin geleceğini önceden öğrenmenin yolu."),
             ("davetli-listesi","Davetli listesi aracı","Nişan misafirlerinizi aile ve arkadaş gruplarına ayırın, kişi sayısını hesaplayın."),
             ("dugun-hashtag-olusturucu","Hashtag oluşturucu","Nişan fotoğraflarınız için isimlerinize özel Instagram etiketi önerileri.")],
  tasarim="gul", oneri=["gul","seftali","pamuk","zeytin"],
  lead="Nişanınızı sevdiklerinize zarif bir dijital davetiyeyle duyurun. Zarfı açılan, müzikli davetiyeniz WhatsApp'tan tek mesajla herkese ulaşır; kimlerin geleceğini panelinizden takip edersiniz.",
  neden=[("Kısa sürede hazırlanır","Nişan çoğu zaman düğünden daha kısa sürede planlanır. Dijital davetiyeniz siparişle aynı gün hazır olur, baskı beklemezsiniz."),
         ("Aile davetine yakışan şıklık","Aile isimleri, davet notu ve size uygun yazı stiliyle resmi ama sıcak bir davetiye."),
         ("Ev ya da salon, fark etmez","Nişan evde, bahçede ya da salonda olsun; adresi ve yol tarifini tek dokunuşla paylaşırsınız."),
         ("Katılımı önceden bilin","Ev nişanlarında kaç kişinin geleceğini bilmek ikram hazırlığını kolaylaştırır.")],
  metinler=["Ailelerimizin uygun görmesiyle hayatımızı birleştirmeye ilk adımı atıyoruz. Nişan törenimizde sizleri de aramızda görmekten mutluluk duyarız.",
            "Sevgimizi yüzüklerle taçlandıracağımız bu güzel günde yanımızda olmanızı dileriz.",
            "Bir ömre uzanan yolun başındayız. Bu mutlu anımızı sizlerle paylaşmak istiyoruz; nişanımıza davetlisiniz.",
            "Yüzüklerimizi takacağımız bu özel günde dualarınız ve varlığınızla bize eşlik etmenizi rica ederiz.",
            "Mutluluğumuzu sevdiklerimizle paylaşmak istiyoruz. Nişan törenimize sizleri de bekleriz."],
  sss=[("Nişan davetiyesinde hangi bilgiler olmalı?","Çiftin ve ailelerin isimleri, tarih, saat, mekân ve kısa bir davet notu yeterlidir. Dijital davetiyede bunlara konum linki, program akışı ve katılım formu da eklenir."),
       ("Nişan davetiyesi ne zaman gönderilir?","Genellikle nişandan 2-4 hafta önce gönderilir. Dijital davetiye anında ulaştığı için kısa sürede planlanan nişanlarda da rahatça kullanılır."),
       ("Aynı tasarımı düğünde de kullanabilir miyim?","Evet. Nişanda kullandığınız tasarımı düğün davetiyenizde de seçebilirsiniz; böylece iki davetiye birbirini tamamlar."),
       ("Misafirler davetiyeyi nasıl açar?","Gönderdiğiniz linke dokunmaları yeterli. Davetiye telefonun tarayıcısında açılır, uygulama indirmek gerekmez."),
       ("Nişan davetiyesini kim gönderir, kimin ağzından yazılır?","Geleneksel olarak nişanı kız tarafı düzenlediği için davetiye çoğu zaman kızın ailesi adına yazılır; günümüzde iki ailenin isimlerinin birlikte yer alması ya da çiftin kendi ağzından yazılması da yaygındır. Dijital davetiyede aile isimlerini ve davet notunu dilediğiniz gibi yazabilirsiniz."),
       ("Ev nişanı için dijital davetiye uygun mu?","Evet. Ev nişanlarında misafir sayısı sınırlı olduğu için kimin geleceğini önceden bilmek ikram ve oturma düzeni için önemlidir. Konum linki sayesinde misafirleriniz evin adresini de kolayca bulur."),
       ("Nişan davetiyesi yazdırılabilir mi?","Dijital davetiye telefonda açılmak üzere tasarlanmıştır. Yaşlı büyükleriniz için davetiyenin ekran görüntüsünü alıp yazdırabilir ya da linki onlar adına bir yakınınıza gönderebilirsiniz.")]),
 dict(slug="dijital-kina-davetiyesi", tur="Kına", kisa="kına", baslik="Dijital Kına Davetiyesi",
  title="Dijital Kına Davetiyesi Hazırla · Kına Gecesi Davetiyesi | LaVie",
  desc="Dijital kına gecesi davetiyesi: zarfı açılan, müzikli davetiye sitesi. Program, kıyafet notu, konum ve LCV takibi dahil; WhatsApp'tan tek link. 500 TL.",
  cta_baslik="Kına gecenizin davetiyesini bugün hazırlayın",
  cta_metin="Tasarımınızı seçin, kına gecesinin tarihini, saatini, adresini ve kıyafet notunuzu girin, canlı önizlemede görün. Beğenirseniz 500 TL tek seferlik ödemeyle linkiniz genellikle aynı gün açılır; kalabalık aile davetinde bile kaç kişinin geleceğini panelinizden izlersiniz.",
  cta_dugme="Kına davetiyemi oluştur",
  rehber_baslik="Kına gecesi hazırlığınız için ücretsiz rehber ve araçlar",
  rehberler=[("kina-davetiyesi-sozleri","Kına davetiyesi sözleri","Duygusal, geleneksel, kısa ve eğlenceli kına gecesi davet sözleri; davetiye notu örnekleri."),
             ("davetiye-sozu-olusturucu","Davetiye sözü oluşturucu","Kına türünü seçip gelinin adını ve tarihi yazın, size özel davet cümleleri hazırlansın."),
             ("davetiye-ne-zaman-gonderilir","Davetiye ne zaman gönderilir?","Kına ve düğün davetiyelerini kaç hafta önce göndermeniz, LCV son tarihini ne zaman koymanız gerektiği."),
             ("davetli-listesi","Davetli listesi aracı","Kına misafirlerinizi aile, komşu ve arkadaş gruplarına ayırın, kişi sayısını hesaplayın."),
             ("lcv-nedir","LCV nedir?","Davetiyedeki LCV ifadesinin anlamı ve kına gecesine kimlerin geleceğini önceden öğrenmenin yolu."),
             ("dugun-hashtag-olusturucu","Hashtag oluşturucu","Kına gecesi fotoğraflarınız için gelin ve damadın adına özel Instagram etiketi önerileri."),
             ("dugun-geri-sayim","Düğün geri sayım","Kına gecenize ve düğününüze kaç gün kaldığını görün, hazırlık takviminizi planlayın.")],
  tasarim="gul", oneri=["gul","lavanta","gece","seftali"],
  lead="Kına geceniz için zarfı açılan, müzikli bir davetiye. Misafirleriniz programı, adresi ve yol tarifini tek linkte bulur; siz de kimlerin geleceğini panelinizden anında görürsünüz.",
  neden=[("Kalabalık aileye tek linkle ulaşın","Kına gecesi davetlileri genellikle geniş aile ve komşulardan oluşur. Tek bir linki aile gruplarına göndermeniz yeterli."),
         ("Program akışı hazır","Karşılama, kına yakılması, eğlence saatleri; misafirleriniz akşamın planını önceden bilir."),
         ("Kıyafet ve hatırlatma notları","Bindallı, kıyafet önerisi ya da \"çocuklarımıza iyi uykular\" gibi notları katılım formunun üstüne ekleyebilirsiniz."),
         ("Düğünle aynı tasarım","Kına ve düğün davetiyelerinizi aynı tasarımla hazırlayıp iki geceyi birbirine bağlayabilirsiniz.")],
  metinler=["Kınamız yakılırken sevdiklerimizi yanımızda görmek istiyoruz. Kına gecemizde sizleri de aramızda görmekten mutluluk duyarız.",
            "Ellerimize kına, gönlümüze sevinç yakacağımız bu gecede bize eşlik etmenizi dileriz.",
            "Gelinimizin baba evinden uğurlanışına tanıklık etmeniz dileğiyle, kına gecemize davetlisiniz.",
            "Türküler, kahkahalar ve kınayla dolu bir gece için sizleri de bekliyoruz.",
            "Mutluluğumuzu kınayla taçlandıracağımız bu özel gecede varlığınız bizi çok mutlu edecek.",
            "Kızımızı gelin edeceğimiz günlerin en duygulu gecesinde, kına sinimize sizleri de bekliyoruz.",
            "Baba ocağındaki son gecemde en sevdiklerimle bir arada olmak istiyorum. Kına geceme davetlisiniz."],
  sss=[("Kına gecesi davetiyesi ayrıca mı hazırlanmalı?","Kına ve düğün farklı gün ya da yerdeyse ayrı davetiye hazırlamak misafirlerin karıştırmasını önler. Aynı tasarımı seçerek iki davetiyeyi birbirine uyumlu yapabilirsiniz."),
       ("Kına davetiyesine hangi notlar eklenebilir?","Kıyafet önerisi, çocuklarla ilgili rica ya da katılım bildirme tarihi gibi notları katılım formunun üstündeki alana yazabilirsiniz. Hazır cümlelerden birini de seçebilirsiniz."),
       ("Kına gecesi davetiyesi ne zaman gönderilir?","Kına gecesinden 2-4 hafta önce göndermek yaygındır. Düğün davetiyesiyle birlikte de gönderebilirsiniz."),
       ("Davetiyede müzik çalar mı?","Evet. Zarf açıldığında seçtiğiniz müzik çalmaya başlar; misafirleriniz isterse sağ alttaki düğmeyle kapatabilir."),
       ("Kına davetiyesi kimin adına yazılır?","Kına gecesini geleneksel olarak gelinin ailesi düzenlediği için davetiye çoğu zaman kızın ailesi adına yazılır. Gelin kendi ağzından ya da iki aile birlikte de davet edebilir; dijital davetiyede aile isimlerini ve davet notunu dilediğiniz gibi yazarsınız."),
       ("Kına gecesinin programını davetiyeye nasıl yazarım?","Program bölümüne her etkinliği saatiyle ayrı satır olarak eklersiniz; örneğin karşılama, gelinin girişi, kına yakılması ve eğlence. Misafirleriniz gecenin akışını önceden görür, geç kalacak olanlar kına yakılma saatini kaçırmaz."),
       ("Kına gecesi davetiyesini düğün davetiyesiyle aynı anda gönderebilir miyim?","Evet. İki ayrı davetiye hazırlayıp linkleri aynı mesajda gönderebilirsiniz. Kınaya yalnızca yakın çevreyi çağırıyorsanız kına linkini sadece o kişilere göndermeniz yeterlidir; böylece herkes kendi davetini görür."),
       ("Kınada sadece kadınlar mı olacak, bunu nasıl belirtirim?","Davet notuna ya da katılım formunun üstündeki not alanına \"Gecemiz kadınlara özeldir\" gibi kısa bir cümle eklemeniz yeterli. Kıyafet önerisi ve çocuklarla ilgili ricalar da aynı alana yazılabilir.")]),
 dict(slug="dijital-soz-davetiyesi", tur="Söz", kisa="söz", baslik="Dijital Söz Davetiyesi",
  title="Dijital Söz Davetiyesi Hazırla · Söz Töreni Davetiyesi | LaVie",
  desc="Dijital söz davetiyesi: zarfı açılan, müzikli söz töreni davetiyesi. Ev adresi konumu, geri sayım ve LCV takibi dahil; WhatsApp'tan tek link. 500 TL.",
  cta_baslik="Söz töreninizin davetiyesini bugün hazırlayın",
  cta_metin="Tasarımınızı seçin, söz töreninin tarihini, saatini ve evin adresini girin, canlı önizlemede görün. Beğenirseniz 500 TL tek seferlik ödemeyle linkiniz genellikle aynı gün açılır; aile büyüklerinizden kimlerin geleceğini panelinizden izler, ikramı ona göre hazırlarsınız.",
  cta_dugme="Söz davetiyemi oluştur",
  rehber_baslik="Söz töreni hazırlığınız için ücretsiz rehber ve araçlar",
  rehberler=[("soz-davetiyesi-sozleri","Söz davetiyesi sözleri","Kısa, geleneksel, romantik ve aile ağzından 27 söz davetiyesi sözü; söz ile nişan arasındaki fark."),
             ("davetiye-sozu-olusturucu","Davetiye sözü oluşturucu","Söz türünü seçip isimlerinizi yazın, size özel davet cümleleri hazırlansın."),
             ("davetiye-ne-zaman-gonderilir","Davetiye ne zaman gönderilir?","Söz, nişan ve düğün davetiyelerini kaç hafta önce göndermeniz gerektiği."),
             ("dijital-davetiye-nasil-yapilir","Dijital davetiye nasıl yapılır?","Bilgileri hazırlamaktan WhatsApp'ta paylaşıma kadar adım adım dijital davetiye hazırlama."),
             ("lcv-nedir","LCV nedir?","Davetiyedeki LCV ifadesinin anlamı ve söz törenine kimlerin geleceğini önceden öğrenmenin yolu."),
             ("davetli-listesi","Davetli listesi aracı","Söz törenine çağıracağınız aile büyüklerini ve yakınlarınızı listeleyin, kişi sayısını hesaplayın."),
             ("dijital-davetiye-fiyatlari","Dijital davetiye fiyatları","Dijital davetiyenin fiyatını neyin belirlediği ve tek seferlik ödemede nelerin dahil olduğu."),
             ("dugun-hashtag-olusturucu","Hashtag oluşturucu","Söz töreni fotoğraflarınız için isimlerinize özel Instagram etiketi önerileri.")],
  tasarim="ege", oneri=["ege","nane","papatya","pamuk"],
  lead="Söz töreniniz için sade ve zarif bir dijital davetiye. Aile büyüklerinize ve yakınlarınıza tek linkle ulaşır, kimlerin geleceğini panelinizden takip edersiniz.",
  neden=[("Samimi davetlere uygun","Söz genellikle yakın aile arasında yapılır. Kısa bir davet notu ve sade bir tasarımla içten bir davetiye hazırlarsınız."),
         ("Hızlı ve zahmetsiz","Söz kısa sürede planlanabilir; davetiyeniz aynı gün hazır olur, baskı beklemezsiniz."),
         ("Evin adresi tek dokunuşta","Tören evde yapılıyorsa konum linki sayesinde misafirleriniz kapıyı kolayca bulur."),
         ("Sonraki davetlere hazırlık","Aynı tasarımı nişan ve düğün davetiyelerinizde de kullanabilirsiniz.")],
  metinler=["Ailelerimizin rızası ve hayır dualarıyla söz kesiyoruz. Bu güzel günümüzde sizleri de aramızda görmek isteriz.",
            "Birbirimize verdiğimiz sözü sevdiklerimizin huzurunda taçlandırmak istiyoruz. Söz törenimize davetlisiniz.",
            "Hayırlı bir başlangıcın ilk adımında dualarınızla yanımızda olmanızı dileriz.",
            "Mutluluğumuzu paylaşacağımız bu küçük ama anlamlı günde varlığınız bizi onurlandıracak.",
            "İki ailenin bir araya geldiği bu güzel günde sizleri de bekliyoruz.",
            "Yüzüklerimiz kırmızı kurdeleyle bağlanırken sevdiklerimizin yanımızda olmasını istiyoruz. Söz törenimize davetlisiniz."],
  sss=[("Söz töreni için davetiye gerekli mi?","Söz genellikle yakın çevreyle yapıldığı için davetiye şart değildir. Ancak dijital davetiye tarih, saat ve adresi herkese aynı anda ve eksiksiz iletmenin en kolay yoludur."),
       ("Söz davetiyesinde neler yazılır?","Çiftin ve ailelerin isimleri, tarih, saat, adres ve kısa bir davet notu yeterlidir."),
       ("Söz, nişan ve düğün için aynı tasarımı kullanabilir miyim?","Evet. On tasarımdan birini seçip tüm davetlerinizde kullanabilirsiniz; her davet türü için başlık otomatik değişir."),
       ("Davetiyeyi sonradan değiştirebilir miyim?","Evet. Size özel panelden saat, adres ve davet notu dahil tüm bilgileri dilediğiniz zaman güncelleyebilirsiniz."),
       ("Söz ile nişan arasındaki fark nedir?","Söz, iki ailenin evliliğe onay verdiği ilk ve daha sade buluşmadır; çoğu zaman kız evinde, yakın aile arasında yapılır ve yüzükler kırmızı kurdeleyle bağlanıp kesilir. Nişan ise daha geniş katılımlı, çoğu zaman salonda ya da bahçede yapılan resmi kutlamadır. Nişan da planlıyorsanız dijital nişan davetiyesini aynı tasarımla hazırlayabilirsiniz."),
       ("Söz davetiyesi kimin adına yazılır?","Söz töreni geleneksel olarak kız evinde yapıldığı için davetiye çoğu zaman kızın ailesi adına yazılır. İki ailenin isimlerinin birlikte yer alması ya da çiftin kendi ağzından davet etmesi de yaygındır; dijital davetiyede aile isimlerini ve davet notunu dilediğiniz gibi yazarsınız."),
       ("Söz davetiyesi ne zaman gönderilir?","Söz genellikle kısa sürede planlandığı için 1-3 hafta önce göndermek yeterlidir. Dijital davetiye anında ulaştığı için birkaç gün kala bile gönderebilirsiniz; katılım formuna son yanıt tarihini yazmanız ikram hazırlığını kolaylaştırır."),
       ("Söz töreni evde yapılıyorsa misafirler adresi nasıl bulur?","Davetiyeye evin adresini ve konumunu eklediğinizde misafirleriniz tek dokunuşla haritada yol tarifi alır. Apartman, kat ya da daire numarası gibi ayrıntıları davet notuna yazabilirsiniz.")]),
]

ORTAK_OZ = ["Zarf açılışı ve müzik","Canlı geri sayım","Program akışı ve yol tarifi","Katılım formu (LCV)","Size özel panel ve Excel listesi","Hatıra defteri","5 tasarım, 7 yazı stili","Panelden sınırsız düzenleme"]
IG='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>'
TIK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg>'
WA='<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2zm0 18.2a8.2 8.2 0 01-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1112 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 01-3.3-2.9c-.3-.4.3-.4.7-1.3a.5.5 0 000-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 00-.7.3 3 3 0 00-.9 2.2 5.2 5.2 0 001.1 2.8 11.9 11.9 0 004.6 4c1.7.7 2.4.8 3.2.7a2.8 2.8 0 001.8-1.3 2.3 2.3 0 00.2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>'
e=html.escape

CSS = """
:root{--paper:#f7f4f2;--paper2:#efe9e5;--ink:#211f27;--muted:#6a6570;--line:#e3dad4;--accent:#5b4a6b;--accent-2:#4b3c5a;--soft:#efe7f1;--gold:#a9824a;--gold-2:#c9a46a;--deep:#1f1b26;--deep-ink:#efe8f2;--deep-mut:#b6aec0;
--display:"Italiana","Cormorant Garamond",Georgia,serif;--serif:"Cormorant Garamond",Georgia,serif;--body:"Jost",system-ui,sans-serif;color-scheme:light}
*{box-sizing:border-box}html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}html,body{margin:0}
body{background:var(--paper);color:var(--ink);font-family:var(--body);font-size:16px;line-height:1.65;overflow-x:hidden}
a{color:inherit}img,svg{display:block}:focus-visible{outline:2px solid var(--gold);outline-offset:3px}
.in{max-width:1080px;margin:0 auto;padding-inline:20px}
section.blk{padding-block:72px}@media(max-width:640px){section.blk{padding-block:52px}}
.eyebrow{display:inline-flex;align-items:center;gap:10px;font-size:.72rem;letter-spacing:.26em;text-transform:uppercase;color:var(--gold);font-weight:500}.eyebrow::before{content:"";width:22px;height:1px;background:currentColor}
h1,h2{font-family:var(--display);font-weight:400;line-height:1.06;text-wrap:balance}
h1{font-size:clamp(2.6rem,7vw,4.4rem);margin:14px 0 18px}h1 em,h2 em{font-family:"Pinyon Script",cursive;font-style:normal;color:var(--accent);font-size:1.08em;line-height:.8}
h2{font-size:clamp(2rem,4.6vw,2.8rem);margin:10px 0 14px}
.lead{color:var(--muted);font-size:1.06rem;max-width:58ch;margin:0}
.btn{font:inherit;font-weight:500;font-size:.95rem;border:1px solid transparent;border-radius:999px;padding:14px 24px;cursor:pointer;text-decoration:none;display:inline-flex;align-items:center;justify-content:center;gap:8px;white-space:nowrap}
.btn.pri{background:var(--accent);color:#fff;box-shadow:0 10px 24px -14px rgba(91,74,107,.9)}.btn.pri:hover{background:var(--accent-2)}
.btn.sec{border-color:rgba(33,31,39,.3);background:rgba(255,255,255,.6)}.btn.sec:hover{border-color:var(--ink);background:#fff}
.ust-serit{display:block;background:var(--deep);color:var(--deep-ink);text-decoration:none;font-size:.8rem}.ust-serit .in{display:flex;align-items:center;justify-content:center;gap:8px;min-height:38px}.ust-serit svg{width:16px;height:16px;color:var(--gold-2)}.ust-serit b{font-weight:500;color:#fff}
.nav{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--paper) 88%,transparent);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.nav .in{display:flex;align-items:center;justify-content:space-between;height:64px;gap:14px}.nav img{height:44px;width:auto}@media(max-width:400px){.nav img{height:38px}}.nav .btn{padding:10px 16px;font-size:.85rem}
.yol{font-size:.82rem;color:var(--muted);padding-top:18px}.yol a{text-decoration:none}.yol a:hover{text-decoration:underline}
.hero{padding-block:24px 64px}.hero .in{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:48px;align-items:center}
@media(max-width:860px){.hero .in{grid-template-columns:minmax(0,1fr);gap:36px}}
.cta{display:flex;gap:10px;flex-wrap:wrap;margin-top:26px}@media(max-width:440px){.cta .btn{flex:1 1 100%}}
.pill{display:inline-flex;align-items:center;gap:10px;margin-top:20px;padding:7px 14px 7px 8px;border-radius:999px;background:#fff;border:1px solid var(--line);font-size:.88rem;color:var(--muted)}.pill b{white-space:nowrap;background:var(--soft);color:var(--accent);font-weight:500;padding:3px 10px;border-radius:999px}
.tel{justify-self:center;width:100%;max-width:300px;margin:0}.tel .ek{aspect-ratio:9/18.5;border-radius:42px;border:10px solid #18161c;background:#18161c;overflow:hidden;box-shadow:0 40px 80px -36px rgba(33,31,39,.7)}
.tel iframe{width:100%;height:100%;border:0;border-radius:32px;display:block}.tel figcaption{text-align:center;font-size:.8rem;color:var(--muted);margin-top:12px}
.kartlar{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin-top:34px}@media(max-width:700px){.kartlar{grid-template-columns:1fr}}
.kart{background:#fff;border:1px solid var(--line);border-radius:18px;padding:24px}.kart h3{margin:0 0 6px;font-weight:500;font-size:1.05rem}.kart p{margin:0;color:var(--muted);font-size:.94rem}
.oz{list-style:none;padding:0;margin:28px 0 0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px 24px}@media(max-width:560px){.oz{grid-template-columns:1fr}}
.oz li{display:flex;gap:10px;align-items:flex-start}.oz svg{flex:0 0 18px;width:18px;height:18px;color:var(--accent);margin-top:4px}
.gri{background:var(--paper2);border-block:1px solid var(--line)}
.metinler{display:grid;gap:14px;margin-top:30px}
.metin{background:#fff;border:1px solid var(--line);border-radius:16px;padding:20px 22px;display:grid;grid-template-columns:1fr auto;gap:14px;align-items:center}
.metin p{margin:0;font-family:var(--serif);font-style:italic;font-size:1.18rem;line-height:1.5}
.metin button{font:inherit;font-size:.8rem;font-weight:500;border:1px solid var(--line);background:var(--paper);border-radius:999px;padding:8px 14px;cursor:pointer;white-space:nowrap}
@media(max-width:560px){.metin{grid-template-columns:1fr}.metin button{justify-self:start}}
.tas{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin-top:30px}@media(max-width:700px){.tas{grid-template-columns:1fr}}
.tas a{display:flex;justify-content:space-between;align-items:center;gap:10px;background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px 20px;text-decoration:none}
.tas b{font-family:var(--display);font-weight:400;font-size:1.4rem}.tas span{font-size:.82rem;color:var(--accent);font-weight:500}
.fiyat{background:var(--deep);color:var(--deep-ink);border-radius:26px;padding:40px 28px;display:grid;grid-template-columns:1fr auto;gap:24px;align-items:center}
@media(max-width:700px){.fiyat{grid-template-columns:1fr;padding:32px 22px}}
.fiyat h2{margin:0 0 6px;color:#fff}.fiyat p{margin:0;color:var(--deep-mut)}.fiyat .tl{font-family:var(--display);font-size:3.4rem;line-height:1;color:var(--gold-2)}.fiyat .tl small{font-family:var(--body);font-size:.85rem;color:var(--deep-mut);margin-left:6px}
.fiyat .btn.pri{background:#fff;color:var(--accent);margin-top:14px}
.sss{border-top:1px solid var(--line);margin-top:26px;max-width:780px}.sss details{border-bottom:1px solid var(--line)}
.sss summary{cursor:pointer;list-style:none;padding:18px 34px 18px 0;font-weight:500;position:relative}.sss summary::-webkit-details-marker{display:none}
.sss summary::after{content:"+";position:absolute;right:4px;top:50%;transform:translateY(-50%);font-size:1.5rem;font-weight:300;color:var(--accent)}.sss details[open] summary::after{content:"–"}
.sss p{margin:0 0 18px;color:var(--muted)}
.diger{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}.diger a{border:1px solid var(--line);background:#fff;border-radius:999px;padding:10px 18px;text-decoration:none;font-size:.92rem}.diger a:hover{border-color:var(--accent);color:var(--accent)}
footer{background:var(--deep);color:var(--deep-mut);padding-block:40px 110px;font-size:.88rem}footer .in{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;align-items:center}footer img{height:50px;width:auto}footer a{color:#fff;text-decoration:none}
.destek{position:fixed;right:16px;bottom:calc(18px + env(safe-area-inset-bottom,0px));z-index:24;display:flex;align-items:center;gap:8px;background:#25d366;color:#0b2b17;text-decoration:none;font-weight:500;font-size:.9rem;padding:12px;border-radius:999px;box-shadow:0 8px 22px -8px rgba(0,0,0,.45)}.destek svg{width:22px;height:22px}
"""

# "Yeni eklenenler" bölümü (/rehber ve /araclar en üstünde). İlk sıradaki sezona uygun içeriktir.
YENILER = [
 dict(slug="2027-dugun-takvimi", ad="2027 düğün takvimi", tip="Araç", tarih="13 Ekim 2026", sezon="Sezonun içeriği",
      ozet="Gelecek yılın düğün tarihini seçme zamanı: bayramlar, Ramazan, iki bayram arası ve uzun hafta sonları tek takvimde."),
 dict(slug="dijital-davetiye-fiyatlari", ad="Dijital davetiye fiyatları", tip="Rehber", tarih="18 Ekim 2026",
      ozet="Dijital davetiyenin fiyatını neler belirler: görsel davetiye ile davetiye sitesi farkı, tek seferlik ödeme ve gizli maliyetler."),
 dict(slug="dugun-geri-sayim", ad="Düğün geri sayım", tip="Araç", tarih="17 Ekim 2026",
      ozet="Düğününüze kaç gün kaldığını canlı görün; paylaşılabilir link, takvime ekleme ve hazırlık takvimi."),
 dict(slug="dijital-davetiye-nasil-yapilir", ad="Dijital davetiye nasıl yapılır?", tip="Rehber", tarih="16 Ekim 2026",
      ozet="Hazırlamanız gereken bilgilerden paylaşıma ve katılım takibine kadar adım adım dijital davetiye."),
]
YENI_CSS = """
.yeni{margin-top:26px}.yeni h2{font-size:1.5rem;margin:0 0 4px}
.yeni .kartlar{grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px;margin-top:14px}
.yeni .kart{padding:18px}.yeni .kart p{margin:0;font-size:.9rem;color:var(--muted)}
.yeni small{display:block;font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);font-weight:500;margin-bottom:6px}
.yeni .kart.sezon{border-color:#dcd0e2;background:var(--soft)}
"""
def yeni_eklenenler():
    for y in YENILER:
        assert os.path.exists(os.path.join(KOK, y["slug"] + ".html")), y["slug"]
    k = "".join(f'<a class="kart{" sezon" if y.get("sezon") else ""}" href="/{y["slug"]}" style="text-decoration:none;display:block"><small>{e(y.get("sezon") or y["tip"])} · {e(y["tarih"])}</small><h3>{e(y["ad"])}</h3><p>{e(y["ozet"])}</p></a>' for y in YENILER)
    return f'<section class="yeni" aria-labelledby="yeni-b"><h2 id="yeni-b">Yeni eklenenler</h2><div class="kartlar">{k}</div></section>'

def hub_ld(slug, ad, aciklama, ogeler):
    """Rehber/araçlar ana sayfaları için CollectionPage + BreadcrumbList JSON-LD. ogeler: [(slug, ad), ...]"""
    url = f"{U}/{slug}"
    col = {"@context":"https://schema.org","@type":"CollectionPage","name":ad,"description":aciklama,"url":url,"inLanguage":"tr-TR",
           "publisher":{"@type":"Organization","name":"LaVie Davetiye","url":U+"/"},
           "mainEntity":{"@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"url":f"{U}/{x}"} for i,(x,n) in enumerate(ogeler)]}}
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Ana sayfa","item":U+"/"},{"@type":"ListItem","position":2,"name":ad,"item":url}]}
    return "\n".join(f'<script type="application/ld+json">{json.dumps(x,ensure_ascii=False)}</script>' for x in (col,bc))

def sayfa(s):
    turq = s["tur"]
    olustur = f"/?tur={turq}&t={s['tasarim']}#olustur"
    demo = f"/d?c=ornek&tur={turq}&t={s['tasarim']}"
    url = f"{U}/{s['slug']}"
    faq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in s["sss"]]}
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Ana sayfa","item":U+"/"},{"@type":"ListItem","position":2,"name":s["baslik"],"item":url}]}
    srv = {"@context":"https://schema.org","@type":"Service","name":s["baslik"],"serviceType":s["baslik"],"provider":{"@type":"Organization","name":"LaVie Davetiye","url":U+"/"},"areaServed":{"@type":"Country","name":"Türkiye"},"offers":{"@type":"Offer","price":"500","priceCurrency":"TRY","url":url}}
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(x,ensure_ascii=False)}</script>' for x in (bc,srv,faq))
    ilk, son = s["baslik"].rsplit(" ",1)
    neden = "".join(f'<div class="kart"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a,b in s["neden"])
    oz = "".join(f"<li>{TIK}<span>{e(x)}</span></li>" for x in ORTAK_OZ)
    metin = "".join(f'<div class="metin"><p>“{e(m)}”</p><button type="button" data-m="{e(m)}">Kopyala</button></div>' for m in s["metinler"])
    tas = "".join(f'<a href="/d?c=ornek&amp;tur={turq}&amp;t={t}" target="_blank" rel="noopener"><b>{TASARIM_AD[t]}</b><span>Canlı önizle →</span></a>' for t in s["oneri"])
    sss = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q,a in s["sss"])
    diger = "".join(f'<a href="/{x["slug"]}">{x["baslik"]}</a>' for x in SAYFALAR if x is not s)
    rehber = ""
    if s.get("rehberler"):
        for x,_,_ in s["rehberler"]:
            assert os.path.exists(os.path.join(KOK, x + ".html")), x
        kart = "".join(f'<a class="kart" href="/{x}" style="text-decoration:none;display:block"><h3>{e(a)}</h3><p>{e(b)}</p></a>' for x,a,b in s["rehberler"])
        rehber = f'''<section class="blk gri"><div class="in">
  <div class="eyebrow">Ücretsiz kaynaklar</div>
  <h2>{e(s["rehber_baslik"])}</h2>
  <div class="kartlar">{kart}</div>
</div></section>
'''
    cta_b = s.get("cta_baslik", "Tüm özellikler tek pakette")
    cta_m = s.get("cta_metin", "Davetiye siteniz, katılım takibi ve size özel paneliniz. Abonelik yok, ödemeyi davetiyenizi beğendikten sonra yaparsınız.")
    cta_d = s.get("cta_dugme", "Hemen oluştur")
    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon-48.png" sizes="48x48" type="image/png"><link rel="apple-touch-icon" href="/favicon-180.png">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(s['title'])}</title>
<meta name="description" content="{e(s['desc'])}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#f6f3f1">
<meta property="og:type" content="website"><meta property="og:locale" content="tr_TR"><meta property="og:site_name" content="LaVie Davetiye">
<meta property="og:title" content="{e(s['baslik'])} · LaVie"><meta property="og:description" content="{e(s['desc'])}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{U}/og/{s['tasarim']}.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Italiana&family=Pinyon+Script&family=Cormorant+Garamond:ital,wght@0,400;1,400&family=Jost:wght@400;500&display=swap">
{ld}
<style>{CSS}</style>
</head>
<body>
<a class="ust-serit" href="https://instagram.com/la.viecreative" target="_blank" rel="noopener"><div class="in">{IG}<span>Instagram'da biz: <b>@la.viecreative</b></span></div></a>
<header class="nav"><div class="in"><a href="/" aria-label="LaVie Davetiye ana sayfa"><img src="/logo.svg" alt="La Vie Creative Studio" width="630" height="165"></a><a class="btn pri" href="{olustur}">Davetiyemi oluştur</a></div></header>
<main>
<div class="in yol"><a href="/">Ana sayfa</a> › {e(s['baslik'])}</div>
<section class="hero"><div class="in">
  <div>
    <div class="eyebrow">LaVie Davetiye</div>
    <h1>{e(ilk)} <em>{e(son)}</em></h1>
    <p class="lead">{e(s['lead'])}</p>
    <div class="cta"><a class="btn pri" href="{olustur}">{e(turq)} davetiyemi oluştur</a><a class="btn sec" href="{demo}" target="_blank" rel="noopener">Canlı örneği aç</a></div>
    <div class="pill"><b>500 TL</b> tek seferlik ödeme · önce görün, sonra ödeyin</div>
  </div>
  <figure class="tel"><div class="ek"><iframe src="{demo}" title="Örnek {e(s['kisa'])} davetiyesi" loading="lazy"></iframe></div><figcaption>Canlı örnek · zarfa dokunun</figcaption></figure>
</div></section>

<section class="blk" style="padding-top:0"><div class="in">
  <div class="eyebrow">Neden dijital</div>
  <h2>Neden dijital {e(s['kisa'])} davetiyesi?</h2>
  <div class="kartlar">{neden}</div>
  <ul class="oz">{oz}</ul>
</div></section>

<section class="blk gri"><div class="in">
  <div class="eyebrow">Metin örnekleri</div>
  <h2>{e(turq)} davetiyesi <em>metinleri</em></h2>
  <p class="lead">Beğendiğiniz metni kopyalayıp davetiyenizin "Davet notu" alanına yapıştırabilir ya da kendinize göre değiştirebilirsiniz.</p>
  <div class="metinler">{metin}</div>
</div></section>

<section class="blk"><div class="in">
  <div class="eyebrow">Tasarımlar</div>
  <h2>{e(turq)} için önerdiğimiz tasarımlar</h2>
  <p class="lead">On tasarımın hepsi her davet türüne uyar; başlık davet türünüze göre kendiliğinden değişir.</p>
  <div class="tas">{tas}</div>
</div></section>

<section class="blk" style="padding-top:0"><div class="in">
  <div class="fiyat">
    <div><h2>{e(cta_b)}</h2><p>{e(cta_m)}</p></div>
    <div><div class="tl">500<small>TL</small></div><a class="btn pri" href="{olustur}">{e(cta_d)}</a></div>
  </div>
</div></section>
{rehber}
<section class="blk"{"" if rehber else ' style="padding-top:0"'}><div class="in">
  <div class="eyebrow">Sıkça sorulanlar</div>
  <h2>{e(turq)} davetiyesi hakkında</h2>
  <div class="sss">{sss}</div>
  <h2 style="font-size:1.6rem;margin-top:48px">Diğer davetiye türleri</h2>
  <div class="diger">{diger}<a href="/">Tüm tasarımlar</a></div>
</div></section>
</main>
<footer><div class="in"><a href="/" aria-label="LaVie Davetiye"><img src="/logo-acik.svg" alt="La Vie Creative Studio" width="630" height="165"></a><span>© <span id="yil">2026</span> LaVie Davetiye · <a href="https://instagram.com/la.viecreative" target="_blank" rel="noopener">@la.viecreative</a></span></div></footer>
<a class="destek" id="destek" target="_blank" rel="noopener" aria-label="WhatsApp destek hattı">{WA}</a>
<script src="/ayarlar.js"></script>
<script>
document.getElementById("yil").textContent = new Date().getFullYear();
document.getElementById("destek").href = "https://wa.me/" + window.LAVIE_AYAR.WHATSAPP + "?text=" + encodeURIComponent("Merhaba LaVie, {s['kisa']} davetiyesi hakkında bilgi almak istiyorum.");
document.querySelectorAll("[data-m]").forEach(b => b.onclick = async () => {{
  try {{ await navigator.clipboard.writeText(b.dataset.m); b.textContent = "Kopyalandı"; }} catch (_) {{ b.textContent = "Kopyalanamadı"; }}
  setTimeout(() => b.textContent = "Kopyala", 1800);
}});
</script>
</body>
</html>
"""

def site_haritasi(ekler=()):
    sm = ['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
          f'  <url><loc>{U}/</loc><lastmod>2026-10-12</lastmod><changefreq>weekly</changefreq><priority>1.0</priority></url>']
    sm += [f'  <url><loc>{U}/{s["slug"]}</loc><lastmod>2026-10-12</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>' for s in SAYFALAR]
    sm += [f'  <url><loc>{U}/{x}</loc><lastmod>2026-10-12</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>' for x in ekler]
    sm.append("</urlset>")
    open(os.path.join(KOK, "sitemap.xml"), "w").write("\n".join(sm) + "\n")

if __name__ == "__main__":
    for s in SAYFALAR:
        open(os.path.join(KOK, s["slug"] + ".html"), "w", encoding="utf8").write(sayfa(s))
    print("ok", [s["slug"] for s in SAYFALAR])
