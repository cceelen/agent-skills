# Experiment: the factory at iteration I-3, against the baseline of I-2

## 1. Question

- **Quote**: "Do the iteration and do a trial. we are going to make more afterwards."
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome.
  - `confirmed`: the change of I-3 stays. The next iteration answers the next finding of the I-2 trial: a large document is read in ranges, so that no knowledge area is lost.
  - `refuted`: the trace of the failed probes shows the stage where each was lost. The next iteration changes that stage, and nothing else. The change of I-3 stays only if no metric is lower than in the I-2 trial.
  - `not decided`: the run is done again after the cause that made it not valid is corrected.

## 2. Hypothesis

- **Statement**: With the tooling of iteration I-3 (each requirement of a source goes through the calculation; each view reads sources of its own field) and the intent of the owner, the research puts three or more of the four basic practices of the owner on level 1.
- **Forbidden result**: fewer than three of the four basic practices are on level 1.
- **Criterion**: C-1
- **Confirmed when**: `i3 >= 1`
- **Refuted when**: `i3 <= 0`

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

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| i3 | the only arm: the tooling of iteration I-3. The prompts, the criteria and the words are those of the trial I-2 | prompts/p1.md, prompts/p2.md | inputs/kit |

- **One arm**: the comparison is the one registered run of the trial I-2 (2 of 4 basic practices; C-1 no). The input differs from that run in the tooling only.

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
| i3 | C-1 | 1 |
| i3 | C-2 | 1 |
| i3 | C-3 | 1 |
| i3 | C-4 | 0 |
| i3 | C-5 | 1 |
| i3 | C-6 | 0 |
| i3 | C-7 | 1 |
| i3 | C-8 | 1 |
| i3 | C-9 | 1 |
| i3 | C-10 | 1 |
| i3 | C-11 | 1 |
| i3 | C-12 | 1 |

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: sota-file-reader, sota-second-reader, sota-source-reader
- **Change of the kit**: the file `skills/library-vetting/scripts/collect.py` is removed from the input folder, because it holds words of the expected answer. Without it, the vetting of a source that is a repository records an error.
