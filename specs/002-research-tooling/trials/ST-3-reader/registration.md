# Experiment: stage test of the fixed form of a requirement line in the report of a reader

## 1. Question

- **Quote**: "continue the trials, tests, and improvement iterations. make sure that you keep what helps and avoid onboarding too much complexity"
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome.
  - `confirmed`: the task of the reader keeps the fixed form. A program can then write the register from the reports.
  - `refuted`: the reader does not keep the form. The form is removed from the task, and no program for the intake is built on it.
  - `not decided`: three more runs of this test.

## 2. Hypothesis

- **Statement**: A reader of the smallest model that gets the fixed form writes each requirement line in that form, with no quotation mark.
- **Forbidden result**: a line that starts with `REQ` and does not have the form, in three or more of five runs.
- **Criterion**: C-1
- **Confirmed when**: `fixed >= 4`
- **Refuted when**: `fixed <= 2`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does each line that starts with `REQ` have the fixed form, and is there one such line at least? | program | `(?m)\A(?=[\s\S]*^REQ \x7c)(?![\s\S]*^REQ(?! \x7c [^\x7c\n]+ \x7c [^\x7c\n]+ \x7c [^\x7c\n]+$)(?! \x7c none$))` | final |
| C-2 | Does the report hold eight or more lines in the fixed form? | program | `(?m)(?:^REQ \x7c [^\x7c\n]+ \x7c [^\x7c\n]+ \x7c [^\x7c\n]+$[\s\S]*?){8}` | final |
| C-3 | Does no line that starts with `REQ` hold a quotation mark? | program | `(?m)\A(?![\s\S]*^REQ .*["“”])` | final |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| fixed | the only arm: the task of the reader with the fixed form of point 4, and 18 pages of one converted source | prompts/read.md | inputs/case |

- **One arm**: the test measures one stage on recorded input. The recorded reports of the trials I-4 and I-5 show the old form: seven different headings for point 4, and a quotation mark in a quarter of the lines.

## 5. Subject

- **Product**: claude
- **Model**: haiku
- **Tools**: Read
- **Runs for each arm**: 5
- **Time limit**: 1200
- **Git repository**: no

## 6. Words of the expected answer

- `REQ`: the task file of the input holds the word. The test is if the reader keeps the form.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| fixed | C-1 | 4 |
| fixed | C-2 | 5 |
| fixed | C-3 | 3 |

The agent also predicts, without a criterion: each run reports between 10 and 25 requirement lines. The recorded reports of the same pages hold 15 and 16.

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
