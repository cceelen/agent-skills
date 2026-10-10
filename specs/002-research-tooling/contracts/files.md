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
```

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
