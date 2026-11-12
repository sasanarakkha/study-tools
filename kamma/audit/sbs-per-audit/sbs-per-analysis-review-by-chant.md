# SBS Pāḷi–English chant analysis — merged review, in reading order

Date: 2026-11-09. Source of every suggestion: (1) the original audit `sbs-per-analysis-audit.md` Parts 1–8 (**A**), (2) the second review found in `temp/Chanting Book Analaysis*` (**B**, "Reviewer B"; the two folders are identical). Rebuilt here **per chant, in line order**, so that everything about one chant is read in one place. Line numbers refer to the current files in `docs/6-pali-class/sbs-per-analysis/` (unchanged since the audit; match on the quoted text, not the line number alone).

## How to use

1. **Policies first** (next section): each policy affects many rows. Delete the policy line you reject, or for an A/B policy pair keep one. Rows belonging to a policy carry its tag in the *Source* column.
2. **Then read chant by chant.** Delete any row you disagree with. Rows marked ⚔ are conflicts: delete the option you do not want from inside the row (or the whole row to reject both). Rows marked ✗ are my recommended rejections of Reviewer B suggestions — they are kept so nothing is lost, and are **not** implemented unless you delete the ✗ mark.
3. Hand the file to an implementing agent. **Agent rules:** match on quoted current text and grep before every edit; stop and report on mismatch; never change Pāḷi chant lines unless a row says so explicitly; implement nothing from a policy whose line was deleted; where two rows touch the same cell, the specific row beats the bulk-policy row; never implement a ✗ or ⚑ row; if a ⚔ row still lists both options, stop and ask.

**Source column legend**

| Tag | Meaning |
|---|---|
| A1 / A2 / A3 | audit Part 1 (`ṃ` corruption) / Part 2 (shifted columns) / Part 3 (split glosses) |
| A4 | audit Part 4 grammar-tag correction |
| A5.n | audit Part 5 notation rule *n*, **computed per row** for this document (the audit gave only examples/counts) |
| A6 / A7 | audit Part 6 translation typos / Part 7 content errors |
| A8-Dn | audit decision Dn |
| B-Nxx | Reviewer B, specific new correction |
| B-Cn | conflict between audit and Reviewer B at this place |
| B-Pn, B-11.n | Reviewer B bulk policy (see policy list) |
| B-Qn | Reviewer B change to Pāḷi chant text (decision) |
| B-Xn ✗ | Reviewer B suggestion I recommend rejecting |
| B-X2 ⚑ | `na` Grammar `neg` → ∅ — weak rejection, left for your decision; not implemented unless you remove the ⚑ |
| B=A | Reviewer B proposes the same as the audit (no extra action) |
| ✔ | appended to an audit row when Reviewer B proposes the identical change |

## Policies (decide once, applies to the tagged rows)

| Policy | From | Rule | Rows |
|---|---|---|---|
| **A5.1** | Audit 5.1 | `1st`/`2nd`/`3rd` → `1`/`2`/`3` in Grammar | 19 |
| **A5.2** | Audit 5.2 | `instr`/`inst` → `ins` | 20 |
| **A5.3** | Audit 5.3 | reflexive notation → `refl`, mood first (`imp.refl.1.pl`). **Pair with B-11.2 — keep one.** | 14 |
| **A5.4** | Audit 5.4 | `emphat`/`emph.`/`emp` → `emph` | 1 |
| **A5.5** | Audit 5.5 | `pres` → `pr` | 0 |
| **A5.6** | Audit 5.6 | compressed one-letter tags (`m.n.s`, `nt.i.sg` …) → full form | 14 |
| **A5.7** | Audit 5.7 | strip trailing periods in tags (bare `masc.`→`masc`; **keeps** bare gender on compound members — pair with B-11.3) | 50 |
| **A5.8** | Audit 5.8 | composite POS (`verbinf`, `verbaor.1.s`, …) → POS + Grammar | 3 |
| **A5.9** | Audit 5.9 | `v.pass`/`v.caus`/`v.refl`/`prp.caus` → `verb`/`prp` + tag in Grammar | 12 |
| **A5.10** | Audit 5.10 | `neg`/`conj`/`interr`/`prep`/`adv` in the POS column → POS `ind`, word moved to Grammar. *Caveat: the audit text also lists `card`; I did not compute `card` rows because audit D4 and B-P8 want POS `card` — confirm.* | 9 |
| **A5.11** | Audit 5.11 | `from loc.sg` → `adv`; `from ger` → `ger` | 1 |
| **A5.12** | Audit 5.12 | `fem nom pl` → `fem.nom.pl` | 1 |
| **D3** | Audit D3 | `<br>` inside tables: keep (document exception) or convert `A<br>(or)<br>B` → `A (or) B` | 6 |
| **D4** | Audit D4 | unify composite POS values (`pp as adj`, `adj (as noun)`, `v + pn`, …) — **decision needed which form**; Reviewer B's rows (B-N…) already propose one form for the `pp as adj` / `adj (as noun)` family | 21 |
| **D5** | Audit D5 | unbold Pāḷi chant lines that are bolded like translations | 19 |
| **D8** | Audit D8 | quote-style sweep (straight apostrophes, balanced pairs) | 22 |
| **B11.2** | Reviewer B 11.2 | **drop `refl`** (`imp.1.pl`) — *alternative to A5.3, keep one* | 7 |
| **B11.3** | Reviewer B 11.3 | **blank** Grammar of compound members (`word-`) that carry a bare gender — *alternative to the A5.7 keep-bare-gender stance; 531 of ~700 compound rows are already empty* | 34 |
| **B11.4** | Reviewer B 11.4 | POS `ger`/`abs` with empty Grammar instead of `verb`+`ger`/`abs` — *alternative to the corpus convention (130 rows keep `verb`); if chosen, extend to all rows* | 20 |
| **BP1** | Reviewer B P1 | `ind` rows: Grammar ∅ → `adv` (DPD sub-type) | 128 |
| **BP2** | Reviewer B P2 | `ca` etc: Grammar ∅ → `conj` | 114 |
| **BP3** | Reviewer B P3 | Grammar ∅ → `emph` | 46 |
| **BP4** | Reviewer B P4 | Grammar ∅ → `excl` (`handa`, `namo`, `vata`, `addhā`) | 21 |
| **BP5** | Reviewer B P5 | Grammar ∅ → `prep` | 5 |
| **BP6** | Reviewer B P6 | Grammar ∅ → `interr` | 8 |
| **BP7** | Reviewer B P7 | POS `ind` → `sandhi` for fused words (`kiñcāpi`, `yadidaṃ`, `n'eva` …); leave Grammar empty | 17 |
| **BP8** | Reviewer B P8 | numerals POS `adj` → `card` | 5 |

Note: P-tagged rows of the **BP** policies are written in the tables with source `B-Pn`; the **A5.n** rows with source `A5.n`.

---

## 01 — Dedication of Offerings

`per-01-dedication-of-offerings.md` — 22 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 01-01 | 11 |  | `Fortunate One the Buddha` → `Fortunate One, the Buddha` *(same fix at: per-01:11, per-01:76)* | A6 |
| 01-02 | 13 |  | `totally perfectly` → `totally, perfectly` *(same fix at: per-01:13, per-01:126)* | A6 |
| 01-03 | 13 | `sammā-` | Grammar ∅ → `adv` | B-P1 |
| 01-04 | 14 | `sambuddho` | Eng `one who has thoroughly understood, being enlightened, a Buddha, fully awakened one` → `one who has thoroughly understood, being enlightened, a Buddha` — *drops `, fully awakened one` from the gloss — loses information; consider keeping the long form* | B-N124 |
| 01-05 | 46 | `mayaṃ` | `1.nom.` → `1.nom.pl` — number missing  ✔ *Reviewer B proposes the same.* | A4 |
| 01-06 | 48 | `sa-` | POS `pron` → `prefix`; Eng `one's own, his own OR with` → `with, accompanied by` — *`sa-` as prefix = "with"* | B-N83 |
| 01-07 | 50 | `sa-` | POS `pron` → `prefix`; Eng `one's own, his own OR with` → `with, accompanied by` — *same as 01:48* | B-N84 |
| 01-08 | 73 | `sādhu` | Gr ∅ → `excl`; Eng `it is good, would be good, please` → `it is good (for); it would be good (if)` | B-N76 |
| 01-09 | 76 |  | `Fortunate One the Buddha` → `Fortunate One, the Buddha` *(same fix at: per-01:11, per-01:76)* | A6 |
| 01-10 | 77 |  | **D3** `<br>` inside table cells (lines 77). Policy: keep (note the exception) or convert `A<br>(or)<br>B` → `A (or) B`. | A8-D3 |
| 01-11 | 77 | `sucira- (or) suciraṃ` | POS `adj` → `ind` (leave Grammar empty) — *reviewer also wrote `ind` into Grammar (duplicate; see X1) — only the POS change is proposed here* | B-N85 |
| 01-12 | 78 |  | `who's fire is out` → `whose fire is out` *(same fix at: per-01:78, per-06:470)* | A6 |
| 01-13 | 79 | `api` | ⚔ **C1 — keep ONE:** **Option A (audit)** Part 5.4: Grammar `emphat` → `emph`  ·  **Option B (reviewer)** Grammar `emphat` → ∅ (empty)  ·  *DPD lists `api` as plain `ind`.* | B-C1 |
| 01-14 | 88 |  | `latest , later` → `latest, later` | A6 |
| 01-15 | 91 | `mānasā` | Grammar `nt.abl/instr.sg` → `nt.abl/ins.sg` | A5.2 |
| 01-16 | 91 | `mānasā` | Gr `nt.abl/instr.sg` → `nt.ins.sg`; Eng `from (with) a mind, intention` → `with a mind, intention` — *extends audit Part 5.2* | B-N21 |
| 01-17 | 102 | `paṇṇākāra-` | Gr ∅ → `masc` — *adds bare gender — contradicts policy 11.3 (B)* | B-N22 |
| 01-18 | 126 |  | `totally perfectly` → `totally, perfectly` *(same fix at: per-01:13, per-01:126)* | A6 |
| 01-19 | 126 | `sammā-` | Grammar `adv.` → `adv`  ✔ *Reviewer B proposes the same.* | A5.7 |
| 01-20 | 146 | `svākkhāto` | POS `pp as adj` — unify to one form (see policy D4) | A8-D4 |
| 01-21 | 146 | `svākkhāto` | POS `pp as adj` → `adj` — *D4: unify `pp as adj`* | B-N86 |
| 01-22 | 159 |  | `I venerate to the Teaching.` → `I venerate the Teaching.`  ✔ *Reviewer B proposes the same.* | A6 |

## 02 — Preliminary Homage

`per-02-preliminary-homage.md` — 7 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 02-01 | 9 | `handa` | Grammar ∅ → `excl` | B-P4 |
| 02-02 | 13 | `pubbabhāga-` | POS `adj` → `noun` | B-N87 |
| 02-03 | 16 | `namakāraṃ` | Gr `nt.acc.sg` → `masc.acc.sg` — *DPD: kāra masc.* | B-N23 |
| 02-04 | 18 | `\>kāraṃ` | Gr `nt.acc.sg` → `masc.acc.sg` — *DPD: kāra masc.* | B-N24 |
| 02-05 | 19 | `karomase` | Grammar `ref.imp.1.pl` → `imp.refl.1.pl` | A5.3 |
| 02-06 | 19 | `karomase` | Grammar `ref.imp.1.pl` → `imp.1.pl` (reviewer drops `refl`; audit 5.3 keeps it: `imp.refl.1.pl`) — policy 11.2 | B-11.2 |
| 02-07 | 27 | `namo` | Grammar ∅ → `excl` | B-P4 |

## 03 — Homage to the Buddha

`per-03-homage-to-the-buddha.md` — 14 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 03-01 | 9 | `handa` | Grammar ∅ → `excl` | B-P4 |
| 03-02 | 13 | `karomase` | Grammar `ref.pr.1.pl` → `imp.refl.1.pl` | A5.3 |
| 03-03 | 13 | `karomase` | Grammar `ref.pr.1.pl` → `imp.1.pl` (reviewer drops `refl`; audit 5.3 keeps it: `imp.refl.1.pl`) — policy 11.2 | B-11.2 |
| 03-04 | 25 | `sammā-` | Grammar ∅ → `adv` | B-P1 |
| 03-05 | 46 | `bhagavā` | POS `adj` → `noun`; Eng `fortunate, illustrious, sublime, blessed, happy glorious, auspicious` → `Sublime One, Blessed One, Fortunate One` — *DPD: bhagavant 1 = masc noun* | B-N88 |
| 03-06 | 71 | `abhiññā` | POS `verb` → `ger`, Grammar `ger` → ∅ (reviewer; audit/corpus keep `verb` + `ger`) — policy 11.4 | B-11.4 |
| 03-07 | 72 | `sacchikatvā` | POS `verb` → `abs`, Grammar `abs` → ∅ (reviewer; audit/corpus keep `verb` + `abs`) — policy 11.4 | B-11.4 |
| 03-08 | 75 |  | `himself  higher understanding` → `himself higher understanding` (double space) | A6 |
| 03-09 | 90 |  | Pāḷi chant text: `sātthaṃ sabyañjaṇaṃ kevala-paripuṇṇaṃ …` → `sabyañjaṇaṃ` → `sabyañjanaṃ` — headword row per-03:95 is already `sabyañjanaṃ`; DPD spelling  *(decision; data-preservation rule)* | B-Q1 |
| 03-10 | 94 | `sātthaṃ` | Gr `masc.acc.sg` → `nt.acc.sg` — *agrees with neuter `brahmacariyaṃ` (also next 3 rows)* | B-N25 |
| 03-11 | 95 | `sabyañjanaṃ` | Gr `masc.acc.sg` → `nt.acc.sg` — *same* | B-N26 |
| 03-12 | 97 | `paripuṇṇaṃ` | Gr `masc.acc.sg` → `nt.acc.sg` — *same* | B-N27 |
| 03-13 | 98 | `parisuddhaṃ` | Gr `masc.acc.sg` → `nt.acc.sg` — *same* | B-N28 |
| 03-14 | 119 |  | `my head  to` → `my head to` | A6 |

## 04 — Homage to the Dhamma

`per-04-homage-to-the-dhamma.md` — 4 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 04-01 | 9 | `handa` | Grammar ∅ → `excl` | B-P4 |
| 04-02 | 13 | `karomase` | Grammar `imp.ref.pr.1.pl` → `imp.refl.1.pl` | A5.3 |
| 04-03 | 13 | `karomase` | Grammar `imp.ref.pr.1.pl` → `imp.1.pl` (reviewer drops `refl`; audit 5.3 keeps it: `imp.refl.1.pl`) — policy 11.2 | B-11.2 |
| 04-04 | 37 | `paccattaṃ` | POS `adv` → `ind`; Grammar `ind` → `adv`  ✔ *Reviewer B proposes the same.* | A5.10 |

## 05 — Homage to the Saṅgha

`per-05-homage-to-the-sangha.md` — 10 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 05-01 | 9 | `handa` | Grammar ∅ → `excl` | B-P4 |
| 05-02 | 13 | `karomase` | Grammar `imp.ref.pr.1.pl` → `imp.refl.1.pl` | A5.3 |
| 05-03 | 13 | `karomase` | Grammar `imp.ref.pr.1.pl` → `imp.1.pl` (reviewer drops `refl`; audit 5.3 keeps it: `imp.refl.1.pl`) — policy 11.2 | B-11.2 |
| 05-04 | 58 | `yadidaṃ` | POS `adv` → `ind`; Grammar `ind` → `adv` | A5.10 |
| 05-05 | 58 | `yadidaṃ` | ⚔ **same cells as the A5.10 row above — keep ONE:** **Option A (A5.10)** POS `adv` → `ind`, Grammar `ind` → `adv`  ·  **Option B (B-P7)** POS `adv` → `sandhi`, Grammar `ind` → ∅ (reviewer himself wrote `sandhi` in both POS and Grammar; I recommend Grammar empty)  ·  *Do not apply both.* | B-P7 |
| 05-06 | 59 | `cattāri` | `masc.nom.pl` → `nt.nom.pl` — agrees with neuter `purisayugāni` | A4 |
| 05-07 | 59 | `cattāri` | POS `adj` → `card` | B-P8 |
| 05-08 | 61 | `aṭṭha` | POS `adj` → `card` | B-P8 |
| 05-09 | 76 |  | Pāḷi chant text: `āhuṇeyyo pāhuṇeyyo dakkhiṇeyyo …` → `āhuneyyo pāhuneyyo` — headword rows per-05:80/81 and per-57:68/69 already `āhuneyyo`/`pāhuneyyo`; per-57 chant line was not flagged  *(decision; data-preservation rule)* | B-Q2 |
| 05-10 | 100 | `ahaṃ` | Eng `i` → `I` — *capital I* | B-N125 |

## 06 — Salutation to The Triple Gem

