# Pātimokkha audit — rearranged for the TSV source

Source audit: `kamma/audit/pat-audit/pat-audit.md` (2026-11-10, written against the old `docs/` md files). This file re-keys it to `data/patimokkha_word_by_word.tsv`. **No suggestion was added, changed or judged; only items still present in the TSV are kept.** For the issue #24 review.

## How to read

- `TSV n` is the physical line in `data/patimokkha_word_by_word.tsv` (quoted cells can span lines, so it is not the record number). Lines shift after edits: apply from the bottom up, or re-locate by rule code + `pali` cell.
- Sections follow TSV order, headed by rule code (column `abbrev`) and `source` name. Items spanning several rules are in 'Corpus-wide'. Tags: `grammar`, `gloss`, `translation`, `format`, `convention` (needs a decision first), `pali-text` (check edition), `doubtful` (not confirmed), `same-word`.
- Multi-row items show the first rows and a total.

## Dropped as already fixed or obsolete in the TSV

- Missing sentence translations (all but the last line `sādhu sādhu sādhu!` now have one); `#REF!` row; placeholder `… 4` headings; duplicated headings and row blocks; raw `<br>` (now line breaks inside cells, kept only where listed); grammar-cell typos (`mac`, `isntr`, `sadnhi` …); placeholders `?` / `“”` / `ta + ?`; stray `, comp` on `bhikkhu`, `bhikkhunā`, `dhammā`, `nissaggiyaṃ`; `dutiyo` / `chappañca` tags; `dhāretabbaṃ`; missing `of` / `sg` in `iminā`, `cīvaraṃ`, `paṭinissaggāya`, `adhikaraṇaṃ`, `niṭṭhitā`; `bhagavant`; `eḷakaloma:42`; `mahānāma` split; `bāhuppacālaka` construction; `saṅghabheda` `uddeso` gloss; `ayaṃ`, `eso`, `hi`, `tāva`, `uposatha`, `capucapu` inconsistencies; `ariṭṭha` `no` row; `jivhānicchāraka` row; sandhi/`matante`/`dulladdhaṃ` POS items; pass `of sīssa`-type items listed below only where still present.
- POS-gender rows for `apanidhāna`, `ujjhānasaññī`, `paṭhamasenāsana` (already `noun`).

## Corpus-wide (scripted fixes)

