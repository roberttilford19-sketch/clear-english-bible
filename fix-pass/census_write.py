#!/usr/bin/env python3
"""Write SURFACE-CENSUS.md from census-raw.json + snapshot/report sources."""
import json, os, re

FIX = os.path.expanduser("~/workspace/ceb-push/fix-pass")
GOAL = os.path.expanduser("~/workspace/goals/clear-english-bible-translation")
d = json.load(open(os.path.join(FIX, "census-raw.json")))
res = d["result"]

def surf_short(surfs):
    out = []
    for s in surfs:
        if s.startswith("books/"):
            out.append("books")
        elif s.startswith("individual-books/"):
            out.append("indiv")
        else:
            out.append(s.split("/")[1])
    return ", ".join(out)

L = []
L.append("# FIX PASS — SURFACE CENSUS (first deliverable, before any text change)")
L.append("")
L.append("Date: 2026-10-18. Authority: FIX-PASS-BRIEF-2026-10-18.md; RULINGS-GIVEN-2026-10-18.md.")
L.append("All work is in the staging tree `fix-pass/staging/` (a copy of `books/`, `individual-books/`, `editions/`). The live shelf is untouched.")
L.append("")
L.append("## Method and surface model")
L.append("")
L.append("Every verse below was extracted from the staged `books/` reader by a parser (chapter-heading + numbered-verse paragraphs), then located on every other staged surface by whitespace-normalized substring search. Extraction succeeded for **185 of 185 enumerated places** (Lanes A, D, E, G, F-members, F-candidates), with **zero extraction failures**. A verse's surfaces are some of five: `books/<BOOK>-reader.txt` (all 73 books), `individual-books/<BOOK>-reader.txt` (the 66-book Protestant set), `editions/catholic` (73 books), `editions/protestant` (66 books), `editions/hebrew` (the 39-book Hebrew-canon volume). In the tables, surfaces are abbreviated: books / indiv / catholic / protestant / hebrew.")
L.append("")
L.append("Verification on samples (brief requirement): (1) 1 Peter 3:20 was read directly in all four of its staged surfaces by independent grep — the draft's \"eight people\" stands in `books/1-PETER-reader.txt` line 149 and in both editions, and \"eight souls\" stands nowhere yet, as expected before the fix. (2) For every Lane A place, the raw verse paragraph in the `books/` reader was compared byte-for-byte against each edition surface: **all identical**, so exact-paragraph replacement is the safe change mechanism for Lane A. (3) Sample extracted texts were read against the packet's descriptions and matched (Numbers 8:25–26 \"must\" side; Nehemiah 10:38 both \"must\" instances; Job 10:6 and Nehemiah 9:2 doubled \"sin\"; Jonah 1:11 and Acts 2:37 drafted \"shall\"; Song of Songs 8:8 drafted \"must\"). (4) Deuterocanonical places (Judith, Tobit, Sirach, Maccabees) correctly show only books + catholic surfaces; New Testament places correctly show no hebrew surface.")
L.append("")
L.append("## Lane A — exact conversions (Ruling 12; Ruling 3)")
L.append("")
L.append("Change plan: at each place, replace the verse paragraph on every surface with the converted paragraph (\"must\" → \"will\" at every standing-duty instance in the named verse; 1 Peter 3:20 \"eight people\" → \"eight souls\"). Log before/after per surface in `logs/lane-a-log.md`.")
L.append("")
L.append("| Place | Drafted text (books reader) | Surfaces |")
L.append("|---|---|---|")
for r in res["A"]:
    L.append(f"| {r['place']} | {r['text']} | {surf_short(r['surfaces'])} |")
