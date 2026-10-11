# Experiment: stage test of the search for the maintained projects of an aspect

## 1. Question

- **Quote**: "I expected the factory or the skill to pick up projects like these when doing the research."
- **Date**: 2026-10-11
- **Decision**: what is done after each outcome.
  - `confirmed`: the rule for the maintained projects stays in the step "List what exists".
  - `refuted`: the rule does not make a session find such projects. The rule is removed, and the next test gives the search a list of places where projects are published.
  - `not decided`: two more runs of this test.

## 2. Hypothesis

- **Statement**: A session that does the step "List what exists" with the rule for the maintained projects lists one project at least that gives reusable components, and one tool at least that examines a project.
- **Forbidden result**: the list of sources has no row of the kind `project-components`, or no row of the kind `project-tool`, in two or more of three runs.
- **Criterion**: C-1
- **Confirmed when**: `search >= 2`
- **Refuted when**: `search <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does the list hold a row of the kind `project-components` and a row of the kind `project-tool`? | program | `(?s)(?=.*\x7c\s*project-components\s*\x7c)(?=.*\x7c\s*project-tool\s*\x7c)` | file:sources.md |
| C-2 | Does the list hold three or more rows of the kinds `standard`, `framework`, `research` or `book`? | program | `(?s)(?:\x7c\s*(?:standard\x7cframework\x7cresearch\x7cbook)\s*\x7c.*){3}` | file:sources.md |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| search | the only arm: the step "List what exists" with the rule for the maintained projects | prompts/search.md | inputs/case |

- **One arm**: the recorded trials I-2 to I-5 show the step without the rule: 58 queries, no query for a maintained project, and no source that is one.

## 5. Subject

- **Product**: claude
- **Model**: opus
- **Tools**: Read, Write, WebSearch, WebFetch
- **Runs for each arm**: 3
- **Time limit**: 1800
- **Git repository**: no
- **Fewer than five runs**: a stage test is small on purpose. A full trial follows only when a stage test shows a difference.

## 6. Words of the expected answer

- (none): the prompt names the kinds of a source, and no project.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| search | C-1 | 3 |
| search | C-2 | 3 |

The agent predicts, without a criterion: the projects that the owner named are in the list of one run at most. The owner named a collection of pipeline templates and two tools that examine a pipeline.

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
