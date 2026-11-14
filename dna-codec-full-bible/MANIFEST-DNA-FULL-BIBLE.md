# MANIFEST — The Clear English Bible (Catholic Edition) Encoded in DNA Letters (full text, in silico)

Built 2026-11-14 at Robert Tilford's desk by Awen by Muse by Meta, in the lane
Robert commissioned the same day, as the companion deposit to the Quran DNA
lane completed earlier the same day. The codec is the house codec demonstrated
on the Bismillah and used for the full Quran: it was verified by machine at
this desk before this build began.

## What this is — and what it is not

This is an **in-silico encoding printed as data**: the complete text of the
Clear English Bible, Catholic Edition, taken from the source file of record
below, written in the four DNA letters A, C, G, T under the codec stated
below. It is an **encoding, not a translation**: no wording was translated,
modernized, or altered in any way by this lane — the source file's bytes were
converted, exactly as they stand, and decoding returns them exactly.
**Nothing has been synthesized. No physical DNA exists.** Physical synthesis
is a separate, future, funded laboratory project and is not part of this
deposit. No claim of priority or firstness is made anywhere in this deposit:
what is claimed is only what the verification figures below prove.

## The codec (exactly the house codec)

Text as UTF-8 bytes → binary bits, most significant bit first → every two
bits become one base: **00 = A, 01 = C, 10 = G, 11 = T**. One byte becomes
four bases. The mapping is lossless and reversible: decoding the base stream
returns the byte stream exactly, which the independent decoder's report in
this deposit proves by hash.

## Source of record

- Source file: `editions/catholic/clear-english-bible-catholic-edition.txt`
  in Robert Tilford's Clear English Bible repository (the packaged Catholic
  Edition volume: all 73 books of the Catholic canon, 1,328 chapters,
  including its own front matter and each book's packaged header, encoded
  entire and exactly as it stands).
- The file was encoded **by code, byte for byte, never retyped**: the
  encoded stream is the file itself, front matter, book headers, draft
  histories, and all.
- Source file size: **4,817,063 bytes**
- SHA-256 of the source byte stream: `dd1cc76282229befcdf8ef6ad352f42c91f5dc9d7442bbea75aa9579529fdef3`
- Base stream: **19,268,252 bases** (4 per byte)
- SHA-256 of the base stream: `3341fe52b5bc2a8ac5558bc4c347824743839c99529854ec483a666cce934fd0`

## Structure of the encoded stream

The stream follows the source file's own structure, parsed by code and
verified as it was parsed: the edition's front matter, then for each of the
73 books its packaged header followed by its chapters in order — 1,328
chapter headings in all, each book's chapters sequential and matching the
chapter range its header declares. (One naming note, as printed in the
source: the book headed "Psalms" heads its chapters "Psalm N".) The printed
book deposited with this manifest carries the full chapter-by-chapter index
with base ranges; the table below gives each book's range in the stream.

## Per-book index

