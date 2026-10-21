/* Study screens: flashcards (Leitner boxes), stage quizzes, exams, the
   wrong-answer book and progress. Data comes in as arguments so the screens
   can be tested with fixtures; app.js loads it. */

import { pick, t } from './i18n.js';
import { el } from './content.js';
import { displayName } from './names.js';
import * as prefs from './prefs.js';
import { review, dueCards } from './leitner.js';
import { drawExam, scoreItem, scoreExam, itemId, kindOf } from './exam.js';
import { cardsFor, questionsFor } from './quiz.js';

const page = (title, ...kids) => el('div', { class: 'page page-tool' }, el('p', { class: 'kicker' }, el('a', { href: '#/tools' }, t('tools'))), el('h1', {}, title), ...kids);
const today = () => { const d = new Date(); return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`; };

/* ---------- One question ----------
   Immediate mode reveals the answer and calls onDone(correct, response) once.
   Deferred mode (exams) only records: onDone is called on every change. */
export function renderItem(item, lang, onDone, { deferred = false } = {}) {
  const li = el('div', { class: 'quiz-q', 'data-id': itemId(item), 'data-answer': kindOf(item) === 'mc' ? String(item.answer) : null },
    el('p', { class: 'quiz-text' }, pick(item.q, lang)),
    item.img ? el('img', { class: 'quiz-img', src: item.img, alt: '' }) : null);
  const why = el('p', { class: 'quiz-why', hidden: true }, pick(item.why, lang));
  if (kindOf(item) === 'match') li.append(matchBody(item, lang, onDone, deferred, why), why);
  else li.append(mcBody(item, lang, onDone, deferred, why), why);
  return li;
}

function mcBody(item, lang, onDone, deferred, why) {
  let done = false;
  const opts = el('div', { class: 'quiz-opts' }, item.options.map((o, oi) => el('button', {
    type: 'button', class: 'quiz-opt',
    onclick: e => {
      if (deferred) {
        for (const b of opts.children) b.classList.remove('is-chosen');
        e.currentTarget.classList.add('is-chosen');
        onDone?.(scoreItem(item, oi), oi);
        return;
      }
      if (done) return;
      done = true;
      [...opts.children].forEach((b, k) => { b.disabled = true; if (k === item.answer) b.classList.add('is-right'); });
      if (oi !== item.answer) e.currentTarget.classList.add('is-wrong');
      why.hidden = false;
      onDone?.(scoreItem(item, oi), oi);
    },
  }, pick(o, lang))));
  return opts;
}

// Right-hand column in a fixed scrambled order (rotate by one) so it never
// lines up with the left by accident.
function matchBody(item, lang, onDone, deferred, why) {
  const n = item.pairs.length;
  const order = item.pairs.map((_, i) => (i + 1) % n);
  const chosen = new Array(n).fill(undefined);
  let active = null;
  const lefts = item.pairs.map((p, i) => el('button', { type: 'button', onclick: () => pickLeft(i) }, pick(p.left, lang)));
  const rights = order.map(ri => el('button', { type: 'button', 'data-i': String(ri), onclick: () => pickRight(ri) }, pick(item.pairs[ri].right, lang)));
  const paint = () => {
    lefts.forEach((b, i) => { b.dataset.pair = chosen[i] === undefined ? '' : String(i % 5); b.classList.toggle('is-active', active === i); });
    rights.forEach(b => { const li = chosen.indexOf(Number(b.dataset.i)); b.dataset.pair = li < 0 ? '' : String(li % 5); });
  };
  const pickLeft = i => { active = i; paint(); };
  const pickRight = ri => {
    if (active === null) return;
    const prev = chosen.indexOf(ri);
    if (prev >= 0) chosen[prev] = undefined;
    chosen[active] = ri;
    active = chosen.findIndex(c => c === undefined);
    if (active < 0) active = null;
    paint();
    if (deferred) onDone?.(scoreItem(item, chosen), [...chosen]);
  };
  const submit = el('button', { type: 'button', class: 'button match-submit', onclick: () => {
    const ok = scoreItem(item, chosen);
    lefts.forEach((b, i) => b.classList.add(chosen[i] === i ? 'is-right' : 'is-wrong'));
    [...lefts, ...rights, submit].forEach(b => { b.disabled = true; });
    why.hidden = false;
    onDone?.(ok, [...chosen]);
  } }, t('submit'));
  return el('div', { class: 'match' }, el('div', { class: 'match-cols' },
    el('div', { class: 'match-left' }, lefts), el('div', { class: 'match-right' }, rights)), deferred ? null : submit);
}

/* ---------- Flashcards ---------- */
export function cardsPage(lang, { terms, stages, stage }) {
  const all = stage ? cardsFor(terms, stages, stage) : terms;
  const byId = new Map(all.map(x => [x.id, x]));
  const host = el('div', { class: 'fc-wrap' });
  const next = () => {
    const due = dueCards(prefs.get().cards, all.map(x => x.id), today());
    if (!due.length) { host.replaceChildren(el('p', { class: 'muted fc-done' }, t('cardsDone', null, lang))); return; }
    const x = byId.get(due[0]);
    const card = el('button', { type: 'button', class: 'flashcard', onclick: () => card.classList.toggle('is-flipped') },
      el('span', { class: 'fc-front' }, displayName(x.name, lang)), el('span', { class: 'fc-back' }, pick(x.short, lang)));
    const answer = ok => { prefs.setCards(review(prefs.get().cards, x.id, ok, today())); next(); };
    host.replaceChildren(el('p', { class: 'muted' }, t('cardsDue', { n: due.length }, lang)), card,
      el('div', { class: 'fc-nav' },
        el('button', { type: 'button', class: 'button button-quiet fc-no', onclick: () => answer(false) }, t('cardNo', null, lang)),
        el('button', { type: 'button', class: 'button fc-yes', onclick: () => answer(true) }, t('cardYes', null, lang))));
  };
  next();
  const picker = el('div', { class: 'chips' }, [0, ...stages.map(s => s.n)].map(n =>
    el('a', { class: n === stage ? 'chip on' : 'chip', href: n ? `#/tools/cards/${n}` : '#/tools/cards' }, n ? t('stageN', { n }, lang) : t('allStages', null, lang))));
  return page(t('flashcards', null, lang), picker, host);
}

