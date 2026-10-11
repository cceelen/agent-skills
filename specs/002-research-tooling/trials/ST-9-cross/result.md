# Result of the experiment: stage test of the grouping of the patterns of different projects

- Registration: seal e07d42f784bb, sealed on 2026-10-11, commit (none)
- Valid runs: 3 of 3

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | cross | 3 | 3 | 100 % | 44 % to 100 % | 3 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: A session that gets the pattern lines of four different projects finds a pattern that two or more projects have.
- Criterion: C-1
- Confirmed when: `cross >= 2`
- Refuted when: `cross <= 0`
- Counts: cross = 3
- Verdict: confirmed

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## The measure (program `agreement.py` of the stage test ST-8, and the files of the runs)

| Run | Groups | Groups with lines of two or more projects | With lines of three or more projects |
|---|---|---|---|
| 1 | 72 | 12 | 5 |
| 2 | 72 | 12 | 5 |
| 3 | 71 | 13 | 5 |

| Runs | Pairs of lines together in the two runs | Pairs together in one run at least | Share |
|---|---|---|---|
| 1 and 2 | 25 | 25 | 1.00 |
| 1 and 3 | 25 | 26 | 0.96 |
| 2 and 3 | 25 | 26 | 0.96 |

- Each run puts each of the 90 lines into one group. Each share is above 0.60: the step of the procedure stays as it is.
- Each pattern that two or more projects have is a pattern of the three projects on one platform. No group holds a line of the fourth project, which is on a different platform. The patterns that the readers report are close to the mechanism of the platform.
- The readers were three sessions of the smallest model, one run each, started without the gate. The report of the fourth project is the first run of the stage test ST-7.

Predictions: C-1 and the number of groups with two or more projects (8 to 20) were correct. The agent predicted 55 to 75 groups: correct. The agent predicted a share between 0.50 and 0.80; each share is 0.96 or more.
