#!/usr/bin/env python3
"""Lane B: restore the 33 Song of Songs speaker headings (Ruling 18).
Positions from the pinned base snapshots' speaker-headings records.
Representation: each heading stands as its own paragraph (the base's own
word alone: Beloved / Friends / Lover / Brothers). Within-verse headings
split the verse paragraph at the recorded anchor; the verse number stays
with the first part. No verse wording is changed."""
import os, re, json

FIX = os.path.expanduser("~/workspace/ceb-push/fix-pass")
STAGE = os.path.join(FIX, "staging")

# (chapter, [(kind, verse, anchor, word), ...]) kinds: before, after, within
HEADINGS = {
 1: [("after",1,None,"Beloved"),
     ("within",4,"his rooms.","Friends"),
     ("within",4,"more than wine!","Beloved"),
     ("before",8,None,"Lover"),
     ("before",11,None,"Friends"),
     ("before",12,None,"Beloved"),
     ("before",15,None,"Lover"),
     ("before",16,None,"Beloved"),
     ("before",17,None,"Lover")],
 2: [("before",1,None,"Beloved"),("before",2,None,"Lover"),
     ("before",3,None,"Beloved"),("before",14,None,"Lover"),
     ("before",16,None,"Beloved")],
 3: [],
 4: [("before",1,None,"Lover"),("before",16,None,"Beloved")],
 5: [("before",1,None,"Lover"),
     ("within",1,"with my milk.","Friends"),
     ("within-end",1,None,"Beloved"),
     ("before",9,None,"Friends"),
     ("before",10,None,"Beloved")],
 6: [("before",1,None,"Friends"),("before",2,None,"Beloved"),
     ("before",4,None,"Lover"),
     ("before",13,None,"Friends"),
     ("within",13,"that we may gaze at you.","Lover")],
 7: [("before",10,None,"Beloved")],
 8: [("before",5,None,"Friends"),
     ("within",5,"leaning on her beloved?","Beloved"),
     ("before",8,None,"Brothers"),
     ("before",10,None,"Beloved"),
     ("before",13,None,"Lover"),
     ("before",14,None,"Beloved")],
}
EXPECTED = {1:9, 2:5, 3:0, 4:2, 5:5, 6:5, 7:1, 8:6}

SURFACES = [
    "books/SONGOFSONGS-reader.txt",
    "individual-books/SONGOFSONGS-reader.txt",
    "editions/catholic/clear-translation-bible-catholic-edition.txt",
    "editions/protestant/clear-translation-bible-protestant-edition.txt",
    "editions/hebrew/the-torah-the-prophets-and-the-writings.txt",
]

def split_paras(raw):
    return re.split(r"\n\s*\n", raw)

def chapter_span(paras, ch):
    """Return (start_idx, end_idx) of the verse paragraphs of chapter ch."""
    head = None
    for i, p in enumerate(paras):
        if p.strip() == f"Song of Songs {ch}":
            head = i
            break
    assert head is not None, f"chapter heading {ch} not found"
    start = head + 1
    end = len(paras)
    # Song verses are all numbered single paragraphs (verified in the
    # completion report); the chapter span ends at the first paragraph
    # that does not begin with a verse number.
    for j in range(start, len(paras)):
        if not re.match(r"^\d+\s", paras[j].strip()):
            end = j
            break
    return start, end

def verse_num(p):
    m = re.match(r"^(\d+)\s+", p.strip())
    return int(m.group(1)) if m else None

def transform_chapter(paras, ch):
    """Return (new_paras, n_headings). paras are the chapter's verse paragraphs."""
    spec = HEADINGS[ch]
    befores = {}
    afters = {}
    withins = {}
    for kind, v, anchor, word in spec:
        if kind == "before":
            befores.setdefault(v, []).append(word)
        elif kind in ("after", "within-end"):
            afters.setdefault(v, []).append(word)
        elif kind == "within":
            withins.setdefault(v, []).append((anchor, word))
    out = []
    n = 0
    for p in paras:
        v = verse_num(p)
        assert v is not None, f"ch{ch}: unnumbered paragraph in span: {p[:50]!r}"
        for w in befores.get(v, []):
            out.append(w); n += 1
        body = p
        for anchor, w in withins.get(v, []):
            idx = body.find(anchor)
            assert idx >= 0, f"ch{ch} v{v}: anchor {anchor!r} not found"
            cut = idx + len(anchor)
            first, rest = body[:cut], body[cut:].strip()
            out.append(first)
            out.append(w); n += 1
            body = rest
        if body:
            out.append(body)
        for w in afters.get(v, []):
            out.append(w); n += 1
    return out, n

