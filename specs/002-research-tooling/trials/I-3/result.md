# Result of the experiment: the factory at iteration I-3, against the baseline of I-2

- Registration: seal 38550c3bf111, sealed on 2026-10-11, commit (none)
- Valid runs: 1 of 1

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | i3 | 0 | 1 | 0 % | 0 % to 79 % | 1 |
| C-2 | i3 | 0 | 1 | 0 % | 0 % to 79 % | 1 |
| C-3 | i3 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-4 | i3 | 0 | 1 | 0 % | 0 % to 79 % | 0 |
| C-5 | i3 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-6 | i3 | 0 | 1 | 0 % | 0 % to 79 % | 0 |
| C-7 | i3 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-8 | i3 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-9 | i3 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-10 | i3 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-11 | i3 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-12 | i3 | 1 | 1 | 100 % | 21 % to 100 % | 1 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: With the tooling of iteration I-3 (each requirement of a source goes through the calculation; each view reads sources of its own field) and the intent of the owner, the research puts three or more of the four basic practices of the owner on level 1.
- Criterion: C-1
- Confirmed when: `i3 >= 1`
- Refuted when: `i3 <= 0`
- Counts: i3 = 0
- Verdict: refuted

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## Where each failed probe was lost (seen after the run)

These lines give where a term is in the files of the run and in the index of the converted guide. They are not a verdict.

| Probe | Stage where it was lost | What the files show |
|---|---|---|
| C-2, a measure of the coverage of the tests | reading | The register has no requirement that asks for a measure of the coverage. Two rows hold the word for a different thing (R-219, R-556). The index finds the subject on the pages 120 to 145 of the guide, in the area of testing. One file reader got the whole guide, with no range of pages. |
| C-4, tests of robustness | reading, then a decision | The register has no row for it. It is an option of the decision "Which security tests to run" in section 3.3. The index finds the subject on the pages 128, 131, 145 and 268 of the guide. |
| C-6, the concerns of the architecture | boundary | The pages of the architecture were read in this run. Eight or more requirements are in the register (for example R-005 to R-010, R-030, R-098). Each goes to `boundary: architecture`. |

Other facts of the run, from the programs:

- 668 requirements in the register: 451 go to an item, 118 to a boundary, 76 to a decision, 23 to an implementation skill.
- 39 items; 25 on level 1; 1 on level 3.
- Each view has 3 or 4 sources that were read for it. In the trial I-2 each view had 0.
- 20 of 234 answers of risk and reward name a source. In the trial I-2: 25 of 180.
- 8 stakeholders. In the trial I-2: 10.
- The second reading corrected 7 of 13 rows of the evidence record.
- 15 sources; 4 read in full, 9 in part, 2 not read. 21 reader agents.

Predictions: 10 of 12 were correct. Wrong: C-1 and C-2 (predicted yes).

The judge marked two answers as judgement calls: C-5 (no item uses the words "automated release") and C-10 (no stakeholder has the name "product owner"; the judge counted `consumers` and `management`).

The registered decision for this outcome: the next iteration changes the stage where the probes were lost, and nothing else; the change of I-3 stays only if no metric is lower than in the trial I-2. Two values are lower: the answers with a source, and the number of stakeholders.
