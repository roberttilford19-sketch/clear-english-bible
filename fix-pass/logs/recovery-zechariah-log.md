# Recovery Log — ZECHARIAH (Wave F: the minor prophets)

Worker: lineation-recovery worker, Wave F. Date: 2026-10-18.

**Ruling cited:** Ruling 8 as amended by the editor 2026-10-18 — where the recorded apparatuses do not carry a chapter's divisions in full, the divisions may be read from the base's own pages (public-domain WEB Classic at ebible.org), wording asserted identical chapter by chapter, stop rule where a page does not speak plainly, base-prose chapters never relineated, no division invented.

**Scope:** Zechariah chapters 9, 10, 11, 13 only (Lane C stopped set only; no other Zechariah chapters touched).

**Method:** `python3 recovery.py ZECHARIAH 9,10,11,13 --apply --readers-only` from `~/workspace/ceb-push/fix-pass`, then independent verification with `verify_recovery.py`. Writes confined to the two reader surfaces in staging (`books/`, `individual-books/`); no editions file touched; the live shelf not touched.

## Per-chapter dispositions (counts from fix-pass/recovery-results/ZECHARIAH.json)

| Chapter | Disposition | q | q2 | m | qs |
|---|---|---|---|---|---|
| Zechariah 9 | RESTORED | 26 | 40 | 0 | 0 |
| Zechariah 10 | RESTORED | 17 | 31 | 0 | 0 |
| Zechariah 11 | RESTORED | 4 | 5 | 0 | 0 |
| Zechariah 13 | RESTORED | 5 | 8 | 0 | 0 |

No chapter in this book came back PAGE-PROSE or STOPPED.

## Totals

RESTORED 4 / PAGE-PROSE 0 / STOPPED 0. Divisions restored: q 52, q2 84, m 0, qs 0 — 136 in all.

## Verification summary

`python3 verify_recovery.py --readers ZECHARIAH:9,10,11,13` (run as part of the Wave F combined verification) returned **VERIFIED for all four chapters** (poetic=True, surfaces_identical=True, rederive_match=True on every chapter).
