# FIX PASS — SURFACE CENSUS (first deliverable, before any text change)

Date: 2026-10-18. Authority: FIX-PASS-BRIEF-2026-10-18.md; RULINGS-GIVEN-2026-10-18.md.
All work is in the staging tree `fix-pass/staging/` (a copy of `books/`, `individual-books/`, `editions/`). The live shelf is untouched.

## Method and surface model

Every verse below was extracted from the staged `books/` reader by a parser (chapter-heading + numbered-verse paragraphs), then located on every other staged surface by whitespace-normalized substring search. Extraction succeeded for **185 of 185 enumerated places** (Lanes A, D, E, G, F-members, F-candidates), with **zero extraction failures**. A verse's surfaces are some of five: `books/<BOOK>-reader.txt` (all 73 books), `individual-books/<BOOK>-reader.txt` (the 66-book Protestant set), `editions/catholic` (73 books), `editions/protestant` (66 books), `editions/hebrew` (the 39-book Hebrew-canon volume). In the tables, surfaces are abbreviated: books / indiv / catholic / protestant / hebrew.

Verification on samples (brief requirement): (1) 1 Peter 3:20 was read directly in all four of its staged surfaces by independent grep — the draft's "eight people" stands in `books/1-PETER-reader.txt` line 149 and in both editions, and "eight souls" stands nowhere yet, as expected before the fix. (2) For every Lane A place, the raw verse paragraph in the `books/` reader was compared byte-for-byte against each edition surface: **all identical**, so exact-paragraph replacement is the safe change mechanism for Lane A. (3) Sample extracted texts were read against the packet's descriptions and matched (Numbers 8:25–26 "must" side; Nehemiah 10:38 both "must" instances; Job 10:6 and Nehemiah 9:2 doubled "sin"; Jonah 1:11 and Acts 2:37 drafted "shall"; Song of Songs 8:8 drafted "must"). (4) Deuterocanonical places (Judith, Tobit, Sirach, Maccabees) correctly show only books + catholic surfaces; New Testament places correctly show no hebrew surface.

## Lane A — exact conversions (Ruling 12; Ruling 3)

Change plan: at each place, replace the verse paragraph on every surface with the converted paragraph ("must" → "will" at every standing-duty instance in the named verse; 1 Peter 3:20 "eight people" → "eight souls"). Log before/after per surface in `logs/lane-a-log.md`.

| Place | Drafted text (books reader) | Surfaces |
|---|---|---|
| 1 Peter 3:20 | who before were disobedient when God waited patiently in the days of Noah while the ship was being built. In it, few, that is, eight people, were saved through water. | books, indiv, catholic, protestant |
| Numbers 8:25 | and from the age of fifty years they must retire from doing the work, and must serve no more, | books, indiv, catholic, protestant, hebrew |
| Numbers 8:26 | but must assist their brothers in the Tent of Meeting, to perform the duty, and must perform no service. This is how you must have the Levites do their duties.” | books, indiv, catholic, protestant, hebrew |
| 2 Chronicles 19:9 | He commanded them, saying, “You must do this in the fear of Yahweh, faithfully, and with a perfect heart. | books, indiv, catholic, protestant, hebrew |
| 2 Chronicles 19:11 | See, Amariah the chief priest is over you in all matters of Yahweh; and Zebadiah the son of Ishmael, the ruler of the house of Judah, in all the king’s matters. Also the Levites must be officers before you. Deal courageously, and may Yahweh be with the good.” | books, indiv, catholic, protestant, hebrew |
| 2 Chronicles 23:4 | This is the thing that you must do: a third part of you, who come in on the Sabbath, of the priests and of the Levites, must be gatekeepers of the thresholds. | books, indiv, catholic, protestant, hebrew |
| 2 Chronicles 23:5 | A third part must be at the king’s house; and a third part at the gate of the foundation. All the people will be in the courts of Yahweh’s house. | books, indiv, catholic, protestant, hebrew |
| 2 Chronicles 23:6 | But let no one come into Yahweh’s house except the priests and those who minister of the Levites. They must come in, for they are holy, but all the people must follow Yahweh’s instructions. | books, indiv, catholic, protestant, hebrew |
| 2 Chronicles 23:7 | The Levites must surround the king, every man with his weapons in his hand. Whoever comes into the house, let him be slain. Be with the king when he comes in and when he goes out.” | books, indiv, catholic, protestant, hebrew |
| Nehemiah 10:38 | The priest, the descendent of Aaron, must be with the Levites when the Levites take tithes. The Levites must bring up the tithe of the tithes to the house of our God, to the rooms, into the treasure house. | books, indiv, catholic, protestant, hebrew |
| Nehemiah 10:39 | For the children of Israel and the children of Levi must bring the wave offering of the grain, of the new wine, and of the oil, to the rooms where the vessels of the sanctuary are, and the priests who minister, with the gatekeepers and the singers. We will not forsake the house of our God. | books, indiv, catholic, protestant, hebrew |
| Ezra 6:8 | Moreover I make a decree regarding what you must do for these elders of the Jews for the building of this house of God: that of the king’s goods, even of the tribute beyond the River, expenses must be given with all diligence to these men, that they not be hindered. | books, indiv, catholic, protestant, hebrew |