`per-06-salutation-to-the-triple-gem.md` — 47 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 06-01 | 9 | `handa` | Grammar ∅ → `excl` | B-P4 |
| 06-02 | 11 | `ratanattaya-` | Grammar `nt.` → `nt` | A5.7 |
| 06-03 | 12 | `paṇāma-` | Grammar `masc.` → `masc` | A5.7 |
| 06-04 | 14 | `ceva` | ⚔ **C12 — keep ONE:** **Option A (audit)** Part 1: POS `idioṃ` → `idiom`  ·  **Option B (reviewer)** POS `idioṃ` → `sandhi`  ·  *Also affects every other `idioṃ` row if B is taken as a principle (see Part 14 P7).* | B-C12 |
| 06-05 | 15 | `saṃvega-` | Grammar `masc.` → `masc` | A5.7 |
| 06-06 | 18 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 06-07 | 19 | `bhaṇāmase` | Grammar `imp.reflx.1.pl` → `imp.refl.1.pl` | A5.3 |
| 06-08 | 19 | `bhaṇāmase` | Grammar `imp.reflx.1.pl` → `imp.1.pl` (reviewer drops `refl`; audit 5.3 keeps it: `imp.refl.1.pl`) — policy 11.2 | B-11.2 |
| 06-09 | 100 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 06-10 | 140 |  | `those who seen the peace` → `those who have seen the peace` | A6 |
| 06-11 | 146 |  | **D3** `<br>` inside table cells (lines 146, 175). Policy: keep (note the exception) or convert `A<br>(or)<br>B` → `A (or) B`. | A8-D3 |
| 06-12 | 158 |  | Rebuild row: `\| saṅghaṃ \| noun \| masc.acc.sg \| Community, assembly \|` | A2 |
| 06-13 | 169 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 |
| 06-14 | 174 | `evaṃ-` | Grammar ∅ → `adv` | B-P1 |
| 06-15 | 177 | `vatthu-ttayaṃ` | Gr `masc.acc.sg` → `nt.acc.sg` — *`vatthu` neuter* | B-N29 |
| 06-16 | 178 | `vandayatā` | Grammar `masc.instr.sg.` → `masc.ins.sg` | A5.2/7 |
| 06-17 | 178 | `vandayatā` | POS `pp` → `prp`; Gr `masc.instr.sg.` → `masc.ins.sg`; Eng `by respected; revered; honoured` → `by one venerating, paying respect` — *extends audit Part 5.2 (`instr` → `ins`)* | B-N89 |
| 06-18 | 186 | `abhisaṅkhataṃ` | Gr `masc.acc.sg` → `nt.acc.sg` — *agrees with neuter `vatthuttayaṃ`* | B-N30 |
| 06-19 | 188 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 |
| 06-20 | 194 | `yaṃ` | Grammar ∅ → `adv` | B-P1 |
| 06-21 | 199 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 |
| 06-22 | 205 | `ve` | Grammar ∅ → `emph` | B-P3 |
| 06-23 | 221 | `sammā-` | Grammar ∅ → `adv` | B-P1 |
| 06-24 | 231 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 06-25 | 249 | `evaṃ` | Grammar ∅ → `adv` | B-P1 |
| 06-26 | 250 | `jānāma` | `pr.3.pl` → `pr.1.pl` — "we know" is 1st person  ✔ *Reviewer B proposes the same.* | A4 |
| 06-27 | 258 | `jāti` | Grammar `f.n.sg` → `fem.nom.sg` | A5.6 |
| 06-28 | 269 |  | Rebuild row: `\| dukkha- \| noun \| \| discomfort, suffering, pain, unease, something unsatisfactory, problem, trouble \|` | A3 |
| 06-29 | 301 | `yam-(p)-icchaṃ` | POS `m.ac.s` → `noun`; Grammar ∅ → `masc.acc.sg` (tag sits in POS column; `noun` is my inference — confirm) | A5.6 |
| 06-30 | 329 | `upādānakkhandho` | POS `m.n.s` → `noun`; Grammar ∅ → `masc.nom.sg` (tag sits in POS column; `noun` is my inference — confirm) | A5.6 |
| 06-31 | 331 | `upādānakkhandho` | POS `m.n.s` → `noun`; Grammar ∅ → `masc.nom.sg` (tag sits in POS column; `noun` is my inference — confirm) | A5.6 |
| 06-32 | 333 | `upādānakkhandho` | POS `m.n.s` → `noun`; Grammar ∅ → `masc.nom.sg` (tag sits in POS column; `noun` is my inference — confirm) | A5.6 |
| 06-33 | 335 | `upādānakkhandho` | POS `m.n.s` → `noun`; Grammar ∅ → `masc.nom.sg` (tag sits in POS column; `noun` is my inference — confirm) | A5.6 |
| 06-34 | 337 | `upādānakkhandho` | POS `m.n.s` → `noun`; Grammar ∅ → `masc.nom.sg` (tag sits in POS column; `noun` is my inference — confirm) | A5.6 |
| 06-35 | 350 | `evaṃ` | Grammar ∅ → `adv` | B-P1 |
| 06-36 | 351 | `bahulaṃ` | POS `adv` → `ind`; Grammar `` → `adv` | A5.10 |
| 06-37 | 355 |  | `during his live` → `during his life` | A6 |
| 06-38 | 362 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 06-39 | 366 |  | Rebuild row: `\| sāvakesu \| noun \| masc.loc.pl \| among disciples, pupils, lit. hearers \|`  ✔ *Reviewer B proposes the same.* | A2 |
| 06-40 | 384 | `aniccā` | Gr `fem.nom.sg` → `masc.nom.pl` — *`aniccā` agrees with `saṅkhārā` (masc.pl)* | B-N31 |
| 06-41 | 394 | `anattā` | POS `noun` → `adj`; Gr `masc.nom.pl` → `masc.nom.sg` — *reviewer wrote `masc.nom.s`; converted to repo canonical* | B-N90 |
| 06-42 | 414 |  | Grammar `masc.nom.sg` → `masc.nom.s` — **recommended reject:** Notation-only, against the `.sg` canon. | **B-X4✗** |
| 06-43 | 461 | `paññāyethā'ti` | Grammar `opt.ref.3.sg` → `opt.refl.3.sg` | A5.3 |
| 06-44 | 470 |  | `who's fire is out` → `whose fire is out` *(same fix at: per-01:78, per-06:470)* | A6 |
| 06-45 | 473 | `uddissa` | Gr `ind` → ∅ — *gerund: no inflectional grammar* | B-N77 |
| 06-46 | 496 | `brahmacariyaṃ` | Gr `masc.acc.sg` → `nt.acc.sg` — *`brahmacariya` neuter* | B-N32 |
| 06-47 | 499 |  | `under  the` → `under the` | A6 |

## 07 — The Buddha's First Exclamation

`per-07-the-buddhas-first-exclamation.md` — 2 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 07-01 | 35 | `puna` | Grammar `adv.` → `adv`  ✔ *Reviewer B proposes the same.* | A5.7 |
| 07-02 | 50 | `ajjhagā` | ⚔ **C3 — keep ONE:** **Option A (audit)** Part 4: Grammar → `aor.3.sg`  ·  **Option B (reviewer)** Grammar → `imperf` (reviewer dropped person/number; if B is kept write `imperf.3.sg`)  ·  *Audit Part 4 has the same pair for `per-54:126`; use the same choice for both. Reviewer did not touch per-54:126.* | B-C3 |

## 08 — Respect for The Dhamma

`per-08-respect-for-the-dhamma.md` — 15 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 08-01 | 14 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 08-02 | 18 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 08-03 | 22 | `c'etarahi` | POS `ind` → `sandhi` (leave Grammar empty; reviewer also wrote `sandhi` in Grammar — not recommended) | B-P7 |
| 08-04 | 40 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 08-05 | 41 | `atha-api` | POS `ind` → `sandhi` (leave Grammar empty; reviewer also wrote `sandhi` in Grammar — not recommended) | B-P7 |
| 08-06 | 43 | `esā` | POS `noun` → `pron` — *DPD: pron, fem.nom.sg of eta* | B-N91 |
| 08-07 | 55 | `hi` | Grammar ∅ → `emph` | B-P3 |
| 08-08 | 57 | `mahattam-` | Rebuild row as `\| mahattam- \| noun \| nt.acc.sg \| greatness; illustriousness \|` — *gender tag was in POS column* | B-N1 |
| 08-09 | 58 | `abhikaṅkhatā` | POS `pp` → `prp` — *active present participle (reviewer: one longing/aspiring); gloss unchanged* | B-N92 |
| 08-10 | 74 | `hi` | Grammar ∅ → `emph` | B-P3 |
| 08-11 | 77 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 08-12 | 78 | `ubho` | Gr `masc.nom.sg` → `masc.nom.pl` — *`ubho` plural* | B-N33 |
| 08-13 | 80 |  | `ripening , resulting` → `ripening, resulting` | A6 |
| 08-14 | 98 | `have` | Grammar ∅ → `emph` | B-P3 |
| 08-15 | 102 | `suciṇṇo` | POS `pp as adj` — unify to one form (see policy D4) | A8-D4 |

## 09 — Going to True and False Refuges

`per-09-going-to-true-and-false-refuges.md` — 12 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 09-01 | 14 | `ve` | Grammar ∅ → `emph` | B-P3 |
| 09-02 | 19 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 09-03 | 35 | `kho` | Grammar ∅ → `emph` | B-P3 |
| 09-04 | 43 | `āgamma` | POS `verb` → `ger`, Grammar `ger` → ∅ (reviewer; audit/corpus keep `verb` + `ger`) — policy 11.4 | B-11.4 |
| 09-05 | 47 |  | `not secure , this` → `not secure, this` | A6 |
| 09-06 | 56 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 09-07 | 62 | `cattāri` | POS `adj` → `card` | B-P8 |
| 09-08 | 78 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 09-09 | 80 | `ariyaṃ-` | `nom.acc.sg` → `masc.acc.sg` — garbled case tag (`ariyaṃ … maggaṃ`)  ✔ *Reviewer B proposes the same.* | A4 |
| 09-10 | 81 | `ca-` | Grammar ∅ → `conj` | B-P2 |
| 09-11 | 96 | `kho` | Grammar ∅ → `emph` | B-P3 |
| 09-12 | 104 | `āgamma` | POS `verb` → `ger`, Grammar `ger` → ∅ (reviewer; audit/corpus keep `verb` + `ger`) — policy 11.4 | B-11.4 |

## 10 — The Pāṭimokkha Exhortation

`per-10-the-patimokkha-exhortation.md` — 10 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 10-01 | 27 |  | Pāḷi chant text: `khantī paramaṃ tapo tītikkhā, …` / `tītikkhā` → `titikkhā` (chant line and headword row, both) — DPD spelling is `titikkhā`; only occurrence in the corpus  *(decision; data-preservation rule)* | B-Q3 |
| 10-02 | 34 | `tapo` | Gr `nt.nom.sg` → `masc.nom.sg` — *DPD: tapas masc.* | B-N34 |
| 10-03 | 35 | `tītikkhā` | Word `tītikkhā` → `titikkhā` — *pairs with chant-line decision Q3 (do together)* | B-N130 |
| 10-04 | 35 |  | Pāḷi chant text: `khantī paramaṃ tapo tītikkhā, …` / `tītikkhā` → `titikkhā` (chant line and headword row, both) — DPD spelling is `titikkhā`; only occurrence in the corpus  *(decision; data-preservation rule)* | B-Q3 |
| 10-05 | 41 | `hi` | Grammar ∅ → `emph` | B-P3 |
| 10-06 | 49 |  | `Patient and forgiveness` → `Patience and forgiveness`; `not onegone forth` → `not one gone forth` | A6 |
| 10-07 | 61 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 10-08 | 64 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 10-09 | 67 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 10-10 | 70 | `ca` | Grammar ∅ → `conj` | B-P2 |

## 11 — The Three Characteristics

`per-11-the-three-characteristics.md` — 17 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 11-01 | 16 | `iti` | Grammar ∅ → `adv` | B-P1 |
| 11-02 | 18 | `paññāya` | POS `verb` → `noun`; Gr `abs` → `fem.ins.sg`; Eng `knowing, understanding (or) noun f.ins.s with understanding` → `with understanding, with wisdom` — *gloss held two alternative readings; reviewer chose the noun reading* | B-N93 |
| 11-03 | 21 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 |
| 11-04 | 25 | `atha` | Gr `adv` → ∅ | B-N78 |
| 11-05 | 45 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 |
| 11-06 | 56 |  | Grammar `masc.nom.sg` → `masc.nom.s` — **recommended reject:** Notation-only, against the `.sg` canon. | **B-X4✗** |
| 11-07 | 58 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 |
| 11-08 | 78 | `eva-` | Grammar ∅ → `emph` | B-P3 |
| 11-09 | 90 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 11-10 | 91 | `kho` | Grammar ∅ → `emph` | B-P3 |
| 11-11 | 92 |  | `well preached , well-taught` → `well preached, well-taught` | A6 |
| 11-12 | 97 | `pāram-` | Grammar ∅ → `prep` | B-P5 |
| 11-13 | 112 | `vippahāya` | POS `verb` → `ger`, Grammar `ger` → ∅ (reviewer; audit/corpus keep `verb` + `ger`) — policy 11.4 | B-11.4 |
| 11-14 | 118 | `āgamma` | POS `verb` → `ger`, Grammar `ger` → ∅ (reviewer; audit/corpus keep `verb` + `ger`) — policy 11.4 | B-11.4 |
| 11-15 | 120 | `yattha` | Grammar ∅ → `adv` | B-P1 |
| 11-16 | 130 | `tatra-` | Grammar ∅ → `adv` | B-P1 |
| 11-17 | 133 | `hitvā` | POS `verb` → `abs`, Grammar `abs` → ∅ (reviewer; audit/corpus keep `verb` + `abs`) — policy 11.4 | B-11.4 |

## 12 — The Burdens

`per-12-the-burdens.md` — 6 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 12-01 | 14 | `have` | Grammar ∅ → `emph` | B-P3 |
| 12-02 | 17 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 12-03 | 33 | `nikkhipitvā` | POS `verb` → `abs`, Grammar `abs` → ∅ (reviewer; audit/corpus keep `verb` + `abs`) — policy 11.4 | B-11.4 |
| 12-04 | 38 | `anādiya` | POS `verb` → `ger`, Grammar `ger` → ∅ (reviewer; audit/corpus keep `verb` + `ger`) — policy 11.4 | B-11.4 |
| 12-05 | 41 | `abbuyha` | POS `verb` → `ger`, Grammar `ger` → ∅ (reviewer; audit/corpus keep `verb` + `ger`) — policy 11.4 | B-11.4 |
| 12-06 | 43 | `parinibbuto` | POS `adj` → `pp` | B-N94 |

## 13 — From the Elder Raṭṭhapāla

