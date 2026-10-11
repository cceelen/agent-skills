# Charter of the aspect DevSecOps (draft)

**State**: reviewed by the owner on 2026-10-11. The owner confirmed the order of the priorities and the words of the tables, and set the target (see "Target").

The charter is the "why" of the aspect. The session reads it before the triage, and the owner gets it first
in the review. Only the owner changes it. Each scope below the aspect gets it unchanged.

Each line below comes from words of the owner in the session of 2026-10-10 and 2026-10-11. The
quotes have corrected spelling; no other word is changed. The agent proposed the order of the
priorities; the owner confirmed it on 2026-10-11.

## Intent

| Id | Words of the owner | Date |
|---|---|---|
| I-1 | "DevSecOps is about doing shift left of operational, security, and quality concerns." | 2026-10-10 |
| I-2 | "we need to check for covering essential and non negotiable basics of each of those 3 points of views." | 2026-10-10 |
| I-3 | "we need to be able to iterate the spec with the sota research and speckit setup so that we can achieve SLSA draft highest levels" | 2026-10-10 |
| I-4 | "architecture is responsible for the integration of the different stakeholder needs, requirements, regulation, and so on." | 2026-10-11 |

## Target

The owner set the target on 2026-10-11: "the slsa L2 should be a baseline. L3 the goal. beyond
L3 aspirational (e.g. hermetic repeatable build, or in the asus zenbook case the usage of a
build service)."

| Id | Part of the target | Level of the scale | What it is in the triage | Level of the recipe |
|---|---|---|---|---|
| T-1 | baseline | level 2 of each track | a constraint: it is not traded against cost | 1 |
| T-2 | goal | level 3 of each track | the principle P-4 | 2 |
| T-3 | aspiration | above level 3, for example a hermetic and repeatable build, or the use of a build service | recorded, with the risk dimension that calls for it; no project must reach it | 3 |

## Principles

A principle with a lower number wins when two principles disagree.

| Priority | Id | Principle | Words of the owner that it comes from | What it means for the triage | How it is checked |
|---|---|---|---|---|---|
| 1 | P-1 | The concerns of operation, of security and of quality are handled as early in the work as possible. | I-1 | A requirement that moves one of these concerns to an earlier step has the first claim on level 1. "It depends on the context" is not a reason to leave it out. | Each of the three concerns has items on level 1. |
| 2 | P-2 | Each concern has its basic practices, and they are not negotiable. | I-2 | A practice that the field of a concern holds for basic is on level 1, also when its cost is not low. | For each view, the owner sees the basic practices and the level of each. |
| 3 | P-3 | The needs of all stakeholders, the requirements and the rules from outside are brought together in one design. No concern is given away. | I-4 | A requirement leaves the aspect only by a decision of the owner. | No requirement goes to a boundary that the owner did not decide. |
| 4 | P-4 | A project that applies the recipe can reach the goal T-2: level 3 of each track. | I-3; the target of the owner | For level 3 of each track, the recipe has the items that the level needs, on level 2 of the recipe. An item above level 3 is on level 3 of the recipe, not left out. | For each track, the items of T-2 and of T-3 are named. |
| 5 | P-5 | A plan uses a maintained component where one exists. It does not build its own. | "is it reusing existing and maintained pipeline elements / components / actions / steps?" (2026-10-10) | An item is written so that an implementation skill can meet it with a maintained component. | The review of a plan counts maintained components and own constructions. |
| 6 | P-6 | The result can be used again and follows a change of the project. It is not made for one project only. | "Is this a one-off construction or something reusable?", "how will the pipeline be able to adapt to change in the repo / product?" (2026-10-10) | An item that leads to a fixed list or a fixed copy is written again. | The review of a plan names what fails without a message when the project changes. |
| 7 | P-7 | The recipe names the rules of governance that it meets. | "to which governance elements are they complying?" (2026-10-10) | An item names the framework and the unit that it meets, where a source gives one. | Each item has its source unit. |
| 8 | P-8 | The work does not make debt that it does not record. | "Is the skill creating more technical debt?" (2026-10-10) | A cheaper way that leaves a weakness is recorded with the item. | The plan lists the debt that it makes. |

## Constraints

A constraint has no priority. It cannot be traded.

| Id | Constraint | Words of the owner or rule that it comes from |
|---|---|---|
| K-0 | A project that applies the recipe meets the baseline T-1: level 2 of each track of the SLSA draft. Each item that the baseline needs is on level 1 of the recipe. | "the slsa L2 should be a baseline." (2026-10-11) |
| K-1 | The recipe names no product. The choice of a tool is an implementation choice, not a requirement. | "using pre-commit is an implementation choice and not a lack." (2026-10-10); constitution, principle VII |
| K-2 | A skill that the factory creates works alone. | "the created skills have to be able to work standalone." (2026-10-10) |
| K-3 | A skill shows a plan before it changes a project. | "it's ok if the skill delivers a plan. with that we can already anticipate drift" (2026-10-10); constitution, principle VIII |
| K-4 | A statement rests on a source that was read, not on memory. | the rules for evidence before action of the kit |
| K-5 | The framework that gives the factory its method is not a source of this aspect and is not named in a skill of this aspect. | "we should avoid feeding IAF to devsecops skills" (2026-10-11) |

## Scope

- The aspect is DevSecOps, as wide as the owner states it in I-1.
- A boundary is part of the scope only after the owner decided it. No boundary is decided now.

## What is not in this charter, and why

- The points of view from which the owner judges a result, and the single practices that the
  owner named as basic. They are the answer key of the trials: the factory must find them. They
  stay in the registration of each trial, sealed, and in no input of a run.
- P-3 names the role of the architecture. A run that gets this charter as input knows that role,
  so the probe C-6 of the trials I-2 to I-5 is not valid for such a run. It needs a new probe.

## Answers of the owner, 2026-10-11

1. The order of the priorities is correct.
2. Level 2 of the SLSA draft is the baseline, level 3 is the goal, and what is above level 3 is an
   aspiration.
3. The words of the tables are correct.

The agent wrote the column "Level of the recipe" of the table "Target" from answer 2. The owner
did not see that column.
