# 昆虫 · Bugs · Serangga

An offline, trilingual (中文 / English / Bahasa Melayu) app for identifying
insects to order and learning Malaysia's farm insects: anatomy, life cycles,
the insect orders, common pests and helpful insects of oil palm, rice,
vegetables, fruit and cocoa, with sourced control methods, flashcards,
quizzes and exams. A static PWA: no build step, no npm dependencies, no CDN.

Built on the same shell as Meteorology and Plant Physiology (shared
`js/reader.js`, settings, update flow), and follows
[APP-STANDARDS](https://github.com/bryanwoo988/woobrothers.my/blob/main/APP-STANDARDS.md).

## Run it locally

```bash
python3 tools/serve.py 4190
```

Open <http://127.0.0.1:4190/>. The service worker is skipped on localhost
unless you add `?sw=1`. Browser tests: <http://127.0.0.1:4190/tests/>.

## Checks

```bash
node tools/lint-content.mjs   # every string in three languages, every block sourced
node tools/build-sw.mjs       # precache list + cache name; fails above 12 MB
node --test tests/*.test.js
```
