# Rehber yazılarını üretir: python3 araclar/rehber.py  (public/ içine yazar, site haritasını günceller)
import json, html, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from tur_sayfalari import U, KOK, CSS, IG, WA, SAYFALAR, site_haritasi, og_gorsel, yeni_eklenenler, YENI_CSS, hub_ld

e = html.escape
TARIH = "2026-10-12"

# Her yazı: bölümler (başlık, paragraflar, örnek sözler, madde listesi)
YAZILAR = [
 dict(slug="dugun-davetiyesi-sozleri", kisa="Düğün davetiyesi sözleri", tur="Düğün",
  title="Düğün Davetiyesi Sözleri: 48 Kısa, Anlamlı ve Dualı Örnek | LaVie",
  desc="48 düğün davetiyesi sözü: kısa, klasik, dualı, modern, aile ağzından ve esprili örnekler. Tek tıkla kopyalayın, dijital düğün davetiyenize ekleyin.",
  guncel=("2026-10-19", "19 Ekim 2026"),
  cta=("Seçtiğiniz sözle düğün davetiyenizi hazırlayın", "Sözü kopyalayın, LaVie'de “Davet notu” alanına yapıştırın; zarfı açılan, müzikli, konumlu ve katılım formlu dijital düğün davetiyenizde anında görün. 500 TL, tek seferlik."),
  ilgili=[("davetiye-sozu-olusturucu","Davetiye sözü oluşturucu"),("davetli-listesi","Davetli listesi aracı"),("dugun-geri-sayim","Düğün geri sayım")],
  h1=("Düğün Davetiyesi", "Sözleri"),
  giris="Davetiyedeki birkaç cümle, misafirinizin düğününüzle ilgili ilk izlenimidir. Aşağıda farklı tarzlarda 48 düğün davetiyesi sözü bulacaksınız. Beğendiğinizi kopyalayabilir, isimleri ve ayrıntıları kendinize göre değiştirebilirsiniz.",
  bolumler=[
   ("Kısa düğün davetiyesi sözleri", ["Davetiyeniz sade bir tasarıma sahipse ya da tek satırlık bir cümle istiyorsanız kısa sözler en iyi seçimdir."],
    ["Bir ömür boyu sürecek mutluluğumuza sizi de bekliyoruz.",
     "En güzel günümüzde yanımızda olun.",
     "Hayatımızı birleştiriyoruz; sevincimize ortak olmanızı dileriz.",
     "İki gönül, tek yol. Düğünümüze davetlisiniz.",
     "Mutluluğumuzu sizinle paylaşmak istiyoruz.",
     "Bu güzel günde sizi de aramızda görmek isteriz.",
     "Evet dedik! Düğünümüzde sizi bekliyoruz.",
     "Sevgimizi bir ömre taşıdığımız günde yanımızda olun."], None),
   ("Klasik ve resmi düğün davetiyesi sözleri", ["Aile büyüklerinin de okuyacağı, geleneksel bir dil tercih ediyorsanız bu sözler uygundur."],
    ["Ailelerimizin hayır dualarıyla hayatımızı birleştiriyoruz. Bu mutlu günümüzde sizleri de aramızda görmekten onur duyarız.",
     "Evlatlarımızın mutluluğunu sizlerle paylaşmak istiyoruz. Düğün törenimize teşriflerinizi rica ederiz.",
     "Bir ömür boyu sürecek yolculuğumuzun ilk adımında, dualarınız ve varlığınızla yanımızda olmanızı dileriz.",
     "Hayatımızın en anlamlı gününde sizleri de aramızda görmekten mutluluk duyarız.",
     "Sevgi ve saygıyla kurduğumuz yuvanın ilk gününe şahitlik etmeniz dileğiyle.",
     "Mutluluğumuzu paylaşmak üzere düğün törenimize sizleri de davet etmekten onur duyarız.",
     "Allah'ın izni ve ailelerimizin rızasıyla evleniyoruz. Bu mutlu günümüzde sizleri de aramızda görmek isteriz.",
     "Bir yastıkta kocamaya niyet ettiğimiz bu günde dualarınızı bekliyoruz."], None),
   ("Dualı ve manevi düğün davetiyesi sözleri", ["Dini nikâh, mevlit ya da dua ile başlayan bir düğün planlıyorsanız davetiyede de bu manevi havayı yansıtan sözler tercih edebilirsiniz."],
    ["Rabbimin takdiri ve ailelerimizin duasıyla kurduğumuz yuvanın ilk gününde sizleri de aramızda görmek isteriz.",
     "Hayırlı bir yuva kurmak niyetiyle çıktığımız bu yolda dualarınızla yanımızda olmanızı rica ederiz.",
     "Allah'ın izniyle birleşen hayatlarımızın ilk adımında sizleri de sevincimize ortak etmek isteriz.",
     "Sevgi ve merhamet üzerine kurmaya niyet ettiğimiz yuvamız için dualarınızı ve varlığınızı bekliyoruz.",
     "Nikâhımızın hayırlara vesile olması dileğiyle, bu mübarek günümüzde sizleri de aramızda görmekten onur duyarız.",
     "Bir ömür boyu birbirimize yoldaş olmaya niyet ettik. Bu güzel niyetimize âmin demeniz için sizleri de bekliyoruz.",
     "Rabbim yuvamızı huzurla doldursun diye dua ederken bu dualara sizin de katılmanızı isteriz.",
     "Hayırlı bir başlangıç için dualarınızı esirgemeyin; düğün merasimimize teşriflerinizi bekleriz."], None),
   ("Modern ve romantik düğün davetiyesi sözleri", ["Daha kişisel ve duygusal bir dil, özellikle genç çiftlerin davetiyelerinde çok sevilir."],
    ["İki ayrı hikâye bu akşam tek bir masalda buluşuyor. Masalımızın ilk sayfasında sizi de görmek istiyoruz.",
     "Birlikte gülmeye, birlikte yaşlanmaya karar verdik. Bu kararı sizinle kutlamak istiyoruz.",
     "Aşkımızın en güzel kutlamasında yanımızda olmanız bizi çok mutlu edecek.",
     "Yıllar önce tanıştık, bugün bir ömre söz veriyoruz. Bu anı sizinle paylaşmak istiyoruz.",
     "Hayat birlikte daha güzel. Bunu kutlarken sizi de aramızda istiyoruz.",
     "Kalplerimizin aynı ritimde attığı bu günde dans pistinde sizi bekliyoruz.",
     "Sonsuza kadar sürecek bir 'evet' için sizi de bekliyoruz.",
     "En güzel hikâyemizin başladığı gün; sevdiklerimizle birlikte olmak istiyoruz."], None),
   ("Aile ağzından düğün davetiyesi sözleri", ["Davetiyeyi anne ve babalar adına yazmak, özellikle geniş ailelerde sıcak bir etki bırakır."],
    ["Kızımız Elif ile oğlumuz Burak'ın mutluluğuna ortak olmanızı dileriz.",
     "Evlatlarımızı dünya evine uğurlarken sevincimizi sizlerle paylaşmak istiyoruz.",
     "Yılmaz ve Demir aileleri olarak çocuklarımızın düğün törenine sizleri de davet ediyoruz.",
     "Bir ömür boyu mutluluk dilediğimiz evlatlarımızın düğününde varlığınız bizi onurlandıracaktır.",
     "Gözümüzün nuru evlatlarımızın en mutlu gününde aramızda olmanızı rica ederiz.",
     "İki ailenin tek bir aile olduğu bu güzel günde sizleri de bekliyoruz.",
     "Mutluluklarına şahit olmanız dileğiyle, düğünümüze teşrif etmenizi rica ederiz.",
     "Çocuklarımızın kurduğu yuvanın ilk gününde dualarınızla yanımızda olun."], None),
   ("Esprili ve eğlenceli düğün davetiyesi sözleri", ["Yakın arkadaş çevresine hitap eden ya da eğlenceli bir düğün planlıyorsanız biraz mizah iyi gider."],
    ["Sonunda evleniyoruz! Annemizin de sizin de sorularına son veriyoruz.",
     "Pasta bizden, dans sizden. Düğünümüzde görüşmek üzere!",
     "Kumandayı paylaşmaya karar verdik. Bu cesur kararı kutlamaya bekleriz.",
     "Bekârlığa veda ediyoruz; vedalaşmaya siz de gelin.",
     "Halay başı aranıyor! Başvurular düğün gecesi kabul edilecektir.",
     "Bu sefer gerçekten oluyor. Takvimlerinize not alın!",
     "Biz evleniyoruz, siz eğleniyorsunuz. Adil bir anlaşma.",
     "Sizsiz olmaz; masanız hazır, ayakkabılarınızı dans için seçin."], None),
   ("Davetiye metnine eklenebilecek notlar", ["Davetiyenin altına eklenen kısa notlar misafirlerinize yol gösterir. LaVie davetiyelerinde bu notları katılım formunun hemen üstüne ekleyebilirsiniz."],
    None, ["Çocuklarımıza iyi uykular dileriz.", "Lütfen katılım durumunuzu düğünden bir hafta önce bildiriniz.", "Davetiyemiz kişiye özeldir.", "Kıyafet önerisi: şık ve açık renkler.", "Otopark mekânın arka girişindedir."]),
   ("Düğün davetiyesine neler yazılmalı?", ["İyi bir düğün davetiyesinde şu bilgiler eksiksiz yer almalıdır. Dijital davetiyede bunlar ayrı bölümlerde düzenli görünür, misafir aradığını hemen bulur."],
    None, ["Gelin ve damadın adları", "İsteğe bağlı olarak ailelerin adları", "Tarih, gün ve saat", "Mekânın adı ve açık adresi", "Kısa bir davet sözü", "Varsa program akışı (nikâh, yemek, eğlence)", "Katılım bildirme (LCV) yöntemi ve tarihi"]),
  ],
  sss=[("Düğün davetiyesine en çok hangi söz yazılır?", "En çok tercih edilenler 'Hayatımızın en güzel gününde sizleri de aramızda görmekten mutluluk duyarız' gibi sade ve sıcak cümlelerdir. Aile büyüklerine de hitap ettiği için geniş davetli listelerinde güvenli bir seçimdir."),
       ("Davetiye sözü ne kadar uzun olmalı?", "Bir ya da iki cümle yeterlidir. Asıl bilgiler (tarih, saat, mekân) ayrıca yer aldığı için davet sözünün kısa ve akılda kalıcı olması daha etkilidir."),
       ("Dijital davetiyede de bu sözleri kullanabilir miyim?", "Evet. LaVie'de sözü 'Davet notu' alanına yapıştırmanız yeterli; yazdığınız anda telefondaki önizlemede görünür ve sonradan panelinizden değiştirebilirsiniz."),
       ("Davetiyede gelinin adı mı damadın adı mı önce yazılır?", "Kesin bir kural yoktur. Yaygın kullanımda gelinin adı önce yazılır; aile adları kullanılıyorsa kız ve erkek tarafı aynı düzende sıralanır. Önemli olan iki ailenin de bu sıralamayı benimsemesidir; dijital davetiyede isimlerin sırasını dilediğiniz zaman değiştirebilirsiniz."),
       ("Düğüne çocuk getirilmemesi davetiyede kibarca nasıl belirtilir?", "Doğrudan yasak dili yerine nazik bir not tercih edin: 'Çocuklarımıza iyi uykular dileriz' ya da 'Bu gece yalnızca yetişkin misafirlerimizi ağırlayacağız' gibi. Notu davet sözünün altına ayrı bir satır olarak eklemek, sözün sıcaklığını bozmadan mesajı iletir."),
       ("Davet sözüne kendi hikâyemizi yazabilir miyiz?", "Elbette. Tanışma yılınız, ilk buluştuğunuz şehir ya da ortak bir esprinizle başlayan bir cümle davetiyeyi kişisel kılar. İsterseniz ücretsiz davetiye sözü oluşturucuyla isimlerinize özel taslaklar üretip üzerinde değişiklik yapabilirsiniz.")]),

 dict(slug="kina-davetiyesi-sozleri", kisa="Kına davetiyesi sözleri", tur="Kına",
  title="Kına Davetiyesi Sözleri: 30 Duygusal, Kısa ve Eğlenceli Örnek | LaVie",
  desc="Kına gecesi davetiyesi için 30 söz: duygusal, geleneksel, kısa, eğlenceli ve gelinin ağzından. Kopyalayın, dijital kına davetiyenize tek tıkla ekleyin.",
  guncel=("2026-10-20", "20 Ekim 2026"),
  cta=("Seçtiğiniz sözle kına davetiyenizi hazırlayın", "Sözü kopyalayın, LaVie'de “Davet notu” alanına yapıştırın; bindallı renklerine uygun, zarfı açılan, müzikli ve katılım formlu dijital kına davetiyenizde anında görün. 500 TL, tek seferlik."),
  ilgili=[("davetiye-sozu-olusturucu","Davetiye sözü oluşturucu"),("davetli-listesi","Davetli listesi aracı"),("tarihi-kaydet-mesaji","Tarihi kaydedin mesajı"),("dugun-geri-sayim","Düğün geri sayım")],
  h1=("Kına Davetiyesi", "Sözleri"),
  giris="Kına gecesi, gelinin baba evinden uğurlandığı hem hüzünlü hem neşeli bir gecedir. Davetiyedeki söz de bu duyguyu taşımalı. Aşağıdaki örnekleri olduğu gibi kullanabilir ya da kendinize göre değiştirebilirsiniz.",
  bolumler=[
   ("Duygusal kına davetiyesi sözleri", ["Gelinin ailesinden uğurlanışını anlatan sözler kına gecesinin ruhuna en çok yakışanlardır."],
    ["Kızımızı baba evinden uğurlarken bu anlamlı gecede yanımızda olmanızı dileriz.",
     "Ellerimize kına, gönlümüze sevinç yakacağımız gecede sizi de bekliyoruz.",
     "Bir kız çocuğunun gelinliğe uzandığı bu gecede dualarınızla yanımızda olun.",
     "Annemizin gözyaşı, babamızın gururu; kına gecemizde siz de olun.",
     "Yuvamızdan yeni bir yuvaya uğurladığımız kızımızın kına gecesine davetlisiniz.",
     "Kınamız yakılırken sevdiklerimizi yanımızda görmek istiyoruz."], None),
   ("Geleneksel kına davetiyesi sözleri", ["Aile büyüklerinin ve komşuların da okuyacağı davetiyelerde geleneksel bir dil tercih edilir."],
    ["Kızımızın kına gecesinde sizleri de aramızda görmekten mutluluk duyarız.",
     "Hayırlı bir yuvanın ilk adımı olan kına gecemize teşriflerinizi rica ederiz.",
     "Gelinimizin kınasını birlikte yakmak üzere sizleri de davet ediyoruz.",
     "Ailelerimizin hayır dualarıyla kına gecemizi kutluyoruz. Varlığınız bizi mutlu edecek.",
     "Bu güzel gecede türkülerimize, dualarımıza ortak olmanızı dileriz."], None),
   ("Kısa kına davetiyesi sözleri", ["Sade tasarımlar ve hikâye paylaşımları için tek satırlık sözler:"],
    ["Kınamız var, sizi de bekleriz!",
     "Bu gece kına, yarın düğün. Bu gece bizimle olun.",
     "Ellerimiz kınalı, gönlümüz sizinle.",
     "Kına gecemizde sizi aramızda görmek isteriz.",
     "Bindallılar hazır, sıra sizde!",
     "Kınalı ellerle mutluluğa ilk adım."], None),
   ("Eğlenceli kına davetiyesi sözleri", ["Arkadaş ağırlıklı, temalı ya da eğlenceli bir kına planlıyorsanız:"],
    ["Halaylar, türküler ve bolca kahkaha. Kına gecemizde dans etmeye hazır olun!",
     "Gelin ağlatmaya değil, gelinle eğlenmeye geliyoruz!",
     "Bu gece kına yakılacak, pist yanacak. Kaçırmayın!",
     "Bekârlığın son gecesi, eğlencenin ilk gecesi.",
     "Kına bizden, eğlence sizden. Görüşmek üzere!",
     "Kınayı yakarız, sizi de beklerken çayı demleriz."], None),
   ("Gelinin ağzından kına davetiyesi sözleri", ["Davetiyeyi gelin kendi adına gönderiyorsa, özellikle arkadaşlarına ve kuzenlerine, birinci tekil ağızdan yazılmış samimi bir söz daha sıcak durur:"],
    ["Avucuma kına, kalbime sevinç yakılacak; o gece yanımda olmanı çok isterim.",
     "Baba evindeki son gecemde en sevdiklerimle olmak istiyorum. Kınama bekliyorum.",
     "Yıllardır her anımı paylaştığın gibi kına gecemi de benimle paylaş.",
     "Bindallımı giyip ağlayacağım, sonra da sabaha kadar oynayacağım. Sen de gel!",
     "Kınam yakılırken elimi tutacak dostlarımı arıyorum; ilk sen geldin aklıma.",
     "Annemin dualarıyla, dostlarımın kahkahalarıyla uğurlanmak istiyorum. Kına gecemde buluşalım.",
     "Bir avuç kına, bir ömürlük hatıra. O hatırada sen de ol."], None),
   ("Kına davetiyesine eklenebilecek notlar", ["Kına gecelerinde sık kullanılan notlar. LaVie'de katılım formunun üstüne ekleyebilirsiniz:"],
    None, ["Bindallı ya da kına kıyafetinizle gelebilirsiniz.", "Çocuklarımıza iyi uykular dileriz.", "Lütfen katılım durumunuzu bir hafta önce bildiriniz.", "Gece kadınlara özeldir."]),
  ],
  sss=[("Kına davetiyesi ne zaman gönderilir?", "Genellikle kına gecesinden 2-4 hafta önce gönderilir. Düğün davetiyesiyle birlikte de gönderilebilir."),
       ("Kına ve düğün için ayrı davetiye gerekir mi?", "Farklı gün ya da mekânda yapılıyorsa ayrı davetiye misafirlerin karıştırmasını önler. Aynı tasarımı seçerek iki davetiyeyi birbirine uyumlu yapabilirsiniz."),
       ("Kına davetiyesinde neler yazmalı?", "Gelinin ve ailenin adı, tarih, saat, adres ve kısa bir davet sözü yeterlidir. Kıyafet önerisi gibi notlar da eklenebilir."),
       ("Kına davetiyesini kim gönderir: gelin mi, aile mi?", "Geleneksel kınalarda davet genellikle gelinin ailesi adına yapılır ve sözde “kızımız” gibi ifadeler kullanılır. Arkadaş ağırlıklı kınalarda gelinin kendi ağzından yazılmış samimi bir söz de tercih edilebilir. İki gruba da aynı davetiyeyi gönderecekseniz aile adına yazılmış, sıcak bir dil herkese uyar."),
       ("Kına davetiyesi WhatsApp'tan gönderilebilir mi?", "Evet. Dijital kına davetiyesi bir bağlantı olarak WhatsApp'tan gönderilir; misafir bağlantıya dokunduğunda davetiye açılır, konuma tek dokunuşla yol tarifi alır ve katılım durumunu formdan bildirir. Büyükler için kısa ve nazik bir eşlik mesajı eklemek iyi olur; örnek mesajlar rehberimizdeki WhatsApp'tan davetiye gönderme yazısında yer alıyor.")]),

 dict(slug="nisan-davetiyesi-sozleri", kisa="Nişan davetiyesi sözleri", tur="Nişan",
  title="Nişan Davetiyesi Sözleri: 33 Resmi, Romantik ve Kısa Örnek | LaVie",
  desc="Nişan davetiyesi için 33 söz: resmi, romantik, kısa, modern ve aile ağzından. Davetiyede ne yazılır, kimin adı geçer? Kopyalayıp hemen kullanın.",
  guncel=("2026-10-21", "21 Ekim 2026"),
  cta=("Seçtiğiniz sözle nişan davetiyenizi hazırlayın", "Sözü kopyalayın, LaVie'de “Davet notu” alanına yapıştırın; iki ailenin adı, yüzük töreni saati ve konumuyla zarfı açılan, müzikli ve katılım formlu dijital nişan davetiyeniz anında hazır. 500 TL, tek seferlik."),
  ilgili=[("davetiye-sozu-olusturucu","Davetiye sözü oluşturucu"),("davetli-listesi","Davetli listesi aracı"),("tarihi-kaydet-mesaji","Tarihi kaydedin mesajı"),("2027-dugun-takvimi","2027 düğün takvimi")],
  h1=("Nişan Davetiyesi", "Sözleri"),
  giris="Nişan, iki ailenin bir araya geldiği ve çiftin birbirine resmen söz verdiği ilk büyük adımdır. Davetiyedeki sözün de bu ciddiyeti ve sevinci birlikte taşıması güzel olur. İşte farklı tarzlarda 33 örnek ve davetiyeye neler yazılacağına dair kısa bir kontrol listesi.",
  bolumler=[
   ("Resmi nişan davetiyesi sözleri", ["Aile büyüklerinin davetli olduğu nişanlar için:"],
    ["Ailelerimizin uygun görmesiyle hayatımızı birleştirmeye ilk adımı atıyoruz. Nişan törenimizde sizleri de aramızda görmekten mutluluk duyarız.",
     "Evlatlarımızın nişan törenine teşriflerinizi rica ederiz.",
     "Yüzüklerimizi takacağımız bu özel günde dualarınızla yanımızda olmanızı dileriz.",
     "Hayırlı bir başlangıcın ilk adımında sizleri de aramızda görmek isteriz.",
     "İki ailenin bir araya geldiği bu güzel günde sizleri de bekliyoruz.",
     "Nişan törenimize katılarak bizleri onurlandırmanızı rica ederiz."], None),
   ("Romantik nişan davetiyesi sözleri", ["Daha kişisel ve sıcak bir dil isteyen çiftler için:"],
    ["Sevgimizi yüzüklerle taçlandırıyoruz. Bu mutlu anımızda yanımızda olun.",
     "Bir ömre uzanan yolun başındayız; ilk adımımızı sizinle atmak istiyoruz.",
     "Kalbimiz çoktan evet dedi, şimdi sıra yüzüklerde.",
     "Aşkımıza ilk resmi imzayı atıyoruz. Bu güzel anı sizinle paylaşmak istiyoruz.",
     "Birlikte geçecek bir ömrün ilk sözünü veriyoruz.",
     "Hikâyemizin yeni sayfasını sevdiklerimizle açmak istiyoruz."], None),
   ("Kısa nişan davetiyesi sözleri", ["Tek satırlık, sade sözler:"],
    ["Nişanlanıyoruz! Sizi de bekliyoruz.",
     "Yüzükler takılıyor, mutluluğumuza ortak olun.",
     "Bir söz, iki yüzük, sonsuz mutluluk.",
     "Nişan törenimize davetlisiniz.",
     "Mutluluğumuzu sizinle paylaşmak istiyoruz.",
     "İlk adımımızda yanımızda olun."], None),
   ("Aile ağzından nişan davetiyesi sözleri", ["Davetiyeyi aileler adına göndermek isteyenler için:"],
    ["Kızımız ile oğlumuzun nişan törenine sizleri de davet ediyoruz.",
     "Evlatlarımızın mutluluğunu paylaşmak üzere nişan törenimize bekleriz.",
     "Çocuklarımızın hayırlı bir yuvaya ilk adımında dualarınızla yanımızda olun.",
     "İki aile olarak bu sevinçli günümüzü sizlerle paylaşmak istiyoruz.",
     "Nişanlarına şahitlik etmeniz dileğiyle, varlığınız bizi onurlandıracaktır.",
     "Sevincimize ortak olmanızı dileriz.",
     "Yüzüklerini takacağımız evlatlarımız için dualarınızı bekliyoruz."], None),
   ("Modern ve samimi nişan davetiyesi sözleri", ["Davetlilerin çoğu arkadaşlarınızsa ya da daha rahat bir kutlama planlıyorsanız, gündelik dile yakın sözler daha içten durur:"],
    ["Uzun zamandır beklenen haber geldi: nişanlanıyoruz! Bu akşam bizimle kutlayın.",
     "Önce bir kahveyle başladı, şimdi yüzüklerle devam ediyor. Nişanımızda görüşmek üzere.",
     "Soru soruldu, cevap evet. Sıra sizi aramızda görmekte.",
     "Yüzükler hazır, müzik hazır, tek eksik sizsiniz.",
     "Bir hayatı paylaşmaya karar verdik; ilk kutlamayı sizinle yapmak istiyoruz.",
     "Nişanlı olarak ilk fotoğrafımızda sizin de olmanızı isteriz.",
     "Söz verdik, yüzüğü takıyoruz. Gelin, bu mutluluğu birlikte büyütelim.",
     "Takvimlerinizi işaretleyin: el ele verdiğimiz günde sizi de bekliyoruz."], None),
   ("Nişan davetiyesinde neler yazmalı?", ["Söz kadar önemli olan, misafirin aklında soru bırakmamaktır. Nişan davetiyesinde şu bilgilerin bulunması yeterlidir:"],
    None, ["Çiftin adları; isterseniz iki ailenin soyadları ya da anne-baba adları",
           "Tarih ve saat; yüzük töreni ayrı bir saatteyse o saati de belirtin",
           "Mekânın adı ve açık adresi; dijital davetiyede tek dokunuşla yol tarifi",
           "Kısa bir davet sözü (yukarıdaki örneklerden biri)",
           "Katılım bildirimi: hangi tarihe kadar ve nasıl bildirileceği",
           "Gerekiyorsa kıyafet önerisi, çocuklarla ilgili not ya da otopark bilgisi"]),
  ],
  sss=[("Nişan davetiyesi ne zaman gönderilir?", "Genellikle nişandan 2-4 hafta önce gönderilir. Kısa sürede planlanan nişanlarda dijital davetiye aynı gün ulaştığı için büyük kolaylık sağlar."),
       ("Nişan davetiyesinde aile isimleri yazılmalı mı?", "Zorunlu değildir ama nişan iki ailenin buluşması olduğu için aile isimlerini yazmak yaygın ve şık bir tercihtir."),
       ("Nişan ve düğün davetiyesi aynı tasarımda olabilir mi?", "Evet. Aynı tasarımı iki davetiyede de kullanmak bütünlük sağlar; LaVie'de davet türünü değiştirdiğinizde başlık kendiliğinden güncellenir."),
       ("Nişan davetiyesini kim gönderir?", "Geleneksel nişanlarda davet çoğunlukla kız tarafı ya da iki aile adına yapılır ve sözde “evlatlarımız” gibi ifadeler kullanılır. Çiftin kendi düzenlediği, arkadaş ağırlıklı nişanlarda ise davetin çiftin ağzından yazılması daha doğal durur. Önemli olan iki ailenin de bu konuda önceden anlaşmasıdır."),
       ("Nişan davetiyesi WhatsApp'tan gönderilebilir mi?", "Evet. Dijital nişan davetiyesi tek bir bağlantıdır; WhatsApp'tan gönderildiğinde misafir bağlantıya dokunup davetiyeyi açar, konuma yol tarifi alır ve katılımını formdan bildirir. Aile büyükleri için bağlantının üstüne kısa, nazik bir mesaj eklemek iyi olur."),
       ("Nişan davetiyesine söz kesimi ya da yüzük töreni yazılır mı?", "Yüzük töreni nişanın kendisidir; ayrıca belirtmek isterseniz “Yüzük töreni saat 20.00'de” gibi bir not ekleyebilirsiniz. Söz kesimi ayrı bir gün yapılıyorsa onun için ayrı bir söz davetiyesi göndermek karışıklığı önler.")]),

 dict(slug="lcv-nedir", kisa="LCV nedir?", tur="Düğün",
  guncel=("2026-10-22", "22 Ekim 2026"),
  ilgili=[("davetli-listesi","Davetli listesi aracı"),("tarihi-kaydet-mesaji","Tarihi kaydedin mesajı"),("dugun-geri-sayim","Düğün geri sayım")],
  cta=("LCV'yi telefonla değil, davetiyenizle toplayın", "LaVie dijital davetiyenizde katılım formu hazır gelir: misafir adını ve kaç kişi geleceğini yazar, yanıt anında panelinize düşer, listeyi Excel'e aktarırsınız. 500 TL, tek seferlik."),
  title="LCV Nedir, Açılımı Ne? Davetiyede LCV Nasıl Yazılır | LaVie",
  desc="LCV açılımı: Lütfen Cevap Veriniz. Davetiyede LCV nasıl yazılır, misafir nasıl cevap verir, son tarih ne olmalı? Hazır LCV ve hatırlatma mesajı örnekleri.",
  h1=("LCV", "nedir?"),
  giris="Davetiyelerin altında sık sık gördüğünüz 'LCV' kısaltması, 'Lütfen Cevap Veriniz' anlamına gelir. Fransızcadaki RSVP (répondez s'il vous plaît) ifadesinin Türkçe karşılığıdır. Davet sahibinin, misafirden gelip gelmeyeceğini bildirmesini rica ettiğini gösterir.",
  bolumler=[
   ("LCV neden önemli?", ["Düğün, nişan ya da kına gibi kalabalık davetlerde kaç kişinin geleceğini bilmek; salon, masa düzeni, yemek ve ikram sayısını belirlemek için gereklidir. Fazla sipariş israfa, eksik sipariş ise misafirlerin mağdur olmasına yol açar.",
     "LCV aynı zamanda misafire karşı bir nezakettir: davetin ciddi ve planlı olduğunu, katılımının önemsendiğini gösterir."], None, None),
   ("Davetiyede LCV nasıl yazılır?", ["Klasik kâğıt davetiyelerde LCV genellikle davetiyenin alt köşesine, bir veya iki telefon numarasıyla yazılır. Örnekler:"],
    ["LCV: Ayşe Yılmaz 0532 000 00 00",
     "Katılım durumunuzu 1 Haziran'a kadar bildirmenizi rica ederiz.",
     "Lütfen katılım durumunuzu düğünden bir hafta önce bildiriniz.",
     "Gelip gelemeyeceğinizi bize bildirirseniz çok seviniriz."], None),
   ("LCV toplamanın zorlukları", ["Telefonla LCV toplamak yüzlerce davetlide çok zaman alır. Mesajlar karışır, kimin kaç kişiyle geleceği not edilmeyi unutulur, son hafta herkes tek tek aranır."],
    None, ["Yanıtlar farklı kişilere (anne, baba, çift) dağınık gelir", "Kaç kişi gelineceği çoğu zaman belirsiz kalır", "Yanıt vermeyenleri takip etmek zordur", "Son dakika değişiklikleri listeye işlenmez"]),
   ("Dijital davetiyede LCV nasıl çalışır?", ["Dijital davetiyede LCV bir form olarak davetiyenin içindedir. Misafir davetiyeyi açtığında adını yazar, gelip gelmeyeceğini ve kaç kişi olacağını iki dokunuşla bildirir. Yanıt anında davet sahibinin paneline düşer.",
     "LaVie davetiyelerinde panelinizde gelecek ve gelemeyecek kişi sayılarını, toplam kişi sayısını ve isim listesini canlı görürsünüz; listeyi tek tuşla Excel'e aktarıp salon ve catering firmasıyla paylaşabilirsiniz."], None, None),
   ("LCV için son tarih ne olmalı?", ["Salon ve catering firmaları genellikle kesin sayıyı düğünden 7-10 gün önce ister. LCV son tarihini bundan birkaç gün öncesine koymak, yanıt vermeyenlere hatırlatma yapmak için size zaman kazandırır."], None, None),
   ("Yanıt vermeyenlere LCV hatırlatma mesajı örnekleri", ["Son tarih yaklaştığında yanıt vermeyen misafirlere kısa ve nazik bir hatırlatma göndermek yeterlidir. Suçlayıcı değil, davet eden bir dil kullanın; davetiye bağlantısını mesajın altına yeniden ekleyin:"],
    ["Merhaba, düğünümüz için hazırlıklar hızlandı. Katılım durumunuzu davetiyedeki formdan bu hafta içinde bildirirseniz çok seviniriz.",
     "Sevgili misafirimiz, masa düzenini tamamlamak üzereyiz. Gelip gelemeyeceğinizi ve kaç kişi olacağınızı bize iletebilir misiniz?",
     "Küçük bir hatırlatma: Kına gecemiz için katılım yanıtlarını cuma gününe kadar topluyoruz. Sizi aramızda görmeyi çok isteriz.",
     "Merhaba, yoğunlukta gözden kaçmış olabilir diye yazıyoruz. Davetiyemize aşağıdaki bağlantıdan ulaşıp katılım durumunuzu iki dokunuşla bildirebilirsiniz.",
     "Değerli büyüğümüz, nişanımızda sizi de aramızda görmek isteriz. Gelebilecekseniz kısa bir mesajla haber vermeniz yeterli."], None),
   ("Misafir olarak LCV'ye nasıl cevap verilir?", ["Davetiyede LCV gördüyseniz, son tarihi beklemeden kısa bir yanıt vermek en nazik davranıştır. Gelecekseniz kaç kişi olacağınızı mutlaka yazın; davetiyede adı geçmeyen birini getirmek istiyorsanız önce davet sahibine sorun. Gelemeyecekseniz bunu da bildirin; sessiz kalmak, davet sahibinin sizi gelecek gibi saymasına yol açabilir."],
    ["Davetiniz için çok teşekkür ederiz, eşimle birlikte 2 kişi olarak katılacağız.",
     "Bu güzel gününüzde yanınızda olmayı çok isterdik ama o tarihte şehir dışında olacağız. Şimdiden mutluluklar dileriz.",
     "Davetinizi aldık, çok sevindik! Ben tek başıma geleceğim; görüşmek üzere.",
     "Katılmayı çok istiyoruz ama programımız henüz kesinleşmedi. En geç bu hafta sonu kesin haber vereceğiz."], None),
  ],
  sss=[("LCV açılımı nedir?", "LCV, 'Lütfen Cevap Veriniz' ifadesinin kısaltmasıdır. Uluslararası karşılığı RSVP'dir."),
       ("LCV'ye cevap vermek zorunlu mu?", "Zorunlu değildir ama nezaket gereği beklenir. Davet sahibinin hazırlık yapabilmesi için gelip gelmeyeceğinizi bildirmeniz önemlidir."),
       ("Dijital davetiyede LCV nasıl toplanır?", "Davetiyenin içindeki katılım formuyla. Misafir formu doldurur, yanıt davet sahibinin paneline anında düşer; telefonla tek tek aramaya gerek kalmaz."),
       ("LCV ile RSVP arasında fark var mı?", "Anlam olarak fark yoktur. RSVP Fransızca “répondez s'il vous plaît” ifadesinin, LCV ise Türkçe “Lütfen Cevap Veriniz” ifadesinin kısaltmasıdır. Türkçe davetiyelerde LCV yazmak daha anlaşılırdır."),
       ("LCV'ye cevap vermeyen misafir sayılmalı mı?", "Kesin sayıyı salona bildirmeden önce yanıt vermeyenlere bir kez nazikçe hatırlatma yapın. Yine de dönüş olmazsa, yakın akraba ve arkadaşları gelecek, uzak tanıdıkları gelmeyecek gibi düşünmek pratik bir yaklaşımdır; son kararı salonunuzun esneklik payına göre verin."),
       ("Davetiyeye kaç LCV numarası yazılmalı?", "Bir ya da iki numara yeterlidir; genellikle gelin ve damat tarafından birer kişi yazılır. Daha fazla numara, yanıtların dağılmasına yol açar. Dijital davetiyede numara yazmak yerine katılım formunu kullanırsanız bütün yanıtlar tek bir listede toplanır.")]),

 dict(slug="davetiye-ne-zaman-gonderilir", kisa="Davetiye ne zaman gönderilir?", tur="Düğün",
  ilgili=[("dugun-geri-sayim","Düğün geri sayım"),("2027-dugun-takvimi","2027 düğün takvimi")],
  title="Düğün Davetiyesi Ne Zaman Gönderilir? Gün Gün Plan | LaVie",
  desc="Düğün, nişan ve kına davetiyesi ne zaman gönderilmeli? Kâğıt ve dijital davetiye için önerilen zamanlar, LCV son tarihi ve hatırlatma planı.",
  h1=("Davetiye ne zaman", "gönderilir?"),
  giris="Davetiyeyi çok erken göndermek unutulmasına, çok geç göndermek ise misafirlerin plan yapamamasına yol açar. Aşağıda düğün, nişan ve kına için önerilen zamanları ve dijital davetiyenin bu takvime getirdiği kolaylıkları bulacaksınız.",
  bolumler=[
   ("Düğün davetiyesi: 4-6 hafta önce", ["Düğün davetiyeleri genellikle düğünden 4-6 hafta önce gönderilir. Şehir dışından ya da yurt dışından gelecek misafirleriniz varsa 8 hafta öncesi daha uygun olur; böylece yol ve konaklama planı yapabilirler.",
     "Kâğıt davetiyede baskı ve dağıtım 2-4 hafta sürebildiği için hazırlığa düğünden 2-3 ay önce başlamak gerekir. Dijital davetiye ise aynı gün hazırlanıp tek mesajla herkese ulaşır."], None, None),
   ("Nişan ve söz davetiyesi: 2-4 hafta önce", ["Nişan ve söz genellikle daha dar bir çevreyle ve daha kısa sürede planlanır. 2-4 hafta önce göndermek yeterlidir."], None, None),
   ("Kına davetiyesi: 2-4 hafta önce", ["Kına davetiyesi çoğunlukla düğün davetiyesiyle birlikte ya da kınadan 2-4 hafta önce gönderilir. İki davet farklı yerlerde yapılıyorsa ayrı davetiye göndermek karışıklığı önler."], None, None),
   ("Örnek takvim", ["Bir düğün için davetiye takvimini şöyle planlayabilirsiniz:"],
    None, ["8 hafta önce: Davetli listesini netleştirin, telefon numaralarını toplayın", "6 hafta önce: Davetiyeyi hazırlayıp gönderin", "3 hafta önce: Yanıt vermeyenlere nazik bir hatırlatma yapın", "10 gün önce: LCV'yi kapatın, kesin sayıyı salona bildirin", "1 gün önce: Konum ve saat için kısa bir hatırlatma mesajı atın"]),
   ("Dijital davetiyenin takvime katkısı", ["Dijital davetiye anında ulaştığı için son dakika davetleri de mümkündür. Saat ya da mekân değişirse panelden düzeltirsiniz; herkesin elindeki link aynı kalır, bilgi anında güncellenir. Katılım yanıtları da panelinize düştüğü için 3. ve 10. gün adımlarını telefonla uğraşmadan halledersiniz."], None, None),
  ],
  sss=[("Düğün davetiyesi en geç ne zaman gönderilmeli?", "En geç düğünden 3 hafta önce gönderilmesi önerilir. Daha geç gönderilen davetiyelerde misafirlerin planları çakışabilir."),
       ("Davetiyeyi WhatsApp'tan göndermek ayıp mı?", "Artık oldukça yaygın. Özenli tasarlanmış bir dijital davetiye linki, kişisel bir mesajla gönderildiğinde saygılı ve şık bir davet olarak karşılanır. İsterseniz yaşlı büyükleriniz için birkaç kâğıt davetiye de bastırabilirsiniz."),
       ("Davetiyeyi gönderdikten sonra bilgi değişirse ne yapmalıyım?", "Kâğıt davetiyede herkese tek tek haber vermek gerekir. Dijital davetiyede bilgiyi panelden güncellemeniz yeterlidir; link değişmeden herkes yeni bilgiyi görür.")]),

 dict(slug="soz-davetiyesi-sozleri", kisa="Söz davetiyesi sözleri", tur="Söz",
  title="Söz Davetiyesi Sözleri: 27 Kısa, Geleneksel ve Romantik Örnek | LaVie",
  desc="Söz töreni davetiyesi için 27 söz örneği: kısa, geleneksel, romantik, aile ağzından ve samimi. Davetiyede olması gereken bilgiler ve söz ile nişan farkı.",
  h1=("Söz Davetiyesi", "Sözleri"),
  giris="Söz töreni, kız isteme sonrasında iki ailenin evliliğe ilk resmî onayını verdiği, yüzüklerin kırmızı kurdeleyle bağlanıp kesildiği samimi bir buluşmadır. Genellikle dar bir aile çevresiyle yapıldığı için davetiyesinin de sıcak ve içten olması yakışır. Aşağıda farklı tarzlarda 27 söz davetiyesi sözü ve davetiyenizi hazırlarken işinize yarayacak pratik bilgiler bulacaksınız.",
  bolumler=[
   ("Kısa söz davetiyesi sözleri", ["Tek satırlık bir cümle, özellikle telefondan gönderilen davetiyelerde hem şık hem okunaklı durur. İsimleri ve tarihi ayrıca yazacağınız için sözün kısa olması yeterlidir."],
    ["Kurdelemizi sizinle kesmek istiyoruz.",
     "Birbirimize söz veriyoruz; şahidimiz olur musunuz?",
     "Bir ömrün ilk sözü için sizi de aramızda bekliyoruz.",
     "Kalplerimiz anlaştı, şimdi sıra ailelerimizde. Söz törenimize davetlisiniz.",
     "Yüzüklerimiz bağlanırken yanımızda olun.",
     "Küçük bir tören, büyük bir mutluluk. Sizi de bekliyoruz."], None),
   ("Geleneksel ve resmi söz davetiyesi sözleri", ["Aile büyüklerine hitap eden, ölçülü ve saygılı bir dil tercih ediyorsanız bu cümleler uygun olur. Özellikle davetiyeyi ailelerin göndereceği durumlarda tercih edilir."],
    ["Ailelerimizin rızası ve büyüklerimizin hayır dualarıyla söz takıyoruz. Bu güzel günümüzde sizleri de aramızda görmekten mutluluk duyarız.",
     "Hayırlı bir yolun ilk adımını atarken dualarınızı ve varlığınızı bekliyoruz.",
     "Büyüklerimizin huzurunda birbirimize söz vereceğimiz bu anlamlı günde teşriflerinizi rica ederiz.",
     "İki ailenin gönül birliğini taçlandıracağımız söz törenimize sizleri de davet etmekten onur duyarız.",
     "Hayırlısıyla verilecek sözümüze şahitlik etmeniz bizi çok mutlu edecektir.",
     "Allah'ın izniyle başlayan bu yolda ilk sözümüzü veriyoruz; sevincimize ortak olmanızı dileriz."], None),
   ("Romantik söz davetiyesi sözleri", ["Davetiyeyi çift olarak kendi ağzınızdan yazmak istiyorsanız daha kişisel ve duygusal cümleler seçebilirsiniz."],
    ["Bir kurdelenin iki ucunda başlayan hikâyemiz, bugün aynı yüzükte buluşuyor.",
     "Seni seçtim, sen de beni. Şimdi bu sözü sevdiklerimizin önünde vermek istiyoruz.",
     "Birlikte kurduğumuz hayallerin ilk adımını sizinle paylaşmak istiyoruz.",
     "Gözlerimizle çoktan verdiğimiz sözü bu kez herkesin önünde veriyoruz.",
     "Aynı yöne bakmaya karar verdik. Bu kararın ilk kutlamasında yanımızda olun.",
     "Parmağımızdaki kurdele kesildiğinde, hikâyemizin en güzel bölümü başlayacak. O anı sizinle yaşamak istiyoruz."], None),
   ("Aile ağzından söz davetiyesi sözleri", ["Söz töreni çoğu zaman kız evinde, ailelerin ev sahipliğinde yapılır. Davetiyeyi anne ve babaların adına yazmak bu yüzden oldukça yerinde olur."],
    ["Kızımız Zeynep ile oğlumuz Emre'nin söz törenine sizleri de bekliyoruz.",
     "Evlatlarımızın mutluluğa attığı ilk adımda sevincimize ortak olmanızı dileriz.",
     "Aksoy ve Kaya aileleri olarak çocuklarımızın söz merasimine teşriflerinizi rica ederiz.",
     "Evimizin kapısını bu kez çok güzel bir haber için açıyoruz. Söz törenimizde aramızda olmanızı isteriz.",
     "Gönülden dilediğimiz bu birlikteliğin ilk sözünde dualarınızla yanımızda olun."], None),
   ("Samimi ve eğlenceli söz davetiyesi sözleri", ["Davetliler çoğunlukla yakın akrabalar ve dostlarsa biraz neşe katmaktan çekinmeyin."],
    ["Kahveler içildi, cevap 'evet' oldu! Şimdi sıra kurdele kesmekte.",
     "Tuzlu kahveyi içen damadımız sınavı geçti; söz törenine bekleriz!",
     "Kurdele makası hazır, çikolatalar paketlendi. Bir tek siz eksiksiniz.",
     "Resmen söz kesiyoruz! Bu tarihi anı kaçırmayın."], None),
   ("Söz davetiyesine neler yazılmalı?", ["Söz töreni daha küçük bir buluşma olsa da davetiyede temel bilgilerin eksiksiz olması misafirlerinizin işini kolaylaştırır. Tören evde yapılıyorsa adresi kat, daire ve tarif bilgisiyle yazmak özellikle önemlidir."],
    None, ["Çiftin adları (isteğe bağlı olarak ailelerin adları)", "Tarih, gün ve saat", "Törenin yapılacağı yer: ev adresi ya da mekânın adı ve açık adresi", "Kısa bir davet sözü", "Haritada konum bağlantısı", "Katılım bildirme (LCV) yöntemi ve son tarihi", "Varsa kısa notlar: otopark, kıyafet önerisi ya da 'tören aile arasında yapılacaktır' gibi"]),
   ("Söz, kız isteme ve nişan arasındaki fark", ["Bu üç adım bölgeden bölgeye ve aileden aileye farklı yaşanabilir; aşağıdaki açıklama en yaygın uygulamayı özetler.",
     "Kız isteme, damat tarafının kız evine gidip izin istediği ilk ziyarettir. Söz, bu iznin ardından iki ailenin evliliğe onay verdiğini gösteren törendir; genellikle bir kurdeleyle birbirine bağlanmış yüzükler takılır ve kurdeleyi ailenin bir büyüğü keser. Bazı aileler kız isteme ile sözü aynı gün yapar. Nişan ise daha kalabalık bir davetli listesiyle, çoğunlukla bir salonda ya da bahçede düzenlenen, takıların takıldığı daha büyük bir kutlamadır.",
     "Söz töreni küçük olduğu için çoğu çift ayrı bir davetiye bastırmaz; telefonla haber vermek ya da kısa bir mesaj göndermek yaygındır. Dijital davetiye bu iki seçeneğin arasında güzel bir yol sunar: özenli bir davetiye hazırlarsınız ama baskı ve dağıtım uğraşına girmezsiniz."], None, None),
  ],
  sss=[("Söz töreni için davetiye gerekli mi?", "Zorunlu değildir. Söz genellikle dar bir çevreyle yapıldığı için birçok aile telefonla davet eder. Ancak tarih, saat ve adresi tek bir yerde toplayan bir davetiye, özellikle evi ilk kez görecek misafirler için karışıklığı önler."),
       ("Söz davetiyesi ne zaman gönderilmeli?", "Genellikle törenden 2-3 hafta önce göndermek yeterlidir. Söz kısa sürede planlandıysa bir hafta önce gönderilen dijital davetiye de misafirlerinize rahatça ulaşır."),
       ("Söz davetiyesini kim gönderir?", "Geleneksel olarak tören kız evinde yapıldığı için davet çoğunlukla kız tarafı ailesinden gelir. Günümüzde çiftin kendi ağzından yazdığı ya da iki ailenin adının birlikte yer aldığı davetiyeler de yaygındır."),
       ("Bu sözleri dijital davetiyede kullanabilir miyim?", "Evet. LaVie'de söz türünü seçip beğendiğiniz cümleyi 'Davet notu' alanına yapıştırmanız yeterli; telefondaki önizlemede anında görünür ve sonradan panelinizden değiştirebilirsiniz.")]),

 dict(slug="dijital-davetiye-nasil-yapilir", kisa="Dijital davetiye nasıl yapılır?", tur="Düğün",
  ilgili=[("davetiye-sozu-olusturucu","Davetiye sözü oluşturucu"),("davetli-listesi","Davetli listesi aracı"),("dugun-hashtag-olusturucu","Düğün hashtag oluşturucu")],
  title="Dijital Davetiye Nasıl Yapılır? Adım Adım Rehber | LaVie",
  desc="Dijital davetiye nasıl yapılır? Hazırlamanız gereken bilgiler, tasarım ve davet sözü seçimi, konum ve program ekleme, paylaşım ve LCV takibi: adım adım anlatım.",
  h1=("Dijital Davetiye", "Nasıl Yapılır?"),
  giris="Dijital davetiye; telefonla açılan, içinde tarih, saat, konum, program ve katılım formu bulunan bir davetiye sayfasıdır. Misafir linke dokunur, davetiye tarayıcıda açılır; uygulama indirmesi gerekmez. Hazırlamak için tasarım bilgisine de ihtiyacınız yok. Bu rehberde düğün, nişan, kına ya da söz için dijital davetiyeyi baştan sona nasıl hazırlayacağınızı, LaVie oluşturucusu üzerinden adım adım anlatıyoruz.",
  bolumler=[
   ("Başlamadan önce: hazır etmeniz gereken bilgiler", ["Oluşturucuyu açmadan önce aşağıdaki bilgileri bir kenara not etmek işinizi çok hızlandırır. Bilgiler hazırsa davetiyenin ilk hâlini birkaç dakikada çıkarabilirsiniz; eksik kalanları sonradan da ekleyebilirsiniz.",
     "Özellikle mekân adresini ve saati aileyle bir kez daha teyit edin. Dijital davetiyede bilgiyi sonradan düzeltmek kolaydır ama misafirin ilk gördüğü bilginin doğru olması her zaman daha iyidir."],
    None, ["Davet türü: düğün, nişan, kına ya da söz", "Gelin ve damadın adları, isteniyorsa ailelerin adları", "Tarih ve saat", "Mekânın adı ve açık adresi", "Mekânın Google Haritalar bağlantısı", "Program akışı (karşılama, nikâh, yemek, eğlence gibi)", "Kısa bir davet sözü", "Varsa katılım formunun üstünde görünecek bir not (son yanıt tarihi, kıyafet önerisi gibi)"]),
   ("1. adım: Davet türünü, tasarımı ve davet sözünü seçin", ["LaVie'de önce davet türünü seçersiniz; davetiyenin başlığı seçiminize göre 'Evleniyoruz', 'Nişanlanıyoruz' ya da 'Kına gecemize davetlisiniz' şeklinde kendiliğinden değişir. Ardından tasarımlar arasından size yakışanı seçin. Her tasarım gerçek bir davetiye olarak açılır; zarfına dokunup müziğini dinleyerek nasıl görüneceğini önceden görebilirsiniz.",
     "Sonra isimlerinizi yazın ve isimler için bir yazı stili seçin. 'Davet notu' alanına da davetiyenin kalbi olan kısa sözü yazın. Bir ya da iki cümle yeterlidir; tarih ve mekân zaten ayrı bölümlerde göründüğü için sözü bilgiyle doldurmanıza gerek yok. Fikir isterseniz aşağıdaki cümlelerden birini kullanabilir ya da rehberimizdeki söz yazılarına göz atabilirsiniz."],
    ["Hayatımızı birleştirdiğimiz bu güzel günde sizi de yanımızda görmek istiyoruz.",
     "Sevdiklerimizle paylaşmadan eksik kalacak bir mutluluğa sizi davet ediyoruz.",
     "Ailelerimizin dualarıyla çıktığımız bu yolun ilk gününde aramızda olun.",
     "Bir ömürlük hikâyemizin ilk sayfasını sizinle birlikte açmak istiyoruz."], None),
   ("2. adım: Tarih, saat, mekân ve konumu ekleyin", ["Tarih ve saati girdiğiniz anda davetiyedeki geri sayım da çalışmaya başlar. Mekân adını ve açık adresi yazdıktan sonra konum bağlantısını eklemeyi unutmayın: misafirleriniz davetiyeden tek dokunuşla yol tarifi alabilir. Bu, özellikle şehir dışından gelenler ve mekânı ilk kez görecek misafirler için büyük kolaylıktır.",
     "Google Haritalar bağlantısını almak için şu adımları izleyin:"],
    None, ["Google Haritalar'da mekânın adını aratıp açın", "'Paylaş' düğmesine dokunun", "'Bağlantıyı kopyala' seçeneğiyle linki kopyalayın", "Kopyaladığınız linki oluşturucudaki 'Konum linki' alanına yapıştırın", "Önizlemede konum düğmesine dokunup doğru yeri açtığını kontrol edin"]),
   ("3. adım: Program akışını ve katılım notunu yazın", ["Program bölümü, misafirlerin gecenin nasıl ilerleyeceğini bilmesini sağlar; kimin hangi saatte gelmesi gerektiği konusundaki soruları da azaltır. Oluşturucuda her satıra bir program maddesi yazmanız yeterlidir. Saatleri gerçekçi tutun; misafirler çoğunlukla davetiyedeki ilk saate göre yola çıkar.",
     "Katılım notu ise katılım formunun hemen üstünde görünür. Buraya son yanıt tarihini ya da misafirin bilmesi gereken kısa bir bilgiyi yazabilirsiniz. Oluşturucudaki hazır cümlelerden birine dokunabilir ya da kendi notunuzu yazabilirsiniz. Örnek bir program şöyle görünebilir:"],
    None, ["19:30 Karşılama", "20:00 Nikâh töreni", "20:30 Akşam yemeği", "22:00 Eğlence"]),
   ("4. adım: Müziği seçin ve önizlemede kontrol edin", ["Davetiye zarfı açıldığında seçtiğiniz müzik çalmaya başlar. Listeden parçalara dokunarak dinleyebilir, davetinizin havasına uyanı seçebilirsiniz.",
     "Yazdığınız her şey ekranın yanındaki telefon önizlemesinde anında görünür; isterseniz önizlemeyi tam ekran açabilirsiniz. Siparişi vermeden önce davetiyeyi bir misafirin gözüyle baştan sona gezin. Şu noktaları kontrol etmenizi öneririz:"],
    None, ["İsimlerin yazımı ve Türkçe karakterler doğru mu?", "Tarih, gün ve saat birbiriyle uyumlu mu?", "Adres eksiksiz, konum düğmesi doğru yeri açıyor mu?", "Program saatleri mekânla konuştuğunuz saatlerle aynı mı?", "Davet sözü ve katılım notunda yazım hatası var mı?", "Müzik davetin havasına uyuyor mu?"]),
   ("5. adım: Siparişi tamamlayın ve linkinizi alın", ["Davetiyenizi beğendiğinizde telefon numaranızı yazıp siparişi oluşturursunuz. LaVie'de önce davetiyeyi görür, beğendikten sonra ödersiniz; ödeme 500 TL ve tek seferliktir, abonelik yoktur. Kartla (Shopier güvencesiyle) ya da IBAN ile havaleyle ödeyebilirsiniz. Kartla ödemede davetiyeniz otomatik olarak açılır; havalede ödeme onaylandıktan sonra linkiniz genellikle aynı gün yayına girer.",
     "Ödemenin ardından iki link alırsınız: misafirlerinize göndereceğiniz davetiye linki ve yalnızca sizin kullanacağınız panel linki. Panel linkini misafirlerle paylaşmayın; katılım listesi ve düzenleme ayarları oradadır.",
     "Konsepti, renkleri ya da düzeni tamamen size özel bir davetiye istiyorsanız Profesyonel Tasarım paketini de seçebilirsiniz. Bu pakette ayrıntıları WhatsApp'tan konuşur, tasarımı sınırsız revizyonla birlikte hazırlarız; fiyat tasarımın kapsamına göre 2.000 TL'den başlar."], None, None),
   ("6. adım: Davetiyeyi paylaşın", ["Davetiye linkini WhatsApp, SMS ya da sosyal medya üzerinden dilediğiniz kadar kişiye gönderebilirsiniz; misafir sayısında bir sınır yoktur. Linki çıplak göndermek yerine kısa ve kişisel bir mesajla göndermek davete sıcaklık katar. Aile büyüklerine göndermeden önce bir telefonla haber vermek de hâlâ çok makbul bir inceliktir.",
     "Linki göndermeden önce kendi telefonunuzdan bir kez açıp denemenizi öneririz. Örnek paylaşım mesajları:"],
    ["Sevgili Ayşe Teyze, hayatımızın en güzel gününde sizi de aramızda görmek istiyoruz. Davetiyemiz bu linkte, katılımınızı da buradan bildirebilirsiniz.",
     "Merhaba! Düğünümüze davetlisin. Tarih, konum ve program davetiyede; gelip gelemeyeceğini formdan bildirirsen çok seviniriz.",
     "Değerli komşularımız, kızımızın kına gecesine sizleri de bekliyoruz. Ayrıntılar davetiyemizde."], None),
   ("7. adım: Katılımları panelden takip edin", ["Misafirleriniz davetiyedeki formdan gelip gelmeyeceğini ve kaç kişi olacağını bildirir; her yanıt anında panelinize düşer. Gelecek, gelemeyecek ve toplam kişi sayısını tek bakışta görür, isim listesini Excel'e aktarıp salon ya da catering firmasıyla paylaşabilirsiniz. Misafirlerin hatıra defterine bıraktığı güzel sözler de panelinizde saklanır.",
     "Bir bilgi değişirse, örneğin saat kayarsa ya da program güncellenirse, panelden kendiniz düzeltirsiniz. Davetiyenin linki değişmez; daha önce linki alan herkes yeni bilgiyi görür. Yine de saat ya da mekân gibi önemli bir değişiklikte misafirlere kısa bir bilgilendirme mesajı atmak iyi olur. Yanıt vermeyenlere de son tarihten birkaç gün önce nazik bir hatırlatma yapabilirsiniz."], None, None),
   ("Sık yapılan hatalar", ["Dijital davetiye hazırlamak kolaydır ama birkaç küçük ayrıntı gözden kaçabiliyor. Göndermeden önce bunlara dikkat edin:"],
    None, ["Konum linkini eklememek ya da yanlış şubenin konumunu eklemek", "Davet sözünü çok uzun tutmak; asıl bilgiler gölgede kalır", "Katılım için son tarih belirtmemek", "Panel linkini yanlışlıkla misafir grubuna göndermek", "Linki kendi telefonunda denemeden toplu göndermek", "Davetiyeyi çok erken ya da çok geç göndermek; düğünler için genellikle 4-6 hafta önce gönderilir"]),
  ],
  sss=[("Dijital davetiye hazırlamak ne kadar sürer?", "Bilgileriniz hazırsa davetiyenin ilk hâlini birkaç dakikada oluşturabilirsiniz. LaVie'de ödeme onaylandıktan sonra davetiye linkiniz genellikle aynı gün açılır; kartla ödemede otomatik olarak açılır."),
       ("Dijital davetiyeyi ücretsiz yapabilir miyim?", "Ücretsiz görsel davetiye şablonları bulunabilir; ancak bunlar genellikle tek bir resimden ibarettir. Katılım formu, panel, konum, geri sayım ve sonradan düzenleme gibi özellikler isterseniz LaVie'de davetiyeyi ödeme yapmadan önce canlı önizlemede ücretsiz deneyebilir, beğenirseniz 500 TL tek seferlik ödemeyle yayına alabilirsiniz."),
       ("Misafirlerin dijital davetiyeyi açmak için uygulama indirmesi gerekir mi?", "Hayır. Davetiye bir link olarak paylaşılır ve telefonun tarayıcısında açılır. Akıllı telefonu olan herkes linke dokunarak davetiyeyi görebilir."),
       ("Davetiyeyi gönderdikten sonra bilgileri değiştirebilir miyim?", "Evet. Saat, mekân, program, davet notu, tasarım, yazı stili ve müziği panelinizden dilediğiniz zaman değiştirebilirsiniz. Link aynı kaldığı için davetiyeyi yeniden göndermeniz gerekmez.")]),

 dict(slug="dijital-davetiye-fiyatlari", kisa="Dijital davetiye fiyatları", tur="Düğün",
  ilgili=[("dugun-butcesi-hesaplama","Düğün bütçesi hesaplama"),("davetli-listesi","Davetli listesi aracı")],
  title="Dijital Davetiye Fiyatları: Fiyatı Neler Belirler? | LaVie",
  desc="Dijital davetiye fiyatları neye göre değişir? Görsel davetiye ile davetiye sitesi farkı, tek seferlik ödeme ve abonelik, gizli maliyetler, kâğıt davetiyeyle karşılaştırma ve LaVie fiyatları.",
  h1=("Dijital Davetiye", "Fiyatları"),
  giris="Dijital davetiye ararken çok farklı fiyatlarla karşılaşırsınız: bir yanda ücretsiz şablonlar, öbür yanda kişiye özel tasarlanan davetiye siteleri. Bu farkın sebebi çoğu zaman ilk bakışta görünmez. Bu rehberde dijital davetiyenin fiyatını hangi unsurların belirlediğini, teklifleri karşılaştırırken nelere bakmanız gerektiğini ve LaVie'de neyin ne kadar tuttuğunu açıkça anlatıyoruz. Başka firmaların fiyatlarını burada listelemiyoruz; fiyatlar sık değiştiği için en doğrusu her teklifi aşağıdaki sorularla kendiniz değerlendirmenizdir.",
  bolumler=[
   ("Dijital davetiye fiyatını belirleyen unsurlar", ["İki dijital davetiye aynı görünse bile içerdikleri özellikler çok farklı olabilir. Fiyatı asıl belirleyen, davetiyenin ne kadar 'iş' yaptığıdır: yalnızca bilgi mi veriyor, yoksa katılımları toplayıp size bir liste mi sunuyor? Teklifleri karşılaştırırken şu başlıklara bakın:"],
    None, ["Biçim: tek bir resim ya da video mu, yoksa linkle açılan bir davetiye sayfası mı?", "Tasarım: hazır şablon mu, size özel hazırlanan bir tasarım mı?", "Katılım formu (LCV) ve yanıtları gördüğünüz bir panel var mı?", "Konum, geri sayım, program akışı ve müzik gibi bölümler dahil mi?", "Gönderdikten sonra bilgileri düzeltebiliyor musunuz, bunun ek ücreti var mı?", "Misafir ya da paylaşım sayısında sınır var mı?", "Ödeme tek seferlik mi, aylık ya da yıllık mı?", "Revizyon hakkı ve destek nasıl veriliyor?"]),
   ("Görsel davetiye ile davetiye sitesi arasındaki fark", ["Fiyat farkının en büyük kaynağı biçimdir. Görsel davetiye; WhatsApp'tan resim ya da kısa video olarak gönderilen, kâğıt davetiyenin dijital bir kopyası gibi düşünülebilecek bir dosyadır. Hazırlaması kolaydır, bu yüzden ücretsiz ya da düşük ücretli seçenekleri çoktur. Ancak gönderildikten sonra değiştirilemez; saat kayarsa yeni bir görsel hazırlayıp herkese yeniden göndermeniz gerekir. Katılım bilgisini de yine telefonla ya da mesajla tek tek toplarsınız.",
     "Davetiye sitesi ise misafirin telefonunda açılan bir sayfadır. İçinde konum düğmesi, geri sayım, program, müzik ve katılım formu bulunur; misafirin yanıtı doğrudan size ulaşır. Bilgiyi siz güncellediğinizde herkesin elindeki link aynı kalır, yeni bilgi anında görünür. Arkasında çalışan bir sistem olduğu için fiyatı görsel davetiyeden yüksektir; karşılığında LCV toplama, liste tutma ve değişiklik duyurma gibi işlerden sizi kurtarır.",
     "Hangisinin size uygun olduğu davetinizin büyüklüğüne bağlıdır. Yirmi kişilik bir söz töreni için bir görsel yeterli olabilir; yüzlerce kişinin davetli olduğu bir düğünde ise katılım takibinin kazandırdığı zaman çoğu zaman fiyat farkından daha değerlidir."], None, None),
   ("Tek seferlik ödeme mi, abonelik mi?", ["Bazı hizmetler davetiyeyi tek seferlik bir ücretle verir, bazıları ise aylık ya da yıllık abonelikle çalışır. Abonelikte ilk görülen fiyat düşük görünebilir; ancak davetiyeyi düğünden birkaç ay önce hazırlayıp düğünden sonra da hatıra defterine bakmak isteyeceğiniz için toplam tutarı hesaplamak önemlidir.",
     "Abonelik seçeneğini değerlendiriyorsanız iptal koşullarını, otomatik yenileme olup olmadığını ve abonelik bittiğinde davetiyenin ve katılım listesinin ne olacağını mutlaka sorun. Tek seferlik ödemede ise ödemenin neleri kapsadığını ve linkin ne kadar süre açık kalacağını öğrenmeniz yeterlidir."], None, None),
   ("Gizli maliyetlere dikkat: sormanız gereken sorular", ["İlan edilen fiyat her zaman ödeyeceğiniz toplam tutar olmayabilir. Ek ücretler genellikle sonradan ihtiyaç duyulan özelliklerde ortaya çıkar. Sipariş vermeden önce şu soruları sormanız sürprizleri önler:"],
    None, ["Katılım formu ve panel fiyata dahil mi, yoksa ayrı bir paket mi?", "Gönderdikten sonra saat, mekân ya da program değişirse düzeltme ücretli mi?", "Misafir sayısı ya da linkin açılma sayısı sınırlı mı?", "Müzik, ek tasarım ya da ek sayfa için ayrıca ücret alınıyor mu?", "Davet türü değişirse (örneğin nişandan düğüne) yeni bir davetiye mi almak gerekiyor?", "Katılım listesini Excel gibi bir dosyaya aktarabiliyor musunuz?", "Ödemeden önce davetiyenin son hâlini görebiliyor musunuz?"]),
   ("Hazır şablon mu, kişiye özel tasarım mı?", ["Hazır şablonlu davetiyelerde tasarım önceden yapılmıştır; siz yalnızca bilgilerinizi girersiniz. Bu yüzden daha hızlı ve daha uygun fiyatlıdır. İyi hazırlanmış bir şablon çoğu düğün, nişan ve kına için fazlasıyla yeterlidir.",
     "Kişiye özel tasarımda ise renkler, süslemeler ve düzen düğününüzün konseptine göre hazırlanır; tasarımcıyla yazışma, önizleme ve düzeltme turları olur. Harcanan emek arttığı için fiyat da yükselir ve genellikle tasarımın kapsamına göre değişir. Konseptli bir düğün planlıyorsanız ya da davetiyenin salon süslemesi, masa kartları gibi diğer unsurlarla uyumlu olmasını istiyorsanız bu seçenek mantıklıdır. Teklif alırken kaç revizyon hakkınız olduğunu ve tasarımı onaylamadan önce görüp göremeyeceğinizi sorun."], None, None),
   ("LaVie'de dijital davetiye fiyatları", ["LaVie'de iki seçenek var. Standart pakette hazır tasarımlarımızdan birini seçip davetiyenizi kendiniz oluşturursunuz; ücret 500 TL'dir ve tek seferliktir, abonelik ya da yenileme ücreti yoktur. Ödemeden önce davetiyenizi kendi bilgilerinizle canlı önizlemede görürsünüz; beğenmezseniz hiçbir ödeme yapmazsınız.",
     "Bu ücrete katılım formu ve size özel panel, gelecek ve gelemeyecek kişi sayılarının canlı takibi, listeyi Excel'e aktarma, hatıra defteri, konum düğmesi, geri sayım, program akışı ve müzik dahildir. Davetiyeyi dilediğiniz kadar kişiyle paylaşabilirsiniz; misafir sınırı yoktur. Gönderdikten sonra saat, mekân, program, davet notu, tasarım ya da müziği panelinizden kendiniz değiştirirsiniz; link aynı kalır. Ödemeyi kartla (Shopier güvencesiyle) ya da IBAN ile havaleyle yapabilirsiniz.",
     "Tamamen size özel bir davetiye isterseniz Profesyonel Tasarım paketini seçebilirsiniz. Bu pakette düğününüzün konseptini, renklerini ve beğendiğiniz örnekleri WhatsApp'tan konuşur, size özel şablon koleksiyonumuzu gösterir ya da sıfırdan bir tasarım hazırlarız. Önizlemeyi gönderir, sınırsız revizyonla istediğiniz hâle getirir ve onayınızdan sonra yayına alırız. Fiyat, tasarımın kapsamına göre 2.000 TL'den başlar; kesin tutarı konuştuktan sonra size bildiririz."], None, None),
   ("Kâğıt davetiyeyle maliyeti karşılaştırırken", ["Dijital davetiyeyi kâğıt davetiyeyle karşılaştırırken yalnızca birim fiyata bakmak yanıltıcı olabilir. Kâğıt davetiyede toplam maliyet; adet, kâğıt ve baskı türü, zarf ve süslemeler gibi seçimlere göre değişir ve davetli sayısı arttıkça büyür. Buna dağıtım için harcanan zaman ve yol da eklenir. Dijital davetiyede ise ücret çoğunlukla davetli sayısından bağımsızdır.",
     "Hesaplarken şu kalemleri de göz önünde bulundurun:"],
    None, ["Baskı adedi ve son dakika eklenen misafirler için ek baskı", "Zarf, mühür, kurdele gibi ek malzemeler", "Elden dağıtım için harcanan zaman ya da kargo ücretleri", "Bilgi değişirse yeniden baskı ihtimali", "LCV'yi telefonla toplamak için harcanan zaman", "Şehir dışındaki ve yurt dışındaki misafirlere ulaştırma"]),
   ("İkisini birlikte kullanmak", ["Birçok aile iki seçeneği birlikte kullanıyor: davetli listesinin büyük bölümüne dijital davetiye gönderip, aile büyükleri ve hatıra olarak saklamak istedikleri için az sayıda kâğıt davetiye bastırıyor. Böylece baskı adedi azalırken büyüklerinize karşı geleneksel incelik de korunmuş olur. Kâğıt davetiyenin üzerine dijital davetiyenizin linkini ya da karekodunu eklerseniz, kâğıt davetiyeyi alan misafirler de konuma ve katılım formuna kolayca ulaşır."], None, None),
  ],
  sss=[("Dijital davetiye ne kadar?", "Fiyat; davetiyenin bir görsel mi yoksa katılım formlu bir davetiye sitesi mi olduğuna, hazır şablon mu kişiye özel tasarım mı olduğuna ve ödemenin tek seferlik mi abonelik mi olduğuna göre değişir. LaVie'de hazır tasarımlı davetiye sitesi 500 TL tek seferlik, kişiye özel Profesyonel Tasarım paketi ise 2.000 TL'den başlayan fiyatlarla sunulur."),
       ("Ücretsiz dijital davetiye yeterli olur mu?", "Küçük ve samimi bir davet için ücretsiz bir görsel davetiye yeterli olabilir. Ancak bu davetiyeler genellikle sonradan değiştirilemez ve katılım toplamaz. Davetli sayınız kalabalıksa ve LCV takibi, konum ya da sonradan düzenleme istiyorsanız davetiye sitesi işinizi daha çok kolaylaştırır."),
       ("Dijital davetiyede misafir sayısı fiyatı etkiler mi?", "Hizmete göre değişir; bazı hizmetler misafir ya da görüntülenme sayısına göre paket sunar. LaVie'de misafir sınırı yoktur; davetiyenizi dilediğiniz kadar kişiyle paylaşabilirsiniz ve fiyat değişmez."),
       ("Ödemeyi yapmadan önce davetiyeyi görebilir miyim?", "LaVie'de evet. Davetiyenizi kendi bilgilerinizle oluşturur, telefon önizlemesinde baştan sona görürsünüz; beğenirseniz sipariş verip ödersiniz. Profesyonel Tasarım paketinde de önizlemeyi onayınıza sunar, onaylamadan yayına almayız.")]),
 dict(slug="whatsapp-davetiye-gonderme", kisa="WhatsApp'tan davetiye gönderme", tur="Düğün",
  ilgili=[("davetli-listesi","Davetli listesi aracı"),("davetiye-sozu-olusturucu","Davetiye sözü oluşturucu")],
  title="WhatsApp'tan Davetiye Gönderme: Nezaket Kuralları ve Örnek Mesajlar | LaVie",
  desc="WhatsApp'tan davetiye nasıl gönderilir? Aile büyüklerine, arkadaşlara ve iş arkadaşlarına örnek davet mesajları, grup mu bire bir mi, hatırlatma mesajları ve kaçınılması gereken hatalar.",
  h1=("WhatsApp'tan Davetiye", "Gönderme"),
  giris="Düğün, nişan ve kına davetlerinin büyük kısmı artık WhatsApp üzerinden yapılıyor. Hızlı ve pratik olduğu kesin; ama aynı link, nasıl ve kime gönderildiğine göre ya çok içten ya da aceleye getirilmiş bir davet gibi algılanabiliyor. Bu rehberde WhatsApp'tan davetiye gönderirken dikkat edilecek nezaket kurallarını, kime nasıl bir mesaj yazacağınızı ve doğrudan kopyalayıp kullanabileceğiniz örnek mesajları bulacaksınız.",
  bolumler=[
   ("WhatsApp'tan davetiye göndermek ayıp mı?", ["Hayır; özenle hazırlanmış bir davetiye, kişisel bir mesajla gönderildiğinde bugün gayet saygılı bir davet olarak karşılanıyor. Misafirleriniz davetiyeyi telefonlarında saklıyor, konuma tek dokunuşla ulaşıyor ve tarihi kolayca hatırlıyor. Özellikle şehir dışında ya da yurt dışında yaşayan yakınlarınız için en hızlı ve en güvenilir yol bu.",
     "Önemli olan davetin özensiz görünmemesi. Linki tek başına ve açıklamasız göndermek, toplu bir duyuru gibi algılanabilir. Kişinin adıyla başlayan, sizin ağzınızdan çıkmış birkaç cümle ise aynı daveti içten hâle getirir. Aile büyükleri söz konusu olduğunda geleneksel inceliği korumak için mesajdan önce ya da sonra kısa bir telefon açmak hâlâ çok makbuldür."], None, None),
   ("Göndermeden önce hazırlık", ["Mesajları göndermeye başlamadan önce birkaç küçük hazırlık, hem sizi hem misafirlerinizi yanlış anlaşılmalardan korur:"],
    None, ["Davetli listenizi netleştirin; kime bireysel mesaj, kime telefon, kime kâğıt davetiye gideceğini işaretleyin", "Eksik ya da eski telefon numaralarını aileden önceden toplayın", "Linki önce kendinize gönderin (WhatsApp'ta kendi numaranıza mesaj atabilirsiniz) ve telefonda açılıp açılmadığını, tarih, saat ve konumun doğru olduğunu kontrol edin", "Davetiyenin kime hitap ettiğini netleştirin: tek kişi mi, aile mi, çocuklar dahil mi?", "Katılım için son yanıt tarihini belirleyin ve mesajda belirtin", "Örnek mesajlarınızı bir not dosyasında hazır tutun; her kişiye adını ekleyip kopyalayın"]),
   ("Bire bir mi, grup mu, toplu mesaj listesi mi?", ["En kişisel yol, davetiyeyi herkese ayrı ayrı göndermektir. Zaman alır ama her misafir kendisinin özel olarak davet edildiğini hisseder. Aile büyükleri, yakın akrabalar ve en yakın arkadaşlar için bunu öneririz.",
     "WhatsApp gruplarına göndermek hızlıdır ancak dikkat ister: grupta davet edilmeyen kişiler varsa kırgınlık yaratabilir, mesaj da kısa sürede diğer yazışmaların arasında kaybolur. Grubun tamamı davetliyse, örneğin bir arkadaş grubu ya da iş yerindeki ekibiniz, grup mesajı uygundur.",
     "WhatsApp'ın toplu mesaj (yayın) listesi özelliği ise ikisinin arasında bir yoldur: mesaj herkese ayrı ayrı, bire bir sohbet olarak ulaşır ve alıcılar birbirini görmez. Yalnız bu özellikte mesaj sadece sizin numaranızı rehberine kaydetmiş kişilere iletilir; numaranızı kaydetmemiş birine davetiye gitmeyebilir. Bu yüzden önemli misafirleri listeye güvenmek yerine ayrıca kontrol edin."],
    None, ["Aile büyükleri ve yakın akraba: bire bir mesaj, mümkünse önce telefon", "Yakın arkadaşlar: bire bir mesaj", "Tamamı davetli arkadaş ya da iş grubu: grup mesajı", "Kalabalık ama dağınık liste: toplu mesaj listesi, ardından kontrol"]),
   ("Aile büyüklerine örnek davet mesajları", ["Büyüklerinize yazarken saygılı bir hitap, kısa ve açık cümleler kullanın. Mesajın sonuna davetiye linkini eklemeniz yeterli:"],
    ["Sevgili teyzeciğim, hayatımızın en güzel gününde sizi de aramızda görmek bizi çok mutlu edecek. Düğün davetiyemizi aşağıdaki linkte bulabilirsiniz; tarih, saat ve konum bilgileri içinde. Hürmetlerimizle.",
     "Kıymetli amcacığım, ailelerimizin rızası ve duasıyla evleniyoruz. Bu mutlu günümüzde sizin de bulunmanız bizim için çok değerli. Davetiyemiz bu linkte, ellerinizden öperiz.",
     "Sevgili büyüklerimiz, düğünümüze sizi ailecek davet etmekten onur duyarız. Davetiyede konum ve program bilgisi var; gelip gelemeyeceğinizi davetiyedeki formdan bildirebilir ya da bize bir telefon açabilirsiniz.",
     "Canım anneannem, düğün davetiyemizi sana da göndermek istedik. Linke dokununca açılıyor; açamazsan hemen ara, birlikte bakalım."], None),
   ("Akraba ve arkadaşlara örnek davet mesajları", ["Yakın çevrenize daha samimi bir dil kullanabilirsiniz. Kısa, sıcak ve davetin ne olduğunu hemen anlatan mesajlar en iyi sonucu verir:"],
    ["Merhaba canım, büyük gün geldi! Düğünümüzde seni de yanımızda görmek istiyoruz. Davetiyemiz bu linkte; katılımını içindeki formdan bildirirsen çok seviniriz.",
     "Sevgili kuzenim, evleniyoruz! Bu mutluluğu seninle paylaşmadan olmazdı. Tüm detaylar davetiyede, şimdiden takvimine not et.",
     "Yıllardır her güzel anımızda yanımızdaydın, bu günde de olmanı istiyoruz. Düğün davetiyemiz aşağıda, yanıtını bekliyoruz.",
     "Hazırlıklar bitmek üzere ve en önemli eksiğimiz sensin. Davetiyemizi gönderiyoruz; gelirsen bizi çok mutlu edersin.",
     "Merhaba! Düğün tarihimiz kesinleşti, davetiyemiz bu linkte. Konum ve saat bilgisi içinde; kaç kişi geleceğinizi formdan bildirmeyi unutmayın."], None),
   ("İş arkadaşları ve daha resmi davetler için örnekler", ["İş çevrenize, öğretmenlerinize ya da ailenizin tanıdıklarına yazarken resmi ama sıcak bir dil uygundur:"],
    ["Merhaba, sizi düğünümüze davet etmekten mutluluk duyarız. Tarih, saat ve konum bilgilerini aşağıdaki davetiyede bulabilirsiniz. Katılımınızı davetiyedeki formdan bildirirseniz seviniriz.",
     "Değerli hocam, evliliğimizin ilk adımında sizi de aramızda görmek bize onur verir. Davetiyemizi bilgilerinize sunarız.",
     "Sevgili ekip arkadaşlarım, düğünümüze hepinizi davet ediyorum. Davetiye linkini paylaşıyorum; gelebilecekler formdan bildirirse organizasyonu planlamamız kolaylaşır."], None),
   ("Nişan, söz ve kına için örnek mesajlar", ["Daha küçük ve aile içi davetlerde mesaj da kısa ve samimi olabilir:"],
    ["Ailelerimizin huzurunda nişanlanıyoruz! Bu güzel günde sizi de aramızda görmek isteriz. Nişan davetiyemiz bu linkte.",
     "Söz törenimiz için sizi evimize bekliyoruz. Adres ve saat bilgisi davetiyede; gelip gelemeyeceğinizi bildirirseniz seviniriz.",
     "Kınamızda kızlar bir araya geliyoruz! Kına davetiyemizi gönderiyorum; kıyafet notunu da içinde bulabilirsin.",
     "Kına gecemizde sizin de bulunmanızı çok isteriz. Konum ve program davetiyede, şimdiden hoş geldiniz."], None),
   ("Hatırlatma ve katılım (LCV) mesajları", ["Davetiyeyi gönderdikten sonra yanıt vermeyenlere nazik bir hatırlatma yapmak tamamen normaldir; çoğu zaman misafir mesajı görmüş ama yanıtlamayı unutmuştur. Hatırlatmayı düğünden yaklaşık iki üç hafta önce, yalnızca yanıt vermeyen kişilere bire bir gönderin. Düğünden bir gün önce de konum bilgisini içeren kısa bir mesaj atabilirsiniz:"],
    ["Merhaba, düğün davetiyemizi görebildin mi? Salona kesin sayıyı bildirmemiz gerekiyor; gelip gelemeyeceğini davetiyedeki formdan ya da buradan yazarsan çok seviniriz.",
     "Küçük bir hatırlatma: katılım bilgisi için son günümüz yaklaşıyor. Davetiye linki aşağıda, yanıtını bekliyoruz.",
     "Yarın görüşüyoruz! Salonun konumu davetiyede, yol tarifi için konum düğmesine dokunman yeterli. Şimdiden hoş geldin.",
     "Davetimize katılacağını bildirdiğin için çok teşekkür ederiz, seni görmek için sabırsızlanıyoruz!"], None),
   ("Kaçınılması gereken hatalar", ["WhatsApp'tan davet ederken en sık yapılan hatalar küçük görünür ama misafirin daveti nasıl algıladığını doğrudan etkiler:"],
    None, ["Linki hiçbir açıklama yazmadan, tek başına göndermek", "Aile büyüklerine yalnızca grup mesajıyla davet göndermek", "Davetsiz kişilerin de bulunduğu bir gruba davetiye atmak", "Gece geç saatlerde ya da çok erken saatlerde mesaj göndermek", "Linki göndermeden önce kendi telefonunuzda denememek", "Aynı kişiye farklı gruplardan defalarca aynı daveti göndermek", "Bilgi değiştiğinde yeni bir görsel hazırlayıp herkesin kafasını karıştırmak; davetiye sitesinde bilgiyi güncellemek yeterlidir", "Yanıt vermeyenlere ısrarcı ya da sitemli bir dille hatırlatma yapmak"]),
  ],
  sss=[("WhatsApp'tan davetiye göndermek kaba kaçar mı?", "Kişisel bir mesajla ve özenle hazırlanmış bir davetiyeyle gönderildiğinde kaba kaçmaz; bugün en yaygın davet yollarından biridir. Aile büyükleri için mesajın yanında kısa bir telefon açmak ya da birkaç kâğıt davetiye vermek inceliği tamamlar."),
       ("Davetiye WhatsApp gruplarına mı, kişilere tek tek mi gönderilmeli?", "Mümkünse tek tek göndermek en kişisel yoldur. Grubun tamamı davetliyse grup mesajı uygundur; davet edilmeyen kişilerin de bulunduğu gruplara davetiye göndermemeye dikkat edin. Toplu mesaj listesi kullanırsanız mesajın yalnızca numaranızı kaydetmiş kişilere ulaştığını unutmayın."),
       ("Davetiye mesajına ne yazılır?", "Kişinin adıyla başlayan bir hitap, davetin ne olduğu (düğün, nişan, kına), onu aranızda görmek istediğinizi anlatan bir cümle ve davetiye linki yeterlidir. Katılım bekliyorsanız yanıt vermesini rica eden kısa bir not ekleyin."),
       ("Davetiyeyi gönderdikten sonra bilgi değişirse herkese yeniden mesaj mı atmalıyım?", "Görsel bir davetiye gönderdiyseniz yeni görseli herkese yeniden göndermeniz gerekir. Davetiye sitesi kullanıyorsanız bilgiyi panelden güncellemeniz yeterlidir; link aynı kalır. Önemli bir değişiklikse misafirlere kısa bir bilgilendirme mesajı atmak yine de iyi olur.")]),
 dict(slug="nikah-davetiyesi-sozleri", kisa="Nikah davetiyesi sözleri", tur="Düğün",
  ilgili=[("davetiye-sozu-olusturucu","Davetiye sözü oluşturucu"),("tarihi-kaydet-mesaji","Tarihi kaydedin mesajı"),("nikah-sekeri-notu-olusturucu","Nikah şekeri notu oluşturucu")],
  cta=("Seçtiğiniz sözle nikah davetiyenizi hazırlayın", "Sözü kopyalayın, LaVie'de “Davet notu” alanına yapıştırın; nikah salonunun konumu, saat ve katılım formuyla birlikte zarfı açılan, müzikli dijital davetiyenizde anında görün. 500 TL, tek seferlik."),
  title="Nikah Davetiyesi Sözleri: Resmi, Modern ve Romantik 25 Örnek | LaVie",
  desc="Nikah davetiyesi sözleri: klasik, modern, romantik ve aile ağzından örnekler; nikah + kokteyl ve nikah + yemek metinleri, davetiyede olması gereken bilgiler ve sık yapılan hatalar.",
  h1=("Nikah Davetiyesi", "Sözleri"),
  giris="Nikah, evliliğin resmî olarak başladığı andır; pek çok çift için de düğünden bile daha duygusal bir an. Kimi çiftler yalnızca nikah töreni yapıp ardından küçük bir kokteyl ya da yemek veriyor, kimileri nikahı düğünle aynı gün kıyıyor, kimileri de nikahı ayrı bir günde, yakın çevresiyle sade biçimde gerçekleştiriyor. Hangisini seçerseniz seçin, davetiyenizdeki söz misafirlerinize bu günün havasını ilk anlatan cümle olacak. Bu rehberde klasik, modern, romantik ve aile ağzından yazılmış, doğrudan kopyalayıp kullanabileceğiniz nikah davetiyesi sözlerini ve davetiyeye yazılması gereken bilgileri bulacaksınız.",
  bolumler=[
   ("Nikah davetiyesi ile düğün davetiyesi arasındaki fark", ["Düğün davetiyesi genellikle uzun bir kutlamaya, yemeğe ve eğlenceye çağırır. Nikah davetiyesi ise daha kısa ve daha resmî bir anın, yani nikahın kıyılıp imzaların atılacağı törenin davetidir. Bu yüzden nikah davetiyelerinde dil çoğu zaman daha sade, daha ağırbaşlı ve daha net olur.",
     "Bir diğer fark da zamanlamadır. Nikah salonlarında törenler randevu saatine göre art arda yapıldığı için saat bilgisinin doğruluğu çok önemlidir; misafirlerin törenin başlangıcını kaçırmaması gerekir. Nikahın ardından bir kokteyl, yemek ya da düğün varsa bunu da davetiyede açıkça belirtmek, misafirin gününü planlamasını kolaylaştırır."], None, None),
   ("Nikah davetiyesine neler yazılır?", ["Söz ne kadar güzel olursa olsun, davetiyenin asıl görevi misafire doğru bilgiyi vermektir. Göndermeden önce şu bilgilerin eksiksiz olduğundan emin olun:"],
    None, ["Gelin ve damadın adları", "Davet eden aileler; geleneksel davetiyelerde iki tarafın aile adları yazılır", "Nikahın tarihi, günü ve saati", "Nikah salonunun ya da mekânın adı ve açık adresi", "Nikahın ardından kokteyl, yemek ya da düğün varsa bunun yeri ve saati", "Katılım (LCV) için son yanıt tarihi ve iletişim bilgisi", "Gerekliyse kıyafet, otopark ya da çocuk katılımıyla ilgili kısa bir not"]),
   ("Klasik ve resmi nikah davetiyesi sözleri", ["Aile büyüklerine, iş çevresine ve kalabalık bir davetli listesine hitap eden davetiyelerde ölçülü ve saygılı bir dil en güvenli tercihtir:"],
    ["Hayatlarımızı birleştireceğimiz nikah törenimizde sizleri de aramızda görmekten mutluluk duyarız.",
     "Ailelerimizin rızası ve dualarıyla nikahımızı kıyıyoruz. Bu anlamlı günde bizleri onurlandırmanızı rica ederiz.",
     "Evliliğimize ilk adımı atacağımız nikah törenimize teşrifinizi bekleriz.",
     "Yeni bir hayata “evet” diyeceğimiz bu güzel günde varlığınız bizim için en değerli hediye olacaktır.",
     "Nikah törenimizde sizleri de aramızda görmek, mutluluğumuzu tamamlayacaktır. Katılımınızı rica ederiz.",
     "Birlikte çıktığımız bu yolun ilk imzasını atarken sevdiklerimizin yanımızda olmasını diliyoruz. Nikahımıza davetlisiniz."], None),
   ("Modern ve kısa nikah davetiyesi sözleri", ["Arkadaş çevresine gönderilecek ya da sade bir tasarımla kullanılacak davetiyelerde kısa ve samimi cümleler daha iyi durur:"],
    ["Evet demeye hazırız! Nikahımızda sizi de görmek istiyoruz.",
     "Bir imza, bir ömür. Nikahımıza bekleriz.",
     "Resmî olarak “biz” oluyoruz. Bu anda yanımızda olur musunuz?",
     "Kısa bir tören, büyük bir mutluluk. Nikahımıza davetlisiniz.",
     "Yüzükler hazır, kalemler hazır; eksik olan bir tek sizsiniz.",
     "Aşkımızı resmîleştiriyoruz! Nikahımızda sizi aramızda görmekten mutluluk duyarız."], None),
   ("Romantik ve duygusal nikah davetiyesi sözleri", ["Hikâyenizi anlatan, biraz daha şiirsel bir dil istiyorsanız bu örneklerden ilham alabilirsiniz:"],
    ["Bir tesadüfle başlayan hikâyemize bu kez bilerek ve isteyerek imza atıyoruz. Bu anı bizimle paylaşmanızı isteriz.",
     "Aynı yöne bakmayı öğrendik; şimdi aynı yolda yürümeye karar verdik. Nikahımızda yanımızda olun.",
     "Kalplerimiz çoktan söz verdi, şimdi sıra imzalarımızda. Nikah törenimize davetlisiniz.",
     "Birbirimize “iyi ki” dediğimiz her günün en güzelini sizinle paylaşmak istiyoruz.",
     "Ömür boyu sürecek bir yolculuğun ilk sayfasını açıyoruz. O sayfada sizin de adınız olsun."], None),
   ("Aile ağzından nikah davetiyesi sözleri", ["Davetiyeyi ailelerin göndermesi, özellikle geleneksel davetlerde ve aile büyüklerinin tanıdıklarına gidecek davetiyelerde hâlâ çok yaygındır:"],
    ["Kızımız ile oğlumuzun nikah törenlerinde sizleri de aramızda görmekten şeref duyarız.",
     "Evlatlarımızın mutluluğunu sevdiklerimizle paylaşmak istiyoruz. Nikah törenlerine teşriflerinizi rica ederiz.",
     "Çocuklarımızın hayatlarını birleştirdiği bu mutlu günde sizleri de aramızda görmek bizleri onurlandıracaktır.",
     "Allah'ın izniyle evlatlarımızın nikahını kıyıyoruz. Bu hayırlı günde dualarınızla yanımızda olmanızı dileriz."], None),
   ("Nikah + kokteyl, nikah + yemek ve nikah + düğün için sözler", ["Nikahın ardından bir kutlama varsa, sözün içinde bunu da anmak misafirin programını netleştirir. Saat ve mekân bilgisini sözün altına ayrıca yazmayı unutmayın:"],
    ["Nikah törenimizin ardından vereceğimiz kokteylde sizleri de aramızda görmekten mutluluk duyarız.",
     "Nikahımızı kıydıktan sonra sevdiklerimizle küçük bir yemekte buluşmak istiyoruz. Bu güzel günde bize eşlik etmenizi dileriz.",
     "Nikah törenimizi ve ardından gelecek düğün kutlamamızı sizinle paylaşmak istiyoruz. Hepinizi bekliyoruz.",
     "Önce imzalar, sonra kutlama! Nikahımıza ve ardından gelecek kokteylimize davetlisiniz."], None),
   ("Doğru sözü seçerken ve davetiyeyi hazırlarken dikkat edilecekler", ["Nikah davetiyesi kısa bir metin olduğu için küçük ayrıntılar fark yaratır. Göndermeden önce şu noktaları gözden geçirin:"],
    None, ["Sözün tonunu davetin havasıyla eşleştirin; resmî bir salon nikahı için fazla esprili bir dil, aile büyükleri arasında yadırganabilir", "Birden fazla davetli grubunuz varsa (aile büyükleri, arkadaşlar) farklı tonda iki davetiye metni hazırlamayı düşünün", "Saati yazarken misafirlerin birkaç dakika erken gelmesi gerektiğini nazikçe belirtin; nikah salonlarında törenler genellikle zamanında başlar", "Nikah ve kutlama farklı mekânlardaysa iki adresi de ayrı ayrı ve açıkça yazın", "Sözü, isimleri ve tarihi yüksek sesle okuyarak kontrol edin; yazım hatası en çok bu kısa metinlerde göze batar", "Şiir ya da şarkı sözü kullanacaksanız, başkasının eserini kendi sözünüz gibi göstermeyin; kendi cümlelerinizle yazmak hem daha samimi hem daha güvenlidir"]),
  ],
  sss=[("Nikah davetiyesi ne zaman gönderilir?", "Misafirlerin gününü planlayabilmesi için davetiyeyi nikahtan birkaç hafta önce göndermek iyi olur; şehir dışından gelecek misafirler için daha erken haber vermek gerekir. Tarih erken kesinleştiyse önce kısa bir “tarihi kaydedin” mesajı gönderip davetiyeyi sonra iletebilirsiniz."),
       ("Nikah ve düğün aynı gündeyse iki ayrı davetiye mi hazırlanmalı?", "Gerekmez. Tek bir davetiyede önce nikahın, ardından düğünün saatini ve yerini ayrı satırlarda yazmanız yeterlidir. Yalnızca bazı misafirleri nikaha, herkesi düğüne çağırıyorsanız iki farklı davetiye metni hazırlamak karışıklığı önler."),
       ("Nikah şahitlerinin adı davetiyeye yazılır mı?", "Genellikle yazılmaz; davetiyede gelin ve damadın adları ile davet eden aileler yer alır. Şahitlerinize davetiyenin yanında kişisel bir mesaj ya da telefonla özellikle teşekkür etmek daha anlamlı olur."),
       ("Sadece nikah yapacağız, düğün olmayacak; davetiyede bunu belirtmeli miyiz?", "Belirtmeniz misafirler için faydalıdır. “Nikah törenimizin ardından küçük bir kokteyl vereceğiz” ya da “Nikahımızı sade bir törenle kıyıyoruz” gibi bir cümle, misafirin ne bekleyeceğini bilmesini sağlar ve yanlış beklentileri önler.")]),
]

