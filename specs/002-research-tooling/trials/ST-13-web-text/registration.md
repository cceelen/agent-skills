# Experiment: stage test of a reader that gets the text of a web source

## 1. Question

- **Quote**: "ok. we can return the text with index but the text is not allowed to be comited."
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome.
  - `confirmed`: the rule stays: a web source is converted, and the reader of converted files reads its text.
  - `refuted`: the text gives a reader no more requirements than the web tool. The conversion of a web source stays a program, and the procedure does not ask for it.
  - `not decided`: five more runs for each arm.

## 2. Hypothesis

- **Statement**: A reader that gets the text of a web page as a converted file reports 25 or more requirements of the page in more runs than a reader that fetches the same page with its web tool.
- **Forbidden result**: the reader with the text reports 25 or more requirements in the same number of runs as the reader with the web tool, or in fewer.
- **Criterion**: C-1
- **Confirmed when**: `text - web >= 3`
- **Refuted when**: `text - web <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does the report have 25 or more requirement lines? | program | `(?m)(?:^REQ \x7c[^\n]*\n(?:(?!REQ \x7c)[^\n]*\n)*){24}^REQ \x7c` | final |
| C-2 | Does the report have 20 or more requirement lines? | program | `(?m)(?:^REQ \x7c[^\n]*\n(?:(?!REQ \x7c)[^\n]*\n)*){19}^REQ \x7c` | final |
| C-3 | Does a requirement line name a secret? | program | `(?mi)^REQ [^\n]*secret` | final |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| web | the reader fetches the page with its web tool | prompts/web.md | inputs/web |
| text | the reader reads the converted file of the same page, written by `web.py` on 2026-10-11 | prompts/text.md | inputs/text |

- **More than one difference**: the arm `text` has a different sentence in the prompt and one more file in its folder. The two belong together: the file is the source that the sentence names.

## 5. Subject

- **Product**: claude
- **Model**: haiku
- **Tools**: Read, WebFetch
- **Runs for each arm**: 5
- **Time limit**: 600
- **Git repository**: no

## 6. Words of the expected answer

- (none): the test counts lines. The prompt names the page, and the task of the reader names the form of a line.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| web | C-1 | 0 |
| web | C-2 | 0 |
| web | C-3 | 5 |
| text | C-1 | 5 |
| text | C-2 | 5 |
| text | C-3 | 5 |

Before the registration, the agent made one reading for each arm outside the gate, to set the limit of C-1: 13 lines with the web tool, 34 lines with the text.

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
