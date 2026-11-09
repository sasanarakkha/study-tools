# Deep Audit — `docs/6-pali-class/sbs-per-analysis/` (78 files)

Audit date: 2026-07-06, repo state: commit `762c5b1`, working tree clean.
Method: (a) scripted structural checks of every table row; (b) Pāḷi morphology heuristic (word ending vs. declared case/number/gender) over all rows, manually triaged; (c) full manual read of all 1,012 bold English translation lines; (d) nav-link/index chain verification.
Not covered exhaustively: gloss quality of every individual table row that passed the morphology heuristics.

## Instructions for the implementing model

- Line numbers refer to the files as of commit `762c5b1`. **Always match on the quoted text, not the line number alone**; verify with a grep before each Edit. If text differs, stop and report.
- `→` means replace the "current" text with the "suggested" text. Edits are within one line unless stated.
- Convention of these files: 4-column tables `| Pāli | POS | Grammar | English |` (5 columns with `Root` in `pubbakicca-analysis.md` and `post-patimokkha.md`). Plain lines = Pāḷi chant text; `**bold**` lines = English translation; rows whose Pāḷi ends in `-` are compound members (no case ending, Grammar cell usually empty).
- Do NOT change Pāḷi chant lines (data preservation) unless an item explicitly says so.
- Items under "DECISIONS NEEDED" (Part 8) must NOT be implemented without explicit user choice.
- After all edits, run the verification greps in Part 9.

---

## Part 1 — Text corruption: `m` → `ṃ` in English words (bad diacritic replacement)

A past replacement turned word-final English `m` into `ṃ`. Fix `ṃ` → `m` in these English glosses/translations only (never in Pāḷi):

| File:Line | Current | Fix |
|---|---|---|
| per-06-salutation-to-the-triple-gem.md:14 | POS `idioṃ` | `idiom` |
| per-19-anupubba-sikkha.md:95 | POS `idioṃ` | `idiom` |
| per-27-principles-of-cordiality.md:12 | POS `idioṃ` | `idiom` |
| per-27-principles-of-cordiality.md:119 | POS `idioṃ` | `idiom` |
| per-27-principles-of-cordiality.md:142 | POS `idioṃ` | `idiom` |
| per-40-anatta-lakkhana-sutta.md:52 | POS `idioṃ` | `idiom` |
| per-41-aditta-pariyaya-sutta.md:52 | POS `idioṃ` | `idiom` |
| per-41-aditta-pariyaya-sutta.md:63 | POS `idioṃ` | `idiom` (row also fixed in Part 3, item merges gloss) |
| per-41-aditta-pariyaya-sutta.md:177 | POS `idioṃ` | `idiom` |
| per-19-anupubba-sikkha.md:1123 | gloss `these, theṃ` | `these, them` |
| per-29-striving-according-to-the-dhamma.md:281 | gloss `of theṃ` | `of them` |
| per-54-ratana-sutta.md:74 | translation `protect theṃ` | `protect them` |
| per-22-the-noble-eightfold-path.md:336 | gloss `hiṃ` (row `| taṃ | pron | masc.acc.sg | hiṃ |`) | `him` |
| per-55-karaniya-metta-sutta.md:215 | gloss `that, hiṃ` | `that, him` |
| per-55-karaniya-metta-sutta.md:320 | gloss `to hiṃ` | `to him` |
| per-23-mindfulness-of-breathing.md:87 | translation `in front of hiṃ` | `in front of him` |
| per-33-universal-well-being.md:20 | gloss `calṃ lit. not trembling` | `calm, lit. not trembling` |
| per-33-universal-well-being.md:46 | gloss `calṃ lit. not trembling` | `calm, lit. not trembling` |
| per-23-mindfulness-of-breathing.md:220 | gloss `causing to be calṃ` | `causing to be calm` |
| per-54-ratana-sutta.md:128 | gloss `firṃ attentive` | `firm, attentive` |
| per-40-anatta-lakkhana-sutta.md:353 | gloss `in forṃ` | `in form` |
| per-37-the-thirty-two-parts.md:57 | gloss `phlegṃ` | `phlegm` |
| per-55-karaniya-metta-sutta.md:232 | gloss `…unease, probleṃ` | `…unease, problem` (row also merged in Part 3) |

## Part 2 — Column-shifted rows (POS cell empty, values slid right)

Pattern: `| word | | noun | m.ac.s gloss… |` — POS is empty, "noun" sits in Grammar, and an abbreviated grammar tag is glued to the front of the English gloss. Rebuild each row as shown (grammar abbreviations expanded to the corpus standard):

