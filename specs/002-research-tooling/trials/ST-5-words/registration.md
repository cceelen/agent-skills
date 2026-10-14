# Experiment: stage test of the words of an item of a basic practice in the calculation

## 1. Question

- **Quote**: "code coverage and static code analysis are both basic levels. just like running the tests, failing on failing builds and tests, and CVE list of scanned dependency."
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome.
  - `confirmed`: the procedure gets one rule for the words of an item: an item names the practice; a number, a goal or a threshold on which the sources disagree goes to a decision of section 3.3.
  - `refuted`: the words of the item do not decide the placement. No rule for the words is added. The next test examines the questions of the rubric.
  - `not decided`: two more runs for each arm.

## 2. Hypothesis

- **Statement**: A session gives the breadth 3 to an item that asks only for the report of the coverage in more runs than to an item that asks for a coverage goal.
- **Forbidden result**: the arm `measure` has the breadth 3 in no more runs than the arm `goal`.
- **Criterion**: C-1
- **Confirmed when**: `measure - goal >= 2`
- **Refuted when**: `measure - goal <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Is the breadth of the item C-44 the value 3? | program | `C-44 \x7c[^\x7c\n]*\x7c[^\x7c\n]*\x7c\s*3\b` | file:vetting.md |
| C-2 | Is the own risk of the item C-44 below 2? | program | `C-44 \x7c(?:[^\x7c\n]*\x7c){5}\s*[01]\b` | file:vetting.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| goal | the item C-44 asks that the coverage is measured against a goal that the project sets | prompts/answers.md | inputs/goal |
| measure | the item C-44 asks that the tests of each change report the coverage and that the team sees the report | prompts/answers.md | inputs/measure |

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Edit, Write
- **Runs for each arm**: 3
- **Time limit**: 1800
- **Git repository**: no
- **Fewer than five runs**: a stage test is small on purpose. A full trial follows only when a stage test shows a difference.

## 6. Words of the expected answer

- (none): the item is in the input of each arm. The test is the value that the session writes.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| goal | C-1 | 0 |
| measure | C-1 | 2 |
| goal | C-2 | 0 |
| measure | C-2 | 3 |

The agent predicts level 1 for the item C-44 in two of three runs of the arm `measure` and in no run of the arm `goal`, computed with the formula of `place.py` after the runs.

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
