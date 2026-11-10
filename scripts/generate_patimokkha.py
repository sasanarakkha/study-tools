"""Generate Markdown pages for Bhikkhu Pātimokkha word-by-word analysis."""

import argparse
import re
from pathlib import Path
from typing import TypedDict, cast
from urllib.parse import quote

import pandas as pd

FEEDBACK_URL = (
    "https://docs.google.com/forms/d/e/"
    "1FAIpQLSdG6zKDtlwibtrX-cbKVn4WmIs8miH4VnuJvb7f94plCDKJyA/"
    "viewform?usp=pp_url"
)
SECTION_LABEL = re.compile(r"^[A-Z]{2,3}(?: \d+)?$")
COLS = [
    "pali",
    "pos",
    "grammar",
    "case",
    "meaning",
    "meaning_lit",
    "root",
    "base",
    "construction",
    "compound_type",
    "compound_construction",
]
HEADERS = [
    "pāḷi",
    "pos",
    "grammar",
    "case",
    "meaning",
    "meaning_lit",
    "root",
    "base",
    "construction",
    "compound_type",
    "compound_construction",
]


class SourceRow(TypedDict):
    source: str
    abbrev: str


def load_data(xlsx_path: Path) -> pd.DataFrame:
    df = pd.read_excel(xlsx_path, engine="openpyxl")
    # Forward fill source and abbrev to handle sparse columns and preserve order
    df["source"] = df["source"].ffill().str.strip()
    df["abbrev"] = df["abbrev"].ffill().str.strip()
    return assign_orphan_sentences(df.fillna(""))


def assign_orphan_sentences(df: pd.DataFrame) -> pd.DataFrame:
    """Give rows with a blank `sentence` the sentence they belong to.

    The sheet stores each rule's English translation on a row of its own and
    usually leaves that row's `sentence` cell empty, so grouping rows by
    `sentence` would drop the translation. Such rows inherit the preceding
    sentence. Rows whose text is itself a sentence of the Pāḷi text (the
    heading of the following rule, which the sheet places inside the previous
    rule's block) and section labels ("PA 1", "PC 42") are left blank so they
    stay excluded.
    """
    sentences = cast(list[str], df["sentence"].astype(str).tolist())
    words = cast(list[str], df["pali"].astype(str).tolist())
    sources = cast(list[str], df["source"].astype(str).tolist())

    known_sentences = {s.strip() for s in sentences if s.strip()}

    resolved: list[str] = []
    current = ""
    current_source = ""
    for sentence, word, source in zip(sentences, words, sources, strict=True):
        if source != current_source:
            current_source, current = source, ""
        text = word.strip()
        if not text or SECTION_LABEL.match(text):
            sentence = ""
        elif sentence.strip():
            current = sentence
        elif text in known_sentences:
            sentence = ""
        else:
            sentence = current
        resolved.append(sentence)

    df["sentence"] = resolved
    return df


def get_sources(df: pd.DataFrame) -> list[SourceRow]:
    # drop_duplicates preserves the order of the first occurrence by default.
    source_series = cast(pd.Series, df["source"])
    abbrev_series = cast(pd.Series, df["abbrev"])
    sources: list[SourceRow] = []
    seen: set[str] = set()
    for source_value, abbrev_value in zip(source_series, abbrev_series, strict=True):
        source = cast(str, source_value)
        if source and source not in seen:
            row: SourceRow = {"source": source, "abbrev": cast(str, abbrev_value)}
            sources.append(row)
            seen.add(source)
    return sources


def file_name(source: str) -> str:
    """Slugify whitespace: filenames must not rely on percent-encoding by renderers."""
    return re.sub(r"\s+", "-", source.strip())


def generate_index(sources: list[SourceRow], output_dir: Path) -> None:
    lines = ["# Bhikkhu Pātimokkha - Word by Word Analysis\n"]
    for s in sources:
        lines.append(f"- [{s['abbrev']} {s['source']}]({file_name(s['source'])}.md)")
    (output_dir / "index.md").write_text("\n".join(lines), encoding="utf-8")


def generate_rule_page(
    source: SourceRow,
    df: pd.DataFrame,
    output_dir: Path,
    sources: list[SourceRow],
    idx: int,
) -> None:
    rule, abbrev = source["source"], source["abbrev"]
    rule_df = df[df["source"] == rule]
    lines = [f"# {abbrev} {rule}\n"]

    sentence_series = cast(pd.Series, rule_df["sentence"])
    sentences = sentence_series.drop_duplicates()
    for sentence in sentences:
        if not sentence:
            continue
        lines.append(f"## {sentence}\n")
        sent_df = cast(
            pd.DataFrame,
            rule_df.loc[sentence_series == sentence, COLS].copy(),
        )
        sent_df = sent_df.replace(0, "").replace("\n", "<br>", regex=True)
        # Rows without a part of speech are the translation, not word analysis:
        # they are rendered outside the table so they are not squeezed into
        # the width of the first column.
        word_mask = sent_df["pos"].astype(str).str.strip().ne("")
        word_df = cast(pd.DataFrame, sent_df[word_mask])
        translations = [
            str(text).strip()
            for text in cast(pd.Series, sent_df.loc[~word_mask, "pali"]).tolist()
            if str(text).strip()
        ]
        if len(word_df):
            word_df.columns = HEADERS
            lines.append(word_df.to_markdown(index=False))
            lines.append("")
        for translation in translations:
            lines.append(f"**{translation}**")
            lines.append("")

    prev_link = (
        f"[← previous]({file_name(sources[idx - 1]['source'])}.md)" if idx > 0 else ""
    )
    index_link = "[index](index.md)"
    rule_encoded = quote(rule)
    feedback_link = f"[Feedback]({FEEDBACK_URL}&entry.1433863141={rule_encoded})"
    next_link = (
        f"[next →]({file_name(sources[idx + 1]['source'])}.md)"
        if idx < len(sources) - 1
        else ""
    )
    nav_parts = [p for p in [prev_link, index_link, feedback_link, next_link] if p]
    lines.append(f"\n{' | '.join(nav_parts)}")
    (output_dir / f"{file_name(rule)}.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "xlsx",
        nargs="?",
        default=str(Path(__file__).parent.parent / "temp" / "patimokkha.xlsx"),
    )
    args = parser.parse_args()
    xlsx_path = Path(args.xlsx)
    if not xlsx_path.exists():
        raise FileNotFoundError(f"XLSX not found: {xlsx_path}")

    output_dir = (
        Path(__file__).parent.parent / "docs" / "6-pali-class" / "bhikkhu-patimokkha"
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    df = load_data(xlsx_path)
    sources = get_sources(df)
    generate_index(sources, output_dir)
    for idx, source in enumerate(sources):
        generate_rule_page(source, df, output_dir, sources, idx)
    print(f"Generated index.md + {len(sources)} rule pages -> {output_dir}")


if __name__ == "__main__":
    main()
