# sota-research

`sota-research` is the tooling of the factory. It takes one major aspect of software
engineering from "what to build" to an accepted aspect specification and a rendered recipe
skill. A person stays in the loop: the owner decides what to build, confirms the sources and
accepts the result.

The tooling is in `factory/sota-research/`. Users of the kit do not install it.

## The four phases

| Phase | What occurs | Your part as the owner |
|---|---|---|
| 1. What to build | The agent asks for your intent. Then it settles only the field and the thing to build with you. | You answer three questions. You name the field and the thing. You confirm or correct the charter that the agent drafted. |
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

## The seeds of the factory

A seed is a document or a standard that the factory starts from. An example is the body of
knowledge of a field. The manifest `factory/sota-research/references/seeds.md` names each seed:
the document, the issuer, the version, the kind, the address, the digest and the terms. The
repository holds no seed document.

| Kind | What `seed.py get` does |
|---|---|
| `pdf` | It downloads the file from its public address and converts it. |
| `owner file` | It uses the file that you give with `--file <id>=<path>`, and converts it. If you run the program in a terminal without that option, it shows the page of the issuer and the terms, and asks for the path. |
| `page` | It only records the seed. A web reader reads the page. |

To see the seeds, run `seed.py list`. To retrieve them, run `seed.py get`:

```text
uv run factory/sota-research/scripts/seed.py list
uv run factory/sota-research/scripts/seed.py get <work folder> [--file <id>=<path>] [--from <folder of a specification>] [--today <date>] [--fresh]
```

- The work folder must be outside each git repository. Do not commit it.
- The program keeps each file in `<work folder>/seeds/`. It writes the text to
  `<work folder>/converted/<id>.md`, with one heading for each page.
- Do not read a converted file in your session. Give its path to an agent of the type
  `sota-file-reader`.
- The program writes `<work folder>/seeds.json`: for each seed the files, the digest, the
  number of pages and the state.
- At its end, the program builds the index `<work folder>/index.sqlite` of the converted files.
  See "Find pages in the converted documents".
- If a file is in the work folder already, the program does not retrieve it again. To
  download each file again, use `--fresh`.
- With `--from`, the program retrieves also each source of section 2 of that specification
  whose address ends in `.pdf`.
- If one seed fails, the program records the reason and continues.
- Obey the terms of each seed. Do not give a file or its converted text to a different person
  if the terms do not permit it.

| State | Meaning | What you do |
|---|---|---|
| `retrieved` | The file and its text are in the work folder. | Nothing. |
| `recorded` | The seed is a web page. | Nothing. A web reader reads it. |
| `owner must give the file` | The file is behind a form or a payment. | Get the file from the address. Run the program again with `--file`. |
| `changed` | The digest is not the digest of the manifest or of the last run. The document has a new version, or it was altered. | Read the page of the issuer. Then correct the row of the manifest. |
| `failed: <reason>` | The program did not get the file or its text. | Read the reason. Run the program again. |

The result code is 0 when each seed is retrieved or recorded. It is 1 when a seed failed,
changed or waits for you. It is 2 when the arguments are wrong.

If the manifest has no digest for a seed, the program prints the digest. Write it into the row.

To add a seed, your agent reads the page of the issuer and writes the row with the version and
the date of that page. The agent does not write a row from memory. You accept each new row.

## Set up the factory again

`init.py` makes a neutral environment of the factory from nothing: a kit, a git repository in
it, and the seeds.

```text
uv run factory/sota-research/scripts/init.py <kit folder> <work folder> [--file <id>=<path>] [--today <date>] [--again]
```

1. The program writes the neutral kit into the kit folder, as `export.py` does.
2. It writes the marker file `.factory-kit` into the kit folder, with the commit of this
   repository.
3. It makes the kit folder a git repository with the branch `main` and one commit. The commit
   names no person. If `git` is not installed, the program tells you and continues.
4. It retrieves the seeds into the work folder, as `seed.py get` does.
5. It retrieves the catalogues into the work folder, as `catalog.py get` does.
6. It prints your next steps.

