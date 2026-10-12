# Experiment: stage test of the ladder in the hands of a session

## 1. Question

- **Quote**: "assigning static values from the source (regulation, governance set a very high value) and some lower values for other sources ... a ladder ... and then creating a simple level system for the depth of an implementation of a skill to do in the first iteration is enough."
- **Date**: 2026-10-12
- **Decision**: what is done after each outcome.
  - `confirmed`: the row I-22 of the iterations gets this test as its test. The program `place.py` stays as it is.
  - `refuted`: a session does not give a class to a source when no item is pending. The program `place.py` names each item that has a source without a class as pending. No other change.
  - `not decided`: two more runs.

## 2. Hypothesis

- **Statement**: A session that does the part "The value and the level of an item" on a specification with two sources without a class places the item that a regulation asks for from that regulation.
- **Forbidden result**: the row of the item C-27 does not name the regulation S-17 as its strongest source, in two or more of three runs.
- **Criterion**: C-1
- **Confirmed when**: `case >= 2`
- **Refuted when**: `case <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does the row of the item C-27 name `regulation (S-17)` as its strongest source? | program | `(?m)^\x7c C-27 \x7c.*\x7c\s*regulation \(S-17\)\s*\x7c` | file:spec.md |
| C-2 | Has the source S-17 the class `regulation` and the source S-18 the class `standard`? | program | `(?s)(?=.*\x7c S-17 \x7c[^\n]*\x7c\s*regulation\s*\x7c)(?=.*\x7c S-18 \x7c[^\n]*\x7c\s*standard\s*\x7c)` | file:spec.md |
| C-3 | Has each row of the ten items a level 1, 2 or 3, and no row the word pending? | program | `(?s)\A(?!.*\n\x7c C-\d+ \x7c[^\n]*\x7c\s*pending\s*\x7c)(?:.*?\n\x7c C-\d+ \x7c(?:[^\x7c\n]*\x7c){3}\s*[123]\s*\x7c){10}` | file:spec.md |
| C-4 | Read this file. Does it give ten checklist items in one order, each with a level and a strongest source, and the values of a ladder of source classes? | judge | | file:review.md |
| C-5 | Read this file. Does its writer state how severe, how probable or how costly something is for a checklist item, or propose a level for an item that differs from the level that the file gives for that item? | judge | | file:review.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| case | the only arm: the ten items of the stage test ST-19 with their 174 requirement rows, in the form of the ladder; the sources S-17 and S-18 have no class | prompts/task.md | inputs/case |

- **One arm**: one run of the program on the input, before the registration, shows the state without a session: no item is pending, the result code is 0, and the item C-27 has the value of the class `standard`.

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Edit, Write, Grep, Bash
- **Runs for each arm**: 3
- **Time limit**: 1500
- **Git repository**: no
- **Fewer than five runs**: a stage test is small on purpose.

## 6. Words of the expected answer

- (none): the prompt names two files and no source and no class. The file part.md holds step 6 of phase 2 of the procedure, which names the classes and their rule, as a session of phase 2 has it.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| case | C-1 | 1 |
| case | C-2 | 1 |
| case | C-3 | 3 |
| case | C-4 | 3 |
| case | C-5 | 0 |

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
