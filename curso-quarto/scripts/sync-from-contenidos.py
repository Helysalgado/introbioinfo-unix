#!/usr/bin/env python3
"""Sincroniza contenidos-2026 → curso-quarto (capa de publicación).

Copia portadas/sesiones/transversal, images PNG y ejemplos; corrige enlaces
legacy; convierte callouts; elimina notas docentes; no toca _quarto.yml ni
páginas de marco (index/programa/recursos).

Uso (desde la raíz del repo o desde curso-quarto/):

    python3 curso-quarto/scripts/sync-from-contenidos.py
"""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "contenidos-2026"
DST = ROOT / "curso-quarto"

KIND_MAP = {
    "NOTA": ("note", None),
    "IMPORTANTE": ("important", None),
    "TIP": ("tip", None),
    "ADVERTENCIA": ("warning", None),
    "COMENTARIO": ("tip", None),
    "¿SABÍAS QUE?": ("tip", "¿Sabías que?"),
}

FIRST = re.compile(
    r"^>\s*\*\*"
    r"(?P<kind>NOTA|IMPORTANTE|TIP|ADVERTENCIA|COMENTARIO|¿SABÍAS QUE\?)"
    r"(?:(?P<sep>\s*[—–-]\s*)(?P<title>.+?))?"
    r"(?P<endpunct>[:.])?"
    r"\*\*"
    r"(?P<rest>.*)$"
)

DOCENTE_START = re.compile(
    r"^>\s*\*\*(?:NOTA DOCENTE|NOTA DE ALINEACIÓN \(docente\)|NOTA sobre el Plan operativo)",
    re.I,
)

LINK_FIXES = [
    ("../introBioInfo/ejemplos/formato_protocolo_v1.0.md", "ejemplos/formato_protocolo_v1.0.md"),
    ("../introBioInfo/ejemplos/ReporteGenomeEcoli_Formato_v2.md", "ejemplos/ReporteGenomeEcoli_Formato_v2.md"),
    ("../introBioInfo/referencias/bioinformatics-data-skills.pdf", "referencias/bioinformatics-data-skills.pdf"),
]

AGENDA_TABLE = re.compile(
    r"(?P<head>(?:^|\n)(?P<h2>#{2,3}[^\n]*\n\n)?)"
    r"(?P<table>\| Tiempo \| Actividad \|\n\| --- \| --- \|\n(?:\|[^\n]+\n)+)",
    re.M,
)


def strip_bq(line: str) -> str:
    if line.startswith("> "):
        return line[2:]
    if line == ">":
        return ""
    if line.startswith(">"):
        return line[1:].lstrip()
    return line