- The two folders must be outside each git repository. Do not put one into the other.
- The kit folder must be new or empty.
- To make a kit again, use `--again`. The program removes the kit folder only if it holds the
  marker file. It does not remove a different folder.
- `--again` keeps the work folder. The program does not download a seed two times.
- The kit holds no seed document and no converted text.

## A created skill works alone

You can use your personal environment and this repository when you operate the factory. A
skill that the factory creates must work without them: a user installs only the folder of the
skill.

- `render.py` renders nothing if a rendered file refers to a path that starts with `factory/`,
  `specs/`, `.specify/`, `rules/` or `tests/`.
- It renders nothing if a rendered file uses the word `constitution` or holds an absolute path.
- The program gives the file, the line and the text. Correct the specification, then render
  again.
- The rules of the kit are text in each skill. The skill does not load them from this
  repository.
- In a trial, the trial project gets only the folder of the rendered skill.
- Start the session of a trial in a clean environment: no personal plugin, connector, skill or
  instruction file.

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
  open, findings with a viewpoint that was not checked, stakeholders that are in no view, a recipe without a trial, and a missing acceptance.
  A view that the boundaries emptied and a view with few sources of its own field are in this
  list also. A boundary that waits for your decision is in this list also: see "The boundaries
  of an aspect". A source with pages that no reader got and an absent table "Reading" are in this
  list also: see "The pages that the readers got".

To compare with an earlier revision, give that file to the program:

```text
git show <commit>:specs/<number>-<name>/spec.md > previous.md
uv run factory/sota-research/scripts/check.py specs/<number>-<name> --previous previous.md
```

- If an item is no longer valid, keep its row and set its level to `retired`.

To compare the register of the requirements with the reports of the readers, add the work
folder of the research:

```text
uv run factory/sota-research/scripts/check.py specs/<number>-<name> --index <work folder>
```

- The check fails for a requirement line of the index that has no row in the register.
- The check fails for a row that has no requirement line with the same source and words.
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

Each source of section 2 names, in the cell `Views`, the views that it was read for. A body of
knowledge has `all` there. The last number of a line of the part "Views" counts the sources
that were read for the view, without the sources with `all`. If this number is less than two,
the list "What remains" names the view:
`Views with fewer than two sources of their own field that were read: <names>.`
The check fails for a cell `Views` that is empty or names a view that section 1 does not have.

### The requirements of the sources

A requirement is a thing that a source says a project must or should do. The agent writes each
requirement into the table "Requirements" of `vetting.md`. It does not judge a requirement
there. The columns are Id, Requirement, Stakeholder, View, Source and Goes to.

The cell `Goes to` holds the one exit of the requirement:

| Form | Meaning |
|---|---|
| `C-<nn>` | The checklist item that holds the requirement. The ladder places the item. |
| `5` | The requirement is knowledge of one product, for an implementation skill. |
| `boundary: <name>` | A neighbouring aspect owns the requirement. The name is a boundary of section 1 that you decided. |
| `duplicate: R-<nn>` | A second source states the same requirement. The row that it names is not a duplicate. |

A requirement does not go to a decision of section 3.3. A decision tells how a practice is
done, not if it is done.

The check fails in these cases:

- The table is absent or has no row, or a cell is empty.
- The cell `Goes to` has a different text, or names a row that does not exist.
- A requirement goes to a retired item.
- A stakeholder, a view or a source of a requirement is not in the specification.
- No requirement goes to an item, and the cell `Strongest source` of the item is not `own rule`.
- A stakeholder of section 1 has no requirement.

The report has a part "Requirements". For each view, it gives the number of requirements and
the number for each exit. If more than half of the requirements of a view go to a boundary,
the list "What remains" says so. Examine such a view in the review. With `--json`, the numbers
are in the key `requirements`.

### The boundaries of an aspect

A boundary says what a neighbouring aspect owns. A requirement that goes to a boundary leaves
the aspect. Thus only you decide a boundary. The agent proposes it.

