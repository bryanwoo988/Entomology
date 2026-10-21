/* Reader preferences and progress.

   Owns storage. Knows nothing about content or routing; applying the
   preferences to the page is applyToDocument(), kept apart so the logic can
   be tested without a DOM. Storage may be missing or throw (private
   browsing, blocked site data): the app then runs on in-memory state and
   simply forgets on reload. */

const KEY = 'bugs.prefs.v1';

export const LANGS = ['zh', 'en', 'ms'];
export const THEMES = ['auto', 'light', 'dark'];
// Each side has its own look; `auto` switches between the two with the phone.
export const LIGHT_THEMES = ['classic', 'paper', 'mint', 'lavender'];
export const DARK_THEMES = ['midnight', 'oled', 'slate', 'grape'];
export const SCALES = [1, 1.15, 1.3, 1.5];

// English is the default so the first screen — shown before anyone has
// chosen — reads for the widest audience. `chosen` tells a first visit
// apart from someone who deliberately picked English.
const DEFAULTS = () => ({
  lang: 'en', theme: 'auto', lightTheme: 'classic', darkTheme: 'midnight', scale: 1, chosen: false,
  read: {}, quiz: {}, lastRoute: '', seenVersion: '',
  cards: {}, wrong: [], exams: [],
});

export const MAX_WRONG = 200;
export const MAX_EXAMS = 50;
const DAY = /^\d{4}-\d{2}-\d{2}$/;
const goodCard = c => isObj(c) && Number.isInteger(c.box) && c.box >= 1 && c.box <= 5 && DAY.test(c.due ?? '');
const goodExam = e => isObj(e) && DAY.test(e.date ?? '') && [e.correct, e.total, e.seconds].every(Number.isFinite) && e.correct >= 0 && e.correct <= e.total;

let state = DEFAULTS();
let store = null;
const listeners = new Set();

function load() {
  try { return JSON.parse(store?.getItem(KEY) || '{}') || {}; } catch { return {}; }
}

function save() {
  try { store?.setItem(KEY, JSON.stringify(state)); } catch { /* not persisted this session */ }
}

const isObj = v => v && typeof v === 'object' && !Array.isArray(v);

// Stored values are checked, not trusted: a corrupted value falls back to the
// default, and an invalid language shows the picker again.
function sanitise(raw) {
  const d = DEFAULTS();
  const lang = LANGS.includes(raw.lang) ? raw.lang : d.lang;
  return {
    lang,
    theme: THEMES.includes(raw.theme) ? raw.theme : d.theme,
    lightTheme: LIGHT_THEMES.includes(raw.lightTheme) ? raw.lightTheme : d.lightTheme,
    darkTheme: DARK_THEMES.includes(raw.darkTheme) ? raw.darkTheme : d.darkTheme,
    scale: SCALES.includes(raw.scale) ? raw.scale : d.scale,
    chosen: raw.chosen === true && LANGS.includes(raw.lang),
    read: isObj(raw.read) ? Object.fromEntries(Object.entries(raw.read).filter(([, v]) => v === true)) : {},
    quiz: isObj(raw.quiz) ? Object.fromEntries(Object.entries(raw.quiz).filter(([, v]) => Number.isFinite(v))) : {},
    lastRoute: typeof raw.lastRoute === 'string' ? raw.lastRoute : '',
    seenVersion: typeof raw.seenVersion === 'string' ? raw.seenVersion : '',
    cards: isObj(raw.cards) ? Object.fromEntries(Object.entries(raw.cards).filter(([, c]) => goodCard(c))) : {},
    wrong: Array.isArray(raw.wrong) ? [...new Set(raw.wrong.filter(x => typeof x === 'string'))].slice(-MAX_WRONG) : [],
    exams: Array.isArray(raw.exams) ? raw.exams.filter(goodExam).slice(-MAX_EXAMS) : [],
  };
}

function change(what) {
  save();
  for (const fn of listeners) fn(what, get());
}

const next = (list, cur) => list[(list.indexOf(cur) + 1) % list.length];

