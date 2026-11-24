# Recovery Log — JOHN (Wave G: New Testament stopped set)

Worker: lineation-recovery worker, Wave G. Date: 2026-10-18.

**Ruling cited:** Ruling 8 as amended by the editor 2026-10-18 — where the recorded apparatuses do not carry a chapter's divisions in full, the divisions may be read from the base's own pages (public-domain WEB Classic at ebible.org), wording asserted identical chapter by chapter, stop rule where a page does not speak plainly, base-prose chapters never relineated, no division invented.

**Scope:** John chapters 1 and 12 (chapter 19 was restored by the pilot and was not re-run). Chapter 12 was stopped in Lane C-1 because the apparatus records only that the tail of v. 38 and the lines of v. 40 stand in q/q2 lines, with no counts and no line texts. Chapter 1's record (chapter apparatus and the JOHN completion report, flag 5) already establishes that the base sets the prologue, vv. 1–18, and the whole chapter in prose, so a PAGE-PROSE disposition was the expected outcome; it was run and recorded as below.

**Method:** `python3 recovery.py JOHN 1,12 --apply --readers-only` from `~/workspace/ceb-push/fix-pass`, then independent verification with `verify_recovery.py`. Writes confined to the two reader surfaces in staging (`books/`, `individual-books/`); no editions file touched; the live shelf not touched.

## Per-chapter dispositions (from fix-pass/recovery-results/JOHN.json)

| Chapter | Disposition | q | q2 | m | qs |
|---|---|---|---|---|---|
| John 1 | PAGE-PROSE | 0 | 0 | 0 | 0 |
| John 12 | RESTORED | 2 | 5 | 0 | 0 |

**John 1 — PAGE-PROSE.** The script's recorded reason: "base page carries no q/q2/qs division in this chapter; nothing to restore; left as staged." This is what the page shows, and it confirms the record: the base sets the prologue and the whole chapter in prose. Nothing was written; the chapter stands exactly as staged, and under the ruling a base-prose chapter is never relineated. This is the correct, expected outcome for this chapter — not a failure.

**John 12 — RESTORED** with 2 q and 5 q2 divisions (the Isaiah quotations at vv. 38 and 40). The Lane C-1 apparatus carried no counts for this chapter, so there is no apparatus-count comparison to make.

No chapter in this book came back STOPPED.

## Verification summary

`python3 verify_recovery.py --readers JOHN:1,12` returned **VERIFIED for both chapters**: John 1 (poetic=False, surfaces_identical=True, rederive_match=True) and John 12 (poetic=True, surfaces_identical=True, rederive_match=True). No verse text affected by words-of-Jesus (wj) spans was observed in any read-back.
