#!/usr/bin/env python3
"""LINEATION RECOVERY PASS — Clear Translation Bible fix pass (Ruling 8 as amended 2026-10-18).

Reads a chapter's line divisions from the BASE'S OWN PAGES (ebible.org eng-web Classic,
the declared public-domain WEB Classic base) and rebuilds the chapter in the STAGED
readers + editions, in Lane C's representation:
  divisions as lines within the verse paragraph; q flush left; q2 indented two spaces;
  m and qs (Selah) divisions on their own unindented line; prose lead on the verse's first
  line; verse number at the head of the verse's first line (inside the indent when a verse
  begins in a q2 division); prose tail after a poetry block on its own unindented line.

Discipline (no deviations from Lane C):
  - Only split points and division kinds come from the base page. The staged text's own
    wording is kept; split points are mapped base-token -> staged-token by alignment.
    A split point falling inside a conversion span is ambiguous -> chapter STOPPED.
  - Before any write, the rebuilt chapter's whitespace-collapsed word stream must be
    character-identical to the staged chapter before rebuilding, on every surface.
  - A chapter whose base page carries no q/q2/qs division anywhere is PAGE-PROSE:
    nothing to restore; left exactly as staged.
  - Any anomaly (unknown div class, verse-set mismatch, alignment failure, surface
    mismatch) stops the chapter; nothing is written for it anywhere.

Usage: recovery.py BOOK CHAPTER[,CHAPTER...] [--apply]
Without --apply it is a dry run (parse + plan + report only).
Results are appended to recovery-results/<BOOK>.json (one record per chapter per run).
"""
import difflib, html as htmllib, json, os, re, subprocess, sys

BASE = os.path.expanduser("~/workspace/ceb-push/fix-pass")
STG = os.path.join(BASE, "staging")
CACHE = os.path.join(BASE, "recovery-cache")
RESULTS = os.path.join(BASE, "recovery-results")
os.makedirs(CACHE, exist_ok=True)
os.makedirs(RESULTS, exist_ok=True)

# stem -> (heading display name, ebible code, n chapters, in hebrew edition)
BOOKS = {
    "DEUTERONOMY": ("Deuteronomy", "DEU", 34, True),
    "PSALMS": ("Psalm", "PSA", 150, True),
    "JOB": ("Job", "JOB", 42, True),
    "ISAIAH": ("Isaiah", "ISA", 66, True),
    "JEREMIAH": ("Jeremiah", "JER", 52, True),
    "EZEKIEL": ("Ezekiel", "EZK", 48, True),
    "HOSEA": ("Hosea", "HOS", 14, True),
    "MICAH": ("Micah", "MIC", 7, True),
    "ZECHARIAH": ("Zechariah", "ZEC", 14, True),
    "AMOS": ("Amos", "AMO", 9, True),
    "JOEL": ("Joel", "JOL", 3, True),
    "JONAH": ("Jonah", "JON", 4, True),
    "HABAKKUK": ("Habakkuk", "HAB", 3, True),
    "ZEPHANIAH": ("Zephaniah", "ZEP", 3, True),
    "ECCLESIASTES": ("Ecclesiastes", "ECC", 12, True),
    "LAMENTATIONS": ("Lamentations", "LAM", 5, True),
    "ROMANS": ("Romans", "ROM", 16, False),
    "ACTS": ("Acts", "ACT", 28, False),
    "1-CORINTHIANS": ("1 Corinthians", "1CO", 16, False),
    "JOHN": ("John", "JHN", 21, False),
}
EDITIONS = ["editions/catholic/clear-translation-bible-catholic-edition.txt",
            "editions/protestant/clear-translation-bible-protestant-edition.txt"]
HEBREW_EDITION = "editions/hebrew/the-torah-the-prophets-and-the-writings.txt"
KNOWN_CLASSES = {"q", "q2", "qs", "p", "m", "d", "b", "pi", "mi", "nb"}
# Coordinator class ruling (2026-10-18, logged in logs/recovery-coordinator-addendum-1.md):
# the base's prose-paragraph furniture is not lineation. 'pi' (indented prose) and 'nb'
# (no-break prose) are prose chunks, handled exactly as 'p'; 'mi' (indented margin) is the
# indented sibling of 'm' and is normalized to 'm' at parse time (own unindented line,
# counted with m). Only q/q2/qs are poetic divisions.
POETIC = {"q", "q2", "qs"}
norm = lambda s: " ".join(s.split())

