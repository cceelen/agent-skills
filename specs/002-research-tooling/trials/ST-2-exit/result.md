# Result of the experiment: stage test of the exit to a decision, on recorded requirements

- Registration: seal 6355ca19c97c, sealed on 2026-10-11, commit (none)
- Valid runs: 3 of 3

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | exit | 3 | 3 | 100 % | 44 % to 100 % | 1 |
| C-2 | exit | 2 | 3 | 67 % | 21 % to 94 % | 2 |
| C-3 | exit | 3 | 3 | 100 % | 44 % to 100 % | 3 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: A session that must give each requirement of a decision of 3.3 to a checklist item writes a new item that names the measure of test coverage for the requirement R-1026.
- Criterion: C-1
- Confirmed when: `exit >= 2`
- Refuted when: `exit <= 0`
- Counts: exit = 3
- Verdict: confirmed

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## What the three runs show (from the files of the runs)

- 117 requirements in each run. A new item for 95, 92 and 97 rows; a recorded item for 20, 21 and 18 rows; a duplicate for 2, 4 and 2 rows. No row has the exit `5`.
- Each run writes 45, 42 and 46 different new items. The recorded checklist has 42 items, thus the rule doubles the checklist before the calculation of risk and reward.
- The row R-1026 goes to a new item that names the coverage in each run.
- The test took about 12 minutes and no reader agent.

Predictions: 2 of 3 were correct (C-2, C-3). The agent predicted C-1 in one of three runs; it is in three. The agent predicted 10 to 40 new items; each run has more.

The test does not show the level that the calculation gives to a new item.