- TSV 5827 … 6685 (75 rows) `[grammar]` `karaṇīyā` in `sikkhā karaṇīyā` (all Sekhiya sentences): `noun | nt abl sg of karaṇīya` → ptp, fem nom sg of `karaṇīya` (`karaṇīya 2`), agreeing with `sikkhā`; gloss "(the training) is to be done". Exclude TSV 5327 (PC 85), where the ablative noun is right.
- TSV 6073 … 6685 (50 rows) `[grammar]` stray `, comp` in the grammar cell of `karaṇīyā`.
- TSV 6082 … 6684 (49 rows) `[grammar]` stray `, comp` in the grammar cell of `sikkhā`.
- TSV 4876, 5630, 5668 `[grammar]` stray `, comp` on `bhikkhūhi`.
- TSV 3475, 3481 `[format]` compound type `genetive tappurisa` → `genitive tappurisa`.
- TSV 183, 504, 1595, 1791, 3119, 5526, 5781, 6701 … (9 rows) `[gloss]` accusative with no object marking: `tatthāyasmante` "in that case the venerables" (?)
- TSV 216, 525, 1612, 1808, 3134, 5547, 5802, 6722 … (9 rows) `[gloss]` `evametaṃ` glossed "therefore this" in the closing formula → "thus this" (`tasmā` already gives "therefore") (?)
- TSV 695, 2673, 2688, 3198, 3205, 4216, 4232, 4718 … (35 rows) `[convention]` compounds with member rows but empty type / construction cells: `samaṇuddesa` (9 rows in `kaṇṭaka`), `saññācikāya`, `piṇḍukkhepakaṃ` … `oṭṭhanillehakaṃ` (SE 44–54), `sabbahatthaṃ`, `sakabaḷena`, `ujjhānasaññī`, `sasitthakaṃ`, `uppannuppannānaṃ`, `nānappakārakaṃ`, `dirattatirattaṃ`, `sahaseyyaṃ`, `diyaḍḍhaṃ`, `aḍḍhateyyā` (?)
- TSV 720, 2573, 5363 `[gloss]` `sugata` "standard; commonly accepted" in `sugatavidatthi`, `sugataṅgula` → "Well Gone One" (genitive tappurisa, as `sugatacīvara` in `nanda`); the genitive reading is the correct one
- TSV 727, 775 `[pali-text]` `vatthuṃ desetabbaṃ` (kuṭikāra) against `vatthu desetabbaṃ` (vihārakāra) - should be `vatthuṃ desetabbaṃ` in both places.
- TSV 1629, 3463, 5875, 6730 `[convention]` headings with no final full stop (`mahallakavihāra`, `okkhittacakkhu`, `adhikaraṇasamathā`, `aniyatuddeso`) (??)
- TSV 1652, 1687, 1742, 1771 `[grammar]` `saddheyyavacasā` typed `kammadhāraya` → `kammadhāraya > bahubbīhi` - should be `kammadhāraya` everywhere.
- TSV 1700, 3213 `[convention]` source names `dutiyasahaseyyasikkhāpada` and `dutiyāniyatasikkhāpada` lack the final `ṃ`
- TSV 1833, 1852, 1876 `[grammar]` `ubbhata` derived from `√dhar (hold)`, `ud + √dhar + ta` → DPD `√bhar`, `ud + √bhar + ta`
- TSV 2057, 2094, 2202, 3608, 3621, 4408, 4428, 4442 … (9 rows) `[grammar]` `cīvaraṃ` tagged `nt nom sg` where it is the object → accusative
- TSV 2484, 2502, 2516, 2601, 2638 `[same-word]` gender of `eḷakaloma`: masc gen pl / nt nom pl in different rows (also `suddhakāḷakānaṃ`) - shoule be nt
- TSV 2985, 3026 `[same-word]` `kattikapuṇṇamaṃ` typed `kammadhāraya` here against `genitive tappurisa` at the `kattikatemāsikapuṇṇamaṃ` row (2985) - should be `kammadhāraya`
- TSV 3753, 3803 `[convention]` no comma before `pācittiyaṃ` (`gaṇabhojana`, `paramparabhojana`)
- TSV 3975, 5698, 5753 `[gloss]` adjective glossed as a clause: `agilāno` "is not ill" - "not sick; healthy"
- TSV 4620, 4661, 4667, 4745, 4789, 4797, 4876, 5630 … (9 rows) `[gloss]` `bhikkhūhi` glossed "with monks" where it is the agent → "by monks"
- TSV 4769, 5141, 5300, 5587, 5618, 5635, 5657, 5665 … (10 rows) `[convention]` quotes: PC / PD headings use `’ti`, SE and others `'ti` - change everywhere from `’` to `'`.
- TSV 5260, 5419, 5477, 5786 `[convention]` headings with trailing space or comma (`ratana`, `kaṇḍupaṭicchādi`, `nanda`, `pāṭidesanīyā`) (??)
- TSV 6425, 6441, 6454, 6467 `[grammar]` `chattapāṇissa`, `daṇḍapāṇissa`, `satthapāṇissa`, `āvudhapāṇissa` typed `kammadhāraya` → `kammadhāraya > bahubbīhi` - make all `kammadhāraya > bahubbīhi`
- TSV 6458, 6471, 6490, 6503, 6516, 6529, 6541, 6556 … (14 rows) `[gloss]` `dhammaṃ` glossed "act, practice, behaviour" in `dhammaṃ desessāmi` → "teaching, Dhamma" (as `chattapāṇi`, `daṇḍapāṇi`)
- TSV 6514, 6527 `[gloss]` `gatassa` "to (a person) on" (truncated) (`yāna`, `sayana`) > "to (a person) going (by)"
- TSV 6539, 6581, 6597, 6609 `[gloss]` "to seated (a person), sitting" (`chamā`, `nīcāsana`, `pallatthika 2`, `ṭhita`) > "to (a person) seated, sitting"
- TSV 6730, 6738 `[pali-text]` heading lacks `dhammā` (`… satta adhikaraṇasamathā dhammā uddesaṃ āgacchanti`); the table has the row - add everywhere (sentences column and first row)

## By rule, in TSV order

### NI · nidānuddeso (TSV from line 3)

- TSV 27 `[convention]` `-dasa` without the space - add space
- TSV 35 `[grammar]` `pattakallaṃ` is `nt nom sg` but its member `kallaṃ` is `masc acc sg of kāla` - should be also nt
- TSV 110 `[gloss]` "in of kind; in of type" > "in having quality"
- TSV 115 `[grammar]` lemma `of anusāvita` / `anusāviyamāna` → `anussāvita` / `anussāviyamāna`
- TSV 164 `[translation]` "fallen" for `āpannena` > "who has committed (an offence),"
- TSV 131 `[format]` POS column holds a gender (`masc` / `fem` / `nt`) → `noun`

### PA · pārājikuddeso (TSV from line 226)

- TSV 230 `[translation]` Pārājika: "defeat" here against "disqualification / disqualified" elsewhere > everywhere "defeat" / "defeated".

### PA 2 · adinnādāna (TSV from line 270)

- TSV 281 `[grammar]` `sankhāyati` → `saṅkhāyati`
- TSV 282 `[grammar]` `ādiyeyya` lacks `+acc` (the parallel row has it)
- TSV 283, 317, 331 `[translation]` "You are a immature!"; `!,”` stray comma; "something what has not been given"; "given(and)"
- TSV 292 `[meaning_lit]` "king's men" remove
- TSV 302 `[translation]` "king's men" for `rājāno` > authorities
- TSV 308 `[gloss]` `bālo` "fool, idiot, moron" > "fool; idiot; immature person"
- TSV 319 `[grammar]` lemma `tathārupa` → `tathārūpa`

### PA 4 · uttarimanussadhamma (TSV from line 404)

- TSV 450 `[grammar]` `ajānaṃ` lemma `from ājānāti` → `from na jānāti`
- TSV 461 `[grammar]` lemma `of vilapi` → `vilapati`

### SA 2 · kāyasaṃsagga (TSV from line 563)

- TSV 594 `[translation]` "any of the limb" (?)

### SA 3 · duṭṭhullavācā (TSV from line 597)

