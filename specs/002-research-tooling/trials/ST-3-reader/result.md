# Result of the experiment: stage test of the fixed form of a requirement line in the report of a reader

- Registration: seal 833c2972c427, sealed on 2026-10-11, commit (none)
- Valid runs: 5 of 5

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | fixed | 5 | 5 | 100 % | 57 % to 100 % | 4 |
| C-2 | fixed | 5 | 5 | 100 % | 57 % to 100 % | 5 |
| C-3 | fixed | 5 | 5 | 100 % | 57 % to 100 % | 3 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: A reader of the smallest model that gets the fixed form writes each requirement line in that form, with no quotation mark.
- Criterion: C-1
- Confirmed when: `fixed >= 4`
- Refuted when: `fixed <= 2`
- Counts: fixed = 5
- Verdict: confirmed

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## What the five runs show (from the final text of the runs)

- The runs report 12, 14, 17, 15 and 16 requirement lines. Each line has the fixed form. No line holds a quotation mark.
- The recorded reports of the same pages hold 15 lines (trial I-4, each with a quotation mark) and 16 lines (trial I-5).
- The test used the smallest model and no reader agent of a session.

Predictions: 2 of 3 were correct (C-1 as a verdict, C-2). The agent predicted C-3 in three of five runs; it is in five.

The test does not show how a report gets into a file that a program can read.
