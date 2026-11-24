# Recovery Log — AMOS (Wave F: the minor prophets)

Worker: lineation-recovery worker, Wave F. Date: 2026-10-18.

**Ruling cited:** Ruling 8 as amended by the editor 2026-10-18 — where the recorded apparatuses do not carry a chapter's divisions in full, the divisions may be read from the base's own pages (public-domain WEB Classic at ebible.org), wording asserted identical chapter by chapter, stop rule where a page does not speak plainly, base-prose chapters never relineated, no division invented.

**Scope:** Amos chapters 1, 2, 3, 4, 5, 6, 8, 9 (Lane C stopped set only; chapter 7 was not in scope and was not touched).

**Method:** `python3 recovery.py AMOS 1,2,3,4,5,6,8,9 --apply --readers-only` from `~/workspace/ceb-push/fix-pass`, then independent verification with `verify_recovery.py`. Writes confined to the two reader surfaces in staging (`books/`, `individual-books/`); no editions file touched; the live shelf not touched.

## Per-chapter dispositions (counts from fix-pass/recovery-results/AMOS.json)

| Chapter | Disposition | q | q2 | m | qs |
|---|---|---|---|---|---|
| Amos 1 | RESTORED | 16 | 31 | 0 | 0 |
| Amos 2 | RESTORED | 16 | 33 | 0 | 0 |
| Amos 3 | RESTORED | 18 | 25 | 0 | 0 |
| Amos 4 | RESTORED | 14 | 29 | 0 | 0 |
| Amos 5 | RESTORED | 28 | 41 | 0 | 0 |
| Amos 6 | RESTORED | 11 | 27 | 0 | 0 |
| Amos 8 | RESTORED | 15 | 28 | 0 | 0 |
| Amos 9 | RESTORED | 4 | 9 | 0 | 0 |

No chapter in this book came back PAGE-PROSE or STOPPED.

## Totals

RESTORED 8 / PAGE-PROSE 0 / STOPPED 0. Divisions restored: q 122, q2 223, m 0, qs 0 — 345 in all.

## Verification summary

`python3 verify_recovery.py --readers AMOS:1,2,3,4,5,6,8,9` (run as part of the Wave F combined verification) returned **VERIFIED for all eight chapters** (poetic=True, surfaces_identical=True, rederive_match=True on every chapter).
