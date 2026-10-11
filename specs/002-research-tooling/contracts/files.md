# Contract: the files

## Head of an aspect specification

The template gets one more field in its head line:

```markdown
**Branch**: `003-name` | **Research date**: 2026-10-09 | **Supersedes**: none | **Accepted**: pending
```

`Accepted` is `pending`, or the person and the date: `<person>, 2026-10-20`.

## Section 5 of an aspect specification

The block of the recipe skill gets one optional field:

```markdown
- **Target folder**: `factory/sota-research/`
```

Without it the target is `skills/<name>/`.

## vetting.md

```markdown
# Vetting record: <aspect>

Rubric for sources: version <n>. Rubric for items: version <n>.

## Sources

| Source | Kind | Gates | Signals | Answers | Score | Date | Confirmed by |
|---|---|---|---|---|---|---|---|
| S-14 | page | pass | reachable yes; date 2025-05-01; age 526 d; author yes; links out 41 | record: yes (URL); fast-lane references: 2 (S-13, S-15) | 7 of 10 | 2026-10-09 | pending |

## Items

| Item | Severity | Probability | Breadth | Adopt | Keep | Own risk | Dimension | Return | Cost | Score | Admitted | Level |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C-07 | 3 (S-14 abstract) | 3 (S-14 finding 1) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | | 27 | 4 | 67 | yes | 1 |

## Requirements

| Id | Requirement | Stakeholder | View | Source | Goes to |
|---|---|---|---|---|---|
| R-01 | <one sentence> | <stakeholder> | <view> | S-14 finding 1 | C-07 |

## Proposed boundaries

| Boundary | Requirements that it would take | Stakeholders that it would leave with no requirement | Reason |
|---|---|---|---|
| <name> | R-02, R-05 to R-07 | <stakeholders, or none> | <reason and source> |

## Reading

The program `index.py unread --write` writes this table. Do not change it by hand.

| Source | Document | Pages | Given to readers | Not read |
|---|---|---|---|---|
| S-01 | <document id> | 40 | 1-25, 26-40 | none |
```

- The session writes the table "Requirements": one row for each requirement that a source
  states for a stakeholder. The cell "Goes to" is `C-<nn>`, `3.3: <decision>`, `5`,
  `boundary: <name>` or `duplicate: R-<nn>`. No program writes this table. A requirement
  goes only to a boundary that the owner decided.
- The session writes the table "Proposed boundaries": one row for each boundary of section 1
  with the state `proposed`. The cell of the requirements holds identifiers of the table
  "Requirements", a range in the form `R-<nn> to R-<nn>`, or `none`. No program writes this
  table. The session removes the row when the owner decides or declines the boundary.
- Each line of the field `Boundaries` of section 1 of `spec.md` holds the state of the
  boundary, before the source: `(proposed)` or `(decided by the owner on <YYYY-MM-DD>)`. A
  line without a state is `proposed`.
- `index.py unread --write SPEC` writes the part "Reading" and replaces it in a later run. No
  person and no session writes it. It has one row for each converted document of the work
  folder that is a source of section 2. `Pages` is the number of pages. `Given to readers`
  holds each recorded range, and `Not read` the pages in no recorded range; each is `none`
  when it is empty. A source with `all` in the cell `Views` and without a converted document
  has `none` in the cell `Document` and `0` in the cell `Pages`.
- The table of section 2 of `spec.md` gets the cell `Views` after the cell `Read`: the views
  that the source was read for, with a comma between two names, or `all`.

- A person or the session writes the cells Answers, Severity to Own risk, Dimension, and
  Confirmed by. The cell Dimension names the risk dimension of an item whose return depends on
  the risk of a project; `place.py` puts it into the Level cell of an item above level 1.
  The programs write the other cells.
- An answer names its source in parentheses. An answer of the session without a source is
  written `2 (judgement)`.
- `Confirmed by` is `pending`, `rejected`, or the person and the date.

## Section 1 of an aspect specification

Section 1 gets one more field of the research, the measured targets:

```markdown
- **Targets**: the measurable results that a project reaches when it applies the recipe.
  - `<name>`: <the scale and its levels; the program or the method that measures it> (S-02 section 4)
```

A specification without a target has `- **Targets**: (none found)`.

Section 1 gets one more field that is settled before the research, the intent of the owner:

```markdown
- **Intent of the owner**: the answers of the owner to the questions of phase 1.
  - `meaning`: "<the words of the owner>" (2026-10-10)
  - `result`: "<the words of the owner>" (2026-10-10)
  - `not wanted`: (no answer)
```

Section 1 gets one more field of the research, the stakeholders. The line of a view names its
stakeholders before the source:

```markdown
- **Stakeholders**: each group of persons that has an interest in the result or carries a duty for it.
  - `<name>`: <the concerns of this stakeholder for this aspect> (S-01 section 1)
- **Views**: the points of view that the aspect brings together.
  - `<name>`: <what this view is concerned with> (stakeholders: <name>, <name>) (S-01 section 1)
```

## trial.md

