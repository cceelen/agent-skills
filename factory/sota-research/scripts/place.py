#!/usr/bin/env python3
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Calculation of risk and reward for the items of an aspect specification. Standard library only.

  place.py SPEC [--write] [--rubric FILE]

  SPEC           the folder with spec.md and vetting.md
  --write        fill the computed cells of the table "Items" in vetting.md and the Level cells
                 of the checklist in spec.md. Without it, the program changes no file.
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

Result code 0: each item is placed. Result code 1: an item stays pending. Result code 2: the
input cannot be read.
"""

import pathlib
import re
import sys

import aspect
import check

ANSWERS = ("severity", "probability", "breadth", "adopt", "keep", "own risk")
COMPUTED = ("return", "cost", "score", "admitted", "level")
QUESTION = re.compile(r"^question (\S+) (\d+)-(\d+):")
SETTING = re.compile(r"^(version|threshold \S+|limit \S+):\s*(\d+)\s*$")
NUMBER = re.compile(r"^\s*(\d+)(?![\d.,/])")  # a whole number only

MESSAGES = {
    "placed": "{0}: return {1}, cost {2}, score {3}, admitted {4}, level {5}, position {6}.",
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
    """The settings and the scale of each question of a rubric file."""
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


def place_item(ident, row, rubric, dimensions):
    """The result for one item: a dictionary with "state" placed, not admitted or pending."""
    if row is None:
        return {"id": ident, "state": "pending", "text": MESSAGES["no-row"].format(ident)}
    values = {}
    for name in ANSWERS:
        m = NUMBER.match(row.get(name, ""))
        low, high = rubric["scales"][name]
        if not m:
            return {"id": ident, "state": "pending", "text": MESSAGES["missing"].format(ident, name)}
        values[name] = int(m.group(1))
        if not low <= values[name] <= high:
            text = MESSAGES["out-of-scale"].format(ident, name, values[name], low, high)
            return {"id": ident, "state": "pending", "text": text}
    gain = values["severity"] * values["probability"] * values["breadth"]
    cost = values["adopt"] + values["keep"]
    score = (gain * 10) // cost - 5 * values["own risk"]
    result = {"id": ident, "return": gain, "cost": cost, "score": score}
    if score < rubric["threshold admission"]:
        return result | {"state": "not admitted", "level": "not admitted"}
    if values["breadth"] == 3 and score >= rubric["threshold level-1"]:
        return result | {"state": "placed", "level": "1", "rank": 1}
    dimension = row.get("dimension", "").strip().strip("`")
    if not dimension:
        return result | {"state": "pending", "text": MESSAGES["no-dimension"].format(ident)}
    if dimension not in dimensions:
        return result | {"state": "pending", "text": MESSAGES["bad-dimension"].format(ident, dimension)}
    rank = 2 if cost <= rubric["limit cost-level-2"] else 3
    return result | {"state": "placed", "level": f"{rank}, {dimension}", "rank": rank}


def place(data, rubric):
    """The result for each item that is not retired, with the position of each placed item."""
    rows = {r.get("item"): r for r in data["vetting_items"]}
    dimensions = {d["name"] for d in data["risk_dimensions"]}
    results = [place_item(r["id"], rows.get(r["id"]), rubric, dimensions) for r in check.live_items(data)]
    placed = sorted(
        (r for r in results if r["state"] == "placed"), key=lambda r: (r["rank"], -r["score"], r["id"])
    )
    for position, result in enumerate(placed, 1):
        result["position"] = position
    return sorted(results, key=lambda r: r["id"])


def line_of(result):
    if result["state"] == "placed":
        r = result
        return MESSAGES["placed"].format(
            r["id"], r["return"], r["cost"], r["score"], "yes", r["level"], r["position"]
        )
    if result["state"] == "not admitted":
        return MESSAGES["not-admitted"].format(
            result["id"], result["return"], result["cost"], result["score"]
        )
    return result["text"]


def write(data, results, rubric):
    """Fill the computed cells of vetting.md and the Level cells of spec.md.

    Returns a message for each cell that the table does not have.
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
    path = folder / "vetting.md"
    text = aspect.read_text(path)
    text = re.sub(r"(Rubric for items: version )\d+", rf"\g<1>{rubric['version']}", text)
    aspect.write_text(path, text)
    return failed


def main(argv=None):
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


