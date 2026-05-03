#!/usr/bin/env python3
import argparse
import re
from pathlib import Path


def normalize_line(line: str) -> str:
    line = line.strip()
    line = re.sub(r"\s+", " ", line)
    line = re.sub(r"([A-Za-zÁÉÍÓÚÜÑáéíóúüñ])- ([a-záéíóúüñ]{2,})", r"\1\2", line)
    line = re.sub(r"Artículo\s+(\d+(?:-[A-Z])?)\.-", r"Artículo \1.", line)
    line = re.sub(r"Artículo\s+(\d+(?:-[A-Z])?)\.", r"Artículo \1.", line)
    return line


def should_keep_as_separate(line: str) -> bool:
    return bool(
        re.match(r"^(Artículo|[0-9]+\.\s|[a-z]\.\s|[A-ZÁÉÍÓÚÑ ]{6,}$)", line)
    )


def canonicalize(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"([A-Za-zÁÉÍÓÚÜÑáéíóúüñ])-\n\s*([a-záéíóúüñ]{2,})", r"\1\2", text)
    text = re.sub(r"([A-Za-zÁÉÍÓÚÜÑáéíóúüñ])- +([a-záéíóúüñ])", r"\1\2", text)
    blocks = re.split(r"\n\s*\n", text)
    output: list[str] = []

    for block in blocks:
        lines = [normalize_line(line) for line in block.splitlines() if line.strip()]
        if not lines:
            continue

        current: list[str] = []
        for line in lines:
            if current and should_keep_as_separate(line):
                output.append(" ".join(current))
                current = [line]
            else:
                current.append(line)
        if current:
            output.append(" ".join(current))

    text = "\n\n".join(output)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Normaliza un snapshot a parrafos estables para git blame."
    )
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    text = args.input.read_text(encoding="utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(canonicalize(text), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
