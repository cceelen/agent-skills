# Experiment: the research of the factory at iteration I-14

## 1. Question

- **Quote**: "ok. do a full research trial again."
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome.
  - `confirmed`: the changes of I-8 to I-14 stay. The specification of this run is rendered, and a trial of the plan on a project follows. That trial gives the main judgement.
  - `refuted`: the list of the searches shows why no maintained project became a source. The step "List what exists" is changed, and nothing else. The trial of the plan follows also.
  - `not decided`: the run is done again after the cause that made it not valid is corrected.

## 2. Hypothesis

- **Statement**: With the tooling of iteration I-14, the research takes one or more maintained projects with components that other projects use again as a source of the specification.
- **Forbidden result**: section 2 of the specification names no such project.
- **Criterion**: G-1
- **Confirmed when**: `i14 >= 1`
- **Refuted when**: `i14 <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| G-1 | Does the table of the sources name one or more maintained projects that give components for other projects to use again, for example a collection of templates or of steps for a pipeline? | judge | | file:specs/001-devsecops/spec.md |
| G-2 | Does the table of the sources name one or more tools that examine or measure a project or its pipeline? | judge | | file:specs/001-devsecops/spec.md |
| G-3 | Does the table of the sources name one or more open projects that many other projects depend on, read for what the project itself does? | judge | | file:specs/001-devsecops/spec.md |
| G-4 | Does the table of the sources name a published report or survey that gives numbers on how common a practice is? | judge | | file:specs/001-devsecops/spec.md |
| G-5 | Does the section on the points where the sources disagree have a row in which a principle or a practice of one project disagrees with a standard or a framework? | judge | | file:specs/001-devsecops/spec.md |
| G-6 | Does the final report give the items that are not admitted in a list of their own, with a score? | judge | | final |
| G-7 | Does the final report give the cases in which the order of the principles decided, as questions for the owner, or say that there was no such case? | judge | | final |
| G-8 | Does the table of the requirements have one or more rows that go to a decision of section 3.3? | judge | | file:specs/001-devsecops/vetting.md |
| B-1 | Does the checklist have an item on level 1 that asks that the tests run for each change? | judge | | file:specs/001-devsecops/spec.md |
| B-2 | Does the checklist have an item on level 1 that asks that a build or a test that fails stops the change? | judge | | file:specs/001-devsecops/spec.md |
| B-3 | Does the checklist have an item on level 1 that asks for a measure of the coverage of the tests? | judge | | file:specs/001-devsecops/spec.md |
| B-4 | Does the checklist have an item on level 1 that asks for static analysis of the code? | judge | | file:specs/001-devsecops/spec.md |
| B-5 | Does the checklist have an item on level 1 that asks for a scan of the dependencies for known vulnerabilities? | judge | | file:specs/001-devsecops/spec.md |
| B-6 | Does the checklist have an item, on any level, that asks for tests of robustness, for example fuzzing, for parts that read input that is not trusted? | judge | | file:specs/001-devsecops/spec.md |
| B-7 | Does the checklist have one or more items on level 3? | judge | | file:specs/001-devsecops/spec.md |
| B-8 | Does the table Reading of the run have a row for the guide of 411 pages with no page that was not read? | program | `swebok \W 411 \W[^\n]*\W none \W` | file:specs/001-devsecops/vetting.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| i14 | the only arm: the tooling of iteration I-14, and the result of phase 1 of run 1 of the stage test ST-11 (the scope and a draft of the charter) | prompts/p2.md | inputs/kit |

- **One arm**: the comparison is the registered run of the trial I-5. The input differs from that run in the tooling of the iterations I-7 to I-14 and in the charter. The criteria G-1 to G-7 are new. The criteria B-3, B-4, B-6, B-7 and B-8 are C-2, C-3, C-4, C-11 and C-13 of that trial; B-6 does not ask for level 1.

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Write, Edit, Glob, Grep, Agent, WebSearch, WebFetch, Bash
- **Runs for each arm**: 1
- **Time limit**: 7200
- **Git repository**: yes
- **Fewer than five runs**: one run starts about fifty reader agents and takes about one hour of the large model. One run gives no interval. The stage tests ST-2 to ST-11 measured the single steps with three or more runs each.

## 6. Words of the expected answer

- `coverage`
- `static analysis`
- `fuzz`
- `to-be-continuous`
- `plumber`
- `openssl`

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| i14 | G-1 | 1 |
| i14 | G-2 | 1 |
| i14 | G-3 | 1 |
| i14 | G-4 | 1 |
| i14 | G-5 | 1 |
| i14 | G-6 | 1 |
| i14 | G-7 | 0 |
| i14 | G-8 | 0 |
| i14 | B-1 | 1 |
| i14 | B-2 | 1 |
| i14 | B-3 | 1 |
| i14 | B-4 | 1 |
| i14 | B-5 | 1 |
| i14 | B-6 | 1 |
| i14 | B-7 | 0 |
| i14 | B-8 | 1 |

The agent predicts also, for the programs after the run: 80 percent or more of the requirement lines of the index have a row in the table of the requirements.

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: sota-file-reader, sota-second-reader, sota-source-reader
- **Change of the kit**: the file `skills/library-vetting/scripts/collect.py` is removed from the input folder, because it holds words of the expected answer. Without it, the vetting of a source that is a repository records an error.
