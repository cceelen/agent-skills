"""Reader of the folder of one aspect specification. Standard library only.

  load(folder)  reads spec.md, evidence.md and vetting.md into plain dictionaries and lists

A module for the programs in this folder; it needs Python 3.14.

The Markdown files are the only store. A section is found by its number, a table by its place
in the section. Each row is a dictionary: the header names in lowercase are the keys, and
"_line" (starts at 1) and "_file" tell where the row is. A file that is absent gives empty data;
only a missing spec.md is an error.
"""

import itertools
import pathlib
import re

HEADING = re.compile(r"^(#{1,6})\s+(?:(\d+(?:\.\d+)?)\.?\s+)?(.*\S)\s*$")
FIELD = re.compile(r"^- \*\*([^*]+)\*\*:\s*(.*)$")
SUB_ITEM = re.compile(r"^\s+- `([^`]+)`:\s*(.*)$")
HEAD_FIELD = re.compile(r"\*\*([^*]+)\*\*:\s*([^|]*)")
SEPARATOR = re.compile(r"^\|(\s*:?-+:?\s*\|)+\s*$")
SOURCE_ID = re.compile(r"\bS-\d+\b")
ITEM_ID = re.compile(r"\bC-\d+\b")
ITEM_RANGE = re.compile(r"\bC-(\d+) to C-(\d+)\b")
PRINCIPLE = re.compile(r"\bconstitution ([IVX]+)\b")


class Unreadable(Exception):
    """The folder or a file in it cannot be read."""


def cell_spans(line):
    """The (start, end) of each cell of a table row. A pipe after a backslash is text."""
    bars = [i for i, c in enumerate(line) if c == "|" and (i == 0 or line[i - 1] != "\\")]
    return [(a + 1, b) for a, b in itertools.pairwise(bars)]


def split_row(line):
    return [line[a:b].strip().replace("\\|", "|") for a, b in cell_spans(line)]


class Doc:
    """One Markdown file as lines, headings, tables and fields."""

    def __init__(self, path):
        self.path = pathlib.Path(path)
        try:
            self.lines = self.path.read_text(encoding="utf-8").splitlines()
        except OSError as e:
            raise Unreadable(f"{self.path}: {e.strerror or e}") from e
        self.headings = []  # (line index, level, number or None, title)
        fenced = False
        for i, line in enumerate(self.lines):
            if line.startswith("```"):
                fenced = not fenced
            m = None if fenced else HEADING.match(line)
            if m:
                self.headings.append((i, len(m.group(1)), m.group(2), m.group(3)))

    def _span(self, pos):
        i, level = self.headings[pos][0], self.headings[pos][1]
        later = (h[0] for h in self.headings[pos + 1 :] if h[1] <= level)
        return i + 1, next(later, len(self.lines))

    def section(self, number):
        """The line span of the section with this number, or None."""
        for pos, h in enumerate(self.headings):
            if h[2] == number:
                return self._span(pos)
        return None

    def titled(self, prefix):
        """The first heading whose title starts with the prefix: (title, span), or None."""
        for pos, h in enumerate(self.headings):
            if h[3].startswith(prefix):
                return h[3], self._span(pos)
        return None

    def text(self, span):
        return "\n".join(self.lines[span[0] : span[1]]).strip() if span else ""

    def tables(self, span=None):
        """Each table in the span: a list of rows."""
        start, end = span or (0, len(self.lines))
        end = min(end, len(self.lines))
        found, i = [], start
        while i < end - 1:
            if self.lines[i].startswith("|") and SEPARATOR.match(self.lines[i + 1]):
                header = [h.lower() for h in split_row(self.lines[i])]
                rows, i = [], i + 2
                while i < end and self.lines[i].startswith("|"):
                    row = dict(zip(header, split_row(self.lines[i]), strict=False))
                    row["_line"], row["_file"] = i + 1, self.path.name
                    rows.append(row)
                    i += 1
                found.append({"header": header, "rows": rows})
            else:
                i += 1
        return found

    def table(self, span, first_header=None):
        """The rows of the first table in the span (with this first header), or []."""
        if not span:
            return []
        for t in self.tables(span):
            if first_header is None or t["header"][:1] == [first_header]:
                return t["rows"]
        return []

    def fields(self, span):
        """The fields "- **Name**: text" in the span. A field can have sub-items."""
        out, name = {}, None
        if not span:
            return out
        for i in range(span[0], span[1]):
            line = self.lines[i]
            m = FIELD.match(line)
            if m:
                name = m.group(1).strip().lower()
                out[name] = {"value": m.group(2).strip(), "items": [], "_line": i + 1}
                continue
            if name is None:
                continue
            sub = SUB_ITEM.match(line)
            if sub:
                out[name]["items"].append(
                    {"name": sub.group(1), "text": sub.group(2).strip(), "_line": i + 1}
                )
            elif line.startswith("  ") and line.strip():
                target = out[name]["items"][-1] if out[name]["items"] else out[name]
                key = "text" if out[name]["items"] else "value"
                target[key] = (target[key] + " " + line.strip()).strip()
            else:
                name = None
        return out

    def head(self):
        """The fields of the head line, for example branch and accepted."""
        for i, line in enumerate(self.lines[:12]):
            if line.startswith("**"):
                out = {k.strip().lower(): v.strip().strip("`") for k, v in HEAD_FIELD.findall(line)}
                out["_line"] = i + 1
                return out
        return {"_line": 1}


