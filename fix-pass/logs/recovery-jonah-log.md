# Recovery Log — JONAH (Wave F: the minor prophets)

Worker: lineation-recovery worker, Wave F. Date: 2026-10-18.

**Ruling cited:** Ruling 8 as amended by the editor 2026-10-18 — where the recorded apparatuses do not carry a chapter's divisions in full, the divisions may be read from the base's own pages (public-domain WEB Classic at ebible.org), wording asserted identical chapter by chapter, stop rule where a page does not speak plainly, base-prose chapters never relineated, no division invented.

**Scope:** Jonah chapters 1, 2, 3, 4 (the whole Lane C stopped set for this book).

**Method:** `python3 recovery.py JONAH 1,2,3,4 --apply --readers-only` from `~/workspace/ceb-push/fix-pass`, then independent verification with `verify_recovery.py`. Writes confined to the two reader surfaces in staging (`books/`, `individual-books/`); no editions file touched; the live shelf not touched.

## Per-chapter dispositions (counts from fix-pass/recovery-results/JONAH.json)

| Chapter | Disposition | q | q2 | m | qs |
|---|---|---|---|---|---|
| Jonah 1 | PAGE-PROSE | 0 | 0 | 0 | 0 |
| Jonah 2 | RESTORED | 11 | 12 | 0 | 0 |
| Jonah 3 | PAGE-PROSE | 0 | 0 | 0 | 0 |
| Jonah 4 | PAGE-PROSE | 0 | 0 | 0 | 0 |

PAGE-PROSE reason (verbatim from the results file, all three chapters): "base page carries no q/q2/qs division in this chapter; nothing to restore; left as staged". No chapter in this book came back STOPPED. Only Jonah 2 — the psalm of Jonah — carries lineation in the base; chapters 1, 3, and 4 are base prose throughout and were never relineated, per the ruling.

## Totals

RESTORED 1 / PAGE-PROSE 3 / STOPPED 0. Divisions restored: q 11, q2 12, m 0, qs 0 — 23 in all.

## Verification summary

`python3 verify_recovery.py --readers JONAH:1,2,3,4` (run as part of the Wave F combined verification, and Jonah 4 re-run on its own to confirm) returned:

- Jonah 1: VERIFIED (poetic=False, surfaces_identical=True, rederive_match=True)
- Jonah 2: VERIFIED (poetic=True, surfaces_identical=True, rederive_match=True)
- Jonah 3: VERIFIED (poetic=False, surfaces_identical=True, rederive_match=True)
- Jonah 4: **MISMATCH (poetic=False, surfaces_identical=True, rederive_match=False)** — reproducible on re-run.

Note on the Jonah 4 mismatch: Jonah 4's disposition was PAGE-PROSE, for which the recovery script writes nothing anywhere, so this mismatch was not produced by this pass — the staged chapter, identical on both reader surfaces, does not match the chapter re-derived from the base page and the current staged wording. No hand-edit was made and no override attempted; the anomaly is reported to the coordinator exactly as returned.
