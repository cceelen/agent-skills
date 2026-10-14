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
| T-1 | The baseline: each project reaches this level. | SLSA L2 | "the slsa L2 should be a baseline. L3 the goal. beyond L3 aspirational (e.g. hermetic repeatable build, or in the asus zenbook case the usage of a build service)." (2026-10-11) |
| T-2 | The goal: the recipe brings a project to this level. | SLSA L3 | "the slsa L2 should be a baseline. L3 the goal. beyond L3 aspirational (e.g. hermetic repeatable build, or in the asus zenbook case the usage of a build service)." (2026-10-11) |
| T-3 | The aspiration: a project can go further, but this is not necessary. | beyond SLSA L3 | "the slsa L2 should be a baseline. L3 the goal. beyond L3 aspirational (e.g. hermetic repeatable build, or in the asus zenbook case the usage of a build service)." (2026-10-11); "we need to be able to iterate the spec with the sota research and speckit setup so that we can achieve SLSA draft highest levels" (2026-10-10) |

## Principles

A principle with a lower number wins when two principles disagree.

| Priority | Id | Principle | Comes from | How it is checked |
|---|---|---|---|---|
| 1 | P-1 | The recipe moves the operational, the security and the quality concerns to the earliest step of the work. | "DevSecOps is about doing shift left of operational, security, and quality concerns." (2026-10-10) | The views of section 1 hold the three concerns, and the order of the work in section 3.2 puts each check at the earliest step that can do it. |
| 2 | P-2 | The recipe uses existing and maintained pipeline components again, and does not build its own. | "is it reusing existing and maintained pipeline elements / components / actions / steps?" (2026-10-10) | The sources of section 2 and the table of implementation skills in section 5 name maintained components, each with the date of its last release. |
| 3 | P-3 | The recipe does not add technical debt to a project. | "Is the skill creating more technical debt?" (2026-10-10) | The plan of a trial: each part that the project must maintain itself has a reason. |
| 4 | P-4 | The result is reusable in more than one project, and is not a one-off construction. | "Is this a one-off construction or something reusable?" (2026-10-10) | The checklist names no product and no project, and the check finds no product name in it. |
| 5 | P-5 | The recipe says which governance elements each practice complies with. | "to which governance elements are they complying?" (2026-10-10) | The cell "Source" of each checklist item names the unit of a standard or of a framework. |
| 6 | P-6 | The pipeline can adapt when the repository or the product changes. | "how will the pipeline be able to adapt to change in the repo / product?" (2026-10-10) | The contexts of section 1 and the decisions of section 3.3 say what changes when a context changes, and the watch list of section 6 names the signals. |
| 7 | P-7 | Architecture integrates the needs of the stakeholders, the requirements and the regulation. | "architecture is responsible for the integration of the different stakeholder needs, requirements, regulation, and so on." (2026-10-11) | Each stakeholder of section 1 is in a view, and each requirement of the table "Requirements" has an exit. |
| 8 | P-8 | The specification can be iterated with the research of the state of the art and with the Spec Kit setup, until the target is reached. | "we need to be able to iterate the spec with the sota research and speckit setup so that we can achieve SLSA draft highest levels" (2026-10-10) | A refresh changes only the rows that a source touches, and the check passes with `--previous`. |
| 9 | P-9 | The choice of a tool is an implementation choice. The recipe does not count such a choice as a gap. | "using pre-commit is an implementation choice and not a lack." (2026-10-10) | No checklist item names a tool, and no finding of a trial reports a tool choice as a gap. |
| 10 | P-10 | A plan is a sufficient delivery of the skill, because a plan shows drift before it occurs. | "it's ok if the skill delivers a plan. with that we can already anticipate drift" (2026-10-10) | The field "Stops when" of the recipe skill in section 5 stops at the plan. |

## Constraints

A constraint has no priority. It cannot be traded.

| Id | Constraint | Comes from |
|---|---|---|
| K-1 | The recipe covers the essential basics of each of the three points of view: operations, security and quality. | "we need to check for covering essential and non negotiable basics of each of those 3 points of views." (2026-10-10) |
| K-2 | The build, the test and the packaging do not run in the same step, and no step exposes credentials. | "running build, test, and packaging in the same step and exposing credentials is a no no. See SLSA build track." (2026-10-11) |
| K-3 | Each skill that is made can work alone. | "the created skills have to be able to work standalone." (2026-10-10) |
