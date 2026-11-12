# Audit of `docs/6-pali-class/bhikkhu-patimokkha/`

Date: 2026-11-10. Scope: the grammatical analysis, the word glosses, the English sentence translations, table-against-text agreement, and consistency of format. Review only; no file in `docs/` was edited.

The folder is structurally uniform and the analysis is sound in the main. It has three kinds of problem:

1. **Half of the corpus has no sentence translations** (PC 37 to the end).
2. **A few systematic errors account for most wrong rows**: `karaṇīyā` in all 75 Sekhiyas, object `cīvaraṃ` tagged nominative, `dhammaṃ` mis-glossed in 14 Sekhiyas, a stray `, comp` tag on about 270 rows.
3. **A steady rate of one-off slips**: copy-paste lemmas, wrong gender/case/number, typos, duplicated or orphaned rows.

Locations are `stem:line`, where the stem is the file name without `sikkhāpadaṃ.md` (`rāja:306` is `rājasikkhāpadaṃ.md` line 306). Files without that ending keep their name (`nidānuddeso:58`, `pācittiyā:70`). Rule numbers are added where they help.

## Coverage

- **Read in full, once:** all 217 content files — 5,539 analysis rows, 515 Pāli sentences, 263 sentence translations. Eight reviewers each read one eighth of the corpus row by row.
- **Checked by script:** index against files, H1 against index label, previous/next links, table header, column count, raw HTML, the POS / case / compound-type vocabularies, and every word that is analysed in more than one way across files (113 words).
- **Checked against the local DPD database:** only the disputed items listed under "Raised but not errors" and a few roots.
- **Spot-checked against the source:** about 110 of the cited rows were printed from the files and match as quoted. The rest are reported as the reviewers quoted them.
- **Not done:** the Pāli headings were not compared with an edition (CST or Ñāṇatusita). Heading deviations are reported from memory of the standard text and are marked "check edition". The DPD was not consulted for every row.

## State of the corpus

| Check | Result |
|---|---|
| Files / index entries | 217 / 217, all linked, no orphans |
| H1 equals index label | all |
| previous / next links | all correct |
| Table header | identical 11 columns in all 515 tables |
| Column count per row | no deviation |
| Sentences with a translation row | 263 of 515 |

**Sekhiya numbering.** The index lists SE 1, 3, 5 … 23 and then 25–75. Each odd-numbered file up to SE 23 holds two rules (`gamissāmi` and `nisīdissāmi`), so SE 2, 4 … 24 exist only as the second `##` block of the preceding file. They have no index entry, no H1 and no file of their own. SE 25 and 26 have separate files.

## Format findings

### Structural (highest priority)

1. **125 files have no translation row at all:** PC 37–92 (56 files), the Pāṭidesanīya intro and PD 1–4, the Sekhiya intro and all Sekhiya files, and `adhikaraṇasamathā`. Everything up to PC 36 is translated.
2. **Sentences without a translation inside otherwise translated files:**
   - `nidānuddeso:26` (`suṇātu me āvuso saṅgho`) and `:44` (`ajj'uposatho cātuddaso`). Both tables also hold only one of the heading words.
   - `sañcaritta:24` (second sentence of SA 5).
   - `pācittiyā:25`, `:36`, `:45`, `:54`, `:63`, `:73` (the closing formula; 1 of 8 sentences translated).
   - `ūnapañcabandhana:63` (`ayaṃ tattha sāmīci`).
   - `dutiyapavāraṇā:22` (second sentence of PC 36).
   - Duplicate headings account for the missing row in `manussaviggaha`, `kuṭikāra` and `bhikkhunūpassaya` (item 5).
   - Placeholder headings account for it in `pārājikuddeso`, `saṅghādisesuddeso`, `aniyatuddeso` and `nissaggiyapācittiyā` (item 4).
3. **A whole row is `#REF!`:** `vihārakāra:27` (`vatthu`). It should match `kuṭikāra:54`.
4. **Placeholder headings that are not Pāli:** `## PA 1 ... 4` (`pārājikuddeso:17`), `## SA 1 ... 12 ` (`saṅghādisesuddeso:22`; there are 13 rules), `## AN 1 ... 2` (`aniyatuddeso:17`), `## PD 1 ... 4` (`pāṭidesanīyā:18`), and the equivalents in `nissaggiyapācittiyā`, `pācittiyā` and `sekhiyā`.
5. **Duplicated headings and split tables:**
   - `manussaviggaha:39` and `:59`: same sentence twice (`matan'te` / `matante`); the table is under the first, the translation under the second.
   - `kuṭikāra:44` and `:60`: same sentence twice; the row `- desanāya` (`:64`) is cut off from its compound `vatthudesanāya` (`:50`).
   - `bhikkhunūpassaya:19`: heading repeated inside the rule; `- upassayaṃ` (`:23`) is cut off from its compound (`:10`).
   - `antepura:28`: heading repeated; the members `aniggata` and `ratana *` (`:18–19`) sit in the first table, their parent `aniggataratanake` at `:33`.
   - `ṭhitouccāra:17–21` (SE 73): a stray copy of the SE 74 heading with one row, `passāvaṃ`. That row is missing from the SE 73 table (`:8–13`), which has `uccāraṃ, vā, vā`.
   - `adhikaraṇasamathā:60–64`: the second half of the list is given a heading but only one row (`tassapāpiyyasikā`). At `:53–54` the members `- tassa`, `- pāpiyyasikā` have no parent row and nest under `yebhuyyasikā`.
6. **Duplicated row blocks with no heading:** `kuladūsaka:58–63` repeats `:52–57`; `:91–109` repeats `:69–89` (no translation); `:127–134` repeats `:115–126`.
7. **Rows that belong elsewhere:**
   - `ariṭṭha:110`: `no` ends the table of `yāvatatiyañce … kusalaṃ`; it belongs to `no ce paṭinissajeyya` (`:112`), whose table starts at `ce`.
   - `ariṭṭha:85` and the parallel row in `kaṇṭaka`: `pana` after `evañca` is not in the heading.
   - `dutiyāniyata:7–11`: `na h'eva` is analysed twice (`na` + `heva`, then `naheva`). (?)
   - `pāṭidesanīyā:7–8`: `pāṭidesanīyā`, `dhammā` appear before `ime` and again at `:13–14`.
   - `dutiyapāṭidesanīya:32`: an extra `detha` row after `dethāti`, without prefix or `iti` row.
   - `jivhānicchāraka:7`: a one-cell row `SE 49` before the first word.
   - `sannidhikāraka:10–11`: one heading word, two rows (`sannidhikārakaṃ` adverb and `sannidhikārakaṃ 2` adjective); `dutiyapāṭidesanīya:66–67` likewise for `nappaṭibhāseyya`. (?)
