# Quickstart: prove that each part works

Run the commands from the root of the repository. The contracts are in
[contracts/programs.md](contracts/programs.md) and [contracts/files.md](contracts/files.md).

## All parts

```text
uv run pytest tests/sota-research
uv run ruff check
```

Expected: all tests pass, without the network.

## 1. The check (user story 1)

```text
python factory/sota-research/scripts/check.py tests/sota-research/fixture/good
python factory/sota-research/scripts/check.py tests/sota-research/fixture/defect-unknown-source
```

Expected: the first command reports no failing check and has result code 0. The second names
the item and the unknown source and has result code 1. Two runs print the same bytes.

On the branch `001-sota-research`:

```text
python factory/sota-research/scripts/check.py specs/001-sota-research
```

Expected: no failing check; the levels and four vettings are listed as "remains".

## 2. The renderer (user story 2)

```text
python factory/sota-research/scripts/render.py tests/sota-research/fixture/good --commit 0000000 --out <empty folder>
```

Expected: the folder holds the same files as `tests/sota-research/fixture/good-rendered`.
With the fixture `not-accepted`, the program writes nothing and names the missing acceptance.

## 3. The calculation (user story 3)

```text
python factory/sota-research/scripts/place.py tests/sota-research/fixture/good
```

Expected: each item has a return, a cost, a score, an admission result and a level that are
the same as the expected values of the fixture. With the fixture `missing-answer`, one item
stays `pending` and the result code is 1.

## 4. The vetting (user story 4)

```text
python factory/sota-research/scripts/vet.py score tests/sota-research/fixture/good --work tests/sota-research/fixture/signals
```

Expected: three sources with the expected scores; one is rejected by a gate; none is
confirmed. Then `check.py` on the same fixture lists the item that rests on an unconfirmed
source.

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
