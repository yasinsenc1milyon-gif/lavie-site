# Ücretsiz araç sayfaları: python3 araclar/araclar.py  (public/ içine yazar, site haritasını günceller)
import json, html, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from tur_sayfalari import U, KOK, CSS, IG, WA, site_haritasi
from rehber import YAZILAR

e = html.escape

ARAC_CSS = """
.arac{background:#fff;border:1px solid var(--line);border-radius:22px;padding:20px;margin-top:26px;box-shadow:0 24px 50px -36px rgba(33,31,39,.4)}
@media(max-width:560px){.arac{padding:16px;border-radius:18px}}
.alan{display:grid;gap:5px;min-width:0}
.alan span{font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-weight:500}
.arac input,.arac select{font:inherit;font-size:16px;width:100%;padding:11px 12px;border:1px solid var(--line);border-radius:10px;background:var(--paper);color:var(--ink)}
.arac input:focus,.arac select:focus{outline:none;border-color:var(--accent);background:#fff}
.izgara{display:grid;gap:10px}
.iki{display:grid;grid-template-columns:1fr 1fr;gap:10px}
@media(max-width:560px){.iki.tek{grid-template-columns:1fr}}
.ozet.para b{font-size:1.4rem;line-height:1.15}
.uc{display:grid;grid-template-columns:2fr 1fr 1fr;gap:10px}
@media(max-width:560px){.uc{grid-template-columns:1fr 1fr}.uc .genis{grid-column:1/-1}}
.seg{display:flex;flex-wrap:wrap;gap:6px}
.seg button{font:inherit;font-size:.86rem;padding:7px 13px;border-radius:999px;border:1px solid var(--line);background:#fff;color:var(--ink);cursor:pointer}
.seg button[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:#fff}
.ozet{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;margin-top:16px}
@media(max-width:560px){.ozet{grid-template-columns:repeat(2,minmax(0,1fr))}}
.ozet div{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:12px}
.ozet b{display:block;font-family:var(--display);font-weight:400;font-size:1.9rem;line-height:1;font-variant-numeric:tabular-nums}
.ozet span{font-size:.74rem;color:var(--muted)}
.ara{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-top:16px}
.ara input{flex:1 1 180px}
.satirlar{margin-top:12px;border:1px solid var(--line);border-radius:14px;overflow:hidden}
.satir{display:grid;grid-template-columns:1fr auto auto;gap:10px;align-items:center;padding:10px 12px;border-top:1px solid var(--line);background:#fff}
.satir:first-child{border-top:0}
.satir b{font-weight:500;display:block}.satir small{color:var(--muted);font-size:.8rem}
.adet{display:flex;align-items:center;gap:4px}
.adet button,.sil{width:30px;height:30px;border-radius:50%;border:1px solid var(--line);background:#fff;cursor:pointer;font:inherit;line-height:1;color:var(--ink)}
.adet b{min-width:22px;text-align:center;font-variant-numeric:tabular-nums}
.sil{color:#a14d4d}
.bos{padding:26px 14px;text-align:center;color:var(--muted);background:#fff}
.dugmeler{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}
.dugmeler .btn{padding:11px 18px;font-size:.88rem}
.btn.kucuk{padding:10px 16px;font-size:.88rem}
.not{font-size:.8rem;color:var(--muted);margin-top:10px}
.cta-kutu{background:var(--soft);border:1px solid #dcd0e2;border-radius:20px;padding:24px;margin:34px 0;display:grid;gap:10px}
.cta-kutu b{font-family:var(--display);font-weight:400;font-size:1.7rem;line-height:1.1}.cta-kutu p{margin:0}.cta-kutu .btn{justify-self:start}
.makale{max-width:760px}.makale h2{font-size:clamp(1.6rem,4vw,2.1rem);margin:44px 0 10px}.makale p,.makale li{color:#3d3a44;line-height:1.75}
.kalem{display:grid;grid-template-columns:1fr 130px;gap:10px;align-items:center;padding:10px 0;border-top:1px solid var(--line)}
.kalem:first-child{border-top:0}
.kalem .ad b{font-weight:500}.kalem .ad small{display:block;color:var(--muted);font-size:.78rem}
.kalem input{text-align:right;font-variant-numeric:tabular-nums}
.cubuk{height:6px;border-radius:999px;background:#eee6ea;margin-top:6px;overflow:hidden}.cubuk i{display:block;height:100%;background:var(--accent)}
.durum{margin-top:14px;padding:12px 14px;border-radius:12px;font-size:.92rem}
.durum.iyi{background:#e5f4ea;color:#2f5f40}.durum.asim{background:#f6e6e6;color:#8a3a3a}
.kars{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}
.kars div{border:1px solid var(--line);border-radius:14px;padding:14px;background:var(--paper)}
.kars div.vurgu{background:var(--soft);border-color:#dcd0e2}
.kars b{display:block;font-family:var(--display);font-weight:400;font-size:1.8rem;line-height:1.1}
.kars span{font-size:.8rem;color:var(--muted)}
.tasarruf{margin-top:10px;font-size:.95rem}
.durum.orta{background:#f7efdf;color:#7a5a22}
.lejant{display:flex;flex-wrap:wrap;gap:6px 14px;margin-top:16px;font-size:.8rem;color:var(--muted)}
.lejant span{display:flex;align-items:center;gap:6px}.lejant i.g{width:14px;height:14px;border-radius:4px;display:inline-block}
.aylar{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px 16px;margin-top:16px}
@media(max-width:700px){.aylar{grid-template-columns:repeat(2,minmax(0,1fr));gap:16px 10px}}
.ay b{font-family:var(--display);font-weight:400;font-size:1.25rem;display:block;margin-bottom:6px}
.hg{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:2px}
.hg i{font-style:normal;font-size:.62rem;color:var(--muted);text-align:center}
.hg button{font:inherit;font-size:.74rem;aspect-ratio:1;border:0;border-radius:5px;cursor:pointer;padding:0;font-variant-numeric:tabular-nums;color:var(--ink)}
.g.uygun{background:#e6f2e9}.g.uzun{background:#8fc29f;color:#16301f}.g.yogun{background:#f2dfb5}.g.ikiBayram{background:#efe2cf}
.g.ramazan{background:#e3d6ea}.g.bayram{background:#c98f8f;color:#fff}.g.tatil{background:#b9cde3}.g.kandil{background:#e3d6ea}
.hg button.sol{background:transparent;color:#c5bdc2}
.hg button.sec{outline:2px solid var(--ink);outline-offset:1px;font-weight:500}
"""

def kabuk(slug, title, desc, h1, giris, govde, script, ld_ekstra=(), cta_tur="Düğün"):
    url = f"{U}/{slug}"
    app = {"@context":"https://schema.org","@type":"WebApplication","name":h1[0]+" "+h1[1],"url":url,"applicationCategory":"LifestyleApplication","operatingSystem":"Web",
           "offers":{"@type":"Offer","price":"0","priceCurrency":"TRY"},"inLanguage":"tr-TR","publisher":{"@type":"Organization","name":"LaVie Davetiye","url":U+"/"}}
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Ana sayfa","item":U+"/"},{"@type":"ListItem","position":2,"name":"Ücretsiz araçlar","item":U+"/araclar"},{"@type":"ListItem","position":3,"name":h1[0]+" "+h1[1],"item":url}]}
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(x,ensure_ascii=False)}</script>' for x in (app,bc,*ld_ekstra))
    digerleri = "".join(f'<a href="/{a["slug"]}">{e(a["ad"])}</a>' for a in ARACLAR if a["slug"] != slug)
    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon-48.png" sizes="48x48" type="image/png"><link rel="apple-touch-icon" href="/favicon-180.png">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#f6f3f1">
