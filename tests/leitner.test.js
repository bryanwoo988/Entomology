import { test } from 'node:test';
import assert from 'node:assert/strict';
import { review, dueCards, BOXES, INTERVAL_DAYS } from '../js/leitner.js';

const TODAY = '2026-10-21';

test('five boxes with growing intervals', () => {
  assert.equal(BOXES, 5);
  assert.deepEqual(INTERVAL_DAYS, [0, 1, 3, 7, 14]);
});
test('a new card answered right moves to box 2, due tomorrow', () => {
  assert.deepEqual(review({}, 'a', true, TODAY).a, { box: 2, due: '2026-10-22' });
});
test('a wrong answer sends a card back to box 1, due today', () => {
  assert.deepEqual(review({ a: { box: 4, due: TODAY } }, 'a', false, TODAY).a, { box: 1, due: TODAY });
});
test('box 5 is the top', () => {
  assert.deepEqual(review({ a: { box: 5, due: TODAY } }, 'a', true, TODAY).a, { box: 5, due: '2026-11-04' });
});
test('review does not change the state it was given', () => {
  const s = { a: { box: 2, due: TODAY } };
  review(s, 'a', true, TODAY);
  assert.deepEqual(s, { a: { box: 2, due: TODAY } });
});
test('due cards: unseen and box 1 first, then by due date; future cards left out', () => {
  const state = { b3: { box: 3, due: TODAY }, b1: { box: 1, due: '2026-10-20' }, later: { box: 2, due: '2026-10-22' } };
  assert.deepEqual(dueCards(state, ['b3', 'later', 'new', 'b1'], TODAY), ['new', 'b1', 'b3']);
});
