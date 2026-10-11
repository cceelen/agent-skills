#!/usr/bin/env python3
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""The value and the level of each item of an aspect specification. Standard library only.

  place.py SPEC [--write] [--rubric FILE]

  SPEC           the folder with spec.md and vetting.md
  --write        fill the cells "Level" and "Strongest source" of the checklist in spec.md.
                 Without it, the program changes no file.
  --rubric FILE  a different ladder; the default is rubric-items.txt beside this program

The ladder gives each class of source one value. A source asks for an item when one of its
requirements goes to the item, or when the item cites it. The value of an item is the highest
value of these sources. An item with an own rule of the owner has the value of an own rule.

The level says how early a skill does the item: level 1 in its first iteration, then level 2,
then level 3. The program does not remove an item. An item that the owner declined keeps the
state "not admitted" and stays in the checklist. The order is by level, then by value from high
to low, then by identifier.

Result code 0: each item is placed. Result code 1: an item stays pending. Result code 2: the
input cannot be read.
"""

import pathlib
import re
import sys

import aspect
import check

OWN = "own-rule"
SETTING = re.compile(r"^(version|level [12]|value \S+):\s*(\d+)\s*$")

MESSAGES = {
    "placed": "{0}: value {1}, {2}, level {3}, position {4}.",
    "declined": "{0}: value {1}, {2}, not admitted by the owner.",
    "no-class": "{0}: pending. No source of the item has a class in section 2 of spec.md.",
    "summary": "Ladder version {0}. Items placed: {1}. Items pending: {2}.",
    "written": "The program wrote the results to spec.md.",
    "not-written": "The program cannot write the cell '{0}' in line {1} of {2}. Correct the table.",
    "rubric": "The ladder cannot be read: {0}",
    "unreadable": "The input cannot be read: {0}",
}


def read_rubric(path):
    r"""The values and the limits of a ladder file.

    >>> path = pathlib.Path(__file__).with_name("rubric-items.txt")
    >>> rubric = read_rubric(path)
    >>> rubric["version"], rubric["level 1"], rubric["level 2"]
    (5, 4, 2)
    >>> rubric["values"]
    {'regulation': 6, 'governance': 6, 'own-rule': 6, 'standard': 4, 'foundation': 3, 'vendor': 2,
     'research': 2, 'trusted-data': 2, 'independent': 1}

    A ladder that is not complete is refused.

    >>> import sample
    >>> other = sample.folder() / "rubric.txt"
    >>> _ = other.write_text("version: 1\nvalue standard: 4\n", encoding="utf-8")
    >>> read_rubric(other)
    Traceback (most recent call last):
        ...
    ValueError: missing: level 1, level 2, regulation, governance, foundation, vendor, research, ...

    The text of each message is in Simplified Technical English.

    >>> aspect.long_sentences(MESSAGES)
    []
    """
    rubric = {"values": {}}
    for line in aspect.read_text(path).splitlines():
        if m := SETTING.match(line):
            if m.group(1).startswith("value "):
                rubric["values"][m.group(1).removeprefix("value ")] = int(m.group(2))
            else:
                rubric[m.group(1)] = int(m.group(2))
    absent = [k for k in ("version", "level 1", "level 2") if k not in rubric]
    absent += [c for c in (*check.CLASSES, OWN) if c not in rubric["values"]]
    if absent:
        raise ValueError("missing: " + ", ".join(absent))
    return rubric


def askers(data):
    """For each item, the identifiers of the sources that ask for it.

    >>> import sample
    >>> askers(sample.load())
    {'C-01': ['S-01', 'S-02'], 'C-02': ['S-02'], 'C-03': ['S-01'], 'C-04': ['S-03'], 'C-05': ['S-01', 'S-04']}
    """
    found = {r["id"]: set(aspect.source_ids(r.get("source", ""))) for r in check.live_items(data)}
    for row in data["requirements"]:
        kind, name = aspect.exit_of(row.get("goes to", ""))
        if kind == "item" and name in found:
            found[name].update(aspect.source_ids(row.get("source", "")))
    return {item: sorted(found[item]) for item in sorted(found)}


def place_item(row, sources, classes, rubric):
    """The result for one item: a dictionary with "state" placed, not admitted or pending.

    >>> rubric = read_rubric(pathlib.Path(__file__).with_name("rubric-items.txt"))
    >>> classes = {"S-1": "regulation", "S-2": "standard", "S-3": "foundation", "S-4": "independent"}
    >>> def item(sources, level="pending", strongest=""):
    ...     row = {"id": "C-01", "level": level, "strongest source": strongest}
    ...     result = place_item(row, sources, classes, rubric)
    ...     return result.get("value"), result.get("from"), result.get("level", result["state"])

    The source with the highest value gives the value. A value of 4 or more is level 1.

    >>> item(["S-1", "S-2", "S-4"]), item(["S-2", "S-3"])
    ((6, 'regulation (S-1)', '1'), (4, 'standard (S-2)', '1'))

    A value of 2 or 3 is level 2, and a lower value is level 3.

    >>> item(["S-3"]), item(["S-4"])
    ((3, 'foundation (S-3)', '2'), (1, 'independent (S-4)', '3'))

    A risk dimension that the Level cell holds stays with a level above 1.

    >>> item(["S-3"], "3, operative"), item(["S-2"], "3, operative")
    ((3, 'foundation (S-3)', '2, operative'), (4, 'standard (S-2)', '1'))

    An own rule of the owner has its own value. The program does not change its cell.

    >>> item([], strongest="own rule (IX)")
    (6, 'own rule (IX)', '1')

    An item that the owner declined keeps its state. An item without a class stays pending.

    >>> item(["S-2"], "not admitted"), item(["S-9"])[2]
    ((4, 'standard (S-2)', 'not admitted'), 'pending')
    >>> place_item({"id": "C-01"}, [], classes, rubric)["text"]
    'C-01: pending. No source of the item has a class in section 2 of spec.md.'
    """
    ident = row["id"]
    own = row.get("strongest source", "").strip()
    if own.lower().startswith(check.OWN_RULE):
        value, origin = rubric["values"][OWN], own
    else:
        known = [s for s in sources if classes.get(s) in rubric["values"]]
        if not known:
            return {"id": ident, "state": "pending", "text": MESSAGES["no-class"].format(ident)}
        value = max(rubric["values"][classes[s]] for s in known)
        top = min(
            (classes[s] for s in known if rubric["values"][classes[s]] == value), key=check.CLASSES.index
        )
        origin = f"{top} ({', '.join(s for s in known if classes[s] == top)})"
    result = {"id": ident, "value": value, "from": origin}
    old, dimension = aspect.level_of(row.get("level"))
    if old == "not admitted":
        return result | {"state": "not admitted", "level": "not admitted"}
    rank = 1 if value >= rubric["level 1"] else 2 if value >= rubric["level 2"] else 3
    level = f"{rank}, {dimension}" if rank > 1 and dimension else str(rank)
    return result | {"state": "placed", "level": level, "rank": rank}


def place(data, rubric):
    """The result for each item that is not retired, with the position of each placed item.

    The order is by level, then by value from high to low, then by identifier.

    >>> import sample
    >>> rubric = read_rubric(pathlib.Path(__file__).with_name("rubric-items.txt"))
    >>> for r in place(sample.load(), rubric):
    ...     print(r["id"], r["value"], r["from"], "|", r["level"], r.get("position"))
    C-01 4 standard (S-01) | 1 1
    C-02 2 research (S-02) | 2, operative 4
    C-03 4 standard (S-01) | 1 2
    C-04 1 independent (S-03) | not admitted None
    C-05 4 standard (S-01) | 1 3

    A retired item is not placed.

    >>> [r["id"] for r in place(sample.load(("spec.md", "| 2, operative |", "| retired |")), rubric)]
    ['C-01', 'C-03', 'C-04', 'C-05']
    """
    classes = {s.get("id"): s.get("class", "").strip() for s in data["sources"]}
    sources = askers(data)
    results = [place_item(r, sources[r["id"]], classes, rubric) for r in check.live_items(data)]
    placed = sorted(
        (r for r in results if r["state"] == "placed"), key=lambda r: (r["rank"], -r["value"], r["id"])
    )
    for position, result in enumerate(placed, 1):
        result["position"] = position
    return sorted(results, key=lambda r: r["id"])


def line_of(result):
    """The line of the report for one result.

    >>> line_of({"id": "C-04", "state": "not admitted", "value": 1, "from": "independent (S-03)"})
    'C-04: value 1, independent (S-03), not admitted by the owner.'
    >>> line_of({"id": "C-02", "state": "pending", "text": "C-02: pending."})
    'C-02: pending.'
    """
    if result["state"] == "placed":
        r = result
        return MESSAGES["placed"].format(r["id"], r["value"], r["from"], r["level"], r["position"])
    if result["state"] == "not admitted":
        return MESSAGES["declined"].format(result["id"], result["value"], result["from"])
    return result["text"]


def write(data, results, rubric):
    r"""Fill the cells "Level" and "Strongest source" of spec.md, and the version in vetting.md.

    Returns a message for each cell that the table does not have.

    >>> import sample
    >>> rubric = read_rubric(pathlib.Path(__file__).with_name("rubric-items.txt"))
    >>> folder = sample.folder(("spec.md", "| 1 | standard (S-01) | the newest", "| pending | | the newest"))
    >>> data = aspect.load(folder)
    >>> write(data, place(data, rubric), rubric)
    []

    Only these cells change: the sample comes back.

    >>> [aspect.read_text(folder / name) == sample.FILES[name] for name in ("spec.md", "vetting.md")]
    [True, True]

    The program finds a cell by the name of its column. A row that is too short is reported.

    >>> old = " | 1 | standard (S-01) | the schedule of the program is in the repository | S-04 README;"
    >>> folder = sample.folder(("spec.md", old + " S-01 section 3 |", " |"))
    >>> data = aspect.load(folder)
    >>> write(data, place(data, rubric), rubric)[0]
    "The program cannot write the cell 'level' in line 71 of spec.md. Correct the table."
    """
    folder = pathlib.Path(data["folder"])
    by_id = {r["id"]: r for r in results}
    failed = []
    for row in check.live_items(data):
        result = by_id[row["id"]]
        cells = {"level": result.get("level", "pending"), "strongest source": result.get("from", "")}
        for name, text in cells.items():
            if not aspect.set_cell(folder / "spec.md", row["_line"], aspect.column_of(row, name), text):
                failed.append(MESSAGES["not-written"].format(name, row["_line"], "spec.md"))
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
    C-01: value 4, standard (S-01), level 1, position 1.
    C-02: value 2, research (S-02), level 2, operative, position 4.
    C-03: value 4, standard (S-01), level 1, position 2.
    C-04: value 1, independent (S-03), not admitted by the owner.
    C-05: value 4, standard (S-01), level 1, position 3.
    Ladder version 5. Items placed: 5. Items pending: 0.
    <BLANKLINE>

    The same input gives the same output. Without --write no file changes.

    >>> before = {p.name: p.read_bytes() for p in good.iterdir()}
    >>> sample.run(main, good) == (code, out, err), before == {p.name: p.read_bytes() for p in good.iterdir()}
    (True, True)

    An item whose sources have no class stays pending, and the result code is 1.

    >>> folder = sample.folder(("spec.md", "| 2024 | research |", "| 2024 | |"))
    >>> code, out, _ = sample.run(main, folder)
    >>> code, out.splitlines()[1]
    (1, 'C-02: pending. No source of the item has a class in section 2 of spec.md.')
    >>> out.splitlines()[-1]
    'Ladder version 5. Items placed: 4. Items pending: 1.'

    --write fills the cells. Files with the line end of Windows keep it, and a different line
    separator in a file does not move the write.

    >>> names = ("spec.md", "vetting.md")
    >>> windows = {n: sample.FILES[n].replace("\n", "\r\n").encode("utf-8") for n in names}
    >>> for name in names:
    ...     _ = (good / name).write_bytes(windows[name])
    >>> code, out, _ = sample.run(main, good, "--write")
    >>> code, out.splitlines()[-1], [(good / n).read_bytes() == windows[n] for n in names]
    (0, 'The program wrote the results to spec.md.', [True, True])
    >>> folder = sample.folder(
    ...     ("spec.md", "A small specification", "A small" + chr(0x2028) + "specification"),
    ...     ("vetting.md", "Rubric for sources", "Rubric" + "\x0c" + "for sources"),
    ... )
    >>> before = {p.name: p.read_bytes() for p in folder.iterdir()}
    >>> sample.run(main, folder, "--write")[0], before == {p.name: p.read_bytes() for p in folder.iterdir()}
    (0, True)

    A cell that cannot be written is reported, and the result code is 1.

    >>> old = " | 1 | standard (S-01) | the schedule of the program is in the repository | S-04 README;"
    >>> short = sample.folder(("spec.md", old + " S-01 section 3 |", " |"))
    >>> code, out, err = sample.run(main, short, "--write")
    >>> code, err, out.splitlines()[-2]
    (1, '', "The program cannot write the cell 'strongest source' in line 71 of spec.md. Correct the table.")

    --rubric gives a different ladder. Its version goes into the record.

    >>> rubric = good.parent / "rubric.txt"
    >>> text = aspect.read_text(pathlib.Path(__file__).with_name("rubric-items.txt"))
    >>> _ = rubric.write_text(text.replace("version: 5", "version: 7"), encoding="utf-8")
    >>> folder = sample.folder()
    >>> sample.run(main, folder, "--write", "--rubric", rubric)[1].splitlines()[-2]
    'Ladder version 7. Items placed: 5. Items pending: 0.'
    >>> vetting = aspect.read_text(folder / "vetting.md")
    >>> "Rubric for items: version 7." in vetting, "Rubric for sources: version 1." in vetting
    (True, True)

    A ladder or an input that cannot be read gives the result code 2.

    >>> import tempfile
    >>> _ = rubric.write_bytes(b"\xff\xfe")
    >>> code, _, err = sample.run(main, folder, "--rubric", rubric)
    >>> code, err.startswith("The ladder cannot be read:")
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
