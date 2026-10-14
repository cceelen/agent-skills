# Result of the experiment: the research of the factory at iteration I-23

- Registration: seal 9f0a9ea19af9, sealed on 2026-10-12, commit (none)
- Valid runs: 1 of 1

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| K-1 | i23 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| K-2 | i23 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| K-3 | i23 | 0 | 1 | 0 % | 0 % to 79 % | 0 |
| K-4 | i23 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| L-1 | i23 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| L-2 | i23 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| L-3 | i23 | 0 | 1 | 0 % | 0 % to 79 % | 1 |
| L-4 | i23 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| L-5 | i23 | 0 | 1 | 0 % | 0 % to 79 % | 0 |
| B-1 | i23 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| B-2 | i23 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| B-3 | i23 | 0 | 1 | 0 % | 0 % to 79 % | 1 |
| B-4 | i23 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| B-5 | i23 | 1 | 1 | 100 % | 21 % to 100 % | 1 |
| B-6 | i23 | 0 | 1 | 0 % | 0 % to 79 % | 1 |
| B-8 | i23 | 1 | 1 | 100 % | 21 % to 100 % | 1 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|

## Verdict

- Hypothesis: With the tooling of iteration I-23, the research takes one or more public data services, which tools of the aspect read their data from, as a source of the specification.
- Criterion: K-1
- Confirmed when: `i23 >= 1`
- Refuted when: `i23 <= 0`
- Counts: i23 = 1
- Verdict: confirmed

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## What the files show (seen after the run)

These lines give where a thing is in the files of the run. They are not a verdict.

Generic measures, from the programs:

- The check passes with the index. The table of the requirements has 2044 rows: 1948 go to an item, 94 to an implementation skill, 2 are a duplicate, none goes to a boundary.
- 36 sources: 12 of a foundation, 8 standards, 5 of research, 5 of a vendor, 4 independent, 1 regulation, 1 governance. No source has the class `trusted-data`. The data service of the criterion K-1 has the class `vendor`.
- 53 queries, of them 13 of the catalogues. Section 7 says that the samples S-29 to S-34 came from the catalogues and from the searches, and that catalogue candidates for products were not given to a reader.
- 52 items: 36 on level 1 and 16 on level 2, none on level 3, none pending. The strongest source: a standard for 36 items, a foundation for 14, a vendor for 2.
- One session of 46 minutes. The work folder holds the reports of the readers for 36 sources.

The ladder:

- L-3, predicted yes, is no. The regulation and the governance source are in section 2 with their classes, and neither gave a requirement row. The pages of the regulation came back empty to the reader and to the two converters. The governance source is paid; only the page of its issuer was read.
- The body of knowledge has the class `research` in this run. In the trial I-14 it had the class `standard`.
- The item C-08 (the build, the test and the packaging run as separate steps with separate privileges) is on level 2: only sources of a foundation ask for it. The field "Intent of the owner" names this as not wanted. The ladder does not read the charter.

The probe of the basic practices:

- B-3: the item C-39 for the measures of the tests is on level 2; a source of a foundation is its strongest source. Eight requirement rows name the coverage; five go to that item.
- B-6: no item names tests of robustness. Five requirement rows name them; four go to the item C-14 (static analysis and security tests run on each change).
