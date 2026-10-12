# Davet türü sayfalarını üretir: python3 araclar/tur_sayfalari.py  (public/ içine yazar)
import json, html, os
U = "https://www.laviedavetiye.workers.dev"
KOK = os.path.join(os.path.dirname(__file__), "..", "public")
TASARIM_AD = {"zeytin": "Zeytin Dalı", "gece": "Gece Mavisi", "gul": "Gül Kurusu", "mono": "Siyah Beyaz", "ege": "Ege"}

SAYFALAR = [
 dict(slug="dijital-dugun-davetiyesi", tur="Düğün", kisa="düğün", baslik="Dijital Düğün Davetiyesi",
  title="Dijital Düğün Davetiyesi · Online Düğün Davetiyesi Sitesi | LaVie",
  desc="Zarfı açılan, müzikli ve geri sayımlı dijital düğün davetiyesi. Katılım (LCV) takibi, konum ve program dahil, WhatsApp'tan tek linkle gönderin. 500 TL, tek seferlik ödeme.",
  tasarim="zeytin", oneri=["zeytin","gece","mono"],
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
       ("Düğün davetiyesi ne zaman gönderilmeli?","Genellikle düğünden 4-6 hafta önce gönderilir. Dijital davetiye anında ulaştığı için daha geç de gönderebilirsiniz; ancak katılım sayısını erken öğrenmek için erken göndermek işinizi kolaylaştırır.")]),
 dict(slug="dijital-nisan-davetiyesi", tur="Nişan", kisa="nişan", baslik="Dijital Nişan Davetiyesi",
  title="Dijital Nişan Davetiyesi · Online Nişan Davetiyesi | LaVie",
  desc="Şık ve müzikli dijital nişan davetiyesi. Zarf açılışı, geri sayım, konum ve katılım takibi dahil; WhatsApp'tan tek linkle paylaşın. 500 TL, tek seferlik ödeme.",
  tasarim="gul", oneri=["gul","zeytin","ege"],
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
       ("Misafirler davetiyeyi nasıl açar?","Gönderdiğiniz linke dokunmaları yeterli. Davetiye telefonun tarayıcısında açılır, uygulama indirmek gerekmez.")]),
 dict(slug="dijital-kina-davetiyesi", tur="Kına", kisa="kına", baslik="Dijital Kına Davetiyesi",
  title="Dijital Kına Davetiyesi · Online Kına Gecesi Davetiyesi | LaVie",
  desc="Müzikli ve zarfı açılan dijital kına gecesi davetiyesi. Konum, program ve katılım takibi dahil; WhatsApp'tan tek linkle gönderin. 500 TL, tek seferlik ödeme.",
  tasarim="gul", oneri=["gul","gece","zeytin"],
  lead="Kına geceniz için zarfı açılan, müzikli bir davetiye. Misafirleriniz programı, adresi ve yol tarifini tek linkte bulur; siz de kimlerin geleceğini panelinizden anında görürsünüz.",
  neden=[("Kalabalık aileye tek linkle ulaşın","Kına gecesi davetlileri genellikle geniş aile ve komşulardan oluşur. Tek bir linki aile gruplarına göndermeniz yeterli."),
         ("Program akışı hazır","Karşılama, kına yakılması, eğlence saatleri; misafirleriniz akşamın planını önceden bilir."),
         ("Kıyafet ve hatırlatma notları","Bindallı, kıyafet önerisi ya da \"çocuklarımıza iyi uykular\" gibi notları katılım formunun üstüne ekleyebilirsiniz."),
         ("Düğünle aynı tasarım","Kına ve düğün davetiyelerinizi aynı tasarımla hazırlayıp iki geceyi birbirine bağlayabilirsiniz.")],
  metinler=["Kınamız yakılırken sevdiklerimizi yanımızda görmek istiyoruz. Kına gecemizde sizleri de aramızda görmekten mutluluk duyarız.",
            "Ellerimize kına, gönlümüze sevinç yakacağımız bu gecede bize eşlik etmenizi dileriz.",
            "Gelinimizin baba evinden uğurlanışına tanıklık etmeniz dileğiyle, kına gecemize davetlisiniz.",
            "Türküler, kahkahalar ve kınayla dolu bir gece için sizleri de bekliyoruz.",
            "Mutluluğumuzu kınayla taçlandıracağımız bu özel gecede varlığınız bizi çok mutlu edecek."],
  sss=[("Kına gecesi davetiyesi ayrıca mı hazırlanmalı?","Kına ve düğün farklı gün ya da yerdeyse ayrı davetiye hazırlamak misafirlerin karıştırmasını önler. Aynı tasarımı seçerek iki davetiyeyi birbirine uyumlu yapabilirsiniz."),
       ("Kına davetiyesine hangi notlar eklenebilir?","Kıyafet önerisi, çocuklarla ilgili rica ya da katılım bildirme tarihi gibi notları katılım formunun üstündeki alana yazabilirsiniz. Hazır cümlelerden birini de seçebilirsiniz."),
       ("Kına gecesi davetiyesi ne zaman gönderilir?","Kına gecesinden 2-4 hafta önce göndermek yaygındır. Düğün davetiyesiyle birlikte de gönderebilirsiniz."),
       ("Davetiyede müzik çalar mı?","Evet. Zarf açıldığında seçtiğiniz müzik çalmaya başlar; misafirleriniz isterse sağ alttaki düğmeyle kapatabilir.")]),
 dict(slug="dijital-soz-davetiyesi", tur="Söz", kisa="söz", baslik="Dijital Söz Davetiyesi",
  title="Dijital Söz Davetiyesi · Online Söz Töreni Davetiyesi | LaVie",
  desc="Zarif ve müzikli dijital söz töreni davetiyesi. Konum, geri sayım ve katılım takibi dahil; WhatsApp'tan tek linkle gönderin. 500 TL, tek seferlik ödeme.",
  tasarim="ege", oneri=["ege","zeytin","gul"],
  lead="Söz töreniniz için sade ve zarif bir dijital davetiye. Aile büyüklerinize ve yakınlarınıza tek linkle ulaşır, kimlerin geleceğini panelinizden takip edersiniz.",
  neden=[("Samimi davetlere uygun","Söz genellikle yakın aile arasında yapılır. Kısa bir davet notu ve sade bir tasarımla içten bir davetiye hazırlarsınız."),
         ("Hızlı ve zahmetsiz","Söz kısa sürede planlanabilir; davetiyeniz aynı gün hazır olur, baskı beklemezsiniz."),
         ("Evin adresi tek dokunuşta","Tören evde yapılıyorsa konum linki sayesinde misafirleriniz kapıyı kolayca bulur."),
         ("Sonraki davetlere hazırlık","Aynı tasarımı nişan ve düğün davetiyelerinizde de kullanabilirsiniz.")],
  metinler=["Ailelerimizin rızası ve hayır dualarıyla söz kesiyoruz. Bu güzel günümüzde sizleri de aramızda görmek isteriz.",
            "Birbirimize verdiğimiz sözü sevdiklerimizin huzurunda taçlandırmak istiyoruz. Söz törenimize davetlisiniz.",
            "Hayırlı bir başlangıcın ilk adımında dualarınızla yanımızda olmanızı dileriz.",
            "Mutluluğumuzu paylaşacağımız bu küçük ama anlamlı günde varlığınız bizi onurlandıracak.",
            "İki ailenin bir araya geldiği bu güzel günde sizleri de bekliyoruz."],
  sss=[("Söz töreni için davetiye gerekli mi?","Söz genellikle yakın çevreyle yapıldığı için davetiye şart değildir. Ancak dijital davetiye tarih, saat ve adresi herkese aynı anda ve eksiksiz iletmenin en kolay yoludur."),
       ("Söz davetiyesinde neler yazılır?","Çiftin ve ailelerin isimleri, tarih, saat, adres ve kısa bir davet notu yeterlidir."),
       ("Söz, nişan ve düğün için aynı tasarımı kullanabilir miyim?","Evet. Beş tasarımdan birini seçip tüm davetlerinizde kullanabilirsiniz; her davet türü için başlık otomatik değişir."),
       ("Davetiyeyi sonradan değiştirebilir miyim?","Evet. Size özel panelden saat, adres ve davet notu dahil tüm bilgileri dilediğiniz zaman güncelleyebilirsiniz.")]),
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
.tas{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin-top:30px}@media(max-width:700px){.tas{grid-template-columns:1fr}}
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
  <p class="lead">Beş tasarımın hepsi her davet türüne uyar; başlık davet türünüze göre kendiliğinden değişir.</p>
  <div class="tas">{tas}</div>
</div></section>

<section class="blk" style="padding-top:0"><div class="in">
  <div class="fiyat">
    <div><h2>Tüm özellikler tek pakette</h2><p>Davetiye siteniz, katılım takibi ve size özel paneliniz. Abonelik yok, ödemeyi davetiyenizi beğendikten sonra yaparsınız.</p></div>
    <div><div class="tl">500<small>TL</small></div><a class="btn pri" href="{olustur}">Hemen oluştur</a></div>
  </div>
</div></section>

<section class="blk" style="padding-top:0"><div class="in">
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
