# RECOVERY PASS — WAVE D LOG: JEREMIAH (lineation-recovery worker)

Pass: Lineation Recovery Pass, Clear Translation Bible fix pass. Readers only (`--readers-only`): writes confined to staging's `books/` and `individual-books/`. No editions file edited, nothing written outside `~/workspace/ceb-push/fix-pass/staging/`, live shelf untouched.

## Ruling cited

**Ruling 8 as amended by the editor 2026-10-18** — where the recorded apparatuses do not carry a chapter's divisions in full, the divisions may be read from the base's own pages (public-domain WEB Classic at ebible.org), wording asserted identical chapter by chapter, stop rule where a page does not speak plainly, base-prose chapters never relineated, no division invented.

Method governed by `logs/recovery-pilot-log.md`; representation conventions per `logs/lane-c-report.md` (divisions as lines within the verse paragraph — q flush left, q2 indented two spaces, m on its own unindented line, qs (Selah) on its own unindented line; prose lead on the verse's first line; verse number at the head of the verse's first line).

## Scope

Jeremiah chapters — the Lane C stopped set only: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 29, 30, 31, 32, 33, 34, 35, 46, 47, 48, 49, 50, 51 — 38 chapters in total.

Not touched, per scope: Jeremiah 24, 27, 28, 36–45, 52 (base-prose skips in Lane C), and no other book. Jeremiah 36 is out of scope in any case.

Applied with `python3 recovery.py JEREMIAH <comma-list> --apply --readers-only` in three batches (1–15; 16,17,18,19,20,21,22,23,25,26,29,30,31,32,33; 34,35,46,47,48,49,50,51). Counts below are taken from `fix-pass/recovery-results/JEREMIAH.json`.

## Per-chapter dispositions

### RESTORED (28 chapters)

- Jeremiah 1 — RESTORED — q 3, q2 6, m 0, qs 0
- Jeremiah 2 — RESTORED — q 48, q2 73, m 0, qs 0
- Jeremiah 6 — RESTORED — q 8, q2 7, m 0, qs 0
- Jeremiah 8 — RESTORED — q 28, q2 40, m 0, qs 0
- Jeremiah 9 — RESTORED — q 35, q2 38, m 0, qs 0
- Jeremiah 10 — RESTORED — q 36, q2 52, m 0, qs 0
- Jeremiah 11 — RESTORED — q 7, q2 9, m 0, qs 0
- Jeremiah 12 — RESTORED — q 24, q2 31, m 0, qs 0
- Jeremiah 13 — RESTORED — q 22, q2 29, m 0, qs 0
- Jeremiah 14 — RESTORED — q 28, q2 36, m 0, qs 0
- Jeremiah 15 — RESTORED — q 31, q2 38, m 0, qs 0
- Jeremiah 16 — RESTORED — q 5, q2 6, m 0, qs 0
- Jeremiah 17 — RESTORED — q 27, q2 35, m 0, qs 0
- Jeremiah 18 — RESTORED — q 16, q2 21, m 0, qs 0
- Jeremiah 20 — RESTORED — q 20, q2 27, m 0, qs 0
- Jeremiah 21 — RESTORED — q 5, q2 7, m 0, qs 0
- Jeremiah 22 — RESTORED — q 30, q2 36, m 1, qs 0
- Jeremiah 23 — RESTORED — q 28, q2 38, m 0, qs 0
- Jeremiah 25 — RESTORED — q 11, q2 14, m 0, qs 0
- Jeremiah 26 — RESTORED — q 1, q2 2, m 0, qs 0
- Jeremiah 30 — RESTORED — q 32, q2 44, m 0, qs 0
- Jeremiah 31 — RESTORED — q 48, q2 56, m 0, qs 0
- Jeremiah 46 — RESTORED — q 39, q2 57, m 0, qs 0
- Jeremiah 47 — RESTORED — q 12, q2 14, m 0, qs 0
- Jeremiah 48 — RESTORED — q 67, q2 87, m 0, qs 0
- Jeremiah 49 — RESTORED — q 58, q2 81, m 0, qs 0
- Jeremiah 50 — RESTORED — q 80, q2 118, m 0, qs 0
- Jeremiah 51 — RESTORED — q 93, q2 124, m 0, qs 0

Division totals across the restored chapters: q 842, q2 1126, m 1, qs 0 (1969 divisions in total). The single m division in the book's scope is in Jeremiah 22.

### PAGE-PROSE (7 chapters)

The base page carries no q/q2/qs division in the chapter; nothing exists to restore; left exactly as staged. Reason recorded in the results file for each: "base page carries no q/q2/qs division in this chapter; nothing to restore; left as staged".

- Jeremiah 3 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Jeremiah 4 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Jeremiah 5 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Jeremiah 7 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Jeremiah 19 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Jeremiah 34 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Jeremiah 35 — PAGE-PROSE — q 0, q2 0, m 0, qs 0

### STOPPED (3 chapters)

Nothing was written for these chapters; each was left exactly as staged. Reasons verbatim from `fix-pass/recovery-results/JEREMIAH.json`:

- Jeremiah 29 — STOPPED — "unhandled div class(es) on base page: ['pi']"
- Jeremiah 32 — STOPPED — "unhandled div class(es) on base page: ['mi', 'pi']"
- Jeremiah 33 — STOPPED — "unhandled div class(es) on base page: ['nb']"

## Totals

- Scope: 38 chapters
- RESTORED: 28
- PAGE-PROSE: 7
- STOPPED: 3
- 28 + 7 + 3 = 38 — scope reconciles in full.

## Verification summary

Every chapter that did not come back STOPPED (35 chapters) was verified with `python3 verify_recovery.py --readers JEREMIAH:<comma-list>` in two batches (25 chapters, then 10 chapters). STOPPED chapters were excluded, as nothing was written for them.

All 35 chapters came back VERIFIED, each with `surfaces_identical=True` and `rederive_match=True`:

- Poetic chapters (`poetic=True`, 28): Jeremiah 1, 2, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 25, 26, 30, 31, 46, 47, 48, 49, 50, 51 — exactly the RESTORED set.
- Prose chapters (`poetic=False`, 7): Jeremiah 3, 4, 5, 7, 19, 34, 35 — exactly the PAGE-PROSE set.

No verification failures, no mismatches.

## Notes for the coordinator

- Systemic observation: all three stops are the same kind — unhandled div classes on the base page that the fixed script does not recognise: `pi` (Jeremiah 29; also in 32), `mi` (Jeremiah 32), and `nb` (Jeremiah 33). No other stop kind occurred in this book: no alignment stops, no fetch failures, no verse-set mismatches. The three stopped chapters cluster in the 29–33 block. Per the brief, no stop was overridden and no text was hand-edited; whether these classes warrant a script-level ruling is the coordinator's call.
- No batch aborted early; all three apply batches and both verify batches completed in full on the first run.
