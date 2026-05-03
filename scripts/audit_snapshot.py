#!/usr/bin/env python3
import re
import sys
from pathlib import Path


def line_numbers(pattern: str, lines: list[str]) -> list[int]:
    regex = re.compile(pattern)
    return [index for index, line in enumerate(lines, start=1) if regex.search(line)]


def main() -> int:
    if len(sys.argv) not in {2, 3}:
        print("uso: audit_snapshot.py constitucion.md [--current]", file=sys.stderr)
        return 2

    require_current_specials = len(sys.argv) == 3 and sys.argv[2] == "--current"
    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    article_matches = list(
        re.finditer(r"^\s*[“\"]?Artículo\s+(\d+(?:-[A-Z])?)", text, re.M)
    )
    articles = {match.group(1) for match in article_matches}
    base_articles = {str(number) for number in range(1, 207)}
    required_special = {"7-A", "14-A", "34-A", "39-A", "90-A", "102-A", "102-B"}
    special_articles = sorted(article for article in articles if not article.isdigit())

    hyphenated = line_numbers(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]-$", lines)
    editorial_notes = line_numbers(r"\(\*\)", lines)
    indented_articles = line_numbers(r"^\s+Artículo\s+\d", lines)
    page_artifacts = line_numbers(
        r"Edición del Congreso|CONSTITUCIÓN POLÍTICA DEL PERÚ\s+\d+|OFICIALÍA MAYOR",
        lines,
    )

    print(f"Archivo: {path}")
    print(f"Lineas: {len(lines)}")
    print(f"Articulos detectados: {len(articles)}")
    print(f"Articulos base faltantes: {', '.join(sorted(base_articles - articles, key=int)) or 'ninguno'}")
    if require_current_specials:
        print(f"Articulos especiales faltantes: {', '.join(sorted(required_special - articles)) or 'ninguno'}")
    print(f"Articulos especiales: {', '.join(special_articles) or 'ninguno'}")
    print(f"Lineas con corte por guion: {len(hyphenated)}")
    print(f"Lineas con notas editoriales (*): {len(editorial_notes)}")
    print(f"Encabezados de articulo indentados: {len(indented_articles)}")
    print(f"Artefactos de pagina detectados: {len(page_artifacts)}")

    if hyphenated:
        print("Primeras lineas con corte por guion:", ", ".join(map(str, hyphenated[:20])))
    if indented_articles:
        print("Encabezados indentados:", ", ".join(map(str, indented_articles[:20])))
    if page_artifacts:
        print("Artefactos de pagina:", ", ".join(map(str, page_artifacts[:20])))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
