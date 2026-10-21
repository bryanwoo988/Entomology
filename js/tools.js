/* The study tools: glossary, flashcards and self-tests.
   Each export builds one page; app.js routes to them. */

import { pick, t } from './i18n.js';
import { pageId } from './markup.js';
import { displayName } from './names.js';
import { el, loadData } from './content.js';
import * as prefs from './prefs.js';

const cid = pageId;
const page = (title, ...kids) => el('div', { class: 'page page-tool' }, el('p', { class: 'kicker' }, el('a', { href: '#/tools' }, t('tools'))), el('h1', {}, title), ...kids);

const TOOLS = [
  ['glossary', 'glossary'], ['cards', 'flashcards'], ['quiz', 'quiz'],
  ['exam', 'exam'], ['wrong', 'wrongBook'], ['progress', 'progress'],
];

export function toolsIndex(lang) {
  return el('div', { class: 'page' }, el('h1', {}, t('tools', null, lang)),
    el('ul', { class: 'tool-list' }, TOOLS.map(([route, key]) => el('li', {}, el('a', { href: `#/tools/${route}` }, t(key, null, lang))))));
}

/* ---------- Glossary ---------- */
function termRow(term, lang, { showAbbr = false } = {}) {
  return el('li', { class: 'gloss-item', id: `term-${term.id}` },
    el('div', { class: 'gloss-head' },
      el('span', { class: 'gloss-name' }, showAbbr && term.abbr ? term.abbr : displayName(term.name, lang)),
      showAbbr && term.abbr ? el('span', { class: 'muted' }, displayName(term.name, lang)) : term.abbr ? el('span', { class: 'muted' }, term.abbr) : null,
      el('a', { class: 'gloss-ch', href: `#/ch/${cid(term.chapter)}` }, t('chapterN', { n: term.chapter }, lang))),
    el('p', {}, pick(term.short, lang)));
}

export async function glossary(lang, { abbrOnly = false } = {}) {
  let terms = await loadData('terms');
  if (abbrOnly) terms = terms.filter(x => x.abbr);
  const key = x => (abbrOnly ? x.abbr : pick(x.name, lang));
  // Chinese has no alphabet order a reader would scan; keep the teaching order there.
  const sorted = [...terms].sort((a, b) => (lang === 'zh' && !abbrOnly ? a.chapter - b.chapter : key(a).localeCompare(key(b), lang)));
  const list = el('ul', { class: 'gloss-list' }, sorted.map(x => termRow(x, lang, { showAbbr: abbrOnly })));
  const filter = el('input', { type: 'search', class: 'field', placeholder: t('search', null, lang), 'aria-label': t('search', null, lang) });
  filter.addEventListener('input', () => {
    const q = filter.value.trim().toLowerCase();
    for (const li of list.children) li.hidden = q && !li.textContent.toLowerCase().includes(q);
  });
  return page(t(abbrOnly ? 'abbr' : 'glossary', null, lang), filter, terms.length ? list : el('p', { class: 'muted' }, '—'));
}

/* ---------- Concept map ---------- */
