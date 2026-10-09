# Quickstart: prove that each part works

Run the commands from the root of the repository. The contracts are in
[contracts/programs.md](contracts/programs.md) and [contracts/files.md](contracts/files.md).

## All parts

```text
uv run pytest
uv run ruff check
```

Expected: all tests pass, without the network. On Python 3.14, `tests/test_repo.py` runs each
program of `factory/` with `--selftest` under coverage and fails below 95 percent.

## One program

Each program holds its tests as examples and validates itself:

```text
uv run factory/sota-research/scripts/check.py --selftest
uv run factory/sota-research/scripts/render.py --selftest
uv run factory/sota-research/scripts/place.py --selftest
uv run factory/sota-research/scripts/vet.py --selftest
uv run factory/sota-research/scripts/models.py --selftest
uv run factory/sota-research/scripts/aspect.py --selftest
```

Expected for each: the number of examples, "0 failed", and result code 0. The examples use the
sample specification in `factory/sota-research/scripts/sample.py`.

| User story | Program | What its examples prove |
|---|---|---|
| 1 | `check.py` | The sample passes. Each rule has an example with a planted defect, in the function of that rule. What remains does not fail the check. |
| 2 | `render.py` | The sample gives four files with the stamp. Nothing is rendered without the acceptance, with a failing check or with a pending level. |
| 3 | `place.py` | The limits of the calculation: admission at 20, level 1 at 40 with a breadth of 3, level 3 above a cost of 4. A write changes only its cells. |
| 4 | `vet.py` | The scores of the sample, each gate, and a collection that records each error and continues. |
| 5 | `models.py` | The two readers get web tools only. |

## On a real specification

On the branch `001-sota-research`:

```text
uv run factory/sota-research/scripts/check.py specs/001-sota-research
```

## The research skill (user story 5)

One trial run with the owner on a small aspect, on a new specification branch:

1. The session reads `factory/sota-research/SKILL.md`.
2. The owner is asked for the aspect, its contexts, its risk dimensions and its boundaries
   before the first search.
3. The readers run with web tools only.
4. The run stops for the review. `check.py` reports no failing check, and "not accepted"
   remains.

Expected: the owner was asked for decisions only (SC-005), and a reviewer finds no line in the
evidence record that says more than its source (SC-007).

## Results

Recorded on 2026-10-09, on the working branch, before the delivery to `main`.

| Scenario | Result |
|---|---|
| All parts | 671 examples in 7 programs, 0 failed. Each line has an example; the coverage with branches is 99 percent. On Python 3.9 the examples are skipped and the other tests pass. |
| The check on the specification 001 | 0.03 seconds (SC-006: less than 10 seconds). It reports five failures: the field `Accepted` is missing, section 1 names no risk dimension in the new form, and three fields of the recipe skill refer to a section. It lists 22 pending levels and 4 pending vettings. |
| The research skill | Open. It needs the delivery to `main` and the owner (T044, T045). |
