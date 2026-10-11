# Experiment: stage test of the charter that the session drafts from the words of the owner

## 1. Question

- **Quote**: "You did understand that the sota and factory skills are there to create the charter from the human interaction?"
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome.
  - `confirmed`: the rule stays: the session drafts the charter. The full trial uses a charter that a session drafted and that the owner confirmed.
  - `refuted`: the session does not derive the principles from the words of the owner. The step of the draft gets a task file of its own, and that task gets its own test.
  - `not decided`: two more runs.

## 2. Hypothesis

- **Statement**: A session that gets the words of the owner in the order in which they were said, with no sorting, drafts a charter that holds a principle for six or more of the seven principles of the charter that the owner reviewed on 2026-10-11.
- **Forbidden result**: the charter of two or more of three runs holds five or fewer of the seven principles.
- **Criterion**: C-1
- **Confirmed when**: `draft >= 2`
- **Refuted when**: `draft <= 1`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does the table of the principles have a principle for six or more of these seven: the concerns of operation, security and quality are handled early; each concern has basic practices that are not negotiable; the needs of all stakeholders and the rules from outside are brought together in one design; maintained components are used in place of own constructions; the result can be used again and follows a change of the project; the rules of governance that are met are named; debt is not made without a record? | judge | | file:specs/001-devsecops/charter.md |
| C-2 | Does the table of the target have separate rows for a baseline on level 2, a goal on level 3 and an aspiration above level 3? | judge | | file:specs/001-devsecops/charter.md |
| C-3 | Does the charter have a constraint that the build is separate from other steps or that credentials are not exposed? | judge | | file:specs/001-devsecops/charter.md |
| C-4 | Does the charter have a constraint that the choice of a tool is a choice of the implementation? | judge | | file:specs/001-devsecops/charter.md |
| C-5 | Does each row of the three tables hold a quote of the owner with a date? | judge | | file:specs/001-devsecops/charter.md |
| C-6 | Does the charter hold a row whose content is in no quote of the owner? | judge | | file:specs/001-devsecops/charter.md |
| C-7 | Is the state of the charter a draft? | program | `\*\*State\*\*: draft` | file:specs/001-devsecops/charter.md |
| C-8 | Does the final report say which parts of the charter are a proposal of the session? | judge | | final |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| draft | the only arm: the kit with the rule that the session drafts the charter, and 15 statements of the owner | prompts/p1.md | inputs/kit |

- **One arm**: the test measures one new step. The comparison is the charter that the owner reviewed on 2026-10-11, which the agent of the factory wrote in a long session with the owner.

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Write, Edit, Glob, Grep, Bash
- **Runs for each arm**: 3
- **Time limit**: 1500
- **Git repository**: yes
- **Fewer than five runs**: a stage test is small on purpose. A full trial follows.

## 6. Words of the expected answer

- (none): the prompt holds the words of the owner on purpose. The seven principles of C-1 are sentences of the agent and are in no input.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| draft | C-1 | 3 |
| draft | C-2 | 3 |
| draft | C-3 | 3 |
| draft | C-4 | 3 |
| draft | C-5 | 3 |
| draft | C-6 | 1 |
| draft | C-7 | 3 |
| draft | C-8 | 2 |

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: sota-file-reader, sota-second-reader, sota-source-reader
- **Change of the kit**: the file `skills/library-vetting/scripts/collect.py` is removed from the input folder, as in the trials I-4 and I-5.
