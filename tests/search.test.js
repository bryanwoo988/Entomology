import { test } from 'node:test';
import assert from 'node:assert/strict';
import { buildIndex, search, normalise } from '../js/search.js';

const page = {
  id: 'p05', num: 5, title: { zh: '翅', en: 'Wings', ms: 'Sayap' },
  sections: [{ id: 's1', heading: { zh: '露点与翅', en: 'Dew point and wings', ms: 'Takat embun dan sayap' }, blocks: [
    { type: 'p', text: { zh: '{{t:dew-point}}是水汽凝结的温度。', en: 'The {{t:dew-point}} is where water vapour condenses.', ms: '{{t:dew-point}} ialah suhu wap air memeluwap.' } },
  ] }],
};
const terms = [{ id: 'dew-point', name: { zh: '露点', en: 'Dew point', ms: 'Takat embun' }, short: { zh: '凝结温度', en: 'Condensation temperature', ms: 'Suhu pemeluwapan' }, chapter: 5 }];
const index = buildIndex([page], terms);

test('a Chinese query finds the chapter, titled in the reading language', () => {
  const hits = search(index, '露点', 'ms');
  assert.ok(hits.length > 0);
  assert.ok(hits.some(h => h.route.startsWith('#/ch/p05')));
  assert.ok(hits.every(h => !/[一-鿿]/.test(h.title)), `titles not in Malay: ${hits.map(h => h.title)}`);
});
test('Latin search ignores case and accents', () => {
  assert.ok(search(index, 'DEW POINT', 'en').length > 0);
  assert.equal(normalise('Évaporation'), 'evaporation');
});
test('all words must match', () => {
  assert.ok(search(index, 'dew point', 'en').length > 0);
  assert.equal(search(index, 'dew zebra', 'en').length, 0);
});
test('term markup is searchable by what the reader sees', () => {
  assert.ok(search(index, 'Takat embun', 'ms').some(h => h.route.startsWith('#/ch/p05')));
});
test('snippets contain no raw markup', () => {
  for (const h of search(index, 'vapour', 'en')) assert.ok(!h.snippet.includes('{{'), h.snippet);
});
test('empty query returns nothing', () => assert.deepEqual(search(index, '  ', 'en'), []));
test('a term result opens the page that teaches it', () => {
  assert.ok(search(index, 'Dew point', 'en').some(h => h.kind === 'term' && h.route === '#/ch/p05'));
});
