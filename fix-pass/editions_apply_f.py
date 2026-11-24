#!/usr/bin/env python3
"""Coordinator serial application of Lane F-1 + F-2 changes to the edition surfaces.
F-1 entries: sentence fragments -> replace in each edition carrying the book.
F-2 entries: verse bodies (no verse number) -> replace the full paragraph 'N body'.
Every replacement asserted to occur exactly once in its file. Log appended to logs/lane-f-editions-application.md.
"""
import json, os, sys

BASE = os.path.expanduser("~/workspace/ceb-push/fix-pass")
STG = os.path.join(BASE, "staging")
EDITIONS = {
    "catholic": "editions/catholic/clear-translation-bible-catholic-edition.txt",
    "protestant": "editions/protestant/clear-translation-bible-protestant-edition.txt",
    "hebrew": "editions/hebrew/the-torah-the-prophets-and-the-writings.txt",
}
DEUTERO = {"Judith", "1 Maccabees"}          # catholic edition only (F-1)
NT_BOOKS = None                               # F-2 is all NT: catholic + protestant only

log = []
def apply(rel, old, new, label):
    path = os.path.join(STG, rel)
    text = open(path, encoding="utf-8").read()
    n = text.count(old)
    assert n == 1, f"{label} in {rel}: found {n} occurrences of target (expected 1)"
    open(path, "w", encoding="utf-8").write(text.replace(old, new))
    log.append(f"- {label} — {rel}: applied (1 replacement)")

f1 = json.load(open(os.path.join(BASE, "logs/lane-f1-changes.json"), encoding="utf-8"))
for e in f1:
    targets = ["catholic"] if e["book"] in DEUTERO else ["catholic", "protestant", "hebrew"]
    for t in targets:
        apply(EDITIONS[t], e["before"], e["after"], f"F-1 {e['place']} ({t})")

f2 = json.load(open(os.path.join(BASE, "logs/lane-f2-changes.json"), encoding="utf-8"))
for e in f2:
    old = f"{e['verse']} {e['before']}"
    new = f"{e['verse']} {e['after']}"
    for t in ["catholic", "protestant"]:
        apply(EDITIONS[t], old, new, f"F-2 {e['place']} ({t})")

out = os.path.join(BASE, "logs/lane-f-editions-application.md")
with open(out, "a", encoding="utf-8") as fh:
    fh.write("\n".join(log) + "\n")
print(f"applied {len(log)} edition replacements")
