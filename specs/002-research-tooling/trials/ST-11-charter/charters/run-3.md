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
| T-1 | The baseline that a project reaches on the build track of SLSA. | L2 | "the slsa L2 should be a baseline. L3 the goal. beyond L3 aspirational (e.g. hermetic repeatable build, or in the asus zenbook case the usage of a build service)." (2026-10-11) |
| T-2 | The goal that a project reaches on the build track of SLSA. | L3 | "the slsa L2 should be a baseline. L3 the goal. beyond L3 aspirational (e.g. hermetic repeatable build, or in the asus zenbook case the usage of a build service)." (2026-10-11) |
| T-3 | The aspiration of a project on the build track of SLSA: for example a hermetic and repeatable build, or the use of a build service. | beyond L3 | "the slsa L2 should be a baseline. L3 the goal. beyond L3 aspirational (e.g. hermetic repeatable build, or in the asus zenbook case the usage of a build service)." (2026-10-11) |
| T-4 | The specification can be iterated until a project can reach the highest levels of the drafts of SLSA. | the highest levels of the drafts of SLSA | "we need to be able to iterate the spec with the sota research and speckit setup so that we can achieve SLSA draft highest levels" (2026-10-10) |

## Principles

A principle with a lower number wins when two principles disagree.

| Priority | Id | Principle | Comes from | How it is checked |
|---|---|---|---|---|
| 1 | P-1 | The recipe covers the basic practices that are not negotiable in each of the three points of view: operations, security and quality. | "we need to check for covering essential and non negotiable basics of each of those 3 points of views." (2026-10-10); "DevSecOps is about doing shift left of operational, security, and quality concerns." (2026-10-10) | The part "Views" of the check: each of the three points of view is a view, and each view has an item on level 1. |
| 2 | P-2 | The recipe gives the integration of the needs of the stakeholders, of the requirements and of the regulation to the architecture. | "architecture is responsible for the integration of the different stakeholder needs, requirements, regulation, and so on." (2026-10-11) | The field "Stakeholders" and the field "Views" of section 1: each stakeholder is in a view. The list "What remains" of the check names no stakeholder that is in no view. |
| 3 | P-3 | The recipe tells which governance elements each practice complies with. | "to which governance elements are they complying?" (2026-10-10) | The cell "Source" of each checklist item, and the sources of section 2 with the class `standard`. |
| 4 | P-4 | The recipe uses pipeline components that exist and are maintained, before it builds a new one. | "is it reusing existing and maintained pipeline elements / components / actions / steps?" (2026-10-10) | The plan of a trial: each step of the pipeline names the maintained component that it uses, or says why it uses none. |
| 5 | P-5 | The result of the recipe can be used again for a different project. It is not a construction for one project. | "Is this a one-off construction or something reusable?" (2026-10-10) | The plan of a trial, and the findings of the reviewer in `trial.md`. |
| 6 | P-6 | The recipe does not add technical debt to a project. | "Is the skill creating more technical debt?" (2026-10-10) | The findings of the reviewer in `trial.md`. |
| 7 | P-7 | The pipeline can adapt when the repository or the product changes. A plan is a sufficient result of the skill, because a plan shows drift. | "how will the pipeline be able to adapt to change in the repo / product?" (2026-10-10); "it's ok if the skill delivers a plan. with that we can already anticipate drift" (2026-10-10) | The field "Stops when" of the recipe skill in section 5, and the plan of a trial: the plan says how a change of the repository is found. |
| 8 | P-8 | A checklist item names the practice. The tool that does the practice is a choice of the project, and the recipe does not report a different tool as a gap. | "using pre-commit is an implementation choice and not a lack." (2026-10-10) | The check with `--words`: no checklist item names a product. |

## Constraints

A constraint has no priority. It cannot be traded.

| Id | Constraint | Comes from |
|---|---|---|
| K-1 | The build, the test and the packaging do not run in the same step, and no such step exposes credentials. | "running build, test, and packaging in the same step and exposing credentials is a no no. See SLSA build track." (2026-10-11) |
| K-2 | Each skill that is made works alone. | "the created skills have to be able to work standalone." (2026-10-10) |