__test__ = {
    "the sample specification": r"""
    >>> import sample
    >>> good = sample.folder()
    >>> code, out, err = sample.run(main, good)
    >>> code, err
    (0, '')
    >>> print(out)
    C-01: return 27, cost 2, score 135, admitted yes, level 1, position 1.
    C-02: return 12, cost 4, score 30, admitted yes, level 2, operative, position 3.
    C-03: return 12, cost 6, score 20, admitted yes, level 3, regulatory, position 4.
    C-04: return 2, cost 5, score -1, not admitted.
    C-05: return 18, cost 3, score 60, admitted yes, level 1, position 2.
    Rubric version 1. Items placed: 5. Items pending: 0.
    <BLANKLINE>
    >>> sample.run(main, good) == sample.run(main, good)
    True
    >>> aspect.long_sentences(MESSAGES)
    []
    """,
    "the limits of the calculation": r"""
    >>> rubric = read_rubric(pathlib.Path(__file__).with_name("rubric-items.txt"))
    >>> [rubric[k] for k in ("version", "threshold admission", "threshold level-1", "limit cost-level-2")]
    [1, 20, 40, 4]
    >>> def item(severity, probability, breadth, adopt, keep, own, dimension=""):
    ...     cells = dict(zip(ANSWERS, map(str, (severity, probability, breadth, adopt, keep, own))))
    ...     result = place_item("C-01", cells | {"dimension": dimension}, rubric, {"operative"})
    ...     return result.get("score"), result.get("level", result["state"])

    The score is (return x 10) // cost - 5 x own risk, in whole numbers.

    >>> item(3, 3, 3, 1, 1, 0), item(3, 3, 3, 3, 3, 2), item(1, 1, 1, 3, 3, 2)
    ((135, '1'), (35, 'pending'), (-9, 'not admitted'))

    Admission is at a score of 20. Level 1 needs a breadth of 3 and a score of 40.

    >>> item(2, 2, 2, 2, 2, 0, "operative"), item(2, 2, 2, 2, 3, 0, "operative")
    ((20, '2, operative'), (16, 'not admitted'))
    >>> item(2, 2, 3, 2, 1, 0), item(2, 2, 3, 2, 2, 0, "operative"), item(3, 3, 2, 1, 1, 0, "operative")
    ((40, '1'), (30, '2, operative'), (90, '2, operative'))

    Above level 1, a cost of 4 or less is level 2, and a higher cost is level 3.

    >>> item(3, 3, 2, 2, 2, 0, "operative"), item(3, 3, 2, 3, 2, 0, "operative")
    ((45, '2, operative'), (36, '3, operative'))

    An item above level 1 needs a risk dimension of section 1. The program does not choose one.

    >>> cells = dict(zip(ANSWERS, "322220"))
    >>> place_item("C-01", cells, rubric, {"operative"})["text"]
    'C-01: pending. The item is above level 1. Record its risk dimension.'
    >>> place_item("C-01", cells | {"dimension": "legal"}, rubric, {"operative"})["text"]
    "C-01: pending. The risk dimension 'legal' is not in section 1 of spec.md."

    An answer is a whole number on its scale, with its source after it.

    >>> cells = dict(zip(ANSWERS, ["3 (S-02 abstract)", "2", "2", "2", "2", "0"]), dimension="operative")
    >>> place_item("C-01", cells, rubric, {"operative"})["score"]
    30
    >>> for answer in ("2.5 (judgement)", "1/2", "2,5", "two", ""):
    ...     cells = dict(zip(ANSWERS, [answer, "2", "2", "2", "2", "0"]))
    ...     text = place_item("C-01", cells, rubric, set())["text"]
    ...     assert text == "C-01: pending. The answer 'severity' is missing.", answer
    >>> place_item("C-01", dict(zip(ANSWERS, "422220")), rubric, set())["text"]
    "C-01: pending. The answer 'severity' is 4. The scale is 1 to 3."
    >>> place_item("C-01", None, rubric, set())["text"]
    'C-01: pending. The table Items of vetting.md has no row for this item.'
    """,
    "pending items and the write": r"""
    >>> import sample
    >>> effort = "2 (judgement) | 2 (judgement) | 2 (judgement)"
    >>> c02 = f"| C-02 | 3 (S-02 section 4) | 2 (S-02 section 4) | {effort} | 0 (judgement) |"
    >>> folder = sample.folder(("vetting.md", c02, c02.replace("| 2 (S-02 section 4) |", "| |")))
    >>> code, out, _ = sample.run(main, folder)
    >>> code, out.splitlines()[1]
    (1, "C-02: pending. The answer 'probability' is missing.")
    >>> out.splitlines()[-1]
    'Rubric version 1. Items placed: 4. Items pending: 1.'

    Without --write no file changes.

    >>> folder = sample.folder(("vetting.md", "| 27 | 2 | 135 | yes | 1 |", "| | | | | |"))
    >>> before = {p.name: p.read_bytes() for p in folder.iterdir()}
    >>> _ = sample.run(main, folder)
    >>> before == {p.name: p.read_bytes() for p in folder.iterdir()}
    True

    With --write only the computed cells and the Level cells change: the sample comes back.

    >>> folder = sample.folder(
    ...     ("vetting.md", "| 27 | 2 | 135 | yes | 1 |", "| | | | | |"),
    ...     ("spec.md", "| 1 | authority (2) |", "| pending | authority (2) |"),
    ... )
    >>> code, out, _ = sample.run(main, folder, "--write")
    >>> code, out.splitlines()[-1]
    (0, 'The program wrote the results to vetting.md and spec.md.')
    >>> (folder / "spec.md").read_text(encoding="utf-8") == sample.SPEC
    True
    >>> (folder / "vetting.md").read_text(encoding="utf-8") == sample.VETTING
    True

    A corrected answer of the owner changes its item.

    >>> folder = sample.folder(("vetting.md", c02, c02.replace(effort, "3 (owner) | 1 (owner) | 1 (owner)")))
    >>> sample.run(main, folder)[1].splitlines()[1]
    'C-02: return 18, cost 2, score 90, admitted yes, level 1, position 2.'

    Files with the line end of Windows keep it. A different line separator does not move the write.

    >>> folder = sample.folder()
    >>> for name in ("spec.md", "vetting.md"):
    ...     _ = (folder / name).write_bytes(sample.FILES[name].replace("\n", "\r\n").encode("utf-8"))
    >>> sample.run(main, folder, "--write")[0]
    0
    >>> names = ("spec.md", "vetting.md")
    >>> windows = {n: sample.FILES[n].replace("\n", "\r\n").encode("utf-8") for n in names}
    >>> [(folder / n).read_bytes() == windows[n] for n in sorted(windows)]
    [True, True]
    >>> folder = sample.folder(
    ...     ("spec.md", "A small specification", "A small" + chr(0x2028) + "specification"),
    ...     ("vetting.md", "Rubric for sources", "Rubric" + "\x0c" + "for sources"),
    ... )
    >>> before = {p.name: p.read_bytes() for p in folder.iterdir()}
    >>> sample.run(main, folder, "--write")[0], before == {p.name: p.read_bytes() for p in folder.iterdir()}
    (0, True)

    A row that is too short is reported. It is not a crash.

    >>> old = " | 1 | practice | the schedule of the program is in the repository | S-04 README;"
    >>> old += " S-01 section 3 |"
    >>> code, out, err = sample.run(main, sample.folder(("spec.md", old, " |")), "--write")
    >>> code, err, "The program cannot write the cell 'level' in line 59 of spec.md." in out
    (1, '', True)
    """,
    "the rubric and input that cannot be read": r"""
    >>> import sample, tempfile
    >>> good = sample.folder()
    >>> text = pathlib.Path(__file__).with_name("rubric-items.txt").read_text(encoding="utf-8")
    >>> rubric = good.parent / "rubric.txt"
    >>> _ = rubric.write_text(text.replace("version: 1", "version: 7"), encoding="utf-8")
    >>> code, out, _ = sample.run(main, good, "--write", "--rubric", rubric)
    >>> code, "Rubric version 7." in out
    (0, True)
    >>> vetting = (good / "vetting.md").read_text(encoding="utf-8")
    >>> "Rubric for items: version 7." in vetting, "Rubric for sources: version 1." in vetting
    (True, True)
    >>> _ = rubric.write_text("version: 1\n", encoding="utf-8")
    >>> code, _, err = sample.run(main, good, "--rubric", rubric)
    >>> code, err.startswith("The rubric cannot be read: missing:")
    (2, True)
    >>> _ = rubric.write_text(text.replace("question adopt 1-3", "question adopt 0-3"), encoding="utf-8")
    >>> code, _, err = sample.run(main, good, "--rubric", rubric)
    >>> code, "must start at 1" in err
    (2, True)
    >>> _ = rubric.write_bytes(b"\xff\xfe")
    >>> sample.run(main, good, "--rubric", rubric)[0]
    2
    >>> sample.run(main, tempfile.mkdtemp(prefix="sota-empty-"))[0], sample.run(main)[0]
    (2, 2)
    """,
}


if __name__ == "__main__":
    main()
