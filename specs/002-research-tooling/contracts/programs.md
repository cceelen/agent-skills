# Contract: the programs

All paths are relative to `factory/sota-research/`. `SPEC` is the folder of one specification.
Each program prints its usage text when it gets no argument. Result codes for all programs:
`0` done and nothing fails or remains; `1` done, and something fails or remains; `2` the input
cannot be read. The output is sorted and holds no current time.

## scripts/check.py

```text
check.py SPEC [--previous FILE] [--words FILE] [--json]
```

- Reads `SPEC/spec.md`, `SPEC/evidence.md` and, when present, `SPEC/vetting.md`.
- `--previous FILE`: an earlier revision of `spec.md`, for the check of stable identifiers.
  Without it, that check is skipped and the report says so.
- `--words FILE`: the word list of products of the aspect, one word in each line.
- Prints one line for each finding: the rule, the place (section and row id) and what is
  wrong. Then the summary: failing checks, pending levels, pending vettings, items that need
  judgement, and whether the specification is accepted.
- `--json`: the same content as one JSON object with sorted keys.
- Result code `1` when a check fails. Pending levels, pending vettings and a missing
  acceptance are listed as "remains" and do not fail the check.

## scripts/render.py

```text
render.py SPEC --commit HASH [--branch NAME] [--out DIR] [--check]
```

- Runs the rules of `check.py` first. Renders nothing when a check fails or when the
  specification is not accepted, and prints the reason.
- Writes `SKILL.md`, `references/checklist.md`, `agent-templates/<name>.md` in the target
  folder, and `docs/<name>.md`. The target folder is the one that section 5 names, or
  `skills/<name>/`. `--out DIR` replaces the root of the repository, for tests.
- `--branch`: the branch of the specification for the stamp. The default is the branch field
  in the head of `spec.md`.
- `--check`: writes nothing. Result code `1` when a file differs from a fresh rendering, and
  the names of those files are printed.

## scripts/place.py

```text
place.py SPEC [--write]
```

- Reads the answers in the table "Items" of `SPEC/vetting.md` and `scripts/rubric-items.txt`.
- Prints for each item: return, cost, score, admitted or not, level, and the position.
- `--write`: fills the computed cells of the table "Items" and the Level cells of the
  checklist in `SPEC/spec.md`. Without it, the program changes no file.
- An item with a missing answer stays `pending`, and the report names the answer. Result
  code `1` when an item is pending.
- An item above level 1 without a risk dimension in the cell Dimension of the table "Items"
  stays `pending` and is reported; the program does not choose a dimension.
- `--rubric FILE`: a different rubric file, for tests.

## scripts/vet.py

```text
vet.py collect SPEC --work DIR --today DATE [SOURCE-ID ...]
vet.py score   SPEC --work DIR [--write] [--max-age DAYS] [--rubric FILE]
```

- `collect`: for each independent source of section 2 (or the named ones), measures the
  signals and writes `DIR/<source-id>.json`. Uses the network. A signal that cannot be
  measured is recorded as not measured with the error, and the run continues. For a
  repository it runs the collector of `library-vetting`. `--today` is the date for the age;
  the program does not read the clock.
- `score`: reads the signal files, the recorded answers in the table "Sources" of
  `SPEC/vetting.md` and `scripts/rubric-sources.txt`. Applies the gates, computes the score.
  Uses no network. `--write` fills the table "Sources"; it never fills "confirmed by".
- `--max-age DAYS` replaces the age limit of the rubric for one aspect.
- Result code `1` when a source is not scored, is rejected or is not confirmed.
- `DIR` is a work folder outside the repository or ignored by git. It is not committed.

## scripts/models.py

```text
models.py detect | apply [--scope user|project] | show
```

The same contract as `skills/library-vetting/scripts/models.py`, for the roles
`source-reader` (smallest capable model; web search and web fetch) and `second-reader`
(mid-size model; web fetch).