8. **Raw `<br>` in 14 files, 25 occurrences.** The project's clean-Markdown rule forbids it.
   - Ending a translation row: `paṭhamaupakkhaṭa:20`, `bhūtārocana:15`, `nikkaḍḍhana:20`, `mahallakavihāra:33`, `saṃvidhāna:28`, `paripācita:22`, `gaṇabhojana:13`, `paṭhamapavāraṇā:22`.
   - Joining two alternative translations: `adinnādāna:20`, `bhedānuvattaka:87`.
   - Inside analysis cells: `nidānuddeso:58`, `adinnādāna:32`, `uttarimanussadhamma:11`, `bhūtārocana:11`, `rāja:293`, `rāja:340`, `kaṇṭaka:140`, `:143`.
   - Inside the Pāli word itself: `mahallakavihāra:16` (`aggaḷaṭṭhapanāya<br>`, also in its lemma).

### Content in the wrong column

- **POS column holds a gender** (18 rows; should be `noun`): `masc` for `patta` (`patta:10`, `ūnapañcabandhana:14`, `:17`, `:30`, `:55`, `apanidhāna:11`, `ujjhānasaññī:12`) and `dūta` (`rāja:20`, `:45`, `:78`, `:111`, `:157`, `:303`), and `nidānuddeso:186`; `fem` for `bhisiṃ` (`paṭhamasenāsana:15`) and `ujjagghikāya` (`ujjagghika:8`, `:19`); `nt` for `kocchaṃ` (`paṭhamasenāsana:17`).
- **Grammar cell holds a gloss:** `eḷakaloma:42` (`hārake | noun | in not being`); copy `:28`.
- **Compound-type cell holds other content:** `fem acc sg of seyyā` on `seyyaṃ` (`dutiyasenāsana:12`, `anupakhajja:18`, `ukkhittasambhoga:28`, `kaṇṭaka:167`; `seyyā` is not a compound); `kāraya + māna` on `vihārakāra:11`; `sugatassa + vidatthi` on `nisīdanasanthata:35`.
- **Case column `+loc` on a word that governs nothing:** `hassadhamma:8`.
- **POS contradicts the grammar cell:** `mohana:98` (`dulladdhaṃ | ind | nt nom sg`), `manussaviggaha:51` (`matante | ind | sandhi`; other sandhi rows are `comp`), `tatuttari:29` (`(or) noun`).
- **Placeholders left in:** `?` as the meaning of `desitaṃ` (`kaṇṭaka:18`); `ta + ?` as the construction of `tāva` (`dutiyapāṭidesanīya:49`, `:77`); `“”` as the meaning of `iti` (about 10 rows, e.g. `nidānuddeso:140`).
- **Homonym numbers left in the Pāli cell:** `tato 2`, `tato 3`, `te 3`, `ahaṃ 2`, `bhikkhu 2`, `patta 2`, `āyasmanto 2`, `theyyasaṅkhātaṃ 2`, `saṅghādisesā 2`, `dhammaṃ 3`, `aññataraṃ 2` (84 rows). They look like DPD headword numbers. Also `ratana *` (`antepura:19`) and `-dasa` without the space (`nidānuddeso:50`).

### Label vocabulary

- **Spurious `, comp` in the grammar cell of words that are not compounds** (about 270 rows): `bhikkhu` 118 times (27 rows lack it), `karaṇīyā` 50, `sikkhā` 49, `bhikkhunā` 13, `dhammā` 8, `nissaggiyaṃ` 4, `bhikkhūhi` 3, and in `adhikaraṇasamathā:100–102` on `pucchāmi`, `kaccittha`, `parisuddhā` in the third repetition only.
- **Absolutive is labelled five ways:** POS `abs` (18 rows), POS `ger` (4), POS `verb` with `ger of` / `abs of` (65), POS `ind` with `adv, ger of` (9), and `āhacca` as `ptp`. `uddissa` alone is `verb | ger` six times and `ind | adv, ger` once (`rāja:262`).
- **Compound types:** `sattamī tappurisa` (21) against `locative tappurisa` (11); `tatiyā tappurisa` (1) against `instrumental tappurisa` (19); `genetive` (2); `bahubīhi` (5) and `> bb` (2) against `bahubbīhi`; `mixed` (2); `verbal comp` / `comp verb`.
- **Ordinal against cardinal:** `dutiyo | card` (`sappāṇaka:31`, `kayavikkaya:26`, `ujjagghika:34`) where the other vagga rows have `ordin`; `chappañca`, `cha`, `pañca` tagged `ordin` (`dhammadesanā:13–15`).
- **`dhāretabbaṃ | verb`** (`chabbassa:15`) against `ptp` at `kaṭhina:20`.
- **Grammar-cell typos:** `mac` (`oguṇṭhita:8`, `:19`, `pattasaññīpaṭiggahaṇa:9`, `ujjhānasaññī:10`, `uccasadda:7`, `:19`), `msac` (`nahāna:42`), `isntr` (`dutiyaupakkhaṭa:31`, `:66`, `mañcapīṭha:22`, `sakabaḷa:8`), `sadnhi` (`dutiyāniyata:21`, `ariṭṭha:74`, `kaṇṭaka:76`), `1sg sg` (`sakabaḷa:11`), `3sg` (`ūnavīsativassa:16`), `fam` (`sañcaritta:33`), `pon` (`bhedānuvattaka:80`), `masc.nom.sg` (`paṭhamasenāsana:32`).
- **Incomplete grammar cells:**
  - `of` missing: `iminā … sg ima` (4 rows), `cīvaraṃ … sg cīvara` (2), `paṭinissaggāya … sg paṭinissagga` (5).
  - `sg` missing: `adhikaraṇaṃ | nt nom of` (4), `saṃvāsaṃ`, `vaṇṇaṃ`, `bhagini`, `upāsako`, `kammasamayo`, `loc of bhojana` (3).
  - Gender missing: `punakammāya` (`ukkoṭana:17`), `ahaṃ 2` (`saṅghādisesuddeso:66`).
  - Gender, case and number all missing: `niṭṭhitā | pp of niṭṭhāti` in 5 of 6 closing lines (`pārājikuddeso:114`, `saṅghādisesuddeso:175`, `aniyatuddeso:70`, `pācittiyā:80`, `pāṭidesanīyā:79`, `sekhiyā:74`); only `nissaggiyapācittiyā:62` has them.

### Convention drift