`per-13-from-the-elder-ratthapala.md` — 45 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 13-01 | 13 |  | `passa`: `imp.2.sg` → `imper.2.s` — **recommended reject:** Regression: corpus uses `imp`, not `imper`. | **B-X3✗** |
| 13-02 | 14 |  | **D3** `<br>` inside table cells (lines 14). Policy: keep (note the exception) or convert `A<br>(or)<br>B` → `A (or) B`. | A8-D3 |
| 13-03 | 14 | `cittakataṃ` | Gr `masc.acc.sg` → `nt.acc.sg` — *agrees with nt `bimbaṃ`/`rūpaṃ`* | B-N35 |
| 13-04 | 22 | `dhuvaṃ` | Grammar ∅ → `adv` | B-P1 |
| 13-05 | 25 |  | `diseased, . There` → `diseased. There` | A6 |
| 13-06 | 32 |  | `passa`: `imp.2.sg` → `imper.2.s` — **recommended reject:** Regression: corpus uses `imp`, not `imper`. | **B-X3✗** |
| 13-07 | 33 | `cittakataṃ` | Gr `masc.acc.sg` → `nt.acc.sg` — *same* | B-N36 |
| 13-08 | 37 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 13-09 | 38 | `aṭṭhiṃ` | Gr `nt.nom.sg` → `nt.acc.sg` — *acc., not nom.* | B-N37 |
| 13-10 | 40 | `onaddhaṃ` | Gr `nt.nom.sg` → `nt.acc.sg` — *acc., not nom.* | B-N38 |
| 13-11 | 41 | `saha` | Grammar ∅ → `prep` | B-P5 |
| 13-12 | 42 | `vatthehi` | `nt.ins.sg` → `nt.ins.pl` — `-ehi` is plural | A4 |
| 13-13 | 52 | `alattaka-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 13-14 | 58 | `alaṃ` | Grammar ∅ → `emph` | B-P3 |
| 13-15 | 62 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 13-16 | 65 |  | `fora seeker` → `for a seeker` | A6 |
| 13-17 | 72 | `aṭṭha-` | POS `adj` → `card` | B-P8 |
| 13-18 | 80 |  | `fora seeker ofthe` → `for a seeker of the` | A6 |
| 13-19 | 106 | `laddhāna` | POS `verb` → `abs`, Grammar `abs` → ∅ (reviewer; audit/corpus keep `verb` + `abs`) — policy 11.4 | B-11.4 |
| 13-20 | 107 | `vittaṃ` | Gr `masc.acc.sg` → `nt.acc.sg` | B-N39 |
| 13-21 | 109 | `mohā` | Gr `nt.abl.sg` → `masc.abl.sg` — *`moha` masc.* | B-N40 |
| 13-22 | 128 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 13-23 | 130 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 13-24 | 133 |  | `desire , not free` → `desire, not free` | A6 |
| 13-25 | 137 | `hutvāna` | POS `verb` → `abs`, Grammar `abs` → ∅ (reviewer; audit/corpus keep `verb` + `abs`) — policy 11.4 | B-11.4 |
| 13-26 | 158 | `labhate` | Grammar `pr.refl.3.sg` → `pr.3.sg` (reviewer drops `refl`; audit 5.3 keeps it: `imp.refl.1.pl`) — policy 11.2 | B-11.2 |
| 13-27 | 161 | `cāpi` | POS `ind` → `sandhi` (leave Grammar empty) | B-P7 |
| 13-28 | 164 | `vihanti` | Gr `pr.3.sg` → `pr.3.pl` | B-N79 |
| 13-29 | 183 | `hi` | Grammar ∅ → `emph` | B-P3 |
| 13-30 | 184 | `paññā-` | Grammar `fem.nom.sg` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 13-31 | 185 | `eva` | Grammar ∅ → `emph` | B-P3 |
| 13-32 | 190 | `idha-` | Grammar ∅ → `adv` | B-P1 |
| 13-33 | 193 | `hi` | Grammar ∅ → `emph` | B-P3 |
| 13-34 | 210 | `hi` | Grammar ∅ → `emph` | B-P3 |
| 13-35 | 219 | `disvā` | POS `verb` → `abs`, Grammar `abs` → ∅ (reviewer; audit/corpus keep `verb` + `abs`) — policy 11.4 | B-11.4 |
| 13-36 | 222 | `pabbajito-` | POS `pp/noun` — unify to one form (see policy D4) | A8-D4 |
| 13-37 | 222 | `pabbajito-` | POS `pp/noun` → `pp` — *drops `/noun`* | B-N95 |
| 13-38 | 241 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 13-39 | 243 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 13-40 | 247 | `disvā` | POS `verb` → `abs`, Grammar `abs` → ∅ (reviewer; audit/corpus keep `verb` + `abs`) — policy 11.4 | B-11.4 |
| 13-41 | 248 | `pabbajito-` | POS `pp/noun` — unify to one form (see policy D4) | A8-D4 |
| 13-42 | 248 | `pabbajito-` | POS `pp/noun` → `pp` — *same* | B-N96 |
| 13-43 | 251 | `apaṇṇakaṃ` | POS `ind` → `adj`; Gr ∅ → `nt.acc.sg` — *gloss `surely; certainly` unchanged (reviewer: DPD adj, used adverbially as acc.sg)* | B-N97 |
| 13-44 | 253 | `eva` | Grammar ∅ → `emph` | B-P3 |
| 13-45 | 254 | `seyyo` | POS `ind` → `adj`; Gr ∅ → `masc.nom.sg` — *DPD: seyya adj, compar* | B-N98 |

## 14 — From the Elder Pārāpariya

`per-14-from-the-elder-parapariya.md` — 27 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 14-01 | 36 | `sītavātaparittāṇaṃ` | Rebuild row as `\| sītavātaparittāṇaṃ \| noun \| nt.nom.sg \| protection from cold and wind \|` — *Tag sits in POS column (audit Part 5.6 `nt.n.s` fix would leave it in the wrong column — this amends it)* | B-N2 |
| 14-02 | 40 | `hirikopīnachādanaṃ` | Rebuild row as `\| hirikopīnachādanaṃ \| noun \| nt.nom.sg \| covering that which arouses shyness \|` — *same as 14:36* | B-N3 |
| 14-03 | 44 |  | `(their robs)` → `(their robes)` | A6 |
| 14-04 | 62 | `paṇītaṃ` | Gr `nt.nom.sg` → `nt.acc.sg` — *object, acc.* | B-N41 |
| 14-05 | 65 | `lūkhaṃ` | Gr `nt.nom.sg` → `nt.acc.sg` — *object, acc.* | B-N42 |
| 14-06 | 66 | `appaṃ` | Gr `nt.nom.sg` → `nt.acc.sg` — *object, acc.* | B-N43 |
| 14-07 | 70 | `bahuṃ` | Gr `nt.nom.sg` → `nt.acc.sg` — *object, acc.* | B-N44 |
| 14-08 | 83 | `\>na-` | POS `neg` → `ind`; Grammar `` → `neg` | A5.10 |
| 14-09 | 94 | `parikkhāre` | Gr `masc.acc.pl` → `masc.loc.sg` — *locative* | B-N45 |
| 14-10 | 95 | `bhesajje` | Gr `nt.acc.pl` → `nt.loc.sg` — *locative* | B-N46 |
| 14-11 | 97 | `paccaye` | Gr `nt.acc.pl` → `masc.loc.sg` — *locative* | B-N47 |
| 14-12 | 103 | `na` | ⚔ **C13 — keep ONE:** **Option A (audit)** Part 5.10: POS `neg` → `ind`, Grammar `neg` (audit lists per-14:83,103,148)  ·  **Option B (reviewer)** POS `neg` → `ind`, Grammar ∅  ·  *Corpus has 16 existing `ind` / `neg` rows; see X2. Reviewer changed only :103 of the three.* | B-C13 |
| 14-13 | 107 | `yathā` | Grammar ∅ → `adv` | B-P1 |
| 14-14 | 109 | `āsavakkhaye` | POS `adj` → `noun`; Gr `masc.acc.pl` → `masc.loc.sg` | B-N99 |
| 14-15 | 120 | `kandarāsu` | Gr `masc.loc.pl` → `fem.loc.pl` — *`kandarā` fem.* | B-N48 |
| 14-16 | 122 | `ca` | POS `conj` → `ind`; Grammar `` → `conj`  ✔ *Reviewer B proposes the same.* | A5.10 |
| 14-17 | 124 |  | `at the foots of trees` → `at the feet of trees` | A6 |
| 14-18 | 147 | `atthaddhamānasā` | Gr ∅ → `masc.nom.pl` — *grammar was empty* | B-N49 |
| 14-19 | 148 | `\>na-` | POS `neg` → `ind`; Grammar `` → `neg` | A5.10 |
| 14-20 | 182 | `teladhārāva` | Rebuild row as `\| teladhārāva \| noun \| fem.nom.sg \| as stream of oil \|` — *POS empty* | B-N4 |
| 14-21 | 196 | `yathā` | Grammar ∅ → `adv` | B-P1 |
| 14-22 | 207 | `upaṭṭhapetvāna,` | POS `verb` → `abs`, Grammar `abs` → ∅ (reviewer; audit/corpus keep `verb` + `abs`) — policy 11.4 | B-11.4 |
| 14-23 | 208 | `evaṃ` | Grammar ∅ → `adv` | B-P1 |
| 14-24 | 220 | `saritvā` | POS `verb` → `abs`, Grammar `abs` → ∅ (reviewer; audit/corpus keep `verb` + `abs`) — policy 11.4 | B-11.4 |
| 14-25 | 224 | `vattam-` | Gr ∅ → `nt.acc.sg` | B-N50 |
| 14-26 | 231 | `kiñcāpi` | POS `ind` → `sandhi` (leave Grammar empty) | B-P7 |
| 14-27 | 232 | `pacchimo` | `masc.nom.pl` → `masc.nom.sg` — `-o` is singular | A4 |

## 15 — On Protection

`per-15-on-protection.md` — 15 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 15-01 | 11 | `handa` | ⚔ **C2 — keep ONE:** **Option A (audit)** Part 5.4: Grammar `emp` → `emph`  ·  **Option B (reviewer)** Grammar `emp` → `excl`  ·  *DPD: `handa` = ind, excl. Choosing B is consistent with P4 (all `handa` rows → `excl`).* | B-C2 |
| 15-02 | 14 | `gāthāyo` | Grammar `fem nom pl` → `fem.nom.pl` | A5.12 |
| 15-03 | 14 | `gāthāyo` | Gr `fem nom pl` → `fem.acc.pl` | B-N51 |
| 15-04 | 15 | `bhaṇāmase` | `imp.reflx.3.pl` → `imp.refl.1.pl` — "let us chant" = 1st person (cf. per-06:19 tagged 1.pl) | A4 |
| 15-05 | 15 | `bhaṇāmase` | Grammar `imp.reflx.3.pl` → `imp.1.pl` (reviewer drops `refl`; audit 5.3 keeps it: `imp.refl.1.pl`) — policy 11.2 | B-11.2 |
| 15-06 | 27 | `parakkamma` | POS `verb` → `ger`, Grammar `ger` → ∅ (reviewer; audit/corpus keep `verb` + `ger`) — policy 11.4 | B-11.4 |
| 15-07 | 31 | `nappahāya` | POS `verb` → `ger`, Grammar `ger` → ∅ (reviewer; audit/corpus keep `verb` + `ger`) — policy 11.4 | B-11.4 |
| 15-08 | 33 | `kāme` | Gr `masc.loc.sg` → `masc.acc.pl` — *acc. pl.* | B-N52 |
| 15-09 | 53 | `hi` | Grammar ∅ → `emph` | B-P3 |
| 15-10 | 55 | `bhiyyo` | Grammar ∅ → `adv` | B-P1 |
| 15-11 | 68 | `seyyo` | POS `ind` → `adj`; Gr ∅ → `masc.nom.sg` — *same* | B-N100 |
| 15-12 | 74 | `seyyo` | POS `ind` → `adj`; Gr ∅ → `masc.nom.sg` — *same* | B-N101 |
| 15-13 | 76 | `katvā` | POS `verb` → `abs`, Grammar `abs` → ∅ (reviewer; audit/corpus keep `verb` + `abs`) — policy 11.4 | B-11.4 |
| 15-14 | 87 | `yathā` | Grammar ∅ → `adv` | B-P1 |
| 15-15 | 90 | `eva-` | Grammar ∅ → `emph` | B-P3 |

## 16 — Miscellaneous Verses

`per-16-miscellaneous-verses.md` — 28 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 16-01 | 29 | `appassuta-` | Gr ∅ → `masc.nom.sg` — *grammar was empty* | B-N53 |
| 16-02 | 51 | `satīmanto` | POS `adj as noun` — unify to one form (see policy D4) | A8-D4 |
| 16-03 | 51 | `satīmanto` | POS `adj as noun` → `noun`; Gr `masc.nom.sg` → `masc.nom.pl` | B-N102 |
| 16-04 | 72 | `pubbe` | ⚔ **C10 — keep ONE:** **Option A (audit)** Part 3: `pubbe / ind / (empty) / before, previously, … in a previous life`  ·  **Option B (reviewer)** Same row but Grammar `adv`  ·  *Audit leaves Grammar empty; reviewer (and audit 5.11 for per-18:248) use `adv` for `pubbe`.* | B-C10 |
| 16-05 | 75 | `pacchā` | Grammar ∅ → `adv` | B-P1 |
| 16-06 | 77 | `m'āhu` | POS `v+ind` → `verb`; Gr `aor.3.sg` → `aor.3.pl` — *POS `v+ind` is a D4 composite value* | B-N103 |
| 16-07 | 79 | `majjhe` | ⚔ **C8 — keep ONE:** **Option A (audit)** Part 5.11: Grammar `from loc. sg.` → `adv`  ·  **Option B (reviewer)** POS `ind` → `noun`, Grammar `from loc. sg.` → `nt.loc.sg` (gloss unchanged: `in the present, lit. in the middle`)  ·  *DPD `majjhe` is a locative of `majjha`; ‘adv’ vs real locative.* | B-C8 |
| 16-08 | 118 | `santiyā;` | POS `verb` → `noun` | B-N104 |
| 16-09 | 121 | `pamatte` | POS `pp as adj` — unify to one form (see policy D4) | A8-D4 |
| 16-10 | 121 | `pamatte` | POS `pp as adj` → `pp` — *D4: `pp as adj` → `pp`* | B-N105 |
| 16-11 | 122 | `viññāya` | POS `verb` → `ger`, Grammar `ger` → ∅ (reviewer; audit/corpus keep `verb` + `ger`) — policy 11.4 | B-11.4 |
| 16-12 | 139 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 16-13 | 149 | `upaccagā` | `imp.3.sg` → `aor.3.sg` — aorist "it passed by" | A4 |
| 16-14 | 150 |  | Rebuild row: `\| khaṇ'ātītā \| adj \| masc.nom.pl \| who has missed the chance, who lost the opportunity, lit. moment passed by \|`  ✔ *Reviewer B proposes the same.* | A3 |
| 16-15 | 151 | `hi` | Grammar ∅ → `emph` | B-P3 |
| 16-16 | 205 | `eva` | Grammar `emph.` → `emph`  ✔ *Reviewer B proposes the same.* | A5.4 |
| 16-17 | 221 | `tumhehi` | `masc.ins.pl` → `2.ins.pl` — personal pronoun | A4 |
| 16-18 | 232 | `yaṃ` | Gr `masc.acc.sg` → `nt.nom.sg` — *neuter, subject* | B-N54 |
| 16-19 | 234 | `karaṇīyaṃ` | Gr `masc.acc.sg` → `nt.nom.sg` — *neuter, subject* | B-N55 |
| 16-20 | 239 | `upādāya` | ⚔ **C9 — keep ONE:** **Option A (audit)** Part 5.11: Grammar `from ger` → `ger`  ·  **Option B (reviewer)** Grammar `from ger` → `adv`  ·  *Reviewer: DPD upādāya 2/3 = ind, adv, used as postposition.* | B-C9 |
| 16-21 | 240 | `kataṃ` | Gr `masc.acc.sg` → `nt.nom.sg` — *neuter, subject* | B-N56 |
| 16-22 | 242 | `taṃ` | Gr `masc.acc.sg` → `nt.nom.sg` — *neuter, subject* | B-N57 |
| 16-23 | 256 | `mā pamād'attha` | POS `ind+m+imp` — unify to one form (see policy D4) | A8-D4 |
| 16-24 | 256 |  | multi-word POS tag (`v + pn` / `ind+pn` / `ind+m+imp` / `adv+ind`): use `idiom` or `sandhi` per corpus convention (policy D4) | A8-D4 |
| 16-25 | 258 | `pacchā` | Grammar ∅ → `adv` | B-P1 |
| 16-26 | 261 | `ayaṃ` | `POS noun` → `POS pron` — demonstrative pronoun (Grammar fem.nom.sg is correct)  ✔ *Reviewer B proposes the same.* | A4 |
| 16-27 | 266 |  | `There are these foots of a tree` → `There are these roots of trees` (check the table rows above for the same wording) | A6 |
| 16-28 | 266 |  | **D6** if a table row above glosses `rukkha-mūlāni` as "foots of a tree", align with the corrected translation ("roots of trees"). | A8-D6 |

## 17 — A single Excellent Night

`per-17-a-single-excellent-night.md` — 21 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 17-01 | 12 | `atītaṃ` | POS `adj (as noun)` — unify to one form (see policy D4) | A8-D4 |
| 17-02 | 12 | `atītaṃ` | POS `adj (as noun)` → `adj` — *D4: unify `adj (as noun)` → `adj`* | B-N106 |
| 17-03 | 21 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 17-04 | 31 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 17-05 | 34 |  | Rebuild row: `\| tattha tattha \| ind \| adv \| right there, here and now, in each and every case, lit. there and there \|`  ✔ *Reviewer B proposes the same row; his gloss order differs.* | A3 |
| 17-06 | 44 | `asaṃhiraṃ` | POS `adj (or as noun)` — unify to one form (see policy D4) | A8-D4 |
| 17-07 | 44 | `asaṃhiraṃ` | POS `adj (or as noun)` → `adj` — *same* | B-N107 |
| 17-08 | 45 | `asaṅkuppaṃ` | POS `adj (or as noun)` — unify to one form (see policy D4) | A8-D4 |
| 17-09 | 45 | `asaṅkuppaṃ` | POS `adj (or as noun)` → `adj` — *same* | B-N108 |
| 17-10 | 47 | `vidvā` | Rebuild row as `\| vidvā \| adj \| masc.nom.sg \| wise \|` — *POS cell held `masc`* | B-N5 |
| 17-11 | 57 | `ajja-` | Grammar ∅ → `adv` | B-P1 |
| 17-12 | 64 | `suve` | Grammar ∅ → `adv` | B-P1 |
| 17-13 | 68 | `saṅgaran-` | Grammar `nt.nom.sg.` → `nt.nom.sg`  ✔ *Reviewer B proposes the same.* | A5.7 |
| 17-14 | 80 | `evaṃ` | Grammar ∅ → `adv` | B-P1 |
| 17-15 | 81 | `vihārim-` | POS `adj (as noun)` — unify to one form (see policy D4) | A8-D4 |
| 17-16 | 81 | `vihārim-` | POS `adj (as noun)` → `adj` — *same* | B-N109 |
| 17-17 | 83 | `ahorattam-` | Grammar `nt.acc.sg.` → `nt.acc.sg` | A5.7 |
| 17-18 | 83 | `ahorattam-` | ⚔ **same cell as A5.7 row above — keep ONE:** **Option A (A5.7)** Grammar `nt.acc.sg.` → `nt.acc.sg`  ·  **Option B (B-P1)** Grammar `nt.acc.sg.` → `adv` (reviewer wrote `adv`; current cell is `nt.acc.sg.`, not empty) | B-P1 |
| 17-19 | 86 | `ve` | Grammar ∅ → `emph` | B-P3 |
| 17-20 | 90 | `ti –` | Grammar ∅ → `adv` | B-P1 |
| 17-21 | 92 | `ācikkhate` | Grammar `reflex.opt.3.sg` → `opt.refl.3.sg` | A5.3 |

## 18 — Setting in Motion The Wheel of Dhamma

`per-18-setting-in-motion-the-wheel-of-dhamma.md` — 29 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 18-01 | 15 | `pabbajitena` | Rebuild row as `\| pabbajitena \| noun \| masc.ins.sg \| by monk, one who has gone forth \|` — *POS cell held `masc`* | B-N6 |
| 18-02 | 28 | `kāmasukhallikā-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 18-03 | 56 | `kho` | Grammar ∅ → `emph` | B-P3 |
| 18-04 | 90 | `eva` | Grammar ∅ → `emph` | B-P3 |
| 18-05 | 122 | `jāti` | Rebuild row as `\| jāti \| noun \| fem.nom.sg \| birth, rebirth, conception \|` — *columns shifted; `f.n.s` embedded in gloss; audit Part 2 missed this row* | B-N7 |
| 18-06 | 136 |  | Rebuild row: `\| dukkha- \| noun \| \| discomfort, suffering, pain, unease, something unsatisfactory, problem, trouble \|`  ✔ *Reviewer B proposes the same.* | A3 |
| 18-07 | 158 | `piyehi` | POS `adj (as noun)` — unify to one form (see policy D4) | A8-D4 |
| 18-08 | 158 | `piyehi` | POS `adj (as noun)` → `adj` — *same* | B-N110 |
| 18-09 | 168 | `yam-(p)-icchaṃ` | Grammar `m.acc.sg` → `masc.acc.sg` | A5.6 |
| 18-10 | 171 | `na` | reviewer: Grammar `neg` → ∅ — **⚑ user decision, not implemented unless you remove the ⚑** (for the word `na` the corpus has 33 rows with empty Grammar vs 7 `neg`) | **B-X2⚑** |
| 18-11 | 245 | `dukkhaṃ` | ⚔ **C4 — keep ONE:** **Option A (audit)** Part 2: rebuilt row `noun` / `nt.nom.sg` (subject of `idaṃ dukkhaṃ ariyasaccaṃ`)  ·  **Option B (reviewer)** Rebuilt row `noun` / `nt.acc.sg` (reviewer just fixed the `nt.ac.s` typo)  ·  *Row is column-shifted: both options rebuild the same row, only the case differs. Reviewer's meaning/POS fix is identical to A.* | B-C4 |
| 18-12 | 247 |  | Rebuild row: `\| me \| pron \| 1.dat.sg \| to me, for me \|`  ✔ *Reviewer B proposes the same.* | A2 |
| 18-13 | 248 | `pubbe` | Grammar `from loc.sg` → `adv`  ✔ *Reviewer B proposes the same.* | A5.11 |
| 18-14 | 262 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 |
| 18-15 | 269 | `kho` | Grammar ∅ → `emph` | B-P3 |
| 18-16 | 283 | `kho` | Grammar ∅ → `emph` | B-P3 |
| 18-17 | 286 | `dukkhaṃ` | Grammar `nt.acc.sg.` → `nt.acc.sg` | A5.7 |
| 18-18 | 294 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 |
| 18-19 | 314 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 |
| 18-20 | 331 |  | Pāḷi (L325) is `dukkha-nirodho … sacchikatan-ti`, but translation says "this noble truth of the **origin** of suffering has been personally experienced." → "this noble truth of the **cessation** of suffering has been personally experienced." | A7 |
| 18-21 | 335 |  | `the noble truth of the the way` → `the noble truth of the way` (doubled word, same section). | A7 |
| 18-22 | 335 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 |
| 18-23 | 343 |  | Pāḷi (L337) is `dukkha-nirodha-gāminī-paṭipadā … bhāvetabban-ti`, translation says "this noble truth of the **cessation of suffering** should be developed." → "this noble truth of the **way leading to the cessation of suffering** should be developed." | A7 |
| 18-24 | 351 |  | Pāḷi (L345) is `dukkha-nirodha-gāminī-paṭipadā … bhāvitan-ti`, translation says "this noble truth of the **origin of suffering** has been developed." → "this noble truth of the **way leading to the cessation of suffering** has been developed." | A7 |
| 18-25 | 364 | `dvādasa-` | POS `adj (num)` — unify to one form (see policy D4) | A8-D4 |
| 18-26 | 364 | `dvādasa-` | POS `adj` → `card` | B-P8 |
| 18-27 | 387 | `sadevamanussāya` | `masc.loc.sg` → `fem.loc.sg` — agrees with fem. `pajāya` | A4 |
| 18-28 | 391 | `paccaññāsiṃ` | POS `verbaor.1.s` → `verb`; Grammar `` → `aor.1.sg`  ✔ *Reviewer B proposes the same.* | A5.8 |
| 18-29 | 400 | `ca` | Grammar ∅ → `conj` | B-P2 |

## 19 — Anupubba-Sikkhā

`per-19-anupubba-sikkha.md` — 39 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 19-01 | 25 |  | `ouseholder or householder's son` → `Householder or householder's son` | A6 |
| 19-02 | 46 | `iti` | Grammar ∅ → `adv` | B-P1 |
| 19-03 | 57 |  | `dirty , lit:` → `dirty, lit:` | A6 |
| 19-04 | 57 | `rajo-patho` | Rebuild row as `\| rajo-patho \| noun \| masc.nom.sg \| dusty, dirty , lit: condition of dust, state of dirt \|` — *POS cell empty (audit only fixes the typo in this row's gloss)* | B-N8 |
| 19-05 | 95 |  | POS `idioṃ` → `idiom` | A1 |
| 19-06 | 188 | `samādāya` | Gr `abs` → `ger` | B-N80 |
| 19-07 | 189 | `sikkhassu` | Grammar `imp.ref.2.sg` → `imp.refl.2.sg` | A5.3 |
| 19-08 | 190 |  | **D8** stray `”` inside the Pāḷi word `sikkhāpadesū'”ti` — remove `”` | A8-D8 |
| 19-09 | 271 |  | `false speech , lit.` → `false speech, lit.` | A6 |
| 19-10 | 316 | `iti` | Grammar ∅ → `adv` | B-P1 |
| 19-11 | 331 |  | `he is reconciler those who are divided` → `he is a reconciler of those who are divided` | A6 |
| 19-12 | 378 |  | Rebuild row: `\| kālena \| ind \| adv \| timely, at the right moment, at a suitable time, at the proper time \|` | A3 |
| 19-13 | 421 |  | Rebuild row: `\| vilepana- \| noun \| \| oil, unguent, ointment, cosmetics, make-up, perfume \|` | A3 |
| 19-14 | 560 |  | Rebuild row: `\| ukkoṭana- \| noun \| \| taking bribes, bribery, corruption, crooked dealing \|` | A3 |
| 19-15 | 588 |  | Rebuild row: `\| cīvarena \| noun \| nt.ins.sg \| with robe \|` (embedded tag said `m.ins.s`; cīvara is neuter) | A2 |
| 19-16 | 592 |  | **Do NOT change** `lit. wherever wherever` (also lines 607, 634) — intentional literal rendering of reduplicated `yena yeneva`. | A6-note |
| 19-17 | 618 |  | Rebuild row: `\| evameva kho \| ind \| \| in the same way \|` (currently `\| evameva \| kho \| ind \| in the same way \|` — the particle `kho` slid into the POS cell; it belongs to the Pāḷi lemma) | A2 |
| 19-18 | 618 |  | Gloss `in the same way` → `ind` — **recommended reject:** Reviewer wiped the gloss (row was already column-shifted); use audit Part 2 rebuild instead. | **B-X5✗** |
| 19-19 | 623 |  | Rebuild row: `\| cīvarena \| noun \| nt.ins.sg \| with robe \|` (same) | A2 |
| 19-20 | 774 |  | multi-word POS tag (`v + pn` / `ind+pn` / `ind+m+imp` / `adv+ind`): use `idiom` or `sandhi` per corpus convention (policy D4) | A8-D4 |
| 19-21 | 783 |  | `you should take a food` → `you should take food` | A6 |
| 19-22 | 803 | `iti` | Grammar ∅ → `adv` | B-P1 |
| 19-23 | 809 | `na-uppādessāmi` | POS `v.caus` → `verb`; Grammar `fut.1.sg` → `fut.1.sg.caus` | A5.9 |
| 19-24 | 811 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 19-25 | 817 |  | `assistance of holy live` → `assistance of the holy life`; `put an end of former` → `put an end to former`; `a new (painful) sensations` / `a new (painfull) sensations` → `new (painful) sensations`; per-31:71 also `(painfull)` → `(painful)` (2×) *(same fix at: per-19:817, per-31:71)* | A6 |
| 19-26 | 830 | `viharāhi` | `imp.sg.sg` → `imp.2.sg` — typo `sg.sg` | A4 |
| 19-27 | 876 |  | Rebuild row: `\| pādaṃ \| noun \| masc.acc.sg \| foot \|` | A2 |
| 19-28 | 994 | `upaṭṭhapetvā` | POS `v.caus` → `verb`; Grammar `abs` → `abs.caus` | A5.9 |
| 19-29 | 996 |  | `Afternoon, he returned` → `In the afternoon, he returned` | A6 |
| 19-30 | 1057 | `kusalesu` | `masc.loc.sg` → `masc.loc.pl` — `-esu` is plural | A4 |
| 19-31 | 1058 | `dhammesu` | `masc.loc.sg` → `masc.loc.pl` — `-esu` is plural | A4 |
| 19-32 | 1123 |  | gloss `these, theṃ` → `these, them` | A1 |
| 19-33 | 1142 |  | `he reaching and dwells` → `he reaches and dwells` | A6 |
| 19-34 | 1168 |  | Rebuild row: `\| khaya- \| noun \| \| exhaustion (of), extinction (of), depletion (of), annihilation (of), destruction (of) \|` | A3 |
| 19-35 | 1191 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 |
| 19-36 | 1203 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 |
| 19-37 | 1232 | `iti` | Grammar ∅ → `adv` | B-P1 |
| 19-38 | 1245 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 |
| 19-39 | 1255 | `kho` | Grammar ∅ → `emph` | B-P3 |

