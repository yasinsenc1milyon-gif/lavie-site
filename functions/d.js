// /d?c=... davetiye sayfası (link önizlemesiyle)
import { davetiyeSayfasi } from "../lib/onizleme.js";

export const onRequestGet = (ctx) => davetiyeSayfasi(ctx);