- **Sandhi rows:** many have member sub-rows, many do not. Missing in SE 23–26 and 32–34 (`gamissāmīti`), in SA 9, 11, 12, 13 (several each), in `tamenaṃ` (`dutiyāniyata:56`), and in all sandhi rows of `aniyatuddeso`, `adhikaraṇasamathā`, `pāṭidesanīyā` and `sekhiyā`. Some sandhi rows have a meaning and some an empty cell (`parisuddhāti`, `seyyoti`, `passāmīti`, `gimhānanti`).
- **Indent depth of members:** `kaṇṭaka:8` (`- samaṇuddeso` under `samaṇuddesopi` should be one level deeper, as under `hassāpekkhopi`, `apanidhāna:30`); `kaṇṭaka:138–142` (`cara`, `pire` lack the `- ` prefix).
- **Compounds with member rows but empty type / construction cells:** `samaṇuddesa` (9 rows in `kaṇṭaka`), `saññācikāya` (`kuṭikāra:7`, `:75`), SE 44–54 (`piṇḍukkhepakaṃ` … `oṭṭhanillehakaṃ`), `sabbahatthaṃ`, `sakabaḷena`, `ujjhānasaññī`, `sasitthakaṃ`, `uppannuppannānaṃ`, `nānappakārakaṃ` (2), `dirattatirattaṃ`, `sahaseyyaṃ`, `aḍḍhateyyā`, `diyaḍḍhaṃ`, `anvaḍḍhamāsaṃ`.
- **Compounds without member rows where parallel compounds have them:** `gilānasamayo`, `addhānagamanasamayo` (`nahāna:49`, `:53`), the samaya compounds of PC 33 and 46.
- **`desessāmīti`** (SE 57–72): the parent construction reads `desissāmi + iti` in every file; member rows only in SE 57.
- **Quotes and elision:** PC files use `’ti`, SE files `'ti`; within SE, five headings write `-īti` without the apostrophe (`pattasaññībhuñjana:3`, `samasūpaka:3`, `sūpodanaviññatti:3`, `ṭhita:3`, `udakeuccāra:3`). `tatth'āyaṃ` / `tatthāyaṃ`, `matan'te` / `matante`, `taṃ'khaṇikāya'pi`, `ekassa'pi`.
- **Heading punctuation:** final full stop missing (`mahallakavihāra:3`, `okkhittacakkhu:3`, `adhikaraṇasamathā:3`, `aniyatuddeso:15`); trailing space or comma (`kaṇḍupaṭicchādi:3`, `ratana:3`, `nanda:3`, `pāṭidesanīyā:44`); no comma before `pācittiyaṃ` in `gaṇabhojana:3`, `paramparabhojana:3`.
- **Titles:** `dutiyasahaseyyasikkhāpada` and `dutiyāniyatasikkhāpada` lack the final `ṃ` (file name, H1, index); `methunadhamma sikkhāpadaṃ` has a space; `dutiyāniyata` against `paṭhamaaniyata`.
- **Root glosses:** `√har (live)` (`vihārakāra:10`, `saṅghabheda:73`, `kuladūsaka:15`, `sāsaṅka:36`) against `√har (carry)`; `√dus (be angry, corrupt)` against `√dus (hate, dislike)`.

### The same word analysed two ways

- `paṭinissajeyya`: `√saj … saja` (7 rows) against `√sajj … sajja` (`saṅghabheda:123`); `paṭinissaggāya` and `appaṭinissaṭṭha` use `√sajj`.
- `bhagavant`: `√bhaj > bhag + avant` (`ariṭṭha:15`) against `√bhaj + a + vant` (`ariṭṭha:50` and after).
- Optative constructions end in `+ ti` or `+ eyya`: `kareyya` `karo + ti` (`nidānuddeso:64`) against `karo + eyya` (`:120`); `uddiseyya`, `ādiyeyya`, `abbheyya`, `hareyya`, `kappeyya` have `+ ti`. Likewise `bhavissati` `bhava + ti` (2) against `bhava + issa + ti`; `nisīditvā` `ni + sīda + ti` (`chamā:9`, `nīcāsana:10`); `vadetu` `vade + ti` (`dubbaca:100`).
- `musāvādo`: `kammadhāraya` (`nidānuddeso:188`) against `abyayībhāva` (`:201`); `sampajānamusāvādo` split in two parts (`:186`) and three (`:199`).
- `tattha`: `ta + ttha` (17) against `ta + tha` (2). `tāva`: `ta + ?` against empty.
- `eso`: `of esa` (2) against `of eta` (`rāja:142`). `ayaṃ`: `masc/fem nom sg` (15) against `masc nom sg` (2).
- `hi`: `excl` (7) against `emph` (2). `evaṃ`: `ind, adv` (20) against `adv` (9). `yāva`: `adv, prep` against `prep`. `iti`: empty (62) against `adv` (3).
- `sugatavidatthi`, `sugataṅgula`: `kammadhāraya` with `sugata` glossed "standard; commonly accepted" (`kuṭikāra:35–36`, `mañcapīṭha:20–21`, `nisīdana:23`, `kaṇḍupaṭicchādi:25`, `vassikasāṭikā:25`, `nanda:32`) against `sugatacīvara` `genitive tappurisa`, "Well Gone One" (`nanda:11–12`). The genitive reading is the correct one.
- `kattikapuṇṇamaṃ`: `kammadhāraya` (`sāsaṅka:10`) against `genitive tappurisa` (`accekacīvara:11`).
- `sakkacca` as `ger of sakkaroti` (`ālopa:18`) against `sakkaccaṃ` as an adverbial accusative.
- `capucapu` `ind, onom` against `surusuru` `noun masc, onom`; final members `kārakaṃ` as `adj` (SE 46, 50, 51) against `ind adv` (SE 45, 47 etc.).
- Gender of `eḷakaloma`: nt (`eḷakaloma:13`) against masc (`suddhakāḷaka:13`, `dvebhāga:15`, `:33`); `suddhakāḷakānaṃ` nt against masc. Gender of `patodaka`, `vivaṇṇaka`, `mohanaka` differs between compound and member or between PC 52, 72 and 73.
- `uposatha` meaning_lit: "living with" (`nidānuddeso:63`) against "living near" (`:38`).
- `rāja`: `√rāj + ā` (`rāja:13`, `nanda:50`) against `√rāj + a` (`antepura:17`).

## Grammatical findings

### Systematic errors

1. **`karaṇīyā` in `sikkhā karaṇīyā` — all 75 Sekhiya sentences.** Tagged `noun | nt abl sg of karaṇīya`, gloss "duty; obligation; business". It is the future passive participle, fem nom sg, agreeing with `sikkhā`: "(the training) is to be done". The row was copied from DPD `karaṇīya 1` (the noun); the right headword is `karaṇīya 2` (ptp). The ablative noun fits only `vikālagāmappavesana:21` (PC 85).
2. **`cīvaraṃ` tagged `nt nom sg` where it is the object** (accusative): `paṭhamaupakkhaṭa:28`, `:72`, `rāja:31` (`cīvaraṃ cetāpetvā`), `cīvaradāna:12`, `cīvarasibbana:12`, `dubbaṇṇakaraṇa:41`, `vikappana:21`, `apanidhāna:13`, `nanda:15`. `dutiyaupakkhaṭa:72` has it right.
3. **`adhikaraṇaṃ` tagged nominative where it is the object** of `samādāya paggayha`: `saṅghabheda:18`, `:49`.
4. **`atikkāmayato | prp | masc dat sg of atikkāmanta`** (7 rows: `kaṭhina:22`, `patta:13`, `bhesajja:43`, `mañcapīṭha:32`, `nisīdana:36`, `kaṇḍupaṭicchādi:35`, `vassikasāṭikā:36`). The base cell gives the causative `kāmaya`, so the lemma is `atikkāmayanta`; the gloss "for (one) going beyond" drops the causative ("letting it pass").
5. **`ubbhata` derived from `√dhar (hold)`, `ud + √dhar + ta`** (`kaṭhina:11`, `udosita:9`, `akālacīvara:9`). DPD: `√bhar`, `ud + √bhar + ta`.
6. **`anaññaṃ | pron | masc acc sg of anaññā`** (`anupakhajja:32`, `uyyojana:66`, `sañcicca 2:32`, `upassuti:37`). Lemma `anañña`; it is an adjective qualifying `paccayaṃ`.
7. **Compounds typed `kammadhāraya` where they are bahubbīhi** (other rows use `kammadhāraya > bahubbīhi`): `saddheyyavacasā` (`paṭhamaaniyata:31`, `:74`, `dutiyāniyata:57`, `:94`), `chattapāṇi`, `daṇḍapāṇi`, `satthapāṇi`, `āvudhapāṇi` (line 8 of SE 57–60), `veṭhitasīsassa` (`veṭhita:8`), `oguṇṭhitasīsassa` (`oguṇṭhita 2:8`), `kalyāṇadhammaṃ` (`attakāmapāricariya:44`).
8. **Lemma is the inflected form or another word** (copy-paste):

