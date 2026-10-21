import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { walk, answerAt, encode, decode, validate } from '../js/key.js';

const key = JSON.parse(readFileSync(new URL('../data/key.json', import.meta.url), 'utf8'));

// Follow option labels (English, by prefix) so the test survives reordering.
function path(...labels) {
  const out = [];
  let node = key.start;
  for (const l of labels) {
    const i = key.nodes[node].options.findIndex(o => o.label.en.startsWith(l));
    assert.ok(i >= 0, `no option "${l}" at ${node}`);
    out.push(i);
    node = key.nodes[node].options[i].next;
  }
  return out;
}
const LADYBIRD = path('No', 'Yes', 'Two pairs', 'No scales', 'No', 'No', 'Different', 'No', 'Yes');

test('ladybird path ends at beetles', () => {
  assert.equal(walk(key, LADYBIRD).result, 'beetles');
});
test('a partial path stops at the next question', () => {
  const r = walk(key, LADYBIRD.slice(0, 3));
  assert.equal(r.result, undefined);
  assert.equal(r.node, 'scales');
  assert.equal(r.path.length, 3);
});
test('changing an earlier answer drops the later ones', () => {
  const a = answerAt(LADYBIRD, 2, 0);
  assert.equal(a.length, 3);
  assert.notEqual(walk(key, a).result, 'beetles');
});
test('answers past a result are ignored', () => {
  const r = walk(key, [0, 1, 1, 1]);
  assert.equal(r.result, 'phasmids');
  assert.equal(r.path.length, 1);
});
test('an out-of-range answer stops at that question', () => {
  const r = walk(key, [1, 99]);
  assert.equal(r.node, 'wings');
  assert.equal(r.path.length, 1);
});
test('"none of these" ends outside the key', () => {
  const last = key.nodes[key.start].options.length - 1;
  assert.equal(walk(key, [last]).result, 'outside');
});
test('decode rejects junk', () => {
  assert.deepEqual(decode('1.x'), []);
  assert.deepEqual(decode(''), []);
  assert.deepEqual(decode(undefined), []);
});
test('encode/decode round-trip', () => assert.deepEqual(decode(encode([0, 1, 1])), [0, 1, 1]));
test('the shipped key is valid', () => assert.deepEqual(validate(key), []));
test('validate finds a dangling next, a cycle and an unreachable node', () => {
  const bad = { start: 'a', nodes: {
    a: { q: {}, options: [{ label: {}, next: 'b' }, { label: {}, next: 'ghost' }] },
    b: { q: {}, options: [{ label: {}, next: 'a' }] },
    lonely: { q: {}, options: [{ label: {}, result: 'r' }] },
  }, results: { r: {} } };
  const errs = validate(bad).join('\n');
  assert.match(errs, /ghost/);
  assert.match(errs, /cycle/);
  assert.match(errs, /lonely.*unreachable/);
});
test('every result except outside points at an order page id', () => {
  for (const [id, r] of Object.entries(key.results)) {
    if (id === 'outside') assert.equal(r.order, null);
    else assert.match(r.order, /^p\d{2}$/, id);
  }
});