Each boundary of section 1 has its state in its line:

| Form | Meaning |
|---|---|
| `(proposed)` | The agent proposes the boundary. No requirement goes to it. |
| `(decided by the owner on <YYYY-MM-DD>)` | You decided the boundary on that date. A requirement can go to it. |

A line without a state is proposed. For each proposed boundary, the agent writes one row into
the table "Proposed boundaries" of `vetting.md`. The columns are Boundary, Requirements that it
would take, Stakeholders that it would leave with no requirement, and Reason.

In the review, you get this table directly after your intent, the stakeholders and the views.
Decide or decline each boundary. If you decide a boundary, the agent writes the state with the
date and changes the exit of the requirements that the boundary takes. If you decline a
boundary, the agent removes it.

The check fails in these cases:

- A requirement goes to a boundary that you did not decide.
- A state has a different form, or a decided state has no date.
- A proposed boundary has no row in the table.
- A row names a boundary that section 1 does not have, or a boundary that you decided.
- A row names a requirement that the table "Requirements" does not have.

The list "What remains" names each boundary that waits for your decision, with the number of
requirements that it would take:
`Boundaries that wait for the decision of the owner: <name> (<n> requirements).`
It has one line for each stakeholder that a proposed boundary would leave with no requirement
in the aspect. Each line of the part "Requirements" ends with the number of requirements of
the view that a proposed boundary would take. With `--json`, the keys are `proposed-boundaries`
and `left-stakeholders` in `remains`.

### The charter of an aspect

The charter is the "why" of an aspect: your target, your principles with their priority, and
your constraints. The file is `charter.md`, beside `spec.md`. It is optional. Its template is
`.specify/templates/overrides/charter-template.md`.

- The agent drafts the charter in phase 1, from what you say in the session.
- Each row names your words that it comes from. The agent writes no row without your words.
- The agent proposes the sentence of each principle, the order, and how you can check it.
- The agent gives you the draft before the research starts. Confirm it or correct it.
- You decide the order of the principles. The agent shows what the order decides.
- If you did not confirm the order, the review gives you each case that the order decided.
- If you state a new principle later, the agent adds it as a proposal and asks you.
- The agent reads the charter before the triage of the requirements.
- A principle with a lower number decides when two requirements disagree.
- In the review, you get the charter first, with the facts for each principle.
- Only you change the charter.

No program reads the charter.

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
   The copy gets only the folder of the rendered skill.
4. A new session uses the skill in the copy, in a clean environment. It writes a plan and
   stops.
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
- The program does not write the sample specification, the task of the reviewer, the list of
  the viewpoints of the review, the documentation, the tests, the specifications or a
  different skill.
- The kit holds the manifest of the seeds. It holds no seed document.
- The program prints each exported file.
- To keep words out of the kit, write them into a file, one word or phrase in each line. Then
  use `--words <file>`. If an exported file holds a word, the program writes nothing. It gives
  the file and the line.
- Make a new repository in the folder, with the branch `main` and one commit. Then start the
  session there. `init.py` does the export, the repository and the seeds in one step.
- The examples of the programs need the sample. Thus `--selftest` does not work in the kit.

### The viewpoints of the review

The reviewer answers fixed questions from eight viewpoints. Each answer is `yes`, `partly`,
`no` or `not applicable`, with a file and a line of the trial project as evidence.

| Viewpoint | What the questions examine |
|---|---|
| `integrity` | For each asset, from the source to the system and the data of the user: who can change it without a trace, what shows the change, where the chain of evidence ends. |
| `architecture` | Technical debt, maintained components in place of own construction, reuse in a second project, changes of the project, silent failures. |
| `operations` | The practices for delivery, who learns that the pipeline is defective, the time of a run. |
| `quality` | The checks of the quality of the code, and which of them stop a change. |
| `development` | The checks before the push, the time to the result, the needs of a contributor from outside. |
| `security` | The basic practices that the plan leaves out, and the reason. |
| `product owner` | The decisions for the owner, the frameworks of governance, the measured targets, the effort against the risk. |
| `views of the recipe` | The basic practices of each view, and the differences from the reference state. |