| File:Line | Corrected full row |
|---|---|
| per-06-salutation-to-the-triple-gem.md:158 | `\| saṅghaṃ \| noun \| masc.acc.sg \| Community, assembly \|` |
| per-06-salutation-to-the-triple-gem.md:366 | `\| sāvakesu \| noun \| masc.loc.pl \| among disciples, pupils, lit. hearers \|` |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:245 | `\| dukkhaṃ \| noun \| nt.nom.sg \| discomfort, suffering, pain, unease, something unsatisfactory, problem, trouble \|` (original embedded tag said `nt.ac.s`, but in `idaṃ kho pana … dukkhaṃ ariya-saccaṃ` it is nominative, matching `ariyasaccaṃ'ti nt.nom.sg` on the next row) |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:247 | `\| me \| pron \| 1.dat.sg \| to me, for me \|` |
| per-19-anupubba-sikkha.md:588 | `\| cīvarena \| noun \| nt.ins.sg \| with robe \|` (embedded tag said `m.ins.s`; cīvara is neuter) |
| per-19-anupubba-sikkha.md:623 | `\| cīvarena \| noun \| nt.ins.sg \| with robe \|` (same) |
| per-19-anupubba-sikkha.md:876 | `\| pādaṃ \| noun \| masc.acc.sg \| foot \|` |
| per-28-principles-of-non-decline.md:230 | `\| pāṭikaṅkhā \| adj \| fem.nom.sg \| to be expected (for), certain (for), should be expected, can be anticipated \|` |
| per-34-the-divine-abidings.md:51 | `\| sabbāvantaṃ \| adj \| masc.acc.sg \| entire, whole \|` |
| per-34-the-divine-abidings.md:59 | `\| abyāpajjena \| adj \| nt.ins.sg \| without ill will, with goodwill \|` |
| per-41-aditta-pariyaya-sutta.md:76 | `\| jātiyā \| noun \| fem.ins.sg \| with birth, rebirth, conception \|` |
| per-66-vipassana-bhumi-patho.md:94 | `\| dukkhaṃ \| noun \| nt.nom.sg \| discomfort, suffering, pain, unease, something unsatisfactory, problem, trouble \|` (embedded `nt.ac.s`; nominative in `idaṃ … dukkhaṃ`-type list — verify against the chant line above it) |
| per-66-vipassana-bhumi-patho.md:97 | `\| dukkhanirodho \| noun \| masc.nom.sg \| cessation of suffering, disappearance of suffering \|` |
| per-68-adasi-me-adi-gatha.md:45 | `\| petānam- \| adj \| masc.gen.pl \| of departed, deceased, dead \|` |
| per-19-anupubba-sikkha.md:618 | `\| evameva kho \| ind \| \| in the same way \|` (currently `\| evameva \| kho \| ind \| in the same way \|` — the particle `kho` slid into the POS cell; it belongs to the Pāḷi lemma) |

## Part 3 — Glosses split across the Grammar and English columns

Pattern: a long gloss was split at a `\|`, its first half sits in the Grammar column. Fix: Grammar cell becomes empty (compound members) or the correct tag; the halves are joined in the English cell. Corrected rows:

