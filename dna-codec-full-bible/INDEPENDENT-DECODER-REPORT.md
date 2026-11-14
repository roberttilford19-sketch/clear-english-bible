# Independent Decoder Report — Bible DNA (full text)

Date: 2026-11-14
Decoder: independent decoder for Robert Tilford's Bible DNA lane
Script: `decode_bible_dna.py` in this deposit, written from the specification alone. The encoder's and validator's code (`encode_bible_dna.py` and `validate_bible_dna.py`, and anything under `work/`) was not read, imported, or copied.

## Codec used

Each base is two bits — A=00, C=01, G=10, T=11. Four bases make one byte, most significant pair first. The byte stream is exactly the source file's bytes (the file is UTF-8 text). Decoding and the spot-proof re-encoding were both implemented independently in the decoder script.

## Source of record

- Source file: `/home/hatch/workspace/ceb-push/editions/catholic/clear-english-bible-catholic-edition.txt`
- Sequence file: `bible-dna-full.txt` in this deposit (wrapped at 60 bases per line; all whitespace stripped before decoding).

## Figures computed

- Total bases in `bible-dna-full.txt` (all whitespace stripped): 19,268,252
- Bases use only A/C/G/T: yes
- Total bases divisible by 4: yes (19,268,252 / 4 = 4,817,063)
- Decoded bytes: 4,817,063
- Source bytes: 4,817,063
- SHA-256 of the decoded byte stream: `dd1cc76282229befcdf8ef6ad352f42c91f5dc9d7442bbea75aa9579529fdef3`
- SHA-256 of the source byte stream: `dd1cc76282229befcdf8ef6ad352f42c91f5dc9d7442bbea75aa9579529fdef3`
- SHA-256 of the base stream (stripped sequence as ASCII): `3341fe52b5bc2a8ac5558bc4c347824743839c99529854ec483a666cce934fd0`
- SHA-256 printed in `MANIFEST-DNA-FULL-BIBLE.md` for the source byte stream: `dd1cc76282229befcdf8ef6ad352f42c91f5dc9d7442bbea75aa9579529fdef3`
- SHA-256 printed in `MANIFEST-DNA-FULL-BIBLE.md` for the base stream: `3341fe52b5bc2a8ac5558bc4c347824743839c99529854ec483a666cce934fd0`

## Checks

a. Base count, alphabet, and divisibility — PASS. The stripped sequence holds 19,268,252 bases, matching the expected count; its alphabet is exactly {A, C, G, T}; and the count is divisible by 4 (19,268,252 / 4 = 4,817,063).

b. Full decode and UTF-8 — PASS. The full 19,268,252-base sequence decoded to 4,817,063 bytes, and those bytes decoded as UTF-8 with no error.

c. Decoded bytes vs. source file — PASS. The SHA-256 of the decoded bytes (`dd1cc76282229befcdf8ef6ad352f42c91f5dc9d7442bbea75aa9579529fdef3`) equals the SHA-256 of the source file's bytes (same value), and the two byte streams are equal byte-for-byte.

d. Manifest figures — PASS, both. The SHA-256 of the source byte stream computed here (`dd1cc76282229befcdf8ef6ad352f42c91f5dc9d7442bbea75aa9579529fdef3`) matches the figure printed in `MANIFEST-DNA-FULL-BIBLE.md`, and the SHA-256 of the base stream computed here (`3341fe52b5bc2a8ac5558bc4c347824743839c99529854ec483a666cce934fd0`) matches the figure printed in `MANIFEST-DNA-FULL-BIBLE.md`.

e. Spot proof — PASS for all three windows. Each window of source bytes was re-encoded with this decoder's own encoder logic and compared against the corresponding slice of the sequence file (byte offset × 4):

- First: source bytes 0–999 (1,000 bytes), base range 1–4000 (1-based), 4,000 bases — exact match.
- Middle: source bytes 2408031–2409030 (1,000 bytes centered on the file's midpoint), base range 9632125–9636124 (1-based), 4,000 bases — exact match.
- Last: source bytes 4816063–4817062 (1,000 bytes), base range 19264253–19268252 (1-based), 4,000 bases — exact match.

## Verdict

Every check passes: base count, alphabet, and divisibility; UTF-8 decode; byte-for-byte and hash equality with the source file; both manifest SHA-256 figures; and the three spot proofs.

VERDICT: PASS
