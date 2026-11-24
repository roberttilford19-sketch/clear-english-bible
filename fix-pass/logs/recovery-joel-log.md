# Recovery Log — JOEL (Wave F: the minor prophets)

Worker: lineation-recovery worker, Wave F. Date: 2026-10-18.

**Ruling cited:** Ruling 8 as amended by the editor 2026-10-18 — where the recorded apparatuses do not carry a chapter's divisions in full, the divisions may be read from the base's own pages (public-domain WEB Classic at ebible.org), wording asserted identical chapter by chapter, stop rule where a page does not speak plainly, base-prose chapters never relineated, no division invented.

**Scope:** Joel chapters 1, 2, 3 (the whole Lane C stopped set for this book).

**Method:** `python3 recovery.py JOEL 1,2,3 --apply --readers-only` from `~/workspace/ceb-push/fix-pass`, then independent verification with `verify_recovery.py`. Writes confined to the two reader surfaces in staging (`books/`, `individual-books/`); no editions file touched; the live shelf not touched.

## Per-chapter dispositions (counts from fix-pass/recovery-results/JOEL.json)

| Chapter | Disposition | q | q2 | m | qs |
|---|---|---|---|---|---|
| Joel 1 | RESTORED | 21 | 40 | 0 | 0 |
| Joel 2 | RESTORED | 39 | 81 | 0 | 0 |
| Joel 3 | RESTORED | 22 | 50 | 0 | 0 |

No chapter in this book came back PAGE-PROSE or STOPPED.

## Totals

RESTORED 3 / PAGE-PROSE 0 / STOPPED 0. Divisions restored: q 82, q2 171, m 0, qs 0 — 253 in all.

## Verification summary

`python3 verify_recovery.py --readers JOEL:1,2,3` (run as part of the Wave F combined verification) returned **VERIFIED for all three chapters** (poetic=True, surfaces_identical=True, rederive_match=True on every chapter).
