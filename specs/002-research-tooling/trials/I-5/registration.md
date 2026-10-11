# Experiment: the factory at iteration I-5, against the trial of I-4

## 1. Question

- **Quote**: "go ahead and do it."
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome.
  - `confirmed`: the change of I-5 stays. The next iteration answers how the calculation places a requirement, with the structure of the levels (why, what, how, with what).
  - `refuted`: the register shows the exit that took the requirements of the concern. The next iteration changes that exit, and nothing else.
  - `not decided`: the run is done again after the cause that made it not valid is corrected.

## 2. Hypothesis

- **Statement**: With the tooling of iteration I-5 (a boundary takes a requirement only after the owner decided it), the concerns of the architecture stay in the aspect: section 1 has a stakeholder or a view for them.
- **Forbidden result**: section 1 has no stakeholder and no view for the concerns of the architecture.
- **Criterion**: C-6
- **Confirmed when**: `i5 >= 1`
- **Refuted when**: `i5 <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does the checklist of the specification have, on level 1, items for three or more of these four: a measure of the coverage of the tests; static analysis of the code; tests of robustness, for example fuzzing, for parts that read input that is not trusted; an automated release? | judge | | file:specs/001-devsecops/spec.md |
| C-2 | Does the checklist have an item on level 1 that asks for a measure of the coverage of the tests? | judge | | file:specs/001-devsecops/spec.md |
| C-3 | Does the checklist have an item on level 1 that asks for static analysis of the code? | judge | | file:specs/001-devsecops/spec.md |
| C-4 | Does the checklist have an item on level 1 that asks for tests of robustness, for example fuzzing, for parts that read input that is not trusted? | judge | | file:specs/001-devsecops/spec.md |
| C-5 | Does the checklist have an item on level 1 that asks for an automated release? | judge | | file:specs/001-devsecops/spec.md |
| C-6 | Does section 1 name a stakeholder or a view for the concerns of the architecture of the software or of its pipeline? | judge | | file:specs/001-devsecops/spec.md |
| C-7 | Does section 1 name a stakeholder or a view for the concerns of the operation of the software? | judge | | file:specs/001-devsecops/spec.md |
| C-8 | Does section 1 name a stakeholder or a view for the concerns of the quality of the software? | judge | | file:specs/001-devsecops/spec.md |
| C-9 | Does section 1 name a stakeholder or a view for the concerns of the persons who develop the software? | judge | | file:specs/001-devsecops/spec.md |
| C-10 | Does section 1 name a stakeholder or a view for the concerns of the person who owns the product or pays for it? | judge | | file:specs/001-devsecops/spec.md |
| C-11 | Does the checklist have one or more items on level 3? | judge | | file:specs/001-devsecops/spec.md |
| C-12 | Does the field Targets of section 1 name a target with a scale of levels for the integrity of the supply chain? | judge | | file:specs/001-devsecops/spec.md |
| C-13 | Does the table Reading of the run have a row for the guide of 411 pages with no page that was not read? | program | `swebok \W 411 \W[^\n]*\W none \W` | file:specs/001-devsecops/vetting.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| i5 | the only arm: the tooling of iteration I-5. The prompts, the criteria and the words are those of the trial I-4; the work folder of the seeds is new and holds only the guide | prompts/p1.md, prompts/p2.md | inputs/kit |

- **One arm**: the comparison is the registered run of the trial I-4 (49 requirements of the architecture went to a boundary; C-6 no). The input differs from that run in the tooling only.

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Write, Edit, Glob, Grep, Agent, WebSearch, WebFetch, Bash
- **Runs for each arm**: 1
- **Time limit**: 5400
- **Git repository**: yes
- **Fewer than five runs**: one run starts about fifty reader agents and takes about one hour of the large model; the owner asked for one trial now and more afterwards. One run gives no interval.

## 6. Words of the expected answer

- `coverage`
- `static analysis`
- `fuzz`
- `release automation`
- `automated release`
- `product owner`
- `architect`

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| i5 | C-1 | 0 |
| i5 | C-2 | 0 |
| i5 | C-3 | 1 |
| i5 | C-4 | 0 |
| i5 | C-5 | 1 |
| i5 | C-6 | 0 |
| i5 | C-7 | 1 |
| i5 | C-8 | 1 |
| i5 | C-9 | 1 |
| i5 | C-10 | 1 |
| i5 | C-11 | 0 |
| i5 | C-12 | 1 |
| i5 | C-13 | 1 |

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: sota-file-reader, sota-second-reader, sota-source-reader
- **Change of the kit**: the file `skills/library-vetting/scripts/collect.py` is removed from the input folder, because it holds words of the expected answer. Without it, the vetting of a source that is a repository records an error.
