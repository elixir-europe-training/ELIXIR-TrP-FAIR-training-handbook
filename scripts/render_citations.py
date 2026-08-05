#!/usr/bin/env python3
"""Pre-render [@citekey] citations and \\full_bibliography into docs_build/.

Replaces the mkdocs-bibtex plugin, which zensical does not support (it has
no plugin API yet). Copies docs/ to docs_build/ and, in that copy only:

  - replaces [@key] (and [@key1, key2, ...]) with an "(Author, Year)" link
    pointing at the matching entry in the references page
  - replaces the literal line \\full_bibliography with the full, formatted
    reference list (pybtex "plain" style), each entry anchored by its key
  - replaces the literal line \\bibliography with the formatted reference
    list for just the citations used earlier on that same page

Usage:
    render_citations.py [--references-page PATH]

--references-page is the path (relative to docs/) of the page inline
citations link to and where \\full_bibliography renders the complete
list. Defaults to "chapters/references.md" - pass a project-specific
path if the reference/literature page lives somewhere else.

Run this before `zensical build` / `zensical serve`. Never edit files
under docs_build/ directly - it is regenerated on every run.
"""
import argparse
import os
import re
import shutil
from pathlib import Path

from pybtex.backends.html import Backend
from pybtex.style.formatting.plain import Style

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "docs"
BUILD_DIR = ROOT / "docs_build"
BIB_FILE = ROOT / "references.bib"
DEFAULT_REFERENCES_PAGE = "chapters/references.md"

CITE_RE = re.compile(r"\[@([\w:./-]+(?:\s*,\s*@?[\w:./-]+)*)\]")
FULL_BIBLIOGRAPHY_MARKER = "\\full_bibliography"
PAGE_BIBLIOGRAPHY_MARKER = "\\bibliography"


def strip_braces(name):
    return name.replace("{", "").replace("}", "")


def author_year_label(entry):
    persons = entry.persons.get("author", [])
    year = entry.fields.get("year", "n.d.")
    if not persons:
        who = entry.fields.get("publisher") or entry.fields.get("organization")
        who = strip_braces(who) if who else "Anon."
        return f"({who}, {year})"
    surnames = [strip_braces(" ".join(p.last_names)) for p in persons]
    if len(surnames) == 1:
        who = surnames[0]
    elif len(surnames) == 2:
        who = f"{surnames[0]} & {surnames[1]}"
    else:
        who = f"{surnames[0]} et al."
    return f"({who}, {year})"


def load_bibliography():
    from pybtex.database import parse_file

    bib_data = parse_file(str(BIB_FILE))
    backend = Backend()
    formatted = Style().format_bibliography(bib_data)
    entries_html = {fe.key: fe.text.render(backend) for fe in formatted}
    return bib_data, entries_html


def relative_link(src_md_path, target_md_path):
    # Written relative to the markdown *source* tree (e.g. "references.md" or
    # "chapters/references.md"), matching how a hand-authored MkDocs/Zensical
    # link would look. Zensical rewrites this itself to account for the
    # directory-URL output structure (foo.md -> foo/index.html) - a link
    # already adjusted for that here would get adjusted a second time.
    rel_dir = os.path.relpath(target_md_path.parent, start=src_md_path.parent)
    rel_path = os.path.normpath(os.path.join(rel_dir, target_md_path.name))
    return rel_path.replace(os.sep, "/")


def process_file(md_path, bib_data, entries_html, references_page):
    text = md_path.read_text(encoding="utf-8")
    changed = False
    cited_keys = []

    def cite_repl(match):
        nonlocal changed
        changed = True
        rel = relative_link(md_path, references_page)
        keys = [k.strip().lstrip("@") for k in match.group(1).split(",")]
        links = []
        for key in keys:
            if key not in bib_data.entries:
                links.append(f"**[unknown citation: {key}]**")
                continue
            if key not in cited_keys:
                cited_keys.append(key)
            label = author_year_label(bib_data.entries[key])
            links.append(f"[{label}]({rel}#{key})")
        return " ".join(links)

    text = CITE_RE.sub(cite_repl, text)

    if FULL_BIBLIOGRAPHY_MARKER in text:
        changed = True
        items = [f'<p id="{key}">{html}</p>' for key, html in entries_html.items()]
        text = text.replace(FULL_BIBLIOGRAPHY_MARKER, "\n".join(items))

    if PAGE_BIBLIOGRAPHY_MARKER in text:
        changed = True
        items = [
            f'<p id="{key}">{entries_html[key]}</p>'
            for key in cited_keys
            if key in entries_html
        ]
        text = text.replace(PAGE_BIBLIOGRAPHY_MARKER, "\n".join(items))

    if changed:
        md_path.write_text(text, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--references-page",
        default=DEFAULT_REFERENCES_PAGE,
        help="Path (relative to docs/) of the references/literature page. "
        "Default: %(default)s",
    )
    args = parser.parse_args()
    references_page = BUILD_DIR / args.references_page

    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    shutil.copytree(SRC_DIR, BUILD_DIR)

    bib_data, entries_html = load_bibliography()
    md_files = list(BUILD_DIR.rglob("*.md"))
    for md_path in md_files:
        process_file(md_path, bib_data, entries_html, references_page)

    print(f"render_citations: rendered {len(md_files)} pages into {BUILD_DIR}")


if __name__ == "__main__":
    main()