Instance count: 18 "must" instances across the ten Ruling 12 verses (Num 8:25 ×2; 8:26 ×3; 2 Chr 19:9 ×1; 19:11 ×1; 23:4 ×2; 23:5 ×1; 23:6 ×2; 23:7 ×1; Neh 10:38 ×2; 10:39 ×1; Ezra 6:8 ×2), plus the single 1 Peter 3:20 restoration.

## Lane B — Song of Songs speaker headings (Ruling 18)

Surfaces carrying the Song: books/SONGOFSONGS-reader.txt, individual-books/SONGOFSONGS-reader.txt, editions/catholic, editions/protestant, editions/hebrew — all five (the Song stands in the 66-book set and in the Hebrew canon volume; confirmed by the census surface search at Song of Songs 8:8, which returned all five). CORRECTION, entered by the coordinator during Lane B: the first version of this paragraph omitted editions/protestant, and Lane B's first applications followed it; the omission was caught in verification against the census data, the protestant edition was then applied and verified like the others, and all five surfaces now carry the headings. The error and its cure are recorded here and in logs/lane-b-log.md and logs/lane-b-report.md. The 33 headings, their words and exact positions, are recorded in the pinned base snapshots (`goals/clear-english-bible-translation/hidden_files/songofsongs-0N-web-base-snapshot-2026-10-16.txt`), whose per-chapter heading lines were verified against the completion report's counts (ch. 1: 9; ch. 2: 5; ch. 3: 0; ch. 4: 2; ch. 5: 5; ch. 6: 5; ch. 7: 1; ch. 8: 6 = 33). Extracted heading records:

