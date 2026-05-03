#!/usr/bin/env python3
import argparse
import re
from pathlib import Path


ARTICLE_RE = re.compile(r"^Artículo\s+(\d+(?:-[A-Z])?)\.", re.MULTILINE)


def article_spans(text: str) -> dict[str, tuple[int, int]]:
    matches = list(ARTICLE_RE.finditer(text))
    spans: dict[str, tuple[int, int]] = {}
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        spans[match.group(1)] = (start, end)
    return spans


def extract_article(text: str, article: str) -> str:
    spans = article_spans(text)
    if article not in spans:
        raise KeyError(f"No existe Artículo {article}")
    start, end = spans[article]
    return text[start:end].strip() + "\n"


def replace_article(text: str, article: str, replacement: str) -> str:
    spans = article_spans(text)
    if article not in spans:
        raise KeyError(f"No existe Artículo {article}")
    start, end = spans[article]
    replacement = replacement.strip() + "\n\n"
    return text[:start] + replacement + text[end:].lstrip("\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Extrae o reemplaza articulos en snapshots canonicos.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    extract = subparsers.add_parser("extract")
    extract.add_argument("snapshot", type=Path)
    extract.add_argument("article")

    replace = subparsers.add_parser("replace")
    replace.add_argument("snapshot", type=Path)
    replace.add_argument("article")
    replace.add_argument("replacement", type=Path)
    replace.add_argument("output", type=Path)

    args = parser.parse_args()
    text = args.snapshot.read_text(encoding="utf-8")

    if args.command == "extract":
        print(extract_article(text, args.article), end="")
    elif args.command == "replace":
        replacement = args.replacement.read_text(encoding="utf-8")
        args.output.write_text(replace_article(text, args.article, replacement), encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

