# Experiment: stage test of the search for the regulation, the governance and the public recommendations of an aspect

## 1. Question

- **Quote**: "dependending upon the aspect / topic we have regulation and governance and public recommendations having very very strong lists and voices"
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome.
  - `confirmed`: the rule goes into the step "List what exists" of the procedure.
  - `refuted`: the rule does not make a session find such sources beyond the view of security. The rule is not added in this form, and the next test gives the search the stakeholders that are bound.
  - `not decided`: two more runs of this test.

## 2. Hypothesis

- **Statement**: A session that does the step "List what exists" with the rule for the regulation, the governance and the public recommendations lists three or more such sources whose subject is not security.
- **Forbidden result**: the list has fewer than three such sources with a subject other than security, in each of three runs.
- **Criterion**: C-2
- **Confirmed when**: `search >= 2`
- **Refuted when**: `search <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does the list hold a row of the kind `regulation`, a row of the kind `governance` and a row of the kind `public-recommendation`? | program | `(?s)(?=.*\x7c\s*regulation\s*\x7c)(?=.*\x7c\s*governance\s*\x7c)(?=.*\x7c\s*public-recommendation\s*\x7c)` | file:sources.md |
| C-2 | Read the table Sources of this file. Count the rows with the kind regulation, governance or public-recommendation whose title shows a subject other than the security of software or of information: for example the operation, the quality or the delivery of software, or the rules of a field such as finance, health or safety. Is the count three or more? | judge | | file:sources.md |
| C-3 | Read the table Sources of this file. Is each row with the kind regulation a law, a regulation, a directive or an order of a state or of a union of states? Answer no if one such row is a standard, a guideline or a framework, or if there is no such row. | judge | | file:sources.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| search | the only arm: the step "List what exists" of the procedure with the rule for the regulation, the governance and the public recommendations | prompts/search.md | inputs/case |

- **One arm**: the three recorded runs of the stage test ST-6 show the step without the rule. Two of them list one regulation, each lists one or two recommendations of a public authority, and all of these are about security. The trial I-14 took none of them as a source.

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Write, WebSearch, WebFetch
- **Runs for each arm**: 3
- **Time limit**: 1800
- **Git repository**: no
- **Fewer than five runs**: a stage test is small on purpose.

## 6. Words of the expected answer

- (none): the prompt names the kinds of a source, and no regulation, no authority and no framework. The rule names the three kinds and no example.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| search | C-1 | 3 |
| search | C-2 | 2 |
| search | C-3 | 2 |

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
