/* Content linter. CI fails on any error.

     node tools/lint-content.mjs

   Beyond "every string has all three languages", it enforces the course's
   central promise: a chapter only uses terms that have already been
   taught — in an earlier chapter, or earlier in the same chapter. */
import { readFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { termIds, chapterIds, pageId } from '../js/markup.js';
import { validate as validateKey } from '../js/key.js';

const LANGS = ['zh', 'en', 'ms'];
// Blocks a reader can mark; every one of them names its source (spec §10.4).
const MARKABLE = new Set(['p', 'list', 'keyval', 'table', 'note', 'control']);
const IPM = ['monitor', 'cultural', 'biological', 'chemical'];
export const LICENCES = ['MPOB-permission', 'own', 'CC0', 'CC BY 2.0', 'CC BY 3.0', 'CC BY 4.0', 'CC BY-SA 2.0', 'CC BY-SA 3.0', 'CC BY-SA 4.0'];
const isTri = v => v && typeof v === 'object' && !Array.isArray(v) && LANGS.some(l => l in v);

function walkStrings(v, fn, path = '') {
  if (typeof v === 'string') return fn(v, path);
  if (Array.isArray(v)) return v.forEach((x, i) => walkStrings(x, fn, `${path}[${i}]`));
  if (v && typeof v === 'object') for (const [k, x] of Object.entries(v)) walkStrings(x, fn, path ? `${path}.${k}` : k);
}

function checkTri(v, where, errors, path = '') {
  if (isTri(v)) {
    for (const l of LANGS) if (typeof v[l] !== 'string' || !v[l].trim()) errors.push(`${where} ${path}: missing ${l}`);
    if ('zhTw' in v && (typeof v.zhTw !== 'string' || !v.zhTw.trim())) errors.push(`${where} ${path}: empty zhTw`);
    return;
  }
  if (Array.isArray(v)) v.forEach((x, i) => checkTri(x, where, errors, `${path}[${i}]`));
  else if (v && typeof v === 'object') for (const [k, x] of Object.entries(v)) checkTri(x, where, errors, path ? `${path}.${k}` : k);
}

export function lint(root) {
  const errors = [];
  const read = f => JSON.parse(readFileSync(join(root, 'data', f), 'utf8'));
  const opt = (f, d) => (existsSync(join(root, 'data', f)) ? read(f) : d);
  const index = read('index.json');
  const terms = opt('terms.json', []);
  const sources = new Set(opt('sources.json', []).map(s => s.id));
  const quiz = opt('quiz.json', []);
  const termChapter = new Map(terms.map(t => [t.id, t.chapter]));
  const cid = pageId;
  const stats = { chapters: 0, blocks: 0, terms: terms.length, quiz: quiz.length };

  checkTri(index, 'index.json', errors);
  checkTri(terms, 'terms.json', errors);
  checkTri(quiz, 'quiz.json', errors);
  const pesticides = new Map(opt('pesticides.json', []).map(p => [p.id, p]));
  const photos = opt('photos.json', []);
  const photoIds = new Set(photos.map(p => p.id));
  checkTri([...pesticides.values()], 'pesticides.json', errors);
  checkTri(photos, 'photos.json', errors);
  for (const p of pesticides.values()) {
    if (!['registered', 'banned', 'unknown'].includes(p.status)) errors.push(`pesticide ${p.id}: bad status "${p.status}"`);
    if (!p.src?.length || !/^\d{4}-\d{2}-\d{2}$/.test(p.checked ?? '')) errors.push(`pesticide ${p.id}: needs src and a checked date`);
    for (const s of p.src ?? []) if (!sources.has(s.split(':')[0])) errors.push(`pesticide ${p.id}: unknown source "${s}"`);
  }
  for (const p of photos) {
    if (!LICENCES.includes(p.licence)) errors.push(`photo ${p.id}: licence "${p.licence}" is missing or not allowed`);
    if (!p.author || !p.url) errors.push(`photo ${p.id}: needs author and url`);
    if (!p.file || !existsSync(join(root, p.file))) errors.push(`photo ${p.id}: file ${p.file} not found`);
  }
  if (existsSync(join(root, 'data', 'releases.json'))) checkTri(read('releases.json'), 'releases.json', errors);

  const defined = new Map();      // term → number of defining blocks
  const chapters = [];
  const chapterSet = new Set(index.chapters.map(m => m.id));   // links may point at chapters not yet written
  for (const meta of index.chapters.filter(m => m.ready !== false)) {
    const file = join(root, 'data', `${meta.id}.json`);
    if (!existsSync(file)) { errors.push(`${meta.id}: listed in index.json but ${meta.id}.json is missing`); continue; }
    chapters.push(JSON.parse(readFileSync(file, 'utf8')));
  }

  for (const ch of chapters) {
    stats.chapters++;
    checkTri(ch, ch.id, errors);
    for (const s of ch.sources ?? []) if (!sources.has(s)) errors.push(`${ch.id}: unknown source "${s}"`);
    const own = terms.filter(t => t.chapter === ch.num).map(t => t.id).sort();
    if (JSON.stringify([...(ch.newTerms ?? [])].sort()) !== JSON.stringify(own)) {
      errors.push(`${ch.id} newTerms ${JSON.stringify(ch.newTerms ?? [])} should be ${JSON.stringify(own)}`);
    }
    const seenHere = new Set();   // terms whose defining block has been passed in this chapter
    let ipm = -1;                 // furthest IPM level reached on this page
    let bi = 0;
    for (const sec of ch.sections ?? []) for (const b of sec.blocks ?? []) {
      bi++; stats.blocks++;
      const at = `${ch.id} §${sec.id} block ${bi}`;
      for (const d of b.defines ?? []) {
        defined.set(d, (defined.get(d) ?? 0) + 1);
        if (termChapter.has(d) && termChapter.get(d) !== ch.num) errors.push(`${at}: defines "${d}" but terms.json puts it in ${cid(termChapter.get(d))}`);
      }
      const uses = new Set();
      walkStrings(b, s => termIds(s).forEach(id => uses.add(id)));
      walkStrings(b, s => chapterIds(s).forEach(id => { if (!chapterSet.has(id)) errors.push(`${at}: unknown chapter "${id}"`); }));
      for (const id of uses) {
        if (!termChapter.has(id)) { errors.push(`${at}: unknown term "${id}"`); continue; }
        const tc = termChapter.get(id);
        if (tc > ch.num) errors.push(`${ch.id} uses "${id}" defined in ${cid(tc)} (${at})`);
        else if (tc === ch.num && !seenHere.has(id) && !(b.defines ?? []).includes(id)) errors.push(`${ch.id} uses "${id}" before its defining paragraph (${at})`);
      }
      for (const d of b.defines ?? []) seenHere.add(d);

      for (const s of b.src ?? []) if (!sources.has(s.split(':')[0])) errors.push(`${at}: unknown source "${s}"`);
      if (MARKABLE.has(b.type) && !(b.src ?? []).length) errors.push(`${at}: block has no src`);
      if (b.type === 'control') {
        const lv = IPM.indexOf(b.level);
        if (lv < 0) errors.push(`${at}: control level "${b.level}" unknown`);
        else if (lv < ipm) errors.push(`${at}: ${b.level} after ${IPM[ipm]} breaks IPM order`);
        else ipm = lv;
        for (const id of b.ai ?? []) {
          const p = pesticides.get(id);
          if (!p) errors.push(`${at}: unknown pesticide "${id}"`);
          else if (p.status === 'unknown') errors.push(`${at}: pesticide "${id}" has status unknown`);
        }
        if ((b.ai ?? []).length && b.level !== 'chemical') errors.push(`${at}: active ingredients only in chemical control`);
      }
      if (b.type === 'photo' && !photoIds.has(b.id)) errors.push(`${at}: unknown photo "${b.id}"`);
      if (b.type === 'species') {
        if (!/^[A-Z][a-z]+( \([A-Z][a-z]+\))? [a-z-]+( [a-z-]+)?$/.test(b.sci ?? '')) errors.push(`${at}: species needs sci (Genus species), got "${b.sci ?? ''}"`);
        if (!chapterSet.has(b.order)) errors.push(`${at}: species links unknown order page "${b.order}"`);
        if (!(b.src ?? []).length) errors.push(`${at}: species block has no src`);
      }
      if (b.type === 'table') (b.rows ?? []).forEach((r, i) => {
        if (r.length !== b.headers.length) errors.push(`${ch.id} table row ${i + 1} has ${r.length} cells, header has ${b.headers.length} (${at})`);
      });
      if (b.type === 'figure' && !existsSync(join(root, b.src))) errors.push(`${at}: figure ${b.src} not found`);
      if (b.type === 'widget' && !existsSync(join(root, 'js', 'widgets', `${String(b.id).toLowerCase()}.js`))) errors.push(`${at}: widget ${b.id} has no module`);
    }
  }
  for (const t of terms) {
    const n = defined.get(t.id) ?? 0;
    if (n === 0 && chapters.some(c => c.num === t.chapter)) errors.push(`"${t.id}" is never defined (expected in ${cid(t.chapter)})`);
    if (n > 1) errors.push(`"${t.id}" is defined ${n} times`);
  }

  // The identification key: a valid tree, sourced results, links to order pages
  // (checked once order pages exist, so the key can be written first).
  const key = opt('key.json', null);
  if (key) {
    checkTri(key, 'key.json', errors);
    for (const e of validateKey(key)) errors.push(`key: ${e}`);
    for (const [id, n] of Object.entries(key.nodes ?? {})) if (n.img && !existsSync(join(root, n.img))) errors.push(`key: ${id} image ${n.img} not found`);
    const ordersWritten = index.chapters.some(m => m.kind === 'order');
    for (const [id, r] of Object.entries(key.results ?? {})) {
      if (!(r.src ?? []).length) errors.push(`key result ${id}: no src`);
      for (const s of r.src ?? []) if (!sources.has(s.split(':')[0])) errors.push(`key result ${id}: unknown source "${s}"`);
      if (r.order !== null && ordersWritten && !chapterSet.has(r.order)) errors.push(`key result ${id}: order page "${r.order}" is not listed`);
    }
  }

  quiz.forEach((q, i) => {
    if (q.options?.length !== 4) errors.push(`quiz ${i + 1} (${q.chapter}): needs exactly 4 options`);
    if (!(Number.isInteger(q.answer) && q.answer >= 0 && q.answer <= 3)) errors.push(`quiz ${i + 1} (${q.chapter}): answer must be 0–3`);
  });
  for (const ch of chapters) if (!quiz.some(q => q.chapter === ch.id)) errors.push(`${ch.id} has no quiz question`);

  return { errors, stats };
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const { errors, stats } = lint(join(fileURLToPath(new URL('..', import.meta.url))));
  for (const e of errors) console.error(`✗ ${e}`);
  console.log(`${stats.chapters} chapters, ${stats.blocks} blocks, ${stats.terms} terms, ${stats.quiz} questions — ${errors.length} error(s)`);
  process.exit(errors.length ? 1 : 0);
}