YAZI_CSS = """
.makale{max-width:760px}
.makale h2{font-size:clamp(1.7rem,4vw,2.2rem);margin:46px 0 10px}
.makale p{color:#3d3a44;font-size:1.04rem;line-height:1.75;margin:0 0 14px}
.makale ul.liste{padding-left:20px;margin:6px 0 18px;color:#3d3a44;line-height:1.8}
.icindekiler{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px 20px;margin:26px 0 8px}
.icindekiler b{display:block;font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);margin-bottom:8px;font-weight:500}
.icindekiler ol{margin:0;padding-left:20px;line-height:1.9}.icindekiler a{text-decoration:none;color:var(--accent)}
.cta-kutu{background:var(--soft);border:1px solid #dcd0e2;border-radius:20px;padding:24px;margin:40px 0;display:grid;gap:10px}
.cta-kutu b{font-family:var(--display);font-weight:400;font-size:1.7rem;line-height:1.1}
.cta-kutu p{margin:0}.cta-kutu .btn{justify-self:start}
.meta{font-size:.84rem;color:var(--muted);margin-top:-6px}
.makale .metinler{gap:10px}.makale .metin{padding:14px 16px;gap:8px 14px}.makale .metin p{font-size:1.1rem;margin:0}
@media(max-width:560px){.makale .metin button{padding:6px 12px}}
"""

