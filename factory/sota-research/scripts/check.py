#!/usr/bin/env python3
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Check of one aspect specification and its evidence record. Standard library only.

  check.py SPEC [--previous FILE] [--words FILE] [--json]
  check.py SPEC --scope

  SPEC             the folder with spec.md, evidence.md and, if present, vetting.md and trial.md
  --previous FILE  an earlier revision of spec.md, for the check of stable identifiers
  --words FILE     the product words of the aspect, one in each line; an item must not use one
  --json           print one JSON object in place of the text report
  --scope          check only what is settled before the research: the head line, the aspect,
                   the field, the intent of the owner, the date of the agreement and the form of
                   the charter. Use this in phase 1.

The report lists each failing rule with its place, then what remains. Result code 0: no rule
fails. Result code 1: a rule fails. Result code 2: the input cannot be read. Pending levels,
pending vettings, changed items, open findings of a trial, a recipe without a trial, an intent of
the owner that was not asked, a specification without a charter, a charter that the owner did not
review and a missing acceptance remain; they do not fail the check.

The intent of the owner is a field of section 1. It has one line for each answer of the owner: a
quote with its date, or "(no answer)".

The report gives one line for the answers of risk and reward in the table "Items" of vetting.md:
how many name a source and how many say "judgement". This line is for the review. It fails nothing.

Each item names one view of section 1. A view is a set of concerns of the aspect. Each view needs
an item, and an item on level 1 when no level is pending. The report gives the items of each view.

Section 1 names the stakeholders of the aspect, each with its concerns and its source. Each view
names its stakeholders in the form "(stakeholders: a, b)". A stakeholder that is in no view remains.

The table "Requirements" of vetting.md is the register of the requirements: one row for each
requirement that a source states for a stakeholder. The cell "Goes to" of a row has one of these
forms, and no other:

  C-<nn>              the checklist item that holds the requirement
  3.3: <decision>     a decision that depends on context; the cell Decision of its row in section 3.3
  5                   knowledge of one product, for an implementation skill
  boundary: <name>    a neighbouring aspect owns the requirement; a boundary of section 1 that
                      the owner decided
  duplicate: R-<nn>   the same requirement from a second source; a row that is not a duplicate

Each item that is not retired holds a requirement, or its cell "Admitted by" is "own rule". Each
stakeholder of section 1 has a requirement. The report gives the requirements of each view by
their exit. A view with more than half of its requirements at a boundary remains.

Each boundary of section 1 has a state in its line: "(proposed)", or "(decided by the owner on
<YYYY-MM-DD>)". A line without a state is proposed. Only the owner decides a boundary. A
requirement that goes to a boundary that the owner did not decide fails. The table "Proposed
boundaries" of vetting.md has one row for each proposed boundary: the boundary, the requirements
of the register that it would take, the stakeholders that it would leave with no requirement, and
the reason. A proposed boundary without a row fails. A row for a boundary that section 1 does not
have or that the owner decided fails. A row that names a requirement that the register does not
have fails. Each proposed boundary remains, with the number of requirements that it would take.
Each stakeholder that a proposed boundary would leave with no requirement in the aspect remains.

The file charter.md beside spec.md is the charter of the aspect: the target, the principles with
their priority and the constraints of the owner. It governs the triage. The file is optional: a
specification without it remains, and no rule of the charter applies. The head line of the charter
has the state: "draft", or "reviewed by the owner on <YYYY-MM-DD>". Each row of the tables "Target",
"Principles" and "Constraints" is one line of the charter, with the identifier T-<n>, P-<n> or
K-<n>. Each principle has a priority: a whole number that no other principle has. The cell "Effect"
of a principle and of a constraint has one or more of these forms, with a semicolon between two
forms, and no other:

  level <n>               each item that holds a requirement that serves the line is admitted,
                          and is on level n of the recipe or on a lower level; n is 1, 2 or 3
  no exit: 3.3            a requirement that serves the line does not go to a decision of 3.3
  no exit: boundary       a requirement that serves the line does not go to a boundary
  no exit: not admitted   an item that holds a requirement that serves the line is admitted
  none                    the line has no effect that a program examines
  none: rule of the factory   the line is a rule for the factory and not for the content; no
                          requirement must serve it

A target part has the effect "level <n>" through its cell "Level of the recipe". With a charter,
the cell "Serves" of each requirement names the lines of the charter that the requirement serves,
with a comma between two identifiers, or "none". A duplicate has the exit of its row. The level of
an item is not higher than the lowest level that such a line gives. The cell "Placed by" of an
item names the line that placed it, or "calculation": place.py writes it. A line places an item
when the item is on the level that the line gives. The calculation of risk and reward places an
item on a lower level. A line that no
requirement serves remains while the charter is a draft, and fails after the review of the owner.
The report gives, for each line, the number of requirements that serve it and the number of items
that it placed. --scope examines only the form of the charter.

The cell "Views" of a source in section 2 names the views that the source was read for, or "all"
for a body of knowledge. A specification of an earlier revision has no such cell: this fails
nothing. A view with fewer than two sources that were read for it remains.

The table "Reading" of vetting.md names, for each converted document of a source, the pages
that the readers got and the pages that no reader got. The program index.py writes it with
"unread --write". A source with "full" in the cell Read and with pages that no reader got fails.
A source with "all" in the cell Views needs a row in the table. Each source with pages that no
reader got remains. A specification without the table remains also. --scope does not examine
the table.

