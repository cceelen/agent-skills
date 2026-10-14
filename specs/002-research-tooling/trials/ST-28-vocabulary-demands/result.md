# Result of the experiment: stage test of the duplicates after a normalization against a vocabulary of practices

- Registration: seal 11052012b44f, sealed on 2026-10-14, commit (none)
- Valid runs: 3 of 3

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | case | 3 | 3 | 100 % | 44 % to 100 % | 1 |
| C-3 | case | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-4 | case | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-5 | case | 1 | 3 | 33 % | 6 % to 79 % | 2 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: After a session writes a vocabulary of the practices of one item of the trial I-25 and brings each requirement row to one term of it, a program finds ten or more terms that join rows of two or more sources.
- Criterion: C-1
- Confirmed when: `case >= 2`
- Refuted when: `case <= 0`
- Counts: case = 3
- Verdict: confirmed

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## What the files show (seen after the run)

The program of the input wrote these counts into the file groups.md of each run. The judge column is the criterion C-5.

| Run | Terms in use | Terms with rows of two or more sources | The rows of one term state one demand (judge) |
|---|---|---|---|
| 1 | 38 | 13 | no |
| 2 | 51 | 10 | yes |
| 3 | 56 | 12 | no |

- The stage test ST-27 used the same rows and the same program with free terms: 3, 8 and 5 terms with rows of two or more sources, and the judge said no in each run.
- In each run, the same two rows of two sources share one term for a measure of the coverage of the tests: "measure test coverage", "measure code coverage" or "track test coverage".
- The judge finds wrong groups in two runs: a general term such as "run tests" joins rows for a release, a commit and a daily run.
- The decision of the registration: the vocabulary is a candidate only if C-5 is yes in two or more runs. It is yes in one. The result is "no gain".
