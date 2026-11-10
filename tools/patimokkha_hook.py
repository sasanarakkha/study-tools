# Adds the CSS class that gives patimokkha tables proportional column widths.
from typing import Any, List, cast
from bs4 import BeautifulSoup, Tag


def on_post_page(output: str, page: Any, config: Any, **kwargs: Any) -> str:
    # Use getattr for safer access to Any object attributes
    page_file = getattr(page, "file", None)
    if page_file is None:
        return output

    src_path = getattr(page_file, "src_path", None)
    if not isinstance(src_path, str) or not src_path.startswith(
        "6-pali-class/bhikkhu-patimokkha/"
    ):
        return output

    soup = BeautifulSoup(output, "html.parser")
    # Cast find_all result to List[Tag] to help Pylance
    tables = cast(List[Tag], soup.find_all("table"))

    for table in tables:
        # Pylance might still want an explicit check even after cast
        if not isinstance(table, Tag):
            continue

        existing = table.get("class") or []
        existing_list: List[str] = []
        if isinstance(existing, str):
            existing_list = [existing]
        elif isinstance(existing, list):
            existing_list = cast(List[str], existing)

        table.attrs["class"] = " ".join(existing_list + ["patimokkha-table"])

    return str(soup)