<meta property="og:type" content="website"><meta property="og:locale" content="tr_TR"><meta property="og:site_name" content="LaVie Davetiye">
<meta property="og:title" content="{e(title.split(' | ')[0])}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{U}/og/lavie.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Italiana&family=Pinyon+Script&family=Cormorant+Garamond:ital,wght@0,400;1,400&family=Jost:wght@400;500&display=swap">
{ld}
<style>{CSS}{ARAC_CSS}</style>
</head>
<body>
<a class="ust-serit" href="https://instagram.com/la.viecreative" target="_blank" rel="noopener"><div class="in">{IG}<span>Instagram'da biz: <b>@la.viecreative</b></span></div></a>
<header class="nav"><div class="in"><a href="/" aria-label="LaVie Davetiye ana sayfa"><img src="/logo.svg" alt="La Vie Creative Studio" width="630" height="165"></a><a class="btn pri" href="/?tur={cta_tur}#olustur">Davetiyemi oluştur</a></div></header>
<main class="in" style="padding-bottom:60px;max-width:860px">
<div class="yol"><a href="/">Ana sayfa</a> › <a href="/araclar">Ücretsiz araçlar</a> › {e(h1[0]+' '+h1[1])}</div>
<div class="eyebrow" style="margin-top:26px">Ücretsiz araç</div>
<h1>{e(h1[0])} <em>{e(h1[1])}</em></h1>
<p class="lead">{e(giris)}</p>
{govde}
<h2 style="font-size:1.5rem;margin-top:48px">Diğer ücretsiz araçlar</h2>
<div class="diger">{digerleri}<a href="/rehber">Davetiye rehberi</a></div>
</main>
<footer><div class="in"><a href="/" aria-label="LaVie Davetiye"><img src="/logo-acik.svg" alt="La Vie Creative Studio" width="630" height="165"></a><span>© <span id="yil">2026</span> LaVie Davetiye · <a href="https://instagram.com/la.viecreative" target="_blank" rel="noopener">@la.viecreative</a></span></div></footer>
<a class="destek" id="destek" target="_blank" rel="noopener" aria-label="WhatsApp destek hattı">{WA}</a>
<script src="/ayarlar.js"></script>
<script>
document.getElementById("yil").textContent = new Date().getFullYear();
document.getElementById("destek").href = "https://wa.me/" + window.LAVIE_AYAR.WHATSAPP + "?text=" + encodeURIComponent("Merhaba LaVie, dijital davetiye hakkında bilgi almak istiyorum.");
const $ = id => document.getElementById(id);
const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}}[c]));
const oku = (k, v) => {{ try {{ const x = localStorage.getItem(k); return x ? JSON.parse(x) : v; }} catch {{ return v; }} }};
const yaz = (k, v) => {{ try {{ localStorage.setItem(k, JSON.stringify(v)); }} catch {{}} }};
const tl = n => (Math.round(n) || 0).toLocaleString("tr-TR") + " TL";
{script}
</script>
</body>
</html>
"""

def sss_html(sss):
    return '<div class="sss">' + "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q,a in sss) + "</div>"
def sss_ld(sss):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in sss]}

# ---------------- Davetli listesi ----------------
DL_SSS = [("Davetli listesi nasıl hazırlanır?", "Önce iki tarafın aile, akraba, arkadaş ve iş çevrelerini ayrı ayrı yazın. Her kayda kaç kişi geleceğini (eşler, çocuklar) ekleyin. Toplam sayıyı salon kapasitenizle karşılaştırın, gerekirse grupları daraltın. Son hâlini Excel'e aktarıp aileyle paylaşın."),
          ("Listem nereye kaydediliyor?", "Listeniz yalnızca kendi telefonunuzda ya da bilgisayarınızda, bu tarayıcıda saklanır. Bize hiçbir bilgi gönderilmez. Başka bir cihazda kullanmak için listeyi Excel'e aktarabilirsiniz."),
          ("Listeyi Excel'de nasıl açarım?", "'Excel'e aktar' düğmesine basınca bir CSV dosyası iner. Excel, Numbers ya da Google E-Tablolar bu dosyayı doğrudan açar; Türkçe karakterler korunur."),
          ("Kaç kişilik davetiye basmalıyım?", "Kâğıt davetiye kişi başı değil hane başı gönderilir; genellikle davetli sayısının yarısı ile üçte biri arası adet yeterlidir. Dijital davetiyede adet sınırı yoktur, tek link herkese gönderilir.")]
DL_GOVDE = """
<div class="arac">
  <form id="ekleForm" class="izgara" autocomplete="off">
    <div class="uc">
      <label class="alan genis"><span>Ad soyad</span><input id="ad" placeholder="Örn. Ayşe ve Mehmet Kaya" required></label>
      <label class="alan"><span>Kişi</span><input id="kisi" type="number" min="1" max="30" value="2" inputmode="numeric"></label>
      <label class="alan"><span>Grup</span><select id="grup"><option>Aile</option><option>Akraba</option><option>Arkadaş</option><option>İş</option><option>Komşu</option><option>Diğer</option></select></label>
    </div>
    <div class="iki tek">
      <div class="alan"><span>Taraf</span><div class="seg" id="tarafSec"></div></div>
      <label class="alan"><span>Telefon (isteğe bağlı)</span><input id="tel" type="tel" inputmode="tel" placeholder="05XX XXX XX XX"></label>
    </div>
    <button class="btn pri kucuk" type="submit" style="justify-self:start">+ Listeye ekle</button>
  </form>
  <div class="ozet" id="ozet"></div>
  <div class="ara"><input id="ara" type="search" placeholder="Listede ara"><div class="seg" id="filtre"></div></div>
  <div class="satirlar" id="liste"></div>
  <div class="dugmeler">
    <button class="btn sec" type="button" id="excel">Excel'e aktar</button>
    <button class="btn sec" type="button" id="yazdir">Yazdır</button>
    <button class="btn sec" type="button" id="temizle" style="color:#a14d4d">Listeyi temizle</button>
  </div>
  <p class="not">Listeniz yalnızca bu cihazda saklanır, bize gönderilmez.</p>
