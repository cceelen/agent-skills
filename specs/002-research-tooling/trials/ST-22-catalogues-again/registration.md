# Experiment: stage test of the search step with the catalogues, done again with a corrected pattern

## 1. Question

- **Quote**: "https://aboutcode.org/ is a common page and financed by the EU same as https://public.vulnerablecode.io/ ... i hope these showed up in the research"
- **Date**: 2026-10-12
- **Decision**: what is done after each outcome.
  - `confirmed`: the row I-23 of the iterations gets this test as its test. The step stays as it is.
  - `refuted`: the step with the catalogues does not bring such a project into the list of a session. The owner gets the result as "no gain". No further change to this step without a decision of the owner.
  - `not decided`: two more runs.

## 2. Hypothesis

- **Statement**: A session that does the step "List what exists" with the catalogues and with the rule for queries without a known name lists the organization or the data service that the owner named.
- **Forbidden result**: the list names neither of the two, in two or more of three runs.
- **Criterion**: C-1
- **Confirmed when**: `search >= 2`
- **Refuted when**: `search <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does the file name the organization or the data service that the owner named? | program | `(?i)aboutcode\|vulnerablecode` | file:sources.md |
| C-2 | Does the table Searches hold a query of the catalogues? | program | `(?mi)^\x7c[^\x7c\n]*catalogues:` | file:sources.md |
| C-3 | Does the table Sources hold a row that was found by a catalogue? | program | `(?mi)\x7c\s*catalogue\s*\x7c\s*$` | file:sources.md |
| C-4 | Does the table Sources hold a row of the kind `data-service`? | program | `\x7c\s*data-service\s*\x7c` | file:sources.md |
| C-5 | Read the table Searches of this file. Leave out the rows that start with the word catalogues. For each of the views operation, security, quality and delivery: is there a row of that view whose query holds no name of a document, of a standard, of a project, of an organization or of a product? Answer yes only if each of the four views has such a row. | judge | | file:sources.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| search | the only arm: the step "List what exists" of the procedure as it is after the iteration I-23, with the programs and a work folder that holds the eight catalogues | prompts/search.md | inputs/case |

- **Done again**: the stage test ST-20 had the same prompt, the same input and the same criteria. The pattern of its criterion C-1 held a bar as a character, thus its verdict is not valid. Only that pattern is changed here.
- **One arm**: the six recorded runs of the stage tests ST-6 and ST-18 show the step without the catalogues and without the rule. A program searched their lists before this registration: none of the six names one of the two.

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Write, Bash, WebSearch, WebFetch
- **Runs for each arm**: 3
- **Time limit**: 2400
- **Git repository**: no
- **Fewer than five runs**: a stage test is small on purpose.

## 6. Words of the expected answer

- (none): the prompt and the step name no organization and no service. The name of the data service is in one input file, the catalogue of one fund in the work folder, as data of that catalogue: the test examines if a session finds it there. The name of the organization is in no input file. The agent of the factory saw the three lists of the stage test ST-20 before this registration; the predictions come from them.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| search | C-1 | 3 |
| search | C-2 | 3 |
| search | C-3 | 3 |
| search | C-4 | 3 |
| search | C-5 | 3 |

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
