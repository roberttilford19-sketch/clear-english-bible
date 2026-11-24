# Recovery Log — 1 CORINTHIANS (Wave G: New Testament stopped set)

Worker: lineation-recovery worker, Wave G. Date: 2026-10-18.

**Ruling cited:** Ruling 8 as amended by the editor 2026-10-18 — where the recorded apparatuses do not carry a chapter's divisions in full, the divisions may be read from the base's own pages (public-domain WEB Classic at ebible.org), wording asserted identical chapter by chapter, stop rule where a page does not speak plainly, base-prose chapters never relineated, no division invented.

**Scope:** 1 Corinthians chapters 1 and 2 only. These chapters were stopped in Lane C-1 because the apparatuses record only the location of the quotations (ch. 1, Isaiah quotation at v. 19; ch. 2, quotation at v. 9), with no division count and no line texts. **1 Corinthians 13 was not touched** (base-prose, outside scope entirely), and no other chapter of this book was touched.

**Method:** `python3 recovery.py 1-CORINTHIANS 1,2 --apply --readers-only` from `~/workspace/ceb-push/fix-pass`, then independent verification with `verify_recovery.py`. Writes confined to the two reader surfaces in staging (`books/`, `individual-books/`); no editions file touched; the live shelf not touched.

## Per-chapter dispositions (counts from fix-pass/recovery-results/1-CORINTHIANS.json)

| Chapter | Disposition | q | q2 | m | qs |
|---|---|---|---|---|---|
| 1 Corinthians 1 | RESTORED | 1 | 1 | 0 | 0 |
| 1 Corinthians 2 | RESTORED | 1 | 2 | 0 | 0 |

No chapter in this book came back PAGE-PROSE or STOPPED. (The Lane C-1 apparatuses carried no counts for either chapter, so there is no apparatus-count comparison to make for this book.)

## Verification summary

`python3 verify_recovery.py --readers 1-CORINTHIANS:1,2` returned **VERIFIED for both chapters** (poetic=True, surfaces_identical=True, rederive_match=True on both). No verse text affected by words-of-Jesus (wj) spans was observed in any read-back.
