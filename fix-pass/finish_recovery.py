#!/usr/bin/env python3
"""FINISHER — Lineation Recovery Pass, the four STOPPED chapters (Ruling 8 as amended).

Applies the three desk/editor rulings recorded in logs/dispositions-log.md
(2026-10-18, "Recovery stops 2 and 3: ruled YES by the desk..." and Stop 1 the
editor's own YES) to the four chapters the recovery pass stopped:

  1. ACTS 8, ACTS 15 — a verse carried only by the base (8:37; 15:34) is treated
     as OUTSIDE the staged text. On the base pages both verses exist only as
     footnote popups (the verse marker stands with no verse body; the parser's
     notemark stripping leaves an empty chunk list). The base-only verse key is
     removed from the parse before the verse-set assertion; the chapter's
     remaining verses restore normally. No word is added or removed — the
     rebuild works from staged tokens only, as everywhere in this pass.
  2. ISAIAH 44 — the one boundary in v. 19 falling inside the Decision 9
     conversion span is placed BY SENSE: after the staged token "thing?" (the
     clause-ending token corresponding to the base's "abomination?"), so the
     division reads "…a detestable thing?" | "Will I bow down to a tree trunk?".
     The placement is asserted against the recorded conversion strings and
     logged in full. This one boundary only, this one reason.
  3. HABAKKUK 3 — the music-director colophon, a chapter-final prose block on
     the base page equal word for word to the staged standalone paragraph, is
     matched AS that standalone: the trailing 'p' chunk is lifted out of
     v. 19's chunks and the base standalone list is set to it, so the standalone
     assertion passes and the staged paragraph itself stays untouched.

Everything else is the recovery pass's own machinery (recovery.py imported, its
primitives used unchanged): split points and division kinds from the base page
only; staged wording kept; whitespace-collapsed word stream asserted
character-identical before any write, on every surface; whole-file assertion
after each splice. Readers are written here; editions follow serially via
editions_apply_recovery.py, as the waves were organized.

Usage: finish_recovery.py [--apply]   (dry run without --apply)
"""
import difflib, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import recovery as R

norm = R.norm
COLOPHON = "For the music director, on my stringed instruments."
JOBS = [("ACTS", 8), ("ACTS", 15), ("ISAIAH", 44), ("HABAKKUK", 3)]


def adjust_parse(book, ch, verses, standalones):
    """Apply the ruled parse-level transforms. Returns (verses, standalones, note)."""
    if book == "ACTS" and ch in (8, 15):
        missing = 37 if ch == 8 else 34
        assert missing in verses, f"Acts {ch}: base parse lacks verse {missing} entirely"
        assert verses[missing] == [], (
            f"Acts {ch}: base-only verse {missing} carries chunks {verses[missing]} — "
            "expected none (footnote-only verse on the base page); stopping")
        verses = dict(verses)
        del verses[missing]
        return verses, standalones, (
            f"base-only verse {missing} (footnote-only on the base page; empty chunk "
            "list) treated as outside the staged text per the editor's ruling")
    if book == "HABAKKUK" and ch == 3:
        assert standalones == [], f"Habakkuk 3: base standalones unexpectedly {standalones}"
        last = max(verses)
        assert last == 19, f"Habakkuk 3: last base verse is {last}, expected 19"
        chunks = verses[19]
        assert chunks and chunks[-1][0] == "p" and chunks[-1][1] == COLOPHON, (
            f"Habakkuk 3: v.19 trailing chunk is {chunks[-1] if chunks else None}, "
            "not the colophon prose block; stopping")
        verses = dict(verses)
        verses[19] = chunks[:-1]
        return verses, [COLOPHON], (
            "chapter-final prose block (the music-director colophon) matched as the "
            "staged standalone paragraph, word for word, per the desk's ruling")
    return verses, standalones, ""


def map_one(opcodes, k):
    """R.map_boundaries' per-boundary walk, verbatim semantics."""
    for tag, i1, i2, j1, j2 in opcodes:
        if tag == "equal":
            if i1 <= k <= i2:
                return j1 + (k - i1)
        else:
            if k == i1:
                return j1
            if k == i2:
                return j2
    return None


