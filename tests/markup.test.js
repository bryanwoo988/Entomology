import { test } from 'node:test';
import assert from 'node:assert/strict';
import { parseInline, termIds, pageId } from '../js/markup.js';

test('terms and labels are split out of text', () => {
  assert.deepEqual(parseInline('A {{t:dew-point}} and {{t:lcl|cloud base}}.'), [
    { text: 'A ' }, { term: 'dew-point' }, { text: ' and ' }, { term: 'lcl', label: 'cloud base' }, { text: '.' },
  ]);
});
test('an unclosed marker stays text', () => {
  assert.deepEqual(parseInline('see {{t:x'), [{ text: 'see {{t:x' }]);
});
test('plain text is one piece; empty is none', () => {
  assert.deepEqual(parseInline('just text'), [{ text: 'just text' }]);
  assert.deepEqual(parseInline(''), []);
});
test('termIds lists ids in order', () => {
  assert.deepEqual(termIds('{{t:a}} x {{t:b|B}} {{t:a}}'), ['a', 'b', 'a']);
});

test('chapter links are split out, with their label', () => {
  assert.deepEqual(parseInline('see {{ch:ch09|Chapter 9}} and {{t:lcl}}'), [
    { text: 'see ' }, { chapter: 'ch09', label: 'Chapter 9' }, { text: ' and ' }, { term: 'lcl' },
  ]);
  assert.deepEqual(termIds('{{ch:ch09|x}} {{t:a}}'), ['a']);
});
test('chapterIds lists linked chapters', async () => {
  const { chapterIds } = await import('../js/markup.js');
  assert.deepEqual(chapterIds('{{ch:ch09|a}} {{ch:ch23|b}}'), ['ch09', 'ch23']);
});

test('page ids are p and two digits', () => {
  assert.equal(pageId(5), 'p05');
  assert.equal(pageId(27), 'p27');
});

test('an order page lists the species pages that name it, in page order', async () => {
  const { speciesOf } = await import('../js/markup.js');
  const index = { chapters: [
    { id: 'p12', kind: 'order' },
    { id: 'p40', kind: 'species', order: 'p12' },
    { id: 'p33', kind: 'species', order: 'p12' },
    { id: 'p28', kind: 'species', order: 'p10' },
    { id: 'p27', kind: 'crop' },
  ] };
  assert.deepEqual(speciesOf(index, 'p12').map(c => c.id), ['p33', 'p40']);
  assert.deepEqual(speciesOf(index, 'p99'), []);
});