- TSV 613, 615 `[gloss]` "with related to sexual intercourse", "with connected with" > "related to sexual intercourse", "connected with"

### SA 4 · attakāmapāricariya (TSV from line 620)

- TSV 649 `[grammar]` `kalyāṇadhammaṃ` typed `kammadhāraya` → `kammadhāraya > bahubbīhi`
- TSV 658 `[gloss]` `paricareyya` "she should serve, administer" → "serve, attend on"

### SA 5 · sañcaritta (TSV from line 665)

- TSV 689 `[gloss]` "in related to moment" > "related to moment"

### SA 7 · vihārakāra (TSV from line 762)

- TSV 768 `[grammar]` `attuddesaṃ`: `fem acc sg` → masc acc sg (with `vihāraṃ`)

### SA 9 · aññabhāgiya (TSV from line 851)

- TSV 897, 908 `[translation]` "is belonging to another class"; "which a mere pretext" > "belongs to another class"; "which is a mere pretext"

### SA 10 · saṅghabheda (TSV from line 911)

- TSV 922, 945 `[grammar]` `adhikaraṇaṃ` tagged nominative where it is the object of `samādāya paggayha` → accusative
- TSV 960 `[gloss]` "Patimokkha" spelling > Pātimokkha

### SA 11 · bhedānuvattaka (TSV from line 1008)

- TSV 1052, 1070 `[grammar]` `amhākaṃ`: `masc gen/dat pl` → `1st gen/dat pl` (no gender; so `dubbaca`)
- TSV 1076 `[translation]` `api` in `amhākampetaṃ` is untranslated; two alternative translations are joined by `(or)` (a line break in the cell)
---- approved untill here -----
- TSV 1085 `[grammar]` `assu`: `pron | opt 3rd pl of assa` → POS verb, of atthi
- TSV 1102 `[gloss]` `āyasmantānampi` "and for the venerables" → "for the venerables too"
- TSV 1108 `[grammar]` `ruccittha`: `aor 2nd pl of rucci`, base `(pass)` → aor 3rd sg (middle) of ruccati; subject is `saṅghabhedo`
- TSV 1120 `[gloss]` "Patimokkha" spelling
- TSV 1125 `[translation]` "Let the community be agreeable for the venerables" — with `saṅghena` the venerables are to agree with the community (`saṅghabheda` has it right); the rows differ too (`+dat` against `+instr`)

### SA 12 · dubbaca (TSV from line 1156)

- TSV 1220 `[gloss]` `akāsi` "(venerable) make!" — stands with `mā`, prohibitive
- TSV 1259 `[grammar]` `vuṭṭḥāpana` → `vuṭṭhāpana`

### SA 13 · kuladūsaka (TSV from line 1292)

- TSV 1300, 1363, 1368, 1468 `[same-word]` `√har (live)` against `√har (carry)` elsewhere
- TSV 1307 `[translation]` "depending on a certain village or town who is a corrupter of families": the relative clause attaches to the town instead of the monk
- TSV 1362, 1467 `[grammar]` `imamhā`: `nt abl sg` → masc abl sg (with `āvāsā`)
- TSV 1398, 1442 `[grammar]` construction `bhaya + gāmino` → `bhaya + gāmī` (as the parallel rows)
- TSV 1414 `[translation]` "Because of this kind offence"
- TSV 1426 `[gloss]` `avaca` "one says | one said" — stands with `mā`, prohibitive

### SA · saṅghādisesuddeso (TSV from line 1503)

- TSV 1547 `[gloss]` `rattaṃ` meaning "days" with literal "night"
- TSV 1554 `[gloss]` `ciṇṇamānatto` "who has completed probation" — mānatta is not probation (parivāsa); the same file has "deference" and "penance"
- TSV 1619 `[translation]` "offences is finished"

### AN 1 · paṭhamaaniyata (TSV from line 1632)

- TSV 1639 `[grammar]` `raho`: `adv, masc nom sg of rahas` — `rahas` is nt; indeclinable
- TSV 1642 `[gloss]` typo "doint"
- TSV 1650 `[grammar]` `taṃ` (in `tamenaṃ`): `fem acc sg` → masc acc sg (the monk)
- TSV 1667, 1682 `[translation]` "dealt in accordance to"; "This is too an uncertain case."

### AN 2 · dutiyāniyata (TSV from line 1700)

- TSV 1704 `[format]` `na h'eva` analysed twice (`na` + `heva`, then `naheva`) (?)
- TSV 1710, 1714 `[gloss]` typo "doint" / "ts"
- TSV 1728 `[grammar]` lemma `tathārupa` → `tathārūpa`
- TSV 1753, 1766, 1781 `[translation]` "dealt in accordance to"; "This is too an uncertain case."
- TSV 1778 `[gloss]` `ayampi` "he too" → "this too"

### AN · aniyatuddeso (TSV from line 1783)

- TSV 1815 `[translation]` "Two uncertain (cases) is finished"; "for six-night"

### NP 2 · udosita (TSV from line 1850)

- TSV 1855 `[grammar]` `akeratta` → `ekaratta`
- TSV 1857 `[gloss]` `rattaṃ` meaning "day" with literal "night"; `ekarattampi` "just for one night, for one day"

### NP 3 · akālacīvara (TSV from line 1874)

