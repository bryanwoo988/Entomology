import { test } from 'node:test';
import assert from 'node:assert/strict';
import { displayName, allNames } from '../js/names.js';

test('different Taiwan name is shown with both labels', () => {
  assert.equal(displayName({ zh: '蝽', zhTw: '椿象', en: 'Stink bug', ms: 'Kepinding' }, 'zh'), '蝽（大陆）／椿象（台湾）');
});
test('no Taiwan name shows the mainland name alone', () => {
  assert.equal(displayName({ zh: '瓢虫', en: 'Ladybird', ms: 'Kumbang kura-kura' }, 'zh'), '瓢虫');
});
test('same name in both places shows it once', () => {
  assert.equal(displayName({ zh: '蜻蜓', zhTw: '蜻蜓', en: 'Dragonfly', ms: 'Pepatung' }, 'zh'), '蜻蜓');
});
test('other languages ignore zhTw', () => {
  assert.equal(displayName({ zh: '蝽', zhTw: '椿象', en: 'Stink bug', ms: 'Kepinding' }, 'en'), 'Stink bug');
});
test('allNames lists every variant once', () => {
  assert.deepEqual(allNames({ zh: '蝽', zhTw: '椿象', en: 'Stink bug', ms: 'Kepinding' }).sort(), ['Kepinding', 'Stink bug', '椿象', '蝽'].sort());
});
