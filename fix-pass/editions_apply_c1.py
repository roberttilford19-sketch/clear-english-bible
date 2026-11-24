#!/usr/bin/env python3
"""Coordinator serial application of Lane C-1 lineation to the edition surfaces.
For each rebuilt chapter (logs/lane-c1-changes.json), transplant the staged reader's
chapter span into the edition, asserting whitespace-collapsed word-stream identity
between the edition's current chapter and the reader's rebuilt chapter first.
"""
import json, os, re

BASE = os.path.expanduser("~/workspace/ceb-push/fix-pass")
STG = os.path.join(BASE, "staging")
EDITIONS = ["editions/catholic/clear-translation-bible-catholic-edition.txt",
            "editions/protestant/clear-translation-bible-protestant-edition.txt"]
BOOKNAME = {"HEBREWS": "Hebrews", "1-PETER": "1 Peter", "1-TIMOTHY": "1 Timothy",
            "2-TIMOTHY": "2 Timothy", "GALATIANS": "Galatians",
            "1-CORINTHIANS": "1 Corinthians", "2-CORINTHIANS": "2 Corinthians"}
changes = json.load(open(os.path.join(BASE, "logs/lane-c1-changes.json"), encoding="utf-8"))

def paras(text):
    return re.split(r"\n\s*\n", text)

def chapter_span(ps, bookname, ch, nchapters):
    head = f"{bookname} {ch}"
    assert ps.count(head) == 1, f"heading {head!r} count {ps.count(head)}"
    i = ps.index(head)
    j = i + 1
    while j < len(ps):
        p = ps[j].strip()
        if p.startswith("Clear English Bible — "):
            break
        if ch < nchapters and p == f"{bookname} {ch+1}":
            break
        j += 1
    return i, j

NCH = {"Hebrews": 13, "1 Peter": 5, "1 Timothy": 6, "2 Timothy": 4,
       "Galatians": 6, "1 Corinthians": 16, "2 Corinthians": 13}
log = []
for rel in EDITIONS:
    epath = os.path.join(STG, rel)
    etext = open(epath, encoding="utf-8").read()
    eps = paras(etext)
    for e in changes:
        book = BOOKNAME[e["book"]]; ch = e["chapter"]
        rpath = os.path.join(STG, "books", f"{e['book']}-reader.txt")
        rps = paras(open(rpath, encoding="utf-8").read())
        ri, rj = chapter_span(rps, book, ch, NCH[book])
        ei, ej = chapter_span(eps, book, ch, NCH[book])
        rspan, espan = rps[ri:rj], eps[ei:ej]
        norm = lambda ps: re.sub(r"\s+", " ", " ".join(ps)).strip()
        assert norm(rspan) == norm(espan), f"{rel} {book} {ch}: word-stream mismatch"
        eps[ei:ej] = rspan
        log.append(f"- C-1 {book} {ch} — {rel}: transplanted ({e['q']} q, {e['q2']} q2, {e['m']} m), word-stream verified")
    open(epath, "w", encoding="utf-8").write("\n\n".join(eps))

out = os.path.join(BASE, "logs/lane-c1-editions-application.md")
open(out, "w", encoding="utf-8").write("# Lane C-1 edition application (coordinator, serial)\n\n" + "\n".join(log) + "\n")
print(f"transplanted {len(log)} chapter-edition spans")
