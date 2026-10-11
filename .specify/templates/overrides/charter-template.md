# Charter: [MAJOR ASPECT]

**State**: draft

The charter is the "why" of the aspect: the target, the principles with their priority and the
constraints of the owner. The session reads it before the triage, and the owner gets it first
in the review. Only the owner changes it. The file is `charter.md`, beside `spec.md`.

Write the state in one of these forms: `draft`, or `reviewed by the owner on <YYYY-MM-DD>`.
Write each line from the words of the owner, with the date. Do not write a line that the owner
did not state.

## Target

What a project reaches when it applies the recipe. One row for each part of the target.

| Id | Part of the target | Level of the scale | Comes from |
|---|---|---|---|
| T-1 | [part of the target] | [level of the measured scale] | ["the words of the owner" (DATE)] |

## Principles

A principle with a lower number wins when two principles disagree.

| Priority | Id | Principle | Comes from | How it is checked |
|---|---|---|---|---|
| 1 | P-1 | [principle] | ["the words of the owner" (DATE)] | [what the owner looks at in the review] |

## Constraints

A constraint has no priority. It cannot be traded.

| Id | Constraint | Comes from |
|---|---|---|
| K-1 | [constraint] | ["the words of the owner" (DATE)] |
