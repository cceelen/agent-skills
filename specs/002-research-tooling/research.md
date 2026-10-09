# Research: design decisions of the research tooling

Each entry: the decision, its reason, and what else was considered. Facts come from this
repository (read on 2026-10-09) unless a source is named.

## R1. Where the tooling lives

- **Decision**: `factory/sota-research/`, in the layout of a skill. `AGENTS.md` points a session
  at it.
- **Reason**: decision of the owner, 2026-10-09. `install.sh` and the plugin copy all of
  `skills/`, so a folder there goes to each user and costs their context.
- **Considered**: `skills/sota-research/` (goes to users); the skill folder of one agent product
  (a session in a different product does not find it).

## R2. Where a specification lives

- **Decision**: on its own branch for its whole life. `main` holds the machinery and the
  delivered skills. A Spec Kit step is a pull request into the branch of the specification. A
  delivery is a pull request into `main`.
- **Reason**: decision of the owner, 2026-10-09. A session on `main` or on one aspect carries
  only what it needs.
- **Consequence**: the programs take the folder of a specification as an argument and never
  look for `specs/` by themselves. The tests use fixtures. A rendered skill carries a stamp
  with the branch, the commit and a digest of its specification.
- **Considered**: one research branch for all specifications; specifications on `main`.

## R3. The data store

- **Decision**: the Markdown files of the specification are the store: `spec.md`,
  `evidence.md`, `vetting.md`. One module, `aspect.py`, reads them into plain data. Sections
  are found by their number, tables by their header row.
- **Reason**: the owner reviews these files in a pull request and corrects answers in them. A
  second store would drift from them. Text files merge and show in a diff.
- **Considered**: JSON or YAML beside the Markdown (two sources of truth); a database (binary,
  does not travel in git; the owner rejected it on 2026-10-08).

## R4. One program for each part

- **Decision**: `check.py`, `render.py`, `place.py`, `vet.py`, each with a usage text, as the
  programs of `library-vetting` are. Result code 0: done, nothing fails. 1: done, and
  something fails or remains. 2: the input cannot be read.
- **Reason**: each user story is delivered alone. An agent reads the result code as the cheap
  signal and the report as the detail.
- **Considered**: one program with subcommands (one large file, as `score.py` with 1298 lines).

## R5. The earlier revision for stable identifiers

- **Decision**: `check.py --previous FILE`. The caller gets the file, for example with
  `git show <commit>:specs/<name>/spec.md`. The procedure gives the command.
- **Reason**: the program stays free of git, and a test needs two files only.
- **Considered**: the program calls git itself (needs a repository in each test).

## R6. How the acceptance is recorded

- **Decision**: a field in the head line of an aspect specification:
  `**Accepted**: <person>, <date>` or `**Accepted**: pending`. The template gets this field.
  The renderer renders only when it is not `pending`.
- **Reason**: FR-009 needs one place that a program can read. Today the acceptance is a phrase
  inside a decision row.
- **Considered**: a row of the decisions table with a fixed wording (fragile).

## R7. The calculation of risk and reward

- **Decision**: six answers for each item, each a whole number with its source:
  severity of the harm (1 to 3), probability without the item (1 to 3), breadth of contexts
  (1 to 3), effort to adopt (1 to 3), effort to keep (1 to 3), risk of the item itself (0 to
  2). The program computes `return = severity x probability x breadth`, `cost = adopt + keep`,
  and `score = (return x 10) // cost - 5 x own risk`, in whole numbers. `rubric-items.txt`
  holds the questions, the scales, the thresholds and the version.
  - Admission: the score is at or above the admission threshold.
  - Level 1: breadth is 3 and the score is at or above the level 1 threshold.
  - Above level 1: the item names a risk dimension. Level 2 when the cost is 4 or less,
    level 3 when it is more.
  - Order: by level, then by score from high to low, then by identifier.
- **Reason**: decision of the owner (return over cost; basic practices on level 1; a risk
  dimension above it). Whole numbers give the same result on each machine. The thresholds are
  first values; the decision row in the specification 001 says to revisit them after the first
  use.
- **Considered**: weights with fractions (rounding differs); a published risk rating scheme
  (about 16 answers for each item, written for security only).

## R8. The vetting of an independent source

- **Decision**: two steps, as in `library-vetting`. `vet.py collect` uses the network and
  writes the signals to a work folder that is not committed. `vet.py score` uses no network: it
  reads the signals and the recorded answers and writes the table in `vetting.md`.
  - A repository: `collect` calls `skills/library-vetting/scripts/collect.py` and takes the
    date of the last commit and the number of commits and authors from its facts.
  - A page: `collect` measures: the page can be reached; a date is present; the age in days
    against a date that the caller gives; an author or issuer is named; the number of links to
    other hosts.
  - Two answers are recorded by the reader, not measured, each with the URL that shows it: the
    author has a record in the field; how many fast-lane sources of the specification refer to
    the source.
  - Gates (no question to the owner): no author or issuer, no date, older than the limit of
    the aspect, not reachable.
- **Reason**: decision of the owner (gates, then score, then confirmation). The split keeps
  the scoring testable without the network. A signal that a program cannot measure is called
  an answer, so that the record does not claim more than it knows.
- **Considered**: let the reader agent rate the source (a model would assign trust by feel).

## R9. How a program fetches a page

