#!/usr/bin/env python3
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Gate for a trial of an agent, a skill, a prompt or an instruction: a registered experiment.

  experiment.py check DIR
  experiment.py seal  DIR --today DATE
  experiment.py run   DIR --work WORKDIR
  experiment.py blind DIR --work WORKDIR
  experiment.py score DIR

  DIR       the folder of one experiment. It holds registration.md, the prompt files and the
            input folders. The template is references/registration-template.md.
  DATE      the date of the seal, as YYYY-MM-DD.
  WORKDIR   a folder outside each git repository, with no instruction file for agents in it
            or above it. The run folders, the transcripts and the packets for the judge go there.

  check   examines the registration. It prints one line FAIL for each finding, the differences
          between the arms, and the instruction files that the input folders hold.
  seal    runs the check and writes sealed.json: the digest of the registration, of each prompt
          file and of each input file. In a git repository these files must be committed.
  run     starts the sessions of each run that has no valid row in results.jsonl. It refuses a
          registration that has no seal or that changed after the seal. It builds each run
          folder from the input folder of the arm, in a clean environment.
  blind   writes one packet for each valid run into WORKDIR/packets, for the judge. A packet
          does not show the arm. The key is blind-key.json in DIR.
  score   counts the answers and writes result.md: the counts, the intervals, the comparison
          of the arms and the verdict from the registered limits.

