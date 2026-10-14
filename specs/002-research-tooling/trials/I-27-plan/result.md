# Result of the experiment: the plan of the rendered skill of the iteration I-27 on a project

- Registration: seal bb168c7c4081, sealed on 2026-10-14, commit (none)
- Valid runs: 1 of 1

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| P-1 | plan | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| P-2 | plan | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| P-3 | plan | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| P-4 | plan | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| P-5 | plan | 1 | 1 | 100 % | 21 % to 100 % | 0 |
| P-6 | plan | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| P-8 | plan | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| P-9 | plan | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| P-10 | plan | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| P-11 | plan | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| P-7 | plan | 1 | 1 | 100 % | 21 % to 100 % | 1 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: The skill that is rendered from a specification with the table "Binding sources" makes a selection that marks one or more items as necessary or as prepared, with the regulation or the governance that asks for it.
- Criterion: P-10
- Confirmed when: `plan >= 1`
- Refuted when: `plan <= 0`
- Counts: plan = 1
- Verdict: confirmed

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## What the files show (seen after the run)

These lines give where a thing is in the files of the run. They are not a verdict.

- The specification is the one of the trial I-25 with the table "Binding sources" of the run 1 of the stage test ST-25. `specification/vetting.md` is that file; the other files are in `trials/I-25/specification`.
- The selection has a table "Regulation and governance" with the columns "Binds the project?", "Binds a user of the product?" and "Prepare for it?". It proposes: the regulation for products binds a user that supplies the product in a commercial activity, not this open project, and the project prepares for it; the directive on liability, the regulation of the financial sector and the governance standard get "no", each with a reason.
- 14 items have the mark `prepared:` with the regulation for products. No item has the mark `necessary:`.
- No item is adopted: each of the 46 lines is a proposal of the session for the owner. In the trial I-25 the selection adopted 42 items without the owner.
- P-1 and the review differ on the coverage: the judge counts the existing workflow for the coverage of the project; the review finds no step of the plan that measures the coverage and no new limit (finding 4).
- The review of the plan has 20 findings: 10 with the route recipe, 6 tooling, 4 implementation skill. It is in `plan-review.md`.
