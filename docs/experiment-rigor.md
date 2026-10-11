# experiment-rigor

`experiment-rigor` is tooling of the factory. It makes a trial of an agent, a skill, a prompt or
an instruction a registered experiment. The tooling is in `factory/experiment-rigor/`. Users of
the kit do not install it.

A trial without a registration can give a result that is not true. These are the causes that
the tooling prevents:

- The subject gets a file that holds the expected answer.
- The subject loads personal plugins, personal skills or a personal instruction file.
- Two runs differ in more than one thing.
- There is one run for each condition.
- There is no prediction before the run.
- The judge knows the expected answer or the group of a run.

The program `experiment.py` is the gate. It refuses a run without a complete and sealed
registration, and it builds the environment of each run itself.

## Before you start

- Install `uv`. The program uses the latest stable Python, and `uv` gets it.
- Install the agent product of the subject. The program knows the product `claude`.
- Select a work folder outside each git repository. No folder above it can hold an instruction
  file for agents. Thus do not use a folder below your home folder if `~/.claude` exists.

## Your part as the owner

1. Give the question in your own words. The agent writes it into the registration as a quote.
2. Read `registration.md` before the seal. Make sure that each outcome changes a decision.
3. Read the list "Loaded instructions" of the command `check`. The subject loads these files.
4. After the seal, do not permit a change of the registration. A change needs a new folder.
5. Read `result.md`. A text below "Explanations after the fact" is a guess.

To start, tell your agent to read `factory/experiment-rigor/SKILL.md` and to do its steps.

## The commands

Run the program with `uv run`. Without an argument, the program prints its usage text.

```text
uv run factory/experiment-rigor/scripts/experiment.py check <folder>
uv run factory/experiment-rigor/scripts/experiment.py seal <folder> --today <date>
uv run factory/experiment-rigor/scripts/experiment.py run <folder> --work <work folder>
uv run factory/experiment-rigor/scripts/experiment.py blind <folder> --work <work folder>
uv run factory/experiment-rigor/scripts/experiment.py score <folder>
```

| Result code | Meaning |
|---|---|
| 0 | The command is done. Nothing fails and nothing remains. |
| 1 | Something fails or remains. The output tells you what. |
| 2 | The program cannot read its input, or the arguments are wrong. |

## The folder of an experiment

One experiment has one folder. Commit it with the specification or the investigation that it
belongs to.

| File | Written by | Contents |
|---|---|---|
| `registration.md` | the agent, before the seal | The eight sections of the registration. |
| prompt files | the agent, before the seal | The task of the subject, as the subject gets it. |
| input folders | the agent, before the seal | The files that the subject sees at the start. |
| `sealed.json` | `seal` | The digest of each file above, the date and the commit. |
| `results.jsonl` | `run` | One row for each run. |
| `blind-key.json` | `blind` | The arm and the run number of each packet. |
| `judgements.md` | the judge | The answers of the judge. |
| `result.md` | `score` | The counts, the intervals, the comparison and the verdict. |

The run folders, the transcripts and the packets are in the work folder. Do not commit them.

## The registration

Copy `factory/experiment-rigor/references/registration-template.md`. A field has the form
`- **Name**: text`. Do not change the headings and the names of the fields.

| Section | Contents |
|---|---|
| 1. Question | Your words as a quote, the date, and the decision after each outcome. |
| 2. Hypothesis | One sentence, the result that it forbids, the criterion and the two limits. |
| 3. Measure | The criteria. Each one is a question with the answer yes or no. |
| 4. Arms | The conditions. Each arm has its prompt files and its input folder. |
| 5. Subject | The product, the model, the tools, the number of runs, the time limit. |
| 6. Words of the expected answer | The words that no prompt and no input file can hold. |
| 7. Predictions | The predicted count for each arm and each criterion. |
| 8. Environment | The names that a session can load in addition to the product itself. |

### The limits of the hypothesis