| File:Line | Corrected full row |
|---|---|
| per-06-salutation-to-the-triple-gem.md:269 | `\| dukkha- \| noun \| \| discomfort, suffering, pain, unease, something unsatisfactory, problem, trouble \|` |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:136 | `\| dukkha- \| noun \| \| discomfort, suffering, pain, unease, something unsatisfactory, problem, trouble \|` |
| per-43-ratanattayanubhavadi-gatha.md:19 | `\| dukkha- \| noun \| \| discomfort, suffering, pain, unease, something unsatisfactory, problem, trouble \|` |
| per-45-culla-mangala-cakka-vala.md:86 | `\| dukkha- \| noun \| \| discomfort, suffering, pain, unease, something unsatisfactory, problem, trouble \|` |
| per-16-miscellaneous-verses.md:72 | `\| pubbe \| ind \| \| before, previously, formerly, in the past, in a previous life \|` |
| per-16-miscellaneous-verses.md:150 | `\| khaṇ'ātītā \| adj \| masc.nom.pl \| who has missed the chance, who lost the opportunity, lit. moment passed by \|` |
| per-17-a-single-excellent-night.md:34 | `\| tattha tattha \| ind \| adv \| right there, here and now, in each and every case, lit. there and there \|` |
| per-19-anupubba-sikkha.md:378 | `\| kālena \| ind \| adv \| timely, at the right moment, at a suitable time, at the proper time \|` |
| per-19-anupubba-sikkha.md:421 | `\| vilepana- \| noun \| \| oil, unguent, ointment, cosmetics, make-up, perfume \|` |
| per-19-anupubba-sikkha.md:560 | `\| ukkoṭana- \| noun \| \| taking bribes, bribery, corruption, crooked dealing \|` |
| per-19-anupubba-sikkha.md:1168 | `\| khaya- \| noun \| \| exhaustion (of), extinction (of), depletion (of), annihilation (of), destruction (of) \|` |
| per-22-the-noble-eightfold-path.md:47 | `\| dukkhanirodha- \| noun \| \| cessation of suffering, disappearance of suffering \|` |
| per-22-the-noble-eightfold-path.md:67 | `\| abyāpāda- \| noun \| \| goodwill, kindness, friendliness, benevolence, lit. not ill-will \|` |
| per-22-the-noble-eightfold-path.md:359 | `\| pubb'eva \| ind \| \| just in front of, just before, previous, as before, as earlier \|` |
| per-22-the-noble-eightfold-path.md:363 | `\| upekkhā- \| noun \| \| mental poise, mental balance, equanimity, composure \|` |
| per-22-the-noble-eightfold-path.md:364 | `\| sati- \| noun \| \| mindfulness, presence, recollection, awareness \|` |
| per-24-dependent-origination.md:45 | `\| dukkhadomanass- \| noun \| \| pain and stress, physical pain and mental suffering \|` |
| per-24-dependent-origination.md:84 | `\| dukkhanirodha- \| noun \| \| cessation of suffering, disappearance of suffering \|` |
| per-24-dependent-origination.md:383 | `\| duvidhena \| ind \| adv \| in two ways; as of two kinds; in a twofold way \|` (also drop the stray `–` after the Pāḷi word) |
| per-24-dependent-origination.md:579 | `\| diṭṭhi- \| noun \| \| view, belief, opinion, concept, theory, attitude \|` (drop the duplicated "opinion") |
| per-27-principles-of-cordiality.md:80 | `\| antamaso \| ind \| \| even so much as, even with, even down to, with as little as \|` |
| per-27-principles-of-cordiality.md:82 | `\| pariyāpanna- \| adj \| \| gone completely into, included in, belonging to, got into \|` (also drop the stray `”`) |
| per-27-principles-of-cordiality.md:89 | `\| appaṭivibhatta- \| adj \| \| not dividing for oneself, without reservations, not without sharing with others \|` (also fixes typo "onself") |
| per-27-principles-of-cordiality.md:111 | `\| samādhi- \| noun \| \| perfect peace of mind, stability of mind, stillness of mind \|` |
| per-27-principles-of-cordiality.md:138 | `\| diṭṭhi- \| noun \| \| view, belief, opinion, concept, theory, attitude \|` (drop duplicated "opinion") |
| per-28-principles-of-non-decline.md:82 | `\| yathā- \| ind \| \| like, as, according to, on account of, because of, how \|` |
| per-30-the-buddhas-final-instruction.md:52 | `\| accayena \| ind \| \| after the passing (of), after the lapse (of), lit. with gone past \|` |
| per-31-the-four-requisites.md:93 | `\| utuparissaya- \| noun \| \| inclement weather, harsh climate, lit. danger of the season \|` |
| per-31-the-four-requisites.md:95 | `\| paṭisallāna- \| noun \| \| privacy, seclusion, solitude, lit. sticking to oneself \|` |
| per-31-the-four-requisites.md:96 | `\| ārāma- \| noun \| \| enjoyment, delight, pleasure \|` (current has corrupted "pleasureenjoyment" in Grammar + "delight, pleasure" in English) |
| per-36-…-gone-forth.md:28 | `\| vevaṇṇiya- \| adj \| \| state of having no caste, who change appearance, social order; lit. discoloured \|` |
| per-47-kala-dana-sutta-gatha.md:15 | `\| kālena \| ind \| adv \| timely, at the right moment, at a suitable time, at the proper time \|` |
| per-47-kala-dana-sutta-gatha.md:54 | `\| appaṭivāna- \| adj \| \| with confidence, without regret, lit. not shrinking back \|` |
| per-49-deva-aradhanai.md:66 | `\| sādhavo \| ind \| \| accomplishing, fulfilling, effecting, completing, with approval \|` (see also Part 8 D6 — `sādhavo` looks like masc.nom.pl "good ones"; verify) |
| per-53-mangala-sutta.md:257 | `\| nibbāna- \| noun \| \| going out (of a lamp), extinguishment (of a fire), quenching, peace \|` |
| per-54-ratana-sutta.md:110 | `\| suvatthi \| noun \| fem.nom.sg \| safety, well-being, blessing; su+[v]+√as+ti \|` (grammar cell held the gloss; root note kept at end) |
| per-54-ratana-sutta.md:420 | same fix as :110 (identical row later in file) |
| per-54-ratana-sutta.md:203 | `\| gotama- \| adj \| \| family name of the Buddha; lit. of the Gotama clan \|` |
| per-54-ratana-sutta.md:394 | `\| viratta- \| pp \| \| detached (from); without desire (for); become indifferent (to); lost interest (in) \|` |
| per-62-jaya-mangala-attha-gatha.md:47 | `\| akkhama- \| adj \| \| impatient (with), intolerant (of), not able to endure \|` |
| per-62-jaya-mangala-attha-gatha.md:100 | `\| yojana- \| noun \| \| measure of length; approximately twenty kilometres \|` |
| per-62-jaya-mangala-attha-gatha.md:153 | `\| abhiropita- \| adj \| \| put on top, placed, (of an argument) refuted, debunked, disproved \|` |
| per-62-jaya-mangala-attha-gatha.md:157 | `\| paññā- \| noun \| \| wisdom, knowledge, intelligence, intellect, understanding, insight \|` |
| per-65-dhamma-sangani-matika.md:46 | `\| upādinna- \| pp \| \| grasped, clung to, attached to, taken as "mine", acquired \|` |
| per-65-dhamma-sangani-matika.md:48 | `\| anupādinna- \| pp \| \| not grasped, not clung to, not attached to, not taken as "mine", not acquired \|` |
| per-71-sharing-of-all-merits.md:100 | `\| anumodana- \| noun \| \| rejoicing, satisfaction, thanks, appreciation, blessing, thanksgiving \|` |
| per-41-aditta-pariyaya-sutta.md:63 | `\| tam'pi \| idiom \| \| that too, he too, even that, just that, that very thing \|` |
| per-28-principles-of-non-decline.md:174 | `\| kinti \| ind \| interr \| how then? in what way? \|` (Grammar had truncated `inter`) |
| per-49-deva-aradhanai.md:67 | `\| me \| pron \| 1.dat.sg \| for me \|` (current: Grammar `1.imp.sg`, gloss `ny be` — both corrupted; `bhaṇantu me` = "may they recite for me") |

---

## Part 4 — Grammar-tag corrections (morphology verified)

Change only the Grammar cell (and gloss where noted):

