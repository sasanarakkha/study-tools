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
- **Parts 10–16 (addendum, Reviewer B from `temp/Chanting Book Analaysis*`) are proposals, not approved edits.** Implement from them only what remains after the user has pruned them; read the rules in Part 10 first (Options A/B, policy blocks, Parts 15–16 are never implemented).

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



---
---

# ADDENDUM — Reviewer B suggestions (`temp/Chanting Book Analaysis*` folders)

Added 2026-11-09. Parts 10–16 below. Parts 1–9 above are the original audit and are unchanged. **All of Parts 10–16 are proposals awaiting the user's selection** — apply nothing from them until the user has removed what they reject (see "How to use" in Part 10).

## Part 10 — Source, method, how to use this addendum

**Why two folders?** `temp/Chanting Book Analaysis/` and `temp/Chanting Book Analysis Done by AI/` are one and the same review. All 76 chapter `.md` files and `analysis_reports/Pali_Accuracy_and_Grammar_Report.md` are byte-identical in both (checked with `diff -rq` / `cmp`). The only differences: the first folder also holds the reviewer's 35 helper scripts (`fix_*.py`, `append_*.py`, …); the second folder (`… Done by AI`) holds a non-empty `scratch/` and two zero-byte `Icon_` files. The reviewer is an AI agent (instructions in the report mention `replace_file_content` and a DPD `sqlite3` lookup) that edited the chapter files in place and logged each correction at the bottom of each file and in the report.

**How the reviewer's edits were recovered.** The reviewer worked on the older Google-Docs export (git commit `71c840b`, before the table reformat). I diffed every chapter against that commit (whitespace-normalised, row by row), then mapped each changed row onto its **current** line in `docs/6-pali-class/sbs-per-analysis/` (same line numbering as Parts 1–8; docs unchanged since the audit). Result: **631 changed table rows**, 4 translation lines, 3 chant-line spellings, 1 deleted row, 7 prose lines. The reviewer's log also lists many corrections that were already in the `71c840b` baseline (e.g. `ṭhiti`, `rājā`, `bahū`, `mukhaṃ` in file 13) — those are not suggestions and are not repeated here. `Pubbakicca Analysis` was not in the reviewer's folders; Parts 1–8 are the only source for it.

**Notation.** The reviewer writes `.s` / `.p` (`masc.nom.s`); the repo canonical is `.sg` / `.pl`. All suggested Grammar values below are already converted to repo canonical. Reviewer's POS values `ger`, `abs`, `prp`, `sandhi`, `card`, `excl` etc. are DPD vocabulary.

**How to use (for the user):** delete any line/item/block you disagree with. For an Option pair (A/B) delete the one you do not want. A whole policy block (P1–P8, Parts 14) can be deleted at once.
**For the implementing agent:** same rules as the top of this file (match quoted current text, grep before Edit, stop on mismatch). Additionally: (1) if both options of a pair remain, stop and ask; (2) a policy block applies only to the rows listed in it; (3) Part 15 and Part 16 are NOT to be implemented (15 = recommended rejections kept for the record, 16 = already in Parts 1–8); (4) where an item says "amends Part N", the Part N row must be implemented in its amended form.

### Where each reviewer change landed

| Bucket | Rows | Where |
|---|---|---|
| Conflicts with an existing audit item (different suggestion, same place) | 13 places | Part 11.1 |
| Conflicts with an audit policy (refl / compound gender / ger-abs POS) | 7 + 34 + 20 rows | Part 11.2–11.4 |
| New specific corrections | 131 rows | Part 12 |
| New Pāḷi-text spelling decisions | 3 chant lines | Part 13 |
| New bulk policies (DPD sub-type in Grammar, POS `sandhi`, POS `card`) | 322 + 17 + 5 rows | Part 14 |
| Recommended rejections (reviewer defects / contradict corpus) | 42 rows | Part 15 |
| Identical to an existing audit item (no action) | 40 rows + 4 translations + 1 deletion | Part 16 |

Every one of the 631 rows is in exactly one bucket above (7 + 34 + 20 policy-conflict rows are counted separately from the 13 single-place conflicts). Four rows of the "identical" bucket carry an extra reviewer change that is listed in Part 12 (51:44, 53:12, 53:80, 34:59); `05:59 cattāri` is counted under P8 and its tag fix is already audit Part 4.


---

## Part 11 — Conflicts: two different suggestions for the same place (pick A or B)

### 11.1 Single-place conflicts

Option **A** = existing audit (Parts 1–8). Option **B** = Reviewer B. Keep one, delete the other. Current = the row as it is in the docs now.

| ID | Place | Current | Option A (audit) | Option B (reviewer) | Note |
|---|---|---|---|---|---|
| C1 | per-01:79 | `api`: POS `ind`, Gr `emphat` | Part 5.4: Grammar `emphat` → `emph` | Grammar `emphat` → ∅ (empty) | DPD lists `api` as plain `ind`. |
| C2 | per-15:11 | `handa`: POS `ind`, Gr `emp` | Part 5.4: Grammar `emp` → `emph` | Grammar `emp` → `excl` | DPD: `handa` = ind, excl. Choosing B is consistent with P4 (all `handa` rows → `excl`). |
| C3 | per-07:50 | `ajjhagā`: POS `verb`, Gr `imper.3.sg` | Part 4: Grammar → `aor.3.sg` | Grammar → `imperf` (reviewer dropped person/number; if B is kept write `imperf.3.sg`) | Audit Part 4 has the same pair for `per-54:126`; use the same choice for both. Reviewer did not touch per-54:126. |
| C4 | per-18:245 | `dukkhaṃ`: POS ∅, Gr `noun` | Part 2: rebuilt row `noun` / `nt.nom.sg` (subject of `idaṃ dukkhaṃ ariyasaccaṃ`) | Rebuilt row `noun` / `nt.acc.sg` (reviewer just fixed the `nt.ac.s` typo) | Row is column-shifted: both options rebuild the same row, only the case differs. Reviewer's meaning/POS fix is identical to A. |
| C5 | per-49:67 | `me`: POS `pron`, Gr `1.imp.sg` | Part 3: `me / pron / 1.dat.sg / for me` | `me / pron / 1.gen.sg / my, of me, by me` | Context `bhaṇantu me` / `suṇantu me`: dative-sense ("for me") vs genitive-sense. |
| C6 | per-49:66 | `sādhavo`: POS `ind`, Gr `accomplishing, fulfilling, effecting, completing` | Part 3: keep `ind`, merge gloss: `accomplishing, fulfilling, effecting, completing, with approval` (D6 asks to verify) | POS `ind` → `adj`, Grammar → `masc.nom.pl`, Eng → `good ones, virtuous ones` | B answers D6 (reviewer: `sādhavo me suṇantu` = "may the virtuous ones hear from me"). |
| C7 | per-36:28 | `vevaṇṇiya-`: POS `adj`, Gr `state of having no caste, who change` | Part 3: POS stays `adj` | POS `adj` → `noun` | Grammar empty in both; gloss merge identical. |
| C8 | per-16:79 | `majjhe`: POS `ind`, Gr `from loc. sg.` | Part 5.11: Grammar `from loc. sg.` → `adv` | POS `ind` → `noun`, Grammar `from loc. sg.` → `nt.loc.sg` (gloss unchanged: `in the present, lit. in the middle`) | DPD `majjhe` is a locative of `majjha`; ‘adv’ vs real locative. |
| C9 | per-16:239 | `upādāya`: POS `ind`, Gr `from ger` | Part 5.11: Grammar `from ger` → `ger` | Grammar `from ger` → `adv` | Reviewer: DPD upādāya 2/3 = ind, adv, used as postposition. |
| C10 | per-16:72 | `pubbe`: POS `ind`, Gr `before, previously, formerly, in the past, in a` | Part 3: `pubbe / ind / (empty) / before, previously, … in a previous life` | Same row but Grammar `adv` | Audit leaves Grammar empty; reviewer (and audit 5.11 for per-18:248) use `adv` for `pubbe`. |
| C11 | per-30:52 | `accayena`: POS `ind`, Gr `after the passing (of), after the lapse (of)` | Part 3: Grammar empty, full gloss incl. `lit. with gone past` | Grammar `adv`; reviewer's gloss is truncated (drops `, lit. with gone past`) | If B is chosen, apply only the Grammar `adv` and keep A's full gloss. |
| C12 | per-06:14 | `ceva`: POS `idioṃ`, Gr ∅ | Part 1: POS `idioṃ` → `idiom` | POS `idioṃ` → `sandhi` | Also affects every other `idioṃ` row if B is taken as a principle (see Part 14 P7). |
| C13 | per-14:103 | `na`: POS `neg`, Gr ∅ | Part 5.10: POS `neg` → `ind`, Grammar `neg` (audit lists per-14:83,103,148) | POS `neg` → `ind`, Grammar ∅ | Corpus has 16 existing `ind` / `neg` rows; see X2. Reviewer changed only :103 of the three. |

