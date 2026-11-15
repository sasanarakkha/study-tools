# Pairs light/dark screenshot twins and tags twin-less images so CSS can invert them per colour scheme.
import posixpath
from pathlib import Path
from typing import Any, List, Optional, Set, cast

from bs4 import BeautifulSoup, Tag
from PIL import Image, ImageStat

from tools.printer import printer as pr

LIGHT_THRESHOLD = 128
RASTER_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp"}

_pairs: Set[str] = set()
_auto_dark: Set[str] = set()
_auto_light: Set[str] = set()
_brightness: dict[Path, Optional[float]] = {}


def _classes(tag: Tag) -> List[str]:
    """Return the tag's current classes as a list of strings."""
    existing = tag.get("class") or []
    if isinstance(existing, str):
        return [existing]
    return list(cast(List[str], existing))


def _dark_twin_name(filename: str) -> str:
    """Return the dark twin's filename: drop one trailing '-b' from the stem, add '-d'."""
    path = Path(filename)
    stem = path.stem[:-2] if path.stem.endswith("-b") else path.stem
    return f"{stem}-d{path.suffix}"


def _mean_brightness(path: Path) -> Optional[float]:
    """Return the mean greyscale brightness (0-255) of an image, or None if unreadable."""
    if path in _brightness:
        return _brightness[path]
    value: Optional[float] = None
    if path.suffix.lower() in RASTER_SUFFIXES:
        try:
            with Image.open(path) as image:
                value = float(ImageStat.Stat(image.convert("L")).mean[0])
        except OSError:
            value = None
    _brightness[path] = value
    return value


def _resolve(src: str, page_url: str, docs_dir: Path) -> Optional[Path]:
    """Map a rendered img src to a file under docs_dir, or None if it is not one."""
    if "://" in src or src.startswith(("//", "data:")) or "#" in src:
        return None
    base = (
        page_url
        if page_url.endswith("/") or not page_url
        else posixpath.dirname(page_url)
    )
    relative = posixpath.normpath(posixpath.join(base, src))
    path = docs_dir / relative
    if relative.startswith("..") or not path.is_file():
        return None
    return path


def on_pre_build(config: Any, **kwargs: Any) -> None:
    """Reset the per-build counters and brightness cache."""
    _pairs.clear()
    _auto_dark.clear()
    _auto_light.clear()
    _brightness.clear()


def on_page_content(
    html: str, page: Any, config: Any, files: Any = None, **kwargs: Any
) -> str:
    docs_dir = Path(str(config["docs_dir"]))
    page_url = str(getattr(page, "url", ""))
    soup = BeautifulSoup(html, "html.parser")
    changed = False

    for img in cast(List[Tag], soup.find_all("img")):
        src = img.get("src")
        if not isinstance(src, str):
            continue
        path = _resolve(src, page_url, docs_dir)
        if path is None:
            continue

        twin_name = _dark_twin_name(path.name)
        if twin_name != path.name and (path.parent / twin_name).is_file():
            dark = BeautifulSoup(str(img), "html.parser").find("img")
            if not isinstance(dark, Tag):
                continue
            dark.attrs["src"] = (
                posixpath.join(posixpath.dirname(src), twin_name) + "#only-dark"
            )
            img.attrs["src"] = src + "#only-light"
            img.insert_after(dark)
            _pairs.add(str(path.relative_to(docs_dir)))
            changed = True
            continue

        brightness = _mean_brightness(path)
        if brightness is None:
            continue
        light = brightness > LIGHT_THRESHOLD
        img.attrs["class"] = " ".join(
            [*_classes(img), "sbs-auto-dark" if light else "sbs-auto-light"]
        )
        (_auto_dark if light else _auto_light).add(str(path.relative_to(docs_dir)))
        changed = True

    return str(soup) if changed else html


def on_post_build(config: Any, **kwargs: Any) -> None:
    pr.green(
        f"dark_image_hook: {len(_pairs)} pairs, "
        f"{len(_auto_dark)} sbs-auto-dark, {len(_auto_light)} sbs-auto-light images"
    )
