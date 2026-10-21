/* Names that differ between mainland China and Taiwan.

   A name is {zh, zhTw?, en, ms}. In Chinese both are shown, each labelled,
   when they differ: 蝽（大陆）／椿象（台湾）. Pure. */

import { pick } from './i18n.js';

export function displayName(name, lang) {
  const main = pick(name, lang);
  if (lang !== 'zh' || !name?.zhTw || name.zhTw === name.zh) return main;
  return `${name.zh}（大陆）／${name.zhTw}（台湾）`;
}

export function allNames(name) {
  return [...new Set(['zh', 'zhTw', 'en', 'ms'].map(k => name?.[k]).filter(Boolean))];
}
