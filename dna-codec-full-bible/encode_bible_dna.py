#!/usr/bin/env python3
"""ENCODER — Bible DNA lane (2026-11-14).
Encodes the ENTIRE Clear English Bible, Catholic Edition, exactly as it
stands, byte for byte, with the house codec (UTF-8 bytes -> bits MSB-first
-> 00=A 01=C 10=G 11=T). No extraction, no retyping: the source file's raw
bytes are the stream. Also parses the source's own structure (73 book
headers, 1,328 chapter headings) to record per-book and per-chapter byte
and base ranges for the printed book's index. Aborts on any mismatch."""
import hashlib, json, re, sys
from pathlib import Path

ROOT = Path.home() / "workspace"
LANE = ROOT / "dna-bible-2026-11-14"
SOURCE = ROOT / "ceb-push/editions/catholic/clear-english-bible-catholic-edition.txt"
EXPECTED_BYTES = 4817063
EXPECTED_SHA256 = "dd1cc76282229befcdf8ef6ad352f42c91f5dc9d7442bbea75aa9579529fdef3"

raw = SOURCE.read_bytes()
if len(raw) != EXPECTED_BYTES:
    sys.exit(f"ABORT: source is {len(raw)} bytes, expected {EXPECTED_BYTES}")
sha = hashlib.sha256(raw).hexdigest()
if sha != EXPECTED_SHA256:
    sys.exit(f"ABORT: source SHA-256 {sha} != expected {EXPECTED_SHA256}")
text = raw.decode("utf-8")

# ---- structure parse (line-based; byte offsets accumulated incrementally) ----
lines = text.split("\n")
offsets = []
pos = 0
for l in lines:
    offsets.append(pos)
    pos += len(l.encode("utf-8")) + 1  # +1 for the '\n'
assert pos - 1 == len(raw) or (pos == len(raw) + 1 and lines[-1] == "")

BOOK_HEADER_RE = re.compile(
    r"^Clear English Bible — (.+?) \((?:Chapters?|Psalms) (\d+)(?:–(\d+))?\):")
CHAP_RE = re.compile(r"^((?:[123] )?[A-Z][A-Za-z ]*?) (\d+)$")

book_headers = []   # (line_idx, book_name, first_ch, last_ch)
chapters = []       # (line_idx, book_name, ch_no)
for i, l in enumerate(lines):
    m = BOOK_HEADER_RE.match(l)
    if m:
        first = int(m.group(2))
        last = int(m.group(3)) if m.group(3) else first
        book_headers.append((i, m.group(1), first, last))
        continue
    m = CHAP_RE.match(l.strip())
    if m and len(l.strip()) < 40:
        chapters.append((i, m.group(1), int(m.group(2))))

if len(book_headers) != 73:
    sys.exit(f"ABORT: found {len(book_headers)} book headers, expected 73")
if len(chapters) != 1328:
    sys.exit(f"ABORT: found {len(chapters)} chapter headings, expected 1328")

# group chapters under books; verify sequence and header ranges
books = []
ci = 0
for bi, (hi, name, first_ch, last_ch) in enumerate(book_headers):
    hend = book_headers[bi + 1][0] if bi + 1 < len(book_headers) else len(lines)
    bchaps = []
    chap_names = set()
    while ci < len(chapters) and chapters[ci][0] < hend:
        li, bname, n = chapters[ci]
        chap_names.add(bname)
        bchaps.append((li, n))
        ci += 1
    if len(chap_names) != 1:
        sys.exit(f"ABORT: book '{name}' has mixed chapter-heading names {chap_names}")
    chap_name = chap_names.pop()
    # header name and chapter-heading name may differ (Psalms / Psalm N)
    if chap_name != name and not (name == "Psalms" and chap_name == "Psalm"):
        sys.exit(f"ABORT: chapter headings '{chap_name}' inside book '{name}'")
    nums = [n for _, n in bchaps]
    if nums != list(range(first_ch, last_ch + 1)):
        sys.exit(f"ABORT: book '{name}' chapters {nums[:5]}... != header range {first_ch}-{last_ch}")
    books.append({"book": name, "chapter_name": chap_name, "header_line": hi,
                  "first_chapter": first_ch,
                  "last_chapter": last_ch, "chapter_lines": bchaps})
if ci != len(chapters):
    sys.exit("ABORT: unassigned chapter headings remain")

def byte_span(start_line, end_line_exclusive):
    s = offsets[start_line]
    e = offsets[end_line_exclusive] if end_line_exclusive < len(lines) else len(raw)
    return s, e

segments = []  # (label, kind, byte_start, byte_end)
segments.append(("Front matter of the edition", "front",
                 0, offsets[book_headers[0][0]]))
for bi, b in enumerate(books):
    next_header = book_headers[bi + 1][0] if bi + 1 < len(book_headers) else len(lines)
    hs, he = byte_span(b["header_line"], b["chapter_lines"][0][0])
    segments.append((f"Book header — {b['book']}", "book_header", hs, he))
    b["byte_start"], b["byte_end"] = byte_span(b["header_line"], next_header)
    b["chapters"] = []
    for k, (li, n) in enumerate(b["chapter_lines"]):
        end_line = b["chapter_lines"][k + 1][0] if k + 1 < len(b["chapter_lines"]) else next_header
        cs, ce = byte_span(li, end_line)
        b["chapters"].append({"chapter": n, "byte_start": cs, "byte_end": ce,
                              "base_start": cs * 4 + 1, "base_end": ce * 4})
        segments.append((f"{b['book']} {n}", "chapter", cs, ce))
    b["base_start"] = b["byte_start"] * 4 + 1
    b["base_end"] = b["byte_end"] * 4

# segments must tile the file exactly
cursor = 0
for label, kind, s, e in segments:
    assert s == cursor, f"gap/overlap before segment {label}: {s} != {cursor}"
    cursor = e
assert cursor == len(raw), f"segments end at {cursor}, file is {len(raw)}"

# ---- encode ----
ENC = {"00": "A", "01": "C", "10": "G", "11": "T"}
table = []
for byte in range(256):
    bits = f"{byte:08b}"
    table.append("".join(ENC[bits[i:i + 2]] for i in range(0, 8, 2)))
bases = "".join(table[b] for b in raw)
assert len(bases) == 4 * len(raw) == 19268252

seq_path = LANE / "bible-dna-full.txt"
with seq_path.open("w", encoding="ascii") as f:
    for i in range(0, len(bases), 60):
        f.write(bases[i:i + 60] + "\n")

sha_bases = hashlib.sha256(bases.encode("ascii")).hexdigest()
fig = {"source_file": str(SOURCE), "source_bytes": len(raw), "source_sha256": sha,
       "total_bases": len(bases), "sha256_base_stream": sha_bases,
       "books": [{k: v for k, v in b.items() if k != "chapter_lines"} for b in books],
       "segments": [{"label": l, "kind": k, "byte_start": s, "byte_end": e,
                     "base_start": s * 4 + 1, "base_end": e * 4}
                    for l, k, s, e in segments]}
(LANE / "work").mkdir(exist_ok=True)
(LANE / "work/encoder.json").write_text(json.dumps(fig, indent=1), encoding="utf-8")
print(json.dumps({"source_bytes": len(raw), "source_sha256": sha,
                  "total_bases": len(bases), "sha256_base_stream": sha_bases,
                  "books": len(books), "chapters": sum(len(b["chapters"]) for b in books),
                  "sequence_file_bytes": seq_path.stat().st_size}, indent=2))
