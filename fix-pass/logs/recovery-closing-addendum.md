# RECOVERY PASS — CLOSING ADDENDUM (finisher, 2026-10-18)

The recovery pass report (`logs/recovery-pass-report.md`) closed with four chapters
STOPPED on three questions for the desk. All three questions were ruled YES — Stop 1
(Acts) by the editor himself (2026-10-18, 06:52 CDT); Stops 2 and 3 (Isaiah 44;
Habakkuk 3) by the desk under the editor's standing test (the logic gate and the love
filter, "Love is the power supreme"), as recorded in `logs/dispositions-log.md`. The
finisher applied the three rulings with the pass's own machinery and discipline
(`finish_recovery.py`, importing `recovery.py` unchanged; readers first, editions
transplanted serially by `editions_apply_recovery.py`, exactly as the waves were
organized). All work is in the staging tree; the published shelf was never written;
nothing was pushed or published.

## Per-chapter evidence

### Acts 8 — RESTORED (2 q, 4 q2), under the editor's ruling on base-only verses
- The base-only verse, Acts 8:37, exists on the base page only as a footnote popup
  ("TR adds Philip said, 'If you believe with all your heart, you may…'"); the verse
  marker stands with no verse body, and the parsed chunk list for the verse is empty.
  It was treated as outside the staged text and removed from the parse before the
  verse-set assertion. No word was added or removed: the rebuild works from staged
  tokens only, and the chapter's word-stream identity was asserted on every surface
  before any write, and whole-file after every splice.
- Divisions restored: the Isaiah quotation at vv. 32–33 — 2 q, 4 q2, matching the
  pass report's recorded page inventory.
- Finisher finding: the staged chapter registers the omitted verse with a
  bare-number paragraph ('37') standing between vv. 36 and 38. It was carried
  through untouched.
- Surfaces (4): `books/` and `individual-books/` readers; catholic and protestant
  editions (transplant log: `logs/recovery-editions-application.md`).
- Verification: independent re-extraction — `verify_recovery.py ACTS:8,15` (the
  pass's stock verifier) VERIFIED, and `verify_finish.py` VERIFIED (surfaces
  identical, re-derivation match).

### Acts 15 — RESTORED (7 q segments), under the same ruling
- Acts 15:34 exists on the base page only as a footnote popup ("Some manuscripts
  add: But it seemed good to Silas to stay there."); empty chunk list; treated as
  outside the staged text, as above.
- Divisions restored: 7 q verse-segments at vv. 16–17. The page carries 6 q blocks —
  the count the chapter's apparatus records and the pass report cites — because the
  v. 16/17 verse boundary falls inside one block ("I will set it up" / "that the
  rest of men may seek after the Lord:"); the block yields one line in each verse.
  Both counts describe the same page; no division was created or lost.
- Finisher finding: the staged bare-number paragraph ('34') between vv. 33 and 35
  stands untouched.
- Surfaces (4) and verification: as Acts 8 — VERIFIED by both verifiers.

### Isaiah 44 — RESTORED (45 q, 82 q2), under the desk's sense-placement ruling
- The single boundary in v. 19 that falls inside the Decision 9 conversion span was
  placed by sense, narrowly, and the placement is logged exactly. Base boundary
  after token 46 ("…into an abomination?") falls strictly inside the replace span
  base[44:47] = ['an', 'abomination?', 'Shall'] -> staged[44:48] = ['a',
  'detestable', 'thing?', 'Will'] (the "abomination" -> "detestable thing" and
  "Shall" -> "Will" conversions). It was placed at staged boundary 47, immediately
  after "thing?", so the division reads "…a detestable thing?" | "Will I bow down
  to a tree trunk?" — the sense-placement Addendum 1 recorded as plain.
- Sense-ground: the base's division separates the idol-maker's two rhetorical
  questions; in the staged wording the first question ends at "thing?", and that is
  where the division stands. No division was created: the boundary is the base's
  own (the verse's other five boundaries — at base tokens 3, 11, 20, 29, 36 — were
  placed mechanically, as was every other boundary in the chapter). The placement
  was asserted against the recorded conversion strings (span contents, the
  '?'-final token, and the following "Will") before any write; had any assertion
  failed, the chapter would have stood stopped.
- Surfaces (5): both readers; catholic, protestant, and hebrew editions.
- Verification: independent re-extraction under the ruling (`verify_finish.py`) —
  VERIFIED (surfaces identical on all five, re-derivation match).

### Habakkuk 3 — RESTORED (23 q, 38 q2, 3 qs), under the desk's colophon ruling
- The music-director colophon ("For the music director, on my stringed
  instruments.") stands on the base page as a prose block after v. 19 and in the
  staged text as a standalone paragraph after v. 19 — equal word for word. It was
  matched as that standalone: the trailing prose chunk was lifted out of v. 19's
  chunk list at parse time, the standalone assertion then passed, and the staged
  paragraph itself stands untouched, exactly as staged.
- Divisions restored: 23 q, 38 q2, 3 qs (Selah lines) — the chapter's full totals on
  the base page, as Addendum 2 recorded them.
- Surfaces (5): both readers; catholic, protestant, and hebrew editions.
- Verification: independent re-extraction under the ruling (`verify_finish.py`) —
  VERIFIED (surfaces identical on all five, re-derivation match).

## Final totals for the recovery pass (Lane C stopped scope, reconciled exactly)

- Chapters disposed: **396** — the full Lane C stopped scope of the pass report.
- **RESTORED: 341 chapters** (337 by the waves and pilot + these 4).
- **PAGE-PROSE: 55 chapters** — unchanged; the base itself sets them in prose.
- **STOPPED: 0.** No chapter in the scope remains unrestored for want of a ruling.
- **Divisions restored: 15,584** — 6,645 q, 8,857 q2, 8 m, 74 qs (Selah lines).
  (Pass report: 15,380 = 6,568 q / 8,733 q2 / 8 m / 71 qs; finisher adds 204 =
  77 q / 124 q2 / 0 m / 3 qs: Acts 8, 6; Acts 15, 7; Isaiah 44, 127; Habakkuk 3, 64.)
- **Editions: 1,002 chapter-edition spans** transplanted under word-stream
  assertion (992 by the coordinator + 10 by the finisher: Acts 8 and 15 × 2
  editions; Isaiah 44 and Habakkuk 3 × 3 editions).

## Boundary of this addendum

The finisher's work ends here, in the staging tree. The desk's final whole-tree
staging-vs-shelf verification — the last term of the shelf word's condition — is
the desk's own act and is not part of this addendum. Method artifacts:
`fix-pass/finish_recovery.py` (application under the rulings) and
`fix-pass/verify_finish.py` (re-extraction under the rulings); per-book finisher
sections appended to `logs/recovery-acts-log.md`, `logs/recovery-isaiah-log.md`,
and `logs/recovery-habakkuk-log.md`.