```markdown
# Trial record: <aspect>

## Trials

| Id | Date | Project | Commit of the specification | Plan |
|---|---|---|---|---|
| T-01 | 2026-10-10 | <project> | abc1234 | not kept |

## Findings

| Id | Trial | Viewpoint | Finding | Route | Status |
|---|---|---|---|---|---|
| F-01 | T-01 | operations | <one sentence> | recipe | open |
```

- The file is optional. The session writes a trial and its findings. The owner decides the
  status of each finding.
- `Plan` holds where the plan is, or `not kept`.
- `Viewpoint` is `architecture`, `operations`, `quality`, `development`, `security`,
  `product owner` or `views of the recipe`. The file `references/viewpoints.txt` of the
  tooling holds these names, one in each line. A kit of `export.py` does not hold the file.
- `Route` is `recipe`, `tooling` or `implementation skill`.
- `Status` is `open`, `corrected in <revision or commit>` or `declined: <reason>`.

## references/seeds.md

```markdown
## The seeds

| Id | Document | Issuer | Version or date | Kind | Address | sha256 | Terms | Row read on |
|---|---|---|---|---|---|---|---|---|
| <id> | <document> | <issuer> | <version, date> | pdf | https://… | <64 characters, or empty> | <terms> | <date> |

## Bodies of knowledge

| Field | Seed |
|---|---|
| <field> | <id> |
```

- `Id` uses lowercase letters, digits and hyphens.
- `Kind` is `pdf`, `page` or `owner file`.
- `sha256` is the digest of the file when the row was written, or empty.

## charter.md

Optional file of the owner, beside `spec.md`. The template is
`.specify/templates/overrides/charter-template.md`. The kit holds the template. No program
reads the file.

## seeds.json of a work folder

```json
{
  "date": "2026-10-10",
  "seeds": [
    {
      "converted": "converted/<id>.md",
      "file": "seeds/<id>.pdf",
      "id": "<id>",
      "kind": "owner file",
      "pages": 411,
      "sha256": "<64 characters>",
      "state": "retrieved"
    }
  ]
}
```

- The paths are relative to the work folder. `date` is `null` without `--today`.
- `converted`, `file`, `pages` and `sha256` are `null` for a seed without a file.
- `state` is `retrieved`, `recorded`, `owner must give the file`, `changed` or
  `failed: <reason>`.

## references/synonyms.txt

```text
# A comment.
first term = second term = third term
```

- One group in each line. The terms are separated by ` = `.
- A line that starts with `#` is a comment. An empty line is ignored.
- `index.py build` reads the file. A file of `--synonyms FILE` has the same form.
- The file `synonyms.txt` of a work folder has the same form. `index.py build` reads it when
  it is there.

## Table of answers for `index.py recall`

```markdown
| Query | Document | Pages |
|---|---|---|
| end user | swebok | 48, 55-57 |
```

- `Query`: the words and the phrases of one search.
- `Document`: the id of a document of the index.
- `Pages`: single pages and ranges, separated by commas.

## Marker of a kit

The file `.factory-kit` in a kit that `init.py` made:

```text
This folder is a kit of the factory. The program init.py made it.
Commit of the repository: <commit, or not known>
```

## Stamp of a rendered file

The first lines after the front matter of `SKILL.md`, and the first lines of each other
rendered file:

```markdown
<!-- Rendered from the specification branch `003-name`, commit `abc1234`, spec.md sha256 `…`.
     Do not edit this file. Change the specification and render it again. -->
```

The stamp of a trial rendering has one more line at its start. For a specification that the
owner accepted, the line is `Trial rendering of a specification. Not a delivered skill.`

```markdown
<!-- Trial rendering of a specification that the owner did not accept. Not a delivered skill.
     Rendered from the specification branch `003-name`, commit `abc1234`, spec.md sha256 `…`.
     Do not edit this file. Change the specification and render it again. -->
```

## Rendered recipe skill

```text
<target>/
├── SKILL.md                 # front matter (name, description), stamp, goals, order of the work,
│                            # decisions by context, how to lead the risk analysis, how to show
│                            # and change the selection, what to delegate, the measured targets,
│                            # the plan before a change, when to stop
├── references/checklist.md  # the checklist: id, item, risk, level, check; no source text
└── agent-templates/<name>.md
docs/<name>.md               # the documentation for the user, in Simplified Technical English
```

`SKILL.md` names no product and stays below 500 lines. No rendered file refers to the factory,
to this repository or to an absolute path.

## Selection of a project

Path in the project of the user: `.agents/kit/<aspect>.md`.

```markdown
# Selection: <aspect>

Recipe: `<name>`, specification branch `003-name`, commit `abc1234`. Last review: 2026-11-02.

## Risk analysis

| Dimension | Question | Answer | Target level |
|---|---|---|---|
| regulatory | Is personal data involved? | Yes, customer addresses. | 3 |
| operative | Can an operation be undone? | Yes, each deployment. | 1 |

## Checklist

- [x] C-01 <item>
- [ ] C-07 <item> (declined: <reason>)
- [ ] C-12 <item> (above the target level)
```

- `[x]` is adopted. `[ ]` with `declined:` keeps its reason. `[ ]` with `above the target
  level` is not selected and needs no reason.
- The recipe skill writes this file and shows it on request. The user can edit it by hand.
