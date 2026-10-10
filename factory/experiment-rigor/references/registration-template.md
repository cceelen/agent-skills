# Experiment: <short name>

## 1. Question

- **Quote**: "<the words of the owner, not changed>"
- **Date**: <YYYY-MM-DD, the date of the quote>
- **Decision**: what is done after each outcome.
  - `confirmed`: <what is done>
  - `refuted`: <what is done>
  - `not decided`: <what is done>

## 2. Hypothesis

- **Statement**: <one sentence>
- **Forbidden result**: <the result that the hypothesis forbids>
- **Criterion**: <the id of the criterion that the limits count>
- **Confirmed when**: `<ARM - ARM >= NUMBER>`
- **Refuted when**: `<ARM - ARM <= NUMBER>`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | <a question with the answer yes or no> | <program or judge> | `<regular expression>` | final |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| <id> | <the one thing that differs> | <prompts/a.md> | <inputs/a or (empty)> |

## 5. Subject

- **Product**: <claude>
- **Model**: <the model of the subject>
- **Tools**: <(none), or the names of the tools with commas>
- **Runs for each arm**: <5 or more>
- **Time limit**: <seconds for one session>
- **Git repository**: <yes or no>

## 6. Words of the expected answer

- `<word or phrase>`

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| <arm> | C-1 | <number of runs with the answer yes> |

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
