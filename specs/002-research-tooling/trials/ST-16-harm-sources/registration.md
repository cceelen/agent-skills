# Experiment: stage test of the answers of risk and reward with statements of harm and frequency

## 1. Question

- **Quote**: "yes. search is important"
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome.
  - `confirmed`: the research gets a search for sources that state harm and frequency, the reader gets the line for such a statement, and the task for the answers gets the rule.
  - `refuted`: the statements that a search of this kind finds do not give the probability of the harm of an item. The search is not added in this form. The owner decides how the probability is answered.
  - `not decided`: two more runs for each arm.

## 2. Hypothesis

- **Statement**: A session that gets the statements of harm and frequency of sources names, for three or more of ten items, a source for the probability that states how often the harm of the item occurs, in more runs than a session without these statements.
- **Forbidden result**: the session with the statements does this in the same number of runs as the session without them, or in fewer.
- **Criterion**: C-3
- **Confirmed when**: `harm - evidence >= 2`
- **Refuted when**: `harm - evidence <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Do three or more rows of the table Items name a source in the cell Probability? | program | `(?m)(?:^\x7c C-\d+ \x7c[^\x7c]*\x7c \d \([^\x7c]*S-\d+[^\n]*\n(?:(?!\x7c C-\d+ \x7c[^\x7c]*\x7c \d \([^\x7c]*S-\d+)[^\n]*\n)*){2}^\x7c C-\d+ \x7c[^\x7c]*\x7c \d \([^\x7c]*S-\d+` | file:vetting.md |
| C-2 | Read the table Items of this file. The risk that an item answers is in the cell Why of the checklist in the file spec.md of this packet. Count each row whose cell Severity names a row of this file (K-n or R-n) or a source S-n with a location, where that row, or the row of the source S-n in the file evidence.md of this packet, states a harm, a threat or a consequence that belongs to the risk of the item. A statement of only a duty does not count. Is the count three or more? | judge | | file:vetting.md |
| C-3 | Read the table Items of the file vetting.md of this packet. The risk that an item answers is in the cell Why of the checklist in this file. Count each row whose cell Probability names a row of vetting.md (K-n or R-n) or a source S-n with a location, where that row states how often or how probable a harm is that belongs to the risk of the item. Is the count three or more? | judge | | file:spec.md |
| C-4 | Read the table Items of the file vetting.md of this packet. Does one or more cell Severity or Probability name a row of vetting.md (K-n or R-n) that is about a different harm than the risk of the item, or whose scope is one group, one place or one product while the answer is given without that limit? | judge | | file:evidence.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| evidence | the task for the answers as it is in the repository, and the specification of the trial I-14 with ten items | prompts/task.md | inputs/evidence |
| harm | the same, with the statements of harm and frequency that eleven readers reported from the sources of a search on 2026-10-11 | prompts/task.md | inputs/harm |

- **More than one difference**: the arm `harm` has one more table in `vetting.md`, eleven more rows of sources in `spec.md`, and one more rule in the task. The three belong together: the rule names the table, and the rows of the table name the sources.

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Edit, Write, Grep
- **Runs for each arm**: 3
- **Time limit**: 1500
- **Git repository**: no
- **Fewer than five runs**: a stage test is small on purpose.

## 6. Words of the expected answer

- (none): the prompt names only the task file. The added rule says that a row must be about the risk of the item; the judge asks for the same. The search that found the sources got the ten items, thus the sources were searched for these items.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| evidence | C-1 | 0 |
| evidence | C-2 | 0 |
| evidence | C-3 | 0 |
| evidence | C-4 | 0 |
| harm | C-1 | 3 |
| harm | C-2 | 3 |
| harm | C-3 | 2 |
| harm | C-4 | 2 |

In the stage test ST-15, the arm `evidence` had a source that states a harm for 1 of ten severities in each run, and no source for a probability.

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
