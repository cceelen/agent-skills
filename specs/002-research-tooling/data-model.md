# Data model: research tooling

The Markdown files of a specification are the store. `aspect.py` reads them into the plain
data below. No program writes `spec.md` except `place.py`, which fills the Level cells. No
program writes `trial.md`.

## Aspect specification (`spec.md`)

| Part | Fields | Rules that the check applies |
|---|---|---|
| Head | branch, research date, supersedes, accepted | accepted is a person and a date, or `pending` |
| 1 Aspect | aspect, field, intent of the owner, agreed on, stakeholders, views, contexts, risk dimensions, boundaries, targets | each field is filled; agreed on has a date; each line of the intent is a quote with a date, or `(no answer)`; each stakeholder is one line below the field, names its concerns and names its source or `judgement`; each view is one line below the field, names one stakeholder of section 1 or more in the form `(stakeholders: a, b)`, has an item, and has an item on level 1 when no level is pending; each risk dimension is one line below the field, in the form `` - `name`: question and opinion ``; each target is one line below the field and names its source, or the field says `(none found)` |
| 2 Sources | id, source, issuer, version or date, class, license, read, views, url | each cell is filled; class is one of six values; read is `full`, `part` or `no`; ids are unique; views holds views of section 1 or `all`, and a table without this cell is permitted |
| 3.3 Decisions by context | decision, depends on, options, sources | each source id is known |
| 3.4 Disagreement | question, positions, handling, sources | the section is present; `none found` is permitted |
| 4 Checklist | id, item, why, view, level, admitted by, check, source | see below; the view is a view of section 1 |
| 5 Skill set | name, target folder, goal, reads first, applies, delegates, stops when; rows of implementation skills | name obeys the rule for a skill name |
| 6 Watch list | signal, where, cadence | one row or more |
| 7 Decisions | date, decision, reason, revisit when | each row has a date |
| 8 Glossary | term, meaning here, other meanings | term and meaning are filled |

### Checklist item

| Field | Values | Rule |
|---|---|---|
| id | `C-` and a number | unique; with `--previous`: an item of the earlier revision is still present (a retired item keeps its row with the level `retired`), a retired id is not in use again, and an id with a changed text is listed for judgement |
| item | one sentence | names no product of the word list of the aspect |
| why | text | names the risk that the item answers |
| level | `1`, or `2, <dimension>`, or `3, <dimension>`, or `pending`, or `not admitted`, or `retired` | the dimension is one of section 1; the renderer leaves out an item that is `not admitted` |
| admitted by | `authority (n)`, `practice`, `own rule (<principle>)`, with an optional `, vetting pending` | |
| check | a check, or `judgement` | not empty |
| source | one or more of `S-nn <unit>` or `constitution <principle>` | each id is known; each cited source has an evidence row that names the item |

An item **rests on** a source when it cites it. The check fails for an item whose sources are
all read `no`, or all independent and rejected. An item whose sources are all independent and
not confirmed yet is listed under "what remains": only the owner can end that state.

## Evidence record (`evidence.md`)

One row for each source: source id, what it contributes, where, supports, read (a date). The
check reads the id, the supports cell and the date. It does not judge the summary.

## Vetting record (`vetting.md`)

Written by `vet.py score` and `place.py`, corrected by the owner. The session writes the
table "Requirements". Three tables, formats in `contracts/files.md`.

| Table | Row | Fields |
|---|---|---|
| Sources | one independent source | source id, kind (`repository` or `page`), gate result, signals, answers with their URL, score, rubric version, date, confirmed by |
| Items | one checklist item | item id, the six answers with their source, return, cost, score, admitted, level, rubric version |
| Requirements | one requirement that a source states for a stakeholder | id `R-<nn>`, requirement, stakeholder, view, source with its location, goes to |

The cell "Goes to" of a requirement is `C-<nn>`, `3.3: <decision>`, `5`, `boundary: <name>` or
`duplicate: R-<nn>`. The check fails for each other text, for an exit that names a row that
does not exist, for an item without a requirement that is not admitted by `own rule`, and for
a stakeholder without a requirement. A view with more than half of its requirements at a
boundary is listed under "what remains".

State of a source: `not vetted` → `rejected by a gate` or `scored` → `confirmed` or `rejected`
(by the owner). Only `confirmed` lets the source carry an item alone.

State of an item: `pending` (an answer is missing) → `placed` (admitted with a level, or not
admitted).

An answer names its source or says `judgement`. The check counts the answers of each kind and
reports the two numbers. The numbers do not fail the check.

## Record of the trials (`trial.md`)

Optional. Written by the session after a trial, and by the owner's decision for each finding.
Two tables.

| Table | Row | Fields | Rules that the check applies |
|---|---|---|---|
| Trials | one trial of the recipe on a project | id, date, project, commit of the specification, plan (where the plan is, or `not kept`) | |
| Findings | one finding of the review of a plan | id, trial, viewpoint, finding, route, status | the trial is in the table "Trials"; the viewpoint is one of the names in `references/viewpoints.txt` (`architecture`, `operations`, `quality`, `development`, `security`, `product owner`, `views of the recipe`), and is not checked when that file is absent; the finding has a text; the route is `recipe`, `tooling` or `implementation skill`; the status is `open`, `corrected in <revision or commit>` or `declined: <reason>` |

