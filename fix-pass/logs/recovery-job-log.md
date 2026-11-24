# RECOVERY LOG — JOB (Wave B)

Pass: Lineation Recovery Pass, Clear Translation Bible fix pass. Readers only (`--readers-only`): writes confined to staging's `books/` and `individual-books/`. No editions file edited, no write outside `~/workspace/ceb-push/fix-pass/staging/`, live shelf untouched.

## Ruling cited

**Ruling 8 as amended by the editor 2026-10-18** — where the recorded apparatuses do not carry a chapter's divisions in full, the divisions may be read from the base's own pages (public-domain WEB Classic at ebible.org), wording asserted identical chapter by chapter, stop rule where a page does not speak plainly, base-prose chapters never relineated, no division invented.

## Scope

Job chapters 3–42 (chapters 1–2 were base-prose skips in Lane C and were not touched).

Tool: `python3 recovery.py JOB <comma-list> --apply --readers-only`, in batches of at most 15 chapters per call. Counts below are taken from `fix-pass/recovery-results/JOB.json`.

## Per-chapter dispositions

- JOB 3: RESTORED — q 24, q2 28, m 0, qs 0
- JOB 4: RESTORED — q 20, q2 23, m 0, qs 0
- JOB 5: RESTORED — q 27, q2 29, m 0, qs 0
- JOB 6: RESTORED — q 30, q2 32, m 0, qs 0
- JOB 7: RESTORED — q 21, q2 26, m 0, qs 0
- JOB 8: RESTORED — q 22, q2 21, m 0, qs 0
- JOB 9: RESTORED — q 34, q2 37, m 0, qs 0
- JOB 10: RESTORED — q 22, q2 30, m 0, qs 0
- JOB 11: RESTORED — q 18, q2 22, m 0, qs 0
- JOB 12: RESTORED — q 24, q2 27, m 0, qs 0
- JOB 13: RESTORED — q 28, q2 31, m 0, qs 0
- JOB 14: RESTORED — q 21, q2 29, m 0, qs 0
- JOB 15: RESTORED — q 34, q2 36, m 0, qs 0
- JOB 16: RESTORED — q 21, q2 28, m 0, qs 0
- JOB 17: RESTORED — q 16, q2 18, m 0, qs 0
- JOB 18: RESTORED — q 20, q2 21, m 0, qs 0
- JOB 19: RESTORED — q 29, q2 30, m 0, qs 0
- JOB 20: RESTORED — q 28, q2 30, m 0, qs 0
- JOB 21: RESTORED — q 33, q2 35, m 0, qs 0
- JOB 22: RESTORED — q 29, q2 29, m 0, qs 0
- JOB 23: RESTORED — q 16, q2 16, m 0, qs 0
- JOB 24: RESTORED — q 25, q2 35, m 0, qs 0
- JOB 25: RESTORED — q 5, q2 5, m 0, qs 0
- JOB 26: RESTORED — q 13, q2 14, m 0, qs 0
- JOB 27: RESTORED — q 22, q2 21, m 0, qs 0
- JOB 28: RESTORED — q 28, q2 31, m 0, qs 0
- JOB 29: RESTORED — q 24, q2 25, m 0, qs 0
- JOB 30: RESTORED — q 31, q2 34, m 0, qs 0
- JOB 31: RESTORED — q 40, q2 44, m 0, qs 0
- JOB 32: RESTORED — q 17, q2 19, m 0, qs 0
- JOB 33: RESTORED — q 33, q2 38, m 0, qs 0
- JOB 34: RESTORED — q 36, q2 42, m 0, qs 0
- JOB 35: RESTORED — q 15, q2 15, m 0, qs 0
- JOB 36: RESTORED — q 32, q2 35, m 0, qs 0
- JOB 37: RESTORED — q 24, q2 28, m 0, qs 0
- JOB 38: RESTORED — q 40, q2 41, m 0, qs 0
- JOB 39: RESTORED — q 30, q2 32, m 0, qs 0
- JOB 40: RESTORED — q 21, q2 21, m 0, qs 0
- JOB 41: RESTORED — q 34, q2 35, m 0, qs 0
- JOB 42: RESTORED — q 5, q2 6, m 0, qs 0

## Totals

- Chapters in scope: 40
- RESTORED: 40
- PAGE-PROSE: 0
- STOPPED: 0
- Divisions restored in total: q 992, q2 1099, m 0, qs 0 (total 2091)

## Verification summary

Verified with `python3 verify_recovery.py --readers JOB:3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42` (run together with the other Wave B books). Every non-stopped chapter returned VERIFIED (poetic=True, surfaces_identical=True, rederive_match=True): 40 of 40 chapters verified, 0 stopped chapters excluded from verification because nothing was written for them. No chapter in this book stopped, so none was excluded.

No systemic problem was observed for this book: no repeating unknown div classes, no fetch failures, and no alignment stops.
