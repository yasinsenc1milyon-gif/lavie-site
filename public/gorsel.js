// Lavie paylaşım görseli: seçilen tasarımla 1080x1920 (hikâye/durum boyutu) görsel üretir.
(function () {
  const W = 1080, H = 1920;
  const UST = { "Düğün": "EVLENİYORUZ", "Nişan": "NİŞANLANIYORUZ", "Kına": "KINA GECEMİZE DAVETLİSİNİZ", "Söz": "SÖZ TÖRENİMİZE DAVETLİSİNİZ" };
  const TEMA = {
    zeytin: { bg: ["#f1f1e8"], fg: "#34402a", soft: "#6f775f", acc: "#6b7a4f", fn: "Pinyon Script", fd: "Cormorant Garamond", ad: 150 },
    gece:   { bg: ["#24305a", "#141a2e"], radial: true, fg: "#efe2c4", soft: "#a99c80", acc: "#d1ad6b", fn: "Italiana", fd: "Italiana", ad: 140 },
    gul:    { bg: ["#f3e6e3", "#e5c9c4"], fg: "#5a3a3d", soft: "#8c6a6c", acc: "#a8676b", fn: "Great Vibes", fd: "Cormorant Garamond", ad: 160 },
    mono:   { bg: ["#141414"], fg: "#fbfbfa", soft: "#b8b8b8", acc: "#fbfbfa", fn: "Bodoni Moda", fnStil: "italic ", fd: "Bodoni Moda", ad: 140 },
    ege:    { bg: ["#fbfaf6"], fg: "#1d3263", soft: "#5d6f96", acc: "#2a4c9a", fn: "Marcellus", fd: "Marcellus", ad: 120 }
  };

  function tarihYazi(c) {
    let t = String(c.tarih || "").trim();
    const m = t.match(/^(\d{1,2})[./-](\d{1,2})[./-](\d{4})$/);
    if (m) t = `${m[3]}-${m[2].padStart(2, "0")}-${m[1].padStart(2, "0")}`;
    const d = new Date(t + "T00:00");
    if (isNaN(d)) return { tarih: c.tarih || "", gun: "" };
    return { tarih: d.toLocaleDateString("tr-TR", { day: "numeric", month: "long", year: "numeric" }), gun: d.toLocaleDateString("tr-TR", { weekday: "long" }) };
  }

  // harf aralıklı yazı (tarayıcı letterSpacing desteklemese de çalışır)
  function aralikli(ctx, metin, x, y, aralik) {
    const harfler = [...metin];
    const genislik = harfler.reduce((t, h) => t + ctx.measureText(h).width, 0) + aralik * (harfler.length - 1);
    let cx = x - genislik / 2;
    ctx.textAlign = "left";
    for (const h of harfler) { ctx.fillText(h, cx, y); cx += ctx.measureText(h).width + aralik; }
    ctx.textAlign = "center";
  }
  // yazı sığmazsa küçült
  function sigdir(ctx, metin, font, boyut, maks) {
    let b = boyut;
    do { ctx.font = font.replace("{b}", b); if (ctx.measureText(metin).width <= maks) break; b -= 4; } while (b > 30);
    return b;
  }

  function dal(ctx, renk, ox, oy, olcek, aci) {
    ctx.save(); ctx.translate(ox, oy); ctx.rotate(aci); ctx.scale(olcek, olcek);
    ctx.strokeStyle = renk; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(10, 10); ctx.quadraticCurveTo(90, 60, 170, 170); ctx.stroke();
    ctx.fillStyle = renk; ctx.globalAlpha = .5;
    [.14, .28, .42, .56, .7, .84].forEach((t, i) => {
      const x = 10 + 160 * t, y = 10 + 160 * t * t * .9 + 60 * t * (1 - t);
      [[x + 13, y - 9, -30 - i * 4], [x - 8, y + 13, 60 + i * 4]].forEach(([ex, ey, a]) => {
        ctx.beginPath(); ctx.ellipse(ex, ey, 13, 5, a * Math.PI / 180, 0, Math.PI * 2); ctx.fill();
      });
    });
    ctx.restore();
  }
  function egeSerit(ctx, y, ters) {
    const s = 150;
    for (let x = -s / 2; x < W + s; x += s) {
      ctx.save(); ctx.translate(x + s / 2, y + s / 2); if (ters) ctx.scale(1, -1);
      ctx.fillStyle = "#2a4c9a"; ctx.fillRect(-s / 2, -s / 2, s, s);
      ctx.strokeStyle = "#fbfaf6"; ctx.lineWidth = 6; ctx.beginPath(); ctx.arc(0, 0, s * .28, 0, Math.PI * 2); ctx.stroke();
      ctx.fillStyle = "#fbfaf6"; ctx.beginPath();
      const r1 = s * .4, r2 = s * .1;
      for (let i = 0; i < 8; i++) { const r = i % 2 ? r2 : r1, a = i * Math.PI / 4 - Math.PI / 2; ctx.lineTo(Math.cos(a) * r, Math.sin(a) * r); }
      ctx.closePath(); ctx.fill();
      ctx.fillStyle = "#2a4c9a"; ctx.beginPath(); ctx.arc(0, 0, s * .07, 0, Math.PI * 2); ctx.fill();
      ctx.restore();
    }
  }

  function arkaPlan(ctx, id, t) {
    if (t.radial) {
      const g = ctx.createRadialGradient(W / 2, H * .35, 50, W / 2, H * .35, H * .8);
      g.addColorStop(0, t.bg[0]); g.addColorStop(1, t.bg[1]); ctx.fillStyle = g;
    } else if (t.bg.length > 1) {
      const g = ctx.createLinearGradient(0, 0, 0, H); g.addColorStop(0, t.bg[0]); g.addColorStop(1, t.bg[1]); ctx.fillStyle = g;
    } else ctx.fillStyle = t.bg[0];
    ctx.fillRect(0, 0, W, H);

    ctx.save();
    if (id === "zeytin") { dal(ctx, t.acc, -150, -130, 2.5, 0); dal(ctx, t.acc, W + 210, H + 190, 2.5, Math.PI); }
    if (id === "gece") {
      ctx.strokeStyle = t.acc; ctx.globalAlpha = .6; ctx.lineWidth = 2;
      ctx.strokeRect(54, 54, W - 108, H - 108); ctx.strokeRect(78, 78, W - 156, H - 156);
      ctx.fillStyle = t.acc;
      for (let i = 0; i < 40; i++) { ctx.globalAlpha = .25 + (i % 4) * .12; ctx.beginPath(); ctx.arc(((i * 53) % 96 + 2) / 100 * W, ((i * 37) % 92 + 3) / 100 * H, 3 + (i % 3), 0, Math.PI * 2); ctx.fill(); }
    }
    if (id === "gul") {
      ctx.strokeStyle = t.acc; ctx.globalAlpha = .45; ctx.lineWidth = 2.5;
      const l = 120, r = W - 120, ust = 140, alt = H - 140, rad = (r - l) / 2;
      ctx.beginPath(); ctx.moveTo(l, alt); ctx.lineTo(l, ust + rad); ctx.arc(W / 2, ust + rad, rad, Math.PI, 0); ctx.lineTo(r, alt); ctx.closePath(); ctx.stroke();
    }
    if (id === "mono") { ctx.fillStyle = t.fg; ctx.globalAlpha = .5; ctx.fillRect(100, 150, W - 200, 2); ctx.fillRect(100, H - 152, W - 200, 2); }
    if (id === "ege") { egeSerit(ctx, 0, false); egeSerit(ctx, H - 150, true); }
    ctx.restore();
  }

  async function fontlariYukle(t) {
    if (!document.fonts) return;
    const istek = [`${t.fnStil || ""}100px "${t.fn}"`, `40px "${t.fd}"`, `italic 40px "Cormorant Garamond"`, `40px "Jost"`];
    try { await Promise.race([Promise.all(istek.map(f => document.fonts.load(f))), new Promise(r => setTimeout(r, 4000))]); } catch {}
  }

  async function olustur(c) {
    const id = TEMA[c.tasarim] ? c.tasarim : "zeytin", t = TEMA[id];
    await fontlariYukle(t);
    const cv = document.createElement("canvas"); cv.width = W; cv.height = H;
    const ctx = cv.getContext("2d");
    arkaPlan(ctx, id, t);
    ctx.textAlign = "center"; ctx.textBaseline = "alphabetic";
    const fd = `"${t.fd}", Georgia, serif`, fn = `${t.fnStil || ""}{b}px "${t.fn}", Georgia, serif`;
    const { tarih, gun } = tarihYazi(c);

    ctx.fillStyle = t.soft; ctx.font = `36px ${fd}`;
    aralikli(ctx, UST[c.tur] || UST["Düğün"], W / 2, 610, 14);

    ctx.fillStyle = t.fg;
    const gelin = c.gelin || "Gelin", damat = c.damat || "Damat";
    const b = Math.min(sigdir(ctx, gelin, fn, t.ad, 860), sigdir(ctx, damat, fn, t.ad, 860));
    ctx.font = fn.replace("{b}", b);
    ctx.fillText(gelin, W / 2, 800);
    ctx.fillStyle = t.acc; ctx.font = fn.replace("{b}", Math.round(b * .55)); ctx.fillText("&", W / 2, 910);
    ctx.fillStyle = t.fg; ctx.font = fn.replace("{b}", b); ctx.fillText(damat, W / 2, 1060);

    ctx.fillStyle = t.acc; ctx.globalAlpha = .6; ctx.fillRect(W / 2 - 110, 1130, 220, 2); ctx.globalAlpha = 1;

    ctx.fillStyle = t.fg; ctx.font = `600 50px ${fd}`;
    aralikli(ctx, tarih.toLocaleUpperCase("tr-TR"), W / 2, 1240, 6);
    ctx.fillStyle = t.soft; ctx.font = `40px ${fd}`;
    ctx.fillText([gun, c.saat].filter(Boolean).join(" · "), W / 2, 1305);

    ctx.fillStyle = t.fg; ctx.font = `46px ${fd}`;
    sigdir(ctx, c.mekan || "", `{b}px ${fd}`, 46, 900); ctx.fillText(c.mekan || "", W / 2, 1420);
    ctx.fillStyle = t.soft; sigdir(ctx, c.adres || "", `{b}px ${fd}`, 34, 900); ctx.fillText(c.adres || "", W / 2, 1475);

    if (c.aile) { ctx.fillStyle = t.soft; sigdir(ctx, c.aile, `italic {b}px "Cormorant Garamond", Georgia, serif`, 36, 880); ctx.fillText(c.aile, W / 2, 1570); }

    ctx.fillStyle = t.soft; ctx.font = `28px "Jost", system-ui, sans-serif`;
    aralikli(ctx, "DAVETİYEMİZ İÇİN LİNKE DOKUNUN", W / 2, id === "ege" ? 1700 : id === "zeytin" ? 1650 : 1745, 6);

    return await new Promise(r => cv.toBlob(r, "image/png"));
  }

  // Görseli bir pencerede gösterir: paylaş / kaydet
  async function goster(c) {
    const kap = document.createElement("div");
    kap.setAttribute("role", "dialog");
    kap.style.cssText = "position:fixed;inset:0;z-index:50;background:rgba(20,18,24,.9);display:grid;place-items:center;padding:16px;overflow:auto";
    kap.innerHTML = `<div style="display:grid;gap:12px;justify-items:center;max-width:380px;width:100%;font-family:Jost,system-ui,sans-serif;color:#fff">
      <div style="font-size:.95rem">Görsel hazırlanıyor...</div></div>`;
    document.body.appendChild(kap);
    const kapat = () => kap.remove();
    kap.addEventListener("click", e => { if (e.target === kap) kapat(); });
    let blob;
    try { blob = await olustur(c); } catch { blob = null; }
    if (!blob) { kap.firstElementChild.innerHTML = `<div>Görsel oluşturulamadı.</div><button type="button" style="font:inherit;padding:10px 18px;border-radius:999px;border:0">Kapat</button>`; kap.querySelector("button").onclick = kapat; return; }
    const url = URL.createObjectURL(blob);
    const ad = `${(c.slug || "davetiye")}-davetiye.png`;
    const dosya = new File([blob], ad, { type: "image/png" });
    const paylasilir = !!(navigator.canShare && navigator.canShare({ files: [dosya] }));
    kap.firstElementChild.innerHTML = `
      <img src="${url}" alt="Davetiye görseli" style="width:100%;max-height:70vh;object-fit:contain;border-radius:8px;box-shadow:0 10px 30px rgba(0,0,0,.4)">
      <div style="font-size:.82rem;color:#ddd;text-align:center">${paylasilir ? "Paylaş ile WhatsApp'a veya fotoğraflara kaydedebilirsiniz." : "Görsele basılı tutup kaydedebilir ya da İndir'e basabilirsiniz."}</div>
      <div style="display:flex;gap:8px;flex-wrap:wrap;justify-content:center">
        ${paylasilir ? `<button type="button" data-a="paylas" style="font:inherit;font-weight:500;padding:11px 20px;border-radius:999px;border:0;background:#25d366;color:#0b2b17;cursor:pointer">Paylaş / Kaydet</button>` : ""}
        <a href="${url}" download="${ad}" style="font:inherit;padding:11px 20px;border-radius:999px;background:#fff;color:#2b2a33;text-decoration:none">İndir</a>
        <button type="button" data-a="kapat" style="font:inherit;padding:11px 20px;border-radius:999px;border:1px solid rgba(255,255,255,.5);background:transparent;color:#fff;cursor:pointer">Kapat</button>
      </div>`;
    kap.querySelector('[data-a="kapat"]').onclick = () => { URL.revokeObjectURL(url); kapat(); };
    const p = kap.querySelector('[data-a="paylas"]');
    if (p) p.onclick = async () => { try { await navigator.share({ files: [dosya], title: "Davetiyemiz" }); } catch {} };
  }

  window.LavieGorsel = { olustur, goster };
})();
