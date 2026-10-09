#!/usr/bin/env python3
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Reader of the folder of one aspect specification. Standard library only.

  load(folder)  reads spec.md, evidence.md and vetting.md into plain dictionaries and lists

A module for the programs in this folder; it needs Python 3.14.

The Markdown files are the only store. A section is found by its number, a table by its place
in the section. Each row is a dictionary: the header names in lowercase are the keys, and
"_line" (starts at 1) and "_file" tell where the row is. A file that is absent gives empty data;
only a missing spec.md is an error.
"""

import doctest
import itertools
import pathlib
import re
import sys

HEADING = re.compile(r"^(#{1,6})\s+(?:(\d+(?:\.\d+)?)\.?\s+)?(.*\S)\s*$")
FIELD = re.compile(r"^- \*\*([^*]+)\*\*:\s*(.*)$")
SUB_ITEM = re.compile(r"^\s+- `([^`]+)`:\s*(.*)$")
HEAD_FIELD = re.compile(r"\*\*([^*]+)\*\*:\s*([^|]*)")
SEPARATOR = re.compile(r"^\|(\s*:?-+:?\s*\|)+\s*$")
SOURCE_ID = re.compile(r"\bS-\d+\b")
ITEM_ID = re.compile(r"\bC-\d+\b")
ITEM_RANGE = re.compile(r"\bC-(\d+) to C-(\d+)\b")
PRINCIPLE = re.compile(r"\bconstitution ([IVX]+)\b", re.I)


class Unreadable(Exception):
    """The folder or a file in it cannot be read."""


def cell_spans(line):
    """The (start, end) of each cell of a table row. A pipe after a backslash is text."""
    bars = [i for i, c in enumerate(line) if c == "|" and (i == 0 or line[i - 1] != "\\")]
    return [(a + 1, b) for a, b in itertools.pairwise(bars)]


def split_row(line):
    r"""The cells of one table row.

    >>> split_row("| a | b c |  |")
    ['a', 'b c', '']
    >>> split_row(r"| a \| b | c |")
    ['a | b', 'c']
    """
    return [line[a:b].strip().replace("\\|", "|") for a, b in cell_spans(line)]


def read_text(path):
    """The text of a file in UTF-8, with its line ends as they are."""
    try:
        with open(path, encoding="utf-8-sig", newline="") as f:
            return f.read()
    except OSError as e:
        raise Unreadable(f"{path}: {e.strerror or e}") from e
    except UnicodeDecodeError as e:
        raise Unreadable(f"{path}: the file is not UTF-8") from e


def write_text(path, text):
    """Write a file in UTF-8. The line ends stay as they are in the text."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


class Doc:
    """One Markdown file as lines, headings, tables and fields."""

    def __init__(self, path):
        self.path = pathlib.Path(path)
        # Only a line feed ends a line, as in set_cell: the line numbers must agree.
        self.lines = [line.removesuffix("\r") for line in read_text(self.path).split("\n")]
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
                    row["_line"], row["_file"], row["_header"] = i + 1, self.path.name, header
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
    """The source identifiers in a cell, sorted.

    >>> source_ids("S-03 items 1, 13; S-04 guideline 11; S-03")
    ['S-03', 'S-04']
    """
    return sorted(set(SOURCE_ID.findall(cell or "")))


def principles(cell):
    """The principles of the constitution in a cell, sorted.

    >>> principles("constitution IV; S-21 abstract; Constitution iii")
    ['III', 'IV']
    """
    return sorted({p.upper() for p in PRINCIPLE.findall(cell or "")})


def item_ids(cell):
    """The item identifiers in a cell. "C-02 to C-04" gives the three of them.

    >>> item_ids("C-02 to C-04, C-09; 3.3 depth")
    ['C-02', 'C-03', 'C-04', 'C-09']
    """
    cell = cell or ""
    ids = set(ITEM_ID.findall(cell))
    for a, b in ITEM_RANGE.findall(cell):
        width = len(a)
        ids.update(f"C-{n:0{width}d}" for n in range(int(a), int(b) + 1))
    return sorted(ids)