| Location | Row says | Should be |
|---|---|---|
| `kayavikkaya:23` | `eḷakalomavaggo … of kosiyavagga` | eḷakalomavagga |
| `udakeuccāra:24` | `pādukavaggo … of surusuruvagga` | pādukavagga |
| `ariṭṭha:17`, `kaṇṭaka:18` | `desitaṃ … masc acc sg of dhamma` | of desita |
| `antepura:14` | `abhisittassa … of avasitta` | abhisitta |
| `anupakhajja:21` | `sambādho … of sambhāda`, `saṃ + √bhād + a` | sambādha, `√bādh` |
| `duṭṭhullārocana:11`, `duṭṭhulla:12` | `of duṭṭhalla` | duṭṭhulla |
| `duṭṭhulla:14` | `of paṭichādeti` | paṭicchādeti |
| `mohana:115` | `mohanake … of mahanka` | mohanaka |
| `talasattika:13` | `talasattikaṃ … of sattika` | talasattika |
| `sahadhammika:44` | `of aññtabba` | aññātabba |
| `nisīdana:7` | `of nidsīdana` | nisīdana |
| `atthaṅgata:12` | `of atthaṇgata` | atthaṅgata |
| `nidānuddeso:166`, `:178` | `of anusāvita`, `anusāviyamāna` | anussāvita, anussāviyamāna |
| `adhikaraṇasamathā:34` | `sammukhā … of samukhā`, `sa + mukha` | sammukhā, `saṃ + mukha` |
| `adhikaraṇasamathā:37` | `of sativinayo` | sativinaya |
| `veṭhita:10`, `oguṇṭhita 2:10` | `sīsassa … of sīssa` | sīsa |
| `padasodhamma:10`, `paṭhamasahaseyya:10` | `of anupasampannaṃ` | anupasampanna |
| `kāyappacālaka:10`, `bāhuppacālaka:10`, `sīsappacālaka:10` | `of pacālakaṃ` | pacālaka |
| `adinnādāna:32` | `rājāno … of rāja`, `√rāj + a + āno` | rājan |
| `uttarimanussadhamma:70` | `vilapiṃ … of vilapi` | vilapati |
| `ariṭṭha:51`, `kaṇṭaka:52` | `abbhācikkhi … of abbhācikkhi` | abbhācikkhati |
| `paṭhamapāṭidesanīya:36`, `tatiya…:45`, `catuttha…:57` | `āpajjiṃ … of āpajji` | āpajjati (as `dutiya…:93`) |
| `dutiyapāṭidesanīya:98` | `paṭidesema … of paṭidesati` | paṭideseti |
| `mahāpesakāra:87`, `:100` | `of anupadajjeyya` | anupadajjati |
| `kaṇṭaka:139` | `cara … of caratu` | carati |
| `uyyojana:36` | `gaccha … of gacchatu` | gacchati |
| `dutiyapāṭidesanīya:28`, `:48`, `:76` | `detha`, `apasakka … of detu`, `apasakkatu` | deti, apasakkati |
| `dubbaca:121` | `yad … of ima` | of ya |
| `uttarimanussadhamma:59` | `ajānaṃ … from ājānāti` | from na jānāti |
| `sāsaṅka:7` | `from upavassati` | upavasati |
| `sāsaṅka:62` | lemma `vippāvāsa` | vippavāsa |
| `dutiyāniyata:39`, `adinnādāna:66` | `tathārupa` | tathārūpa |
| `adinnādāna:18` | `sankhāyati` | saṅkhāyati |
| `dubbaca:130` | `vuṭṭḥāpana` | vuṭṭhāpana |
| `udosita:12` | `akeratta` | ekaratta |
| `rāja:64`, `kāṇamātu:34` | `patiggaṇhāti`, `patigaṇheyya` | paṭiggaṇhāti, paṭiggaṇheyya |
| `kāṇamātu:24` | `paṭigahetabba` | paṭiggahetabba |
| `eḷakaloma:9` | `addhānamaggapgaṭipanna` | addhānamaggapaṭipanna |
| PC 35–43, PD 1, 3, 4 | `of khādaniya` | khādanīya |
| `ariṭṭha:23` and parallels | `anatra + aya + ika`, "in-betweeen" | antara, "in-between" |
| `ariṭṭha:18`, `kaṇṭaka:19`, `mohana:20` | base `√ña + a > jānā` | `√ñā + nā` |
| `paripācita:11` | `bhikkhuni + paripācita` | bhikkhunī |

### Wrong gender, case, number or person

