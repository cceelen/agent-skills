# Result of the experiment: stage test of the search step with the catalogues, done again with a corrected pattern

- Registration: seal 596d6c7b59a2, sealed on 2026-10-12, commit (none)
- Valid runs: 3 of 3

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | search | 2 | 3 | 67 % | 21 % to 94 % | 3 |
| C-2 | search | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-3 | search | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-4 | search | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-5 | search | 3 | 3 | 100 % | 44 % to 100 % | 3 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: A session that does the step "List what exists" with the catalogues and with the rule for queries without a known name lists the organization or the data service that the owner named.
- Criterion: C-1
- Confirmed when: `search >= 2`
- Refuted when: `search <= 0`
- Counts: search = 2
- Verdict: confirmed

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## What the files show (seen after the run)

- The prediction 3 for the criterion C-1 was high: one run names neither of the two.
- Where the two runs found the data service: each has a row from the search, and one of them has also a row from the catalogue of a fund. In the three runs of the stage test ST-20, three rows come from a catalogue and one from the search.
- The six runs of the two tests together: five lists name the data service; four have a row for it from a catalogue, and three a row from the search. None of the six recorded runs of the old step names it.
- Queries: 85, 86 and 87 rows, of them 23, 27 and 36 of the catalogues. Sources: 99, 90 and 99 rows, of them 17, 26 and 23 found by a catalogue, and 7, 6 and 7 of the kind `data-service`.
- No source was read by a reader.
