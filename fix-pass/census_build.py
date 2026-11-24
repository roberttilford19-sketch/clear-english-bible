#!/usr/bin/env python3
"""Fix-pass surface census builder. Reads ONLY the staging tree.
Extracts each enumerated verse from staging/books/<BOOK>-reader.txt and
locates it (whitespace-normalized) on every staged surface."""
import os, re, sys, json

STAGE = os.path.expanduser("~/workspace/ceb-push/fix-pass/staging")
BOOKS = os.path.join(STAGE, "books")
INDIV = os.path.join(STAGE, "individual-books")
EDITIONS = {
    "catholic": os.path.join(STAGE, "editions/catholic/clear-translation-bible-catholic-edition.txt"),
    "protestant": os.path.join(STAGE, "editions/protestant/clear-translation-bible-protestant-edition.txt"),
    "hebrew": os.path.join(STAGE, "editions/hebrew/the-torah-the-prophets-and-the-writings.txt"),
}

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

_edition_cache = {}
def edition_text(name):
    if name not in _edition_cache:
        with open(EDITIONS[name], encoding="utf-8") as f:
            _edition_cache[name] = norm(f.read())
    return _edition_cache[name]

def book_file(book):
    key = re.sub(r"[^A-Z0-9]", "", book.upper())
    for fn in os.listdir(BOOKS):
        if re.sub(r"[^A-Z0-9]", "", fn.upper().replace("-READER.TXT", "")) == key:
            return os.path.join(BOOKS, fn)
    return None

def indiv_file(book):
    p = book_file(book)
    if not p:
        return None
    cand = os.path.join(INDIV, os.path.basename(p))
    return cand if os.path.exists(cand) else None

def parse_reader(path):
    """Return {chapter: {verse: text}} from a reader file.
    Chapters are heading paragraphs '<Name> <n>'; verses are paragraphs
    starting '<n> '. A verse's text includes any following unnumbered
    paragraphs up to the next verse/chapter heading (defensive)."""
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    paras = [p.strip() for p in re.split(r"\n\s*\n", raw) if p.strip()]
    # Pass 1: find the display name — the heading prefix whose trailing
    # numbers form the longest 1..N run across the file.
    from collections import defaultdict
    cand = defaultdict(list)
    for p in paras:
        m = re.match(r"^(.+?)\s+(\d+)$", p)
        if m and len(p) < 45 and not re.search(r"[.!?;:,]", p):
            cand[m.group(1)].append(int(m.group(2)))
    display = None
    best = 0
    for name, nums in cand.items():
        s = set(nums)
        run = 0
        while run + 1 in s:
            run += 1
        if run > best:
            best = run
            display = name
    chapters = {}
    cur_ch = None
    cur_v = None
    for p in paras:
        m = re.match(r"^(.+?)\s+(\d+)$", p)
        if m and display is not None and m.group(1) == display and len(p) < 45 \
                and not re.search(r"[.!?;:,]", p):
            n = int(m.group(2))
            if cur_ch is None or n == cur_ch + 1 or n == 1:
                cur_ch = n
                chapters.setdefault(cur_ch, {})
                cur_v = None
                continue
        mv = re.match(r"^(\d+)\s+(.*)$", p, re.S)
        if mv and cur_ch is not None:
            cur_v = int(mv.group(1))
            chapters[cur_ch][cur_v] = mv.group(2).strip()
            continue
        if cur_ch is not None and cur_v is not None:
            # continuation paragraph of current verse
            chapters[cur_ch][cur_v] += "\n" + p
    return chapters

_reader_cache = {}
def get_verse(book, ch, v):
    if book not in _reader_cache:
        p = book_file(book)
        if not p:
            return None
        _reader_cache[book] = parse_reader(p)
    return _reader_cache[book].get(ch, {}).get(v)

def surfaces_for(book, verse_text):
    """Which staged surfaces carry this verse text (normalized search)."""
    out = []
    p = book_file(book)
    if p:
        out.append("books/" + os.path.basename(p))
    ip = indiv_file(book)
    anchor = norm(verse_text)[:70]
    if ip:
        with open(ip, encoding="utf-8") as f:
            if anchor in norm(f.read()):
                out.append("individual-books/" + os.path.basename(ip))
    for name in ("catholic", "protestant", "hebrew"):
        if anchor in edition_text(name):
            out.append("editions/" + name)
    return out

