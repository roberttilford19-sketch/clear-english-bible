# Recovery Log — ACTS (Wave G: New Testament stopped set)

Worker: lineation-recovery worker, Wave G. Date: 2026-10-18.

**Ruling cited:** Ruling 8 as amended by the editor 2026-10-18 — where the recorded apparatuses do not carry a chapter's divisions in full, the divisions may be read from the base's own pages (public-domain WEB Classic at ebible.org), wording asserted identical chapter by chapter, stop rule where a page does not speak plainly, base-prose chapters never relineated, no division invented.

**Scope:** Acts chapters 1, 2, 4, 7, 8, 13, 15, 28. These chapters were stopped in Lane C-1 because the chapter apparatuses record the poetry locations (and, in chs. 15 and 28, counts) but do not record the divisions in full.

**Method:** `python3 recovery.py ACTS 1,2,4,7,8,13,15,28 --apply --readers-only` from `~/workspace/ceb-push/fix-pass`, then independent verification with `verify_recovery.py` for every chapter that did not come back STOPPED. Writes confined to the two reader surfaces in staging (`books/`, `individual-books/`); no editions file touched; the live shelf not touched.

## Per-chapter dispositions (counts from fix-pass/recovery-results/ACTS.json)

| Chapter | Disposition | q | q2 | m | qs |
|---|---|---|---|---|---|
| Acts 1 | RESTORED | 2 | 1 | 0 | 0 |
| Acts 2 | RESTORED | 11 | 13 | 0 | 0 |
| Acts 4 | RESTORED | 2 | 3 | 0 | 0 |
| Acts 7 | RESTORED | 6 | 5 | 0 | 0 |
| Acts 8 | STOPPED | — | — | — | — |
| Acts 13 | RESTORED | 3 | 5 | 0 | 0 |
| Acts 15 | STOPPED | — | — | — | — |
| Acts 28 | RESTORED | 5 | 8 | 0 | 0 |

**Acts 8 — STOPPED, reason verbatim:** "verse set mismatch: staged [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40] vs base [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]"

In plain terms: the staged chapter carries no verse 37, while the base page carries verse 37. The script's assertion (staged verse set == base verse set) failed before any rebuild, so nothing was written for this chapter. The stop was not overridden. For the coordinator's information only, the cached base page (recovery-cache/ACT08.htm) carries 2 q and 4 q2 divisions in the chapter (the Isaiah quotation at vv. 32–33), which remain unrestored pending a coordinator decision on the verse-set difference.

**Acts 15 — STOPPED, reason verbatim:** "verse set mismatch: staged [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 40, 41] vs base [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]"

In plain terms: the staged chapter carries no verse 34, while the base page carries verse 34. The script's assertion failed before any rebuild, so nothing was written for this chapter. The stop was not overridden.

## Apparatus-count comparisons

**Acts 15.** Lane C-1's log records for Acts 15 (vv. 15–17) a count only: **6 q divisions**, no line texts. The chapter itself STOPPED (verse-set mismatch above), so no restoration count exists to compare. The page's own class inventory, read directly from the cached base page (recovery-cache/ACT15.htm), is **6 q and 0 q2 — exact agreement with the apparatus count of 6 q.** The disagreement in this chapter is not about the divisions; it is the verse-set difference at v. 34, reported here, not smoothed.

**Acts 28.** Lane C-1's log records for Acts 28 (vv. 26–27) counts only: **5 q and 8 q2**, no line texts. The page-derived restoration gives **5 q and 8 q2 — exact agreement** with the apparatus counts.

## Verification summary

`python3 verify_recovery.py --readers ACTS:1,2,4,7,13,28` (the two STOPPED chapters excluded — nothing was written for them) returned **VERIFIED for all six restored chapters** (poetic=True, surfaces_identical=True, rederive_match=True on every chapter). No verse text affected by words-of-Jesus (wj) spans was observed in any read-back.

## Finisher addendum (2026-10-18) — Acts 8 and Acts 15 RESTORED under the editor's ruling

Ruling (dispositions log): Acts 8:37 and 15:34, verses carried only by the base, are treated as outside the staged text; both chapters restore around them (editor's own YES, 06:52 CDT). On the base pages both verses exist only as footnote popups (8:37 "TR adds Philip said…"; 15:34 "Some manuscripts add: But it seemed good to Silas to stay there.") — the verse markers stand with no verse body, and the parser's notemark stripping leaves an empty chunk list. Applied by `finish_recovery.py` (readers), transplanted serially by `editions_apply_recovery.py`, word-stream identity asserted on every surface before any write and whole-file after each splice.

- Acts 8 — RESTORED — 2 q, 4 q2 (the Isaiah quotation at vv. 32–33). Surfaces: both readers + catholic + protestant editions. Finisher finding: the staged chapter registers the omitted verse with a bare-number paragraph ('37') between vv. 36 and 38; carried through untouched.
- Acts 15 — RESTORED — 7 q segments at vv. 16–17 (the page carries 6 q blocks; the v. 16/17 boundary falls inside the "I will set it up" block, so the apparatus's 6 q agrees at block level). Surfaces: both readers + catholic + protestant editions. The bare-number paragraph ('34') between vv. 33 and 35 stands untouched.

Verification: `verify_recovery.py ACTS:8,15` (stock verifier) — VERIFIED for both chapters (surfaces identical, re-derivation match); `verify_finish.py` — VERIFIED for both. No word added or removed anywhere.
