/* Active ingredients named in chemical control, with their status in Malaysia
   (checked against the Pesticides Board). A banned one is never named without
   saying so. Pure apart from loadPesticides. */

import { displayName } from './names.js';
import { loadData } from './content.js';

const BANNED = { zh: '已禁用', en: 'Banned', ms: 'Diharamkan' };

export function statusLabel(status, lang) {
  return status === 'banned' ? BANNED[lang] ?? BANNED.en : '';
}

export function aiLabel(p, lang) {
  const name = displayName(p.name, lang), tag = statusLabel(p.status, lang);
  if (!tag) return name;
  return lang === 'zh' ? `${name}（${tag}）` : `${name} (${tag})`;
}

let byId = null;
export async function loadPesticides() {
  if (!byId) byId = new Map((await loadData('pesticides')).map(p => [p.id, p]));
  return byId;
}