The names of the viewpoints are in `factory/sota-research/references/viewpoints.txt`, one in
each line. A neutral kit does not hold this file and the task of the reviewer: a session of
the research must not see them.

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
- A finding names a viewpoint that is not one of the eight viewpoints. Use lowercase letters.
  In a neutral kit, the check does not examine the viewpoint. The list "What remains" then
  says: `Trial findings with a viewpoint that was not checked: F-01. The list is absent.`
- A finding has no text.
- A finding names a route that is not one of the three routes.
- A finding has a status that is not one of the three forms.

The list "What remains" names the findings that are open: `Trial findings that are open: F-01.`
If the specification has no trial, the list says: `The recipe has no trial.`

## Place the items with the ladder

Use `place.py` to get the value, the order and the level of each item. A model does not assign
a level, and it answers no question about harm or cost.

1. Give each source its class in section 2 of `spec.md`. Give a law or a regulation the class
   `regulation`, and a framework of governance or of audit the class `governance`.
2. Run the program:

   ```text
   uv run factory/sota-research/scripts/place.py specs/<number>-<name>
   ```

3. Run the program with `--write`. It fills the cells `Level` and `Strongest source`.

The ladder is in `factory/sota-research/scripts/rubric-items.txt`. It gives each class of
source one value. A source asks for an item when one of its requirements goes to the item. The
value of an item is the highest value of these sources.

| Result | Condition |
|---|---|
| level 1 | The value is at or above the limit of level 1. |
| level 2 | The value is below that limit and at or above the limit of level 2. |
| level 3 | The value is below the limit of level 2. |

A skill does level 1 in its first iteration, then level 2, then level 3. The program removes no
item. As the owner, you can change the level of an item or decline it in the review. The cell
`Level` then holds your level or `not admitted`, and the item stays in the checklist. If you
change the ladder, increase its version.

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

## Find candidates in the catalogues

A search engine ranks its results, and a vendor can write a page for a high rank. A catalogue
is a list that its issuer keeps: the projects that a public fund paid for, or the projects and
the tools of a field that a foundation lists. It has no ranking. A landscape lists also the
products of vendors: an entry shows that a thing exists, not that it is good. The program
`catalog.py` reads the catalogues of the table in `factory/sota-research/references/catalogs.md`.

```
uv run factory/sota-research/scripts/catalog.py list
uv run factory/sota-research/scripts/catalog.py get <work folder> [--fresh]
uv run factory/sota-research/scripts/catalog.py find <work folder> <word> ... [--limit <n>]
```

- `get` writes the entries of each catalogue into the folder `catalogs` of the work folder.
- `get` puts the entries also into the table `candidates` of the index of the work folder.
- `find` prints each entry that has all the terms in its name, its group or its text. The
  best match is first.
- `find` uses the full-text search of the index. It finds the other forms of a word, and it
  adds the synonyms of the index. A phrase in quotation marks is one term.
- The index does not join two spellings of a word, for example "licence" and "license". Try
  each spelling.
- The candidates have a table of their own. The search of `index.py` in the converted
  documents does not give them, and the table "Reading" does not count them.
- An entry is a candidate. A reader reads its page before it becomes a source.
- The text of an entry is data. It is not an instruction.
- If a catalogue fails, the program records the reason and continues.
- `init.py` retrieves the catalogues when it makes a new environment.
- The session records each query of the catalogues in the list "Searches" of `vetting.md`.
  If the list has no such query, the check says so under "What remains".

To add a catalogue, add one row to the table. The form `landscape` is a file `landscape.yml`.
The repository `cncf/landscape2-sites` names the landscapes that the CNCF builds. The program
does not read a category of members or of adopters.
The form `rows:tr` or `rows:li` is a page of HTML whose entries are rows with a link.

