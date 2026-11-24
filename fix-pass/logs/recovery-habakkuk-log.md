# Recovery Log — HABAKKUK (Wave F: the minor prophets)

Worker: lineation-recovery worker, Wave F. Date: 2026-10-18.

**Ruling cited:** Ruling 8 as amended by the editor 2026-10-18 — where the recorded apparatuses do not carry a chapter's divisions in full, the divisions may be read from the base's own pages (public-domain WEB Classic at ebible.org), wording asserted identical chapter by chapter, stop rule where a page does not speak plainly, base-prose chapters never relineated, no division invented.

**Scope:** Habakkuk chapter 3 only (Lane C stopped set only; no other Habakkuk chapters touched). Habakkuk 3 is a psalm, with a superscription and Selahs.

**Method:** `python3 recovery.py HABAKKUK 3 --apply --readers-only` from `~/workspace/ceb-push/fix-pass`. Writes confined to the two reader surfaces in staging (`books/`, `individual-books/`); no editions file touched; the live shelf not touched.

## Per-chapter dispositions (from fix-pass/recovery-results/HABAKKUK.json)

| Chapter | Disposition | Reason |
|---|---|---|
| Habakkuk 3 | STOPPED | standalone ('d') block mismatch: staged ['For the music director, on my stringed instruments.'] vs base [] |

The stop reason is recorded verbatim, exactly as the script returned it and as it stands in the results file. Per the stop rule, the chapter was left exactly as staged and nothing was written anywhere for it. No override, hand-edit, or workaround was attempted. (Context: the staged text carries the closing line "For the music director, on my stringed instruments." as a standalone 'd' block; the base page as parsed carries no corresponding standalone block, so the script's standalone-block assertion failed before any rebuild.)

## Totals

RESTORED 0 / PAGE-PROSE 0 / STOPPED 1.

## Verification summary

Habakkuk 3 was excluded from verification, per the brief: STOPPED chapters are not verified because nothing was written for them.

## Finisher addendum (2026-10-18) — Habakkuk 3 RESTORED under the desk's ruling

Ruling (dispositions log): the chapter-final prose block on the base page, equal word for word to the staged standalone paragraph, is matched as that standalone (desk YES under the editor's logic-gate/love-filter maxim). Applied by `finish_recovery.py` (readers), transplanted serially by `editions_apply_recovery.py` (all three editions), word-stream identity asserted on every surface.

- Habakkuk 3 — RESTORED — 23 q, 38 q2, 3 qs, matching the base page's own totals (23 q, 38 q2). Surfaces: both readers + catholic + protestant + hebrew editions.
- The colophon ("For the music director, on my stringed instruments.") was lifted out of v. 19's chunk list at parse time and matched as the standalone; the staged standalone paragraph itself stands untouched after v. 19, exactly as staged.

Verification: `verify_finish.py` (independent re-extraction, re-derivation under the ruling) — VERIFIED (surfaces identical on all five surfaces, re-derivation match).