</div>
<div class="cta-kutu"><b>Listeniz hazır, şimdi davet zamanı</b><p>Bu listedeki herkese tek bir linkle zarfı açılan, müzikli davetiyenizi gönderin; kimin geldiğini ve kaç kişi olduğunu panelinizden canlı takip edin. 500 TL, tek seferlik.</p><a class="btn pri" href="/?tur=Düğün#olustur">Davetiyemi oluştur</a></div>
<section class="makale">
<h2>Davetli listesi hazırlarken 5 ipucu</h2>
<ol>
<li><b>Önce sınırı belirleyin.</b> Salonun kapasitesi ve bütçeniz toplam kişi sayısını belirler; listeye bu rakamı bilerek başlayın.</li>
<li><b>Tarafları ayrı yazın.</b> Gelin ve damat tarafının sayılarını görmek, ailelerle konuşurken işinizi kolaylaştırır.</li>
<li><b>Kişi sayısını hane hane girin.</b> "Kaya ailesi, 4 kişi" gibi kayıtlar hem davetiye adedini hem masa düzenini netleştirir.</li>
<li><b>Gruplar masa planının temelidir.</b> Aile, arkadaş, iş gibi gruplar sonradan masaları yerleştirirken size zaman kazandırır.</li>
<li><b>Telefonları baştan toplayın.</b> Dijital davetiyeyi WhatsApp'tan göndereceğiniz için numaraları listeye eklemek son haftayı rahatlatır.</li>
</ol>
<h2>Sıkça sorulanlar</h2>
""" + sss_html(DL_SSS) + "</section>"
DL_JS = r"""
const TARAFLAR = [["gelin","Gelin tarafı"],["damat","Damat tarafı"],["ortak","Ortak"]];
let L = oku("lavie_davetli", []), TARAF = "gelin", FILTRE = "hepsi";
const kaydet = () => yaz("lavie_davetli", L);
function seg(el, ogeler, secili, fn){ el.innerHTML = ogeler.map(([k,v]) => `<button type="button" data-k="${k}" aria-pressed="${k===secili}">${v}</button>`).join(""); el.querySelectorAll("button").forEach(b => b.onclick = () => fn(b.dataset.k)); }
function ciz(){
  seg($("tarafSec"), TARAFLAR, TARAF, k => { TARAF = k; ciz(); });
  seg($("filtre"), [["hepsi","Hepsi"], ...TARAFLAR.map(([k,v]) => [k, v.replace(" tarafı","")])], FILTRE, k => { FILTRE = k; ciz(); });
  const top = t => L.filter(x => !t || x.taraf === t).reduce((a,x) => a + (+x.kisi||0), 0);
  const gruplar = {}; L.forEach(x => gruplar[x.grup] = (gruplar[x.grup]||0) + (+x.kisi||0));
  $("ozet").innerHTML = `<div><b>${top()}</b><span>Toplam kişi</span></div><div><b>${L.length}</b><span>Davetiye (hane)</span></div><div><b>${top("gelin")}</b><span>Gelin tarafı</span></div><div><b>${top("damat")}</b><span>Damat tarafı</span></div>`
    + (Object.keys(gruplar).length ? `<div style="grid-column:1/-1;background:#fff"><span>${Object.entries(gruplar).map(([g,n]) => `${esc(g)}: <b style="display:inline;font-family:inherit;font-size:.95rem">${n}</b>`).join(" · ")}</span></div>` : "");
  const q = $("ara").value.trim().toLocaleLowerCase("tr");
  const g = L.filter(x => (FILTRE === "hepsi" || x.taraf === FILTRE) && (!q || (x.ad + " " + x.grup + " " + (x.tel||"")).toLocaleLowerCase("tr").includes(q)));
  $("liste").innerHTML = g.length ? g.map(x => `<div class="satir" data-id="${x.id}"><div><b>${esc(x.ad)}</b><small>${esc((TARAFLAR.find(t=>t[0]===x.taraf)||[,""])[1])} · ${esc(x.grup)}${x.tel ? " · " + esc(x.tel) : ""}</small></div>
      <div class="adet"><button type="button" data-a="-" aria-label="Azalt">−</button><b>${x.kisi}</b><button type="button" data-a="+" aria-label="Artır">+</button></div>
      <button type="button" class="sil" data-a="sil" aria-label="Sil">×</button></div>`).join("")
    : `<div class="bos">${L.length ? "Aramanıza uyan kayıt yok." : "Henüz kimseyi eklemediniz. Yukarıdan ilk davetlinizi ekleyin."}</div>`;
}
$("ekleForm").addEventListener("submit", ev => {
  ev.preventDefault();
  const ad = $("ad").value.trim(); if (!ad) return;
  L.unshift({ id: Date.now().toString(36) + Math.random().toString(36).slice(2,6), ad, kisi: Math.max(1, Math.min(30, +$("kisi").value || 1)), grup: $("grup").value, taraf: TARAF, tel: $("tel").value.trim() });
  kaydet(); $("ad").value = ""; $("tel").value = ""; $("kisi").value = 2; $("ad").focus(); ciz();
});
$("liste").addEventListener("click", ev => {
  const b = ev.target.closest("button[data-a]"); if (!b) return;
  const id = b.closest(".satir").dataset.id, x = L.find(y => y.id === id); if (!x) return;
  if (b.dataset.a === "sil") { if (!confirm(x.ad + " listeden silinsin mi?")) return; L = L.filter(y => y.id !== id); }
  else x.kisi = Math.max(1, Math.min(30, x.kisi + (b.dataset.a === "+" ? 1 : -1)));
  kaydet(); ciz();
});
$("ara").addEventListener("input", ciz);
$("excel").onclick = () => {
  if (!L.length) return alert("Liste boş.");
  const h = s => `"${String(s ?? "").replace(/"/g,'""')}"`;
  const satir = [["Ad soyad","Kişi","Taraf","Grup","Telefon"], ...L.map(x => [x.ad, x.kisi, (TARAFLAR.find(t=>t[0]===x.taraf)||[,""])[1], x.grup, x.tel])];
  const csv = "﻿" + satir.map(r => r.map(h).join(";")).join("\r\n");
  const a = document.createElement("a"); a.href = URL.createObjectURL(new Blob([csv], { type: "text/csv;charset=utf-8" })); a.download = "davetli-listesi.csv"; a.click(); setTimeout(() => URL.revokeObjectURL(a.href), 2000);
};
$("yazdir").onclick = () => window.print();
$("temizle").onclick = () => { if (L.length && confirm("Tüm liste silinsin mi? Bu geri alınamaz.")) { L = []; kaydet(); ciz(); } };
ciz();
"""

# ---------------- Düğün bütçesi ----------------
BT_SSS = [("Düğün bütçesi nasıl hesaplanır?", "Önce harcayabileceğiniz toplam tutarı ve davetli sayısını belirleyin. Ardından salon ve yemek, kıyafet, fotoğraf, takı gibi kalemlere pay ayırın. En büyük kalem genellikle salon ve yemektir ve davetli sayısıyla doğrudan artar; bu yüzden kişi başı maliyeti takip etmek önemlidir."),
          ("Bu araçtaki oranlar neye göre?", "Kalemlere başlangıç için örnek oranlar dağıtılır; bunlar bir öneridir, ortalama ya da istatistik değildir. Aldığınız teklifleri girdikçe her kalemi kendi rakamınızla değiştirin."),
          ("Dijital davetiye ne kadar tasarruf sağlar?", "Kâğıt davetiyede maliyet adet sayısıyla artar; baskı, zarf ve dağıtım da eklenir. Dijital davetiye ise davetli sayısından bağımsız tek fiyattır. Aracın davetiye bölümünde kendi adet ve fiyatınızla farkı görebilirsiniz."),
          ("Bilgilerim kaydediliyor mu?", "Girdiğiniz rakamlar yalnızca bu cihazdaki tarayıcıda saklanır, bize gönderilmez.")]
KALEMLER = [("salon","Salon ve yemek","Mekân, menü, ikram",45),("kiyafet","Gelinlik ve damatlık","Kıyafet, ayakkabı, aksesuar",10),("takı","Takı ve alyans","Alyans, takı seti",12),
            ("foto","Fotoğraf ve video","Çekim, albüm, klip",8),("muzik","Müzik ve organizasyon","DJ / orkestra, organizasyon",6),("susleme","Çiçek ve süsleme","Gelin buketi, masa süsü",5),
            ("kuafor","Kuaför ve makyaj","Gelin saçı, makyaj, prova",4),("davetiye","Davetiye ve hediyelik","Davetiye, nikâh şekeri",3),("diger","Diğer","Ulaşım, sürprizler, yedek",7)]
BT_GOVDE = """
<div class="arac">
  <div class="iki">
    <label class="alan"><span>Toplam bütçe (TL)</span><input id="butce" type="number" min="0" step="1000" inputmode="numeric" placeholder="Örn. 400000"></label>
    <label class="alan"><span>Davetli sayısı (kişi)</span><input id="kisi" type="number" min="0" step="10" inputmode="numeric" placeholder="Örn. 300"></label>
  </div>
  <div class="ozet para" id="ozet"></div>
  <div style="margin-top:18px;display:flex;justify-content:space-between;align-items:baseline;gap:10px;flex-wrap:wrap"><b style="font-weight:500">Kalemler</b><button class="btn sec kucuk" type="button" id="dagit">Örnek oranlarla yeniden dağıt</button></div>
  <p class="not" style="margin-top:4px">Başlangıç tutarları örnek oranlarla dağıtılır; aldığınız teklifleri girdikçe kendi rakamlarınızla değiştirin.</p>
  <div id="kalemler"></div>
  <div id="durum"></div>