- TSV 1890 `[grammar]` `khippameva | sandhi, pr + ind` → ind + ind
- TSV 1906 `[grammar]` `taṃ`: `masc nom sg` → nt nom sg (with `cīvaraṃ`)

### NP 4 · purāṇacīvara (TSV from line 1928)

- TSV 1944 `[translation]` stray comma, "beat used robe"

### NP 5 · cīvarapaṭiggahaṇa (TSV from line 1947)

- TSV 1950, 1951 `[gloss]` genitive glossed as instrumental: `aññātikāya` "by unrelated", `bhikkhuniyā` "by a nun" in `hatthato`

### NP 6 · aññātakaviññatti (TSV from line 1962)

- TSV 1986 `[gloss]` typo "who's"

### NP 8 · paṭhamaupakkhaṭa (TSV from line 2038)

- TSV 2067 `[translation]` `cetāpetvā`: "Having bought" (NP 8, NP 10) against "exchanged" (NP 9 and the row glosses)
- TSV 2076 `[gloss]` locative glossed as genitive: `cīvare` "of robe"

### NP 9 · dutiyaupakkhaṭa (TSV from line 2110)

- TSV 2110 `[pali-text]` heading `paccekacīvaracetāpanā upakkhaṭā honti`: CST reads `-cetāpannāni upakkhaṭāni`; if the masculine reading is intended, the rows should not say `nt nom pl` (check edition)
- TSV 2119, 2124 `[grammar]` `paccekacīvaracetāpanā`, `upakkhaṭā`: `nt nom pl` — nt pl would be `-āni`; see Pāli text
- TSV 2126, 2173 `[translation]` "of an unrelated male householders … has been set up"; "for a such and such a robe"
- TSV 2148 `[gloss]` locative glossed as genitive: `cīvare` "of robe"

### NP 10 · rāja (TSV from line 2182)

- TSV 2187 `[gloss]` typo "offical"
- TSV 2195, 2212, 2239, 2265, 2303, 2418 `[format]` POS column holds a gender (`masc` / `fem` / `nt`) → `noun`
- TSV 2208 `[translation]` `cetāpetvā`: "Having bought" (NP 8, NP 10) against "exchanged" (NP 9 and the row glosses)
- TSV 2227 `[grammar]` `patiggaṇhāti` → `paṭiggaṇhāti`
- TSV 2258 `[grammar]` `kappiyanti | sandhi, pr + ind` → adj + ind
- TSV 2351 `[gloss]` instrumental glossed as ablative: `cīvarena` "from a robe" in `attho me cīvarena`
- TSV 2377 `[doubtful]` `uddissa ṭhātabbaṃ` rendered "for the sake of (it)"
- TSV 2407 `[doubtful]` `yatassa`: `assa` given as both pronoun and optative; the translation fits only the optative
- TSV 2421 `[translation]` `no ce abhinipphādeyya` translated "If he would succeed in obtaining" — the negation is dropped: "If he should not succeed"
- TSV 2438, 2456 `[translation]` `āyasmanto`, `vo`, `yuñjantu` are plural; the translations have "Sir", "Let the sir get back what is his"; `pahiṇittha` is "sent", not "conveyed"

### NP 12 · suddhakāḷaka (TSV from line 2478)

- TSV 2485 `[grammar]` `- eḷaka`: `noun | nt` → masc

### NP 13 · dvebhāga (TSV from line 2494)

- TSV 2508, 2526 `[translation]` "muddy brown", "sheep-wool" against "ruddy brown", "sheep's hair" for identical Pāli

### NP 14 · chabbassa (TSV from line 2529)

- TSV 2539 `[pali-text]` heading `visajjetvā vā avisajjetvā vā` (the row lemma is `vissajjeti`) (check edition)

### NP 15 · nisīdanasanthata (TSV from line 2561)

- TSV 2564 `[grammar]` member `santhataṃ | nom sg` in an acc compound → acc, or stem
- TSV 2567 `[gloss]` `kārayamānena` "having made" (a present participle)
- TSV 2572 `[gloss]` typo "standart"
- TSV 2575 `[grammar]` `ādātabbā`: `fem nom pl` → fem nom sg (subject `sugatavidatthi`)
- TSV 2579, 2592 `[translation]` "throughout" for `sāmantā` against the row gloss "all around"

### NP 16 · eḷakaloma (TSV from line 2595)

- TSV 2597 `[grammar]` `addhānamaggapgaṭipanna` → `addhānamaggapaṭipanna`
- TSV 2602 `[gloss]` `uppajjeyyuṃ` "it could arise" (plural)

### NP 20 · kayavikkaya (TSV from line 2685)

- TSV 2697 `[grammar]` lemma `of kosiyavagga` → `of eḷakalomavagga`

### NP 21 · patta (TSV from line 2704)

- TSV 2707 `[format]` POS column holds a gender (`masc` / `fem` / `nt`) → `noun`

### NP 22 · ūnapañcabandhana (TSV from line 2716)

- TSV 2731 `[pali-text]` heading `nissajitabbo` (the row lemma is `nissajjitabba`) (check edition)
- TSV 2735, 2757 `[format]` POS column holds a gender (`masc` / `fem` / `nt`) → `noun`

### NP 23 · bhesajja (TSV from line 2771)

