# Result of the experiment: stage test of the probability answer from what regulations and standards ask for

- Registration: seal e9e385fb57d9, sealed on 2026-10-11, commit (none)
- Valid runs: 6 of 6

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | old | 0 | 3 | 0 % | 0 % to 56 % | 0 |
| C-1 | new | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-2 | old | 0 | 3 | 0 % | 0 % to 56 % | 0 |
| C-2 | new | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-3 | old | 3 | 3 | 100 % | 44 % to 100 % | 0 |
| C-3 | new | 1 | 3 | 33 % | 6 % to 79 % | 1 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|
| C-1 | old, new | p = 0.1000 |
| C-2 | old, new | p = 0.1000 |
| C-3 | old, new | p = 0.4000 |

## Verdict

- Hypothesis: A session that is asked how strongly regulations and standards ask for an item names, for seven or more of ten items, a requirement row of a source of the class `standard` or `foundation` that requires or recommends a practice, in more runs than a session that is asked how probable the harm is.
- Criterion: C-2
- Confirmed when: `new - old >= 2`
- Refuted when: `new - old <= 0`
- Counts: old = 0, new = 3
- Verdict: confirmed

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## What the files show (seen after the run)

- A program read the cell Probability of each run. Arm `old`: no cell names a source in each of the three runs. Arm `new`: 9, 10 and 10 of ten cells name a source.
- Arm `new`: nine of ten items have the same number in the three runs. The item C-21 has 3, 3 and 2.
- The criterion C-3 counts a cell with the number 2 or 3 and the word judgement as a failure. Thus each run of the arm `old` fails it, and the prediction 0 for that arm was wrong. The one run of the arm `new` that fails has the item C-05 by judgement.
- The judge did not count the item C-05 in each run of the arm `new`: its requirement row of a standard describes and does not require or recommend. Its other rows come from sources of the classes `research` and `independent`.
- The placement program gave these levels from the answers. C-08 (provenance): not admitted in each run of the arm `old`, level 1 in each run of the arm `new`. C-31 (separated and hardened environments): not admitted, then level 3. C-05 (automated build with tests): level 1 in one run of the arm `old`; in no run of the arm `new` (pending without a dimension).
- The sources of the specification hold standards and specifications of foundations. No source is a regulation. The test does not show what a session does with the rows of a regulation.
- The judge gave the identifiers of the rows that it counted. A program did not compare them; the agent of the factory read seven of the rows in the input.
