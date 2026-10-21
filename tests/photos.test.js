import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { mkdtempSync, writeFileSync, mkdirSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const ROOT = new URL('..', import.meta.url).pathname;
// A 1×1 PNG.
const PNG = Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==', 'base64');
const src = () => { const d = mkdtempSync(join(tmpdir(), 'bugs-ph-')); const f = join(d, 'a.png'); writeFileSync(f, PNG); return f; };
const run = (...args) => JSON.parse(execFileSync('python3', ['tools/photos.py', 'add', src(), '--dry-run', ...args], { cwd: ROOT, encoding: 'utf8' }));
const SUBJ = ['--subject-zh', '袋蛾的袋子', '--subject-en', 'Bagworm bags', '--subject-ms', 'Bungkus ulat bungkus'];

test('an MPOB photo is credited in the agreed words, with issue and year', () => {
  const e = run('--id', 'metisa-plana-bags', ...SUBJ, '--licence', 'MPOB-permission', '--author', 'MPOB', '--url', 'https://palmoilis.mpob.gov.my/files/2021/05/Risalah-Sawit-no-34.pdf', '--source', 'RS34', '--issue', '34', '--year', '2018');
  assert.equal(e.file, 'img/species/metisa-plana-bags.webp');
  assert.equal(e.credit.zh, '照片：马来西亚棕油局（MPOB），引自《Risalah Sawit》第 34 期（2018）');
  assert.equal(e.credit.en, 'Photo: Malaysian Palm Oil Board (MPOB), from Risalah Sawit No. 34 (2018)');
  assert.equal(e.credit.ms, 'Foto: Lembaga Minyak Sawit Malaysia (MPOB), daripada Risalah Sawit Bil. 34 (2018)');
  assert.equal(e.source, 'RS34');
});
test('a CC photo is credited with author and licence', () => {
  const e = run('--id', 'plutella', ...SUBJ, '--licence', 'CC BY 4.0', '--author', 'Jane Doe', '--url', 'https://www.inaturalist.org/photos/1');
  assert.equal(e.credit.en, 'Photo: Jane Doe, CC BY 4.0');
  assert.equal(e.credit.zh, '照片：Jane Doe，CC BY 4.0');
  assert.equal(e.credit.ms, 'Foto: Jane Doe, CC BY 4.0');
});
test('a non-commercial licence is refused', () => {
  assert.throws(() => run('--id', 'x', ...SUBJ, '--licence', 'CC BY-NC 4.0', '--author', 'A', '--url', 'https://x'));
});
