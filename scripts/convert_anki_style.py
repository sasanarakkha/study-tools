"""Convert anki-style/*.txt files to docs/anki/*.md with code block wrapping."""
from pathlib import Path

SRC = Path("anki-style")
DST = Path("docs/anki")
DST.mkdir(parents=True, exist_ok=True)

for txt_file in sorted(SRC.glob("*.txt")):
    content = txt_file.read_text(encoding="utf-8")
    name = txt_file.stem

    if name.startswith("field-list"):
        deck = name.replace("field-list-", "").replace("-", " ").title()
        title = f"# Field List: {deck}"
        body = f"```\n{content}\n```"
    elif name.endswith(("-front", "-back")):
        suffix = "Front" if name.endswith("-front") else "Back"
        deck = name.replace("-front", "").replace("-back", "").replace("-", " ").title()
        title = f"# {deck} — {suffix} Template"
        body = f"```html\n{content}\n```"
    elif "styling" in name:
        deck = name.replace("-", " ").title()
        title = f"# {deck}"
        body = f"```css\n{content}\n```"
    else:
        title = f"# {name.replace('-', ' ').title()}"
        body = f"```\n{content}\n```"

    md_path = DST / f"{name}.md"
    md_path.write_text(f"{title}\n\n{body}\n", encoding="utf-8")
    print(f"  {txt_file.name} → {md_path}")

print(f"Done: {len(list(SRC.glob('*.txt')))} files converted.")
