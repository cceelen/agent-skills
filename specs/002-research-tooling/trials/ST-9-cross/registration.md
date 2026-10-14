# Experiment: stage test of the grouping of the patterns of different projects

## 1. Question

- **Quote**: "so the goal of the factory is to be able to scan for interesting patterns, tooling, integrations and similar in samples"
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome. The decision uses the measure of the program `agreement.py` of the stage test ST-8: for each two runs, the share of the pairs of lines that are together in the two runs, of the pairs that are together in one run at least.
  - `confirmed`: if each share is at or above 0.60, the step of the procedure stays as it is. If one share is below 0.60, the groups of different projects are not stable: the rule in the procedure gets the limit "of one project", and the next test gives the session a fixed list of concerns.
  - `refuted`: no run finds a pattern in two projects. The step of the procedure gets the limit "of one project".
  - `not decided`: two more runs.

## 2. Hypothesis

- **Statement**: A session that gets the pattern lines of four different projects finds a pattern that two or more projects have.
- **Forbidden result**: no group holds lines of two projects, in two or more of three runs. The agent examines this from the files of the runs; the criterion C-1 examines only that the session wrote groups.
- **Criterion**: C-1
- **Confirmed when**: `cross >= 2`
- **Refuted when**: `cross <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does the file hold ten or more groups? | program | `(?s)(?:\x7c\s*G-\d+\s*\x7c.*){10}` | file:groups.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| cross | the only arm: 90 pattern lines from the reports of four projects, one file of each project, read by the smallest model | prompts/group.md | inputs/case |

- **One arm**: the stage test ST-8 gives the value for the lines of one file.

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Write
- **Runs for each arm**: 3
- **Time limit**: 1800
- **Git repository**: no
- **Fewer than five runs**: a stage test is small on purpose. A full trial follows only when a stage test shows a difference.

## 6. Words of the expected answer

- (none): the test has no expected groups.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| cross | C-1 | 3 |

The agent predicts: each run writes between 55 and 75 groups; between 8 and 20 groups of each run hold lines of two or more projects; the share of the measure is between 0.50 and 0.80 for each two runs.

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
