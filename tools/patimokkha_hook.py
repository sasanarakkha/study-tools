# Applies colspan to patimokkha translation rows and adds CSS class for proportional column widths.
from typing import Any, List, cast, Optional
from bs4 import BeautifulSoup, Tag

def on_post_page(output: str, page: Any, config: Any, **kwargs: Any) -> str:
    # Use getattr for safer access to Any object attributes
    page_file = getattr(page, "file", None)
    if page_file is None:
        return output
        
    src_path = getattr(page_file, "src_path", None)
    if not isinstance(src_path, str) or not src_path.startswith("6-pali-class/bhikkhu-patimokkha/"):
        return output

    soup = BeautifulSoup(output, "html.parser")
    # Cast find_all result to List[Tag] to help Pylance
    tables = cast(List[Tag], soup.find_all("table"))
    
    for table in tables:
        # Pylance might still want an explicit check even after cast
        if not isinstance(table, Tag):
            continue

        existing = table.get("class", [])
        existing_list: List[str] = []
        if isinstance(existing, str):
            existing_list = [existing]
        elif isinstance(existing, list):
            existing_list = cast(List[str], existing)
            
        table.attrs["class"] = existing_list + ["patimokkha-table"]

        headers = cast(List[Tag], table.find_all("th"))
        col_count = len(headers)
        if col_count == 0:
            continue
            
        tbody = table.find("tbody")
        if not isinstance(tbody, Tag):
            continue
            
        rows = cast(List[Tag], tbody.find_all("tr"))
        for tr in rows:
            if not isinstance(tr, Tag):
                continue
                
            # Filter for Tag children only
            tds = [td for td in tr.find_all("td", recursive=False) if isinstance(td, Tag)]
            if len(tds) > 1:
                first_td = tds[0]
                if first_td.get_text(strip=True) != "":
                    if all(td.get_text(strip=True) == "" for td in tds[1:]):
                        first_td.attrs["colspan"] = str(col_count)
                        for td in tds[1:]:
                            td.decompose()
                        
                        tr_existing = tr.get("class", [])
                        tr_existing_list: List[str] = []
                        if isinstance(tr_existing, str):
                            tr_existing_list = [tr_existing]
                        elif isinstance(tr_existing, list):
                            tr_existing_list = cast(List[str], tr_existing)
                            
                        tr.attrs["class"] = tr_existing_list + ["patimokkha-translation"]
                        
    return str(soup)
