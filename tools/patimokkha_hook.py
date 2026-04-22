# Applies colspan to patimokkha translation rows and adds CSS class for proportional column widths.
from bs4 import BeautifulSoup

def on_post_page(output, page, config, **kwargs):
    if not page.file.src_path.startswith("6-pali-class/bhikkhu-patimokkha/"):
        return output

    soup = BeautifulSoup(output, "html.parser")
    for table in soup.find_all("table"):
        existing = table.get("class", [])
        table["class"] = existing + ["patimokkha-table"]

        headers = table.find_all("th")
        col_count = len(headers)
        if col_count == 0:
            continue
        tbody = table.find("tbody")
        if not tbody:
            continue
        for tr in tbody.find_all("tr"):
            tds = tr.find_all("td")
            if len(tds) > 1 and tds[0].get_text(strip=True) != "":
                if all(td.get_text(strip=True) == "" for td in tds[1:]):
                    tds[0]["colspan"] = str(col_count)
                    for td in tds[1:]:
                        td.decompose()
                    tr["class"] = tr.get("class", []) + ["patimokkha-translation"]
    return str(soup)