- TSV 2785 `[translation]` "butter" for `navanīta` (the row has "fresh butter")

### NP 24 · vassikasāṭika (TSV from line 2810)

- TSV 2829, 2848 `[translation]` "robe-cloth for the rain's cloth" against "rain's bathing-cloth"

### NP 25 · cīvaraacchindana (TSV from line 2851)

- TSV 2869 `[translation]` "given a robe to a monk, who is angry (and) displeased": the comma gives the anger to the recipient; `kupito anattamano` is the giver

### NP 27 · mahāpesakāra (TSV from line 2888)

- TSV 2940 `[gloss]` `suvilekhitaṃ` "well combed" against the translation's "well scraped"
- TSV 2953 `[gloss]` `āyasmantānaṃ` "for the the good men"
- TSV 2956 `[grammar]` `- mattaṃ`: `masc` inside nt `kiñcimattaṃ` → nt
- TSV 2958 `[gloss]` `anupadajjeyyāma` "I could give" (1st pl)
- TSV 2960 `[translation]` "Perhaps I could also give" (1st pl)
- TSV 2967 `[grammar]` lemma `of anupadajjeyya` → `anupadajjati`
- TSV 2978 `[translation]` "and that monk, having said so, would give": "if" is missing

### NP 28 · accekacīvara (TSV from line 2981)

- TSV 3007 `[grammar]` `yāva | +dat` → governs acc `cīvarakālasamayaṃ`

### NP 29 · sāsaṅka (TSV from line 3023)

- TSV 3023 `[grammar]` `upavassaṃ` lemma `from upavassati` → `upavasati`
- TSV 3023, 3048, 3070, 3079, 3085 `[same-word]` `√har (live)` against `√har (carry)` elsewhere
- TSV 3070 `[grammar]` lemma `vippāvāsa` → `vippavāsa`

### NP 30 · pariṇata (TSV from line 3093)

- TSV 3100 `[grammar]` `attano`: `masc dat sg` with `atthāya (+gen)` → gen sg (as `paṇītabhojana`)

### NP · nissaggiyapācittiyā (TSV from line 3112)

- TSV 3136 `[translation]` "requiring confessing"
- TSV 3143 `[translation]` omits "thirty" (`tiṃsa`); "forfeiture" here, "relinquishment" elsewhere

### PC 04 · padasodhamma (TSV from line 3181)

- TSV 3184 `[grammar]` lemma `of anupasampannaṃ` → `anupasampanna`

### PC 05 · paṭhamasahaseyya (TSV from line 3192)

- TSV 3195 `[grammar]` lemma `of anupasampannaṃ` → `anupasampanna`

### PC 09 · duṭṭhullārocana (TSV from line 3258)

- TSV 3262 `[grammar]` lemma `of duṭṭhalla` → `duṭṭhulla`

### PC 10 · pathavīkhaṇana (TSV from line 3272)

- TSV 3272, 3275 `[pali-text]` heading `paṭhaviṃ` against the lemma and title `pathavī` (check edition)

### PC 11 · bhūtagāma (TSV from line 3290)

- TSV 3290 `[doubtful]` `bhūtagāmapātabyatāya | fem loc sg`: could be instrumental or dative

### PC 16 · anupakhajja (TSV from line 3391)

- TSV 3407 `[grammar]` lemma `of sambhāda` → `sambādha`; construction `saṃ + √bhād + a` → `√bādh`

### PC 17 · nikkaḍḍhana (TSV from line 3423)

- TSV 3431, 3433 `[gloss]` mixed forms: "he would drag out, expels, remove"

### PC 18 · vehāsakuṭi (TSV from line 3440)

- TSV 3445, 3446, 3447, 3448 `[grammar]` `upari`, `vehāsa`, `kuṭiyā` listed flat; the structure is (`upari` + `vehāsa`) + `kuṭi`

### PC 19 · mahallakavihāra (TSV from line 3465)

- TSV 3472 `[gloss]` `dvārakosā` "as the door frame" → with `yāva` "up to the door frame"
- TSV 3475 `[format]` raw line break inside the Pāli word itself (`aggaḷaṭṭhapanāya⏎`, also in its lemma)
- TSV 3490 `[grammar]` `pariyāyaṃ`: `nt nom sg` → masc acc sg
- TSV 3496, 3508 `[translation]` "standing on a few crops" for `appaharite ṭhitena` (sense: "standing where there is little vegetation"); also "upto", and "can be arranged" for a ptp

### PC 20 · sappāṇaka (TSV from line 3511)

- TSV 3526 `[translation]` "on grass or clay", while the table makes `tiṇaṃ` and `mattikaṃ` accusative objects

### PC 22 · atthaṅgata (TSV from line 3545)

- TSV 3550 `[grammar]` lemma `of atthaṇgata` → `atthaṅgata`
- TSV 3557 `[translation]` "a authorised monk"

### PC 23 · bhikkhunūpassaya (TSV from line 3560)

- TSV 3560, 3563 `[pali-text]` `bhikkhun'ūpassayaṃ` with long `ū`; the third occurrence has `bhikkhun'upassayaṃ`; the stem name also has `ū` (check edition)

### PC 24 · āmisa (TSV from line 3586)

- TSV 3591 `[grammar]` `āmisahetu | abyayībhāva` — first member is a noun, so a tappurisa used adverbially