### 11.2 Policy conflict — reflexive tag on `karomase` / `bhaṇāmase` (and one `labhate`)

Current tags are inconsistent (`ref.imp.1.pl`, `imp.ref.pr.1.pl`, `imp.reflx.1.pl`, …).
- **Option A (audit Part 5.3):** standardise to `imp.refl.1.pl` (keep the reflexive marker).
- **Option B (reviewer):** drop it: `imp.1.pl` (and `labhate`: `pr.refl.3.sg` → `pr.3.sg`).
Rows (same set for A and B):
- **per-02**: L19 karomase (ref.imp.1.pl→imp.1.pl)
- **per-03**: L13 karomase (ref.pr.1.pl→imp.1.pl)
- **per-04**: L13 karomase (imp.ref.pr.1.pl→imp.1.pl)
- **per-05**: L13 karomase (imp.ref.pr.1.pl→imp.1.pl)
- **per-06**: L19 bhaṇāmase (imp.reflx.1.pl→imp.1.pl)
- **per-13**: L158 labhate (pr.refl.3.sg→pr.3.sg)
- **per-15**: L15 bhaṇāmase (imp.reflx.3.pl→imp.1.pl)

(Audit Part 5.3 also lists `post-patimokkha.md:19` `karomase`; the reviewer did not touch that file's `karomase`; if B is kept, use `imp.1.pl` there too for consistency. Part 4 item `per-15:15` `bhaṇāmase` → `imp.refl.1.pl` is the A form of the same change.)

### 11.3 Policy conflict — gender tag on compound members (`word-` rows)

- **Option A (audit Part 5.7):** keep the bare gender (`masc`, `fem`, `nt`), only drop a trailing dot.
- **Option B (reviewer):** blank the Grammar cell (a bare gender is not an inflected form).
Corpus data for the choice: of ~700 compound-member rows (`word-`, POS noun/adj) **531 already have an empty Grammar**, only 41 carry a bare gender. B would make these ~34 rows consistent with the majority. The reviewer himself is inconsistent once: `paṇṇākāra-` `∅ → masc` (the `paṇṇākāra-` item in 12.2a — decide it together with this policy).
Rows changed by B (bare gender → ∅):
- **per-13**: L52 alattaka- (masc→∅) · L184 paññā- (fem.nom.sg→∅)
- **per-18**: L28 kāmasukhallikā- (fem→∅)
- **per-21**: L39 vimuttiñāṇadassana- (nt→∅) · L128 parivīmaṃsaṃ- (fem→∅) · L143 parivīmaṃsaṃ- (fem→∅)
- **per-22**: L218 abhijjhā- (fem→∅)
- **per-23**: L174 kāya- (masc→∅) · L184 kāya- (masc→∅) · L195 pīti- (fem→∅) · L229 citta- (masc→∅)
- **per-24**: L13 \>avijjā- (fem→∅) · L14 \>paccayā (masc→∅)
- **per-28**: L30 sannipāta- (masc→∅)
- **per-31**: L21 ḍaṃsa- (masc→∅) · L22 makasa- (masc→∅) · L23 vāt'ātapa- (masc→∅) · L24 siriṃsapa- (masc→∅) · L53 vihiṃsa- (fem→∅) · L55 brahmacariya- (nt→∅) · L86 ḍaṃsa- (masc→∅) · L87 makasa- (masc→∅) · L88 vātātapa- (masc→∅) · L89 siriṃsapa- (masc→∅)
- **per-35**: L12 jarā- (fem→∅) · L24 byādhi- (nt→∅)
- **per-42**: L121 abhivādana- (nt→∅)
- **per-51**: L67 visuddhi- (fem→∅)
- **per-54**: L206 patti- (fem→∅)
- **per-62**: L128 janakāya- (masc→∅) · L148 mati- (fem→∅)
- **per-66**: L109 \>avijjā- (fem→∅) · L110 \>paccayā (masc→∅)
- **per-74**: L140 āsavakkhayā- (masc→∅)

### 11.4 Policy conflict — POS of gerunds / absolutives

- **Option A (current corpus + audit Part 5.8/5.11):** POS `verb`, Grammar `ger` / `abs` (the corpus has 84 `verb | abs`, 46 `verb | ger`, 10 `verb | inf`; the audit even converts `from ger` → `ger` in Grammar).
- **Option B (reviewer):** POS `ger` / `abs`, Grammar empty. The reviewer converted only the 20 rows below and left ~130 others as `verb | abs/ger` (he "verified" them in his log), so B applied to these rows alone would create inconsistency — if B is chosen, it should be applied to **all** `verb | abs/ger/inf` rows (ask the agent to extend it).
Rows changed by B (Grammar before→after shown; POS also changes `verb` → `ger`/`abs`):
- **per-03**: L71 abhiññā (ger→∅) · L72 sacchikatvā (abs→∅)
- **per-09**: L43 āgamma (ger→∅) · L104 āgamma (ger→∅)
- **per-11**: L112 vippahāya (ger→∅) · L118 āgamma (ger→∅) · L133 hitvā (abs→∅)
- **per-12**: L33 nikkhipitvā (abs→∅) · L38 anādiya (ger→∅) · L41 abbuyha (ger→∅)
- **per-13**: L106 laddhāna (abs→∅) · L137 hutvāna (abs→∅) · L219 disvā (abs→∅) · L247 disvā (abs→∅)
- **per-14**: L207 upaṭṭhapetvāna, (abs→∅) · L220 saritvā (abs→∅)
- **per-15**: L27 parakkamma (ger→∅) · L31 nappahāya (ger→∅) · L76 katvā (abs→∅)
- **per-16**: L122 viññāya (ger→∅)

---

## Part 12 — New specific corrections (not in Parts 1–8)

Format: `ID | place | word | change (current → suggested)`. Gloss text is quoted exactly. "Reviewer note" is the reviewer's own stated reason, where he gave one.


### 12.1 Misplaced / shifted cells and tag-in-wrong-column (new finds)

| ID | Place | Word | Change | Note |
|---|---|---|---|---|
| N1 | per-08:57 | `mahattam-` | Rebuild row as `| mahattam- | noun | nt.acc.sg | greatness; illustriousness |` | gender tag was in POS column |
| N2 | per-14:36 | `sītavātaparittāṇaṃ` | Rebuild row as `| sītavātaparittāṇaṃ | noun | nt.nom.sg | protection from cold and wind |` | Tag sits in POS column (audit Part 5.6 `nt.n.s` fix would leave it in the wrong column — this amends it) |
| N3 | per-14:40 | `hirikopīnachādanaṃ` | Rebuild row as `| hirikopīnachādanaṃ | noun | nt.nom.sg | covering that which arouses shyness |` | same as 14:36 |
| N4 | per-14:182 | `teladhārāva` | Rebuild row as `| teladhārāva | noun | fem.nom.sg | as stream of oil |` | POS empty |
| N5 | per-17:47 | `vidvā` | Rebuild row as `| vidvā | adj | masc.nom.sg | wise |` | POS cell held `masc` |
| N6 | per-18:15 | `pabbajitena` | Rebuild row as `| pabbajitena | noun | masc.ins.sg | by monk, one who has gone forth |` | POS cell held `masc` |
| N7 | per-18:122 | `jāti` | Rebuild row as `| jāti | noun | fem.nom.sg | birth, rebirth, conception |` | columns shifted; `f.n.s` embedded in gloss; audit Part 2 missed this row |
| N8 | per-19:57 | `rajo-patho` | Rebuild row as `| rajo-patho | noun | masc.nom.sg | dusty, dirty , lit: condition of dust, state of dirt |` | POS cell empty (audit only fixes the typo in this row's gloss) |
| N9 | per-36:126 | `uttari-` | Rebuild row as `| uttari- | adj | | over; beyond; further; moreover; additional |` |  |
| N10 | per-36:140 | `na` | Rebuild row as `| na | ind | | not |` |  |
| N11 | per-39:48 | `te` | Rebuild row as `| te | pron | masc.nom.pl | those |` | columns shifted; audit Part 2 missed this row; abbreviation `m.n.pl` |
| N12 | per-40:293 | `vā` | Rebuild row as `| vā | ind | | or |` |  |
| N13 | per-40:295 | `vā` | Rebuild row as `| vā | ind | | or |` |  |
| N14 | per-40:297 | `vā` | Rebuild row as `| vā | ind | | or |` |  |
| N15 | per-40:299 | `vā` | Rebuild row as `| vā | ind | | or |` |  |
| N16 | per-40:301 | `vā` | Rebuild row as `| vā | ind | | or |` |  |
| N17 | per-40:303 | `vā` | Rebuild row as `| vā | ind | | or |` |  |
| N18 | per-40:307 | `vā` | Rebuild row as `| vā | ind | | or |` |  |
| N19 | per-41:254 | `te` | Rebuild row as `| te | pron | masc.nom.pl | those |` | same as 39:48 |
| N20 | per-59:134 | `anuppatti-` | Rebuild row as `| anuppatti- | noun | | following attainment (of), after getting |` | POS cell held `masc`; compound member, Grammar stays ∅ |

### 12.2a Gender / case / number tags on nouns, adjectives, pronouns, participles

| ID | Place | Word | Change | Note |
|---|---|---|---|---|
| N21 | per-01:91 | `mānasā` | Gr `nt.abl/instr.sg` → `nt.ins.sg`; Eng `from (with) a mind, intention` → `with a mind, intention` | extends audit Part 5.2 |
| N22 | per-01:102 | `paṇṇākāra-` | Gr ∅ → `masc` | adds bare gender — contradicts policy 11.3 (B) |
| N23 | per-02:16 | `namakāraṃ` | Gr `nt.acc.sg` → `masc.acc.sg` | DPD: kāra masc. |
| N24 | per-02:18 | `\>kāraṃ` | Gr `nt.acc.sg` → `masc.acc.sg` | DPD: kāra masc. |
| N25 | per-03:94 | `sātthaṃ` | Gr `masc.acc.sg` → `nt.acc.sg` | agrees with neuter `brahmacariyaṃ` (also next 3 rows) |
| N26 | per-03:95 | `sabyañjanaṃ` | Gr `masc.acc.sg` → `nt.acc.sg` | same |
| N27 | per-03:97 | `paripuṇṇaṃ` | Gr `masc.acc.sg` → `nt.acc.sg` | same |
| N28 | per-03:98 | `parisuddhaṃ` | Gr `masc.acc.sg` → `nt.acc.sg` | same |
| N29 | per-06:177 | `vatthu-ttayaṃ` | Gr `masc.acc.sg` → `nt.acc.sg` | `vatthu` neuter |
| N30 | per-06:186 | `abhisaṅkhataṃ` | Gr `masc.acc.sg` → `nt.acc.sg` | agrees with neuter `vatthuttayaṃ` |
| N31 | per-06:384 | `aniccā` | Gr `fem.nom.sg` → `masc.nom.pl` | `aniccā` agrees with `saṅkhārā` (masc.pl) |
| N32 | per-06:496 | `brahmacariyaṃ` | Gr `masc.acc.sg` → `nt.acc.sg` | `brahmacariya` neuter |
| N33 | per-08:78 | `ubho` | Gr `masc.nom.sg` → `masc.nom.pl` | `ubho` plural |
| N34 | per-10:34 | `tapo` | Gr `nt.nom.sg` → `masc.nom.sg` | DPD: tapas masc. |
| N35 | per-13:14 | `cittakataṃ` | Gr `masc.acc.sg` → `nt.acc.sg` | agrees with nt `bimbaṃ`/`rūpaṃ` |
| N36 | per-13:33 | `cittakataṃ` | Gr `masc.acc.sg` → `nt.acc.sg` | same |
| N37 | per-13:38 | `aṭṭhiṃ` | Gr `nt.nom.sg` → `nt.acc.sg` | acc., not nom. |
| N38 | per-13:40 | `onaddhaṃ` | Gr `nt.nom.sg` → `nt.acc.sg` | acc., not nom. |
| N39 | per-13:107 | `vittaṃ` | Gr `masc.acc.sg` → `nt.acc.sg` |  |
| N40 | per-13:109 | `mohā` | Gr `nt.abl.sg` → `masc.abl.sg` | `moha` masc. |
| N41 | per-14:62 | `paṇītaṃ` | Gr `nt.nom.sg` → `nt.acc.sg` | object, acc. |
| N42 | per-14:65 | `lūkhaṃ` | Gr `nt.nom.sg` → `nt.acc.sg` | object, acc. |
| N43 | per-14:66 | `appaṃ` | Gr `nt.nom.sg` → `nt.acc.sg` | object, acc. |
| N44 | per-14:70 | `bahuṃ` | Gr `nt.nom.sg` → `nt.acc.sg` | object, acc. |
| N45 | per-14:94 | `parikkhāre` | Gr `masc.acc.pl` → `masc.loc.sg` | locative |
| N46 | per-14:95 | `bhesajje` | Gr `nt.acc.pl` → `nt.loc.sg` | locative |
| N47 | per-14:97 | `paccaye` | Gr `nt.acc.pl` → `masc.loc.sg` | locative |
| N48 | per-14:120 | `kandarāsu` | Gr `masc.loc.pl` → `fem.loc.pl` | `kandarā` fem. |
| N49 | per-14:147 | `atthaddhamānasā` | Gr ∅ → `masc.nom.pl` | grammar was empty |
| N50 | per-14:224 | `vattam-` | Gr ∅ → `nt.acc.sg` |  |
| N51 | per-15:14 | `gāthāyo` | Gr `fem nom pl` → `fem.acc.pl` |  |
| N52 | per-15:33 | `kāme` | Gr `masc.loc.sg` → `masc.acc.pl` | acc. pl. |
| N53 | per-16:29 | `appassuta-` | Gr ∅ → `masc.nom.sg` | grammar was empty |
| N54 | per-16:232 | `yaṃ` | Gr `masc.acc.sg` → `nt.nom.sg` | neuter, subject |
| N55 | per-16:234 | `karaṇīyaṃ` | Gr `masc.acc.sg` → `nt.nom.sg` | neuter, subject |
| N56 | per-16:240 | `kataṃ` | Gr `masc.acc.sg` → `nt.nom.sg` | neuter, subject |
| N57 | per-16:242 | `taṃ` | Gr `masc.acc.sg` → `nt.nom.sg` | neuter, subject |
| N58 | per-31:41 | `piṇḍapātaṃ` | Gr `masc` → `masc.acc.sg` | grammar was only `masc` |
| N59 | per-42:156 | `te` | Gr `1.dat.sg` → `2.dat.sg` | audit Part 4 has the same fix for te@51:44, 59:58, 63:33 but not this row |
| N60 | per-43:22 | `verā` | Gr `masc.nom.pl` → `nt.nom.pl` | `vera` neuter |
| N61 | per-44:40 | `sukhassa` | Gr `masc.gen.sg` → `nt.gen.sg` | `sukha` neuter |
| N62 | per-45:89 | `verā` | Gr `masc.nom.pl` → `nt.nom.pl` | same as 43:22 |
| N63 | per-47:16 | `dinnaṃ` | Gr `nt.acc.sg` → `nt.nom.sg`; Eng `given, offered` → `a gift given, what is given` | pp is the subject: nt.nom; gloss changes to match |
| N64 | per-47:57 | `dinnaṃ` | Gr `masc.acc.sg` → `nt.nom.sg`; Eng `given, offered` → `gift, what is given` | same as 47:16 |
| N65 | per-47:58 | `mahapphalaṃ` | Gr `masc.acc.sg` → `nt.nom.sg`; Eng `of great fruit, yielding good results` → `of great fruit, yielding great results` | predicate agrees with subject `dinnaṃ` (also gloss `good` → `great`) |
| N66 | per-52:38 | `ratanattayassa` | Gr `masc.dat.sg` → `nt.dat.sg` | `ratanattaya` neuter |
| N67 | per-52:50 | `vatthu-ttayassa'pi` | Gr `masc.dat.sg` → `nt.dat.sg` | `vatthu` neuter |
| N68 | per-52:66 | `suvatthi` | Gr `masc.nom.sg` → `fem.nom.sg` | DPD: suvatthi fem. (audit Part 3 item per-54:110 already uses fem.nom.sg for the same word) |
| N69 | per-53:95 | `bālānaṃ,` | Gr `masc.dat.pl` → `masc.gen.pl`; Eng `to ignorant; fools` → `of fools; ignorant ones` | dat → gen (also changes gloss `to ignorant; fools` → `of fools; ignorant ones`) |
| N70 | per-53:96 | `paṇḍitānaṃ-` | Gr `masc.dat.pl` → `masc.gen.pl`; Eng `to wise people` → `of wise people` | dat → gen (gloss `to wise people` → `of wise people`) |
| N71 | per-53:102 | `etaṃ` | Gr `masc.acc.sg` → `nt.nom.sg` | neuter, subject |
| N72 | per-53:178 | `ñātakānaṃ-` | Gr `masc.dat.pl` → `masc.gen.pl`; Eng `to relations, relatives, kinsmans` → `of relations, relatives, kinsmen` | dat → gen (gloss `to relations, relatives, kinsmans` → `of relations, relatives, kinsmen`) |
| N73 | per-61:73 | `balaṃ` | Gr `nt` → `nt.acc.sg` | grammar was only `nt` |
| N74 | per-62:127 | `vacanaṃ` | Gr `nt` → `nt.acc.sg` | grammar was only `nt` |
| N75 | per-63:104 | `paṇīdhi` | Gr `fem` → `masc.nom.sg` | DPD: paṇīdhi masc. |

### 12.2b Verb tags and indeclinable (DPD sub-type) cleanups

| ID | Place | Word | Change | Note |
|---|---|---|---|---|
| N76 | per-01:73 | `sādhu` | Gr ∅ → `excl`; Eng `it is good, would be good, please` → `it is good (for); it would be good (if)` |  |
| N77 | per-06:473 | `uddissa` | Gr `ind` → ∅ | gerund: no inflectional grammar |
| N78 | per-11:25 | `atha` | Gr `adv` → ∅ |  |
| N79 | per-13:164 | `vihanti` | Gr `pr.3.sg` → `pr.3.pl` |  |
| N80 | per-19:188 | `samādāya` | Gr `abs` → `ger` |  |
| N81 | per-27:170 | `no` | Gr `interr` → ∅ | DPD: `no` is plain ind |
| N82 | per-42:147 | `rakkhantu` | Gr `imp.3.sg` → `imp.3.pl` | `rakkhantu` is 3.pl |

### 12.3 POS corrections (with accompanying Grammar / gloss edits where shown)

| ID | Place | Word | Change | Note |
|---|---|---|---|---|
| N83 | per-01:48 | `sa-` | POS `pron` → `prefix`; Eng `one's own, his own OR with` → `with, accompanied by` | `sa-` as prefix = "with" |
| N84 | per-01:50 | `sa-` | POS `pron` → `prefix`; Eng `one's own, his own OR with` → `with, accompanied by` | same as 01:48 |
| N85 | per-01:77 | `sucira- (or) suciraṃ` | POS `adj` → `ind` (leave Grammar empty) | reviewer also wrote `ind` into Grammar (duplicate; see X1) — only the POS change is proposed here |
| N86 | per-01:146 | `svākkhāto` | POS `pp as adj` → `adj` | D4: unify `pp as adj` |
| N87 | per-02:13 | `pubbabhāga-` | POS `adj` → `noun` |  |
| N88 | per-03:46 | `bhagavā` | POS `adj` → `noun`; Eng `fortunate, illustrious, sublime, blessed, happy glorious, auspicious` → `Sublime One, Blessed One, Fortunate One` | DPD: bhagavant 1 = masc noun |
| N89 | per-06:178 | `vandayatā` | POS `pp` → `prp`; Gr `masc.instr.sg.` → `masc.ins.sg`; Eng `by respected; revered; honoured` → `by one venerating, paying respect` | extends audit Part 5.2 (`instr` → `ins`) |
| N90 | per-06:394 | `anattā` | POS `noun` → `adj`; Gr `masc.nom.pl` → `masc.nom.sg` | reviewer wrote `masc.nom.s`; converted to repo canonical |
| N91 | per-08:43 | `esā` | POS `noun` → `pron` | DPD: pron, fem.nom.sg of eta |
| N92 | per-08:58 | `abhikaṅkhatā` | POS `pp` → `prp` | active present participle (reviewer: one longing/aspiring); gloss unchanged |
| N93 | per-11:18 | `paññāya` | POS `verb` → `noun`; Gr `abs` → `fem.ins.sg`; Eng `knowing, understanding (or) noun f.ins.s with understanding` → `with understanding, with wisdom` | gloss held two alternative readings; reviewer chose the noun reading |
| N94 | per-12:43 | `parinibbuto` | POS `adj` → `pp` |  |
| N95 | per-13:222 | `pabbajito-` | POS `pp/noun` → `pp` | drops `/noun` |
| N96 | per-13:248 | `pabbajito-` | POS `pp/noun` → `pp` | same |
| N97 | per-13:251 | `apaṇṇakaṃ` | POS `ind` → `adj`; Gr ∅ → `nt.acc.sg` | gloss `surely; certainly` unchanged (reviewer: DPD adj, used adverbially as acc.sg) |
| N98 | per-13:254 | `seyyo` | POS `ind` → `adj`; Gr ∅ → `masc.nom.sg` | DPD: seyya adj, compar |
| N99 | per-14:109 | `āsavakkhaye` | POS `adj` → `noun`; Gr `masc.acc.pl` → `masc.loc.sg` |  |
| N100 | per-15:68 | `seyyo` | POS `ind` → `adj`; Gr ∅ → `masc.nom.sg` | same |
| N101 | per-15:74 | `seyyo` | POS `ind` → `adj`; Gr ∅ → `masc.nom.sg` | same |
| N102 | per-16:51 | `satīmanto` | POS `adj as noun` → `noun`; Gr `masc.nom.sg` → `masc.nom.pl` |  |
| N103 | per-16:77 | `m'āhu` | POS `v+ind` → `verb`; Gr `aor.3.sg` → `aor.3.pl` | POS `v+ind` is a D4 composite value |
| N104 | per-16:118 | `santiyā;` | POS `verb` → `noun` |  |
| N105 | per-16:121 | `pamatte` | POS `pp as adj` → `pp` | D4: `pp as adj` → `pp` |
| N106 | per-17:12 | `atītaṃ` | POS `adj (as noun)` → `adj` | D4: unify `adj (as noun)` → `adj` |
| N107 | per-17:44 | `asaṃhiraṃ` | POS `adj (or as noun)` → `adj` | same |
| N108 | per-17:45 | `asaṅkuppaṃ` | POS `adj (or as noun)` → `adj` | same |
| N109 | per-17:81 | `vihārim-` | POS `adj (as noun)` → `adj` | same |
| N110 | per-18:158 | `piyehi` | POS `adj (as noun)` → `adj` | same |
| N111 | per-29:329 | `ubhaya-` | POS `pron` → `adj` | adj (from `ubha`) |
| N112 | per-33:80 | `sakā-` | POS `noun` → `adj` |  |
| N113 | per-34:43 | `sabbattatāya` | POS `adj` → `ind`; Gr `masc.dat.sg` → `adv`; Eng `to all encompassing, all pervading lit. all spread out` → `to all beings; encompassing all living beings` |  |
| N114 | per-35:63 | `sako-` | POS `noun` → `adj` |  |
| N115 | per-38:150 | `sukho` | POS `noun` → `adj` |  |
| N116 | per-42:25 | `dinnaṃ` | POS `adj` → `pp` |  |
| N117 | per-48:12 | `laddhā` | POS `verb` → `pp`; Gr `ger` → `masc.nom.pl`; Eng `getting, obtaining` → `having obtained, having gotten` | reviewer: `laddha` is a past participle, not a gerund |
| N118 | per-51:76 | `suciṇṇo` | POS `noun` → `adj` | `suciṇṇo` adj per DPD |
| N119 | per-52:37 | `āraddhassa` | POS `noun` → `pp`; Eng `accomplishment, achievement; success` → `won; accomplished; succeeded` | reviewer: `āraddha` is a past participle (DPD) |
| N120 | per-53:101 | `pūjanīyānaṃ,` | POS `adj, ptp` → `ptp`; Gr `masc.dat.pl` → `masc.gen.pl`; Eng `to entitled to homage; should be venerated` → `of those worthy of veneration; who should be revered` | same dat → gen fix as `bālānaṃ` / `paṇḍitānaṃ` / `ñātakānaṃ` in 12.2a |

#### 12.3b Extensions of existing audit items (same row, extra change)

| ID | Place | Word | Change | Note |
|---|---|---|---|---|
| N121 | per-51:44 | `te` | POS `noun` → `pron` | extends audit Part 4 (which only changes Grammar to `2.dat.sg`) |
| N122 | per-53:12 | `sutaṃ:` | Eng `heard` → `what is heard; something heard` | extends audit Part 4 (`sutaṃ` → nt.nom.sg) |
| N123 | per-53:80 | `brūhi` | Eng `you speak, may you say, you shall talk` → `say!; tell!; speak!` | extends audit Part 4 (`brūhi` → imp.2.sg) |

### 12.4 Gloss (English) edits only

| ID | Place | Word | Change | Note |
|---|---|---|---|---|
| N124 | per-01:14 | `sambuddho` | Eng `one who has thoroughly understood, being enlightened, a Buddha, fully awakened one` → `one who has thoroughly understood, being enlightened, a Buddha` | drops `, fully awakened one` from the gloss — loses information; consider keeping the long form |
| N125 | per-05:100 | `ahaṃ` | Eng `i` → `I` | capital I |
| N126 | per-42:27 | `upakappati` | Eng `is beneficial to, is serve for, is accrue` → `is beneficial to, serves, accrues` | grammar fixes in the gloss |
| N127 | per-42:41 | `samijjhatu` | Eng `may it achieves, succeeds, prospers` → `may it achieve, succeed, prosper` |  |
| N128 | per-42:81 | `vivajjantu` | Eng `may they be avoided, abandoned, forsaked` → `may they be avoided, abandoned, forsaken` | typo `forsaked` |
| N129 | per-43:54 | `yasavā` | Eng `famous, renowned, lit.: possessing fame'` → `famous, renowned, lit.: possessing fame` | stray `'` removed |

### 12.5 Headword spelling / typos (headword rows only; chant lines are Part 13)

| ID | Place | Word | Change | Note |
|---|---|---|---|---|
| N130 | per-10:35 | `tītikkhā` | Word `tītikkhā` → `titikkhā` | pairs with chant-line decision Q3 (do together) |
| N131 | per-33:88 | `paṭisaraṇoā` | Word `paṭisaraṇoā` → `paṭisaraṇā` | obvious typo: chant has `kammapaṭisaraṇā` |
| N132 | per-34:53 | `mettāsahagatena` | Word `mettāsahagatena` → `mettā-sahagatena` | chant line has `mettā-sahagatena` (hyphen); row should match |
| N133 | per-34:61 | `viharati;` | Word `viharati;` → `viharati` | stray `;` |
| N134 | per-37:22 | `pariyantaṃ` | Gr `masc.acc.sg` → `masc.nom.sg`; Word `pariyantaṃ` → `pariyanto` | chant line has `taca-pariyanto` (nom.) |

#### 12.5b Spelling amending existing audit item

| ID | Place | Word | Change | Note |
|---|---|---|---|---|
| N135 | per-34:59 | `abyāpajjena` | Word `abyāpajjena` → `abyāpajjhena` | amends audit Part 2 row for 34:59; chant line 34:47 already reads `abyāpajjhena` |

### 12.6 Prose file `word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md` (not touched by Parts 1–8)

Seven grammar-label corrections inside the prose notes (the reviewer's reasons in brackets). Match the quoted fragment inside the given line.

| ID | Line | Word | Change | Reviewer note |
|---|---|---|---|---|
| N136 | 145 | *paripūrenti* | `vb. first pers. act. pl.` → `vb. third pers. act. pl.` | `-enti` = 3rd pl. |
| N137 | 149 | *sāgaraṁ* | `m. n., nom. sg. object of main clause` → `m. n., acc. sg. object of main clause` | `-ṁ` ending, object |
| N138 | 163 | *upakappati* | `vb. pres. ind. first pers. act. sg.` → `vb. pres. ind. third pers. act. sg.` | `-ati` = 3rd sg. |
| N139 | 231 | *te* | `pers. pron. third pers. dat. sg.` → `pers. pron. second pers. dat. sg.` | `te` = "for you"; (line 391 already says second pers.) |
| N140 | 443 | *sukhassa* | `m. n. gen. sg.` → `neutr. n. gen. sg.` | `sukha` is neuter |
| N141 | 449 | *sukhaṁ* | `m. n. acc. sg.` → `neutr. n. acc. sg.` | `sukha` is neuter |
| N142 | 627 | *sabbe* | `second pers. adj. pron. nom. pl.` → `adj. pron. nom. pl.` | `sabbe` = "all", not a personal pronoun |

---

## Part 13 — Decisions: spelling of Pāḷi chant lines (data-preservation rule applies)

The reviewer changed the Pāḷi **chant text itself** in three places (Parts 1–8 forbid this without an explicit item). In two cases the chant line currently disagrees with its own headword rows, so the change would remove an internal inconsistency; in the third (`tītikkhā`) both chant and row change. Recommendation: accept only if the SBS book's printed text permits it. Each is an independent yes/no:

| ID | Place | Current chant text | Reviewer's change | Facts |
|---|---|---|---|---|
| Q1 | per-03:90 | `sātthaṃ sabyañjaṇaṃ kevala-paripuṇṇaṃ …` | `sabyañjaṇaṃ` → `sabyañjanaṃ` | headword row per-03:95 is already `sabyañjanaṃ`; DPD spelling |
| Q2 | per-05:76 | `āhuṇeyyo pāhuṇeyyo dakkhiṇeyyo …` | → `āhuneyyo pāhuneyyo` | headword rows per-05:80/81 and per-57:68/69 already `āhuneyyo`/`pāhuneyyo`; per-57 chant line was not flagged |
| Q3 | per-10:27 **and** row per-10:35 | `khantī paramaṃ tapo tītikkhā, …` / `tītikkhā` | → `titikkhā` (chant line and headword row, both) | DPD spelling is `titikkhā`; only occurrence in the corpus |


---

## Part 14 — New bulk policies from Reviewer B

Each block can be accepted or deleted as a whole. Rows are listed as `L<line> word`. Apply to **exactly** these rows.

### P0 — The rule behind P1–P6 (the reviewer's "DPD sub-type" policy)
For every row with POS `ind` and an empty Grammar cell, write the DPD sub-type into Grammar: `adv`, `conj`, `emph`, `excl`, `prep`, `interr`; leave it empty when DPD gives only plain `ind`. This agrees with the direction of audit D4/Part 5.10 (those sub-types live in Grammar, POS `ind`) and with the existing corpus (already 102 `ind | adv`, 18 `ind | conj`, 5 `ind | emph`, 4 `ind | prep`; 703 `ind` rows have an empty Grammar). Accepting P1–P6 changes 322 rows. Some rows already covered elsewhere are excluded (conflicts C1/C2/C10/C11, audit-identical rows).


### P1 — Grammar `adv` (128 rows; POS stays `ind`)

- **per-01**: L13 sammā-
- **per-03**: L25 sammā-
- **per-06**: L174 evaṃ- · L194 yaṃ · L221 sammā- · L249 evaṃ · L350 evaṃ
- **per-11**: L16 iti · L120 yattha · L130 tatra-
- **per-13**: L22 dhuvaṃ · L190 idha-
- **per-14**: L107 yathā · L196 yathā · L208 evaṃ
- **per-15**: L55 bhiyyo · L87 yathā
- **per-16**: L75 pacchā · L258 pacchā
- **per-17**: L57 ajja- · L64 suve · L80 evaṃ · L83 ahorattam- · L90 ti –
- **per-19**: L46 iti · L316 iti · L803 iti · L1232 iti
- **per-35**: L90 evaṃ
- **per-38**: L59 avassaṃ · L103 aciraṃ
- **per-39**: L28 tatra
- **per-40**: L11 evaṃ- · L27 tatra · L62 evaṃ · L66 evaṃ · L78 yasmā · L82 tasmā · L283 tasmā-(t)
- **per-41**: L12 evaṃ- · L23 tatra · L168 evaṃ
- **per-42**: L10 yathā · L23 evam'eva · L24 ito · L39 khippaṃ- · L61 yathā · L71 yathā · L153 sadā
- **per-43**: L30 asesato
- **per-44**: L55 yattha · L56 yattha-
- **per-45**: L78 sabbadā
- **per-47**: L10 kāle · L33 tattha · L52 tasmā · L56 yattha
- **per-49**: L61 santike
- **per-51**: L15 sāmaṃ · L105 sayaṃ
- **per-52**: L12 sammā- · L20 idha · L39 sādhukaṃ · L68 sabbadā
- **per-53**: L10 evaṃ- · L38 yena · L40 tena- · L52 ekaṃantaṃ · L54 ekaṃantaṃ · L122 sammā- · L217 kālena · L235 kālena · L295 sabbattha'm- · L297 sabbattha · L298 sotthiṃ
- **per-54**: L35 sakkacca · L46 tasmā · L68 tasmā · L211 mudhā · L224 yathā- · L232 tathā- · L238 avecca · L350 yathā · L357 tathā- · L404 yathā-
- **per-55**: L176 dūre · L178 avidūre · L257 evam- · L319 yāvatā- · L374 puna-
- **per-56**: L149 sammā-
- **per-57**: L14 sammā-
- **per-58**: L16 puthu · L21 tasmā
- **per-59**: L15 tathā · L21 tathā- · L38 sammā- · L60 sabbadā · L97 ekadā · L105 sādaraṃ · L111 ṭhānaso
- **per-61**: L30 ettāvatā · L54 sabbadā · L78 sabbaso
- **per-62**: L23 vidhinā · L52 vidhinā · L79 vidhinā · L129 majjhe · L132 vidhinā · L184 vidhinā · L211 vidhinā
- **per-63**: L49 evaṃ
- **per-64**: L25 sadā
- **per-68**: L21 pubbe · L47 evaṃ · L63 dīgharattaṃ · L66 ṭhānaso
- **per-69**: L65 ettha · L79 aciraṃ
- **per-70**: L123 khippaṃ- · L141 yāva · L152 sabbadā · L154 yattha
- **per-71**: L15 idāni · L82 sayaṃ · L104 sadā
- **per-73**: L12 ettāvatā
- **per-74**: L57 yāva

### P2 — Grammar `conj` (114 rows; POS stays `ind`)

All are the word `ca`.

- **per-06**: L18 ca · L100 ca · L231 ca · L362 ca
- **per-08**: L14 ca · L18 ca · L40 ca · L77 ca
- **per-09**: L19 ca · L56 ca · L78 ca · L81 ca-
- **per-10**: L61 ca · L64 ca · L67 ca · L70 ca
- **per-11**: L90 ca
- **per-12**: L17 ca
- **per-13**: L37 ca · L62 ca · L128 ca · L130 ca · L241 ca · L243 ca
- **per-16**: L139 ca
- **per-17**: L21 ca · L31 ca
- **per-18**: L400 ca
- **per-19**: L811 ca
- **per-40**: L60 ca · L79 ca
- **per-43**: L48 ca · L50 ca · L53 ca · L57 ca · L59 ca
- **per-45**: L97 ca · L116 ca · L118 ca · L121 ca · L125 ca · L127 ca
- **per-46**: L54 ca · L56 ca
- **per-49**: L27 ca · L36 ca
- **per-51**: L50 ca · L108 ca
- **per-53**: L75 ca · L94 ca · L97 ca · L100 ca · L117 ca · L119 ca · L124 ca · L135 ca · L137 ca · L139 ca · L142 ca · L163 ca · L175 ca · L177 ca · L179 ca · L196 ca · L199 ca · L211 ca · L213 ca · L215 ca · L230 ca · L233 ca · L252 ca · L254 ca · L259 ca
- **per-54**: L306 ca-
- **per-55**: L33 ca · L36 ca · L51 ca · L53 ca, · L55 ca · L63 ca · L65 ca, · L80 ca · L280 ca · L292 ca · L351 ca
- **per-56**: L25 ca; · L90 ca
- **per-59**: L20 ca · L45 ca · L80 ca · L107 ca · L125 ca
- **per-61**: L11 ca · L14 ca · L17 ca · L31 ca
- **per-63**: L88 ca
- **per-68**: L16 ca · L77 ca · L82 ca
- **per-69**: L56 ca · L58 ca
- **per-70**: L28 ca · L30 ca · L45 ca · L55 ca · L57 ca · L59 ca · L71 ca · L75 ca · L115 ca · L210 ca
- **per-71**: L37 ca
- **per-73**: L13 ca

### P3 — Grammar `emph` (46 rows; POS stays `ind`)

- **per-06**: L205 ve
- **per-08**: L55 hi · L74 hi · L98 have
- **per-09**: L14 ve · L35 kho · L96 kho
- **per-10**: L41 hi
- **per-11**: L78 eva- · L91 kho
- **per-12**: L14 have
- **per-13**: L58 alaṃ · L183 hi · L185 eva · L193 hi · L210 hi · L253 eva
- **per-15**: L53 hi · L90 eva-
- **per-16**: L151 hi
- **per-17**: L86 ve
- **per-18**: L56 kho · L90 eva · L269 kho · L283 kho
- **per-19**: L1255 kho
- **per-39**: L29 kho
- **per-40**: L28 kho · L80 kho · L205 hi-
- **per-41**: L24 kho
- **per-42**: L40 eva
- **per-46**: L11 ve
- **per-51**: L16 va = eva
- **per-53**: L56 kho
- **per-54**: L29 eva · L47 hi · L69 hi · L277 eva
- **per-55**: L370 hi · L371 jātu
- **per-59**: L132 va
- **per-68**: L34 hi · L58 kho
- **per-69**: L89 va
- **per-74**: L69 kho

### P4 — Grammar `excl` (21 rows; POS stays `ind`)

- **per-02**: L9 handa · L27 namo
- **per-03**: L9 handa
- **per-04**: L9 handa
- **per-05**: L9 handa
- **per-06**: L9 handa
- **per-38**: L100 vata · L120 vata
- **per-52**: L10 namo · L15 namo · L28 namo · L34 namo · L47 namo · L51 namo- · L63 namo- · L69 namo-
- **per-69**: L11 vata · L80 vata-
- **per-74**: L123 addhā
- **post-patimokkha**: L9 handa · L27 namo

### P5 — Grammar `prep` (5 rows; POS stays `ind`)

- **per-11**: L97 pāram-
- **per-13**: L41 saha
- **per-41**: L21 saddhiṃ
- **per-48**: L19 saha
- **per-54**: L276 saha-

### P6 — Grammar `interr` (8 rows; POS stays `ind`)

- **per-36**: L60 kacci · L61 nu kho · L74 kacci · L75 nu kho · L110 kacci · L111 nu kho · L124 nu kho
- **per-40**: L186 nu

### P7 — POS `ind` → `sandhi` for fused words (17 rows)
Reviewer's reason: DPD classes these (`kiñcāpi`, `yadidaṃ`, `c'etarahi`, `n'eva`, `tv'eva`, …) as `sandhi`. Audit D4 recommends `idiom` **or** `sandhi` for multi-word entries, so this makes the choice for the `ind`-type fusions. (Related conflict: C12 `ceva`.) The reviewer wrote `sandhi` in Grammar as well for three rows (`yadidaṃ` 05:58, `c'etarahi` 08:22, `atha-api` 08:41, and `seyyathīdaṃ` 20:58 / 22:17) and `conj + loc` for `c'antalikkhe` 49:32 — **recommend leaving Grammar empty** for all of them, as the other rows do.
- **per-05**: L58 yadidaṃ
- **per-08**: L22 c'etarahi · L41 atha-api
- **per-13**: L161 cāpi
- **per-14**: L231 kiñcāpi
- **per-20**: L58 seyyathīdaṃ
- **per-22**: L17 seyyathīdaṃ
- **per-49**: L32 c'antalikkhe
- **per-54**: L256 kiñcāpi · L320 kiñcāpi
- **per-57**: L60 yadidaṃ
- **per-59**: L85 taṅ'khaṇe
- **per-65**: L38 n'eva
- **per-66**: L166 tv'eva
- **per-69**: L60 tatha'eva-
- **per-70**: L126 c'eva · L153 yeva

### P8 — POS `adj` → `card` for numerals (5 rows)
Audit D4 already recommends `card`. Grammar for numerals follows the existing `x.` convention (audit D4); reviewer's `card, x pl` for 13:72 is non-standard — keep Grammar as it is (∅) there; for 05:59 the Grammar change `masc.nom.pl` → `nt.nom.pl` is already audit Part 4, and 05:61 `aṭṭha` keeps `masc.nom.pl`.
- **per-05**: L59 cattāri · L61 aṭṭha
- **per-09**: L62 cattāri
- **per-13**: L72 aṭṭha-
- **per-18**: L364 dvādasa-

---

## Part 15 — Reviewer suggestions I recommend **rejecting** (do NOT implement; kept so nothing is lost)

If the user disagrees with a rejection, move that item into Part 12 or 14 before the agent runs.

| ID | Rows | What the reviewer did | Why reject |
|---|---|---|---|
| X1 | 28 rows (list below) | Wrote `ind` into Grammar of `ind` rows (`ind | ind`) in files 20–22 | His own rule 3 forbids duplicating `ind` into Grammar; empty Grammar (703 rows) is the corpus norm. |
| X2 ⚑ | 7 rows (list below) | `na`: Grammar `neg` → ∅ | **Demoted to user decision.** For the word `na` the corpus has 33 rows with empty Grammar vs 7 `neg`, so blanking moves toward the majority; the "16 `ind | neg` rows" are mostly other words. Against: the audit (Part 5.10) moves `neg` into Grammar. Not implemented unless you decide so. |
| X3 | per-13:13, per-13:32 | `passa`: `imp.2.sg` → `imper.2.s` | Regression: corpus uses `imp`, not `imper`. |
| X4 | per-06:414 `anattā'ti`, per-11:56 `anattā` | Grammar `masc.nom.sg` → `masc.nom.s` | Notation-only, against the `.sg` canon. |
| X5 | per-19:618 `evameva` | Gloss `in the same way` → `ind` | Reviewer wiped the gloss (row was already column-shifted); use audit Part 2 rebuild instead. |
| X6 | per-21:196 `sādhukaṃ` | Row rewritten to `ind | ind <spaces> well, thoroughly, fully |` | Garbled cells; keep the current row (`ind | | well, thoroughly, fully`). |
| X7 | per-27:12 `ekaṃ samayaṃ` | POS stays `idioṃ`, Grammar → `idiom, card + masc` | Descriptive text in Grammar; use audit Part 1 (`idioṃ` → `idiom`, Grammar ∅). |

X1 rows: per-20:20 `sādhukaṃ` · per-21:22 `sammā` · per-21:42 `api` · per-21:56 `api` · per-21:59 `api` · per-21:62 `api` · per-21:65 `api` · per-21:68 `api` · per-21:94 `ca` · per-21:96 `ca` · per-21:105 `tathā` · per-21:120 `tathā` · per-21:169 `api` · per-21:172 `api` · per-22:13 `eva` · per-22:40 `kho` · per-22:117 `idha` · per-22:119 `micchā-` · per-22:136 `idha` · per-22:259 `ca` · per-22:270 `idha` · per-22:274 `eva` · per-22:323 `ca` · per-22:326 `ca` · per-22:329 `ca` · per-22:332 `ca` · per-22:354 `ca` · per-22:357 `ca`

X2 rows: per-18:171 `na` · per-53:273 `na` · per-54:91 `na` · per-54:129 `na` · per-54:160 `na` · per-54:261 `na` · per-55:79 `na`


---

## Part 16 — Reviewer items identical to existing audit items (no action; for traceability)

These reviewer changes were also proposed in Parts 1–8 (or differ only in wording). Implement the audit version; nothing to add.

| Place | Word | Reviewer's resulting row | Already in |
|---|---|---|---|
| per-01:46 | `mayaṃ` | `| mayaṃ | pron | 1.nom.pl | we |` | Part 4 (mayaṃ number) |
| per-01:126 | `sammā-` | `| sammā- | ind | adv | completely, thoroughly, fully, totally perfectly, rightly, correctly |` | Part 5.7 (strip period) |
| per-04:37 | `paccattaṃ` | `| paccattaṃ | ind | adv | for oneself, individually, personally |` | Part 5.10 (adv → Grammar, POS ind) |
| per-06:250 | `jānāma` | `| jānāma | verb | pr.1.pl | we know, understand |` | Part 4 (jānāma pr.1.pl) |
| per-06:366 | `sāvakesu` | `| sāvakesu | noun | masc.loc.pl | among disciples, pupils, lit. hearers |` | Part 2 (sāvakesu) |
| per-07:35 | `puna` | `| puna | ind | adv | again, once more |` | Part 5.7 |
| per-09:80 | `ariyaṃ-` | `| ariyaṃ- | adj | masc.acc.sg | noble, distinguished |` | Part 4 (ariyaṃ- masc.acc.sg) |
| per-14:122 | `ca` | `| ca | ind | conj | and |` | Part 5.10 (conj → Grammar, POS ind) |
| per-16:150 | `khaṇ'ātītā` | `| khaṇ'ātītā | adj | masc.nom.pl | who has missed the chance, who lost the opportunity, lit. moment passed by |` | Part 3 |
| per-16:205 | `eva` | `| eva | ind | emph | only, just, so, even |` | Part 5.4/5.7 |
| per-16:261 | `ayaṃ` | `| ayaṃ | pron | fem.nom.sg | this |` | Part 4 (ayaṃ → pron) |
| per-17:34 | `tattha tattha` | `| tattha tattha | ind | adv | in each and every case, right there, here and now, lit. there and there |` | Part 3 (same fix; reviewer gloss order differs — audit wording preferred) |
| per-17:68 | `saṅgaran-` | `| saṅgaran- | noun | nt.nom.sg | promise, agreement |` | Part 5.7 |
| per-18:136 | `dukkha-` | `| dukkha- | noun | | discomfort, suffering, pain, unease, something unsatisfactory, problem, trouble |` | Part 3 |
| per-18:247 | `me` | `| me | pron | 1.dat.sg | to me, for me |` | Part 2 |
| per-18:248 | `pubbe` | `| pubbe | ind | adv | before, previously, formerly, in the past |` | Part 5.11 (pubbe → adv) |
| per-18:391 | `paccaññāsiṃ` | `| paccaññāsiṃ | verb | aor.1.sg | I admitted, I claimed |` | Part 5.8 |
| per-27:80 | `antamaso` | `| antamaso | ind | | even so much as, even with, even down to, with as little as |` | Part 3 |
| per-27:82 | `pariyāpanna-` | `| pariyāpanna- | adj | | gone completely into, included in, belonging to, got into |` | Part 3 (reviewer also drops the stray `”`) |
| per-27:89 | `appaṭivibhatta-` | `| appaṭivibhatta- | adj | | not for oneself dividing, without reservations, not without sharing with others |` | Part 3 (reviewer keeps typo `onself`→`oneself` fixed but word order `not for oneself dividing`; audit wording preferred) |
| per-27:111 | `samādhi-` | `| samādhi- | noun | | perfect peace of mind, stability of mind, stillness of mind |` | Part 3 |
| per-27:138 | `diṭṭhi-` | `| diṭṭhi- | noun | | view, belief, opinion, concept, theory, opinion, attitude |` | Part 3 (reviewer still keeps duplicated `opinion`; audit version preferred) |
| per-28:82 | `yathā-` | `| yathā- | ind | | like, as, according to, on account of, because of, how |` | Part 3 |
| per-31:93 | `utuparissaya-` | `| utuparissaya- | noun | | inclement weather, harsh climate, lit. danger of the season |` | Part 3 |
| per-34:13 | `sahagatena` | `| sahagatena | pp | nt.ins.sg | with full of |` | Part 5.6 |
| per-34:14 | `cetasā` | `| cetasā | noun | nt.ins.sg | with a mind |` | Part 5.6 |
| per-34:51 | `sabbāvantaṃ` | `| sabbāvantaṃ | adj | masc.acc.sg | entire, whole |` | Part 2 |
| per-34:59 | `abyāpajjena` | `| abyāpajjhena | adj | nt.ins.sg | without ill will, with goodwill |` | Part 2 (spelling `abyāpajjhena` is separate → 12.5b) |
| per-41:63 | `tam'pi` | `| tam'pi | idiom | | that too, he too, even that, just that, that very thing |` | Part 1/3 (tam'pi → idiom) |
| per-41:76 | `jātiyā` | `| jātiyā | noun | fem.ins.sg | with birth, rebirth, conception |` | Part 2 |
| per-42:91 | `vinassatu` | `| vinassatu | verb | imp.3.sg | may disappear, vanish, perish |` | Part 4 (vinassatu imp.3.sg) |
| per-43:19 | `dukkha-` | `| dukkha- | noun | | discomfort, suffering, pain, unease, something unsatisfactory, problem, trouble |` | Part 3 |
| per-45:86 | `dukkha-` | `| dukkha- | noun | | discomfort, suffering, pain, unease, something unsatisfactory, problem, trouble |` | Part 3 |
| per-47:15 | `kālena` | `| kālena | ind | adv | timely, at the right moment, at a suitable time, at the proper time |` | Part 3 |
| per-47:54 | `appaṭivāna-` | `| appaṭivāna- | adj | | with confidence, without regret, lit. not shrinking back |` | Part 3 |
| per-51:44 | `te` | `| te | pron | 2.dat.sg | for you |` | Part 4 (te 2.dat.sg; POS → N-pos) |
| per-51:47 | `hotu` | `| hotu | verb | imp.3.sg | may it be |` | Part 4 (hotu imp.3.sg) |
| per-53:12 | `sutaṃ:` | `| sutaṃ: | pp | nt.nom.sg | what is heard; something heard |` | Part 4 (sutaṃ nt.nom.sg; gloss → N-gloss) |
| per-53:80 | `brūhi` | `| brūhi | verb | imp.2.sg | say!; tell!; speak! |` | Part 4 (brūhi imp.2.sg; gloss → N-gloss) |
| per-57:43 | `paccattaṃ` | `| paccattaṃ | ind | adv | for oneself, individually, personally |` | Part 5.10 |

Also identical to the audit:
- **Translations (4 lines):** per-01:159 `I venerate to the Teaching.` → `I venerate the Teaching.` (Part 6); per-42:43 `May your desires and wishes be succeeds only quickly.` → `…succeed quickly.` (Part 6); per-42:104 `May danger does not be for you.` → `May there be no danger for you.` (Part 6); per-45:133 `May be f or you` → `May there be for you` (Part 6).
- **Row deletion:** per-37 duplicate `matthaluṅgaṃ` (reviewer removed the row at L55 `| matthaluṅgaṃ | noun | nt.nom.sg | the brain |`) = audit **D1** (the reviewer did *not* remove the first `brain` from the translation line; D1 asks to).
