# Experiment: stage test of the grouping of the requirements of one item into distinct demands

## 1. Question

- **Quote**: "also we need to check for duplication. the same or similar requirements will come from different sources"
- **Date**: 2026-10-14
- **Decision**: what is done after each outcome.
  - `confirmed`: the grouping is built into the tooling: a task for an agent, a program that records the groups, and the ladder that reads them.
  - `refuted`: the grouping does not make a lost demand visible. The owner gets the result as "no gain". The grouping is not built without a decision of the owner.
  - `not decided`: two more runs.

## 2. Hypothesis

- **Statement**: A session that groups the requirement rows of one item of the trial I-25 into distinct demands gives the measure of the coverage of the tests a group of its own.
- **Forbidden result**: no row of the table names the coverage in its cell "Demand", in two or more of three runs.
- **Criterion**: C-1
- **Confirmed when**: `case >= 2`
- **Refuted when**: `case <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does a row of the table name the coverage in its cell "Demand"? | program | `(?mi)^\x7c[^\x7c\n]*coverage[^\x7c\n]*\x7c` | file:demands.md |
| C-2 | Does the table hold a group with two or more rows? | program | `(?m)^\x7c[^\x7c\n]*\x7c[^\x7c\n]*R-\d+\s*,\s*R-\d+` | file:demands.md |
| C-3 | Read the table. Do two of its rows state the same demand, so that a project that meets the one meets the other also? | judge | | file:demands.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| case | the only arm: the 98 requirement rows of the item C-31 of the trial I-25, each with its sentence and its source, and the task of the grouping | prompts/group.md | inputs/case |

- **One arm**: the input is the case without groups. In the trial I-25, no row of the 2499 has the exit of a duplicate. A program counted before this registration: three rows of this item name the coverage, and the item of the checklist does not name it.
- **The item**: it is the item for the tests. The owner names a measure of the coverage as a basic practice, and the checklist of the trial I-25 has no item for it.

## 5. Subject

- **Product**: claude
- **Model**: sonnet
- **Tools**: Read, Write
- **Runs for each arm**: 3
- **Time limit**: 1200
- **Git repository**: no
- **Fewer than five runs**: a stage test is small on purpose.

## 6. Words of the expected answer

- `coverage`: the word is in three rows of the input, as data of these rows. The prompt does not hold it. The test examines if the grouping keeps the demand apart.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| case | C-1 | 3 |
| case | C-2 | 3 |
| case | C-3 | 1 |

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
