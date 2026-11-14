# Verification Record — Clear English Bible, Ge'ez Edition (built 2026-11-14)

Status of the edition: DRAFT — NOT REVIEWED. Publication gate: a named human reader of Ge'ez; seat empty; unmet. This record accompanies the edition's shelf deposit in `editions/geez/` of the Clear English Bible repository. It certifies the checks below and nothing more.

## The base text (his 73)

- Base file: `editions/catholic/clear-english-bible-catholic-edition.txt`, SHA-256 `dd1cc76282229befcdf8ef6ad352f42c91f5dc9d7442bbea75aa9579529fdef3`, 4,817,063 bytes. The base file was not modified.
- The base splits into exactly 73 book blocks at its own book headers; re-concatenation of the blocks with the base's front matter reproduces the base file byte-for-byte.
- In the assembled Ge'ez Edition, every one of the 73 blocks was verified present byte-identical (compared after normalizing only the single newline that joins parts). Two books stand divided, with both parts verified present and the parts' concatenation verified equal to the original block: Proverbs (divided at its chapter 25 heading into Messale, chs. 1–24, and Tagsas, chs. 25–31) and Baruch (divided at its chapter 6 heading; Baruch chs. 1–5, then the Letter of Jeremiah standing as its own book after Lamentations).

## The additions (built 2026-11-14)

Each unit was built by a separate builder from its named public-domain control, spot-checked at assembly (chapter/canon counts and first/last lines against the control, as reported by the builders and re-counted in the assembled file where headings allow).

| Unit | Control | Extent verified |
|---|---|---|
| Jubilees | Charles 1902 (SPCK 1917), from the Ethiopic; archive.org `bookofjubileesor01char` | 50 of 50 chapters; 1,307 verses; per-chapter counts match the control; first verse (1:1) and last (50:13) checked in the assembled file. Verse text taken from a clean transcription of the same 1917 edition and checked against the archive.org djvu control of record; damaged verse markers repaired from the djvu. |
| Enoch | Robert Tilford's own finished Enoch (2026-11-07), from Charles 1912 (Ethiopic) | 108 of 108 chapters; body byte-identical to his book's reader text (`~/workspace/enoch/enoch-reader.txt`, lines from "Chapter 1" to end; body SHA-256 `b0c6d7efb927b40b1959354d40ad9cd091a0db96fb017e60e904030920f12307`). |
| Ezra Sutu'el (4 Ezra) | Box 1917 (SPCK), from the Syriac with the Ethiopic among versions collated; archive.org `theapocalypseofe00unknuoft`. Control of record Laurence 1820 (Ethiopic line) not obtainable as text in this run — stated on the book's face | 12 of 12 chapters (3–14); verse counts per chapter match the control (36, 52, 56, 59, 140, 63, 47, 60, 46, 51, 58, 50); no material from chs. 1–2 or 15–16; control's numbering gaps marked in place. |
| The Ethiopic Didascalia | Harden 1920 (SPCK), from the Ge'ez; archive.org `cu31924096083336` | 43 of 43 chapters (heading count verified); first and last lines checked. The control's scan is defective in places; restored spans are bracketed in the text and were rebuilt from the raw control; [vii., 13.] is absent from Harden as printed and nothing was invented for it. |
| Te'ezaz (Sinodos II) | Horner 1904, Ethiopic line; archive.org `statutesapostle00unkngoog` | Built entire: 73 statute entries (Horner's numbers 1–72 with his repeated 40) + 13 concluding prayers. Ethiopian lists count this book at 71 canons — a numbering difference, recorded in the collation printed in the unit. |
| The Second Book of the Covenant | James 1924, pp. 485–503 (witness-eclectic: Coptic, Ethiopic, Latin); archive.org `apocryphalnewtes0000mont_v2n2` | James's sections 1–51 entire (count verified programmatically), plus the labelled prefixed-prophecy fragment he prints. Partial control, stated on the book's face. |
| 3 Ezra | Brenton 1851 (Greek line); archive.org `septuagint-with-apocrypha-the` | 9 of 9 chapters; 448 verses; per-chapter counts match Brenton (58, 30, 24, 63, 73, 34, 15, 96, 55). |
| The Prayer of Manasseh | Brenton 1851 (Greek line) | 15 of 15 verses. |
| Psalm 151 | Brenton 1851 (Greek line) | 7 of 7 verses, with Brenton's superscription. |

## The collation that changed the Sinodos (2026-11-14)

Horner 1904 was collated against the four Ethiopian books of the Sinodos before building. Finding: his Ethiopic translation prints one continuous Statutes series and covers Te'ezaz only. Ser'ata Seyon (30 canons), Gessew (56), and Abtelis (81) have no Ethiopic text in Horner and stand outstanding. This corrects the foundation dossier's §3 expectation that Horner serves Ser'ata Seyon and Te'ezaz; the correction is recorded here and on the units' faces. The dossier itself should receive a dated addendum noting it.

## Outstanding seats (10), carried as naming pages only

1, 2, and 3 Meqabyan; 4 Baruch; Ser'ata Seyon; Gessew; Abtelis; the First Book of the Covenant; Ethiopic Clement; Josippon (Ethiopic form). Reasons are printed on each seat's page and in the edition's front matter. No text was built, borrowed, or invented for any of them. The in-copyright Meqabyan translations (2005/2008; 2018/2023) and the Creative Commons 3 Meqabyan were not used.

## The count

- Church's grouped count: 81 (46 OT + 35 NT), per the Fetha Nagast.
- Itemised: 90 volumes (54 OT seats + 27 NT + 9 church-order/broader seats).
- This edition: text present for 80 of the 90; 10 outstanding. Additionally carried: the Prayer of Manasseh and Psalm 151 within their Ethiopian seats, and 1–2 Maccabees from the Catholic edition (not seated in the traditional Ethiopian lists; variance disclosed in the front matter).
- Assembled file: `clear-english-bible-geez-edition.txt` — 6,027,396 bytes, SHA-256 `364e8c71e38ac81ee85e38190e50087db07f58a7c9a7c27dbdbe72c478ade4f4` (as assembled locally; the deposited copy is verified against this hash after push).

## What this record does not certify

Fidelity of any addition to the Ge'ez. The desk cannot read Ge'ez; the additions are modernizations of their named English controls, and the human Ge'ez review gate stands unmet. OCR-damaged controls (Charles, Harden, Horner, James djvu texts) were repaired only against the controls themselves or a same-edition transcription, as each builder reported; residual scan-defect spots are marked in the units where the builders found them.