PLACES = {
 "A": [("1 Peter",3,20),("Numbers",8,25),("Numbers",8,26),
       ("2 Chronicles",19,9),("2 Chronicles",19,11),
       ("2 Chronicles",23,4),("2 Chronicles",23,5),("2 Chronicles",23,6),("2 Chronicles",23,7),
       ("Nehemiah",10,38),("Nehemiah",10,39),("Ezra",6,8)],
 "D": [("Job",10,6),("Job",13,23),("Hosea",12,8),("Jeremiah",16,10),
       ("Jeremiah",36,3),("Nehemiah",9,2)],
 "E": [("Judith",7,27),("Revelation",18,13),("Revelation",18,14)],
 "G": [("Ezekiel",3,19),("Ezekiel",3,21),("Ezekiel",13,18),("Ezekiel",13,20),
       ("Ezekiel",14,14),("Ezekiel",14,20),("Ezekiel",18,4),("Ezekiel",18,20),
       ("Ezekiel",18,27),("Ezekiel",33,5),("Ezekiel",33,9),
       ("Isaiah",3,9),("Sirach",6,2),("Matthew",10,28),("Matthew",26,38),
       ("Mark",14,34),("Leviticus",22,3),("Lamentations",2,12),
       ("Hebrews",4,12),("Hebrews",6,19),("Hebrews",10,38)],
}
F_MEMBERS = [("Ruth",3,1),("Joshua",7,8),("Judges",13,12),("Judges",20,18),
 ("Judges",20,23),("Judges",20,28),("Ezra",9,10),("Genesis",30,31),
 ("Exodus",2,7),("Exodus",17,4),("1 Samuel",5,8),("1 Samuel",6,2),
 ("1 Samuel",10,2),("1 Samuel",14,37),("1 Samuel",14,45),("1 Samuel",23,2),
 ("1 Samuel",25,11),("1 Samuel",28,11),("1 Samuel",28,15),
 ("2 Samuel",2,1),("2 Samuel",5,19),("2 Samuel",11,11),("2 Samuel",16,20),
 ("2 Samuel",17,6),("2 Samuel",19,22),("1 Kings",22,15),("2 Kings",2,9),
 ("2 Kings",3,8),("2 Kings",6,15),("2 Kings",6,21),("2 Kings",20,9),
 ("1 Chronicles",11,19),("1 Chronicles",14,10),("2 Chronicles",18,5),
 ("2 Chronicles",18,14),("2 Chronicles",25,9),("Tobit",5,14),
 ("Judith",12,12),("Esther",6,6),("Job",2,10),("Job",32,16),
 ("Psalms",116,12),("Isaiah",6,8),("Hosea",6,4),("Micah",6,6),("Micah",6,7),
 ("Jonah",1,11),("Song of Songs",8,8),("Sirach",24,7),("1 Maccabees",14,25),
 ("Acts",2,37),("Acts",22,10),("1 Corinthians",4,21),("Matthew",18,21),
 ("Matthew",19,16),("Matthew",27,22),("Mark",6,24),("Mark",10,17),
 ("Mark",15,12),("Luke",10,25),("Luke",18,18),("Luke",20,13),("John",19,15)]
F_CANDIDATES = [("Romans",6,1),("Romans",6,15),("Romans",7,7),("Romans",8,31),
 ("Romans",9,14),("Romans",9,30),("Romans",3,5),("Romans",3,31),("Romans",4,1),
 ("Acts",4,16),("Acts",8,36),("Acts",21,22),("Acts",25,9),
 ("1 Corinthians",6,15),("1 Corinthians",11,22),("1 Corinthians",14,6),
 ("1 Corinthians",14,15),("Hebrews",11,32),("Hebrews",12,9),
 ("James",3,13),("James",5,13),("James",5,14),("2 Peter",3,11),
 ("John",12,27),("John",13,37),("John",18,39),("Matthew",11,16),
 ("Matthew",9,5),("Matthew",26,15),("Matthew",27,17),("Matthew",27,21),
 ("Mark",6,37),("Mark",2,9),("Mark",15,9),("Luke",9,41),("Luke",13,18),
 ("Luke",13,20),("Luke",22,49),("Jeremiah",6,10),("Jeremiah",8,14),
 ("Jeremiah",9,7),("Jeremiah",15,2),("Isaiah",8,19),("Isaiah",10,11),
 ("Isaiah",20,6),("Isaiah",38,15),("Isaiah",40,6),("Isaiah",44,19),
 ("Isaiah",51,19),("Isaiah",52,5),("Isaiah",57,6),("Isaiah",66,9),
 ("Lamentations",2,13),("Malachi",3,7),("Zechariah",7,3),
 ("Sirach",14,15),("Sirach",49,11),("Proverbs",22,27),("1 Maccabees",3,17)]
PLACES["F-members"] = F_MEMBERS
PLACES["F-candidates"] = F_CANDIDATES

def main():
    result = {}
    failures = []
    for lane, places in PLACES.items():
        rows = []
        for (book, ch, v) in places:
            text = get_verse(book, ch, v)
            if text is None:
                failures.append(f"{lane}: {book} {ch}:{v} NOT EXTRACTED")
                rows.append({"place": f"{book} {ch}:{v}", "error": "not extracted"})
                continue
            surfs = surfaces_for(book, text)
            rows.append({"place": f"{book} {ch}:{v}", "text": norm(text),
                         "surfaces": surfs})
        result[lane] = rows
    with open(os.path.expanduser("~/workspace/ceb-push/fix-pass/census-raw.json"), "w") as f:
        json.dump({"result": result, "failures": failures}, f, indent=1)
    print("failures:", len(failures))
    for x in failures:
        print(" ", x)
    for lane, rows in result.items():
        ok = sum(1 for r in rows if "text" in r)
        print(lane, ok, "/", len(rows), "extracted")

if __name__ == "__main__":
    main()
