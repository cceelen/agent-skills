# Iterations of the factory

This file tracks each iteration of the tooling: what changed, which defect it answers, and the
measured values before and after. A value comes from a program or from a judge who does not
know the expected answer. A value from a run that was not registered is marked `not registered`:
it shows a direction only and is not a baseline.

## Metrics

| Id | Question | How it is measured | Better is |
|---|---|---|---|
| M-01 | How many sources were read in full? | `spec.md` section 2, cell Read; counted by a program | higher |
| M-02 | How many sources were not read? | the same; Read `no`, and sources recorded as not reached | lower |
| M-03 | How many answers of risk and reward name a source? | `check.py --json`, key `answers` | higher |
| M-04 | Does each view have an item on level 1? | `check.py --json`, key `views` | yes |
| M-05 | How many stakeholders does the specification name, and how many are in a view? | `check.py --json` | higher; all in a view |
| M-06 | How many items are on the highest level? | `spec.md` section 4; counted by a program | above zero when a target needs them |
| M-07 | How many search queries name the aspect or one of its views by a known title only? | list "Searches" of `vetting.md`; a judge | lower |
| M-08 | How many of the owner's basic practices are on level 1? | the answer key of the owner, sealed before the run; a judge who does not know the key's source | higher |
| M-09 | How many of the owner's stakeholders and viewpoints did the research find? | the same key; a judge | higher |
| M-10 | Which level of each measured target does the plan reach? | `skills/library-vetting/scripts/score.py` on the trial project | higher |
| M-11 | How many parts of the plan use a maintained component, and how many are own construction? | the plan review, with a file and a line for each part | more maintained |
| M-12 | How many rows of the evidence record did the second reading correct? | count of corrected rows; recorded by the session | lower |
| M-13 | What did the run cost? | sessions, reader agents, minutes; from the transcripts | lower |
| M-14 | Does the created skill work alone? | `render.py` check, and a run in a clean environment through `factory/experiment-rigor` | yes |
| M-15 | How many pages of the converted sources did no reader get? | table Reading of vetting.md, written by index.py | lower |

M-08 and M-09 use the answer key in the registration of each trial. The key of `trials/I-2` is a draft from the words of the owner; the owner did not review it.

## Iterations

