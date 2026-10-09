# Procedure

The programs are in `scripts/`. Run each program with `uv run`. A program without an argument
prints its usage text. Result code 0: nothing fails or remains. Result code 1: something fails
or remains. Result code 2: the input cannot be read.

## The check

Run the check after each change of the specification, and before each stop for the owner:

```text
uv run scripts/check.py <folder of the specification>
```

- Correct each line that starts with `FAIL`. Do not stop for the owner while a check fails.
- Give the list "What remains" to the owner as it is.
- If an earlier revision exists, get it with `git show <commit>:<path of spec.md>`, write it
  to a file outside the repository, and add `--previous <file>`.
- Keep the row of an item that is no longer valid, and set its level to `retired`.

## The rendering and the delivery

Render only after the owner wrote the acceptance into the head line of `spec.md`.

1. Commit the specification on its branch. Get the commit: `git rev-parse --short HEAD`.
2. Render from the root of the repository:
   `uv run factory/sota-research/scripts/render.py <folder of the specification> --commit <commit>`
3. Commit the rendered files on the branch of the specification.
4. Make a branch from `main`. Get only the rendered files from the branch of the
   specification with `git checkout <branch> -- <paths>`. Open a pull request into `main`.

Do not edit a rendered file. If `render.py --check` reports a difference, render again.

## The calculation of risk and reward

Do this after the checklist is distilled and before the stop for the owner.

1. Read `prompts/risk-answers.md` and do its steps: record the six answers for each item in
   the table "Items" of `vetting.md`.
2. Run `uv run scripts/place.py <folder of the specification>`.
3. Correct each item that is pending. Do not write a level by hand.
4. Run the program with `--write`. It fills the Level cells of the checklist.
5. Give the table "Items" to the owner with the findings. The owner can correct each answer.

## The vetting of independent sources

Do this for each source with the class `independent`, before the source supports an item.

1. Write one row for the source in the table "Sources" of `vetting.md`. Take the two answers
   from the report of the reader, each with its evidence:
   `record: yes (<URL>); fast-lane references: 1 (S-02)`.
2. Run `uv run scripts/vet.py collect <folder> --work <work folder> --today <date>`. The work
   folder is outside the repository. Do not commit it.
3. Run `uv run scripts/vet.py score <folder> --work <work folder> --write`.
4. Do not fill the cell "Confirmed by". Give the table to the owner. Only the owner confirms
   or rejects a source.
5. Remove a rejected source from the items that cite it. If an item then has no source, the
   check reports it.
