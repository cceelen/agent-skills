# Result of the experiment: stage test of the viewpoint integrity in the review of a plan

- Registration: seal 820c39be8d5c, sealed on 2026-10-11, commit (none)
- Valid runs: 3 of 3

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | review | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-2 | review | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-3 | review | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-4 | review | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-5 | review | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-6 | review | 1 | 3 | 33 % | 6 % to 79 % | 2 |
| C-7 | review | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-8 | review | 3 | 3 | 100 % | 44 % to 100 % | 2 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: A reviewer that gets the viewpoint integrity finds, in the plan of the trial I-14, four or more of the five gaps that the agent of the factory found when the owner asked for this view.
- Criterion: C-1
- Confirmed when: `review >= 2`
- Refuted when: `review <= 1`
- Counts: review = 3
- Verdict: confirmed

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## What the files show (seen after the run)

- Each of the three reviews has a finding for the packages of the distributions, for the results that are not kept, for a check that a change can weaken, and for the question of the risk analysis.
- One of three reviews has a finding for the data that the software reads (C-6, predicted 2). Two reviews mark the data as not applicable or name it only inside a different finding.
- Each review has findings that are not of the five, for example: the provenance is not required to name the digest of the archive and the commit; no tag ties a release to a commit; only one of the parts that run with high rights has a check of its hardening.

Limit, as registered: the questions were written after the five gaps were known, on this same plan.