| Id | Date | Tooling at | What changed | Defect that it answers | Run |
|---|---|---|---|---|---|
| I-0 | 2026-10-10 | `feat/research-tooling` 96033b3 | the first tooling with the rules for evidence | none; the first trial | trial 1, not registered |
| I-1 | 2026-10-10 | `002-research-tooling-tasks` e6ffafd | views and their check; PDF converter; file reader with a hook; start from the bodies of knowledge; search rules | one view only; standards not read | trial 2, not registered |
| I-2 | 2026-10-11 | `002-research-tooling-tasks` ce9320f | plan step in a rendered skill; trial rendering, plan review and trial record; targets; intent of the owner; stakeholders; template without content examples; neutral kit; seeds and reinitialisation; the skill must work alone; `factory/experiment-rigor` | full implementation in place of a plan; biased input; no intent; no stakeholders; no measured target | `trials/I-2`, registered, one run, verdict refuted |
| I-3 | 2026-10-11 | `002-research-tooling-tasks`, this commit | a register of the requirements of the sources in `vetting.md`, with five named exits that the check examines; an item needs a requirement or an own rule; the reader reports each requirement; each source names the views that it was read for, and each view gets the references of its own field | the session dropped requirements of the sources before the calculation by its own judgement; one requirement of the evidence record became no item, with no reason; no source of the own field of one view was read | none yet |
| I-4 | 2026-10-11 | `002-research-tooling-tasks`, this commit | the research reads each converted source in the page ranges of the index, one range for one reader; the index records each range that a reader got; a program writes the table "Reading" into `vetting.md`, and the check examines it; the search, the references and the synonyms of the index are steps of the procedure | a large document was given to one reader; a knowledge area was not read; nobody saw it | none yet |
| I-5 | 2026-10-11 | `002-research-tooling-tasks`, this commit | each boundary of section 1 has a state, proposed or decided by the owner with a date; a requirement goes only to a boundary that the owner decided, and the check examines it; the table "Proposed boundaries" of `vetting.md` names the requirements that each proposed boundary would take; the owner gets the proposed boundaries directly after the intent, the stakeholders and the views | the session sent each requirement of one concern to a boundary that it wrote itself | none yet |
| I-6 | 2026-10-11 | `002-research-tooling-tasks`, this commit | an aspect specification can have a charter of the owner in `charter.md`: the target, the principles with their priority and the constraints; each requirement names the lines of the charter that it serves; the charter places an item before the calculation, and closes the exit to a decision, to a boundary and to "not admitted" for a requirement that serves a line with that effect; the cell "Placed by" of each item names the line that placed it; the check examines it and reports each line of the charter | the triage decides without a reference to what the owner wants: a requirement left through a decision, one was folded and put on level 2 by the calculation | none yet |
| I-7 | 2026-10-11 | `002-research-tooling-tasks`, this commit | the cell "Serves", the cell "Effect" of the charter, the cell "Placed by" and their checks are removed; the charter stays as a file of the owner that the session reads before the triage and that the owner gets first in the review; no program reads it | the stage test ST-1 refuted the cell "Serves": a session ties about 10 of 151 requirements to a line of the charter, and no basic practice | none; stage tests first |
| I-8 | 2026-10-11 | `002-research-tooling-tasks`, this commit | a requirement does not go to a decision of section 3.3: it goes to an item that names its practice, or to a new item; the reader writes each requirement in one fixed line `REQ` with no quotation mark | a requirement of a basic practice left through a decision (trials I-4 and I-5); the reports had seven forms of point 4 and a quotation mark in a quarter of the lines | none; the stage tests ST-2 and ST-3 |
| I-9 | 2026-10-11 | `002-research-tooling-tasks`, this commit | an item names the practice only; a number, a goal or a threshold on which the sources disagree goes to section 3.4 and to a decision of section 3.3 | the calculation did not admit an item that held a goal on which the sources disagree (stage test ST-4) | none; the stage test ST-5, on one item of one aspect |
| I-10 | 2026-10-11 | `002-research-tooling-tasks`, this commit | the step "List what exists" searches also for the maintained projects of the aspect: projects with reusable components, and tools that examine a project; the review gives the owner each item that is not admitted | 58 queries of four trials found no maintained project; the owner did not see an item that the calculation did not admit in a list of its own | none; the stage test ST-6 |
| I-11 | 2026-10-11 | `002-research-tooling-tasks`, this commit | the search covers also the open projects that many other projects depend on; a reader with the task `prompts/sample-reader.md` reports the tools, the integrations, the frameworks and the patterns of a sample in one fixed line each | the research read what the field writes and not what it does | none; the stage test ST-7 |
| I-12 | 2026-10-11 | `002-research-tooling-tasks`, this commit | the index keeps the lines that the readers report: `index.py take` stores the requirement lines and the lines of a sample of one report, and `index.py lines` lists them; the session writes the register from that list; the session puts the pattern lines of the same pattern together | the session wrote the register from its memory of the reports and lost lines: 228 rows of 889 lines in the trial I-5 | none; a replay on eight recorded reports, and the stage test ST-8 for the patterns |
| I-13 | 2026-10-11 | `002-research-tooling-tasks`, this commit | a reader reads the writing of a sampled project also, and reports each principle that the project states with its reason; the session compares the principles with the standards and writes each disagreement into section 3.4; the research uses published statistics and computes none from its samples | the research took what a project does as it is, without the opinion and the reasons of the project | none; the stage test ST-10 |
| I-14 | 2026-10-11 | `002-research-tooling-tasks`, this commit | the session drafts the charter in phase 1 from what the owner says in the session: the target, one sentence for each principle with the words of the owner that it comes from, a proposed order, and a proposed way to check each principle; the owner confirms or corrects the draft before the research | the charter was a file that the owner had to bring; a first form of this change asked the owner to state the principles in three more questions, and the owner corrected it: the skill creates the charter from the interaction | the stage test ST-11; `trials/I-14`, registered, one run, verdict confirmed |
| I-15 | 2026-10-11 | `002-research-tooling-tasks`, this commit | the review of a plan has the viewpoint `integrity`: the reviewer lists the assets, from the source to the system and the data of the user, and answers for each one who can change it without a trace, what shows the change, and if the check is tied to the asset | the seven viewpoints did not find that the chain of evidence of the plan of the trial I-14 ends before the packages that the users install, that no result of a test is kept, that a change can weaken a test, and that the risk analysis does not ask about the system of the user | the stage test ST-12 |
| I-16 | 2026-10-11 | `002-research-tooling-tasks`, this commit | `check.py --index` compares the register of the requirements with the requirement lines of the index: a line without a row, and a row without a line with the same source and words, fail; the session copies the words of a line and does not change them; the records of the trials are not changed for the spelling check | no program compared the register with what the readers reported; the agent of the factory changed three words in two records of trials so that a hook passed | the check on the register of the trial I-14: 1104 of 1105 rows have their line; the words of one row (R-1068) were changed by the session |
| I-17 | 2026-10-11 | `002-research-tooling-tasks`, this commit | `web.py` writes the text of a web source as a converted file in the work folder, in parts of 60 lines as pages; the index and the reader of converted files use it as they use a PDF source; the text is not committed; the procedure asks for it only when a page came back empty or in part, or when its words must be examined | the web tool of a reader returns a summary of a page and not its text: 11 of 16 sources of the trial I-14 were read in this way | the stage test ST-13, refuted: the text gives no more requirement lines than the web tool |
| I-18 | 2026-10-11 | `002-research-tooling-tasks`, this commit | the cost of an item is a count of the elements that a project changes to adopt the item and to keep it, and not an estimate of time (rubric for items, version 2); a source of an answer is a source of the specification, not a context or a view; the check names each item whose severity and probability have no source, as questions for the owner; the rendered checklist marks a level that rests on no source | 437 of 450 answers of the trial I-14 are by judgement; the owner: an estimate of effort from data of the past is flawed since agents write code, and a reference is to the original source | not tested. On the specification of the trial I-14 the check names 73 items without a source for the harm and 56 admitted items without a source for each answer |
| I-19 | 2026-10-11 | `002-research-tooling-tasks`, this commit | the answer `probability` says how strongly regulations and standards ask for the item, and no more how probable the harm is (rubric for items, version 3); the requirement rows of the item give the answer: a regulation or a standard requires (3), recommends, or a specification of a foundation asks (2), none (1) | no source measures how probable a harm is in one project (stage test ST-16); the owner: regulation points at existing issues, and its recommendations are strong indicators | the stage test ST-17, confirmed |