### PC 27 · saṃvidhāna (TSV from line 3630)

- TSV 3668 `[translation]` `satthagamanīyo` detached into "which has to be gone with a company"

### PC 28 · nāvābhirūhana (TSV from line 3671)

- TSV 3691 `[grammar]` `aññatra` has no case although it governs `tiriyaṃtaraṇāya`; other `aññatra` rows have `+abl`

### PC 29 · paripācita (TSV from line 3699)

- TSV 3703 `[grammar]` construction `bhikkhuni + paripācita` → `bhikkhunī`
- TSV 3710 `[grammar]` `genitive tappurisa | gihī + samārambha` — type and construction disagree; row spells `gihī-` against the heading `gihi-`
- TSV 3710 `[gloss]` typo "inititative"

### PC 32 · gaṇabhojana (TSV from line 3755)

- TSV 3794 `[gloss]` `samaṇabhattasamayo` "time of food being offered by an ascetic" — the meal is given to ascetics

### PC 33 · paramparabhojana (TSV from line 3805)

- TSV 3805, 3806 `[grammar]` construction `paramparā + bhojana` against the member row `parampara`

### PC 34 · kāṇamātu (TSV from line 3824)

- TSV 3826, 3827 `[grammar]` `kulaṃ` `nt nom sg` → acc; `upagataṃ` `pp | nt nom sg` → masc acc sg (with `bhikkhuṃ`)
- TSV 3844 `[grammar]` `patigaṇheyya` / `paṭigahetabba` → `paṭiggaṇheyya` / `paṭiggahetabba`
- TSV 3845 `[translation]` "should an approached family invite … a monk": `upagataṃ` qualifies `bhikkhuṃ` ("a monk who has come to a family"); "biscuits" for `manthehi` and "take away" for `abhihaṭṭhuṃ` are doubtful

### PC 35 · paṭhamapavāraṇā (TSV from line 3866)

- TSV 3872 `[grammar]` lemma `of khādaniya` → `khādanīya`

### PC 36 · dutiyapavāraṇā (TSV from line 3885)

- TSV 3892 `[grammar]` lemma `of khādaniya` → `khādanīya`
- TSV 3898 `[translation]` `abhihaṭṭhuṃ` is untranslated; the instrumentals "with non-staple or staple food" become "to chew or eat", which belongs to the next sentence; ends with a full stop although the clause continues

### PC 37 · vikālabhojana (TSV from line 3915)

- TSV 3919 `[grammar]` lemma `of khādaniya` → `khādanīya`

### PC 38 · sannidhikāraka (TSV from line 3931)

- TSV 3934, 3935 `[format]` one heading word, two rows (`sannidhikārakaṃ` adverb and `sannidhikārakaṃ 2` adjective) (?)
- TSV 3936 `[grammar]` lemma `of khādaniya` → `khādanīya`

### PC 39 · paṇītabhojana (TSV from line 3948)

- TSV 3971 `[grammar]` `evarūpāni`: member `evaṃ` against construction `eva + rūpa`; `rūpāni | nom pl` inside an acc pl compound

### PC 40 · dantapona (TSV from line 3984)

- TSV 3987 `[grammar]` `adinnaṃ`: `noun | nt acc sg` → adj, masc acc sg (with `āhāraṃ`)

### PC 41 · acelaka (TSV from line 4011)

- TSV 4021 `[grammar]` lemma `of khādaniya` → `khādanīya`

### PC 42 · uyyojana (TSV from line 4030)

- TSV 4050, 4052 `[gloss]` `dāpetvā` "having got", `adāpetvā` "having not got" → causative: "having had (it) given"
- TSV 4056 `[grammar]` lemma `of gacchatu` → `gacchati`

### PC 44 · rahopaṭicchanna (TSV from line 4102)

- TSV 4108 `[gloss]` "on covered, concealed"

### PC 46 · cāritta (TSV from line 4130)

- TSV 4145 `[gloss]` `āpajjeyya` "would cause"

### PC 50 · uyyodhika (TSV from line 4232)

- TSV 4244 `[grammar]` `senābyūhaṃ | dative tappurisa | senāya + byūha` → genitive

### PC 53 · hassadhamma (TSV from line 4278)

- TSV 4279 `[grammar]` `+loc` on `hassadhamme`, which governs nothing

### PC 58 · dubbaṇṇakaraṇa (TSV from line 4376)

- TSV 4386 `[grammar]` `karaṇānaṃ`: `nt gen sg` → gen pl (parent row has pl)
- TSV 4400 `[gloss]` `anādā` "not adding, not having included" → "not having taken"

### PC 60 · apanidhāna (TSV from line 4436)

- TSV 4450 `[doubtful]` "dative tappurisa" with a genitive in the construction (`attano + uddesa`, `vatthuno + desanā`, `pattassa + dhovana`, `pānīyassa + thālaka`, `ālokāya + sandhi` …)

### PC 63 · ukkoṭana (TSV from line 4501)

- TSV 4508 `[grammar]` `nihatādhikaraṇaṃ | accusative tappurisa | nihata + adhikaraṇaṃ` — pp + noun is a kammadhāraya; construction should not be inflected

### PC 64 · duṭṭhulla (TSV from line 4521)

