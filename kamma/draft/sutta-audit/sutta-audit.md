# Audit of `docs/6-pali-class/suttas/`

Date: 2026-11-10. Scope: quality of the grammatical analysis and consistency of file format. Review only; no file in `docs/` was edited.

The folder has two different problems: the format is not uniform across files, and the grammatical analysis has a steady rate of real errors, though it is sound in the main.

Locations are given as `file:line`, where `22-94` means `sn-22/22-94.md` and `mn107` means `mn-107-ganakamoggallanasuttam.md`.

## Coverage

- **Read in full:** every unique analysis for words a– to nis– (about half of the 3,643 unique analyses, drawn from 10,244 filled rows).
- **Read partly:** for nis– to the end of the alphabet, all verbs and participles that have a construction.
- **Heuristic checks only:** nouns, adjectives and compound labels in that second half (ending versus case/number, gender conflicts).
- **Not reviewed:** the English sentence translations, and whether each table matches its Pāli sentence word for word.

## State of the corpus

| Group | Files | State |
|---|---|---|
| `sn-22/`, `sn-35/`, `sn-56/` | 49 | Fully analysed, 6 columns, sentence → table → bold translation |
| `mn-107-ganakamoggallanasuttam.md` | 1 | Fully analysed, but a different format (below) |
| SN 43, 45, 46, 47 combined files | 4 | Stubs: Pāli text plus ID/word lists, all analysis cells empty |
| `nidana-samyutta-sn-12.md` | 1 | Mostly stub; 21 translated blocks, 603 of 644 rows empty |
| SN 22 / 35 / 56 index files | 3 | Link lists |

## Format findings

### Structural (highest priority)

1. **MN 107 has no ID column** (5 columns against 6 everywhere else). It also uses `para N` markers, apostrophe sandhi (`ten’upasaṅkami`), and its own POS labels (`pn`, `ord`, `(pp as) adj`).
2. **The ID column is largely empty in many SN files.** Examples: `sn-35/35-232` has 381 of 530 rows without an ID, `sn-22/22-82` 273 of 523, `sn-35/35-247` 287 of 536, `sn-22/22-59` 182 of 346. Other files (`22-12`, `56-1`, `56-13`) are complete.
3. **Stub tables have no header row.** The first vocabulary word sits above the `| --- |` line, so it renders as the table header (e.g. `| 9320 | asaṅkhataṃ |` in SN 43).
4. **`nidana-samyutta-sn-12.md` lines 818–862 have 7 columns** instead of 6.
5. **The example row leaked in as a table header** at `nidana-samyutta-sn-12.md:371` and `sn-35/35-232.md:662`.
6. **Raw `<br>` appears 82 times in table cells**, which the project's clean-Markdown rule forbids. The files with most are MN 107 (16) and `35-247` (9).
7. **Link label and target disagree:** `maggasamyutta-samyutta-sn-45.md:11` says "SN45.49" but points to the heading "SN45.56".
8. **The instruction paragraph** ("Please make line by line translation…") plus an example table is published in all the index and combined files, with two wordings ("in the last column" / "on the last column").

### Convention drift

