# Result of the experiment: stage test of the calculation for an item of a basic practice, with and without a collection of maintained templates as a source

- Registration: seal 8339db21049c, sealed on 2026-10-11, commit (none)
- Valid runs: 6 of 6

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | plain | 0 | 3 | 0 % | 0 % to 56 % | 3 |
| C-1 | templates | 0 | 3 | 0 % | 0 % to 56 % | 3 |
| C-2 | plain | 3 | 3 | 100 % | 44 % to 100 % | 0 |
| C-2 | templates | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-3 | plain | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-3 | templates | 3 | 3 | 100 % | 44 % to 100 % | 3 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|
| C-1 | plain, templates | p = 1.0000 |
| C-2 | plain, templates | p = 1.0000 |
| C-3 | plain, templates | p = 1.0000 |

## Verdict

- Hypothesis: A session that answers the questions of risk and reward for the item of the coverage gives the breadth 3 in more runs when the evidence record holds a collection of maintained pipeline templates.
- Criterion: C-1
- Confirmed when: `templates - plain >= 2`
- Refuted when: `templates - plain <= 0`
- Counts: plain = 0, templates = 0
- Verdict: refuted

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## Defect of the instrument

The input holds the identifier C-43 two times: the recorded checklist of the trial I-4 has an item C-43 already, and the agent added the item of the coverage with the same identifier. Each session wrote its answers into the empty row, and the sources that it names are sources of the coverage. The agent reads the rows as answers for the item of the coverage. A reader who does not accept that reads the test as not valid.

## What the six runs show (from the files of the runs; the levels are computed with the formula of `place.py`)

| Arm | Run | Severity | Probability | Breadth | Adopt | Keep | Own risk | Score | Result |
|---|---|---|---|---|---|---|---|---|---|
| plain | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 10 | not admitted |
| plain | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 16 | not admitted |
| plain | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 10 | not admitted |
| templates | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 16 | not admitted |
| templates | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 30 | level 2 |
| templates | 3 | 2 | 2 | 2 | 1 | 2 | 2 | 16 | not admitted |

- The item of the coverage is on level 1 in no run. It is not admitted in five of six runs.
- Each run gives the own risk 2 and names the source that warns of a coverage goal. Each run gives the breadth 2.
- The collection of templates lowers the answer "Adopt" to 1 in three of three runs, against one of three without it. It does not change the breadth or the own risk.
- The item of static analysis (C-24) is on level 1 in each run. The item of the dynamic security tests (C-19) is on level 2 with the dimension of the criticality in each run.
- The words of the item were "measured against a goal that the project sets". The test does not show the result for an item that asks only for the measure.

Predictions: 2 of 6 rows were correct (C-3 in each arm). The agent predicted the breadth 3 and level 1 in each run; no run has them. The agent predicted no source in the arm `plain`; each run names one.