| # | Book | Chapters | Source bytes | Bases | Base range |
|---|---|---|---|---|---|
| 1 | Genesis | 50 | 194,847 | 779,388 | 13,409–792,796 |
| 2 | Exodus | 40 | 167,105 | 668,420 | 792,797–1,461,216 |
| 3 | Leviticus | 27 | 125,225 | 500,900 | 1,461,217–1,962,116 |
| 4 | Numbers | 36 | 173,088 | 692,352 | 1,962,117–2,654,468 |
| 5 | Deuteronomy | 34 | 144,879 | 579,516 | 2,654,469–3,233,984 |
| 6 | Joshua | 24 | 98,998 | 395,992 | 3,233,985–3,629,976 |
| 7 | Judges | 21 | 98,494 | 393,976 | 3,629,977–4,023,952 |
| 8 | Ruth | 4 | 14,035 | 56,140 | 4,023,953–4,080,092 |
| 9 | 1 Samuel | 31 | 128,365 | 513,460 | 4,080,093–4,593,552 |
| 10 | 2 Samuel | 24 | 106,393 | 425,572 | 4,593,553–5,019,124 |
| 11 | 1 Kings | 22 | 125,214 | 500,856 | 5,019,125–5,519,980 |
| 12 | 2 Kings | 25 | 120,817 | 483,268 | 5,519,981–6,003,248 |
| 13 | 1 Chronicles | 29 | 111,720 | 446,880 | 6,003,249–6,450,128 |
| 14 | 2 Chronicles | 36 | 138,527 | 554,108 | 6,450,129–7,004,236 |
| 15 | Ezra | 10 | 41,025 | 164,100 | 7,004,237–7,168,336 |
| 16 | Nehemiah | 13 | 57,950 | 231,800 | 7,168,337–7,400,136 |
| 17 | Tobit | 14 | 37,195 | 148,780 | 7,400,137–7,548,916 |
| 18 | Judith | 16 | 60,379 | 241,516 | 7,548,917–7,790,432 |
| 19 | Esther | 10 | 41,168 | 164,672 | 7,790,433–7,955,104 |
| 20 | Job | 42 | 98,997 | 395,988 | 7,955,105–8,351,092 |
| 21 | Psalms | 150 | 238,058 | 952,232 | 8,351,093–9,303,324 |
| 22 | Proverbs | 31 | 81,763 | 327,052 | 9,303,325–9,630,376 |
| 23 | Ecclesiastes | 12 | 29,880 | 119,520 | 9,630,377–9,749,896 |
| 24 | Song of Songs | 8 | 15,138 | 60,552 | 9,749,897–9,810,448 |
| 25 | Wisdom | 19 | 59,871 | 239,484 | 9,810,449–10,049,932 |
| 26 | Sirach | 51 | 151,073 | 604,292 | 10,049,933–10,654,224 |
| 27 | Isaiah | 66 | 197,589 | 790,356 | 10,654,225–11,444,580 |
| 28 | Jeremiah | 52 | 227,571 | 910,284 | 11,444,581–12,354,864 |
| 29 | Lamentations | 5 | 20,002 | 80,008 | 12,354,865–12,434,872 |
| 30 | Baruch | 6 | 27,934 | 111,736 | 12,434,873–12,546,608 |
| 31 | Ezekiel | 48 | 206,221 | 824,884 | 12,546,609–13,371,492 |
| 32 | Greek Daniel | 14 | 83,631 | 334,524 | 13,371,493–13,706,016 |
| 33 | Hosea | 14 | 29,329 | 117,316 | 13,706,017–13,823,332 |
| 34 | Joel | 3 | 11,827 | 47,308 | 13,823,333–13,870,640 |
| 35 | Amos | 9 | 23,140 | 92,560 | 13,870,641–13,963,200 |
| 36 | Obadiah | 1 | 4,252 | 17,008 | 13,963,201–13,980,208 |
| 37 | Jonah | 4 | 7,591 | 30,364 | 13,980,209–14,010,572 |
| 38 | Micah | 7 | 17,302 | 69,208 | 14,010,573–14,079,780 |
| 39 | Nahum | 3 | 7,540 | 30,160 | 14,079,781–14,109,940 |
| 40 | Habakkuk | 3 | 8,711 | 34,844 | 14,109,941–14,144,784 |
| 41 | Zephaniah | 3 | 9,336 | 37,344 | 14,144,785–14,182,128 |
| 42 | Haggai | 2 | 6,622 | 26,488 | 14,182,129–14,208,616 |
| 43 | Zechariah | 14 | 33,472 | 133,888 | 14,208,617–14,342,504 |
| 44 | Malachi | 4 | 10,516 | 42,064 | 14,342,505–14,384,568 |
| 45 | 1 Maccabees | 16 | 125,809 | 503,236 | 14,384,569–14,887,804 |
| 46 | 2 Maccabees | 15 | 96,356 | 385,424 | 14,887,805–15,273,228 |
| 47 | Matthew | 28 | 128,644 | 514,576 | 15,273,229–15,787,804 |
| 48 | Mark | 16 | 82,304 | 329,216 | 15,787,805–16,117,020 |
| 49 | Luke | 24 | 138,102 | 552,408 | 16,117,021–16,669,428 |
| 50 | John | 21 | 103,237 | 412,948 | 16,669,429–17,082,376 |
| 51 | Acts | 28 | 131,404 | 525,616 | 17,082,377–17,607,992 |
| 52 | Romans | 16 | 53,470 | 213,880 | 17,607,993–17,821,872 |
| 53 | 1 Corinthians | 16 | 52,075 | 208,300 | 17,821,873–18,030,172 |
| 54 | 2 Corinthians | 13 | 34,200 | 136,800 | 18,030,173–18,166,972 |
| 55 | Galatians | 6 | 18,023 | 72,092 | 18,166,973–18,239,064 |
| 56 | Ephesians | 6 | 17,998 | 71,992 | 18,239,065–18,311,056 |
| 57 | Philippians | 4 | 12,955 | 51,820 | 18,311,057–18,362,876 |
| 58 | Colossians | 4 | 12,055 | 48,220 | 18,362,877–18,411,096 |
| 59 | 1 Thessalonians | 5 | 10,976 | 43,904 | 18,411,097–18,455,000 |
| 60 | 2 Thessalonians | 3 | 6,573 | 26,292 | 18,455,001–18,481,292 |
| 61 | 1 Timothy | 6 | 14,150 | 56,600 | 18,481,293–18,537,892 |
| 62 | 2 Timothy | 4 | 10,164 | 40,656 | 18,537,893–18,578,548 |
| 63 | Titus | 3 | 6,234 | 24,936 | 18,578,549–18,603,484 |
| 64 | Philemon | 1 | 3,247 | 12,988 | 18,603,485–18,616,472 |
| 65 | Hebrews | 13 | 39,889 | 159,556 | 18,616,473–18,776,028 |
| 66 | James | 5 | 13,323 | 53,292 | 18,776,029–18,829,320 |
| 67 | 1 Peter | 5 | 14,626 | 58,504 | 18,829,321–18,887,824 |
| 68 | 2 Peter | 3 | 9,653 | 38,612 | 18,887,825–18,926,436 |
| 69 | 1 John | 5 | 13,862 | 55,448 | 18,926,437–18,981,884 |
| 70 | 2 John | 1 | 2,465 | 9,860 | 18,981,885–18,991,744 |
| 71 | 3 John | 1 | 2,449 | 9,796 | 18,991,745–19,001,540 |
| 72 | Jude | 1 | 4,447 | 17,788 | 19,001,541–19,019,328 |
| 73 | Revelation | 22 | 62,231 | 248,924 | 19,019,329–19,268,252 |

