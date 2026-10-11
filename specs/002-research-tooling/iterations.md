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

The metric that must move in I-3 is M-08, from 2 of 4.

The metrics that must move in I-4 are M-15 and the probe C-6 of the trials.

The metrics that must move in I-5 are the probe C-6 of the trials and M-09.

The metrics that must move in I-6 are M-08, from 2 of 4, and M-06.

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