export function init(storage = globalThis.localStorage) {
  store = storage ?? null;
  state = sanitise(load());
  return get();
}

export function get() {
  return { ...state, read: { ...state.read }, quiz: { ...state.quiz }, cards: { ...state.cards }, wrong: [...state.wrong], exams: [...state.exams] };
}

export function setCards(cards) {
  state.cards = Object.fromEntries(Object.entries(cards).filter(([, c]) => goodCard(c)));
  change('cards');
}

// Newest last; a question answered wrong again moves to the end.
export function addWrong(ids) {
  const set = new Set(ids);
  state.wrong = [...state.wrong.filter(x => !set.has(x)), ...set].slice(-MAX_WRONG);
  change('wrong');
}

export function removeWrong(id) {
  state.wrong = state.wrong.filter(x => x !== id);
  change('wrong');
}

export function addExam(result) {
  if (!goodExam(result)) return;
  state.exams = [...state.exams, result].slice(-MAX_EXAMS);
  change('exams');
}

export function subscribe(fn) {
  listeners.add(fn);
  return () => listeners.delete(fn);
}

export function chooseLang(lang) {
  if (!LANGS.includes(lang)) throw new RangeError(`unknown language: ${lang}`);
  state.lang = lang;
  state.chosen = true;
  change('lang');
  return lang;
}

// Cycling is a choice too, so the picker does not come back.
export function cycleLang() {
  return chooseLang(next(LANGS, state.lang));
}

export function cycleTheme() {
  state.theme = next(THEMES, state.theme);
  change('theme');
  return state.theme;
}

export function cycleFontScale() {
  state.scale = next(SCALES, state.scale);
  change('scale');
  return state.scale;
}

// Settings screen: set directly.
export function setTheme(theme) {
  if (!THEMES.includes(theme)) return state.theme;
  state.theme = theme;
  change('theme');
  return state.theme;
}

// Picking a look also shows it: a light look switches a fixed dark mode to light, and back.
export function setLightTheme(name) {
  if (!LIGHT_THEMES.includes(name)) return state.lightTheme;
  state.lightTheme = name;
  if (state.theme === 'dark') state.theme = 'light';
  change('theme');
  return state.lightTheme;
}

export function setDarkTheme(name) {
  if (!DARK_THEMES.includes(name)) return state.darkTheme;
  state.darkTheme = name;
  if (state.theme === 'light') state.theme = 'dark';
  change('theme');
  return state.darkTheme;
}

export function setScale(scale) {
  if (!SCALES.includes(scale)) return state.scale;
  state.scale = scale;
  change('scale');
  return state.scale;
}

export function markRead(chId, on) {
  if (on) state.read[chId] = true;
  else delete state.read[chId];
  change('read');
}

export function setQuizBest(stage, score) {
  if (!(state.quiz[stage] >= score)) state.quiz[stage] = score;
  change('quiz');
}

export function setLastRoute(route) {
  state.lastRoute = String(route);
  save();
}

export function setSeenVersion(v) {
  state.seenVersion = String(v);
  save();
}

/* The stylesheet reads these attributes. `auto` resolves against the OS
   setting here and again whenever it changes (app.js listens). */
export function applyToDocument(doc = document, prefersDark = globalThis.matchMedia?.('(prefers-color-scheme: dark)').matches) {
  const r = doc.documentElement;
  r.lang = state.lang === 'zh' ? 'zh-Hans' : state.lang;
  const side = state.theme === 'auto' ? (prefersDark ? 'dark' : 'light') : state.theme;
  r.dataset.theme = side;
  r.dataset.palette = side === 'dark' ? state.darkTheme : state.lightTheme;
  // The browser bar takes the page colour of the chosen look.
  const bg = doc.defaultView?.getComputedStyle?.(r).getPropertyValue('--bg').trim();
  if (bg) doc.querySelectorAll?.('meta[name="theme-color"]').forEach(m => m.setAttribute('content', bg));
  r.dataset.themePref = state.theme;
  r.style.setProperty('--font-scale', String(state.scale));
  if (state.scale >= 1.3) r.dataset.single = '';
  else delete r.dataset.single;
}