# ---------------- base page fetch + parse ----------------

def fetch_page(code, ch):
    pad = 3 if code == "PSA" else 2
    name = f"{code}{str(ch).zfill(pad)}.htm"
    path = os.path.join(CACHE, name)
    if not os.path.exists(path):
        url = f"https://ebible.org/eng-web/{name}"
        tmp = path + ".tmp"
        r = subprocess.run(["curl", "-sfL", "--max-time", "90", url, "-o", tmp],
                           capture_output=True, text=True)
        if r.returncode != 0 or not os.path.exists(tmp) or os.path.getsize(tmp) < 500:
            raise RuntimeError(f"fetch failed for {url}")
        body = open(tmp, encoding="utf-8").read()
        if "chapterlabel" not in body:
            os.unlink(tmp)
            raise RuntimeError(f"fetched page for {url} carries no chapterlabel (not a chapter page)")
        os.rename(tmp, path)
    return open(path, encoding="utf-8").read()

def clean_text(fragment):
    # drop footnote anchors whole (dagger + popup text are not verse text)
    fragment = re.sub(r"<a\b[^>]*class=\"notemark\"[^>]*>.*?</a>", "", fragment, flags=re.S)
    fragment = re.sub(r"<a\b[^>]*class='notemark'[^>]*>.*?</a>", "", fragment, flags=re.S)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    return norm(htmllib.unescape(fragment))

def parse_base(html):
    """Return (verses, standalones, unknown_classes):
    verses: {v: [(cls, text), ...]} ordered chunks; standalones: [text of 'd' blocks]."""
    start = html.find("class='chapterlabel'")
    if start < 0:
        start = html.find('class="chapterlabel"')
    if start < 0:
        raise RuntimeError("chapterlabel not found on base page")
    ends = [i for i in (html.find("<ul class='tnav'>", start),
                        html.find('<div class="footnote"', start)) if i > start]
    region = html[start:min(ends) if ends else len(html)]
    verses, standalones, unknown = {}, [], set()
    cur = None  # current verse number
    div_re = re.compile(r"<div class='([a-z0-9]+)'>(.*?)</div>", re.S)
    vspan_re = re.compile(r"<span class=\"verse\" id=\"V(\d+)\">.*?</span>", re.S)
    for m in div_re.finditer(region):
        cls, inner = m.group(1), m.group(2)
        if cls == "chapterlabel":
            continue
        if cls not in KNOWN_CLASSES:
            unknown.add(cls)
            continue
        if cls == "b":
            continue
        # segment inner by verse markers
        parts, last = [], 0
        for vm in vspan_re.finditer(inner):
            parts.append((None, inner[last:vm.start()]))
            parts.append((int(vm.group(1)), None))
            last = vm.end()
        parts.append((None, inner[last:]))
        for vnum, frag in parts:
            if vnum is not None:
                cur = vnum
                verses.setdefault(cur, [])
                continue
            text = clean_text(frag or "")
            if not text:
                continue
            if cls == "d":
                standalones.append(text)
            elif cur is None:
                standalones.append(text)  # pre-verse material, non-'d': flag via marker
            else:
                verses[cur].append(("m" if cls == "mi" else cls, text))
    return verses, standalones, unknown

# ---------------- staged surface handling ----------------

def split_paras(text):
    """Return list of (start, end, para_text) with offsets, splitting on blank lines."""
    spans, pos = [], 0
    for m in re.finditer(r"\n\s*\n", text):
        spans.append((pos, m.start(), text[pos:m.start()]))
        pos = m.end()
    spans.append((pos, len(text), text[pos:]))
    return spans

def chapter_span(paras, display, ch, nch):
    head = f"{display} {ch}"
    idx = [i for i, p in enumerate(paras) if p.strip() == head]
    assert len(idx) == 1, f"heading {head!r} found {len(idx)} times"
    i = idx[0]
    j = i + 1
    while j < len(paras):
        p = paras[j].strip()
        if p.startswith("Clear English Bible — "):
            break
        if ch < nch and p == f"{display} {ch + 1}":
            break
        j += 1
    return i, j

