# RECOVERY PASS — ISAIAH LOG (Wave C worker)

Pass: Lineation Recovery Pass, Clear Translation Bible fix pass.

Ruling cited: **Ruling 8 as amended by the editor 2026-10-18** — where the recorded apparatuses do not carry a chapter's divisions in full, the divisions may be read from the base's own pages (public-domain WEB Classic at ebible.org), wording asserted identical chapter by chapter, stop rule where a page does not speak plainly, base-prose chapters never relineated, no division invented.

Method: governed by `logs/recovery-pilot-log.md`. Fixed tools used unmodified: `recovery.py ISAIAH <chapters> --apply --readers-only` (batches of at most 15) and `verify_recovery.py --readers ISAIAH:<chapters>` (batches of at most 25). Writes confined to the two readers in staging (`books/`, `individual-books/`). No editions file was touched, nothing was written outside `~/workspace/ceb-push/fix-pass/staging/`, and the live shelf was not touched. Counts below are taken from `fix-pass/recovery-results/ISAIAH.json`.

## Scope

Isaiah chapters — the Lane C stopped set only, 47 chapters: 1, 2, 3, 5, 6, 9, 10, 11, 12, 13, 14, 15, 16, 26, 31, 32, 33, 34, 35, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66.

Not touched, per the editor-authorized scope: Isaiah 4, 7, 8, 17–25, 27–30, 36, 37, 39 (base-prose skips in Lane C), and no other book.

Apply batches run: (1) 1,2,3,5,6,9,10,11,12,13,14,15,16,26,31; (2) 32,33,34,35,38,40,41,42,43,44,45,46,47,48,49; (3) 50,51,52,53,54,55,56,57,58,59,60,61,62,63,64; (4) 65,66. All four batches completed with exit code 0.

## Per-chapter dispositions

RESTORED chapters carry their division counts as q / q2 / m / qs, from `recovery-results/ISAIAH.json`.

- Isaiah 1 — RESTORED — q 37, q2 64, m 0, qs 0
- Isaiah 2 — RESTORED — q 20, q2 49, m 0, qs 0
- Isaiah 3 — RESTORED — q 19, q2 48, m 0, qs 0
- Isaiah 5 — RESTORED — q 37, q2 59, m 0, qs 0
- Isaiah 6 — RESTORED — q 8, q2 13, m 0, qs 0
- Isaiah 9 — RESTORED — q 18, q2 26, m 0, qs 0
- Isaiah 10 — RESTORED — q 1, q2 2, m 0, qs 0
- Isaiah 11 — RESTORED — q 11, q2 16, m 0, qs 0
- Isaiah 12 — PAGE-PROSE — base page carries no q/q2/qs division in this chapter; nothing to restore; left as staged
- Isaiah 13 — PAGE-PROSE — base page carries no q/q2/qs division in this chapter; nothing to restore; left as staged
- Isaiah 14 — PAGE-PROSE — base page carries no q/q2/qs division in this chapter; nothing to restore; left as staged
- Isaiah 15 — PAGE-PROSE — base page carries no q/q2/qs division in this chapter; nothing to restore; left as staged
- Isaiah 16 — PAGE-PROSE — base page carries no q/q2/qs division in this chapter; nothing to restore; left as staged
- Isaiah 26 — RESTORED — q 27, q2 35, m 0, qs 0
- Isaiah 31 — RESTORED — q 12, q2 20, m 0, qs 0
- Isaiah 32 — RESTORED — q 20, q2 35, m 0, qs 0
- Isaiah 33 — RESTORED — q 28, q2 50, m 0, qs 0
- Isaiah 34 — RESTORED — q 20, q2 42, m 0, qs 0
- Isaiah 35 — RESTORED — q 13, q2 24, m 0, qs 0
- Isaiah 38 — RESTORED — q 13, q2 21, m 0, qs 0
- Isaiah 40 — RESTORED — q 28, q2 73, m 0, qs 0
- Isaiah 41 — RESTORED — q 32, q2 69, m 0, qs 0
- Isaiah 42 — RESTORED — q 27, q2 66, m 0, qs 0
- Isaiah 43 — RESTORED — q 35, q2 55, m 0, qs 0
- Isaiah 44 — STOPPED — verse 19: split point falls inside a conversion span (ambiguous alignment)
- Isaiah 45 — RESTORED — q 45, q2 56, m 0, qs 0
- Isaiah 46 — RESTORED — q 23, q2 29, m 0, qs 0
- Isaiah 47 — RESTORED — q 25, q2 34, m 0, qs 0
- Isaiah 48 — RESTORED — q 32, q2 51, m 0, qs 0
- Isaiah 49 — RESTORED — q 43, q2 51, m 0, qs 0
- Isaiah 50 — RESTORED — q 22, q2 26, m 0, qs 0
- Isaiah 51 — RESTORED — q 40, q2 60, m 0, qs 0
- Isaiah 52 — RESTORED — q 17, q2 30, m 0, qs 0
- Isaiah 53 — RESTORED — q 24, q2 28, m 0, qs 0
- Isaiah 54 — RESTORED — q 20, q2 32, m 0, qs 0
- Isaiah 55 — RESTORED — q 17, q2 27, m 0, qs 0
- Isaiah 56 — RESTORED — q 19, q2 27, m 0, qs 0
- Isaiah 57 — RESTORED — q 31, q2 44, m 0, qs 0
- Isaiah 58 — RESTORED — q 27, q2 41, m 0, qs 0
- Isaiah 59 — RESTORED — q 36, q2 42, m 0, qs 0
- Isaiah 60 — RESTORED — q 37, q2 44, m 0, qs 0
- Isaiah 61 — RESTORED — q 19, q2 27, m 0, qs 0
- Isaiah 62 — RESTORED — q 21, q2 24, m 0, qs 0
- Isaiah 63 — RESTORED — q 31, q2 39, m 0, qs 0
- Isaiah 64 — RESTORED — q 17, q2 24, m 0, qs 0
- Isaiah 65 — RESTORED — q 39, q2 55, m 0, qs 0
- Isaiah 66 — RESTORED — q 27, q2 36, m 0, qs 0

