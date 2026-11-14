"""Export the Bhikkhu Pātimokkha English translation as Markdown and DOCX."""

import argparse
from pathlib import Path
from typing import cast

import pandas as pd
import pypandoc
from scripts.generate_patimokkha import (
    Page,
    get_pages,
    load_data,
    normalize_cell,
    strip_anki_number,
)
from tools.printer import printer as pr

TITLE = "# Bhikkhu Pātimokkha — English Translation"

# The TSV only has Pāḷi case forms, so the section names are fixed here.
SECTION_NAMES = {
    "NI": "Nidāna",
    "PA": "Pārājika",
    "SA": "Saṅghādisesa",
    "AN": "Aniyata",
    "NP": "Nissaggiya Pācittiya",
    "PC": "Pācittiya",
    "PD": "Pāṭidesanīya",
    "SE": "Sekhiya",
    "AS": "Adhikaraṇasamatha",
}


def run_translation(df: pd.DataFrame, run: int) -> str:
    """Join one run's English sentences, chosen exactly as the website pages choose them.

    A row is a translation when it has no part of speech and belongs to a
    sentence; rows are visited sentence by sentence, in the site's order. The
    cell is folded to one line and stripped of the Anki disambiguation number.
    """
    rows = cast(pd.DataFrame, df[df["run"] == run])
    sentence_series = cast(pd.Series, rows["sentence"])
    translations: list[str] = []
    for sentence in sentence_series.drop_duplicates():
        if not sentence:
            continue
        group = cast(pd.DataFrame, rows.loc[sentence_series == sentence])
        translation_mask = group["pos"].astype(str).str.strip() == ""
        for value in cast(pd.Series, group.loc[translation_mask, "pali"]).tolist():
            translation = strip_anki_number(normalize_cell(value))
            if translation:
                translations.append(translation)
    return " ".join(translations)


def build_markdown(df: pd.DataFrame, pages: list[Page]) -> str:
    """Render the recitation as one section per heading and one paragraph per run."""
    blocks = [TITLE]
    for page in pages:
        abbrev = page["abbrev"]
        body = run_translation(df, page["run"])
        if " " not in abbrev and page["run_of_rule"] == 0:
            blocks.append(f"## {SECTION_NAMES[abbrev]}")
            blocks.append(body)
        elif page["run_of_rule"] >= 1:
            blocks.append(body)
        else:
            blocks.append(f"{abbrev}. {body}")
    return "\n\n".join(blocks) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "tsv",
        nargs="?",
        default=str(
            Path(__file__).parent.parent / "data" / "patimokkha_word_by_word.tsv"
        ),
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Where to write the files (default: output/docs).",
    )
    args = parser.parse_args()

    tsv_path = Path(args.tsv)
    if not tsv_path.exists():
        raise FileNotFoundError(f"TSV not found: {tsv_path}")
    output_dir = (
        Path(args.output_dir)
        if args.output_dir
        else Path(__file__).parent.parent / "output" / "docs"
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    pr.bip()
    df = load_data(tsv_path)
    pages = get_pages(df)
    md_path = output_dir / "patimokkha_english.md"
    md_path.write_text(build_markdown(df, pages), encoding="utf-8")
    docx_path = output_dir / "patimokkha_english.docx"
    # Disable pandoc's smart punctuation so the DOCX text stays verbatim.
    pypandoc.convert_file(
        str(md_path),
        "docx",
        format="markdown-smart",
        outputfile=str(docx_path),
    )
    pr.green(f"Wrote {md_path} and {docx_path}")
    pr.yes(len(pages))


if __name__ == "__main__":
    main()
