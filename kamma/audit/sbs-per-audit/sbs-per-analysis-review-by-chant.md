# SBS Pāḷi–English chant analysis — merged review, in reading order

Date: 2026-11-09. Source of every suggestion: (1) the original audit `kamma/archive/audit/sbs-per-analysis-audit.md` Parts 1–8 (**A**), (2) the second review found in `temp/Chanting Book Analaysis*` (**B**, "Reviewer B"; the two folders are identical). Rebuilt here **per chant, in line order**, so that everything about one chant is read in one place. Line numbers refer to the current files in `docs/6-pali-class/sbs-per-analysis/` (unchanged since the audit; match on the quoted text, not the line number alone).

## How to use

1. **Policies first** (next section): each policy affects many rows. Delete the policy line you reject, or for an A/B policy pair keep one. Rows belonging to a policy carry its tag in the *Source* column.
2. **Then read chant by chant.** Delete any row you disagree with. Rows marked ⚔ are conflicts: delete the option you do not want from inside the row (or the whole row to reject both). Rows marked ✗ are my recommended rejections of Reviewer B suggestions — they are kept so nothing is lost, and are **not** implemented unless you delete the ✗ mark.
3. Hand the file to an implementing agent. **Agent rules:** match on quoted current text and grep before every edit; stop and report on mismatch; never change Pāḷi chant lines unless a row says so explicitly; implement nothing from a policy whose line was deleted; where two rows touch the same cell, the specific row beats the bulk-policy row; never implement a ✗ or ⚑ row; if a ⚔ row still lists both options, stop and ask. **The `Re-check` cell overrides the original suggestion:** a `drop` row is not implemented, an `adjust` row uses the re-check replacement, an `undecided` row waits for the owner, `gone` and `keep` leave the original suggestion as it stands. Rows in the Fresh look section follow the same rules; there, Conf. below 8 means "check before changing".

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

| Policy | From | Rule | Rows | Re-check |
|---|---|---|---| --- |
| **A5.1** | Audit 5.1 | `1st`/`2nd`/`3rd` → `1`/`2`/`3` in Grammar | 19 | undecided |
| **A5.2** | Audit 5.2 | `instr`/`inst` → `ins` | 20 | undecided |
| **A5.3** | Audit 5.3 | reflexive notation → `refl`, mood first (`imp.refl.1.pl`). **Pair with B-11.2 — keep one.** | 14 | undecided |
| **A5.4** | Audit 5.4 | `emphat`/`emph.`/`emp` → `emph` | 1 | undecided |
| **A5.5** | Audit 5.5 | `pres` → `pr` | 0 | undecided |
| **A5.6** | Audit 5.6 | compressed one-letter tags (`m.n.s`, `nt.i.sg` …) → full form | 14 | undecided |
| **A5.7** | Audit 5.7 | strip trailing periods in tags (bare `masc.`→`masc`; **keeps** bare gender on compound members — pair with B-11.3) | 50 | undecided |
| **A5.8** | Audit 5.8 | composite POS (`verbinf`, `verbaor.1.s`, …) → POS + Grammar | 3 | undecided |
| **A5.9** | Audit 5.9 | `v.pass`/`v.caus`/`v.refl`/`prp.caus` → `verb`/`prp` + tag in Grammar | 12 | undecided |
| **A5.10** | Audit 5.10 | `neg`/`conj`/`interr`/`prep`/`adv` in the POS column → POS `ind`, word moved to Grammar. *Caveat: the audit text also lists `card`; I did not compute `card` rows because audit D4 and B-P8 want POS `card` — confirm.* | 9 | undecided |
| **A5.11** | Audit 5.11 | `from loc.sg` → `adv`; `from ger` → `ger` | 1 | undecided |
| **A5.12** | Audit 5.12 | `fem nom pl` → `fem.nom.pl` | 1 | undecided |
| **D3** | Audit D3 | `<br>` inside tables: keep (document exception) or convert `A<br>(or)<br>B` → `A (or) B` | 6 | undecided |
| **D4** | Audit D4 | unify composite POS values (`pp as adj`, `adj (as noun)`, `v + pn`, …) — **decision needed which form**; Reviewer B's rows (B-N…) already propose one form for the `pp as adj` / `adj (as noun)` family | 21 | undecided |
| **D5** | Audit D5 | unbold Pāḷi chant lines that are bolded like translations | 19 | undecided |
| **D8** | Audit D8 | quote-style sweep (straight apostrophes, balanced pairs) | 22 | undecided |
| **B11.2** | Reviewer B 11.2 | **drop `refl`** (`imp.1.pl`) — *alternative to A5.3, keep one* | 7 | undecided |
| **B11.3** | Reviewer B 11.3 | **blank** Grammar of compound members (`word-`) that carry a bare gender — *alternative to the A5.7 keep-bare-gender stance; 531 of ~700 compound rows are already empty* | 34 | undecided |
| **B11.4** | Reviewer B 11.4 | POS `ger`/`abs` with empty Grammar instead of `verb`+`ger`/`abs` — *alternative to the corpus convention (130 rows keep `verb`); if chosen, extend to all rows* | 20 | undecided |
| **BP1** | Reviewer B P1 | `ind` rows: Grammar ∅ → `adv` (DPD sub-type) | 128 | undecided |
| **BP2** | Reviewer B P2 | `ca` etc: Grammar ∅ → `conj` | 114 | undecided |
| **BP3** | Reviewer B P3 | Grammar ∅ → `emph` | 46 | undecided |
| **BP4** | Reviewer B P4 | Grammar ∅ → `excl` (`handa`, `namo`, `vata`, `addhā`) | 21 | undecided |
| **BP5** | Reviewer B P5 | Grammar ∅ → `prep` | 5 | undecided |
| **BP6** | Reviewer B P6 | Grammar ∅ → `interr` | 8 | undecided |
| **BP7** | Reviewer B P7 | POS `ind` → `sandhi` for fused words (`kiñcāpi`, `yadidaṃ`, `n'eva` …); leave Grammar empty | 17 | undecided |
| **BP8** | Reviewer B P8 | numerals POS `adj` → `card` | 5 | undecided |

Note: P-tagged rows of the **BP** policies are written in the tables with source `B-Pn`; the **A5.n** rows with source `A5.n`.

---

## 01 — Dedication of Offerings

`per-01-dedication-of-offerings.md` — 22 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 01-01 | 11 |  | `Fortunate One the Buddha` → `Fortunate One, the Buddha` *(same fix at: per-01:11, per-01:76)* | A6 | keep (9) |
| 01-02 | 13 |  | `totally perfectly` → `totally, perfectly` *(same fix at: per-01:13, per-01:126)* | A6 | keep (9) |
| 01-03 | 13 | `sammā-` | Grammar ∅ → `adv` | B-P1 | keep (8) |
| 01-04 | 14 | `sambuddho` | Eng `one who has thoroughly understood, being enlightened, a Buddha, fully awakened one` → `one who has thoroughly understood, being enlightened, a Buddha` — *drops `, fully awakened one` from the gloss — loses information; consider keeping the long form* | B-N124 | drop: no error. B-N124 only removes the valid gloss `fully awakened one`, which loses information; DPD sambuddha 1 (masc, "Awakened One; Buddha; who is wide awake; who has completely understood") supports the full sense, and the old reviewer also advised keeping the long form. |
| 01-05 | 46 | `mayaṃ` | `1.nom.` → `1.nom.pl` — number missing  ✔ *Reviewer B proposes the same.* | A4 | keep (10) |
| 01-06 | 48 | `sa-` | POS `pron` → `prefix`; Eng `one's own, his own OR with` → `with, accompanied by` — *`sa-` as prefix = "with"* | B-N83 | keep (8) — DPD sa 5.1: prefix, abbreviation of saha, "with; having" |
| 01-07 | 50 | `sa-` | POS `pron` → `prefix`; Eng `one's own, his own OR with` → `with, accompanied by` — *same as 01:48* | B-N84 | keep (8) — DPD sa 5.1: prefix "with" (same as 76) |
| 01-08 | 73 | `sādhu` | Gr ∅ → `excl`; Eng `it is good, would be good, please` → `it is good (for); it would be good (if)` | B-N76 | keep (9) |
| 01-09 | 76 |  | `Fortunate One the Buddha` → `Fortunate One, the Buddha` *(same fix at: per-01:11, per-01:76)* | A6 | keep (9) |
| 01-10 | 77 |  | **D3** `<br>` inside table cells (lines 77). Policy: keep (note the exception) or convert `A<br>(or)<br>B` → `A (or) B`. | A8-D3 | undecided — owner decision D3: whether to keep `<br>` in table cells. The `<br>` is still at per-01:77 (mech `gone` is a false negative). |
| 01-11 | 77 | `sucira- (or) suciraṃ` | POS `adj` → `ind` (leave Grammar empty) — *reviewer also wrote `ind` into Grammar (duplicate; see X1) — only the POS change is proposed here* | B-N85 | drop: DPD has `sucira` as adj (in comps), which is the reading in the chant compound `sucira-parinibbuto`. `ind` fits only the alternative `suciraṃ`, so changing the whole cell to `ind` would be wrong. |
| 01-12 | 78 |  | `who's fire is out` → `whose fire is out` *(same fix at: per-01:78, per-06:470)* | A6 | keep (10) |
| 01-13 | 79 | `api` | ⚔ **C1 — keep ONE:** **Option A (audit)** Part 5.4: Grammar `emphat` → `emph`  ·  **Option B (reviewer)** Grammar `emphat` → ∅ (empty)  ·  *DPD lists `api` as plain `ind`.* | B-C1 | undecided |
| 01-14 | 88 |  | `latest , later` → `latest, later` | A6 | keep (10) |
| 01-15 | 91 | `mānasā` | Grammar `nt.abl/instr.sg` → `nt.abl/ins.sg` | A5.2 | drop: superseded by 86 (same cell). DPD mānasa 1 is adj in comps, so the cell needs a full tag change, not only `instr` → `ins`. |
| 01-16 | 91 | `mānasā` | Gr `nt.abl/instr.sg` → `nt.ins.sg`; Eng `from (with) a mind, intention` → `with a mind, intention` — *extends audit Part 5.2* | B-N21 | adjust: per-01:91 `\| mānasā \| noun \| nt.abl/instr.sg \| from (with) a mind, intention \|` → `\| mānasā \| adj \| masc.nom.sg \| having a mind, intention \|`. DPD mānasa 1 is adj in comps ("of such mind; having such intention"); the bahubbīhi `pacchimā-janatānukampa-mānasā` agrees with `bhagavā`, as the translation "having a mind full of compassion" shows. DPD silent on the form `mānasā`. (6) |
| 01-17 | 102 | `paṇṇākāra-` | Gr ∅ → `masc` — *adds bare gender — contradicts policy 11.3 (B)* | B-N22 | undecided — owner decision: bare gender on compound members (A5.7 keeps it, B11.3 blanks it). If the gender is kept, DPD confirms `paṇṇākāra` is masc. |
| 01-18 | 126 |  | `totally perfectly` → `totally, perfectly` *(same fix at: per-01:13, per-01:126)* | A6 | keep (9) |
| 01-19 | 126 | `sammā-` | Grammar `adv.` → `adv`  ✔ *Reviewer B proposes the same.* | A5.7 | keep (9) |
| 01-20 | 146 | `svākkhāto` | POS `pp as adj` — unify to one form (see policy D4) | A8-D4 | drop: duplicate of 91 (same cell; 91 gives the concrete fix). |
| 01-21 | 146 | `svākkhāto` | POS `pp as adj` → `adj` — *D4: unify `pp as adj`* | B-N86 | undecided — owner decision D4: one form for `pp as adj` (B proposes `adj`). DPD svākkhāta is adj, which supports B's form. |
| 01-22 | 159 |  | `I venerate to the Teaching.` → `I venerate the Teaching.`  ✔ *Reviewer B proposes the same.* | A6 | keep (10) |

## 02 — Preliminary Homage

`per-02-preliminary-homage.md` — 7 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 02-01 | 9 | `handa` | Grammar ∅ → `excl` | B-P4 | keep (9) |
| 02-02 | 13 | `pubbabhāga-` | POS `adj` → `noun` | B-N87 | keep (9) |
| 02-03 | 16 | `namakāraṃ` | Gr `nt.acc.sg` → `masc.acc.sg` — *DPD: kāra masc.* | B-N23 | keep (9) — DPD namakkāra: masc, comp; kāra 1: masc |
| 02-04 | 18 | `\>kāraṃ` | Gr `nt.acc.sg` → `masc.acc.sg` — *DPD: kāra masc.* | B-N24 | keep (9) — DPD kāra 1: masc |
| 02-05 | 19 | `karomase` | Grammar `ref.imp.1.pl` → `imp.refl.1.pl` | A5.3 | undecided — owner decision: A5.3 (`imp.refl.1.pl`) or B11.2 (`imp.1.pl`). DPD gives `karomase` as "imp, reflx 1st pl", which supports keeping refl. |
| 02-06 | 19 | `karomase` | Grammar `ref.imp.1.pl` → `imp.1.pl` (reviewer drops `refl`; audit 5.3 keeps it: `imp.refl.1.pl`) — policy 11.2 | B-11.2 | undecided — same A5.3/B11.2 pair as 104. DPD marks `karomase` as reflx. |
| 02-07 | 27 | `namo` | Grammar ∅ → `excl` | B-P4 | keep (9) |

## 03 — Homage to the Buddha

`per-03-homage-to-the-buddha.md` — 14 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 03-01 | 9 | `handa` | Grammar ∅ → `excl` | B-P4 | keep (9) |
| 03-02 | 13 | `karomase` | Grammar `ref.pr.1.pl` → `imp.refl.1.pl` | A5.3 | undecided — A5.3/B11.2 choice on `refl`. Either way, per-03:13 must change `pr` → `imp` (DPD: imp, reflx 1st pl). |
| 03-03 | 13 | `karomase` | Grammar `ref.pr.1.pl` → `imp.1.pl` (reviewer drops `refl`; audit 5.3 keeps it: `imp.refl.1.pl`) — policy 11.2 | B-11.2 | undecided — same A5.3/B11.2 pair as 115. The `pr` → `imp` change applies either way. |
| 03-04 | 25 | `sammā-` | Grammar ∅ → `adv` | B-P1 | keep (8) |
| 03-05 | 46 | `bhagavā` | POS `adj` → `noun`; Eng `fortunate, illustrious, sublime, blessed, happy glorious, auspicious` → `Sublime One, Blessed One, Fortunate One` — *DPD: bhagavant 1 = masc noun* | B-N88 | keep (9) |
| 03-06 | 71 | `abhiññā` | POS `verb` → `ger`, Grammar `ger` → ∅ (reviewer; audit/corpus keep `verb` + `ger`) — policy 11.4 | B-11.4 | undecided — owner decision B11.4: POS `ger` with empty Grammar, or the corpus form `verb` + `ger`. DPD: abhiññā 3 is ger. |
| 03-07 | 72 | `sacchikatvā` | POS `verb` → `abs`, Grammar `abs` → ∅ (reviewer; audit/corpus keep `verb` + `abs`) — policy 11.4 | B-11.4 | undecided — owner decision B11.4 (as 119). DPD: sacchikatvā is abs. |
| 03-08 | 75 |  | `himself  higher understanding` → `himself higher understanding` (double space) | A6 | keep (10) |
| 03-09 | 90 |  | Pāḷi chant text: `sātthaṃ sabyañjaṇaṃ kevala-paripuṇṇaṃ …` → `sabyañjaṇaṃ` → `sabyañjanaṃ` — headword row per-03:95 is already `sabyañjanaṃ`; DPD spelling  *(decision; data-preservation rule)* | B-Q1 | keep (8) — DPD sabyañjana (and the idiom `sātthaṃ sabyañjanaṃ`) is spelt with dental n; the chant-line change still needs owner sign-off (data preservation) |
| 03-10 | 94 | `sātthaṃ` | Gr `masc.acc.sg` → `nt.acc.sg` — *agrees with neuter `brahmacariyaṃ` (also next 3 rows)* | B-N25 | keep (9) — DPD sātthaṃ sabyañjanaṃ: idiom, adj + adj |
| 03-11 | 95 | `sabyañjanaṃ` | Gr `masc.acc.sg` → `nt.acc.sg` — *same* | B-N26 | keep (9) — DPD sabyañjana: adj |
| 03-12 | 97 | `paripuṇṇaṃ` | Gr `masc.acc.sg` → `nt.acc.sg` — *same* | B-N27 | keep (9) — DPD paripuṇṇa: pp |
| 03-13 | 98 | `parisuddhaṃ` | Gr `masc.acc.sg` → `nt.acc.sg` — *same* | B-N28 | keep (9) — DPD parisuddha: pp (the gender fix stands; POS `adj` vs DPD `pp` not judged) |
| 03-14 | 119 |  | `my head  to` → `my head to` | A6 | keep (10) |

## 04 — Homage to the Dhamma

`per-04-homage-to-the-dhamma.md` — 4 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 04-01 | 9 | `handa` | Grammar ∅ → `excl` | B-P4 | keep (9) |
| 04-02 | 13 | `karomase` | Grammar `imp.ref.pr.1.pl` → `imp.refl.1.pl` | A5.3 | undecided — owner decision A5.3/B11.2 (DPD: imp, reflx 1st pl). |
| 04-03 | 13 | `karomase` | Grammar `imp.ref.pr.1.pl` → `imp.1.pl` (reviewer drops `refl`; audit 5.3 keeps it: `imp.refl.1.pl`) — policy 11.2 | B-11.2 | undecided — same pair as 136. |
| 04-04 | 37 | `paccattaṃ` | POS `adv` → `ind`; Grammar `ind` → `adv`  ✔ *Reviewer B proposes the same.* | A5.10 | keep (9) |

## 05 — Homage to the Saṅgha

`per-05-homage-to-the-sangha.md` — 10 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 05-01 | 9 | `handa` | Grammar ∅ → `excl` | B-P4 | keep (9) |
| 05-02 | 13 | `karomase` | Grammar `imp.ref.pr.1.pl` → `imp.refl.1.pl` | A5.3 | undecided — owner decision A5.3/B11.2 (DPD: imp, reflx 1st pl). |
| 05-03 | 13 | `karomase` | Grammar `imp.ref.pr.1.pl` → `imp.1.pl` (reviewer drops `refl`; audit 5.3 keeps it: `imp.refl.1.pl`) — policy 11.2 | B-11.2 | undecided — same pair as 147. |
| 05-04 | 58 | `yadidaṃ` | POS `adv` → `ind`; Grammar `ind` → `adv` | A5.10 | adjust: per-05:58 `\| yadidaṃ \| adv \| ind \|` → `\| yadidaṃ \| sandhi \| \|`. DPD gives yadidaṃ as sandhi (yad + idaṃ), so `ind` + `adv` is wrong. This is the same as BP7. (8) |
| 05-05 | 58 | `yadidaṃ` | ⚔ **same cells as the A5.10 row above — keep ONE:** **Option A (A5.10)** POS `adv` → `ind`, Grammar `ind` → `adv`  ·  **Option B (B-P7)** POS `adv` → `sandhi`, Grammar `ind` → ∅ (reviewer himself wrote `sandhi` in both POS and Grammar; I recommend Grammar empty)  ·  *Do not apply both.* | B-P7 | undecided |
| 05-06 | 59 | `cattāri` | `masc.nom.pl` → `nt.nom.pl` — agrees with neuter `purisayugāni` | A4 | keep (10) |
| 05-07 | 59 | `cattāri` | POS `adj` → `card` | B-P8 | keep (9) |
| 05-08 | 61 | `aṭṭha` | POS `adj` → `card` | B-P8 | keep (9) |
| 05-09 | 76 |  | Pāḷi chant text: `āhuṇeyyo pāhuṇeyyo dakkhiṇeyyo …` → `āhuneyyo pāhuneyyo` — headword rows per-05:80/81 and per-57:68/69 already `āhuneyyo`/`pāhuneyyo`; per-57 chant line was not flagged  *(decision; data-preservation rule)* | B-Q2 | keep (8) — DPD headwords āhuneyya, pāhuneyya (dental n); the chant-line change still needs owner sign-off (data preservation) |
| 05-10 | 100 | `ahaṃ` | Eng `i` → `I` — *capital I* | B-N125 | keep (10) |

## 06 — Salutation to The Triple Gem

`per-06-salutation-to-the-triple-gem.md` — 47 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 06-01 | 9 | `handa` | Grammar ∅ → `excl` | B-P4 | keep (9) |
| 06-02 | 11 | `ratanattaya-` | Grammar `nt.` → `nt` | A5.7 | undecided — owner decision on bare gender on compound members (A5.7 `nt` or B11.3 blank). DPD: ratanattaya is nt. |
| 06-03 | 12 | `paṇāma-` | Grammar `masc.` → `masc` | A5.7 | undecided — same compound-member gender decision as 164. DPD: paṇāma is masc. |
| 06-04 | 14 | `ceva` | ⚔ **C12 — keep ONE:** **Option A (audit)** Part 1: POS `idioṃ` → `idiom`  ·  **Option B (reviewer)** POS `idioṃ` → `sandhi`  ·  *Also affects every other `idioṃ` row if B is taken as a principle (see Part 14 P7).* | B-C12 | undecided |
| 06-05 | 15 | `saṃvega-` | Grammar `masc.` → `masc` | A5.7 | undecided — same compound-member gender decision as 164. DPD: saṃvega is masc. |
| 06-06 | 18 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 06-07 | 19 | `bhaṇāmase` | Grammar `imp.reflx.1.pl` → `imp.refl.1.pl` | A5.3 | undecided — owner decision A5.3/B11.2. DPD gives `bhaṇāmase` as "imp, reflx 1st pl", using DPD's own label `reflx`. |
| 06-08 | 19 | `bhaṇāmase` | Grammar `imp.reflx.1.pl` → `imp.1.pl` (reviewer drops `refl`; audit 5.3 keeps it: `imp.refl.1.pl`) — policy 11.2 | B-11.2 | undecided — same pair as 169. |
| 06-09 | 100 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1/2.2: ind, conj |
| 06-10 | 140 |  | `those who seen the peace` → `those who have seen the peace` | A6 | keep (10) |
| 06-11 | 146 |  | **D3** `<br>` inside table cells (lines 146, 175). Policy: keep (note the exception) or convert `A<br>(or)<br>B` → `A (or) B`. | A8-D3 | undecided — owner decision D3 on `<br>` in table cells. `<br>` is still at per-06:146 and 175 (mech `gone` is a false negative). |
| 06-12 | 158 |  | Rebuild row: `\| saṅghaṃ \| noun \| masc.acc.sg \| Community, assembly \|` | A2 | keep (10) |
| 06-13 | 169 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 | keep (8) |
| 06-14 | 174 | `evaṃ-` | Grammar ∅ → `adv` | B-P1 | keep (8) |
| 06-15 | 177 | `vatthu-ttayaṃ` | Gr `masc.acc.sg` → `nt.acc.sg` — *`vatthu` neuter* | B-N29 | keep (9) — DPD vatthuttaya: nt, comp |
| 06-16 | 178 | `vandayatā` | Grammar `masc.instr.sg.` → `masc.ins.sg` | A5.2/7 | drop: superseded by 06-17 (same cell) — its fixes already include Grammar `masc.instr.sg.` → `masc.ins.sg`; implement 06-16 only if 06-17 is rejected — DPD silent: vandayant (7) |
| 06-17 | 178 | `vandayatā` | POS `pp` → `prp`; Gr `masc.instr.sg.` → `masc.ins.sg`; Eng `by respected; revered; honoured` → `by one venerating, paying respect` — *extends audit Part 5.2 (`instr` → `ins`)* | B-N89 | keep (6) — DPD silent: vandayant |
| 06-18 | 186 | `abhisaṅkhataṃ` | Gr `masc.acc.sg` → `nt.acc.sg` — *agrees with neuter `vatthuttayaṃ`* | B-N30 | keep (9) — DPD abhisaṅkhata: pp; it agrees with nt vatthuttaya |
| 06-19 | 188 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 | keep (8) |
| 06-20 | 194 | `yaṃ` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 06-21 | 199 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 | keep (8) |
| 06-22 | 205 | `ve` | Grammar ∅ → `emph` | B-P3 | keep (9) — DPD ve: ind, emph |
| 06-23 | 221 | `sammā-` | Grammar ∅ → `adv` | B-P1 | keep (8) |
| 06-24 | 231 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 06-25 | 249 | `evaṃ` | Grammar ∅ → `adv` | B-P1 | keep (8) |
| 06-26 | 250 | `jānāma` | `pr.3.pl` → `pr.1.pl` — "we know" is 1st person  ✔ *Reviewer B proposes the same.* | A4 | keep (9) — DPD jānāti: pr; `-ma` is 1st pl |
| 06-27 | 258 | `jāti` | Grammar `f.n.sg` → `fem.nom.sg` | A5.6 | keep (9) |
| 06-28 | 269 |  | Rebuild row: `\| dukkha- \| noun \| \| discomfort, suffering, pain, unease, something unsatisfactory, problem, trouble \|` | A3 | keep (10) |
| 06-29 | 301 | `yam-(p)-icchaṃ` | POS `m.ac.s` → `noun`; Grammar ∅ → `masc.acc.sg` (tag sits in POS column; `noun` is my inference — confirm) | A5.6 | adjust: per-06:301 `\| yam-(p)-icchaṃ \| m.ac.s \| \|` → `\| yam-(p)-icchaṃ \| sandhi \| \|`. It is a fused form (yaṃ + pi + icchaṃ) with its parts on 302–303, not a noun. (6) |
| 06-30 | 329 | `upādānakkhandho` | POS `m.n.s` → `noun`; Grammar ∅ → `masc.nom.sg` (tag sits in POS column; `noun` is my inference — confirm) | A5.6 | keep (9) — DPD upādānakkhandha: masc, comp |
| 06-31 | 331 | `upādānakkhandho` | POS `m.n.s` → `noun`; Grammar ∅ → `masc.nom.sg` (tag sits in POS column; `noun` is my inference — confirm) | A5.6 | keep (9) — DPD upādānakkhandha: masc, comp |
| 06-32 | 333 | `upādānakkhandho` | POS `m.n.s` → `noun`; Grammar ∅ → `masc.nom.sg` (tag sits in POS column; `noun` is my inference — confirm) | A5.6 | keep (9) — DPD upādānakkhandha: masc, comp |
| 06-33 | 335 | `upādānakkhandho` | POS `m.n.s` → `noun`; Grammar ∅ → `masc.nom.sg` (tag sits in POS column; `noun` is my inference — confirm) | A5.6 | keep (9) — DPD upādānakkhandha: masc, comp |
| 06-34 | 337 | `upādānakkhandho` | POS `m.n.s` → `noun`; Grammar ∅ → `masc.nom.sg` (tag sits in POS column; `noun` is my inference — confirm) | A5.6 | keep (9) — DPD upādānakkhandha: masc, comp |
| 06-35 | 350 | `evaṃ` | Grammar ∅ → `adv` | B-P1 | keep (8) |
| 06-36 | 351 | `bahulaṃ` | POS `adv` → `ind`; Grammar `` → `adv` | A5.10 | keep (9) |
| 06-37 | 355 |  | `during his live` → `during his life` | A6 | keep (10) |
| 06-38 | 362 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 06-39 | 366 |  | Rebuild row: `\| sāvakesu \| noun \| masc.loc.pl \| among disciples, pupils, lit. hearers \|`  ✔ *Reviewer B proposes the same.* | A2 | keep (10) |
| 06-40 | 384 | `aniccā` | Gr `fem.nom.sg` → `masc.nom.pl` — *`aniccā` agrees with `saṅkhārā` (masc.pl)* | B-N31 | keep (9) |
| 06-41 | 394 | `anattā` | POS `noun` → `adj`; Gr `masc.nom.pl` → `masc.nom.sg` — *reviewer wrote `masc.nom.s`; converted to repo canonical* | B-N90 | adjust: per-06:394 Grammar `masc.nom.pl` → `masc.nom.sg`. Keep POS `noun`: DPD anatta 2 is masc (atta group), glossed "which is impersonal; non-self; not subject to identification", which is this row's gloss word for word; the atta-group nom sg is `anattā`. (7) |
| 06-42 | 414 |  | Grammar `masc.nom.sg` → `masc.nom.s` — **recommended reject:** Notation-only, against the `.sg` canon. | **B-X4✗** | drop: B-X4✗ notation regression (`.sg` → `.s`); the corpus uses `.sg`. |
| 06-43 | 461 | `paññāyethā'ti` | Grammar `opt.ref.3.sg` → `opt.refl.3.sg` | A5.3 | undecided — owner decision A5.3/B11.2. `ref` is a typo either way: `opt.refl.3.sg` (A5.3) or `opt.3.sg` (B11.2). DPD paññāyetha: "opt, reflx 3rd sg", which supports keeping refl. |
| 06-44 | 470 |  | `who's fire is out` → `whose fire is out` *(same fix at: per-01:78, per-06:470)* | A6 | keep (10) |
| 06-45 | 473 | `uddissa` | Gr `ind` → ∅ — *gerund: no inflectional grammar* | B-N77 | adjust: per-06:473 `\| uddissa \| ger \| ind \|` → `\| uddissa \| ind \| adv \|`. DPD uddissa 1 is "ind, adv, ger of uddisati", glossed "on account of; for the sake of", which matches this row's gloss. Blanking Grammar under POS `ger` (B-N77) contradicts DPD. (7) |
| 06-46 | 496 | `brahmacariyaṃ` | Gr `masc.acc.sg` → `nt.acc.sg` — *`brahmacariya` neuter* | B-N32 | keep (10) |
| 06-47 | 499 |  | `under  the` → `under the` | A6 | keep (10) |

## 07 — The Buddha's First Exclamation

`per-07-the-buddhas-first-exclamation.md` — 2 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 07-01 | 35 | `puna` | Grammar `adv.` → `adv`  ✔ *Reviewer B proposes the same.* | A5.7 | keep (9) |
| 07-02 | 50 | `ajjhagā` | ⚔ **C3 — keep ONE:** **Option A (audit)** Part 4: Grammar → `aor.3.sg`  ·  **Option B (reviewer)** Grammar → `imperf` (reviewer dropped person/number; if B is kept write `imperf.3.sg`)  ·  *Audit Part 4 has the same pair for `per-54:126`; use the same choice for both. Reviewer did not touch per-54:126.* | B-C3 | undecided |

## 08 — Respect for The Dhamma

`per-08-respect-for-the-dhamma.md` — 15 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 08-01 | 14 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 08-02 | 18 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 08-03 | 22 | `c'etarahi` | POS `ind` → `sandhi` (leave Grammar empty; reviewer also wrote `sandhi` in Grammar — not recommended) | B-P7 | keep (7) — DPD silent: c'etarahi (DPD etarahi: ind, adv; the parallel fusions cāpi, athāpi are sandhi) |
| 08-04 | 40 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 08-05 | 41 | `atha-api` | POS `ind` → `sandhi` (leave Grammar empty; reviewer also wrote `sandhi` in Grammar — not recommended) | B-P7 | keep (9) — DPD athāpi: sandhi |
| 08-06 | 43 | `esā` | POS `noun` → `pron` — *DPD: pron, fem.nom.sg of eta* | B-N91 | keep (10) |
| 08-07 | 55 | `hi` | Grammar ∅ → `emph` | B-P3 | keep (9) — DPD hi 1: ind, emph |
| 08-08 | 57 | `mahattam-` | Rebuild row as `\| mahattam- \| noun \| nt.acc.sg \| greatness; illustriousness \|` — *gender tag was in POS column* | B-N1 | keep (9) — DPD mahatta 2: nt, abstr, "greatness; illustriousness" |
| 08-09 | 58 | `abhikaṅkhatā` | POS `pp` → `prp` — *active present participle (reviewer: one longing/aspiring); gloss unchanged* | B-N92 | keep (7) — DPD silent: abhikaṅkhant (DPD has only abhikaṅkhatā fem, abstr) |
| 08-10 | 74 | `hi` | Grammar ∅ → `emph` | B-P3 | keep (9) — DPD hi 1: ind, emph |
| 08-11 | 77 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 08-12 | 78 | `ubho` | Gr `masc.nom.sg` → `masc.nom.pl` — *`ubho` plural* | B-N33 | keep (10) |
| 08-13 | 80 |  | `ripening , resulting` → `ripening, resulting` | A6 | keep (10) |
| 08-14 | 98 | `have` | Grammar ∅ → `emph` | B-P3 | keep (9) |
| 08-15 | 102 | `suciṇṇo` | POS `pp as adj` — unify to one form (see policy D4) | A8-D4 | undecided — owner decision D4: one form for `pp as adj`. DPD suciṇṇa is adj. |

## 09 — Going to True and False Refuges

`per-09-going-to-true-and-false-refuges.md` — 12 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 09-01 | 14 | `ve` | Grammar ∅ → `emph` | B-P3 | keep (9) — DPD ve: ind, emph |
| 09-02 | 19 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 09-03 | 35 | `kho` | Grammar ∅ → `emph` | B-P3 | keep (9) |
| 09-04 | 43 | `āgamma` | POS `verb` → `ger`, Grammar `ger` → ∅ (reviewer; audit/corpus keep `verb` + `ger`) — policy 11.4 | B-11.4 | undecided — owner decision B11.4. DPD: āgamma 1 is ger. |
| 09-05 | 47 |  | `not secure , this` → `not secure, this` | A6 | keep (10) |
| 09-06 | 56 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.2: ind, conj ("but") |
| 09-07 | 62 | `cattāri` | POS `adj` → `card` | B-P8 | keep (9) |
| 09-08 | 78 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 09-09 | 80 | `ariyaṃ-` | `nom.acc.sg` → `masc.acc.sg` — garbled case tag (`ariyaṃ … maggaṃ`)  ✔ *Reviewer B proposes the same.* | A4 | keep (9) |
| 09-10 | 81 | `ca-` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 09-11 | 96 | `kho` | Grammar ∅ → `emph` | B-P3 | keep (9) |
| 09-12 | 104 | `āgamma` | POS `verb` → `ger`, Grammar `ger` → ∅ (reviewer; audit/corpus keep `verb` + `ger`) — policy 11.4 | B-11.4 | undecided — owner decision B11.4. DPD: āgamma 1 is ger. |

## 10 — The Pāṭimokkha Exhortation

`per-10-the-patimokkha-exhortation.md` — 10 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 10-01 | 27 |  | Pāḷi chant text: `khantī paramaṃ tapo tītikkhā, …` / `tītikkhā` → `titikkhā` (chant line and headword row, both) — DPD spelling is `titikkhā`; only occurrence in the corpus  *(decision; data-preservation rule)* | B-Q3 | drop: DPD has `tītikkhā` as a headword (fem, "endurance; patience / forgiveness") alongside `titikkhā`, so the chant spelling is attested. A change to the chant line would also need owner sign-off under data preservation. |
| 10-02 | 34 | `tapo` | Gr `nt.nom.sg` → `masc.nom.sg` — *DPD: tapas masc.* | B-N34 | keep (9) — DPD tapas 1: masc, mano group, "spiritual practice; religious practice"; `tapo` is its nom sg |
| 10-03 | 35 | `tītikkhā` | Word `tītikkhā` → `titikkhā` — *pairs with chant-line decision Q3 (do together)* | B-N130 | drop: DPD has the headword `tītikkhā`. This row pairs with 267. |
| 10-04 | 35 |  | Pāḷi chant text: `khantī paramaṃ tapo tītikkhā, …` / `tītikkhā` → `titikkhā` (chant line and headword row, both) — DPD spelling is `titikkhā`; only occurrence in the corpus  *(decision; data-preservation rule)* | B-Q3 | drop: duplicate of 267 (same B-Q3 text, cited at line 35). DPD also has `tītikkhā`. |
| 10-05 | 41 | `hi` | Grammar ∅ → `emph` | B-P3 | keep (9) — DPD hi 1: ind, emph |
| 10-06 | 49 |  | `Patient and forgiveness` → `Patience and forgiveness`; `not onegone forth` → `not one gone forth` | A6 | keep (10) |
| 10-07 | 61 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 10-08 | 64 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 10-09 | 67 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 10-10 | 70 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |

## 11 — The Three Characteristics

`per-11-the-three-characteristics.md` — 17 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 11-01 | 16 | `iti` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 11-02 | 18 | `paññāya` | POS `verb` → `noun`; Gr `abs` → `fem.ins.sg`; Eng `knowing, understanding (or) noun f.ins.s with understanding` → `with understanding, with wisdom` — *gloss held two alternative readings; reviewer chose the noun reading* | B-N93 | keep (8) |
| 11-03 | 21 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 | undecided — owner decision D8. If applied: per-11:21 `**all conditioned things are impermanent'` → `**'all conditioned things are impermanent'`. |
| 11-04 | 25 | `atha` | Gr `adv` → ∅ | B-N78 | keep (8) |
| 11-05 | 45 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 | undecided — owner decision D8. If applied: per-11:45 `**all conditioned things are unsatisfactory'` → `**'all conditioned things are unsatisfactory'`. |
| 11-06 | 56 |  | Grammar `masc.nom.sg` → `masc.nom.s` — **recommended reject:** Notation-only, against the `.sg` canon. | **B-X4✗** | drop: B-X4✗ notation regression (`.sg` → `.s`). |
| 11-07 | 58 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 | undecided — owner decision D8. If applied: per-11:58 `**everything is void of self'` → `**'everything is void of self'`. |
| 11-08 | 78 | `eva-` | Grammar ∅ → `emph` | B-P3 | keep (8) |
| 11-09 | 90 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 11-10 | 91 | `kho` | Grammar ∅ → `emph` | B-P3 | keep (9) |
| 11-11 | 92 |  | `well preached , well-taught` → `well preached, well-taught` | A6 | keep (10) |
| 11-12 | 97 | `pāram-` | Grammar ∅ → `prep` | B-P5 | keep (9) — DPD pāraṃ: ind, prep |
| 11-13 | 112 | `vippahāya` | POS `verb` → `ger`, Grammar `ger` → ∅ (reviewer; audit/corpus keep `verb` + `ger`) — policy 11.4 | B-11.4 | undecided — owner decision B11.4. DPD: vippahāya is ger. |
| 11-14 | 118 | `āgamma` | POS `verb` → `ger`, Grammar `ger` → ∅ (reviewer; audit/corpus keep `verb` + `ger`) — policy 11.4 | B-11.4 | undecided — owner decision B11.4. DPD: āgamma 1 is ger. |
| 11-15 | 120 | `yattha` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 11-16 | 130 | `tatra-` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 11-17 | 133 | `hitvā` | POS `verb` → `abs`, Grammar `abs` → ∅ (reviewer; audit/corpus keep `verb` + `abs`) — policy 11.4 | B-11.4 | undecided — owner decision B11.4. DPD: hitvā is abs. |

## 12 — The Burdens

`per-12-the-burdens.md` — 6 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 12-01 | 14 | `have` | Grammar ∅ → `emph` | B-P3 | keep (9) |
| 12-02 | 17 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 12-03 | 33 | `nikkhipitvā` | POS `verb` → `abs`, Grammar `abs` → ∅ (reviewer; audit/corpus keep `verb` + `abs`) — policy 11.4 | B-11.4 | undecided — owner decision B11.4. DPD: nikkhipitvā is abs. |
| 12-04 | 38 | `anādiya` | POS `verb` → `ger`, Grammar `ger` → ∅ (reviewer; audit/corpus keep `verb` + `ger`) — policy 11.4 | B-11.4 | undecided — owner decision B11.4. DPD: anādiya is ger. |
| 12-05 | 41 | `abbuyha` | POS `verb` → `ger`, Grammar `ger` → ∅ (reviewer; audit/corpus keep `verb` + `ger`) — policy 11.4 | B-11.4 | undecided — owner decision B11.4. DPD: abbuyha is ger. |
| 12-06 | 43 | `parinibbuto` | POS `adj` → `pp` | B-N94 | keep (9) — DPD parinibbuta: pp |

## 13 — From the Elder Raṭṭhapāla

`per-13-from-the-elder-ratthapala.md` — 45 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 13-01 | 13 |  | `passa`: `imp.2.sg` → `imper.2.s` — **recommended reject:** Regression: corpus uses `imp`, not `imper`. | **B-X3✗** | drop: B-X3✗ regression. DPD passa 2.1 is "imp 2nd sg" and the corpus uses `imp`. |
| 13-02 | 14 |  | **D3** `<br>` inside table cells (lines 14). Policy: keep (note the exception) or convert `A<br>(or)<br>B` → `A (or) B`. | A8-D3 | undecided — owner decision D3 on `<br>`. The `<br>` is still at per-13:14 (mech `gone` is a false negative). |
| 13-03 | 14 | `cittakataṃ` | Gr `masc.acc.sg` → `nt.acc.sg` — *agrees with nt `bimbaṃ`/`rūpaṃ`* | B-N35 | keep (9) — DPD bimba 1: nt, so `cittakataṃ` agreeing with `bimbaṃ` is nt |
| 13-04 | 22 | `dhuvaṃ` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 13-05 | 25 |  | `diseased, . There` → `diseased. There` | A6 | keep (10) |
| 13-06 | 32 |  | `passa`: `imp.2.sg` → `imper.2.s` — **recommended reject:** Regression: corpus uses `imp`, not `imper`. | **B-X3✗** | drop: B-X3✗ regression (corpus `imp`; DPD passa imp 2nd sg). |
| 13-07 | 33 | `cittakataṃ` | Gr `masc.acc.sg` → `nt.acc.sg` — *same* | B-N36 | keep (8) |
| 13-08 | 37 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 13-09 | 38 | `aṭṭhiṃ` | Gr `nt.nom.sg` → `nt.acc.sg` — *acc., not nom.* | B-N37 | undecided — DPD aṭṭhi 1.1 is nt ("bone") but DPD silent on the form `aṭṭhiṃ`; the syntax choice is still open: the bold translation reads `aṭṭhiṃ` as the subject of `sobhati` (nom); B reads it as the object of `passa` (acc). |
| 13-10 | 40 | `onaddhaṃ` | Gr `nt.nom.sg` → `nt.acc.sg` — *acc., not nom.* | B-N38 | undecided — depends on 329 (`onaddhaṃ` agrees with `aṭṭhiṃ`). DPD onaddha is pp, so the POS is right. |
| 13-11 | 41 | `saha` | Grammar ∅ → `prep` | B-P5 | keep (9) |
| 13-12 | 42 | `vatthehi` | `nt.ins.sg` → `nt.ins.pl` — `-ehi` is plural | A4 | keep (9) — DPD vattha 1.1: nt |
| 13-13 | 52 | `alattaka-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision A5.7/B11.3. If the gender is kept, DPD gives alattaka as nt, so per-13:52 `masc` → `nt`. |
| 13-14 | 58 | `alaṃ` | Grammar ∅ → `emph` | B-P3 | keep (9) |
| 13-15 | 62 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.2: ind, conj ("but") |
| 13-16 | 65 |  | `fora seeker` → `for a seeker` | A6 | keep (10) |
| 13-17 | 72 | `aṭṭha-` | POS `adj` → `card` | B-P8 | keep (9) |
| 13-18 | 80 |  | `fora seeker ofthe` → `for a seeker of the` | A6 | keep (10) |
| 13-19 | 106 | `laddhāna` | POS `verb` → `abs`, Grammar `abs` → ∅ (reviewer; audit/corpus keep `verb` + `abs`) — policy 11.4 | B-11.4 | undecided — owner decision B11.4. DPD: laddhāna is abs. |
| 13-20 | 107 | `vittaṃ` | Gr `masc.acc.sg` → `nt.acc.sg` | B-N39 | keep (9) — DPD vitta 1.1: nt, "wealth; property" |
| 13-21 | 109 | `mohā` | Gr `nt.abl.sg` → `masc.abl.sg` — *`moha` masc.* | B-N40 | keep (10) |
| 13-22 | 128 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 13-23 | 130 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 13-24 | 133 |  | `desire , not free` → `desire, not free` | A6 | keep (10) |
| 13-25 | 137 | `hutvāna` | POS `verb` → `abs`, Grammar `abs` → ∅ (reviewer; audit/corpus keep `verb` + `abs`) — policy 11.4 | B-11.4 | undecided — owner decision B11.4. DPD: hutvāna is abs. |
| 13-26 | 158 | `labhate` | Grammar `pr.refl.3.sg` → `pr.3.sg` (reviewer drops `refl`; audit 5.3 keeps it: `imp.refl.1.pl`) — policy 11.2 | B-11.2 | undecided — owner decision A5.3/B11.2. DPD gives labhate as "pr, reflx 3rd sg", which supports keeping refl. |
| 13-27 | 161 | `cāpi` | POS `ind` → `sandhi` (leave Grammar empty) | B-P7 | keep (10) |
| 13-28 | 164 | `vihanti` | Gr `pr.3.sg` → `pr.3.pl` | B-N79 | drop: DPD has vihanti as "pr", vi + hana + ti > hanti (3rd sg). The implied subject is "one" (translation: "can not even ward off"), so `pr.3.sg` is right. |
| 13-29 | 183 | `hi` | Grammar ∅ → `emph` | B-P3 | keep (9) — DPD hi 1: ind, emph |
| 13-30 | 184 | `paññā-` | Grammar `fem.nom.sg` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision A5.7/B11.3; note `paññā-` is sandhi (paññ'eva), not a compound member, and fem.nom.sg fits DPD paññā fem as subject of seyyā |
| 13-31 | 185 | `eva` | Grammar ∅ → `emph` | B-P3 | keep (8) |
| 13-32 | 190 | `idha-` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 13-33 | 193 | `hi` | Grammar ∅ → `emph` | B-P3 | keep (9) — DPD hi 1: ind, emph |
| 13-34 | 210 | `hi` | Grammar ∅ → `emph` | B-P3 | keep (9) — DPD hi 1: ind, emph |
| 13-35 | 219 | `disvā` | POS `verb` → `abs`, Grammar `abs` → ∅ (reviewer; audit/corpus keep `verb` + `abs`) — policy 11.4 | B-11.4 | undecided — owner decision B11.4; DPD disvā pos abs |
| 13-36 | 222 | `pabbajito-` | POS `pp/noun` — unify to one form (see policy D4) | A8-D4 | undecided — owner decision D4 (POS `pp/noun`); DPD has pabbajita 1 masc "monk" and pabbajita 2 pp "ordained"; the gloss "(one) gone forth, a monk" fits pabbajita 1 |
| 13-37 | 222 | `pabbajito-` | POS `pp/noun` → `pp` — *drops `/noun`* | B-N95 | undecided — owner decision D4 (B proposes `pp`); same cell as 356; DPD pabbajita 1 (masc, "monk") fits this gloss better than `pp` |
| 13-38 | 241 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 13-39 | 243 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 13-40 | 247 | `disvā` | POS `verb` → `abs`, Grammar `abs` → ∅ (reviewer; audit/corpus keep `verb` + `abs`) — policy 11.4 | B-11.4 | undecided — owner decision B11.4; DPD disvā pos abs |
| 13-41 | 248 | `pabbajito-` | POS `pp/noun` — unify to one form (see policy D4) | A8-D4 | undecided — owner decision D4 (POS `pp/noun`); DPD has pabbajita 1 masc "monk" and pabbajita 2 pp "ordained"; the gloss "(one) gone forth, a monk" fits pabbajita 1 |
| 13-42 | 248 | `pabbajito-` | POS `pp/noun` → `pp` — *same* | B-N96 | undecided — owner decision D4 (B proposes `pp`); same cell as 361; DPD pabbajita 1 (masc, "monk") fits this gloss better than `pp` |
| 13-43 | 251 | `apaṇṇakaṃ` | POS `ind` → `adj`; Gr ∅ → `nt.acc.sg` — *gloss `surely; certainly` unchanged (reviewer: DPD adj, used adverbially as acc.sg)* | B-N97 | drop: DPD apaṇṇakaṃ = ind, adv (acc sg of apaṇṇaka), so POS ind is right; at most Grammar ∅ → `adv` under BP1 |
| 13-44 | 253 | `eva` | Grammar ∅ → `emph` | B-P3 | keep (8) |
| 13-45 | 254 | `seyyo` | POS `ind` → `adj`; Gr ∅ → `masc.nom.sg` — *DPD: seyya adj, compar* | B-N98 | drop: DPD seyyo = ind, compar (nom sg of seyya), so POS ind is right |

## 14 — From the Elder Pārāpariya

`per-14-from-the-elder-parapariya.md` — 27 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 14-01 | 36 | `sītavātaparittāṇaṃ` | Rebuild row as `\| sītavātaparittāṇaṃ \| noun \| nt.nom.sg \| protection from cold and wind \|` — *Tag sits in POS column (audit Part 5.6 `nt.n.s` fix would leave it in the wrong column — this amends it)* | B-N2 | adjust: per-14:36 `\| sītavātaparittāṇaṃ \| nt.n.s \| \| protection from cold and wind \|` → `\| sītavātaparittāṇaṃ \| ind \| adv \| for protection from cold and wind \|` (DPD: ind, adv, comp) (6) |
| 14-02 | 40 | `hirikopīnachādanaṃ` | Rebuild row as `\| hirikopīnachādanaṃ \| noun \| nt.nom.sg \| covering that which arouses shyness \|` — *same as 14:36* | B-N3 | adjust: per-14:40 `\| hirikopīnachādanaṃ \| nt.n.s \| \| covering that which arouses shyness \|` → `\| hirikopīnachādanaṃ \| ind \| adv \| for covering that which arouses shyness \|` (DPD: ind, adv, comp "to conceal the genitals") (6) |
| 14-03 | 44 |  | `(their robs)` → `(their robes)` | A6 | keep (10) |
| 14-04 | 62 | `paṇītaṃ` | Gr `nt.nom.sg` → `nt.acc.sg` — *object, acc.* | B-N41 | keep (7) — DPD paṇīta: pp (cross-check only; the case comes from syntax) |
| 14-05 | 65 | `lūkhaṃ` | Gr `nt.nom.sg` → `nt.acc.sg` — *object, acc.* | B-N42 | keep (7) — DPD lūkha: adj (cross-check only; the case comes from syntax) |
| 14-06 | 66 | `appaṃ` | Gr `nt.nom.sg` → `nt.acc.sg` — *object, acc.* | B-N43 | keep (7) |
| 14-07 | 70 | `bahuṃ` | Gr `nt.nom.sg` → `nt.acc.sg` — *object, acc.* | B-N44 | keep (7) — DPD bahu: adj (cross-check only; the case comes from syntax) |
| 14-08 | 83 | `\>na-` | POS `neg` → `ind`; Grammar `` → `neg` | A5.10 | keep (8) — DPD na 1: ind, so POS `neg` → `ind` is right; Grammar `neg` vs ∅ follows owner decision B-X2⚑ |
| 14-09 | 94 | `parikkhāre` | Gr `masc.acc.pl` → `masc.loc.sg` — *locative* | B-N45 | keep (6) |
| 14-10 | 95 | `bhesajje` | Gr `nt.acc.pl` → `nt.loc.sg` — *locative* | B-N46 | keep (8) |
| 14-11 | 97 | `paccaye` | Gr `nt.acc.pl` → `masc.loc.sg` — *locative* | B-N47 | keep (8) — DPD paccaya 1 (masc) and 2 (nt) share the gloss "support; requisite", so `masc` is valid; the acc.pl → loc.sg change is the substance |
| 14-12 | 103 | `na` | ⚔ **C13 — keep ONE:** **Option A (audit)** Part 5.10: POS `neg` → `ind`, Grammar `neg` (audit lists per-14:83,103,148)  ·  **Option B (reviewer)** POS `neg` → `ind`, Grammar ∅  ·  *Corpus has 16 existing `ind` / `neg` rows; see X2. Reviewer changed only :103 of the three.* | B-C13 | undecided |
| 14-13 | 107 | `yathā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 14-14 | 109 | `āsavakkhaye` | POS `adj` → `noun`; Gr `masc.acc.pl` → `masc.loc.sg` | B-N99 | keep (8) |
| 14-15 | 120 | `kandarāsu` | Gr `masc.loc.pl` → `fem.loc.pl` — *`kandarā` fem.* | B-N48 | keep (10) |
| 14-16 | 122 | `ca` | POS `conj` → `ind`; Grammar `` → `conj`  ✔ *Reviewer B proposes the same.* | A5.10 | keep (9) — DPD ca 2.1: ind, conj |
| 14-17 | 124 |  | `at the foots of trees` → `at the feet of trees` | A6 | keep (9) |
| 14-18 | 147 | `atthaddhamānasā` | Gr ∅ → `masc.nom.pl` — *grammar was empty* | B-N49 | keep (8) |
| 14-19 | 148 | `\>na-` | POS `neg` → `ind`; Grammar `` → `neg` | A5.10 | keep (8) — DPD na 1: ind, so POS `neg` → `ind` is right; Grammar `neg` vs ∅ follows owner decision B-X2⚑ |
| 14-20 | 182 | `teladhārāva` | Rebuild row as `\| teladhārāva \| noun \| fem.nom.sg \| as stream of oil \|` — *POS empty* | B-N4 | undecided — owner decision: POS for the head row of a split word that has `\>` sub-rows (empty, as at per-14:82, or `noun`, or `sandhi` under BP7) |
| 14-21 | 196 | `yathā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 14-22 | 207 | `upaṭṭhapetvāna,` | POS `verb` → `abs`, Grammar `abs` → ∅ (reviewer; audit/corpus keep `verb` + `abs`) — policy 11.4 | B-11.4 | undecided — owner decision B11.4; DPD upaṭṭhapetvāna pos abs |
| 14-23 | 208 | `evaṃ` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 14-24 | 220 | `saritvā` | POS `verb` → `abs`, Grammar `abs` → ∅ (reviewer; audit/corpus keep `verb` + `abs`) — policy 11.4 | B-11.4 | undecided — owner decision B11.4; DPD saritvā pos abs |
| 14-25 | 224 | `vattam-` | Gr ∅ → `nt.acc.sg` | B-N50 | keep (9) — DPD vatta 1.1: nt, "custom; practice; way of life" |
| 14-26 | 231 | `kiñcāpi` | POS `ind` → `sandhi` (leave Grammar empty) | B-P7 | keep (9) |
| 14-27 | 232 | `pacchimo` | `masc.nom.pl` → `masc.nom.sg` — `-o` is singular | A4 | keep (9) |

## 15 — On Protection

`per-15-on-protection.md` — 15 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 15-01 | 11 | `handa` | ⚔ **C2 — keep ONE:** **Option A (audit)** Part 5.4: Grammar `emp` → `emph`  ·  **Option B (reviewer)** Grammar `emp` → `excl`  ·  *DPD: `handa` = ind, excl. Choosing B is consistent with P4 (all `handa` rows → `excl`).* | B-C2 | undecided |
| 15-02 | 14 | `gāthāyo` | Grammar `fem nom pl` → `fem.nom.pl` | A5.12 | drop: superseded by 409 (same cell; the case should be acc, not just the notation fixed) |
| 15-03 | 14 | `gāthāyo` | Gr `fem nom pl` → `fem.acc.pl` | B-N51 | keep (8) |
| 15-04 | 15 | `bhaṇāmase` | `imp.reflx.3.pl` → `imp.refl.1.pl` — "let us chant" = 1st person (cf. per-06:19 tagged 1.pl) | A4 | adjust: per-15:15 `imp.reflx.3.pl` → `imp.reflx.1.pl` (DPD: imp, reflx 1st pl); spelling of `reflx`/`refl` follows owner decision A5.3/B11.2 (9) |
| 15-05 | 15 | `bhaṇāmase` | Grammar `imp.reflx.3.pl` → `imp.1.pl` (reviewer drops `refl`; audit 5.3 keeps it: `imp.refl.1.pl`) — policy 11.2 | B-11.2 | undecided — owner decision A5.3/B11.2; DPD keeps reflx (imp, reflx 1st pl) |
| 15-06 | 27 | `parakkamma` | POS `verb` → `ger`, Grammar `ger` → ∅ (reviewer; audit/corpus keep `verb` + `ger`) — policy 11.4 | B-11.4 | undecided — owner decision B11.4; DPD parakkamma pos ger |
| 15-07 | 31 | `nappahāya` | POS `verb` → `ger`, Grammar `ger` → ∅ (reviewer; audit/corpus keep `verb` + `ger`) — policy 11.4 | B-11.4 | undecided — owner decision B11.4; DPD nappahāya pos ger |
| 15-08 | 33 | `kāme` | Gr `masc.loc.sg` → `masc.acc.pl` — *acc. pl.* | B-N52 | adjust: per-15:33 `\| kāme \| noun \| masc.loc.sg \| in pleasure, sensual pleasure \|` → `\| kāme \| noun \| masc.acc.pl \| pleasures, sensual pleasures \|` (object of nappahāya; gloss as per-15:28) (8) |
| 15-09 | 53 | `hi` | Grammar ∅ → `emph` | B-P3 | keep (9) — DPD hi 1: ind, emph |
| 15-10 | 55 | `bhiyyo` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 15-11 | 68 | `seyyo` | POS `ind` → `adj`; Gr ∅ → `masc.nom.sg` — *same* | B-N100 | drop: DPD seyyo = ind, compar, so POS ind is right |
| 15-12 | 74 | `seyyo` | POS `ind` → `adj`; Gr ∅ → `masc.nom.sg` — *same* | B-N101 | drop: DPD seyyo = ind, compar, so POS ind is right |
| 15-13 | 76 | `katvā` | POS `verb` → `abs`, Grammar `abs` → ∅ (reviewer; audit/corpus keep `verb` + `abs`) — policy 11.4 | B-11.4 | undecided — owner decision B11.4; DPD katvā pos abs |
| 15-14 | 87 | `yathā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 15-15 | 90 | `eva-` | Grammar ∅ → `emph` | B-P3 | keep (8) |

## 16 — Miscellaneous Verses

`per-16-miscellaneous-verses.md` — 28 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 16-01 | 29 | `appassuta-` | Gr ∅ → `masc.nom.sg` — *grammar was empty* | B-N53 | keep (7) |
| 16-02 | 51 | `satīmanto` | POS `adj as noun` — unify to one form (see policy D4) | A8-D4 | undecided — owner decision D4 (POS `adj as noun`) |
| 16-03 | 51 | `satīmanto` | POS `adj as noun` → `noun`; Gr `masc.nom.sg` → `masc.nom.pl` | B-N102 | adjust: per-16:51 Grammar `masc.nom.sg` → `masc.nom.pl` (-manto is nom pl; verb uyyuñjanti is pr.3.pl); POS `adj as noun` waits on owner decision D4 (8) |
| 16-04 | 72 | `pubbe` | ⚔ **C10 — keep ONE:** **Option A (audit)** Part 3: `pubbe / ind / (empty) / before, previously, … in a previous life`  ·  **Option B (reviewer)** Same row but Grammar `adv`  ·  *Audit leaves Grammar empty; reviewer (and audit 5.11 for per-18:248) use `adv` for `pubbe`.* | B-C10 | undecided |
| 16-05 | 75 | `pacchā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 16-06 | 77 | `m'āhu` | POS `v+ind` → `verb`; Gr `aor.3.sg` → `aor.3.pl` — *POS `v+ind` is a D4 composite value* | B-N103 | undecided — owner decision D4 for POS `v+ind`; keep `aor.3.sg`: DPD ahu 1.1 is "aor of hoti, was" and the subject kiñcanaṃ is sg; DPD āhu (perf 3pl of āha, "they say") is a different word from m'āhu = mā ahu |
| 16-07 | 79 | `majjhe` | ⚔ **C8 — keep ONE:** **Option A (audit)** Part 5.11: Grammar `from loc. sg.` → `adv`  ·  **Option B (reviewer)** POS `ind` → `noun`, Grammar `from loc. sg.` → `nt.loc.sg` (gloss unchanged: `in the present, lit. in the middle`)  ·  *DPD `majjhe` is a locative of `majjha`; ‘adv’ vs real locative.* | B-C8 | undecided |
| 16-08 | 118 | `santiyā;` | POS `verb` → `noun` | B-N104 | keep (9) — DPD santi 1.1: fem, abstr, "peace" |
| 16-09 | 121 | `pamatte` | POS `pp as adj` — unify to one form (see policy D4) | A8-D4 | undecided — owner decision D4 (POS `pp as adj`) |
| 16-10 | 121 | `pamatte` | POS `pp as adj` → `pp` — *D4: `pp as adj` → `pp`* | B-N105 | undecided — owner decision D4 (B proposes `pp`); same cell as 437 |
| 16-11 | 122 | `viññāya` | POS `verb` → `ger`, Grammar `ger` → ∅ (reviewer; audit/corpus keep `verb` + `ger`) — policy 11.4 | B-11.4 | undecided — owner decision B11.4; DPD viññāya pos ger |
| 16-12 | 139 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 16-13 | 149 | `upaccagā` | `imp.3.sg` → `aor.3.sg` — aorist "it passed by" | A4 | adjust: per-16:149 `imp.3.sg` → `imperf.3.sg` (DPD upaccagā = imperf of upa ati √gam, not aor) (7) |
| 16-14 | 150 |  | Rebuild row: `\| khaṇ'ātītā \| adj \| masc.nom.pl \| who has missed the chance, who lost the opportunity, lit. moment passed by \|`  ✔ *Reviewer B proposes the same.* | A3 | keep (9) |
| 16-15 | 151 | `hi` | Grammar ∅ → `emph` | B-P3 | keep (9) — DPD hi 1: ind, emph |
| 16-16 | 205 | `eva` | Grammar `emph.` → `emph`  ✔ *Reviewer B proposes the same.* | A5.4 | keep (8) |
| 16-17 | 221 | `tumhehi` | `masc.ins.pl` → `2.ins.pl` — personal pronoun | A4 | keep (9) |
| 16-18 | 232 | `yaṃ` | Gr `masc.acc.sg` → `nt.nom.sg` — *neuter, subject* | B-N54 | keep (8) |
| 16-19 | 234 | `karaṇīyaṃ` | Gr `masc.acc.sg` → `nt.nom.sg` — *neuter, subject* | B-N55 | keep (8) |
| 16-20 | 239 | `upādāya` | ⚔ **C9 — keep ONE:** **Option A (audit)** Part 5.11: Grammar `from ger` → `ger`  ·  **Option B (reviewer)** Grammar `from ger` → `adv`  ·  *Reviewer: DPD upādāya 2/3 = ind, adv, used as postposition.* | B-C9 | undecided |
| 16-21 | 240 | `kataṃ` | Gr `masc.acc.sg` → `nt.nom.sg` — *neuter, subject* | B-N56 | keep (8) |
| 16-22 | 242 | `taṃ` | Gr `masc.acc.sg` → `nt.nom.sg` — *neuter, subject* | B-N57 | keep (8) |
| 16-23 | 256 | `mā pamād'attha` | POS `ind+m+imp` — unify to one form (see policy D4) | A8-D4 | undecided — owner decision D4 (POS `ind+m+imp`) |
| 16-24 | 256 |  | multi-word POS tag (`v + pn` / `ind+pn` / `ind+m+imp` / `adv+ind`): use `idiom` or `sandhi` per corpus convention (policy D4) | A8-D4 | undecided — owner decision D4; duplicate of 451 (same cell) |
| 16-25 | 258 | `pacchā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 16-26 | 261 | `ayaṃ` | `POS noun` → `POS pron` — demonstrative pronoun (Grammar fem.nom.sg is correct)  ✔ *Reviewer B proposes the same.* | A4 | keep (9) |
| 16-27 | 266 |  | `There are these foots of a tree` → `There are these roots of trees` (check the table rows above for the same wording) | A6 | adjust: per-16:266 `There are these foots of a tree` → `There are these roots of trees` (7) |
| 16-28 | 266 |  | **D6** if a table row above glosses `rukkha-mūlāni` as "foots of a tree", align with the corrected translation ("roots of trees"). | A8-D6 | adjust: per-16:252 `foots of trees, bases of trees` → `roots of trees, bases of trees` (7) |

## 17 — A single Excellent Night

`per-17-a-single-excellent-night.md` — 21 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 17-01 | 12 | `atītaṃ` | POS `adj (as noun)` — unify to one form (see policy D4) | A8-D4 | undecided — owner decision D4 (POS `adj (as noun)`); DPD atīta 1 is nt "past; what is past" (a noun), which fits `nt.acc.sg` here; DPD atītaṃ ind, adv is the adverb "in the past" |
| 17-02 | 12 | `atītaṃ` | POS `adj (as noun)` → `adj` — *D4: unify `adj (as noun)` → `adj`* | B-N106 | undecided — owner decision D4 (B proposes `adj`); same cell as 464; DPD atīta 1 is nt (noun), not adj |
| 17-03 | 21 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 17-04 | 31 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 17-05 | 34 |  | Rebuild row: `\| tattha tattha \| ind \| adv \| right there, here and now, in each and every case, lit. there and there \|`  ✔ *Reviewer B proposes the same row; his gloss order differs.* | A3 | keep (7) |
| 17-06 | 44 | `asaṃhiraṃ` | POS `adj (or as noun)` — unify to one form (see policy D4) | A8-D4 | undecided — owner decision D4 (POS `adj (or as noun)`); DPD asaṃhira: ptp |
| 17-07 | 44 | `asaṃhiraṃ` | POS `adj (or as noun)` → `adj` — *same* | B-N107 | undecided — owner decision D4 (B proposes `adj`); same cell as 469; DPD gives asaṃhira as ptp, not adj |
| 17-08 | 45 | `asaṅkuppaṃ` | POS `adj (or as noun)` — unify to one form (see policy D4) | A8-D4 | undecided — owner decision D4 (POS `adj (or as noun)`); DPD asaṅkuppa: ptp |
| 17-09 | 45 | `asaṅkuppaṃ` | POS `adj (or as noun)` → `adj` — *same* | B-N108 | undecided — owner decision D4 (B proposes `adj`); same cell as 471; DPD gives asaṅkuppa as ptp, not adj |
| 17-10 | 47 | `vidvā` | Rebuild row as `\| vidvā \| adj \| masc.nom.sg \| wise \|` — *POS cell held `masc`* | B-N5 | adjust: per-17:47 `\| vidvā \| masc \| masc.nom.sg \| wise \|` → `\| vidvā \| noun \| masc.nom.sg \| wise \|`: DPD vidvant is masc ("who is wise"), not adj as B-N5 proposes (8) |
| 17-11 | 57 | `ajja-` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 17-12 | 64 | `suve` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 17-13 | 68 | `saṅgaran-` | Grammar `nt.nom.sg.` → `nt.nom.sg`  ✔ *Reviewer B proposes the same.* | A5.7 | keep (8) |
| 17-14 | 80 | `evaṃ` | Grammar ∅ → `adv` | B-P1 | keep (8) — DPD evaṃ 1: ind, adv |
| 17-15 | 81 | `vihārim-` | POS `adj (as noun)` — unify to one form (see policy D4) | A8-D4 | undecided — owner decision D4 (`adj (as noun)` form); same decision as 479; DPD silent: vihārin |
| 17-16 | 81 | `vihārim-` | POS `adj (as noun)` → `adj` — *same* | B-N109 | undecided — owner decision D4 (B-N109 is one option of the D4 pair with 478); DPD silent: vihārin |
| 17-17 | 83 | `ahorattam-` | Grammar `nt.acc.sg.` → `nt.acc.sg` | A5.7 | adjust: per-17:83 `\| ahorattam- \| ind \| nt.acc.sg. \|` → `\| ahorattam- \| ind \| adv \|`: DPD ahorattaṃ is ind, adv, comp (acc sg of ahoratta), so stripping the period alone leaves a case tag on an `ind` row (7) |
| 17-18 | 83 | `ahorattam-` | ⚔ **same cell as A5.7 row above — keep ONE:** **Option A (A5.7)** Grammar `nt.acc.sg.` → `nt.acc.sg`  ·  **Option B (B-P1)** Grammar `nt.acc.sg.` → `adv` (reviewer wrote `adv`; current cell is `nt.acc.sg.`, not empty) | B-P1 | undecided |
| 17-19 | 86 | `ve` | Grammar ∅ → `emph` | B-P3 | keep (9) — DPD ve: ind, emph |
| 17-20 | 90 | `ti –` | Grammar ∅ → `adv` | B-P1 | keep (7) — DPD iti: ind, adv |
| 17-21 | 92 | `ācikkhate` | Grammar `reflex.opt.3.sg` → `opt.refl.3.sg` | A5.3 | undecided — owner decision A5.3/B11.2; DPD writes reflexive as `reflx`; DPD silent: ācikkhate (DPD ācikkhati is pr only; `-te` is a pr reflx ending, so the `opt` mood may also be wrong) |

## 18 — Setting in Motion The Wheel of Dhamma

`per-18-setting-in-motion-the-wheel-of-dhamma.md` — 29 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 18-01 | 15 | `pabbajitena` | Rebuild row as `\| pabbajitena \| noun \| masc.ins.sg \| by monk, one who has gone forth \|` — *POS cell held `masc`* | B-N6 | keep (9) — POS cell `masc` is a plain column error; DPD pabbajita 1: masc ("monk") |
| 18-02 | 28 | `kāmasukhallikā-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision A5.7/B11.3; DPD kāmasukhallikā: fem, comp (the gender itself is right) |
| 18-03 | 56 | `kho` | Grammar ∅ → `emph` | B-P3 | keep (9) — DPD kho: ind, emph |
| 18-04 | 90 | `eva` | Grammar ∅ → `emph` | B-P3 | keep (8) — DPD eva 1: ind, emph ("only; just") |
| 18-05 | 122 | `jāti` | Rebuild row as `\| jāti \| noun \| fem.nom.sg \| birth, rebirth, conception \|` — *columns shifted; `f.n.s` embedded in gloss; audit Part 2 missed this row* | B-N7 | keep (9) — DPD jāti 1: fem, "birth; rebirth; conception" |
| 18-06 | 136 |  | Rebuild row: `\| dukkha- \| noun \| \| discomfort, suffering, pain, unease, something unsatisfactory, problem, trouble \|`  ✔ *Reviewer B proposes the same.* | A3 | keep (9) — DPD dukkha 3: nt |
| 18-07 | 158 | `piyehi` | POS `adj (as noun)` — unify to one form (see policy D4) | A8-D4 | undecided — owner decision D4 (`adj (as noun)` form); same decision as 499; DPD piya 1 is adj, with noun senses piya 3 (nt, "dear one") and piya 5 (masc) |
| 18-08 | 158 | `piyehi` | POS `adj (as noun)` → `adj` — *same* | B-N110 | undecided — owner decision D4 (B-N110 is one option of the D4 pair with 498); DPD piya 1: adj (noun senses piya 3 nt, piya 5 masc) |
| 18-09 | 168 | `yam-(p)-icchaṃ` | Grammar `m.acc.sg` → `masc.acc.sg` | A5.6 | keep (8) |
| 18-10 | 171 | `na` | reviewer: Grammar `neg` → ∅ — **⚑ user decision, not implemented unless you remove the ⚑** (for the word `na` the corpus has 33 rows with empty Grammar vs 7 `neg`) | **B-X2⚑** | undecided — owner decision: Grammar for `na` (`neg` vs ∅, B-X2⚑); count 33/7 not re-checked; DPD na 1 is ind with no sub-type, which supports ∅ |
| 18-11 | 245 | `dukkhaṃ` | ⚔ **C4 — keep ONE:** **Option A (audit)** Part 2: rebuilt row `noun` / `nt.nom.sg` (subject of `idaṃ dukkhaṃ ariyasaccaṃ`)  ·  **Option B (reviewer)** Rebuilt row `noun` / `nt.acc.sg` (reviewer just fixed the `nt.ac.s` typo)  ·  *Row is column-shifted: both options rebuild the same row, only the case differs. Reviewer's meaning/POS fix is identical to A.* | B-C4 | undecided |
| 18-12 | 247 |  | Rebuild row: `\| me \| pron \| 1.dat.sg \| to me, for me \|`  ✔ *Reviewer B proposes the same.* | A2 | keep (9) — DPD me 3: pron, 1st dat sg |
| 18-13 | 248 | `pubbe` | Grammar `from loc.sg` → `adv`  ✔ *Reviewer B proposes the same.* | A5.11 | keep (9) — DPD pubbe 1: ind, adv, loc sg of pubba |
| 18-14 | 262 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 | undecided — owner decision D8 (per-18:262 opening `“` missing before `This is`) |
| 18-15 | 269 | `kho` | Grammar ∅ → `emph` | B-P3 | keep (9) — DPD kho: ind, emph |
| 18-16 | 283 | `kho` | Grammar ∅ → `emph` | B-P3 | keep (9) — DPD kho: ind, emph |
| 18-17 | 286 | `dukkhaṃ` | Grammar `nt.acc.sg.` → `nt.acc.sg` | A5.7 | undecided — owner decision A5.7 (trailing period); `dukkhaṃ` at per-18:286 may be nom (subject), not acc — not judged |
| 18-18 | 294 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 | undecided — owner decision D8 (per-18:294 opening `“` missing) |
| 18-19 | 314 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 | undecided — owner decision D8 (per-18:314 opening `“` missing) |
| 18-20 | 331 |  | Pāḷi (L325) is `dukkha-nirodho … sacchikatan-ti`, but translation says "this noble truth of the **origin** of suffering has been personally experienced." → "this noble truth of the **cessation** of suffering has been personally experienced." | A7 | keep (9) — per-18:331 still reads "origin" |
| 18-21 | 335 |  | `the noble truth of the the way` → `the noble truth of the way` (doubled word, same section). | A7 | keep (10) |
| 18-22 | 335 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 | undecided — owner decision D8 (per-18:335 opening `“` missing) |
| 18-23 | 343 |  | Pāḷi (L337) is `dukkha-nirodha-gāminī-paṭipadā … bhāvetabban-ti`, translation says "this noble truth of the **cessation of suffering** should be developed." → "this noble truth of the **way leading to the cessation of suffering** should be developed." | A7 | keep (9) |
| 18-24 | 351 |  | Pāḷi (L345) is `dukkha-nirodha-gāminī-paṭipadā … bhāvitan-ti`, translation says "this noble truth of the **origin of suffering** has been developed." → "this noble truth of the **way leading to the cessation of suffering** has been developed." | A7 | keep (9) — per-18:351 still reads "origin" |
| 18-25 | 364 | `dvādasa-` | POS `adj (num)` — unify to one form (see policy D4) | A8-D4 | undecided — owner decision D4; DPD dvādasa 1 = card (supports 517) |
| 18-26 | 364 | `dvādasa-` | POS `adj` → `card` | B-P8 | adjust: per-18:364 `\| dvādasa- \| adj (num) \| \|` → `\| dvādasa- \| card \| \|` (the current POS is `adj (num)`, not `adj`; DPD dvādasa 1: card) (9) |
| 18-27 | 387 | `sadevamanussāya` | `masc.loc.sg` → `fem.loc.sg` — agrees with fem. `pajāya` | A4 | keep (9) — agrees with `pajāya` fem.loc.sg; DPD sadevamanussa: adj, comp |
| 18-28 | 391 | `paccaññāsiṃ` | POS `verbaor.1.s` → `verb`; Grammar `` → `aor.1.sg`  ✔ *Reviewer B proposes the same.* | A5.8 | keep (7) — DPD silent: paccaññāsiṃ (DPD has only paṭijānāti, pr) |
| 18-29 | 400 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.2: ind, conj ("but") |

## 19 — Anupubba-Sikkhā

`per-19-anupubba-sikkha.md` — 39 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 19-01 | 25 |  | `ouseholder or householder's son` → `Householder or householder's son` | A6 | keep (10) |
| 19-02 | 46 | `iti` | Grammar ∅ → `adv` | B-P1 | keep (9) — DPD iti: ind, adv |
| 19-03 | 57 |  | `dirty , lit:` → `dirty, lit:` | A6 | keep (9) |
| 19-04 | 57 | `rajo-patho` | Rebuild row as `\| rajo-patho \| noun \| masc.nom.sg \| dusty, dirty , lit: condition of dust, state of dirt \|` — *POS cell empty (audit only fixes the typo in this row's gloss)* | B-N8 | adjust: per-19:57 `\| rajo-patho \| \| masc.nom.sg \|` → `\| rajo-patho \| noun \| masc.nom.sg \|`: change only the POS cell, because the rebuild as written puts back the `dirty , lit:` typo that 530 fixes (8) |
| 19-05 | 95 |  | POS `idioṃ` → `idiom` | A1 | keep (10) |
| 19-06 | 188 | `samādāya` | Gr `abs` → `ger` | B-N80 | keep (8) — DPD samādāya 2: ger; the same file has `samādāy'eva \| verb \| ger` (per-19:594) |
| 19-07 | 189 | `sikkhassu` | Grammar `imp.ref.2.sg` → `imp.refl.2.sg` | A5.3 | undecided — owner decision A5.3/B11.2; DPD sikkhassu: "imp, reflx 2rd sg" |
| 19-08 | 190 |  | **D8** stray `”` inside the Pāḷi word `sikkhāpadesū'”ti` — remove `”` | A8-D8 | keep (8) — a stray `”` inside a Pāḷi cell is a plain error, not a style choice; the passage at L170 has `sikkhāpadesū'ti` |
| 19-09 | 271 |  | `false speech , lit.` → `false speech, lit.` | A6 | keep (10) |
| 19-10 | 316 | `iti` | Grammar ∅ → `adv` | B-P1 | keep (9) — DPD iti: ind, adv |
| 19-11 | 331 |  | `he is reconciler those who are divided` → `he is a reconciler of those who are divided` | A6 | keep (9) |
| 19-12 | 378 |  | Rebuild row: `\| kālena \| ind \| adv \| timely, at the right moment, at a suitable time, at the proper time \|` | A3 | keep (9) — DPD kālena: ind, adv, "timely; at the right time" |
| 19-13 | 421 |  | Rebuild row: `\| vilepana- \| noun \| \| oil, unguent, ointment, cosmetics, make-up, perfume \|` | A3 | keep (9) — DPD vilepana 1: nt |
| 19-14 | 560 |  | Rebuild row: `\| ukkoṭana- \| noun \| \| taking bribes, bribery, corruption, crooked dealing \|` | A3 | keep (9) — DPD ukkoṭana 1: nt, gloss matches |
| 19-15 | 588 |  | Rebuild row: `\| cīvarena \| noun \| nt.ins.sg \| with robe \|` (embedded tag said `m.ins.s`; cīvara is neuter) | A2 | keep (9) — DPD cīvara 1: nt |
| 19-16 | 592 |  | **Do NOT change** `lit. wherever wherever` (also lines 607, 634) — intentional literal rendering of reduplicated `yena yeneva`. | A6-note | drop: an informational do-not-change note, not a defect (DPD yeneva = sandhi "wherever"; the doubled form is intentional) |
| 19-17 | 618 |  | Rebuild row: `\| evameva kho \| ind \| \| in the same way \|` (currently `\| evameva \| kho \| ind \| in the same way \|` — the particle `kho` slid into the POS cell; it belongs to the Pāḷi lemma) | A2 | adjust: per-19:618 `\| evameva \| kho \| ind \| in the same way \|` → `\| evameva \| sandhi \| \| in the same way \|`: the Pāḷi at L614 is `evameva bhikkhu`, with no `kho`, so `kho` must not join the lemma; DPD evameva = sandhi (use `ind` if BP7 is rejected) (7) |
| 19-18 | 618 |  | Gloss `in the same way` → `ind` — **recommended reject:** Reviewer wiped the gloss (row was already column-shifted); use audit Part 2 rebuild instead. | **B-X5✗** | drop: the reviewer's change wipes the gloss; superseded by 544 |
| 19-19 | 623 |  | Rebuild row: `\| cīvarena \| noun \| nt.ins.sg \| with robe \|` (same) | A2 | keep (9) — same as 542; DPD cīvara 1: nt |
| 19-20 | 774 |  | multi-word POS tag (`v + pn` / `ind+pn` / `ind+m+imp` / `adv+ind`): use `idiom` or `sandhi` per corpus convention (policy D4) | A8-D4 | undecided — owner decision D4; DPD `ehi tvaṃ` = idiom (imp + pron) |
| 19-21 | 783 |  | `you should take a food` → `you should take food` | A6 | keep (9) |
| 19-22 | 803 | `iti` | Grammar ∅ → `adv` | B-P1 | keep (9) — DPD iti: ind, adv |
| 19-23 | 809 | `na-uppādessāmi` | POS `v.caus` → `verb`; Grammar `fut.1.sg` → `fut.1.sg.caus` | A5.9 | keep (8) — DPD uppādeti: pr, caus of uppajjati (the `caus` tag is right) |
| 19-24 | 811 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) — DPD ca 2.1: ind, conj |
| 19-25 | 817 |  | `assistance of holy live` → `assistance of the holy life`; `put an end of former` → `put an end to former`; `a new (painful) sensations` / `a new (painfull) sensations` → `new (painful) sensations`; per-31:71 also `(painfull)` → `(painful)` (2×) *(same fix at: per-19:817, per-31:71)* | A6 | keep (7) — the per-31:71 part was not re-checked |
| 19-26 | 830 | `viharāhi` | `imp.sg.sg` → `imp.2.sg` — typo `sg.sg` | A4 | keep (9) |
| 19-27 | 876 |  | Rebuild row: `\| pādaṃ \| noun \| masc.acc.sg \| foot \|` | A2 | keep (9) — DPD pāda 1: masc; consistent with `pāde` masc.loc.sg at L875 |
| 19-28 | 994 | `upaṭṭhapetvā` | POS `v.caus` → `verb`; Grammar `abs` → `abs.caus` | A5.9 | keep (8) — DPD upaṭṭhapetvā 1: abs of upaṭṭhapeti (√ṭhā *āpe, causative) |
| 19-29 | 996 |  | `Afternoon, he returned` → `In the afternoon, he returned` | A6 | keep (9) |
| 19-30 | 1057 | `kusalesu` | `masc.loc.sg` → `masc.loc.pl` — `-esu` is plural | A4 | keep (10) |
| 19-31 | 1058 | `dhammesu` | `masc.loc.sg` → `masc.loc.pl` — `-esu` is plural | A4 | keep (10) |
| 19-32 | 1123 |  | gloss `these, theṃ` → `these, them` | A1 | keep (10) |
| 19-33 | 1142 |  | `he reaching and dwells` → `he reaches and dwells` | A6 | keep (10) |
| 19-34 | 1168 |  | Rebuild row: `\| khaya- \| noun \| \| exhaustion (of), extinction (of), depletion (of), annihilation (of), destruction (of) \|` | A3 | keep (9) — DPD khaya: masc |
| 19-35 | 1191 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 | undecided — owner decision D8 (per-19:1191 opening quotes missing before each `This is`) |
| 19-36 | 1203 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 | undecided — owner decision D8 (per-19:1203 opening quotes missing) |
| 19-37 | 1232 | `iti` | Grammar ∅ → `adv` | B-P1 | keep (9) — DPD iti: ind, adv, "this is" |
| 19-38 | 1245 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 | undecided — owner decision D8 (per-19:1245 quotes not balanced) |
| 19-39 | 1255 | `kho` | Grammar ∅ → `emph` | B-P3 | keep (9) — DPD kho: ind, emph |

## 20 — Requisites for Awakening

`per-20-requisites-for-awakening.md` — 3 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 20-01 | 20 | `sādhukaṃ` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ duplicates the POS; DPD sādhukaṃ: ind, adv |
| 20-02 | 42 | `lokānukampāya` | Grammar `fem.instr.sg` → `fem.ins.sg` | A5.2 | keep (8) — DPD lokānukampā: fem, abstr, comp (the case was not checked) |
| 20-03 | 58 | `seyyathīdaṃ` | POS `ind` → `sandhi` (leave Grammar empty; reviewer also wrote `sandhi` in Grammar — not recommended) | B-P7 | keep (9) — DPD seyyathīdaṃ: sandhi |

## 21 — The Seven Factors of Awakening

`per-21-the-seven-factors-of-awakening.md` — 19 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 21-01 | 22 | `sammā` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ duplicates the POS; DPD sammā 1: ind, adv |
| 21-02 | 39 | `vimuttiñāṇadassana-` | Grammar `nt` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision A5.7/B11.3; DPD vimuttiñāṇadassana: nt, comp |
| 21-03 | 42 | `api` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ duplicates the POS (DPD api 1.2: ind, no sub-type) |
| 21-04 | 56 | `api` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ duplicates the POS (DPD api 1.2: ind) |
| 21-05 | 59 | `api` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ duplicates the POS (DPD api 1.2: ind) |
| 21-06 | 62 | `api` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ duplicates the POS (DPD api 1.2: ind) |
| 21-07 | 65 | `api` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ duplicates the POS (DPD api 1.2: ind) |
| 21-08 | 68 | `api` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ duplicates the POS (DPD api 1.2: ind) |
| 21-09 | 94 | `ca` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ duplicates the POS; DPD ca 2.1: ind, conj |
| 21-10 | 96 | `ca` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ duplicates the POS; DPD ca 2.1: ind, conj |
| 21-11 | 105 | `tathā` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ duplicates the POS; DPD tathā: ind, adv |
| 21-12 | 120 | `tathā` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ duplicates the POS; DPD tathā: ind, adv |
| 21-13 | 128 | `parivīmaṃsaṃ-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | adjust: per-21:128 `\| parivīmaṃsaṃ- \| noun \| fem \|` → `\| parivīmaṃsaṃ- \| noun \| fem.acc.sg \|`: the word is the object of āpajjati and the hyphen marks sandhi (`parivīmaṃsam'āpajjati`), not a compound member, so B11.3 does not apply (compare `dassanaṃ- \| noun \| nt.acc.sg` at L41); DPD parivīmaṃsā: fem (8). Applies regardless of the B-11.3 policy decision — the Source tag records where Reviewer B's row came from; do not skip this row if the policy 11.3 line is deleted |
| 21-14 | 143 | `parivīmaṃsaṃ-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | adjust: per-21:143 `\| parivīmaṃsaṃ- \| noun \| fem \|` → `\| parivīmaṃsaṃ- \| noun \| fem.acc.sg \|`: the same case as 596 (applies regardless of the B-11.3 policy decision); DPD parivīmaṃsā: fem (8) |
| 21-15 | 150 |  | `there is effort arises without sluggishness` → `effort arises without sluggishness` | A6 | keep (8) |
| 21-16 | 169 | `api` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ duplicates the POS (DPD api 1.2: ind) |
| 21-17 | 172 | `api` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ duplicates the POS (DPD api 1.2: ind) |
| 21-18 | 186 |  | `with relaxed body and who at ease` → `with relaxed body and at ease` | A6 | keep (8) |
| 21-19 | 196 |  | Row rewritten to `ind \| ind <spaces> well, thoroughly, fully \|` — **recommended reject:** Garbled cells; keep the current row (`ind \| \| well, thoroughly, fully`). | **B-X6✗** | drop: ✗ row; current row `\| sādhukaṃ \| ind \| \| well, thoroughly, fully \|` is fine and matches DPD sādhukaṃ (ind, adv) (9) |

## 22 — The Noble Eightfold Path

`per-22-the-noble-eightfold-path.md` — 36 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 22-01 | 13 | `eva` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ row; writing `ind` into Grammar repeats the POS (9) |
| 22-02 | 17 | `seyyathīdaṃ` | POS `ind` → `sandhi` (leave Grammar empty; reviewer also wrote `sandhi` in Grammar — not recommended) | B-P7 | keep (9) |
| 22-03 | 40 | `kho` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ row; writing `ind` into Grammar repeats the POS (9) |
| 22-04 | 47 |  | Rebuild row: `\| dukkhanirodha- \| noun \| \| cessation of suffering, disappearance of suffering \|` | A3 | keep (9) |
| 22-05 | 67 |  | Rebuild row: `\| abyāpāda- \| noun \| \| goodwill, kindness, friendliness, benevolence, lit. not ill-will \|` | A3 | keep (9) |
| 22-06 | 117 | `idha` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ row; writing `ind` into Grammar repeats the POS (9) |
| 22-07 | 119 | `micchā-` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ row; writing `ind` into Grammar repeats the POS (9) |
| 22-08 | 136 | `idha` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ row; writing `ind` into Grammar repeats the POS (9) |
| 22-09 | 152 |  | `he exerts oneself` → `he exerts himself` *(same fix at: per-22:152, per-22:165, per-22:176, per-22:193)* | A6 | keep (9) |
| 22-10 | 165 |  | `he exerts oneself` → `he exerts himself` *(same fix at: per-22:152, per-22:165, per-22:176, per-22:193)* | A6 | keep (9) |
| 22-11 | 176 |  | `he exerts oneself` → `he exerts himself` *(same fix at: per-22:152, per-22:165, per-22:176, per-22:193)* | A6 | keep (9) |
| 22-12 | 176 |  | third right-effort clause: translation says "generates intention for the **arising** of unarisen **worthless, unskilful** states of mind". The Pāḷi for this clause is `anuppannānaṃ kusalānaṃ dhammānaṃ uppādāya` (check table above the line) → "…arising of unarisen **wholesome, skillful** states of mind." | A7 | adjust: per-22:176 `the arising of unarisen worthless, unskilful states of mind` → `the arising of unarisen wholesome, skillful states of mind` (Pāḷi per-22:167 anuppannānaṃ kusalānaṃ dhammānaṃ uppādāya) (9) |
| 22-13 | 190 | `bhāvanāya` | Grammar `fem.instr.sg` → `fem.ins.sg` | A5.2 | keep (7) — DPD silent: case of bhāvanāya (DPD bhāvanā 1 confirms fem only; in `bhāvanāya pāripūriyā` it may be gen, not ins) |
| 22-14 | 193 |  | `he exerts oneself` → `he exerts himself` *(same fix at: per-22:152, per-22:165, per-22:176, per-22:193)* | A6 | keep (9) |
| 22-15 | 213 |  | `strenuous , with` → `strenuous, with` | A6 | keep (9) |
| 22-16 | 218 | `abhijjhā-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision A5.7/B11.3; DPD abhijjhā is fem, so the current tag is factually right |
| 22-17 | 230 |  | `a monk stay with` → `a monk stays with` | A6 | keep (9) |
| 22-18 | 236 | `citte` | `masc.loc.pl` → `nt.loc.sg` — citta is neuter; loc. singular | A4 | keep (9) |
| 22-19 | 252 |  | `this moks is called` → `this monks is called` | A6 | keep (9) |
| 22-20 | 259 | `ca` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ row; writing `ind` into Grammar repeats the POS (9) |
| 22-21 | 270 | `idha` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ row; writing `ind` into Grammar repeats the POS (9) |
| 22-22 | 274 | `eva` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ row; writing `ind` into Grammar repeats the POS (9) |
| 22-23 | 295 |  | `he attaining and remains` → `he attains and remains` *(same fix at: per-22:295, per-22:316, per-22:347, per-22:371)* | A6 | keep (9) |
| 22-24 | 316 |  | `he attaining and remains` → `he attains and remains` *(same fix at: per-22:295, per-22:316, per-22:347, per-22:371)* | A6 | keep (9) |
| 22-25 | 323 | `ca` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ row; writing `ind` into Grammar repeats the POS (9) |
| 22-26 | 326 | `ca` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ row; writing `ind` into Grammar repeats the POS (9) |
| 22-27 | 329 | `ca` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ row; writing `ind` into Grammar repeats the POS (9) |
| 22-28 | 332 | `ca` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ row; writing `ind` into Grammar repeats the POS (9) |
| 22-29 | 336 |  | gloss `hiṃ` (row `\| taṃ \| pron \| masc.acc.sg \| hiṃ \|`) → `him` | A1 | keep (9) |
| 22-30 | 347 |  | `he attaining and remains` → `he attains and remains` *(same fix at: per-22:295, per-22:316, per-22:347, per-22:371)* | A6 | keep (9) |
| 22-31 | 354 | `ca` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ row; writing `ind` into Grammar repeats the POS (9) |
| 22-32 | 357 | `ca` | reviewer wrote `ind` into Grammar of this `ind` row — **recommended reject** (duplicate) | **B-X1✗** | drop: ✗ row; writing `ind` into Grammar repeats the POS (9) |
| 22-33 | 359 |  | Rebuild row: `\| pubb'eva \| ind \| \| just in front of, just before, previous, as before, as earlier \|` | A3 | adjust: DPD pubbeva is sandhi (adv + ind), not ind. per-22:359 `\| pubb'eva \| ind \| just in front of, just before, previous \| as before, as earlier \|` → `\| pubb'eva \| sandhi \| \| just in front of, just before, previous, as before, as earlier \|` (8) |
| 22-34 | 363 |  | Rebuild row: `\| upekkhā- \| noun \| \| mental poise, mental balance, equanimity, composure \|` | A3 | keep (9) |
| 22-35 | 364 |  | Rebuild row: `\| sati- \| noun \| \| mindfulness, presence, recollection, awareness \|` | A3 | keep (9) |
| 22-36 | 371 |  | `he attaining and remains` → `he attains and remains` *(same fix at: per-22:295, per-22:316, per-22:347, per-22:371)* | A6 | keep (9) |

## 23 — Mindfulness of Breathing

`per-23-mindfulness-of-breathing.md` — 29 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 23-01 | 32 |  | `it is fills up` → `it fills up` | A6 | keep (9) |
| 23-02 | 44 | `paripūreti` | `pr.3.pl` → `pr.3.sg` — 3.sg form; also fix gloss "fill up" → "fills up" | A4 | adjust: the passage (per-23:34) has paripūrenti with a plural subject, so the Pāḷi word is wrong, not the tag. per-23:44 `\| paripūreti \| verb \| pr.3.pl \| fill up, suffuse, lit. cause to fill \|` → `\| paripūrenti \| verb \| pr.3.pl \| fill up, suffuse, lit. cause to fill \|` (8) |
| 23-03 | 85 | `upaṭṭhapetvā` | POS `v.caus` → `verb`; Grammar `abs` → `abs.caus` | A5.9 | keep (7) |
| 23-04 | 87 |  | translation `in front of hiṃ` → `in front of him` | A1 | keep (9) |
| 23-05 | 107 | `assasāmī'ti` | `pr.3.sg` → `pr.1.sg` — "-āmi" = 1st sg ("I breathe in") | A4 | keep (9) |
| 23-06 | 110 |  | `I'm breath in deeply.` / `I'm breath out deeply.` / `…shortly.` → `I breathe in deeply.` / `I breathe out deeply.` / `…shortly.` *(same fix at: per-23:110, per-23:121, per-23:134, per-23:145)* | A6 | keep (9) |
| 23-07 | 118 | `passasāmī'ti` | `pr.3.sg` → `pr.1.sg` — same; also gloss "I breathes out" → "I breathe out" | A4 | keep (9) |
| 23-08 | 121 |  | `I'm breath in deeply.` / `I'm breath out deeply.` / `…shortly.` → `I breathe in deeply.` / `I breathe out deeply.` / `…shortly.` *(same fix at: per-23:110, per-23:121, per-23:134, per-23:145)* | A6 | keep (9) |
| 23-09 | 131 | `assasāmī'ti` | `pr.3.sg` → `pr.1.sg` — same | A4 | keep (9) |
| 23-10 | 134 |  | `I'm breath in deeply.` / `I'm breath out deeply.` / `…shortly.` → `I breathe in deeply.` / `I breathe out deeply.` / `…shortly.` *(same fix at: per-23:110, per-23:121, per-23:134, per-23:145)* | A6 | keep (9) |
| 23-11 | 142 | `passasāmī'ti` | `pr.3.sg` → `pr.1.sg` — same | A4 | keep (9) |
| 23-12 | 145 |  | `I'm breath in deeply.` / `I'm breath out deeply.` / `…shortly.` → `I breathe in deeply.` / `I breathe out deeply.` / `…shortly.` *(same fix at: per-23:110, per-23:121, per-23:134, per-23:145)* | A6 | keep (9) |
| 23-13 | 154 | `assasissāmī'ti` | `fut.3.sg` → `fut.1.sg` — "-ssāmi" = 1st sg | A4 | keep (9) |
| 23-14 | 157 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 | undecided — owner decision D8 (line ends with ” and has no opening quote) |
| 23-15 | 164 | `passasissāmī'ti` | `fut.3.sg` → `fut.1.sg` — same | A4 | keep (9) |
| 23-16 | 167 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 | undecided — owner decision D8 |
| 23-17 | 173 | `passambhayaṃ` | POS `prp.caus` → `prp`; Grammar `masc.nom.sg` → `masc.nom.sg.caus` | A5.9 | keep (9) |
| 23-18 | 174 | `kāya-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision A5.7/B11.3; DPD kāya is masc, so the current tag is factually right |
| 23-19 | 176 | `assasissāmī'ti` | `fut.3.sg` → `fut.1.sg` — same | A4 | keep (9) |
| 23-20 | 179 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 | undecided — owner decision D8 |
| 23-21 | 183 | `passambhayaṃ` | POS `prp.caus` → `prp`; Grammar `masc.nom.sg` → `masc.nom.sg.caus` | A5.9 | keep (9) |
| 23-22 | 184 | `kāya-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision A5.7/B11.3; DPD kāya is masc |
| 23-23 | 186 | `passasissāmī'ti` | `fut.3.sg` → `fut.1.sg` — same | A4 | keep (9) |
| 23-24 | 189 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 | undecided — owner decision D8 |
| 23-25 | 195 | `pīti-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision A5.7/B11.3; DPD pīti 1.1 is fem |
| 23-26 | 213 |  | `breathe out experiences mental activity` → `breathe out experiencing mental activity` | A6 | keep (9) |
| 23-27 | 220 |  | gloss `causing to be calṃ` → `causing to be calm` | A1 | keep (9) |
| 23-28 | 229 | `citta-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision A5.7/B11.3; if the gender is kept, DPD citta is nt, so per-23:229 `masc` → `nt` |
| 23-29 | 231 |  | `breathe in experiences the mind` and `breathe out experiences the mind` → `experiencing` (2×) | A6 | keep (9) |

## 24 — Dependent Origination

`per-24-dependent-origination.md` — 12 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 24-01 | 13 | `\>avijjā-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision A5.7/B11.3; DPD avijjā is fem |
| 24-02 | 14 | `\>paccayā` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision A5.7/B11.3 (DPD paccayā is ind adv, abl sg of paccaya; paccaya itself is not in the dump) |
| 24-03 | 45 |  | Rebuild row: `\| dukkhadomanass- \| noun \| \| pain and stress, physical pain and mental suffering \|` | A3 | keep (8) |
| 24-04 | 49 |  | `becoming arise` → `becoming arises`; `birth arise` → `birth arises` *(same fix at: per-24:49, per-66:145)* | A6 | keep (9) |
| 24-05 | 84 |  | Rebuild row: `\| dukkhanirodha- \| noun \| \| cessation of suffering, disappearance of suffering \|` | A3 | keep (9) |
| 24-06 | 164 |  | `the sphere of the sphere of the formless` → `the sphere of the formless` | A6 | keep (9) |
| 24-07 | 383 |  | Rebuild row: `\| duvidhena \| ind \| adv \| in two ways; as of two kinds; in a twofold way \|` (also drop the stray `–` after the Pāḷi word) | A3 | keep (8) |
| 24-08 | 456 |  | `non-perseption` → `non-perception` | A6 | keep (9) |
| 24-09 | 579 |  | Rebuild row: `\| diṭṭhi- \| noun \| \| view, belief, opinion, concept, theory, attitude \|` (drop the duplicated "opinion") | A3 | keep (9) |
| 24-10 | 597 |  | `of one who endowed with` → `of one who is endowed with` *(same fix at: per-24:597, per-24:624)* | A6 | keep (9) |
| 24-11 | 624 |  | `of one who endowed with` → `of one who is endowed with` *(same fix at: per-24:597, per-24:624)* | A6 | keep (9) |
| 24-12 | 699 |  | `for affected by` → `for one affected by`; `for endowed all kinds` → `for one endowed with all kinds`; `for affected by all kinds` → `for one affected by all kinds` | A6 | keep (8) |

## 25 — The Dhamma in Brief

`per-25-the-dhamma-in-brief.md` — 4 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 25-01 | 30 |  | `Bhessed One` → `Blessed One` (3×) | A6 | keep (9) |
| 25-02 | 43 |  | `whatever , that which` → `whatever, that which` | A6 | keep (9) |
| 25-03 | 53 | `vihareyyaṃ-` | Grammar `opt.ref.1.sg` → `opt.refl.1.sg` | A5.3 | undecided — owner decision A5.3/B11.2 (`ref` is a typo under either option: `opt.refl.1.sg` or `opt.1.sg`) |
| 25-04 | 66 | `gotamī` | Grammar `fem.v.sg` → `fem.voc.sg` | A5.6 | keep (9) |

## 26 — The Four Great References

`per-26-the-four-great-references.md` — 7 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 26-01 | 44 |  | `Here a monks could say` → `Here a monk could say` | A6 | keep (9) |
| 26-02 | 65 |  | `certan` → `certain` (3×); `heared` → `heard` (3×) *(same fix at: per-26:65, per-26:91, per-26:95)* | A6 | keep (9) |
| 26-03 | 83 |  | **D6** `tesaṃ` tagged masc.gen.sg, gloss "of that" — form is plural; check context: gloss may need "of those". | A8-D6 | adjust: DPD tesaṃ 2 is masc & nt gen pl. per-26:83 `\| tesaṃ \| pron \| masc.gen.sg \| of that \|` → `\| tesaṃ \| pron \| masc.gen.pl \| of those \|`; per-26:91 `that elders` → `those elders` (9) |
| 26-04 | 91 |  | `certan` → `certain` (3×); `heared` → `heard` (3×) *(same fix at: per-26:65, per-26:91, per-26:95)* | A6 | keep (9) |
| 26-05 | 95 |  | `certan` → `certain` (3×); `heared` → `heard` (3×) *(same fix at: per-26:65, per-26:91, per-26:95)* | A6 | keep (9) |
| 26-06 | 173 | `h'etaṃ` | POS `ind+pn` — unify to one form (see policy D4) | A8-D4 | undecided — owner decision D4 (POS form for `ind+pn`; DPD has no h'etaṃ headword) |
| 26-07 | 173 |  | multi-word POS tag (`v + pn` / `ind+pn` / `ind+m+imp` / `adv+ind`): use `idiom` or `sandhi` per corpus convention (policy D4) | A8-D4 | drop: duplicate of 724 (same row, same D4 item) (8) |

## 27 — Principles of Cordiality

`per-27-principles-of-cordiality.md` — 12 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 27-01 | 12 |  | POS `idioṃ` → `idiom` | A1 | keep (9) |
| 27-02 | 12 |  | POS stays `idioṃ`, Grammar → `idiom, card + masc` — **recommended reject:** Descriptive text in Grammar; use audit Part 1 (`idioṃ` → `idiom`, Grammar ∅). | **B-X7✗** | drop: ✗ row; it puts descriptive text in Grammar, and 733 already fixes the cell (9) |
| 27-03 | 68 |  | `for a monks` → `for a monk` | A6 | keep (9) |
| 27-04 | 80 |  | Rebuild row: `\| antamaso \| ind \| \| even so much as, even with, even down to, with as little as \|`  ✔ *Reviewer B proposes the same.* | A3 | keep (9) |
| 27-05 | 82 |  | Rebuild row: `\| pariyāpanna- \| adj \| \| gone completely into, included in, belonging to, got into \|` (also drop the stray `”`)  ✔ *Reviewer B proposes the same.* | A3 | keep (9) |
| 27-06 | 89 |  | Rebuild row: `\| appaṭivibhatta- \| adj \| \| not dividing for oneself, without reservations, not without sharing with others \|` (also fixes typo "onself")  ✔ *Reviewer B proposes the same row, but keeps the gloss "not for oneself dividing".* | A3 | keep (8) |
| 27-07 | 111 |  | Rebuild row: `\| samādhi- \| noun \| \| perfect peace of mind, stability of mind, stillness of mind \|`  ✔ *Reviewer B proposes the same.* | A3 | keep (9) |
| 27-08 | 119 |  | POS `idioṃ` → `idiom` | A1 | keep (10) |
| 27-09 | 138 |  | Rebuild row: `\| diṭṭhi- \| noun \| \| view, belief, opinion, concept, theory, attitude \|` (drop duplicated "opinion")  ✔ *Reviewer B proposes the same row but keeps the duplicated "opinion".* | A3 | keep (9) |
| 27-10 | 142 |  | POS `idioṃ` → `idiom` | A1 | keep (10) |
| 27-11 | 157 | `cha` | `Grammar pl` → `x.nom.pl` — match corpus numeral convention | A4 | adjust: per-27:157 `\| cha \| card \| pl \|` → `\| cha \| card \| x.acc.pl \|`. DPD has cha as `card, x pl`, and in the chant cha is the object with `dhamme` (masc.acc.pl), so x.nom.pl is wrong (8) |
| 27-12 | 170 | `no` | Gr `interr` → ∅ — *DPD: `no` is plain ind* | B-N81 | drop: DPD no 1.2 is ind, interr "(adds a question mark)"; the chant line is a question, so `interr` is right (9) |

## 28 — Principles of Non-Decline

`per-28-principles-of-non-decline.md` — 8 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 28-01 | 30 | `sannipāta-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision B11.3/A5.7. DPD: sannipāta is masc |
| 28-02 | 63 |  | `perferm` → `perform` | A6 | keep (10) |
| 28-03 | 82 |  | Rebuild row: `\| yathā- \| ind \| \| like, as, according to, on account of, because of, how \|`  ✔ *Reviewer B proposes the same.* | A3 | keep (9) |
| 28-04 | 88 |  | `as they has beed formulated` → `as they have been formulated` | A6 | keep (10) |
| 28-05 | 174 |  | Rebuild row: `\| kinti \| ind \| interr \| how then? in what way? \|` (Grammar had truncated `inter`) | A3 | keep (8) |
| 28-06 | 187 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 | undecided — owner decision D8. Line 187 ends in `”` with no opening quote in the line |
| 28-07 | 220 |  | `seven seven principles` → `seven principles` | A6 | keep (10) |
| 28-08 | 230 |  | Rebuild row: `\| pāṭikaṅkhā \| adj \| fem.nom.sg \| to be expected (for), certain (for), should be expected, can be anticipated \|` | A2 | adjust: DPD pāṭikaṅkha is ptp of paṭikaṅkhati, not adj. per-28:230 `\| pāṭikaṅkhā \| \| adj \| f.n.s to be expected (for), certain (for), should be expected, can be anticipated \|` → `\| pāṭikaṅkhā \| ptp \| fem.nom.sg \| to be expected (for), certain (for), should be expected, can be anticipated \|` (8) |

## 29 — Striving According to the Dhamma

`per-29-striving-according-to-the-dhamma.md` — 6 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 29-01 | 47 |  | `to arose energy` → `to arouse energy` | A6 | keep (10) |
| 29-02 | 281 |  | gloss `of theṃ` → `of them` | A1 | keep (10) |
| 29-03 | 284 | `amhesu` | `masc.loc.sg` → `1.loc.pl` — "in us", plural | A4 | keep (10) |
| 29-04 | 286 | `bhavissanti` | `POS pt` → `POS verb` — Grammar fut.3.pl already correct | A4 | keep (9) |
| 29-05 | 289 |  | `grate result and grate merit` → `great result and great merit` | A6 | keep (10) |
| 29-06 | 329 | `ubhaya-` | POS `pron` → `adj` — *adj (from `ubha`)* | B-N111 | keep (9) |

## 30 — The Buddha's Final Instruction

`per-30-the-buddhas-final-instruction.md` — 5 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 30-01 | 12 | `siyā` | Grammar `opt.3rd.sg` → `opt.3.sg` | A5.1 | keep (9) |
| 30-02 | 14 | `tumhākaṃ` | Grammar `2nd.dat.pl` → `2.dat.pl` | A5.1 | keep (9) |
| 30-03 | 29 | `no` | Grammar `1st.dat.pl` → `1.dat.pl` | A5.1 | keep (9) |
| 30-04 | 52 | `accayena` | ⚔ **C11 — keep ONE:** **Option A (audit)** Part 3: Grammar empty, full gloss incl. `lit. with gone past`  ·  **Option B (reviewer)** Grammar `adv`; reviewer's gloss is truncated (drops `, lit. with gone past`)  ·  *If B is chosen, apply only the Grammar `adv` and keep A's full gloss.* | B-C11 | undecided |
| 30-05 | 79 |  | `condition phenomena are of the liable to disintegrate` → `conditioned phenomena are liable to disintegrate`; `This is final statement` → `This is the final statement` | A6 | keep (9) |

## 31 — The Four Requisites

`per-31-the-four-requisites.md` — 21 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 31-01 | 21 | `ḍaṃsa-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision B11.3/A5.7. DPD: ḍaṃsa is masc |
| 31-02 | 22 | `makasa-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision B11.3/A5.7. DPD: makasa is masc |
| 31-03 | 23 | `vāt'ātapa-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision B11.3/A5.7. DPD: vātātapa is masc, comp |
| 31-04 | 24 | `siriṃsapa-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision B11.3/A5.7. DPD: siriṃsapa is masc (siriṃsapa 2 is nt) |
| 31-05 | 30 |  | **D6** `\| attha \| noun \| masc.acc.sg \|` — bare `attha` cannot be acc.sg; chant probably has sandhi `…paṭicchādan'atthaṃ`. Suggest `atthaṃ` with a sandhi note; verify. | A8-D6 | adjust: per-31:30 `\| attha \| noun \| masc.acc.sg \|` → `\| atthaṃ \| noun \| masc.acc.sg \|`. The chant has `paṭicchādan'atthaṃ`, and per-31:97 uses the same `atthaṃ` row. DPD also lists `atthaṃ` as ind, adv, in comps, "for the sake of" (8) |
| 31-06 | 32 |  | `for ward off heat, for ward off the touch` → `to ward off heat, to ward off the touch` *(same fix at: per-31:32, per-31:99)* | A6 | keep (10) |
| 31-07 | 41 | `piṇḍapātaṃ` | Gr `masc` → `masc.acc.sg` — *grammar was only `masc`* | B-N58 | keep (9) |
| 31-08 | 53 | `vihiṃsa-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision B11.3/A5.7. vihiṃsa is not in the DPD file |
| 31-09 | 55 | `brahmacariya-` | Grammar `nt` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision B11.3/A5.7. DPD: brahmacariya is nt |
| 31-10 | 63 | `na-uppādessāmi` | POS `v.caus` → `verb`; Grammar `fut.1.sg` → `fut.1.sg.caus` | A5.9 | keep (9) |
| 31-11 | 71 |  | `assistance of holy live` → `assistance of the holy life`; `put an end of former` → `put an end to former`; `a new (painful) sensations` / `a new (painfull) sensations` → `new (painful) sensations`; per-31:71 also `(painfull)` → `(painful)` (2×) *(same fix at: per-19:817, per-31:71)* | A6 | keep (8) — the per-19:817 part was not re-checked |
| 31-12 | 86 | `ḍaṃsa-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision B11.3/A5.7. DPD: ḍaṃsa is masc |
| 31-13 | 87 | `makasa-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision B11.3/A5.7. DPD: makasa is masc |
| 31-14 | 88 | `vātātapa-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision B11.3/A5.7. DPD: vātātapa is masc |
| 31-15 | 89 | `siriṃsapa-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision B11.3/A5.7. DPD: siriṃsapa is masc |
| 31-16 | 93 |  | Rebuild row: `\| utuparissaya- \| noun \| \| inclement weather, harsh climate, lit. danger of the season \|`  ✔ *Reviewer B proposes the same.* | A3 | keep (9) |
| 31-17 | 95 |  | Rebuild row: `\| paṭisallāna- \| noun \| \| privacy, seclusion, solitude, lit. sticking to oneself \|` | A3 | keep (9) |
| 31-18 | 96 |  | Rebuild row: `\| ārāma- \| noun \| \| enjoyment, delight, pleasure \|` (current has corrupted "pleasureenjoyment" in Grammar + "delight, pleasure" in English) | A3 | keep (9) |
| 31-19 | 99 |  | `for ward off heat, for ward off the touch` → `to ward off heat, to ward off the touch` *(same fix at: per-31:32, per-31:99)* | A6 | keep (10) |
| 31-20 | 99 |  | `for the sake of removal the danger` → `for the sake of removal of the danger` | A6 | keep (9) |
| 31-21 | 118 | `paramatāyā` | `masc.dat.sg` → `fem.dat.sg` — paramatā is feminine | A4 | keep (9) |

## 32 — The Repulsiveness of Food

`per-32-the-repulsiveness-of-food.md` — 2 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 32-01 | 18 |  | `of living , abiding` → `of living, abiding` | A6 | keep (10) |
| 32-02 | 29 |  | `does not drawn towards it` → `is not drawn towards it` | A6 | keep (10) |

## 33 — Universal Well-Being

`per-33-universal-well-being.md` — 5 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 33-01 | 20 |  | gloss `calṃ lit. not trembling` → `calm, lit. not trembling` | A1 | keep (10) |
| 33-02 | 46 |  | gloss `calṃ lit. not trembling` → `calm, lit. not trembling` | A1 | keep (10) |
| 33-03 | 71 |  | `may all beings do not lost gained fortune` → `may all beings not lose their gained fortune` | A6 | keep (9) |
| 33-04 | 80 | `sakā-` | POS `noun` → `adj` | B-N112 | keep (8) |
| 33-05 | 88 | `paṭisaraṇoā` | Word `paṭisaraṇoā` → `paṭisaraṇā` — *obvious typo: chant has `kammapaṭisaraṇā`* | B-N131 | keep (10) |

## 34 — The Divine Abidings

`per-34-the-divine-abidings.md` — 8 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 34-01 | 13 | `sahagatena` | Grammar `nt.i.sg` → `nt.ins.sg`  ✔ *Reviewer B proposes the same.* | A5.6 | adjust: per-34:13 `\| sahagatena \| pp \| nt.i.sg \|` → `\| sahagatena \| adj \| masc.ins.sg \|`. DPD sahagata is adj, comp, and it agrees with cetasā, which DPD gives as masc (8) |
| 34-02 | 14 | `cetasā` | Grammar `nt.i.sg` → `nt.ins.sg`  ✔ *Reviewer B proposes the same.* | A5.6 | adjust: per-34:14 `\| cetasā \| noun \| nt.i.sg \|` → `\| cetasā \| noun \| masc.ins.sg \|`. DPD: cetasā is "masc, instr sg of cetas", which matches per-32:16 (8) |
| 34-03 | 43 | `sabbattatāya` | POS `adj` → `ind`; Gr `masc.dat.sg` → `adv`; Eng `to all encompassing, all pervading lit. all spread out` → `to all beings; encompassing all living beings` | B-N113 | keep (9) |
| 34-04 | 51 |  | Rebuild row: `\| sabbāvantaṃ \| adj \| masc.acc.sg \| entire, whole \|`  ✔ *Reviewer B proposes the same.* | A2 | keep (9) |
| 34-05 | 53 | `mettāsahagatena` | Word `mettāsahagatena` → `mettā-sahagatena` — *chant line has `mettā-sahagatena` (hyphen); row should match* | B-N132 | keep (8) |
| 34-06 | 59 |  | Rebuild row: `\| abyāpajjena \| adj \| nt.ins.sg \| without ill will, with goodwill \|`  ✔ *Reviewer B proposes the same.* | A2 | adjust: per-34:59 `\| abyāpajjena \| \| adj \| nt.ins.s without ill will, with goodwill \|` → `\| abyāpajjhena \| adj \| masc.ins.sg \| without ill will, with goodwill \|`. DPD abyāpajjha 2.2 is adj "free from ill will"; this combines with 847 (the chant spelling `abyāpajjhena`); the gender follows cetasā (8) |
| 34-07 | 59 | `abyāpajjena` | Word `abyāpajjena` → `abyāpajjhena` — *amends audit Part 2 row for 34:59; chant line 34:47 already reads `abyāpajjhena`* | B-N135 | drop: superseded by 34-06 (same cell) — its rebuild already changes `abyāpajjena` → `abyāpajjhena`; implement 34-07 only if 34-06 is rejected (9) |
| 34-08 | 61 | `viharati;` | Word `viharati;` → `viharati` — *stray `;`* | B-N133 | keep (8) |

## 35 — Five Subjects for Frequent Recollection

`per-35-five-subjects-for-frequent-recollection.md` — 6 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 35-01 | 12 | `jarā-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision B11.3/A5.7. DPD: jarā is fem |
| 35-02 | 24 | `byādhi-` | Grammar `nt` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision B11.3/A5.7. DPD: byādhi is masc, so if the bare gender is kept, `nt` → `masc` |
| 35-03 | 30 |  | `of the nature to sick` → `of the nature to sicken` | A6 | keep (8) |
| 35-04 | 55 |  | `from all that dear and pleasing` → `from all that is dear and pleasing` *(same fix at: per-35:55, per-36:88)* | A6 | keep (9) |
| 35-05 | 63 | `sako-` | POS `noun` → `adj` | B-N114 | keep (8) |
| 35-06 | 90 | `evaṃ` | Grammar ∅ → `adv` | B-P1 | keep (9) |

## 36 — Ten Subjects for Frequent Recollection by One Who Has Gone Forth

`per-36-ten-subjects-for-frequent-recollection-by-one-who-has-gone-forth.md` — 16 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 36-01 | 22 |  | `these are ten principles should often be reflected` → `these ten principles should often be reflected` | A6 | keep (9) |
| 36-02 | 28 | `vevaṇṇiya-` | ⚔ **C7 — keep ONE:** **Option A (audit)** Part 3: POS stays `adj`  ·  **Option B (reviewer)** POS `adj` → `noun`  ·  *Grammar empty in both; gloss merge identical.* | B-C7 | undecided |
| 36-03 | 60 | `kacci` | Grammar ∅ → `interr` | B-P6 | keep (9) |
| 36-04 | 61 | `nu kho` | Grammar ∅ → `interr` | B-P6 | keep (9) |
| 36-05 | 66 | `upavadatī'ti` | `pr.3.pl` → `pr.3.sg` — `-ti` singular; gloss is singular too | A4 | keep (9) |
| 36-06 | 74 | `kacci` | Grammar ∅ → `interr` | B-P6 | keep (9) |
| 36-07 | 75 | `nu kho` | Grammar ∅ → `interr` | B-P6 | keep (9) |
| 36-08 | 88 |  | `from all that dear and pleasing` → `from all that is dear and pleasing` *(same fix at: per-35:55, per-36:88)* | A6 | keep (9) |
| 36-09 | 104 |  | `How my days and nights pass?` → `How do my days and nights pass?` | A6 | keep (9) |
| 36-10 | 110 | `kacci` | Grammar ∅ → `interr` | B-P6 | keep (9) |
| 36-11 | 111 | `nu kho` | Grammar ∅ → `interr` | B-P6 | keep (9) |
| 36-12 | 124 | `nu kho` | Grammar ∅ → `interr` | B-P6 | keep (9) |
| 36-13 | 125 | `me` | Grammar `1.instr.sg` → `1.ins.sg` | A5.2 | keep (9) |
| 36-14 | 126 | `uttari-` | Rebuild row as `\| uttari- \| adj \| \| over; beyond; further; moreover; additional \|` | B-N9 | adjust: per-36:126 `\| uttari- \| \| \| over; beyond; further; moreover; additional \|` → `\| uttari- \| adj \| \| superior; higher; beyond \|`. DPD uttari 1.1 is adj, "superior; supreme; better; higher"; the current gloss is the ind, adv sense (7) |
| 36-15 | 140 | `na` | Rebuild row as `\| na \| ind \| \| not \|` | B-N10 | keep (10) |
| 36-16 | 148 |  | `these is ten principles should often be reflected` → `these ten principles should often be reflected` | A6 | keep (9) |

## 37 — The Thirty-Two Parts

`per-37-the-thirty-two-parts.md` — 6 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 37-01 | 7 |  | **D9** sutta reference `[dn 22.5]` → `[DN 22.5]` (match `[SN 56.11]`, `[MN 27 / 38 / 51]` style) | A8-D9 | keep (8) |
| 37-02 | 22 | `pariyantaṃ` | Gr `masc.acc.sg` → `masc.nom.sg`; Word `pariyantaṃ` → `pariyanto` — *chant line has `taca-pariyanto` (nom.)* | B-N134 | keep (9) |
| 37-03 | 33 | `atthi` | `pres.3.pl` → `pr.3.sg` — normalize `pres`; atthi is 3.sg (used with plural list) | A4 | adjust: per-37:33 `\| atthi \| verb \| pres.3.pl \|` → `\| atthi \| verb \| pr.3.pl \|`. DPD atthi 1.2 is "pr 3rd pl of atthi, there are; they are", so normalise `pres` only and keep pl (8) |
| 37-04 | 55 |  | **D1** Delete this duplicate row `\| matthaluṅgaṃ \| noun \| nt.nom.sg \| the brain \|` (chant line lists it once, at the end), and delete the first "brain" in the translation line (L70). Needs approval (data-preservation rule).  ✔ *Reviewer B also deleted this row.* | A8-D1 | undecided — owner decision D1 (deleting a row falls under the data-preservation rule). The source confirms that chant line 29 has matthaluṅgan'ti only at the end and that row 68 already covers it |
| 37-05 | 57 |  | gloss `phlegṃ` → `phlegm` | A1 | keep (10) |
| 37-06 | 70 |  | **D1** (part 2) remove the first "brain" from this translation line. | A8-D1 | undecided — owner decision D1, same as 895. "brain" really appears twice in L70 |

## 38 — Recollection of Impermanence

`per-38-recollection-of-impermanence.md` — 7 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 38-01 | 59 | `avassaṃ` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 38-02 | 63 |  | **D10** `inevitable by me to be dead` — literal but broken English; recommend "my death is unavoidable" (verify against the Pāḷi line and neighbouring lines). | A8-D10 | adjust: per-38:63 `**inevitable by me to be dead**` → `**inevitably I have to die**`. DPD: avassaṃ is ind, adv, "inevitably" (7) |
| 38-03 | 100 | `vata` | Grammar ∅ → `excl` | B-P4 | adjust: per-38:100 `\| vata \| ind \| \|` → `\| vata \| ind \| emph \|`. The gloss `indeed` matches DPD vata 1.2 (ind, emph, "certainly; surely; indeed"), not 1.1 excl (7) |
| 38-04 | 103 | `aciraṃ` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 38-05 | 113 |  | `on the the ground` → `on the ground` | A6 | keep (10) |
| 38-06 | 120 | `vata` | Grammar ∅ → `excl` | B-P4 | adjust: per-38:120 `\| vata \| ind \| \|` → `\| vata \| ind \| emph \|`. Same as 907: the gloss `indeed` is the DPD vata 1.2 emph sense (7) |
| 38-07 | 150 | `sukho` | POS `noun` → `adj` | B-N115 | keep (9) |

## 39 — DhammacakkappavattanaSutta

`per-39-dhammacakkappavattana-sutta.md` — 13 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 39-01 | 3 |  | **D9** Title `DhammacakkappavattanaSutta` → `Dhammacakkappavattana-Sutta` | A8-D9 | undecided — owner decision: title style. DPD headword is one word, `dhammacakkappavattanasutta`; the only defect is the capital S inside the word |
| 39-02 | 21 | `isipatane` | `(English cell empty)` → `add gloss in Isipatana` — missing gloss | A4 | keep (8) |
| 39-03 | 22 | `migadāye` | `masc.gen.sg, English empty` → `masc.loc.sg + gloss in the Deer Park` — locative; missing gloss | A4 | keep (9) |
| 39-04 | 28 | `tatra` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 39-05 | 29 | `kho` | Grammar ∅ → `emph` | B-P3 | keep (9) |
| 39-06 | 48 | `te` | Rebuild row as `\| te \| pron \| masc.nom.pl \| those \|` — *columns shifted; audit Part 2 missed this row; abbreviation `m.n.pl`* | B-N11 | keep (9) |
| 39-07 | 89 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 | undecided — owner decision D5 (line 89 is a word-breakdown label `>mahārājā + ikā`, not a chant line) |
| 39-08 | 97 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 | undecided — owner decision D5 |
| 39-09 | 103 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 | undecided — owner decision D5 |
| 39-10 | 109 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 | undecided — owner decision D5 |
| 39-11 | 117 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 | undecided — owner decision D5 |
| 39-12 | 129 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 | undecided — owner decision D5 |
| 39-13 | 137 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 | undecided — owner decision D5 |

## 40 — Anatta-Lakkhaṇa-Sutta

`per-40-anatta-lakkhana-sutta.md` — 46 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 40-01 | 11 | `evaṃ-` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 40-02 | 12 | `me` | `masc.ins.sg` → `1.ins.sg` — personal pronoun convention (digit person) | A4 | keep (9) |
| 40-03 | 13 | `sutaṃ` | `masc.acc.sg` → `nt.nom.sg` — `evaṃ me sutaṃ` = "thus it was heard by me" (pp as nt. subject) | A4 | keep (7) — DPD silent: sutaṃ (DPD suta 1.1 confirms pp only, not the case) |
| 40-04 | 19 |  | `in jetavana (jets's grove)` → `in Jetavana (Jeta's grove)` | A6 | keep (9) |
| 40-05 | 23 |  | `in sāvatthi in jets's grove in anāthapindika's park` → `in Sāvatthī in Jeta's Grove in Anāthapiṇḍika's park` | A6 | keep (9) |
| 40-06 | 27 | `tatra` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 40-07 | 28 | `kho` | Grammar ∅ → `emph` | B-P3 | keep (9) |
| 40-08 | 52 |  | POS `idioṃ` → `idiom` | A1 | keep (9) |
| 40-09 | 59 |  | `onself` → `oneself` *(same fix at: per-40:59, per-40:72, per-40:94, per-40:107, per-40:124, per-40:137)* | A6 | keep (9) |
| 40-10 | 59 | `labbhetha` | POS `v.pass` → `verb`; Grammar `opt.refl.3.sg` → `opt.refl.3.sg.pass` | A5.9 | keep (7) |
| 40-11 | 60 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) |
| 40-12 | 62 | `evaṃ` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 40-13 | 66 | `evaṃ` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 40-14 | 72 |  | `than form/feeling/perception/volitional formations could not` → `then …` (4×) *(same fix at: per-40:72, per-40:94, per-40:107, per-40:124)* | A6 | adjust: per-40:72 `than form could not` → `then form could not` (9) |
| 40-15 | 72 |  | `onself` → `oneself` *(same fix at: per-40:59, per-40:72, per-40:94, per-40:107, per-40:124, per-40:137)* | A6 | keep (9) |
| 40-16 | 78 | `yasmā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 40-17 | 79 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) |
| 40-18 | 80 | `kho` | Grammar ∅ → `emph` | B-P3 | keep (9) |
| 40-19 | 82 | `tasmā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 40-20 | 83 | `no labbhati` | POS `v.pass` → `verb`; Grammar `pr.3.sg` → `pr.3.sg.pass` | A5.9 | keep (8) |
| 40-21 | 94 |  | `than form/feeling/perception/volitional formations could not` → `then …` (4×) *(same fix at: per-40:72, per-40:94, per-40:107, per-40:124)* | A6 | adjust: per-40:94 `than feeling could not` → `then feeling could not` (9) |
| 40-22 | 94 |  | `onself` → `oneself` *(same fix at: per-40:59, per-40:72, per-40:94, per-40:107, per-40:124, per-40:137)* | A6 | keep (9) |
| 40-23 | 107 |  | `than form/feeling/perception/volitional formations could not` → `then …` (4×) *(same fix at: per-40:72, per-40:94, per-40:107, per-40:124)* | A6 | adjust: per-40:107 `than perception could not` → `then perception could not` (9) |
| 40-24 | 107 |  | `onself` → `oneself` *(same fix at: per-40:59, per-40:72, per-40:94, per-40:107, per-40:124, per-40:137)* | A6 | keep (9) |
| 40-25 | 122 |  | **D6** `ahesun'ti` gloss reads "but pr. - may they be," — garbled; needs a proper gloss ("(if they) had been", aor.3.pl). | A8-D6 | adjust: per-40:122 `\| ahesun'ti \| verb \| aor.3.pl \| but pr. - may they be, \|` → `\| ahesun'ti \| verb \| aor.3.pl \| (with mā) may they not be; lit. they were \|`. DPD ahesuṃ = aor 3rd pl "they were"; DPD idiom mā ahesuṃ = "may they not be". The finding's "(if they) had been" is wrong (8) |
| 40-26 | 124 |  | `than form/feeling/perception/volitional formations could not` → `then …` (4×) *(same fix at: per-40:72, per-40:94, per-40:107, per-40:124)* | A6 | adjust: per-40:124 `than volitional formations could not` → `then volitional formations could not` (9) |
| 40-27 | 124 |  | `onself` → `oneself` *(same fix at: per-40:59, per-40:72, per-40:94, per-40:107, per-40:124, per-40:137)* | A6 | keep (9) |
| 40-28 | 137 |  | `onself` → `oneself` *(same fix at: per-40:59, per-40:72, per-40:94, per-40:107, per-40:124, per-40:137)* | A6 | keep (9) |
| 40-29 | 186 | `nu` | Grammar ∅ → `interr` | B-P6 | keep (9) |
| 40-30 | 188 | `samanupassituṃ` | POS `verbinf` → `verb`; Grammar `` → `inf` | A5.8 | keep (9) |
| 40-31 | 205 | `hi-` | Grammar ∅ → `emph` | B-P3 | keep (9) |
| 40-32 | 264 |  | Pāḷi is `viññāṇaṃ niccaṃ vā aniccaṃ vā'ti`; translation "Is **conscience** permanent or impermanent?" → "Is **consciousness** permanent or impermanent?" | A7 | keep (9) |
| 40-33 | 283 | `tasmā-(t)` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 40-34 | 285 | `bhikkhave` | Grammar `masc.v.sg` → `masc.voc.sg` | A5.6 | adjust: per-40:285 Grammar `masc.v.sg` → `masc.voc.pl` (DPD bhikkhave = masc voc pl of bhikkhu) (9) |
| 40-35 | 287 |  | `something , anything` → `something, anything` | A6 | keep (9) |
| 40-36 | 293 | `vā` | Rebuild row as `\| vā \| ind \| \| or \|` | B-N12 | keep (9) |
| 40-37 | 295 | `vā` | Rebuild row as `\| vā \| ind \| \| or \|` | B-N13 | keep (9) |
| 40-38 | 297 | `vā` | Rebuild row as `\| vā \| ind \| \| or \|` | B-N14 | keep (9) |
| 40-39 | 299 | `vā` | Rebuild row as `\| vā \| ind \| \| or \|` | B-N15 | keep (9) |
| 40-40 | 301 | `vā` | Rebuild row as `\| vā \| ind \| \| or \|` | B-N16 | keep (9) |
| 40-41 | 303 | `vā` | Rebuild row as `\| vā \| ind \| \| or \|` | B-N17 | keep (9) |
| 40-42 | 307 | `vā` | Rebuild row as `\| vā \| ind \| \| or \|` | B-N18 | keep (9) |
| 40-43 | 327 |  | **D8** quote style: `''` closers on lines 327–343 (policy D8) | A8-D8 | undecided — owner decision D8 |
| 40-44 | 353 |  | gloss `in forṃ` → `in form` | A1 | keep (9) |
| 40-45 | 362 | `vimuccati` | POS `v.pass` → `verb`; Grammar `pr.3.sg` → `pr.3.sg.pass` | A5.9 | keep (9) |
| 40-46 | 419 |  | `throught not grasping` → `through not grasping` *(same fix at: per-40:419, per-41:277)* | A6 | keep (9) |

## 41 — Āditta-Pariyāya-Sutta

`per-41-aditta-pariyaya-sutta.md` — 20 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 41-01 | 12 | `evaṃ-` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 41-02 | 13 | `me` | `masc.ins.sg` → `1.ins.sg` — same | A4 | keep (9) |
| 41-03 | 14 | `sutaṃ` | `masc.acc.sg` → `nt.nom.sg` — same | A4 | keep (7) — DPD silent: sutaṃ (DPD suta 1.1 confirms pp only, not the case) |
| 41-04 | 21 | `saddhiṃ` | Grammar ∅ → `prep` | B-P5 | keep (9) |
| 41-05 | 23 | `tatra` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 41-06 | 24 | `kho` | Grammar ∅ → `emph` | B-P3 | keep (9) |
| 41-07 | 41 |  | "Monks, everything is burning? And what is everything what is burning?" → "Monks, everything is burning. And what is the everything that is burning?" | A7 | keep (8) |
| 41-08 | 52 |  | POS `idioṃ` → `idiom` | A1 | keep (9) |
| 41-09 | 63 |  | POS `idioṃ` → `idiom` (row also fixed in Part 3, item merges gloss)  ✔ *Reviewer B proposes the same.* | A1 | keep (9) |
| 41-10 | 63 |  | Rebuild row: `\| tam'pi \| idiom \| \| that too, he too, even that, just that, that very thing \|` | A3 | keep (9) |
| 41-11 | 74 | `dos'agginā` | `nt.ins.sg` → `masc.ins.sg` — aggi is masculine; also fix `hate , aversion` → `hate, aversion` | A4 | keep (9) |
| 41-12 | 76 |  | Rebuild row: `\| jātiyā \| noun \| fem.ins.sg \| with birth, rebirth, conception \|`  ✔ *Reviewer B proposes the same.* | A2 | keep (9) |
| 41-13 | 79 | `sokehi` | `masc.ins.sg` → `masc.ins.pl` — `-ehi` plural | A4 | keep (9) |
| 41-14 | 80 | `paridevehi` | `masc.ins.sg` → `masc.ins.pl` — `-ehi` plural | A4 | keep (9) |
| 41-15 | 168 | `evaṃ` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 41-16 | 177 |  | POS `idioṃ` → `idiom` | A1 | keep (9) |
| 41-17 | 220 | `vimuccati` | POS `v.pass` → `verb`; Grammar `pr.3.sg` → `pr.3.sg.pass` | A5.9 | keep (9) |
| 41-18 | 243 |  | `What have to be done – is done` → `What has to be done – is done` | A6 | keep (9) |
| 41-19 | 254 | `te` | Rebuild row as `\| te \| pron \| masc.nom.pl \| those \|` — *same as 39:48* | B-N19 | keep (9) |
| 41-20 | 277 |  | `throught not grasping` → `through not grasping` *(same fix at: per-40:419, per-41:277)* | A6 | keep (9) |

## 42 — Yathā Vāri-Vahā

`per-42-yatha-vari-vaha.md` — 19 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 42-01 | 10 | `yathā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 42-02 | 23 | `evam'eva` | Grammar ∅ → `adv` | B-P1 | adjust: per-42:23 `\| evam'eva \| ind \| \| …` → POS `sandhi`, Grammar stays ∅ (DPD evameva = sandhi, adv + ind; BP7 treatment, not BP1 `adv`) (6) |
| 42-03 | 24 | `ito` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 42-04 | 25 | `dinnaṃ` | POS `adj` → `pp` | B-N116 | keep (9) |
| 42-05 | 27 | `upakappati` | Eng `is beneficial to, is serve for, is accrue` → `is beneficial to, serves, accrues` — *grammar fixes in the gloss* | B-N126 | keep (8) |
| 42-06 | 39 | `khippaṃ-` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 42-07 | 40 | `eva` | Grammar ∅ → `emph` | B-P3 | keep (9) |
| 42-08 | 41 | `samijjhatu` | Eng `may it achieves, succeeds, prospers` → `may it achieve, succeed, prosper` | B-N127 | keep (9) |
| 42-09 | 43 |  | `May your desires and wishes be succeeds only quickly.` → `May your desires and wishes succeed quickly.`  ✔ *Reviewer B proposes the same.* | A6 | keep (9) |
| 42-10 | 61 | `yathā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 42-11 | 71 | `yathā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 42-12 | 81 | `vivajjantu` | Eng `may they be avoided, abandoned, forsaked` → `may they be avoided, abandoned, forsaken` — *typo `forsaked`* | B-N128 | keep (9) |
| 42-13 | 91 | `vinassatu` | `pr.3.sg` → `imp.3.sg` — `-tu` imperative ("may it disappear")  ✔ *Reviewer B proposes the same.* | A4 | keep (9) |
| 42-14 | 104 |  | `May danger does not be for you.` → `May there be no danger for you.`  ✔ *Reviewer B proposes the same.* | A6 | keep (9) |
| 42-15 | 121 | `abhivādana-` | Grammar `nt` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision B11.3/A5.7 (DPD abhivādana = nt) |
| 42-16 | 140 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 | undecided — owner decision D5 |
| 42-17 | 147 | `rakkhantu` | Gr `imp.3.sg` → `imp.3.pl` — *`rakkhantu` is 3.pl* | B-N82 | keep (9) |
| 42-18 | 153 | `sadā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 42-19 | 156 | `te` | Gr `1.dat.sg` → `2.dat.sg` — *audit Part 4 has the same fix for te@51:44, 59:58, 63:33 but not this row* | B-N59 | keep (9) |

## 43 — Ratanattayānubhāv'ādi-Gāthā

`per-43-ratanattayanubhavadi-gatha.md` — 10 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 43-01 | 11 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 | undecided — owner decision D5 (unbold Pāḷi chant lines) |
| 43-02 | 19 |  | Rebuild row: `\| dukkha- \| noun \| \| discomfort, suffering, pain, unease, something unsatisfactory, problem, trouble \|`  ✔ *Reviewer B proposes the same.* | A3 | keep (9) |
| 43-03 | 22 | `verā` | Gr `masc.nom.pl` → `nt.nom.pl` — *`vera` neuter* | B-N60 | keep (9) |
| 43-04 | 30 | `asesato` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 43-05 | 48 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) |
| 43-06 | 50 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) |
| 43-07 | 53 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) |
| 43-08 | 54 | `yasavā` | Eng `famous, renowned, lit.: possessing fame'` → `famous, renowned, lit.: possessing fame` — *stray `'` removed* | B-N129 | keep (8) |
| 43-09 | 57 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) |
| 43-10 | 59 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) |

## 44 — Bhojana-Dānānumodanā

`per-44-bhojana-dananumodana.md` — 3 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 44-01 | 40 | `sukhassa` | Gr `masc.gen.sg` → `nt.gen.sg` — *`sukha` neuter* | B-N61 | keep (9) |
| 44-02 | 55 | `yattha` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 44-03 | 56 | `yattha-` | Grammar ∅ → `adv` | B-P1 | keep (8) |

## 45 — Culla-Maṅgala-Cakka-Vāḷa

`per-45-culla-mangala-cakka-vala.md` — 11 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 45-01 | 47 |  | `ny the power` → `by the power` | A6 | keep (10) |
| 45-02 | 78 | `sabbadā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 45-03 | 86 |  | Rebuild row: `\| dukkha- \| noun \| \| discomfort, suffering, pain, unease, something unsatisfactory, problem, trouble \|`  ✔ *Reviewer B proposes the same.* | A3 | keep (9) |
| 45-04 | 89 | `verā` | Gr `masc.nom.pl` → `nt.nom.pl` — *same as 43:22* | B-N62 | keep (9) |
| 45-05 | 97 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) |
| 45-06 | 116 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) |
| 45-07 | 118 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) |
| 45-08 | 121 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) |
| 45-09 | 125 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) |
| 45-10 | 127 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) |
| 45-11 | 133 |  | `May be f or you` → `May there be for you`  ✔ *Reviewer B proposes the same.* | A6 | keep (9) |

## 46 — Aggappasāda-Sutta-Gāthā

`per-46-aggappasada-sutta-gatha.md` — 3 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 46-01 | 11 | `ve` | Grammar ∅ → `emph` | B-P3 | keep (9) |
| 46-02 | 54 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) |
| 46-03 | 56 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) |

## 47 — Kāla-Dāna-Sutta-Gāthā

`per-47-kala-dana-sutta-gatha.md` — 9 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 47-01 | 10 | `kāle` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 47-02 | 15 |  | Rebuild row: `\| kālena \| ind \| adv \| timely, at the right moment, at a suitable time, at the proper time \|`  ✔ *Reviewer B proposes the same.* | A3 | keep (9) |
| 47-03 | 16 | `dinnaṃ` | Gr `nt.acc.sg` → `nt.nom.sg`; Eng `given, offered` → `a gift given, what is given` — *pp is the subject: nt.nom; gloss changes to match* | B-N63 | keep (7) — DPD silent: case of dinnaṃ (DPD dinna 1 pp; dinna 2 nt "offering; gift" supports the new gloss) |
| 47-04 | 33 | `tattha` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 47-05 | 52 | `tasmā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 47-06 | 54 |  | Rebuild row: `\| appaṭivāna- \| adj \| \| with confidence, without regret, lit. not shrinking back \|`  ✔ *Reviewer B proposes the same.* | A3 | keep (9) |
| 47-07 | 56 | `yattha` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 47-08 | 57 | `dinnaṃ` | Gr `masc.acc.sg` → `nt.nom.sg`; Eng `given, offered` → `gift, what is given` — *same as 47:16* | B-N64 | keep (8) |
| 47-09 | 58 | `mahapphalaṃ` | Gr `masc.acc.sg` → `nt.nom.sg`; Eng `of great fruit, yielding good results` → `of great fruit, yielding great results` — *predicate agrees with subject `dinnaṃ` (also gloss `good` → `great`)* | B-N65 | adjust: Grammar fix only; the gloss change contradicts DPD mahapphala (adj, "of great fruit; yielding good results"). per-47:58 `\| mahapphalaṃ \| adj \| masc.acc.sg \| of great fruit, yielding good results \|` → `\| mahapphalaṃ \| adj \| nt.nom.sg \| of great fruit, yielding good results \|` (8) |

## 48 — So Attha-Laddho

`per-48-so-attha-laddho.md` — 2 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 48-01 | 12 | `laddhā` | POS `verb` → `pp`; Gr `ger` → `masc.nom.pl`; Eng `getting, obtaining` → `having obtained, having gotten` — *reviewer: `laddha` is a past participle, not a gerund* | B-N117 | keep (7) |
| 48-02 | 19 | `saha` | Grammar ∅ → `prep` | B-P5 | keep (9) |

## 49 — Devā-ārādhanāi

`per-49-deva-aradhanai.md` — 8 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 49-01 | 3 |  | **D2** Title `Devā-ārādhanāi` carries a stray trailing `i` (standard: `Devā-ārādhanā`). Recommend: fix the visible title only, keep the filename (renaming would need nav links in per-48/per-50, index and feedback URL). | A8-D2 | keep (8) |
| 49-02 | 27 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) |
| 49-03 | 32 | `c'antalikkhe` | POS `ind` → `sandhi` (leave Grammar empty; reviewer also wrote `conj + loc` in Grammar) | B-P7 | keep (8) |
| 49-04 | 36 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) |
| 49-05 | 61 | `santike` | Grammar ∅ → `adv` | B-P1 | adjust: per-49:61 santike Grammar ∅ → `prep` (not `adv`): DPD santike 1 = ind, prep "to; in the presence (of); near (to)…", the sense used in the row; santike 2 adv = "compared (to)" (8) |
| 49-06 | 66 |  | **D6** `sādhavo` tagged ind — looks like masc.nom.pl of `sādhu` ("good sirs"); verify against chant context. | A8-D6 | adjust: per-49:66 `\| sādhavo \| ind \| accomplishing, fulfilling, effecting, completing \| with approval \|` → `\| sādhavo \| noun \| masc.nom.pl \| good people, virtuous ones \|` (DPD sādhu 6 masc "good person"; the current row also has its gloss split into the Grammar column). The translation at per-49:70 ("with approval") would need owner review to match (6) DPD silent: sādhavo (form not a headword; the fix rests on sādhu 6) |
| 49-07 | 66 | `sādhavo` | ⚔ **C6 — keep ONE:** **Option A (audit)** Part 3: keep `ind`, merge gloss: `accomplishing, fulfilling, effecting, completing, with approval` (D6 asks to verify)  ·  **Option B (reviewer)** POS `ind` → `adj`, Grammar → `masc.nom.pl`, Eng → `good ones, virtuous ones`  ·  *B answers D6 (reviewer: `sādhavo me suṇantu` = "may the virtuous ones hear from me").* | B-C6 | undecided |
| 49-08 | 67 | `me` | ⚔ **C5 — keep ONE:** **Option A (audit)** Part 3: `me / pron / 1.dat.sg / for me`  ·  **Option B (reviewer)** `me / pron / 1.gen.sg / my, of me, by me`  ·  *Context `bhaṇantu me` / `suṇantu me`: dative-sense ("for me") vs genitive-sense.* | B-C5 | undecided |

## 50 — Saraṇa-Gamana-Pāṭho

`per-50-sarana-gamana-patho.md` — 4 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 50-01 | 18 | `dutiyam'pi` | POS `adv+ind` — unify to one form (see policy D4) | A8-D4 | undecided — owner decision D4 (one form for composite POS `adv+ind`); dutiyam'pi is not in the DPD file |
| 50-02 | 18 |  | multi-word POS tag (`v + pn` / `ind+pn` / `ind+m+imp` / `adv+ind`): use `idiom` or `sandhi` per corpus convention (policy D4) | A8-D4 | drop: duplicate of 1140 (same row, same D4 issue) |
| 50-03 | 26 | `tatiyam'pi` | POS `adv+ind` — unify to one form (see policy D4) | A8-D4 | undecided — owner decision D4 (one form for composite POS `adv+ind`); tatiyam'pi is not in the DPD file |
| 50-04 | 26 |  | multi-word POS tag (`v + pn` / `ind+pn` / `ind+m+imp` / `adv+ind`): use `idiom` or `sandhi` per corpus convention (policy D4) | A8-D4 | drop: duplicate of 1142 (same row, same D4 issue) |

## 51 — Nama-Kāra-Siddhi-Gāthā

`per-51-nama-kara-siddhi-gatha.md` — 10 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 51-01 | 15 | `sāmaṃ` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 51-02 | 16 | `va = eva` | Grammar ∅ → `emph` | B-P3 | keep (8) |
| 51-03 | 44 | `te` | `masc.dat.sg` → `2.dat.sg` — "for you" = 2nd person pronoun  ✔ *Reviewer B proposes the same.* | A4 | keep (9) |
| 51-04 | 44 | `te` | POS `noun` → `pron` — *extends audit Part 4 (which only changes Grammar to `2.dat.sg`)* | B-N121 | keep (9) |
| 51-05 | 47 | `hotu` | `pr.3.sg` → `imp.3.sg` — `-tu` imperative  ✔ *Reviewer B proposes the same.* | A4 | keep (10) |
| 51-06 | 50 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) |
| 51-07 | 67 | `visuddhi-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision B11.3/A5.7 (blank or keep bare gender on compound members); DPD visuddhi = fem |
| 51-08 | 76 | `suciṇṇo` | POS `noun` → `adj` — *`suciṇṇo` adj per DPD* | B-N118 | keep (9) |
| 51-09 | 105 | `sayaṃ` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 51-10 | 108 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) |

## 52 — Namo-Kāra-Aṭṭhaka

`per-52-namo-kara-atthaka.md` — 19 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 52-01 | 10 | `namo` | Grammar ∅ → `excl` | B-P4 | keep (9) |
| 52-02 | 12 | `sammā-` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 52-03 | 15 | `namo` | Grammar ∅ → `excl` | B-P4 | keep (9) |
| 52-04 | 20 | `idha` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 52-05 | 28 | `namo` | Grammar ∅ → `excl` | B-P4 | keep (9) |
| 52-06 | 34 | `namo` | Grammar ∅ → `excl` | B-P4 | keep (9) |
| 52-07 | 35 |  | **D3** `<br>` inside table cells (lines 35). Policy: keep (note the exception) or convert `A<br>(or)<br>B` → `A (or) B`. | A8-D3 | undecided — owner decision D3 (`<br>` in table cells); `<br>(or)<br>` is still at per-52:35 although mech says gone |
| 52-08 | 36 | `omāti-` | Grammar `pr.3rd.sg` → `pr.3.sg` | A5.1 | keep (8) |
| 52-09 | 37 | `āraddhassa` | POS `noun` → `pp`; Eng `accomplishment, achievement; success` → `won; accomplished; succeeded` — *reviewer: `āraddha` is a past participle (DPD)* | B-N119 | keep (8) |
| 52-10 | 38 | `ratanattayassa` | Gr `masc.dat.sg` → `nt.dat.sg` — *`ratanattaya` neuter* | B-N66 | keep (9) |
| 52-11 | 39 | `sādhukaṃ` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 52-12 | 41 |  | `Tiple Gem` → `Triple Gem`; `succseed` → `succeed` | A6 | keep (10) |
| 52-13 | 47 | `namo` | Grammar ∅ → `excl` | B-P4 | keep (9) |
| 52-14 | 50 | `vatthu-ttayassa'pi` | Gr `masc.dat.sg` → `nt.dat.sg` — *`vatthu` neuter* | B-N67 | keep (9) |
| 52-15 | 51 | `namo-` | Grammar ∅ → `excl` | B-P4 | keep (8) |
| 52-16 | 63 | `namo-` | Grammar ∅ → `excl` | B-P4 | keep (8) |
| 52-17 | 66 | `suvatthi` | Gr `masc.nom.sg` → `fem.nom.sg` — *DPD: suvatthi fem. (audit Part 3 item per-54:110 already uses fem.nom.sg for the same word)* | B-N68 | keep (9) |
| 52-18 | 68 | `sabbadā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 52-19 | 69 | `namo-` | Grammar ∅ → `excl` | B-P4 | keep (8) |

## 53 — Maṅgala-Sutta

`per-53-mangala-sutta.md` — 56 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 53-01 | 10 | `evaṃ-` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 53-02 | 11 | `me` | `masc.ins.sg` → `1.ins.sg` — same | A4 | keep (9) |
| 53-03 | 12 | `sutaṃ` | `masc.acc.sg` → `nt.nom.sg` — same  ✔ *Reviewer B proposes the same.* | A4 | keep (7) — DPD silent: sutaṃ (DPD suta 1.1 confirms pp only, not the case) |
| 53-04 | 12 | `sutaṃ:` | Eng `heard` → `what is heard; something heard` — *extends audit Part 4 (`sutaṃ` → nt.nom.sg)* | B-N122 | drop: the current gloss `heard` matches DPD suta 1.1 (pp, "heard") and the translation "thus was heard by me"; the proposed gloss is DPD suta 1.3, the nt noun sense, which does not fit this pp row (7) |
| 53-05 | 38 | `yena` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 53-06 | 40 | `tena-` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 53-07 | 52 | `ekaṃantaṃ` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 53-08 | 54 | `ekaṃantaṃ` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 53-09 | 56 | `kho` | Grammar ∅ → `emph` | B-P3 | keep (9) |
| 53-10 | 60 | `gāthāya` | `fem.ins` → `fem.ins.sg` — number missing | A4 | keep (9) |
| 53-11 | 75 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) |
| 53-12 | 80 | `brūhi` | `imp.3.sg` → `imp.2.sg` — "you speak" is 2nd person  ✔ *Reviewer B proposes the same.* | A4 | keep (10) |
| 53-13 | 80 | `brūhi` | Eng `you speak, may you say, you shall talk` → `say!; tell!; speak!` — *extends audit Part 4 (`brūhi` → imp.2.sg)* | B-N123 | keep (9) |
| 53-14 | 84 |  | `tall about highest blessing` → `tell about the highest blessing` | A6 | keep (9) |
| 53-15 | 84 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 | undecided — owner decision D8 (quote style); per-53:84 has a closing ” with no opening quote on that line |
| 53-16 | 94 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (9) |
| 53-17 | 95 | `bālānaṃ,` | Gr `masc.dat.pl` → `masc.gen.pl`; Eng `to ignorant; fools` → `of fools; ignorant ones` — *dat → gen (also changes gloss `to ignorant; fools` → `of fools; ignorant ones`)* | B-N69 | keep (7) — DPD silent on the case: DPD bāla 2 = masc only; dat vs gen of bālānaṃ is a syntax call |
| 53-18 | 96 | `paṇḍitānaṃ-` | Gr `masc.dat.pl` → `masc.gen.pl`; Eng `to wise people` → `of wise people` — *dat → gen (gloss `to wise people` → `of wise people`)* | B-N70 | keep (7) — DPD silent on the case: DPD paṇḍita 2 = masc only; dat vs gen of paṇḍitānaṃ is a syntax call |
| 53-19 | 97 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-20 | 100 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-21 | 101 | `pūjanīyānaṃ,` | POS `adj, ptp` → `ptp`; Gr `masc.dat.pl` → `masc.gen.pl`; Eng `to entitled to homage; should be venerated` → `of those worthy of veneration; who should be revered` — *same dat → gen fix as `bālānaṃ` / `paṇḍitānaṃ` / `ñātakānaṃ` in 12.2a* | B-N120 | keep (7) — DPD pūjanīya = ptp, which confirms POS `ptp`; DPD silent on dat vs gen of pūjanīyānaṃ |
| 53-22 | 102 | `etaṃ` | Gr `masc.acc.sg` → `nt.nom.sg` — *neuter, subject* | B-N71 | keep (9) |
| 53-23 | 117 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-24 | 119 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-25 | 122 | `sammā-` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 53-26 | 124 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-27 | 135 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-28 | 137 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-29 | 139 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-30 | 142 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-31 | 152 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 | undecided — owner decision D5 (unbold Pāḷi chant lines) |
| 53-32 | 163 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-33 | 175 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-34 | 177 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-35 | 178 | `ñātakānaṃ-` | Gr `masc.dat.pl` → `masc.gen.pl`; Eng `to relations, relatives, kinsmans` → `of relations, relatives, kinsmen` — *dat → gen (gloss `to relations, relatives, kinsmans` → `of relations, relatives, kinsmen`)* | B-N72 | keep (7) — DPD silent on the case: DPD ñātaka 1 = masc only; dat vs gen of ñātakānaṃ is a syntax call |
| 53-36 | 179 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-37 | 196 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-38 | 199 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-39 | 211 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-40 | 213 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-41 | 215 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-42 | 217 | `kālena` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 53-43 | 230 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-44 | 233 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-45 | 235 | `kālena` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 53-46 | 247 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 | undecided — owner decision D5 (unbold Pāḷi chant lines) |
| 53-47 | 252 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-48 | 254 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-49 | 257 |  | Rebuild row: `\| nibbāna- \| noun \| \| going out (of a lamp), extinguishment (of a fire), quenching, peace \|` | A3 | keep (9) |
| 53-50 | 259 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 53-51 | 273 | `na` | reviewer: Grammar `neg` → ∅ — **⚑ user decision, not implemented unless you remove the ⚑** (for the word `na` the corpus has 33 rows with empty Grammar vs 7 `neg`) | **B-X2⚑** | undecided — owner decision B-X2⚑ (`na`: Grammar `neg` or empty); DPD na 1 = plain `ind` |
| 53-52 | 287 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 | undecided — owner decision D5 (unbold Pāḷi chant lines) |
| 53-53 | 295 | `sabbattha'm-` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 53-54 | 297 | `sabbattha` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 53-55 | 298 | `sotthiṃ` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 53-56 | 304 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 | undecided — owner decision D8 (quote style); the row's English cell holds only `”` |

## 54 — Ratana-Sutta

`per-54-ratana-sutta.md` — 35 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 54-01 | 29 | `eva` | Grammar ∅ → `emph` | B-P3 | keep (9) |
| 54-02 | 35 | `sakkacca` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 54-03 | 46 | `tasmā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 54-04 | 47 | `hi` | Grammar ∅ → `emph` | B-P3 | keep (8) — DPD hi 1 = ind, emph "indeed" |
| 54-05 | 48 | `bhūtā` | Grammar `masc.v.pl` → `masc.voc.pl` | A5.6 | keep (8) — DPD bhūta 03 = nt "being", but bhūtā here declines as masc pl; the fix (`v` → `voc`) stands |
| 54-06 | 49 | `nisāmetha` | POS `v.caus` → `verb`; Grammar `imp.2.pl` → `imp.2.pl.caus` | A5.9 | keep (8) — DPD nisāmeti = pr, caus, which confirms the caus tag |
| 54-07 | 68 | `tasmā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 54-08 | 69 | `hi` | Grammar ∅ → `emph` | B-P3 | keep (8) — DPD hi 1 = ind, emph "indeed" |
| 54-09 | 74 |  | translation `protect theṃ` → `protect them` | A1 | keep (10) |
| 54-10 | 91 | `na` | reviewer: Grammar `neg` → ∅ — **⚑ user decision, not implemented unless you remove the ⚑** (for the word `na` the corpus has 33 rows with empty Grammar vs 7 `neg`) | **B-X2⚑** | undecided — owner decision B-X2⚑ (`na`: Grammar `neg` or empty); DPD na 1 = plain `ind` |
| 54-11 | 110 |  | Rebuild row: `\| suvatthi \| noun \| fem.nom.sg \| safety, well-being, blessing; su+[v]+√as+ti \|` (grammar cell held the gloss; root note kept at end) | A3 | keep (9) |
| 54-12 | 126 | `ajjhagā` | `imperf.3.sg` → `aor.3.sg` — same form | A4 | drop: DPD has ajjhagā as `imperf` (imperf of adhigacchati), so the source `imperf.3.sg` agrees with DPD |
| 54-13 | 128 |  | gloss `firṃ attentive` → `firm, attentive` | A1 | keep (9) |
| 54-14 | 129 | `na` | reviewer: Grammar `neg` → ∅ — **⚑ user decision, not implemented unless you remove the ⚑** (for the word `na` the corpus has 33 rows with empty Grammar vs 7 `neg`) | **B-X2⚑** | undecided — owner decision B-X2⚑ (`na`: Grammar `neg` or empty); DPD na 1 = plain `ind` |
| 54-15 | 144 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 | undecided — owner decision D5 (unbold Pāḷi chant lines) |
| 54-16 | 160 | `na` | reviewer: Grammar `neg` → ∅ — **⚑ user decision, not implemented unless you remove the ⚑** (for the word `na` the corpus has 33 rows with empty Grammar vs 7 `neg`) | **B-X2⚑** | undecided — owner decision B-X2⚑ (`na`: Grammar `neg` or empty); DPD na 1 = plain `ind` |
| 54-17 | 202 | `nikkāmino` | `masc.ins.sg` → `masc.nom.pl` — nom. pl. agreeing with `ye … nikkāmino`; gloss stays | A4 | keep (6) — DPD silent: nikkāmin |
| 54-18 | 203 |  | Rebuild row: `\| gotama- \| adj \| \| family name of the Buddha; lit. of the Gotama clan \|` | A3 | adjust: per-54-ratana-sutta.md:203 `\| gotama- \| adj \| family name of the Buddha; lit. of the Gotama \| clan \|` → `\| gotama- \| noun \| \| family name of the Buddha; lit. of the Gotama clan \|` (DPD gotama 1 = masc "family name of the Buddha") (7) |
| 54-19 | 206 | `patti-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision B11.3 / A5.7 (bare gender on compound members); DPD patti 1.1 is fem, so `fem` is correct if kept |
| 54-20 | 211 | `mudhā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 54-21 | 224 | `yathā-` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 54-22 | 232 | `tathā-` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 54-23 | 238 | `avecca` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 54-24 | 256 | `kiñcāpi` | POS `ind` → `sandhi` (leave Grammar empty) | B-P7 | keep (9) |
| 54-25 | 261 | `na` | reviewer: Grammar `neg` → ∅ — **⚑ user decision, not implemented unless you remove the ⚑** (for the word `na` the corpus has 33 rows with empty Grammar vs 7 `neg`) | **B-X2⚑** | undecided — owner decision B-X2⚑ (`na`: Grammar `neg` or empty); DPD na 1 = plain `ind` |
| 54-26 | 276 | `saha-` | Grammar ∅ → `prep` | B-P5 | keep (8) |
| 54-27 | 277 | `eva` | Grammar ∅ → `emph` | B-P3 | keep (9) |
| 54-28 | 306 | `ca-` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 54-29 | 320 | `kiñcāpi` | POS `ind` → `sandhi` (leave Grammar empty) | B-P7 | keep (9) |
| 54-30 | 350 | `yathā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 54-31 | 357 | `tathā-` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 54-32 | 373 |  | `knower the best , who` → `knower of the best, who` | A6 | keep (9) |
| 54-33 | 394 |  | Rebuild row: `\| viratta- \| pp \| \| detached (from); without desire (for); become indifferent (to); lost interest (in) \|` | A3 | keep (10) |
| 54-34 | 404 | `yathā-` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 54-35 | 420 |  | Rebuild row: same fix as :110 (identical row later in file) | A3 | keep (9) |

## 55 — Karaṇīya-Metta-Sutta

`per-55-karaniya-metta-sutta.md` — 33 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 55-01 | 11 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 | undecided — owner decision D5 (unbold Pāḷi chant lines) |
| 55-02 | 33 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 55-03 | 36 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 55-04 | 51 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 55-05 | 53 | `ca,` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 55-06 | 55 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 55-07 | 63 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 55-08 | 65 | `ca,` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 55-09 | 79 | `na` | reviewer: Grammar `neg` → ∅ — **⚑ user decision, not implemented unless you remove the ⚑** (for the word `na` the corpus has 33 rows with empty Grammar vs 7 `neg`) | **B-X2⚑** | undecided — owner decision B-X2⚑ (`na`: Grammar `neg` or empty); DPD na 1 = plain `ind` |
| 55-10 | 80 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 55-11 | 125 | `atthi` | `pr.3.pl` → `pr.3.sg` — atthi is singular (used distributively: "there are") | A4 | drop: DPD atthi 1.2 = "pr 3rd pl of atthi; there are; they are", so the source `pr.3.pl` agrees with DPD |
| 55-12 | 174 |  | `whoever , that which` → `whoever, that which` | A6 | keep (10) |
| 55-13 | 176 | `dūre` | Grammar ∅ → `adv` | B-P1 | keep (8) |
| 55-14 | 178 | `avidūre` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 55-15 | 207 | `nikubbetha` | Grammar `opt.3.sg refl` → `opt.refl.3.sg` (reviewer did not touch this row; B-11.2 does not apply) | A5.3 | undecided — owner decision A5.3 / B11.2 (refl notation); DPD nikubbetha = opt, reflx 3rd sg |
| 55-16 | 213 | `na-atimaññetha` | Grammar `opt.3.sg refl` → `opt.refl.3.sg` (reviewer did not touch this row; B-11.2 does not apply) | A5.3 | undecided — owner decision A5.3 / B11.2 (refl notation) |
| 55-17 | 214 | `katthaci` | POS `adv` → `ind`; Grammar `` → `adv` | A5.10 | keep (9) |
| 55-18 | 215 |  | gloss `that, hiṃ` → `that, him` | A1 | keep (10) |
| 55-19 | 226 |  | `(throught)` → `(through)` | A6 | keep (9) |
| 55-20 | 232 |  | gloss `…unease, probleṃ` → `…unease, problem` (row also merged in Part 3) | A1 | keep (9) |
| 55-21 | 235 |  | `one to anothershould not wish` → `one to another should not wish` | A6 | keep (9) |
| 55-22 | 257 | `evam-` | Grammar ∅ → `adv` | B-P1 | keep (8) |
| 55-23 | 260 | `bhūtesu` | `masc.loc.sg` → `masc.loc.pl` — `-esu` plural | A4 | keep (8) — DPD bhūta 03 = nt "being"; `-esu` is plural in masc and nt alike, so sg → pl stands and the gender is left as the source has it |
| 55-24 | 280 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 55-25 | 284 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 | undecided — owner decision D5 |
| 55-26 | 292 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 55-27 | 319 | `yāvatā-` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 55-28 | 320 |  | gloss `to hiṃ` → `to him` | A1 | keep (9) |
| 55-29 | 339 | `āhu` | `pref.p.3.pl` → `perf.3.pl` — typo `pref.p` | A4 | keep (9) |
| 55-30 | 351 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 / 2.2 = ind, conj ("and" / "but") |
| 55-31 | 370 | `hi` | Grammar ∅ → `emph` | B-P3 | keep (8) — DPD hi 1 = ind, emph "indeed" |
| 55-32 | 371 | `jātu` | Grammar ∅ → `emph` | B-P3 | keep (9) |
| 55-33 | 374 | `puna-` | Grammar ∅ → `adv` | B-P1 | keep (9) |

## 56 — Khandha-Parittaṃ

`per-56-khandha-parittam.md` — 4 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 56-01 | 25 | `ca;` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 56-02 | 90 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 56-03 | 98 | `agamā` | POS `v.refl` → `verb`; Grammar `aor.3.sg` → `aor.3.sg.refl` | A5.9 | adjust: per-56:98 `\| agamā \| v.refl \| aor.3.sg \|` → `\| agamā \| verb \| imperf.3.sg \|`. Not refl and not aor: DPD agamā = imperf of gacchati (āgamā 1 is likewise imperf) (8) |
| 56-04 | 149 | `sammā-` | Grammar ∅ → `adv` | B-P1 | keep (9) |

## 57 — Buddha-Dhamma-Saṅgha-Guṇā

`per-57-buddha-dhamma-sangha-guna.md` — 5 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 57-01 | 14 | `sammā-` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 57-02 | 43 | `paccattaṃ` | POS `adv` → `ind`; Grammar `ind` → `adv`  ✔ *Reviewer B proposes the same.* | A5.10 | keep (9) |
| 57-03 | 60 | `yadidaṃ` | POS `adv` → `ind`; Grammar `ind` → `adv` | A5.10 | adjust: per-57:60 `\| yadidaṃ \| adv \| ind \|` → `\| yadidaṃ \| sandhi \| \|`. DPD: yadidaṃ = sandhi (pron + pron), which matches BP7 (8) |
| 57-04 | 60 | `yadidaṃ` | ⚔ **same cells as the A5.10 row above — keep ONE:** **Option A (A5.10)** POS `adv` → `ind`, Grammar `ind` → `adv`  ·  **Option B (B-P7)** POS `adv` → `sandhi`, Grammar `ind` → ∅ (reviewer himself wrote `sandhi` in both POS and Grammar; I recommend Grammar empty)  ·  *Do not apply both.* | B-P7 | undecided |
| 57-05 | 61 | `cattāri` | `masc.nom.pl` → `nt.nom.pl` — same passage | A4 | keep (9) |

## 58 — Yaṅ Kiñci Ratanaṃ Loke

`per-58-yan-kinci-ratanam-loke.md` — 2 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 58-01 | 16 | `puthu` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 58-02 | 21 | `tasmā` | Grammar ∅ → `adv` | B-P1 | keep (9) |

## 59 — Bojjh'aṅga-Parittaṃ

`per-59-bojjhanga-parittam.md` — 18 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 59-01 | 15 | `tathā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 59-02 | 20 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 59-03 | 21 | `tathā-` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 59-04 | 38 | `sammā-` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 59-05 | 45 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 59-06 | 48 |  | `which has been thoroughly told by the sage who understand` → `which have been thoroughly told by the sage who understands` | A6 | keep (8) |
| 59-07 | 56 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 | undecided — owner decision D8 |
| 59-08 | 58 | `te` | `masc.dat.sg` → `2.dat.sg` — same | A4 | keep (9) — DPD te 2.3 = 2nd dat sg of tvaṃ |
| 59-09 | 60 | `sabbadā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 59-10 | 80 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 59-11 | 85 | `taṅ'khaṇe` | POS `ind` → `sandhi` (leave Grammar empty) | B-P7 | undecided — DPD silent: taṅkhaṇe (no headword for taṅkhaṇe or taṅ'khaṇe; DPD has only the idiom tena khaṇena), so sandhi vs ind adv cannot be settled from DPD |
| 59-12 | 97 | `ekadā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 59-13 | 105 | `sādaraṃ` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 59-14 | 107 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 59-15 | 111 | `ṭhānaso` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 59-16 | 125 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 59-17 | 132 | `va` | Grammar ∅ → `emph` | B-P3 | drop: DPD va 1.1 = ind, abbrev of iva "like; as", which matches the row's gloss and the translation "just as"; emph would be va 2.1 (abbrev of eva) |
| 59-18 | 134 | `anuppatti-` | Rebuild row as `\| anuppatti- \| noun \| \| following attainment (of), after getting \|` — *POS cell held `masc`; compound member, Grammar stays ∅* | B-N20 | keep (8) |

## 60 — Abhaya-Parittaṃ

`per-60-abhaya-parittam.md` — *no suggestions from either review*

## 61 — Devatā-Uyyojana-Gāthā

`per-61-devata-uyyojana-gatha.md` — 8 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 61-01 | 11 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 61-02 | 14 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 61-03 | 17 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 61-04 | 30 | `ettāvatā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 61-05 | 31 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 61-06 | 54 | `sabbadā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 61-07 | 73 | `balaṃ` | Gr `nt` → `nt.acc.sg` — *grammar was only `nt`* | B-N73 | undecided — case of `yaṃ balaṃ` (nom in an elliptic relative clause vs acc) is a syntax call; nt.?.sg is certain |
| 61-08 | 78 | `sabbaso` | Grammar ∅ → `adv` | B-P1 | keep (9) |

## 62 — Jaya-Maṅgala-Aṭṭha-Gāthā

`per-62-jaya-mangala-attha-gatha.md` — 17 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 62-01 | 23 | `vidhinā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 62-02 | 47 |  | Rebuild row: `\| akkhama- \| adj \| \| impatient (with), intolerant (of), not able to endure \|` | A3 | keep (9) |
| 62-03 | 52 | `vidhinā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 62-04 | 79 | `vidhinā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 62-05 | 100 |  | Rebuild row: `\| yojana- \| noun \| \| measure of length; approximately twenty kilometres \|` | A3 | keep (8) |
| 62-06 | 125 | `ciñcāya` | Grammar `fem.inst.sg` → `fem.ins.sg` | A5.2 | keep (7) |
| 62-07 | 127 | `vacanaṃ` | Gr `nt` → `nt.acc.sg` — *grammar was only `nt`* | B-N74 | keep (7) |
| 62-08 | 128 | `janakāya-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision A5.7/B11.3 |
| 62-09 | 129 | `majjhe` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 62-10 | 132 | `vidhinā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 62-11 | 148 | `mati-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision A5.7/B11.3 |
| 62-12 | 151 |  | **D3** `<br>` inside table cells (lines 151). Policy: keep (note the exception) or convert `A<br>(or)<br>B` → `A (or) B`. | A8-D3 | undecided — owner decision D3 (the `<br>` is still at per-62:151, despite mech=gone) |
| 62-13 | 153 |  | Rebuild row: `\| abhiropita- \| adj \| \| put on top, placed, (of an argument) refuted, debunked, disproved \|` | A3 | adjust: per-62:153 → `\| abhiropita- \| pp \| \| put on top, placed, (of an argument) refuted, debunked, disproved \|`. POS is pp, not adj: DPD abhiropita = pp of abhiropeti (7) |
| 62-14 | 157 |  | Rebuild row: `\| paññā- \| noun \| \| wisdom, knowledge, intelligence, intellect, understanding, insight \|` | A3 | keep (9) |
| 62-15 | 184 | `vidhinā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 62-16 | 211 | `vidhinā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 62-17 | 236 |  | **D6** `sarate-m'` tagged opt.3.sg — form is middle present (`sarate`); suggest `pr.refl.3.sg`; verify. | A8-D6 | adjust: per-62:236 `\| sarate-m' \| verb \| opt.3.sg \|` → `\| sarate-m' \| verb \| pr.refl.3.sg \|`. Write `pr.3.sg` instead if B11.2 is chosen over A5.3. DPD silent: sarate (no headword); DPD sarati 1.1 = pr "remembers", and the pattern follows labhate = pr reflx 3rd sg (6) |

## 63 — Jaya-Parittaṃ

`per-63-jaya-parittam.md` — 7 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 63-01 | 33 | `te` | `masc.dat.sg` → `2.dat.sg` — same | A4 | keep (9) — DPD te 2.3 = 2nd dat sg of tvaṃ |
| 63-02 | 46 | `sakyānaṃ` | `masc.gen.sg` → `masc.gen.pl` — `-ānaṃ` plural | A4 | keep (9) — DPD sakya 1 = masc; `-ānaṃ` is plural |
| 63-03 | 49 | `evaṃ` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 63-04 | 52 | `hohi` | `pr.2.sg` → `imp.2.sg` — imperative "may you be" | A4 | keep (9) |
| 63-05 | 53 | `jayassu` | POS `verbimp.reflx.2.s` → `verb`; Grammar `` → `imp.refl.2.sg` | A5.8 | adjust: per-63:53 POS `verbimp.reflx.2.s` → `verb`; Grammar ∅ → `imp.refl.2.sg` (A5.3) or `imp.2.sg` (B11.2), pending owner decision A5.3/B11.2. The pattern follows sikkhassu = imp reflx 2nd sg; DPD silent: jayassu (DPD jayati = pr only) (7) |
| 63-06 | 88 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 63-07 | 104 | `paṇīdhi` | Gr `fem` → `masc.nom.sg` — *DPD: paṇīdhi masc.* | B-N75 | keep (6) |

## 64 — Bhavatu-Sabba-Maṅgalaṃ

`per-64-bhavatu-sabba-mangalam.md` — 2 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 64-01 | 12 |  | **D5** Pāḷi chant line is bolded like a translation → unbold (policy D5; per-39's deva-refrain block is systematic — decide once) | A8-D5 | undecided — owner decision D5 |
| 64-02 | 25 | `sadā` | Grammar ∅ → `adv` | B-P1 | keep (9) |

## 65 — Dhamma-Saṅgaṇī-Mātikā

`per-65-dhamma-sangani-matika.md` — 7 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 65-01 | 38 | `n'eva` | POS `ind` → `sandhi` (leave Grammar empty) | B-P7 | keep (9) — DPD neva 1 = sandhi, ind + ind "neither; not" |
| 65-02 | 46 |  | Rebuild row: `\| upādinna- \| pp \| \| grasped, clung to, attached to, taken as "mine", acquired \|` | A3 | keep (8) |
| 65-03 | 48 |  | Rebuild row: `\| anupādinna- \| pp \| \| not grasped, not clung to, not attached to, not taken as "mine", not acquired \|` | A3 | keep (8) |
| 65-04 | 62 |  | `dhammas neither defiled and subject to defilements` → `dhammas neither defiled nor subject to defilements` | A6 | keep (9) |
| 65-05 | 126 |  | `exhalted` → `exalted` *(same fix at: per-65:126, per-65:134)* | A6 | keep (9) |
| 65-06 | 134 |  | `exhalted` → `exalted` *(same fix at: per-65:126, per-65:134)* | A6 | keep (9) |
| 65-07 | 200 |  | `internal and external dhamams` → `internal and external dhammas` | A6 | keep (9) |

## 66 — Vipassanā-Bhūmi-Pāṭho

`per-66-vipassana-bhumi-patho.md` — 9 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 66-01 | 82 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 | undecided — owner decision D8 |
| 66-02 | 86 |  | `the I am knowing the unknown' faculty` → `the 'I am knowing the unknown' faculty` | A6 | keep (8) |
| 66-03 | 94 |  | Rebuild row: `\| dukkhaṃ \| noun \| nt.nom.sg \| discomfort, suffering, pain, unease, something unsatisfactory, problem, trouble \|` (embedded `nt.ac.s`; nominative in `idaṃ … dukkhaṃ`-type list — verify against the chant line above it) | A2 | keep (7) |
| 66-04 | 97 |  | Rebuild row: `\| dukkhanirodho \| noun \| masc.nom.sg \| cessation of suffering, disappearance of suffering \|` | A2 | keep (9) |
| 66-05 | 109 | `\>avijjā-` | Grammar `fem` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision A5.7/B11.3 |
| 66-06 | 110 | `\>paccayā` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision A5.7/B11.3 |
| 66-07 | 145 |  | `becoming arise` → `becoming arises`; `birth arise` → `birth arises` *(same fix at: per-24:49, per-66:145)* | A6 | keep (9) |
| 66-08 | 166 | `tv'eva` | POS `ind` → `sandhi` (leave Grammar empty) | B-P7 | keep (9) — DPD tveva 1 = sandhi, ind + ind "however; but; rather" |
| 66-09 | 167 | `asesa-virāga-nirodhā` | POS `m.abl.s` → `noun`; Grammar ∅ → `masc.abl.sg` (tag sits in POS column; `noun` is my inference — confirm) | A5.6 | keep (8) |

## 67 — Paṭṭhāna-Mātikā-Pāṭho

`per-67-patthana-matika-patho.md` — 1 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 67-01 | 32 |  | `there is not , there not exists` → `there is not, there does not exist` | A6 | keep (9) |

## 68 — Adāsi-Me Ādi Gāthā

`per-68-adasi-me-adi-gatha.md` — 12 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 68-01 | 16 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 68-02 | 21 | `pubbe` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 68-03 | 25 |  | **D8** quote style: opening quote missing / unbalanced (policy D8: straight apostrophes, balanced pairs) | A8-D8 | undecided — owner decision D8 |
| 68-04 | 34 | `hi` | Grammar ∅ → `emph` | B-P3 | keep (8) — DPD hi 1 = ind, emph "indeed" |
| 68-05 | 45 |  | Rebuild row: `\| petānam- \| adj \| masc.gen.pl \| of departed, deceased, dead \|` | A2 | keep (8) — DPD peta 1 = pp, peta 2 = masc "departed"; the rebuild only repairs the shifted columns and keeps the source POS `adj` |
| 68-06 | 47 | `evaṃ` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 68-07 | 58 | `kho` | Grammar ∅ → `emph` | B-P3 | keep (9) |
| 68-08 | 63 | `dīgharattaṃ` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 68-09 | 66 | `ṭhānaso` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 68-10 | 69 |  | `it is benefits immediately` → `it benefits immediately` | A6 | keep (9) |
| 68-11 | 77 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 68-12 | 82 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |

## 69 — Paṃsu-Kūla for the Dead

`per-69-pamsu-kula.md` — 8 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 69-01 | 11 | `vata` | Grammar ∅ → `excl` | B-P4 | adjust: per-69-pamsu-kula.md:11 `\| vata \| ind \| \|` → `\| vata \| ind \| emph \|` (DPD vata 1.2 = emph "certainly; surely; indeed", which fits the gloss "indeed"; vata 1.1 excl = "oh!") (8) |
| 69-02 | 56 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 69-03 | 58 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 69-04 | 60 | `tatha'eva-` | POS `ind` → `sandhi` (leave Grammar empty) | B-P7 | keep (9) — DPD tatheva 1 = sandhi, adv + ind "likewise" |
| 69-05 | 65 | `ettha` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 69-06 | 79 | `aciraṃ` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 69-07 | 80 | `vata-` | Grammar ∅ → `excl` | B-P4 | adjust: per-69-pamsu-kula.md:80 `\| vata- \| ind \| \|` → `\| vata- \| ind \| emph \|` (gloss "indeed" = DPD vata 1.2 emph) (8) |
| 69-08 | 89 | `va` | Grammar ∅ → `emph` | B-P3 | drop: DPD va 1.1 = ind, abbrev of iva "like; as", which is the row's gloss; emph would be va 2.1 (abbrev of eva) |

## 70 — Sharing and Aspirations

`per-70-sharing-and-aspirations.md` — 24 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 70-01 | 28 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 70-02 | 30 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 70-03 | 45 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 70-04 | 55 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 70-05 | 56 |  | `Indras , kings` → `Indras, kings` | A6 | keep (9) |
| 70-06 | 57 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 70-07 | 59 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 70-08 | 71 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 70-09 | 75 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 70-10 | 89 | `me` | `masc.ins.sg` → `1.ins.sg` — personal pronoun | A4 | keep (9) — DPD me 2 = 1st instr sg of ahaṃ |
| 70-11 | 99 | `dentu` | `pr.3.pl` → `imp.3.pl` — `-ntu` imperative ("may they give") | A4 | keep (8) — DPD detu = imp of deti (de + tu); dentu is the 3rd plural of the same (dentu itself has no headword) |
| 70-12 | 115 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 70-13 | 123 | `khippaṃ-` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 70-14 | 125 | `sulabhe` | Grammar `imp.reflx.1.sg` → `imp.refl.1.sg` | A5.3 | undecided — owner decision A5.3/B11.2 |
| 70-15 | 126 | `c'eva` | POS `ind` → `sandhi` (leave Grammar empty) | B-P7 | keep (7) — DPD silent: c'eva (no headword; DPD has only the idiom na ceva); DPD lists cāpi as sandhi |
| 70-16 | 141 | `yāva` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 70-17 | 152 | `sabbadā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 70-18 | 153 | `yeva` | POS `ind` → `sandhi` (leave Grammar empty) | B-P7 | keep (9) |
| 70-19 | 154 | `yattha` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 70-20 | 157 | `bhave` | Grammar `imp.reflx.1.sg` → `imp.refl.1.sg` | A5.3 | adjust: per-70-sharing-and-aspirations.md:157 `\| bhave \| verb \| imp.reflx.1.sg \|` → `\| bhave \| verb \| opt.1.sg \|` (DPD bhave = opt of bhavati, not imp and not reflx, so the A5.3/B11.2 choice no longer applies; DPD gives no person, so 1.sg is kept from the source and the translation "may I be") (6) |
| 70-21 | 185 | `me` | `masc.gen.sg` → `1.gen.sg` — personal pronoun | A4 | keep (9) — DPD me 5 = 1st gen sg of ahaṃ |
| 70-22 | 187 |  | `may Maras do not get a chance` → `may Māras not get a chance` (2×) *(same fix at: per-70:187, per-70:230)* | A6 | keep (8) |
| 70-23 | 210 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 70-24 | 230 |  | `may Maras do not get a chance` → `may Māras not get a chance` (2×) *(same fix at: per-70:187, per-70:230)* | A6 | keep (8) |

## 71 — Sharing of All Merits

`per-71-sharing-of-all-merits.md` — 10 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 71-01 | 15 | `idāni` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 71-02 | 22 | `bhāgino` | `masc.nom.p` → `masc.nom.pl` — truncated | A4 | keep (9) — DPD bhāgī 1 = masc |
| 71-03 | 37 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |
| 71-04 | 69 |  | `Beings lives in the world` → `Beings live in the world` | A6 | keep (9) |
| 71-05 | 82 | `sayaṃ` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 71-06 | 90 |  | `sharing of merrit` → `sharing of merit` | A6 | keep (9) |
| 71-07 | 100 |  | Rebuild row: `\| anumodana- \| noun \| \| rejoicing, satisfaction, thanks, appreciation, blessing, thanksgiving \|` | A3 | keep (8) |
| 71-08 | 104 | `sadā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 71-09 | 112 |  | **D6** `\| tesāsāṃ \| ? \| \| \|` — empty analysis. Likely `tesāsā` = `tesaṃ` + `āsā` ("their wishes"); verify against chant line and DPD (covers L112–113). | A8-D6 | adjust: per-71:112 `\| tesāsāṃ \| ? \| \| \|` → two rows `\| tesaṃ- \| pron \| masc.gen.pl \| their \|` + `\| āsā \| noun \| fem.nom.sg \| wish, hope \|` (DPD tesaṃ 2 = gen pl "their"; DPD āsā = fem "wish; hope"; singular because sijjhataṃ is 3rd sg, see 1574; DPD silent: sijjhataṃ) (6) |
| 71-10 | 113 |  | **D6** `sijjhataṃ=sijjhanaṃ \| noun \| nt.acc.sg` should probably be `sijjhataṃ \| verb \| imp.3.sg (middle) \| may (they) succeed`; verify. | A8-D6 | adjust: per-71:113 `\| sijjhataṃ=sijjhanaṃ \| noun \| nt.acc.sg \| happening; success. \|` → `\| sijjhataṃ \| verb \| imp.3.sg \| may (it) succeed \|`, with refl marking per owner decision A5.3/B11.2. DPD sijjhati 1 = pr "succeeds", so the word is a verb, not a noun; DPD silent: sijjhataṃ (the imp 3rd sg parse rests on the -taṃ ending) (6) |

## 72 — Sharing of Merits with the Departed

`per-72-sharing-of-merits-with-the-departed.md` — 1 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 72-01 | 18 | `ñātinaṃ` | `nom.dat.pl` → `masc.dat.pl` — garbled case tag | A4 | keep (9) — DPD ñāti = masc |

## 73 — Sharing of Merits with the Devas

`per-73-sharing-of-merits-with-the-devas.md` — 2 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 73-01 | 12 | `ettāvatā` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 73-02 | 13 | `ca` | Grammar ∅ → `conj` | B-P2 | keep (8) — DPD ca 2.1 = ind, conj "and" |

## 74 — The Highest Honour and Aspirations

`per-74-the-highest-honour-and-aspirations.md` — 6 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| 74-01 | 46 | `me` | `1.g.sg` → `1.gen.sg` — truncated | A4 | keep (7) — the truncated `g` means gen; DPD has both me 3 = dat "to me; for me" (the row's gloss) and me 5 = gen; expanding `g` → `gen` stands unless the owner prefers dat |
| 74-02 | 57 | `yāva` | Grammar ∅ → `adv` | B-P1 | keep (9) |
| 74-03 | 61 |  | `a assembly` → `an assembly` | A6 | keep (9) |
| 74-04 | 69 | `kho` | Grammar ∅ → `emph` | B-P3 | keep (9) |
| 74-05 | 123 | `addhā` | Grammar ∅ → `excl` | B-P4 | keep (9) |
| 74-06 | 140 | `āsavakkhayā-` | Grammar `masc` → ∅ (reviewer blanks bare gender on compound member; audit 5.7 keeps it) — policy 11.3 | B-11.3 | undecided — owner decision A5.7/B11.3 |

## Word-by-word analysis of SBS Anumodana chants (Ṭhanuttamo)

`word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md` — 7 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| wbw-01 | 145 | `*paripūrenti*` | `vb. first pers. act. pl.` → `vb. third pers. act. pl.` — *`-enti` = 3rd pl.* | B-N136 | keep (8) |
| wbw-02 | 149 | `*sāgaraṁ*` | `m. n., nom. sg. object of main clause` → `m. n., acc. sg. object of main clause` — *`-ṁ` ending, object* | B-N137 | keep (8) |
| wbw-03 | 163 | `*upakappati*` | `vb. pres. ind. first pers. act. sg.` → `vb. pres. ind. third pers. act. sg.` — *`-ati` = 3rd sg.* | B-N138 | keep (9) |
| wbw-04 | 231 | `*te*` | `pers. pron. third pers. dat. sg.` → `pers. pron. second pers. dat. sg.` — *`te` = "for you"; (line 391 already says second pers.)* | B-N139 | keep (9) — DPD te 2.3 = 2nd dat sg of tvaṃ |
| wbw-05 | 443 | `*sukhassa*` | `m. n. gen. sg.` → `neutr. n. gen. sg.` — *`sukha` is neuter* | B-N140 | keep (8) |
| wbw-06 | 449 | `*sukhaṁ*` | `m. n. acc. sg.` → `neutr. n. acc. sg.` — *`sukha` is neuter* | B-N141 | keep (8) |
| wbw-07 | 627 | `*sabbe*` | `second pers. adj. pron. nom. pl.` → `adj. pron. nom. pl.` — *`sabbe` = "all", not a personal pronoun* | B-N142 | keep (8) |

## Post Pātimokkha

`post-patimokkha.md` — 3 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| post-01 | 9 | `handa` | Grammar ∅ → `excl` | B-P4 | keep (9) |
| post-02 | 19 | `karomase` | Grammar `ref.imp.1.pl` → `imp.refl.1.pl` | A5.3 | undecided — owner decision A5.3/B11.2 |
| post-03 | 27 | `namo` | Grammar ∅ → `excl` | B-P4 | keep (9) |

## Pubbakicca analysis

`pubbakicca-analysis.md` — 74 suggestion(s)

| ID | Line | Word | Suggestion | Source | Re-check |
|---|---|---|---|---| --- |
| pubbakicca-01 | 10 | `me` | Grammar `1st.acc.sg` → `1.acc.sg` | A5.1 | keep (8) |
| pubbakicca-02 | 13 | `detu` | Grammar `imp.3rd.sg` → `imp.3.sg` | A5.1 | keep (8) |
| pubbakicca-03 | 24 | `karomi` | Grammar `pr.1st.sg` → `pr.1.sg` | A5.1 | keep (8) |
| pubbakicca-04 | 41 | `hoti` | Grammar `pr.3rd.sg` → `pr.3.sg` | A5.1 | keep (8) |
| pubbakicca-05 | 50 | `\#taṃ` | Grammar `nt.` → `nt` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-06 | 51 | `\#ṭhāna` | Grammar `nt.` → `nt` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-07 | 56 | `\#padīpa` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-08 | 60 | `\#āsana` | Grammar `nt.` → `nt` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-09 | 64 | `\#pānīya` | Grammar `nt.` → `nt` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-10 | 65 | `\#paribhojanīya` | Grammar `nt.` → `nt` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-11 | 84 | `\#akata` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-12 | 120 | `\#padīpa` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-13 | 127 | `n'atthi` | Grammar `pr.3rd.sg` → `pr.3.sg` | A5.1 | keep (8) |
| pubbakicca-14 | 130 | `bhikkhūnaṃ` | `masc.gen.sg` → `masc.gen.pl` — `-ūnaṃ` plural | A4 | keep (9) |
| pubbakicca-15 | 132 | `jānantehi` | Grammar `masc.instr.pl` → `masc.ins.pl` | A5.2 | keep (8) |
| pubbakicca-16 | 133 | `bhikkhūhi` | Grammar `masc.instr.pl` → `masc.ins.pl` | A5.2 | keep (8) |
| pubbakicca-17 | 136 | `honti` | Grammar `pr.3rd.pl` → `pr.3.pl` | A5.1 | keep (8) |
| pubbakicca-18 | 143 | `chand'āharaṇa` | Grammar `nt.` → `nt` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-19 | 145 | `\#chanda` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-20 | 146 | `\#āharaṇa` | Grammar `nt.` → `nt` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-21 | 148 | `\#pārisuddhi` | Grammar `fem.` → `fem` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-22 | 158 | `n'atthi` | Grammar `pr.3rd.sg` → `pr.3.sg` | A5.1 | keep (8) |
| pubbakicca-23 | 193 | `\#hemanta` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-24 | 194 | `\#gimha` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-25 | 195 | `\#vassāna` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-26 | 198 | `honti` | Grammar `pr.3rd.pl` → `pr.3.pl` | A5.1 | keep (9) |
| pubbakicca-27 | 222 | `iminā` | Grammar `masc.instr.sg` → `masc.ins.sg` | A5.2 | keep (9) |
| pubbakicca-28 | 223 | `pakkhena` | Grammar `masc.instr.sg` → `masc.ins.sg` | A5.2 | keep (9) |
| pubbakicca-29 | 232 |  | **D6** `\| attha \| card \| x.nom.pl \| eight \|` — Pāḷi typo for `aṭṭha`? Verify against chant line before touching Pāḷi text. | A8-D6 | adjust: pubbakicca-analysis.md:232 `\| attha \| card \| x.nom.pl \| eight \|` → `\| aṭṭha \| card \| x.nom.pl \| eight \|` (Word column only. Chant line 203 and row 220 already read aṭṭha. In DPD, aṭṭha is card "eight" and attha is masc "meaning") (9) |
| pubbakicca-30 | 244 | `sabbehi` | Grammar `masc.instr.pl` → `masc.ins.pl` | A5.2 | keep (9) |
| pubbakicca-31 | 245 | `āyasmantehi` | Grammar `masc.instr.pl` → `masc.ins.pl` | A5.2 | keep (9) |
| pubbakicca-32 | 258 | `\#bhikkhu` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-33 | 263 | `\#uposatha` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-34 | 283 | `\#uposatha` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-35 | 288 | `honti` | Grammar `pr.3rd.pl` → `pr.3.pl` | A5.1 | keep (9) |
| pubbakicca-36 | 295 | `sabbehi` | Grammar `masc.instr.pl` → `masc.ins.pl` | A5.2 | keep (9) |
| pubbakicca-37 | 296 | `āyasmantehi` | Grammar `masc.instr.pl` → `masc.ins.pl` | A5.2 | keep (9) |
| pubbakicca-38 | 299 | `\#\#bhikkhu` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-39 | 315 | `n'atthi` | Grammar `pr.3rd.sg` → `pr.3.sg` | A5.1 | keep (9) |
| pubbakicca-40 | 326 | `\#karaṇa` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-41 | 329 | `\#pubba` | Grammar `nt.` → `nt` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-42 | 333 | `\#nikkaraṇa` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-43 | 335 | `\#\#karaṇa` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-44 | 345 | `\#pubba` | Grammar `nt.` → `nt` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-45 | 348 | `hoti` | Grammar `pr.3rd.sg` → `pr.3.sg` | A5.1 | keep (9) |
| pubbakicca-46 | 370 |  | **D3** `<br>` inside table cells (lines 370, 376). Policy: keep (note the exception) or convert `A<br>(or)<br>B` → `A (or) B`. | A8-D3 | undecided — owner decision D3 (`<br>` is still present at pubbakicca-analysis.md:370 `as per<br>or<br>since` and :376 `<br>(or)<br>`) |
| pubbakicca-47 | 390 | `\#saṅgha` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-48 | 391 | `\#uposatha` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-49 | 401 | `saṅghena` | Grammar `masc.instr.sg` → `masc.ins.sg` | A5.2 | keep (9) |
| pubbakicca-50 | 431 | `\#vikāla` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-51 | 432 | `\#bhojana` | Grammar `nt.` → `nt` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-52 | 437 | `\#sabhāga` | Grammar `fem.` → `fem` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-53 | 441 | `vijjanti` | Grammar `pr.pass.3rd.pl` → `pr.pass.3.pl` | A5.1 | keep (9) |
| pubbakicca-54 | 456 | `\#karaṇa` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-55 | 461 | `\#vajjanīya` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-56 | 464 | `n'atthi` | Grammar `pr.3rd.sg` → `pr.3.sg` | A5.1 | keep (9) |
| pubbakicca-57 | 478 | `imehi` | Grammar `nt.instr.pl` → `nt.ins.pl` | A5.2 | keep (9) |
| pubbakicca-58 | 479 | `catūhi` | Grammar `nt.instr.pl` → `nt.ins.pl` | A5.2 | keep (9) |
| pubbakicca-59 | 480 | `lakkhaṇehi` | Grammar `nt.instr.pl` → `nt.ins.pl` | A5.2 | keep (9) |
| pubbakicca-60 | 482 | `pattakallaṃ` | Grammar `nt.` → `nt` | A5.7 | adjust: pubbakicca-analysis.md:482 `\| pattakallaṃ \| noun \| nt. \|` → `\| pattakallaṃ \| noun \| nt.nom.sg \|` (a headword, not a compound member, so B11.3 does not apply. It is the predicate of `nāma hoti`, so case and number are missing, not just the period. DPD pattakalla = nt, comp "good time; suitable occasion", which confirms noun and nt) (8) |
| pubbakicca-61 | 483 | `\#patta` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-62 | 486 | `hoti` | Grammar `pr.3rd.sg` → `pr.3.sg` | A5.1 | keep (9) |
| pubbakicca-63 | 489 | `\#yutta` | Grammar `nt.` → `nt` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-64 | 499 | `\#uposatha` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-65 | 502 | `\#patta` | Grammar `nt.` → `nt` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-66 | 508 | `saṅghena` | Grammar `masc.instr.sg` → `masc.ins.sg` | A5.2 | keep (9) |
| pubbakicca-67 | 518 | `pubbakaraṇa` | Grammar `nt.` → `nt` | A5.7 | undecided — owner decision A5.7/B11.3 (no `#` mark, but it is the first member of `pubbakaraṇa-pubbakiccāni` on chant line 514) |
| pubbakicca-68 | 519 | `\#pubba` | Grammar `nt.` → `nt` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-69 | 520 | `\#karaṇa` | Grammar `nt.` → `nt` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-70 | 522 | `\#pubba` | Grammar `nt.` → `nt` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-71 | 528 | `\#bhikkhu` | Grammar `masc.` → `masc` | A5.7 | undecided — owner decision A5.7/B11.3 |
| pubbakicca-72 | 530 | `anumatiyā` | Grammar `fem.instr.sg` → `fem.ins.sg` | A5.2 | keep (9) |
| pubbakicca-73 | 534 | `karomi` | Grammar `pr.1st.sg` → `pr.1.sg` | A5.1 | keep (9) |
| pubbakicca-74 | 537 |  | **D7** No footer nav (no `[index]` link) and not referenced from `docs/6-pali-class/sbs-per-analysis.md` (post-patimokkha.md is, at index line 114). Recommend: add a footer index link and an index entry. | A8-D7 | adjust: docs/6-pali-class/sbs-per-analysis.md:114, after the post-patimokkha line, add `In addition there is an analysis of [Dhammayuttika Pubba-kicca analysis](sbs-per-analysis/pubbakicca-analysis.md)` (link text = the page's H1). The footer `[index]` link stays undecided — owner decision: footer nav in the source or added by a script (CLAUDE.md says navigation goes in scripts) (7) |

## Fresh look (2026-11-16)

### Summary

| Category | per-01–05 | 06–09 | 10–15 | 16–18 | 19 a | 19 b | 20–22 | 23 | 24 | 25–27 | 28–31 | 32–39 | 40–42 | 43–52 | 53–54 | 55–59 | 60–65 | 66–73 | 74, post | pubbakicca | Anum. a | Anum. b | Total | Conf. ≥ 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A. Pāli and grammar content errors | 2 | 17 | 16 | 15 | 4 | 25 | 20 | 9 | 13 | 33 | 28 | 12 | 20 | 16 | 28 | 25 | 34 | 27 | 24 | 22 | 18 | 16 | 424 | 273 |
| B. Tables, paradigms and lists that disagree with each other or themselves | 0 | 8 | 3 | 0 | 4 | 3 | 1 | 1 | 1 | 0 | 6 | 4 | 0 | 8 | 0 | 4 | 1 | 6 | 1 | 6 | 5 | 1 | 63 | 30 |
| C. Translation and gloss problems | 3 | 2 | 7 | 9 | 5 | 6 | 1 | 3 | 9 | 7 | 5 | 6 | 5 | 5 | 7 | 4 | 12 | 6 | 1 | 4 | 4 | 3 | 114 | 51 |
| D. English typos and grammar | 11 | 25 | 32 | 25 | 19 | 21 | 30 | 21 | 22 | 40 | 39 | 18 | 50 | 22 | 44 | 23 | 19 | 15 | 10 | 11 | 7 | 7 | 511 | 284 |
| E. Markdown defects that affect rendering | 0 | 4 | 1 | 0 | 0 | 4 | 0 | 0 | 1 | 0 | 0 | 2 | 8 | 0 | 4 | 6 | 3 | 4 | 0 | 15 | 0 | 13 | 65 | 37 |
| F. Convention drift | 12 | 5 | 14 | 6 | 16 | 10 | 6 | 3 | 21 | 21 | 6 | 15 | 21 | 10 | 3 | 6 | 9 | 18 | 2 | 5 | 1 | 3 | 213 | 58 |
| G. Links | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| H. Data to re-verify (forms, references, counts) | 1 | 1 | 5 | 4 | 1 | 8 | 0 | 0 | 11 | 0 | 2 | 5 | 4 | 1 | 0 | 0 | 2 | 3 | 3 | 3 | 1 | 1 | 56 | 5 |
| I. Further details on the material under review | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | **29** | **62** | **78** | **59** | **49** | **77** | **58** | **37** | **78** | **101** | **86** | **62** | **108** | **62** | **86** | **68** | **80** | **79** | **41** | **66** | **36** | **44** | **1446** | **738** |

Method: each of the 22 slices of `docs/6-pali-class/sbs-per-analysis/` was read line by line (Opus), every Pāḷi item was checked against DPD, and every excerpt was checked with `verify_rows.py`. Rows the old audit already has are left out. Open Policies pairs in the review-by-chant file are owner decisions; rows that depend on them say so.
Date: 2026-11-16. Location is `<file>.md:<line>` under `docs/6-pali-class/sbs-per-analysis/`; a row that cites several lines lists every line that carries the excerpt. Slice labels are the per-NN file numbers ("Anum." = the Ṭhanuttamo anumodana file, two halves).
Conf. below 8 means "check before changing". Rows with no concrete Suggested are in category H.

### A. Pāli and grammar content errors

| Location | Current | Problem | Suggested | Conf. |
| --- | --- | --- | --- | --- |
| per-03-homage-to-the-buddha.md:45 | `\| buddho \| adj \| masc.nom.sg \| awakened, woke up, understood \|` | Here `buddho` is the epithet (translation line 48: "Awakened One"), i.e. DPD buddha 1 (masc, "Buddha; Awakened One"), not buddha 2 (pp, "awakened; woke up; understood"). Known row 03-05 covers `bhagavā` on line 46 only | POS `noun`; English `Buddha, Awakened One` | 9 |
| per-03-homage-to-the-buddha.md:69 | `\| sadevamanussaṃ \| adj \| masc.acc.sg \|` | Adj (DPD sadevamanussa) qualifying `pajaṃ` (DPD pajā 2, fem; row 68 fem.acc.sg), so it is feminine accusative, not masculine | `fem.acc.sg` | 8 |
| per-06-salutation-to-the-triple-gem.md:206 | `\| tassa \| pron \| masc.gen.sg \| of this \|` | `tassa pabhāvasiddhiyā` refers back to `puññaṃ` (192, nt; DPD `puñña 1` nt), so the gender is neuter. | `nt.gen.sg` | 6 |
| per-06-salutation-to-the-triple-gem.md:254 | `domanassupāyāsāpi dukkha` | The chant line ends `dukkha`; the table (273) and the standard text read `dukkhā` (plural predicate). | `domanassupāyāsāpi dukkhā` | 8 |
| per-06-salutation-to-the-triple-gem.md:273 | `\| dukkhā \| adj \| fem.nom.sg \| uncomfortable, painful, unpleasant; unsatisfactory \|` | This predicate agrees with `upāyāsā` (271, `masc.nom.pl`; DPD `upāyāsa` masc), the last member of the plural dvanda, not with a feminine singular. | `masc.nom.pl` | 8 |
| per-06-salutation-to-the-triple-gem.md:302 | `\| \>yaṃ \| pron \| masc.acc.sg \|` | `yaṃ` is "what" (the thing not obtained), the object of `labhati`, so it is neuter (DPD `yaṃ 2`: masc fem & nt acc sg). Known 06-29 touches line 301 only. | `nt.acc.sg` | 6 |
| per-06-salutation-to-the-triple-gem.md:303 | `\| \>icchaṃ \| prp \| masc.acc.sg \|` | The participle goes with the implied subject of `labhati` ("one, wishing, does not get"). It is nominative, not accusative. | `masc.nom.sg` | 6 |
| per-06-salutation-to-the-triple-gem.md:306 | `\| tam'pi \| pron \| masc.acc.sg \|` | `tampi` is the subject of the predicate `dukkhaṃ` (307, `nt.nom.sg`); DPD `taṃ 1.1`: nt nom sg of ta. | `nt.nom.sg` | 8 |
| per-06-salutation-to-the-triple-gem.md:311 | `pañcupādānakkhandhā dukkha` | The chant line ends `dukkha`; the table (319) and the standard text read `dukkhā`. | `pañcupādānakkhandhā dukkhā` | 8 |
| per-06-salutation-to-the-triple-gem.md:319 | `\| dukkhā \| adj \| fem.nom.sg \| uncomfortable, painful, unpleasant unsatisfactory \|` | This predicate agrees with `khandhā` (318, `masc.nom.pl`; DPD `khandha` masc). | `masc.nom.pl` | 8 |
| per-06-salutation-to-the-triple-gem.md:327 | `seyyathidaṃ` | The chant line (323) and DPD spell it `seyyathīdaṃ`. | `seyyathīdaṃ` | 9 |
| per-06-salutation-to-the-triple-gem.md:330 | `\| vedan- \|` | The member is cut short: `vedanūpādāna` is `vedanā + upādāna` (DPD `vedanā` fem). | `vedanā-` | 8 |
| per-06-salutation-to-the-triple-gem.md:402 | `\| sabbe \| adj \| masc.nom.pl \|` | DPD gives `sabbe` as pron, and per-08:35 uses `pron`. | POS `pron` | 8 |
| per-06-salutation-to-the-triple-gem.md:412 | `\| sabbe \| adj \| masc.nom.pl \|` | DPD gives `sabbe` as pron, and per-08:35 uses `pron`. | POS `pron` | 8 |
| per-06-salutation-to-the-triple-gem.md:456 | `app”eva'nāma-` | A curly double quote `”` stands where an apostrophe belongs (chant: `appevanāma`; DPD `appeva nāma`). | `app'eva'nāma-` | 8 |
| per-06-salutation-to-the-triple-gem.md:471 | `\| taṃ \| noun \| masc.acc.sg \| that, he \|` | `taṃ` is a pronoun (DPD: pron; elsewhere in this file it is `pron`). | POS `pron` | 9 |
| per-07-the-buddhas-first-exclamation.md:36 | `\| gehaṃ \| noun \| masc.acc.sg \|` | `geha` is neuter (DPD `geha` nt). | `nt.acc.sg` | 9 |
| per-08-respect-for-the-dhamma.md:63 | `\| sāsanaṃ \| noun \| masc.acc.sg \| teaching \|` | `sāsana` is neuter (DPD `sāsana 1` nt). | `nt.acc.sg` | 9 |
| per-08-respect-for-the-dhamma.md:80 | `\| vipākino \| adj \| masc.nom.sg \|` | The word agrees with `ubho` ("both", plural; DPD `ubho` nom & acc pl), and the `-ino` ending is nom.pl. DPD has no headword `vipākin`. Known 08-13 touches only the English cell of this row. | `masc.nom.pl` | 7 |
| per-10-the-patimokkha-exhortation.md:17 | `\| ūpasampadā \| noun \|` | Headword split from the sandhi `kusalassūpasampadā` (line 8) keeps the sandhi-lengthened vowel; DPD headword is `upasampadā` (fem) | `\| upasampadā \| noun \|` | 8 |
| per-11-the-three-characteristics.md:56 | `\| anattā \| adj \| masc.nom.sg \|` | Tagged adj (DPD anatta 1 adj; glosses are the adj glosses) but singular, although it is predicate of plural `dhammā` (line 55); an adj here must be plural. Known 11-06 (B-X4✗) touches only the `.sg` notation | `\| anattā \| adj \| masc.nom.pl \|` | 7 |
| per-11-the-three-characteristics.md:67 | `\| appakā \| noun \| masc.nom.pl \|` | DPD appaka 1 adj "small; few; little"; predicate of `te`, so adj masc.nom.pl (DPD's noun appaka 2/3 is nt, never masc) | `\| appakā \| adj \| masc.nom.pl \|` | 8 |
| per-11-the-three-characteristics.md:77 | `\| tīram- \| noun \| nt \|` | Not a compound member: `tīram-evānudhāvati` is sandhi, `tīraṃ` (DPD tīra nt) is the acc object of `anudhāvati`; case and number missing (unaffected by B11.3, which concerns real compound members) | `\| tīram- \| noun \| nt.acc.sg \|` | 8 |
| per-11-the-three-characteristics.md:99 | `\| maccudheyyaṃ \| noun \| masc.acc.sg \|` | DPD maccudheyya nt | `\| maccudheyyaṃ \| noun \| nt.acc.sg \|` | 9 |
| per-11-the-three-characteristics.md:100 | `\| sud'uttaraṃ \| adj \| masc.acc.sg \|` | Qualifies `maccudheyyaṃ` (DPD nt, see line 99); DPD suduttara adj | `\| sud'uttaraṃ \| adj \| nt.acc.sg \|` | 8 |
| per-13-from-the-elder-ratthapala.md:5 | `R aṭṭhapāla-thera-gāthā` | Stray space inside the name (DPD raṭṭhapāla) | `Raṭṭhapāla-thera-gāthā` | 9 |
| per-13-from-the-elder-ratthapala.md:163 | `\| jaraṃ \| noun \| masc.acc.sg \|` | DPD: jarā fem | `\| jaraṃ \| noun \| fem.acc.sg \|` | 9 |
| per-13-from-the-elder-ratthapala.md:189 | `\| vosānaṃ- \| noun \| \|` | Grammar empty; `vosānaṃ` (DPD vosāna nt) is the acc object of `adhigacchati` (sandhi, not compound member) | `\| vosānaṃ- \| noun \| nt.acc.sg \|` | 8 |
| per-14-from-the-elder-parapariya.md:159 | `\| attha- \| \| \| goal` | POS empty; DPD attha 1.3 masc noun "purpose; use; function; goal" | `\| attha- \| noun \| \| goal` | 8 |
| per-14-from-the-elder-parapariya.md:181 | `\| siniddhā \| pp \| masc.nom.pl \|` | Plural is wrong: it qualifies `teladhārā` (fem.nom.sg) in the simile for `iriyāpatho` (sg); no masc pl referent; `-ā` sg form is fem | `\| siniddhā \| pp \| fem.nom.sg \|` | 6 |
| per-15-on-protection.md:32 | `\| muni \| noun \|` | Chant line 21 has `munī` (metrical nom sg of DPD muni masc; cf. per-14:210 row `munī`) | `\| munī \| noun \|` | 7 |
| per-15-on-protection.md:48 | `\| enaṃ \| noun \| masc.acc.sg \|` | `enaṃ` is a pronoun (DPD silent: `ena` no headword in saved output) | `\| enaṃ \| pron \| masc.acc.sg \|` | 7 |
| per-15-on-protection.md:50 | `\| enaṃ \| noun \| masc.acc.sg \|` | `enaṃ` is a pronoun (DPD silent, as line 48) | `\| enaṃ \| pron \| masc.acc.sg \|` | 7 |
| per-15-on-protection.md:56 | `\| ākirate \| verb \| opt.3.sg \|` | DPD ākirati pr; `-te` is the present reflexive ending, not optative (corpus: `labhate` per-13:158 `pr.refl.3.sg`); keeping or dropping `refl` is policy A5.3/B11.2 (`pr.3.sg` under B11.2), not this row | `\| ākirate \| verb \| pr.refl.3.sg \|` | 8 |
| per-15-on-protection.md:95 | `\| ūpakaḍḍhati \|` | Chant line 82 has `nirayāy'upakaḍḍhati`; DPD headword `upakaḍḍhati` | `\| upakaḍḍhati \|` | 9 |
| per-16-miscellaneous-verses.md:71 | `yaṃ \| pron \| masc.acc.sg \| whatever, that which` | `yaṃ pubbe taṃ visosehi`: relative pronoun with no masculine referent ("whatever was before"); neuter (DPD yaṃ 2 = acc sg of any gender, so the gender must come from context) | Grammar `masc.acc.sg` → `nt.acc.sg` | 7 |
| per-16-miscellaneous-verses.md:73 | `taṃ \| pron \| masc.acc.sg \| that` | correlative of neuter `yaṃ` (object of `visosehi`); neuter (DPD taṃ 1.2 = acc sg of any gender) | Grammar `masc.acc.sg` → `nt.acc.sg` | 7 |
| per-16-miscellaneous-verses.md:78 | `kiñcanaṃ \| noun \| nt.acc.sg` | `pacchā te m'āhu kiñcanaṃ`: `kiñcanaṃ` is the subject of `āhu` ("let there not be anything"), so nominative; DPD kiñcana 1.2 nt gives no case. Known 16-06 touches line 77 (`m'āhu`), not this row | Grammar `nt.acc.sg` → `nt.nom.sg` | 6 |
| per-16-miscellaneous-verses.md:124 | `amohayittha \| verb \| aor.2.pl` | subject is `maccurājā` (3 sg); `-ittha` here is the 3 sg (reflexive) aorist ending, not 2 pl. DPD has no entry for the form (only `mohayati`, caus pr). Whether to add a reflexive tag falls under the open A5.3/B11.2 pair (owner) | Grammar `aor.2.pl` → `aor.3.sg` | 6 |
| per-17-a-single-excellent-night.md:89 | `ratto- \| noun \| \| night` | final member of `bhadd'eka-ratto` (nominative before `ti`) has empty Grammar; DPD bhaddekaratta 2 = adj (bahubbīhi) "having a single auspicious night", so masc nom sg agreeing with the sage described | Grammar ∅ → `masc.nom.sg` | 6 |
| per-17-a-single-excellent-night.md:90 | `ti – \| ind` | Pāḷi cell carries a stray en dash from the translation | `ti` | 7 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:17 | `sevitabbā \| pp \| masc.nom.pl \| should be associated with` | `-tabba` form is a future passive participle, not pp (DPD sevitabba 1 = ptp of sevati) | POS `pp` → `ptp` | 9 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:101 | `sammāsati \| noun \| masc.nom.sg` | `sammāsati` is feminine (DPD sammāsati 1 fem; sati 1.2 fem) | Grammar `masc.nom.sg` → `fem.nom.sg` | 9 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:169 | `\>yaṃ \| pron \| masc.acc.sg` | `yampicchaṃ … tampi dukkhaṃ`: "what one wishes", neuter object (DPD yaṃ 2 = acc sg of any gender). Known 18-09 touches line 168 only | Grammar `masc.acc.sg` → `nt.acc.sg` | 7 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:170 | `\>icchaṃ \| adj \| masc.acc.sg \| wishing for, desiring, wanting` | `icchaṃ` is the present participle (nom sg) of `icchati`, agreeing with the unexpressed subject of `labhati`; DPD has no entry for the form (only `icchati` pr) | POS `adj` → `prp`; Grammar `masc.acc.sg` → `masc.nom.sg` | 7 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:173 | `tam'pi \| pron \| masc.acc.sg` | `tampi dukkhaṃ`: subject of a nominal sentence with nt `dukkhaṃ` (DPD taṃ 1.1 = nt nom sg) | Grammar `masc.acc.sg` → `nt.nom.sg` | 7 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:186 | `dukkhā \| adj \| fem.nom.sg` | predicate of `pañcupādānakkhandhā` (line 185 `masc.nom.pl`; DPD khandha masc); adj `dukkha` must agree | Grammar `fem.nom.sg` → `masc.nom.pl` | 8 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:272 | `dukkhaṃ \| noun \| nt.acc.sg` | `taṃ … idaṃ dukkhaṃ ariya-saccaṃ pariññeyyan-ti`: subject, in agreement with `idaṃ`/`ariya-saccaṃ` (both tagged `nt.nom.sg`; DPD idiom `dukkhaṃ ariyasaccaṃ` nt + nt). Known 18-11 (C4) asks the same nom/acc question at line 245, not here | Grammar `nt.acc.sg` → `nt.nom.sg` | 7 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:286 | `dukkhaṃ \| noun \| nt.acc.sg.` | same as line 272 (`… pariññātan-ti`): nominative subject; known 18-17 on this cell only strips the period, not the case | Grammar `nt.acc.sg.` → `nt.nom.sg` | 7 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:363 | `ti-parivaṭṭaṃ \| noun \| nt.acc.sg` | DPD tiparivaṭṭa = masc comp (digu) "three phases"; source tags it neuter. The parallel member `ākāraṃ` (DPD dvādasākāra masc) at line 365 is already `masc.acc.sg` | Grammar `nt.acc.sg` → `masc.acc.sg` | 7 |
| per-19-anupubba-sikkha.md:22 | `\| kule \| noun \| masc.loc.sg \|` | kula (family) is neuter (DPD kula 1: nt) | `\| kule \| noun \| nt.loc.sg \|` | 9 |
| per-19-anupubba-sikkha.md:176 | `\| sīlavā \| noun \| masc.nom.sg \| virtuous;` | sīlavant is an adjective (DPD sīlavant: adj); the gloss is adjectival too | `\| sīlavā \| adj \| masc.nom.sg \| virtuous;` | 8 |
| per-19-anupubba-sikkha.md:186 | `\| vajjesu \| noun \| masc.loc.pl \|` | vajja "fault" is neuter (DPD vajja 2.1: nt) | `\| vajjesu \| noun \| nt.loc.pl \|` | 9 |
| per-19-anupubba-sikkha.md:260 | `\| methunā \| noun \| masc.abl.sg \|` | in `methunā gāmadhammā` methuna qualifies gāmadhamma (masc), so it is DPD methuna 1 adj "sexual"; the noun methuna 2 is neuter and could not be masc.abl; the gloss `from sexual intercourse` follows the noun reading and would need adjusting too | `\| methunā \| adj \| masc.abl.sg \|` | 7 |
| per-19-anupubba-sikkha.md:675 | `indriyesu \| noun \| masc.loc.pl` | indriya is neuter (DPD indriya 1–3: nt) | `nt.loc.pl` | 8 |
| per-19-anupubba-sikkha.md:694 | `cakkhu-indriyaṃ \| noun \| masc.acc.sg` | cakkhundriya is neuter (DPD: nt) | `nt.acc.sg` | 8 |
| per-19-anupubba-sikkha.md:713 | `cakkhundriyaṃ \| noun \| masc.acc.sg` | cakkhundriya is neuter (DPD: nt) | `nt.acc.sg` | 8 |
| per-19-anupubba-sikkha.md:714 | `cakkhundriye \| noun \| masc.loc.sg` | cakkhundriya is neuter (DPD: nt) | `nt.loc.sg` | 8 |
| per-19-anupubba-sikkha.md:758 | `mano-indriyaṃ \| noun \| masc.acc.sg` | manindriya is neuter (DPD: nt) | `nt.acc.sg` | 8 |
| per-19-anupubba-sikkha.md:679 | `rūpaṃ \| noun \| masc.acc.sg` | rūpa is neuter (DPD rūpa 3: nt) | `nt.acc.sg` | 8 |
| per-19-anupubba-sikkha.md:695 | `asaṃvutaṃ \| pp \| masc.acc.sg` | qualifies cakkhundriyaṃ (nt in DPD), not enaṃ | `nt.acc.sg` | 7 |
| per-19-anupubba-sikkha.md:724 | `sotena \| noun \| masc.ins.sg` | sota "ear" is neuter (DPD sota 2.1: nt) | `nt.ins.sg` | 8 |
| per-19-anupubba-sikkha.md:727 | `ghānena \| noun \| masc.ins.sg` | ghāna is neuter (DPD: nt) | `nt.ins.sg` | 8 |
| per-19-anupubba-sikkha.md:734 | `phoṭṭhabbaṃ \| noun \| masc.acc.sg` | phoṭṭhabba is neuter (DPD phoṭṭhabba 1: nt) | `nt.acc.sg` | 8 |
| per-19-anupubba-sikkha.md:843 | `cittaṃ \| noun \| masc.acc.sg` | citta is neuter (DPD citta 1.1: nt); line 1010 has `nt.acc.sg` | `nt.acc.sg` | 9 |
| per-19-anupubba-sikkha.md:859 | `cittaṃ \| noun \| masc.acc.sg` | citta is neuter (DPD citta 1.1: nt) | `nt.acc.sg` | 9 |
| per-19-anupubba-sikkha.md:897 | `cittaṃ \| noun \| masc.acc.sg` | citta is neuter (DPD citta 1.1: nt) | `nt.acc.sg` | 9 |
| per-19-anupubba-sikkha.md:872 | `passena \| noun \| masc.ins.sg` | passa (side of the body) is neuter (DPD passa 1.1: nt) | `nt.ins.sg` | 8 |
| per-19-anupubba-sikkha.md:871 | `dakkhiṇena \| adj \| masc.ins.sg` | agrees with passena (nt, DPD passa 1.1) | `nt.ins.sg` | 8 |
| per-19-anupubba-sikkha.md:898 | `parisodhehi, \| verb` | chant line 885 has `parisodhehī'ti`; row copied from the earlier tables (844, 860) | `parisodhehī'ti` | 6 |
| per-19-anupubba-sikkha.md:879 | `sampajāno \| pp \| masc.nom.sg` | sampajāna is an adjective (DPD sampajāna 1: adj); line 1035 has `adj` | POS `adj` | 8 |
| per-19-anupubba-sikkha.md:911 | `satisampajaññena \| noun \| masc.ins.sg` | satisampajañña is neuter (DPD: nt) | `nt.ins.sg` | 8 |
| per-19-anupubba-sikkha.md:964 | `vivittaṃ \| adj \| masc.acc.sg` | agrees with senāsanaṃ (nt.acc.sg, line 965) | `nt.acc.sg` | 8 |
| per-19-anupubba-sikkha.md:975 | `palālapuñjan'ti \| noun \| nt.acc.sg` | palālapuñja is masculine (DPD: masc) | `masc.acc.sg` | 8 |
| per-19-anupubba-sikkha.md:1171 | `abhininnāmeti \| verb \| aor.3.sg` | -eti form is present, not aorist (DPD abhininnāmeti: pr) | `pr.3.sg` | 9 |
| per-19-anupubba-sikkha.md:1175 | `ayaṃ dukkha- samudayo'ti` | stray hyphen and space split the compound in the chant line (DPD dukkhasamudaya; table line 1184 has `dukkhasamudayo'ti`) | `ayaṃ dukkhasamudayo'ti` | 8 |
| per-19-anupubba-sikkha.md:1188 | `dukkhanirodhagāminī \| noun \| fem.nom.sg` | gāminī is an adjective (DPD gāminī: adj, fem nom sg of gāmī) | POS `adj` | 8 |
| per-19-anupubba-sikkha.md:1201 | `āsavanirodha-gāminī \| adj \| masc.nom.sg` | -inī is feminine, agrees with paṭipadā (DPD gāminī: fem nom sg) | `fem.nom.sg` | 8 |
| per-19-anupubba-sikkha.md:1230 | `vimuttasmiṃ \| pp \| masc.loc.sg` | qualifies citta (nt) understood from the preceding sentence (cittaṃ vimuccati, line 1205) | `nt.loc.sg` | 6 |
| per-20-requisites-for-awakening.md:32 | `yathayidaṃ \| pron \| nt.nom.sg` | `yatha'y-idaṃ` is a sandhi of `yathā + [y] + idaṃ` (DPD yathayidaṃ = sandhi, adv + pron), not a single pronoun; a nominative tag does not fit | POS `sandhi`, Grammar ∅ | 8 |
| per-20-requisites-for-awakening.md:42 | `lokānukampāya \| noun \| fem.instr.sg` | Known row 20-02 only renames `instr` → `ins`; the case itself is doubtful: in the `bahujanahitāya … lokānukampāya atthāya` series this is a dative of purpose ("out of compassion for the world", as the translation on line 48 says), not instrumental. DPD lokānukampā fem (case not given) | `fem.dat.sg` | 5 |
| per-20-requisites-for-awakening.md:62 | `sammappadhānā \| noun \| nt.nom.pl` | The preceding `cattāro` (line 61) is masc.nom.pl (DPD cattāro card, masc nom & acc pl); DPD lists sammappadhāna both as nt (1) and masc (2), and the masc entry fits the agreement | `masc.nom.pl` | 7 |
| per-21-the-seven-factors-of-awakening.md:19 | `niyyānikā \| adj \| fem.nom.sg` | Agrees with `bojjhaṅgā` (masc.nom.pl), like `ariyā` on line 17; no feminine noun in the sentence (DPD niyyānika adj) | `masc.nom.pl` | 8 |
| per-21-the-seven-factors-of-awakening.md:77 | `taṃ \| pron \| masc.acc.sg \| that` | In `taṃ kissa hetu` (DPD idiom) `taṃ` is the neuter subject ("what is the reason for that?"), DPD taṃ 1.1 pron, nt nom sg; nothing masculine or accusative here | `nt.nom.sg` | 8 |
| per-21-the-seven-factors-of-awakening.md:194 | `samāhitaṃ \| adj \| masc.nom.sg` | Qualifies `cittaṃ` (neuter), the object of `ajjhupekkhitā` ("looks on at the mind thus composed"); a form in `-aṃ` cannot be masc.nom.sg | `nt.acc.sg` | 7 |
| per-21-the-seven-factors-of-awakening.md:195 | `cittaṃ \| noun \| nt.nom.sg \| mind, heart` | Subject is `so`; `cittaṃ` is the object of the agent noun `ajjhupekkhitā hoti` (DPD ajjhupekkhitar masc, agent) | `nt.acc.sg` | 6 |
| per-22-the-noble-eightfold-path.md:24 | `sammāsati \| noun \| masc.nom.sg` | sammāsati is feminine (DPD sammāsati 1 fem; sati 1.2 fem); line 18 `sammādiṭṭhi` correctly has fem | `fem.nom.sg` | 9 |
| per-22-the-noble-eightfold-path.md:105 | `kāmesumicchācārā \| noun \| nt.abl.sg` | kāmesumicchācāra is masculine (DPD kāmesumicchācāra masc; cf. `pāṇātipātā` masc.abl.sg in the same list) | `masc.abl.sg` | 9 |
| per-22-the-noble-eightfold-path.md:142 | `anuppādāya \| noun \| nt.dat.sg` | anuppāda is masculine (DPD anuppāda masc); line 174 has `uppādāya \| noun \| masc.dat.sg` | `masc.dat.sg` | 9 |
| per-22-the-noble-eightfold-path.md:207 | `idha- \| ind` | `idha, bhikkhave, bhikkhu` (line 203) is not a compound or sandhi; the trailing hyphen marks a compound member wrongly (other `idha` rows, e.g. 117, 270, have none; DPD idha ind, adv) | `idha` | 7 |
| per-22-the-noble-eightfold-path.md:211 | `anupassī \| noun \| masc.nom.sg` | Second member of kāyānupassī, which DPD gives as adj (kāyānupassī adj, comp); bare `anupassī` not looked up separately | POS `adj` | 7 |
| per-22-the-noble-eightfold-path.md:228 | `vedanānupassī \| noun \| masc.nom.sg` | DPD vedanānupassī adj, comp | POS `adj` | 8 |
| per-22-the-noble-eightfold-path.md:237 | `cittānupassī \| noun \| masc.nom.sg` | DPD cittānupassī adj, comp | POS `adj` | 8 |
| per-22-the-noble-eightfold-path.md:246 | `dhammānupassī \| noun \| masc.nom.sg` | DPD dhammānupassī adj, comp | POS `adj` | 8 |
| per-22-the-noble-eightfold-path.md:227 | `vedanāsu \| noun \| masc.loc.pl` | vedanā is feminine (DPD vedanā 1 fem) | `fem.loc.pl` | 9 |
| per-22-the-noble-eightfold-path.md:303 | `ajjhattaṃ \| adj \| nt.nom.sg` | DPD ajjhattaṃ is ind, adv (acc sg of ajjhatta used adverbially, "internally"), not an adjective in the nominative; the commentary reading as a qualifier of `sampasādanaṃ` would still need acc., not nom. | POS `ind`, Grammar ∅ | 7 |
| per-22-the-noble-eightfold-path.md:304 | `sampasādanaṃ \| adj \| nt.nom.sg` | Agrees with or stands in apposition to `dutiyaṃ jhānaṃ` (nt.acc.sg, object of `upasampajja`), as lines 307–311 are tagged; nominative is wrong. (DPD has sampasādana only as nt noun; POS left as is here) | `nt.acc.sg` | 6 |
| per-22-the-noble-eightfold-path.md:306 | `ekodibhāvaṃ \| adj \| masc.acc.sg` | DPD ekodibhāva is a masc noun (abstr, comp), so masc.acc.sg is right but POS `adj` is not | POS `noun` (Grammar `masc.acc.sg` unchanged) | 6 |
| per-22-the-noble-eightfold-path.md:362 | `adukkhamasukhaṃ \| adj \| masc.acc.sg` | Qualifies `catutthaṃ jhānaṃ` (nt.acc.sg); DPD adukkhamasukha 1 adj | `nt.acc.sg` | 8 |
| per-23-mindfulness-of-breathing.md:38 | `\| cattāro \| adj \| masc.acc.pl \| four (4) \|` | In chant line 34 `cattāro satipaṭṭhānā` is the subject (row 39 tags `satipaṭṭhānā` masc.nom.pl); DPD `cattāro` = masc nom & acc pl, and here it is nom, not acc as copied from the line-28 table (POS `card` is policy BP8, not this row) | `masc.nom.pl` | 9 |
| per-23-mindfulness-of-breathing.md:40 | `\| bhāvitā \| pp \| fem.nom.pl \|` | Agrees with masc `satipaṭṭhānā` (row 39), not with fem `ānāpānassati` as in the earlier tables | `masc.nom.pl` | 8 |
| per-23-mindfulness-of-breathing.md:41 | `\| bahulīkatā \| adj \| fem.nom.pl \|` | Agrees with masc `satipaṭṭhānā` (row 39); gender copied from the fem tables above | `masc.nom.pl` | 8 |
| per-23-mindfulness-of-breathing.md:69 | `\| idha- \| ind \|` | `idha` (DPD idha 1, ind, adv) is a free word here (chant line 65 `idha, bhikkhave`), not a compound member; trailing hyphen is wrong | `\| idha \| ind \|` | 8 |
| per-23-mindfulness-of-breathing.md:229 | `\| citta- \| noun \| masc \| mind \|` | `citta` (mind) is neuter in DPD (citta 1.1 nt); `masc` is wrong whichever compound-member policy is chosen. Known 23-28 (B-11.3) blanks the same cell; this row is the gender error, which stands if A5.7 is kept | `nt` (or ∅ if B11.3 is chosen) | 9 |
| per-23-mindfulness-of-breathing.md:14 | `\| bahulīkatā \| adj \| fem.nom.sg \|` | POS `adj`, but DPD `bahulīkata` is pp (pp of bahulīkaroti), parallel to `bhāvitā \| pp` in the row above | `pp` | 8 |
| per-23-mindfulness-of-breathing.md:27 | `\| bahulīkatā \| adj \| fem.nom.sg \|` | Same as line 14: DPD `bahulīkata` is pp | `pp` | 8 |
| per-23-mindfulness-of-breathing.md:41 | `\| bahulīkatā \| adj \|` | Same as line 14: DPD `bahulīkata` is pp (POS cell; the gender row for this line is separate) | `pp` | 8 |
| per-23-mindfulness-of-breathing.md:299 | `\| bahulīkatā \| adj \| fem.nom.sg \|` | Same as line 14: DPD `bahulīkata` is pp | `pp` | 8 |
| per-24-dependent-origination.md:255 | `rūpaṃ \| noun \| nt.acc.sg` | in `cattāro mahābhūtā, … upādāya rūpaṃ` rūpaṃ is the subject listed beside `mahābhūtā` (nom.), not acc.; DPD gives gender only (rūpa nt), case is a syntax judgment | `nt.nom.sg` | 7 |
| per-24-dependent-origination.md:491 | `āyatanānaṃ \| noun \| masc.gen.pl` | āyatana is neuter (DPD āyatana 1–5 nt) | `nt.gen.pl` | 9 |
| per-24-dependent-origination.md:521 | `āyuno \| noun \| masc.gen.sg` | āyu is neuter (DPD āyu 1–4 nt) | `nt.gen.sg` | 9 |
| per-24-dependent-origination.md:523 | `indriyānaṃ \| noun \| masc.gen.pl` | indriya is neuter (DPD indriya 1–3 nt) | `nt.gen.pl` | 9 |
| per-24-dependent-origination.md:570 | `byasanena \| noun \| masc.ins.sg` | byasana is neuter (DPD byasana nt) | `nt.ins.sg` | 9 |
| per-24-dependent-origination.md:574 | `byasanena \| noun \| masc.ins.sg` | byasana is neuter (DPD byasana nt) | `nt.ins.sg` | 9 |
| per-24-dependent-origination.md:576 | `byasanena \| noun \| masc.ins.sg` | byasana is neuter (DPD byasana nt) | `nt.ins.sg` | 9 |
| per-24-dependent-origination.md:578 | `byasanena \| noun \| masc.ins.sg` | byasana is neuter (DPD byasana nt) | `nt.ins.sg` | 9 |
| per-24-dependent-origination.md:580, 582 | `byasanena \| noun \| masc.ins.sg` | byasana is neuter (DPD byasana nt; same defect, remaining lines) | `nt.ins.sg` | 9 |
| per-24-dependent-origination.md:592 | `cetaso \| noun \| masc.gen.sg` | ceto is neuter (mano-group); DPD lookup returned no headword for `ceto`, so unconfirmed | `nt.gen.sg` | 7 |
| per-24-dependent-origination.md:593 | `parijjhāyanā, \| noun \| masc.nom.sg` | parijjhāyanā is feminine (DPD parijjhāyanā fem) | `fem.nom.sg` | 9 |
| per-24-dependent-origination.md:638 | `yaṃ \| noun \| nt.nom.sg` | yaṃ is the relative pronoun, not a noun (DPD yaṃ 1 pron, nt nom sg of ya) | `yaṃ \| pron \| nt.nom.sg` | 9 |
| per-24-dependent-origination.md:666 | `yaṃ \| noun \| nt.nom.sg` | yaṃ is the relative pronoun, not a noun (DPD yaṃ 1 pron, nt nom sg of ya) | `yaṃ \| pron \| nt.nom.sg` | 9 |
| per-25-the-dhamma-in-brief.md:20 | `ekaṃantaṃ` | Pāḷi cell misspelt; chant line 8 and row 22 have `ekamantaṃ` (DPD ekamantaṃ) | `ekamantaṃ` | 9 |
| per-25-the-dhamma-in-brief.md:155 | `subharatāya \| noun \| masc.dat.sg` | Abstract noun in -tā is feminine (DPD subharatā fem; cf. appicchatāya, line 111, fem) | Grammar `fem.dat.sg` | 9 |
| per-25-the-dhamma-in-brief.md:158 | `dubbharatāya \| noun \| masc.dat.sg` | Abstract noun in -tā is feminine (DPD dubbharatā fem) | Grammar `fem.dat.sg` | 9 |
| per-25-the-dhamma-in-brief.md:168 | `gotami \| noun \| masc.voc.sg` | Gotamī is feminine (DPD gotamī fem); known 25-04 is line 66 only | Grammar `fem.voc.sg` | 9 |
| per-25-the-dhamma-in-brief.md:170 | `eso \| noun \| masc.nom.sg` | Demonstrative pronoun tagged as noun (DPD eso pron) | POS `pron` | 9 |
| per-25-the-dhamma-in-brief.md:172 | `eso \| noun \| masc.nom.sg` | Demonstrative pronoun tagged as noun (DPD eso pron) | POS `pron` | 9 |
| per-25-the-dhamma-in-brief.md:174 | `etaṃ \| noun \| nt.nom.sg` | Pronoun tagged as noun (DPD etaṃ pron) | POS `pron` | 9 |
| per-26-the-four-great-references.md:37 | `ayaṃ \| noun \| masc.nom.sg` | Pronoun tagged as noun (DPD ayaṃ pron) | POS `pron` | 9 |
| per-26-the-four-great-references.md:39 | `ayaṃ \| noun \| masc.nom.sg` | Pronoun tagged as noun (DPD ayaṃ pron) | POS `pron` | 9 |
| per-26-the-four-great-references.md:41 | `idaṃ \| noun \| nt.nom.sg` | Pronoun tagged as noun (DPD idaṃ pron) | POS `pron` | 9 |
| per-26-the-four-great-references.md:32 | `āvuso \| noun \| masc.voc.pl` | āvuso is an indeclinable (DPD āvuso ind, "voc sg & pl"), not a declined noun form | POS `ind`, Grammar ∅ | 8 |
| per-26-the-four-great-references.md:128 | `sandassetabbāni \| prp` | -tabba form is a ptp, not prp (DPD sandassetabba ptp; cf. otāretabbāni, line 126) | POS `ptp` | 9 |
| per-27-principles-of-cordiality.md:17 | `arāme` | Chant `ghositārāme` = ghosita + ārāme; DPD ārāma | `ārāme` | 9 |
| per-27-principles-of-cordiality.md:56 | `mettaṃ \| adj \| nt.acc.sg` | Subject of `paccupaṭṭhitaṃ hoti`, so nominative | Grammar `nt.nom.sg` | 7 |
| per-27-principles-of-cordiality.md:57 | `kāyakammaṃ \| noun \| nt.acc.sg` | Subject of `paccupaṭṭhitaṃ hoti`, so nominative | Grammar `nt.nom.sg` | 7 |
| per-27-principles-of-cordiality.md:58 | `vacīkammaṃ \| noun \| nt.acc.sg` | Subject of `paccupaṭṭhitaṃ hoti`, so nominative | Grammar `nt.nom.sg` | 7 |
| per-27-principles-of-cordiality.md:59 | `manokammaṃ \| noun \| nt.acc.sg` | Subject of `paccupaṭṭhitaṃ hoti`, so nominative | Grammar `nt.nom.sg` | 7 |
| per-27-principles-of-cordiality.md:60 | `paccupaṭṭhitaṃ \| pp \| nt.acc.sg` | Predicate with `hoti`, so nominative | Grammar `nt.nom.sg` | 7 |
| per-27-principles-of-cordiality.md:75 | `ye \| pron \| masc.acc.pl` | Agrees with nominative `lābhā` (line 77); DPD ye 1 masc nom pl | Grammar `masc.nom.pl` | 7 |
| per-27-principles-of-cordiality.md:76 | `te \| pron \| masc.acc.pl` | Agrees with nominative `lābhā` (line 77); DPD te 1.1 masc nom pl | Grammar `masc.nom.pl` | 7 |
| per-27-principles-of-cordiality.md:90 | `bhogī \| adj \| \| enjoying` | Final compound member left without case tag; it is the predicate nominative with `hoti` | Grammar `masc.nom.sg` | 6 |
| per-27-principles-of-cordiality.md:92 | `bhogī \| adj \| \| enjoying` | Final compound member left without case tag | Grammar `masc.nom.sg` | 6 |
| per-27-principles-of-cordiality.md:101 | `yāni \| pron \| nt.acc.pl` | Relative clause subject (parallel to nom `ye te lābhā`, line 70) is nominative | Grammar `nt.nom.pl` | 6 |
| per-27-principles-of-cordiality.md:102 | `tāni \| pron \| nt.acc.pl` | Nominative, as line 101 | Grammar `nt.nom.pl` | 6 |
| per-27-principles-of-cordiality.md:103 | `sīlāni \| noun \| nt.acc.pl` | Nominative, as line 101 | Grammar `nt.nom.pl` | 6 |
| per-27-principles-of-cordiality.md:104 | `akhaṇḍāni \| adj \| nt.acc.pl` | Nominative, as line 101 | Grammar `nt.nom.pl` | 6 |
| per-27-principles-of-cordiality.md:105 | `acchiddāni \| adj \| nt.acc.pl` | Nominative, as line 101 | Grammar `nt.nom.pl` | 6 |
| per-27-principles-of-cordiality.md:106, 107, 108, 109, 110, 112 | `nt.acc.pl` | Same defect on the remaining adjectives of the clause | Grammar `nt.nom.pl` | 6 |
| per-27-principles-of-cordiality.md:155 | `ime \| pron \| masc.nom.pl` | Object of `samādāya`, agreeing with `dhamme` masc.acc.pl (line 159); DPD ime nom & acc pl | Grammar `masc.acc.pl` | 7 |
| per-27-principles-of-cordiality.md:193 | `sāraṇīyesāra` | Corrupted word in chant line; line 151 has `sāraṇīye` | `sāraṇīye` | 9 |
| per-27-principles-of-cordiality.md:193 | `tasmā't'iha` | Misplaced apostrophe; DPD tasmātiha = tasmā + [t] + iha | `tasmāt'iha` | 8 |
| per-27-principles-of-cordiality.md:197 | `tasmā't'iha \| ind` | Misplaced apostrophe, as line 193 (DPD tasmātiha) | `tasmāt'iha` | 8 |
| per-27-principles-of-cordiality.md:198 | `vattatha \| verb \| imp.2.sg` | -tha ending is 2nd plural (addressed to monks; line 161 opt.2.pl); DPD silent on the form | Grammar `imp.2.pl` | 7 |
| per-28-principles-of-non-decline.md:13 | `\| bhikkhave \| noun \| masc.voc.sg \|` | bhikkhave is vocative plural (DPD: masc voc pl of bhikkhu); file elsewhere has `masc.voc.pl` (l. 228) | `masc.voc.pl` | 9 |
| per-28-principles-of-non-decline.md:25 | `\| bhikkhave \| noun \| masc.voc.sg \|` | voc sg for plural vocative (DPD masc voc pl) | `masc.voc.pl` | 9 |
| per-28-principles-of-non-decline.md:52 | `\| bhikkhave \| noun \| masc.voc.sg \|` | voc sg for plural vocative (DPD masc voc pl) | `masc.voc.pl` | 9 |
| per-28-principles-of-non-decline.md:74 | `\| bhikkhave \| noun \| masc.voc.sg \|` | voc sg for plural vocative (DPD masc voc pl) | `masc.voc.pl` | 9 |
| per-28-principles-of-non-decline.md:99 | `\| bhikkhave \| noun \| masc.voc.sg \|` | voc sg for plural vocative (DPD masc voc pl) | `masc.voc.pl` | 9 |
| per-28-principles-of-non-decline.md:130, 150, 168, 198 | `\| bhikkhave \| noun \| masc.voc.sg \|` | same: voc sg for plural vocative (4 more lines; DPD masc voc pl) | `masc.voc.pl` | 9 |
| per-28-principles-of-non-decline.md:29 | `\| bhavissanti \| verb \| pr.3.pl \| will be \|` | bhavissanti is future, gloss says "will be"; l. 155 has `fut.3.pl` (DPD lookup hit only an unrelated sandhi headword) | `fut.3.pl` | 7 |
| per-28-principles-of-non-decline.md:76 | `\| apaññattaṃ \| pp \| masc.acc.sg \|` | used substantively ("what has not been laid down"): neuter | `nt.acc.sg` | 6 |
| per-28-principles-of-non-decline.md:79 | `\| paññattaṃ \| pp \| masc.acc.sg \|` | used substantively ("what has been laid down"): neuter | `nt.acc.sg` | 6 |
| per-28-principles-of-non-decline.md:83 | `\| paññattesu \| pp \| masc.loc.pl \|` | agrees with `sikkhāpadesu` (nt.loc.pl, l. 84) | `nt.loc.pl` | 7 |
| per-28-principles-of-non-decline.md:116 | `\| sotabbaṃ \| ptp \| masc.acc.sg \|` | impersonal ptp (`tesañca sotabbaṃ maññissanti`): neuter | `nt.acc.sg` | 6 |
| per-28-principles-of-non-decline.md:132 | `\| uppannāya \| adj \| fem.gen.sg \|` | uppanna is pp (DPD uppanna 1, pp of uppajjati); per-31:113 tags `uppannānaṃ` as pp | POS `pp` | 8 |
| per-28-principles-of-non-decline.md:184 | `\| phāsuṃ \| noun \| masc.acc.sg \| ease, comfort \|` | `phāsuṃ vihareyyuṃ`: adverb (DPD phāsuṃ ind, adv "easily; comfortably"), not a masc noun | `\| phāsuṃ \| ind \| \| comfortably, at ease \|` | 8 |
| per-28-principles-of-non-decline.md:309 | `\| indriyesu \| noun \| masc.loc.pl \|` | indriya is neuter (DPD indriya nt) | `nt.loc.pl` | 9 |
| per-29-striving-according-to-the-dhamma.md:41 | `\| saddhā- \| adj \| \| faithful; with confidence \|` | in `saddhā-pabbajita` the member is the fem noun saddhā "faith" (DPD saddhāpabbajita: tatiyā tappurisa saddhāya + pabbajita) | `\| saddhā- \| noun \| \| faith, confidence \|` | 8 |
| per-29-striving-according-to-the-dhamma.md:79 | `\| yaṃ \| pron \| masc.acc.sg \| whatever \|` | `yaṃ taṃ … pattabbaṃ`: subject of a passive ptp, neuter | `nt.nom.sg` | 6 |
| per-29-striving-according-to-the-dhamma.md:80 | `\| taṃ \| pron \| masc.acc.sg \| that \|` | correlative of `yaṃ … pattabbaṃ`, neuter nom | `nt.nom.sg` | 6 |
| per-29-striving-according-to-the-dhamma.md:87 | `\| pattabbaṃ \| ptp \| masc.acc.sg \|` | predicate ptp agreeing with neuter `yaṃ taṃ` | `nt.nom.sg` | 6 |
| per-29-striving-according-to-the-dhamma.md:89 | `\| taṃ \| pron \| masc.acc.sg \| that \|` | object of `apāpuṇitvā`, refers to the neuter `yaṃ` | `nt.acc.sg` | 6 |
| per-29-striving-according-to-the-dhamma.md:101 | `\| dukkhaṃ \| noun \| nt.acc.sg \|` | `dukkhaṃ viharati`: adverb (DPD dukkhaṃ ind, adv "badly; with difficulty; uncomfortably"); cf. `sukhaṃ` ind l. 138 | `\| dukkhaṃ \| ind \| \| badly, with difficulty, uncomfortably \|` | 8 |
| per-29-striving-according-to-the-dhamma.md:246 | `\| sacchikiriyāya \| noun \| masc.dat.sg \|` | sacchikiriyā is feminine (DPD fem) | `fem.dat.sg` | 9 |
| per-29-striving-according-to-the-dhamma.md:256 | `\| ayaṃ \| pron \| masc.nom.sg \|` | agrees with `pabbajjā` (fem); DPD ayaṃ masc & fem nom sg | `fem.nom.sg` | 8 |
| per-29-striving-according-to-the-dhamma.md:257 | `\| amhākaṃ \| pron \| 1.gen.sg \| our \|` | amhākaṃ is plural (DPD amhākaṃ 3, 1st gen pl "our") | `1.gen.pl` | 9 |
| per-31-the-four-requisites.md:5 | `Cattaro parikkhāra` | Pāḷi title: masc nom pl (DPD cattāro card masc nom pl; parikkhāra masc) | `Cattāro parikkhārā` | 8 |
| per-31-the-four-requisites.md:25 | `\| samphassānaṃ \| noun \| masc.dat.pl \| for contacts \|` | governed by `paṭighātāya` like `sītassa` (gen): genitive | `\| samphassānaṃ \| noun \| masc.gen.pl \| of contacts \|` | 7 |
| per-31-the-four-requisites.md:90 | `\| samphassānaṃ \| noun \| masc.dat.pl \| for touches; contacts \|` | genitive governed by `paṭighātāya` | `\| samphassānaṃ \| noun \| masc.gen.pl \| of touches; contacts \|` | 7 |
| per-31-the-four-requisites.md:29 | `\| paṭicchādaṃ- \|` | chant has `paṭicchādan'atthaṃ`: member is paṭicchādana (DPD paṭicchādana nt); known 31-05 covers only l. 30 `attha` | `paṭicchādana-` | 9 |
| per-31-the-four-requisites.md:117 | `\| abyāpajjha- \| adj \| \| freedom from oppressive pain, relief \|` | gloss is DPD abyāpajjha 1.1 (nt, "freedom from oppressive pain; relief from suffering"), so the member is a noun, not adj | `\| abyāpajjha- \| noun \| \| freedom from oppressive pain, relief \|` | 8 |
| per-32-the-repulsiveness-of-food.md:12 | `āhāre \| noun \| masc.acc.pl \| food, sustenances, nutriments` | In `āhāre paṭikūlasaññāparicitena` (perception of repulsiveness in food) āhāre is loc.sg, not acc.pl (DPD āhāra 1 masc; case from context) | Grammar `masc.loc.sg`; English `in food` | 7 |
| per-33-universal-well-being.md:96 | `tassa \| pron \| masc.gen.sg \| of that` | Refers back to `kammaṃ` (nt); DPD tassa 2 is masc & nt gen sg | Grammar `nt.gen.sg` | 7 |
| per-35-five-subjects-for-frequent-recollection.md:27 | `byādhiṃ \| noun \| nt.acc.sg` | DPD byādhi is masc | Grammar `masc.acc.sg` | 9 |
| per-35-five-subjects-for-frequent-recollection.md:80 | `tassa \| pron \| masc.gen.sg \| of that` | Refers back to `kammaṃ` (nt); DPD tassa 2 is masc & nt gen sg | Grammar `nt.gen.sg` | 7 |
| per-36-ten-subjects-for-frequent-recollection-by-one-who-has-gone-forth.md:64 | `sīlato \| noun \| masc.abl.sg` | DPD sīla 1 is nt | Grammar `nt.abl.sg` | 9 |
| per-36-ten-subjects-for-frequent-recollection-by-one-who-has-gone-forth.md:80 | `sīlato \| noun \| masc.abl.sg` | DPD sīla 1 is nt | Grammar `nt.abl.sg` | 9 |
| per-36-ten-subjects-for-frequent-recollection-by-one-who-has-gone-forth.md:114 | `āgāre \| noun \| masc.loc.sg` | āgāra is nt (saved DPD output has no āgāra entry) | Grammar `nt.loc.sg` (DPD lookup: āgāra) | 7 |
| per-37-the-thirty-two-parts.md:39 | `dantā \| noun \| nt.nom.pl` | DPD danta 1.1 (tooth) is masc | Grammar `masc.nom.pl` | 9 |
| per-38-recollection-of-impermanence.md:72 | `jīvitaṃ \| noun \| nt.acc.sg` | Subject of the nominal sentence `maraṇa-pariyosānaṃ me jīvitaṃ` (cf. line 80 `nt.nom.sg`) | Grammar `nt.nom.sg` | 8 |
| per-39-dhammacakkappavattana-sutta.md:21 | `isipatane \| noun \| masc.loc.sg` | DPD isipatana is nt; known 39-02 covers only the empty English cell | Grammar `nt.loc.sg` | 9 |
| per-39-dhammacakkappavattana-sutta.md:61 | `imasmiñ'ca \| pron \| \| while this` | Grammar empty; imasmiṃ agrees with `veyyākaraṇasmiṃ` (DPD imasmiṃ 2: masc & nt loc sg, loc abs; veyyākaraṇa 2 nt) | Grammar `nt.loc.sg` | 8 |
| per-39-dhammacakkappavattana-sutta.md:109 | `saddamanussavesum` | Misspelt (missing `ā`, `m` for `ṃ`); every parallel line has `saddam’anussāvesuṃ` (DPD anussāveti); known 39-10 covers only the bold | `saddam’anussāvesuṃ` | 9 |
| per-40-anatta-lakkhana-sutta.md:19 | `\| jeta-vane \| noun \| masc.loc.sg \|` | DPD `jetavana` is nt; known 40-04 fixes only the gloss | `\| jeta-vane \| noun \| nt.loc.sg \|` | 9 |
| per-40-anatta-lakkhana-sutta.md:83 | `\| no labbhati \|` | Pāḷi line 74 reads `na ca labbhati`; `no` is not in the text, and the positive gloss `is obtained…` (DPD `labbhati`) then lacks the negation (DPD `na 1` "not"); known 40-20 fixes only POS/Grammar | split into two rows: `\| na \| ind \| \| not \|` and `\| labbhati \| v.pass \| pr.3.sg \| is obtained, is acquired, is received, is possible, is proper \|` (POS/Grammar of the second row per known 40-20) | 8 |
| per-40-anatta-lakkhana-sutta.md:147 | `\| taṃ \| pron \| masc.acc.sg \|` | In `taṃ kiṃ maññatha` (DPD idiom) `taṃ` refers to the matter, nt (DPD `taṃ 1.1` nt; acc `taṃ 1.2` is gender-ambiguous) | `\| taṃ \| pron \| nt.acc.sg \|` | 7 |
| per-40-anatta-lakkhana-sutta.md:148 | `\| kiṃ \| pron \| masc.acc.sg \|` | `kiṃ` is the nt form (DPD `kiṃ 1` nt nom and acc sg of ka; masc acc is `kaṃ`) | `\| kiṃ \| pron \| nt.acc.sg \|` | 9 |
| per-40-anatta-lakkhana-sutta.md:285 | `masc.v.sg` | `bhikkhave` is voc pl (DPD masc, voc pl of bhikkhu); known 40-34 only expands `v` and keeps `sg`, this row corrects the number in the same cell | `masc.voc.pl` | 9 |
| per-41-aditta-pariyaya-sutta.md:37 | `\| bhikkhave \| noun \| masc.voc.sg \|` | `bhikkhave` is voc pl (DPD masc, voc pl of bhikkhu) | `\| bhikkhave \| noun \| masc.voc.pl \|` | 9 |
| per-40-anatta-lakkhana-sutta.md:353 | `\| rūpasmim'pi \| noun \| masc.loc.sg \|` | DPD `rūpa` is nt (cf. lines 49, 61); known 40-44 fixes only the gloss | `\| rūpasmim'pi \| noun \| nt.loc.sg \|` | 9 |
| per-40-anatta-lakkhana-sutta.md:361 | `\| virāgā \| noun \| abl.sg \|` | Gender missing; DPD `virāga` masc | `\| virāgā \| noun \| masc.abl.sg \|` | 9 |
| per-41-aditta-pariyaya-sutta.md:219 | `\| virāgā \| noun \| abl.sg \|` | Gender missing; DPD `virāga` masc | `\| virāgā \| noun \| masc.abl.sg \|` | 9 |
| per-40-anatta-lakkhana-sutta.md:408 | `\| imasmiñ'ca \| pron \| \|` | Grammar empty; DPD `imasmiṃ 2` masc & nt loc sg, loc abs; agrees with nt `veyyākaraṇasmiṃ` | `\| imasmiñ'ca \| pron \| nt.loc.sg \|` | 8 |
| per-41-aditta-pariyaya-sutta.md:266 | `\| imasmiñ'ca \| pron \| \|` | Grammar empty; DPD `imasmiṃ 2` masc & nt loc sg, loc abs; agrees with nt `veyyākaraṇasmiṃ` | `\| imasmiñ'ca \| pron \| nt.loc.sg \|` | 8 |
| per-40-anatta-lakkhana-sutta.md:416 | `\| cittāni \| noun \| nt.acc.pl \|` | Subject of `vimucciṃsu`, so nominative (DPD `citta` nt) | `\| cittāni \| noun \| nt.nom.pl \|` | 8 |
| per-41-aditta-pariyaya-sutta.md:274 | `\| cittāni \| noun \| nt.acc.pl \|` | Subject of `vimucciṃsu`, so nominative (DPD `citta` nt) | `\| cittāni \| noun \| nt.nom.pl \|` | 8 |
| per-41-aditta-pariyaya-sutta.md:20 | `\| gayāsīse \| noun \| masc.loc.sg \|` | DPD `gayāsīsa` nt | `\| gayāsīse \| noun \| nt.loc.sg \|` | 9 |
| per-41-aditta-pariyaya-sutta.md:22 | `\| bhikkhusahassena \| noun \| masc.ins.sg \|` | DPD `bhikkhusahassa` nt | `\| bhikkhusahassena \| noun \| nt.ins.sg \|` | 9 |
| per-41-aditta-pariyaya-sutta.md:271 | `\| bhikkhusahassassa \| noun \| masc.gen.sg \|` | DPD `bhikkhusahassa` nt | `\| bhikkhusahassassa \| noun \| nt.gen.sg \|` | 9 |
| per-41-aditta-pariyaya-sutta.md:72 | `\| kena \| pron \| masc.ins.sg \|` | Interrogative "by what?" refers to a thing: nt (DPD `kena` instr sg of ka, gender not given) | `\| kena \| pron \| nt.ins.sg \|` | 7 |
| per-41-aditta-pariyaya-sutta.md:73 | `\| rāg'agginā \| noun \| nt.ins.sg \|` | DPD `aggi` masc (known 41-11 fixes only line 74) | `\| rāg'agginā \| noun \| masc.ins.sg \|` | 9 |
| per-41-aditta-pariyaya-sutta.md:75 | `\| moh'agginā \| noun \| nt.ins.sg \|` | DPD `aggi` masc (known 41-11 fixes only line 74) | `\| moh'agginā \| noun \| masc.ins.sg \|` | 9 |
| per-41-aditta-pariyaya-sutta.md:188 | `\| tasmim'pi \| pron \| masc.loc.sg \|` | Refers back to `vedayitaṃ` (DPD `vedayita` nt; `tasmiṃ` masc & nt loc sg) | `\| tasmim'pi \| pron \| nt.loc.sg \|` | 8 |
| per-43-ratanattayanubhavadi-gatha.md:5 | `dukkha-roga-bhayā-verā` | The compound `dukkha-roga-bhayā` ends at `bhayā`; `verā` (DPD vera nt) is a separate word with its own case (table line 22), and the same chant in per-45:82 writes `bhayā verā`. Chant-line change: owner approves | `dukkha-roga-bhayā verā` | 6 |
| per-43-ratanattayanubhavadi-gatha.md:41 | `\| lābhaṃ \| noun \| nt.nom.sg \|` | DPD lābha 1 is masc only; the `-aṃ` nominative is a verse gender shift, so `nt` misstates the lemma's gender | `\| lābhaṃ \| noun \| masc.nom.sg \|` | 6 |
| per-45-culla-mangala-cakka-vala.md:109 | `\| lābhaṃ \| noun \| nt.nom.sg \|` | Same as per-43:41 (DPD lābha 1 masc) | `\| lābhaṃ \| noun \| masc.nom.sg \|` | 6 |
| per-44-bhojana-dananumodana.md:55-56 | `\| yattha- \| ind \| \| wherever, where \|` | Chant `yattha yatth'ūpapajjatī'ti` contains the DPD idiom `yattha yattha` (idiom, adv + adv, "wherever; wheresoever"); the split into `yattha` + `yattha-` hyphenates the second word as if compounded. Known 44-02/44-03 only fill the Grammar cells of these rows | Replace lines 55–56 with `\| yattha yattha \| idiom \| \| wherever, wheresoever \|` | 8 |
| per-45-culla-mangala-cakka-vala.md:18 | `saṅgha-ratanaṃtiṇṇaṃ` | Missing space between two words (table lines 27–28 list them separately) | `saṅgha-ratanaṃ tiṇṇaṃ` | 9 |
| per-45-culla-mangala-cakka-vala.md:28 | `\| tiṇṇaṃ \| adj \| masc.gen.pl \|` | DPD tiṇṇaṃ is masc & nt gen pl; it agrees with `ratanānaṃ` (nt.gen.pl, line 29), so the gender is nt (POS `card` is policy BP8, not decided here) | `\| tiṇṇaṃ \| adj \| nt.gen.pl \|` | 8 |
| per-45-culla-mangala-cakka-vala.md:34 | `piṭakattay'ānubhavena` | Misspelling: the word in the series is `ānubhāvena` (DPD ānubhāva 2 "power"), as in the two neighbouring compounds; DPD anubhava means "experience". Chant-line change: owner approves | `piṭakattay'ānubhāvena` | 8 |
| per-45-culla-mangala-cakka-vala.md:43 | `\| anubhavena \| noun \| masc.ins.sg \|` | Same misspelling in the table; the gloss is that of DPD ānubhāva | `\| ānubhāvena \| noun \| masc.ins.sg \|` | 8 |
| per-46-aggappasada-sutta-gatha.md:33 | `\| sukhe \| noun \| masc.loc.sg \| in ease, comfort, pleasant, good \|` | The noun `sukha` is nt (DPD sukha 2), so masc.loc is impossible for it; here `sukhe` is the adj (DPD sukha 1) agreeing with `dhamme`; gloss mixes noun and adj | `\| sukhe \| adj \| masc.loc.sg \| in pleasant, happy, good \|` | 8 |
| per-47-kala-dana-sutta-gatha.md:12 | `\| sapaññā \|` | Misspelt; chant line 6 has `sappaññā` (DPD sappañña adj) | `\| sappaññā \|` | 9 |
| per-49-deva-aradhanai.md:16 | `\| parittaṃ \| noun \| fem.acc.sg \|` | `paritta` (protection, protective chant) is nt; the saved DPD lines give only paritta 1 (pp, "little") | `\| parittaṃ \| noun \| nt.acc.sg \|` (DPD lookup: paritta "protection") | 7 |
| per-49-deva-aradhanai.md:42 | `\| vatthumhi \| noun \| masc.loc.sg \|` | DPD: `vatthu` nt (land; property; ground) | `\| vatthumhi \| noun \| nt.loc.sg \|` | 8 |
| per-49-deva-aradhanai.md:62 | `\| yaṃ \| pron \| masc.acc.sg \|` | `yaṃ` agrees with `vacanaṃ` (nt.acc.sg, line 65); DPD yaṃ 2 is masc, fem & nt acc sg | `\| yaṃ \| pron \| nt.acc.sg \|` | 8 |
| per-49-deva-aradhanai.md:80 | `\| bhadantā \| noun \| masc.voc.sg \| o venerables!, reverends! \|` | `bhadantā` and the gloss are plural; the tag says sg | `\| bhadantā \| noun \| masc.voc.pl \| o venerables!, reverends! \|` | 8 |
| per-51-nama-kara-siddhi-gatha.md:51 | `\| vināsamentu \| verb \| imp.3.pl \| may they be destroyed \|` | Not one verb form: sandhi `vināsaṃ` (DPD vināsa masc) + `entu` (DPD eti 2 "goes (to)"), "may they go to destruction" | Split: `\| vināsaṃ \| noun \| masc.acc.sg \| destruction \|` + `\| entu \| verb \| imp.3.pl \| may they go \|` | 7 |
| per-51-nama-kara-siddhi-gatha.md:103 | `\| jetā \| adj \| fem.nom.sg \|` | `jetā` is nom sg of the agent noun `jetu` (masc; no DPD headword), referring to `yo` (masc.nom.sg, line 99) | `\| jetā \| adj \| masc.nom.sg \|` | 7 |
| per-53-mangala-sutta.md:18 | `\| jeta-vane \| noun \| masc.loc.sg \|` | jetavana is neuter (DPD: jetavana nt) | `\| jeta-vane \| noun \| nt.loc.sg \|` | 8 |
| per-53-mangala-sutta.md:36 | `\| jetavanaṃ \| noun \| masc.acc.sg \|` | jetavana is neuter (DPD: jetavana nt) | `\| jetavanaṃ \| noun \| nt.acc.sg \|` | 8 |
| per-53-mangala-sutta.md:35 | `\| kevalakappaṃ \| adj \| masc.acc.sg \|` | adjective agrees with neuter `jetavanaṃ` (DPD: kevalakappa adj) | `\| kevalakappaṃ \| adj \| nt.acc.sg \|` | 7 |
| per-53-mangala-sutta.md:19 | `of Anāthapindika` | name misspelt in gloss (DPD: anāthapiṇḍika; Pāḷi column has `anāthapiṇḍikassa`) | `of Anāthapiṇḍika` | 8 |
| per-53-mangala-sutta.md:22 | `in Anāthapindika's park` | name misspelt in translation (DPD: anāthapiṇḍika) | `in Anāthapiṇḍika's park` | 8 |
| per-53-mangala-sutta.md:52 | `\| ekaṃantaṃ \| ind \|` | invalid form: niggahita inside one word; passage line 45 has `ekam-antaṃ` (DPD: ekamantaṃ ind). Pāḷi cell only; the known B-P1 item at :52 touches Grammar | `\| ekamantaṃ \| ind \|` | 8 |
| per-53-mangala-sutta.md:54 | `\| ekaṃantaṃ \| ind \|` | same invalid form as :52; passage has `ekam-antaṃ` (DPD: ekamantaṃ ind). Pāḷi cell only; the known B-P1 item at :54 touches Grammar | `\| ekamantaṃ \| ind \|` | 8 |
| per-53-mangala-sutta.md:141 | `\| su'bhāsitā \| pp \|` | stray apostrophe (no elision); chant line 130 has `subhāsitā` (DPD: subhāsita) | `\| subhāsitā \| pp \|` | 8 |
| per-53-mangala-sutta.md:255 | `\| ariyasaccānaṃ- \| noun \| masc.gen.pl \|` | ariyasacca is neuter (DPD: ariyasacca nt; per-54:237, 251 tag `ariyasaccāni` nt) | `\| ariyasaccānaṃ- \| noun \| nt.gen.pl \|` | 8 |
| per-53-mangala-sutta.md:299 | `\| gacchanti, \| noun \| pr.3.pl \|` | POS `noun` on a finite verb (DPD: gacchati pr) | `\| gacchanti, \| verb \| pr.3.pl \|` | 9 |
| per-54-ratana-sutta.md:14 | `\| \>yāni- \| pron \| nt.acc.pl \|` | subject of the relative clause (`yāni … bhūtāni samāgatāni`), so nominative (DPD yāni: nt nom & acc pl; case from context) | `\| \>yāni- \| pron \| nt.nom.pl \|` | 7 |
| per-54-ratana-sutta.md:16 | `\| bhūtāni \| noun \| nt.acc.pl \|` | subject, nominative | `\| bhūtāni \| noun \| nt.nom.pl \|` | 7 |
| per-54-ratana-sutta.md:17 | `\| samāgatāni \| pp \| nt.acc.pl \|` | predicate of the subject `bhūtāni`, nominative | `\| samāgatāni \| pp \| nt.nom.pl \|` | 7 |
| per-54-ratana-sutta.md:18 | `\| bhummāni \| adj \| nt.acc.pl \|` | agrees with nominative `bhūtāni` | `\| bhummāni \| adj \| nt.nom.pl \|` | 7 |
| per-54-ratana-sutta.md:20 | `\| yāni \| pron \| nt.acc.pl \|` | subject (`yāni va antalikkhe`), nominative (DPD yāni: nt nom & acc pl) | `\| yāni \| pron \| nt.nom.pl \|` | 7 |
| per-54-ratana-sutta.md:28 | `\| sabbā \| adj \| masc.nom.pl \|` | chant `sabb'eva` = sabbe + eva; masc nom pl of sabba is `sabbe` (DPD: sabbe pron masc nom pl), as at :50 | `\| sabbe \| pron \| masc.nom.pl \|` | 8 |
| per-54-ratana-sutta.md:66 | `\| ye \| pron \| masc.acc.pl \|` | `ye` is the subject of `haranti` (DPD: ye 1 masc & nt nom pl) | `\| ye \| pron \| masc.nom.pl \|` | 8 |
| per-54-ratana-sutta.md:104 | `\| idam'pi \| pron \| masc.nom.sg \|` | idaṃ is neuter (DPD: idaṃ nt nom sg) | `\| idam'pi \| pron \| nt.nom.sg \|` | 8 |
| per-54-ratana-sutta.md:125 | `\| yad- \| pron \| masc.acc.sg \|` | `yad` is the neuter form (refers to the whole `khayaṃ … amataṃ`); DPD silent on `yad` | `\| yad- \| pron \| nt.acc.sg \|` | 7 |
| per-54-ratana-sutta.md:132 | `\| sama- \| adj \| \|` | chant `sam-atthi` = samaṃ + atthi, an inflected word, not a compound member. DPD gives this as samaṃ 4 ind, adv `equal (to)`; note :93 tags the same word `adj \| nt.nom.sg` | `\| samaṃ- \| ind \| adv \|` | 6 |
| per-54-ratana-sutta.md:204 | `\| sāsanamhi \| noun \| masc.loc.sg \|` | sāsana is neuter (DPD: sāsana nt) | `\| sāsanamhi \| noun \| nt.loc.sg \|` | 8 |
| per-54-ratana-sutta.md:265 | `\| adiyanti \| verb \|` | long vowel lost; chant line 246 has `ādiyanti` (DPD: ādiyati) | `\| ādiyanti \| verb \|` | 9 |
| per-54-ratana-sutta.md:281 | `\| tayo- \| adj \| \|` | `tayo` (from `taya'ssu`) is an inflected numeral joined by sandhi, not a compound member; Grammar empty (DPD: tayo 1 card, masc nom pl). POS left as is: numeral POS is owner policy BP8 | `\| tayo- \| adj \| masc.nom.pl \|` | 8 |
| per-54-ratana-sutta.md:286 | `\| sakkāyadiṭṭhi \| noun \| masc.nom.sg \|` | diṭṭhi is feminine (DPD: sakkāyadiṭṭhi fem) | `\| sakkāyadiṭṭhi \| noun \| fem.nom.sg \|` | 9 |
| per-54-ratana-sutta.md:332 | `\| tassa \| pron \| masc.dat.sg \| to this \|` | refers to `kammaṃ` (nt), object of `paṭicchadāya` (DPD tassa: masc & nt dat or gen sg; case from context) | `\| tassa \| pron \| nt.gen.sg \| of it \|` | 5 |
| per-54-ratana-sutta.md:363 | `\| hitāya \| adj \| masc.dat.sg \| for benefit \|` | `hita` here is the neuter noun `benefit`, as the gloss shows (DPD: hita 3 nt, welfare; benefit) | `\| hitāya \| noun \| nt.dat.sg \| for benefit \|` | 8 |
| per-54-ratana-sutta.md:399 | `\| khīṇa'bījā \| adj \|` | stray apostrophe (no elision); chant line 384 has `khīṇa-bījā` (DPD: khīṇabīja adj) | `\| khīṇabījā \| adj \|` | 8 |
| per-54-ratana-sutta.md:405 | `\| ayaṃ- \| pron \| masc.acc.sg \|` | `ayaṃ` is nominative (DPD: masc & fem nom sg), agreeing with `padīpo` | `\| ayaṃ- \| pron \| masc.nom.sg \|` | 9 |
| per-55-karaniya-metta-sutta.md:81 | `\| khuddaṃ \| adj \| masc.acc.sg \|` | `khuddaṃ` qualifies neuter `kiñci` ("anything slight"), so it is neuter | `nt.acc.sg` | 7 |
| per-55-karaniya-metta-sutta.md:83 | `\| kiñci \| pron \| masc.acc.sg \|` | "something, anything" is neuter here (object of samācare; DPD kiñci 3 is masc & nt acc sg); per-56:96 tags the same use nt | `nt.acc.sg` | 7 |
| per-55-karaniya-metta-sutta.md:91 | `\| pare \| pron \| masc.acc.pl \| others \|` | In `yena viññū pare upavadeyyuṃ`, `viññū pare` ("other wise people") is the subject of upavadeyyuṃ, so nominative | `masc.nom.pl` | 6 |
| per-55-karaniya-metta-sutta.md:110 | `\| sukhita-attā \| adj \| nt.nom.pl \|` | Bahubbīhi adjective (DPD sukhitatta adj, kammadhāraya > bahubbīhi) that agrees with `sattā` (masc.nom.pl, line 108) | `masc.nom.pl` | 8 |
| per-55-karaniya-metta-sutta.md:222 | `\| byārosanā \| noun \| fem.nom.sg \|` | In the verse `byārosanā paṭighasaññā` gives the means ("through anger…", as line 226 translates), i.e. instrumental (byārosanāya); DPD byārosanā fem gives the gender only | `fem.ins.sg` | 6 |
| per-55-karaniya-metta-sutta.md:224 | `\| saññā, \| noun \| fem.nom.sg \|` | Same instrumental use as `byārosanā` (line 222; translation line 226 "(through)"); DPD saññā fem gives the gender only | `fem.ins.sg` | 6 |
| per-55-karaniya-metta-sutta.md:300 | `\| asambādhaṃ, \| adj \| nt.nom.sg \|` | Qualifies `mānasaṃ` (object of bhāvaye, line 273), so accusative | `nt.acc.sg` | 6 |
| per-55-karaniya-metta-sutta.md:301 | `\| averaṃ \| adj \| nt.nom.sg \|` | Qualifies `mānasaṃ` (object of bhāvaye), so accusative | `nt.acc.sg` | 6 |
| per-55-karaniya-metta-sutta.md:302 | `\| asapattaṃ \| adj \| nt.nom.sg \|` | Qualifies `mānasaṃ` (object of bhāvaye), so accusative | `nt.acc.sg` | 6 |
| per-55-karaniya-metta-sutta.md:320 | `\| assa \| pron \| masc.dat.sg \|` | In `yāvat-assa vigata-middho` `assa` is the optative of atthi (DPD assa 3.1 "opt of atthi … would be"; line 323 "as long as he is"), not the pronoun (DPD assa 4.1). Known 55-28 only fixes the `hiṃ` typo in the English cell, which this row replaces | `\| assa \| verb \| opt.3.sg \| he would be \|` | 7 |
| per-56-khandha-parittam.md:98 | `\| agamā \| v.refl \| aor.3.sg \|` | Chant line 80 has `pāpam-āgamā`; the gloss "came (to), arrived (at)" is DPD āgamā 1 (ā + √gam); the Pāli cell drops the prefix `ā`. Known 56-03 (A5.9) touches only POS/Grammar | `\| āgamā \|` (Pāli cell) | 7 |
| per-56-khandha-parittam.md:98 | `\| agamā \| v.refl \| aor.3.sg \|` | DPD tags both `agamā` and `āgamā 1` as imperf (3rd person); DPD's only aorist reading (āgamā 2) is reflexive 2nd sg, which does not fit the 3rd-sg subject `kiñci pāpaṃ`. Conflicts with known 56-03 (A5.9 → `aor.3.sg.refl`) on the same Grammar cell | `imperf.3.sg` (POS `verb` as in known 56-03; drop `.refl`) | 7 |
| per-56-khandha-parittam.md:137 | `\| rakkhā \| noun \| fem.nom.pl \|` | Translation line 152 reads singular "Protection"; `katā me rakkhā` = "protection has been made by me" | `fem.nom.sg` | 5 |
| per-58-yan-kinci-ratanam-loke.md:10 | `\| yaṃ- \| pron \| masc.acc.sg \|` | `yaṃ kiñci ratanaṃ` is the subject of `vijjati` (DPD vijjati pass "exists; is found"), neuter nominative | `nt.nom.sg` | 8 |
| per-58-yan-kinci-ratanam-loke.md:11 | `\| kiñci \| pron \| masc.acc.sg \|` | Part of the subject `yaṃ kiñci ratanaṃ` of `vijjati`; DPD kiñci 2 = nt nom sg | `nt.nom.sg` | 8 |
| per-58-yan-kinci-ratanam-loke.md:12 | `\| ratanaṃ \| noun \| nt.acc.sg \|` | Subject of passive `vijjati` (DPD "exists; is found"; pr.3.sg, line 14), so nominative | `nt.nom.sg` | 8 |
| per-58-yan-kinci-ratanam-loke.md:15 | `\| vividhaṃ \| adj \| masc.acc.sg \|` | Qualifies `ratanaṃ` (nt, subject of vijjati) | `nt.nom.sg` | 7 |
| per-58-yan-kinci-ratanam-loke.md:65 | `\| upasamanaṃ \| adj \| masc.acc.sg \|` | Qualifies or stands in apposition to `osadhaṃ` (nt.acc.sg, line 43); DPD upasamana is nt (noun) or adj, neuter either way | `nt.acc.sg` | 8 |
| per-58-yan-kinci-ratanam-loke.md:74 | `\| āhuneyyaṃ \| adj \| masc.acc.sg \|` | In apposition to `saṅgha-ratanaṃ` / `osadhaṃ` (nt.acc.sg) | `nt.acc.sg` | 5 |
| per-58-yan-kinci-ratanam-loke.md:75 | `\| pāhuneyyaṃ \| adj \| masc.acc.sg \|` | In apposition to `saṅgha-ratanaṃ` / `osadhaṃ` (nt.acc.sg) | `nt.acc.sg` | 5 |
| per-59-bojjhanga-parittam.md:18 | `\| passaddhi \| noun \| masc.nom.sg \|` | `passaddhi` is feminine (DPD passaddhi fem) | `fem.nom.sg` | 8 |
| per-59-bojjhanga-parittam.md:56 | `\| vajjena \| adj \| masc.ins.sg \|` | DPD saccavajja is nt ("speaking honestly; telling the truth"), so the head `vajjena` is neuter; DPD vajja 1.1 is ptp of vadati ("speaking; saying") | `\| vajjena \| ptp \| nt.ins.sg \|` | 7 |
| per-59-bojjhanga-parittam.md:73 | `\| gilāne \| adj \| masc.loc.sg \| in sick, ill \|` | Object complement of `disvā` with Moggallāna and Kassapa ("having seen them sick", translation line 87): accusative plural | `\| gilāne \| adj \| masc.acc.pl \| sick, ill \|` | 6 |
| per-59-bojjhanga-parittam.md:74 | `\| dukkhite \| adj \| masc.loc.sg \| in when afflicted, miserable, suffering \|` | Same construction as `gilāne` (line 73): accusative plural after `disvā` | `\| dukkhite \| adj \| masc.acc.pl \| afflicted, miserable, suffering \|` | 6 |
| per-59-bojjhanga-parittam.md:102 | `\| cunda-ttherena \|` | Hyphen splits the doubled consonant; the member is `thera` (chant `cundattherena`); DPD has no headword `cundatthera` | `\| cunda-therena \|` | 7 |
| per-61-devata-uyyojana-gatha.md:37 | `devā- \| noun \| masc.nom.pl` | `devā` is a free word (subject of anumodantu, chant line 26 `sabbe devā anumodantu`), not a compound member; the hyphen is wrong | `devā \| noun \| masc.nom.pl` | 8 |
| per-61-devata-uyyojana-gatha.md:39 | `sabba \| adj \| masc.nom.pl` | First member of the compound `sabba-sampatti-siddhiyā` (chant line 26); a case tag is wrong under every option | `sabba- \| adj \| ` (Grammar empty) | 8 |
| per-61-devata-uyyojana-gatha.md:40 | `sampatti \| noun \| fem.nom.sg` | Middle member of `sabba-sampatti-siddhiyā`; a case tag is wrong under every option | `sampatti- \| noun \| ` (Grammar empty) | 8 |
| per-61-devata-uyyojana-gatha.md:59 | `devatā- \| noun \| \| deity, god` | `gacchantu devatā-gatā` is devatā + āgatā (DPD āgata 3 pp "come; arrived"), "may the deities who have come go"; devatā (DPD fem) is a free word, the subject of gacchantu | `devatā \| noun \| fem.nom.pl \| deities` | 7 |
| per-61-devata-uyyojana-gatha.md:60 | `gatā \| pp \| masc.nom.pl` | Wrong split: the word is āgatā "come, arrived" (DPD āgata 3), agreeing with devatā (fem) | `āgatā \| pp \| fem.nom.pl \| come, arrived` | 7 |
| per-61-devata-uyyojana-gatha.md:56 | `abhiratā \| pp \| masc.nom.pl` | Subject of this stanza is devatā (fem, line 45 `gacchantu devatā-gatā`), so masc does not agree | `abhiratā \| pp \| fem.nom.pl` | 5 |
| per-61-devata-uyyojana-gatha.md:72 | `yaṃ \| pron \| masc.acc.sg` | yaṃ (DPD yaṃ 2: masc, fem & nt acc sg) agrees with neuter `balaṃ` (DPD bala nt; line 73, where the known item 61-07 fixes balaṃ to `nt.acc.sg`); this row is line 72, the yaṃ tag; masc is wrong | `yaṃ \| pron \| nt.acc.sg` | 8 |
| per-62-jaya-mangala-attha-gatha.md:39 | `māra- \| noun \| masc.acc.sg` | Compound member (`mār'ātirekam'`) with a full case tag; wrong under every option | `māra- \| noun \| ` (Grammar empty) | 7 |
| per-62-jaya-mangala-attha-gatha.md:44 | `ghoram' \| adj \| \|` | Free inflected word with no Grammar; agrees with āḷavakaṃ (line 46) | `ghoram' \| adj \| masc.acc.sg` | 7 |
| per-62-jaya-mangala-attha-gatha.md:45 | `pana'` | Chant has `ghoram'pan'āḷavakam'`; the elided form is `pan'`, `pana'` is neither the full nor the elided form | `pan'` | 7 |
| per-62-jaya-mangala-attha-gatha.md:74 | `sudāruṇan' \| adj \| \|` | Free inflected word with no Grammar; agrees with nāḷāgiriṃ / taṃ | `sudāruṇan' \| adj \| masc.acc.sg` | 6 |
| per-62-jaya-mangala-attha-gatha.md:76 | `metta' \| noun` | Chant has `mett'ambu-seka`; the lemma is mettā (DPD fem); `metta'` is neither lemma nor chant form | `mettā- \| noun` | 8 |
| per-62-jaya-mangala-attha-gatha.md:96 | `sudāruṇan' \| adj \| \|` | Free inflected word with no Grammar; agrees with taṃ (Aṅgulimāla) | `sudāruṇan' \| adj \| masc.acc.sg` | 6 |
| per-62-jaya-mangala-attha-gatha.md:151 | `ketuṃ \| noun \| \|` | Free inflected word (end of `mati-saccaka-vāda-ketuṃ`) with no Grammar; DPD ketu masc. The known item 62-12 (D3) on this line concerns the `<br>` in the English cell; this is the Grammar cell | `ketuṃ \| noun \| masc.acc.sg` | 8 |
| per-62-jaya-mangala-attha-gatha.md:175 | `vibudhaṃ \| noun \| \| with distorted wisdom` | Adjective agreeing with bhujagaṃ (DPD vibudha 1 adj "with distorted wisdom"); POS and Grammar wrong | `vibudhaṃ \| adj \| masc.acc.sg \| with distorted wisdom` | 8 |
| per-62-jaya-mangala-attha-gatha.md:176 | `mah'iddhiṃ \| adj \| \|` | Free inflected word with no Grammar; agrees with bhujagaṃ (DPD has mahiddhi only as masc name of a god, so the adj reading is unconfirmed) | `mah'iddhiṃ \| adj \| masc.acc.sg` | 6 |
| per-62-jaya-mangala-attha-gatha.md:181 | `apayanto \| prp \| masc.nom.sg \| going away; is retreating.` | `dam'āpayanto` is damāpayanto, a causative prp of the dameti family (DPD dameti "makes tame"; translation line 188: "to tame him"), not dama- + apayanto "going away"; rows 180–181 split it wrongly. DPD has no headword damāpeti | Replace rows 180–181 with `dam'āpayanto \| prp \| caus.masc.nom.sg \| causing to tame, having tamed` (DPD lookup: damāpeti for tag and gloss) | 6 |
| per-62-jaya-mangala-attha-gatha.md:210 | `gadena \| noun \| masc.ins.sg \| by speech, sentence` | `ñāṇā-gadena` is ñāṇa + agada (DPD agada "medicine; drug; antidote", nt and masc), "with the antidote of knowledge" (the image follows the snake-bite of line 200); rows 209–210 split it wrongly | Row 209 `ñāṇa-`; row 210 `agadena \| noun \| masc.ins.sg \| by medicine, antidote` | 8 |
| per-62-jaya-mangala-attha-gatha.md:225 | `etā \| pron \| fem.nom.pl` | `etā … gāthā` is the object of sarate (yo … sarate), so acc | `etā \| pron \| fem.acc.pl` | 6 |
| per-62-jaya-mangala-attha-gatha.md:231 | `gāthā \| noun \| fem.nom.pl` | Object of sarate, so acc | `gāthā \| noun \| fem.acc.pl` | 6 |
| per-62-jaya-mangala-attha-gatha.md:235 | `dine \| noun \| masc.acc.pl \| days` | `dina-dine` "day after day" is loc.sg, not acc.pl; DPD dina is nt | `dine \| noun \| nt.loc.sg \| on (each) day` | 8 |
| per-62-jaya-mangala-attha-gatha.md:237 | `atandī \| adj \| \|` | Free inflected word with no Grammar (DPD atandī adj); agrees with yo / naro | `atandī \| adj \| masc.nom.sg` | 7 |
| per-63-jaya-parittam.md:35 | `maṅgaṃ \| noun \| nt.nom.sg` | Typo: chant line 25 has `jaya-maṅgalaṃ` (DPD maṅgala nt) | `maṅgalaṃ \| noun \| nt.nom.sg` | 9 |
| per-63-jaya-parittam.md:55 | `maṅgale \| noun \| nt.acc.pl` | `-e` is not a neuter acc.pl ending (DPD maṅgala nt); `jayassu jaya-maṅgale` is loc.sg | `maṅgale \| noun \| nt.loc.sg \| in what is auspicious, in the blessing` | 8 |
| per-63-jaya-parittam.md:65 | `sīse \| noun \| \|` | Free inflected word with no Grammar; loc.sg ("on the top"); DPD sīsa nt | `sīse \| noun \| nt.loc.sg` | 8 |
| per-63-jaya-parittam.md:67 | `pokkhare \| noun \| \|` | Free inflected word with no Grammar; loc.sg; DPD pokkhara 1 nt (water lily) | `pokkhare \| noun \| nt.loc.sg` | 8 |
| per-63-jaya-parittam.md:68 | `abhiseke \| noun \| \|` | Free inflected word with no Grammar; loc.sg; DPD abhiseka masc | `abhiseke \| noun \| masc.loc.sg` | 8 |
| per-63-jaya-parittam.md:89 | `suyiṭṭhaṃ \| adj \| \|` | Free inflected word with no Grammar (DPD suyiṭṭha adj) | `suyiṭṭhaṃ \| adj \| nt.nom.sg` | 7 |
| per-63-jaya-parittam.md:105 | `te \| pron \| masc.nom.pl \| they` | In `paṇīdhi te padakkhiṇe` te is "your" (your aspirations; DPD te 2.4 "your; of you"), not "they" | `te \| pron \| 2.gen.sg \| your` | 8 |
| per-63-jaya-parittam.md:109 | `labhanta- \| prp \| \| getting; obtaining; attaining.` | Chant `labhant'atthe` is labhanti atthe, a finite verb (DPD labhati pr "gets; obtains"; translation line 113: "they get"); not a prp compound member | `labhant' \| verb \| pr.3.pl \| they get, obtain` | 8 |
| per-64-bhavatu-sabba-mangalam.md:19 | `rakkhantu \| verb \| imp.3.sg` | `-antu` is 3.pl (subject devatā pl; gloss "may they") | `rakkhantu \| verb \| imp.3.pl` | 9 |
| per-64-bhavatu-sabba-mangalam.md:28 | `te \| pron \| 1.dat.sg` | te "for you" is 2nd person (DPD te 2.3 "for you; to you", 2nd dat sg) | `te \| pron \| 2.dat.sg` | 9 |
| per-65-dhamma-sangani-matika.md:84 | `dassanena \| noun \| masc.ins.sg` | dassana is neuter (DPD dassana nt) | `dassanena \| noun \| nt.ins.sg` | 9 |
| per-65-dhamma-sangani-matika.md:197 | `bahiddhā \| adj \| masc.nom.pl` | bahiddhā is an indeclinable (DPD bahiddhā 1 ind, adv "externally; outwardly"); a case tag is wrong | `bahiddhā \| ind \| ` | 7 |
| per-66-vipassana-bhumi-patho.md:53 | `\| aṭṭhārasa \| adj \| masc.nom.pl \|` | Qualifies `dhātuyo` (fem.nom.pl, L54); DPD aṭṭhārasa 1: card, x pl (same form in every gender), so the tag must follow the noun, not masc; POS adj/card is left to policy BP8 | `\| aṭṭhārasa \| adj \| fem.nom.pl \|` | 6 |
| per-66-vipassana-bhumi-patho.md:98 | `\| dukkhanirodhagāminī \| noun \| fem.nom.sg \|` | `gāminī` is an adjective qualifying `paṭipadā` (DPD gāminī: adj, fem nom sg of gāmī) | `\| dukkhanirodhagāminī \| adj \| fem.nom.sg \|` | 8 |
| per-66-vipassana-bhumi-patho.md:141 | `\| dukkhadomanass- \|` | Truncated stem; chant `dukkhadomanass'upāyāsā` = dukkhadomanassa + upāyāsā (DPD domanassa 1: nt, stem in -a) | `\| dukkhadomanassa- \|` | 8 |
| per-68-adasi-me-adi-gatha.md:15 | `\| sakhā \| noun \| masc.nom.pl \|` | Translation L25 reads singular "my companion"; `sakhā` is the nom sg (DPD has sakhi masc only, no sakhā headword: number not confirmed by DPD) | `\| sakhā \| noun \| masc.nom.sg \|` | 6 |
| per-68-adasi-me-adi-gatha.md:22 | `\| katam- \| pp \| masc.acc.sg \|` | `pubbe katam anussaraṃ` "remembering what was done": substantivised pp is neuter (DPD kata 2: nt, "something done") | `\| katam- \| pp \| nt.acc.sg \|` | 8 |
| per-68-adasi-me-adi-gatha.md:44 | `\| taṃ \| pron \| masc.acc.sg \|` | `na taṃ petānam atthāya` "that is not for the good": subject referring to weeping/grief, so neuter nominative (DPD taṃ 1.1: pron, nt nom sg of ta), not masc acc | `\| taṃ \| pron \| nt.nom.sg \|` | 7 |
| per-68-adasi-me-adi-gatha.md:59 | `\| dakkhinā \|` | Misspelt; chant L53 has `dakkhiṇā` (DPD dakkhiṇā 1, retroflex ṇ, as in L19) | `\| dakkhiṇā \|` | 9 |
| per-68-adasi-me-adi-gatha.md:62 | `\| supatiṭṭhitā \|` | Table form differs from the chant L53 `suppatiṭṭhitā` (DPD suppatiṭṭhita) | `\| suppatiṭṭhitā \|` | 9 |
| per-68-adasi-me-adi-gatha.md:64 | `\| hitāya- \| noun \| masc.dat.sg \|` | `hita` "welfare, benefit" is a neuter noun (DPD hita 3: nt) | `\| hitāya- \| noun \| nt.dat.sg \|` | 8 |
| per-68-adasi-me-adi-gatha.md:87 | `\| anuppadinnaṃ \| pp \| nt.acc.sg \|` | Predicate of `balañ'ca` (nt.nom.sg, L85) in a passive clause; must agree in case (DPD anuppadinna pp; case from syntax only) | `\| anuppadinnaṃ \| pp \| nt.nom.sg \|` | 7 |
| per-69-pamsu-kula.md:41 | `\| sukho \| noun \| masc.nom.sg \|` | `sukho` agrees with `vūpasamo` (masc); the noun sukha is neuter (DPD sukha 2), so this is the adjective (DPD sukha 1 adj; gloss follows the adjective) | `\| sukho \| adj \| masc.nom.sg \| pleasant, happy, comfortable \|` | 8 |
| per-69-pamsu-kula.md:60 | `\| tatha'eva- \|` | Neither the sandhi form nor the parts: chant `tath'ev'āhaṃ` = tathā + eva (DPD tatheva 1: sandhi, tathā + eva). Known row 69-04 changes only the POS of this row | `\| tath'eva- \|` | 7 |
| per-70-sharing-and-aspirations.md:53 | `\| brahmā- \| noun \| masc.nom.pl \|` | Chant `brahma-mārā` is a compound; member written with long ā and given a full case tag (DPD brahma 1: masc, stem brahma) | `\| brahma- \| noun \| \|` | 6 |
| per-70-sharing-and-aspirations.md:103 | `\| amataṃ \| noun \| nt.nom.sg \|` | Goal/object of `pāpetha` ("lead you to the deathless", L105): accusative, not nominative (DPD amata 1.1 nt; case from syntax only) | `\| amataṃ \| noun \| nt.acc.sg \|` | 7 |
| per-70-sharing-and-aspirations.md:143 | `\| mamaṃ \| noun \| 1.dat.sg \|` | Personal pronoun tagged as noun (DPD mamaṃ 2: pron, 1st dat sg of ahaṃ); same word is `pron` at L214 | `\| mamaṃ \| pron \| 1.dat.sg \|` | 9 |
| per-70-sharing-and-aspirations.md:157 | `\| bhave \| verb \| imp.reflx.1.sg \|` | Mood wrong: DPD bhave: opt of bhavati, not imp. Known row 70-20's re-check fixes the whole cell (mood, and the reflx too: DPD gives no reflx, so the A5.3/B11.2 choice no longer applies; 1.sg is kept from the source and the translation "may I be") | mood `imp` → `opt`: `\| bhave \| verb \| opt.1.sg \|` (matches the re-check of 70-20) | 8 |
| per-70-sharing-and-aspirations.md:224 | `\| ānubhāvena \|` | Long ā comes from sandhi with `uttama` (chant `tes'ottam'ānubhāvena`); DPD headword is anubhāva (its construction notes anu > ānu, so ānubhāva is an attested variant: stem-convention choice) | `\| anubhāvena \|` | 6 |
| per-71-sharing-of-all-merits.md:14 | `\| puññassa- \| noun \| masc.gen.sg \|` | puñña is neuter (DPD puñña 1: nt) | `\| puññassa- \| noun \| nt.gen.sg \|` | 8 |
| per-71-sharing-of-all-merits.md:16 | `\| katassa \| pp \| masc.gen.sg \|` | Agrees with `puññassa` (DPD puñña 1: nt) | `\| katassa \| pp \| nt.gen.sg \|` | 8 |
| per-71-sharing-of-all-merits.md:21 | `\| tesañ'ca \| pron \| masc.gen.pl \|` | Refers back to the merits (`puññassa`, `yāni … katāni`, neuter); DPD tesaṃ 2 allows masc & nt gen pl, gender from context only | `\| tesañ'ca \| pron \| nt.gen.pl \|` | 6 |
| per-71-sharing-of-all-merits.md:58 | `\| te \| adj \| masc.nom.pl \| three \|` | Glossed "three" (translation L69 "three planes"), so it is the compound form te- (ti > te) of `tebhummā`, a member without case (DPD: no tebhumma headword) | `\| te- \| adj \| \| three \|` | 6 |
| per-71-sharing-of-all-merits.md:75 | `\| ñātaṃ \| pp \| masc.acc.sg \|` | Qualifies `pattidānaṃ` (nt.acc.sg, L78); gender from context only (DPD ñāta 1 pp) | `\| ñātaṃ \| pp \| nt.acc.sg \|` | 7 |
| per-71-sharing-of-all-merits.md:84 | `\| c'imaṃ \| pron \| masc.acc.sg \|` | Refers to the `pattidānaṃ` (neuter); DPD imaṃ allows masc, fem & nt acc sg, gender from context only | `\| c'imaṃ \| pron \| nt.acc.sg \|` | 6 |
| per-71-sharing-of-all-merits.md:101 | `\| hetunā \| adj \| masc.ins.sg \|` | hetu with case tag and gloss "by reason, cause" is the masculine noun (DPD hetu 2: masc); DPD hetu 1 adj exists only "in comps" | `\| hetunā \| noun \| masc.ins.sg \|` | 7 |
| per-71-sharing-of-all-merits.md:110 | `\| padañ'ca \| noun \| masc.acc.sg \|` | pada is neuter (DPD pada 05: nt, "place; position; state") | `\| padañ'ca \| noun \| nt.acc.sg \|` | 8 |
| per-71-sharing-of-all-merits.md:114 | `\| subhā \| adj \| nt.nom.pl \|` | Qualifies `āsā` (DPD āsā: fem); with `sijjhataṃ` (3 sg, known row 71-10, which touches L113 only) it is fem nom sg | `\| subhā \| adj \| fem.nom.sg \|` | 7 |
| per-72-sharing-of-merits-with-the-departed.md:16 | `\| idaṃ \| noun \| nt.nom.sg \|` | Pronoun tagged as noun (DPD idaṃ 1: pron, nt nom sg of ima) | `\| idaṃ \| pron \| nt.nom.sg \|` | 9 |
| per-74-the-highest-honour-and-aspirations.md:54 | `sataṃ \| adj \| masc.acc.sg` | In `sataṃ samāgamo` (association of the good), sataṃ is gen pl of santa (DPD sataṃ 2: masc, gen pl of santa, "of virtuous people"), not acc sg of an adjective | `sataṃ \| noun \| masc.gen.pl` | 8 |
| per-74-the-highest-honour-and-aspirations.md:97 | `apaciyati = apacayati,` | Chant line 87 reads apacayati (DPD apacayati, pr, "honours; pays respect to"); `apaciyati` is a wrong form, and the cell carries a trailing comma | `apacayati` | 8 |
| per-74-the-highest-honour-and-aspirations.md:140 | `āsavakkhayā- \| noun` | Wrong split: the compound is āsavakkhaya + āvaha (DPD āsavakkhaya masc comp; āvaha adj, in comps, "bringing"); the first member has short -a. Pāḷi cell only; known item 74-06 touches the Grammar cell of this row | `āsavakkhaya- \| noun` | 8 |
| per-74-the-highest-honour-and-aspirations.md:141 | `vahaṃ \| adj` | Second member is āvahaṃ (DPD āvaha, adj, in comps, from āvahati), not vahaṃ | `āvahaṃ \| adj` | 8 |
| post-patimokkha.md:5 | `pubbabhaganamakāraṃ` | `bhaga` lacks the long ā; table line 13 and DPD (pubbabhāga 3, "preliminary part") have pubbabhāga | `pubbabhāganamakāraṃ` | 9 |
| post-patimokkha.md:13 | `pubbabhāga- \| adj` | DPD: pubbabhāga is masc, comp (a noun), not adj | `pubbabhāga- \| noun` | 8 |
| post-patimokkha.md:16 | `namakāraṃ \| noun \| nt.acc.sg` | DPD namakāra: masc, comp | `namakāraṃ \| noun \| masc.acc.sg` | 8 |
| post-patimokkha.md:18 | `\>kāraṃ \| noun \| nt.acc.sg` | DPD kāra 1 ("deed; action; service"): masc | `\>kāraṃ \| noun \| masc.acc.sg` | 8 |
| post-patimokkha.md:23 | `sammasambuddhassa` | Missing long ā (DPD sammāsambuddha); table line 31 has `sammā-`, line 110 `sammāsambuddhena` | `sammāsambuddhassa` | 9 |
| post-patimokkha.md:46 | `saranaṃ` | Dental n for retroflex ṇ (DPD saraṇa 1.1 "refuge"; cf. `saraṇaṃ` per-74:17) | `saraṇaṃ` (both occurrences) | 9 |
| post-patimokkha.md:68 | `saranaṃ` | Dental n for retroflex ṇ (DPD saraṇa 1.1) | `saraṇaṃ` (both occurrences) | 9 |
| post-patimokkha.md:75 | `saranaṃ` | Dental n for retroflex ṇ (DPD saraṇa 1.1) | `saraṇaṃ` (both occurrences) | 9 |
| post-patimokkha.md:46 | `annaṃ` | añña ("other", DPD añña 1.1 pron) misspelt as annaṃ (= food) | `aññaṃ` | 9 |
| post-patimokkha.md:68 | `annaṃ` | añña ("other", DPD añña 1.1 pron) misspelt as annaṃ | `aññaṃ` | 9 |
| post-patimokkha.md:75 | `annaṃ` | añña ("other", DPD añña 1.1 pron) misspelt as annaṃ | `aññaṃ` | 9 |
| post-patimokkha.md:53 | `saranaṃ` | Dental n for retroflex ṇ (DPD saraṇa 1.1) | `saraṇaṃ` | 9 |
| post-patimokkha.md:57 | `saranaṃ` | Dental n for retroflex ṇ (DPD saraṇa 1.1) | `saraṇaṃ` | 9 |
| post-patimokkha.md:54 | `annaṃ` | añña ("other", DPD añña 1.1 pron) misspelt as annaṃ | `aññaṃ` | 9 |
| post-patimokkha.md:99 | `bhasitam’idaṃ` | DPD bhāsita (pp of bhāsati) has long ā | `bhāsitam’idaṃ` | 9 |
| post-patimokkha.md:103 | `bhasitaṃ` | DPD bhāsita (pp of bhāsati) has long ā | `bhāsitaṃ` | 9 |
| post-patimokkha.md:99 | `janatā passatā` | Should be jānatā (prp ins sg of jānāti, "by the one who knows"), paired with passatā; janatā means "people". DPD has jānāti; the prp form jānatā was not looked up | `jānatā passatā` | 7 |
| post-patimokkha.md:107 | `janatā` | Should be jānatā (prp of jānāti); DPD prp form not looked up | `jānatā` | 7 |
| post-patimokkha.md:197 | `janatā passatā` | Should be jānatā (prp of jānāti); DPD prp form not looked up | `jānatā passatā` | 7 |
| post-patimokkha.md:167 | `ācāragocarasampanna.` | Final ā missing (masc nom pl of sampanna, pp, agreeing with viharissāma; line 125 has `ācāragocarasampannā`) | `ācāragocarasampannā.` | 8 |
| pubbakicca-analysis.md:15 | `ud+ √dis･1 a (point out, explain)` | uddisati / uddesituṃ is √dis 2 a in DPD; √dis 1 is a different root. | `ud+ √dis･2 a (point out, explain)` | 8 |
| pubbakicca-analysis.md:532 | `ud√dis･1 a (point out, explain)` | Same root number error (DPD uddesituṃ: √dis 2 a). | `ud√dis･2 a (point out, explain)` | 8 |
| pubbakicca-analysis.md:65 | `\| \#paribhojanīya \| adj \| nt. \| rinsing water \|` | POS adj, but DPD has paribhojanīya nt 'washing water; rinsing water', and the gloss is a noun. POS cell only; known pubbakicca-10 touches the Grammar cell. | `\| \#paribhojanīya \| noun \| nt. \| rinsing water \|` | 8 |
| pubbakicca-analysis.md:71 | `\| chand'ārahānaṃ \| adj \| masc.gen.pl \| and [bringing] the consent of the monks entitled to vote by proxy \|` | Repeats the word of :68 instead of giving the member of chand'āharaṇañ'ca (DPD chandāharaṇa nt 'conveying consent', gloss as at :143). | `\| \#chand'āharaṇaṃ \| noun \| nt.nom.sg \| conveying consent \| \|` | 8 |
| pubbakicca-analysis.md:85 | `\| \#uposathānaṃ \| noun \| masc.acc.sg \|` | `-ānaṃ` is gen.pl, not acc.sg (DPD uposatha masc). | `\| \#uposathānaṃ \| noun \| masc.gen.pl \|` | 8 |
| pubbakicca-analysis.md:99 | `\| \#\#bhikkhunaṃ \| noun \| masc.gen.pl \|` | Misspelt: gen.pl is bhikkhūnaṃ (long ū), as at :69 and in DPD bhikkhugaṇanā (bhikkh<b>ūnaṃ</b> + gaṇanā). | `\| \#\#bhikkhūnaṃ \| noun \| masc.gen.pl \|` | 8 |
| pubbakicca-analysis.md:119 | `\| padīpakiccaṃ \| sandhi \| \|` | Plain compound with no sandhi; DPD padīpakicca is nt (tatiyā tappurisa); parallel `pubbakiccaṃ` (:39) is `noun \| nt.nom.sg`. | `\| padīpakiccaṃ \| noun \| nt.nom.sg \|` | 8 |
| pubbakicca-analysis.md:131 | `\| vattaṃ \| noun \| nt.nom.sg \|` | Object of jānantehi ("knowing the practice"), so acc. | `\| vattaṃ \| noun \| nt.acc.sg \|` | 7 |
| pubbakicca-analysis.md:155 | `sīda (irreg)+na+ṃ` | Ending of nisinnānaṃ (masc.gen.pl) given as `+ṃ`; the gen.pl ending is -ānaṃ. (The sīda stem itself agrees with DPD nisinna: ni + sīda + na.) | `sīda (irreg)+na+ānaṃ` | 6 |
| pubbakicca-analysis.md:157 | `\| abhāvato \| noun \| masc.nom.sg \| absence (of) \|` | `-to` form is abl.sg ("because of the absence"), as the translation renders it (DPD abhāva masc). | `\| abhāvato \| noun \| masc.abl.sg \| because of the absence (of) \|` | 8 |
| pubbakicca-analysis.md:192 | `\| hemantagimhavassānānaṃ \| noun \| masc.acc.sg \|` | `-ānaṃ` is gen.pl (governed by vasena); DPD hemanta masc. | `\| hemantagimhavassānānaṃ \| noun \| masc.gen.pl \|` | 8 |
| pubbakicca-analysis.md:267 | `\| \#atthāya \| adj \| masc.dat.sg \|` | DPD atthāya 1: masc, in comps, dat sg; POS adj contradicts the tag. | `\| \#atthāya \| noun \| masc.dat.sg \|` | 8 |
| pubbakicca-analysis.md:324 | `\| sakaraṇ'okāsānaṃ \| adj \| masc.gen.pl \|` | Bahubbīhi qualifying pubbakiccānaṃ (nt.gen.pl, :328), so neuter. DPD has no sakaraṇa headword. | `\| sakaraṇ'okāsānaṃ \| adj \| nt.gen.pl \|` | 6 |
| pubbakicca-analysis.md:331 | `\| katattā \| noun \| nt.nom.pl (+gen) \|` | DPD katattā: nt, abl sg of katatta ("because of doing"), as its own gloss says. | `\| katattā \| noun \| nt.abl.sg (+gen) \|` | 9 |
| pubbakicca-analysis.md:339 | `\| pariniṭṭhitattā \| noun \| nt.nom.pl \| total accomplishment(s) \|` | abl.sg of pariniṭṭhitatta (DPD nt abstr), parallel to katattā. | `\| pariniṭṭhitattā \| noun \| nt.abl.sg \| because of being fully accomplished \|` | 8 |
| pubbakicca-analysis.md:393 | `\| cattāro \| noun \| masc.nom.pl \| four \|` | POS noun; DPD cattāro is card, and the same word at :285 is `card`. | `\| cattāro \| card \| masc.nom.pl \| four \|` | 9 |
| pubbakicca-analysis.md:436 | `\| sabhāg'āpattiyo \| adj \| fem.nom.pl \|` | Kammadhāraya "common offences" (DPD sabhāga adj + āpatti fem noun), subject of vijjanti: a noun. The gloss "having offences in common" reads it as an adj, so check. | `\| sabhāg'āpattiyo \| noun \| fem.nom.pl \|` | 6 |
| pubbakicca-analysis.md:438 | `\| \#āpattiyo \| adj \| fem.nom.pl \| having offences \|` | DPD āpatti 2: fem noun '(vinaya) offence'. | `\| \#āpattiyo \| noun \| fem.nom.pl \| offences \|` | 8 |
| pubbakicca-analysis.md:460 | `\| vajjanīyapuggalo \| sandhi \| \|` | Plain compound with no sandhi (DPD vajjanīya ptp + puggala masc). | `\| vajjanīyapuggalo \| noun \| masc.nom.sg \|` | 7 |
| pubbakicca-analysis.md:461 | `\| \#vajjanīya \| adj \|` | DPD: vajjanīya is ptp of vajjeti. POS cell only; known pubbakicca-55 touches the Grammar cell. | `\| \#vajjanīya \| ptp \|` | 8 |
| pubbakicca-analysis.md:482 | `\| pattakallaṃ \| noun \| nt. \|` | Top-level word tagged with stem gender only (DPD pattakalla nt); it is nom.sg (predicate of hoti). Known pubbakicca-60 only strips the period in the same cell; this row supersedes it. | `\| pattakallaṃ \| noun \| nt.nom.sg \|` | 7 |
| pubbakicca-analysis.md:503 | `\| \#kallattaṃ \| adj \| nt.nom.sg \| proper \|` | `-tta` abstract noun (Root cell: kalla + tta), not adj. DPD has no kallatta headword. | `\| \#kallattaṃ \| noun \| nt.nom.sg \| properness; suitability \|` | 7 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:141 | `neutr. n. nom. pl. sentence subject` | *vārivaha* (river) is masculine (DPD *vārivaha 2* masc); `-ā` nom. pl. is the masculine ending (neuter would be `-āni`) | `m. n. nom. pl. sentence subject` | 9 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:143 | `neutr. adj. nom. pl. in agreement with *vārivahā*` | agrees with masculine *vārivahā* (DPD *vārivaha 2* masc; *pūra* adj); `pūrā` is m. nom. pl. | `m. adj. nom. pl. in agreement with *vārivahā*` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:147 | `*vārivahaṃ*).` | wrong form of the subject: the noun in the verse and at line 141 is *vārivahā* (nom. pl.), not acc. sg. `-aṃ` | `*vārivahā*).` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:139 | `introducing the main clause` | *yathā* introduces the subordinate (comparison) clause; *evameva* (line 151) introduces the main clause. Line 199 treats the *yathā* clause as subordinate. Labels at 149, 159, 161 follow the same swap | `introducing the subordinate clause` | 6 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:151 | `conjunctive *nipāta* introducing the subordinate` | *evameva* introduces the main clause (correlative of *yathā*), see row for line 139 | `conjunctive *nipāta* introducing the main` | 6 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:179 | `– adv. compound` | *khippameva* is a sandhi of *khippaṃ* + *eva*, not a compound (cf. *evameva* line 151, DPD `sandhi`; DPD *khippaṃ* ind, adv); DPD has no headword for *khippameva* itself | `– adv. + emphatic *nipāta* (sandhi)` | 5 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:199 | `comparison with *chando*` | misspelt: the word is *cando* (line 193, verse line 79) | `comparison with *cando*` | 9 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:203 | `– m. nom. pl. nominal compound subject of` | *maṇijotiraso* (DPD *maṇijotirasa* masc) ends in `-o`: nom. sg., not pl. | `– m. nom. sg. nominal compound subject of` | 9 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:217 | `[of *vivajjeti*] third pers. pass. pl.` | `vivajjantu` is the active imp. 3 pl. of *vivajjati* (DPD *vivajjati* pr "does not happen; does not occur"); *vivajjeti* "avoids" would give *vivajjentu*; no passive marker | `[of *vivajjati*] third pers. act. pl.` | 7 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:225 | `[of *vinassati*] third pers. pass. sg.` | *vinassati* is an intransitive active verb (DPD pr, √nas ya), not passive; the passive sense is in the gloss only. Line 187 tags the same kind of form `act.` | `[of *vinassati*] third pers. act. sg.` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:347 | `[of *vinassati*] third pers. pass. pl.` | same as line 225: *vinassantu* is active in form (DPD *vinassati* pr, √nas ya) | `[of *vinassati*] third pers. act. pl.` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:235 | `– m. nom. sg. nominal compound subject of main` | *bhavatvantarāyo* is a sandhi of a verb (*bhavatu*) and a noun (*antarāyo*, DPD *antarāya* masc); it cannot be a nominal compound or the subject as a whole | `– sandhi; *antarāyo* m. n. nom. sg. subject of main` | 7 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:337 | `m. nom. pl. nominal compound` | *cupaddavā* is a sandhi of the particle *ca* + *upaddavā* (DPD *upaddava* masc), not a nominal compound | `sandhi; *upaddavā* m. n. nom. pl.` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:349 | `m. adj. dat. sg. used adverbially` | `-to` is an ablative ending; DPD: *asesato* ind, adv, abl sg of na sesa | `m. adj. abl. sg. used adverbially` | 9 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:373 | `(“riches”, “possessions” – m. n. nom. sg.)` | `bhogaṁ` cannot be m. nom. sg. (*bhogo*); DPD *bhoga 1.3* is nt "wealth; possessions; property; riches", which fits the gloss: nt. nom. sg. | `(“riches”, “possessions” – neutr. n. nom. sg.)` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:381 | `agreement with *āyu*` | *satavassā* (pl.) agrees with the plural *āyū* (line 383), not *āyu* | `agreement with *āyū*` | 7 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:399 | `*vaṇṇado paṭibhāṇado.*` | *paṭibhāna* has dental `n` (DPD *paṭibhāna*, *paṭibhānada*); line 407 has `paṭibhānakaṁ`. Chant-line change | `*vaṇṇado paṭibhānado.*` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:441 | `*paṭibhāṇado*:` | same spelling as line 399 (DPD *paṭibhānada*) | `*paṭibhānado*:` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:477 | `*upapapajjati*` | Misspelt (extra `pa`); the same line then spells it `*upapajjati*` (DPD: upapajjati, pr, √pad ya). | `*upapajjati*` | 9 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:495 | `*piṭakattayānubhavena*` | Short `a`: the word is `ānubhāva` (DPD ānubhāva, masc; the 619 analysis itself gives `*ānubhāvena*`; every other compound in the chant has `-ānubhāvena`). | `*piṭakattayānubhāvena*` | 9 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:619 | `*piṭakattayānubhavena*:` | Same misspelling in the headword (DPD ānubhāva). | `*piṭakattayānubhāvena*:` | 9 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:599 | `[*saṅghaṃ* + *ratanaṃ*]` | `saṅgha` is masculine (DPD saṅgha 1 masc); the parallel analyses at 591 and 595 give the nom. sg. `*buddho*`, `*dhammo*`. | `[*saṅgho* + *ratanaṃ*]` | 9 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:609 | `m. n. instr. pl.` | `ānubhāvena` is instr. sg. (masc `-ena`; the compounds at 581–589 say sg.). | `m. n. instr. sg.` | 9 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:615 | `*khanda*` | Misspelt; the headword has `-kkhandha-` (DPD khandha, masc). | `*khandha*` | 9 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:645 | `third pers. pass. pl.` | `vinassati` is an active intransitive verb (DPD vinassati: pr, √nas ya, "perishes; is destroyed"), not a passive; the passive sense is only in the English. | `third pers. act. pl.` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:687 | `third pers. pass. pl.` | Same as 645 (DPD vinassati: pr, √nas ya). | `third pers. act. pl.` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:677 | `m. nom. pl. nominal compound` | `cupaddavā` is the sandhi `ca` + `upaddavā`, not a compound (the analysis in the same line shows that; DPD upaddava 1 masc). | `sandhi of *ca* + m. n. nom. pl.` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:689 | `m. adj. dat. sg. used adverbially` | `-to` is an ablative ending, not dative. DPD: `asesato` ind, adv, abl sg of na sesa. | `m. adj. abl. sg. used adverbially` | 9 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:713 | `(“riches”, “possessions” – m. n. nom. sg.)` | `bhogaṃ` cannot be masc. nom. sg. (`bhogo`). DPD bhoga 1.3 is nt with exactly this meaning ("wealth; possessions; property; riches"), so `bhogaṃ` is neutr. nom. sg. | `(“riches”, “possessions” – neutr. n. nom. sg.)` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:721 | `agreement with *āyu*` | The word it agrees with is the plural `āyū` (chant line 537, entry 723). | `agreement with *āyū*` | 7 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:820 | `(“is realized” – pres. part. vb. [of *vijānati*] in agreement with *dhammaṃ*)` | `vijānataṃ` is a pres. part. gen. pl. ("of those who understand"), parallel with `pasannānaṃ`; it does not agree with the acc. sg. `dhammaṃ`, which is its object. DPD has the verb (vijānāti) but no entry for the participle form. | `(“of those who understand” – pres. part. vb. [of *vijānati*] functioning as m. n. gen. pl.; *dhammaṃ* is its object)` | 7 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:852 | `(“in the saṅgha” – neutr. n. loc. sg.)` | `saṅgha` is masculine (DPD saṅgha 1 masc). | `(“in the saṅgha” – m. n. loc. sg.)` | 9 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:878 | `m. adj. nom. sg. in agreement with` | `aggaṃ` agreeing with the neuter `āyu` (DPD āyu nt) is neuter nom. sg.; the masc. nom. sg. would be `aggo`. | `neutr. adj. nom. sg. in agreement with` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:878 | `*ayu* and also modifying *vanno*` | Missing diacritics (cf. 880 `*āyu*`, 882 `*vaṇṇo*`). | `*āyu* and also modifying *vaṇṇo*` | 9 |

### B. Tables, paradigms and lists that disagree with each other or themselves

| Location | Current | Problem | Suggested | Conf. |
| --- | --- | --- | --- | --- |
| per-06-salutation-to-the-triple-gem.md:125 | `\| khetta- \| noun \| \| field, plot of land \|` | This row repeats the `khetta` already contained in `abhyatikhetta-` (124). The chant (`sukhettābhyatikhetta-saññito`) has only one `khetta` after `abhyati`. DPD has `khetta` (nt) but no headword `abhyatikhetta`. | Delete row 125 | 6 |
| per-06-salutation-to-the-triple-gem.md:328 | `\| rūpa- \| \| \| form, matter` | The POS cell is empty; compound members elsewhere in this file carry `noun` (DPD `rūpa 1` nt). Known 06-30…34 touch only the `upādānakkhandho` rows. | POS `noun` | 8 |
| per-06-salutation-to-the-triple-gem.md:330 | `\| vedan- \| \| \| experience, feeling` | The POS cell is empty (DPD `vedanā` fem). | POS `noun` | 8 |
| per-06-salutation-to-the-triple-gem.md:332 | `\| saññā- \| \| \| perception` | The POS cell is empty (DPD `saññā` fem). | POS `noun` | 8 |
| per-06-salutation-to-the-triple-gem.md:334 | `\| saṅkhāra- \| \| \| intention` | The POS cell is empty (DPD `saṅkhāra` masc). | POS `noun` | 8 |
| per-06-salutation-to-the-triple-gem.md:336 | `\| viññāṇa- \| \| \| consciousness` | The POS cell is empty (DPD `viññāṇa` nt). | POS `noun` | 8 |
| per-08-respect-for-the-dhamma.md:44 | `\| buddhānaṃ \| noun \| masc.gen.pl \| of Buddhas \|` | The chant (31) reads the metrical `buddhāna`; the row gives a different form. | `buddhāna` | 5 |
| per-08-respect-for-the-dhamma.md:62 | `\| buddhānaṃ \| noun \| masc.gen.pl \| of Buddhas \|` | The chant (50) reads the metrical `buddhāna`; the row gives a different form. | `buddhāna` | 5 |
| per-13-from-the-elder-ratthapala.md:162 | `\| vittena \| noun \| masc.ins.sg \|` | DPD vitta nt; known row B-N39 changes `vittaṃ` (line 107) only; this second instance is not covered | `\| vittena \| noun \| nt.ins.sg \|` | 8 |
| per-13-from-the-elder-ratthapala.md:186 | `\| dhanena \| noun \| masc.ins.sg \|` | DPD dhana nt; same word tagged nt at lines 111 (`dhanaṃ`) and 159 (`dhanena`) | `\| dhanena \| noun \| nt.ins.sg \|` | 9 |
| per-14-from-the-elder-parapariya.md:150 | `\| \>mānasā \| noun \| masc.ins.sg \|` | Final member of the bahubbīhi `atthaddhamānasā` (DPD: kammadhāraya > bahubbīhi; known B-N49 tags the whole, line 147, masc.nom.pl); cf. line 134 `\>parāyanā` tagged like its whole | `\| \>mānasā \| noun \| masc.nom.pl \|` | 7 |
| per-19-anupubba-sikkha.md:136 | `\| anupubba-sikkhā \| noun \| fem.acc.pl \|` | same compound tagged `fem.nom.sg` at line 150 in the same construction (`sakkā … paññapetuṃ`); plural is wrong for one "gradual training" (DPD anupubbasikkhā: fem; case not given by DPD) | `\| anupubba-sikkhā \| noun \| fem.nom.sg \|` | 7 |
| per-19-anupubba-sikkha.md:137 | `\| anupubba-kiriyā \| noun \| fem.acc.pl \|` | same compound tagged `fem.nom.sg` at line 151 in the same construction | `\| anupubba-kiriyā \| noun \| fem.nom.sg \|` | 7 |
| per-19-anupubba-sikkha.md:138 | `\| anupubba-paṭipadā \| noun \| fem.acc.pl \|` | same compound tagged `fem.nom.sg` at line 152 in the same construction | `\| anupubba-paṭipadā \| noun \| fem.nom.sg \|` | 7 |
| per-19-anupubba-sikkha.md:618 | `\| evameva \| kho \| ind \| in the same way \|` | touches known item 19-17 (same row): 19-17 rebuilds it as `evameva kho`, but the chant line 614 reads `evameva bhikkhu` with no `kho`, so that rebuild adds a word absent from the text; DPD has both `evameva` (sandhi) and `evameva kho` (idiom). Owner to choose between this row and 19-17; POS `ind` vs DPD `sandhi` is policy BP7 (open) | `\| evameva \| ind \| \| in the same way \|` | 7 |
| per-19-anupubba-sikkha.md:794 | `yāva'd'eva \| \| ind \|` | POS empty, `ind` shifted into the Grammar column (DPD yāvadeva: sandhi; POS value itself falls under policy BP7) | `yāva'd'eva \| ind \| \| just up to; as far as` | 8 |
| per-19-anupubba-sikkha.md:1065 | `ime pañca nīvaraṇe appahīne attani` | chant line ends without `samanupassati`, which the table glosses (line 1085) and the parallel line 1089 has | `ime pañca nīvaraṇe appahīne attani samanupassati.` | 7 |
| per-19-anupubba-sikkha.md:1034 | `sato \| adj \| masc.nom.sg` | same word has POS `pp` at line 878; DPD sata 1.1 is pp of sarati | `sato \| pp \| masc.nom.sg` | 7 |
| per-21-the-seven-factors-of-awakening.md:18 | `ariyā \| adj \| fem.nom.sg` | Duplicate row: the chant line (8) has `ariyā` only once, already glossed on line 17 as masc.nom.pl | delete the row on line 18 | 8 |
| per-23-mindfulness-of-breathing.md:196 | `\| paṭisaṃvedī \| noun \| masc.nom.sg \|` | Same word is POS `adj` at lines 153 and 163; DPD `paṭisaṃvedī` is adj | `\| paṭisaṃvedī \| adj \| masc.nom.sg \|` | 8 |
| per-24-dependent-origination.md:37 | `upādānapaccayā \| \| \| from grasping as condition` | POS and Grammar empty, unlike every other `…paccayā` row in the file (DPD paccaya 1/3 masc) | `upādānapaccayā \| noun \| masc.abl.sg \| from grasping as condition` | 9 |
| per-29-striving-according-to-the-dhamma.md:135 | `\| ca \| \| ind \| but \|` | POS shifted into Grammar column | `\| ca \| ind \| \| but \|` | 9 |
| per-30-the-buddhas-final-instruction.md:25 | `\| atīta- \| \| \| has passed \|` | POS empty (DPD atīta 2 pp "past; gone past; bygone") | `\| atīta- \| pp \| \| passed, gone by \|` | 8 |
| per-31-the-four-requisites.md:113 | `\| uppannānaṃ \| pp \| masc.dat.pl \|` | phrase is genitive (`vedanānaṃ` tagged `fem.gen.pl`, l. 115) and agrees with fem `vedanānaṃ` | `fem.gen.pl` | 7 |
| per-31-the-four-requisites.md:114 | `\| veyyābādhikānaṃ \| adj \| masc.dat.pl \|` | agrees with `vedanānaṃ` fem.gen.pl | `fem.gen.pl` | 7 |
| per-31-the-four-requisites.md:28 | `\| hirikopīna- \| noun \| that which arouses shyness, private shameful \| parts \|` | gloss shifted into Grammar column and split | `\| hirikopīna- \| noun \| \| that which arouses shyness, private shameful parts \|` | 9 |
| per-31-the-four-requisites.md:48 | `\| yāva'd'eva \| \| ind \| just up to; as far as \|` | POS shifted into Grammar column | `\| yāva'd'eva \| ind \| \| just up to; as far as \|` | 9 |
| per-32-the-repulsiveness-of-food.md:52 | `jigucchanīyāni \| ptp \| nt.nom.pl` | Row does not match chant line 43 `jigucchanīyo` (agrees with `piṇḍapāto`); the plural looks copied from the robe reflection (`cīvarāni … jigucchanīyāni jāyanti`) | `jigucchanīyo \| ptp \| masc.nom.sg` (confirm chant against the SBS book) | 7 |
| per-32-the-repulsiveness-of-food.md:53 | `jāyanti \| verb \| pr.3.pl \| born; arises` | Row does not match chant line 43 `jāyati` | `jāyati \| verb \| pr.3.sg \| becomes; is born; arises` (confirm chant against the SBS book) | 7 |
| per-36-ten-subjects-for-frequent-recollection-by-one-who-has-gone-forth.md:18 | `paccavekkhitabbaṃ \| ptp \| masc.acc.sg` | Chant line 8 has `paccavekkhitabbā`, agreeing with `dhammā` (DPD paccavekkhitabba ptp) | `paccavekkhitabbā \| ptp \| masc.nom.pl` | 8 |
| per-36-ten-subjects-for-frequent-recollection-by-one-who-has-gone-forth.md:30 | `ajjhūpagato' ti` | Row does not match chant line 24 `ajjhupagato'ti` (ū, stray space); DPD ajjhupagata has short u | `ajjhupagato'ti` | 8 |
| per-43-ratanattayanubhavadi-gatha.md:21 | `\| bhayā- \| noun \| nt.nom.pl \|` | Row carries a full case tag but is hyphenated as a bare compound member; as the inflected end of `dukkha-roga-bhayā` it needs no hyphen (per-45:56 writes `bhayā` without one). Tag agrees with DPD bhaya 2 nt | `\| bhayā \| noun \| nt.nom.pl \|` | 7 |
| per-45-culla-mangala-cakka-vala.md:88 | `\| bhayā- \| noun \| nt.nom.pl \|` | Same as per-43:21: hyphen on an inflected form with a case tag | `\| bhayā \| noun \| nt.nom.pl \|` | 7 |
| per-43-ratanattayanubhavadi-gatha.md:24 | `\| sattu \| noun \| \| enemy, enmity \|` | Free-standing inflected word in a list of nominatives (`sokā sattu c'upaddavā`) but Grammar empty, unlike every neighbour. DPD sattu 2.1 is masc; DPD does not settle sg/pl here | `\| sattu \| noun \| masc.nom.pl \| enemy, enmity \|` (owner: sg or pl) | 5 |
| per-45-culla-mangala-cakka-vala.md:91 | `\| sattu \| noun \| \| enemy, enmity \|` | Same as per-43:24: Grammar empty on a free-standing nominative (DPD sattu 2.1 masc) | `\| sattu \| noun \| masc.nom.pl \| enemy, enmity \|` (owner: sg or pl) | 5 |
| per-43-ratanattayanubhavadi-gatha.md:58 | `\| āyū \| noun \| masc.nom.pl \|` | DPD āyu is nt only; same table tags `āyu` `nt.nom.sg` (line 47), and the translation reads one lifespan ("a lifespan of … years"), so `āyū` is the metrically lengthened nt nom sg | `\| āyū \| noun \| nt.nom.sg \|` | 7 |
| per-45-culla-mangala-cakka-vala.md:126 | `\| āyū \| noun \| masc.nom.pl \|` | Same as per-43:58 (DPD āyu nt; line 115 tags `āyu` `nt.nom.sg`) | `\| āyū \| noun \| nt.nom.sg \|` | 7 |
| per-44-bhojana-dananumodana.md:41 | `\| dātā \| adj \| masc.nom.sg \|` | Same word in the same phrase (`dātā medhāvī`) is POS `noun` in per-46:69; `dātu` is an agent noun (DPD has no `dātu` headword) | `\| dātā \| noun \| masc.nom.sg \|` | 6 |
| per-51-nama-kara-siddhi-gatha.md:98 | `\| anugo \| adj \| \|` | Inflected final member of `sugatānugo` (DPD anuga adj) but Grammar empty | `\| anugo \| adj \| masc.nom.sg \|` | 7 |
| per-55-karaniya-metta-sutta.md:20 | `\| \| adj \| masc.ins.sg \| by skillful \|` | Pāli cell is empty: the word `kusalena` (end of the compound in line 9; DPD kusala 2 adj "skilled") is missing from the analysis | `\| kusalena \| adj \| masc.ins.sg \| by skillful \|` | 9 |
| per-56-khandha-parittam.md:135 | `\| katā \| pp \| masc.nom.pl \|` | `katā` agrees with `rakkhā` (DPD rakkhā fem); masc does not agree; translation line 152 is singular ("Protection done by me") | `fem.nom.sg` | 6 |
| per-58-yan-kinci-ratanam-loke.md:50 | `\| sotthinā \| noun \| masc.ins.sg \|` | `sotthi` is feminine (DPD sotthi 1.1 fem; line 22 `sotthī` fem; per-59:57 `sotthi` fem) | `fem.ins.sg` | 9 |
| per-59-bojjhanga-parittam.md:22 | `\| apare \| adj \| \|` | Free word (not a compound member) with empty Grammar; agrees with `bojjh'aṅgā` | `masc.nom.pl` | 7 |
| per-62-jaya-mangala-attha-gatha.md:124 | `gabbhiniyā \| adj \| fem.gen.sg` | Chant line 116 has `gabbhinīyā` (the metre needs long nī); table and chant disagree | `gabbhinīyā \| adj \| fem.gen.sg` | 6 |
| per-66-vipassana-bhumi-patho.md:133 | `\| upādānapaccayā \| \| \| from grasping as condition \|` | POS and Grammar empty; all sibling `…paccayā` rows (L129–137) have `noun \| masc.abl.sg` | `\| upādānapaccayā \| noun \| masc.abl.sg \| from grasping as condition \|` | 8 |
| per-70-sharing-and-aspirations.md:29 | `\| mātā-pitā \| noun \| masc.nom.sg \|` | Dvanda "parents" is plural; the same word is `masc.nom.pl` at per-71:39 (DPD: no mātāpitu headword) | `\| mātā-pitā \| noun \| masc.nom.pl \|` | 7 |
| per-70-sharing-and-aspirations.md:212 | `\| nātha- \| noun \| masc.nom.sg \|` | Compound member (chant `nāth'ottaro`) carries a full case tag; every other member in the file (`buddha-`, `adhipa-`, `vara-` L193–199) has empty Grammar; wrong under both A5.7 and B11.3 | `\| nātha- \| noun \| \|` | 7 |
| per-71-sharing-of-all-merits.md:39 | `\| mātāpitā- \| noun \| masc.nom.pl \|` | Member of `mātāpit'ādayo` carries a full case tag; other members in the file (`satta-`, `majjhatta-`) have empty Grammar | `\| mātāpitā- \| noun \| \|` | 6 |
| per-73-sharing-of-merits-with-the-devas.md:21 | `\| sabba \| adj \| masc.nom.pl \|` | Member of `sabba-sampatti-siddhiyā` (L8) treated as a free word with a case tag | `\| sabba- \| adj \| \|` | 7 |
| per-73-sharing-of-merits-with-the-devas.md:22 | `\| sampatti \| noun \| fem.nom.sg \|` | Member of `sabba-sampatti-siddhiyā` treated as a free word with a case tag | `\| sampatti- \| noun \| \|` | 7 |
| post-patimokkha.md:55 | `\| annaṃ \| \| \| \|` | Duplicate row; in chant order (line 46) the word after aññaṃ is buddho, which has no row | `\| buddho \| \| \| \|` | 9 |
| pubbakicca-analysis.md:70 | `\| chand'āharaṇañ'ca \| \| \| \| \|` | Headword row has empty POS and English cells. | `\| chand'āharaṇañ'ca \| sandhi \| \| and the bringing of consent \| \|` | 8 |
| pubbakicca-analysis.md:103 | `fem.dat.pl \| to the nuns` | Same compound parsed as gen at :309 (`fem.gen.pl \| of the nuns`). | `fem.gen.pl \| of the nuns` | 5 |
| pubbakicca-analysis.md:216 | `\| asmiñ'ca \| sandhi \| \| \| \|` | English cell empty. | `\| asmiñ'ca \| sandhi \| \| and in this \| \|` | 8 |
| pubbakicca-analysis.md:297 | `\| bhikkhugaṇanā'pi \| sandhi \| \| \| \|` | English cell empty. | `\| bhikkhugaṇanā'pi \| sandhi \| \| the counting of the monks too \| \|` | 8 |
| pubbakicca-analysis.md:311 | `\| pana \| \| \| \| \|` | POS and English empty (cf. :150 `pana \| ind \| \| but`; DPD pana ind). | `\| pana \| ind \| \| but \| \|` | 8 |
| pubbakicca-analysis.md:332 | `\| nikkaraṇ'okāsānaṃ \| adj \| \|` | Grammar cell empty; the parallel word at :324 is tagged. | `\| nikkaraṇ'okāsānaṃ \| adj \| nt.gen.pl \|` | 7 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:261 | `with fut. indication` | `fut.` is used but missing from the Abbreviations list (lines 5–59) | add `fut. future tense` to the Abbreviations list after `f. feminine gender` (line 19) | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:5 | `abs. absolute construction` | `abs.` is used for the absolutive *datvā* (line 457; DPD *datvā* pos `abs`, "having given"), not an absolute construction | `abs. absolutive` (verify use of `abs.` in lines 459–916 first) | 5 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:435 | `(“the one who gives strength” [*āyu* + *do*` | copy-paste from line 433: first member is *bala* (DPD *balada* bala + da) | `(“the one who gives strength” [*bala* + *do*` | 9 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:439 | `(“the one who gives beauty” [*āyu* + *do*` | copy-paste from line 433: first member is *vaṇṇa* (DPD *vaṇṇada* vaṇṇa + da) | `(“the one who gives beauty” [*vaṇṇa* + *do*` | 9 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:441 | `(“the one who gives intelligence” [*āyu* + *do*` | copy-paste from line 433: first member is *paṭibhāna* (DPD *paṭibhānada* paṭibhāna + da) | `(“the one who gives intelligence” [*paṭibhāna* + *do*` | 9 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:900 | `m. nom. sg. nominal compound in` | Called a nominal compound although it agrees with `dātā` as an adjective; DPD aggadhammasamāhita is adj, comp (tatiyā tappurisa); the parallel entries at 904 and 912 say `adjectival compound`. | `m. nom. sg. adjectival compound in` | 8 |

### C. Translation and gloss problems

| Location | Current | Problem | Suggested | Conf. |
| --- | --- | --- | --- | --- |
| per-03-homage-to-the-buddha.md:13 | `\| karomase \| verb \| ref.pr.1.pl \| we do, make, act, perform \|` | English gloss is indicative; DPD karomase is imp, reflx 1st pl ("we must do; let us make; let us act; we must perform"). per-04:13 and per-05:13 already use the imperative gloss. Known rows 03-02/03-03 touch only the Grammar cell | English `let us make; let us act; we must perform` | 9 |
| per-03-homage-to-the-buddha.md:15 | `**now we make high praise to the Buddha**` | Translation renders the imperative `karomase` (DPD imp) as indicative; per-04:15 and per-05:15 have "let us perform" | `**now let us make high praise to the Buddha**` | 8 |
| per-03-homage-to-the-buddha.md:75 | `having realized it himself` … `higher understanding, proclaimed` | `abhiññā` (DPD abhiññā 3, ger, "directly knowing") is left without a connecting word, so the clause does not parse. Known row 03-08 only removes the double space here; this row adds the missing word | `having realized it himself through higher understanding, proclaimed` | 6 |
| per-06-salutation-to-the-triple-gem.md:471 | `that, he` | An accusative form is glossed with the nominative "he" (DPD `taṃ 1.2`: him; her; one). | `that, him` | 8 |
| per-09-going-to-true-and-false-refuges.md:63 | `\| ariya-saccāni \| noun \| nt.acc.pl \| noble truth \|` | A plural form is glossed in the singular (DPD `ariyasacca`: noble truth). | `noble truths` | 8 |
| per-10-the-patimokkha-exhortation.md:76 | `these are the Teachings of the Buddhas` | `etaṃ … sāsanaṃ` is singular (DPD sāsana nt; row 74 `nt.nom.sg`); the same pāda at line 24 is rendered "This is the Teaching of the Buddhas" | `this is the Teaching of the Buddhas` | 7 |
| per-13-from-the-elder-ratthapala.md:168 | `\| āhu \| verb \| perf.3.pl \| they said \|` | DPD āhu gloss `they say`; translation line 173 has "the wise say" | `\| āhu \| verb \| perf.3.pl \| they say \|` | 8 |
| per-13-from-the-elder-ratthapala.md:170 | `not eternal, endless, perpetual` | `endless, perpetual` give the opposite meaning; DPD asassata: "not eternal; not endless; not perpetual" | `not eternal, not endless, not perpetual` | 9 |
| per-13-from-the-elder-ratthapala.md:188 | `with which (woman)` | `yāya` is fem because it refers to `paññā`, not to a woman | `by which, with which` | 7 |
| per-14-from-the-elder-parapariya.md:213 | `he establishes mindfulness` | `upaṭṭhapetvāna` (line 207) is an absolutive; DPD: abs "having established; having set up" | `having established mindfulness` | 8 |
| per-15-on-protection.md:17 | `the verse of Tāyana` | `gāthāyo` is plural (line 14; DPD gāthā fem "verse"); known 15-02/15-03 touch only the Grammar cell of line 14 | `the verses of Tāyana` | 7 |
| per-15-on-protection.md:56 | `could stir up, should heap up, kick up` | Modal glosses follow the wrong `opt` tag; DPD ākirati 1 (pr): "stirs up; heaps up; kicks up" | `stirs up, heaps up, kicks up` | 8 |
| per-16-miscellaneous-verses.md:136 | `by whichever, with which (woman)` | `yāya` refers to `visattikaṃ` (fem. noun "attachment"), not a woman; DPD yāya = "by whichever; by which; with which", DPD visattikā fem | `by whichever, with which` | 8 |
| per-16-miscellaneous-verses.md:144 | `etaṃ \| pron \| fem.acc.sg \| this, this thing (subject)` | accusative object of `taratha`; gloss says "(subject)" (DPD etaṃ 2 = acc, "this thing (object)") | `this, this thing (object)` | 8 |
| per-16-miscellaneous-verses.md:156 | `Indeed, who has missed the chance sorrows, ended up in hell.` | `socanti` and `samappitā` are plural; translation is singular | `Indeed, those who have missed the chance sorrow, consigned to hell.` | 6 |
| per-16-miscellaneous-verses.md:184 | `piyato \| noun \| masc.abl.sg \| from love, affliction` | DPD piya = dear, beloved (1), love (4); "affliction" is not a meaning of `piya` | `from what is dear, from love` | 8 |
| per-16-miscellaneous-verses.md:187, 190 | `piyato \| noun \| masc.abl.sg \| from love, affliction` | same wrong gloss as line 184 (DPD piya: no "affliction") | `from what is dear, from love` | 8 |
| per-16-miscellaneous-verses.md:197 | `From affliction arises grief, from affliction arises fear. For one who is released from affliction` | `piyato` = from what is dear (DPD piya 1); translation built on the wrong gloss | `From what is dear arises grief, from what is dear arises fear. For one who is released from what is dear` | 8 |
| per-16-miscellaneous-verses.md:103 | `for pierced by an arrow` | missing head noun; reads ungrammatically (DPD sallaviddha = "pierced by an arrow"; translation line 106 has "for those pierced") | `for those pierced by an arrow` | 6 |
| per-17-a-single-excellent-night.md:90 | `ti – \| ind \| \| ”` | English cell holds only a closing quote mark, no gloss (DPD ti 2 "(end of direct speech)"). Known 17-20 touches the Grammar cell of this row, not English | English `”` → `(end of direct speech)` | 7 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:381 | `in with devas, with gods` | garbled gloss (`in with`); DPD sadevaka "with devas; having gods" | `with devas, with gods` | 8 |
| per-19-anupubba-sikkha.md:155 | `**Is it possible to define gradual training` | line 143 is the Buddha's affirmative answer (`sakkā … paññapetuṃ.`, no `nu`; DPD sakkā 1 "it is possible", vs `sakkā nu` "is it possible?"), not a question | `**It is possible to define gradual training, gradual doing, gradual practice in this Teaching and Discipline.**` | 9 |
| per-19-anupubba-sikkha.md:310 | `here in order to divide those people, nor` | first clause renders `imesaṃ bhedāya` (ima "this") as "those people"; both clauses now end "divide those people", though the second is `amūsaṃ bhedāya` (amu "that") | `here in order to divide these people, nor` | 7 |
| per-19-anupubba-sikkha.md:609 | `having one's wings as one's whole burden, just as` | `'va` here is eva "only", not iva "just as" (DPD sapattabhāra "carrying only one's wings"; translation line 612 says "only burden") | `having one's wings as one's only burden` | 8 |
| per-19-anupubba-sikkha.md:221 | `\| nihitadaṇḍo \| adj \| masc.nom.sg \| put down a stick \|` | adjective glossed as a bare verb phrase (DPD nihitadaṇḍa: adj "non-violent") | `who has put down the stick, non-violent` | 6 |
| per-19-anupubba-sikkha.md:222 | `\| nihitasattho \| adj \| masc.nom.sg \| put down a weapon \|` | adjective glossed as a bare verb phrase (DPD nihitasattha: adj "non-violent") | `who has put down the weapon, non-violent` | 6 |
| per-19-anupubba-sikkha.md:712 | `rakkhāhi \| verb \| imp.2.sg \| protects; guards; observes; preserves` | 3rd-person indicative gloss for an imperative | `protect!; guard!; observe!; preserve!` | 7 |
| per-19-anupubba-sikkha.md:874 | `kappeyyāsi \| verb \| opt.2.sg \| could prepare; trim; make` | with sīhaseyyaṃ the sense is "adopt (a posture), lie down" (DPD kappeti 5); 2nd person missing | `you should adopt (a posture), lie down (in); lit. could prepare` | 7 |
| per-19-anupubba-sikkha.md:1171 | `he turned or directed` | past gloss for a present-tense verb (DPD abhininnāmeti: pr, inclines; directs) | `he directs, inclines` | 7 |
| per-19-anupubba-sikkha.md:1025 | `Giving up ill will and malevolence` | same compound rendered "ill will and anger" later in the sentence and in the gloss (line 1019) | `Giving up ill will and anger` | 6 |
| per-19-anupubba-sikkha.md:1048 | `cleansing the mind from restlessness and remorse` | same compound rendered "restlessness and worry" earlier in the sentence | `cleansing the mind from restlessness and worry` | 6 |
| per-19-anupubba-sikkha.md:1203 | `This is effluents'` | ime āsavā is plural (known 19-36 at this line is only the quote-style D8 item) | `These are the effluents'` | 7 |
| per-22-the-noble-eightfold-path.md:248 | `removing greed and depression towards the world` | Same Pāḷi `abhijjhā-domanassaṃ` is "greed and dissatisfaction" in lines 221, 230, 239 and in the gloss (line 219); DPD abhijjhādomanassa allows both ("covetousness and depression; … greed and dist…"), so this is consistency only | `removing greed and dissatisfaction towards the world` | 6 |
| per-23-mindfulness-of-breathing.md:87 | `**Here monk, having gone to the forest` | Chant line 65 has `bhikkhave` (DPD: masc voc pl, monks), not translated; `monk` also lacks its article | `**Here, monks, a monk, having gone to the forest` | 8 |
| per-23-mindfulness-of-breathing.md:204 | `\| sukha- \| noun \| \| pleasure, ease, happiness \|` | The `sukha-paṭisaṃvedī` block (chant line 200) is the only block with no bold translation line after its table | add after the table (wording for owner approval): `**He trains: 'I will breathe in experiencing pleasure.' He trains: 'I will breathe out experiencing pleasure.'**` | 7 |
| per-23-mindfulness-of-breathing.md:261 | `impermanence, unsuitability` | `unsuitability` is not a meaning of `anicca`; DPD anicca 2 (nt): impermanence; inconstancy; instability; irregularity | `impermanence, instability` | 8 |
| per-24-dependent-origination.md:122 | `what is wholesome practice' in that regard?` | puññābhisaṅkhāra rendered "practice" here but "formation" in the table (109) and translations 118, 408; DPD puññābhisaṅkhāra "positive karmic formations" | `wholesome formation` | 8 |
| per-24-dependent-origination.md:140, 144, 152, 156, 168 | `practice` | same drift: `wholesome/unwholesome practice`, `practice of imperturbability` for (a)puñña/āneñja-abhisaṅkhāra (DPD apuññābhisaṅkhāra "negative karmic formations", āneñjābhisaṅkhāra "imperturbable formations") | 140 `wholesome formation`; 144, 152 `unwholesome formation`; 156, 168 `imperturbable formation` | 8 |
| per-24-dependent-origination.md:118 | `bodily formations, verbal formations, mental formation.` | number drift: all six Pāḷi words are singular | `bodily formation, verbal formation, mental formation.` | 5 |
| per-24-dependent-origination.md:236 | `the feeling, perceptions, intention, contact and attention.` | saññā is singular like the rest | `the feeling, perception, intention, contact and attention.` | 5 |
| per-24-dependent-origination.md:284 | `base of mental, mind` | gloss broken: "mental" without a noun (DPD manāyatana "field of the mind; mental sphere") | `mental base, mind` | 5 |
| per-24-dependent-origination.md:357 | `**what is 'clinging', with craving as a condition?**` | `tattha` of chant line 355 ("in that regard", DPD tattha 2) untranslated, unlike all parallel questions | `**what is 'clinging', with craving as a condition, in that regard?**` | 8 |
| per-24-dependent-origination.md:419 | `api \| ind \| \| just, only` | in `sabbam'pi` the sense is "even, also" (DPD api 1.2 "even"), not "just, only" (api 1.1) | `even, also` | 7 |
| per-24-dependent-origination.md:526 | `deterioration of faculties for various beings among the various classes of beings.**` | the chant line 512 ends `ayaṃ vuccati jarā`, which is not translated | append ` This is called aging.` before `**` | 8 |
| per-24-dependent-origination.md:551 | `for various beings from the various classes of beings.**` | the chant line 532 ends `idaṃ vuccati maraṇaṃ`, which is not translated | append ` This is called death.` before `**` | 8 |
| per-26-the-four-great-references.md:56 | `including chiefs, first, excellents, eminents` | Ungrammatical plurals of adjectives; DPD sapāmokkha "with leaders; with eminent monks" | `with leaders, with eminent monks` | 7 |
| per-26-the-four-great-references.md:106 | `bhikkhuno \| noun \| masc.gen.sg \| of monks` | Gloss plural, form singular | `of the monk` | 9 |
| per-26-the-four-great-references.md:143 | `ceva \| ind \| \| only if, if just` | In `na ceva … na` the word is ca + eva (DPD ceva 2 "and even; as well as"), not ce + eva "only if" (DPD ceva 1); line 162 already glosses it so | `and even, as well as; (na ceva … na) neither … nor` | 7 |
| per-26-the-four-great-references.md:183 | `ceva \| ind \| \| only if, if just` | In `sutte ceva … vinaye ca` it reads as ca + eva "both … and" (DPD ceva 2), not ce + eva "only if" (DPD ceva 1); English line 199 "Only if" follows the current gloss | `and even, as well as; (ceva … ca) both … and` | 6 |
| per-26-the-four-great-references.md:210 | `It has been learned well by that monk.` | `imassa` = "of this" (DPD imassa 2; gloss line 205), not "that" | `It has been learned well by this monk.` | 8 |
| per-27-principles-of-cordiality.md:170 | `? (integration)` | "integration" is a wrong word for the interrogative particle (DPD no 1.2 interr); known 27-12 on this line touches the Grammar cell only | `(interrogative)` | 8 |
| per-27-principles-of-cordiality.md:191 | `'This is definitely not, Venerable Sir.'` | Literal rendering of `no h'etaṃ` is not idiomatic English | `'Definitely not, Venerable Sir.'` | 5 |
| per-28-principles-of-non-decline.md:134 | `\| ponobhavikāya \| adj \| fem.gen.sg \| repeated existence, leading to rebirth \|` | adjective glossed with a noun phrase (DPD ponobhavika adj "leading to repeated existence; leading to rebirth") | `leading to repeated existence, leading to rebirth` | 8 |
| per-28-principles-of-non-decline.md:217 | `\| bhikkhū \| noun \| masc.nom.pl \| monks, among monks \|` | nominative subject; "among monks" belongs to `bhikkhūsu` (l. 203) | `monks` | 8 |
| per-28-principles-of-non-decline.md:283 | `**Do not come to a stop midway because of some minor achievement of distinction**` | Pāḷi `na … āpajjissanti` is future, in the "as long as" frame, not an imperative | `**will not come to a stop midway because of some minor achievement of distinction**` | 6 |
| per-29-striving-according-to-the-dhamma.md:161 | `\| paripūreti \| verb \| pr.3.sg \| is swelling, is filling up, is increasing \|` | with `sadatthaṃ` the sense is DPD paripūreti 3 "fulfils; completes" (opposite of `parihāpeti`); current gloss is DPD paripūreti 2 | `fulfils, completes, accomplishes` | 6 |
| per-30-the-buddhas-final-instruction.md:55 | `**Ānanda, whatever Teaching` | `Ānanda` is not in the chant line (l. 36), which omits the vocative | `**Whatever Teaching` | 6 |
| per-32-the-repulsiveness-of-food.md:41 | `yet all this alms food should not be disgusted` | Food cannot "be disgusted"; DPD ajigucchanīya = not disgusting; not repulsive | `**yet all this alms food is not disgusting**` | 7 |
| per-32-the-repulsiveness-of-food.md:55 | `arise those what should be disgusted very much` | Broken English, built on the plural rows 52–53 | `**having reached this putrid body, it becomes extremely disgusting**` | 6 |
| per-39-dhammacakkappavattana-sutta.md:19 | `bārāṇasiyaṃ \| noun \| fem.loc.sg \| in \|` | Gloss truncated to `in` (DPD bārāṇasī fem, name of a city) | English `near Bārāṇasī` | 8 |
| per-39-dhammacakkappavattana-sutta.md:24 | `Thus was heard by me: on one occasion the Fortunate One staying in` | Translation stops mid-sentence; "Thus was heard by me" has no Pāḷi in line 11 | `**On one occasion the Fortunate One was staying near Bārāṇasī, at Isipatana in the Deer Park.**` | 7 |
| per-39-dhammacakkappavattana-sutta.md:63 | `while answer, explanation, exposition` | "while" belongs to the loc. absolute (row 64), not to the noun gloss | `answer, explanation, exposition` | 6 |
| per-39-dhammacakkappavattana-sutta.md:76 | `While this exposition has been preached,` | Translation stops mid-sentence; Koṇḍañña and the Dhamma-eye (line 57) are not translated | `**While this exposition was being preached, there arose in Venerable Koṇḍañña the dust-free, stainless eye of Dhamma.**` | 6 |
| per-40-anatta-lakkhana-sutta.md:70 | `but pr. - may it be,` | Garbled gloss for `ahosī'ti` (DPD `ahosi` aor of hoti; same defect as known D6 at line 122, not listed for 70) | `be (aor. with mā: may it not be)` | 7 |
| per-40-anatta-lakkhana-sutta.md:186 | `? (integration)` | Gloss of `nu` is a typo / placeholder; DPD `nu` ind, interr "(adds a question mark) surely?"; known 40-29 touches only the Grammar cell | `(adds a question mark) surely?` | 8 |
| per-40-anatta-lakkhana-sutta.md:385 | `When liberated, there is understanding 'This is liberated'.` | Line 371 has no such clause; it repeats the translation of line 345 (already at 369) | delete this sentence; start with `He knows clearly:` | 7 |
| per-40-anatta-lakkhana-sutta.md:419 | `While this exposition has been preached` | `bhaññamāne` is a present participle (DPD `bhaññamāna` prp "being spoken"), loc abs: ongoing, past narrative; known 40-46 fixes only `throught` | `While this exposition was being spoken` | 7 |
| per-41-aditta-pariyaya-sutta.md:277 | `While this exposition has been preached` | `bhaññamāne` is a present participle (DPD `bhaññamāna` prp), loc abs; known 41-20 fixes only `throught` | `While this exposition was being spoken` | 7 |
| per-45-culla-mangala-cakka-vala.md:100 | `may completely disappear` | "completely" renders `asesato`, which is in per-43 but not in this chant (line 82 ends `vinassantu ca tejasā`); translation copied from per-43 | `may disappear` | 7 |
| per-49-deva-aradhanai.md:52 | `and may they come from āyāti` | Derivation note inside the gloss | `and may they come` | 6 |
| per-49-deva-aradhanai.md:14 | `\| avikkhitta- \| pp \| \| not scattered, confused \|` | The negation is lost on the second item: reads as "confused" (DPD avikkhitta "not scattered; not confused; not distracted") | `\| avikkhitta- \| pp \| \| not scattered, not confused \|` | 8 |
| per-51-nama-kara-siddhi-gatha.md:23 | `let to go; caused to reach or attain.` | `pāpesi` (DPD pāpeti 1.1 "helps to reach; brings; leads (to)"); "let to go" is wrong English and wrong sense | `led (to); caused to reach or attain.` | 8 |
| per-52-namo-kara-atthaka.md:33 | `\| diṭṭhino \| adj \| masc.dat.sg \| view, belief, opinion, concept, theory, opinion attitude \|` | POS adj but noun gloss (and "opinion" repeated); DPD diṭṭhi 3 adj "with a view; having a belief" | `\| diṭṭhino \| adj \| masc.dat.sg \| with a view, having a belief \|` | 8 |
| per-53-mangala-sutta.md:229 | `patience; wish; forbearance.` | `wish` is the wrong sense of khanti here (DPD khantī: patience; endurance; tolerance) | `patience; endurance; forbearance.` | 7 |
| per-53-mangala-sutta.md:231 | `eloquence, suavity, gentleness (in speech) obedience` | in the Maṅgala context sovacassatā is DPD sovacassatā 2 (docility; obedience; amenability to instruction); `eloquence` is not in DPD, and `suavity; gentleness` is DPD sense 1 | `docility, obedience, amenability to instruction` | 6 |
| per-53-mangala-sutta.md:239 | `gentleness in speech` | translation follows DPD sovacassatā 1 (suavity; gentleness); in this context sense 2 (docility; amenability to instruction) is meant | `amenability to instruction` | 6 |
| per-54-ratana-sutta.md:124 | `\| paṇītaṃ, \| adj \| nt.acc.sg \| excellent; delicious \|` | `delicious` is the food sense (DPD paṇīta 1, of food); here paṇīta 2 (refined; superior; sublime); same word at :90 and :107 glossed `superior, sublime, refined` | `superior, sublime, refined; lit. directed towards` | 7 |
| per-54-ratana-sutta.md:173 | `\| puggalā \| noun \| masc.nom.pl \| an individual; a people \|` | plural form glossed as singular; `a people` is wrong sense (DPD puggala: person; individual) | `individuals; persons` | 8 |
| per-54-ratana-sutta.md:289 | `\| vā'pi \| ind \| \| definitely even \|` | written `vā'pi` = vā + api, `or even` (DPD vāpi 1); the current gloss is DPD vāpi 2 (ve + api), so the reading is a choice | `\| vā'pi \| ind \| \| or even \|` | 5 |
| per-54-ratana-sutta.md:356 | `\| gimhe \| noun \| masc.loc.sg \| in hot \|` | noun glossed as bare adjective (DPD gimha: heat; warmth) | `\| gimhe \| noun \| masc.loc.sg \| in the heat \|` | 7 |
| per-55-karaniya-metta-sutta.md:68 | `not covetous; greedy` | Second gloss drops the negation and says the opposite (DPD anugiddha "greedy"; the word is the negated an-anugiddho) | `not covetous; not greedy` | 8 |
| per-55-karaniya-metta-sutta.md:94 | `because of which wise people might criticize others` | Follows the acc. reading of `pare` (row above); the others who are wise are the ones who criticize | `because of which other wise people might criticize (him)` | 6 |
| per-55-karaniya-metta-sutta.md:260 | `in born; nature as the result of becoming living beings` | Garbled gloss; DPD bhūta 03 "being; living being" (translation line 262 "toward all living beings"). Known 55-23 touches only the Grammar cell of this row | `in living beings, among beings` | 8 |
| per-58-yan-kinci-ratanam-loke.md:78 | `may your fears subside` | Chant line 70 reads `rogā vūpasamentu te` (diseases, gloss line 76; DPD roga "disease"); "fears" is copied from the Dhamma verse (line 68) | `may your diseases subside` | 9 |
| per-61-devata-uyyojana-gatha.md:62 | `May they go the state of deity.` | Mistranslation from the wrong split (rows 59–60); the line sends off the deities who have come | `May the deities who have come (here) depart.` | 6 |
| per-61-devata-uyyojana-gatha.md:77 | `may I bind, tie up` | Tag is `pr.1.sg` (DPD bandhati pr "binds; ties up") but the gloss uses a wish form | `I bind, tie up` | 8 |
| per-61-devata-uyyojana-gatha.md:80 | `By all Buddhas attained the power` | Ungrammatical; balappattā (DPD balappatta adj "come into power") read as a verb; rakkhaṃ is the object of bandhāmi, not "for protection" | `By all the Buddhas who have attained power, by whatever power the solitary Buddhas have, and by the might of the worthy ones, I bind protection in every way.` | 7 |
| per-62-jaya-mangala-attha-gatha.md:131 | `soma- \| noun \| \| ? (nectar)` | Placeholder gloss; translation line 136 renders `soma-vidhinā` as "gracious means". DPD has soma only as masc ("moon"; "soma plant"), no adj "gentle", so the POS stays noun | `soma- \| noun \| \| moon; (here) moon-like, gentle` | 5 |
| per-62-jaya-mangala-attha-gatha.md:215 | `by means of his words of knowledge` | Follows the wrong split gadena "speech" (row 210); DPD agada "medicine; antidote" | `by means of the medicine of knowledge` | 8 |
| per-62-jaya-mangala-attha-gatha.md:233 | `vācano \| noun \| masc.nom.sg \| recitation, reading` | `yo vācano` is "whoever recites" (agent, translation line 248), not "recitation"; DPD vācana 2 adj "reciting; reading" | `vācano \| adj \| masc.nom.sg \| reciting, reading` | 8 |
| per-62-jaya-mangala-attha-gatha.md:236 | `could remember` | The known item 62-17 (D6) fixes the tag to present (sarate); this row is the English cell, whose gloss still uses optative wording (DPD sarati 1.1 "remembers") | `remembers` | 8 |
| per-63-jaya-parittam.md:37 | `may victory and blessing always be for you` | "always" has no Pāḷi word (`hotu te jaya-maṅgalaṃ`) | `may victory and blessing be for you` | 7 |
| per-65-dhamma-sangani-matika.md:40 | `Dhammas having consequence, subject to consequential dhammas` | Second and third items are garbled ("subject to consequential dhammas"); the triad is vipākā / vipāka-dhamma-dhammā / neither. The sense of the first item is for the owner to check: DPD vipāka 2 adj "with result; having consequence" supports the current first item, vipāka 1 masc "result" the reading below | `Dhammas that are results, dhammas productive of results, dhammas neither results nor productive of results.` | 5 |
| per-65-dhamma-sangani-matika.md:72 | `mattā \| adj \| masc.nom.pl \| measured` | In `avitakka-vicāra-mattā` matta means "only, mere" (DPD matta 1.3 "mere; simple"): without thought, with examination only | `mattā \| adj \| masc.nom.pl \| only, mere` | 8 |
| per-65-dhamma-sangani-matika.md:75 | `free from thought but measured examination` | Follows the wrong gloss "measured" (row 72) | `free from thought, with examination only` | 7 |
| per-65-dhamma-sangani-matika.md:96 | `conditioned dhammas abandoned by seeing` | pahātabba-hetukā means "whose roots are to be abandoned" (DPD hetuka "having a cause; with a basis"), not "conditioned … abandoned"; same for the other two items | `dhammas whose roots are to be abandoned by seeing. dhammas whose roots are to be abandoned by development. dhammas whose roots are to be abandoned by neither seeing nor development.` | 6 |
| per-66-vipassana-bhumi-patho.md:18 | `the material form aggregate affected by clinging` | "affected by clinging" (×5) translates upādānakkhandhā (DPD upādāna 2: grasping; clinging); the chant L6 has plain `pañcakkhandhā` / `rūpakkhandho` | drop "affected by clinging" from all five items | 7 |
| per-66-vipassana-bhumi-patho.md:171 | `comes cessation of volitional formations` | Same terms rendered differently from the arising half of this chant (L123/145: formations, mind and body, becoming; here: volitional formations, name-and-form, existence) | at L171–172 use the L123/145 renderings: `volitional formations` → `formations`, `name-and-form` → `mind and body`, `existence` → `becoming` | 5 |
| per-68-adasi-me-adi-gatha.md:51 | `just as relatives persist in that way` | `evaṃ tiṭṭhanti ñātayo` means "yet the relatives keep on so (grieving)"; "just as" reverses the logic | `but the relatives keep on like this` | 5 |
| per-68-adasi-me-adi-gatha.md:67 | `is benefits, is serve, is accrue` | Garbled gloss (DPD upakappati: is beneficial; is good (for)) | `is beneficial, is good (for), serves` | 8 |
| per-68-adasi-me-adi-gatha.md:90 | `engaged (in), pursuing, doing, pursuing` | Wrong sense for `puññaṃ pasutaṃ` (merit produced, translation L93 "merit made"); DPD pasuta 1.4: collected; accumulated (1.1 "engaged (in) … pursuing" is the other word sense); also "pursuing" twice | `collected, accumulated` | 8 |
| per-69-pamsu-kula.md:30 | `having born; arisen, appears` | Garbled gloss for an absolutive (DPD uppajjitvā: having appeared; having arisen) | `having arisen, having appeared` | 8 |
| per-74-the-highest-honour-and-aspirations.md:50 | `may I not have a foolish assembly` | `mā me bāla-samāgamo` means "may I not meet/associate with fools" (DPD bāla 2 masc "fool"; samāgama 2 "association (with)"); bāla- names the people met, not a quality of the assembly | `may I not have association with fools` | 6 |
| pubbakicca-analysis.md:68 | `the consent [of the monks] entitled to give vote by proxy` | chand'ārahānaṃ means "of those entitled to (give) consent" (DPD chandāraha 'entitled to give consent by proxy'); "the consent" (bringing) belongs to chand'āharaṇa (:70). | `[of those] entitled to give consent by proxy` | 8 |
| pubbakicca-analysis.md:159 | `because of the absence of [monks] [who] have left the hand’s reach of the seated monks in this boundary` | Misconstrued: nisinnānaṃ bhikkhūnaṃ are the absent monks themselves (cf. italic :161). | `because of the absence in this boundary of seated monks who have left hand’s reach` | 7 |
| pubbakicca-analysis.md:235 | `eight observance days are remaining` | Chant has the placeholder `[\#] uposathā avasiṭṭhā` (:203); with one arrived and seven passed of eight, "eight remaining" is wrong; italic :237 keeps `\#`. | `[\#] observance days are remaining` | 8 |
| pubbakicca-analysis.md:349 | `Thus, of the opportunities of doing the preliminary duties, because of the opportunity of doing the preliminary duties, with no opportunities to do [those] because of [their] natural state` | Garbled: does not render katattā / pariniṭṭhitattā; italic :351 has the sense. | `Thus, because the preliminary duties that had an opportunity of doing have been done, and because the preliminary duties that had no opportunity of doing are completed by [their] natural state` | 7 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:247 | `(“for the one of devout character”` | DPD *abhivādanasīlī* "habitually respectful; in the habit of being reverential"; "devout" is a different idea; translation line 127 has "respectful" | `(“for the one who is habitually respectful”` | 7 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:111 | `Prosper only fast,` | ungrammatical English for *khippameva samijjhatu* | `Quickly come to pass,` | 6 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:303 | `May suffering, sickness, impediments and animosity,` | *bhaya* = fear (DPD *bhaya 2* nt "fear; terror"), not "impediments" (impediment is *antarāya*, line 307) | `May suffering, sickness, fear and animosity,` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:329 | `(“suffering, sickness, impediments and animosity”` | same gloss error for *bhaya* (DPD *bhaya 2* "fear") | `(“suffering, sickness, fear and animosity”` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:559 | `May suffering, sickness, impediments and animosity,` | `bhaya` is rendered "impediments" (that is `antarāya`, line 563); DPD bhaya 2 nt "fear; terror"; 635 glosses `bhayā` as "fears". | `May suffering, sickness, fear and animosity,` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:669 | `(“suffering, sickness, impediments and animosity”` | `bhaya` is glossed "impediments"; it means "fear" (DPD bhaya 2 nt; cf. 635). | `(“suffering, sickness, fear and animosity”` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:773 | `The supreme Dhamma is realized –` | `vijānataṃ` is "of those who understand" (pres. part. gen. pl. of DPD vijānāti, parallel with `pasannānaṃ`); `dhammaṃ` is its object. The passive "is realized" has no basis in the text. DPD has no entry for the participle form. | `Who understand the supreme Dhamma –` | 6 |

### D. English typos and grammar

| Location | Current | Problem | Suggested | Conf. |
| --- | --- | --- | --- | --- |
| per-01-dedication-of-offerings.md:67 | `we highly worship by these hallowed honour, as is suitable**` | Number disagreement: "these … honour" | `we highly worship by these hallowed honours, as is suitable**` | 7 |
| per-01-dedication-of-offerings.md:81 | `**o lord! it is good for us` | Lower-case sentence start | `**O lord! it is good for us` | 7 |
| per-01-dedication-of-offerings.md:83 | `o lord! it is good for us, even though the Blessed One eventually` | Lower-case sentence start | `O lord! it is good for us, even though the Blessed One eventually` | 7 |
| per-01-dedication-of-offerings.md:108 | `this humble act of veneration that have come to be as a gift**` | Subject-verb disagreement: "act … that have" | `this humble act of veneration that has come to be as a gift**` | 8 |
| per-02-preliminary-homage.md:16 | `homage- paying` | Stray space after hyphen | `homage-paying` | 9 |
| per-02-preliminary-homage.md:21 | `**now let us make preliminary act of veneration to the Buddha` | Missing article | `**now let us make a preliminary act of veneration to the Buddha` | 7 |
| per-03-homage-to-the-buddha.md:23 | `being in such a state such gone or such came` | Run-on list with no separator, and "such came" is ungrammatical | `being in such a state; such gone or such come` | 6 |
| per-03-homage-to-the-buddha.md:43 | `\| deva- \| noun \| \| deity(s), god(s) \|` | Plural of "deity" is "deities" | `deity(ies), god(s)` | 6 |
| per-03-homage-to-the-buddha.md:96 | `whole, altogether, totally, completly` | Typo | `whole, altogether, totally, completely` | 9 |
| per-04-homage-to-the-dhamma.md:21 | `\| yo \| pron \| masc.nom.sg \| which, that … which, \|` | Trailing comma in gloss (per-05:21 has none) | `which, that … which` | 7 |
| per-04-homage-to-the-dhamma.md:27 | `**that which well explained by the Blessed One, the Teaching,**` | Missing verb | `**that which is well explained by the Blessed One, the Teaching,**` | 7 |
| per-06-salutation-to-the-triple-gem.md:309 | `not getting what is desiring is also uncomfortable` | Ungrammatical English. | `not getting what one desires is also uncomfortable` | 7 |
| per-06-salutation-to-the-triple-gem.md:239 | `the explained teaching which leading out` | The verb is missing. | `the explained teaching which is leading out` | 6 |
| per-06-salutation-to-the-triple-gem.md:64 | `respect reverence, honour` | Two glosses run together without a comma. | `respect, reverence, honour` | 8 |
| per-06-salutation-to-the-triple-gem.md:126 | `so-to-speak, known perceived` | Two glosses run together without a comma. | `so-to-speak, known, perceived` | 8 |
| per-06-salutation-to-the-triple-gem.md:147 | `removed given up` | Two glosses run together without a comma. | `removed, given up` | 8 |
| per-06-salutation-to-the-triple-gem.md:186 | `arranged done` | Two glosses run together without a comma. | `arranged, done` | 8 |
| per-06-salutation-to-the-triple-gem.md:217 | `being in such a state such gone or such came` | Two glosses run together without a comma. | `being in such a state, such gone or such came` | 8 |
| per-06-salutation-to-the-triple-gem.md:113, 160 | `respect reverence, honour` | Two glosses run together without a comma (same as line 64). | `respect, reverence, honour` | 8 |
| per-06-salutation-to-the-triple-gem.md:221 | `totally perfectly` | Two glosses run together without a comma. | `totally, perfectly` | 8 |
| per-06-salutation-to-the-triple-gem.md:233 | `salvation salutary, sanctifying, saving profitable` | Two pairs of glosses run together without a comma. | `salvation, salutary, sanctifying, saving, profitable` | 8 |
| per-06-salutation-to-the-triple-gem.md:235 | `extinction liberation` | Two glosses run together without a comma. | `extinction, liberation` | 8 |
| per-06-salutation-to-the-triple-gem.md:282 | `association affiliation` | Two glosses run together without a comma. | `association, affiliation` | 8 |
| per-06-salutation-to-the-triple-gem.md:307, 319, 385, 403, 414, 437, 438, 447 | `unpleasant unsatisfactory` | The same run-together glosses without a comma on these lines; the excerpt is the text on 307 and 319, the other lines read: 385 `sentience knowing`, 403 `fabrications conditional phenomena`, 414 `non-subjective without a soul`, 437 `unease something unsatisfactory`, 438 `distresses dissatisfaction`, 447 `unsatisfactory struck`. | Insert `, `: 307/319 `unpleasant, unsatisfactory`; 385 `sentience, knowing`; 403 `fabrications, conditional phenomena`; 414 `non-subjective, without a soul`; 437 `unease, something unsatisfactory`; 438 `distresses, dissatisfaction`; 447 `unsatisfactory, struck` | 8 |
| per-06-salutation-to-the-triple-gem.md:85 | `which, that which, \|` | The gloss ends with a trailing comma. | `which, that which \|` | 8 |
| per-06-salutation-to-the-triple-gem.md:99 | `which, that which, \|` | The gloss ends with a trailing comma. | `which, that which \|` | 8 |
| per-06-salutation-to-the-triple-gem.md:345 | `of which, \|` | The gloss ends with a trailing comma. | `of which \|` | 8 |
| per-07-the-buddhas-first-exclamation.md:49 | `depletion (of) annihilation (of)` | Two glosses run together without a comma. | `depletion (of), annihilation (of)` | 8 |
| per-08-respect-for-the-dhamma.md:56 | `desiring one's own good lit. wanting self` | Two glosses run together without a comma. | `desiring one's own good, lit. wanting self` | 8 |
| per-08-respect-for-the-dhamma.md:60 | `should be respected. (adj), worthy of esteem.` | A stray POS note `(adj)` and full stops inside the gloss. | `should be respected, worthy of esteem` | 7 |
| per-08-respect-for-the-dhamma.md:86 | `heaven lit. going well` | Two glosses run together without a comma. | `heaven, lit. going well` | 8 |
| per-08-respect-for-the-dhamma.md:88 | `both have not the same result` | Unidiomatic word order. | `do not both have the same result` | 6 |
| per-08-respect-for-the-dhamma.md:100 | `practices the Teaching who walks in truth` | Two glosses run together without a comma. | `practices the Teaching, who walks in truth` | 8 |
| per-08-respect-for-the-dhamma.md:112 | `practices the Teaching who walks in truth` | Two glosses run together without a comma. | `practices the Teaching, who walks in truth` | 8 |
| per-09-going-to-true-and-false-refuges.md:47 | `arriving to this refuge` | Wrong preposition. Known 09-05 on this line touches only `secure ,`. | `arriving at this refuge` | 6 |
| per-09-going-to-true-and-false-refuges.md:108 | `arriving to this refuge` | Wrong preposition. | `arriving at this refuge` | 6 |
| per-10-the-patimokkha-exhortation.md:17 | `undertaking (of) taking up (of)` | Missing comma between glosses (DPD upasampadā 1: "undertaking; taking up (of)") | `undertaking (of), taking up (of)` | 9 |
| per-10-the-patimokkha-exhortation.md:58 | `not insulting, nor abusing` | `nor` without a preceding `neither`; breaks the parallel `not …` list | `not insulting, not abusing` | 7 |
| per-10-the-patimokkha-exhortation.md:62 | `restraint (according to) holding back` | Missing comma between glosses | `restraint (according to), holding back` | 9 |
| per-10-the-patimokkha-exhortation.md:63 | `knowing the correct amount (of) temperance` | Missing comma between glosses | `knowing the correct amount (of), temperance` | 9 |
| per-10-the-patimokkha-exhortation.md:69 | `in mediation` | Typo for `meditation` (cf. translation line 76 "mental development") | `in meditation` | 9 |
| per-11-the-three-characteristics.md:14 | `fabrications formations` | Missing comma between glosses | `fabrications, formations` | 8 |
| per-11-the-three-characteristics.md:42 | `fabrications formations` | Missing comma between glosses | `fabrications, formations` | 8 |
| per-11-the-three-characteristics.md:43 | `unpleasant causing misery` | Missing comma between glosses | `unpleasant, causing misery` | 8 |
| per-11-the-three-characteristics.md:21 | `**all conditioned things are impermanent'` | Lower-case sentence start (the missing opening quote is known item 11-03, policy D8, not this row) | `**All conditioned things are impermanent'` | 6 |
| per-11-the-three-characteristics.md:45 | `**all conditioned things are unsatisfactory'` | Lower-case sentence start (opening quote is known item 11-05, D8) | `**All conditioned things are unsatisfactory'` | 6 |
| per-11-the-three-characteristics.md:58 | `**everything is void of self'` | Lower-case sentence start (opening quote is known item 11-07, D8) | `**Everything is void of self'` | 6 |
| per-11-the-three-characteristics.md:59 | `this is the path to purity**` | Missing full stop (the parallel line 46 has it) | `this is the path to purity.**` | 7 |
| per-11-the-three-characteristics.md:72 | `who going beyond` | Ungrammatical | `who go beyond` | 7 |
| per-11-the-three-characteristics.md:93 | `in Dhamma, \|` | Stray trailing comma in gloss | `in Dhamma \|` | 6 |
| per-11-the-three-characteristics.md:135 | `possession- less` | Broken word | `possessionless` | 8 |
| per-12-the-burdens.md:19 | `picking up (of)the burden` | Missing space | `picking up (of) the burden` | 9 |
| per-12-the-burdens.md:43 | `who's fire is out` | `who's` for `whose` (old row 206 lists only per-01:78 and per-06:470) | `whose fire is out` | 9 |
| per-13-from-the-elder-ratthapala.md:23 | `long lasting lit. standing` | Missing comma before `lit.` | `long lasting, lit. standing` | 7 |
| per-13-from-the-elder-ratthapala.md:45 | `earrings. bone wrapped` | Lower-case sentence start | `earrings. Bone wrapped` | 8 |
| per-13-from-the-elder-ratthapala.md:108 | `they not give` | Ungrammatical | `they do not give` | 7 |
| per-13-from-the-elder-ratthapala.md:215 | `shakes about` | Number disagreement with `they agitate` | `shake about` | 7 |
| per-14-from-the-elder-parapariya.md:15 | `living lit. standing` | Missing comma before `lit.` | `living, lit. standing` | 7 |
| per-14-from-the-elder-parapariya.md:119 | `nearthe foots of trees` | Missing space (known 14-17 fixes `foots` at line 124 only; the rendering of "foots" here is not this row) | `near the foots of trees` | 9 |
| per-14-from-the-elder-parapariya.md:130 | `spreading cultivating` | Missing comma between glosses | `spreading, cultivating` | 8 |
| per-14-from-the-elder-parapariya.md:156 | `un-defiled` | Stray hyphen (translation line 163 has `undefiled`) | `undefiled` | 6 |
| per-14-from-the-elder-parapariya.md:163 | `they subject to beneficial thoughts` | Verb missing | `they were subject to beneficial thoughts` | 7 |
| per-14-from-the-elder-parapariya.md:234 | `could touche` | Typo | `could touch` | 9 |
| per-15-on-protection.md:27 | `persevering persisting` | Missing comma between glosses | `persevering, persisting` | 8 |
| per-15-on-protection.md:45 | `on should do` | Typo | `one should do` | 9 |
| per-15-on-protection.md:51 | `advance towards make an effort` | Missing comma between glosses | `advance towards, make an effort` | 8 |
| per-15-on-protection.md:59 | `Indeed loose wandering monk` | Article missing | `Indeed a loose wandering monk` | 7 |
| per-15-on-protection.md:108 | `dirty stained` | Missing comma between glosses | `dirty, stained` | 8 |
| per-16-miscellaneous-verses.md:18 | `who's support is the Dhamma` | `who's` (who is) for possessive | `whose support is the Dhamma` | 9 |
| per-16-miscellaneous-verses.md:152 | `they sorrow, grief, mourn` | `grief` is a noun; verb gloss needs `grieve` (DPD socati "grieves") | `they sorrow, grieve, mourn` | 8 |
| per-16-miscellaneous-verses.md:37 | `intellect understanding, insight` | missing comma between gloss items | `intellect, understanding, insight` | 8 |
| per-16-miscellaneous-verses.md:74 | `make wither evaporate` | missing comma between gloss items | `make wither, evaporate` | 8 |
| per-16-miscellaneous-verses.md:125 | `under the control of subject to` | missing comma between gloss items | `under the control of, subject to` | 8 |
| per-16-miscellaneous-verses.md:154 | `delivered (to) committed (to)` | missing comma between gloss items (DPD samappita 2 "delivered (to); committed (to)") | `delivered (to), committed (to)` | 8 |
| per-16-miscellaneous-verses.md:168 | `afflicted (with) stricken (by)` | missing comma between gloss items | `afflicted (with), stricken (by)` | 8 |
| per-16-miscellaneous-verses.md:206 | `extinguishing (of a fire) quenching` | missing comma between gloss items (per-18:76 has the comma) | `extinguishing (of a fire), quenching` | 8 |
| per-16-miscellaneous-verses.md:173 | `arrow,spike, dagger` | missing space after comma | `arrow, spike, dagger` | 9 |
| per-17-a-single-excellent-night.md:3 | `**A single Excellent Night**` | title case inconsistent | `**A Single Excellent Night**` | 6 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:3 | `**Setting in Motion The Wheel of Dhamma**` | capital `The` mid-title | `**Setting in Motion the Wheel of Dhamma**` | 5 |
| per-17-a-single-excellent-night.md:18 | `removed given up` | missing comma between gloss items (per-18:308 has it) | `removed, given up` | 8 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:19 | `**Monks there are these two extremes that should not be pursued by one who has gone forth**` | missing vocative comma and final full stop | `**Monks, there are these two extremes that should not be pursued by one who has gone forth.**` | 7 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:104 | `**this is the noble eight-fold path` | sentence starts lower case | `**This is the noble eight-fold path` | 7 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:142 | `**birth is suffering, ageing is suffering` | sentence starts lower case | `**Birth is suffering, ageing is suffering` | 7 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:152 | `**association with the disliked is suffering**` | lower-case start, no full stop | `**Association with the disliked is suffering.**` | 7 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:162 | `**separation from dears is suffering**` | lower-case start, no full stop | `**Separation from the dear is suffering.**` | 7 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:238 | `**just this noble eightfold path` | sentence starts lower case | `**Just this noble eightfold path` | 7 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:149 | `association affiliation, interaction` | missing comma between gloss items | `association, affiliation, interaction` | 8 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:188 | `**In brief the five aggregates of clinging are suffering**` | no full stop | `**In brief, the five aggregates of clinging are suffering.**` | 7 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:205 | `getting pleasure (from) thoroughly enjoying` | missing comma between gloss items | `getting pleasure (from), thoroughly enjoying` | 8 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:255 | `intellect understanding, insight` | missing comma between gloss items | `intellect, understanding, insight` | 8 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:388 | `incomparable (to) superior (to)` | missing comma between gloss items | `incomparable (to), superior (to)` | 8 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:393 | `kings and commoners**` | no full stop at end of translation | `kings and commoners.**` | 7 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:410 | `**Than, I did claim` | `Than` for `Then` | `**Then, I did claim` | 9 |
| per-19-anupubba-sikkha.md:131 | `? (integation)` | typo | `? (interrogation)` | 9 |
| per-19-anupubba-sikkha.md:254 | `unchasity, uncelibacy` | typo | `unchastity, uncelibacy` | 9 |
| per-19-anupubba-sikkha.md:153 | `to regulates or make a rule; makes known; declares; prepares, define` | mixed infinitive and 3sg forms; "to regulates" ungrammatical | `to regulate or make a rule; to make known; to declare; to prepare; to define` | 8 |
| per-19-anupubba-sikkha.md:192 | `train yourself in according to them` | stray "in" | `train yourself according to them` | 8 |
| per-19-anupubba-sikkha.md:72 | `renunciation is an open air` | wrong article | `renunciation is the open air` | 7 |
| per-19-anupubba-sikkha.md:359 | `he is speaker of such words` | missing article | `he is a speaker of such words` | 7 |
| per-19-anupubba-sikkha.md:383 | `speaks what is beneficial, who speaks according to the Teaching and the Discipline` | relative "who" breaks the parallel list | `speaks what is beneficial, speaks according to the Teaching and the Discipline` | 7 |
| per-19-anupubba-sikkha.md:44 | `obtaining (of) gaining (of)` | missing comma between glosses | `obtaining (of), gaining (of)` | 8 |
| per-19-anupubba-sikkha.md:83 | `having clothed oneself (in) having put on` | missing comma between glosses | `having clothed oneself (in), having put on` | 8 |
| per-19-anupubba-sikkha.md:116 | `having clothed oneself (in) having put on` | missing comma between glosses | `having clothed oneself (in), having put on` | 8 |
| per-19-anupubba-sikkha.md:119 | `renounces the household life goes forth` | missing comma between glosses (line 86 has it) | `renounces the household life, goes forth` | 8 |
| per-19-anupubba-sikkha.md:224 | `full of kindness lit. accomplished in kindness` | missing comma before `lit.` | `full of kindness, lit. accomplished in kindness` | 8 |
| per-19-anupubba-sikkha.md:290 | `slanderous backbiting` | missing comma (line 287 has it) | `slanderous, backbiting` | 8 |
| per-19-anupubba-sikkha.md:324 | `who is fond of concord who likes harmony` | missing comma between glosses | `who is fond of concord, who likes harmony` | 8 |
| per-19-anupubba-sikkha.md:187 | `one, realising the danger` | stray comma | `one realising the danger` | 6 |
| per-19-anupubba-sikkha.md:168 | `disciplines him like this**` | translation lacks final punctuation before the quoted speech | `disciplines him like this:**` | 7 |
| per-19-anupubba-sikkha.md:215 | `he abstains from killing living beings**` | missing full stop | `he abstains from killing living beings.**` | 7 |
| per-19-anupubba-sikkha.md:612 | `flies with its wings as its only burden**` | missing punctuation; the sentence continues at line 627 (`so too, …`) | `flies with its wings as its only burden,**` | 6 |
| per-19-anupubba-sikkha.md:627 | `with almsfood to maintain his stomach**` | missing final punctuation; the sentence continues in lower case at line 639 (`and wherever he goes …`), as line 627 itself continues line 612 | `with almsfood to maintain his stomach,**` | 6 |
| per-19-anupubba-sikkha.md:704 | `follow a course of action follow a method` | missing separator between glosses | `follow a course of action, follow a method` | 8 |
| per-19-anupubba-sikkha.md:792 | `decoration beautification` | missing separator | `decoration, beautification` | 8 |
| per-19-anupubba-sikkha.md:806 | `will put an end to will terminate` | missing separator | `will put an end to, will terminate` | 8 |
| per-19-anupubba-sikkha.md:810 | `support of life way of going on` | missing separator | `support of life, way of going on` | 8 |
| per-19-anupubba-sikkha.md:829 | `practising given to` | missing separator | `practising, given to` | 8 |
| per-19-anupubba-sikkha.md:994 | `having set up having made sure is present` | missing separator (English cell; known 19-28 touches only POS/Grammar) | `having set up, having made sure is present` | 8 |
| per-19-anupubba-sikkha.md:1101 | `removed given up` | missing separator | `removed, given up` | 8 |
| per-19-anupubba-sikkha.md:1159 | `immovable steadfast` | missing separator | `immovable, steadfast` | 8 |
| per-19-anupubba-sikkha.md:716 | `brings into being, make happened` | verb forms wrong | `bring into being, make happen` | 8 |
| per-19-anupubba-sikkha.md:801 | `brahmacariya- \| noun \| nt \| holy live` | typo (known 19-25 fixes only the translation at 817) | `holy life` | 9 |
| per-19-anupubba-sikkha.md:817 | `thus (should think) :` | lower-case sentence start after full stop; space before colon (known 19-25 fixes other phrases in this line) | `Thus (should think):` | 7 |
| per-19-anupubba-sikkha.md:944 | `nisinne \| noun \| nt.loc.sg \| in seating` | wrong word | `in sitting` | 7 |
| per-19-anupubba-sikkha.md:1152 | `when mind, when mind` | duplicated gloss | `when mind` | 8 |
| per-19-anupubba-sikkha.md:1128 | `impurities; defilements;` | trailing semicolon | `impurities; defilements` | 8 |
| per-19-anupubba-sikkha.md:1140 | `lives; abides; dwells;` | trailing semicolon | `lives; abides; dwells` | 8 |
| per-19-anupubba-sikkha.md:687 | `appearances or details**` | translation sentence lacks final full stop | `appearances or details.**` | 7 |
| per-19-anupubba-sikkha.md:706 | `restraint of that**` | missing final full stop | `restraint of that.**` | 7 |
| per-19-anupubba-sikkha.md:752 | `appearances or details**` | missing final full stop | `appearances or details.**` | 7 |
| per-19-anupubba-sikkha.md:760 | `restraint of that**` | missing final full stop | `restraint of that.**` | 7 |
| per-19-anupubba-sikkha.md:846 | `mental states**` | missing final full stop | `mental states.**` | 7 |
| per-19-anupubba-sikkha.md:783, 862, 883, 900, 927, 996, 1013, 1025, 1037, 1048, 1060, 1087, 1173 | `**` | translation sentences lack a final full stop | add `.` before the closing `**` | 7 |
| per-22-the-noble-eightfold-path.md:43 | `source of unsatisfactory` | Adjective used as a noun | `source of unsatisfactoriness` | 6 |
| per-20-requisites-for-awakening.md:74 | `four basis for psychic power` | Singular for plural | `four bases for psychic power` | 8 |
| per-20-requisites-for-awakening.md:48 | `for the benefit of mass of people` | Missing article | `for the benefit of the mass of people` | 7 |
| per-21-the-seven-factors-of-awakening.md:21 | `for who does that` | Missing antecedent | `for one who does that` | 6 |
| per-22-the-noble-eightfold-path.md:147 | `begins, starts, undertaking, arouses` | `undertaking` breaks the finite-verb series | `begins, starts, undertakes, arouses` | 8 |
| per-22-the-noble-eightfold-path.md:68 | `intention, volition, thought,` | Trailing comma in the gloss (lines 66, 70 have none) | `intention, volition, thought` | 8 |
| per-22-the-noble-eightfold-path.md:126 | `Here disciple of the noble ones` | Missing article | `Here a disciple of the noble ones` | 6 |
| per-22-the-noble-eightfold-path.md:280 | `monk separating oneself from sensual pleasures` | Missing article; `oneself` does not agree with `monk` | `a monk, separating himself from sensual pleasures` | 6 |
| per-22-the-noble-eightfold-path.md:371 | `as from earlier disappearance satisfaction and dissatisfaction` | Missing `of`; garbled connective (known 22-36 on this line covers only `he attaining and remains`) | `and from the earlier disappearance of satisfaction and dissatisfaction` | 6 |
| per-20-requisites-for-awakening.md:60 | `setting up attention foundations of mindfulness` | Two glosses run together without a separator | `setting up attention, foundations of mindfulness` | 7 |
| per-20-requisites-for-awakening.md:71 | `eight-fold having eight constituents` | Two glosses run together without a separator | `eight-fold, having eight constituents` | 7 |
| per-21-the-seven-factors-of-awakening.md:16 | `devoted oneself to lit. made much of` | Missing separator before `lit.` | `devoted oneself to, lit. made much of` | 7 |
| per-21-the-seven-factors-of-awakening.md:19 | `leading to deliverance lit. leading out` | Missing separator before `lit.` | `leading to deliverance, lit. leading out` | 7 |
| per-21-the-seven-factors-of-awakening.md:111 | `rethinks reconsiders` | Two glosses run together without a separator | `rethinks, reconsiders` | 7 |
| per-21-the-seven-factors-of-awakening.md:61 | `attending (to) lit. sitting around near` | Missing separator before `lit.` | `attending (to), lit. sitting around near` | 7 |
| per-21-the-seven-factors-of-awakening.md:129 | `engages in brings into being` | Two glosses run together without a separator | `engages in, brings into being` | 7 |
| per-21-the-seven-factors-of-awakening.md:144 | `producing bringing into being` | Two glosses run together without a separator | `producing, bringing into being` | 7 |
| per-21-the-seven-factors-of-awakening.md:156 | `with energy aroused (to) applying energy (to)` | Two glosses run together without a separator | `with energy aroused (to), applying energy (to)` | 7 |
| per-21-the-seven-factors-of-awakening.md:159 | `non-physical lit. not fleshly` | Missing separator before `lit.` | `non-physical, lit. not fleshly` | 7 |
| per-21-the-seven-factors-of-awakening.md:167; per-22-the-noble-eightfold-path.md:41, 145, 149, 150, 191, 214, 219, 302, 306, 355, 358, 360, 362 | `thrilled lit. enraptured mind` | Same defect on each listed line: two glosses (or a gloss and `lit.`) run together without a separator. Pairs: 21:167 `thrilled lit.`; 22:41 `unease something`, 145 `strives for exerts`, 149 `goes for it endeavours`, 150 `oneself lit.`, 191 `culmination maturity`, 214 `attentive knowing`, 219 `distress dissatisfaction`, 302 `subsiding settling`, 306 `unification lit.`, 355/358 `removal abandoning`, 360 `displeasure satisfaction`, 362 `pleasant neither` | insert `, ` between the two parts in each listed pair (e.g. `thrilled, lit. enraptured mind`) | 7 |
| per-21-the-seven-factors-of-awakening.md:71 | `**even listening to (them)` | Translation sentence starts lower-case | `**Even listening to (them)` | 6 |
| per-21-the-seven-factors-of-awakening.md:81 | `**what's the reason for that? why is that?**` | Lower-case sentence starts | `**What's the reason for that? Why is that?**` | 6 |
| per-22-the-noble-eightfold-path.md:27 | `**this is the noble eightfold path, as follows` | Lower-case sentence start | `**This is the noble eightfold path, as follows` | 6 |
| per-22-the-noble-eightfold-path.md:197 | `**this monks is called right effort**` | Lower-case sentence start | `**This monks is called right effort**` | 6 |
| per-22-the-noble-eightfold-path.md:201 | `**and what monks is right mindfulness?**` | Lower-case sentence start | `**And what monks is right mindfulness?**` | 6 |
| per-22-the-noble-eightfold-path.md:252 | `**this moks is called right mindfulness**` | Lower-case sentence start (known 22-19 on this line covers only `moks` → `monks`) | `**This moks is called right mindfulness**` (capital only) | 6 |
| per-22-the-noble-eightfold-path.md:264 | `**and what monks is right stability of mind?**` | Lower-case sentence start | `**And what monks is right stability of mind?**` | 6 |
| per-22-the-noble-eightfold-path.md:295 | `**he attaining and remains` | Lower-case sentence start (known 22-23 on this line covers only `attaining` → `attains`) | `**He attaining and remains` (capital only) | 6 |
| per-22-the-noble-eightfold-path.md:375 | `**this monks is called right stability of mind**` | Lower-case sentence start | `**This monks is called right stability of mind**` | 6 |
| per-22-the-noble-eightfold-path.md:379 | `**this is the noble eightfold path**` | Lower-case sentence start | `**This is the noble eightfold path**` | 6 |
| per-23-mindfulness-of-breathing.md:138 | `short, shortly or` | Stray `or` at the end of the gloss (the next row is `vā \| or`); compare line 127 `short, shortly` | `short, shortly` | 9 |
| per-23-mindfulness-of-breathing.md:12 | `attention to in and out breathing mindfulness of inhalation and exhalation` | Two glosses run together without a separator | `attention to in and out breathing; mindfulness of inhalation and exhalation` | 8 |
| per-23-mindfulness-of-breathing.md:25 | `attention to in and out breathing mindfulness of inhalation and exhalation` | Two glosses run together without a separator | `attention to in and out breathing; mindfulness of inhalation and exhalation` | 8 |
| per-23-mindfulness-of-breathing.md:297 | `attention to in and out breathing mindfulness of inhalation and exhalation` | Two glosses run together without a separator | `attention to in and out breathing; mindfulness of inhalation and exhalation` | 8 |
| per-23-mindfulness-of-breathing.md:41 | `devoted oneself to lit. made much of` | Missing comma before `lit.` (lines 14, 27, 299 have it) | `devoted oneself to, lit. made much of` | 9 |
| per-23-mindfulness-of-breathing.md:85 | `having set up having made sure is present` | Two glosses run together without a comma (DPD upaṭṭhapetvā 1 gives them as separate meanings); known 23-03 touches the POS/Grammar cells of this line, not the gloss | `having set up, having made sure is present` | 8 |
| per-23-mindfulness-of-breathing.md:175 | `formation intention` | Two glosses run together without a comma | `formation, intention` | 8 |
| per-23-mindfulness-of-breathing.md:185 | `formation intention` | Two glosses run together without a comma | `formation, intention` | 8 |
| per-23-mindfulness-of-breathing.md:237 | `making please` | Ungrammatical gloss | `making pleased` | 7 |
| per-23-mindfulness-of-breathing.md:262 | `one who contemplates. \|` | Stray full stop at the end of a gloss cell | `one who contemplates \|` | 8 |
| per-23-mindfulness-of-breathing.md:63 | `**And how monks mindfulness of inhalation and exhalation is developed? How practised often it is of great fruit and great benefit?**` | Questions written in statement word order; vocative `monks` not set off | `**And how, monks, is mindfulness of inhalation and exhalation developed? How practised often is it of great fruit and great benefit?**` | 7 |
| per-23-mindfulness-of-breathing.md:32 | `four foundations of mindfulness**` | Translation sentence has no closing full stop (known 23-01 fixes `it is fills up` in the same line, not the full stop) | `four foundations of mindfulness.**` | 8 |
| per-23-mindfulness-of-breathing.md:87 | `in front of hiṃ**` | Translation sentence has no closing full stop (the `hiṃ` fix is known 23-04) | `in front of him.**` | 8 |
| per-23-mindfulness-of-breathing.md:280 | `observing cessation**` | Missing full stop at the end of the translation (quote balance is policy D8) | `observing cessation.**` | 8 |
| per-23-mindfulness-of-breathing.md:46 | `**four foundations of mindfulness, (when)` | Translation sentence starts lower-case | `**Four foundations of mindfulness, (when)` | 8 |
| per-23-mindfulness-of-breathing.md:55 | `**seven factors of awakening, (when)` | Translation sentence starts lower-case | `**Seven factors of awakening, (when)` | 8 |
| per-23-mindfulness-of-breathing.md:99 | `**just mindful, he breathes in` | Translation sentence starts lower-case | `**Just mindful, he breathes in` | 8 |
| per-23-mindfulness-of-breathing.md:110 | `**breathing in deeply he knows clearly` | Translation sentence starts lower-case (known 23-06 fixes `I'm breath` in the same line, not the capital) | `**Breathing in deeply he knows clearly` | 8 |
| per-23-mindfulness-of-breathing.md:121 | `**or breathing out deeply` | Translation sentence starts lower-case (known 23-08 is another defect in this line) | `**Or breathing out deeply` | 8 |
| per-23-mindfulness-of-breathing.md:134, 145 | `**or breathing` | Translation sentences start lower-case (same as lines 110, 121) | `**Or breathing` | 8 |
| per-23-mindfulness-of-breathing.md:157, 167, 179, 189 | `**he trains` | Translation sentences start lower-case (lines 198 onward use `He trains`); known D8 items at these lines are quote style only | `**He trains` | 8 |
| per-24-dependent-origination.md:315 | `'feeling',with` | missing space after comma | `'feeling', with` | 9 |
| per-24-dependent-origination.md:322 | `produced by from auditory impression` | doubled preposition | `produced by auditory impression` | 9 |
| per-24-dependent-origination.md:366 | `self- concept` | stray space in hyphenated word | `self-concept` | 9 |
| per-24-dependent-origination.md:517 | `deterioriation` | typo | `deterioration` | 9 |
| per-24-dependent-origination.md:551 | `power of life of for various beings` | stray `of` | `power of life for various beings` | 9 |
| per-24-dependent-origination.md:715 | `fitting togethe lit.` | typo and missing comma | `fitting together, lit.` | 9 |
| per-24-dependent-origination.md:442 | `non perception, non conception` | missing hyphens (cf. `non-perception` line 456) | `non-perception, non-conception` | 6 |
| per-24-dependent-origination.md:426 | `all action(s) that leads to existence` | verb agreement with optional plural | `all action that leads to existence` | 5 |
| per-24-dependent-origination.md:148 | `**unskillful intentions belonging to the sphere of sensual experience**` | missing full stop | `**unskillful intentions belonging to the sphere of sensual experience.**` | 8 |
| per-24-dependent-origination.md:368 | `clinging to a self-concept**` | missing full stop | `clinging to a self-concept.**` | 8 |
| per-24-dependent-origination.md:408 | `imperturbable formation**` | missing full stop | `imperturbable formation.**` | 8 |
| per-24-dependent-origination.md:21 | `six (internal sense) bases six sense organs` | separator lost between gloss items | `six (internal sense) bases, six sense organs` | 7 |
| per-24-dependent-origination.md:78 | `unease something unsatisfactory` | separator lost between gloss items | `unease, something unsatisfactory` | 7 |
| per-24-dependent-origination.md:195 | `auditory awareness hearing` | separator lost between gloss items | `auditory awareness, hearing` | 7 |
| per-24-dependent-origination.md:196 | `olfactory awareness smelling` | separator lost between gloss items | `olfactory awareness, smelling` | 7 |
| per-24-dependent-origination.md:197 | `gustatory awareness tasting` | separator lost between gloss items | `gustatory awareness, tasting` | 7 |
| per-24-dependent-origination.md:199 | `mental awareness thinking` | separator lost between gloss items | `mental awareness, thinking` | 7 |
| per-24-dependent-origination.md:253 | `earth water fire wind lit. great element` | separator lost before `lit.` (cf. `mind, lit. name` line 216) | `earth water fire wind, lit. great element` | 7 |
| per-24-dependent-origination.md:254 | `dependent (on) lit. grasping (onto)` | separator lost before `lit.` | `dependent (on), lit. grasping (onto)` | 7 |
| per-24-dependent-origination.md:437 | `sense desire sensual sphere becoming` | separator lost between gloss items | `sense desire, sensual sphere becoming` | 7 |
| per-24-dependent-origination.md:487 | `(into a womb) lit. descent` | separator lost before `lit.` | `(into a womb), lit. descent` | 7 |
| per-24-dependent-origination.md:492, 547, 549, 585, 589, 591, 615, 616, 642, 646, 670 | `obtaining (of) gaining (of)`; `putting down throwing away (of)`; `breaking off complete stopping (of)`; `painful experience state of suffering`; `state of sorrow state of sadness`; `severe personal sadness severe heartache`; `wailing crying, bewailing`; `wailing crying etc`; `unease something unsatisfactory`; `impression lit. sensed`; `unease something unsatisfactory` | same lost separator in the English gloss (remaining lines, in the order cited) | insert `, ` at each join: `obtaining (of), gaining (of)`; `putting down, throwing away (of)`; `breaking off, complete stopping (of)`; `painful experience, state of suffering`; `state of sorrow, state of sadness`; `severe personal sadness, severe heartache`; `wailing, crying, bewailing`; `wailing, crying etc`; `unease, something unsatisfactory`; `impression, lit. sensed`; `unease, something unsatisfactory` | 7 |
| per-25-the-dhamma-in-brief.md:19 | `saluted, greeted,` | Trailing comma at end of gloss | `having paid homage, saluted, greeted` | 8 |
| per-25-the-dhamma-in-brief.md:30 | `Mahāpajāpatī gotamī where` | Proper name lower case in the English (known 25-01 on this line is only `Bhessed`) | `Mahāpajāpatī Gotamī where` | 8 |
| per-25-the-dhamma-in-brief.md:56 | `Venerable Sir, It would be good` | Capital letter after a comma | `Venerable Sir, it would be good` | 8 |
| per-25-the-dhamma-in-brief.md:79 | `they are lead (to)` | "are lead" is ungrammatical | `they lead (to)` | 9 |
| per-25-the-dhamma-in-brief.md:90 | `they are lead (to)` | "are lead" is ungrammatical | `they lead (to)` | 9 |
| per-25-the-dhamma-in-brief.md:101 | `they are lead (to)` | "are lead" is ungrammatical | `they lead (to)` | 9 |
| per-25-the-dhamma-in-brief.md:112 | `they are lead (to)` | "are lead" is ungrammatical | `they lead (to)` | 9 |
| per-25-the-dhamma-in-brief.md:123 | `are lead (to)` | "are lead" is ungrammatical | `they lead (to)` | 9 |
| per-25-the-dhamma-in-brief.md:134, 145, 156 | `are lead (to)` | Same defect on the remaining lines | `they lead (to)` | 9 |
| per-25-the-dhamma-in-brief.md:169 | `could keep in mind remember` | Missing comma between glosses | `could keep in mind, remember` | 8 |
| per-25-the-dhamma-in-brief.md:175 | `Teacher's message Teacher's Doctrine` | Missing comma; stray capital D (line per-26:42 has lower case) | `Teacher's message, Teacher's doctrine` | 8 |
| per-26-the-four-great-references.md:42 | `Teacher's message Teacher's doctrine` | Missing comma between glosses | `Teacher's message, Teacher's doctrine` | 8 |
| per-26-the-four-great-references.md:17 | `statements references` | Missing comma between glosses | `statements, references` | 8 |
| per-26-the-four-great-references.md:19 | `What monks are the four great references?` | Vocative not set off by commas | `What, monks, are the four great references?` | 7 |
| per-26-the-four-great-references.md:79 | `to whom scriptures has been arrived` | Subject–verb agreement; "arrived" unidiomatic | `to whom the scriptures have come down` | 8 |
| per-26-the-four-great-references.md:91 | `Who knowledgeable` | Sentence fragment with no verb | `They are knowledgeable` | 8 |
| per-26-the-four-great-references.md:91 | `In the presence of that elders` | Singular demonstrative with plural noun (known 26-04 on this line is only `certan`/`heared`) | `In the presence of those elders` | 9 |
| per-26-the-four-great-references.md:95 | `Who knowledgeable` | Sentence fragment with no verb | `He is knowledgeable` | 8 |
| per-26-the-four-great-references.md:109 | `should be approved of applauded` | Missing comma between glosses | `should be approved of, applauded` | 8 |
| per-26-the-four-great-references.md:113 | `Statement of that monk neither should be approved nor should be rejected.` | Missing article; misplaced "neither" | `The statement of that monk should be neither approved nor rejected.` | 7 |
| per-26-the-four-great-references.md:139 | `being causing to go into` | Ungrammatical passive | `being caused to go into` | 8 |
| per-26-the-four-great-references.md:145 | `flow down fit` | Missing comma between glosses | `flow down, fit` | 8 |
| per-26-the-four-great-references.md:148 | `are agree with` | Ungrammatical | `agree with` | 9 |
| per-26-the-four-great-references.md:153 | `does not fit to the discourses, does not agree with discipline` | Subject–verb agreement with plural "those (statements)"; "fit to" | `do not fit the discourses, do not agree with discipline` | 8 |
| per-26-the-four-great-references.md:171 | `taken in the wrong wayincorrectly understood,` | Duplicated gloss run together without space | `incorrectly understood, poorly grasped, taken in the wrong way` | 9 |
| per-26-the-four-great-references.md:184 | `flow down fit` | Missing comma between glosses | `flow down, fit` | 8 |
| per-26-the-four-great-references.md:187 | `are agree with` | Ungrammatical | `agree with` | 9 |
| per-26-the-four-great-references.md:199 | `are fit the discourses` | Ungrammatical | `fit the discourses` | 8 |
| per-26-the-four-great-references.md:199 | `this is the words of the Blessed One` | Number agreement; line 176 has "the word" | `this is the word of the Blessed One` | 8 |
| per-27-principles-of-cordiality.md:13 | `Fortunate One Buddha` | Missing comma between glosses | `Fortunate One, Buddha` | 8 |
| per-27-principles-of-cordiality.md:46 | `that making friendship and respect, and conduce to collaboration` | No finite verb in the first clause | `that create affection and respect, and conduce to collaboration` | 7 |
| per-27-principles-of-cordiality.md:50 | `what are the six?` | Sentence starts lower case | `What are the six?` | 8 |
| per-27-principles-of-cordiality.md:87 | `with virtuous, ethical, moral,` | Trailing comma at end of gloss | `with virtuous, ethical, moral` | 8 |
| per-27-principles-of-cordiality.md:94 | `he does not using without sharing, but using in common` | Wrong verb forms | `he does not use without sharing, but uses in common` | 8 |
| per-27-principles-of-cordiality.md:121 | `Monk dwells both` | Missing article | `A monk dwells both` | 7 |
| per-27-principles-of-cordiality.md:129 | `theory, opinion attitude` | Duplicated "opinion" and missing comma (known 27-09 covers line 138 only) | `theory, attitude` | 8 |
| per-27-principles-of-cordiality.md:137 | `theory opinion, attitude` | Duplicated "opinion" and missing comma in the `diṭṭhiyā` row (known 27-09 covers the `diṭṭhi-` row, line 138, only) | `theory, attitude` | 8 |
| per-27-principles-of-cordiality.md:144 | `Monk dwells both` | Missing article | `A monk dwells both` | 7 |
| per-27-principles-of-cordiality.md:149 | `that making friendship and respect, and conduce to collaboration` | No finite verb in the first clause | `that create affection and respect, and conduce to collaboration` | 7 |
| per-27-principles-of-cordiality.md:161 | `go forward practice` | Missing comma between glosses | `go forward, practice` | 8 |
| per-28-principles-of-non-decline.md:111 | `will respects; reveres.` | verb agreement; inconsistent with other glosses | `will respect; revere` | 8 |
| per-28-principles-of-non-decline.md:119 | `those monks - who senior,` | missing verb | `those monks - who are senior,` | 7 |
| per-28-principles-of-non-decline.md:139 | `which leading to rebirth` | ungrammatical | `which leads to rebirth` | 8 |
| per-28-principles-of-non-decline.md:202 | `\| dhammā \| noun \| masc.nom.pl \| principles, law \|` | plural form glossed `law`; l. 16 has `principles, laws` | `principles, laws` | 6 |
| per-28-principles-of-non-decline.md:216 | `\| dhammesu \| noun \| masc.loc.pl \| in principles, law \|` | plural glossed `law` | `in principles, laws` | 6 |
| per-28-principles-of-non-decline.md:314 | `enjoyment of non- manifoldness` | stray space after hyphen | `enjoyment of non-manifoldness` | 9 |
| per-28-principles-of-non-decline.md:15, 201 | `deterioration, decrease decline` | missing comma between gloss items (same text on both lines) | `deterioration, decrease, decline` | 7 |
| per-28-principles-of-non-decline.md:57 | `withdraw (from) emerge (from)` | missing comma between gloss items | `withdraw (from), emerge (from)` | 7 |
| per-28-principles-of-non-decline.md:177, 182 | `well-behaved amiable` | missing comma between gloss items (same text on both lines) | `well-behaved, amiable` | 7 |
| per-29-striving-according-to-the-dhamma.md:112 | `mixed up full of` | missing comma between gloss items | `mixed up, full of` | 7 |
| per-29-striving-according-to-the-dhamma.md:312; per-30-the-buddhas-final-instruction.md:72 | `caution, vigilance diligence` | missing comma between gloss items (same text in both files) | `caution, vigilance, diligence` | 7 |
| per-28-principles-of-non-decline.md:76 | `not decreed not declared` | missing comma between gloss items | `not decreed, not declared` | 7 |
| per-28-principles-of-non-decline.md:215 | `deterioration decrease, decline` | missing comma between gloss items | `deterioration, decrease, decline` | 7 |
| per-28-principles-of-non-decline.md:218 | `engaged in agree with` | missing comma between gloss items | `engaged in, agree with` | 7 |
| per-28-principles-of-non-decline.md:264; per-29-striving-according-to-the-dhamma.md:134 | `applying energy making an effort` | missing comma between gloss items (same text in both files) | `applying energy, making an effort` | 7 |
| per-29-striving-according-to-the-dhamma.md:29 | `a rag a bandage` | missing comma between gloss items | `a rag, a bandage` | 7 |
| per-29-striving-according-to-the-dhamma.md:101 | `unease unsatisfaction` | missing comma between gloss items | `unease, unsatisfaction` | 7 |
| per-29-striving-according-to-the-dhamma.md:263 | `with result with coming forth` | missing comma between gloss items | `with result, with coming forth` | 7 |
| per-29-striving-according-to-the-dhamma.md:276; per-31-the-four-requisites.md:79 | `lodging lit. bed and chair` | missing comma before `lit.` (cf. `alms round, lit. lump dropping`, per-29:275) | `lodging, lit. bed and chair` | 7 |
| per-29-striving-according-to-the-dhamma.md:299 | `should be practised should be trained` | missing comma between gloss items | `should be practised, should be trained` | 7 |
| per-29-striving-according-to-the-dhamma.md:305 | `personal benefit personal profit` | missing comma between gloss items | `personal benefit, personal profit` | 7 |
| per-31-the-four-requisites.md:46 | `decoration beautification` | missing comma between gloss items | `decoration, beautification` | 7 |
| per-31-the-four-requisites.md:60 | `will put an end to will terminate` | missing comma between gloss items | `will put an end to, will terminate` | 7 |
| per-31-the-four-requisites.md:64 | `support of life way of going on` | missing comma between gloss items | `support of life, way of going on` | 7 |
| per-29-striving-according-to-the-dhamma.md:258 | `going forth' \|` | stray apostrophe | `going forth \|` | 9 |
| per-29-striving-according-to-the-dhamma.md:19 | `the Teaching thus been well preached by me` | missing auxiliary | `the Teaching has thus been well preached by me` | 8 |
| per-29-striving-according-to-the-dhamma.md:45 | `\| ārabhituṃ \| verb \| inf \| to arose, to begin, start \|` | `arose` is past tense of arise; known row 29-01 fixes only l. 47 | `to arouse, to begin, start` | 9 |
| per-29-striving-according-to-the-dhamma.md:60 | `let left over; may remain over` | missing verb | `let be left over; may remain over` | 7 |
| per-29-striving-according-to-the-dhamma.md:95 | `will be not stilling of effort` | ungrammatical | `there will be no stilling of effort` | 7 |
| per-29-striving-according-to-the-dhamma.md:139 | `lives; abides; dwells; \|` | trailing semicolon | `lives; abides; dwells \|` | 7 |
| per-29-striving-according-to-the-dhamma.md:239 | `for the achievement of unachieved` | missing article | `for the achievement of the unachieved` | 7 |
| per-29-striving-according-to-the-dhamma.md:313 | `to presse on, cause to accomplish, strive to achieve, trie to accomplish` | typos `presse`, `trie` | `to press on, cause to accomplish, strive to achieve, try to accomplish` | 9 |
| per-30-the-buddhas-final-instruction.md:68 | `I addresse, speak (to)` | typo | `I address, speak (to)` | 9 |
| per-30-the-buddhas-final-instruction.md:73 | `you presse on, cause to accomplish, strive to achieve, trie to accomplish` | typos `presse`, `trie` | `you press on, cause to accomplish, strive to achieve, try to accomplish` | 9 |
| per-31-the-four-requisites.md:55 | `\| brahmacariya- \| noun \| nt \| holy live \|` | typo; known row 31-11 fixes only l. 71 | `holy life` | 9 |
| per-31-the-four-requisites.md:42 | `\| paṭisevāmi \| verb \| pr.1.sg \| uses, makes use (of) \|` | 3rd-person gloss for 1st sg; l. 15 has `I use, make use (of)` | `I use, make use (of)` | 8 |
| per-31-the-four-requisites.md:80 | `\| paṭisevāmi \| verb \| pr.1.sg \| uses, makes use (of) \|` | 3rd-person gloss for 1st sg | `I use, make use (of)` | 8 |
| per-31-the-four-requisites.md:111 | `\| paṭisevāmi \| verb \| pr.1.sg \| uses, makes use (of) \|` | 3rd-person gloss for 1st sg | `I use, make use (of)` | 8 |
| per-31-the-four-requisites.md:71 | `thus (should think) :` | space before colon (known 31-11 fixes other typos on this line, not this one) | `thus (should think):` | 6 |
| per-32-the-repulsiveness-of-food.md:22 | `lit. bents back` | Typo | `lit. bends back` | 9 |
| per-32-the-repulsiveness-of-food.md:24 | `lit. does not caused to go forward` | Ungrammatical | `lit. is not caused to go forward` | 8 |
| per-32-the-repulsiveness-of-food.md:39 | `should not be disgusted,should not be detested` | Missing space after comma | `should not be disgusted, should not be detested` | 9 |
| per-32-the-repulsiveness-of-food.md:52 | `should be disgusted should be detested` | Missing comma between glosses | `should be disgusted, should be detested` | 8 |
| per-35-five-subjects-for-frequent-recollection.md:16 | `not pasted, not free from` | Typo | `not passed, not free from` | 9 |
| per-35-five-subjects-for-frequent-recollection.md:28 | `not pasted, not free from` | Typo | `not passed, not free from` | 9 |
| per-35-five-subjects-for-frequent-recollection.md:40 | `not pasted, not free from` | Typo | `not passed, not free from` | 9 |
| per-36-ten-subjects-for-frequent-recollection-by-one-who-has-gone-forth.md:16 | `by monk, a one who has gone forth` | Missing article / stray article | `by a monk, one who has gone forth` | 8 |
| per-36-ten-subjects-for-frequent-recollection-by-one-who-has-gone-forth.md:22 | `by a one who has gone forth` | Stray article; known 36-01 fixes only `these are ten principles should` on this line | `by one who has gone forth` | 8 |
| per-36-ten-subjects-for-frequent-recollection-by-one-who-has-gone-forth.md:138 | `by a fellow monks` | Article with plural | `by fellow monks` | 9 |
| per-36-ten-subjects-for-frequent-recollection-by-one-who-has-gone-forth.md:144 | `Is there (any) superior human states` | Verb number with plural subject; moot if the H row at :128 (abl.sg reading) is accepted | `Are there (any) superior human states` | 6 |
| per-36-ten-subjects-for-frequent-recollection-by-one-who-has-gone-forth.md:148 | `by a one who has gone forth` | Stray article; known 36-16 fixes only `these is ten principles should` on this line | `by one who has gone forth` | 8 |
| per-37-the-thirty-two-parts.md:16 | `upwards (+ abl. )` | Space before closing bracket | `upwards (+ abl.)` | 8 |
| per-37-the-thirty-two-parts.md:18 | `downwards (+ abl. )` | Space before closing bracket | `downwards (+ abl.)` | 8 |
| per-37-the-thirty-two-parts.md:66 | `synovic fluid` | Misspelt term | `synovial fluid` | 9 |
| per-38-recollection-of-impermanence.md:139 | `having born; arisen, appears` | Ungrammatical | `having been born; having arisen; having appeared` | 7 |
| per-39-dhammacakkappavattana-sutta.md:36 | `addressed group of five monks` | Missing article | `addressed the group of five monks` | 8 |
| per-39-dhammacakkappavattana-sutta.md:103 | `saddam’anussāvesuṃ..**` | Two dots; the parallel lines have `...` (known 39-09 covers only the bold) | `saddam’anussāvesuṃ...**` | 8 |
| per-40-anatta-lakkhana-sutta.md:17 | `in sāvatthi` | Proper name lower-case and missing long ī (DPD `jetavana`: "monastery in Sāvatthī"); known 40-05 fixes line 23 only | `in Sāvatthī` | 8 |
| per-40-anatta-lakkhana-sutta.md:20 | `of anāthapindika` | Proper name lower-case, `nd` for `ṇḍ` (Pāḷi line 7 `anāthapiṇḍikassa`); known 40-05 fixes line 23 only | `of Anāthapiṇḍika` | 8 |
| per-40-anatta-lakkhana-sutta.md:23 | `the Fortunate One staying in` | Finite verb missing; known 40-05 fixes only the names in this cell | `the Fortunate One was staying in` | 8 |
| per-40-anatta-lakkhana-sutta.md:29 | `Fortunate One Buddha` | Missing comma and article (same fix as known A6 for per-01) | `Fortunate One, the Buddha` | 7 |
| per-40-anatta-lakkhana-sutta.md:40 | `Fortunate One Buddha` | Missing comma and article | `Fortunate One, the Buddha` | 7 |
| per-40-anatta-lakkhana-sutta.md:394 | `Fortunate One the Buddha` | Missing comma | `Fortunate One, the Buddha` | 7 |
| per-41-aditta-pariyaya-sutta.md:25 | `Fortunate One, \|` | Gloss ends on a dangling comma | `Fortunate One, the Buddha \|` | 7 |
| per-41-aditta-pariyaya-sutta.md:252 | `Fortunate One the Buddha` | Missing comma | `Fortunate One, the Buddha` | 7 |
| per-40-anatta-lakkhana-sutta.md:43 | `addressed group of five monks` | Article missing | `addressed the group of five monks` | 8 |
| per-40-anatta-lakkhana-sutta.md:59 | `obtained is be permitted, is be possible or proper` | Garbled English `is be`; known 40-09/40-10 fix `onself` and POS only | `obtained; it could be permitted, could be possible or proper` | 8 |
| per-40-anatta-lakkhana-sutta.md:72 | `with regard to form :` | Space before colon | `with regard to form:` | 9 |
| per-40-anatta-lakkhana-sutta.md:94 | `with regard to feeling :` | Space before colon | `with regard to feeling:` | 9 |
| per-40-anatta-lakkhana-sutta.md:160 | `Impermanent venerable Sir.` | Missing comma before vocative | `Impermanent, venerable Sir.` | 8 |
| per-40-anatta-lakkhana-sutta.md:214 | `Impermanent venerable Sir.` | Missing comma before vocative | `Impermanent, venerable Sir.` | 8 |
| per-40-anatta-lakkhana-sutta.md:231 | `Impermanent venerable Sir.` | Missing comma before vocative | `Impermanent, venerable Sir.` | 8 |
| per-40-anatta-lakkhana-sutta.md:248 | `Impermanent venerable Sir.` | Missing comma before vocative | `Impermanent, venerable Sir.` | 8 |
| per-40-anatta-lakkhana-sutta.md:265 | `Impermanent venerable Sir.` | Missing comma before vocative | `Impermanent, venerable Sir.` | 8 |
| per-40-anatta-lakkhana-sutta.md:289 | `past; gone by. (m.), the past` | Stray dictionary residue `. (m.),` | `past; gone by; the past` | 6 |
| per-40-anatta-lakkhana-sutta.md:359 | `being disinterested (in) being disillusioned` | Missing comma between glosses | `being disinterested (in), being disillusioned` | 9 |
| per-40-anatta-lakkhana-sutta.md:400 | `were pleased (with) approved (of)` | Missing comma between glosses | `were pleased (with), approved (of)` | 9 |
| per-40-anatta-lakkhana-sutta.md:417 | `were released (from) were liberated` | Missing comma between glosses | `were released (from), were liberated` | 9 |
| per-40-anatta-lakkhana-sutta.md:61 | `materiality experience of material world` | Missing comma between glosses (DPD `rūpa 1` "materiality; experience of material world") | `materiality, experience of material world` | 9 |
| per-40-anatta-lakkhana-sutta.md:135 | `sentience knowing` | Missing comma between glosses | `sentience, knowing` | 9 |
| per-41-aditta-pariyaya-sutta.md:54 | `supporting condition (for) precondition (for)` | Missing comma between glosses | `supporting condition (for), precondition (for)` | 9 |
| per-41-aditta-pariyaya-sutta.md:179 | `supporting condition (for) precondition (for)` | Missing comma between glosses | `supporting condition (for), precondition (for)` | 9 |
| per-41-aditta-pariyaya-sutta.md:82 | `distresses dissatisfactions` | Missing comma between glosses | `distresses, dissatisfactions` | 9 |
| per-41-aditta-pariyaya-sutta.md:217 | `being disinterested being disillusioned` | Missing comma between glosses | `being disinterested, being disillusioned` | 9 |
| per-41-aditta-pariyaya-sutta.md:258 | `were pleased (with) approved (of)` | Missing comma between glosses | `were pleased (with), approved (of)` | 9 |
| per-41-aditta-pariyaya-sutta.md:275 | `were released (from) were liberated` | Missing comma between glosses | `were released (from), were liberated` | 9 |
| per-40-anatta-lakkhana-sutta.md:361 | `form absence of rāga` | Typo `form` for `from` | `from absence of rāga` | 9 |
| per-41-aditta-pariyaya-sutta.md:219 | `form fading of desire` | Typo `form` for `from` | `from fading of desire` | 9 |
| per-40-anatta-lakkhana-sutta.md:386 | `' There is nothing` | Space after opening quote | `'There is nothing` | 8 |
| per-41-aditta-pariyaya-sutta.md:22 | `with thousand of monks` | Article and `of` wrong | `with a thousand monks` | 8 |
| per-41-aditta-pariyaya-sutta.md:271 | `of thousand monks` | Article missing | `of a thousand monks` | 8 |
| per-41-aditta-pariyaya-sutta.md:29 | `the Fortunate One staying in Gayā` | Finite verb missing | `the Fortunate One was staying in Gayā` | 8 |
| per-41-aditta-pariyaya-sutta.md:29 | `together with thousand of monks` | Article and `of` wrong | `together with a thousand monks` | 8 |
| per-41-aditta-pariyaya-sutta.md:66 | `that too are burning` | Subject–verb agreement | `that too is burning` | 8 |
| per-41-aditta-pariyaya-sutta.md:98 | `that too are burning` | Subject–verb agreement | `that too is burning` | 8 |
| per-41-aditta-pariyaya-sutta.md:113 | `that too are burning` | Subject–verb agreement | `that too is burning` | 8 |
| per-41-aditta-pariyaya-sutta.md:128 | `that too are burning` | Subject–verb agreement | `that too is burning` | 8 |
| per-41-aditta-pariyaya-sutta.md:143 | `that too are burning` | Subject–verb agreement | `that too is burning` | 8 |
| per-41-aditta-pariyaya-sutta.md:158 | `that too are burning` | Subject–verb agreement (last remaining line) | `that too is burning` | 8 |
| per-41-aditta-pariyaya-sutta.md:66 | `what felt pleasant` | Auxiliary missing | `what is felt as pleasant` | 7 |
| per-41-aditta-pariyaya-sutta.md:98 | `what felt pleasant` | Auxiliary missing | `what is felt as pleasant` | 7 |
| per-41-aditta-pariyaya-sutta.md:113 | `what felt pleasant` | Auxiliary missing | `what is felt as pleasant` | 7 |
| per-41-aditta-pariyaya-sutta.md:128 | `what felt pleasant` | Auxiliary missing | `what is felt as pleasant` | 7 |
| per-41-aditta-pariyaya-sutta.md:143 | `what felt pleasant` | Auxiliary missing | `what is felt as pleasant` | 7 |
| per-41-aditta-pariyaya-sutta.md:158, 191, 195, 199, 203, 207, 211 | `what felt pleasant` | Auxiliary missing (remaining lines) | `what is felt as pleasant` | 7 |
| per-41-aditta-pariyaya-sutta.md:244 | `(or )` | Stray space inside brackets | `(or)` | 9 |
| per-42-yatha-vari-vaha.md:134 | `For one who respectful by habit` | Verb missing | `For one who is respectful by habit` | 9 |
| per-43-ratanattayanubhavadi-gatha.md:30 | `without remain` | Truncated word (known 43-04 touches only the Grammar cell of this row) | `without remainder` | 8 |
| per-43-ratanattayanubhavadi-gatha.md:32 | `By the majesty of three jewels, by the power of triple gem` | Missing articles | `By the majesty of the three jewels, by the power of the triple gem` | 7 |
| per-43-ratanattayanubhavadi-gatha.md:65 | `May be for you` | Ungrammatical; the known row 45-11 fixes the same phrase only in per-45 | `May there be for you` | 7 |
| per-43-ratanattayanubhavadi-gatha.md:66 | `a lifespan of a 100 years` | Stray article; per-45:134 has `a lifespan of 100 years` | `a lifespan of 100 years` | 8 |
| per-44-bhojana-dananumodana.md:27 | `Longevity, strength, ease, beauty and intelligence as fifth.**` | Mid-sentence capital after `five (things)` with no colon | `five (things): longevity, strength, ease, beauty and intelligence as fifth.**` | 6 |
| per-44-bhojana-dananumodana.md:63 | `he is one who renowned and having long life` | Ungrammatical | `he is renowned and long-lived` | 7 |
| per-45-culla-mangala-cakka-vala.md:47 | `eighty four thousands groups` | Number plural and missing hyphen (known 45-01 fixes only `ny the power` on this line) | `eighty-four thousand groups` | 8 |
| per-45-culla-mangala-cakka-vala.md:80 | `**increasing of longevity` | A new sentence (line 63 ends with a full stop) starts lower-case | `**Increasing of longevity` | 6 |
| per-46-aggappasada-sutta-gatha.md:15 | `for those who knowing, understanding comprehending` | Ungrammatical, missing comma | `for those who know, understand, comprehend` | 7 |
| per-46-aggappasada-sutta-gatha.md:20 | `incomparable (to) superior (to)` | Missing comma between gloss items | `incomparable (to), superior (to)` | 8 |
| per-46-aggappasada-sutta-gatha.md:38 | `incomparable (to) superior (to)` | Missing comma between gloss items | `incomparable (to), superior (to)` | 8 |
| per-48-so-attha-laddho.md:14 | `grown, spouted, developed` | Typo | `grown, sprouted, developed` | 8 |
| per-49-deva-aradhanai.md:85 | `This is the time to see to the Buddha` | "see to" means "attend to"; wrong sense | `This is the time to see the Buddha` | 7 |
| per-49-deva-aradhanai.md:85 | `attend to the Saṅgha, venerable sirs**` | Missing full stop at the end of the translation | `attend to the Saṅgha, venerable sirs.**` | 7 |
| per-51-nama-kara-siddhi-gatha.md:63 | `of him, his,` | Trailing comma in gloss | `of him, his` | 7 |
| per-51-nama-kara-siddhi-gatha.md:70 | `of those who knows the Dhamma by heart` | Number disagreement; the tag is gen.sg | `of one who knows the Dhamma by heart` | 7 |
| per-51-nama-kara-siddhi-gatha.md:78 | `uphold it. rightly practised` | Lower-case sentence start | `uphold it. Rightly practised` | 8 |
| per-51-nama-kara-siddhi-gatha.md:105 | `it's own` | Wrong apostrophe (known 51-09 touches only the Grammar cell of this row) | `its own` | 9 |
| per-51-nama-kara-siddhi-gatha.md:114 | `the world. virtuous` | Lower-case sentence start | `the world. Virtuous` | 8 |
| per-51-nama-kara-siddhi-gatha.md:124 | `theory, opinion attitude` | Repeated "opinion" and missing comma (DPD diṭṭhi 1: "…; theory; attitude; …") | `theory, attitude` | 8 |
| per-52-namo-kara-atthaka.md:12 | `totally perfectly` | Missing comma; known row 01-02 fixes the same gloss only in per-01, and 52-02 touches only the Grammar cell of this row | `totally, perfectly` | 8 |
| per-52-namo-kara-atthaka.md:76 | `By the splendour this homage` | Missing "of" | `By the splendour of this homage` | 9 |
| per-53-mangala-sutta.md:231 | `gentleness (in speech) obedience` | separator missing between two glosses (applies if the gloss is kept) | `gentleness (in speech), obedience` | 7 |
| per-53-mangala-sutta.md:22 | `the Fortunate One staying in Sāvatthi` | verb missing | `the Fortunate One was staying in Sāvatthi` | 8 |
| per-53-mangala-sutta.md:63 | `addressed to the Fortunate One` | `address` takes a direct object | `addressed the Fortunate One` | 8 |
| per-53-mangala-sutta.md:106 | `and veneration who should be venerated` | object missing | `and veneration of those who should be venerated` | 7 |
| per-53-mangala-sutta.md:126 | `having a merit done in the past` | ungrammatical | `having done merit in the past` | 7 |
| per-53-mangala-sutta.md:164 | `works; business es, jobs` | word split by a space | `works; businesses, jobs` | 9 |
| per-53-mangala-sutta.md:274 | `\| shake, tremble, waver \|` | 3rd sg verb glossed as bare infinitive (cf. `viharati` `stays`) | `\| shakes, trembles, wavers \|` | 6 |
| per-53-mangala-sutta.md:279 | `his mind not tremble` | verb form | `his mind does not tremble` | 8 |
| per-53-mangala-sutta.md:31 | `had advanced was waning` | separator missing between two glosses | `had advanced, was waning` | 7 |
| per-53-mangala-sutta.md:159 | `service care` | separator missing between two glosses | `service, care` | 7 |
| per-53-mangala-sutta.md:162 | `not confused unembarrassed` | separator missing between two glosses | `not confused, unembarrassed` | 7 |
| per-53-mangala-sutta.md:232 | `monks recluses` | separator missing between two glosses | `monks, recluses` | 7 |
| per-53-mangala-sutta.md:270 | `things of the world vicissitudes of life` | separator missing between two glosses | `things of the world, vicissitudes of life` | 7 |
| per-53-mangala-sutta.md:276 | `stainless faultless` | separator missing between two glosses | `stainless, faultless` | 7 |
| per-54-ratana-sutta.md:121 | `consumption decay` | separator missing between two glosses | `consumption, decay` | 7 |
| per-54-ratana-sutta.md:254 | `knowledgeable skilled` | separator missing between two glosses | `knowledgeable, skilled` | 7 |
| per-54-ratana-sutta.md:376 | `without a superior incomparable` | separator missing between two glosses | `without a superior, incomparable` | 7 |
| per-54-ratana-sutta.md:415 | `being in such a state thus gone` | separator missing between two glosses | `being in such a state, thus gone` | 7 |
| per-53-mangala-sutta.md:126 | `directing oneself rightly**` | translation lacks final full stop | `directing oneself rightly.**` | 6 |
| per-53-mangala-sutta.md:184 | `blameless actions**` | translation lacks final full stop | `blameless actions.**` | 6 |
| per-53-mangala-sutta.md:239 | `discussing the Teaching**` | translation lacks final full stop | `discussing the Teaching.**` | 6 |
| per-53-mangala-sutta.md:261 | `realization of nibbāna**` | translation lacks final full stop | `realization of nibbāna.**` | 6 |
| per-54-ratana-sutta.md:24 | `or in the sky**` | translation lacks final full stop | `or in the sky.**` | 6 |
| per-54-ratana-sutta.md:39 | `(this) speech**` | translation lacks final full stop (in this file only 113, 215, 294 have one) | `(this) speech.**` | 6 |
| per-54-ratana-sutta.md:56 | `generation**` | translation lacks final full stop | `generation.**` | 6 |
| per-54-ratana-sutta.md:74 | `protect theṃ**` | translation lacks final full stop (the known A1 item at :74 fixes `theṃ` only) | `protect theṃ.**` | 6 |
| per-54-ratana-sutta.md:97 | `equal to the Thus-Gone One**` | translation lacks final full stop | `equal to the Thus-Gone One.**` | 6 |
| per-54-ratana-sutta.md:136 | `equal to that Dhamma**` | translation lacks final full stop | `equal to that Dhamma.**` | 6 |
| per-54-ratana-sutta.md:163, 189, 241, 267, 311, 339, 365, 380, 408, 423 | `can be found**`…`rich in result**`…`the noble truths**`…`eighth existence**`…`great crimes**`…`seen the way**`…`leading to Nibbāna**`…`excellent Doctrine**`…`as this lamp**`…`may there be well-being**` | translation lines lack final full stop (one excerpt per line, in line order) | add `.` before the closing `**` on each listed line | 6 |
| per-54-ratana-sutta.md:34 | `also: and also; even so` | colon used as gloss separator | `also; and also; even so` | 7 |
| per-54-ratana-sutta.md:39 | `carefully listen intently (this) speech` | ungrammatical; `listen` needs `to` | `listen carefully to (this) speech` | 7 |
| per-54-ratana-sutta.md:49 | `(and listern)` | typo (the known A5.9 item at :49 touches POS/Grammar only) | `(and listen)` | 9 |
| per-54-ratana-sutta.md:56 | `the human's generation` | wrong possessive | `the human generation` | 6 |
| per-54-ratana-sutta.md:156 | `they has said, called` | agreement | `they have said, called` | 9 |
| per-54-ratana-sutta.md:189 | `they worthy of an offerings` | verb missing; article with plural | `they are worthy of offerings` | 8 |
| per-54-ratana-sutta.md:231 | `not can be shaken, not can be moved` | ungrammatical | `cannot be shaken, cannot be moved` | 8 |
| per-54-ratana-sutta.md:241 | `as the indra's post` | proper name lower-case (gloss :225 has `Indra's`) | `as Indra's post` | 8 |
| per-54-ratana-sutta.md:311 | `incapable to do the six great crimes` | `incapable` takes `of` + -ing | `incapable of doing the six great crimes` | 7 |
| per-54-ratana-sutta.md:323 | `done, performs, makes` | `done` is a participle; 3rd sg needed | `does, performs, makes` | 8 |
| per-54-ratana-sutta.md:339 | `incapable to hiding this` | ungrammatical | `incapable of hiding it` | 7 |
| per-54-ratana-sutta.md:374 | `giver the best` | preposition missing (known row covers only :373) | `giver of the best` | 8 |
| per-54-ratana-sutta.md:375 | `one who bring the best` | agreement | `one who brings the best` | 8 |
| per-54-ratana-sutta.md:380 | `giver the best,` | preposition missing | `giver of the best,` | 7 |
| per-54-ratana-sutta.md:380 | `who bringing the best` | verb form | `who brings the best` | 7 |
| per-55-karaniya-metta-sutta.md:143 | `what which, that are, whatever` | Typo `what which` | `that which, that are, whatever` | 7 |
| per-55-karaniya-metta-sutta.md:189 | `whether they born or seeking birth` | Verb missing | `whether they are born or seeking birth` | 9 |
| per-55-karaniya-metta-sutta.md:207 | `should defrauds` | Wrong verb form after `should` (English cell; known 55-15 touches only the Grammar cell of this row) | `should defraud` | 9 |
| per-55-karaniya-metta-sutta.md:233 | `could wishes; should desires` | Wrong verb forms after modals | `could wish; should desire` | 9 |
| per-55-karaniya-metta-sutta.md:302 | `without hostility without adversary` | Missing comma between glosses | `without hostility, without adversary` | 8 |
| per-55-karaniya-metta-sutta.md:328 | `recollection awareness` | Missing comma between glosses | `recollection, awareness` | 8 |
| per-55-karaniya-metta-sutta.md:355 | `completed perfected` | Missing comma between glosses | `completed, perfected` | 8 |
| per-56-khandha-parittam.md:27 | `the Erapatha snakes, my friendliness with the Chabyaputta snakes` | Names lack the macrons used in the Pāli and gloss (`Erāpatha`, `Chabyāputta`) | `the Erāpatha snakes, my friendliness with the Chabyāputta snakes` | 8 |
| per-56-khandha-parittam.md:124 | `rats; mouses` | Wrong plural | `rats; mice` | 9 |
| per-56-khandha-parittam.md:126 | `immeasurable. measured are creeping things` | Sentence after a full stop starts lower-case | `immeasurable. Measured are creeping things` | 8 |
| per-56-khandha-parittam.md:150 | `to those who has thoroughly understood` | Subject-verb agreement (plural) | `to those who have thoroughly understood` | 8 |
| per-57-buddha-dhamma-sangha-guna.md:12 | `Fortunate One the Buddha` | Missing comma (same fix as known per-01:11, not listed for per-57) | `Fortunate One, the Buddha` | 8 |
| per-57-buddha-dhamma-sangha-guna.md:14 | `totally perfectly` | Missing comma (same fix as known per-01:13; known 57-01 touches only the Grammar cell) | `totally, perfectly` | 8 |
| per-57-buddha-dhamma-sangha-guna.md:28 | `blessed happy` | Missing comma between glosses | `blessed, happy` | 8 |
| per-57-buddha-dhamma-sangha-guna.md:42 | `lit leading towards` | `lit` without the full stop used everywhere else | `lit. leading towards` | 8 |
| per-57-buddha-dhamma-sangha-guna.md:58 | `following the correct method walking in the right path` | Missing comma between glosses | `following the correct method, walking in the right path` | 7 |
| per-57-buddha-dhamma-sangha-guna.md:71 | `should make anjali to` | `añjali` without its tilde | `should make añjali to` | 7 |
| per-58-yan-kinci-ratanam-loke.md:58 | `the welfare of human and deities` | Number: `human` should be plural | `the welfare of humans and deities` | 7 |
| per-59-bojjhanga-parittam.md:14 | `analysis discrimination` | Missing comma between glosses | `analysis, discrimination` | 7 |
| per-59-bojjhanga-parittam.md:44 | `extinguishing (of a fire) quenching` | Missing comma between glosses | `extinguishing (of a fire), quenching` | 7 |
| per-59-bojjhanga-parittam.md:82 | `having applauded having been pleased` | Missing comma between glosses | `having applauded, having been pleased` | 7 |
| per-59-bojjhanga-parittam.md:87 | `Moggallana and Kassapa` | `Moggallāna` without its macron (Pāli line 71) | `Moggallāna and Kassapa` | 7 |
| per-59-bojjhanga-parittam.md:123 | `removed given up` | Missing comma between glosses | `removed, given up` | 7 |
| per-61-devata-uyyojana-gatha.md:24 | `who afflicted with suffering` | Verb missing; the same in `who afflicted with terror` and `who afflicted with sorrow` in this line | `who are afflicted with suffering` (also `who are afflicted with terror`, `who are afflicted with sorrow`) | 8 |
| per-61-devata-uyyojana-gatha.md:24 | `free from fear, May all` | Capital letter in the middle of the sentence | `free from fear, may all` | 9 |
| per-62-jaya-mangala-attha-gatha.md:31 | `good omens prosperity` | Missing comma between glosses (per-63:35 has `good omen, prosperity`; DPD maṅgala 1 "good omen; prosperity") | `good omens, prosperity` | 8 |
| per-62-jaya-mangala-attha-gatha.md:33 | `With thousand created arms` | Missing article | `With a thousand created arms` | 8 |
| per-62-jaya-mangala-attha-gatha.md:136 | `like of pregnant` | Ungrammatical | `like a pregnant woman's` | 8 |
| per-62-jaya-mangala-attha-gatha.md:248 | `recites or remember them` | Verb agreement | `recites or remembers them` | 9 |
| per-63-jaya-parittam.md:57 | `the Sakyans delight` | Possessive apostrophe missing | `the Sakyans' delight` | 8 |
| per-63-jaya-parittam.md:75 | `he is very happy attained the highest` | Ungrammatical | `he rejoices, having attained the highest` | 7 |
| per-63-jaya-parittam.md:90 | `those who living the holy life` | Ungrammatical | `those who live the holy life` | 8 |
| per-63-jaya-parittam.md:98 | `lucky auspicious` | Missing comma between glosses | `lucky, auspicious` | 7 |
| per-63-jaya-parittam.md:101 | `lucky auspicious` | Missing comma between glosses | `lucky, auspicious` | 7 |
| per-63-jaya-parittam.md:102 | `lucky auspicious` | Missing comma between glosses | `lucky, auspicious` | 7 |
| per-63-jaya-parittam.md:106 | `lucky auspicious` | Missing comma between glosses | `lucky, auspicious` | 7 |
| per-63-jaya-parittam.md:107 | `lucky auspicious` | Missing comma between glosses | `lucky, auspicious` | 7 |
| per-63-jaya-parittam.md:111 | `lucky auspicious` | Missing comma between glosses | `lucky, auspicious` | 7 |
| per-65-dhamma-sangani-matika.md:26 | `neither unpleasant nor pleasant neither comfortable` | Missing comma between glosses | `neither unpleasant nor pleasant, neither comfortable` | 7 |
| per-65-dhamma-sangani-matika.md:51 | `Dhammas clung and can be grasped to` | Ungrammatical throughout the line | `Dhammas clung to and able to be grasped, dhammas not clung to but able to be grasped, dhammas neither clung to nor able to be grasped` | 6 |
| per-65-dhamma-sangani-matika.md:88 | `Dhammas what should be abandoned` | "what" for "that", three times in the line | `Dhammas that should be abandoned` (all three) | 8 |
| per-65-dhamma-sangani-matika.md:151 | `determined, fixed. certain` | Full stop for a comma inside the gloss | `determined, fixed, certain` | 8 |
| per-66-vipassana-bhumi-patho.md:80 | `intellect understanding` | Missing separator between glosses | `intellect, understanding` | 6 |
| per-66-vipassana-bhumi-patho.md:117 | `six (internal sense) bases six sense organs` | Missing separator between glosses | `six (internal sense) bases, six sense organs` | 6 |
| per-66-vipassana-bhumi-patho.md:158 | `such is arising of this whole heap` | Missing article; parallel L176 has "such is the cessation" | `such is the arising of this whole heap` | 7 |
| per-66-vipassana-bhumi-patho.md:167 | `from complete fading away and ending from remainderless dispassion and cessation` | Two glosses run together without separator (known row 66-09 touches only the POS cell of this row) | `from complete fading away and ending; from remainderless dispassion and cessation` | 6 |
| per-67-patthana-matika-patho.md:11 | `prerequisite requirement` | Missing separator between glosses | `prerequisite, requirement` | 6 |
| per-67-patthana-matika-patho.md:16 | `equal in age coexistent` | Missing separator between glosses | `equal in age, coexistent` | 6 |
| per-67-patthana-matika-patho.md:19 | `assurance certainty` | Missing separator between glosses | `assurance, certainty` | 6 |
| per-68-adasi-me-adi-gatha.md:35 | `weeping, crying lamentation` | Missing separator between glosses | `weeping, crying, lamentation` | 6 |
| per-68-adasi-me-adi-gatha.md:51 | `for the good of departed` | Missing article | `for the good of the departed` | 7 |
| per-68-adasi-me-adi-gatha.md:69 | `benefits immediately**` | Prose sentence without final full stop (all other translations end with one); known row 68-10 fixes only `it is benefits` on this line | `benefits immediately.**` | 6 |
| per-68-adasi-me-adi-gatha.md:93 | `strength have been given to monks` | Subject–verb agreement | `strength has been given to monks` | 8 |
| per-69-pamsu-kula.md:13 | `constructions fabrications` | Missing separator between glosses | `constructions, fabrications` | 6 |
| per-69-pamsu-kula.md:92 | `Indeed soon, this body, will lie on the ground cast off` | Comma between subject and verb | `Indeed, soon this body will lie on the ground, cast off` | 6 |
| per-70-sharing-and-aspirations.md:62 | `guardians deities of the world` | Plural noun used attributively | `guardian deities of the world` | 8 |
| per-70-sharing-and-aspirations.md:91 | `May all living being be at ease!` | Number: "all … being" | `May all living beings be at ease!` | 9 |
| per-74-the-highest-honour-and-aspirations.md:50 | `**by this righteous action, may I not have a foolish assembly**` | Translation starts lower case and has no full stop | `**By this righteous action, may I not have a foolish assembly.**` | 8 |
| per-74-the-highest-honour-and-aspirations.md:59 | `to reaching, attainment, \|` | Trailing comma at the end of the gloss | `to reaching, attainment \|` | 8 |
| per-74-the-highest-honour-and-aspirations.md:97 | `honour respect, pay reverence` | Missing comma between glosses | `honour, respect, pay reverence` | 8 |
| per-74-the-highest-honour-and-aspirations.md:112 | `I worship, offers (to), honour` | 3sg `offers` inside a 1sg gloss | `I worship, offer (to), honour` | 8 |
| per-74-the-highest-honour-and-aspirations.md:150 | `extinguishing (of a fire) quenching` | Missing comma between glosses | `extinguishing (of a fire), quenching` | 8 |
| per-74-the-highest-honour-and-aspirations.md:153 | `be supporting condition` | Missing article | `be a supporting condition` | 7 |
| post-patimokkha.md:16 | `homage- paying` | Stray space after hyphen | `homage-paying` | 8 |
| post-patimokkha.md:21 | `**now let us make preliminary act of veneration to the Buddha, the Blessed One**` | Lower-case start, missing article, no full stop | `**Now let us make a preliminary act of veneration to the Buddha, the Blessed One.**` | 7 |
| post-patimokkha.md:31 | `totally perfectly` | Missing comma between glosses (same fix as audit 01-02, which covers per-01 only) | `totally, perfectly` | 8 |
| post-patimokkha.md:34 | `**homage to him, to the Blessed One, the worthy one, perfectly awakened one**` | Lower-case start, no full stop | `**Homage to him, to the Blessed One, the worthy one, perfectly awakened one.**` | 7 |
| pubbakicca-analysis.md:42 | `Before the performance of the observation day ceremony` | "observation" for "observance" (row :33 and the whole file use "observance day"). | `Before the performance of the observance day ceremony` | 9 |
| pubbakicca-analysis.md:108 | `participate in the Observation Day ceremony` | "Observation" for "Observance". | `participate in the Observance Day ceremony` | 9 |
| pubbakicca-analysis.md:159 | `there is not the conveying consent` | Lower-case sentence start. | `There is not the conveying consent` | 7 |
| pubbakicca-analysis.md:235 | `this [is] the winter season` | Lower-case sentence start. | `This [is] the winter season` | 7 |
| pubbakicca-analysis.md:237 | `seven uposathas have past` | "past" for "passed". | `seven uposathas have passed` | 9 |
| pubbakicca-analysis.md:245 | `by the venerab les` | Word split by a space. | `by the venerables` | 10 |
| pubbakicca-analysis.md:296 | `by the venerab les` | Word split by a space. | `by the venerables` | 10 |
| pubbakicca-analysis.md:250 | `thus, like this, the announcing` | Lower-case sentence start. | `Thus, like this, the announcing` | 7 |
| pubbakicca-analysis.md:275 | `the [so-]called counting the monks` | Lower-case sentence start. | `The [so-]called counting the monks` | 7 |
| pubbakicca-analysis.md:367 | `concord;unity; harmony` | Missing space after `;`. | `concord; unity; harmony` | 9 |
| pubbakicca-analysis.md:510 | `having known the fact` | Lower-case sentence start. | `Having known the fact` | 7 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:167 | `[for]” –pp. vb.` | missing space after the dash (every other entry has `– `) | `[for]” – pp. vb.` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:171 | `desired” –pp. vb.` | missing space after the dash | `desired” – pp. vb.` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:195 | `[used as ordinal]).` | stray `).` closes the entry in mid-sentence; the entry continues on line 197 and closes there | `[used as ordinal]` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:213 | `f. nom. pl. nominal compound … of main clause` | missing word: function not stated (cf. line 221 "compound subject of main clause") | `f. nom. pl. nominal compound subject of main clause` | 7 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:315 | `successes in live` | typo | `successes in life` | 9 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:315 | `Lifespans that are hundred years` | missing article, awkward | `Lifespans of a hundred years` | 7 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:337 | `[ *ca* + *upaddavā*]` | stray space after `[` | `[*ca* + *upaddavā*]` | 7 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:463 | `(“pleasure”– neutr.` | Missing space before the dash (every other entry has `” –`). | `(“pleasure” – neutr.` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:571 | `successes in live` | Typo. | `successes in life` | 9 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:571 | `Lifespans that are hundred years` | Missing article. | `Lifespans that are a hundred years` | 7 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:623 | `Conquerors disciples` | Missing possessive apostrophe (cf. 551 `Conqueror’s disciples`). | `Conqueror’s disciples` | 9 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:717 | `m. adj. used substantively` | Case and number missing (cf. 471 `masc. nom. sg.`). | `m. adj. nom. sg. used substantively` | 7 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:910 | `(“or” conjunctive` | Missing dash between the gloss and the grammar. | `(“or” – conjunctive` | 9 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:912 | `(“having reached the highest” m. nom.` | Missing dash between the gloss and the grammar. | `(“having reached the highest” – m. nom.` | 9 |

### E. Markdown defects that affect rendering

| Location | Current | Problem | Suggested | Conf. |
| --- | --- | --- | --- | --- |
| per-06-salutation-to-the-triple-gem.md:180 | `**by venerating thus this perfect Triple Gem, which should be strongly venerated` | The bold translation runs over three hard-wrapped source lines (180–182), with the `(or)` line inside it. The opening `**` is on line 180 and the closing `**` on line 182 (mech check ODD `**`). Line 151 writes an `(or)` translation on one line. | `**by venerating thus this perfect Triple Gem, which should be strongly venerated (or) this Triple Gem, the only thing that should be highly worshiped**` (one line, replacing 180–182) | 7 |
| per-06-salutation-to-the-triple-gem.md:167 | `\| icc'evam-ekant-abhipūjaneyyakaṃ \| \| \| \|` | The first chant line of this verse appears only as a table with no word rows (165–167). Its words are glossed after the bolded second chant line 169, so the order chant line, table, translation breaks here. (Known 06-13 covers only the bold on line 169.) | Replace the table at 165–167 with the plain chant line `icc'evam-ekant-abhipūjaneyyakaṃ` | 7 |
| per-06-salutation-to-the-triple-gem.md:186 | `\| abhisaṅkhataṃ \| pp \|` | This word belongs to chant line 169 (`vandayatābhisaṅkhataṃ`) but sits in its own table after the translation (180–182), cut off from its line and from `vandayatā` (178). (Known 06-18 covers only the Grammar cell of this row.) | Move this row into the table at 171–178, after `vandayatā`, and delete the table at 184–186 | 7 |
| per-06-salutation-to-the-triple-gem.md:36 | `\| yo'ccanta-suddhabbara-ñāṇa-locano \| \| \| \|` | The chant line is missing as plain text before its table. Every other verse line has one (23, 46, 57). | Add the plain chant line `yo'ccanta-suddhabbara-ñāṇa-locano` before the table at line 34; keep the compound row | 6 |
| per-14-from-the-elder-parapariya.md:76 | `\| yāpanatthaṃ \| \| \| \|` | Empty duplicate of the full row 77; renders a blank table row | delete line 76 | 8 |
| per-19-anupubba-sikkha.md:1249 | `[MN 107]` | no blank line before the chant line 1250, so the reference and the Pāḷi render as one paragraph | insert a blank line after line 1249 | 8 |
| per-19-anupubba-sikkha.md:951 | `**Cultivating attention in eating, drinking, chewing and tasting.` | trailing space (mech check); a single space makes no line break, so the bold lines 951–953 run together | delete the trailing space (line breaks, if wanted, via build hook) | 6 |
| per-19-anupubba-sikkha.md:952 | `Cultivating attention in urinating and defecating.` | trailing space (mech check); no line break rendered | delete the trailing space (line breaks, if wanted, via build hook) | 6 |
| per-19-anupubba-sikkha.md:1245 | `There is nothing further than this existence.'` | trailing space (mech check); lines 1245–1246 render as one line | delete the trailing space (line breaks, if wanted, via build hook) | 6 |
| per-24-dependent-origination.md:432, 433 | `saññābhavo, asaññābhavo,` | chant line hard-wrapped across two lines, with a trailing space after `asaññābhavo,` (mech check) | join 432–433 into one line: `… asaññābhavo, nevasaññānāsaññābhavo; …` | 6 |
| per-38-recollection-of-impermanence.md:128 | `\| uppāda-vaya-dhammino \| \| \| \|` | The chant line is missing before this table; the phrase sits as an empty first table row | Move `uppāda-vaya-dhammino` out of the table as the chant line before line 126 (after line 124) | 7 |
| per-39-dhammacakkappavattana-sutta.md:89 | `**\>mahārājā + ikā**` | Sub-row of the cātummahārājikā table, cut off by a blank line and rendered as a bold paragraph | Make it a table row after line 87: `\| \>mahārājā + ikā \| \| \| \|` | 6 |
| per-42-yatha-vari-vaha.md:138 | `\| [Trad] \| \| \| \|` | A Pāḷi/POS table whose only data row is a source tag; other sources (`[DHP 109]`, line 116) are plain lines | replace the table at 136–138 with the plain line `[Trad]` | 8 |
| per-40-anatta-lakkhana-sutta.md:213 | `**Monks, what do you think: 'Is feeling permanent or impermanent?'` | Bold spans a hard line break (trailing spaces) into line 214 | close bold at end of 213 (`…impermanent?'**`) and reopen at start of 214 (`**Impermanent`) | 5 |
| per-40-anatta-lakkhana-sutta.md:224 | `**'Is what is impermanent, unsatisfactory and subject to change` | Bold spans a hard line break into line 225 | close bold at end of 224 and reopen at start of 225 | 5 |
| per-40-anatta-lakkhana-sutta.md:230 | `**Monks, what do you think: 'Is perception permanent or impermanent?'` | Bold spans a hard line break into line 231 | close bold at end of 230 and reopen at start of 231 | 5 |
| per-40-anatta-lakkhana-sutta.md:241 | `**'Is what is impermanent, unsatisfactory and subject to change` | Bold spans a hard line break into line 242 | close bold at end of 241 and reopen at start of 242 | 5 |
| per-40-anatta-lakkhana-sutta.md:247 | `**Monks, what do you think: 'Are volitional formations permanent or impermanent?'` | Bold spans a hard line break into line 248 | close bold at end of 247 and reopen at start of 248 | 5 |
| per-40-anatta-lakkhana-sutta.md:258, 264, 276, 385 | `**` | Same bold-across-line-break pattern (remaining lines; pairs 258–259, 264–265, 276–277, 385–386) | close bold at end of each first line and reopen on the next | 5 |
| per-41-aditta-pariyaya-sutta.md:243 | `**He knows clearly: 'Birth is exhausted.` | Bold spans a hard line break into line 244 | close bold at end of 243 and reopen at start of 244 | 5 |
| per-53-mangala-sutta.md:150 | `\| mātā-pitu-upaṭṭhānaṃ, \| \| \| \|` | chant line put into an otherwise empty analysis table (148–150): renders as a table row, not as chant text | delete lines 148–149 and write line 150 as plain text `mātā-pitu-upaṭṭhānaṃ,` | 8 |
| per-53-mangala-sutta.md:245 | `\| ariya-saccāna-dassanaṃ; \| \| \| \|` | chant line inside an empty table (243–245) | delete lines 243–244 and write line 245 as plain text `ariya-saccāna-dassanaṃ;` | 8 |
| per-53-mangala-sutta.md:285 | `\| sabbattha'm-aparājitā; \| \| \| \|` | chant line inside an empty table (283–285) | delete lines 283–284 and write line 285 as plain text `sabbattha'm-aparājitā;` | 8 |
| per-54-ratana-sutta.md:142 | `\| samādhim'ānantarikañ'ñam'āhu. \| \| \| \|` | chant line inside an empty table (140–142) | delete lines 140–141 and write line 142 as plain text `samādhim'ānantarikañ'ñam'āhu.` | 8 |
| per-55-karaniya-metta-sutta.md:9 | `\| karaṇīyam-attha-kusalena \| \| \| \|` | The first chant line is put in a one-row table (with its own header at lines 7–8) instead of standing as a chant line like lines 13–14 | Replace lines 7–9 with the plain chant line `karaṇīyam-attha-kusalena` | 7 |
| per-55-karaniya-metta-sutta.md:132 | `\| vā \| \| ind \| or \|` | Shifted column: POS empty, `ind` sits in Grammar | `\| vā \| ind \| \| or \|` | 9 |
| per-55-karaniya-metta-sutta.md:134 | `\| vā \| \| ind \| or \|` | Shifted column: POS empty, `ind` sits in Grammar | `\| vā \| ind \| \| or \|` | 9 |
| per-55-karaniya-metta-sutta.md:142 | `\| vā \| \| ind \| or \|` | Shifted column: POS empty, `ind` sits in Grammar | `\| vā \| ind \| \| or \|` | 9 |
| per-55-karaniya-metta-sutta.md:185 | `\| vā \| \| ind \| or \|` | Shifted column: POS empty, `ind` sits in Grammar | `\| vā \| ind \| \| or \|` | 9 |
| per-55-karaniya-metta-sutta.md:294 | `\| ca \| \| ind \| and \|` | Shifted column: POS empty, `ind` sits in Grammar | `\| ca \| ind \| \| and \|` | 9 |
| per-64-bhavatu-sabba-mangalam.md:10 | `sabba-buddh-ānubhāvena,` | The third chant line is rendered as a table row under a Pāli/POS/Grammar/English header (lines 8–10) | Replace lines 8–10 with the plain chant line `sabba-buddh'ānubhāvena,` | 8 |
| per-64-bhavatu-sabba-mangalam.md:30 | `**may every blessing come to be` | Trailing space (mech check); the two verse lines 30–31 run together on render with no comma between | `**may every blessing come to be, may all deities protect (you),**` (one line, no trailing space) | 6 |
| per-64-bhavatu-sabba-mangalam.md:34 | `by the power of all Buddhas` | Trailing space (mech check); lines 34–35 run together on render | `by the power of all Buddhas, may safety always be for you.` (one line, no trailing space) | 6 |
| per-66-vipassana-bhumi-patho.md:10 | `\| viññāṇakkhandho. \| \| \| \|` | End of the chant line (L6 stops at `saṅkhārakkhandho,`) fell into the table as an empty first data row; the word also has its own row at L16 | move `viññāṇakkhandho.` to the end of L6 and delete the L10 row | 8 |
| per-69-pamsu-kula.md:19 | `\| uppāda-vaya-dhammino \| \| \| \|` | Chant line sits inside the table as an empty first data row; every other section has the chant line above the table | put `uppāda-vaya-dhammino` as a chant line above the table (before L17) and delete the L19 row | 8 |
| per-72-sharing-of-merits-with-the-departed.md:30 | `may this (merit) be for your relatives, happy may the relatives be.` | Third translation line is outside the bold that covers L26–27, and separated by two blank lines | join it to the bold block: `may this (merit) be for your relatives, happy may the relatives be.**` (closing `**` moved from L27) | 8 |
| per-72-sharing-of-merits-with-the-departed.md:10 | `idaṃ me ñātinaṃ hotu sukhitā hontu ñātayo` | L10–12 are three verse lines with single newlines; Markdown renders them as one run-on line | separate the three lines (blank line or build-hook line break) | 6 |
| pubbakicca-analysis.md:3 | `\| Pāli \| POS \| Grammar \| English \| Root \|` | Header-only table with no body (line 4 is its separator, line 5 blank): renders as an empty table and heads none of the word tables below. | Delete lines 3–4; give each word table its own header row (see the next rows) | 7 |
| pubbakicca-analysis.md:8 | `\| okāsaṃ \| noun \| masc.acc.sg \| permission \| \|` | First data row sits above the `---` separator (line 9), so it renders as the bold table header. | Insert `\| Pāli \| POS \| Grammar \| English \| Root \|` + `\| --- \| --- \| --- \| --- \| --- \|` above line 8 and delete the separator at line 9 | 7 |
| pubbakicca-analysis.md:22 | `\| thera \| noun \| masc.voc.sg? \| elder monk \| \|` | Same: first data row used as header (separator at line 23). | Insert the header + separator above line 22; delete line 23 | 7 |
| pubbakicca-analysis.md:33 | `\| uposathakaraṇato \| noun \| nt.abl.sg \|` | Same: first data row used as header (separator at line 34). | Insert the header + separator above line 33; delete line 34 | 7 |
| pubbakicca-analysis.md:48 | `\| taṇ'ṭhānasammajjanañ'ca \| sandhi \|` | Same: first data row used as header (separator at line 49). | Insert the header + separator above line 48; delete line 49 | 7 |
| pubbakicca-analysis.md:80 | `\| --- \| --- \| --- \| --- \| --- \|` | Same: `tesaññ'eva` row (79) above the separator renders as header. | Insert the header + separator above line 79; delete line 80 | 7 |
| pubbakicca-analysis.md:115, 144, 166, 183, 206, 242, 257, 280, 294, 308, 323, 358, 383, 413, 427, 449, 472, 498, 517 | `\| --- \| --- \| --- \| --- \| --- \|` | Same in every remaining table: the separator follows the first data row (lines 114, 143, 165, 182, 205, 241, 256, 279, 293, 307, 322, 357, 382, 412, 426, 448, 471, 497, 516), which renders as header. | Per table: insert `\| Pāli \| POS \| Grammar \| English \| Root \|` + separator above the first data row; delete the cited separator | 7 |
| pubbakicca-analysis.md:72 | `\| ca \| ind \| conj \| and \| \|` | Member of chand'āharaṇañ'ca lacks `\#` (cf. :53, :58). | `\| \#ca \| ind \| conj \| and \| \|` | 8 |
| pubbakicca-analysis.md:103 | `\| \#\#bhikkhunīnaṃ \|` | Members of the top-level word `bhikkhunīnam'ovādo` (:102) marked level 2 `\#\#`; the same compound at :309 uses `\#`. | `\| \#bhikkhunīnaṃ \|` | 8 |
| pubbakicca-analysis.md:104 | `\| \#\#ovādo \|` | Same wrong nesting level. | `\| \#ovādo \|` | 8 |
| pubbakicca-analysis.md:106 | `\| ca \| ind \| conj \| and \| \|` | Member of `cā'ti` (:105) lacks `\#` (cf. :174–175). | `\| \#ca \| ind \| conj \| and \| \|` | 8 |
| pubbakicca-analysis.md:107 | `\| iti \| ind \| quotation mark \|` | Member of `cā'ti` lacks `\#`. | `\| \#iti \| ind \| quotation mark \|` | 8 |
| pubbakicca-analysis.md:351 | `the nine-fold preliminary function has*` | Italic sentence hard-wrapped into two paragraphs (:351 and :353 `*been completed.*`). | Join into one line: `… the nine-fold preliminary function has been completed.*` | 8 |
| pubbakicca-analysis.md:406 | `who have not committed*` | Italic sentence hard-wrapped into two paragraphs (:406 and :408). | Join into one line: `… who have not committed an offence of pārājika, who have not been suspended by the community,*` | 8 |
| pubbakicca-analysis.md:441 | `\>(dy \> jj\>+anti` | Unclosed parenthesis in the Root cell. | `\>(dy \> jj)\>+anti` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:465 | `conjunctive *nipāta*)*.*` | Stray italic markup around the closing full stop. | `conjunctive *nipāta*).` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:481 | `third pers. act. sg.)` | Tail of the 477 entry, cut off by the footnote definition at 479 and blank lines; renders as an orphan paragraph. | Join onto 477 (`… *upapajjati* – vb. pres. ind. third pers. act. sg.)`) and put the `[^1]:` definition after it. | 9 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:579 | `[*sabbe* + *buddhā* + *ānubhāvena*] – m.` | Entry hard-wrapped across a blank line (579/581): the grammar tail renders as a separate paragraph. | Join 581 onto 579: `… [*sabbe* + *buddhā* + *ānubhāvena*] – m. instr. sg. nominal compound).` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:583 | `[*sabbe* + *dhammā* + *ānubhāvena*] – m.` | Entry split across a blank line (583/585); tail renders as a separate paragraph. | Join 585 onto 583: `… – m. instr. sg. nominal compound).` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:587 | `[*sabbe* + *saṅghā* + *ānubhāvena*] – m.` | Entry split across a blank line (587/589); tail renders as a separate paragraph. | Join 589 onto 587: `… – m. instr. sg. nominal compound).` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:591 | `[*buddho* + *ratanaṃ*] – neutr.` | Entry split across a blank line (591/593); tail renders as a separate paragraph. | Join 593 onto 591: `… – neutr. nom. sg. nominal compound).` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:595 | `[*dhammo* + *ratanaṃ*] – neutr.` | Entry split across a blank line (595/597); tail renders as a separate paragraph. | Join 597 onto 595: `… – neutr. nom. sg. nominal compound).` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:599 | `[*saṅghaṃ* + *ratanaṃ*] – neutr.` | Entry split across a blank line (599/601); tail renders as a separate paragraph. (The `saṅghaṃ` error is a separate A row.) | Join 601 onto 599: `… – neutr. nom. sg. nominal compound).` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:603 | `cardinal num. gen. pl.` | Entry split across a blank line (603/605); `*ratanānaṃ*).` renders as a separate paragraph. | Join 605 onto 603: `… gen. pl. in agreement with *ratanānaṃ*).` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:611 | `*caturāsītisahassa-*` | Entry split three times across blank lines (611 → 613 → 615 → 617), including the headword itself, so it renders as four paragraphs. (84.000 and `khanda` are separate rows.) | Join 613, 615 and 617 onto 611 as one line, closing up the headword: `*caturāsītisahassadhammakkhandhānubhāvena*: (“by the power of … – m. instr. sg. nominal compound).` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:619 | `[*piṭaka* + *taya*` | Entry split across a blank line (619/621); tail renders as a separate paragraph. | Join 621 onto 619: `… [*piṭaka* + *taya* + *ānubhāvena*] – m. instr. sg. nominal compound).` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:623, 629, 647, 651, 655, 659, 669, 679, 719, 725, 812, 826, 830, 842, 846, 854, 868, 900, 904, 912 | `(“` | Same defect as 595: each entry starting on these lines continues after a blank line, so its tail renders as a separate paragraph. | Join each continuation line (the next non-blank line) onto the cited line, removing the blank line between them. | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:795 | `**` | Line 795 is `**` plus a trailing hard break, and 796 starts `(d)**`, so the bold label spans a line break (mech: ODD ** at 795/796, trailing space at 795). | Delete line 795 and make 796 `**(d)** The wise one who gives to the supreme,` | 9 |

### F. Convention drift

| Location | Current | Problem | Suggested | Conf. |
| --- | --- | --- | --- | --- |
| per-01-dedication-of-offerings.md:45 | `\| taṃ- \| pron \| masc.acc.sg \| that \|` | Chant line 41 has `tam'mayaṃ`; per-03:109, per-04:48, per-05:95 write the sandhi member `tam-` | `tam-` | 6 |
| per-01-dedication-of-offerings.md:61 | `\| yath'ārahaṃ \| ind \| adv \|` | Table spelling differs from chant line 55 `yathārahaṃ` (changing the chant line instead would be an owner decision) | `yathārahaṃ` | 6 |
| per-01-dedication-of-offerings.md:81 | `since the Blessed One attained liberation,` | Line ends with a trailing space after `liberation,` (mech check) | delete the trailing space after `liberation,` | 9 |
| per-01-dedication-of-offerings.md:90 | `compassion, pity; lit: trembling with` | `lit:` among `lit.` elsewhere (lines 12, 36) | `compassion, pity; lit. trembling with` | 8 |
| per-01-dedication-of-offerings.md:147 | `by the Sublime One, Blessed One, fortunate one, the Buddha` | Lower-case epithet; line 24 has `Fortunate One` | `by the Sublime One, Blessed One, Fortunate One, the Buddha` | 8 |
| per-01-dedication-of-offerings.md:166 | `of Sublime One, Blessed One, fortunate one, the Buddha` | Lower-case epithet; line 35 has `Fortunate One` | `of Sublime One, Blessed One, Fortunate One, the Buddha` | 8 |
| per-04-homage-to-the-dhamma.md:24 | `by Sublime One, Blessed One, fortunate one, the Buddha` | Lower-case epithet; per-01:24 has `Fortunate One` | `by Sublime One, Blessed One, Fortunate One, the Buddha` | 8 |
| per-03-homage-to-the-buddha.md:67 | `\| sassamaṇabrāhmaṇiṃ \|` | Table drops the hyphen of chant line 63 `sassamaṇa-brāhmaṇiṃ`; rows 84–86 keep chant hyphens | `sassamaṇa-brāhmaṇiṃ` | 6 |
| per-03-homage-to-the-buddha.md:69 | `\| sadevamanussaṃ \|` | Table drops the hyphen of chant line 63 `sadeva-manussaṃ` | `sadeva-manussaṃ` | 6 |
| per-04-homage-to-the-dhamma.md:36 | `lit leading towards (to the goal)` | Missing period after `lit` | `lit. leading towards (to the goal)` | 8 |
| per-05-homage-to-the-sangha.md:64 | `**that is - four pairs of people` | Hyphen used as a dash | `**that is – four pairs of people` | 6 |
| per-05-homage-to-the-sangha.md:83 | `lit. should make anjali to` | Pāḷi word without diacritic; row headword has `añjali` | `lit. should make añjali to` | 7 |
| per-06-salutation-to-the-triple-gem.md:40 | `vara\>bara` | This compound member has no trailing hyphen; the other members (`suddha-`, `ñāṇa-`) have one. | `vara\>bara-` | 6 |
| per-08-respect-for-the-dhamma.md:7 | `[sn 6.2]` | A lower-case collection abbreviation; the other labels are capitalised (`[Dhp 153]`, `[TH 8.195]`). | `[SN 6.2]` | 8 |
| per-08-respect-for-the-dhamma.md:47 | `live - are all revering the true teaching - that is` | A hyphen is used as a dash; line 28 uses `–`. | `live – are all revering the true teaching – that is` | 7 |
| per-09-going-to-true-and-false-refuges.md:26 | `tree shrines -people` | A hyphen is used as a dash, with the space on the wrong side. | `tree shrines – people` | 8 |
| per-09-going-to-true-and-false-refuges.md:90 | `etaṃ kho saraṇaṃ khemaṃ – etaṃ saraṇam-uttamaṃ` | The line ends with a trailing space after `uttamaṃ` (mech check). | Delete the trailing space after `uttamaṃ` | 9 |
| per-11-the-three-characteristics.md:102 | `well-taught Dharma` | Sanskrit `Dharma` among `Dhamma` everywhere else (line 93 gloss `in Dhamma`) | `well-taught Dhamma` | 8 |
| per-12-the-burdens.md:16 | `\| bhāra-hāro \| noun \|` | Row hyphenates a word the chant line 8 writes solid (`bhārahāro`; DPD headword bhārahāra) | `\| bhārahāro \| noun \|` | 7 |
| per-14-from-the-elder-parapariya.md:37 | `cool; cold. \|` | Stray full stop at end of gloss | `cool; cold \|` | 6 |
| per-14-from-the-elder-parapariya.md:53 | `lit: in another` | `lit:` among `lit.` elsewhere | `lit. in another` | 7 |
| per-14-from-the-elder-parapariya.md:78 | `\| \> yāpana- \|` | Space after `\>` (other member rows: `\>sīta-`, `\>vivekaṃ-`) | `\| \>yāpana- \|` | 7 |
| per-14-from-the-elder-parapariya.md:79 | `\| \> atthaṃ \|` | Space after `\>` | `\| \>atthaṃ \|` | 7 |
| per-14-from-the-elder-parapariya.md:121 | `in caves; caverns. \|` | Stray full stop at end of gloss | `in caves; caverns \|` | 6 |
| per-14-from-the-elder-parapariya.md:159 | `\| attha- \|` | Member row of split compound lacks the `\>` prefix used at lines 37–42, 49–50 | `\| \>attha- \|` | 7 |
| per-14-from-the-elder-parapariya.md:160 | `\| cintā \| noun \|` | Member row lacks the `\>` prefix | `\| \>cintā \| noun \|` | 7 |
| per-14-from-the-elder-parapariya.md:170 | `lit: from there` | `lit:` among `lit.` elsewhere | `lit. from there` | 7 |
| per-14-from-the-elder-parapariya.md:196 | `as; like; just as. \|` | Stray full stop at end of gloss | `as; like; just as \|` | 6 |
| per-15-on-protection.md:72 | `\| kataṃ'ca \|` | Row spelling differs from chant line 62 `katañ'ca` (cf. line 108 `saṅkiliṭṭhañ'ca` follows the chant) | `\| katañ'ca \|` | 7 |
| per-15-on-protection.md:57 | `lit: dust, dirt` | `lit:` among `lit.` elsewhere | `lit. dust, dirt` | 7 |
| per-15-on-protection.md:116 | `\| mahapphalan-ti \|` | Row uses hyphen where chant line 100 has `mahapphalan'ti` | `\| mahapphalan'ti \|` | 6 |
| per-16-miscellaneous-verses.md:7 | `[sn 22.43]` | lower-case collection abbreviation; same file uses `[MN 107]`, `[MN 19]` | `[SN 22.43]` | 7 |
| per-17-a-single-excellent-night.md:7 | `[Mn 131]` | abbreviation case drift (`[MN 107]` in per-16) | `[MN 131]` | 7 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:7 | `[sn 56.11]` | lower-case collection abbreviation | `[SN 56.11]` | 7 |
| per-17-a-single-excellent-night.md:37 | `any state which is presently arisen. (or)` | line ends with a trailing space after `(or)` (mech check) | delete the trailing space after `(or)` | 6 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:83 | `**And what bhikkhus is that middle way of practice?**` | `bhikkhave` rendered `bhikkhus` here, `Monks` everywhere else in the file | `**And what, monks, is that middle way of practice?**` | 6 |
| per-18-setting-in-motion-the-wheel-of-dhamma.md:410 | `with devas, māras and brahmas` | lower case here, `Māras and Brahmas` in the parallel line 393 | `with devas, Māras and Brahmas` | 7 |
| per-19-anupubba-sikkha.md:161 | `\| tathāgato \| noun \| masc.nom.sg \| the Tathagata \|` | diacritic missing (`Tathāgata`); line 33 uses "Such Become" | `the Tathāgata` | 7 |
| per-19-anupubba-sikkha.md:168 | `**The Tathagata, having taken on` | diacritic missing | `**The Tathāgata, having taken on` | 7 |
| per-19-anupubba-sikkha.md:151 | `\| anupubba-kiriyā \| noun \| fem.nom.sg \| gradual action \|` | same word glossed `gradual activity` at line 137 (DPD anupubbakiriyā "step-by-step activity") | `gradual activity` | 6 |
| per-19-anupubba-sikkha.md:370 | `\| kālavādī \| noun \| masc.nom.sg \|` | `-vādī` compounds are `adj` at line 274 (`saccavādī`) but `noun` here; DPD kālavādī: adj | `\| kālavādī \| adj \| masc.nom.sg \|` | 8 |
| per-19-anupubba-sikkha.md:371 | `\| bhūtavādī \| noun \| masc.nom.sg \|` | same POS drift as line 370; DPD bhūtavādī: adj | `\| bhūtavādī \| adj \| masc.nom.sg \|` | 8 |
| per-19-anupubba-sikkha.md:372 | `\| atthavādī \| noun \| masc.nom.sg \|` | same POS drift as line 370; DPD atthavādī 1: adj | `\| atthavādī \| adj \| masc.nom.sg \|` | 8 |
| per-19-anupubba-sikkha.md:373 | `\| dhammavādī \| noun \| masc.nom.sg \|` | same POS drift as line 370; DPD dhammavādī 1: adj | `\| dhammavādī \| adj \| masc.nom.sg \|` | 8 |
| per-19-anupubba-sikkha.md:374 | `\| vinayavādī \| noun \| masc.nom.sg \|` | same POS drift as line 370; DPD vinayavādī: adj | `\| vinayavādī \| adj \| masc.nom.sg \|` | 8 |
| per-19-anupubba-sikkha.md:55 | `inconvenient. \|` | gloss ends with a full stop; most glosses do not | `inconvenient \|` | 7 |
| per-19-anupubba-sikkha.md:56 | `family life. \|` | trailing full stop in gloss | `family life \|` | 7 |
| per-19-anupubba-sikkha.md:106 | `the circle of relations. \|` | trailing full stop in gloss | `the circle of relations \|` | 7 |
| per-19-anupubba-sikkha.md:110 | `the circle of relations. \|` | trailing full stop in gloss | `the circle of relations \|` | 7 |
| per-19-anupubba-sikkha.md:163 | `having attained. \|` | trailing full stop in gloss | `having attained \|` | 7 |
| per-19-anupubba-sikkha.md:241 | `taking (only) what is given. \|` | trailing full stop in gloss | `taking (only) what is given \|` | 7 |
| per-19-anupubba-sikkha.md:242 | `wishing for only what is given. \|` | trailing full stop in gloss | `wishing for only what is given \|` | 7 |
| per-19-anupubba-sikkha.md:482 | `female slave. \|` | trailing full stop in gloss | `female slave \|` | 7 |
| per-19-anupubba-sikkha.md:1249 | `[MN 107]` | reference not bold; lines 657 and 1063 have `**[MN 107]**`, `**[MN 39]**` | `**[MN 107]**` | 7 |
| per-19-anupubba-sikkha.md:1226 | `pajānātī ti.` | missing apostrophe; table line 1243 and the rest of the file use `'ti` | `pajānātī'ti.` | 8 |
| per-19-anupubba-sikkha.md:659 | `tam'enaṃ tathāgato uttariṃ vineti:` | same phrase written `tamenaṃ` at 766, 819, 902, 955 | `tamenaṃ tathāgato uttariṃ vineti:` | 5 |
| per-19-anupubba-sikkha.md:650 | `ajjhattaṃ \| ind \| \|` | Grammar empty here, `adv` at line 1045 (DPD ajjhattaṃ: ind, adv; also covered by policy BP1) | `ajjhattaṃ \| ind \| adv \|` | 7 |
| per-19-anupubba-sikkha.md:685 | `anubyañjana-ggāhī. \|` | full stop inside the Pāḷi cell | `anubyañjana-ggāhī \|` | 8 |
| per-19-anupubba-sikkha.md:704 | `paṭipajjāhi; \|` | semicolon inside the Pāḷi cell | `paṭipajjāhi \|` | 8 |
| per-19-anupubba-sikkha.md:750 | `anubyañjana-ggāhī. \|` | full stop inside the Pāḷi cell | `anubyañjana-ggāhī \|` | 8 |
| per-19-anupubba-sikkha.md:844 | `parisodhehi, \|` | comma inside the Pāḷi cell | `parisodhehi \|` | 8 |
| per-19-anupubba-sikkha.md:860 | `parisodhehi, \|` | comma inside the Pāḷi cell | `parisodhehi \|` | 8 |
| per-19-anupubba-sikkha.md:1238 | `brahmacariyaṃ, \|` | comma inside the Pāḷi cell | `brahmacariyaṃ \|` | 8 |
| per-20-requisites-for-awakening.md:24 | `bahulīkātabbā, \| ptp` | Chant comma copied into the Pāḷi cell; no other headword cell carries punctuation | `bahulīkātabbā` | 8 |
| per-21-the-seven-factors-of-awakening.md:41 | `dassanaṃ- \| noun` | Same sandhi form written with `ṃ` here but with `m` in the chant line (28 `dassanam'p'āhaṃ`) and in the parallel rows `savanam-`, `upasaṅkamanam-` … (lines 55–67) | `dassanam-` | 7 |
| per-22-the-noble-eightfold-path.md:37 | `katamā ca \| pron \| fem.nom.sg` | Two words in one row with one tag; elsewhere `katamo` and `ca` get separate rows (lines 258–259) | split into `katamā \| pron \| fem.nom.sg \| what?` and `ca \| ind \| \| and` | 6 |
| per-22-the-noble-eightfold-path.md:338 | `ācikkhanti — \| verb` | Chant dash copied into the Pāḷi cell | `ācikkhanti` | 8 |
| per-22-the-noble-eightfold-path.md:154 | `pahānāya chandaṃ janeti vāyamati` | Chant line hard-wrapped onto line 155; all other chant lines are single lines | join lines 154–155 with a space | 6 |
| per-22-the-noble-eightfold-path.md:178 | `ṭhitiyā asammosāya bhiyyobhāvāya vepullāya` | Chant line hard-wrapped onto line 179 | join lines 178–179 with a space | 6 |
| per-23-mindfulness-of-breathing.md:177 | `\| sikkhati, \| verb \|` | Comma from the chant line copied into the Pāḷi cell; every other `sikkhati` row has none | `\| sikkhati \| verb \|` | 9 |
| per-23-mindfulness-of-breathing.md:187 | `\| sikkhati, \| verb \|` | Comma from the chant line copied into the Pāḷi cell | `\| sikkhati \| verb \|` | 9 |
| per-23-mindfulness-of-breathing.md:8, 290 | `bahulī-katā mahapphalā hoti mahā-nisaṃsā` … `bahulīkatā mahapphalā hoti mahānisaṃsā` | The same chant phrase is hyphenated at line 8 (and 21, 34, 48, 57) but unhyphenated at line 290; changing it alters a Pāḷi chant line | owner decision; simplest: line 290 → `bahulī-katā mahapphalā hoti mahā-nisaṃsā` | 5 |
| per-24-dependent-origination.md:111 | `abhisaṅkhāro, \| noun` | chant punctuation carried into the Pāḷi cell (most rows have none; may be corpus-wide) | `abhisaṅkhāro \| noun` | 6 |
| per-24-dependent-origination.md:113 | `abhisaṅkhāro; \| noun` | chant punctuation carried into the Pāḷi cell | `abhisaṅkhāro \| noun` | 6 |
| per-24-dependent-origination.md:131 | `rūpāvacarā; \| adj` | chant punctuation carried into the Pāḷi cell | `rūpāvacarā \| adj` | 6 |
| per-24-dependent-origination.md:194 | `cakkhuviññāṇaṃ, \| noun` | chant punctuation carried into the Pāḷi cell | `cakkhuviññāṇaṃ \| noun` | 6 |
| per-24-dependent-origination.md:583 | `samannāgatassa, \| adj` | chant punctuation carried into the Pāḷi cell | `samannāgatassa \| adj` | 6 |
| per-24-dependent-origination.md:196 | `ghānaviññāṇaṃ, \| noun` | chant punctuation carried into the Pāḷi cell | `ghānaviññāṇaṃ \| noun` | 6 |
| per-24-dependent-origination.md:197 | `jivhāviññāṇaṃ, \| noun` | chant punctuation carried into the Pāḷi cell | `jivhāviññāṇaṃ \| noun` | 6 |
| per-24-dependent-origination.md:199 | `manoviññāṇaṃ. \| noun` | chant punctuation carried into the Pāḷi cell | `manoviññāṇaṃ \| noun` | 6 |
| per-24-dependent-origination.md:279 | `cakkhāyatanaṃ, \| noun` | chant punctuation carried into the Pāḷi cell | `cakkhāyatanaṃ \| noun` | 6 |
| per-24-dependent-origination.md:280 | `sotāyatanaṃ, \| noun` | chant punctuation carried into the Pāḷi cell | `sotāyatanaṃ \| noun` | 6 |
| per-24-dependent-origination.md:300, 404, 406, 524, 588, 589, 593, 616, 617, 618, 619, 620, 621, 642, 646, 670, 674 | `cakkhusamphasso, \| noun`; `abhisaṅkhāro, \| noun`; `abhisaṅkhāro; \| noun`; `paripāko; \| noun`; `socanā, \| noun`; `socitattaṃ; \| noun`; `parijjhāyanā, \| noun`; `paridevitattaṃ; \| noun`; `vācā, \| noun`; `palāpo, \| noun`; `vippalāpo; \| noun`; `lālappo, \| noun`; `lālappanā, \| noun`; `dukkhaṃ; \| noun`; `vedayitaṃ; \| noun`; `dukkhaṃ; \| noun`; `vedayitaṃ; \| noun` | same: trailing `,` `;` `.` in the Pāḷi cell (remaining lines, in the order cited; 406 even has `;` where chant line 397 has `.`) | drop the trailing punctuation from each Pāḷi cell (e.g. `cakkhusamphasso \| noun`) | 6 |
| per-24-dependent-origination.md:131 | `belonging to the world of (subtle material) form. \|` | trailing full stop in an English gloss cell | `belonging to the world of (subtle material) form \|` | 7 |
| per-24-dependent-origination.md:234 | `attention; mental application; \|` | trailing separator in gloss cell | `attention; mental application \|` | 7 |
| per-24-dependent-origination.md:621 | `murmuring, \|` | trailing comma in gloss cell | `murmuring \|` | 7 |
| per-24-dependent-origination.md:622 | `murmuration. \|` | trailing full stop in gloss cell | `murmuration \|` | 7 |
| per-24-dependent-origination.md:34 | `desire; lit: thirst` | `lit:` beside `lit.` elsewhere | `desire, lit. thirst` | 7 |
| per-24-dependent-origination.md:251 | `earth water fire wind, lit great element` | `lit` without period beside `lit.` | `earth water fire wind, lit. great element` | 7 |
| per-24-dependent-origination.md:572 | `suffering (from), lit touched (by)` | `lit` without period beside `lit.` | `suffering (from), lit. touched (by)` | 7 |
| per-24-dependent-origination.md:586 | `suffering (from), lit touched (by)` | `lit` without period beside `lit.` | `suffering (from), lit. touched (by)` | 7 |
| per-24-dependent-origination.md:321 | `cakkhu-samphassa-jā` | hyphenated, unlike chant line 317 and sibling rows 322–326 | `cakkhusamphassajā` | 7 |
| per-24-dependent-origination.md:484 | `satta-nikāye` | hyphenated, unlike chant line 474 `sattanikāye` | `sattanikāye` | 7 |
| per-25-the-dhamma-in-brief.md:81 | `sarāgāya;` | Chant punctuation copied into the Pāḷi cell; other cells are bare | `sarāgāya` | 6 |
| per-25-the-dhamma-in-brief.md:92 | `saṃyogāya;` | Chant punctuation copied into the Pāḷi cell | `saṃyogāya` | 6 |
| per-25-the-dhamma-in-brief.md:103 | `ācayāya;` | Chant punctuation copied into the Pāḷi cell | `ācayāya` | 6 |
| per-25-the-dhamma-in-brief.md:114 | `mahicchatāya;` | Chant punctuation copied into the Pāḷi cell | `mahicchatāya` | 6 |
| per-25-the-dhamma-in-brief.md:125 | `asantuṭṭhiyā;` | Chant punctuation copied into the Pāḷi cell | `asantuṭṭhiyā` | 6 |
| per-25-the-dhamma-in-brief.md:136 | `saṅgaṇikāya;` | Chant punctuation copied into the Pāḷi cell | `saṅgaṇikāya` | 6 |
| per-25-the-dhamma-in-brief.md:147 | `kosajjāya;` | Chant punctuation copied into the Pāḷi cell | `kosajjāya` | 6 |
| per-25-the-dhamma-in-brief.md:167 | `ekaṃsena,` | Chant punctuation copied into the Pāḷi cell | `ekaṃsena` | 6 |
| per-25-the-dhamma-in-brief.md:171 | `dhammo,` | Chant punctuation copied into the Pāḷi cell | `dhammo` | 6 |
| per-26-the-four-great-references.md:12 | `mah'āpadesā` | Chant spelling differs from line 224 `mahāpadesā` | `mahāpadesā` | 5 |
| per-26-the-four-great-references.md:44 | `has been learned - this is` | Hyphen used as a dash (known 26-01 on this line is only `a monks`) | `has been learned – this is` | 7 |
| per-26-the-four-great-references.md:60 | `sammukhā \| ind \| \| face to face (with)` | Lines 29 and 35 give Grammar `(+gen)` for the same word | Grammar `(+gen)` | 6 |
| per-26-the-four-great-references.md:62 | `sammukhā \| ind \| \| face to face (with)` | Lines 29 and 35 give Grammar `(+gen)` | Grammar `(+gen)` | 6 |
| per-26-the-four-great-references.md:86 | `sammukhā \| ind \| \| face to face (with)` | Lines 29 and 35 give Grammar `(+gen)` | Grammar `(+gen)` | 6 |
| per-26-the-four-great-references.md:88 | `sammukhā \| ind \| \| face to face (with)` | Lines 29 and 35 give Grammar `(+gen)` | Grammar `(+gen)` | 6 |
| per-26-the-four-great-references.md:108 | `neva \| ind \| \| neither` | Pāḷi cell differs from chant line 101 `n'eva` | `n'eva` | 5 |
| per-26-the-four-great-references.md:224 | `mahāpadesā ti` | Detached `ti`; elsewhere the quotative is `'ti` (line 97) | `mahāpadesā'ti` | 6 |
| per-26-the-four-great-references.md:38 | `dhammo,` | Chant punctuation copied into the Pāḷi cell | `dhammo` | 6 |
| per-26-the-four-great-references.md:56 | `sapāmokkho.` | Chant punctuation copied into the Pāḷi cell | `sapāmokkho` | 6 |
| per-26-the-four-great-references.md:167 | `sammāsambuddhassa;` | Chant punctuation copied into the Pāḷi cell | `sammāsambuddhassa` | 6 |
| per-26-the-four-great-references.md:197 | `sammāsambuddhassa;` | Chant punctuation copied into the Pāḷi cell | `sammāsambuddhassa` | 6 |
| per-29-striving-according-to-the-dhamma.md:90 | `\| a'pāpuṇitvā \|` | stray apostrophe; chant line and DPD have `apāpuṇitvā` | `apāpuṇitvā` | 9 |
| per-29-striving-according-to-the-dhamma.md:7 | `[sn 12.22]` | lower-case collection abbreviation; others `[AN 7.23]`, `[DN 16.36]`, `[MN 2.4]` | `[SN 12.22]` | 8 |
| per-29-striving-according-to-the-dhamma.md:298 | `\| bhikkhave \| noun \| voc.pl \|` | gender missing; DPD masc voc pl, rest of corpus `masc.voc.pl` | `masc.voc.pl` | 9 |
| per-29-striving-according-to-the-dhamma.md:308 | `\| bhikkhave \| noun \| voc.pl \|` | gender missing; DPD masc voc pl | `masc.voc.pl` | 9 |
| per-30-the-buddhas-final-instruction.md:67 | `\| bhikkhave \| noun \| voc.pl \|` | gender missing; DPD masc voc pl | `masc.voc.pl` | 9 |
| per-30-the-buddhas-final-instruction.md:15 | `\| evaṃ'assa \|` | table spelling differs from chant line `evam'assa` (l. 8); DPD headword evamassa | `evam'assa` | 8 |
| per-32-the-repulsiveness-of-food.md:39 | `a'jigucchanīyo` | Apostrophe inside the word; chant line 31 has `ajigucchanīyo` (DPD ajigucchanīya) | `ajigucchanīyo` | 7 |
| per-33-universal-well-being.md:80 | `sakā- \| noun` | Final member of `kammassakā` carries a compound hyphen though nothing follows (per-35:63 `sako-` is followed by `amhi`); known 33-04 changes only the POS of this row | `sakā` | 7 |
| per-33-universal-well-being.md:100 | `good or bad – of that` | En dash and hyphen mixed in one sentence (`- good or bad –`); per-35:84 uses `-` both times | `good or bad - of that` | 7 |
| per-34-the-divine-abidings.md:73 | `pharitvā viharati …` | `…` here; parallel lines 65 and 81 use `...` | `pharitvā viharati ...` | 6 |
| per-36-ten-subjects-for-frequent-recollection-by-one-who-has-gone-forth.md:20 | `dasa? \| adj` | Question mark inside the word cell | `dasa` | 8 |
| per-36-ten-subjects-for-frequent-recollection-by-one-who-has-gone-forth.md:66 | `upavadatī'ti, \| verb` | Trailing punctuation in the word cell; known 36-05 changes only the Grammar cell | `upavadatī'ti` | 8 |
| per-36-ten-subjects-for-frequent-recollection-by-one-who-has-gone-forth.md:86 | `vinābhāvo' ti` | Space after the elision apostrophe; line 24 writes `'ti` | `vinābhāvo'ti` | 6 |
| per-36-ten-subjects-for-frequent-recollection-by-one-who-has-gone-forth.md:102 | `vītivattantī'ti; \| verb` | Trailing punctuation in the word cell | `vītivattantī'ti` | 8 |
| per-36-ten-subjects-for-frequent-recollection-by-one-who-has-gone-forth.md:142 | `bhavissāmī'ti, \| verb` | Trailing punctuation in the word cell | `bhavissāmī'ti` | 8 |
| per-36-ten-subjects-for-frequent-recollection-by-one-who-has-gone-forth.md:146 | `paccavekkhitabbā' ti` | Space after the elision apostrophe; line 24 writes `'ti` | `paccavekkhitabbā'ti` | 6 |
| per-37-the-thirty-two-parts.md:17 | `pādatalā, \| noun` | Trailing punctuation in the word cell | `pādatalā` | 8 |
| per-37-the-thirty-two-parts.md:20 | `matthakā, \| noun` | Trailing punctuation in the word cell | `matthakā` | 8 |
| per-39-dhammacakkappavattana-sutta.md:9 | `**[SN 56.11]**` | Reference bolded; other chants write it plain (`[AN 7.49]`, `[DN 13.8]`) | `[SN 56.11]` | 6 |
| per-39-dhammacakkappavattana-sutta.md:31 | `pañca \| adj \| \| five (5)` | First member of compound `pañcavaggiye` lacks the compound hyphen used elsewhere | `pañca-` | 7 |
| per-39-dhammacakkappavattana-sutta.md:45 | `idamavoca \| verb` | Row drops the apostrophe of chant line 41 `idam'avoca` | `idam'avoca` | 6 |
| per-40-anatta-lakkhana-sutta.md:113 | `saṅkhārā ca hidaṃ` | Lines 45, 87, 100 write `h'idaṃ` | `saṅkhārā ca h'idaṃ` | 6 |
| per-40-anatta-lakkhana-sutta.md:130 | `viññāṇañ'ca hidaṃ` | Lines 45, 87, 100 write `h'idaṃ` | `viññāṇañ'ca h'idaṃ` | 6 |
| per-40-anatta-lakkhana-sutta.md:216 | `yam pan'āniccaṃ` | `yaṃ` on 162, 175 | `yaṃ pan'āniccaṃ` | 7 |
| per-40-anatta-lakkhana-sutta.md:233 | `yam pan'āniccaṃ` | `yaṃ` on 162, 175 | `yaṃ pan'āniccaṃ` | 7 |
| per-40-anatta-lakkhana-sutta.md:250 | `yam pan'āniccaṃ` | `yaṃ` on 162, 175 | `yaṃ pan'āniccaṃ` | 7 |
| per-40-anatta-lakkhana-sutta.md:268 | `yam pan'āniccaṃ` | `yaṃ` on 162, 175 | `yaṃ pan'āniccaṃ` | 7 |
| per-40-anatta-lakkhana-sutta.md:351 | `\| sutavā \| noun \|` | Same word is POS `adj` at per-41:170; DPD `sutavant 1` adj | `\| sutavā \| adj \|` | 8 |
| per-40-anatta-lakkhana-sutta.md:382 | `\| itthattāyā'ti \| n. abstr \|` | Non-standard POS; same word is `noun` at per-41:240; DPD `itthatta` nt, abstr | `\| itthattāyā'ti \| noun \|` | 8 |
| per-41-aditta-pariyaya-sutta.md:89 | `tam pi ādittaṃ` | Same word is `tampi` (43) and `tam'pi` (table 63) | `tam'pi ādittaṃ` | 6 |
| per-41-aditta-pariyaya-sutta.md:104 | `tam pi ādittaṃ` | Spelling drift (see 43, 63) | `tam'pi ādittaṃ` | 6 |
| per-41-aditta-pariyaya-sutta.md:119 | `tam pi ādittaṃ` | Spelling drift (see 43, 63) | `tam'pi ādittaṃ` | 6 |
| per-41-aditta-pariyaya-sutta.md:134 | `tam pi ādittaṃ` | Spelling drift (see 43, 63) | `tam'pi ādittaṃ` | 6 |
| per-41-aditta-pariyaya-sutta.md:149 | `tam pi ādittaṃ` | Spelling drift (see 43, 63) | `tam'pi ādittaṃ` | 6 |
| per-41-aditta-pariyaya-sutta.md:193 | `saddesu pi nibbindati, sotaviññāṇe pi nibbindati` | Detached `pi`; line 164 writes `rūpesu'pi`, `cakkhuviññāṇe'pi` | `saddesu'pi nibbindati, sotaviññāṇe'pi nibbindati` | 6 |
| per-41-aditta-pariyaya-sutta.md:197 | `gandhesu pi nibbindati, ghānaviññāṇe pi nibbindati` | Detached `pi` (cf. 164) | `gandhesu'pi nibbindati, ghānaviññāṇe'pi nibbindati` | 6 |
| per-41-aditta-pariyaya-sutta.md:201 | `jivhāya pi nibbindati, rasesu pi nibbindati, jivhāviññāṇe pi nibbindati` | Detached `pi` (cf. 164) | `jivhāya'pi nibbindati, rasesu'pi nibbindati, jivhāviññāṇe'pi nibbindati` | 6 |
| per-41-aditta-pariyaya-sutta.md:205 | `phoṭṭhabbesu pi nibbindati, kāyaviññāṇe pi nibbindati` | Detached `pi` (cf. 164) | `phoṭṭhabbesu'pi nibbindati, kāyaviññāṇe'pi nibbindati` | 6 |
| per-41-aditta-pariyaya-sutta.md:209 | `dhammesu pi nibbindati, manoviññāṇe pi nibbindati, manosamphasse pi nibbindati` | Detached `pi` (cf. 164) | `dhammesu'pi nibbindati, manoviññāṇe'pi nibbindati, manosamphasse'pi nibbindati` | 6 |
| per-41-aditta-pariyaya-sutta.md:213 | `vimuttam' iti` | Space after elision apostrophe; per-40:345 has `vimuttam'iti` | `vimuttam'iti` | 8 |
| per-42-yatha-vari-vaha.md:12 | `lit: carrying` | `lit.` everywhere else | `lit. carrying` | 8 |
| per-42-yatha-vari-vaha.md:152 | `\| ānubhāvena, \|` | Comma in the word cell, not in the Pāḷi line 140 | `\| ānubhāvena \|` | 6 |
| per-43-ratanattayanubhavadi-gatha.md:65 | `**May be for you: victory, success, wealth, gain, safety, luck, happiness, strength,` | Hard-wrapped bold translation with a trailing space (mech: TRAILING SPACE, ODD ** on 65 and 66) | Join lines 65–66 into one line, no trailing space | 7 |
| per-44-bhojana-dananumodana.md:26 | `**One who gives food to whoever, he gives to him also five (things)` | Hard-wrapped bold translation with a trailing space (mech: TRAILING SPACE, ODD ** on 26 and 27) | Join lines 26–27 into one line, no trailing space | 7 |
| per-44-bhojana-dananumodana.md:59 | `**The wise-one is a longevity-giver, strength-giver, beauty-giver, understanding-giver.` | Hard-wrapped bold translation with a trailing space (mech: TRAILING SPACE, ODD ** on 59 and 60) | Join lines 59–60 into one line, no trailing space | 7 |
| per-45-culla-mangala-cakka-vala.md:133 | `**May be f or you: victory, success, wealth, gain, safety, luck, happiness, strength,` | Hard-wrapped bold translation with a trailing space (mech: TRAILING SPACE, ODD ** on 133 and 134); known 45-11 fixes only the wording on this line | Join lines 133–134 into one line, no trailing space | 7 |
| per-44-bhojana-dananumodana.md:22 | `\| vaṇṇaṃ, \|` | Chant punctuation copied into the Pāli cell | `\| vaṇṇaṃ \|` | 7 |
| per-44-bhojana-dananumodana.md:39 | `\| paṭibhānado. \|` | Chant punctuation copied into the Pāli cell | `\| paṭibhānado \|` | 7 |
| per-44-bhojana-dananumodana.md:51 | `\| paṭibhānakaṃ. \|` | Chant punctuation copied into the Pāli cell | `\| paṭibhānakaṃ \|` | 7 |
| per-44-bhojana-dananumodana.md:23 | `\| paṭibhānaṃ ca \|` | Pāli cell does not match the chant spelling `paṭibhānañ'ca` (line 7); line 50 keeps the chant form `sukhañ'ca` | `\| paṭibhānañ'ca \|` | 6 |
| per-44-bhojana-dananumodana.md:63 | `Having given longevity, strength, beauty, happiness and understanding` | The only translation line in this slice that is not bold | `**Having given longevity, … wherever he is reborn.**` | 6 |
| per-51-nama-kara-siddhi-gatha.md:69 | `lit leading out` | `lit` without the full stop used everywhere else (`lit.`) | `lit. leading out` | 8 |
| per-53-mangala-sutta.md:43 | `almost the whole Jeta's grove` | `Jeta's Grove` capitalised at :22 and :18 | `almost the whole Jeta's Grove` | 7 |
| per-54-ratana-sutta.md:115 | `khayaṃ virāgaṃ amataṃ paṇītaṃ,` | trailing space (mech check) | remove the trailing space after `paṇītaṃ,` | 8 |
| per-54-ratana-sutta.md:116 | `yad-ajjhagā sakya-munī samāhito.` | trailing space (mech check) | remove the trailing space after `samāhito.` | 8 |
| per-55-karaniya-metta-sutta.md:159 | `ye сa dūre vasanti avidūre` | `сa` is written with a Cyrillic `с` (U+0441) in the chant line | `ye ca dūre vasanti avidūre` (Latin `c`) | 10 |
| per-55-karaniya-metta-sutta.md:175 | `\| сa \| ind \| \| and \|` | `сa` is written with a Cyrillic `с` (U+0441) | `\| ca \| ind \| \| and \|` (Latin `c`) | 10 |
| per-55-karaniya-metta-sutta.md:193 | `**may all beings be easygoing` | Trailing space at end of line | Remove the trailing space | 9 |
| per-56-khandha-parittam.md:24 | `with Gotamaka snakes – family of snakes` | En dash here; lines 13, 17, 19 use `-` in the same formula | `with Gotamaka snakes - family of snakes` | 7 |
| per-57-buddha-dhamma-sangha-guna.md:76 | `that which practiced well,` | Lines 76–81 end in one trailing space; a single space makes no line break, so the seven-line translation renders as one run-on line | Remove the trailing spaces on lines 76–81 (line breaks, if wanted, by build hook) | 8 |
| per-58-yan-kinci-ratanam-loke.md:5 | `yaṅ'kiñci ratanaṃ loke` | Apostrophe here; the same chant lines 28 and 32 write `yaṅ kiñci` | `yaṅ kiñci ratanaṃ loke` | 7 |
| per-60-abhaya-parittam.md:27 | `yo cāmanāpo` | Same chant line has `yo c'āmanāpo` on line 5 and in table row 14; elision mark dropped here | `yo c'āmanāpo` | 7 |
| per-60-abhaya-parittam.md:31 | `yo cāmanāpo` | Same as line 27 (line 5 and row 14 have `c'āmanāpo`) | `yo c'āmanāpo` | 7 |
| per-62-jaya-mangala-attha-gatha.md:56 | `than Mara making war` | Macron missing; tables have `Māra` (DPD māra) | `than Māra making war` | 8 |
| per-62-jaya-mangala-attha-gatha.md:89 | `mālavantaṃ. iddhī'bhisaṅkhata-mano` | Full stop inside the verse; the other stanzas put a comma before the `… jitavā mun'indo` line | `mālavantaṃ, iddhī'bhisaṅkhata-mano` | 6 |
| per-62-jaya-mangala-attha-gatha.md:155 | `atiandha \| adj` | Chant has `ati-andha-bhūtaṃ`; the compound member has no hyphen | `ati-andha- \| adj` | 7 |
| per-62-jaya-mangala-attha-gatha.md:236 | `sarate-m'` | Chant line 221 has `sarate'm'atandī`; hyphen marks a compound member, which this is not (the known item 62-17 covers only the tag) | `sarate'm'` | 6 |
| per-64-bhavatu-sabba-mangalam.md:34 | `by the power of all Buddhas` | Second half of the translation is not bold, unlike lines 30–31 and every other translation | `**by the power of all Buddhas, may safety always be for you.**` | 7 |
| per-65-dhamma-sangani-matika.md:134 | `dhammas from limited sense-objects` | `-ārammaṇā` is rendered "with … object(s)" on lines 166, 190, 204; "from" here (three times). The known item 65-06 on this line is the `exhalted` typo; this row is the preposition | `dhammas with limited sense-objects` (and `with` for the other two items) | 7 |
| per-65-dhamma-sangani-matika.md:212 | `anidassana \| adj` | Compound member without hyphen; line 210 has `sanidassana-` | `anidassana- \| adj` | 8 |
| per-66-vipassana-bhumi-patho.md:57 | `**eighteen elements: the eye element, the form element, the eye-consciousness` | Hard-wrapped paragraph (break mid-sentence, trailing space) | join L57 and L58 into one line | 7 |
| per-66-vipassana-bhumi-patho.md:160 | `nāma-rūpa-nirodhā, saḷ-āyatana-nirodho,` | Hard-wrapped chant line (trailing space, continues on L161) | join L160 and L161 into one line | 7 |
| per-66-vipassana-bhumi-patho.md:171 | `cessation of consciousness; with the cessation of consciousness, cessation of name-and-form;` | Hard-wrapped paragraph (trailing space, continues on L172) | join L171 and L172 into one line | 7 |
| per-68-adasi-me-adi-gatha.md:25 | `**He gave to me, he made for me` | Hard-wrapped translation (trailing space, continues on L26) | join L25 and L26 into one line | 6 |
| per-72-sharing-of-merits-with-the-departed.md:26 | `**may this (merit) be for my relatives, happy may the relatives be.` | Hard-wrapped translation (trailing space); renders run-on with L27 | join L26 and L27 (or separate lines via build hook) | 6 |
| per-66-vipassana-bhumi-patho.md:73 | `\| somanassa \|` | Only compound member in the table without the trailing `-` | `\| somanassa- \|` | 8 |
| per-66-vipassana-bhumi-patho.md:40 | `the form base` | Hyphen drift within the sentence: `eye-base`, `ear-base`, `sound-base` … but `form base`, `mind-object base` | `the form-base` … `the mind-object-base` | 6 |
| per-66-vipassana-bhumi-patho.md:160 | `nāma-rūpa-nirodho, … saḷ-āyatana-nirodho` | Compound spelling drift within the chant: arising half has `nāmarūpa`, `saḷāyatana`, `jarāmaraṇaṃ`, `dukkhadomanass'`; cessation half (L160–161) hyphenates them | `nāmarūpa-nirodho`, `saḷāyatana-nirodho` (and `jarāmaraṇaṃ`, `dukkhadomanass'` at L161) | 6 |
| per-66-vipassana-bhumi-patho.md:174 | `dukkha-kkhandhassa` | Hyphen splits the doubled consonant; L147 has `dukkhakkhandhassa` | `dukkhakkhandhassa` | 7 |
| per-68-adasi-me-adi-gatha.md:76 | `the duty of relatives.` | Gloss cell ends with a full stop; gloss cells otherwise have none | `the duty of relatives` | 7 |
| per-68-adasi-me-adi-gatha.md:87 | `given; handed over.` | Gloss cell ends with a full stop | `given; handed over` | 7 |
| per-69-pamsu-kula.md:86 | `gone away; rid of; without.` | Gloss cell ends with a full stop | `gone away; rid of; without` | 7 |
| per-70-sharing-and-aspirations.md:98 | `in three ways; in a threefold way.` | Gloss cell ends with a full stop | `in three ways; in a threefold way` | 7 |
| per-70-sharing-and-aspirations.md:129 | `cutting; severing; destruction.` | Gloss cell ends with a full stop | `cutting; severing; destruction` | 7 |
| per-70-sharing-and-aspirations.md:17 | `\| guṇa' \|` | Compound member marked with `'` instead of the file's `-` (cf. `ācariya-` L26, `vara-` L199) | `\| guṇa- \|` | 7 |
| per-71-sharing-of-all-merits.md:17 | `\| yāni-' \|` | Double marker `-'` on a sandhi word | `\| yāni- \|` | 7 |
| per-73-sharing-of-merits-with-the-devas.md:27 | `sabba sampatti siddhiyā` | Same compound hyphenated at L8 (`sabba-sampatti-siddhiyā`) | `sabba-sampatti-siddhiyā` | 7 |
| per-73-sharing-of-merits-with-the-devas.md:35 | `sabba sampatti siddhiyā` | Same compound hyphenated at L8 | `sabba-sampatti-siddhiyā` | 7 |
| per-74-the-highest-honour-and-aspirations.md:83 | `anudhammacārī,` | Chant comma copied into the Pāḷi cell | `anudhammacārī` | 8 |
| post-patimokkha.md:85 | `## Recitation of virtue` | Heading case differs from the other H2s (`Preliminary Homage`, `On Protection`, `The Pāṭimokkha Exhortation`) | `## Recitation of Virtue` | 7 |
| pubbakicca-analysis.md:35 | `\| \#uposatha \| noun \| - \|` | Grammar `-` on a compound member; elsewhere the file has bare gender (`masc.` :263, :283; `masc` :266) or empty — a third form under either A5.7 or B11.3. | `\| \#uposatha \| noun \| masc \|` (A5.7 form; ∅ if B11.3 is chosen) | 7 |
| pubbakicca-analysis.md:105 | `“...and”` | `...` where the file also uses `…` (:13 `may…give`). | `“…and”` | 6 |
| pubbakicca-analysis.md:173 | `“... remaining”` | `...` vs `…`. | `“… remaining”` | 6 |
| pubbakicca-analysis.md:270 | `“...this many”` | `...` vs `…`. | `“…this many”` | 6 |
| pubbakicca-analysis.md:414 | `\| ca \| ind \| and \| and \|` | Grammar `and` instead of `conj` (used for every other ca in the file). | `\| ca \| ind \| conj \| and \|` | 9 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:391 | `dative. sg.` | abbreviation drift: everywhere else `dat.` | `dat. sg.` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:613 | `84.000` | Decimal point used as a thousands separator; the translation at 549 has `84,000`. | `84,000` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:655 | `*vaṇṇavaḍḍhako* :` | Space before the colon (no other headword has one). | `*vaṇṇavaḍḍhako*:` | 8 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:731 | `dative. sg.` | Abbreviation drift: everywhere else it is `dat.` (629, 870). | `dat. sg.` | 8 |

### G. Links

None.

### H. Data to re-verify (forms, references, counts)

| Location | Current | Problem | Suggested | Conf. |
| --- | --- | --- | --- | --- |
| per-03-homage-to-the-buddha.md:77 | `pariyosāṇa-kalyāṇaṃ` | Chant line has retroflex `ṇ`; DPD headword is pariyosāna (dental `n`), as is table row 86. Changing a Pāḷi chant line is an owner decision (data-preservation rule, like known B-Q1/B-Q2) | owner decision: change chant line to `pariyosāna-kalyāṇaṃ` (DPD pariyosāna 1) | 7 |
| per-08-respect-for-the-dhamma.md:67 | `[TH 8.195] dhammika-theragāthā` | The Dhammikattheragāthā (`na hi dhammo adhammo ca…`, `dhammo have rakkhati…`) is, from memory, Th 4.10 (Thag 303–306); `8.195` does not fit. Not checked against SuttaCentral. | Verify on SuttaCentral; probably `[Th 4.10]` | 6 |
| per-11-the-three-characteristics.md:13 | `\| sabbe \| adj \| masc.nom.pl \|` | DPD: sabba pos `pron` (grammar "pron, adj"); the corpus tags sabba `adj` (e.g. per-10:13 `sabba-`), so this is a corpus-wide POS choice for the owner (near D4), not a single-row fix | Owner decision: if DPD `pron` is adopted for sabba, `\| sabbe \| pron \| masc.nom.pl \|` | 7 |
| per-11-the-three-characteristics.md:41 | `\| sabbe \| adj \| masc.nom.pl \|` | Same as line 13 (DPD sabba `pron`; corpus-wide POS choice, near D4) | Owner decision: if DPD `pron` is adopted for sabba, `\| sabbe \| pron \| masc.nom.pl \|` | 7 |
| per-11-the-three-characteristics.md:54 | `\| sabbe \| adj \| masc.nom.pl \|` | Same as line 13 (DPD sabba `pron`; corpus-wide POS choice, near D4) | Owner decision: if DPD `pron` is adopted for sabba, `\| sabbe \| pron \| masc.nom.pl \|` | 7 |
| per-13-from-the-elder-ratthapala.md:230 | `pabbajito'mhi raja` | Chant line: the vocative is `rāja` elsewhere (chant line 205, rows 224, 250); a Pāḷi chant-text change is an owner decision (data-preservation rule); DPD silent (no `rājan` headword in saved output) | Owner decision: `pabbajito'mhi rāja` | 7 |
| per-14-from-the-elder-parapariya.md:22 | `\| iriyaṃ \| noun \| fem.acc.sg \|` | Subject of `āsi`, so cannot be acc; DPD has only iriyā fem (no `iriya` headword), so the gender is right and the `nt` alternative is ruled out, but `iriyaṃ` is not a regular fem nom form | Owner/verify: `fem.nom.sg` (metrical `-ṃ` for `iriyā`, per DPD fem) or keep `fem.acc.sg` with a note | 6 |
| per-16-miscellaneous-verses.md:169 | `rajo \| adj \| masc.nom.sg \| one with impurity, defiled` | `pamād'ānupatito rajo`: `rajo` is the same word as line 165 ("dust/defilement follows heedlessness"); DPD has only `raja` adj = "dusty; dirty; with dirt" (from `rajas`), not "one with impurity", and no entry for the form `rajo`; translation line 176 is built on the adj reading | owner decision / DPD lookup `rajas`: likely `rajo \| noun \| masc.nom.sg \| (mental) impurity, defilement, lit: dust` (as line 165) and line 176 retranslated | 5 |
| per-16-miscellaneous-verses.md:65 | `Snp 66 [v 949]` | Snp 66 is Jatukaṇṇimāṇavapucchā (verse 1099); v 949 is in Attadaṇḍasutta (Snp 53); the verse occurs in both, but the two numbers point to different suttas | verify; `Snp 66 [v 1099]` or `Snp 53 [v 949]` | 5 |
| per-16-miscellaneous-verses.md:88, 108, 129, 158 | `Snp 22 [v` | Uṭṭhānasutta (Snp 22) is believed to be vv 331–334 (Rāhulasutta starts at 335); labels 333–336 look shifted by 2 | verify; if confirmed, 333→331, 334→332, 335→333, 336→334 | 5 |
| per-17-a-single-excellent-night.md:16 | `yad \| pron \| nt.nom.sg \| whichever, whatever, that which (object)` | Grammar says nominative (subject of `pahīnaṃ`) but gloss says "(object)"; DPD `yad` is only nt acc sg, "which (object)", so DPD backs the gloss against the tag, while the syntax backs the tag | owner decision: keep `nt.nom.sg` and drop `(object)` from the gloss, or follow DPD `yad` and set Grammar `nt.acc.sg` | 5 |
| per-19-anupubba-sikkha.md:78 | `\| yannūnāhaṃ \| \| \| what if I` | POS and Grammar empty; chant line 74 writes `yan'nūn'āhaṃ`; DPD silent (no headword for `yannūna` in the slice lookup) | DPD lookup: yannūna; owner decision: POS `ind` or `sandhi` (policy BP7, open), and whether to align the spelling with line 74 | 5 |
| per-19-anupubba-sikkha.md:770 | `paṭisankhā` | chant line uses `n` for `ṅ`; table line 778 has `paṭisaṅkhā` | owner decision (chant `n` vs `ṅ`): `paṭisaṅkhā` | 6 |
| per-19-anupubba-sikkha.md:785 | `paṭihankhāmi` | chant line uses `n` for `ṅ`; table line 806 has `paṭihaṅkhāmi` | owner decision (chant `n` vs `ṅ`): `paṭihaṅkhāmi` | 6 |
| per-19-anupubba-sikkha.md:834 | `cankamena` | chant line uses `n` for `ṅ`; table line 839 has `caṅkamena` | owner decision (chant `n` vs `ṅ`): `caṅkamena` | 6 |
| per-19-anupubba-sikkha.md:848 | `cankamena` | chant line uses `n` for `ṅ`; table line 855 has `caṅkamena` | owner decision (chant `n` vs `ṅ`): `caṅkamena` | 6 |
| per-19-anupubba-sikkha.md:885 | `cankamena` | chant line uses `n` for `ṅ`; table line 893 has `caṅkamena` | owner decision (chant `n` vs `ṅ`): `caṅkamena` | 6 |
| per-19-anupubba-sikkha.md:906 | `sanghāṭipattacīvaradhāraṇe` | chant line uses `n` for `ṅ`; table line 923 has `saṅghāṭi-` | owner decision (chant `n` vs `ṅ`): `saṅghāṭipattacīvaradhāraṇe` | 6 |
| per-19-anupubba-sikkha.md:979 | `pallankaṃ` | chant line uses `n` for `ṅ`; table line 987 has `pallaṅkaṃ` | owner decision (chant `n` vs `ṅ`): `pallaṅkaṃ` | 6 |
| per-19-anupubba-sikkha.md:1144 | `anangaṇe` | chant line uses `n` for `ṅ`; table line 1155 has `anaṅgaṇe` | owner decision (chant `n` vs `ṅ`): `anaṅgaṇe` | 6 |
| per-24-dependent-origination.md:62 | `**such is arising of this whole heap of suffering.**` | translation sentence starts lower-case; the file mostly uses lower-case starts (upper-case only at 27, 49, 72, 118, 526, 551), and this may be corpus-wide, so the direction is a convention decision | owner decision: capitalise translation starts (then `**Such is arising of this whole heap of suffering.**`) or lower-case the six upper-case lines | 5 |
| per-24-dependent-origination.md:89 | `**not knowing suffering` | lower-case translation start (convention decision, see :62) | owner decision; if capitalising: `**Not knowing suffering` | 5 |
| per-24-dependent-origination.md:102 | `**what are formations'` | lower-case translation start (convention decision, see :62) | owner decision; if capitalising: `**What are formations'` | 5 |
| per-24-dependent-origination.md:122 | `**what is wholesome practice'` | lower-case translation start (convention decision, see :62); the C row on this line is a separate problem | owner decision; if capitalising: `**What is wholesome practice'` | 5 |
| per-24-dependent-origination.md:136 | `**skillful intentions` | lower-case translation start (convention decision, see :62) | owner decision; if capitalising: `**Skillful intentions` | 5 |
| per-24-dependent-origination.md:98 | `**this is called ignorance'.**` | lower-case translation start (convention decision, see :62) | owner decision; if capitalising: `**This is called` | 5 |
| per-24-dependent-origination.md:140 | `**this is called wholesome practice'.**` | lower-case translation start (convention decision, see :62) | owner decision; if capitalising: `**This is called` | 5 |
| per-24-dependent-origination.md:152 | `**this is called unwholesome practice'.**` | lower-case translation start (convention decision, see :62) | owner decision; if capitalising: `**This is called` | 5 |
| per-24-dependent-origination.md:168 | `**this is called practice of imperturbability'.**` | lower-case translation start (convention decision, see :62) | owner decision; if capitalising: `**This is called` | 5 |
| per-24-dependent-origination.md:184 | `**these are called formations'` | lower-case translation start (convention decision, see :62) | owner decision; if capitalising: `**These are called` | 5 |
| per-24-dependent-origination.md:205, 240, 261, 269, 290, 311, 332, 353, 372, 412, 460, 468, 498, 559, 601, 628, 656, 684, 703 | `**this is called` | same lower-case translation start (remaining lines; the other lower-case `what is` / `therein` / `thus` lines follow the same pattern) | owner decision; if capitalising: `**This is called` | 5 |
| per-28-principles-of-non-decline.md:69, 85 | `yathāpaññattesu sikkhāpadesu vattissanti` … `\| samādāya \| verb \| ger \|` | table and translation (l. 88 "undertaking") have `samādāya`, the chant line does not (AN 7.23 reads `sikkhāpadesu samādāya vattissanti`) | verify SBS chant book: add `samādāya` to the chant line, or drop the table row | 8 |
| per-29-striving-according-to-the-dhamma.md:250, 260 | `avaṅkatā avaññā bhavissati` … `\| avañjhā \|` | chant line `avaññā` disagrees with table `avañjhā` (DPD avañjha adj "productive; profitable"; SN 12.22 `avañjhā`) | verify SBS chant book; if it reads `avañjhā`, correct the chant line to `avañjhā` (owner decision: chant-text change) | 7 |
| per-35-five-subjects-for-frequent-recollection.md:24 | `byādhi- \| noun \| nt` | DPD byādhi is masc; the bare gender is wrong only if A5.7 (keep bare gender) is chosen; known 35-02 (B11.3) blanks this cell instead | Owner decision A5.7/B11.3: under A5.7 Grammar `masc`; under B11.3 ∅ (known 35-02) | 8 |
| per-36-ten-subjects-for-frequent-recollection-by-one-who-has-gone-forth.md:128 | `dhammā \| noun \| masc.nom.pl \| mental states` | In the AN 10.48 phrase `uttarimanussadhammā alamariyañāṇadassanaviseso adhigato` (chant line 119), `viseso` is the subject and `uttarimanussadhammā` is usually read as masc.abl.sg ("beyond the human state"); the row and translation line 144 make it a plural subject. DPD uttarimanussadhamma masc gives no case | Verify against the SBS book / CST and a commentary; if abl.sg: row `dhammā \| noun \| masc.abl.sg \| (beyond) human states`, chant unchanged, translation 144 rebuilt | 5 |
| per-39-dhammacakkappavattana-sutta.md:65, 66, 67, 68, 69, 70, 71, 72, 73, 74 | `\| āyasmato \| \| \| \|` | Rows āyasmato … udapādi have no POS, Grammar or English; saved DPD output covers only koṇḍañña (masc) | Fill POS, Grammar and English for each row from DPD (lookup: āyasmant, viraja, vītamala, dhammacakkhu, uppajjati) | 8 |
| per-39-dhammacakkappavattana-sutta.md:86, 87, 95, 101, 107, 113, 114, 115, 121, 122, 123, 124, 125, 126, 127, 133, 134, 135 | `\| cātummahārājikā \| \| \| \|` | Deva-name tables have only the Pāḷi column filled | Fill POS, Grammar and English from DPD, or owner decision to drop the empty tables | 7 |
| per-39-dhammacakkappavattana-sutta.md:139, 140, 141 | `ayañca dasasahassilokadhātu saṅkampi` | Closing chant lines (and lines 78–82) have no table and no translation | Owner decision: add tables and translations, or mark the passage as untranslated | 5 |
| per-40-anatta-lakkhana-sutta.md:329 | `yā kiñci vedanā` | `kiñci` is nt (DPD `kiñci 2/3` nt nom, masc & nt acc) and cannot agree with fem `vedanā`; DPD `kāci` fem nom sg & pl. Chant-line change; the SN 22.59 reading `yā kāci vedanā` is from memory and must be checked | owner: check SN 22.59 / SBS chant book; if confirmed, `yā kāci vedanā` | 7 |
| per-40-anatta-lakkhana-sutta.md:333 | `yā kiñci saññā` | `kiñci` is nt; fem nom is `kāci` (DPD). Chant-line change, reading from memory | owner: check SN 22.59 / SBS chant book; if confirmed, `yā kāci saññā` | 7 |
| per-40-anatta-lakkhana-sutta.md:337 | `yā kiñci saṅkhārā … sabbā saṅkhārā` | `saṅkhārā` is masc pl (DPD `saṅkhāra` masc); relative and `sabba` must agree (DPD `keci` masc nom pl). Chant-line change; SN 22.59 reading from memory | owner: check SN 22.59 / SBS chant book; if confirmed, `ye keci saṅkhārā … ye dūre santike vā, sabbe saṅkhārā` | 7 |
| per-41-aditta-pariyaya-sutta.md:68 | `rāg'agginā, dos'agginā, moh'agginā ādittaṃ` | Refrain differs from lines 100, 115, 130, 145, 160 (`ādittaṃ rāgagginā dosagginā mohagginā, ādittaṃ`) in word order and apostrophes; chant-line change | owner: check SN 35.28 and unify the six refrains | 5 |
| per-45-culla-mangala-cakka-vala.md:54 | `\| te \| pron \| 2.gen.sg \| your, of you \|` | DPD has the idiom `sabbe te` "all of them" and te 1.1 masc nom pl "they; those"; `te` here may be "those", not "your" (translation line 63 follows "your"); te 2.4 "your" is also possible | Owner decision: `te` masc.nom.pl "those" (and line 63 "all those …") vs keep 2.gen.sg "your" | 5 |
| per-62-jaya-mangala-attha-gatha.md:26 | `tan' \| pron \| masc.acc.sg` | The refrain `tan'tejasā` means "by the power of that" (taṃ as compound member, = tassa tejasā); an acc tag does not fit that meaning. DPD has tejasā only as ind, adv ("powerfully"), which does not settle tan' | Owner decision / DPD lookup: Grammar empty (compound member `tan-`) | 5 |
| per-63-jaya-parittam.md:77 | `[AN 3.156]` | The verse is from the Pubbaṇhasutta, whose number differs between editions (SuttaCentral may number it AN 3.155) | Verify the sutta number against SuttaCentral | 4 |
| per-67-patthana-matika-patho.md:5 | `[Abhi-A Dh.s]` | The 24 conditions are the Paṭṭhāna mātikā (paccayuddesa of the Paṭṭhāna), not Dhammasaṅgaṇī (that is per-65) | verify the source and relabel to a Paṭṭhāna reference (owner picks the label form) | 7 |
| per-70-sharing-and-aspirations.md:161 | `viriyavā'minā. (?viriyamhinā)` | Editorial query left inside the chant line; DPD viriyavant adj (nom sg viriyavā) supports the table's reading `viriyavā- + iminā` (L170–171) | owner decision on the reading; if `viriyavā'minā` is kept, delete `(?viriyamhinā)` | 7 |
| per-70-sharing-and-aspirations.md:101 | `\| pāpetha \| verb \| opt.refl.3.sg \|` | Mood/person doubtful: subject is plural `puññāni` (L87) and the parallel `dentu` is imp.3.pl; DPD pāpeti 1.1 confirms caus "leads (to)" but has no pāpetha form, which may be pr/imp 2.pl or opt.refl.3.sg | DPD lookup: pāpeti inflection table for `pāpetha`, then fix mood/person (refl notation per A5.3/B11.2) | 4 |
| per-74-the-highest-honour-and-aspirations.md:133 | `āsavakkhayā-vahaṃ` | Chant hyphen falls inside the second member (DPD: āsavakkhaya + āvaha) | owner decision on chant text: `āsavakkhayāvahaṃ` or `āsavakkhaya-āvahaṃ` | 8 |
| per-74-the-highest-honour-and-aspirations.md:63 | `DN 16.27` | Reference format/number doubtful; the passage is in DN 16 (Mahāparinibbāna), SuttaCentral segment dn16:5.3 | verify reference and use the corpus citation style | 4 |
| post-patimokkha.md:40 | `\| saccakiriyāgāthāyo \| \| \| \|` | Every table in the file (lines 40–208) has empty POS, Grammar and English cells; the analysis is unfinished | owner decision: fill the cells from DPD or mark the page as draft | 9 |
| pubbakicca-analysis.md:22 | `masc.voc.sg?` | Open query `?` left in the Grammar cell; `thera` is the speaker label of the bracketed rubric, and :516 tags the same label `masc.voc.sg` without `?`. | owner decision: tag the label (`masc.voc.sg` as at :516, or stem only) and drop `?` | 6 |
| pubbakicca-analysis.md:364 | `\| cātuddasī \| noun \| fem.nom.sg \|` | In the chant (:355) cātuddasī is a member of the hyphenated compound `cātuddasī-paṇṇarasī-sāmaggīnam'aññataro`, not a free nom.sg word. | owner decision: re-tag as compound member (`\#cātuddasī`, stem gender) under one headword row | 5 |
| pubbakicca-analysis.md:365 | `\| paṇṇarasī \| noun \| fem.nom.sg \|` | Same: paṇṇarasī is a member of the hyphenated compound at :355. | owner decision: re-tag as compound member (`\#paṇṇarasī`, stem gender) under one headword row | 5 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:355 | `(“gain” – m. n. nom. sg.)` | *lābha* is masculine only in DPD (*lābha 1*, *lābha 2* masc; nom. sg. *lābho*); `lābhaṁ` with tag m. nom. sg. is self-contradictory | owner decision: tag as `neutr. n. nom. sg.` (masc. noun treated as nt. in the verse) or `m. n. acc. sg.` | 5 |
| word-by-word-analysis-of-sbs-anumodana-chants-by-a-thanuttamo.md:695 | `(“gain” – m. n. nom. sg.)` | `lābhaṃ` cannot be masc. nom. sg. (that is `lābho`). DPD lābha 1–2 is masc only, so the neuter reading is out; it stands as an acc. form in a nominative list. Same decision as slice 21 :355. | Owner confirms `(“gain” – m. n. acc. sg. used as nom.)`. | 6 |

### I. Further details on the material under review

None.
