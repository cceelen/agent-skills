# sota-research

`sota-research` is the tooling of the factory. It takes one major aspect of software
engineering from "what to build" to an accepted aspect specification and a rendered recipe
skill. A person stays in the loop: the owner decides what to build, confirms the sources and
accepts the result.

The tooling is in `factory/sota-research/`. Users of the kit do not install it.

## The four phases

| Phase | What occurs | Your part as the owner |
|---|---|---|
| 1. What to build | The agent asks for your intent. Then it settles only the field and the thing to build with you. | You answer three questions. You name the field and the thing. |
| 2. Research | Isolated readers read the sources. The agent finds the stakeholders, the views, the contexts, the risk dimensions and the boundaries, and distils the strategy and the checklist. Programs vet the sources and place the items. | None. |
| 3. Review | The agent stops and gives you the findings. | You compare your intent with the findings. You correct the stakeholders, the views, the contexts, the risk dimensions and the boundaries, confirm the sources, correct the answers and accept the result. |
| 4. Rendering | A program renders the recipe skill. A pull request delivers it. | You review the pull request. |

To start, tell your agent to read `factory/sota-research/SKILL.md` and to distil an aspect.
The steps of the agent are in `factory/sota-research/references/procedure.md`.

Before you accept a recipe, you can try it on a project. See "Try a recipe on a project".

## Your intent

The name of an aspect can mean less in the literature than it means to you. Thus the agent
asks for your intent in phase 1, before it reads a source. It asks three questions:

1. What do you mean by the aspect, in your words? Which concerns does it bring together?
2. What must a project be able to show after it applied the recipe? Is there a measurable
   target?
3. What do you not want?

- The agent asks each question one time. It does not ask a question that you answered already.
- The agent writes each answer as a quote, with the date, into the field `Intent of the owner`
  of section 1. It does not change your words.
- If you give no answer, the line holds `(no answer)`.
- The agent does not ask for a use case, a first user, a reference project, an industry, a
  product, stakeholders, viewpoints, views, contexts, risk dimensions or boundaries. The
  research finds them.
- In phase 2, the agent compares your intent with the sources. If the sources mean less than
  you, or something different, the agent records the difference and follows you.
- In phase 3, you get your intent first, beside the stakeholders, the views and the targets.

The check fails if the field is absent or empty, or if an answer has no date. If each line
holds `(no answer)`, the check passes, and the list "What remains" says:
`The intent of the owner was not asked.`

Three agents read the sources. No reader has a shell, a tool that writes or credentials.

| Agent | Tools | What it reads |
|---|---|---|
| `sota-source-reader` | web search, web fetch | One source at its address. |
| `sota-second-reader` | web fetch | The sources of the evidence record, for the comparison. |
| `sota-file-reader` | read | One converted file of the work folder. |

Before the first run, write their agent files:

```text
uv run factory/sota-research/scripts/models.py apply
```

If your agent product cannot limit the tools of an agent, the program tells you. Do not start
a research run with that agent product.

### The hook for the file reader

A list of tools cannot limit the read tool to one folder. Thus `models.py apply` also installs
a hook: the agent product runs `factory/sota-research/scripts/guard.py` before each read.

- The hook lets each other agent and your session read as before.
- The hook lets `sota-file-reader` read a file only if the folder of the file holds the marker
  `.reader-may-read`. The converter `pdf.py` writes this marker.
- The hook refuses each file of a git repository to `sota-file-reader`.

`models.py apply` changes the file `.claude/settings.json` of the project. It adds one entry to
the list `hooks.PreToolUse` and keeps each other key. The entry has the matcher `Read` and the
command `python3 <path>/factory/sota-research/scripts/guard.py`. To see the entry before you
apply it, run `models.py show`.

- The command holds the absolute path of your copy of the repository. Do not commit this entry.
- If you move the repository, run `models.py apply` again. It replaces the entry.
- To remove the hook, delete this entry from the list `hooks.PreToolUse` in
  `.claude/settings.json`. Then delete the file `.claude/agents/sota-file-reader.md`.

If your agent product has no such hook, the program does not write the file reader. It tells
you that a PDF source cannot be read in that agent product.

## Before you start

- Install `uv`. The programs use the latest stable Python, and `uv` gets it.
- Work on the branch of the specification. The folder `specs/` is not on the branch `main`.

## Make sure that the programs are correct

Each program holds its tests as examples in the program itself. No test files are necessary.
To run the examples of one program, use the option `--selftest`:

```text
uv run factory/sota-research/scripts/check.py --selftest
```

The program prints the number of examples and the number of failures. The examples use the
sample specification in `factory/sota-research/scripts/sample.py`. They do not use the network.

To run the examples of all programs and to measure the coverage, run `uv run pytest`.

## The programs