## 20 — Requisites for Awakening

`per-20-requisites-for-awakening.md` — 3 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 20-01 | 20 | `sādhukaṃ` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 20-02 | 42 | `lokānukampāya` | Grammar `fem.instr.sg` → `fem.ins.sg` | A5.2 |
| 20-03 | 58 | `seyyathīdaṃ` | POS `ind` → `sandhi` (leave Grammar empty; reviewer also wrote `sandhi` in Grammar — not recommended) | B-P7 |

## 21 — The Seven Factors of Awakening

`per-21-the-seven-factors-of-awakening.md` — 19 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 21-01 | 22 | `sammā` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 21-02 | 39 | `vimuttiñāṇadassana-` | Grammar `nt` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 21-03 | 42 | `api` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 21-04 | 56 | `api` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 21-05 | 59 | `api` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 21-06 | 62 | `api` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 21-07 | 65 | `api` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 21-08 | 68 | `api` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 21-09 | 94 | `ca` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 21-10 | 96 | `ca` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 21-11 | 105 | `tathā` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 21-12 | 120 | `tathā` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 21-13 | 128 | `parivīmaṃsaṃ-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 21-14 | 143 | `parivīmaṃsaṃ-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 21-15 | 150 |  | `there is effort arises without sluggishness` → `effort arises without sluggishness` | A6 |
| 21-16 | 169 | `api` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 21-17 | 172 | `api` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 21-18 | 186 |  | `with relaxed body and who at ease` → `with relaxed body and at ease` | A6 |
| 21-19 | 196 |  | Row rewritten to `ind \| ind <spaces> well, thoroughly, fully \|` — **recommended reject:** Garbled cells; keep the current row (`ind \| \| well, thoroughly, fully`). | **B-X6✗** |

## 22 — The Noble Eightfold Path

`per-22-the-noble-eightfold-path.md` — 36 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 22-01 | 13 | `eva` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 22-02 | 17 | `seyyathīdaṃ` | POS `ind` → `sandhi` (leave Grammar empty; reviewer also wrote `sandhi` in Grammar — not recommended) | B-P7 |
| 22-03 | 40 | `kho` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 22-04 | 47 |  | Rebuild row: `\| dukkhanirodha- \| noun \| \| cessation of suffering, disappearance of suffering \|` | A3 |
| 22-05 | 67 |  | Rebuild row: `\| abyāpāda- \| noun \| \| goodwill, kindness, friendliness, benevolence, lit. not ill-will \|` | A3 |
| 22-06 | 117 | `idha` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 22-07 | 119 | `micchā-` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 22-08 | 136 | `idha` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 22-09 | 152 |  | `he exerts oneself` → `he exerts himself` *(same fix at: per-22:152, per-22:165, per-22:176, per-22:193)* | A6 |
| 22-10 | 165 |  | `he exerts oneself` → `he exerts himself` *(same fix at: per-22:152, per-22:165, per-22:176, per-22:193)* | A6 |
| 22-11 | 176 |  | `he exerts oneself` → `he exerts himself` *(same fix at: per-22:152, per-22:165, per-22:176, per-22:193)* | A6 |
| 22-12 | 176 |  | third right-effort clause: translation says "generates intention for the **arising** of unarisen **worthless, unskilful** states of mind". The Pāḷi for this clause is `anuppannānaṃ kusalānaṃ dhammānaṃ uppādāya` (check table above the line) → "…arising of unarisen **wholesome, skillful** states of mind." | A7 |
| 22-13 | 190 | `bhāvanāya` | Grammar `fem.instr.sg` → `fem.ins.sg` | A5.2 |
| 22-14 | 193 |  | `he exerts oneself` → `he exerts himself` *(same fix at: per-22:152, per-22:165, per-22:176, per-22:193)* | A6 |
| 22-15 | 213 |  | `strenuous , with` → `strenuous, with` | A6 |
| 22-16 | 218 | `abhijjhā-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 22-17 | 230 |  | `a monk stay with` → `a monk stays with` | A6 |
| 22-18 | 236 | `citte` | `masc.loc.pl` → `nt.loc.sg` — citta is neuter; loc. singular | A4 |
| 22-19 | 252 |  | `this moks is called` → `this monks is called` | A6 |
| 22-20 | 259 | `ca` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 22-21 | 270 | `idha` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 22-22 | 274 | `eva` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 22-23 | 295 |  | `he attaining and remains` → `he attains and remains` *(same fix at: per-22:295, per-22:316, per-22:347, per-22:371)* | A6 |
| 22-24 | 316 |  | `he attaining and remains` → `he attains and remains` *(same fix at: per-22:295, per-22:316, per-22:347, per-22:371)* | A6 |
| 22-25 | 323 | `ca` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 22-26 | 326 | `ca` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 22-27 | 329 | `ca` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 22-28 | 332 | `ca` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 22-29 | 336 |  | gloss `hiṃ` (row `\| taṃ \| pron \| masc.acc.sg \| hiṃ \|`) → `him` | A1 |
| 22-30 | 347 |  | `he attaining and remains` → `he attains and remains` *(same fix at: per-22:295, per-22:316, per-22:347, per-22:371)* | A6 |
| 22-31 | 354 | `ca` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 22-32 | 357 | `ca` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** |
| 22-33 | 359 |  | Rebuild row: `\| pubb'eva \| ind \| \| just in front of, just before, previous, as before, as earlier \|` | A3 |
| 22-34 | 363 |  | Rebuild row: `\| upekkhā- \| noun \| \| mental poise, mental balance, equanimity, composure \|` | A3 |
| 22-35 | 364 |  | Rebuild row: `\| sati- \| noun \| \| mindfulness, presence, recollection, awareness \|` | A3 |
| 22-36 | 371 |  | `he attaining and remains` → `he attains and remains` *(same fix at: per-22:295, per-22:316, per-22:347, per-22:371)* | A6 |

## 23 — Mindfulness of Breathing

`per-23-mindfulness-of-breathing.md` — 29 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 23-01 | 32 |  | `it is fills up` → `it fills up` | A6 |
| 23-02 | 44 | `paripūreti` | `pr.3.pl` → `pr.3.sg` — 3.sg form; also fix gloss "fill up" → "fills up" | A4 |
| 23-03 | 85 | `upaṭṭhapetvā` | POS `v.caus` → `verb`; Grammar `abs` → `abs.caus` | A5.9 |
| 23-04 | 87 |  | translation `in front of hiṃ` → `in front of him` | A1 |
| 23-05 | 107 | `assasāmī'ti` | `pr.3.sg` → `pr.1.sg` — "-āmi" = 1st sg ("I breathe in") | A4 |
| 23-06 | 110 |  | `I'm breath in deeply.` / `I'm breath out deeply.` / `…shortly.` → `I breathe in deeply.` / `I breathe out deeply.` / `…shortly.` *(same fix at: per-23:110, per-23:121, per-23:134, per-23:145)* | A6 |
| 23-07 | 118 | `passasāmī'ti` | `pr.3.sg` → `pr.1.sg` — same; also gloss "I breathes out" → "I breathe out" | A4 |
| 23-08 | 121 |  | `I'm breath in deeply.` / `I'm breath out deeply.` / `…shortly.` → `I breathe in deeply.` / `I breathe out deeply.` / `…shortly.` *(same fix at: per-23:110, per-23:121, per-23:134, per-23:145)* | A6 |
| 23-09 | 131 | `assasāmī'ti` | `pr.3.sg` → `pr.1.sg` — same | A4 |
| 23-10 | 134 |  | `I'm breath in deeply.` / `I'm breath out deeply.` / `…shortly.` → `I breathe in deeply.` / `I breathe out deeply.` / `…shortly.` *(same fix at: per-23:110, per-23:121, per-23:134, per-23:145)* | A6 |
| 23-11 | 142 | `passasāmī'ti` | `pr.3.sg` → `pr.1.sg` — same | A4 |
| 23-12 | 145 |  | `I'm breath in deeply.` / `I'm breath out deeply.` / `…shortly.` → `I breathe in deeply.` / `I breathe out deeply.` / `…shortly.` *(same fix at: per-23:110, per-23:121, per-23:134, per-23:145)* | A6 |
| 23-13 | 154 | `assasissāmī'ti` | `fut.3.sg` → `fut.1.sg` — "-ssāmi" = 1st sg | A4 |
| 23-14 | 157 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 |
| 23-15 | 164 | `passasissāmī'ti` | `fut.3.sg` → `fut.1.sg` — same | A4 |
| 23-16 | 167 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 |
| 23-17 | 173 | `passambhayaṃ` | POS `prp.caus` → `prp`; Grammar `masc.nom.sg` → `masc.nom.sg.caus` | A5.9 |
| 23-18 | 174 | `kāya-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 23-19 | 176 | `assasissāmī'ti` | `fut.3.sg` → `fut.1.sg` — same | A4 |
| 23-20 | 179 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 |
| 23-21 | 183 | `passambhayaṃ` | POS `prp.caus` → `prp`; Grammar `masc.nom.sg` → `masc.nom.sg.caus` | A5.9 |
| 23-22 | 184 | `kāya-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 23-23 | 186 | `passasissāmī'ti` | `fut.3.sg` → `fut.1.sg` — same | A4 |
| 23-24 | 189 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 |
| 23-25 | 195 | `pīti-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 23-26 | 213 |  | `breathe out experiences mental activity` → `breathe out experiencing mental activity` | A6 |
| 23-27 | 220 |  | gloss `causing to be calṃ` → `causing to be calm` | A1 |
| 23-28 | 229 | `citta-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 23-29 | 231 |  | `breathe in experiences the mind` and `breathe out experiences the mind` → `experiencing` (2×) | A6 |

## 24 — Dependent Origination

`per-24-dependent-origination.md` — 12 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 24-01 | 13 | `\>avijjā-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 24-02 | 14 | `\>paccayā` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 24-03 | 45 |  | Rebuild row: `\| dukkhadomanass- \| noun \| \| pain and stress, physical pain and mental suffering \|` | A3 |
| 24-04 | 49 |  | `becoming arise` → `becoming arises`; `birth arise` → `birth arises` *(same fix at: per-24:49, per-66:145)* | A6 |
| 24-05 | 84 |  | Rebuild row: `\| dukkhanirodha- \| noun \| \| cessation of suffering, disappearance of suffering \|` | A3 |
| 24-06 | 164 |  | `the sphere of the sphere of the formless` → `the sphere of the formless` | A6 |
| 24-07 | 383 |  | Rebuild row: `\| duvidhena \| ind \| adv \| in two ways; as of two kinds; in a twofold way \|` (also drop the stray `–` after the Pāḷi word) | A3 |
| 24-08 | 456 |  | `non-perseption` → `non-perception` | A6 |
| 24-09 | 579 |  | Rebuild row: `\| diṭṭhi- \| noun \| \| view, belief, opinion, concept, theory, attitude \|` (drop the duplicated "opinion") | A3 |
| 24-10 | 597 |  | `of one who endowed with` → `of one who is endowed with` *(same fix at: per-24:597, per-24:624)* | A6 |
| 24-11 | 624 |  | `of one who endowed with` → `of one who is endowed with` *(same fix at: per-24:597, per-24:624)* | A6 |
| 24-12 | 699 |  | `for affected by` → `for one affected by`; `for endowed all kinds` → `for one endowed with all kinds`; `for affected by all kinds` → `for one affected by all kinds` | A6 |

## 25 — The Dhamma in Brief

`per-25-the-dhamma-in-brief.md` — 4 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 25-01 | 30 |  | `Bhessed One` → `Blessed One` (3×) | A6 |
| 25-02 | 43 |  | `whatever , that which` → `whatever, that which` | A6 |
| 25-03 | 53 | `vihareyyaṃ-` | Grammar `opt.ref.1.sg` → `opt.refl.1.sg` | A5.3 |
| 25-04 | 66 | `gotamī` | Grammar `fem.v.sg` → `fem.voc.sg` | A5.6 |

## 26 — The Four Great References

`per-26-the-four-great-references.md` — 7 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 26-01 | 44 |  | `Here a monks could say` → `Here a monk could say` | A6 |
| 26-02 | 65 |  | `certan` → `certain` (3×); `heared` → `heard` (3×) *(same fix at: per-26:65, per-26:91, per-26:95)* | A6 |
| 26-03 | 83 |  | **D6** `tesaṃ` tagged masc.gen.sg, gloss "of that" — form is plural; check context: gloss may need "of those". | A8-D6 |
| 26-04 | 91 |  | `certan` → `certain` (3×); `heared` → `heard` (3×) *(same fix at: per-26:65, per-26:91, per-26:95)* | A6 |
| 26-05 | 95 |  | `certan` → `certain` (3×); `heared` → `heard` (3×) *(same fix at: per-26:65, per-26:91, per-26:95)* | A6 |
| 26-06 | 173 | `h'etaṃ` | POS `ind+pn` — unify to one form (see policy D4) | A8-D4 |
| 26-07 | 173 |  | multi-word POS tag (`v + pn` / `ind+pn` / `ind+m+imp` / `adv+ind`): use `idiom` or `sandhi` per corpus convention (policy D4) | A8-D4 |

## 27 — Principles of Cordiality

`per-27-principles-of-cordiality.md` — 12 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 27-01 | 12 |  | POS `idioṃ` → `idiom` | A1 |
| 27-02 | 12 |  | POS stays `idioṃ`, Grammar → `idiom, card + masc` — **recommended reject:** Descriptive text in Grammar; use audit Part 1 (`idioṃ` → `idiom`, Grammar ∅). | **B-X7✗** |
| 27-03 | 68 |  | `for a monks` → `for a monk` | A6 |
| 27-04 | 80 |  | Rebuild row: `\| antamaso \| ind \| \| even so much as, even with, even down to, with as little as \|`  ✔ *Reviewer B proposes the same.* | A3 |
| 27-05 | 82 |  | Rebuild row: `\| pariyāpanna- \| adj \| \| gone completely into, included in, belonging to, got into \|` (also drop the stray `”`)  ✔ *Reviewer B proposes the same.* | A3 |
| 27-06 | 89 |  | Rebuild row: `\| appaṭivibhatta- \| adj \| \| not dividing for oneself, without reservations, not without sharing with others \|` (also fixes typo "onself")  ✔ *Reviewer B proposes the same row, but keeps the gloss "not for oneself dividing".* | A3 |
| 27-07 | 111 |  | Rebuild row: `\| samādhi- \| noun \| \| perfect peace of mind, stability of mind, stillness of mind \|`  ✔ *Reviewer B proposes the same.* | A3 |
| 27-08 | 119 |  | POS `idioṃ` → `idiom` | A1 |
| 27-09 | 138 |  | Rebuild row: `\| diṭṭhi- \| noun \| \| view, belief, opinion, concept, theory, attitude \|` (drop duplicated "opinion")  ✔ *Reviewer B proposes the same row but keeps the duplicated "opinion".* | A3 |
| 27-10 | 142 |  | POS `idioṃ` → `idiom` | A1 |
| 27-11 | 157 | `cha` | `Grammar pl` → `x.nom.pl` — match corpus numeral convention | A4 |
| 27-12 | 170 | `no` | Gr `interr` → ∅ — *DPD: `no` is plain ind* | B-N81 |

