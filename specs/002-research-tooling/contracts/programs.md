# Contract: the programs

All paths are relative to `factory/sota-research/`. `SPEC` is the folder of one specification.
Each program prints its usage text when it gets no argument. Result codes for all programs:
`0` done and nothing fails or remains; `1` done, and something fails or remains; `2` the input
cannot be read. The output is sorted and holds no current time.

## scripts/check.py

```text
check.py SPEC [--previous FILE] [--words FILE] [--json]
check.py SPEC --scope
```

- Reads `SPEC/spec.md`, `SPEC/evidence.md` and, when present, `SPEC/vetting.md` and
  `SPEC/trial.md`.
- `--previous FILE`: an earlier revision of `spec.md`, for the check of stable identifiers.
  Without it, that check is skipped and the report says so.
- `--words FILE`: the word list of products of the aspect, one word in each line.
- Prints one line for each finding: the rule, the place (section and row id) and what is
  wrong. Then the summary: failing checks, pending levels, pending vettings, items that need
  judgement, and whether the specification is accepted.
- `--json`: the same content as one JSON object with sorted keys.
- `--scope`: examines only the head line and the fields of section 1 that are settled before
  the research: the aspect, the field, the intent of the owner and the date of the agreement.
  The report says so.
- The field `Intent of the owner` fails the check when it is absent or empty, and when a line
  has no date and is not `(no answer)`. Under "remains", when each line is `(no answer)`:
  `The intent of the owner was not asked.`
- Outside `--scope`, the field `Stakeholders` fails the check when it has no stakeholder, and
  when a stakeholder names no concern, or no source and no `judgement`. A view fails the check
  when it names no stakeholder, or a stakeholder that section 1 does not have. Under
  "remains": `Stakeholders that are in no view: <names>.` Each line of the part "Views" ends
  with the number of stakeholders of the view.
- After the part "Views", one line: `Answers of risk and reward: <n> with a source, <m> by
  judgement.` It counts the answers in the table "Items" of `SPEC/vetting.md` and fails
  nothing. With `--json`: the key `answers` with `source`, `judgement` and `other`, and the
  key `intent_asked`.
- Result code `1` when a check fails. Pending levels, pending vettings and a missing
  acceptance are listed as "remains" and do not fail the check.
- A finding of `trial.md` with an unknown trial, viewpoint or route, an empty text or a wrong
  status fails the check. Under "remains": `Trial findings that are open: <ids>.`, and
  `The recipe has no trial.` when the specification has no trial.
- The names of the viewpoints come from `references/viewpoints.txt`, one in each line. When
  the file is absent, the viewpoint of a finding is not checked. Under "remains":
  `Trial findings with a viewpoint that was not checked: <ids>. The list is absent.` With
  `--json`: the key `viewpoints` in `remains`.
- Outside `--scope`, the field `Targets` of section 1 fails the check when it has no target
  and not `(none found)`, and when a target names no source and no `judgement`.
- Outside `--scope`, the table "Requirements" of `SPEC/vetting.md` fails the check when it is
  absent or empty; when a cell is empty; when an identifier is used two times; when the cell
  "Goes to" is not `C-<nn>`, `3.3: <decision>`, `5`, `boundary: <name>` or
  `duplicate: R-<nn>`; when the exit names an item, a decision, a boundary or a row that does
  not exist, an item that is retired, or a row that is a duplicate; when a stakeholder or a
  view is not in section 1; and when the source is not in section 2. An item that is not
  retired fails the check when no requirement goes to it and its cell "Admitted by" does not
  start with `own rule`. A stakeholder of section 1 without a requirement fails the check.
- After the part "Views", the part "Requirements": one line for each view with the number of
  requirements and the number for each exit. With `--json`: the key `requirements`. Under
  "remains", one line for each view: `More than half of the requirements of the view '<name>'
  go to a boundary.` With `--json`: the key `boundaries` in `remains`.
- A source of section 2 fails the check when its cell `Views` names a view that section 1
  does not have, or when the table has the cell and it is empty. Each line of the part
  "Views" ends with `sources read for the view: <n>`: the sources with the view in the cell
  `Views`, without `all`, and with `full` or `part` in the cell `Read`. Under "remains":
  `Views with fewer than two sources of their own field that were read: <names>.` With
  `--json`: the key `own-sources` in `remains`.

## scripts/render.py