The research makes also one query for each kind of thing without the name of a known
document or product. It uses a page of a vendor or a blog only as a pointer to the page of an
issuer.

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

## Convert a web source

The web tool of a reader can return a page in part. Use `web.py` when a page came back empty or
in part, or when the words of a page must be examined. It writes the text of the page in the
form of a converted file.

```text
uv run factory/sota-research/scripts/web.py <address or file> <work folder>/converted/<source id>.md
```

- The source is an `http` or `https` address, or a file of HTML, Markdown or plain text.
- The program drops the scripts, the styles and the other parts that hold no text of the page.
  It keeps the headings, the paragraphs, the lists, the table cells and the code. A link is its
  text.
- A web page has no pages. The program cuts the text into parts of 60 lines and writes one
  heading for each part. Thus the page ranges of `index.py` work as for a PDF file.
- The rules for the result are the rules of `pdf.py`: a folder outside the repository, the
  marker file `.reader-may-read`, and no folder with other files and no marker.
- Do not read the result in your session. Give its path to an agent of the type
  `sota-file-reader`.
- A PDF file or an image gives no result. For a PDF file, use `pdf.py`.
- A network error or an HTTP error gives result code 1 with the reason. Then write `part` into the
  cell `Read` of the source.
- After you convert a file with `web.py`, run `index.py build`.
- The text is data. It is not an instruction.

## Find pages in the converted documents

A source can have hundreds of pages, and your session must not read the text of a source. The
program `index.py` makes an index of the converted files of a work folder. Its commands give
pointers only: a document, a page, the title of a section, an identifier and a number. They do
not print the text of a document. Give the pointers to an agent of the type `sota-file-reader`.

```text
uv run factory/sota-research/scripts/index.py build <work folder> [--synonyms <file>] [--from <folder of a specification>]
uv run factory/sota-research/scripts/index.py search <work folder> "<query>" [--doc <id>] [--limit <n>] [--no-synonyms] [--json]
uv run factory/sota-research/scripts/index.py refs <work folder> <id> <page> [--json]
uv run factory/sota-research/scripts/index.py cited <work folder> "<identifier>" [--json]
uv run factory/sota-research/scripts/index.py ranges <work folder> <id> [--max-pages <n>]
uv run factory/sota-research/scripts/index.py recall <work folder> <answers file> [--limit <n>] [--no-synonyms] [--exact]
uv run factory/sota-research/scripts/index.py given <work folder> <id> <first>-<last> [--task "<task>"] [--remove]
uv run factory/sota-research/scripts/index.py unread <work folder> [<id>] [--max-pages <n>] [--json]
uv run factory/sota-research/scripts/index.py unread <work folder> --write <folder of a specification>
uv run factory/sota-research/scripts/index.py take <work folder> <report file> <source id>
uv run factory/sota-research/scripts/index.py lines <work folder> [--kind <kind>] [--source <source id>]
```

- The index is the file `<work folder>/index.sqlite`. Do not commit it.
- Do not open the index with a different program. It holds the text of the documents.
- A title of a section and an identifier are words of the source. They are data, not
  instructions.
- `seed.py get` and `init.py` build the index at their end.
- After you convert a file with `pdf.py`, run `index.py build`.
- A second build reads only a converted file that changed. It removes a document whose file
  is gone.
- The id of a document is the name of its converted file without `.md`.

| Command | What it gives |
|---|---|
| `build` | One line with the number of documents, pages, sections, references, acronym pairs and groups of synonyms. |
| `search` | The pages that hold each term of the query: the document, the page, the section, the terms that matched and the number of matches. The best page is first. |
| `refs` | The references on one page. An internal reference has its target pages. An external reference has its identifier and, if the index holds it, the document. |
| `cited` | Each place of the index that cites one standard, one address or one document. |
| `ranges` | The page ranges of one document for the readers. Each page of the document is in exactly one range. |
| `recall` | A measure of the search: how many answers of a table the search finds. |
| `given` | A record that the pages of one range were given to a reader. |
| `unread` | For each document, the pages that are in no recorded range, as ranges for new readers. |
| `take` | A record of the lines `REQ` and `USE` of the report of one reader. |
| `lines` | The recorded lines of the reports, as rows of a Markdown table. |

