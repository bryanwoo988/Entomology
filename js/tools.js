/* The study tools: glossary, flashcards and self-tests.
   Each export builds one page; app.js routes to them. */

import { pick, t } from './i18n.js';
import { pageId } from './markup.js';
import { el, loadData } from './content.js';
import { scoreQuiz, questionsFor, cardsFor } from './quiz.js';
import * as prefs from './prefs.js';

const cid = pageId;
const page = (title, ...kids) => el('div', { class: 'page page-tool' }, el('p', { class: 'kicker' }, el('a', { href: '#/tools' }, t('tools'))), el('h1', {}, title), ...kids);

const TOOLS = [
  ['glossary', 'glossary'], ['cards', 'flashcards'], ['quiz', 'quiz'],
];

export function toolsIndex(lang) {
  return el('div', { class: 'page' }, el('h1', {}, t('tools', null, lang)),
    el('ul', { class: 'tool-list' }, TOOLS.map(([route, key]) => el('li', {}, el('a', { href: `#/tools/${route}` }, t(key, null, lang))))));
}

/* ---------- Glossary ---------- */
function termRow(term, lang, { showAbbr = false } = {}) {
  return el('li', { class: 'gloss-item', id: `term-${term.id}` },
    el('div', { class: 'gloss-head' },
      el('span', { class: 'gloss-name' }, showAbbr && term.abbr ? term.abbr : pick(term.name, lang)),
      showAbbr && term.abbr ? el('span', { class: 'muted' }, pick(term.name, lang)) : term.abbr ? el('span', { class: 'muted' }, term.abbr) : null,
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
/* ---------- Flashcards ---------- */
export async function flashcards(lang, { stage }) {
  const [terms, index] = await Promise.all([loadData('terms'), loadData('index')]);
  const n = stage || index.stages.find(st => cardsFor(terms, index.stages, st.n).length)?.n || 1;
  const cards = cardsFor(terms, index.stages, n);
  let i = 0;
  const card = el('button', { type: 'button', class: 'flashcard' });
  const counter = el('p', { class: 'muted fc-count' });
  const show = () => {
    const x = cards[i];
    card.classList.remove('is-flipped');
    card.replaceChildren(el('span', { class: 'fc-front' }, pick(x.name, lang)), el('span', { class: 'fc-back' }, pick(x.short, lang)));
    counter.textContent = `${i + 1} / ${cards.length}`;
  };
  card.addEventListener('click', () => card.classList.toggle('is-flipped'));
  const nav = el('div', { class: 'fc-nav' },
    el('button', { type: 'button', class: 'button button-quiet', onclick: () => { i = (i - 1 + cards.length) % cards.length; show(); } }, t('prev', null, lang)),
    el('button', { type: 'button', class: 'button', onclick: () => { i = (i + 1) % cards.length; show(); } }, t('next', null, lang)));
  const chips = el('div', { class: 'stage-chips' }, index.stages.map(st => {
    const has = cardsFor(terms, index.stages, st.n).length > 0;
    return has ? el('a', { class: `chip${st.n === n ? ' is-on' : ''}`, href: `#/tools/cards/${st.n}` }, t('stageN', { n: st.n }, lang)) : null;
  }));
  if (cards.length) show();
  return page(t('flashcards', null, lang), chips, cards.length ? el('div', { class: 'fc-wrap' }, card, counter, nav) : el('p', { class: 'muted' }, '—'));
}

/* ---------- Self-test ---------- */
export async function quizPage(lang, { stage }) {
  const [quiz, index] = await Promise.all([loadData('quiz'), loadData('index')]);
  if (!stage) {
    const best = prefs.get().quiz;
    return page(t('quiz', null, lang), el('ul', { class: 'tool-list' }, index.stages.map(st => {
      const qs = questionsFor(quiz, st.n);
      if (!qs.length) return null;
      return el('li', {}, el('a', { href: `#/tools/quiz/${st.n}` }, `${t('stageN', { n: st.n }, lang)} · ${pick(st.title, lang)}`,
        el('span', { class: 'muted' }, best[st.n] != null ? ` — ${best[st.n]}/${qs.length}` : ` — ${qs.length}`)));
    })));
  }
  const qs = questionsFor(quiz, stage);
  const answers = new Array(qs.length);
  const result = el('div', { class: 'quiz-result', 'aria-live': 'polite' });
  const list = el('ol', { class: 'quiz-list' }, qs.map((q, qi) => {
    const why = el('p', { class: 'quiz-why', hidden: true }, pick(q.why, lang));
    const li = el('li', { class: 'quiz-q', 'data-answer': String(q.answer) }, el('p', { class: 'quiz-text' }, pick(q.q, lang)));
    const opts = el('div', { class: 'quiz-opts' }, q.options.map((o, oi) => el('button', {
      type: 'button', class: 'quiz-opt',
      onclick: e => {
        if (answers[qi] !== undefined) return;
        answers[qi] = oi;
        for (const [k, b] of [...opts.children].entries()) { b.disabled = true; if (k === q.answer) b.classList.add('is-right'); }
        if (oi !== q.answer) e.currentTarget.classList.add('is-wrong');
        why.hidden = false;
        if (answers.filter(a => a !== undefined).length === qs.length) {
          const { correct, total } = scoreQuiz(answers, qs);
          prefs.setQuizBest(stage, correct);
          result.replaceChildren(el('p', { class: 'quiz-score' }, `${correct}/${total}`),
            el('a', { class: 'button button-quiet', href: `#/stage/${stage}` }, t('stageN', { n: stage }, lang)));
        }
      },
    }, pick(o, lang))));
    li.append(opts, why);
    return li;
  }));
  return page(`${t('quiz', null, lang)} · ${t('stageN', { n: stage }, lang)}`, list, result);
}
