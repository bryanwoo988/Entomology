import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, mkdirSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, dirname } from 'node:path';
import { lint } from '../tools/lint-content.mjs';

const T = (en) => ({ zh: `中${en}`, en, ms: `M${en}` });

// A two-chapter course that passes every rule. Each test breaks one thing.
function base() {
  return {
    index: { app: T('App'), stages: [{ n: 1, title: T('S1'), blurb: T('b'), chapters: ['p01'] }, { n: 6, title: T('S6'), blurb: T('b'), chapters: ['p02'] }],
      chapters: [{ id: 'p01', num: 1, stage: 1, kind: 'order', title: T('One'), blurb: T('b') }, { id: 'p02', num: 2, stage: 6, title: T('Two'), blurb: T('b') }] },
    terms: [
      { id: 'air', name: T('air'), short: T('gas'), chapter: 1 },
      { id: 'monsoon', name: T('monsoon'), short: T('seasonal wind'), chapter: 2 },
    ],
    sources: [{ id: 'PAM', title: 'Principles of Agricultural Meteorology', publisher: 'Scientific Publishers', url: '', accessed: '' },
      { id: 'met', title: 'MetMalaysia', publisher: 'MetMalaysia', url: 'https://www.met.gov.my/', accessed: '2026-10-02' }],
    quiz: [
      { stage: 1, chapter: 'p01', q: T('q1'), options: [T('a'), T('b'), T('c'), T('d')], answer: 0, why: T('w'), src: ['PAM'] },
      { stage: 1, chapter: 'p01', q: T('q2'), options: [T('True'), T('False')], answer: 1, why: T('w'), src: ['PAM'] },
      { type: 'match', stage: 1, chapter: 'p01', q: T('q3'), pairs: [{ left: T('a'), right: T('1') }, { left: T('b'), right: T('2') }, { left: T('c'), right: T('3') }], why: T('w'), src: ['PAM'] },
      { stage: 6, chapter: 'p02', q: T('q4'), options: [T('a'), T('b'), T('c'), T('d')], answer: 3, why: T('w'), src: ['met'] },
      { stage: 6, chapter: 'p02', q: T('q5'), options: [T('a'), T('b'), T('c')], answer: 2, why: T('w'), src: ['met'] },
      { stage: 6, chapter: 'p02', q: T('q6'), options: [T('a'), T('b')], answer: 0, why: T('w'), src: ['met'] },
    ],
    datasets: [],
    pesticides: [{ id: 'cypermethrin', name: T('Cypermethrin'), status: 'registered', src: ['met'], checked: '2026-10-21' },
      { id: 'endosulfan', name: T('Endosulfan'), status: 'banned', src: ['met'], checked: '2026-10-21' }],
    photos: [{ id: 'bug', file: 'img/species/bug.webp', subject: T('bug'), credit: T('MPOB'), licence: 'MPOB-permission', author: 'MPOB', url: 'https://mpob.gov.my/' }],
    files: { 'img/species/bug.webp': 'x' },
    key: { start: 'a', nodes: { a: { q: T('q'), hint: T('h'), options: [{ label: T('yes'), result: 'r' }, { label: T('no'), result: 'outside' }] } },
      results: { r: { group: T('Bugs'), order: 'p01', check: [T('c')], confused: [], src: ['met'] }, outside: { group: T('x'), order: null, check: [T('x')], confused: [], src: ['met'] } } },
    p01: { id: 'p01', num: 1, stage: 1, title: T('One'), newTerms: ['air'], sources: ['PAM'], sections: [
      { id: 's1', heading: T('h'), level: 'basic', blocks: [
        { type: 'p', src: ['PAM'], defines: ['air'], text: { zh: '{{t:air}} 是', en: '{{t:air}} is', ms: '{{t:air}} ialah' } },
        { type: 'table', src: ['PAM'], caption: T('c'), headers: [T('a'), T('b')], rows: [[T('1'), T('2')]] },
      ] }] },
    p02: { id: 'p02', num: 2, stage: 6, title: T('Two'), newTerms: ['monsoon'], sources: ['met'], sections: [
      { id: 's1', heading: T('h'), level: 'basic', blocks: [
        { type: 'p', src: ['met'], defines: ['monsoon'], text: { zh: '{{t:monsoon}} 和 {{t:air}}', en: '{{t:monsoon}} and {{t:air}}', ms: '{{t:monsoon}} dan {{t:air}}' } },
      ] }] },
  };
}

