/* Loading chapters and turning their blocks into DOM.

   Knows nothing about routing. Widgets are drawn by their own modules,
   passed in through `ctx`, so this file stays a plain renderer. */

import { pick, t } from './i18n.js';
import { parseInline } from './markup.js';
import { displayName } from './names.js';
import { aiLabel } from './pesticides.js';

const cache = new Map();
// Resolved against this module, not the page, so it works from any route or test page.
const DATA = new URL('../data/', import.meta.url);

async function json(name) {
  const path = new URL(name, DATA).href;
  if (!cache.has(path)) {
    cache.set(path, fetch(path).then(r => {
      if (!r.ok) throw new Error(`${path}: ${r.status}`);
      return r.json();
    }).catch(e => { cache.delete(path); throw e; }));
  }
  return cache.get(path);
}

export const loadIndex = () => json('index.json');
export const loadChapter = id => json(`${id}.json`);
export const loadData = name => json(`${name}.json`);

export function el(tag, attrs = {}, ...kids) {
  const n = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (v == null || v === false) continue;
    if (k === 'class') n.className = v;
    else if (k.startsWith('on')) n.addEventListener(k.slice(2), v);
    else n.setAttribute(k, v === true ? '' : v);
  }
  for (const k of kids.flat(Infinity)) if (k != null) n.append(k instanceof Node ? k : String(k));
  return n;
}

// Text with {{t:…}} terms turned into buttons that open the term sheet.
export function inline(value, ctx) {
  const frag = document.createDocumentFragment();
  // A value carrying a Taiwan form is a name: show both in Chinese.
  for (const piece of parseInline(value?.zhTw ? displayName(value, ctx.lang) : pick(value, ctx.lang))) {
    if (piece.text !== undefined) { frag.append(piece.text); continue; }
    if (piece.chapter) { frag.append(el('a', { class: 'ch-link', href: `#/ch/${piece.chapter}` }, piece.label)); continue; }
    const term = ctx.terms?.get(piece.term);
    const label = piece.label ?? (term ? pick(term.name, ctx.lang) : piece.term);
    frag.append(el('button', { class: 'term', type: 'button', 'data-term': piece.term, onclick: () => ctx.onTerm?.(piece.term) }, label));
  }
  return frag;
}

const NOTE_LABEL = { tip: 'noteTip', warn: 'noteWarn', key: 'noteKey', myth: 'noteMyth' };

function sourceTag(b, ctx) {
  if (!b.src?.length || !ctx.sourceLabel) return null;
  return el('p', { class: 'block-src' }, `${t('source', null, ctx.lang)}: `, b.src.map(ctx.sourceLabel).join(' · '));
}

