# Data model: research tooling

The Markdown files of a specification are the store. `aspect.py` reads them into the plain
data below. No program writes `spec.md` except `place.py`, which fills the Level cells.

## Aspect specification (`spec.md`)

| Part | Fields | Rules that the check applies |
|---|---|---|
| Head | branch, research date, supersedes, accepted | accepted is a person and a date, or `pending` |
| 1 Aspect | aspect, field, contexts, risk dimensions, boundaries, agreed on | each field is filled; agreed on has a date; each risk dimension has a name and a question |
| 2 Sources | id, source, issuer, version or date, class, license, read, url | each cell is filled; class is one of six values; read is `full`, `part` or `no`; ids are unique |
| 3.3 Decisions by context | decision, depends on, options, sources | each source id is known |
| 3.4 Disagreement | question, positions, handling, sources | the section is present; `none found` is permitted |
| 4 Checklist | id, item, why, level, admitted by, check, source | see below |
| 5 Skill set | name, target folder, goal, reads first, applies, delegates, stops when; rows of implementation skills | name obeys the rule for a skill name |
| 6 Watch list | signal, where, cadence | one row or more |
| 7 Decisions | date, decision, reason, revisit when | each row has a date |
| 8 Glossary | term, meaning here, other meanings | each cell is filled |

### Checklist item

| Field | Values | Rule |
|---|---|---|
| id | `C-` and a number | unique; with `--previous`: the same id has the same item, and a retired id is not in use |
| item | one sentence | names no product of the word list of the aspect |
| why | text | names the risk that the item answers |
| level | `1`, or `2, <dimension>`, or `3, <dimension>`, or `pending` | the dimension is one of section 1 |
| admitted by | `authority (n)`, `practice`, `own rule (<principle>)`, with an optional `, vetting pending` | |
| check | a check, or `judgement` | not empty |
| source | one or more of `S-nn <unit>` or `constitution <principle>` | each id is known; each cited source has an evidence row that names the item |

An item **rests on** a source when it cites it. The check reports an item whose sources are all
read `no`, or all independent and not confirmed.

## Evidence record (`evidence.md`)

One row for each source: source id, what it contributes, where, supports, read (a date). The
check reads the id, the supports cell and the date. It does not judge the summary.

## Vetting record (`vetting.md`)

Written by `vet.py score` and `place.py`, corrected by the owner. Two tables, formats in
`contracts/files.md`.

| Table | Row | Fields |
|---|---|---|
| Sources | one independent source | source id, kind (`repository` or `page`), gate result, signals, answers with their URL, score, rubric version, date, confirmed by |
| Items | one checklist item | item id, the six answers with their source, return, cost, score, admitted, level, rubric version |

State of a source: `not vetted` → `rejected by a gate` or `scored` → `confirmed` or `rejected`
(by the owner). Only `confirmed` lets the source carry an item alone.

State of an item: `pending` (an answer is missing) → `placed` (admitted with a level, or not
admitted).

## Rubrics (in the tooling)

| File | Holds |
|---|---|
| `rubric-items.txt` | version; the six questions with their scales; the admission threshold; the level 1 threshold; the cost limit between level 2 and level 3 |
| `rubric-sources.txt` | version; the gates; the signals and answers with their weights; the score at which a source passes to the owner |

A change of a question, a scale, a weight or a threshold increases the version. The identifier
of a question does not change.

## Rendered recipe skill

Owned by the renderer: `SKILL.md`, `references/checklist.md`, `agent-templates/<name>.md`,
`docs/<name>.md`. Each starts with the stamp: specification branch, commit, digest of `spec.md`.

## Selection (in a project of a user)

One file for each aspect. It holds the stamp of the recipe that was used, the risk analysis
(dimension, question, answer, target level), and each checklist item with its state: adopted,
or declined with a reason. The distance of the project is the list of adopted items whose
check fails.
