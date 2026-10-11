# Experiment: stage test of the grouping of the patterns of several reports

## 1. Question

- **Quote**: "so the goal of the factory is to be able to scan for interesting patterns, tooling, integrations and similar in samples"
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome. The decision uses the measure of the program `agreement.py`, which is sealed with this registration: for each two runs, the share of the pairs of lines that are together in the two runs, of the pairs that are together in one run at least.
  - `confirmed`: if each share is at or above 0.60, a session can put the patterns of several reports together, and the procedure gets this step. If one share is below 0.60, the groups are not stable: the step is not built in this form, and the next test gives the session a fixed list of concerns to sort the patterns into.
  - `refuted`: a session does not place each line one time. The step is not built in this form.
  - `not decided`: two more runs.

## 2. Hypothesis

- **Statement**: A session that gets the pattern lines of five reports of one sample puts each line into one group.
- **Forbidden result**: the file of the groups is missing or has fewer than ten groups in two or more of three runs.
- **Criterion**: C-1
- **Confirmed when**: `group >= 2`
- **Refuted when**: `group <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does the file hold ten or more groups? | program | `(?s)(?:\x7c\s*G-\d+\s*\x7c.*){10}` | file:groups.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| group | the only arm: 121 pattern lines of the five runs of the stage test ST-7 | prompts/group.md | inputs/case |

- **One arm**: the test measures one new stage. No earlier form of the stage exists.

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Write
- **Runs for each arm**: 3
- **Time limit**: 1800
- **Git repository**: no
- **Fewer than five runs**: a stage test is small on purpose. A full trial follows only when a stage test shows a difference.

## 6. Words of the expected answer

- (none): the test has no expected groups. It measures if three runs give the same groups.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| group | C-1 | 3 |

The agent predicts: each run writes between 25 and 45 groups, and the share of the measure is between 0.40 and 0.60 for each two runs.

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