/* ---------- Stage quiz ---------- */
export function quizPage(lang, { items, index, stage }) {
  if (!stage) {
    const best = prefs.get().quiz;
    return page(t('quiz', null, lang), el('ul', { class: 'tool-list' }, index.stages.map(st => {
      const qs = questionsFor(items, st.n);
      if (!qs.length) return null;
      return el('li', {}, el('a', { href: `#/tools/quiz/${st.n}` }, `${t('stageN', { n: st.n }, lang)} · ${pick(st.title, lang)}`,
        el('span', { class: 'muted' }, best[st.n] != null ? ` — ${best[st.n]}/${qs.length}` : ` — ${qs.length}`)));
    })));
  }
  const qs = questionsFor(items, stage);
  const got = new Array(qs.length);
  const result = el('div', { class: 'quiz-result', 'aria-live': 'polite' });
  const list = el('ol', { class: 'quiz-list' }, qs.map((q, i) => el('li', {}, renderItem(q, lang, ok => {
    got[i] = ok;
    if (!ok) prefs.addWrong([itemId(q)]);
    if (got.every(x => x !== undefined)) {
      const correct = got.filter(Boolean).length;
      prefs.setQuizBest(stage, correct);
      result.replaceChildren(el('p', { class: 'quiz-score' }, `${correct}/${qs.length}`),
        el('a', { class: 'button button-quiet', href: `#/stage/${stage}` }, t('stageN', { n: stage }, lang)));
    }
  }))));
  return page(`${t('quiz', null, lang)} · ${t('stageN', { n: stage }, lang)}`, list, result);
}