function write(c) {
  const root = mkdtempSync(join(tmpdir(), 'bugs-lint-'));
  mkdirSync(join(root, 'data'));
  const w = (f, v) => writeFileSync(join(root, 'data', f), JSON.stringify(v));
  w('index.json', c.index); w('terms.json', c.terms); w('sources.json', c.sources);
  w('quiz.json', c.quiz); w('datasets.json', c.datasets); w('p01.json', c.p01); w('p02.json', c.p02);
  w('pesticides.json', c.pesticides); w('photos.json', c.photos); w('key.json', c.key);
  for (const [f, body] of Object.entries(c.files)) { mkdirSync(join(root, dirname(f)), { recursive: true }); writeFileSync(join(root, f), body); }
  return root;
}
const errorsOf = mutate => { const c = base(); mutate(c); return lint(write(c)).errors; };
const has = (errors, re) => assert.ok(errors.some(e => re.test(e)), `expected ${re} in:\n${errors.join('\n')}`);

test('a valid course has no errors', () => assert.deepEqual(lint(write(base())).errors, []));

test('missing Malay is an error', () => has(errorsOf(c => { delete c.p01.title.ms; }), /p01.*\bms\b/));

test('a term used before the chapter that defines it', () => has(errorsOf(c => {
  c.p01.sections[0].blocks.push({ type: 'p', text: T('{{t:monsoon}}') });
}), /p01 uses "monsoon" defined in p02/));

test('a term used before its defining paragraph in the same chapter', () => has(errorsOf(c => {
  c.p01.sections[0].blocks.unshift({ type: 'p', text: T('{{t:air}} early') });
}), /p01 uses "air" before its defining paragraph/));

test('an unknown term', () => has(errorsOf(c => { c.p01.sections[0].blocks.push({ type: 'p', text: T('{{t:nope}}') }); }), /unknown term "nope"/));

test('a term defined twice or never', () => {
  has(errorsOf(c => { c.p02.sections[0].blocks[0].defines.push('air'); }), /"air" is defined 2 times/);
  has(errorsOf(c => { delete c.p01.sections[0].blocks[0].defines; }), /"air" is never defined/);
});

test('newTerms must match the terms of that chapter', () => has(errorsOf(c => { c.p01.newTerms = []; }), /p01 newTerms/));

test('unknown source', () => has(errorsOf(c => { c.p01.sources.push('ghost'); }), /unknown source "ghost"/));

test('a Malaysia-stage block without a source', () => has(errorsOf(c => { delete c.p02.sections[0].blocks[0].src; }), /p02 .*no src/));

test('table rows must match headers', () => has(errorsOf(c => { c.p01.sections[0].blocks[1].rows[0].push(T('3')); }), /p01 table row 1 has 3 cells/));

test('a widget without a module', () => has(errorsOf(c => { c.p01.sections[0].blocks.push({ type: 'widget', id: 'W99' }); }), /widget W99 has no module/));

test('every page needs at least 3 quiz items', () => has(errorsOf(c => { c.quiz.shift(); }), /p01 has 2 quiz items/));
test('mc needs 2–4 options and an answer among them', () => {
  has(errorsOf(c => { c.quiz[1].options.pop(); }), /quiz 2 .*2–4 options/);
  has(errorsOf(c => { c.quiz[0].answer = 4; }), /quiz 1 .*answer/);
});
test('match needs 3–5 pairs', () => has(errorsOf(c => { c.quiz[2].pairs.pop(); }), /quiz 3 .*3–5 pairs/));
test('a quiz item needs a source', () => has(errorsOf(c => { delete c.quiz[0].src; }), /quiz 1 .*src/));
test('an unknown quiz type fails', () => has(errorsOf(c => { c.quiz[0].type = 'essay'; }), /quiz 1 .*type/));

test('a chapter not yet written (ready:false) is listed but not required', () => {
  assert.deepEqual(errorsOf(c => {
    c.index.chapters.push({ id: 'p03', num: 3, stage: 6, title: T('Three'), blurb: T('b'), ready: false });
  }), []);
});