## Files in this deposit

- `bible-dna-full.txt` — the full base stream, wrapped at 60 bases per line.
- `MANIFEST-DNA-FULL-BIBLE.md` — this manifest.
- `encode_bible_dna.py` — the encoder (structure parse + encoding).
- `validate_bible_dna.py` — the hygiene validator (report-only).
- `decode_bible_dna.py` — the independent decoder, written separately.
- `INDEPENDENT-DECODER-REPORT.md` — the decoder's verdict, preserved unedited.
- `BIBLE-DNA-FULL-PRINT.pdf` — the paper book typeset from the verified
  sequence file.

## Codec hygiene (validator — report only)

- Alphabet: A, C, G, T only — pure.
- Base counts: A 5,131,884 · C 6,270,165 · G 5,025,800 · T 2,840,403
- GC content: 58.6248%
- Homopolymer runs: 15,301,611 in total; longest run **7**;
  runs of length ≥ 4: 1,758 · ≥ 5: 410 · ≥ 6: 79 · ≥ 8: 0 · ≥ 10: 0

The sequence was **not** altered to improve these figures; they are disclosed
for any future synthesis discussion. One honest difference from the Quran
lane is recorded here in the same breath: that lane's Arabic stream's longest
homopolymer run was 4, while this English text's longest is 7 — a single run
of seven C's in Revelation, arising from the plain ASCII wording (the runs of
six arise chiefly from the books' own packaged "(AUDITED)" header lines).
English text under this fixed codec produces such runs; the codec and the
source were both left exactly as they stand, and the round-trip proof below
is unaffected. A synthesis-grade layer would add screening, addressing, and
error correction on top of this codec.

## Independent verification

A separate agent wrote an independent decoder from the specification alone —
no encoder or validator code read or shared — and ran it end to end.
**VERDICT: PASS.** Its decoded bytes are byte-for-byte equal to the source
file and hash to `dd1cc76282229befcdf8ef6ad352f42c91f5dc9d7442bbea75aa9579529fdef3`,
the source figure printed above; the base stream hashes to
`3341fe52b5bc2a8ac5558bc4c347824743839c99529854ec483a666cce934fd0`, also as printed above.
Its spot proofs re-encoded the first, middle, and last 1,000 source bytes
with its own logic and matched the sequence exactly at each place
(19,268,252 bases in total; 4,817,063 bytes decoded). Its report,
`INDEPENDENT-DECODER-REPORT.md`, is preserved unedited in this deposit.
