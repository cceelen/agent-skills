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

M-08 and M-09 need the answer key of the owner. It does not exist yet.

## Iterations

| Id | Date | Tooling at | What changed | Defect that it answers | Run |
|---|---|---|---|---|---|
| I-0 | 2026-10-10 | `feat/research-tooling` 96033b3 | the first tooling with the rules for evidence | none; the first trial | trial 1, not registered |
| I-1 | 2026-10-10 | `002-research-tooling-tasks` e6ffafd | views and their check; PDF converter; file reader with a hook; start from the bodies of knowledge; search rules | one view only; standards not read | trial 2, not registered |
| I-2 | 2026-10-11 | `002-research-tooling-tasks` ce9320f | plan step in a rendered skill; trial rendering, plan review and trial record; targets; intent of the owner; stakeholders; template without content examples; neutral kit; seeds and reinitialisation; the skill must work alone; `factory/experiment-rigor` | full implementation in place of a plan; biased input; no intent; no stakeholders; no measured target | none yet |

Between I-0 and I-1 several things changed together, and each condition has one run. Thus no
value below shows the effect of one change.

## Values

| Metric | I-0, trial 1 (not registered) | I-1, trial 2 (not registered) | I-2 |
|---|---|---|---|
| M-01 sources read in full | 3 of 23 | 11 of 20 | not run |
| M-02 sources not read | 5 of 23 | 0 of 20, and 3 not reached | not run |
| M-03 answers with a source | 37 of 156 | 14 of 180 | not run |
| M-04 each view has a level 1 item | no views | yes, 6 of 6 views | not run |
| M-05 stakeholders | 0 | 0 | not run |
| M-06 items on level 3 | 0 of 26 | 0 of 30 | not run |
| M-07 searches by known title or one concern only | 8 of 8 (not judged blind) | 10 of 10 (not judged blind) | not run |
| M-08 basics of the owner on level 1 | not measured: no key | not measured: no key | not run |
| M-09 stakeholders and viewpoints of the owner found | not measured: no key | not measured: no key | not run |
| M-10 target levels of the plan | Build 2, Source 1, Dependency 1 (the workflows did not run); reference project: 2, 1, 3 | no plan | not run |
| M-11 maintained components in the plan | 5 maintained, 4 own construction (not judged blind) | no plan | not run |
| M-12 rows corrected by the second reading | "most rows"; not counted | not counted | not run |
| M-13 cost | 3 sessions, 56 reader agents, 28 minutes of research | 2 sessions, 51 reader agents | not run |
| M-14 the skill works alone | not examined | not examined | not run |

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
