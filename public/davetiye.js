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
      <section class="album"><h3>Anı Albümü</h3>
        <p style="color:var(--soft);margin-bottom:5cqw">Düğünümüzde çektiğiniz fotoğraf ve videoları bizimle paylaşın. Yüklediklerinizi yalnızca biz görürüz.</p>
        <form class="album-f">
          <input name="isim" placeholder="Adınız (isteğe bağlı)" aria-label="Adınız" maxlength="60">
          <label class="ibtn solid album-sec">Fotoğraf veya video seç<input type="file" accept="image/*,video/*" multiple hidden></label>
          <div class="album-bar" hidden><span></span></div>
          <div class="rsvp-ok album-durum" hidden></div>
        </form>
      </section>
      <footer>${gelin} &amp; ${damat}<small>Lavie ile hazırlandı</small></footer>
    </div>`;
  }

  function mesajKart(m) {
    const z = m.zaman ? new Date(m.zaman).toLocaleDateString("tr-TR", { day: "numeric", month: "long" }) : "";
    return `<figure class="mk"><blockquote>${esc(m.mesaj)}</blockquote><figcaption>${esc(m.isim)}${z ? ` · ${esc(z)}` : ""}</figcaption></figure>`;
  }
  // Anı albümü: fotoğrafı telefonda küçültür, dosyayı 4 MB'lık parçalarla yükler
  const UZANTI = { mov: "video/quicktime", mp4: "video/mp4", m4v: "video/mp4", webm: "video/webm", "3gp": "video/3gpp", jpg: "image/jpeg", jpeg: "image/jpeg", png: "image/png", webp: "image/webp" };
  function mimeBul(f) { return (f.type || UZANTI[(f.name.split(".").pop() || "").toLowerCase()] || "").toLowerCase(); }
  async function kucult(dosya) {
    const url = URL.createObjectURL(dosya);
    try {
      const img = await new Promise((ok, no) => { const i = new Image(); i.onload = () => ok(i); i.onerror = no; i.src = url; });
      const o = Math.min(1, 2000 / Math.max(img.naturalWidth, img.naturalHeight));
      const cv = document.createElement("canvas"); cv.width = Math.round(img.naturalWidth * o); cv.height = Math.round(img.naturalHeight * o);
      cv.getContext("2d").drawImage(img, 0, 0, cv.width, cv.height);
      return await new Promise(r => cv.toBlob(r, "image/jpeg", .86));
    } finally { URL.revokeObjectURL(url); }
  }
  function albumYukleyici(API, slug) {
    const postJ = async b => { const r = await fetch(API + "/album", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ c: slug, ...b }) }); const j = await r.json(); if (!j.ok) throw new Error(j.hata || "hata"); return j; };
    return async (dosya, isim, ilerleme) => {
      let mime = mimeBul(dosya), tur = mime.startsWith("video/") ? "video" : "foto", veri = dosya;
      if (tur === "foto") { try { veri = await kucult(dosya); mime = "image/jpeg"; } catch { throw new Error("tur"); } }
      const b = await postJ({ islem: "baslat", tur, mime, boyut: veri.size, isim });
      for (let i = 0; i < b.parca; i++) {
        const parca = veri.slice(i * b.parcaBoyutu, (i + 1) * b.parcaBoyutu);
        let deneme = 0;
        while (true) {
          try {
            const r = await fetch(`${API}/album?islem=parca&c=${encodeURIComponent(slug)}&id=${b.id}&i=${i}`, { method: "POST", headers: { "content-type": "application/octet-stream" }, body: parca });
            if (!(await r.json()).ok) throw new Error("parca");
            break;
          } catch (e) { if (++deneme >= 3) throw e; await new Promise(r => setTimeout(r, 1500)); }
        }
        ilerleme && ilerleme((i + 1) / b.parca);
      }
      await postJ({ islem: "bitir", id: b.id });
    };
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
  // ek: { mesajlar, mesajGonder: async ({isim,mesaj}) => kayıt, albumYukle: async (dosya, isim, ilerleme) => void }
  function ciz(kok, d, yanitGonder, ek) {
    ek = ek || {};
    kok.innerHTML = html(d, ek);
    const af = kok.querySelector("form.album-f");
    af.addEventListener("submit", e => e.preventDefault());
    af.querySelector("input[type=file]").addEventListener("change", async e => {
      const dosyalar = [...e.target.files]; e.target.value = "";
      if (!dosyalar.length) return;
      const durum = af.querySelector(".album-durum"), bar = af.querySelector(".album-bar"), dol = bar.querySelector("span"), sec = af.querySelector(".album-sec");
      durum.hidden = false;
      if (!ek.albumYukle) { durum.textContent = "Önizlemede yükleme yapılmaz; davetiyenizde misafirleriniz buradan yükler."; return; }
      sec.style.pointerEvents = "none"; sec.style.opacity = ".6"; bar.hidden = false;
      let basari = 0; const hatalar = [];
      for (let n = 0; n < dosyalar.length; n++) {
        const f = dosyalar[n];
        durum.textContent = `${n + 1}/${dosyalar.length} yükleniyor...`;
        try { await ek.albumYukle(f, af.isim.value.trim(), p => { dol.style.width = Math.round(((n + p) / dosyalar.length) * 100) + "%"; }); basari++; }
        catch (err) { hatalar.push(err.message); }
      }
      bar.hidden = true; dol.style.width = "0"; sec.style.pointerEvents = ""; sec.style.opacity = "";
      const m = { boyut: "100 MB'den büyük videolar yüklenemiyor; daha kısa bir video seçin.", tur: "Bu dosya türü desteklenmiyor.", dolu: "Albüm doldu, yeni dosya eklenemiyor.", ornek: "Bu örnek davetiyede yükleme kapalıdır." };
      durum.textContent = (basari ? `Teşekkürler! ${basari} dosya çiftimize ulaştı. ` : "") + (hatalar.length ? (m[hatalar[0]] || `${hatalar.length} dosya yüklenemedi, bağlantınızı kontrol edip tekrar deneyin.`) : "");
    });
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

  window.Lavie = { albumYukleyici, TASARIMLAR, TURLER, UST, YAZILAR, KATILIM_NOTLARI, esc, ciz, uzunTarih };
})();
