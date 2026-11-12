# Audit of the website English and site structure (Issue #19)

Date: 2026-11-12. Scope: English grammar, spelling, punctuation and clarity, plus site defects (links, nav, headings, raw HTML, stray files), in the 90 in-scope `.md` files under `docs/`. Review only; no file in `docs/`, `mkdocs.yaml` or `scripts/` was edited.

**Excluded** (comment on issue #19 and owner decision): `docs/6-pali-class/bhikkhu-patimokkha/`, `docs/6-pali-class/sbs-per-analysis/`, `docs/6-pali-class/suttas/` (already audited in `kamma/audit/*-audit/`), `docs/6-pali-class/advanced/` (unpublished draft), and `docs/6-pali-class/draft-advanced-pali-course.md` (still being edited).

**Evidence** (git-ignored, in `temp/site-audit/`): `files.txt` (the 90 files), `languagetool.tsv` (689 rows), `build.log` (build succeeds, 0 warnings), `find_unseparated_lists.py` and `check_links.py` (the scripts behind findings 70 and 71), `suspect-urls-status.txt` (HTTP status of 55 release-download and DPD links), `triage.tsv` (a disposition for every LanguageTool row).

## How to use this report

- **Delete every finding you reject.** Every finding left in this file counts as approved and will be applied. You can edit the **Proposed** text of a finding you keep; the edited text is what gets applied.
- Findings marked **⚠ data/URL** delete content, rename a published page, or change a URL. Approve them only on purpose.
- Findings marked **Pāḷi** change the spelling of a Pāḷi word. Everything else leaves Pāḷi text unchanged.
- **Generated files.** `docs/index.md`, `docs/4-dictionaries/index.md`, `docs/5-anki/index.md` and `docs/6-pali-class/index.md` are rebuilt from the `.header.md` file in the same folder by `scripts/generate_indexes.py`, and the `mkdocs.yaml` nav is rebuilt from first headings by `scripts/generate_mkdocs_yaml.py` (both run in `scripts/web_preprocessing.sh`). Findings name the source file (`.header.md` or the page's first heading); the generated copies change when preprocessing runs.
- Line numbers are from the files as of commit `519a7ca` plus this thread's uncommitted changes (none in `docs/`).

## Coverage

All 90 files were read. "Full" means every line was read; "prose only" means the page is a code listing (an Anki template or field list) and only the text outside the code block was checked.

| Folder | Files | Read |
|---|---|---|
| `docs/` (top level: `.header.md`, `index.md`, `1-pre-pali-study.md`, `2-sbs-book.md`, `3-patimokkha.md`, `7-notebook-lm.md`) | 6 | Full |
| `docs/4-dictionaries/` (`.header.md`, `index.md`, `1-sbs-pali-dictionary.md`, `2-ru-pali-dictionary.md`, `3-ta-pali-dictionary copy.md`) | 5 | Full |
| `docs/5-anki/` pages (`.header.md`, `index.md`, `3-patimokkha-learning.md`, `9-native.md`, `1-sbs/` ×2, `10-dps/` ×2, `2-patimokkha/` ×2, `4-vibhanga/` ×1, `5-dhp/` ×2, `6-suttas/` ×1, `7-daily_chants/` ×2, `8-parittas/` ×1, `general/` ×3, `other/` ×3) | 23 | Full (Russian pages: checked for site defects; their language is out of scope, see Follow-ups) |
| `docs/5-anki/field-lists/` (`index.md` full; 13 `field-list-*.md` prose only) | 14 | Full / prose only |
| `docs/5-anki/templates/` (`index.md` full; 34 template pages prose only) | 35 | Full / prose only |
| `docs/6-pali-class/` (`.header.md`, `index.md`, `1-pali-class-adv.md`, `2-patimokkha-class.md`, `atth-hoti.md`, `sbs-per-analysis.md`, `sbs-per-ex.md`) | 7 | Full |
| **Total** | **90** | |

**Not reviewed:** the English inside the Anki template code (field labels such as `Constr.:`; they must match the live Anki note types), and external links other than the 55 release-download and DPD links plus a handful that looked suspect (no full crawl, per the spec).

## Findings — Prose

### Decisions

1. **Spelling variety: American English.** Counted in the in-scope prose: American forms 26 (`memorization` 11, `memorizing` 4, `synchronize` 2, `specialized` 2, `labeled` 2, `realizing`/`realization` 2, `organized`, `generalized`, `analyzed`); British forms 6 (`honour` 5, `analysed` 1). All five `honour` are inside chant translations or SBS Recitations chapter titles, which quote the book and stay as they are. The only British form to change is `analysed`, in finding 47. LanguageTool already runs in `en-US`.
   - Category: Prose / consistency. Confidence: high.
   - Proposed: adopt American English for site prose; leave quoted book text alone.

2. **Pāli / Pāḷi and Pātimokkha / Pāṭimokkha: no blanket change.** In-scope prose has `Pāli` 69, `Pāḷi` 38, `Pali` 15 (most of these inside Anki deck names or search strings, which must stay), `Pātimokkha` 22, `Pāṭimokkha` 10, `Patimokkha` 3. `Pāḷi` is fixed inside proper names (*SBS Pāḷi-English Recitations*, *Digital Pāḷi Dictionary*), and the `Pātimokkha`/`Pāṭimokkha` split follows the source each page cites. Unifying them would touch 100+ lines, nav titles and generated pages, for no gain in clarity.
   - Category: Prose / consistency. Confidence: medium.
   - Proposed: no change. Only the unaccented `Pali` in English prose is fixed (findings 18 and 38).

### Top level

3. `docs/.header.md:11` (generates `docs/index.md:11`) — capital letter mid-sentence.
   - Current: `We would greatly appreciate your [Feedback]`
   - Proposed: `We would greatly appreciate your [feedback]`
   - Category: Prose / capitalisation. Confidence: medium.

4. `docs/1-pre-pali-study.md:3` — the site name is wrong (the home page calls the site "SBS DhammaVinaya Learning Tools"), and "or/and their" is awkward.
   - Current: `While the [SBS Pāli Study Tools](index.md) page provides extensive resources for learning Pāli, it is highly recommended to establish a strong foundation in the Dhamma and Vinaya first in English or/and their native language.`
   - Proposed: `While the [SBS DhammaVinaya Learning Tools](index.md) site provides extensive resources for learning Pāli, it is highly recommended to first establish a strong foundation in the Dhamma and Vinaya in English and/or one's native language.`
   - Category: Prose / grammar, naming. Confidence: medium.

5. `docs/1-pre-pali-study.md:21` — book title is miscapitalised and lacks its colon.
   - Current: `[“The wings to Awakening An Anthology from the Pāli Canon”]`
   - Proposed: `[“The Wings to Awakening: An Anthology from the Pāli Canon”]`
   - Category: Prose / title. Confidence: high.

6. `docs/1-pre-pali-study.md:25` — the paired dashes don't match (one closed up, one spaced).
   - Current: `(loving-kindness) — and reading all related suttas.`
   - Proposed: `(loving-kindness)—and reading all related suttas.`
   - Category: Prose / punctuation. Confidence: medium.

7. `docs/1-pre-pali-study.md:27` — missing full stop (the line above has one).
   - Current: `A more comprehensive index [can be found here](https://index.readingfaithfully.org)`
   - Proposed: `A more comprehensive index [can be found here](https://index.readingfaithfully.org).`
   - Category: Prose / punctuation. Confidence: low.

8. `docs/1-pre-pali-study.md:31` — **Pāḷi.** `Majjhimā` and `Therigāthā` are misspelt (the collection is *Majjhima Nikāya*, the book *Therīgāthā*; `7-notebook-lm.md:32` already has `Therīgāthāpāḷi`).
   - Current: `Then one may read the Majjhimā Nikāya` … `and the Theragāthā and Therigāthā).`
   - Proposed: `Then one may read the Majjhima Nikāya` … `and the Theragāthā and Therīgāthā).`
   - Category: Prose / Pāḷi spelling. Confidence: high.

9. `docs/1-pre-pali-study.md:37` — stray comma before a restrictive clause.
   - Current: `there’s an excellent [online tool](https://find.dhamma.gift/bw/home/index.html) available, that displays`
   - Proposed: `there’s an excellent [online tool](https://find.dhamma.gift/bw/home/index.html) available that displays`
   - Category: Prose / punctuation. Confidence: high.

10. `docs/2-sbs-book.md:5` — missing article; the full stop is inside the link text.
    - Current: `Online version can be found [here.](https://sasanarakkha.org/2019/09/08/sbs-pali-english-recitations/)`
    - Proposed: `An online version can be found [here](https://sasanarakkha.org/2019/09/08/sbs-pali-english-recitations/).`
    - Category: Prose / grammar. Confidence: high.

11. `docs/2-sbs-book.md:9` — sentence has no subject or verb.
    - Current: `Also available word by word [Analysis of SBS Pāḷi-English Recitations](6-pali-class/sbs-per-analysis.md)`
    - Proposed: `A word-by-word [Analysis of SBS Pāḷi-English Recitations](6-pali-class/sbs-per-analysis.md) is also available.`
    - Category: Prose / grammar. Confidence: high.

12. `docs/3-patimokkha.md:3` — unidiomatic.
    - Current: `Different editions of Pāṭimokkha are made in a format comfortable for recitation and memorization.`
    - Proposed: `Several editions of the Pāṭimokkha are available, formatted for easy recitation and memorization.`
    - Category: Prose / clarity. Confidence: medium.

13. `docs/3-patimokkha.md:7` — missing full stop after the abbreviation (`Ven.` everywhere else).
    - Current: `done by Ven Ñāṇatusita in his book`
    - Proposed: `done by Ven. Ñāṇatusita in his book`
    - Category: Prose / punctuation. Confidence: high.

14. `docs/3-patimokkha.md:13` — missing verb, comma splice, wrong preposition.
    - Current: `The following materials made as a draft, you can use them on your own risk.`
    - Proposed: `The following materials are drafts; use them at your own risk.`
    - Category: Prose / grammar. Confidence: high.

15. `docs/3-patimokkha.md:24` — missing determiner; **Pāḷi:** `Tipitaka` lacks its diacritic (`Tipiṭaka` everywhere else).
    - Current: `Edition of the Pāṭimokkha is based on the Sri Lankan edition of the Tipitaka,`
    - Proposed: `This edition of the Pāṭimokkha is based on the Sri Lankan edition of the Tipiṭaka,`
    - Category: Prose / grammar, Pāḷi spelling. Confidence: high.

16. `docs/3-patimokkha.md:31` — wrong preposition and article; the site is spelt *SuttaCentral*.
    - Current: `or in the [Suttacentral]`
    - Proposed: `or on [SuttaCentral]`
    - Category: Prose / grammar, naming. Confidence: high.

17. `docs/7-notebook-lm.md:15` and `:19` — missing articles.
    - Current (`:15`): `mūla of Early part of the Sutta Tipiṭaka and mūla of whole Vinaya Tipiṭaka`
    - Proposed (`:15`): `mūla of the early part of the Sutta Tipiṭaka and mūla of the whole Vinaya Tipiṭaka`
    - Current (`:19`): `everything from Tipiṭaka (mūla, atthakathā, ṭīkā)`
    - Proposed (`:19`): `everything from the Tipiṭaka (mūla, atthakathā, ṭīkā)`
    - Category: Prose / grammar. Confidence: high.

### Dictionaries

18. `docs/4-dictionaries/.header.md:3`, `:5`, `:7` (generates `docs/4-dictionaries/index.md`) — the opening sentence needs a comma or reordering; `Pali` lacks diacritics while the same list spells it *Digital Pāḷi Dictionary*.
    - Current (`:3`): `In studying Pāli digital dictionaries are invaluable resources. Here is a list of them.`
    - Proposed (`:3`): `Digital dictionaries are invaluable resources for studying Pāli. Here is a list of them.`
    - Current (`:5`): `- [Digital Pali Dictionary](https://dpdict.net)`
    - Proposed (`:5`): `- [Digital Pāḷi Dictionary](https://dpdict.net)`
    - Current (`:7`): `- [Other Pali and Sanskrit dictionaries]`
    - Proposed (`:7`): `- [Other Pāli and Sanskrit dictionaries]`
    - Category: Prose / grammar, consistency. Confidence: high.

19. `docs/4-dictionaries/1-sbs-pali-dictionary.md:19` — "extended version dictionary" is ungrammatical.
    - Current: `this extended version dictionary provides`
    - Proposed: `this extended dictionary provides`
    - Category: Prose / grammar. Confidence: high.

20. `docs/4-dictionaries/1-sbs-pali-dictionary.md:21` — garbled sentence.
    - Current: `Also it includes English translation as it in the Key to Exercises.`
    - Proposed: `It also includes the English translation as given in the Key to Exercises.`
    - Category: Prose / grammar. Confidence: high.

21. `docs/4-dictionaries/1-sbs-pali-dictionary.md:29`, `docs/4-dictionaries/2-ru-pali-dictionary.md:29`, `docs/4-dictionaries/3-ta-pali-dictionary copy.md:25` — the product is *GoldenDict* (as on line 14/18 of the same pages).
    - Current: `Instructions for installing Goldendict and MDict`
    - Proposed: `Instructions for installing GoldenDict and MDict`
    - Category: Prose / naming. Confidence: high.

### Anki

22. `docs/5-anki/.header.md:7` (generates `docs/5-anki/index.md:7`) — word order.
    - Current: `on the [release GitHub page]`
    - Proposed: `on the [GitHub release page]`
    - Category: Prose / wording. Confidence: medium.

23. `docs/5-anki/1-sbs/1-sbs-vocab.md:7` — a semicolon where a comma belongs.
    - Current: `together with [SBS Pāḷi-English Recitations](../../2-sbs-book.md); the [Analysis of SBS Pāḷi-English Recitations](../../6-pali-class/sbs-per-analysis.md) and the [DPD with SBS examples]`
    - Proposed: `together with [SBS Pāḷi-English Recitations](../../2-sbs-book.md), the [Analysis of SBS Pāḷi-English Recitations](../../6-pali-class/sbs-per-analysis.md), and the [DPD with SBS examples]`
    - Category: Prose / punctuation. Confidence: high.

24. `docs/5-anki/1-sbs/1-sbs-vocab.md:9` and `docs/6-pali-class/sbs-per-analysis.md:77` — clumsy passive ("can be made use of").
    - Current (`1-sbs-vocab.md:9`): `Also, as a reference [Word by Word Analysis of SBS Anumodana made by Ven. Ṭhanuttamo](../../6-pali-class/sbs-per-analysis/word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md) can be made use of.`
    - Proposed: `The [Word by Word Analysis of SBS Anumodana made by Ven. Ṭhanuttamo](../../6-pali-class/sbs-per-analysis/word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md) can also be used as a reference.`
    - Current (`sbs-per-analysis.md:77`): `Also, as a reference [Word by Word Analysis of SBS Anumodana made by Ven. Ṭhanuttamo](sbs-per-analysis/word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md) can be made use of.`
    - Proposed: `The [Word by Word Analysis of SBS Anumodana made by Ven. Ṭhanuttamo](sbs-per-analysis/word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md) can also be used as a reference.`
    - Category: Prose / clarity. Confidence: medium.

25. `docs/5-anki/1-sbs/study-ways.md:5`, `:8`, `:14`, `:16` — missing articles, fragments, and an unclear explanation.
    - Current (`:5`): `- Read analysis of the first chant.`
    - Proposed (`:5`): `- Read the analysis of the first chant.`
    - Current (`:8`): `- Better to go with the order of the Recitation Book.`
    - Proposed (`:8`): `- It is best to follow the order of the Recitation Book.`
    - Current (`:14`): `Using this method you are at risk of missing some words, because they have been added in the order of the Recitation Book, and if a word appears later it is not always added again.`
    - Proposed (`:14`): `With this method you may miss some words: words were added in the order of the Recitation Book, and a word that appears again in a later chant is not always added again.`
    - Current (`:16`): `- Read the analysis of the chant that you like to study.`
    - Proposed (`:16`): `- Read the analysis of the chant that you would like to study.`
    - Category: Prose / grammar, clarity. Confidence: medium.

26. `docs/5-anki/2-patimokkha/custom-study.md:3`, `:7`, `:17` — missing article and full stops; mismatched quotation marks (`*…"`) on line 7.
    - Current (`:3`): `Create a **Custom study** for current deck`
    - Proposed (`:3`): `Create a **Custom study** for the current deck.`
    - Current (`:7`): `For example choose *Study by card state", and simply click "OK" without selecting any tags.`
    - Proposed (`:7`): `For example, choose "Study by card state" and simply click "OK" without selecting any tags.`
    - Current (`:17`): `This will filter all words from the current deck that are from Nidāna`
    - Proposed (`:17`): `This will filter all words from the current deck that are from Nidāna.`
    - Category: Prose / punctuation, grammar. Confidence: high.

27. `docs/5-anki/2-patimokkha/custom-study.md:11` — run-together words; Anki's button is *Options*.
    - Current: `Go to **Option** of this **Custom study** and adjust the *search* fieldto find the words you need, for example: `
    - Proposed: `Go to **Options** of this **Custom study** and adjust the *search* field to find the words you need, for example: `
    - Category: Prose / spelling. Confidence: high (`fieldto`), medium (`Options`).

28. `docs/5-anki/2-patimokkha/1-patimokkha-word-by-word.md:5` — two main verbs in one clause ("This is … is based on").
    - Current: `This is the word by word analysis of the version of the Bhikkhu Pāṭimokkha is based on the comparative study done by Ñāṇatusita in his book`
    - Proposed: `This is a word-by-word analysis of the version of the Bhikkhu Pāṭimokkha that is based on the comparative study by Ñāṇatusita in his book`
    - Category: Prose / grammar. Confidence: high.

29. `docs/5-anki/2-patimokkha/1-patimokkha-word-by-word.md:9`, `:11` — inverted word order; sentence starts lower case.
    - Current (`:9`): `Analysis of the Bhikkhupātimokkha you can see and comment [here]`
    - Proposed (`:9`): `You can view and comment on the analysis of the Bhikkhupātimokkha [here]`
    - Current (`:11`): `or use analysis in [HTML]`
    - Proposed (`:11`): `Or use the analysis in [HTML]`
    - Category: Prose / grammar. Confidence: high.

30. `docs/5-anki/2-patimokkha/1-patimokkha-word-by-word.md:15` — the language name is capitalised everywhere else.
    - Current: `which contains pāli words from definitions`
    - Proposed: `which contains Pāli words from definitions`
    - Category: Prose / capitalisation. Confidence: high.

31. `docs/5-anki/3-patimokkha-learning.md:3` — stray possessive; "is also include".
    - Current: `with the voice of Bhante Ariyadhammika’s and English translations. It is also include Pubbakicca.`
    - Proposed: `with the voice of Bhante Ariyadhammika and English translations. It also includes the Pubbakicca.`
    - Category: Prose / grammar. Confidence: high.

32. `docs/5-anki/3-patimokkha-learning.md:5` — **Pāḷi.** Name misspelt (`Ñāṇatusita` everywhere else on the site).
    - Current: `[Ven. Ñānatusita's version of the Pāṭimokkha]`
    - Proposed: `[Ven. Ñāṇatusita's version of the Pāṭimokkha]`
    - Category: Prose / Pāḷi spelling. Confidence: high.

33. `docs/5-anki/3-patimokkha-learning.md:9` — "the anki.web" is not a name.
    - Current: `- Or download this deck from [the sharing page on the anki.web]`
    - Proposed: `- Or download this deck from [its AnkiWeb sharing page]`
    - Category: Prose / naming. Confidence: medium.

34. `docs/5-anki/4-vibhanga/1-vibhanga.md:5` and `docs/5-anki/5-dhp/1-dhp-vocab.md:5` — missing article (the SBS deck page has it).
    - Current: `Made for memorization of`
    - Proposed: `Made for the memorization of`
    - Category: Prose / grammar. Confidence: medium.

35. `docs/5-anki/5-dhp/1-dhp-vocab.md:7` and `docs/5-anki/5-dhp/study-ways.md:3` — missing full stops.
    - Current (`1-dhp-vocab.md:7`): `[Dhammapada grammatical analysis](https://buddhism.lib.ntu.edu.tw/DLMBS/en/lesson/pali/lesson_pali3.jsp)`
    - Proposed: add `.` at the end of the line.
    - Current (`study-ways.md:3`): `in the Pāḷi and in [the analysis](https://buddhism.lib.ntu.edu.tw/DLMBS/en/lesson/pali/lesson_pali3.jsp)`
    - Proposed: add `.` at the end of the line.
    - Category: Prose / punctuation. Confidence: low.

36. `docs/5-anki/6-suttas/1-sutta-advanced.md:3` and `docs/6-pali-class/1-pali-class-adv.md:35` — "Venerable Bhikkhu" doubles the title; `:35` also has a stray "the" before the book title.
    - Current (`1-sutta-advanced.md:3`): `by Venerable Bhikkhu Bodhi.`
    - Proposed: `by Bhikkhu Bodhi.`
    - Current (`1-pali-class-adv.md:35`): `can be found in the **Reading the Buddha’s Discourses in Pāli** by Venerable Bhikkhu Bodhi.`
    - Proposed: `can be found in **Reading the Buddha’s Discourses in Pāli** by Bhikkhu Bodhi.`
    - Category: Prose / wording. Confidence: medium.

37. `docs/5-anki/6-suttas/1-sutta-advanced.md:5` — typo.
    - Current: `secton`
    - Proposed: `section`
    - Category: Prose / spelling. Confidence: high.

38. `docs/5-anki/6-suttas/1-sutta-advanced.md:5` — link text lacks the diacritic used in the target page's title.
    - Current: `[Advanced Pali]`
    - Proposed: `[Advanced Pāli]`
    - Category: Prose / consistency. Confidence: high.

39. `docs/5-anki/8-parittas/1-parittas.md:9`, `:15` — incomplete sentence; missing subject.
    - Current (`:9`): `Word by word analysis of those suttas can be found `
    - Proposed (`:9`): `Word-by-word analyses of these suttas can be found here:`
    - Current (`:15`): `For easier memorization, can be helpful to use audio of those chants.`
    - Proposed (`:15`): `For easier memorization, it can be helpful to listen to recordings of these chants.`
    - Category: Prose / grammar. Confidence: high.

40. `docs/5-anki/9-native.md:5` — wordy and hedged twice ("may potentially").
    - Current: `We are delighted to provide additional data for Russian at the moment, and we may potentially expand our language support to include other languages in the future.`
    - Proposed: `At the moment we provide additional data for Russian, and we may add other languages in the future.`
    - Category: Prose / clarity. Confidence: medium.

41. `docs/5-anki/9-native.md:12`, `:13` — the deck labels look swapped: the *common roots* CSV is labelled "Grammar Deck" and the *grammar* CSV "Common Roots Deck". Owner to confirm.
    - Current (`:12`): `[ru-common-roots.csv](https://github.com/sasanarakkha/study-tools/releases/latest/download/ru-common-roots.csv) (Grammar Deck; Grammar Note Type)`
    - Proposed (`:12`): `[ru-common-roots.csv](https://github.com/sasanarakkha/study-tools/releases/latest/download/ru-common-roots.csv) (Common Roots Deck)`
    - Current (`:13`): `[ru-grammar-pali-class-gramm.csv](https://github.com/sasanarakkha/study-tools/releases/latest/download/ru-grammar-pali-class-gramm.csv) (Common Roots Deck)`
    - Proposed (`:13`): `[ru-grammar-pali-class-gramm.csv](https://github.com/sasanarakkha/study-tools/releases/latest/download/ru-grammar-pali-class-gramm.csv) (Grammar Deck; Grammar Note Type)`
    - Category: Prose / accuracy. Confidence: medium.

42. `docs/5-anki/9-native.md:9`, `:19` — the file is called `sbs-rus.csv` (the link target), but the text calls it `sbs_russian.csv`.
    - Current (`:9`): `- [sbs_russian.csv](https://github.com/sasanarakkha/study-tools/releases/latest/download/sbs-rus.csv)`
    - Proposed (`:9`): `- [sbs-rus.csv](https://github.com/sasanarakkha/study-tools/releases/latest/download/sbs-rus.csv)`
    - Current (`:19`): `Let’s describe the process for sbs_russian.csv in detail.`
    - Proposed (`:19`): `Let’s describe the process for sbs-rus.csv in detail.`
    - Category: Prose / accuracy. Confidence: medium.

43. `docs/5-anki/9-native.md:33`, `:39` — double space; the button and key names are capitalised elsewhere (`**Import**`, `Ctrl + Del`).
    - Current (`:33`): `then click  **import**`
    - Proposed (`:33`): `then click **Import**`
    - Current (`:39`): `(**Ctrl + del**)`
    - Proposed (`:39`): `(**Ctrl + Del**)`
    - Category: Prose / consistency. Confidence: high.

44. `docs/5-anki/general/csv-update.md:3` — "more reliable but complex" doesn't parallel.
    - Current: `this method is more reliable but complex.`
    - Proposed: `this method is more reliable but more complex.`
    - Category: Prose / grammar. Confidence: medium.

45. `docs/5-anki/general/special-fields.md:3`, `:9`, `:15`, `:17`, `:21`, `:23`, `:27` — lower-case sentence starts, missing articles, garbled sentences.
    - Current (`:3`): `By default it is easier without this add-on.`
    - Proposed (`:3`): `By default, it is easier without this add-on.`
    - Current (`:9`): `You can check [page](https://ankiweb.net/shared/info/1102281552) of Add-on "special fields"`
    - Proposed (`:9`): `See the add-on's [page on AnkiWeb](https://ankiweb.net/shared/info/1102281552).`
    - Current (`:15`): `restart Anki`
    - Proposed (`:15`): `Restart Anki.`
    - Current (`:17`): `open settings of Add-on special fields **Tools > Special Fields**`
    - Proposed (`:17`): `Open the add-on's settings: **Tools > Special Fields**`
    - Current (`:21`): `click **'Update' Settings**`
    - Proposed (`:21`): `Click **'Update' Settings**.`
    - Current (`:23`): `also, if you like to protect fields which you edit yourself, like **native** or **marks** - you may add them, and Add-on will protect them while next update.`
    - Proposed (`:23`): `Also, if you want to protect fields that you edit yourself, such as **native** or **marks**, add them here, and the add-on will protect them during the next update.`
    - Current (`:27`): `For more details how to use this add-on see small [video](https://youtu.be/TTHpODHBk3U).`
    - Proposed (`:27`): `For more details on how to use this add-on, see this short [video](https://youtu.be/TTHpODHBk3U).`
    - Category: Prose / grammar. Confidence: high.

46. `docs/5-anki/general/updating.md:19` — "up-to-date" is hyphenated only before a noun.
    - Current: `to stay up-to-date.`
    - Proposed: `to stay up to date.`
    - Category: Prose / punctuation. Confidence: low.

47. `docs/5-anki/other/reading-common-pali-phrases.md:5` — verb agreement, British `analysed` (finding 1), word order, and an unclear last clause.
    - Current: `This Anki pack consist of the most commonly used phrases in the Sutta and Vinaya Piṭaka, analysed word-by-word. In this way, with learning relatively a small amount of words, a lot of phrases in the Pāli texts can be understood. Ideal for those starting to learn Pāli or those who have been learning Pāli for a while and want to deepen those important phrases.`
    - Proposed: `This Anki pack consists of the most commonly used phrases in the Sutta and Vinaya Piṭaka, analyzed word by word. In this way, by learning a relatively small number of words, a lot of phrases in the Pāli texts can be understood. Ideal for those starting to learn Pāli or those who have been learning Pāli for a while and want to deepen their knowledge of these important phrases.`
    - Category: Prose / grammar. Confidence: high.

48. `docs/5-anki/other/reading-common-pali-phrases.md:7`, `:9`, `:11` — wrong preposition; "extend" for "extent".
    - Current (`:7`): `Version 1.0 consists of 15 phrases of a total of 152 words`
    - Proposed (`:7`): `Version 1.0 consists of 15 phrases with a total of 152 words.`
    - Current (`:9`): `every month with full-moon uposatha.`
    - Proposed (`:9`): `every month on the full-moon uposatha.`
    - Current (`:11`): `to the extend that`
    - Proposed (`:11`): `to the extent that`
    - Category: Prose / grammar, spelling. Confidence: high.

49. `docs/5-anki/other/reading-common-pali-phrases.md:30`, `:32` — garbled instructions.
    - Current (`:30`): `- For updating existing pack with keeping statistic do the same, while your Anki is open, just double-click on the downloaded file reading-common-pali-phrases.apkg, and it will update.`
    - Proposed (`:30`): `- To update an existing pack and keep your statistics, do the same: with Anki open, double-click the downloaded file reading-common-pali-phrases.apkg, and it will update.`
    - Current (`:32`): `- If English is not your first language, it is always recommended to translate words on your native language. For this, we have empty field "native". You can fill it. And even with next update, this field still will keep all your info.`
    - Proposed (`:32`): `- If English is not your first language, it is always recommended to translate words into your native language. For this, there is an empty field called "native" that you can fill in; it keeps your entries across updates.`
    - Category: Prose / grammar. Confidence: high.

50. `docs/5-anki/other/reading-common-pali-phrases.md:40`, `:42`, `:49` — this section downloads the **CSV** and imports it, but step `:42` says to choose the `.apkg`; missing article and hyphen.
    - Current (`:40`): `- in the Anki click on **File - Import**`
    - Proposed (`:40`): `- in Anki, click on **File - Import**`
    - Current (`:42`): `- choose downloaded reading-common-pali-phrases.apkg`
    - Proposed (`:42`): `- choose the downloaded reading-common-pali-phrases.csv`
    - Current (`:49`): `- double check everything, and click **import**`
    - Proposed (`:49`): `- double-check everything, and click **Import**`
    - Category: Prose / accuracy, grammar. Confidence: high (`.csv`, see the download link on line 38).

51. `docs/5-anki/other/test.md:7`, `:15`, `:17`, `:21`, `:27` — fragments and typos (`Brows`, `delate`).
    - Current (`:7`): `After you updated the downloaded Anki Deck (by double-clicking on the latest downloaded file, or using CSV). Choose your Deck and in the Browse and add:`
    - Proposed (`:7`): `After updating the downloaded Anki deck (by double-clicking the latest downloaded file, or by using CSV), open **Browse**, choose your deck and add:`
    - Current (`:15`): `As it depends on the name of the deck you are updating and the {day} of update.`
    - Proposed (`:15`): `It depends on the name of the deck you are updating and the {date} of the update.`
    - Current (`:17`): `You can look it on the [page of latest release](https://github.com/sasanarakkha/study-tools/releases/latest/). For example if date is 25.11 you need to use {date} in the format 25-11.`
    - Proposed (`:17`): `You can find it on the [latest release page](https://github.com/sasanarakkha/study-tools/releases/latest/). For example, if the date is 25.11, you need to use {date} in the format 25-11.`
    - Current (`:21`): `Using this search in the Anki Brows you will see all cards which do not have a {day} in field "Test". And you can easily delate all of this old words,`
    - Proposed (`:21`): `Using this search in the Anki Browser, you will see all cards that do not have the {date} in the "Test" field. You can easily delete all these old words`
    - Current (`:27`): `## If it is not regular update`
    - Proposed (`:27`): `## If it is not a regular update`
    - Category: Prose / grammar, spelling. Confidence: high.

### Pāli classes

52. `docs/6-pali-class/1-pali-class-adv.md:5` — the opening is a sentence fragment.
    - Current: `How to proceed with individual Pāli study once you're finished with the`
    - Proposed: `This page explains how to continue individual Pāli study once you have finished the`
    - Category: Prose / grammar. Confidence: medium.

53. `docs/6-pali-class/1-pali-class-adv.md:11` — "do analysis of the book" is unclear.
    - Current: `It is recommended to do analysis of the SBS Pāḷi-English Recitations book together with the Anki deck.`
    - Proposed: `It is recommended to study the analysis of the SBS Pāḷi-English Recitations book together with the Anki deck.`
    - Category: Prose / clarity. Confidence: medium.

54. `docs/6-pali-class/1-pali-class-adv.md:17` — typo.
    - Current: `incluading`
    - Proposed: `including`
    - Category: Prose / spelling. Confidence: high.

55. `docs/6-pali-class/1-pali-class-adv.md:31` — missing verb and article.
    - Current: `Or [update deck from csv](https://digitalpalidictionary.github.io/dpd-pali-courses/anki/) if you already using one.`
    - Proposed: `Or [update the deck from CSV](https://digitalpalidictionary.github.io/dpd-pali-courses/anki/) if you are already using one.`
    - Category: Prose / grammar. Confidence: high.

56. `docs/6-pali-class/1-pali-class-adv.md:37`, `:39`, `:41`, `:43`, `:53` — double spaces.
    - Current: `Compilation from  ` (two spaces)
    - Proposed: `Compilation from ` (one space)
    - Category: Prose / whitespace. Confidence: low (no visible effect; the browser collapses spaces).

57. `docs/6-pali-class/1-pali-class-adv.md:49`, `:51` — **Pāḷi.** "Bojjhaṅgasaṃyutta Saṃyutta" and "Maggasaṃyutta Saṃyutta" say *saṃyutta* twice (also noted in `kamma/audit/sutta-audit/sutta-audit.md` for the linked pages, which are out of scope here).
    - Current (`:49`): `Bojjhaṅgasaṃyutta Saṃyutta`
    - Proposed (`:49`): `Bojjhaṅga Saṃyutta`
    - Current (`:51`): `Maggasaṃyutta Saṃyutta`
    - Proposed (`:51`): `Magga Saṃyutta`
    - Category: Prose / Pāḷi naming. Confidence: medium.

58. `docs/6-pali-class/1-pali-class-adv.md:63` — no capital, typo, comma splice.
    - Current: `materials in the proccess of development, if you want to see drafts, please contact us.`
    - Proposed: `These materials are in the process of development. If you would like to see drafts, please contact us.`
    - Category: Prose / grammar, spelling. Confidence: high.

59. `docs/6-pali-class/2-patimokkha-class.md:5` — the linked analysis is a Google Sheet, not a Google document (line 13 calls it "the Google Sheet").
    - Current: `or by commenting directly in the Google document.`
    - Proposed: `or by commenting directly in the Google Sheet.`
    - Category: Prose / accuracy. Confidence: medium.

60. `docs/6-pali-class/sbs-per-analysis.md:3` and `docs/6-pali-class/sbs-per-ex.md:3` — typo and missing article.
    - Current: `Made for better gramatical understanding`
    - Proposed: `Made for a better grammatical understanding`
    - Category: Prose / spelling. Confidence: high.

61. `docs/6-pali-class/sbs-per-analysis.md:7` and `docs/6-pali-class/sbs-per-ex.md:5` — typo.
    - Current: `Files that may be usefull with this analysis:`
    - Proposed: `Files that may be useful with this analysis:`
    - Category: Prose / spelling. Confidence: high.

62. `docs/6-pali-class/sbs-per-analysis.md:106` and `docs/6-pali-class/sbs-per-ex.md:105` — typo.
    - Current: `**SHARING OF MERRITS**`
    - Proposed: `**SHARING OF MERITS**`
    - Category: Prose / spelling. Confidence: high.

63. `docs/6-pali-class/sbs-per-analysis.md:32`, `:36` and `docs/6-pali-class/sbs-per-ex.md:33`, `:37` — title case is inconsistent within the list.
    - Current: `[A single Excellent Night]` and `[Setting in Motion The Wheel of Dhamma]`
    - Proposed: `[A Single Excellent Night]` and `[Setting in Motion the Wheel of Dhamma]`
    - Category: Prose / capitalisation. Confidence: low (the SBS book's own capitalisation was not checked).

64. `docs/6-pali-class/sbs-per-analysis.md:114` and `docs/6-pali-class/sbs-per-ex.md:113` — missing comma and full stop; on `sbs-per-ex` the article doesn't fit a plural.
    - Current (`sbs-per-analysis.md:114`): `In addition there is an analysis of [Post Pātimokkha recitations](sbs-per-analysis/post-patimokkha.md)`
    - Proposed: `In addition, there is an analysis of [Post Pātimokkha recitations](sbs-per-analysis/post-patimokkha.md).`
    - Current (`sbs-per-ex.md:113`): `In addition there is a [Post Pātimokkha recitations]()`
    - Proposed: `In addition, there are [Post Pātimokkha recitations]().`
    - Category: Prose / punctuation. Confidence: low.

65. `docs/6-pali-class/sbs-per-ex.md:1` — typo in the page title.
    - Current: `# **Exersises of sentences from SBS Pāḷi-English Recitations**`
    - Proposed: `# **Exercises of sentences from SBS Pāḷi-English Recitations**`
    - Category: Prose / spelling. Confidence: high.

66. `docs/6-pali-class/atth-hoti.md:3` — says "suttas" twice in one sentence.
    - Current: `Based on the suttas, there is a distinction between **atthi** and **hoti** in the Pāḷi suttas.`
    - Proposed: `The Pāḷi suttas show a distinction between **atthi** and **hoti**.`
    - Category: Prose / clarity. Confidence: low.

67. `docs/6-pali-class/atth-hoti.md:57` — typo; "Saying this" for "That said".
    - Current: `Saying this, it is improtant to remember:`
    - Proposed: `That said, it is important to remember:`
    - Category: Prose / spelling. Confidence: high.

68. `docs/6-pali-class/atth-hoti.md:63`, `:85` — "the provided sources" reads like text left over from an AI research tool; the reader was given no sources.
    - Current (`:63`): `The provided sources **do not support**`
    - Proposed (`:63`): `The suttas **do not support**`
    - Current (`:85`): `The sources clearly show`
    - Proposed (`:85`): `The suttas clearly show`
    - Category: Prose / clarity. Confidence: medium.

69. `docs/6-pali-class/atth-hoti.md:77` — the site uses *kamma* (`1-pre-pali-study.md:25`), not *karma*.
    - Current: `the objective laws of karma and the universe`
    - Proposed: `the objective laws of kamma and the universe`
    - Category: Prose / consistency. Confidence: medium.

## Findings — Site

70. **Lists shown as plain text.** Python-Markdown needs a blank line before a list. Without it, the items render as one paragraph with literal `- ` or `*` characters (seen in `site/1-pre-pali-study/index.html` and `site/4-dictionaries/1-sbs-pali-dictionary/index.html`). On `atth-hoti.md` the bold line before each list also swallows the next line, which garbles the bold and italics across lines 67–82. Found by `temp/site-audit/find_unseparated_lists.py`.
    - Proposed: insert one empty line **after** each of these lines (no other change):
      - `docs/1-pre-pali-study.md:25` (`This method involves selecting…`)
      - `docs/4-dictionaries/1-sbs-pali-dictionary.md:13` (`Download the latest update in various formats:`)
      - `docs/4-dictionaries/2-ru-pali-dictionary.md:17` (same text)
      - `docs/4-dictionaries/3-ta-pali-dictionary copy.md:17` (same text)
      - `docs/5-anki/9-native.md:11` (`For Pāli Class decks:`)
      - `docs/5-anki/other/reading-common-pali-phrases.md:13` (`This learning tool consists of:`)
      - `docs/6-pali-class/atth-hoti.md:67`, `:68`, `:73`, `:74`, `:79`, `:80`, `:84` (each bold label and each line that introduces a list)
      - `docs/6-pali-class/sbs-per-analysis.md:7` (`Files that may be usefull…`) and `:12` (`**HOMAGE TO THE TRIPLE GEM**`)
      - `docs/7-notebook-lm.md:27` (`*__Early part of the Sutta Tipiṭaka__, it includes:`)
    - Category: Site / rendering. Confidence: high.

71. **"Anki Decks index" links go to the site home page.** From `docs/5-anki/general/` and `docs/5-anki/field-lists/` and `docs/5-anki/templates/`, `../../index.md` is `docs/index.md` (the home page); the Anki index is `../index.md`. The sibling links in `special-fields.md:33`, `updating.md:45` and `csv-update.md:45` already use `../index.md`.
    - Current (`docs/5-anki/general/updating.md:11`): `[Anki Decks index](../../index.md)`
    - Proposed: `[Anki Decks index](../index.md)`
    - Current (`docs/5-anki/field-lists/index.md:29` and `docs/5-anki/templates/index.md:35`): `[Anki Decks](../../index.md)`
    - Proposed: `[Anki Decks](../index.md)`
    - Category: Site / wrong link. Confidence: high.

72. **Dead DPD links (HTTP 404).** The DPD site moved to directory URLs; `features/` and `install/` return 200 (checked with `curl`).
    - Current (`docs/4-dictionaries/1-sbs-pali-dictionary.md:19`): `https://digitalpalidictionary.github.io/features.html`
    - Proposed: `https://digitalpalidictionary.github.io/features/`
    - Current (`1-sbs-pali-dictionary.md:29`, `2-ru-pali-dictionary.md:29`, `3-ta-pali-dictionary copy.md:25`): `https://digitalpalidictionary.github.io/titlepage.html`
    - Proposed: `https://digitalpalidictionary.github.io/install/`
    - Category: Site / dead link. Confidence: high.

73. **Dead BPS link (HTTP 404)** in `docs/3-patimokkha.md:7` and `docs/5-anki/2-patimokkha/1-patimokkha-word-by-word.md:5`: `https://www.bps.lk/olib/bp/bp626s_Nyanatusita_Analysis-of-Bhikkhu-Patimokkha.pdf`. No replacement URL was found. **Needs input:** if the owner supplies a new URL, write it into the Proposed line below before approving; otherwise leave unticked.
    - Current: `https://www.bps.lk/olib/bp/bp626s_Nyanatusita_Analysis-of-Bhikkhu-Patimokkha.pdf`
    - Proposed: *(owner to supply)*
    - Category: Site / dead link. Confidence: high (that the link is dead).

74. **⚠ data/URL — the Tamil page's file name ends in " copy".** `docs/4-dictionaries/3-ta-pali-dictionary copy.md` is **not** a duplicate: it is the only Tamil page, and its text, images (`dict-grammar-ta.png`, `dict-ta-pali.png`) and downloads (`dpd+ta-*.zip`) differ from the Russian page. The space gives the published URL `4-dictionaries/3-ta-pali-dictionary%20copy/`. Nothing else in `docs/` links to it by name; the index and nav are generated from the file name.
    - Current: `docs/4-dictionaries/3-ta-pali-dictionary copy.md`
    - Proposed: `git mv "docs/4-dictionaries/3-ta-pali-dictionary copy.md" docs/4-dictionaries/3-ta-pali-dictionary.md`; the old URL stops working (the new one is `4-dictionaries/3-ta-pali-dictionary/`).
    - Category: Site / stray file name. Confidence: high.

75. **Bold markup in page titles shows as `**` in the nav.** The nav is built from the first heading, so `mkdocs.yaml` gets `'**Advanced Pāli Education**'`, and the sidebar and `6-pali-class/index.md` show it with the asterisks (seen in `site/6-pali-class/index.html`).
    - Current (`docs/6-pali-class/1-pali-class-adv.md:1`): `# **Advanced Pāli Education**`
    - Proposed: `# Advanced Pāli Education`
    - Current (`docs/6-pali-class/2-patimokkha-class.md:1`): `# **Pātimokkha Word By Word class**`
    - Proposed: `# Pātimokkha Word By Word Class`
    - Category: Site / heading. Confidence: high.

76. **More than one H1 per page.** These lines are section headings but use `#`, the page-title level.
    - Current → Proposed (change `# ` to `## `, text unchanged):
      - `docs/5-anki/10-dps/1-ru-pali-vocab.md:12`, `:20`, `:24`
      - `docs/6-pali-class/2-patimokkha-class.md:18`, `:24`
      - `docs/6-pali-class/sbs-per-analysis.md:10`
      - `docs/6-pali-class/sbs-per-ex.md:10`
      - `docs/5-anki/other/reading-common-pali-phrases.md:34`
    - Category: Site / heading. Confidence: medium (the heading anchors stay the same; no link in `docs/` points at them).

77. **⚠ data — empty headings.** A `## Maintenance` heading with nothing under it closes three pages.
    - Current: `## Maintenance` at `docs/5-anki/10-dps/ru-test.md:26`, `docs/5-anki/other/reading-common-pali-phrases.md:53`, `docs/5-anki/other/sbs-anumodana.md:14`
    - Proposed: delete those three lines.
    - Category: Site / heading. Confidence: medium.

78. **Raw HTML with an empty link** in `docs/5-anki/other/reading-common-pali-phrases.md:22` (raw HTML is against the project's clean-Markdown rule, and `href=""` goes nowhere).
    - Current: `Spot a mistake? <a class="link" href="">Fix it here</a>`
    - Proposed: `Spot a mistake? [Fix it here](https://docs.google.com/forms/d/1Z8Jjt0-E0HNX7ygABIzAcrChG23M3IOyoZGQ-EDRzXY/viewform?)` (the feedback form already linked on line 20)
    - Category: Site / raw HTML, dead link. Confidence: medium.

79. **HTML entity in source URLs.** `&amp;` inside a Markdown URL. It renders the same as `&` (checked in the built HTML), but entities in sources break the clean-Markdown rule.
    - Current: `usp=pp_url&amp;entry.1433863141=` at `docs/5-anki/4-vibhanga/1-vibhanga.md:5`, `docs/5-anki/5-dhp/1-dhp-vocab.md:5`, `docs/5-anki/8-parittas/1-parittas.md:5`
    - Proposed: `usp=pp_url&entry.1433863141=`
    - Category: Site / raw HTML. Confidence: low.

80. **Template pages missing from the templates index.** `paritta-front.md`, `paritta-back.md`, `dps-front.md`, `dps-back.md` are published but nothing links to them. `field-lists/index.md:24` already lists Paritta.
    - Current (`docs/5-anki/templates/index.md:31`): `- Advanced Suttas: [Front](suttas-front.md)|[Back](suttas-back.md)`
    - Proposed: keep that line and add two lines after it:
      `- Paritta: [Front](paritta-front.md)|[Back](paritta-back.md)`
      `- Pāli (Russian deck): [Front](dps-front.md)|[Back](dps-back.md)`
    - Category: Site / orphan page. Confidence: medium (the label for the `dps` templates is a guess: their heading is just "Pāli", and `field-list-dps.md` has `ru_meaning` fields).

### Anki field-list and template pages

81. **Template page titles are lower case**, unlike `templates/index.md`, which names the same note types in title case.
    - Current → Proposed (heading line 1 only):
      - `class-back.md`, `class-front.md`: `pali class Vocab` → `Pāli Class Vocab`
      - `common-roots-back.md`, `common-roots-front.md`: `common roots` → `Common Roots`
      - `grammar-abbrev-back.md`, `grammar-abbrev-front.md`: `pali class abbrev` → `Pāli Class Abbrev`
      - `grammar-gramm-back-back.md`, `grammar-gramm-back-front.md`, `grammar-gramm-forth-back.md`, `grammar-gramm-forth-front.md`: `pali class Grammar` → `Pāli Class Grammar`
      - `grammar-sandhi-back-back.md`, `grammar-sandhi-back-front.md`, `grammar-sandhi-forth-back.md`, `grammar-sandhi-forth-front.md`: `pali class Sandhi` → `Pāli Class Sandhi`
    - Category: Site / heading. Confidence: low.

82. `docs/5-anki/field-lists/index.md:3` and `docs/5-anki/templates/index.md:3` — missing "to"; capitals.
    - Current: `Here the names correspond the names of the Note Type in Anki Decks`
    - Proposed: `The names here correspond to the names of the note types in the Anki decks.`
    - Category: Prose / grammar (on index pages). Confidence: high.

83. `docs/5-anki/templates/index.md:1`, `:7` — typo in the title; run-on sentence.
    - Current (`:1`): `# Card Templets for Note Types`
    - Proposed (`:1`): `# Card Templates for Note Types`
    - Current (`:7`): `[Styling](styling.md) is the same for all Types of Notes, only for [Pātimokkha word by word](pat-styling.md) it is different.`
    - Proposed (`:7`): `[Styling](styling.md) is the same for all note types except [Pātimokkha word by word](pat-styling.md), which has its own.`
    - Category: Prose / spelling, grammar. Confidence: high.

84. `docs/5-anki/general/special-fields.md:1` — the page title doesn't match the name every link uses ("Special Fields Add-on").
    - Current: `# Add-on special fields`
    - Proposed: `# Special Fields Add-on`
    - Category: Site / heading. Confidence: medium.

85. `docs/5-anki/7-daily_chants/sbs-daily-chanting-text.md:1` — the title names the deck "SBS Daily Chanting Sentences", but the deck page it links to is titled "SBS Daily Chanting - Anki Deck"; the title also ends in a full stop.
    - Current: `# Text for Anki deck [SBS Daily Chanting Sentences](1-sbs-daily-chanting.md).`
    - Proposed: `# Text for the Anki deck [SBS Daily Chanting](1-sbs-daily-chanting.md)`
    - Category: Site / heading. Confidence: low.

### Site checks with nothing to fix

- **Build warnings:** none. `temp/site-audit/build.log` has 0 `WARNING` lines; the coloured banner at the top is an upstream Material for MkDocs notice about MkDocs 2.0, not a warning about this site.
- **Nav vs files:** every nav entry in `mkdocs.yaml` points at an existing file (the nav is generated from digit-prefixed files). In-scope pages not in the nav are reached by links, except the orphans in Follow-ups.
- **Internal links and anchors:** `temp/site-audit/check_links.py` found no link to a missing file and no bad anchor. The only internal anchor link, `csv-update.md:41` → `updating.md#removing-outdated-words`, resolves. The script's only other output is the 75 empty links `[…]()` in `sbs-per-ex.md` (see Follow-ups).
- **Release downloads:** 49 of the 55 release-download and DPD links return 200. The 404s are in findings 72 and 73 and in Follow-ups (the four `other/` downloads).

## Follow-ups (not to be fixed here)

- **Orphaned pages.** These are built and published but have no nav entry and no inbound link: `docs/5-anki/other/test.md` (an older copy of `general/updating.md#removing-outdated-words`, with one extra section, "If it is not regular update"), `docs/5-anki/other/reading-common-pali-phrases.md` and `docs/5-anki/other/sbs-anumodana.md` (their `.apkg`, `.csv` and `.ods` release downloads all return 404), `docs/6-pali-class/sbs-per-ex.md` (linked only from an HTML comment in `1-pali-class-adv.md:13`; its 75 chapter links are all empty `()`), and `docs/6-pali-class/atth-hoti.md` (added 2026-05/06, no link to it). Whether to link, exclude from the build (`exclude_docs`), or leave them is an owner decision; deleting them would lose content, so none is proposed here.
- **HTML comments in `docs/6-pali-class/1-pali-class-adv.md:13` and `:65–79`.** Raw HTML (against the clean-Markdown rule). Comments are copied into the published page source, so the internal server path `\\FILESRV1\…` on line 69 is public in the HTML (it is also shown openly on `2-patimokkha-class.md`). Removing them would lose the draft links, so this needs an owner decision.
- **Chant translations to check against the SBS Recitations book** (`docs/5-anki/7-daily_chants/sbs-daily-chanting-text.md`), not changed here because the text quotes the book: `:184` "inspired by the Noble Ones Straightened - their offering" (capital mid-line), `:300` "Either equanimity or disgust become settled" (verb agreement), `:323` "I use the robe, Only to ward off cold" (capital after a comma), `:113` "Tripitaka". Also `docs/6-pali-class/sbs-per-analysis.md:56–57` call the chapters "…for Frequent Reflection" while their file names and `sbs-per-ex.md:57–58` say "Recollection".
- **`docs/5-anki/field-lists/index.md:15`** links "Phonetic Class" to `field-list-roots-class.md`. There is no phonetic field list. If the two note types share fields, this is correct; the owner should confirm.
- **`docs/6-pali-class/2-patimokkha-class.md:20`** says "there are two Anki decks available" but links only one deck page, and doesn't name the decks.
- **Russian pages** (`docs/5-anki/10-dps/1-ru-pali-vocab.md`, `ru-test.md`) are outside this English audit. Obvious typos seen: `1-ru-pali-vocab.md:5` "Удобрый интрумент" (→ "Удобный инструмент"); `ru-test.md:3` "Следовательно,устареашие" (→ "Следовательно, устаревшие"); `1-ru-pali-vocab.md:32` tells the user to pick the `.apkg` in the CSV import steps (the same error as finding 50). `ru-test.md` also has no H1 (it starts at `##`).
- **Pāḷi page names in `docs/7-notebook-lm.md:7`, `:15`, `:27`:** "Sutta Tipiṭaka" and "Vinaya Tipiṭaka" for what is usually called the Sutta Piṭaka and Vinaya Piṭaka. Left unchanged because it is a naming choice used consistently on that page.
- **Visual/CSS:** none found.

## Triage summary (LanguageTool)

`temp/site-audit/languagetool.tsv` has **689** data rows. Every row has a disposition in `temp/site-audit/triage.tsv` (columns: TSV row number, file, line, rule, matched text, disposition).

| Disposition | Rows |
|---|---|
| **Accepted** (merged into findings 8, 11, 15, 16, 20, 21, 27, 29, 31, 37, 43, 45, 47, 48, 51, 54–56, 58, 60–62, 64, 67) | 38 |
| Dropped: Pāḷi word or Pāḷi compound | 299 |
| Dropped: proper name or product name (Anki, AnkiWeb, MDict, GoldenDict, SuttaCentral, Ajahn, Bhante, …) | 131 |
| Dropped: Buddhist English loanword (suttas, devas, kamma, almsfood, uposatha, …) | 43 |
| Dropped: file name, extension, URL or code (`apkg`, `csv`, `sbs-per-analysis`, `href`, …) | 103 |
| Dropped: duplicate in a generated `index.md` (counted on its `.header.md`) | 13 |
| Dropped: whitespace with no visible effect (list indentation, line-break spaces, `nl2br`) | 25 |
| Dropped: quoted SBS book text (chant translations, chapter titles) | 4 |
| Dropped: inside an HTML comment (not rendered) | 3 |
| Dropped: non-English text (Russian; see Follow-ups) | 18 |
| Dropped: style suggestion, not an error | 12 |
| **Total** | 689 |

## Implementation check

*(Filled in by Phase 3.)*