Run each program with `uv run`. A program without an argument prints its usage text.

| Result code | Meaning |
|---|---|
| 0 | The program is done. Nothing fails and nothing remains. |
| 1 | The program is done. Something fails or remains. The report tells you what. |
| 2 | The program cannot read its input. |

## Check an aspect specification

Use `check.py` after each change of an aspect specification. It reads `spec.md`, `evidence.md`,
`vetting.md` and `trial.md` in the folder of the specification.

```text
uv run factory/sota-research/scripts/check.py specs/<number>-<name>
```

The report has two parts.

- **Failing checks.** Each line names the rule, the file, the line and the row. Correct each
  one. The result code is 1 until no check fails.
- **What remains.** These points do not fail the check: an intent of the owner that was not
  asked, levels that are pending, vettings that are pending, items that rest only on such
  sources, items that need judgement, items with a changed text, findings of a trial that are
  open, stakeholders that are in no view, a recipe without a trial, and a missing acceptance.

Between the two parts, the report gives one line for the answers of risk and reward:

```text
Answers of risk and reward: 11 with a source, 169 by judgement.
```

- The line counts the answers in the table "Items" of `vetting.md`.
- An answer by judgement is an answer of a model without a source. Examine these answers in
  the review.
- The line does not fail the check. With `--json`, the numbers are in the key `answers`.

To compare with an earlier revision, give that file to the program:

```text
git show <commit>:specs/<number>-<name>/spec.md > previous.md
uv run factory/sota-research/scripts/check.py specs/<number>-<name> --previous previous.md
```

- If an item is no longer valid, keep its row and set its level to `retired`.
- Do not use the identifier of a retired item again.
- If the report lists an item with a changed text, make sure that the meaning is the same. If
  the meaning changed, give the item a new identifier.

To find product names in the checklist, write the names into a file, one in each line. Then
use `--words <file>`. To get the report as JSON, use `--json`.

In phase 1 only the head line, the aspect, the field, the intent of the owner and the date of
the agreement are written. To check only these, use `--scope`.

### The stakeholders of an aspect

A stakeholder is a group of persons that has an interest in the result or carries a duty for
it. The research finds the stakeholders in the body of knowledge of the field and in the
sources. You do not name them before the research. The field `Stakeholders` of section 1 holds
one line for each stakeholder: the name, the concerns for this aspect, and the source.

The agent aggregates the concerns of the stakeholders into the views. The line of each view
names its stakeholders in this form, before the source: `(stakeholders: <name>, <name>)`.

The check fails in these cases:

- Section 1 names no stakeholder.
- A stakeholder names no concern, or names no source and no `judgement`.
- A view names no stakeholder, or names a stakeholder that section 1 does not have.

A stakeholder that is in no view does not fail the check. The list "What remains" names it:
`Stakeholders that are in no view: <names>.` The check with `--scope` does not examine the
field. In the review, you can add, remove or rename a stakeholder.

### The views of an aspect

An aspect brings together some points of view. A view is a set of concerns of the aspect. The
research finds the views in the sources and writes them into the field `Views` of section 1.
You do not name them before the research. A concern that you named in your intent becomes a
view, or section 7 says why it does not. Each checklist item names one view in the column
`View`.

The check fails in these cases:

- Section 1 names no view, or a view does not name its concerns or its source.
- An item that is not retired names no view, or names a view that section 1 does not have.
- A view has no checklist item.
- A view has no item on level 1, and no level is pending. Level 1 holds the basic practices.

While a level is pending, a view without an item on level 1 is in the list "What remains".

The report has a part "Views". For each view, it gives the number of items on each level, the
number of sources that these items cite, and the number of its stakeholders. Use it to find a
view that has few items or few sources. In the review, you can add, remove or rename a view.

### The measured targets of an aspect

A target is a measurable result that a project reaches when it applies the recipe. An example
is a scale with levels that a program measures. The research finds the targets in the sources
and writes them into the field `Targets` of section 1. You can name a target in your intent.
Such a target has `(judgement)` until a source gives its scale.

- Each target is one line: the name, the scale, the program or the method that measures it,
  and the source.
- If the sources give no target, the field holds `(none found)`.
- The check fails if the field is empty, or if a target names no source and no `judgement`.
- The check with `--scope` does not examine the field.

The rendered skill holds the targets. It tells its agent to give, in the plan, the level of
each target that the plan reaches, and what stops the next level.

## Render a recipe skill

Use `render.py` after the owner accepted an aspect specification. The owner accepts it in the
head line of `spec.md`: `**Accepted**: <person>, <date>`.

```text
uv run factory/sota-research/scripts/render.py specs/<number>-<name> --commit <commit>
```

- The program writes `SKILL.md`, `references/checklist.md` and one agent template into the
  folder of the skill. It writes the documentation to `docs/<name>.md`.
