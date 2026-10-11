# Experiment: stage test of the calculation for an item of a basic practice, with and without a collection of maintained templates as a source

## 1. Question

- **Quote**: "code coverage and static code analysis are both basic levels. just like running the tests, failing on failing builds and tests, and CVE list of scanned dependency. All are very basic things that for instance are automated practices in most stack that you can find in the to-be-continuous gitlab pipeline template project. They implement a solid baseline."
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome.
  - `confirmed`: the research reads the maintained implementations of an aspect as a class of sources, and the task of the answers uses them for the breadth and for the cost.
  - `refuted`: such a source does not change where the calculation puts the item. No rule for this class of sources is added for the placement. The numbers of the two arms decide the next test.
  - `not decided`: two more runs for each arm.

## 2. Hypothesis

- **Statement**: A session that answers the questions of risk and reward for the item of the coverage gives the breadth 3 in more runs when the evidence record holds a collection of maintained pipeline templates.
- **Forbidden result**: the arm with the collection has the breadth 3 for the item in no more runs than the arm without it.
- **Criterion**: C-1
- **Confirmed when**: `templates - plain >= 2`
- **Refuted when**: `templates - plain <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Is the breadth of the item C-43 (coverage) the value 3? | program | `C-43 \x7c[^\x7c\n]*\x7c[^\x7c\n]*\x7c\s*3\b` | file:vetting.md |
| C-2 | Does one answer at least of the item C-43 name a source? | program | `C-43 \x7c[^\n]*\(S-\d` | file:vetting.md |
| C-3 | Is the breadth of the item C-19 (dynamic security tests by the risk of the product) below 3? | program | `C-19 \x7c[^\x7c\n]*\x7c[^\x7c\n]*\x7c\s*[12]\b` | file:vetting.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| plain | the recorded specification of the trial I-4 with one new item for the coverage; three items wait for their answers | prompts/answers.md | inputs/plain |
| templates | the same, and one more source in section 2 and in the evidence record: the reference of one template of a collection of maintained pipeline templates | prompts/answers.md | inputs/templates |

- **More than one difference**: one source is the one difference. A source has a row in section 2 of spec.md and a row in evidence.md, thus two files differ.

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Edit, Write
- **Runs for each arm**: 3
- **Time limit**: 1800
- **Git repository**: no
- **Fewer than five runs**: a stage test is small on purpose. A full trial follows only when a stage test shows a difference.

## 6. Words of the expected answer

- (none): the item of the coverage is in the input of each arm. The test is the value that the session writes.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| plain | C-1 | 3 |
| templates | C-1 | 3 |
| plain | C-2 | 0 |
| templates | C-2 | 3 |
| plain | C-3 | 3 |
| templates | C-3 | 3 |

The agent predicts that the hypothesis is refuted: the session gives the breadth 3 without the new source. The agent predicts level 1 for the item C-43 in each run of each arm, computed by `place.py` after the runs.

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