The metric that must move in I-3 is M-08, from 2 of 4.

The metrics that must move in I-4 are M-15 and the probe C-6 of the trials.

The metrics that must move in I-5 are the probe C-6 of the trials and M-09.

The metrics that must move in I-6 are M-08, from 2 of 4, and M-06.

I-7 removes the mechanism of I-6. No metric must move: the change removes what a stage test refuted.

Decision of the owner, 2026-10-11: the change of I-3 stays. The registration of its trial said that it stays only if no metric is lower than in the trial I-2; two values are lower. The owner keeps the register of requirements, because it shows where a requirement is lost.

Between I-0 and I-1 several things changed together, and each condition has one run. Thus no
value below shows the effect of one change.

## Values

| Metric | I-0, trial 1 (not registered) | I-1, trial 2 (not registered) | I-2 | I-3 | I-4 | I-5 | I-6 |
|---|---|---|---|---|---|---|---|
| M-01 sources read in full | 3 of 23 | 11 of 20 | 4 of 14 | 4 of 15 | 4 of 17 | 3 of 14 | not run |
| M-02 sources not read | 5 of 23 | 0 of 20, and 3 not reached | 1 of 14; one guide read in part by one reader | 2 of 15; one guide given to one reader | 1 of 17 | 0 of 14 | not run |
| M-03 answers with a source | 37 of 156 | 14 of 180 | 25 of 180 | 20 of 234 | 11 of 252 | 19 of 234 | not run |
| M-04 each view has a level 1 item | no views | yes, 6 of 6 views | yes, 4 of 4 views | yes, 4 of 4 views | yes, 5 of 5 views | yes, 4 of 4 views | not run |
| M-05 stakeholders | 0 | 0 | 10, each in a view | 8, each in a view | 11, each in a view | 9, each in a view | not run |
| M-06 items on level 3 | 0 of 26 | 0 of 30 | 1 of 30 | 1 of 39 | 0 of 42 | 0 of 39 | not run |
| M-07 searches by known title or one concern only | 8 of 8 (not judged blind) | 10 of 10 (not judged blind) | not judged | not judged | not judged | not judged | not run |
| M-08 basics of the owner on level 1 | not measured: no key | not measured: no key | 2 of 4 (blind judge) | 2 of 4 (blind judge) | 2 of 4 (blind judge) | 2 of 4 (blind judge) | not run |
| M-09 stakeholders and viewpoints of the owner found | not measured: no key | not measured: no key | 4 of 5 (blind judge); architecture not found | 4 of 5 (blind judge); architecture is a boundary | 4 of 5 (blind judge); architecture is a boundary | 4 of 5 (blind judge); architecture is not in the register | not run |
| M-10 target levels of the plan | Build 2, Source 1, Dependency 1 (the workflows did not run); reference project: 2, 1, 3 | no plan | no plan yet | no plan yet | no plan yet | no plan yet | not run |
| M-11 maintained components in the plan | 5 maintained, 4 own construction (not judged blind) | no plan | no plan yet | no plan yet | no plan yet | no plan yet | not run |
| M-12 rows corrected by the second reading | "most rows"; not counted | not counted | 9 of 13 | 7 of 13 | 13 of 16 | not counted here | not run |
| M-13 cost | 3 sessions, 56 reader agents, 28 minutes of research | 2 sessions, 51 reader agents | 2 sessions, 20 reader agents | 2 sessions, 21 reader agents | 2 sessions, 48 reader agents | 2 sessions, 46 reader agents | not run |
| M-14 the skill works alone | not examined | not examined | not examined | not examined | not examined | not examined | not run |
| M-15 pages that no reader got | not measured | not measured | not measured | not measured | 0 of 488 pages | 0 of 488 pages | not run |