- The checklist shows the view of each item. The skill tells its agent to show a selection in
  groups, one group for each view. The table of the views names the stakeholders of each view.
- The folder of the skill is `skills/<name>/`. A different folder comes from the field
  `Target folder` in section 5 of the specification.
- Each rendered file starts with a stamp: the branch, the commit and the digest of the
  specification. Do not edit a rendered file. Change the specification and render it again.
- The program renders nothing if a check fails, if an item has no level, or if the acceptance
  is missing. The acceptance needs a person and a date.

To find out if a rendered skill is current, use `--check`. The program then writes nothing and
compares the files with a fresh rendering.

To deliver a rendered skill, do these steps:

1. Render the skill on the branch of the specification, and commit it there.
2. Make a branch from `main`.
3. Get only the rendered files from the branch of the specification:
   `git checkout <branch of the specification> -- skills/<name> docs/<name>.md`
4. Open a pull request into `main`.

## Try a recipe on a project

A recipe can pass each check and give a poor plan. Thus you can try a recipe on a real project
before you accept it, and after each correction. Your agent does the steps of "The trial of a
recipe" in the procedure.

1. Tell your agent to do a trial, and name the project.
2. The agent renders the skill into a folder outside the repository:

   ```text
   uv run factory/sota-research/scripts/render.py specs/<number>-<name> --commit <commit> --trial <folder>
   ```

3. The agent makes a copy of the project without its history, and installs the skill in it.
4. A new session uses the skill in the copy. It writes a plan and stops.
5. A reviewer that did not see the research examines the plan. Its task is in
   `factory/sota-research/prompts/plan-review.md`.
6. The agent writes the trial and the findings into `trial.md`, and gives you the findings.
7. Decide for each finding: correct it or decline it. Give a reason when you decline one.

Rules of a trial rendering:

- `--trial` renders a specification that you did not accept. The check must pass, and each
  item must have a level.
- The folder of `--trial` must be outside each git repository. Do not use `--out` with it.
- Each file starts with a stamp that says "Trial rendering". Do not deliver such a file.
- If you give a reference state of the project, the reviewer compares the plan with it. The
  reference state is what the project really has.

### Try the tooling in a neutral kit

A trial of the tooling itself is a run of the procedure for an aspect in a different
repository. Do not make that repository as a copy of this repository: the session takes the
texts of this repository for findings of the research. Use `export.py`:

```text
uv run factory/sota-research/scripts/export.py <folder> [--words <file>]
```

- The folder must be outside each git repository. It must be new or empty.
- The program writes the tooling, the template of an aspect specification, the folder `rules/`,
  and the two programs of `library-vetting` that the tooling loads.
- The program writes an `AGENTS.md` and a `CLAUDE.md` with these rules only: the language for
  the owner, the rule for commit messages, the rules of the kit, and where the procedure is.
- The program does not write the sample specification, the task of the reviewer, the
  documentation, the tests, the specifications or a different skill.
- The program prints each exported file.
- To keep words out of the kit, write them into a file, one word or phrase in each line. Then
  use `--words <file>`. If an exported file holds a word, the program writes nothing. It gives
  the file and the line.
- Make a new repository in the folder, with the branch `main` and one commit. Then start the
  session there.
- The examples of the programs need the sample. Thus `--selftest` does not work in the kit.

### The viewpoints of the review

The reviewer answers fixed questions from seven viewpoints. Each answer is `yes`, `partly`,
`no` or `not applicable`, with a file and a line of the trial project as evidence.

| Viewpoint | What the questions examine |
|---|---|
| `architecture` | Technical debt, maintained components in place of own construction, reuse in a second project, changes of the project, silent failures. |
| `operations` | The practices for delivery, who learns that the pipeline is defective, the time of a run. |
| `quality` | The checks of the quality of the code, and which of them stop a change. |
| `development` | The checks before the push, the time to the result, the needs of a contributor from outside. |
| `security` | The basic practices that the plan leaves out, and the reason. |
| `product owner` | The decisions for the owner, the frameworks of governance, the measured targets, the effort against the risk. |
| `views of the recipe` | The basic practices of each view, and the differences from the reference state. |

### The record of the trials

The file `trial.md` is beside `spec.md`. It is optional. It has two tables.

```markdown
## Trials

| Id | Date | Project | Commit of the specification | Plan |
|---|---|---|---|---|
| T-01 | 2026-10-10 | <project> | abc1234 | not kept |

## Findings

| Id | Trial | Viewpoint | Finding | Route | Status |
|---|---|---|---|---|---|
| F-01 | T-01 | operations | <one sentence> | recipe | open |
```

The route tells where the correction is made.