def yazi(y):
    url = f"{U}/{y['slug']}"
    turq = y["tur"]
    olustur = f"/?tur={turq}#olustur"
    tur_sayfa = next((s for s in SAYFALAR if s["tur"] == turq), SAYFALAR[0])
    art = {"@context":"https://schema.org","@type":"Article","headline":y["title"].split(" | ")[0],"description":y["desc"],"datePublished":TARIH,"dateModified":y.get("guncel",(TARIH,))[0],
           "author":{"@type":"Organization","name":"LaVie Davetiye","url":U+"/"},"publisher":{"@type":"Organization","name":"LaVie Davetiye","logo":{"@type":"ImageObject","url":U+"/logo.svg"}},
           "mainEntityOfPage":url,"image":og_gorsel(y["slug"]),"inLanguage":"tr-TR"}
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Ana sayfa","item":U+"/"},{"@type":"ListItem","position":2,"name":"Rehber","item":U+"/rehber"},{"@type":"ListItem","position":3,"name":y["kisa"],"item":url}]}
    faq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in y["sss"]]}
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(x,ensure_ascii=False)}</script>' for x in (art,bc,faq))
    ic = "".join(f'<li><a href="#b{i}">{e(b[0])}</a></li>' for i,b in enumerate(y["bolumler"]))
    govde = ""
    for i,(baslik, paragraflar, ornekler, liste) in enumerate(y["bolumler"]):
        govde += f'<h2 id="b{i}">{e(baslik)}</h2>' + "".join(f"<p>{e(p)}</p>" for p in paragraflar)
        if ornekler: govde += '<div class="metinler">' + "".join(f'<div class="metin"><p>“{e(m)}”</p><button type="button" data-m="{e(m)}">Kopyala</button></div>' for m in ornekler) + "</div>"
        if liste: govde += '<ul class="liste">' + "".join(f"<li>{e(x)}</li>" for x in liste) + "</ul>"
        if i == 1:
            cb, cp = y.get("cta") or ("Bu sözü davetiyenizde görün", f"Zarfı açılan, müzikli ve katılım formlu dijital {turq.lower()} davetiyenizi oluşturun; yazdığınız söz anında önizlemede belirir. 500 TL, tek seferlik.")
            govde += f'<div class="cta-kutu"><b>{e(cb)}</b><p>{e(cp)}</p><a class="btn pri" href="{olustur}">Davetiyemi oluştur</a></div>'
    sss = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q,a in y["sss"])
    diger = "".join(f'<a href="/{x["slug"]}">{e(x["kisa"])}</a>' for x in YAZILAR if x is not y)
    ilgili = ""
    if y.get("ilgili"):
        ilgili = '<h2 style="font-size:1.5rem">İlgili ücretsiz araçlar</h2><div class="diger">' + "".join(f'<a href="/{x}">{e(a)}</a>' for x,a in y["ilgili"]) + "</div>"
    ilk, son = y["h1"]
    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon-48.png" sizes="48x48" type="image/png"><link rel="apple-touch-icon" href="/favicon-180.png">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(y['title'])}</title>
