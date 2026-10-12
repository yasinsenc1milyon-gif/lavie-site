// Lavie · Cloudflare Worker girişi (workers.dev)
// Statik dosyalar (public/) doğrudan Cloudflare tarafından sunulur; yalnızca /api/*, /d ve /d.html bu koda gelir.
import * as cift from "./functions/api/cift.js";
import * as yanit from "./functions/api/yanit.js";
import * as mesaj from "./functions/api/mesaj.js";
import * as panel from "./functions/api/panel.js";
import * as siparis from "./functions/api/siparis.js";
import * as yonetim from "./functions/api/yonetim.js";
import * as yorumlar from "./functions/api/yorumlar.js";
import * as durum from "./functions/api/durum.js";
import * as istatistik from "./functions/api/istatistik.js";
import * as odeme from "./functions/api/odeme.js";
import * as odemeBildirim from "./functions/api/odeme-bildirim.js";
import { davetiyeSayfasi } from "./lib/onizleme.js";
import { indexNowGonder } from "./lib/indexnow.js";

const ROTALAR = {
  "/api/cift": cift, "/api/yanit": yanit, "/api/mesaj": mesaj, "/api/panel": panel,
  "/api/siparis": siparis, "/api/yonetim": yonetim, "/api/yorumlar": yorumlar, "/api/durum": durum, "/api/istatistik": istatistik, "/api/odeme": odeme, "/api/odeme/bildirim": odemeBildirim,
  "/d": { onRequestGet: davetiyeSayfasi }, "/d.html": { onRequestGet: davetiyeSayfasi }
};

// Google Search Console doğrulama dosyası (yönlendirmesiz, birebir içerik)
const GOOGLE_DOGRULAMA = "google26fc845d62d4047b.html";

export default {
  async fetch(request, env, ctx) {
    const yol = new URL(request.url).pathname.replace(/\/+$/, "") || "/";
    if (yol === "/" + GOOGLE_DOGRULAMA) return new Response("google-site-verification: " + GOOGLE_DOGRULAMA, { headers: { "content-type": "text/html; charset=utf-8" } });
    const mod = ROTALAR[yol];
    if (!mod) return env.ASSETS.fetch(request);
    const yontem = request.method.charAt(0) + request.method.slice(1).toLowerCase();
    const h = mod["onRequest" + yontem] || mod.onRequest;
    if (!h) return new Response(JSON.stringify({ ok: false, hata: "yontem" }), { status: 405, headers: { "content-type": "application/json; charset=utf-8" } });
    return h({ request, env, params: {}, waitUntil: p => ctx.waitUntil(p), next: () => env.ASSETS.fetch(request) });
  },
  // Haftalık: arama motorlarına güncel sayfaları bildir
  async scheduled(event, env, ctx) {
    ctx.waitUntil(indexNowGonder(env, env.SITE_ADRESI || "https://www.laviedavetiye.workers.dev").then(r => console.log("indexnow", JSON.stringify(r))));
  }
};
