#!/usr/bin/env python3
"""Independent verification of the finisher's four chapters, by re-extraction.
Mirrors verify_recovery.py exactly, except that the re-derivation runs under the
same three stop rulings the application ran under (finish_recovery.adjust_parse
and finish_recovery.rebuild_finish): re-parse the base page, re-derive the
expected chapter paragraphs from the CURRENT staged wording, compare exactly
against the staged books reader, and confirm every surface carries the
identical chapter span. Usage: verify_finish.py (verifies all four chapters)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import recovery as R
import finish_recovery as F

def derive(book, ch):
    display, code, nch, in_hebrew = R.BOOKS[book]
    verses, standalones, unknown = R.parse_base(R.fetch_page(code, ch))
    assert not unknown, f"unknown classes {unknown}"
    verses, standalones, _note = F.adjust_parse(book, ch, verses, standalones)
    path = os.path.join(R.STG, "books", f"{book}-reader.txt")
    text = open(path, encoding="utf-8").read()
    spans = R.split_paras(text)
    paras = [p for _, _, p in spans]
    si, sj = R.chapter_span(paras, display, ch, nch)
    _h, items = R.parse_staged_chapter(paras[si:sj])
    staged_verses = {it[1] for it in items if it[0] == "verse"}
    assert staged_verses == set(verses), f"{book} {ch}: verse sets differ under the ruling"
    out = [paras[si]]
    evidence = []
    poetic_any = False
    for it in items:
        if it[0] == "standalone":
            out.append(it[1]); continue
        v, body, raw = it[1], it[2], it[3]
        chunks = verses[v]
        if not any(c in R.POETIC for c, _ in chunks):
            out.append(raw); continue
        poetic_any = True
        np_, counts = F.rebuild_finish(book, ch, v, chunks, body, evidence)
        assert np_ is not None, f"{book} {ch} v{v}: re-derivation failed: {counts}"
        out.append(np_)
    return out, paras[si:sj], poetic_any

def main():
    bad = 0
    for book, ch in F.JOBS:
        display, code, nch, in_hebrew = R.BOOKS[book]
        expected, actual, poetic_any = derive(book, ch)
        surfaces = [f"books/{book}-reader.txt", f"individual-books/{book}-reader.txt"]
        surfaces += R.EDITIONS
        if in_hebrew:
            surfaces.append(R.HEBREW_EDITION)
        ok = expected == actual
        surf_ok = True
        for surf in surfaces[1:]:
            text = open(os.path.join(R.STG, surf), encoding="utf-8").read()
            spans = R.split_paras(text)
            paras = [p for _, _, p in spans]
            si, sj = R.chapter_span(paras, display, ch, nch)
            if paras[si:sj] != actual:
                surf_ok = False
        status = "VERIFIED" if (ok and surf_ok) else "MISMATCH"
        if status != "VERIFIED":
            bad += 1
        print(f"{book} {ch}: {status} (poetic={poetic_any}, surfaces_identical={surf_ok}, "
              f"rederive_match={ok}, surfaces={len(surfaces)})")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
