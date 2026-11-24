#!/usr/bin/env python3
"""Lane A: exact conversions. Asserts every replacement; writes the lane log."""
import os, re, json

FIX = os.path.expanduser("~/workspace/ceb-push/fix-pass")
STAGE = os.path.join(FIX, "staging")
census = json.load(open(os.path.join(FIX, "census-raw.json")))["result"]["A"]

EDITION_PATHS = {
    "editions/catholic": "editions/catholic/clear-translation-bible-catholic-edition.txt",
    "editions/protestant": "editions/protestant/clear-translation-bible-protestant-edition.txt",
    "editions/hebrew": "editions/hebrew/the-torah-the-prophets-and-the-writings.txt",
}

def surf_path(s):
    if s in EDITION_PATHS:
        return os.path.join(STAGE, EDITION_PATHS[s])
    return os.path.join(STAGE, s)  # books/... or individual-books/...

def find_para(text, body_text):
    """Locate the unique paragraph whose normalized body equals body_text."""
    hits = []
    start = 0
    while True:
        i = text.find(body_text[:60], start)
        if i < 0:
            break
        a = text.rfind("\n\n", 0, i) + 2
        b = text.find("\n\n", i)
        if b < 0:
            b = len(text)
        para = text[a:b]
        m = re.match(r"^(\d+\s+)(.*)$", para, re.S)
        if m and re.sub(r"\s+", " ", m.group(2)).strip() == body_text:
            hits.append((a, b, para))
        start = i + 1
    assert len(hits) == 1, f"expected 1 matching paragraph, found {len(hits)}"
    return hits[0]

def convert(place, verse_text):
    if place == "1 Peter 3:20":
        assert "eight people" in verse_text
        return verse_text.replace("eight people", "eight souls"), "Ruling 3 (Trigger 1: 'were saved' predicated of the souls) — restore the base's 'eight souls'."
    n = len(re.findall(r"\bmust\b", verse_text, flags=re.I))
    new = re.sub(r"\bMust\b", "Will", verse_text)
    new = re.sub(r"\bmust\b", "will", new)
    return new, n

log = []
file_cache = {}

def load(path):
    if path not in file_cache:
        with open(path, encoding="utf-8") as f:
            file_cache[path] = f.read()
    return file_cache[path]

total_instances = 0
for row in census:
    place, old_text = row["place"], row["text"]
    if place == "1 Peter 3:20":
        new_text, ground = convert(place, old_text)
        ruling = "Ruling 3"
    else:
        new_text, n = convert(place, old_text)
        total_instances += n
        ground = ("Ruling 12 ('will' for the whole class — arrangements described): standing-duty "
                  "'must' in this verse converts to 'will'.")
        ruling = "Ruling 12"
    for surf in row["surfaces"]:
        path = surf_path(surf)
        content = load(path)
        a, b, para = find_para(content, old_text)
        m = re.match(r"^(\d+\s+)(.*)$", para, re.S)
        num, body = m.group(1), m.group(2)
        new_para = num + new_text
        assert content.count(para) == 1, (place, surf, "para not unique")
        file_cache[path] = content.replace(para, new_para)
        log.append((place, surf, old_text, new_text, ruling, ground))

for path, content in file_cache.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

os.makedirs(os.path.join(FIX, "logs"), exist_ok=True)
with open(os.path.join(FIX, "logs", "lane-a-log.md"), "w", encoding="utf-8") as f:
    f.write("# LANE A CHANGE LOG — exact conversions (Ruling 12; Ruling 3)\n\n")
    f.write("Mechanism: exact verse-paragraph replacement on each surface, asserted unique per file. "
            "Ground for every Ruling 12 entry: the ruling reads prescribed arrangements and standing duties as descriptions of how things will stand ('will' for the whole class). "
            "Ground for the 1 Peter entry: Ruling 3, Trigger 1.\n\n")
    for (place, surf, before, after, ruling, ground) in log:
        f.write(f"## {place} — {surf}\n- Ruling: {ruling}\n- Before: {before}\n- After: {after}\n- Ground: {ground}\n\n")
print("log entries:", len(log), "| Ruling 12 'must' instances converted:", total_instances)
