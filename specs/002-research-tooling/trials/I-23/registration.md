# Experiment: the research of the factory at iteration I-23

## 1. Question

- **Quote**: "do ST-20 again with the valid verdict. start 22 and 23"
- **Date**: 2026-10-12
- **Decision**: what is done after each outcome.
  - `confirmed`: the changes of I-22 and I-23 stay. The specification of this run is rendered, and a trial of the plan on a project follows. The owner judges that plan in a walk.
  - `refuted`: the list of the searches of the run shows where the candidates of the catalogues were lost. The owner gets that list. The trial of the plan follows also.
  - `not decided`: the run is done again after the cause that made it not valid is corrected.

## 2. Hypothesis

- **Statement**: With the tooling of iteration I-23, the research takes one or more public data services, which tools of the aspect read their data from, as a source of the specification.
- **Forbidden result**: section 2 of the specification names no such data service.
- **Criterion**: K-1
- **Confirmed when**: `i23 >= 1`
- **Refuted when**: `i23 <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| K-1 | Does the table of the sources name one or more public data services that tools read their data from, for example a public database? A standard, a framework, a tool, a book and a report are not a data service. | judge | | file:specs/001-devsecops/spec.md |
| K-2 | Does the list of the searches hold a query of the catalogues? | program | `(?mi)^- [^\n]*catalogues:` | file:specs/001-devsecops/vetting.md |
| K-3 | Does the specification name the organization or the data service that the owner named? | program | `(?i)aboutcode\|vulnerablecode` | file:specs/001-devsecops/spec.md |
| K-4 | Does the table of the sources name a source of the class `regulation` or `governance`? | program | `(?m)^\x7c S-\d+ \x7c[^\n]*\x7c\s*(?:regulation\|governance)\s*\x7c` | file:specs/001-devsecops/spec.md |
| L-1 | Has no row of the checklist the word pending in its cell Level? | program | `(?s)\A(?!.*\n\x7c C-\d+ \x7c[^\n]*\x7c\s*pending\s*\x7c).*\n\x7c C-\d+ \x7c` | file:specs/001-devsecops/spec.md |
| L-2 | Has the checklist one or more items on level 2 or on level 3? | program | `(?m)^\x7c C-\d+ \x7c(?:[^\x7c\n]*\x7c){3}\s*[23]\b` | file:specs/001-devsecops/spec.md |
| L-3 | Has the checklist one or more items whose strongest source is a regulation or a source of governance? | program | `(?m)^\x7c C-\d+ \x7c(?:[^\x7c\n]*\x7c){4}\s*(?:regulation\|governance) \(` | file:specs/001-devsecops/spec.md |
| L-4 | Does the final report give the checklist in an order, with the level and the strongest source of each item, and the values of the ladder? | judge | | final |
| L-5 | Does the final report state, as a judgement of its writer, how severe, how probable or how costly something is for a checklist item? | judge | | final |
| B-1 | Does the checklist have an item on level 1 that asks that the tests run for each change? | judge | | file:specs/001-devsecops/spec.md |
| B-2 | Does the checklist have an item on level 1 that asks that a build or a test that fails stops the change? | judge | | file:specs/001-devsecops/spec.md |
| B-3 | Does the checklist have an item on level 1 that asks for a measure of the coverage of the tests? | judge | | file:specs/001-devsecops/spec.md |
| B-4 | Does the checklist have an item on level 1 that asks for static analysis of the code? | judge | | file:specs/001-devsecops/spec.md |
| B-5 | Does the checklist have an item on level 1 that asks for a scan of the dependencies for known vulnerabilities? | judge | | file:specs/001-devsecops/spec.md |
| B-6 | Does the checklist have an item, on any level, that asks for tests of robustness, for example fuzzing, for parts that read input that is not trusted? | judge | | file:specs/001-devsecops/spec.md |
| B-8 | Does the table Reading of the run have a row for the guide of 411 pages with no page that was not read? | program | `swebok \W 411 \W[^\n]*\W none \W` | file:specs/001-devsecops/vetting.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| i23 | the only arm: the tooling of iteration I-23, the result of phase 1 of the trial I-14 in the template of this iteration, and a work folder with the seed and the eight catalogues | prompts/p2.md | inputs/kit |

- **One arm**: the comparison is the registered run of the trial I-14. The input differs from that run in the tooling of the iterations I-15 to I-23. The criteria K-1 to K-4 and L-1 to L-5 are new. The criteria B-1 to B-6 and B-8 are those of that trial.

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Write, Edit, Glob, Grep, Agent, WebSearch, WebFetch, Bash
- **Runs for each arm**: 1
- **Time limit**: 9000
- **Git repository**: yes
- **Fewer than five runs**: one run starts about fifty reader agents and takes more than one hour of the large model. One run gives no interval. The stage tests ST-20 and ST-21 measured the two changed steps with three runs each.

## 6. Words of the expected answer

- `coverage`
- `static analysis`
- `fuzz`
- `aboutcode`
- `vulnerablecode`

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| i23 | K-1 | 1 |
| i23 | K-2 | 1 |
| i23 | K-3 | 0 |
| i23 | K-4 | 1 |
| i23 | L-1 | 1 |
| i23 | L-2 | 1 |
| i23 | L-3 | 1 |
| i23 | L-4 | 1 |
| i23 | L-5 | 0 |
| i23 | B-1 | 1 |
| i23 | B-2 | 1 |
| i23 | B-3 | 1 |
| i23 | B-4 | 1 |
| i23 | B-5 | 1 |
| i23 | B-6 | 1 |
| i23 | B-8 | 1 |

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: sota-file-reader, sota-second-reader, sota-source-reader
- **Change of the kit**: the file `skills/library-vetting/scripts/collect.py` is removed from the input folder, because it holds words of the expected answer. Without it, the vetting of a source that is a repository records an error.
- **Work folder**: the catalogues in the work folder hold the name of the data service that the owner named, as data of one catalogue. The work folder is not an input file of the registration.
- **Ladder**: the values and the level limits of the ladder are a draft of the agent of the factory. The owner did not confirm them.