## 28 — Principles of Non-Decline

`per-28-principles-of-non-decline.md` — 8 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 28-01 | 30 | `sannipāta-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 28-02 | 63 |  | `perferm` → `perform` | A6 |
| 28-03 | 82 |  | Rebuild row: `\| yathā- \| ind \| \| like, as, according to, on account of, because of, how \|`  ✔ *Reviewer B proposes the same.* | A3 |
| 28-04 | 88 |  | `as they has beed formulated` → `as they have been formulated` | A6 |
| 28-05 | 174 |  | Rebuild row: `\| kinti \| ind \| interr \| how then? in what way? \|` (Grammar had truncated `inter`) | A3 |
| 28-06 | 187 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 |
| 28-07 | 220 |  | `seven seven principles` → `seven principles` | A6 |
| 28-08 | 230 |  | Rebuild row: `\| pāṭikaṅkhā \| adj \| fem.nom.sg \| to be expected (for), certain (for), should be expected, can be anticipated \|` | A2 |

## 29 — Striving According to the Dhamma

`per-29-striving-according-to-the-dhamma.md` — 6 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 29-01 | 47 |  | `to arose energy` → `to arouse energy` | A6 |
| 29-02 | 281 |  | gloss `of theṃ` → `of them` | A1 |
| 29-03 | 284 | `amhesu` | `masc.loc.sg` → `1.loc.pl` — "in us", plural | A4 |
| 29-04 | 286 | `bhavissanti` | `POS pt` → `POS verb` — Grammar fut.3.pl already correct | A4 |
| 29-05 | 289 |  | `grate result and grate merit` → `great result and great merit` | A6 |
| 29-06 | 329 | `ubhaya-` | POS `pron` → `adj` — *adj (from `ubha`)* | B-N111 |

## 30 — The Buddha's Final Instruction

`per-30-the-buddhas-final-instruction.md` — 5 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 30-01 | 12 | `siyā` | Grammar `opt.3rd.sg` → `opt.3.sg` | A5.1 |
| 30-02 | 14 | `tumhākaṃ` | Grammar `2nd.dat.pl` → `2.dat.pl` | A5.1 |
| 30-03 | 29 | `no` | Grammar `1st.dat.pl` → `1.dat.pl` | A5.1 |
| 30-04 | 52 | `accayena` | ⚔ **C11 — keep ONE:** **Option A (audit)** Part 3: Grammar empty, full gloss incl. `lit. with gone past`  ·  **Option B (reviewer)** Grammar `adv`; reviewer's gloss is truncated (drops `, lit. with gone past`)  ·  *If B is chosen, apply only the Grammar `adv` and keep A's full gloss.* | B-C11 |
| 30-05 | 79 |  | `condition phenomena are of the liable to disintegrate` → `conditioned phenomena are liable to disintegrate`; `This is final statement` → `This is the final statement` | A6 |

## 31 — The Four Requisites

`per-31-the-four-requisites.md` — 21 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 31-01 | 21 | `ḍaṃsa-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 31-02 | 22 | `makasa-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 31-03 | 23 | `vāt'ātapa-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 31-04 | 24 | `siriṃsapa-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 31-05 | 30 |  | **D6** `\| attha \| noun \| masc.acc.sg \|` — bare `attha` cannot be acc.sg; chant probably has sandhi `…paṭicchādan'atthaṃ`. Suggest `atthaṃ` with a sandhi note; verify. | A8-D6 |
| 31-06 | 32 |  | `for ward off heat, for ward off the touch` → `to ward off heat, to ward off the touch` *(same fix at: per-31:32, per-31:99)* | A6 |
| 31-07 | 41 | `piṇḍapātaṃ` | Gr `masc` → `masc.acc.sg` — *grammar was only `masc`* | B-N58 |
| 31-08 | 53 | `vihiṃsa-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 31-09 | 55 | `brahmacariya-` | Grammar `nt` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 31-10 | 63 | `na-uppādessāmi` | POS `v.caus` → `verb`; Grammar `fut.1.sg` → `fut.1.sg.caus` | A5.9 |
| 31-11 | 71 |  | `assistance of holy live` → `assistance of the holy life`; `put an end of former` → `put an end to former`; `a new (painful) sensations` / `a new (painfull) sensations` → `new (painful) sensations`; per-31:71 also `(painfull)` → `(painful)` (2×) *(same fix at: per-19:817, per-31:71)* | A6 |
| 31-12 | 86 | `ḍaṃsa-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 31-13 | 87 | `makasa-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 31-14 | 88 | `vātātapa-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 31-15 | 89 | `siriṃsapa-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 31-16 | 93 |  | Rebuild row: `\| utuparissaya- \| noun \| \| inclement weather, harsh climate, lit. danger of the season \|`  ✔ *Reviewer B proposes the same.* | A3 |
| 31-17 | 95 |  | Rebuild row: `\| paṭisallāna- \| noun \| \| privacy, seclusion, solitude, lit. sticking to oneself \|` | A3 |
| 31-18 | 96 |  | Rebuild row: `\| ārāma- \| noun \| \| enjoyment, delight, pleasure \|` (current has corrupted "pleasureenjoyment" in Grammar + "delight, pleasure" in English) | A3 |
| 31-19 | 99 |  | `for ward off heat, for ward off the touch` → `to ward off heat, to ward off the touch` *(same fix at: per-31:32, per-31:99)* | A6 |
| 31-20 | 99 |  | `for the sake of removal the danger` → `for the sake of removal of the danger` | A6 |
| 31-21 | 118 | `paramatāyā` | `masc.dat.sg` → `fem.dat.sg` — paramatā is feminine | A4 |

## 32 — The Repulsiveness of Food

`per-32-the-repulsiveness-of-food.md` — 2 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 32-01 | 18 |  | `of living , abiding` → `of living, abiding` | A6 |
| 32-02 | 29 |  | `does not drawn towards it` → `is not drawn towards it` | A6 |

## 33 — Universal Well-Being

`per-33-universal-well-being.md` — 5 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 33-01 | 20 |  | gloss `calṃ lit. not trembling` → `calm, lit. not trembling` | A1 |
| 33-02 | 46 |  | gloss `calṃ lit. not trembling` → `calm, lit. not trembling` | A1 |
| 33-03 | 71 |  | `may all beings do not lost gained fortune` → `may all beings not lose their gained fortune` | A6 |
| 33-04 | 80 | `sakā-` | POS `noun` → `adj` | B-N112 |
| 33-05 | 88 | `paṭisaraṇoā` | Word `paṭisaraṇoā` → `paṭisaraṇā` — *obvious typo: chant has `kammapaṭisaraṇā`* | B-N131 |

## 34 — The Divine Abidings

`per-34-the-divine-abidings.md` — 8 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 34-01 | 13 | `sahagatena` | Grammar `nt.i.sg` → `nt.ins.sg`  ✔ *Reviewer B proposes the same.* | A5.6 |
| 34-02 | 14 | `cetasā` | Grammar `nt.i.sg` → `nt.ins.sg`  ✔ *Reviewer B proposes the same.* | A5.6 |
| 34-03 | 43 | `sabbattatāya` | POS `adj` → `ind`; Gr `masc.dat.sg` → `adv`; Eng `to all encompassing, all pervading lit. all spread out` → `to all beings; encompassing all living beings` | B-N113 |
| 34-04 | 51 |  | Rebuild row: `\| sabbāvantaṃ \| adj \| masc.acc.sg \| entire, whole \|`  ✔ *Reviewer B proposes the same.* | A2 |
| 34-05 | 53 | `mettāsahagatena` | Word `mettāsahagatena` → `mettā-sahagatena` — *chant line has `mettā-sahagatena` (hyphen); row should match* | B-N132 |
| 34-06 | 59 |  | Rebuild row: `\| abyāpajjena \| adj \| nt.ins.sg \| without ill will, with goodwill \|`  ✔ *Reviewer B proposes the same.* | A2 |
| 34-07 | 59 | `abyāpajjena` | Word `abyāpajjena` → `abyāpajjhena` — *amends audit Part 2 row for 34:59; chant line 34:47 already reads `abyāpajjhena`* | B-N135 |
| 34-08 | 61 | `viharati;` | Word `viharati;` → `viharati` — *stray `;`* | B-N133 |

## 35 — Five Subjects for Frequent Recollection

`per-35-five-subjects-for-frequent-recollection.md` — 6 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 35-01 | 12 | `jarā-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 35-02 | 24 | `byādhi-` | Grammar `nt` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 35-03 | 30 |  | `of the nature to sick` → `of the nature to sicken` | A6 |
| 35-04 | 55 |  | `from all that dear and pleasing` → `from all that is dear and pleasing` *(same fix at: per-35:55, per-36:88)* | A6 |
| 35-05 | 63 | `sako-` | POS `noun` → `adj` | B-N114 |
| 35-06 | 90 | `evaṃ` | Grammar ∅ → `adv` | B-P1 |

## 36 — Ten Subjects for Frequent Recollection by One Who Has Gone Forth

`per-36-ten-subjects-for-frequent-recollection-by-one-who-has-gone-forth.md` — 16 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 36-01 | 22 |  | `these are ten principles should often be reflected` → `these ten principles should often be reflected` | A6 |
| 36-02 | 28 | `vevaṇṇiya-` | ⚔ **C7 — keep ONE:** **Option A (audit)** Part 3: POS stays `adj`  ·  **Option B (reviewer)** POS `adj` → `noun`  ·  *Grammar empty in both; gloss merge identical.* | B-C7 |
| 36-03 | 60 | `kacci` | Grammar ∅ → `interr` | B-P6 |
| 36-04 | 61 | `nu kho` | Grammar ∅ → `interr` | B-P6 |
| 36-05 | 66 | `upavadatī'ti` | `pr.3.pl` → `pr.3.sg` — `-ti` singular; gloss is singular too | A4 |
| 36-06 | 74 | `kacci` | Grammar ∅ → `interr` | B-P6 |
| 36-07 | 75 | `nu kho` | Grammar ∅ → `interr` | B-P6 |
| 36-08 | 88 |  | `from all that dear and pleasing` → `from all that is dear and pleasing` *(same fix at: per-35:55, per-36:88)* | A6 |
| 36-09 | 104 |  | `How my days and nights pass?` → `How do my days and nights pass?` | A6 |
| 36-10 | 110 | `kacci` | Grammar ∅ → `interr` | B-P6 |
| 36-11 | 111 | `nu kho` | Grammar ∅ → `interr` | B-P6 |
| 36-12 | 124 | `nu kho` | Grammar ∅ → `interr` | B-P6 |
| 36-13 | 125 | `me` | Grammar `1.instr.sg` → `1.ins.sg` | A5.2 |
| 36-14 | 126 | `uttari-` | Rebuild row as `\| uttari- \| adj \| \| over; beyond; further; moreover; additional \|` | B-N9 |
| 36-15 | 140 | `na` | Rebuild row as `\| na \| ind \| \| not \|` | B-N10 |
| 36-16 | 148 |  | `these is ten principles should often be reflected` → `these ten principles should often be reflected` | A6 |

## 37 — The Thirty-Two Parts

`per-37-the-thirty-two-parts.md` — 6 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 37-01 | 7 |  | **D9** sutta reference `[dn 22.5]` → `[DN 22.5]` (match `[SN 56.11]`, `[MN 27 / 38 / 51]` style) | A8-D9 |
| 37-02 | 22 | `pariyantaṃ` | Gr `masc.acc.sg` → `masc.nom.sg`; Word `pariyantaṃ` → `pariyanto` — *chant line has `taca-pariyanto` (nom.)* | B-N134 |
| 37-03 | 33 | `atthi` | `pres.3.pl` → `pr.3.sg` — normalize `pres`; atthi is 3.sg (used with plural list) | A4 |
| 37-04 | 55 |  | **D1** Delete this duplicate row `\| matthaluṅgaṃ \| noun \| nt.nom.sg \| the brain \|` (chant line lists it once, at the end), and delete the first "brain" in the translation line (L70). Needs approval (data-preservation rule).  ✔ *Reviewer B also deleted this row.* | A8-D1 |
| 37-05 | 57 |  | gloss `phlegṃ` → `phlegm` | A1 |
| 37-06 | 70 |  | **D1** (part 2) remove the first "brain" from this translation line. | A8-D1 |

## 38 — Recollection of Impermanence

`per-38-recollection-of-impermanence.md` — 7 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 38-01 | 59 | `avassaṃ` | Grammar ∅ → `adv` | B-P1 |
| 38-02 | 63 |  | **D10** `inevitable by me to be dead` — literal but broken English; recommend "my death is unavoidable" (verify against the Pāḷi line and neighbouring lines). | A8-D10 |
| 38-03 | 100 | `vata` | Grammar ∅ → `excl` | B-P4 |
| 38-04 | 103 | `aciraṃ` | Grammar ∅ → `adv` | B-P1 |
| 38-05 | 113 |  | `on the the ground` → `on the ground` | A6 |
| 38-06 | 120 | `vata` | Grammar ∅ → `excl` | B-P4 |
| 38-07 | 150 | `sukho` | POS `noun` → `adj` | B-N115 |

## 39 — DhammacakkappavattanaSutta

`per-39-dhammacakkappavattana-sutta.md` — 13 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 39-01 | 3 |  | **D9** Title `DhammacakkappavattanaSutta` → `Dhammacakkappavattana-Sutta` | A8-D9 |
| 39-02 | 21 | `isipatane` | `(English cell empty)` → `add gloss in Isipatana` — missing gloss | A4 |
| 39-03 | 22 | `migadāye` | `masc.gen.sg, English empty` → `masc.loc.sg + gloss in the Deer Park` — locative; missing gloss | A4 |
| 39-04 | 28 | `tatra` | Grammar ∅ → `adv` | B-P1 |
| 39-05 | 29 | `kho` | Grammar ∅ → `emph` | B-P3 |
| 39-06 | 48 | `te` | Rebuild row as `\| te \| pron \| masc.nom.pl \| those \|` — *columns shifted; audit Part 2 missed this row; abbreviation `m.n.pl`* | B-N11 |
| 39-07 | 89 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 |
| 39-08 | 97 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 |
| 39-09 | 103 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 |
| 39-10 | 109 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 |
| 39-11 | 117 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 |
| 39-12 | 129 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 |
| 39-13 | 137 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 |

## 40 — Anatta-Lakkhaṇa-Sutta

`per-40-anatta-lakkhana-sutta.md` — 46 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 40-01 | 11 | `evaṃ-` | Grammar ∅ → `adv` | B-P1 |
| 40-02 | 12 | `me` | `masc.ins.sg` → `1.ins.sg` — personal pronoun convention (digit person) | A4 |
| 40-03 | 13 | `sutaṃ` | `masc.acc.sg` → `nt.nom.sg` — `evaṃ me sutaṃ` = "thus it was heard by me" (pp as nt. subject) | A4 |
| 40-04 | 19 |  | `in jetavana (jets's grove)` → `in Jetavana (Jeta's grove)` | A6 |
| 40-05 | 23 |  | `in sāvatthi in jets's grove in anāthapindika's park` → `in Sāvatthī in Jeta's Grove in Anāthapiṇḍika's park` | A6 |
| 40-06 | 27 | `tatra` | Grammar ∅ → `adv` | B-P1 |
| 40-07 | 28 | `kho` | Grammar ∅ → `emph` | B-P3 |
| 40-08 | 52 |  | POS `idioṃ` → `idiom` | A1 |
| 40-09 | 59 |  | `onself` → `oneself` *(same fix at: per-40:59, per-40:72, per-40:94, per-40:107, per-40:124, per-40:137)* | A6 |
| 40-10 | 59 | `labbhetha` | POS `v.pass` → `verb`; Grammar `opt.refl.3.sg` → `opt.refl.3.sg.pass` | A5.9 |
| 40-11 | 60 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 40-12 | 62 | `evaṃ` | Grammar ∅ → `adv` | B-P1 |
| 40-13 | 66 | `evaṃ` | Grammar ∅ → `adv` | B-P1 |
| 40-14 | 72 |  | `than form/feeling/perception/volitional formations could not` → `then …` (4×) *(same fix at: per-40:72, per-40:94, per-40:107, per-40:124)* | A6 |
| 40-15 | 72 |  | `onself` → `oneself` *(same fix at: per-40:59, per-40:72, per-40:94, per-40:107, per-40:124, per-40:137)* | A6 |
| 40-16 | 78 | `yasmā` | Grammar ∅ → `adv` | B-P1 |
| 40-17 | 79 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 40-18 | 80 | `kho` | Grammar ∅ → `emph` | B-P3 |
| 40-19 | 82 | `tasmā` | Grammar ∅ → `adv` | B-P1 |
| 40-20 | 83 | `no labbhati` | POS `v.pass` → `verb`; Grammar `pr.3.sg` → `pr.3.sg.pass` | A5.9 |
| 40-21 | 94 |  | `than form/feeling/perception/volitional formations could not` → `then …` (4×) *(same fix at: per-40:72, per-40:94, per-40:107, per-40:124)* | A6 |
| 40-22 | 94 |  | `onself` → `oneself` *(same fix at: per-40:59, per-40:72, per-40:94, per-40:107, per-40:124, per-40:137)* | A6 |
| 40-23 | 107 |  | `than form/feeling/perception/volitional formations could not` → `then …` (4×) *(same fix at: per-40:72, per-40:94, per-40:107, per-40:124)* | A6 |
| 40-24 | 107 |  | `onself` → `oneself` *(same fix at: per-40:59, per-40:72, per-40:94, per-40:107, per-40:124, per-40:137)* | A6 |
| 40-25 | 122 |  | **D6** `ahesun'ti` gloss reads "but pr. - may they be," — garbled; needs a proper gloss ("(if they) had been", aor.3.pl). | A8-D6 |
| 40-26 | 124 |  | `than form/feeling/perception/volitional formations could not` → `then …` (4×) *(same fix at: per-40:72, per-40:94, per-40:107, per-40:124)* | A6 |
| 40-27 | 124 |  | `onself` → `oneself` *(same fix at: per-40:59, per-40:72, per-40:94, per-40:107, per-40:124, per-40:137)* | A6 |
| 40-28 | 137 |  | `onself` → `oneself` *(same fix at: per-40:59, per-40:72, per-40:94, per-40:107, per-40:124, per-40:137)* | A6 |
| 40-29 | 186 | `nu` | Grammar ∅ → `interr` | B-P6 |
| 40-30 | 188 | `samanupassituṃ` | POS `verbinf` → `verb`; Grammar `` → `inf` | A5.8 |
| 40-31 | 205 | `hi-` | Grammar ∅ → `emph` | B-P3 |
| 40-32 | 264 |  | Pāḷi is `viññāṇaṃ niccaṃ vā aniccaṃ vā'ti`; translation "Is **conscience** permanent or impermanent?" → "Is **consciousness** permanent or impermanent?" | A7 |
| 40-33 | 283 | `tasmā-(t)` | Grammar ∅ → `adv` | B-P1 |
| 40-34 | 285 | `bhikkhave` | Grammar `masc.v.sg` → `masc.voc.sg` | A5.6 |
| 40-35 | 287 |  | `something , anything` → `something, anything` | A6 |
| 40-36 | 293 | `vā` | Rebuild row as `\| vā \| ind \| \| or \|` | B-N12 |
| 40-37 | 295 | `vā` | Rebuild row as `\| vā \| ind \| \| or \|` | B-N13 |
| 40-38 | 297 | `vā` | Rebuild row as `\| vā \| ind \| \| or \|` | B-N14 |
| 40-39 | 299 | `vā` | Rebuild row as `\| vā \| ind \| \| or \|` | B-N15 |
| 40-40 | 301 | `vā` | Rebuild row as `\| vā \| ind \| \| or \|` | B-N16 |
| 40-41 | 303 | `vā` | Rebuild row as `\| vā \| ind \| \| or \|` | B-N17 |
| 40-42 | 307 | `vā` | Rebuild row as `\| vā \| ind \| \| or \|` | B-N18 |
| 40-43 | 327 |  | **D8** quote style: `''` closers on lines 327–343 (policy D8) | A8-D8 |
| 40-44 | 353 |  | gloss `in forṃ` → `in form` | A1 |
| 40-45 | 362 | `vimuccati` | POS `v.pass` → `verb`; Grammar `pr.3.sg` → `pr.3.sg.pass` | A5.9 |
| 40-46 | 419 |  | `throught not grasping` → `through not grasping` *(same fix at: per-40:419, per-41:277)* | A6 |