</div>
<div class="arac">
  <b style="font-weight:500;font-size:1.05rem">Davetiye: kâğıt mı dijital mi?</b>
  <p class="not" style="margin-top:4px">Kâğıt davetiye hane başına gönderilir. Kendi adet ve fiyatınızı girin.</p>
  <div class="iki" style="margin-top:10px">
    <label class="alan"><span>Davetiye adedi</span><input id="adet" type="number" min="0" inputmode="numeric"></label>
    <label class="alan"><span>Kâğıt davetiye adet fiyatı (TL)</span><input id="adetFiyat" type="number" min="0" step="1" inputmode="decimal" placeholder="Zarf ve baskı dahil"></label>
  </div>
  <div class="kars"><div><span>Kâğıt davetiye</span><b id="kagit">–</b><span>+ dağıtım zahmeti</span></div><div class="vurgu"><span>LaVie dijital davetiye</span><b>500 TL</b><span>adet sınırı yok, LCV takibi dahil</span></div></div>
  <div class="tasarruf" id="tasarruf"></div>
</div>
<div class="cta-kutu"><b>Davetiyede tasarruf edin</b><p>Zarfı açılan, müzikli, katılım formlu dijital davetiyenizi tek linkle herkese gönderin. Davetli sayısı ne olursa olsun 500 TL.</p><a class="btn pri" href="/?tur=Düğün#olustur">Davetiyemi oluştur</a></div>
<section class="makale">
<h2>Düğün bütçesi planlarken</h2>
<ol>
<li><b>Davetli sayısı bütçenin anahtarıdır.</b> Salon ve yemek kişi başı fiyatlandığı için her ek 10 kişi toplamı belirgin şekilde artırır.</li>
<li><b>Yedek ayırın.</b> Son dakika harcamaları için bütçenin bir kısmını "Diğer" kalemine bırakmak sürprizleri önler.</li>
<li><b>Teklifleri girdikçe güncelleyin.</b> Bu araç tahmin değil, plan aracıdır; gerçek teklifler geldikçe rakamları değiştirin.</li>
<li><b>Sabit maliyetli seçenekleri değerlendirin.</b> Davetiye gibi kalemlerde kişi sayısından bağımsız çözümler, kalabalık düğünlerde ciddi fark yaratır.</li>
</ol>
<h2>Sıkça sorulanlar</h2>
""" + sss_html(BT_SSS) + "</section>"
BT_JS = "const KALEMLER = " + json.dumps([{"k":k,"ad":a,"alt":s,"oran":o} for k,a,s,o in KALEMLER], ensure_ascii=False) + ";\n" + r"""
let S = oku("lavie_butce", { butce: "", kisi: "", tutar: {}, adet: "", adetFiyat: "" });
const kaydet = () => yaz("lavie_butce", S);
function dagit(){ const b = +S.butce || 0; KALEMLER.forEach(x => S.tutar[x.k] = Math.round(b * x.oran / 100 / 100) * 100); }
function hesapla(){
  const b = +S.butce || 0, k = +S.kisi || 0;
  const toplam = KALEMLER.reduce((a,x) => a + (+S.tutar[x.k] || 0), 0);
  $("ozet").innerHTML = `<div><b>${tl(b)}</b><span>Bütçe</span></div><div><b>${tl(toplam)}</b><span>Planlanan</span></div><div><b>${tl(b - toplam)}</b><span>${b - toplam < 0 ? "Aşım" : "Kalan"}</span></div><div><b>${k ? tl(toplam / k) : "–"}</b><span>Kişi başı</span></div>`;
  KALEMLER.forEach(x => { const el = document.querySelector(`[data-cubuk="${x.k}"]`); if (el) el.style.width = (toplam ? Math.min(100, (+S.tutar[x.k]||0) / toplam * 100) : 0) + "%"; });
  $("durum").innerHTML = b ? (toplam > b ? `<div class="durum asim">Planınız bütçeyi <b>${tl(toplam - b)}</b> aşıyor. Davetli sayısını ya da büyük kalemleri gözden geçirin.</div>` : `<div class="durum iyi">Planınız bütçe içinde, <b>${tl(b - toplam)}</b> yedeğiniz var.</div>`) : "";
  const adet = +S.adet || 0, f = +S.adetFiyat || 0;
  $("kagit").textContent = adet && f ? tl(adet * f) : "–";
  $("tasarruf").innerHTML = adet && f ? (adet * f > 500 ? `Dijital davetiyeyle yaklaşık <b>${tl(adet * f - 500)}</b> tasarruf edersiniz.` : `Bu adette kâğıt davetiye daha ucuz görünüyor; dijital davetiyede ise LCV takibi, konum ve müzik dahildir.`) : "";
  kaydet();
}
function ciz(){
  $("kalemler").innerHTML = KALEMLER.map(x => `<div class="kalem"><div class="ad"><b>${x.ad}</b><small>${x.alt}</small><div class="cubuk"><i data-cubuk="${x.k}"></i></div></div><input type="number" min="0" step="500" inputmode="numeric" data-k="${x.k}" value="${S.tutar[x.k] ?? ""}" aria-label="${x.ad} tutarı"></div>`).join("");
  $("kalemler").querySelectorAll("input").forEach(i => i.oninput = () => { S.tutar[i.dataset.k] = i.value === "" ? "" : +i.value; hesapla(); });
  hesapla();
}
$("butce").value = S.butce; $("kisi").value = S.kisi; $("adet").value = S.adet; $("adetFiyat").value = S.adetFiyat;
$("butce").oninput = () => { const ilk = !Object.values(S.tutar).some(v => v !== "" && v != null); S.butce = $("butce").value; if (ilk || S._oto) { dagit(); S._oto = true; ciz(); } else hesapla(); };
$("kisi").oninput = () => { S.kisi = $("kisi").value; if (!S._adetElle) { S.adet = S.kisi ? Math.ceil(S.kisi / 2.5) : ""; $("adet").value = S.adet; } hesapla(); };
$("adet").oninput = () => { S.adet = $("adet").value; S._adetElle = true; hesapla(); };
$("adetFiyat").oninput = () => { S.adetFiyat = $("adetFiyat").value; hesapla(); };
$("kalemler").addEventListener("input", () => { S._oto = false; });
$("dagit").onclick = () => { if (!+S.butce) { $("butce").focus(); return; } dagit(); S._oto = true; ciz(); };
ciz();
"""


# ---------------- Davetiye sözü oluşturucu ----------------
SZ_SSS = [("Davetiye sözü oluşturucu nasıl çalışır?", "Davet türünü ve istediğiniz tarzı seçip isimleri yazdığınızda, araç hazır söz kalıplarını sizin bilgilerinizle birleştirerek öneriler sunar. 'Yeni öneriler' ile farklı seçenekleri görebilir, beğendiğinizi kopyalayabilirsiniz."),
          ("Önerilen sözleri değiştirebilir miyim?", "Elbette. Sözü kopyalayıp dilediğiniz gibi düzenleyebilir ya da 'Bu sözle davetiye oluştur' ile doğrudan davetiye oluşturucuya aktarıp orada değiştirebilirsiniz."),
          ("Ücretli mi?", "Hayır, araç tamamen ücretsizdir ve üyelik gerektirmez.")]
SZ_GOVDE = """
<div class="arac">
  <div class="izgara">
    <div class="alan"><span>Davet türü</span><div class="seg" id="turSec"></div></div>
    <div class="alan"><span>Tarz</span><div class="seg" id="tarzSec"></div></div>
    <div class="iki">
      <label class="alan"><span>Gelin</span><input id="gelin" placeholder="Elif" maxlength="40"></label>
      <label class="alan"><span>Damat</span><input id="damat" placeholder="Burak" maxlength="40"></label>
    </div>
    <label class="alan"><span>Aile isimleri (isteğe bağlı)</span><input id="aile" placeholder="Yılmaz ve Demir aileleri" maxlength="80"></label>
  </div>
  <div class="dugmeler"><button class="btn pri kucuk" type="button" id="yeni">Yeni öneriler</button></div>
  <div class="metinler" id="oneriler" style="margin-top:16px"></div>