def convert_callouts(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    while i < len(lines):
        raw = lines[i].rstrip("\n")
        m = FIRST.match(raw) if raw.startswith(">") else None
        if not m:
            out.append(lines[i])
            i += 1
            continue

        block = [raw]
        i += 1
        while i < len(lines) and lines[i].startswith(">"):
            block.append(lines[i].rstrip("\n"))
            i += 1

        kind = m.group("kind")
        callout, default_title = KIND_MAP[kind]
        title = (m.group("title") or "").strip().rstrip(".")
        if default_title and not title:
            title = default_title
        rest_first = (m.group("rest") or "").strip()

        body_lines: list[str] = []
        if rest_first:
            body_lines.append(rest_first)
        for bq_line in block[1:]:
            body_lines.append(strip_bq(bq_line))
        while body_lines and body_lines[-1].strip() == "":
            body_lines.pop()

        if title:
            t_esc = title.replace('"', '\\"')
            header = f'::: {{.callout-{callout} title="{t_esc}"}}'
        else:
            header = f"::: {{.callout-{callout}}}"

        out.append(header + "\n")
        if body_lines:
            out.append("\n".join(body_lines) + "\n")
        out.append(":::\n")
    return "".join(out)


def strip_docente_notes(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    while i < len(lines):
        raw = lines[i].rstrip("\n")
        if DOCENTE_START.match(raw):
            i += 1
            while i < len(lines) and lines[i].startswith(">"):
                i += 1
            if i < len(lines) and lines[i].strip() == "":
                i += 1
            continue
        out.append(lines[i])
        i += 1
    return "".join(out)


def fix_links(text: str) -> str:
    for a, b in LINK_FIXES:
        text = text.replace(a, b)
    # broken "]  (path)" from earlier bad replaces
    text = re.sub(r"\]  \((ejemplos/[^)]+)\)", r"](\1)", text)
    return text


def left_align_agenda_separators(text: str) -> str:
    return re.sub(
        r"(\| Tiempo \| Actividad \|\n)\| ---: \| --- \|",
        r"\1| --- | --- |",
        text,
    )


def wrap_agenda_tables(text: str) -> str:
    def repl(m: re.Match[str]) -> str:
        start = m.start("table")
        before = text[max(0, start - 40) : start]
        if "tabla-agenda" in before:
            return m.group(0)
        return f"{m.group('head') or ''}::: {{.tabla-agenda}}\n{m.group('table')}:::\n"

    return AGENDA_TABLE.sub(repl, text)


def soften_docente_links(text: str) -> str:
    """Quita enlaces a docente/ en el sitio publicado."""
    text = re.sub(
        r"y su auditoría completa —qué\ncontiene cada uno y para qué sirve— está en "
        r"\[`docente/u6-auditoria-datos\.md`\]\(docente/u6-auditoria-datos\.md\)\.",
        "La auditoría docente del conjunto (qué contiene cada archivo y para qué sirve) "
        "no se publica en este sitio.",
        text,
    )
    return text


def process_lesson(text: str) -> str:
    text = fix_links(text)
    text = soften_docente_links(text)
    text = left_align_agenda_separators(text)
    text = convert_callouts(text)
    text = strip_docente_notes(text)
    text = wrap_agenda_tables(text)
    return text


def copy_lessons() -> int:
    patterns = ["u*.md", "s*.md", "mini-proyecto*.md"]
    n = 0
    for pat in patterns:
        for src in sorted(SRC.glob(pat)):
            if src.name in {"README.md", "plantilla-unidad.md"}:
                continue
            raw = src.read_text(encoding="utf-8")
            (DST / src.name).write_text(process_lesson(raw), encoding="utf-8")
            n += 1
    return n


def sync_images() -> int:
    dest = DST / "images"
    dest.mkdir(exist_ok=True)
    for old in dest.glob("*.png"):
        old.unlink()
    n = 0
    for src in sorted((SRC / "images").glob("*.png")):
        shutil.copy2(src, dest / src.name)
        n += 1
    return n


def sync_ejemplos() -> None:
    dest = DST / "ejemplos"
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(SRC / "ejemplos", dest)


def sync_buffalo() -> None:
    pdf_src = ROOT / "introBioInfo" / "referencias" / "bioinformatics-data-skills.pdf"
    pdf_dst_dir = DST / "referencias"
    pdf_dst_dir.mkdir(exist_ok=True)
    if pdf_src.exists():
        shutil.copy2(pdf_src, pdf_dst_dir / pdf_src.name)
        print(f"  Buffalo PDF ← {pdf_src.relative_to(ROOT)}")
    else:
        print("  AVISO: no se encontró Buffalo PDF en introBioInfo/referencias/")


def main() -> int:
    if not SRC.is_dir():
        print(f"ERROR: no existe {SRC}", file=sys.stderr)
        return 1
    DST.mkdir(exist_ok=True)
    print(f"Fuente: {SRC}")
    print(f"Destino: {DST}")
    n = copy_lessons()
    print(f"  Lecciones procesadas: {n}")
    print(f"  Imágenes PNG: {sync_images()}")
    sync_ejemplos()
    print("  ejemplos/ sincronizado")
    sync_buffalo()
    print("Listo. Revisa con: cd curso-quarto && quarto preview")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