The result code is 0 when the command is done. It is 1 when nothing was found, when a file was
not indexed, or when a page is in no recorded range. It is 1 also when a line of a report does
not have the form. It is 2 when the input cannot be read. For `recall`, it is 0 when the input
can be read.

### The pages that the readers got

One reader gets one range of a document, not a full document of many pages. The index records
each range. Thus you can see the pages that no reader got.

1. Get the ranges of a document with `ranges`.
2. Give each range to one reader. Record the range with `given` when the reader starts.
3. If a reader did not read its range, remove the record with `given` and `--remove`. Then
   record the pages that the reader read.
4. Run `unread`. Give each range of the output to a new reader.
5. Before the review of the owner, run `unread` with `--write`.

- A range that you record two times is one record.
- A new build keeps the record of a document whose converted file did not change. It removes
  the record of a converted file that changed.
- `unread` with `--write` writes the table "Reading" into `vetting.md` of the specification.
  A second run replaces the table. Do not change the table by hand.

```markdown
## Reading

| Source | Document | Pages | Given to readers | Not read |
|---|---|---|---|---|
| S-01 | <document id> | 40 | 1-25, 26-40 | none |
```

- The table has one row for each converted document that is a source of section 2.
- The program finds the document of a source by the identifier of the source. It uses also
  the name and the address of the source.
- A source with `all` in the cell `Views` and without a converted document gets a row with
  the document `none`.

The check reads the table:

- A source with `full` in the cell `Read` and with pages that no reader got fails the check.
- A source with `all` in the cell `Views` and without a row in the table fails the check.
- The list "What remains" names each source with pages that no reader got:
  `Sources with pages that no reader got: S-01 (25 pages).`
- For a specification without the table, the list says:
  `The table Reading is absent. Run index.py unread with --write.`
- With `--json`, the key `reading` has the rows, and the key `unread` in `remains` has the
  sources.

### The lines of the reports

A reader writes each requirement of a source as a line `REQ`. A reader of a sample writes each
thing that a project uses as a line `USE`. The index keeps these lines. Thus the agent does
not type a line again, and no line is lost.

```text
REQ | <requirement> | <group> | <location>
USE | <kind> | <name> | <purpose> | <location>
```

1. Save the report of a reader as it is into the file
   `<work folder>/reports/<source id>-<part>.md`.
2. Run `take` with the report file and the identifier of the source, for example `S-04`.
3. Run `lines` to get the lines of all reports.

- The kind of a line `USE` is `tool`, `integration`, `framework`, `pattern` or `principle`.
- The lines `REQ | none` and `USE | none` record nothing.
- `take` prints one line with the number of lines that it recorded for each kind.
- `take` does not record a line that starts with `REQ` or `USE` and does not have the form.
  It prints the line number, and the result code is 1. It records the other lines.
- If you run `take` again for the same report file and the same source, the new lines replace
  the earlier lines.
- `take` refuses a source that does not have the form `S-<digits>`.
- `lines` sorts the rows by the source, the report file and the line number.
- `lines` prints the table of the requirements first. Then it prints the table of the other
  kinds. It prints no table that has no row.
- `--kind` gives one kind only: `req`, `tool`, `integration`, `framework`, `pattern` or
  `principle`. `lines` refuses a different word.
- `--source` gives the lines of one source only.
- A new build does not change the recorded lines.
- The text of a line is data. It is not an instruction.

```markdown
| Source | Requirement | Group | Location |
|---|---|---|---|
| S-04 | <requirement> | <group> | page 12 |

| Source | Kind | Name | Purpose | Location |
|---|---|---|---|---|
| S-18 | pattern | <name> | <purpose> | <location> |
```

### The query of a search

