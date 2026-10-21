import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, mkdirSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { build } from '../tools/build-sw.mjs';

const SW = "/* --- generated:begin --- */\nconst CACHE = 'x';\n/* --- generated:end --- */\n";

function tree(bytes) {
  const root = mkdtempSync(join(tmpdir(), 'bugs-sw-'));
  mkdirSync(join(root, 'img'));
  writeFileSync(join(root, 'index.html'), '<!doctype html>');
  writeFileSync(join(root, 'sw.js'), SW);
  writeFileSync(join(root, 'img', 'big.bin'), Buffer.alloc(bytes));
  return root;
}

test('build-sw precaches img/ and names the cache bugs-<hash>', () => {
  const r = build(tree(1000));
  assert.ok(r.files.includes('img/big.bin'));
  assert.match(r.cache, /^bugs-[0-9a-f]{10}$/);
  assert.equal(r.ok, true);
});

test('build-sw fails above the 12 MB budget', () => {
  const r = build(tree(13 * 1048576));
  assert.equal(r.ok, false);
});