</div>
<div class="cta-kutu"><b>Sözünüz davetiyenizde</b><p>Beğendiğiniz sözün altındaki "Bu sözle davetiye oluştur"a dokunun; isimleriniz ve sözünüz hazır şekilde zarfı açılan dijital davetiyenizin önizlemesi açılsın.</p><a class="btn pri" href="/#olustur">Davetiyemi oluştur</a></div>
<section class="makale">
<h2>İyi bir davetiye sözü nasıl olmalı?</h2>
<ol>
<li><b>Kısa olsun.</b> Bir ya da iki cümle yeterli; tarih, saat ve mekân zaten davetiyede ayrıca yer alır.</li>
<li><b>Misafirinize uygun olsun.</b> Aile büyüklerinin ağırlıkta olduğu davetlerde klasik, arkadaş ağırlıklı davetlerde daha samimi bir dil seçin.</li>
<li><b>Size benzesin.</b> Önerileri başlangıç olarak kullanıp kendi hikâyenizden bir kelime eklemek sözü unutulmaz yapar.</li>
</ol>
<p>Daha fazla örnek için <a href="/dugun-davetiyesi-sozleri">düğün</a>, <a href="/kina-davetiyesi-sozleri">kına</a> ve <a href="/nisan-davetiyesi-sozleri">nişan</a> davetiyesi sözleri yazılarımıza göz atın.</p>
<h2>Sıkça sorulanlar</h2>
""" + sss_html(SZ_SSS) + "</section>"
SZ_JS = r"""
const TURLER = { "Düğün": { olay: "düğünümüze", olayAd: "düğün", gun: "en güzel günümüzde", fiil: "evleniyoruz", yer: "düğün törenimize" },
  "Nişan": { olay: "nişan törenimize", olayAd: "nişan", gun: "bu özel günümüzde", fiil: "nişanlanıyoruz", yer: "nişan törenimize" },
  "Kına": { olay: "kına gecemize", olayAd: "kına gecesi", gun: "bu anlamlı gecede", fiil: "kınamızı yakıyoruz", yer: "kına gecemize" },
  "Söz": { olay: "söz törenimize", olayAd: "söz", gun: "bu güzel günümüzde", fiil: "söz kesiyoruz", yer: "söz törenimize" } };
