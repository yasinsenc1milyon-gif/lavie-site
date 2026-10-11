// Lavie müzik çalar: Pixabay lisanslı gerçek kayıtlar (Leberch). Yumuşak giriş/çıkış, döngü.
(function () {
  const PARCALAR = [
    { id: "piyano", ad: "Düğün Piyanosu", dosya: "muzik/dugun-piyanosu.mp3" },
    { id: "kirlar", ad: "Yeşil Kırlar", dosya: "muzik/yesil-kirlar.mp3" }
  ];
  const ESKI = { kutu: "piyano" }; // eski kayıtlar için
  const bul = id => PARCALAR.find(p => p.id === (ESKI[id] || id)) || null;

  let ses = null, aktif = null, sonId = null, zaman = null, acik = false;

  // iOS'ta ses düzeyi değiştirilemez; adım sayısıyla sınırlı solma her cihazda biter
  function solma(hedef, sure, bitince) {
    clearInterval(zaman);
    const adim = 40, n = Math.max(1, Math.round(sure / adim)), bas = ses.volume;
    let i = 0;
    zaman = setInterval(() => {
      i++;
      try { ses.volume = Math.min(1, Math.max(0, bas + (hedef - bas) * i / n)); } catch {}
      if (i >= n) { clearInterval(zaman); bitince && bitince(); }
    }, adim);
  }

  function baslat(id) {
    const p = bul(id || sonId || "piyano");
    if (!p) return;
    sonId = p.id;
    if (!ses) { ses = new Audio(); ses.loop = true; ses.preload = "auto"; }
    if (aktif !== p.id) { ses.src = p.dosya; aktif = p.id; }
    ses.volume = 0; acik = true;
    const s = ses.play();
    if (s && s.catch) s.catch(() => { acik = false; });
    solma(.85, 1500);
  }
  function durdur() {
    if (!ses || !acik) return;
    acik = false;
    solma(0, 400, () => { if (!acik) ses.pause(); });
  }
  const calisiyor = () => acik;
  document.addEventListener("visibilitychange", () => { if (document.hidden) durdur(); });

  window.LavieMuzik = { PARCALAR, bul, baslat, durdur, calisiyor, calan: () => (calisiyor() ? aktif : null) };
})();
