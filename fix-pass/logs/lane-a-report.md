# LANE A REPORT — exact conversions (Ruling 12; Ruling 3)

Status: COMPLETE, verified. Log: `logs/lane-a-log.md` (59 entries).

## What changed
- Ruling 12 ("will" for the whole class — arrangements described): 18 "must" instances converted to "will" across 11 verses — Numbers 8:25 (×2), 8:26 (×3), 2 Chronicles 19:9 (×1), 19:11 (×1), 23:4 (×2), 23:5 (×1), 23:6 (×2), 23:7 (×1), Nehemiah 10:38 (×2), 10:39 (×1), Ezra 6:8 (×2).
- Ruling 3 (Trigger 1): 1 Peter 3:20 — "eight people" restored to the base's "eight souls" ("were saved" is predicated of the souls).
- Each change was applied on every surface the census names: 59 paragraph replacements in all (11 Old Testament places × 5 surfaces = 55; 1 Peter × 4 surfaces).

## Mechanism and safeguards
Exact verse-paragraph replacement, asserted unique in each target file before replacing; the run aborts on any assertion failure with nothing written. (One abort occurred during the run: a 40-character anchor for Nehemiah 10:39 also matched a Jeremiah verse in the hebrew volume; the locator was rebuilt to match the full verse body uniquely, staging verified clean, and the run repeated.) Files were written only after all 59 replacements succeeded in memory.

## Verification performed
- Diff of the whole staging tree against the live shelf: exactly 13 files differ (the five governed books in `books/` and `individual-books/`, plus the three editions), and the changed-line counts are symmetric (old lines = new lines: books 12/12, individual-books 12/12, editions 35/35), so no verse was added, dropped, or re-paragraphed.
- All 12 governed verses re-extracted from the staged `books/` readers after the change and read back: every governed verse now reads "will" at its standing-duty instances; no "must" remains in any governed verse.
- 1 Peter 3:20: "eight souls" now stands in the books reader and both editions (individual-books reader carries it through the same replacement, logged); "eight people" occurs nowhere in the staged 1 Peter surfaces.
- Verse totals: unchanged — replacements were one-paragraph-for-one-paragraph everywhere (diff line symmetry above).

## Held / remaining
Nothing held in this lane. No place required a judgment beyond the rulings' own text.
