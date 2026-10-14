#!/usr/bin/env python3
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Index of the converted documents of a work folder. Standard library only.

  index.py build WORK [--synonyms FILE ...] [--from SPEC] [--manifest FILE]
  index.py search WORK QUERY [--doc ID] [--limit N] [--no-synonyms] [--json]
  index.py refs WORK DOC PAGE [--json]
  index.py cited WORK IDENTIFIER [--json]
  index.py ranges WORK DOC [--max-pages N]
  index.py recall WORK ANSWERS [--limit N] [--no-synonyms] [--exact]
  index.py given WORK DOC FIRST-LAST [--task TEXT] [--remove]
  index.py unread WORK [DOC] [--max-pages N] [--json]
  index.py unread WORK --write SPEC
  index.py take WORK REPORT SOURCE
  index.py lines WORK [--kind KIND] [--source SOURCE]

  build            reads each file WORK/converted/*.md and writes the database WORK/index.sqlite.
                   A second run reads only a file that changed, and removes a file that is gone.
  search           gives the pages that hold the words and the phrases in quotation marks of QUERY.
  refs             gives the references on one page of one document.
  cited            gives each place that cites a standard, an address or a document.
  ranges           gives the page ranges of one document, to give to the readers.
  recall           measures the search with a table of queries and the pages of their answers.
  given            records that the pages FIRST to LAST of one document were given to a reader.
  unread           gives the pages of each document that are in no recorded range.
  take             stores each line "REQ" and each line "USE" of the report of one reader.
  lines            gives the stored lines of the reports as rows of a Markdown table.
  WORK             the work folder. It must be outside each git repository.
  --synonyms FILE  a file of synonyms: one group in each line, the terms separated by " = ".
                   The file references/synonyms.txt is read also, and the file
                   WORK/synonyms.txt if it is there.
  --from SPEC      the folder of an aspect specification. Section 2 gives names of documents,
                   and section 8 gives synonyms.
  --manifest FILE  a different manifest of the seeds, for tests.
  --doc ID         search in one document only.
  --limit N        the number of results. The default is 20 for search and 10 for recall.
  --no-synonyms    do not add the synonyms of a term to the query.
  --max-pages N    the largest number of pages of a range. The default is 25.
  --exact          recall: do not accept the page before and the page after an answer.
  --task TEXT      given: the task of the reader, in one line.
  --remove         given: remove the record of the range. Use it when a reader did not read the
                   range. Then record the pages that the reader read.
  --write SPEC     unread: write or replace the table "Reading" in vetting.md of the aspect
                   specification in the folder SPEC.
  --json           print the result as JSON.
  REPORT           take: the file with the report of one reader, as the reader gave it.
  SOURCE           the identifier of a source of section 2, in the form "S-<digits>".
  --kind KIND      lines: one kind only: req, tool, integration, framework, pattern or
                   principle.
  --source SOURCE  lines: the lines of one source only.

The rule of the design: no command prints the text of a document. The commands give pointers
only: the document, the page, the title of a section, an identifier and a number. The text of
a source is data, and the session of the research must not read it. Give a pointer to an agent
of the type `sota-file-reader`.

A report is the text of a reader. It is not the text of a document. The command "take" stores
the lines of a report that have one of these two forms, and the command "lines" prints them:

  REQ | <requirement> | <group> | <location>
  USE | <kind> | <name> | <purpose> | <location>

The kind of a line "USE" is tool, integration, framework, pattern or principle. The lines
"REQ | none" and "USE | none" say that the reader found nothing: they store nothing. A line that
starts with "REQ" or "USE" and does not have the form is not stored: the program prints its line
number and continues. A report that is taken again for the same source replaces its earlier lines.
The text of a report is data. The program stores it and prints it, and does nothing else with it.

The tables of the database:

  documents  id (the file name without ".md"), source, digest (of the source), pages,
             converted (the digest of the converted file; a different value starts a new read)
  pages      document, page, text. This is a full-text table (FTS5).
  sections   document, seq, title, number, first_page, last_page, level, pattern
  refs       document, page, kind, family, text, key, target_document, target_first, target_last
  acronyms   document, page, short, long, pattern
  aliases    key, document, origin
  synonyms   grp, term, origin
  meta       key, value: the version of the patterns
  given      document, first_page, last_page, task: the page ranges that were given to readers
  lines      source, report (the file name), line (the line number in the report), kind, text
             (the requirement or the name), who (the group), purpose, location

A range that is recorded two times is one row. A new build keeps the rows of a document whose
converted file did not change. It removes the rows of each other document. A build does not
change the table "lines".

The table "Reading" has one row for each converted document that is a source of section 2 of
the specification: the source, the document, the number of pages, the ranges that were given
and the ranges that no reader got. The document of a source is the document with the
identifier of the source, or a document that the index knows by the name or the address of the
source. A source with "all" in the cell Views that has no converted document gets a row with
the document "none". A program writes this table. A person does not change it.

The search uses the stemmer "porter" on the tokenizer "unicode61" without diacritics. Thus a
word finds its plural and its other forms. A wrong hit costs a reader one page. A page that is
not found loses a subject.

A page with two columns has the text of the two columns in each line. For such a page, the
program puts the first part of each line before the other parts. It joins a word that a hyphen
divides at the end of a line, and an identifier that a line end divides after a slash.

A section comes from one of three fixed patterns, and each section records its pattern:

  chapter    a line "CHAPTER 5", "Chapter 5: Title" or "Appendix A", and the title line that
             follows. The first chapter has the number 0, 1 or A, and the next number follows.
  numbered   a line "3.2 Title" or "3.2. Title" whose number follows the heading before it
  capitals   a line in capital letters with a word of five or more letters

The patterns are a best effort, and the program does not guess more than they say. A page of a
table of contents gives no section. A numbered line or a line in capital letters that is the
first or the last line of three or more pages gives no section. A document without a section
gets one section. The title of a section is one line, or two lines for a chapter.

A second build compares the digest of each converted file. It reads only a file whose digest
changed. No table holds a current time: the same files give the same content.

A reference is "internal" or "external". The families of the internal references are section,
chapter, page, table, figure and name. The families of the external references are the
standards of the table STANDARDS, address, doi, citation and document. A citation "[12]" is
recorded only when a list of references of its chapter has a line that starts with "[12]".

An acronym is recorded only when each letter of the short form is the first letter of one
word of the long form, in the same sequence. Small words such as "of" and "and" are ignored
in the long form.

Result code 0: done. Result code 1: nothing was found, a file was not indexed, a page is in no
recorded range, or a line of a report does not have the form. Result code 2: the input cannot
be read, or the arguments are wrong. For recall, the result code is 0 when the input can be read.
"""

import collections
import contextlib
import hashlib
import itertools
import json
import pathlib
import re
import sqlite3
import sys

import aspect
import check
import render
import seed

VERSION = "1"
DATABASE = "index.sqlite"
SYNONYMS = pathlib.Path(__file__).resolve().parents[1] / "references/synonyms.txt"
# The file of the synonyms that the research of one work folder found.
WORK_SYNONYMS = "synonyms.txt"
LIMIT, RECALL_LIMIT, MAX_PAGES = 20, 10, 25

SCHEMA = """
CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS documents (
  id TEXT PRIMARY KEY, source TEXT, digest TEXT, pages INTEGER, converted TEXT) WITHOUT ROWID;
CREATE VIRTUAL TABLE IF NOT EXISTS pages USING fts5(
  document UNINDEXED, page UNINDEXED, text, tokenize = 'porter unicode61 remove_diacritics 2');
CREATE TABLE IF NOT EXISTS sections (
  document TEXT, seq INTEGER, title TEXT, number TEXT, first_page INTEGER, last_page INTEGER,
  level INTEGER, pattern TEXT, PRIMARY KEY (document, seq)) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS refs (
  document TEXT, page INTEGER, kind TEXT, family TEXT, text TEXT, key TEXT,
  target_document TEXT, target_first INTEGER, target_last INTEGER);
CREATE INDEX IF NOT EXISTS refs_place ON refs (document, page);
CREATE INDEX IF NOT EXISTS refs_key ON refs (key);
CREATE TABLE IF NOT EXISTS acronyms (document TEXT, page INTEGER, short TEXT, long TEXT, pattern TEXT);
CREATE TABLE IF NOT EXISTS aliases (
  key TEXT, document TEXT, origin TEXT, PRIMARY KEY (key, document, origin)) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS synonyms (
  grp INTEGER, term TEXT, origin TEXT, PRIMARY KEY (grp, term, origin)) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS given (
  document TEXT, first_page INTEGER, last_page INTEGER, task TEXT,
  PRIMARY KEY (document, first_page, last_page)) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS lines (
  source TEXT, report TEXT, line INTEGER, kind TEXT, text TEXT, who TEXT, purpose TEXT,
  location TEXT, PRIMARY KEY (source, report, line)) WITHOUT ROWID;
CREATE VIRTUAL TABLE IF NOT EXISTS candidates USING fts5(
  catalog UNINDEXED, address UNINDEXED, name, category, text,
  tokenize = 'porter unicode61 remove_diacritics 2');
"""
TABLES = ("documents", "pages", "sections", "refs", "acronyms", "aliases", "synonyms")
# The table of the vetting record that names the pages that the readers got.
READING = "Reading"
READING_CELLS = ("Source", "Document", "Pages", "Given to readers", "Not read")
READING_NOTE = "The program `index.py unread --write` writes this table. Do not change it by hand."
NONE = "none"
RANGE = re.compile(r"(\d+)(?:-(\d+))?")
# The lines of the reports of the readers. See prompts/reader.md and prompts/sample-reader.md.
REQ, USE = "REQ", "USE"
USE_KINDS = ("tool", "integration", "framework", "pattern", "principle")
LINE_KINDS = ("req", *USE_KINDS)
# A line of a report that can be a line "REQ" or "USE", also after the mark of a list or a quote.
REPORT_LINE = re.compile(r"[\s>*+`-]*(REQ|USE)\b")
SOURCE_ID = re.compile(r"S-\d+")
REQ_CELLS = ("Source", "Requirement", "Group", "Location")
USE_CELLS = ("Source", "Kind", "Name", "Purpose", "Location")

HEAD = re.compile(r"^- (Source|sha256|Pages): (.*)$", re.M)
PAGE = re.compile(r"^## Page \d+$", re.M)
WORD = re.compile(r"[^\W_]+")
# A line of a table of contents ends with a page number: "12", "5-3", "xii" or "A-2".
PAGE_NUMBER = re.compile(r"\d{1,4}|\d{1,2}-\d{1,3}|[ivxlc]+|[A-Z]-\d{1,3}")
CONTENTS_LINES, COLUMN_LINES, RUNNING_PAGES = 8, 4, 3

# The patterns of the sections.
CHAPTER = re.compile(
    r"(CHAPTER|Chapter|APPENDIX|Appendix)\s+(\d{1,3}|[A-Z])(?:\s*[:.\u2013\u2014-]\s*([A-Z0-9].{2,78}))?"
)
NUMBERED = re.compile(r"(\d{1,2}(?:\.\d{1,2}){0,3})\.?\s+([A-Z].{2,77})")
CAPITALS = re.compile(r"[A-Z][A-Z0-9 ,.&/:'()-]{3,78}")
WHOLE, WHOLE_TITLE = "none", "(all pages)"
# More numbered headings than this on one page are a list, not headings.
MAX_ON_PAGE = 10

# The patterns of the internal references. The group "n" is the number of the target.
NUMBER = r"(?P<n>\d{1,3}(?:[.-]\d{1,3})?|[A-Z][.-]\d{1,3})\b"
INTERNAL = (
    ("section", re.compile(r"\b[Ss]ections?\s+(?P<n>\d{1,2}(?:\.\d{1,2}){0,3})\b")),
    ("chapter", re.compile(r"\b(?P<w>[Cc]hapter|[Aa]ppendix)\s+(?P<n>\d{1,3}|[A-Z])\b")),
    ("page", re.compile(r"\b[Pp]ages?\s+(?P<n>\d{1,4})\b")),
    ("table", re.compile(r"\bTables?\s+" + NUMBER)),
    ("figure", re.compile(r"\bFig(?:ures?|\.)\s+" + NUMBER)),
)
LABELS = {"section": "Section", "page": "page", "table": "Table", "figure": "Figure"}
CAPTION = re.compile(r"(Table|TABLE|Figure|FIGURE|Fig\.?|FIG\.?)\s+" + NUMBER)
SEE = re.compile(r"\b[Ss]ee\b([^.;]{0,120})")
IN_CHAPTER = re.compile(r",?\s+(?:in|of)\s+")

# The families of the identifiers of standards and reports. Add a family as one more row.
STANDARDS = (
    (
        "ISO/IEC/IEEE",
        re.compile(
            r"\b(?:ISO|IEC|IEEE)(?:/(?:ISO|IEC|IEEE)){0,2}(?:\s+(?:Std\.?|TR|TS|PAS|Guide))?"
            r"\s+\d{3,5}(?:[-.]\d{1,3}(?!\d))*"
        ),
    ),
    ("NIST", re.compile(r"\bNIST(?:\s+(?:SP|IR)|IR)\s+\d{2,4}(?:-\d{1,3}[A-Z]?)?")),
    ("FIPS", re.compile(r"\bFIPS(?:\s+PUB)?\s+\d{2,3}(?:-\d)?")),
    ("RFC", re.compile(r"\bRFC\s?\d{3,5}\b")),
    ("EN", re.compile(r"\bEN\s+\d{3,5}(?:-\d{1,2})*")),
    ("MIL", re.compile(r"\bMIL-(?:STD|HDBK)-\d{3,5}[A-Z]?")),
    ("DO", re.compile(r"\bDO-\d{3}[A-C]?\b")),
)
# "IEEE 2014" is the year of a publication, not a standard.
YEAR = re.compile(r"IEEE (?:19|20)\d\d")
DOI = re.compile(r"(?:\bdoi:\s*|https?://(?:dx\.)?doi\.org/)(10\.\d{4,9}/[^\s\"<>\]]+)", re.I)
ADDRESS = re.compile(r"https?://[^\s<>\"\]]+")
TRAIL = ".,;:)'\u2019\u201d"
CITE = re.compile(r"\[(\d{1,3}\*?(?:\s*[,;\u2013-]\s*\d{1,3}\*?)*)(?:\s*[,;:]\s*[^\]\[]{1,40})?\]")
ENTRY = re.compile(r"\[(\d{1,3})\*?\]\s+\S")
LIST_HEAD = re.compile(r"(?:\d{1,2}(?:\.\d{1,2})*\.?\s+)?(?:REFERENCES|References|BIBLIOGRAPHY|Bibliography)")
ENTRY_LINES = 4

# The patterns of the acronyms.
SHORT = r"[A-Z][A-Za-z0-9&/-]{1,9}"
IN_PARENTHESES = re.compile(rf"\(({SHORT}?)s?\)")
SMALL_WORDS = frozenset({"a", "an", "and", "by", "for", "in", "of", "on", "the", "to", "with"})
QUERY = re.compile(r'"([^"]+)"|(\S+)')
MAX_WORDS = 6

MESSAGES = {
    "in-repository": "Nothing was done: the folder WORK must be outside each git repository.",
    "no-index": "The folder has no index. Run: index.py build {0}",
    "unreadable": "The input cannot be read: {0}",
    "built": (
        "Index: documents {documents}, pages {pages}, sections {sections}, references {references}, "
        "acronym pairs {acronyms}, groups of synonyms {groups}, updated {updated}, removed {removed}."
    ),
    "not-indexed": "{0}: not indexed: {1}",
    "no-pages": "the file has no page heading",
    "not-built": "Index: not built: {0}",
    "no-words": "the query has no word",
    "no-document": "The index has no document '{0}'.",
    "hit": "{0} | page {1} | {2} | {3} | matches: {4}",
    "partial": "No page holds all terms. These pages hold one term or more (a partial result):",
    "nothing": "No page holds a term of the query.",
    "synonyms": "Synonyms used: {0}",
    "none": "none",
    "ref": "{0} | {1} | {2} | {3}",
    "pages": "pages {0}-{1}",
    "page": "page {0}",
    "not-resolved": "not resolved",
    "in-index": "document {0}",
    "not-in-index": "not in the index",
    "entry": "list entry on page {0}",
    "no-refs": "The page has no reference.",
    "cite": "{0} | page {1} | {2} | {3} | {4}",
    "not-cited": "No place cites '{0}'.",
    "range": "{0} | {1} | number of pages: {2} | {3}",
    "front": "(before the first section)",
    "recall": "Found: {0} of {1} ({2} %). Found with a partial result only: {3}.",
    "missing": "Not found: {0} | {1} | {2}",
    "no-answers": "the file has no table with the cells Query, Document and Pages",
    "wrong-range": "the range '{0}' is not in the pages 1-{1} of the document",
    "recorded": "Recorded: {0} | {1}",
    "removed": "Removed: {0} | {1}",
    "not-recorded": "The record has no range {1} of the document '{0}'.",
    "reading": "{0} | number of pages: {1} | given to readers: {2} | not read: {3}",
    "written": "The table Reading of {0} is written. Rows: {1}. Sources with pages that no reader got: {2}.",
    "pages-left": "{0} ({1} pages)",
    "wrong-source": "the source '{0}' does not have the form S-<digits>",
    "wrong-kind": "the kind '{0}' is not one of these words: {1}",
    "no-form": "{0} | line {1} | not stored: the line does not have the form of a {2} line",
    "taken": "Stored: {0} | {1} | {2}",
    "no-lines": "The index has no such line of a report.",
}


def read_converted(text):
    r"""The head lines and the text of each page of a converted file.

    The n-th page heading starts page n. The converter writes a backslash before a line of the
    source that starts with "#", and "(no text)" for an empty page.

    >>> import pdf
    >>> head, pages = read_converted(pdf.markdown(["one\n# two", ""], "https://a.example/a.pdf", "ab12"))
    >>> head, pages
    ({'source': 'https://a.example/a.pdf', 'sha256': 'ab12', 'pages': '2'}, ['one\n# two', ''])
    >>> read_converted("no page heading")
    ({}, [])
    """
    parts = PAGE.split(text)
    head = {name.lower(): value.strip() for name, value in HEAD.findall(parts[0])}
    pages = [re.sub(r"^\\(?=\s*#)", "", part.strip(), flags=re.M) for part in parts[1:]]
    return head, ["" if page == "(no text)" else page for page in pages]


def is_contents(text):
    """True for a page of a table of contents: many lines end with a page number.

    >>> import sample
    >>> [is_contents(page) for page in sample.PAGES["S-01"][:2]]
    [True, False]
    """
    rows = [line.split("  ") for line in text.splitlines()]
    return sum(len(row) > 1 and bool(PAGE_NUMBER.fullmatch(row[-1])) for row in rows) >= CONTENTS_LINES


def flow(text):
    """The lines of a page in the sequence in which a person reads them.

    The converter puts two spaces between the parts of a line that are far from each other.
    Each part becomes one line. When half of the lines or more have two parts or more, the page
    has two columns: the first part of each line comes before the other parts.

    >>> flow("a title\\nleft one  right one\\nleft two  right two\\nleft three  right three  3")
    ['a title', 'left one', 'left two', 'left three', 'right one', 'right two', 'right three', '3']
    >>> flow("one line\\n\\nRPO  Recovery Point Objective\\nmore text\\nand more\\nthe end")
    ['one line', '', 'RPO', 'Recovery Point Objective', 'more text', 'and more', 'the end']
    """
    rows = [line.split("  ") for line in text.splitlines()]
    filled = [row for row in rows if row != [""]]
    if len(filled) >= COLUMN_LINES and 2 * sum(len(row) > 1 for row in filled) >= len(filled):
        return [row[0] for row in rows] + [part for row in rows for part in row[1:]]
    return [part for row in rows for part in row]


def joined(lines):
    """The lines of a page as one text. A word that a hyphen divides at a line end is joined, and
    an identifier that a line end divides after a slash.

    >>> joined(["A copy is not a back-", "up. See ISO/", "IEC 27040 and the well-", "Known rule."])
    'A copy is not a backup. See ISO/IEC 27040 and the well-\\nKnown rule.'
    """
    text = re.sub(r"(?<=[a-z])-\n(?=[a-z])", "", "\n".join(lines))
    return re.sub(r"(?<=[^\W_])/\n(?=[^\W_])", "/", text)


def flat(lines):
    """The lines of a page as one line. See joined().

    >>> flat(["A copy is not a back-", "up.  It is", "", "in the same room."])
    'A copy is not a backup. It is in the same room.'
    """
    return " ".join(joined(lines).split())


def running_heads(pages):
    """The lines that are the first or the last line of three or more pages. A number is "#".

    >>> running_heads(["GUIDE 1\\ntext\\n1-1", "GUIDE 2  A TITLE\\ntext\\n1-2", "GUIDE 3\\n\\n1-3", "", "a"])
    ['#-#', 'GUIDE #']
    """
    seen = collections.Counter()
    for text in pages:
        filled = [line for line in text.splitlines() if line]
        edges = {part for line in (*filled[:1], *filled[-1:]) for part in line.split("  ")}
        seen.update({re.sub(r"\d+", "#", part) for part in edges})
    return sorted(key for key, count in seen.items() if count >= RUNNING_PAGES)


def follows(last, number):
    """True if a heading number can follow the heading number before it.

    The first number of a chapter ends in 0 or 1. A later number is larger at one place by 1 or
    2 (one heading can be absent), and each place after that is 0 or 1.

    >>> [follows(None, n) for n in ((1,), (5, 1), (3,))]
    [True, True, False]
    >>> [follows((1, 2), n) for n in ((1, 3), (1, 2, 1), (2,), (1, 4), (2, 1), (1, 5), (1, 2), (1,), (2, 3))]
    [True, True, True, True, True, False, False, False, False]
    """
    if last is None:
        return number[-1] <= 1
    same = sum(
        1 for _ in itertools.takewhile(lambda pair: pair[0] == pair[1], zip(last, number, strict=False))
    )
    if same == len(number):
        return False
    step = number[same] - (last[same] if same < len(last) else 0)
    return 1 <= step <= 2 and all(n <= 1 for n in number[same + 1 :])


def chapter_follows(last, number):
    """True if a chapter number can follow the chapter number before it of the same kind.

    A number is digits or one capital letter. The first number is 0, 1 or A. A later number is
    larger by 1 or 2. A chapter can start again with the first number. The same number is a
    running head.

    >>> [chapter_follows(None, n) for n in ("1", "A", "3", "C")]
    [True, True, False, False]
    >>> [chapter_follows("2", n) for n in ("3", "4", "5", "2", "1")]
    [True, True, False, False, True]
    >>> chapter_follows("A", "B"), chapter_follows("A", "A")
    (True, False)
    """
    place, before = (int(n) if n.isdigit() else ord(n) - 64 for n in (number, last or number))
    return number != last and (place <= 1 or (last is not None and 1 <= place - before <= 2))


def is_capitals(cell):
    """True for a line in capital letters with a word of five letters or more.

    >>> [is_capitals(cell) for cell in ("FURTHER READINGS", "MATRIX OF TOPICS VS. TEXTS", "UML", "A Title")]
    [True, True, False, False]
    """
    return bool(CAPITALS.fullmatch(cell) and re.search(r"[A-Z]{5}", cell))


def find_sections(pages, lines):
    """The sections of a document, from the three patterns. pages: the text of each page.

    Each section is a dictionary with seq, title, number, first, last, level, pattern and chapter
    (the seq of its chapter, or None).

    >>> import sample
    >>> pages = sample.PAGES["S-01"]
    >>> for s in find_sections(pages, [flow(page) for page in pages]):
    ...     span = f"{s['first']}-{s['last']}"
    ...     print(s["seq"], s["pattern"], s["level"], s["number"] or "-", span, s["title"])
    1 chapter 1 1 2-3 Copies of the Data
    2 capitals 2 - 2-2 ACRONYMS
    3 capitals 2 - 2-2 INTRODUCTION
    4 numbered 2 1 2-2 Copies of the Data
    5 numbered 3 1.1 2-2 Kinds of Copies
    6 numbered 2 2 3-3 Places
    7 capitals 2 - 3-3 REFERENCES
    8 chapter 1 2 4-5 The Restore Drill
    9 numbered 2 1 4-4 The Restore Drill
    10 numbered 2 2 5-5 Records of a Drill
    11 chapter 1 A 6-6 Forms

    A chapter line without a title line is not a heading. A chapter line with the number of the
    open chapter is a running head. A title can be on the chapter line. A title has a second
    line when a heading in capital letters follows that line. A citation at the end of a title
    is not a part of the title. Without a chapter, the level of a heading is the number of the
    parts of its number.

    >>> def found(*pages):
    ...     sections = find_sections(pages, [flow(page) for page in pages])
    ...     return [(s["title"], s["number"], s["level"]) for s in sections]
    >>> found("Chapter 1: Tests\\n1.1 Unit Tests [2, c4]", "Chapter 1: Tests\\n1.2 System Tests\\nChapter 2")
    [('Tests', '1', 1), ('Unit Tests', '1.1', 3), ('System Tests', '1.2', 3)]
    >>> found("CHAPTER 01\\nThe Tests\\nof a System\\nINTRODUCTION", "CHAPTER 02\\nTwo\\nA text.\\nSUMMARY")
    [('The Tests of a System', '1', 1), ('INTRODUCTION', '', 2), ('Two', '2', 1), ('SUMMARY', '', 2)]

    The first chapter of a kind has the number 0, 1 or A. A chapter line with a different number
    is not a heading: it can be a line of a list that names a chapter.

    >>> found("Appendix C: Lists\\ntext")
    [('(all pages)', '', 1)]
    >>> found("1 First\\n1.1 Second\\nSUMMARY OF IT")
    [('First', '1', 1), ('Second', '1.1', 2), ('SUMMARY OF IT', '', 1)]

    The title of a chapter can be the first line of the page, in capital letters, above the
    chapter line.

    >>> found("TABLES OF THE GUIDE\\nAppendix A\\nINTRODUCTION\\ntext")
    [('TABLES OF THE GUIDE', 'A', 1), ('INTRODUCTION', '', 2)]

    A caption in capital letters is not a heading. On a page with a list of acronyms, a short
    form is not a heading. A page with more than ten numbered headings holds a list: its
    numbered lines are not headings.

    >>> found("ACRONYMS\\nSWEBOK  Software Engineering Body of Knowledge\\nTABLE 2. THE KINDS\\nINTRODUCTION")
    [('ACRONYMS', '', 1), ('INTRODUCTION', '', 1)]
    >>> found("OVERVIEW\\n" + "\\n".join(f"{n} Subject {n}" for n in range(1, 12)))
    [('OVERVIEW', '', 1)]

    A document without a heading gets one section for all its pages.

    >>> find_sections(["text", "more"], [["text"], ["more"]]) == [{"seq": 1, "title": "(all pages)",
    ...     "number": "", "first": 1, "last": 2, "depth": 1, "level": 1, "pattern": "none", "chapter": None}]
    True
    """
    heads = set(running_heads(pages))
    found, chapter, open_chapters, last = [], None, {}, None

    def is_head(cell):
        return re.sub(r"\d+", "#", cell) in heads

    def add(page, title, number, depth, pattern):
        title = re.sub(r"\s*\[[^\]\[]*\]$", "", re.sub(r"[\x00-\x1f]", "", title).strip())
        section = {"seq": len(found) + 1, "title": title, "number": number, "first": page}
        found.append({**section, "depth": depth, "pattern": pattern, "chapter": chapter})

    for page, cells in enumerate(lines, 1):
        if is_contents(pages[page - 1]):
            continue
        filled = [cell for cell in cells if cell]
        skip, listed = set(), False
        for i, cell in enumerate(filled):
            listed = listed or (len(cell) <= 40 and "acronym" in cell.casefold())
            if i in skip:
                continue
            if m := CHAPTER.fullmatch(cell):
                kind, number = m.group(1).casefold(), m.group(2).lstrip("0") or "0"
                above = i == 1 and not m.group(3) and is_capitals(filled[0]) and not is_head(filled[0])
                below = filled[i + 1 : i + 4]
                two = len(below) == 3 and is_capitals(below[2]) and not is_capitals(below[1])
                two = two and len(below[1]) <= 40 and not below[1].endswith(".")
                title = m.group(3) or (filled[0] if above else " ".join(below[: 2 if two else 1]))
                if title and len(title) <= 120 and chapter_follows(open_chapters.get(kind), number):
                    if above and found and (found[-1]["first"], found[-1]["title"]) == (page, title):
                        found.pop()
                    if not (above or m.group(3)):
                        skip = {i + 1, i + 2} if two else {i + 1}
                    open_chapters[kind], chapter, last = number, len(found) + 1, None
                    add(page, title, number, 0, "chapter")
            elif (m := NUMBERED.fullmatch(cell)) and not is_head(cell):
                number = tuple(int(part) for part in m.group(1).split("."))
                if follows(last, number) and not m.group(2).endswith((".", ",", ";", ":")):
                    last = number
                    add(page, m.group(2), m.group(1), len(number), "numbered")
            elif is_capitals(cell) and not is_head(cell) and not CAPTION.match(cell):
                if not (listed and re.fullmatch(SHORT, cell) and "ACRONYM" not in cell):
                    add(page, cell, "", 1, "capitals")
    on_page = collections.Counter(section["first"] for section in found if section["pattern"] == "numbered")
    lists = {page for page, count in on_page.items() if count > MAX_ON_PAGE}
    found = [
        section for section in found if section["pattern"] != "numbered" or section["first"] not in lists
    ]
    if not found:
        add(1, WHOLE_TITLE, "", 1, WHOLE)
    seqs = {section["seq"]: n for n, section in enumerate(found, 1)}
    base = 1 if any(section["pattern"] == "chapter" for section in found) else 0
    for i, section in enumerate(found):
        section["seq"], section["chapter"] = i + 1, seqs.get(section["chapter"])
        section["level"] = max(1, section["depth"] + base)
        later = (s["first"] for s in found[i + 1 :] if s["depth"] <= section["depth"])
        section["last"] = max(section["first"], next(later, len(pages) + 1) - 1)
    return found


def key_of(text):
    """The form in which two names of one thing are equal: an identifier, an address or a name.

    Capital letters, the word "Std", the year of a standard, "http" or "https" and "www" make
    no difference.

    >>> [key_of(t) for t in ("IEEE Std 1012-2016", "ISO/IEC  27040:2015", "IEEE 1012", "Guide to Backups")]
    ['ieee 1012', 'iso/iec 27040', 'ieee 1012', 'guide to backups']
    >>> [key_of(t) for t in ("https://www.A.example/x/", "http://a.example/x", "DOI: 10.1000/182", "S-01")]
    ['a.example/x', 'a.example/x', 'doi:10.1000/182', 's-01']
    >>> key_of("https://doi.org/10.1000/182.")
    'doi:10.1000/182'
    """
    text = " ".join(text.split()).casefold()
    if m := DOI.fullmatch(text):
        return "doi:" + m.group(1).rstrip(TRAIL)
    if text.startswith(("http://", "https://")):
        return re.sub(r"^https?://(?:www\.)?", "", text).rstrip("/" + TRAIL)
    return re.sub(r"(?<=\d)[:-](?:19|20)\d\d$", "", re.sub(r"\bstd\.?\s+", "", text))


def externals(text):
    """The identifiers in a text that point outside the document: (family, text, key), sorted.

    >>> for found in externals("See ISO/IEC/IEEE 12207:2017, IEEE Std 1012-2016, NIST SP 800-218 and "
    ...                        "RFC 2119 (https://a.example/rfc), doi:10.1000/182. Proc. IEEE 2014."):
    ...     print(found)
    ('ISO/IEC/IEEE', 'IEEE Std 1012', 'ieee 1012')
    ('ISO/IEC/IEEE', 'ISO/IEC/IEEE 12207', 'iso/iec/ieee 12207')
    ('NIST', 'NIST SP 800-218', 'nist sp 800-218')
    ('RFC', 'RFC 2119', 'rfc 2119')
    ('address', 'https://a.example/rfc', 'a.example/rfc')
    ('doi', 'doi:10.1000/182', 'doi:10.1000/182')
    >>> externals("ISO 9001, IEC 61508-3, FIPS 140-2, EN 50128, MIL-STD-498, DO-178C, https://doi.org/10.1000/9")
    [('DO', 'DO-178C', 'do-178c'), ('EN', 'EN 50128', 'en 50128'), ('FIPS', 'FIPS 140-2', 'fips 140-2'),
     ('ISO/IEC/IEEE', 'IEC 61508-3', 'iec 61508-3'), ('ISO/IEC/IEEE', 'ISO 9001', 'iso 9001'),
     ('MIL', 'MIL-STD-498', 'mil-std-498'), ('doi', 'doi:10.1000/9', 'doi:10.1000/9')]
    """
    found = {("doi", "doi:" + m.group(1).rstrip(TRAIL)) for m in DOI.finditer(text)}
    text = DOI.sub(" ", text)
    found |= {("address", m.group(0).rstrip(TRAIL)) for m in ADDRESS.finditer(text)}
    text = ADDRESS.sub(" ", text)
    for family, pattern in STANDARDS:
        found |= {(family, " ".join(m.group(0).split())) for m in pattern.finditer(text)}
        text = pattern.sub(" ", text)
    return sorted((family, shown, key_of(shown)) for family, shown in found if not YEAR.fullmatch(shown))


def cited_numbers(inner):
    """The numbers of a citation: "1*, 3-5" gives 1, 3, 4 and 5.

    >>> cited_numbers("1*, 3-5"), cited_numbers("12"), cited_numbers("7\u20138; 2")
    ([1, 3, 4, 5], [12], [2, 7, 8])
    """
    numbers = set()
    for token in re.split(r"[,;]", inner.replace("*", "").replace("\u2013", "-")):
        first, _, last = token.partition("-")
        numbers.update(range(int(first), min(int(last or first), int(first) + 30) + 1))
    return sorted(numbers)


def find_references(pages, lines, sections):
    """The references of a document: (page, kind, family, text, key, first target page, last), sorted.

    >>> import sample
    >>> pages = sample.PAGES["S-01"]
    >>> lines = [flow(page) for page in pages]
    >>> for row in find_references(pages, lines, find_sections(pages, lines)):
    ...     print(*("-" if cell is None else cell for cell in row))
    2 external ISO/IEC/IEEE ISO/IEC 27040 iso/iec 27040 - -
    2 external RFC RFC 2119 rfc 2119 - -
    2 external citation [1] doi:10.1000/182 3 3
    2 external citation [2] iso/iec 27040 3 3
    2 internal figure Figure 1 figure 1 2 2
    2 internal name The Restore Drill the restore drill 4 5
    2 internal page page 4 page 4 4 4
    2 internal section Section 1 section 1 4 4
    2 internal section Section 1.1 section 1.1 2 2
    2 internal table Table 2 table 2 4 4
    3 external ISO/IEC/IEEE ISO/IEC 27040 iso/iec 27040 - -
    3 external NIST NIST SP 800-34 nist sp 800-34 - -
    3 external address https://rules.example/backups rules.example/backups - -
    3 external doi doi:10.1000/182 doi:10.1000/182 - -
    3 internal name The Restore Drill the restore drill 4 5
    3 internal section Section 9.9 section 9.9 - -
    4 internal chapter Appendix A appendix a 6 6
    4 internal chapter Chapter 1 chapter 1 2 3
    4 internal table Table 2 table 2 4 4
    6 external ISO/IEC/IEEE ISO 9001 iso 9001 - -
    6 external RFC RFC 2119 rfc 2119 - -

    A citation without a line in a list of references is not recorded. An entry of a list that
    names no identifier gives a citation without a key. A page number that the document does not
    have is not resolved. A section number that two chapters have, outside of them, is not resolved.

    >>> pages = ["See Section 1 and page 9 [1] [3].", "Chapter 1\\nOne\\n1 First", "Chapter 2\\nTwo\\n1 Last",
    ...          "References\\n[1] A. Writer, A book.\\n\\n[2] A second book."]
    >>> lines = [flow(page) for page in pages]
    >>> for row in find_references(pages, lines, find_sections(pages, lines)):
    ...     print(*("-" if cell is None else cell for cell in row))
    1 internal page page 9 page 9 - -
    1 internal section Section 1 section 1 - -
    >>> lines = [["Text [1] and Fig. 2", "", "References", "[1] A. Writer, A book."], ["Figure 2 is here"]]
    >>> [row[:5] for row in find_references(["", ""], lines, find_sections(["", ""], lines))]
    [(1, 'external', 'citation', '[1]', None), (1, 'internal', 'figure', 'Figure 2', 'figure 2')]
    """
    texts = [flat(cells) for cells in lines]
    chapters = [s for s in sections if s["pattern"] == "chapter"]
    named = collections.defaultdict(list)
    for section in sections:
        if section["level"] == 1 and section["pattern"] != WHOLE and len(section["title"]) >= 6:
            named[section["title"].casefold()].append(section)
    # A front part can name a chapter before the chapter starts: the last heading is the target.
    tops = [same[-1] for _, same in sorted(named.items(), key=lambda item: (-len(item[0]), item[0]))]

    def chapter_at(page):
        return max((s["seq"] for s in chapters if s["first"] <= page), default=None)

    captions, entries, entry_cells, zone = {}, {}, set(), ()
    for page, cells in enumerate(lines, 1):
        here = chapter_at(page)
        for i, cell in enumerate(cells):
            if LIST_HEAD.fullmatch(cell):
                zone = (here,)
            if m := CAPTION.match(cell):
                family = "table" if m.group(1).casefold() == "table" else "figure"
                captions.setdefault((family, m.group("n")), []).append(page)
            if zone == (here,) and (m := ENTRY.match(cell)):
                more = itertools.takewhile(lambda c: c and not ENTRY.match(c), cells[i + 1 : i + ENTRY_LINES])
                entries.setdefault((here, int(m.group(1))), (page, externals(" ".join([cell, *more]))))
                entry_cells.add((page, i))

    def span(section):
        return (section["first"], section["last"]) if section else (None, None)

    def numbered(number, tail, here):
        """The section with this number: in the chapter that the text names, or in this chapter."""
        prefix = IN_CHAPTER.match(tail)
        rest = tail[prefix.end() :].casefold() if prefix else ""
        titles = ((s["seq"], s["title"].casefold()) for s in tops if s["pattern"] == "chapter")
        where = next((seq for seq, title in titles if rest.startswith((title, "the " + title))), here)
        found = [s for s in sections if s["pattern"] == "numbered" and s["number"] == number]
        return next((s for s in found if s["chapter"] == where), found[0] if len(found) == 1 else None)

    rows = set()
    for page, text in enumerate(texts, 1):
        here = chapter_at(page)
        rows |= {(page, "external", family, shown, key, None, None) for family, shown, key in externals(text)}
        if is_contents(pages[page - 1]):
            continue
        for family, pattern in INTERNAL:
            matches = list(pattern.finditer(text))
            for m in matches:
                number, first, last = m.group("n"), None, None
                label = LABELS.get(family) or m.group("w").capitalize()
                if family == "section":
                    first, last = span(numbered(number, text[m.end() : m.end() + 100], here))
                elif family == "chapter":
                    number = str(int(number)) if number.isdigit() else number
                    target = next((s for s in reversed(chapters) if s["number"] == number), None)
                    if target and target["seq"] == here:
                        continue  # the heading of the chapter, or its running head
                    first, last = span(target)
                elif family == "page":
                    first = last = int(number) if 1 <= int(number) <= len(lines) else None
                else:
                    places = captions.get((family, number), [])
                    if places.count(page) >= sum(1 for other in matches if other.group("n") == number):
                        continue  # the caption itself
                    first = last = next(iter([p for p in places if chapter_at(p) == here] or places), None)
                rows.add(
                    (
                        page,
                        "internal",
                        family,
                        f"{label} {number}",
                        f"{label} {number}".casefold(),
                        first,
                        last,
                    )
                )
        for m in SEE.finditer(text):
            for section in tops:
                if re.search(
                    rf"(?<!\w){re.escape(section['title'].casefold())}(?!\w)", m.group(1).casefold()
                ):
                    key = section["title"].casefold()
                    rows.add((page, "internal", "name", section["title"], key, *span(section)))
        for i, cell in enumerate(lines[page - 1]):
            for m in CITE.finditer(cell):
                found = [] if (page, i) in entry_cells and m.start() == 0 else cited_numbers(m.group(1))
                for number, place in ((n, entries[here, n]) for n in found if (here, n) in entries):
                    keys = [key for _, _, key in place[1]] or [None]
                    rows |= {
                        (page, "external", "citation", f"[{number}]", key, place[0], place[0]) for key in keys
                    }
    return sorted(rows, key=lambda row: (row[0], repr(row[1:])))


def long_form(short, text, whole=False):
    """The long form of an acronym at the end of a text, or None.

    The rule is strict: each letter or digit of the short form is the first letter of one word
    of the long form, in the same sequence, and the long form has no other word. A small word
    (a, an, and, by, for, in, of, on, the, to, with) in the long form is ignored. The short form
    has two capital letters or more. With whole, the long form is the full text.

    >>> long_form("SRS", "The software requirements specification ")
    'software requirements specification'
    >>> long_form("V&V", "do the Verification and Validation"), long_form("OO", "an Object-Oriented")
    ('Verification and Validation', 'Object-Oriented')
    >>> long_form("SRS", "a software specification"), long_form("Ab", "a big"), long_form("QA", "assurance")
    (None, None, None)
    >>> long_form("RPO", "Recovery Point Objective", whole=True)
    'Recovery Point Objective'
    >>> long_form("RPO", "A Recovery Point Objective", whole=True)
    >>> long_form("DoD", "Department of Defense"), long_form("AB", "")
    (None, None)
    """
    letters = [c for c in short.casefold() if c.isalnum()]
    words = list(WORD.finditer(text))
    need, start = len(letters), None
    if sum(c.isupper() for c in short) < 2:
        return None
    for word in reversed(words):
        if need == 0:
            break
        if word.group().casefold() in SMALL_WORDS and need < len(letters):
            continue
        if word.group()[0].casefold() != letters[need - 1]:
            return None
        need, start = need - 1, word.start()
    if need or (whole and words[0].start() != start):
        return None
    return " ".join(text[start:].split())


def find_acronyms(pages):
    """The acronyms of a document: (page, short form, long form, pattern), sorted.

    The pattern "parentheses" is a long form with its short form in parentheses after it. The
    pattern "list" is a line with a short form, spaces and its long form, on a page below a
    heading that holds the word "acronym".

    >>> import sample
    >>> for row in find_acronyms(sample.PAGES["S-01"]):
    ...     print(*row)
    2 FB full backup parentheses
    2 RPO Recovery Point Objective list
    2 RTO Recovery Time Objective list
    4 RD restore drill parentheses
    5 SRS software requirements specification parentheses
    >>> pages = ["Very small entities (VSEs) and a virtual machine (VM).", "A VM  Virtual Machine"]
    >>> find_acronyms([*pages, "Acronyms\\nsee below  Virtual Machine\\nVM  Virtual Machine"])
    [(1, 'VM', 'virtual machine', 'parentheses'), (1, 'VSE', 'Very small entities', 'parentheses')]
    """
    found = {}
    for page, text in enumerate(pages, 1):
        pairs, listed = [], False
        for line in text.splitlines():
            cells = line.split("  ")
            listed = listed or any(len(cell) <= 40 and "acronym" in cell.casefold() for cell in cells)
            for short, long in itertools.pairwise(cells if listed else ()):
                if re.fullmatch(SHORT, short):
                    pairs.append((short, long_form(short, long, whole=True), "list"))
        line = flat(flow(text))
        for m in IN_PARENTHESES.finditer(line):
            pairs.append(
                (m.group(1), long_form(m.group(1), line[max(0, m.start() - 150) : m.start()]), "parentheses")
            )
        for short, long, pattern in pairs:
            if long:
                found.setdefault((short.casefold(), long.casefold()), (page, short, long, pattern))
    return sorted(found.values())


def analyse(text):
    """All that the index holds of one converted file.

    >>> import pdf, sample
    >>> data = analyse(pdf.markdown(sample.PAGES["S-02"], "https://journal.example/restore", "ab12"))
    >>> data["source"], data["digest"], len(data["texts"]), data["texts"][1]
    ('https://journal.example/restore', 'ab12', 2, '')
    >>> [(s["title"], s["first"], s["last"], s["pattern"]) for s in data["sections"]], data["acronyms"]
    ([('(all pages)', 1, 2, 'none')], [])
    >>> [row[3] for row in data["references"]]
    ['IEEE Std 1012', 'ISO/IEC 27040', 'https://standards.example/backups']
    >>> analyse("no page heading")["texts"]
    []
    """
    head, pages = read_converted(text)
    lines = [flow(page) for page in pages]
    sections = find_sections(pages, lines)
    return {
        "source": head.get("source", ""),
        "digest": head.get("sha256", ""),
        "texts": [joined(cells) for cells in lines],
        "sections": sections,
        "references": find_references(pages, lines, sections),
        "acronyms": find_acronyms(pages),
    }


def names_of(cell):
    """The names in the cell of a document: the cell, its part before a last part in parentheses,
    that part, and each identifier of a standard in it.

    >>> names_of("Guide to the Body of Knowledge (BOK Guide)")
    ['BOK Guide', 'Guide to the Body of Knowledge', 'Guide to the Body of Knowledge (BOK Guide)']
    >>> names_of("ISO/IEC 27040:2015 Storage security"), names_of(" ")
    (['ISO/IEC 27040', 'ISO/IEC 27040:2015 Storage security'], [])
    """
    cell = " ".join(cell.split())
    parts = re.fullmatch(r"(.+?)\s*\(([^()]+)\)", cell)
    names = {cell, *(parts.groups() if parts else ())}
    names |= {shown for family, shown, _ in externals(cell) if family not in ("address", "doi")}
    return sorted(name for name in names if name)


def alias_rows(documents, seeds=(), sources=()):
    """The other names of the documents of the index: (the rows of the table, the names to find).

    documents: {id: address of the source}. seeds: the rows of the manifest. sources: the rows
    of section 2 of an aspect specification; the source id is the id of the document. A row for
    a document that is not in the index gives nothing.

    >>> seeds = [{"id": "guide", "document": "A Guide (AG)", "address": "https://a.example/form"}]
    >>> sources = [{"id": "S-02", "source": "A study", "url": "https://j.example/s"}, {"id": "S-09"}]
    >>> seeds += [{"id": "b"}]
    >>> rows, names = alias_rows({"guide": "https://a.example/a.pdf", "S-02": ""}, seeds, sources)
    >>> for row in rows:
    ...     print(*row)
    a guide guide manifest
    a guide (ag) guide manifest
    a study S-02 specification
    a.example/a.pdf guide head
    a.example/form guide manifest
    ag guide manifest
    guide guide head
    j.example/s S-02 specification
    s-02 S-02 head
    >>> names
    [('A Guide', 'guide'), ('A Guide (AG)', 'guide'), ('A study', 'S-02'), ('AG', 'guide')]
    """
    rows, names = set(), set()
    for ident, source in documents.items():
        rows |= {(key_of(text), ident, "head") for text in (ident, source) if text}
    given = [("manifest", s["id"], s.get("address", ""), s.get("document", "")) for s in seeds]
    given += [
        ("specification", r.get("id", ""), r.get("url", "").strip("<>`"), r.get("source", ""))
        for r in sources
    ]
    for origin, ident, address, cell in given:
        if ident in documents:
            found = names_of(cell)
            names |= {(name, ident) for name in found}
            rows |= {(key_of(text), ident, origin) for text in (address, *found) if text}
    return sorted(rows), sorted(names)


def read_synonyms(path):
    r"""The groups of a file of synonyms: one group in each line, the terms separated by " = ".

    A line that starts with "#" is a comment.

    >>> import tempfile
    >>> path = pathlib.Path(tempfile.mkdtemp(prefix="sota-index-")) / "synonyms.txt"
    >>> _ = path.write_text("# a comment\n\nclient = customer = Acquirer\nalone\n", encoding="utf-8")
    >>> read_synonyms(path), read_synonyms(SYNONYMS)
    ([['client', 'customer', 'Acquirer'], ['alone']], [])
    """
    lines = (line.strip() for line in aspect.read_text(path).splitlines())
    return [
        [term.strip() for term in line.split(" = ")] for line in lines if line and not line.startswith("#")
    ]


def glossary_groups(rows):
    """The groups of the glossary of an aspect specification, section 8.

    The names of one term are in the cell "Term", separated by ";", and in a cell "Other names"
    if the table has one.

    >>> glossary_groups([{"term": "backup; safety copy", "other names": "archive"}, {"term": "drill"}])
    [['backup', 'safety copy', 'archive'], ['drill']]
    """
    cells = (f"{row.get('term', '')};{row.get('other names', '')}" for row in rows)
    return [[name.strip() for name in cell.split(";") if name.strip()] for cell in cells]


def synonym_rows(groups):
    """The rows of the table of the synonyms: (group, term, origin), sorted.

    groups: pairs of an origin and the terms of one group. A group is symmetric and transitive:
    two groups that share a term are one group. The terms are compared without case. A group
    with one term gives no row. The groups are numbered in the sequence of their first terms.

    >>> groups = [("file", ["client", "Customer"]), ("acronym", ["SRS", "software requirements text"])]
    >>> groups += [("glossary", ["customer", "acquirer"]), ("file", ["alone"]), ("file", ["a", "A"])]
    >>> for row in synonym_rows(groups):
    ...     print(*row)
    1 acquirer glossary
    1 client file
    1 customer file
    1 customer glossary
    2 software requirements text acronym
    2 srs acronym
    """
    parent, origins = {}, collections.defaultdict(set)

    def root(term):
        while parent.setdefault(term, term) != term:
            term = parent[term]
        return term

    for origin, terms in groups:
        terms = [" ".join(term.split()).casefold() for term in terms]
        for term in terms:
            origins[term].add(origin)
            parent[max(root(term), root(terms[0]))] = min(root(term), root(terms[0]))
    members = collections.defaultdict(list)
    for term in sorted(parent):
        members[root(term)].append(term)
    kept = [terms for _, terms in sorted(members.items()) if len(terms) > 1]
    return [
        (n, term, origin)
        for n, terms in enumerate(kept, 1)
        for term in terms
        for origin in sorted(origins[term])
    ]


def connect(work):
    """The database of a work folder, with its tables."""
    db = sqlite3.connect(pathlib.Path(work) / DATABASE)
    db.executescript(SCHEMA)
    return db


def dump(work):
    """The content of each table, sorted. Two builds from the same files give the same content."""
    with contextlib.closing(connect(work)) as db:
        return {
            table: sorted(db.execute(f"SELECT * FROM {table}"), key=repr)
            for table in (*TABLES, "given", "lines")
        }


def build(work, synonyms=(), spec=None, seeds=()):
    r"""Build or update the index of a work folder. Returns the numbers and the names of the result.

    >>> import sample
    >>> work = sample.converted()
    >>> result = build(work)
    >>> {k: v for k, v in result.items() if k not in ("updated", "removed", "problems")}
    {'documents': 2, 'pages': 8, 'sections': 12, 'references': 24, 'acronyms': 5, 'groups': 5}
    >>> result["updated"], result["removed"], result["problems"]
    (['S-01', 'S-02'], [], [])
    >>> first = dump(work)
    >>> first["documents"][1][:2], first["documents"][1][3], len(first["documents"][1][4])
    (('S-02', 'https://journal.example/restore'), 2, 64)
    >>> first["synonyms"][:2], first["aliases"]
    ([(1, 'fb', 'acronym'), (1, 'full backup', 'acronym')],
     [('journal.example/restore', 'S-02', 'head'), ('s-01', 'S-01', 'head'), ('s-02', 'S-02', 'head'),
      ('standards.example/backups', 'S-01', 'head')])

    An address or an identifier that is a name of a document of the index gets that document as
    its target.

    >>> [row[4] for row in first["refs"] if row[6] == "S-01"]
    ['https://standards.example/backups']

    A second build reads only a file that changed. It removes a document whose file is gone. The
    same files give the same content of the database.

    >>> result = build(work)
    >>> result["updated"], result["removed"], dump(work) == first
    ([], [], True)
    >>> path = work / "converted" / "S-02.md"
    >>> text = path.read_text(encoding="utf-8")
    >>> _ = path.write_text(text.replace("restores.", "restores. See RFC 2119."), encoding="utf-8")
    >>> build(work)["updated"], len(dump(work)["refs"]) - len(first["refs"])
    (['S-02'], 1)
    >>> _ = path.write_text(text, encoding="utf-8")
    >>> build(work)["updated"], dump(work) == first
    (['S-02'], True)
    >>> path.rename(work / "S-02.md").name, build(work)["removed"], len(dump(work)["pages"])
    ('S-02.md', ['S-02'], 6)
    >>> (work / "S-02.md").rename(path).name, build(work)["updated"], dump(work) == first
    ('S-02.md', ['S-02'], True)

    A database with a different version of the patterns is made again.

    >>> with contextlib.closing(connect(work)) as db, db:
    ...     _ = db.execute("UPDATE meta SET value = '0'")
    >>> build(work)["updated"], dump(work) == first
    (['S-01', 'S-02'], True)

    The synonyms come from the acronyms of the documents, from files and from the glossary of
    an aspect specification. The names of the documents come from the head lines, from the rows
    of the manifest and from section 2 of the specification. A place in a different document
    that names a document of the index gets a reference of the family "document".

    >>> extra = work / "more.txt"
    >>> _ = extra.write_text("backup = safety copy\n", encoding="utf-8")
    >>> spec = sample.folder(("spec.md", "| backup |", "| backup; reserve copy |"))
    >>> seeds = [{"id": "S-02", "document": "A study of restore failures (the study)", "address": "https://j.example"}]
    >>> build(work, [extra], spec, seeds)["groups"]
    6
    >>> full = dump(work)
    >>> [row[1:] for row in full["synonyms"] if row[0] == 1]
    [('backup', 'file'), ('backup', 'glossary'), ('reserve copy', 'glossary'), ('safety copy', 'file')]
    >>> sorted({row[0] for row in full["aliases"] if row[2] != "head"})
    ['a study of restore failures', 'a study of restore failures (the study)', 'guide to backups',
     'j.example', 'journal.example/restore', 'standards.example/backups', 'the study']
    >>> [row[:2] + row[3:7] for row in full["refs"] if row[3] == "document"]
    [('S-02', 1, 'document', 'Guide to backups', 'guide to backups', 'S-01')]

    The file synonyms.txt of the work folder is read without an option.

    >>> _ = (work / WORK_SYNONYMS).write_text("drill = exercise\n", encoding="utf-8")
    >>> build(work)["groups"], [row[1:] for row in dump(work)["synonyms"] if row[1] == "exercise"]
    (6, [('exercise', 'file')])
    >>> (work / WORK_SYNONYMS).unlink()

    The record of the ranges that were given to the readers stays when the converted file of
    its document did not change, also after a change of the version of the patterns. A file
    that changed has new pages: its record is removed.

    >>> with contextlib.closing(connect(work)) as db, db:
    ...     record_given(db, "S-01", 1, 3)
    ...     record_given(db, "S-02", 1, 2)
    ...     _ = db.execute("UPDATE meta SET value = '0'")
    >>> build(work)["updated"], dump(work)["given"]
    (['S-01', 'S-02'], [('S-01', 1, 3, ''), ('S-02', 1, 2, '')])
    >>> _ = path.write_text(text.replace("restores.", "restores. See RFC 2119."), encoding="utf-8")
    >>> build(work)["updated"], dump(work)["given"]
    (['S-02'], [('S-01', 1, 3, '')])
    >>> _ = path.write_text(text, encoding="utf-8")
    >>> with contextlib.closing(connect(work)) as db, db:
    ...     _ = db.execute("DELETE FROM given")
    >>> _ = build(work)

    A file that cannot be read, or that has no page heading, is not indexed. The program records
    it and continues. A work folder without converted files gives an empty index.

    >>> _ = (work / "converted" / "bad.md").write_bytes(b"\xff")
    >>> _ = (work / "converted" / "empty.md").write_text("no page heading", encoding="utf-8")
    >>> result = build(work)
    >>> result["documents"], [problem.split(": ")[:2] for problem in result["problems"]]
    (2, [['bad', 'not indexed'], ['empty', 'not indexed']])
    >>> build(sample.converted({}))["documents"]
    0
    """
    work = pathlib.Path(work)
    files = {path.stem: path for path in sorted((work / "converted").glob("*.md"))}
    given = [path for path in (SYNONYMS, work / WORK_SYNONYMS) if path.is_file()] + list(synonyms)
    groups = [("file", terms) for path in given for terms in read_synonyms(path)]
    data = aspect.load(spec) if spec is not None else {"sources": [], "glossary": []}
    groups += [("glossary", terms) for terms in glossary_groups(data["glossary"])]
    updated, problems = [], []
    with contextlib.closing(connect(work)) as db, db:
        before = dict(db.execute("SELECT id, converted FROM documents"))
        if db.execute("SELECT value FROM meta WHERE key = 'version'").fetchone() != (VERSION,):
            for table in TABLES:
                db.execute(f"DELETE FROM {table}")
            db.execute("INSERT OR REPLACE INTO meta VALUES ('version', ?)", (VERSION,))
        known = dict(db.execute("SELECT id, converted FROM documents"))

        def forget(ident):
            for table in ("pages", "sections", "refs", "acronyms"):
                db.execute(f"DELETE FROM {table} WHERE document = ?", (ident,))
            db.execute("DELETE FROM documents WHERE id = ?", (ident,))

        for ident, path in files.items():
            reason = MESSAGES["no-pages"]
            try:
                text = aspect.read_text(path)
            except aspect.Unreadable as e:
                text, reason = "", str(e).rsplit(": ", 1)[-1]
            converted = hashlib.sha256(text.encode("utf-8")).hexdigest()
            if known.get(ident) == converted:
                continue
            forget(ident)
            if before.get(ident) != converted:
                db.execute("DELETE FROM given WHERE document = ?", (ident,))
            found = analyse(text)
            if not found["texts"]:
                problems.append(MESSAGES["not-indexed"].format(ident, reason))
                continue
            updated.append(ident)
            db.execute(
                "INSERT INTO documents VALUES (?, ?, ?, ?, ?)",
                (ident, found["source"], found["digest"], len(found["texts"]), converted),
            )
            db.executemany(
                "INSERT INTO pages VALUES (?, ?, ?)", [(ident, n, t) for n, t in enumerate(found["texts"], 1)]
            )
            cells = ("seq", "title", "number", "first", "last", "level", "pattern")
            db.executemany(
                "INSERT INTO sections VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                [(ident, *(section[cell] for cell in cells)) for section in found["sections"]],
            )
            rows = [(ident, *row[:5], None, *row[5:]) for row in found["references"]]
            db.executemany("INSERT INTO refs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", rows)
            db.executemany(
                "INSERT INTO acronyms VALUES (?, ?, ?, ?, ?)", [(ident, *row) for row in found["acronyms"]]
            )
        removed = sorted(set(known) - set(files))
        for ident in removed:
            forget(ident)
        db.execute("DELETE FROM given WHERE document NOT IN (SELECT id FROM documents)")

        # The names of the documents and the synonyms depend on all documents: write them again.
        documents = dict(db.execute("SELECT id, source FROM documents"))
        aliases, names = alias_rows(documents, seeds, data["sources"])
        db.execute("DELETE FROM aliases")
        db.executemany("INSERT INTO aliases VALUES (?, ?, ?)", aliases)
        db.execute("DELETE FROM refs WHERE family = 'document'")
        for name, ident in names:
            query = "SELECT document, CAST(page AS INTEGER) FROM pages WHERE pages MATCH ? AND document != ?"
            for document, page in db.execute(query, (quoted(name), ident)).fetchall():
                row = (document, page, "external", "document", name, key_of(name), ident, None, None)
                db.execute("INSERT INTO refs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", row)
        db.execute(
            "UPDATE refs SET target_document ="
            " (SELECT min(document) FROM aliases WHERE aliases.key = refs.key)"
            " WHERE kind = 'external' AND family != 'document'"
        )
        groups += [("acronym", pair) for pair in db.execute("SELECT short, long FROM acronyms ORDER BY 1, 2")]
        db.execute("DELETE FROM synonyms")
        db.executemany("INSERT INTO synonyms VALUES (?, ?, ?)", synonym_rows(groups))
        counts = {
            name: db.execute(f"SELECT count(*) FROM {table}").fetchone()[0]
            for name, table in (
                ("pages", "pages"),
                ("sections", "sections"),
                ("references", "refs"),
                ("acronyms", "acronyms"),
            )
        }
        counts["groups"] = db.execute("SELECT count(DISTINCT grp) FROM synonyms").fetchone()[0]
    return {
        "documents": len(documents),
        **counts,
        "updated": updated,
        "removed": removed,
        "problems": problems,
    }


def build_lines(work, synonyms=(), spec=None, seeds=()):
    """Build the index and give (the result code, the lines to print). An error does not stop the caller.

    >>> import sample
    >>> work = sample.converted()
    >>> build_lines(work)
    (0, ['Index: documents 2, pages 8, sections 12, references 24, acronym pairs 5, groups of synonyms 5,
          updated 2, removed 0.'])
    >>> _ = (work / "converted" / "empty.md").write_text("no page heading", encoding="utf-8")
    >>> code, lines = build_lines(work)
    >>> code, lines[0], lines[1][-21:]
    (1, 'empty: not indexed: the file has no page heading', 'updated 0, removed 0.')
    >>> build_lines(work, synonyms=[work / "absent.txt"])
    (2, ['Index: not built: ...absent.txt: No such file or directory'])
    >>> aspect.long_sentences(MESSAGES)
    []
    """
    try:
        result = build(work, synonyms, spec, seeds)
    except (aspect.Unreadable, OSError, sqlite3.Error) as e:
        return 2, [MESSAGES["not-built"].format(e)]
    numbers = {**result, "updated": len(result["updated"]), "removed": len(result["removed"])}
    return int(bool(result["problems"])), [*result["problems"], MESSAGES["built"].format(**numbers)]


def quoted(term):
    """A term as one phrase of a full-text query.

    >>> print(quoted('an "end user" here'))
    "an ""end user"" here"
    """
    return '"' + term.replace('"', '""') + '"'


def query_terms(query, known):
    """The terms of a query: each word, each phrase in quotation marks, and each run of words
    that is a known term of the synonyms.

    >>> known = {"software requirements specification": [], "srs": []}
    >>> query_terms('review of the Software  requirements specification "end user" - srs', known)
    ['review', 'of', 'the', 'Software requirements specification', 'end user', 'srs']
    >>> query_terms("software requirements", known)
    ['software', 'requirements']
    >>> query_terms('"software" requirements specification', known)
    ['software', 'requirements', 'specification']
    >>> query_terms(" - ", known)
    []
    """
    parts = [(m.group(1) or m.group(2), bool(m.group(1))) for m in QUERY.finditer(query)]
    parts = [(" ".join(text.split()), fixed) for text, fixed in parts if WORD.search(text)]
    terms, i = [], 0
    while i < len(parts):
        ends = range(min(len(parts), i + MAX_WORDS), i + 1, -1)
        runs = (
            (j, " ".join(text for text, _ in parts[i:j])) for j in ends if not any(f for _, f in parts[i:j])
        )
        end, term = next(((j, run) for j, run in runs if run.casefold() in known), (i + 1, parts[i][0]))
        terms.append(term)
        i = end
    return list(dict.fromkeys(terms))


def term_groups(db, query, synonyms=True):
    """The groups of a query: each term with its synonyms of the index.

    >>> import sample
    >>> work = sample.converted()
    >>> _ = build(work)
    >>> with contextlib.closing(connect(work)) as db:
    ...     term_groups(db, "RPO target"), term_groups(db, "RPO", synonyms=False)
    ([['RPO', 'recovery point objective'], ['target']], [['RPO']])
    """
    rows = db.execute("SELECT DISTINCT grp, term FROM synonyms ORDER BY grp, term") if synonyms else ()
    members = collections.defaultdict(list)
    for group, term in rows:
        members[group].append(term)
    known = {term: terms for terms in members.values() for term in terms}
    groups = []
    for term in query_terms(query, known):
        groups.append(
            [term, *(other for other in known.get(term.casefold(), ()) if other != term.casefold())]
        )
    if not groups:
        raise ValueError(MESSAGES["no-words"])
    return groups


def match_of(groups, operator=" AND "):
    """The full-text query of the groups of a query.

    >>> print(match_of([["RPO", "recovery point objective"], ["target"]]))
    ("RPO" OR "recovery point objective") AND ("target")
    """
    return operator.join("(" + " OR ".join(quoted(term) for term in group) + ")" for group in groups)


def search(db, query, doc=None, limit=LIMIT, synonyms=True):
    """The pages that hold the terms of a query. Returns a dictionary with the results.

    Each term is one group with its synonyms. A page must hold one term of each group. If no
    page does, the result is the pages that hold a term of one group or more, and "partial" is
    true. The results are sorted by the rank of the full-text search, the document and the page.
    A result holds no text of a document.

    >>> import sample
    >>> work = sample.converted()
    >>> _ = build(work)
    >>> db = contextlib.closing(sqlite3.connect(work / DATABASE)).__enter__()
    >>> found = search(db, "RPO target")
    >>> found["partial"], found["synonyms"], len(found["results"])
    (False, [['rpo', 'recovery point objective']], 1)
    >>> found["results"][0] == {"document": "S-01", "page": 2, "section": "Kinds of Copies", "matches": 5,
    ...                         "terms": {"RPO": 2, "recovery point objective": 2, "target": 1}}
    True

    The stemmer finds the other forms of a word. A word that a hyphen divides at a line end is found.

    >>> [(r["document"], r["page"], r["terms"]) for r in search(db, "backups")["results"]]
    [('S-02', 1, {'backups': 2}), ('S-01', 3, {'backups': 3}), ('S-01', 6, {'backups': 1}),
     ('S-01', 5, {'backups': 1}), ('S-01', 4, {'backups': 1}), ('S-01', 1, {'backups': 1}),
     ('S-01', 2, {'backups': 1})]
    >>> [(r["page"], r["matches"]) for r in search(db, "backups", doc="S-01", limit=1)["results"]]
    [(3, 3)]

    Without the synonyms, only the words of the query are used.

    >>> [r["page"] for r in search(db, '"recovery time objective"')["results"]]
    [2, 1]
    >>> found = search(db, "RTO", synonyms=False)
    >>> found["synonyms"], [(r["document"], r["page"], r["terms"]) for r in found["results"]]
    ([], [('S-01', 2, {'RTO': 1})])
    >>> [(r["document"], r["page"]) for r in search(db, "RTO")["results"]]
    [('S-01', 2), ('S-02', 1)]

    No page with all terms gives a partial result. No page with a term gives no result.

    >>> found = search(db, "drill quarter zebra")
    >>> found["partial"], [(r["page"], sorted(r["terms"])) for r in found["results"]]
    (True, [(4, ['drill', 'quarter']), (5, ['drill']), (1, ['drill']), (6, ['drill']), (3, ['drill']),
            (2, ['drill'])])
    >>> search(db, "zebra") == {"partial": False, "results": [], "synonyms": []}
    True
    >>> search(db, " - ")
    Traceback (most recent call last):
        ...
    ValueError: the query has no word
    >>> db.close()
    """
    groups = term_groups(db, query, synonyms)

    def pages(operator):
        match = match_of(groups, operator)
        where = "pages MATCH ?" + (" AND document = ?" if doc else "")
        cells = "rowid, document, CAST(page AS INTEGER)"
        sql = f"SELECT {cells} FROM pages WHERE {where} ORDER BY rank, 2, 3 LIMIT ?"
        return db.execute(sql, [match, *([doc] if doc else []), limit]).fetchall()

    found, partial = pages(" AND "), False
    if not found and len(groups) > 1:
        found, partial = pages(" OR "), True
    counts = collections.defaultdict(dict)
    ids = ",".join(str(rowid) for rowid, _, _ in found)
    for term in sorted({term for group in groups for term in group}):
        # The mark of each match makes the text one character longer: the difference is the count.
        sql = (
            "SELECT rowid, length(highlight(pages, 2, char(1), '')) - length(text) FROM pages"
            f" WHERE pages MATCH ? AND rowid IN ({ids})"
        )
        for rowid, count in db.execute(sql, (quoted(term),)):
            counts[rowid][term] = count
    results = []
    for rowid, document, page in found:
        section, matches = section_at(db, document, page), sum(counts[rowid].values())
        results.append(
            {
                "document": document,
                "page": page,
                "section": section,
                "terms": counts[rowid],
                "matches": matches,
            }
        )
    used = [[group[0].casefold(), *group[1:]] for group in groups if len(group) > 1]
    return {"partial": partial, "results": results, "synonyms": used}


def search_lines(found):
    """The lines that the command "search" prints.

    >>> result = {"document": "a", "page": 2, "section": "First", "matches": 3}
    >>> result["terms"] = {"srs": 2, "review": 1}
    >>> found = {"partial": True, "results": [result], "synonyms": [["srs", "a spec"]]}
    >>> print("\\n".join(search_lines(found)))
    No page holds all terms. These pages hold one term or more (a partial result):
    a | page 2 | First | review 1, srs 2 | matches: 3
    Synonyms used: srs = a spec
    >>> search_lines({"partial": False, "results": [], "synonyms": []})
    ['No page holds a term of the query.', 'Synonyms used: none']
    """
    lines = [MESSAGES["partial"]] if found["partial"] else []
    for r in found["results"]:
        terms = ", ".join(f"{term} {count}" for term, count in sorted(r["terms"].items()))
        lines.append(MESSAGES["hit"].format(r["document"], r["page"], r["section"], terms, r["matches"]))
    used = "; ".join(" = ".join(group) for group in found["synonyms"])
    return [*(lines or [MESSAGES["nothing"]]), MESSAGES["synonyms"].format(used or MESSAGES["none"])]


def section_at(db, document, page):
    """The title of the last section that starts on the page or before it, or ""."""
    sql = "SELECT title FROM sections WHERE document = ? AND first_page <= ? ORDER BY seq DESC LIMIT 1"
    return next(iter(db.execute(sql, (document, page)).fetchone() or [""]))


def references(db, document, page):
    """The references on one page, as dictionaries, sorted: the internal references first.

    >>> import sample
    >>> work = sample.converted()
    >>> _ = build(work)
    >>> db = contextlib.closing(sqlite3.connect(work / DATABASE)).__enter__()
    >>> print("\\n".join(reference_lines(references(db, "S-01", 2))))
    internal | figure | Figure 1 | page 2
    internal | name | The Restore Drill | pages 4-5
    internal | page | page 4 | page 4
    internal | section | Section 1 | page 4
    internal | section | Section 1.1 | page 2
    internal | table | Table 2 | page 4
    external | ISO/IEC/IEEE | ISO/IEC 27040 | iso/iec 27040; not in the index
    external | RFC | RFC 2119 | rfc 2119; not in the index
    external | citation | [1] | doi:10.1000/182; not in the index; list entry on page 3
    external | citation | [2] | iso/iec 27040; not in the index; list entry on page 3
    >>> print("\\n".join(reference_lines(references(db, "S-02", 1))))
    external | ISO/IEC/IEEE | IEEE Std 1012 | ieee 1012; not in the index
    external | ISO/IEC/IEEE | ISO/IEC 27040 | iso/iec 27040; not in the index
    external | address | https://standards.example/backups | standards.example/backups; document S-01
    >>> print("\\n".join(reference_lines(references(db, "S-01", 3))[:2]))
    internal | name | The Restore Drill | pages 4-5
    internal | section | Section 9.9 | not resolved
    >>> reference_lines(references(db, "S-01", 1))
    ['The page has no reference.']
    >>> reference_lines([{**references(db, "S-01", 2)[-1], "key": None}])
    ['external | citation | [2] | list entry on page 3']
    >>> db.close()
    """
    names = ("kind", "family", "text", "key", "target_document", "target_first", "target_last")
    sql = f"SELECT DISTINCT {', '.join(names)} FROM refs WHERE document = ? AND page = ?"
    rows = [dict(zip(names, row, strict=True)) for row in db.execute(sql, (document, page))]
    return sorted(rows, key=lambda row: (row["kind"] != "internal", row["family"], row["text"], repr(row)))


def reference_lines(rows):
    """The lines that the command "refs" prints. See references()."""
    lines = []
    for row in rows:
        first, last = row["target_first"], row["target_last"]
        place = MESSAGES["page"].format(first) if first == last else MESSAGES["pages"].format(first, last)
        if row["kind"] == "internal":
            target = [place if first else MESSAGES["not-resolved"]]
        else:
            in_index = row["target_document"] and MESSAGES["in-index"].format(row["target_document"])
            target = [row["key"], in_index or MESSAGES["not-in-index"]] if row["key"] else []
            target += [MESSAGES["entry"].format(first)] if first else []
        lines.append(MESSAGES["ref"].format(row["kind"], row["family"], row["text"], "; ".join(target)))
    return lines or [MESSAGES["no-refs"]]


def cited(db, identifier):
    """Each place that cites a standard, an address or a document, as dictionaries, sorted.

    The identifier can be a name of a document of the index. Then each place that points at
    that document is in the result.

    >>> import sample
    >>> work = sample.converted()
    >>> _ = build(work, spec=sample.folder())
    >>> db = contextlib.closing(sqlite3.connect(work / DATABASE)).__enter__()
    >>> for place in cited(db, "ISO/IEC 27040:2015"):
    ...     print(*place.values(), sep=" | ")
    S-01 | 2 | Kinds of Copies | ISO/IEC/IEEE | ISO/IEC 27040
    S-01 | 2 | Kinds of Copies | citation | [2]
    S-01 | 3 | REFERENCES | ISO/IEC/IEEE | ISO/IEC 27040
    S-02 | 1 | (all pages) | ISO/IEC/IEEE | ISO/IEC 27040
    >>> [(p["document"], p["page"], p["family"]) for p in cited(db, "S-01")]
    [('S-02', 1, 'address'), ('S-02', 1, 'document')]
    >>> cited(db, "guide to Backups") == cited(db, "S-01"), cited(db, "ISO 1")
    (True, [])
    >>> db.close()
    """
    key = key_of(identifier)
    document = db.execute("SELECT min(document) FROM aliases WHERE key = ?", (key,)).fetchone()[0]
    sql = (
        "SELECT DISTINCT document, page, family, text FROM refs"
        " WHERE kind = 'external' AND (key = ? OR target_document = ?) ORDER BY document, page, family, text"
    )
    names = ("document", "page", "section", "family", "text")
    rows = db.execute(sql, (key, document)).fetchall()
    return [dict(zip(names, (d, p, section_at(db, d, p), f, t), strict=True)) for d, p, f, t in rows]


def page_ranges(sections, pages, limit=MAX_PAGES):
    """The page ranges of a document for the readers: (first page, last page, titles of the sections).

    sections: (title, first page, level) in the sequence of the document. A section that fits is
    one range. A section that is too long is divided at its sections of the next level, or, if it
    has none, at page borders. Short ranges that are neighbours are joined. Each page of the
    document is in exactly one range. A range names the sections at which it was divided, not
    the sections in them.

    >>> sections = [("One", 3, 1), ("1.1", 3, 2), ("1.2", 10, 2), ("Two", 30, 1), ("Three", 34, 1)]
    >>> sections += [("3.1", 36, 2)]
    >>> page_ranges(sections, 80, 10)
    [(1, 9, ['One', '1.1']), (10, 19, ['1.2']), (20, 29, ['1.2']), (30, 35, ['Two', 'Three']),
     (36, 45, ['3.1']), (46, 55, ['3.1']), (56, 65, ['3.1']), (66, 75, ['3.1']), (76, 80, ['3.1'])]
    >>> page_ranges(sections, 80, 100), page_ranges([("All", 1, 1)], 5, 2)
    ([(1, 80, ['One', 'Two', 'Three'])], [(1, 2, ['All']), (3, 4, ['All']), (5, 5, ['All'])])
    >>> page_ranges([("Late", 3, 1)], 4, 2)
    [(1, 2, []), (3, 4, ['Late'])]

    Each page is in exactly one range, and no range is longer than the limit.

    >>> import random
    >>> source = random.Random(7)
    >>> for _ in range(300):
    ...     pages, limit = source.randint(1, 60), source.randint(1, 12)
    ...     firsts = sorted(source.randint(1, pages) for _ in range(source.randint(0, 15)))
    ...     sections = [(str(i), first, source.randint(1, 3)) for i, first in enumerate(firsts)]
    ...     found = page_ranges(sections, pages, limit)
    ...     assert [p for a, b, _ in found for p in range(a, b + 1)] == list(range(1, pages + 1))
    ...     assert all(b - a < limit for a, b, _ in found)
    """

    def pieces(first, last, titles, inner):
        if last - first < limit:
            top = min((level for _, _, level in inner), default=0)
            return [(first, last, titles or [title for title, _, level in inner if level == top])]
        if not inner:
            return [(a, min(a + limit - 1, last), titles) for a in range(first, last + 1, limit)]
        top = min(level for _, _, level in inner)
        cuts = {first: (list(titles), [])}
        at = first
        for section in inner:
            if section[2] == top:
                at = min(max(section[1], first), last)
                names = cuts.setdefault(at, ([], []))[0]
                names += [section[0]] if section[0] not in names else []
            else:
                cuts[at][1].append(section)
        starts = sorted(cuts)
        units = []
        for start, end in zip(starts, [*(s - 1 for s in starts[1:]), last], strict=True):
            units += pieces(start, end, *cuts[start])
        joined = []
        for a, b, names in units:
            if joined and b - joined[-1][0] < limit:
                a, names = joined[-1][0], list(dict.fromkeys(joined.pop()[2] + names))
            joined.append((a, b, names))
        return joined

    return pieces(1, pages, [], list(sections))


def read_answers(path):
    r"""The rows of a table of answers: (query, document, the set of the pages).

    >>> import tempfile
    >>> path = pathlib.Path(tempfile.mkdtemp(prefix="sota-index-")) / "answers.md"
    >>> rows = ["| Query | Document | Pages |", "|---|---|---|", "| end user | a | 3, 7-9 |", "| x | a |"]
    >>> _ = path.write_text("\n".join(rows) + "\n")
    >>> read_answers(path)
    [('end user', 'a', [3, 7, 8, 9]), ('x', 'a', [])]
    >>> _ = path.write_text("no table\n")
    >>> read_answers(path)
    Traceback (most recent call last):
        ...
    ValueError: the file has no table with the cells Query, Document and Pages
    """
    tables = [t for t in aspect.Doc(path).tables() if t["header"][:3] == ["query", "document", "pages"]]
    if not tables:
        raise ValueError(MESSAGES["no-answers"])
    rows = []
    for row in tables[0]["rows"]:
        rows.append((row["query"], row["document"], aspect.pages_of(row.get("pages"))))
    return rows


def recall(db, answers, limit=RECALL_LIMIT, synonyms=True, exact=False):
    """Measure the search: (rows found, rows found with a partial result only, the rows not found).

    A row is found when one of its pages is in the first results of the search for its query.
    A page border of a converted file is not exact. Thus the page before and the page after are
    accepted also, if exact is not set.

    >>> import sample
    >>> work = sample.converted()
    >>> _ = build(work)
    >>> db = contextlib.closing(sqlite3.connect(work / DATABASE)).__enter__()
    >>> answers = [("RTO", "S-02", [1]), ("restore drill", "S-01", [5]), ("drill zebra", "S-01", [3]),
    ...            ("zebra", "S-01", [1]), ("-", "S-01", [1]), ("RPO", "S-01", [3])]
    >>> recall(db, answers)
    (4, 1, [('zebra', 'S-01', [1]), ('-', 'S-01', [1])])
    >>> [recall(db, answers, **option)[0] for option in ({"synonyms": False}, {"exact": True}, {"limit": 1})]
    [3, 2, 3]
    >>> db.close()
    """
    found, partial, missing = 0, 0, []
    for query, document, pages in answers:
        wanted = set(pages) if exact else {page + d for page in pages for d in (-1, 0, 1)}
        try:
            result = search(db, query, limit=limit, synonyms=synonyms)
        except ValueError:
            result = {"partial": False, "results": []}
        if any(r["document"] == document and r["page"] in wanted for r in result["results"]):
            found, partial = found + 1, partial + result["partial"]
        else:
            missing.append((query, document, pages))
    return found, partial, missing


def parse_range(text, pages):
    """The first and the last page of a range "FIRST-LAST" of a document with this number of pages.

    >>> parse_range("3-7", 10), parse_range("4", 4)
    ((3, 7), (4, 4))
    >>> for text in ("0-2", "7-3", "3-11", "a-b", "3-"):
    ...     try:
    ...         parse_range(text, 10)
    ...     except ValueError as e:
    ...         print(e)
    the range '0-2' is not in the pages 1-10 of the document
    the range '7-3' is not in the pages 1-10 of the document
    the range '3-11' is not in the pages 1-10 of the document
    the range 'a-b' is not in the pages 1-10 of the document
    the range '3-' is not in the pages 1-10 of the document
    """
    found = RANGE.fullmatch(text)
    first, last = (int(found.group(1)), int(found.group(2) or found.group(1))) if found else (0, 0)
    if not 1 <= first <= last <= pages:
        raise ValueError(MESSAGES["wrong-range"].format(text, pages))
    return first, last


def runs(pages):
    """The runs of pages that follow each other: (first page, last page), sorted.

    >>> runs([9, 1, 2, 3, 7, 10, 2]), runs([])
    ([(1, 3), (7, 7), (9, 10)], [])
    """
    out = []
    for page in sorted(set(pages)):
        if out and page == out[-1][1] + 1:
            out[-1] = (out[-1][0], page)
        else:
            out.append((page, page))
    return out


def spans(pairs):
    """Ranges of pages as the text of one cell: "1-3, 7", or "none".

    >>> spans([(1, 3), (7, 7)]), spans([])
    ('1-3, 7', 'none')
    """
    return ", ".join(str(a) if a == b else f"{a}-{b}" for a, b in pairs) or NONE


def record_given(db, document, first, last, task=""):
    """Record that the pages first to last of a document were given to a reader.

    A range that is recorded two times is one row. A second record without a task keeps the task.

    >>> import sample
    >>> work = sample.converted()
    >>> _ = build(work)
    >>> db = contextlib.closing(connect(work)).__enter__()
    >>> for task in ("the first task", "", "a new  task"):
    ...     record_given(db, "S-01", 2, 3, task)
    ...     print(db.execute("SELECT * FROM given").fetchall())
    [('S-01', 2, 3, 'the first task')]
    [('S-01', 2, 3, 'the first task')]
    [('S-01', 2, 3, 'a new task')]
    >>> db.close()
    """
    db.execute(
        "INSERT INTO given VALUES (?, ?, ?, ?) ON CONFLICT DO UPDATE SET task ="
        " CASE WHEN excluded.task != '' THEN excluded.task ELSE task END",
        (document, first, last, " ".join(task.split())),
    )


def unread(db, document, limit=MAX_PAGES):
    """The pages of one document that are in no recorded range. Returns a dictionary.

    "given" holds each recorded range with its task. "not_read" holds the pages that no reader
    got, as ranges for new readers: each one is a range of page_ranges(), or a part of one, with
    the titles of the sections of that range. The result holds no text of a document.

    >>> import sample
    >>> work = sample.converted()
    >>> _ = build(work)
    >>> db = contextlib.closing(connect(work)).__enter__()
    >>> unread(db, "S-02") == {"document": "S-02", "pages": 2, "given": [],
    ...                        "not_read": [{"first": 1, "last": 2, "sections": ["(all pages)"]}]}
    True
    >>> record_given(db, "S-01", 1, 2, "a task")
    >>> record_given(db, "S-01", 2, 4)
    >>> found = unread(db, "S-01", 2)
    >>> found["given"], found["not_read"]
    ([{'first': 1, 'last': 2, 'task': 'a task'}, {'first': 2, 'last': 4, 'task': ''}],
     [{'first': 5, 'last': 5, 'sections': ['The Restore Drill']},
      {'first': 6, 'last': 6, 'sections': ['Forms']}])
    >>> record_given(db, "S-01", 5, 6)
    >>> unread(db, "S-01")["not_read"]
    []
    >>> db.close()
    """
    pages = db.execute("SELECT pages FROM documents WHERE id = ?", (document,)).fetchone()[0]
    sql = "SELECT first_page, last_page, task FROM given WHERE document = ? ORDER BY 1, 2"
    given = [dict(zip(("first", "last", "task"), row, strict=True)) for row in db.execute(sql, (document,))]
    read = {page for row in given for page in range(row["first"], row["last"] + 1)}
    sql = "SELECT title, first_page, level FROM sections WHERE document = ? ORDER BY seq"
    parts = []
    for first, last, titles in page_ranges(db.execute(sql, (document,)).fetchall(), pages, limit):
        for a, b in runs(page for page in range(first, last + 1) if page not in read):
            parts.append({"first": a, "last": b, "sections": titles})
    return {"document": document, "pages": pages, "given": given, "not_read": parts}


def range_line(document, first, last, titles):
    """One line for a range of pages of a document, with the titles of its sections.

    >>> range_line("a", 3, 3, []), range_line("a", 4, 9, ["One", "Two"])
    ('a | page 3 | number of pages: 1 | (before the first section)',
     'a | pages 4-9 | number of pages: 6 | One; Two')
    """
    place = MESSAGES["page"].format(first) if first == last else MESSAGES["pages"].format(first, last)
    return MESSAGES["range"].format(document, place, last - first + 1, "; ".join(titles) or MESSAGES["front"])


def unread_lines(found):
    """The lines that the command "unread" prints for one document. See unread().

    >>> part = {"first": 5, "last": 6, "sections": ["Forms"]}
    >>> given = [{"first": 1, "last": 2, "task": ""}, {"first": 2, "last": 4, "task": ""}]
    >>> print("\\n".join(unread_lines({"document": "a", "pages": 6, "given": given, "not_read": [part]})))
    a | pages 5-6 | number of pages: 2 | Forms
    a | number of pages: 6 | given to readers: 1-2, 2-4 | not read: 5-6
    """
    lines = [range_line(found["document"], r["first"], r["last"], r["sections"]) for r in found["not_read"]]
    given = spans((r["first"], r["last"]) for r in found["given"])
    left = spans(runs(page for r in found["not_read"] for page in range(r["first"], r["last"] + 1)))
    return [*lines, MESSAGES["reading"].format(found["document"], found["pages"], given, left)]


def reading_rows(db, sources):
    """The rows of the table "Reading": (source, document, pages, ranges given, ranges not read).

    sources: the rows of section 2 of an aspect specification. The document of a source is the
    document with the identifier of the source, or a document that the index knows by the name
    or the address of the source. A source without a document gives no row. A source with "all"
    in the cell Views and without a document gives a row with the document "none".

    >>> import sample
    >>> work = sample.converted({"guide": ["one", "two", "three"], "S-02": ["one"]})
    >>> seeds = [{"id": "guide", "document": "A Guide to Things (AGT)", "address": "https://a.example/form"}]
    >>> _ = build(work, seeds=seeds)
    >>> db = contextlib.closing(connect(work)).__enter__()
    >>> record_given(db, "guide", 2, 2)
    >>> sources = [{"id": "S-01", "source": "AGT", "views": "all"}, {"id": "S-02", "source": "A study"},
    ...            {"id": "S-03", "source": "A page", "views": "all", "url": "https://b.example"},
    ...            {"id": "S-04", "source": "A second page", "views": "storage"},
    ...            {"id": "S-05", "source": "The form", "url": "<https://a.example/form>"}]
    >>> reading_rows(db, sources)
    [('S-01', 'guide', 3, '2', '1, 3'), ('S-02', 'S-02', 1, 'none', '1'), ('S-03', 'none', 0, 'none', 'none'),
     ('S-05', 'guide', 3, '2', '1, 3')]
    >>> db.close()
    """
    documents = {ident for (ident,) in db.execute("SELECT id FROM documents")}
    known = collections.defaultdict(set)
    for key, document in db.execute("SELECT key, document FROM aliases"):
        known[key].add(document)
    rows = []
    for source in sources:
        ident = source.get("id", "")
        texts = (source.get("url", "").strip("<>`"), *names_of(source.get("source", "")))
        found = {ident} & documents
        found |= {document for text in texts if text for document in known[key_of(text)]}
        for document in sorted(found):
            state = unread(db, document)
            given = spans((r["first"], r["last"]) for r in state["given"])
            left = runs(page for r in state["not_read"] for page in range(r["first"], r["last"] + 1))
            rows.append((ident, document, state["pages"], given, spans(left)))
        if not found and check.ALL_VIEWS in aspect.names_of(source.get("views")):
            rows.append((ident, NONE, 0, NONE, NONE))
    return rows


def write_reading(spec, rows):
    r"""Write or replace the table "Reading" in vetting.md of an aspect specification.

    Only the part "Reading" changes. The same rows give the same file. A file with the line end
    of Windows keeps it. Returns the sources with pages that no reader got, each with the number.

    >>> import sample
    >>> spec = sample.folder()
    >>> rows = [("S-01", "S-01", 6, "1-6", "none"), ("S-02", "S-02", 2, "1-2", "none")]
    >>> write_reading(spec, rows), aspect.read_text(spec / "vetting.md") == sample.VETTING
    ([], True)
    >>> write_reading(spec, [("S-01", "a|b", 6, "1-2", "3-6"), ("S-01", "c", 2, "none", "1-2")])
    ['S-01 (6 pages)']
    >>> print(aspect.read_text(spec / "vetting.md")[len(sample.VETTING.split("## Reading")[0]) :])
    ## Reading
    <BLANKLINE>
    The program `index.py unread --write` writes this table. Do not change it by hand.
    <BLANKLINE>
    | Source | Document | Pages | Given to readers | Not read |
    |---|---|---|---|---|
    | S-01 | a\|b | 6 | 1-2 | 3-6 |
    | S-01 | c | 2 | none | 1-2 |
    <BLANKLINE>

    A part "Reading" in the middle of the file is replaced there. A file without the part gets it
    at its end. A folder without the file gets the file.

    >>> head, tail = sample.VETTING.split("## Requirements")
    >>> tail = tail.split("## Reading")[0].rstrip()
    >>> middle = head + "## Reading\n\nold text\n\n## Requirements" + tail + "\n"
    >>> _ = (spec / "vetting.md").write_bytes(middle.replace("\n", "\r\n").encode("utf-8"))
    >>> _ = write_reading(spec, rows)
    >>> text = (spec / "vetting.md").read_bytes().decode("utf-8")
    >>> text.count("\r\n") == text.count("\n"), "old text" in text
    (True, False)
    >>> text.index("## Reading") < text.index("## Requirements")
    True
    >>> [(row["source"], row["not read"]) for row in aspect.load(spec)["reading"]]
    [('S-01', 'none'), ('S-02', 'none')]
    >>> _ = (spec / "vetting.md").write_text(sample.VETTING.split("## Reading")[0], encoding="utf-8")
    >>> write_reading(spec, rows), aspect.read_text(spec / "vetting.md") == sample.VETTING
    ([], True)
    >>> (spec / "vetting.md").unlink()
    >>> _ = write_reading(spec, rows[:1])
    >>> aspect.read_text(spec / "vetting.md").splitlines()[:3], len(aspect.load(spec)["reading"])
    (['# Vetting record: Backups of project data', '', '## Reading'], 1)
    """
    path = pathlib.Path(spec) / "vetting.md"
    if not path.is_file():
        aspect.write_text(path, f"# Vetting record: {aspect.load(spec)['title']}\n")
    text = aspect.read_text(path)
    lines = [line.removesuffix("\r") for line in text.split("\n")]
    block = [f"## {READING}", "", READING_NOTE, "", *table_lines(READING_CELLS, rows)]
    found = aspect.Doc(path).titled(READING)
    if found:
        first, last = found[1]
        lines[first - 1 :] = [*block, "", *lines[last:]]
    else:
        while lines and not lines[-1]:
            lines.pop()
        lines += ["", *block, ""]
    aspect.write_text(path, ("\r\n" if "\r\n" in text else "\n").join(lines))
    left = collections.Counter()
    for row in rows:
        left[row[0]] += len(aspect.pages_of(row[4]))
    return [MESSAGES["pages-left"].format(ident, count) for ident, count in sorted(left.items()) if count]


def table_lines(cells, rows):
    """The lines of a Markdown table: the head, the line below it and one line for each row.

    >>> print(*table_lines(("A", "B"), [("one", 2), ("a|b", "")]), sep=" ; ")
    | A | B | ; |---|---| ; | one | 2 | ; | a\\|b |  |
    """
    lines = ["| " + " | ".join(cells) + " |", "|" + "---|" * len(cells)]
    return lines + ["| " + " | ".join(str(cell).replace("|", "\\|") for cell in row) + " |" for row in rows]


def source_id(text):
    """The identifier of a source, if it has the form "S-<digits>".

    >>> source_id("S-01"), source_id("S-118")
    ('S-01', 'S-118')
    >>> for text in ("s-01", "S-1a", "S-01; DROP TABLE lines", ""):
    ...     try:
    ...         source_id(text)
    ...     except ValueError as e:
    ...         print(e)
    the source 's-01' does not have the form S-<digits>
    the source 'S-1a' does not have the form S-<digits>
    the source 'S-01; DROP TABLE lines' does not have the form S-<digits>
    the source '' does not have the form S-<digits>
    """
    if not SOURCE_ID.fullmatch(text):
        raise ValueError(MESSAGES["wrong-source"].format(text))
    return text


def report_lines(text):
    r"""The lines "REQ" and "USE" of the report of a reader: (the rows, the lines without the form).

    A row is (line number, kind, text, who, purpose, location). For a line "REQ", the text is
    the requirement and who is the group. For a line "USE", the text is the name. A line
    without the form is (line number, "REQ" or "USE"). The lines "REQ | none" and "USE | none"
    give nothing. Each other line of the report gives nothing.

    >>> text = "4. **Requirements**\nREQ | A project must keep two copies. | operators | page 3\n"
    >>> text += "  USE | tool | Restic | Makes the copies each night. | line 12  \nREQ | none\nUSE | none\n"
    >>> text += "USE | pattern | Copy before change | Each change starts with a copy. | job backup\n"
    >>> rows, wrong = report_lines(text)
    >>> for row in rows:
    ...     print(row)
    (2, 'req', 'A project must keep two copies.', 'operators', '', 'page 3')
    (3, 'tool', 'Restic', '', 'Makes the copies each night.', 'line 12')
    (6, 'pattern', 'Copy before change', '', 'Each change starts with a copy.', 'job backup')
    >>> wrong
    []

    A line does not have the form when a cell is absent or empty, when it has one cell more,
    when the kind is a different word, or when the line has other text.

    >>> text = "REQ | no location | operators\nUSE | product | A | b | c\n- REQ | a | b | c\n"
    >>> text += "USE |  | a | b | c\nREQ\nUSE | none | more\n`REQ | a | b | c`\nREQ: none\n"
    >>> text += "REQ | a | b | c | d\nREQ | a |  | c\n"
    >>> report_lines(text + "REQUIRED: nothing\nUSEFUL | tool | a | b | c\nThe REQ lines follow.\n")
    ([], [(1, 'REQ'), (2, 'USE'), (3, 'REQ'), (4, 'USE'), (5, 'REQ'), (6, 'USE'), (7, 'REQ'), (8, 'REQ'),
          (9, 'REQ'), (10, 'REQ')])
    """
    rows, wrong = [], []
    for number, line in enumerate(text.splitlines(), 1):
        found = REPORT_LINE.match(line)
        if not found:
            continue
        head, *cells = (cell.strip() for cell in line.split("|"))
        if head == found.group(1) and cells == [NONE]:
            continue
        if head == REQ and len(cells) == 3 and all(cells):
            rows.append((number, "req", cells[0], cells[1], "", cells[2]))
        elif head == USE and len(cells) == 4 and cells[0] in USE_KINDS and all(cells):
            rows.append((number, cells[0], cells[1], "", cells[2], cells[3]))
        else:
            wrong.append((number, found.group(1)))
    return rows, wrong


def take(db, source, report, text):
    r"""Store the lines "REQ" and "USE" of one report of one source. See report_lines().

    report: the name of the report file. The lines of the same report of the same source that
    the table has are removed first. Thus the same report gives the same content, and a
    corrected report replaces its earlier lines. Returns (the number of stored lines of each
    kind, the lines without the form).

    >>> import sample
    >>> work = sample.converted({})
    >>> db = contextlib.closing(connect(work)).__enter__()
    >>> text = "REQ | A project must keep two copies. | operators | page 3\nREQ | no location\n"
    >>> text += "USE | pattern | Copy first | A copy comes first. | line 2\n"
    >>> take(db, "S-01", "S-01-1.md", text)
    ({'req': 1, 'tool': 0, 'integration': 0, 'framework': 0, 'pattern': 1, 'principle': 0}, [(2, 'REQ')])
    >>> first = db.execute("SELECT * FROM lines").fetchall()
    >>> first
    [('S-01', 'S-01-1.md', 1, 'req', 'A project must keep two copies.', 'operators', '', 'page 3'),
     ('S-01', 'S-01-1.md', 3, 'pattern', 'Copy first', '', 'A copy comes first.', 'line 2')]
    >>> _ = take(db, "S-01", "S-01-1.md", text)
    >>> db.execute("SELECT * FROM lines").fetchall() == first
    True

    A different report and a different source add their lines. The text of a report is data.

    >>> take(db, "S-01", "S-01-1.md", "REQ | none\n")[0]["req"], take(db, "S-02", "S-01-1.md", text)[1]
    (0, [(2, 'REQ')])
    >>> db.execute("SELECT source, kind FROM lines").fetchall()
    [('S-02', 'req'), ('S-02', 'pattern')]
    >>> _ = take(db, "S-02", "S-01-1.md", text.splitlines()[0])
    >>> _ = take(db, "S-02", "b.md", "REQ | x'); DROP TABLE lines; -- | not named | page 1\n")
    >>> db.execute("SELECT source, report, text FROM lines").fetchall()
    [('S-02', 'S-01-1.md', 'A project must keep two copies.'), ('S-02', 'b.md', "x'); DROP TABLE lines; --")]
    >>> db.close()
    """
    rows, wrong = report_lines(text)
    db.execute("DELETE FROM lines WHERE source = ? AND report = ?", (source, report))
    db.executemany(
        "INSERT INTO lines VALUES (?, ?, ?, ?, ?, ?, ?, ?)", [(source, report, *row) for row in rows]
    )
    return {kind: sum(row[1] == kind for row in rows) for kind in LINE_KINDS}, wrong


def stored_lines(db, kind=None, source=None):
    r"""The lines of the reports as the lines of Markdown tables, sorted by the source, the report
    and the line number.

    The table of the requirements is first. The table of the other kinds follows after an empty
    line. A table without a row is left out.

    >>> import sample
    >>> work = sample.converted({})
    >>> db = contextlib.closing(connect(work)).__enter__()
    >>> _ = take(db, "S-10", "a.md", "REQ | Ten. | not named | page 1\nUSE | tool | T | It runs. | line 4\n")
    >>> _ = take(db, "S-2", "b.md", "USE | pattern | P | A way. | line 9\nREQ | Two. | users | page 7\n")
    >>> _ = take(db, "S-2", "a.md", "REQ | First. | users | page 5\n")
    >>> print("\n".join(stored_lines(db)))
    | Source | Requirement | Group | Location |
    |---|---|---|---|
    | S-2 | First. | users | page 5 |
    | S-2 | Two. | users | page 7 |
    | S-10 | Ten. | not named | page 1 |
    <BLANKLINE>
    | Source | Kind | Name | Purpose | Location |
    |---|---|---|---|---|
    | S-2 | pattern | P | A way. | line 9 |
    | S-10 | tool | T | It runs. | line 4 |
    >>> stored_lines(db, "pattern"), stored_lines(db, "req", "S-10")[2:], stored_lines(db, "framework")
    (['| Source | Kind | Name | Purpose | Location |', '|---|---|---|---|---|',
      '| S-2 | pattern | P | A way. | line 9 |'], ['| S-10 | Ten. | not named | page 1 |'], [])

    A principle is a rule that a project states in its own writing, with the reason of the project.

    >>> take(db, "S-3", "c.md", "USE | principle | Test each restore | no reason given | Rules\n")[0]
    {'req': 0, 'tool': 0, 'integration': 0, 'framework': 0, 'pattern': 0, 'principle': 1}
    >>> stored_lines(db, "principle")[2:]
    ['| S-3 | principle | Test each restore | no reason given | Rules |']
    >>> db.close()
    """
    sql = (
        "SELECT source, kind, text, who, purpose, location FROM lines"
        " WHERE (?1 IS NULL OR kind = ?1) AND (?2 IS NULL OR source = ?2)"
        " ORDER BY CAST(substr(source, 3) AS INTEGER), source, report, line"
    )
    rows = db.execute(sql, (kind, source)).fetchall()
    requirements = [(s, text, who, location) for s, k, text, who, _, location in rows if k == "req"]
    uses = [(s, k, text, purpose, location) for s, k, text, _, purpose, location in rows if k != "req"]
    tables = [
        table_lines(cells, part) for cells, part in ((REQ_CELLS, requirements), (USE_CELLS, uses)) if part
    ]
    return [line for n, table in enumerate(tables) for line in ([""] * bool(n) + table)]


def command(name, db, values, options):
    """Do one command that reads the index. Returns (the result code, the lines to print)."""
    as_json = "--json" in options["flags"]
    use_synonyms = "--no-synonyms" not in options["flags"]
    if name == "search":
        found = search(db, values[0], options["doc"], options["limit"] or LIMIT, use_synonyms)
        lines = [json.dumps(found, indent=2, sort_keys=True)] if as_json else search_lines(found)
        return int(not found["results"]), lines
    if name == "cited":
        places = cited(db, values[0])
        lines = [MESSAGES["cite"].format(*place.values()) for place in places]
        lines = [json.dumps(places, indent=2, sort_keys=True)] if as_json else lines
        return int(not places), lines or [MESSAGES["not-cited"].format(values[0])]
    if name == "recall":
        answers = read_answers(values[0])
        found, partial, missing = recall(
            db, answers, options["limit"] or RECALL_LIMIT, use_synonyms, "--exact" in options["flags"]
        )
        share = round(100 * found / len(answers)) if answers else 0
        rows = [MESSAGES["missing"].format(q, d, ", ".join(map(str, pages))) for q, d, pages in missing]
        return 0, [MESSAGES["recall"].format(found, len(answers), share, partial), *rows]
    if name == "take":
        source, path = source_id(values[1]), pathlib.Path(values[0])
        counts, wrong = take(db, source, path.name, aspect.read_text(path))
        db.commit()
        lines = [MESSAGES["no-form"].format(path.name, number, word) for number, word in wrong]
        stored = ", ".join(f"{kind} {count}" for kind, count in counts.items())
        return int(bool(wrong)), [*lines, MESSAGES["taken"].format(source, path.name, stored)]
    if name == "lines":
        kind, source = options["kind"], options["source"]
        if kind is not None and kind not in LINE_KINDS:
            raise ValueError(MESSAGES["wrong-kind"].format(kind, ", ".join(LINE_KINDS)))
        lines = stored_lines(db, kind, None if source is None else source_id(source))
        return int(not lines), lines or [MESSAGES["no-lines"]]
    if name == "unread" and options["write"] is not None:
        rows = reading_rows(db, aspect.load(options["write"])["sources"])
        left = write_reading(options["write"], rows)
        path = pathlib.Path(options["write"]) / "vetting.md"
        return int(bool(left)), [MESSAGES["written"].format(path, len(rows), ", ".join(left) or NONE)]
    if name == "unread" and not values:
        found = [
            unread(db, ident, options["max_pages"] or MAX_PAGES)
            for (ident,) in db.execute("SELECT id FROM documents ORDER BY id").fetchall()
        ]
        lines = [line for state in found for line in unread_lines(state)]
        lines = [json.dumps(found, indent=2, sort_keys=True)] if as_json else lines
        return int(any(state["not_read"] for state in found)), lines
    pages = db.execute("SELECT pages FROM documents WHERE id = ?", (values[0],)).fetchone()
    if pages is None:
        return 1, [MESSAGES["no-document"].format(values[0])]
    if name == "refs":
        rows = references(db, values[0], int(values[1]))
        return int(not rows), [json.dumps(rows, indent=2, sort_keys=True)] if as_json else reference_lines(
            rows
        )
    if name == "unread":
        found = unread(db, values[0], options["max_pages"] or MAX_PAGES)
        lines = [json.dumps([found], indent=2, sort_keys=True)] if as_json else unread_lines(found)
        return int(bool(found["not_read"])), lines
    if name == "given":
        first, last = parse_range(values[1], pages[0])
        place = MESSAGES["page"].format(first) if first == last else MESSAGES["pages"].format(first, last)
        if "--remove" in options["flags"]:
            sql = "DELETE FROM given WHERE document = ? AND first_page = ? AND last_page = ?"
            removed = db.execute(sql, (values[0], first, last)).rowcount
            db.commit()
            said = MESSAGES["removed" if removed else "not-recorded"].format(values[0], place)
            return int(not removed), [said]
        record_given(db, values[0], first, last, options["task"] or "")
        db.commit()
        return 0, [MESSAGES["recorded"].format(values[0], place)]
    sql = "SELECT title, first_page, level FROM sections WHERE document = ? ORDER BY seq"
    found = page_ranges(db.execute(sql, (values[0],)).fetchall(), pages[0], options["max_pages"] or MAX_PAGES)
    return 0, [range_line(values[0], *part) for part in found]


# The numbers of the arguments that each command can have after the work folder.
COMMANDS = {
    "build": (0,),
    "search": (1,),
    "refs": (2,),
    "cited": (1,),
    "ranges": (1,),
    "recall": (1,),
    "given": (2,),
    "unread": (0, 1),
    "take": (2,),
    "lines": (0,),
}
FLAGS = {"--no-synonyms", "--json", "--exact", "--remove"}


def main(argv=None):
    r"""The command line. See the text at the start of this file. Returns the result code.

    >>> import tempfile
    >>> import sample
    >>> work = sample.converted()
    >>> def run(*args):
    ...     code, out, err = sample.run(main, *args)
    ...     print((out + err).replace(str(work), "WORK").strip())
    ...     return code
    >>> run("search", work, "backup")
    The folder has no index. Run: index.py build WORK
    2
    >>> run("build", work, "--from", sample.folder())
    Index: documents 2, pages 8, sections 12, references 25, acronym pairs 5, groups of synonyms 5, updated 2,
    removed 0.
    0

    The search gives pointers and no text of a document.

    >>> run("search", work, "RPO target")
    S-01 | page 2 | Kinds of Copies | RPO 2, recovery point objective 2, target 1 | matches: 5
    Synonyms used: rpo = recovery point objective
    0
    >>> run("search", work, "RPO", "--no-synonyms", "--doc", "S-01", "--limit", "5")
    S-01 | page 2 | Kinds of Copies | RPO 2 | matches: 2
    Synonyms used: none
    0
    >>> run("search", work, "zebra"), run("search", work, "zebra", "--json")
    No page holds a term of the query.
    Synonyms used: none
    {
      "partial": false,
      "results": [],
      "synonyms": []
    }
    (1, 1)

    The references of a page, and the places that cite one identifier.

    >>> run("refs", work, "S-02", "1")
    external | ISO/IEC/IEEE | IEEE Std 1012 | ieee 1012; not in the index
    external | ISO/IEC/IEEE | ISO/IEC 27040 | iso/iec 27040; not in the index
    external | address | https://standards.example/backups | standards.example/backups; document S-01
    external | document | Guide to backups | guide to backups; document S-01
    0
    >>> run("refs", work, "S-01", "1"), run("refs", work, "S-09", "1")
    The page has no reference.
    The index has no document 'S-09'.
    (1, 1)
    >>> json.loads(sample.run(main, "refs", work, "S-02", "2", "--json")[1])
    []
    >>> run("cited", work, "Guide to backups")
    S-02 | page 1 | (all pages) | address | https://standards.example/backups
    S-02 | page 1 | (all pages) | document | Guide to backups
    0
    >>> run("cited", work, "ISO 1")
    No place cites 'ISO 1'.
    1
    >>> json.loads(sample.run(main, "cited", work, "RFC 2119", "--json")[1])[0]["page"]
    2

    The ranges for the readers.

    >>> run("ranges", work, "S-01", "--max-pages", "2")
    S-01 | page 1 | number of pages: 1 | (before the first section)
    S-01 | pages 2-3 | number of pages: 2 | Copies of the Data
    S-01 | pages 4-5 | number of pages: 2 | The Restore Drill
    S-01 | page 6 | number of pages: 1 | Forms
    0
    >>> run("ranges", work, "S-01", "--max-pages", "1")
    S-01 | page 1 | number of pages: 1 | (before the first section)
    S-01 | page 2 | number of pages: 1 | Copies of the Data; ACRONYMS; INTRODUCTION
    S-01 | page 3 | number of pages: 1 | Places; REFERENCES
    S-01 | page 4 | number of pages: 1 | The Restore Drill
    S-01 | page 5 | number of pages: 1 | Records of a Drill
    S-01 | page 6 | number of pages: 1 | Forms
    0
    >>> run("ranges", work, "S-02")
    S-02 | pages 1-2 | number of pages: 2 | (all pages)
    0

    The record of the ranges that were given to the readers, and the pages that no reader got.
    A page that is in no recorded range gives the result code 1.

    >>> run("given", work, "S-01", "1-3", "--task", "the concerns of the operators")
    Recorded: S-01 | pages 1-3
    0
    >>> run("given", work, "S-01", "1-3"), run("given", work, "S-01", "6"), run("given", work, "S-01", "3-5")
    Recorded: S-01 | pages 1-3
    Recorded: S-01 | page 6
    Recorded: S-01 | pages 3-5
    (0, 0, 0)
    >>> run("given", work, "S-01", "3-5", "--remove"), run("given", work, "S-01", "3-5", "--remove")
    Removed: S-01 | pages 3-5
    The record has no range pages 3-5 of the document 'S-01'.
    (0, 1)
    >>> run("unread", work, "--max-pages", "2")
    S-01 | pages 4-5 | number of pages: 2 | The Restore Drill
    S-01 | number of pages: 6 | given to readers: 1-3, 6 | not read: 4-5
    S-02 | pages 1-2 | number of pages: 2 | (all pages)
    S-02 | number of pages: 2 | given to readers: none | not read: 1-2
    1
    >>> run("unread", work, "S-01")
    S-01 | pages 4-5 | number of pages: 2 | Copies of the Data; The Restore Drill; Forms
    S-01 | number of pages: 6 | given to readers: 1-3, 6 | not read: 4-5
    1
    >>> json.loads(sample.run(main, "unread", work, "S-01", "--json")[1])[0]["given"][0]
    {'first': 1, 'last': 3, 'task': 'the concerns of the operators'}
    >>> [state["document"] for state in json.loads(sample.run(main, "unread", work, "--json")[1])]
    ['S-01', 'S-02']

    --write writes the table "Reading" into vetting.md of an aspect specification. The table
    has one row for each converted document that is a source of section 2.

    >>> spec = sample.folder()
    >>> code, out, _ = sample.run(main, "unread", work, "--write", spec)
    >>> code, out.replace(str(spec), "SPEC").strip()
    (1, 'The table Reading of SPEC/vetting.md is written. Rows: 2. Sources with pages that no reader got:
         S-01 (2 pages), S-02 (2 pages).')
    >>> [(r["source"], r["given to readers"], r["not read"]) for r in aspect.load(spec)["reading"]]
    [('S-01', '1-3, 6', '4-5'), ('S-02', 'none', '1-2')]
    >>> run("given", work, "S-01", "4-5"), run("given", work, "S-02", "1-2"), run("unread", work)
    Recorded: S-01 | pages 4-5
    Recorded: S-02 | pages 1-2
    S-01 | number of pages: 6 | given to readers: 1-3, 4-5, 6 | not read: none
    S-02 | number of pages: 2 | given to readers: 1-2 | not read: none
    (0, 0, 0)
    >>> code, out, _ = sample.run(main, "unread", work, "--write", spec)
    >>> code, out.replace(str(spec), "SPEC").strip()
    (0, 'The table Reading of SPEC/vetting.md is written. Rows: 2. Sources with pages that no reader got:
         none.')
    >>> run("given", work, "S-01", "7"), run("given", work, "S-09", "1"), run("unread", work, "S-09")
    The input cannot be read: the range '7' is not in the pages 1-6 of the document
    The index has no document 'S-09'.
    The index has no document 'S-09'.
    (2, 1, 1)
    >>> wrong = [("unread", work, "S-01", "--write", spec), ("search", work, "a", "--write", spec)]
    >>> wrong += [("unread", work, "--write"), ("given", work, "S-01"), ("unread", work, "a", "b")]
    >>> [sample.run(main, *args)[0] for args in wrong]
    [2, 2, 2, 2, 2]
    >>> sample.run(main, "unread", work, "--write", work / "absent")[0]
    2

    The lines "REQ" and "USE" of the reports of the readers. A line without the form is not
    stored, and gives the result code 1. A report that is taken again replaces its lines.

    >>> report = work / "reports" / "S-01-1.md"
    >>> report.parent.mkdir()
    >>> text = "REQ | A project must keep two copies. | operators | page 3\nREQ | none\n"
    >>> _ = report.write_text(text + "REQ | A copy should be in a second place.\n", encoding="utf-8")
    >>> run("take", work, report, "S-01")
    S-01-1.md | line 3 | not stored: the line does not have the form of a REQ line
    Stored: S-01 | S-01-1.md | req 1, tool 0, integration 0, framework 0, pattern 0, principle 0
    1
    >>> _ = report.write_text(text + "REQ | A copy should be in a second place. | not named | page 4\n")
    >>> run("take", work, report, "S-01"), run("take", work, report, "S-01")
    Stored: S-01 | S-01-1.md | req 2, tool 0, integration 0, framework 0, pattern 0, principle 0
    Stored: S-01 | S-01-1.md | req 2, tool 0, integration 0, framework 0, pattern 0, principle 0
    (0, 0)
    >>> sample_report = report.with_name("S-18-1.md")
    >>> text = "USE | tool | Restic | Makes the copies each night. | line 12\nUSE | none\n"
    >>> _ = sample_report.write_text(text + "USE | pattern | Copy first | A copy comes first. | job backup\n")
    >>> run("take", work, sample_report, "S-18")
    Stored: S-18 | S-18-1.md | req 0, tool 1, integration 0, framework 0, pattern 1, principle 0
    0
    >>> run("lines", work)
    | Source | Requirement | Group | Location |
    |---|---|---|---|
    | S-01 | A project must keep two copies. | operators | page 3 |
    | S-01 | A copy should be in a second place. | not named | page 4 |
    <BLANKLINE>
    | Source | Kind | Name | Purpose | Location |
    |---|---|---|---|---|
    | S-18 | tool | Restic | Makes the copies each night. | line 12 |
    | S-18 | pattern | Copy first | A copy comes first. | job backup |
    0
    >>> run("lines", work, "--kind", "pattern", "--source", "S-18")
    | Source | Kind | Name | Purpose | Location |
    |---|---|---|---|---|
    | S-18 | pattern | Copy first | A copy comes first. | job backup |
    0
    >>> run("lines", work, "--kind", "req", "--source", "S-18"), run("lines", work, "--kind", "other")
    The index has no such line of a report.
    The input cannot be read: the kind 'other' is not one of these words: req, tool, integration, framework,
    pattern, principle
    (1, 2)
    >>> run("lines", work, "--source", "18"), run("take", work, report, "one")
    The input cannot be read: the source '18' does not have the form S-<digits>
    The input cannot be read: the source 'one' does not have the form S-<digits>
    (2, 2)
    >>> run("take", work, work / "reports" / "absent.md", "S-01")
    The input cannot be read: WORK/reports/absent.md: No such file or directory
    2
    >>> [sample.run(main, *args)[0] for args in (("take", work, report), ("lines", work, "S-01"))]
    [2, 2]

    A build keeps the lines of the reports.

    >>> run("build", work, "--from", sample.folder())
    Index: documents 2, pages 8, sections 12, references 25, acronym pairs 5, groups of synonyms 5, updated 0,
    removed 0.
    0
    >>> run("lines", work, "--kind", "tool")
    | Source | Kind | Name | Purpose | Location |
    |---|---|---|---|---|
    | S-18 | tool | Restic | Makes the copies each night. | line 12 |
    0

    The measure of the search.

    >>> answers = work / "answers.md"
    >>> rows = ["| Query | Document | Pages |", "|---|---|---|", "| RTO | S-02 | 1 |"]
    >>> rows += ["| zebra | S-01 | 2-3 |"]
    >>> _ = answers.write_text("\n".join(rows) + "\n", encoding="utf-8")
    >>> run("recall", work, answers)
    Found: 1 of 2 (50 %). Found with a partial result only: 0.
    Not found: zebra | S-01 | 2, 3
    0
    >>> run("recall", work, answers, "--no-synonyms", "--exact", "--limit", "3")
    Found: 0 of 2 (0 %). Found with a partial result only: 0.
    Not found: RTO | S-02 | 1
    Not found: zebra | S-01 | 2, 3
    0
    >>> _ = answers.write_text("\n".join(rows[:2]) + "\n", encoding="utf-8")
    >>> run("recall", work, answers)
    Found: 0 of 0 (0 %). Found with a partial result only: 0.
    0

    A file that is not indexed gives the result code 1. Input that cannot be read and wrong
    arguments give the result code 2.

    >>> _ = (work / "converted" / "empty.md").write_text("no page heading", encoding="utf-8")
    >>> run("build", work, "--manifest", seed.MANIFEST)
    empty: not indexed: the file has no page heading
    Index: documents 2, pages 8, sections 12, references 24, acronym pairs 5, groups of synonyms 5, updated 0,
    removed 0.
    1
    >>> run("build", work, "--synonyms", work / "absent.txt"), run("recall", work, work / "absent.md")
    Index: not built: WORK/absent.txt: No such file or directory
    The input cannot be read: WORK/absent.md: No such file or directory
    (2, 2)
    >>> run("build", work, "--manifest", work / "absent.md"), run("build", work, "--manifest", answers)
    The input cannot be read: WORK/absent.md: No such file or directory
    answers.md:1 : The manifest has no table of seeds.
    (2, 2)
    >>> run("search", work, " - "), run("refs", work, "S-01", "one")
    The input cannot be read: the query has no word
    The input cannot be read: invalid literal for int() with base 10: 'one'
    (2, 2)
    >>> outside = pathlib.Path(tempfile.mkdtemp(prefix="sota-index-"))
    >>> (outside / "repo" / ".git").mkdir(parents=True)
    >>> code, out, _ = sample.run(main, "build", outside / "repo" / "work")
    >>> code, out.strip(), (outside / "repo" / "work").exists()
    (2, 'Nothing was done: the folder WORK must be outside each git repository.', False)
    >>> wrong = [(), ("--help",), ("build",), ("other", work), ("search", work), ("ranges", work, "a", "x")]
    >>> wrong += [("search", work, "a", "--limit", "0"), ("search", work, "a", "--other")]
    >>> [sample.run(main, *args)[0] for args in wrong]
    [2, 2, 2, 2, 2, 2, 2, 2]
    """
    args = [str(a) for a in (sys.argv[1:] if argv is None else argv)]
    files = []
    while (value := check.option(args, "--synonyms")) is not None:
        files.append(value)
    spec, manifest, doc = (check.option(args, flag) for flag in ("--from", "--manifest", "--doc"))
    task, write = check.option(args, "--task"), check.option(args, "--write")
    kind, source = check.option(args, "--kind"), check.option(args, "--source")
    numbers = [check.option(args, flag) for flag in ("--limit", "--max-pages")]
    flags = {a for a in args if a.startswith("--")}
    names = [a for a in args if not a.startswith("--")]
    wrong = flags - FLAGS or any(n is not None and not (n.isdigit() and int(n)) for n in numbers)
    wrong = wrong or (write is not None and (names[:1] != ["unread"] or len(names) != 2 or not write))
    if wrong or not names or len(names) - 2 not in COMMANDS.get(names[0], ()):
        print(__doc__, file=sys.stderr)
        return 2
    name, work = names[0], pathlib.Path(names[1])
    if render.in_repository(work):
        print(MESSAGES["in-repository"])
        return 2
    limit, max_pages = (int(n) if n else None for n in numbers)
    options = {"flags": flags, "doc": doc, "limit": limit, "max_pages": max_pages, "task": task}
    options.update(write=write, kind=kind, source=source)
    try:
        if name == "build":
            seeds, _, problems = seed.read_manifest(manifest or seed.MANIFEST)
            code, lines = (2, problems) if problems else build_lines(work, files, spec, seeds)
        elif not (work / DATABASE).is_file():
            code, lines = 2, [MESSAGES["no-index"].format(work)]
        else:
            with contextlib.closing(connect(work)) as db:
                code, lines = command(name, db, names[2:], options)
    except (aspect.Unreadable, OSError, sqlite3.Error, ValueError) as e:
        code, lines = 2, [MESSAGES["unreadable"].format(e)]
    print("\n".join(lines))
    return code


if __name__ == "__main__":
    if sys.argv[1:2] == ["--selftest"]:
        sys.exit(aspect.selftest())
    sys.exit(main())
