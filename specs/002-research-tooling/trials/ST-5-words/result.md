# Result of the experiment: stage test of the words of an item of a basic practice in the calculation

- Registration: seal ff629f84e328, sealed on 2026-10-11, commit (none)
- Valid runs: 6 of 6

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | goal | 0 | 3 | 0 % | 0 % to 56 % | 0 |
| C-1 | measure | 3 | 3 | 100 % | 44 % to 100 % | 2 |
| C-2 | goal | 0 | 3 | 0 % | 0 % to 56 % | 0 |
| C-2 | measure | 3 | 3 | 100 % | 44 % to 100 % | 3 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|
| C-1 | goal, measure | p = 0.1000 |
| C-2 | goal, measure | p = 0.1000 |

## Verdict

- Hypothesis: A session gives the breadth 3 to an item that asks only for the report of the coverage in more runs than to an item that asks for a coverage goal.
- Criterion: C-1
- Confirmed when: `measure - goal >= 2`
- Refuted when: `measure - goal <= 0`
- Counts: goal = 0, measure = 3
- Verdict: confirmed

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## What the six runs show (from the files of the runs; the levels are computed with the formula of `place.py`)

| Arm | Run | Severity | Probability | Breadth | Adopt | Keep | Own risk | Score | Result |
|---|---|---|---|---|---|---|---|---|---|
| goal | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 16 | not admitted |
| goal | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 16 | not admitted |
| goal | 3 | 2 | 2 | 2 | 1 | 1 | 2 | 30 | level 2 |
| measure | 1 | 2 | 2 | 3 | 1 | 1 | 1 | 55 | level 1 |
| measure | 2 | 2 | 2 | 3 | 1 | 1 | 1 | 55 | level 1 |
| measure | 3 | 2 | 2 | 3 | 1 | 1 | 1 | 55 | level 1 |

- The item that names only the practice is on level 1 in each run. The item that holds a goal on which the sources disagree is on level 1 in no run.
- The three runs of the arm `measure` give the same six answers.

Predictions: 3 of 4 rows were correct. The agent predicted the breadth 3 in two of three runs of the arm `measure`; it is in three.

The test used one item of one aspect. It does not show that the rule holds for a different aspect.