## What the values show

- M-01 and M-02 went in the wanted direction from I-0 to I-1.
- M-03 went in the wrong direction: fewer answers name a source.
- M-05 and M-06 did not move.
- M-08 to M-12 have no valid value. They need the key of the owner, a count in the session, or
  a judge.

## Rules

- Each iteration gets a row before its run, with the defect that it answers and the metric
  that must move.
- A run that gives a value for this file goes through `factory/experiment-rigor`.
- One iteration changes one thing, or the row says why not.

## Stage tests

A stage test tries one stage on recorded input of an earlier trial. It has no reader agent.

| Id | Date | Stage | Recorded input | Result | Folder |
|---|---|---|---|---|---|
| ST-1 | 2026-10-11 | the cell Serves of the register (iteration I-6) | 151 requirements of the trial I-4, the charter of DevSecOps | refuted, 3 runs: the row of the coverage and the row of fuzzing serve `none` in each run; 148 of 151 cells are the same in the three runs | `trials/ST-1-serves` |
| ST-2 | 2026-10-11 | the exit of a requirement to a decision of 3.3 | 117 requirements of the trial I-4 that went to a decision, its decisions and its checklist | confirmed, 3 runs: the row of the coverage goes to a new item that names the coverage in each run; each run writes 42 to 46 new items beside the 42 recorded items | `trials/ST-2-exit` |
| ST-3 | 2026-10-11 | the fixed form of a requirement line in the report of a reader | 18 pages of one converted source, the smallest model | confirmed, 5 runs: each of 12 to 17 lines has the form, and no line holds a quotation mark | `trials/ST-3-reader` |
| ST-4 | 2026-10-11 | the calculation of risk and reward for an item of the coverage, with and without a collection of maintained templates as a source | the specification of the trial I-4 with one new item | refuted, 3 runs for each arm: the breadth is 2 and the own risk is 2 in each run; the item is not admitted in five of six runs; the new source lowers only the answer "Adopt"; the input had one identifier two times | `trials/ST-4-place` |
| ST-5 | 2026-10-11 | the words of an item in the calculation of risk and reward | the specification of the trial I-4 with one new item in two wordings | confirmed, 3 runs for each arm: the item that names only the practice is on level 1 in each run; the item with a goal on which the sources disagree is on level 1 in no run; one item of one aspect | `trials/ST-5-words` |
| ST-6 | 2026-10-11 | the search for the maintained projects of an aspect, in the step "List what exists" | the step of the procedure, the aspect and four candidate views; web search | confirmed, 3 runs: each run lists 4 to 9 projects with reusable components and 8 to 10 tools, beside 30 or more standards, frameworks, research sources and books; no run lists a tool that examines a pipeline; the pattern of one criterion was wrong | `trials/ST-6-search` |
| ST-7 | 2026-10-11 | the reader of a sample of the practice | one pipeline template of a public collection, 2238 lines, the smallest model | confirmed, 5 runs: each of 418 lines has the fixed form; 26 of 48 tool names are in each run; no pattern name of 112 is in two runs | `trials/ST-7-sample` |
| ST-8 | 2026-10-11 | the grouping of the patterns of several reports | 121 pattern lines of the five runs of the stage test ST-7 | confirmed, 3 runs: each line is in one group; 42, 39 and 40 groups; the share of the pairs of lines that two runs put together is 0.95 to 0.98; the lines come from one file | `trials/ST-8-group` |
| ST-9 | 2026-10-11 | the grouping of the patterns of different projects | 90 pattern lines of the reports of four projects, one file each | confirmed, 3 runs: 72, 72 and 71 groups; 12 to 13 groups hold lines of two or more projects; the share of the pairs that two runs put together is 0.96 to 1.00; no group joins the project of the second platform with the others | `trials/ST-9-cross` |
| ST-10 | 2026-10-11 | the principles of the sampled projects against a standard, and the patterns across two platforms | 127 pattern lines and 104 principle lines of four projects, and 56 requirements of one standard, from the index | confirmed, 3 runs: each run records the disagreement between the principle of one project and the standard; the patterns of the two platforms are joined in one run of three | `trials/ST-10-principles` |
| ST-11 | 2026-10-11 | the charter that a session drafts in phase 1 from the words of the owner | a neutral kit and 15 statements of the owner in the order in which they were said | confirmed, 3 runs: each charter holds six or more of the seven principles of the charter that the owner reviewed, three rows of the target, and a quote of the owner in each row; the order of the principles differs in each run; no run wrote the choice of a tool as a constraint | `trials/ST-11-charter` |
| ST-12 | 2026-10-11 | the viewpoint `integrity` in the review of a plan | the trial project of the trial I-14 with its plan and its selection | confirmed, 3 runs of the mid-size model: each review finds four or more of the five gaps that the agent of the factory had found; the gap of the data is found in 1 of 3; each review finds also gaps that are not of the five; the questions were written after the five gaps were known | `trials/ST-12-integrity` |
| ST-13 | 2026-10-11 | a reader with the text of a web page against a reader with its web tool | one page of a specification, as a converted file of `web.py` and as an address | refuted, 5 runs of the smallest model for each arm: each run of the two arms reports 25 or more requirement lines (web tool 25 to 39, text 32 to 41); the test does not measure if a line says what the page says | `trials/ST-13-web-text` |
| ST-14 | 2026-10-11 | the requirement lines of a reader against the text of the page | the ten reports of the stage test ST-13 and the converted text of the page | a reading without registration, 4 judges of the mid-size model, each mark with a quote that a program compares with the text: web tool 159 of 159 lines say what the page says, text 172 of 176; the expectation of the agent (the text gives lines that are more true) was wrong; a first pass without the quote was not valid | `trials/ST-14-line-fidelity` |
| ST-15 | 2026-10-11 | the answers of risk and reward from the requirement rows of each item, against the answers from the evidence record | the specification of the trial I-14 with ten items chosen by a program, and their 143 requirement rows | refuted, 3 runs of the largest model for each arm: no run names a source that states a harm for five or more of ten severities (evidence record 1, 1, 1; rows 4, 3, 2); no run names a source for a probability; not registered: the breadth has a source for 9 or 10 of ten items with the rows, and for 4 or 5 without | `trials/ST-15-answer-rows` |
| ST-16 | 2026-10-11 | a search for sources that state harm and frequency, a reader line for such a statement, and the answers of risk and reward with these statements | the ten items of the stage test ST-15; 14 sources of a search without a named report, 11 read, 139 statements | refuted, 3 runs of the largest model for each arm: no run names a source for a probability, with or without the statements; two of ten severities name a statement in each run with them, and the judge finds the scope of the two narrower than the answer; the statements give a share in a group, and the question of the rubric asks for the probability in one project | `trials/ST-16-harm-sources` |
| ST-17 | 2026-10-11 | the answer `probability` from what regulations and standards ask for, against the question how probable the harm is | the ten items of the stage test ST-15 with their 143 requirement rows | confirmed, 3 runs of the largest model for each arm: each run with the new question names, for nine of ten items, a requirement row of a standard or of a foundation that requires or recommends; no run with the old question names a source; nine of ten items have the same number in the three runs; the item of the automated build with tests gets no row of a standard and is on level 1 in no run; the sources hold no regulation | `trials/ST-17-indicator` |
