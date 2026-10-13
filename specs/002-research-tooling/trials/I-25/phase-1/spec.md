# Aspect specification: DevSecOps
| 2026-10-11 | Not verified: the intent of the owner was not asked in the session of phase 1. The lines of "Intent of the owner" are the words of the owner from 2026-10-10 and 2026-10-11, and the session put each quote under its question. | The owner was not in the session. | The owner reviews the intent and the draft of the charter. |

**Branch**: `001-devsecops` | **Research date**: pending | **Supersedes**: none | **Accepted**: pending

Layer one of the factory: the exploration of one major aspect of software engineering. This
specification is the source of the recipe for the aspect, a strategy and a generic checklist
that hold the global state of the art (SOTA): the best practices that the industry has produced
so far. A helper renders the recipe skill from it. The implementation skills for single products
are layer two: each set gets its own specification through the Spec Kit product flow. Keep this
file high level. It holds nothing that an agent can learn from the project or from a source.

## 1. Aspect

Settled with the owner before the research. Only the field, the thing to build and the intent
of the owner: no use case, no first user, no stakeholder, nothing narrower.

- **Aspect**: DevSecOps: the shift left of operational, security and quality concerns.
- **Field and disciplines**: software engineering; it cuts across the disciplines of operations, security and quality.
- **Intent of the owner**: the answers of the owner to the questions of phase 1. One line each:
  the words of the owner as a quote, with the date, or `(no answer)`.
  - `meaning`: "DevSecOps is about doing shift left of operational, security, and quality concerns." (2026-10-10)
  - `result`: "we need to check for covering essential and non negotiable basics of each of those 3 points of views." (2026-10-10); "we need to be able to iterate the spec with the sota research and speckit setup so that we can achieve SLSA draft highest levels" (2026-10-10); "the slsa L2 should be a baseline. L3 the goal. beyond L3 aspirational (e.g. hermetic repeatable build, or in the asus zenbook case the usage of a build service)." (2026-10-11)
  - `not wanted`: "running build, test, and packaging in the same step and exposing credentials is a no no. See SLSA build track." (2026-10-11)
- **Agreed with the owner on**: 2026-10-11; the field is software engineering, and the thing to build is the aspect specification and the recipe skill `devsecops` ("do the DevSecOps research and generate a skill", 2026-10-10).

Found by the research, and reviewed by the owner with the other findings. Each line names its
source, or says `(judgement)`. A use case is chosen only when the recipe is applied to a project.

- **Stakeholders**: each group of persons that has an interest in the result or carries a duty
  for it. The research finds them in the body of knowledge of the field and in the sources.
  One line each: a short name, the concerns of the stakeholder for this aspect, and the source.
  - `[name]`: [the concerns of this stakeholder for this aspect] ([S-01 section 1])
  - `[name]`: [the concerns of this stakeholder for this aspect] ([source])
- **Views**: the points of view that the aspect brings together. A view is a set of concerns
  of the aspect. The research aggregates the concerns of the stakeholders into the views. A
  concern that the owner named in the intent is in a view, or section 7 says why it is not.
  One line each: a short name, what the view is concerned with, the stakeholders whose
  concerns the view holds, and the source. Name the stakeholders in this form, before the
  source: `(stakeholders: [name], [name])`. Use the names of the field "Stakeholders".
  - `[name]`: [what this view is concerned with] (stakeholders: [name], [name]) ([S-01 section 1])
  - `[name]`: [what this view is concerned with] (stakeholders: [name]) ([source])
- **Contexts**: the values of each dimension that change the strategy. One line each.
  - `[name]`: [values] ([S-01 section 2])
  - `[name]`: [values] ([source])
- **Risk dimensions**: the dimensions on which the risk of a project differs for this aspect.
  One line each: the name, the question that finds it out, the opinion of the kit on the
  answer, and the source.
  - `[name]`: [question] [Opinion: the opinion of the kit on the answer] ([source])
  - `[name]`: [question] [Opinion: the opinion of the kit on the answer] ([source])
