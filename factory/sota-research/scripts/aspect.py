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
    r"""The (start, end) of each cell of a table row. A pipe after a backslash is text.

    >>> line = r"| a | b \| c |"
    >>> [line[a:b] for a, b in cell_spans(line)]
    [' a ', ' b \\| c ']
    >>> cell_spans("no table row")
    []
    """
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
    r"""The text of a file in UTF-8, with its line ends as they are.

    >>> import tempfile
    >>> path = pathlib.Path(tempfile.mkdtemp(prefix="sota-read-")) / "a.md"
    >>> _ = path.write_bytes(b"\xef\xbb\xbfone\r\ntwo\n")
    >>> read_text(path)
    'one\r\ntwo\n'

    A file that is absent or is not UTF-8 cannot be read. The caller reports it; it is not a crash.

    >>> def error_of(path):
    ...     try:
    ...         read_text(path)
    ...     except Unreadable as e:
    ...         return str(e).split(": ", 1)[1]
    >>> _ = path.write_bytes(b"one\xff\n")
    >>> error_of(path), error_of(path.with_name("absent.md"))
    ('the file is not UTF-8', 'No such file or directory')
    """
    try:
        with open(path, encoding="utf-8-sig", newline="") as f:
            return f.read()
    except OSError as e:
        raise Unreadable(f"{path}: {e.strerror or e}") from e
    except UnicodeDecodeError as e:
        raise Unreadable(f"{path}: the file is not UTF-8") from e


def write_text(path, text):
    r"""Write a file in UTF-8. The line ends stay as they are in the text.

    >>> import tempfile
    >>> path = pathlib.Path(tempfile.mkdtemp(prefix="sota-write-")) / "a.md"
    >>> write_text(path, "one\r\ntwo\n")
    >>> path.read_bytes()
    b'one\r\ntwo\n'
    """
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


