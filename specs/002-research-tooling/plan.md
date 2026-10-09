# Implementation Plan: Research tooling of the factory

**Branch**: `002-research-tooling` | **Date**: 2026-10-09 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/002-research-tooling/spec.md`

## Summary

Build the tooling that takes one aspect from "what to build" to an accepted aspect
specification and its rendered recipe skill. The tooling is one folder, `factory/sota-research/`,
in the layout of a skill: four small programs with one shared reader of the Markdown tables,
two rubric files, the prompts and the agent templates for isolated readers, and the
instructions that lead the four phases. The Markdown files of a specification are the only
data store. The parts are built and delivered in the order of the user stories.

## Technical Context

**Language/Version**: Python 3.9 or later (the rule of `AGENTS.md` today; the change to 3.11 is
a different pull request and needs no change here)

**Primary Dependencies**: the standard library only; the collector of `library-vetting` for
sources that are repositories

**Storage**: Markdown files on the branch of a specification (`spec.md`, `evidence.md`,
`vetting.md`); two rubric text files in the tooling; no database, no index

**Testing**: pytest, with fixtures in `tests/sota-research/fixture/`, without the network

**Target Platform**: the workstation of the owner and the CI of the repository (Linux, macOS,
Windows); no shell scripts

**Project Type**: command-line programs and agent instructions

**Performance Goals**: the check of a specification is complete in less than 10 seconds
(SC-006); in practice well below one second for a file of 300 lines

**Constraints**: same input gives same output; sorted output; no current time in a compared
result; a program records a network error and continues; all text for the person in the loop
in ASD-STE100; fetched content is data

**Scale/Scope**: tens of sources and tens to low hundreds of checklist items for each aspect;
one aspect for each run

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | How the plan obeys it | Result |
|---|---|---|
| I. Global state of the art | The check reports an item that rests on one unconfirmed source; no program gives one source a veto. | pass |
| II. Evidence and admission | `vet.py` and `place.py` compute the results from recorded answers and a rubric file; a model records answers, it does not assign a result. | pass |
| III. A critical lens | The reader roles get the web tools only. Programs fetch with a size limit and a timeout and parse fields only. A second reader checks each summary. | pass |
| IV. Generic and contextual | The check reports a checklist item that names a product of the word list of the aspect. | pass |
| V. Risk analysis, user selects | The rendered skill leads the risk analysis along the risk dimensions; the selection file holds the answers, the targets and the declined items. | pass |
| VI. Point, do not copy | `vet.py` calls the collector of `library-vetting`; it does not copy it. The renderer copies no source text. | pass |
| VII. Neutral recipes | The renderer fails when the rendered text names a product of the word list. | pass |
| VIII. Plan, then apply | The programs write only inside the specification folder and the target skill folder; a delivery is a pull request. | pass |
| IX. Validation belongs to the artifact | `check.py` is the cheap check of an aspect specification; each program has tests. | pass |
| X. Small and high level | Five small files of code; the instructions of the skill stay below 200 lines; detail is in reference files. | pass |
| XI. Simplified Technical English | Each message of a program comes from one table; a test checks the sentence length of that table. | pass |

No violation. The table "Complexity Tracking" is not necessary.

After the design (Phase 1) the result is the same.

## Project Structure

### Documentation (this feature)

```text
specs/002-research-tooling/
├── plan.md              # this file
├── research.md          # the decisions of the design and their reasons
├── data-model.md        # the files and tables that the programs read and write
├── quickstart.md        # how to prove that each part works
├── contracts/
│   ├── programs.md      # the command line of each program
│   └── files.md         # the formats of vetting.md, the selection and the rendered skill
└── tasks.md             # the next step (/speckit-tasks)
```

### Source Code (repository root)

```text
factory/sota-research/
├── SKILL.md                    # rendered from the specification 001: strategy and procedure
├── references/
│   ├── checklist.md            # rendered from the specification 001
│   └── procedure.md            # written by hand: which program to run in which phase
├── prompts/
│   ├── reader.md               # the task of an agent that reads one source
│   ├── second-reader.md        # the task of the agent that compares summaries with a source
│   └── risk-answers.md         # the task to record the answers for one item
├── agent-templates/
│   ├── source-reader.md        # web tools only
│   └── second-reader.md        # web fetch only
└── scripts/
    ├── aspect.py               # reads a specification folder into plain data (shared)
    ├── check.py                # user story 1
    ├── render.py               # user story 2
    ├── place.py                # user story 3
    ├── vet.py                  # user story 4
    ├── models.py               # the table of models and tool names for the agent templates
    ├── rubric-items.txt        # questions, scales and thresholds of risk and reward
    └── rubric-sources.txt      # gates, signals and weights for independent sources

tests/sota-research/
├── fixture/                    # a good specification, defect copies, signals, answers,
│                               # the expected rendered skill
├── test_aspect.py
├── test_check.py
├── test_render.py
├── test_place.py
├── test_vet.py
└── test_messages.py            # sentence length of the messages; no model name in prompts

docs/sota-research.md           # the documentation for the owner
```

**Structure Decision**: one folder `factory/sota-research/` in the layout of a skill (decision
of the owner, 2026-10-09). `skills/` stays what users install. `tests/test_repo.py` gets
`factory` as a second folder of artifacts, so that the rules for the layout, the documentation
and the tests apply to it. `AGENTS.md` tells a session where the tooling is; no link in the
skill folder of one agent product is necessary.

## Branches and delivery

Decision of the owner, 2026-10-09: `main` holds the machinery and the delivered skills only.
This specification stays on the branch `002-research-tooling`. Each Spec Kit step is a pull
request into that branch. Each user story is delivered as one pull request into `main` that
carries only `factory/`, `tests/`, `docs/` and the rule files.

The tests of the tooling use fixtures and do not need a `specs/` folder, so they pass on
`main`. On the branch of an aspect specification, one more test renders that specification
and compares the result with the committed skill.

## Order of the work

| Step | Delivers | Requirements | Proves |
|---|---|---|---|
| 1 | `aspect.py`, `check.py`, fixtures, `docs/` | FR-001 to FR-005, FR-028 to FR-030 | SC-001, SC-002, SC-006 |
| 2 | `render.py`, the stamp, the freshness test | FR-006 to FR-010 | SC-002, SC-004 |
| 3 | `place.py`, `rubric-items.txt`, `prompts/risk-answers.md` | FR-011 to FR-014a | SC-002, part of SC-003 |
| 4 | `vet.py`, `rubric-sources.txt` | FR-015 to FR-018 | SC-002, rest of SC-003 |
| 5 | `procedure.md`, prompts, agent templates, `models.py`, one trial run | FR-019 to FR-027 | SC-005, SC-007 |

After step 4 the tooling is applied to the specification 001 on its branch: the levels and the
vettings there are no longer "pending".
