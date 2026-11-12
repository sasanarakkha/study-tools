# Audit of `docs/6-pali-class/suttas/`

Date: 2026-11-10 (first pass and second-pass review on the same day). Scope: quality of the grammatical analysis, the English sentence translations, and consistency of file format. Review only; no file in `docs/` was edited.

The folder has three different problems: the format is not uniform across files, the grammatical analysis has a steady rate of real errors (though it is sound in the main), and the sentence translations have omissions and copy-paste slips.

Locations are given as `file:line`, where `22-94` means `sn-22/22-94.md` and `mn107` means `mn-107-ganakamoggallanasuttam.md`.

## What the second pass changed

The second pass re-checked every location and count in the first version against the source, then covered the parts the first pass had left open.

- **All cited rows exist as quoted.** Every `file:line` in the first version was printed from the source and matches.
- **Counts corrected:** `<br>` occurrences (71, not 82), the missing-ID figures (the denominators were mixed), and the SN 12 description (no row is analysed, and the bold blocks are Pāli, not translations).
- **One finding downgraded:** `labheyyaṃ` and `puccheyyaṃ` tagged reflexive is a convention matter, not a definite error. `vihareyyāmi` tagged reflexive remains an error.
- **Scope widened:** the instruction paragraph is also in MN 107; curly quotes are in more files than listed.
- **New material:** about 70 further grammatical errors, a table-against-text check, and a first review of the sentence translations.

## Coverage

- **Read in full, twice:** all 3,687 unique analyses (from 10,246 filled rows). The first pass read a– to nis– in full and the rest partly; the second pass had the whole list read again by three independent reviewers, and every item they raised was checked against the source row.
- **Read in full, once:** all 365 Pāli passage / English translation pairs in the SN 22, SN 35, SN 56 files and MN 107.
- **Checked by script only:** whether each table matches its Pāli passage word for word. The check is noisy because tables expand `... pe ...` and split sandhi, so only the mismatches confirmed by eye are listed.
- **Not reviewed:** the English gloss of each individual row, the DPD ID numbers, and the Pāli text against an external edition (CST).

## State of the corpus

| Group | Files | State |
|---|---|---|
| `sn-22/`, `sn-35/`, `sn-56/` | 49 | Fully analysed, 6 columns, sentence → table → bold translation |
| `mn-107-ganakamoggallanasuttam.md` | 1 | Fully analysed, but a different format (below) |
| SN 43, 45, 46, 47 combined files | 4 | Stubs: Pāli text plus ID/word lists, all analysis cells empty |
| `nidana-samyutta-sn-12.md` | 1 | Stub: Pāli text with 21 passages in bold, 643 ID/word rows, all analysis cells empty, no translations |
| SN 22 / 35 / 56 index files | 3 | Link lists |

## Format findings

### Structural (highest priority)

1. **MN 107 has no ID column** (5 columns against 6 everywhere else). It also uses `para N` markers, apostrophe sandhi (`ten’upasaṅkami`), and its own POS labels (`pn`, `ord`, `(pp as) adj`).
2. **The ID column is largely empty in many SN files.** Counting all filled rows:
   - Worst: `35-232` 430 of 531 rows without an ID, `35-247` 342 of 536, `22-82` 320 of 523, `35-241` 286 of 526, `35-70` 229 of 320, `22-59` 193 of 346.
   - Every SN 35 file is affected (between 48% and 81% of rows).
   - Complete: `22-12`, `22-18`, `22-23`, `22-24`, `22-28`, `56-1`, `56-5`, `56-13`, `56-25`, `56-27`, `56-28`. The other SN 56 files miss at most 7 rows each.
3. **Stub tables have no header row.** The first vocabulary word sits above the `| --- |` line, so it renders as the table header (e.g. `| 9320 | asaṅkhataṃ |` in SN 43). Affected tables: SN 43 (3), SN 45 (7), SN 46 (7), SN 47 (8), SN 12 (7).
4. **`nidana-samyutta-sn-12.md` lines 818–862 have 7 columns** instead of 6 (45 rows).
5. **The example row leaked in as a table header** at `nidana-samyutta-sn-12.md:371` and `sn-35/35-232.md:662`. The second sits under a duplicate of the preceding translation.
6. **Raw `<br>` appears 71 times in table cells**, which the project's clean-Markdown rule forbids. The files with most are MN 107 (16), `35-247` (9) and `22-26` (6).
7. **Link label and target disagree:** `maggasamyutta-samyutta-sn-45.md:11` says "SN45.49" but points to the heading "SN45.56".
8. **The instruction paragraph** ("Please make line by line translation…") plus an example table is published in nine files: the three index files, the five combined files and MN 107. Seven say "in the last column", two "on the last column".
9. **Pāli passages are hard-wrapped in mid-sentence** in most SN 35 files and ten SN 56 files (worst: `35-247`, `35-241`, `35-232`, `35-246`). The other files keep one paragraph per line.
10. **One Pāli passage is split over several tables** without repeating the Pāli: MN 107 (the opening passage over five tables, and five more places) and `56-1` (twice).
11. **MN 107 lines 1081–1095:** two compound-member rows (`\#vitakkā (ca)`, `\#vicārā \*ca)`) stand outside the table as loose lines.

