# Recovery Log — HOSEA (Wave F: the minor prophets)

Worker: lineation-recovery worker, Wave F. Date: 2026-10-18.

**Ruling cited:** Ruling 8 as amended by the editor 2026-10-18 — where the recorded apparatuses do not carry a chapter's divisions in full, the divisions may be read from the base's own pages (public-domain WEB Classic at ebible.org), wording asserted identical chapter by chapter, stop rule where a page does not speak plainly, base-prose chapters never relineated, no division invented.

**Scope:** Hosea chapters 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 (Lane C stopped set only; chapters 1 and 3 were base-prose skips in Lane C and were not touched).

**Method:** `python3 recovery.py HOSEA 2,4,5,6,7,8,9,10,11,12,13,14 --apply --readers-only` from `~/workspace/ceb-push/fix-pass`, then independent verification with `verify_recovery.py`. Writes confined to the two reader surfaces in staging (`books/`, `individual-books/`); no editions file touched; the live shelf not touched.

## Per-chapter dispositions (counts from fix-pass/recovery-results/HOSEA.json)

| Chapter | Disposition | q | q2 | m | qs |
|---|---|---|---|---|---|
| Hosea 2 | RESTORED | 29 | 48 | 0 | 0 |
| Hosea 4 | RESTORED | 23 | 36 | 0 | 0 |
| Hosea 5 | RESTORED | 18 | 31 | 0 | 0 |
| Hosea 6 | RESTORED | 13 | 21 | 0 | 0 |
| Hosea 7 | RESTORED | 20 | 34 | 0 | 0 |
| Hosea 8 | RESTORED | 14 | 29 | 0 | 0 |
| Hosea 9 | RESTORED | 17 | 40 | 0 | 0 |
| Hosea 10 | RESTORED | 15 | 33 | 0 | 0 |
| Hosea 11 | RESTORED | 13 | 26 | 0 | 0 |
| Hosea 12 | RESTORED | 13 | 27 | 0 | 0 |
| Hosea 13 | RESTORED | 15 | 36 | 0 | 0 |
| Hosea 14 | RESTORED | 9 | 23 | 0 | 0 |

No chapter in this book came back PAGE-PROSE or STOPPED. Hosea 12 restored cleanly, including at 12:8, where the editor disposition in staging ("iniquity" restored against the base's "sin" conversion) aligned without an ambiguous-alignment stop.

## Totals

RESTORED 12 / PAGE-PROSE 0 / STOPPED 0. Divisions restored: q 199, q2 384, m 0, qs 0 — 583 in all.

## Verification summary

`python3 verify_recovery.py --readers HOSEA:2,4,5,6,7,8,9,10,11,12,13,14` (run as part of the Wave F combined verification) returned **VERIFIED for all twelve chapters** (poetic=True, surfaces_identical=True, rederive_match=True on every chapter).
