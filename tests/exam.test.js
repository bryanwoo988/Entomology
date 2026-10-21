import { test } from 'node:test';
import assert from 'node:assert/strict';
import { drawExam, scoreItem, scoreExam, itemId } from '../js/exam.js';

const T = en => ({ zh: `中${en}`, en, ms: `M${en}` });
const mc = (n, stage = 1) => ({ type: 'mc', stage, chapter: `p0${stage}`, q: T(`q${n}`), options: [T('a'), T('b'), T('c')], answer: 1 });
const items = Array.from({ length: 12 }, (_, i) => mc(i, (i % 3) + 1));
const match = { type: 'match', stage: 1, chapter: 'p01', q: T('pair them'), pairs: [{ left: T('A'), right: T('1') }, { left: T('B'), right: T('2') }, { left: T('C'), right: T('3') }] };
const tf = { stage: 1, chapter: 'p01', q: T('true?'), options: [T('True'), T('False')], answer: 0 };

test('the same seed draws the same exam', () => {
  assert.deepEqual(drawExam(items, { count: 5, seed: 7 }).map(itemId), drawExam(items, { count: 5, seed: 7 }).map(itemId));
});
test('a draw has no duplicates and is capped at what exists', () => {
  const d = drawExam(items, { count: 50, seed: 1 });
  assert.equal(d.length, 12);
  assert.equal(new Set(d.map(itemId)).size, 12);
});
test('a draw can be limited to stages', () => {
  assert.ok(drawExam(items, { count: 50, stages: [2], seed: 3 }).every(q => q.stage === 2));
});
test('multiple choice and true/false score by index; untyped items are mc', () => {
  assert.equal(scoreItem(mc(1), 1), true);
  assert.equal(scoreItem(mc(1), 0), false);
  assert.equal(scoreItem(tf, 0), true);
});
test('a match item is right only if every pair is right', () => {
  assert.equal(scoreItem(match, [0, 1, 2]), true);
  assert.equal(scoreItem(match, [1, 0, 2]), false);
  assert.equal(scoreItem(match, [0, 1]), false);
});
test('scoreExam counts and lists the wrong items', () => {
  const qs = [mc(1), mc(2), match];
  const r = scoreExam(qs, [1, 0, [0, 1, 2]]);
  assert.deepEqual(r, { correct: 2, total: 3, wrongIds: [itemId(mc(2))] });
});
test('itemId is stable and differs between questions', () => {
  assert.equal(itemId(mc(1)), itemId(mc(1)));
  assert.notEqual(itemId(mc(1)), itemId(mc(2)));
});
