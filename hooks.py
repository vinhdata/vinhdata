from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

# Filled during on_config, used in on_nav
KB_GROUP_LINKS: dict[str, list[tuple[str, str]]] = {}


def _titleize_folder(name: str) -> str:
    # "how-to" -> "How to", "data-platform" -> "Data platform"
    name = name.replace("_", " ").replace("-", " ").strip().strip("/")
    parts = [p for p in name.split() if p]
    return " ".join([parts[0].capitalize(), *parts[1:]]) if parts else name


def _read_front_matter(md_path: Path) -> tuple[dict[str, Any], list[str]]:
    """Return (meta, body_lines)."""
    text = md_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text.splitlines()

    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text.splitlines()

    meta_raw = parts[1]
    body = parts[2]
    meta = yaml.safe_load(meta_raw) or {}
    return meta, body.splitlines()


def _extract_title(md_path: Path) -> str:
    try:
        meta, body_lines = _read_front_matter(md_path)
    except Exception:
        return md_path.stem

    title = meta.get("title")
    if isinstance(title, str) and title.strip():
        return title.strip()

    for line in body_lines:
        if line.startswith("# "):
            return line[2:].strip() or md_path.stem

    return md_path.stem


def _extract_date_iso(md_path: Path) -> str:
    try:
        meta, _ = _read_front_matter(md_path)
    except Exception:
        return ""

    date = meta.get("date")
    return str(date) if date else ""


def _post_url(md_path: Path, docs_dir: Path) -> str:
    """
    Compute the blog post URL that mkdocs-material's blog plugin will generate
    with its default `post_url_format: "{date}/{slug}"`.
    """
    date = _extract_date_iso(md_path)
    # Expect YYYY-MM-DD
    if len(date) >= 10 and date[4] == "-" and date[7] == "-":
        yyyy, mm, dd = date[:4], date[5:7], date[8:10]
        date_path = f"{yyyy}/{mm}/{dd}"
    else:
        # Fallback: place undated posts under 'drafts'
        date_path = "drafts"

    # mkdocs-material slugify: lower + "-" separator
    from pymdownx.slugs import slugify

    slug_fn = slugify(case="lower")
    slug = slug_fn(_extract_title(md_path), "-")

    return f"blog/{date_path}/{slug}/"


def _build_knowledge_base_nav(docs_dir: Path) -> list[Any]:
    posts_root = docs_dir / "blog" / "posts"
    # Use blog index as the landing page for the tab
    nav: list[Any] = [{"Overview": "blog/index.md"}]

    # Recompute links each time config is loaded
    global KB_GROUP_LINKS
    KB_GROUP_LINKS = {}

    if not posts_root.exists():
        return nav

    folder_names = sorted(
        [p.name for p in posts_root.iterdir() if p.is_dir() and not p.name.startswith(".")]
    )

    # Ensure folders show as toggles (even if empty)
    for folder in folder_names:
        folder_path = posts_root / folder
        posts = sorted(
            [p for p in folder_path.glob("*.md") if p.is_file() and not p.name.startswith(".")],
            key=lambda p: (_extract_date_iso(p), p.name),
            reverse=True,
        )

        group_title = _titleize_folder(folder)
        # Create a collapsible section for each folder
        nav.append({group_title: []})

        items: list[tuple[str, str]] = []
        for p in posts:
            title = _extract_title(p)
            items.append((title, _post_url(p, docs_dir)))

        KB_GROUP_LINKS[group_title] = items

    return nav


def on_config(config: dict[str, Any]) -> dict[str, Any]:
    nav = config.get("nav")
    if not isinstance(nav, list):
        return config

    docs_dir = Path(config.get("docs_dir") or "docs")
    kb_nav = _build_knowledge_base_nav(docs_dir)
    for entry in nav:
        if isinstance(entry, dict) and "Knowledge Base" in entry:
            entry["Knowledge Base"] = kb_nav
            break
    config["nav"] = nav
    return config


def on_nav(nav, config, files):
    """Inject internal links to blog posts under Knowledge Base sections."""
    if not KB_GROUP_LINKS:
        return nav

    try:
        from mkdocs.structure.nav import Link, Section
    except Exception:
        return nav

    # Find the "Knowledge Base" section in the rendered navigation
    kb_section = None
    for item in getattr(nav, "items", []):
        if isinstance(item, Section) and item.title == "Knowledge Base":
            kb_section = item
            break

    if not kb_section:
        return nav

    for item in getattr(kb_section, "children", []):
        if not isinstance(item, Section):
            continue
        links = KB_GROUP_LINKS.get(item.title)
        if links is None:
            continue
        item.children = [Link(title, url) for (title, url) in links]

    return nav

