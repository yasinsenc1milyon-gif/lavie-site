// Shopier'den gelen "yeni sipariş" bildirimi: imzayı doğrular, bekleyen kart ödemelerini eşleştirir.
import { json, uc } from "../../lib/ortak.js";
import { bekleyenleriKontrolEt, imzaDogru } from "../../lib/odeme.js";

export const onRequestPost = uc(async ({ request, env, db }) => {
  const metin = await request.text();
  const t = await db.prepare("SELECT deger FROM ayarlar WHERE anahtar = 'webhook_token'").first();
  if (!t || !(await imzaDogru(metin, request.headers.get("shopier-signature"), t.deger))) return json({ ok: false, hata: "imza" }, 401);
  const olay = request.headers.get("shopier-event") || "";
  if (olay !== "order.created") return json({ ok: true, atlandi: olay });
  const n = await bekleyenleriKontrolEt(env, db);
  return json({ ok: true, eslesen: n });
});
