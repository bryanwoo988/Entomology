/* Browser tests: each case opens the real app in an iframe at a given size
   with given saved preferences, then inspects it. Same origin, so storage
   written here is what the app reads. */

const KEY = 'bugs.prefs.v1';
const results = document.getElementById('results');
let passed = 0, failed = 0;

const sleep = ms => new Promise(r => setTimeout(r, ms));

async function until(fn, ms = 4000) {
  const t0 = performance.now();
  for (;;) {
    try { const v = fn(); if (v) return v; } catch { /* not yet */ }
    if (performance.now() - t0 > ms) throw new Error(`timed out waiting for ${fn}`);
    await sleep(50);
  }
}

async function openApp({ hash = '', width = 375, height = 740, prefs = null }) {
  localStorage.removeItem(KEY);
  if (prefs) localStorage.setItem(KEY, JSON.stringify({ lang: 'en', theme: 'light', scale: 1, chosen: true, read: {}, quiz: {}, lastRoute: '', seenVersion: '1.0.0', ...prefs }));
  const f = document.createElement('iframe');
  f.width = width; f.height = height;
  f.src = `../index.html${hash}`;
  document.getElementById('frames').append(f);
  await new Promise(r => f.addEventListener('load', r, { once: true }));
  const w = f.contentWindow;
  await until(() => w.document.documentElement.dataset.ready === 'true');
  return { f, w, d: w.document, close: () => f.remove() };
}

async function test(name, fn) {
  const li = document.createElement('li');
  try { await fn(); li.className = 'pass'; li.textContent = `✓ ${name}`; passed++; }
  catch (e) { li.className = 'fail'; li.innerHTML = `✗ ${name}<pre>${e.stack || e}</pre>`; failed++; }
  results.append(li);
}

const assert = (c, msg) => { if (!c) throw new Error(msg); };

// Page-dependent cases wait until content exists (the content tasks re-enable them).
const IDX = await (await fetch('../data/index.json', { cache: 'no-store' })).json();
const P = IDX.chapters.map(c => c.id);
async function testIf(cond, name, fn) {
  if (cond) return test(name, fn);
  const li = document.createElement('li');
  li.className = 'skip'; li.textContent = `– ${name} (skipped: no pages yet)`;
  results.append(li);
}

await test('first visit shows the language picker with English as default', async () => {
  const a = await openApp({});
  const picker = await until(() => a.d.getElementById('picker'));
  assert(!picker.hidden, 'picker hidden');
  assert(a.d.querySelector('#picker [data-lang="en"]').classList.contains('is-default'), 'English not marked default');
  a.close();
});

await testIf(P.length > 0, 'deep link survives the language picker', async () => {
  const a = await openApp({ hash: '#/ch/p09/s3' });
  a.d.querySelector('#picker [data-lang="zh"]').click();
  await until(() => a.d.getElementById('s3'));
  assert(a.w.location.hash === '#/ch/p09/s3', `hash is ${a.w.location.hash}`);
  assert(a.d.documentElement.lang.startsWith('zh'), 'language not applied');
  await sleep(200);
  const top = a.d.getElementById('s3').getBoundingClientRect().top;
  assert(top > -5 && top < 160, `section s3 at ${top}px`);
  a.close();
});

await test('Settings sets language, theme and text size', async () => {
  const a = await openApp({ hash: '#/settings', prefs: { lang: 'en' } });
  const segs = await until(() => a.d.querySelectorAll('.setseg').length >= 3 && a.d.querySelectorAll('.setseg'));
  [...segs[0].querySelectorAll('button')].find(b => b.textContent === 'Bahasa Melayu').click();
  await until(() => a.d.documentElement.lang === 'ms' && a.d.querySelector('[data-nav="settings"] span').textContent === 'Tetapan');
  [...a.d.querySelectorAll('.setseg')[1].querySelectorAll('button')][2].click();
  await until(() => a.d.documentElement.dataset.theme === 'dark');
  assert(a.d.querySelectorAll('.setseg')[1].querySelectorAll('button')[2].classList.contains('on'), 'dark not shown as chosen');
  [...a.d.querySelectorAll('.setseg')[2].querySelectorAll('button')].find(b => b.textContent === '130%').click();
  await until(() => 'single' in a.d.documentElement.dataset);
  const saved = JSON.parse(localStorage.getItem(KEY));
  assert(saved.lang === 'ms' && saved.theme === 'dark' && saved.scale === 1.3, JSON.stringify(saved));
  assert(!a.d.querySelector('[data-action="lang"]'), 'old language button still in the top bar');
  a.close();
});

