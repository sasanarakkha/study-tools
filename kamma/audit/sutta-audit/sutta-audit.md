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

1. **MN 107 has no ID column** (5 columns against 6 everywhere else). It also uses `para N` markers, apostrophe sandhi (`ten’upasaṅkami`), and its own POS labels (`pn`, `ord`, `(pp as) adj`). — **re-check: undecided — owner decision: add an ID column to MN 107, or accept its 5-column layout. The `pn`/`ord`/apostrophe-sandhi drift is also an owner convention call.**
2. **The ID column is largely empty in many SN files.** Counting all filled rows:
   - Worst: `35-232` 430 of 531 rows without an ID, `35-247` 342 of 536, `22-82` 320 of 523, `35-241` 286 of 526, `35-70` 229 of 320, `22-59` 193 of 346. — **re-check: undecided — each missing ID must be looked up in DPD row by row; count not re-checked**
   - Every SN 35 file is affected (between 48% and 81% of rows). — **re-check: undecided — same as 42 (sub-bullet of it); percentages not re-checked**
   - Complete: `22-12`, `22-18`, `22-23`, `22-24`, `22-28`, `56-1`, `56-5`, `56-13`, `56-25`, `56-27`, `56-28`. The other SN 56 files miss at most 7 rows each. — **re-check: drop: not a defect, only context for 42 (lists the files that are complete)**
3. **Stub tables have no header row.** The first vocabulary word sits above the `| --- |` line, so it renders as the table header (e.g. `| 9320 | asaṅkhataṃ |` in SN 43). Affected tables: SN 43 (3), SN 45 (7), SN 46 (7), SN 47 (8), SN 12 (7). — **re-check: adjust: insert `| ID | Pāli | POS | Grammar | English | Construction |` followed by a `| --- | --- | --- | --- | --- | --- |` line above the FIRST vocabulary row of each stub table (e.g. above `maggasamyutta-samyutta-sn-45.md:35`), and delete the old `| --- |` separator line that sat below the first vocabulary row (SN 43/45/46/47/12); count not re-checked (7)**
4. **`nidana-samyutta-sn-12.md` lines 818–862 have 7 columns** instead of 6 (45 rows). — **re-check: adjust: `nidana-samyutta-sn-12.md:818–845`: drop the 7th, empty cell from every row, so `| --- |` ×7 becomes ×6. Delete the all-empty rows 846–862 (they hold no data). (8)**
5. **The example row leaked in as a table header** at `nidana-samyutta-sn-12.md:371` and `sn-35/35-232.md:662`. The second sits under a duplicate of the preceding translation. — **re-check: adjust: delete the leaked example header and separator at `nidana-samyutta-sn-12.md:371–372` and `sn-35/35-232.md:662–663`. The duplicate translation claimed for 35-232 is not visible at 640–663. (7)**
6. **Raw `<br>` appears 71 times in table cells**, which the project's clean-Markdown rule forbids. The files with most are MN 107 (16), `35-247` (9) and `22-26` (6). — **re-check: undecided — owner decision: `<br>` in table cells (recurring owner item); count not re-checked**
7. **Link label and target disagree:** `maggasamyutta-samyutta-sn-45.md:11` says "SN45.49" but points to the heading "SN45.56". — **re-check: adjust: `maggasamyutta-samyutta-sn-45.md:11`: change `[SN45.49 kalyāṇamittasutta]` to `[SN45.56 kalyāṇamittasutta]` to match the heading. If the section text is really SN 45.49, rename the heading and anchor instead; check against the sutta text. DPD silent: kalyāṇamittasutta (no sutta number to settle it) (6)**
8. **The instruction paragraph** ("Please make line by line translation…") plus an example table is published in nine files: the three index files, the five combined files and MN 107. Seven say "in the last column", two "on the last column". — **re-check: undecided — owner decision: keep or remove the published instruction paragraph and example (data-preservation rule), and pick "in" or "on the last column"**
9. **Pāli passages are hard-wrapped in mid-sentence** in most SN 35 files and ten SN 56 files (worst: `35-247`, `35-241`, `35-232`, `35-246`). The other files keep one paragraph per line. — **re-check: undecided — owner decision: rejoin hard-wrapped Pāḷi lines (they do not change rendering); files not re-checked**
10. **One Pāli passage is split over several tables** without repeating the Pāli: MN 107 (the opening passage over five tables, and five more places) and `56-1` (twice). — **re-check: undecided — owner decision: repeat the Pāḷi passage above each split table or merge the tables**
11. **MN 107 lines 1081–1095:** two compound-member rows (`\#vitakkā (ca)`, `\#vicārā \*ca)`) stand outside the table as loose lines. — **re-check: adjust: `mn-107…md:1090–1096`: replace the loose lines and the second header with the rows `| \#vitakkā (ca) | | | | |` and `| \#vicārā (ca) | | | | |` straight after `:1089`, so the two tables join (also fixes `\*ca)` to `(ca)`) (8)**

### Convention drift

