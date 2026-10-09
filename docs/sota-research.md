# sota-research

`sota-research` is the tooling of the factory. It takes one major aspect of software
engineering from "what to build" to an accepted aspect specification and a rendered recipe
skill. A person stays in the loop: the owner decides what to build, confirms the sources and
accepts the result.

The tooling is in `factory/sota-research/`. Users of the kit do not install it.

## The four phases

| Phase | What occurs | Your part as the owner |
|---|---|---|
| 1. What to build | The agent settles the aspect, its contexts, its risk dimensions and its boundaries with you. | You decide the scope. |
| 2. Research | Isolated readers read the sources. The agent distils the strategy and the checklist. Programs vet the sources and place the items. | None. |
| 3. Review | The agent stops and gives you the findings. | You confirm the sources, correct the answers and accept the result. |
| 4. Rendering | A program renders the recipe skill. A pull request delivers it. | You review the pull request. |

To start, tell your agent to read `factory/sota-research/SKILL.md` and to distil an aspect.
The steps of the agent are in `factory/sota-research/references/procedure.md`.

The readers of sources are agents with web tools only. They have no shell, no file tools and
no credentials. Before the first run, write their agent files:

```text
uv run factory/sota-research/scripts/models.py apply
```

If your agent product cannot limit the tools of an agent, the program tells you. Do not start
a research run with that agent product.

## Before you start

- Install `uv`. The programs use the latest stable Python, and `uv` gets it.
- Work on the branch of the specification. The folder `specs/` is not on the branch `main`.

## The programs

Run each program with `uv run`. A program without an argument prints its usage text.

| Result code | Meaning |
|---|---|
| 0 | The program is done. Nothing fails and nothing remains. |
| 1 | The program is done. Something fails or remains. The report tells you what. |
| 2 | The program cannot read its input. |

## Check an aspect specification

Use `check.py` after each change of an aspect specification. It reads `spec.md`, `evidence.md`
and `vetting.md` in the folder of the specification.

```text
uv run factory/sota-research/scripts/check.py specs/<number>-<name>
```

The report has two parts.

- **Failing checks.** Each line names the rule, the file, the line and the row. Correct each
  one. The result code is 1 until no check fails.
- **What remains.** These points do not fail the check: levels that are pending, vettings that
  are pending, items that rest only on such sources, items that need judgement, items with a
  changed text, and a missing acceptance.

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

## Render a recipe skill

Use `render.py` after the owner accepted an aspect specification. The owner accepts it in the
head line of `spec.md`: `**Accepted**: <person>, <date>`.

```text
uv run factory/sota-research/scripts/render.py specs/<number>-<name> --commit <commit>
```

- The program writes `SKILL.md`, `references/checklist.md` and one agent template into the
  folder of the skill. It writes the documentation to `docs/<name>.md`.
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
