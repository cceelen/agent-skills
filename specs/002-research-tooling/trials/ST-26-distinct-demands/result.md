# Result of the experiment: stage test of the grouping of the requirements of one item into distinct demands

- Registration: seal 99bb254af3a8, sealed on 2026-10-14, commit (none)
- Valid runs: 3 of 3

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | case | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-2 | case | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-3 | case | 0 | 3 | 0 % | 0 % to 56 % | 1 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: A session that groups the requirement rows of one item of the trial I-25 into distinct demands gives the measure of the coverage of the tests a group of its own.
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

A program counted the three tables.

| Run | Groups | Rows in a group | Groups with two or more rows of different sources | Largest group |
|---|---|---|---|---|
| 1 | 92 | 98 of 98, none two times | 2 | 4 rows |
| 2 | 92 | 98 of 98, none two times | 2 | 4 rows |
| 3 | 92 | 98 of 98, none two times | 2 | 4 rows |

- The verdict is `confirmed` by the registered limit, and the grouping gives no gain. The limit asks only for the word in the name of a group. The 98 rows become 92 groups: the grouping joins almost nothing.
- The three groups that name the coverage hold one row each. Each states a special case. No group states "measure the coverage of the tests" as a demand, and no row of the input states it.
- The judge finds no two groups with the same demand. Thus the rows of this item are 92 different demands, not one demand that many sources repeat.
- The agent of the factory wrote the hypothesis too weak. A limit on the number of groups would have forbidden this result.
