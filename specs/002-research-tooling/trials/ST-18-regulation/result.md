# Result of the experiment: stage test of the search for the regulation, the governance and the public recommendations of an aspect

- Registration: seal f84fb22a06f3, sealed on 2026-10-11, commit (none)
- Valid runs: 3 of 3

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | search | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-2 | search | 3 | 3 | 100 % | 44 % to 100 % | 2 |
| C-3 | search | 0 | 3 | 0 % | 0 % to 56 % | 2 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: A session that does the step "List what exists" with the rule for the regulation, the governance and the public recommendations lists three or more such sources whose subject is not security.
- Criterion: C-2
- Confirmed when: `search >= 2`
- Refuted when: `search <= 0`
- Counts: search = 3
- Verdict: confirmed

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## What the files show (seen after the run)

- A program counted the rows by kind. Regulation: 6, 7 and 9. Governance: 9, 5 and 6. Public recommendation: 7, 11 and 8. The three recorded runs of the stage test ST-6, without the rule, have one regulation at most and one or two recommendations of a public authority.
- Each run lists the regulation of the European Union for products with digital elements, its regulation for the operational resilience of finance, its directive for the security of networks, the attestation form for suppliers of the government of the United States, and the guidance for medical devices.
- The criterion C-3 is no in each run: each run gives the kind `regulation` to a guidance of an authority, and two runs give it to a summary, a page of questions or a commentary. The prediction 2 was wrong.
- The rows that the judge counted for C-2 are about the operational resilience of finance and about the management of changes. Most of the other rows are about security.
- The lists were not read by a reader. The test does not show what such a source gives to the register.