- **Decision**: `urllib` of the standard library, `http` and `https` only, public addresses
  only (also after a redirect), a timeout for each operation and a time limit for each page, a
  size limit of 2 MB, no cookies, no credentials. The program reads header fields and meta fields
  only. An error is recorded as a signal that was not measured, and the run continues.
- **Reason**: constitution III and the rule of `AGENTS.md` for the network.

## R10. Isolated readers

- **Decision**: two agent templates. `source-reader` gets the web search and web fetch tools
  only. `second-reader` gets web fetch only. Neither can write a file: each returns text, and
  the session writes. `models.py` holds the table of models and tool names for each agent
  product and fills the templates, as `library-vetting` does. Where a product cannot limit the
  tools of an agent, the procedure tells the session to stop before it reads a source.
- **Reason**: FR-020, C-21. The moment a model reads a page is the moment hostile content can
  act; an agent without a shell and without files can do little with it.
- **Considered**: readers that write their notes to a folder (needs a write tool, and the
  notes would be stored material).

## R11. What the renderer writes

- **Decision**: for an aspect specification, the renderer owns a fixed set of files in the
  target folder: `SKILL.md`, `references/checklist.md`, `agent-templates/<name>.md` and
  `docs/<name>.md`. The target is `skills/<name>/`, or the folder that section 5 of the
  specification names (for 001: `factory/sota-research/`). Each rendered file starts with a
  stamp: the specification branch, the commit that the caller gives, and the SHA-256 digest of
  `spec.md`. Files beside these are written by hand and are not touched.
- **Reason**: FR-006, FR-010 and the branch model. A fixed set makes "differs from a fresh
  rendering" a plain comparison.
- **Considered**: a manifest file that lists what was rendered (one more file to keep right).

## R12. The selection of a project

- **Decision**: one Markdown file for each aspect in the project of the user:
  `.agents/kit/<aspect>.md`. It holds the stamp of the recipe, the table of the risk analysis,
  and the checklist with a mark for each item and a reason for each declined item. The format
  is in `contracts/files.md`.
- **Reason**: decision of the owner (a Markdown checklist, committed, simple to revisit).
  `.agents/` is the folder that most agent products read.
- **Open for the review**: the path. It is the first file that the kit puts into a project of
  a user.

## R14. Python version and how the programs run

- **Decision**: the latest stable Python, today 3.14, for the tooling of the factory. Each
  program has a script header with `requires-python = ">=3.14"` and no dependencies, and runs
  with `uv run <program>`. Tools run with `uvx` or through `uv run`. The tests of the tooling
  run on Python 3.14; a `conftest.py` in `tests/sota-research/` skips the folder on an older
  version, and the CI gets a job for 3.14.
- **Reason**: decision of the owner, 2026-10-09. Fact: `uv` 0.12.19 offers 3.14 as the newest
  stable version; 3.15 is a release candidate. The tooling runs only on the workstation of the
  owner and in the CI, so it does not need an old version.
- **This supersedes** the decision of the same day to require Python 3.11 for helpers. The
  skills that users install keep the rule of `AGENTS.md`.

## R15. One working branch, one commit for each phase

- **Decision**: the implementation is done on the branch of the tasks pull request, with one
  commit for each phase. The branch is merged as a whole into `002-research-tooling`. One
  delivery to `main` follows.
- **Reason**: decision of the owner, 2026-10-09.
- **This supersedes** one pull request into `main` for each user story.

## R16. Tests inside the programs

- **Decision**: each program holds its tests as examples (doctests) and runs them with
  `--selftest`. Short examples are in the docstring of a function; scenarios are in the table
  `__test__` at the end of the file. The sample data is a Python file, `sample.py`. There is no
  test folder for the tooling. `tests/test_repo.py` runs each program with `--selftest` under
  coverage; the minimum is 90 percent with branches. Ruff examines all files; only the sample
  data is free of the rule for the line length, because a table row cannot be split.
- **Reason**: direction of the owner, 2026-10-09: a program then validates itself, and a user
  installs the Python files without test files.
- **Result**: 424 examples in 7 files; coverage 94 percent. The part without examples is the
  real network read of one page.
- **This supersedes** the folder `tests/sota-research/` of the plan.

## R17. Coverage tracking with Codecov

- **Decision**: the job for Python 3.14 writes `coverage.xml` and sends it to Codecov with the
  action `codecov/codecov-action`, pinned by its commit. The upload uses OIDC; no token is
  stored. The workflow runs on each push and each pull request, thus on `main`, on each
  specification branch and on each working branch. `codecov.yml` sets two checks for a pull
  request: the project must not lose more than one point, and the added lines need 90 percent.
- **Reason**: direction of the owner, 2026-10-09: track the coverage on the long-lived branches
  and during pull requests. Facts: the repository is public; Codecov knows it but it is not
  active there yet; the action v7.1.1 supports OIDC.
- **Result**: the first upload worked without a token and without a setup step: Codecov shows
  92.8 percent for 7 files. Thus the CI now fails when an upload fails.
- **Part of the owner**: install the Codecov app for the repository one time. Codecov needs it
  to write its checks and its comment into a pull request.

## R13. Simplified Technical English in the programs

- **Decision**: each program keeps its messages in one table at the top of the file. A test
  reads the tables and fails on a sentence of more than 25 words.
- **Reason**: constitution XI needs a cheap check; the full standard cannot be checked by a
  program.