<meta name="description" content="{e(y['desc'])}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#f6f3f1">
<meta property="og:type" content="article"><meta property="og:locale" content="tr_TR"><meta property="og:site_name" content="LaVie Davetiye">
<meta property="og:title" content="{e(y['title'].split(' | ')[0])}"><meta property="og:description" content="{e(y['desc'])}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{og_gorsel(y['slug'])}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Italiana&family=Pinyon+Script&family=Cormorant+Garamond:ital,wght@0,400;1,400&family=Jost:wght@400;500&display=swap">
{ld}
<style>{CSS}{YAZI_CSS}</style>
</head>
<body>
<a class="ust-serit" href="https://instagram.com/la.viecreative" target="_blank" rel="noopener"><div class="in">{IG}<span>Instagram'da biz: <b>@la.viecreative</b></span></div></a>
<header class="nav"><div class="in"><a href="/" aria-label="LaVie Davetiye ana sayfa"><img src="/logo.svg" alt="La Vie Creative Studio" width="630" height="165"></a><a class="btn pri" href="{olustur}">Davetiyemi oluştur</a></div></header>
<main class="in makale" style="padding-bottom:60px">
<div class="yol"><a href="/">Ana sayfa</a> › <a href="/rehber">Rehber</a> › {e(y['kisa'])}</div>
<div class="eyebrow" style="margin-top:26px">LaVie Rehber</div>
<h1>{e(ilk)} <em>{e(son)}</em></h1>
<p class="meta">Güncelleme: {y.get("guncel",(TARIH,"12 Ekim 2026"))[1]} · LaVie Davetiye</p>
<p class="lead" style="font-size:1.1rem">{e(y['giris'])}</p>
<nav class="icindekiler" aria-label="İçindekiler"><b>İçindekiler</b><ol>{ic}</ol></nav>
{govde}
<h2>Sıkça sorulanlar</h2>
<div class="sss">{sss}</div>
<div class="cta-kutu"><b>Dijital {e(turq.lower())} davetiyesi</b><p>Tasarımları, canlı örneği ve özellikleri görmek için tanıtım sayfamıza göz atın.</p><a class="btn sec" href="/{tur_sayfa['slug']}">{e(tur_sayfa['baslik'])}</a></div>
{ilgili}<h2 style="font-size:1.5rem">Diğer rehber yazıları</h2>
<div class="diger">{diger}<a href="/rehber">Tüm rehber</a></div>
</main>
<footer><div class="in"><a href="/" aria-label="LaVie Davetiye"><img src="/logo-acik.svg" alt="La Vie Creative Studio" width="630" height="165"></a><span>© <span id="yil">2026</span> LaVie Davetiye · <a href="https://instagram.com/la.viecreative" target="_blank" rel="noopener">@la.viecreative</a></span></div></footer>
<a class="destek" id="destek" target="_blank" rel="noopener" aria-label="WhatsApp destek hattı">{WA}</a>
<script src="/ayarlar.js"></script>
<script>
document.getElementById("yil").textContent = new Date().getFullYear();
document.getElementById("destek").href = "https://wa.me/" + window.LAVIE_AYAR.WHATSAPP + "?text=" + encodeURIComponent("Merhaba LaVie, dijital davetiye hakkında bilgi almak istiyorum.");
document.querySelectorAll("[data-m]").forEach(b => b.onclick = async () => {{
  try {{ await navigator.clipboard.writeText(b.dataset.m); b.textContent = "Kopyalandı"; }} catch (_) {{ b.textContent = "Kopyalanamadı"; }}
  setTimeout(() => b.textContent = "Kopyala", 1800);
}});
</script>
</body>
</html>
"""

def rehber_ana():
    kartlar = "".join(f'<a class="kart" href="/{y["slug"]}" style="text-decoration:none;display:block"><h3>{e(y["kisa"])}</h3><p>{e(y["desc"])}</p></a>' for y in YAZILAR)
    turler = "".join(f'<a href="/{s["slug"]}">{e(s["baslik"])}</a>' for s in SAYFALAR)
    url = U + "/rehber"
    return f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon-48.png" sizes="48x48" type="image/png"><link rel="apple-touch-icon" href="/favicon-180.png"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Davetiye Rehberi: Sözler, LCV ve Gönderim Zamanı | LaVie</title>
<meta name="description" content="Düğün, nişan ve kına davetiyesi sözleri, LCV'nin anlamı ve davetiyenin ne zaman gönderileceği üzerine pratik rehber yazıları.">
<link rel="canonical" href="{url}"><meta name="theme-color" content="#f6f3f1">
<meta property="og:type" content="website"><meta property="og:title" content="LaVie Davetiye Rehberi"><meta property="og:url" content="{url}"><meta property="og:image" content="{og_gorsel('rehber')}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Italiana&family=Pinyon+Script&family=Cormorant+Garamond:ital,wght@0,400;1,400&family=Jost:wght@400;500&display=swap">
{hub_ld("rehber", "Davetiye rehberi", "Düğün, nişan ve kına davetiyesi sözleri, LCV'nin anlamı ve davetiyenin ne zaman gönderileceği üzerine pratik rehber yazıları.", [(y["slug"], y["kisa"]) for y in YAZILAR])}
<style>{CSS}{YENI_CSS}</style></head><body>
<a class="ust-serit" href="https://instagram.com/la.viecreative" target="_blank" rel="noopener"><div class="in">{IG}<span>Instagram'da biz: <b>@la.viecreative</b></span></div></a>
<header class="nav"><div class="in"><a href="/" aria-label="LaVie Davetiye ana sayfa"><img src="/logo.svg" alt="La Vie Creative Studio" width="630" height="165"></a><a class="btn pri" href="/#olustur">Davetiyemi oluştur</a></div></header>
<main class="in" style="padding-bottom:60px"><div class="yol"><a href="/">Ana sayfa</a> › Rehber</div>
<div class="eyebrow" style="margin-top:26px">LaVie Rehber</div><h1>Davetiye <em>rehberi</em></h1>
<p class="lead">Davetiye sözlerinden LCV'ye, gönderim zamanından dijital davetiyenin inceliklerine kadar ihtiyacınız olan her şey.</p>
{yeni_eklenenler()}
<div class="kartlar">{kartlar}</div>
<h2 style="font-size:1.6rem;margin-top:48px">Davetiye türleri</h2><div class="diger">{turler}</div></main>
<footer><div class="in"><a href="/" aria-label="LaVie Davetiye"><img src="/logo-acik.svg" alt="La Vie Creative Studio" width="630" height="165"></a><span>© 2026 LaVie Davetiye</span></div></footer>
<script src="/ayarlar.js"></script></body></html>
"""

if __name__ == "__main__":
    for y in YAZILAR:
        open(os.path.join(KOK, y["slug"] + ".html"), "w", encoding="utf8").write(yazi(y))
    open(os.path.join(KOK, "rehber.html"), "w", encoding="utf8").write(rehber_ana())
    import araclar; araclar.yaz_hepsi()  # site haritası araçlarla birlikte yazılır
    print("ok", len(YAZILAR), "yazı")