```text
render.py SPEC --commit HASH [--branch NAME] [--out DIR] [--check]
render.py SPEC --commit HASH --trial DIR [--branch NAME] [--check]
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
- `--trial DIR`: a trial rendering, only into `DIR`. `DIR` must be outside each git
  repository, and `--out` is not permitted with it. The rules of `check.py` must pass and each
  item must have a level, but the acceptance is not necessary. The stamp of each file says
  that the file is a trial rendering. With `--check`, the files in `DIR` are compared with a
  fresh trial rendering.
- Renders nothing when a rendered file refers to a path that starts with `factory/`, `specs/`,
  `.specify/`, `rules/` or `tests/`, uses the word `constitution`, or holds an absolute path
  (`/home/` or a drive letter). Prints one line for each place:
  `Nothing was rendered: a skill must work alone. The file <file> holds '<text>' in line <n>.`

## scripts/export.py

```text
export.py DIR [--words FILE]
```

- Writes a neutral kit for a trial of the tooling into `DIR`. `DIR` must be outside each git
  repository, and must be new or empty.
- The kit holds `factory/sota-research/` without `scripts/sample.py`, without
  `prompts/plan-review.md`, without `references/viewpoints.txt` and without the files that
  Python makes when it runs; the template
  `.specify/templates/overrides/aspect-spec-template.md`; the folder `rules/`;
  `skills/library-vetting/scripts/collect.py` and `models.py`; and an `AGENTS.md` and a
  `CLAUDE.md` that the program makes.
- `--words FILE`: one word or phrase in each line. If an exported file holds one, the program
  writes nothing and prints the file and the line of each use.
- Prints each exported file, sorted. Result code `1` when nothing was exported.

## scripts/seed.py

```text
seed.py list [--manifest FILE]
seed.py get WORK [--file ID=PATH ...] [--from SPEC] [--today DATE] [--fresh] [--manifest FILE]
```

- Reads `references/seeds.md`. `--manifest FILE` gives a different manifest, for tests.
- `list`: prints one line for each seed, sorted: id, kind, version or date, address and
  digest. Then one line for each body of knowledge of a field. A malformed row gives one line
  with the file, the line and the id, and the result code `1`.
- `get`: retrieves each seed into `WORK`, which must be outside each git repository. A file
  is kept as `WORK/seeds/<id>.pdf`, and its text is written to `WORK/converted/<id>.md`
  through the functions of `pdf.py`.
  - Kind `pdf`: downloads the address through `pdf.py`. Kind `owner file`: uses the path of
    `--file ID=PATH`, or the file in `WORK/seeds/`. Kind `page`: records only.
  - `--from SPEC`: also each source of section 2 of `SPEC/spec.md` whose address ends in
    `.pdf`, with the source id as the id.
  - A file that is in `WORK/seeds/` is not retrieved again, and a text with the same digest is
    not converted again. `--fresh` downloads each file of the kind `pdf` again.
  - The digest of the file is compared with the digest of the manifest or, without one, with
    the digest in the `WORK/seeds.json` of the last run. A different digest gives the state
    `changed`; the new file is kept and converted.
  - A seed of the manifest without a digest: the program prints the digest for the row.
  - A seed that fails does not stop the program. Its reason is in the state.
  - Writes `WORK/seeds.json`, with sorted keys and without a current time. `--today DATE`
    gives its date.
- Result code `0`: each seed is `retrieved` or `recorded`. `1`: a seed failed, changed or
  waits for the owner. `2`: the manifest is malformed or cannot be read, or an argument is
  wrong.

## scripts/init.py

```text
init.py KIT WORK [--file ID=PATH ...] [--today DATE] [--again] [--manifest FILE]
```

- `KIT` and `WORK` must be outside each git repository, and neither can be in the other. `KIT`
  must be new or empty.
- In this order: writes the kit of `export.py` into `KIT`; writes `KIT/.factory-kit` with the
  commit of this repository, or `not known`; makes `KIT` a git repository with the branch
  `main` and one commit that names no person; retrieves the seeds into `WORK` as `seed.py get`
  does; prints the next steps for a person.
- Without the program `git`, or when a git command fails, the program says so and continues.
- `--again`: removes a `KIT` that holds `.factory-kit`, and makes it again. `WORK` is kept. A
  folder with files and without the marker is never removed; the program refuses it.
- `--file`, `--today` and `--manifest` are the options of `seed.py get`.
- Result code `0`: the kit is made and each seed is `retrieved` or `recorded`. `1`: the kit is
  made, and a seed failed, changed or waits for the owner. `2`: nothing was made.

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
models.py detect | apply | show   [--host H] [--source-reader M] [--second-reader M]
                                  [--file-reader M] [--root DIR]
```

`apply` writes the three agent files into the project folder of the agent product in this
repository. `show` prints them and writes nothing. The names of the tools and the detection of
the agent product come from `skills/library-vetting/scripts/models.py`. The roles are
`source-reader` (smallest capable model; web search and web fetch), `second-reader`
(mid-size model; web fetch) and `file-reader` (smallest capable model; read).

`apply` also merges one hook entry for `scripts/guard.py` into the settings file of the
project, keeps each other key, and names the file under `written`. The output has
`reads_converted_files`. If the agent product has no such hook, `apply` does not write the
agent file of `file-reader`, and the `note` says that a PDF source cannot be read.

## scripts/guard.py

```text
guard.py < EVENT
```

The hook of the agent product before a call of the read tool. `EVENT` is JSON with
`agent_type`, `tool_name` and `tool_input.file_path`. Result code `0`: the call passes. Result
code `2`: the call is refused, with the reason on the standard error output. A call passes if
`agent_type` is not `sota-file-reader`. A call of `sota-file-reader` passes only for the read
tool, on a file whose resolved folder holds the marker `.reader-may-read` and is not in a git
repository. `scripts/pdf.py` writes the marker.