| File:Line | Word | Current | Suggested | Reason |
|---|---|---|---|---|
| per-05-homage-to-the-sangha.md:59 | cattāri | masc.nom.pl | nt.nom.pl | agrees with neuter `purisayugāni` |
| per-57-buddha-dhamma-sangha-guna.md:61 | cattāri | masc.nom.pl | nt.nom.pl | same passage |
| per-06-salutation-to-the-triple-gem.md:250 | jānāma | pr.3.pl | pr.1.pl | "we know" is 1st person |
| per-07-the-buddhas-first-exclamation.md:50 | ajjhagā | imper.3.sg | aor.3.sg | aorist "he attained", not imperative |
| per-54-ratana-sutta.md:126 | ajjhagā | imperf.3.sg | aor.3.sg | same form |
| per-13-from-the-elder-ratthapala.md:42 | vatthehi | nt.ins.sg | nt.ins.pl | `-ehi` is plural |
| per-14-from-the-elder-parapariya.md:232 | pacchimo | masc.nom.pl | masc.nom.sg | `-o` is singular |
| per-16-miscellaneous-verses.md:149 | upaccagā | imp.3.sg | aor.3.sg | aorist "it passed by" |
| per-16-miscellaneous-verses.md:261 | ayaṃ | POS `noun` | POS `pron` | demonstrative pronoun (Grammar fem.nom.sg is correct) |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:387 | sadevamanussāya | masc.loc.sg | fem.loc.sg | agrees with fem. `pajāya` |
| per-19-anupubba-sikkha.md:1057 | kusalesu | masc.loc.sg | masc.loc.pl | `-esu` is plural |
| per-19-anupubba-sikkha.md:1058 | dhammesu | masc.loc.sg | masc.loc.pl | `-esu` is plural |
| per-19-anupubba-sikkha.md:830 | viharāhi | imp.sg.sg | imp.2.sg | typo `sg.sg` |
| per-22-the-noble-eightfold-path.md:236 | citte | masc.loc.pl | nt.loc.sg | citta is neuter; loc. singular |
| per-23-mindfulness-of-breathing.md:44 | paripūreti | pr.3.pl | pr.3.sg | 3.sg form; also fix gloss "fill up" → "fills up" |
| per-23-mindfulness-of-breathing.md:107 | assasāmī'ti | pr.3.sg | pr.1.sg | "-āmi" = 1st sg ("I breathe in") |
| per-23-mindfulness-of-breathing.md:118 | passasāmī'ti | pr.3.sg | pr.1.sg | same; also gloss "I breathes out" → "I breathe out" |
| per-23-mindfulness-of-breathing.md:131 | assasāmī'ti | pr.3.sg | pr.1.sg | same |
| per-23-mindfulness-of-breathing.md:142 | passasāmī'ti | pr.3.sg | pr.1.sg | same |
| per-23-mindfulness-of-breathing.md:154 | assasissāmī'ti | fut.3.sg | fut.1.sg | "-ssāmi" = 1st sg |
| per-23-mindfulness-of-breathing.md:164 | passasissāmī'ti | fut.3.sg | fut.1.sg | same |
| per-23-mindfulness-of-breathing.md:176 | assasissāmī'ti | fut.3.sg | fut.1.sg | same |
| per-23-mindfulness-of-breathing.md:186 | passasissāmī'ti | fut.3.sg | fut.1.sg | same |
| per-31-the-four-requisites.md:118 | paramatāyā | masc.dat.sg | fem.dat.sg | paramatā is feminine |
| per-36-…-gone-forth.md:66 | upavadatī'ti | pr.3.pl | pr.3.sg | `-ti` singular; gloss is singular too |
| per-37-the-thirty-two-parts.md:33 | atthi | pres.3.pl | pr.3.sg | normalize `pres`; atthi is 3.sg (used with plural list) |
| per-39-dhammacakkappavattana-sutta.md:21 | isipatane | (English cell empty) | add gloss `in Isipatana` | missing gloss |
| per-39-dhammacakkappavattana-sutta.md:22 | migadāye | masc.gen.sg, English empty | masc.loc.sg + gloss `in the Deer Park` | locative; missing gloss |
| per-40-anatta-lakkhana-sutta.md:12 | me | masc.ins.sg | 1.ins.sg | personal pronoun convention (digit person) |
| per-41-aditta-pariyaya-sutta.md:13 | me | masc.ins.sg | 1.ins.sg | same |
| per-53-mangala-sutta.md:11 | me | masc.ins.sg | 1.ins.sg | same |
| per-40-anatta-lakkhana-sutta.md:13 | sutaṃ | masc.acc.sg | nt.nom.sg | `evaṃ me sutaṃ` = "thus it was heard by me" (pp as nt. subject) |
| per-41-aditta-pariyaya-sutta.md:14 | sutaṃ | masc.acc.sg | nt.nom.sg | same |
| per-53-mangala-sutta.md:12 | sutaṃ | masc.acc.sg | nt.nom.sg | same |
| per-41-aditta-pariyaya-sutta.md:74 | dos'agginā | nt.ins.sg | masc.ins.sg | aggi is masculine; also fix `hate , aversion` → `hate, aversion` |
| per-41-aditta-pariyaya-sutta.md:79 | sokehi | masc.ins.sg | masc.ins.pl | `-ehi` plural |
| per-41-aditta-pariyaya-sutta.md:80 | paridevehi | masc.ins.sg | masc.ins.pl | `-ehi` plural |
| per-42-yatha-vari-vaha.md:91 | vinassatu | pr.3.sg | imp.3.sg | `-tu` imperative ("may it disappear") |
| per-51-nama-kara-siddhi-gatha.md:47 | hotu | pr.3.sg | imp.3.sg | `-tu` imperative |
| per-51-nama-kara-siddhi-gatha.md:44 | te | masc.dat.sg | 2.dat.sg | "for you" = 2nd person pronoun |
| per-59-bojjhanga-parittam.md:58 | te | masc.dat.sg | 2.dat.sg | same |
| per-63-jaya-parittam.md:33 | te | masc.dat.sg | 2.dat.sg | same |
| per-16-miscellaneous-verses.md:221 | tumhehi | masc.ins.pl | 2.ins.pl | personal pronoun |
| per-29-striving-according-to-the-dhamma.md:284 | amhesu | masc.loc.sg | 1.loc.pl | "in us", plural |
| per-70-sharing-and-aspirations.md:89 | me | masc.ins.sg | 1.ins.sg | personal pronoun |
| per-70-sharing-and-aspirations.md:185 | me | masc.gen.sg | 1.gen.sg | personal pronoun |
| per-53-mangala-sutta.md:80 | brūhi | imp.3.sg | imp.2.sg | "you speak" is 2nd person |
| per-54-ratana-sutta.md:202 | nikkāmino | masc.ins.sg | masc.nom.pl | nom. pl. agreeing with `ye … nikkāmino`; gloss stays |
| per-55-karaniya-metta-sutta.md:125 | atthi | pr.3.pl | pr.3.sg | atthi is singular (used distributively: "there are") |
| per-55-karaniya-metta-sutta.md:260 | bhūtesu | masc.loc.sg | masc.loc.pl | `-esu` plural |
| per-55-karaniya-metta-sutta.md:339 | āhu | pref.p.3.pl | perf.3.pl | typo `pref.p` |
| per-63-jaya-parittam.md:46 | sakyānaṃ | masc.gen.sg | masc.gen.pl | `-ānaṃ` plural |
| per-63-jaya-parittam.md:52 | hohi | pr.2.sg | imp.2.sg | imperative "may you be" |
| per-70-sharing-and-aspirations.md:99 | dentu | pr.3.pl | imp.3.pl | `-ntu` imperative ("may they give") |
| pubbakicca-analysis.md:130 | bhikkhūnaṃ | masc.gen.sg | masc.gen.pl | `-ūnaṃ` plural |
| per-29-striving-according-to-the-dhamma.md:286 | bhavissanti | POS `pt` | POS `verb` | Grammar fut.3.pl already correct |
| per-15-on-protection.md:15 | bhaṇāmase | imp.reflx.3.pl | imp.refl.1.pl | "let us chant" = 1st person (cf. per-06:19 tagged 1.pl) |
| per-72-sharing-of-merits-with-the-departed.md:18 | ñātinaṃ | nom.dat.pl | masc.dat.pl | garbled case tag |
| per-09-going-to-true-and-false-refuges.md:80 | ariyaṃ- | nom.acc.sg | masc.acc.sg | garbled case tag (`ariyaṃ … maggaṃ`) |
| per-01-dedication-of-offerings.md:46 | mayaṃ | 1.nom. | 1.nom.pl | number missing |
| per-53-mangala-sutta.md:60 | gāthāya | fem.ins | fem.ins.sg | number missing |
| per-71-sharing-of-all-merits.md:22 | bhāgino | masc.nom.p | masc.nom.pl | truncated |
| per-74-the-highest-honour-and-aspirations.md:46 | me | 1.g.sg | 1.gen.sg | truncated |
| per-27-principles-of-cordiality.md:157 | cha | Grammar `pl` | x.nom.pl | match corpus numeral convention |

