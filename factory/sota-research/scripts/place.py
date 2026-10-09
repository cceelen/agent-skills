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


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        sys.exit(__doc__)
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