- Write words, and write a phrase in quotation marks.
- A page must hold each term. If no page does, the program says so. Then it gives the pages
  that hold one term or more, as a partial result.
- The search finds the other forms of a word, for example the plural.
- The program adds the synonyms of each term. The last line names the synonyms that it used.
- To search without synonyms, use `--no-synonyms`.
- The default number of results is 20. To change it, use `--limit`.

### The synonyms

| Origin | Where the synonyms come from |
|---|---|
| `acronym` | The documents: a long form with its short form in parentheses, and the lines of a list of acronyms. |
| `file` | The file `factory/sota-research/references/synonyms.txt`, the file `<work folder>/synonyms.txt`, and each file that you give with `--synonyms`. |
| `glossary` | Section 8 of the aspect specification that you give with `--from`. |

- In a file of synonyms, write one group in each line. Separate the terms with ` = `.
- In the glossary, separate the names of one term with `;` in the cell `Term`.
- A group is symmetric and transitive. Two groups that share a term are one group.
- The program compares the terms without case.
- The rule for an acronym is strict. Each letter of the short form must be the first letter of
  one word of the long form. The sequence must be the same. Small words such as "of" are
  ignored.
- One short form can have two long forms. Then the two long forms are in one group.

### The sections and the references

The program finds a section with three fixed patterns. It records the pattern of each section.
It does not guess.

| Pattern | The line of the heading |
|---|---|
| `chapter` | `CHAPTER 5`, `Chapter 5: Title` or `Appendix A`, with the title line that follows. |
| `numbered` | `3.2 Title` or `3.2. Title`, when the number follows the heading before it. |
| `capitals` | A line in capital letters with a word of five or more letters. |

- A page of a table of contents gives no section. A running head gives no section.
- A document without a found section gets one section for all its pages.
- The title of a section is one line. A long title can be cut.
- A page with two columns has the text of the two columns in each line. The program puts the
  columns in sequence. A phrase that goes from one column to the next can be lost.

| Kind | Family | Example |
|---|---|---|
| `internal` | `section`, `chapter`, `page`, `table`, `figure` | "Section 3.2", "Chapter 5", "page 12", "Table 4", "Figure 2" |
| `internal` | `name` | the title of a chapter after "see" |
| `external` | `ISO/IEC/IEEE`, `NIST`, `FIPS`, `RFC`, `EN`, `MIL`, `DO` | "ISO/IEC/IEEE 12207", "IEEE Std 1012", "NIST SP 800-218", "RFC 2119" |
| `external` | `address`, `doi` | an address with `http` or `https`, "doi:10.1000/182" |
| `external` | `citation` | "[12]", when the list of references of the chapter has a line that starts with "[12]" |
| `external` | `document` | a name of a document of the index, in a different document |

- An internal reference has its target pages when the target is in the document.
- The page of a reference such as "page 12" is the page of the converted file.
- The year of a standard and the word "Std" make no difference: "IEEE Std 1012-2016" is
  "IEEE 1012".
- The program knows the names of a document from three places: the head lines of the converted
  file, the manifest of the seeds, and section 2 of the specification of `--from`.
- An external reference that names a document of the index points at that document. Thus
  `cited` connects the documents with each other.
- To add a family of standards, add one row to the table `STANDARDS` in the program.

### The ranges for the readers

- Give each range of `ranges` to one file reader. Then no part of a long document is lost.
- A section that fits into `--max-pages` (default 25) is one range.
- A section that is too long is divided at its sections, or at page borders.
- Short ranges that are neighbours are joined.

### Measure the search

Write a table of answers in a Markdown file. A row has a query, a document and the pages that
answer the query:

```markdown
| Query | Document | Pages |
|---|---|---|
| end user | swebok | 48, 55-57 |
```

`recall` runs the search for each row. A row is found when one of its pages is in the first
results (default 10). The page before and the page after are accepted also, because a page
border of a converted file is not exact. To switch this off, use `--exact`. The program prints
the number of rows found, the share, and each row that was not found.