await test('theme is applied by an inline script before the stylesheet', async () => {
  const html = await (await fetch('../index.html', { cache: 'no-store' })).text();
  const pre = html.indexOf('id="prepaint"'), css = html.indexOf('css/app.css');
  assert(pre > 0 && pre < css, 'prepaint script missing or after the stylesheet');
  const a = await openApp({ prefs: { theme: 'dark' } });
  assert(a.d.documentElement.dataset.theme === 'dark', 'dark theme not applied');
  a.close();
});

await testIf(P.length > 0, 'text size 1.3 switches the chapter to a single column', async () => {
  const cols = async scale => {
    const a = await openApp({ hash: '#/ch/p05', width: 1200, prefs: { scale } });
    await until(() => a.d.getElementById('s1'));
    const n = a.w.getComputedStyle(a.d.querySelector('.page-chapter')).gridTemplateColumns.split(' ').length;
    const single = 'single' in a.d.documentElement.dataset;
    a.close();
    return [n, single];
  };
  const [normal] = await cols(1);
  const [big, single] = await cols(1.3);
  assert(normal === 2, `scale 1 has ${normal} columns`);
  assert(single && big === 1, `scale 1.3 has ${big} columns, data-single=${single}`);
});

for (const lang of ['ms', 'zh', 'en']) {
  await test(`no horizontal overflow at 375px × scale 1.5 in ${lang}`, async () => {
    for (const hash of ['#/', '#/key', '#/key/1.0.1.1.1.1.1.1.0', ...P.map(id => `#/ch/${id}`), '#/stage/3', '#/info', '#/settings', '#/notes', '#/bookmarks', '#/share', '#/search', '#/tools', '#/tools/glossary', '#/tools/quiz/1', '#/tools/cards', '#/tools/exam', '#/tools/wrong', '#/tools/progress']) {
      const a = await openApp({ hash, prefs: { lang, scale: 1.5 } });
      await sleep(250);
      const sw = a.d.scrollingElement.scrollWidth;
      a.close();
      assert(sw <= 375, `${hash}: scrollWidth ${sw}`);
    }
  });
}

await test('share page shows a QR code, a share button and copy link', async () => {
  const a = await openApp({ hash: '#/share', prefs: { lang: 'zh' } });
  const svg = await until(() => a.d.querySelector('#share-host svg'));
  assert(svg.querySelectorAll('rect, path').length > 0, 'QR svg is empty');
  assert(a.d.querySelector('[data-share="copy"]'), 'no copy button');
  assert(a.d.querySelector('[data-share="native"]'), 'no share button');
  assert(a.d.querySelector('.share-url').textContent.includes('bryanwoo988.github.io/Entomology/'), 'URL not shown');
  a.close();
});

const type = (a, input, text) => { input.value = text; input.dispatchEvent(new a.w.Event('input', { bubbles: true })); };

await testIf(P.includes('p33'), 'an order page links to its farm insects', async () => {
  const a = await openApp({ hash: '#/ch/p12', prefs: { lang: 'en' } });
  await until(() => a.d.querySelector('.chapter h1'));
  const link = a.d.querySelector('.farm-links a[href="#/ch/p33"]');
  assert(link && link.textContent.includes('Sycanus'), 'no link to the assassin bug page');
  a.close();
});

await testIf(P.length > 0, 'About lists every photo with its credit and link', async () => {
  const photos = await (await fetch('/data/photos.json')).json();
  const a = await openApp({ hash: '#/settings', prefs: { lang: 'en' } });
  await until(() => a.d.querySelector('.photo-credits'));
  const items = [...a.d.querySelectorAll('.photo-credits li')];
  assert(items.length === photos.length, `${items.length} credits for ${photos.length} photos`);
  const first = items.find(li => li.textContent.includes(photos[0].credit.en));
  assert(first && first.querySelector(`a[href="${photos[0].url}"]`), 'credit or link missing');
  a.close();
});

await testIf(P.length > 0, 'search finds a chapter from a query in another language', async () => {
  const a = await openApp({ hash: '#/search', prefs: { lang: 'ms' } });
  const input = await until(() => a.d.querySelector('#search-input'));
  type(a, input, '复眼');
  const first = await until(() => a.d.querySelector('.search-results a'));
  assert(first.getAttribute('href').startsWith('#/ch/p03'), first.getAttribute('href'));
  assert(!/[\u4e00-\u9fff]/.test(first.querySelector('.hit-title').textContent), 'title not in Malay');
  a.close();
});

