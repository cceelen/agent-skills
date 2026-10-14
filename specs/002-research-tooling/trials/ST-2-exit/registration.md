# Experiment: stage test of the exit to a decision, on recorded requirements

## 1. Question

- **Quote**: "continue the trials, tests, and improvement iterations. make sure that you keep what helps and avoid onboarding too much complexity"
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome.
  - `confirmed`: the tooling gets one rule: a requirement does not go to a decision of 3.3. The check examines it.
  - `refuted`: the rule alone does not keep the practice visible: the session puts the requirement into an item that does not name it. The rule is not built. The next test examines the words of an item against the requirements that it holds.
  - `not decided`: two more runs of this test.

## 2. Hypothesis

- **Statement**: A session that must give each requirement of a decision of 3.3 to a checklist item writes a new item that names the measure of test coverage for the requirement R-1026.
- **Forbidden result**: the row R-1026 goes to an item of the recorded checklist, to `5` or to a duplicate, in each of three runs.
- **Criterion**: C-1
- **Confirmed when**: `exit >= 2`
- **Refuted when**: `exit <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does the row R-1026 (a measure of coverage) go to a new item that names coverage? | program | `R-1026 \x7c(?:[^\x7c\n]*\x7c){4}\s*new:[^\x7c\n]*[Cc]overage` | file:vetting.md |
| C-2 | Does the row R-1094 (start with continuous delivery) go to the recorded item of the automated deployment, C-38? | program | `R-1094 \x7c(?:[^\x7c\n]*\x7c){4}\s*C-38\b` | file:vetting.md |
| C-3 | Is the cell "Goes to" of no row empty or a decision of 3.3? | program | `\A(?![\s\S]*R-\d+ \x7c(?:[^\x7c\n]*\x7c){4}\s*(?:3\.3[^\x7c\n]*)?\x7c)` | file:vetting.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| exit | the only arm: the decisions and the checklist of the trial I-4, and its 117 requirements that went to a decision of 3.3, with an empty cell "Goes to" | prompts/exit.md | inputs/case |

- **One arm**: the test measures one stage with one rule on recorded input.

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Edit, Write
- **Runs for each arm**: 3
- **Time limit**: 1800
- **Git repository**: no
- **Fewer than five runs**: a stage test is small on purpose; three runs show if the stage is stable. A full trial follows only when a stage test shows a difference.

## 6. Words of the expected answer

- coverage: the recorded requirement R-1026 and one recorded decision of 3.3 hold the word; the prompt does not. The test is where the session puts the requirement.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| exit | C-1 | 1 |
| exit | C-2 | 2 |
| exit | C-3 | 3 |

The agent also predicts, without a criterion: each run writes between 10 and 40 different new items for the 117 rows.

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
