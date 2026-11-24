# RECOVERY PASS — PILOT LOG + METHOD NOTE (coordinator)

Pass: Lineation Recovery Pass, Clear Translation Bible fix pass. Ruling cited at every place:
**Ruling 8 as amended by the editor 2026-10-18, 06:30 CDT** — where the recorded apparatuses do
not carry a chapter's divisions in full, the divisions may be read from the base's own pages
(the public-domain WEB Classic, the declared base of the whole work), under the same discipline:
wording asserted identical chapter by chapter; the stop rule wherever a page does not speak
plainly; base-prose chapters never relineated; no division invented.

## Source

The base's own pages at ebible.org, `https://ebible.org/eng-web/<CODE><NN>.htm` — the same
pages the audit crews fetched live throughout the audit (each chapter's apparatus cites its
page). The pages carry the base's lineation as HTML block classes: `q`, `q2`, `qs` (Selah),
`p`, `m`, `d` (descriptive heading: psalm superscriptions, Psalm 119's letter headings),
`b` (empty separator). Verse starts are marked in place by `<span class="verse" id="VN">`.
Fetched pages are cached in `fix-pass/recovery-cache/` (a page enters the cache only after
validation that it carries a chapter label). Footnote anchors (`<a class="notemark">`, dagger
plus popup text) are apparatus matter and are stripped whole before any text is read.

## Method (scripts: fix-pass/recovery.py, verify_recovery.py, editions_apply_recovery.py)

1. Parse the base page into, per verse, the ordered list of (kind, text) chunks; `d` blocks
   are standalone paragraphs, never verse text.
2. Take each verse's split points and division kinds from the base ONLY. The staged text's
   own wording is kept: split points are mapped from base tokens to staged tokens by token
   alignment (difflib). A split point falling strictly inside a conversion span (where the
   draft's wording differs from the base's) is ambiguous — the chapter STOPS, logged, prose kept.
3. Representation (Lane C's, unchanged): divisions as lines within the verse paragraph —
   q flush left; q2 indented two spaces; m on its own unindented line; **qs (Selah) on its
   own unindented line** (coordinator's representation decision for the one kind Lane C
   never met, recorded here: the Selah stands in the staged prose at the verse's end, and
   becomes the verse paragraph's last line); prose lead on the verse's first line; verse
   number at the head of the verse's first line (inside the indent when a verse begins in
   a q2 division); prose tail after a poetry block on its own unindented line. Verses with
   no poetic chunk keep their staged paragraph byte-for-byte.
4. Assertions before any write: verse set of the staged chapter == verse set of the base
   page; standalone ('d') blocks match; the rebuilt chapter's whitespace-collapsed word
   stream is character-identical to the staged chapter before rebuilding. After writing,
   the whole file's collapsed word stream must equal its pre-write stream.
5. Dispositions: RESTORED (rebuilt and asserted); PAGE-PROSE (the base page carries no
   q/q2/qs division anywhere in the chapter — nothing exists to restore; left as staged);
   STOPPED (anomaly logged, chapter left exactly as staged, nothing written anywhere).
6. Surfaces: workers write the two readers only (`books/`, `individual-books/`); the
   coordinator transplants into the editions serially (asserted word-stream identity
   before each splice), as Lane C organized it. OT books also go to the Hebrew edition.
7. Verification: verify_recovery.py re-parses the base page and re-derives the expected
   chapter from the current staged wording, comparing paragraph-for-paragraph, and checks
   every surface carries the identical chapter span.

## Pilot wave (coordinator, 2026-10-18) — method proven before any delegation

| Chapter | Result | Divisions (q/q2/m/qs) | Cross-check |
|---|---|---|---|
| Psalm 1 | RESTORED | 6 / 9 / 0 / 0 | page class inventory 6 q, 9 q2 — exact |
| Psalm 3 | RESTORED | 9 / 9 / 0 / 3 | page class inventory 9 q, 9 q2, 3 qs — exact; superscription paragraph untouched; read back in full |
| Deuteronomy 32 | RESTORED | 60 / 85 / 0 / 0 | page class inventory 60 q, 85 q2 — exact |
| John 19 | RESTORED | 1 / 1 / 1 / 0 | matches the counts RECORDED in ch. 19's apparatus (1 q, 1 q2, m tail) — the record's partial count confirmed by the page |
| Romans 12 | RESTORED | 1 / 2 / 0 / 0 | matches the counts recorded in ch. 12's apparatus (1 q, 2 q2) |
| Ezekiel 37 | PAGE-PROSE | 0 / 0 / 0 / 0 | base page is prose blocks throughout (10 p, no q/q2/qs); nothing to restore; left as staged |

All five restored pilot chapters re-verified by independent re-extraction
(verify_recovery.py: VERIFIED on every surface, editions included — the pilot was applied
to all surfaces directly). John 19:24 read back in Lane C's exact form: prose lead, q,
q2, then the m tail "Therefore the soldiers did these things." on its own line.

Scope reconciliation: the stopped chapters enumerated in Lane C's logs (lane-c2-log.md
extraction, recovery-scope-ot.json) total OT 374 stopped / 51 base-prose skipped — matching
Lane C's own totals exactly; NT stopped per lane-c1-log.md: 1 Corinthians 1, 2; Romans 3, 4,
8, 9, 10, 11, 12, 14, 15; Acts 1, 2, 4, 7, 8, 13, 15, 28; John 12, 19 (John 1 examined in the
NT wave; its record already establishes base prose). The 22 Lane C chapters are NOT in scope
and are not touched. Zephaniah has no stopped chapters (all three chapters were base-prose
skips in Lane C) and Ecclesiastes' scope is chapters 3, 10, 11, 12 only.
