# Release rule

Every change that ships to users adds an entry at the top of `data/releases.json`:
the new version number, today's date (YYYY-MM-DD), and what changed in plain
words for users, in every language the app supports. After the update the app
shows these notes once ("what's new" sheet: version, date, changes), and the
About/Settings screen shows the current version and the full history.

Version numbers: bug fixes bump the last digit, new features the middle one.

Shared standard for all of Bryan Woo's apps (including new ones):
https://github.com/bryanwoo988/woobrothers.my/blob/main/APP-STANDARDS.md

# Content rules

- Every markable block (paragraph, list, table, key-value, note, control) has `src`; `node tools/lint-content.mjs` must report 0 errors.
- Facts come from official or peer-reviewed sources. A source opened only through search summaries carries `"via": "search"` in `tools/content/sources.py`.
- Chinese names: where mainland and Taiwan differ, use `T2(zh, zh_tw, en, ms)`; the app shows `大陆名（大陆）／台湾名（台湾）`. Use a species-level Chinese name only when a source confirms it, otherwise a group name plus the scientific name.
- Control methods in IPM order: monitor → cultural → biological → chemical. Name an active ingredient only after checking its Malaysian status in `tools/content/pesticides.py`; banned ones are labelled, unknown ones may not ship.
- Photos: MPOB photos credit MPOB and the Risalah Sawit issue; other photos only CC0 / CC BY / CC BY-SA with author and licence. Never use a photo of another species in place of a missing one.
- Taxonomy: termites under Blattodea; Zygentoma (not Thysanura); Homoptera within Hemiptera; fishflies in Megaloptera.
- No book text, Taijiang photos or WTKhoo photos are copied; reference books (PDFs) never enter the repo.