- TSV 4526 `[grammar]` lemma `of duṭṭhalla` → `duṭṭhulla`; also `paṭicchādeyya` lemma `of paṭichādeti` → `paṭicchādeti`

### PC 68 · ariṭṭha (TSV from line 4588)

- TSV 4598 `[grammar]` lemma `masc acc sg of dhamma` → `of desita`
- TSV 4599 `[grammar]` base `√ña + a > jānā` → `√ñā + nā`
- TSV 4604, 4644, 4646 `[grammar]` construction `anatra + aya + ika`, "in-betweeen" → `antara`, "in-between"
- TSV 4605 `[gloss]` number: `dhammā` "act; practice" (plural at the later occurrence)
- TSV 4626 `[gloss]` `avaca` "one says | one said" — stands with `mā`, prohibitive
- TSV 4629 `[grammar]` lemma `of abbhācikkhi` → `abbhācikkhati`
- TSV 4658 `[format]` `pana` after `evañca` is not in the heading

### PC 69 · ukkhittasambhoga (TSV from line 4689)

- TSV 4695 `[gloss]` `- vādinā` "with a view" → "(one) who asserts"
- TSV 4704 `[grammar]` `appaṭinissaṭṭhena`: `masc nom sg` → masc instr sg
- TSV 4713 `[gloss]` `kappeyya` "should take, use" with `seyyaṃ` — `seyyaṃ kappeti` is "lie down"

### PC 70 · kaṇṭaka (TSV from line 4718)

- TSV 4719 `[convention]` indent depth: `- samaṇuddeso` under `samaṇuddesopi` should be one level deeper (as under `hassāpekkhopi`)
- TSV 4729 `[grammar]` lemma `masc acc sg of dhamma` → `of desita`
- TSV 4730 `[grammar]` base `√ña + a > jānā` → `√ñā + nā`
- TSV 4733, 4773, 4775 `[grammar]` construction `anatra + aya + ika`, "in-betweeen" → `antara`, "in-between"
- TSV 4752 `[gloss]` `avaca` "one says | one said" — stands with `mā`, prohibitive
- TSV 4757 `[grammar]` lemma `of abbhācikkhi` → `abbhācikkhati`
- TSV 4778 `[gloss]` typo "ts"
- TSV 4786 `[format]` `pana` after `evañca` is not in the heading
- TSV 4832, 4833, 4834 `[convention]` `kaṇṭaka` member rows `cara`, `pire` lack the `- ` prefix (`carapire`)
- TSV 4833 `[grammar]` lemma `of caratu` → `carati`
- TSV 4862 `[gloss]` `kappeyya` "should take, use" with `seyyaṃ` — `seyyaṃ kappeti` is "lie down"

### PC 71 · sahadhammika (TSV from line 4873)

- TSV 4891 `[grammar]` `yāva | +dat` → conjunction, governs nothing
- TSV 4893 `[grammar]` `aññaṃ`: `nt acc sg` → masc acc sg (with `bhikkhuṃ`)
- TSV 4909 `[grammar]` lemma `of aññtabba` → `aññātabba`

### PC 72 · vilekhana (TSV from line 4918)

- TSV 4934 `[grammar]` `uddiṭṭhehi`: `nt instr sg` → instr pl

### PC 73 · mohana (TSV from line 4952)

- TSV 4966 `[grammar]` base `√ña + a > jānā` → `√ñā + nā`
- TSV 4966 `[pali-text]` the row is `ājānāmi`; the heading has `jānāmi` (check edition)
- TSV 4989 `[grammar]` `nisinnapubbaṃ`: `noun | nt nom sg` → adj, masc acc sg (with `bhikkhuṃ`)
- TSV 4992 `[grammar]` `iminā`: `nt instr sg` → masc instr sg (with `bhikkhunā`)
- TSV 5056 `[grammar]` lemma `of mahanka` → `mohanaka`

### PC 75 · talasattika (TSV from line 5073)

- TSV 5079 `[grammar]` lemma `of sattika` → `talasattika`

### PC 78 · upassuti (TSV from line 5125)

- TSV 5135 `[grammar]` `vivādāpannānaṃ`: `noun` → adj (with `bhikkhūnaṃ`)
- TSV 5147 `[grammar]` `sossāmi`: `fut 3rd pl` → fut 1st sg

### PC 79 · kammappaṭibāhana (TSV from line 5157)

- TSV 5169 `[gloss]` `āpajjeyya` "would cause"

### PC 81 · dubbala (TSV from line 5192)

- TSV 5202 `[gloss]` `āpajjeyya` "would cause"

### PC 83 · antepura (TSV from line 5237)

- TSV 5244 `[grammar]` lemma `of avasitta` → `of abhisitta`

### PC 85 · vikālagāmappavesana (TSV from line 5313)

- TSV 5323 `[gloss]` `tathārūpā` "suitable, appropriate" → "of such a kind" (as `tatiyapāṭidesanīya`)

### PC 89 · nisīdana (TSV from line 5391)

- TSV 5391 `[grammar]` lemma `of nidsīdana` → `nisīdana`

### PC 90 · kaṇḍupaṭicchādi (TSV from line 5421)

- TSV 5427, 5429 `[gloss]` `kārayamānena` "building", `kāretabbā` "should be built" for cloths; "making / made" elsewhere

