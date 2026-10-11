# Result of the experiment: stage test of the patterns across platforms and of the principles against a standard

- Registration: seal 18f580f9e780, sealed on 2026-10-11, commit (none)
- Valid runs: 3 of 3

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | compare | 3 | 3 | 100 % | 44 % to 100 % | 2 |
| C-2 | compare | 3 | 3 | 100 % | 44 % to 100 % | 2 |
| C-3 | compare | 1 | 3 | 33 % | 6 % to 79 % | 3 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: A session that gets the principles of the projects and the requirements of a standard records the disagreement on the use of the newest version of a tool against a fixed version.
- Criterion: C-1
- Confirmed when: `compare >= 2`
- Refuted when: `compare <= 0`
- Counts: compare = 3
- Verdict: confirmed

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## What the three runs show (from the files of the runs)

| Run | Groups of patterns | With lines of two or more projects | That join the project S-18 with a project of the other platform | Rows of disagreements |
|---|---|---|---|---|
| 1 | 107 | 13 | 0 | 4 |
| 2 | 108 | 12 | 0 | 4 |
| 3 | 106 | 14 | 2 | 7 |

- Each run records the disagreement between the principle of one project to use the newest version of its analysis tools and the requirements of the standard to pin by hash. The prompt names no topic.
- The rows of run 1: the versions of the tool images; how pinned dependencies are updated; vulnerabilities that have no fix; tests on changes in early development.
- The new rule for the name of a pattern did not join the patterns of the two platforms: two groups in one run, none in two runs.

## Before the runs (the readers were started without the gate)

- Nine reports of the smallest model: eight for the files and the writing of four projects, one for the standard.
- The index refused each line of a principle with six cells: 10 lines of one report and 75 lines of one report. After the form of a principle line was added to the task, three more reports of one page had 7 of 61, 6 of 54 and 0 of 57 lines without the form.

## Difference between the sealed registration and the file in the repository

The quote of the owner in the sealed registration has one word with the spelling of the owner. The file in the repository has the corrected spelling of that word, because the check of the spelling of the repository refuses the other form. No other character differs.

Predictions: C-1 and C-2 as a verdict were correct (predicted 2, counted 3). The agent predicted C-3 in three runs; it is in one. The agent predicted 5 to 20 rows of disagreements; two runs have 4.