const KALIP = {
  "Klasik": [
    "Ailelerimizin hayır dualarıyla {fiil}. {GUN} sizleri de aramızda görmekten onur duyarız.",
    "{GUN} mutluluğumuzu sizlerle paylaşmak istiyoruz. {YER} teşriflerinizi rica ederiz.",
    "Bir ömür boyu sürecek yolculuğumuzun ilk adımında dualarınız ve varlığınızla yanımızda olmanızı dileriz.",
    "Sevgi ve saygıyla attığımız bu adımda sizleri de {olay} bekliyoruz.",
    "{GUN} varlığınız bizi onurlandıracaktır. {YER} davetlisiniz.",
    "Mutluluğumuzu paylaşmak üzere {yer} sizleri de davet etmekten onur duyarız."],
  "Romantik": [
    "{gelin} ve {damat} olarak iki ayrı hikâyeyi tek bir masalda birleştiriyoruz. Masalımızın bu sayfasında sizi de görmek istiyoruz.",
    "Birlikte gülmeye, birlikte yaşlanmaya karar verdik. Bu kararı {olay} gelerek bizimle kutlayın.",
    "Kalplerimizin aynı ritimde attığı {gun} sevdiklerimizi yanımızda istiyoruz.",
    "Yıllar önce başlayan hikâyemizin en güzel bölümünü sizinle paylaşmak istiyoruz.",
    "Sevgimizi bir ömre taşıdığımız {gun} yanımızda olun.",
    "Aşkımızın en güzel kutlamasında sizi de aramızda görmek istiyoruz."],
  "Kısa": [
    "{GUN} yanımızda olun.",
    "Mutluluğumuza ortak olun; {olay} davetlisiniz.",
    "Biz {fiil}! {gelin} & {damat} olarak sizi de bekleriz.",
    "Sevincimizi sizinle paylaşmak istiyoruz.",
    "İki gönül, tek yol. {YER} bekliyoruz.",
    "Bu mutlu günde sizi de aramızda görmek isteriz."],
  "Aile ağzından": [
    "{AILE} olarak evlatlarımız {gelin} ile {damat} için en mutlu günümüzü yaşıyoruz. Sevincimize ortak olmanızı dileriz.",
    "Evlatlarımızın {gun} sevincimizi sizlerle paylaşmak istiyoruz. {YER} teşriflerinizi rica ederiz.",
    "{gelin} ile {damat} hayırlı bir yuvaya ilk adımını atıyor; dualarınızla yanımızda olun.",
    "Gözümüzün nuru evlatlarımızın {gun} aramızda olmanızı rica ederiz.",
    "{AILE} olarak çocuklarımızın {yer} sizleri de davet ediyoruz.",
    "İki ailenin tek bir aile olduğu {gun} varlığınız bizi mutlu edecek."],
  "Eğlenceli": [
    "Sonunda {fiil}! Sorularınıza son veriyoruz, {olay} bekleriz.",
    "Pasta bizden, dans sizden. Görüşmek üzere!",
    "{gelin} ve {damat} büyük bir karar verdi. Bu cesaretı kutlamaya bekleriz!",
    "Halay başı aranıyor! Başvurular {olayAd} günü kabul edilecektir.",
    "Biz {fiil}, siz eğleniyorsunuz. Bence adil bir anlaşma.",
    "Takvimlerinize not alın: bu sefer gerçekten oluyor!"]
};
const TARZLAR = Object.keys(KALIP);
let S = oku("lavie_soz", { tur: "Düğün", tarz: "Klasik" }), KARIS = 0;
const q = new URLSearchParams(location.search); if (TURLER[q.get("tur")]) S.tur = q.get("tur");
const buyuk = s => s ? s.charAt(0).toLocaleUpperCase("tr") + s.slice(1) : s;
function doldur(k){
  const t = TURLER[S.tur], g = $("gelin").value.trim() || "Elif", d = $("damat").value.trim() || "Burak", a = $("aile").value.trim() || "Yılmaz ve Demir aileleri";
  return k.replace(/\{gun\}/g, t.gun).replace(/\{GUN\}/g, buyuk(t.gun)).replace(/\{olay\}/g, t.olay).replace(/\{olayAd\}/g, t.olayAd)
    .replace(/\{fiil\}/g, t.fiil).replace(/\{yer\}/g, t.yer).replace(/\{YER\}/g, buyuk(t.yer)).replace(/\{gelin\}/g, g).replace(/\{damat\}/g, d)
    .replace(/\{AILE\}/g, buyuk(a)).replace(/cesaretı/g, "cesareti");
}
function seg(el, ogeler, secili, fn){ el.innerHTML = ogeler.map(k => `<button type="button" data-k="${k}" aria-pressed="${k===secili}">${k}</button>`).join(""); el.querySelectorAll("button").forEach(b => b.onclick = () => fn(b.dataset.k)); }
function ciz(){
  seg($("turSec"), Object.keys(TURLER), S.tur, k => { S.tur = k; yaz("lavie_soz", S); ciz(); });
  seg($("tarzSec"), TARZLAR, S.tarz, k => { S.tarz = k; KARIS = 0; yaz("lavie_soz", S); ciz(); });
  const liste = KALIP[S.tarz], n = liste.length, sec = [0,1,2,3].map(i => liste[(i + KARIS) % n]);
  $("oneriler").innerHTML = sec.map(k => { const m = doldur(k);
    const link = "/?" + new URLSearchParams({ tur: S.tur, gelin: $("gelin").value.trim(), damat: $("damat").value.trim(), aile: $("aile").value.trim(), not: m }).toString() + "#olustur";
    return `<div class="metin" style="grid-template-columns:1fr"><p>“${esc(m)}”</p><div style="display:flex;gap:6px;flex-wrap:wrap"><button type="button" data-m="${esc(m)}">Kopyala</button><a class="btn pri" style="padding:8px 14px;font-size:.8rem" href="${esc(link)}">Bu sözle davetiye oluştur</a></div></div>`; }).join("");
  $("oneriler").querySelectorAll("[data-m]").forEach(b => b.onclick = async () => { try { await navigator.clipboard.writeText(b.dataset.m); b.textContent = "Kopyalandı"; } catch { b.textContent = "Kopyalanamadı"; } setTimeout(() => b.textContent = "Kopyala", 1800); });
}
["gelin","damat","aile"].forEach(k => $(k).addEventListener("input", ciz));
$("yeni").onclick = () => { KARIS = (KARIS + 4) % KALIP[S.tarz].length; ciz(); };
ciz();
"""

# ---------------- 2027 düğün takvimi ----------------
TK_SSS = [("2027'de Ramazan Bayramı ve Kurban Bayramı ne zaman?", "Diyanet takvimine göre 2027 Ramazan Bayramı 9-11 Mart (arefe 8 Mart Pazartesi), Kurban Bayramı 16-19 Mayıs (arefe 15 Mayıs Cumartesi) tarihlerindedir. Ramazan ayı 8 Şubat Pazartesi günü başlar."),
          ("İki bayram arası düğün yapılır mı?", "Halk arasında Ramazan Bayramı ile Kurban Bayramı arasında düğün yapılmaması geleneği vardır. Dinî bir yasak değildir ve pek çok çift bu dönemde evlenir; ancak aileleriniz bu geleneğe önem veriyorsa 2027'de 12 Mart ile 15 Mayıs arası bu döneme denk gelir."),
          ("2027'de düğün için en uygun tarihler hangileri?", "Uzaktan gelecek misafirleriniz varsa resmî tatille birleşen hafta sonları avantajlıdır: 2-3 Ocak, 24-25 Nisan, 28-29 Ağustos ve 30-31 Ekim 2027. Haziran-Eylül cumartesileri en yoğun dönemdir; salonlar bu tarihler için aylar önceden dolar."),
          ("Düğün tarihini ne kadar önceden belirlemeliyiz?", "Yaz sezonu ve cumartesi günleri için salon rezervasyonunu 8-12 ay önceden yapmak gerekir. Tarih kesinleşince misafirlere 'tarihi kaydedin' mesajı, düğünden 4-6 hafta önce de davetiye gönderilir."),
          ("Düğün için hafta içi mi hafta sonu mu daha uygun?", "Cumartesi en çok tercih edilen ve en pahalı gündür. Cuma ve pazar akşamları salonlarda genellikle daha uygun fiyat bulunur; hafta içi düğünler en ekonomik seçenektir ancak çalışan misafirler için katılımı zorlaştırabilir.")]
TK_GOVDE = """
<div class="arac">
  <div class="iki tek" style="align-items:end">
    <label class="alan"><span>Düşündüğünüz tarih</span><input id="tarih" type="date" min="2027-01-01" max="2027-12-31" value="2027-06-19"></label>
    <div class="seg" id="filtre"></div>
  </div>
  <div class="durum" id="sonuc" aria-live="polite"></div>
  <div class="lejant" id="lejant"></div>
  <div class="aylar" id="aylar"></div>
  <p class="not">Dinî gün tarihleri Diyanet İşleri Başkanlığı'nın 2027 takvimine dayanır. Bayram öncesi veya sonrası verilebilecek ek idari izin günleri henüz açıklanmadığı için takvimde yer almaz.</p>
</div>
<h2 style="font-size:1.6rem;margin-top:44px">2027 resmî tatiller ve dinî bayramlar</h2>
<div class="satirlar">
  <div class="satir"><div><b>1 Ocak, Cuma</b><small>Yılbaşı · 2-3 Ocak uzun hafta sonu</small></div></div>
  <div class="satir"><div><b>22 Ocak, Cuma</b><small>Berat Kandili</small></div></div>
  <div class="satir"><div><b>8 Şubat - 8 Mart</b><small>Ramazan ayı (Kadir Gecesi 5 Mart Cuma)</small></div></div>
  <div class="satir"><div><b>9-11 Mart, Salı-Perşembe</b><small>Ramazan Bayramı · arefe 8 Mart Pazartesi</small></div></div>
  <div class="satir"><div><b>23 Nisan, Cuma</b><small>Ulusal Egemenlik ve Çocuk Bayramı · 24-25 Nisan uzun hafta sonu</small></div></div>
  <div class="satir"><div><b>1 Mayıs, Cumartesi</b><small>Emek ve Dayanışma Günü</small></div></div>
  <div class="satir"><div><b>16-19 Mayıs, Pazar-Çarşamba</b><small>Kurban Bayramı · arefe 15 Mayıs Cumartesi · 19 Mayıs aynı gün</small></div></div>
  <div class="satir"><div><b>15 Temmuz, Perşembe</b><small>Demokrasi ve Millî Birlik Günü</small></div></div>
  <div class="satir"><div><b>30 Ağustos, Pazartesi</b><small>Zafer Bayramı · 28-29 Ağustos uzun hafta sonu</small></div></div>
  <div class="satir"><div><b>28 Ekim yarım gün, 29 Ekim Cuma</b><small>Cumhuriyet Bayramı · 30-31 Ekim uzun hafta sonu</small></div></div>
