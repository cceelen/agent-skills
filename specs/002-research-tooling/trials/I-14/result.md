# Result of the experiment: the research of the factory at iteration I-14

- Registration: seal ee1a540eff12, sealed on 2026-10-11, commit (none)
- Valid runs: 1 of 1

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| G-1 | i14 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| G-2 | i14 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| G-3 | i14 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| G-4 | i14 | 0 | 1 | 0 % | 0 % to 79 % | 1 |
| G-5 | i14 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| G-6 | i14 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| G-7 | i14 | 1 | 1 | 100 % | 21 % to 100 % | 0 |
| G-8 | i14 | 0 | 1 | 0 % | 0 % to 79 % | 0 |
| B-1 | i14 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| B-2 | i14 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| B-3 | i14 | 0 | 1 | 0 % | 0 % to 79 % | 1 |
| B-4 | i14 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| B-5 | i14 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| B-6 | i14 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| B-7 | i14 | 1 | 1 | 100 % | 21 % to 100 % | 0 |
| B-8 | i14 | 1 | 1 | 100 % | 21 % to 100 % | 1 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: With the tooling of iteration I-14, the research takes one or more maintained projects with components that other projects use again as a source of the specification.
- Criterion: G-1
- Confirmed when: `i14 >= 1`
- Refuted when: `i14 <= 0`
- Counts: i14 = 1
- Verdict: confirmed

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## What the files show (seen after the run)

These lines give where a thing is in the files of the run. They are not a verdict.

Generic measures, from the programs:

- The index holds 1105 requirement lines of 14 sources. The table of the requirements has 1105 rows. In the trial I-5: 228 rows of 889 lines.
- Where the requirements go: 1089 to an item, 15 to an implementation skill, 1 duplicate, none to a boundary, none to a decision of section 3.3.
- 73 items: 29 on level 1, 34 on level 2, 6 on level 3, 6 not admitted. Each view has an item on level 1.
- 659 of the 1105 lines come from the body of knowledge. Ten boundaries are proposed; they would take 431 requirements. The session wrote ten items (C-68 to C-77) to give these requirements an exit.
- 13 of 450 answers of risk and reward name a source.
- 16 sources: 3 read in full, 11 in part, 2 not read (paid standards). Three sources are samples of projects, all for the provenance of a build. The index holds 79 lines of samples: 24 tools, 12 integrations, 13 frameworks, 10 patterns, 20 principles.
- 18 search queries. Two ask for statistics; no source of statistics was read (G-4, predicted yes).
- One session of 33 minutes, 53 reports of readers.

The probe of the basic practices:

- B-3, a measure of the coverage of the tests: the session drafted an item and removed it, because no requirement line of a reader held the practice (section 7 of the specification). Two lines of the index hold the word; the two are about the analysis tools and go to the item of the static analysis.
- B-6: the item for tests of robustness is on level 2.

The charter:

- The final report gives two cases in which the order of the principles decided, each as a question for the owner (G-7, predicted no).
- The session reports that the pages of the build track that the readers read do not hold the rule of the constraint K-2, and asks the owner for the place.

Predictions: 12 of 16 were correct. Wrong: G-4, G-7, B-3, B-7.

Limits: one run. The readers ran as new sessions of the agent product, not as sub-agents: the session wrote this into section 7. The web tool of a reader returns a summary of a page.

The copy of `vetting.md` in this folder differs from the file of the run in two words of rows 735 and 766: the spelling check of the repository refused them.
