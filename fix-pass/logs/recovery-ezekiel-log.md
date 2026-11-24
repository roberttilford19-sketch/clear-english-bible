# RECOVERY PASS — WAVE E LOG: EZEKIEL (lineation-recovery worker)

Pass: Lineation Recovery Pass, Clear Translation Bible fix pass. Readers only (`--readers-only`): writes confined to staging's `books/` and `individual-books/`. No editions file edited, nothing written outside `~/workspace/ceb-push/fix-pass/staging/`, live shelf untouched.

## Ruling cited

**Ruling 8 as amended by the editor 2026-10-18** — where the recorded apparatuses do not carry a chapter's divisions in full, the divisions may be read from the base's own pages (public-domain WEB Classic at ebible.org), wording asserted identical chapter by chapter, stop rule where a page does not speak plainly, base-prose chapters never relineated, no division invented.

Method governed by `logs/recovery-pilot-log.md`; representation conventions per `logs/lane-c-report.md` (divisions as lines within the verse paragraph — q flush left, q2 indented two spaces, m on its own unindented line, qs (Selah) on its own unindented line; prose lead on the verse's first line; verse number at the head of the verse's first line).

## Scope

Ezekiel chapters 1–48 — the whole book, which was in Lane C's stopped set — 48 chapters in total. No other book was touched in this log's work, except Deuteronomy 27 and 33, which are reported in their own log (`logs/recovery-deuteronomy-log.md`).

Applied with `python3 recovery.py EZEKIEL <comma-list> --apply --readers-only` in four batches (1–15; 16–30; 31–45; 46–48). Counts below are taken from `fix-pass/recovery-results/EZEKIEL.json`.

## Per-chapter dispositions

### RESTORED (12 chapters)

- Ezekiel 18 — RESTORED — q 19, q2 24, m 2, qs 0
- Ezekiel 19 — RESTORED — q 21, q2 25, m 1, qs 0
- Ezekiel 21 — RESTORED — q 24, q2 31, m 0, qs 0
- Ezekiel 23 — RESTORED — q 4, q2 6, m 1, qs 0
- Ezekiel 24 — RESTORED — q 15, q2 23, m 2, qs 0
- Ezekiel 26 — RESTORED — q 4, q2 4, m 0, qs 0
- Ezekiel 27 — RESTORED — q 30, q2 38, m 0, qs 0
- Ezekiel 28 — RESTORED — q 29, q2 46, m 0, qs 0
- Ezekiel 29 — RESTORED — q 7, q2 7, m 0, qs 0
- Ezekiel 30 — RESTORED — q 23, q2 32, m 0, qs 0
- Ezekiel 31 — RESTORED — q 12, q2 15, m 0, qs 0
- Ezekiel 32 — RESTORED — q 21, q2 27, m 0, qs 0

Division totals across the restored chapters: q 209, q2 278, m 6, qs 0 (493 divisions in total).

### PAGE-PROSE (36 chapters)

The base page carries no q/q2/qs division in the chapter; nothing exists to restore; left exactly as staged. Reason recorded in the results file for each: "base page carries no q/q2/qs division in this chapter; nothing to restore; left as staged".

- Ezekiel 1 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 2 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 3 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 4 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 5 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 6 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 7 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 8 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 9 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 10 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 11 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 12 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 13 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 14 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 15 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 16 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 17 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 20 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 22 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 25 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 33 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 34 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 35 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 36 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 37 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 38 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 39 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 40 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 41 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 42 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 43 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 44 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 45 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 46 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 47 — PAGE-PROSE — q 0, q2 0, m 0, qs 0
- Ezekiel 48 — PAGE-PROSE — q 0, q2 0, m 0, qs 0

Ezekiel 37's PAGE-PROSE result agrees with the pilot's independent finding for that chapter (base page prose blocks throughout), recorded in `logs/recovery-pilot-log.md`.

### STOPPED (0 chapters)

No chapter in Ezekiel came back STOPPED. There are no stopped reasons to quote.

## PAGE-PROSE pattern

The PAGE-PROSE chapters are not scattered at random; they form the book's prose frame, with the restored poetry concentrated in one middle block:

- Chapters 1–17: all 17 chapters PAGE-PROSE, without exception.
- Chapters 18–32: the restored block — 12 of these 15 chapters RESTORED, with only chapters 20, 22, and 25 PAGE-PROSE inside the block.
- Chapters 33–48: all 16 chapters PAGE-PROSE, without exception, including the temple and allotment chapters 40–48 and chapter 37.

A PAGE-PROSE disposition is a complete outcome under the ruling for these chapters: the base page itself sets them in prose, so no lineation exists there to restore, and none was invented.

## Totals

- Scope: 48 chapters
- RESTORED: 12
- PAGE-PROSE: 36
- STOPPED: 0
- 12 + 36 + 0 = 48 — scope reconciles in full.

## Verification summary — with its caveat in the same breath

Every chapter (all 48, none having stopped) was verified with `python3 verify_recovery.py --readers EZEKIEL:<comma-list>` in three batches (1–15; 16–30; 31–48, the last run together with the Deuteronomy verification). 47 chapters came back VERIFIED; Ezekiel 48 came back MISMATCH on re-derivation only, as detailed below — so this book does **not** carry a clean all-verified summary.

- VERIFIED (47 chapters): Ezekiel 1–47, each with `surfaces_identical=True` and `rederive_match=True`.
  - Poetic chapters (`poetic=True`, 12): Ezekiel 18, 19, 21, 23, 24, 26, 27, 28, 29, 30, 31, 32 — exactly the RESTORED set.
  - Prose chapters (`poetic=False`, 35): Ezekiel 1–17, 20, 22, 25, 33–47 — the PAGE-PROSE set except chapter 48.
- Ezekiel 48: `MISMATCH (poetic=False, surfaces_identical=True, rederive_match=False)`, reproduced on a second single-chapter verify run.

### Ezekiel 48 mismatch — diagnostic (read-only, no text changed)

A read-only re-derivation comparison was run to locate the difference. The expected and staged chapters both contain 36 paragraphs, and the first difference is at paragraph 35, the chapter's and the book's last paragraph (verse 35). The two forms are word-for-word identical except that the staged paragraph carries a trailing newline character at the end of the file and the re-derived paragraph does not:

- Expected (re-derived): `35 “It will be eighteen thousand reeds in circumference; and the name of the city from that day will be, ‘Yahweh is there.’'`
- Staged (actual): the same text followed by `\n`

Chapter 48 is PAGE-PROSE, so the recovery pass wrote nothing for it; the trailing newline is therefore not a recovery-introduced wording change. Both reader surfaces are identical for this chapter (`surfaces_identical=True`). No hand edit was made to correct it, per the brief: whether this file-end newline is normalised at script level or accepted as a verifier artefact at the end of a book file is the coordinator's call.

## Notes for the coordinator

- No systemic stop problem occurred in Ezekiel: no unknown div classes, no fetch failures, no alignment stops, no verse-set mismatches — indeed no stops at all.
- No batch aborted early; all four apply batches completed in full on the first run.
- The one open item is the Ezekiel 48 verification mismatch described above, confined to a single trailing newline on the book's final paragraph.
