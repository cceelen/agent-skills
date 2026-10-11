# Result of the experiment: stage test of the reader of a sample of the practice

- Registration: seal ef523e8ec155, sealed on 2026-10-11, commit (none)
- Valid runs: 5 of 5

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | sample | 5 | 5 | 100 % | 57 % to 100 % | 5 |
| C-2 | sample | 5 | 5 | 100 % | 57 % to 100 % | 4 |
| C-3 | sample | 5 | 5 | 100 % | 57 % to 100 % | 4 |
| C-4 | sample | 5 | 5 | 100 % | 57 % to 100 % | 3 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: A reader of the smallest model reports what one file of a project uses in the fixed form, and the report holds three tools that the file runs and one pattern at least.
- Criterion: C-4
- Confirmed when: `sample >= 4`
- Refuted when: `sample <= 2`
- Counts: sample = 5
- Verdict: confirmed

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## What the five runs show (from the final text of the runs)

| Kind | Lines in each run | Different names in the five runs | Names that are in each run |
|---|---|---|---|
| tool | 34, 36, 30, 39, 37 | 48 | 26 |
| integration | 9, 10, 10, 11, 12 | 24 | 5 |
| framework | 14, 14, 12, 10, 19 | 36 | 2 |
| pattern | 29, 22, 23, 25, 22 | 112 | 0 |

- Each of 418 lines has the fixed form.
- A program can count the tools: more than half of the names are the same in each run.
- A program cannot count the patterns by their names: no name is in two runs. A pattern needs a step that puts the same pattern of two reports together.
- The test used the smallest model, one file and one aspect.

Predictions: the verdict and the prediction on the names of the patterns were correct. The agent predicted 15 to 40 lines for each run; each run has 75 to 90.
