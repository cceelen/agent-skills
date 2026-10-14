# Result of the experiment: stage test of the ladder in the hands of a session

- Registration: seal b1065a7b528d, sealed on 2026-10-12, commit (none)
- Valid runs: 3 of 3

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | case | 3 | 3 | 100 % | 44 % to 100 % | 1 |
| C-2 | case | 3 | 3 | 100 % | 44 % to 100 % | 1 |
| C-3 | case | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-4 | case | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-5 | case | 0 | 3 | 0 % | 0 % to 56 % | 0 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: A session that does the part "The value and the level of an item" on a specification with two sources without a class places the item that a regulation asks for from that regulation.
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

- The prediction 1 for the criteria C-1 and C-2 was wrong: each session gave the two sources a class, although the program named no pending item.
- A program compared the rows of the ten items in the three runs: the level and the strongest source of each item are the same in each run.
- Nine of ten items are on level 1: the level limit of the ladder puts the classes `regulation` and `standard` on one level. The value orders them inside the level.
- The input has ten items. The test does not show the ladder on a complete checklist.