def rebuild_isaiah_44_19(chunks, staged_body, evidence):
    """rebuild_verse for Isaiah 44:19 with the single sense-placed boundary."""
    base_tokens, bounds = [], []
    for cls, text in chunks:
        toks = text.split()
        base_tokens.extend(toks)
        bounds.append(len(base_tokens))
    staged_tokens = staged_body.split()
    sm = difflib.SequenceMatcher(None, base_tokens, staged_tokens, autojunk=False)
    assert sm.ratio() >= 0.55, "Isaiah 44:19: alignment ratio below pass threshold"
    opcodes = sm.get_opcodes()
    inner = bounds[:-1]
    mapped = [map_one(opcodes, k) for k in inner]
    ambiguous = [k for k, m in zip(inner, mapped) if m is None]
    assert ambiguous == [46], (
        f"Isaiah 44:19: ambiguous boundaries are {ambiguous}, expected exactly [46]; stopping")
    # The recorded conversion, asserted against the live alignment:
    assert base_tokens[45] == "abomination?", (
        f"Isaiah 44:19: base token before the boundary is {base_tokens[45]!r}, not 'abomination?'")
    covering = [op for op in opcodes if op[0] != "equal" and op[1] < 46 < op[2]]
    assert len(covering) == 1, f"Isaiah 44:19: covering opcodes {covering}"
    tag, i1, i2, j1, j2 = covering[0]
    assert base_tokens[i1:i2] == ["an", "abomination?", "Shall"], (
        f"Isaiah 44:19: base span is {base_tokens[i1:i2]}")
    assert staged_tokens[j1:j2] == ["a", "detestable", "thing?", "Will"], (
        f"Isaiah 44:19: staged span is {staged_tokens[j1:j2]}")
    qmarked = [j for j in range(j1, j2) if staged_tokens[j].endswith("?")]
    assert qmarked == [j1 + 2] and staged_tokens[j1 + 2] == "thing?", (
        f"Isaiah 44:19: '?'-final staged tokens in span at {qmarked}")
    forced = j1 + 3  # boundary immediately after "thing?"
    assert staged_tokens[forced] == "Will", (
        f"Isaiah 44:19: staged token after the placed boundary is {staged_tokens[forced]!r}")
    mapped = [forced if m is None else m for m in mapped]
    evidence.append(
        "Isaiah 44:19 sense placement: base boundary after token 46 ('…into an "
        "abomination?') falls inside replace span base[44:47]=['an','abomination?',"
        "'Shall'] -> staged[44:48]=['a','detestable','thing?','Will']; placed at "
        "staged boundary 47, immediately after 'thing?', so the division reads "
        "'…a detestable thing?' | 'Will I bow down to a tree trunk?'. All other "
        "boundaries in the verse (3, 11, 20, 29, 36) placed mechanically.")
    seg_bounds = [0] + mapped + [len(staged_tokens)]
    lines, counts = [], {"q": 0, "q2": 0, "m": 0, "qs": 0}
    first = True
    for i, (cls, _t) in enumerate(chunks):
        seg = " ".join(staged_tokens[seg_bounds[i]:seg_bounds[i + 1]])
        assert seg, f"Isaiah 44:19: division {i} maps to an empty staged segment"
        if cls in counts:
            counts[cls] += 1
        indent = "  " if cls == "q2" else ""
        lines.append(f"{indent}{'19 ' if first else ''}{seg}")
        first = False
    return "\n".join(lines), counts


def rebuild_finish(book, ch, v, chunks, staged_body, evidence):
    if (book, ch, v) == ("ISAIAH", 44, 19):
        return rebuild_isaiah_44_19(chunks, staged_body, evidence)
    return R.rebuild_verse(v, chunks, staged_body)


