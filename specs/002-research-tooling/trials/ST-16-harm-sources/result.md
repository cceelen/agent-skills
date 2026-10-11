# Result of the experiment: stage test of the answers of risk and reward with statements of harm and frequency

- Registration: seal 182483048cf0, sealed on 2026-10-11, commit (none)
- Valid runs: 6 of 6

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | evidence | 0 | 3 | 0 % | 0 % to 56 % | 0 |
| C-1 | harm | 0 | 3 | 0 % | 0 % to 56 % | 3 |
| C-2 | evidence | 0 | 3 | 0 % | 0 % to 56 % | 0 |
| C-2 | harm | 0 | 3 | 0 % | 0 % to 56 % | 3 |
| C-3 | evidence | 0 | 3 | 0 % | 0 % to 56 % | 0 |
| C-3 | harm | 0 | 3 | 0 % | 0 % to 56 % | 2 |
| C-4 | evidence | 0 | 3 | 0 % | 0 % to 56 % | 0 |
| C-4 | harm | 3 | 3 | 100 % | 44 % to 100 % | 2 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|
| C-1 | evidence, harm | p = 1.0000 |
| C-2 | evidence, harm | p = 1.0000 |
| C-3 | evidence, harm | p = 1.0000 |
| C-4 | evidence, harm | p = 0.1000 |

## Verdict

- Hypothesis: A session that gets the statements of harm and frequency of sources names, for three or more of ten items, a source for the probability that states how often the harm of the item occurs, in more runs than a session without these statements.
- Criterion: C-3
- Confirmed when: `harm - evidence >= 2`
- Refuted when: `harm - evidence <= 0`
- Counts: evidence = 0, harm = 0
- Verdict: refuted

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## What the files show (seen after the run)

- The search found 14 sources with a task that names no report and no issuer. Eleven were
  read. The readers reported 139 statements: 76 of the kind `frequency`, 63 of the kind `harm`.
- Answers with a source, of ten items, counted by a program in each run:

| Answer | Arm `evidence`, runs 1 to 3 | Arm `harm`, runs 1 to 3 |
|---|---|---|
| Severity | 3, 1, 1 | 2, 2, 2 |
| Probability | 0, 0, 0 | 0, 0, 0 |

- In each run of the arm `harm`, the same two items name a statement for the severity. The
  judge counts the two as statements of a harm of the item, and also as statements whose scope
  is narrower than the answer: one incident of one product, and breaches with stolen
  credentials.
- No session used one of the 76 statements of frequency for a probability. The statements give
  a share or a count in a group: of breaches, of repositories, of packages. The question of
  the rubric asks how probable the harm is in a project that does not have the item. No
  statement gives that.
- Ten of the eleven readers wrote that the web tool returned a summary and not the text of
  the page. Most read only the first page of a report. No second reader compared a statement
  with its source.
- The search named four of the ten items for which it found no source.

Predictions: 4 of 8 were correct. Wrong: the arm `harm` on C-1, C-2, C-3, and on C-4 it was
3 and not 2.
