# Restructures the rendered home page into a hero band and a grid of section cards.
from typing import Any, List, cast

from bs4 import BeautifulSoup, Tag

HOME_SRC_PATH = "index.md"


def _classes(tag: Tag) -> List[str]:
    """Return the tag's current classes as a list of strings."""
    existing = tag.get("class") or []
    if isinstance(existing, str):
        return [existing]
    return list(cast(List[str], existing))


def restructure_home(output: str) -> str:
    """Return the home page HTML with hero, card grid and closing note marked up.

    The markdown source stays plain: a heading, intro paragraphs, a rule, closing
    paragraphs and a list of section links. Nothing is removed; elements are only
    wrapped, given classes, or moved.
    """
    soup = BeautifulSoup(output, "html.parser")
    article = soup.select_one("article.md-content__inner")
    body = soup.body
    if article is None or body is None:
        return output

    heading = article.find("h1", recursive=False)
    rule = article.find("hr", recursive=False)
    lists = article.find_all("ul", recursive=False)
    if not isinstance(heading, Tag) or not isinstance(rule, Tag) or not lists:
        return output
    cards = lists[-1]
    if not isinstance(cards, Tag):
        return output

    body.attrs["class"] = " ".join([*_classes(body), "sbs-home"])

    # Hero: the heading and everything up to the horizontal rule.
    hero = soup.new_tag("div", attrs={"class": "sbs-hero"})
    heading.insert_before(hero)
    node = hero.next_sibling
    while node is not None and node is not rule:
        following = node.next_sibling
        hero.append(node.extract())
        node = following

    # Cards: the last list of section links, moved directly under the hero.
    cards.attrs["class"] = " ".join([*_classes(cards), "sbs-cards"])
    hero.insert_after(cards.extract())

    # Closing note: what remains between the rule and the end of the article.
    foot = soup.new_tag("div", attrs={"class": "sbs-home-foot"})
    rule.insert_before(foot)
    node = foot.next_sibling
    while node is not None:
        following = node.next_sibling
        foot.append(node.extract())
        node = following

    return str(soup)


def on_post_page(output: str, page: Any, config: Any, **kwargs: Any) -> str:
    page_file = getattr(page, "file", None)
    if getattr(page_file, "src_path", None) != HOME_SRC_PATH:
        return output
    return restructure_home(output)
