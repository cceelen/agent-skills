# Charter: [MAJOR ASPECT]

**State**: draft

The charter is the "why" of the aspect: the target, the principles with their priority and the
constraints of the owner. It governs the triage of each requirement. Only the owner changes it.
The file is `charter.md`, beside `spec.md`.

Write the state in one of these forms: `draft`, or `reviewed by the owner on <YYYY-MM-DD>`.
Write each line from the words of the owner, with the date. Do not write a line that the owner
did not state.

## Target

What a project reaches when it applies the recipe. One row for each part of the target.

- **Id**: `T-<number>`. Use each identifier one time.
- **Part of the target**: the name of the part, in the words of the owner.
- **Level of the scale**: the level of the measured scale that this part asks for.
- **Level of the recipe**: 1, 2 or 3. Each checklist item that holds a requirement that serves
  this part is admitted, and is on this level of the recipe or on a lower level.

| Id | Part of the target | Level of the scale | Level of the recipe |
|---|---|---|---|
| T-1 | [part of the target] | [level of the scale] | [1, 2 or 3] |

## Principles

A principle with a lower number wins when two principles disagree.

- **Priority**: a whole number. Use each number one time.
- **Id**: `P-<number>`. Use each identifier one time.
- **Principle**: one sentence.
- **Comes from**: the words of the owner as a quote, with the date.
- **Effect**: what the principle does in the triage. See "The cell Effect".

| Priority | Id | Principle | Comes from | Effect |
|---|---|---|---|---|
| 1 | P-1 | [principle] | ["the words of the owner" (DATE)] | [effect] |

## Constraints

A constraint has no priority. It cannot be traded.

- **Id**: `K-<number>`. Use each identifier one time.
- **Constraint**: one sentence.
- **Comes from**: the words of the owner as a quote, with the date, or the rule that it comes
  from.
- **Effect**: what the constraint does in the triage. See "The cell Effect".

| Id | Constraint | Comes from | Effect |
|---|---|---|---|
| K-1 | [constraint] | ["the words of the owner" (DATE)] | [effect] |

## The cell Effect

A program reads the cell. Write one or more of these forms, with a semicolon between two forms.
Do not write a different text into the cell.

- `level <n>`: n is 1, 2 or 3. Each checklist item that holds a requirement that serves the
  line is admitted, and is on level n of the recipe or on a lower level.
- `no exit: 3.3`: a requirement that serves the line does not go to a decision that depends on
  context.
- `no exit: boundary`: a requirement that serves the line does not go to a boundary.
- `no exit: not admitted`: a checklist item that holds a requirement that serves the line is
  admitted.
- `none`: the line has no effect that a program examines. Write `none` alone.
- `none: rule of the factory`: the line is a rule for the factory and not for the content of
  the recipe. No requirement must serve it. Write this form alone.

A requirement serves a line when its cell "Serves" in the table "Requirements" of `vetting.md`
names the identifier of the line.
