#!/usr/bin/env python3
"""VALIDATOR — Bible DNA lane (2026-11-14). Separate code, separately run.
Reads bible-dna-full.txt and reports storage-codec hygiene figures honestly:
alphabet purity, GC content, homopolymer runs. REPORT ONLY — the codec of
record is the plain house mapping; nothing here alters the sequence."""
import json, re
from collections import Counter
from pathlib import Path

LANE = Path.home() / "workspace/dna-bible-2026-11-14"
raw = (LANE / "bible-dna-full.txt").read_text(encoding="ascii")
seq = "".join(raw.split())
counts = Counter(seq)
alphabet = sorted(counts)
gc = (counts["G"] + counts["C"]) / len(seq) * 100 if seq else 0.0
runs = [(m.group(0)[0], len(m.group(0))) for m in re.finditer(r"(.)\1*", seq)]
run_hist = Counter(L for _, L in runs)
fig = {
    "bases_read": len(seq),
    "alphabet": alphabet,
    "alphabet_pure_acgt": alphabet == ["A", "C", "G", "T"],
    "base_counts": {b: counts[b] for b in "ACGT"},
    "gc_content_percent": round(gc, 4),
    "total_runs": len(runs),
    "longest_homopolymer_run": max(L for _, L in runs),
    "runs_ge_4": sum(1 for _, L in runs if L >= 4),
    "runs_ge_5": sum(1 for _, L in runs if L >= 5),
    "runs_ge_6": sum(1 for _, L in runs if L >= 6),
    "runs_ge_8": sum(1 for _, L in runs if L >= 8),
    "runs_ge_10": sum(1 for _, L in runs if L >= 10),
    "run_length_histogram": {str(k): run_hist[k] for k in sorted(run_hist)[:12]},
}
(LANE / "work").mkdir(exist_ok=True)
(LANE / "work/validator.json").write_text(json.dumps(fig, indent=2), encoding="utf-8")
report = f"""# VALIDATOR REPORT — codec hygiene (report only)

Sequence file: `bible-dna-full.txt` — {fig['bases_read']:,} bases read
(whitespace stripped).

- Alphabet: {', '.join(alphabet)} — pure A/C/G/T: **{fig['alphabet_pure_acgt']}**
- Base counts: A {counts['A']:,} · C {counts['C']:,} · G {counts['G']:,} · T {counts['T']:,}
- GC content: **{fig['gc_content_percent']}%**
- Homopolymer runs in total: {fig['total_runs']:,}
- Longest homopolymer run: **{fig['longest_homopolymer_run']}**
- Runs of length ≥ 4: {fig['runs_ge_4']:,} · ≥ 5: {fig['runs_ge_5']:,} · ≥ 6: {fig['runs_ge_6']:,} · ≥ 8: {fig['runs_ge_8']:,} · ≥ 10: {fig['runs_ge_10']:,}

These figures are disclosed facts about the plain house codec's output,
recorded for any future synthesis discussion. The codec of record is the
plain mapping (00=A, 01=C, 10=G, 11=T); **the sequence was not altered to
improve these figures.** A synthesis-grade encoding would add screening,
addressing, and error correction on top of this layer, as the manifest states.
"""
(LANE / "work/VALIDATOR-REPORT.md").write_text(report, encoding="utf-8")
print(json.dumps(fig, indent=2))