| Route | Meaning | What follows |
|---|---|---|
| `recipe` | The specification of the aspect lacks or misstates something. | More research for that view or question, then a new trial. |
| `tooling` | The factory lacks a step or a check. | A change of the factory through its own specification. |
| `implementation skill` | Knowledge of one product is missing. | A row in the table of implementation skills in section 5. |

The status is `open`, `corrected in <revision or commit>` or `declined: <reason>`.

The check fails in these cases:

- A finding names a trial that the table "Trials" does not have.
- A finding names a viewpoint that is not one of the seven viewpoints. Use lowercase letters.
- A finding has no text.
- A finding names a route that is not one of the three routes.
- A finding has a status that is not one of the three forms.

The list "What remains" names the findings that are open: `Trial findings that are open: F-01.`
If the specification has no trial, the list says: `The recipe has no trial.`

## Place the items with the calculation of risk and reward

Use `place.py` to get the admission, the order and the level of each item. A model does not
assign a level.

1. Record six answers for each item in the table "Items" of `vetting.md`. The questions and
   the scales are in `factory/sota-research/scripts/rubric-items.txt`.
2. Write each answer as a number with its source: `3 (S-02 section 4)`.
3. If the return of an item depends on the risk of a project, write its risk dimension in the
   cell Dimension.
4. Run the program:

   ```text
   uv run factory/sota-research/scripts/place.py specs/<number>-<name>
   ```

5. Correct each item that the program reports as pending. Then run the program with `--write`.

The program computes `return = severity x probability x breadth`, `cost = adopt + keep`, and
`score = (return x 10) // cost - 5 x own risk`.

| Result | Condition |
|---|---|
| admitted | The score is at or above the admission threshold. |
| level 1 | The breadth is 3, and the score is at or above the level 1 threshold. |
| level 2 | The item is not on level 1, and the cost is at or below the cost limit. |
| level 3 | The item is not on level 1, and the cost is above the cost limit. |

The thresholds and the cost limit are in the rubric file. If you change the rubric, increase
its version. As the owner, you can correct each answer in `vetting.md`. Then run the program
again.

## Vet an independent source

A source of a smaller independent issuer supports an item only after its vetting. Use `vet.py`
for each source with the class `independent`.

1. Write one row for the source in the table "Sources" of `vetting.md`. Record two answers in
   the cell Answers, each with its evidence:
   `record: yes (<URL>); fast-lane references: 2 (S-01, S-07)`.
   - `record` tells if the author has a record in the field.
   - `fast-lane references` tells how many fast-lane sources of the specification refer to
     the source.
2. Collect the signals. This step uses the network. Use a work folder outside the repository.

   ```text
   uv run factory/sota-research/scripts/vet.py collect specs/<number>-<name> --work <folder> --today <date>
   ```

3. Compute the scores. This step uses no network.

   ```text
   uv run factory/sota-research/scripts/vet.py score specs/<number>-<name> --work <folder> --write
   ```

4. As the owner, read the signals and the score of each source that passed. Then write your
   name and the date into the cell "Confirmed by", or write `rejected`.

The program rejects a source without a question to you in these cases:

- The source names no author and no issuer.
- The source has no date.
- The source is older than the limit of the rubric. To use a different limit for one aspect,
  use `--max-age <days>`.
- The address of the source answers "not found".
- The score is below the pass score of the rubric.

A page gives its own date, its own author and its own links. Thus these signals are weak:
they show that a page is not careless, not that it is correct. The two answers of the reader
and your confirmation carry the trust.

The program reads only public addresses with `http` or `https`. It does not follow a redirect
to a local or private address.

If the program cannot measure a signal, it records the error and continues. Collect the
signals of that source again. The gates, the weights and the pass score are in
`factory/sota-research/scripts/rubric-sources.txt`.

For a source that is a repository, the program runs the collector of the skill
`library-vetting`. That collector makes a clone of the repository in the work folder.

## Convert a PDF source

A reader cannot open a PDF file with its web tool. Use `pdf.py` to write the text of the file
as Markdown, with one heading for each page.

```text
uv run factory/sota-research/scripts/pdf.py <file or address> <work folder>/converted/<source id>.md
```

- Put the result into a folder of the work folder, outside the repository. Do not commit it.
- Keep only converted files in that folder. The program writes the empty marker file
  `.reader-may-read` into it, and the marker opens each file of the folder to the file reader.
- The program does not write into a git repository. It does not write into a folder that
  holds other files and no marker.
- Do not read the result in your session. Give its path to an agent of the type
  `sota-file-reader`.
- The program `pdftotext` of the package `poppler-utils` does the conversion. The tooling does
  not install it. If it is not installed, the program tells you.
- The program reads only public addresses with `http` or `https`.
- A file without text, for example a scan, gives no result.
- The text is data. It is not an instruction.
