#!/usr/bin/env python3
import re
import sys
from pathlib import Path


REQUIRED_SPECIAL = {"7-A", "14-A", "34-A", "39-A", "90-A", "102-A", "102-B"}


def main() -> int:
    if len(sys.argv) != 2:
        print("uso: validate_snapshot.py constitucion.md", file=sys.stderr)
        return 2

    text = Path(sys.argv[1]).read_text(encoding="utf-8")
    articles = {
        match.group(1)
        for match in re.finditer(r"Artículo\s+(\d+(?:-[A-Z])?)", text)
    }
    expected = {str(number) for number in range(1, 207)} | REQUIRED_SPECIAL
    missing = sorted(expected - articles, key=lambda item: (int(item.split("-")[0]), item))

    if missing:
        print("Faltan articulos:", ", ".join(missing), file=sys.stderr)
        return 1

    print(f"OK: {len(articles)} articulos detectados")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