## 41 — Āditta-Pariyāya-Sutta

`per-41-aditta-pariyaya-sutta.md` — 20 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 41-01 | 12 | `evaṃ-` | Grammar ∅ → `adv` | B-P1 |
| 41-02 | 13 | `me` | `masc.ins.sg` → `1.ins.sg` — same | A4 |
| 41-03 | 14 | `sutaṃ` | `masc.acc.sg` → `nt.nom.sg` — same | A4 |
| 41-04 | 21 | `saddhiṃ` | Grammar ∅ → `prep` | B-P5 |
| 41-05 | 23 | `tatra` | Grammar ∅ → `adv` | B-P1 |
| 41-06 | 24 | `kho` | Grammar ∅ → `emph` | B-P3 |
| 41-07 | 41 |  | "Monks, everything is burning? And what is everything what is burning?" → "Monks, everything is burning. And what is the everything that is burning?" | A7 |
| 41-08 | 52 |  | POS `idioṃ` → `idiom` | A1 |
| 41-09 | 63 |  | POS `idioṃ` → `idiom` (row also fixed in Part 3, item merges gloss)  ✔ *Reviewer B proposes the same.* | A1 |
| 41-10 | 63 |  | Rebuild row: `\| tam'pi \| idiom \| \| that too, he too, even that, just that, that very thing \|` | A3 |
| 41-11 | 74 | `dos'agginā` | `nt.ins.sg` → `masc.ins.sg` — aggi is masculine; also fix `hate , aversion` → `hate, aversion` | A4 |
| 41-12 | 76 |  | Rebuild row: `\| jātiyā \| noun \| fem.ins.sg \| with birth, rebirth, conception \|`  ✔ *Reviewer B proposes the same.* | A2 |
| 41-13 | 79 | `sokehi` | `masc.ins.sg` → `masc.ins.pl` — `-ehi` plural | A4 |
| 41-14 | 80 | `paridevehi` | `masc.ins.sg` → `masc.ins.pl` — `-ehi` plural | A4 |
| 41-15 | 168 | `evaṃ` | Grammar ∅ → `adv` | B-P1 |
| 41-16 | 177 |  | POS `idioṃ` → `idiom` | A1 |
| 41-17 | 220 | `vimuccati` | POS `v.pass` → `verb`; Grammar `pr.3.sg` → `pr.3.sg.pass` | A5.9 |
| 41-18 | 243 |  | `What have to be done – is done` → `What has to be done – is done` | A6 |
| 41-19 | 254 | `te` | Rebuild row as `\| te \| pron \| masc.nom.pl \| those \|` — *same as 39:48* | B-N19 |
| 41-20 | 277 |  | `throught not grasping` → `through not grasping` *(same fix at: per-40:419, per-41:277)* | A6 |

## 42 — Yathā Vāri-Vahā

`per-42-yatha-vari-vaha.md` — 19 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 42-01 | 10 | `yathā` | Grammar ∅ → `adv` | B-P1 |
| 42-02 | 23 | `evam'eva` | Grammar ∅ → `adv` | B-P1 |
| 42-03 | 24 | `ito` | Grammar ∅ → `adv` | B-P1 |
| 42-04 | 25 | `dinnaṃ` | POS `adj` → `pp` | B-N116 |
| 42-05 | 27 | `upakappati` | Eng `is beneficial to, is serve for, is accrue` → `is beneficial to, serves, accrues` — *grammar fixes in the gloss* | B-N126 |
| 42-06 | 39 | `khippaṃ-` | Grammar ∅ → `adv` | B-P1 |
| 42-07 | 40 | `eva` | Grammar ∅ → `emph` | B-P3 |
| 42-08 | 41 | `samijjhatu` | Eng `may it achieves, succeeds, prospers` → `may it achieve, succeed, prosper` | B-N127 |
| 42-09 | 43 |  | `May your desires and wishes be succeeds only quickly.` → `May your desires and wishes succeed quickly.`  ✔ *Reviewer B proposes the same.* | A6 |
| 42-10 | 61 | `yathā` | Grammar ∅ → `adv` | B-P1 |
| 42-11 | 71 | `yathā` | Grammar ∅ → `adv` | B-P1 |
| 42-12 | 81 | `vivajjantu` | Eng `may they be avoided, abandoned, forsaked` → `may they be avoided, abandoned, forsaken` — *typo `forsaked`* | B-N128 |
| 42-13 | 91 | `vinassatu` | `pr.3.sg` → `imp.3.sg` — `-tu` imperative ("may it disappear")  ✔ *Reviewer B proposes the same.* | A4 |
| 42-14 | 104 |  | `May danger does not be for you.` → `May there be no danger for you.`  ✔ *Reviewer B proposes the same.* | A6 |
| 42-15 | 121 | `abhivādana-` | Grammar `nt` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 42-16 | 140 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 |
| 42-17 | 147 | `rakkhantu` | Gr `imp.3.sg` → `imp.3.pl` — *`rakkhantu` is 3.pl* | B-N82 |
| 42-18 | 153 | `sadā` | Grammar ∅ → `adv` | B-P1 |
| 42-19 | 156 | `te` | Gr `1.dat.sg` → `2.dat.sg` — *audit Part 4 has the same fix for te@51:44, 59:58, 63:33 but not this row* | B-N59 |

## 43 — Ratanattayānubhāv'ādi-Gāthā

`per-43-ratanattayanubhavadi-gatha.md` — 10 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 43-01 | 11 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 |
| 43-02 | 19 |  | Rebuild row: `\| dukkha- \| noun \| \| discomfort, suffering, pain, unease, something unsatisfactory, problem, trouble \|`  ✔ *Reviewer B proposes the same.* | A3 |
| 43-03 | 22 | `verā` | Gr `masc.nom.pl` → `nt.nom.pl` — *`vera` neuter* | B-N60 |
| 43-04 | 30 | `asesato` | Grammar ∅ → `adv` | B-P1 |
| 43-05 | 48 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 43-06 | 50 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 43-07 | 53 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 43-08 | 54 | `yasavā` | Eng `famous, renowned, lit.: possessing fame'` → `famous, renowned, lit.: possessing fame` — *stray `'` removed* | B-N129 |
| 43-09 | 57 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 43-10 | 59 | `ca` | Grammar ∅ → `conj` | B-P2 |

## 44 — Bhojana-Dānānumodanā

`per-44-bhojana-dananumodana.md` — 3 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 44-01 | 40 | `sukhassa` | Gr `masc.gen.sg` → `nt.gen.sg` — *`sukha` neuter* | B-N61 |
| 44-02 | 55 | `yattha` | Grammar ∅ → `adv` | B-P1 |
| 44-03 | 56 | `yattha-` | Grammar ∅ → `adv` | B-P1 |

## 45 — Culla-Maṅgala-Cakka-Vāḷa

`per-45-culla-mangala-cakka-vala.md` — 11 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 45-01 | 47 |  | `ny the power` → `by the power` | A6 |
| 45-02 | 78 | `sabbadā` | Grammar ∅ → `adv` | B-P1 |
| 45-03 | 86 |  | Rebuild row: `\| dukkha- \| noun \| \| discomfort, suffering, pain, unease, something unsatisfactory, problem, trouble \|`  ✔ *Reviewer B proposes the same.* | A3 |
| 45-04 | 89 | `verā` | Gr `masc.nom.pl` → `nt.nom.pl` — *same as 43:22* | B-N62 |
| 45-05 | 97 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 45-06 | 116 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 45-07 | 118 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 45-08 | 121 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 45-09 | 125 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 45-10 | 127 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 45-11 | 133 |  | `May be f or you` → `May there be for you`  ✔ *Reviewer B proposes the same.* | A6 |

## 46 — Aggappasāda-Sutta-Gāthā

`per-46-aggappasada-sutta-gatha.md` — 3 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 46-01 | 11 | `ve` | Grammar ∅ → `emph` | B-P3 |
| 46-02 | 54 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 46-03 | 56 | `ca` | Grammar ∅ → `conj` | B-P2 |

## 47 — Kāla-Dāna-Sutta-Gāthā

`per-47-kala-dana-sutta-gatha.md` — 9 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 47-01 | 10 | `kāle` | Grammar ∅ → `adv` | B-P1 |
| 47-02 | 15 |  | Rebuild row: `\| kālena \| ind \| adv \| timely, at the right moment, at a suitable time, at the proper time \|`  ✔ *Reviewer B proposes the same.* | A3 |
| 47-03 | 16 | `dinnaṃ` | Gr `nt.acc.sg` → `nt.nom.sg`; Eng `given, offered` → `a gift given, what is given` — *pp is the subject: nt.nom; gloss changes to match* | B-N63 |
| 47-04 | 33 | `tattha` | Grammar ∅ → `adv` | B-P1 |
| 47-05 | 52 | `tasmā` | Grammar ∅ → `adv` | B-P1 |
| 47-06 | 54 |  | Rebuild row: `\| appaṭivāna- \| adj \| \| with confidence, without regret, lit. not shrinking back \|`  ✔ *Reviewer B proposes the same.* | A3 |
| 47-07 | 56 | `yattha` | Grammar ∅ → `adv` | B-P1 |
| 47-08 | 57 | `dinnaṃ` | Gr `masc.acc.sg` → `nt.nom.sg`; Eng `given, offered` → `gift, what is given` — *same as 47:16* | B-N64 |
| 47-09 | 58 | `mahapphalaṃ` | Gr `masc.acc.sg` → `nt.nom.sg`; Eng `of great fruit, yielding good results` → `of great fruit, yielding great results` — *predicate agrees with subject `dinnaṃ` (also gloss `good` → `great`)* | B-N65 |

## 48 — So Attha-Laddho

`per-48-so-attha-laddho.md` — 2 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 48-01 | 12 | `laddhā` | POS `verb` → `pp`; Gr `ger` → `masc.nom.pl`; Eng `getting, obtaining` → `having obtained, having gotten` — *reviewer: `laddha` is a past participle, not a gerund* | B-N117 |
| 48-02 | 19 | `saha` | Grammar ∅ → `prep` | B-P5 |

## 49 — Devā-ārādhanāi

`per-49-deva-aradhanai.md` — 8 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 49-01 | 3 |  | **D2** Title `Devā-ārādhanāi` carries a stray trailing `i` (standard: `Devā-ārādhanā`). Recommend: fix the visible title only, keep the filename (renaming would need nav links in per-48/per-50, index and feedback URL). | A8-D2 |
| 49-02 | 27 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 49-03 | 32 | `c'antalikkhe` | POS `ind` → `sandhi` (leave Grammar empty; reviewer also wrote `conj + loc` in Grammar) | B-P7 |
| 49-04 | 36 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 49-05 | 61 | `santike` | Grammar ∅ → `adv` | B-P1 |
| 49-06 | 66 |  | **D6** `sādhavo` tagged ind — looks like masc.nom.pl of `sādhu` ("good sirs"); verify against chant context. | A8-D6 |
| 49-07 | 66 | `sādhavo` | ⚔ **C6 — keep ONE:** **Option A (audit)** Part 3: keep `ind`, merge gloss: `accomplishing, fulfilling, effecting, completing, with approval` (D6 asks to verify)  ·  **Option B (reviewer)** POS `ind` → `adj`, Grammar → `masc.nom.pl`, Eng → `good ones, virtuous ones`  ·  *B answers D6 (reviewer: `sādhavo me suṇantu` = "may the virtuous ones hear from me").* | B-C6 |
| 49-08 | 67 | `me` | ⚔ **C5 — keep ONE:** **Option A (audit)** Part 3: `me / pron / 1.dat.sg / for me`  ·  **Option B (reviewer)** `me / pron / 1.gen.sg / my, of me, by me`  ·  *Context `bhaṇantu me` / `suṇantu me`: dative-sense ("for me") vs genitive-sense.* | B-C5 |

## 50 — Saraṇa-Gamana-Pāṭho

`per-50-sarana-gamana-patho.md` — 4 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 50-01 | 18 | `dutiyam'pi` | POS `adv+ind` — unify to one form (see policy D4) | A8-D4 |
| 50-02 | 18 |  | multi-word POS tag (`v + pn` / `ind+pn` / `ind+m+imp` / `adv+ind`): use `idiom` or `sandhi` per corpus convention (policy D4) | A8-D4 |
| 50-03 | 26 | `tatiyam'pi` | POS `adv+ind` — unify to one form (see policy D4) | A8-D4 |
| 50-04 | 26 |  | multi-word POS tag (`v + pn` / `ind+pn` / `ind+m+imp` / `adv+ind`): use `idiom` or `sandhi` per corpus convention (policy D4) | A8-D4 |

## 51 — Nama-Kāra-Siddhi-Gāthā

`per-51-nama-kara-siddhi-gatha.md` — 10 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 51-01 | 15 | `sāmaṃ` | Grammar ∅ → `adv` | B-P1 |
| 51-02 | 16 | `va = eva` | Grammar ∅ → `emph` | B-P3 |
| 51-03 | 44 | `te` | `masc.dat.sg` → `2.dat.sg` — "for you" = 2nd person pronoun  ✔ *Reviewer B proposes the same.* | A4 |
| 51-04 | 44 | `te` | POS `noun` → `pron` — *extends audit Part 4 (which only changes Grammar to `2.dat.sg`)* | B-N121 |
| 51-05 | 47 | `hotu` | `pr.3.sg` → `imp.3.sg` — `-tu` imperative  ✔ *Reviewer B proposes the same.* | A4 |
| 51-06 | 50 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 51-07 | 67 | `visuddhi-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 51-08 | 76 | `suciṇṇo` | POS `noun` → `adj` — *`suciṇṇo` adj per DPD* | B-N118 |
| 51-09 | 105 | `sayaṃ` | Grammar ∅ → `adv` | B-P1 |
| 51-10 | 108 | `ca` | Grammar ∅ → `conj` | B-P2 |

## 52 — Namo-Kāra-Aṭṭhaka

`per-52-namo-kara-atthaka.md` — 19 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 52-01 | 10 | `namo` | Grammar ∅ → `excl` | B-P4 |
| 52-02 | 12 | `sammā-` | Grammar ∅ → `adv` | B-P1 |
| 52-03 | 15 | `namo` | Grammar ∅ → `excl` | B-P4 |
| 52-04 | 20 | `idha` | Grammar ∅ → `adv` | B-P1 |
| 52-05 | 28 | `namo` | Grammar ∅ → `excl` | B-P4 |
| 52-06 | 34 | `namo` | Grammar ∅ → `excl` | B-P4 |
| 52-07 | 35 |  | **D3** `<br>` inside table cells (lines 35). Policy: keep (note the exception) or convert `A<br>(or)<br>B` → `A (or) B`. | A8-D3 |
| 52-08 | 36 | `omāti-` | Grammar `pr.3rd.sg` → `pr.3.sg` | A5.1 |
| 52-09 | 37 | `āraddhassa` | POS `noun` → `pp`; Eng `accomplishment, achievement; success` → `won; accomplished; succeeded` — *reviewer: `āraddha` is a past participle (DPD)* | B-N119 |
| 52-10 | 38 | `ratanattayassa` | Gr `masc.dat.sg` → `nt.dat.sg` — *`ratanattaya` neuter* | B-N66 |
| 52-11 | 39 | `sādhukaṃ` | Grammar ∅ → `adv` | B-P1 |
| 52-12 | 41 |  | `Tiple Gem` → `Triple Gem`; `succseed` → `succeed` | A6 |
| 52-13 | 47 | `namo` | Grammar ∅ → `excl` | B-P4 |
| 52-14 | 50 | `vatthu-ttayassa'pi` | Gr `masc.dat.sg` → `nt.dat.sg` — *`vatthu` neuter* | B-N67 |
| 52-15 | 51 | `namo-` | Grammar ∅ → `excl` | B-P4 |
| 52-16 | 63 | `namo-` | Grammar ∅ → `excl` | B-P4 |
| 52-17 | 66 | `suvatthi` | Gr `masc.nom.sg` → `fem.nom.sg` — *DPD: suvatthi fem. (audit Part 3 item per-54:110 already uses fem.nom.sg for the same word)* | B-N68 |
| 52-18 | 68 | `sabbadā` | Grammar ∅ → `adv` | B-P1 |
| 52-19 | 69 | `namo-` | Grammar ∅ → `excl` | B-P4 |

## 53 — Maṅgala-Sutta