def process_finish(book, ch, apply):
    display, code, nch, in_hebrew = R.BOOKS[book]
    rec = {"book": book, "chapter": ch,
           "ruling": "Ruling 8 (as amended 2026-10-18); finisher under the three stop rulings (dispositions log, 2026-10-18)"}
    evidence = []
    verses, standalones, unknown = R.parse_base(R.fetch_page(code, ch))
    assert not unknown, f"unhandled div class(es): {sorted(unknown)}"
    verses, standalones, note = adjust_parse(book, ch, verses, standalones)
    if note:
        evidence.append(note)
    poetic_total = sum(1 for v in verses.values() for c, _ in v if c in R.POETIC)
    assert poetic_total > 0, "no poetic divisions after adjustment — not a finisher chapter"
    reader_path = os.path.join(R.STG, "books", f"{book}-reader.txt")
    rtext = open(reader_path, encoding="utf-8").read()
    rspans = R.split_paras(rtext)
    rparas = [p for _, _, p in rspans]
    ri, rj = R.chapter_span(rparas, display, ch, nch)
    _head, items = R.parse_staged_chapter(rparas[ri:rj])
    staged_verses = {it[1]: it[2] for it in items if it[0] == "verse"}
    staged_standalones = [it[1] for it in items if it[0] == "standalone"]
    staged_raw = {it[1]: it[3] for it in items if it[0] == "verse"}
    assert set(staged_verses) == set(verses), (
        f"verse set mismatch after ruled adjustment: staged {sorted(staged_verses)} "
        f"vs base {sorted(verses)}")
    if book == "ACTS":
        # Finisher finding: the staged chapter registers the base-only verse with a
        # bare-number paragraph ('37' / '34') standing at the verse's place between
        # the neighbouring verses. It is the draft's own marker of the omission;
        # it is carried through untouched (adds and removes no word).
        missing = 37 if ch == 8 else 34
        assert standalones == [], f"Acts {ch}: base standalones unexpectedly {standalones}"
        assert staged_standalones == [str(missing)], (
            f"Acts {ch}: staged standalones are {staged_standalones}, expected exactly "
            f"the bare-number paragraph ['{missing}']")
        idx = next(i for i, it in enumerate(items) if it[0] == "standalone")
        assert items[idx - 1][1] == missing - 1 and items[idx + 1][1] == missing + 1, (
            f"Acts {ch}: bare-number paragraph is not between vv. {missing - 1} and {missing + 1}")
        evidence.append(
            f"staged chapter registers the base-only verse {missing} with a "
            f"bare-number paragraph ('{missing}') between vv. {missing - 1} and "
            f"{missing + 1}; carried through untouched")
    else:
        assert norm(" ".join(staged_standalones)) == norm(" ".join(standalones)), (
            f"standalone mismatch after ruled adjustment: staged {staged_standalones} "
            f"vs base {standalones}")
    new_items, totals = [], {"q": 0, "q2": 0, "m": 0, "qs": 0}
    for it in items:
        if it[0] == "standalone":
            new_items.append(it[1])
            continue
        v, body = it[1], it[2]
        chunks = verses[v]
        if not any(c in R.POETIC for c, _ in chunks):
            new_items.append(staged_raw[v])
            continue
        new_para, counts = rebuild_finish(book, ch, v, chunks, body, evidence)
        assert new_para is not None, f"verse {v}: rebuild failed: {counts}"
        for k2 in totals:
            totals[k2] += counts[k2]
        new_items.append(new_para)
    new_span_paras = [rparas[ri]] + new_items
    assert norm("\n\n".join(new_span_paras)) == norm("\n\n".join(rparas[ri:rj])), \
        "word-stream identity assertion failed on books reader"
    rec.update(disposition="RESTORED", divisions=totals, surfaces=[], evidence=evidence)
    if not apply:
        rec["disposition"] = "RESTORED (dry run)"
        return rec
    for surf in (f"books/{book}-reader.txt", f"individual-books/{book}-reader.txt"):
        path = os.path.join(R.STG, surf)
        text = open(path, encoding="utf-8").read()
        spans = R.split_paras(text)
        paras = [p for _, _, p in spans]
        si, sj = R.chapter_span(paras, display, ch, nch)
        assert norm("\n\n".join(paras[si:sj])) == norm("\n\n".join(rparas[ri:rj])), \
            f"surface {surf}: chapter word stream differs from books reader; not written"
        start, end = spans[si][0], spans[sj - 1][1]
        new_text = text[:start] + "\n\n".join(new_span_paras) + text[end:]
        assert norm(new_text) == norm(text), f"{surf}: whole-file word-stream assertion failed"
        open(path, "w", encoding="utf-8").write(new_text)
        rec["surfaces"].append(surf)
    # update the book's results file in the pass's own format
    out_path = os.path.join(R.RESULTS, f"{book}.json")
    prior = json.load(open(out_path)) if os.path.exists(out_path) else []
    prior = [r for r in prior if r["chapter"] != ch] + [rec]
    json.dump(prior, open(out_path, "w"), indent=1)
    return rec


def main():
    apply = "--apply" in sys.argv
    for book, ch in JOBS:
        try:
            rec = process_finish(book, ch, apply)
            print(f"{book} {ch}: {rec['disposition']} {rec.get('divisions', '')}")
            for ev in rec.get("evidence", []):
                print(f"    evidence: {ev}")
        except AssertionError as e:
            print(f"{book} {ch}: STOPPED (finisher assertion) — {e}")


if __name__ == "__main__":
    main()
