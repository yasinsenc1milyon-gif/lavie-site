// Ana sayfada gösterilen, yönetimde onaylanmış gerçek çift yorumları
import { json, uc } from "../../lib/ortak.js";

export const onRequestGet = uc(async ({ db }) => {
  const { results } = await db.prepare("SELECT ad, tur, puan, yorum, zaman FROM yorumlar WHERE onay = 1 ORDER BY zaman DESC LIMIT 12").all();
  return json({ ok: true, yorumlar: results || [] });
});
