import { test } from 'node:test';
import assert from 'node:assert/strict';
import { statusLabel, aiLabel } from '../js/pesticides.js';

const banned = { id: 'endosulfan', name: { zh: '硫丹', en: 'Endosulfan', ms: 'Endosulfan' }, status: 'banned' };
const ok = { id: 'cypermethrin', name: { zh: '氯氰菊酯', en: 'Cypermethrin', ms: 'Sipermetrin' }, status: 'registered' };

test('status labels in three languages', () => {
  assert.equal(statusLabel('banned', 'zh'), '已禁用');
  assert.equal(statusLabel('banned', 'en'), 'Banned');
  assert.equal(statusLabel('banned', 'ms'), 'Diharamkan');
  assert.equal(statusLabel('registered', 'en'), '');
});
test('a banned ingredient is never named without its label', () => {
  assert.equal(aiLabel(banned, 'zh'), '硫丹（已禁用）');
  assert.equal(aiLabel(banned, 'en'), 'Endosulfan (Banned)');
  assert.equal(aiLabel(ok, 'ms'), 'Sipermetrin');
});
test('a pesticide with a Taiwan name shows both, then the banned tag', () => {
  const p = { name: { zh: '克百威', zhTw: '加保扶', en: 'Carbofuran', ms: 'Karbofuran' }, status: 'banned' };
  assert.equal(aiLabel(p, 'zh'), '克百威（大陆）／加保扶（台湾）（已禁用）');
  assert.equal(aiLabel(p, 'en'), 'Carbofuran (Banned)');
});