- **Chapter 1:** Speaker headings on the base page (page furniture, not verse text; not carried into the draft): Beloved (after v. 1); Friends (within v. 4, after “his rooms.”); Beloved (within v. 4, after “more than wine!”); Lover (before v. 8); Friends (before v. 11); Beloved (before v. 12); Lover (before v. 15); Beloved (before v. 16); Lover (before v. 17)
- **Chapter 2:** Speaker headings on the base page (page furniture, not verse text; not carried into the draft): Beloved (before v. 1); Lover (before v. 2); Beloved (before v. 3); Lover (before v. 14); Beloved (before v. 16)
- **Chapter 3:** Speaker headings on the base page: none in this chapter.
- **Chapter 4:** Speaker headings on the base page (page furniture, not verse text; not carried into the draft): Lover (before v. 1); Beloved (before v. 16)
- **Chapter 5:** Speaker headings on the base page (page furniture, not verse text; not carried into the draft): Lover (before v. 1); Friends (within v. 1, after “with my milk.”); Beloved (within v. 1, after “beloved.” (i.e., before v. 2)); Friends (before v. 9); Beloved (before v. 10)
- **Chapter 6:** Speaker headings on the base page (page furniture, not verse text; not carried into the draft): Friends (before v. 1); Beloved (before v. 2); Lover (before v. 4); Friends (within v. 13, after v. 12's close (“chariots.”)); Lover (within v. 13, after “that we may gaze at you.”)
- **Chapter 7:** Speaker headings on the base page (page furniture, not verse text; not carried into the draft): Beloved (within v. 10, after v. 9)
- **Chapter 8:** Speaker headings on the base page (page furniture, not verse text; not carried into the draft): Friends (before v. 5); Beloved (within v. 5, after “leaning on her beloved?”); Brothers (before v. 8); Beloved (before v. 10); Lover (before v. 13); Beloved (before v. 14)

Change plan: insert each heading on its own line at its recorded position in the staged Song reader on every surface (before-verse positions as a standalone line before the verse paragraph; after-verse positions as a standalone line after that verse's paragraph; within-verse positions at the recorded sentence boundary). No verse wording changes. Chapter 3 gets none.

## Lane C — lineation form pass (Ruling 8)

Source of record: each chapter's apparatus in `goals/clear-english-bible-translation/files/<BOOK>-<NN>-DRAFT.md` records the base's divisions in full and in order (verified on Hebrews 1: 9 q + 11 q2 + 1 m, each line quoted exactly), with the completion reports carrying the per-book presentation flags (Decision 8 sources). Surfaces per book follow the surface model above. Governed scope, per Decision 8: 1 Timothy 3:16 (6 divisions); 2 Timothy 2:11–13 (9 divisions); Hebrews chs. 1–5, 7, 8, 10, 12, 13 (88 q/q2 lines + 1 m); 1 Peter chs. 1–3 (18 divisions); Galatians 4:27; the quotation blocks at 1 Corinthians 1:19; 2:9; 15:55 (1 Cor 13 is base-prose, never relineated); 2 Corinthians' and Romans' and Acts' poetry quotation passages; John's prologue and poetry passages; Deuteronomy chs. 32–33 and the joined paragraphs of ch. 27; Revelation's song and list chapters as its chapter files record; and the book-wide presentation flags of Judges, 1 Samuel, 2 Samuel, 1 Chronicles, 2 Chronicles, 2 Kings, Nehemiah, Job, Psalms, Proverbs, Isaiah, Jeremiah, Ezekiel, Hosea, Micah, Zechariah (chs. 9–11, 13), Tobit (ch. 13), Judith, Sirach, Wisdom, Baruch, Greek Daniel, Esther (the prayers), 1 Maccabees, 2 Maccabees, Amos, Joel, Jonah, Habakkuk, Zephaniah, Ecclesiastes, Lamentations, Song of Songs. Red-letter spans riding with the pass: 1 Corinthians 11:24–25; 2 Corinthians 12:9; Revelation 21:5–8.

Change plan: per chapter, rebuild the staged reader's prose verse-paragraphs into the recorded lines (q lines flush, q2 lines indented two spaces to carry the base's q/q2 distinction, m prose-link divisions on their own line unindented), preserving every word, punctuation mark, and verse number exactly. Verification per chapter: the rebuilt chapter text, with all whitespace collapsed, must be identical to the pre-change chapter text; verse counts unchanged.

## Lane D — the six doubled "sin and sin" places (Ruling 6) — REPORT ONLY

| Place | Drafted text (books reader) | Surfaces |
|---|---|---|
| Job 10:6 | that you inquire after my sin, and search after my sin? | books, indiv, catholic, protestant, hebrew |
| Job 13:23 | How many are my sins and sins? Make me know my disobedience and my sin. | books, indiv, catholic, protestant, hebrew |
| Hosea 12:8 | Ephraim said, “Surely I have become rich. I have found myself wealth. In all my wealth they won’t find in me any sin that is sin.” | books, indiv, catholic, protestant, hebrew |
| Jeremiah 16:10 | It will happen, when you tell this people all these words, and they ask you, ‘Why has Yahweh pronounced all this great evil against us?’ or ‘What is our sin?’ or ‘What is our sin that we have committed against Yahweh our God?’ | books, indiv, catholic, protestant, hebrew |
| Jeremiah 36:3 | It may be that the house of Judah will hear all the evil which I intend to do to them, that they may each return from his evil way; that I may forgive their sin and their sin.” | books, indiv, catholic, protestant, hebrew |
| Nehemiah 9:2 | The offspring of Israel separated themselves from all foreigners and stood and confessed their sins and the sins of their fathers. | books, indiv, catholic, protestant, hebrew |

No text changes in this lane. Output: `DOUBLED-AUDIT.md` with per-place source wording, justification analysis, erased-distinction analysis, and a recommended disposition for the editor.

## Lane E — challengeable grounds (Ruling 5, sharpening two) — DOCUMENTATION ONLY

| Place | Drafted text (books reader) | Surfaces |
|---|---|---|
| Judith 7:27 | For it is better for us to be captured by them. For we will be servants, and our souls will live, and we will not see the death of our babies before our eyes, and our wives and our children fainting in death. | books, catholic |
| Revelation 18:13 | and cinnamon, incense, perfume, frankincense, wine, olive oil, fine flour, wheat, cattle, sheep, horses, chariots, and people’s bodies and souls. | books, indiv, catholic, protestant |
| Revelation 18:14 | The fruits which your soul lusted after have been lost to you. All things that were dainty and sumptuous have perished from you, and you will find them no more at all. | books, indiv, catholic, protestant |

Grounds are drafted from the books' own audit records (JUDITH-COMPLETION-REPORT.md flag 1; REVELATION-COMPLETION-REPORT.md and the Revelation 18 chapter draft/audit record). No text changes in this lane.

## Lane F — per-context review, deliberative "shall" (Rulings 1 + 2)

Change plan: work book by book from the completion reports (packet Decision 1/2 source flags). Judge each place against Ruling 1's force-principles (obligation → "should"; open course/intention → "will"; solemn/formal deliberation or base-precedent weight → "shall"; prescribed duty → "must"). Drafted forms stand unless a place fails its context test; candidate places are judged with their built-in answers as one unit. Every adjustment logged with its ground; every stand counted. Record-only places (Psalm 116:12; 2 Kings 20:9; Esther 6:6) are unaffected.

### Members (Decision 1)

| Place | Drafted verse (excerpt) | Surfaces |
|---|---|---|
| Ruth 3:1 | Naomi her mother-in-law said to her, “My daughter, will I not seek rest for you, that it may be well with you? | books, indiv, catholic, protestant, hebrew |
| Joshua 7:8 | Oh, Lord, what will I say, after Israel has turned their backs before their enemies? | books, indiv, catholic, protestant, hebrew |
| Judges 13:12 | Manoah said, “Now let your words happen. What must the child’s way of life and mission be?” | books, indiv, catholic, protestant, hebrew |
| Judges 20:18 | The children of Israel arose, went up to Bethel, and asked counsel of God. They asked, “Who will go up for us first to battle agai | books, indiv, catholic, protestant, hebrew |
| Judges 20:23 | The children of Israel went up and wept before Yahweh until evening; and they asked of Yahweh, saying, “Will I again draw near to  | books, indiv, catholic, protestant, hebrew |
| Judges 20:28 | and Phinehas, the son of Eleazar, the son of Aaron, stood before it in those days), saying, “Will I yet again go out to battle aga | books, indiv, catholic, protestant, hebrew |
| Ezra 9:10 | “Now, our God, what will we say after this? For we have forsaken your commandments, | books, indiv, catholic, protestant, hebrew |
| Genesis 30:31 | Laban said, "What shall I give you?" Jacob said, "You shall not give me anything. If you will do this thing for me, I will again f | books, indiv, catholic, protestant, hebrew |
| Exodus 2:7 | Then his sister said to Pharaoh's daughter, "Shall I go and call a nurse for you from the Hebrew women, so that she may nurse the  | books, indiv, catholic, protestant, hebrew |
| Exodus 17:4 | Moses cried to Yahweh, saying, “What shall I do with these people? They are almost ready to stone me.” | books, indiv, catholic, protestant, hebrew |
| 1 Samuel 5:8 | They sent therefore and gathered together all the lords of the Philistines, and said, “What must we do with the ark of the God of  | books, indiv, catholic, protestant, hebrew |
| 1 Samuel 6:2 | The Philistines called for the priests and the diviners, saying, “What must we do with Yahweh’s ark? Show us how we should send it | books, indiv, catholic, protestant, hebrew |
| 1 Samuel 10:2 | When you have departed from me today, then you will find two men by Rachel’s tomb, on the border of Benjamin at Zelzah. They will  | books, indiv, catholic, protestant, hebrew |
| 1 Samuel 14:37 | Saul asked counsel of God: “Will I go down after the Philistines? Will you deliver them into the hand of Israel?” But he didn’t an | books, indiv, catholic, protestant, hebrew |
| 1 Samuel 14:45 | The people said to Saul, “Will Jonathan die, who has worked this great salvation in Israel? Far from it! As Yahweh lives, there wi | books, indiv, catholic, protestant, hebrew |
| 1 Samuel 23:2 | Therefore David inquired of Yahweh, saying, “Will I go and strike these Philistines?” Yahweh said to David, “Go strike the Philist | books, indiv, catholic, protestant, hebrew |
| 1 Samuel 25:11 | Will I then take my bread, my water, and my meat that I have killed for my shearers, and give it to men who I don’t know where the | books, indiv, catholic, protestant, hebrew |
| 1 Samuel 28:11 | Then the woman said, “Whom will I bring up to you?” He said, “Bring Samuel up for me.” | books, indiv, catholic, protestant, hebrew |
| 1 Samuel 28:15 | Samuel said to Saul, “Why have you disturbed me, to bring me up?” Saul answered, “I am very distressed; for the Philistines make w | books, indiv, catholic, protestant, hebrew |
| 2 Samuel 2:1 | After this, David inquired of Yahweh, saying, “Will I go up into any of the cities of Judah?” Yahweh said to him, “Go up.” David s | books, indiv, catholic, protestant, hebrew |
| 2 Samuel 5:19 | David inquired of Yahweh, saying, “Will I go up against the Philistines? Will you deliver them into my hand?” Yahweh said to David | books, indiv, catholic, protestant, hebrew |
| 2 Samuel 11:11 | Uriah said to David, “The ark, Israel, and Judah, are staying in tents; and my lord Joab and the servants of my lord are encamped  | books, indiv, catholic, protestant, hebrew |
| 2 Samuel 16:20 | Then Absalom said to Ahithophel, “Give your counsel what we will do.” | books, indiv, catholic, protestant, hebrew |
| 2 Samuel 17:6 | When Hushai had come to Absalom, Absalom spoke to him, saying, “Ahithophel has spoken like this. Will we do what he says? If not,  | books, indiv, catholic, protestant, hebrew |
| 2 Samuel 19:22 | David said, “What have I to do with you, you sons of Zeruiah, that you should be adversaries to me today? Will any man be put to d | books, indiv, catholic, protestant, hebrew |
| 1 Kings 22:15 | When he had come to the king, the king said to him, “Micaiah, will we go to Ramoth Gilead to battle, or will we forbear?” He answe | books, indiv, catholic, protestant, hebrew |
| 2 Kings 2:9 | When they had gone over, Elijah said to Elisha, “Ask what I will do for you, before I am taken from you.” Elisha said, “Please let | books, indiv, catholic, protestant, hebrew |
| 2 Kings 3:8 | Then he said, “Which way will we go up?” Jehoram answered, “The way of the wilderness of Edom.” | books, indiv, catholic, protestant, hebrew |
| 2 Kings 6:15 | When the servant of the man of God had risen early and gone out, see, an army with horses and chariots was around the city. His se | books, indiv, catholic, protestant, hebrew |
| 2 Kings 6:21 | The king of Israel said to Elisha, when he saw them, “My father, will I strike them? Will I strike them?” | books, indiv, catholic, protestant, hebrew |
| 2 Kings 20:9 | Isaiah said, “This will be the sign to you from Yahweh, that Yahweh will do the thing that he has spoken: should the shadow go for | books, indiv, catholic, protestant, hebrew |
| 1 Chronicles 11:19 | and said, “My God forbid me, that I should do this! Should I drink the blood of these men who have put their lives in jeopardy?” F | books, indiv, catholic, protestant, hebrew |
| 1 Chronicles 14:10 | David inquired of God, saying, “Will I go up against the Philistines? Will you deliver them into my hand?” Yahweh said to him, “Go | books, indiv, catholic, protestant, hebrew |
| 2 Chronicles 18:5 | Then the king of Israel gathered the prophets together, four hundred men, and said to them, “Will we go to Ramoth Gilead to battle | books, indiv, catholic, protestant, hebrew |
| 2 Chronicles 18:14 | When he had come to the king, the king said to him, “Micaiah, will we go to Ramoth Gilead to battle, or will I forbear?” He said,  | books, indiv, catholic, protestant, hebrew |
| 2 Chronicles 25:9 | Amaziah said to the man of God, “But what will we do for the hundred talents which I have given to the army of Israel?” The man of | books, indiv, catholic, protestant, hebrew |
| Tobit 5:14 | But tell me, what wages will I give you? A drachma a day, and those things that be necessary for you, as to my son? | books, catholic |
| Judith 12:12 | For see, it would be a disgrace if we shall let such a woman go, not having had her company; for if we don’t draw her to ourselves | books, catholic |
| Esther 6:6 | The king said to Haman, “What should I do for the man whom I wish to honor?” Haman said within himself, “Whom would the king honor | books, indiv, catholic, protestant, hebrew |
| Job 2:10 | But he said to her, “You speak as one of the foolish women would speak. What? Should we receive good at the hand of God, and shoul | books, indiv, catholic, protestant, hebrew |
| Job 32:16 | Should I wait, because they don’t speak, because they stand still, and answer no more? | books, indiv, catholic, protestant, hebrew |
| Psalms 116:12 | What will I give to Yahweh for all his benefits toward me? | books, indiv, catholic, protestant, hebrew |
| Isaiah 6:8 | I heard the Lord’s voice, saying, “Whom will I send, and who will go for us?” Then I said, “Here I am. Send me!” | books, indiv, catholic, protestant, hebrew |
| Hosea 6:4 | “Ephraim, what shall I do to you? Judah, what shall I do to you? For your love is like a morning cloud, and like the dew that disa | books, indiv, catholic, protestant, hebrew |
| Micah 6:6 | How shall I come before Yahweh, and bow myself before the exalted God? Shall I come before him with burnt offerings, with calves a | books, indiv, catholic, protestant, hebrew |
| Micah 6:7 | Will Yahweh be pleased with thousands of rams? With tens of thousands of rivers of oil? Shall I give my firstborn for my disobedie | books, indiv, catholic, protestant, hebrew |
| Jonah 1:11 | Then they said to him, “What shall we do to you, that the sea may be calm to us?” For the sea grew more and more stormy. | books, indiv, catholic, protestant, hebrew |
| Song of Songs 8:8 | We have a little sister. She has no breasts. What must we do for our sister in the day when she is to be spoken for? | books, indiv, catholic, protestant, hebrew |
| Sirach 24:7 | With all these I sought rest. In whose inheritance will I lodge? | books, catholic |
| 1 Maccabees 14:25 | But when the people heard these things, they said, “What thanks shall we give to Simon and his sons? | books, catholic |
| Acts 2:37 | Now when they heard this, they were cut to the heart, and said to Peter and the rest of the apostles, “Brothers, what shall we do? | books, indiv, catholic, protestant |
| Acts 22:10 | I said, ‘What shall I do, Lord?’ The Lord said to me, ‘Arise, and go into Damascus. There you will be told about all things which  | books, indiv, catholic, protestant |
| 1 Corinthians 4:21 | What do you want? Shall I come to you with a rod, or in love and a spirit of gentleness? | books, indiv, catholic, protestant |
| Matthew 18:21 | Then Peter came and said to him, “Lord, how often shall my brother sin against me, and I forgive him? Until seven times?” | books, indiv, catholic, protestant |
| Matthew 19:16 | See, one came to him and said, “Good teacher, what good thing shall I do, that I may have eternal life?” | books, indiv, catholic, protestant |
| Matthew 27:22 | Pilate said to them, “What then shall I do to Jesus who is called Christ?” They all said to him, “Let him be crucified!” | books, indiv, catholic, protestant |
| Mark 6:24 | She went out and said to her mother, “What shall I ask?” She said, “The head of John the Baptizer.” | books, indiv, catholic, protestant |
| Mark 10:17 | As he was going out into the way, one ran to him, knelt before him, and asked him, “Good Teacher, what shall I do that I may inher | books, indiv, catholic, protestant |
| Mark 15:12 | Pilate again asked them, “What then should I do to him whom you call the King of the Jews?” | books, indiv, catholic, protestant |
| Luke 10:25 | See, a certain lawyer stood up and tested him, saying, “Teacher, what shall I do to inherit eternal life?” | books, indiv, catholic, protestant |
| Luke 18:18 | A certain ruler asked him, saying, “Good Teacher, what shall I do to inherit eternal life?” | books, indiv, catholic, protestant |
| Luke 20:13 | The lord of the vineyard said, ‘What shall I do? I will send my beloved son. It may be that seeing him, they will respect him.’ | books, indiv, catholic, protestant |
| John 19:15 | They cried out, “Away with him! Away with him! Crucify him!” Pilate said to them, “Shall I crucify your King?” The chief priests a | books, indiv, catholic, protestant |

