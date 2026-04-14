# plan.md — Thread 2: Pātimokkha Generation

**GitHub issue:** sasanarakkha/dpd-db-sbs#21
**Depends on:** 20260413_core-migration merged

---

## Phase 1 — Dependencies & Download Script

- [~] Add pandas, openpyxl, tabulate to `pyproject.toml` dependencies:
  ```toml
  "pandas>=2.0",
  "openpyxl>=3.1",
  "tabulate>=0.9",
  ```
  Then run `uv sync` to update `uv.lock`.
  → verify: `uv run python -c "import pandas, openpyxl, tabulate"` exits 0

- [~] Create `scripts/download_patimokkha.sh`:
  ```bash
  #!/usr/bin/env bash
  # Download the Pātimokkha Word by Word spreadsheet from Google Sheets.
  set -euo pipefail

  XLSX_URL="https://docs.google.com/spreadsheets/d/1rS-IlX4DvKmnBO58KON37eVnOZqwfkG-ot-zIjCuzH4/export?format=xlsx"
  OUT_DIR="$(dirname "$0")/../temp"
  OUT_FILE="$OUT_DIR/patimokkha.xlsx"

  mkdir -p "$OUT_DIR"

  if ! ping -c 1 google.com &>/dev/null; then
      echo "Error: no internet connection." >&2
      exit 1
  fi

  echo "Downloading Pātimokkha XLSX..."
  curl -L "$XLSX_URL" -o "$OUT_FILE"

  if [ ! -f "$OUT_FILE" ]; then
      echo "Error: download failed." >&2
      exit 1
  fi

  echo "Saved to $OUT_FILE"
  ```
  Make executable: `chmod +x scripts/download_patimokkha.sh`
  Add to `scripts/cl/` symlink or README as a runnable script.
  → verify: `bash scripts/download_patimokkha.sh` downloads `temp/patimokkha.xlsx`

**Phase 1 complete when:** `temp/patimokkha.xlsx` exists after running
the download script.

---

## Phase 2 — Generation Script

- [~] Create `scripts/generate_patimokkha.py` — full implementation:

  ```python
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
      return df.fillna("")

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
  ```
  → verify: `uv run python scripts/generate_patimokkha.py` runs without
    error and creates `docs/bhikkhu_patimokkha/index.md` + rule `.md` files

- [ ] Inspect generated output:
  - `docs/bhikkhu_patimokkha/index.md` contains list of rules with `.md` links
  - Open one rule `.md` in editor: confirm Markdown table present, footer links correct
  - Count rule files: `ls docs/bhikkhu_patimokkha/*.md | wc -l`
  → verify: index.md exists; rule count ≥ 200; no absolute web URLs in any file

- [~] Add `bhikkhu_patimokkha` section to `mkdocs.yaml` nav:
  ```yaml
  - Bhikkhu Pātimokkha:
    - Index: bhikkhu_patimokkha/index.md
  ```
  → verify: entry added to nav block

**Phase 2 complete when:** generation script produces correct output
and nav is updated.

---

## Phase 3 — Local Rendering Verification

- [~] Run `uv run mkdocs serve` and check in browser:
  - Navigate to Bhikkhu Pātimokkha → Index page loads, rule links visible
  - Click one rule link: page loads with Markdown table rendered correctly
  - `[← Home]` link navigates back to index
  - Feedback link present at bottom of rule page
  - No broken links in browser console
  → verify: all above pass

- [ ] Check URL encoding: open a rule with Pāli diacritics in the filename
  (e.g. Pārājika) — confirm URL is accessible and page loads
  → verify: page loads at the diacritic URL

**Phase 3 complete when:** pages render correctly in local serve.

---

## Phase 4 — Weekly GitHub Action

- [~] Create `.github/workflows/regen_patimokkha.yaml`:
  ```yaml
  name: Regenerate Pātimokkha Pages

  on:
    schedule:
      - cron: '0 3 * * 1'   # Monday 03:00 UTC
    workflow_dispatch:

  permissions:
    contents: write

  jobs:
    regen:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
          with:
            token: ${{ secrets.GITHUB_TOKEN }}

        - uses: astral-sh/setup-uv@v5
          with:
            enable-cache: true
            python-version: "3.12"

        - run: uv sync --frozen

        - name: Download Pātimokkha XLSX
          run: bash scripts/download_patimokkha.sh

        - name: Generate Markdown pages
          run: uv run python scripts/generate_patimokkha.py

        - name: Commit and push if changed
          run: |
            git config user.name  "github-actions[bot]"
            git config user.email "github-actions[bot]@users.noreply.github.com"
            git add docs/bhikkhu_patimokkha/
            if git diff --cached --quiet; then
              echo "No changes — skipping commit"
            else
              git commit -m "regen: patimokkha pages (sasanarakkha/dpd-db-sbs#21)"
              git push
            fi
  ```
  → verify: file created at `.github/workflows/regen_patimokkha.yaml`

- [ ] Test via manual dispatch:
  - Push workflow file to main
  - Trigger `workflow_dispatch` from GitHub Actions tab
  → verify: workflow runs green; commit appears (or "No changes" if XLSX
    unchanged since last run)

**Phase 4 complete when:** workflow runs green on manual dispatch.

---

## Phase 5 — Commit Preparation

- [x] Stage all new files:
  ```bash
  git add scripts/download_patimokkha.sh \
          scripts/generate_patimokkha.py \
          docs/bhikkhu_patimokkha/ \
          mkdocs.yaml \
          pyproject.toml uv.lock \
          .github/workflows/regen_patimokkha.yaml
  ```
  Draft commit message:
  ```
  sasanarakkha/dpd-db-sbs#21: add patimokkha md generation + weekly action
  ```

**Phase 5 complete when:** commit staged and ready for user review.

---

## Errors & Issues Log

*(Append new findings here during implementation — never overwrite)*