The file trial.md records each trial of the recipe on a project, and each finding of the review of
the plan. A finding names its trial, one of seven viewpoints, one of three routes and its status.
The names of the viewpoints are in the file references/viewpoints.txt, one in each line. A kit
that export.py made does not hold this file. Without the file, the viewpoint of a finding is not
checked, and the list of what remains says so.
"""

import json
import pathlib
import re
import sys

import aspect

CLASSES = ("standard", "foundation", "vendor", "research", "trusted-data", "independent")
READ = ("full", "part", "no")
SOURCE_CELLS = ("id", "source", "issuer", "version or date", "class", "license", "read", "url")
# The cell Views of a source: the views that the source was read for, or "all".
ALL_VIEWS = "all"
OWN_SOURCES = 2
REQUIREMENT_CELLS = ("id", "requirement", "stakeholder", "view", "source", "goes to")
# The exits of a requirement, with the words of the report.
EXIT_WORDS = {
    "item": "to an item",
    "decision": "to a decision",
    "skill": "to an implementation skill",
    "boundary": "to a boundary",
    "duplicate": "duplicates",
}
OWN_RULE = "own rule"
# The words of the report for the requirements of a view that a proposed boundary would take.
WOULD_TAKE = "a proposed boundary would take"
# The keys of what remains that give one line for each entry.
ONE_LINE_EACH = ("boundaries", "left-stakeholders")
SCOPE_FIELDS = ("aspect", "field and disciplines", "agreed with the owner on")
FINDING_FIELDS = ("contexts", "boundaries")
NO_ANSWER = "(no answer)"
# The answers of the calculation of risk and reward: the cells of the table "Items" of vetting.md.
ANSWERS = ("severity", "probability", "breadth", "adopt", "keep", "own risk")
DATE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
NOT_CONFIRMED = ("", "pending", "rejected")
NONE_FOUND = "none found"
# The names of the viewpoints of the review of a plan, one in each line. A session of the
# research must not see them: export.py does not put this file into a kit.
VIEWPOINTS_FILE = pathlib.Path(__file__).resolve().parents[1] / "references/viewpoints.txt"
ROUTES = ("recipe", "tooling", "implementation skill")
STATUS = re.compile(r"open|corrected in \S.*|declined: \S.*")

MESSAGES = {
    "accepted-missing": "The head line has no field Accepted.",
    "aspect-field-empty": "The field '{0}' of section 1 is empty.",
    "agreed-without-date": "The field 'Agreed with the owner on' has no date.",
    "intent-without-date": (
        "The line '{0}' of the intent of the owner has no date. "
        "Write the quote and its date, or '(no answer)'."
    ),
    "finding-without-source": "This finding of section 1 names no source. Name it, or write 'judgement'.",
    "risk-dimensions-missing": "Section 1 names no risk dimension.",
    "risk-dimension-empty": "The risk dimension '{0}' has no question.",
    "targets-missing": "Section 1 names no target. Write one line for each target, or '(none found)'.",
    "views-missing": "Section 1 names no view.",
    "view-empty": "The view '{0}' does not name its concerns.",
    "view-twice": "The view '{0}' is in section 1 two times.",
    "stakeholders-missing": "Section 1 names no stakeholder.",
    "stakeholder-empty": "The stakeholder '{0}' names no concern.",
    "stakeholder-unknown": (
        "The view '{0}' names the stakeholder '{1}'. Section 1 does not have this stakeholder."
    ),
    "view-without-stakeholder": "The view '{0}' names no stakeholder. Use the form '(stakeholders: a, b)'.",
    "item-without-view": "The item names no view of section 1.",
    "view-unknown": "The view '{0}' is not in section 1.",
    "view-without-item": "The view '{0}' has no checklist item.",
    "view-without-basics": "The view '{0}' has no item on level 1.",
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
    "full-with-unread-pages": (
        "The source says 'full'. The table Reading names pages that no reader got: {0}."
    ),
    "body-without-reading": (
        "The cell Views of the source is 'all'. The table Reading has no row for the source. "
        "Run index.py unread with --write."
    ),
    "requirements-missing": "The table Requirements of vetting.md is absent or empty.",
    "requirement-cell-empty": "The cell '{0}' of the requirement is empty.",
    "requirement-id-twice": "The identifier of the requirement is used two times.",
    "requirement-exit-unknown": (
        "The cell 'Goes to' is '{0}'. "
        "Use 'C-<nn>', '3.3: <decision>', '5', 'boundary: <name>' or 'duplicate: R-<nn>'."
    ),
    "requirement-item-unknown": "The requirement goes to '{0}'. The checklist does not have this item.",
    "requirement-item-retired": "The requirement goes to '{0}'. This item is retired.",
    "requirement-decision-unknown": (
        "The requirement goes to the decision '{0}'. Section 3.3 does not have this decision."
    ),
    "requirement-boundary-unknown": (
        "The requirement goes to the boundary '{0}'. Section 1 does not have this boundary."
    ),
    "requirement-boundary-not-decided": (
        "The requirement goes to the boundary '{0}'. The owner did not decide this boundary. "
        "Give the requirement a different exit, and propose the boundary to the owner."
    ),
    "boundary-state-unknown": (
        "The state '{0}' of the boundary is not permitted. "
        "Use '(proposed)' or '(decided by the owner on <YYYY-MM-DD>)'."
    ),
    "boundary-without-date": (
        "The boundary '{0}' is decided and has no date. Use '(decided by the owner on <YYYY-MM-DD>)'."
    ),
    "proposed-boundary-without-row": (
        "The boundary '{0}' is proposed. The table 'Proposed boundaries' of vetting.md has no row for it."
    ),
    "proposed-row-unknown": (
        "The table 'Proposed boundaries' has a row for '{0}'. Section 1 does not have this boundary."
    ),
    "proposed-row-decided": (
        "The table 'Proposed boundaries' has a row for '{0}'. The owner decided this boundary. "
        "Remove the row."
    ),
    "proposed-requirement-unknown": (
        "The row of the boundary '{0}' names '{1}'. The table Requirements does not have this row."
    ),
    "requirement-duplicate-unknown": (
        "The requirement is a duplicate of '{0}'. The table Requirements does not have this row."
    ),
    "requirement-duplicate-of-duplicate": (
        "The requirement is a duplicate of '{0}'. That row is a duplicate also."
    ),
    "requirement-stakeholder-unknown": (
        "The requirement names the stakeholder '{0}'. Section 1 does not have this stakeholder."
    ),
    "requirement-without-source": "The requirement names no source of section 2.",
    "item-without-requirement": "No requirement of the table Requirements goes to the item.",
    "stakeholder-without-requirement": "The stakeholder '{0}' has no requirement in the table Requirements.",
    "checklist-empty": "The checklist of section 4 has no item.",
    "charter-state-unknown": (
        "The state '{0}' of the charter is not permitted. "
        "Use 'draft' or 'reviewed by the owner on <YYYY-MM-DD>'."
    ),
    "charter-without-line": "The charter has no line. Write the tables Target, Principles and Constraints.",
    "charter-id-unknown": "The identifier '{0}' is not permitted in the table '{1}'. Use '{2}-<n>'.",
    "charter-id-twice": "The identifier of the line of the charter is used two times.",
    "charter-priority-missing": "The principle has no priority. Write a whole number.",
    "charter-priority-twice": (
        "The priority '{0}' is used two times. Give each principle a different priority."
    ),
    "charter-effect-unknown": (
        "The effect '{0}' is not permitted. Use 'level <n>', 'no exit: 3.3', 'no exit: boundary', "
        "'no exit: not admitted', 'none' or 'none: rule of the factory'."
    ),
    "charter-level-unknown": "The level '{0}' of the line of the charter is not permitted. Use 1, 2 or 3.",
    "charter-line-unserved": "No requirement serves the line '{0}' of the charter.",
    "requirement-serves-unknown": (
        "The requirement serves '{0}'. The charter does not have this line. "
        "Write identifiers of the charter with a comma between them, or 'none'."
    ),
    "requirement-exit-closed": (
        "The requirement serves '{0}'. This line of the charter does not permit the exit '{1}'. "
        "Give the requirement a different exit."
    ),
    "item-not-admitted-against-charter": (
        "The item is not admitted. It holds '{0}', which serves '{1}'. "
        "This line of the charter does not permit that. Run place.py with --write."
    ),
    "item-above-charter-level": (
        "The level of the item is '{0}'. The line '{1}' of the charter gives it level {2} or a lower level. "
        "Run place.py with --write."
    ),
    "placed-by-differs": (
        "The cell 'Placed by' is '{0}'. The program place.py computes '{1}'. Run place.py with --write."
    ),
    "product-word": "The item uses the product word '{0}'.",
    "id-removed": "The earlier revision has this item. Keep the row and set its level to 'retired'.",
    "id-reused": "The earlier revision retired this identifier. Use a new identifier.",
    "skill-field-empty": "The field '{0}' of the recipe skill in section 5 is empty.",
    "skill-refers-to-section": "The field '{0}' of the recipe skill refers to a section of spec.md.",
    "trial-unknown": "The finding names the trial '{0}'. The table Trials does not have this trial.",
    "trial-viewpoint-unknown": "The viewpoint '{0}' is not one of the seven viewpoints.",
    "trial-finding-empty": "The finding of the trial has no text.",
    "trial-route-unknown": "The route '{0}' is not permitted. Use recipe, tooling or implementation skill.",
    "trial-status-unknown": (
        "The status '{0}' is not permitted. Use 'open', 'corrected in <revision>' or 'declined: <reason>'."
    ),
    "no-failure": "No check fails.",
    "scope-only": "Only the field and the thing to build were checked. The findings wait for the research.",
    "failures": "Failing checks: {0}.",
    "views-head": "Views, with the number of items on each level, of sources and of stakeholders:",
    "view-line": (
        "{0}: level 1: {1}, level 2: {2}, level 3: {3}, pending: {4}, not admitted: {5}, sources: {6}, "
        "stakeholders: {7}, sources read for the view: {8}."
    ),
    "requirements-head": "Requirements of the sources, with the number for each view and where they go:",
    "requirement-line": (
        "{0}: requirements: {1}, to an item: {2}, to a decision: {3}, to an implementation skill: {4}, "
        "to a boundary: {5}, duplicates: {6}, a proposed boundary would take: {7}."
    ),
    "charter-head": (
        "Charter, with the number of requirements that serve each line and of items that it placed:"
    ),
    "charter-line": "{0}: requirements: {1}, items placed: {2}.",
    "answers": "Answers of risk and reward: {0} with a source, {1} by judgement.",
    "answers-other": "Answers of risk and reward without a source and without 'judgement': {0}.",
    "remains-head": "What remains:",
    "remains-intent": "The intent of the owner was not asked.",
    "remains-no-charter": "The specification has no charter.",
    "remains-charter-draft": "The owner did not review the charter.",
    "remains-charter-unserved": "Lines of the charter that no requirement serves: {0}.",
    "remains-serves-none": "Requirements that serve no line of the charter, for each view: {0}.",
    "serves-none-view": "{0}: {1}",
    "remains-levels": "Levels that are pending: {0}.",
    "remains-basics": "Views without an item on level 1, while levels are pending: {0}.",
    "remains-vettings": "Vettings that are pending: {0}.",
    "remains-waiting": "Items that rest only on sources with a pending vetting: {0}.",
    "remains-judgement": "Items that need judgement: {0}.",
    "remains-changed": "Items with a changed text. Make sure that the meaning is the same: {0}.",
    "remains-trial": "Trial findings that are open: {0}.",
    "remains-viewpoints": "Trial findings with a viewpoint that was not checked: {0}. The list is absent.",
    "remains-stakeholders": "Stakeholders that are in no view: {0}.",
    "remains-boundaries": "More than half of the requirements of the view '{0}' go to a boundary.",
    "remains-proposed-boundaries": "Boundaries that wait for the decision of the owner: {0}.",
    "boundary-takes": "{0} ({1} requirements)",
    "remains-left-stakeholders": (
        "The boundary '{0}' would leave the stakeholder '{1}' with no requirement in the aspect."
    ),
    "remains-own-sources": "Views with fewer than two sources of their own field that were read: {0}.",
    "remains-unread": "Sources with pages that no reader got: {0}.",
    "remains-no-reading": "The table Reading is absent. Run index.py unread with --write.",
    "pages-left": "{0} ({1} pages)",
    "remains-no-trial": "The recipe has no trial.",
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


def check_scope(data):
    r"""What the owner and the agent settle before the research: the field and the thing to build.

    These are the head line and four fields of section 1: the aspect, the field, the intent of
    the owner, and the date of the agreement. Nothing narrower is settled before the research.

    >>> import sample
    >>> check_scope(sample.load())
    []
    >>> brief(check_scope(sample.load(("spec.md", " | **Accepted**: A. Person, 2026-01-15", ""))))
    [('accepted-missing', '')]
    >>> empty = ("spec.md", "- **Aspect**: backups of the data of a software project.", "- **Aspect**:")
    >>> check_scope(sample.load(empty))[0]["text"]
    "The field 'aspect' of section 1 is empty."
    >>> date = ("spec.md", "2026-01-05; a recipe for", "in January; a recipe for")
    >>> brief(check_scope(sample.load(date)))
    [('agreed-without-date', '')]

    The intent of the owner has one line for each answer: a quote with its date, or "(no answer)".
    A specification without the field fails. A line that is empty or has no date fails.

    >>> lines = "\n".join(sample.INTENT) + "\n"
    >>> head = sample.INTENT_HEAD + "\n"
    >>> found = check_scope(sample.load(("spec.md", head + lines, "")))
    >>> brief(found), found[0]["text"]
    ([('aspect-field-empty', '')], "The field 'intent of the owner' of section 1 is empty.")
    >>> brief(check_scope(sample.load(("spec.md", head + lines, "- **Intent of the owner**:\n"))))
    [('aspect-field-empty', '')]
    >>> undated = sample.INTENT_RESULT.removesuffix(" (2026-01-05)")
    >>> found = check_scope(sample.load(("spec.md", sample.INTENT_RESULT, undated)))
    >>> brief(found), found[0]["line"]
    ([('intent-without-date', 'result')], 25)
    >>> found[0]["text"]
    "The line 'result' of the intent of the owner has no date. Write the quote and its date, or '(no
    answer)'."
    >>> brief(check_scope(sample.load(("spec.md", sample.INTENT_RESULT, "  - `result`:"))))
    [('intent-without-date', 'result')]
    >>> brief(check_scope(sample.load(("spec.md", head + lines, head))))
    [('intent-without-date', 'intent of the owner')]

    "(no answer)" in each line passes: the owner was not in the session.

    >>> none = [("spec.md", line, line.split(":")[0] + ": (no answer)") for line in sample.INTENT[:2]]
    >>> data = sample.load(*none)
    >>> check_scope(data), intent_asked(data), intent_asked(sample.load())
    ([], False, True)

    The stakeholders, the views, the contexts, the risk dimensions, the boundaries and the targets
    are not part of the scope.

    >>> findings = ("- **Views", "- **Contexts", "  ", "- **Boundaries", "- **Targets", "- **Stakeholders")
    >>> intent = ("- **Intent", *sample.INTENT)
    >>> lines = [x for x in sample.SPEC.splitlines() if x.startswith(intent) or not x.startswith(findings)]
    >>> folder = sample.folder()
    >>> _ = (folder / "spec.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    >>> check_scope(aspect.load(folder))
    []
    """
    out, head = [], data["head"]
    if "accepted" not in head:
        out.append(finding("accepted-missing", head))
    for name in SCOPE_FIELDS:
        field = data["aspect"].get(name)
        if not field or not field["value"]:
            out.append(finding("aspect-field-empty", field or {}, "", name))
    agreed = data["aspect"].get("agreed with the owner on")
    if agreed and agreed["value"] and not DATE.search(agreed["value"]):
        out.append(finding("agreed-without-date", agreed))
    if not data["intent"]:
        out.append(finding("aspect-field-empty", data["aspect"].get(aspect.INTENT, {}), "", aspect.INTENT))
    for line in data["intent"]:
        if not no_answer(line) and not DATE.search(line["text"]):
            out.append(finding("intent-without-date", line, line["name"], line["name"]))
    return out


def no_answer(line):
    """True if a line of the intent of the owner says that the owner gave no answer.

    >>> [no_answer({"text": text}) for text in ("(no answer)", " (No answer). ", '"No." (2026-01-05)', "")]
    [True, True, False, False]
    """
    return line["text"].strip().rstrip(".").lower() == NO_ANSWER


def intent_asked(data):
    """False if each line of the intent of the owner says "(no answer)".

    A specification without the field fails the check; this function then gives True, so that
    the report does not say the same thing two times.

    >>> intent_asked({"intent": []}), intent_asked({"intent": [{"text": "(no answer)"}]})
    (True, False)
    >>> intent_asked({"intent": [{"text": "(no answer)"}, {"text": '"Short." (2026-01-05)'}]})
    True
    """
    return not data["intent"] or not all(no_answer(line) for line in data["intent"])


def answer_counts(data):
    """How many answers of risk and reward name a source, and how many say "judgement".

    The answers are the six cells of each row of the table "Items" of vetting.md. An answer with
    a different note, or without a note, is counted as "other". An empty cell is not an answer.

    >>> import sample
    >>> answer_counts(sample.load())
    {'judgement': 22, 'other': 0, 'source': 8}
    >>> row = "| C-04 | 1 (judgement) | 1 (judgement) |"
    >>> answer_counts(sample.load(("vetting.md", row, "| C-04 | 1 (owner) | |")))
    {'judgement': 20, 'other': 1, 'source': 8}
    >>> answer_counts({"vetting_items": []})
    {'judgement': 0, 'other': 0, 'source': 0}
    """
    counts = {"judgement": 0, "other": 0, "source": 0}
    for row in data["vetting_items"]:
        for name in ANSWERS:
            cell = row.get(name, "").strip()
            if aspect.source_ids(cell):
                counts["source"] += 1
            elif "judgement" in cell.lower():
                counts["judgement"] += 1
            elif cell:
                counts["other"] += 1
    return counts


def check_scope_findings(data):
    r"""What the research finds for section 1: contexts, risk dimensions, boundaries, targets.

    They are findings, as the checklist items are. Thus each one is filled and names its source,
    or says "judgement".

    >>> import sample
    >>> check_scope_findings(sample.load())
    []
    >>> old = "- **Boundaries**: the recovery of a complete site belongs to a different aspect. (judgement)"
    >>> check_scope_findings(sample.load(("spec.md", old, "- **Boundaries**:")))[0]["text"]
    "The field 'boundaries' of section 1 is empty."
    >>> brief(check_scope_findings(sample.load(("spec.md", old, old.removesuffix(" (judgement)")))))
    [('finding-without-source', 'boundaries')]

    Each risk dimension needs a name, a question and a source. A specification without one fails.

    >>> operative = "  - `operative`: Can a lost record be made again? Opinion: if not, go past level 1."
    >>> source = " (S-02 section 4)"
    >>> brief(check_scope_findings(sample.load(("spec.md", operative + source, "  - `operative`:"))))
    [('risk-dimension-empty', 'operative')]
    >>> brief(check_scope_findings(sample.load(("spec.md", operative + source, operative))))
    [('finding-without-source', 'operative')]
    >>> regulatory = "  - `regulatory`: Is personal data in the backup? Opinion: if yes, aim for level 3."
    >>> first, second = operative + source + "\n", regulatory + " (S-01 section 5)\n"
    >>> none = sample.load(("spec.md", first, ""), ("spec.md", second, ""))
    >>> brief(check_scope_findings(none))
    [('risk-dimensions-missing', '')]

    A field can hold one sub-item for each finding. Then each sub-item names its source.

    >>> one = "- **Boundaries**: the recovery of a complete site belongs to a different aspect. (judgement)"
    >>> two = "- **Boundaries**: what the neighbours own.\n"
    >>> two += "  - `recovery`: a complete site. (S-01 section 5)\n  - `tests`: test design."
    >>> brief(check_scope_findings(sample.load(("spec.md", one, two))))
    [('finding-without-source', 'tests')]

    A target is a measurable result of the recipe. Each target is one line below the field and
    names its source. A field without a target says "(none found)".

    >>> no_source = sample.TARGET.removesuffix(" (S-02 section 4)")
    >>> brief(check_scope_findings(sample.load(("spec.md", sample.TARGET, no_source))))
    [('finding-without-source', 'restore drill')]
    >>> found = check_scope_findings(sample.load(("spec.md", sample.TARGET + "\n", "")))
    >>> brief(found), found[0]["line"], found[0]["text"]
    ([('targets-missing', '')], 20,
     "Section 1 names no target. Write one line for each target, or '(none found)'.")
    >>> field = "- **Targets**: the measurable results that a project reaches when it applies the recipe.\n"
    >>> none = ("spec.md", field + sample.TARGET, "- **Targets**: (none found)")
    >>> check_scope_findings(sample.load(none))
    []
    >>> brief(check_scope_findings(sample.load(("spec.md", field + sample.TARGET + "\n", ""))))
    [('targets-missing', '')]
    """
    out = []
    for name in FINDING_FIELDS:
        field = data["aspect"].get(name)
        if not field or not (field["value"] or field["items"]):
            out.append(finding("aspect-field-empty", field or {}, "", name))
            continue
        parts = field["items"] or [{"name": name, "text": field["value"], "_line": field["_line"]}]
        for part in parts:
            if not aspect.source_ids(part["text"]) and "judgement" not in part["text"].lower():
                out.append(finding("finding-without-source", part, part["name"]))
    if not data["risk_dimensions"]:
        out.append(finding("risk-dimensions-missing", data["aspect"].get("risk dimensions", {})))
    for dim in data["risk_dimensions"]:
        if not dim["text"]:
            out.append(finding("risk-dimension-empty", dim, dim["name"], dim["name"]))
        elif not aspect.source_ids(dim["text"]) and "judgement" not in dim["text"].lower():
            out.append(finding("finding-without-source", dim, dim["name"]))
    field = data["aspect"].get("targets", {})
    if not data["targets"] and NONE_FOUND not in field.get("value", "").lower():
        out.append(finding("targets-missing", field))
    for target in data["targets"]:
        if not aspect.source_ids(target["text"]) and "judgement" not in target["text"].lower():
            out.append(finding("finding-without-source", target, target["name"]))
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

    The cell Views names the views that the source was read for, or "all". A view that section 1
    does not have fails. An empty cell fails.

    >>> for cell in ("all", "operation; storage", "operation, quality", ""):
    ...     edit = ("spec.md", "| MIT | part | operation |", f"| MIT | part | {cell} |")
    ...     print(repr(cell), [(f["rule"], f["id"], f["text"]) for f in check_sources(sample.load(edit))])
    'all' []
    'operation; storage' []
    'operation, quality' [('view-unknown', 'S-04', "The view 'quality' is not in section 1.")]
    '' [('source-cell-empty', 'S-04', "The cell 'views' of the source is empty.")]

    A specification of an earlier revision has no cell Views. This fails nothing.

    >>> old = sample.load()
    >>> for row in old["sources"]:
    ...     del row["views"]
    ...     row["_header"] = [name for name in row["_header"] if name != "views"]
    >>> check_sources(old)
    []
    """
    out, seen = [], set()
    views = {v["name"] for v in data["views"]}
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
        if "views" in row.get("_header", ()) and not row.get("views", ""):
            out.append(finding("source-cell-empty", row, ident, "views"))
        for name in aspect.names_of(row.get("views")):
            if views and name != ALL_VIEWS and name not in views:
                out.append(finding("view-unknown", row, ident, name))
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
    ([('unknown-source', 'C-02')], 68, "The row cites 'S-09'. Section 2 does not list this source.")

    The rows of the strategy are checked also.

    >>> strategy = ("spec.md", "| S-01 section 3 |\n\n### 3.4", "| S-08 |\n\n### 3.4")
    >>> brief(check_references(sample.load(strategy)))
    [('unknown-source', '')]

    The views, the targets and the stakeholders of section 1 are checked also.

    >>> owners = sample.STAKEHOLDER_OWNERS
    >>> other = ("spec.md", owners, owners.replace("S-01", "S-08"))
    >>> brief(check_references(sample.load(other)))
    [('unknown-source', 'owners of the data')]

    >>> view = ("spec.md", "data) (S-01 section 2)", "data) (S-08 section 2)")
    >>> brief(check_references(sample.load(view)))
    [('unknown-source', 'storage')]
    >>> target = ("spec.md", "measures it. (S-02 section 4)", "measures it. (S-08 section 4)")
    >>> brief(check_references(sample.load(target)))
    [('unknown-source', 'restore drill')]
    """
    known = {s.get("id") for s in data["sources"]}
    out = []
    rows = [(r, r.get("source", ""), r.get("id", "")) for r in data["checklist"]]
    rows += [(r, r.get("sources", ""), "") for r in data["context_decisions"] + data["disagreement"]]
    for name in FINDING_FIELDS:
        field = data["aspect"].get(name) or {"value": "", "items": []}
        rows += [(field, field["value"], name)] + [(i, i["text"], i["name"]) for i in field["items"]]
    findings = data["risk_dimensions"] + data["views"] + data["targets"] + data["stakeholders"]
    rows += [(d, d["text"], d["name"]) for d in findings]
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


def check_views(data):
    r"""The views of section 1, and the view of each item.

    A view is a set of concerns of the aspect. Each view names its concerns and its source, or
    says "judgement". Each item that is not retired names one view of section 1.

    >>> import sample
    >>> check_views(sample.load())
    []
    >>> storage = sample.VIEW_STORAGE
    >>> brief(check_views(sample.load(("spec.md", storage, "  - `storage`:"))))
    [('view-empty', 'storage')]
    >>> brief(check_views(sample.load(("spec.md", storage, storage.removesuffix(" (S-01 section 2)")))))
    [('finding-without-source', 'storage')]
    >>> why = "| Risk: a backup that cannot be restored is found too late. |"
    >>> brief(check_views(sample.load(("spec.md", why + " operation |", why + " |"))))
    [('item-without-view', 'C-02')]
    >>> found = check_views(sample.load(("spec.md", why + " operation |", why + " `quality` |")))
    >>> brief(found), found[0]["text"]
    ([('view-unknown', 'C-02')], "The view 'quality' is not in section 1.")

    A view of section 1 needs an item. A retired item does not count, and names no view.

    >>> quality = storage + "\n  - `quality`: how the copies are examined. (judgement)"
    >>> found = check_views(sample.load(("spec.md", storage, quality)))
    >>> brief(found), found[0]["line"], found[0]["text"]
    ([('view-without-item', 'quality')], 13, "The view 'quality' has no checklist item.")
    >>> c01 = ("spec.md", "| storage | 1 | authority (2) |", "| | retired | authority (2) |")
    >>> c03 = ("spec.md", "| storage | 3, regulatory |", "| | retired |")
    >>> brief(check_views(sample.load(c01, c03)))
    [('view-without-item', 'storage')]

    A view is in section 1 one time only.

    >>> brief(check_views(sample.load(("spec.md", storage, storage + "\n" + storage))))
    [('view-twice', 'storage')]

    An aspect can have one view. A specification without a view fails, with one finding.

    >>> operation = sample.VIEW_OPERATION + "\n"
    >>> one = sample.load(("spec.md", operation, ""))
    >>> brief(check_views(one))
    [('view-unknown', 'C-02'), ('view-unknown', 'C-04'), ('view-unknown', 'C-05')]
    >>> for row in one["checklist"]:
    ...     row["view"] = "storage"
    >>> check_views(one)
    []
    >>> none = sample.load(("spec.md", operation, ""), ("spec.md", storage + "\n", ""))
    >>> brief(check_views(none)), check_views(none)[0]["line"]
    ([('views-missing', '')], 11)
    """
    if not data["views"]:
        return [finding("views-missing", data["aspect"].get("views", {}))]
    out, used, seen = [], set(), set()
    for view in data["views"]:
        if view["name"] in seen:
            out.append(finding("view-twice", view, view["name"], view["name"]))
        seen.add(view["name"])
        if not view["text"]:
            out.append(finding("view-empty", view, view["name"], view["name"]))
        elif not aspect.source_ids(view["text"]) and "judgement" not in view["text"].lower():
            out.append(finding("finding-without-source", view, view["name"]))
    names = {v["name"] for v in data["views"]}
    for row in live_items(data):
        name = aspect.view_of(row)
        used.add(name)
        if not name:
            out.append(finding("item-without-view", row, row.get("id", "")))
        elif name not in names:
            out.append(finding("view-unknown", row, row.get("id", ""), name))
    for view in data["views"]:
        if view["name"] not in used:
            out.append(finding("view-without-item", view, view["name"], view["name"]))
    return out


def check_stakeholders(data):
    r"""The stakeholders of section 1, and the stakeholders of each view.

    A stakeholder is a group of persons that has an interest in the result or carries a duty for
    it. Each stakeholder names its concerns and its source, or says "judgement". Each view names
    one stakeholder of section 1 or more.

    >>> import sample
    >>> check_stakeholders(sample.load())
    []
    >>> owners, operators = sample.STAKEHOLDER_OWNERS, sample.STAKEHOLDER_OPERATORS
    >>> found = check_stakeholders(sample.load(("spec.md", owners, "  - `owners of the data`:")))
    >>> brief(found), found[0]["line"], found[0]["text"]
    ([('stakeholder-empty', 'owners of the data')], 29,
     "The stakeholder 'owners of the data' names no concern.")
    >>> no_source = ("spec.md", owners, owners.removesuffix(" (S-01 section 2)"))
    >>> brief(check_stakeholders(sample.load(no_source)))
    [('finding-without-source', 'owners of the data')]

    A view names only stakeholders of section 1, and names one or more.

    >>> other = ("spec.md", "(stakeholders: operators)", "(stakeholders: users)")
    >>> found = check_stakeholders(sample.load(other))
    >>> brief(found), found[0]["line"]
    ([('stakeholder-unknown', 'operation')], 13)
    >>> found[0]["text"]
    "The view 'operation' names the stakeholder 'users'. Section 1 does not have this stakeholder."
    >>> found = check_stakeholders(sample.load(("spec.md", " (stakeholders: operators)", "")))
    >>> brief(found), found[0]["text"]
    ([('view-without-stakeholder', 'operation')],
     "The view 'operation' names no stakeholder. Use the form '(stakeholders: a, b)'.")

    A specification without a stakeholder fails, with one finding for section 1.

    >>> none = sample.load(("spec.md", owners + "\n", ""), ("spec.md", operators + "\n", ""))
    >>> brief(check_stakeholders(none))[0], check_stakeholders(none)[0]["line"]
    (('stakeholders-missing', ''), 27)

    A stakeholder that is in no view does not fail the check. It remains.

    >>> more = ("spec.md", owners, owners + "\n  - `auditors`: they examine the record. (judgement)")
    >>> check_stakeholders(sample.load(more)), stakeholders_without_view(sample.load(more))
    ([], ['auditors'])
    >>> stakeholders_without_view(sample.load())
    []
    """
    out = []
    if not data["stakeholders"]:
        out.append(finding("stakeholders-missing", data["aspect"].get("stakeholders", {})))
    for holder in data["stakeholders"]:
        if not holder["text"]:
            out.append(finding("stakeholder-empty", holder, holder["name"], holder["name"]))
        elif not aspect.source_ids(holder["text"]) and "judgement" not in holder["text"].lower():
            out.append(finding("finding-without-source", holder, holder["name"]))
    known = {s["name"] for s in data["stakeholders"]}
    for view in data["views"]:
        if not view["stakeholders"]:
            out.append(finding("view-without-stakeholder", view, view["name"], view["name"]))
        for name in view["stakeholders"]:
            if name not in known:
                out.append(finding("stakeholder-unknown", view, view["name"], view["name"], name))
    return out


def stakeholders_without_view(data):
    """The stakeholders of section 1 that no view names, sorted.

    >>> names = [{"name": "b"}, {"name": "a"}, {"name": "c"}]
    >>> stakeholders_without_view({"stakeholders": names, "views": [{"stakeholders": ["c"]}]})
    ['a', 'b']
    """
    used = {name for view in data["views"] for name in view["stakeholders"]}
    return sorted({s["name"] for s in data["stakeholders"]} - used)


def view_counts(data):
    """For each view of section 1, by name: its items on each level, its sources, its stakeholders.

    A retired item does not count. A source counts one time for a view. The last number is the
    number of the sources of the own field of the view: see own_sources.

    >>> import sample
    >>> for view in view_counts(sample.load()):
    ...     print(*view.values())
    operation 3 1 1 0 0 1 4 1 4
    storage 2 1 0 1 0 0 2 1 2
    >>> list(view)
    ['view', 'items', 'level 1', 'level 2', 'level 3', 'pending', 'not admitted', 'sources',
     'stakeholders', 'sources read for the view']
    """
    out = []
    for view in sorted(data["views"], key=lambda v: (v["name"], v["_line"])):
        rows = [r for r in live_items(data) if aspect.view_of(r) == view["name"]]
        levels = [aspect.level_of(r.get("level"))[0] for r in rows]
        counts = {f"level {n}": levels.count(n) for n in (1, 2, 3)}
        counts |= {state: levels.count(state) for state in ("pending", "not admitted")}
        cited = {s for r in rows for s in aspect.source_ids(r.get("source", ""))}
        counts |= {"sources": len(cited), "stakeholders": len(set(view["stakeholders"]))}
        counts["sources read for the view"] = len(own_sources(data, view["name"]))
        out.append({"view": view["name"], "items": len(rows), **counts})
    return out


def own_sources(data, view):
    """The sources of the own field of a view: read for the view, in full or in part. Sorted.

    A source with "all" in the cell Views is a body of knowledge. It is not such a source.

    >>> import sample
    >>> own_sources(sample.load(), "storage"), own_sources(sample.load(), "operation")
    (['S-01', 'S-02'], ['S-01', 'S-02', 'S-03', 'S-04'])
    >>> whole = ("spec.md", "| public | full | storage, operation |", "| public | full | all |")
    >>> unread = ("spec.md", "| CC BY 4.0 | full |", "| CC BY 4.0 | no |")
    >>> own_sources(sample.load(whole), "storage"), own_sources(sample.load(whole, unread), "storage")
    (['S-02'], [])
    >>> views_with_few_sources(sample.load()), views_with_few_sources(sample.load(whole))
    ([], ['storage'])
    """
    out = set()
    for row in data["sources"]:
        names = aspect.names_of(row.get("views"))
        if row.get("read") in ("full", "part") and view in names and ALL_VIEWS not in names:
            out.add(row.get("id", ""))
    return sorted(out)


def views_with_few_sources(data):
    """The views with fewer than two sources of their own field that were read, sorted.

    >>> views = [{"name": "b"}, {"name": "a"}]
    >>> first = {"id": "S-01", "read": "full", "views": "a"}
    >>> second = {"id": "S-02", "read": "part", "views": "a; b"}
    >>> views_with_few_sources({"views": views, "sources": [first, second]})
    ['b']
    """
    return sorted({v["name"] for v in data["views"] if len(own_sources(data, v["name"])) < OWN_SOURCES})


def reading_of(data):
    """The rows of the table "Reading" for the sources of section 2, with numbers. Sorted.

    Each row is a dictionary: the source, the document, the number of pages, and the number of
    pages that no reader got.

    >>> import sample
    >>> reading_of(sample.load())
    [{'source': 'S-01', 'document': 'S-01', 'pages': 6, 'not read': 0},
     {'source': 'S-02', 'document': 'S-02', 'pages': 2, 'not read': 0}]
    >>> other = "| S-01 | S-01 | many | 1-2 | 3, 5-6 |" + chr(10) + "| S-09 | a | 1 | 1 | none |"
    >>> short = ("vetting.md", sample.READING_S01, other)
    >>> reading_of(sample.load(short))[0]
    {'source': 'S-01', 'document': 'S-01', 'pages': 0, 'not read': 3}
    >>> unread_sources(sample.load(short)), unread_sources(sample.load())
    (['S-01 (3 pages)'], [])
    """
    known = {row.get("id", "") for row in data["sources"]}
    out = []
    for row in data["reading"]:
        if row.get("source", "") in known:
            pages = row.get("pages", "")
            left = len(aspect.pages_of(row.get("not read")))
            out.append(
                {
                    "source": row["source"],
                    "document": row.get("document", ""),
                    "pages": int(pages) if pages.isdigit() else 0,
                    "not read": left,
                }
            )
    return sorted(out, key=lambda row: (row["source"], row["document"]))


def unread_sources(data):
    """The sources with pages that no reader got, each with the number of the pages. Sorted."""
    left = {}
    for row in reading_of(data):
        left[row["source"]] = left.get(row["source"], 0) + row["not read"]
    return [MESSAGES["pages-left"].format(ident, count) for ident, count in sorted(left.items()) if count]


def reading_absent(data):
    """True if the specification has sources and its vetting record has no table "Reading".

    >>> import sample
    >>> reading_absent(sample.load()), reading_absent(sample.load(("vetting.md", "## Reading", "## Other")))
    (False, True)
    >>> reading_absent({"has_reading": False, "sources": []})
    False
    """
    return bool(data["sources"]) and not data["has_reading"]


def check_reading(data):
    """The table "Reading" of vetting.md agrees with section 2.

    >>> import sample
    >>> check_reading(sample.load())
    []

    A source with "full" in the cell Read and with pages that no reader got fails. A source with
    "part" does not fail: it remains.

    >>> left = ("vetting.md", sample.READING_S01, "| S-01 | S-01 | 6 | 1-2, 6 | 3-5 |")
    >>> [(f["rule"], f["id"], f["file"], f["text"]) for f in check_reading(sample.load(left))]
    [('full-with-unread-pages', 'S-01', 'spec.md',
      "The source says 'full'. The table Reading names pages that no reader got: 3-5.")]
    >>> part = ("spec.md", "| public | full | storage, operation |", "| public | part | storage, operation |")
    >>> check_reading(sample.load(left, part)), run_checks(sample.load(left, part))[1]["unread"]
    ([], ['S-01 (3 pages)'])

    A source with "all" in the cell Views needs a row in the table. A row with the document
    "none" says that the source has no converted document. Without the table, nothing fails:
    the absent table remains.

    >>> whole = ("spec.md", "| public | full | storage, operation |", "| public | full | all |")
    >>> gone = ("vetting.md", sample.READING_S01 + chr(10), "")
    >>> [(f["rule"], f["id"]) for f in check_reading(sample.load(whole))]
    []
    >>> [(f["rule"], f["id"], f["text"]) for f in check_reading(sample.load(whole, gone))]
    [('body-without-reading', 'S-01', "The cell Views of the source is 'all'. The table Reading has no row for
      the source. Run index.py unread with --write.")]
    >>> none = ("vetting.md", sample.READING_S01, "| S-01 | none | 0 | none | none |")
    >>> check_reading(sample.load(whole, none))
    []
    >>> check_reading(sample.load(whole, gone, ("vetting.md", "## Reading", "## Other")))
    []
    """
    out = []
    rows = {}
    for row in data["reading"]:
        rows.setdefault(row.get("source", ""), []).append(row)
    for source in data["sources"]:
        ident = source.get("id", "")
        cells = [
            row.get("not read", "") for row in rows.get(ident, []) if aspect.pages_of(row.get("not read"))
        ]
        if source.get("read") == "full" and cells:
            out.append(finding("full-with-unread-pages", source, ident, "; ".join(cells)))
        whole = ALL_VIEWS in aspect.names_of(source.get("views"))
        if whole and data["has_reading"] and ident not in rows:
            out.append(finding("body-without-reading", source, ident))
    return out


def boundary_names(data):
    r"""The names of the boundaries of section 1.

    >>> import sample
    >>> boundary_names(sample.load())
    set()
    >>> named = sample.BOUNDARIES + "\n  - `recovery`: a complete site. (judgement)"
    >>> boundary_names(sample.load(("spec.md", sample.BOUNDARIES, named))), boundary_names({"aspect": {}})
    ({'recovery'}, set())
    """
    return {item["name"] for item in data["aspect"].get("boundaries", {}).get("items", [])}


def boundaries_in_state(data, state):
    """The names of the boundaries of section 1 that have this state, in the order of section 1.

    >>> import sample
    >>> data = sample.load(("spec.md", sample.BOUNDARIES, sample.BOUNDARIES_NAMED))
    >>> boundaries_in_state(data, aspect.DECIDED), boundaries_in_state(data, aspect.PROPOSED)
    (['recovery'], ['tests', 'archive'])
    >>> boundaries_in_state(sample.load(), aspect.PROPOSED)
    []
    """
    return [b["name"] for b in data["boundaries"] if b["state"] == state]


def row_boundary(row):
    """The name of the boundary in a row of the table "Proposed boundaries".

    >>> row_boundary({"boundary": " `tests` "}), row_boundary({})
    ('tests', '')
    """
    return row.get("boundary", "").strip().strip("`").strip()


def proposed_takes(data):
    """For each proposed boundary of section 1: the requirements of the register that it would take.

    These are the requirements that its row in the table "Proposed boundaries" names. A requirement
    whose cell "Goes to" names the boundary counts also: the check fails for it, and the owner sees
    the number. The identifiers are sorted.

    >>> import sample
    >>> named = ("spec.md", sample.BOUNDARIES, sample.BOUNDARIES_NAMED)
    >>> proposed_takes(sample.load(named, sample.PROPOSED_TABLE)), proposed_takes(sample.load())
    ({'tests': ['R-03'], 'archive': []}, {})
    >>> row = sample.PROPOSED_ARCHIVE
    >>> more = ("vetting.md", row, row.replace("| none | none |", "| R-07 to R-09, R-01 | none |"))
    >>> exit = ("vetting.md", "| none | C-03 |", "| none | boundary: archive |")
    >>> proposed_takes(sample.load(named, sample.PROPOSED_TABLE, more, exit))["archive"]
    ['R-01', 'R-02', 'R-07', 'R-08']
    """
    known = {row.get("id", "") for row in data["requirements"]}
    takes = {name: set() for name in boundaries_in_state(data, aspect.PROPOSED)}
    for row in data["proposed_boundaries"]:
        if row_boundary(row) in takes:
            ids = aspect.requirement_ids(row.get("requirements that it would take"))
            takes[row_boundary(row)].update(ident for ident in ids if ident in known)
    for row in data["requirements"]:
        kind, name = aspect.exit_of(row.get("goes to"))
        if kind == "boundary" and name in takes:
            takes[name].add(row.get("id", ""))
    return {name: sorted(ids) for name, ids in takes.items()}


def waiting_boundaries(data):
    """The proposed boundaries, each with the number of requirements that it would take.

    >>> import sample
    >>> named = ("spec.md", sample.BOUNDARIES, sample.BOUNDARIES_NAMED)
    >>> waiting_boundaries(sample.load(named, sample.PROPOSED_TABLE)), waiting_boundaries(sample.load())
    (['tests (1 requirements)', 'archive (0 requirements)'], [])
    """
    return [MESSAGES["boundary-takes"].format(name, len(ids)) for name, ids in proposed_takes(data).items()]


def left_stakeholders(data):
    """Each [boundary, stakeholder]: the proposed boundary would take each requirement of the stakeholder.

    A requirement that goes to a boundary that the owner decided is not in the aspect. A
    stakeholder that has no requirement in the aspect before the proposal is not in this list.

    >>> import sample
    >>> named = ("spec.md", sample.BOUNDARIES, sample.BOUNDARIES_NAMED)
    >>> left_stakeholders(sample.load(named, sample.PROPOSED_TABLE)), left_stakeholders(sample.load())
    ([], [])
    >>> row = sample.PROPOSED_ARCHIVE
    >>> more = ("vetting.md", row, row.replace("| none | none |", "| R-01, R-02 | owners of the data |"))
    >>> left_stakeholders(sample.load(named, sample.PROPOSED_TABLE, more))
    [['archive', 'owners of the data']]

    Here the boundary "archive" would take R-02 only. When R-01 goes to the boundary "recovery",
    which the owner decided, no requirement of the owners of the data stays in the aspect.

    >>> one = ("vetting.md", row, row.replace("| none | none |", "| R-02 | owners of the data |"))
    >>> away = ("vetting.md", "| none | C-01 |", "| none | boundary: recovery |")
    >>> left_stakeholders(sample.load(named, sample.PROPOSED_TABLE, one))
    []
    >>> left_stakeholders(sample.load(named, sample.PROPOSED_TABLE, one, away))
    [['archive', 'owners of the data']]
    """
    decided = set(boundaries_in_state(data, aspect.DECIDED))
    kept = {}
    for row in data["requirements"]:
        kind, name = aspect.exit_of(row.get("goes to"))
        if kind != "boundary" or name not in decided:
            for holder in aspect.names_of(row.get("stakeholder")):
                kept.setdefault(holder, set()).add(row.get("id", ""))
    out = []
    for boundary, ids in proposed_takes(data).items():
        for holder in data["stakeholders"]:
            rows = kept.get(holder["name"])
            if rows and rows <= set(ids) and [boundary, holder["name"]] not in out:
                out.append([boundary, holder["name"]])
    return out


def check_boundaries(data):
    r"""The state of each boundary of section 1, and the table "Proposed boundaries" of vetting.md.

    Only the owner decides a boundary. The line of a boundary holds its state: "(proposed)", or
    "(decided by the owner on <YYYY-MM-DD>)". A line without a state is proposed.

    >>> import sample
    >>> check_boundaries(sample.load())
    []
    >>> named = ("spec.md", sample.BOUNDARIES, sample.BOUNDARIES_NAMED)
    >>> check_boundaries(sample.load(named, sample.PROPOSED_TABLE))
    []
    >>> def planted(old, new, file="spec.md"):
    ...     found = check_boundaries(sample.load(named, sample.PROPOSED_TABLE, (file, old, new)))
    ...     return [(f["rule"], f["id"], f["file"], f["line"], f["text"]) for f in found]

    A state that is none of the two forms fails. A decided state without a date fails.

    >>> planted("(proposed)", "(proposed by a reader)")
    [('boundary-state-unknown', 'tests', 'spec.md', 21,
      "The state 'proposed by a reader' of the boundary is not permitted. Use '(proposed)' or '(decided by
      the owner on <YYYY-MM-DD>)'.")]
    >>> planted("(decided by the owner on 2026-01-12)", "(decided by the owner)")
    [('boundary-without-date', 'recovery', 'spec.md', 20,
      "The boundary 'recovery' is decided and has no date. Use '(decided by the owner on <YYYY-MM-DD>)'.")]

    Each proposed boundary has a row in the table "Proposed boundaries".

    >>> planted(sample.PROPOSED_ARCHIVE + "\n", "", "vetting.md")
    [('proposed-boundary-without-row', 'archive', 'spec.md', 22,
      "The boundary 'archive' is proposed. The table 'Proposed boundaries' of vetting.md has no row for it.")]
    >>> brief(check_boundaries(sample.load(named)))
    [('proposed-boundary-without-row', 'tests'), ('proposed-boundary-without-row', 'archive')]

    A row names a proposed boundary of section 1, and requirements of the register.

    >>> planted("| tests | R-03 |", "| quality | R-03 |", "vetting.md")[1]
    ('proposed-row-unknown', 'quality', 'vetting.md', 39,
     "The table 'Proposed boundaries' has a row for 'quality'. Section 1 does not have this boundary.")
    >>> planted("| tests | R-03 |", "| recovery | R-03 |", "vetting.md")[1]
    ('proposed-row-decided', 'recovery', 'vetting.md', 39,
     "The table 'Proposed boundaries' has a row for 'recovery'. The owner decided this boundary. Remove the
     row.")
    >>> planted("| tests | R-03 |", "| tests | R-03, R-19 |", "vetting.md")
    [('proposed-requirement-unknown', 'tests', 'vetting.md', 39,
      "The row of the boundary 'tests' names 'R-19'. The table Requirements does not have this row.")]
    """
    out = []
    rows = data["proposed_boundaries"]
    with_row = {row_boundary(row) for row in rows}
    states = {b["name"]: b["state"] for b in data["boundaries"]}
    for boundary in data["boundaries"]:
        name = boundary["name"]
        if boundary["state"] is None:
            out.append(finding("boundary-state-unknown", boundary, name, boundary["state text"]))
        elif boundary["state"] == "undated":
            out.append(finding("boundary-without-date", boundary, name, name))
        elif boundary["state"] == aspect.PROPOSED and name not in with_row:
            out.append(finding("proposed-boundary-without-row", boundary, name, name))
    known = {row.get("id", "") for row in data["requirements"]}
    for row in rows:
        name = row_boundary(row)
        if name not in states:
            out.append(finding("proposed-row-unknown", row, name, name))
        elif states[name] == aspect.DECIDED:
            out.append(finding("proposed-row-decided", row, name, name))
        for ident in aspect.requirement_ids(row.get("requirements that it would take")):
            if ident not in known:
                out.append(finding("proposed-requirement-unknown", row, name, name, ident))
    return out


def exit_fault(data, kind, name):
    """The rule that the exit of a requirement fails, or None. See check_requirements.

    >>> import sample
    >>> exit_fault(sample.load(), None, "a text"), exit_fault(sample.load(), "skill", "5")
    ('requirement-exit-unknown', None)
    """
    if kind is None:
        return "requirement-exit-unknown"
    if kind == "item":
        levels = {r.get("id"): aspect.level_of(r.get("level"))[0] for r in data["checklist"]}
        if name not in levels:
            return "requirement-item-unknown"
        return "requirement-item-retired" if levels[name] == "retired" else None
    if kind == "decision":
        known = {r.get("decision", "").strip().lower() for r in data["context_decisions"]}
        return None if name.lower() in known else "requirement-decision-unknown"
    if kind == "boundary":
        if name not in boundary_names(data):
            return "requirement-boundary-unknown"
        decided = boundaries_in_state(data, aspect.DECIDED)
        return None if name in decided else "requirement-boundary-not-decided"
    if kind == "duplicate":
        exits = {r.get("id"): aspect.exit_of(r.get("goes to"))[0] for r in data["requirements"]}
        if name not in exits:
            return "requirement-duplicate-unknown"
        return "requirement-duplicate-of-duplicate" if exits[name] == "duplicate" else None
    return None


def check_requirements(data):
    r"""The register of the requirements: the table "Requirements" of vetting.md.

    Each requirement that a source states for a stakeholder has one row. Each cell is filled. The
    stakeholder and the view are in section 1, and the source is in section 2.

    >>> import sample
    >>> check_requirements(sample.load())
    []
    >>> def planted(old, new, *more):
    ...     found = check_requirements(sample.load(("vetting.md", old, new), *more))
    ...     return [(f["rule"], f["id"], f["text"]) for f in found]
    >>> planted("| Do a restore from the backup as a test. |", "| |")
    [('requirement-cell-empty', 'R-03', "The cell 'requirement' of the requirement is empty.")]
    >>> planted("| R-02 | Keep a copy", "| R-01 | Keep a copy")
    [('requirement-id-twice', 'R-01', 'The identifier of the requirement is used two times.')]
    >>> r03 = "| operators | operation | S-02 section 4 |"
    >>> planted(r03, "| operators; users | operation | S-02 section 4 |")
    [('requirement-stakeholder-unknown', 'R-03',
      "The requirement names the stakeholder 'users'. Section 1 does not have this stakeholder.")]
    >>> planted(r03, "| operators | quality | S-02 section 4 |")
    [('view-unknown', 'R-03', "The view 'quality' is not in section 1.")]
    >>> planted(r03, "| operators | operation | S-09 section 4 |")
    [('unknown-source', 'R-03', "The row cites 'S-09'. Section 2 does not list this source.")]
    >>> planted(r03, "| operators | operation | a talk |")
    [('requirement-without-source', 'R-03', 'The requirement names no source of section 2.')]

    The cell "Goes to" has one of five forms. A requirement has no other exit.

    >>> exit = sample.REQUIREMENT_R07
    >>> def goes(cell, *more):
    ...     return planted(exit, exit.replace("3.3: How frequently to make a backup", cell), *more)
    >>> for cell in ("one source only states it", "depends on context", "3.3", ""):
    ...     print(goes(cell)[0][::2])
    ('requirement-exit-unknown', "The cell 'Goes to' is 'one source only states it'. Use 'C-<nn>',
    '3.3: <decision>', '5', 'boundary: <name>' or 'duplicate: R-<nn>'.")
    ('requirement-exit-unknown', "The cell 'Goes to' is 'depends on context'. Use 'C-<nn>',
    '3.3: <decision>', '5', 'boundary: <name>' or 'duplicate: R-<nn>'.")
    ('requirement-exit-unknown', "The cell 'Goes to' is '3.3'. Use 'C-<nn>', '3.3: <decision>', '5',
    'boundary: <name>' or 'duplicate: R-<nn>'.")
    ('requirement-cell-empty', "The cell 'goes to' of the requirement is empty.")

    An exit names a row that exists: an item that is not retired, a decision of section 3.3, a
    boundary of section 1 that the owner decided, or a requirement that is not a duplicate.

    >>> goes("C-09")
    [('requirement-item-unknown', 'R-07',
      "The requirement goes to 'C-09'. The checklist does not have this item.")]
    >>> goes("3.3: Where to keep the copies")
    [('requirement-decision-unknown', 'R-07',
      "The requirement goes to the decision 'Where to keep the copies'. Section 3.3 does not have this
      decision.")]
    >>> goes("3.3: how frequently to make a backup"), goes("5"), goes("C-02")
    ([], [], [])
    >>> goes("boundary: recovery")
    [('requirement-boundary-unknown', 'R-07',
      "The requirement goes to the boundary 'recovery'. Section 1 does not have this boundary.")]
    >>> named = ("spec.md", sample.BOUNDARIES, sample.BOUNDARIES_NAMED)
    >>> goes("boundary: recovery", named)
    []

    Only the owner decides a boundary. A requirement does not go to a proposed boundary, and not
    to a boundary without a state.

    >>> goes("boundary: tests", named)
    [('requirement-boundary-not-decided', 'R-07',
      "The requirement goes to the boundary 'tests'. The owner did not decide this boundary. Give the
      requirement a different exit, and propose the boundary to the owner.")]
    >>> goes("boundary: archive", named)[0][:2]
    ('requirement-boundary-not-decided', 'R-07')
    >>> goes("duplicate: R-19")
    [('requirement-duplicate-unknown', 'R-07',
      "The requirement is a duplicate of 'R-19'. The table Requirements does not have this row.")]
    >>> goes("duplicate: R-06")
    [('requirement-duplicate-of-duplicate', 'R-07',
      "The requirement is a duplicate of 'R-06'. That row is a duplicate also.")]
    >>> goes("duplicate: R-07")[0][0], goes("duplicate: R-05")
    ('requirement-duplicate-of-duplicate', [])

    A requirement that goes to a retired item has no exit.

    >>> retired = ("spec.md", "| storage | 3, regulatory |", "| | retired |")
    >>> found = check_requirements(sample.load(retired))
    >>> [(f["rule"], f["id"], f["text"]) for f in found]
    [('requirement-item-retired', 'R-02', "The requirement goes to 'C-03'. This item is retired.")]

    Each item that is not retired holds a requirement. An item of an own rule needs none.

    >>> row = sample.REQUIREMENT_R02
    >>> other = ("vetting.md", row, row.replace("| C-03 |", "| C-01 |"))
    >>> found = check_requirements(sample.load(other))
    >>> [(f["rule"], f["id"], f["file"], f["line"], f["text"]) for f in found]
    [('item-without-requirement', 'C-03', 'spec.md', 69,
      'No requirement of the table Requirements goes to the item.')]
    >>> own = ("spec.md", "| 3, regulatory | authority (1) |", "| 3, regulatory | own rule (IX) |")
    >>> check_requirements(sample.load(other, own)), check_requirements(sample.load(other, retired))
    ([], [])

    Each stakeholder of section 1 has a requirement.

    >>> owners = sample.STAKEHOLDER_OWNERS
    >>> more = ("spec.md", owners, owners + "\n  - `auditors`: they examine the record. (judgement)")
    >>> found = check_requirements(sample.load(more))
    >>> [(f["rule"], f["id"], f["line"], f["text"]) for f in found]
    [('stakeholder-without-requirement', 'auditors', 30,
      "The stakeholder 'auditors' has no requirement in the table Requirements.")]

    A specification without the table, or with a table without a row, fails with one finding.

    >>> data = sample.load()
    >>> data["requirements"] = []
    >>> [(f["rule"], f["file"], f["line"], f["text"]) for f in check_requirements(data)]
    [('requirements-missing', 'vetting.md', 0, 'The table Requirements of vetting.md is absent or empty.')]
    """
    rows = data["requirements"]
    if not rows:
        return [finding("requirements-missing", {"_file": "vetting.md"})]
    out, seen, held, served = [], set(), set(), set()
    views = {v["name"] for v in data["views"]}
    holders = {s["name"] for s in data["stakeholders"]}
    known = {s.get("id") for s in data["sources"]}
    for row in rows:
        ident = row.get("id", "")
        for cell in REQUIREMENT_CELLS:
            if not row.get(cell, ""):
                out.append(finding("requirement-cell-empty", row, ident, cell))
        if ident in seen:
            out.append(finding("requirement-id-twice", row, ident))
        seen.add(ident)
        names = aspect.names_of(row.get("stakeholder"))
        served.update(names)
        for name in names:
            if name not in holders:
                out.append(finding("requirement-stakeholder-unknown", row, ident, name))
        view = aspect.view_of(row)
        if view and view not in views:
            out.append(finding("view-unknown", row, ident, view))
        cited = aspect.source_ids(row.get("source", ""))
        if row.get("source") and not cited:
            out.append(finding("requirement-without-source", row, ident))
        for sid in cited:
            if sid not in known:
                out.append(finding("unknown-source", row, ident, sid))
        if not row.get("goes to", ""):
            continue
        kind, name = aspect.exit_of(row["goes to"])
        if kind == "item":
            held.add(name)
        fault = exit_fault(data, kind, name)
        if fault:
            out.append(finding(fault, row, ident, name))
    for row in live_items(data):
        own = row.get("admitted by", "").strip().lower().startswith(OWN_RULE)
        if row.get("id") not in held and not own:
            out.append(finding("item-without-requirement", row, row.get("id", "")))
    for holder in data["stakeholders"]:
        if holder["name"] not in served:
            out.append(finding("stakeholder-without-requirement", holder, holder["name"], holder["name"]))
    return out


def requirement_counts(data):
    """For each view of section 1, by name: its requirements, and how many take each exit.

    >>> import sample
    >>> for view in requirement_counts(sample.load()):
    ...     print(*view.values())
    operation 6 3 1 1 0 1 0
    storage 2 2 0 0 0 0 0
    >>> list(view)
    ['view', 'requirements', 'to an item', 'to a decision', 'to an implementation skill', 'to a boundary',
     'duplicates', 'a proposed boundary would take']

    The last number is the number of requirements of the view that a proposed boundary would take.

    >>> named = ("spec.md", sample.BOUNDARIES, sample.BOUNDARIES_NAMED)
    >>> [view[WOULD_TAKE] for view in requirement_counts(sample.load(named, sample.PROPOSED_TABLE))]
    [1, 0]
    """
    out = []
    taken = {ident for ids in proposed_takes(data).values() for ident in ids}
    for view in sorted(data["views"], key=lambda v: (v["name"], v["_line"])):
        rows = [r for r in data["requirements"] if aspect.view_of(r) == view["name"]]
        kinds = [aspect.exit_of(r.get("goes to"))[0] for r in rows]
        exits = {words: kinds.count(kind) for kind, words in EXIT_WORDS.items()}
        exits[WOULD_TAKE] = sum(r.get("id", "") in taken for r in rows)
        out.append({"view": view["name"], "requirements": len(rows), **exits})
    return out


def views_emptied_by_boundaries(data):
    r"""The views with more than half of their requirements at a boundary, sorted.

    The owner sees such a view: the boundaries that the owner decided took most of what the
    sources state for it.

    >>> import sample
    >>> views_emptied_by_boundaries(sample.load())
    []
    >>> named = ("spec.md", sample.BOUNDARIES, sample.BOUNDARIES_NAMED)
    >>> row = sample.REQUIREMENT_R02
    >>> away = ("vetting.md", row, row.replace("| C-03 |", "| boundary: recovery |"))
    >>> views_emptied_by_boundaries(sample.load(named, away))
    []
    >>> more = ("vetting.md", "| none | C-01 |", "| none | boundary: recovery |")
    >>> views_emptied_by_boundaries(sample.load(named, away, more))
    ['storage']
    """
    counts = requirement_counts(data)
    return sorted({c["view"] for c in counts if 2 * c["to a boundary"] > c["requirements"]})


def check_charter(data):
    r"""The form of the charter: the file charter.md beside spec.md. Without the file, nothing fails.

    The head line has the state "draft" or "reviewed by the owner on <YYYY-MM-DD>". Each line has
    an identifier that is used one time: T-<n> in the table "Target", P-<n> in the table
    "Principles", K-<n> in the table "Constraints". Each principle has a priority, a whole number
    that is used one time. Each effect has one of the forms, and each level is 1, 2 or 3.

    >>> import sample
    >>> check_charter(sample.load())
    []
    >>> def planted(old, new):
    ...     found = check_charter(sample.load(("charter.md", old, new)))
    ...     return [(f["rule"], f["id"], f["file"], f["line"], f["text"]) for f in found]
    >>> planted(sample.CHARTER_STATE, "**State**: reviewed")
    [('charter-state-unknown', '', 'charter.md', 3,
      "The state 'reviewed' of the charter is not permitted. Use 'draft' or 'reviewed by the owner on
      <YYYY-MM-DD>'.")]
    >>> planted(sample.CHARTER_STATE, "**State**: draft"), planted(sample.CHARTER_STATE + "\n", "")[0][:2]
    ([], ('charter-state-unknown', ''))
    >>> planted("| 2 | P-2 |", "| 1 | P-2 |")
    [('charter-priority-twice', 'P-2', 'charter.md', 21,
      "The priority '1' is used two times. Give each principle a different priority.")]
    >>> planted("| 2 | P-2 |", "| | P-2 |"), planted("| 2 | P-2 |", "| high | P-2 |")[0][:2]
    ([('charter-priority-missing', 'P-2', 'charter.md', 21,
       'The principle has no priority. Write a whole number.')], ('charter-priority-missing', 'P-2'))
    >>> planted("| 2 | P-2 |", "| 2 | P-1 |")
    [('charter-id-twice', 'P-1', 'charter.md', 21,
      'The identifier of the line of the charter is used two times.')]
    >>> planted("| K-2 |", "| P-9 |")
    [('charter-id-unknown', 'P-9', 'charter.md', 28,
      "The identifier 'P-9' is not permitted in the table 'Constraints'. Use 'K-<n>'.")]
    >>> planted("| T-2 |", "| the goal |")[0][:2]
    ('charter-id-unknown', 'the goal')

    An effect that is none of the forms fails. A level that is not 1, 2 or 3 fails.

    >>> planted("| no exit: 3.3 |", "| the first claim on level 1 |")
    [('charter-effect-unknown', 'P-1', 'charter.md', 20,
      "The effect 'the first claim on level 1' is not permitted. Use 'level <n>', 'no exit: 3.3', 'no exit:
      boundary', 'no exit: not admitted', 'none' or 'none: rule of the factory'.")]
    >>> planted("| no exit: 3.3 |", "| |")[0][:2], planted("| no exit: 3.3 |", "| level 1; no exit: 3.3 |")
    (('charter-effect-unknown', 'P-1'), [])
    >>> planted("| no exit: 3.3 |", "| level 4 |")
    [('charter-level-unknown', 'P-1', 'charter.md', 20,
      "The level '4' of the line of the charter is not permitted. Use 1, 2 or 3.")]
    >>> planted("| no drill | 1 |", "| no drill | |")[0][:2]
    ('charter-level-unknown', 'T-1')

    A charter without a line fails. A specification without a charter does not fail.

    >>> folder = sample.folder()
    >>> _ = (folder / "charter.md").write_text("# Charter\n\n**State**: draft\n", encoding="utf-8")
    >>> [(f["rule"], f["line"], f["text"]) for f in check_charter(aspect.load(folder))]
    [('charter-without-line', 3,
      'The charter has no line. Write the tables Target, Principles and Constraints.')]
    >>> check_charter(sample.load(charter=False)), charter_remains(sample.load(charter=False))
    ([], ['The specification has no charter.'])
    """
    charter = data.get("charter")
    if charter is None:
        return []
    out, seen, priorities = [], set(), set()
    if charter["state"] is None:
        out.append(finding("charter-state-unknown", charter, "", charter["state text"]))
    if not charter["lines"]:
        out.append(finding("charter-without-line", charter))
    letters = {kind: letter for _, kind, letter in aspect.CHARTER_TABLES}
    for line in charter["lines"]:
        ident = line["id"]
        form = aspect.CHARTER_ID.fullmatch(ident)
        if not form or form.group(1) != letters[line["kind"]]:
            out.append(
                finding("charter-id-unknown", line, ident, ident, line["table"], letters[line["kind"]])
            )
        if ident in seen:
            out.append(finding("charter-id-twice", line, ident))
        seen.add(ident)
        priority = (line["priority"] or "").strip()
        if line["kind"] == "principle" and not priority.isdigit():
            out.append(finding("charter-priority-missing", line, ident))
        elif line["kind"] == "principle" and int(priority) in priorities:
            out.append(finding("charter-priority-twice", line, ident, priority))
        elif line["kind"] == "principle":
            priorities.add(int(priority))
        out += [finding("charter-effect-unknown", line, ident, part) for part in line["effect"]["unknown"]]
        out += [finding("charter-level-unknown", line, ident, n) for n in line["effect"]["wrong levels"]]
    return out


def charter_remains(data):
    """The lines of what remains for the state of the charter: no charter, or a draft.

    >>> import sample
    >>> charter_remains(sample.load())
    []
    >>> charter_remains(sample.load(sample.CHARTER_DRAFT))
    ['The owner did not review the charter.']
    >>> charter_remains({})
    ['The specification has no charter.']
    """
    charter = data.get("charter")
    if charter is None:
        return [MESSAGES["remains-no-charter"]]
    return [MESSAGES["remains-charter-draft"]] if charter["state"] == aspect.DRAFT else []


def final_exits(data):
    """The exit of each requirement, by its identifier: (kind, name). A duplicate has the exit of its row.

    >>> import sample
    >>> exits = final_exits(sample.load())
    >>> exits["R-05"], exits["R-06"], exits["R-07"]
    (('item', 'C-05'), ('item', 'C-05'), ('decision', 'How frequently to make a backup'))
    >>> final_exits(sample.load(("vetting.md", "| duplicate: R-05 |", "| duplicate: R-19 |")))["R-06"]
    ('duplicate', 'R-19')
    """
    exits = {row.get("id", ""): aspect.exit_of(row.get("goes to")) for row in data["requirements"]}
    return {
        ident: exits.get(name, (kind, name)) if kind == "duplicate" else (kind, name)
        for ident, (kind, name) in exits.items()
    }


def lines_served(data, row):
    """The lines of the charter that a requirement serves: those of its cell "Serves" that the charter has.

    >>> import sample
    >>> data = sample.load()
    >>> [[line["id"] for line in lines_served(data, row)] for row in data["requirements"][1:5]]
    [[], ['T-2', 'P-1'], [], ['T-1', 'P-2', 'K-1']]
    >>> lines_served({}, data["requirements"][2])
    []
    """
    known = {line["id"]: line for line in (data.get("charter") or {}).get("lines", [])}
    return [known[name] for name in aspect.serves_of(row.get("serves")) if name in known]


def charter_rules(data):
    r"""What the charter decides for the items, before the calculation of risk and reward.

    Returns two dictionaries. The first has the items that a line of the charter gives a level:
    {item: {"level": n, "by": the line}}. The second has the items that the charter does not
    permit to be "not admitted": {item: [(requirement, line)]}.

    For each item, take the requirements that go to it, and the lines of the charter that they
    serve. If one or more of these lines gives a level, the item is admitted, and its level is
    not higher than the lowest such level. The line with the lowest level is the line of the
    item. If two lines give that level, a constraint comes before a target part, and a target
    part before a principle; then the lowest identifier decides.

    The programs place.py and check.py use this function: the rule is written one time.

    >>> import sample
    >>> charter_rules(sample.load())
    ({'C-02': {'level': 2, 'by': 'T-2'}, 'C-05': {'level': 1, 'by': 'T-1'}}, {'C-05': [('R-05', 'K-1')]})

    A requirement that serves a line with a level gives the level to its item. A duplicate
    counts for the item of its row.

    >>> r04 = sample.SERVES_R04
    >>> charter_rules(sample.load(("vetting.md", r04, r04.replace("| none |", "| T-2, K-1 |"))))
    ({'C-02': {'level': 2, 'by': 'T-2'}, 'C-04': {'level': 2, 'by': 'T-2'},
      'C-05': {'level': 1, 'by': 'T-1'}}, {'C-04': [('R-04', 'K-1')], 'C-05': [('R-05', 'K-1')]})
    >>> second = ("vetting.md", "| none | duplicate: R-05 |", "| T-1 | duplicate: R-04 |")
    >>> charter_rules(sample.load(second))[0]["C-04"]
    {'level': 1, 'by': 'T-1'}

    The lowest level decides. If two lines give the same level, a constraint comes first, then
    a target part.

    >>> def line_of(effect_p1, effect_k2, serves):
    ...     edits = [("charter.md", "| no exit: 3.3 |", f"| {effect_p1} |")]
    ...     edits += [("charter.md", "| none: rule of the factory |", f"| {effect_k2} |")]
    ...     edits += [("vetting.md", r04, r04.replace("| none |", f"| {serves} |"))]
    ...     return charter_rules(sample.load(*edits))[0]["C-04"]
    >>> line_of("level 2", "level 2", "P-1, T-2, K-2"), line_of("level 2", "level 3", "P-1, T-2, K-2")
    ({'level': 2, 'by': 'K-2'}, {'level': 2, 'by': 'T-2'})
    >>> line_of("level 2", "none", "P-1"), line_of("level 3", "level 1", "T-2, P-1, K-2")
    ({'level': 2, 'by': 'P-1'}, {'level': 1, 'by': 'K-2'})

    A specification without a charter has no such item.

    >>> charter_rules(sample.load(charter=False))
    ({}, {})
    """
    order = {kind: n for n, kind in enumerate(aspect.KIND_ORDER)}
    exits = final_exits(data)
    places, admits = {}, {}
    for row in data["requirements"]:
        kind, item = exits.get(row.get("id", ""), (None, ""))
        for line in lines_served(data, row) if kind == "item" else ():
            level = line["effect"]["level"]
            key = (level, order[line["kind"]], aspect.charter_key(line["id"]))
            if level is not None and (item not in places or key < places[item][0]):
                places[item] = (key, line["id"])
            if "not admitted" in line["effect"]["no exit"]:
                admits.setdefault(item, []).append((row.get("id", ""), line["id"]))
    places = {item: {"level": key[0], "by": ident} for item, (key, ident) in sorted(places.items())}
    return places, {item: sorted(rows) for item, rows in sorted(admits.items())}


def placed_by(place, level):
    """The text of the cell "Placed by" of an item: the line of the charter that placed it, or "calculation".

    A line places an item when the item is on the level that the line gives. The calculation of
    risk and reward places an item on a lower level, and each item that no line gives a level.

    >>> place = {"level": 2, "by": "T-2"}
    >>> placed_by(place, 2), placed_by(place, 1), placed_by(None, 2), placed_by(place, "not admitted")
    ('T-2', 'calculation', 'calculation', 'calculation')
    """
    return place["by"] if place and level == place["level"] else aspect.CALCULATION


def served_by(data):
    """For each line of the charter, by its identifier: the requirements that serve it, sorted.

    >>> import sample
    >>> served_by(sample.load())
    {'T-1': ['R-05'], 'T-2': ['R-03'], 'P-1': ['R-03'], 'P-2': ['R-05'], 'K-1': ['R-05'], 'K-2': []}
    """
    out = {line["id"]: set() for line in (data.get("charter") or {}).get("lines", [])}
    for row in data["requirements"]:
        for line in lines_served(data, row):
            out[line["id"]].add(row.get("id", ""))
    return {ident: sorted(rows) for ident, rows in out.items()}


def charter_counts(data):
    """For each line of the charter: the number of requirements that serve it and of items that it placed.

    >>> import sample
    >>> for line in charter_counts(sample.load()):
    ...     print(*line.values())
    T-1 1 1
    T-2 1 1
    P-1 1 0
    P-2 1 0
    K-1 1 0
    K-2 0 0
    >>> list(line), charter_counts(sample.load(charter=False))
    (['line', 'requirements', 'items placed'], [])

    An item on a lower level than the level of its line was placed by the calculation.

    >>> higher = ("charter.md", "| no drill | 1 |", "| no drill | 2 |")
    >>> [line["items placed"] for line in charter_counts(sample.load(higher))][:2]
    [0, 1]
    """
    served = served_by(data)
    places = charter_rules(data)[0] if served else {}
    levels = (
        {row.get("id"): aspect.level_of(row.get("level"))[0] for row in live_items(data)} if served else {}
    )
    placed = [placed_by(places.get(ident), level) for ident, level in levels.items()]
    return [
        {"line": ident, "requirements": len(rows), "items placed": placed.count(ident)}
        for ident, rows in served.items()
    ]


def serving_none(data):
    """The number of requirements that serve no line of the charter, for each view. Sorted.

    A specification without a charter gives nothing.

    >>> import sample
    >>> serving_none(sample.load()), serving_none(sample.load(charter=False))
    (['operation: 4', 'storage: 2'], [])
    """
    counts = {}
    for row in data["requirements"] if data.get("charter") else ():
        if not lines_served(data, row):
            counts[aspect.view_of(row)] = counts.get(aspect.view_of(row), 0) + 1
    return [MESSAGES["serves-none-view"].format(view, n) for view, n in sorted(counts.items())]


def check_serves(data):
    r"""The charter governs the triage. Returns the findings, and the lines that no requirement serves.

    Without a charter, nothing fails and the cell "Serves" is not necessary. With a charter, each
    requirement has the cell: identifiers of lines of the charter, or "none".

    >>> import sample
    >>> check_serves(sample.load()), check_serves(sample.load(charter=False))
    (([], []), ([], []))
    >>> def planted(*edits):
    ...     found, unserved = check_serves(sample.load(*edits))
    ...     return [(f["rule"], f["id"], f["file"], f["text"]) for f in found], unserved
    >>> r02, r03, r04, r05 = sample.REQUIREMENT_R02, sample.SERVES_R03, sample.SERVES_R04, sample.SERVES_R05
    >>> planted(("vetting.md", r04, r04.replace("| none |", "| |")))
    ([('requirement-cell-empty', 'R-04', 'vetting.md', "The cell 'serves' of the requirement is empty.")], [])
    >>> planted(("vetting.md", r04, r04.replace("| none |", "| P-9, the first principle |")))[0]
    [('requirement-serves-unknown', 'R-04', 'vetting.md',
      "The requirement serves 'P-9'. The charter does not have this line. Write identifiers of the charter
      with a comma between them, or 'none'."),
     ('requirement-serves-unknown', 'R-04', 'vetting.md',
      "The requirement serves 'the first principle'. The charter does not have this line. Write identifiers
      of the charter with a comma between them, or 'none'.")]

    A requirement does not take an exit that a line that it serves closes: a decision that
    depends on context, or a boundary. A duplicate has the exit of its row.

    >>> decision = "3.3: How frequently to make a backup"
    >>> planted(("vetting.md", r03, r03.replace("| C-02 |", f"| {decision} |")))[0][0]
    ('requirement-exit-closed', 'R-03', 'vetting.md',
     "The requirement serves 'P-1'. This line of the charter does not permit the exit '3.3'. Give the
     requirement a different exit.")
    >>> named = ("spec.md", sample.BOUNDARIES, sample.BOUNDARIES_NAMED)
    >>> planted(named, ("vetting.md", r05, r05.replace("| C-05 |", "| boundary: recovery |")))[0][0][::3]
    ('requirement-exit-closed', "The requirement serves 'P-2'. This line of the charter does not permit the
    exit 'boundary'. Give the requirement a different exit.")
    >>> second = ("vetting.md", "| none | duplicate: R-05 |", "| P-1 | duplicate: R-07 |")
    >>> [f[:2] for f in planted(second)[0]]
    [('requirement-exit-closed', 'R-06')]

    An item that holds a requirement that serves a line with "no exit: not admitted" is admitted.

    >>> planted(("vetting.md", r04, r04.replace("| none |", "| K-1 |")))[0]
    [('item-not-admitted-against-charter', 'C-04', 'spec.md',
      "The item is not admitted. It holds 'R-04', which serves 'K-1'. This line of the charter does not
      permit that. Run place.py with --write.")]

    An item that a line gives a level is admitted, and its level is not higher than that level.

    >>> planted(("vetting.md", r04, r04.replace("| none |", "| T-2 |")))[0]
    [('item-above-charter-level', 'C-04', 'spec.md',
      "The level of the item is 'not admitted'. The line 'T-2' of the charter gives it level 2 or a lower
      level. Run place.py with --write.")]
    >>> planted(("vetting.md", r02, r02.replace("| none |", "| T-2 |")))[0]
    [('item-above-charter-level', 'C-03', 'spec.md',
      "The level of the item is '3, regulatory'. The line 'T-2' of the charter gives it level 2 or a lower
      level. Run place.py with --write.")]

    The cell "Placed by" names the line that placed the item, or "calculation". The calculation
    placed an item that is on a lower level than the level of its line. The cell of an item with
    a pending level is not examined.

    >>> planted(("spec.md", "| S-02 section 4 | T-2 |", "| S-02 section 4 | calculation |"))[0]
    [('placed-by-differs', 'C-02', 'spec.md',
      "The cell 'Placed by' is 'calculation'. The program place.py computes 'T-2'. Run place.py with
      --write.")]
    >>> planted(("charter.md", "| no drill | 1 |", "| no drill | 2 |"))[0]
    [('placed-by-differs', 'C-05', 'spec.md',
      "The cell 'Placed by' is 'T-1'. The program place.py computes 'calculation'. Run place.py with
      --write.")]
    >>> planted(("spec.md", "| 2, operative |", "| pending |"))
    ([], [])

    A line that no requirement serves fails after the review of the owner. While the charter is
    a draft, the line remains. A line that is a rule of the factory needs no requirement.

    >>> rule = ("charter.md", "| none: rule of the factory |", "| none |")
    >>> planted(rule)
    ([('charter-line-unserved', 'K-2', 'charter.md', "No requirement serves the line 'K-2' of the charter.")],
     [])
    >>> planted(rule, sample.CHARTER_DRAFT), planted(sample.CHARTER_DRAFT)
    (([], ['K-2']), ([], []))
    """
    charter = data.get("charter")
    if charter is None:
        return [], []
    out = []
    known = {line["id"] for line in charter["lines"]}
    exits = final_exits(data)
    for row in data["requirements"]:
        ident = row.get("id", "")
        if not row.get("serves", ""):
            out.append(finding("requirement-cell-empty", row, ident, "serves"))
        out += [
            finding("requirement-serves-unknown", row, ident, name)
            for name in aspect.serves_of(row.get("serves"))
            if name not in known
        ]
        closed = aspect.CLOSED_EXITS.get(exits.get(ident, (None, ""))[0])
        out += [
            finding("requirement-exit-closed", row, ident, line["id"], closed)
            for line in lines_served(data, row)
            if closed in line["effect"]["no exit"]
        ]
    places, admits = charter_rules(data)
    for row in live_items(data):
        ident = row.get("id", "")
        level = aspect.level_of(row.get("level"))[0]
        decided = isinstance(level, int) or level == "not admitted"
        place = places.get(ident)
        if level == "not admitted":
            rule = "item-not-admitted-against-charter"
            out += [finding(rule, row, ident, *names) for names in admits.get(ident, [])]
        if place and decided and (level == "not admitted" or level > place["level"]):
            cell = row.get("level", "").strip()
            out.append(finding("item-above-charter-level", row, ident, cell, place["by"], place["level"]))
        cell = row.get("placed by", "").strip().strip("`").strip()
        if decided and cell != placed_by(place, level):
            out.append(finding("placed-by-differs", row, ident, cell, placed_by(place, level)))
    served = served_by(data)
    unserved = [line for line in charter["lines"] if not served[line["id"]] and not line["effect"]["factory"]]
    if charter["state"] == aspect.REVIEWED:
        return out + [finding("charter-line-unserved", line, line["id"], line["id"]) for line in unserved], []
    return out, [line["id"] for line in unserved]


def check_basics(data):
    r"""Each view needs its basic practices: an item on level 1.

    Returns the findings, and the views that wait while a level is pending. A view without an
    item is the finding of check_views, not of this rule.

    >>> import sample
    >>> check_basics(sample.load())
    ([], [])
    >>> c01, above = "| storage | 1 | authority (2) |", "| storage | 2, regulatory | authority (2) |"
    >>> found, waiting = check_basics(sample.load(("spec.md", c01, above)))
    >>> brief(found), found[0]["line"], found[0]["text"], waiting
    ([('view-without-basics', 'storage')], 12, "The view 'storage' has no item on level 1.", [])

    While a level is pending, the calculation can still give the view an item on level 1.

    >>> check_basics(sample.load(("spec.md", c01, "| storage | pending | authority (2) |")))
    ([], ['storage'])
    >>> other = ("spec.md", "| 2, operative |", "| pending |")
    >>> check_basics(sample.load(("spec.md", c01, above), other))
    ([], ['storage'])
    >>> storage = sample.VIEW_STORAGE
    >>> quality = storage + "\n  - `quality`: how the copies are examined. (judgement)"
    >>> check_basics(sample.load(("spec.md", storage, quality)))
    ([], [])
    """
    names = [c["view"] for c in view_counts(data) if c["items"] and not c["level 1"]]
    if any(aspect.level_of(r.get("level"))[0] == "pending" for r in live_items(data)):
        return [], names
    places = {v["name"]: v for v in reversed(data["views"])}
    return [finding("view-without-basics", places[name], name, name) for name in names], []


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


def viewpoints(path=VIEWPOINTS_FILE):
    r"""The names of the viewpoints of the review, or None if the file is absent.

    >>> len(viewpoints()), len(set(viewpoints()))
    (7, 7)
    >>> import sample
    >>> path = sample.folder() / "viewpoints.txt"
    >>> viewpoints(path)
    >>> _ = path.write_text("first name\n\n second \n", encoding="utf-8")
    >>> viewpoints(path)
    ['first name', 'second']
    """
    if not pathlib.Path(path).is_file():
        return None
    return [line.strip() for line in aspect.read_text(path).splitlines() if line.strip()]


def unchecked_viewpoints(data, path=VIEWPOINTS_FILE):
    """The findings of the trials whose viewpoint was not checked: the list of the viewpoints is absent.

    >>> import sample
    >>> unchecked_viewpoints(sample.load()), unchecked_viewpoints(sample.load(), "absent.txt")
    ([], ['F-01', 'F-02'])
    """
    if viewpoints(path) is not None:
        return []
    return sorted(row.get("id", "") for row in data["trial_findings"])


def check_trials(data, path=VIEWPOINTS_FILE):
    """The record of the trials: each finding names a trial, a viewpoint, a route and a status.

    >>> import sample
    >>> check_trials(sample.load())
    []
    >>> def planted(old, new):
    ...     row = sample.FINDING_F01
    ...     return check_trials(sample.load(("trial.md", row, row.replace(old, new))))
    >>> found = planted("| T-01 |", "| T-07 |")
    >>> brief(found), found[0]["file"], found[0]["line"], found[0]["text"]
    ([('trial-unknown', 'F-01')], 'trial.md', 13,
     "The finding names the trial 'T-07'. The table Trials does not have this trial.")
    >>> viewpoint = sample.load()["trial_findings"][0]["viewpoint"]
    >>> planted(f"| {viewpoint} |", "| No Such Viewpoint |")[0]["text"]
    "The viewpoint 'No Such Viewpoint' is not one of the seven viewpoints."

    Without the list of the viewpoints, as in a kit that export.py made, the viewpoint is not checked.

    >>> row = sample.FINDING_F01
    >>> data = sample.load(("trial.md", row, row.replace(f"| {viewpoint} |", "| No Such Viewpoint |")))
    >>> check_trials(data, "absent.txt")
    []
    >>> planted("The plan has no step that examines the restored data.", "")[0]["text"]
    'The finding of the trial has no text.'
    >>> planted("| recipe |", "| research |")[0]["text"]
    "The route 'research' is not permitted. Use recipe, tooling or implementation skill."

    The status is "open", "corrected in" with a revision or a commit, or "declined:" with a reason.

    >>> for status in ("open", "corrected in revision 2026-02", "done", "corrected in", "declined:", ""):
    ...     print(repr(status), brief(planted("corrected in abc1235", status)))
    'open' []
    'corrected in revision 2026-02' []
    'done' [('trial-status-unknown', 'F-01')]
    'corrected in' [('trial-status-unknown', 'F-01')]
    'declined:' [('trial-status-unknown', 'F-01')]
    '' [('trial-status-unknown', 'F-01')]

    A specification without a record of the trials has no such finding.

    >>> data = sample.load()
    >>> data["trials"] = data["trial_findings"] = []
    >>> check_trials(data)
    []
    """
    out = []
    permitted = viewpoints(path)
    known = {t.get("id", "") for t in data["trials"]}
    for row in data["trial_findings"]:
        ident = row.get("id", "")
        names = ("trial", "viewpoint", "finding", "route", "status")
        cell = {name: row.get(name, "").strip() for name in names}
        if cell["trial"] not in known:
            out.append(finding("trial-unknown", row, ident, cell["trial"]))
        if permitted is not None and cell["viewpoint"] not in permitted:
            out.append(finding("trial-viewpoint-unknown", row, ident, cell["viewpoint"]))
        if not cell["finding"]:
            out.append(finding("trial-finding-empty", row, ident))
        if cell["route"] not in ROUTES:
            out.append(finding("trial-route-unknown", row, ident, cell["route"]))
        if not STATUS.fullmatch(cell["status"]):
            out.append(finding("trial-status-unknown", row, ident, cell["status"]))
    return out


def open_findings(data):
    """The findings of the trials that the owner did not decide yet, sorted.

    >>> import sample
    >>> open_findings(sample.load())
    []
    >>> open_findings(sample.load(("trial.md", "| recipe | corrected in abc1235 |", "| recipe | open |")))
    ['F-01']
    """
    return sorted(r.get("id", "") for r in data["trial_findings"] if r.get("status", "").strip() == "open")


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


def run_checks(data, previous_rows=None, words=(), viewpoints_file=VIEWPOINTS_FILE):
    """All findings, sorted, and what remains.

    >>> import sample
    >>> found, remains = run_checks(sample.load())
    >>> found, remains
    ([], {'levels': [], 'basics': [], 'vettings': [], 'waiting': [], 'judgement': ['C-04'], 'changed': [],
          'trial': [], 'viewpoints': [], 'stakeholders': [], 'boundaries': [], 'proposed-boundaries': [],
          'left-stakeholders': [], 'own-sources': [], 'unread': [], 'charter-unserved': [],
          'serves-none': ['operation: 4', 'storage: 2']})

    A view that the boundaries emptied remains. A view with fewer than two sources of its own
    field remains also.

    >>> named = sample.BOUNDARIES + chr(10) + sample.BOUNDARY_DECIDED
    >>> away = [
    ...     ("vetting.md", f"| none | C-0{c} |", "| none | boundary: recovery |") for c in (1, 3)
    ... ]
    >>> whole = ("spec.md", "| public | full | storage, operation |", "| public | full | all |")
    >>> found, remains = run_checks(sample.load(("spec.md", sample.BOUNDARIES, named), whole, *away))
    >>> brief(found), remains["boundaries"], remains["own-sources"]
    ([('item-without-requirement', 'C-01'), ('item-without-requirement', 'C-03')], ['storage'], ['storage'])

    A proposed boundary remains, with the number of requirements that it would take. A
    stakeholder that it would leave with no requirement in the aspect remains also. A requirement
    that goes to a proposed boundary fails the check.

    >>> named = ("spec.md", sample.BOUNDARIES, sample.BOUNDARIES_NAMED)
    >>> row = sample.PROPOSED_ARCHIVE
    >>> more = ("vetting.md", row, row.replace("| none | none |", "| R-01, R-02 | owners of the data |"))
    >>> found, remains = run_checks(sample.load(named, sample.PROPOSED_TABLE, more))
    >>> found, remains["proposed-boundaries"], remains["left-stakeholders"]
    ([], ['tests (1 requirements)', 'archive (2 requirements)'], [['archive', 'owners of the data']])
    >>> exit = ("vetting.md", "| none | C-03 |", "| none | boundary: archive |")
    >>> found, remains = run_checks(sample.load(named, sample.PROPOSED_TABLE, exit))
    >>> brief(found), remains["proposed-boundaries"]
    ([('item-without-requirement', 'C-03'), ('requirement-boundary-not-decided', 'R-02')],
     ['tests (1 requirements)', 'archive (1 requirements)'])

    What remains does not fail the check: a pending level, a pending vetting, a changed text.

    >>> level = ("spec.md", "| 2, operative |", "| pending |")
    >>> vetting = ("vetting.md", sample.CONFIRMED_S04, "| 8 of 10 | 2026-01-10 | pending |")
    >>> found, remains = run_checks(sample.load(level, vetting))
    >>> found, remains["levels"], remains["vettings"]
    ([], ['C-02'], ['S-04'])

    A view without an item on level 1 remains while a level is pending. Then it fails the check.

    >>> basic = ("spec.md", "| storage | 1 | authority (2) |", "| storage | 2, regulatory | authority (2) |")
    >>> found, remains = run_checks(sample.load(basic, level))
    >>> found, remains["basics"]
    ([], ['storage'])
    >>> found, remains = run_checks(sample.load(basic))
    >>> brief(found), remains["basics"]
    ([('view-without-basics', 'storage')], [])

    A finding of a trial that is open remains. A finding with a defect fails the check.

    >>> status = "| recipe | corrected in abc1235 |"
    >>> found, remains = run_checks(sample.load(("trial.md", status, "| recipe | open |")))
    >>> found, remains["trial"]
    ([], ['F-01'])
    >>> brief(run_checks(sample.load(("trial.md", status, "| recipe | later |")))[0])
    [('trial-status-unknown', 'F-01')]

    Without the list of the viewpoints, the findings whose viewpoint was not checked remain.

    >>> found, remains = run_checks(sample.load(), viewpoints_file="absent.txt")
    >>> found, remains["viewpoints"]
    ([], ['F-01', 'F-02'])

    The findings of all rules come in the order of the file and the line.

    >>> level, cell = ("spec.md", "| 2, operative |", "| high |"), ("spec.md", "| Example Journal |", "| |")
    >>> two = sample.load(level, cell)
    >>> [(f["line"], f["rule"]) for f in run_checks(two, None, ["program"])[0]]
    [(36, 'source-cell-empty'), (68, 'level-unknown'), (71, 'product-word')]
    """
    support, waiting = check_support(data)
    basics, without_basics = check_basics(data)
    serves, unserved = check_serves(data)
    found = (
        check_scope(data)
        + check_charter(data)
        + serves
        + check_scope_findings(data)
        + check_sources(data)
        + check_references(data)
        + check_items(data)
        + check_views(data)
        + check_stakeholders(data)
        + check_requirements(data)
        + check_boundaries(data)
        + check_reading(data)
        + basics
        + check_evidence(data)
        + check_other_sections(data)
        + check_skill(data)
        + check_trials(data, viewpoints_file)
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
        "basics": without_basics,
        "vettings": sorted(
            s["id"] for s in data["sources"] if s.get("class") == "independent" and s["id"] not in confirmed
        ),
        "waiting": waiting,
        "judgement": sorted(r["id"] for r in live if r.get("check", "").strip().lower() == "judgement"),
        "changed": changed,
        "trial": open_findings(data),
        "viewpoints": unchecked_viewpoints(data, viewpoints_file),
        "stakeholders": stakeholders_without_view(data),
        "boundaries": views_emptied_by_boundaries(data),
        "proposed-boundaries": waiting_boundaries(data),
        "left-stakeholders": left_stakeholders(data),
        "own-sources": views_with_few_sources(data),
        "unread": unread_sources(data),
        "charter-unserved": unserved,
        "serves-none": serving_none(data),
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
    r"""The text report: the failing rules, the views, the requirements, then what remains.

    >>> import sample
    >>> data = sample.load()
    >>> print(report(data, *run_checks(data), previous_given=False))
    No check fails.
    Views, with the number of items on each level, of sources and of stakeholders:
    - operation: level 1: 1, level 2: 1, level 3: 0, pending: 0, not admitted: 1, sources: 4, stakeholders: 1,
      sources read for the view: 4.
    - storage: level 1: 1, level 2: 0, level 3: 1, pending: 0, not admitted: 0, sources: 2, stakeholders: 1,
      sources read for the view: 2.
    Requirements of the sources, with the number for each view and where they go:
    - operation: requirements: 6, to an item: 3, to a decision: 1, to an implementation skill: 1,
      to a boundary: 0, duplicates: 1, a proposed boundary would take: 0.
    - storage: requirements: 2, to an item: 2, to a decision: 0, to an implementation skill: 0,
      to a boundary: 0, duplicates: 0, a proposed boundary would take: 0.
    Charter, with the number of requirements that serve each line and of items that it placed:
    - T-1: requirements: 1, items placed: 1.
    - T-2: requirements: 1, items placed: 1.
    - P-1: requirements: 1, items placed: 0.
    - P-2: requirements: 1, items placed: 0.
    - K-1: requirements: 1, items placed: 0.
    - K-2: requirements: 0, items placed: 0.
    Answers of risk and reward: 8 with a source, 22 by judgement.
    What remains:
    - Items that need judgement: C-04.
    - Requirements that serve no line of the charter, for each view: operation: 4, storage: 2.
    Accepted: A. Person, 2026-01-15.
    The check of stable identifiers was skipped: no earlier revision was given.

    >>> data = sample.load(
    ...     ("spec.md", "| S-02 section 4 |", "| S-09 section 4 |"),
    ...     ("spec.md", "**Accepted**: A. Person, 2026-01-15", "**Accepted**: pending"),
    ...     ("spec.md", "| judgement |", "| the review is in the record |"),
    ... )
    >>> print(report(data, *run_checks(data, data["checklist"]), previous_given=True))
    FAIL unknown-source spec.md:68 C-02: The row cites 'S-09'. Section 2 does not list this source.
    Failing checks: 1.
    Views, with the number of items on each level, of sources and of stakeholders:
    - operation: level 1: 1, level 2: 1, level 3: 0, pending: 0, not admitted: 1, sources: 4, stakeholders: 1,
      sources read for the view: 4.
    - storage: level 1: 1, level 2: 0, level 3: 1, pending: 0, not admitted: 0, sources: 2, stakeholders: 1,
      sources read for the view: 2.
    Requirements of the sources, with the number for each view and where they go:
    - operation: requirements: 6, to an item: 3, to a decision: 1, to an implementation skill: 1,
      to a boundary: 0, duplicates: 1, a proposed boundary would take: 0.
    - storage: requirements: 2, to an item: 2, to a decision: 0, to an implementation skill: 0,
      to a boundary: 0, duplicates: 0, a proposed boundary would take: 0.
    Charter, with the number of requirements that serve each line and of items that it placed:
    - T-1: requirements: 1, items placed: 1.
    - T-2: requirements: 1, items placed: 1.
    - P-1: requirements: 1, items placed: 0.
    - P-2: requirements: 1, items placed: 0.
    - K-1: requirements: 1, items placed: 0.
    - K-2: requirements: 0, items placed: 0.
    Answers of risk and reward: 8 with a source, 22 by judgement.
    What remains:
    - Requirements that serve no line of the charter, for each view: operation: 4, storage: 2.
    - The owner did not accept the specification.

    When nothing remains, the report is short. A specification without a view has no such part.
    A specification without answers of risk and reward has no line for them.

    >>> data = sample.load(("spec.md", "| judgement |", "| the review is in the record |"))
    >>> data["views"] = data["stakeholders"] = data["vetting_items"] = data["requirements"] = []
    >>> print(report(data, [], run_checks(data, data["checklist"])[1], previous_given=True))
    No check fails.
    Charter, with the number of requirements that serve each line and of items that it placed:
    - T-1: requirements: 0, items placed: 0.
    - T-2: requirements: 0, items placed: 0.
    - P-1: requirements: 0, items placed: 0.
    - P-2: requirements: 0, items placed: 0.
    - K-1: requirements: 0, items placed: 0.
    - K-2: requirements: 0, items placed: 0.
    Accepted: A. Person, 2026-01-15.

    A specification without a charter has no part "Charter". This remains. A charter that the
    owner did not review remains also, with each line that no requirement serves.

    >>> data = sample.load(charter=False)
    >>> print("\n".join(report(data, *run_checks(data), previous_given=True).splitlines()[7:]))
    Answers of risk and reward: 8 with a source, 22 by judgement.
    What remains:
    - The specification has no charter.
    - Items that need judgement: C-04.
    Accepted: A. Person, 2026-01-15.
    >>> rule = ("charter.md", "| none: rule of the factory |", "| none |")
    >>> data = sample.load(sample.CHARTER_DRAFT, rule)
    >>> print("\n".join(report(data, *run_checks(data), previous_given=True).splitlines()[15:]))
    What remains:
    - The owner did not review the charter.
    - Items that need judgement: C-04.
    - Lines of the charter that no requirement serves: K-2.
    - Requirements that serve no line of the charter, for each view: operation: 4, storage: 2.
    Accepted: A. Person, 2026-01-15.

    A failure of a rule of the charter names the file of its row.

    >>> data = sample.load(("charter.md", "| 2 | P-2 |", "| 1 | P-2 |"), rule)
    >>> print("\n".join(report(data, *run_checks(data), previous_given=True).splitlines()[:3]))
    FAIL charter-priority-twice charter.md:21 P-2: The priority '1' is used two times. Give each principle a
    different priority.
    FAIL charter-line-unserved charter.md:28 K-2: No requirement serves the line 'K-2' of the charter.
    Failing checks: 2.

    A stakeholder that is in no view remains. An intent of the owner that was not asked remains.

    >>> owners = sample.STAKEHOLDER_OWNERS
    >>> more = ("spec.md", owners, owners + "\n  - `auditors`: they examine the record. (judgement)")
    >>> none = [("spec.md", line, line.split(":")[0] + ": (no answer)") for line in sample.INTENT[:2]]
    >>> data = sample.load(more, *none)
    >>> print("\n".join(report(data, *run_checks(data), previous_given=True).splitlines()[0:2]))
    FAIL stakeholder-without-requirement spec.md:30 auditors: The stakeholder 'auditors' has no requirement
    in the table Requirements.
    Failing checks: 1.
    >>> print("\n".join(report(data, *run_checks(data), previous_given=True).splitlines()[16:20]))
    What remains:
    - The intent of the owner was not asked.
    - Items that need judgement: C-04.
    - Stakeholders that are in no view: auditors.

    A view that the boundaries emptied remains, with one line for each view. A view with fewer
    than two sources of its own field remains also.

    >>> named = sample.BOUNDARIES + "\n" + sample.BOUNDARY_DECIDED
    >>> row = sample.REQUIREMENT_R02
    >>> away = ("vetting.md", "| none | C-01 |", "| none | boundary: recovery |")
    >>> second = ("vetting.md", "| S-02 section 4 | T-2, P-1 | C-02 |", "| S-02 section 4 | none | C-01 |")
    >>> third = ("vetting.md", row, row.replace("| C-03 |", "| boundary: recovery |"))
    >>> fourth = ("vetting.md", sample.SERVES_R05, "| S-01 section 3 | none | C-03 |")
    >>> fifth = ("vetting.md", "| duplicate: R-05 |", "| C-05 |")
    >>> sixth = ("vetting.md", sample.SERVES_R04, '| S-03 "After the drill" | none | C-02 |')
    >>> own = ("spec.md", "| not admitted | practice |", "| not admitted | own rule, constitution IX |")
    >>> whole = ("spec.md", "| public | full | storage, operation |", "| public | full | all |")
    >>> edits = (("spec.md", sample.BOUNDARIES, named), away, second, third, fourth, fifth, sixth, own, whole)
    >>> data = sample.load(*edits, charter=False)
    >>> lines = report(data, *run_checks(data), previous_given=True).splitlines()
    >>> print("\n".join([lines[0], lines[6], *lines[8:]]))
    No check fails.
    - storage: requirements: 2, to an item: 0, to a decision: 0, to an implementation skill: 0,
      to a boundary: 2, duplicates: 0, a proposed boundary would take: 0.
    What remains:
    - The specification has no charter.
    - Items that need judgement: C-04.
    - More than half of the requirements of the view 'storage' go to a boundary.
    - Views with fewer than two sources of their own field that were read: storage.
    Accepted: A. Person, 2026-01-15.

    A proposed boundary remains, with the number of requirements that it would take. The part
    "Requirements" gives that number for each view. A stakeholder that a proposed boundary would
    leave with no requirement in the aspect remains, with one line for each.

    >>> named = ("spec.md", sample.BOUNDARIES, sample.BOUNDARIES_NAMED)
    >>> row = sample.PROPOSED_ARCHIVE
    >>> more = ("vetting.md", row, row.replace("| none | none |", "| R-01, R-02 | owners of the data |"))
    >>> data = sample.load(named, sample.PROPOSED_TABLE, more)
    >>> lines = report(data, *run_checks(data), previous_given=True).splitlines()
    >>> print("\n".join([lines[0], *lines[5:7], *lines[15:]]))
    No check fails.
    - operation: requirements: 6, to an item: 3, to a decision: 1, to an implementation skill: 1,
      to a boundary: 0, duplicates: 1, a proposed boundary would take: 1.
    - storage: requirements: 2, to an item: 2, to a decision: 0, to an implementation skill: 0,
      to a boundary: 0, duplicates: 0, a proposed boundary would take: 2.
    What remains:
    - Items that need judgement: C-04.
    - Boundaries that wait for the decision of the owner: tests (1 requirements), archive (2 requirements).
    - The boundary 'archive' would leave the stakeholder 'owners of the data' with no requirement in the
      aspect.
    - Requirements that serve no line of the charter, for each view: operation: 4, storage: 2.
    Accepted: A. Person, 2026-01-15.

    An open finding of a trial remains. A recipe without a trial remains also.

    >>> data = sample.load(("trial.md", "| recipe | corrected in abc1235 |", "| recipe | open |"))
    >>> print("\n".join(report(data, *run_checks(data), previous_given=True).splitlines()[15:]))
    What remains:
    - Items that need judgement: C-04.
    - Trial findings that are open: F-01.
    - Requirements that serve no line of the charter, for each view: operation: 4, storage: 2.
    Accepted: A. Person, 2026-01-15.
    >>> folder = sample.folder()
    >>> (folder / "trial.md").unlink()
    >>> data = aspect.load(folder)
    >>> print("\n".join(report(data, *run_checks(data), previous_given=True).splitlines()[15:]))
    What remains:
    - Items that need judgement: C-04.
    - Requirements that serve no line of the charter, for each view: operation: 4, storage: 2.
    - The recipe has no trial.
    Accepted: A. Person, 2026-01-15.

    In a kit without the list of the viewpoints, one line says that the viewpoints were not checked.

    >>> data = sample.load()
    >>> found, remains = run_checks(data, viewpoints_file="absent.txt")
    >>> print("\n".join(report(data, found, remains, previous_given=True).splitlines()[15:18]))
    What remains:
    - Items that need judgement: C-04.
    - Trial findings with a viewpoint that was not checked: F-01, F-02. The list is absent.

    A source with pages that no reader got remains. A source that says "full" fails also. A
    specification without the table "Reading" remains.

    >>> left = ("vetting.md", sample.READING_S01, "| S-01 | S-01 | 6 | 1-2, 6 | 3-5 |")
    >>> data = sample.load(left)
    >>> lines = report(data, *run_checks(data), previous_given=True).splitlines()
    >>> print("\n".join([*lines[:2], *lines[16:19]]))
    FAIL full-with-unread-pages spec.md:35 S-01: The source says 'full'. The table Reading names pages that
    no reader got: 3-5.
    Failing checks: 1.
    What remains:
    - Items that need judgement: C-04.
    - Sources with pages that no reader got: S-01 (3 pages).
    >>> data = sample.load(("vetting.md", "## Reading", "## Other"))
    >>> print("\n".join(report(data, *run_checks(data), previous_given=True).splitlines()[15:19]))
    What remains:
    - Items that need judgement: C-04.
    - Requirements that serve no line of the charter, for each view: operation: 4, storage: 2.
    - The table Reading is absent. Run index.py unread with --write.

    A view that waits for the levels is in the list of what remains.

    >>> c01 = ("spec.md", "| storage | 1 | authority (2) |", "| storage | pending | authority (2) |")
    >>> data = sample.load(c01)
    >>> lines = report(data, *run_checks(data), previous_given=True).splitlines()
    >>> print("\n".join(lines[2:4] + lines[14:18]))
    - operation: level 1: 1, level 2: 1, level 3: 0, pending: 0, not admitted: 1, sources: 4, stakeholders: 1,
      sources read for the view: 4.
    - storage: level 1: 0, level 2: 0, level 3: 1, pending: 1, not admitted: 0, sources: 2, stakeholders: 1,
      sources read for the view: 2.
    Answers of risk and reward: 8 with a source, 22 by judgement.
    What remains:
    - Levels that are pending: C-01.
    - Views without an item on level 1, while levels are pending: storage.
    """
    lines = [
        f"FAIL {f['rule']} {f['file']}:{f['line']} {f['id']}: {f['text']}".replace(" : ", ": ") for f in found
    ]
    lines.append(MESSAGES["failures"].format(len(found)) if found else MESSAGES["no-failure"])
    keys = ("view", "level 1", "level 2", "level 3", "pending", "not admitted", "sources", "stakeholders")
    keys += ("sources read for the view",)
    views = ["- " + MESSAGES["view-line"].format(*(v[k] for k in keys)) for v in view_counts(data)]
    if views:
        lines += [MESSAGES["views-head"], *views]
    keys = ("view", "requirements", *EXIT_WORDS.values(), WOULD_TAKE)
    counts = requirement_counts(data) if data["requirements"] else []
    if counts:
        lines.append(MESSAGES["requirements-head"])
        lines += ["- " + MESSAGES["requirement-line"].format(*(c[k] for k in keys)) for c in counts]
    lines += charter_lines(data) + answer_lines(data)
    rest = ([] if intent_asked(data) else [MESSAGES["remains-intent"]]) + charter_remains(data)
    for key, ids in remains.items():
        if key in ONE_LINE_EACH:
            # One line for each entry. An entry is one name, or a list with one name for each place.
            rest += [MESSAGES[f"remains-{key}"].format(*([e] if isinstance(e, str) else e)) for e in ids]
        elif ids:
            rest.append(MESSAGES[f"remains-{key}"].format(", ".join(ids)))
    if reading_absent(data):
        rest.append(MESSAGES["remains-no-reading"])
    if not data["trials"]:
        rest.append(MESSAGES["remains-no-trial"])
    if not is_accepted(data):
        rest.append(MESSAGES["remains-accepted"])
    if rest:
        lines += [MESSAGES["remains-head"], *("- " + r for r in rest)]
    if is_accepted(data):
        lines.append(MESSAGES["accepted"].format(data["head"]["accepted"]))
    if not previous_given:
        lines.append(MESSAGES["previous-skipped"])
    return "\n".join(lines)


def charter_lines(data):
    """The part "Charter" of the report: one line for each line of the charter. No charter gives no line.

    >>> import sample
    >>> print(chr(10).join(charter_lines(sample.load())[:3]))
    Charter, with the number of requirements that serve each line and of items that it placed:
    - T-1: requirements: 1, items placed: 1.
    - T-2: requirements: 1, items placed: 1.
    >>> charter_lines({"requirements": []})
    []
    """
    counts = charter_counts(data)
    lines = ["- " + MESSAGES["charter-line"].format(*line.values()) for line in counts]
    return [MESSAGES["charter-head"], *lines] if lines else []


def answer_lines(data):
    """The lines of the report for the answers of risk and reward. No answer gives no line.

    >>> import sample
    >>> answer_lines(sample.load())
    ['Answers of risk and reward: 8 with a source, 22 by judgement.']
    >>> row = "| C-04 | 1 (judgement) | 1 (judgement) |"
    >>> answer_lines(sample.load(("vetting.md", row, "| C-04 | 1 (owner) | 1 |")))[1]
    "Answers of risk and reward without a source and without 'judgement': 2."
    >>> answer_lines({"vetting_items": []})
    []
    """
    counts = answer_counts(data)
    if not any(counts.values()):
        return []
    lines = [MESSAGES["answers"].format(counts["source"], counts["judgement"])]
    if counts["other"]:
        lines.append(MESSAGES["answers-other"].format(counts["other"]))
    return lines


def scope_report(data):
    """The report of phase 1: only what is settled before the research.

    That is the head line, the aspect, the field, the intent of the owner and the date of the
    agreement. The other parts of the sample have a defect here. The scope is correct, so nothing
    fails.

    >>> import sample
    >>> print(scope_report(sample.load(("spec.md", "| S-02 section 4 |", "| S-09 section 4 |"))))
    No check fails.
    Only the field and the thing to build were checked. The findings wait for the research.
    >>> old = "- **Aspect**: backups of the data of a software project."
    >>> print(scope_report(sample.load(("spec.md", old, "- **Aspect**:"))))
    FAIL aspect-field-empty spec.md:9: The field 'aspect' of section 1 is empty.
    Failing checks: 1.
    Only the field and the thing to build were checked. The findings wait for the research.

    A charter that exists must have the right form. The lines that no requirement serves are not
    examined: the register is empty in phase 1. A charter that the owner did not review remains.
    A specification without a charter remains also.

    >>> state = ("charter.md", sample.CHARTER_STATE, "**State**: accepted")
    >>> print(scope_report(sample.load(state)))
    FAIL charter-state-unknown charter.md:3: The state 'accepted' of the charter is not permitted. Use 'draft'
    or 'reviewed by the owner on <YYYY-MM-DD>'.
    Failing checks: 1.
    Only the field and the thing to build were checked. The findings wait for the research.
    >>> rule = ("charter.md", "| none: rule of the factory |", "| none |")
    >>> print(scope_report(sample.load(sample.CHARTER_DRAFT, rule)))
    No check fails.
    Only the field and the thing to build were checked. The findings wait for the research.
    What remains:
    - The owner did not review the charter.
    >>> print(scope_report(sample.load(charter=False)).splitlines()[-1])
    - The specification has no charter.

    An intent of the owner that has "(no answer)" in each line passes, and remains.

    >>> none = [("spec.md", line, line.split(":")[0] + ": (no answer)") for line in sample.INTENT[:2]]
    >>> print(scope_report(sample.load(*none)))
    No check fails.
    Only the field and the thing to build were checked. The findings wait for the research.
    What remains:
    - The intent of the owner was not asked.
    """
    found = scope_findings(data)
    lines = [
        f"FAIL {f['rule']} {f['file']}:{f['line']} {f['id']}: {f['text']}".replace(" : ", ": ") for f in found
    ]
    lines.append(MESSAGES["failures"].format(len(found)) if found else MESSAGES["no-failure"])
    lines.append(MESSAGES["scope-only"])
    rest = ([] if intent_asked(data) else [MESSAGES["remains-intent"]]) + charter_remains(data)
    if rest:
        lines += [MESSAGES["remains-head"], *("- " + r for r in rest)]
    return "\n".join(lines)


def scope_findings(data):
    """The findings of phase 1, sorted: the scope, and the form of a charter that exists.

    >>> import sample
    >>> scope_findings(sample.load())
    []
    >>> date = ("spec.md", "2026-01-05; a recipe for", "in January; a recipe for")
    >>> state = ("charter.md", sample.CHARTER_STATE, "**State**: accepted")
    >>> brief(scope_findings(sample.load(date, state)))
    [('charter-state-unknown', ''), ('agreed-without-date', '')]
    """
    found = check_scope(data) + check_charter(data)
    return sorted(found, key=lambda f: (f["file"], f["line"], f["rule"], f["id"], f["text"]))


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
    (['accepted', 'answers', 'charter', 'findings', 'intent_asked', 'previous', 'reading', 'remains',
      'requirements', 'trials', 'views'], [('unknown-source', 'C-02')], True)
    >>> result["charter"]["present"], result["charter"]["state"], result["charter"]["lines"][:2]
    (True, 'reviewed', [{'items placed': 1, 'line': 'T-1', 'requirements': 1},
                        {'items placed': 1, 'line': 'T-2', 'requirements': 1}])
    >>> result["remains"]["charter-unserved"], result["remains"]["serves-none"]
    ([], ['operation: 4', 'storage: 2'])
    >>> result["reading"]["table"], result["reading"]["sources"][1], result["remains"]["unread"]
    (True, {'document': 'S-02', 'not read': 0, 'pages': 2, 'source': 'S-02'}, [])
    >>> result["answers"], result["intent_asked"], result["remains"]["stakeholders"]
    ({'judgement': 22, 'other': 0, 'source': 8}, True, [])
    >>> result["trials"], result["remains"]["trial"]
    (['T-01'], [])
    >>> result["views"][1]
    {'items': 2, 'level 1': 1, 'level 2': 0, 'level 3': 1, 'not admitted': 0, 'pending': 0, 'sources': 2,
     'sources read for the view': 2, 'stakeholders': 1, 'view': 'storage'}
    >>> result["requirements"][1]
    {'a proposed boundary would take': 0, 'duplicates': 0, 'requirements': 2, 'to a boundary': 0,
     'to a decision': 0, 'to an implementation skill': 0, 'to an item': 2, 'view': 'storage'}
    >>> result["remains"]["proposed-boundaries"], result["remains"]["left-stakeholders"]
    ([], [])

    --previous compares with an earlier revision, and --words finds product words.

    >>> earlier = good.parent / "earlier.md"
    >>> _ = earlier.write_text(sample.SPEC.replace("was done and recorded.", "was done."), encoding="utf-8")
    >>> words = good.parent / "words.txt"
    >>> _ = words.write_text("program\n", encoding="utf-8")
    >>> code, out, _ = sample.run(main, good, "--previous", earlier, "--words", words, "--json")
    >>> result = json.loads(out)
    >>> code, brief(result["findings"]), result["remains"]["changed"], result["previous"]
    (1, [('product-word', 'C-05')], ['C-02'], True)

    --scope checks only what is settled before the research, for phase 1.

    >>> code, out, _ = sample.run(main, bad, "--scope")
    >>> code, out.splitlines()[0]
    (0, 'No check fails.')
    >>> no_field = sample.folder(("spec.md", " | **Accepted**: A. Person, 2026-01-15", ""))
    >>> sample.run(main, no_field, "--scope")[0]
    1

    --scope examines the form of a charter that exists. A specification without a charter passes.

    >>> effect = sample.folder(("charter.md", "| no exit: 3.3 |", "| the first claim on level 1 |"))
    >>> code, out, _ = sample.run(main, effect, "--scope")
    >>> code, out.splitlines()[0][:45]
    (1, 'FAIL charter-effect-unknown charter.md:20 P-1')
    >>> none = sample.folder(charter=False)
    >>> sample.run(main, none, "--scope")[0], sample.run(main, none)[0]
    (0, 0)

    In phase 1 the fields of the research are as the template has them. --scope does not examine
    them. The template holds a placeholder in each such line, and no name of a real concern: the
    check does not depend on a word of the template.

    >>> import pathlib
    >>> template = pathlib.Path(__file__).resolve().parents[3] / ".specify/templates/overrides"
    >>> text = aspect.read_text(template / "aspect-spec-template.md")
    >>> "- **Views**:" in text and "| Id | Item | Why | View | Level |" in text
    True
    >>> template_data = aspect.Doc(template / "aspect-spec-template.md")
    >>> fields = template_data.fields(template_data.section("1"))
    >>> research = ("stakeholders", "views", "contexts", "risk dimensions", "boundaries", "targets")
    >>> sorted({item["name"] for name in research for item in fields[name]["items"]})
    ['[name]']
    >>> text = text.replace("[one major aspect, in one line]", "backups")
    >>> text = text.replace("[the field it", "operations [it")
    >>> text = text.replace("[DATE; the field", "2026-01-05 [the field")
    >>> phase_1 = sample.folder()
    >>> _ = (phase_1 / "spec.md").write_text(text, encoding="utf-8")

    The intent of the owner is settled in phase 1 also. A line that is as the template has it fails.

    >>> code, out, _ = sample.run(main, phase_1, "--scope")
    >>> code, [line.split(":")[0] for line in out.splitlines()[:3]]
    (1, ['FAIL intent-without-date spec.md', 'FAIL intent-without-date spec.md',
         'FAIL intent-without-date spec.md'])
    >>> for name in ("meaning", "result", "not wanted"):
    ...     start = text.index(f"  - `{name}`: [")
    ...     text = text[:start] + f"  - `{name}`: (no answer)" + text[text.index("\n", start) :]
    >>> _ = (phase_1 / "spec.md").write_text(text, encoding="utf-8")
    >>> code, out, _ = sample.run(main, phase_1, "--scope")
    >>> code, out.splitlines()[0], out.splitlines()[-1]
    (0, 'No check fails.', '- The intent of the owner was not asked.')
    >>> sample.run(main, phase_1)[0]
    1

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
    if "--scope" in args:
        print(scope_report(data))
        sys.exit(1 if scope_findings(data) else 0)
    found, remains = run_checks(data, previous_rows, words)
    if as_json:
        result = {
            "accepted": is_accepted(data),
            "answers": answer_counts(data),
            "charter": {
                "present": data["charter"] is not None,
                "state": (data["charter"] or {}).get("state"),
                "lines": charter_counts(data),
            },
            "findings": found,
            "intent_asked": intent_asked(data),
            "previous": previous is not None,
            "reading": {"table": data["has_reading"], "sources": reading_of(data)},
            "remains": remains,
            "requirements": requirement_counts(data),
            "trials": sorted(t.get("id", "") for t in data["trials"]),
            "views": view_counts(data),
        }
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(report(data, found, remains, previous is not None))
    sys.exit(1 if found else 0)


if __name__ == "__main__":
    main()
