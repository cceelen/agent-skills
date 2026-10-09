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
import pathlib
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
    "only-rejected-source": "The item rests only on independent sources that were rejected.",
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
    return {
        "rule": rule,
        "file": row.get("_file", "spec.md"),
        "line": row.get("_line", 0),
        "id": ident,
        "text": MESSAGES[rule].format(*args),
    }


def confirmed_sources(data):
    """The independent sources that the owner confirmed in vetting.md."""
    done = set()
    for row in data["vetting_sources"]:
        state = row.get("confirmed by", "").strip().lower()
        if state not in NOT_CONFIRMED:
            done.add(row.get("source", ""))
    return done


def rejected_sources(data):
    """The independent sources that a gate or the owner rejected."""
    out = set()
    for row in data["vetting_sources"]:
        state = row.get("confirmed by", "").strip().lower()
        if state == "rejected" or row.get("gates", "").strip().lower().startswith("rejected"):
            out.add(row.get("source", ""))
    return out


def check_head_and_aspect(data):
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
    out, seen = [], set()
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
    """Each source that a row cites is in section 2."""
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
    out, seen = [], set()
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
    """The fields of the recipe skill go into the rendered skill as they are."""
    out = []
    for name in ("goal", "reads first", "applies", "delegates", "stops when"):
        value = data["skill"].get(name)
        if not value or not value["value"]:
            out.append(finding("skill-field-empty", value or {}, "", name))
        elif re.search(r"\bsection \d|\b\d\.\d\b", value["value"]):
            out.append(finding("skill-refers-to-section", value, "", name))
    return out


def live_items(data):
    """The items that are not retired."""
    return [r for r in data["checklist"] if aspect.level_of(r.get("level"))[0] != "retired"]


def check_support(data):
    """An item must rest on a source that was read, and not only on rejected sources.

    Returns the findings and the items that wait for the vetting of their only sources.
    """
    out, waiting = [], []
    sources = {s.get("id"): s for s in data["sources"]}
    confirmed, rejected = confirmed_sources(data), rejected_sources(data)
    for row in live_items(data):
        cited = row.get("source", "")
        ids = [i for i in aspect.source_ids(cited) if i in sources]
        if not ids or aspect.principles(cited):
            continue
        if all(sources[i].get("read") == "no" for i in ids):
            out.append(finding("only-unread-source", row, row["id"]))
        elif all(sources[i].get("class") == "independent" and i not in confirmed for i in ids):
            if all(i in rejected for i in ids):
                out.append(finding("only-rejected-source", row, row["id"]))
            else:
                waiting.append(row["id"])
    return out, sorted(waiting)


def check_words(data, words):
    out = []
    for row in live_items(data):
        for word in words:
            if re.search(rf"(?<!\w){re.escape(word)}(?!\w)", row.get("item", ""), re.I):
                out.append(finding("product-word", row, row.get("id", ""), word))
    return out


def compare_previous(data, previous_rows):
    """Findings for removed and reused identifiers, and the identifiers whose text changed."""
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
    """All findings, sorted, and what remains."""
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
    return data["head"].get("accepted", "pending").strip().lower() not in ("", "pending")


def report(data, found, remains, previous_given):
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
    if flag in args:
        i = args.index(flag)
        value = args[i + 1] if i + 1 < len(args) else ""
        del args[i : i + 2]
        return value
    return None


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        sys.exit(__doc__)
    previous, words_file = option(args, "--previous"), option(args, "--words")
    as_json = "--json" in args
    folder = next((a for a in args if not a.startswith("--")), "")
    try:
        data = aspect.load(folder)
        previous_rows = None
        if previous is not None:
            doc = aspect.Doc(previous)
            previous_rows = doc.table(doc.section("4"), "id")
        words = []
        if words_file is not None:
            text = pathlib.Path(words_file).read_text(encoding="utf-8")
            words = sorted({w.strip() for w in text.splitlines() if w.strip()})
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
