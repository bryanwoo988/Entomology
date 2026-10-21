import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { PARTS } from '../js/widgets/anatomy.js';

const svg = readFileSync(new URL('../img/svg/anatomy.svg', import.meta.url), 'utf8');
const parts = [...svg.matchAll(/data-part="([a-z-]+)"/g)].map(m => m[1]);

test('the diagram has exactly one hotspot per part', () => {
  assert.deepEqual([...parts].sort(), [...PARTS].sort());
  assert.equal(new Set(parts).size, parts.length);
});

test('every part is a glossary term', { todo: 'terms are written in Task 9' }, () => {
  const terms = new Set(JSON.parse(readFileSync(new URL('../data/terms.json', import.meta.url), 'utf8')).map(t => t.id));
  for (const p of PARTS) assert.ok(terms.has(p), p);
});
