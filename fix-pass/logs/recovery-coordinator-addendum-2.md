# RECOVERY PASS — COORDINATOR ADDENDUM 2 (2026-10-18)

## The book-final trailing-newline artifact (Ezekiel 48, Jonah 4) — verifier artifact, no defect

Two PAGE-PROSE chapters came back MISMATCH from verify_recovery.py: Ezekiel 48 (Wave E)
and Jonah 4 (Wave F), both reproducible. The coordinator diagnosed both directly. In each
case the chapter is the book's LAST chapter, the staged reader file ends with a trailing
newline byte, and the chapter's final paragraph therefore carries that "\n" in its raw
slice, while the verifier's re-derivation compares against the stripped paragraph. The
normalized word streams are identical (checked explicitly for Jonah 4: norm equal, True);
both reader surfaces are identical to each other; recovery wrote nothing for either
chapter (both are page-prose). Some staged reader files end with a final newline and
some do not (e.g., the EZEKIEL and JONAH readers do; the JOB reader does not) — a
pre-existing byte in the staged tree, outside this pass. Disposition: accepted as a
verifier artifact. No file is normalized; the pass does not edit bytes it was not
authorized to touch. In the final sweep, any book-final MISMATCH must be checked for
this signature (trailing "\n" only, norm streams equal) before being treated as a defect.

## Habakkuk 3 — the colophon stop, anatomy recorded for the desk

Habakkuk 3 stopped: standalone mismatch — staged standalones ['For the music director,
on my stringed instruments.'] vs base []. The coordinator inspected the cached page:
the colophon stands on the base page as a `p` block AFTER verse 19's closing q2 lines —
a separate block, not part of the verse's lines, exactly as the staged text carries it
(as its own paragraph after v. 19). The parser, however, assigns a trailing prose block
to the current verse as a prose chunk, so the base parse reports no standalone and the
chapter's standalone assertion fails before any rebuild. The two arrangements agree in
substance — neither side treats the line as verse text — but the pass's standalone rule
matches only base `d` blocks against staged standalone paragraphs.

Proposed narrow rule, for the desk's ruling: where a chapter's final prose block on the
base page equals, word for word, a staged standalone paragraph standing after the last
verse, the block may be matched as that standalone (the staged paragraph itself stays
untouched; the last verse is rebuilt without the block). Verse 19's lineation itself is
fully recorded on the page (the chapter carries 23 q and 38 q2 in all). The chapter
stands STOPPED, as staged, until the desk rules. The pattern is unique in the canon to
this colophon; no other wave met it.

## Psalms concurrency note (Waves A1/A2) — coordinator's design error, guard stated

Waves A1 and A2 wrote the SAME two Psalms reader files concurrently (disjoint chapters,
whole-file splice per chapter). Whole-file read-splice-write from two processes can
lose a chapter's restore when the writes interleave. Wave A2's first verification pass
caught exactly this signature on Psalms 125, 142, 148 (reader surfaces disagreeing /
re-derivation mismatch); the worker's idempotent re-runs of those three chapters healed
them, and A2's final full-range verification is clean. Guard for the whole book: after
Wave A1 lands, the coordinator will run a FULL 150-chapter re-derivation verification
of the Psalms readers, re-run any chapter that does not verify, and only then transplant
the editions. No Psalms edition transplant has been made yet.
