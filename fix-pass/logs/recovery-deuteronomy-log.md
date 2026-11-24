# RECOVERY PASS — WAVE E LOG: DEUTERONOMY (lineation-recovery worker)

Pass: Lineation Recovery Pass, Clear Translation Bible fix pass. Readers only (`--readers-only`): writes confined to staging's `books/` and `individual-books/`. No editions file edited, nothing written outside `~/workspace/ceb-push/fix-pass/staging/`, live shelf untouched.

## Ruling cited

**Ruling 8 as amended by the editor 2026-10-18** — where the recorded apparatuses do not carry a chapter's divisions in full, the divisions may be read from the base's own pages (public-domain WEB Classic at ebible.org), wording asserted identical chapter by chapter, stop rule where a page does not speak plainly, base-prose chapters never relineated, no division invented.

Method governed by `logs/recovery-pilot-log.md`; representation conventions per `logs/lane-c-report.md` (divisions as lines within the verse paragraph — q flush left, q2 indented two spaces, m on its own unindented line, qs (Selah) on its own unindented line; prose lead on the verse's first line; verse number at the head of the verse's first line).

## Scope

Deuteronomy chapters 27 and 33 only — 2 chapters in total. Chapter 32 was restored by the pilot and was not re-run here; the rest of Deuteronomy was never in scope and was not touched. No other book was touched in this log's work, except Ezekiel 1–48, which are reported in their own log (`logs/recovery-ezekiel-log.md`).

Applied with `python3 recovery.py DEUTERONOMY 27,33 --apply --readers-only` in a single batch. Counts below are taken from `fix-pass/recovery-results/DEUTERONOMY.json` for chapters 27 and 33 only. That results file also carries the pilot's earlier chapter 32 entry, which predates this wave and is not counted here.

## Per-chapter dispositions

### RESTORED (1 chapter)

- Deuteronomy 33 — RESTORED — q 40, q2 56, m 0, qs 0

Division totals across the restored chapter: q 40, q2 56, m 0, qs 0 (96 divisions in total).

### PAGE-PROSE (1 chapter)

The base page carries no q/q2/qs division in the chapter; nothing exists to restore; left exactly as staged. Reason recorded in the results file: "base page carries no q/q2/qs division in this chapter; nothing to restore; left as staged".

- Deuteronomy 27 — PAGE-PROSE — q 0, q2 0, m 0, qs 0

### STOPPED (0 chapters)

Neither chapter came back STOPPED. There are no stopped reasons to quote.

## Totals

- Scope: 2 chapters
- RESTORED: 1
- PAGE-PROSE: 1
- STOPPED: 0
- 1 + 1 + 0 = 2 — scope reconciles in full.

## Verification summary

Both chapters (neither having stopped) were verified with `python3 verify_recovery.py --readers DEUTERONOMY:27,33`, run together with the final Ezekiel verification batch.

Both chapters came back VERIFIED, each with `surfaces_identical=True` and `rederive_match=True`:

- Deuteronomy 27 — VERIFIED (`poetic=False`) — exactly consistent with its PAGE-PROSE disposition.
- Deuteronomy 33 — VERIFIED (`poetic=True`) — exactly the RESTORED chapter.

No verification failures, no mismatches.

## Notes for the coordinator

- No systemic problem occurred in Deuteronomy: no unknown div classes, no fetch failures, no alignment stops, no verse-set mismatches.
- The apply batch completed in full on the first run.