| Location | Row says | Should be |
|---|---|---|
| `upassuti:32` | `sossāmi | fut 3rd pl` | fut 1st sg |
| `anāhaṭa:11` | `vivarissāmīti | sandhi, pr + ind` | fut + ind |
| `bhedānuvattaka:125` | `ruccittha | aor 2nd pl of rucci`, base `(pass)` | aor 3rd sg (middle) of ruccati; subject is `saṅghabhedo` |
| `bhedānuvattaka:98` | `assu | pron | opt 3rd pl of assa` | POS verb, of atthi |
| `nisīdanasanthata:20` | `ādātabbā | fem nom pl` | fem nom sg (subject `sugatavidatthi`) |
| `vilekhana:22` | `uddiṭṭhehi | nt instr sg` | instr pl |
| `dubbaṇṇakaraṇa:16` | `- karaṇānaṃ | nt gen sg` | gen pl (the parent row has pl) |
| `ukkhittasambhoga:20` | `appaṭinissaṭṭhena | masc nom sg` | masc instr sg |
| `paṭhamaaniyata:29` | `- taṃ | fem acc sg` (in `tamenaṃ`) | masc acc sg (the monk) |
| `akālacīvara:47` | `taṃ | masc nom sg` | nt nom sg (with `cīvaraṃ`) |
| `vihārakāra:13` | `attuddesaṃ | fem acc sg` | masc acc sg (with `vihāraṃ`) |
| `kuladūsaka:118`, `:128` | `imamhā | nt abl sg` | masc abl sg (with `āvāsā`) |
| `sahadhammika:27` | `aññaṃ | nt acc sg` | masc acc sg (with `bhikkhuṃ`) |
| `mohana:48` | `iminā | nt instr sg` | masc instr sg (with `bhikkhunā`) |
| `mohana:45` | `nisinnapubbaṃ | noun | nt nom sg` | adj, masc acc sg (with `bhikkhuṃ`) |
| `kāṇamātu:9–10` | `kulaṃ | nt nom sg`, `upagataṃ | pp | nt nom sg` | `kulaṃ` acc; `upagataṃ` masc acc sg (with `bhikkhuṃ`) |
| `dantapona:10` | `adinnaṃ | noun | nt acc sg` | adj, masc acc sg (with `āhāraṃ`) |
| `mahallakavihāra:27` | `pariyāyaṃ | nt nom sg` | masc acc sg |
| `nanda:28`, `:43` | `sugatacīvarappamāṇaṃ | nt acc sg` | nt nom sg (predicate of `idaṃ`) |
| `suddhakāḷaka:14` | `- eḷaka | noun | nt` | masc |
| `paṭhamaaniyata:14` | `raho | adv, masc nom sg of rahas` | `rahas` is nt; indeclinable |
| `okkhittacakkhu:9` | `- cakkhu | adj | masc nom sg | with eyes` | noun nt, "eye" |
| `upassuti:17` | `vivādāpannānaṃ | noun` | adj (with `bhikkhūnaṃ`) |
| `nidānuddeso:166` | `anussāvitaṃ | noun` | pp (predicate of `hoti`) |
| `sūpodanaviññatti:13`, `pariṇata:14` | `attano | masc dat sg` with `atthāya (+gen)` | gen sg (as `paṇītabhojana:37`) |
| `bhedānuvattaka:59`, `:81` | `amhākaṃ | masc gen/dat pl` | `1st gen/dat pl` (no gender; so `dubbaca:36`) |
| `mahāpesakāra:85` | `- mattaṃ | masc` inside nt `kiñcimattaṃ` | nt |
| `nisīdanasanthata:9` | member `santhataṃ | nom sg` in an acc compound | acc, or stem |
| `kuṭikāra:54` | `vatthuṃ | nt nom sg` | the `-uṃ` form is acc; see Pāli text |
| `dutiyaupakkhaṭa:16`, `:18`, `:20`, `:21` | `paccekacīvaracetāpanā`, `upakkhaṭā | nt nom pl` | nt pl would be `-āni`; see Pāli text |

### Wrong governed case

- `yāva | +dat`: `accekacīvara:36` (governs acc `cīvarakālasamayaṃ`), `sahadhammika:25`, `dutiyapāṭidesanīya:51`, `:79` (conjunction, governs nothing).
- `nāvābhirūhana:24`: `aññatra` has no case although it governs `tiriyaṃtaraṇāya`; other `aññatra` rows have `+abl`.
- `ādiyeyya` lacks `+acc` at `adinnādāna:19`; `:71` has it.

### Wrong sandhi or compound analysis

- `uttarimanussadhamma:58`, `:60`: `ajānamevāhaṃ` = `ajānaṃ + evaṃ`, member `evaṃ | thus`. It is `ajānaṃ + eva + ahaṃ` (emphatic `eva`). The gloss "not knowing thus" and the translation at `:72` inherit the error.
- `akālacīvara:27`: `khippameva | sandhi, pr + ind` → ind + ind. `rāja:100`: `kappiyanti | sandhi, pr + ind` → adj + ind.
- `mahānāma:9`: top-level split `cātumāsapaccayassa + pavāraṇā` contradicts its own member rows (`cātumāsa + paccayapavāraṇā`).
- `vehāsakuṭi:13–15`: `upari`, `vehāsa`, `kuṭiyā` are listed flat; the structure is (`upari` + `vehāsa`) + `kuṭi`.
- `āmisa:12`: `āmisahetu | abyayībhāva`. The first member is a noun, so it is a tappurisa used adverbially.
- `ukkoṭana:14`: `nihatādhikaraṇaṃ | accusative tappurisa | nihata + adhikaraṇaṃ`. A pp + noun is a kammadhāraya; the construction should not be inflected.
- `uyyodhika:18`: `senābyūhaṃ | dative tappurisa | senāya + byūha` → genitive.
- `bāhuppacālaka:8`, `:21`: `accusative tappurisa | bāhavo + pacālaka`. `bāhavo` is nominative plural; the parallel rows have `kāyaṃ`, `sīsaṃ`.
- `paripācita:18`: `gihīsamārambhā | genitive tappurisa | gihinā + samārambha`. `gihinā` is instrumental; type and construction disagree. The row also spells `gihī-` against the heading's `gihi-`.
- `kuladūsaka:170`, `:215`: `bhaya + gāmino` in the construction; the parallel rows use the stem `gāmī`.
- `paṇītabhojana:32–35`: `evarūpāni` has the member `evaṃ` against the construction `eva + rūpa`, and `rūpāni | nom pl` inside an acc pl compound.
- `kāyasaṃsagga:29`, `:33`: `gāhaṃ | adj` inside the noun compound `hatthagāhaṃ`.
- `nidānuddeso:58`, `:60`: `pattakallaṃ` is `nt nom sg` but its member `kallaṃ` is `masc acc sg of kāla`.
- `adhikaraṇasamathā:54`, `:64`: `pāpiyyasikā` built as `pāpa + iya + [s] + ikā` and as `tassa + pāpiya > pāpiyya + [s] + ikā`.
- `paramparabhojana:7–8`: construction `paramparā + bhojana` against the member row `parampara`.

## Word-gloss findings

### Wrong sense for the context

