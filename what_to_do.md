
## instruction how to do monthly update of [sbs study tools](https://sasanarakkha.github.io/study-tools/):

- generate latest dps-full using [dpd-db/dps/scripts/dps_csv.py](https://github.com/digitalpalidictionary/dpd-db/blob/main/dps/scripts/dps_csv.py)
- generate latest ru and sbs dict using [exporter/mkall.sh](https://github.com/Devamitta/exporter/blob/main/mkall.sh)
- generate anki-csvs using [dpd-db/dps/scripts/anki_csvs.py](https://github.com/digitalpalidictionary/dpd-db/blob/main/dps/scripts/anki_csvs.py)
- make patimokkha and grammar using [utilities/all_in_one.sh](https://github.com/Devamitta/utilities/blob/main/all_in_one.sh)
- in Anki update all decks from importing csvs (dpd-db/dps/csvs/anki-csvs/)
- push [patimokkha_dict](https://github.com/Devamitta/patimokkha_dict) to github, updating [html version of word-by-word.](https://devamitta.github.io/patimokkha_dict/Bhikkhu_Patimokkha/main.html)


## plans on pali projects

**sutta interlude**

- checking words in [Anki deck related to MN107](https://github.com/sasanarakkha/study-tools/blob/main/pali-class/anki-decks/Suttas%20Advanced.apkg)
- checking [analysis of SBS PER](https://sasanarakkha.github.io/study-tools/sbs-per-analysis.html)
- checking words in [Anki deck of SBS PER](https://sasanarakkha.github.io/study-tools/anki-decks/sbs-pali-english-vocab.html)
- adding words from **Reading the Buddha’s Discourses in Pāli** by Venerable Bhikkhu Bodhi which analyzing by Ñāna [(6 chapters-saṃyuttas)](https://sasanarakkha.github.io/study-tools/pali-class/pali-class-adv.html) using [dpd-db/dps/scripts/extract_id_from_docs.py](https://github.com/digitalpalidictionary/dpd-db/blob/main/dps/scripts/extract_id_from_docs.py) and in [GUI](https://github.com/digitalpalidictionary/dpd-db/blob/main/gui/gui.py) in "Words To Add" tab section "from id-list" field: "sbs_category" do not have value - and all words one by one add relevant sutta by "edit word in DPS" button. Then using [dpd-db/dps/scripts/anki_csvs.py](https://github.com/digitalpalidictionary/dpd-db/blob/main/dps/scripts/anki_csvs.py) extract csv for anki deck. Add words to [Anki deck](https://github.com/sasanarakkha/study-tools/blob/main/pali-class/anki-decks/Suttas%20Advanced.apkg) using generated csv.
- check words from anki deck related to each saṃyutta

**[advanced pali course](https://sasanarakkha.github.io/study-tools/pali-class/pali-class-adv.html)**

- add commentary examples from [file](https://docs.google.com/document/d/1lK846LWGEpC9VJvQ6GZYUgZDWdjLtZSZ/edit), distribute them in the classes accordingly.
- check key
- check words in Anki deck related to classes
- add full information from "The New Pali Course Part III by A.P. Buddhadatta.pdf" into [class doc](https://docs.google.com/document/d/1QMX_yuH9uJeTEfg3ItetlI5RVsPGlj0Q1XUstHXRLZo/edit)

**patimokkha word by word**

- slowly in the class making translation of sentences in [xlsx]([Pātimokkha Word by Word - Google Sheets](https://docs.google.com/spreadsheets/d/1rS-IlX4DvKmnBO58KON37eVnOZqwfkG-ot-zIjCuzH4/edit#gid=1426532622))
- gradually make updates in [html version of word-by-word.](https://devamitta.github.io/patimokkha_dict/Bhikkhu_Patimokkha/main.html) by using [patimokkha_dict/make_pat.sh](https://github.com/Devamitta/patimokkha_dict/blob/main/make_pat.sh)
- make additional vibhanga Anki deck by adding words from vibhanga using in [GUI](https://github.com/digitalpalidictionary/dpd-db/blob/main/gui/gui.py) tab Words To Add section "from source" by adding source (like VIN 1.1.1) and adding words in [GUI](https://github.com/digitalpalidictionary/dpd-db/blob/main/gui/gui.py) in "Edit DPS" tab
- then checking words which do not have source in sbs_source, using button "no source" in  [GUI](https://github.com/digitalpalidictionary/dpd-db/blob/main/gui/gui.py)in tab Words To Add. 