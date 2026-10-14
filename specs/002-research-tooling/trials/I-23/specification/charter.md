# Charter: DevSecOps

**State**: draft

The charter is the "why" of the aspect: the target, the principles with their priority and the
constraints of the owner. The session reads it before the triage, and the owner gets it first
in the review. Only the owner changes it. The file is `charter.md`, beside `spec.md`.

Write the state in one of these forms: `draft`, or `reviewed by the owner on <YYYY-MM-DD>`.
Write the words of the owner, with the date, into the cell "Comes from" of each row. Do not
write a row that has no words of the owner.

## Target

What a project reaches when it applies the recipe. One row for each part of the target.

| Id | Part of the target | Level of the scale | Comes from |
|---|---|---|---|
| T-1 | The baseline that each project reaches. | SLSA L2 | "the slsa L2 should be a baseline. L3 the goal. beyond L3 aspirational (e.g. hermetic repeatable build, or in the asus zenbook case the usage of a build service)." (2026-10-11) |
| T-2 | The goal that the recipe leads a project to. | SLSA L3 | "the slsa L2 should be a baseline. L3 the goal. beyond L3 aspirational (e.g. hermetic repeatable build, or in the asus zenbook case the usage of a build service)." (2026-10-11) |
| T-3 | The aspiration, which is not a duty. | Beyond SLSA L3 | "the slsa L2 should be a baseline. L3 the goal. beyond L3 aspirational (e.g. hermetic repeatable build, or in the asus zenbook case the usage of a build service)." (2026-10-11); "we need to be able to iterate the spec with the sota research and speckit setup so that we can achieve SLSA draft highest levels" (2026-10-10) |

## Principles

A principle with a lower number wins when two principles disagree.

| Priority | Id | Principle | Comes from | How it is checked |
|---|---|---|---|---|
| 1 | P-1 | The recipe brings the operational, the security and the quality concerns to the start of the work. | "DevSecOps is about doing shift left of operational, security, and quality concerns." (2026-10-10) | The owner looks at the checks of the checklist items: each check can run before the delivery. |
| 2 | P-2 | The architecture integrates the needs of the stakeholders, the requirements and the regulation. | "architecture is responsible for the integration of the different stakeholder needs, requirements, regulation, and so on." (2026-10-11) | The owner looks at the stakeholders and the views of section 1, and at section 3.4: each disagreement has one answer of the recipe. |
| 3 | P-3 | The recipe tells to which governance elements each practice complies. | "to which governance elements are they complying?" (2026-10-10) | The owner looks at the cell "Source" of each checklist item: it names the unit of a source. |
| 4 | P-4 | The recipe uses pipeline components that exist and are maintained, before it builds a new one. | "is it reusing existing and maintained pipeline elements / components / actions / steps?" (2026-10-10) | The owner looks at the plan of a trial: each step names a maintained component, or says why none is used. |
| 5 | P-5 | The result can be used again and is not made for one project only. | "Is this a one-off construction or something reusable?" (2026-10-10) | The owner looks at the plan of a trial: its parts are not written for one project only. |
| 6 | P-6 | The skill does not add technical debt to the project. | "Is the skill creating more technical debt?" (2026-10-10) | The owner looks at the plan of a trial: each new part has a named component or a named person that maintains it. |
| 7 | P-7 | The pipeline can follow a change of the repository or of the product. | "how will the pipeline be able to adapt to change in the repo / product?" (2026-10-10) | The owner looks at the plan of a trial: it tells what changes in the pipeline when the repository or the product changes. |
| 8 | P-8 | The recipe judges a practice, and the product that does the practice is a choice of the project. | "using pre-commit is an implementation choice and not a lack." (2026-10-10) | The owner looks at the checklist: no item names a product. The check with `--words` finds such names. |
| 9 | P-9 | A plan is a sufficient result of the skill, because a plan shows the drift. | "it's ok if the skill delivers a plan. with that we can already anticipate drift" (2026-10-10) | The owner looks at the field "Stops when" of the recipe skill in section 5: the skill stops at the plan. |
| 10 | P-10 | The specification can be done again with the research and the Spec Kit setup, to come nearer to the target. | "we need to be able to iterate the spec with the sota research and speckit setup so that we can achieve SLSA draft highest levels" (2026-10-10) | The owner looks at the watch list of section 6 and at the check with `--previous` after a refresh. |

## Constraints

A constraint has no priority. It cannot be traded.

| Id | Constraint | Comes from |
|---|---|---|
| K-1 | The recipe covers the essential basics of each of the three points of view: operations, security and quality. | "we need to check for covering essential and non negotiable basics of each of those 3 points of views." (2026-10-10) |
| K-2 | The build, the test and the packaging do not run in the same step, and no step exposes credentials. | "running build, test, and packaging in the same step and exposing credentials is a no no. See SLSA build track." (2026-10-11) |
| K-3 | Each created skill can work alone. | "the created skills have to be able to work standalone." (2026-10-10) |