def parse_staged_chapter(paras):
    """paras: chapter span paragraphs (heading first).
    Return (heading, items): items = [('standalone', raw) | ('verse', v, body, raw)]."""
    items = []
    for p in paras[1:]:
        t = p.strip()
        m = re.match(r"^(\d+)\s+(.*)$", t, re.S)
        if m:
            items.append(("verse", int(m.group(1)), norm(m.group(2)), t))
        else:
            items.append(("standalone", t))
    return paras[0], items

# ---------------- alignment + rebuild ----------------

def map_boundaries(base_tokens, staged_tokens, bounds):
    """bounds: sorted base-token indices (chunk ends, excluding final total).
    Return list of staged-token indices, or None if any boundary is ambiguous."""
    sm = difflib.SequenceMatcher(None, base_tokens, staged_tokens, autojunk=False)
    if sm.ratio() < 0.55:
        return None
    opcodes = sm.get_opcodes()
    out = []
    for k in bounds:
        mapped = None
        for tag, i1, i2, j1, j2 in opcodes:
            if tag == "equal":
                if i1 <= k <= i2:
                    mapped = j1 + (k - i1)
                    break
            else:
                if k == i1:
                    mapped = j1
                    break
                if k == i2:
                    mapped = j2
                    break
        if mapped is None:
            return None
        out.append(mapped)
    return out

def rebuild_verse(v, chunks, staged_body):
    """chunks: [(cls, base_text)]; staged_body: the staged verse text (no number).
    Return (new_para, counts) or (None, reason)."""
    base_tokens, bounds = [], []
    for cls, text in chunks:
        toks = text.split()
        base_tokens.extend(toks)
        bounds.append(len(base_tokens))
    staged_tokens = staged_body.split()
    if not base_tokens:
        return None, f"verse {v}: empty base segmentation"
    mapped = map_boundaries(base_tokens, staged_tokens, bounds[:-1])
    if mapped is None:
        return None, f"verse {v}: split point falls inside a conversion span (ambiguous alignment)"
    seg_bounds = [0] + mapped + [len(staged_tokens)]
    lines, counts = [], {"q": 0, "q2": 0, "m": 0, "qs": 0}
    first = True
    for i, (cls, _t) in enumerate(chunks):
        seg = " ".join(staged_tokens[seg_bounds[i]:seg_bounds[i + 1]])
        if not seg:
            return None, f"verse {v}: a division maps to an empty staged segment (division would be lost)"
        if cls in counts:
            counts[cls] += 1
        indent = "  " if cls == "q2" else ""
        if first:
            lines.append(f"{indent}{v} {seg}")
            first = False
        else:
            lines.append(f"{indent}{seg}")
    return "\n".join(lines), counts

READERS_ONLY = False

