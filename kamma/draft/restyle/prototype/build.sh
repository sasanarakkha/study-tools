#!/bin/bash
# Builds one restyle prototype (p1, p2 or p3) into temp/restyle/<variant>/site without touching docs/, identity/ or mkdocs.yaml.
# Usage (from the repo root):  bash kamma/draft/restyle/prototype/build.sh p2
set -e

VARIANT="${1:-p2}"
case "$VARIANT" in p1|p2|p3) ;; *) echo "usage: build.sh p1|p2|p3"; exit 1 ;; esac

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
PROTO="$ROOT/kamma/draft/restyle/prototype"
OUT="$ROOT/temp/restyle/$VARIANT"

rm -rf "$OUT"
mkdir -p "$OUT/identity"
cp "$ROOT/identity/sbs.js" "$OUT/identity/"
cp "$PROTO"/identity/*.svg "$PROTO"/identity/*.png "$OUT/identity/"
cp "$PROTO/identity/sbs.$VARIANT.css" "$OUT/identity/sbs.css"

HOOKS="  - $ROOT/tools/patimokkha_hook.py"
if [ "$VARIANT" != "p1" ]; then
  HOOKS="$HOOKS
  - $PROTO/tools/home_hook.py"
fi

cat > "$OUT/mkdocs.yaml" <<YAML
INHERIT: $ROOT/mkdocs.yaml
docs_dir: $ROOT/docs
site_dir: $OUT/site
theme:
  custom_dir: $OUT/identity
  logo: sbs-mark.svg
  favicon: sbs-favicon-48.png
  palette:
    - media: '(prefers-color-scheme: light)'
      scheme: default
      primary: custom
      accent: custom
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - media: '(prefers-color-scheme: dark)'
      scheme: slate
      primary: custom
      accent: custom
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
hooks:
$HOOKS
YAML

if [ "$VARIANT" != "p1" ]; then
  cat >> "$OUT/mkdocs.yaml" <<'YAML'
copyright: 'Sāsanārakkha Buddhist Sanctuary · <a href="https://sasanarakkha.org/">sasanarakkha.org</a> · <a href="http://creativecommons.org/licenses/by-nc/4.0/">CC BY-NC 4.0</a>'
extra:
  generator: false
  social:
    - icon: fontawesome/solid/house
      link: https://sasanarakkha.org/
      name: Sāsanārakkha Buddhist Sanctuary
    - icon: fontawesome/brands/github
      link: https://github.com/sasanarakkha/study-tools
      name: Source on GitHub
    - icon: fontawesome/solid/envelope
      link: mailto:studytools@sasanarakkha.org
      name: Contact us
YAML
fi

cd "$ROOT"
uv run mkdocs build -q -f "$OUT/mkdocs.yaml"
echo "Built $VARIANT -> $OUT/site"
echo "Preview: cd $OUT/site && python3 -m http.server 8765   then open http://127.0.0.1:8765/"