log_entries = []
for surf in SURFACES:
    path = os.path.join(STAGE, surf)
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    already = sum(1 for p in split_paras(raw) if p.strip() in ("Beloved", "Friends", "Lover", "Brothers"))
    if already == 33:
        print(f"{surf}: already carries 33 headings — skipped (idempotent)")
        continue
    assert already == 0, f"{surf}: unexpected partial heading state ({already})"
    paras = split_paras(raw)
    total = 0
    # work from last chapter to first so indices stay valid
    for ch in sorted(HEADINGS, reverse=True):
        if not HEADINGS[ch]:
            continue
        s, e = chapter_span(paras, ch)
        span = paras[s:e]
        before_norm = re.sub(r"\s+", " ", "\n\n".join(span)).strip()
        new_span, n = transform_chapter(span, ch)
        total += n
        # verification: removing inserted heading paragraphs restores the text
        stripped = [p for p in new_span if p.strip() not in ("Beloved", "Friends", "Lover", "Brothers")]
        # rejoin split verses: splitting only added paragraph breaks; compare word streams
        assert re.sub(r"\s+", " ", "\n\n".join(stripped)).strip() == before_norm, f"{surf} ch{ch}: word-stream mismatch"
        paras[s:e] = new_span
        log_entries.append((surf, ch, n))
    assert total == 33, f"{surf}: inserted {total} headings, expected 33"
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(paras))

with open(os.path.join(FIX, "logs", "lane-b-log.md"), "w", encoding="utf-8") as f:
    f.write("# LANE B CHANGE LOG — Song of Songs speaker headings (Ruling 18)\n\n")
    f.write("Source of record: the pinned base snapshots' speaker-headings lines (hidden_files/songofsongs-0N-web-base-snapshot-2026-10-16.txt), cross-checked against SONGOFSONGS-COMPLETION-REPORT.md flag 2 counts (9, 5, 0, 2, 5, 5, 1, 6 = 33). Representation: each heading stands as its own paragraph in the base's own word (Beloved / Friends / Lover / Brothers); within-verse headings split the verse paragraph at the recorded anchor, verse number staying with the first part. Chapter 3: none recorded, none inserted. Ground for every entry: Ruling 18 (headings restored in the base's own heading words at the recorded positions; no verse wording changes).\n\n")
    for surf, ch, n in sorted(log_entries):
        f.write(f"- {surf} — chapter {ch}: {n} headings inserted.\n")
    f.write("\nPositions applied, per chapter (from the snapshot records):\n\n")
    f.write("- Ch 1: Beloved after v.1; Friends within v.4 after 'his rooms.'; Beloved within v.4 after 'more than wine!'; Lover before v.8; Friends before v.11; Beloved before v.12; Lover before v.15; Beloved before v.16; Lover before v.17.\n")
    f.write("- Ch 2: Beloved before v.1; Lover before v.2; Beloved before v.3; Lover before v.14; Beloved before v.16.\n")
    f.write("- Ch 4: Lover before v.1; Beloved before v.16.\n")
    f.write("- Ch 5: Lover before v.1; Friends within v.1 after 'with my milk.'; Beloved at v.1's end (recorded 'within v.1, after \"beloved.\" (i.e., before v.2)'); Friends before v.9; Beloved before v.10.\n")
    f.write("- Ch 6: Friends before v.1; Beloved before v.2; Lover before v.4; Friends at v.13's head (recorded 'within v.13, after v.12's close'); Lover within v.13 after 'that we may gaze at you.'.\n")
    f.write("- Ch 7: Beloved at v.10's head (recorded 'within v.10, after v.9').\n")
    f.write("- Ch 8: Friends before v.5; Beloved within v.5 after 'leaning on her beloved?'; Brothers before v.8; Beloved before v.10; Lover before v.13; Beloved before v.14.\n")
print("Lane B done:", len(log_entries), "chapter-surface applications")
