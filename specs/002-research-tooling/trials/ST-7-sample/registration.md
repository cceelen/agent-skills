# Experiment: stage test of the reader of a sample of the practice

## 1. Question

- **Quote**: "so the goal of the factory is to be able to scan for interesting patterns, tooling, integrations and similar in samples"
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome.
  - `confirmed`: the task of the reader of a sample stays. The next step is a program that counts the lines of many samples.
  - `refuted`: a reader of the smallest model does not report a sample in the fixed form, or it does not find what the file holds. The task is removed, and the next test uses a larger model.
  - `not decided`: three more runs of this test.

## 2. Hypothesis

- **Statement**: A reader of the smallest model reports what one file of a project uses in the fixed form, and the report holds three tools that the file runs and one pattern at least.
- **Forbidden result**: a line that starts with `USE` and does not have the form, or a report without the three tools, or a report without a pattern, in three or more of five runs.
- **Criterion**: C-4
- **Confirmed when**: `sample >= 4`
- **Refuted when**: `sample <= 2`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does each line that starts with `USE` have the fixed form, and is there one such line at least? | program | `(?m)\A(?=[\s\S]*^USE \x7c)(?![\s\S]*^USE(?! \x7c [a-z]+ \x7c [^\x7c\n]+ \x7c [^\x7c\n]+ \x7c [^\x7c\n]+$))(?![\s\S]*^USE \x7c (?!tool )(?!integration )(?!framework )(?!pattern ))` | final |
| C-2 | Does the report hold a tool line for each of three tools that the file runs: trivy, semgrep and syft? | program | `(?im)\A(?=[\s\S]*^USE \x7c tool \x7c[^\x7c\n]*trivy)(?=[\s\S]*^USE \x7c tool \x7c[^\x7c\n]*semgrep)(?=[\s\S]*^USE \x7c tool \x7c[^\x7c\n]*syft)` | final |
| C-3 | Does the report hold one pattern line at least? | program | `(?m)^USE \x7c pattern \x7c` | final |
| C-4 | Are C-1, C-2 and C-3 true together? | program | `(?im)\A(?=[\s\S]*^USE \x7c pattern \x7c)(?=[\s\S]*^USE \x7c tool \x7c[^\x7c\n]*trivy)(?=[\s\S]*^USE \x7c tool \x7c[^\x7c\n]*semgrep)(?=[\s\S]*^USE \x7c tool \x7c[^\x7c\n]*syft)(?![\s\S]*^USE(?! \x7c [a-z]+ \x7c [^\x7c\n]+ \x7c [^\x7c\n]+ \x7c [^\x7c\n]+$))(?![\s\S]*^USE \x7c (?!tool )(?!integration )(?!framework )(?!pattern ))` | final |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| sample | the only arm: the task of the reader of a sample, and one pipeline template of a public collection, 2238 lines | prompts/read.md | inputs/case |

- **One arm**: the test measures one new stage. No earlier form of the stage exists.

## 5. Subject

- **Product**: claude
- **Model**: haiku
- **Tools**: Read
- **Runs for each arm**: 5
- **Time limit**: 1200
- **Git repository**: no

## 6. Words of the expected answer

- `trivy`, `semgrep`, `syft`: the file of the input holds the words. The prompt and the task do not.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| sample | C-1 | 5 |
| sample | C-2 | 4 |
| sample | C-3 | 4 |
| sample | C-4 | 3 |

The agent predicts, without a criterion: each run reports between 15 and 40 lines, and fewer than half of the names of the patterns are the same in two runs.

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