---

## Part 5 — Notation standardization (bulk, best done by a temp script)

Canonical Grammar scheme used by the overwhelming majority of the corpus:
`masc|fem|nt|x . nom|acc|ins|dat|abl|gen|loc|voc . sg|pl` for nominals; `pr|aor|fut|opt|imp|cond|perf . 1|2|3 . sg|pl` (with optional `refl`/`pass`/`caus` after the tense: e.g. `pr.refl.3.sg`) for verbs; digit person (`1.`/`2.`) for personal pronouns.

Apply these replacements **in the Grammar column (3rd cell) only** (5-column files: also 3rd cell):

1. `1st` → `1`, `2nd` → `2`, `3rd` → `3` (≈35 hits, mostly pubbakicca-analysis.md; also per-30:12,14,29; per-52:36; per-36 several)
2. `instr` → `ins`, `inst` → `ins` (≈25 hits; e.g. per-01:91, per-06:178, per-20:42, per-22:190, per-36:125, per-62:125, pubbakicca many)
3. `reflx` → `refl`, `reflex` → `refl`, and standalone `ref` → `refl`; order mood-first: `ref.imp.1.pl` → `imp.refl.1.pl`, `ref.pr.1.pl`/`imp.ref.pr.1.pl` → `imp.refl.1.pl`, `reflex.opt.3.sg` → `opt.refl.3.sg`, `opt.3.sg refl` → `opt.refl.3.sg`, `imp.ref.2.sg` → `imp.refl.2.sg`, `opt.ref.3.sg`/`opt.ref.1.sg` → `opt.refl.3.sg`/`opt.refl.1.sg`. Note: `karomase` is tagged 4 different ways across per-02:19, per-03:13, per-04:13, per-05:13, post-patimokkha.md:19 — standardize all five to `imp.refl.1.pl`.
4. `emphat` / `emph.` / `emp` → `emph` (per-01:79, per-15:11, +1)
5. `pres` → `pr` (per-37:33 — see Part 4)
6. Compressed one-letter tags → full form: `m.n.s`→`masc.nom.sg` (per-06:329,331,333,335,337); `m.ac.s`→`masc.acc.sg` (per-06:301); `f.n.sg`→`fem.nom.sg` (per-06:258); `nt.n.s`→`nt.nom.sg` (per-14:36,40); `m.abl.s`→`masc.abl.sg` (per-66:167); `m.acc.sg`→`masc.acc.sg` (per-18:168); `nt.i.sg`→`nt.ins.sg` (per-34:13,14); `masc.v.sg`→`masc.voc.sg` (per-40:285); `masc.v.pl`→`masc.voc.pl` (per-54:48); `fem.v.sg`→`fem.voc.sg` (per-25:66)
7. Strip trailing periods from tags: `nt.acc.sg.`, `nt.nom.sg.`, `masc.instr.sg.`, `adv.`, `masc.`→`masc`, `nt.`→`nt`, `fem.`→`fem` (compound-member bare-gender tags: keep the bare gender, drop the dot — ≈45 hits)
8. Composite POS values split into POS+Grammar: per-40:188 `verbinf` → POS `verb`, Grammar `inf`; per-18:391 `verbaor.1.s` → POS `verb`, Grammar `aor.1.sg`; per-63:53 `verbimp.reflx.2.s` → POS `verb`, Grammar `imp.refl.2.sg`
9. `v.pass` POS (per-40:59,83,362; per-41:220) → POS `verb`, prepend `pass.` into Grammar if empty, else add `pass`; `v.caus` POS (per-19:809,994; per-23:85; per-31:63; per-54:49) → POS `verb` + `caus` in Grammar; `v.refl` (per-56:98) → POS `verb` + `refl` in Grammar; `prp.caus` (per-23:173,183) → POS `prp`, add `caus` to Grammar
10. `neg`, `conj`, `interr`, `prep`, `card`, `adv` appearing in the POS column where the corpus normally puts them in Grammar with POS `ind` (e.g. per-14:83,103,122,148 `neg`/`conj`) → POS `ind`, move the word to Grammar
11. `1.imp.sg` (per-49:67 — already rebuilt in Part 3); `from loc.sg` (per-18:248) → `adv`; `from loc. sg.` (per-16:79) → `adv`; `from ger` (per-16:239) → `ger`
12. `fem nom pl` (spaces) → `fem.nom.pl` — locate with `grep -rn "fem nom pl" *.md`