### Candidates (Decision 2)

| Place | Drafted verse (excerpt) | Surfaces |
|---|---|---|
| Romans 6:1 | What shall we say then? Shall we continue in sin, that grace may abound? | books, indiv, catholic, protestant |
| Romans 6:15 | What then? Shall we sin because we are not under law but under grace? May it never be! | books, indiv, catholic, protestant |
| Romans 7:7 | What shall we say then? Is the law sin? May it never be! However, I wouldn’t have known sin except through the law. For I wouldn’t | books, indiv, catholic, protestant |
| Romans 8:31 | What then shall we say about these things? If God is for us, who can be against us? | books, indiv, catholic, protestant |
| Romans 9:14 | What shall we say then? Is there unrighteousness with God? May it never be! | books, indiv, catholic, protestant |
| Romans 9:30 | What shall we say then? That the Gentiles, who didn’t follow after righteousness, attained to righteousness, even the righteousnes | books, indiv, catholic, protestant |
| Romans 3:5 | But if our unrighteousness commends the righteousness of God, what will we say? Is God unrighteous who inflicts wrath? I speak lik | books, indiv, catholic, protestant |
| Romans 3:31 | Do we then nullify the law through faith? May it never be! No, we establish the law. | books, indiv, catholic, protestant |
| Romans 4:1 | What then will we say that Abraham, our forefather, has found according to the flesh? | books, indiv, catholic, protestant |
| Acts 4:16 | saying, “What shall we do to these men? Because indeed a notable miracle has been done through them, as can be plainly seen by all | books, indiv, catholic, protestant |
| Acts 8:36 | As they went on the way, they came to some water; and the eunuch said, “See, here is water. What is keeping me from being baptized | books, indiv, catholic, protestant |
| Acts 21:22 | What then? The assembly must certainly meet, for they will hear that you have come. | books, indiv, catholic, protestant |
| Acts 25:9 | But Festus, desiring to gain favor with the Jews, answered Paul and said, “Are you willing to go up to Jerusalem and be judged by  | books, indiv, catholic, protestant |
| 1 Corinthians 6:15 | Don’t you know that your bodies are members of Christ? Shall I then take the members of Christ and make them members of a prostitu | books, indiv, catholic, protestant |
| 1 Corinthians 11:22 | What, don’t you have houses to eat and to drink in? Or do you despise God’s assembly and put them to shame who don’t have enough?  | books, indiv, catholic, protestant |
| 1 Corinthians 14:6 | But now, brothers, if I come to you speaking with other languages, what would I profit you unless I speak to you either by way of  | books, indiv, catholic, protestant |
| 1 Corinthians 14:15 | What should I do? I will pray with the spirit, and I will pray with the understanding also. I will sing with the spirit, and I wil | books, indiv, catholic, protestant |
| Hebrews 11:32 | What more shall I say? For the time would fail me if I told of Gideon, Barak, Samson, Jephthah, David, Samuel, and the prophets— | books, indiv, catholic, protestant |
| Hebrews 12:9 | Furthermore, we had the fathers of our flesh to chasten us, and we paid them respect. Shall we not much rather be in subjection to | books, indiv, catholic, protestant |
| James 3:13 | Who is wise and understanding among you? Let him show by his good conduct that his deeds are done in gentleness of wisdom. | books, indiv, catholic, protestant |
| James 5:13 | Is any among you suffering? Let him pray. Is any cheerful? Let him sing praises. | books, indiv, catholic, protestant |
| James 5:14 | Is any among you sick? Let him call for the elders of the assembly, and let them pray over him, anointing him with oil in the name | books, indiv, catholic, protestant |
| 2 Peter 3:11 | Therefore, since all these things will be destroyed like this, what kind of people ought you to be in holy living and godliness, | books, indiv, catholic, protestant |
| John 12:27 | “Now my soul is troubled. What shall I say? ‘Father, save me from this time’? But I came to this time for this cause. | books, indiv, catholic, protestant |
| John 13:37 | Peter said to him, “Lord, why can’t I follow you now? I will lay down my life for you.” | books, indiv, catholic, protestant |
| John 18:39 | But you have a custom that I should release someone to you at the Passover. Therefore, do you want me to release to you the King o | books, indiv, catholic, protestant |
| Matthew 11:16 | “But to what shall I compare this generation? It is like children sitting in the marketplaces, who call to their companions | books, indiv, catholic, protestant |
| Matthew 9:5 | For which is easier, to say, ‘Your sins are forgiven;’ or to say, ‘Get up, and walk’? | books, indiv, catholic, protestant |
| Matthew 26:15 | and said, “What are you willing to give me if I deliver him to you?” So they weighed out for him thirty pieces of silver. | books, indiv, catholic, protestant |
| Matthew 27:17 | When therefore they were gathered together, Pilate said to them, “Whom do you want me to release to you? Barabbas, or Jesus who is | books, indiv, catholic, protestant |
| Matthew 27:21 | But the governor answered them, “Which of the two do you want me to release to you?” They said, “Barabbas!” | books, indiv, catholic, protestant |
| Mark 6:37 | But he answered them, “You give them something to eat.” They asked him, “Shall we go and buy two hundred denarii worth of bread an | books, indiv, catholic, protestant |
| Mark 2:9 | Which is easier, to tell the paralytic, ‘Your sins are forgiven;’ or to say, ‘Arise, and take up your bed, and walk’? | books, indiv, catholic, protestant |
| Mark 15:9 | Pilate answered them, saying, “Do you want me to release to you the King of the Jews?” | books, indiv, catholic, protestant |
| Luke 9:41 | Jesus answered, “Faithless and perverse generation, how long shall I be with you and bear with you? Bring your son here.” | books, indiv, catholic, protestant |
| Luke 13:18 | He said, “What is God’s Kingdom like? To what shall I compare it? | books, indiv, catholic, protestant |
| Luke 13:20 | Again he said, “To what shall I compare God’s Kingdom? | books, indiv, catholic, protestant |
| Luke 22:49 | When those who were around him saw what was about to happen, they said to him, “Lord, shall we strike with the sword?” | books, indiv, catholic, protestant |
| Jeremiah 6:10 | To whom should I speak and testify, that they may hear? See, their ear is uncircumcised, and they can’t listen. See, Yahweh’s word | books, indiv, catholic, protestant, hebrew |
| Jeremiah 8:14 | “Why do we sit still? Assemble yourselves! Let’s enter into the fortified cities, and let’s be silent there; for Yahweh our God ha | books, indiv, catholic, protestant, hebrew |
| Jeremiah 9:7 | Therefore Yahweh of Armies says, “See, I will melt them and test them; for how should I deal with the daughter of my people? | books, indiv, catholic, protestant, hebrew |
| Jeremiah 15:2 | It will happen when they ask you, ‘Where shall we go out?’ then you must tell them, ‘Yahweh says: “Such as are for death, to death | books, indiv, catholic, protestant, hebrew |
| Isaiah 8:19 | When they tell you, “Consult with those who have familiar spirits and with the wizards, who chirp and who mutter,” shouldn’t a peo | books, indiv, catholic, protestant, hebrew |
| Isaiah 10:11 | will I not, as I have done to Samaria and her idols, so do to Jerusalem and her idols? | books, indiv, catholic, protestant, hebrew |
| Isaiah 20:6 | The inhabitants of this coast land will say in that day, ‘See, this is our expectation, where we fled for help to be delivered fro | books, indiv, catholic, protestant, hebrew |
| Isaiah 38:15 | What will I say? He has both spoken to me, and himself has done it. I will walk carefully all my years because of the anguish of m | books, indiv, catholic, protestant, hebrew |
| Isaiah 40:6 | The voice of one saying, “Cry out!” One said, “What shall I cry?” “All flesh is like grass, and all its glory is like the flower o | books, indiv, catholic, protestant, hebrew |
| Isaiah 44:19 | No one thinks, neither is there knowledge nor understanding to say, “I have burned part of it in the fire. Yes, I have also baked  | books, indiv, catholic, protestant, hebrew |
| Isaiah 51:19 | These two things have happened to you— who will grieve with you?— desolation and destruction, and famine and the sword. How can I  | books, indiv, catholic, protestant, hebrew |
| Isaiah 52:5 | “Now therefore, what do I do here,” says Yahweh, “seeing that my people are taken away for nothing? Those who rule over them mock, | books, indiv, catholic, protestant, hebrew |
| Isaiah 57:6 | Among the smooth stones of the valley is your portion. They, they are your lot. You have even poured a drink offering to them. You | books, indiv, catholic, protestant, hebrew |
| Isaiah 66:9 | Will I bring to the birth, and not cause to be delivered?” says Yahweh. “Will I who cause to give birth shut the womb?” says your  | books, indiv, catholic, protestant, hebrew |
| Lamentations 2:13 | What shall I testify to you? What shall I liken to you, daughter of Jerusalem? What shall I compare to you, that I may comfort you | books, indiv, catholic, protestant, hebrew |
| Malachi 3:7 | From the days of your fathers you have turned away from my rules and have not kept them. Return to me, and I will return to you,”  | books, indiv, catholic, protestant, hebrew |
| Zechariah 7:3 | and to speak to the priests of the house of Yahweh of Armies and to the prophets, saying, “Should I weep in the fifth month, separ | books, indiv, catholic, protestant, hebrew |
| Sirach 14:15 | Won’t you leave your labors to another, and your toils be divided by lot? | books, catholic |
| Sirach 49:11 | How will we magnify Zerubbabel? He was like a signet ring on the right hand. | books, catholic |
| Proverbs 22:27 | If you don’t have means to pay, why should he take away your bed from under you? | books, indiv, catholic, protestant, hebrew |
| 1 Maccabees 3:17 | But when they saw the army coming to meet them, they said to Judas, “What? Shall we be able, being a small company, to fight again | books, catholic |

