# Experiment: stage test of the scope of a regulation and of a governance source

## 1. Question

- **Quote**: "we kind of need both. we are recommending an order where regulations has raised the items and depending upon the project type we mark them according to the necessity/usecase"
- **Date**: 2026-10-14
- **Decision**: what is done after each outcome.
  - `confirmed`: the table and its rule stay. The specification of one run is rendered, and one trial of the plan on a project shows the marks of the selection.
  - `refuted`: a session does not get the scope of a source from a reader into the table. The owner gets the result as "no gain". No further change to this rule without a decision of the owner.
  - `not decided`: two more runs.

## 2. Hypothesis

- **Statement**: A session that does the part of step 6 for the binding sources of the trial I-25 writes, for the regulation of one sector, that it binds that sector.
- **Forbidden result**: the row of the source S-12 does not name the financial sector, in two or more of three runs.
- **Criterion**: C-2
- **Confirmed when**: `case >= 2`
- **Refuted when**: `case <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does the table "Binding sources" hold four rows? | program | `(?s)## Binding sources.*?(?:\n\x7c S-\d+ \x7c[^\n]*){4}` | file:specs/001-devsecops/vetting.md |
| C-2 | Does the row of the source S-12 name the financial sector? | program | `(?mi)^\x7c S-12 \x7c[^\n]*financial` | file:specs/001-devsecops/vetting.md |
| C-3 | Does the row of the source S-07 name the data of payment cards? | program | `(?mi)^\x7c S-07 \x7c[^\n]*(?:card\|payment)` | file:specs/001-devsecops/vetting.md |
| C-4 | Does the row of the source S-06 name the products with digital elements? | program | `(?mi)^\x7c S-06 \x7c[^\n]*digital elements` | file:specs/001-devsecops/vetting.md |
| C-5 | Does the check pass, and does it name no binding source without a row? | program | `(?s)\A(?!.*without a row in the table 'Binding sources').*No check fails\.` | file:check.out |
| C-6 | Read the table "Binding sources" of the file. Does each of its rows give a location in the source, for example an article, a section or a page? | judge | | file:specs/001-devsecops/vetting.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| case | the only arm: the specification of the trial I-25, the tooling of the iteration I-27, and the work folder of that trial with the converted texts of the four sources | prompts/scope.md | inputs/case |

- **One arm**: the input is the case without the table. The check of the input names the four sources under "What remains".

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Write, Edit, Glob, Grep, Agent, Bash
- **Runs for each arm**: 3
- **Time limit**: 2400
- **Git repository**: yes
- **Fewer than five runs**: a stage test is small on purpose.

## 6. Words of the expected answer

- (none): the prompt names no scope. The titles of two of the four sources in section 2 of the input name their field. The title of the source S-07 names payment cards.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| case | C-1 | 3 |
| case | C-2 | 3 |
| case | C-3 | 3 |
| case | C-4 | 3 |
| case | C-5 | 3 |
| case | C-6 | 3 |

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: sota-file-reader, sota-second-reader, sota-source-reader
- **Work folder**: the three runs use one work folder. A run records in its index which ranges it gave to a reader. The work folder is not an input file of the registration.