---

## Part 6 — English translation/gloss typos (mechanical, safe)

Fix in place (translation lines are the `**bold**` lines; glosses are 4th cells):

| File:Line | Current → Suggested |
|---|---|
| per-01:159 | `I venerate to the Teaching.` → `I venerate the Teaching.` |
| per-01:78, per-06:470 | `who's fire is out` → `whose fire is out` |
| per-01:11,76 | `Fortunate One the Buddha` → `Fortunate One, the Buddha` |
| per-01:13,126 | `totally perfectly` → `totally, perfectly` |
| per-01:88 | `latest , later` → `latest, later` |
| per-03:75 | `himself  higher understanding` → `himself higher understanding` (double space) |
| per-03:119 | `my head  to` → `my head to` |
| per-06:140 | `those who seen the peace` → `those who have seen the peace` |
| per-06:355 | `during his live` → `during his life` |
| per-06:499 | `under  the` → `under the` |
| per-08:80 | `ripening , resulting` → `ripening, resulting` |
| per-09:47 | `not secure , this` → `not secure, this` |
| per-10:49 | `Patient and forgiveness` → `Patience and forgiveness`; `not onegone forth` → `not one gone forth` |
| per-11:92 | `well preached , well-taught` → `well preached, well-taught` |
| per-13:25 | `diseased, . There` → `diseased. There` |
| per-13:65 | `fora seeker` → `for a seeker` |
| per-13:80 | `fora seeker ofthe` → `for a seeker of the` |
| per-13:133 | `desire , not free` → `desire, not free` |
| per-14:44 | `(their robs)` → `(their robes)` |
| per-14:124 | `at the foots of trees` → `at the feet of trees` |
| per-16:266 | `There are these foots of a tree` → `There are these roots of trees` (check the table rows above for the same wording) |
| per-19:25 | `ouseholder or householder's son` → `Householder or householder's son` |
| per-19:57 | `dirty , lit:` → `dirty, lit:` |
| per-19:271 | `false speech , lit.` → `false speech, lit.` |
| per-19:331 | `he is reconciler those who are divided` → `he is a reconciler of those who are divided` |
| per-19:783 | `you should take a food` → `you should take food` |
| per-19:817, per-31:71 | `assistance of holy live` → `assistance of the holy life`; `put an end of former` → `put an end to former`; `a new (painful) sensations` / `a new (painfull) sensations` → `new (painful) sensations`; per-31:71 also `(painfull)` → `(painful)` (2×) |
| per-19:996 | `Afternoon, he returned` → `In the afternoon, he returned` |
| per-19:1142 | `he reaching and dwells` → `he reaches and dwells` |
| per-21:150 | `there is effort arises without sluggishness` → `effort arises without sluggishness` |
| per-21:186 | `with relaxed body and who at ease` → `with relaxed body and at ease` |
| per-22:152,165,176,193 | `he exerts oneself` → `he exerts himself` |
| per-22:230 | `a monk stay with` → `a monk stays with` |
| per-22:252 | `this moks is called` → `this monks is called` |
| per-22:295,316,347,371 | `he attaining and remains` → `he attains and remains` |
| per-22:213 | `strenuous , with` → `strenuous, with` |
| per-23:32 | `it is fills up` → `it fills up` |
| per-23:110,121,134,145 | `I'm breath in deeply.` / `I'm breath out deeply.` / `…shortly.` → `I breathe in deeply.` / `I breathe out deeply.` / `…shortly.` |
| per-23:213 | `breathe out experiences mental activity` → `breathe out experiencing mental activity` |
| per-23:231 | `breathe in experiences the mind` and `breathe out experiences the mind` → `experiencing` (2×) |
| per-24:49, per-66:145 | `becoming arise` → `becoming arises`; `birth arise` → `birth arises` |
| per-24:164 | `the sphere of the sphere of the formless` → `the sphere of the formless` |
| per-24:456 | `non-perseption` → `non-perception` |
| per-24:597,624 | `of one who endowed with` → `of one who is endowed with` |
| per-24:699 | `for affected by` → `for one affected by`; `for endowed all kinds` → `for one endowed with all kinds`; `for affected by all kinds` → `for one affected by all kinds` |
| per-25:30 | `Bhessed One` → `Blessed One` (3×) |
| per-25:43 | `whatever , that which` → `whatever, that which` |
| per-26:44 | `Here a monks could say` → `Here a monk could say` |
| per-26:65,91,95 | `certan` → `certain` (3×); `heared` → `heard` (3×) |
| per-27:68 | `for a monks` → `for a monk` |
| per-28:63 | `perferm` → `perform` |
| per-28:88 | `as they has beed formulated` → `as they have been formulated` |
| per-28:220 | `seven seven principles` → `seven principles` |
| per-29:47 | `to arose energy` → `to arouse energy` |
| per-29:289 | `grate result and grate merit` → `great result and great merit` |
| per-30:79 | `condition phenomena are of the liable to disintegrate` → `conditioned phenomena are liable to disintegrate`; `This is final statement` → `This is the final statement` |
| per-31:32,99 | `for ward off heat, for ward off the touch` → `to ward off heat, to ward off the touch` |
| per-31:99 | `for the sake of removal the danger` → `for the sake of removal of the danger` |
| per-32:18 | `of living , abiding` → `of living, abiding` |
| per-32:29 | `does not drawn towards it` → `is not drawn towards it` |
| per-33:71 | `may all beings do not lost gained fortune` → `may all beings not lose their gained fortune` |
| per-35:30 | `of the nature to sick` → `of the nature to sicken` |
| per-35:55, per-36:88 | `from all that dear and pleasing` → `from all that is dear and pleasing` |
| per-36:22 | `these are ten principles should often be reflected` → `these ten principles should often be reflected` |
| per-36:148 | `these is ten principles should often be reflected` → `these ten principles should often be reflected` |
| per-36:104 | `How my days and nights pass?` → `How do my days and nights pass?` |
| per-38:113 | `on the the ground` → `on the ground` |
| per-40:19 | `in jetavana (jets's grove)` → `in Jetavana (Jeta's grove)` |
| per-40:23 | `in sāvatthi in jets's grove in anāthapindika's park` → `in Sāvatthī in Jeta's Grove in Anāthapiṇḍika's park` |
| per-40:72,94,107,124 | `than form/feeling/perception/volitional formations could not` → `then …` (4×) |
| per-40:59,72,94,107,124,137 | `onself` → `oneself` |
| per-40:287 | `something , anything` → `something, anything` |
| per-40:419, per-41:277 | `throught not grasping` → `through not grasping` |
| per-41:243 | `What have to be done – is done` → `What has to be done – is done` |
| per-42:43 | `May your desires and wishes be succeeds only quickly.` → `May your desires and wishes succeed quickly.` |
| per-42:104 | `May danger does not be for you.` → `May there be no danger for you.` |
| per-45:47 | `ny the power` → `by the power` |
| per-45:133 | `May be f or you` → `May there be for you` |
| per-52:41 | `Tiple Gem` → `Triple Gem`; `succseed` → `succeed` |
| per-53:84 | `tall about highest blessing` → `tell about the highest blessing` |
| per-54:373 | `knower the best , who` → `knower of the best, who` |
| per-55:174 | `whoever , that which` → `whoever, that which` |
| per-55:226 | `(throught)` → `(through)` |
| per-55:235 | `one to anothershould not wish` → `one to another should not wish` |
| per-59:48 | `which has been thoroughly told by the sage who understand` → `which have been thoroughly told by the sage who understands` |
| per-65:126,134 | `exhalted` → `exalted` |
| per-65:200 | `internal and external dhamams` → `internal and external dhammas` |
| per-65:62 | `dhammas neither defiled and subject to defilements` → `dhammas neither defiled nor subject to defilements` |
| per-66:86 | `the I am knowing the unknown' faculty` → `the 'I am knowing the unknown' faculty` |
| per-67:32 | `there is not , there not exists` → `there is not, there does not exist` |
| per-68:69 | `it is benefits immediately` → `it benefits immediately` |
| per-70:56 | `Indras , kings` → `Indras, kings` |
| per-70:187,230 | `may Maras do not get a chance` → `may Māras not get a chance` (2×) |
| per-71:69 | `Beings lives in the world` → `Beings live in the world` |
| per-71:90 | `sharing of merrit` → `sharing of merit` |
| per-74:61 | `a assembly` → `an assembly` |

