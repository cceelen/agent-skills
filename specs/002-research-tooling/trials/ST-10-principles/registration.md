# Experiment: stage test of the patterns across platforms and of the principles against a standard

## 1. Question

- **Quote**: "don't only look at the items produced by a projects but also by their writing and principals about it. the TBC project is quite opinionated. i don't agree with all of the choices, and there are common recommendations that disagree too, e.g. pinning all external resources used."
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome.
  - `confirmed`: the kind `principle` and the comparison stay in the procedure. The full trial of the factory follows.
  - `refuted`: a session does not find the disagreement between a principle of a project and the standard. The comparison becomes a step of its own with one principle at a time, and that step gets its own test before a full trial.
  - `not decided`: two more runs.

## 2. Hypothesis

- **Statement**: A session that gets the principles of the projects and the requirements of a standard records the disagreement on the use of the newest version of a tool against a fixed version.
- **Forbidden result**: no row of the table of the disagreements names the line Q-18-039, in two or more of three runs.
- **Criterion**: C-1
- **Confirmed when**: `compare >= 2`
- **Refuted when**: `compare <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does a row of the disagreements name the line Q-18-039 (the newest version of the analysis tools)? | program | `(?m)^\x7c[^\n]*Q-18-039` | file:disagreements.md |
| C-2 | Does that row name a requirement of the standard also? | program | `(?m)^\x7c(?=[^\n]*Q-18-039)[^\n]*R-22-\d` | file:disagreements.md |
| C-3 | Does one group of patterns hold a line of the project S-18 and a line of a project of the other platform? | program | `(?m)^\x7c\s*G-\d+(?=[^\n]*P-18-)(?=[^\n]*P-(?:19-)?(?:2[01]-)?\d)[^\n]*P-(?:19\b)?(?:2[01]\b)?-\d` | file:groups.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| compare | the only arm: 127 pattern lines and 104 principle lines of four projects, and 56 requirements of one standard, from the index | prompts/compare.md | inputs/case |

- **One arm**: the test measures one new stage. The stage test ST-9 gives the value for the patterns without the new rule for their names: no group joined the project of the second platform with the others.

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Write
- **Runs for each arm**: 3
- **Time limit**: 2400
- **Git repository**: no
- **Fewer than five runs**: a stage test is small on purpose. A full trial follows only when a stage test shows a difference.

## 6. Words of the expected answer

- (none): the prompt names no topic. The input holds the lines themselves.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| compare | C-1 | 2 |
| compare | C-2 | 2 |
| compare | C-3 | 3 |

The agent predicts: each run writes between 5 and 20 rows of disagreements.

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