A limit compares counts. A count is the number of runs of one arm with the answer yes, for the
criterion of the hypothesis.

- Write a limit as `ARM >= NUMBER` or `ARM - ARM >= NUMBER`. Join two parts with `and`.
- The operators are `>=`, `<=`, `>`, `<` and `==`.
- The verdict is "confirmed" if the limit `Confirmed when` is true.
- The verdict is "refuted" if the limit `Refuted when` is true.
- In each other case, the verdict is "not decided".
- The check fails if a result can make the two limits true together.
- The check fails if no result can confirm the hypothesis, or if no result can refute it.

### The criteria

- The cell `Answered by` holds `program` or `judge`.
- A criterion of the program has a regular expression in the cell `Pattern`. The answer is yes
  if the pattern is in the text. Write a pipe in a pattern as `\|`.
- The cell `Where` holds `final` or `file:<path>`. `final` is the final text of the last session
  of the run. `file:<path>` is a file of the run folder after the last session.
- If the run did not write the file, the answer of the program is no.

### The arms

- The cell `Prompt files` holds one file or more, with commas. Each file is one new session in
  the same run folder, in this order.
- The cell `Input folder` holds a folder of the experiment, or `(empty)`.
- The id of an arm starts with a letter and holds only letters, digits and `_`.

### The optional fields

| Field | Section | When it is necessary |
|---|---|---|
| `One arm` | 4, below the table | There are fewer than two arms. |
| `More than one difference` | 4, below the table | Two arms differ in more than one thing. |
| `Fewer than five runs` | 5 | The number of runs for each arm is below 5. |

Each of these fields holds the reason. Section 6 can hold `- (none): <reason>`.

## What the check examines

The command `check` prints one line `FAIL` for each finding, with the section and the field.

- A field is absent or empty, or holds the placeholder of the template.
- The question has no quote or no date.
- A decision is absent, or each outcome gives the same decision.
- The hypothesis has no forbidden result, or a limit that the program cannot read.
- A criterion has no id, no question or no `program` or `judge`.
- A criterion of the program has no pattern that compiles.
- A prompt file or an input folder of an arm is not there.
- Two arms have the same prompts and the same inputs.
- Two arms differ in more than one thing, and the field with the reason is absent.
- There are fewer than five runs for each arm, and the field with the reason is absent.
- A prediction for an arm and a criterion is absent.
- A word of the expected answer is in a prompt or in an input file. The line gives the file
  and the line number.

The program counts the differences between two arms as follows. Each block of lines that
differs between two prompt files is one difference. Each input file that only one arm has, or
that has a different content, is one difference. The part "Differences between the arms" lists
each of them.

The part "Loaded instructions" lists the files of the input folders that an agent product
loads as instructions, for example `CLAUDE.md`, `AGENTS.md` and each file of a folder `.claude`.
These files do not fail the check. Make sure that the subject must get each of them.

## The seal

The command `seal` runs the check. If nothing fails, it writes `sealed.json`.

- If the folder is in a git repository, commit the registration, the prompt files and the
  input folders first. The seal records the commit.
- The commit shows that the predictions are older than the runs.
- You can seal again before the first run. After the first run, the program refuses a new seal.
- The commands `run`, `blind` and `score` refuse a folder whose files differ from the seal.

## The runs

The command `run` does each run that has no valid row in `results.jsonl`.

1. It makes a new run folder in the work folder. The name is a code that does not show the arm.
2. It copies the input folder of the arm into the run folder.
3. If the registration says `Git repository: yes`, it makes the run folder a repository with
   one commit.
4. It starts one session for each prompt file, in the registered order.
5. It writes the transcript of each session into the folder `transcripts` of the work folder.
6. It adds one row to `results.jsonl`.

- The program does at most four runs at the same time.
- The program never does more runs than the registered number.
- If a session broke or was not clean, the row is not valid and gives the reason. The row stays
  in the record. Run the command again: it does that run again.