/* ---------- Exam ---------- */
export function examPage(lang, { items, seed = Date.now() }) {
  const body = el('div', { class: 'exam' });
  const counts = [...new Set([10, 20, 40].map(n => Math.min(n, items.length)))].filter(n => n > 0);
  const timed = el('input', { type: 'checkbox', class: 'exam-timed' });
  const start = count => {
    const qs = drawExam(items, { count, seed });
    const responses = new Array(qs.length);
    const t0 = Date.now();
    const clock = el('p', { class: 'exam-clock', hidden: !timed.checked }, '0:00');
    const tick = setInterval(() => {
      if (!clock.isConnected) { clearInterval(tick); return; }
      const s = Math.round((Date.now() - t0) / 1000);
      clock.textContent = `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;
    }, 1000);
    const submit = el('button', { type: 'button', class: 'button exam-submit', onclick: () => {
      clearInterval(tick);
      const seconds = Math.round((Date.now() - t0) / 1000);
      const r = scoreExam(qs, responses);
      prefs.addWrong(r.wrongIds);
      prefs.addExam({ date: today(), correct: r.correct, total: r.total, seconds });
      body.replaceChildren(
        el('p', { class: 'exam-score' }, `${r.correct}/${r.total}`),
        el('p', { class: 'muted' }, t('examTime', { m: Math.floor(seconds / 60), s: seconds % 60 }, lang)),
        r.wrongIds.length ? el('a', { class: 'button', href: '#/tools/wrong' }, t('wrongBook', null, lang)) : null,
        el('ol', { class: 'quiz-list' }, qs.map(q => el('li', {}, renderItem(q, lang, null)))));
    } }, t('submit', null, lang));
    body.replaceChildren(clock, el('ol', { class: 'quiz-list' }, qs.map((q, i) =>
      el('li', {}, renderItem(q, lang, (ok, resp) => { responses[i] = resp; }, { deferred: true })))), submit);
  };
  body.append(
    el('p', {}, t('examPick', null, lang)),
    el('div', { class: 'exam-count' }, counts.map(n => el('button', { type: 'button', class: 'button', onclick: () => start(n) }, t('examN', { n }, lang)))),
    el('label', { class: 'exam-timer' }, timed, ' ', t('examTimer', null, lang)));
  if (!counts.length) body.replaceChildren(el('p', { class: 'muted' }, t('noQuestions', null, lang)));
  return page(t('exam', null, lang), body);
}

/* ---------- Wrong-answer book ---------- */
export function wrongPage(lang, { items }) {
  const byId = new Map(items.map(q => [itemId(q), q]));
  const ids = prefs.get().wrong.filter(id => byId.has(id)).reverse();
  if (!ids.length) return page(t('wrongBook', null, lang), el('p', { class: 'muted wrong-empty' }, t('wrongEmpty', null, lang)));
  return page(t('wrongBook', null, lang), el('p', { class: 'muted' }, t('wrongHint', null, lang)),
    el('ol', { class: 'quiz-list' }, ids.map(id => el('li', { class: 'wrong-item' }, renderItem(byId.get(id), lang, ok => { if (ok) prefs.removeWrong(id); })))));
}

/* ---------- Progress ---------- */
export function progressPage(lang, { index, items }) {
  const p = prefs.get();
  const rows = index.stages.map(s => {
    const read = s.chapters.filter(id => p.read[id]).length;
    const qs = questionsFor(items, s.n).length;
    return el('tr', {}, el('td', {}, `${s.n}. ${pick(s.title, lang)}`), el('td', {}, `${read}/${s.chapters.length}`),
      el('td', {}, p.quiz[s.n] != null ? `${p.quiz[s.n]}/${qs}` : '—'));
  });
  const exams = p.exams.slice(-10).reverse();
  return page(t('progress', null, lang),
    el('div', { class: 'table-scroll' }, el('table', { class: 'progress-table' },
      el('thead', {}, el('tr', {}, [t('stage', null, lang), t('pagesRead', null, lang), t('bestQuiz', null, lang)].map(h => el('th', { scope: 'col' }, h)))),
      el('tbody', {}, rows))),
    el('h2', {}, t('examHistory', null, lang)),
    exams.length ? el('ul', { class: 'exam-history' }, exams.map(e => el('li', {}, `${e.date} · ${e.correct}/${e.total} · ${Math.floor(e.seconds / 60)}:${String(e.seconds % 60).padStart(2, '0')}`)))
      : el('p', { class: 'muted' }, '—'),
    el('p', {}, el('a', { href: '#/tools/wrong' }, `${t('wrongBook', null, lang)} (${p.wrong.length})`)));
}
