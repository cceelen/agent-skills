# Result of the experiment: stage test of the duplicates after a normalization of the requirements

- Registration: seal 5fbc2279421b, sealed on 2026-10-14, commit (none)
- Valid runs: 3 of 3

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | case | 0 | 3 | 0 % | 0 % to 56 % | 2 |
| C-2 | case | 0 | 3 | 0 % | 0 % to 56 % | 3 |
| C-3 | case | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-4 | case | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-5 | case | 0 | 3 | 0 % | 0 % to 56 % | 2 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: After a session brings the requirement rows of one item of the trial I-25 into a fixed form, a program finds ten or more groups with the same practice and the same object that join rows of two or more sources.
- Criterion: C-1
- Confirmed when: `case >= 2`
- Refuted when: `case <= 0`
- Counts: case = 0
- Verdict: refuted

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## What the files show (seen after the run)

The program of the input wrote these counts into the file groups.md of each run.

| Run | Groups with the same practice and object | Of them with rows of two or more sources | Different practices | Rows with a party that is not the producer |
|---|---|---|---|---|
| 1 | 75 | 3 | 57 | 4 |
| 2 | 53 | 8 | 42 | 0 |
| 3 | 75 | 5 | 49 | 0 |

- The stage test ST-26 found 2 such groups in the same rows, by a grouping of the sentences.
- The judge finds in each run a group whose rows state different demands: for example, a unit test on a release branch and a system test on a packaged artifact both became "run test / software".
- The terms vary between the runs: the same rows become "run test / tests", "run test / software" or "run tests / change".
- In one run, two rows of two sources became one group "track coverage / code".
- The normalization lets a program join more rows than the grouping of the sentences, and the groups that it joins are not the same demand. The verdict is `refuted`: no gain.
- The test program is in `program/group.py.txt`, as it ran, without a change. It is stored as text: it is a record of the instrument, not a program of the repository.
