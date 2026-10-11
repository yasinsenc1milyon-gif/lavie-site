// Eski /d.html?c=... linkleri için aynı sayfa
import { davetiyeSayfasi } from "../lib/onizleme.js";

export const onRequestGet = (ctx) => davetiyeSayfasi(ctx);