## Lane G — soul candidates under the two-trigger rule (Ruling 11)

Change plan: judge each place trigger by trigger (Trigger 1: an outcome — saving, destruction, death, deliverance, or the like — predicated of the soul itself → "soul" stands; Trigger 2: mere headcount tally → "people"). Every candidate already stands in the base's word, so a Trigger 1 judgment confirms the place with no text change; a Trigger 2 judgment would change "soul" to "people" on every surface. Clean answers settle the place; genuinely borderline places are HELD and reported, never forced.

| Place | Drafted text (books reader) | Surfaces |
|---|---|---|
| Ezekiel 3:19 | Yet if you warn the wicked, and he doesn’t turn from his wickedness, nor from his wicked way, he will die in his sin; but you have delivered your soul | books, indiv, catholic, protestant, hebrew |
| Ezekiel 3:21 | Nevertheless if you warn the righteous man, that the righteous not sin, and he does not sin, he will surely live, because he took warning; and you hav | books, indiv, catholic, protestant, hebrew |
| Ezekiel 13:18 | and say, “The Lord Yahweh says: ‘Woe to the women who sew magic bands on all elbows and make veils for the head of persons of every stature to hunt so | books, indiv, catholic, protestant, hebrew |
| Ezekiel 13:20 | “Therefore the Lord Yahweh says: ‘See, I am against your magic bands, with which you hunt the souls to make them fly, and I will tear them from your a | books, indiv, catholic, protestant, hebrew |
| Ezekiel 14:14 | though these three men, Noah, Daniel, and Job, were in it, they would deliver only their own souls by their righteousness,” says the Lord Yahweh. | books, indiv, catholic, protestant, hebrew |
| Ezekiel 14:20 | though Noah, Daniel, and Job, were in it, as I live,” says the Lord Yahweh, “they would deliver neither son nor daughter; they would deliver only thei | books, indiv, catholic, protestant, hebrew |
| Ezekiel 18:4 | See, all souls are mine; as the soul of the father, so also the soul of the son is mine. The soul who sins, he will die. | books, indiv, catholic, protestant, hebrew |
| Ezekiel 18:20 | The soul who sins, he will die. The son will not bear the sin of the father, neither will the father bear the sin of the son. The righteousness of the | books, indiv, catholic, protestant, hebrew |
| Ezekiel 18:27 | Again, when the wicked man turns away from his wickedness that he has committed, and does that which is lawful and right, he will save his soul alive. | books, indiv, catholic, protestant, hebrew |
| Ezekiel 33:5 | He heard the sound of the trumpet and didn’t take warning. His blood will be on him; whereas if he had heeded the warning, he would have delivered his | books, indiv, catholic, protestant, hebrew |
| Ezekiel 33:9 | Nevertheless, if you warn the wicked of his way to turn from it, and he doesn’t turn from his way; he will die in his sin, but you have delivered your | books, indiv, catholic, protestant, hebrew |
| Isaiah 3:9 | The look of their faces testify against them. They parade their sin like Sodom. They don’t hide it. Woe to their soul! For they have brought disaster  | books, indiv, catholic, protestant, hebrew |
| Sirach 6:2 | Don’t exalt yourself in the counsel of your soul, that your soul not be torn in pieces like a bull. | books, catholic |
| Matthew 10:28 | Don’t be afraid of those who kill the body, but are not able to kill the soul. Rather, fear him who is able to destroy both soul and body in Gehenna. | books, indiv, catholic, protestant |
| Matthew 26:38 | Then Jesus said to them, “My soul is exceedingly sorrowful, even to death. Stay here and watch with me.” | books, indiv, catholic, protestant |
| Mark 14:34 | He said to them, “My soul is exceedingly sorrowful, even to death. Stay here and watch.” | books, indiv, catholic, protestant |
| Leviticus 22:3 | “Tell them, ‘If anyone of all your offspring throughout your generations approaches the holy things which the children of Israel make holy to Yahweh,  | books, indiv, catholic, protestant, hebrew |
| Lamentations 2:12 | They ask their mothers, “Where is grain and wine?” when they swoon as the wounded in the streets of the city, when their soul is poured out into their | books, indiv, catholic, protestant, hebrew |
| Hebrews 4:12 | For the word of God is living and active, and sharper than any two-edged sword, piercing even to the dividing of soul and spirit, of both joints and m | books, indiv, catholic, protestant |
| Hebrews 6:19 | This hope we have as an anchor of the soul, a hope both sure and steadfast and entering into that which is within the veil, | books, indiv, catholic, protestant |
| Hebrews 10:38 | But the righteous one will live by faith. If he shrinks back, my soul has no pleasure in him.” | books, indiv, catholic, protestant |

Ezekiel 13:18 and 13:20 each carry additional candidate occurrences beside the verse's member occurrence (Decision 4), and Matthew 10:28 carries two instances; instance-level treatment is recorded in the lane log.

*Census ends. Raw extraction data: `census-raw.json`; builder: `census_build.py`.*
