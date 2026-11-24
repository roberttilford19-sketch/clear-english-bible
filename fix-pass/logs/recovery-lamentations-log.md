# RECOVERY LOG — LAMENTATIONS (Wave B)

Pass: Lineation Recovery Pass, Clear Translation Bible fix pass. Readers only (`--readers-only`): writes confined to staging's `books/` and `individual-books/`. No editions file edited, no write outside `~/workspace/ceb-push/fix-pass/staging/`, live shelf untouched.

## Ruling cited

**Ruling 8 as amended by the editor 2026-10-18** — where the recorded apparatuses do not carry a chapter's divisions in full, the divisions may be read from the base's own pages (public-domain WEB Classic at ebible.org), wording asserted identical chapter by chapter, stop rule where a page does not speak plainly, base-prose chapters never relineated, no division invented.

## Scope

Lamentations chapters 1–5.

Tool: `python3 recovery.py LAMENTATIONS <comma-list> --apply --readers-only`, in batches of at most 15 chapters per call. Counts below are taken from `fix-pass/recovery-results/LAMENTATIONS.json`.

## Per-chapter dispositions

- LAMENTATIONS 1: RESTORED — q 46, q2 61, m 0, qs 0
- LAMENTATIONS 2: RESTORED — q 40, q2 60, m 0, qs 0
- LAMENTATIONS 3: RESTORED — q 58, q2 69, m 0, qs 0
- LAMENTATIONS 4: RESTORED — q 34, q2 46, m 0, qs 0
- LAMENTATIONS 5: RESTORED — q 22, q2 22, m 0, qs 0

## Totals

- Chapters in scope: 5
- RESTORED: 5
- PAGE-PROSE: 0
- STOPPED: 0
- Divisions restored in total: q 200, q2 258, m 0, qs 0 (total 458)

## Verification summary

Verified with `python3 verify_recovery.py --readers LAMENTATIONS:1,2,3,4,5` (run together with the other Wave B books). Every non-stopped chapter returned VERIFIED (poetic=True, surfaces_identical=True, rederive_match=True): 5 of 5 chapters verified, 0 stopped chapters excluded from verification because nothing was written for them. No chapter in this book stopped, so none was excluded.

No systemic problem was observed for this book: no repeating unknown div classes, no fetch failures, and no alignment stops.
