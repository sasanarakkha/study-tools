# Tests that the home page hook restructures index.html without losing content.
from types import SimpleNamespace
from typing import cast

from bs4 import BeautifulSoup, Tag

from tools.home_hook import on_post_page, restructure_home

LINKS = ["1-one/", "2-two/", "3-three/"]

PAGE = (
    '<html><body><article class="md-content__inner md-typeset">'
    "<h1>Title</h1><p>Intro one.</p><p>Intro two.</p>"
    "<hr><p>Closing note.</p>"
    + "<ul>"
    + "".join(f'<li><a href="{h}">Link {h}</a></li>' for h in LINKS)
    + "</ul>"
    "</article></body></html>"
)

NO_RULE = PAGE.replace("<hr>", "")


def _article(html: str) -> Tag:
    article = BeautifulSoup(html, "html.parser").select_one("article")
    assert isinstance(article, Tag)
    return article


def _texts(html: str) -> list[str]:
    return [s.strip() for s in _article(html).stripped_strings]


def _hrefs(html: str) -> list[str]:
    return sorted(str(a["href"]) for a in _article(html).find_all("a"))


def test_all_text_and_links_preserved() -> None:
    result = restructure_home(PAGE)
    assert sorted(_texts(result)) == sorted(_texts(PAGE))
    assert _hrefs(result) == sorted(LINKS)


def test_cards_list_follows_hero() -> None:
    article = _article(restructure_home(PAGE))
    hero = article.select_one(".sbs-hero")
    assert isinstance(hero, Tag)
    nxt = hero.find_next_sibling()
    assert isinstance(nxt, Tag)
    assert nxt.name == "ul"
    assert "sbs-cards" in cast(list[str], nxt.get("class"))


def test_hero_holds_heading_and_pre_rule_paragraphs_only() -> None:
    hero = _article(restructure_home(PAGE)).select_one(".sbs-hero")
    assert isinstance(hero, Tag)
    assert [c.name for c in hero.find_all(recursive=False)] == ["h1", "p", "p"]
    assert hero.get_text(" ", strip=True) == "Title Intro one. Intro two."


def test_foot_holds_rule_and_post_rule_paragraph() -> None:
    foot = _article(restructure_home(PAGE)).select_one(".sbs-home-foot")
    assert isinstance(foot, Tag)
    assert [c.name for c in foot.find_all(recursive=False)] == ["hr", "p"]
    assert foot.get_text(strip=True) == "Closing note."


def test_body_gets_home_class() -> None:
    body = BeautifulSoup(restructure_home(PAGE), "html.parser").body
    assert body is not None
    assert "sbs-home" in cast(list[str], body.get("class"))


def test_page_without_rule_is_unchanged() -> None:
    assert restructure_home(NO_RULE) == NO_RULE


def test_other_pages_are_untouched_by_hook() -> None:
    other = SimpleNamespace(file=SimpleNamespace(src_path="2-sbs-book/index.md"))
    assert on_post_page(PAGE, other, {}) == PAGE
    home = SimpleNamespace(file=SimpleNamespace(src_path="index.md"))
    assert on_post_page(PAGE, home, {}) != PAGE