### PC 91 · vassikasāṭikā (TSV from line 5450)

- TSV 5455, 5457 `[gloss]` `kārayamānena` "building", `kāretabbā` "should be built" for cloths; "making / made" elsewhere
- TSV 5458 `[translation]` "robe-cloth for the rain's cloth" against "rain's bathing-cloth"

### PC 92 · nanda (TSV from line 5479)

- TSV 5482, 5497, 5509 `[grammar]` `sugatacīvarappamāṇaṃ`: `nt acc sg` → nt nom sg (predicate of `idaṃ`), at the first two occurrences

### PD 1 · paṭhamapāṭidesanīya (TSV from line 5568)

- TSV 5576 `[grammar]` lemma `of khādaniya` → `khādanīya`
- TSV 5594 `[grammar]` lemma `of āpajji` → `āpajjati` (as `dutiyapāṭidesanīya`)

### PD 2 · dutiyapāṭidesanīya (TSV from line 5603)

- TSV 5621, 5625, 5636, 5658 `[grammar]` `detha`, `apasakka`: lemma `of detu`, `apasakkatu` → `deti`, `apasakkati`
- TSV 5625 `[format]` an extra `detha` row after `dethāti`, without prefix or `iti` row
- TSV 5639, 5661 `[grammar]` `yāva | +dat` → conjunction, governs nothing
- TSV 5645 `[pali-text]` `ekassa'pi` (check edition)
- TSV 5651, 5652 `[format]` one heading word, two rows (`nappaṭibhāseyya 1`, `2`) (?)
- TSV 5677 `[grammar]` lemma `of paṭidesati` → `paṭideseti`

### PD 3 · tatiyapāṭidesanīya (TSV from line 5682)

- TSV 5699 `[grammar]` lemma `of khādaniya` → `khādanīya`
- TSV 5717 `[grammar]` lemma `of āpajji` → `āpajjati` (as `dutiyapāṭidesanīya`)

### PD 4 · catutthapāṭidesanīya (TSV from line 5725)

- TSV 5744 `[grammar]` lemma `of khādaniya` → `khādanīya`
- TSV 5766 `[grammar]` lemma `of āpajji` → `āpajjati` (as `dutiyapāṭidesanīya`)

### SE 7 · okkhittacakkhu (TSV from line 5877)

- TSV 5879 `[grammar]` `- cakkhu`: `adj | masc nom sg | with eyes` → noun nt, "eye"

### SE 11 · ujjagghika (TSV from line 5919)

- TSV 5920, 5929 `[format]` POS column holds a gender (`masc` / `fem` / `nt`) → `noun`

### SE 15 · kāyappacālaka (TSV from line 5955)

- TSV 5958 `[grammar]` lemma `of pacālakaṃ` → `pacālaka`

### SE 17 · bāhuppacālaka (TSV from line 5975)

- TSV 5978 `[grammar]` lemma `of pacālakaṃ` → `pacālaka`

### SE 19 · sīsappacālaka (TSV from line 5995)

- TSV 5998 `[grammar]` lemma `of pacālakaṃ` → `pacālaka`

### SE 37 · sūpodanaviññatti (TSV from line 6186)

- TSV 6192 `[grammar]` `attano`: `masc dat sg` with `atthāya (+gen)` → gen sg (as `paṇītabhojana`)

### SE 38 · ujjhānasaññī (TSV from line 6201)

- TSV 6208 `[gloss]` `olokessāmi` "I will look down" → "look at"

### SE 41 · anāhaṭa (TSV from line 6240)

- TSV 6245 `[grammar]` `vivarissāmīti` POS `sandhi, pr + ind` → `fut + ind`

### SE 55 · sāmisa (TSV from line 6398)

- TSV 6399 `[gloss]` `sāmisena` "with a dirty" (truncated)

### SE 57 · chattapāṇi (TSV from line 6424)

- TSV 6425 `[gloss]` typo "an sunshade"

### SE 66 · veṭhita (TSV from line 6549)

- TSV 6550 `[grammar]` `veṭhitasīsassa` typed `kammadhāraya` → `kammadhāraya > bahubbīhi`
- TSV 6554 `[grammar]` lemma `of sīssa` → `sīsa`

### SE 67 · oguṇṭhita (TSV from line 6564)

- TSV 6565 `[grammar]` `oguṇṭhitasīsassa` typed `kammadhāraya` → `kammadhāraya > bahubbīhi`
- TSV 6567 `[grammar]` lemma `of sīssa` → `sīsa`

### SE 75 · udakeuccāra (TSV from line 6674)

- TSV 6688 `[grammar]` lemma `of surusuruvagga` → `of pādukavagga`

### AS · adhikaraṇasamathā (TSV from line 6731)

- TSV 6750 `[pali-text]` `paṭiññāya kāretabbo` here against `kāretabbaṃ` at the later occurrence (check edition)
- TSV 6753 `[grammar]` lemma `of samukhā`, construction `sa + mukha` → `sammukhā`, `saṃ + mukha`
- TSV 6758 `[grammar]` lemma `of sativinayo` → `of sativinaya`
- TSV 6777, 6779 `[grammar]` `pāpiyyasikā` built as `pāpa + iya + [s] + ikā` and as `tassa + pāpiya > pāpiyya + [s] + ikā`
