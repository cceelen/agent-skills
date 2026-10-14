# Experiment: stage test of the exit for a duty of another party

## 1. Question

- **Quote**: "Yeah ... i guess it needs a triage and plausibility check and then a re-prioritization with all requirements on the table after the seach finished."
- **Date**: 2026-10-14
- **Decision**: what is done after each outcome.
  - `confirmed`: the exit and the rule stay. The next step is the grouping of the requirements that say the same.
  - `refuted`: the rule does not bring a session to give this exit. The owner gets the result as "no gain". No further change to this rule without a decision of the owner.
  - `not decided`: two more runs.

## 2. Hypothesis

- **Statement**: A session that does the rule on the specification of the trial I-25 gives the exit `other party` to one hundred or more requirements.
- **Forbidden result**: fewer than one hundred rows have this exit, in two or more of three runs.
- **Criterion**: C-2
- **Confirmed when**: `case >= 2`
- **Refuted when**: `case <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does no row whose requirement starts with an authority, a state or a court go to an item? | program | `(?s)\A(?!.*\n\x7c R-\d+ \x7c (?:The \|A \|An \|Each )?(?:European )?(?:Commission\|Member States?\|ESAs\|ENISA\|CSIRTs?\|competent authorit\w+\|national courts?\|courts?\|Lead Overseer)\b[^\n]*\x7c C-\d+ \x7c\s*\n)` | file:specs/001-devsecops/vetting.md |
| C-2 | Do one hundred or more rows have the exit `other party`? | program | `(?s)\A(?:(?>.*?\x7c other party: )){100}` | file:specs/001-devsecops/vetting.md |
| C-3 | Does no row whose requirement starts with the manufacturer or the financial entity as the party with the duty have the exit `other party`? | program | `(?s)\A(?!.*\n\x7c R-\d+ \x7c (?:Manufacturers\|A manufacturer\|Financial entities) shall[^\n]*\x7c other party:)` | file:specs/001-devsecops/vetting.md |
| C-4 | Does the check pass at the end? | program | `(?m)^No check fails\.$` | file:check.out |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| case | the only arm: the specification of the trial I-25 with its 2499 requirement rows, the tooling of the iteration I-26 and the part of the step "Distil" with the rule | prompts/duty.md | inputs/case |

- **One arm**: the input is the case without the rule. A program counted it before this registration: 875 rows come from the four sources of the classes `regulation` and `governance`, each goes to an item, and the pattern of the criterion C-1 finds 116 of them. No row has the exit `other party`.
- **The limit**: one hundred is below the 116 rows that the pattern finds, because the words at the start of a row do not decide each case.

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Write, Edit, Glob, Grep, Bash
- **Runs for each arm**: 3
- **Time limit**: 2400
- **Git repository**: no
- **Fewer than five runs**: a stage test is small on purpose.

## 6. Words of the expected answer

- (none): the prompt names no party. The rule of the procedure gives four examples of a party that is not in a project. The agent of the factory saw the first words of the rows through a program, to write the patterns.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| case | C-1 | 1 |
| case | C-2 | 3 |
| case | C-3 | 3 |
| case | C-4 | 3 |

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
- **Ladder**: the values and the level limits of the ladder are a draft of the agent of the factory. The owner did not confirm them.
