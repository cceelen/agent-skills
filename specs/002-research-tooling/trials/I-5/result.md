# Result of the experiment: the factory at iteration I-5, against the trial of I-4

- Registration: seal 48dd2f689898, sealed on 2026-10-11, commit (none)
- Valid runs: 1 of 1

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | i5 | 0 | 1 | 0 % | 0 % to 79 % | 0 |
| C-2 | i5 | 0 | 1 | 0 % | 0 % to 79 % | 0 |
| C-3 | i5 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-4 | i5 | 0 | 1 | 0 % | 0 % to 79 % | 0 |
| C-5 | i5 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-6 | i5 | 0 | 1 | 0 % | 0 % to 79 % | 0 |
| C-7 | i5 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-8 | i5 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-9 | i5 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-10 | i5 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-11 | i5 | 0 | 1 | 0 % | 0 % to 79 % | 0 |
| C-12 | i5 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-13 | i5 | 1 | 1 | 100 % | 21 % to 100 % | 1 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: With the tooling of iteration I-5 (a boundary takes a requirement only after the owner decided it), the concerns of the architecture stay in the aspect: section 1 has a stakeholder or a view for them.
- Criterion: C-6
- Confirmed when: `i5 >= 1`
- Refuted when: `i5 <= 0`
- Counts: i5 = 0
- Verdict: refuted

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## Where each failed probe was lost (seen after the run)

These lines give where a term is in the files of the run. They are not a verdict.

| Probe | Stage where it was lost | What the files show |
|---|---|---|
| C-2, a measure of the coverage of the tests | before the register | No row of the register holds the word. In the trial I-4 two rows did. |
| C-4, tests of robustness | exit to a decision | One row (R-143). Its exit is a decision of section 3.3. |
| C-6, the concerns of the architecture | before the register | No row of the register holds the word. In the trial I-4 ten rows did, and 49 requirements went to a boundary of that name. Each page of the guide was given to a reader in the two trials. |
| C-11, an item on level 3 | calculation | No item is on level 3. |

The boundary rule, from the programs:

- No requirement goes to a boundary. In the trial I-4: 336.
- Section 1 has four boundaries, each with the state `(proposed)`. The table "Proposed boundaries" names the 15 requirements that they would take, and no stakeholder that a boundary would leave with no requirement.

Other facts of the run, from the programs:

- 228 requirements in the register: 155 go to an item, 54 to a decision, 15 are duplicates, 4 go to an implementation skill. In the trial I-4: 1202 requirements; in the trial I-3: 668.
- 39 items; 21 on level 1; none on level 3; 4 not admitted.
- 19 of 234 answers of risk and reward name a source.
- 9 stakeholders; 4 views.
- Each page of the three converted documents was given to a reader (411, 36 and 41 pages).
- 14 sources; 3 read in full, 11 in part. 46 reader agents.

Predictions: 13 of 13 were correct, with C-13 answered by the program on the full file.

The judge marked two answers as judgement calls: C-5 (a scripted release build, not an automated publication) and C-10 (no stakeholder has the name "product owner").

The number of requirements in the register differs much between three runs with one run each: 668, 1202, 228. No check compares the register with the requirements that the readers reported. With one run for each iteration, this difference is larger than the effect of a change.
