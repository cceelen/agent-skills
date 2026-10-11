# Result of the experiment: stage test of the answers of risk and reward from the requirement rows

- Registration: seal ad9edfc79cd8, sealed on 2026-10-11, commit (none)
- Valid runs: 6 of 6

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | evidence | 0 | 3 | 0 % | 0 % to 56 % | 0 |
| C-1 | lines | 0 | 3 | 0 % | 0 % to 56 % | 2 |
| C-2 | evidence | 0 | 3 | 0 % | 0 % to 56 % | 0 |
| C-2 | lines | 0 | 3 | 0 % | 0 % to 56 % | 2 |
| C-3 | evidence | 0 | 3 | 0 % | 0 % to 56 % | 0 |
| C-3 | lines | 0 | 3 | 0 % | 0 % to 56 % | 0 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|
| C-1 | evidence, lines | p = 1.0000 |
| C-2 | evidence, lines | p = 1.0000 |
| C-3 | evidence, lines | p = 1.0000 |

## Verdict

- Hypothesis: A session that reads the requirement rows of each item names, for five or more of ten items, a source for the severity that states a harm, in more runs than a session that reads only the evidence record.
- Criterion: C-2
- Confirmed when: `lines - evidence >= 2`
- Refuted when: `lines - evidence <= 0`
- Counts: evidence = 0, lines = 0
- Verdict: refuted

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## What the files show (seen after the run)

Answers with a source, of ten items, counted by a program in the table "Items" of each run:

| Answer | Arm `evidence`, runs 1 to 3 | Arm `lines`, runs 1 to 3 |
|---|---|---|
| Severity | 1, 1, 1 | 4, 3, 2 |
| Probability | 0, 0, 0 | 0, 0, 0 |
| Breadth | 5, 5, 4 | 10, 9, 10 |
| Adopt | 10, 9, 8 | 10, 10, 10 |
| Keep | 6, 9, 6 | 10, 9, 9 |
| Own risk | 2, 1, 4 | 2, 4, 1 |

- The judge counted, for the severity, 1, 1 and 1 source that states a harm in the arm
  `evidence`, and 4, 3 and 2 in the arm `lines`. One of these rows is a borderline case.
- No run of the two arms names a source for a probability.
- The sessions of the arm `lines` wrote `(judgement)` where no row states a harm. They did
  not name a row that states only a duty.
- The breadth has a source for almost each item in the arm `lines`. This was not a
  registered criterion. No judge examined if the named rows give the breadth.

Predictions: 4 of 6 were correct. Wrong: the two for the arm `lines` on C-1 and C-2. The limit
of five of ten was a guess without a reading before the registration.
