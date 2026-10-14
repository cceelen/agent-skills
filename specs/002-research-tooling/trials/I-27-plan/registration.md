# Experiment: the plan of the rendered skill of the iteration I-27 on a project

## 1. Question

- **Quote**: "we do both after each other"
- **Date**: 2026-10-14
- **Decision**: what is done after each outcome.
  - `confirmed`: the owner and the agent walk through the plan. The findings of that walk go to the routes recipe, tooling or implementation skill.
  - `refuted`: the owner and the agent walk through the plan also. The first question of the walk is at which step the basic practices were lost: the specification, the rendering or the plan.
  - `not decided`: the run is done again after the cause that made it not valid is corrected.

## 2. Hypothesis

- **Statement**: The skill that is rendered from a specification with the table "Binding sources" makes a selection that marks one or more items as necessary or as prepared, with the regulation or the governance that asks for it.
- **Forbidden result**: no line of an item in the selection has the mark `necessary:` or `prepared:`.
- **Criterion**: P-10
- **Confirmed when**: `plan >= 1`
- **Refuted when**: `plan <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| P-1 | Does the plan have a part for four or more of these five: the tests run for each change; a build or a test that fails stops the change; a measure of the coverage of the tests; static analysis of the code; a scan of the dependencies for known vulnerabilities? | judge | | file:.agents/kit/devsecops-plan.md |
| P-2 | Does the plan name, for one or more of its parts, a maintained component of a different project that it uses in place of an own construction? | judge | | file:.agents/kit/devsecops-plan.md |
| P-3 | Does the plan separate the step that builds from the step that publishes, with separate rights? | judge | | file:.agents/kit/devsecops-plan.md |
| P-4 | Does the plan say which level of each measured target it reaches? | judge | | file:.agents/kit/devsecops-plan.md |
| P-5 | Does the plan say what stops the next level of a measured target? | judge | | file:.agents/kit/devsecops-plan.md |
| P-6 | Does the plan list the decisions that it leaves to the owner, each marked as a proposal? | judge | | file:.agents/kit/devsecops-plan.md |
| P-8 | Does the file record which regulation and which governance bind the project, or which of them the owner prepares for, or that the place of use of the product is not known? | judge | | file:.agents/kit/devsecops.md |
| P-9 | Does the file give the class of a source, for example regulation, governance, standard or foundation, as a reason for the order of the items or for an item that is declined? | judge | | file:.agents/kit/devsecops.md |
| P-10 | Does a line of an item in the selection have the mark `necessary:` or `prepared:`? | program | `(?m)^- \[[ x]\] C-\d+ .*\((?:necessary\|prepared): ` | file:.agents/kit/devsecops.md |
| P-11 | Does the selection compare whom each regulation and each governance binds with the kind of this project? | judge | | file:.agents/kit/devsecops.md |
| P-7 | Is there a plan? | program | `\S` | file:.agents/kit/devsecops-plan.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| plan | the only arm: a copy of one project of the owner without its history and without the files of its pipeline, with the rendered skill installed | prompts/plan.md | inputs/project |

- **One arm**: the plan is the object of a walk of the owner and the agent. The criteria prepare that walk. The plan of the trial I-25 came from the same project and the same prompt, and from the specification of that trial without the table "Binding sources".
- **The specification**: the specification of the trial I-25 with the table "Binding sources" that the run 1 of the stage test ST-25 wrote. Nothing else of it changed. It is rendered with the tooling of the iteration I-27.
- **The criteria P-10 and P-11** are new: they examine the marks and the comparison of the iteration I-27.

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Write, Edit, Glob, Grep, Skill, WebSearch, WebFetch, Bash
- **Runs for each arm**: 1
- **Time limit**: 3600
- **Git repository**: yes
- **Fewer than five runs**: the owner judges one plan in a walk. One run gives no interval.

## 6. Words of the expected answer

- (none): the input is the rendered skill of the research and the project itself. They hold the names of practices. The prompt names no practice.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| plan | P-1 | 1 |
| plan | P-2 | 1 |
| plan | P-3 | 1 |
| plan | P-4 | 1 |
| plan | P-5 | 0 |
| plan | P-6 | 1 |
| plan | P-7 | 1 |
| plan | P-8 | 1 |
| plan | P-9 | 1 |
| plan | P-10 | 1 |
| plan | P-11 | 1 |

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: devsecops
- **Agents**: (none)
- **Limit of the input**: the files README.md, CONTRIBUTING.md and CHANGELOG.md of the project, and six container files, name tools of the pipeline that was removed. They were not changed.