function block(b, ctx) {
  switch (b.type) {
    case 'p': return el('p', {}, inline(b.text, ctx));
    case 'list': {
      const tag = b.ordered ? 'ol' : 'ul';
      return el(tag, {}, b.items.map(i => el('li', {}, inline(i, ctx))));
    }
    case 'keyval':
      // Each pair in its own <div> (valid inside <dl>; display: contents in the
      // stylesheet keeps the grid) so a pair can be marked as one block.
      return el('dl', { class: 'keyval' }, b.rows.map(r => el('div', { class: 'keyval-row' }, el('dt', {}, inline(r.k, ctx)), el('dd', {}, inline(r.v, ctx)))));
    case 'table':
      return el('figure', { class: 'table-wrap' },
        b.caption ? el('figcaption', {}, inline(b.caption, ctx)) : null,
        el('div', { class: 'table-scroll', tabindex: '0' },
          el('table', {},
            el('thead', {}, el('tr', {}, b.headers.map(h => el('th', { scope: 'col' }, inline(h, ctx))))),
            el('tbody', {}, b.rows.map(r => el('tr', {}, r.map(c => el('td', {}, inline(c, ctx)))))))));
    case 'note':
      return el('aside', { class: `note note-${b.kind}` },
        el('p', { class: 'note-label' }, t(NOTE_LABEL[b.kind] ?? 'noteKey', null, ctx.lang)),
        el('p', {}, inline(b.text, ctx)));
    case 'figure':
      return el('figure', { class: 'figure' },
        el('img', { src: b.src, alt: pick(b.alt ?? b.caption, ctx.lang), loading: 'lazy' }),
        b.caption ? el('figcaption', {}, inline(b.caption, ctx)) : null);
    case 'species':
      return el('header', { class: 'species-card' },
        el('p', { class: 'species-name' }, displayName(b.names, ctx.lang)),
        el('p', { class: 'species-sci' }, el('i', {}, b.sci), b.authority ? ` ${b.authority}` : null),
        el('dl', { class: 'species-facts' },
          el('div', {}, el('dt', {}, t('orderLabel', null, ctx.lang)), el('dd', {}, el('a', { href: `#/ch/${b.order}` }, ctx.pageTitle?.(b.order) ?? b.order))),
          b.crops?.length ? el('div', {}, el('dt', {}, t('cropsLabel', null, ctx.lang)), el('dd', {}, b.crops.map(c => pick(c, ctx.lang)).join(ctx.lang === 'zh' ? '、' : ', '))) : null,
          el('div', {}, el('dt', {}, t('damagingStage', null, ctx.lang)), el('dd', {}, inline(b.stage, ctx)))));
    case 'photo': {
      const ph = ctx.photos?.get(b.id);
      if (!ph) return null;
      return el('figure', { class: 'photo' },
        el('img', { src: ph.file, alt: pick(ph.subject, ctx.lang), loading: 'lazy' }),
        el('figcaption', {}, el('span', { class: 'photo-subject' }, pick(ph.subject, ctx.lang)), el('span', { class: 'photo-credit' }, pick(ph.credit, ctx.lang))));
    }
    case 'control': {
      const ais = (b.ai ?? []).map(id => ctx.pesticides?.get(id)).filter(Boolean);
      return el('div', { class: `control control-${b.level}` },
        el('p', {}, inline(b.text, ctx)),
        ais.length ? el('p', { class: 'control-ai' }, `${t('activeIngredients', null, ctx.lang)}: `,
          ais.map((p, i) => [i ? (ctx.lang === 'zh' ? '、' : ', ') : null, el('span', { class: p.status === 'banned' ? 'ai ai-banned' : 'ai' }, aiLabel(p, ctx.lang))])) : null);
    }
    case 'widget': {
      const host = el('div', { class: `widget widget-${b.type}`, 'data-widget': b.id });
      ctx.mountWidget?.(host, b.id, { lang: ctx.lang, opts: b.opts ?? {}, onTerm: ctx.onTerm, terms: ctx.terms });
      return host;
    }
    default:
      console.warn('[content] unknown block type', b.type);
      return null;
  }
}

/* What a reader can mark, bookmark or have read aloud (reader.js), in
   reading order within a section. */
const MARKABLE = new Set(['p', 'list', 'keyval', 'table', 'note', 'control']);
const UNITS = ':scope > p[data-blk], :scope > div.control[data-blk], :scope > ul[data-blk] > li, :scope > ol[data-blk] > li, '
  + ':scope > dl[data-blk] > .keyval-row, :scope > aside[data-blk], :scope > figure[data-blk] tbody tr';

export function renderSections(chapter, ctx) {
  const frag = document.createDocumentFragment();
  let level = null, lastChemical = null;
  for (const sec of chapter.sections) {
    const body = sec.blocks.map(b => {
      const node = block(b, ctx);
      // Control methods are grouped under an IPM heading each time the level changes.
      if (b.type === 'control' && node) {
        const head = b.level !== level ? el('h3', { class: 'ipm-head' }, t(`ipm_${b.level}`, null, ctx.lang)) : null;
        level = b.level;
        if (b.level === 'chemical') lastChemical = node;
        const src = sourceTag(b, ctx);
        node.dataset.blk = '';
        return [head, node, src];
      }
      if (node && MARKABLE.has(b.type)) node.dataset.blk = '';
      const src = b.type === 'widget' ? null : sourceTag(b, ctx);
      return src && node ? [node, src] : node;
    }).flat().filter(Boolean);
    if (sec.level === 'advanced') {
      frag.append(el('details', { class: 'section advanced', id: sec.id },
        el('summary', {}, el('span', { class: 'adv-tag' }, t('advanced', null, ctx.lang)), ' ', inline(sec.heading, ctx)),
        ...body));
    } else {
      frag.append(el('section', { class: 'section', id: sec.id }, el('h2', {}, inline(sec.heading, ctx)), ...body));
    }
  }
  // Any page that names chemical control ends that group with the label warning.
  if (lastChemical) {
    const warn = el('aside', { class: 'note note-warn' }, el('p', { class: 'note-label' }, t('noteWarn', null, ctx.lang)), el('p', {}, t('pesticideWarning', null, ctx.lang)));
    const after = lastChemical.nextElementSibling?.classList.contains('block-src') ? lastChemical.nextElementSibling : lastChemical;
    after.after(warn);
  }
  // Each markable block gets a key that is the same in every language:
  // chapter, section, place in the section.
  for (const sec of frag.children) {
    sec.querySelectorAll(UNITS).forEach((u, i) => { u.dataset.rk = `${chapter.id}/${sec.id}#${i}`; });
  }
  return frag;
}
