# Contract: the programs

All paths are relative to `factory/sota-research/`. `SPEC` is the folder of one specification.
Each program prints its usage text when it gets no argument. Result codes for all programs:
`0` done and nothing fails or remains; `1` done, and something fails or remains; `2` the input
cannot be read. The output is sorted and holds no current time.

## scripts/check.py

```text
check.py SPEC [--previous FILE] [--words FILE] [--index WORK] [--json]
check.py SPEC --scope
```

- Reads `SPEC/spec.md`, `SPEC/evidence.md` and, when present, `SPEC/vetting.md` and
  `SPEC/trial.md`.
- `--previous FILE`: an earlier revision of `spec.md`, for the check of stable identifiers.
  Without it, that check is skipped and the report says so.
- `--words FILE`: the word list of products of the aspect, one word in each line.
- `--index WORK`: the work folder of the research. The check compares the table
  "Requirements" with the requirement lines of the index: a line without a row fails, and a
  row without a line with the same source and words fails. A folder without an index fails.
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
  key `intent_asked`. Then, when there are such items, the line `Items with a severity or a
  probability by judgement. Each one is a question for the owner: <ids>.` and the line `Items
  whose level rests on judgement only: <ids>.`
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
- Outside `--scope`, the table "Reading" of `SPEC/vetting.md` is examined. Rule
  `full-with-unread-pages`: a source with `full` in the cell `Read` whose row has pages in the
  cell `Not read`: `The source says 'full'. The table Reading names pages that no reader got:
  <ranges>.` Rule `body-without-reading`: the table exists, and a source with `all` in the
  cell `Views` has no row. Under "remains": `Sources with pages that no reader got: <id>
  (<n> pages).` and, for a specification with sources and without the table, `The table
  Reading is absent. Run index.py unread with --write.` With `--json`: the key `reading` with
  `table` (true or false) and `sources` (source, document, pages, not read), and the key
  `unread` in `remains`.
- Outside `--scope`, the table "Requirements" of `SPEC/vetting.md` fails the check when it is
  absent or empty; when a cell is empty; when an identifier is used two times; when the cell
  "Goes to" is not `C-<nn>`, `5`, `boundary: <name>` or `duplicate: R-<nn>`; when the cell
  names a decision of section 3.3; when the exit names an item, a boundary or a row that does
  not exist, an item that is retired, or a row that is a duplicate; when a stakeholder or a
  view is not in section 1; and when the source is not in section 2. An item that is not
  retired fails the check when no requirement goes to it and its cell "Admitted by" does not
  start with `own rule`. A stakeholder of section 1 without a requirement fails the check.
- After the part "Views", the part "Requirements": one line for each view with the number of
  requirements and the number for each exit. With `--json`: the key `requirements`. Under
  "remains", one line for each view: `More than half of the requirements of the view '<name>'
  go to a boundary.` With `--json`: the key `boundaries` in `remains`.
- Outside `--scope`, the state of each boundary of section 1 and the table "Proposed
  boundaries" of `SPEC/vetting.md` are examined. `aspect.py` reads the state from the line of
  the boundary: `(proposed)` or `(decided by the owner on <YYYY-MM-DD>)`; a line without a
  state is `proposed`. Rule `requirement-boundary-not-decided`: the cell "Goes to" names a
  boundary that the owner did not decide: `The requirement goes to the boundary '<name>'. The
  owner did not decide this boundary. Give the requirement a different exit, and propose the
  boundary to the owner.` Rule `boundary-state-unknown`: a state of a different form. Rule
  `boundary-without-date`: a decided state without a date. Rule
  `proposed-boundary-without-row`: a proposed boundary has no row in the table. Rule
  `proposed-row-unknown`: a row for a boundary that section 1 does not have. Rule
  `proposed-row-decided`: a row for a boundary that the owner decided. Rule
  `proposed-requirement-unknown`: a row names a requirement that the table "Requirements"
  does not have. Each line of the part "Requirements" ends with `a proposed boundary would
  take: <n>`: the requirements of the view that a row names, and the requirements whose cell
  "Goes to" names a proposed boundary. Under "remains": `Boundaries that wait for the decision
  of the owner: <name> (<n> requirements).` and, one line for each, `The boundary '<name>'
  would leave the stakeholder '<name>' with no requirement in the aspect.` With `--json`: the
  key `a proposed boundary would take` in each row of `requirements`, and the keys
  `proposed-boundaries` and `left-stakeholders` in `remains`.
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
  - At its end, builds or updates the index `WORK/index.sqlite` as `index.py build` does, with
    the rows of the manifest and the folder of `--from`, and prints its line. A failure of the
    index does not change the result code.
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

