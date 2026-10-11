# Result of the experiment: stage test of the charter that the session drafts from the words of the owner

- Registration: seal 1bdc2a20136d, sealed on 2026-10-11, commit (none)
- Valid runs: 3 of 3

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | draft | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-2 | draft | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-3 | draft | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-4 | draft | 0 | 3 | 0 % | 0 % to 56 % | 3 |
| C-5 | draft | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-6 | draft | 0 | 3 | 0 % | 0 % to 56 % | 1 |
| C-7 | draft | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-8 | draft | 3 | 3 | 100 % | 44 % to 100 % | 2 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: A session that gets the words of the owner in the order in which they were said, with no sorting, drafts a charter that holds a principle for six or more of the seven principles of the charter that the owner reviewed on 2026-10-11.
- Criterion: C-1
- Confirmed when: `draft >= 2`
- Refuted when: `draft <= 1`
- Counts: draft = 3
- Verdict: confirmed

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## What the files show (seen after the run)

These lines are not a verdict.

- Each run wrote three rows of the target (run 3: four), 8 to 10 principles and 2 or 3 constraints. Each row names a quote of the owner.
- The order of the principles differs in each run. The principle of the architecture has the priority 2 in two runs and 7 in one. The basic practices are the first principle in one run and a constraint in two.
- No run wrote the choice of a tool as a constraint (C-4, predicted 3): each run wrote it as a principle. The charter that the owner reviewed has it as a constraint.
- Each run wrote the statement on the build step and the credentials as a constraint. The charter that the owner reviewed does not have it: the owner said it later.
- Two runs wrote a principle from the statement on the iteration of the specification. That statement is about the factory, not about the aspect.
- The prediction for C-6 (1) and for C-8 (2) was wrong also: 0 and 3.

Limits: one aspect, one set of 15 statements that the agent of the factory selected, three runs. The owner was not in the sessions: no run tests the dialogue itself.