- **Sandhi:** MN 107 uses a `sandhi` row plus `#` sub-rows; the SN files mix inline `rūpasmim+api`, `sandhi` rows, and POS such as `noun+ind`, `pron+verb`. `etadavoca` is tagged three different ways (`pron+verb`, `sandhi` with `ind+aor.3rd.sg`, `sandhi` with `pron+aor.3rd.sg`); `etad` is a pronoun, so the `ind+` variants are also wrong. — **re-check: adjust: wherever `etadavoca` is a `sandhi` row tagged `ind+aor.3rd.sg`, change it to `pron+aor.3rd.sg` (DPD: etad pron; etadavoca "aor, comp vb", etad + avoca). Rows not located. The sandhi notation drift is an owner decision. (7)**
- **Compound members:** decorated inconsistently as `(ca)`, `+ke`, `(in comps)`, `<br>(ca)`, or a trailing `-`. — **re-check: undecided**
- **Multi-word cells:** `na madāya`, `bhavaṃ gotamo`, `ehi tvaṃ`; punctuation left in the Pāli cell (`vineti —`, `saṃvasati”`, `dasakā’ti`). — **re-check: undecided**
- **Headings:** `SN 43.1` against `SN46.1`; title case is mixed (`Aniccasutta` / `tatiyāssādasutta`); "Bojjhaṅgasaṃyutta Saṃyutta" and "Maggasaṃyutta Saṃyutta" are redundant; `56-28` lacks the `---` after the full text. — **re-check: undecided — owner decision: heading style (`SN 43.1`/`SN46.1`, title case). Plain fixes: `# Maggasaṃyutta Saṃyutta` → `# Maggasaṃyutta` (same for Bojjhaṅga), and add `---` after the full text in 56-28.**
- **Quotes:** curly quotes and apostrophes appear in MN 107, the SN 12, 43, 45 and 46 files and 15 of the 18 SN 56 files, and nowhere else. — **re-check: undecided**
- **Capitals:** 15 of the 18 SN 56 files capitalise the first word of each Pāli sentence, and the capital is carried into the table (`Appamattakāni`, `Āditte`, `Kiṃ`). All other files are lower case. — **re-check: undecided**
- **Stray characters:** 80 construction cells have an unbalanced `[` or `]`; there are escaped backticks (``opt.3rd.sg\` `` at `22-95:356`, `:360`, `22-82:58`), bold inside a cell (`aññathābhāv**ino**`), and a capital inside a word (`nibbindatI`, `22-59:397`, `:399`). — **re-check: adjust: `22-95:356`, `:360` `opt.3rd.sg\`` → `opt.3rd.sg`; `22-82:58` `pr.3rd.sg\`` → `pr.3rd.sg`; the `nibbindatI` → `nibbindati` fix is covered by the † typo item (`rūpasssa`, `##rajā`, `viharāti`, `nibbindatI`) — implement it there only. The bold `aññathābhāv**ino**` was not found by the excerpt check. The count of 80 brackets was not re-checked. (7)**

### Label vocabulary

- **POS has 66 distinct values.**
  - Typos: `veerb`, `insd`, `nou`, `prom`, `pron.`, `ind.`, `adj (app)`, `inf` for `ind` (`sace`, `22-82:133`). — **re-check: adjust: `22-82:133` `| sace | inf |` → `| sace | ind |` (DPD: sace ind). `veerb`/`insd`/`nou`/`prom`/`adj (app)` have no location and were not found. (7)**
  - Gender used as POS: `masc` (`35-28:268`), `nt` (6 times in `56-44`). — **re-check: adjust: `35-28:268` `| \#attano | masc |` → `| \#attano | noun |` (DPD: masc, gen sg of atta). The six `nt` POS cells in `56-44` are not located. (8)**
  - Synonyms: `ptp` / `fpp` / `adj (ptp)`; `pp (adj)` / `pp/adj` / `pp(adj)` / `adj (pp)` / `(pp as) adj`. — **re-check: undecided**
  - Nine rows have no POS. — **re-check: undecided — the nine rows are not located; each POS must be read from DPD; count not re-checked**
- **Grammar has about 300 distinct values.**
  - Typos: `masc.nomsg` (18), `masc.acc.g` (9), `masc.voc,sg` (6), `masc.genb.sg` (4), `nt.acc.ag` (2), `nt.inst.sg` (2), `fen.gen.sg`, `nt.no.sg`, `masc.nomm.sg`, `masc.nom.pl.medium`. — **re-check: adjust: `masc.nomsg`→`masc.nom.sg`, `masc.acc.g`→`masc.acc.sg`, `masc.voc,sg`→`masc.voc.sg`, `masc.genb.sg`→`masc.gen.sg`, `nt.acc.ag`→`nt.acc.sg`, `nt.inst.sg`→`nt.instr.sg`, `fen.gen.sg`→`fem.gen.sg`, `nt.no.sg`→`nt.nom.sg`, `masc.nomm.sg`→`masc.nom.sg`. `masc.nom.pl.medium` stays undecided. Count not re-checked. (6)**
  - Impossible tags: `masc.fem.sg`, `masc.fem.nom`, `nt.masc.pl`, `fem.nom.acc`. — **re-check: undecided — each row's case and gender must be read from its passage. The located instances are handled at 134 and 147; the rest are not located.**
  - Variants: `abs` / `abs.` / `ger` / `ger/abs` / `abs/ger`; `reflex` / `reflx`; `loc abs` / `loc. abs` / `loc.abs`; `quotation mark` / `quotation` / `quote`. — **re-check: undecided**
- **Compound types mix Pāli and English.**
  - `chaṭṭhī tappurisa` (155) sits beside `genitive tappurisa`, `accusative`, `locative`, `instrumental`, `dative`, `ablative tappurisa?`. — **re-check: undecided**
  - Misspellings: `chaṭṭa`, `chaṭṭha`, `chatti`, `dutiya`, `sattāni tappurisa (?)`, `kammādhāraya`, `avyayībhāva`. — **re-check: adjust: `chaṭṭa`/`chaṭṭha`/`chatti` → `chaṭṭhī`; `dutiya` → `dutiyā`; `sattāni tappurisa (?)` → `sattamī tappurisa`; `kammādhāraya` → `kammadhāraya` (DPD labels). Drop `avyayībhāva`: DPD headword spelling. (7)**
  - The bahubbīhi notation has seven spellings (`kammadhāraya\> bahubbīhi`, `kammadhāraya \> bahubbīhi`, `kammadhāraya\>bahubbīhi`, `kammadhāraya \>bahubbīhi`, `kammadhāraya\><br>bahubbīhi`, `kammadhāraya as bahubbīhi`, plain `bahubbīhi`). — **re-check: undecided**
- **The Construction column holds three kinds of content:** root derivation, compound type, and free commentary ("*probably truncated ablative (Bodhi)", "(the entire chain is a dvanda)"). — **re-check: undecided**
- **Two derivation notations:** MN 107 uses the full DPD style (`ni√sad･1 a (sink, sit, settle)+…`); the SN files use `ni + √sad + a + na`. — **re-check: undecided**
- **178 non-present verbs carry a present-tense construction** ending in `+ ti` (100 optatives, 52 futures, 26 imperatives; e.g. `desessāmi` → `√dis + *e + ti`), while others show the real ending. — **re-check: drop: owner pattern**
- **35 rows have a truncated construction** (11 distinct: `√vad`, `[√vad`, `vi + ā + √pad`, `nī + √sar`, `saṃ + √chid`, `√caj`, `nī + √yat`, `vi + √likh`, `ud + √i`, `upa + ni + √khip`, `vi + √takk`). — **re-check: undecided — only `22-94:54` `√vad` → `vada + āmi` is settled (DPD vadāmi). DPD silent on the other ten (√pad, √sar, √chid, √caj, √yat, √likh, √i, √khip, √takk); rows not located; count not re-checked.**
- **Prefix dropped from the construction** in MN 107: `āhāreyyāsi` (`:548`), `paripūreti` (`:1060`), `parisodhehi` (`:643`), `parisodheti` (`:909`), `paṭipucchissāmi` (`:1405`). — **re-check: adjust: MN107 `:548` `√har･1` → `ā√har･1`; `:1060` `√pūr･1` → `pari√pūr･1`; `:643`, `:909` `√sudh･3` → `pari√sudh･3`; `:1405` `√pucch･1` → `paṭi√pucch･1`. This follows the file's own `pari√sand･1` at `:1059`; DPD paripūreti `pari + pūre + ti`, parisodheti `pari + sodhe + ti`. DPD silent: āhāreyyāsi, paṭipucchissāmi (7)**

## Grammatical findings

### Definite errors

Rows marked † were added in the second pass.

**Verbs: person, number, voice**

| Location | Row | Problem | Re-check |
|---|---|---| --- |
| `22-94:54` (10 rows) | `vadāmi` pr.3rd.sg | 1st.sg | keep (6) — DPD: vadāmi pr 1st sg; count (10 rows) not re-checked |
| `35-118:100` (3 rows) | `santi` pr.3rd.sg | 3rd.pl | keep (6) — DPD: santi pr 3rd pl; count (3 rows) not re-checked |
| `35-230:136` | `abhinandati` pr.3rd.pl | 3rd.sg | keep (9) |
| `22-63:62` | `vihareyyāmi` opt.reflex.1st.sg | active; and the text reads `vihareyyaṃ` (see table-against-text) | adjust: `22-63:62` `\| \| vihareyyāmi \| verb \| opt.reflex.1st.sg \|` → `\| \| vihareyyaṃ \| verb \| opt.1st.sg \|` (the text reads `vihareyyanti`). DPD silent: vihareyyaṃ (DPD viharati 1 confirms the verb only) (6) |
| `56-33:61` | `gacchanti` construction `√gam + a + nta` | `+ nti` | adjust: `56-33:61` `√gam + a + nta` → `√gam + a + ti` (DPD gacchati: pr, `gaccha + ti`). The column writes plural verbs with the lemma's `ti` (`22-18:87` bhavissanti `√bhū + a + issa + ti`), so `+ nti` would add drift. (8) |

**Wrong POS**

| Location | Row | Problem | Re-check |
|---|---|---| --- |
| `22-12:74` (4 rows) | `karaṇīyaṃ` POS `prp` | ptp | keep (6) — POS `prp` → `ptp` (DPD karaṇīya 2: ptp of karoti, `√kar + aṇīya`); count (4 rows) not re-checked |
| `35-118:234–235` | `anabhinandato`, `anabhivadato` POS `pp` | prp (the construction itself ends in `nta`) | keep (7) — DPD silent: anabhinandato, anabhivadato |
| `56-47:65` | `ummujjanto` POS `pp` | prp | keep (7) — DPD silent: ummujjanto |
| `22-26:23` | `anabhisambuddhassa` POS `noun` | pp | keep (7) — DPD silent: anabhisambuddhassa |
| `22-58:188` | `akkhātā` pp, `ā + √khā + ta` | agent noun (akkhātar), not a pp | adjust: `22-58:188` `\| akkhātā \| pp \|` → `\| akkhātā \| noun \|` and construction `ā + √khā + ta` → `ā + √khā + tar` (DPD akkhātar: masc, agent, from akkhāti) (9) |
| `35-28:268` | `attano` POS `masc` | pron/noun | drop: duplicate of 69 |
| `35-241:645` | `atthāya` POS `adj` | noun | keep (9) — DPD: atthāya masc dat sg |
| `22-12:29` | `evaṃ` ind, grammar `adj` | adv | keep (9) — DPD: evaṃ ind, adv |
| † `mn107:1006` | `so` POS `ind` | pron masc.nom.sg | keep (8) — `mn107:1006` `\| so \| ind \| \|` → `\| so \| pron \| masc.nom.sg \|` (DPD so 1.1: pron, masc nom sg of ta; the English column already says "he"; the translation says "Thus") |
| † `22-78:37` | `samantā` adj/ind, fem.acc.pl | indeclinable; no case tag | adjust: `22-78:37` `\| samantā \| adj/ind \| fem.acc.pl \|` → `\| samantā \| ind \| adv \|` (DPD: ind, adv) (9) |
| † `22-59:347` | `bahiddhā` adj nt.nom.sg | indeclinable | adjust: `22-59:347` `\| bahiddhā \| adj \| nt.nom.sg \|` → `\| bahiddhā \| ind \| adv \|` (DPD: ind, adv) (9) |
| † `mn107:321` | `sīlavā` POS `noun` | adj (as at `mn107:355`) | keep (7) — DPD silent: sīlavā |

**Wrong case or number**

| Location | Row | Problem | Re-check |
|---|---|---| --- |
| `22-82:505, 511, 517` | `saññā-/saṅkhāra-/viññāṇakkhandhassa` masc.nom.sg | gen/dat | adjust: `22-82:505`, `:511`, `:517` `masc.nom.sg` → `masc.gen.sg` (genitive governed by `paññāpanāya`; the English says "of the …") (8) |
| `35-118:237` | `tiṭṭhato` masc.nom.sg | dat/gen | adjust: `35-118:237` `masc.nom.sg` → `masc.dat.sg` (as `anabhinandato` and `anabhivadato` at :234–235) (8) |
| `35-28:50` | `bhikkhū` masc.acc.sg | acc.pl | keep (7) — DPD silent: bhikkhū |
| `mn107:191`, `:195` | `dve` masc.acc.sg; `cattāri` nt.nom.sg | plural | adjust: `mn107:191` `\| dve \| card \| masc.acc.sg \|` → `\| dve \| card \| x.nom.pl \|`; `:195` `\| cattāri \| card \| nt.nom.sg \|` → `nt.nom.pl` (DPD: dve x pl; cattāri nt nom pl) (8) |
| † `mn107:193` | `tīṇi` nt.nom.sg | plural | adjust: `mn107:193` `\| tīṇi \| card \| nt.nom.sg \|` → `nt.nom.pl` (DPD: nt nom & acc pl) (9) |
| `mn107:993`, `:994` | `kusalesu`, `dhammesu` loc.sg | loc.pl | keep (7) — DPD silent: kusalesu |
| `mn107:1170` | `atthaṅgamā` instr.sg | abl.sg | keep (9) — DPD atthaṅgama is masc (a-stem), so `atthaṅgamā` is abl.sg, not instr.sg |
| † `mn107:1172` | `#gamā` instr.sg | abl.sg | keep (8) — DPD atthaṅgama masc, `atthaṃ + gama` |
| † `mn107:1097` | `vūpasamā` masc.instr.sg | abl.sg ("vitakkavicārānaṃ vūpasamā") | keep (9) — DPD vūpasama masc (a-stem), so `vūpasamā` is abl.sg |
| `35-246:154` | `me` 1st.acc.sg | dat ("for me") | keep (8) — `35-246:154` `1st.acc.sg` → `1st.dat.sg` |
| `22-82:65` | `##mātuyā` fem.loc.sg | gen | keep (8) — `22-82:65` `fem.loc.sg` → `fem.gen.sg` (parent row :63 is a gen chaṭṭhī member) |
| `22-23:65`, `:67` | `pariññeyyā` masc.nom.sg; `katamā` masc.fem.sg | first is nom.pl; second fem.nom.sg | keep (7) — `pariññeyyā` → `masc.nom.pl`; `katamā` → `fem.nom.sg`. DPD silent: katamā |
| † `22-26:47` | `saññāya` fem.nom.sg | gen.sg | keep (9) — DPD: saññā fem; `fem.nom.sg` → `fem.gen.sg` |
| † `22-58:185` | `sañjanetā` masc.gen.sg | nom.sg (agent noun, like `uppādetā` at `:182`) | keep (9) |
| † `22-59:398` | `viññāṇasmim+api` nt.nom.sg | loc.sg | keep (9) |
| † `22-78:299` | `tathāgato` masc.nom.pl | nom.sg | keep (9) |
| † `22-33:96` | `#paccayaṃ` masc.nom.sg | acc.sg | keep (8) |
| † `22-102:115` | `#tārakāya` fem.gen.pl | gen.sg | keep (9) |
| † `22-18:86` | `niccā` nt.nom.sg | masc.nom.pl (agrees with `saṅkhārā`) | keep (9) |
| † `22-95:76, 79, 82` | `rittakaṃ`, `tucchakaṃ`, `asārakaṃ` masc.nom.sg | nt.nom.sg | adjust: `22-95:79` `\| tucchakaṃ \| adj \| masc.nom.sg \|` → `\| tucchakaṃ \| ind \| adv \|`, and the same for every other `tucchakaṃ` row in 22-95 (`:127` … `:531`, e.g. `:392`, `:487`) (DPD tucchakaṃ: ind, adv, acc sg of tucchaka). `:76` rittakaṃ and `:82` asārakaṃ `masc.nom.sg` → `nt.nom.sg`; DPD silent: rittakaṃ, asārakaṃ (6) |
| † `35-93:101` | `aniccaṃ` masc.nom.sg | form and tag disagree | adjust: `35-93:101` `\| \| aniccaṃ \| adj \| masc.nom.sg \|` → `\| \| anicco \| adj \| masc.nom.sg \|` (the text after `paccayo` reads `anicco`) (8) |
| † `35-118:245`, `:247` | `tadupādānaṃ`, `#upādānaṃ` masc.nom.sg | nt.nom.sg (as at `:135`, `:137`) | keep (9) |
| † `35-136:67` | `phoṭṭhabbārāmā` masc.loc.pl | nom.pl | keep (9) |
| † `56-13:133` | `#kāmesu` masc.loc.sg | loc.pl | keep (9) |
| † `56-13:126` | `tatratatrābhinandinī` masc.fem.sg | fem.nom.sg | keep (9) |
| † `56-31:142–147` | `#saṃhitaṃ`, `nādibrahmacariya+kaṃ` and its two members, masc.nom.pl | nt.nom.sg | keep (8) — rows 142, 143, 145 and 147 → `nt.nom.sg`, agreeing with `etaṃ`/`atthasaṃhitaṃ` (:140) |
| † `56-42:243` | `jātisaṃvattanike+pi` masc.loc.pl | acc.pl (agrees with `saṅkhāre`, tagged acc.pl in the next row) | keep (9) |
| † `56-49:56` | `#pabbatarājā` masc.gen.pl | nom.sg | keep (9) |
| † `mn107:748` | `saṅghāṭipattacīvaradhāraṇe` nt.nom.sg | loc.sg | keep (9) |
| † `mn107:1089` | `vitakkavicārānaṃ` masc.acc.sg | gen.pl | keep (9) |
| † `mn107:1167` | `somanassadomanassānaṃ` nt.acc.sg | gen.pl | keep (9) |
| † `mn107:1875` | `anuyuttā` masc.nom.sg | nom.pl | keep (9) |
| † `mn107:1922`, `:1933`, `:1942` | `mūlagandhā`, `sāragandhā` masc.nom.sg; `pupphagandhā` masc.abl.sg | all nom.pl ("ye keci …gandhā") | keep (9) |
| † `mn107:18` | `sutaṃ` masc.acc.sg | nt.nom.sg ("evaṃ me sutaṃ") | keep (9) |

**Wrong root, prefix or suffix**

| Location | Row | Problem | Re-check |
|---|---|---| --- |
| `35-53:51` (10) | `jānato` construction `√ñā + nā + a` | `+ nta` | adjust: 35-53:51 (and the other rows behind "(10)") `√ñā + nā + a` → `√ñā + nā + nta + to` (as `passato` at :53); count not re-checked (7) |
| `22-78:262`, `22-26:27`, `35-230:163` | `samānā`, `sato`, `santi` with `sa + √as` | no `sa` prefix | adjust: in DPD `sa` is the form √as takes, not a prefix. 22-26:27 `sa + √as + a + nta` → `sa + nta + to` (DPD sato); 35-230:163 `sa + √as + a + nti` → `sa + nti` (DPD santi 2.1); 22-78:262 `sa + √as + a + māna` → `sa + māna` (DPD samāna 2.1, prp of atthi, √as) (8) |
| † `mn107:953` | `sato` "mindful" with `sa√as … (be)` | √sar + ta (as at `mn107:679`) | keep (9) — DPD sata 1.1: pp of sarati, `√sar + ta`, "mindful" |
| † `22-63:76`, `35-28:282` | `anupādiyamāno`, `anupādāya` with `√ādā` | `ā + √dā` | drop: DPD anupādāya has root √ādā and construction `na > an + upa + √ādā + ya`, so the source matches DPD |
| † `22-78:117` | `baddhā` with `√badh` | √bandh | drop: DPD baddha 1 is `√badh + ta` (root √badh), so 22-78:117 matches DPD |
| † `mn107:944` | `#thīna` with `√thī + ana` | `+ na` | drop: DPD thīna is `√thī + ana`, so the source matches DPD (the cell only has a stray trailing `+`) |

### Reclassified: not a definite error

- `labheyyaṃ` (`35-241:532`, 4 rows) and `puccheyyaṃ` (`22-82:127`) tagged reflexive. The first version called these "ordinary active optatives". In traditional grammar `-eyyaṃ` is the attanopada (reflexive) 1st.sg optative ending and `-eyyāmi` the active one, so the tag is defensible. Modern grammars list `-eyyaṃ` as active. Decide one convention in the schema and apply it; the gloss "I would obtain myself" should go either way. — **re-check: undecided — owner decision: one label for the -eyyaṃ 1st.sg optative (reflexive or active), then the gloss; also `opt.reflx.` vs `opt. reflex.` notation**

### Wrong gender

- **Neuter tagged masc:**
  - MN 107: `cittaṃ` (`:642`); `cakkhundriyaṃ` and `manindriyaṃ` (`:418, 439, 440, 490, 511, 512`); `rūpaṃ` (`:396`); `ghānena` (`:454`); † `sotena` (`:451`); † `phoṭṭhabbaṃ` (`:461`); † `bhojane` (`:608`); † `satisampajaññena` (`:804`); † `#vanānaṃ` (`:1558`); † `#jaṃ` (`:1037`, `:1108`); † `#karaṇīyaṃ` (`:1231`); `kāraṇaṃ` (`:288, 292`); † `avitakkaṃ`, `avicāraṃ`, `samādhijaṃ` (`:1104–1106`). — **re-check: keep (8) — DPD gives nt for cakkhundriya, manindriya, rūpa, ghāna, sota 2.1, phoṭṭhabba, bhojana, satisampajañña, vana, karaṇīya, kāraṇa. DPD silent: citta, ja, avitakka, avicāra, samādhija**
  - SN files: `rūpesu` (`35-70:90`); † `rūpasmim+api` (`22-59:390`, `22-95:554`); † `#rūpe` (`22-102:34`); † `#phoṭṭhabbesu` (`35-136:68`); † `#kulānaṃ` (`22-63:243`); † `#kiṃ` (`56-1:36`). — **re-check: keep (9) — DPD rūpa, phoṭṭhabba, kula nt; kiṃ 1 pron nt**
- **Masc tagged nt:** `pāde` (`mn107:676`); † `pādaṃ` (`mn107:677`); `attena` (`35-85:50`); † `anuggahāya` (`mn107:576`); † `dhamme` (`35-247:537`). — **re-check: keep (7) — DPD pāda 1 masc; anuggaha 2.1 masc ("support; help"). DPD silent: attena, dhamme**
- **Fem tagged otherwise:** `gīvaṃ` nt (`56-47:69`); `appaṭivānī` masc (`56-34:64`); `dukkhanirodhagāminī` masc (`56-1:122`, but fem at `56-1:65`); † `sassamaṇabrāhmaṇiyā` masc (`22-26:202`); † `paññāpanā`, `paṭṭhapanā`, `vivaraṇā`, `vibhajanā` nt (`56-38:160–163`; `ācikkhaṇā` at `:157` is fem); † `paññāpanāya` nt (`22-82:494`). — **re-check: adjust: 56-47:69 `nt.acc.sg` → `fem.acc.sg` (DPD gīvā fem); 56-1:122 `masc.nom.sg` → `fem.nom.sg`; 22-26:202 `masc.loc.sg` → `fem.loc.sg`; 56-38:160–163 `nt.nom.sg` → `fem.nom.sg` (DPD paññāpanā, paṭṭhapanā, vivaraṇā, vibhajanā fem). Remove `appaṭivānī` (DPD: masc, as the source has it) and `paññāpanāya` (DPD: nt, dat sg of paññāpana) from the finding (8)**
- **Self-contradicting:** `cittāni` tagged `nt.masc.pl` (`35-28:284`). — **re-check: adjust: 35-28:284 `nt.masc.pl` → `nt.nom.pl` (subject of vimucciṃsu) (9)**
- **Split within one file:** `jāgariyaṃ` fem and nt, `bhojane` nt and masc, `satisampajaññena` nt and masc (all MN 107); `kulānaṃ` nt and masc across files. — **re-check: adjust: mn107:627 `| jāgariyaṃ | noun | fem.acc.sg |` → `nt.acc.sg` (DPD jāgariya nt; :717 and :1874 already nt). bhojane, satisampajaññena and kulānaṃ repeat 176/177 (DPD bhojana, satisampajañña, kula nt) (8)**

### Wrong or doubtful compound analysis

- `khīṇāsavā`, `katakaraṇīyā` given as "dutiyā tappurisa" (`mn107:1225, 1229`): these are bahubbīhi. — **re-check: adjust: mn107:1225 `dutiyā tappurisa` → `kammadhāraya as bahubbīhi` (DPD khīṇāsava: kammadhāraya > bahubbīhi); :1229 `dutiyā tappurisa` → `dutiyā tappurisa as bahubbīhi` (DPD katakaraṇīya: dutiyā tappurisa > bahubbīhi; cf. :1232) (9)**
- `attamanā` given as "chaṭṭhī tappurisa" (`35-28:267`): bahubbīhi. — **re-check: drop: DPD attamana is adj, chaṭṭhī tappurisa (attano + mana), so 35-28:267 matches DPD**
- `bhikkhusahassena` given as "digu" (`35-28:45`, and `bhikkhusahassassa` at `:281`): chaṭṭhī tappurisa. `chappāṇake` given as "kammadhāraya" (`35-247:293`): this one is the digu. — **re-check: adjust: keep 35-28:45 and :281 `digu` (DPD bhikkhusahassa: nt, digu bhikkhū + sahassa); 35-247:293 `chappāṇake` `kammadhāraya` → `digu`. DPD silent: chappāṇaka (6)**
- `dhammamayo` given as "instrumental tappurisa" (`35-228:104`, `:110`): `-maya` is a suffix, not a compound member. — **re-check: drop: DPD lists maya as "adj, in comps" (a compound member), so treating it as a member matches DPD. `instrumental tappurisa` vs `tatiyā tappurisa` wording is a convention question**
- `pātimokkhasaṃvarasaṃvuto` given as "sattamī tappurisa" (`mn107:323`): tatiyā. — **re-check: adjust: mn107:323 `sattamī tappurisa` → `tatiyā tappurisa`; :324 `#pātimokkhe | noun | masc.loc.sg` → `#pātimokkhasaṃvarena | noun | masc.instr.sg`; :325 → `#saṃvuto | pp | masc.nom.sg` (DPD pātimokkhasaṃvarasaṃvuta: tatiyā tappurisa pātimokkhasaṃvarena + saṃvuta) (9)**
- † `piṇḍapātapaṭikkanto` given as "dutiyā tappurisa" (`mn107:875`): pañcamī ("returned from alms round"). — **re-check: adjust: mn107:875 `dutiyā tappurisa` → `pañcamī tappurisa`; :876 `#piṇḍapātaṃ | noun | masc.acc.sg` → `#piṇḍapātasmā | noun | masc.abl.sg` (DPD piṇḍapātapaṭikkanta: pañcamī tappurisa piṇḍapātasmā + paṭikkanta; -asmā as the file's :1036, :1203) (9)**
- † `savitakkaṃ`, `savicāraṃ` given as "kammadhāraya" (`mn107:1029, 1032`): bahubbīhi. — **re-check: adjust: DPD gives savitakka and savicāra as "adj, from vitakka/vicāra" with no compound type, so neither kammadhāraya nor bahubbīhi: mn107:1029 `kammadhāraya` → `sa + vi + √takk + a`; :1032 `kammadhāraya` → `sa + vi + cāre + a` (6)**
- † `pacchāmukho` given as "abyayībhāva" (`mn107:1583`): a declined adjective, so bahubbīhi (as at `mn107:1656`). `parimukhaṃ` given as "kammadhāraya" (`mn107:886`): this one is the abyayībhāva. — **re-check: adjust: mn107:1583 `abyayībhāva` → `kammadhāraya as bahubbīhi` (DPD pacchāmukha: kammadhāraya > bahubbīhi; as :1656, where `kammādhāraya` is a typo); :886 `kammadhāraya` → `pari + mukha + aṃ` (DPD parimukhaṃ: ind, adv, acc sg of parimukha, no compound type) (7)**
- † Adjectives of persons given as plain "kammadhāraya" where sibling rows use "kammadhāraya > bahubbīhi": `mahiddhiko` (`22-78:134`), `sukhabahulā` (`22-78:231`), `muṭṭhassatino` (`mn107:1819`), `duppaññā` (`mn107:1827`), `pakkagatto` (`35-247:99`), `arugatto` (`35-247:96`), `evaṃsamācāro` (`35-247:164`), `acakkhukaṃ` (`22-94:311`), `vigatavalāhake` (`22-102:150`). — **re-check: adjust: only 22-78:231 `sukhabahulā` `kammadhāraya` → `kammadhāraya > bahubbīhi` (DPD sukhabahula). DPD gives plain kammadhāraya for mahiddhika, duppañña, evaṃsamācāra, acakkhuka, vigatavalāhaka, so those rows match DPD. DPD silent: muṭṭhassati, arugatta, pakkagatta (7)**
- † `anuppattasadatthā` "dutiyā tappurisa" and `apattamānasā` "kammadhāraya" (`mn107:1235, 1198`): both bahubbīhi. — **re-check: adjust: mn107:1235 `dutiyā tappurisa` → `dutiyā tappurisa as bahubbīhi` (DPD anuppattasadattha); :1198 `kammadhāraya` → `kammadhāraya as bahubbīhi` (DPD apattamānasa: kammadhāraya > bahubbīhi) (9)**
- † `sīsapāvane` "kammadhāraya" (`56-31:30`): chaṭṭhī tappurisa ("grove of sīsapā trees"). — **re-check: keep (9) — DPD sīsapāvana: chaṭṭhī tappurisa**
- The same compound is labelled differently: `dukkhanirodhaṃ` (chaṭṭhī tappurisa at `56-1:66` / "kammadhāraya > bahubbīhi" with POS noun at `56-13:42`), `andhakāratimisā` (kammadhāraya fem.sg at `56-38:46` / dvanda nt.pl at `56-38:104`), `mahiddhiko` / `mahesakkho` (`22-78:134`, `:144`). — **re-check: adjust: 56-13:42 `kammadhāraya \> bahubbīhi` → `chaṭṭhī tappurisa` (as 56-1:66); 56-38:104 `nt.nom.pl` … `dvanda` → `fem.nom.sg` … `kammadhāraya`, and drop ` (ca)` at :105 (DPD: fem, kammadhāraya andhakāra + timisa); for mahiddhiko see 193 (8)**

### Other doubtful rows (lower certainty, worth a second look)

- `bhūmirāmaṇeyyakaṃ` adj masc.acc.sg (`mn107:1560`), and the sister compounds at `mn107:1556–1566`: these look like neuter nouns. — **re-check: adjust: mn107:1554–1566 set every `…rāmaṇeyyakaṃ` row to POS `noun`, grammar `nt.acc.sg` (1554 has no grammar; the others are masc.acc.sg, with adj/noun mixed) (DPD rāmaṇeyyaka 2: nt, "delightfulness; loveliness") (8)**
- `khemaṃ` noun masc.acc.sg (`mn107:1204`). — **re-check: drop: DPD yogakkhema is masc and khema 2 is masc ("safety"), so mn107:1202 and :1204 `masc.acc.sg` match DPD**
- `saṃhitaṃ`: see definite errors. — **re-check: drop: duplicate of 148**
- `vutte` masc.loc.sg (`mn107:1273`) against nt.loc.sg (`35-241:246`). — **re-check: adjust: mn107:1273 `masc.loc.sg (loc abs)` → `nt.loc.sg (loc abs)` (as 35-241:246). DPD silent: vutte / evaṃ vutte (DPD vutta 2.1 gives pp only, no gender) (7)**
- `doṇiṃ` tagged `fem.nom.acc` (`35-246:243`): fem.acc.sg. — **re-check: keep (9)**
- `nibbānaninnā` tagged `masc.fem.nom` (`35-241:230`). — **re-check: adjust: 35-241:230 `masc.fem.nom` → `fem.nom.sg` (agrees with sammādiṭṭhi) (8)**
- `#gayāyaṃ` as a member of `gayāsīse` tagged fem.gen.sg (`35-28:42`): the form is locative; the genitive member would be `gayāya`. — **re-check: keep (8)**
- `me` 1st.instr.sg glossed "to me" (`mn107:17`): gloss does not match the tag ("by me"). — **re-check: keep (8)**
- `aññamañña` labelled "dutiyā tappurisa" (`56-47:159`). — **re-check: drop: DPD aññamañña is dutiyā tappurisa (aññaṃ + añña), so the source matches DPD**
- `āvuso` POS ind with grammar `masc.voc.sg` (`35-232:97`). — **re-check: adjust: 35-232:97 grammar `masc.voc.sg` → `voc.sg` (DPD: ind, voc sg & pl) (6)**
- † `daḷhāya` pp with `√dah + ta` (`35-247:303`): `daḷha` is normally an adjective, and √dah is "burn". — **re-check: drop: DPD daḷha 1 is the pp of √dah (`√dah + ta > daḍha > daḷha`, "strong"), so the source matches DPD**
- † `thullaphusitake` noun nt.loc.sg (`22-95:150`): agrees with `deve`, so masc and adjectival. — **re-check: adjust: 22-95:150 `noun | nt.loc.sg (loc abs)` → `adj | masc.loc.sg (loc abs)` (DPD thullaphusitaka 2: adj, kammadhāraya > bahubbīhi, "with big fat droplets") (9)**
- † `āmisacakkhu` nt.nom.sg (`35-230:45`): qualifies `maccho`. — **re-check: adjust: 35-230:45 `nt.nom.sg` → `masc.nom.sg` (DPD: adj; qualifies maccho) (8)**
- † `Āditte` masc.loc.sg (`56-34:25`): with `cele vā sīse vā`, nt. — **re-check: adjust: 56-34:25 `masc.loc.sg` → `nt.loc.sg` (8)**
- † `saddhā` fem.instr.sg (`mn107:1775`): ablative in "saddhā agārasmā anagāriyaṃ pabbajitā". — **re-check: adjust: mn107:1775 `fem.instr.sg` → `fem.abl.sg` (parallel to `agārasmā`; translation "not because of faith"). DPD silent: saddhā as an ablative form (DPD saddhā gives fem only) (5)**
- † `sugatā` masc.nom.sg (`22-63:90`), `upadhāraṇe` nt.acc.pl (`35-246:252`), `āyaṃ` pron fem.nom.sg (`35-246:333`), `asatī` prp fem.nom.sg (`35-246:331`): form and tag disagree; check against the sentence. — **re-check: adjust: 22-63:90 `sugatā | noun | masc.nom.sg` → `sugata | noun | masc.voc.sg` (sugata + iti, parallel to bhagavā at :88; DPD sugata 2 masc); 35-246:333 `āyaṃ` → `ayaṃ` (kira + ayaṃ; fem.nom.sg stays); 35-246:331 POS `prp` → `adj` and `na + √as + a + nta` → `na > a + sa + nta + tī` (DPD asatī); 35-246:252 `upadhāraṇe` keeps `nt.acc.pl` (DPD upadhāraṇa 1 nt), gloss `headstock(s)` → `tuning cords` (DPD "(of a vīṇā) tuning cords") (7)**
- † `sārapariyesanaṃ` ind adv (`22-95:335`): object of `caramāno`, so a noun in the accusative. — **re-check: drop: DPD sārapariyesanaṃ is ind, adv, acc sg of sārapariyesana, so the source matches DPD**
- † `#mattāyo` POS pp (`56-49:33`): noun. — **re-check: keep (9) — DPD mattā: fem noun**
- † `dukā`, `tikā`, `catukkā`, `chakkā`, `aṭṭhakā`, `dasakā` nt.nom.pl (`mn107:192–208`): the `-ā` ending points to masc. — **re-check: drop: DPD duka 1 nt (2 masc), tika 2 nt, catukka 2 nt, so the nt tags match DPD; the -ā ending alone does not make them masc. chakka, aṭṭhaka, dasaka not in DPD**
- † `#sacchi` POS adj (`22-63:263`): indeclinable. — **re-check: drop: DPD sacchi is "adj, in comps", so the source matches DPD**
- † `passena` nt (`mn107:671`), `padakkhiṇaṃ` fem (`22-63:216`), `vajjesu` masc (`mn107:335`), `#pheṇa` nt (`22-95:58`), `#pubbuḷe` nt (`22-95:92`), `#saṃvaccharā` "nt (or masc.)" (`56-38:67`), `#addhānaṃ` nt.nom.sg (`56-21:53`): gender to be checked against DPD. — **re-check: adjust: remove the items DPD confirms: `#pheṇa` nt (DPD nt), `padakkhiṇaṃ` fem (DPD: acc sg of padakkhiṇā; idiom fem + abs), `#addhānaṃ` nt (DPD idiom nt + pr). mn107:671 `passena | noun | nt.instr.sg` → `ind | adv` (DPD: ind, adv, instr sg of passa); mn107:335 `vajjesu` `masc.loc.pl` → `nt.loc.pl` (DPD vajja 2.1 nt, "fault"); 56-38:67 `#saṃvaccharā (ca)` `nt.nom.pl (or masc.)` → `masc.nom.pl` (DPD saṃvacchara 2 masc; -ā plural, dvanda head masc.nom.pl at :65). #pubbuḷe (22-95:92) goes under 236 (7)**
- † `kiccakaraṇīyesu` "kammadhāraya" (`35-241:357`): probably dvanda. `giriguhaṃ` (`mn107:831`), `gijjhakūṭe` (`35-118:29`), `chandarāgavemattatā` (`22-82:342`) "kammadhāraya": probably chaṭṭhī tappurisa. — **re-check: adjust: 22-82:342 `kammadhāraya` → `pañcamī tappurisa` (DPD: chandarāgehi + vemattatā). Drop the rest: DPD kiccakaraṇīya, giriguhā and gijjhakūṭa are kammadhāraya, so 35-241:357, mn107:831 and 35-118:29 match DPD (9)**

### Pāli typos

**In the word column**

- `kukkurao` (`35-247:381`), `imina` (`35-241:390`), `ko nu kno` (`22-26:37`), `pajānati` (`56-49:157`, 4 rows), `viññāṇasmim` without `pi` (`22-12:44`), `itthattāyā` (`22-12:76`). — **re-check: adjust: 35-247:381 `kukkurao` → `kukkuro`; 35-241:390 `imina` → `iminā`; 22-26:37 `ko nu kno` → `ko nu kho`; 56-49:157 (+3 rows, count not re-checked) `pajānati` → `pajānāti`; 22-12:44 `viññāṇasmim` → `viññāṇasmim+api` (passage :25 has viññāṇasmimpi); 22-12:76 `itthattāyā` → `itthattāya` (8)**
- `bhagavā` tagged instr.sg (`56-31:86`): the passage has `bhagavatā`. — **re-check: keep (9)**
- † `rūpasssa` (`22-26:121`), `##rajā` (`56-49:58`), `viharāti` (`mn107:362`), `nibbindatI` (`22-59:397`, `:399`), `dukkhanirodhagāminim` (`56-44:39`, 4 rows). — **re-check: adjust: 22-26:121 `rūpasssa` → `rūpassa`; 56-49:58 `##rajā` → `##rājā`; mn107:362 `viharāti` → `viharati`; 22-59:391, :395, :397, :399 `nibbindatI` → `nibbindati`; 56-44:39 (+3 rows) `dukkhanirodhagāminim` → `dukkhanirodhagāminiṃ` (9)**
- † `thīnamiddhaṃ`, `vigatathīnamiddho` (`mn107:943–949`) against `thinamiddhaṃ` in the passage (`mn107:939`). — **re-check: undecided — owner decision: DPD's headword is `thīna`, the passage edition has `thina`; choose one spelling for both table and passage**

**In the Pāli passages**

- † `manoiññeyyā` for `manoviññeyyā` (`35-118:17`, `:199`). — **re-check: keep (9)**
- † `pajānātiti` for `pajānātīti` (`22-95:25`, `:545`). — **re-check: keep (9)**
- † `22-95:47`: the foam simile ends "kiñhi siyā, bhikkhave, udakapubbuḷe sāro"; the full text at line 5 has `pheṇapiṇḍe`. The translation follows the wrong word ("in a water bubble?"). — **re-check: adjust: 22-95:47 `udakapubbuḷe sāro` → `pheṇapiṇḍe sāro` (confirmed at line 5); rows :90–92 → `pheṇapiṇḍe | noun | masc.loc.sg | in a lump of foam | kammadhāraya` + `#pheṇa` / `#piṇḍe` (mirror :57–59); translation :95 "in a water bubble?" → "in a lump of foam?" (9)**
- † `56-5`: the full text (line 5) reads `abhisambujjhanti`; the split passages and tables (`:65`, `:79`, `:87`, `:150`, `:159`) read `abhisambojjhanti`. One spelling should be chosen after checking the source edition. — **re-check: adjust: 56-5:65, :79, :87, :150, :159 `abhisambojjhanti` → `abhisambujjhanti` (DPD abhisambujjhati, `abhi + saṃ + bujjha + ti`; the full text at line 5 and :91 already read so) (7)**
- † `22-102:199`: the passage starts mid-sentence ("rūpassa samudayo…"); the opening "kathaṃ bhāvitā ca, bhikkhave, aniccasaññā…" is missing, though the table and the translation cover it. — **re-check: adjust: the old finding was wrong, not out of date: 22-102:198 holds the full sentence from `kathaṃ bhāvitā ca` (sources unchanged since before the audit), so no opening is missing. The real defect is that :199 repeats the tail of :198; remove line :199 `rūpassa samudayo, … viññāṇassa atthaṅgamoti.` (8)**
- † `mn107:1048–1160`: the pervasion simile ("so imameva kāyaṃ vivekajena pītisukhena abhisandeti…") and three passages addressed "puna caparaṃ, bhikkhave, bhikkhu" do not look like MN 107, which is spoken to a brahmin and gives the jhāna formulas without similes. Check against the source edition; if confirmed, the text was pasted from another sutta. — **re-check: undecided — compare mn107:1048–1160 with the CST text of MN 107 to see whether the similes and "puna caparaṃ, bhikkhave" passages belong there**

### Table against text †

Places where the table does not carry the words of its passage (confirmed by eye):

- `22-82:525`: the passage has "nāmarūpaṃ hetu, nāmarūpaṃ paccayo viññāṇakkhandhassa paññāpanāya"; the table has `phasso hetu phasso paccayo`, and the translation follows the table ("Contact [is] the cause…"). — **re-check: adjust: 22-82:557, :559 `| 47646 | phasso | noun | masc.nom.sg | contact | |` → `| | nāmarūpaṃ | noun | nt.nom.sg | mind and matter | dvanda |` (DPD nāmarūpa: nt, dvanda); :565 last sentence "Contact [is] the cause, contact [is] the supporting condition … consciousness-aggregate" → "Mind-and-matter [is] the cause, mind-and-matter [is] the supporting condition …" (9)**
- `22-95:394`, `:397`, `:486–492`: the table has `khāyati` (pr) where the passage has `khāyeyya` (opt), in the plantain-trunk and magic-show similes. — **re-check: adjust: 22-95:394, :397, :486, :489, :492 `khāyati | verb | pr.pass.3rd.sg (+nom) | it appears to be` → `khāyeyya | verb | opt.pass.3rd.sg (+nom) | it would appear to be` (as :391) (9)**
- `22-63:62`: the table has `vihareyyāmi`; the passage has `vihareyyanti` (`vihareyyaṃ` + `ti`). — **re-check: adjust: 22-63:62 `vihareyyāmi` → `vihareyyaṃ` (8)**
- `22-78:19`: `nadati` is missing after `sīhanādaṃ`. — **re-check: adjust: insert after 22-78:50 `| | nadati | verb | pr.3rd.sg | roars | √nad + a + ti |` (DPD nadati 1) (9)**
- `35-230:161`: `abhedi baḷisaṃ, paribhedi baḷisaṃ` is missing from the table and from the translation. — **re-check: adjust: insert after 35-230:189 `| | abhedi | verb | aor.3rd.sg | broke; shattered | a + bhede + i |`, `| | baḷisaṃ | noun | nt.acc.sg | hook | |`, `| | paribhedi | verb | aor.3rd.sg | completely broke up; shattered | pari + bhede + i |`, `| | baḷisaṃ | noun | nt.acc.sg | hook | |` (DPD); in :203 add "has broken the hook, has shattered the hook," after "has not swallowed the bait of death" (if the re-check of 318 already renamed it, after "has not swallowed Māra's hook") (8)**
- `35-118:151`: the closing sentence "ayaṃ kho, devānaminda, hetu, ayaṃ paccayo yena-m-idhekacce sattā diṭṭheva dhamme no parinibbāyanti" is missing from the table and from the translation. — **re-check: adjust: after 35-118:195 add rows for "ayaṃ kho devānaminda hetu ayaṃ paccayo yena-m-idhekacce sattā diṭṭheva dhamme no parinibbāyanti" (copy them from the file's first table for this sentence if it exists), and append to :197 "This, lord of the gods, is the cause, this is the condition why some beings here do not attain final nibbāna in this very life." (6)**
- `56-31:134`, `:201`: `sambodhāya` is missing, the repeated `na` is dropped, and the table has `saṃvattanti` for `saṃvattati`. — **re-check: adjust: 56-31:152–156 insert `| 35345 | na | ind | neg | not | |` before each of virāgāya…nibbānāya; add `| | sambodhāya | noun | masc.dat.sg | full awakening | |` after :155 and after :218 (DPD sambodha: masc, "full awakening"); :157 and :220 `saṃvattanti | verb | pr.3rd.pl (+dat)` → `saṃvattati | verb | pr.3rd.sg (+dat)` (DPD saṃvattati pr); add "to full awakening" in :163 and :226 (8)**
- `56-31:166`: the passage includes the "Kasmā cetaṃ…" section, which is then repeated as its own passage at `:199`. — **re-check: adjust: 56-31:166 drop the trailing "Kasmā cetaṃ, bhikkhave, mayā akkhātaṃ? … tasmā taṃ mayā akkhātaṃ." It is the passage at :199, which has its own table and translation, so no text is lost (7)**
- `mn107:915`, `:941`, `:962`: `viharati` is missing from the table. — **re-check: adjust: mn107: add row `| viharati | verb | pr.3rd.sg | dwells; lives | |` after :921 (abyāpannacitto), after :949 (#thīnamiddho) and after :967 (anuddhato); DPD viharati 1 "lives; dwells" (9)**

### Systematic inconsistencies

- Passive against active: `virajjati`, `vimuccati`, `nirujjhati` are `pr.pass` in some files and `pr` in others. — **re-check: undecided — owner decision: whether the grammar column marks passive. DPD: vimuccati and nirujjhati are "pr, pass"; virajjati is "pr, from rajjati" (not passive). Locations not listed in the finding**
- Causative marking: `deseti` / `desessāmi` appear both as `pr.caus` / `fut.caus` and plain `pr` / `fut`. — **re-check: undecided — owner decision: whether the grammar column marks causative. DPD: deseti is "pr, caus of disati". Locations not listed in the finding**
- `addasā` is `imperf` once (`35-241:76`); all similar forms are `aor`. — **re-check: drop: DPD gives addasā as "imperf of √dis", so `35-241:76` imperf is correct. If anything is wrong, it is the other rows tagged `aor`**
- `ger` is used for `-ya` forms and `abs` for `-tvā` forms in most files, but `ger/abs`, `abs/ger` and `abs` on `-ya` forms (`samādāya`, `viññāya` in MN 107) also occur. — **re-check: drop: owner pattern**
- Cardinal numbers: `x.nom.pl`, `masc.x.pl`, `(in comps)` and plain gender labels are all used. — **re-check: undecided — owner decision: one label for cardinals (DPD uses "card, x pl" for dve and "nt nom pl" for cattāri)**
- Reflexive optatives: see "Reclassified" above. — **re-check: drop: only a pointer, a duplicate of audit line 171 (reflexive optatives, already undecided)**

## Translation findings †

Line numbers are the first line of the table whose bold translation is affected. Stylistic roughness and literal renderings are not listed.

### Mistranslations

| Location | Pāli | Given | Problem | Re-check |
|---|---|---|---| --- |
| `22-33:125` | taṃ kissa hetu? na hi no etaṃ, bhante, attā vā attaniyaṃ vā | "Because, Venerable Sir, the self is not what belongs to oneself." | "Why is that? Because this is not our self or what belongs to our self." | keep (8) |
| `22-59:328` | sabbaṃ viññāṇaṃ | "all form should be seen" | consciousness | keep (9) |
| `22-94:135` | viññāṇaṃ aniccaṃ dukkhaṃ | "[that is] permanent, suffering" | impermanent | keep (9) |
| `22-82:525` | nāmarūpaṃ hetu… viññāṇakkhandhassa | "Contact [is] the cause…" | name-and-form | keep (9) |
| `22-95:49` | pheṇapiṇḍe sāro | "in a water bubble?" | in a lump of foam | drop: duplicate of audit line 236. The passage at 22-95:47 still reads `udakapubbuḷe`, so the translation matches the current text; fix the passage and the translation together under 236 |
| `22-102:54` | mahānaṅgalena | "with a great soil" | plough | keep (9) |
| `22-78:256` | bho (4 times, devas to each other) | "Venerable Sir" | "sirs" / "friends" | keep (8) |
| `35-228:97` | dhammamayaṃ vegaṃ | "current made of forms" | mental objects (copied from the eye section) | keep (9) |
| `35-246:359` | evameva kho, bhikkhave | "Just as, monks" | "In the same way" (it applies the simile) | keep (8) |
| `35-247:288`, `:566` | bandheyya | "we would bind it" | he would bind | keep (9) |
| `mn107:255` | sakkā, brāhmaṇa, … paññapetuṃ | "Is it possible, Brahman, to define…" | a statement: "It is possible" | keep (8) |
| `mn107:272` | seyyathāpi, brāhmaṇa, dakkho assadammako | "Brahman, even a skilled trainer of horses" | "Just as, brahman, a skilled horse-trainer" | keep (8) |
| `mn107:520` | yato kho, brāhmaṇa, bhikkhu … hoti | "Because, brahman, as a monk is…" | "When, brahman, a monk is…" (as at `:351`, `:711`) | keep (8) |
| `mn107:869` | parimukhaṃ satiṃ upaṭṭhapetvā | "with the intention of setting up mindfulness" | absolutive: "having set up" | keep (9) |
| `mn107:1544` | dakkhissasi rājagahassa ārāmarāmaṇeyyakaṃ … | "you will see Rājagaha, pleasant as a park…" | "you will see the delightful parks, groves, grounds and ponds of Rājagaha"; "tena muhuttaṃ gantvā" is also left out | adjust: mn107:1569 "Go by that [road] for a while [and] you will see Rājagaha, pleasant as a park, delightful as a wood, a pleasant region, delightful as a lotus pond." → "Go by that [road] for a while; having gone by that [road] for a while, you will see the delightful parks, the delightful groves, the delightful grounds and the delightful lotus ponds of Rājagaha." (7) |
| `mn107:1974` | seyyathāpi, bho gotama, nikkujjitaṃ vā ukkujjeyya, … mūḷhassa vā maggaṃ ācikkheyya | "as if Master Gotama would turn upside down or turn right side up and uncover what was hidden for a deluded person…" | `bho gotama` is a vocative, not the subject; "set upright what was overturned"; `mūḷhassa` goes with "show the way" | adjust: mn107:2001 "[It is] as if Master Gotama would turn upside down or turn right side up and uncover what was hidden for a deluded person, or would show the way to someone in blindness," → "Just as, Master Gotama, one would set upright what was overturned, or uncover what was hidden, or show the way to one who is lost," (rest unchanged) (DPD mūḷha 2 "who is lost; who is disoriented") (8) |

### Words or clauses left untranslated

- `22-102:144`: `bhāsate ca tapate ca virocate ca` (the main verbs). — **re-check: adjust: 22-102:196 "having dispelled all the darkness throughout space, in the same way" → "having dispelled all the darkness throughout space, shines and glows and radiates; in the same way". DPD silent: bhāsate, tapate, virocate (7)**
- `22-63:117`, `:154`: "anupādiyamāno mutto pāpimato" for form; `:202`: `pakkāmi`, leaving the sentence unfinished. — **re-check: adjust: 22-63:150 and :198, after the first "is bound to Māra" insert "; one not clinging is freed from the Evil One"; 22-63:220, after "circumambulation to the right," add "he departed." (DPD pakkāmi "left; went away") (9)**
- `22-78:156`: `sugato`. — **re-check: adjust: 22-78:217 "endowed with knowledge and moral conduct, knower of the world" → "endowed with knowledge and moral conduct, the Fortunate One, knower of the world" (DPD sugata 2 "Accomplished One; Fortunate One"; the file glosses it "Fortunate One" at 22-63:90) (8)**
- `22-82:639`: `ariya` in "sutavā ariyasāvako". — **re-check: adjust: 22-82:698 "the learned disciple" → "the learned noble disciple" (DPD ariya 1 "noble") (9)**
- `22-94:199`, `:228`, `:323`: `vibhajati` in each list; `:288`, `:354`: `tathāgatena`. — **re-check: adjust: 22-94:224, :284 (twice), :350 "he reveals [it], [and] he elucidates [it]" → "he reveals [it], he analyses [it] in detail, [and] he elucidates [it]" (DPD vibhajati 1); :319 and :385 "thus being pointed out" → "thus being pointed out by the Tathāgata" (8)**
- `35-118:151`, `35-230:161`: see table-against-text. — **re-check: drop: only a pointer, a duplicate of audit lines 250 (35-118:151) and 249 (35-230:161)**
- `35-241:430`: `kasambujāto`. — **re-check: adjust: 35-241:474 "rotten inside, overflowing [with lust]." → "rotten inside, overflowing [with lust], filthy." (DPD kasambujāta "rotten; filthy; rubbish") (7)**
- `35-246:68`: "so evaṃ vadeyya"; `:287`: "ettha ca mahājano ativelaṃ pamatto palaḷito". — **re-check: adjust: 35-246:114 "He would hear the sound of a lute. Hey," → "He would hear the sound of a lute. He would say thus: Hey,"; 35-246:353 add at the end, after "just like anything [else].": " And yet the people are excessively heedless over this and led astray [by it]." (DPD pamatta "heedless"; palaḷita "deluded; misled") (8)**
- `35-93:50`: "rūpā aniccā vipariṇāmino aññathābhāvino". — **re-check: adjust: 35-93:80, after "The eye [is] impermanent, changing, becoming otherwise." insert "Forms [are] impermanent, changing, becoming otherwise." (passage :47 confirmed) (9)**
- `56-31:134`, `:201`: `sambodhāya`. — **re-check: adjust: 56-31:163 and :226 "to higher understanding, to total emancipation" → "to higher understanding, to full awakening, to total emancipation" (DPD sambodha "full awakening") (9)**
- `56-33:40`: `gacchanti`. — **re-check: adjust: 56-33:69 "sometimes (lit: once also) from this world to the next world, sometimes from the next world come back to this world" → "sometimes (lit: once also) go from this world to the next world, sometimes come back from the next world to this world" (8)**
- `56-34:23`: `bhikkhave`. — **re-check: adjust: 56-34:37 "clothes or head are burning, what should" → "clothes or head are burning, monks, what should" (9)**
- `56-38:121`: two full sentences ("neva tāva mahato ālokassa pātubhāvo hoti… andhakāratimisā"). — **re-check: adjust: 56-38:168 after "the perfectly awakened one," insert "for just so long there is no manifestation of great light, of great radiance; then there is blinding darkness, pitch-black darkness. For just so long" and drop the old "for just so long" before "there is no explaining" (DPD andhakāratimisā "pitch black darkness") (8)**
- `56-47:26`: "vassasatassa vassasatassa accayena sakiṃ sakiṃ ummujjanto" in the question. — **re-check: adjust: 56-47:73 "would that turtle blind in one eye put its neck" → "would that turtle blind in one eye, emerging once every hundred years, put its neck" (9)**
- `56-49:67`: "sinerupabbatarājānaṃ upanidhāya". — **re-check: adjust: 56-49:103 "they don’t even approach a tiny fraction.”" → "they don’t even approach a tiny fraction, compared to Sineru, king of mountains.”" (passage :64–65 confirmed; table gloss for upanidhāya is "compared to") (9)**
- MN 107: `brāhmaṇa` (`:299`), `bhikkhave` (`:1081`, `:1158`), "icchāmahaṃ, bhante, rājagahaṃ gantuṃ" (`:1471`), "evaṃ anusāsīyamāno" (`:1610`), `brāhmaṇo` (`:1749`), "bho gotama" (`:1915`). — **re-check: adjust: mn107:311 "in the same way, the Tathagata" → "In the same way, brahman, the Tathagata"; :1115 "Furthermore, with" → "Furthermore, monks, with"; :1186 "And furthermore, with" → "And furthermore, monks, with"; :1492 "he would say, ‘show me" → "he would say, ‘I wish to go to Rājagaha, sir; show me"; :1622 "being thus advised by you," → "being thus advised, thus instructed by you,"; :1759 "Gaṇakamoggallāna said" → "the brahman Gaṇakamoggallāna said"; :1959 "Just as the fragrant" → "Just as, Master Gotama, the fragrant" (8)**

### Typos and broken English

- `22-26:170`, `:223`: "Marā". `22-58:19`, `:53`: "non-clininging". `22-82:125`, `:270`, `:476`: "the Blessed" without "One". `22-95:143`: "rains clouds". — **re-check: adjust: 22-26:219, :261 "Marā" → "Māra"; 22-58:49, :86 "non-clininging" → "non-clinging"; 22-82:141, :282, :521 "the Blessed" → "the Blessed One"; 22-95:188 "rains clouds" → "rain clouds" (9)**
- `35-136:33`: "cessations". `35-228:55`, `:97`: "a persons ocean". `35-241:67`: "[it[". `35-241:577`: "cowhere". `35-247:401`: "would go it [its] control". — **re-check: adjust: 35-136:89 "cessations" → "cessation"; 35-228:92, :135 "a persons ocean" → "a person's ocean"; 35-241:105 "[it[" → "[it]"; 35-241:607 "cowhere" → "cowherd"; 35-247:424 "(lit: would go it [its] control)" → "(lit: would go [to] its control)" (8)**
- `56-13:103`: "The craving that which is leading". `56-21:93`: "the way of leading". `56-33:20`: "a stick … fall once". `56-42:140`: "also leading to old age also". `56-31:168`: missing space after a closing quote. — **re-check: adjust: 56-13:146 "The craving that which is leading" → "The craving which is leading"; 56-21:120 "the way of leading" → "the way leading"; 56-33:36 "fall once" → "falls once"; 56-42:182 "also leading to old age also" → "leading also to old age"; 56-31:197 "suffering”has" → "suffering” has" (9)**
- MN 107: `:214` unmatched bracket "(lit: cause … to count]"; `:962` "[his] the mind"; `:1285` "finalgoal"; `:1626` "you, as encourager, exists". — **re-check: adjust: mn107:225 "(lit: cause … to count]" → "(lit: cause … to count)"; :976 "[his] the mind" → "[his] mind"; :1311 "finalgoal" → "final goal"; :1665 "you, as encourager, exists" → "you, as encourager, exist" (9)**

### Doubtful

- `22-95:324`: `akukkukajātaṃ` as "not crooked" (commentary: without a fruit-bud core). — **re-check: drop: DPD akukkukajāta is "growing straight up; not crooked; (comm) without a solid core", so "not crooked" at 22-95:404 matches DPD**
- `35-230:131`, `:161`: `gilitabaḷiso mārassa` as "swallowed the bait of death"; `baḷisa` is "hook" elsewhere in the file. — **re-check: adjust: 35-230:156 "has swallowed the bait of death" → "has swallowed Māra's hook"; :203 "has not swallowed the bait of death" → "has not swallowed Māra's hook" (DPD gilitabaḷisa "swallowed the hook; taken the bait (of)": "bait" is also within DPD, so this is a consistency fix with baḷisa "hook" in the same file) (6)**
- `35-241:286`: `nandīrāga` as "desire and lust" (delight and lust). — **re-check: adjust: 35-241:331 "a designation for desire and lust" → "a designation for delight and desire" (DPD nandīrāga "delight and desire") (8)**
- `35-246:39`: "santiṭṭhati sannisīdati ekodi hoti samādhiyati": four verbs, the last not clearly rendered. — **re-check: adjust: 35-246:63 "it becomes internally composed, [it] settles down, [it] calms down, is unified." → "it stands still internally, settles down, becomes unified, [and] becomes composed." (DPD santiṭṭhati "stands still", sannisīdati "settles down", ekodi hoti "becomes one", samādhiyati "becomes composed") (8)**
- `56-21:36`, `:70`, `:93`: "evamidaṃ dīghamaddhānaṃ sandhāvitaṃ saṃsaritaṃ mamañceva tumhākañca": the English has no main verb. — **re-check: adjust: 56-21:64, :86, :120 "thus this for a long time [that] has been running through [and] wandering on for you and me" → "thus for this long time there has been running on [and] wandering on by me and by you" (7)**
- `mn107:604`: `yato kho` as "Because". `mn107:1763`: `uddhatā` as "haughty". — **re-check: adjust: mn107:620 "Because, brahman, he is a monk knowing the measure regarding food," → "When, brahman, a monk knows the measure regarding food," (DPD yato 3 "when"). Drop the uddhatā part: "haughty" at :1794 matches DPD uddhata 1 "arrogant; conceited; haughty" (8)**

## Recommendation

Fix in this order:

1. **Decide the canonical schema**: 6 columns with ID, one sandhi convention, a closed POS/Grammar/compound vocabulary, one rule for `-eyyaṃ` optatives, one rule for capitals, quotes and line wrapping in Pāli passages. Write it down; everything else depends on it. — **re-check: undecided**
2. **Normalise the labels mechanically** with a script (typos, synonyms, brackets, `<br>`). This is low risk and removes most of the noise. — **re-check: undecided**
3. **Correct the Pāli text and table-against-text mismatches**, since tables and translations hang on them. Check the MN 107 passage at lines 1048–1160 against the source edition first. — **re-check: undecided**
4. **Correct the grammatical errors and the translations above by hand.** — **re-check: undecided**
5. **Backfill the missing IDs and convert MN 107**, which is the largest job. — **re-check: undecided**

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

## Fresh look (2026-11-16)

### Summary

| Category | SN 22.12–28 | 22.33–59 | 22.63–78 | 22.82 | 22.94 | 22.95–102 | 35.24–60 | 35.70–93 | 35.118–230 | 35.232 | 35.241 | 35.246 | 35.247, 56.1 | 56.5–25 | 56.27–38 | 56.42–49 | MN 107 a | MN 107 b | MN 107 c | Total | Conf. ≥ 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A. Pāli and grammar content errors | 10 | 17 | 8 | 7 | 9 | 18 | 23 | 6 | 10 | 9 | 9 | 8 | 17 | 12 | 12 | 17 | 10 | 23 | 15 | 240 | 127 |
| B. Tables, paradigms and lists that disagree with each other or themselves | 5 | 7 | 14 | 4 | 10 | 5 | 5 | 4 | 14 | 4 | 5 | 3 | 8 | 15 | 6 | 9 | 11 | 9 | 21 | 159 | 119 |
| C. Translation and gloss problems | 5 | 3 | 1 | 6 | 0 | 5 | 2 | 2 | 6 | 6 | 2 | 2 | 5 | 1 | 3 | 4 | 5 | 5 | 8 | 71 | 43 |
| D. English typos and grammar | 2 | 3 | 13 | 10 | 4 | 14 | 8 | 5 | 7 | 10 | 4 | 0 | 3 | 8 | 3 | 15 | 6 | 15 | 15 | 145 | 117 |
| E. Markdown defects that affect rendering | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 2 | 2 |
| F. Convention drift | 4 | 12 | 19 | 6 | 5 | 2 | 1 | 16 | 4 | 10 | 1 | 8 | 12 | 2 | 16 | 17 | 27 | 17 | 3 | 182 | 105 |
| G. Links | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| H. Data to re-verify (forms, references, counts) | 1 | 6 | 1 | 2 | 1 | 0 | 0 | 5 | 0 | 2 | 1 | 2 | 11 | 9 | 12 | 1 | 4 | 0 | 2 | 60 | 10 |
| I. Further details on the material under review | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 9 | 0 | 10 | 5 |
| **Total** | **27** | **48** | **56** | **35** | **29** | **44** | **39** | **38** | **41** | **41** | **22** | **23** | **56** | **47** | **52** | **63** | **65** | **78** | **65** | **869** | **528** |

Method: each of the 19 slices of `docs/6-pali-class/suttas/` was read line by line (Opus; MN 107 read by Fable and finalised by Opus), every Pāḷi item was checked against DPD, and every excerpt was checked with `verify_rows.py`. Rows the old audit already has are left out.
Date: 2026-11-16. Location is `<file>.md:<line>` under `docs/6-pali-class/suttas/`; a row that cites several lines lists every line that carries the excerpt.
Conf. below 8 means "check before changing". Rows with no concrete Suggested are in category H. Slice labels are the SN/MN numbers of the files read.

### A. Pāli and grammar content errors

| Location | Current | Problem | Suggested | Conf. |
| --- | --- | --- | --- | --- |
| sn-22/22-12.md:75 | `\| 36370 \| nāparaṃ \| noun \| nt.nom.sg \|` | `nāparaṃ` is the sandhi `na + aparaṃ`, not a noun (DPD has `apara` but no `nāparaṃ` headword) | POS `sandhi`, Grammar `ind+adj`, Construction `na + aparaṃ` | 6 |
| sn-22/22-18.md:82 | `aniccasambhūtā \| adj \| nt.nom.pl` | DPD `aniccasambhūta` is an adj, so it takes the gender of `saṅkhārā` (masc.nom.pl, line 84) and cannot be neuter. The known item at line 86 is `niccā`, a different row | `masc.nom.pl` | 8 |
| sn-22/22-23.md:15 | `[√dis + \*e + ti` | Stray `[` at the start of the construction (the `+ ti` ending is the known global finding) | `√dis + \*e + ti` | 9 |
| sn-22/22-23.md:62 | `\| ime \| prom \|` | POS typo (DPD `ima`: pron) | `pron` | 9 |
| sn-22/22-26.md:27 | `\| sato \| prp \| masc.dat.sg \|` | DPD: `sato` is prp, masc gen sg of santa, gen abs. It agrees with `anabhisambuddhassa` and `bodhisattassa` (lines 23–24, tagged gen abs). The known item for this line is the Construction cell (`sa + √as`); this row is the Grammar cell | `masc.gen.sg (gen abs)` | 9 |
| sn-22/22-26.md:115 | `masc.gensg` | Grammar tag typo | `masc.gen.sg` | 9 |
| sn-22/22-26.md:191 | `\| yathābhūtaṃ \| sandhi \| ind \|` | DPD `yathābhūtaṃ`: ind, adv, abyayībhāva compound, not a sandhi | POS `ind`, Grammar `adv` | 9 |
| sn-22/22-26.md:243 | `\| yathābhūtaṃ \| sandhi \| ind \|` | Same as line 191 (DPD: ind, adv, abyayībhāva) | POS `ind`, Grammar `adv` | 9 |
| sn-22/22-28.md:104 | `\| vedanāya \| noun \| fem.loc.sg \| in feeling \|` | `vedanāya … assādo` parallels `rūpassa assādo` and `saṅkhārānaṃ` (gen.pl, line 115), so it is genitive. The translation (line 149) has "of feeling" | `fem.gen.sg`, gloss `of feeling` | 8 |
| sn-22/22-28.md:110 | `\| saññāya \| noun \| fem.loc.sg \| in perception \|` | Genitive, as at line 104. The translation (line 149) has "of perception" | `fem.gen.sg`, gloss `of perception` | 8 |
| sn-22/22-33.md:17 | `\| 30215 \| taṃ \| pron \| nt.nom.sg \| that \|` | `taṃ` in `taṃ pajahatha` is the object (DPD `taṃ 1.2` acc sg); the same slot is `30216` nt.acc.sg at :41 and :61 | `\| 30216 \| taṃ \| pron \| nt.acc.sg \| that \|` | 9 |
| sn-22/22-33.md:83 | `tiṇakaṭṭhasākhāpalāsaṃ \| noun \| nt.acc.sg` | In `yaṃ imasmiṃ jetavane tiṇakaṭṭhasākhāpalāsaṃ` the compound agrees with `yaṃ` (nt.nom.sg at :78); the acc is `taṃ`. DPD confirms nt only; the case is syntax | `tiṇakaṭṭhasākhāpalāsaṃ \| noun \| nt.nom.sg` | 7 |
| sn-22/22-33.md:134 | `\| 38883 \| no \| ind \| neg \| no; not \|` | In `na hi no etaṃ … attā` the negation is `na`; `no` is the pronoun (DPD `no 2.3` pron 1st dat pl), as `10868 no pron 1st.dat.pl` at 22-58:120. Table cell only; the known item at 22-33:125 is the translation | `\| 10868 \| no \| pron \| 1st.dat.pl \| our; for us \|` | 8 |
| sn-22/22-58.md:7 | `ko adhippayāso, adhippāyaso, kiṃ nānākaraṇaṃ` | Variant reading pasted into the text; DPD has only `adhippayāsa`, and :13, :88 and :172 have only `adhippayāso` | `ko adhippayāso, kiṃ nānākaraṇaṃ` | 8 |
| sn-22/22-58.md:198 | `maggānugā \| adj \| masc.nom.pl` | Compound type given as genitive (`chaṭṭha`, member `#maggassa` at :199); DPD `maggānuga` is `dutiyā tappurisa maggaṃ + anuga`. The misspelling `chaṭṭha` itself is already known | Construction `dutiyā tappurisa`; member at :199 `\| \| \#maggaṃ \| noun \| masc.acc.sg \| the path \| \|` | 8 |
| sn-22/22-59.md:32 | `\| 29605 \| tatra \| ind \| abl \|` | `tatra` "there; in that place" is DPD `ind, adv`, not ablative; 22-58:92 tags it `adv` | `\| 29605 \| tatra \| ind \| adv \|` | 8 |
| sn-22/22-59.md:59 | `anattā \| adj \| nt.nom.sg` | `anattā` cannot be nt.nom.sg of an adjective (that is `anattaṃ`); it stands unchanged with fem `vedanā` and pl `saṅkhārā`, so it is the noun `anattā` masc.nom.sg. Saved DPD output has no `anattā`/`anatta` line | `anattā \| noun \| masc.nom.sg` (DPD lookup: anattā) | 7 |
| sn-22/22-59.md:88 | `anattā \| adj \| nt.nom.sg` | As :59 | `anattā \| noun \| masc.nom.sg` (DPD lookup: anattā) | 7 |
| sn-22/22-59.md:115 | `anattā \| adj \| nt.nom.sg` | As :59; subject `vedanā` is fem, so nt is wrong in any reading | `anattā \| noun \| masc.nom.sg` (DPD lookup: anattā) | 7 |
| sn-22/22-59.md:117 | `anattā \| adj \| nt.nom.sg` | As :59; subject `saññā` is fem | `anattā \| noun \| masc.nom.sg` (DPD lookup: anattā) | 7 |
| sn-22/22-59.md:119 | `anattā \| adj \| nt.nom.sg` | As :59; subject `saṅkhārā` is pl | `anattā \| noun \| masc.nom.sg` (DPD lookup: anattā) | 7 |
| sn-22/22-59.md:121, 150 | `anattā \| adj \| nt.nom.sg` | As :59 | `anattā \| noun \| masc.nom.sg` (DPD lookup: anattā) | 7 |
| sn-22/22-59.md:201 | `\#dhammaṃ \| noun \| nt.nom.sg \| nature` | DPD `dhamma 1.01` is masc ("nature; character"); as a compound member it takes the bare gender like `\#vipariṇāma \| noun \| masc.` at :200 | `\#dhamma \| noun \| masc. \| nature` | 8 |
| sn-22/22-59.md:393 | `nibbindatI` | Capital `I` inside the word (DPD `nibbindati`). The re-check of the known † typo item covers :391, :395, :397, :399; this row adds only :393 | `nibbindati` | 9 |
| sn-22/22-59.md:402 | `virāgā \| noun \| masc.instr/abl.sg` | `virāgā` can only be abl.sg (instr is `virāgena`); 22-58:27 has `masc.abl.sg` | `virāgā \| noun \| masc.abl.sg` | 8 |
| sn-22/22-59.md:414 | `karaṇīyaṃ \| prp \| nt.nom.sg` | `-anīya` form is a future passive participle (DPD `karaṇīya 2` ptp), not a present participle | `karaṇīyaṃ \| ptp \| nt.nom.sg` | 9 |
| sn-22/22-59.md:415 | `nāparaṃ \| noun \| nt.nom.sg \| nothing more; no further state \| (na+ apa + ra)` | `nāparaṃ` is sandhi of `na + aparaṃ`, not a noun; the construction skips the sandhi step (its `apa + ra` matches DPD `apara`). DPD has no `nāparaṃ` headword | `nāparaṃ \| sandhi \| \| nothing more; no further state \| na + aparaṃ` | 6 |
| sn-22/22-63.md:110 | `ājānāsī` | headword keeps the sandhi lengthening of `ājānāsīti`; the form is `ājānāsi` + `ti` (iti is its own row at :111) | `ājānāsi` | 7 |
| sn-22/22-63.md:211 | `uṭṭhāyāsanā \| verb \| ger \| rising from his seat \| verbal compound?` | `uṭṭhāyāsanā` is a sandhi of `uṭṭhāya` (DPD: ger of uṭṭhahati) + `āsanā` (as the `#` sub-rows :212–213 show), not a verb or a compound | POS `sandhi`, Grammar empty, Construction `uṭṭhāya+āsanā` | 7 |
| sn-22/22-63.md:249 | `anagāriyaṃ \| noun \| nt.acc.sg` | DPD `anagāriyā` is fem ("homelessness"); `anagāriyaṃ` is fem.acc.sg | `fem.acc.sg` | 8 |
| sn-22/22-63.md:271 | `karaṇīyaṃ \| prp` | `-aṇīya` form is a future passive participle (DPD karaṇīya 2: ptp of karoti), not a present participle | `ptp` | 9 |
| sn-22/22-63.md:272 | `nāparaṃ \| noun \| nt.nom.sg` | `nāparaṃ` is the sandhi `na + aparaṃ` (sub-rows :273–274 follow the sandhi pattern), not a kammadhāraya noun; DPD has no headword `nāparaṃ` | POS `sandhi`, Grammar empty, Construction `na+aparaṃ` | 7 |
| sn-22/22-78.md:264 | `amhā \| verb \| pr.1st.pl` | DPD amha 1.1: pr 1st pl of atthi, `√as + mha`; the long ā in `niccamhāti` comes from sandhi with `iti` | `amha \| verb \| pr.1st.pl \| we are \| √as + mha` | 8 |
| sn-22/22-78.md:274 | `amhā \| verb \| pr.1st.pl` | as :264 (`dhuvamhāti`) | `amha` | 8 |
| sn-22/22-78.md:283 | `amhā \| verb \| pr.1st.pl` | as :264 (`sassatamhāti`) | `amha` | 8 |
| sn-22/22-82.md:549 | `saññākkhandhassa \| noun \| masc.nom.sg` | `-assa` form of masc `saññākkhandha` (DPD) is gen/dat sg, tagged nom.sg; known item covers only :505, :511, :517 | `masc.gen.sg` | 8 |
| sn-22/22-82.md:555 | `saṅkhārakkhandhassa \| noun \| masc.nom.sg` | `-assa` form of masc `saṅkhārakkhandha` (DPD) is gen/dat sg, tagged nom.sg; known item covers only :505, :511, :517 | `masc.gen.sg` | 8 |
| sn-22/22-82.md:561 | `viññāṇakkhandhassa \| noun \| masc.nom.sg` | `-assa` form of masc `viññāṇakkhandha` (DPD) is gen/dat sg, tagged nom.sg; known item covers only :505, :511, :517 | `masc.gen.sg` | 8 |
| sn-22/22-82.md:150 | `56270 \| sake \| adj \| masc.loc.sg \| in [your] own` | `sake` (DPD saka 1, adj) agrees with `āsane` (nt.loc.sg, :151) | `nt.loc.sg` | 7 |
| sn-22/22-82.md:173 | `56270 \| sake \| adj \| masc.loc.sg \| in [his] own` | `sake` (DPD saka 1, adj) agrees with `āsane` (nt.loc.sg, :174) | `nt.loc.sg` | 7 |
| sn-22/22-82.md:155 | `53738 \| yadā \| ind \| adv \| whatever; whenever` | `yadākaṅkhasi` = `yad` (yaṃ, "whatever") + `ākaṅkhasi`, not `yadā`; DPD `yadā` means only "when; whenever"; the gloss "whatever" already shows the pronoun (DPD has no headword for the sandhi) | `\| \| \#yad (yaṃ) \| pron \| nt.acc.sg \| whatever \| \|` | 7 |
| sn-22/22-82.md:469 | `khandhādhivacanaṃ \| noun \| nt.acc.sg` | Subject of a nominal sentence (`ettāvatā … khandhādhivacanaṃ`); :393 tags the same form nom.sg | `nt.nom.sg` | 7 |
| sn-22/22-94.md:79 | `yaṃ \| pron \| nt.nom.sg \| which; that; that which` | In `yamahaṃ natthīti vadāmi` (line 69) `yaṃ` is the object of `vadāmi`; the parallel `taṃ` (line 51) is tagged nt.acc.sg. DPD ya 2.1 gives no case | `yaṃ \| pron \| nt.acc.sg \| which; that; that which` | 6 |
| sn-22/22-94.md:143 | `yaṃ \| pron \| nt.nom.sg \| which` | As line 79: object of `vadāmi` in `yamahaṃ atthīti vadāmi` | `yaṃ \| pron \| nt.acc.sg \| which` | 6 |
| sn-22/22-94.md:155 | `\#vipariṇāma \| noun \| nt. \| change; alteration` | vipariṇāma is masculine (DPD vipariṇāma: masc) | `\#vipariṇāma \| noun \| masc. \| change; alteration` | 9 |
| sn-22/22-94.md:312 | `ajānantaṃ \| adj \| masc.acc.sg` | Present participle tagged adj; DPD ajānanta: prp of na jānāti; other participles in the file use `prp` | `ajānantaṃ \| prp \| masc.acc.sg` | 8 |
| sn-22/22-94.md:313 | `apassantaṃ \| adj \| masc.acc.sg` | Present participle tagged adj; DPD apassanta: prp of na passati | `apassantaṃ \| prp \| masc.acc.sg` | 8 |
| sn-22/22-94.md:378 | `ajānantaṃ \| adj \| masc.acc.sg` | As line 312 | `ajānantaṃ \| prp \| masc.acc.sg` | 8 |
| sn-22/22-94.md:379 | `apassantaṃ \| adj \| masc.acc.sg` | As line 313 | `apassantaṃ \| prp \| masc.acc.sg` | 8 |
| sn-22/22-94.md:315 | `\#kiṃ \| pron \| nt.nom.sg \| what` | In `kinti karomi` `kiṃ` is not a nominative; DPD kinti 1 (sandhi, ind + ind, interr) and the idiom kinti karomi (ind + ind + pr) take it as the interrogative indeclinable | `\#kiṃ \| ind \| interr \| what` | 7 |
| sn-22/22-94.md:381 | `\#kiṃ \| pron \| nt.nom.sg \| what` | As line 315 | `\#kiṃ \| ind \| interr \| what` | 7 |
| sn-22/22-95.md:119 | `taṃ \| pron \| masc.acc.sg \| it` | `taṃ` refers to `rūpaṃ` (nt); no masculine antecedent in this section (line 112 tags the same `taṃ` nt.acc.sg) | `taṃ \| pron \| nt.acc.sg \| it` | 7 |
| sn-22/22-95.md:166 | `taṃ \| pron \| masc.acc.sg \| it` | `taṃ` refers to `udakapubbuḷaṃ` (nt.nom.sg at line 154); masc is wrong | `taṃ \| pron \| nt.acc.sg \| it` | 7 |
| sn-22/22-95.md:212 | `taṃ \| pron \| masc.acc.sg \| it` | Antecedent is `vedanā` (fem); line 205 tags the same `taṃ` nt.acc.sg; masc is wrong under either reading | `taṃ \| pron \| nt.acc.sg \| it` (or fem.acc.sg) | 7 |
| sn-22/22-95.md:258 | `taṃ \| pron \| masc.acc.sg \| it` | Antecedent is `marīcikā` (fem); masc is wrong | `taṃ \| pron \| nt.acc.sg \| it` (or fem.acc.sg) | 7 |
| sn-22/22-95.md:300 | `taṃ \| pron \| masc.acc.sg \| it` | Antecedent is `saññā` (fem); line 293 tags the same `taṃ` nt.acc.sg; masc is wrong | `taṃ \| pron \| nt.acc.sg \| it` (or fem.acc.sg) | 7 |
| sn-22/22-95.md:428, 479, 523 | `taṃ \| pron \| masc.acc.sg \| it` | Same defect: antecedents `saṅkhārā` (generic sg `taṃ`), `māyaṃ` (fem), `viññāṇaṃ` (nt); masc is wrong in each | `taṃ \| pron \| nt.acc.sg \| it` (479: or fem.acc.sg) | 7 |
| sn-22/22-95.md:566 | `virāgā \| noun \| masc.instr.sg` | `virāgā` is the ablative singular of masc `virāga` (DPD virāga 1.1 masc; instr. would be `virāgena`) | `virāgā \| noun \| masc.abl.sg` | 8 |
| sn-22/22-95.md:573 | `nāparaṃ \| noun \| nt.nom.sg` | `nāparaṃ` is sandhi of `na + aparaṃ` (DPD apara 1 adj "further"), not a noun | `nāparaṃ \| sandhi \| ind+adj` with construction `na + aparaṃ` | 7 |
| sn-22/22-95.md:370 | `vi + nī + √bhuj + a + anta` | Present participle suffix doubled `a`; DPD vinibbhujati is `√bhuj 2 a` (vi + nī + bhuja + ti), and all other prp rows in the file use `a + nta` (e.g. line 152 `√vass + a + nta`) | `vi + nī + √bhuj + a + nta` | 8 |
| sn-22/22-95.md:337 | `\#pariyesana+ṃ \| noun\>adj \| fem.nom.sg\>adv` | The form ending in `-ṃ` is the accusative, not the nominative; DPD sārapariyesanaṃ is "ind, adv, acc sg of sārapariyesana" (sāra + pariyesanā + aṃ). The known item cites only the compound row at line 335; this is the member row | `\#pariyesana+ṃ \| noun\>adj \| fem.acc.sg\>adv` | 8 |
| sn-22/22-102.md:124 | `na + √aggh + a + ti` | Grammar is `pr.3rd.pl` but the construction gives the 3rd sg ending (DPD agghati `√aggh a`, aggha + ti) | `na + √aggh + a + nti` | 8 |
| sn-22/22-102.md:210 | `sabbaṃ \| pron \| nt.acc.sg` | Qualifies `kāmarāgaṃ` (masc.acc.sg; DPD kāmarāga masc); other `sabbaṃ kāmarāgaṃ` rows tag masc | `sabbaṃ \| pron \| masc.acc.sg` | 8 |
| sn-22/22-102.md:256 | `sabbaṃ \| pron \| nt.acc.sg` | Qualifies `kāmarāgaṃ` (masc.acc.sg; DPD kāmarāga masc) | `sabbaṃ \| pron \| masc.acc.sg` | 8 |
| sn-22/22-102.md:157 | `sabbaṃ \| pron \| masc.acc.sg` | Qualifies `tamagataṃ` (nt.acc.sg at line 161; DPD tamagata nt) | `sabbaṃ \| pron \| nt.acc.sg` | 8 |
| sn-22/22-102.md:158 | `ākāsagataṃ \| adj \| masc.acc.sg` | Adjective (DPD ākāsagata adj) agreeing with `tamagataṃ` (nt.acc.sg at line 161; DPD tamagata nt) | `ākāsagataṃ \| adj \| nt.acc.sg` | 8 |
| sn-22/22-102.md:165 | `√bhās + a + ti` | Grammar is `pr.reflex.3rd.sg` (form `bhāsate`) but the construction gives the active ending | `√bhās + a + te` | 6 |
| sn-22/22-102.md:167 | `√tap + a + ti` | Grammar is `pr.reflex.3rd.sg` (form `tapate`) but the construction gives the active ending | `√tap + a + te` | 6 |
| sn-22/22-102.md:169 | `vi + √ruc + \*a + ti` | Grammar is `pr.reflex.3rd.sg` (form `virocate`) but the construction gives the active ending; the `\*a` is right (DPD virocati `√ruc *a`) | `vi + √ruc + \*a + te` | 6 |
| sn-35/35-28.md:240 | `virāgā \| noun \| masc.instr.sg` | `virāgā` is the ablative singular (instr.sg is `virāgena`); "through dispassion" is an ablative of cause | Grammar `masc.abl.sg` | 7 |
| sn-35/35-60.md:62 | `virāgā \| noun \| masc.instr.sg` | `virāgā` is abl.sg, not instr.sg | Grammar `masc.abl.sg` | 7 |
| sn-35/35-60.md:109 | `virāgā \| noun \| masc.instr.sg` | `virāgā` is abl.sg, not instr.sg | Grammar `masc.abl.sg` | 7 |
| sn-35/35-60.md:64 | `vimokkhā \| noun \| masc.instr.sg` | `vimokkhā` is abl.sg (instr.sg is `vimokkhena`) | Grammar `masc.abl.sg` | 7 |
| sn-35/35-60.md:111 | `vimokkhā \| noun \| masc.instr.sg` | `vimokkhā` is abl.sg, not instr.sg | Grammar `masc.abl.sg` | 7 |
| sn-35/35-28.md:253 | `nāparaṃ \| noun \| nt.nom.sg \| nothing more` | `nāparaṃ` is a sandhi of `na + aparaṃ`, not a noun; the Construction cell is empty | POS `sandhi`; Construction `na + aparaṃ` | 7 |
| sn-35/35-28.md:274 | `abhinanduṃ \| verb \| aor.3rd.pl (+acc) … abhi + √nand + i` | Construction ends in the 3rd sg aorist ending `+ i`; the form is 3rd pl `-uṃ` | `abhi + √nand + a + uṃ` | 6 |
| sn-35/35-28.md:252 | `√kar + aṇīya]` | Stray closing bracket in the construction | `√kar + aṇīya` | 8 |
| sn-35/35-53.md:32 | `upa + saṃ + √kam + i]` | Stray closing bracket in the construction | `upa + saṃ + √kam + i` | 8 |
| sn-35/35-53.md:41 | `[ni + √sad + a + na` | Stray opening bracket in the construction | `ni + √sad + a + na` | 8 |
| sn-35/35-53.md:57 | `[ud + √pad + ya + ti` | Stray opening bracket in the construction (line 102 has it without) | `ud + √pad + ya + ti` | 8 |
| sn-35/35-53.md:75 | `[ud + √pad + ya + ti` | Stray opening bracket in the construction | `ud + √pad + ya + ti` | 8 |
| sn-35/35-53.md:83 | `[ud + √pad + ya + ti` | Stray opening bracket in the construction | `ud + √pad + ya + ti` | 8 |
| sn-35/35-53.md:91 | `[ud + √pad + ya + ti` | Stray opening bracket in the construction | `ud + √pad + ya + ti` | 8 |
| sn-35/35-53.md:99 | `[ud + √pad + ya + ti` | Stray opening bracket in the construction | `ud + √pad + ya + ti` | 8 |
| sn-35/35-53.md:117, 133, 141, 150, 168 | `[ud + √pad + ya + ti` | Same stray opening bracket on the remaining `uppajjati` rows | `ud + √pad + ya + ti` | 8 |
| sn-35/35-53.md:103 | `vedayitaṃ \| noun \| nt.acc.sg` | `vedayitaṃ` is the subject of `uppajjati` in the relative clause (nom.); 35-24 and 35-28 tag the same clause `nt.nom.sg` | Grammar `nt.nom.sg` | 6 |
| sn-35/35-53.md:154 | `vedayitaṃ \| noun \| nt.acc.sg` | Subject of `uppajjati`: nominative, not accusative | Grammar `nt.nom.sg` | 6 |
| sn-35/35-53.md:104 | `sukhaṃ \| adj \| nt.acc.sg` | Qualifies `vedayitaṃ`, the subject of `uppajjati`: nominative | Grammar `nt.nom.sg` | 6 |
| sn-35/35-53.md:106 | `dukkhaṃ \| adj \| nt.acc.sg` | Qualifies the nominative `vedayitaṃ` | Grammar `nt.nom.sg` | 6 |
| sn-35/35-53.md:108 | `adukkhamasukhaṃ \| adj \| nt.acc.sg` | Qualifies the nominative `vedayitaṃ` | Grammar `nt.nom.sg` | 6 |
| sn-35/35-53.md:155, 157, 159 | `adj \| nt.acc.sg` | Same accusative tag on `sukhaṃ`, `dukkhaṃ`, `adukkhamasukhaṃ` in the mind clause | Grammar `nt.nom.sg` | 6 |
| sn-35/35-60.md:37 | `cakkhuviññāṇaṃ \| noun \| nt.acc.sg` | Subject of `uppajjati`; the parallel `manoviññāṇaṃ` on line 83 is `nt.nom.sg` | Grammar `nt.nom.sg` | 8 |
| sn-35/35-70.md:13 | `viññūhī... .` | Closing `ti` missing; the same passage at line 222 reads `viññūhīti... .` | `viññūhīti... .` | 6 |
| sn-35/35-70.md:95, 120, 125, 248, 253, 273, 278 | `\| rūpesu \| noun \| masc.loc.pl \|` | Remaining lines of the known `rūpesu` gender error, which cites only `35-70:90`: DPD `rūpa 1–3` nt, and the same file tags `##rūpe` nt.loc.sg (81, 111) | `nt.loc.pl` | 8 |
| sn-35/35-85.md:59 | `\| 21641 \| kiñca \| sandhi \| ind+ind \|` | `kiṃ` here is the interrogative pronoun (subject of `suññaṃ`: "what is empty"); DPD `kiñca 1`: sandhi, pron + ind | `pron+ind` | 8 |
| sn-35/35-85.md:62, 70, 76, 84, 92, 115, 124 | `\| attena \| noun \| nt.instr.sg \|` | Remaining lines of the known `attena` gender error, which cites only `35-85:50`: DPD `atta 1.1` masc | `masc.instr.sg` | 8 |
| sn-35/35-93.md:72 | `\| √cal \|` | Truncated construction for `calaṃ` (root only); DPD `cala`: `√cal + a`. Not in the known list of 11 truncated constructions | `√cal + a` | 8 |
| sn-35/35-93.md:103 | `\| aññathābhāvī \| adj \| nt.nom.sg \|` | Agrees with masc `paccayo` (`sopi paccayo anicco vipariṇāmī aññathābhāvī`); the neighbouring `vipariṇāmī` (102) is masc.nom.sg | `masc.nom.sg` | 8 |
| sn-35/35-118.md:75 | `\| \#diṭṭhe \| pp \| nt.loc.sg \|` | `diṭṭhe` agrees with `dhamme` (masc.loc.sg at :77); neuter contradicts the noun it qualifies (DPD idiom diṭṭhe dhamme: pp + masc) | `\| \#diṭṭhe \| pp \| masc.loc.sg \|` | 7 |
| sn-35/35-118.md:263 | `\| \#diṭṭhe \| pp \| nt.loc.sg \|` | Same as :75; `dhamme` at :265 is masc.loc.sg | `\| \#diṭṭhe \| pp \| masc.loc.sg \|` | 7 |
| sn-35/35-136.md:37 | `\| \| \#rāmā \| adj \|` | Second member of `rūpārāmā` is `ārāma` (DPD rūpārāma: rūpa + ārāma), as in `\#ārāmā` at :60 | `\| \| \#ārāmā \| adj \|` | 9 |
| sn-35/35-136.md:122 | `\| \| \#rāmo \| adj \|` | Second member of `rūpārāmo` is `ārāma` (DPD rūpārāma: rūpa + ārāma), as in `\#ārāmo` at :158 | `\| \| \#ārāmo \| adj \|` | 9 |
| sn-35/35-230.md:9 | `manoiññeyyā dhammā iṭṭhā kantā manāpā` | Misspelling (missing `v`); table passage :71 has `manoviññeyyā` (DPD manoviññeyya). The known item lists only 35-118:17, :199 | `manoviññeyyā dhammā iṭṭhā kantā manāpā` | 9 |
| sn-35/35-230.md:17 | `manoiññeyyā dhammā iṭṭhā` | Misspelling (missing `v`); table passage :158 has `manoviññeyyā`. The known item lists only 35-118 | `manoviññeyyā dhammā iṭṭhā` | 9 |
| sn-35/35-230.md:45 | `\| 12126 \| āmisacakkhu \| … \| kammadhāraya\> bahubbīhi \|` | DPD gives `sattamī tappurisa > bahubbīhi` (āmise + cakkhu). The known item on this row is about the grammar cell (nt.nom.sg), not the construction | `sattamī tappurisa\> bahubbīhi` | 9 |
| sn-35/35-230.md:64 | `\| \| \#kāma \| adj \| masc. \| wishing to \|` | In `yathākāma` the member `kāma` is the noun "wish, desire", not an adjective "wishing to" (DPD has kāma 1 adj "wishing" in comps and kāma 3 masc, but does not say which sense yathākāmakaraṇīya uses) | `\| \| \#kāma \| noun \| masc. \| wish; desire \|` | 5 |
| sn-35/35-230.md:152 | `\| \| \#kāma \| adj \| masc. \| wishing to \|` | Same as :64 | `\| \| \#kāma \| noun \| masc. \| wish; desire \|` | 5 |
| sn-35/35-230.md:199 | `\| \| \#kāma \| adj \| masc. \| wishing to \|` | Same as :64 | `\| \| \#kāma \| noun \| masc. \| wish; desire \|` | 5 |
| sn-35/35-232.md:58 | `vi + √har + a + ti` | Construction of 3rd plural `viharanti` ends in the 3rd singular `ti` (DPD viharati: `vi + hara + ti` for the 3rd sg) | `vi + √har + a + nti` | 7 |
| sn-35/35-232.md:105 | `mano \| noun \| masc.nom.sg` | `mano` (manas stem) is neuter, not masculine; saved DPD has no `mano` headword, only `manindriya` with member `man<b>aso</b>` | `nt.nom.sg` | 7 |
| sn-35/35-232.md:109 | `manassa \| noun \| masc.gen.sg` | `mano` (manas stem) is neuter, not masculine; saved DPD silent on gender | `nt.gen.sg` | 7 |
| sn-35/35-232.md:146 | `mano \| noun \| masc.nom.sg` | `mano` (manas stem) is neuter, not masculine; saved DPD silent on gender | `nt.nom.sg` | 7 |
| sn-35/35-232.md:151 | `manassa \| noun \| masc.gen.sg` | `mano` (manas stem) is neuter, not masculine; saved DPD silent on gender | `nt.gen.sg` | 7 |
| sn-35/35-232.md:189 | `assu \| verb \| opt.3rd.pl \| would be; were \| √as + a` | Construction stops before the optative ending; DPD assu 3.1 (opt 3rd pl of assa, √as) gives `assa + u` | `assa + u` | 8 |
| sn-35/35-232.md:594 | `manasā \| noun \| masc.instr.sg` | `mano` (manas stem) is neuter, not masculine; saved DPD silent on gender | `nt.instr.sg` | 7 |
| sn-35/35-232.md:283, 382, 409, 474, 591, 637 | `mano \| noun \| masc.nom.sg` | Same masc-for-nt error as line 105 | `nt.nom.sg` | 7 |
| sn-35/35-232.md:288, 390, 415, 480, 643 | `manassa \| noun \| masc.gen.sg` | Same masc-for-nt error as line 109 | `nt.gen.sg` | 7 |
| sn-35/35-241.md:255 | `orimaṃ \| adj \| nt.acc.sg` | In the question `kiṃ nu kho … orimaṃ tīraṃ` the phrase is nominative (subject with `kiṃ` nt.nom.sg, line 251); the answer table (line 288) tags it nt.nom.sg | `nt.nom.sg` | 8 |
| sn-35/35-241.md:256 | `tīraṃ \| noun \| nt.acc.sg` | Same question: nominative, not accusative (cf. line 289) | `nt.nom.sg` | 8 |
| sn-35/35-241.md:258 | `pārimaṃ \| adj \| nt.acc.sg` | Same question `kiṃ pārimaṃ tīraṃ`: nominative (cf. line 299) | `nt.nom.sg` | 8 |
| sn-35/35-241.md:259 | `tīraṃ \| noun \| nt.acc.sg` | Same question: nominative (cf. line 300) | `nt.nom.sg` | 8 |
| sn-35/35-241.md:675 | `karaṇīyaṃ \| prp \| nt.nom.sg` | `karaṇīya` is a potential participle, not a present participle (DPD karaṇīya 2: ptp of karoti, `√kar + aṇīya`); same file tags `\#karaṇīyesu` as `ptp` (line 359) | `ptp` | 9 |
| sn-35/35-241.md:676 | `nāparaṃ \| noun \| nt.nom.sg \| nothing more; no further state \| kammadhāraya (na+ aparaṃ)` | `nāparaṃ` is the sandhi of two words `na` + `aparaṃ`, not a kammadhāraya compound or a noun (DPD has no headword `nāparaṃ`) | `nāparaṃ \| sandhi \| ind+adj \| nothing more; no further state \| ` (keep the `\#na` / `\#aparaṃ` sub-rows) | 6 |
| sn-35/35-241.md:363 | `[ā + √pad + ya + ti` | Stray opening bracket in the construction (DPD āpajjati: √pad ya) | `ā + √pad + ya + ti` | 9 |
| sn-35/35-241.md:464 | `[ava + √su + ta` | Stray opening bracket in the construction (DPD avassuta: `ava + √su + ta`) | `ava + √su + ta` | 9 |
| sn-35/35-241.md:560 | `vacchagiddhiniyo \| noun \| fem.nom.pl` | Qualifies `gāvo` ("longing for their calves"); its own head member is tagged `adj` (line 562), so the compound is an adjective; DPD has no headword `vacchagiddhinī` | `vacchagiddhiniyo \| adj \| fem.nom.pl` | 5 |
| sn-35/35-246.md:155 | `\| \| bho \| noun \| masc.voc.sg \| good man \| \|` | Addressed to several people (`gacchatha`, `āharatha` imp.2nd.pl; translation line 165 "Go, men"); DPD bho is voc sg & pl | `\| \| bho \| noun \| masc.voc.pl \| good men \| \|` | 8 |
| sn-35/35-246.md:206 | `\| \| bho \| noun \| masc.voc.sg \| good man \| \|` | Addressed to several people (`āharatha` imp.2nd.pl, line 213); DPD bho is voc sg & pl | `\| \| bho \| noun \| masc.voc.pl \| good men \| \|` | 8 |
| sn-35/35-246.md:334 | `\| \| bho \| noun \| masc.voc.sg \| good man (men) \| \|` | Translation (line 353) has "good men"; tag says singular (DPD bho is voc sg & pl) | `\| \| bho \| noun \| masc.voc.pl \| good men \| \|` | 6 |
| sn-35/35-246.md:211 | `\| \| me \| pron \| 1st.acc.sg \| me \| \|` | "bring me just the sound": `me` is the recipient, dative, not accusative (`saddaṃ` is the object); the known item covers only line 154 | `\| \| me \| pron \| 1st.dat.sg \| to me \| \|` | 7 |
| sn-35/35-246.md:240 | `\| 59773 \| samāraddhā \| pp \| masc.nom.pl \|` | `samāraddhā` agrees with `vīṇā` (fem.nom.sg, subject of `vadati`); nothing masc.nom.pl in the sentence (`sambhārehi` is instr.) | `\| 59773 \| samāraddhā \| pp \| fem.nom.sg \|` | 7 |
| sn-35/35-246.md:279 | `\| 59773 \| samāraddhā \| pp \| masc.nom.pl \|` | Same as line 240 | `\| 59773 \| samāraddhā \| pp \| fem.nom.sg \|` | 7 |
| sn-35/35-246.md:266 | `\| \| eva \| ind \| adv \| thus \| \|` | DPD evāyaṃ = evaṃ + ayaṃ; "thus" is `evaṃ`, `eva` means "just; only" | `\| \| evaṃ \| ind \| adv \| thus \| \|` | 8 |
| sn-35/35-246.md:339 | `\| \| āyaṃ \| pron \| fem.nom.sg \| this \| \|` | `yathevayaṃ` = yathā + eva + ayaṃ; `āyaṃ` is not a pronoun form (DPD ayaṃ masc & fem nom sg); the known row covers only line 333; depends on the reading (H row :27, 285) | `\| \| ayaṃ \| pron \| fem.nom.sg \| this \| \|` | 7 |
| sn-35/35-247.md:83 | `tasmātiha o, bhikkhave` | Pāḷi typo: the enclitic is `vo` (the same sentence at line 700 has `tasmātiha vo`) | `tasmātiha vo, bhikkhave` | 9 |
| sn-35/35-247.md:357 | `chappāṇake \| noun \| masc.acc.pl` | Text (line 346) has the subject `chappāṇakā` (nom.pl), not acc.pl `chappāṇake`. The known item at `35-247:293` concerns the compound type on another line | `chappāṇakā \| noun \| masc.nom.pl` | 9 |
| sn-35/35-247.md:358 | `nānāvisaye \| noun\>adj \| masc.acc.pl` | Text (line 346) has `nānāvisayā` (nom.pl, agreeing with `chappāṇakā`) | `nānāvisayā \| noun\>adj \| masc.nom.pl` | 9 |
| sn-35/35-247.md:359 | `nānāgocare \| noun \| masc.acc.pl` | Text (line 347) has `nānāgocarā` (nom.pl) | `nānāgocarā \| noun \| masc.nom.pl` | 9 |
| sn-35/35-247.md:606 | `chappāṇake \| noun \| masc.acc.pl` | Text (line 564) has `chappāṇakā` (nom.pl) | `chappāṇakā \| noun \| masc.nom.pl` | 9 |
| sn-35/35-247.md:607 | `nānāvisaye \| noun\>adj \| masc.acc.pl` | Text (line 564) has `nānāvisayā` (nom.pl) | `nānāvisayā \| noun\>adj \| masc.nom.pl` | 9 |
| sn-35/35-247.md:608 | `nānāgocare \| noun \| masc.acc.pl` | Text (line 564) has `nānāgocarā` (nom.pl) | `nānāgocarā \| noun \| masc.nom.pl` | 9 |
| sn-35/35-247.md:169 | `\#gāmakaṇṭako \| sandhi` | `gāmakaṇṭaka` is a compound (sub-rows `##gāma`, `##kaṇṭako`), not a sandhi | `\#gāmakaṇṭako \| noun \| masc.nom.sg \| thorn of the village \| chaṭṭhī tappurisa` (DPD lookup: gāmakaṇṭaka, for the compound type; saved DPD has no headword) | 6 |
| sn-35/35-247.md:223 | `\#cetaso \| noun \| masc.gen.sg` | `ceto`/`cetas` is neuter (saved DPD has no `ceto` headword) | `\#cetaso \| noun \| nt.gen.sg` | 7 |
| sn-35/35-247.md:227 | `\#cetaso \| noun \| masc.gen.sg` | `ceto`/`cetas` is neuter (saved DPD has no `ceto` headword) | `\#cetaso \| noun \| nt.gen.sg` | 7 |
| sn-35/35-247.md:502 | `\#cetaso \| noun \| masc.gen.sg` | `ceto`/`cetas` is neuter (saved DPD has no `ceto` headword) | `\#cetaso \| noun \| nt.gen.sg` | 7 |
| sn-35/35-247.md:506 | `\#cetaso \| noun \| masc.gen.sg` | `ceto`/`cetas` is neuter (saved DPD has no `ceto` headword) | `\#cetaso \| noun \| nt.gen.sg` | 7 |
| sn-35/35-247.md:599 | `vā \| ind \| cond \| or` | `vā` "or" is disjunctive, not conditional (DPD vā 1 "or; either or"); the file's other `vā` rows (lines 151, 707) have `conj` | `vā \| ind \| conj \| or` | 8 |
| sn-35/35-247.md:601 | `vā \| ind \| cond \| or` | `vā` "or" is disjunctive, not conditional (DPD vā 1); lines 151, 709 have `conj` | `vā \| ind \| conj \| or` | 8 |
| sn-35/35-247.md:645 | `vā \| ind \| cond \| or` | `vā` "or" is disjunctive, not conditional (DPD vā 1); lines 151, 707 have `conj` | `vā \| ind \| conj \| or` | 8 |
| sn-35/35-247.md:647 | `vā \| ind \| cond \| or` | `vā` "or" is disjunctive, not conditional (DPD vā 1); lines 151, 709 have `conj` | `vā \| ind \| conj \| or` | 8 |
| sn-35/35-247.md:721 | `vo \| pron \| 2nd.nom/instr.pl \| you; by you` | Double tag; here `vo` can only be the agent of `sikkhitabbaṃ` (the translation at line 749 has "it should be trained by you"), i.e. DPD vo 1.3 instr pl "by you all" | `vo \| pron \| 2nd.instr.pl \| by you` | 7 |
| sn-56/56-13.md:161 | `\| 29188 \| \#tassāya \| pron \| fem.gen.sg \| of that \|` | `tassāyeva` = `tassā` + `eva` with the sandhi glide -y-; `tassāya` is not a form of `ta`. DPD `tassā 2`: pron, fem gen sg of ta. | `\| 29188 \| \#tassā \| pron \| fem.gen.sg \| of that \|` | 8 |
| sn-56/56-13.md:130 | `\| 7797 \| \#abhinandī \| noun \| fem.nom.sg \| delight \|` | The member of `tatratatrābhinandinī` is the adjective `abhinandinī` (fem. of `abhinandin`, "delighting in"), not a noun `abhinandī` "delight". DPD has no headword `abhinandin`. The known item at :126 concerns the parent's grammar, not this member row. | `\| 7797 \| \#abhinandinī \| adj \| fem.nom.sg \| delighting (in) \|` (ID: DPD lookup `abhinandin`) | 6 |
| sn-56/56-13.md:116 | `\| 47464 \| ponobhavikā \| adj \| fem.nom.sg \| leading to repeated existence \| kammadhāraya \> bahubbīhi \|` | DPD `ponobbhavika` is an adj derived from `punabbhava` + `*ika` (construction `puna > pono + bhava + *ika / punabbhava + *ika`), with no compound type; the row labels it a kammadhāraya > bahubbīhi. (DPD also spells it with `bb`; see NOTES.) | Construction `punabbhava + ika` in place of `kammadhāraya \> bahubbīhi` | 8 |
| sn-56/56-25.md:28 | `\| 66122 \| vadāmi \| verb \| pr.1st.sg (+acc) \| I say \| √vad + a + ti \|` | First-person singular present ends in -mi; DPD `vadāmi` construction is `vada + āmi`. Not a non-present verb, so not covered by the GLOBAL "+ ti" finding. | `√vad + a + mi` | 9 |
| sn-56/56-21.md:54 | `\| sandhāvitaṃ \| noun \| nt.nom.sg \| transmigration; lit. ran along \| saṃ + √dhāv \|` | Construction truncated; DPD `sandhāvita 1` (nt, pp of sandhāvati) has `saṃ + √dhāv + ita`, like `saṃsaritaṃ` on the next line. Not among the 11 truncated constructions in GLOBAL. | `saṃ + √dhāv + ita` | 8 |
| sn-56/56-21.md:81 | `\| sandhāvitaṃ \| noun \| nt.nom.sg \| transmigration \| saṃ + √dhāv \|` | Same truncated construction as :54 (DPD `saṃ + √dhāv + ita`). | `saṃ + √dhāv + ita` | 8 |
| sn-56/56-21.md:115 | `\| sandhāvitaṃ \| noun \| nt.nom.sg \| transmigration \| saṃ + √dhāv \|` | Same truncated construction as :54 (DPD `saṃ + √dhāv + ita`). | `saṃ + √dhāv + ita` | 8 |
| sn-56/56-5.md:101 | `\| 32949 \| dukkhasamudayaṃ \| noun \| nt.nom.sg \| origin of suffering \| kammadhāraya \> bahubbīhi \|` | DPD `dukkhasamudaya` is `chaṭṭhī tappurisa dukkhassa + samudaya`, as at 56-7:96, 56-21:95, 56-25:56; here it is labelled `kammadhāraya > bahubbīhi`. The known finding covers only `dukkhanirodhaṃ`. | `chaṭṭhī tappurisa` | 8 |
| sn-56/56-13.md:38 | `\| 32949 \| dukkhasamudayaṃ \| noun \| nt.nom.sg \| origin of suffering \| kammadhāraya \> bahubbīhi \|` | Same as 56-5:101: DPD `dukkhasamudaya` is a chaṭṭhī tappurisa. | `chaṭṭhī tappurisa` | 8 |
| sn-56/56-13.md:108 | `\| 32949 \| dukkhasamudayaṃ \| noun \| nt.nom.sg \| origin of suffering \| kammadhāraya \> bahubbīhi \|` | Same as 56-5:101: DPD `dukkhasamudaya` is a chaṭṭhī tappurisa. | `chaṭṭhī tappurisa` | 8 |
| sn-56/56-13.md:143 | `\| 32949 \| dukkhasamudayaṃ \| noun \| nt.nom.sg \| origin of suffering \| kammadhāraya \> bahubbīhi \|` | Same as 56-5:101: DPD `dukkhasamudaya` is a chaṭṭhī tappurisa. | `chaṭṭhī tappurisa` | 8 |
| sn-56/56-21.md:134 | `\| 32949 \| dukkhasamudayaṃ \| noun \| nt.nom.sg \| origin of suffering \| kammadhāraya \> bahubbīhi \|` | Same as 56-5:101: DPD `dukkhasamudaya` is a chaṭṭhī tappurisa. | `chaṭṭhī tappurisa` | 8 |
| sn-56/56-31.md:7 | `yaṃ o mayā abhiññāya` | `o` for `vo` (DPD `vo` pron, 2nd pl of tvaṃ); the same passage at :104 reads `yaṃ vo mayā` | `yaṃ vo mayā abhiññāya` | 9 |
| sn-56/56-31.md:65 | `\| 53973 \| yāni \| pron \| nt.acc.pl \| which; that \| \|` | Subject of the passive `mayā … gahitāni` (an implied "are"), so nominative; cf. `etāni` nt.nom.pl at :92 (DPD `yāni`: nt nom & acc pl, so either form is possible) | `nt.nom.pl` | 7 |
| sn-56/56-31.md:68 | `\| 43492 \| parittāni \| pp(adj) \| nt.acc.pl \|` | Agrees with the nominative subject `yāni … sīsapāpaṇṇāni … gahitāni`; not an object here (unlike :42 with `gahetvā`) | `nt.nom.pl` | 7 |
| sn-56/56-31.md:69 | `\| \| sīsapāpaṇṇāni \| noun \| nt.acc.pl \|` | Subject of passive `gahitāni`, so nominative | `nt.nom.pl` | 7 |
| sn-56/56-31.md:71 | `\| 24683 \| gahitāni \| pp \| nt.acc.pl \|` | Predicate pp agreeing with the nominative subject (agent `mayā`) | `nt.nom.pl` | 7 |
| sn-56/56-31.md:72 | `\| 53973 \| yāni \| pron \| nt.acc.pl \| which \|` | Subject of `yāni vā upari sīsapāvane [santi]`, so nominative | `nt.nom.pl` | 7 |
| sn-56/56-31.md:84 | `\| 6960 \| Appamattakāni \| adj \| nt.acc.pl \|` | Predicate of the reply `appamattakāni … gahitāni`, so nominative | `nt.nom.pl` | 7 |
| sn-56/56-31.md:87 | `\| 43492 \| parittāni \| pp(adj) \| nt.acc.pl \|` | Agrees with the nominative subject of passive `gahitāni` (agent `bhagavatā`) | `nt.nom.pl` | 7 |
| sn-56/56-31.md:88 | `\| 63280 \| sīsapāpaṇṇāni \| noun \| nt.acc.pl \|` | Subject of passive `gahitāni` (agent `bhagavatā`), so nominative | `nt.nom.pl` | 7 |
| sn-56/56-31.md:90 | `\| 24683 \| gahitāni \| pp \| nt.acc.pl \|` | Predicate pp agreeing with the nominative subject (agent `bhagavatā`) | `nt.nom.pl` | 7 |
| sn-56/56-33.md:53 | `\| 61682 \| \#saṃyojanā \| noun \| masc.nom.pl \|` | DPD `saṃyojana` is nt only (1, 2); the member is given the gender of the bahubbīhi head (`\#taṇhāya` at :52 keeps its own) | `\| 61682 \| \#saṃyojanāni \| noun \| nt.nom.pl \|` | 8 |
| sn-56/56-38.md:7 | `N’eva andhakāratamaṃ tadā hoti` | The parallel sentence at :11 and :170 reads `N’eva andhatamaṃ`, and the table for :73 has `Andhatamaṃ` (:98); DPD has `andhatama` nt "deep darkness" and no `andhakāratama`; `andhakāratamaṃ` looks like a slip (verify against CST) | `N’eva andhatamaṃ tadā hoti` | 6 |
| sn-56/56-44.md:35 | `\| dukkhaṃ \| noun \| nt.nom.sg \|` | object of the gerund `anabhisamecca` (DPD: "not realizing; not completely understanding", transitive), so accusative; `paṭipadaṃ` in the same phrase is tagged fem.acc.sg | `nt.acc.sg` | 7 |
| sn-56/56-44.md:36 | `\| ariyasaccaṃ \| noun \| nt.nom.sg \|` | object of `anabhisamecca`, accusative | `nt.acc.sg` | 7 |
| sn-56/56-44.md:41 | `\| ariyasaccaṃ \| noun \| nt.nom.sg \|` | apposed to `paṭipadaṃ` (fem.acc.sg, :40), object of `anabhisamecca` | `nt.acc.sg` | 7 |
| sn-56/56-44.md:92 | `\| dukkhaṃ \| noun \| nt.nom.sg \|` | object of `anabhisamecca`, accusative | `nt.acc.sg` | 7 |
| sn-56/56-44.md:93 | `\| ariyasaccaṃ \| noun \| nt.nom.sg \|` | object of `anabhisamecca`, accusative | `nt.acc.sg` | 7 |
| sn-56/56-44.md:98, 125, 126, 131, 175, 176, 181 | `noun \| nt.nom.sg` | same: `dukkhaṃ` / `ariyasaccaṃ` are objects of `anabhisamecca` / `abhisamecca` | `nt.acc.sg` | 7 |
| sn-56/56-49.md:46 | `\| yā \| pron \| fem.acc.pl \|` | in `katamaṃ … bahutaraṃ: yā vā … upanikkhittā, yo vā sinerupabbatarājā` the two compared items are subjects; `yo … sinerupabbatarājā` is tagged nom | `fem.nom.pl` | 7 |
| sn-56/56-49.md:51 | `\| upanikkhittā \| pp \| fem.acc.pl \|` | same clause: nominative, agreeing with `yā` | `fem.nom.pl` | 7 |
| sn-56/56-49.md:78 | `\| Appamattikā \| adj \| fem.acc.pl \|` | predicate of a nominal sentence with `pāsāṇasakkharā upanikkhittā` as subject: nominative | `fem.nom.pl` | 7 |
| sn-56/56-49.md:84 | `\| upanikkhittā \| pp \| fem.acc.pl \|` | subject of the nominal sentence, nominative | `fem.nom.pl` | 7 |
| sn-56/56-49.md:100 | `\| upanikkhittā \| pp \| fem.acc.pl \|` | the pebbles are the subject of `upenti` (3rd pl): nominative | `fem.nom.pl` | 7 |
| sn-56/56-49.md:48, 49, 50, 81, 82, 83, 97, 98, 99 | `acc.pl` | `satta`, `muggamattiyo`, `pāsāṇasakkharā` in the same three clauses are nominative too | `nom.pl` in the same cells (`x.nom.pl`, `fem.nom.pl`) | 7 |
| sn-56/56-49.md:125 | `\| dukkhaṃ \| noun \| nt.acc.sg \|` | subject of `etadeva bahutaraṃ` (`bahutaraṃ` tagged nt.nom.sg at :124): nominative | `nt.nom.sg` | 7 |
| sn-56/56-49.md:127 | `\| parikkhīṇaṃ \| pp \| nt.acc.sg \|` | agrees with the nominative `dukkhaṃ` (`yadidaṃ parikkhīṇaṃ`) | `nt.nom.sg` | 7 |
| sn-56/56-49.md:128 | `\| pariyādinnaṃ \| pp \| nt.acc.sg \|` | same: nominative | `nt.nom.sg` | 7 |
| sn-56/56-49.md:129 | `\| appamattakaṃ \| adj \| nt.acc.sg \|` | predicate of the nominal sentence `appamattakaṃ avasiṭṭhaṃ`: nominative | `nt.nom.sg` | 7 |
| sn-56/56-49.md:130 | `\| avasiṭṭhaṃ \| pp \| nt.acc.sg \|` | subject of `appamattakaṃ avasiṭṭhaṃ` and of `upeti` (3rd sg): nominative | `nt.nom.sg` | 7 |
| mn-107-ganakamoggallanasuttam.md:157 | `ā√jīv･1 a (live)+a+aṃ` | Ending `+aṃ` does not give the form in the row (`ājīvānaṃ`, dat.pl); DPD `ājīva` stem `ā + √jīv + a` | `ā√jīv･1 a (live)+a+ānaṃ` | 7 |
| mn-107-ganakamoggallanasuttam.md:176 | `\#ante \| adj \| masc. \| inside, within; near` | `ante` is tagged adj masc.; DPD has `ante` as a prefix ("inside; inner; within"), with `antevāsī` = `ante + vāsī` | `\#ante \| prefix \| \| inside, within; near` | 8 |
| mn-107-ganakamoggallanasuttam.md:217 | `\#satam \| card \| nt.nom.sg` | `sataṃ` is the object of `gaṇāpema`, so accusative, not nominative (DPD `sata 2.1` card nt gives no case) | `nt.acc.sg` | 7 |
| mn-107-ganakamoggallanasuttam.md:393 | `\#dvāro \| noun \| masc.nom.sg \| door` | DPD `dvāra 1` is nt; the masc ending belongs only to the whole bahubbīhi `guttadvāro` | `\#dvāra \| noun \| nt. \| door` | 8 |
| mn-107-ganakamoggallanasuttam.md:417 | `\#enaṃ \| pron \| nt. \| this, him` | `enaṃ` refers to the person (it agrees with `viharantaṃ` masc.acc.sg, line 420, and is masc.acc.sg at lines 377 and 615); DPD silent (`ena` no headword) | `masc.acc.sg` | 6 |
| mn-107-ganakamoggallanasuttam.md:456 | `√ghā･3 ya (smell)+ ya \> ghāya` | Construction of the absolutive `ghāyitvā` stops at the present stem; DPD `ghāyitvā` = `ghāya + itvā` | `√ghā･3 ya (smell)+ ya \> ghāya+itvā` | 8 |
| mn-107-ganakamoggallanasuttam.md:674 | `\#seyyāṃ` | Impossible form (long ā before ṃ); DPD `seyyā` fem, acc.sg `seyyaṃ`; member of `sīhaseyyaṃ` | `\#seyyaṃ` | 9 |
| mn-107-ganakamoggallanasuttam.md:682 | `ud√ṭhā･1 a (stand)(d\>t)+ ana` | Sandhi note gives dental `t`; the result `uṭṭhāna` (DPD `ud + √ṭhā + ana`) has retroflex `ṭ` | `ud√ṭhā･1 a (stand)(d \> ṭ)+ ana` | 7 |
| mn-107-ganakamoggallanasuttam.md:697 | `pacc + u√ṭhā･1 a (stand)+ya` | Prefix written `u`; DPD `paccuṭṭhāya` = `pati > paty > pacc + ud + √ṭhā + ya` | `pati\> paty \> pacc + ud√ṭhā･1 a (stand)+ya` | 9 |
| mn-107-ganakamoggallanasuttam.md:278 | `\#damma+ko \| ptp \| - \| tamable; trainable` | Member glossed as ptp "tamable", but DPD `assadammaka` (masc, agent, chaṭṭhī tappurisa) = `assa + dammaka` "horse trainer"; the second member is the agent noun `dammaka`, not ptp `damma` | `\#dammako \| noun \| masc.nom.sg \| trainer; tamer` | 7 |
| mn-107-ganakamoggallanasuttam.md:702 | `\| cittaṃ \| noun \| masc.acc.sg \| mind \|` | `cittaṃ` is neuter (DPD `citta 1.1` nt; tagged nt.acc.sg at :908, :934, :955); the known finding lists only :642 | `nt.acc.sg` | 9 |
| mn-107-ganakamoggallanasuttam.md:904 | `\| \#abhijjhā \| noun \| fem.instr.sg \|` | Member of the bahubbīhi `vigatābhijjhena`; the form `abhijjhā` is nom.sg, not instr.sg (compare `\#thīnamiddho` nom.sg at :949, `\#citto` nom.sg at :971) | `fem.nom.sg` | 6 |
| mn-107-ganakamoggallanasuttam.md:905 | `\| cetasā \| noun \| masc.instr.sg \|` | `ceto` (mano group) is neuter; `vigatābhijjhena` at :902 (masc.instr.sg) agrees with it and changes too | `nt.instr.sg` (and :902 `nt.instr.sg`) | 6 |
| mn-107-ganakamoggallanasuttam.md:1011 | `\| cetaso \| noun \| masc.gen.sg \| of the mind \|` | `ceto` is neuter | `nt.gen.sg` | 6 |
| mn-107-ganakamoggallanasuttam.md:1100 | `\| cetaso \| noun \| masc.gen.sg \| of the mind \|` | `ceto` is neuter | `nt.gen.sg` | 6 |
| mn-107-ganakamoggallanasuttam.md:924 | `\| sabbapāṇabhūtahitānukampī \| noun \| masc.nom.sg \|` | POS `noun`, but the word is an adjective describing the monk (DPD `sabbapāṇabhūtahitānukampī` adj); its own member row :930 says `adj` | `adj` | 8 |
| mn-107-ganakamoggallanasuttam.md:1013 | `pa√ñā･5 nā (know)+ya` | This is the construction of the gerund; the row is the noun `paññā` in the genitive ("of wisdom"), DPD `paññā 1` pa + √ñā + ā | `pa√ñā･5 nā (know)+ā+āya` | 8 |
| mn-107-ganakamoggallanasuttam.md:1034 | `\| \#vicāraṃ \| noun \| masc.acc.sg \| examination \| √car･1 \*e (move, walk)+ \*e \> cāre (caus)+a+aṃ \|` | Prefix `vi` dropped from the construction (DPD `vicāra 1` vi + cāre + a; not in the known list of dropped prefixes); :1031 `vi√takk` has it | `vi√car･1 \*e (move, walk)+ \*e \> cāre (caus)+a+aṃ` | 8 |
| mn-107-ganakamoggallanasuttam.md:1036 | `\| \#vivekasmā \| noun \| nt.abl.sg \|` | `viveka` is masculine (DPD `viveka 1` masc) | `masc.abl.sg` | 9 |
| mn-107-ganakamoggallanasuttam.md:1052 | `\| so \| ind \| \| he \|` | `so` "he" is a pronoun (DPD `so 1.1` pron, masc nom sg of ta; tagged `pron \| masc.nom.sg` at :851, :871, :898). Same defect as the known row :1006, but on another line, so kept | `\| so \| pron \| masc.nom.sg \| he \|` | 8 |
| mn-107-ganakamoggallanasuttam.md:1074 | `\| apphuṭaṃ \| adj \| masc.acc.sg (+instr) \|` | Predicate of `kiñci … hoti` ("nothing … is not pervaded"), so neuter nominative, not masc accusative | `nt.nom.sg (+instr)` | 6 |
| mn-107-ganakamoggallanasuttam.md:1188, 1198 | `apattamānasā` | Pāḷi spelling: DPD has `appattamānasa` (na > a + patta + mānasa, with doubled p); also `\#apatta` at :1199 | `appattamānasā`; :1199 `\#appatta` | 8 |
| mn-107-ganakamoggallanasuttam.md:1199 | `na\>a√ap･4 uṇā (reach, attain)+ta (p\>t)` | Prefix `pa` missing: DPD `appatta 1` na > a + pa + √ap + ta (compare :1236 `anu+pa√ap`) | `na \> a + pa√ap･4 uṇā (reach, attain)+ta` | 8 |
| mn-107-ganakamoggallanasuttam.md:1200 | `\| \#mānasā \| adj \| nt.acc.pl \| of such a mind \|` | `nt.acc.pl` fits neither the stem-form member nor the compound (masc.nom.pl at :1198). DPD has `mānasa 1` adj in comps "of such mind" and `mānasa 2` nt "mind; intention"; the compound meaning ("not fulfilled one's intention") takes the noun | `\| \#mānasaṃ \| noun \| nt.nom.sg \| mind; intention \|` | 6 |
| mn-107-ganakamoggallanasuttam.md:1209 | `\| ayaṃ \| pron \| masc.nom.sg \| this \|` | `ayaṃ` agrees with `anusāsanī` (fem.nom.sg at :1210–1211); DPD `ayaṃ` is masc & fem nom sg | `fem.nom.sg` | 8 |
| mn-107-ganakamoggallanasuttam.md:1296 | `\| evaṃ \| ind \| emph \| thus \|` | `evaṃ` "thus" is an adverb (DPD `ind, adv`; tagged `adv` at :1272), not an emphatic particle | `adv` | 8 |
| mn-107-ganakamoggallanasuttam.md:1298 | `\| evaṃ \| ind \| emph \| thus \|` | Same: `evaṃ` is an adverb | `adv` | 8 |
| mn-107-ganakamoggallanasuttam.md:1324 | `\| evaṃ \| ind \| emph \| thus \|` | Same: `evaṃ` is an adverb | `adv` | 8 |
| mn-107-ganakamoggallanasuttam.md:1326 | `\| evaṃ \| ind \| emph \| thus \|` | Same: `evaṃ` is an adverb | `adv` | 8 |
| mn-107-ganakamoggallanasuttam.md:1378 | `\| evaṃ \| ind \| emph \| thus \|` | Same: `evaṃ` is an adverb | `adv` | 8 |
| mn-107-ganakamoggallanasuttam.md:1380 | `\| evaṃ \| ind \| emph \| thus \|` | Same: `evaṃ` is an adverb (last of six) | `adv` | 8 |
| mn-107-ganakamoggallanasuttam.md:1353 | `\| nibbānaṃ, \| noun \| nt.acc.sg \| to extinguishing; to nibbāna \|` | `nibbānaṃ` is the subject of `tiṭṭhateva` ("nibbāna exists", as the translation at :1364 has it), so nominative | `\| nibbānaṃ, \| noun \| nt.nom.sg \| extinguishing; nibbāna \|` | 7 |
| mn-107-ganakamoggallanasuttam.md:1176 | `\| upekkhāsatipārisuddhiṃ \| noun \| fem.acc.sg \| purification of awareness by equanimity \| tatiyā tappurisa as bahubbīhi \|` | Labelled bahubbīhi but tagged as a feminine noun; DPD `upekkhāsatipārisuddhi` is adj (tatiyā tappurisa > bahubbīhi), here describing `jhānaṃ` | `\| upekkhāsatipārisuddhiṃ \| adj \| nt.acc.sg \|` | 8 |
| mn-107-ganakamoggallanasuttam.md:1402 | `\#taṃ \| pron \| nt.nom.sg \| that` | In "taṃyevettha paṭipucchissāmi" `taṃ` is the object of the verb, so it cannot be nominative. DPD `taṃyevettha` (taṃ + eva + ettha, "about this matter") does not say which `taṃ`; it may also be the person asked (`taṃ` 2nd.acc.sg, as at line 1474). | `\#taṃ \| pron \| nt.acc.sg \| that` (or `\#taṃ \| pron \| 2nd.acc.sg \| you` if read as the person asked) | 6 |
| mn-107-ganakamoggallanasuttam.md:1438 | `evaṃ \| ind \| emph \| indeed` | `evaṃ` is not an emphatic particle. Here ("evaṃ, bho") it is the affirmative reply; DPD `evaṃ 2`: ind, excl, "yes!". The translation at line 1449 has "Yes". | `evaṃ \| ind \| excl \| yes` | 9 |
| mn-107-ganakamoggallanasuttam.md:1476 | `evaṃ \| ind \| emph \| thus` | `evaṃ` "thus" is an adverb (DPD `evaṃ 1`: ind, adv), not `emph`. Line 1949 tags it `adv`. | `evaṃ \| ind \| adv \| thus` | 9 |
| mn-107-ganakamoggallanasuttam.md:1502 | `evaṃ \| ind \| emph \| thus` | Same: `evaṃ` "thus" tagged `emph` (DPD `evaṃ 1`: ind, adv). | `evaṃ \| ind \| adv \| thus` | 9 |
| mn-107-ganakamoggallanasuttam.md:1577 | `evaṃ \| ind \| emph \| thus` | Same: `evaṃ` "thus" tagged `emph` (DPD `evaṃ 1`: ind, adv). | `evaṃ \| ind \| adv \| thus` | 9 |
| mn-107-ganakamoggallanasuttam.md:1579 | `evaṃ \| ind \| emph \| thus` | Same: `evaṃ` "thus" tagged `emph` (DPD `evaṃ 1`: ind, adv). | `evaṃ \| ind \| adv \| thus` | 9 |
| mn-107-ganakamoggallanasuttam.md:1614, 1616, 1648, 1650, 1692, 1715, 1717 | `evaṃ \| ind \| emph` | Same: `evaṃ` "thus" tagged `emph` on the remaining lines of this range (DPD `evaṃ 1`: ind, adv). | `evaṃ \| ind \| adv` | 9 |
| mn-107-ganakamoggallanasuttam.md:1612 | `so \| ind \| \| then` | `so` is the pronoun "he" (subject of `gaccheyya`; DPD `so 1.1`: pron, masc nom sg, "he"), as in the identical sentence at line 1575. The translation at line 1622 follows the wrong gloss ("Then, … he would go"). | `so \| pron \| masc.nom.sg \| he` | 9 |
| mn-107-ganakamoggallanasuttam.md:1426, 1443, 1462, 1482, 1510, 1598, 1619, 1660 | `rājagahaṃ \| noun \| masc.acc.sg` | DPD `rājagaha` is nt (comp, chaṭṭhī tappurisa), but every row tags it masculine. Line 1637 is handled in its own row below. | `rājagahaṃ \| noun \| nt.acc.sg` on all these rows | 9 |
| mn-107-ganakamoggallanasuttam.md:1486, 1553 | `rājagahassa \| noun \| masc.gen.sg` | Same: DPD `rājagaha` is nt; the genitive rows are tagged masculine (split from the `rājagahaṃ` row). | `rājagahassa \| noun \| nt.gen.sg` | 9 |
| mn-107-ganakamoggallanasuttam.md:1637 | `rājagahaṃ \| noun \| masc.acc.sg \| Rāgagaha` | In "tiṭṭhateva rājagahaṃ" the word is the subject of `tiṭṭhati` ("Rājagaha exists"), so nominative, like `nibbānaṃ` nt.nom.sg in the parallel sentence (line 1697). DPD `rājagaha` is nt. | `rājagahaṃ \| noun \| nt.nom.sg` | 8 |
| mn-107-ganakamoggallanasuttam.md:1673 | `\#kiṃ \| pron \| nt.nom.sg \| what` | In "kyāhaṃ … karomi" `kiṃ` is the object of `karomi`, so accusative (DPD `kiṃ 1`: nt nom and acc sg). | `\#kiṃ \| pron \| nt.acc.sg \| what` | 8 |
| mn-107-ganakamoggallanasuttam.md:1873 | `\#ñūno \| noun \| masc.nom.pl \| knower` | Wrong form: the nominative plural of `-ññū` is `-ññuno` (short `u`), as in `mattaññuno` in the row above (line 1871). The gloss is singular. DPD `mattaññū` = matta + ñū; DPD has no headword `ññū`. | `\#ñuno \| noun \| masc.nom.pl \| knowers` | 6 |
| mn-107-ganakamoggallanasuttam.md:1930 | `\#aggaṃ \| adj \| masc.acc.sg \| highest; foremost; supreme` | With the passive `akkhāyati` ("is said to be") the predicate is nominative, not accusative; and a masculine nominative would be `aggo`. DPD `aggamakkhāyati` = aggaṃ + akkhāyati gives no case. | `\#aggaṃ \| adj \| nt.nom.sg \| highest; foremost; supreme` | 6 |
| mn-107-ganakamoggallanasuttam.md:2051 | `gatan”t \| sandhi` | Truncated: the passage (line 2020) has `gatan”ti`. | `gatan”ti \| sandhi` | 9 |

### B. Tables, paradigms and lists that disagree with each other or themselves

| Location | Current | Problem | Suggested | Conf. |
| --- | --- | --- | --- | --- |
| sn-22/22-26.md:145 | `\| sukhaṃ \| noun \| nt.acc.sg \|` | Subject of `uppajjati`. The same construction is tagged nt.nom.sg at line 82 | `nt.nom.sg` | 8 |
| sn-22/22-26.md:146 | `\| somanassaṃ \| noun \| nt.acc.sg \|` | Subject of `uppajjati`. The same construction is tagged nt.nom.sg at line 83 | `nt.nom.sg` | 8 |
| sn-22/22-26.md:151 | `\| viññāṇaṃ \| noun \| nt.acc.sg \|` | Subject in `yaṃ viññāṇaṃ aniccaṃ dukkhaṃ…`. The parallel `rūpaṃ` is tagged nt.nom.sg at line 95 | `nt.nom.sg` | 8 |
| sn-22/22-28.md:87 | `\| 2736 \| atthi \| verb \| pr.3rd.sg \| there is \| √as + ti \|` | The Pāḷi (line 69) reads `atthi rūpassa nissaraṇaṃ`, but the table has no `rūpassa` row between `atthi` and `nissaraṇaṃ` (the parallel tables have it at lines 32 and 60) | Insert `\| 55151 \| rūpassa \| noun \| nt.gen.sg \| of form \| \|` after line 87 | 8 |
| sn-22/22-28.md:124 | `\| 74149 \| idaṃ \| pron (or ind) \| nt.nom.sg \| this (here; in this case) \|` | The same ID and word (`nayidaṃ`) is tagged `ind`, `adv`, "here; in this case" at lines 25, 53, 81, 144 and 172, which is DPD `idaṃ 3` (ind, adv) | `\| 74149 \| idaṃ \| ind \| adv \| here; in this case \|` | 8 |
| sn-22/22-33.md:139 | `attaniyaṃ \| adj as noun \| nt.nom.sg` | Text `attaniyaṃ vāti` has a second `vā`; the table goes straight to `ti (iti)` at :140 | insert `\| 66665 \| vā \| ind \| conj \| or \| \|` after line 139 | 8 |
| sn-22/22-58.md:35 | `\| 6663 \| api \| ind \| \| too; also \|` | Text `bhikkhupi, bhikkhave, paññāvimutto`: the `bhikkhave` after `api` has no row | insert `\| 49868 \| bhikkhave \| noun \| masc.voc.pl \| monks \| \|` after line 35 | 8 |
| sn-22/22-58.md:72 | `\| 6663 \| api \| ind \| \| too; also \|` | Text `bhikkhupi, bhikkhave, paññāvimutto`: the `bhikkhave` after `api` has no row | insert `\| 49868 \| bhikkhave \| noun \| masc.voc.pl \| monks \| \|` after line 72 | 8 |
| sn-22/22-59.md:182 | `vā \| ind \| conj \| or` | Text `aniccaṃ vāti? aniccaṃ`: no `ti (iti)` row between the second `vā` (:182) and `aniccaṃ` (:183); present at :235 | insert `\| 30431 \| ti (iti) \| ind \| \| end of direct speech \| \|` after line 182 | 8 |
| sn-22/22-59.md:198 | `aniccaṃ \| adj \| nt.nom.sg \| impermanent` | Text `yaṃ panāniccaṃ dukkhaṃ vipariṇāmadhammaṃ`: `dukkhaṃ` has no row | insert `\| \| dukkhaṃ \| noun (or adj) \| nt.nom.sg \| suffering; discomfort \| \|` after line 198 | 8 |
| sn-22/22-59.md:251 | `aniccaṃ \| adj \| nt.nom.sg \| impermanent` | Text `yaṃ panāniccaṃ dukkhaṃ vipariṇāmadhammaṃ`: `dukkhaṃ` has no row | insert `\| \| dukkhaṃ \| noun (or adj) \| nt.nom.sg \| suffering; discomfort \| \|` after line 251 | 8 |
| sn-22/22-59.md:284 | `\| 21657 \| \#kiñci \| ind \| \| anything \|` | Same member is `21658 \#kiñci pron nt.nom.sg` at :342; in `yaṃ kiñci rūpaṃ` it agrees with `rūpaṃ`, i.e. DPD `kiñci 2` pron nt nom sg | `\| 21658 \| \#kiñci \| pron \| nt.nom.sg \| some; something \|` | 7 |
| sn-22/22-63.md:167 | `ājānāsī` | the passage at :152 reads `ājānāsi.` (no `iti`), so the long ī has no source at all | `ājānāsi` | 8 |
| sn-22/22-63.md:131 | `viññāṇaṃ \| noun \| nt.acc.sg` | passage :115 has `viññāṇaṃ upādiyamāno baddho`; the table goes from `viññāṇaṃ` (:131) straight to `baddho` (:132), so `upādiyamāno` is missing | insert after :131 `\| 16367 \| upādiyamāno \| prp \| masc.nom.sg (+acc) \| one clinging (lit: taking near) \| upa + √ādā + ya + māna \|` (copy of :122) | 8 |
| sn-22/22-63.md:180 | `viññāṇaṃ \| noun \| nt.acc.sg` | passage :152 has `viññāṇaṃ upādiyamāno baddho`; table goes from `viññāṇaṃ` (:180) to `baddho` (:181), `upādiyamāno` missing | insert after :180 `\| 16367 \| upādiyamāno \| prp \| masc.nom.sg (+acc) \| one clinging (lit: taking near) \| upa + √ādā + ya + māna \|` (copy of :171) | 8 |
| sn-22/22-71.md:126 | `rūpaṃ \| noun \| nt.nom.sg \| form` | the passage (:59) reads `sabbaṃ viññāṇaṃ` here (the viññāṇa repetition); the table repeats `rūpaṃ` | `viññāṇaṃ \| noun \| nt.nom.sg \| consciousness` | 9 |
| sn-22/22-71.md:153 | `kathaṃ \| ind \| adv-interr \| how?` | the passage (:145) reads `evaṃ passato`, not `kathaṃ` | `evaṃ \| ind \| adv \| thus; in this way` (as :149; DPD evaṃ 1) | 9 |
| sn-22/22-71.md:65 | `21657 \| \#kiñci \| ind` | the same word in the same idiom at :117 is ID 21658, pron nt.nom.sg; DPD has both (kiñci 1 ind, kiñci 2 pron nt nom sg), and here it goes with nt `rūpaṃ` as at :117 | `21658 \| \#kiñci \| pron \| nt.nom.sg \| some; something` as :117 (DPD kiñci 2) | 7 |
| sn-22/22-71.md:70 | `\#anāgata (ca) \| adj \| masc.` | three adjective members of one dvanda labelled `nt.` (:69), `masc.` (:70), `masc` (:71) | `nt.` as :69 | 6 |
| sn-22/22-71.md:71 | `\#paccuppanna (ca) \| adj \| masc` | as :70 | `nt.` as :69 | 6 |
| sn-22/22-78.md:259 | `eva \| ind \| emph \| indeed` | passage :254 `aniccāva kira, bho`: no `kira` row between `eva` (:259) and `bho` (:260); the other two sentences have it (:269, :278) | insert after :259 `\| 21807 \| kira \| ind \| adv \| truly \| \|` | 9 |
| sn-22/22-78.md:295 | `\#pariyāpannā` | passage :254 has `sakkāyapariyāpannāti.`; no `ti (iti)` row after the compound (next row :296 is `evaṃ`) | insert after :295 `\| 30431 \| ti (iti) \| ind \| \| end of direct speech \| \|` | 8 |
| sn-22/22-78.md:297, 298 | `bhikkhave \| noun \| masc.voc.pl` | passage :254 `mahiddhiko kho, bhikkhave`: no `kho` row between `mahiddhiko` (:297) and `bhikkhave` (:298) | insert after :297 `\| \| kho \| ind \| emph \| indeed \| \|` | 9 |
| sn-22/22-78.md:81 | `\#bila \| noun \| nt.` | English cell empty | `hole` (DPD bila 2) | 8 |
| sn-22/22-78.md:135 | `\#mahā \| adj \| masc` | English cell empty | `great` (DPD mahā 2) | 8 |
| sn-22/22-78.md:115 | `daḷhehi \| pp (adj) \| masc.instr.pl` | `daḷhehi` agrees with `varattehi`, which :116 tags `nt.instr.pl`; DPD varatta is nt | `nt.instr.pl` | 8 |
| sn-22/22-82.md:127 | `puccheyyaṃ \| verb \| opt. reflex.1st.sg \| I would ask` | Text has `puccheyyāhaṃ` (:123); the table has no row for `ahaṃ` (DPD pron "I"); the known :127 item concerns only the reflexive tag | Add row `\| \| ahaṃ \| pron \| 1st.nom.sg \| I \| \|` after :127 | 8 |
| sn-22/22-82.md:259 | `\| \| kho pana \| idiom \| ind+ind \| indeed \| \|` | Text has `ime kho, bhikkhu` (:233), no `pana` | `\| \| kho \| ind \| emph \| indeed \| \|` | 8 |
| sn-22/22-82.md:580 | `\#ariyassa \| noun \| masc.gen.sg \| of the noble ones` | Singular tag with plural gloss; DPD ariyadhamma 2 resolves the member as `ariyassa` (sg), so the gloss is the wrong cell | `\#ariyassa \| noun \| masc.gen.sg \| of the noble one` | 7 |
| sn-22/22-82.md:584 | `\#ariyassa \| noun \| masc.gen.sg \| of the noble ones` | Singular tag with plural gloss; DPD ariyadhamma 2 resolves the member as `ariyassa` (sg), so the gloss is the wrong cell | `\#ariyassa \| noun \| masc.gen.sg \| of the noble one` | 7 |
| sn-22/22-94.md:57 | `atthisammataṃ \| adj \| nt.nom.sg \| agreed to be existent` | Same construction with `paṇḍitānaṃ` as `natthisammataṃ` (line 46), which is tagged `(+dat)` and glossed `(by)`; this row drops both. DPD atthisammata: "deemed existent (by)" | `atthisammataṃ \| adj \| nt.nom.sg (+dat) \| agreed to be existent (by)` (follow whatever case the owner settles for line 46) | 7 |
| sn-22/22-94.md:140 | `atthisammataṃ \| adj \| nt.nom.sg \| agreed to be existent` | As line 57: tagging differs from `natthisammataṃ` | `atthisammataṃ \| adj \| nt.nom.sg (+dat) \| agreed to be existent (by)` | 7 |
| sn-22/22-94.md:157 | `atthisammataṃ \| adj \| nt.nom.sg \| agreed to be existent` | As line 57: tagging differs from `natthisammataṃ` | `atthisammataṃ \| adj \| nt.nom.sg (+dat) \| agreed to be existent (by)` | 7 |
| sn-22/22-94.md:173 | `atthisammataṃ \| adj \| nt.nom.sg \| agreed to be existent` | As line 57: tagging differs from `natthisammataṃ` | `atthisammataṃ \| adj \| nt.nom.sg (+dat) \| agreed to be existent (by)` | 7 |
| sn-22/22-94.md:185 | `atthisammataṃ \| adj \| nt.nom.sg \| agreed to be existent` | As line 57: tagging differs from `natthisammataṃ` | `atthisammataṃ \| adj \| nt.nom.sg (+dat) \| agreed to be existent (by)` | 7 |
| sn-22/22-94.md:145 | `api \| ind \| \| too` | Row not in the text: the clause is `yamahaṃ atthīti vadāmi` (line 133), with no `api`; copied from the `ahampi taṃ` clause | Delete the row | 8 |
| sn-22/22-94.md:146 | `taṃ \| pron \| nt.acc.sg \| that` | Row not in the text: `yamahaṃ atthīti vadāmi` (line 133) has no `taṃ` | Delete the row | 8 |
| sn-22/22-94.md:240 | `taṃ \| pron \| masc.acc.sg \| that; it` | Row not in the text: line 226 reads `abhisambujjhitvā abhisametvā ācikkhati` with no `taṃ` | Delete the row | 8 |
| sn-22/22-94.md:258 | `taṃ \| pron \| masc.acc.sg \| that; it` | Row not in the text: the `rūpaṃ` clause of line 226 has no `taṃ` before `ācikkhati` | Delete the row | 8 |
| sn-22/22-94.md:266–282 | `rūpaṃ \| noun \| nt.nom.sg \| form` | Rows 266–282 repeat the whole `rūpaṃ … uttānīkaroti` block of rows 248–265; the clause occurs once in line 226 | Delete rows 266–282 | 8 |
| sn-22/22-95.md:199 | `atītānāgatapaccuppannaṃ \| adj \| nt.nom.sg` | The passage (line 190) has `atītānāgatapaccuppannā`, agreeing with `vedanā`; the table copies the neuter form from the rūpa section | `atītānāgatapaccuppannā \| adj \| fem.nom.sg` | 9 |
| sn-22/22-95.md:287 | `atītānāgatapaccuppannaṃ \| adj \| nt.nom.sg` | The passage (line 278) has `atītānāgatapaccuppannā`, agreeing with `saññā` | `atītānāgatapaccuppannā \| adj \| fem.nom.sg` | 9 |
| sn-22/22-95.md:415 | `atītānāgatapaccuppannaṃ \| adj \| nt.nom.sg` | The passage (line 406) has `atītānāgatapaccuppannā`, agreeing with `saṅkhārā` (masc.nom.pl) | `atītānāgatapaccuppannā \| adj \| masc.nom.pl` | 9 |
| sn-22/22-95.md:417 | `yā \| pron \| fem.nom.sg` | The passage (line 406) has `ye dūre santike vā`, agreeing with `saṅkhārā`; the table copies `yā` from the vedanā/saññā sections | `ye \| pron \| masc.nom.pl` | 9 |
| sn-22/22-95.md:512 | `yā \| pron \| fem.nom.sg` | The passage (line 501) has `yaṃ dūre santike vā`, agreeing with `viññāṇaṃ` | `yaṃ \| pron \| nt.nom.sg` | 9 |
| sn-35/35-28.md:127 | `ādittā \| pp \| nt.nom.pl` | Agrees with `dhammā`, tagged `masc.nom.pl` on line 126; the participle must be masculine | Grammar `masc.nom.pl` | 8 |
| sn-35/35-28.md:280 | `tassa \| pron \| masc.gen.sg \| of the` | Qualifies `bhikkhusahassassa`, tagged `nt.gen.sg` on line 281; gender disagrees | Grammar `nt.gen.sg`; English `of that` | 7 |
| sn-35/35-53.md:142 | `51304 \| manoviññāṇaṃ \| noun \| nt.acc.sg` | The table jumps from `manoviññāṇaṃ` to `manosamphassaṃ` (line 143); the text's `aniccato jānato passato avijjā pahīyati, vijjā uppajjati` after `manoviññāṇaṃ` has no rows | Insert after line 142 the seven rows `aniccato` … `uppajjati` as at lines 135–141 | 8 |
| sn-35/35-53.md:169 | `ti (iti) \| ind \| \| end of direct speech` | The table ends without rows for the text's last sentence `evaṃ kho, bhikkhu, jānato evaṃ passato avijjā pahīyati, vijjā uppajjatīti` (line 122) | Insert before line 169 rows for `evaṃ`, `kho`, `bhikkhu`, `jānato`, `evaṃ`, `passato`, `avijjā`, `pahīyati`, `vijjā`, `uppajjati` | 8 |
| sn-35/35-60.md:81 | `dhamme \| noun \| masc.acc.pl \| mind objects; mental phenomena` | Text `dhamme ca uppajjati` (line 73), but no `ca` row follows `dhamme`; the eye passage has `rūpe`, `ca` (lines 34–35) | Insert row `\| \| ca \| ind \| conj \| and \| \|` after line 81 | 7 |
| sn-35/35-93.md:98 | `\| so \| pron \| masc.nom.sg \| the \|` | Text (line 82) is `sopi hetu sopi paccayo`; table goes `so`, `api`, `paccayo`, missing `hetu`, the second `so` and `api` | Insert after line 99: `\| \| hetu \| noun \| masc.nom.sg \| the cause \| \|`, `\| \| so \| pron \| masc.nom.sg \| that \| \|`, `\| \| api \| ind \| \| too; also \| \|` | 9 |
| sn-35/35-93.md:146 | `\| so \| pron \| masc.nom.sg \| the \|` | Text (line 118) is `sopi hetu sopi paccayo`; table goes `so`, `api`, `paccayo`, missing `hetu`, the second `so` and `api` | Insert after line 147: `\| \| hetu \| noun \| masc.nom.sg \| the cause \| \|`, `\| \| so \| pron \| masc.nom.sg \| that \| \|`, `\| \| api \| ind \| \| too; also \| \|` | 9 |
| sn-35/35-93.md:158 | `\| 16596 \| uppannaṃ \| pp \| nt.nom.sg \|` | Text (line 118) reads `uppanno cakkhusamphasso`; the table copies the nt form from the eye-consciousness paragraph (line 110) | `\| 16596 \| uppanno \| pp \| masc.nom.sg \|` | 9 |
| sn-35/35-93.md:161 | `\| niccaṃ \| adj \| nt.nom.sg \| permanent \|` | Text (line 118) reads `kuto nicco bhavissati` (agreeing with `cakkhusamphasso`); table has nt `niccaṃ` | `\| nicco \| adj \| masc.nom.sg \| permanent \|` | 9 |
| sn-35/35-118.md:37 | `\| 13718 \| indo \| noun \|` | Second member of `devānamindo` (:35) lacks the `\#` member marker that the first member `\#devānaṃ` (:36) has, so it reads as a separate word (DPD devānaminda: devānaṃ + inda) | `\| 13718 \| \#indo \| noun \|` | 8 |
| sn-35/35-118.md:165 | `\| \#rūpā \| noun \| masc.nom.pl \| forms \|` | Member noun `rūpa` of `piyarūpā` is neuter, as tagged at :112; masc copies the gender of `dhammā` (DPD piyarūpa: piya + rūpa; rūpa nt, but DPD also has rūpa 4 adj in comps, so check) | `\| \#rūpā \| noun \| nt.nom.pl \| forms \|` | 5 |
| sn-35/35-118.md:220 | `\| \#rūpā \| noun \| masc.nom.pl \| forms \|` | Same as :165 | `\| \#rūpā \| noun \| nt.nom.pl \| forms \|` | 5 |
| sn-35/35-230.md:120 | `\| \#rūpā \| noun \| masc.nom.pl \| forms \|` | Same as 35-118:165: member noun `rūpa` is neuter | `\| \#rūpā \| noun \| nt.nom.pl \| forms \|` | 5 |
| sn-35/35-118.md:170 | `\| \| taṃ \| pron \| masc.acc.sg \| that (them) \|` | Same `taṃ` (in `tañce`) is nt.acc.sg at :117, :178, :233; a masc sg has no referent (`dhammā` is plural) | `\| \| taṃ \| pron \| nt.acc.sg \| that (them) \|` | 6 |
| sn-35/35-118.md:225 | `\| \| taṃ \| pron \| masc.acc.sg \| that (those mental objects) \|` | Same as :170 | `\| \| taṃ \| pron \| nt.acc.sg \| that (those mental objects) \|` | 6 |
| sn-35/35-118.md:240 | `\| \| \#taṃ \| pron \| masc.acc.sg \| that (those mental objects) \|` | First member of `tannissitaṃ` is nt.acc.sg at :131 and :184; masc here | `\| \| \#taṃ \| pron \| nt.acc.sg \| that (those mental objects) \|` | 6 |
| sn-35/35-118.md:246 | `\| \| \#taṃ \| pron \| masc.acc.sg \| that (them) \|` | First member of `tadupādānaṃ` is nt.acc.sg at :136 and :189; masc here (DPD tadupādāna: tad + upādāna). The known item covers only :245 and :247, not this member row | `\| \| \#taṃ \| pron \| nt.acc.sg \| that (them) \|` | 7 |
| sn-35/35-136.md:61 | `\| 24373 \| gandhārāmā \| adj \| masc.nom.pl \| delight in smells; take pleasure in aromas \| \|` | Construction empty; the parallel `saddārāmā`, `rasārāmā`, `phoṭṭhabbārāmā`, `dhammārāmā` rows give `sattamī tappurisa` (DPD gandhārāma: sattamī tappurisa > bahubbīhi) | `\| 24373 \| gandhārāmā \| adj \| masc.nom.pl \| delight in smells; take pleasure in aromas \| sattamī tappurisa \|` | 8 |
| sn-35/35-136.md:164, :165 | `\| dhammasammudito \| adj \| masc.nom.sg \| pleased with mental objects \| sattamī tappurisa \|` | Compound label `sattamī tappurisa` contradicts its member `\#dhammehi` masc.instr.pl (:165); DPD dhammasammudita is tatiyā tappurisa (dhammehi + sammudita), so the member is right and the label is wrong | `\| dhammasammudito \| adj \| masc.nom.sg \| pleased with mental objects \| tatiyā tappurisa \|` | 8 |
| sn-35/35-136.md:167 | `\| 34920 \| dhammavipariṇāmavirāganirodhā \| adj \| masc.abl.sg \|` | Same compound at :81 is POS `noun` with construction `genitive tappurisa`; here POS `adj` and construction empty (DPD: masc, chaṭṭhī tappurisa) | `\| 34920 \| dhammavipariṇāmavirāganirodhā \| noun \| masc.abl.sg \|` and construction `genitive tappurisa` | 8 |
| sn-35/35-230.md:51 | `\| \| hi \| ind \| emph \| indeed \| \|` | Text :24 reads `evaṃ hi so, bhikkhave, maccho`, but the table has no row for `so` between `hi` (:51) and `bhikkhave` (:52) | Insert after :51: `\| \| so \| pron \| masc.nom.sg \| that \| \|` | 8 |
| sn-35/35-230.md:103 | `\| jivhāviññeyyā \| adj \| masc.nom.pl \| cognizable by the tongue; to be known by the tongue \| \|` | Compound row has an empty construction cell; its compound type sits on the member row :104, unlike every sibling row (DPD jivhāviññeyya: tatiyā tappurisa) | `\| jivhāviññeyyā \| adj \| masc.nom.pl \| cognizable by the tongue; to be known by the tongue \| tatiyā tappurisa \|` | 9 |
| sn-35/35-230.md:104 | `\| \#jivhāya \| noun \| fem.instr.sg \| by the tongue \| tatiyā tappurisa \|` | Compound type on the member row instead of the compound row :103 | `\| \#jivhāya \| noun \| fem.instr.sg \| by the tongue \| \|` | 9 |
| sn-35/35-232.md:258 | `evameva \| sandhi \| ind+ind` | Text line 253 reads `evameva kho, āvuso`; the table has no `kho` row | Insert `\| \| kho \| ind \| emph \| indeed \| \|` after line 258 | 9 |
| sn-35/35-232.md:410 | `āvuso \| ind \| masc.voc.sg` | Text line 378 reads `na mano dhammānaṃ` with no `āvuso` here; extra row (not the known `āvuso` grammar-tag item at line 97) | Delete the `āvuso` row at line 410 | 8 |
| sn-35/35-232.md:475 | `āvuso \| ind \| masc.voc.sg` | Text line 442 reads `na mano dhammānaṃ` with no `āvuso` here; extra row | Delete the `āvuso` row at line 475 | 8 |
| sn-35/35-232.md:638 | `āvuso \| ind \| masc.voc.sg` | Text line 605 reads `na mano dhammānaṃ` with no `āvuso` here; extra row | Delete the `āvuso` row at line 638 | 8 |
| sn-35/35-241.md:215 | `antopūti \| adj \| masc.nom.sg` | The text (lines 9, 179) reads plural `antopūtī bhavissatha` (subject `tumhe`); the table gives the singular form and tag (DPD: antopūti adj) | `antopūtī \| adj \| masc.nom.pl` | 8 |
| sn-35/35-241.md:160 | `\#poṇa \| adj \| masc.nom.sg` | Stem form under a masc.nom.sg tag; sibling member rows give the inflected form (`\#ninno` line 156, `\#pabbhāro` line 163); DPD poṇa 1 is an adj | `\#poṇo` | 8 |
| sn-35/35-241.md:538 | `\#labheyyaṃ \| verb \| opt.reflx.1st.sg` | `labheyyaṃ` before `upasampadaṃ` is a separate word, not a member of a sandhi/compound row, but carries the `\#` member marker (the known item on the `reflx` tag concerns the Grammar cell, not this marker) | `labheyyaṃ \| verb \| opt.reflx.1st.sg` | 8 |
| sn-35/35-241.md:604 | `\#labheyyaṃ \| verb \| opt.reflx.1st.sg` | Same: standalone word marked as a member row (the known `reflx` item concerns the Grammar cell, not this marker) | `labheyyaṃ \| verb \| opt.reflx.1st.sg` | 8 |
| sn-35/35-241.md:349 | `sahasokī \| adj \| masc.nom.sg \| grieving together \| ` | No compound type although it has member rows; DPD sahasokī: `kammadhāraya saha + sokī`; parallel `sahanandī` (line 346) is already typed `kammadhāraya` | `kammadhāraya` | 8 |
| sn-35/35-246.md:182 | `\| 36426 \| nāma \| ind \| \| \| \|` | Table row for `nāma`, but the passage it analyses (line 167: "ayaṃ kho sā, bhante, vīṇā yassā") has no `nāma`; the row also has empty Grammar and English cells | Delete the row | 8 |
| sn-35/35-246.md:283 | `depending on the belly, depending on the parchment` | Translation and table disagree: table glosses `doṇiṃ` "soundbox; body" (243) and `cammaṃ` "sound board" (246), as DPD doṇi 2 and camma 4 | `depending on the soundbox, depending on the sound board` | 7 |
| sn-35/35-246.md:326 | `\| 65197 \| \#sotāya \| noun\>adj \| fem.instr.sg \| with a current \| \|` | Compound-member row gives the inflected bahubbīhi ending of the whole word (line 324); the member is DPD sota 1.1 (masc) "current", which has no fem. form | `\| 65197 \| \#sota \| noun \| masc \| current \| \|` | 7 |
| sn-35/35-247.md:412 | `\| \| piyarūpe \| adj \| nt.loc.sg \|` | Stray copy of the `piyarūpe` row; the text (line 399) has `atha kho yo nesaṃ`, so the row for `yo` is missing (DPD ya 2.1 pron "whoever; whatever; whichever") | Replace the row with: `\| \| yo \| pron \| masc.nom.sg \| whichever; which \| \|` | 9 |
| sn-35/35-247.md:143 | `eva \| ind \| \| so` | Text (line 135) is `evameva kho`; the table has no row for `kho` (DPD kho: ind, emph) | Insert after this row: `\| \| kho \| ind \| emph \| indeed \| \|` | 8 |
| sn-35/35-247.md:210 | `\#appiya \| noun \| nt.` | DPD has no neuter noun `appiya` (appiya 1, 3 adj; appiya 2 masc "enemy"); the parallel member `#piya` (line 205) is `adj` and the compound is adj | `\#appiya \| adj \| nt \| unpleasant; disagreeable` (DPD lookup: whether ID 7110 is appiya 3) | 8 |
| sn-35/35-247.md:454 | `manāpiyesu \| adj \| nt.loc.pl` | Qualifies `dhammesu` (DPD dhamma: masc; row at line 455 masc.loc.pl); the parallel row at line 685 has masc | `manāpiyesu \| adj \| masc.loc.pl` | 9 |
| sn-35/35-247.md:456 | `amanāpiyā \| adj \| nt.nom.pl` | Qualifies `dhammā` (DPD dhamma: masc); the parallel row at line 687 has masc | `amanāpiyā \| adj \| masc.nom.pl` | 9 |
| sn-35/35-247.md:457 | `paṭikūlā \| adj \| nt.nom.pl` | Predicate of `dhammā` (DPD dhamma: masc); cf. `nappaṭikūlā` masc.nom.pl at line 689 | `paṭikūlā \| adj \| masc.nom.pl` | 9 |
| sn-35/35-247.md:457 | `paṭikūlā \| adj \| nt.nom.pl` | Text (line 427) is `amanāpiyā dhammā paṭikūlā`; the table has no row for `dhammā` (line 688 has one) | Insert before this row: `\| \| dhammā \| noun \| masc.nom.pl \| mental objects \| \|` | 8 |
| sn-35/35-247.md:710 | `kho \| ind \| emph \| indeed` | Text (line 699) is `thambhe vāti kho`; the table has no `ti (iti)` row after `vā` | Insert before this row: `\| 30431 \| ti (iti) \| ind \| \| end of direct speech \| \|` | 8 |
| sn-56/56-7.md:126 | `\| 17919 \| \#ete \| pron \| masc.nom.pl \| these \|` | Standalone word marked as a member (`#`) with no parent row; copied from the `nete` breakdown at :50. | `\| 17919 \| ete \| pron \| masc.nom.pl \| these \|` | 8 |
| sn-56/56-7.md:132 | `\| 17919 \| \#ete \| pron \| masc.nom.pl \| these \|` | Standalone word marked as a member (`#`) with no parent row. | `\| 17919 \| ete \| pron \| masc.nom.pl \| these \|` | 8 |
| sn-56/56-7.md:138 | `\| 17919 \| \#ete \| pron \| masc.nom.pl \| these \|` | Standalone word marked as a member (`#`) with no parent row. | `\| 17919 \| ete \| pron \| masc.nom.pl \| these \|` | 8 |
| sn-56/56-7.md:133 | `\| 11578 \| \#ādibrahmacariyakā \|` | In the positive passage `ādibrahmacariyakā` is a standalone word, but it keeps the `#` it had as a member of `nādibrahmacariyakā` (:58); its own members at :134–137 are therefore one level too deep. | `\| 11578 \| ādibrahmacariyakā \|`; on :134–137 change `\#\#` to `\#` and `\#\#\#` to `\#\#` | 8 |
| sn-56/56-13.md:76 | `\| 55151 \| rūpassa \| noun \| nt.gen.sg \|` | Member of `rūpupādānakkhandho` (DPD: chaṭṭhī tappurisa `rūpassa + upādānakkhandha`) lacks the `#` prefix that the parallel members carry (`#vedanāya` :81, `#saññāya` :84, `#viññāṇassa` :90). | `\| 55151 \| \#rūpassa \|` | 8 |
| sn-56/56-13.md:77 | `\| 16318 \| upādānakkhandho \| noun \| masc.nom.sg \|` | Second member of `rūpupādānakkhandho` lacks `#`; its own members at :78–79 then need `\#\#`. | `\| 16318 \| \#upādānakkhandho \|`; :78–79 `\#upādāna`/`\#khandho` → `\#\#upādāna`/`\#\#khandho` | 8 |
| sn-56/56-13.md:82 | `\| 16318 \| upādānakkhandho \| noun \| masc.nom.sg \|` | Second member of `vedanupādānakkhandho` lacks `#` (first member `#vedanāya` :81 has it). | `\| 16318 \| \#upādānakkhandho \|` | 8 |
| sn-56/56-13.md:85 | `\| 16318 \| upādānakkhandho \| noun \| masc.nom.sg \|` | Second member of `saññupādānakkhandho` lacks `#`. | `\| 16318 \| \#upādānakkhandho \|` | 8 |
| sn-56/56-13.md:88 | `\| 16318 \| upādānakkhandho \| noun \| masc.nom.sg \|` | Second member of `saṅkhārupādānakkhandho` lacks `#`. | `\| 16318 \| \#upādānakkhandho \|` | 8 |
| sn-56/56-13.md:91 | `\| 16318 \| upādānakkhandho \| noun \| masc.nom.sg \|` | Second member of `viññāṇupādānakkhandho` lacks `#`. | `\| 16318 \| \#upādānakkhandho \|` | 8 |
| sn-56/56-13.md:142 | `\| 69965 \| vuccati \| verb \| pr.pass.3rd.sg \| is called \| √vac + ya + ti \|` | The Pāḷi (:101 `Idaṃ vuccati, bhikkhave, ‘dukkhasamudayaṃ`) has `bhikkhave`; the table drops it (the parallel table at :92–96 keeps it). | Insert `\| 49868 \| bhikkhave \| noun \| masc.voc.pl \| monks \| \|` after :142 | 9 |
| sn-56/56-13.md:174 | `\| 69965 \| vuccati \| verb \| pr.pass.3rd.sg \| is called \| √vac + ya + ti \|` | The Pāḷi (:148 `Idaṃ vuccati, bhikkhave, ‘dukkhanirodhaṃ`) has `bhikkhave`; the table drops it. | Insert `\| 49868 \| bhikkhave \| noun \| masc.voc.pl \| monks \| \|` after :174 | 9 |
| sn-56/56-13.md:215 | `\| 69965 \| vuccati \| verb \| pr.pass.3rd.sg \| is called \| √vac + ya + ti \|` | The Pāḷi (:181 `Idaṃ vuccati, bhikkhave, ‘dukkhanirodhagāminī`) has `bhikkhave`; the table drops it. | Insert `\| 49868 \| bhikkhave \| noun \| masc.voc.pl \| monks \| \|` after :215 | 9 |
| sn-56/56-13.md:220 | `\| 23966 \| kho \| ind \| emph \| indeed; surely; truly \|` | The Pāḷi (:181 `Imāni kho, bhikkhave, cattāri ariyasaccāni`) has `bhikkhave`; the table drops it. | Insert `\| 49868 \| bhikkhave \| noun \| masc.voc.pl \| monks \| \|` after :220 | 9 |
| sn-56/56-21.md:103 | `\| 32908 \| Dukkhanirodhagāminiyā \| adj \| fem.gen.sg \|` | The word occurs once in the Pāḷi (:89) but has two rows (:103 without construction, :104 with). | Delete the row at :103 (capitalise :104 if the capitals convention is kept) | 9 |
| sn-56/56-31.md:213 | `\| 17896 \| etaṃ \| pron \| nt.nom.sg \| this \| \|` | Passage at :199 has `etaṃ ādibrahmacariyakaṃ etaṃ nibbidāya`; the table goes from this `etaṃ` straight to `nibbidāya` (:214), with no row for `ādibrahmacariyakaṃ` or the following `etaṃ` (the known item at :201 is about `sambodhāya`/`saṃvattanti`, not these words) | Insert after :213: `\| 11578 \| ādibrahmacariyakaṃ \| adj \| nt.nom.sg \| fundamental to the spiritual life \| kammadhāraya \|` and `\| 17896 \| etaṃ \| pron \| nt.nom.sg \| this \| \|` | 8 |
| sn-56/56-37.md:45 | `\| 49868 \| bhikkhave \| noun \| masc.voc.pl \| monks \| \|` | Passage at :36 has `bhikkhave, bhikkhuno catunnaṃ`; the table has no row for `bhikkhuno` (DPD `bhikkhuno 1` masc dat sg "for a monk") | Insert after :45: `\| \| bhikkhuno \| noun \| masc.dat.sg \| for a monk \| \|` | 8 |
| sn-56/56-37.md:50 | `\| 17896 \| etaṃ \| pron \| nt.nom.sg \| this \| \|` | Passage at :37 has `etaṃ pubbaṅgamaṃ etaṃ pubbanimittaṃ`; the table has only one `etaṃ` and no `pubbaṅgamaṃ` (DPD `pubbaṅgama 2` nt "forerunner") | Insert after :50: `\| 71833 \| pubbaṅgamaṃ \| noun \| nt.nom.sg \| forerunner (of) [lit: going before] \| dutiyā tappurisa (or kammadhāraya) \|` and `\| 17896 \| etaṃ \| pron \| nt.nom.sg \| this \| \|` | 9 |
| sn-56/56-38.md:73, 98 | `N’eva andhakāratamaṃ tadā hoti` `\| 5906 \| Andhatamaṃ \| noun \|` | Passage has `andhakāratamaṃ`, its table row at :98 has `Andhatamaṃ` (DPD `andhatama` nt; no `andhakāratama` headword) | `N’eva andhatamaṃ tadā hoti` (after CST check) | 7 |
| sn-56/56-38.md:151, 196 | `\| 5902 \| andhakāratimisā \| noun \| nt.nom.pl \| pitch black darkness \| dvanda \|` | DPD: `andhakāratimisā` fem, kammadhāraya (as at :46); the known finding cites only :46/:104, these two rows are further lines | `\| 5902 \| andhakāratimisā \| noun \| fem.nom.sg \| pitch black darkness \| kammadhāraya \|` | 9 |
| sn-56/56-38.md:68 | `\| 35345 \| na \| ind \| neg \| not \| \|` | Passage has `na utusaṃvaccharā paññāyanti`; this `na` row stands after `utusaṃvaccharā` and its members (:65–67) | Move the :68 row to before :65 | 7 |
| sn-56/56-42.md:80 | `\| 65088 \| \#sokāya (ca) \| noun \| masc.dat.sg \|` | the compound `soka-parideva-dukkha-domanass’upāyāsasaṃvattanikesu` has member rows only and no headword row, unlike `jātisaṃvattanikesu` (:65) and the `…papātaṃ` compound (:178); DPD has no headword for the compound | insert before this row: `\| \| soka-parideva-dukkha-domanass’upāyāsasaṃvattanikesu \| adj \| masc.loc.pl \| leading to grief, lamentation, suffering, dejection, [and] affliction \| catutthī tappurisa (with dvanda compounds internal) \|` | 7 |
| sn-56/56-42.md:106 | `\| 65088 \| \#sokāya (ca) \| noun \| masc.dat.sg \|` | same: no headword row for `soka-…-upāyāsasaṃvattanikesu` | insert the same headword row (masc.loc.pl) before this row | 7 |
| sn-56/56-42.md:126 | `\| 65088 \| \#sokāya (ca) \| noun \| masc.dat.sg \|` | same: no headword row for `soka-…-upāyāsasaṃvattanike` | insert `\| \| soka-parideva-dukkha-domanass’upāyāsasaṃvattanike \| adj \| masc.acc.pl \| leading to grief, lamentation, suffering, dejection, [and] affliction \| catutthī tappurisa (with dvanda compounds internal) \|` before this row | 7 |
| sn-56/56-42.md:155 | `\| 65088 \| \#sokāya (ca) \| noun \| masc.dat.sg \|` | same: no headword row for `soka-…-upāyāsasaṃvattanike` | insert the same masc.acc.pl headword row before this row | 7 |
| sn-56/56-44.md:86 | `\| \| kho \| ind \| emph \| \| \|` | row has no English gloss (and no ID); the same word at :120 and :169 is `23966`, "indeed" | `\| 23966 \| kho \| ind \| emph \| indeed \| \|` | 8 |
| sn-56/56-47.md:101 | `\| 66551 \| vassasatassa \| noun \| nt.gen.sg \| of one hundred years \| \|` | three `vassasatassa` rows (:101–103) for two words in the text (:91) | delete this row | 9 |
| sn-56/56-47.md:178 | `\| 32908 \| dukkhanirodhagāminiyā \| noun \| fem.gen.sg \| of leading to the cessation of suffering \|` | POS `noun` and gloss "of leading" here; the same ID 32908 is `adj` "leading to the cessation of suffering" in every other row (e.g. 56-42.md:59), and DPD `dukkhanirodhagāminī paṭipadā` is "adj + fem" | `\| 32908 \| dukkhanirodhagāminiyā \| adj \| fem.gen.sg \| leading to the cessation of suffering \|` | 9 |
| sn-56/56-49.md:145 | `\| parikkhīṇaṃ \| pp \| nt.acc.sg \|` | qualifies `dukkhakkhandhaṃ`, tagged masc.acc.sg at :142 (DPD dukkhakkhandha: masc) | `masc.acc.sg` | 8 |
| sn-56/56-49.md:146 | `\| pariyādinnaṃ \| pp \| nt.acc.sg \|` | qualifies `dukkhakkhandhaṃ` (masc.acc.sg, :142; DPD masc) | `masc.acc.sg` | 8 |
| mn-107-ganakamoggallanasuttam.md:112 | `\#\#kaḷevarā \| noun \| masc \| step` | Member tagged masc while the compound it heads is nt.abl.sg at lines 108 and 110; DPD `kaḷevara 3` (stair; step) is nt | `\#\#kaḷevarā \| noun \| nt.abl.sg \| step` | 8 |
| mn-107-ganakamoggallanasuttam.md:610 | `\#mattaṃ \| adj \| masc.acc.sg \| measure` | Same member of `mattaññū` is `noun \| fem.acc.sg` at line 542; DPD `mattā` fem, `mattaññū` = `mattaṃ + ñū` | `\#mattaṃ \| noun \| fem.acc.sg \| measure` | 8 |
| mn-107-ganakamoggallanasuttam.md:573 | `brahmacariya \| noun \| nt \| holy life; spiritual path \| kammadhāraya` | The text has one compound `brahmacariyānuggahāya` (DPD `brahmacariyānuggaha` masc, catutthī tappurisa); the table splits it into two top-level rows (`brahmacariya`, `anuggahāya` at line 576) with no row and no compound type for the whole. The gender of `anuggahāya` at 576 is a separate known item | Add a parent row `brahmacariyānuggahāya \| noun \| masc.dat.sg \| for assistance in the holy life \| catutthī tappurisa` and mark lines 573 and 576 as `\#` members (573–575 members one level deeper) | 8 |
| mn-107-ganakamoggallanasuttam.md:594 | `phāsuvihāro \| noun \| masc. nom.sg` | Members of the sandhi row `phāsuvihāro cā’ti` (line 593) lack the `\#` marker at lines 594, 597, 598, and the compound members at 595–596 are then one level too high | `\#phāsuvihāro`, `\#\#phāsu`, `\#\#vihāro`, `\#ca`, `\#iti` | 7 |
| mn-107-ganakamoggallanasuttam.md:270 | `seyyathāpi, brāhmaṇa, dakkho` | `brāhmaṇa` in the passage has no row in the table (lines 274–293) | Add after line 274: `\| brāhmaṇa, \| noun \| masc.voc.sg \| Brahman \| \|` (as line 258) | 8 |
| mn-107-ganakamoggallanasuttam.md:349 | `“yato kho, brāhmaṇa, bhikkhu sīlavā hoti` | `brāhmaṇa` in the passage has no row in the table (lines 353–380) | Add after line 353: `\| brāhmaṇa, \| noun \| masc.voc.sg \| Brahman \| \|` | 8 |
| mn-107-ganakamoggallanasuttam.md:384 | `‘ehi tvaṃ, bhikkhu, indriyesu` | `bhikkhu` in the passage has no row in the table (lines 388–406) | Add after line 389: `\| bhikkhu, \| noun \| masc.voc.sg \| monk! \| \|` (as line 320) | 8 |
| mn-107-ganakamoggallanasuttam.md:518 | `“yato kho, brāhmaṇa, bhikkhu indriyesu` | `brāhmaṇa` in the passage has no row in the table (lines 522–530) | Add after line 522: `\| brāhmaṇa, \| noun \| masc.voc.sg \| Brahman \| \|` | 8 |
| mn-107-ganakamoggallanasuttam.md:534 | `‘ehi tvaṃ, bhikkhu, bhojane` | `bhikkhu` in the passage has no row in the table (lines 538–548) | Add after line 539: `\| bhikkhu, \| noun \| masc.voc.sg \| monk! \| \|` | 8 |
| mn-107-ganakamoggallanasuttam.md:602 | `“yato kho, brāhmaṇa, bhikkhu bhojane` | `brāhmaṇa` in the passage has no row in the table (lines 606–618) | Add after line 606: `\| brāhmaṇa, \| noun \| masc.voc.sg \| Brahman \| \|` | 8 |
| mn-107-ganakamoggallanasuttam.md:622 | `‘ehi tvaṃ, bhikkhu, jāgariyaṃ` | `bhikkhu` in the passage has no row in the table (lines 626–629) | Add after line 626: `\| bhikkhu, \| noun \| masc.voc.sg \| monk! \| \|` | 8 |
| mn-107-ganakamoggallanasuttam.md:731 | `\| ehi tvaṃ \| verb \| imp.2nd.sg \| come you! \|` | The passage (:727) has `ehi tvaṃ, bhikkhu, satisampajaññena`; the table has no `bhikkhu` row (the parallel table has it at :819) | Add after :731: `\| bhikkhu \| noun \| masc.voc.sg \| monk \| \|` | 9 |
| mn-107-ganakamoggallanasuttam.md:954 | `\| sampajāno \| adj \| masc.nom.sg \|` | The passage (:939) has `thinamiddhā cittaṃ parisodheti`; the table has no row for the ablative `thinamiddhā` (the parallel tables have `byāpādapadosā` :933, `uddhaccakukkuccā` :972) | Add after :954: `\| thinamiddhā \| noun \| nt.abl.sg \| from dullness and drowsiness \| \|` (spelling per the decision on known finding 230) | 8 |
| mn-107-ganakamoggallanasuttam.md:1160 | `\| sukhassa ca \| noun \| nt.gen.sg \| of happiness; comfort \|` | The passage (:1156) begins `puna caparaṃ, bhikkhave, bhikkhu`; the table starts at `sukhassa ca` and has none of these three rows (the tables at :1083–1088 and :1121–1123 have them) | Add before :1160 the rows of :1121–1123 (`puna caparaṃ,`, `bhikkhave`, `bhikkhu`); or, if known finding 239 is confirmed, delete the phrase from :1156 instead | 7 |
| mn-107-ganakamoggallanasuttam.md:1320 | `\| kho \| ind \| emph \| indeed \|` | The passage (:1313) has `appekacce kho, brāhmaṇa, mama sāvakā`; the table has no `brāhmaṇa` row | Add after :1320: `\| brāhmaṇa \| noun \| masc.voc.sg \| brahman \| \|` | 9 |
| mn-107-ganakamoggallanasuttam.md:930 | `\| \#hitānukampī \| adj \| \| compassionate for the welfare of \|` | Grammar cell empty | `masc.nom.sg` | 8 |
| mn-107-ganakamoggallanasuttam.md:928 | `\| \#\#\#pāṇa \| noun \| masc. \| \|` | English cell empty | `living being (lit: breathing)` | 6 |
| mn-107-ganakamoggallanasuttam.md:839 | `\| palālapuñjan’ti \| sandhi \| \| \| \|` | English cell empty; the other sandhi rows carry a gloss (:703, :1144, :1307) | `“...a heap of straw”` | 7 |
| mn-107-ganakamoggallanasuttam.md:971 | `\| \#citto \| noun (as adj) \| masc.nom.sg \| mind; heart \|` | The same member in the parallel compound `abyāpannacitto` is given at :923 as `\#cittaṃ`, `noun (as adj in comp)`, nt.nom.sg; `citta` is neuter (DPD `citta 1.1` nt; `vūpasantacitta` = vūpasanta + citta) | `\| \#cittaṃ \| noun (as adj in comp) \| nt.nom.sg \| mind; heart \|` | 7 |
| mn-107-ganakamoggallanasuttam.md:1242 | `\| \#\#saṃyojanā \| noun \| nt.nom.pl \| fetters; chains; bonds (lit: yoking together) \|` | Member row is nom.pl while its parent `\#bhavasaṃyojanaṃ` (:1240) is nt.acc.sg "the bond" | `\| \#\#saṃyojanaṃ \| noun \| nt.acc.sg \| fetter; chain; bond (lit: yoking together) \|` | 5 |
| mn-107-ganakamoggallanasuttam.md:1554 | `ārāmarāmaṇeyyakaṃ \| noun \| \| delighfulness` | Grammar cell is empty. DPD `ārāmarāmaṇeyyaka` is nt. The known gender finding covers lines 1556–1566 only; this row is the empty cell at 1554. | `ārāmarāmaṇeyyakaṃ \| noun \| nt.acc.sg \|` | 8 |
| mn-107-ganakamoggallanasuttam.md:1565 | `\#\#pokkharaṇīnaṃ \| noun \| fem. \| of lotus ponds` | Grammar is incomplete; the parallel member rows (lines 1555, 1558, 1561) give case and number. DPD `pokkharaṇī` fem; construction `pokkharaṇīnaṃ` (gen.pl). | `\#\#pokkharaṇīnaṃ \| noun \| fem.gen.pl \| of lotus ponds` | 9 |
| mn-107-ganakamoggallanasuttam.md:1613 | `tayā \| pron \| masc.instr.sg \| by you` | Second-person pronoun tagged with a gender (DPD `tayā 1`: 2nd instr sg); lines 1576 and 1647 have `2nd.instr.sg`. | `tayā \| pron \| 2nd.instr.sg \| by you` | 9 |
| mn-107-ganakamoggallanasuttam.md:1641 | `tiṭṭhasi \| verb \| pr.2nd.sg \| you stand; you exist` | The passage (line 1624) has "tiṭṭhasi tvaṃ samādapetā"; the table has no row for `tvaṃ` (DPD `tvaṃ 1`: 2nd nom sg). | Add after this row: `\| tvaṃ \| pron \| 2nd.nom.sg \| you \| \|` | 9 |
| mn-107-ganakamoggallanasuttam.md:1643 | `atha kho pana \| idiom \| \| and yet` | The passage (line 1624) has "atha ca pana" (DPD idiom `atha ca pana`, "and yet; but still"), as does the row at line 1712. | `atha ca pana \| idiom \| \| and yet` | 9 |
| mn-107-ganakamoggallanasuttam.md:1645 | `kho \| ind \| emph \| indeed` | The passage (line 1624) has `ca` here, not `kho`. | `ca \| ind \| conj \| and` | 9 |
| mn-107-ganakamoggallanasuttam.md:1714 | `sāvakā \| noun \| masc.nom.pl \| disciples; followers` | The passage (line 1708) has "mama sāvakā mayā evaṃ ovadīyamānā"; the table has no row for `mayā` (DPD `mayā 1`: 1st instr sg). | Add after this row: `\| mayā \| pron \| 1st.instr.sg \| by me \| \|` | 9 |
| mn-107-ganakamoggallanasuttam.md:1725 | `nārādhenti \| verb \| pr.3rd.pl \| do not attain` | DPD `ārādheti`: pr, caus of ā √rādh. The same verb two rows above (line 1723, `ārādhenti`) is correctly `pr.caus.3rd.pl`; this row drops `caus`. | `nārādhenti \| verb \| pr.caus.3rd.pl \| do not attain` | 8 |
| mn-107-ganakamoggallanasuttam.md:1773 | `\#attha \| noun \| masc.abl.sg \| for the purpose (of); for the sake (of);` | The form `attha` is not an ablative singular. DPD `jīvikattha` is chaṭṭhī tappurisa > bahubbīhi (jīvikāya + attha), and the member is `attha 1.3` masc "purpose; goal"; the sibling bahubbīhi members in this file carry the plural of the whole (`\#vīriyā`, `\#cittā`). The gloss also ends in a stray `;`. | `\#atthā \| noun \| masc.nom.pl \| purpose; goal` | 7 |
| mn-107-ganakamoggallanasuttam.md:1803 | `anapekkhavanto \| adj (pp) \| +loc \|` | Gender, case and number are missing, and a `-vant` adjective is labelled `(pp)` (DPD `anapekkhavant`: adj). The positive form at line 1877 has `adj` and `masc.nom.pl (+loc)`. | `anapekkhavanto \| adj \| masc.nom.pl (+loc) \|` | 9 |
| mn-107-ganakamoggallanasuttam.md:1811 | `paviveke \| adj \| masc.loc.sg \| related to solitude` | The same word in the parallel passage (line 1888) is `noun`, "solitude; seclusion". DPD has both (`paviveka 1` masc "solitude; seclusion", `paviveka 2` adj); in "paviveke nikkhittadhurā" it is the noun. | `paviveke \| noun \| masc.loc.sg \| solitude; seclusion` | 7 |
| mn-107-ganakamoggallanasuttam.md:1818 | `\#vīriyā \| noun \| masc.nom.pl \| effort; energy; might` | DPD `vīriya` is nt; the same member at line 1892 is tagged `nt`. | `\#vīriyaṃ \| noun \| nt.nom.sg \| effort; energy; might` (or `\#vīriyāni \| noun \| nt.nom.pl` to keep the plural used by the sibling members) | 8 |
| mn-107-ganakamoggallanasuttam.md:1821 | `\#satino \| noun \| \| mindfulness; presence` | Grammar cell is empty, and `satino` is not a form of the noun `sati`: DPD `satī 2.1` adj, in comps, "with mindfulness; having presence; with awareness". The same member at line 1898 is `adj`, `masc.nom.pl`. (The known item on `muṭṭhassatino` :1819 is the compound type, another row.) | `\#satino \| adj \| masc.nom.pl \| with mindfulness; with awareness` | 8 |
| mn-107-ganakamoggallanasuttam.md:1892 | `\#vīriya \| noun \| nt.nom.pl \| energy` | The cell shows the stem `vīriya`, which is not a neuter nominative plural. | `\#vīriyaṃ \| noun \| nt.nom.sg \| energy` (or `\#vīriyāni \| noun \| nt.nom.pl \| energy` to match `\#cittā` nt.nom.pl at line 1903) | 7 |
| mn-107-ganakamoggallanasuttam.md:1895 | `\#attā \| adj \| masc.nom.pl \| self; oneself (themselves)` | `atta` "self" is a noun (DPD `atta 1.1` masc; `pahitatta` = pahita + atta); POS `adj` is wrong. | `\#attā \| noun \| masc.nom.pl \| self; oneself (themselves)` | 8 |
| mn-107-ganakamoggallanasuttam.md:1830 | `eḷamūgā \| adj \| masc.nom.pl \| stupid as sheep` | One word, two analyses: here `adj` "stupid as sheep", but `aneḷamūgā` (line 1905) is `noun` "not drivelling idiots". DPD agrees with line 1905: `eḷamūga` masc, kammadhāraya eḷā + mūga, "drooling fool; drivelling idiot"; `aneḷamūga` masc. The translation at line 1839 ("dumb as sheep") follows this row. | `eḷamūgā \| noun \| masc.nom.pl \| drooling fools; drivelling idiots`, and "drivelling idiots" for "dumb as sheep" at line 1839 | 7 |
| mn-107-ganakamoggallanasuttam.md:1909 | `saṃvasati” \| verb+ind \| pr.3rd.sg (+instr) \| lives together` | The passage (line 1841) ends "saṃvasati." with no quote mark and no `iti`; the cell and POS are carried over from line 1837. The known global item lists `saṃvasati”` only as punctuation in a Pāli cell; this row is the mismatch with the passage and the wrong POS. | `saṃvasati \| verb \| pr.3rd.sg (+instr) \| lives together` | 7 |
| mn-107-ganakamoggallanasuttam.md:1954 | `paramajjadhammesu \| sandhi \| \| highest among` | A compound (`parama` + `ajja` + `dhamma`, members at lines 1955–1957) is labelled `sandhi`, with no grammar and no compound type. Other compounds in the file carry their own POS and case. DPD has no headword `paramajjadhamma`. | `paramajjadhammesu \| noun \| masc.loc.pl \| highest among` (compound type: DPD lookup `paramajjadhamma`) | 6 |
| mn-107-ganakamoggallanasuttam.md:1987 | `vā \| ind \| conj \| or` | Extra row: the passage (line 1972) has "mūḷhassa vā maggaṃ ācikkheyya", with one `vā` (row 1985). There is no `vā` between `maggaṃ` and `ācikkheyya`. | Delete the row at line 1987 | 9 |
| mn-107-ganakamoggallanasuttam.md:2015 | `dhammo \| noun \| masc. \| the teaching; the doctrine` | Case and number missing. | `dhammo \| noun \| masc.nom.sg \| the teaching; the doctrine` | 9 |
| mn-107-ganakamoggallanasuttam.md:2049 | `\#upeta \| pp \| masc.acc.sg (+instr)` | The cell shows the stem `upeta` but is tagged `masc.acc.sg`; the other final members carry their ending (`\#gataṃ` line 2052). | `\#upetaṃ \| pp \| masc.acc.sg (+instr)` | 8 |

### C. Translation and gloss problems

| Location | Current | Problem | Suggested | Conf. |
| --- | --- | --- | --- | --- |
| sn-22/22-23.md:83 | `destruction of aversion; hatred` | The second gloss reads as plain "hatred", not "destruction of hatred" (DPD `dosakkhaya`: wearing away of ill-will; extinction of aversion) | `destruction of aversion; destruction of hatred` | 8 |
| sn-22/22-24.md:15 | `not losing desire (for); losing interest (lit: causing to fade)` | The negation is missing from the second gloss and the literal gloss of the negative `avirājayaṃ` (DPD has no headword for the form) | `not losing desire (for); not losing interest (lit: not causing to fade)` | 7 |
| sn-22/22-24.md:37 | `not losing desire (for); losing interest (lit: causing to fade)` | Same missing negation as line 15 | `not losing desire (for); not losing interest (lit: not causing to fade)` | 7 |
| sn-22/22-26.md:59 | `of volitional formations` | The table (line 49) and every other place in these files gloss `saṅkhārā` as "mental formations", which is DPD `saṅkhāra 3`, the aggregate sense | `of mental formations` | 8 |
| sn-22/22-26.md:261 | `to that extent, monks, in the world` | `athāhaṃ` = "then I" (DPD `atha 1`: then; table line 245). The translation copies line 219's "to that extent", which renders `tāva` | `then, monks, in the world` | 8 |
| sn-22/22-33.md:26 | `[is] not yours, abandon. That` | `taṃ pajahatha` has an object; "abandon." lacks it (cf. "abandon that" at :70) | `[is] not yours, abandon that. That` | 7 |
| sn-22/22-58.md:144 | `Venerable One, for us` | `bhante` is "Venerable Sir" in the table (:121), in DPD ("venerable sir") and in all other translations | `Venerable Sir, for us` | 8 |
| sn-22/22-58.md:206 | `pacchāsamannāgatā \| noun \| masc.nom.pl \| \|` | English cell is empty (DPD has no headword) | English `possessed [of it] afterwards` (as in the translation at :224) | 6 |
| sn-22/22-78.md:142 | `pāṇānaṃ \| noun \| masc.gen.pl \| living beings` | genitive plural glossed without "of" (cf. :141 "of the animals") | `of living beings` | 6 |
| sn-22/22-82.md:517 | `viññāṇakkhandhassa \| noun \| masc.nom.sg \| consciousness aggregate` | Gloss lacks the genitive "of the" used for the parallel rows (:493, :499); the known :517 item concerns the Grammar cell, this is the English cell | `of the consciousness aggregate` | 8 |
| sn-22/22-82.md:561 | `viññāṇakkhandhassa \| noun \| masc.nom.sg \| consciousness aggregate` | Gloss lacks the genitive "of the" used for the parallel rows (:537, :543) | `of the consciousness aggregate` | 8 |
| sn-22/22-82.md:231 | `**Indeed, monk, those [are] the five aggregates that are clung to` | Pāli has `ime` "these" (:213); table :217 glosses "these" | `**Indeed, monk, these [are] the five aggregates that are clung to` | 8 |
| sn-22/22-82.md:264 | `\#mūlakā \| noun\>adj \| masc.nom.pl \| masc.nom.pl` | English cell repeats the grammar tag instead of a gloss (DPD mūlaka 1 "rooted in") | `\#mūlakā \| noun\>adj \| masc.nom.pl \| rooted in` | 9 |
| sn-22/22-82.md:327 | `\| \| taṃ \| pron \| nt.nom.sg \| the \| \|` | `taṃ` glossed "the"; DPD ta 1.1 "that"; translation :332 has "that" | `\| \| taṃ \| pron \| nt.nom.sg \| that \| \|` | 8 |
| sn-22/22-82.md:63 | `\#migāramātuyā \| noun \| fem.gen.sg \| in Migāra's Mothers` | Gen.sg member (DPD migāramātupāsāda: chaṭṭhī tappurisa migāramātuyā + pāsāda) glossed with locative "in"; apostrophe missing in "Mothers"; the known item is :65 `##mātuyā` Grammar cell | `of Migāra's mother` | 9 |
| sn-22/22-102.md:20 | `\#aniccassa \| noun \| nt.gen.sg \| \|` | English cell empty | `\#aniccassa \| noun \| nt.gen.sg \| of the impermanent \|` | 8 |
| sn-22/22-102.md:76 | `\#aniccassa \| noun \| nt.gen.sg \| \|` | English cell empty | `\#aniccassa \| noun \| nt.gen.sg \| of the impermanent \|` | 8 |
| sn-22/22-102.md:175 | `\#aniccassa \| noun \| nt.gen.sg \| \|` | English cell empty | `\#aniccassa \| noun \| nt.gen.sg \| of the impermanent \|` | 8 |
| sn-22/22-102.md:105 | `perception of the impermanent, monks, developed` | Second "monks" has no Pāḷi counterpart; the clause has one `bhikkhave`, already rendered after "in the same way" | `perception of the impermanent, developed` | 7 |
| sn-22/22-102.md:196 | `perception of the impermanent, monks, developed` | Same as line 105: "monks" rendered twice for one `bhikkhave` | `perception of the impermanent, developed` | 7 |
| sn-35/35-53.md:171 | `ignorance is abandoned [and] knowledge arises.**` | The translation omits the closing sentence `evaṃ kho, bhikkhu, jānato evaṃ passato avijjā pahīyati, vijjā uppajjatīti` | Append before `**`: ` Thus, monk, for one knowing thus, for one seeing thus, ignorance is abandoned [and] knowledge arises.` | 8 |
| sn-35/35-28.md:45 | `nt.instr.sg \| one thousand monks` | Gloss drops the instrumental sense of `bhikkhusahassena` (after `saddhiṃ`); English cell only, the known item on this line is the compound-type cell | `with one thousand monks` | 6 |
| sn-35/35-93.md:98 | `\| so \| pron \| masc.nom.sg \| the \|` | `so` (correlative of `yo`) glossed "the"; DPD `so 1.1`: "he; that person; that thing" | `that` | 7 |
| sn-35/35-93.md:146 | `\| so \| pron \| masc.nom.sg \| the \|` | `so` (correlative of `yo`) glossed "the"; DPD `so 1.1`: "he; that person; that thing" | `that` | 7 |
| sn-35/35-118.md:126 | `is delighting (in); is finding pleasure (in)` | Present participle glossed as a finite verb; the translation (:144) has "delighting in them"; DPD abhinandanta: "delighting (in); … finding pleasure (in)" | `delighting (in); finding pleasure (in)` | 8 |
| sn-35/35-118.md:179 | `is delighting (in); is finding pleasure (in)` | Same as :126; translation :197 has "delighting in them" | `delighting (in); finding pleasure (in)` | 8 |
| sn-35/35-136.md:70 | `delight in mental objects; phenomena` | Second gloss is a bare noun, not a gloss of `dhammārāmā` | `delight in mental objects; delight in phenomena` | 6 |
| sn-35/35-136.md:160 | `\| \| dhammarato \| adj \| masc.nom.sg \| is delighted (with) \|` | Compound gloss leaves out its first member; cf. `rūparato` "is delighted with forms" at :124; DPD dhammarata 2: "taking pleasure in mental phenomena" | `\| \| dhammarato \| adj \| masc.nom.sg \| is delighted with mental objects \|` | 8 |
| sn-35/35-228.md:105 | `\| \| \#dhammehi \| noun \| masc.instr.pl \| of/by forms \|` | Gloss copied from the eye section (:63); `dhammehi` is mental objects. The known item (`35-228:97`) covers the translation, not this table gloss | `\| \| \#dhammehi \| noun \| masc.instr.pl \| of/by mental objects \|` | 8 |
| sn-35/35-228.md:48 | `The ocean, the ocean, monks, the unlearned worldling speaks.` | Reads as if the worldling speaks the ocean; `bhāsati` here means "says/speaks of" with the quoted word as object (DPD bhāsati 1.1: "speaks; talks (about); says") | `The unlearned worldling, monks, speaks of the ocean, the ocean.` | 6 |
| sn-35/35-232.md:208 | `vadamāno \| prp \| masc.nom.sg \| be speaking` | Present participle glossed as an infinitive phrase; DPD vadamāna: "speaking; saying" | `speaking` | 8 |
| sn-35/35-232.md:251 | `But [rather] the harness by which they are yoked together` | Translation drops `ekena` and `yottena vā` (one harness or yoke-tie) | `But [rather] the one harness or yoke-tie by which they are yoked together` | 6 |
| sn-35/35-232.md:376 | `– the living of the spiritual life is clearly known` | `tasmā` (DPD tasmā 2: "therefore") is not translated | `– therefore the living of the spiritual life is clearly known` | 8 |
| sn-35/35-232.md:439 | `– the living of the spiritual life is clearly known` | `tasmā` (DPD tasmā 2: "therefore") is not translated | `– therefore the living of the spiritual life is clearly known` | 8 |
| sn-35/35-232.md:451 | `it can be understood; it to be known` | Second gloss is ungrammatical English | `it can be understood; it is to be known` | 7 |
| sn-35/35-232.md:614 | `it can be understood; it to be known` | Second gloss is ungrammatical English | `it can be understood; it is to be known` | 7 |
| sn-35/35-241.md:183 | `evameva \| sandhi \| ind+ind \| just as` | `evameva` is "just so; in the same way" (the correlative of `yathā`), not "just as"; DPD evameva: "similarly; in the same way; so too; just so"; the translation (line 238) says "Just so" | `just so; in the same way; similarly` | 8 |
| sn-35/35-241.md:238 | `thus, indeed, monks, you will be slanting toward nibbāna` | "indeed" renders `hi`, which is in the log sentence (`evaṃ hi so`, line 107) but not here (`evaṃ tumhe, bhikkhave`, line 179) | `thus, monks, you will be slanting toward nibbāna` | 7 |
| sn-35/35-246.md:216 | `Enough for me with that lute, good man.` | `bho` addresses the same people told `āharatha` (2nd pl); line 165 renders it "men" | `Enough for me with that lute, good men.` | 7 |
| sn-35/35-246.md:426 | `do not occur to him` | `tampi tassa na hoti` (sg; DPD tampi "even that"): `pi` not rendered, verb made plural | `even that does not occur to him` | 7 |
| sn-35/35-247.md:183 | `would get a speaker` | `labhati` is present tense (row at line 156: pr.3rd.sg; DPD labhati 1 pr "gets; receives; obtains"), not optative | `gets a speaker` | 8 |
| sn-35/35-247.md:194 | `\| ca \| ind \| conj \| \| \|` | English cell empty; every other `ca` row has "and" (DPD ca 2.1 conj "and; both") | `\| ca \| ind \| conj \| and \| \|` | 8 |
| sn-35/35-247.md:602 | `fasten (to)` | Gloss of an optative lacks "would" (cf. `would bind` for `bandheyya`) | `would fasten (to)` | 7 |
| sn-56/56-1.md:58 | `cessation of suffering; stress` | Second gloss incomplete; cf. `source of suffering; source of stress` (line 51); DPD dukkhanirodha "end of suffering; cessation of distress" | `cessation of suffering; cessation of stress` | 7 |
| sn-56/56-1.md:115 | `cessation of suffering; stress` | Second gloss incomplete | `cessation of suffering; cessation of stress` | 7 |
| sn-56/56-13.md:76 | `\| rūpassa \| noun \| nt.gen.sg \| matter; material thing \|` | Genitive glossed without "of", unlike the parallel members (`of feeling`, `of perception`, `of consciousness`). | `of matter; of material thing` | 8 |
| sn-56/56-31.md:67 | `\| 51429 \| mayā \| pron \| 1st.instr.sg \| with my \|` | `mayā` is the agent of `gahitāni` ("by me"; DPD `mayā 1` "by me; with me"), not "with my"; cf. :120 | `by me` | 8 |
| sn-56/56-31.md:121 | `directly knowing; understanding experientially; has been directly known` | An absolutive is active; "has been directly known" is a passive gloss not in DPD (`abhiññāya` ger: "directly knowing; understanding experientially") | `directly knowing; understanding experientially` | 8 |
| sn-56/56-37.md:59 | `Just so, monks, this is the forerunner` | `bhikkhuno` ("for a monk") is not translated | `Just so, monks, for a monk this is the forerunner` | 8 |
| sn-56/56-42.md:182 | `they fall down from the precipice of birth` | table glosses `papatanti` as "fall down (into)" with `…papātaṃ` acc (DPD papatati 2: "falls (into)"); "from" reverses the sense (they fall into the precipice) | `they fall down into the precipice of birth` (and "into" for the three following clauses) | 8 |
| sn-56/56-42.md:259 | `they do not fall down from the precipice of birth` | same: `nappapatanti` glossed "do not fall down (into)" (DPD nappapatati: "does not fall (into)") | `they do not fall down into the precipice of birth` (and "into" for the three following clauses) | 8 |
| sn-56/56-44.md:54 | `(lit: it is not possible [that] this exists)` | the "lit." repeats the free rendering; the table glosses `ṭhānaṃ` "reason; ground" (DPD ṭhāna 02 "reason; grounds") and `vijjati` "exists" | `(lit: this ground does not exist)` | 6 |
| sn-56/56-47.md:167 | `\| \#dubbalassa \| noun \| nt.gen.sg \| the weak one \|` | genitive glossed without "of"; other genitive members are glossed "of …" (e.g. :161) | `of the weak one` | 7 |
| mn-107-ganakamoggallanasuttam.md:242 | `\#eva \| ind \| emph \| thus` | `eva` glossed "thus", which is the gloss of `evaṃ` on the line above; DPD `eva 1` "only; just; merely"; elsewhere in the file "even; only" / "just; only" (lines 558, 565) | `\#eva \| ind \| emph \| just; only` | 8 |
| mn-107-ganakamoggallanasuttam.md:266 | `makes known; declares; prepares, define` | Infinitive `paññapetuṃ` glossed with finite present forms; DPD `paññapetuṃ` "to define; to delineate; to describe"; line 247 has the infinitive gloss | `to define; delineate; describe (lit: to make known)` | 9 |
| mn-107-ganakamoggallanasuttam.md:579 | `\#purāṇaṃ \| adj \| fem.acc.sg \| old; former and` | Member gloss still carries "and", which belongs to the `\#ca` row (line 580) | `old; former` | 8 |
| mn-107-ganakamoggallanasuttam.md:584 | `\#navaṃ \| adj \| fem.acc.sg \| new, fresh and` | Member gloss still carries "and", which belongs to the `\#ca` row (line 585) | `new, fresh` | 8 |
| mn-107-ganakamoggallanasuttam.md:600 | `it will be for my living blameless[ly] and in ease.` | `yātrā ca me bhavissati` (line 588 "way; means; support"; DPD `yātrā 1` "means of sustaining") is not translated; three things are listed in the Pāli (`yātrā`, `anavajjatā`, `phāsuvihāro`), two in the English | `and I will have sustenance, blamelessness and living in ease.` | 7 |
| mn-107-ganakamoggallanasuttam.md:779 | `urinating and defecating` | Order reversed against the Pāḷi `uccārapassāva`, the table gloss at :772 and DPD `uccārapassāvakamma` ("defecating and urinating") | `defecating and urinating` | 8 |
| mn-107-ganakamoggallanasuttam.md:958 | `he dwells with a mind free from dullness and drowsiness` | `vigatathinamiddho` describes the monk; "with a mind" is not in the Pāḷi (carried over from `vigatābhijjhena cetasā`, :911) | `he dwells free from dullness and drowsiness` | 6 |
| mn-107-ganakamoggallanasuttam.md:1261 | `\| satisampajaññāya \| noun \| nt.dat.sg \| mindful attentiveness \| dvanda \|` | The dative is not rendered ("for"); the gloss itself matches DPD `satisampajañña` ("mindful attentiveness") | `for mindful attentiveness` | 6 |
| mn-107-ganakamoggallanasuttam.md:1335 | `attain the unchanging [goal] — nibbāna` | `accantaṃ niṭṭhaṃ` is glossed "final; complete; ultimate; absolute" + "aim; goal" (:1328–1329) and translated "final goal" at :1311; "unchanging" is not among the glosses | `attain the final goal — nibbāna` | 5 |
| mn-107-ganakamoggallanasuttam.md:1390 | `attain the unchanging goal — nibbāna` | Same: "unchanging" against "final" at :1311 and the glosses at :1383 | `attain the final goal — nibbāna` | 5 |
| mn-107-ganakamoggallanasuttam.md:1432 | `as it would be acceptable to you). Are you competent in` | "taṃ kiṃ maññasi, brāhmaṇa" (table rows 1419–1422; DPD idiom `taṃ kiṃ maññasi` "what do you think about that?") is not translated. | `as it would be acceptable to you). What do you think, brahman, are you competent in` | 8 |
| mn-107-ganakamoggallanasuttam.md:1442 | `rājagahagāmissa \| adj \| masc.gen.sg \| in the way/road to Rājagaha` | The gloss includes "way/road", which belongs to `maggassa` (line 1446). DPD `rājagahagāmī`: "going to Rājagaha"; the same word at line 1425 is "(in) going to Rājagaha". | `rājagahagāmissa \| adj \| masc.gen.sg \| (in) going to Rājagaha` | 8 |
| mn-107-ganakamoggallanasuttam.md:1562 | `\#rāmaṇeyyakaṃ \| adj \| masc.acc.sg \| delighfulness of a place; lovlineness of an area` | The member row repeats the gloss of the whole compound (line 1560), with its misspellings. DPD `rāmaṇeyyaka 2`: "delightfulness; loveliness"; the same member at lines 1556 and 1559 is "delightfulness; pleasantness". | `\#rāmaṇeyyakaṃ \| adj \| masc.acc.sg \| delightfulness; pleasantness` | 8 |
| mn-107-ganakamoggallanasuttam.md:1564 | `\#pokkharaṇīrāmaṇeyyakaṃ \| adj \| masc.acc.sg \| delightful as a lotus pond` | The gloss is a simile ("delightful as"), which contradicts the row above it (line 1563) and the compound type in the same row. DPD `pokkharaṇīrāmaṇeyyaka`: chaṭṭhī tappurisa, "delightfulness of a lotus pond; loveliness of a lotus pool". | `\#pokkharaṇīrāmaṇeyyakaṃ \| adj \| masc.acc.sg \| delightfulness of a lotus pond` | 8 |
| mn-107-ganakamoggallanasuttam.md:1727 | `some attain the unchanging nibbāna and some do not` | "accantaṃ niṭṭhaṃ" is glossed in the table (lines 1720–1721) as "final; complete; ultimate" + "aim; goal" (DPD `accanta 1`, `niṭṭhā 2`); "unchanging" matches neither, and "goal" is left out. | `some attain the ultimate goal, nibbāna, and some do not` | 8 |
| mn-107-ganakamoggallanasuttam.md:1767 | `\#ime \| pron \| masc.nom.pl \| those` | `ime` is the near demonstrative (DPD `ima 1.1`: "this"), so "these"; the sandhi row above (line 1765) repeats the error ("whoever of those"). | `\#ime \| pron \| masc.nom.pl \| these` (and line 1765 "whoever of these") | 8 |
| mn-107-ganakamoggallanasuttam.md:1922 | `fragrant root(s) \| kammadhāraya` | DPD `mūlagandha`: chaṭṭhī tappurisa, "root fragrance; scent of root"; the head is `gandha` (line 1924, "the scents"). "Fragrant roots" makes `mūla` the head. The known item at this line is the grammar cell, not this one. | `root fragrance(s); scent(s) of roots \| chaṭṭhī tappurisa` | 8 |
| mn-107-ganakamoggallanasuttam.md:1933 | `fragrant heartwood(s) \| kammadhāraya` | DPD `sāragandha`: chaṭṭhī tappurisa (sārassa + gandha), "fragrant hardwood; scent of heartwood". The compound type is wrong; the gloss is DPD's first sense and can stay. The known item at this line is the grammar cell, not this one. | `fragrant heartwood(s); scent(s) of heartwood \| chaṭṭhī tappurisa` | 8 |

### D. English typos and grammar

| Location | Current | Problem | Suggested | Conf. |
| --- | --- | --- | --- | --- |
| sn-22/22-24.md:22 | `Monks, One not directly knowing` | Capital letter in the middle of a sentence | `Monks, one not directly knowing` | 9 |
| sn-22/22-26.md:88 | `**indeed, whichever pleasure` | The sentence starts with a lower-case letter | `**Indeed, whichever pleasure` | 9 |
| sn-22/22-33.md:87 | `leave(s)` | Plural of "leaf" misspelt (DPD `palāsa 1.1` "leaf; foliage") | `leaf (leaves)` | 9 |
| sn-22/22-58.md:126 | `relying on the Blessed one` | "One" lower case; "Blessed One" everywhere else | `relying on the Blessed One` | 9 |
| sn-22/22-59.md:200 | `change; alternation` | "alternation" for "alteration" (DPD `vipariṇāma` "change; alteration; transformation") | `change; alteration` | 8 |
| sn-22/22-63.md:234 | `[vi + √har + a + nta` | stray opening bracket | `vi + √har + a + nta` | 9 |
| sn-22/22-63.md:198 | `in brief. one clinging to form` | sentence starts lower case | `in brief. One clinging to form` | 9 |
| sn-22/22-63.md:101 | `whats the reason?` | missing apostrophe | `what's the reason?` | 9 |
| sn-22/22-63.md:220 | `Blessed Ones statement` | missing apostrophe | `Blessed One's statement` | 9 |
| sn-22/22-63.md:260 | `by ones own` | missing apostrophe | `by one's own` | 9 |
| sn-22/22-63.md:263 | `with ones own eyes` | missing apostrophe (DPD sacchi: "with one's own eyes"). English cell only; the known item on this line concerns the POS cell | `with one's own eyes` | 9 |
| sn-22/22-78.md:185 | `masc.gen.p` | grammar tag typo | `masc.gen.pl` | 9 |
| sn-22/22-78.md:148 | `of might power` | typo | `of mighty power` | 8 |
| sn-22/22-78.md:307 | `of might power` | typo | `of mighty power` | 8 |
| sn-22/22-78.md:46 | `lions roar` | missing apostrophe | `lion's roar` | 9 |
| sn-22/22-78.md:50 | `lions roar` | missing apostrophe | `lion's roar` | 9 |
| sn-22/22-78.md:55 | `he roars a lions roar three times; having roared a lions roar` | missing apostrophe (twice) | `he roars a lion's roar three times; having roared a lion's roar` | 9 |
| sn-22/22-78.md:132 | `[√palā + \*aya + ti` | stray opening bracket | `√palā + \*aya + ti` | 8 |
| sn-22/22-82.md:194 | `from clinging-aggregate; aggregate of form that is clung to` | "from" is a typo for "form" | `form clinging-aggregate; aggregate of form that is clung to` | 8 |
| sn-22/22-82.md:222 | `from clinging-aggregate; aggregate of form that is clung to` | "from" is a typo for "form" | `form clinging-aggregate; aggregate of form that is clung to` | 8 |
| sn-22/22-82.md:266 | `Certainly, Monk, these five aggregates` | Capital "Monk" mid-sentence; lower case elsewhere | `Certainly, monk, these five aggregates` | 7 |
| sn-22/22-82.md:349 | `bhagavā avoca —idha, bhikkhu` | Missing space after em dash (cf. :29 `avoca — idha`) | `bhagavā avoca — idha, bhikkhu` | 8 |
| sn-22/22-82.md:600 | `attato \| ind \| abv (abl.sg)` | Typo `abv` for `adv` | `attato \| ind \| adv (abl.sg)` | 8 |
| sn-22/22-82.md:615 | `attato \| ind \| abv (abl.sg)` | Typo `abv` for `adv` | `attato \| ind \| adv (abl.sg)` | 8 |
| sn-22/22-82.md:661 | `attato \| ind \| abv (abl.sg)` | Typo `abv` for `adv` | `attato \| ind \| adv (abl.sg)` | 8 |
| sn-22/22-82.md:683 | `attato \| ind \| abv (abl.sg)` | Typo `abv` for `adv` | `attato \| ind \| adv (abl.sg)` | 8 |
| sn-22/22-82.md:62 | `in Migāra's Mothers mansion` | Missing possessive apostrophe | `in Migāra's Mother's mansion` | 8 |
| sn-22/22-82.md:95 | `in Migāra's Mothers mansion` | Missing possessive apostrophe | `in Migāra's Mother's mansion` | 8 |
| sn-22/22-94.md:131 | `permanent, stable. eternal` | Full stop inside a list | `permanent, stable, eternal` | 9 |
| sn-22/22-94.md:131 | `I too, say [of] that: It does not exist` | Missing comma; elsewhere `I, too, say` | `I, too, say [of] that: It does not exist` | 8 |
| sn-22/22-94.md:195 | `I too, say [of] that: It exists. This` | Missing comma; elsewhere `I, too, say` | `I, too, say [of] that: It exists. This` | 8 |
| sn-22/22-94.md:195 | `with changing nature, agreed to be existent by the wise in the world; I, too,` | Main verb missing; line 131 has `[is] agreed` | `with changing nature, [is] agreed to be existent by the wise in the world; I, too,` | 7 |
| sn-22/22-95.md:95 | `A man with eyes, would see [it]` | Comma between subject and verb | `A man with eyes would see [it]` | 8 |
| sn-22/22-95.md:188 | `A man with eyes, would see [this]` | Comma between subject and verb | `A man with eyes would see [this]` | 8 |
| sn-22/22-95.md:276 | `A man with eyes, would see [this]` | Comma between subject and verb | `A man with eyes would see [this]` | 8 |
| sn-22/22-95.md:404 | `A man with eyes, would see [it]` | Comma between subject and verb | `A man with eyes would see [it]` | 8 |
| sn-22/22-95.md:499 | `A man with eyes, would see [this]` | Comma between subject and verb | `A man with eyes would see [this]` | 8 |
| sn-22/22-95.md:188 | `ceases, A man with eyes` | Comma before a new sentence with a capital | `ceases. A man with eyes` | 8 |
| sn-22/22-95.md:404 | `(leaf roll); He, unrolling` | Semicolon before a new sentence with a capital | `(leaf roll). He, unrolling` | 7 |
| sn-22/22-95.md:460 | `magicians apprentice` | Missing possessive apostrophe | `magician's apprentice` | 8 |
| sn-22/22-95.md:499 | `a magicians apprentice` | Missing possessive apostrophe | `a magician's apprentice` | 8 |
| sn-22/22-102.md:28 | `lust in regard for sensual pleasure` | Wrong preposition; sibling rows say "in regard to" | `lust in regard to sensual pleasure` | 7 |
| sn-22/22-102.md:83 | `lust in regard for sensual pleasure` | Wrong preposition | `lust in regard to sensual pleasure` | 7 |
| sn-22/22-102.md:180 | `lust in regard for sensual pleasure` | Wrong preposition | `lust in regard to sensual pleasure` | 7 |
| sn-22/22-102.md:211 | `lust in regard for sensual pleasure` | Wrong preposition | `lust in regard to sensual pleasure` | 7 |
| sn-22/22-102.md:257 | `lust in regard for sensual pleasure` | Wrong preposition | `lust in regard to sensual pleasure` | 7 |
| sn-35/35-60.md:58 | `vedanāya+api \| nou` | POS typo `nou` | `noun` | 9 |
| sn-35/35-60.md:105 | `vedanāya+api \| nou` | POS typo `nou` | `noun` | 9 |
| sn-35/35-60.md:71 | `fully understood by me....**` | Four full stops | `fully understood by me…**` | 6 |
| sn-35/35-28.md:41 | `at Gayas Head` | Missing apostrophe | `at Gaya's Head` | 8 |
| sn-35/35-28.md:85 | `at Gayas Head` | Missing apostrophe | `at Gaya's Head` | 8 |
| sn-35/35-28.md:85 | `And, what, monks [is] the all` | Comma after `And` misplaced; vocative not closed by a comma | `And what, monks, [is] the all` | 7 |
| sn-35/35-28.md:268 | `of ones own` | Missing apostrophe; English cell only, the known item on this line is the POS `masc` | `of one's own` | 8 |
| sn-35/35-28.md:172 | `troubles, I say**` | Translation paragraph ends without a full stop | `troubles, I say.**` | 7 |
| sn-35/35-70.md:61 | `Blessed One….Seated` | No space after the ellipsis, so the next sentence runs on | `Blessed One… Seated` | 9 |
| sn-35/35-70.md:250 | `there doesnt exist` | Missing apostrophe in `doesnt` | `there does not exist` | 9 |
| sn-35/35-70.md:275 | `there doesnt exist` | Missing apostrophe in `doesnt` | `there does not exist` | 9 |
| sn-35/35-70.md:327 | `there doesnt exist` | Missing apostrophe in `doesnt` | `there does not exist` | 9 |
| sn-35/35-70.md:352 | `there doesnt exist` | Missing apostrophe in `doesnt` | `there does not exist` | 9 |
| sn-35/35-118.md:127 | `abhi + √vad + a + nta]` | Stray closing bracket in construction | `abhi + √vad + a + nta` | 9 |
| sn-35/35-118.md:180 | `abhi + √vad + a + nta]` | Stray closing bracket in construction | `abhi + √vad + a + nta` | 9 |
| sn-35/35-136.md:77 | `[√ram + ta` | Stray opening bracket in construction (`√ram + ta` at :44) | `√ram + ta` | 9 |
| sn-35/35-228.md:82 | `with sharks(s)` | Doubled plural | `with shark(s)` | 9 |
| sn-35/35-228.md:124 | `with sharks(s)` | Doubled plural | `with shark(s)` | 9 |
| sn-35/35-230.md:31 | `bait-gone- hook` | Stray space inside hyphenated gloss | `bait-gone-hook` | 8 |
| sn-35/35-230.md:81 | `masc.nompl` | Tag typo (missing full stop) | `masc.nom.pl` | 9 |
| sn-35/35-232.md:59 | `(lit: in sages landing)` | Missing possessive apostrophe | `(lit: in sages' landing)` | 7 |
| sn-35/35-232.md:113 | `How is it, friend Sāriputta [that]` | Missing comma after the vocative | `How is it, friend Sāriputta, [that]` | 6 |
| sn-35/35-232.md:123 | `koṭṭhika \| noun \| masc.voc.sg \| koṭṭhika` | Proper name in the English column is lower case | English cell `Koṭṭhika` | 8 |
| sn-35/35-232.md:168 | `Friend, Koṭṭhika,` | Comma splits the vocative "friend Koṭṭhika" | `Friend Koṭṭhika,` | 8 |
| sn-35/35-232.md:186 | `tie of a plowmans yoke` | Missing possessive apostrophe (DPD yotta 2: "tie of a plough's yoke") | `tie of a plowman's yoke` | 9 |
| sn-35/35-232.md:188 | `[saṃ + √yuj + ta` | Stray opening bracket in the construction | `saṃ + √yuj + ta` | 9 |
| sn-35/35-232.md:212 | `tie of a plowmans yoke` | Missing possessive apostrophe | `tie of a plowman's yoke` | 9 |
| sn-35/35-232.md:244 | `tie of a plowmans yoke` | Missing possessive apostrophe | `tie of a plowman's yoke` | 9 |
| sn-35/35-232.md:246 | `[saṃ + √yuj + ta` | Stray opening bracket in the construction | `saṃ + √yuj + ta` | 9 |
| sn-35/35-232.md:602 | `desire- and-lust` … `desire- and- lust` | Broken hyphenation; the rest of the line has `desire-and-lust` | `desire-and-lust` | 9 |
| sn-35/35-241.md:164 | `whats the reason for that?` | Missing apostrophe | `what's the reason for that?` | 9 |
| sn-35/35-241.md:229 | `whats the reason for that?` | Missing apostrophe | `what's the reason for that?` | 9 |
| sn-35/35-241.md:664 | `by ones own` | Missing apostrophe | `by one's own` | 9 |
| sn-35/35-241.md:667 | `with ones own eyes; personal` | Missing apostrophe | `with one's own eyes; personal` | 9 |
| sn-35/35-247.md:164 | `behaving like his (lit: such behavior)` | Typo: "his" for "this" (cf. `acting like this` at line 161; DPD evaṃsamācāra "behaving like this"). The known item at this line concerns the Construction cell, not the gloss | `behaving like this (lit: such behavior)` | 9 |
| sn-35/35-247.md:196 | `lack of restrain; non-restraint` | Typo: "restrain" for "restraint" (cf. line 179) | `lack of restraint; non-restraint` | 9 |
| sn-35/35-247.md:261 | `is troubled;is vexed` | Missing space after semicolon (cf. line 213) | `is troubled; is vexed` | 9 |
| sn-56/56-7.md:53 | `profitable; beneficial lit (lit: connected with benefit)` | Stray `lit` before the bracket. | `profitable; beneficial (lit: connected with benefit)` | 9 |
| sn-56/56-7.md:129 | `profitable; beneficial lit (lit: connected with benefit)` | Stray `lit` before the bracket. | `profitable; beneficial (lit: connected with benefit)` | 9 |
| sn-56/56-13.md:98 | `It should be answered: ‘The five aggregates of clinging;` | Opening quote is never closed. | Close after the list: `…the aggregate of consciousness that is clung to.’ This is called…` | 7 |
| sn-56/56-13.md:98 | `This is called, monks, ‘the noble truth of suffering.**` | Opening quote is never closed. | `This is called, monks, ‘the noble truth of suffering.’**` | 8 |
| sn-56/56-13.md:146 | `This is called, monks, the ‘noble truth of the origin of suffering.**` | Opening quote placed after `the` and never closed. | `This is called, monks, ‘the noble truth of the origin of suffering.’**` | 8 |
| sn-56/56-13.md:178 | `This is called, monks, the ‘noble truth of the cessation of suffering.**` | Opening quote placed after `the` and never closed. | `This is called, monks, ‘the noble truth of the cessation of suffering.’**` | 8 |
| sn-56/56-13.md:224 | `This is called, monks, ‘the noble truth of the way leading to the cessation of suffering.` | Opening quote is never closed. | `This is called, monks, ‘the noble truth of the way leading to the cessation of suffering.’` | 8 |
| sn-56/56-25.md:64, 98 | `for one seeing, ‘This [is]` | Each `‘This [is] …` quote (twice on :64, twice on :98) is opened and never closed. | Close each quote, e.g. `‘This [is] suffering’, [that]`, `‘This [is] the origin of suffering’, [that]`, `‘This [is] the cessation of suffering’, [that]`, `‘This [is] the way leading to the cessation of suffering’, [that]` | 8 |
| sn-56/56-33.md:90 | `suffering…the noble truth` | No spaces around the ellipsis | `suffering … the noble truth` | 7 |
| sn-56/56-27.md:53 | `they are called ‘noble truths.**` | Unclosed quote in the translation | `they are called ‘noble truths’.**` | 8 |
| sn-56/56-28.md:42 | `they are called ‘noble truths.**` | Unclosed quote in the translation | `they are called ‘noble truths’.**` | 8 |
| sn-56/56-42.md:80 | `grief; sorrow sadness` | missing separator between glosses | `grief; sorrow; sadness` | 9 |
| sn-56/56-42.md:106 | `grief; sorrow sadness` | missing separator between glosses | `grief; sorrow; sadness` | 9 |
| sn-56/56-42.md:126 | `grief; sorrow sadness` | missing separator between glosses | `grief; sorrow; sadness` | 9 |
| sn-56/56-42.md:155 | `grief; sorrow sadness` | missing separator between glosses | `grief; sorrow; sadness` | 9 |
| sn-56/56-42.md:89 | `as it truly is: ‘This is suffering’: ‘This is the origin of suffering’: ‘This is the cessation of suffering’;` | colons used as list separators between the four quoted truths, then a semicolon | `as it truly is: ‘This is suffering’; ‘This is the origin of suffering’; ‘This is the cessation of suffering’;` | 7 |
| sn-56/56-42.md:136 | `dejection, [and] affliction; [And] they construct` | capital after a semicolon mid-sentence | `dejection, [and] affliction; [and] they construct` | 8 |
| sn-56/56-47.md:3 | `Seyyathāpi, bhikkhave, puriso mahāsamudde` | the speech closes with `paveseyyā”ti?` but has no opening quote | `“Seyyathāpi, bhikkhave, puriso mahāsamudde` | 6 |
| sn-56/56-47.md:7 | `Yadi nūna, bhante, kadāci` | closes with `accayenā”ti.` but has no opening quote | `“Yadi nūna, bhante, kadāci` | 6 |
| sn-56/56-47.md:23 | `Seyyathāpi, bhikkhave, puriso mahāsamudde` | no opening quote for the speech closed by `paveseyyā”ti?` | `“Seyyathāpi, bhikkhave, puriso mahāsamudde` | 6 |
| sn-56/56-47.md:75 | `Yadi nūna, bhante, kadāci` | no opening quote for the speech closed by `accayenā”ti.` | `“Yadi nūna, bhante, kadāci` | 6 |
| sn-56/56-49.md:3 | `Seyyathāpi, bhikkhave, puriso sinerussa` | the speech closes with `sinerupabbatarājā”ti?` but has no opening quote | `“Seyyathāpi, bhikkhave, puriso sinerussa` | 6 |
| sn-56/56-49.md:5 | `Etadeva, bhante, bahutaraṃ` | the reply closes with `upanikkhittā”ti.` (line 9) but has no opening quote | `“Etadeva, bhante, bahutaraṃ` | 6 |
| sn-56/56-49.md:19 | `Seyyathāpi, bhikkhave, puriso sinerussa` | no opening quote for the speech closed by `sinerupabbatarājā”ti?` | `“Seyyathāpi, bhikkhave, puriso sinerussa` | 6 |
| sn-56/56-49.md:63 | `Etadeva, bhante, bahutaraṃ` | no opening quote for the reply closed by `upanikkhittā”ti.` (line 65) | `“Etadeva, bhante, bahutaraṃ` | 6 |
| sn-56/56-47.md:170 | `[because of ] the fact of not having understood` | space before the closing bracket | `[because of] the fact of not having understood` | 9 |
| mn-107-ganakamoggallanasuttam.md:24 | `In Pubbārāma` | Capital "In" inside a gloss cell (all other glosses lower case: "in Savatthi", line 22) | `in Pubbārāma` | 8 |
| mn-107-ganakamoggallanasuttam.md:194 | `triads; groups of threes` | "groups of threes" (other rows: "groups of two", "groups of four") | `triads; groups of three` | 8 |
| mn-107-ganakamoggallanasuttam.md:197 | `five.` | Stray full stop in the gloss (other numerals have none) | `five` | 8 |
| mn-107-ganakamoggallanasuttam.md:293 | `veerb` | POS label misspelt | `verb` | 10 |
| mn-107-ganakamoggallanasuttam.md:371 | `(lit: [one] who has seen]` | Bracket opened with `(` and closed with `]` | `(lit: [one] who has seen)` | 9 |
| mn-107-ganakamoggallanasuttam.md:522 | `\*from where; whence;) since` | Opening bracket typed as `\*`; line 353 has the same gloss with `(` | `(from where; whence;) since` | 9 |
| mn-107-ganakamoggallanasuttam.md:776 | `in in the action` | Doubled word | `in the action` | 9 |
| mn-107-ganakamoggallanasuttam.md:1143 | `mindfull; fully present` | Typo | `mindful; fully present` | 9 |
| mn-107-ganakamoggallanasuttam.md:1235 | `who have achieve the highest goal` | Verb form | `who have achieved the highest goal` | 9 |
| mn-107-ganakamoggallanasuttam.md:1274 | `Ganaka-Moggalana` | One `l`; the translation at :1281 has `Ganaka-Moggallana` | `Ganaka-Moggallana` | 8 |
| mn-107-ganakamoggallanasuttam.md:1154 | `'Equanimous & mindful, he [is one] who lives at ease.”` | Quote opens with a straight single mark and closes with a curly double mark | `‘Equanimous & mindful, he [is one] who lives at ease.’` | 8 |
| mn-107-ganakamoggallanasuttam.md:1364 | `[and], the way leading to` | Stray comma after `[and]` | `[and] the way leading to` | 8 |
| mn-107-ganakamoggallanasuttam.md:888 | `front foremost` | Two glosses run together | `front; foremost` | 6 |
| mn-107-ganakamoggallanasuttam.md:1054 | `only, just even` | Glosses run together | `only; just; even` | 6 |
| mn-107-ganakamoggallanasuttam.md:928 | `(breath, blow)` | Root meaning needs the verb | `(breathe, blow)` | 6 |
| mn-107-ganakamoggallanasuttam.md:725 | `**indeed, brahman, when a monk` | Lower-case sentence start; the parallel sentence at :812 starts `Indeed` | `**Indeed, brahman, when a monk` | 7 |
| mn-107-ganakamoggallanasuttam.md:734 | `with full comprehension; \|` | Trailing semicolon | `with full comprehension \|` | 8 |
| mn-107-ganakamoggallanasuttam.md:1044 | `lives; abides; dwells; \|` | Trailing semicolon | `lives; abides; dwells \|` | 8 |
| mn-107-ganakamoggallanasuttam.md:1113 | `lives; abides; dwells; \|` | Trailing semicolon | `lives; abides; dwells \|` | 8 |
| mn-107-ganakamoggallanasuttam.md:1152 | `lives; abides; dwells; \|` | Trailing semicolon | `lives; abides; dwells \|` | 8 |
| mn-107-ganakamoggallanasuttam.md:1184 | `lives; abides; dwells; \|` | Trailing semicolon | `lives; abides; dwells \|` | 8 |
| mn-107-ganakamoggallanasuttam.md:1432 | `the way to Rajagaha?”` | Diacritic missing; "Rājagaha" everywhere else. | `the way to Rājagaha?”` | 9 |
| mn-107-ganakamoggallanasuttam.md:1547 | `for a moment , a little while` | Space before the comma. | `for a moment, a little while` | 9 |
| mn-107-ganakamoggallanasuttam.md:1554 | `delighfulness of a park(s); lovlineness of a grove(s)` | Two misspellings (DPD `ārāmarāmaṇeyyaka`: "delightfulness of a park; loveliness of a grove"). | `delightfulness of a park(s); loveliness of a grove(s)` | 9 |
| mn-107-ganakamoggallanasuttam.md:1556 | `delightfulness; pleasentness` | Misspelling. | `delightfulness; pleasantness` | 9 |
| mn-107-ganakamoggallanasuttam.md:1559 | `delightfulness; pleasentness` | Misspelling. | `delightfulness; pleasantness` | 9 |
| mn-107-ganakamoggallanasuttam.md:1560 | `delighfulness of a place; lovlineness of an area` | Two misspellings. | `delightfulness of a place; loveliness of an area` | 9 |
| mn-107-ganakamoggallanasuttam.md:1563 | `“.... delighfulness of a lotus pond; lovlineness of a lotus pool ”` | Two misspellings, four dots instead of three, and a space before the closing quote. | `“... delightfulness of a lotus pond; loveliness of a lotus pool”` | 9 |
| mn-107-ganakamoggallanasuttam.md:1637 | `Rāgagaha` | Misspelling. | `Rājagaha` | 9 |
| mn-107-ganakamoggallanasuttam.md:1680 | `ā + √khā + ī]` | Stray closing bracket. | `ā + √khā + ī` | 9 |
| mn-107-ganakamoggallanasuttam.md:1759 | `to the Blessed one:` | Lower-case "one"; the table (line 1754) has "the Blessed One". | `to the Blessed One:` | 8 |
| mn-107-ganakamoggallanasuttam.md:1815 | `lazy; in active` | Split word. | `lazy; inactive` | 9 |
| mn-107-ganakamoggallanasuttam.md:1837 | `pr.3rd.sg (+instr) \| live together` | Verb form does not agree with 3rd singular; line 1909 has "lives together". | `pr.3rd.sg (+instr) \| lives together` | 8 |
| mn-107-ganakamoggallanasuttam.md:1864 | `kammadhārayaas bahubbīhi` | Space missing. | `kammadhāraya as bahubbīhi` | 9 |
| mn-107-ganakamoggallanasuttam.md:1956 | `\#ajja \| insd \| adv \| today` | Typo in the POS; line 2045 has `ind`. | `\#ajja \| ind \| adv \| today` | 9 |
| mn-107-ganakamoggallanasuttam.md:2016 | `pa + √kās + \*e + ita]` | Stray closing bracket. | `pa + √kās + \*e + ita` | 9 |

### E. Markdown defects that affect rendering

| Location | Current | Problem | Suggested | Conf. |
| --- | --- | --- | --- | --- |
| mn-107-ganakamoggallanasuttam.md:446 | `So fare along controlling it, guard the organ of sight, achieve control over the organ of sight. (T)` | Second, unbolded translation line with no blank line before the next Pāli passage (line 447), so English and Pāli render as one paragraph; it also duplicates the bold translation at line 444 | Insert a blank line between lines 446 and 447 (owner to decide whether to keep the alternative translation and whether to bold it) | 8 |
| mn-107-ganakamoggallanasuttam.md:1604 | `Having approached you he would say, ‘show me the road to Rājagaha.’` | This line and the next three (1605–1607) are the translation of the passage at line 1603, but they are not bold like every other translation, and there is no blank line between passage 1603, these four lines and the next passage (line 1608). All six lines render as one paragraph. The passage at 1603 also has no table. | Put a blank line after line 1603, join lines 1604–1607 into one bold paragraph (`**Having approached you … lotus pond.”**`), and put a blank line before line 1608 | 8 |

### F. Convention drift

| Location | Current | Problem | Suggested | Conf. |
| --- | --- | --- | --- | --- |
| sn-22/22-18.md:3, :59 | `saññā aniccā...` | Three dots, while the translation (line 76) and the other files use `…` | `saññā aniccā…` | 6 |
| sn-22/22-24.md:3, :24, :61 | `abhijānaṃ...` | `...` and `…` mixed in the same passage (line 3: `anabhijānaṃ …` beside `anabhijānaṃ...`) | `…` | 6 |
| sn-22/22-26.md:5, :126 | `... pe ...` | `...` beside `…` in the same passage | `… pe …` | 6 |
| sn-22/22-28.md:9, :96 | `... pe ...` | `...` beside `…` in the same passage | `… pe …` | 6 |
| sn-22/22-33.md:3 | `vedanā na tumhākaṃ … saññā na tumhākaṃ ... saṅkhārā na tumhākaṃ …` | `…` and `...` mixed in one line | `vedanā na tumhākaṃ … saññā na tumhākaṃ … saṅkhārā na tumhākaṃ …` | 8 |
| sn-22/22-33.md:5 | `vedanā na tumhākaṃ… saññā na tumhākaṃ... saṅkhārā na tumhākaṃ...` | `…` and `...` mixed in one line (and spacing differs) | `vedanā na tumhākaṃ … saññā na tumhākaṃ … saṅkhārā na tumhākaṃ …` | 8 |
| sn-22/22-33.md:28 | `vedanā na tumhākaṃ … saññā na tumhākaṃ ... saṅkhārā na tumhākaṃ …` | `…` and `...` mixed in one line | `vedanā na tumhākaṃ … saññā na tumhākaṃ … saṅkhārā na tumhākaṃ …` | 8 |
| sn-22/22-33.md:123 | `vedanā na tumhākaṃ… saññā na tumhākaṃ... saṅkhārā na tumhākaṃ...` | `…` and `...` mixed in one line | `vedanā na tumhākaṃ … saññā na tumhākaṃ … saṅkhārā na tumhākaṃ …` | 8 |
| sn-22/22-58.md:5 | `vedanāya … saññāya... saṅkhārānaṃ...` | `…` and `...` mixed in one line | `vedanāya … saññāya … saṅkhārānaṃ …` | 8 |
| sn-22/22-58.md:51 | `vedanāya … saññāya... saṅkhārānaṃ...` | `…` and `...` mixed in one line | `vedanāya … saññāya … saṅkhārānaṃ …` | 8 |
| sn-22/22-59.md:11, 223 | `… vedanā... saññā... saṅkhārā... viññāṇaṃ` | `...` beside `…` in the same passage | `… vedanā … saññā … saṅkhārā … viññāṇaṃ` | 8 |
| sn-22/22-59.md:15, 326 | `yā kāci vedanā … yā kāci saññā ... ye keci saṅkhārā ...` | `…` and `...` mixed in one line | `yā kāci vedanā … yā kāci saññā … ye keci saṅkhārā …` | 8 |
| sn-22/22-58.md:77 | `fem.instr.sg (abl)` | Same word tagged `fem.instr.sg\*` with a note at :26, :40, :63 | `fem.instr.sg\*` with Construction `\*probably truncated ablative (Bodhi)` | 7 |
| sn-22/22-58.md:124 | `\| \| bhagavaṃ \| noun \| masc. (form in comps)` | Compound member without the `\#` marker (cf. :118, :127) | `\| \| \#bhagavaṃ \| noun \| masc. (form in comps)` | 8 |
| sn-22/22-58.md:128 | `\| 40858 \| paṭisaraṇā \| noun \| masc.nom.pl` | Compound member of `bhagavaṃpaṭisaraṇā` without the `\#` marker (cf. :125) | `\| 40858 \| \#paṭisaraṇā \| noun \| masc.nom.pl` | 8 |
| sn-22/22-59.md:289 | `\#paccuppanna (ca) \| noun \| masc \|` | Gender label without full stop (`masc.` at :288) | `\#paccuppanna (ca) \| noun \| masc. \|` | 8 |
| sn-22/22-63.md:17 | `pabbajanti tadanuttaraṃ — brahmacariyapariyosānaṃ` | dash misplaced: `tad` belongs with `brahmacariyapariyosānaṃ`; the same sentence at :222 reads `pabbajanti — tadanuttaraṃ brahmacariyapariyosānaṃ` | `pabbajanti — tadanuttaraṃ brahmacariyapariyosānaṃ` | 7 |
| sn-22/22-63.md:11, 115 | `vedanaṃ … saññaṃ... saṅkhāre ...` | `…` and `...` mixed in one sentence, with uneven spacing; :13 and :152 use `vedanaṃ... saññaṃ... saṅkhāre...` | `vedanaṃ... saññaṃ... saṅkhāre...` | 6 |
| sn-22/22-63.md:76 | `(not taking near)` | `lit:` missing; the positive at :71 has `(lit: taking near)`. English cell only; the known item on this line concerns the Construction cell (`√ādā`) | `(lit: not taking near)` | 8 |
| sn-22/22-63.md:125 | `(not taking near)` | as :76 | `(lit: not taking near)` | 8 |
| sn-22/22-63.md:134 | `(not taking near)` | as :76 | `(lit: not taking near)` | 8 |
| sn-22/22-63.md:174 | `(not taking near)` | as :76 | `(lit: not taking near)` | 8 |
| sn-22/22-63.md:183 | `(not taking near)` | as :76 | `(lit: not taking near)` | 8 |
| sn-22/22-63.md:150 | `form, Bhante, is bound` | translation uses "Bhante" while the table (:121) and the other translations render `bhante` as "Venerable Sir" | `form, Venerable Sir, is bound` | 6 |
| sn-22/22-71.md:47 | `mamaṅkāra (ca)` | member of the dvanda at :43 lacks the `\#` that :44 `\#ahaṅkāra (ca)` has | `\#mamaṅkāra (ca)` | 7 |
| sn-22/22-71.md:50 | `mānānusayā (ca)` | member of the dvanda at :43 lacks `\#` | `\#mānānusayā (ca)` | 7 |
| sn-22/22-71.md:45, 46, 48, 49, 51, 52 | `\#` | sub-members of the members (`ahaṃ`, `kāra`, `mamaṃ`, `kāra`, `mānassa`, `anusayā`) carry the same single `\#` as the members themselves; elsewhere (e.g. 22-63 sub-sub rows, 22-78:28) the second level is `\#\#` | `\#\#` on lines 45, 46, 48, 49, 51, 52 | 6 |
| sn-22/22-71.md:29, 152 | `√ñā + nā + nta` | `jānato` construction stops at `nta` while its pair `passato` (:31, :154) adds `+ to` | `√ñā + nā + nta + to` | 6 |
| sn-22/22-78.md:145 | `\#maha \| adj` | member spelt `maha`; `mahā` at :135 and DPD headword `mahā` | `\#mahā` | 7 |
| sn-22/22-78.md:149 | `\#maha \| adj` | as :145 | `\#mahā` | 7 |
| sn-22/22-78.md:304 | `\#maha \| adj` | as :145 | `\#mahā` | 7 |
| sn-22/22-78.md:308 | `\#maha \| adj` | as :145 | `\#mahā` | 7 |
| sn-22/22-78.md:112 | `\# rājadhānīsu (ca)` | space after `\#`, unlike every other member row | `\#rājadhānīsu (ca)` | 8 |
| sn-22/22-78.md:11 | `santāsaṃ āpajjanti` | full-text line ends without punctuation before the devas' speech; the same sentence at :219 ends `āpajjanti:` | `santāsaṃ āpajjanti:` | 6 |
| sn-22/22-78.md:5 | `suṇanti; yebhuyyena` | the same sentence at :57 has `suṇanti, yebhuyyena`; the `ye … suṇanti` clause is relative, so the comma fits | `suṇanti, yebhuyyena` | 6 |
| sn-22/22-82.md:155, 156 | `yadā \| ind` … `ākaṅkhasi \| verb` | Members of the sandhi row :154 lack the `\#` prefix used for members everywhere else in the file | `\#yad (yaṃ)`, `\#ākaṅkhasi` | 7 |
| sn-22/22-82.md:233 | `pañhaṃ apucchi – ime kho pana` | En dash where every other Pāli line uses em dash `—` | `pañhaṃ apucchi — ime kho pana` | 7 |
| sn-22/22-82.md:393 | `designation as aggregates \| kammadhāraya? \|` | Same word at :469 has `kammadhāraya` without the query mark; DPD khandhādhivacana is kammadhāraya | `kammadhāraya` | 8 |
| sn-22/22-82.md:426 | `rūpakkhandho \| noun \| masc.nom.sg \| form aggregate \| kammadhāraya? \|` | Query mark left in the compound type; DPD gives the sibling saññā-/saṅkhāra-/viññāṇakkhandha as chaṭṭhī tappurisa, so plain `kammadhāraya` (as at :493, :537) may itself be wrong | DPD lookup: rūpakkhandha; drop the `?` and use DPD's compound type | 6 |
| sn-22/22-82.md:394 | `\#khandha \| noun \| masc \|` | Gender label without the full stop used everywhere else (`masc.`) | `\#khandha \| noun \| masc. \|` | 7 |
| sn-22/22-82.md:400 | `yā kāci vedanā... yā kāci saññā ... ye keci saṅkhārā...` | Three-dot ellipsis, inconsistently spaced; :349 and :523 in the same file use `…` | `yā kāci vedanā … yā kāci saññā … ye keci saṅkhārā …` | 6 |
| sn-22/22-94.md:131 | `[of] which I, too, say: it does not exist.` | Lower-case quoted clause; all other quotes start `It` | `[of] which I, too, say: It does not exist.` | 6 |
| sn-22/22-94.md:163 | `atthi \| verb \| pr.3rd.sg \| it exists` | Same word glossed `it is; it exists` on lines 63, 147, 179, 191 | `atthi \| verb \| pr.3rd.sg \| it is; it exists` | 6 |
| sn-22/22-94.md:290 | `yo \| pron. \| masc.nom.sg` | POS `pron.` with a full stop; `pron` everywhere else | `yo \| pron \| masc.nom.sg` | 9 |
| sn-22/22-94.md:356 | `yo \| pron. \| masc.nom.sg` | As line 290 | `yo \| pron \| masc.nom.sg` | 9 |
| sn-22/22-94.md:391 | `se+ yathā+api` | Uneven spacing around `+` in the construction | `se + yathā + api` | 7 |
| sn-22/22-95.md:375 | `\#sāraṃ \| noun \| masc.acc.sg \| heartwood` | `#` marks compound members, but `sāraṃ` in `kuto sāraṃ` is an independent word | `sāraṃ \| noun \| masc.acc.sg \| heartwood` | 7 |
| sn-22/22-95.md:496 | `\#māyāya \| noun \| fem.loc.sg` | `#` marks compound members, but `māyāya` is an independent word | `māyāya \| noun \| fem.loc.sg` | 7 |
| sn-35/35-28.md:250 | `nt. nom.sg` | Stray space inside the grammar tag | `nt.nom.sg` | 9 |
| sn-35/35-70.md:7 | `viññūhī ti.` | `viññūhī ti` written with a space; the same word is `viññūhīti` at lines 5, 15, 19 | `viññūhīti.` | 7 |
| sn-35/35-70.md:63 | `viññūhī ti.` | Same split `viññūhī ti` as line 7; elsewhere `viññūhīti` | `viññūhīti.` | 7 |
| sn-35/35-70.md:148 | `viññūhī ti.` | Same split `viññūhī ti`; the full-text copy of this passage (line 11) has `viññūhīti` | `viññūhīti.` | 7 |
| sn-35/35-70.md:31 | `[ni + √sad + a + na` | Stray unmatched `[` at the start of the Construction cell | `ni + √sad + a + na` | 9 |
| sn-35/35-70.md:44 | `[√vac + ya + ti` | Stray unmatched `[` in Construction | `√vac + ya + ti` | 9 |
| sn-35/35-70.md:73 | `[√dis + tvā` | Stray unmatched `[` in Construction | `√dis + tvā` | 9 |
| sn-35/35-70.md:98 | `[pa + √ñā + nā + ti` | Stray unmatched `[` in Construction | `pa + √ñā + nā + ti` | 9 |
| sn-35/35-70.md:105 | `[√dis + tvā` | Stray unmatched `[` in Construction | `√dis + tvā` | 9 |
| sn-35/35-70.md:128 | `[pa + √ñā + nā + ti` | Stray unmatched `[` in the Construction cell of `pajānāti` | `pa + √ñā + nā + ti` | 9 |
| sn-35/35-70.md:180 | `[pa + √ñā + nā + ti` | Stray unmatched `[` in the Construction cell of `pajānāti` | `pa + √ñā + nā + ti` | 9 |
| sn-35/35-70.md:208 | `[pa + √ñā + nā + ti` | Stray unmatched `[` in the Construction cell of `pajānāti` | `pa + √ñā + nā + ti` | 9 |
| sn-35/35-70.md:232 | `[√dis + tvā` | Stray unmatched `[` in the Construction cell of `disvā` | `√dis + tvā` | 9 |
| sn-35/35-70.md:263 | `[√dis + tvā` | Stray unmatched `[` in the Construction cell of `disvā` | `√dis + tvā` | 9 |
| sn-35/35-70.md:256, 281, 333, 358 | `[pa + √ñā + nā + ti` | Same stray `[` in the Construction cell of `pajānāti` on each line | `pa + √ñā + nā + ti` (delete the leading `[` on each line) | 9 |
| sn-35/35-93.md:67 | `vipariṇām**ino** \| adj \| nt.nom.pl?` | Bold inside the Pāḷi cell and a query mark left in the Grammar cell; the same form is tagged plainly at 189, 212, 239. Not the known `35-93:50` item, which is the untranslated clause in the translation | `vipariṇāmino \| adj \| nt.nom.pl` | 6 |
| sn-35/35-93.md:68 | `aññathābhāv**ino** \| adj \| nt.nom.pl?` | Bold inside the Pāḷi cell and a query mark left in the Grammar cell. Not the known `35-93:50` item, which is the untranslated clause in the translation | `aññathābhāvino \| adj \| nt.nom.pl` | 6 |
| sn-35/35-118.md:158 | `\| \#viññeyyā \| adj \| masc.nom.pl \|` | Same compound member is POS `ptp` at :105 and :209 in this file; DPD viññeyya is ptp | `\| \#viññeyyā \| ptp \| masc.nom.pl \|` | 8 |
| sn-35/35-118.md:213 | `\| \#viññeyyā \| adj \| masc.nom.pl \|` | Same as :158 | `\| \#viññeyyā \| ptp \| masc.nom.pl \|` | 8 |
| sn-35/35-118.md:219 | `\| 46170 \| \#piya \| adj \| masc \|` | Gender label without full stop; `masc.` at :164 for the same row | `\| 46170 \| \#piya \| adj \| masc. \|` | 8 |
| sn-35/35-230.md:119 | `\| 46170 \| \#piya \| adj \| masc \|` | Gender label without full stop; `masc.` elsewhere in the file (:152) | `\| 46170 \| \#piya \| adj \| masc. \|` | 7 |
| sn-35/35-232.md:9 | `saṃyojanaṃ... . na mano` | Pe-ellipsis written `... .` (dots, space, full stop); line 35 writes the same gap as ` ... ` | `saṃyojanaṃ ... na mano` | 5 |
| sn-35/35-232.md:21 | `saṃyojanaṃ... . na mano` | Same `... .` ellipsis drift as line 9 | `saṃyojanaṃ ... na mano` | 5 |
| sn-35/35-232.md:29 | `dukkhakkhayāya... .` | Same `... .` ellipsis drift as line 9 | `dukkhakkhayāya ...` | 5 |
| sn-35/35-232.md:56 | `mahākoṭṭhiko \| noun \| masc. nom.sg` | Space inside grammar tag; all other rows write `masc.nom.sg` | `masc.nom.sg` | 8 |
| sn-35/35-232.md:65 | `mahākoṭṭhiko \| noun \| masc. nom.sg` | Space inside grammar tag | `masc.nom.sg` | 8 |
| sn-35/35-232.md:91 | `mahākoṭṭhiko \| noun \| masc. nom.sg` | Space inside grammar tag | `masc.nom.sg` | 8 |
| sn-35/35-232.md:113 | `eye?...[Is]` | Three dots and no spaces; the other translations use `…` | `eye? … [Is]` | 6 |
| sn-35/35-232.md:116 | `saṃyojanaṃ... . na mano` | Same `... .` ellipsis drift as line 9 | `saṃyojanaṃ ... na mano` | 5 |
| sn-35/35-232.md:254 | `saṃyojanaṃ... . na mano` | Same `... .` ellipsis drift as line 9 | `saṃyojanaṃ ... na mano` | 5 |
| sn-35/35-232.md:338 | `paññāyati sammā dukkhakkhayāya` | Sentence has no closing punctuation; the same sentence at line 29 ends in `... .` | `paññāyati sammā dukkhakkhayāya.` | 6 |
| sn-35/35-241.md:280 | `what [is] the grasp of a whirlpool` | Every other place in the file (tables 140, 271; translations 423, 542) renders `āvaṭṭaggāho` as "clutch of a whirlpool", as does DPD āvaṭṭaggāha | `what [is] the clutch of a whirlpool` | 8 |
| sn-35/35-246.md:105 | `\| 51011 \| \#madanīyo \| adj \|` | Parallel -anīya members `\#rajanīyo`, `\#kamanīyo` (99, 102) are tagged `adj (ptp)`, this one plain `adj`; DPD madanīya is ptp | `\| 51011 \| \#madanīyo \| adj (ptp) \|` | 8 |
| sn-35/35-246.md:108 | `\| 52840 \| \#mucchanīyo \| adj \|` | Same drift as line 105: plain `adj` beside `adj (ptp)`; DPD mucchanīya is ptp | `\| 52840 \| \#mucchanīyo \| adj (ptp) \|` | 8 |
| sn-35/35-246.md:111 | `\| 47924 \| \#bandhanīyo \| adj \|` | Same drift as line 105: plain `adj` beside `adj (ptp)`; DPD bandhanīya 1 is ptp | `\| 47924 \| \#bandhanīyo \| adj (ptp) \|` | 8 |
| sn-35/35-246.md:143 | `\| 51011 \| \#madanīyo \| adj \|` | Same drift as line 105: plain `adj` beside `adj (ptp)` | `\| 51011 \| \#madanīyo \| adj (ptp) \|` | 8 |
| sn-35/35-246.md:146 | `\| 52840 \| \#mucchanīyo \| adj \|` | Same drift as line 105: plain `adj` beside `adj (ptp)` | `\| 52840 \| \#mucchanīyo \| adj (ptp) \|` | 8 |
| sn-35/35-246.md:149, 194, 197, 200 | `\| adj \| masc.nom.sg \|` | Same drift as line 105 on the remaining `\#bandhanīyo` (149, 200), `\#madanīyo` (194) and `\#mucchanīyo` (197) member rows | `\| adj (ptp) \| masc.nom.sg \|` | 8 |
| sn-35/35-246.md:243 | `(of a veena) soundbox` | "veena" here; "lute" in every other row (249) and in the translation (DPD doṇi 2 "(of a vīṇā) soundbox"); the known item on this line is about the Grammar cell | `(of a lute) soundbox` | 7 |
| sn-35/35-246.md:246 | `(of a veena) sound board` | Same drift as line 243 (DPD camma 4 "(of a vīṇā) sound board") | `(of a lute) sound board` | 7 |
| sn-35/35-247.md:737 | `lit. ground` | Literal-gloss format drift; elsewhere `(lit: …)` | `(lit: ground)` | 8 |
| sn-35/35-247.md:21 | `nirujjhanti... .` | Ellipsis attached to the word plus a stray full stop; elsewhere ` ... ` (line 51) | `nirujjhanti ...` | 6 |
| sn-35/35-247.md:61 | `nirujjhanti... .` | Ellipsis attached to the word plus a stray full stop | `nirujjhanti ...` | 6 |
| sn-35/35-247.md:471 | `nirujjhanti... .` | Ellipsis attached to the word plus a stray full stop | `nirujjhanti ...` | 6 |
| sn-35/35-247.md:37 | `atha kho, te, bhikkhave` | Extra comma after `kho`; the repeat at line 71 has `atha kho te, bhikkhave` | `atha kho te, bhikkhave` | 7 |
| sn-35/35-247.md:346 | `atha kho, te, bhikkhave` | Extra comma after `kho`; line 564 has `atha kho te, bhikkhave` | `atha kho te, bhikkhave` | 7 |
| sn-56/56-1.md:59 | `32877 \| dukkhassa \| noun` | Compound-member row lacks the `\#` marker (the same rows at lines 116–117 have it) | `32877 \| \#dukkhassa \| noun` | 8 |
| sn-56/56-1.md:60 | `38097 \| nirodho \| noun` | Compound-member row lacks the `\#` marker | `38097 \| \#nirodho \| noun` | 8 |
| sn-56/56-1.md:99 | `30148 \| tasmā \| ind` | Sandhi-member row lacks the `\#` marker (cf. `35-247.md:719`) | `30148 \| \#tasmā \| ind` | 8 |
| sn-56/56-1.md:100 | `13936 \| iha \| ind` | Sandhi-member row lacks the `\#` marker | `13936 \| \#iha \| ind` | 8 |
| sn-56/56-1.md:107 | `masc. nom.sg` | Stray space in grammar tag | `masc.nom.sg` | 9 |
| sn-56/56-1.md:114 | `masc. nom.sg` | Stray space in grammar tag | `masc.nom.sg` | 9 |
| sn-56/56-13.md:224 | `right-view, right-intention, right-speech, right-action, right-livelihood, right effort, right mindfulness, right concentration` | First five factors hyphenated, last three not; the table glosses (:204–213) are unhyphenated. | `right view, right intention, right speech, right action, right livelihood, right effort, right mindfulness, right concentration` | 9 |
| sn-56/56-25.md:25 | `√dis + a + nta + to` | `passato` rows add the case ending (`+ to`: :25, :35, :52, :59, :75, :84, :93) while `jānato`, `ajānato`, `apassato` rows (:22, :30, :31, :34 …) stop at `nta`. | `√dis + a + nta` on every `passato` row | 7 |
| sn-56/56-31.md:147 | `kammadhāraya+kā` | Construction cell carries a stray `+kā` suffix not used elsewhere in the file (the known item for :142–147 covers only the Grammar cells) | `kammadhāraya` | 6 |
| sn-56/56-33.md:33 | `\| \| sakim’pi \| sandhi \|` | Pāli cell does not match the passage (`sakimpi`) or :56, :62 | `\| \| sakimpi \| sandhi \|` | 8 |
| sn-56/56-34.md:88 | `na+abhi + saṃ + √i` | Spacing drift in the construction (`+` is spaced everywhere else) | `na + abhi + saṃ + √i` | 7 |
| sn-56/56-34.md:107 | `[one's] garment` | Straight apostrophe; :37 and :71 use `one’s` | `[one’s] garment` | 7 |
| sn-56/56-37.md:13 | `sūriyassa, bhikkhave, udayato` | Lower case, while the full text (:3) and the table (:18) have `Sūriyassa` | `Sūriyassa, bhikkhave, udayato` | 7 |
| sn-56/56-38.md:91 | `\| \| \#pātur \| ind \| \| manifest; visible; open \|` | Same member of the same compound as :36 (`45441 \| \#pātu \| … in front; visible; open`): different spelling, gloss and no ID; DPD `pātu` ind "in front; visible; open" | `\| 45441 \| \#pātu \| ind \| \| in front; visible; open \|` | 8 |
| sn-56/56-38.md:62 | `\| 2990 \| \#addha \| noun \| masc. \| half \|` | `addha` is a member of `\#addhamāsā` (:61), so it needs the second-level marker `\#\#` | `\| 2990 \| \#\#addha \|` | 8 |
| sn-56/56-38.md:63 | `\| 52490 \| \#māso \| noun \| masc.nom.sg \| month \|` | `māso` is a member of `\#addhamāsā` (:61), so it needs the second-level marker `\#\#` | `\| 52490 \| \#\#māso \|` | 8 |
| sn-56/56-38.md:133 | `\| 35347 \| na \| ind \| prefix \| does not \|` | Other `na` rows (e.g. :30) use ID 35345 with `neg`; here `na` is the negative particle of `n’uppajjati`, not a compound prefix (DPD `na 3` prefix is "in comps") | `\| 35345 \| na \| ind \| neg \| not \| \|` | 6 |
| sn-56/56-27.md:43 | `\| 26117 \| Cattāri \|` | Capital in the table, but the word is mid-sentence and lower case in the passage (:36 `cattāri`) | `\| 26117 \| cattāri \|` | 8 |
| sn-56/56-38.md:98 | `\| 5906 \| Andhatamaṃ \|` | Capital mid-sentence (passage :73 `N’eva andhakāratamaṃ`) | `\| 5906 \| andhatamaṃ \|` | 7 |
| sn-56/56-38.md:190 | `\| 5906 \| Andhatamaṃ \|` | Capital mid-sentence (passage :170 `N’eva andhatamaṃ`) | `\| 5906 \| andhatamaṃ \|` | 7 |
| sn-56/56-28.md:26 | `\# brāhmaṇā (ca)` | Space after the member marker; every other member row has none | `\#brāhmaṇā (ca)` | 8 |
| sn-56/56-28.md:32 | `\# manussā (ca)` | Space after the member marker | `\#manussā (ca)` | 8 |
| sn-56/56-29.md:3 | `ariyasaccāni... . Imesaṃ` | Stray full stop after the ellipsis | `ariyasaccāni ... Imesaṃ` | 7 |
| sn-56/56-29.md:72 | `[√bhū + \*e + tabba` | Stray opening bracket in the construction | `√bhū + \*e + tabba` | 8 |
| sn-56/56-42.md:3 | `‘idaṃ dukkhan’ti yathā-bhūtaṃ nappajānanti` | `yathā-bhūtaṃ` is hyphenated here and nowhere else (`yathābhūtaṃ` at :29 and in every table row) | `‘idaṃ dukkhan’ti yathābhūtaṃ nappajānanti` | 8 |
| sn-56/56-42.md:11 | `domanass’upāyāsapapātam’pi papatanti` | apostrophe before `pi` here only; the same word is `…papātampi` at :138, :21 and :210 | `domanass’upāyāsapapātampi papatanti` | 8 |
| sn-56/56-42.md:29 | `maraṇasaṃvattanikesu saṅkhāresu abhiramanti,` | trailing space at end of line (mech check) | `maraṇasaṃvattanikesu saṅkhāresu abhiramanti,` with the trailing space removed | 9 |
| sn-56/56-42.md:21, 210 | `saṅkhāresu nābhiramanti... . Te` | stray ` .` after the ellipsis (also after `nābhisaṅkharonti...` on the same lines) | `saṅkhāresu nābhiramanti... Te` (and `nābhisaṅkharonti... Te`) | 7 |
| sn-56/56-42.md:259 | `who clearly understand as it really is: ‘This is suffering’` | `yathābhūtaṃ` rendered "as it really is" here (twice) but "as it truly is" in the table and every other translation in the file | `who clearly understand as it truly is: ‘This is suffering’` (and `who understand as it truly is` later in the line) | 6 |
| sn-56/56-44.md:13 | `sammā dukkhassantaṃ karissāmī’ti` | `dukkhassantaṃ` without apostrophe; `dukkhass’antaṃ` at :3, :17, :21, :25 | `sammā dukkhass’antaṃ karissāmī’ti` | 8 |
| sn-56/56-44.md:60 | `sammā dukkhassantaṃ karissāmī’ti` | same apostrophe drift | `sammā dukkhass’antaṃ karissāmī’ti` | 8 |
| sn-56/56-44.md:21, 146 | `yo evaṃ vadeyya: ‘Ahaṃ dukkhaṃ` | colon before the quotation here; a comma in all other instances of `vadeyya, ‘Ahaṃ` | `yo evaṃ vadeyya, ‘Ahaṃ dukkhaṃ` | 6 |
| sn-56/56-44.md:51 | `\| ṭhānaṃ \| nt \| nt.nom.sg \|` | POS column holds a gender (`nt`) instead of `noun` | `\| ṭhānaṃ \| noun \| nt.nom.sg \|` | 9 |
| sn-56/56-44.md:82 | `\| ṭhānaṃ \| nt \| nt.nom.sg \|` | POS `nt` instead of `noun` | `\| ṭhānaṃ \| noun \| nt.nom.sg \|` | 9 |
| sn-56/56-44.md:108 | `\| ṭhānaṃ \| nt \| nt.nom.sg \|` | POS `nt` instead of `noun` | `\| ṭhānaṃ \| noun \| nt.nom.sg \|` | 9 |
| sn-56/56-44.md:139 | `\| ṭhānaṃ \| nt \| nt.nom.sg \|` | POS `nt` instead of `noun` | `\| ṭhānaṃ \| noun \| nt.nom.sg \|` | 9 |
| sn-56/56-44.md:164, 189 | `\| ṭhānaṃ \| nt \| nt.nom.sg \|` | POS `nt` instead of `noun` | `\| ṭhānaṃ \| noun \| nt.nom.sg \|` | 9 |
| sn-56/56-44.md:78 | `fut.caus.1st. sg` | stray dot-space inside the grammar label | `fut.caus.1st.sg` | 9 |
| sn-56/56-44.md:162 | `fut.caus.1st. sg` | stray dot-space inside the grammar label | `fut.caus.1st.sg` | 9 |
| sn-56/56-47.md:97 | `\| 65082 \| So \| pron \|` | capital carried into the table although `so` is mid-sentence in the text (`Khippataraṃ kho so`); not the known sentence-initial capitals item, since the text itself is lower case here | `\| 65082 \| so \| pron \|` | 8 |
| sn-56/56-49.md:123 | `\| 17871 \| Etadeva \| sandhi \|` | capital carried into the table although the word is mid-sentence in the text (`abhisametāvino etadeva`, :106); not the known sentence-initial capitals item | `\| 17871 \| etadeva \| sandhi \|` | 9 |
| mn-107-ganakamoggallanasuttam.md:59 | `√raj 3ya (to desire, attach)` | Root notation without the `･` separator and with "to" in the meaning; the file's style is `√root･N sign (meaning)` | `√raj･3 ya (desire, attach)` | 7 |
| mn-107-ganakamoggallanasuttam.md:321 | `√sīl×1 a (conduct oneself)` | `×` used instead of `･` between root and class | `√sīl･1 a (conduct oneself)` | 8 |
| mn-107-ganakamoggallanasuttam.md:559 | `√dū×1 a (go, run)` | `×` used instead of `･` between root and class | `√dū･1 a (go, run)` | 8 |
| mn-107-ganakamoggallanasuttam.md:318 | `imp.2nd sg` | Space instead of dot in the grammar tag | `imp.2nd.sg` | 9 |
| mn-107-ganakamoggallanasuttam.md:286 | `nt. loc.sg` | Space inside the grammar tag | `nt.loc.sg` | 9 |
| mn-107-ganakamoggallanasuttam.md:594 | `masc. nom.sg` | Space inside the grammar tag | `masc.nom.sg` | 9 |
| mn-107-ganakamoggallanasuttam.md:26 | `fem.gen.sg.` | Trailing dot on a full grammar tag (others have none) | `fem.gen.sg` | 8 |
| mn-107-ganakamoggallanasuttam.md:156 | `nt.instr.sg.` | Trailing dot on a full grammar tag | `nt.instr.sg` | 8 |
| mn-107-ganakamoggallanasuttam.md:629 | `imp.2nd.sg.` | Trailing dot on a full grammar tag (line 328 has `imp.2nd.sg`) | `imp.2nd.sg` | 8 |
| mn-107-ganakamoggallanasuttam.md:399 | `nimittag’gāhī` | Apostrophe inside a compound (not a sandhi junction); lines 404 and 474 write the same pattern without it | `nimittaggāhī` | 8 |
| mn-107-ganakamoggallanasuttam.md:216 | `satampi \| sandhi` | Sandhi row without the apostrophe the file uses in the same pattern (`imesam’pi` 113, `amhākam’pi` 149, `imasmim’pi` 234) | `satam’pi` | 6 |
| mn-107-ganakamoggallanasuttam.md:150 | `\#amhākam` | Resolved sandhi member keeps final `m`; other resolved members restore `ṃ` (`\#imesaṃ` 114, `\#imasmiṃ` 235) | `\#amhākaṃ` | 7 |
| mn-107-ganakamoggallanasuttam.md:217 | `\#satam` | Resolved sandhi member keeps final `m`; other resolved members restore `ṃ` (`\#imesaṃ` 114, `\#imasmiṃ` 235). The case tag on this line is a separate row | `\#sataṃ` | 7 |
| mn-107-ganakamoggallanasuttam.md:489 | `yatvādhikaraṇamenaṃ \| ind` | Same word is a `sandhi` row with three `\#` members at lines 414–417; here it is `ind` with the parts in the Construction column | `sandhi` plus the member rows of lines 415–417 | 7 |
| mn-107-ganakamoggallanasuttam.md:545 | `paṭi+ saṃ +√khā･1 a` | Prefix written `paṭi` in the construction; DPD `paṭisaṅkhā` = `pati + saṃ + √khā + (ya) > khā`, and lines 430, 502 and 697 write `pati` | `pati+ saṃ +√khā･1 a` | 8 |
| mn-107-ganakamoggallanasuttam.md:582 | `paṭi√han･1 a` | Prefix written `paṭi` in the construction; DPD `paṭihaṅkhati` = `pati + haṅkha + ti`, and lines 430, 502 and 697 write `pati` | `pati√han･1 a` | 8 |
| mn-107-ganakamoggallanasuttam.md:80 | `yadidaṃ -` | Hyphen where the other passages use an em dash (`yadidaṃ —` at lines 103, 145) | `yadidaṃ —` | 8 |
| mn-107-ganakamoggallanasuttam.md:128 | `yadidaṃ - issatthe .` | Hyphen instead of em dash, and a space before the full stop | `yadidaṃ — issatthe.` | 8 |
| mn-107-ganakamoggallanasuttam.md:141 | `issatthe .` | Space before the full stop in the Pāli cell | `issatthe.` | 8 |
| mn-107-ganakamoggallanasuttam.md:447 | `phusitvā …` | Three `... pe ...` in the line, then a lone `…` without `pe` | `phusitvā ... pe ...` | 7 |
| mn-107-ganakamoggallanasuttam.md:210 | `**'One group of one` | Straight single quotes in the translation (the file uses curly quotes) | `**‘One group of one … groups of ten,’**` | 8 |
| mn-107-ganakamoggallanasuttam.md:250 | `Discipline?"**` | Straight double quote in the translation | `Discipline?”**` | 8 |
| mn-107-ganakamoggallanasuttam.md:347 | `**"'Come you, monk` | Straight quotes at both ends of the translation (`…rules of training.'**`) | `**“‘Come you, monk … rules of training.’**` | 8 |
| mn-107-ganakamoggallanasuttam.md:31 | `in Savatthi, in Pubbarama, in Migāramātupāsāda` | Proper names without diacritics beside one with them (gloss at line 24 has `Pubbārāma`) | `in Sāvatthi, in Pubbārāma, in Migāramātupāsāda` | 8 |
| mn-107-ganakamoggallanasuttam.md:36, :44, :71 | `Ganaka-Moggallāna` | Name with diacritics on one half only | `Gaṇaka-Moggallāna` | 8 |
| mn-107-ganakamoggallanasuttam.md:78 | `the brahman Ganaka-Moggallana` | Third spelling of the name (no diacritics at all); "brahman" lower case here, "Brahman" at lines 37, 44, 72 | `the Brahman Gaṇaka-Moggallāna` | 7 |
| mn-107-ganakamoggallanasuttam.md:311, :378, :382, :528, :532, :616, :620 | `the Tathagata` | `Tathagata` without diacritics beside `the Tathāgata` at line 302 | `the Tathāgata` | 8 |
| mn-107-ganakamoggallanasuttam.md:725 | `the Tathagata instructs him further` | No diacritics; `Tathāgata` at :721 and :812 | `the Tathāgata instructs him further` | 8 |
| mn-107-ganakamoggallanasuttam.md:1364 | `nibbana exists, [and], the way leading to nibbana exists` | `nibbana` twice without the macron; `nibbāna` at :1311, :1335, :1390 | `nibbāna` in both places | 8 |
| mn-107-ganakamoggallanasuttam.md:766 | `\| sampajāna-kārī \|` | Hyphen inside the Pāḷi word; the passage (:758) and all other rows have `sampajānakārī` | `\| sampajānakārī \|` | 9 |
| mn-107-ganakamoggallanasuttam.md:766 | `\| sampajāna-kārī \| noun \| masc.nom.sg \|` | POS `noun`; DPD `sampajānakārī` is adj, and the same word is `adj` at :739 and :744 | `adj` | 8 |
| mn-107-ganakamoggallanasuttam.md:747 | `\| sampajānakārī \| noun \| masc.nom.sg \|` | POS `noun`; DPD `sampajānakārī` adj, and the same word in the same sentence is `adj` at :739 and :744 | `adj` | 8 |
| mn-107-ganakamoggallanasuttam.md:754 | `\| sampajānakārī \| noun \| masc.nom.sg \|` | POS `noun` against DPD adj and `adj` at :739, :744 | `adj` | 8 |
| mn-107-ganakamoggallanasuttam.md:777 | `\| sampajānakārī \| noun \| masc.nom.sg \|` | POS `noun` against DPD adj and `adj` at :739, :744 | `adj` | 8 |
| mn-107-ganakamoggallanasuttam.md:792 | `\| sampajānakārī \| noun \| masc.nom.sg \|` | POS `noun` against DPD adj and `adj` at :739, :744 | `adj` | 8 |
| mn-107-ganakamoggallanasuttam.md:738 | `\| pp. (as noun) \|` | Label drift: `pp (as noun)` at :737, `noun (pp)` at :742–746 and :762–788 | `pp (as noun)` (or `noun (pp)` throughout :737–738) | 7 |
| mn-107-ganakamoggallanasuttam.md:738 | `pati√kam･1 a (go)+ta+e` | The assimilation `(m \> n)` given for the same verb at :737 and :879 is missing. (The prefix `pati` agrees with DPD `paṭikkanta` construction pati + √kam + ta; `paṭi` at :879 is the variant) | `pati√kam･1 a (go)(m \> n)+ta+e` | 6 |
| mn-107-ganakamoggallanasuttam.md:883 | `√uj×1 a (be straight)` | `×` instead of the `･` used in every other root reference | `√uj･1 a (be straight)` | 6 |
| mn-107-ganakamoggallanasuttam.md:1204 | `√khi×1 a (live, abide peacefully)` | `×` instead of `･` | `√khi･1 a (live, abide peacefully)` | 6 |
| mn-107-ganakamoggallanasuttam.md:922 | `\| \#abyāpanna \| pp \| masc \|` | Gender label without the full stop used elsewhere (`masc.` at :903, :948, :970) | `masc.` | 7 |
| mn-107-ganakamoggallanasuttam.md:965 | `\| \#uddhacca (ca) \| noun \| nt \|` | Gender label without the full stop (`nt.` at :752, :836) | `nt.` | 7 |
| mn-107-ganakamoggallanasuttam.md:1083 | `\| puna caparaṃ \| sandhi/ idiom \|` | The same phrase is `idiom` at :1121 (DPD `puna caparaṃ` idiom), with a trailing comma in the Pāḷi cell and no member rows | `idiom` (and one form of the row in both tables) | 5 |
| mn-107-ganakamoggallanasuttam.md:1110 | `\| dutiyaṃ \| adj \| nt.acc.sg \| the second \|` | POS `adj`; DPD `dutiya 1` ordin, and the other ordinals are `ord` (`paṭhamaṃ` :1041, `tatiyaṃ` :1149, `catutthaṃ` :1181) | `ord` | 8 |
| mn-107-ganakamoggallanasuttam.md:823 | `\| \#āsana (ca) \| noun \| nt.acc.sg \| seat \|` | Compound member written as a stem but tagged with a case; the stem beside it (:822) has gender only. Same at :919 `\#padosa (ca)` masc.acc.sg, :944 `\#thīna (ca)` nt.acc.sg, :1040 `\#sukha (ca)` nt.acc.sg, :1263 `\#sampajañña (ca)` nt.dat.sg | `nt.` (gender only for stem-form members; likewise on the four other lines) | 5 |
| mn-107-ganakamoggallanasuttam.md:1407 | `In that case, Brahman, I will ask` | "Brahman" has a capital here; the translations at lines 1467, 1665 and 1706 write "brahman". | `In that case, brahman, I will ask` | 6 |
| mn-107-ganakamoggallanasuttam.md:1671 | `ettha \| ind. \| adv. \| here, in this regard` | Full stops after `ind` and `adv`; the same word at line 1733 and all other rows have none. | `ettha \| ind \| adv \| here; in this regard` | 8 |
| mn-107-ganakamoggallanasuttam.md:1970, 1977, 2001, 2010, 2018, 2041, 2055 | `Master` | "Master Gotama" has a capital from line 1970 to the end; lines 1675, 1685, 1768, 1835, 1839, 1907, 1911, 1918 and 1959 write "master Gotama". | One spelling throughout; `master` is the majority in this file | 7 |

### G. Links

None.

### H. Data to re-verify (forms, references, counts)

| Location | Current | Problem | Suggested | Conf. |
| --- | --- | --- | --- | --- |
| sn-22/22-18.md:3 | `vedanā kuto niccā bhavissati!` | The full text ends three of the four questions with `!`, but the breakdown (lines 78, 108) uses `?` for the same sentences | Check against CST and use the same mark in the full text and the breakdown | 5 |
| sn-22/22-58.md:36 | `liberated by knowledge; by understanding` | Gloss drift: member `#paññāya` is "by wisdom" (:37) and :105, :111 say "liberated by wisdom"; DPD `paññāvimutta` "liberated by understanding" does not settle knowledge vs wisdom | owner decision: one gloss for `paññāvimutta` in this file, `liberated by wisdom` (as :37, :105, :111, :224) or `liberated by knowledge` | 6 |
| sn-22/22-58.md:45 | `liberated by knowledge; by understanding` | Gloss drift with :105 "liberated by wisdom"; DPD ("liberated by understanding") does not settle it | owner decision, as at :36 | 6 |
| sn-22/22-58.md:73 | `liberated by knowledge; by understanding` | Gloss drift with :105 "liberated by wisdom"; DPD ("liberated by understanding") does not settle it | owner decision, as at :36 | 6 |
| sn-22/22-58.md:82 | `liberated by knowledge; by understanding` | Gloss drift with :105 "liberated by wisdom"; DPD ("liberated by understanding") does not settle it | owner decision, as at :36 | 6 |
| sn-22/22-58.md:49 | `A monk, monks, liberated by knowledge` | Same term translated "liberated by wisdom" at :111 and :224; DPD does not settle it | owner decision, as at :36; if "wisdom", also `is called liberated by wisdom` at the end of the line | 6 |
| sn-22/22-58.md:86 | `A monk, monks, liberated by knowledge` | Same term translated "liberated by wisdom" at :111 and :224; DPD does not settle it | owner decision, as at :36; if "wisdom", also `is called liberated by wisdom` at the end of the line | 6 |
| sn-22/22-63.md:52 | `yaṃ \| pron \| nt.acc.sg \| which; that` | in `yamahaṃ bhagavato dhammaṃ sutvā … vihareyyaṃ` the tag nt.acc.sg fits neither reading: DPD offers `yaṃ 2` (pron, masc fem & nt acc sg; would agree with masc `dhammaṃ`) and `yaṃ 3` (ind, adv "because; since; when"); the translation at :65 has "[so] that" | owner decision: either `pron \| masc.acc.sg \| which` (with `dhammaṃ`) or `ind \| adv \| so that` (DPD yaṃ 3) | 5 |
| sn-22/22-82.md:567 | `idha, bhikkhu, assutavā puthujjano` | The question `kathaṃ nu kho, bhante, sakkāyadiṭṭhi hotīti?` (full text :41) has no Pāli line, table or translation in the line-by-line part; the answer at :567 follows directly after the :523 block | Owner decision: add the question block (Pāli, table, translation) before :567, as for the other questions | 8 |
| sn-22/22-82.md:637 | `idha, bhikkhu, sutavā ariyasāvako` | The question `kathaṃ pana, bhante, sakkāyadiṭṭhi na hotīti?` (full text :45) has no Pāli line, table or translation in the line-by-line part | Owner decision: add the question block (Pāli, table, translation) before :637 | 8 |
| sn-22/22-94.md:48, 59, 78, 94, 111, 123, 142, 159, 175, 187 | `paṇḍitānaṃ \| noun \| masc.dat.pl \| (by) the wise` | Agent of the pp `sammata` is usually read as genitive; the row tags dative while glossing an agent. DPD (atthisammata, natthisammata, paṇḍita) gives no case | Owner decision: `masc.gen.pl` (and `(+gen)` on `natthisammataṃ`/`atthisammataṃ`) or keep `masc.dat.pl` | 5 |
| sn-35/35-70.md:158, 163 | `\| 34809 \| dhammarāgappaṭisaṃvedī \|` | ID 34809 is given both to `dhammappaṭisaṃvedī` (158) and to `dhammarāgappaṭisaṃvedī` (163); one of them is wrong. DPD has `dhammappaṭisaṃvedī 1` (mental phenomena, the sense here), `dhammappaṭisaṃvedī 2` and one `dhammarāgappaṭisaṃvedī`; the saved output gives no IDs | DPD lookup: ID of `dhammappaṭisaṃvedī 1` and of `dhammarāgappaṭisaṃvedī` | 8 |
| sn-35/35-70.md:188, 191 | `\| 34809 \| dhammarāgappaṭisaṃvedī \|` | Same shared ID 34809 for two different compounds | DPD lookup: ID of `dhammappaṭisaṃvedī 1` and of `dhammarāgappaṭisaṃvedī` | 8 |
| sn-35/35-70.md:310, 317 | `\| 34809 \| dhammarāgappaṭisaṃvedī \|` | Same shared ID 34809 for two different compounds | DPD lookup: ID of `dhammappaṭisaṃvedī 1` and of `dhammarāgappaṭisaṃvedī` | 8 |
| sn-35/35-70.md:341, 346 | `\| 34809 \| dhammarāgappaṭisaṃvedī \|` | Same shared ID 34809 for two different compounds | DPD lookup: ID of `dhammappaṭisaṃvedī 1` and of `dhammarāgappaṭisaṃvedī` | 8 |
| sn-35/35-70.md:245, 322 | `\| 9432 \| asantaṃ \| … \| 9428 \| asantaṃ \|` | The same word `asantaṃ` (same tag and gloss) carries two different IDs, 9432 and 9428; DPD has a single headword `asantaṃ` (prp), but the saved output gives no ID | DPD lookup: ID of headword `asantaṃ`, used on both lines | 8 |
| sn-35/35-232.md:335 | `living this holy life would not be discerned` | Translation style: "this holy life" reads `idaṃ` as qualifying masc `brahmacariyavāso`; DPD idaṃ 3 is ind, adv "here; in this case" | owner decision: keep, or `here the living of the holy life would not be discerned` | 5 |
| sn-35/35-232.md:439 | `living this holy life would not be discerned` | Translation style: "this holy life" reads `idaṃ` as qualifying masc `brahmacariyavāso`; DPD idaṃ 3 is ind, adv "here; in this case" | owner decision: keep, or `here the living of the holy life would not be discerned` | 5 |
| sn-35/35-241.md:179 | `na thale ussīdissatha, na manussaggāho gahessati` | In the 2nd-person application the translation (line 238) adds "[you]" as object; Nanda's version has `na maṃ manussaggāho` (line 477), and some editions may read `na vo manussaggāho gahessati` here (unverified, from memory). The same text is at line 9 | verify against CST SN 35.241; if `vo` is present, add it here, at line 9 and as a `vo \| pron \| 2nd.acc.pl` row in the table at line 204 | 4 |
| sn-35/35-246.md:97 | `\| 18142 \| evaṃrajanīyo \|` | Same ID 18142 as `evaṃkamanīyo` (lines 100, 138, 189); one of the two IDs is wrong (saved DPD output gives no IDs) | DPD lookup: IDs of evaṃrajanīya and evaṃkamanīya | 6 |
| sn-35/35-246.md:27, 285 | `yathevayaṃ kiñci vīṇā nāma` | Reading doubtful: editions may have `yathevaṃ yaṃkiñci` (or similar); DPD has no headword `yathevayaṃ` | Verify against CST SN 35.246 | 4 |
| sn-35/35-247.md:493 | `4652 \| upaṭṭhitakāyassati` | Same ID 4652 as `anupaṭṭhitakāyassati` (line 214); one of the two is wrong. Saved DPD output gives no IDs | DPD lookup: ID of `upaṭṭhitakāyassati` | 8 |
| sn-35/35-247.md:494 | `4650 \| \#upaṭṭhita` | Same ID 4650 as `#anupaṭṭhita` (line 215); one of the two is wrong. Saved DPD output gives no IDs | DPD lookup: ID of `upaṭṭhita` | 8 |
| sn-35/35-247.md:540 | `4652 \| upaṭṭhitakāyassati` | Same ID 4652 as `anupaṭṭhitakāyassati` (line 262) | DPD lookup: ID of `upaṭṭhitakāyassati` | 8 |
| sn-35/35-247.md:216 | `\#kāyasati \| sandhi` | `kāyasati` is a compound with member sub-rows, not a sandhi; saved DPD has no `kāyasati` headword | DPD lookup: POS `noun`, `fem`, and its compound type | 6 |
| sn-35/35-247.md:495 | `\#kāyasati \| sandhi` | `kāyasati` is a compound with member sub-rows, not a sandhi; saved DPD has no `kāyasati` headword | DPD lookup: POS `noun`, `fem`, and its compound type | 6 |
| sn-56/56-1.md:5 | `karaṇīyo”ti` | Closing `”` has no opening `“` anywhere in the passage (Pāḷi quote balance is edition-dependent) | Owner decision: drop the `”` (`karaṇīyoti`) or restore the opening `“` per the edition | 6 |
| sn-56/56-1.md:94 | `karaṇīyo”ti` | Closing `”` has no opening `“` (Pāḷi quote balance is edition-dependent) | Owner decision: drop the `”` (`karaṇīyoti`) or restore the opening `“` per the edition | 6 |
| sn-56/56-1.md:3 | `‘idaṃ dukkhanti` | Opening `‘` never closed (the `’` is lost in `dukkhanti`); same for each quoted truth on the line | Owner decision: restore `‘idaṃ dukkhan’ti` style or drop the `‘` | 6 |
| sn-56/56-1.md:5 | `‘idaṃ dukkhanti yogo` | Opening `‘` never closed | Owner decision: restore `‘idaṃ dukkhan’ti` style or drop the `‘` | 6 |
| sn-56/56-1.md:31 | `‘idaṃ dukkhanti` | Opening `‘` never closed | Owner decision: restore `‘idaṃ dukkhan’ti` style or drop the `‘` | 6 |
| sn-56/56-1.md:94 | `‘idaṃ dukkhanti yogo` | Opening `‘` never closed | Owner decision: restore `‘idaṃ dukkhan’ti` style or drop the `‘` | 6 |
| sn-56/56-7.md:7, 81 | `‘idaṃ dukkhanti vitakkeyyātha` | Opening ‘ never closed: the closing ’ before `ti` was dropped (SuttaCentral style `‘idaṃ dukkhan’ti`). | `‘idaṃ dukkhan’ti vitakkeyyātha` (check source edition; or drop the ‘ throughout) | 6 |
| sn-56/56-7.md:9, 82 | `dukkhasamudayoti vitakkeyyātha … dukkhanirodhoti vitakkeyyātha … paṭipadāti vitakkeyyātha` | Same unclosed ‘ before each quoted statement (`‘ayaṃ dukkhasamudayoti`, `‘ayaṃ dukkhanirodhoti`, `‘ayaṃ dukkhanirodhagāminī paṭipadāti`). | Close each as `…’ti` (e.g. `‘ayaṃ dukkhanirodho’ti`) per the source edition | 6 |
| sn-56/56-13.md:7, 56 | `‘Pañcupādānakkhandhātissa vacanīyaṃ` | Opening ‘ never closed; the closing ’ before `tissa` was dropped. | `‘Pañcupādānakkhandhā’tissa vacanīyaṃ` (check source edition) | 6 |
| sn-56/56-13.md:7, 11, 13, 17, 56, 101, 148, 181 | `vuccati, bhikkhave, ‘` | `Idaṃ vuccati, bhikkhave, ‘… ariyasaccaṃ.` opens a quote that is never closed. | Close as `‘… ariyasaccan’ti` per the source edition, or drop the ‘ | 6 |
| sn-56/56-25.md:7, 42 | `dukkhanti, bhikkhave, jānato` | `‘Idaṃ dukkhanti` (opened at :5 and :42) lost the closing ’ before `ti`. | `‘Idaṃ dukkhan’ti` (check source edition) | 6 |
| sn-56/56-25.md:9, 43 | `dukkhasamudayoti jānato passato` | `‘Ayaṃ dukkhasamudayoti` (opened at :7 and :42) lost the closing ’ before `ti`. | `‘Ayaṃ dukkhasamudayo’ti` per the source edition | 6 |
| sn-56/56-25.md:11, 66 | `dukkhanirodhoti jānato passato` | `‘Ayaṃ dukkhanirodhoti` lost the closing ’ before `ti`. | `‘Ayaṃ dukkhanirodho’ti` per the source edition | 6 |
| sn-56/56-25.md:13, 67 | `paṭipadāti jānato passato` | `‘Ayaṃ dukkhanirodhagāminī paṭipadāti` (opened at :11 and :66) lost the closing ’ before `ti`. | `‘Ayaṃ dukkhanirodhagāminī paṭipadā’ti` per the source edition | 6 |
| sn-56/56-7.md:46 | `\| 21931 \| kissa \| pron \| masc.dat.sg \|` | The same word in the same phrase `Taṃ kissa hetu?` has ID 21931 here and 21930 at :124, both tagged dat.sg. DPD `kissa 1` is dat ("for what reason?; why?"), `kissa 2` gen; the saved DPD output has no IDs, so which ID is `kissa 1` is not known. | DPD lookup `kissa 1` ID; use it on both rows, keeping `masc.dat.sg` | 6 |
| sn-56/56-27.md:3 | `tasmā ‘ariyasaccānīti vuccanti` | Opening quote with no closing quote before `ti`; quote placement is edition-dependent | Check the source edition; if it closes the quote: `tasmā ‘ariyasaccānī’ti vuccanti` | 6 |
| sn-56/56-27.md:36 | `tasmā ‘ariyasaccānīti vuccanti` | Same unclosed quote; edition-dependent | Check the source edition; if it closes the quote: `tasmā ‘ariyasaccānī’ti vuccanti` | 6 |
| sn-56/56-28.md:3 | `tasmā ‘ariyasaccānīti vuccanti` | Same unclosed quote; edition-dependent | Check the source edition; if it closes the quote: `tasmā ‘ariyasaccānī’ti vuccanti` | 6 |
| sn-56/56-31.md:15 | `‘Idaṃ dukkhanti` | Unclosed quote; edition-dependent | Check the source edition; if it closes the quote: `‘Idaṃ dukkhan’ti` | 6 |
| sn-56/56-31.md:165 | `‘Idaṃ dukkhanti` | Unclosed quote; edition-dependent | Check the source edition; if it closes the quote: `‘Idaṃ dukkhan’ti` | 6 |
| sn-56/56-31.md:17, 166 | `‘ayaṃ dukkhasamudayoti mayā akkhātaṃ` | Same unclosed quotes (three per line: `dukkhasamudayoti`, `dukkhanirodhoti`, `paṭipadāti`); edition-dependent | Check the source edition; if it closes the quotes: `‘ayaṃ dukkhasamudayo’ti`, `‘ayaṃ dukkhanirodho’ti`, `‘ayaṃ dukkhanirodhagāminī paṭipadā’ti` | 6 |
| sn-56/56-31.md:5 | `Appamattakāni, bhante, bhagavatā` | Closing `”ti` with no opening quote (the translation at :102 has one); edition-dependent | Check the source edition; if it opens the quote: `“Appamattakāni, bhante, bhagavatā` | 6 |
| sn-56/56-31.md:80 | `Appamattakāni, bhante, bhagavatā` | Closing `”ti` with no opening quote; edition-dependent | Check the source edition; if it opens the quote: `“Appamattakāni, bhante, bhagavatā` | 6 |
| sn-56/56-34.md:3 | `Āditte, bhikkhave, cele vā sīse vā` | Closing `”ti` with no opening quote (translation :37 has one); edition-dependent | Check the source edition; if it opens the quote: `“Āditte, bhikkhave, cele vā sīse vā` | 6 |
| sn-56/56-34.md:5 | `Āditte, bhante, cele vā sīse vā` | Closing `”ti` (:9) with no opening quote; edition-dependent | Check the source edition; if it opens the quote: `“Āditte, bhante, cele vā sīse vā` | 6 |
| sn-56/56-34.md:21 | `Āditte, bhikkhave, cele vā sīse vā` | Closing `”ti` with no opening quote; edition-dependent | Check the source edition; if it opens the quote: `“Āditte, bhikkhave, cele vā sīse vā` | 6 |
| sn-56/56-34.md:39 | `Āditte, bhante, cele vā sīse vā` | Closing `”ti` (:41) with no opening quote; edition-dependent | Check the source edition; if it opens the quote: `“Āditte, bhante, cele vā sīse vā` | 6 |
| sn-56/56-42.md:34 | `\| \| Ye hi keci \| gen. pron \| \| whatever \| \|` | POS `gen. pron` is not a label used anywhere else; the row duplicates the three member rows that follow, which carry no `#` | owner decision: drop the row or relabel it (e.g. POS `idiom`) and mark the member rows with `#` | 5 |
| mn-107-ganakamoggallanasuttam.md:103 | `pacchimasopānakaḷevarā: imesampi` | Colon after `kaḷevarā` and after `ajjhene` in the Pāli passage; the source edition may have `;` in both places, and the parallel sentences end `issatthe.` / `saṅkhāne.` | Check against the source edition; if confirmed, `pacchimasopānakaḷevarā; imesampi … ajjhene;` | 5 |
| mn-107-ganakamoggallanasuttam.md:428 | `tassa \| pn \| masc.dat.sg \| for that` | `tassa saṃvarāya` can be read as genitive "for the restraint of that [faculty]"; the row reads it as dative and the translation at line 432 as "for that [reason]". Line 500 glosses the same word "to that" | Owner to decide dat or gen; if gen: `gen.sg \| of that [faculty]` here and at line 500, translation "practise for its restraint" | 5 |
| mn-107-ganakamoggallanasuttam.md:470 | `manasā \| noun \| masc.instr.sg` | `mano` tagged masc; saved DPD has only `mana` adj (in comps) and `manindriya` = `mano + indriya` (man**aso**), so the noun's gender is not in the saved output | DPD lookup `mano` (manas group); if nt, `nt.instr.sg` | 5 |
| mn-107-ganakamoggallanasuttam.md:685 | `\#manasi \| noun \| masc.loc.sg` | `mano` tagged masc; saved DPD has only `mana` adj (in comps), so the noun's gender is not in the saved output | DPD lookup `mano` (manas group); if nt, `nt.loc.sg` | 5 |
| mn-107-ganakamoggallanasuttam.md:1926 | `\#kāla \| noun \| masc. \| necklace plant` | The member glosses ("necklace plant" + "fragrant", line 1927) do not add up to the compound gloss at line 1925. DPD has the word as `kāḷānusārī` (no headword `kālānusārī`): masc, dutiyā tappurisa kāḷaṃ + anusārī, "fragrant powder from black sandalwood", so the compound type at line 1925 agrees; the member meanings are not in the saved DPD files. | DPD lookup `kāḷa` and `anusārī` for the member glosses of lines 1926–1927 | 5 |
| mn-107-ganakamoggallanasuttam.md:1945 | `vassikaṃ \| noun \| fem.acc.sg \| jasmine` | Subject of the passive `aggamakkhāyati`, so nominative is expected (cf. `lohitacandanaṃ` nt.nom.sg, line 1936). But DPD has "jasmine" only as fem `vassikā` (nom `vassikā`); `vassika` nt is not in DPD, so changing to `nt.nom.sg` has no support. | DPD lookup: inflections of `vassikā` (is `vassikaṃ` listed as a nominative?), then decide between `fem.acc.sg` and a nominative tag | 5 |

### I. Further details on the material under review

| Location | Current | Problem | Suggested | Conf. |
| --- | --- | --- | --- | --- |
| mn-107-ganakamoggallanasuttam.md:489 | `yato + adhikaraṇa + enaṃ` | From line 489 to line 538 the Construction column switches to the short SN-style notation (`na + saṃ + √var + ta`, `vi + √nī + a + ti`, `√i + a + hi`), then returns to the full style at line 543. The same words have full-style constructions at lines 419–442, so this block looks pasted from another hand | Rewrite lines 489–538 in the full style, copying from the parallel rows at lines 419–442 and 309 | 7 |
| mn-107-ganakamoggallanasuttam.md:946 | `pa + √hā + ya` | Short SN-style construction inside MN 107, which the global finding (audit line 81) says uses the full DPD style; the same word has the full notation at :901 | `pa√hā･1 a (abandon)+ya` | 8 |
| mn-107-ganakamoggallanasuttam.md:776 | `√kar (r \> m) + ma + e` | Short SN-style construction without root class or meaning (refines audit line 81: MN 107 mixes both notations) | `√kar･7 o (do, make)(r \> m)+ma+e` | 6 |
| mn-107-ganakamoggallanasuttam.md:704 | `pari + √sudh + \*e + ti` | Short SN-style construction (refines audit line 81; the `+ ti` ending on an imperative is covered by the known global finding) | `pari√sudh･3 \*e (be pure)+ \*e \> sodhe (caus)+hi` | 6 |
| mn-107-ganakamoggallanasuttam.md:1308 | `na + ā + √rādh + \*e + ti]` | Stray `]` at the end; short SN-style construction (refines audit line 81), while :1304 has the full one | `na + ā√rādh･3 \*e (succeed, please)+ e \> rādhe (caus)+enti` | 8 |
| mn-107-ganakamoggallanasuttam.md:1325 | `ava + √vad + īya + māna]` | Stray `]`; short construction (refines audit line 81), while :1297 has the full one | Copy the construction of :1297 | 8 |
| mn-107-ganakamoggallanasuttam.md:1327 | `anu + √sās + īya + māna]` | Stray `]`; short construction (refines audit line 81), while :1299 has the full one | Copy the construction of :1299 | 8 |
| mn-107-ganakamoggallanasuttam.md:1331 | `ā + √rādh + \*e + ti]` | Stray `]`; short construction (refines audit line 81), while :1304 has the full one | `ā√rādh･3 \*e (succeed, please)+ e \> rādhe (caus)+enti` | 8 |
| mn-107-ganakamoggallanasuttam.md:1333 | `\| nārādhentī”ti. \| verb+ind \| pr.3rd.pl \|` | SN-style `verb+ind` row inside MN 107 (refines audit line 57: MN 107 also mixes sandhi conventions); the same word at :1307–1309 is a `sandhi` row with `\#nārādhenti` (pr.caus.3rd.pl) and `\#iti` member rows | `\| nārādhentī”ti. \| sandhi \| \| “...do not obtain/accomplish…” \| \|` plus the member rows of :1308–1309 | 6 |
| mn-107-ganakamoggallanasuttam.md:1388 | `\| nārādhentī”ti? \| verb+ind \| pr.3rd.pl \|` | Same: `verb+ind` and `pr.3rd.pl` against `sandhi` and `pr.caus.3rd.pl` at :1307–1308 | `\| nārādhentī”ti? \| sandhi \| \| “...do not obtain/accomplish…” \| \|` plus the member rows of :1308–1309 | 6 |
