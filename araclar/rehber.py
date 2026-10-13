# Rehber yazılarını üretir: python3 araclar/rehber.py  (public/ içine yazar, site haritasını günceller)
import json, html, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from tur_sayfalari import U, KOK, CSS, IG, WA, SAYFALAR, site_haritasi

e = html.escape
TARIH = "2026-10-12"

# Her yazı: bölümler (başlık, paragraflar, örnek sözler, madde listesi)
YAZILAR = [
 dict(slug="dugun-davetiyesi-sozleri", kisa="Düğün davetiyesi sözleri", tur="Düğün",
  title="Düğün Davetiyesi Sözleri: 40 Kısa, Anlamlı ve Modern Örnek | LaVie",
  desc="En güzel düğün davetiyesi sözleri: kısa, klasik, modern, aile ağzından ve esprili 40 örnek. Kopyalayıp davetiyenize ekleyin, dijital davetiyenizde kullanın.",
  h1=("Düğün Davetiyesi", "Sözleri"),
  giris="Davetiyedeki birkaç cümle, misafirinizin düğününüzle ilgili ilk izlenimidir. Aşağıda farklı tarzlarda 40 düğün davetiyesi sözü bulacaksınız. Beğendiğinizi kopyalayabilir, isimleri ve ayrıntıları kendinize göre değiştirebilirsiniz.",
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
       ("Dijital davetiyede de bu sözleri kullanabilir miyim?", "Evet. LaVie'de sözü 'Davet notu' alanına yapıştırmanız yeterli; yazdığınız anda telefondaki önizlemede görünür ve sonradan panelinizden değiştirebilirsiniz.")]),

 dict(slug="kina-davetiyesi-sozleri", kisa="Kına davetiyesi sözleri", tur="Kına",
  title="Kına Davetiyesi Sözleri: 23 Duygusal, Kısa ve Eğlenceli Örnek | LaVie",
  desc="Kına gecesi davetiyesi için 23 söz örneği: duygusal, geleneksel, kısa ve eğlenceli. Kopyalayın, dijital kına davetiyenizde kullanın.",
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
   ("Kına davetiyesine eklenebilecek notlar", ["Kına gecelerinde sık kullanılan notlar. LaVie'de katılım formunun üstüne ekleyebilirsiniz:"],
    None, ["Bindallı ya da kına kıyafetinizle gelebilirsiniz.", "Çocuklarımıza iyi uykular dileriz.", "Lütfen katılım durumunuzu bir hafta önce bildiriniz.", "Gece kadınlara özeldir."]),
  ],
  sss=[("Kına davetiyesi ne zaman gönderilir?", "Genellikle kına gecesinden 2-4 hafta önce gönderilir. Düğün davetiyesiyle birlikte de gönderilebilir."),
       ("Kına ve düğün için ayrı davetiye gerekir mi?", "Farklı gün ya da mekânda yapılıyorsa ayrı davetiye misafirlerin karıştırmasını önler. Aynı tasarımı seçerek iki davetiyeyi birbirine uyumlu yapabilirsiniz."),
       ("Kına davetiyesinde neler yazmalı?", "Gelinin ve ailenin adı, tarih, saat, adres ve kısa bir davet sözü yeterlidir. Kıyafet önerisi gibi notlar da eklenebilir.")]),

 dict(slug="nisan-davetiyesi-sozleri", kisa="Nişan davetiyesi sözleri", tur="Nişan",
  title="Nişan Davetiyesi Sözleri: 25 Zarif ve Kısa Örnek | LaVie",
  desc="Nişan davetiyesi için 25 söz örneği: resmi, romantik, kısa ve aile ağzından. Kopyalayıp dijital nişan davetiyenizde kullanın.",
  h1=("Nişan Davetiyesi", "Sözleri"),
  giris="Nişan, iki ailenin bir araya geldiği ve çiftin birbirine resmen söz verdiği ilk büyük adımdır. Davetiyedeki sözün de bu ciddiyeti ve sevinci birlikte taşıması güzel olur. İşte farklı tarzlarda 25 örnek.",
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
  ],
  sss=[("Nişan davetiyesi ne zaman gönderilir?", "Genellikle nişandan 2-4 hafta önce gönderilir. Kısa sürede planlanan nişanlarda dijital davetiye aynı gün ulaştığı için büyük kolaylık sağlar."),
       ("Nişan davetiyesinde aile isimleri yazılmalı mı?", "Zorunlu değildir ama nişan iki ailenin buluşması olduğu için aile isimlerini yazmak yaygın ve şık bir tercihtir."),
       ("Nişan ve düğün davetiyesi aynı tasarımda olabilir mi?", "Evet. Aynı tasarımı iki davetiyede de kullanmak bütünlük sağlar; LaVie'de davet türünü değiştirdiğinizde başlık kendiliğinden güncellenir.")]),

 dict(slug="lcv-nedir", kisa="LCV nedir?", tur="Düğün",
  title="LCV Nedir? Davetiyede LCV Ne Demek, Nasıl Toplanır? | LaVie",
  desc="LCV, 'Lütfen Cevap Veriniz' demektir. Davetiyede LCV'nin anlamı, ne zaman istenir, misafirlerden katılım bilgisi nasıl toplanır ve örnek LCV cümleleri.",
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
  ],
  sss=[("LCV açılımı nedir?", "LCV, 'Lütfen Cevap Veriniz' ifadesinin kısaltmasıdır. Uluslararası karşılığı RSVP'dir."),
       ("LCV'ye cevap vermek zorunlu mu?", "Zorunlu değildir ama nezaket gereği beklenir. Davet sahibinin hazırlık yapabilmesi için gelip gelmeyeceğinizi bildirmeniz önemlidir."),
       ("Dijital davetiyede LCV nasıl toplanır?", "Davetiyenin içindeki katılım formuyla. Misafir formu doldurur, yanıt davet sahibinin paneline anında düşer; telefonla tek tek aramaya gerek kalmaz.")]),

 dict(slug="davetiye-ne-zaman-gonderilir", kisa="Davetiye ne zaman gönderilir?", tur="Düğün",
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
    art = {"@context":"https://schema.org","@type":"Article","headline":y["title"].split(" | ")[0],"description":y["desc"],"datePublished":TARIH,"dateModified":TARIH,
           "author":{"@type":"Organization","name":"LaVie Davetiye","url":U+"/"},"publisher":{"@type":"Organization","name":"LaVie Davetiye","logo":{"@type":"ImageObject","url":U+"/logo.svg"}},
           "mainEntityOfPage":url,"image":U+"/og/lavie.jpg","inLanguage":"tr-TR"}
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Ana sayfa","item":U+"/"},{"@type":"ListItem","position":2,"name":"Rehber","item":U+"/rehber"},{"@type":"ListItem","position":3,"name":y["kisa"],"item":url}]}
    faq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in y["sss"]]}
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(x,ensure_ascii=False)}</script>' for x in (art,bc,faq))
    ic = "".join(f'<li><a href="#b{i}">{e(b[0])}</a></li>' for i,b in enumerate(y["bolumler"]))
    govde = ""
    for i,(baslik, paragraflar, ornekler, liste) in enumerate(y["bolumler"]):
        govde += f'<h2 id="b{i}">{e(baslik)}</h2>' + "".join(f"<p>{e(p)}</p>" for p in paragraflar)
        if ornekler: govde += '<div class="metinler">' + "".join(f'<div class="metin"><p>“{e(m)}”</p><button type="button" data-m="{e(m)}">Kopyala</button></div>' for m in ornekler) + "</div>"
        if liste: govde += '<ul class="liste">' + "".join(f"<li>{e(x)}</li>" for x in liste) + "</ul>"
        if i == 1: govde += f'<div class="cta-kutu"><b>Bu sözü davetiyenizde görün</b><p>Zarfı açılan, müzikli ve katılım formlu dijital {e(turq.lower())} davetiyenizi oluşturun; yazdığınız söz anında önizlemede belirir. 500 TL, tek seferlik.</p><a class="btn pri" href="{olustur}">Davetiyemi oluştur</a></div>'
    sss = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q,a in y["sss"])
    diger = "".join(f'<a href="/{x["slug"]}">{e(x["kisa"])}</a>' for x in YAZILAR if x is not y)
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
<meta property="og:image" content="{U}/og/lavie.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">
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
<p class="meta">Güncelleme: 12 Ekim 2026 · LaVie Davetiye</p>
<p class="lead" style="font-size:1.1rem">{e(y['giris'])}</p>
<nav class="icindekiler" aria-label="İçindekiler"><b>İçindekiler</b><ol>{ic}</ol></nav>
{govde}
<h2>Sıkça sorulanlar</h2>
<div class="sss">{sss}</div>
<div class="cta-kutu"><b>Dijital {e(turq.lower())} davetiyesi</b><p>Tasarımları, canlı örneği ve özellikleri görmek için tanıtım sayfamıza göz atın.</p><a class="btn sec" href="/{tur_sayfa['slug']}">{e(tur_sayfa['baslik'])}</a></div>
<h2 style="font-size:1.5rem">Diğer rehber yazıları</h2>
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
<meta property="og:type" content="website"><meta property="og:title" content="LaVie Davetiye Rehberi"><meta property="og:url" content="{url}"><meta property="og:image" content="{U}/og/lavie.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Italiana&family=Pinyon+Script&family=Cormorant+Garamond:ital,wght@0,400;1,400&family=Jost:wght@400;500&display=swap">
<style>{CSS}</style></head><body>
<a class="ust-serit" href="https://instagram.com/la.viecreative" target="_blank" rel="noopener"><div class="in">{IG}<span>Instagram'da biz: <b>@la.viecreative</b></span></div></a>
<header class="nav"><div class="in"><a href="/" aria-label="LaVie Davetiye ana sayfa"><img src="/logo.svg" alt="La Vie Creative Studio" width="630" height="165"></a><a class="btn pri" href="/#olustur">Davetiyemi oluştur</a></div></header>
<main class="in" style="padding-bottom:60px"><div class="yol"><a href="/">Ana sayfa</a> › Rehber</div>
<div class="eyebrow" style="margin-top:26px">LaVie Rehber</div><h1>Davetiye <em>rehberi</em></h1>
<p class="lead">Davetiye sözlerinden LCV'ye, gönderim zamanından dijital davetiyenin inceliklerine kadar ihtiyacınız olan her şey.</p>
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
