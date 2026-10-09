# sota-research

`sota-research` is the tooling of the factory. It takes one major aspect of software
engineering from "what to build" to an accepted aspect specification and a rendered recipe
skill. A person stays in the loop: the owner decides what to build, confirms the sources and
accepts the result.

The tooling is in `factory/sota-research/`. Users of the kit do not install it.

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
- The program renders nothing if a check fails or if the acceptance is missing.

To find out if a rendered skill is current, use `--check`. The program then writes nothing and
compares the files with a fresh rendering.

To deliver a rendered skill, do these steps:

1. Render the skill on the branch of the specification, and commit it there.
2. Make a branch from `main`.
3. Get only the rendered files from the branch of the specification:
   `git checkout <branch of the specification> -- skills/<name> docs/<name>.md`
4. Open a pull request into `main`.
