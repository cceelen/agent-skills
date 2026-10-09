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