- **Boundaries**: what each neighbouring aspect owns, and what this aspect keeps. One line each:
  a short name, what the neighbouring aspect owns and what this aspect keeps, the state, and
  the source. A boundary has one of two states. Write the state in one of these forms, before
  the source. `(proposed)`: the research proposes the boundary, and it takes no requirement.
  `(decided by the owner on <YYYY-MM-DD>)`: the owner decided the boundary on that date, and
  a requirement can go to it. Only the owner decides a boundary. A line without a state is
  proposed.
  - `[name]`: [what it owns; what this aspect keeps] (proposed) ([source])
  - `[name]`: [what it owns; what this aspect keeps] (decided by the owner on [YYYY-MM-DD]) ([source])
- **Targets**: the measurable results that a project reaches when it applies the recipe. The
  targets come from the sources in the research; the owner can name one in the intent. One
  line each: the name, the scale with its levels, the program or the method that measures it,
  and the source of the scale. If the sources give no target, write `(none found)` in place
  of the lines.
  - `[name]`: [the scale and its levels; the program or the method that measures it] ([source])

## 2. Sources

No single source gates the recipe: the recipe is the fixed side, and each source supports the
items that cite it. **Class** decides the route of admission. The fast lane: `standard`
(standards bodies and public authorities), `regulation` (laws and regulations), `governance`
(frameworks of governance and of audit, rules of an industry), `foundation` (open foundations), `vendor` (a platform vendor
on its own platform), `research` (peer-reviewed research and recognized books), `trusted-data`
(a recorded data source marked as trusted). Every other source is `independent` and passes the
source vetting first. **Read**: full, part or no. A paid source is cited from its official
preview and marked part. **Views**: the views of section 1 that the source was read for, with a
comma between two names, or `all` for a body of knowledge. Each view has two or more sources
of its own field that were read.

| Id | Source | Issuer | Version or date | Class | License | Read | Views | URL |
|---|---|---|---|---|---|---|---|---|
| S-01 | | | | | | | | |

## 3. Strategy

High level, for the agent that runs the work. One page.

### 3.1 Goals

[What "done well" means for this aspect, in three to six lines.]

### 3.2 Order of the work

1. [step: what, and why at this point]

### 3.3 Decisions that depend on context

| Decision | Depends on | Options | Sources |
|---|---|---|---|

### 3.4 Where the sources disagree

| Question | Positions | How this recipe handles it | Sources |
|---|---|---|---|

## 4. Checklist

Generic items, valid across the contexts of section 1. One short sentence each. The way to do an
item that depends on context belongs in 3.3; an item for one product belongs in an
implementation skill. There is no fixed number of items: distil until each item earns its
place.

- **Why**: the risk that the item answers, in one line. A practice of the state of the art
  answers a specific result of a risk analysis.
- **View**: one view name of section 1: the view that the item belongs to. Each view has an
  item on level 1: the practices that are basic and not negotiable in that view.
- **Level**: 1, 2 or 3, cumulative. The program `place.py` writes it from the ladder of the
  source classes. A skill does level 1 in its first iteration, then level 2, then level 3.
  An item above level 1 can name the risk dimension of section 1 that calls for it, in the
  form `2, [risk dimension]`. If the owner declines an item, the cell is `not admitted` and
  the item stays in the list.
- **Strongest source**: the program `place.py` writes the class with the highest value of
  the ladder and its sources, for example `regulation (S-04)`. For an item without a
  requirement, write `own rule` (a rule of this kit, with its principle).
- **Check**: the cheap, deterministic check that shows the item is met, or `judgement`.
- **Source**: the unit of a source by its identifier where it has one. No text of a source is
  copied here; the evidence record says what the source contributes.

| Id | Item | Why | View | Level | Strongest source | Check | Source |
|---|---|---|---|---|---|---|---|
| C-01 | | | | | | | [S-01 unit] |

**Selection.** The kit recommends; the user decides. The recipe skill leads the owner of the
project through a risk analysis of the project, along the risk dimensions of section 1. It
gives the opinion of the kit and proposes a target level for each dimension. The user picks
the targets and declines single items with a reason. The selection is a Markdown checklist
that is committed in the project, and the recipe skill shows and changes it on request. A
declined item keeps its reason, and a refresh shows the declined items whose source changed.
The distance of a project is the list of adopted items whose check fails.