- **`dhammaṃ` glossed "act, practice, behaviour" in `dhammaṃ desessāmi`** — 14 files (SE 59–72). It is "teaching, Dhamma", as `chattapāṇi:12` and `daṇḍapāṇi:12` have it.
- **`evametaṃ` glossed "therefore this"** in every closing formula (`nidānuddeso:303`, `pārājikuddeso:103`, `saṅghādisesuddeso:165`, `aniyatuddeso:60`, `nissaggiyapācittiyā:50`, `pācittiyā:70`, `pāṭidesanīyā:69`, `sekhiyā:65`, `adhikaraṇasamathā:111`). `evaṃ` is "thus" (the literal column says so); `tasmā` already gives "therefore".
- **`bhikkhūhi` glossed "with monks" where it is the agent** ("by monks"): `ariṭṭha:42`, `:88`, `:94`, `kaṇṭaka:37`, `:90`, `:101`, `sahadhammika:10`, `dutiyapāṭidesanīya:39`, `:89`.
- `saṅghādisesuddeso:95`: `ciṇṇamānatto` "who has completed probation". Mānatta is not probation (parivāsa); the same file has "deference" (`:87`) and "penance" (`:97`).
- `udosita:14`, `saṅghādisesuddeso:84`: `rattaṃ` meaning "day(s)" with literal "night"; `udosita:11` "for one day only" for `ekarattampi`.
- `saṅghabheda:70`: `uddeso` in `ekuddeso` glossed "designated, appearing to be". It is "recitation" (as `dubbaca:16`).
- `gaṇabhojana:47–48`: `samaṇabhattasamayo` "time of food being offered by an ascetic". The meal is given to ascetics.
- `mahallakavihāra:13`: `dvārakosā` "as the door frame". With `yāva` it is "up to the door frame".
- `mañcapīṭha:21` and parallels: `sugata` "standard; commonly accepted" (see "The same word analysed two ways").
- `kaṇḍupaṭicchādi:12`, `:14`, `vassikasāṭikā:12`, `:14`: `kārayamānena` "building", `kāretabbā` "should be built" for cloths; "making / made" elsewhere.
- `ukkhittasambhoga:29`, `kaṇṭaka:168`: `kappeyya` "should take, use" with `seyyaṃ`. `seyyaṃ kappeti` is "lie down".
- `ukkhittasambhoga:13`: `- vādinā` "with a view". It is "(one) who asserts".
- `dubbaṇṇakaraṇa:33`: `anādā` "not adding, not having included" → "not having taken".
- `ujjhānasaññī:14`: `olokessāmi` "I will look down" → "look at".
- `vikālagāmappavesana:17`: `tathārūpā` "suitable, appropriate" → "of such a kind" (as `tatiyapāṭidesanīya:18`).
- `attakāmapāricariya:53`: `paricareyya` "she should serve, administer" → "serve, attend on".
- `cāritta:22`, `kammappaṭibāhana:18`, `dubbala:16`: `āpajjeyya` "would cause".
- `uyyojana:30`, `:32`: `dāpetvā` "having got", `adāpetvā` "having not got". Causative: "having had (it) given".
- `dubbaca:83`: `akāsi` glossed "(venerable) make!"; `kuladūsaka:199`, `ariṭṭha:48`, `kaṇṭaka:44`: `avaca` "one says | one said". Both stand with `mā` and are prohibitive.
- `dutiyāniyata:101`: `ayampi` "he too" → "this too". `bhedānuvattaka:119`: `āyasmantānampi` "and for the venerables" → "for the venerables too".
- `mahāpesakāra:82`: `āyasmantānaṃ` "for the the good men". `:87`: `anupadajjeyyāma` "I could give" (1st pl). `:65`: `suvilekhitaṃ` "well combed" against the translation's "well scraped".
- `adinnādāna:51`: `bālo` "fool, idiot, moron" against the translation's "immature".
- `nisīdanasanthata:12`: `kārayamānena` "having made" (a present participle).
- `eḷakaloma:14`: `uppajjeyyuṃ` "it could arise" (plural).

### Gloss does not match the case, or is broken

- Genitive glossed as instrumental: `cīvarapaṭiggahaṇa:10–11` (`aññātikāya` "by unrelated", `bhikkhuniyā` "by a nun" in `hatthato`).
- Locative glossed as genitive: `paṭhamaupakkhaṭa:51`, `dutiyaupakkhaṭa:53` (`cīvare` "of robe"), `sāsaṅka:33` (`rūpesu` "of type").
- Instrumental glossed as ablative: `rāja:217` (`cīvarena` "from a robe" in `attho me cīvarena`).
- Accusative with no object marking: `tatthāyasmante` "in that case the venerables" (`pāṭidesanīyā:39`, `sekhiyā:35`, `adhikaraṇasamathā:81`).
- Case marker stuck in front of an adjective gloss: "in belonging to the community" (`dutiyasenāsana:10`, `anupakhajja:10`, `vehāsakuṭi:10`), "in of kind; in of type" (`nidānuddeso:161`), "with related to sexual intercourse", "with connected with" (`duṭṭhullavācā:27`, `:29`), "in related to moment" (`sañcaritta:35`), "on covered, concealed" (`rahopaṭicchanna:13`), "to seated (a person), sitting" (`chamā:11`, `nīcāsana:13`, `pallatthika 2:9`, `ṭhita:9`).
- Truncated: `sāmisena` "with a dirty" (`sāmisa:8`), `gatassa` "to (a person) on" (`yāna:10`, `sayana:10`).
- Mixed forms: `nikkaḍḍhana:15` "he would drag out, expels, remove".
- Adjective glossed as a clause: `agilāno` "is not ill" (`tatiyapāṭidesanīya:23`, `catutthapāṭidesanīya:41`).
- Number: `ariṭṭha:24` `dhammā` "act; practice" (plural at `:62`).
- Typos: "doint" (`paṭhamaaniyata:17`, `dutiyāniyata:17`), "ts" (`dutiyāniyata:21`, `kaṇṭaka:76`), "procede" (`saṅghabheda:16`, `bhedānuvattaka:15`, `kuladūsaka:184`, `:188`, `acelaka:12`, `:14`), "offical" (`rāja:12`), "who's" (`aññātakaviññatti:35`), "standart" (`nisīdanasanthata:17`), "inititative" (`paripācita:18`), "an sunshade" (`chattapāṇi:8`), "to be lead" (`kuṭikāra:49`, `vihārakāra:15`), "Patimokkha" (`saṅghabheda:68`, `:141`), stray `"` (`adinnādāna:56`, `dubbaca:128`).

## Sentence-translation findings

Only PA to PC 36 could be reviewed; the rest has no translations.

### Mistranslations and omissions

- **`rāja:306`** — `no ce abhinipphādeyya` is translated "If he would succeed in obtaining". The negation is dropped: "If he should not succeed".
- `rāja:327`, `:347`, `dutiyaupakkhaṭa:82` — `āyasmanto`, `vo`, `yuñjantu` are plural; the translations have "Sir", "Let the sir get back what is his". `pahiṇittha` is "sent", not "conveyed".
- `uttarimanussadhamma:72` — "Not knowing thus, friend(s), I spoke" follows the wrong `evaṃ` analysis; "Not knowing, I said 'I know'".
- `bhedānuvattaka:146` — "Let the community be agreeable for the venerables". With `saṅghena` the venerables are to agree with the community; `saṅghabheda:75` has it right. The rows differ too (`+dat` against `+instr`).
- `bhedānuvattaka:87` — `api` in `amhākampetaṃ` is untranslated; two alternative translations are joined by `<br>(or)<br>`.
- `kuladūsaka:22` — "depending on a certain village or town who is a corrupter of families": the relative clause attaches to the town instead of the monk.
- `kāṇamātu:25` — "should an approached family invite … a monk". `upagataṃ` qualifies `bhikkhuṃ`: "a monk who has come to a family". "Biscuits" for `manthehi` and "take away" for `abhihaṭṭhuṃ` are doubtful.
- `mahallakavihāra:33`, `:48` — "standing on a few crops" for `appaharite ṭhitena` (the sense is "standing where there is little vegetation"). Also "upto", and "can be arranged" for a ptp.
- `dutiyapavāraṇā:20` — `abhihaṭṭhuṃ` is untranslated; the instrumentals "with non-staple or staple food" become "to chew or eat", which belongs to the next sentence; ends with a full stop although the clause continues.
- `cīvaraacchindana:25` — "given a robe to a monk, who is angry (and) displeased": the comma gives the anger to the recipient; `kupito anattamano` is the giver.
- `mahāpesakāra:111` — "and that monk, having said so, would give": "if" is missing. `:89` — "Perhaps I could also give" (1st pl).
- `nissaggiyapācittiyā:63` — omits "thirty" (`tiṃsa`); "forfeiture" here, "relinquishment" elsewhere.
- `bhesajja:26` — "butter" for `navanīta` (the row has "fresh butter").
- `nidānuddeso:168` — "there is an announcement" for `anussāvitaṃ hoti` ("has been announced"). `:228` — bare "fallen" for `āpannena`.
- `adinnādāna:41` — "king's men" for `rājāno`.
- `sappāṇaka:22` — "on grass or clay", while the table makes `tiṇaṃ` and `mattikaṃ` accusative objects.
- `saṃvidhāna:48` — `satthagamanīyo` detached into "which has to be gone with a company".

