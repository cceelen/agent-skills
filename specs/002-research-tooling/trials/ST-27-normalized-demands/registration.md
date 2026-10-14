# Experiment: stage test of the duplicates after a normalization of the requirements

## 1. Question

- **Quote**: "duplication detection will only work once requirements have been normalized."
- **Date**: 2026-10-14
- **Decision**: what is done after each outcome.
  - `confirmed`: the normalization is a candidate for the tooling. The owner gets the groups and decides on the form of the fields before anything is built.
  - `refuted`: a normalization into these fields does not let a program find duplicates across sources in this item. The owner gets the result as "no gain".
  - `not decided`: two more runs.

## 2. Hypothesis

- **Statement**: After a session brings the requirement rows of one item of the trial I-25 into a fixed form, a program finds ten or more groups with the same practice and the same object that join rows of two or more sources.
- **Forbidden result**: the program finds nine or fewer such groups, in two or more of three runs.
- **Criterion**: C-1
- **Confirmed when**: `case >= 2`
- **Refuted when**: `case <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does the program find ten or more groups with the same practice and the same object, with rows of two or more sources? | program | `(?m)^Groups with the same practice and the same object, with rows of two or more sources: [1-9]\d+$` | file:groups.md |
| C-2 | Does the program find ten or more groups with the same practice, with rows of two or more sources? | program | `(?m)^Groups with the same practice, with rows of two or more sources: [1-9]\d+$` | file:groups.md |
| C-3 | Does the table hold the 98 rows of the input? | program | `(?m)^Rows: 98$` | file:groups.md |
| C-4 | Does the program find twenty or more different practices? | program | `(?m)^Groups with the same practice: (?:[2-9]\d\|\d{3,})$` | file:groups.md |
| C-5 | Read the table. Look at the rows that have the same practice and the same object. Do the rows of each such pair state the same demand, so that a project that meets the one meets the other also, apart from the condition and the measure? Answer yes only if this holds for each pair that you examine; examine ten pairs or all pairs if there are fewer. | judge | | file:normal.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| case | the only arm: the 98 requirement rows of the item for the tests of the trial I-25, the task of the normalization and the program that groups the rows by their fields | prompts/normalize.md | inputs/case |

- **One arm**: the stage test ST-26 is the comparison. It gave the same rows to a session that grouped the sentences: 2 groups joined rows of two sources.
- **The criterion C-4**: it guards against a practice so general that it joins each row. Twenty is about one fifth of the rows.
- **The program**: the file group.py of the input is a test program of the agent of the factory, not a program of the tooling. Two rows are one group when their practice and their object have the same words after the case and the punctuation are removed.

## 5. Subject

- **Product**: claude
- **Model**: sonnet
- **Tools**: Read, Write, Bash
- **Runs for each arm**: 3
- **Time limit**: 1800
- **Git repository**: no
- **Fewer than five runs**: a stage test is small on purpose.

## 6. Words of the expected answer

- `coverage`: the word is in three rows of the input, as data of these rows. The prompt does not hold it.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| case | C-1 | 2 |
| case | C-2 | 3 |
| case | C-3 | 3 |
| case | C-4 | 3 |
| case | C-5 | 2 |

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
