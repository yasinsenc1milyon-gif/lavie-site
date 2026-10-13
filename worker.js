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
import * as ziyaret from "./functions/api/ziyaret.js";
import { gunAnahtari } from "./functions/api/ziyaret.js";
import { veritabani } from "./lib/ortak.js";
import { davetiyeSayfasi } from "./lib/onizleme.js";
import { indexNowGonder } from "./lib/indexnow.js";

const ROTALAR = {
  "/api/cift": cift, "/api/yanit": yanit, "/api/mesaj": mesaj, "/api/panel": panel,
  "/api/siparis": siparis, "/api/yonetim": yonetim, "/api/yorumlar": yorumlar, "/api/durum": durum, "/api/istatistik": istatistik, "/api/odeme": odeme, "/api/odeme/bildirim": odemeBildirim, "/api/ziyaret": ziyaret,
  "/d": { onRequestGet: davetiyeSayfasi }, "/d.html": { onRequestGet: davetiyeSayfasi }
};

// Google Search Console doğrulama dosyası (yönlendirmesiz, birebir içerik)
const GOOGLE_DOGRULAMA = "google26fc845d62d4047b.html";

export default {
  async fetch(request, env, ctx) {
    const yol = new URL(request.url).pathname.replace(/\/+$/, "") || "/";
    if (yol === "/" + GOOGLE_DOGRULAMA) return new Response("google-site-verification: " + GOOGLE_DOGRULAMA, { headers: { "content-type": "text/html; charset=utf-8" } });
    // Kısa örnek linki: /o/Ferhat-ve-Yasin → isimlerle örnek davetiye
    if (yol.startsWith("/o/")) {
      let ad = ""; try { ad = decodeURIComponent(yol.slice(3)); } catch {}
      const [g, d] = ad.replace(/_/g, " ").split("-ve-");
      const q = new URLSearchParams({ c: "ornek" });
      if (g && d) { q.set("gelin", g.trim().slice(0, 20)); q.set("damat", d.trim().slice(0, 20)); }
      const gelen = new URL(request.url).searchParams;
      for (const k of ["t", "tur", "ref"]) if (gelen.get(k)) q.set(k, gelen.get(k));
      return Response.redirect(new URL("/d?" + q.toString(), request.url).toString(), 302);
    }
    const mod = ROTALAR[yol];
    if (!mod) return env.ASSETS.fetch(request);
    const yontem = request.method.charAt(0) + request.method.slice(1).toLowerCase();
    const h = mod["onRequest" + yontem] || mod.onRequest;
    if (!h) return new Response(JSON.stringify({ ok: false, hata: "yontem" }), { status: 405, headers: { "content-type": "application/json; charset=utf-8" } });
    return h({ request, env, params: {}, waitUntil: p => ctx.waitUntil(p), next: () => env.ASSETS.fetch(request) });
  },
  // Haftalık: arama motorlarına güncel sayfaları bildir
  async scheduled(event, env, ctx) {
    // 400 günden eski ziyaret sayılarını temizle
    ctx.waitUntil(veritabani(env).then(db => db.prepare("DELETE FROM ziyaretler WHERE gun < ?").bind(gunAnahtari(Date.now() - 400 * 864e5)).run()).catch(e => console.error("temizlik", e && e.message)));
    ctx.waitUntil(indexNowGonder(env, env.SITE_ADRESI || "https://www.laviedavetiye.workers.dev").then(r => console.log("indexnow", JSON.stringify(r))));
  }
};