## scripts/index.py

```text
index.py build WORK [--synonyms FILE ...] [--from SPEC] [--manifest FILE]
index.py search WORK QUERY [--doc ID] [--limit N] [--no-synonyms] [--json]
index.py refs WORK DOC PAGE [--json]
index.py cited WORK IDENTIFIER [--json]
index.py ranges WORK DOC [--max-pages N]
index.py recall WORK ANSWERS [--limit N] [--no-synonyms] [--exact]
index.py given WORK DOC FIRST-LAST [--task TEXT] [--remove]
index.py unread WORK [DOC] [--max-pages N] [--json]
index.py unread WORK --write SPEC
index.py take WORK REPORT SOURCE
index.py lines WORK [--kind KIND] [--source SOURCE]
```

- `WORK` must be outside each git repository. The database is `WORK/index.sqlite`.
- No command prints the text of a document. A command gives the document, the page, the title
  of a section, an identifier and a number. `lines` prints the text of the reports of the
  readers; a report is not a document.
- `build`: reads each `WORK/converted/*.md`: the head lines `Source`, `sha256` and `Pages`,
  and the text below each heading `## Page N`. Writes the tables of "Index" in
  `data-model.md`.
  - Reads only a file whose digest changed. Removes a document whose file is gone.
  - Reads `references/synonyms.txt`, the file `WORK/synonyms.txt` when it is there, and each
    file of `--synonyms FILE`.
  - Keeps the rows of the table `given` of a document whose converted file did not change.
    Removes the rows of each other document.
  - Reads `references/seeds.md` for the names of the documents. `--manifest FILE` gives a
    different manifest, for tests.
  - `--from SPEC`: reads section 2 (the id and the title of each source) for the names of the
    documents, and section 8 (the cell `Term`, names separated by `;`, and a cell
    `Other names` if there is one) for the synonyms.
  - A file that cannot be read or that has no page heading is not indexed. The program prints
    one line for it and continues.
  - Prints one line with the numbers of the index.
- `search`: `QUERY` is words and phrases in quotation marks. Each term is one group with its
  synonyms. A page must hold one term of each group. Prints one line for each page, sorted by
  the rank of the full-text search, the document and the page: the document, the page, the
  title of the section, each term that matched with its count, and the number of matches.
  The last line names the synonyms that were used.
  - No page with each term: one line says so, and the pages that hold one term or more follow
    as a partial result.
  - `--doc ID`: one document only. `--limit N`: the number of results, default 20.
  - `--no-synonyms`: the terms of the query only. `--json`: the result as JSON.
- `refs`: the references on the page `PAGE` of the document `DOC`: the kind, the family, the
  text and the target. The target of an internal reference is its pages, or `not resolved`.
  The target of an external reference is its key and the document of the index, or
  `not in the index`; for a citation, also the page of its entry in the list of references.
- `cited`: each place that cites `IDENTIFIER`: the document, the page, the title of the
  section, the family and the text. `IDENTIFIER` is a standard, an address or a name of a
  document of the index.
- `ranges`: the page ranges of `DOC`, each with its number of pages and the titles of its
  sections. No range has more pages than `--max-pages N` (default 25). Each page of the
  document is in exactly one range.
- `recall`: `ANSWERS` is a Markdown file with the table of answers of `files.md`. Prints the
  number of rows found, the total, the share, the number of rows found with a partial result
  only, and each row that was not found. `--limit N`: the number of results for each query,
  default 10. `--exact`: the page before and the page after an answer are not accepted.