</div>
<h2 style="font-size:1.6rem;margin-top:44px">Tarih seçerken dikkat edilecekler</h2>
<div class="makale">
<p><b>Ramazan ayı (8 Şubat - 8 Mart 2027):</b> Oruç tutan misafirler nedeniyle düğün ve kına genellikle yapılmaz. Nişan ve söz törenleri iftar sonrasına alınabilir.</p>
<p><b>İki bayram arası (12 Mart - 15 Mayıs 2027):</b> Bazı aileler bu dönemde düğün yapmamayı tercih eder. Dinî bir yasak değildir; aile büyüklerinize danışmanız yeterli.</p>
<p><b>Uzun hafta sonları:</b> Şehir dışından gelecek misafirleriniz çoksa resmî tatille birleşen hafta sonları katılımı artırır.</p>
<p><b>Yaz cumartesileri (Haziran-Eylül):</b> En yoğun ve en pahalı dönemdir. Salon ve fotoğrafçıyı erken ayırtın, davetiyeyi düğünden 4-6 hafta önce gönderin.</p>
<p><b>Özel tarih:</b> 07.07.2027 Çarşamba gününe denk gelir; akılda kalan tarih isteyen çiftler için hafta içi bir seçenek.</p>
</div>
<div class="cta-kutu"><b>Tarihiniz belli mi?</b><p>Dijital davetiyenizi hemen hazırlayın: geri sayım, konum ve katılım formu tek linkte. Misafirleriniz WhatsApp'tan tek dokunuşla açar.</p><a class="btn pri" href="/?tur=Düğün#olustur">Davetiyemi oluştur</a></div>
""" + sss_html(TK_SSS)
TK_JS = r"""
const AY = ["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"];
const GUN = ["Pazar","Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi"];
const T = {
  "2027-01-01":["tatil","Yılbaşı"], "2027-01-22":["kandil","Berat Kandili"],
  "2027-03-05":["ramazan","Kadir Gecesi"], "2027-03-08":["bayram","Ramazan Bayramı arefesi"],
  "2027-03-09":["bayram","Ramazan Bayramı 1. gün"], "2027-03-10":["bayram","Ramazan Bayramı 2. gün"], "2027-03-11":["bayram","Ramazan Bayramı 3. gün"],
  "2027-04-23":["tatil","23 Nisan Ulusal Egemenlik ve Çocuk Bayramı"], "2027-05-01":["tatil","1 Mayıs Emek ve Dayanışma Günü"],
  "2027-05-15":["bayram","Kurban Bayramı arefesi"], "2027-05-16":["bayram","Kurban Bayramı 1. gün"], "2027-05-17":["bayram","Kurban Bayramı 2. gün"],
  "2027-05-18":["bayram","Kurban Bayramı 3. gün"], "2027-05-19":["bayram","Kurban Bayramı 4. gün · 19 Mayıs"],
  "2027-07-15":["tatil","15 Temmuz Demokrasi ve Millî Birlik Günü"], "2027-08-30":["tatil","30 Ağustos Zafer Bayramı"],
  "2027-10-28":["tatil","Cumhuriyet Bayramı arefesi (yarım gün)"], "2027-10-29":["tatil","29 Ekim Cumhuriyet Bayramı"]
};
const UZUN = {"2027-01-02":"Yılbaşı","2027-01-03":"Yılbaşı","2027-04-24":"23 Nisan","2027-04-25":"23 Nisan","2027-08-28":"30 Ağustos","2027-08-29":"30 Ağustos","2027-10-30":"29 Ekim","2027-10-31":"29 Ekim"};
const ACIK = {
  bayram:["Bayram","Aileler bayramda ziyaretlerde ve memlekette olur; düğün yapılmaz."],
  ramazan:["Ramazan · kandil","Oruç nedeniyle düğün ve kına genellikle yapılmaz."],
  ikiBayram:["İki bayram arası","Bazı aileler bu dönemde düğün yapmamayı tercih eder (gelenek, dinî yasak değil)."],
  tatil:["Resmî tatil","Misafirler izinli; tatile çıkanlar olabilir."],
  kandil:["Kandil","Bazı aileler kandil gecelerinde düğün yapmamayı tercih eder."],
  uzun:["Uzun hafta sonu","Şehir dışından gelecek misafirler için ideal."],
  yogun:["Yoğun sezon","Yaz cumartesisi: salonlar aylar önceden dolar, erken ayırtın."],
  uygun:["Uygun","Bilinen bir engel yok."]
};
const iso = d => d.getFullYear()+"-"+String(d.getMonth()+1).padStart(2,"0")+"-"+String(d.getDate()).padStart(2,"0");
function tur(s){
  if (T[s]) return T[s][0];
  if (s >= "2027-02-08" && s <= "2027-03-07") return "ramazan";
  if (UZUN[s]) return "uzun";
  if (s >= "2027-03-12" && s <= "2027-05-14") return "ikiBayram";
  const d = new Date(s+"T12:00"); if (d.getDay()===6 && d.getMonth()>=5 && d.getMonth()<=8) return "yogun";
  return "uygun";
}
let F = oku("lavie_tk", "Hafta sonu");
function seg(){ $("filtre").innerHTML = ["Hafta sonu","Tüm günler"].map(k=>`<button type="button" aria-pressed="${k===F}">${k}</button>`).join("");
  $("filtre").querySelectorAll("button").forEach(b=>b.onclick=()=>{F=b.textContent;yaz("lavie_tk",F);seg();takvim();}); }
