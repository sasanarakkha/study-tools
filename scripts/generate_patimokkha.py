"""Generate Markdown pages for Bhikkhu Pātimokkha word-by-word analysis."""
import argparse
from urllib.parse import quote
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
    # Forward fill source and abbrev to handle sparse columns and preserve order
    df["source"] = df["source"].ffill().str.strip()
    df["abbrev"] = df["abbrev"].ffill().str.strip()
    return df.fillna("")

def get_sources(df: pd.DataFrame) -> list[dict]:
    # drop_duplicates preserves the order of the first occurrence by default.
    return (
        df[["source", "abbrev"]]
        .drop_duplicates(subset="source")
        .query("source != ''")
        .to_dict("records")
    )

def generate_index(sources: list[dict], output_dir: Path) -> None:
    lines = ["# Bhikkhu Pātimokkha - Word by Word Analysis\n"]
    for s in sources:
        lines.append(f"- [{s['abbrev']} {s['source']}]({s['source']}.md)")
    (output_dir / "index.md").write_text("\n".join(lines), encoding="utf-8")

def generate_rule_page(source: dict, df: pd.DataFrame, output_dir: Path, sources: list[dict], idx: int) -> None:
    rule, abbrev = source["source"], source["abbrev"]
    rule_df = df[df["source"] == rule]
    lines = [f"# {abbrev} {rule}\n"]
    
    sentences = rule_df["sentence"].drop_duplicates()
    for sentence in sentences:
        if not sentence:
            continue
        lines.append(f"## {sentence}\n")
        sent_df = rule_df[rule_df["sentence"] == sentence][COLS].copy()
        sent_df = sent_df.replace(0, "").replace("\n", "<br>", regex=True)
        sent_df.columns = HEADERS
        lines.append(sent_df.to_markdown(index=False))
        lines.append("")
    
    prev_link = f"[← previous]({sources[idx - 1]['source']}.md)" if idx > 0 else ""
    index_link = "[index](index.md)"
    rule_encoded = quote(rule)
    feedback_link = f"[Feedback]({FEEDBACK_URL}&entry.1433863141={rule_encoded})"
    next_link = f"[next →]({sources[idx + 1]['source']}.md)" if idx < len(sources) - 1 else ""
    nav_parts = [p for p in [prev_link, index_link, feedback_link, next_link] if p]
    lines.append(f"\n{' | '.join(nav_parts)}")
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

    output_dir = Path(__file__).parent.parent / "docs" / "6-pali-class" / "bhikkhu-patimokkha"
    output_dir.mkdir(parents=True, exist_ok=True)

    df = load_data(xlsx_path)
    sources = get_sources(df)
    generate_index(sources, output_dir)
    for idx, source in enumerate(sources):
        generate_rule_page(source, df, output_dir, sources, idx)
    print(f"Generated index.md + {len(sources)} rule pages -> {output_dir}")

if __name__ == "__main__":
    main()
