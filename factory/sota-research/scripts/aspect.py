#!/usr/bin/env python3
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Reader of the folder of one aspect specification. Standard library only.

  load(folder)  reads spec.md, charter.md, evidence.md, vetting.md and trial.md into plain
                dictionaries and lists

The file charter.md is the charter of the aspect: the target, the principles with their priority
and the constraints of the owner. It has a head line with the state, and three tables: "Target",
"Principles" and "Constraints". Each row is one line of the charter. The identifier of a target
part is T-<n>, of a principle P-<n> and of a constraint K-<n>. The cell "Effect" of a principle
and of a constraint tells what the line does in the triage. A target part has the effect of its
cell "Level of the recipe". The file is optional.

The file vetting.md has five tables: "Sources", "Items", "Requirements", "Proposed boundaries"
and "Reading". The table "Requirements" has one row for each requirement that a source states
for a stakeholder. Its cell "Serves" names the lines of the charter that the requirement serves.
The table "Proposed boundaries" has one row for each boundary of section 1
that the owner did not decide, with the requirements that the boundary would take.
The table "Reading" has one row for each converted document of a source, with the pages that
the readers got and the pages that no reader got. The program index.py writes it.

A module for the programs in this folder; it needs Python 3.14.

The Markdown files are the only store. A section is found by its number, a table by its place
in the section. Each row is a dictionary: the header names in lowercase are the keys, and
"_line" (starts at 1) and "_file" tell where the row is. A file that is absent gives empty data;
only a missing spec.md is an error. An absent charter.md gives None for the charter.
"""

import datetime
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
INTENT = "intent of the owner"
STAKEHOLDERS = re.compile(r"\s*\(stakeholders:([^)]*)\)", re.I)
PAGE_SPAN = re.compile(r"(\d+)(?:\s*[-\u2013]\s*(\d+))?")
REQUIREMENT_ID = re.compile(r"\bR-\d+\b")
REQUIREMENT_RANGE = re.compile(r"\bR-(\d+) to R-(\d+)\b")
# The state of a boundary of section 1, in the line of the boundary: "(proposed)" or
# "(decided by the owner on <YYYY-MM-DD>)". A line without a state is proposed.
PROPOSED, DECIDED = "proposed", "decided"
BOUNDARY_STATE = re.compile(r"\(\s*((?:proposed|decided)\b[^)]*)\)", re.I)
DECIDED_ON = re.compile(r"decided by the owner on (\S+)")
DECIDED_START = "decided by the owner"
# The forms of the cell "Goes to" of a requirement. A requirement has no other exit.
EXITS = (
    ("item", re.compile(r"(C-\d+)")),
    ("decision", re.compile(r"3\.3:\s*(\S.*)")),
    ("skill", re.compile(r"(5)")),
    ("boundary", re.compile(r"boundary:\s*(\S.*)")),
    ("duplicate", re.compile(r"duplicate:\s*(R-\d+)")),
)
# The charter: the title of each table, the kind of its lines and the letter of their identifiers.
CHARTER_FILE = "charter.md"
CHARTER_TABLES = (
    ("Target", "target", "T"),
    ("Principles", "principle", "P"),
    ("Constraints", "constraint", "K"),
)
# The order of the kinds when two lines of the charter give the same level to an item.
KIND_ORDER = ("constraint", "target", "principle")
CHARTER_ID = re.compile(r"([TPK])-(\d+)")
DRAFT, REVIEWED = "draft", "reviewed"
REVIEWED_ON = re.compile(r"reviewed by the owner on (\d{4}-\d{2}-\d{2})(?!\d)")
# The forms of the cell "Effect" of a line of the charter. A cell holds one form or more, with a
# semicolon between two forms, or "none". FACTORY_RULE marks a line that is a rule for the
# factory and not for the content: no requirement must serve such a line.
NO_EFFECT = "none"
FACTORY_RULE = "none: rule of the factory"
LEVEL_EFFECT = re.compile(r"level\s+(\S+)")
NO_EXIT_EFFECT = re.compile(r"no exit:\s*(\S.*)")
NO_EXITS = ("3.3", "boundary", "not admitted")
# The exits of a requirement that an effect "no exit" closes, by the kind of the exit.
CLOSED_EXITS = {"decision": "3.3", "boundary": "boundary"}
CALCULATION = "calculation"


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


def view_of(row):
    """The name of the view in the View cell of a checklist row, or "".

    >>> view_of({"view": " `security` "}), view_of({"view": "quality"}), view_of({})
    ('security', 'quality', '')
    """
    return row.get("view", "").strip().strip("`").strip()


def names_of(cell):
    """The names in a cell that holds a list, for example the cell Views of a source.

    A comma or a semicolon is between two names.

    >>> names_of("storage, `operation`; quality"), names_of(" all "), names_of(""), names_of(None)
    (['storage', 'operation', 'quality'], ['all'], [], [])
    """
    names = (part.strip().strip("`").strip() for part in re.split(r"[,;]", cell or ""))
    return [name for name in names if name]


def pages_of(cell):
    """The pages in a cell that holds pages and ranges of pages, sorted. "none" gives no page.

    >>> pages_of("3, 7-9; 8"), pages_of("none"), pages_of(""), pages_of(None)
    ([3, 7, 8, 9], [], [], [])
    """
    found = PAGE_SPAN.findall(cell or "")
    return sorted({page for a, b in found for page in range(int(a), int(b or a) + 1)})


def exit_of(cell):
    """(kind, name) of the cell "Goes to" of a requirement. The kind is None for a different text.

    A requirement goes to a checklist item, to a decision of section 3.3, to an implementation
    skill of section 5 or to a boundary of section 1, or it is a duplicate of a different row.

    >>> exit_of("C-02"), exit_of("3.3: How frequently to make a backup"), exit_of("5")
    (('item', 'C-02'), ('decision', 'How frequently to make a backup'), ('skill', '5'))
    >>> exit_of("boundary: `recovery`"), exit_of("`duplicate: R-05`")
    (('boundary', 'recovery'), ('duplicate', 'R-05'))

    Each other text is not an exit.

    >>> other = ("one source only states it", "depends on context", "3.3", "C-02, C-03", "boundary:", None)
    >>> for cell in other:
    ...     print(exit_of(cell))
    (None, 'one source only states it')
    (None, 'depends on context')
    (None, '3.3')
    (None, 'C-02, C-03')
    (None, 'boundary:')
    (None, '')
    """
    cell = (cell or "").strip().strip("`").strip()
    for kind, form in EXITS:
        found = form.fullmatch(cell)
        if found:
            return kind, found.group(1).strip().strip("`").strip()
    return None, cell


def requirement_ids(cell):
    """The identifiers of requirements in a cell. "R-02 to R-04" gives the three of them.

    >>> requirement_ids("R-02 to R-04, R-09; `R-011`"), requirement_ids("none"), requirement_ids(None)
    (['R-011', 'R-02', 'R-03', 'R-04', 'R-09'], [], [])
    """
    cell = cell or ""
    ids = set(REQUIREMENT_ID.findall(cell))
    for a, b in REQUIREMENT_RANGE.findall(cell):
        width = len(a)
        ids.update(f"R-{n:0{width}d}" for n in range(int(a), int(b) + 1))
    return sorted(ids)


def boundary_state(text):
    """(state, detail) of the line of a boundary of section 1.

    The state is "proposed" or "decided". A boundary takes a requirement away from the aspect
    only after the owner decided it. The detail of a decided boundary is the date of the decision.
    A line without a state is proposed.

    >>> boundary_state("what it owns. (proposed) (S-01 section 5)"), boundary_state("it owns. (judgement)")
    (('proposed', None), ('proposed', None))
    >>> boundary_state("what it owns. (decided by the owner on 2026-01-12) (S-01 section 5)")
    ('decided', '2026-01-12')

    A decided state needs a date: the state is then "undated". Each other text that starts with
    one of the two words is not a state: the state is then None, and the detail is the text.

    >>> other = ("(decided by the owner in the review)", "(decided by the owner on 2026-13-40)")
    >>> other += ("(decided by the session)", "(Proposed)", "(proposed by a reader)")
    >>> for text in (*other, "(proposed) (decided by the owner on 2026-01-12)", None):
    ...     print(boundary_state(text))
    ('undated', 'decided by the owner in the review')
    ('undated', 'decided by the owner on 2026-13-40')
    (None, 'decided by the session')
    (None, 'Proposed')
    (None, 'proposed by a reader')
    (None, 'proposed; decided by the owner on 2026-01-12')
    ('proposed', None)
    """
    found = [state.strip() for state in BOUNDARY_STATE.findall(text or "")]
    if not found or found == [PROPOSED]:
        return PROPOSED, None
    if len(found) > 1:
        return None, "; ".join(found)
    on = DECIDED_ON.fullmatch(found[0])
    if on:
        try:
            return DECIDED, datetime.date.fromisoformat(on.group(1)).isoformat()
        except ValueError:
            return "undated", found[0]
    return ("undated" if found[0].startswith(DECIDED_START) else None), found[0]


def effect_of(cell):
    """The effect of a line of the charter in the triage, from its cell "Effect".

    The result is a dictionary. "level": the level of the recipe that the line gives, or None.
    "no exit": the exits that the line closes, sorted. "factory": the line is a rule for the
    factory. "unknown": each part of the cell that is none of the forms. "wrong levels": each
    level that is not 1, 2 or 3.

    >>> effect_of("level 1; no exit: not admitted")
    {'level': 1, 'no exit': ['not admitted'], 'factory': False, 'unknown': [], 'wrong levels': []}
    >>> effect_of("`no exit: 3.3`; no exit: boundary")["no exit"], effect_of("none")["no exit"]
    (['3.3', 'boundary'], [])
    >>> effect_of("none: rule of the factory")["factory"], effect_of("none")["factory"]
    (True, False)

    Two levels in one cell give the lowest one.

    >>> effect_of("level 3; level 2")["level"]
    2

    A text that is none of the forms is not an effect. An empty cell is not an effect.

    >>> cells = ("level 4", "level one; level 2", "first claim on level 1", "no exit: 5", "none; level 1")
    >>> for cell in (*cells, "", None):
    ...     found = effect_of(cell)
    ...     print(found["level"], found["unknown"], found["wrong levels"])
    None [] ['4']
    2 [] ['one']
    None ['first claim on level 1'] []
    None ['no exit: 5'] []
    1 ['none'] []
    None [''] []
    None [''] []
    """
    cell = (cell or "").strip().strip("`").strip()
    out = {"level": None, "no exit": [], "factory": cell == FACTORY_RULE, "unknown": [], "wrong levels": []}
    if cell in (NO_EFFECT, FACTORY_RULE):
        return out
    levels, closed = [], set()
    for part in (p.strip().strip("`").strip() for p in cell.split(";")):
        level, no_exit = LEVEL_EFFECT.fullmatch(part), NO_EXIT_EFFECT.fullmatch(part)
        if level and level.group(1) in ("1", "2", "3"):
            levels.append(int(level.group(1)))
        elif level:
            out["wrong levels"].append(level.group(1))
        elif no_exit and no_exit.group(1) in NO_EXITS:
            closed.add(no_exit.group(1))
        else:
            out["unknown"].append(part)
    out["level"], out["no exit"] = min(levels, default=None), sorted(closed)
    return out


def charter_state(text):
    """(state, date) of the head line of a charter. The state is "draft", "reviewed" or None.

    The owner reviews the charter. The state "reviewed" needs the date of the review. A sentence
    can follow the state.

    >>> charter_state("draft"), charter_state("reviewed by the owner on 2026-01-06")
    (('draft', None), ('reviewed', '2026-01-06'))
    >>> charter_state("reviewed by the owner on 2026-01-06. The owner confirmed the order.")
    ('reviewed', '2026-01-06')
    >>> for text in ("reviewed", "reviewed by the owner on 2026-13-40", "drafted", "done", "", None):
    ...     print(charter_state(text))
    (None, None)
    (None, None)
    (None, None)
    (None, None)
    (None, None)
    (None, None)
    """
    text = (text or "").strip().strip("`").strip()
    if re.match(r"draft\b", text):
        return DRAFT, None
    on = REVIEWED_ON.match(text)
    try:
        return (REVIEWED, datetime.date.fromisoformat(on.group(1)).isoformat()) if on else (None, None)
    except ValueError:
        return None, None


def charter_key(ident):
    """The key that puts the identifiers of the lines of a charter in order: the number counts.

    >>> sorted(["P-10", "P-2", "K-1", "other"], key=charter_key)
    ['K-1', 'P-2', 'P-10', 'other']
    """
    found = CHARTER_ID.fullmatch(ident or "")
    return (0, found.group(1), int(found.group(2)), "") if found else (1, "", 0, ident or "")


def serves_of(cell):
    """The lines of the charter that the cell "Serves" of a requirement names. "none" gives no line.

    A comma is between two identifiers.

    >>> serves_of("P-2, `K-1`"), serves_of("none"), serves_of(" `none` "), serves_of(""), serves_of(None)
    (['P-2', 'K-1'], [], [], [], [])
    >>> serves_of("the first principle; T-1")
    ['the first principle', 'T-1']
    """
    names = names_of(cell)
    return [] if names == [NO_EFFECT] else names


def read_charter(folder):
    r"""The charter of a specification: the file charter.md beside spec.md. None without the file.

    The result has the state, the date of the review, and one dictionary for each line of the
    charter, in the order of the file. A line has its identifier, its kind, its text, its
    priority and its effect.

    >>> import sample
    >>> charter = read_charter(sample.folder())
    >>> charter["state"], charter["date"], charter["_line"], charter["_file"]
    ('reviewed', '2026-01-06', 3, 'charter.md')
    >>> for line in charter["lines"]:
    ...     effect = line["effect"]
    ...     print(line["id"], line["kind"], line["priority"], effect["level"], effect["no exit"])
    T-1 target None 1 []
    T-2 target None 2 []
    P-1 principle 1 None ['3.3']
    P-2 principle 2 None ['boundary']
    K-1 constraint None None ['not admitted']
    K-2 constraint None None []
    >>> charter["lines"][0]["text"], charter["lines"][5]["effect"]["factory"], charter["lines"][5]["_line"]
    ('a backup is made without a person', True, 28)

    A target part has the effect of its cell "Level of the recipe". A level that is not 1, 2 or 3
    is a wrong level.

    >>> wrong = ("charter.md", "| no drill | 1 |", "| no drill | high |")
    >>> read_charter(sample.folder(wrong))["lines"][0]["effect"]["wrong levels"]
    ['high']

    A file without a head line and without a table gives no state and no line.

    >>> folder = sample.folder()
    >>> _ = (folder / "charter.md").write_text("A text.\n", encoding="utf-8")
    >>> charter = read_charter(folder)
    >>> charter["state"], charter["state text"], charter["lines"]
    (None, '', [])
    >>> (folder / "charter.md").unlink()
    >>> read_charter(folder) is None
    True
    """
    path = pathlib.Path(folder) / CHARTER_FILE
    if not path.is_file():
        return None
    doc = Doc(path)
    head = doc.head()
    state, date = charter_state(head.get("state"))
    lines = []
    for title, kind, _ in CHARTER_TABLES:
        found = doc.titled(title)
        for row in doc.table(found[1]) if found else []:
            effect, text = effect_of(row.get("effect")), row.get(kind, "")
            if kind == "target":
                level = row.get("level of the recipe", "").strip().strip("`").strip()
                effect, text = effect_of(NO_EFFECT), row.get("part of the target", "")
                effect |= {"level": int(level)} if level in ("1", "2", "3") else {"wrong levels": [level]}
            line = {"id": row.get("id", "").strip().strip("`").strip(), "kind": kind, "table": title}
            line |= {"text": text, "priority": row.get("priority"), "effect": effect}
            lines.append(line | {"_line": row["_line"], "_file": CHARTER_FILE})
    return {
        "state": state,
        "date": date,
        "state text": head.get("state", ""),
        "lines": sorted(lines, key=lambda line: line["_line"]),
        "_line": head["_line"],
        "_file": CHARTER_FILE,
    }


def stakeholders_of(text):
    """The stakeholders that the line of a view names, in the form "(stakeholders: a, b)".

    >>> stakeholders_of("what the view holds. (stakeholders: operators, `owners of the data`) (S-01)")
    ['operators', 'owners of the data']
    >>> stakeholders_of("what the view holds. (S-01)"), stakeholders_of("(stakeholders: )")
    ([], [])
    """
    found = STAKEHOLDERS.search(text or "")
    names = (name.strip().strip("`").strip() for name in found.group(1).split(",")) if found else ()
    return [name for name in names if name]


def without_stakeholders(text):
    """The line of a view without the part that names its stakeholders.

    >>> without_stakeholders("what the view holds. (stakeholders: operators) (S-01 section 2)")
    'what the view holds. (S-01 section 2)'
    """
    return STAKEHOLDERS.sub("", text or "")


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
    >>> [v["name"] for v in data["views"]], [view_of(c) for c in data["checklist"]][:3]
    (['storage', 'operation'], ['storage', 'operation', 'storage'])
    >>> [(t["name"], t["text"][:13]) for t in data["targets"]]
    [('restore drill', 'three levels:')]

    The stakeholders of the aspect are a field of section 1. Each view names its stakeholders.

    >>> [s["name"] for s in data["stakeholders"]], [v["stakeholders"] for v in data["views"]]
    (['operators', 'owners of the data'], [['owners of the data'], ['operators']])

    The intent of the owner has one line for each answer: a quote with its date, or "(no answer)".

    >>> [(i["name"], i["text"][-12:]) for i in data["intent"]]
    [('meaning', '(2026-01-05)'), ('result', '(2026-01-05)'), ('not wanted', '(no answer)')]

    A field without such lines gives its text as one line. A specification without the field
    gives no line.

    >>> one = "- **Intent of the owner**: (no answer)"
    >>> text = sample.SPEC.replace("\n".join(sample.INTENT) + "\n", "")
    >>> text = text.replace(sample.INTENT_HEAD, one)
    >>> folder = sample.folder()
    >>> _ = (folder / "spec.md").write_text(text, encoding="utf-8")
    >>> [(i["name"], i["text"]) for i in load(folder)["intent"]]
    [('intent of the owner', '(no answer)')]
    >>> _ = (folder / "spec.md").write_text(text.replace(one + "\n", ""), encoding="utf-8")
    >>> load(folder)["intent"]
    []

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

    The table "Requirements" of vetting.md has one row for each requirement that a source states.
    The cell "Goes to" names the one exit of the requirement. Each source names the views that it
    was read for.

    >>> [(r["id"], r["stakeholder"], view_of(r), r["goes to"]) for r in data["requirements"]][5:]
    [('R-06', 'operators', 'operation', 'duplicate: R-05'),
     ('R-07', 'operators', 'operation', '3.3: How frequently to make a backup'),
     ('R-08', 'operators', 'operation', '5')]
    >>> data["requirements"][0]["_file"], [names_of(s["views"]) for s in data["sources"]][1:3]
    ('vetting.md', [['storage', 'operation'], ['operation']])

    The cell "Serves" of a requirement names the lines of the charter that the requirement
    serves, or "none". The charter is the file charter.md. A specification without the file has
    no charter.

    >>> [serves_of(r["serves"]) for r in data["requirements"]][1:5], data["charter"]["state"]
    ([[], ['T-2', 'P-1'], [], ['T-1', 'P-2', 'K-1']], 'reviewed')
    >>> load(sample.folder(charter=False))["charter"] is None
    True

    Each boundary of section 1 has a state. A boundary line without a state is proposed. The
    table "Proposed boundaries" of vetting.md has one row for each proposed boundary.

    >>> data["boundaries"], data["proposed_boundaries"]
    ([], [])
    >>> edits = (("spec.md", sample.BOUNDARIES, sample.BOUNDARIES_NAMED), sample.PROPOSED_TABLE)
    >>> data = load(sample.folder(*edits))
    >>> [(b["name"], b["state"], b["date"]) for b in data["boundaries"]]
    [('recovery', 'decided', '2026-01-12'), ('tests', 'proposed', None), ('archive', 'proposed', None)]
    >>> rows = data["proposed_boundaries"]
    >>> [(r["boundary"], r["requirements that it would take"], r["_file"]) for r in rows]
    [('tests', 'R-03', 'vetting.md'), ('archive', 'none', 'vetting.md')]
    >>> data = load(sample.folder())

    The table "Reading" of vetting.md has one row for each converted document of a source.

    >>> data["has_reading"], [(r["source"], r["document"], r["pages"]) for r in data["reading"]]
    (True, [('S-01', 'S-01', '6'), ('S-02', 'S-02', '2')])
    >>> [(r["given to readers"], r["not read"]) for r in data["reading"]]
    [('1-6', 'none'), ('1-2', 'none')]
    >>> load(sample.folder(("vetting.md", "## Reading", "## Other")))["has_reading"]
    False

    The record of the trials has the table of the trials and the table of their findings.

    >>> [t["id"] for t in data["trials"]], data["trials"][0]["plan"]
    (['T-01'], 'not kept')
    >>> [(f["id"], f["trial"], bool(f["viewpoint"]), f["route"]) for f in data["trial_findings"]]
    [('F-01', 'T-01', True, 'recipe'), ('F-02', 'T-01', True, 'implementation skill')]
    >>> data["trial_findings"][0]["_file"], data["trial_findings"][0]["_line"]
    ('trial.md', 13)

    Only spec.md is necessary. An absent evidence, vetting or trial record gives empty data.

    >>> folder = sample.folder()
    >>> [(folder / name).unlink() for name in ("evidence.md", "vetting.md", "trial.md", "charter.md")]
    [None, None, None, None]
    >>> data = load(folder)
    >>> data["evidence"], data["vetting_items"], data["has_vetting"], data["trials"], data["trial_findings"]
    ([], [], False, [], [])
    >>> data["requirements"], data["proposed_boundaries"], data["reading"], data["has_reading"]
    ([], [], [], False)
    >>> data["charter"] is None
    True
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
        "requirements": [],
        "proposed_boundaries": [],
        "reading": [],
        "has_reading": False,
        "has_vetting": False,
        "charter": read_charter(folder),
        "trials": [],
        "trial_findings": [],
    }
    data["risk_dimensions"] = data["aspect"].get("risk dimensions", {}).get("items", [])
    data["views"] = data["aspect"].get("views", {}).get("items", [])
    data["targets"] = data["aspect"].get("targets", {}).get("items", [])
    data["stakeholders"] = data["aspect"].get("stakeholders", {}).get("items", [])
    data["boundaries"] = data["aspect"].get("boundaries", {}).get("items", [])
    for view in data["views"]:
        view["stakeholders"] = stakeholders_of(view["text"])
    for boundary in data["boundaries"]:
        boundary["state"], detail = boundary_state(boundary["text"])
        boundary["date"] = detail if boundary["state"] == DECIDED else None
        boundary["state text"] = detail if boundary["state"] != DECIDED else None
    intent = data["aspect"].get(INTENT, {})
    whole = {"name": INTENT, "text": intent.get("value"), "_line": intent.get("_line")}
    data["intent"] = intent.get("items") or ([whole] if whole["text"] else [])
    if (folder / "evidence.md").is_file():
        data["evidence"] = Doc(folder / "evidence.md").table((0, 10**9), "source")
    data["has_vetting"] = (folder / "vetting.md").is_file()
    tables = {
        "vetting.md": (
            ("Sources", "vetting_sources"),
            ("Items", "vetting_items"),
            ("Requirements", "requirements"),
            ("Proposed boundaries", "proposed_boundaries"),
            ("Reading", "reading"),
        ),
        "trial.md": (("Trials", "trials"), ("Findings", "trial_findings")),
    }
    for name, parts in tables.items():
        if (folder / name).is_file():
            record = Doc(folder / name)
            for title_, key in parts:
                found = record.titled(title_)
                data[key] = record.table(found[1]) if found else []
                data["has_reading"] = data["has_reading"] or bool(found and key == "reading")
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
    ...     done = set_cell(folder / "spec.md", row["_line"], 4, "pending")
    ...     print(row["id"], done, load(folder)["checklist"][3]["level"])
    C-04 True pending
    C-04 True pending
    C-04 True pending
    C-04 True pending
    C-04 True pending

    A file with the line end of Windows keeps it.

    >>> _ = (folder / "spec.md").write_bytes(sample.SPEC.replace("\n", "\r\n").encode("utf-8"))
    >>> row = load(folder)["checklist"][1]
    >>> row["level"], set_cell(folder / "spec.md", row["_line"], 4, "pending")
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
    (0, 4, -1, -1)
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