def level_of(cell):
    """(level, dimension) of a Level cell.

    The level is 1, 2, 3, "pending", "not admitted", "retired", or None for a cell that is wrong.

    >>> level_of("2, operative"), level_of("1"), level_of("pending"), level_of("retired")
    ((2, 'operative'), (1, None), ('pending', None), ('retired', None))
    >>> level_of("high"), level_of(""), level_of(None)
    ((None, None), (None, None), (None, None))
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
    r"""Replace one cell of one table row. No other byte of the file changes.

    Returns False, and changes nothing, if the row has no cell in that column.

    >>> import tempfile
    >>> path = pathlib.Path(tempfile.mkdtemp(prefix="sota-cell-")) / "t.md"
    >>> _ = path.write_text("| a | b |\n|---|---|\n| short |\n", encoding="utf-8")
    >>> set_cell(path, 3, 1, "x"), set_cell(path, 9, 0, "x"), set_cell(path, 3, -1, "x")
    (False, False, False)
    >>> set_cell(path, 3, 0, "x | y"), path.read_text(encoding="utf-8").splitlines()[2]
    (True, '| x \\| y |')
    """
    try:
        with open(path, encoding="utf-8", newline="") as f:  # a byte order mark stays in the text
            lines = f.read().split("\n")
    except (OSError, UnicodeDecodeError) as e:
        raise Unreadable(f"{path}: {e}") from e
    if not 0 < line_number <= len(lines):
        return False
    line = lines[line_number - 1]
    spans = cell_spans(line)
    if not 0 <= column < len(spans):
        return False
    a, b = spans[column]
    lines[line_number - 1] = line[:a] + " " + text.replace("|", "\\|") + " " + line[b:]
    write_text(path, "\n".join(lines))
    return True


def column_of(row, name):
    """The position of a column in the table of the row, or -1."""
    header = row.get("_header", [])
    return header.index(name) if name in header else -1


def long_sentences(messages, limit=25):
    """The sentences of a message table that have more words than the limit.

    The text for the person in the loop is in Simplified Technical English: short sentences.

    >>> long_sentences({"a": "One short sentence. And a second one: with {0} parts."})
    []
    >>> long_sentences({"a": "one two three four. five"}, limit=3)
    ['one two three four.']
    """
    out = []
    for text in messages.values():
        flat = re.sub(r"\s+", " ", re.sub(r"^\s*(?:-|\d+\.)\s+", "", text, flags=re.M))
        out += [s for s in re.split(r"(?<=[.:;])\s+", flat) if len(s.split()) > limit]
    return out


def selftest(name="__main__"):
    """Run the examples (doctests) of one module of the tooling. Returns the result code.

    Each program validates itself with the option --selftest. No test file is necessary.
    """
    flags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    result = doctest.testmod(sys.modules[name], optionflags=flags)
    print(f"{result.attempted} examples, {result.failed} failed")
    return 1 if result.failed or not result.attempted else 0


__test__ = {
    "the sample specification": r"""
    >>> import sample
    >>> data = load(sample.folder())
    >>> data["is_aspect"], data["title"], data["head"]["branch"], data["head"]["accepted"]
    (True, 'Backups of project data', '900-backups', 'A. Person, 2026-01-15')

    A field that continues on the next line is one value. A field can have sub-items.

    >>> data["aspect"]["contexts"]["value"]
    'the size of the data; who operates the software; the place where the data is.'
    >>> [(d["name"], d["text"][:31]) for d in data["risk_dimensions"]]
    [('operative', 'Can a lost record be made again'), ('regulatory', 'Is personal data in the backup?')]

    Each table is found in its section, and each row knows its place.

    >>> [s["id"] for s in data["sources"]], data["sources"][0]["version or date"]
    (['S-01', 'S-02', 'S-03', 'S-04'], '2.0, 2025-03')
    >>> [c["id"] for c in data["checklist"]]
    ['C-01', 'C-02', 'C-03', 'C-04', 'C-05']
    >>> [c["level"] for c in data["checklist"]]
    ['1', '2, operative', '3, regulatory', 'not admitted', '1']
    >>> row = data["checklist"][0]
    >>> row["_file"], column_of(row, "level"), column_of(row, "no such column")
    ('spec.md', 3, -1)
    >>> [len(data[k]) for k in ("context_decisions", "disagreement", "watch", "decisions", "glossary")]
    [1, 1, 1, 2, 1]
    >>> data["skill_name"], data["skill"]["goal"]["value"][:11], "target folder" in data["skill"]
    ('backups', 'Each record', False)
    >>> data["goals"][:13], data["order"][:11]
    ('A lost record', '1. Find out')
    >>> [e["source"] for e in data["evidence"]], [v["source"] for v in data["vetting_sources"]]
    (['S-01', 'S-02', 'S-03', 'S-04'], ['S-03', 'S-04'])
    >>> data["vetting_items"][0]["severity"]
    '3 (S-02 abstract)'
    """,
    "files that are absent or wrong": r"""
    >>> import sample, tempfile, pathlib
    >>> def error_of(folder):
    ...     try:
    ...         load(folder)
    ...     except Unreadable as e:
    ...         return str(e).split("spec.md: ")[1]
    >>> error_of(tempfile.mkdtemp(prefix="sota-empty-"))
    'No such file or directory'
    >>> folder = sample.folder()
    >>> (folder / "evidence.md").unlink(); (folder / "vetting.md").unlink()
    >>> data = load(folder)
    >>> data["evidence"], data["vetting_items"], data["has_vetting"]
    ([], [], False)

    A file that is not UTF-8 cannot be read. A byte order mark is accepted.

    >>> spec = folder / "spec.md"
    >>> good = spec.read_bytes()
    >>> _ = spec.write_bytes(b"\xef\xbb\xbf" + good)
    >>> load(folder)["is_aspect"]
    True
    >>> _ = spec.write_bytes(good + b"\xff\n")
    >>> error_of(folder)
    'the file is not UTF-8'
    """,
    "a write changes one cell only": r"""
    >>> import sample
    >>> folder = sample.folder()
    >>> spec = folder / "spec.md"
    >>> before = spec.read_text(encoding="utf-8")
    >>> row = load(folder)["checklist"][3]
    >>> set_cell(spec, row["_line"], column_of(row, "level"), "pending")
    True
    >>> spec.read_text(encoding="utf-8") == before.replace("| not admitted |", "| pending |")
    True

    Only a line feed ends a line. A different separator above the table must not move the write.

    >>> for separator in (chr(0x2028), chr(0x2029), "\x0c", "\x0b", "\x85"):
    ...     folder = sample.folder(("spec.md", "A small spec", "A small" + separator + "spec"))
    ...     row = load(folder)["checklist"][3]
    ...     assert row["id"] == "C-04" and set_cell(folder / "spec.md", row["_line"], 3, "pending")
    ...     assert load(folder)["checklist"][3]["level"] == "pending", repr(separator)

    A file with the line end of Windows keeps it.

    >>> folder = sample.folder()
    >>> _ = (folder / "spec.md").write_bytes((folder / "spec.md").read_bytes().replace(b"\n", b"\r\n"))
    >>> row = load(folder)["checklist"][1]
    >>> row["level"], set_cell(folder / "spec.md", row["_line"], 3, "pending")
    ('2, operative', True)
    >>> raw = (folder / "spec.md").read_bytes()
    >>> b"| pending |" in raw, raw.count(b"\r\n") == raw.count(b"\n")
    (True, True)
    """,
}


if __name__ == "__main__":
    sys.exit(selftest())
