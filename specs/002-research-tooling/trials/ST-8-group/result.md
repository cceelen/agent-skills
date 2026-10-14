# Result of the experiment: stage test of the grouping of the patterns of several reports

- Registration: seal c87be8c53726, sealed on 2026-10-11, commit (none)
- Valid runs: 3 of 3

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | group | 3 | 3 | 100 % | 44 % to 100 % | 3 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: A session that gets the pattern lines of five reports of one sample puts each line into one group.
- Criterion: C-1
- Confirmed when: `group >= 2`
- Refuted when: `group <= 0`
- Counts: group = 3
- Verdict: confirmed

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## The measure of the agreement (program `agreement.py`, written before the runs; the seal does not cover it; its lines were made shorter after the runs, with the same result)

| Runs | Pairs of lines together in the two runs | Pairs together in one run at least | Share |
|---|---|---|---|
| 1 and 2 | 169 | 178 | 0.95 |
| 1 and 3 | 169 | 174 | 0.97 |
| 2 and 3 | 174 | 178 | 0.98 |

- Each run puts each of the 121 lines into one group. The runs write 42, 39 and 40 groups.
- Each share is above 0.60. By the registered decision, the procedure gets this step.
- The lines come from five reports of one file. The test does not show the agreement for the reports of different projects.

Predictions: C-1 was correct. The agent predicted a share between 0.40 and 0.60; each share is 0.95 or more.
