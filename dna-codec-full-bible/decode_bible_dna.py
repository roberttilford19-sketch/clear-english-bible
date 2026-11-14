#!/usr/bin/env python3
"""Independent decoder for the Bible DNA lane.

Written from the written specification alone:
  Each base is two bits -- A=00, C=01, G=10, T=11.
  Four bases make one byte, most significant pair first.
  The byte stream is exactly the source file's bytes (UTF-8 text).

This script does not import or reuse any encoder/validator code.
"""
import hashlib
import re
import sys
from pathlib import Path

WORK = Path(__file__).resolve().parent
SEQ_PATH = WORK / "bible-dna-full.txt"
MANIFEST_PATH = WORK / "MANIFEST-DNA-FULL-BIBLE.md"
SOURCE_PATH = Path("/home/hatch/workspace/ceb-push/editions/catholic/clear-english-bible-catholic-edition.txt")

EXPECTED_BASES = 19268252

BASE_TO_BITS = {"A": 0, "C": 1, "G": 2, "T": 3}
BITS_TO_BASE = {0: "A", 1: "C", 2: "G", 3: "T"}


def decode_sequence(seq: str) -> bytes:
    """Decode a base string to bytes: 4 bases -> 1 byte, MS pair first."""
    # Translate bases to their 2-bit values as raw bytes (0..3) for speed.
    table = bytes.maketrans(b"ACGT", bytes([0, 1, 2, 3]))
    vals = seq.encode("ascii").translate(table)
    out = bytearray(len(vals) // 4)
    j = 0
    for i in range(0, len(vals), 4):
        out[j] = (vals[i] << 6) | (vals[i + 1] << 4) | (vals[i + 2] << 2) | vals[i + 3]
        j += 1
    return bytes(out)


def encode_bytes(data: bytes) -> str:
    """Re-encode bytes to bases with independent logic (for spot proof)."""
    parts = []
    for b in data:
        parts.append(BITS_TO_BASE[(b >> 6) & 0b11])
        parts.append(BITS_TO_BASE[(b >> 4) & 0b11])
        parts.append(BITS_TO_BASE[(b >> 2) & 0b11])
        parts.append(BITS_TO_BASE[b & 0b11])
    return "".join(parts)


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    checks = {}

    # 1. Read sequence, strip whitespace, count, alphabet, divisibility.
    raw_seq_text = SEQ_PATH.read_text(encoding="ascii")
    seq = "".join(raw_seq_text.split())
    total_bases = len(seq)
    print(f"Total bases (whitespace stripped): {total_bases}")
    print(f"Expected bases: {EXPECTED_BASES}")
    checks["base_count_matches_expected"] = (total_bases == EXPECTED_BASES)
    print(f"Base count matches expected: {checks['base_count_matches_expected']}")

    alphabet = set(seq)
    print(f"Alphabet observed: {sorted(alphabet)}")
    checks["alphabet_ok"] = alphabet.issubset({"A", "C", "G", "T"})
    print(f"Alphabet subset of {{A,C,G,T}}: {checks['alphabet_ok']}")

    checks["divisible_by_4"] = (total_bases % 4 == 0)
    print(f"Total bases divisible by 4: {checks['divisible_by_4']} ({total_bases} / 4 = {total_bases // 4})")

    # 2. Decode full sequence.
    decoded = decode_sequence(seq)
    print(f"Decoded bytes: {len(decoded)}")

    # UTF-8 sanity (spec says byte stream is UTF-8 text)
    try:
        decoded.decode("utf-8")
        checks["utf8_ok"] = True
    except UnicodeDecodeError as e:
        checks["utf8_ok"] = False
        print(f"UTF-8 decode error: {e}")
    print(f"Decoded bytes are valid UTF-8: {checks['utf8_ok']}")

    # 3. Source comparison + hashes.
    source = SOURCE_PATH.read_bytes()
    print(f"Source bytes: {len(source)}")
    checks["byte_for_byte_equal"] = (decoded == source)
    print(f"Decoded bytes equal source byte-for-byte: {checks['byte_for_byte_equal']}")

    h_decoded = sha256_hex(decoded)
    h_source = sha256_hex(source)
    h_bases = sha256_hex(seq.encode("ascii"))
    print(f"SHA-256 of decoded bytes: {h_decoded}")
    print(f"SHA-256 of source bytes: {h_source}")
    print(f"SHA-256 of base stream (stripped, ASCII): {h_bases}")
    checks["decoded_hash_equals_source_hash"] = (h_decoded == h_source)
    print(f"Decoded hash equals source hash: {checks['decoded_hash_equals_source_hash']}")

    # 4. Manifest figures.
    manifest_text = MANIFEST_PATH.read_text(encoding="utf-8")
    m_src = re.search(r"SHA-256 of the source byte stream:\s*`([0-9a-f]{64})`", manifest_text)
    m_base = re.search(r"SHA-256 of the base stream:\s*`([0-9a-f]{64})`", manifest_text)
    if not m_src or not m_base:
        print("ERROR: could not parse SHA-256 figures from manifest")
        return 1
    manifest_source_hash = m_src.group(1)
    manifest_base_hash = m_base.group(1)
    print(f"SHA-256 printed in manifest for source byte stream: {manifest_source_hash}")
    print(f"SHA-256 printed in manifest for base stream: {manifest_base_hash}")
    checks["manifest_source_hash_match"] = (h_source == manifest_source_hash and h_decoded == manifest_source_hash)
    checks["manifest_base_hash_match"] = (h_bases == manifest_base_hash)
    print(f"Manifest source hash matches computed: {checks['manifest_source_hash_match']}")
    print(f"Manifest base hash matches computed: {checks['manifest_base_hash_match']}")

    # 5. Spot proof: re-encode three 1,000-byte windows and compare to seq slices.
    n = len(source)
    mid_start = n // 2 - 500
    windows = [
        ("first", 0, source[0:1000]),
        ("middle", mid_start, source[mid_start:mid_start + 1000]),
        ("last", n - 1000, source[n - 1000:n]),
    ]
    spot_results = {}
    for label, byte_offset, chunk in windows:
        re_enc = encode_bytes(chunk)
        base_start = byte_offset * 4
        base_end = base_start + len(chunk) * 4
        seq_slice = seq[base_start:base_end]
        ok = (re_enc == seq_slice)
        spot_results[label] = ok
        print(
            f"Spot proof [{label}]: source bytes {byte_offset}-{byte_offset + len(chunk) - 1} "
            f"(1000 bytes), base range {base_start + 1}-{base_end} (1-based), "
            f"{len(re_enc)} bases re-encoded, exact match: {ok}"
        )
    checks["spot_first"] = spot_results["first"]
    checks["spot_middle"] = spot_results["middle"]
    checks["spot_last"] = spot_results["last"]

    # 6. Verdict.
    print("--- Checks summary ---")
    all_pass = True
    for k, v in checks.items():
        print(f"{k}: {'PASS' if v else 'FAIL'}")
        all_pass = all_pass and bool(v)
    print(f"OVERALL: {'PASS' if all_pass else 'FAIL'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
