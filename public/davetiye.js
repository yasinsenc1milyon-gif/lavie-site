// Lavie davetiye çizici: vitrin, canlı davetiye ve önizleme aynı kodu kullanır.
(function () {
  const esc = s => String(s == null ? "" : s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

  const LEAF = `<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><path d="M10 10 Q90 60 170 170" fill="none" stroke="currentColor" stroke-width="1.6"/><g fill="currentColor" opacity=".5">${[.14,.28,.42,.56,.7,.84].map((t,i)=>{const x=10+160*t,y=10+160*t*t*.9+60*t*(1-t);return `<ellipse cx="${x+13}" cy="${y-9}" rx="13" ry="5" transform="rotate(${-30-i*4} ${x+13} ${y-9})"/><ellipse cx="${x-8}" cy="${y+13}" rx="13" ry="5" transform="rotate(${60+i*4} ${x-8} ${y+13})"/>`}).join("")}</g></svg>`;
  const TILE = `url("data:image/svg+xml,${encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" fill="#2a4c9a"/><circle cx="20" cy="20" r="11" fill="none" stroke="#fbfaf6" stroke-width="2"/><path d="M20 4 L24 16 L36 20 L24 24 L20 36 L16 24 L4 20 L16 16Z" fill="#fbfaf6"/><circle cx="20" cy="20" r="3" fill="#2a4c9a"/><circle cx="0" cy="0" r="5" fill="#fbfaf6"/><circle cx="40" cy="0" r="5" fill="#fbfaf6"/><circle cx="0" cy="40" r="5" fill="#fbfaf6"/><circle cx="40" cy="40" r="5" fill="#fbfaf6"/></svg>')}")`;
  const stars = () => Array.from({ length: 18 }, (_, i) => `<i class="deco star" style="left:${(i*53)%96+2}%;top:${(i*37)%92+3}%;opacity:${.3+(i%4)*.15}"></i>`).join("");

  const TASARIMLAR = [
    { id: "zeytin", ad: "Zeytin Dalı", mini: ["#f1f1e8", "#34402a", "Pinyon Script"], hero: () => `<div class="deco leaf a">${LEAF}</div><div class="deco leaf b">${LEAF}</div>` },
    { id: "gece", ad: "Gece Mavisi", mini: ["#141a2e", "#d1ad6b", "Italiana"], hero: () => `<div class="deco frame"></div>${stars()}` },
    { id: "gul", ad: "Gül Kurusu", mini: ["#f3e6e3", "#a8676b", "Great Vibes"], hero: () => `<div class="deco arch"></div>` },
    { id: "mono", ad: "Siyah Beyaz", mini: ["#141414", "#fbfbfa", "Bodoni Moda"], hero: () => `<div class="deco hbar" style="top:12cqw"></div><div class="deco hbar" style="bottom:12cqw"></div>` },
    { id: "ege", ad: "Ege", mini: ["#fbfaf6", "#2a4c9a", "Marcellus"], hero: () => `<div class="deco tile top" style="background-image:${TILE}"></div><div class="deco tile bot" style="background-image:${TILE}"></div>` }
  ];
  const TURLER = ["Düğün", "Nişan", "Kına", "Söz"];
  const YAZILAR = [["", "Tasarımın yazısı", null], ["el", "El yazısı", "Great Vibes"], ["zarif", "Zarif", "Pinyon Script"], ["klasik", "Klasik", "Cormorant Garamond"], ["modern", "Modern", "Italiana"], ["bodoni", "Moda", "Bodoni Moda"], ["sade", "Sade", "Marcellus"]];
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
      ${galeri(ek)}
      <section><h3>Katılım</h3>
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
      <footer>${gelin} &amp; ${damat}<small>Lavie ile hazırlandı</small></footer>
    </div>`;
  }

  function galeri(ek) {
    const f = ek.fotolar || [];
    if (f.length) return `<section><h3>Anılarımız</h3><div class="gal">${f.map((u, i) => `<button type="button" class="gal-i" data-i="${i}" aria-label="Fotoğraf ${i + 1}"><img src="${esc(u)}" alt="" loading="lazy"></button>`).join("")}</div></section>`;
    if (ek.ornekGaleri) return `<section><h3>Anılarımız</h3><div class="gal">${[1, 2, 3, 4].map(i => `<div class="gal-i gal-bos"><span>Fotoğraf ${i}</span></div>`).join("")}</div><p style="color:var(--soft);font-size:3.4cqw;margin-top:3cqw">Fotoğraflarınızı sipariş sonrası panelinizden eklersiniz.</p></section>`;
    return "";
  }
  function mesajKart(m) {
    const z = m.zaman ? new Date(m.zaman).toLocaleDateString("tr-TR", { day: "numeric", month: "long" }) : "";
    return `<figure class="mk"><blockquote>${esc(m.mesaj)}</blockquote><figcaption>${esc(m.isim)}${z ? ` · ${esc(z)}` : ""}</figcaption></figure>`;
  }
  function buyut(kok, fotolar, i) {
    const o = document.createElement("div");
    o.className = "lb"; o.setAttribute("role", "dialog");
    o.innerHTML = `<img alt=""><button type="button" class="lb-x" aria-label="Kapat">×</button>`;
    const img = o.querySelector("img");
    const goster = () => { img.src = fotolar[i]; };
    goster();
    o.addEventListener("click", e => {
      if (e.target.classList.contains("lb-x") || e.target === o) return o.remove();
      i = (i + (e.clientX > innerWidth / 2 ? 1 : -1) + fotolar.length) % fotolar.length; goster();
    });
    document.body.appendChild(o);
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
  // ek: { fotolar, mesajlar, ornekGaleri, mesajGonder: async ({isim,mesaj}) => kayıt }
  function ciz(kok, d, yanitGonder, ek) {
    ek = ek || {};
    kok.innerHTML = html(d, ek);
    kok.querySelectorAll(".gal-i[data-i]").forEach(b => b.addEventListener("click", () => buyut(kok, ek.fotolar, Number(b.dataset.i))));
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
      } catch (err) {
        ok.textContent = "Yanıt gönderilemedi. İnternet bağlantınızı kontrol edip tekrar deneyin.";
      } finally { btn.disabled = false; }
    });
  }

  window.Lavie = { TASARIMLAR, TURLER, UST, YAZILAR, esc, ciz, uzunTarih };
})();
