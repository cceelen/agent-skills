# Experiment: stage test of the answers of risk and reward from the requirement rows

## 1. Question

- **Quote**: "ok. try this change and compare again."
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome.
  - `confirmed`: the rule goes into the task for the answers: the session reads the requirement rows of each item and names the row that gives the answer.
  - `refuted`: the requirement rows do not give the harm of an item. The rule does not go into the task. The research needs sources that state harm, and that is a step of the search.
  - `not decided`: two more runs for each arm.

## 2. Hypothesis

- **Statement**: A session that reads the requirement rows of each item names, for five or more of ten items, a source for the severity that states a harm, in more runs than a session that reads only the evidence record.
- **Forbidden result**: the session with the requirement rows does this in the same number of runs as the session with the evidence record, or in fewer.
- **Criterion**: C-2
- **Confirmed when**: `lines - evidence >= 2`
- **Refuted when**: `lines - evidence <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Do eight or more rows of the table Items name a source in the cell Severity? | program | `(?m)(?:^\x7c C-\d+ \x7c \d \([^\x7c]*S-\d+[^\n]*\n(?:(?!\x7c C-\d+ \x7c \d \([^\x7c]*S-\d+)[^\n]*\n)*){7}^\x7c C-\d+ \x7c \d \([^\x7c]*S-\d+` | file:vetting.md |
| C-2 | Read the table Items of this file. Count each row whose cell Severity names a row R-n of the table Requirements of this file, or a source S-n with a location, where that row R-n, or the row of the source S-n in the file evidence.md of this packet, states a harm, a threat or a consequence that the item prevents. A statement of only a duty does not count. Is the count five or more? | judge | | file:vetting.md |
| C-3 | Read the table Items of the file vetting.md of this packet. Count each row whose cell Probability names a row R-n of the table Requirements of that file, or a source S-n with a location, where that row R-n, or the row of the source S-n in this file, states how often or how probable a harm is. Is the count three or more? | judge | | file:evidence.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| evidence | the task for the answers as it is in the repository: the session reads the evidence record | prompts/task.md | inputs/evidence |
| lines | the task for the answers has one more rule: read the requirement rows of the item and name the row that gives the severity, the probability or the breadth | prompts/task.md | inputs/lines |

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Edit, Write, Grep
- **Runs for each arm**: 3
- **Time limit**: 1500
- **Git repository**: no
- **Fewer than five runs**: a stage test is small on purpose.

## 6. Words of the expected answer

- (none): the prompt names only the task file. The added rule says what a row must state to give an answer; the judge asks for the same. The input is the specification of the trial I-14 with ten items that a program chose with a fixed seed, and the requirement rows of these items.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| evidence | C-1 | 0 |
| evidence | C-2 | 0 |
| evidence | C-3 | 0 |
| lines | C-1 | 2 |
| lines | C-2 | 2 |
| lines | C-3 | 0 |

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
