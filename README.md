# 昆虫 · Bugs · Serangga

An offline, trilingual (中文 / English / Bahasa Melayu) app for identifying
insects to order and learning Malaysia's farm insects. A static PWA: no build
step, no npm dependencies, no CDN.

Live: <https://bryanwoo988.github.io/Entomology/>

## What is in it

- **63 pages in 6 stages**:
  1. Meeting the insects.
  2. Classifying and identifying.
  3. Life cycles.
  4. The insect orders: 17 pages with name origins, memory aids, look-alikes and quizzes.
  5. Malaysia's farm insects: oil palm, rice, vegetables, fruit, cocoa and pollinators. That is 30 species pages and 6 crop overviews, with control methods in IPM order.
  6. Watching insects safely.
- **Step-by-step identification key** (`#/key`). It is based on the
  Taijiang insect guide (pp. 38–40) and extended for Malaysia. Every answer can be
  changed; every result links to its order page. Order pages list the farm
  insects in that order.
- **Photos**: 14 from MPOB (used with permission, credited to MPOB) and 36
  open-licence photos (CC0 / CC BY / CC BY-SA, mostly iNaturalist). Every
  photo has its credit and link on its page and in About.
- **Chinese names** show mainland and Taiwan forms where they differ:
  `蝽（大陆）／椿象（台湾）`. Both forms are searchable.
- **Pesticides**: only active ingredients whose Malaysian status was checked;
  banned ones are labelled 已禁用 / Banned / Diharamkan. Unknown status may not
  ship.
- **Study tools**:
  - Glossary and flashcards (5-box Leitner).
  - Stage quizzes and timed exams.
  - A wrong-answer book that fills itself.
  - A progress page.
- **Highlights, notes, bookmarks and read-aloud** (`js/reader.js`, shared with
  the sibling apps).
- **House conventions**:
  - First-run language picker (default English).
  - Settings: System / Light / Dark with four light and four dark looks, and text size.
  - About: version, update history, QR code and share link.
  - Offline after the first visit. Updates are offered, never forced, with a "what's new" sheet.

## Sources

Every markable block on every page cites its source, and each page lists its
sources at the end. About lists all sources and all photo credits. A source
marked "checked through a search summary" could not be opened from the build
environment; its facts were taken from search-result summaries that named the
page. The Taijiang guide and the WTKhoo notes are cited by page. No book text
and no photos from them are copied, and reference books never enter this
repository. See `docs/sources-log.md`.

## Run it locally

```bash
python3 tools/serve.py 4190
```

Open <http://127.0.0.1:4190/>. The service worker is skipped on localhost
unless you add `?sw=1`. Browser tests: <http://127.0.0.1:4190/tests/>.

## Editing content

Pages are generated: edit `tools/content/*.py` (one script per page or crop
group, helpers in `build.py`, sources in `sources.py`) and run it, for example
`python3 tools/content/rice.py`. That rewrites `data/pNN.json`, `terms.json`,
`quiz.json`, `sources.json` and `index.json`. Photos are added with
`tools/photos.py add …`.

## Checks

```bash
node tools/lint-content.mjs   # three languages, every block sourced, IPM order, pesticide status, licences
node tools/build-sw.mjs       # precache list + cache name; fails above 12 MB
node --test tests/*.test.js
node tools/verify-qr.mjs      # the QR code decodes to the live URL
```

## Deploy

GitHub Pages serves the `main` branch. Before merging, add a release entry
(see `CLAUDE.md`) and run the checks above, including `tools/build-sw.mjs`.
That script refreshes the cache name so installed copies offer the update.
