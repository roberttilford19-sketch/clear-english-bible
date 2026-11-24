# RECOVERY LOG — ECCLESIASTES (Wave B)

Pass: Lineation Recovery Pass, Clear Translation Bible fix pass. Readers only (`--readers-only`): writes confined to staging's `books/` and `individual-books/`. No editions file edited, no write outside `~/workspace/ceb-push/fix-pass/staging/`, live shelf untouched.

## Ruling cited

**Ruling 8 as amended by the editor 2026-10-18** — where the recorded apparatuses do not carry a chapter's divisions in full, the divisions may be read from the base's own pages (public-domain WEB Classic at ebible.org), wording asserted identical chapter by chapter, stop rule where a page does not speak plainly, base-prose chapters never relineated, no division invented.

## Scope

Ecclesiastes chapters 3, 10, 11, 12 only (the rest of Ecclesiastes was base-prose in Lane C and was not touched).

Tool: `python3 recovery.py ECCLESIASTES <comma-list> --apply --readers-only`, in batches of at most 15 chapters per call. Counts below are taken from `fix-pass/recovery-results/ECCLESIASTES.json`.

## Per-chapter dispositions

- ECCLESIASTES 3: RESTORED — q 14, q2 14, m 0, qs 0
- ECCLESIASTES 10: RESTORED — q 7, q2 13, m 0, qs 0
- ECCLESIASTES 11: RESTORED — q 9, q2 19, m 0, qs 0
- ECCLESIASTES 12: RESTORED — q 6, q2 21, m 0, qs 0

## Totals

- Chapters in scope: 4
- RESTORED: 4
- PAGE-PROSE: 0
- STOPPED: 0
- Divisions restored in total: q 36, q2 67, m 0, qs 0 (total 103)

## Verification summary

Verified with `python3 verify_recovery.py --readers ECCLESIASTES:3,10,11,12` (run together with the other Wave B books). Every non-stopped chapter returned VERIFIED (poetic=True, surfaces_identical=True, rederive_match=True): 4 of 4 chapters verified, 0 stopped chapters excluded from verification because nothing was written for them. No chapter in this book stopped, so none was excluded.

No systemic problem was observed for this book: no repeating unknown div classes, no fetch failures, and no alignment stops.
