"""Generate Markdown pages for Bhikkhu Pātimokkha word-by-word analysis."""
import argparse
from pathlib import Path
import pandas as pd

FEEDBACK_URL = (
    "https://docs.google.com/forms/d/e/"
    "1FAIpQLSdG6zKDtlwibtrX-cbKVn4WmIs8miH4VnuJvb7f94plCDKJyA/"
    "viewform?usp=pp_url"
)
COLS = [
    "pali_1", "pos", "grammar", "case", "meaning",
    "meaning_lit", "root", "base", "construction",
    "compound_type", "compound_construction",
]
HEADERS = [
    "pāḷi", "pos", "grammar", "case", "meaning",
    "meaning_lit", "root", "base", "construction",
    "compound_type", "compound_construction",
]

def load_data(xlsx_path: Path) -> pd.DataFrame:
    df = pd.read_excel(xlsx_path, engine="openpyxl")
    df = df.fillna("")
    # Strip whitespace and remove all newlines/carriage returns from all cells
    # We cast to str first to ensure replace and strip work consistently
    df = df.astype(str).replace(r"[\r\n]+", " ", regex=True)
    return df.apply(lambda x: x.str.strip())

def get_sources(df: pd.DataFrame) -> list[dict]:
    return (
        df[["source", "abbrev"]]
        .drop_duplicates(subset="source")
        .query("source != ''")
        .to_dict("records")
    )

def generate_index(sources: list[dict], output_dir: Path) -> None:
    lines = ["# [SBS] Bhikkhu Pātimokkha\n"]
    for s in sources:
        lines.append(f"- [{s['abbrev']} {s['source']}]({s['source']}.md)")
    (output_dir / "index.md").write_text("\n".join(lines), encoding="utf-8")

def generate_rule_page(source: dict, df: pd.DataFrame, output_dir: Path) -> None:
    rule, abbrev = source["source"], source["abbrev"]
    rule_df = df[df["source"] == rule]
    lines = [f"# {abbrev} {rule}\n"]
    for sentence in rule_df["sentence"].drop_duplicates():
        if not sentence:
            continue
        lines.append(f"## {sentence}\n")
        sent_df = rule_df[rule_df["sentence"] == sentence][COLS].copy()
        sent_df.columns = HEADERS
        lines.append(sent_df.to_markdown(index=False))
        lines.append("")
    lines.append(f"\n[← Home](index.md) | [Feedback]({FEEDBACK_URL})")
    (output_dir / f"{rule}.md").write_text("\n".join(lines), encoding="utf-8")

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "xlsx", nargs="?",
        default=str(Path(__file__).parent.parent / "temp" / "patimokkha.xlsx"),
    )
    args = parser.parse_args()
    xlsx_path = Path(args.xlsx)
    if not xlsx_path.exists():
        raise FileNotFoundError(f"XLSX not found: {xlsx_path}")

    output_dir = Path(__file__).parent.parent / "docs" / "bhikkhu_patimokkha"
    output_dir.mkdir(parents=True, exist_ok=True)

    df = load_data(xlsx_path)
    sources = get_sources(df)
    generate_index(sources, output_dir)
    for source in sources:
        generate_rule_page(source, df, output_dir)
    print(f"Generated index.md + {len(sources)} rule pages → {output_dir}")

if __name__ == "__main__":
    main()
