# Experiment: stage test of the answers of risk and reward with the rows of a regulation and of a public recommendation

## 1. Question

- **Quote**: "We can only mark requirements that come from governance and regulation and give them high priorities depending upon the aspect and later in the skill the usecase."
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome.
  - `confirmed`: the iterations I-19 to I-21 stay as they are. The next test is a full trial.
  - `refuted`: the rows of such sources do not give the answer for a basic practice. The owner gets the answers of the runs, and the rule for the answer `probability` is examined again before a full trial.
  - `not decided`: two more runs for each arm.

## 2. Hypothesis

- **Statement**: A session that gets the requirement rows of one regulation and of one recommendation of a public authority names, for the item of the automated build with tests, a requirement row of such a source that requires or recommends the practice, in more runs than a session without these rows.
- **Forbidden result**: the session with the rows does this in the same number of runs as the session without them, or in fewer.
- **Criterion**: C-3
- **Confirmed when**: `join - old >= 2`
- **Refuted when**: `join - old <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Has the source S-17 the class `regulation` and the source S-18 the class `standard`? | program | `(?s)(?=.*\x7c S-17 \x7c[^\n]*\x7c\s*regulation\s*\x7c)(?=.*\x7c S-18 \x7c[^\n]*\x7c\s*standard\s*\x7c)` | file:spec.md |
| C-2 | Does the cell Probability of the item C-05 name the source S-18? | program | `(?m)^\x7c C-05 \x7c[^\x7c]*\x7c \d \([^\x7c]*S-18` | file:vetting.md |
| C-3 | Read the row of the item C-05 in the table Items of this file. Does its cell Probability name a row R-n of the table Requirements of this file, where that row R-n names C-05 in its last cell, the source of that row has the class regulation, governance, standard or foundation in the table of section 2 of the file spec.md of this packet, and the sentence of that row requires or recommends automated tests or an automated build? | judge | | file:vetting.md |
| C-4 | Has the cell Probability of the item C-27 the number 3 with the source S-17? | program | `(?m)^\x7c C-27 \x7c[^\x7c]*\x7c 3 \([^\x7c]*S-17` | file:vetting.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| old | the ten items of the stage test ST-15 with their 143 requirement rows, the task for the answers and the rubric as they are in the repository | prompts/task.md | inputs/old |
| join | the same, with two more sources in section 2 without a class, and their 31 requirement rows that go to the ten items | prompts/task.md | inputs/join |

- **More than one difference**: the arm `join` has two more rows of sources in `spec.md` and 31 more rows in `vetting.md`. The two belong together: each new row names one of the new sources.

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Edit, Write, Grep
- **Runs for each arm**: 3
- **Time limit**: 1500
- **Git repository**: no
- **Fewer than five runs**: a stage test is small on purpose.

## 6. Words of the expected answer

- (none): the prompt names two files and no source. Five small readers reported 329 requirement lines from the text of the two sources; an agent of the largest model sent 31 of them to one of the ten items. Five of the 31 go to the item C-05, all of the source S-18. The agent of the factory saw these five rows before the registration.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| old | C-1 | 0 |
| old | C-2 | 0 |
| old | C-3 | 0 |
| old | C-4 | 0 |
| join | C-1 | 2 |
| join | C-2 | 3 |
| join | C-3 | 3 |
| join | C-4 | 2 |

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