- A row holds the arm, the run number, the attempt, the final text of each session, the paths
  of the transcripts in the work folder and the start event of each session.

### The clean environment of the product `claude`

The program starts each session with these options, with no input, in the run folder:

```text
claude -p <prompt> --model <model> --tools <tools> --allowedTools <tools>
  --setting-sources project --no-session-persistence --output-format stream-json --verbose
  --strict-mcp-config --disable-slash-commands
```

It sets the variable `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` for the session. Without tools, it
gives `--tools ""` and no `--allowedTools`.

These are the results of real sessions with version 2.1.296 of the product on 2026-10-10:

| Options | Plugins | Connectors | Skills | Agents | Personal instruction file |
|---|---|---|---|---|---|
| none | 3 of the product, 3 personal | 22 | 57 | 5 of the product, 2 personal | loaded |
| `--setting-sources project` | 3 of the product | 2 in one session, 0 in a second session | 19 of the product | 5 of the product | not loaded |
| the options of the program | 3 of the product | 0 | 0 | 5 of the product | not loaded |

- `--strict-mcp-config` removes the connectors of the account.
- `--disable-slash-commands` removes the skills of the product.
- `--tools` sets the tools that the subject has. `--allowedTools` only permits a tool.
- `--no-session-persistence` and the variable stop the files that the product writes below
  the home folder for each run folder.
- If section 8 permits a connector, the program does not give `--strict-mcp-config`.
- If section 8 permits a skill, the program does not give `--disable-slash-commands`.

The program reads the start event of each session. A run is clean only if the event names no
plugin, no connector, no skill and no agent in addition to the names of the product itself and
the names of section 8, and no memory folder. The names of the product itself are in the table
`HOSTS` of the program. If a new version of the product has a new name, add it to that table.

The program cannot switch off these parts:

- The three plugins and the five agents of the product itself stay. Each row records them.
- The product loads the instruction files of each folder above the run folder. A real session
  in a folder below the home folder loaded `~/.claude/CLAUDE.md`, also with the options above.
  Thus the program refuses a work folder if a folder above it holds such a file.
- The product loads the instruction files of the input folder. The check lists them.
- The system prompt of the product and the variables of your shell stay.
- The tools of the subject can read a file outside the run folder. The program does not
  prevent this.
- The option `--bare` needs an API key. With a login it gives "Not logged in". The program does
  not use it.

To add a second agent product, add one entry to the table `HOSTS` and one function that reads
its stream.

## The judge

The command `blind` writes one packet for each valid run into `<work folder>/packets`.

- The name of a packet is a code. It does not show the arm.
- A packet holds the final texts, the files that a criterion of the judge names, and the file
  `criteria.md`. It holds no hypothesis, no prediction and no name of an arm.
- The key is `blind-key.json` in the folder of the experiment. Do not give it to the judge.
- The task of the judge is `factory/experiment-rigor/prompts/judge.md`.
- The judge writes `judgements.md`. The agent copies it into the folder of the experiment.
- If no criterion has the judge, the command writes no packet.

## The result

The command `score` writes `result.md` and prints it.

- For each criterion and each arm: the count, the share, the Wilson interval of 95 percent and
  the predicted count.
- For each pair of arms: the exact test of Fisher with two sides.
- The verdict from the registered limits. The program uses no other rule.
- If runs remain or an answer of the judge is absent or wrong, the verdict is "none". The part
  "What remains" lists each point, and the count of that criterion is "remains".
- The runs that were not valid, with the reason.
- The part "Explanations after the fact". Write an explanation only there. The command keeps
  that text when you run it again.

## Make sure that the program is correct

The program holds its tests as examples in the program itself. The examples use the sample in
`factory/experiment-rigor/scripts/sample.py`. They do not use the network and they do not start
the agent product.

```text
uv run factory/experiment-rigor/scripts/experiment.py --selftest
```

To run the examples of all programs and to measure the coverage, run `uv run pytest`.