### Inconsistent renderings

- Pārājika: "defeat" (`pārājikuddeso:15`) against "disqualification / disqualified" (`:33`, `:115`, `manussaviggaha:95`).
- `dvebhāga:21` "muddy brown", "sheep-wool" against `:43` "ruddy brown", "sheep's hair" for identical Pāli.
- `vassikasāṭika:25` "robe-cloth for the rain's cloth" against `:47` "rain's bathing-cloth".
- `cetāpetvā`: "Having bought" (NP 8, NP 10) against "exchanged" (NP 9 and the row glosses).
- `nisīdanasanthata:24`, `:41`: "throughout" for `sāmantā` against the row gloss "all around".
- The final clause "…, is a saṅghādisesa (offence)" lacks its subject in SA 8–13 (`duṭṭhadosa:67`, `aññabhāgiya:76`, `saṅghabheda:125`, `bhedānuvattaka:182`, `dubbaca:168`, `kuladūsaka:252`); SA 6 and 7 have "it is".

### Typos and broken English

- `adinnādāna:60` "You are a immature!"; `!,”` with a stray comma (also `duṭṭhadosa:36`, `aññabhāgiya:39`). `:78` "something what has not been given". `:20` "given(and)".
- `saṅghādisesuddeso:176` "offences is finished"; `aniyatuddeso:71` "Two uncertain (cases) is finished"; `:89` "for six-night".
- `paṭhamaaniyata:46`, `:65`, `dutiyāniyata:68`, `:85` "dealt in accordance to"; `dutiyāniyata:104` "This is too an uncertain case."
- `dutiyaupakkhaṭa:23` "of an unrelated male householders … has been set up"; `:82` "for a such and such a robe".
- `aññabhāgiya:61` "is belonging to another class"; `:76` "which a mere pretext"; `kuladūsaka:190` "Because of this kind offence".
- `kāyasaṃsagga:42` "any of the limb"; `purāṇacīvara:23` stray comma, "beat used robe"; `atthaṅgata:19` "a authorised monk"; `anupakhajja:34` mismatched quotes; `vassikasāṭika:47` unreadable as it stands.
- `nissaggiyapācittiyā:52` "requiring confessing"; spaces before `?` and `,` in the `nidānuddeso`, `aniyatuddeso` and `nissaggiyapācittiyā` formulas.
- Lower-case start or no final stop: `pārājikuddeso:33`, `:115`, `sukkavisaṭṭhi:16`, `saṅghādisesuddeso:46`, `kāyasaṃsagga:42`, `dutiyāniyata:50`, `udosita:28`, `akālacīvara:70`, `purāṇacīvara:23`, `kāṇamātu:46`, `sappāṇaka:32`, `pariṇata:28`, `pathavīkhaṇana:26`.

## Pāli text

All of these need a check against the edition the class uses.

- `adhikaraṇasamathā:3`: the heading lacks `dhammā` (`… satta adhikaraṇasamathā dhammā uddesaṃ āgacchanti`); the table has the row (`:14`).
- `adhikaraṇasamathā:46` `paṭiññāya kāretabbo` against `:60` `kāretabbaṃ`.
- `kuṭikāra:44`, `:60`: `vatthuṃ desetabbaṃ`; `vihārakāra:21` has `vatthu desetabbaṃ`.
- `dutiyaupakkhaṭa:3`: `paccekacīvaracetāpanā upakkhaṭā honti`. CST reads `-cetāpannāni upakkhaṭāni`. If the masculine reading is intended, the rows should not say `nt nom pl`.
- `chabbassa:18`: `visajjetvā vā avisajjetvā vā` (the row lemma is `vissajjeti`). `ūnapañcabandhana:23`: `nissajitabbo` (the row lemma is `nissajjitabba`).
- `ūnapañcabandhana:31`, `:44`: `bhikkhūnam` with `m`.
- `bhikkhunūpassaya:3`, `:10`: `bhikkhun'ūpassayaṃ` with long `ū`; `:19` has `bhikkhun'upassayaṃ`. The file name and index also have `ū`.
- `pathavīkhaṇana:3`, `:10`: `paṭhaviṃ` against the lemma and title `pathavī`.
- `sañcaritta:24`, `:33`: `taṃ'khaṇikāya'pi` / `taṃkhaṇikāyapi` (standard `taṅkhaṇikāyapi`). `dutiyapāṭidesanīya:57`: `ekassa'pi`.
- `mohana:20`: the row is `ājānāmi`; the heading (`:3`) has `jānāmi`.

## Doubtful (worth a second look, not confirmed errors)

