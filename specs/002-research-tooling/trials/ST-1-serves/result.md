# Result of the experiment: stage test of the cell Serves, on recorded requirements

- Registration: seal 25d0fbd1da66, sealed on 2026-10-11, commit (none)
- Valid runs: 3 of 3

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | serves | 0 | 3 | 0 % | 0 % to 56 % | 2 |
| C-2 | serves | 0 | 3 | 0 % | 0 % to 56 % | 2 |
| C-3 | serves | 0 | 3 | 0 % | 0 % to 56 % | 1 |
| C-4 | serves | 3 | 3 | 100 % | 44 % to 100 % | 3 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: A session that gets the charter and recorded requirements writes, for the requirement about the measure of test coverage, a line of the charter that keeps it in the checklist (P-1 or P-2).
- Criterion: C-1
- Confirmed when: `serves >= 2`
- Refuted when: `serves <= 0`
- Counts: serves = 0
- Verdict: refuted

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## What the three runs show (from the files of the runs)

- 151 requirements in each run. `none` in 140, 139 and 141 rows.
- 148 of the 151 rows have the same cell in the three runs. The stage is stable.
- The line P-2 (basic practices) is in no row of a run. The lines that are used: P-1 (3 to 5 rows), T-1 and K-0 (2 to 3), T-2 and P-4 (1 to 2), P-3, P-5 and T-3 (1 each).
- The row of the measure of coverage (R-1026) and the row of fuzzing (R-606): `none` in each run.
- 10 rows of the architecture: 1 or 2 serve a line.
- The test took about three minutes and no reader agent.

Predictions: 1 of 4 was correct (C-4). The agent predicted that the session connects the rows with P-1 or P-2 in two of three runs.

Thus the effects of the charter place nothing: a session does not see from the words of a requirement that it is a basic practice.
