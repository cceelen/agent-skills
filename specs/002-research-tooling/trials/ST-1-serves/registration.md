# Experiment: stage test of the cell Serves, on recorded requirements

## 1. Question

- **Quote**: "continue the trials, tests, and improvement iterations. make sure that you keep what helps and avoid onboarding too much complexity"
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome.
  - `confirmed`: the charter in the triage (iteration I-6) stays. The next small test replays the placement on the whole recorded register.
  - `refuted`: the session does not connect a requirement with the line of the charter that keeps it. The effects of the charter then place nothing. The next step changes how a line of the charter says what serves it, or the change of I-6 is removed.
  - `not decided`: two more runs of this test.

## 2. Hypothesis

- **Statement**: A session that gets the charter and recorded requirements writes, for the requirement about the measure of test coverage, a line of the charter that keeps it in the checklist (P-1 or P-2).
- **Forbidden result**: the cell Serves of that requirement is `none`, or names only other lines, in two or more of three runs.
- **Criterion**: C-1
- **Confirmed when**: `serves >= 2`
- **Refuted when**: `serves <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does the row R-1026 (a measure of coverage) serve P-1 or P-2? | program | `R-1026 \x7c(?:[^\x7c\n]*\x7c){4}[^\x7c\n]*\bP-[12]\b` | file:vetting.md |
| C-2 | Does the row R-606 (fuzzing) serve P-1 or P-2? | program | `R-606 \x7c(?:[^\x7c\n]*\x7c){4}[^\x7c\n]*\bP-[12]\b` | file:vetting.md |
| C-3 | Does the row R-028 (a requirement of the architecture) serve a line of the charter? | program | `R-028 \x7c(?:[^\x7c\n]*\x7c){4}[^\x7c\n]*\b[PKT]-\d` | file:vetting.md |
| C-4 | Is the row R-339 (a requirement with no relation to the charter) marked `none`? | program | `R-339 \x7c(?:[^\x7c\n]*\x7c){4}\s*none\s*\x7c` | file:vetting.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| serves | the only arm: the charter of DevSecOps with its effects, and 150 recorded requirements of the trial I-4 | prompts/serves.md | inputs/case |

- **One arm**: the test measures one stage of one tooling version on recorded input.

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Edit, Write
- **Runs for each arm**: 3
- **Time limit**: 1800
- **Git repository**: no
- **Fewer than five runs**: a stage test is small on purpose; three runs show if the stage is stable. A full trial follows only when a stage test shows a difference.

## 6. Words of the expected answer

- (none): the input holds the recorded requirements themselves, with their words; the test is which line of the charter the session writes for them.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| serves | C-1 | 2 |
| serves | C-2 | 2 |
| serves | C-3 | 1 |
| serves | C-4 | 3 |

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