State of a finding: `open` → `corrected` or `declined` (by the owner). A finding that is open
is listed under "what remains". A specification without a trial is listed there also. A
finding whose viewpoint was not checked is listed there also.

## Seeds (`references/seeds.md` in the tooling)

Written by a session from the page of the issuer, accepted by the owner. Read by `seed.py`.
Two tables.

| Table | Row | Fields | Rules that `seed.py` applies |
|---|---|---|---|
| The seeds | one document or standard | id, document, issuer, version or date, kind, address, sha256, terms, row read on | each cell but sha256 is filled; the id uses lowercase letters, digits and hyphens and is unique; the kind is `pdf`, `page` or `owner file`; the address starts with `http://` or `https://`; sha256 is empty or 64 hexadecimal characters; row read on has a date |
| Bodies of knowledge | one body of knowledge of one field | field, seed | the seed is an id of the first table |

## Work folder (outside each git repository)

Written by `seed.py get`, and by `pdf.py`, `vet.py` and `index.py` for their files. Not
committed.

| Path | Holds |
|---|---|
| `seeds/<id>.pdf` | the file of one seed, or of one PDF source of an aspect specification |
| `converted/<id>.md` | the text of that file with one heading for each page, and the marker `.reader-may-read` beside it |
| `seeds.json` | the date of `--today` or `null`, and for each seed: id, kind, file, converted, sha256, pages, state |
| `index.sqlite` | the index of the converted files: see "Index" |

State of a seed: `retrieved`, `recorded` (kind `page`), `owner must give the file`, `changed`
(the digest is not the digest of the manifest or, without one, of the last run),
`failed: <reason>`. Only `retrieved` and `recorded` give the result code 0.

## Index (`index.sqlite` in a work folder)

Written by `index.py build`, and by `seed.py get` and `init.py` at their end. Not committed. It
holds the text of the documents: only `index.py` reads it. The same converted files give the
same content. No table holds a current time.

| Table | Row | Fields |
|---|---|---|
| documents | one converted file | id (the file name without `.md`), source, digest (of the source), pages, converted (the digest of the converted file) |
| pages | one page of a document, with a full-text search (FTS5, tokenizer `porter unicode61 remove_diacritics 2`) | document, page, text |
| sections | one section of a document | document, seq, title, number, first_page, last_page, level, pattern (`chapter`, `numbered`, `capitals` or `none`) |
| refs | one reference on one page | document, page, kind (`internal` or `external`), family, text, key, target_document, target_first, target_last |
| acronyms | one short form with its long form | document, page, short, long, pattern (`parentheses` or `list`) |
| aliases | one other name of a document of the index | key, document, origin (`head`, `manifest` or `specification`) |
| synonyms | one term of one group | grp, term, origin (`acronym`, `file` or `glossary`) |
| meta | the version of the patterns | key, value |

A converted file with a different digest is read again. A different version of the patterns
makes the index again. The tables aliases and synonyms, the references of the family
`document` and the target document of each external reference are written again in each build.

Families of a reference: `section`, `chapter`, `page`, `table`, `figure`, `name` (internal);
the families of the table `STANDARDS` of the program, `address`, `doi`, `citation`, `document`
(external). The key of a reference is its identifier without case, without the year of a
standard and without the word `Std`.

## Synonyms (`references/synonyms.txt` in the tooling)

Written by a session or by the owner. Read by `index.py build`. One group in each line, the
terms separated by ` = `. A line that starts with `#` is a comment. A group is symmetric and
transitive.

## Kit (outside each git repository)

Written by `export.py` or `init.py`. The kit of `init.py` holds the marker `.factory-kit` with
the commit of this repository, and is a git repository with the branch `main` and one commit.
`init.py --again` removes only a folder that holds the marker.

## Rubrics (in the tooling)

| File | Holds |
|---|---|
| `rubric-items.txt` | version; the six questions with their scales; the admission threshold; the level 1 threshold; the cost limit between level 2 and level 3 |
| `rubric-sources.txt` | version; the gates; the signals and answers with their weights; the score at which a source passes to the owner |

A change of a question, a scale, a weight or a threshold increases the version. The identifier
of a question does not change.

## Rendered recipe skill

Owned by the renderer: `SKILL.md`, `references/checklist.md`, `agent-templates/<name>.md`,
`docs/<name>.md`. Each starts with the stamp: specification branch, commit, digest of `spec.md`.
The stamp of a trial rendering starts with a note that the file is a trial rendering.

## Selection (in a project of a user)

One file for each aspect. It holds the stamp of the recipe that was used, the risk analysis
(dimension, question, answer, target level), and each checklist item with its state: adopted,
or declined with a reason. The distance of the project is the list of adopted items whose
check fails.