## 5. Skill set to define

What the recipe skill and its agent wrapper do, and which implementation skills layer two must
work out. Each skill of the set holds the rules of the kit, `rules/evidence-before-action.md`,
and reads a source in the turn in which it uses a value from it. The renderer copies the fields
of the recipe skill into the skill as they are. Thus write them for the reader of the skill,
and do not refer to a section of this specification.

### Recipe skill and agent: [name]

- **Target folder**: [the folder of the rendered skill; leave this line out for `skills/<name>/`]
- **Goal**: [the state it brings a case to]
- **Reads first**: [the contexts of section 1 it finds out; the risk analysis and the selection
  of the project]
- **Applies**: [the strategy of section 3; the checklist items it judges]
- **Delegates**: [capabilities, each provided by an implementation skill]
- **Stops when**: [goal reached; blocked; a decision of section 3.3 needs a person]

### Implementation skills (layer two)

One line per product or tool that needs a skill. A skill holds knowledge and pointers, never a
copy of what the product's own catalog maintains: how and what to query in the catalog; how to
identify trustworthy entries; lighthouse projects, chosen by measurable criteria and dated; how the product works and how to get the work
done; settings as a file from the current documentation; common traps and points to review;
which review tools work with it and how to apply their corrections. A skill that cannot reach
its sources says what it could not verify. A skill writes a setting only from the documentation
that it read in the same turn, not from memory.

| Product or tool | Capability | Checklist items it implements | Helper software it needs |
|---|---|---|---|

## 6. Watch list

| Signal | Where to read it | Cadence |
|---|---|---|

## 7. Decisions and changes

Dated. A reversed decision stays and is marked superseded. Name the models that made or
suggested a judgement, and the person who reviewed the findings and accepted the recipe.

| Date | Decision or change | Reason | Revisit when |
|---|---|---|---|

## 8. Glossary

Terms that mean different things in the sources. One preferred form per meaning.

| Term | Meaning here | Other meanings in the sources |
|---|---|---|

## Files beside this specification

- `charter.md`: the charter of the owner, if the owner gave one: the target, the principles
  with their priority, and the constraints. Only the owner changes it. Its template is
  `.specify/templates/overrides/charter-template.md`.
- `evidence.md`: for each source a summary of what it contributes, where in the source that
  is, the rows of this specification that it supports, and the date read. The summary is in
  Simplified Technical English and in the words of this kit. A second reader compares each
  line with the source. A quote stays only where the wording itself is the point.
- `vetting.md`: for each independent source the measured signals, the result of the rubric and
  the owner's confirmation.
  - The table "Requirements" has one row for each requirement that a source states for a
    stakeholder. Its columns are Id, Requirement, Stakeholder, View, Source and Goes to.
  - The cell "Goes to" has one of these forms: `C-<nn>`, `5`, `boundary: <name>` or
    `duplicate: R-<nn>`. A requirement has no other exit.
  - A requirement does not go to a decision of section 3.3.
  - A requirement goes only to a boundary that the owner decided.
  - The table "Proposed boundaries" has one row for each boundary of section 1 with the state
    `(proposed)`. Its columns are Boundary, Requirements that it would take, Stakeholders that
    it would leave with no requirement, and Reason. The cell of the requirements holds
    identifiers of the table "Requirements", or `none`.
  - Each checklist item holds a requirement, or its cell "Strongest source" is `own rule`.
- `trial.md`: the record of the trials of the recipe on a project. This file is optional.
  - The table "Trials" has one row for each trial. Its columns are Id, Date, Project, Commit
    of the specification, and Plan. The cell "Plan" holds where the plan is, or `not kept`.
  - The table "Findings" has one row for each finding of the review of a plan. Its columns
    are Id, Trial, Viewpoint, Finding, Route and Status.
  - The viewpoint is one of the viewpoints of the review. The reviewer gives it.
  - The route is `recipe`, `tooling` or `implementation skill`.
  - The status is `open`, `corrected in <revision or commit>` or `declined: <reason>`.