### Convention drift

- **Sandhi:** MN 107 uses a `sandhi` row plus `#` sub-rows; the SN files mix inline `rūpasmim+api`, `sandhi` rows, and POS such as `noun+ind`, `pron+verb`. `etadavoca` is tagged three different ways (`pron+verb`, `sandhi` with `ind+aor.3rd.sg`, `sandhi` with `pron+aor.3rd.sg`); `etad` is a pronoun, so the `ind+` variants are also wrong.
- **Compound members:** decorated inconsistently as `(ca)`, `+ke`, `(in comps)`, `<br>(ca)`, or a trailing `-`.
- **Multi-word cells:** `na madāya`, `bhavaṃ gotamo`, `ehi tvaṃ`; punctuation left in the Pāli cell (`vineti —`, `saṃvasati”`, `dasakā’ti`).
- **Headings:** `SN 43.1` against `SN46.1`; title case is mixed (`Aniccasutta` / `tatiyāssādasutta`); "Bojjhaṅgasaṃyutta Saṃyutta" and "Maggasaṃyutta Saṃyutta" are redundant; `56-28` lacks the `---` after the full text.
- **Quotes:** curly quotes and apostrophes appear in MN 107, the SN 12, 43, 45 and 46 files and 15 of the 18 SN 56 files, and nowhere else.
- **Capitals:** 15 of the 18 SN 56 files capitalise the first word of each Pāli sentence, and the capital is carried into the table (`Appamattakāni`, `Āditte`, `Kiṃ`). All other files are lower case.
- **Stray characters:** 80 construction cells have an unbalanced `[` or `]`; there are escaped backticks (``opt.3rd.sg\` `` at `22-95:356`, `:360`, `22-82:58`), bold inside a cell (`aññathābhāv**ino**`), and a capital inside a word (`nibbindatI`, `22-59:397`, `:399`).

### Label vocabulary

- **POS has 66 distinct values.**
  - Typos: `veerb`, `insd`, `nou`, `prom`, `pron.`, `ind.`, `adj (app)`, `inf` for `ind` (`sace`, `22-82:133`).
  - Gender used as POS: `masc` (`35-28:268`), `nt` (6 times in `56-44`).
  - Synonyms: `ptp` / `fpp` / `adj (ptp)`; `pp (adj)` / `pp/adj` / `pp(adj)` / `adj (pp)` / `(pp as) adj`.
  - Nine rows have no POS.
- **Grammar has about 300 distinct values.**
  - Typos: `masc.nomsg` (18), `masc.acc.g` (9), `masc.voc,sg` (6), `masc.genb.sg` (4), `nt.acc.ag` (2), `nt.inst.sg` (2), `fen.gen.sg`, `nt.no.sg`, `masc.nomm.sg`, `masc.nom.pl.medium`.
  - Impossible tags: `masc.fem.sg`, `masc.fem.nom`, `nt.masc.pl`, `fem.nom.acc`.
  - Variants: `abs` / `abs.` / `ger` / `ger/abs` / `abs/ger`; `reflex` / `reflx`; `loc abs` / `loc. abs` / `loc.abs`; `quotation mark` / `quotation` / `quote`.
- **Compound types mix Pāli and English.**
  - `chaṭṭhī tappurisa` (155) sits beside `genitive tappurisa`, `accusative`, `locative`, `instrumental`, `dative`, `ablative tappurisa?`.
  - Misspellings: `chaṭṭa`, `chaṭṭha`, `chatti`, `dutiya`, `sattāni tappurisa (?)`, `kammādhāraya`, `avyayībhāva`.
  - The bahubbīhi notation has seven spellings (`kammadhāraya\> bahubbīhi`, `kammadhāraya \> bahubbīhi`, `kammadhāraya\>bahubbīhi`, `kammadhāraya \>bahubbīhi`, `kammadhāraya\><br>bahubbīhi`, `kammadhāraya as bahubbīhi`, plain `bahubbīhi`).
- **The Construction column holds three kinds of content:** root derivation, compound type, and free commentary ("*probably truncated ablative (Bodhi)", "(the entire chain is a dvanda)").
- **Two derivation notations:** MN 107 uses the full DPD style (`ni√sad･1 a (sink, sit, settle)+…`); the SN files use `ni + √sad + a + na`.
- **178 non-present verbs carry a present-tense construction** ending in `+ ti` (100 optatives, 52 futures, 26 imperatives; e.g. `desessāmi` → `√dis + *e + ti`), while others show the real ending.
- **35 rows have a truncated construction** (11 distinct: `√vad`, `[√vad`, `vi + ā + √pad`, `nī + √sar`, `saṃ + √chid`, `√caj`, `nī + √yat`, `vi + √likh`, `ud + √i`, `upa + ni + √khip`, `vi + √takk`).
- **Prefix dropped from the construction** in MN 107: `āhāreyyāsi` (`:548`), `paripūreti` (`:1060`), `parisodhehi` (`:643`), `parisodheti` (`:909`), `paṭipucchissāmi` (`:1405`).

## Grammatical findings

### Definite errors

Rows marked † were added in the second pass.

**Verbs: person, number, voice**

| Location | Row | Problem |
|---|---|---|
| `22-94:54` (10 rows) | `vadāmi` pr.3rd.sg | 1st.sg |
| `35-118:100` (3 rows) | `santi` pr.3rd.sg | 3rd.pl |
| `35-230:136` | `abhinandati` pr.3rd.pl | 3rd.sg |
| `22-63:62` | `vihareyyāmi` opt.reflex.1st.sg | active; and the text reads `vihareyyaṃ` (see table-against-text) |
| `56-33:61` | `gacchanti` construction `√gam + a + nta` | `+ nti` |

**Wrong POS**

| Location | Row | Problem |
|---|---|---|
| `22-12:74` (4 rows) | `karaṇīyaṃ` POS `prp` | ptp |
| `35-118:234–235` | `anabhinandato`, `anabhivadato` POS `pp` | prp (the construction itself ends in `nta`) |
| `56-47:65` | `ummujjanto` POS `pp` | prp |
| `22-26:23` | `anabhisambuddhassa` POS `noun` | pp |
| `22-58:188` | `akkhātā` pp, `ā + √khā + ta` | agent noun (akkhātar), not a pp |
| `35-28:268` | `attano` POS `masc` | pron/noun |
| `35-241:645` | `atthāya` POS `adj` | noun |
| `22-12:29` | `evaṃ` ind, grammar `adj` | adv |
| † `mn107:1006` | `so` POS `ind` | pron masc.nom.sg |
| † `22-78:37` | `samantā` adj/ind, fem.acc.pl | indeclinable; no case tag |
| † `22-59:347` | `bahiddhā` adj nt.nom.sg | indeclinable |
| † `mn107:321` | `sīlavā` POS `noun` | adj (as at `mn107:355`) |

**Wrong case or number**

| Location | Row | Problem |
|---|---|---|
| `22-82:505, 511, 517` | `saññā-/saṅkhāra-/viññāṇakkhandhassa` masc.nom.sg | gen/dat |
| `35-118:237` | `tiṭṭhato` masc.nom.sg | dat/gen |
| `35-28:50` | `bhikkhū` masc.acc.sg | acc.pl |
| `mn107:191`, `:195` | `dve` masc.acc.sg; `cattāri` nt.nom.sg | plural |
| † `mn107:193` | `tīṇi` nt.nom.sg | plural |
| `mn107:993`, `:994` | `kusalesu`, `dhammesu` loc.sg | loc.pl |
| `mn107:1170` | `atthaṅgamā` instr.sg | abl.sg |
| † `mn107:1172` | `#gamā` instr.sg | abl.sg |
| † `mn107:1097` | `vūpasamā` masc.instr.sg | abl.sg ("vitakkavicārānaṃ vūpasamā") |
| `35-246:154` | `me` 1st.acc.sg | dat ("for me") |
| `22-82:65` | `##mātuyā` fem.loc.sg | gen |
| `22-23:65`, `:67` | `pariññeyyā` masc.nom.sg; `katamā` masc.fem.sg | first is nom.pl; second fem.nom.sg |
| † `22-26:47` | `saññāya` fem.nom.sg | gen.sg |
| † `22-58:185` | `sañjanetā` masc.gen.sg | nom.sg (agent noun, like `uppādetā` at `:182`) |
| † `22-59:398` | `viññāṇasmim+api` nt.nom.sg | loc.sg |
| † `22-78:299` | `tathāgato` masc.nom.pl | nom.sg |
| † `22-33:96` | `#paccayaṃ` masc.nom.sg | acc.sg |
| † `22-102:115` | `#tārakāya` fem.gen.pl | gen.sg |
| † `22-18:86` | `niccā` nt.nom.sg | masc.nom.pl (agrees with `saṅkhārā`) |
| † `22-95:76, 79, 82` | `rittakaṃ`, `tucchakaṃ`, `asārakaṃ` masc.nom.sg | nt.nom.sg |
| † `35-93:101` | `aniccaṃ` masc.nom.sg | form and tag disagree |
| † `35-118:245`, `:247` | `tadupādānaṃ`, `#upādānaṃ` masc.nom.sg | nt.nom.sg (as at `:135`, `:137`) |
| † `35-136:67` | `phoṭṭhabbārāmā` masc.loc.pl | nom.pl |
| † `56-13:133` | `#kāmesu` masc.loc.sg | loc.pl |
| † `56-13:126` | `tatratatrābhinandinī` masc.fem.sg | fem.nom.sg |
| † `56-31:142–147` | `#saṃhitaṃ`, `nādibrahmacariya+kaṃ` and its two members, masc.nom.pl | nt.nom.sg |
| † `56-42:243` | `jātisaṃvattanike+pi` masc.loc.pl | acc.pl (agrees with `saṅkhāre`, tagged acc.pl in the next row) |
| † `56-49:56` | `#pabbatarājā` masc.gen.pl | nom.sg |
| † `mn107:748` | `saṅghāṭipattacīvaradhāraṇe` nt.nom.sg | loc.sg |
| † `mn107:1089` | `vitakkavicārānaṃ` masc.acc.sg | gen.pl |
| † `mn107:1167` | `somanassadomanassānaṃ` nt.acc.sg | gen.pl |
| † `mn107:1875` | `anuyuttā` masc.nom.sg | nom.pl |
| † `mn107:1922`, `:1933`, `:1942` | `mūlagandhā`, `sāragandhā` masc.nom.sg; `pupphagandhā` masc.abl.sg | all nom.pl ("ye keci …gandhā") |
| † `mn107:18` | `sutaṃ` masc.acc.sg | nt.nom.sg ("evaṃ me sutaṃ") |

**Wrong root, prefix or suffix**

| Location | Row | Problem |
|---|---|---|
| `35-53:51` (10) | `jānato` construction `√ñā + nā + a` | `+ nta` |
| `22-78:262`, `22-26:27`, `35-230:163` | `samānā`, `sato`, `santi` with `sa + √as` | no `sa` prefix |
| † `mn107:953` | `sato` "mindful" with `sa√as … (be)` | √sar + ta (as at `mn107:679`) |
| † `22-63:76`, `35-28:282` | `anupādiyamāno`, `anupādāya` with `√ādā` | `ā + √dā` |
| † `22-78:117` | `baddhā` with `√badh` | √bandh |
| † `mn107:944` | `#thīna` with `√thī + ana` | `+ na` |

### Reclassified: not a definite error

- `labheyyaṃ` (`35-241:532`, 4 rows) and `puccheyyaṃ` (`22-82:127`) tagged reflexive. The first version called these "ordinary active optatives". In traditional grammar `-eyyaṃ` is the attanopada (reflexive) 1st.sg optative ending and `-eyyāmi` the active one, so the tag is defensible. Modern grammars list `-eyyaṃ` as active. Decide one convention in the schema and apply it; the gloss "I would obtain myself" should go either way.

### Wrong gender

- **Neuter tagged masc:**
  - MN 107: `cittaṃ` (`:642`); `cakkhundriyaṃ` and `manindriyaṃ` (`:418, 439, 440, 490, 511, 512`); `rūpaṃ` (`:396`); `ghānena` (`:454`); † `sotena` (`:451`); † `phoṭṭhabbaṃ` (`:461`); † `bhojane` (`:608`); † `satisampajaññena` (`:804`); † `#vanānaṃ` (`:1558`); † `#jaṃ` (`:1037`, `:1108`); † `#karaṇīyaṃ` (`:1231`); `kāraṇaṃ` (`:288, 292`); † `avitakkaṃ`, `avicāraṃ`, `samādhijaṃ` (`:1104–1106`).
  - SN files: `rūpesu` (`35-70:90`); † `rūpasmim+api` (`22-59:390`, `22-95:554`); † `#rūpe` (`22-102:34`); † `#phoṭṭhabbesu` (`35-136:68`); † `#kulānaṃ` (`22-63:243`); † `#kiṃ` (`56-1:36`).
- **Masc tagged nt:** `pāde` (`mn107:676`); † `pādaṃ` (`mn107:677`); `attena` (`35-85:50`); † `anuggahāya` (`mn107:576`); † `dhamme` (`35-247:537`).
- **Fem tagged otherwise:** `gīvaṃ` nt (`56-47:69`); `appaṭivānī` masc (`56-34:64`); `dukkhanirodhagāminī` masc (`56-1:122`, but fem at `56-1:65`); † `sassamaṇabrāhmaṇiyā` masc (`22-26:202`); † `paññāpanā`, `paṭṭhapanā`, `vivaraṇā`, `vibhajanā` nt (`56-38:160–163`; `ācikkhaṇā` at `:157` is fem); † `paññāpanāya` nt (`22-82:494`).
- **Self-contradicting:** `cittāni` tagged `nt.masc.pl` (`35-28:284`).
- **Split within one file:** `jāgariyaṃ` fem and nt, `bhojane` nt and masc, `satisampajaññena` nt and masc (all MN 107); `kulānaṃ` nt and masc across files.

### Wrong or doubtful compound analysis

- `khīṇāsavā`, `katakaraṇīyā` given as "dutiyā tappurisa" (`mn107:1225, 1229`): these are bahubbīhi.
- `attamanā` given as "chaṭṭhī tappurisa" (`35-28:267`): bahubbīhi.
- `bhikkhusahassena` given as "digu" (`35-28:45`, and `bhikkhusahassassa` at `:281`): chaṭṭhī tappurisa. `chappāṇake` given as "kammadhāraya" (`35-247:293`): this one is the digu.
- `dhammamayo` given as "instrumental tappurisa" (`35-228:104`, `:110`): `-maya` is a suffix, not a compound member.
- `pātimokkhasaṃvarasaṃvuto` given as "sattamī tappurisa" (`mn107:323`): tatiyā.
- † `piṇḍapātapaṭikkanto` given as "dutiyā tappurisa" (`mn107:875`): pañcamī ("returned from alms round").
- † `savitakkaṃ`, `savicāraṃ` given as "kammadhāraya" (`mn107:1029, 1032`): bahubbīhi.
- † `pacchāmukho` given as "abyayībhāva" (`mn107:1583`): a declined adjective, so bahubbīhi (as at `mn107:1656`). `parimukhaṃ` given as "kammadhāraya" (`mn107:886`): this one is the abyayībhāva.
- † Adjectives of persons given as plain "kammadhāraya" where sibling rows use "kammadhāraya > bahubbīhi": `mahiddhiko` (`22-78:134`), `sukhabahulā` (`22-78:231`), `muṭṭhassatino` (`mn107:1819`), `duppaññā` (`mn107:1827`), `pakkagatto` (`35-247:99`), `arugatto` (`35-247:96`), `evaṃsamācāro` (`35-247:164`), `acakkhukaṃ` (`22-94:311`), `vigatavalāhake` (`22-102:150`).
- † `anuppattasadatthā` "dutiyā tappurisa" and `apattamānasā` "kammadhāraya" (`mn107:1235, 1198`): both bahubbīhi.
- † `sīsapāvane` "kammadhāraya" (`56-31:30`): chaṭṭhī tappurisa ("grove of sīsapā trees").
- The same compound is labelled differently: `dukkhanirodhaṃ` (chaṭṭhī tappurisa at `56-1:66` / "kammadhāraya > bahubbīhi" with POS noun at `56-13:42`), `andhakāratimisā` (kammadhāraya fem.sg at `56-38:46` / dvanda nt.pl at `56-38:104`), `mahiddhiko` / `mahesakkho` (`22-78:134`, `:144`).

### Other doubtful rows (lower certainty, worth a second look)

- `bhūmirāmaṇeyyakaṃ` adj masc.acc.sg (`mn107:1560`), and the sister compounds at `mn107:1556–1566`: these look like neuter nouns.
- `khemaṃ` noun masc.acc.sg (`mn107:1204`).
- `saṃhitaṃ`: see definite errors.
- `vutte` masc.loc.sg (`mn107:1273`) against nt.loc.sg (`35-241:246`).
- `doṇiṃ` tagged `fem.nom.acc` (`35-246:243`): fem.acc.sg.
- `nibbānaninnā` tagged `masc.fem.nom` (`35-241:230`).
- `#gayāyaṃ` as a member of `gayāsīse` tagged fem.gen.sg (`35-28:42`): the form is locative; the genitive member would be `gayāya`.
- `me` 1st.instr.sg glossed "to me" (`mn107:17`): gloss does not match the tag ("by me").
- `aññamañña` labelled "dutiyā tappurisa" (`56-47:159`).
- `āvuso` POS ind with grammar `masc.voc.sg` (`35-232:97`).
- † `daḷhāya` pp with `√dah + ta` (`35-247:303`): `daḷha` is normally an adjective, and √dah is "burn".
- † `thullaphusitake` noun nt.loc.sg (`22-95:150`): agrees with `deve`, so masc and adjectival.
- † `āmisacakkhu` nt.nom.sg (`35-230:45`): qualifies `maccho`.
- † `Āditte` masc.loc.sg (`56-34:25`): with `cele vā sīse vā`, nt.
- † `saddhā` fem.instr.sg (`mn107:1775`): ablative in "saddhā agārasmā anagāriyaṃ pabbajitā".
- † `sugatā` masc.nom.sg (`22-63:90`), `upadhāraṇe` nt.acc.pl (`35-246:252`), `āyaṃ` pron fem.nom.sg (`35-246:333`), `asatī` prp fem.nom.sg (`35-246:331`): form and tag disagree; check against the sentence.
- † `sārapariyesanaṃ` ind adv (`22-95:335`): object of `caramāno`, so a noun in the accusative.
- † `#mattāyo` POS pp (`56-49:33`): noun.
- † `dukā`, `tikā`, `catukkā`, `chakkā`, `aṭṭhakā`, `dasakā` nt.nom.pl (`mn107:192–208`): the `-ā` ending points to masc.
- † `#sacchi` POS adj (`22-63:263`): indeclinable.
- † `passena` nt (`mn107:671`), `padakkhiṇaṃ` fem (`22-63:216`), `vajjesu` masc (`mn107:335`), `#pheṇa` nt (`22-95:58`), `#pubbuḷe` nt (`22-95:92`), `#saṃvaccharā` "nt (or masc.)" (`56-38:67`), `#addhānaṃ` nt.nom.sg (`56-21:53`): gender to be checked against DPD.
- † `kiccakaraṇīyesu` "kammadhāraya" (`35-241:357`): probably dvanda. `giriguhaṃ` (`mn107:831`), `gijjhakūṭe` (`35-118:29`), `chandarāgavemattatā` (`22-82:342`) "kammadhāraya": probably chaṭṭhī tappurisa.

### Pāli typos

**In the word column**

- `kukkurao` (`35-247:381`), `imina` (`35-241:390`), `ko nu kno` (`22-26:37`), `pajānati` (`56-49:157`, 4 rows), `viññāṇasmim` without `pi` (`22-12:44`), `itthattāyā` (`22-12:76`).
- `bhagavā` tagged instr.sg (`56-31:86`): the passage has `bhagavatā`.
- † `rūpasssa` (`22-26:121`), `##rajā` (`56-49:58`), `viharāti` (`mn107:362`), `nibbindatI` (`22-59:397`, `:399`), `dukkhanirodhagāminim` (`56-44:39`, 4 rows).
- † `thīnamiddhaṃ`, `vigatathīnamiddho` (`mn107:943–949`) against `thinamiddhaṃ` in the passage (`mn107:939`).

**In the Pāli passages**

- † `manoiññeyyā` for `manoviññeyyā` (`35-118:17`, `:199`).
- † `pajānātiti` for `pajānātīti` (`22-95:25`, `:545`).
- † `22-95:47`: the foam simile ends "kiñhi siyā, bhikkhave, udakapubbuḷe sāro"; the full text at line 5 has `pheṇapiṇḍe`. The translation follows the wrong word ("in a water bubble?").
- † `56-5`: the full text (line 5) reads `abhisambujjhanti`; the split passages and tables (`:65`, `:79`, `:87`, `:150`, `:159`) read `abhisambojjhanti`. One spelling should be chosen after checking the source edition.
- † `22-102:199`: the passage starts mid-sentence ("rūpassa samudayo…"); the opening "kathaṃ bhāvitā ca, bhikkhave, aniccasaññā…" is missing, though the table and the translation cover it.
- † `mn107:1048–1160`: the pervasion simile ("so imameva kāyaṃ vivekajena pītisukhena abhisandeti…") and three passages addressed "puna caparaṃ, bhikkhave, bhikkhu" do not look like MN 107, which is spoken to a brahmin and gives the jhāna formulas without similes. Check against the source edition; if confirmed, the text was pasted from another sutta.

### Table against text †

Places where the table does not carry the words of its passage (confirmed by eye):

- `22-82:525`: the passage has "nāmarūpaṃ hetu, nāmarūpaṃ paccayo viññāṇakkhandhassa paññāpanāya"; the table has `phasso hetu phasso paccayo`, and the translation follows the table ("Contact [is] the cause…").
- `22-95:394`, `:397`, `:486–492`: the table has `khāyati` (pr) where the passage has `khāyeyya` (opt), in the plantain-trunk and magic-show similes.
- `22-63:62`: the table has `vihareyyāmi`; the passage has `vihareyyanti` (`vihareyyaṃ` + `ti`).
- `22-78:19`: `nadati` is missing after `sīhanādaṃ`.
- `35-230:161`: `abhedi baḷisaṃ, paribhedi baḷisaṃ` is missing from the table and from the translation.
- `35-118:151`: the closing sentence "ayaṃ kho, devānaminda, hetu, ayaṃ paccayo yena-m-idhekacce sattā diṭṭheva dhamme no parinibbāyanti" is missing from the table and from the translation.
- `56-31:134`, `:201`: `sambodhāya` is missing, the repeated `na` is dropped, and the table has `saṃvattanti` for `saṃvattati`.
- `56-31:166`: the passage includes the "Kasmā cetaṃ…" section, which is then repeated as its own passage at `:199`.
- `mn107:915`, `:941`, `:962`: `viharati` is missing from the table.

### Systematic inconsistencies

- Passive against active: `virajjati`, `vimuccati`, `nirujjhati` are `pr.pass` in some files and `pr` in others.
- Causative marking: `deseti` / `desessāmi` appear both as `pr.caus` / `fut.caus` and plain `pr` / `fut`.
- `addasā` is `imperf` once (`35-241:76`); all similar forms are `aor`.
- `ger` is used for `-ya` forms and `abs` for `-tvā` forms in most files, but `ger/abs`, `abs/ger` and `abs` on `-ya` forms (`samādāya`, `viññāya` in MN 107) also occur.
- Cardinal numbers: `x.nom.pl`, `masc.x.pl`, `(in comps)` and plain gender labels are all used.
- Reflexive optatives: see "Reclassified" above.

## Translation findings †

Line numbers are the first line of the table whose bold translation is affected. Stylistic roughness and literal renderings are not listed.

### Mistranslations

| Location | Pāli | Given | Problem |
|---|---|---|---|
| `22-33:125` | taṃ kissa hetu? na hi no etaṃ, bhante, attā vā attaniyaṃ vā | "Because, Venerable Sir, the self is not what belongs to oneself." | "Why is that? Because this is not our self or what belongs to our self." |
| `22-59:328` | sabbaṃ viññāṇaṃ | "all form should be seen" | consciousness |
| `22-94:135` | viññāṇaṃ aniccaṃ dukkhaṃ | "[that is] permanent, suffering" | impermanent |
| `22-82:525` | nāmarūpaṃ hetu… viññāṇakkhandhassa | "Contact [is] the cause…" | name-and-form |
| `22-95:49` | pheṇapiṇḍe sāro | "in a water bubble?" | in a lump of foam |
| `22-102:54` | mahānaṅgalena | "with a great soil" | plough |
| `22-78:256` | bho (4 times, devas to each other) | "Venerable Sir" | "sirs" / "friends" |
| `35-228:97` | dhammamayaṃ vegaṃ | "current made of forms" | mental objects (copied from the eye section) |
| `35-246:359` | evameva kho, bhikkhave | "Just as, monks" | "In the same way" (it applies the simile) |
| `35-247:288`, `:566` | bandheyya | "we would bind it" | he would bind |
| `mn107:255` | sakkā, brāhmaṇa, … paññapetuṃ | "Is it possible, Brahman, to define…" | a statement: "It is possible" |
| `mn107:272` | seyyathāpi, brāhmaṇa, dakkho assadammako | "Brahman, even a skilled trainer of horses" | "Just as, brahman, a skilled horse-trainer" |
| `mn107:520` | yato kho, brāhmaṇa, bhikkhu … hoti | "Because, brahman, as a monk is…" | "When, brahman, a monk is…" (as at `:351`, `:711`) |
| `mn107:869` | parimukhaṃ satiṃ upaṭṭhapetvā | "with the intention of setting up mindfulness" | absolutive: "having set up" |
| `mn107:1544` | dakkhissasi rājagahassa ārāmarāmaṇeyyakaṃ … | "you will see Rājagaha, pleasant as a park…" | "you will see the delightful parks, groves, grounds and ponds of Rājagaha"; "tena muhuttaṃ gantvā" is also left out |
| `mn107:1974` | seyyathāpi, bho gotama, nikkujjitaṃ vā ukkujjeyya, … mūḷhassa vā maggaṃ ācikkheyya | "as if Master Gotama would turn upside down or turn right side up and uncover what was hidden for a deluded person…" | `bho gotama` is a vocative, not the subject; "set upright what was overturned"; `mūḷhassa` goes with "show the way" |

### Words or clauses left untranslated

- `22-102:144`: `bhāsate ca tapate ca virocate ca` (the main verbs).
- `22-63:117`, `:154`: "anupādiyamāno mutto pāpimato" for form; `:202`: `pakkāmi`, leaving the sentence unfinished.
- `22-78:156`: `sugato`.
- `22-82:639`: `ariya` in "sutavā ariyasāvako".
- `22-94:199`, `:228`, `:323`: `vibhajati` in each list; `:288`, `:354`: `tathāgatena`.
- `35-118:151`, `35-230:161`: see table-against-text.
- `35-241:430`: `kasambujāto`.
- `35-246:68`: "so evaṃ vadeyya"; `:287`: "ettha ca mahājano ativelaṃ pamatto palaḷito".
- `35-93:50`: "rūpā aniccā vipariṇāmino aññathābhāvino".
- `56-31:134`, `:201`: `sambodhāya`.
- `56-33:40`: `gacchanti`.
- `56-34:23`: `bhikkhave`.
- `56-38:121`: two full sentences ("neva tāva mahato ālokassa pātubhāvo hoti… andhakāratimisā").
- `56-47:26`: "vassasatassa vassasatassa accayena sakiṃ sakiṃ ummujjanto" in the question.
- `56-49:67`: "sinerupabbatarājānaṃ upanidhāya".
- MN 107: `brāhmaṇa` (`:299`), `bhikkhave` (`:1081`, `:1158`), "icchāmahaṃ, bhante, rājagahaṃ gantuṃ" (`:1471`), "evaṃ anusāsīyamāno" (`:1610`), `brāhmaṇo` (`:1749`), "bho gotama" (`:1915`).

### Typos and broken English

- `22-26:170`, `:223`: "Marā". `22-58:19`, `:53`: "non-clininging". `22-82:125`, `:270`, `:476`: "the Blessed" without "One". `22-95:143`: "rains clouds".
- `35-136:33`: "cessations". `35-228:55`, `:97`: "a persons ocean". `35-241:67`: "[it[". `35-241:577`: "cowhere". `35-247:401`: "would go it [its] control".
- `56-13:103`: "The craving that which is leading". `56-21:93`: "the way of leading". `56-33:20`: "a stick … fall once". `56-42:140`: "also leading to old age also". `56-31:168`: missing space after a closing quote.
- MN 107: `:214` unmatched bracket "(lit: cause … to count]"; `:962` "[his] the mind"; `:1285` "finalgoal"; `:1626` "you, as encourager, exists".

### Doubtful

- `22-95:324`: `akukkukajātaṃ` as "not crooked" (commentary: without a fruit-bud core).
- `35-230:131`, `:161`: `gilitabaḷiso mārassa` as "swallowed the bait of death"; `baḷisa` is "hook" elsewhere in the file.
- `35-241:286`: `nandīrāga` as "desire and lust" (delight and lust).
- `35-246:39`: "santiṭṭhati sannisīdati ekodi hoti samādhiyati": four verbs, the last not clearly rendered.
- `56-21:36`, `:70`, `:93`: "evamidaṃ dīghamaddhānaṃ sandhāvitaṃ saṃsaritaṃ mamañceva tumhākañca": the English has no main verb.
- `mn107:604`: `yato kho` as "Because". `mn107:1763`: `uddhatā` as "haughty".

## Recommendation

Fix in this order:

1. **Decide the canonical schema**: 6 columns with ID, one sandhi convention, a closed POS/Grammar/compound vocabulary, one rule for `-eyyaṃ` optatives, one rule for capitals, quotes and line wrapping in Pāli passages. Write it down; everything else depends on it.
2. **Normalise the labels mechanically** with a script (typos, synonyms, brackets, `<br>`). This is low risk and removes most of the noise.
3. **Correct the Pāli text and table-against-text mismatches**, since tables and translations hang on them. Check the MN 107 passage at lines 1048–1160 against the source edition first.
4. **Correct the grammatical errors and the translations above by hand.**
5. **Backfill the missing IDs and convert MN 107**, which is the largest job.

Optional follow-up: turn the checks used for this audit into a permanent verifier script (new script plus README entry) so regressions are caught. Not started.

## Remaining work for a complete audit

- The Pāli text of every file against a source edition (CST). Only internal inconsistencies were caught here.
- The English gloss of each table row, and the DPD ID numbers.
- A full manual word-for-word check of tables against passages; the script check finds only gross mismatches.
- A second independent read of the translations. They were read once.

## Method

- All filled table rows were extracted by script (10,246 rows) and deduplicated to 3,687 unique analyses (word, POS, grammar, construction).
- Format counts (columns, headers, missing IDs, `<br>`, label vocabularies, brackets) come from scripts run over all 58 files. In the second pass they were recomputed with independently written scripts.
- First pass: grammatical findings came from reading the deduplicated list (first half in full), plus heuristic checks of ending against case/number, POS against construction suffix, and gender conflicts for the same word form.
- Second pass: every cited row was printed from the source; a new ending-against-tag heuristic was run over all rows; the full list of unique analyses was read by three independent reviewers and the 365 passage/translation pairs by three more. Each item they raised was checked against the source before it was listed, and items that rested on a different dictionary convention were dropped.
- The scripts were temporary and live in the session scratchpad, not in the repository.

## Confidence

- 9/10 on the format findings, which are counted by script and were recounted.
- 8/10 on the rows under "Definite errors" and "Wrong gender". The gender items assume the usual dictionary gender; a few may differ in DPD.
- 7/10 on the translation findings. The quoted English was confirmed in the files, but the judgement was made by one reader per file.
- 7/10 that the grammatical list is complete, and 5/10 for the translations and Pāli text, for the reasons under "Remaining work".