def source_ids(cell):
    return sorted(set(SOURCE_ID.findall(cell or "")))


def principles(cell):
    return sorted(set(PRINCIPLE.findall(cell or "")))


def item_ids(cell):
    """The item identifiers in a cell. "C-02 to C-04" gives the three of them."""
    cell = cell or ""
    ids = set(ITEM_ID.findall(cell))
    for a, b in ITEM_RANGE.findall(cell):
        width = len(a)
        ids.update(f"C-{n:0{width}d}" for n in range(int(a), int(b) + 1))
    return sorted(ids)


def level_of(cell):
    """(level, dimension) of a Level cell.

    The level is 1, 2, 3, "pending", "not admitted", "retired", or None for a cell that is wrong.
    """
    cell = (cell or "").strip()
    if cell in ("pending", "not admitted", "retired"):
        return cell, None
    m = re.fullmatch(r"([123])(?:\s*,\s*(\S.*))?", cell)
    return (int(m.group(1)), m.group(2)) if m else (None, None)


def load(folder):
    folder = pathlib.Path(folder)
    spec = Doc(folder / "spec.md")
    title = spec.headings[0][3] if spec.headings else ""
    s5 = spec.section("5")
    block = spec.titled("Recipe skill and agent:")
    skill = spec.fields(block[1]) if block else {}
    data = {
        "folder": str(folder),
        "title": title.split(":", 1)[1].strip() if ":" in title else title,
        "is_aspect": title.startswith("Aspect specification"),
        "sections": sorted(h[2] for h in spec.headings if h[2]),
        "head": spec.head(),
        "aspect": spec.fields(spec.section("1")),
        "sources": spec.table(spec.section("2"), "id"),
        "goals": spec.text(spec.section("3.1")),
        "order": spec.text(spec.section("3.2")),
        "context_decisions": spec.table(spec.section("3.3"), "decision"),
        "disagreement": spec.table(spec.section("3.4"), "question"),
        "disagreement_text": spec.text(spec.section("3.4")),
        "checklist": spec.table(spec.section("4"), "id"),
        "skill_name": block[0].split(":", 1)[1].strip() if block else "",
        "skill": skill,
        "implementation_skills": spec.table(s5, "product or tool"),
        "watch": spec.table(spec.section("6"), "signal"),
        "decisions": spec.table(spec.section("7"), "date"),
        "glossary": spec.table(spec.section("8"), "term"),
        "evidence": [],
        "vetting_sources": [],
        "vetting_items": [],
        "has_vetting": False,
    }
    data["risk_dimensions"] = data["aspect"].get("risk dimensions", {}).get("items", [])
    if (folder / "evidence.md").is_file():
        data["evidence"] = Doc(folder / "evidence.md").table((0, 10**9), "source")
    if (folder / "vetting.md").is_file():
        vetting = Doc(folder / "vetting.md")
        data["has_vetting"] = True
        for title_, key in (("Sources", "vetting_sources"), ("Items", "vetting_items")):
            found = vetting.titled(title_)
            data[key] = vetting.table(found[1]) if found else []
    return data


def set_cell(path, line_number, column, text):
    """Replace one cell of one table row. No other byte of the file changes."""
    path = pathlib.Path(path)
    raw = path.read_text(encoding="utf-8")
    lines = raw.split("\n")
    line = lines[line_number - 1]
    a, b = cell_spans(line)[column]
    lines[line_number - 1] = line[:a] + " " + text.replace("|", "\\|") + " " + line[b:]
    path.write_text("\n".join(lines), encoding="utf-8")
