#!/usr/bin/env python3
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Check of one aspect specification and its evidence record. Standard library only.

  check.py SPEC [--previous FILE] [--words FILE] [--json]

  SPEC             the folder with spec.md, evidence.md and, if present, vetting.md
  --previous FILE  an earlier revision of spec.md, for the check of stable identifiers
  --words FILE     the product words of the aspect, one in each line; an item must not use one
  --json           print one JSON object in place of the text report

The report lists each failing rule with its place, then what remains. Result code 0: no rule
fails. Result code 1: a rule fails. Result code 2: the input cannot be read. Pending levels,
pending vettings, changed items and a missing acceptance remain; they do not fail the check.
"""

import json
import re
import sys

import aspect

CLASSES = ("standard", "foundation", "vendor", "research", "trusted-data", "independent")
READ = ("full", "part", "no")
SOURCE_CELLS = ("id", "source", "issuer", "version or date", "class", "license", "read", "url")
ASPECT_FIELDS = ("aspect", "field and disciplines", "contexts", "boundaries", "agreed with the owner on")
DATE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
NOT_CONFIRMED = ("", "pending", "rejected")

MESSAGES = {
    "accepted-missing": "The head line has no field Accepted.",
    "aspect-field-empty": "The field '{0}' of section 1 is empty.",
    "agreed-without-date": "The field 'Agreed with the owner on' has no date.",
    "risk-dimensions-missing": "Section 1 names no risk dimension.",
    "risk-dimension-empty": "The risk dimension '{0}' has no question.",
    "source-cell-empty": "The cell '{0}' of the source is empty.",
    "source-without-version": "The source has no version and no date.",
    "class-unknown": "The class '{0}' is not one of the six classes.",
    "read-unknown": "The cell Read is '{0}'. Use full, part or no.",
    "source-id-twice": "The identifier of the source is used two times.",
    "item-id-twice": "The identifier of the item is used two times.",
    "unknown-source": "The row cites '{0}'. Section 2 does not list this source.",
    "item-without-source": "The item cites no source and no principle of the constitution.",
    "check-empty": "The item names no check. Write a check or 'judgement'.",
    "why-empty": "The item does not name the risk that it answers.",
    "level-unknown": "The level '{0}' is not permitted.",
    "level-without-dimension": "The item is above level 1 and names no risk dimension.",
    "dimension-unknown": "The risk dimension '{0}' is not in section 1.",
    "no-evidence-row": "The evidence record has no row for the source '{0}'.",
    "evidence-does-not-name-item": "The evidence row of '{0}' does not name this item.",
    "evidence-without-date": "The evidence row has no date in the cell Read.",
    "no-disagreement-section": "Section 3.4 is absent or empty. Write the disagreements or 'none found'.",
    "glossary-cell-empty": "The cell '{0}' of the glossary term is empty.",
    "decision-without-date": "The decision has no date.",
    "watch-list-empty": "The watch list has no row.",
    "only-unread-source": "The item rests only on sources that were not read.",
    "only-rejected-source": "Each source of the item was rejected or was not read.",
    "sources-empty": "Section 2 lists no source.",
    "checklist-empty": "The checklist of section 4 has no item.",
    "product-word": "The item uses the product word '{0}'.",
    "id-removed": "The earlier revision has this item. Keep the row and set its level to 'retired'.",
    "id-reused": "The earlier revision retired this identifier. Use a new identifier.",
    "skill-field-empty": "The field '{0}' of the recipe skill in section 5 is empty.",
    "skill-refers-to-section": "The field '{0}' of the recipe skill refers to a section of spec.md.",
    "no-failure": "No check fails.",
    "failures": "Failing checks: {0}.",
    "remains-head": "What remains:",
    "remains-levels": "Levels that are pending: {0}.",
    "remains-vettings": "Vettings that are pending: {0}.",
    "remains-waiting": "Items that rest only on sources with a pending vetting: {0}.",
    "remains-judgement": "Items that need judgement: {0}.",
    "remains-changed": "Items with a changed text. Make sure that the meaning is the same: {0}.",
    "remains-accepted": "The owner did not accept the specification.",
    "accepted": "Accepted: {0}.",
    "previous-skipped": "The check of stable identifiers was skipped: no earlier revision was given.",
    "unreadable": "The input cannot be read: {0}",
}


def finding(rule, row, ident="", *args):
    """One finding: the rule, the place of the row, the identifier and the text for the person.

    >>> finding("unknown-source", {"_file": "spec.md", "_line": 56}, "C-02", "S-09")["text"]
    "The row cites 'S-09'. Section 2 does not list this source."
    >>> finding("watch-list-empty", {})["file"], finding("watch-list-empty", {})["line"]
    ('spec.md', 0)

    Each text is in Simplified Technical English: a sentence has 25 words or less.

    >>> aspect.long_sentences(MESSAGES)
    []
    """
    return {
        "rule": rule,
        "file": row.get("_file", "spec.md"),
        "line": row.get("_line", 0),
        "id": ident,
        "text": MESSAGES[rule].format(*args),
    }


def brief(findings):
    """The rule and the row of each finding: a short view for a person or an example.

    >>> brief([finding("check-empty", {}, "C-02"), finding("watch-list-empty", {})])
    [('check-empty', 'C-02'), ('watch-list-empty', '')]
    """
    return [(f["rule"], f["id"]) for f in findings]


def confirmed_sources(data):
    """The independent sources that the owner confirmed in vetting.md.

    >>> import sample
    >>> sorted(confirmed_sources(sample.load()))
    ['S-03', 'S-04']
    >>> pending = ("vetting.md", sample.CONFIRMED_S03, "| 9 of 10 | 2026-01-10 | pending |")
    >>> sorted(confirmed_sources(sample.load(pending)))
    ['S-04']

    A new rejection by a gate is stronger than an earlier confirmation.

    >>> gate = ("vetting.md", "| S-03 | page | pass |", "| S-03 | page | rejected: no date |")
    >>> sorted(confirmed_sources(sample.load(gate)))
    ['S-04']
    """
    done = set()
    for row in data["vetting_sources"]:
        state = row.get("confirmed by", "").strip().lower()
        # A new rejection by a gate is stronger than an earlier confirmation.
        if state not in NOT_CONFIRMED and not row.get("gates", "").strip().lower().startswith("rejected"):
            done.add(row.get("source", ""))
    return done


def rejected_sources(data):
    """The independent sources that a gate or the owner rejected.

    >>> import sample
    >>> rejected_sources(sample.load())
    set()
    >>> owner = ("vetting.md", sample.CONFIRMED_S03, "| 9 of 10 | 2026-01-10 | rejected |")
    >>> gate = ("vetting.md", "| S-04 | repository | pass |", "| S-04 | repository | rejected: no date |")
    >>> sorted(rejected_sources(sample.load(owner, gate)))
    ['S-03', 'S-04']
    """
    out = set()
    for row in data["vetting_sources"]:
        state = row.get("confirmed by", "").strip().lower()
        if state == "rejected" or row.get("gates", "").strip().lower().startswith("rejected"):
            out.add(row.get("source", ""))
    return out


def check_head_and_aspect(data):
    r"""The head line and section 1: the acceptance field, each field, the risk dimensions.

    >>> import sample
    >>> check_head_and_aspect(sample.load())
    []
    >>> brief(check_head_and_aspect(sample.load(("spec.md", " | **Accepted**: A. Person, 2026-01-15", ""))))
    [('accepted-missing', '')]
    >>> old = "- **Boundaries**: the recovery of a complete site belongs to a different aspect."
    >>> check_head_and_aspect(sample.load(("spec.md", old, "- **Boundaries**:")))[0]["text"]
    "The field 'boundaries' of section 1 is empty."
    >>> date = ("spec.md", "2026-01-05; a recipe for", "in January; a recipe for")
    >>> brief(check_head_and_aspect(sample.load(date)))
    [('agreed-without-date', '')]

    Each risk dimension needs a name and a question. A specification without one fails.

    >>> old = "  - `operative`: Can a lost record be made again? Opinion: if not, go past level 1."
    >>> brief(check_head_and_aspect(sample.load(("spec.md", old, "  - `operative`:"))))
    [('risk-dimension-empty', 'operative')]
    >>> regulatory = "  - `regulatory`: Is personal data in the backup? Opinion: if yes, aim for level 3.\n"
    >>> brief(check_head_and_aspect(sample.load(("spec.md", old + "\n", ""), ("spec.md", regulatory, ""))))
    [('risk-dimensions-missing', '')]
    """
    out, head = [], data["head"]
    if "accepted" not in head:
        out.append(finding("accepted-missing", head))
    for name in ASPECT_FIELDS:
        field = data["aspect"].get(name)
        if not field or not field["value"]:
            out.append(finding("aspect-field-empty", field or {}, "", name))
    agreed = data["aspect"].get("agreed with the owner on")
    if agreed and agreed["value"] and not DATE.search(agreed["value"]):
        out.append(finding("agreed-without-date", agreed))
    if not data["risk_dimensions"]:
        out.append(finding("risk-dimensions-missing", data["aspect"].get("risk dimensions", {})))
    for dim in data["risk_dimensions"]:
        if not dim["text"]:
            out.append(finding("risk-dimension-empty", dim, dim["name"], dim["name"]))
    return out


def check_sources(data):
    """Section 2: each cell is filled, the class and the cell Read are known, each identifier is new.

    >>> import sample
    >>> check_sources(sample.load())
    []
    >>> brief(check_sources(sample.load(("spec.md", "| Example Journal |", "| |"))))
    [('source-cell-empty', 'S-02')]
    >>> brief(check_sources(sample.load(("spec.md", "| 2.0, 2025-03 |", "| |"))))
    [('source-without-version', 'S-01')]
    >>> brief(check_sources(sample.load(("spec.md", "| 2024 | research |", "| 2024 | paper |"))))
    [('class-unknown', 'S-02')]
    >>> brief(check_sources(sample.load(("spec.md", "| CC BY 4.0 | full |", "| CC BY 4.0 | yes |"))))
    [('read-unknown', 'S-02')]
    >>> brief(check_sources(sample.load(("spec.md", "| S-02 | A study", sample.SOURCE_ROW))))
    [('source-id-twice', 'S-01')]

    A specification without a source fails.

    >>> data = sample.load()
    >>> data["sources"] = []
    >>> brief(check_sources(data))
    [('sources-empty', '')]
    """
    out, seen = [], set()
    if not data["sources"]:
        out.append(finding("sources-empty", {}))
    for row in data["sources"]:
        ident = row.get("id", "")
        for cell in SOURCE_CELLS:
            if not row.get(cell, ""):
                rule = "source-without-version" if cell == "version or date" else "source-cell-empty"
                out.append(finding(rule, row, ident, cell))
        if row.get("class") and row["class"] not in CLASSES:
            out.append(finding("class-unknown", row, ident, row["class"]))
        if row.get("read") and row["read"] not in READ:
            out.append(finding("read-unknown", row, ident, row["read"]))
        if ident in seen:
            out.append(finding("source-id-twice", row, ident))
        seen.add(ident)
    return out


def check_references(data):
    r"""Each source that a row cites is in section 2.

    >>> import sample
    >>> check_references(sample.load())
    []
    >>> found = check_references(sample.load(("spec.md", "| S-02 section 4 |", "| S-09 section 4 |")))
    >>> brief(found), found[0]["line"], found[0]["text"]
    ([('unknown-source', 'C-02')], 56, "The row cites 'S-09'. Section 2 does not list this source.")

    The rows of the strategy are checked also.

    >>> strategy = ("spec.md", "| S-01 section 3 |\n\n### 3.4", "| S-08 |\n\n### 3.4")
    >>> brief(check_references(sample.load(strategy)))
    [('unknown-source', '')]
    """
    known = {s.get("id") for s in data["sources"]}
    out = []
    rows = [(r, r.get("source", ""), r.get("id", "")) for r in data["checklist"]]
    rows += [(r, r.get("sources", ""), "") for r in data["context_decisions"] + data["disagreement"]]
    for row, cell, ident in rows:
        for sid in aspect.source_ids(cell):
            if sid not in known:
                out.append(finding("unknown-source", row, ident, sid))
    return out


def check_items(data):
    """Section 4: each item has a source or a principle, a check, a risk and a permitted level.

    >>> import sample
    >>> check_items(sample.load())
    []
    >>> brief(check_items(sample.load(("spec.md", "| S-02 section 4 |", "| a talk |"))))
    [('item-without-source', 'C-02')]
    >>> brief(check_items(sample.load(("spec.md", "| the record of the last restore has a date |", "| |"))))
    [('check-empty', 'C-02')]
    >>> why = "| Risk: a backup that cannot be restored is found too late. |"
    >>> brief(check_items(sample.load(("spec.md", why, "| |"))))
    [('why-empty', 'C-02')]

    The level is 1, or 2 or 3 with a risk dimension of section 1, or a state.

    >>> for level in ("high", "2", "2, commercial", "pending", "retired"):
    ...     print(level, brief(check_items(sample.load(("spec.md", "| 2, operative |", f"| {level} |")))))
    high [('level-unknown', 'C-02')]
    2 [('level-without-dimension', 'C-02')]
    2, commercial [('dimension-unknown', 'C-02')]
    pending []
    retired []

    An identifier is used one time. A retired item is not checked. A checklist needs an item.

    >>> brief(check_items(sample.load(("spec.md", "| C-02 | A restore", "| C-01 | A restore"))))
    [('item-id-twice', 'C-01')]
    >>> old = "| 2, operative | authority (1) | the record of the last restore has a date |"
    >>> check_items(sample.load(("spec.md", old, "| retired | authority (1) | |")))
    []
    >>> data = sample.load()
    >>> data["checklist"] = []
    >>> brief(check_items(data))
    [('checklist-empty', '')]
    """
    out, seen = [], set()
    if not live_items(data):
        out.append(finding("checklist-empty", {}))
    dimensions = {d["name"] for d in data["risk_dimensions"]}
    for row in data["checklist"]:
        ident = row.get("id", "")
        if ident in seen:
            out.append(finding("item-id-twice", row, ident))
        seen.add(ident)
        level, dimension = aspect.level_of(row.get("level"))
        if level == "retired":
            continue
        cited = row.get("source", "")
        if not aspect.source_ids(cited) and not aspect.principles(cited):
            out.append(finding("item-without-source", row, ident))
        if not row.get("check", ""):
            out.append(finding("check-empty", row, ident))
        if not row.get("why", ""):
            out.append(finding("why-empty", row, ident))
        if level is None:
            out.append(finding("level-unknown", row, ident, row.get("level", "")))
        elif level in (2, 3) and not dimension:
            out.append(finding("level-without-dimension", row, ident))
        elif dimension and dimension not in dimensions:
            out.append(finding("dimension-unknown", row, ident, dimension))
    return out


def check_evidence(data):
    """The evidence record: a row for each cited source, the item in the row, a date in the row.

    >>> import sample
    >>> check_evidence(sample.load())
    []
    >>> absent = ("evidence.md", "| S-03 | A written review", "| S-07 | A written review")
    >>> brief(check_evidence(sample.load(absent)))
    [('no-evidence-row', 'C-04')]
    >>> old, new = '| "After the drill" | C-04 |', '| "After the drill" | 3.3 frequency |'
    >>> brief(check_evidence(sample.load(("evidence.md", old, new))))
    [('evidence-does-not-name-item', 'C-04')]
    >>> undated = ("evidence.md", "| README | C-05 | 2026-01-10 |", "| README | C-05 | yes |")
    >>> brief(check_evidence(sample.load(undated)))
    [('evidence-without-date', 'S-04')]

    A source that section 2 does not list is the finding of check_references, not of this rule.

    >>> check_evidence(sample.load(("spec.md", "| S-02 section 4 |", "| S-09 section 4 |")))
    []
    """
    out = []
    rows = {e.get("source"): e for e in data["evidence"]}
    known = {s.get("id") for s in data["sources"]}
    for row in data["evidence"]:
        if not DATE.search(row.get("read", "")):
            out.append(finding("evidence-without-date", row, row.get("source", "")))
    for row in live_items(data):
        for sid in aspect.source_ids(row.get("source", "")):
            if sid not in known:
                continue  # check_references reports it
            if sid not in rows:
                out.append(finding("no-evidence-row", row, row["id"], sid))
            elif row["id"] not in aspect.item_ids(rows[sid].get("supports", "")):
                out.append(finding("evidence-does-not-name-item", rows[sid], row["id"], sid))
    return out


def check_other_sections(data):
    r"""Sections 3.4, 6, 7 and 8: the disagreements, the watch list, the decisions, the glossary.

    >>> import sample
    >>> check_other_sections(sample.load())
    []
    >>> heading = ("spec.md", "### 3.4 Where the sources", "### Where the sources")
    >>> brief(check_other_sections(sample.load(heading)))
    [('no-disagreement-section', '')]

    A section 3.4 without a row is correct when it says "none found".

    >>> row = "| Whether one copy is sufficient | One source accepts one copy with a restore test."
    >>> row += " One source wants a second place. | One copy is level 1; the second place is above it."
    >>> row += " | S-01, S-02 |\n"
    >>> brief(check_other_sections(sample.load(("spec.md", row, "")))), check_other_sections(
    ...     sample.load(("spec.md", row, "None found.\n"))
    ... )
    ([('no-disagreement-section', '')], [])
    >>> watch = "| A new version of S-01 | the page of the issuer | at each refresh |\n"
    >>> brief(check_other_sections(sample.load(("spec.md", watch, ""))))
    [('watch-list-empty', '')]
    >>> undated = ("spec.md", "| 2026-01-05 | The recipe is", "| January | The recipe is")
    >>> brief(check_other_sections(sample.load(undated)))
    [('decision-without-date', '')]
    >>> meaning = "| a copy that is kept to make lost data again |"
    >>> brief(check_other_sections(sample.load(("spec.md", meaning, "| |"))))
    [('glossary-cell-empty', 'backup')]
    """
    out = []
    if "3.4" not in data["sections"] or not (
        data["disagreement"] or "none found" in data["disagreement_text"].lower()
    ):
        out.append(finding("no-disagreement-section", {}))
    for row in data["glossary"]:
        for cell in ("term", "meaning here"):
            if not row.get(cell, ""):
                out.append(finding("glossary-cell-empty", row, row.get("term", ""), cell))
    for row in data["decisions"]:
        if not DATE.fullmatch(row.get("date", "")):
            out.append(finding("decision-without-date", row))
    if not data["watch"]:
        out.append(finding("watch-list-empty", {}))
    return out


def check_skill(data):
    """The fields of the recipe skill go into the rendered skill as they are.

    Thus each field is filled and does not refer to a section of the specification.

    >>> import sample
    >>> check_skill(sample.load())
    []
    >>> brief(check_skill(sample.load(("spec.md", sample.APPLIES, "- **Applies**:"))))
    [('skill-field-empty', '')]
    >>> section = ("spec.md", sample.APPLIES, "- **Applies**: the strategy of section 3.")
    >>> found = check_skill(sample.load(section))
    >>> found[0]["text"]
    "The field 'applies' of the recipe skill refers to a section of spec.md."
    """
    out = []
    for name in ("goal", "reads first", "applies", "delegates", "stops when"):
        value = data["skill"].get(name)
        if not value or not value["value"]:
            out.append(finding("skill-field-empty", value or {}, "", name))
        elif re.search(r"\bsection \d|\b\d\.\d\b", value["value"]):
            out.append(finding("skill-refers-to-section", value, "", name))
    return out


def live_items(data):
    """The items that are not retired.

    >>> import sample
    >>> [r["id"] for r in live_items(sample.load(("spec.md", "| 2, operative |", "| retired |")))]
    ['C-01', 'C-03', 'C-04', 'C-05']
    """
    return [r for r in data["checklist"] if aspect.level_of(r.get("level"))[0] != "retired"]


def check_support(data):
    """An item must rest on a source that was read, and not only on rejected sources.

    Returns the findings and the items that wait for the vetting of their only sources.

    >>> import sample
    >>> check_support(sample.load())
    ([], [])
    >>> found, waiting = check_support(sample.load(("spec.md", "| CC BY 4.0 | full |", "| CC BY 4.0 | no |")))
    >>> brief(found), waiting
    ([('only-unread-source', 'C-02')], [])

    C-04 rests on the independent source S-03 only. While the owner did not confirm S-03, the
    item waits: this is not a failure, because only the owner can end that state.

    >>> pending = ("vetting.md", sample.CONFIRMED_S03, "| 9 of 10 | 2026-01-10 | pending |")
    >>> check_support(sample.load(pending))
    ([], ['C-04'])
    >>> rejected = ("vetting.md", sample.CONFIRMED_S03, "| 9 of 10 | 2026-01-10 | rejected |")
    >>> brief(check_support(sample.load(rejected))[0])
    [('only-rejected-source', 'C-04')]

    A second source that was not read does not help the item.

    >>> more = ("spec.md", '| S-03 "After the drill" |', '| S-03 "After the drill"; S-02 section 9 |')
    >>> unread = ("spec.md", "| CC BY 4.0 | full |", "| CC BY 4.0 | no |")
    >>> found, waiting = check_support(sample.load(more, unread, pending))
    >>> brief(found), waiting
    ([('only-unread-source', 'C-02')], ['C-04'])

    An item that cites a principle of the constitution is an own rule and needs no source.

    >>> own = ("spec.md", '| S-03 "After the drill" |', '| constitution IX; S-03 "After the drill" |')
    >>> check_support(sample.load(own, rejected))
    ([], [])
    """
    out, waiting = [], []
    sources = {s.get("id"): s for s in data["sources"]}
    confirmed, rejected = confirmed_sources(data), rejected_sources(data)
    for row in live_items(data):
        cited = row.get("source", "")
        ids = [i for i in aspect.source_ids(cited) if i in sources]
        if not ids or aspect.principles(cited):
            continue
        read = [i for i in ids if sources[i].get("read") != "no"]
        usable = [i for i in read if sources[i].get("class") != "independent" or i in confirmed]
        if usable:
            continue
        if not read:
            out.append(finding("only-unread-source", row, row["id"]))
        elif any(i not in rejected for i in read):
            waiting.append(row["id"])  # an independent source that was read waits for its vetting
        else:
            out.append(finding("only-rejected-source", row, row["id"]))
    return out, sorted(waiting)


def check_words(data, words):
    """An item must not use a product word of the aspect.

    >>> import sample
    >>> brief(check_words(sample.load(), ["Restic", "program"]))
    [('product-word', 'C-05')]
    >>> check_words(sample.load(), ["gram"]), check_words(sample.load(), [])
    ([], [])
    """
    out = []
    for row in live_items(data):
        for word in words:
            if re.search(rf"(?<!\w){re.escape(word)}(?!\w)", row.get("item", ""), re.I):
                out.append(finding("product-word", row, row.get("id", ""), word))
    return out


def compare_previous(data, previous_rows):
    """Findings for removed and reused identifiers, and the identifiers whose text changed.

    In the earlier revision of this example, C-02 had a different text, C-05 was retired, and an
    item C-06 existed.

    >>> import sample
    >>> now = sample.load()
    >>> earlier = [dict(row) for row in now["checklist"]]
    >>> earlier[1]["item"], earlier[4]["level"] = "A restore was done.", "retired"
    >>> earlier.append({"id": "C-06", "item": "An old item.", "level": "1"})
    >>> found, changed = compare_previous(now, earlier)
    >>> sorted(brief(found)), changed
    ([('id-removed', 'C-06'), ('id-reused', 'C-05')], ['C-02'])

    The same revision gives nothing.

    >>> compare_previous(now, now["checklist"])
    ([], [])
    """
    out, changed = [], []
    now = {r.get("id"): r for r in data["checklist"]}
    for old in previous_rows:
        ident = old.get("id")
        new = now.get(ident)
        was_retired = aspect.level_of(old.get("level"))[0] == "retired"
        if new is None:
            out.append(finding("id-removed", {"_file": "spec.md", "_line": 0}, ident))
        elif was_retired and aspect.level_of(new.get("level"))[0] != "retired":
            out.append(finding("id-reused", new, ident))
        elif not was_retired and new.get("item") != old.get("item"):
            changed.append(ident)
    return out, sorted(changed)


def run_checks(data, previous_rows=None, words=()):
    """All findings, sorted, and what remains.

    >>> import sample
    >>> found, remains = run_checks(sample.load())
    >>> found, remains
    ([], {'levels': [], 'vettings': [], 'waiting': [], 'judgement': ['C-04'], 'changed': []})

    What remains does not fail the check: a pending level, a pending vetting, a changed text.

    >>> level = ("spec.md", "| 2, operative |", "| pending |")
    >>> vetting = ("vetting.md", sample.CONFIRMED_S04, "| 8 of 10 | 2026-01-10 | pending |")
    >>> found, remains = run_checks(sample.load(level, vetting))
    >>> found, remains["levels"], remains["vettings"]
    ([], ['C-02'], ['S-04'])

    The findings of all rules come in the order of the file and the line.

    >>> level, cell = ("spec.md", "| 2, operative |", "| high |"), ("spec.md", "| Example Journal |", "| |")
    >>> two = sample.load(level, cell)
    >>> [(f["line"], f["rule"]) for f in run_checks(two, None, ["program"])[0]]
    [(24, 'source-cell-empty'), (56, 'level-unknown'), (59, 'product-word')]
    """
    support, waiting = check_support(data)
    found = (
        check_head_and_aspect(data)
        + check_sources(data)
        + check_references(data)
        + check_items(data)
        + check_evidence(data)
        + check_other_sections(data)
        + check_skill(data)
        + support
        + check_words(data, words)
    )
    changed = []
    if previous_rows is not None:
        more, changed = compare_previous(data, previous_rows)
        found += more
    found.sort(key=lambda f: (f["file"], f["line"], f["rule"], f["id"], f["text"]))
    confirmed = confirmed_sources(data)
    live = live_items(data)
    remains = {
        "levels": sorted(r["id"] for r in live if aspect.level_of(r.get("level"))[0] == "pending"),
        "vettings": sorted(
            s["id"] for s in data["sources"] if s.get("class") == "independent" and s["id"] not in confirmed
        ),
        "waiting": waiting,
        "judgement": sorted(r["id"] for r in live if r.get("check", "").strip().lower() == "judgement"),
        "changed": changed,
    }
    return found, remains


def is_accepted(data):
    """The head line names the person and the date of the acceptance.

    >>> [is_accepted({"head": {"accepted": v}}) for v in ("A. Person, 2026-01-15", "pending", "no")]
    [True, False, False]
    >>> [is_accepted({"head": {"accepted": v}}) for v in ("A. Person", "2026-01-15", "")]
    [False, False, False]
    >>> is_accepted({"head": {}})
    False
    """
    value = data["head"].get("accepted", "pending").strip()
    return value.lower() != "pending" and bool(DATE.search(value)) and bool(DATE.sub("", value).strip(" ,;"))


def read_words(path):
    r"""The words of a word list file, sorted, or [] without a file.

    >>> import sample
    >>> path = sample.folder() / "words.txt"
    >>> _ = path.write_text("program\n\n Restic \nprogram\n", encoding="utf-8")
    >>> read_words(path), read_words(None)
    (['Restic', 'program'], [])
    """
    if path is None:
        return []
    return sorted({w.strip() for w in aspect.read_text(path).splitlines() if w.strip()})


def report(data, found, remains, previous_given):
    """The text report: each failing rule with its place, then what remains.

    >>> import sample
    >>> data = sample.load()
    >>> print(report(data, *run_checks(data), previous_given=False))
    No check fails.
    What remains:
    - Items that need judgement: C-04.
    Accepted: A. Person, 2026-01-15.
    The check of stable identifiers was skipped: no earlier revision was given.

    >>> data = sample.load(
    ...     ("spec.md", "| S-02 section 4 |", "| S-09 section 4 |"),
    ...     ("spec.md", "**Accepted**: A. Person, 2026-01-15", "**Accepted**: pending"),
    ...     ("spec.md", "| judgement |", "| the review is in the record |"),
    ... )
    >>> print(report(data, *run_checks(data, data["checklist"]), previous_given=True))
    FAIL unknown-source spec.md:56 C-02: The row cites 'S-09'. Section 2 does not list this source.
    Failing checks: 1.
    What remains:
    - The owner did not accept the specification.

    When nothing remains, the report is short.

    >>> data = sample.load(("spec.md", "| judgement |", "| the review is in the record |"))
    >>> print(report(data, *run_checks(data, data["checklist"]), previous_given=True))
    No check fails.
    Accepted: A. Person, 2026-01-15.
    """
    lines = [
        f"FAIL {f['rule']} {f['file']}:{f['line']} {f['id']}: {f['text']}".replace(" : ", ": ") for f in found
    ]
    lines.append(MESSAGES["failures"].format(len(found)) if found else MESSAGES["no-failure"])
    rest = [MESSAGES[f"remains-{key}"].format(", ".join(ids)) for key, ids in remains.items() if ids]
    if not is_accepted(data):
        rest.append(MESSAGES["remains-accepted"])
    if rest:
        lines += [MESSAGES["remains-head"], *("- " + r for r in rest)]
    if is_accepted(data):
        lines.append(MESSAGES["accepted"].format(data["head"]["accepted"]))
    if not previous_given:
        lines.append(MESSAGES["previous-skipped"])
    return "\n".join(lines)


def option(args, flag):
    """Take an option and its value out of the arguments. Returns the value, or None.

    >>> args = ["folder", "--words", "w.txt", "--json"]
    >>> option(args, "--words"), args
    ('w.txt', ['folder', '--json'])
    >>> option(args, "--previous"), option(["--words"], "--words")
    (None, '')
    """
    if flag in args:
        i = args.index(flag)
        value = args[i + 1] if i + 1 < len(args) else ""
        del args[i : i + 2]
        return value
    return None


def main(argv=None):
    r"""The command line. See the text at the start of this file.

    >>> import sample
    >>> good = sample.folder()
    >>> code, out, err = sample.run(main, good)
    >>> code, out.splitlines()[0], err
    (0, 'No check fails.', '')

    A failing rule gives the result code 1. The same input gives the same output.

    >>> bad = sample.folder(("spec.md", "| S-02 section 4 |", "| S-09 section 4 |"))
    >>> code, out, _ = sample.run(main, bad)
    >>> code, out.splitlines()[1]
    (1, 'Failing checks: 1.')
    >>> sample.run(main, bad) == sample.run(main, bad)
    True

    --json gives the same content as one object with sorted keys.

    >>> result = json.loads(sample.run(main, bad, "--json")[1])
    >>> sorted(result), brief(result["findings"]), result["accepted"]
    (['accepted', 'findings', 'previous', 'remains'], [('unknown-source', 'C-02')], True)

    --previous compares with an earlier revision, and --words finds product words.

    >>> earlier = good.parent / "earlier.md"
    >>> _ = earlier.write_text(sample.SPEC.replace("was done and recorded.", "was done."), encoding="utf-8")
    >>> words = good.parent / "words.txt"
    >>> _ = words.write_text("program\n", encoding="utf-8")
    >>> code, out, _ = sample.run(main, good, "--previous", earlier, "--words", words, "--json")
    >>> result = json.loads(out)
    >>> code, brief(result["findings"]), result["remains"]["changed"], result["previous"]
    (1, [('product-word', 'C-05')], ['C-02'], True)

    Input that cannot be read gives the result code 2. No argument prints the usage text.

    >>> import tempfile
    >>> code, out, err = sample.run(main, tempfile.mkdtemp(prefix="sota-empty-"))
    >>> code, out, err.startswith("The input cannot be read:")
    (2, '', True)
    >>> _ = words.write_bytes(b"\xff\xfe")
    >>> sample.run(main, good, "--words", words)[0], sample.run(main, good, "--previous", words)[0]
    (2, 2)
    >>> code, _, err = sample.run(main)
    >>> code, "check.py SPEC" in err
    (2, True)
    """
    args = list(sys.argv[1:] if argv is None else argv)
    if args[:1] == ["--selftest"]:
        sys.exit(aspect.selftest())
    if not args or args[0] in ("-h", "--help"):
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    previous, words_file = option(args, "--previous"), option(args, "--words")
    as_json = "--json" in args
    folder = next((a for a in args if not a.startswith("--")), "")
    try:
        data = aspect.load(folder)
        previous_rows = None
        if previous is not None:
            doc = aspect.Doc(previous)
            previous_rows = doc.table(doc.section("4"), "id")
        words = read_words(words_file)
    except (aspect.Unreadable, OSError) as e:
        print(MESSAGES["unreadable"].format(e), file=sys.stderr)
        sys.exit(2)
    found, remains = run_checks(data, previous_rows, words)
    if as_json:
        result = {
            "accepted": is_accepted(data),
            "findings": found,
            "previous": previous is not None,
            "remains": remains,
        }
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(report(data, found, remains, previous is not None))
    sys.exit(1 if found else 0)


if __name__ == "__main__":
    main()