Result code 0: nothing fails and nothing remains. Result code 1: something fails or remains.
Result code 2: the input cannot be read, or the arguments are wrong.
"""

import concurrent.futures
import datetime
import difflib
import doctest
import hashlib
import itertools
import json
import math
import operator
import os
import pathlib
import re
import shutil
import subprocess
import sys

SECTIONS = {
    "1": "Question",
    "2": "Hypothesis",
    "3": "Measure",
    "4": "Arms",
    "5": "Subject",
    "6": "Words of the expected answer",
    "7": "Predictions",
    "8": "Environment",
}
REQUIRED = {
    "1": ("quote", "date"),
    "2": ("statement", "forbidden result", "criterion", "confirmed when", "refuted when"),
    "5": ("product", "model", "tools", "runs for each arm", "time limit", "git repository"),
    "8": ("plugins", "connectors", "skills", "agents"),
}
OUTCOMES = ("confirmed", "refuted", "not decided")
# The lists of the first event of a session, and the field of section 8 that permits a name.
LISTS = {"plugins": "plugins", "mcp_servers": "connectors", "skills": "skills", "agents": "agents"}
INSTRUCTION_FILES = ("AGENTS.md", "CLAUDE.local.md", "CLAUDE.md", "GEMINI.md", ".cursorrules", ".mcp.json")
INSTRUCTION_FOLDERS = (".agents", ".claude", ".codex", ".cursor")
MIN_RUNS = 5
POOL = 4
MAX_RESULTS = 200_000
JUDGE_TASK = pathlib.Path(__file__).resolve().parent.parent / "prompts" / "judge.md"
# A file of a run that a criterion names is stored up to this size. The limit was 100,000
# characters; a file of 207,740 characters lost its last table, and a criterion gave a wrong "no".
MAX_FILE = 5_000_000

HEADING = re.compile(r"^##\s+(\d+)\.\s")
FIELD = re.compile(r"^- \*\*([^*]+)\*\*:\s*(.*)$")
SUB_ITEM = re.compile(r"^\s+- `([^`]+)`:\s*(.*)$")
ITEM = re.compile(r"^- (.*\S)\s*$")
SEPARATOR = re.compile(r"^\|(\s*:?-+:?\s*\|)+\s*$")
QUOTE = re.compile(r"[\"“].*\S.*[\"”]")
ARM = re.compile(r"[A-Za-z]\w*")
WHERE = re.compile(r"file:(?!/)(?!.*\.\.)\S+")
LIMIT = re.compile(r"([A-Za-z]\w*)(?:\s+-\s+([A-Za-z]\w*))?\s*(>=|<=|==|>|<)\s*(\d+)")
OPERATORS = {">=": operator.ge, "<=": operator.le, "==": operator.eq, ">": operator.gt, "<": operator.lt}

MESSAGES = {
    "unreadable": "The input cannot be read: {0}",
    "empty": "The field is empty.",
    "no-quote": "The field holds no quote. Write the words of the owner between quotation marks.",
    "no-date": "The date does not have the form YYYY-MM-DD.",
    "no-outcome": "The decision is empty for: {0}.",
    "same-decision": "Each outcome gives the same decision. Do not run the experiment.",
    "no-limit": "The limit cannot be read. Write `ARM - ARM >= NUMBER` or `ARM >= NUMBER`.",
    "unknown-arm": "The limits name an arm that section 4 does not have: {0}.",
    "unknown-criterion": "Section 3 does not have the criterion {0}.",
    "overlap": "The two limits are true together for: {0}.",
    "never": "No result can make the hypothesis {0}.",
    "no-id": "The criterion has no id.",
    "twice": "The id is used two times.",
    "no-question": "The criterion has no question.",
    "no-answerer": "The cell `Answered by` must hold `program` or `judge`.",
    "no-pattern": "A criterion of the program needs a pattern that compiles.",
    "no-where": "The cell `Where` must hold `final` or `file:<path in the run folder>`.",
    "no-arm-id": "The id of an arm starts with a letter and holds only letters, digits and `_`.",
    "no-text": "The cell `What differs` is empty.",
    "no-prompt": "The arm has no prompt file.",
    "no-file": "The prompt file is not in the folder of the experiment: {0}",
    "no-folder": "The input folder is not in the folder of the experiment: {0}",
    "one-arm": "There are fewer than two arms. Add an arm, or add the field `One arm` with the reason.",
    "same-arms": "The two arms have the same prompts and the same inputs.",
    "many-differences": "The two arms differ in {0} things. Add the field `More than one difference` "
    "with the reason, or change the arms.",
    "no-host": "The program does not know the product {0}. It knows: {1}.",
    "no-number": "The field must hold a number above 0.",
    "few-runs": "There are fewer than 5 runs for each arm. Add the field `Fewer than five runs` "
    "with the reason.",
    "no-yes-no": "The field must hold `yes` or `no`.",
    "no-reason": "`(none)` needs a reason: `- (none): <reason>`.",
    "leak": "The word is in {0}, line {1}.",
    "no-prediction": "There is no predicted count from 0 to the number of runs.",
    "differences": "Differences between the arms:",
    "only-prompt": "prompt {0}: only the arm {1} has one",
    "prompt-differs": "prompt {0} ({1}, {2}): the lines {3} to {4} differ",
    "only-input": "input file {0}: only the arm {1} has it",
    "input-differs": "input file {0}: the content differs",
    "instructions": "Loaded instructions:",
    "fails": "Result: {0} checks fail.",
    "complete": "Result: the registration is complete.",
    "has-result": "No seal: results.jsonl exists. A registration with a result cannot be sealed again.",
    "not-committed": "No seal: commit these files first. Git shows a change:",
    "sealed": "Sealed: {0} files, seal {1}, commit {2}.",
    "no-seal": "sealed.json is absent or cannot be read. Run the command seal first.",
    "changed": "{0} changed after the seal.",
    "refused": "Refused:",
    "in-repository": "{0} is in a git repository. Use a work folder outside each repository.",
    "instructions-above": "An agent in the work folder loads {0}. Use a different work folder.",
    "time-limit": "the session did not end in {0} seconds",
    "no-start": "the product did not start: {0}",
    "result-code": "the product ended with the result code {0}",
    "no-init": "the stream has no start event",
    "no-result": "the stream has no result",
    "not-clean": "the environment is not clean: {0}",
    "run-valid": "arm {0}, run {1}: valid",
    "run-not-valid": "arm {0}, run {1}: not valid: {2}",
    "runs": "Valid runs: {0} of {1}. The transcripts are in {2}.",
    "runs-remain": "Runs remain: {0} of {1} are valid. Run the command run again.",
    "no-judge": "No criterion has the judge. No packet is necessary.",
    "packets": "Packets: {0} in {1}. Give only this folder to the judge.",
    "judgement-unknown": "judgements.md line {0}: the code or the criterion is not known.",
    "judgement-wrong": "judgements.md line {0}: the answer is not `yes` or `no`, or the evidence is empty.",
    "judgement-twice": "judgements.md line {0}: there is a second answer for {1}, {2}.",
    "judgement-missing": "judgements.md has no answer for {0}, {1}.",
    "verdict-none": "none: runs or answers remain",
    "guess": "Each explanation written here is a guess. No next step rests on it.",
    "written": "Written: {0}",
}


class Unreadable(Exception):
    """A file of the experiment cannot be read."""


def digest(data):
    """The sha256 digest of bytes or of a text.

    >>> digest(b"a")[:8], digest("a")[:8]
    ('ca978112', 'ca978112')
    """
    return hashlib.sha256(data.encode("utf-8") if isinstance(data, str) else data).hexdigest()


def read(path):
    r"""The text of a file in UTF-8.

    >>> import tempfile
    >>> path = pathlib.Path(tempfile.mkdtemp(prefix="experiment-")) / "a.md"
    >>> _ = path.write_bytes(b"one\n")
    >>> read(path)
    'one\n'

    A file that is absent or is not UTF-8 cannot be read. The caller reports it.

    >>> def error_of(path):
    ...     try:
    ...         read(path)
    ...     except Unreadable as e:
    ...         return str(e).split(": ", 1)[1]
    >>> _ = path.write_bytes(b"one\xff\n")
    >>> error_of(path), error_of(path.with_name("absent.md"))
    ('the file is not UTF-8', 'No such file or directory')
    """
    try:
        return pathlib.Path(path).read_text(encoding="utf-8")
    except OSError as e:
        raise Unreadable(f"{path}: {e.strerror}") from e
    except UnicodeDecodeError as e:
        raise Unreadable(f"{path}: the file is not UTF-8") from e


def tree(folder):
    """The files of a folder: the relative path and the digest of each. No folder gives no file.

    >>> import sample
    >>> base = sample.folder()
    >>> {name: value[:6] for name, value in tree(base / "inputs" / "base").items()}
    {'note.txt': '6187ba'}
    >>> tree(base / "absent"), tree(None)
    ({}, {})
    """
    if folder is None:
        return {}
    found = sorted(p for p in pathlib.Path(folder).rglob("*") if p.is_file())
    return {p.relative_to(folder).as_posix(): digest(p.read_bytes()) for p in found}


def split_row(line):
    r"""The cells of one table row. A pipe after a backslash is text.

    >>> split_row("| a | b c |  |"), split_row(r"| `a\|b` | c |")
    (['a', 'b c', ''], ['`a|b`', 'c'])
    """
    return [cell.strip().replace("\\|", "|") for cell in re.split(r"(?<!\\)\|", line.strip())[1:-1]]


def table(lines):
    r"""The rows of the first table in the numbered lines: one dictionary for each row.

    >>> rows = table([(4, "text"), (5, "| Id | Name |"), (6, "|---|---|"), (7, "| a | one |"), (8, "| b |"), (9, "")])
    >>> rows
    [{'id': 'a', 'name': 'one', '_line': 7}, {'id': 'b', '_line': 8}]
    >>> table([(1, "| no table |")]), table([])
    ([], [])
    """
    for at in range(len(lines) - 1):
        if lines[at][1].startswith("|") and SEPARATOR.match(lines[at + 1][1]):
            header = [name.lower() for name in split_row(lines[at][1])]
            rows = itertools.takewhile(lambda item: item[1].startswith("|"), lines[at + 2 :])
            return [{**dict(zip(header, split_row(line), strict=False)), "_line": n} for n, line in rows]
    return []


def fields(lines):
    r"""The fields "- **Name**: text" in the numbered lines. A field can have sub-items.

    >>> found = fields(list(enumerate('''- **Quote**: "one
    ...   two"
    ... - **Decision**: the list.
    ...   - `confirmed`: do this
    ...     and that.
    ...   - `refuted`: do nothing.
    ...
    ...   not a part of a field
    ... '''.splitlines(), 1)))
    >>> found["quote"], found["decision"]["items"]
    ({'value': '"one two"', 'items': {}}, {'confirmed': 'do this and that.', 'refuted': 'do nothing.'})
    """
    out, name, last = {}, None, None
    for _, line in lines:
        field, sub = FIELD.match(line), SUB_ITEM.match(line)
        if field:
            name, last = field.group(1).strip().lower(), None
            out[name] = {"value": field.group(2).strip(), "items": {}}
        elif name and sub:
            last = sub.group(1)
            out[name]["items"][last] = sub.group(2).strip()
        elif name and line.startswith("  ") and line.strip():
            target, key = (out[name]["items"], last) if last else (out[name], "value")
            target[key] = (target[key] + " " + line.strip()).strip()
        else:
            name = None
    return out


def blank(text):
    """True for an empty text and for a placeholder of the template.

    >>> blank(""), blank(" <one sentence> "), blank("`<word>`"), blank("a <b>")
    (True, True, True, False)
    """
    text = text.strip().strip("`").strip()
    return not text or re.fullmatch(r"<[^>]*>", text) is not None


def value(found, name):
    """The text of a field without its backticks, or "" for a field that is absent or blank.

    >>> found = {"a": {"value": "`B - A >= 3`"}, "b": {"value": "<text>"}}
    >>> value(found, "a"), value(found, "b"), value(found, "c")
    ('B - A >= 3', '', '')
    """
    text = found.get(name, {"value": ""})["value"].strip()
    return "" if blank(text) else text.strip("`").strip()


def listed(text):
    """The names in a field. `(none)` gives no name.

    >>> listed("(none)"), listed("Read, `Grep`"), listed("")
    ([], ['Read', 'Grep'], [])
    """
    if text.startswith("(none)"):
        return []
    return [name.strip().strip("`") for name in text.split(",") if name.strip()]


def whole(text):
    """The number in a field, or 0.

    >>> whole("12"), whole("0"), whole("many"), whole("")
    (12, 0, 0, 0)
    """
    return int(text) if text.isdigit() else 0


def is_date(text):
    """True for a date of the form YYYY-MM-DD.

    >>> is_date("2026-10-10"), is_date("2026-13-01"), is_date("10.10.2026"), is_date("20261010")
    (True, False, False, False)
    """
    try:
        return bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", text)) and bool(datetime.date.fromisoformat(text))
    except ValueError:
        return False


def compiles(pattern):
    """True for a regular expression that is not empty and that compiles.

    >>> compiles(r"\\bhello\\b"), compiles("(open"), compiles("")
    (True, False, False)
    """
    try:
        return bool(pattern) and bool(re.compile(pattern))
    except re.error:
        return False


def inside(path):
    """True for a relative path that stays in the folder of the experiment.

    >>> inside("prompts/a.md"), inside("/etc/passwd"), inside("../a.md"), inside("")
    (True, False, False, False)
    """
    return bool(path) and not path.startswith("/") and ".." not in pathlib.PurePosixPath(path).parts


def limit(text):
    """The parts of a limit: (arm, arm to subtract or None, operator, number). None if not readable.

    The number is a count of runs with the answer yes, for the criterion of the hypothesis.

    >>> limit("polite - plain >= 3"), limit("A > 3 and B <= 1")
    ([('polite', 'plain', '>=', 3)], [('A', None, '>', 3), ('B', None, '<=', 1)])
    >>> limit("more than half"), limit("")
    (None, None)
    """
    found = [LIMIT.fullmatch(part.strip()) for part in re.split(r"\s+and\s+", text.strip())]
    if not all(found):
        return None
    return [(m.group(1), m.group(2), m.group(3), int(m.group(4))) for m in found]


def holds(parts, counts):
    """True if each part of a limit is true for the counts of the arms.

    >>> holds(limit("B - A >= 3"), {"A": 1, "B": 4}), holds(limit("B - A >= 3 and A < 1"), {"A": 1, "B": 4})
    (True, False)
    """
    return all(OPERATORS[op](counts[a] - (counts[b] if b else 0), n) for a, b, op, n in parts)


def reach(confirmed, refuted, runs):
    """What the two limits can give: (a result confirms, a result refutes, a result for the two or "").

    >>> reach(limit("B - A >= 3"), limit("B - A <= 0"), 5)
    (True, True, '')
    >>> reach(limit("B - A >= 3"), limit("B - A <= 3"), 5)
    (True, True, 'A = 0, B = 3')
    >>> reach(limit("B >= 9"), limit("B < 0"), 5)
    (False, False, '')

    With many arms and many runs the function does not examine each result.

    >>> reach(limit("B - A >= 3 and C > 1"), limit("D < 1"), 99)
    (True, True, '')
    """
    names = sorted({arm for a, b, _, _ in confirmed + refuted for arm in (a, b) if arm})
    if (runs + 1) ** len(names) > MAX_RESULTS:
        return True, True, ""
    can_confirm, can_refute, both = False, False, ""
    for numbers in itertools.product(range(runs + 1), repeat=len(names)):
        counts = dict(zip(names, numbers, strict=True))
        yes, no = holds(confirmed, counts), holds(refuted, counts)
        can_confirm, can_refute = can_confirm or yes, can_refute or no
        if yes and no and not both:
            both = ", ".join(f"{name} = {counts[name]}" for name in names)
    return can_confirm, can_refute, both


def twice(names):
    """The names that a list holds more than one time, sorted.

    >>> twice(["b", "a", "b", "c", "a"]), twice(["a"])
    (['a', 'b'], [])
    """
    return sorted({name for name in names if names.count(name) > 1})


def blocks(first, second):
    r"""The blocks of lines that differ between two texts: (first line, last line) in the first text.

    >>> blocks("a\nb\nc\nd\n", "a\nB\nc\nD\nE\n"), blocks("a\n", "a\n"), blocks("a\n", "a\nb\n")
    ([(2, 2), (4, 4)], [], [(2, 2)])
    """
    matcher = difflib.SequenceMatcher(None, first.splitlines(), second.splitlines(), autojunk=False)
    return [(a + 1, max(a + 1, b)) for tag, a, b, _, _ in matcher.get_opcodes() if tag != "equal"]


def differences(first, second, folder):
    r"""Each thing that differs between two arms: the prompts by content, the input files by digest.

    >>> import sample
    >>> base = sample.folder(files={"inputs/more/note.txt": "A different note.\n", "inputs/more/b.txt": "b",
    ...     "inputs/less/a.txt": "a"})
    >>> one = {"id": "A", "prompts": ["prompts/plain.md"], "input": "inputs/base"}
    >>> for line in differences(one, {"id": "B", "prompts": ["prompts/polite.md"], "input": "inputs/base"}, base):
    ...     print(line)
    prompt 1 (prompts/plain.md, prompts/polite.md): the lines 1 to 1 differ
    >>> two = {"id": "B", "prompts": ["prompts/plain.md", "prompts/polite.md"], "input": "inputs/more"}
    >>> for line in differences(one, two, base) + differences(two, {**one, "input": "inputs/less"}, base):
    ...     print(line)
    prompt 2: only the arm B has one
    input file b.txt: only the arm B has it
    input file note.txt: the content differs
    prompt 2: only the arm B has one
    input file a.txt: only the arm A has it
    input file b.txt: only the arm B has it
    input file note.txt: only the arm B has it
    >>> differences(one, {**one, "id": "B"}, base), differences(one, {**one, "input": None}, base)
    ([], ['input file note.txt: only the arm A has it'])
    """
    out = []
    pairs = itertools.zip_longest(first["prompts"], second["prompts"])
    for number, (a, b) in enumerate(pairs, 1):
        if a is None or b is None:
            out.append(MESSAGES["only-prompt"].format(number, (first if b is None else second)["id"]))
        else:
            found = blocks(read(folder / a), read(folder / b))
            out += [MESSAGES["prompt-differs"].format(number, a, b, x, y) for x, y in found]
    files = [tree(folder / arm["input"] if arm["input"] else None) for arm in (first, second)]
    for path in sorted(set(files[0]) | set(files[1])):
        if path in files[0] and path in files[1] and files[0][path] != files[1][path]:
            out.append(MESSAGES["input-differs"].format(path))
        elif files[0].get(path) != files[1].get(path):
            out.append(MESSAGES["only-input"].format(path, (first if path in files[0] else second)["id"]))
    return out


def instruction(path):
    """True for a file that an agent product loads as an instruction.

    >>> [instruction(p) for p in ("CLAUDE.md", "docs/AGENTS.md", ".claude/skills/a/SKILL.md", "src/a.py")]
    [True, True, True, False]
    """
    parts = pathlib.PurePosixPath(path).parts
    return parts[-1] in INSTRUCTION_FILES or any(part in INSTRUCTION_FOLDERS for part in parts)


def load(folder):
    r"""Read registration.md of a folder: the fields, the tables and the list of each section.

    >>> import sample
    >>> found = load(sample.folder())
    >>> found["title"], found["1"]["date"]["value"], sorted(found["1"]["decision"]["items"])
    ('a polite prompt', '2026-01-10', ['confirmed', 'not decided', 'refuted'])
    >>> [row["id"] for row in found["3"]], [row["id"] for row in found["4"]], found["6"], len(found["7"])
    (['C-1', 'C-2', 'C-3', 'C-4'], ['plain', 'polite'], ['`hello`'], 8)
    >>> found["4f"], found["8"]["skills"]["value"]
    ({}, '(none)')

    A section with a different number is not read. A folder without the file is an error.

    >>> load(sample.folder(("## 8. Environment", "## 9. Notes")))["8"]
    {}
    >>> load(sample.folder(files={"registration.md": None}))
    Traceback (most recent call last):
        ...
    Unreadable: ...registration.md: No such file or directory
    """
    parts, title, number = {number: [] for number in SECTIONS}, "", None
    for at, line in enumerate(read(pathlib.Path(folder) / "registration.md").splitlines(), 1):
        heading = HEADING.match(line)
        if heading:
            number = heading.group(1) if heading.group(1) in parts else None
        elif number:
            parts[number].append((at, line))
        elif line.startswith("# "):
            title = line[2:].split(":", 1)[-1].strip()
    found = {number: fields(parts[number]) for number in REQUIRED}
    found.update({number: table(parts[number]) for number in ("3", "4", "7")})
    found["6"] = [m.group(1) for _, line in parts["6"] if (m := ITEM.match(line))]
    return {**found, "4f": fields(parts["4"]), "title": title}


def examine(folder):
    r"""Examine the registration of a folder.

    Returns (plan, failures, differences between the arms, instruction files of the input folders).
    The plan holds what the other commands use: the arms, the criteria, the subject, the limits.

    >>> import sample
    >>> plan, failures, lines, instructions = examine(sample.folder())
    >>> failures, instructions
    ([], [])
    >>> lines
    ['plain and polite: prompt 1 (prompts/plain.md, prompts/polite.md): the lines 1 to 1 differ']
    >>> plan["arms"][0]
    {'id': 'plain', 'prompts': ['prompts/plain.md'], 'input': 'inputs/base', 'sound': True}
    >>> plan["criteria"][0]
    {'id': 'C-1', 'question': 'Does the answer hold a greeting?', 'by': 'program', 'pattern': '(?i)\\bhello\\b', 'where': 'final'}
    >>> plan["product"], plan["model"], plan["tools"], plan["runs"], plan["limit"], plan["git"]
    ('claude', 'small-model', ['Read', 'Write'], 5, 60, False)
    >>> plan["permits"], plan["criterion"], plan["predicted"]["polite", "C-1"]
    ({'plugins': [], 'mcp_servers': [], 'skills': [], 'agents': []}, 'C-1', 4)

    Each example below changes the sample and shows the findings.

    >>> def findings(*edits, files=None):
    ...     for line in examine(sample.folder(*edits, files=files))[1]:
    ...         print(line)

    Section 1: the quote of the owner with its date, and a decision for each outcome.

    >>> findings(('"Does the word please change the answer?"', "Find out if please helps."),
    ...     ("2026-01-10", "in January"), ("  - `refuted`: keep the prompt as it is.\n", ""))
    FAIL 1. Question, quote: The field holds no quote. Write the words of the owner between quotation marks.
    FAIL 1. Question, date: The date does not have the form YYYY-MM-DD.
    FAIL 1. Question, decision: The decision is empty for: refuted.
    >>> findings(("add the word to the prompt of the skill.", "go on."), ("keep the prompt as it is.", "go on."),
    ...     ("run a larger experiment.", "go on."), ("- **Date**: 2026-01-10\n", ""))
    FAIL 1. Question, date: The field is empty.
    FAIL 1. Question, decision: Each outcome gives the same decision. Do not run the experiment.

    Section 2: the forbidden result and the two limits. The limits must not be true together, and
    a result must be able to confirm and to refute.

    >>> findings(("The arm polite has no more greetings than the arm plain.", "<the result>"),
    ...     ("`polite - plain >= 3`", "clearly more"), ("- **Refuted when**: `polite - plain <= 0`\n", ""),
    ...     ("- **Criterion**: C-1", "- **Criterion**: C-9"))
    FAIL 2. Hypothesis, forbidden result: The field is empty.
    FAIL 2. Hypothesis, refuted when: The field is empty.
    FAIL 2. Hypothesis, criterion: Section 3 does not have the criterion C-9.
    FAIL 2. Hypothesis, confirmed when: The limit cannot be read. Write `ARM - ARM >= NUMBER` or `ARM >= NUMBER`.
    >>> findings(("`polite - plain <= 0`", "`polite - plain <= 3`"))
    FAIL 2. Hypothesis, refuted when: The two limits are true together for: plain = 0, polite = 3.
    >>> findings(("`polite - plain >= 3`", "`polite >= 6`"), ("`polite - plain <= 0`", "`polite < 0`"))
    FAIL 2. Hypothesis, confirmed when: No result can make the hypothesis confirmed.
    FAIL 2. Hypothesis, refuted when: No result can make the hypothesis refuted.
    >>> findings(("`polite - plain >= 3`", "`polite - other >= 3`"))
    FAIL 2. Hypothesis, confirmed when: The limits name an arm that section 4 does not have: other.

    Section 3: each criterion has an id, a question and who answers it.

    >>> findings(("| C-2 | Is the answer friendly? | judge | | final |", "| C-1 | | person | | the text |"),
    ...     ("`\\d{4}` | file:note.txt", "`(\\d{4}` | file:../note.txt"), ("| C-3 | Does", "| | Does"))
    FAIL 3. Measure, C-1: The criterion has no question.
    FAIL 3. Measure, C-1: The cell `Answered by` must hold `program` or `judge`.
    FAIL 3. Measure, C-1: The cell `Where` must hold `final` or `file:<path in the run folder>`.
    FAIL 3. Measure, line 26: The criterion has no id.
    FAIL 3. Measure, C-4: A criterion of the program needs a pattern that compiles.
    FAIL 3. Measure, C-4: The cell `Where` must hold `final` or `file:<path in the run folder>`.
    FAIL 3. Measure, C-1: The id is used two times.
    FAIL 7. Predictions, plain, : There is no predicted count from 0 to the number of runs.
    FAIL 7. Predictions, polite, : There is no predicted count from 0 to the number of runs.

    >>> findings(("| Id | Question | Answered by | Pattern | Where |\n", ""))
    FAIL 3. Measure, table: The field is empty.
    FAIL 2. Hypothesis, criterion: Section 3 does not have the criterion C-1.

    Section 4: the files of each arm are there, and two arms differ in one thing.

    >>> findings(("| polite | The word please.", "| plain | The word please."))
    FAIL 4. Arms, plain: The id is used two times.
    FAIL 2. Hypothesis, confirmed when: The limits name an arm that section 4 does not have: polite.

    >>> findings(("| polite | The word please. | prompts/polite.md | inputs/base |",
    ...     "| 2 polite | | prompts/absent.md, ../x.md | inputs/absent |\n| empty | No prompt. | | (empty) |"),
    ...     ("`polite - plain >= 3`", "`plain >= 4`"), ("`polite - plain <= 0`", "`plain <= 1`"))
    FAIL 4. Arms, 2 polite: The id of an arm starts with a letter and holds only letters, digits and `_`.
    FAIL 4. Arms, 2 polite: The cell `What differs` is empty.
    FAIL 4. Arms, 2 polite: The prompt file is not in the folder of the experiment: prompts/absent.md
    FAIL 4. Arms, 2 polite: The prompt file is not in the folder of the experiment: ../x.md
    FAIL 4. Arms, 2 polite: The input folder is not in the folder of the experiment: inputs/absent
    FAIL 4. Arms, empty: The arm has no prompt file.
    FAIL 7. Predictions, 2 polite, C-1: There is no predicted count from 0 to the number of runs.
    ...
    FAIL 7. Predictions, empty, C-4: There is no predicted count from 0 to the number of runs.
    >>> one = (("| polite | The word please. | prompts/polite.md | inputs/base |\n", ""),
    ...     ("`polite - plain >= 3`", "`plain >= 4`"), ("`polite - plain <= 0`", "`plain <= 1`"),
    ...     ("| polite | C-1 | 4 |\n| polite | C-2 | 5 |\n| polite | C-3 | 0 |\n| polite | C-4 | 0 |\n", ""))
    >>> findings(*one)
    FAIL 4. Arms, table: There are fewer than two arms. Add an arm, or add the field `One arm` with the reason.
    >>> findings(*one, ("## 5. Subject", "- **One arm**: only the share of one prompt is measured.\n\n## 5. Subject"))
    >>> findings(("prompts/polite.md | inputs/base", "prompts/plain.md | inputs/base"),
    ...     ("| plain | C-4 | 0 |", "| plain | C-4 | 0 |\n| plain | C-4 | 0 |"))
    FAIL 4. Arms, plain and polite: The two arms have the same prompts and the same inputs.
    >>> two = {"inputs/more/note.txt": "A note for the colleague.\n", "inputs/more/CLAUDE.md": "Be polite.\n"}
    >>> more = ("prompts/polite.md | inputs/base", "prompts/polite.md | inputs/more")
    >>> findings(more, files=two)
    FAIL 4. Arms, plain and polite: The two arms differ in 2 things. Add the field `More than one
    difference` with the reason, or change the arms.
    >>> reason = ("## 5. Subject", "- **More than one difference**: the rule needs the prompt.\n\n## 5. Subject")
    >>> plan, failures, lines, instructions = examine(sample.folder(more, reason, files=two))
    >>> failures, instructions
    ([], ['arm polite: inputs/more/CLAUDE.md'])
    >>> for line in lines:
    ...     print(line)
    plain and polite: prompt 1 (prompts/plain.md, prompts/polite.md): the lines 1 to 1 differ
    plain and polite: input file CLAUDE.md: only the arm polite has it

    Section 5: a product that the program knows, and five runs or a reason.

    >>> findings(("**Product**: claude", "**Product**: other"), ("**Runs for each arm**: 5", "**Runs for each arm**: some"),
    ...     ("**Time limit**: 60", "**Time limit**: 0"), ("**Git repository**: no", "**Git repository**: maybe"))
    FAIL 5. Subject, product: The program does not know the product other. It knows: claude.
    FAIL 5. Subject, runs for each arm: The field must hold a number above 0.
    FAIL 5. Subject, time limit: The field must hold a number above 0.
    FAIL 5. Subject, git repository: The field must hold `yes` or `no`.
    >>> few = (("**Runs for each arm**: 5", "**Runs for each arm**: 4"), ("`polite - plain >= 3`", "`polite - plain >= 2`"),
    ...     ("| polite | C-2 | 5 |", "| polite | C-2 | 4 |"))
    >>> findings(*few)
    FAIL 5. Subject, runs for each arm: There are fewer than 5 runs for each arm. Add the field `Fewer than
    five runs` with the reason.
    >>> findings(*few, ("- **Git", "- **Fewer than five runs**: a first look at the cost.\n- **Git"))

    Section 6: no word of the expected answer is in a prompt or in an input file.

    >>> findings(("- `hello`", "- `Colleague`\n- (none)"))
    FAIL 6. Words of the expected answer, (none): `(none)` needs a reason: `- (none): <reason>`.
    FAIL 6. Words of the expected answer, Colleague: The word is in inputs/base/note.txt, line 1.
    FAIL 6. Words of the expected answer, Colleague: The word is in prompts/plain.md, line 1.
    FAIL 6. Words of the expected answer, Colleague: The word is in prompts/polite.md, line 1.
    >>> findings(("- `hello`", "- (none): the answer has no fixed word."))
    >>> findings(("- `hello`", "- `<word or phrase>`"))
    FAIL 6. Words of the expected answer, list: The field is empty.
    >>> findings(("- `hello`\n", ""))
    FAIL 6. Words of the expected answer, list: The field is empty.

    Section 7 and section 8: a prediction for each arm and each criterion, and the permitted names.

    >>> findings(("| plain | C-1 | 1 |", "| plain | C-1 | 6 |"), ("| polite | C-2 | 5 |\n", ""),
    ...     ("- **Skills**: (none)", "- **Skills**:"))
    FAIL 8. Environment, skills: The field is empty.
    FAIL 7. Predictions, plain, C-1: There is no predicted count from 0 to the number of runs.
    FAIL 7. Predictions, polite, C-2: There is no predicted count from 0 to the number of runs.
    >>> examine(sample.folder(("- **Skills**: (none)", "- **Skills**: own-skill, `second`")))[0]["permits"]["skills"]
    ['own-skill', 'second']

    The template is not a complete registration: each field of it fails.

    >>> import shutil, tempfile
    >>> folder = pathlib.Path(tempfile.mkdtemp(prefix="experiment-"))
    >>> template = pathlib.Path(sample.__file__).parents[1] / "references" / "registration-template.md"
    >>> _ = shutil.copy(template, folder / "registration.md")
    >>> failures = examine(folder)[1]
    >>> len(failures), sorted({line.split(".")[0] for line in failures})
    (22, ['FAIL 1', 'FAIL 2', 'FAIL 3', 'FAIL 4', 'FAIL 5', 'FAIL 6', 'FAIL 7'])
    """
    folder = pathlib.Path(folder)
    found = load(folder)
    failures = []

    def fail(section, field, key, *args):
        failures.append(f"FAIL {section}. {SECTIONS[section]}, {field}: " + MESSAGES[key].format(*args))

    for section, names in REQUIRED.items():
        for name in names:
            if not value(found[section], name):
                fail(section, name, "empty")

    # Section 1: the question.
    question = found["1"]
    if value(question, "quote") and not QUOTE.fullmatch(value(question, "quote")):
        fail("1", "quote", "no-quote")
    if value(question, "date") and not is_date(value(question, "date")):
        fail("1", "date", "no-date")
    decisions = question.get("decision", {"items": {}})["items"]
    absent = [name for name in OUTCOMES if blank(decisions.get(name, ""))]
    if absent:
        fail("1", "decision", "no-outcome", ", ".join(absent))
    elif len({decisions[name] for name in OUTCOMES}) == 1:
        fail("1", "decision", "same-decision")

    # Section 3: the criteria.
    criteria = []
    for row in found["3"]:
        criterion = {
            "id": row.get("id", ""),
            "question": row.get("question", ""),
            "by": row.get("answered by", "").lower(),
            "pattern": row.get("pattern", "").strip("`"),
            "where": row.get("where", "") or "final",
        }
        name = criterion["id"] or f"line {row['_line']}"
        if blank(criterion["id"]):
            fail("3", name, "no-id")
        if blank(criterion["question"]):
            fail("3", name, "no-question")
        if criterion["by"] not in ("program", "judge"):
            fail("3", name, "no-answerer")
        if criterion["by"] == "program" and not compiles(criterion["pattern"]):
            fail("3", name, "no-pattern")
        if criterion["where"] != "final" and not WHERE.fullmatch(criterion["where"]):
            fail("3", name, "no-where")
        criteria.append(criterion)
    if not criteria:
        fail("3", "table", "empty")
    for name in twice([c["id"] for c in criteria]):
        fail("3", name, "twice")
    hypothesis = found["2"]
    if value(hypothesis, "criterion") and value(hypothesis, "criterion") not in [c["id"] for c in criteria]:
        fail("2", "criterion", "unknown-criterion", value(hypothesis, "criterion"))

    # Section 4: the arms.
    arms = []
    for row in found["4"]:
        prompts = [name.strip().strip("`") for name in row.get("prompt files", "").split(",") if name.strip()]
        source = row.get("input folder", "").strip("`")
        arm = {"id": row.get("id", ""), "prompts": prompts, "input": None if source == "(empty)" else source}
        name = arm["id"] or f"line {row['_line']}"
        arm["sound"] = bool(prompts)
        if not ARM.fullmatch(arm["id"]):
            fail("4", name, "no-arm-id")
        if blank(row.get("what differs", "")):
            fail("4", name, "no-text")
        if not prompts:
            fail("4", name, "no-prompt")
        for prompt in prompts:
            if not inside(prompt) or not (folder / prompt).is_file():
                fail("4", name, "no-file", prompt)
                arm["sound"] = False
        if arm["input"] is not None and not (inside(source) and (folder / source).is_dir()):
            fail("4", name, "no-folder", source)
            arm["sound"] = False
        arms.append(arm)
    for name in twice([arm["id"] for arm in arms]):
        fail("4", name, "twice")
    if len(arms) < 2 and not value(found["4f"], "one arm"):
        fail("4", "table", "one-arm")
    sound = [arm for arm in arms if arm["sound"]]
    lines = []
    for first, second in itertools.combinations(sound, 2):
        pair = f"{first['id']} and {second['id']}"
        differing = differences(first, second, folder)
        lines += [f"{pair}: {line}" for line in differing]
        if not differing:
            fail("4", pair, "same-arms")
        elif len(differing) > 1 and not value(found["4f"], "more than one difference"):
            fail("4", pair, "many-differences", len(differing))

    # Section 5: the subject.
    subject = found["5"]
    product = value(subject, "product")
    if product and product not in HOSTS:
        fail("5", "product", "no-host", product, ", ".join(sorted(HOSTS)))
    runs, seconds = whole(value(subject, "runs for each arm")), whole(value(subject, "time limit"))
    if value(subject, "runs for each arm") and not runs:
        fail("5", "runs for each arm", "no-number")
    elif 0 < runs < MIN_RUNS and not value(subject, "fewer than five runs"):
        fail("5", "runs for each arm", "few-runs")
    if value(subject, "time limit") and not seconds:
        fail("5", "time limit", "no-number")
    if value(subject, "git repository") and value(subject, "git repository") not in ("yes", "no"):
        fail("5", "git repository", "no-yes-no")

    # Section 2: the limits. They need the arms and the number of runs.
    limits = {name: limit(value(hypothesis, name)) for name in ("confirmed when", "refuted when")}
    for name, parts in limits.items():
        if value(hypothesis, name) and parts is None:
            fail("2", name, "no-limit")
    named = {arm for parts in limits.values() for a, b, _, _ in parts or [] for arm in (a, b) if arm}
    unknown = sorted(named - {arm["id"] for arm in arms})
    if unknown:
        fail("2", "confirmed when", "unknown-arm", ", ".join(unknown))
    elif all(limits.values()) and runs:
        can_confirm, can_refute, both = reach(limits["confirmed when"], limits["refuted when"], runs)
        if not can_confirm:
            fail("2", "confirmed when", "never", "confirmed")
        if not can_refute:
            fail("2", "refuted when", "never", "refuted")
        if both:
            fail("2", "refuted when", "overlap", both)

    # Section 6: the words of the expected answer must not be in a file that the subject gets.
    words = []
    for item in found["6"] or [""]:
        if item.startswith("(none)"):
            if blank(item[6:].lstrip(": ")):
                fail("6", "(none)", "no-reason")
        elif blank(item):
            fail("6", "list", "empty")
        else:
            words.append(item.strip("`"))
    shown = {prompt for arm in sound for prompt in arm["prompts"]}
    instructions = []
    for arm in sound:
        for path in tree(folder / arm["input"] if arm["input"] else None):
            shown.add(f"{arm['input']}/{path}")
            if instruction(path):
                instructions.append(f"arm {arm['id']}: {arm['input']}/{path}")
    for path in sorted(shown):
        text = (folder / path).read_text(encoding="utf-8", errors="replace")
        for number, line in enumerate(text.splitlines(), 1):
            for word in words:
                if word.lower() in line.lower():
                    fail("6", word, "leak", path, number)

    # Section 7: one prediction for each arm and each criterion.
    predicted = {}
    for row in found["7"]:
        count = row.get("predicted count", "")
        if count.isdigit() and (not runs or int(count) <= runs):
            predicted[row.get("arm", ""), row.get("criterion", "")] = int(count)
    for arm in arms:
        for criterion in criteria:
            if (arm["id"], criterion["id"]) not in predicted:
                fail("7", f"{arm['id']}, {criterion['id']}", "no-prediction")

    plan = {
        "title": found["title"],
        "arms": arms,
        "criteria": criteria,
        "criterion": value(hypothesis, "criterion"),
        "limits": limits,
        "product": product,
        "model": value(subject, "model"),
        "tools": listed(value(subject, "tools")),
        "runs": runs,
        "limit": seconds,
        "git": value(subject, "git repository") == "yes",
        "permits": {key: listed(value(found["8"], field)) for key, field in LISTS.items()},
        "predicted": predicted,
    }
    return plan, failures, lines, sorted(instructions)


def bullets(title, items):
    """Print a title and a list. An empty list prints `(none)`.

    >>> bullets("Loaded instructions:", [])
    Loaded instructions:
    - (none)
    """
    print(title)
    for item in items or ["(none)"]:
        print(f"- {item}")


def check(folder):
    r"""The command check: print the findings. Returns the result code.

    >>> import sample
    >>> check(sample.folder())
    Differences between the arms:
    - plain and polite: prompt 1 (prompts/plain.md, prompts/polite.md): the lines 1 to 1 differ
    Loaded instructions:
    - (none)
    Result: the registration is complete.
    0
    >>> check(sample.folder(("**Model**: small-model", "**Model**:"), files={"inputs/base/AGENTS.md": "Rules.\n"}))
    FAIL 5. Subject, model: The field is empty.
    Differences between the arms:
    - plain and polite: prompt 1 (prompts/plain.md, prompts/polite.md): the lines 1 to 1 differ
    Loaded instructions:
    - arm plain: inputs/base/AGENTS.md
    - arm polite: inputs/base/AGENTS.md
    Result: 1 checks fail.
    1
    """
    _, failures, lines, instructions = examine(folder)
    for line in failures:
        print(line)
    bullets(MESSAGES["differences"], lines)
    bullets(MESSAGES["instructions"], instructions)
    print(MESSAGES["fails"].format(len(failures)) if failures else MESSAGES["complete"])
    return 1 if failures else 0


def git(folder, *args):
    """Run git in a folder. Returns (result code, output). The variables of a git hook are removed.

    >>> import tempfile
    >>> git(tempfile.mkdtemp(prefix="experiment-"), "rev-parse", "--is-inside-work-tree")[0] != 0
    True
    """
    env = {name: text for name, text in os.environ.items() if not name.startswith("GIT_")}
    identity = ["-c", "user.name=experiment", "-c", "user.email=experiment@example.invalid"]
    command = ["git", "-C", str(folder), *identity, "-c", "commit.gpgsign=false", *args]
    done = subprocess.run(command, capture_output=True, text=True, check=False, env=env)
    return done.returncode, done.stdout


def sealed_files(folder, plan):
    """The digest of each file that the seal covers: the registration, the prompts and the inputs.

    >>> import sample
    >>> folder = sample.folder()
    >>> sorted(sealed_files(folder, examine(folder)[0]))
    ['inputs/base/note.txt', 'prompts/plain.md', 'prompts/polite.md', 'registration.md']
    """
    paths = {"registration.md"}
    for arm in plan["arms"]:
        paths.update(arm["prompts"])
        paths.update(
            f"{arm['input']}/{path}" for path in tree(folder / arm["input"] if arm["input"] else None)
        )
    return {path: digest((folder / path).read_bytes()) for path in sorted(paths) if (folder / path).is_file()}


def seal(folder, today):
    r"""The command seal: write sealed.json for a complete registration. Returns the result code.

    >>> import sample
    >>> folder = sample.folder()
    >>> seal(folder, "2026-01-11")
    Sealed: 4 files, seal ..., commit (none).
    0
    >>> record = json.loads((folder / "sealed.json").read_text())
    >>> record["date"], record["commit"], sorted(record["files"]), len(record["seal"])
    ('2026-01-11', None, ['inputs/base/note.txt', 'prompts/plain.md', 'prompts/polite.md', 'registration.md'], 64)

    A registration with a failing check gets no seal. A registration with a result gets no new seal.

    >>> seal(sample.folder(("**Model**: small-model", "**Model**:")), "2026-01-11")
    FAIL 5. Subject, model: The field is empty.
    Differences between the arms:
    ...
    Result: 1 checks fail.
    1
    >>> _ = (folder / "results.jsonl").write_text("")
    >>> seal(folder, "2026-01-12")
    No seal: results.jsonl exists. A registration with a result cannot be sealed again.
    1

    In a git repository, the files must be committed. The seal records the commit.

    >>> folder = sample.folder()
    >>> _ = git(folder, "init", "-q")
    >>> seal(folder, "2026-01-11")
    No seal: commit these files first. Git shows a change:
    ?? inputs/base/
    ?? prompts/plain.md
    ?? prompts/polite.md
    ?? registration.md
    1
    >>> _ = git(folder, "add", "-A"), git(folder, "commit", "-q", "-m", "docs: register the experiment")
    >>> seal(folder, "2026-01-11")
    Sealed: 4 files, seal ..., commit ...
    0
    >>> json.loads((folder / "sealed.json").read_text())["commit"] == git(folder, "rev-parse", "HEAD")[1].strip()
    True
    """
    plan, failures, _, _ = examine(folder)
    if failures:
        return check(folder)
    if (folder / "results.jsonl").exists():
        print(MESSAGES["has-result"])
        return 1
    commit = None
    if any((above / ".git").exists() for above in (folder.resolve(), *folder.resolve().parents)):
        paths = [
            "registration.md",
            *sorted({p for arm in plan["arms"] for p in [*arm["prompts"], arm["input"]] if p}),
        ]
        changes = git(folder, "status", "--porcelain", "--ignored", "--", *paths)[1].rstrip()
        if changes:
            print(MESSAGES["not-committed"])
            print(changes)
            return 1
        commit = git(folder, "rev-parse", "HEAD")[1].strip()
    files = sealed_files(folder, plan)
    record = {
        "commit": commit,
        "date": today,
        "files": files,
        "seal": digest(json.dumps(files, sort_keys=True)),
    }
    (folder / "sealed.json").write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(MESSAGES["sealed"].format(len(files), record["seal"][:12], commit or "(none)"))
    return 0


def verify(folder):
    r"""Compare the folder with its seal. Returns (plan, record of the seal, problems).

    >>> import sample
    >>> folder = sample.folder()
    >>> verify(folder)[2]
    ['sealed.json is absent or cannot be read. Run the command seal first.']
    >>> _ = seal(folder, "2026-01-11")
    Sealed: ...
    >>> verify(folder)[2]
    []

    Each file that changed, that is new or that is absent is a problem.

    >>> _ = (folder / "prompts" / "polite.md").write_text("Write two lines to a new colleague, please.\n")
    >>> _ = (folder / "inputs" / "base" / "new.txt").write_text("new")
    >>> (folder / "inputs" / "base" / "note.txt").unlink()
    >>> verify(folder)[2]
    ['inputs/base/new.txt changed after the seal.', 'inputs/base/note.txt changed after the seal.',
     'prompts/polite.md changed after the seal.']
    >>> _ = (folder / "sealed.json").write_text("not JSON")
    >>> verify(folder)[2]
    ['sealed.json is absent or cannot be read. Run the command seal first.']
    """
    plan, failures, _, _ = examine(folder)
    try:
        record = json.loads(read(folder / "sealed.json"))
    except (Unreadable, ValueError):
        return plan, None, [MESSAGES["no-seal"]]
    now, then = sealed_files(folder, plan), record["files"]
    changed = sorted(path for path in set(now) | set(then) if now.get(path) != then.get(path))
    return plan, record, [MESSAGES["changed"].format(path) for path in changed] + failures


def unsafe(work):
    r"""The reason why a folder is not a work folder, or "".

    The run folders are in the work folder. An agent product loads the instruction files of each
    folder above its folder. Thus the work folder is outside each git repository, and no folder
    above it holds an instruction file for agents.

    >>> import tempfile
    >>> base = pathlib.Path(tempfile.mkdtemp(prefix="experiment-")).resolve()
    >>> unsafe(base / "work")
    ''
    >>> _ = (base / "AGENTS.md").write_text("Rules.\n")
    >>> unsafe(base / "work")
    'An agent in the work folder loads ...AGENTS.md. Use a different work folder.'
    >>> (base / "repo" / ".git").mkdir(parents=True)
    >>> unsafe(base / "repo" / "work")
    '...repo is in a git repository. Use a work folder outside each repository.'
    """
    work = pathlib.Path(work).resolve()
    for above in (work, *work.parents):
        if (above / ".git").exists():
            return MESSAGES["in-repository"].format(above)
        loaded = [name for name in (*INSTRUCTION_FILES, *INSTRUCTION_FOLDERS) if (above / name).exists()]
        if loaded:
            return MESSAGES["instructions-above"].format(above / loaded[0])
    return ""


def names(entries):
    """The names of a list of the start event, sorted. An entry is a name or a record with a name.

    >>> names([{"name": "b", "path": "builtin"}, "a"]), names(None)
    (['a', 'b'], [])
    """
    return sorted(entry["name"] if isinstance(entry, dict) else str(entry) for entry in entries or [])


def claude_events(stream):
    r"""Read the stream of one session of the product `claude`: (start event, final text).

    The start event becomes a small record. A part that is absent is None.

    >>> import sample
    >>> init, final = claude_events(sample.agent(init={"memory_paths": {"auto": "/m"}})(["", "", "Say it, please."], cwd=".").stdout)
    >>> final, init["version"], init["plugins"], init["agents"], init["memory"]
    ('Hello and welcome.', '0.0.0', ['cc-plugin-telemetry'], ['Plan', 'claude'], ['/m'])
    >>> claude_events('not JSON\n3\n{"type": "result", "is_error": true, "result": "Not logged in"}\n')
    (None, None)
    >>> claude_events('{"type": "result", "result": null}\n')
    (None, '')
    """
    init, final = None, None
    for line in stream.splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if not isinstance(event, dict):
            continue
        if event.get("type") == "system" and event.get("subtype") == "init" and init is None:
            init = {key: names(event.get(key)) for key in ("tools", *LISTS)}
            init["version"], init["model"] = event.get("claude_code_version"), event.get("model")
            init["memory"] = sorted(str(path) for path in (event.get("memory_paths") or {}).values())
        elif event.get("type") == "result" and not event.get("is_error"):
            final = event.get("result") or ""
    return init, final


# The agent products that the program can start. To add a product, add one entry.
#   options        the options of each session
#   no ...         the options that switch a part off when section 8 permits no name for it
#   environment    the variables of each session
#   always         the names that the product itself has in each session (version 2.1.296 of
#                  `claude`, found on 2026-10-10 with real sessions)
#   read           the function that reads the stream of a session
HOSTS = {
    "claude": {
        "program": "claude",
        "options": [
            "--setting-sources",
            "project",
            "--no-session-persistence",
            "--output-format",
            "stream-json",
            "--verbose",
        ],
        "no mcp_servers": ["--strict-mcp-config"],
        "no skills": ["--disable-slash-commands"],
        "environment": {"CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1"},
        "always": {
            "plugins": ["cc-plugin-agents-md", "cc-plugin-plugin-authoring", "cc-plugin-telemetry"],
            "mcp_servers": [],
            "skills": [
                "batch",
                "claude-api",
                "code-review",
                "dataviz",
                "debug",
                "deep-research",
                "design",
                "design-sync",
                "doctor",
                "fewer-permission-prompts",
                "loop",
                "plugin-authoring",
                "run",
                "run-skill-generator",
                "schedule",
                "simplify",
                "update-config",
                "verify",
                "workflow-authoring",
            ],
            "agents": ["Explore", "Plan", "claude", "general-purpose", "statusline-setup"],
        },
        "read": claude_events,
    }
}


def command(plan, prompt):
    """The command that starts one session of the product, with the options of the clean environment.

    >>> import sample
    >>> plan = examine(sample.folder())[0]
    >>> command(plan, "Say OK")
    ['claude', '-p', 'Say OK', '--model', 'small-model', '--tools', 'Read,Write', '--allowedTools', 'Read,Write',
     '--setting-sources', 'project', '--no-session-persistence', '--output-format', 'stream-json', '--verbose',
     '--strict-mcp-config', '--disable-slash-commands']

    Without tools, the product gets an empty list. A part that section 8 permits is not switched off.

    >>> plan["tools"], plan["permits"]["skills"], plan["permits"]["mcp_servers"] = [], ["own"], ["own"]
    >>> command(plan, "Say OK")
    ['claude', '-p', 'Say OK', '--model', 'small-model', '--tools', '', '--setting-sources', 'project',
     '--no-session-persistence', '--output-format', 'stream-json', '--verbose']
    """
    host, tools = HOSTS[plan["product"]], ",".join(plan["tools"])
    off = [
        option
        for key in ("mcp_servers", "skills")
        if not plan["permits"][key]
        for option in host[f"no {key}"]
    ]
    permitted = ["--allowedTools", tools] if tools else []
    return [
        host["program"],
        "-p",
        prompt,
        "--model",
        plan["model"],
        "--tools",
        tools,
        *permitted,
        *host["options"],
        *off,
    ]


def unclean(init, plan):
    """The reason why the environment of a session is not clean, or "".

    The start event must name nothing beyond the names of the product itself and of section 8.

    >>> import sample
    >>> plan = examine(sample.folder(("- **Agents**: (none)", "- **Agents**: own-agent")))[0]
    >>> init = {"plugins": ["cc-plugin-telemetry"], "mcp_servers": [], "skills": [], "agents": ["Plan", "own-agent"], "memory": []}
    >>> unclean(init, plan)
    ''
    >>> unclean({**init, "plugins": ["finance"], "mcp_servers": ["mail"], "memory": ["/m"]}, plan)
    'the environment is not clean: plugins: finance; mcp_servers: mail; memory: /m'
    """
    always, permits = HOSTS[plan["product"]]["always"], plan["permits"]
    extra = [
        f"{key}: {name}" for key in LISTS for name in init[key] if name not in always[key] + permits[key]
    ]
    extra += [f"memory: {path}" for path in init["memory"]]
    return MESSAGES["not-clean"].format("; ".join(extra)) if extra else ""


def session(plan, prompt, folder, run=subprocess.run):
    r"""Start one session in a run folder. Returns the reason if it broke, the final text, the start
    event and the stream.

    The function `run` is subprocess.run. An example gives a different function.

    >>> import sample
    >>> plan = examine(sample.folder())[0]
    >>> done = session(plan, "Say it, please.", ".", run=sample.agent())
    >>> done["reason"], done["final"], done["init"]["model"], len(done["stream"].splitlines())
    ('', 'Hello and welcome.', 'small-model', 2)

    The session gets no input, the time limit of the registration and the variables of the host.

    >>> def show(command, **options):
    ...     print(options["timeout"], options["stdin"] == subprocess.DEVNULL, options["env"]["CLAUDE_CODE_DISABLE_AUTO_MEMORY"])
    ...     return sample.agent()(command, **options)
    >>> _ = session(plan, "Say OK", ".", run=show)
    60 True 1

    Each session that broke gives its reason.

    >>> def reason(run):
    ...     return session(plan, "Say OK", ".", run=run)["reason"]
    >>> reason(sample.agent(code=1)), reason(sample.agent(init={"subtype": "other"}))
    ('the product ended with the result code 1', 'the stream has no start event')
    >>> reason(sample.agent(reply=lambda prompt, folder: None))
    'the stream has no result'
    >>> def slow(command, **options):
    ...     raise subprocess.TimeoutExpired(command, 60)
    >>> def absent(command, **options):
    ...     raise FileNotFoundError("claude")
    >>> reason(slow), reason(absent)
    ('the session did not end in 60 seconds', 'the product did not start: claude')
    """
    host = HOSTS[plan["product"]]
    done = {"reason": "", "final": "", "init": None, "stream": ""}
    try:
        ended = run(
            command(plan, prompt),
            capture_output=True,
            text=True,
            timeout=plan["limit"],
            cwd=str(folder),
            stdin=subprocess.DEVNULL,
            env={**os.environ, **host["environment"]},
            check=False,
        )
    except subprocess.TimeoutExpired:
        return {**done, "reason": MESSAGES["time-limit"].format(plan["limit"])}
    except OSError as e:
        return {**done, "reason": MESSAGES["no-start"].format(e)}
    init, final = host["read"](ended.stdout)
    if ended.returncode:
        done["reason"] = MESSAGES["result-code"].format(ended.returncode)
    elif init is None:
        done["reason"] = MESSAGES["no-init"]
    elif final is None:
        done["reason"] = MESSAGES["no-result"]
    return {**done, "final": final or "", "init": init, "stream": ended.stdout}


def attempt(plan, folder, work, seal_id, job, run=subprocess.run):
    r"""Do one run: build the run folder, start one session for each prompt, and return the row.

    A job is (arm, run number, number of the attempt). The name of the run folder is a code: it
    does not show the arm to the subject.

    >>> import sample, tempfile
    >>> folder = sample.folder(("**Git repository**: no", "**Git repository**: yes"),
    ...     ("| prompts/polite.md |", "| prompts/polite.md, prompts/plain.md |"))
    >>> plan, work = examine(folder)[0], pathlib.Path(tempfile.mkdtemp(prefix="experiment-"))
    >>> def note(prompt, run_folder):
    ...     _ = (run_folder / "note.txt").write_text("Written in 2026.\n")
    ...     return sample.greeting(prompt, run_folder)
    >>> row = attempt(plan, folder, work, "seal", (plan["arms"][1], 2, 1), run=sample.agent(reply=note))
    >>> row["arm"], row["run"], row["attempt"], row["valid"], row["reason"], row["finals"]
    ('polite', 2, 1, True, '', ['Hello and welcome.', 'Welcome.'])
    >>> row["folder"], row["transcripts"], row["files"]
    ('runs/...', ['transcripts/...-1.jsonl', 'transcripts/...-2.jsonl'], {'note.txt': 'Written in 2026.\n'})
    >>> row["environment"][0]["plugins"], len(row["environment"]), "polite" in row["folder"]
    (['cc-plugin-telemetry'], 2, False)
    >>> len((work / row["transcripts"][1]).read_text().splitlines())
    2

    The run folder is a copy of the input folder. With `Git repository: yes` it is a repository
    with one commit.

    >>> sorted(p.name for p in (work / row["folder"]).iterdir()), git(work / row["folder"], "log", "--oneline")[1]
    (['.git', 'note.txt'], '... input\n')

    A session that broke or that was not clean ends the run. The row is not valid and gives the reason.

    >>> empty = {**plan["arms"][1], "input": None}
    >>> row = attempt({**plan, "git": False}, folder, work, "seal", (empty, 2, 1), run=sample.agent(init={"skills": ["own"]}))
    >>> row["valid"], row["reason"], row["finals"], row["files"], row["attempt"]
    (False, 'session 1: the environment is not clean: skills: own', ['Hello and welcome.'], {'note.txt': None}, 2)
    >>> attempt(plan, folder, work, "seal", (empty, 3, 1), run=sample.agent(code=2))["reason"]
    'session 1: the product ended with the result code 2'
    """
    arm, number, tries = job
    code = digest(f"{seal_id}:{arm['id']}:{number}:{tries}")[:12]
    while (work / "runs" / code).exists():
        tries += 1
        code = digest(f"{seal_id}:{arm['id']}:{number}:{tries}")[:12]
    target = work / "runs" / code
    (work / "transcripts").mkdir(parents=True, exist_ok=True)
    if arm["input"]:
        shutil.copytree(folder / arm["input"], target)
    else:
        target.mkdir(parents=True)
    if plan["git"]:
        git(target, "init", "-q")
        git(target, "add", "-A")
        git(target, "commit", "-q", "--allow-empty", "-m", "input")
    row = {"arm": arm["id"], "run": number, "attempt": tries, "folder": f"runs/{code}", "reason": ""}
    row.update({"finals": [], "transcripts": [], "environment": []})
    for at, prompt in enumerate(arm["prompts"], 1):
        done = session(plan, read(folder / prompt), target, run=run)
        (work / "transcripts" / f"{code}-{at}.jsonl").write_text(done["stream"], encoding="utf-8")
        row["finals"].append(done["final"])
        row["transcripts"].append(f"transcripts/{code}-{at}.jsonl")
        row["environment"].append(done["init"])
        reason = done["reason"] or unclean(done["init"], plan)
        if reason:
            row["reason"] = f"session {at}: {reason}"
            break
    row["valid"] = not row["reason"]
    row["files"] = {}
    for name in sorted({c["where"][5:] for c in plan["criteria"] if c["where"] != "final"}):
        path = target / name
        row["files"][name] = (
            path.read_text(encoding="utf-8", errors="replace")[:MAX_FILE] if path.is_file() else None
        )
    return row


def results(folder):
    r"""The rows of results.jsonl. No file gives no row.

    >>> import sample
    >>> folder = sample.folder(files={"results.jsonl": '{"arm": "plain"}\n\n{"arm": "polite"}\n'})
    >>> results(folder), results(sample.folder())
    ([{'arm': 'plain'}, {'arm': 'polite'}], [])
    >>> results(sample.folder(files={"results.jsonl": "{broken\n"}))
    Traceback (most recent call last):
        ...
    Unreadable: ...results.jsonl: a line is not JSON
    """
    path = folder / "results.jsonl"
    try:
        return [json.loads(line) for line in read(path).splitlines() if line.strip()] if path.exists() else []
    except ValueError as e:
        raise Unreadable(f"{path}: a line is not JSON") from e


def valid_rows(plan, rows):
    """The valid row of each arm and run number: {(arm, run): row}, and the number that is registered.

    >>> rows = [{"arm": "A", "run": 1, "valid": False}, {"arm": "A", "run": 1, "valid": True, "x": 1}]
    >>> valid_rows({"arms": [{"id": "A"}, {"id": "B"}], "runs": 5}, rows)
    ({('A', 1): {'arm': 'A', 'run': 1, 'valid': True, 'x': 1}}, 10)
    """
    return {(row["arm"], row["run"]): row for row in rows if row["valid"]}, len(plan["arms"]) * plan["runs"]


def refused(problems):
    """Print why a command does not start. Returns True if there is a problem.

    >>> refused([]), refused(["", ""])
    (False, False)
    >>> refused(["", "prompts/a.md changed after the seal."])
    Refused:
    prompts/a.md changed after the seal.
    True
    """
    problems = [problem for problem in problems if problem]
    if problems:
        print(MESSAGES["refused"])
        print("\n".join(problems))
    return bool(problems)


def run_command(folder, work, run=subprocess.run):
    r"""The command run: do each run that has no valid row. Returns the result code.

    >>> import sample, tempfile
    >>> folder, work = sample.folder(), pathlib.Path(tempfile.mkdtemp(prefix="experiment-")) / "work"
    >>> run_command(folder, work, run=sample.agent())
    Refused:
    sealed.json is absent or cannot be read. Run the command seal first.
    1
    >>> _ = seal(folder, "2026-01-11")
    Sealed: ...

    A session that was not clean gives a row that is not valid. The run is done again by the next call.

    >>> def first_fails(prompt, run_folder):
    ...     return None if run_folder.name == (work / "runs" / digest(f"{seal_id}:plain:2:1")[:12]).name else sample.greeting(prompt, run_folder)
    >>> seal_id = json.loads((folder / "sealed.json").read_text())["seal"]
    >>> run_command(folder, work, run=sample.agent(reply=first_fails))
    arm plain, run 1: valid
    arm plain, run 2: not valid: session 1: the stream has no result
    arm plain, run 3: valid
    ...
    arm polite, run 5: valid
    Runs remain: 9 of 10 are valid. Run the command run again.
    1
    >>> run_command(folder, work, run=sample.agent())
    arm plain, run 2: valid
    Valid runs: 10 of 10. The transcripts are in ...work.
    0
    >>> rows = results(folder)
    >>> len(rows), [(row["arm"], row["run"], row["attempt"]) for row in rows if row["arm"] == "plain"][:3], rows[-1]["attempt"]
    (11, [('plain', 1, 1), ('plain', 2, 1), ('plain', 3, 1)], 2)

    The program never does more than the registered number of runs.

    >>> run_command(folder, work, run=None)
    Valid runs: 10 of 10. The transcripts are in ...work.
    0

    A change after the seal, and a work folder in a git repository, stop the command.

    >>> (work / ".git").mkdir()
    >>> run_command(folder, work, run=None)
    Refused:
    ...work is in a git repository. Use a work folder outside each repository.
    1
    >>> _ = (folder / "prompts" / "plain.md").write_text("Write two lines.\n")
    >>> run_command(folder, work.parent / "second", run=None)
    Refused:
    prompts/plain.md changed after the seal.
    1
    """
    plan, record, problems = verify(folder)
    if refused([*problems, unsafe(work)]):
        return 1
    rows = results(folder)
    valid, registered = valid_rows(plan, rows)
    tries = [(row["arm"], row["run"]) for row in rows]
    jobs = [
        (arm, number, tries.count((arm["id"], number)) + 1)
        for arm in plan["arms"]
        for number in range(1, plan["runs"] + 1)
        if (arm["id"], number) not in valid
    ]
    count = len(valid)
    with (
        concurrent.futures.ThreadPoolExecutor(POOL) as pool,
        open(folder / "results.jsonl", "a", encoding="utf-8") as out,
    ):
        for row in pool.map(
            lambda job: attempt(plan, folder, pathlib.Path(work), record["seal"], job, run), jobs
        ):
            out.write(json.dumps(row, sort_keys=True) + "\n")
            out.flush()
            count += row["valid"]
            key = "run-valid" if row["valid"] else "run-not-valid"
            print(MESSAGES[key].format(row["arm"], row["run"], row["reason"]))
    if count < registered:
        print(MESSAGES["runs-remain"].format(count, registered))
        return 1
    print(MESSAGES["runs"].format(count, registered, pathlib.Path(work).resolve()))
    return 0


def packet(seal_id, arm, number):
    """The code of the packet of one run. It does not show the arm.

    >>> packet("seal", "plain", 1), packet("seal", "polite", 1)
    ('P-d024990b2d', 'P-0d881432b0')
    """
    return "P-" + digest(f"{seal_id}:packet:{arm}:{number}")[:10]


def blind(folder, work):
    r"""The command blind: write the packets for the judge. Returns the result code.

    >>> import sample, tempfile
    >>> folder, work = sample.folder(), pathlib.Path(tempfile.mkdtemp(prefix="experiment-")) / "work"
    >>> _ = seal(folder, "2026-01-11")
    Sealed: ...
    >>> blind(folder, work)
    Runs remain: 0 of 10 are valid. Run the command run again.
    1
    >>> _ = run_command(folder, work, run=sample.agent())
    arm plain, run 1: valid
    ...
    >>> blind(folder, work)
    Packets: 10 in ...packets. Give only this folder to the judge.
    0

    A packet holds the final texts, the files that a criterion of the judge names, and the criteria.

    >>> key = json.loads((folder / "blind-key.json").read_text())
    >>> code = packet(json.loads((folder / "sealed.json").read_text())["seal"], "polite", 3)
    >>> len(key), key[code], sorted(p.relative_to(work / "packets" / code).as_posix() for p in (work / "packets" / code).rglob("*"))
    (10, {'arm': 'polite', 'run': 3}, ['criteria.md', 'files', 'files/note.txt', 'final-1.md'])
    >>> print((work / "packets" / code / "criteria.md").read_text())
    # Criteria
    <BLANKLINE>
    | Criterion | Question | Where |
    |---|---|---|
    | C-2 | Is the answer friendly? | final |
    | C-3 | Does the note hold a year? | file:note.txt |
    <BLANKLINE>
    >>> (work / "packets" / code / "final-1.md").read_text()
    'Hello and welcome.'

    The task of the judge is in the folder of the packets.

    >>> (work / "packets" / "judge-task.md").read_text() == JUDGE_TASK.read_text()
    True

    A second call writes the same packets. A file that a run did not write is not in its packet.

    >>> (folder / "results.jsonl").write_text((folder / "results.jsonl").read_text().replace('"A note for the colleague.\\n"', "null")) > 0
    True
    >>> blind(folder, work), (work / "packets" / code / "files").exists()
    Packets: 10 in ...packets. Give only this folder to the judge.
    (0, False)

    An experiment without a criterion of the judge needs no packet.

    >>> folder = sample.folder(("| judge |", "| program | `friend` |"))
    >>> _ = seal(folder, "2026-01-11"), run_command(folder, work.parent / "two", run=sample.agent())
    Sealed: ...
    >>> blind(folder, work.parent / "two"), (folder / "blind-key.json").exists()
    No criterion has the judge. No packet is necessary.
    (0, False)
    >>> _ = (folder / "CLAUDE.md").write_text("Rules.\n")
    >>> blind(folder, folder / "work")
    Refused:
    An agent in the work folder loads ...CLAUDE.md. Use a different work folder.
    1
    """
    plan, record, problems = verify(folder)
    work = pathlib.Path(work)
    if refused([*problems, unsafe(work)]):
        return 1
    valid, registered = valid_rows(plan, results(folder))
    if len(valid) < registered:
        print(MESSAGES["runs-remain"].format(len(valid), registered))
        return 1
    judged = [c for c in plan["criteria"] if c["by"] == "judge"]
    if not judged:
        print(MESSAGES["no-judge"])
        return 0
    shutil.rmtree(work / "packets", ignore_errors=True)
    criteria = ["# Criteria", "", "| Criterion | Question | Where |", "|---|---|---|"]
    criteria += [f"| {c['id']} | {c['question']} | {c['where']} |" for c in judged]
    key = {}
    for (arm, number), row in sorted(valid.items()):
        code = packet(record["seal"], arm, number)
        key[code] = {"arm": arm, "run": number}
        target = work / "packets" / code
        target.mkdir(parents=True)
        (target / "criteria.md").write_text("\n".join(criteria) + "\n", encoding="utf-8")
        for at, text in enumerate(row["finals"], 1):
            (target / f"final-{at}.md").write_text(text, encoding="utf-8")
        for name in sorted({c["where"][5:] for c in judged if c["where"] != "final"}):
            if row["files"][name] is not None:
                (target / "files" / name).parent.mkdir(parents=True, exist_ok=True)
                (target / "files" / name).write_text(row["files"][name], encoding="utf-8")
    # The task of the judge goes with the packets: the judge needs no other folder.
    (work / "packets" / "judge-task.md").write_text(JUDGE_TASK.read_text(encoding="utf-8"), encoding="utf-8")
    (folder / "blind-key.json").write_text(json.dumps(key, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(MESSAGES["packets"].format(len(key), (work / "packets").resolve()))
    return 0


def interval(hits, runs):
    """The Wilson interval of 95 percent for a share, in percent.

    >>> interval(0, 30), interval(15, 30), interval(5, 5), interval(0, 0)
    ((0, 11), (33, 67), (57, 100), (0, 100))
    """
    if not runs:
        return (0, 100)
    z, p = 1.96, hits / runs
    centre = (p + z * z / (2 * runs)) / (1 + z * z / runs)
    half = z * ((p * (1 - p) / runs + z * z / (4 * runs * runs)) ** 0.5) / (1 + z * z / runs)
    return (round(100 * max(0, centre - half)), round(100 * min(1, centre + half)))


def fisher(a, b, c, d):
    """The exact test of Fisher, two sides, for the table [[a, b], [c, d]].

    >>> round(fisher(12, 0, 0, 12), 7), round(fisher(5, 0, 0, 5), 4), fisher(2, 3, 2, 3), fisher(0, 0, 0, 0)
    (7e-07, 0.0079, 1.0, 1.0)
    """
    n, r1, c1 = a + b + c + d, a + b, a + c

    def p(x):
        return math.comb(c1, x) * math.comb(n - c1, r1 - x) / math.comb(n, r1)

    p0 = p(a)
    return min(
        1.0, sum(p(x) for x in range(max(0, r1 - (n - c1)), min(r1, c1) + 1) if p(x) <= p0 * (1 + 1e-9))
    )


def judgements(folder, codes, judged):
    r"""Read judgements.md. Returns (answers, problems).

    An answer is {(code, criterion): True or False}. A problem is (criterion or "", text).

    >>> import sample
    >>> folder = sample.folder(files={"judgements.md": '''| Code | Criterion | Answer | Evidence |
    ... |---|---|---|---|
    ... | P-1 | C-2 | yes | final-1.md line 1 |
    ... | `P-2` | `C-2` | NO | final-1.md line 2 |
    ... | P-1 | C-2 | no | final-1.md line 1 |
    ... | P-2 | C-3 | perhaps | final-1.md line 1 |
    ... | P-1 | C-3 | yes | |
    ... | P-9 | C-2 | yes | final-1.md line 1 |
    ... | P-1 | C-1 | yes | final-1.md line 1 |
    ... '''})
    >>> answers, problems = judgements(folder, ["P-1", "P-2"], ["C-2", "C-3"])
    >>> answers
    {('P-1', 'C-2'): True, ('P-2', 'C-2'): False}
    >>> for problem in problems:
    ...     print(problem)
    ('C-2', 'judgements.md line 5: there is a second answer for P-1, C-2.')
    ('C-3', 'judgements.md line 6: the answer is not `yes` or `no`, or the evidence is empty.')
    ('C-3', 'judgements.md line 7: the answer is not `yes` or `no`, or the evidence is empty.')
    ('', 'judgements.md line 8: the code or the criterion is not known.')
    ('', 'judgements.md line 9: the code or the criterion is not known.')
    ('C-3', 'judgements.md has no answer for P-1, C-3.')
    ('C-3', 'judgements.md has no answer for P-2, C-3.')
    >>> judgements(sample.folder(), ["P-1"], ["C-2"])
    ({}, [('C-2', 'judgements.md has no answer for P-1, C-2.')])
    """
    path = folder / "judgements.md"
    rows = table(list(enumerate(read(path).splitlines(), 1))) if path.exists() else []
    answers, problems = {}, []
    for row in rows:
        code, criterion = row.get("code", "").strip("`"), row.get("criterion", "").strip("`")
        answer = row.get("answer", "").strip("`").lower()
        if code not in codes or criterion not in judged:
            problems.append(("", MESSAGES["judgement-unknown"].format(row["_line"])))
        elif answer not in ("yes", "no") or not row.get("evidence", ""):
            problems.append((criterion, MESSAGES["judgement-wrong"].format(row["_line"])))
        elif (code, criterion) in answers:
            problems.append((criterion, MESSAGES["judgement-twice"].format(row["_line"], code, criterion)))
        else:
            answers[code, criterion] = answer == "yes"
    for code in codes:
        for criterion in judged:
            if (code, criterion) not in answers:
                problems.append((criterion, MESSAGES["judgement-missing"].format(code, criterion)))
    return answers, problems


def answer(criterion, row):
    r"""The answer of the program for one criterion and one run: the pattern is in the text, or not.

    `final` is the final text of the last session. A file that the run did not write gives no.

    >>> row = {"finals": ["Hello", "Bye"], "files": {"note.txt": "In 2026.\n", "b.txt": None}}
    >>> [answer({"pattern": p, "where": w}, row) for p, w in (("Bye", "final"), ("Hello", "final"),
    ...     (r"\d{4}", "file:note.txt"), ("a", "file:b.txt"))]
    [True, False, True, False]
    """
    text = row["finals"][-1] if criterion["where"] == "final" else row["files"][criterion["where"][5:]]
    return text is not None and re.search(criterion["pattern"], text) is not None


def score(folder):
    r"""The command score: count the answers and write result.md. Returns the result code.

    >>> import sample, tempfile
    >>> folder, work = sample.folder(), pathlib.Path(tempfile.mkdtemp(prefix="experiment-")) / "work"
    >>> score(folder)
    Refused:
    sealed.json is absent or cannot be read. Run the command seal first.
    1
    >>> _ = seal(folder, "2026-01-11")
    Sealed: ...

    While runs or answers of the judge remain, there is no verdict.

    >>> def third_fails(prompt, run_folder):
    ...     return None if run_folder.name == digest(f"{seal_id}:polite:3:1")[:12] else sample.greeting(prompt, run_folder)
    >>> seal_id = json.loads((folder / "sealed.json").read_text())["seal"]
    >>> _ = run_command(folder, work, run=sample.agent(reply=third_fails))
    arm plain, run 1: valid
    ...
    >>> score(folder)
    # Result of the experiment: a polite prompt
    <BLANKLINE>
    - Registration: seal ..., sealed on 2026-01-11, commit (none)
    - Valid runs: 9 of 10
    <BLANKLINE>
    ## Counts
    <BLANKLINE>
    | Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
    |---|---|---|---|---|---|---|
    | C-1 | plain | 0 | 5 | 0 % | 0 % to 43 % | 1 |
    | C-1 | polite | 4 | 4 | 100 % | 51 % to 100 % | 4 |
    | C-2 | plain | remains | 5 | - | - | 4 |
    | C-2 | polite | remains | 4 | - | - | 5 |
    | C-3 | plain | remains | 5 | - | - | 0 |
    | C-3 | polite | remains | 4 | - | - | 0 |
    | C-4 | plain | 0 | 5 | 0 % | 0 % to 43 % | 0 |
    | C-4 | polite | 0 | 4 | 0 % | 0 % to 49 % | 0 |
    <BLANKLINE>
    ## Comparison of the arms
    <BLANKLINE>
    | Criterion | Arms | Exact test of Fisher, two sides |
    |---|---|---|
    | C-1 | plain, polite | p = 0.0079 |
    | C-2 | plain, polite | remains |
    | C-3 | plain, polite | remains |
    | C-4 | plain, polite | p = 1.0000 |
    <BLANKLINE>
    ## Verdict
    <BLANKLINE>
    - Hypothesis: With the word please, more answers hold a greeting.
    - Criterion: C-1
    - Confirmed when: `polite - plain >= 3`
    - Refuted when: `polite - plain <= 0`
    - Counts: plain = 0, polite = 4
    - Verdict: none: runs or answers remain
    <BLANKLINE>
    ## What remains
    <BLANKLINE>
    - Runs remain: 9 of 10 are valid. Run the command run again.
    - judgements.md has no answer for P-..., C-2.
    ...
    <BLANKLINE>
    ## Runs that were not valid
    <BLANKLINE>
    | Arm | Run | Attempt | Reason |
    |---|---|---|---|
    | polite | 3 | 1 | session 1: the stream has no result |
    <BLANKLINE>
    ## Explanations after the fact
    <BLANKLINE>
    Each explanation written here is a guess. No next step rests on it.
    <BLANKLINE>
    Written: ...result.md
    1

    With each run and each answer, the verdict comes from the registered limits and from no other rule.

    >>> def verdict(reply, friendly=lambda arm, criterion: "yes"):
    ...     folder = sample.folder()
    ...     work = pathlib.Path(tempfile.mkdtemp(prefix="experiment-")) / "work"
    ...     with contextlib.redirect_stdout(io.StringIO()) as out:
    ...         codes = [seal(folder, "2026-01-11"), run_command(folder, work, run=sample.agent(reply=reply)), blind(folder, work)]
    ...         sample.judge(folder, friendly)
    ...         codes.append(score(folder))
    ...     return codes, [line for line in out.getvalue().splitlines() if line.startswith(("- Verdict", "| C-2"))]
    >>> import contextlib, io
    >>> verdict(sample.greeting)
    ([0, 0, 0, 0], ['| C-2 | plain | 5 | 5 | 100 % | 57 % to 100 % | 4 |', '| C-2 | polite | 5 | 5 | 100 % | 57 % to 100 % | 5 |',
      '| C-2 | plain, polite | p = 1.0000 |', '- Verdict: confirmed'])
    >>> verdict(lambda prompt, folder: "Hello.", lambda arm, criterion: "no" if arm == "plain" else "yes")[1][2:]
    ['| C-2 | plain, polite | p = 0.0079 |', '- Verdict: refuted']
    >>> some = lambda prompt, folder: "Hello." if "please" in prompt and int(folder.name, 16) % 2 else "Welcome."
    >>> verdict(some)[1][3:]
    ['- Verdict: not decided']

    A text below the last heading of result.md stays when the command runs again.

    >>> folder = sample.folder(("| judge |", "| program | `friend` |"), ("- **Skills**: (none)", "- **Skills**: own"))
    >>> with contextlib.redirect_stdout(io.StringIO()):
    ...     _ = seal(folder, "2026-01-11"), run_command(folder, work.parent / "two", run=sample.agent()), score(folder)
    >>> with open(folder / "result.md", "a") as out:
    ...     _ = out.write("\nA guess: the word please is seen as a greeting.\n")
    >>> with contextlib.redirect_stdout(io.StringIO()) as out:
    ...     _ = score(folder)
    >>> print(out.getvalue())
    # Result of the experiment: a polite prompt
    ...
    ## Runs that were not valid
    <BLANKLINE>
    (none)
    <BLANKLINE>
    ## Explanations after the fact
    <BLANKLINE>
    Each explanation written here is a guess. No next step rests on it.
    <BLANKLINE>
    A guess: the word please is seen as a greeting.
    <BLANKLINE>
    Written: ...result.md
    <BLANKLINE>
    """
    plan, record, problems = verify(folder)
    if refused(problems):
        return 1
    rows = results(folder)
    valid, registered = valid_rows(plan, rows)
    arms = [arm["id"] for arm in plan["arms"]]
    judged = [c["id"] for c in plan["criteria"] if c["by"] == "judge"]
    codes = {packet(record["seal"], arm, number): (arm, number) for arm, number in sorted(valid)}
    given, wrong = judgements(folder, sorted(codes), judged) if judged else ({}, [])
    remains = [] if len(valid) == registered else [MESSAGES["runs-remain"].format(len(valid), registered)]
    remains += [text for _, text in wrong]
    answers = {(codes[code], criterion): yes for (code, criterion), yes in given.items()}
    for criterion in plan["criteria"]:
        if criterion["by"] == "program":
            answers.update({(key, criterion["id"]): answer(criterion, row) for key, row in valid.items()})
    open_criteria = {criterion for criterion, _ in wrong}
    size = {arm: sum(1 for key in valid if key[0] == arm) for arm in arms}
    hits = {
        (arm, c["id"]): sum(answers.get((key, c["id"]), False) for key in valid if key[0] == arm)
        for arm in arms
        for c in plan["criteria"]
    }

    out = [f"# Result of the experiment: {plan['title']}", ""]
    commit = record["commit"] or "(none)"
    out += [f"- Registration: seal {record['seal'][:12]}, sealed on {record['date']}, commit {commit}"]
    out += [f"- Valid runs: {len(valid)} of {registered}", "", "## Counts", ""]
    out += [
        "| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |",
        "|---|---|---|---|---|---|---|",
    ]
    for criterion in plan["criteria"]:
        for arm in arms:
            k, n = hits[arm, criterion["id"]], size[arm]
            cells = ["remains", n, "-", "-"]
            if criterion["id"] not in open_criteria:
                low, high = interval(k, n)
                cells = [k, n, f"{round(100 * k / n) if n else 0} %", f"{low} % to {high} %"]
            row = [criterion["id"], arm, *cells, plan["predicted"][arm, criterion["id"]]]
            out.append("| " + " | ".join(str(cell) for cell in row) + " |")
    out += ["", "## Comparison of the arms", ""]
    out += ["| Criterion | Arms | Exact test of Fisher, two sides |", "|---|---|---|"]
    for criterion in plan["criteria"]:
        for a, b in itertools.combinations(arms, 2):
            ka, kb = hits[a, criterion["id"]], hits[b, criterion["id"]]
            p = f"p = {fisher(ka, size[a] - ka, kb, size[b] - kb):.4f}"
            out.append(
                f"| {criterion['id']} | {a}, {b} | {'remains' if criterion['id'] in open_criteria else p} |"
            )
    counts = {arm: hits[arm, plan["criterion"]] for arm in arms}
    verdict = MESSAGES["verdict-none"]
    if len(valid) == registered and plan["criterion"] not in open_criteria:
        confirmed, refuted = (
            holds(plan["limits"][name], counts) for name in ("confirmed when", "refuted when")
        )
        verdict = "confirmed" if confirmed else "refuted" if refuted else "not decided"
    found = load(folder)["2"]
    out += [
        "",
        "## Verdict",
        "",
        f"- Hypothesis: {value(found, 'statement')}",
        f"- Criterion: {plan['criterion']}",
    ]
    out += [
        f"- Confirmed when: `{value(found, 'confirmed when')}`",
        f"- Refuted when: `{value(found, 'refuted when')}`",
    ]
    out += ["- Counts: " + ", ".join(f"{arm} = {counts[arm]}" for arm in arms), f"- Verdict: {verdict}"]
    if remains:
        out += ["", "## What remains", "", *(f"- {text}" for text in remains)]
    out += ["", "## Runs that were not valid", ""]
    broken = [row for row in rows if not row["valid"]]
    if broken:
        out += ["| Arm | Run | Attempt | Reason |", "|---|---|---|---|"]
        out += [f"| {row['arm']} | {row['run']} | {row['attempt']} | {row['reason']} |" for row in broken]
    else:
        out.append("(none)")
    tail = f"## Explanations after the fact\n\n{MESSAGES['guess']}\n"
    path = folder / "result.md"
    kept = read(path).split(tail, 1)[-1] if path.exists() and tail in read(path) else ""
    text = "\n".join(out) + "\n\n" + tail + kept
    path.write_text(text, encoding="utf-8")
    print(text)
    print(MESSAGES["written"].format(path))
    return 1 if remains else 0


OPTIONS = {"check": (), "seal": ("--today",), "run": ("--work",), "blind": ("--work",), "score": ()}


def arguments(args):
    """Read the arguments: (command, folder, options), or None if they are wrong.

    >>> arguments(["seal", "dir", "--today", "2026-10-10"])
    ('seal', PosixPath('dir'), {'--today': '2026-10-10'})
    >>> arguments(["check", "dir"]), arguments(["run", "dir", "--work", "w"])[2]
    (('check', PosixPath('dir'), {}), {'--work': 'w'})
    >>> [arguments(a) for a in ([], ["check"], ["other", "dir"], ["check", "--help"], ["run", "dir"],
    ...     ["run", "dir", "--work"], ["check", "dir", "--work", "w"], ["seal", "dir", "--today", "today"])]
    [None, None, None, None, None, None, None, None]
    """
    if len(args) < 2 or args[0] not in OPTIONS or args[1].startswith("--"):
        return None
    options = dict(zip(args[2::2], args[3::2], strict=False))
    if (
        len(args) % 2
        or tuple(options) != OPTIONS[args[0]]
        or not is_date(options.get("--today", "2026-01-01"))
    ):
        return None
    return args[0], pathlib.Path(args[1]), options


def main(argv=None, run=subprocess.run):
    r"""Run one command. Returns the result code.

    >>> import sample, tempfile
    >>> folder, work = sample.folder(("| judge |", "| program | `friend` |")), tempfile.mkdtemp(prefix="experiment-")
    >>> main(["check", str(folder)])
    Differences between the arms:
    ...
    Result: the registration is complete.
    0
    >>> main(["seal", str(folder), "--today", "2026-01-11"])
    Sealed: 4 files, seal ..., commit (none).
    0
    >>> main(["run", str(folder), "--work", work], run=sample.agent())
    arm plain, run 1: valid
    ...
    Valid runs: 10 of 10. The transcripts are in ...
    0
    >>> main(["blind", str(folder), "--work", work])
    No criterion has the judge. No packet is necessary.
    0
    >>> main(["score", str(folder)])
    # Result of the experiment: a polite prompt
    ...
    - Verdict: confirmed
    ...
    Written: ...result.md
    0

    A folder without a registration gives the result code 2. Wrong arguments print the usage text.

    >>> main(["check", str(folder / "absent")])
    The input cannot be read: ...registration.md: No such file or directory
    2
    >>> with contextlib.redirect_stderr(io.StringIO()) as usage:
    ...     main([]), main(["check"])
    (2, 2)
    >>> usage.getvalue().splitlines()[2]
    '  experiment.py check DIR'
    """
    parsed = arguments(list(sys.argv[1:] if argv is None else argv))
    if parsed is None:
        print(__doc__, file=sys.stderr)
        return 2
    name, folder, options = parsed
    calls = {
        "check": lambda: check(folder),
        "seal": lambda: seal(folder, options["--today"]),
        "run": lambda: run_command(folder, options["--work"], run=run),
        "blind": lambda: blind(folder, options["--work"]),
        "score": lambda: score(folder),
    }
    try:
        return calls[name]()
    except Unreadable as e:
        print(MESSAGES["unreadable"].format(e))
        return 2


def selftest():
    """Run the examples (doctests) of this program. Returns the result code."""
    globs = {"contextlib": __import__("contextlib"), "io": __import__("io")}
    flags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE | doctest.IGNORE_EXCEPTION_DETAIL
    result = doctest.testmod(sys.modules["__main__"], optionflags=flags, extraglobs=globs)
    print(f"{result.attempted} examples, {result.failed} failed")
    return 1 if result.failed or not result.attempted else 0


if __name__ == "__main__":
    if sys.argv[1:2] == ["--selftest"]:
        sys.exit(selftest())
    sys.exit(main())
