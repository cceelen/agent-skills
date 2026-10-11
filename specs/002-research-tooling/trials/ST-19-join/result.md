# Result of the experiment: stage test of the answers of risk and reward with the rows of a regulation and of a public recommendation

- Registration: seal 4522509fad35, sealed on 2026-10-11, commit (none)
- Valid runs: 6 of 6

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | old | 0 | 3 | 0 % | 0 % to 56 % | 0 |
| C-1 | join | 3 | 3 | 100 % | 44 % to 100 % | 2 |
| C-2 | old | 0 | 3 | 0 % | 0 % to 56 % | 0 |
| C-2 | join | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-3 | old | 0 | 3 | 0 % | 0 % to 56 % | 0 |
| C-3 | join | 0 | 3 | 0 % | 0 % to 56 % | 3 |
| C-4 | old | 0 | 3 | 0 % | 0 % to 56 % | 0 |
| C-4 | join | 3 | 3 | 100 % | 44 % to 100 % | 2 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|
| C-1 | old, join | p = 0.1000 |
| C-2 | old, join | p = 0.1000 |
| C-3 | old, join | p = 1.0000 |
| C-4 | old, join | p = 0.1000 |

## Verdict

- Hypothesis: A session that gets the requirement rows of one regulation and of one recommendation of a public authority names, for the item of the automated build with tests, a requirement row of such a source that requires or recommends the practice, in more runs than a session without these rows.
- Criterion: C-3
- Confirmed when: `join - old >= 2`
- Refuted when: `join - old <= 0`
- Counts: old = 0, join = 0
- Verdict: refuted

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## What the files show (seen after the run)

- The verdict `refuted` comes from a fault of the instrument, made by the agent of the factory. The criterion C-3 asks the judge for the class of a source in `spec.md`, but no criterion of a judge names that file, thus the packets did not hold it. The judge answered no for each packet of the arm `join` and wrote that the sentence of the named row qualifies and that the class cannot be read. The verdict is not a result about the hypothesis.
- What a program shows for the same question: in each run of the arm `join` the cell Probability of the item C-05 names the row R-2018 of the source S-18 (criterion C-2), and the source S-18 has the class `standard` (criterion C-1). In each run of the arm `old` the cell names the row R-0033, which describes and does not require.
- The sessions gave the class `regulation` to the regulation and the class `standard` to the guidance of the public authority in each of three runs. The prediction 2 was low.
- The item C-27 has the probability 3 with the regulation in each run of the arm `join`, and 2 in each run of the arm `old`.
- The item C-05 (automated build with tests) is not admitted in two runs of the arm `join` and pending in one. Its probability is 2 with a source. Its severity is 2 by judgement in each run, its cost to keep is 3 in two runs (a person corrects a broken build each time), and its own risk is 1. The return is 12, the cost 5 or 4, the score 19 or 25.
- The triage before the test: of 136 requirement lines of the regulation, 2 go to one of the ten items; of 193 lines of the public recommendation, 29 go to six of the ten items. The other lines of the regulation ask for practices that none of the ten items names.
- The program `render.py` computes the mark from the folder of one run of the arm `join`: the item C-27 names the regulation, and no other item has a mark.
- No source of the class `governance` was read. The frameworks that the search found are paid; the search listed commentaries of other parties; two sites of an authority refuse a program.
- The requirement lines of the five readers were not compared with the text of the sources.
