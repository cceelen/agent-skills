# Quickstart: prove that each part works

Run the commands from the root of the repository. The contracts are in
[contracts/programs.md](contracts/programs.md) and [contracts/files.md](contracts/files.md).
`GOOD` is the folder `tests/sota-research/fixture/good`.

## All parts

```text
uv run --python 3.14 pytest tests/sota-research
uv run ruff check
```

Expected: all tests pass, without the network.

## 1. The check (user story 1)

```text
uv run factory/sota-research/scripts/check.py GOOD
```

Expected: "No check fails.", one item that needs judgement, and result code 0. The tests plant
one defect for each rule in a copy of the fixture (the table `DEFECTS` in
`tests/sota-research/test_check.py`); each copy gives exactly its finding and result code 1.

On the branch `001-sota-research`:

```text
uv run factory/sota-research/scripts/check.py specs/001-sota-research
```

## 2. The renderer (user story 2)

```text
uv run factory/sota-research/scripts/render.py GOOD --commit 0000000 --out <empty folder>
```

Expected: the folder holds the same files as `tests/sota-research/fixture/good-rendered`. With
`**Accepted**: pending` in the head line, the program writes nothing and names the missing
acceptance.

## 3. The calculation (user story 3)

```text
uv run factory/sota-research/scripts/place.py GOOD
```

Expected: C-01 and C-05 on level 1, C-02 on `2, operative`, C-03 on `3, regulatory`, C-04 not
admitted, and result code 0. With one answer removed, that item stays `pending` and the result
code is 1.

## 4. The vetting (user story 4)

```text
uv run factory/sota-research/scripts/vet.py score GOOD --work tests/sota-research/fixture/signals
```

Expected: S-03 with 9 of 10 and S-04 with 8 of 10, the two confirmed, and result code 0. With
"Confirmed by" set to `pending` for S-03, `check.py` lists C-04 as an item that rests only on a
source with a pending vetting.

## 5. The research skill (user story 5)

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
| All parts | 201 tests pass on Python 3.14. On Python 3.9 the folder `tests/sota-research` is skipped and the other 99 tests pass. Python 3.13 is not installed on this machine; the CI runs it. |
| 1 to 4 | As expected. |
| The check on the specification 001 | 0.03 seconds (SC-006: less than 10 seconds). It reports five failures: the field `Accepted` is missing, section 1 names no risk dimension in the new form, and three fields of the recipe skill refer to a section. It lists 22 pending levels and 4 pending vettings. |
| 5 | Open. It needs the delivery to `main` and the owner (T044, T045). |
