#!/usr/bin/env python3
"""Independent verification of recovery-pass chapters, by re-extraction and read-back.
For each chapter: re-parse the base page, re-derive the expected chapter paragraphs from
the CURRENT staged wording (alignment re-run from scratch), and compare exactly against
the staged books reader; then confirm every surface carries the identical chapter span.
Usage: verify_recovery.py BOOK CH[,CH...] [...]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import recovery as R

def derive(book, ch):
    display, code, nch, in_hebrew = R.BOOKS[book]
    verses, standalones, unknown = R.parse_base(R.fetch_page(code, ch))
    assert not unknown, f"unknown classes {unknown}"
    path = os.path.join(R.STG, "books", f"{book}-reader.txt")
    text = open(path, encoding="utf-8").read()
    spans = R.split_paras(text)
    paras = [p for _, _, p in spans]
    si, sj = R.chapter_span(paras, display, ch, nch)
    _h, items = R.parse_staged_chapter(paras[si:sj])
    out = [paras[si]]
    poetic_any = False
    for it in items:
        if it[0] == "standalone":
            out.append(it[1]); continue
        v, body, raw = it[1], it[2], it[3]
        chunks = verses[v]
        if not any(c in R.POETIC for c, _ in chunks):
            out.append(raw); continue
        poetic_any = True
        np_, counts = R.rebuild_verse(v, chunks, body)
        assert np_ is not None, f"{book} {ch} v{v}: re-derivation failed: {counts}"
        out.append(np_)
    return out, paras[si:sj], poetic_any

def main():
    args = sys.argv[1:]
    readers_only = "--readers" in args
    args = [a for a in args if not a.startswith("--")]
    jobs = []
    for a in args:
        book, chs = a.split(":")
        jobs += [(book, int(c)) for c in chs.split(",")]
    bad = 0
    for book, ch in jobs:
        display, code, nch, in_hebrew = R.BOOKS[book]
        expected, actual, poetic_any = derive(book, ch)
        surfaces = [f"books/{book}-reader.txt", f"individual-books/{book}-reader.txt"]
        if not readers_only:
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
        print(f"{book} {ch}: {status} (poetic={poetic_any}, surfaces_identical={surf_ok}, rederive_match={ok})")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