test('a link to a chapter that does not exist', () => has(errorsOf(c => {
  c.p01.sections[0].blocks.push({ type: 'p', text: T('{{ch:ch99|nowhere}}') });
}), /unknown chapter "ch99"/));

test('empty zhTw is an error', () => has(errorsOf(c => { c.terms[0].name.zhTw = ''; }), /zhTw/));

// Species pages, photos and control sections (p02 doubles as a species page here).
const sp = c => c.p02.sections[0].blocks;
const control = (level, ai) => ({ type: 'control', level, text: T(level), src: ['met'], ...(ai ? { ai } : {}) });

test('a markable block without src is an error on any stage', () => has(errorsOf(c => { delete c.p01.sections[0].blocks[0].src; }), /p01.*no src/));
test('control blocks must follow IPM order', () => has(errorsOf(c => { sp(c).push(control('chemical', ['cypermethrin']), control('cultural')); }), /IPM order/));
test('control blocks in IPM order pass', () => assert.deepEqual(errorsOf(c => { sp(c).push(control('monitor'), control('cultural'), control('biological'), control('chemical', ['cypermethrin'])); }), []));
test('unknown pesticide status fails', () => has(errorsOf(c => { c.pesticides.push({ id: 'x', name: T('x'), status: 'unknown', src: ['met'], checked: '2026-10-21' }); sp(c).push(control('chemical', ['x'])); }), /status unknown/));
test('undeclared pesticide fails', () => has(errorsOf(c => { sp(c).push(control('chemical', ['nope'])); }), /unknown pesticide/));
test('a pesticide named in text must be declared in a chemical block', () => {
  has(errorsOf(c => { sp(c).push({ type: 'p', text: T('Spray cypermethrin weekly.'), src: ['met'] }); }), /names pesticide "cypermethrin"/);
  has(errorsOf(c => { sp(c).push(control('chemical')); sp(c)[sp(c).length - 1].text = T('Use Cypermethrin.'); }), /names pesticide "cypermethrin"/);
});
test('a pesticide named in a chemical block that declares it passes', () => assert.deepEqual(errorsOf(c => {
  sp(c).push(control('chemical', ['cypermethrin'])); sp(c)[sp(c).length - 1].text = T('Use cypermethrin.');
}), []));
test('a photo block must name a registered photo', () => has(errorsOf(c => { sp(c).push({ type: 'photo', id: 'ghost' }); }), /unknown photo "ghost"/));
test('a photo needs a licence', () => has(errorsOf(c => { delete c.photos[0].licence; }), /photo bug.*licence/));
test('a photo licence must be open or MPOB permission', () => has(errorsOf(c => { c.photos[0].licence = 'CC BY-NC 4.0'; }), /photo bug.*licence/));
test('a photo file must exist', () => has(errorsOf(c => { c.files = {}; }), /photo bug.*not found/));
test('species block needs sci and an existing order page', () => {
  has(errorsOf(c => { sp(c).push({ type: 'species', names: T('Bug'), order: 'p01', crops: [], stage: T('larva'), src: ['met'] }); }), /species.*sci/);
  has(errorsOf(c => { sp(c).push({ type: 'species', names: T('Bug'), sci: 'Bugus bugus', order: 'p99', crops: [], stage: T('larva'), src: ['met'] }); }), /order page "p99"/);
});

test('a broken key fails lint', () => has(errorsOf(c => { c.key.nodes.a.options[0].next = 'ghost'; }), /key: .*ghost/));
test('a key result needs a source', () => has(errorsOf(c => { c.key.results.r.src = []; }), /key result r.*src/));
test('a key result must point at a listed page', () => has(errorsOf(c => { c.key.results.r.order = 'p77'; }), /key result r.*p77/));
test('a species card may list several species, comma-separated', () => {
  assert.deepEqual(errorsOf(c => { sp(c).push({ type: 'species', names: T('Bagworms'), sci: 'Metisa plana, Pteroma pendula', order: 'p01', crops: [], stage: T('larva'), src: ['met'] }); }), []);
  has(errorsOf(c => { sp(c).push({ type: 'species', names: T('Bagworms'), sci: 'Metisa plana, pendula', order: 'p01', crops: [], stage: T('larva'), src: ['met'] }); }), /species needs sci/);
});
