#!/usr/bin/env python3
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Calculation of risk and reward for the items of an aspect specification. Standard library only.

  place.py SPEC [--write] [--rubric FILE]

  SPEC           the folder with spec.md and vetting.md, and charter.md if the aspect has a charter
  --write        fill the computed cells of the table "Items" in vetting.md, and the cells Level
                 and "Placed by" of the checklist in spec.md. Without it, the program changes no
                 file.
  --rubric FILE  a different rubric; the default is rubric-items.txt beside this program

The table "Items" of vetting.md holds six answers for each item, each a whole number with its
source in parentheses, and the risk dimension for an item whose return depends on the risk of a
project. The program computes, in whole numbers:

  return = severity x probability x breadth        cost = adopt + keep
  score  = (return x 10) // cost - 5 x own risk

An item is admitted when its score is at or above the admission threshold. It is on level 1 when
its breadth is 3 and its score is at or above the level 1 threshold. If not, it is on level 2
when its cost is at or below the cost limit, and on level 3 when the cost is above. The order is
by level, then by score from high to low, then by identifier.

The charter of the owner governs this calculation. The file charter.md gives the lines of the
charter, and the cell "Serves" of a requirement in vetting.md names the lines that the requirement
serves. For each item, the program takes the requirements that go to it, and the lines that they
serve. A line with the effect "level <n>" admits the item, and the item is on level n or on a
lower level: the calculation does not put it on a higher level. A line with the effect "no exit:
not admitted" admits the item, and the calculation gives its level. The cell "Placed by" of an
item names the line of the charter that placed it, or "calculation". A line places an item when
the item is on the level that the line gives. A specification without a charter has "calculation"
in each such cell.

