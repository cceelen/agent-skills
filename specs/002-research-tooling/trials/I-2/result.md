# Result of the experiment: baseline of the factory at iteration I-2

- Registration: seal 3d6644fd0940, sealed on 2026-10-11, commit (none)
- Valid runs: 1 of 1

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | i2 | 0 | 1 | 0 % | 0 % to 79 % | 0 |
| C-2 | i2 | 0 | 1 | 0 % | 0 % to 79 % | 0 |
| C-3 | i2 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-4 | i2 | 0 | 1 | 0 % | 0 % to 79 % | 0 |
| C-5 | i2 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-6 | i2 | 0 | 1 | 0 % | 0 % to 79 % | 1 |
| C-7 | i2 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-8 | i2 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-9 | i2 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-10 | i2 | 1 | 1 | 100 % | 21 % to 100 % | 0 |
| C-11 | i2 | 1 | 1 | 100 % | 21 % to 100 % | 0 |
| C-12 | i2 | 1 | 1 | 100 % | 21 % to 100 % | 1 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: With the tooling of iteration I-2 and the intent of the owner, the research puts three or more of the four basic practices of the owner on level 1.
- Criterion: C-1
- Confirmed when: `i2 >= 1`
- Refuted when: `i2 <= 0`
- Counts: i2 = 0
- Verdict: refuted

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## Where each failed probe was lost (seen after the run)

These lines give where a term is in the files of the run. They are not a verdict.

| Probe | Stage where it was lost | What the files show |
|---|---|---|
| C-2, a measure of the coverage of the tests | distilling | The word is one time in `evidence.md` and not in the checklist. Section 7 gives no reason. |
| C-4, tests of robustness | before the calculation | Section 7 lists "fuzzing" under "Requirements of the sources that are not checklist items", with the reason "depend on context, belong to a neighbouring aspect, or one source only states them. They were not put through the calculation." |
| C-6, the concerns of the architecture | reading | One file reader got the whole converted guide of 411 pages. Section 7 says that the areas architecture and design were not read. "architecture and design" is a boundary in section 1. |

Other facts of the run, from the programs:

- 14 sources; 4 read in full, 9 in part, 1 not read.
- 20 reader agents: 4 file readers, 9 web readers, 7 second readers.
- 155 of 180 answers of risk and reward are by judgement.
- 10 stakeholders, each in a view; 4 views; 6 targets.
- The view `supply chain` has no item on level 3 and two items that are not admitted, although the target of the owner needs the highest levels.
- The second reading corrected 9 of 13 rows of the evidence record.

Predictions: 9 of 12 were correct. Wrong: C-6 (predicted yes), C-10 and C-11 (predicted no).
