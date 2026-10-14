# Experiment: stage test of the duplicates after a normalization against a vocabulary of practices

## 1. Question

- **Quote**: "we do both after each other"
- **Date**: 2026-10-14
- **Decision**: what is done after each outcome.
  - `confirmed`: if the criterion C-5 is also yes in two or more runs, the vocabulary is a candidate for the tooling, and the owner decides on it before anything is built. If C-5 is no, the result is "no gain".
  - `refuted`: a vocabulary of the session does not let a program find duplicates across sources in this item. The owner gets the result as "no gain".
  - `not decided`: two more runs.

## 2. Hypothesis

- **Statement**: After a session writes a vocabulary of the practices of one item of the trial I-25 and brings each requirement row to one term of it, a program finds ten or more terms that join rows of two or more sources.
- **Forbidden result**: the program finds nine or fewer such terms, in two or more of three runs.
- **Criterion**: C-1
- **Confirmed when**: `case >= 2`
- **Refuted when**: `case <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does the program find ten or more groups with the same practice and the same object, with rows of two or more sources? | program | `(?m)^Groups with the same practice and the same object, with rows of two or more sources: [1-9]\d+$` | file:groups.md |
| C-3 | Does the table hold the 98 rows of the input? | program | `(?m)^Rows: 98$` | file:groups.md |
| C-4 | Does the program find twenty or more different practices? | program | `(?m)^Groups with the same practice: (?:[2-9]\d\|\d{3,})$` | file:groups.md |
| C-5 | Read the table. Look at the rows that have the same practice. Do the rows of each such pair state the same demand, so that a project that meets the one meets the other also, apart from the condition and the measure? Answer yes only if this holds for each pair that you examine; examine ten pairs or all pairs if there are fewer. | judge | | file:normal.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| case | the only arm: the 98 requirement rows of the item for the tests of the trial I-25, the task of the vocabulary and of the normalization, and the program that groups the rows | prompts/vocabulary.md | inputs/case |

- **One arm**: the stage test ST-27 is the comparison. It used the same rows, the same fields and the same program, with free terms: 3, 8 and 5 groups across sources, and a judge found a wrong group in each run.
- **The object**: the term holds the object, thus the cell Object is `-` in each row, and the groups of the program are the groups of the terms.
- **The owner**: in the tooling the owner would confirm the vocabulary. In this test nobody confirms it.

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
| case | C-1 | 1 |
| case | C-3 | 3 |
| case | C-4 | 3 |
| case | C-5 | 2 |

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
