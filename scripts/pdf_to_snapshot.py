#!/usr/bin/env python3
import argparse
import re
import subprocess
import tempfile
from pathlib import Path


HEADER_FOOTER = [
    re.compile(r"^\s*\d+\s*$"),
    re.compile(r"^\s*\d+\s+Edición del Congreso de la República\s*$"),
    re.compile(r"^\s*CONSTITUCIÓN POLÍTICA DEL PERÚ\s+\d+\s*$"),
]


def run_pdftotext(pdf: Path) -> str:
    with tempfile.NamedTemporaryFile(suffix=".txt") as tmp:
        subprocess.run(
            ["pdftotext", "-layout", "-enc", "UTF-8", str(pdf), tmp.name],
            check=True,
        )
        return Path(tmp.name).read_text(encoding="utf-8", errors="replace")


def is_header_footer(line: str) -> bool:
    return any(pattern.match(line) for pattern in HEADER_FOOTER)


def clean_text(text: str) -> str:
    text = text.replace("\ufeff", "")
    text = text.replace("\x0c", "\n")
    lines = [line.rstrip() for line in text.splitlines()]

    cleaned = []
    for line in lines:
        if is_header_footer(line):
            continue
        line = re.sub(r"Artículo\s+(\d+(?:-[A-Z])?)", r"Artículo \1", line)
        cleaned.append(line)

    text = "\n".join(cleaned)

    start = text.find("CONSTITUCIÓN POLÍTICA\n            DEL PERÚ")
    if start == -1:
        start = text.find("P R E Á M B U L O")
    if start != -1:
        text = text[start:]

    end = text.find("     REFORMAS A LA CONSTITUCIÓN POLÍTICA")
    if end != -1:
        text = text[:end]

    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extrae un snapshot Markdown desde el PDF oficial del Congreso."
    )
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    raw = run_pdftotext(args.pdf)
    cleaned = clean_text(raw)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(cleaned, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
