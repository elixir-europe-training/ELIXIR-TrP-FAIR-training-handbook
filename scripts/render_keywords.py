#!/usr/bin/env python3
"""Pre-render the [TAGS] marker in docs_build/keywords.md into a keyword index.

Replaces the mkdocs `tags` plugin, which zensical does not support (it has
no plugin API yet). Must run after scripts/render_citations.py, which
creates docs_build/ - this script only edits the [TAGS] marker within it,
reading the original front-matter `tags:` lists already copied there.

Run before `zensical build` / `zensical serve`.
"""
import os
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BUILD_DIR = ROOT / "docs_build"
MKDOCS_YML = ROOT / "mkdocs.yml"
KEYWORDS_PAGE = BUILD_DIR / "keywords.md"
TAGS_MARKER = "[TAGS]"

FRONT_MATTER_RE = re.compile(r"\A---\n(.*?\n)---\n", re.DOTALL)


class _IgnoreUnknownTagsLoader(yaml.SafeLoader):
    """mkdocs.yml uses !!python/name: tags (for emoji extensions) that
    yaml.safe_load can't construct. We only need the nav: key, so ignore
    any tag we don't recognize instead of failing to parse the whole file.
    """


def _construct_undefined(loader, suffix, node):
    return None


_IgnoreUnknownTagsLoader.add_multi_constructor(
    "tag:yaml.org,2002:python", _construct_undefined
)


def load_nav_titles():
    """Map doc path (relative to docs/, e.g. 'chapters/chapter_01.md') -> nav title."""
    config = yaml.load(
        MKDOCS_YML.read_text(encoding="utf-8"), Loader=_IgnoreUnknownTagsLoader
    )
    titles = {}

    def walk(node):
        if isinstance(node, list):
            for item in node:
                walk(item)
        elif isinstance(node, dict):
            for title, target in node.items():
                if isinstance(target, str):
                    titles[target] = title
                else:
                    walk(target)

    walk(config.get("nav", []))
    return titles


def extract_tags(md_path):
    text = md_path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return []
    front_matter = yaml.safe_load(match.group(1)) or {}
    return front_matter.get("tags") or []


def main():
    nav_titles = load_nav_titles()

    tag_pages = {}
    for md_path in sorted(BUILD_DIR.rglob("*.md")):
        rel_path = md_path.relative_to(BUILD_DIR).as_posix()
        for tag in extract_tags(md_path):
            tag = str(tag).strip()
            if not tag:
                continue
            tag_pages.setdefault(tag, []).append((rel_path, md_path))

    lines = []
    for tag in sorted(tag_pages, key=str.casefold):
        lines.append(f"### {tag}\n")
        for rel_path, md_path in tag_pages[tag]:
            title = nav_titles.get(rel_path, md_path.stem)
            rel_link = os.path.relpath(md_path, start=KEYWORDS_PAGE.parent)
            lines.append(f"- [{title}]({Path(rel_link).as_posix()})")
        lines.append("")

    text = KEYWORDS_PAGE.read_text(encoding="utf-8")
    if TAGS_MARKER not in text:
        raise SystemExit(
            f"render_keywords: marker {TAGS_MARKER!r} not found in {KEYWORDS_PAGE}"
        )
    text = text.replace(TAGS_MARKER, "\n".join(lines).rstrip())
    KEYWORDS_PAGE.write_text(text, encoding="utf-8")

    print(f"render_keywords: rendered {len(tag_pages)} tags into {KEYWORDS_PAGE}")


if __name__ == "__main__":
    main()
