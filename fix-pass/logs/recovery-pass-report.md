# RECOVERY PASS REPORT — poetry lineation read from the base's own pages (Ruling 8 as amended)

Status: COMPLETE for every chapter the amended ruling reaches, with four chapters STOPPED
on three questions that are the desk's to rule (below). Method note:
`logs/recovery-pilot-log.md`; coordinator rulings: `logs/recovery-coordinator-addendum-1.md`
(class rule for pi/mi/nb) and `logs/recovery-coordinator-addendum-2.md` (trailing-newline
artifact; Habakkuk colophon anatomy; Psalms concurrency guard). Per-book logs:
`logs/recovery-<book>-log.md`. All work is in the staging tree; the published shelf was
never written; nothing was pushed or published.

## Totals (396 chapters disposed — the full Lane C stopped scope, reconciled exactly)

- **337 chapters RESTORED** in the base's own lineation, on every surface carrying them.
- **55 chapters PAGE-PROSE**: the base page carries no q/q2/qs division anywhere in the
  chapter, so there is nothing to restore; each stands exactly as staged. (Ezekiel 36 of
  48 — the book's prose frame; Isaiah 12–16; Jeremiah 9; Jonah 1, 3, 4; Deuteronomy 27;
  John 1 among them.)
- **4 chapters STOPPED**, left exactly as staged, on the three desk questions below.
- **Divisions restored: 15,380** — 6,568 q, 8,733 q2, 8 m, 71 qs (Selah lines).
- **Editions: 992 chapter-edition spans transplanted under assertion** (318 restored OT
  chapters × 3 editions + 19 restored NT chapters × 2 editions — the exact expected count).

Per book (restored / page-prose / stopped): Psalms 150/0/0 · Job 40/0/0 · Isaiah 41/5/1 ·
Jeremiah 29/9/0 · Ezekiel 12/36/0 · Deuteronomy 2/1/0 (chs. 32, 33; 27) · Hosea 12/0/0 ·
Micah 7/0/0 · Amos 8/0/0 · Joel 3/0/0 · Zechariah 4/0/0 · Jonah 1/3/0 · Habakkuk 0/0/1 ·
Ecclesiastes 4/0/0 · Lamentations 5/0/0 · Romans 9/0/0 · Acts 6/0/2 · 1 Corinthians 2/0/0 ·
John 2/1/0.

## Verification

Every restored chapter was verified by independent re-extraction (re-parse the base page,
re-derive the chapter from the current staged wording, compare paragraph for paragraph,
confirm every surface carries the identical span): workers verified their full ranges on
the readers; the coordinator verified samples on all surfaces for every wave, ran the full
150-chapter Psalms verification twice consecutively (all VERIFIED), and transplanted all
editions serially under word-stream assertion. Two verification MISMATCHes (Ezekiel 48,
Jonah 4) were diagnosed to a pre-existing trailing newline byte at the end of those staged
reader files — normalized word streams identical, chapters untouched; a verifier artifact,
recorded in Addendum 2, no file normalized.

## Coordinator representation rulings (logged, no division created or destroyed by either)

1. **qs (Selah)** stands on its own unindented line, like m (pilot log).
2. **pi / mi / nb** (Addendum 1): the base pages' prose-paragraph furniture — `pi` and
   `nb` are prose chunks handled as `p`; `mi` is `m`'s indented sibling, normalized to
   `m`. Under this ruling Jeremiah 29 and 32 resolved PAGE-PROSE and Jeremiah 33 RESTORED.

## The Psalms concurrency incident (coordinator's design error; healed and guarded)

Waves A1/A2 wrote the same two Psalms reader files concurrently; interleaved whole-file
splices transiently reverted six chapters (38, 63, 65, 125, 142, 148) to flat prose.
Both workers' verifications caught their halves; idempotent re-runs healed all six; the
coordinator's subsequent full-book double verification is clean, and the editions were
transplanted only after that proof. Addendum 2 records it.

## STOPPED — three questions for the desk (nothing written for these four chapters)

1. **Acts 8 and Acts 15 — the base-only verse.** The staged chapters omit Acts 8:37 and
   Acts 15:34, verses the WEB Classic base carries (both famous textual variants the
   draft set aside). The verse-set assertion stops both chapters, though their divisions
   are clean (Acts 8: 2 q / 4 q2 at vv. 32–33; Acts 15: 6 q, matching its apparatus).
   Question: may a base-only verse be treated as outside the staged text, restoring the
   divisions of the verses the staged text carries? Coordinator's recommendation: yes —
   no word is added or removed; the omission stands as the drafters left it.
2. **Isaiah 44 — the single boundary inside a conversion.** One split in v. 19 falls
   inside the span where the base's "an abomination? Shall" became the staged "a
   detestable thing? Will"; token alignment cannot place it mechanically, though its
   sense-placement is plain. Question: may this one boundary be placed by sense?
   Coordinator's recommendation: yes, narrowly (Addendum 1, §3).
3. **Habakkuk 3 — the colophon.** The base page carries "For the music director, on my
   stringed instruments." as a prose block after v. 19; the staged text carries it as a
   standalone paragraph; the parser assigns the block to the verse, failing the
   standalone assertion. Question: may a chapter-final prose block that equals a staged
   standalone paragraph word for word be matched as that standalone? Coordinator's
   recommendation: yes (Addendum 2, §2).

If the desk rules yes on any of these, the affected chapters restore mechanically under
the same assertions, and this report can be closed by addendum.