class Doc:
    r"""One Markdown file as lines, headings, tables and fields.

    >>> import tempfile
    >>> path = pathlib.Path(tempfile.mkdtemp(prefix="sota-doc-")) / "spec.md"
    >>> _ = path.write_text('''# Title
    ...
    ... **Branch**: `001-a` | **Accepted**: pending
    ...
    ... ## 1. First
    ...
    ... - **Aspect**: one
    ...   line more
    ... - **Risk dimensions**: the list.
    ...   - `operative`: Can it be undone?
    ...     Opinion: yes.
    ...
    ... Text after the fields.
    ...
    ... ```text
    ... ## 9. Not a heading: it is in a code block
    ... ```
    ...
    ... ### 1.1 Table
    ...
    ... | Id | Name |
    ... |---|---|
    ... | S-01 | one \\| two |
    ... | S-02 |
    ...
    ... ### Recipe skill and agent: backups
    ...
    ... ## 2. Second
    ... ''', encoding="utf-8")
    >>> doc = Doc(path)
    >>> [(level, number, title) for _, level, number, title in doc.headings]
    [(1, None, 'Title'), (2, '1', 'First'), (3, '1.1', 'Table'),
     (3, None, 'Recipe skill and agent: backups'), (2, '2', 'Second')]

    A section is found by its number. It ends at the next heading of its level or above.

    >>> doc.section("1"), doc.section("1.1"), doc.section("7")
    ((5, 27), (19, 25), None)
    >>> doc.titled("Recipe skill"), doc.titled("No such title")
    (('Recipe skill and agent: backups', (26, 27)), None)
    >>> doc.text(doc.section("2")), doc.text(None)
    ('', '')

    The head line and the fields. A field can continue on the next line and can have sub-items.

    >>> doc.head()
    {'branch': '001-a', 'accepted': 'pending', '_line': 3}
    >>> fields = doc.fields(doc.section("1"))
    >>> fields["aspect"]["value"], fields["aspect"]["_line"]
    ('one line more', 7)
    >>> fields["risk dimensions"]["value"], fields["risk dimensions"]["items"]
    ('the list.', [{'name': 'operative', 'text': 'Can it be undone? Opinion: yes.', '_line': 10}])
    >>> doc.fields(None), doc.fields(doc.section("2"))
    ({}, {})

    A table gives one dictionary for each row. A short row has no key for a missing cell.

    >>> rows = doc.table(doc.section("1.1"), "id")
    >>> [(r["id"], r.get("name"), r["_line"], r["_file"]) for r in rows]
    [('S-01', 'one | two', 23, 'spec.md'), ('S-02', None, 24, 'spec.md')]
    >>> doc.table(doc.section("1.1"), "other header"), doc.table(None), len(doc.tables())
    ([], [], 1)

    A file without a head line gives the line 1 for a finding.

    >>> _ = path.write_text("plain text\n", encoding="utf-8")
    >>> Doc(path).head(), Doc(path).headings
    ({'_line': 1}, [])
    """

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
    r"""Read the folder of one specification into plain dictionaries and lists.

    >>> import sample
    >>> data = load(sample.folder())
    >>> data["is_aspect"], data["title"], data["head"]["branch"], data["head"]["accepted"]
    (True, 'Backups of project data', '900-backups', 'A. Person, 2026-01-15')
    >>> data["aspect"]["contexts"]["value"]
    'the size of the data; who operates the software; the place where the data is. (S-01 section 1)'
    >>> [d["name"] for d in data["risk_dimensions"]]
    ['operative', 'regulatory']

    Each table is found in its section, and each row knows its place.

    >>> [s["id"] for s in data["sources"]], data["sources"][0]["version or date"]
    (['S-01', 'S-02', 'S-03', 'S-04'], '2.0, 2025-03')
    >>> [c["level"] for c in data["checklist"]]
    ['1', '2, operative', '3, regulatory', 'not admitted', '1']
    >>> [len(data[k]) for k in ("context_decisions", "disagreement", "watch", "decisions", "glossary")]
    [1, 1, 1, 2, 1]
    >>> data["skill_name"], data["skill"]["goal"]["value"][:11], data["goals"][:13], data["order"][:11]
    ('backups', 'Each record', 'A lost record', '1. Find out')
    >>> [e["source"] for e in data["evidence"]], [v["source"] for v in data["vetting_sources"]]
    (['S-01', 'S-02', 'S-03', 'S-04'], ['S-03', 'S-04'])
    >>> data["vetting_items"][0]["severity"], data["has_vetting"]
    ('3 (S-02 abstract)', True)

    Only spec.md is necessary. An absent evidence record or vetting record gives empty data.

    >>> folder = sample.folder()
    >>> (folder / "evidence.md").unlink(), (folder / "vetting.md").unlink()
    (None, None)
    >>> data = load(folder)
    >>> data["evidence"], data["vetting_items"], data["has_vetting"]
    ([], [], False)
    >>> (folder / "spec.md").unlink()
    >>> load(folder)
    Traceback (most recent call last):
        ...
    Unreadable: ...spec.md: No such file or directory

    A file that is not a specification of an aspect is read also; it only has no aspect data.

    >>> _ = (folder / "spec.md").write_text("# Feature Specification: a tool\n", encoding="utf-8")
    >>> data = load(folder)
    >>> data["is_aspect"], data["title"], data["skill_name"], data["sources"]
    (False, 'a tool', '', [])
    """
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

    >>> import sample
    >>> folder = sample.folder()
    >>> row = load(folder)["checklist"][3]
    >>> row["id"], row["level"]
    ('C-04', 'not admitted')
    >>> set_cell(folder / "spec.md", row["_line"], column_of(row, "level"), "pending")
    True
    >>> read_text(folder / "spec.md") == sample.SPEC.replace("| not admitted |", "| pending |")
    True

    A pipe in the new text is written as text. A cell that the row does not have is not written.

    >>> path = folder / "t.md"
    >>> _ = path.write_text("| a | b |\n|---|---|\n| short |\n", encoding="utf-8")
    >>> set_cell(path, 3, 1, "x"), set_cell(path, 9, 0, "x"), set_cell(path, 3, -1, "x")
    (False, False, False)
    >>> set_cell(path, 3, 0, "x | y"), read_text(path).splitlines()[2]
    (True, '| x \\| y |')

    Only a line feed ends a line, as in the reader. Thus a different separator above the table
    does not move the write to a wrong row.

    >>> for separator in (chr(0x2028), chr(0x2029), "\x0c", "\x0b", "\x85"):
    ...     folder = sample.folder(("spec.md", "A small spec", "A small" + separator + "spec"))
    ...     row = load(folder)["checklist"][3]
    ...     done = set_cell(folder / "spec.md", row["_line"], 3, "pending")
    ...     print(row["id"], done, load(folder)["checklist"][3]["level"])
    C-04 True pending
    C-04 True pending
    C-04 True pending
    C-04 True pending
    C-04 True pending

    A file with the line end of Windows keeps it.

    >>> _ = (folder / "spec.md").write_bytes(sample.SPEC.replace("\n", "\r\n").encode("utf-8"))
    >>> row = load(folder)["checklist"][1]
    >>> row["level"], set_cell(folder / "spec.md", row["_line"], 3, "pending")
    ('2, operative', True)
    >>> raw = (folder / "spec.md").read_bytes()
    >>> b"| pending |" in raw, raw.count(b"\r\n") == raw.count(b"\n")
    (True, True)

    A file that is not UTF-8 cannot be read.

    >>> _ = path.write_bytes(b"| a |\xff\n")
    >>> set_cell(path, 1, 0, "x")
    Traceback (most recent call last):
        ...
    Unreadable: ...t.md: 'utf-8' codec can't decode byte 0xff in position 5: invalid start byte
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
    """The position of a column in the table of the row, or -1.

    >>> import sample
    >>> row = sample.load()["checklist"][0]
    >>> column_of(row, "id"), column_of(row, "level"), column_of(row, "no such column"), column_of({}, "id")
    (0, 3, -1, -1)
    """
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
    flags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE | doctest.IGNORE_EXCEPTION_DETAIL
    result = doctest.testmod(sys.modules[name], optionflags=flags)
    print(f"{result.attempted} examples, {result.failed} failed")
    return 1 if result.failed or not result.attempted else 0


if __name__ == "__main__":
    sys.exit(selftest())
