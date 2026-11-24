# Recovery Log — ROMANS (Wave G: New Testament stopped set)

Worker: lineation-recovery worker, Wave G. Date: 2026-10-18.

**Ruling cited:** Ruling 8 as amended by the editor 2026-10-18 — where the recorded apparatuses do not carry a chapter's divisions in full, the divisions may be read from the base's own pages (public-domain WEB Classic at ebible.org), wording asserted identical chapter by chapter, stop rule where a page does not speak plainly, base-prose chapters never relineated, no division invented.

**Scope:** Romans chapters 3, 4, 8, 9, 10, 11, 14, 15 (chapter 12 was restored by the pilot and was not re-run). These chapters were stopped in Lane C-1 because the chapter apparatuses record the poetry locations (and, in chs. 14 and 15, counts) but do not record the divisions in full.

**Method:** `python3 recovery.py ROMANS 3,4,8,9,10,11,14,15 --apply --readers-only` from `~/workspace/ceb-push/fix-pass`, then independent verification with `verify_recovery.py`. Writes confined to the two reader surfaces in staging (`books/`, `individual-books/`); no editions file touched; the live shelf not touched.

## Per-chapter dispositions (counts from fix-pass/recovery-results/ROMANS.json)

| Chapter | Disposition | q | q2 | m | qs |
|---|---|---|---|---|---|
| Romans 3 | RESTORED | 9 | 9 | 0 | 0 |
| Romans 4 | RESTORED | 2 | 1 | 0 | 0 |
| Romans 8 | RESTORED | 1 | 1 | 0 | 0 |
| Romans 9 | RESTORED | 6 | 7 | 0 | 0 |
| Romans 10 | RESTORED | 4 | 4 | 0 | 0 |
| Romans 11 | RESTORED | 6 | 6 | 0 | 0 |
| Romans 14 | RESTORED | 1 | 1 | 0 | 0 |
| Romans 15 | RESTORED | 5 | 5 | 0 | 0 |

No chapter in this book came back PAGE-PROSE or STOPPED.

## Apparatus-count comparison — Romans 15

Lane C-1's log records for Romans 15 (vv. 9–12, 21) per-verse counts only: **10 divisions in all**, no line texts. The page-derived restoration gives 5 q + 5 q2 = **10 divisions — exact agreement** with the apparatus total. (For completeness, Romans 14's apparatus counts, 1 q and 1 q2, also match the restoration exactly: 1 q, 1 q2.)

## Verification summary

`python3 verify_recovery.py --readers ROMANS:3,4,8,9,10,11,14,15` returned **VERIFIED for all eight chapters** (poetic=True, surfaces_identical=True, rederive_match=True on every chapter). No verse text affected by words-of-Jesus (wj) spans was observed in any read-back.
