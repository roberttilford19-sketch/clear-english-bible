# Recovery Log — MICAH (Wave F: the minor prophets)

Worker: lineation-recovery worker, Wave F. Date: 2026-10-18.

**Ruling cited:** Ruling 8 as amended by the editor 2026-10-18 — where the recorded apparatuses do not carry a chapter's divisions in full, the divisions may be read from the base's own pages (public-domain WEB Classic at ebible.org), wording asserted identical chapter by chapter, stop rule where a page does not speak plainly, base-prose chapters never relineated, no division invented.

**Scope:** Micah chapters 1, 2, 3, 4, 5, 6, 7 (the whole Lane C stopped set for this book).

**Method:** `python3 recovery.py MICAH 1,2,3,4,5,6,7 --apply --readers-only` from `~/workspace/ceb-push/fix-pass`, then independent verification with `verify_recovery.py`. Writes confined to the two reader surfaces in staging (`books/`, `individual-books/`); no editions file touched; the live shelf not touched.

## Per-chapter dispositions (counts from fix-pass/recovery-results/MICAH.json)

| Chapter | Disposition | q | q2 | m | qs |
|---|---|---|---|---|---|
| Micah 1 | RESTORED | 22 | 29 | 0 | 0 |
| Micah 2 | RESTORED | 17 | 29 | 0 | 0 |
| Micah 3 | RESTORED | 12 | 31 | 0 | 0 |
| Micah 4 | RESTORED | 17 | 39 | 0 | 0 |
| Micah 5 | RESTORED | 17 | 31 | 0 | 0 |
| Micah 6 | RESTORED | 19 | 33 | 0 | 0 |
| Micah 7 | RESTORED | 25 | 48 | 0 | 0 |

No chapter in this book came back PAGE-PROSE or STOPPED.

## Totals

RESTORED 7 / PAGE-PROSE 0 / STOPPED 0. Divisions restored: q 129, q2 240, m 0, qs 0 — 369 in all.

## Verification summary

`python3 verify_recovery.py --readers MICAH:1,2,3,4,5,6,7` (run as part of the Wave F combined verification) returned **VERIFIED for all seven chapters** (poetic=True, surfaces_identical=True, rederive_match=True on every chapter).
