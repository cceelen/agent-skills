# Experiment: stage test of the reading of a regulation and of a governance standard

## 1. Question

- **Quote**: "PCIDSS / payment card standard and EU regulation should have been converted into a good amount of directions ... they do not give requirements but are very broad in saying that the minimum is."
- **Date**: 2026-10-13
- **Decision**: what is done after each outcome.
  - `confirmed`: the reader and its task stay as they are. The trial I-23 lacked the text, not the reading. The next step is the retrieval and the search for the duties of a product.
  - `refuted`: the task of the reader does not take the broad statements of a regulation as requirement lines. The owner gets the result, and the task of the reader is the next change.
  - `not decided`: two more runs.

## 2. Hypothesis

- **Statement**: A file reader that reads the range of a regulation that states the duties of a manufacturer returns requirement lines for it.
- **Forbidden result**: the report has no requirement line, or the line `REQ | none`, in two or more of three runs.
- **Criterion**: C-1
- **Confirmed when**: `regulation >= 2`
- **Refuted when**: `regulation <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does the report hold a requirement line that is not `none`? | program | `(?m)^REQ \x7c (?!none)` | final |
| C-2 | Does the report hold ten or more requirement lines? | program | `(?ms)(?:^REQ \x7c (?!none).*?){10}` | final |
| C-3 | Does the report hold thirty or more requirement lines? | program | `(?ms)(?:^REQ \x7c (?!none).*?){30}` | final |
| C-4 | Read the lines of the report that start with REQ. Does one or more of these lines state a duty in broad words: it names a result that must hold, and it names no technique, no tool and no number? | judge | | final |
| C-5 | Read the lines of the report that start with REQ. Does one or more of these lines name the group of persons that has the duty? | judge | | final |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| regulation | the first range of the index for the converted regulation of the trial I-23 (pages 1 to 25 of 31: the articles and the first annexes) | prompts/regulation.md | inputs/regulation |
| governance | one range of the index for the converted governance standard of the trial I-23 (pages 147 to 171 of 397) | prompts/governance.md | inputs/governance |

- **More than one difference**: the two arms are two cases of one reader, not a comparison. Each arm has its source, its range and its class.
- **The second arm**: the limit of a hypothesis reads one arm. The same limit holds for the arm `governance`: two or more of three runs with the criterion C-1. The result names its count beside the verdict.
- **The task**: the file task.md is the file `prompts/reader.md` of the tooling as it is. The prompt holds the rules of the agent `sota-file-reader` and what a caller gives: the file, the range, the class and the questions.
- **No arm without the text**: the trial I-23 is that case. Its two reports hold no requirement line of these sources.

## 5. Subject

- **Product**: claude
- **Model**: haiku
- **Tools**: Read
- **Runs for each arm**: 3
- **Time limit**: 1200
- **Git repository**: no
- **Fewer than five runs**: a stage test is small on purpose.

## 6. Words of the expected answer

- (none): the prompt and the task name no requirement of the two sources. The agent of the factory did not read the two converted files. It searched them with a program for the headings of the articles, of the annexes and of one requirement, to choose the ranges.

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| regulation | C-1 | 3 |
| regulation | C-2 | 3 |
| regulation | C-3 | 2 |
| regulation | C-4 | 3 |
| regulation | C-5 | 3 |
| governance | C-1 | 3 |
| governance | C-2 | 3 |
| governance | C-3 | 1 |
| governance | C-4 | 2 |
| governance | C-5 | 1 |

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