function takvim(){
  $("lejant").innerHTML = ["uygun","uzun","yogun","ikiBayram","ramazan","bayram","tatil"].map(k=>`<span><i class="g ${k}"></i>${ACIK[k][0]}</span>`).join("");
  let h = "";
  for (let m=0;m<12;m++){
    const ilk = new Date(2027,m,1), bos = (ilk.getDay()+6)%7, son = new Date(2027,m+1,0).getDate();
    h += `<div class="ay"><b>${AY[m]}</b><div class="hg">${"PSÇPCCP".split("").map(x=>`<i>${x}</i>`).join("")}${"<span></span>".repeat(bos)}`;
    for (let g=1; g<=son; g++){ const d=new Date(2027,m,g), s=iso(d), t=tur(s), hs=d.getDay()===0||d.getDay()===6;
      const sol = F==="Hafta sonu" && !hs && !T[s] ? " sol" : "";
      h += `<button type="button" class="g ${t}${sol}${s===$("tarih").value?" sec":""}" data-s="${s}" aria-label="${g} ${AY[m]} ${GUN[d.getDay()]}: ${ACIK[t][0]}">${g}</button>`; }
    h += `</div></div>`;
  }
  $("aylar").innerHTML = h;
  $("aylar").querySelectorAll("button").forEach(b=>b.onclick=()=>{$("tarih").value=b.dataset.s;sonuc();takvim();});
}
function sonuc(){
  const s = $("tarih").value; if (!s) { $("sonuc").hidden = true; return; }
  const d = new Date(s+"T12:00"), t = tur(s), [ad, ac] = ACIK[t];
  const ek = T[s] ? T[s][1] + ". " : UZUN[s] ? UZUN[s] + " tatiliyle birleşen hafta sonu. " : "";
  const kalan = Math.round((d - new Date(new Date().toDateString())) / 864e5);
  $("sonuc").hidden = false;
  $("sonuc").className = "durum " + (["bayram","ramazan"].includes(t) ? "asim" : ["ikiBayram","kandil","tatil","yogun"].includes(t) ? "orta" : "iyi");
  $("sonuc").innerHTML = `<b>${d.getDate()} ${AY[d.getMonth()]} 2027, ${GUN[d.getDay()]}</b> · ${ad}<br>${esc(ek + ac)}${kalan>0?`<br><small>Bugünden ${kalan.toLocaleString("tr-TR")} gün sonra.</small>`:""}`;
}
$("tarih").addEventListener("change", ()=>{sonuc();takvim();});
seg(); takvim(); sonuc();
"""

ARACLAR = [
 dict(slug="davetli-listesi", ad="Davetli listesi", title="Ücretsiz Düğün Davetli Listesi Hazırlama Aracı (Excel'e Aktar) | LaVie",
      desc="Düğün, nişan ve kına davetli listenizi ücretsiz hazırlayın: gelin ve damat tarafı, gruplar, kişi sayısı, toplamlar ve Excel'e aktarma. Üyelik gerekmez.",
      h1=("Davetli", "listesi"), giris="Misafirlerinizi ekleyin; gelin ve damat tarafına, gruplara göre toplam kişi sayınızı anında görün. Listenizi Excel'e aktarın ya da yazdırın. Ücretsiz, üyelik gerekmez.",
      govde=DL_GOVDE, js=DL_JS, sss=DL_SSS),
 dict(slug="dugun-butcesi-hesaplama", ad="Düğün bütçesi hesaplama", title="Düğün Bütçesi Hesaplama Aracı: Kalem Kalem Plan, Kişi Başı Maliyet | LaVie",
      desc="Ücretsiz düğün bütçesi hesaplayıcı: toplam bütçenizi salon, kıyafet, fotoğraf, takı gibi kalemlere dağıtın, kişi başı maliyeti ve kâğıt-dijital davetiye farkını görün.",
      h1=("Düğün bütçesi", "hesaplama"), giris="Toplam bütçenizi ve davetli sayınızı girin; kalem kalem planlayın, kişi başı maliyetinizi ve kalan bütçenizi anında görün. Ücretsiz, üyelik gerekmez.",
      govde=BT_GOVDE, js=BT_JS, sss=BT_SSS),
 dict(slug="davetiye-sozu-olusturucu", ad="Davetiye sözü oluşturucu", title="Davetiye Sözü Oluşturucu: İsimlerinize Özel Düğün, Nişan, Kına Sözleri | LaVie",
      desc="Ücretsiz davetiye sözü oluşturucu: davet türünü ve tarzı seçin, isimleri yazın; size özel düğün, nişan, kına ve söz davetiyesi sözleri anında hazır.",
      h1=("Davetiye sözü", "oluşturucu"), giris="Davet türünü ve tarzını seçin, isimleri yazın; size özel davetiye sözleri anında hazırlansın. Beğendiğinizi kopyalayın ya da doğrudan davetiyenize aktarın.",
      govde=SZ_GOVDE, js=SZ_JS, sss=SZ_SSS),
 dict(slug="2027-dugun-takvimi", ad="2027 düğün takvimi", title="2027 Düğün Takvimi: Bayramlar, Ramazan, Uzun Hafta Sonları ve Uygun Tarihler | LaVie",
      desc="2027 düğün takvimi: Ramazan ve Kurban Bayramı, Ramazan ayı, iki bayram arası, resmî tatiller ve uzun hafta sonları tek takvimde. Düğün tarihinizin uygun olup olmadığını hemen görün.",
      h1=("2027 düğün", "takvimi"), giris="Düğün, nişan ya da kına için düşündüğünüz tarihi seçin; bayram, Ramazan, iki bayram arası, resmî tatil ve yoğun sezon bilgisini anında görün. Uzaktan gelecek misafirler için uzun hafta sonlarını da işaretledik.",
      govde=TK_GOVDE, js=TK_JS, sss=TK_SSS),
]

def araclar_ana():
    kart = "".join(f'<a class="kart" href="/{a["slug"]}" style="text-decoration:none;display:block"><h3>{e(a["ad"])}</h3><p>{e(a["desc"])}</p></a>' for a in ARACLAR)
    url = U + "/araclar"
    return f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon-48.png" sizes="48x48" type="image/png"><link rel="apple-touch-icon" href="/favicon-180.png"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Ücretsiz Düğün Araçları: Davetli Listesi, Bütçe Hesaplama | LaVie</title>
<meta name="description" content="Düğün hazırlığı için ücretsiz araçlar: davetli listesi hazırlama, düğün bütçesi hesaplama ve davetiye sözü oluşturucu. Üyelik gerekmez.">
<link rel="canonical" href="{url}"><meta name="theme-color" content="#f6f3f1">
<meta property="og:type" content="website"><meta property="og:title" content="Ücretsiz düğün araçları · LaVie"><meta property="og:url" content="{url}"><meta property="og:image" content="{U}/og/lavie.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Italiana&family=Pinyon+Script&family=Cormorant+Garamond:ital,wght@0,400;1,400&family=Jost:wght@400;500&display=swap">
<style>{CSS}</style></head><body>
<a class="ust-serit" href="https://instagram.com/la.viecreative" target="_blank" rel="noopener"><div class="in">{IG}<span>Instagram'da biz: <b>@la.viecreative</b></span></div></a>
<header class="nav"><div class="in"><a href="/" aria-label="LaVie Davetiye ana sayfa"><img src="/logo.svg" alt="La Vie Creative Studio" width="630" height="165"></a><a class="btn pri" href="/#olustur">Davetiyemi oluştur</a></div></header>
<main class="in" style="padding-bottom:60px"><div class="yol"><a href="/">Ana sayfa</a> › Ücretsiz araçlar</div>
<div class="eyebrow" style="margin-top:26px">Ücretsiz</div><h1>Düğün <em>araçları</em></h1>
<p class="lead">Düğün hazırlığını kolaylaştıran ücretsiz araçlar. Üyelik gerekmez, bilgileriniz yalnızca kendi cihazınızda saklanır.</p>
<div class="kartlar">{kart}</div>
<h2 style="font-size:1.6rem;margin-top:48px">Davetiye rehberi</h2><div class="diger">{"".join(f'<a href="/{y["slug"]}">{e(y["kisa"])}</a>' for y in YAZILAR)}</div></main>
<footer><div class="in"><a href="/" aria-label="LaVie Davetiye"><img src="/logo-acik.svg" alt="La Vie Creative Studio" width="630" height="165"></a><span>© 2026 LaVie Davetiye</span></div></footer>
<script src="/ayarlar.js"></script></body></html>
"""

def yaz_hepsi():
    for a in ARACLAR:
        open(os.path.join(KOK, a["slug"] + ".html"), "w", encoding="utf8").write(kabuk(a["slug"], a["title"], a["desc"], a["h1"], a["giris"], a["govde"], a["js"], (sss_ld(a["sss"]),)))
    open(os.path.join(KOK, "araclar.html"), "w", encoding="utf8").write(araclar_ana())
    site_haritasi(["rehber"] + [y["slug"] for y in YAZILAR] + ["araclar"] + [a["slug"] for a in ARACLAR])

if __name__ == "__main__":
    yaz_hepsi()
    print("ok", [a["slug"] for a in ARACLAR])