## Totals

- Chapters in scope: 47
- RESTORED: 41
- PAGE-PROSE: 5 (Isaiah 12, 13, 14, 15, 16)
- STOPPED: 1 (Isaiah 44)
- Divisions restored across the 41 RESTORED chapters: q 1018, q2 1594, m 0, qs 0 — 2612 divisions in total.

## Verification summary

Every chapter that did not come back STOPPED was verified with `verify_recovery.py --readers`, in two batches: ISAIAH:1,2,3,5,6,9,10,11,12,13,14,15,16,26,31,32,33,34,35,38,40,41,42,43,45 and ISAIAH:46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66. All 46 chapters returned VERIFIED (rederive_match=True, surfaces_identical=True on both readers). The 41 RESTORED chapters verified with poetic=True; the 5 PAGE-PROSE chapters verified with poetic=False, as expected. Isaiah 44 was excluded from verification because it STOPPED and nothing was written for it. Both verification batches exited with code 0; there were no MISMATCH results.

## Notes for the coordinator

- The PAGE-PROSE cluster at Isaiah 12–16 is faithful to the base pages, not a parser failure. A read-only check of the cached pages (`recovery-cache/ISA12.htm`, `ISA13.htm`, `ISA14.htm`) shows those pages carry only `p` blocks and no `q`/`q2`/`qs` divs at all (Isaiah 12: one `p` block; Isaiah 13: four; Isaiah 14: ten), whereas restored neighbours carry the expected mix (Isaiah 1: 37 `q`, 64 `q2`; Isaiah 40: 28 `q`, 73 `q2`). These five chapters sat in Lane C's stopped set, so the coordinator may wish to note that the WEB Classic pages themselves set them in prose. The dispositions were not overridden.
- Isaiah 10 restored with only q 1, q2 2 — a single small poetic island in an otherwise prose chapter, as the base page carries it; verified.
- No unknown div classes, no fetch failures, and no other alignment stops occurred in this scope. The single STOPPED chapter, Isaiah 44, stopped on the standard ambiguous-alignment rule at verse 19 and was left exactly as staged.

## Finisher addendum (2026-10-18) — Isaiah 44 RESTORED under the desk's ruling

Ruling (dispositions log): the one boundary in v. 19 falling inside the Decision 9 conversion span is placed by sense (desk YES under the editor's logic-gate/love-filter maxim). Applied by `finish_recovery.py` (readers), transplanted serially by `editions_apply_recovery.py` (all three editions), word-stream identity asserted on every surface.

- Isaiah 44 — RESTORED — 45 q, 82 q2. Surfaces: both readers + catholic + protestant + hebrew editions.
- The sense placement, exactly: base boundary after token 46 ("…into an abomination?") falls inside the replace span base[44:47] = ['an', 'abomination?', 'Shall'] -> staged[44:48] = ['a', 'detestable', 'thing?', 'Will']; placed at staged boundary 47, immediately after "thing?", so the division reads "…a detestable thing?" | "Will I bow down to a tree trunk?". Every other boundary in the verse (3, 11, 20, 29, 36) placed mechanically; the placement was asserted against the recorded conversion strings before any write.

Verification: `verify_finish.py` (independent re-extraction, re-derivation under the ruling) — VERIFIED (surfaces identical on all five surfaces, re-derivation match).