def process_chapter(book, ch, apply):
    display, code, nch, in_hebrew = BOOKS[book]
    rec = {"book": book, "chapter": ch, "ruling": "Ruling 8 (as amended 2026-10-18)"}
    surfaces = [f"books/{book}-reader.txt", f"individual-books/{book}-reader.txt"]
    if not READERS_ONLY:
        surfaces += EDITIONS
        if in_hebrew:
            surfaces.append(HEBREW_EDITION)
    # --- base parse
    try:
        verses, standalones, unknown = parse_base(fetch_page(code, ch))
    except Exception as e:
        rec.update(disposition="STOPPED", reason=f"base page: {e}")
        return rec
    if unknown:
        rec.update(disposition="STOPPED", reason=f"unhandled div class(es) on base page: {sorted(unknown)}")
        return rec
    poetic_total = sum(1 for v in verses.values() for c, _ in v if c in POETIC)
    if poetic_total == 0:
        rec.update(disposition="PAGE-PROSE",
                   reason="base page carries no q/q2/qs division in this chapter; nothing to restore; left as staged",
                   divisions={"q": 0, "q2": 0, "m": 0, "qs": 0})
        return rec
    # --- per-surface rebuild from books reader, transplant-verified elsewhere
    reader_path = os.path.join(STG, "books", f"{book}-reader.txt")
    rtext = open(reader_path, encoding="utf-8").read()
    rspans = split_paras(rtext)
    rparas = [p for _, _, p in rspans]
    ri, rj = chapter_span(rparas, display, ch, nch)
    _head, items = parse_staged_chapter(rparas[ri:rj])
    staged_verses = {it[1]: it[2] for it in items if it[0] == "verse"}
    staged_standalones = [it[1] for it in items if it[0] == "standalone"]
    staged_raw = {it[1]: it[3] for it in items if it[0] == "verse"}
    if set(staged_verses) != set(verses):
        rec.update(disposition="STOPPED",
                   reason=f"verse set mismatch: staged {sorted(staged_verses)} vs base {sorted(verses)}")
        return rec
    if norm(" ".join(staged_standalones)) != norm(" ".join(standalones)):
        rec.update(disposition="STOPPED",
                   reason=f"standalone ('d') block mismatch: staged {staged_standalones} vs base {standalones}")
        return rec
    new_items, totals = [], {"q": 0, "q2": 0, "m": 0, "qs": 0}
    for it in items:
        if it[0] == "standalone":
            new_items.append(it[1])
            continue
        _k, v, body = it[0], it[1], it[2]
        chunks = verses[v]
        if not any(c in POETIC for c, _ in chunks):
            new_items.append(staged_raw[v])
            continue
        new_para, counts = rebuild_verse(v, chunks, body)
        if new_para is None:
            rec.update(disposition="STOPPED", reason=counts)
            return rec
        for k2 in totals:
            totals[k2] += counts[k2]
        new_items.append(new_para)
    new_span_paras = [rparas[ri]] + new_items
    if norm("\n\n".join(new_span_paras)) != norm("\n\n".join(rparas[ri:rj])):
        rec.update(disposition="STOPPED", reason="word-stream identity assertion failed on books reader")
        return rec
    rec.update(disposition="RESTORED", divisions=totals, surfaces=[])
    if not apply:
        rec["disposition"] = "RESTORED (dry run)"
        return rec
    # --- write readers by byte-splice of the chapter span, then transplant to editions
    for surf in surfaces:
        path = os.path.join(STG, surf)
        text = open(path, encoding="utf-8").read()
        spans = split_paras(text)
        paras = [p for _, _, p in spans]
        si, sj = chapter_span(paras, display, ch, nch)
        if norm("\n\n".join(paras[si:sj])) != norm("\n\n".join(rparas[ri:rj])):
            rec.update(disposition="STOPPED",
                       reason=f"surface {surf}: chapter word stream differs from books reader; not written")
            return rec
        start = spans[si][0]
        end = spans[sj - 1][1]
        new_text = text[:start] + "\n\n".join(new_span_paras) + text[end:]
        assert norm(new_text) == norm(text), f"{surf}: whole-file word-stream assertion failed"
        open(path, "w", encoding="utf-8").write(new_text)
        rec["surfaces"].append(surf)
    return rec

def main():
    global READERS_ONLY
    book = sys.argv[1]
    chapters = [int(x) for x in sys.argv[2].split(",")]
    apply = "--apply" in sys.argv
    READERS_ONLY = "--readers-only" in sys.argv
    tag = os.environ.get("RECOVERY_TAG", "")
    out_path = os.path.join(RESULTS, f"{book}{'-' + tag if tag else ''}.json")
    prior = json.load(open(out_path)) if os.path.exists(out_path) else []
    for ch in chapters:
        try:
            rec = process_chapter(book, ch, apply)
        except Exception as e:
            rec = {"book": book, "chapter": ch, "ruling": "Ruling 8 (as amended 2026-10-18)",
                   "disposition": "STOPPED", "reason": f"exception: {type(e).__name__}: {e}"}
        prior = [r for r in prior if r["chapter"] != ch] + [rec]
        d = rec["disposition"]
        extra = rec.get("divisions") or rec.get("reason") or ""
        print(f"{book} {ch}: {d} {extra}")
    json.dump(prior, open(out_path, "w"), indent=1)

if __name__ == "__main__":
    main()
