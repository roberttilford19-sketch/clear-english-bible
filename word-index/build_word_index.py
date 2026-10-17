#!/usr/bin/env python3
"""Build WORD-INDEX.md — a mechanical index of every word in the 73-book
Clear English Bible draft corpus, from the staged reader files in ../books/.

Tokenization rules (also stated at the top of WORD-INDEX.md):
  * The corpus is the complete staged reader files, exactly as staged,
    including each book's header and draft notice, and including verse
    numerals as they stand in the files.
  * A word (token) is a maximal run of Unicode letters and digits.
    An apostrophe (' or U+2019) inside such a run counts as part of the
    word when it sits between two letters/digits, so "God's" and "don't"
    are single words; a leading or trailing apostrophe is punctuation
    and is stripped.
  * Words are case-folded to lowercase (Unicode casefold).
  * Every other character — whitespace, punctuation, quotation marks,
    dashes, colons — is a separator. Numbers are words: "1" and "50"
    are entries in the index.

Verification: the whole of Genesis is also counted by an independent
implementation (Perl, Unicode regex) and the two frequency tables are
compared in full before the index is written; the build fails if they
differ. Run:  python3 build_word_index.py [perl-genesis-freq.tsv]
where the optional TSV holds "word<TAB>count" lines from the Perl pass.
"""
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
BOOKS = HERE.parent / "books"

ORDER = [
    ("Genesis", "genesis-reader.txt"), ("Exodus", "EXODUS-reader.txt"),
    ("Leviticus", "LEVITICUS-reader.txt"), ("Numbers", "NUMBERS-reader.txt"),
    ("Deuteronomy", "DEUTERONOMY-reader.txt"), ("Joshua", "JOSHUA-reader.txt"),
    ("Judges", "JUDGES-reader.txt"), ("Ruth", "RUTH-reader.txt"),
    ("1 Samuel", "1SAMUEL-reader.txt"), ("2 Samuel", "2SAMUEL-reader.txt"),
    ("1 Kings", "1KINGS-reader.txt"), ("2 Kings", "2KINGS-reader.txt"),
    ("1 Chronicles", "1CHRONICLES-reader.txt"), ("2 Chronicles", "2CHRONICLES-reader.txt"),
    ("Ezra", "EZRA-reader.txt"), ("Nehemiah", "NEHEMIAH-reader.txt"),
    ("Tobit", "TOBIT-reader.txt"), ("Judith", "JUDITH-reader.txt"),
    ("Esther", "ESTHER-reader.txt"), ("Job", "JOB-reader.txt"),
    ("Psalms", "PSALMS-reader.txt"), ("Proverbs", "PROVERBS-reader.txt"),
    ("Ecclesiastes", "ECCLESIASTES-reader.txt"), ("Song of Songs", "SONGOFSONGS-reader.txt"),
    ("Wisdom", "WISDOM-reader.txt"), ("Sirach", "SIRACH-reader.txt"),
    ("Isaiah", "ISAIAH-reader.txt"), ("Jeremiah", "JEREMIAH-reader.txt"),
    ("Lamentations", "LAMENTATIONS-reader.txt"), ("Baruch", "BARUCH-reader.txt"),
    ("Ezekiel", "EZEKIEL-reader.txt"), ("Daniel", "DANIEL-GREEK-reader.txt"),
    ("Hosea", "HOSEA-reader.txt"), ("Joel", "JOEL-reader.txt"),
    ("Amos", "AMOS-reader.txt"), ("Obadiah", "OBADIAH-reader.txt"),
    ("Jonah", "JONAH-reader.txt"), ("Micah", "MICAH-reader.txt"),
    ("Nahum", "NAHUM-reader.txt"), ("Habakkuk", "HABAKKUK-reader.txt"),
    ("Zephaniah", "ZEPHANIAH-reader.txt"), ("Haggai", "HAGGAI-reader.txt"),
    ("Zechariah", "ZECHARIAH-reader.txt"), ("Malachi", "MALACHI-reader.txt"),
    ("1 Maccabees", "1MACCABEES-reader.txt"), ("2 Maccabees", "2MACCABEES-reader.txt"),
    ("Matthew", "MATTHEW-reader.txt"), ("Mark", "MARK-reader.txt"),
    ("Luke", "LUKE-reader.txt"), ("John", "JOHN-reader.txt"),
    ("Acts", "ACTS-reader.txt"), ("Romans", "ROMANS-reader.txt"),
    ("1 Corinthians", "1-CORINTHIANS-reader.txt"), ("2 Corinthians", "2-CORINTHIANS-reader.txt"),
    ("Galatians", "GALATIANS-reader.txt"), ("Ephesians", "EPHESIANS-reader.txt"),
    ("Philippians", "PHILIPPIANS-reader.txt"), ("Colossians", "COLOSSIANS-reader.txt"),
    ("1 Thessalonians", "1-THESSALONIANS-reader.txt"),
    ("2 Thessalonians", "2-THESSALONIANS-reader.txt"),
    ("1 Timothy", "1-TIMOTHY-reader.txt"), ("2 Timothy", "2-TIMOTHY-reader.txt"),
    ("Titus", "TITUS-reader.txt"), ("Philemon", "PHILEMON-reader.txt"),
    ("Hebrews", "HEBREWS-reader.txt"), ("James", "JAMES-reader.txt"),
    ("1 Peter", "1-PETER-reader.txt"), ("2 Peter", "2-PETER-reader.txt"),
    ("1 John", "1-JOHN-reader.txt"), ("2 John", "2-JOHN-reader.txt"),
    ("3 John", "3-JOHN-reader.txt"), ("Jude", "JUDE-reader.txt"),
    ("Revelation", "REVELATION-reader.txt"),
]