Do NOT change: per-19:592,607,634 `lit. wherever wherever` — intentional literal rendering of reduplicated `yena yeneva`.

---

## Part 7 — Content errors (translation contradicts the Pāḷi) — review each

1. **per-18:331** — Pāḷi (L325) is `dukkha-nirodho … sacchikatan-ti`, but translation says "this noble truth of the **origin** of suffering has been personally experienced." → "this noble truth of the **cessation** of suffering has been personally experienced."
2. **per-18:343** — Pāḷi (L337) is `dukkha-nirodha-gāminī-paṭipadā … bhāvetabban-ti`, translation says "this noble truth of the **cessation of suffering** should be developed." → "this noble truth of the **way leading to the cessation of suffering** should be developed."
3. **per-18:351** — Pāḷi (L345) is `dukkha-nirodha-gāminī-paṭipadā … bhāvitan-ti`, translation says "this noble truth of the **origin of suffering** has been developed." → "this noble truth of the **way leading to the cessation of suffering** has been developed."
4. **per-18:335** — `the noble truth of the the way` → `the noble truth of the way` (doubled word, same section).
5. **per-40:264** — Pāḷi is `viññāṇaṃ niccaṃ vā aniccaṃ vā'ti`; translation "Is **conscience** permanent or impermanent?" → "Is **consciousness** permanent or impermanent?"
6. **per-22:176** — third right-effort clause: translation says "generates intention for the **arising** of unarisen **worthless, unskilful** states of mind". The Pāḷi for this clause is `anuppannānaṃ kusalānaṃ dhammānaṃ uppādāya` (check table above the line) → "…arising of unarisen **wholesome, skillful** states of mind."
7. **per-41:41** — "Monks, everything is burning? And what is everything what is burning?" → "Monks, everything is burning. And what is the everything that is burning?"

---

## Part 8 — DECISIONS NEEDED (do not implement without user approval)