`per-53-mangala-sutta.md` — 56 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 53-01 | 10 | `evaṃ-` | Grammar ∅ → `adv` | B-P1 |
| 53-02 | 11 | `me` | `masc.ins.sg` → `1.ins.sg` — same | A4 |
| 53-03 | 12 | `sutaṃ` | `masc.acc.sg` → `nt.nom.sg` — same  ✔ *Reviewer B proposes the same.* | A4 |
| 53-04 | 12 | `sutaṃ:` | Eng `heard` → `what is heard; something heard` — *extends audit Part 4 (`sutaṃ` → nt.nom.sg)* | B-N122 |
| 53-05 | 38 | `yena` | Grammar ∅ → `adv` | B-P1 |
| 53-06 | 40 | `tena-` | Grammar ∅ → `adv` | B-P1 |
| 53-07 | 52 | `ekaṃantaṃ` | Grammar ∅ → `adv` | B-P1 |
| 53-08 | 54 | `ekaṃantaṃ` | Grammar ∅ → `adv` | B-P1 |
| 53-09 | 56 | `kho` | Grammar ∅ → `emph` | B-P3 |
| 53-10 | 60 | `gāthāya` | `fem.ins` → `fem.ins.sg` — number missing | A4 |
| 53-11 | 75 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-12 | 80 | `brūhi` | `imp.3.sg` → `imp.2.sg` — "you speak" is 2nd person  ✔ *Reviewer B proposes the same.* | A4 |
| 53-13 | 80 | `brūhi` | Eng `you speak, may you say, you shall talk` → `say!; tell!; speak!` — *extends audit Part 4 (`brūhi` → imp.2.sg)* | B-N123 |
| 53-14 | 84 |  | `tall about highest blessing` → `tell about the highest blessing` | A6 |
| 53-15 | 84 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 |
| 53-16 | 94 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-17 | 95 | `bālānaṃ,` | Gr `masc.dat.pl` → `masc.gen.pl`; Eng `to ignorant; fools` → `of fools; ignorant ones` — *dat → gen (also changes gloss `to ignorant; fools` → `of fools; ignorant ones`)* | B-N69 |
| 53-18 | 96 | `paṇḍitānaṃ-` | Gr `masc.dat.pl` → `masc.gen.pl`; Eng `to wise people` → `of wise people` — *dat → gen (gloss `to wise people` → `of wise people`)* | B-N70 |
| 53-19 | 97 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-20 | 100 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-21 | 101 | `pūjanīyānaṃ,` | POS `adj, ptp` → `ptp`; Gr `masc.dat.pl` → `masc.gen.pl`; Eng `to entitled to homage; should be venerated` → `of those worthy of veneration; who should be revered` — *same dat → gen fix as `bālānaṃ` / `paṇḍitānaṃ` / `ñātakānaṃ` in 12.2a* | B-N120 |
| 53-22 | 102 | `etaṃ` | Gr `masc.acc.sg` → `nt.nom.sg` — *neuter, subject* | B-N71 |
| 53-23 | 117 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-24 | 119 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-25 | 122 | `sammā-` | Grammar ∅ → `adv` | B-P1 |
| 53-26 | 124 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-27 | 135 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-28 | 137 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-29 | 139 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-30 | 142 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-31 | 152 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 |
| 53-32 | 163 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-33 | 175 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-34 | 177 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-35 | 178 | `ñātakānaṃ-` | Gr `masc.dat.pl` → `masc.gen.pl`; Eng `to relations, relatives, kinsmans` → `of relations, relatives, kinsmen` — *dat → gen (gloss `to relations, relatives, kinsmans` → `of relations, relatives, kinsmen`)* | B-N72 |
| 53-36 | 179 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-37 | 196 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-38 | 199 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-39 | 211 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-40 | 213 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-41 | 215 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-42 | 217 | `kālena` | Grammar ∅ → `adv` | B-P1 |
| 53-43 | 230 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-44 | 233 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-45 | 235 | `kālena` | Grammar ∅ → `adv` | B-P1 |
| 53-46 | 247 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 |
| 53-47 | 252 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-48 | 254 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-49 | 257 |  | Rebuild row: `\| nibbāna- \| noun \| \| going out (of a lamp), extinguishment (of a fire), quenching, peace \|` | A3 |
| 53-50 | 259 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 53-51 | 273 | `na` | reviewer: Grammar `neg` → ∅ — **⚑ user decision, not implemented unless you remove the ⚑** (for the word `na` the corpus has 33 rows with empty Grammar vs 7 `neg`) | **B-X2⚑** |
| 53-52 | 287 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 |
| 53-53 | 295 | `sabbattha'm-` | Grammar ∅ → `adv` | B-P1 |
| 53-54 | 297 | `sabbattha` | Grammar ∅ → `adv` | B-P1 |
| 53-55 | 298 | `sotthiṃ` | Grammar ∅ → `adv` | B-P1 |
| 53-56 | 304 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 |

## 54 — Ratana-Sutta

`per-54-ratana-sutta.md` — 35 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 54-01 | 29 | `eva` | Grammar ∅ → `emph` | B-P3 |
| 54-02 | 35 | `sakkacca` | Grammar ∅ → `adv` | B-P1 |
| 54-03 | 46 | `tasmā` | Grammar ∅ → `adv` | B-P1 |
| 54-04 | 47 | `hi` | Grammar ∅ → `emph` | B-P3 |
| 54-05 | 48 | `bhūtā` | Grammar `masc.v.pl` → `masc.voc.pl` | A5.6 |
| 54-06 | 49 | `nisāmetha` | POS `v.caus` → `verb`; Grammar `imp.2.pl` → `imp.2.pl.caus` | A5.9 |
| 54-07 | 68 | `tasmā` | Grammar ∅ → `adv` | B-P1 |
| 54-08 | 69 | `hi` | Grammar ∅ → `emph` | B-P3 |
| 54-09 | 74 |  | translation `protect theṃ` → `protect them` | A1 |
| 54-10 | 91 | `na` | reviewer: Grammar `neg` → ∅ — **⚑ user decision, not implemented unless you remove the ⚑** (for the word `na` the corpus has 33 rows with empty Grammar vs 7 `neg`) | **B-X2⚑** |
| 54-11 | 110 |  | Rebuild row: `\| suvatthi \| noun \| fem.nom.sg \| safety, well-being, blessing; su+[v]+√as+ti \|` (grammar cell held the gloss; root note kept at end) | A3 |
| 54-12 | 126 | `ajjhagā` | `imperf.3.sg` → `aor.3.sg` — same form | A4 |
| 54-13 | 128 |  | gloss `firṃ attentive` → `firm, attentive` | A1 |
| 54-14 | 129 | `na` | reviewer: Grammar `neg` → ∅ — **⚑ user decision, not implemented unless you remove the ⚑** (for the word `na` the corpus has 33 rows with empty Grammar vs 7 `neg`) | **B-X2⚑** |
| 54-15 | 144 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 |
| 54-16 | 160 | `na` | reviewer: Grammar `neg` → ∅ — **⚑ user decision, not implemented unless you remove the ⚑** (for the word `na` the corpus has 33 rows with empty Grammar vs 7 `neg`) | **B-X2⚑** |
| 54-17 | 202 | `nikkāmino` | `masc.ins.sg` → `masc.nom.pl` — nom. pl. agreeing with `ye … nikkāmino`; gloss stays | A4 |
| 54-18 | 203 |  | Rebuild row: `\| gotama- \| adj \| \| family name of the Buddha; lit. of the Gotama clan \|` | A3 |
| 54-19 | 206 | `patti-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 54-20 | 211 | `mudhā` | Grammar ∅ → `adv` | B-P1 |
| 54-21 | 224 | `yathā-` | Grammar ∅ → `adv` | B-P1 |
| 54-22 | 232 | `tathā-` | Grammar ∅ → `adv` | B-P1 |
| 54-23 | 238 | `avecca` | Grammar ∅ → `adv` | B-P1 |
| 54-24 | 256 | `kiñcāpi` | POS `ind` → `sandhi` (leave Grammar empty) | B-P7 |
| 54-25 | 261 | `na` | reviewer: Grammar `neg` → ∅ — **⚑ user decision, not implemented unless you remove the ⚑** (for the word `na` the corpus has 33 rows with empty Grammar vs 7 `neg`) | **B-X2⚑** |
| 54-26 | 276 | `saha-` | Grammar ∅ → `prep` | B-P5 |
| 54-27 | 277 | `eva` | Grammar ∅ → `emph` | B-P3 |
| 54-28 | 306 | `ca-` | Grammar ∅ → `conj` | B-P2 |
| 54-29 | 320 | `kiñcāpi` | POS `ind` → `sandhi` (leave Grammar empty) | B-P7 |
| 54-30 | 350 | `yathā` | Grammar ∅ → `adv` | B-P1 |
| 54-31 | 357 | `tathā-` | Grammar ∅ → `adv` | B-P1 |
| 54-32 | 373 |  | `knower the best , who` → `knower of the best, who` | A6 |
| 54-33 | 394 |  | Rebuild row: `\| viratta- \| pp \| \| detached (from); without desire (for); become indifferent (to); lost interest (in) \|` | A3 |
| 54-34 | 404 | `yathā-` | Grammar ∅ → `adv` | B-P1 |
| 54-35 | 420 |  | Rebuild row: same fix as :110 (identical row later in file) | A3 |

## 55 — Karaṇīya-Metta-Sutta

`per-55-karaniya-metta-sutta.md` — 33 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 55-01 | 11 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 |
| 55-02 | 33 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 55-03 | 36 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 55-04 | 51 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 55-05 | 53 | `ca,` | Grammar ∅ → `conj` | B-P2 |
| 55-06 | 55 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 55-07 | 63 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 55-08 | 65 | `ca,` | Grammar ∅ → `conj` | B-P2 |
| 55-09 | 79 | `na` | reviewer: Grammar `neg` → ∅ — **⚑ user decision, not implemented unless you remove the ⚑** (for the word `na` the corpus has 33 rows with empty Grammar vs 7 `neg`) | **B-X2⚑** |
| 55-10 | 80 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 55-11 | 125 | `atthi` | `pr.3.pl` → `pr.3.sg` — atthi is singular (used distributively: "there are") | A4 |
| 55-12 | 174 |  | `whoever , that which` → `whoever, that which` | A6 |
| 55-13 | 176 | `dūre` | Grammar ∅ → `adv` | B-P1 |
| 55-14 | 178 | `avidūre` | Grammar ∅ → `adv` | B-P1 |
| 55-15 | 207 | `nikubbetha` | Grammar `opt.3.sg refl` → `opt.refl.3.sg` (reviewer did not touch this row; B-11.2 does not apply) | A5.3 |
| 55-16 | 213 | `na-atimaññetha` | Grammar `opt.3.sg refl` → `opt.refl.3.sg` (reviewer did not touch this row; B-11.2 does not apply) | A5.3 |
| 55-17 | 214 | `katthaci` | POS `adv` → `ind`; Grammar `` → `adv` | A5.10 |
| 55-18 | 215 |  | gloss `that, hiṃ` → `that, him` | A1 |
| 55-19 | 226 |  | `(throught)` → `(through)` | A6 |
| 55-20 | 232 |  | gloss `…unease, probleṃ` → `…unease, problem` (row also merged in Part 3) | A1 |
| 55-21 | 235 |  | `one to anothershould not wish` → `one to another should not wish` | A6 |
| 55-22 | 257 | `evam-` | Grammar ∅ → `adv` | B-P1 |
| 55-23 | 260 | `bhūtesu` | `masc.loc.sg` → `masc.loc.pl` — `-esu` plural | A4 |
| 55-24 | 280 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 55-25 | 284 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 |
| 55-26 | 292 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 55-27 | 319 | `yāvatā-` | Grammar ∅ → `adv` | B-P1 |
| 55-28 | 320 |  | gloss `to hiṃ` → `to him` | A1 |
| 55-29 | 339 | `āhu` | `pref.p.3.pl` → `perf.3.pl` — typo `pref.p` | A4 |
| 55-30 | 351 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 55-31 | 370 | `hi` | Grammar ∅ → `emph` | B-P3 |
| 55-32 | 371 | `jātu` | Grammar ∅ → `emph` | B-P3 |
| 55-33 | 374 | `puna-` | Grammar ∅ → `adv` | B-P1 |

## 56 — Khandha-Parittaṃ

`per-56-khandha-parittam.md` — 4 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 56-01 | 25 | `ca;` | Grammar ∅ → `conj` | B-P2 |
| 56-02 | 90 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 56-03 | 98 | `agamā` | POS `v.refl` → `verb`; Grammar `aor.3.sg` → `aor.3.sg.refl` | A5.9 |
| 56-04 | 149 | `sammā-` | Grammar ∅ → `adv` | B-P1 |

## 57 — Buddha-Dhamma-Saṅgha-Guṇā

`per-57-buddha-dhamma-sangha-guna.md` — 5 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 57-01 | 14 | `sammā-` | Grammar ∅ → `adv` | B-P1 |
| 57-02 | 43 | `paccattaṃ` | POS `adv` → `ind`; Grammar `ind` → `adv`  ✔ *Reviewer B proposes the same.* | A5.10 |
| 57-03 | 60 | `yadidaṃ` | POS `adv` → `ind`; Grammar `ind` → `adv` | A5.10 |
| 57-04 | 60 | `yadidaṃ` | ⚔ **same cells as the A5.10 row above — keep ONE:** **Option A (A5.10)** POS `adv` → `ind`, Grammar `ind` → `adv`  ·  **Option B (B-P7)** POS `adv` → `sandhi`, Grammar `ind` → ∅ (reviewer himself wrote `sandhi` in both POS and Grammar; I recommend Grammar empty)  ·  *Do not apply both.* | B-P7 |
| 57-05 | 61 | `cattāri` | `masc.nom.pl` → `nt.nom.pl` — same passage | A4 |

## 58 — Yaṅ Kiñci Ratanaṃ Loke

`per-58-yan-kinci-ratanam-loke.md` — 2 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 58-01 | 16 | `puthu` | Grammar ∅ → `adv` | B-P1 |
| 58-02 | 21 | `tasmā` | Grammar ∅ → `adv` | B-P1 |

## 59 — Bojjh'aṅga-Parittaṃ

`per-59-bojjhanga-parittam.md` — 18 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 59-01 | 15 | `tathā` | Grammar ∅ → `adv` | B-P1 |
| 59-02 | 20 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 59-03 | 21 | `tathā-` | Grammar ∅ → `adv` | B-P1 |
| 59-04 | 38 | `sammā-` | Grammar ∅ → `adv` | B-P1 |
| 59-05 | 45 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 59-06 | 48 |  | `which has been thoroughly told by the sage who understand` → `which have been thoroughly told by the sage who understands` | A6 |
| 59-07 | 56 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 |
| 59-08 | 58 | `te` | `masc.dat.sg` → `2.dat.sg` — same | A4 |
| 59-09 | 60 | `sabbadā` | Grammar ∅ → `adv` | B-P1 |
| 59-10 | 80 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 59-11 | 85 | `taṅ'khaṇe` | POS `ind` → `sandhi` (leave Grammar empty) | B-P7 |
| 59-12 | 97 | `ekadā` | Grammar ∅ → `adv` | B-P1 |
| 59-13 | 105 | `sādaraṃ` | Grammar ∅ → `adv` | B-P1 |
| 59-14 | 107 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 59-15 | 111 | `ṭhānaso` | Grammar ∅ → `adv` | B-P1 |
| 59-16 | 125 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 59-17 | 132 | `va` | Grammar ∅ → `emph` | B-P3 |
| 59-18 | 134 | `anuppatti-` | Rebuild row as `\| anuppatti- \| noun \| \| following attainment (of), after getting \|` — *POS cell held `masc`; compound member, Grammar stays ∅* | B-N20 |

## 60 — Abhaya-Parittaṃ

`per-60-abhaya-parittam.md` — *no suggestions from either review*

## 61 — Devatā-Uyyojana-Gāthā

`per-61-devata-uyyojana-gatha.md` — 8 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 61-01 | 11 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 61-02 | 14 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 61-03 | 17 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 61-04 | 30 | `ettāvatā` | Grammar ∅ → `adv` | B-P1 |
| 61-05 | 31 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 61-06 | 54 | `sabbadā` | Grammar ∅ → `adv` | B-P1 |
| 61-07 | 73 | `balaṃ` | Gr `nt` → `nt.acc.sg` — *grammar was only `nt`* | B-N73 |
| 61-08 | 78 | `sabbaso` | Grammar ∅ → `adv` | B-P1 |

## 62 — Jaya-Maṅgala-Aṭṭha-Gāthā

`per-62-jaya-mangala-attha-gatha.md` — 17 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 62-01 | 23 | `vidhinā` | Grammar ∅ → `adv` | B-P1 |
| 62-02 | 47 |  | Rebuild row: `\| akkhama- \| adj \| \| impatient (with), intolerant (of), not able to endure \|` | A3 |
| 62-03 | 52 | `vidhinā` | Grammar ∅ → `adv` | B-P1 |
| 62-04 | 79 | `vidhinā` | Grammar ∅ → `adv` | B-P1 |
| 62-05 | 100 |  | Rebuild row: `\| yojana- \| noun \| \| measure of length; approximately twenty kilometres \|` | A3 |
| 62-06 | 125 | `ciñcāya` | Grammar `fem.inst.sg` → `fem.ins.sg` | A5.2 |
| 62-07 | 127 | `vacanaṃ` | Gr `nt` → `nt.acc.sg` — *grammar was only `nt`* | B-N74 |
| 62-08 | 128 | `janakāya-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 62-09 | 129 | `majjhe` | Grammar ∅ → `adv` | B-P1 |
| 62-10 | 132 | `vidhinā` | Grammar ∅ → `adv` | B-P1 |
| 62-11 | 148 | `mati-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 62-12 | 151 |  | **D3** `<br>` inside table cells (lines 151). Policy: keep (note the exception) or convert `A<br>(or)<br>B` → `A (or) B`. | A8-D3 |
| 62-13 | 153 |  | Rebuild row: `\| abhiropita- \| adj \| \| put on top, placed, (of an argument) refuted, debunked, disproved \|` | A3 |
| 62-14 | 157 |  | Rebuild row: `\| paññā- \| noun \| \| wisdom, knowledge, intelligence, intellect, understanding, insight \|` | A3 |
| 62-15 | 184 | `vidhinā` | Grammar ∅ → `adv` | B-P1 |
| 62-16 | 211 | `vidhinā` | Grammar ∅ → `adv` | B-P1 |
| 62-17 | 236 |  | **D6** `sarate-m'` tagged opt.3.sg — form is middle present (`sarate`); suggest `pr.refl.3.sg`; verify. | A8-D6 |

## 63 — Jaya-Parittaṃ

`per-63-jaya-parittam.md` — 7 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 63-01 | 33 | `te` | `masc.dat.sg` → `2.dat.sg` — same | A4 |
| 63-02 | 46 | `sakyānaṃ` | `masc.gen.sg` → `masc.gen.pl` — `-ānaṃ` plural | A4 |
| 63-03 | 49 | `evaṃ` | Grammar ∅ → `adv` | B-P1 |
| 63-04 | 52 | `hohi` | `pr.2.sg` → `imp.2.sg` — imperative "may you be" | A4 |
| 63-05 | 53 | `jayassu` | POS `verbimp.reflx.2.s` → `verb`; Grammar `` → `imp.refl.2.sg` | A5.8 |
| 63-06 | 88 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 63-07 | 104 | `paṇīdhi` | Gr `fem` → `masc.nom.sg` — *DPD: paṇīdhi masc.* | B-N75 |

## 64 — Bhavatu-Sabba-Maṅgalaṃ

`per-64-bhavatu-sabba-mangalam.md` — 2 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 64-01 | 12 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 |
| 64-02 | 25 | `sadā` | Grammar ∅ → `adv` | B-P1 |

## 65 — Dhamma-Saṅgaṇī-Mātikā

