/* The identification key screens: one question at a time, the answered
   steps as a trail that can be tapped to answer again, and the result with
   a checklist to confirm it. The route (#/key/0.1.1) holds the answers. */

import { pick, t } from './i18n.js';
import { el } from './content.js';
import { displayName } from './names.js';
import { walk } from './key.js';

export function renderKey(key, { answers, lang, onAnswer, onStep, onRestart, openSheet, pageTitle, sourceLabel }) {
  const r = walk(key, answers);
  const crumbs = r.path.length ? el('ol', { class: 'key-crumbs' }, r.path.map(({ node, choice }, i) =>
    el('li', {}, el('button', { type: 'button', onclick: () => onStep(i) },
      el('span', { class: 'key-crumb-n' }, String(i + 1)),
      el('span', { class: 'key-crumb-text' },
        el('span', { class: 'key-crumb-q' }, pick(key.nodes[node].q, lang)),
        el('span', { class: 'key-crumb-a' }, pick(key.nodes[node].options[choice].label, lang))))))) : null;

  const head = el('header', { class: 'key-head' },
    el('h1', {}, t('identify', null, lang)),
    el('p', { class: 'muted' }, t('keyIntro', null, lang)));

  if (r.result) {
    const res = key.results[r.result];
    return el('div', { class: 'page page-key' }, head, crumbs,
      el('section', { class: 'key-result' },
        el('p', { class: 'kicker' }, t('keyResult', null, lang)),
        el('h2', {}, displayName(res.group, lang)),
        res.order ? el('a', { class: 'button', href: `#/ch/${res.order}` }, [t('openOrder', null, lang), pageTitle(res.order)].filter(Boolean).join(': ')) : null,
        res.check.length ? el('div', { class: 'key-check' },
          el('h3', {}, t('keyCheck', null, lang)),
          el('ul', {}, res.check.map(c => el('li', {}, el('label', {}, el('input', { type: 'checkbox' }), ' ', pick(c, lang)))))) : null,
        res.confused.length ? el('div', { class: 'key-confused' },
          el('h3', {}, t('keyConfused', null, lang)),
          el('ul', {}, res.confused.map(c => el('li', {}, pick(c, lang))))) : null,
        el('aside', { class: 'note note-warn' }, el('p', {}, t('keyDisclaimer', null, lang))),
        el('p', { class: 'block-src' }, `${t('source', null, lang)}: `, res.src.map(sourceLabel).join(' · ')),
        el('button', { type: 'button', class: 'button button-quiet', onclick: onRestart }, t('keyRestart', null, lang))));
  }

  const node = key.nodes[r.node];
  const step = r.path.length;
  return el('div', { class: 'page page-key' }, head, crumbs,
    el('section', { class: 'key-q' },
      el('p', { class: 'kicker' }, t('keyStep', { n: step + 1 }, lang)),
      el('h2', {}, pick(node.q, lang)),
      node.img ? el('img', { class: 'key-img', src: node.img, alt: '', width: 240, height: 120 }) : null,
      el('div', { class: 'key-opts' }, node.options.map((o, i) =>
        el('button', { type: 'button', class: o.result === 'outside' ? 'key-opt key-opt-none' : 'key-opt', onclick: () => onAnswer(step, i) }, pick(o.label, lang)))),
      el('button', { type: 'button', class: 'key-hint-btn', onclick: () => openSheet(el('div', { class: 'key-hint' }, el('h3', {}, t('keyCantTell', null, lang)), el('p', {}, pick(node.hint, lang)))) }, t('keyCantTell', null, lang))),
    step ? el('button', { type: 'button', class: 'button button-quiet', onclick: onRestart }, t('keyRestart', null, lang)) : null);
}
