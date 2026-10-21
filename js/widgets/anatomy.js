/* A tappable side view of an insect. Each hotspot in img/svg/anatomy.svg is a
   glossary term id; tapping it opens that term's sheet. */

import { displayName } from '../names.js';

export const PARTS = ['head', 'thorax', 'abdomen', 'antenna', 'compound-eye', 'ocellus', 'mouthparts',
  'prothorax', 'mesothorax', 'metathorax', 'coxa', 'trochanter', 'femur', 'tibia', 'tarsus', 'claw',
  'forewing', 'hindwing', 'scutellum', 'cercus', 'ovipositor', 'spiracle'];

const SVG = new URL('../../img/svg/anatomy.svg', import.meta.url);

export async function mount(el, { lang, onTerm, terms }) {
  el.innerHTML = await (await fetch(SVG)).text();
  el.classList.add('anatomy');
  for (const g of el.querySelectorAll('[data-part]')) {
    const id = g.dataset.part, term = terms?.get(id);
    g.setAttribute('role', 'button');
    g.setAttribute('tabindex', '0');
    g.setAttribute('aria-label', term ? displayName(term.name, lang) : id);
    const open = () => {
      el.querySelectorAll('[data-part].on').forEach(x => x.classList.remove('on'));
      g.classList.add('on');
      onTerm?.(id);
    };
    g.addEventListener('click', open);
    g.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(); } });
  }
  return { destroy() { el.replaceChildren(); } };
}