await testIf(P.length > 0, 'a stage quiz scores answers and remembers the best', async () => {
  const a = await openApp({ hash: '#/tools/quiz/3', prefs: { lang: 'en' } });
  await until(() => a.d.querySelector('.quiz-q'));
  const qs = a.d.querySelectorAll('.quiz-q');
  for (const q of qs) {
    if (q.dataset.answer !== undefined) { q.querySelectorAll('.quiz-opt')[Number(q.dataset.answer)].click(); continue; }
    const lefts = q.querySelectorAll('.match-left button');
    lefts.forEach((b, i) => { b.click(); q.querySelector(`.match-right button[data-i="${i}"]`).click(); });
    q.querySelector('.match-submit').click();
  }
  const score = await until(() => a.d.querySelector('.quiz-score'));
  assert(score.textContent.includes(`${qs.length}/${qs.length}`), score.textContent);
  const saved = JSON.parse(a.w.localStorage.getItem('bugs.prefs.v1'));
  assert(saved.quiz[3] === qs.length, `best not saved: ${JSON.stringify(saved.quiz)}`);
  a.close();
});

await testIf(P.length > 0, 'glossary, flashcards and the tools list open', async () => {
  for (const [hash, sel, min] of [['#/tools/glossary', '.gloss-item', 1], ['#/tools/cards', '.flashcard', 1], ['#/tools', '.tool-list a', 3]]) {
    const a = await openApp({ hash, prefs: { lang: 'zh' } });
    await until(() => a.d.querySelectorAll(sel).length >= min);
    a.close();
  }
});

await test('nested children render as elements, never as "[object HTMLElement]"', async () => {
  const { el } = await import('../js/content.js');
  const dl = el('dl', {}, [[el('dt', {}, 'k1'), el('dd', {}, 'v1')], [el('dt', {}, 'k2'), el('dd', {}, 'v2')]]);
  assert(!dl.textContent.includes('[object'), 'pairs were turned into text');
  assert(dl.querySelectorAll('dt').length === 2 && dl.querySelectorAll('dd').length === 2, 'dt/dd missing');
});

