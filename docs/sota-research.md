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