L.append("")
L.append("Instance count: 18 \"must\" instances across the ten Ruling 12 verses (Num 8:25 ×2; 8:26 ×3; 2 Chr 19:9 ×1; 19:11 ×1; 23:4 ×2; 23:5 ×1; 23:6 ×2; 23:7 ×1; Neh 10:38 ×2; 10:39 ×1; Ezra 6:8 ×2), plus the single 1 Peter 3:20 restoration.")
L.append("")
L.append("## Lane B — Song of Songs speaker headings (Ruling 18)")
L.append("")
L.append("Surfaces carrying the Song: books/SONGOFSONGS-reader.txt, individual-books/SONGOFSONGS-reader.txt, editions/catholic, editions/hebrew (verified by the book's presence on each; the Song is in the Hebrew canon volume and in the 66-book set). The 33 headings, their words and exact positions, are recorded in the pinned base snapshots (`goals/clear-english-bible-translation/hidden_files/songofsongs-0N-web-base-snapshot-2026-10-16.txt`), whose per-chapter heading lines were verified against the completion report's counts (ch. 1: 9; ch. 2: 5; ch. 3: 0; ch. 4: 2; ch. 5: 5; ch. 6: 5; ch. 7: 1; ch. 8: 6 = 33). Extracted heading records:")
L.append("")
for n in range(1, 9):
    p = os.path.join(GOAL, "hidden_files", f"songofsongs-0{n}-web-base-snapshot-2026-10-16.txt")
    line = ""
    with open(p, encoding="utf-8") as f:
        for ln in f:
            if ln.startswith("Speaker headings"):
                line = ln.strip()
                break
    L.append(f"- **Chapter {n}:** {line if line else 'no speaker-headings line (none recorded)'}")
L.append("")
L.append("Change plan: insert each heading on its own line at its recorded position in the staged Song reader on every surface (before-verse positions as a standalone line before the verse paragraph; after-verse positions as a standalone line after that verse's paragraph; within-verse positions at the recorded sentence boundary). No verse wording changes. Chapter 3 gets none.")
L.append("")
L.append("## Lane C — lineation form pass (Ruling 8)")
L.append("")
L.append("Source of record: each chapter's apparatus in `goals/clear-english-bible-translation/files/<BOOK>-<NN>-DRAFT.md` records the base's divisions in full and in order (verified on Hebrews 1: 9 q + 11 q2 + 1 m, each line quoted exactly), with the completion reports carrying the per-book presentation flags (Decision 8 sources). Surfaces per book follow the surface model above. Governed scope, per Decision 8: 1 Timothy 3:16 (6 divisions); 2 Timothy 2:11–13 (9 divisions); Hebrews chs. 1–5, 7, 8, 10, 12, 13 (88 q/q2 lines + 1 m); 1 Peter chs. 1–3 (18 divisions); Galatians 4:27; the quotation blocks at 1 Corinthians 1:19; 2:9; 15:55 (1 Cor 13 is base-prose, never relineated); 2 Corinthians' and Romans' and Acts' poetry quotation passages; John's prologue and poetry passages; Deuteronomy chs. 32–33 and the joined paragraphs of ch. 27; Revelation's song and list chapters as its chapter files record; and the book-wide presentation flags of Judges, 1 Samuel, 2 Samuel, 1 Chronicles, 2 Chronicles, 2 Kings, Nehemiah, Job, Psalms, Proverbs, Isaiah, Jeremiah, Ezekiel, Hosea, Micah, Zechariah (chs. 9–11, 13), Tobit (ch. 13), Judith, Sirach, Wisdom, Baruch, Greek Daniel, Esther (the prayers), 1 Maccabees, 2 Maccabees, Amos, Joel, Jonah, Habakkuk, Zephaniah, Ecclesiastes, Lamentations, Song of Songs. Red-letter spans riding with the pass: 1 Corinthians 11:24–25; 2 Corinthians 12:9; Revelation 21:5–8.")
L.append("")
L.append("Change plan: per chapter, rebuild the staged reader's prose verse-paragraphs into the recorded lines (q lines flush, q2 lines indented two spaces to carry the base's q/q2 distinction, m prose-link divisions on their own line unindented), preserving every word, punctuation mark, and verse number exactly. Verification per chapter: the rebuilt chapter text, with all whitespace collapsed, must be identical to the pre-change chapter text; verse counts unchanged.")
L.append("")
L.append("## Lane D — the six doubled \"sin and sin\" places (Ruling 6) — REPORT ONLY")
L.append("")
L.append("| Place | Drafted text (books reader) | Surfaces |")
L.append("|---|---|---|")
for r in res["D"]:
    L.append(f"| {r['place']} | {r['text']} | {surf_short(r['surfaces'])} |")