- **Compound types.** `…vaggo` compounds are all `kammadhāraya` ("chapter about X" suggests tappurisa). `antaraghare`, `tiracchānagatā`, `yānagatassa`, `sayanagatassa` are `kammadhāraya` while `pādukārūḷha` is `locative tappurisa`. `samasūpakaṃ`, `samatitthikaṃ`, `appaharite`, `āhaccapādaka`, `okkhittacakkhu`, `appasaddo`, `aṭṭhaṅgulapādakaṃ`, `ūnapañcabandhana`, `ūnavīsativassaṃ`, `akaṭānudhammena`, `sassāmikaṃ` are plain `kammadhāraya` with bahubbīhi glosses. `manussaviggaha`, `purisaviggaha`, `kaṇḍupaṭicchādiṃ`, `aññamañña` are `accusative tappurisa`. `uttarimanussadhamma` is `kammadhāraya` with an indeclinable first member. Numeral compounds are `dvanda` in `nidānuddeso:39`, `:48` and `digu` in `saṅghādisesuddeso:101`.
- **"dative tappurisa" with a genitive in the construction:** `attano + uddesa`, `vatthuno + desanā`, `vaggassa + vādaka`, `pattassa + dhovana`, `pānīyassa + thālaka`, `ālokāya + sandhi`.
- **`saṅghādisesa`**: typed `sattamī tappurisa` with a three-part construction `saṅgha + ādi + sesa`; POS is `adj` in four rows and `noun` in `amūlaka:12` for the same use.
- **`chedanakaṃ`, `bhedanakaṃ`, `uddālanakaṃ`** (PC 86–92): `ind, adv, acc sg`. DPD has `chedanaka` as an adjective; here it qualifies `pācittiyaṃ`.
- **`vinassā` (`rāja:338–342`)**: `imp 2nd sg` cannot have `sakaṃ` as subject; after `mā` it is an aorist 3rd sg. **`yatassa` (`rāja:293–296`)**: `assa` given as both pronoun and optative; the translation fits only the optative.
- **`cāveyyaṃ | opt reflx 1st sg`** (`duṭṭhadosa:34`): `-eyyaṃ` is active.
- **`sādiyeyya … (pass)`** with an active gloss (`tatuttari:44`, `rūpiya:21`, `mahānāma:28`).
- **ptp glossed "can be"** where the rule states an obligation: `senāvāsa:21`, `rāja:149`, `:219`, `:252`.
- **`uddissa ṭhātabbaṃ`** (`rāja:250–269`) rendered "for the sake of (it)".
- **`vikappaṃ āpajjeyya`** (`paṭhamaupakkhaṭa:52`, `dutiyaupakkhaṭa:54`): "cause an alteration in the robe"; the Vinaya sense is "make a stipulation about the robe".
- **`senāya | instr | with the army`** with `vasati` (`senāvāsa:20`, `uyyodhika`): locative "in the army" has the same form.
- **`bhūtagāmapātabyatāya | fem loc sg`** (`bhūtagāma:5`): could be instrumental or dative.
- **`kaddamaṃ | adj`** (`dubbaṇṇakaraṇa:22`): normally a noun. **`tiṇaṃ`, `mattikaṃ`** in `sappāṇaka`.
- **`kiñci | masc acc sg`** qualifying `atthaṃ` (`rāja:324` and 4 more); `kiñci` is the neuter form used adverbially.
- **`tassa 2 | masc gen sg`** referring to neuter `adhikaraṇa` (`saṅghabheda:103`).
- **Feminine lemma:** `aññātikāya … of aññātaka` (6 rows).
- **`dubbaṇṇa` as `dur + √var`** (`nisīdanasanthata:22`); **`avagaṇḍa` as `yuva > ava + gaṇḍa`** (`avagaṇḍakāraka:9`; DPD `ava + gaṇḍa`); **`chatta` as `√chad + ra`**.
- **`kattikā` glossed "last month of the rains season"**; **`aggaḷa` "hinge"**; **`uppathena` "not on the road"**; **`ekaṃ` "the same"** (`nāvābhirūhana:13`); **`sabhojana 1` "amorously engaged"** against its own construction.
- **`uttarimanussadhamma:54`**: the heading has no `avacaṃ` after `apassaṃ`; editions differ.
- **`cīvarāni + dāna`, `cīvarāni + kāra`** in accusative-tappurisa constructions (`gaṇabhojana:25`, `:30`): plural where `cīvaraṃ` is expected.

## Raised but not errors (checked against DPD or the text)

- `āvuso … voc of āyasmant`: DPD derives `āvuso` from `āyasmanto`. Only the POS (`noun` here, `ind` in DPD) and the construction `āyas + mant` differ.
- `avacaṃ | imperf 1st sg of avaca`: this is the DPD entry verbatim.
- `manasi | masc loc sg of manas`: DPD treats the `mano` group as masculine.
- Prefix `nī` in `nī + √dis`, `abhi + nī + phāde`, `pati + nī + saja`: DPD notation for `nis`.
- `āhacca | ptp | removable`: DPD `āhacca 2.1`.
- `anāpucchaṃ | prp`: a present participle nominative in `-aṃ` is a sound reading; only the two rows label it differently (`masc.nom.sg of` against `prp of`).
- `cīvaralābhena | adj`: correct, a bahubbīhi qualifying `bhikkhunā`.
- `sekhiya | ptp`, `sammuti √mun`, `vihesaka √his`, `ujjhāna ava > o > u`, `sāmisa sa + āma + isa`, `aphāsu masc`, `tiṃsa fem sg`, `jānaṃ | ind`, `patta √pā`, `theyya` nt / masc, `māsa` masc / nt: all as in DPD.
- `pācittiyaṃ | +loc`: consistent throughout; a convention.

## Recommendation

In order of value for the effort:

1. **Fix the systematic rows by script**, each a single search-and-replace reviewed once: `karaṇīyā` (75), stray `, comp` (about 270), POS `masc` / `fem` / `nt` (18), `evametaṃ` gloss (9), `dhammaṃ` gloss in SE 59–72 (14), `atikkāmayato` lemma (7), `khādaniya`, `mac` / `isntr` / `sadnhi`, compound-type spellings, the `<br>` endings.
2. **Repair the structural defects by hand** (about 15 places): the `#REF!` row, duplicated headings and blocks, orphaned members, the SE 73 / SE 74 mix-up, the `no` row in `ariṭṭha`, the incomplete second block of `adhikaraṇasamathā`.
3. **Correct the one-off grammar rows** in the three tables above (about 110 rows).
4. **Decide the conventions** before touching the rest: one label for absolutives, `sattamī` or `locative`, whether sandhi rows always get member rows and a meaning, whether homonym numbers stay in the Pāli cell, and whether SE 2–24 get their own files or at least index entries.
5. **Check the 11 Pāli readings** against the chosen edition.
6. **Write the missing translations** (about 240 sentences once placeholder and duplicate headings are discounted; the 75 Sekhiyas and the closing formulas are formulaic) and correct the 18 mistranslations listed.

## Remaining work for a complete audit

- A second, independent read. Each row was read once; the suttas audit found about as many additional errors on its second pass as on its first.
- A word-for-word comparison of the headings with an edition.
- A script comparison of each heading with its table (missing or extra rows); here that was done by eye only.
- A systematic DPD comparison of root, base and construction cells; only disputed items were looked up.

## Method

1. A script compacted the 217 files into eight batches in index order, keeping the original line numbers, and ran the mechanical checks and the cross-file consistency listing.
2. Eight reviewers (Claude Sonnet subagents) each read one batch row by row for grammar, glosses, translations, table-against-text and format, with instructions to separate confident errors from doubtful ones.
3. The findings were merged by Claude Fable 5.2. Cross-batch patterns were counted by script over the whole corpus. About 110 cited rows were printed from the source and compared. Disputed items were looked up in the local DPD database, which removed the reported "errors" listed under "Raised but not errors".

## Confidence

- **Format and consistency findings: 9/10.** They are script-derived or were checked against the source.
- **Systematic grammar errors and the lemma / agreement tables: 8/10.** Most were confirmed against the source row and follow from agreement within the sentence.
- **Compound-type judgments, gloss criticisms and the Doubtful list: 6/10.** They depend on DPD conventions and on interpretation.
- **Completeness: 6/10.** One reading pass by a weaker model than the merger; the reviewers' recall is unmeasured, and the Pāli text was not collated with an edition. Missing: a second independent pass and an edition to collate against.
