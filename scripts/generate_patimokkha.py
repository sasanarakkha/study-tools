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
BOLD_TAG = r"</?b>"
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


class Page(TypedDict):
    """One generated page: a contiguous run of rows for a rule or a section.

    A section such as pācittiyā is stored in two runs, one before its rules and
    one after, so it produces two pages: `pc` and `pc-end`.
    """

    run: int
    abbrev: str
    source: str
    run_of_rule: int
    filename: str


def load_data(tsv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(tsv_path, sep="\t", dtype=str, keep_default_na=False)
    # Bold is kept as <b> tags in the source (Anki needs it); Markdown pages stay clean.
    df = df.replace(BOLD_TAG, "", regex=True)
    # Blank cells are "", so turn them into NA or the ffill below would do nothing.
    df[["source", "abbrev"]] = df[["source", "abbrev"]].replace("", pd.NA)
    # Forward fill source and abbrev to handle sparse columns and preserve order
    df["source"] = df["source"].ffill().str.strip()
    df["abbrev"] = df["abbrev"].ffill().str.strip()
    return assign_orphan_sentences(df.fillna(""))


def text(value: object) -> str:
    return str(value).strip()


def assign_orphan_sentences(df: pd.DataFrame) -> pd.DataFrame:
    """Assign every row to a rule run and give orphan rows their sentence.

    A run is a contiguous block of rows sharing an abbreviation. Sections are
    stored as two runs separated by their rules, so the run — not the name — is
    the unit of a page. Inheritance of a blank `sentence` stops at run
    boundaries, and rows of two rules with the same name never share a run.

    The sheet stores each rule's English translation on a row of its own and
    usually leaves that row's `sentence` cell empty, so grouping rows by
    `sentence` would drop the translation. Such rows inherit the preceding
    sentence. Rows whose text is itself a sentence of the Pāḷi text (the
    heading of the following rule, which the sheet places inside the previous
    rule's block) and section labels ("PA 1", "PC 42") are left blank so they
    stay excluded.
    """
    sentences = cast(list[object], df["sentence"].tolist())
    words = cast(list[object], df["pali"].tolist())
    abbrevs = cast(list[object], df["abbrev"].tolist())

    known_sentences = {text(s) for s in sentences if text(s)}

    resolved: list[str] = []
    run_ids: list[int] = []
    current = ""
    current_abbrev = ""
    run = -1
    runs = -1
    for sentence_value, word_value, abbrev_value in zip(
        sentences, words, abbrevs, strict=True
    ):
        abbrev = text(abbrev_value)
        if abbrev != current_abbrev:
            current_abbrev, current = abbrev, ""
            if abbrev:
                runs += 1
                run = runs
            else:
                run = -1
        sentence = text(sentence_value)
        word = text(word_value)
        if not word or SECTION_LABEL.match(word):
            sentence = ""
        elif sentence:
            current = sentence
        elif word in known_sentences:
            sentence = ""
        else:
            sentence = current
        resolved.append(sentence)
        run_ids.append(run)

    df["sentence"] = resolved
    df["run"] = run_ids
    return df


def code_slug(abbrev: str) -> str:
    """Lowercase a rule code and use hyphens for its spaces ("PA 1" -> "pa-1")."""
    return re.sub(r"\s+", "-", abbrev.strip().lower())


def page_filename(ordinal: int, abbrev: str, run_of_rule: int) -> str:
    """Name a page so the folder lists it in recitation order.

    The leading ordinal keeps the folder sorted exactly as the text is recited;
    the rule code makes the name unique even when two rules share a name.
    """
    name = f"{ordinal:03d}-{code_slug(abbrev)}"
    if run_of_rule == 1:
        name += "-end"
    elif run_of_rule > 1:
        name += f"-end-{run_of_rule}"
    return f"{name}.md"


def get_pages(df: pd.DataFrame) -> list[Page]:
    """Return one page per run, in recitation order."""
    pages: list[Page] = []
    seen: dict[str, int] = {}
    for run, group in df.groupby("run", sort=True):
        run_id = cast(int, run)
        if run_id < 0:
            continue
        first = group.iloc[0]
        abbrev = text(first["abbrev"])
        source = next((text(s) for s in group["source"] if text(s)), abbrev)
        run_of_rule = seen.get(abbrev, 0)
        seen[abbrev] = run_of_rule + 1
        pages.append(
            {
                "run": run_id,
                "abbrev": abbrev,
                "source": source,
                "run_of_rule": run_of_rule,
                "filename": page_filename(len(pages) + 1, abbrev, run_of_rule),
            }
        )
    filenames = [page["filename"] for page in pages]
    if len(set(filenames)) != len(filenames):
        duplicates = sorted({name for name in filenames if filenames.count(name) > 1})
        raise ValueError(f"Duplicate page filenames: {duplicates}")
    return pages


def generate_index(pages: list[Page], output_dir: Path) -> None:
    lines = ["# Bhikkhu Pātimokkha - Word by Word Analysis\n"]
    for page in pages:
        label = f"{page['abbrev']} {page['source']}"
        if page["run_of_rule"]:
            label += " — closing"
        lines.append(f"- [{label}]({page['filename']})")
    (output_dir / "index.md").write_text("\n".join(lines), encoding="utf-8")


def strip_anki_number(value: str) -> str:
    """Drop the Anki disambiguation suffix from a Pāḷi cell ("kallaṃ 2" -> "kallaṃ").

    The sheet numbers repeated headwords so the Anki exporter can tell them
    apart. Markdown readers do not need the numbers; section labels such as
    "PA 1" never reach this function because they are excluded as labels first.
    """
    return re.sub(r"\s+\d+$", "", value)


def normalize_cell(value: object) -> str:
    """Fold a multi-line sheet cell into one clean line of Markdown text.

    Tables cannot hold a line break without raw HTML, so alternatives that the
    sheet writes on separate lines are joined with " / " (the separator the
    sheet itself uses, e.g. "suṇātu me bhante / āvuso saṅgho"). A line that only
    carries a marker such as "(or)" is attached to the line that follows it, and
    a line starting with punctuation is joined directly.
    """
    lines = [line.strip() for line in str(value).splitlines() if line.strip()]
    if not lines:
        return ""
    folded: list[str] = []
    pending: list[str] = []
    for line in lines:
        if re.fullmatch(r"\([A-Za-z.]+\)", line):
            pending.append(line)
            continue
        folded.append(" ".join(pending + [line]))
        pending = []
    if pending:
        folded.append(" ".join(pending))
    text = folded[0]
    for line in folded[1:]:
        if re.search(r"\([A-Za-z.]+\)$", text) or line.startswith("("):
            separator = " "
        elif line[0] in ",.;:":
            separator = " "
        else:
            separator = " / "
        text += separator + line
    text = re.sub(r"\s+", " ", text)
    return re.sub(r"\s+([,.;:])", r"\1", text)


def generate_rule_page(
    page: Page,
    df: pd.DataFrame,
    output_dir: Path,
    pages: list[Page],
    idx: int,
) -> None:
    rule, abbrev = page["source"], page["abbrev"]
    rule_df = cast(pd.DataFrame, df[df["run"] == page["run"]])
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
        sent_df = sent_df.replace(0, "")
        for column in COLS:
            sent_df[column] = sent_df[column].map(normalize_cell)
        sent_df["pali"] = sent_df["pali"].map(strip_anki_number)
        # Rows without a part of speech are the translation, not word analysis:
        # they are rendered outside the table so they are not squeezed into
        # the width of the first column.
        word_mask = sent_df["pos"].astype(str).str.strip().ne("")
        word_df = cast(pd.DataFrame, sent_df[word_mask])
        translations = [
            translation
            for translation in cast(pd.Series, sent_df.loc[~word_mask, "pali"]).tolist()
            if translation
        ]
        if len(word_df):
            word_df.columns = HEADERS
            lines.append(word_df.to_markdown(index=False))
            lines.append("")
        for translation in translations:
            lines.append(f"**{translation}**")
            lines.append("")

    prev_link = f"[← previous]({pages[idx - 1]['filename']})" if idx > 0 else ""
    index_link = "[index](index.md)"
    rule_encoded = quote(rule)
    feedback_link = f"[Feedback]({FEEDBACK_URL}&entry.1433863141={rule_encoded})"
    next_link = (
        f"[next →]({pages[idx + 1]['filename']})" if idx < len(pages) - 1 else ""
    )
    nav_parts = [
        part for part in [prev_link, index_link, feedback_link, next_link] if part
    ]
    lines.append(f"\n{' | '.join(nav_parts)}")
    (output_dir / page["filename"]).write_text("\n".join(lines), encoding="utf-8")


def prune_stale_pages(output_dir: Path, pages: list[Page], enabled: bool) -> list[Path]:
    """Delete generated pages that this run did not produce.

    Adding or removing a rule renumbers every following page, so without this
    the folder keeps a copy of the old numbering. Only `NNN-*.md` files are
    considered; `index.md` and anything else in the folder is left alone.
    """
    if not enabled:
        return []
    keep = {page["filename"] for page in pages}
    removed: list[Path] = []
    for path in sorted(output_dir.glob("[0-9][0-9][0-9]-*.md")):
        if path.name not in keep:
            path.unlink()
            removed.append(path)
    return removed


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
        "--no-prune",
        action="store_true",
        help="Keep generated pages that this run did not produce.",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Where to write the pages (default: docs/6-pali-class/bhikkhu-patimokkha).",
    )
    args = parser.parse_args()
    tsv_path = Path(args.tsv)
    if not tsv_path.exists():
        raise FileNotFoundError(f"TSV not found: {tsv_path}")

    output_dir = (
        Path(args.output_dir)
        if args.output_dir
        else Path(__file__).parent.parent
        / "docs"
        / "6-pali-class"
        / "bhikkhu-patimokkha"
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    df = load_data(tsv_path)
    pages = get_pages(df)
    if not pages:
        raise SystemExit(
            f"No pages generated from {tsv_path}; refusing to overwrite {output_dir}."
        )
    generate_index(pages, output_dir)
    for idx, page in enumerate(pages):
        generate_rule_page(page, df, output_dir, pages, idx)
    removed = prune_stale_pages(output_dir, pages, not args.no_prune)
    print(
        f"Generated index.md + {len(pages)} rule pages -> {output_dir} "
        f"(removed {len(removed)} stale pages)"
    )


if __name__ == "__main__":
    main()