APOS = {"'", "’"}


def tokens(text):
    """Yield case-folded tokens per the stated rules (character state machine)."""
    out = []
    buf = []
    chars = list(text)
    n = len(chars)
    for i, c in enumerate(chars):
        if c.isalnum():
            buf.append(c)
        elif c in APOS and buf and i + 1 < n and chars[i + 1].isalnum():
            buf.append(c)
        else:
            if buf:
                out.append("".join(buf).casefold())
                buf = []
    if buf:
        out.append("".join(buf).casefold())
    return out


def main():
    per_book = {}
    total = Counter()
    for name, fname in ORDER:
        text = (BOOKS / fname).read_text(encoding="utf-8")
        c = Counter(tokens(text))
        per_book[name] = c
        total.update(c)

    vocab = sorted(total)
    grand = sum(total.values())

    verif = ("No independent recount was supplied to this build, so no "
             "verification figure is claimed in this header.")
    if len(sys.argv) > 1:
        perl = {}
        for line in Path(sys.argv[1]).read_text(encoding="utf-8").splitlines():
            if "\t" in line:
                w, n = line.split("\t")
                perl[w] = int(n)
        mine = dict(per_book["Genesis"])
        if perl != mine:
            only_p = sorted(set(perl) - set(mine))[:10]
            only_m = sorted(set(mine) - set(perl))[:10]
            diffn = [w for w in set(perl) & set(mine) if perl[w] != mine[w]][:10]
            print("FATAL: Genesis tables differ.")
            print(" only in perl:", only_p)
            print(" only in python:", only_m)
            print(" count diffs:", [(w, perl[w], mine[w]) for w in diffn])
            return 1
        verif = (f"Independent verification: the whole of Genesis was recounted by a "
                 f"separate implementation (Perl, Unicode regular expressions) under the "
                 f"same stated rules, and the two frequency tables agree exactly — all "
                 f"{len(perl):,} distinct words and all {sum(perl.values()):,} tokens of "
                 f"Genesis match. No other book has been hand-checked; the rest of the "
                 f"index is machine-generated and unchecked by hand beyond this verification.")
        print(f"Genesis verification: AGREE ({len(perl)} words, {sum(perl.values())} tokens)")

    lines = []
    lines.append("# Word Index — Clear Translation Bible (Clear English Bible draft corpus)")
    lines.append("")
    lines.append("A complete index of every word used in the 73 books of the draft corpus, "
                 "generated mechanically by script (`build_word_index.py`, kept beside this file) "
                 "from the staged reader files in `books/`. It is a machine-generated index: no "
                 "entry was written or corrected by hand.")
    lines.append("")
    lines.append("## Tokenization rules")
    lines.append("")
    lines.append("- The corpus is the complete staged reader files, exactly as staged, including each "
                 "book's header and draft notice, and including the verse numerals as they stand in the files.")
    lines.append("- A word (token) is a maximal run of Unicode letters and digits. An apostrophe "
                 "(' or ') inside such a run counts as part of the word when it sits between two "
                 "letters or digits, so \"God's\" and \"don't\" are single words; a leading or trailing "
                 "apostrophe is punctuation and is stripped.")
    lines.append("- Words are case-folded to lowercase. Every other character — whitespace, punctuation, "
                 "quotation marks, dashes, colons — is a separator.")
    lines.append("- Numbers are words: the verse and chapter numerals are entries in this index like any other word.")
    lines.append("")
    lines.append("## Totals")
    lines.append("")
    lines.append(f"- Total words (tokens) in the corpus: **{grand:,}**")
    lines.append(f"- Distinct words (vocabulary): **{len(vocab):,}**")
    lines.append(f"- Words occurring exactly once: **{sum(1 for w in vocab if total[w] == 1):,}**")
    lines.append("")
    lines.append("## Verification")
    lines.append("")
    lines.append(verif)
    lines.append("")
    lines.append("## Tokens per book")
    lines.append("")
    for name, _ in ORDER:
        lines.append(f"- {name}: {sum(per_book[name].values()):,}")
    lines.append("")
    lines.append("## The index")
    lines.append("")
    lines.append("Each entry gives the word, its total count across the corpus, and its count in each "
                 "book where it occurs (books named only where the count is above zero).")
    lines.append("")
    book_names = [n for n, _ in ORDER]
    for w in vocab:
        parts = [f"{b}: {per_book[b][w]}" for b in book_names if per_book[b][w]]
        lines.append(f"- **{w}** — {total[w]:,} — " + "; ".join(parts))
    lines.append("")

    out = HERE / "WORD-INDEX.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out} — {grand:,} tokens, {len(vocab):,} distinct words, "
          f"{out.stat().st_size:,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
