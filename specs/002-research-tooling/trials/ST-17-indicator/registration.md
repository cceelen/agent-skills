# Experiment: stage test of the probability answer from what regulations and standards ask for

## 1. Question

- **Quote**: "regulated: we have hard defined what the minimum bar is. un-regulated: the regulated environments do all of that due to past problems ... regulation points us to existing issues and their recommendations are strong indicators."
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome.
  - `confirmed`: the rubric for items gets the question (version 3), and the task for the answers gets the rule that a requirement row of a regulation, a standard or a foundation gives the answer.
  - `refuted`: the question is not changed in this form. The owner gets the answers of the runs and decides.
  - `not decided`: two more runs for each arm.

## 2. Hypothesis

- **Statement**: A session that is asked how strongly regulations and standards ask for an item names, for seven or more of ten items, a requirement row of a source of the class `standard` or `foundation` that requires or recommends a practice, in more runs than a session that is asked how probable the harm is.
- **Forbidden result**: the session with the new question does this in the same number of runs as the session with the old question, or in fewer.
- **Criterion**: C-2
- **Confirmed when**: `new - old >= 2`
- **Refuted when**: `new - old <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Do seven or more rows of the table Items name a source in the cell Probability? | program | `(?m)(?:^\x7c C-\d+ \x7c[^\x7c]*\x7c \d \([^\x7c]*S-\d+[^\n]*\n(?:(?!\x7c C-\d+ \x7c[^\x7c]*\x7c \d \([^\x7c]*S-\d+)[^\n]*\n)*){6}^\x7c C-\d+ \x7c[^\x7c]*\x7c \d \([^\x7c]*S-\d+` | file:vetting.md |
| C-2 | Read the table Items of this file. Count each row whose cell Probability names a row R-n of the table Requirements of this file, where that row R-n names the item in its last cell, the source of that row has the class standard or foundation in the table of section 2 of the file spec.md of this packet, and the sentence of that row requires or recommends a practice. Is the count seven or more? | judge | | file:vetting.md |
| C-3 | Read the table Items of the file vetting.md of this packet, and the class of each source in the table of section 2 of this file. Is there one or more row of the table Items whose cell Probability has the number 3 while no row R-n that the cell names has a source of the class standard and a sentence that requires (shall, must, is required), or has the number 2 or 3 while no row R-n that the cell names has a source of the class standard or foundation? | judge | | file:spec.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| old | the input of the arm `lines` of the stage test ST-15: the question of the probability asks how probable the harm is | prompts/task.md | inputs/old |
| new | the question of the probability asks how strongly regulations and standards ask for the item | prompts/task.md | inputs/new |

- **More than one difference**: the question is in two files, the rubric and the task for the answers. The task has also the rule that says which requirement row gives the answer. The three belong together: the rule explains the scale of the question.

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Edit, Write, Grep
- **Runs for each arm**: 3
- **Time limit**: 1500
- **Git repository**: no
- **Fewer than five runs**: a stage test is small on purpose.

## 6. Words of the expected answer

- (none): the prompt names only the task file. The rule of the arm `new` names the classes of the sources and the words that require or recommend; the judge asks for the same. A program counted before the registration that each of the ten items has one or more requirement rows of a source of the class `standard` or `foundation`.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| old | C-1 | 0 |
| old | C-2 | 0 |
| old | C-3 | 0 |
| new | C-1 | 3 |
| new | C-2 | 3 |
| new | C-3 | 1 |

In the stage test ST-15, the arm `lines` named no source for a probability in each of three runs.

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
