# Experiment: stage test of the viewpoint integrity in the review of a plan

## 1. Question

- **Quote**: "the sota skills and factory have to be sharp on integrity in the process and the created skills. integrity creates trust."
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome.
  - `confirmed`: the viewpoint stays in the task of the reviewer. The next step is the same walk on the process of the factory itself.
  - `refuted`: the questions are too open for a reviewer. The viewpoint gets a fixed list of assets for each question, and that form gets its own test.
  - `not decided`: two more runs.

## 2. Hypothesis

- **Statement**: A reviewer that gets the viewpoint integrity finds, in the plan of the trial I-14, four or more of the five gaps that the agent of the factory found when the owner asked for this view.
- **Forbidden result**: two or more of three reviews find three or fewer of the five.
- **Criterion**: C-1
- **Confirmed when**: `review >= 2`
- **Refuted when**: `review <= 1`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does the list of findings hold a finding for four or more of these five: the packages that the users install are built outside the chain of evidence of the plan; a change can weaken or remove a test and pass; the results of the tests or of the checks are not kept as evidence that is tied to a commit or an artifact; the risk analysis does not ask what the software can do to the system on which it runs; the plan has nothing for the integrity of the data that the software reads or writes? | judge | | final |
| C-2 | Does the report have a finding that the packages that the users install are built outside the chain of evidence of the plan? | judge | | final |
| C-3 | Does the report have a finding that a change can weaken or remove a test and pass? | judge | | final |
| C-4 | Does the report have a finding that the results of the tests or of the checks are not kept as evidence that is tied to a commit or an artifact? | judge | | final |
| C-5 | Does the report have a finding that the risk analysis does not ask what the software can do to the system on which it runs? | judge | | final |
| C-6 | Does the report have a finding about the integrity of the data that the software reads or writes? | judge | | final |
| C-7 | Does the report have a finding about integrity that is none of the five of C-1? | judge | | final |
| C-8 | Does each finding give a file and a line? | judge | | final |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| review | the only arm: the task of the reviewer with the viewpoint integrity, on the trial project of the trial I-14 with its plan and its selection | prompts/review.md | inputs/project |

- **One arm**: the comparison is the review of the same plan with the task before this change (`trials/I-14/plan/plan-review.md`): of the five gaps, its findings hold a part of the first one and none of the other four.

## 5. Subject

- **Product**: claude
- **Model**: sonnet
- **Tools**: Read, Glob, Grep
- **Runs for each arm**: 3
- **Time limit**: 1500
- **Git repository**: no
- **Fewer than five runs**: a stage test is small on purpose.

## 6. Words of the expected answer

- (none): the input is a project and its plan; they hold the names of practices. The questions of the viewpoint were written after the agent of the factory had found the five gaps in this same plan. Thus this test shows only that a reviewer can do the walk. It does not show that the walk finds gaps in a plan that nobody examined before.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| review | C-1 | 3 |
| review | C-2 | 3 |
| review | C-3 | 3 |
| review | C-4 | 3 |
| review | C-5 | 3 |
| review | C-6 | 2 |
| review | C-7 | 3 |
| review | C-8 | 2 |

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: devsecops
- **Agents**: (none)
