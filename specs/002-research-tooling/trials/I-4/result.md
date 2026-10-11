# Result of the experiment: the factory at iteration I-4, against the trial of I-3

- Registration: seal a8ef266c6c63, sealed on 2026-10-11, commit (none)
- Valid runs: 1 of 1

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | i4 | 0 | 1 | 0 % | 0 % to 79 % | 0 |
| C-2 | i4 | 0 | 1 | 0 % | 0 % to 79 % | 0 |
| C-3 | i4 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-4 | i4 | 0 | 1 | 0 % | 0 % to 79 % | 0 |
| C-5 | i4 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-6 | i4 | 0 | 1 | 0 % | 0 % to 79 % | 0 |
| C-7 | i4 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-8 | i4 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-9 | i4 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-10 | i4 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-11 | i4 | 0 | 1 | 0 % | 0 % to 79 % | 1 |
| C-12 | i4 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| C-13 | i4 | 0 | 1 | 0 % | 0 % to 79 % | 1 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: With the tooling of iteration I-4 (the research reads each converted source in ranges of the index and records what was read), each page of the guide of the body of knowledge reaches a reader.
- Criterion: C-13
- Confirmed when: `i4 >= 1`
- Refuted when: `i4 <= 0`
- Counts: i4 = 0
- Verdict: refuted

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## Where each failed probe was lost (seen after the run)

These lines give where a term is in the files of the run. They are not a verdict.

| Probe | Stage where it was lost | What the files show |
|---|---|---|
| C-2, a measure of the coverage of the tests | exit to a decision | The register has one requirement for it (R-1026, from a source of the field of testing). Its exit is `3.3: Depth of verification`. No item asks for it. |
| C-4, tests of robustness | calculation | The register has one requirement (R-606). It goes to the item C-19, which names fuzzing with a different kind of test. The calculation put C-19 on level 2. |
| C-6, the concerns of the architecture | boundary | 49 requirements go to `boundary: architecture`. Section 1 gives the architecture to a neighbouring aspect. |
| C-11, an item on level 3 | calculation | No item is on level 3. In the trials I-2 and I-3 one item was. |

Other facts of the run, from the programs:

- The table Reading: each page of the three converted documents was given to a reader (411, 36 and 41 pages; none not read).
- 1202 requirements in the register: 623 go to an item, 336 to a boundary, 117 to a decision, 96 are duplicates, 30 go to an implementation skill.
- The session wrote 9 boundaries. The view `quality` sends 151 of its 303 requirements to a boundary.
- 42 items; 20 on level 1; none on level 3; 3 not admitted.
- 11 of 252 answers of risk and reward name a source. In the trial I-3: 20 of 234.
- 11 stakeholders; 5 views.
- The second reading corrected 13 of 16 rows of the evidence record.
- 17 sources; 4 read in full, 12 in part, 1 not read. 48 reader agents.

Predictions: 12 of 13 were correct. Wrong: C-11 (predicted yes).

The judge marked two answers as judgement calls: C-5 (no item uses the words "automated release") and C-6 (a stakeholder `platform engineers` and a view `delivery` are about the pipeline; a lenient reading gives yes).

## A defect of the instrument for the criterion C-13

The verdict above says "refuted", because the program criterion C-13 gave "no". The cause is the
instrument, not the run: the gate stores a maximum of 100,000 characters of a file, and
`vetting.md` of this run has 207,740 characters. The table Reading is at the end of the file,
after the 1202 rows of the register, so the stored copy does not hold it.

The registered pattern of C-13 matches the full file of the run folder: the row of the guide is
`| S-01 | swebok | 411 | 1-25, 26-42, ... 387-411 | none |`, and `check.py --json` gives
`not read: 0` for each of the three converted documents.

Thus the forbidden result of the hypothesis did not occur. The verdict that the registered limits
give on the stored copy stays in this file as the gate wrote it. The owner decides how this trial
counts.
