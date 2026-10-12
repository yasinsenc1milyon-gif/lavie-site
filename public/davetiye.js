// Lavie davetiye çizici: vitrin, canlı davetiye ve önizleme aynı kodu kullanır.
(function () {
  const esc = s => String(s == null ? "" : s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

  const LEAF = `<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><path d="M10 10 Q90 60 170 170" fill="none" stroke="currentColor" stroke-width="1.6"/><g fill="currentColor" opacity=".5">${[.14,.28,.42,.56,.7,.84].map((t,i)=>{const x=10+160*t,y=10+160*t*t*.9+60*t*(1-t);return `<ellipse cx="${x+13}" cy="${y-9}" rx="13" ry="5" transform="rotate(${-30-i*4} ${x+13} ${y-9})"/><ellipse cx="${x-8}" cy="${y+13}" rx="13" ry="5" transform="rotate(${60+i*4} ${x-8} ${y+13})"/>`}).join("")}</g></svg>`;
  const TILE = `url("data:image/svg+xml,${encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" fill="#2a4c9a"/><circle cx="20" cy="20" r="11" fill="none" stroke="#fbfaf6" stroke-width="2"/><path d="M20 4 L24 16 L36 20 L24 24 L20 36 L16 24 L4 20 L16 16Z" fill="#fbfaf6"/><circle cx="20" cy="20" r="3" fill="#2a4c9a"/><circle cx="0" cy="0" r="5" fill="#fbfaf6"/><circle cx="40" cy="0" r="5" fill="#fbfaf6"/><circle cx="0" cy="40" r="5" fill="#fbfaf6"/><circle cx="40" cy="40" r="5" fill="#fbfaf6"/></svg>')}")`;
  // Yeni tatlı tasarımların süsleri
  const DAISY = `<svg viewBox="0 0 40 40"><g fill="#fffdf6" stroke="#eadfc4" stroke-width=".5">${Array.from({length:14},(_,i)=>`<ellipse cx="20" cy="9.5" rx="3.1" ry="8.5" transform="rotate(${i*360/14} 20 20)"/>`).join("")}</g><circle cx="20" cy="20" r="5" fill="#f2c14e"/><circle cx="20" cy="20" r="5" fill="none" stroke="#e0a935" stroke-width=".8"/></svg>`;
  const LEAFLET = `<svg viewBox="0 0 40 20"><path d="M2 10 Q20 -4 38 10 Q20 24 2 10Z" fill="#9fb67a"/><path d="M4 10 H36" stroke="#7f9a5c" stroke-width=".8"/></svg>`;
  const papatyalar = () => [[-6,-4,30,-10],[18,6,18,20],[4,22,14,0],[30,-2,10,40],[74,150,30,170],[62,164,18,150],[86,140,14,190],[60,150,10,200],[8,70,7,0],[86,60,8,0],[16,120,6,0],[82,100,6,0]]
    .map(([x,y,w,r])=>`<div class="deco dz" style="left:${x}cqw;top:${y}cqw;width:${w}cqw;transform:rotate(${r}deg)">${DAISY}</div>`).join("")
    + [[14,24,14,30],[-2,22,12,-20],[70,148,14,200],[86,156,12,150]].map(([x,y,w,r])=>`<div class="deco lf" style="left:${x}cqw;top:${y}cqw;width:${w}cqw;transform:rotate(${r}deg)">${LEAFLET}</div>`).join("");
  const SPRIG = `<svg viewBox="0 0 40 200"><path d="M20 200 Q22 110 20 14" stroke="#7d8f69" stroke-width="1.6" fill="none"/>${Array.from({length:16},(_,i)=>{const y=18+i*6.2,s=i%2?1:-1,c=["#9b84c6","#b6a1dc","#8670b8","#c8b8e8"][i%4];return `<ellipse cx="${20+s*4.2}" cy="${y}" rx="3.6" ry="5.6" fill="${c}" transform="rotate(${s*28} ${20+s*4.2} ${y})"/>`}).join("")}<ellipse cx="20" cy="14" rx="3" ry="5" fill="#b6a1dc"/></svg>`;
  const buket = (x,y,r,sc) => `<div class="deco lv" style="left:${x}cqw;top:${y}cqw;transform:rotate(${r}deg) scale(${sc})">${[-18,0,18].map(a=>`<div style="transform:rotate(${a}deg)">${SPRIG}</div>`).join("")}<i class="kurdele"></i></div>`;
  const BLOSSOM = c => `<svg viewBox="0 0 40 40">${Array.from({length:5},(_,i)=>`<ellipse cx="20" cy="10.5" rx="7.4" ry="9.5" fill="${c}" transform="rotate(${i*72} 20 20)"/>`).join("")}<circle cx="20" cy="20" r="4" fill="#fff4e6"/>${Array.from({length:7},(_,i)=>`<circle cx="${20+6.5*Math.cos(i*0.9)}" cy="${20+6.5*Math.sin(i*0.9)}" r="1" fill="#d9825f"/>`).join("")}</svg>`;
  const dal = (x,y,r,sc) => `<div class="deco dal" style="left:${x}cqw;top:${y}cqw;transform:rotate(${r}deg) scale(${sc})"><svg viewBox="0 0 120 60"><path d="M0 50 Q40 40 70 22 T120 6" stroke="#8a6650" stroke-width="2" fill="none"/><path d="M50 32 Q58 46 72 50" stroke="#8a6650" stroke-width="1.4" fill="none"/></svg>${[[30,28,16,"#f6b8a4"],[58,8,20,"#f9c7b6"],[86,-6,15,"#f3a891"],[66,36,13,"#fbd5c8"],[104,-12,10,"#f6b8a4"]].map(([a,b,w,c])=>`<i style="left:${a}%;top:${b}%;width:${w}%">${BLOSSOM(c)}</i>`).join("")}</div>`;
  const HEART = c => `<svg viewBox="0 0 32 30"><path d="M16 29 C6 21 0 15 0 8.5 A7.6 7.6 0 0 1 16 5 A7.6 7.6 0 0 1 32 8.5 C32 15 26 21 16 29Z" fill="${c}"/></svg>`;
  const kalpler = () => [[6,8,9,"#f4a7bd",-12],[80,12,7,"#f9c5d3",10],[14,44,5,"#f7b8ca",8],[86,46,10,"#ee93ad",14],[70,26,4,"#f4a7bd",-6],[4,140,8,"#f9c5d3",-10],[82,150,7,"#f4a7bd",12],[30,160,4,"#ee93ad",0],[60,166,6,"#f7b8ca",-14],[46,10,4,"#f9c5d3",6],[90,100,5,"#f7b8ca",-8],[6,96,6,"#f4a7bd",10]]
    .map(([x,y,w,c,r],i)=>`<div class="deco kalp" style="left:${x}cqw;top:${y}cqw;width:${w}cqw;--r:${r}deg;animation-delay:${-i*.7}s">${HEART(c)}</div>`).join("");
  const stars = () => Array.from({ length: 18 }, (_, i) => `<i class="deco star" style="left:${(i*53)%96+2}%;top:${(i*37)%92+3}%;opacity:${.3+(i%4)*.15}"></i>`).join("");

  const TASARIMLAR = [
    { id: "zeytin", ad: "Zeytin Gölgesi", mini: ["#f1f1e8", "#34402a", "Pinyon Script"], hero: () => `<div class="deco leaf a">${LEAF}</div><div class="deco leaf b">${LEAF}</div>` },
    { id: "pamuk", ad: "Pamuk Şeker", mini: ["#fde9ee", "#b04a6c", "Parisienne"], hero: kalpler },
    { id: "papatya", ad: "Papatya Sabahı", mini: ["#fbf7e9", "#5d6b3a", "Great Vibes"], hero: papatyalar },
    { id: "gece", ad: "Yıldızlı Gece", mini: ["#141a2e", "#d1ad6b", "Italiana"], hero: () => `<div class="deco frame"></div>${stars()}` },
    { id: "seftali", ad: "Şeftali Çiçeği", mini: ["#fdf1ea", "#b0573f", "Great Vibes"], hero: () => `<div class="deco lek a"></div><div class="deco lek b"></div>${dal(40, 4, 0, 1)}${dal(-12, 150, 180, .9)}` },
    { id: "lavanta", ad: "Lavanta Rüzgârı", mini: ["#f3effa", "#5b4a86", "Pinyon Script"], hero: () => `${buket(-6, 122, 24, .95)}${buket(88, -30, 204, .6)}` },
    { id: "gul", ad: "Pudra Gülü", mini: ["#f3e6e3", "#a8676b", "Great Vibes"], hero: () => `<div class="deco arch"></div>` },
    { id: "nane", ad: "Nane Şekeri", mini: ["#e6f4ee", "#2f6656", "Parisienne"], hero: () => `<div class="deco serit ust"></div><div class="deco serit alt"></div><div class="deco fiyonk">${HEART("#fff")}</div>` },
    { id: "ege", ad: "Ege Çinisi", mini: ["#fbfaf6", "#2a4c9a", "Marcellus"], hero: () => `<div class="deco tile top" style="background-image:${TILE}"></div><div class="deco tile bot" style="background-image:${TILE}"></div>` },
    { id: "mono", ad: "Siyah İnci", mini: ["#141414", "#fbfbfa", "Bodoni Moda"], hero: () => `<div class="deco hbar" style="top:12cqw"></div><div class="deco hbar" style="bottom:12cqw"></div>` }
  ];
  const TURLER = ["Düğün", "Nişan", "Kına", "Söz"];
  const YAZILAR = [["", "Tasarımın yazısı", null], ["el", "El yazısı", "Great Vibes"], ["zarif", "Zarif", "Pinyon Script"], ["klasik", "Klasik", "Cormorant Garamond"], ["modern", "Modern", "Italiana"], ["bodoni", "Moda", "Bodoni Moda"], ["sade", "Sade", "Marcellus"]];
  const KATILIM_NOTLARI = ["Çocuklarımıza iyi uykular dileriz.", "Lütfen katılım durumunuzu düğünden bir hafta önce bildiriniz.", "Davetiyemiz kişiye özeldir.", "Kıyafet önerisi: şık ve açık renkler."];
  const UST = { "Düğün": "Evleniyoruz", "Nişan": "Nişanlanıyoruz", "Kına": "Kına gecemize davetlisiniz", "Söz": "Söz törenimize davetlisiniz" };

  function hedef(d) {
    let tr = String(d.tarih || "").trim();
    if (!tr) return null;
    const m = tr.match(/^(\d{1,2})[./-](\d{1,2})[./-](\d{4})$/); // 12.06.2027 biçimi
    if (m) tr = `${m[3]}-${m[2].padStart(2, "0")}-${m[1].padStart(2, "0")}`;
    const saat = /^\d{1,2}[:.]\d{2}$/.test(String(d.saat || "").trim()) ? String(d.saat).trim().replace(".", ":").padStart(5, "0") : "00:00";
    const t = new Date(tr + "T" + saat);
    return isNaN(t) ? null : t;
  }
  function uzunTarih(d) { const t = hedef(d); return t ? t.toLocaleDateString("tr-TR", { day: "numeric", month: "long", year: "numeric" }) : ""; }
  function gun(d) { const t = hedef(d); return t ? t.toLocaleDateString("tr-TR", { weekday: "long" }) : ""; }
  function haritaLinki(d) {
    const l = String(d.konum || "").trim();
    if (/^https:\/\/(maps\.app\.goo\.gl|goo\.gl\/maps|(www\.)?google\.[a-z.]+\/maps|maps\.google\.)/i.test(l)) return l;
    return "https://www.google.com/maps/search/?api=1&query=" + encodeURIComponent(((d.mekan || "") + " " + (d.adres || "")).trim());
  }

  function html(d, ek) {
    ek = ek || {};
    const t = TASARIMLAR.find(x => x.id === d.tasarim) || TASARIMLAR[0];
    const tur = UST[d.tur] ? d.tur : "Düğün";
    const gelin = esc(d.gelin || "Gelin"), damat = esc(d.damat || "Damat");
    const prog = String(d.program || "").split(/\n|\s\|\s/).map(l => l.trim()).filter(Boolean).map(l => {
      const m = l.match(/^(\d{1,2}[:.]\d{2})\s*(.*)$/);
      return m ? `<li><b>${esc(m[1].replace(".", ":"))}</b><span>${esc(m[2])}</span></li>` : `<li><b></b><span>${esc(l)}</span></li>`;
    }).join("");
    const t0 = hedef(d);
    const yazi = YAZILAR.some(y => y[0] && y[0] === d.yazi) ? ` y-${d.yazi}` : "";
    return `<div class="inv t-${t.id}${yazi}">
      <section class="hero">${t.hero()}
        <div class="eyebrow">${esc(UST[tur])}</div>
        <h1 class="names">${gelin}<span class="amp">&amp;</span>${damat}</h1>
        <div class="hdate">${esc(uzunTarih(d))}</div>
        ${d.aile ? `<div class="fam">${esc(d.aile)}</div>` : ""}
        <div class="scroll">Aşağı kaydırın</div>
      </section>
      ${d.not ? `<section class="note"><p>${esc(d.not)}</p></section>` : ""}
      ${t0 ? `<section><h3>Büyük güne kalan</h3><div class="cd" data-t="${t0.getTime()}"></div></section>` : ""}
      ${prog ? `<section><h3>Program</h3><p style="margin-bottom:5cqw;color:var(--soft)">${esc(gun(d))}, ${esc(uzunTarih(d))}</p><ol>${prog}</ol></section>` : ""}
      ${d.mekan || d.adres ? `<section><h3>Konum</h3><div class="venue">${esc(d.mekan)}</div><div class="addr">${esc(d.adres)}</div>
        <a class="ibtn" href="${esc(haritaLinki(d))}" target="_blank" rel="noopener">Yol tarifi al</a></section>` : ""}
      <section><h3>Katılım</h3>
        ${d.katilimNotu ? `<p class="knot">${esc(d.katilimNotu)}</p>` : ""}
        <form class="rsvp">
          <input name="isim" placeholder="Adınız soyadınız" aria-label="Adınız soyadınız" maxlength="80" required>
          <select name="kisi" aria-label="Kişi sayısı"><option value="1">1 kişi</option><option value="2">2 kişi</option><option value="3">3 kişi</option><option value="4">4 kişi</option><option value="5">5+ kişi</option></select>
          <select name="durum" aria-label="Katılım"><option value="Katılacak">Katılacağım</option><option value="Katılamayacak">Maalesef katılamayacağım</option></select>
          <button class="ibtn solid" type="submit">Yanıtımı gönder</button>
          <div class="rsvp-ok" hidden></div>
        </form></section>
      <section class="defter"><h3>Hatıra Defteri</h3>
        <p style="color:var(--soft);margin-bottom:5cqw">Bize güzel bir not bırakın, ömür boyu saklayalım.</p>
        <form class="mesaj-f">
          <input name="isim" placeholder="Adınız" aria-label="Adınız" maxlength="60" required>
          <textarea name="mesaj" placeholder="Mesajınız" aria-label="Mesajınız" maxlength="400" rows="3" required></textarea>
          <button class="ibtn solid" type="submit">Mesaj bırak</button>
          <div class="rsvp-ok" hidden></div>
        </form>
        <div class="mesajlar">${(ek.mesajlar || []).map(mesajKart).join("")}</div>
      </section>
      <footer>${gelin} &amp; ${damat}<small><a href="/${d.slug && d.slug !== "ornek" ? "?ref=d-" + esc(d.slug) : ""}" target="_blank" rel="noopener" style="text-decoration:none">LaVie Davetiye</a></small></footer>
    </div>`;
  }

  function mesajKart(m) {
    const z = m.zaman ? new Date(m.zaman).toLocaleDateString("tr-TR", { day: "numeric", month: "long" }) : "";
    return `<figure class="mk"><blockquote>${esc(m.mesaj)}</blockquote><figcaption>${esc(m.isim)}${z ? ` · ${esc(z)}` : ""}</figcaption></figure>`;
  }
  function sayac() {
    document.querySelectorAll(".inv .cd[data-t]").forEach(el => {
      const ms = Math.max(0, Number(el.dataset.t) - Date.now());
      const g = Math.floor(ms / 864e5), s = Math.floor(ms / 36e5) % 24, dk = Math.floor(ms / 6e4) % 60, sn = Math.floor(ms / 1e3) % 60;
      el.innerHTML = [[g, "Gün"], [s, "Saat"], [dk, "Dakika"], [sn, "Saniye"]].map(([n, l]) => `<div><b>${String(n).padStart(2, "0")}</b><small>${l}</small></div>`).join("");
    });
  }
  setInterval(sayac, 1000);

  // kok: kapsayıcı eleman, d: çift bilgileri, yanitGonder: async ({isim,kisi,durum}) => void
  // ek: { mesajlar, mesajGonder: async ({isim,mesaj}) => kayıt }
  function ciz(kok, d, yanitGonder, ek) {
    ek = ek || {};
    kok.innerHTML = html(d, ek);
    const mf = kok.querySelector("form.mesaj-f");
    const mok = mf.querySelector(".rsvp-ok"), mbtn = mf.querySelector("button");
    mf.addEventListener("submit", async e => {
      e.preventDefault();
      const isim = mf.isim.value.trim(), mesaj = mf.mesaj.value.trim();
      if (!isim || !mesaj) { mok.textContent = "Lütfen adınızı ve mesajınızı yazın."; mok.hidden = false; return; }
      mbtn.disabled = true; mok.hidden = false; mok.textContent = "Gönderiliyor...";
      try {
        const k = ek.mesajGonder ? await ek.mesajGonder({ isim, mesaj }) : { isim, mesaj, zaman: new Date().toISOString() };
        kok.querySelector(".mesajlar").insertAdjacentHTML("afterbegin", mesajKart(k || { isim, mesaj }));
        mf.reset(); mok.textContent = "Teşekkürler, mesajınız deftere eklendi.";
      } catch { mok.textContent = "Mesaj gönderilemedi, tekrar deneyin."; }
      finally { mbtn.disabled = false; }
    });
    sayac();
    const f = kok.querySelector("form.rsvp");
    const ok = f.querySelector(".rsvp-ok");
    const btn = f.querySelector("button");
    f.addEventListener("submit", async e => {
      e.preventDefault();
      const isim = f.isim.value.trim();
      if (!isim) { ok.textContent = "Lütfen adınızı yazın."; ok.hidden = false; return; }
      const durum = f.durum.value;
      const veri = { isim, kisi: durum === "Katılacak" ? Number(f.kisi.value) : 0, durum };
      btn.disabled = true; ok.hidden = false; ok.textContent = "Gönderiliyor...";
      try {
        await yanitGonder(veri);
        f.isim.value = "";
        ok.textContent = durum === "Katılacak" ? "Teşekkürler, sizi aramızda görmek için sabırsızlanıyoruz." : "Yanıtınız için teşekkürler.";
        if (d.slug && d.slug !== "ornek" && !f.querySelector(".lv-oner")) f.insertAdjacentHTML("beforeend",
          `<a class="lv-oner" href="/?ref=d-${esc(d.slug)}" target="_blank" rel="noopener" style="display:block;margin-top:5cqw;padding:4cqw;border:1px dashed var(--line2);color:var(--soft);font-size:3.4cqw;text-decoration:none;line-height:1.5">Bu davetiyeyi beğendiniz mi? Siz de kendi dijital davetiyenizi <b style="color:var(--acc)">LaVie Davetiye</b> ile oluşturun →</a>`);
      } catch (err) {
        ok.textContent = "Yanıt gönderilemedi. İnternet bağlantınızı kontrol edip tekrar deneyin.";
      } finally { btn.disabled = false; }
    });
  }

  window.Lavie = { TASARIMLAR, TURLER, UST, YAZILAR, KATILIM_NOTLARI, esc, ciz, uzunTarih };
})();