- **D1 per-37-the-thirty-two-parts.md** — the chant line (L29) lists `matthaluṅgan'ti` once (at the end), but the table has TWO `matthaluṅgaṃ` rows (L55 after `karīsaṃ`, and L68 at the end) and the translation (L70) says "brain" twice. Recommend: delete the L55 row and the first "brain" in L70. Deleting a row touches the docs/ data-preservation rule, hence approval needed.
- **D2 per-49-deva-aradhanai.md** — file name and title `Devā-ārādhanāi` carry a stray trailing `i` (standard name: `Devā-ārādhanā`). Renaming the file requires updating nav links in per-48/per-50 and the index + feedback URL param. Recommend: fix the visible title only, keep the filename.
- **D3 `<br>` inside tables** (per-01:77, per-06, per-13, per-52, per-62, pubbakicca) vs. the project "no raw HTML in sources" rule. `<br>`-in-table is hard to replace in pure Markdown. Recommend: keep, but note the exception in the project docs, or convert `A<br>(or)<br>B` cells to `A (or) B`.
- **D4 POS conventions to unify** (pick one form each): `pp as adj` vs `pp/noun`; `adj as noun` vs `adj (as noun)` vs `adj (or as noun)`; numerals tagged `card` in some files but `adj` in others (recommend `card`); multi-word entries tagged `v + pn` (per-19:774), `ind+pn` (per-26:173), `ind+m+imp` (per-16:256), `adv+ind` (per-50:18,26) — recommend `idiom` or `sandhi` per corpus convention. The `x.` gender prefix for numerals (`x.nom.pl` etc.) appears deliberate — recommend keep.
- **D5 Bold Pāḷi lines** — Pāḷi chant text is normally plain; these lines are bolded like translations: per-06:169,188,199; per-39:89,97,103,109,117,129,137; per-42:140; per-53:152,247,287; per-54:144; per-55:11,284; per-64:12; per-43:11. Recommend: unbold (per-39's deva-refrain block is systematic — decide once for all).
- **D6 Rows needing scholarly verification** (I could not settle them mechanically):
  - per-71:112–113 `| tesāsāṃ | ? | | |` — empty analysis. Likely `tesāsā` = `tesaṃ` + `āsā` ("their wishes"); next row `sijjhataṃ=sijjhanaṃ | noun | nt.acc.sg` should probably be `sijjhataṃ | verb | imp.3.sg (middle) | may (they) succeed`. Verify against the chant line and DPD.
  - per-31:30 `| attha | noun | masc.acc.sg |` — bare `attha` cannot be acc.sg; the chant probably has sandhi `…paṭicchādan'atthaṃ`. Suggest `atthaṃ` with a sandhi note; verify.
  - per-40:122 `ahesun'ti` gloss reads "but pr. - may they be," — garbled; needs a proper gloss ("(if they) had been" aor.3.pl).
  - per-26:83 `tesaṃ` tagged masc.gen.sg, gloss "of that" — form is plural (`tesaṃ` gen.pl); check context: gloss may need "of those".
  - pubbakicca-analysis.md:232 `| attha | card | x.nom.pl | eight |` — Pāḷi typo for `aṭṭha`? Verify against the chant line before touching Pāḷi text.
  - per-62:236 `sarate-m'` tagged opt.3.sg — form is middle present (`sarate`); suggest `pr.refl.3.sg`; verify.
  - per-49:66 `sādhavo` tagged ind — looks like masc.nom.pl of `sādhu` ("good sirs"); verify against chant context.
  - per-16 table above L266: if a row glosses `rukkha-mūlāni` as "foots of a tree", align with the corrected translation ("roots of trees").
- **D7 Navigation/index gaps** — `pubbakicca-analysis.md` has no footer nav (no `[index]` link) and is not referenced from `docs/6-pali-class/sbs-per-analysis.md` (post-patimokkha.md is, at index line 114). Recommend: add a footer index link and an index entry.
- **D8 Quote style policy** — mixed straight `'`, curly `”`, doubled `''`, and unbalanced quotes: opening quote missing in per-11:21,45,58; per-18:262,294,314,335; per-19:1191,1203,1245; per-23:157,167,179,189; per-28:187; per-40:327–343 (`''` closers); per-53:84,304; per-59:56; per-66:82; per-68:25; stray `”` inside a Pāḷi word at per-19:190 (`sikkhāpadesū'”ti` — remove `”`). pubbakicca-analysis.md's `“...and”` placeholders look intentional — keep. Recommend: straight apostrophes, balanced pairs; needs one decision then a sweep.
- **D9 per-39 title** (line 3) `DhammacakkappavattanaSutta` → `Dhammacakkappavattana-Sutta`; also per-37 sutta reference `[dn 22.5]` → `[DN 22.5]` to match `[SN 56.11]`, `[MN 27 / 38 / 51]` style.
- **D10 per-38:63** `inevitable by me to be dead` — literal but broken English; recommend "my death is unavoidable" (verify against the Pāḷi line and the style of neighbouring lines).

---

## Part 9 — Verification after implementation

```bash
cd docs/6-pali-class/sbs-per-analysis
grep -rn "idioṃ\|theṃ\|calṃ\|firṃ\|forṃ\|phlegṃ\|probleṃ\|pleasureenjoyment" *.md   # expect 0
grep -rn "1st\.\|2nd\.\|3rd\.\|instr\|reflx\|emphat\|pres\.3" *.md                    # expect 0 in Grammar cells
grep -rn "Bhessed\|certan\|heared\|onself\|throught\|fora \|ofthe\|onegone\|moks \|perferm\|beed \|succseed\|Tiple\|merrit\|exhalted\|dhamams\|grate result" *.md  # expect 0
grep -rn " ,\" *.md | grep "\*\*"                                                    # spaces before commas in translations, expect 0
grep -rn "m\.n\.s\|m\.ac\.s\|nt\.n\.s\|nt\.i\.sg\|f\.n\.sg\|m\.abl\.s" *.md          # expect 0
```
Also re-run the table-structure check (each row's cell count equals its header's; POS values from the canonical set; no English prose in Grammar cells).

---

## Statistics

- Corruption fixes (Part 1): 23 · Shifted rows (Part 2): 15 · Split glosses (Part 3): 48
- Grammar-tag corrections (Part 4): 64 · Standardization classes (Part 5): 12 (≈200 line touches)
- Translation typos (Part 6): ~90 · Content errors (Part 7): 7 · Decisions (Part 8): 10