L.append("")
L.append("No text changes in this lane. Output: `DOUBLED-AUDIT.md` with per-place source wording, justification analysis, erased-distinction analysis, and a recommended disposition for the editor.")
L.append("")
L.append("## Lane E — challengeable grounds (Ruling 5, sharpening two) — DOCUMENTATION ONLY")
L.append("")
L.append("| Place | Drafted text (books reader) | Surfaces |")
L.append("|---|---|---|")
for r in res["E"]:
    L.append(f"| {r['place']} | {r['text']} | {surf_short(r['surfaces'])} |")
L.append("")
L.append("Grounds are drafted from the books' own audit records (JUDITH-COMPLETION-REPORT.md flag 1; REVELATION-COMPLETION-REPORT.md and the Revelation 18 chapter draft/audit record). No text changes in this lane.")
L.append("")
L.append("## Lane F — per-context review, deliberative \"shall\" (Rulings 1 + 2)")
L.append("")
L.append("Change plan: work book by book from the completion reports (packet Decision 1/2 source flags). Judge each place against Ruling 1's force-principles (obligation → \"should\"; open course/intention → \"will\"; solemn/formal deliberation or base-precedent weight → \"shall\"; prescribed duty → \"must\"). Drafted forms stand unless a place fails its context test; candidate places are judged with their built-in answers as one unit. Every adjustment logged with its ground; every stand counted. Record-only places (Psalm 116:12; 2 Kings 20:9; Esther 6:6) are unaffected.")
L.append("")
L.append("### Members (Decision 1)")
L.append("")
L.append("| Place | Drafted verse (excerpt) | Surfaces |")
L.append("|---|---|---|")
for r in res["F-members"]:
    L.append(f"| {r['place']} | {r['text'][:130]} | {surf_short(r['surfaces'])} |")
L.append("")
L.append("### Candidates (Decision 2)")
L.append("")
L.append("| Place | Drafted verse (excerpt) | Surfaces |")
L.append("|---|---|---|")
for r in res["F-candidates"]:
    L.append(f"| {r['place']} | {r['text'][:130]} | {surf_short(r['surfaces'])} |")
L.append("")
L.append("## Lane G — soul candidates under the two-trigger rule (Ruling 11)")
L.append("")
L.append("Change plan: judge each place trigger by trigger (Trigger 1: an outcome — saving, destruction, death, deliverance, or the like — predicated of the soul itself → \"soul\" stands; Trigger 2: mere headcount tally → \"people\"). Every candidate already stands in the base's word, so a Trigger 1 judgment confirms the place with no text change; a Trigger 2 judgment would change \"soul\" to \"people\" on every surface. Clean answers settle the place; genuinely borderline places are HELD and reported, never forced.")
L.append("")
L.append("| Place | Drafted text (books reader) | Surfaces |")
L.append("|---|---|---|")
for r in res["G"]:
    L.append(f"| {r['place']} | {r['text'][:150]} | {surf_short(r['surfaces'])} |")
L.append("")
L.append("Ezekiel 13:18 and 13:20 each carry additional candidate occurrences beside the verse's member occurrence (Decision 4), and Matthew 10:28 carries two instances; instance-level treatment is recorded in the lane log.")
L.append("")
L.append("*Census ends. Raw extraction data: `census-raw.json`; builder: `census_build.py`.*")

with open(os.path.join(FIX, "SURFACE-CENSUS.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(L) + "\n")
print("written", len(L), "lines")
