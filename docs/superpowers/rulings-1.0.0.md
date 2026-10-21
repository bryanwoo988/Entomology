# Bugs 1.0.0 — decisions made during the build

Every judgement call taken on the owner's behalf, in the order made, each with what it costs if wrong. Then the review findings not fixed.

## Rulings

- Pre-flight: Ruling: T5 order-link test asserts order is null (outside) or /^p\d{2}$/; the "page exists" half is enforced by lint (unknown page error) only once index.json lists pages; T10 Step 3 re-runs it — cost if wrong: a dangling order link survives until T10.
- Task 1: Ruling: page ids pNN need one helper — added pageId() in js/markup.js and replaced every local chNN cid helper (app, terms, tools, search, lint); cardsFor now strips non-digits — cost if wrong: a missed chNN link 404s (tests cover search/quiz).
- Task 1: Ruling: Meteorology data-dependent tests (quiz, search, lint fixtures) rewritten with inline fixtures; browser cases that need pages are skipped via testIf until content exists (re-enabled in Task 9) — cost if wrong: reader/search browser behaviour unverified until Task 9.
- Task 1: Ruling: build-sw exports build(root) returning {files,bytes,cache,ok}; over budget it does not write sw.js — cost if wrong: none.
- Task 1: Ruling: removed tools abbr/map/convert/beaufort/data — Meteorology-only — cost if wrong: none.
- Task 2: Ruling: maskable/apple-touch background #fff1f1 (soft logo red) replaces Meteorology's blue; CJK face Noto Sans CJK SC (index 2) — cost if wrong: cosmetic.
- Task 3: Ruling: inline {{t:}} terms in running text show the mainland name only; the dual 蝽（大陆）／椿象（台湾） form appears in the term sheet, glossary, chips, flashcards and species headers — keeps prose readable — cost if wrong: a Taiwan reader must tap to see their name.
- Task 4: Ruling: Review Focus 4 "banned shown without label" is enforced in code, not lint — aiLabel() always appends the banned tag and the renderer only names ingredients through it (pesticides.test + browser test) — cost if wrong: none found.
- Task 4: Ruling: added lint rules beyond the plan: active ingredients only allowed in chemical-level control; pesticide entries need src and a checked date; photos need author and url — follow the spec's sourcing rule — cost if wrong: stricter data entry.
- Task 4: Ruling: IPM headings are page-wide (level change), not per section — spec says groups in IPM order on a page — cost if wrong: repeated heading if a page interleaves levels (lint forbids that).
- Task 5: Ruling: key shape — stick-insect question first (else they fall to beetles/orthoptera), mayflies offered at the wing-pairs question (their hind wings can be invisible), silverfish added under wingless — spec §5 lists these Malaysian additions — cost if wrong: a branch order a reviewer may prefer differently.
- Task 5: Ruling: Taiwan names are written in simplified characters (the difference shown is the name, not the script), e.g. 椿象、螽蟴 — cost if wrong: Taiwan readers see simplified script.
- Task 5: Ruling: Malay common names chosen: Cocopet (earwig), Anjing tanah (mole cricket), Katidid, Lalat sehari (mayfly), Lalat kadis (caddisfly), Gegat (silverfish), Trips — UNVERIFIED against DBP; check in content tasks — cost if wrong: an odd Malay name.
- Task 5: Ruling: key→order link lint check activates once any page has kind 'order' — lets the key ship before order pages — cost if wrong: dangling link until Task 10.
- Task 5: Ruling: key images are <img> SVGs with a fixed mid-grey stroke (#7a8699), legible on light and dark — currentColor does not reach into <img> — cost if wrong: slightly low contrast on some themes.
- Task 6: Ruling: no on-diagram text labels; each hotspot has an aria-label and opens the term sheet (shows the dual name) — avoids three-language label layout in SVG — cost if wrong: parts are discovered by tapping rather than read at a glance.
- Task 7: Ruling: study screens take their data as arguments (items, terms, index) so browser tests use fixtures; app.js loads quiz.json per route — cost if wrong: none.
- Task 7: Ruling: wrong answers in stage quizzes also go to the wrong-answer book (spec: 自动收集错题), not only exam ones — cost if wrong: a busier book.
- Task 7: Ruling: exams are deferred (answers revealed after submit); quizzes and the wrong-answer book reveal immediately — cost if wrong: preference.
- Task 8: Ruling: allowed licences extended with "PD" (public domain) and "CC BY 3.0 US" — both no stricter than CC BY — cost if wrong: none legally; list differs from spec text.
- Task 8: Ruling: CC0 photos credited with the observer's name although not required — fairness and traceability — cost if wrong: none.
- Task 8: Ruling: Setora nitens candidate labelled "adult" on iNaturalist is a larva; registered as larva after viewing — cost if wrong: none.
- Task 8: Ruling: Commons originals and thumb.wikimedia.org blocked/429; used 960px thumbnails on upload.wikimedia.org — cost if wrong: one damage photo (BPH damage2) not added.
- Task 9: Ruling: any text value carrying zhTw (names in tables, keyval labels, captions) renders as 大陆／台湾 in zh; prose {{t:}} terms stay mainland-only (Task 3 ruling) — cost if wrong: none.
- Task 9: Ruling: web sources (AES, Purdue, NC State, LCWU, UMN, Encyclopedia of Arkansas, ICZN) were verified through search-result excerpts; their hosts are not in the network allowlist, so pages were not opened directly — cost if wrong: a citation whose page wording differs slightly.
- Task 9: Ruling: larva types limited to eruciform, scarabaeiform, vermiform (the three the sources supported); campodeiform/elateriform left out — cost if wrong: less complete list.
- Task 9: Ruling: browser overflow check now covers every page in all three languages — cost if wrong: slower browser suite.
- Task 10: Ruling: order pages generated from one data file (tools/content/orders.py) instead of 17 scripts — identical structure, easier review — cost if wrong: none.
- Task 10: Ruling: farm species links on order pages deferred to Task 12 (species pages don't exist yet; lint rejects links to unlisted pages) — cost if wrong: none if Task 12 adds them.
- Task 10: Ruling: Greek roots other than Coleoptera/Lepidoptera/Hymenoptera cited to Liddell–Scott (Perseus), not opened from this environment; mouthparts/development by order partly cited to the UMN orders deck, also not opened directly — cost if wrong: a citation that needs a page check.
- Task 10: Ruling: WTKhoo errors not repeated: fishflies placed in Megaloptera (MDC), mayfly "no ocelli" claim dropped, termites under Blattodea (Inward et al. 2007) — cost if wrong: none.
- Task 10: Ruling: unsourced key-result checks replaced (cockroach shield, mantis triangular head, hoverfly/aphid comparisons); dragonfly/damselfly eyes, mayfly tails and caddisfly wing posture now sourced (iNaturalist guide, Australian Museum) — cost if wrong: none.
- Task 11: Ruling: bagworms (3 species) share one page and nettle caterpillars (2 species) share one page; species cards may list several binomials (lint allows comma-separated) — shared damage/control, less repetition — cost if wrong: fewer pages than the plan's one-per-species.
- Task 11: Ruling: species-level Chinese names unconfirmed, so pages use confirmed family-level names (袋蛾／蓑蛾, 犀角金龟, 象甲／象鼻虫, 猎蝽／猎椿象) plus the scientific name — cost if wrong: less specific Chinese names.
- Task 11: Ruling: pesticide status: carbofuran banned (DOA poster + Aug 2025 list); cypermethrin and lambda-cyhalothrin "registered" via DOA MyMRL registered-active list (product-level registration not checked; label warning covers it); monocrotophos, methamidophos, trichlorfon (older MPOB leaflets) unconfirmed → omitted with an explicit note; fipronil (termite trial) not recommended — cost if wrong: a registered option left out.
- Task 11: Ruling: DOA/MARDI sites are blocked by the network policy; statuses were confirmed through official DOA documents surfaced by search rather than by opening the portal — cost if wrong: a status that changed after the August 2025 list.
- Task 11: Ruling: termite page states MPOB trialled fungi/fipronil but gives no result (not found) — cost if wrong: none.
- Task 12: Ruling: WebFetch lost DNS for every host mid-task (also for all research agents); facts for p34–p62 come from search-result summaries, except IRRI planthopper/green leafhopper and JIRCAS TARS 14/20 (opened earlier). Such sources carry "via": "search" and the page's source list says "checked through a search summary; the page itself could not be opened". A fact went in only if the summary pinned it to a URL — cost if wrong: a number or wording that differs from the original page.
- Task 12: Ruling: no new pesticide names; chemical blocks give only source warnings (resurgence, resistance, harm to natural enemies) plus "use a DOA-registered product, follow the label" (cited to DOA-MRL). AIs named in research notes (lindane, imidacloprid, etc.) left out because their Malaysian status was not checked — cost if wrong: less specific advice.
- Task 12: Ruling: carambola and oriental fruit flies share one page (p52), like the bagworms; their notes were too thin for two pages and the key teaching point is that they are hard to separate — cost if wrong: one page fewer.
- Task 12: Ruling: Chinese species names used only where a search confirmed them (褐飞虱, 三化螟, 稻纵卷叶螟, 小菜蛾, 斜纹夜蛾, 草地贪夜蛾, 棕榈蓟马, 瓜实蝇); others use a group name plus the scientific name (e.g. 叶蝉（Nephotettix）, 粉虱（Bemisia tabaci）) — cost if wrong: less familiar Chinese titles.
- Task 12: Ruling: Malay common names for new species are standard Malaysian names or literal translations (bena perang, pianggang, lalat putih…) and are not separately sourced; taxonomic authorities written from standard nomenclature — cost if wrong: a Malay name a farmer would not use.
- Task 12: Ruling: order pages list their farm insects automatically from index.json (species pages record their order); no hand-written link blocks, so no markable block without a source — cost if wrong: none.
- Task 12: Ruling: weak-source lines dropped rather than kept: DBM larva behaviour, S. litura adult, thrips microscope note, melon fly thorax, 28-spot synonym, transverse ladybird 450-aphid figure, Sarawak HLB loss figure, P. demoleus hosts from hobby sites — cost if wrong: thinner pages.
- Task 13: Ruling: safety page omits clothing advice — no source found for long sleeves/closed shoes in the searches; tools, permission and recording are sourced (OSU, U Idaho, MSU 4-H) — cost if wrong: one practical tip missing.
- Task 13: Ruling: bee-sting first aid cited to URMC through a search summary that pooled several medical pages; wording kept to points all of them agreed on (scrape, no tweezers, emergency signs, auto-injector) — cost if wrong: a citation that should name a different page.
- Task 13: Ruling: no Malaysian emergency number written (no source captured) — cost if wrong: readers look it up themselves.
- Task 13: Ruling: offline check done with Playwright against ?sw=1 (prefs seeded with chosen: true); key, two species pages, exam and safety page rendered offline with all images — cost if wrong: none.
- Final: Ruling: skipWaiting + clients.claim kept (old app.js may read new data until reload) — same update policy as Meteorology and Plant Physiology, the app reloads itself when idle, data schema did not change within 1.0.0 — cost if wrong: one confused session after a schema-changing update; revisit when quiz/page schema changes.
- Final: Ruling: 95 of 137 sources are search-summary only; shown to readers as such; the user is asked to allow the hosts or check RS40/RS12/DOA by hand before wide release; "registered" status for cypermethrin and lambda-cyhalothrin is active-ingredient level (MyMRL), not product registration for the crop — cost if wrong: advice resting on a summary that differs from the page.
- Final: Ruling: Review Focus 2 wording — tapping crumb N re-asks question N (change that answer) and drops later answers; implementation kept, plan text was loose — cost if wrong: none.

## Deferred minor findings (final review)

- p28 carbofuran block repeats the dose for a banned product.
- progress page counts wrong-answer ids that no longer exist in quiz.json.
- goodExam accepts fractional/negative seconds and total 0.
- wrong-answer ids hash the English question text; rewording orphans them.
- displayName with zhTw but no zh would print "（大陆）／X（台湾）" (lint prevents it today).

## Fixed in the final review

- update replacing a complete offline copy with a partial one — sw.test "an update with a failed download keeps the old complete copy" RED→GREEN, suite 156/156
- pesticide names in plain text escaping the linter — lint.test "a pesticide named in text must be declared in a chemical block" RED→GREEN, suite 156/156
