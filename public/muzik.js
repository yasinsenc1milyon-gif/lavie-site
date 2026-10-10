// Lavie müzik kutusu: tarayıcıda üretilen, telifsiz özgün bir vals ezgisi (Web Audio).
(function () {
  const BPM = 72, VURUS = 60 / BPM;
  const midi = n => 440 * Math.pow(2, (n - 69) / 12);
  // [nota (MIDI), vuruş] — 8 ölçülük, 3/4 özgün ezgi
  const EZGI = [
    [76, 2], [79, 1],          // C
    [81, 1.5], [79, .5], [76, 1], // Am
    [77, 2], [81, 1],          // F
    [79, 2], [74, 1],          // G
    [76, 1], [79, 1], [84, 1], // C
    [83, 1], [81, 2],          // Am
    [81, 1], [79, 1], [77, 1], // F
    [74, 2], [71, 1]           // G
  ];
  const AKOR = [[48, 55, 64], [45, 52, 60], [41, 48, 57], [43, 50, 59]]; // C, Am, F, G
  const OLCU = 3, DONGU = 8 * OLCU;

  let ctx = null, ana = null, zamanlayici = null, basla = 0, siradaki = 0, calisiyor = false;

  function hazirla() {
    if (ctx) return;
    const AC = window.AudioContext || window.webkitAudioContext;
    if (!AC) return;
    ctx = new AC();
    ana = ctx.createGain(); ana.gain.value = 0;
    // hafif yankı
    const gecikme = ctx.createDelay(); gecikme.delayTime.value = .32;
    const geri = ctx.createGain(); geri.gain.value = .32;
    const filtre = ctx.createBiquadFilter(); filtre.type = "lowpass"; filtre.frequency.value = 2400;
    ana.connect(ctx.destination);
    ana.connect(gecikme); gecikme.connect(filtre); filtre.connect(geri); geri.connect(gecikme); filtre.connect(ctx.destination);
  }

  function nota(frekans, t, sure, ses) {
    const kat = [[1, 1], [2, .28], [4.2, .06]];
    kat.forEach(([k, g]) => {
      const o = ctx.createOscillator(), v = ctx.createGain();
      o.type = "sine"; o.frequency.value = frekans * k;
      v.gain.setValueAtTime(0, t);
      v.gain.linearRampToValueAtTime(ses * g, t + .006);
      v.gain.exponentialRampToValueAtTime(.0001, t + Math.max(sure * 1.6, 1.4));
      o.connect(v); v.connect(ana);
      o.start(t); o.stop(t + Math.max(sure * 1.6, 1.4) + .05);
    });
  }

  // döngüdeki bir vuruş aralığını planla
  function planla(bas, son) {
    let b = 0;
    for (const [n, s] of EZGI) {
      for (let tur = Math.floor((bas - b) / DONGU) - 1; tur <= Math.floor((son - b) / DONGU) + 1; tur++) {
        const vurus = b + tur * DONGU;
        if (vurus >= bas && vurus < son) nota(midi(n), basla + vurus * VURUS, s * VURUS, .16);
      }
      b += s;
    }
    for (let v = Math.ceil(bas * 2) / 2; v < son; v += .5) {
      const dongudeki = ((v % DONGU) + DONGU) % DONGU;
      const olcu = Math.floor(dongudeki / OLCU), icinde = dongudeki - olcu * OLCU;
      const [k, b5, u] = AKOR[olcu % 4];
      const sira = [k, b5, u + 12, b5 + 12, u + 12, b5][Math.round(icinde * 2)];
      nota(midi(sira), basla + v * VURUS, .5 * VURUS, icinde === 0 ? .07 : .045);
    }
  }

  function dongu() {
    const simdi = (ctx.currentTime - basla) / VURUS;
    const hedef = simdi + 2;
    if (hedef > siradaki) { planla(siradaki, hedef); siradaki = hedef; }
  }

  function baslat() {
    hazirla();
    if (!ctx || calisiyor) return;
    if (ctx.state === "suspended") ctx.resume();
    calisiyor = true;
    basla = ctx.currentTime + .1; siradaki = 0;
    ana.gain.cancelScheduledValues(ctx.currentTime);
    ana.gain.setValueAtTime(0, ctx.currentTime);
    ana.gain.linearRampToValueAtTime(.9, ctx.currentTime + 2);
    dongu(); zamanlayici = setInterval(dongu, 250);
  }
  function durdur() {
    if (!ctx || !calisiyor) return;
    calisiyor = false; clearInterval(zamanlayici);
    ana.gain.cancelScheduledValues(ctx.currentTime);
    ana.gain.setValueAtTime(ana.gain.value, ctx.currentTime);
    ana.gain.linearRampToValueAtTime(0, ctx.currentTime + .4);
    setTimeout(() => { if (!calisiyor) ctx.suspend(); }, 500);
  }
  document.addEventListener("visibilitychange", () => { if (document.hidden) durdur(); });

  window.LavieMuzik = { baslat, durdur, calisiyor: () => calisiyor };
})();