- **Sandhi:** MN 107 uses a `sandhi` row plus `#` sub-rows; the SN files mix inline `rūpasmim+api`, `sandhi` rows, and POS such as `noun+ind`, `pron+verb`. `etadavoca` is tagged three different ways.
- **Compound members:** decorated inconsistently as `(ca)`, `+ke`, `(in comps)`, `<br>(ca)`, or a trailing `-`.
- **Multi-word cells:** `na madāya`, `bhavaṃ gotamo`, `ehi tvaṃ`; punctuation left in the Pāli cell (`vineti —`, `saṃvasati”`, `dasakā’ti`).
- **Headings:** `SN 43.1` against `SN46.1`; title case is mixed (`Aniccasutta` / `tatiyāssādasutta`); "Bojjhaṅgasaṃyutta Saṃyutta" and "Maggasaṃyutta Saṃyutta" are redundant; `56-28` lacks the `---` after the full text.
- **Quotes:** curly quotes and apostrophes in some files only (MN 107, SN 12, parts of SN 56).
- **Stray characters:** 82 construction cells have an unbalanced `[` or `]`; there are escaped backticks (``opt.3rd.sg\` ``), bold inside a cell (`aññathābhāv**ino**`), and a capitalised `Appamattakāni`.

### Label vocabulary

- **POS has 66 distinct values.**
  - Typos: `veerb`, `insd`, `nou`, `prom`, `pron.`, `ind.`, `adj (app)`.
  - Gender used as POS: `masc`, `nt` (6 times in `56-44`).
  - Synonyms: `ptp` / `fpp` / `adj (ptp)`; `pp (adj)` / `pp/adj` / `pp(adj)` / `adj (pp)` / `(pp as) adj`.
  - Nine rows have no POS.
- **Grammar has about 290 distinct values.**
  - Typos: `masc.nomsg` (18), `masc.acc.g` (9), `masc.voc,sg` (6), `masc.genb.sg` (4), `nt.acc.ag`, `fen.gen.sg`, `nt.no.sg`, `masc.nomm.sg`, `nt.inst.sg`, `masc.nom.pl.medium`.
  - Variants: `abs` / `abs.` / `ger` / `ger/abs` / `abs/ger`; `reflex` / `reflx`; `loc abs` / `loc. abs` / `loc.abs`; `quotation mark` / `quotation` / `quote`.
- **Compound types mix Pāli and English.**
  - `chaṭṭhī tappurisa` (155) sits beside `genitive tappurisa`, `accusative`, `locative`, `instrumental`, `ablative tappurisa?`.
  - Misspellings: `chaṭṭa`, `chaṭṭha`, `chatti`, `dutiya`, `sattāni tappurisa (?)`, `kammādhāraya`, `avyayībhāva`.
  - The bahubbīhi notation has six spellings (`kammadhāraya\> bahubbīhi`, `kammadhāraya \> bahubbīhi`, `kammadhāraya\>bahubbīhi`, `kammadhāraya \>bahubbīhi`, `kammadhāraya as bahubbīhi`, plain `bahubbīhi`).
- **The Construction column holds three kinds of content:** root derivation, compound type, and free commentary ("*probably truncated ablative (Bodhi)", "both words together suggest…").
- **Two derivation notations:** MN 107 uses the full DPD style (`ni√sad･1 a (sink, sit, settle)+…`); the SN files use `ni + √sad + a + na`.
- **178 non-present verbs carry a present-tense construction** ending in `+ ti` (e.g. `desessāmi` → `√dis + *e + ti`), while others show the real ending.
- **About 15 constructions are truncated** (`√vad`, `nī + √sar`, `vi + √likh`, `saṃ + √chid`, `ud + √i`, `vi + √takk`, `nī + √yat`, `upa + ni + √khip`, `√caj`, `vi + ā + √pad`).

## Grammatical findings

### Definite errors

| Location | Row | Problem |
|---|---|---|
| `22-94:54` (10 rows) | `vadāmi` pr.3rd.sg | should be 1st.sg |
| `35-118:100` (3 rows) | `santi` pr.3rd.sg | should be 3rd.pl |
| `35-230:136` | `abhinandati` pr.3rd.pl | should be 3rd.sg |
| `22-12:74` (4 rows) | `karaṇīyaṃ` POS `prp` | should be ptp |
| `35-118:234–235` | `anabhinandato`, `anabhivadato` POS `pp` | prp (the construction itself ends in `nta`) |
| `56-47:65` | `ummujjanto` POS `pp` | prp |
| `22-26:23` | `anabhisambuddhassa` POS `noun` | pp |
| `22-58:188` | `akkhātā` pp, `ā + √khā + ta` | agent noun (akkhātar), not a pp |
| `22-82:505, 511, 517` | `saññā-/saṅkhāra-/viññāṇakkhandhassa` masc.nom.sg | gen/dat |
| `35-118:237` | `tiṭṭhato` masc.nom.sg | dat/gen |
| `35-28:50` | `bhikkhū` masc.acc.sg | acc.pl |
| `mn107:195`, `:191` | `cattāri` nt.nom.sg; `dve` masc.acc.sg | plural |
| `mn107:994`, `:993` | `dhammesu`, `kusalesu` loc.sg | loc.pl |
| `mn107:1170` | `atthaṅgamā` instr.sg | abl.sg |
| `35-246:154` | `me` 1st.acc.sg | dat ("for me") |
| `22-82:65` | `mātuyā` fem.loc.sg | gen |
| `56-1:122` | `dukkhanirodhagāminī` masc.nom.sg | fem |
| `22-23:65`, `:67` | `pariññeyyā` masc.nom.sg; `katamā` masc.fem.sg | first should be nom.pl; second fem.nom.sg |
| `35-241:532` (4), `22-82:127`, `22-63:62` | `labheyyaṃ`, `puccheyyaṃ`, `vihareyyāmi` tagged reflexive | ordinary active optatives |
| `56-33:61` | `gacchanti` construction `√gam + a + nta` | `+ nti` |
| `35-53:51` (10) | `jānato` construction `√ñā + nā + a` | `+ nta` |
| `22-78:262`, `22-26:27` | `samānā`, `sato` with `sa + √as` | no `sa` prefix |
| `22-12:29` | `evaṃ` ind, grammar `adj` | adv |
| `35-28:268` | `attano` POS `masc` | pron/noun |

### Wrong gender

- `cittaṃ` masc (`mn107:642`); `cakkhundriyaṃ` and `manindriyaṃ` masc (`mn107:418, 439, 440, 490, 511, 512`); `rūpaṃ` masc (`mn107:396`); `ghānena` masc (`mn107:454`); `rūpesu` masc (`35-70:90`).
- `pāde` nt (`mn107:676`); `gīvaṃ` nt (`56-47:69`); `attena` nt (`35-85:50`); `appaṭivānī` masc (`56-34:64`).
- `cittāni` tagged `nt.masc.pl` (`35-28:284`).
- Split within one file: `jāgariyaṃ` fem and nt, `bhojane` nt and masc, `satisampajaññena` nt and masc (all MN 107); `kulānaṃ` nt and masc across files.

### Wrong or doubtful compound analysis

- `khīṇāsavā`, `katakaraṇīyā` given as "dutiyā tappurisa" (`mn107:1225, 1229`): these are bahubbīhi.
- `attamanā` given as "chaṭṭhī tappurisa" (`35-28:267`): bahubbīhi.
- `bhikkhusahassena` given as "digu" (`35-28:45`, also `:281`): chaṭṭhī tappurisa. `chappāṇake` given as "kammadhāraya" (`35-247:293`): this one is the digu.
- `dhammamayo` given as "instrumental tappurisa" (`35-228:104`, `:110`): `-maya` is a suffix, not a compound member.
- `pātimokkhasaṃvarasaṃvuto` given as "sattamī tappurisa" (`mn107:323`): tatiyā.
- The same compound is labelled differently: `dukkhanirodhaṃ` (chaṭṭhī tappurisa at `56-1:66` / "kammadhāraya > bahubbīhi" at `56-13:42`), `andhakāratimisā` (kammadhāraya fem.sg at `56-38:46` / dvanda nt.pl at `56-38:104`), `mahiddhiko` / `mahesakkho` (`22-78:134`, `:144`).

### Other doubtful rows (lower certainty, worth a second look)

- `bhūmirāmaṇeyyakaṃ` adj masc.acc.sg (`mn107:1560`): looks like a neuter noun.
- `kāraṇaṃ` masc.acc.sg (`mn107:288, 292`): not masculine.
- `khemaṃ` noun masc.acc.sg (`mn107:1204`).
- `mūlagandhā` masc.nom.sg (`mn107:1922`): plural in context ("ye keci mūlagandhā").
- `atthāya` POS adj (`35-241:645`): noun.
- `saṃhitaṃ` pp masc.nom.pl (`56-31:142`).
- `vutte` masc.loc.sg (`mn107:1273`) against nt.loc.sg (`35-241:246`).
- `doṇiṃ` tagged `fem.nom.acc` (`35-246:243`): fem.acc.sg.
- `nibbānaninnā` tagged `masc.fem.nom` (`35-241:230`).
- `gayāyaṃ` as compound member tagged fem.gen.sg (`35-28:42`): form and tag disagree.
- `jātisaṃvattanike+pi` tagged masc.loc.pl (`56-42:243`): form and tag disagree.
- `me` 1st.instr.sg glossed "to me" (`mn107:17`): gloss does not match the tag ("by me").
- `aññamañña` labelled "dutiyā tappurisa" (`56-47:159`).
- `āvuso` POS ind with grammar `masc.voc.sg` (`35-232:97`).

### Pāli text typos in the word column

- `kukkurao` (`35-247:381`), `imina` (`35-241:390`), `ko nu kno` (`22-26:37`), `pajānati` (`56-49:157`, 4 rows), `viññāṇasmim` without `pi` (`22-12`), `itthattāyā` (`22-12:76`).
- `bhagavā` tagged instr.sg (`56-31:86`): the tag suggests the word should be `bhagavatā`.

### Systematic inconsistencies

- Passive against active: `virajjati`, `vimuccati`, `nirujjhati` are `pr.pass` in some files and `pr` in others.
- Causative marking: `deseti` / `desessāmi` appear both as `pr.caus` / `fut.caus` and plain `pr` / `fut`.
- `addasā` is `imperf` once (`35-241:76`); all similar forms are `aor`.
- `ger` is used for `-ya` forms and `abs` for `-tvā` forms in most files, but `ger/abs`, `abs/ger` and `abs` on `-ya` forms (`samādāya`, `viññāya` in MN 107) also occur.
- Cardinal numbers: `x.nom.pl`, `masc.x.pl`, `(in comps)` and plain gender labels are all used.

## Recommendation

Fix in this order:

1. **Decide the canonical schema**: 6 columns with ID, one sandhi convention, a closed POS/Grammar/compound vocabulary. Write it down; everything else depends on it.
2. **Normalise the labels mechanically** with a script (typos, synonyms, brackets, `<br>`). This is low risk and removes most of the noise.
3. **Correct the grammatical errors above by hand.**
4. **Backfill the missing IDs and convert MN 107**, which is the largest job.

Optional follow-up: turn the checks used for this audit into a permanent verifier script (new script plus README entry) so regressions are caught. Not started.

## Remaining work for a complete audit

- Full read of nouns, adjectives and compound labels for words nis– to the end of the alphabet.
- Review of the English sentence translations against the Pāli.
- Check that each table matches its Pāli sentence word for word.

## Method

- All filled table rows were extracted by script (10,244 rows) and deduplicated to 3,643 unique analyses (word, POS, grammar, construction).
- Format counts (columns, headers, missing IDs, `<br>`, label vocabularies, brackets) come from scripts run over all 58 files.
- Grammatical findings come from reading the deduplicated list, plus heuristic checks of ending against case/number, POS against construction suffix, and gender conflicts for the same word form.
- The scripts were temporary and live in the session scratchpad, not in the repository.

## Confidence

- 9/10 on the format findings, which are counted by script.
- 8/10 on the grammatical errors in the "Definite errors" table.
- 6/10 that the list is complete, for the reasons under "Remaining work".
