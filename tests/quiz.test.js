import { test } from 'node:test';
import assert from 'node:assert/strict';
import { scoreQuiz, questionsFor, cardsFor } from '../js/quiz.js';

const T = en => ({ zh: `中${en}`, en, ms: `M${en}` });
const quiz = [
  { stage: 3, chapter: 'p09', q: T('a'), options: [T('1'), T('2')], answer: 0 },
  { stage: 3, chapter: 'p09', q: T('b'), options: [T('1'), T('2')], answer: 1 },
  { stage: 1, chapter: 'p01', q: T('c'), options: [T('1'), T('2')], answer: 1 },
];
const terms = [
  { id: 'larva', name: T('larva'), short: T('x'), chapter: 9 },
  { id: 'head', name: T('head'), short: T('x'), chapter: 1 },
  { id: 'elytra', name: T('elytra'), short: T('x'), chapter: 10 },
];
const stages = [{ n: 1, chapters: ['p01'] }, { n: 3, chapters: ['p09'] }, { n: 4, chapters: ['p10'] }];

test('score counts right answers; unanswered is wrong', () => {
  const qs = [{ answer: 0 }, { answer: 2 }, { answer: 1 }];
  assert.deepEqual(scoreQuiz([0, 1, undefined], qs), { correct: 1, total: 3 });
});
test('questions for a stage come from that stage only', () => {
  assert.deepEqual(questionsFor(quiz, 3).map(q => q.q.en), ['a', 'b']);
  assert.deepEqual(questionsFor(quiz, 10), []);
});
test('flashcards for a stage are the terms taught in its pages', () => {
  assert.deepEqual(cardsFor(terms, stages, 3).map(c => c.id), ['larva']);
  assert.deepEqual(cardsFor(terms, stages, 1).map(c => c.id), ['head']);
  assert.deepEqual(cardsFor(terms, stages, 4).map(c => c.id), ['elytra']);
});