- `given`: records that the pages `FIRST` to `LAST` of `DOC` were given to a reader. One page
  is `FIRST` only. A range that is recorded two times is one row; `--task TEXT` replaces the
  task of the row. `--remove` removes the row of the range; result code `1` when the record
  has no such range. A range outside the pages of the document gives the result code `2`.
- `unread`: for each document, or for `DOC`, one line for each range that is in no recorded
  range, in the form of `ranges`, and one line with the number of pages, the recorded ranges
  and the pages that no reader got. A range of the output has no more pages than
  `--max-pages N` (default 25). `--json`: a list with, for each document, `document`, `pages`,
  `given` (first, last, task) and `not_read` (first, last, sections).
  - `--write SPEC`: writes or replaces the part "Reading" of `SPEC/vetting.md`, in the form
    of `files.md`. No other byte of the file changes, and the line ends stay. A folder without
    the file gets the file. The document of a source is the document with the id of the
    source, or a document that the table `aliases` knows by the address or by a name of the
    source. Prints one line with the number of rows and the sources with pages that no reader
    got.
  - Result code `1` when a page is in no recorded range.
- `take`: stores the lines `REQ` and `USE` of the report file `REPORT` for the source `SOURCE`
  in the table `lines` of "Index" in `data-model.md`. The forms are
  `REQ | <requirement> | <group> | <location>` and
  `USE | <kind> | <name> | <purpose> | <location>`, with the kind `tool`, `integration`,
  `framework`, `pattern` or `principle`. `REQ | none` and `USE | none` store nothing.
  - `SOURCE` has the form `S-<digits>`. A different form gives the result code `2`.
  - Removes the earlier lines of the same file name and the same source first.
  - A line that starts with `REQ` or `USE`, also after the mark of a list or a quote, and
    does not have the form is not stored. Prints one line for it: the file name, the line
    number and the word. Result code `1` when there is such a line.
  - Prints one line: the source, the file name, and the number of stored lines of each kind.
  - The text of a report goes into the database as a parameter. The program does not read it
    in a different way.
- `lines`: prints the stored lines, sorted by the number of the source, the file name and the
  line number. The table `| Source | Requirement | Group | Location |` has the lines of the
  kind `req`. The table `| Source | Kind | Name | Purpose | Location |` has the other kinds.
  An empty line is between the two tables. A table without a row is not printed.
  - `--kind KIND`: one of `req`, `tool`, `integration`, `framework`, `pattern`, `principle`. A
    different word gives the result code `2`. `--source SOURCE`: one source.
  - Result code `1` and one line that says so when no line is stored for the selection.
- Result code `0`: done. `1`: nothing was found, a file was not indexed, a page is in no
  recorded range, or a line of a report does not have the form. `2`: the input cannot be read, an argument is wrong, or the folder has no
  index. `recall` gives `0` when the input can be read.

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

## scripts/web.py

```text
web.py SOURCE OUT
```

- `SOURCE`: an http or https address, or a file of HTML, Markdown or plain text. `OUT`: the
  converted file to write.
- Writes the text of the source in the form of a converted file of `pdf.py`, through its
  functions: the head lines `Source`, `sha256` and `Pages`, and one heading `## Page <n>` for
  each part of 60 lines. A line of the text that starts with `#` is escaped.
- HTML: the program drops `head`, `script`, `style` and the other elements without text of
  the page, keeps headings, paragraphs, list items, table cells and code, and writes a link as
  its text.
- The rules for `OUT` are the rules of `pdf.py`: refuses a target in a git repository and a
  folder with other files and no marker, writes the marker `.reader-may-read`, prints
  `Written: <OUT> (<n> pages, sha256 <digest>)`.
- Result code `1` with the reason: a source that is not text (a PDF file gives a message that
  names `pdf.py`), a source without text, a network error, an HTTP error, a target that is
  refused. Result code `2`: wrong arguments.

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