`per-65-dhamma-sangani-matika.md` — 7 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 65-01 | 38 | `n'eva` | POS `ind` → `sandhi` (leave Grammar empty) | B-P7 |
| 65-02 | 46 |  | Rebuild row: `\| upādinna- \| pp \| \| grasped, clung to, attached to, taken as "mine", acquired \|` | A3 |
| 65-03 | 48 |  | Rebuild row: `\| anupādinna- \| pp \| \| not grasped, not clung to, not attached to, not taken as "mine", not acquired \|` | A3 |
| 65-04 | 62 |  | `dhammas neither defiled and subject to defilements` → `dhammas neither defiled nor subject to defilements` | A6 |
| 65-05 | 126 |  | `exhalted` → `exalted` *(same fix at: per-65:126, per-65:134)* | A6 |
| 65-06 | 134 |  | `exhalted` → `exalted` *(same fix at: per-65:126, per-65:134)* | A6 |
| 65-07 | 200 |  | `internal and external dhamams` → `internal and external dhammas` | A6 |

## 66 — Vipassanā-Bhūmi-Pāṭho

`per-66-vipassana-bhumi-patho.md` — 9 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 66-01 | 82 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 |
| 66-02 | 86 |  | `the I am knowing the unknown' faculty` → `the 'I am knowing the unknown' faculty` | A6 |
| 66-03 | 94 |  | Rebuild row: `\| dukkhaṃ \| noun \| nt.nom.sg \| discomfort, suffering, pain, unease, something unsatisfactory, problem, trouble \|` (embedded `nt.ac.s`; nominative in `idaṃ … dukkhaṃ`-type list — verify against the chant line above it) | A2 |
| 66-04 | 97 |  | Rebuild row: `\| dukkhanirodho \| noun \| masc.nom.sg \| cessation of suffering, disappearance of suffering \|` | A2 |
| 66-05 | 109 | `\>avijjā-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 66-06 | 110 | `\>paccayā` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |
| 66-07 | 145 |  | `becoming arise` → `becoming arises`; `birth arise` → `birth arises` *(same fix at: per-24:49, per-66:145)* | A6 |
| 66-08 | 166 | `tv'eva` | POS `ind` → `sandhi` (leave Grammar empty) | B-P7 |
| 66-09 | 167 | `asesa-virāga-nirodhā` | POS `m.abl.s` → `noun`; Grammar ∅ → `masc.abl.sg` (tag sits in POS column; `noun` is my inference — confirm) | A5.6 |

## 67 — Paṭṭhāna-Mātikā-Pāṭho

`per-67-patthana-matika-patho.md` — 1 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 67-01 | 32 |  | `there is not , there not exists` → `there is not, there does not exist` | A6 |

## 68 — Adāsi-Me Ādi Gāthā

`per-68-adasi-me-adi-gatha.md` — 12 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 68-01 | 16 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 68-02 | 21 | `pubbe` | Grammar ∅ → `adv` | B-P1 |
| 68-03 | 25 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 |
| 68-04 | 34 | `hi` | Grammar ∅ → `emph` | B-P3 |
| 68-05 | 45 |  | Rebuild row: `\| petānam- \| adj \| masc.gen.pl \| of departed, deceased, dead \|` | A2 |
| 68-06 | 47 | `evaṃ` | Grammar ∅ → `adv` | B-P1 |
| 68-07 | 58 | `kho` | Grammar ∅ → `emph` | B-P3 |
| 68-08 | 63 | `dīgharattaṃ` | Grammar ∅ → `adv` | B-P1 |
| 68-09 | 66 | `ṭhānaso` | Grammar ∅ → `adv` | B-P1 |
| 68-10 | 69 |  | `it is benefits immediately` → `it benefits immediately` | A6 |
| 68-11 | 77 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 68-12 | 82 | `ca` | Grammar ∅ → `conj` | B-P2 |

## 69 — Paṃsu-Kūla for the Dead

`per-69-pamsu-kula.md` — 8 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 69-01 | 11 | `vata` | Grammar ∅ → `excl` | B-P4 |
| 69-02 | 56 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 69-03 | 58 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 69-04 | 60 | `tatha'eva-` | POS `ind` → `sandhi` (leave Grammar empty) | B-P7 |
| 69-05 | 65 | `ettha` | Grammar ∅ → `adv` | B-P1 |
| 69-06 | 79 | `aciraṃ` | Grammar ∅ → `adv` | B-P1 |
| 69-07 | 80 | `vata-` | Grammar ∅ → `excl` | B-P4 |
| 69-08 | 89 | `va` | Grammar ∅ → `emph` | B-P3 |

## 70 — Sharing and Aspirations

`per-70-sharing-and-aspirations.md` — 24 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 70-01 | 28 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 70-02 | 30 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 70-03 | 45 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 70-04 | 55 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 70-05 | 56 |  | `Indras , kings` → `Indras, kings` | A6 |
| 70-06 | 57 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 70-07 | 59 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 70-08 | 71 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 70-09 | 75 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 70-10 | 89 | `me` | `masc.ins.sg` → `1.ins.sg` — personal pronoun | A4 |
| 70-11 | 99 | `dentu` | `pr.3.pl` → `imp.3.pl` — `-ntu` imperative ("may they give") | A4 |
| 70-12 | 115 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 70-13 | 123 | `khippaṃ-` | Grammar ∅ → `adv` | B-P1 |
| 70-14 | 125 | `sulabhe` | Grammar `imp.reflx.1.sg` → `imp.refl.1.sg` | A5.3 |
| 70-15 | 126 | `c'eva` | POS `ind` → `sandhi` (leave Grammar empty) | B-P7 |
| 70-16 | 141 | `yāva` | Grammar ∅ → `adv` | B-P1 |
| 70-17 | 152 | `sabbadā` | Grammar ∅ → `adv` | B-P1 |
| 70-18 | 153 | `yeva` | POS `ind` → `sandhi` (leave Grammar empty) | B-P7 |
| 70-19 | 154 | `yattha` | Grammar ∅ → `adv` | B-P1 |
| 70-20 | 157 | `bhave` | Grammar `imp.reflx.1.sg` → `imp.refl.1.sg` | A5.3 |
| 70-21 | 185 | `me` | `masc.gen.sg` → `1.gen.sg` — personal pronoun | A4 |
| 70-22 | 187 |  | `may Maras do not get a chance` → `may Māras not get a chance` (2×) *(same fix at: per-70:187, per-70:230)* | A6 |
| 70-23 | 210 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 70-24 | 230 |  | `may Maras do not get a chance` → `may Māras not get a chance` (2×) *(same fix at: per-70:187, per-70:230)* | A6 |

## 71 — Sharing of All Merits

`per-71-sharing-of-all-merits.md` — 10 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 71-01 | 15 | `idāni` | Grammar ∅ → `adv` | B-P1 |
| 71-02 | 22 | `bhāgino` | `masc.nom.p` → `masc.nom.pl` — truncated | A4 |
| 71-03 | 37 | `ca` | Grammar ∅ → `conj` | B-P2 |
| 71-04 | 69 |  | `Beings lives in the world` → `Beings live in the world` | A6 |
| 71-05 | 82 | `sayaṃ` | Grammar ∅ → `adv` | B-P1 |
| 71-06 | 90 |  | `sharing of merrit` → `sharing of merit` | A6 |
| 71-07 | 100 |  | Rebuild row: `\| anumodana- \| noun \| \| rejoicing, satisfaction, thanks, appreciation, blessing, thanksgiving \|` | A3 |
| 71-08 | 104 | `sadā` | Grammar ∅ → `adv` | B-P1 |
| 71-09 | 112 |  | **D6** `\| tesāsāṃ \| ? \| \| \|` — empty analysis. Likely `tesāsā` = `tesaṃ` + `āsā` ("their wishes"); verify against chant line and DPD (covers L112–113). | A8-D6 |
| 71-10 | 113 |  | **D6** `sijjhataṃ=sijjhanaṃ \| noun \| nt.acc.sg` should probably be `sijjhataṃ \| verb \| imp.3.sg (middle) \| may (they) succeed`; verify. | A8-D6 |

## 72 — Sharing of Merits with the Departed

`per-72-sharing-of-merits-with-the-departed.md` — 1 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 72-01 | 18 | `ñātinaṃ` | `nom.dat.pl` → `masc.dat.pl` — garbled case tag | A4 |

## 73 — Sharing of Merits with the Devas

`per-73-sharing-of-merits-with-the-devas.md` — 2 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 73-01 | 12 | `ettāvatā` | Grammar ∅ → `adv` | B-P1 |
| 73-02 | 13 | `ca` | Grammar ∅ → `conj` | B-P2 |

## 74 — The Highest Honour and Aspirations

`per-74-the-highest-honour-and-aspirations.md` — 6 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| 74-01 | 46 | `me` | `1.g.sg` → `1.gen.sg` — truncated | A4 |
| 74-02 | 57 | `yāva` | Grammar ∅ → `adv` | B-P1 |
| 74-03 | 61 |  | `a assembly` → `an assembly` | A6 |
| 74-04 | 69 | `kho` | Grammar ∅ → `emph` | B-P3 |
| 74-05 | 123 | `addhā` | Grammar ∅ → `excl` | B-P4 |
| 74-06 | 140 | `āsavakkhayā-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 |

## Word-by-word analysis of SBS Anumodana chants (Ṭhanuttamo)

`word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md` — 7 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| wbw-01 | 145 | `*paripūrenti*` | `vb. first pers. act. pl.` → `vb. third pers. act. pl.` — *`-enti` = 3rd pl.* | B-N136 |
| wbw-02 | 149 | `*sāgaraṁ*` | `m. n., nom. sg. object of main clause` → `m. n., acc. sg. object of main clause` — *`-ṁ` ending, object* | B-N137 |
| wbw-03 | 163 | `*upakappati*` | `vb. pres. ind. first pers. act. sg.` → `vb. pres. ind. third pers. act. sg.` — *`-ati` = 3rd sg.* | B-N138 |
| wbw-04 | 231 | `*te*` | `pers. pron. third pers. dat. sg.` → `pers. pron. second pers. dat. sg.` — *`te` = "for you"; (line 391 already says second pers.)* | B-N139 |
| wbw-05 | 443 | `*sukhassa*` | `m. n. gen. sg.` → `neutr. n. gen. sg.` — *`sukha` is neuter* | B-N140 |
| wbw-06 | 449 | `*sukhaṁ*` | `m. n. acc. sg.` → `neutr. n. acc. sg.` — *`sukha` is neuter* | B-N141 |
| wbw-07 | 627 | `*sabbe*` | `second pers. adj. pron. nom. pl.` → `adj. pron. nom. pl.` — *`sabbe` = "all", not a personal pronoun* | B-N142 |

## Post Pātimokkha

`post-patimokkha.md` — 3 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| post-01 | 9 | `handa` | Grammar ∅ → `excl` | B-P4 |
| post-02 | 19 | `karomase` | Grammar `ref.imp.1.pl` → `imp.refl.1.pl` | A5.3 |
| post-03 | 27 | `namo` | Grammar ∅ → `excl` | B-P4 |

## Pubbakicca analysis

`pubbakicca-analysis.md` — 74 suggestion(s)

| ID | Line | Word | Suggestion | Source |
|---|---|---|---|---|
| pubbakicca-01 | 10 | `me` | Grammar `1st.acc.sg` → `1.acc.sg` | A5.1 |
| pubbakicca-02 | 13 | `detu` | Grammar `imp.3rd.sg` → `imp.3.sg` | A5.1 |
| pubbakicca-03 | 24 | `karomi` | Grammar `pr.1st.sg` → `pr.1.sg` | A5.1 |
| pubbakicca-04 | 41 | `hoti` | Grammar `pr.3rd.sg` → `pr.3.sg` | A5.1 |
| pubbakicca-05 | 50 | `\#taṃ` | Grammar `nt.` → `nt` | A5.7 |
| pubbakicca-06 | 51 | `\#ṭhāna` | Grammar `nt.` → `nt` | A5.7 |
| pubbakicca-07 | 56 | `\#padīpa` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-08 | 60 | `\#āsana` | Grammar `nt.` → `nt` | A5.7 |
| pubbakicca-09 | 64 | `\#pānīya` | Grammar `nt.` → `nt` | A5.7 |
| pubbakicca-10 | 65 | `\#paribhojanīya` | Grammar `nt.` → `nt` | A5.7 |
| pubbakicca-11 | 84 | `\#akata` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-12 | 120 | `\#padīpa` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-13 | 127 | `n'atthi` | Grammar `pr.3rd.sg` → `pr.3.sg` | A5.1 |
| pubbakicca-14 | 130 | `bhikkhūnaṃ` | `masc.gen.sg` → `masc.gen.pl` — `-ūnaṃ` plural | A4 |
| pubbakicca-15 | 132 | `jānantehi` | Grammar `masc.instr.pl` → `masc.ins.pl` | A5.2 |
| pubbakicca-16 | 133 | `bhikkhūhi` | Grammar `masc.instr.pl` → `masc.ins.pl` | A5.2 |
| pubbakicca-17 | 136 | `honti` | Grammar `pr.3rd.pl` → `pr.3.pl` | A5.1 |
| pubbakicca-18 | 143 | `chand'āharaṇa` | Grammar `nt.` → `nt` | A5.7 |
| pubbakicca-19 | 145 | `\#chanda` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-20 | 146 | `\#āharaṇa` | Grammar `nt.` → `nt` | A5.7 |
| pubbakicca-21 | 148 | `\#pārisuddhi` | Grammar `fem.` → `fem` | A5.7 |
| pubbakicca-22 | 158 | `n'atthi` | Grammar `pr.3rd.sg` → `pr.3.sg` | A5.1 |
| pubbakicca-23 | 193 | `\#hemanta` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-24 | 194 | `\#gimha` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-25 | 195 | `\#vassāna` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-26 | 198 | `honti` | Grammar `pr.3rd.pl` → `pr.3.pl` | A5.1 |
| pubbakicca-27 | 222 | `iminā` | Grammar `masc.instr.sg` → `masc.ins.sg` | A5.2 |
| pubbakicca-28 | 223 | `pakkhena` | Grammar `masc.instr.sg` → `masc.ins.sg` | A5.2 |
| pubbakicca-29 | 232 |  | **D6** `\| attha \| card \| x.nom.pl \| eight \|` — Pāḷi typo for `aṭṭha`? Verify against chant line before touching Pāḷi text. | A8-D6 |
| pubbakicca-30 | 244 | `sabbehi` | Grammar `masc.instr.pl` → `masc.ins.pl` | A5.2 |
| pubbakicca-31 | 245 | `āyasmantehi` | Grammar `masc.instr.pl` → `masc.ins.pl` | A5.2 |
| pubbakicca-32 | 258 | `\#bhikkhu` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-33 | 263 | `\#uposatha` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-34 | 283 | `\#uposatha` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-35 | 288 | `honti` | Grammar `pr.3rd.pl` → `pr.3.pl` | A5.1 |
| pubbakicca-36 | 295 | `sabbehi` | Grammar `masc.instr.pl` → `masc.ins.pl` | A5.2 |
| pubbakicca-37 | 296 | `āyasmantehi` | Grammar `masc.instr.pl` → `masc.ins.pl` | A5.2 |
| pubbakicca-38 | 299 | `\#\#bhikkhu` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-39 | 315 | `n'atthi` | Grammar `pr.3rd.sg` → `pr.3.sg` | A5.1 |
| pubbakicca-40 | 326 | `\#karaṇa` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-41 | 329 | `\#pubba` | Grammar `nt.` → `nt` | A5.7 |
| pubbakicca-42 | 333 | `\#nikkaraṇa` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-43 | 335 | `\#\#karaṇa` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-44 | 345 | `\#pubba` | Grammar `nt.` → `nt` | A5.7 |
| pubbakicca-45 | 348 | `hoti` | Grammar `pr.3rd.sg` → `pr.3.sg` | A5.1 |
| pubbakicca-46 | 370 |  | **D3** `<br>` inside table cells (lines 370, 376). Policy: keep (note the exception) or convert `A<br>(or)<br>B` → `A (or) B`. | A8-D3 |
| pubbakicca-47 | 390 | `\#saṅgha` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-48 | 391 | `\#uposatha` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-49 | 401 | `saṅghena` | Grammar `masc.instr.sg` → `masc.ins.sg` | A5.2 |
| pubbakicca-50 | 431 | `\#vikāla` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-51 | 432 | `\#bhojana` | Grammar `nt.` → `nt` | A5.7 |
| pubbakicca-52 | 437 | `\#sabhāga` | Grammar `fem.` → `fem` | A5.7 |
| pubbakicca-53 | 441 | `vijjanti` | Grammar `pr.pass.3rd.pl` → `pr.pass.3.pl` | A5.1 |
| pubbakicca-54 | 456 | `\#karaṇa` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-55 | 461 | `\#vajjanīya` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-56 | 464 | `n'atthi` | Grammar `pr.3rd.sg` → `pr.3.sg` | A5.1 |
| pubbakicca-57 | 478 | `imehi` | Grammar `nt.instr.pl` → `nt.ins.pl` | A5.2 |
| pubbakicca-58 | 479 | `catūhi` | Grammar `nt.instr.pl` → `nt.ins.pl` | A5.2 |
| pubbakicca-59 | 480 | `lakkhaṇehi` | Grammar `nt.instr.pl` → `nt.ins.pl` | A5.2 |
| pubbakicca-60 | 482 | `pattakallaṃ` | Grammar `nt.` → `nt` | A5.7 |
| pubbakicca-61 | 483 | `\#patta` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-62 | 486 | `hoti` | Grammar `pr.3rd.sg` → `pr.3.sg` | A5.1 |
| pubbakicca-63 | 489 | `\#yutta` | Grammar `nt.` → `nt` | A5.7 |
| pubbakicca-64 | 499 | `\#uposatha` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-65 | 502 | `\#patta` | Grammar `nt.` → `nt` | A5.7 |
| pubbakicca-66 | 508 | `saṅghena` | Grammar `masc.instr.sg` → `masc.ins.sg` | A5.2 |
| pubbakicca-67 | 518 | `pubbakaraṇa` | Grammar `nt.` → `nt` | A5.7 |
| pubbakicca-68 | 519 | `\#pubba` | Grammar `nt.` → `nt` | A5.7 |
| pubbakicca-69 | 520 | `\#karaṇa` | Grammar `nt.` → `nt` | A5.7 |
| pubbakicca-70 | 522 | `\#pubba` | Grammar `nt.` → `nt` | A5.7 |
| pubbakicca-71 | 528 | `\#bhikkhu` | Grammar `masc.` → `masc` | A5.7 |
| pubbakicca-72 | 530 | `anumatiyā` | Grammar `fem.instr.sg` → `fem.ins.sg` | A5.2 |
| pubbakicca-73 | 534 | `karomi` | Grammar `pr.1st.sg` → `pr.1.sg` | A5.1 |
| pubbakicca-74 | 537 |  | **D7** No footer nav (no `[index]` link) and not referenced from `docs/6-pali-class/sbs-per-analysis.md` (post-patimokkha.md is, at index line 114). Recommend: add a footer index link and an index entry. | A8-D7 |
