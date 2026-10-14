# Experiment: the factory at iteration I-4, against the trial of I-3

## 1. Question

- **Quote**: "merge i-4 and run its trial"
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome.
  - `confirmed`: the change of I-4 stays. The next iteration answers the probe C-6: a boundary that takes the whole concern of a stakeholder is a decision of the owner.
  - `refuted`: the record of the reading shows which pages no reader got and why. The next iteration changes that step, and nothing else.
  - `not decided`: the run is done again after the cause that made it not valid is corrected.

## 2. Hypothesis

- **Statement**: With the tooling of iteration I-4 (the research reads each converted source in ranges of the index and records what was read), each page of the guide of the body of knowledge reaches a reader.
- **Forbidden result**: the table Reading of the run is absent, or it names pages of the guide that no reader got.
- **Criterion**: C-13
- **Confirmed when**: `i4 >= 1`
- **Refuted when**: `i4 <= 0`

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
| i4 | the only arm: the tooling of iteration I-4. The prompts, the criteria C-1 to C-12 and the words are those of the trials I-2 and I-3; the work folder of the seeds is new and holds only the guide | prompts/p1.md, prompts/p2.md | inputs/kit |

- **One arm**: the comparison is the registered run of the trial I-3 (one reader got the whole guide; C-1 no, C-6 no). The input differs from that run in the tooling and in the work folder of the seeds.

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
| i4 | C-1 | 0 |
| i4 | C-2 | 0 |
| i4 | C-3 | 1 |
| i4 | C-4 | 0 |
| i4 | C-5 | 1 |
| i4 | C-6 | 0 |
| i4 | C-7 | 1 |
| i4 | C-8 | 1 |
| i4 | C-9 | 1 |
| i4 | C-10 | 1 |
| i4 | C-11 | 1 |
| i4 | C-12 | 1 |
| i4 | C-13 | 1 |

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: sota-file-reader, sota-second-reader, sota-source-reader
- **Change of the kit**: the file `skills/library-vetting/scripts/collect.py` is removed from the input folder, because it holds words of the expected answer. Without it, the vetting of a source that is a repository records an error.
