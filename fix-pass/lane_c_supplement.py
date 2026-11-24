#!/usr/bin/env python3
"""Lane C supplement (coordinator): Revelation 5, 7, 15 lineation from the chapters'
own apparatuses (divisions quoted in full, auditor-verified). Same representation
and assertions as Lane C-1: segments must concatenate to the current verse body.
Applies to staged readers, then transplants the chapters into catholic + protestant.
"""
import json, os, re

STG = os.path.expanduser("~/workspace/ceb-push/fix-pass/staging")
# segments: list of (kind, text); kind in {"lead","q","q2"}; verse number handled separately
SPEC = {
    5: {9: [("lead", "They sang a new song, saying,"),
            ("q", "“You are worthy to take the book"),
            ("q2", "and to open its seals,"),
            ("q", "for you were killed,"),
            ("q2", "and bought us for God with your blood"),
            ("q2", "out of every tribe, language, people, and nation,")],
        10: [("q", "and made us kings and priests to our God;"),
             ("q2", "and we will reign on the earth.”")]},
    7: {5: [("q", "of the tribe of Judah twelve thousand were sealed,"),
            ("q", "of the tribe of Reuben twelve thousand,"),
            ("q", "of the tribe of Gad twelve thousand,")],
        6: [("q", "of the tribe of Asher twelve thousand,"),
            ("q", "of the tribe of Naphtali twelve thousand,"),
            ("q", "of the tribe of Manasseh twelve thousand,")],
        7: [("q", "of the tribe of Simeon twelve thousand,"),
            ("q", "of the tribe of Levi twelve thousand,"),
            ("q", "of the tribe of Issachar twelve thousand,")],
        8: [("q", "of the tribe of Zebulun twelve thousand,"),
            ("q", "of the tribe of Joseph twelve thousand, and"),
            ("q", "of the tribe of Benjamin twelve thousand were sealed.")]},
    15: {3: [("lead", "They sang the song of Moses, the servant of God, and the song of the Lamb, saying,"),
             ("q", "“Great and marvelous are your works, Lord God, the Almighty!"),
             ("q2", "Righteous and true are your ways, you King of the nations.")],
         4: [("q", "Who wouldn’t fear you, Lord,"),
             ("q2", "and glorify your name?"),
             ("q", "For you only are holy."),
             ("q2", "For all the nations will come and worship before you."),
             ("q2", "For your righteous acts have been revealed.”")]},
}

def rebuild_verse(vnum, body, segs):
    joined = " ".join(t for _, t in segs)
    assert joined == body, f"v{vnum}: segments do not reproduce verse body"
    lines = []
    for i, (kind, t) in enumerate(segs):
        prefix = f"{vnum} " if i == 0 else ""
        indent = "  " if kind == "q2" else ""
        # verse number precedes the indent only when the verse begins inside a q2;
        # here no verse begins inside a q2, so number simply heads the first line.
        lines.append(f"{indent}{prefix}{t}" if not (i == 0) else f"{prefix}{indent}{t}")
    return "\n".join(lines)

def process_file(path):
    text = open(path, encoding="utf-8").read()
    paras = re.split(r"\n\s*\n", text)
    # locate Revelation chapter spans by heading paragraphs "Revelation N"
    for ch, verses in SPEC.items():
        head = f"Revelation {ch}"
        assert paras.count(head) == 1, f"{path}: heading {head}"
        i = paras.index(head)
        j = i + 1
        while j < len(paras) and not paras[j].startswith("Clear English Bible — ") and paras[j].strip() != f"Revelation {ch+1}":
            j += 1
        for vnum, segs in verses.items():
            for k in range(i + 1, j):
                m = re.match(rf"^{vnum} ", paras[k])
                if m:
                    body = paras[k][len(str(vnum)) + 1:]
                    paras[k] = rebuild_verse(vnum, body, segs)
                    break
            else:
                raise AssertionError(f"{path}: verse {ch}:{vnum} not found")
    open(path, "w", encoding="utf-8").write("\n\n".join(paras))

for rel in ["books/REVELATION-reader.txt", "individual-books/REVELATION-reader.txt"]:
    process_file(os.path.join(STG, rel))
print("readers rebuilt: Revelation 5, 7, 15")
