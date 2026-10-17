# Clear English Bible — Ruth Completion Report

**Date:** 2026-10-16 · **Book:** Ruth (4 chapters, 85 verses) · **Reader:** RUTH-reader.txt (2,586 words including header notes, counted by the method stated under Word count below)
**Status:** 4 of 4 chapters AUDITED. Everything stops at AUDITED pending Robert's read-through; nothing published, emailed, posted, or uploaded. This is audit-complete staging, not a finished or definitive text.

## Method
Drafted by Draft Crew U from the World English Bible Classic base fetched live from ebible.org (public domain); KJV/ASV (1901) controls only; no copyrighted modern translation used as a base or skeleton. Every chapter was then independently audited by Audit Crew U-1, a different crew than the drafter, verse-by-verse against the pinned WEB Classic base snapshot kept for each chapter: completeness and order, names, numbers, divine-name counts, banner and disclosure, plain-rendering fidelity, and no tradition-injected specifics. This book is a clear-English modernization from that public-domain base. It is not a fresh translation made directly from the Hebrew or Greek. The draft was prepared with AI assistance. Robert Tilford is the editor.

## Per-chapter audit verdicts

| Chapter | Verses | Yahweh (base = draft) | “Shall” in base | Conversions | Audit outcome |
|---------|--------|----------------------|---------------|-------------|---------------|
| Ruth 1 | 22 | 7 = 7 | 0 | None needed; no “shall” remains | PASS, no fixes |
| Ruth 2 | 23 | 5 = 5 | 1 | “must” 1 (v. 21); “will” 0 | PASS, no fixes |
| Ruth 3 | 18 | 2 = 2 | 4 | “will” 2 (v. 1; v. 4 opening); “must” 2 (both v. 4) | PASS, with the Ruth 3:1 flag carried as PENDING ROBERT (see Flags below); no fixes |
| Ruth 4 | 22 | 4 = 4 | 1 | “will” 1 (v. 15); “must” 0 | FIXED AND PASSED — apparatus only, no verse text changed (see Audit history) |
| **Book total** | **85** | **18 = 18** | **6** | **“must” 3; “will” 3** | **4 of 4 chapters AUDITED** |

The per-chapter verse counts are 22, 23, 18, and 22, which sum to the book total of 85 verses. The per-chapter Yahweh counts are 7, 5, 2, and 4, which sum to the book total of 18. The base's six “shall” occurrences are accounted for by six conversions in all, three to “must” and three to “will,” and no “shall” remains in the verses of any chapter. In Ruth 4 the base's own “must” at verse 5 is the base's wording, not a conversion, and it is not counted in the conversions above. “Behold” in the base is rendered “See” or “see” at Ruth 1:15, 2:4, 3:2, 3:8, and 4:1, as each chapter's apparatus discloses.

## Audit history
Ruth 1–4 were drafted by Draft Crew U and independently audited by Audit Crew U-1 on 2026-10-16. Chapters 1, 2, and 3 passed with no verse fix and no apparatus fix. Chapter 3 passes with one flag carried as PENDING ROBERT, stated in full under Flags below; the auditor neither accepted the rendering at 3:1 as lane-consistent nor changed it under audit authority, so the verse stands exactly as drafted. Chapter 4 was fixed and passed on one apparatus fix, disclosed here at the point of the claim: the kept-terms list in the chapter's apparatus had named “near kinsman” at verses 1, 3, and 14 only, but the phrase also occurs at verses 6 and 8, so the list was corrected to verses 1, 3, 6, 8, and 14, and the same list was corrected to separate “redeem” (verses 4 and 6) and “redeeming” (verse 7) and to place “right of redemption” at verse 6 alone. No verse text was changed by that fix. The reader was then assembled by Packaging Crew Ruth-1 from the audited chapter files only, and verified as stated under Outputs below.

## FLAGS CARRIED FOR ROBERT

1. **Ruth 3:1 — PENDING ROBERT.** The draft renders Naomi's deliberative “shall I not seek rest for you” as “will I not seek rest for you.” The auditor found that the drafter's claimed Genesis precedent does not exist. Genesis's “will I” questions are the base's own wording, kept and not converted, and the audited Genesis 30:31, Exodus 2:7, and Exodus 17:4 keep the base's deliberative “shall I.” The verse therefore stands as drafted, disclosed here and in the chapter's apparatus and audit record, awaiting Robert's ruling on one uniform treatment of deliberative “shall.” The same question is open at Joshua 7:8 and Judges 13:12.
2. **Kept kinship and redemption terms, and “lest.”** The kinship terms “near kinsman” and “near kinsmen,” “kinsman,” “the kinsman's duty” and “the duty of a kinsman,” and the redemption terms “redeem,” “redeeming,” and “right of redemption” are kept as the base's words, as is “lest” at Ruth 4:6. They are flagged in each chapter's apparatus for Robert's read-through, because no plainer word was found that carries them without loss or added interpretation, and the base's own terms were not modernized into different concepts.

Other kept terms — among them “Moabitess,” “glean,” “maidens,” “ephah,” “threshing floor,” “winnowing,” “mantle,” “parcel of land,” and “formalizing transactions” — are likewise kept as the base's words and flagged in the chapter apparatuses. Non-blocking plain-rendering notes are itemized in each chapter's apparatus and audit record.

## Word count
The reader's word count is 2,586 words, including its header notes. The count was made by this exact command, run from the goal folder (`~/workspace/goals/clear-english-bible-translation/`): `LC_ALL=C.UTF-8 wc -w files/RUTH-reader.txt`. The locale is named in the command because it matters: the same file counted by `wc -w` under the POSIX locale gives 2,582, as the plain-locale counter handles some multibyte characters differently. A cross-check by Python — `python3 -c "from pathlib import Path; print(len(Path('files/RUTH-reader.txt').read_text(encoding='utf-8').split()))"`, run from the same folder — also gives 2,586. The stated command reproduces the stated figure.

## Outputs
- 4 chapter slices: files/RUTH-01-DRAFT.md … files/RUTH-04-DRAFT.md (4 AUDITED).
- files/RUTH-reader.txt — all 4 chapters in order. Verification by Packaging Crew Ruth-1, by exact string count and by diff: the reader's verse blocks match the audited chapter files' verse sections exactly, chapter by chapter, with nothing altered, added, or dropped in assembly; the reader carries 85 verses in all (22, 23, 18, and 22); and “Yahweh” occurs 18 times in the reader, which equals the sum of the chapters' audited counts (7 + 5 + 2 + 4 = 18).
- This report.