Result code 0: each item is placed. Result code 1: an item stays pending. Result code 2: the
input cannot be read.
"""

import pathlib
import re
import sys

import aspect
import check

ANSWERS = check.ANSWERS
COMPUTED = ("return", "cost", "score", "admitted", "level")
QUESTION = re.compile(r"^question (\S+) (\d+)-(\d+):")
SETTING = re.compile(r"^(version|threshold \S+|limit \S+):\s*(\d+)\s*$")
NUMBER = re.compile(r"^\s*(\d+)(?![\d.,/])")  # a whole number only

MESSAGES = {
    "placed": "{0}: return {1}, cost {2}, score {3}, admitted {4}, level {5}, position {6}.",
    "placed-by-charter": (
        "{0}: return {1}, cost {2}, score {3}, admitted {4}, level {5}, position {6}, placed by {7}."
    ),
    "admitted-by-charter": (
        "{0}: return {1}, cost {2}, score {3}, admitted {4}, level {5}, position {6}, "
        "admitted by the charter."
    ),
    "not-admitted": "{0}: return {1}, cost {2}, score {3}, not admitted.",
    "no-row": "{0}: pending. The table Items of vetting.md has no row for this item.",
    "missing": "{0}: pending. The answer '{1}' is missing.",
    "out-of-scale": "{0}: pending. The answer '{1}' is {2}. The scale is {3} to {4}.",
    "no-dimension": "{0}: pending. The item is above level 1. Record its risk dimension.",
    "bad-dimension": "{0}: pending. The risk dimension '{1}' is not in section 1 of spec.md.",
    "summary": "Rubric version {0}. Items placed: {1}. Items pending: {2}.",
    "written": "The program wrote the results to vetting.md and spec.md.",
    "not-written": "The program cannot write the cell '{0}' in line {1} of {2}. Correct the table.",
    "rubric": "The rubric cannot be read: {0}",
    "unreadable": "The input cannot be read: {0}",
}


def read_rubric(path):
    r"""The settings and the scale of each question of a rubric file.

    >>> path = pathlib.Path(__file__).with_name("rubric-items.txt")
    >>> rubric = read_rubric(path)
    >>> [rubric[k] for k in ("version", "threshold admission", "threshold level-1", "limit cost-level-2")]
    [1, 20, 40, 4]
    >>> rubric["scales"]
    {'severity': (1, 3), 'probability': (1, 3), 'breadth': (1, 3), 'adopt': (1, 3), 'keep': (1, 3),
     'own risk': (0, 2)}

    A rubric that is not complete, or that can give a cost of zero, is refused.

    >>> import sample
    >>> other = sample.folder() / "rubric.txt"
    >>> _ = other.write_text("version: 1\n", encoding="utf-8")
    >>> read_rubric(other)
    Traceback (most recent call last):
        ...
    ValueError: missing: threshold admission, threshold level-1, limit cost-level-2, severity, ...
    >>> text = aspect.read_text(path).replace("question adopt 1-3", "question adopt 0-3")
    >>> _ = other.write_text(text, encoding="utf-8")
    >>> read_rubric(other)
    Traceback (most recent call last):
        ...
    ValueError: the scales of adopt and keep must start at 1 or above

    The text of each message is in Simplified Technical English.

    >>> aspect.long_sentences(MESSAGES)
    []
    """
    rubric = {"scales": {}}
    for line in aspect.read_text(path).splitlines():
        if m := SETTING.match(line):
            rubric[m.group(1)] = int(m.group(2))
        elif m := QUESTION.match(line):
            rubric["scales"][m.group(1).replace("-", " ")] = (int(m.group(2)), int(m.group(3)))
    needed = ("version", "threshold admission", "threshold level-1", "limit cost-level-2")
    absent = [k for k in needed if k not in rubric] + [a for a in ANSWERS if a not in rubric["scales"]]
    if absent:
        raise ValueError("missing: " + ", ".join(absent))
    if min(rubric["scales"]["adopt"][0], rubric["scales"]["keep"][0]) < 1:
        raise ValueError("the scales of adopt and keep must start at 1 or above")
    return rubric


def place_item(ident, row, rubric, dimensions, rule=None, admit=False):
    """The result for one item: a dictionary with "state" placed, not admitted or pending.

    rule is the level that a line of the charter gives to the item: {"level": n, "by": the line},
    or None. admit says that the charter does not permit "not admitted" for the item.

    >>> rubric = read_rubric(pathlib.Path(__file__).with_name("rubric-items.txt"))
    >>> def item(severity, probability, breadth, adopt, keep, own, dimension="", rule=None, admit=False):
    ...     cells = dict(zip(ANSWERS, map(str, (severity, probability, breadth, adopt, keep, own))))
    ...     cells["dimension"] = dimension
    ...     result = place_item("C-01", cells, rubric, {"operative"}, rule, admit)
    ...     if rule or admit:
    ...         return result.get("level", result["state"]), result["by"], result["charter admits"]
    ...     return result.get("score"), result.get("level", result["state"])

    The return is severity x probability x breadth, and the cost is adopt + keep. The score is
    (return x 10) // cost - 5 x own risk, in whole numbers.

    >>> item(3, 3, 3, 1, 1, 0), item(1, 1, 1, 3, 3, 2)
    ((135, '1'), (-9, 'not admitted'))

    An item is admitted at a score of 20.

    >>> item(2, 2, 2, 2, 2, 0, "operative"), item(2, 2, 2, 2, 3, 0, "operative")
    ((20, '2, operative'), (16, 'not admitted'))

    Level 1 needs a breadth of 3 and a score of 40. The items of level 1 are the basic practices.

    >>> item(2, 2, 3, 2, 1, 0), item(2, 2, 3, 2, 2, 0, "operative"), item(3, 3, 2, 1, 1, 0, "operative")
    ((40, '1'), (30, '2, operative'), (90, '2, operative'))

    Above level 1, a cost of 4 or less is level 2, and a higher cost is level 3.

    >>> item(3, 3, 2, 2, 2, 0, "operative"), item(3, 3, 2, 3, 2, 0, "operative")
    ((45, '2, operative'), (36, '3, operative'))

    A line of the charter that gives a level places the item before the calculation: the item is
    admitted, and it is on that level or on a lower level. The calculation does not put it on a
    higher level. These two items are on level 2 and are not admitted without the charter.

    >>> basic = {"level": 1, "by": "K-1"}
    >>> item(3, 3, 2, 1, 1, 0, "operative", rule=basic), item(1, 1, 2, 3, 2, 1, rule=basic)
    (('1', 'K-1', False), ('1', 'K-1', True))

    The calculation places an item that it puts on a lower level than the level of the line.

    >>> goal = {"level": 2, "by": "T-2"}
    >>> item(3, 3, 3, 1, 1, 0, rule=goal), item(3, 3, 2, 3, 2, 0, "operative", rule=goal)
    (('1', 'calculation', False), ('2, operative', 'T-2', False))
    >>> item(3, 3, 2, 3, 2, 0, rule=goal)
    ('pending', 'calculation', False)

    A line that does not permit "not admitted" admits the item. The calculation gives its level.

    >>> item(1, 1, 2, 3, 2, 1, "operative", admit=True), item(1, 1, 2, 2, 2, 1, "operative", admit=True)
    (('3, operative', 'calculation', True), ('2, operative', 'calculation', True))

    An item above level 1 needs a risk dimension of section 1. The program does not choose one.

    >>> cells = dict(zip(ANSWERS, "322220"))
    >>> place_item("C-01", cells, rubric, {"operative"})["text"]
    'C-01: pending. The item is above level 1. Record its risk dimension.'
    >>> place_item("C-01", cells | {"dimension": "legal"}, rubric, {"operative"})["text"]
    "C-01: pending. The risk dimension 'legal' is not in section 1 of spec.md."

    An answer is a whole number on its scale. Its source follows in parentheses.

    >>> cells = dict(zip(ANSWERS, ["3 (S-02 abstract)", "2", "2", "2", "2", "0"]), dimension="operative")
    >>> place_item("C-01", cells, rubric, {"operative"})["score"]
    30
    >>> for answer in ("2.5 (judgement)", "1/2", "2,5", "two", ""):
    ...     cells = dict(zip(ANSWERS, [answer, "2", "2", "2", "2", "0"]))
    ...     print(repr(answer), "->", place_item("C-01", cells, rubric, set())["text"])
    '2.5 (judgement)' -> C-01: pending. The answer 'severity' is missing.
    '1/2' -> C-01: pending. The answer 'severity' is missing.
    '2,5' -> C-01: pending. The answer 'severity' is missing.
    'two' -> C-01: pending. The answer 'severity' is missing.
    '' -> C-01: pending. The answer 'severity' is missing.
    >>> place_item("C-01", dict(zip(ANSWERS, "422220")), rubric, set())["text"]
    "C-01: pending. The answer 'severity' is 4. The scale is 1 to 3."
    >>> place_item("C-01", None, rubric, set())["text"]
    'C-01: pending. The table Items of vetting.md has no row for this item.'
    """
    result = {"id": ident, "state": "pending", "by": aspect.CALCULATION, "charter admits": False}
    if row is None:
        return result | {"text": MESSAGES["no-row"].format(ident)}
    values = {}
    for name in ANSWERS:
        m = NUMBER.match(row.get(name, ""))
        low, high = rubric["scales"][name]
        if not m:
            return result | {"text": MESSAGES["missing"].format(ident, name)}
        values[name] = int(m.group(1))
        if not low <= values[name] <= high:
            return result | {"text": MESSAGES["out-of-scale"].format(ident, name, values[name], low, high)}
    gain = values["severity"] * values["probability"] * values["breadth"]
    cost = values["adopt"] + values["keep"]
    score = (gain * 10) // cost - 5 * values["own risk"]
    result |= {"return": gain, "cost": cost, "score": score}
    if score < rubric["threshold admission"]:
        if not (rule or admit):
            return result | {"state": "not admitted", "level": "not admitted"}
        result["charter admits"] = True
    if values["breadth"] == 3 and score >= rubric["threshold level-1"]:
        rank = 1
    else:
        rank = 2 if cost <= rubric["limit cost-level-2"] else 3
    rank = min(rank, rule["level"]) if rule else rank
    if rank == 1:
        return result | {"state": "placed", "level": "1", "rank": 1, "by": check.placed_by(rule, 1)}
    dimension = row.get("dimension", "").strip().strip("`")
    if not dimension:
        return result | {"text": MESSAGES["no-dimension"].format(ident)}
    if dimension not in dimensions:
        return result | {"text": MESSAGES["bad-dimension"].format(ident, dimension)}
    placed = {"state": "placed", "level": f"{rank}, {dimension}", "rank": rank}
    return result | placed | {"by": check.placed_by(rule, rank)}


def place(data, rubric):
    """The result for each item that is not retired, with the position of each placed item.

    The order is by level, then by score from high to low, then by identifier.

    >>> import sample
    >>> rubric = read_rubric(pathlib.Path(__file__).with_name("rubric-items.txt"))
    >>> for r in place(sample.load(), rubric):
    ...     print(r["id"], r["return"], r["cost"], r["score"], r["level"], r.get("position"))
    C-01 27 2 135 1 1
    C-02 12 4 30 2, operative 3
    C-03 12 6 20 3, regulatory 4
    C-04 2 5 -1 not admitted None
    C-05 18 3 60 1 2

    A retired item is not placed.

    >>> [r["id"] for r in place(sample.load(("spec.md", "| 2, operative |", "| retired |")), rubric)]
    ['C-01', 'C-03', 'C-04', 'C-05']

    The charter places an item before the calculation. In the sample, the line T-2 gives level 2
    to C-02, and the line T-1 gives level 1 to C-05. The calculation gives the same levels.

    >>> [(r["id"], r["by"]) for r in place(sample.load(), rubric)]
    [('C-01', 'calculation'), ('C-02', 'T-2'), ('C-03', 'calculation'), ('C-04', 'calculation'),
     ('C-05', 'T-1')]

    Here the requirement of C-03 serves the line T-1 also, and the requirement of C-04 serves the
    line K-1. The calculation puts C-03 on level 3 and does not admit C-04.

    >>> r02, r04 = sample.REQUIREMENT_R02, sample.SERVES_R04
    >>> basic = ("vetting.md", r02, r02.replace("| none |", "| T-1 |"))
    >>> admit = ("vetting.md", r04, r04.replace("| none |", "| K-1 |"))
    >>> dimension = ("vetting.md", "| 1 (judgement) |  | 2 | 5 |", "| 1 (judgement) | operative | 2 | 5 |")
    >>> for r in place(sample.load(basic, admit, dimension), rubric)[2:4]:
    ...     print(r["id"], r["score"], r["level"], r["by"], r["charter admits"], r["position"])
    C-03 20 1 T-1 False 3
    C-04 -1 3, operative calculation True 5

    A specification without a charter has "calculation" for each item.

    >>> {r["by"] for r in place(sample.load(charter=False), rubric)}
    {'calculation'}
    """
    rows = {r.get("item"): r for r in data["vetting_items"]}
    dimensions = {d["name"] for d in data["risk_dimensions"]}
    places, admits = check.charter_rules(data)
    results = [
        place_item(r["id"], rows.get(r["id"]), rubric, dimensions, places.get(r["id"]), r["id"] in admits)
        for r in check.live_items(data)
    ]
    placed = sorted(
        (r for r in results if r["state"] == "placed"), key=lambda r: (r["rank"], -r["score"], r["id"])
    )
    for position, result in enumerate(placed, 1):
        result["position"] = position
    return sorted(results, key=lambda r: r["id"])


def line_of(result):
    """The line of the report for one result.

    >>> line_of({"id": "C-04", "state": "not admitted", "return": 2, "cost": 5, "score": -1})
    'C-04: return 2, cost 5, score -1, not admitted.'
    >>> line_of({"id": "C-02", "state": "pending", "text": "C-02: pending. The answer 'keep' is missing."})
    "C-02: pending. The answer 'keep' is missing."

    The line names the line of the charter that placed the item. It says so if only the charter
    admits the item.

    >>> placed = {"id": "C-03", "state": "placed", "return": 12, "cost": 6, "score": 20, "position": 3}
    >>> line_of(placed | {"level": "1", "by": "T-1", "charter admits": False})
    'C-03: return 12, cost 6, score 20, admitted yes, level 1, position 3, placed by T-1.'
    >>> print(line_of(placed | {"level": "3, operative", "by": "calculation", "charter admits": True}))
    C-03: return 12, cost 6, score 20, admitted yes, level 3, operative, position 3, admitted by the
    charter.
    """
    if result["state"] == "placed":
        r = result
        by = r.get("by", aspect.CALCULATION)
        rule = "placed" if by == aspect.CALCULATION else "placed-by-charter"
        rule = "admitted-by-charter" if rule == "placed" and r.get("charter admits") else rule
        return MESSAGES[rule].format(
            r["id"], r["return"], r["cost"], r["score"], "yes", r["level"], r["position"], by
        )
    if result["state"] == "not admitted":
        return MESSAGES["not-admitted"].format(
            result["id"], result["return"], result["cost"], result["score"]
        )
    return result["text"]


def write(data, results, rubric):
    r"""Fill the computed cells of vetting.md, and the cells Level and "Placed by" of spec.md.

    Returns a message for each cell that the table does not have. A specification without a
    charter needs no cell "Placed by": the program fills the cell only if the table has it.

    >>> import sample
    >>> rubric = read_rubric(pathlib.Path(__file__).with_name("rubric-items.txt"))
    >>> folder = sample.folder(
    ...     ("vetting.md", "| 27 | 2 | 135 | yes | 1 |", "| | | | | |"),
    ...     ("spec.md", "| 1 | authority (2) |", "| pending | authority (2) |"),
    ... )
    >>> data = aspect.load(folder)
    >>> write(data, place(data, rubric), rubric)
    []

    Only the computed cells and the Level cells change: the sample comes back.

    >>> [aspect.read_text(folder / name) == sample.FILES[name] for name in ("spec.md", "vetting.md")]
    [True, True]

    The program finds the Level cell by the name of its column. Thus the View cell stays.

    >>> [(aspect.view_of(r), r["level"]) for r in aspect.load(folder)["checklist"]][:2]
    [('storage', '1'), ('operation', '2, operative')]

    A row of vetting.md for an item that the checklist does not have is left as it is. A row that
    is too short is reported.

    >>> old = " | 1 | practice | the schedule of the program is in the repository | S-04 README;"
    >>> extra = "| C-09 | 1 | 1 | 1 | 1 | 1 | 0 |  | | | | | |\n"
    >>> short = ("spec.md", old + " S-01 section 3 | T-1 |", " |")
    >>> folder = sample.folder(short, ("vetting.md", "| C-01 | 3", extra + "| C-01 | 3"))
    >>> data = aspect.load(folder)
    >>> write(data, place(data, rubric), rubric)
    ["The program cannot write the cell 'level' in line 71 of spec.md. Correct the table.",
     "The program cannot write the cell 'placed by' in line 71 of spec.md. Correct the table."]
    >>> extra in aspect.read_text(folder / "vetting.md")
    True

    The program writes the line of the charter that placed an item into the cell "Placed by".
    Here the requirement of C-03 serves the line T-1 also, which gives level 1.

    >>> r02 = sample.REQUIREMENT_R02
    >>> folder = sample.folder(("vetting.md", r02, r02.replace("| none |", "| T-1 |")))
    >>> data = aspect.load(folder)
    >>> check.brief(check.check_serves(data)[0])
    [('item-above-charter-level', 'C-03')]
    >>> write(data, place(data, rubric), rubric)
    []
    >>> data = aspect.load(folder)
    >>> [(r["level"], r["placed by"]) for r in data["checklist"]], check.check_serves(data)
    ([('1', 'calculation'), ('2, operative', 'T-2'), ('1', 'T-1'), ('not admitted', 'calculation'),
      ('1', 'T-1')], ([], []))

    A specification without a charter gets "calculation" in each cell "Placed by" that its table
    has. A table without the column stays as it is.

    >>> folder = sample.folder(charter=False)
    >>> data = aspect.load(folder)
    >>> write(data, place(data, rubric), rubric), {r["placed by"] for r in aspect.load(folder)["checklist"]}
    ([], {'calculation'})
    >>> head = ("spec.md", "| Check | Source | Placed by |", "| Check | Source | Other |")
    >>> folder = sample.folder(head, charter=False)
    >>> data = aspect.load(folder)
    >>> write(data, place(data, rubric), rubric), aspect.load(folder)["checklist"][1]["other"]
    ([], 'T-2')
    """
    folder = pathlib.Path(data["folder"])
    by_id = {r["id"]: r for r in results}
    failed = []

    def put(file, row, name, text):
        if not aspect.set_cell(folder / file, row["_line"], aspect.column_of(row, name), text):
            failed.append(MESSAGES["not-written"].format(name, row["_line"], file))

    for row in data["vetting_items"]:
        result = by_id.get(row.get("item"))
        if result is None:
            continue
        cells = {
            "return": str(result.get("return", "")),
            "cost": str(result.get("cost", "")),
            "score": str(result.get("score", "")),
            "admitted": {"placed": "yes", "not admitted": "no"}.get(result["state"], ""),
            "level": result.get("level", "pending"),
        }
        for name in COMPUTED:
            put("vetting.md", row, name, cells[name])
    for row in check.live_items(data):
        put("spec.md", row, "level", by_id[row["id"]].get("level", "pending"))
        if data["charter"] is not None or aspect.column_of(row, "placed by") >= 0:
            put("spec.md", row, "placed by", by_id[row["id"]]["by"])
    path = folder / "vetting.md"
    text = aspect.read_text(path)
    text = re.sub(r"(Rubric for items: version )\d+", rf"\g<1>{rubric['version']}", text)
    aspect.write_text(path, text)
    return failed


def main(argv=None):
    r"""The command line. See the text at the start of this file.

    >>> import sample
    >>> good = sample.folder()
    >>> code, out, err = sample.run(main, good)
    >>> code, err
    (0, '')
    >>> print(out)
    C-01: return 27, cost 2, score 135, admitted yes, level 1, position 1.
    C-02: return 12, cost 4, score 30, admitted yes, level 2, operative, position 3, placed by T-2.
    C-03: return 12, cost 6, score 20, admitted yes, level 3, regulatory, position 4.
    C-04: return 2, cost 5, score -1, not admitted.
    C-05: return 18, cost 3, score 60, admitted yes, level 1, position 2, placed by T-1.
    Rubric version 1. Items placed: 5. Items pending: 0.
    <BLANKLINE>

    The same input gives the same output. Without --write no file changes.

    >>> before = {p.name: p.read_bytes() for p in good.iterdir()}
    >>> sample.run(main, good) == (code, out, err), before == {p.name: p.read_bytes() for p in good.iterdir()}
    (True, True)

    An item with a missing answer stays pending, and the result code is 1.

    >>> effort = "2 (judgement) | 2 (judgement) | 2 (judgement)"
    >>> c02 = f"| C-02 | 3 (S-02 section 4) | 2 (S-02 section 4) | {effort} | 0 (judgement) |"
    >>> folder = sample.folder(("vetting.md", c02, c02.replace("| 2 (S-02 section 4) |", "| |")))
    >>> code, out, _ = sample.run(main, folder)
    >>> code, out.splitlines()[1]
    (1, "C-02: pending. The answer 'probability' is missing.")
    >>> out.splitlines()[-1]
    'Rubric version 1. Items placed: 4. Items pending: 1.'

    The owner corrects an answer in vetting.md and runs the program again.

    >>> folder = sample.folder(("vetting.md", c02, c02.replace(effort, "3 (owner) | 1 (owner) | 1 (owner)")))
    >>> sample.run(main, folder)[1].splitlines()[1]
    'C-02: return 18, cost 2, score 90, admitted yes, level 1, position 2.'

    --write fills the cells. Files with the line end of Windows keep it, and a different line
    separator in a file does not move the write.

    >>> names = ("spec.md", "vetting.md")
    >>> windows = {n: sample.FILES[n].replace("\n", "\r\n").encode("utf-8") for n in names}
    >>> for name in names:
    ...     _ = (good / name).write_bytes(windows[name])
    >>> code, out, _ = sample.run(main, good, "--write")
    >>> code, out.splitlines()[-1], [(good / n).read_bytes() == windows[n] for n in names]
    (0, 'The program wrote the results to vetting.md and spec.md.', [True, True])
    >>> folder = sample.folder(
    ...     ("spec.md", "A small specification", "A small" + chr(0x2028) + "specification"),
    ...     ("vetting.md", "Rubric for sources", "Rubric" + "\x0c" + "for sources"),
    ... )
    >>> before = {p.name: p.read_bytes() for p in folder.iterdir()}
    >>> sample.run(main, folder, "--write")[0], before == {p.name: p.read_bytes() for p in folder.iterdir()}
    (0, True)

    A cell that cannot be written is reported, and the result code is 1.

    >>> old = " | 1 | practice | the schedule of the program is in the repository | S-04 README;"
    >>> short = sample.folder(("spec.md", old + " S-01 section 3 | T-1 |", " |"))
    >>> code, out, err = sample.run(main, short, "--write")
    >>> code, err, out.splitlines()[-3]
    (1, '', "The program cannot write the cell 'level' in line 71 of spec.md. Correct the table.")

    --rubric gives a different rubric. Its version goes into the record.

    >>> rubric = good.parent / "rubric.txt"
    >>> text = aspect.read_text(pathlib.Path(__file__).with_name("rubric-items.txt"))
    >>> _ = rubric.write_text(text.replace("version: 1", "version: 7"), encoding="utf-8")
    >>> folder = sample.folder()
    >>> sample.run(main, folder, "--write", "--rubric", rubric)[1].splitlines()[-2]
    'Rubric version 7. Items placed: 5. Items pending: 0.'
    >>> vetting = aspect.read_text(folder / "vetting.md")
    >>> "Rubric for items: version 7." in vetting, "Rubric for sources: version 1." in vetting
    (True, True)

    A rubric or an input that cannot be read gives the result code 2.

    >>> import tempfile
    >>> _ = rubric.write_bytes(b"\xff\xfe")
    >>> code, _, err = sample.run(main, folder, "--rubric", rubric)
    >>> code, err.startswith("The rubric cannot be read:")
    (2, True)
    >>> sample.run(main, tempfile.mkdtemp(prefix="sota-empty-"))[0], sample.run(main)[0]
    (2, 2)
    """
    args = list(sys.argv[1:] if argv is None else argv)
    if args[:1] == ["--selftest"]:
        sys.exit(aspect.selftest())
    if not args or args[0] in ("-h", "--help"):
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    rubric_file = check.option(args, "--rubric") or pathlib.Path(__file__).with_name("rubric-items.txt")
    folder = next((a for a in args if not a.startswith("--")), "")
    try:
        data = aspect.load(folder)
    except (aspect.Unreadable, OSError) as e:
        print(MESSAGES["unreadable"].format(e), file=sys.stderr)
        sys.exit(2)
    try:
        rubric = read_rubric(rubric_file)
    except (aspect.Unreadable, OSError, ValueError) as e:
        print(MESSAGES["rubric"].format(e), file=sys.stderr)
        sys.exit(2)
    results = place(data, rubric)
    pending = [r for r in results if r["state"] == "pending"]
    print("\n".join(line_of(r) for r in results))
    print(MESSAGES["summary"].format(rubric["version"], len(results) - len(pending), len(pending)))
    if "--write" in args:
        failed = write(data, results, rubric)
        print("\n".join([*failed, MESSAGES["written"]]))
        if failed:
            sys.exit(1)
    sys.exit(1 if pending else 0)


if __name__ == "__main__":
    main()
