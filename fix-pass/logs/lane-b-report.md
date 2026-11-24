# LANE B REPORT — Song of Songs speaker headings (Ruling 18)

Status: COMPLETE, verified. Log: `logs/lane-b-log.md`.

## What changed
All 33 speaker headings restored on all five surfaces carrying the Song (`books/SONGOFSONGS-reader.txt`, `individual-books/SONGOFSONGS-reader.txt`, `editions/catholic`, `editions/protestant`, `editions/hebrew`), at the positions recorded in the pinned base snapshots, in the base's own heading words ("Beloved," "Friends," "Lover," "Brothers"), cross-checked against SONGOFSONGS-COMPLETION-REPORT.md flag 2 (chapter counts 9, 5, 0, 2, 5, 5, 1, 6). Chapter 3: no headings recorded, none inserted. No verse wording changed anywhere.

Representation (coordinator's decision, recorded in the log): each heading stands as its own paragraph; a within-verse heading splits the verse paragraph at the recorded anchor, the verse number staying with the first part. Three records phrased as positions inside a verse resolve to verse boundaries and were applied there, as the log states: ch. 5's second heading (at v. 1's end, "before v. 2"), ch. 6's Friends (at v. 13's head, after v. 12's close), ch. 7's Beloved (at v. 10's head, after v. 9).

## Verification performed
- Heading counts per surface after application: 33 on each of the four surfaces; per-chapter counts match the completion report on the readers and on the hebrew edition region check.
- Word-stream integrity: for each surface, the Song's text with the inserted heading paragraphs removed is whitespace-normalized-identical to the live shelf's Song text — checked chapter by chapter on both readers, by whole-region comparison on both editions. (Two early check scripts produced false failures — a wrong next-book boundary in the hebrew volume and a parser that dropped split-verse continuations; both were checker faults, identified as such, and the corrected checks pass.)
- One genuine concurrent-work difference found and accounted for: the staged `books/` Song 8:8 now reads "should" for the live "must" — that is Lane F-1's Ruling 1 judgment at its listed member place (the brothers' question; the packet records the drafted "must" as sitting outside all three audit positions), applied after Lane B's Song application and verified by the coordinator as a one-word deliberative change. It is Lane F's to log; it is not a Lane B alteration.
- The application script asserted, per chapter per surface, that removing the inserted headings restores the pre-change word stream exactly, before writing.

## Held / remaining
Nothing held. One coordinator error occurred and was cured inside this lane, recorded here plainly: the census paragraph and the first application passes listed four Song surfaces and omitted `editions/protestant` (the Song does stand in the 66-book set). The omission was caught in verification against the census's own surface data at Song of Songs 8:8, the protestant edition was applied with the same asserted transform (33 headings; Song-region word stream verified identical to live with headings removed), and the census has been corrected with a dated note. All five surfaces now carry the headings; no surface remains missed.
