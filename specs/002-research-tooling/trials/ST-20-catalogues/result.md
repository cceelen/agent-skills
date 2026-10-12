# Result of the experiment: stage test of the search step with the catalogues and the queries without a known name

- Registration: seal 93cafee34aff, sealed on 2026-10-12, commit (none)
- Valid runs: 3 of 3

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | search | 0 | 3 | 0 % | 0 % to 56 % | 2 |
| C-2 | search | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-3 | search | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-4 | search | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-5 | search | 3 | 3 | 100 % | 44 % to 100 % | 2 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: A session that does the step "List what exists" with the catalogues and with the rule for queries without a known name lists the organization or the data service that the owner named.
- Criterion: C-1
- Confirmed when: `search >= 2`
- Refuted when: `search <= 0`
- Counts: search = 0
- Verdict: refuted

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## What the files show (seen after the run)

- The verdict `refuted` comes from a fault of the instrument, made by the agent of the factory. The pattern of the criterion C-1 holds `\x7c` between the two names. In a pattern that is a bar as a character, not a choice between two names, thus the pattern finds only the two names with a bar between them. The agent tried the pattern with a bar before the seal, not the pattern of the registration. The verdict is not a result about the hypothesis.
- What a program shows for the same question, with a choice between the two names: each of the three lists names the data service. Run 1 has two rows for it, one found by the search and one by the catalogue of a fund. Run 2 and run 3 have one row each, found by a catalogue. The name of the organization is in the title of one row of run 1 and in the address of a row of run 1 and of run 3.
- None of the six recorded runs of the stage tests ST-6 and ST-18 names one of the two.
- Queries: 71, 132 and 122 rows, of them 28, 80 and 78 of the catalogues. Sources: 122, 114 and 126 rows, of them 29, 30 and 48 found by a catalogue, and 10, 6 and 6 of the kind `data-service`.
- No source was read by a reader. The test does not show if a candidate of a catalogue is a good source.
