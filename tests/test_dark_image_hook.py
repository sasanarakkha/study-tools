# Tests that the dark image hook pairs light/dark twins and tags twin-less images by brightness.
from pathlib import Path
from types import SimpleNamespace
from typing import cast

from bs4 import BeautifulSoup, Tag
from PIL import Image

from tools.dark_image_hook import on_page_content, on_pre_build

PAGE = SimpleNamespace(url="5-anki/general/updating/")
IMG_DIR = "assets/images/anki"
REL = "../../../assets/images/anki"


def _png(path: Path, shade: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new("RGB", (8, 8), (shade, shade, shade)).save(path)


def _run(docs: Path, html: str, page: SimpleNamespace = PAGE) -> list[Tag]:
    on_pre_build({"docs_dir": str(docs)})
    out = on_page_content(html, page, {"docs_dir": str(docs)}, None)
    return cast(list[Tag], BeautifulSoup(out, "html.parser").find_all("img"))


def _classes(img: Tag) -> list[str]:
    value = img.get("class") or []
    return [value] if isinstance(value, str) else list(cast(list[str], value))


def test_b_suffix_with_d_twin_becomes_light_dark_pair(tmp_path: Path) -> None:
    _png(tmp_path / IMG_DIR / "x-b.png", 240)
    _png(tmp_path / IMG_DIR / "x-d.png", 20)
    imgs = _run(tmp_path, f'<p><img alt="A" src="{REL}/x-b.png"></p>')
    assert [i["src"] for i in imgs] == [
        f"{REL}/x-b.png#only-light",
        f"{REL}/x-d.png#only-dark",
    ]
    assert [i["alt"] for i in imgs] == ["A", "A"]
    assert not any("sbs-auto-dark" in _classes(i) for i in imgs)


def test_unsuffixed_image_with_d_twin_becomes_pair(tmp_path: Path) -> None:
    _png(tmp_path / IMG_DIR / "y.png", 240)
    _png(tmp_path / IMG_DIR / "y-d.png", 20)
    imgs = _run(tmp_path, f'<img alt="B" src="{REL}/y.png">')
    assert [i["src"] for i in imgs] == [
        f"{REL}/y.png#only-light",
        f"{REL}/y-d.png#only-dark",
    ]


def test_light_image_without_twin_gets_auto_dark_class(tmp_path: Path) -> None:
    _png(tmp_path / IMG_DIR / "z.png", 240)
    imgs = _run(tmp_path, f'<img class="keep" alt="C" src="{REL}/z.png">')
    assert len(imgs) == 1
    assert imgs[0]["src"] == f"{REL}/z.png"
    assert _classes(imgs[0]) == ["keep", "sbs-auto-dark"]


def test_dark_image_without_twin_gets_auto_light_class(tmp_path: Path) -> None:
    _png(tmp_path / IMG_DIR / "w.png", 30)
    imgs = _run(tmp_path, f'<img alt="D" src="{REL}/w.png">')
    assert len(imgs) == 1
    assert _classes(imgs[0]) == ["sbs-auto-light"]


def test_existing_fragment_is_left_alone(tmp_path: Path) -> None:
    _png(tmp_path / IMG_DIR / "v-b.png", 240)
    _png(tmp_path / IMG_DIR / "v-d.png", 20)
    html = f'<img alt="E" src="{REL}/v-b.png#only-light">'
    imgs = _run(tmp_path, html)
    assert len(imgs) == 1
    assert imgs[0]["src"] == f"{REL}/v-b.png#only-light"
    assert _classes(imgs[0]) == []


def test_external_image_is_left_alone(tmp_path: Path) -> None:
    html = '<img alt="F" src="https://example.org/u.png">'
    imgs = _run(tmp_path, html)
    assert len(imgs) == 1
    assert imgs[0]["src"] == "https://example.org/u.png"
    assert _classes(imgs[0]) == []


def test_src_resolves_against_page_output_url(tmp_path: Path) -> None:
    # MkDocs has already rewritten src relative to the page's output URL, so a
    # directory-URL page reaches assets/ with one extra "../" than its .md source.
    _png(tmp_path / IMG_DIR / "d-b.png", 240)
    _png(tmp_path / IMG_DIR / "d-d.png", 20)
    imgs = _run(tmp_path, f'<img alt="G" src="{REL}/d-b.png">')
    assert len(imgs) == 2
    # The same src from a page one level up does not reach the file: left alone.
    shallow = SimpleNamespace(url="index.html")
    imgs = _run(tmp_path, f'<img alt="G" src="{REL}/d-b.png">', shallow)
    assert len(imgs) == 1
    assert _classes(imgs[0]) == []


def test_svg_without_twin_is_left_alone(tmp_path: Path) -> None:
    svg = tmp_path / IMG_DIR / "s.svg"
    svg.parent.mkdir(parents=True, exist_ok=True)
    svg.write_text('<svg xmlns="http://www.w3.org/2000/svg"/>')
    imgs = _run(tmp_path, f'<p><img src="{REL}/s.svg"></p>')
    assert len(imgs) == 1
    assert _classes(imgs[0]) == []


def test_unreadable_png_without_twin_is_left_alone(tmp_path: Path) -> None:
    broken = tmp_path / IMG_DIR / "broken.png"
    broken.parent.mkdir(parents=True, exist_ok=True)
    broken.write_bytes(b"not a png")
    imgs = _run(tmp_path, f'<p><img src="{REL}/broken.png"></p>')
    assert len(imgs) == 1
    assert _classes(imgs[0]) == []
