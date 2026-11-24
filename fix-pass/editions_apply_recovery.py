#!/usr/bin/env python3
"""Coordinator serial application of recovery-pass lineation to the EDITION surfaces.
For every RESTORED chapter recorded in recovery-results/*.json and not yet transplanted,
splice the staged books reader's (lineated) chapter span into each edition carrying the
book, asserting first that the edition's current chapter span is word-stream identical
(whitespace-collapsed) to the reader's span. State kept in recovery-results/editions-state.json
so re-runs are idempotent. Usage: editions_apply_recovery.py [BOOK ...] (default: all)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import recovery as R

state_path = os.path.join(R.RESULTS, "editions-state.json")
state = json.load(open(state_path)) if os.path.exists(state_path) else {}
only = set(sys.argv[1:])
log = []
for fname in sorted(os.listdir(R.RESULTS)):
    if not fname.endswith(".json") or fname == "editions-state.json":
        continue
    stem = fname[:-5]
    book = next((b for b in R.BOOKS if stem == b or stem.startswith(b + "-")), None)
    if book is None or (only and book not in only):
        continue
    display, code, nch, in_hebrew = R.BOOKS[book]
    editions = list(R.EDITIONS) + ([R.HEBREW_EDITION] if in_hebrew else [])
    rtext = open(os.path.join(R.STG, "books", f"{book}-reader.txt"), encoding="utf-8").read()
    rspans = R.split_paras(rtext)
    rparas = [p for _, _, p in rspans]
    for rec in json.load(open(os.path.join(R.RESULTS, fname))):
        if rec["disposition"] != "RESTORED":
            continue
        ch = rec["chapter"]
        key = f"{book} {ch}"
        ri, rj = R.chapter_span(rparas, display, ch, nch)
        rspan = rparas[ri:rj]
        for rel in editions:
            skey = f"{key} :: {rel}"
            if state.get(skey):
                continue
            path = os.path.join(R.STG, rel)
            text = open(path, encoding="utf-8").read()
            spans = R.split_paras(text)
            paras = [p for _, _, p in spans]
            si, sj = R.chapter_span(paras, display, ch, nch)
            assert R.norm("\n\n".join(paras[si:sj])) == R.norm("\n\n".join(rspan)), \
                f"{rel} {key}: word-stream mismatch before transplant"
            start, end = spans[si][0], spans[sj - 1][1]
            new_text = text[:start] + "\n\n".join(rspan) + text[end:]
            assert R.norm(new_text) == R.norm(text), f"{rel} {key}: whole-file assertion failed"
            open(path, "w", encoding="utf-8").write(new_text)
            state[skey] = True
            d = rec["divisions"]
            log.append(f"- Recovery {display} {ch} — {rel}: transplanted "
                       f"({d['q']} q, {d['q2']} q2, {d['m']} m, {d['qs']} qs), word-stream verified")
    json.dump(state, open(state_path, "w"), indent=1)
out = os.path.join(R.BASE, "logs", "recovery-editions-application.md")
prior = open(out).read() if os.path.exists(out) else "# Recovery pass — edition application (coordinator, serial)\n"
with open(out, "a", encoding="utf-8") as f:
    if not prior.endswith("\n"):
        f.write("\n")
    f.write("\n".join(log) + ("\n" if log else ""))
print(f"transplanted {len(log)} chapter-edition spans")
