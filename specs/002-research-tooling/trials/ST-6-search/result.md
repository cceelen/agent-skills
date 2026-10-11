# Result of the experiment: stage test of the search for the maintained projects of an aspect

- Registration: seal c3703801b5ed, sealed on 2026-10-11, commit (none)
- Valid runs: 3 of 3

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | search | 3 | 3 | 100 % | 44 % to 100 % | 3 |
| C-2 | search | 0 | 3 | 0 % | 0 % to 56 % | 3 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: A session that does the step "List what exists" with the rule for the maintained projects lists one project at least that gives reusable components, and one tool at least that examines a project.
- Criterion: C-1
- Confirmed when: `search >= 2`
- Refuted when: `search <= 0`
- Counts: search = 3
- Verdict: confirmed

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## Defect of the instrument

The pattern of C-2 is wrong: `\x7c` in a group is the character and not the alternative, thus C-2 is "no" in each run. The counts below come from the files of the runs. They show 30, 32 and 34 rows of the kinds `standard`, `framework`, `research` and `book`.

## What the three runs show (from the file sources.md of each run)

| Run | Queries | Sources | standard, framework, research, book | vendor, practice | project-components | project-tool |
|---|---|---|---|---|---|---|
| 1 | 44 | 64 | 33 | 13 | 9 | 9 |
| 2 | 39 | 58 | 32 | 12 | 6 | 8 |
| 3 | 50 | 63 | 34 | 15 | 4 | 10 |

- Each run lists projects of the two kinds. The recorded trials I-2 to I-5 list none.
- The collection of pipeline templates that the owner named is in two of three runs. The two tools that examine a pipeline, which the owner named, are in no run.
- The tools that the runs list are scanners and dashboards for metrics. No run lists a tool that examines the pipeline of a project.
- The lists differ between the runs: 4 projects are in each run, of 36 different ones.

Predictions: C-1 was correct. The agent predicted the projects of the owner in one run at most; the collection is in two.