await test('no chapter shows "[object …]" text', async () => {
  const idx = await (await fetch('../data/index.json')).json();
  const { renderSections } = await import('../js/content.js');
  const bad = [];
  for (const meta of idx.chapters) {
    const ch = await (await fetch(`../data/${meta.id}.json`)).json();
    const host = document.createElement('div');
    host.append(renderSections(ch, { lang: 'en', terms: new Map() }));
    if (/\[object /.test(host.textContent)) bad.push(meta.id);
  }
  assert(!bad.length, 'broken text in ' + bad.join(', '));
});

await test('a figure renders its drawing and caption, with no source line', async () => {
  const { renderSections } = await import('../js/content.js');
  const T = en => ({ zh: `中${en}`, en, ms: `M${en}` });
  const page = { id: 'p92', sections: [{ id: 's1', heading: T('Legs'), blocks: [{ type: 'figure', src: 'img/svg/fig-leg.svg', caption: T('Drawing: 1 coxa') }] }] };
  const host = document.createElement('div');
  host.append(renderSections(page, { lang: 'en', terms: new Map(), sourceLabel: s => s }));
  assert(host.querySelector('figure.figure img')?.getAttribute('src') === 'img/svg/fig-leg.svg', 'drawing missing');
  assert(host.textContent.includes('Drawing: 1 coxa') && !host.querySelector('.block-src'), 'caption or stray source line');
});

await test('a gallery shows its photos side by side, each with its credit', async () => {
  const { renderSections } = await import('../js/content.js');
  const T = en => ({ zh: `中${en}`, en, ms: `M${en}` });
  const ph = id => ({ id, file: 'icons/icon-192.png', subject: T(id), credit: T(`Photo ${id}`) });
  const page = { id: 'p91', sections: [{ id: 's1', heading: T('Beetles'), blocks: [{ type: 'gallery', ids: ['a', 'b', 'gone'] }] }] };
  const host = document.createElement('div');
  host.append(renderSections(page, { lang: 'en', terms: new Map(), photos: new Map([['a', ph('a')], ['b', ph('b')]]) }));
  const g = host.querySelector('.gallery');
  assert(g && g.querySelectorAll('figure.photo').length === 2, 'gallery should hold the two known photos');
  assert(g.textContent.includes('Photo a') && g.textContent.includes('Photo b'), 'credits missing');
});

await test('a species page renders its card, credited photo, IPM headings and the label warning', async () => {
  const { renderSections } = await import('../js/content.js');
  const T = en => ({ zh: `中${en}`, en, ms: `M${en}` });
  const page = { id: 'p90', sections: [{ id: 's1', heading: T('Bagworm'), blocks: [
    { type: 'species', names: { zh: '袋蛾', zhTw: '避债蛾', en: 'Bagworm', ms: 'Ulat bungkus' }, sci: 'Metisa plana', authority: 'Walker, 1883', order: 'p11', crops: [T('Oil palm')], stage: T('Larva'), src: ['RS34'] },
    { type: 'photo', id: 'bug' },
    { type: 'control', level: 'monitor', text: T('Count larvae'), src: ['RS34'] },
    { type: 'control', level: 'chemical', text: T('Trunk injection'), ai: ['cypermethrin', 'endosulfan'], src: ['RS34'] },
  ] }] };
  const ctx = {
    lang: 'zh', terms: new Map(), sourceLabel: s => s,
    pageTitle: id => (id === 'p11' ? '鳞翅目' : id),
    photos: new Map([['bug', { id: 'bug', file: 'icons/icon-192.png', subject: T('bags'), credit: { zh: '照片：MPOB', en: 'Photo: MPOB', ms: 'Foto: MPOB' } }]]),
    pesticides: new Map([['cypermethrin', { name: T('Cypermethrin'), status: 'registered' }], ['endosulfan', { name: { zh: '硫丹', en: 'Endosulfan', ms: 'Endosulfan' }, status: 'banned' }]]),
  };
  const host = document.createElement('div');
  host.append(renderSections(page, ctx));
  const card = host.querySelector('.species-card');
  assert(card && card.textContent.includes('袋蛾（大陆）／避债蛾（台湾）'), 'dual name missing');
  assert(card.querySelector('i')?.textContent === 'Metisa plana', 'sci name not italic');
  assert(card.querySelector('a[href="#/ch/p11"]')?.textContent.includes('鳞翅目'), 'order link missing');
  assert(host.querySelector('figure.photo img')?.getAttribute('src') === 'icons/icon-192.png', 'photo missing');
  assert(host.querySelector('figure.photo .photo-credit')?.textContent === '照片：MPOB', 'credit missing');
  const heads = [...host.querySelectorAll('.ipm-head')].map(h => h.textContent);
  assert(heads.length === 2 && heads[0] === '监测' && heads[1] === '化学防治', `IPM heads: ${heads}`);
  assert(host.textContent.includes('硫丹（已禁用）'), 'banned label missing');
  const warn = host.querySelector('.note-warn');
  assert(warn && warn.textContent.includes('使用任何农药前'), 'pesticide warning missing');
  assert(!/\[object /.test(host.textContent), 'object text');
  const kv = document.createElement('div');
  kv.append(renderSections({ id: 'p91', sections: [{ id: 's1', heading: T('h'), blocks: [{ type: 'keyval', src: ['TJ'], rows: [{ k: { zh: '蝽', zhTw: '椿象', en: 'Stink bug', ms: 'Pepijat busuk' }, v: T('x') }] }] }] }, ctx));
  assert(kv.querySelector('dt').textContent === '蝽（大陆）／椿象（台湾）', `keyval name: ${kv.querySelector('dt').textContent}`);
});

await test('key walks to a result and back', async () => {
  const key = await (await fetch('../data/key.json', { cache: 'no-store' })).json();
  const { encode } = await import('../js/key.js');
  const a = await openApp({ hash: '#/key', prefs: { lang: 'en' } });
  const choose = async label => {
    const btn = await until(() => [...a.d.querySelectorAll('.key-opt')].find(b => b.textContent.startsWith(label)));
    btn.click();
    await sleep(60);
  };
  for (const l of ['No', 'Yes', 'Two pairs', 'No scales', 'No', 'No', 'Different', 'No', 'Yes']) await choose(l);
  const head = await until(() => a.d.querySelector('.key-result h2'));
  assert(head.textContent.includes('Beetle'), `result: ${head.textContent}`);
  assert(a.d.querySelectorAll('.key-check input[type=checkbox]').length >= 2, 'no checklist');
  assert(a.d.querySelector('.key-result a[href="#/ch/p10"]'), 'no order link');
  const crumbs = a.d.querySelectorAll('.key-crumbs button');
  assert(crumbs.length === 9, `crumbs: ${crumbs.length}`);
  crumbs[2].click();
  await until(() => !a.d.querySelector('.key-result') && a.d.querySelector('.key-q'));
  assert(a.d.querySelector('.key-q').textContent.includes(key.nodes.pairs.q.en), 'not back at step 3');
  const first3 = a.w.location.hash.replace('#/key/', '');
  assert(first3 === encode([1, 0]), `hash ${a.w.location.hash}`);
  a.close();
});

await test("key: Can't tell opens the hint", async () => {
  const a = await openApp({ hash: '#/key', prefs: { lang: 'zh' } });
  const btn = await until(() => a.d.querySelector('.key-hint-btn'));
  btn.click();
  await until(() => !a.d.getElementById('sheet').hidden && a.d.querySelector('.sheet-body').textContent.includes('伪装'));
  a.close();
});

await test('exam records a wrong answer in the wrong-answer book, and a right redo clears it', async () => {
  localStorage.removeItem(KEY);
  const prefs = await import('../js/prefs.js'); prefs.init();
  const study = await import('../js/study.js');
  const T = en => ({ zh: `中${en}`, en, ms: `M${en}` });
  const items = [{ stage: 1, chapter: 'p01', q: T('Six legs?'), options: [T('Yes'), T('No')], answer: 0, why: T('Insects have six legs.'), src: ['TJ'] }];
  const host = document.createElement('div'); document.getElementById('frames').append(host);
  host.append(study.examPage('en', { items, seed: 1 }));
  host.querySelector('.exam-count button').click();
  await until(() => host.querySelector('.quiz-opt'));
  host.querySelectorAll('.quiz-opt')[1].click();
  host.querySelector('.exam-submit').click();
  const score = await until(() => host.querySelector('.exam-score'));
  assert(score.textContent.includes('0/1'), score.textContent);
  assert(prefs.get().wrong.length === 1, `wrong: ${prefs.get().wrong}`);
  assert(prefs.get().exams.length === 1, 'exam not recorded');
  host.replaceChildren(study.wrongPage('en', { items }));
  assert(host.querySelectorAll('.wrong-item').length === 1, 'not in the book');
  host.querySelectorAll('.quiz-opt')[0].click();
  await until(() => prefs.get().wrong.length === 0);
  host.replaceChildren(study.wrongPage('en', { items }));
  assert(host.querySelector('.wrong-empty'), 'book not empty');
  host.remove();
});

await test('a match question pairs left and right by tapping', async () => {
  const study = await import('../js/study.js');
  const T = en => ({ zh: `中${en}`, en, ms: `M${en}` });
  const item = { type: 'match', stage: 1, chapter: 'p01', q: T('Match'), why: T('w'), src: ['TJ'],
    pairs: [{ left: T('Beetle'), right: T('Elytra') }, { left: T('Fly'), right: T('Halteres') }, { left: T('Moth'), right: T('Scales') }] };
  let got = null;
  const host = document.createElement('div'); document.getElementById('frames').append(host);
  host.append(study.renderItem(item, 'en', r => { got = r; }));
  const lefts = host.querySelectorAll('.match-left button'), rights = [...host.querySelectorAll('.match-right button')];
  const right = name => rights.find(b => b.textContent === name);
  lefts[0].click(); right('Elytra').click();
  lefts[1].click(); right('Halteres').click();
  lefts[2].click(); right('Scales').click();
  host.querySelector('.match-submit').click();
  assert(got === true, `result ${got}`);
  host.remove();
});

const RKEY = 'bugs.reader';
const reader = () => JSON.parse(localStorage.getItem(RKEY) || '{}');
const bar = a => until(() => { const b = a.d.querySelector('.rd-bar'); return b && !b.hidden && b; });
const firstP = a => until(() => a.d.querySelector('#s2 > p[data-rk]'));

await testIf(P.length > 0, 'tapping a paragraph and a colour marks it in every language, after a reload', async () => {
  localStorage.removeItem(RKEY);
  let a = await openApp({ hash: '#/ch/p01', prefs: { lang: 'en' } });
  const p = await firstP(a);
  const key = p.dataset.rk;
  p.click();
  const b = await bar(a);
  const w = b.getBoundingClientRect();
  assert(w.left >= 0 && w.right <= a.w.innerWidth, `bar overflows: ${w.left}–${w.right}`);
  b.querySelector('[data-c="pink"]').click();
  await until(() => p.querySelector('.rd-ink[data-hl="pink"]'));
  assert(reader().marks[key].hl === 'pink', JSON.stringify(reader().marks));
  a.close();
  a = await openApp({ hash: '#/ch/p01', prefs: { lang: 'zh' } });
  await until(() => a.d.querySelector(`[data-rk="${key}"] .rd-ink[data-hl="pink"]`));
  a.close();
  localStorage.removeItem(RKEY);
});

await testIf(P.length > 0, 'long-press words: only those words are marked, in that language', async () => {
  localStorage.removeItem(RKEY);
  const a = await openApp({ hash: '#/ch/p01', prefs: { lang: 'en' } });
  const p = await firstP(a);
  // The first run of plain text long enough to select 12 characters from.
  const tw = a.d.createTreeWalker(p, 4);
  let tn = tw.nextNode();
  while (tn && tn.data.length < 12) tn = tw.nextNode();
  const r = a.d.createRange(); r.setStart(tn, 0); r.setEnd(tn, 12);
  a.w.getSelection().removeAllRanges(); a.w.getSelection().addRange(r);
  a.d.dispatchEvent(new a.w.Event('selectionchange'));
  (await bar(a)).querySelector('[data-c="green"]').click();
  const mk = await until(() => p.querySelector('.rd-r[data-hl="green"]'));
  assert(mk.textContent === tn.data.slice(0, 12), `marked "${mk.textContent}"`);
  const [range] = Object.values(reader().ranges);
  assert(range.lang === 'en' && range.e - range.s === 12, JSON.stringify(range));
  // Tapping the marked words opens their menu.
  a.w.getSelection().removeAllRanges();
  mk.click();
  await until(() => a.d.querySelector('.rd-sheet [data-do="remove"]'));
  a.d.querySelector('.rd-sheet [data-do="remove"]').click();
  await until(() => !p.querySelector('.rd-r') && !Object.keys(reader().ranges).length);
  a.close();
  localStorage.removeItem(RKEY);
});

await testIf(P.length > 0, 'a note and a bookmark show in Notes and Bookmarks, and lead back', async () => {
  localStorage.removeItem(RKEY);
  const a = await openApp({ hash: '#/ch/p01', prefs: { lang: 'en' } });
  let p = await firstP(a);
  const key = p.dataset.rk;
  p.click();
  (await bar(a)).querySelector('[data-act="bookmark"]').click();
  await until(() => p.querySelector('.rd-bm'));
  p.click();
  (await bar(a)).querySelector('[data-act="note"]').click();
  const ta = await until(() => a.d.querySelector('.rd-sheet textarea'));
  ta.value = 'pressure first';
  a.d.querySelector('.rd-sheet [data-do="save"]').click();
  await until(() => p.querySelector('.rd-nb'));
  a.d.querySelector('[data-nav="notes"]').click();
  const note = await until(() => a.d.querySelector('.page-lib .rd-item-note'));
  assert(note.textContent === 'pressure first', note.textContent);
  assert(a.d.querySelector('[data-nav="notes"]').classList.contains('on'), 'Notes tab not lit');
  a.d.querySelector('[data-nav="bookmarks"]').click();
  const item = await until(() => a.d.querySelector('.page-lib .rd-item'));
  assert(item.querySelector('.rd-item-where').textContent.startsWith('Chapter 1'), item.textContent);
  item.click();
  p = await until(() => a.d.querySelector(`[data-rk="${key}"]`));
  assert(a.w.location.hash === '#/ch/p01', a.w.location.hash);
  a.close();
  localStorage.removeItem(RKEY);
});

await testIf(P.length > 0, 'Read aloud asks for a chapter first, then plays and stops', async () => {
  const a = await openApp({ hash: '#/', prefs: { lang: 'en' } });
  a.d.querySelector('[data-nav="listen"]').click();
  await until(() => !a.d.getElementById('toast').hidden && a.d.getElementById('toast').textContent.includes('Open a chapter'));
  if (a.w.speechSynthesis) {
    a.w.location.hash = '#/ch/p01';
    await firstP(a);
    a.d.querySelector('[data-nav="listen"]').click();
    const pl = await until(() => { const x = a.d.querySelector('.rd-player'); return x && !x.hidden && x; });
    assert(a.d.getElementById('nav-listen').textContent === 'Stop', 'nav label not Stop');
    pl.querySelector('[data-pl="stop"]').click();
    await until(() => pl.hidden);
  }
  a.close();
});

document.getElementById('summary').textContent = `${passed} passed, ${failed} failed`;
