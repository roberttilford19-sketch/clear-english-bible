# CORRECTIONS — Bible DNA deposit (2026-11-14)

Dated corrections note for the deposit in this folder
(`dna-codec-full-bible/` in Robert Tilford's Clear English Bible
repository), first deposited 2026-11-14 in commit
`f81ffd77db9bf8d76f26f08565976881613b7816`.

## Why this note exists

After the deposit landed, the encoding was audited from outside the desk.
Grok Bot and Spokbot each decoded the deposited sequence with their own
code and recovered the source file byte for byte, and The EYE reviewed
the deposit's paperwork. Their combined report reached Robert Tilford by
email on 2026-11-14 and was graded at his desk. The decodings confirmed
the sequence; the paperwork findings below were verified one by one
against the deposited files, and every one of them was real. This note
records each fix and its reason. The original deposit record is not
rewritten; this note rides beside it.

## The DNA sequence did not change

The corrections are paperwork only. `bible-dna-full.txt` is byte-unchanged:

- SHA-256 of `bible-dna-full.txt` before the corrections:
  `3437561de1f49137acc4f1c7a0afcff784b332851523c91fa624466c07b1b9f8`
- SHA-256 of `bible-dna-full.txt` after the corrections:
  `3437561de1f49137acc4f1c7a0afcff784b332851523c91fa624466c07b1b9f8`
- SHA-256 of the base stream (whitespace stripped), before and after:
  `3341fe52b5bc2a8ac5558bc4c347824743839c99529854ec483a666cce934fd0`

Not one letter of the sequence was altered.

## Fixes made

1. **"Funded" removed (manifest and the printed book's front matter).**
   The manifest described physical synthesis as "a separate, future,
   funded laboratory project." Nothing supports the word "funded": no
   funding exists or was shown. Both texts now read that synthesis "is a
   separate future step that would require funding and a laboratory; no
   funding is in place and no physical DNA has been made."

2. **Internal machine path scrubbed.** The decoder report named the
   source file by an internal machine path (`/home/hatch/workspace/...`),
   and the decode script carried the same path hardcoded. The report now
   refers to "the source edition file in the Bible repository," and
   `decode_bible_dna.py` now takes the source file's path as a
   command-line argument (defaulting to the edition file's location
   relative to this folder in the repository). The corrected script was
   re-run end to end and returned PASS on every check, including the
   byte-for-byte and hash equality with the source.

3. **"Independent" corrected to "separate."** The desk's decoder was
   written and run by a separate agent in the same house, from the
   specification alone — separate, but not a third-party auditor, and
   the deposit's wording now says so in the manifest, in the decoder
   report, and in the printed book's front matter. (The report's file
   name, `INDEPENDENT-DECODER-REPORT.md`, is kept as originally
   deposited; the manifest now glosses it.) Genuinely external
   decodings did happen afterward — Grok Bot's and Spokbot's, above —
   and are recorded here, in this note, not retro-claimed in the
   report itself.

4. **Printed book rebuilt with its name on it.** The PDF's metadata
   read Title "untitled" and Author "anonymous." The book was rebuilt
   from the same typesetting pipeline with Title "The Clear English
   Bible in DNA — Catholic Edition (encoded 2026-11-14)" and Author
   "Robert Tilford," and with the front-matter wording corrections of
   items 1 and 3. The cosmetic grammar "1 chapters" was also corrected
   to "1 chapter" for the five one-chapter books (Obadiah, Philemon,
   2 John, 3 John, Jude) in Appendix A. After the rebuild the printed
   stream was re-verified in full: the bases extracted from all 3,719
   pages total exactly 19,268,252 and equal the deposited sequence
   exactly, and the head/midpoint/tail decode checks pass. New figures:
   **3,719 pages**, **10,398,830 bytes**, SHA-256
   `726df666b7a31b9a200e4595e589c9a1c6a45b0e79d278caf24d59ae74d3a13f`
   (the first printing was 10,398,699 bytes, SHA-256
   `d4dd91e23e6e186571bbef78ce3fd8c90b1649dc92733bce6eff0d70dfc24a2d`).

5. **Manifest updated** with the new PDF figures and the corrected
   wording above.

## Open

- LICENSE file: pending the author's ruling. No license file is added
  by this corrections pass; the gift wording in the source and in the
  printed book stands as it is until Robert rules.
