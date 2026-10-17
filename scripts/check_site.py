#!/usr/bin/env python3
# Website source code of Mass Collaboration Labs
#
# Copyright (C) 2026 Mass Collaboration Labs
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""Run dependency-free structural checks for the static website."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.local_references: list[str] = []
        self.images_without_alt: list[str] = []
        self.untitled_iframes: list[str] = []
        self.non_lazy_iframes: list[str] = []
        self.unsafe_external_links: list[str] = []
        self.document_language: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        element_id = attributes.get("id")
        if element_id:
            self.ids.append(element_id)

        if tag == "html":
            self.document_language = attributes.get("lang")
        if tag == "img" and attributes.get("alt") is None:
            self.images_without_alt.append(attributes.get("src", "<unknown image>"))
        if tag == "iframe":
            source = attributes.get("src", "<unknown iframe>")
            if not attributes.get("title"):
                self.untitled_iframes.append(source)
            if attributes.get("loading") != "lazy":
                self.non_lazy_iframes.append(source)

        for attribute in ("href", "src"):
            value = attributes.get(attribute)
            if not value:
                continue
            parsed = urlsplit(value)
            if parsed.scheme or parsed.netloc or value.startswith(("#", "data:")):
                continue
            self.local_references.append(parsed.path)

        if tag == "a" and attributes.get("target") == "_blank":
            rel = set(attributes.get("rel", "").lower().split())
            if not {"noopener", "noreferrer"}.issubset(rel):
                self.unsafe_external_links.append(attributes.get("href", "<unknown link>"))


def main() -> None:
    parser = SiteParser()
    parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))
    parser.close()

    errors: list[str] = []
    if not parser.document_language:
        errors.append("The document must declare its language.")
    if len(parser.ids) != len(set(parser.ids)):
        errors.append("HTML id attributes must be unique.")
    if parser.images_without_alt:
        errors.append(f"Images missing alt text: {parser.images_without_alt}")
    if parser.untitled_iframes:
        errors.append(f"Iframes missing title: {parser.untitled_iframes}")
    if parser.non_lazy_iframes:
        errors.append(f"Iframes missing lazy loading: {parser.non_lazy_iframes}")
    if parser.unsafe_external_links:
        errors.append(f"New-tab links missing noopener/noreferrer: {parser.unsafe_external_links}")

    for reference in parser.local_references:
        if reference and not (ROOT / reference).is_file():
            errors.append(f"Local asset does not exist: {reference}")

    for svg_path in (ROOT / "img").glob("*.svg"):
        try:
            ElementTree.parse(svg_path)
        except ElementTree.ParseError as error:
            errors.append(f"Invalid SVG {svg_path.relative_to(ROOT)}: {error}")

    if errors:
        raise SystemExit("\n".join(f"ERROR: {error}" for error in errors))
    print("Static site checks passed.")


if __name__ == "__main__":
    main()
