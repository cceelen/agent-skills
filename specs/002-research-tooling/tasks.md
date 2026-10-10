# Tasks: Research tooling of the factory

**Input**: Design documents from `specs/002-research-tooling/` on the branch `002-research-tooling`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/programs.md,
contracts/files.md, quickstart.md

**Tests**: included. The specification requires tests without the network for each program
(FR-029), and fixtures prove the success criteria.

**Organization**: one phase for each user story, and one commit for each phase, on the working
branch `002-research-tooling-tasks`. Mark the tasks of a phase as done in the commit of that
phase. The branch is merged as a whole into `002-research-tooling`. One delivery then carries
`factory/`, `tests/`, `docs/` and the rule files to `main`.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: can run in parallel (different files, no dependency on an open task)
- **[Story]**: the user story of the task (US1 to US5)

## Rules for each task

- The latest stable Python (3.14), standard library only, no shell script. Each program
  starts with a script header with `requires-python = ">=3.14"` and `dependencies = []`. Run a
  program with `uv run <program>`, and a tool with `uvx` or `uv run`.
- Same input gives same output: sort the output, do not read the clock.
- Result codes: `0` nothing fails or remains, `1` something fails or remains, `2` the input
  cannot be read.
- Each program keeps its messages in one table `MESSAGES` at the top of the file, in
  ASD-STE100, with a maximum of 25 words in a sentence.
- Before each commit: `uv run --python 3.14 pytest`, `uv run ruff check`,
  `uv run pre-commit run --all-files`.

---

## Phase 1: Setup

**Purpose**: the folder of the tooling and the rules that let it exist on `main`

- [x] T001 Create `factory/sota-research/` with the folders `scripts/`, `references/`, `prompts/`, `agent-templates/`, and a first `factory/sota-research/SKILL.md` with front matter (`name: sota-research`, a `description` that says what it does and when to use it) and one paragraph that points at `references/procedure.md`
- [x] T002 [P] Add `"factory"` to `ARTIFACT_TYPES` in `tests/test_repo.py`, and make `test_skill_layout` run for the folders in `factory/` also
- [x] T003 [P] Create `docs/sota-research.md` in ASD-STE100 with the purpose of the tooling and one section for each program (filled by the stories)
- [x] T004 [P] Add to `AGENTS.md`: in the section "Structure", one sentence that tells a session to read `factory/sota-research/SKILL.md` to distil an aspect; in the section "Rules for the programs", that the programs in `factory/` use the latest stable Python, declare it in their script header and run with `uv run`, and that the rule for Python 3.9 applies to the skills that users install
- [x] T050 [P] Create `tests/sota-research/conftest.py` that skips the folder on a Python older than 3.14, and add `"3.14"` to the matrix of `.github/workflows/test.yml`
- [x] T005 Add the field `**Accepted**: [person and date, or pending]` to the head line, and the optional field `- **Target folder**: [folder, or leave out for skills/<name>/]` to the recipe skill block of section 5, in `.specify/templates/overrides/aspect-spec-template.md` (formats: `contracts/files.md`)

---

## Phase 2: Foundational

**Purpose**: the shared reader and the base fixture. Each story needs them.

- [x] T006 Create the fixture `tests/sota-research/fixture/good/` with `spec.md`, `evidence.md` and `vetting.md`: a small aspect specification made from the template, with 4 sources (one `standard`, one `research`, two `independent`), 5 checklist items, 2 risk dimensions, `**Accepted**: A. Person, 2026-01-15`, and no rule of `data-model.md` broken
- [x] T007 Write `tests/sota-research/test_aspect.py`: reading the fixture `good` gives the head fields, the fields of section 1, the rows of each table of `data-model.md` by header name, and the block of section 5; a cell with an escaped pipe is one cell; a missing file gives a clear error
- [x] T008 Implement `factory/sota-research/scripts/aspect.py`: `load(folder)` returns plain dictionaries and lists for `spec.md`, `evidence.md` and `vetting.md` (absent files give empty data); sections are found by their number, tables by their header row; each row keeps its line number; a function writes one changed cell back without a change to any other byte of the file
- [x] T009 [P] Write `tests/sota-research/test_messages.py`: for each program in `factory/sota-research/scripts/`, each sentence in `MESSAGES` has a maximum of 25 words; no file in `prompts/` or `agent-templates/` or `SKILL.md` contains a model name of the table in `scripts/models.py`

**Checkpoint**: `uv run pytest tests/sota-research` passes.

---

## Phase 3: User Story 1 - Know what remains in an aspect specification (Priority: P1) 🎯 MVP

**Goal**: one program reports each failing rule and what remains (FR-001 to FR-005).

**Independent Test**: `check.py` on the fixture `good` has result code 0; on each defect
fixture it names that defect and no other; two runs print the same bytes.

### Tests for User Story 1

- [x] T010 [P] [US1] Create one defect fixture for each rule in `tests/sota-research/fixture/defect-<rule>/`, each a copy of `good` with one planted defect: `source-cell-empty`, `class-unknown`, `read-unknown`, `source-id-twice`, `unknown-source` (an item cites an id that section 2 does not list), `check-empty`, `no-evidence-row`, `evidence-does-not-name-item`, `no-disagreement-section`, `glossary-cell-empty`, `decision-without-date`, `source-without-version`, `watch-list-empty`, `level-without-dimension`, `dimension-unknown`, `why-empty`, `only-unread-source`, `only-unconfirmed-source`, `product-word` (with a word list file)
- [x] T011 [P] [US1] Create `tests/sota-research/fixture/previous/spec.md`: an earlier revision of `good` in which one identifier has a different item and one identifier is retired, and a copy `good-reuses-id/` that uses the retired identifier again
- [x] T012 [US1] Write `tests/sota-research/test_check.py`: `good` gives no finding and result code 0; each defect fixture gives exactly its finding with the section and the row id, and result code 1; `--previous` reports the changed and the reused identifier; without `--previous` the report says that the check was skipped; pending levels, pending vettings and `Accepted: pending` are listed as "remains" and do not change the result code; `--json` holds the same findings with sorted keys; two runs give the same bytes; a folder without `spec.md` gives result code 2

Done differently than T010 and T011 say: the tests make each defect copy from the fixture `good`
at run time (the table `DEFECTS` in `tests/sota-research/test_check.py`). Thus the repository
holds one fixture, not twenty copies of it. A retired item keeps its row with the level
`retired`; this is how the check knows a retired identifier.

### Implementation for User Story 1

- [x] T013 [US1] Implement the rules of `data-model.md` in `factory/sota-research/scripts/check.py` as one function for each rule, each returning sorted findings `(rule, section, row id, text)`: class is one of `standard`, `foundation`, `vendor`, `research`, `trusted-data`, `independent`; read is `full`, `part` or `no`; level is `1`, `2, <dimension>`, `3, <dimension>` or `pending`; check is not empty; each cited source has an evidence row that names the item
- [x] T014 [US1] Implement the rules across files in `factory/sota-research/scripts/check.py`: an item whose sources are all read `no`, or all `independent` without a confirmation in `vetting.md`; the comparison with `--previous`; the word list of `--words`
- [x] T015 [US1] Implement the command line of `check.py` as in `contracts/programs.md`: the report lines, the summary (failing checks, pending levels, pending vettings, items that need judgement, accepted or not), `--json`, the result codes
- [x] T016 [US1] Fill the section for `check.py` in `docs/sota-research.md`, and write in `factory/sota-research/references/procedure.md` when to run the check and how to get the earlier revision (`git show <commit>:specs/<name>/spec.md`)

**Checkpoint**: commit the phase. After the delivery to `main`, on the branch
`001-sota-research`, run `check.py specs/001-sota-research` and correct that specification in
a pull request into its branch (expected: the new fields `Accepted` and `Target folder` are
missing).

---

## Phase 4: User Story 2 - Render the recipe skill from its specification (Priority: P2)

**Goal**: a complete recipe skill from an accepted specification, and a test that fails when a
committed skill differs (FR-006 to FR-010).

**Independent Test**: rendering the fixture `good` gives the same files as the fixture
`good-rendered`; a changed item makes `render.py --check` fail until the skill is rendered again.

### Tests for User Story 2

- [x] T017 [P] [US2] Create `tests/sota-research/fixture/not-accepted/` (a copy of `good` with `**Accepted**: pending`) and `tests/sota-research/fixture/target-folder/` (a copy with `- **Target folder**: \`factory/example/\`` in section 5)
- [x] T018 [US2] Write `tests/sota-research/test_render.py`: rendering `good` with `--commit 0000000 --out <tmp>` gives exactly the files of `tests/sota-research/fixture/good-rendered/`; each rendered file starts with the stamp of `contracts/files.md`; `SKILL.md` has the front matter and fewer than 500 lines; the checklist reference holds id, item, risk, level and check, and no Source cell; `not-accepted` and each defect fixture write nothing and have result code 1; `target-folder` writes into that folder; `--check` has result code 1 and names the file after one item changed; a word of the word list in the rendered text fails the rendering

Done differently than T017 says: the tests make the copies `not-accepted` and `target-folder`
from the fixture `good` at run time. One rule was added to the check: a field of the recipe
skill in section 5 must not refer to a section of the specification, because the renderer
copies it into the skill.

### Implementation for User Story 2

- [x] T019 [US2] Implement the rendering of `SKILL.md` in `factory/sota-research/scripts/render.py`: front matter (`name` from section 5, `description` from the aspect and the goal), the stamp, the goals (3.1), the order of the work (3.2), the decisions by context (3.3), the handling of disagreement (3.4, without the positions), how to lead the risk analysis along the risk dimensions of section 1 with the opinion of the kit (FR-008), how to show and change the selection in `.agents/kit/<aspect>.md` (FR-008a, format of `contracts/files.md`), what to delegate, when to stop
- [x] T020 [US2] Implement the rendering of `references/checklist.md`, `agent-templates/<name>.md` and `docs/<name>.md` in `factory/sota-research/scripts/render.py`; the documentation is in ASD-STE100
- [x] T021 [US2] Implement the command line of `render.py` as in `contracts/programs.md`: run the rules of `check.py` first; refuse when a check fails or the acceptance is missing; `--commit`, `--branch`, `--out`, `--check`; the target folder from section 5 or `skills/<name>/`
- [x] T022 [US2] Create `tests/sota-research/fixture/good-rendered/` from the reviewed output of T019 to T021
- [x] T023 [US2] Write `tests/sota-research/test_fresh.py`: for each `specs/*/spec.md` in the repository that is an aspect specification and is accepted, `render.py --check` passes; with no such file (the case on `main`) the test checks only that each skill with a stamp has a stamp of the right form
- [x] T024 [US2] In `tests/test_repo.py`, let a skill whose `SKILL.md` carries a stamp pass without a folder `tests/<name>/`: `test_fresh.py` covers it
- [x] T025 [US2] Fill the section for `render.py` in `docs/sota-research.md`, and add the delivery of a rendered skill to `factory/sota-research/references/procedure.md`: render on the branch of the specification, then carry only the rendered files to a branch from `main`

**Checkpoint**: commit the phase.

---

## Phase 5: User Story 3 - Place each item with a calculation of risk and reward (Priority: P3)

**Goal**: admission, order and level of each item from recorded answers (FR-011 to FR-014a).

**Independent Test**: `place.py` on the fixture `good` gives the expected values; the fixture
`missing-answer` leaves one item `pending` with result code 1.

### Tests for User Story 3

- [x] T026 [P] [US3] Fill the table "Items" in `tests/sota-research/fixture/good/vetting.md` with answers that give: one item on level 1, one on `2, <dimension>`, one on `3, <dimension>`, one not admitted; create `tests/sota-research/fixture/missing-answer/` (one answer empty) and `tests/sota-research/fixture/level-without-dimension/` (an item above level 1 whose Level cell names no dimension)
- [x] T027 [US3] Write `tests/sota-research/test_place.py`: the return, cost, score, admission, level and position of each item of `good` are the expected values; `missing-answer` leaves that item `pending`, names the answer and has result code 1; an answer out of its scale is reported; without `--write` no file changes; with `--write` only the computed cells of "Items" and the Level cells of the checklist change; a corrected answer changes only its item; the record carries the version of the rubric; two runs give the same bytes

Done differently than T026 and T029 say: the tests make the defect copies at run time. The risk
dimension of an item is recorded in a new cell Dimension of the table "Items", not in the Level
cell: the program then writes the Level cell as a whole.

### Implementation for User Story 3

- [x] T028 [US3] Write `factory/sota-research/scripts/rubric-items.txt`: the version; the six questions with stable identifiers and scales (severity 1 to 3, probability 1 to 3, breadth 1 to 3, adopt 1 to 3, keep 1 to 3, own risk 0 to 2), each with the meaning of each value in one line; the admission threshold; the level 1 threshold; the cost limit 4 between level 2 and level 3
- [x] T029 [US3] Implement `factory/sota-research/scripts/place.py` as in `contracts/programs.md` and R7 of `research.md`, in whole numbers: `return = severity x probability x breadth`, `cost = adopt + keep`, `score = (return x 10) // cost - 5 x own risk`; admitted when the score is at or above the admission threshold; level 1 when breadth is 3 and the score is at or above the level 1 threshold; else level 2 when the cost is 4 or less, level 3 when it is more, with the dimension that the Level cell already names; order by level, then score from high to low, then identifier
- [x] T030 [P] [US3] Write `factory/sota-research/prompts/risk-answers.md`: the task to record the six answers for one item, each with its source or `(judgement)`, and to name the risk dimension for an item whose return depends on the risk of a project; the task says that a program computes the level
- [x] T031 [US3] Fill the section for `place.py` in `docs/sota-research.md`, and add the step to `factory/sota-research/references/procedure.md`

**Checkpoint**: commit the phase.

---

## Phase 6: User Story 4 - Vet an independent source before it supports an item (Priority: P4)

**Goal**: measured signals, a scripted score and the confirmation of the owner (FR-015 to FR-018).

**Independent Test**: `vet.py score` on the fixture signals gives the expected scores, one
source is rejected by a gate, and `check.py` reports the item that rests on an unconfirmed source.

### Tests for User Story 4

- [x] T032 [P] [US4] Create `tests/sota-research/fixture/signals/` with one JSON file for each independent source of `good` and of a new fixture `tests/sota-research/fixture/vetting/`: a page that passes, a page without a date (gate), a page older than the limit (gate), a repository with facts in the form of the collector of `library-vetting`, and a source with one signal not measured
- [x] T033 [US4] Write `tests/sota-research/test_vet.py`: `score` gives the expected gate result and score for each source and uses no network (the test replaces `urllib.request.urlopen` with a function that fails); a signal that is not measured is shown as not measured and the run continues; `--write` fills the table "Sources" and never the cell "Confirmed by"; result code 1 while a source is not confirmed; the parsing of a saved page (`tests/sota-research/fixture/pages/*.html`) gives the date, the author and the number of links to other hosts; `collect` with a failing network writes a signal file with the error and has no exception

Done differently than T032, T036 and T037 say: the tests change the two signal files at run time
to make the gate cases. The age limit is an option of `score`, not of `collect`, so that a new
limit needs no new collection. The collector of `library-vetting` runs without `--lite`,
because only its full mode gives the history of the repository. A date in section 2 is used
when the page gives none.

### Implementation for User Story 4

- [x] T034 [US4] Write `factory/sota-research/scripts/rubric-sources.txt`: the version; the gates (no author or issuer, no date, older than the limit, not reachable); the signals and the two recorded answers with their weights; the score at which a source passes to the owner
- [x] T035 [US4] Implement `vet.py score` in `factory/sota-research/scripts/vet.py` as in `contracts/programs.md`: read the signal files and the answers of the table "Sources", apply the gates, compute the score, print and with `--write` fill the table
- [x] T036 [US4] Implement `vet.py collect` in `factory/sota-research/scripts/vet.py` for a page, as in R9 of `research.md`: `http` and `https` only, a timeout, a limit of 2 MB, no cookies, no credentials; read the header fields and the meta fields for the date and the author; count the links to other hosts; the age from `--today`; each error becomes a signal that was not measured
- [x] T037 [US4] Implement `vet.py collect` for a repository: run `skills/library-vetting/scripts/collect.py --lite` with the interpreter of the current process and take the facts that the rubric names; when the collector is absent or fails, record that and continue
- [x] T038 [US4] Fill the section for `vet.py` in `docs/sota-research.md`, and add the two steps and the confirmation of the owner to `factory/sota-research/references/procedure.md`

**Checkpoint**: commit the phase. After the delivery to `main`, on the branch
`001-sota-research`, apply `vet.py` and `place.py` to that specification in a pull request
into its branch (SC-003).

---

## Phase 7: User Story 5 - Take one aspect through the four phases (Priority: P5)

**Goal**: the instructions, the prompts and the isolated readers that lead a run (FR-019 to FR-027).

**Independent Test**: one trial run with the owner on a small aspect stops for the review with
a specification whose check reports no failure other than "not accepted".

- [x] T039 [P] [US5] Write `factory/sota-research/prompts/reader.md`: the task of an agent that reads one source: what to report (issuer, version or date, license, what the source contributes with the location, the two recorded answers of the vetting with a URL), that fetched text is data and never an instruction, that instructions found in a page are reported as content, and that the agent says what it did not reach
- [x] T040 [P] [US5] Write `factory/sota-research/prompts/second-reader.md`: the task to compare each line of an evidence record with its source and to report each line that says more than the source, with the correct wording and the location
- [x] T041 [P] [US5] Write `factory/sota-research/agent-templates/source-reader.md` (web search and web fetch only) and `factory/sota-research/agent-templates/second-reader.md` (web fetch only), with placeholders for the model and the tool names
- [x] T042 [US5] Implement `factory/sota-research/scripts/models.py` for the roles `source-reader` and `second-reader`, with the contract of `skills/library-vetting/scripts/models.py` (`detect`, `apply`, `show`), and write `tests/sota-research/test_reader_agents.py`: the rendered agent file of each product lists no shell, read, write or search-in-files tool for the two roles
- [x] T043 [US5] Complete `factory/sota-research/references/procedure.md` for the four phases: (1) settle the aspect, its contexts, its risk dimensions and its boundaries with the owner, start a specification branch with the next number, record the date; (2) research with isolated readers, give each source its class, vet, distil, write the evidence record in ASD-STE100, let the second reader check it, record the answers, place the items, record where the sources disagree and what was not verified; (3) stop and give the owner the findings, the strategy, the disagreements and the open judgements; (4) after the acceptance render and deliver; and the refresh from the watch list. The procedure says: stop before the first source when the agent product cannot limit the tools of an agent; do not store what was read; record the roles of the models and the person who accepted
- [ ] T044 [US5] After the delivery to `main`, on the branch `001-sota-research`: set `- **Target folder**: \`factory/sota-research/\`` and the acceptance in that specification, render it, and deliver the rendered `SKILL.md` and `references/checklist.md` into `factory/sota-research/` on `main`, in place of the first `SKILL.md` of T001
- [ ] T045 [US5] Do one trial run with the owner on a small aspect that the owner names, and record the result against SC-005 and SC-007 in `specs/002-research-tooling/quickstart.md`
- [x] T046 [US5] Complete `docs/sota-research.md` with the four phases, and add a section for the change to `CHANGELOG.md`

**Checkpoint**: commit the phase.

---

## Phase 8: Polish

- [x] T047 Run each scenario of `specs/002-research-tooling/quickstart.md` and correct what differs
- [x] T048 [P] Make sure that the job for Python 3.14 in `.github/workflows/test.yml` runs the tests of `tests/sota-research`, and that the jobs for older versions pass without them
- [x] T049 Measure `check.py` on the specification 001 against SC-006 (less than 10 seconds) and record the time in `specs/002-research-tooling/quickstart.md`

---

## Phase 9: Review

**Purpose**: an independent review of the code against the specification and the contracts,
and the correction of its findings

- [x] T051 Let a second model review `factory/sota-research/` for wrong results, input that causes a crash, the security of the collection step, same output for same input, and tests that cannot fail
- [x] T052 Make `factory/sota-research/scripts/aspect.py` read and write with the same rule for a line (only a line feed ends a line), keep the line ends of a file, accept a byte order mark, and report a file that is not UTF-8 as input that cannot be read
- [x] T053 In `factory/sota-research/scripts/check.py`: fail on an empty checklist and on no sources; an item needs one usable source (read, and confirmed if it is independent); a rejection by a gate is stronger than an earlier confirmation; the acceptance needs a person and a date
- [x] T054 In `factory/sota-research/scripts/render.py`: write the description as a quoted string; refuse a target folder outside the repository, a commit or a branch that can break the stamp, and a pending level; make the digest independent of the line end
- [x] T055 In `factory/sota-research/scripts/place.py` and `factory/sota-research/scripts/vet.py`: report a cell that cannot be written; accept whole numbers only; refuse a rubric that can give a cost of zero
- [x] T056 In `factory/sota-research/scripts/vet.py`: read only public addresses and refuse a redirect to a local address; give a page a time limit; record each error of a page; ignore a date that does not exist or is after the day of the collection; accept only identifiers of the form `S-<number>`; do not use facts of an earlier run, signals of a different address or a signal file of the wrong form
- [x] T057 Write `tests/sota-research/test_robust.py` with one test for each finding, and make `tests/sota-research/test_fresh.py` and `tests/sota-research/test_messages.py` able to fail on each branch

---

## Phase 10: Tests inside the programs

**Purpose**: direction of the owner, 2026-10-09: use doctest in place of test files as much as
possible, so that an installed program validates itself; measure the coverage; let ruff
examine all new code

- [x] T058 Create `factory/sota-research/scripts/sample.py` with the sample specification, its evidence and vetting records, the signal files, two pages and the table of planted defects, and with the helpers `folder`, `work` and `run`
- [x] T059 Give each program in `factory/sota-research/scripts/` the option `--selftest`, which runs its examples and prints the number of examples and of failures
- [x] T060 Move each test of `tests/sota-research/` into its program as an example: short examples in the docstring of a function, scenarios in the table `__test__` at the end of the file
- [x] T061 Remove the folder `tests/sota-research/` with its fixtures
- [x] T062 In `tests/test_repo.py`: run each program of `factory/` with `--selftest` under coverage, fail below the minimum of `pyproject.toml`, and accept an artifact whose programs validate themselves in place of a folder `tests/<name>/`
- [x] T064 Send the coverage report of each branch and each pull request to Codecov from `.github/workflows/test.yml` with OIDC, and set the rules for a change in `codecov.yml`: the project must not lose more than one point, and the lines of a pull request need 90 percent
- [x] T063 Add `coverage` to the development group in `pyproject.toml`, and write the rule for tests into `AGENTS.md`

---

## Phase 11: Examples in the documentation of each function

**Purpose**: direction of the owner, 2026-10-09: the examples belong into the documentation of
the function or the class that they test, not into a `__test__` table; use the coverage report
to add the tests that are missing

- [x] T065 Move each example of the `__test__` tables into the docstring of the function or the class that it tests, in each program of `factory/sota-research/scripts/`, and remove the tables
- [x] T066 Make each example show its result; replace the loops with `assert` where a printed result is possible
- [x] T067 Add an example for each line that the coverage report shows without one: the class `Doc` and the errors of the reader, an identifier that is used two times, the short report, the parts of a skill that a specification can leave out, the network read (from a server on the same computer), the collector that fails, the command `apply`
- [x] T068 Give `models.py apply` the option `--root DIR`, so that its example writes into a temporary folder
- [x] T070 Replace the CI job for Python 3.13 with the job for Python 3.14 in `.github/workflows/test.yml`, so that this branch adds no third version; the migration of all other code to one version is a different pull request
- [x] T069 Increase the coverage minimum in `pyproject.toml` to 95 percent, and write the rule for examples into `AGENTS.md`

---

## Phase 12: First trial of phase 1

**Purpose**: a new agent session did phase 1 of the procedure for the aspect DevSecOps, with a
simulated owner. This phase corrects what the trial found.

- [x] T071 Let an agent that knows only `factory/sota-research/SKILL.md` do "Before the first run" and phase 1 in an isolated copy of the repository, and collect its notes on the procedure
- [x] T072 Give `factory/sota-research/scripts/check.py` the option `--scope`, which examines only the head line and section 1: in phase 1 the other sections are empty and failed the check
- [x] T073 Complete phase 1 in `factory/sota-research/references/procedure.md`: settle the short name, the field and "for whom" with the owner; find the next number from all branches, local and remote; stop if `main` does not have the tooling; write `pending` for the research date; run the check with `--scope`; show section 1 to the owner and stop; commit and push after the agreement
- [x] T074 Add `tests/conftest.py`, which removes the git variables of a hook from the environment of the tests: in a commit inside a worktree, two tests of `library-vetting` wrote into the index of the repository

---

## Phase 13: No narrowing before the research

**Purpose**: direction of the owner, 2026-10-09: the trial of phase 12 was not valid. The
scoping narrowed the aspect to one use case before the research, and the simulated owner added
a use case that belongs two steps later. The narrowing was built into the specification.

- [x] T076 In the specification 001 (pull request into its branch): settle only the field and the thing to build before the research; retire C-01 and add C-23; record the decision
- [x] T077 In this specification: change FR-019 and add FR-019a; the contexts, the risk dimensions and the boundaries are findings of the research with a source each
- [x] T078 In `.specify/templates/overrides/aspect-spec-template.md` and `.specify/memory/constitution.md`: divide section 1 into what is settled before the research and what the research finds
- [x] T079 In `factory/sota-research/scripts/check.py`: `--scope` examines only the head line, the aspect, the field and the date of the agreement; the complete check needs a source or "judgement" for each context, risk dimension and boundary
- [x] T080 In `factory/sota-research/scripts/render.py`: leave the source of a risk dimension out of the rendered skill
- [x] T081 In `factory/sota-research/references/procedure.md`: phase 1 asks only for the field and the thing to build; phase 2 finds the rest in the sources; phase 3 shows it to the owner first
- [ ] T082 Do the trial again for the aspect DevSecOps, through the research, with an owner who says only the field and the thing to build

---

## Phase 14: Each view of an aspect has its basic practices

**Purpose**: the trial for DevSecOps gave a checklist with 19 of 26 items for security, and no
item for static analysis, coverage or fuzzing. Nothing found the views of the aspect or checked
that each view has its basic practices (FR-031).

- [x] T083 In `.specify/templates/overrides/aspect-spec-template.md`: add the field "Views" to section 1 and the column "View" to the checklist
- [x] T084 In `factory/sota-research/scripts/aspect.py` and `sample.py`: read the views and the view of each item; give the sample two views
- [x] T085 In `factory/sota-research/scripts/check.py`: fail for an item without a known view, a view without an item and a view without an item on level 1; report the items and the sources of each view
- [x] T086 In `factory/sota-research/scripts/render.py`: show the view of each item in the checklist; tell the agent to show the selection in groups by view
- [x] T087 In `factory/sota-research/scripts/place.py`: an example shows that `--write` keeps the column "View"
- [x] T088 In `factory/sota-research/references/procedure.md` and `docs/sota-research.md`: name the views from the sources in phase 2, read sources for each view, and show the views to the owner first in phase 3

## Phase 15: A reader for converted files

**Purpose**: FR-032. A web reader cannot open a PDF file, and the session must not read the
text of a source. Measured in the agent product of this repository, 2026-10-10: the web fetch
tool does not read a local server, a hook in an agent file does not limit the agent, and a
hook in the settings file of the project does.

- [x] T089 In `factory/sota-research/scripts/pdf.py`: write the empty marker `.reader-may-read` beside the Markdown file; refuse a target in a git repository and a folder that holds other files and no marker
- [x] T090 Add `factory/sota-research/scripts/guard.py`, the hook: a call of a different agent passes; the agent `sota-file-reader` reads only a file whose resolved folder holds the marker and is not in a git repository
- [x] T091 In `factory/sota-research/scripts/models.py`: add the role `file-reader` with the read tool only and the template `agent-templates/sota-file-reader.md`; `apply` merges the hook into the settings file of the project; without such a hook, the file reader is not written
- [x] T092 In `factory/sota-research/prompts/reader.md` and `prompts/second-reader.md`: a source is an address or the path of a converted file; for a file, the location is the page number
- [x] T093 In `factory/sota-research/references/procedure.md`: the third agent file and the hook before the first run; in phase 2, convert a PDF source and give the path to the file reader; a new file reader does the second reading of its rows
- [x] T094 In `.specify/memory/constitution.md`, principle III: the agent product enforces the limit of the reader of converted files (version 3.3.2)
- [x] T095 Verify in a scratch project outside the repository, with the smallest model: the file reader reports the title on page 1 of a converted PDF source, and the hook refuses a file of the project

## Phase 16: The trial of a recipe

**Purpose**: FR-033 to FR-037. Two trials of a recipe on a real project gave a poor plan,
while each check of the tooling passed: the plan built by hand what maintained components
offer, built a construction for one project, and covered one point of view only. The factory
had no step that tries a recipe on a project and feeds the findings back.

- [x] T096 In `factory/sota-research/scripts/render.py`: add the option `--trial DIR`; refuse a folder in a git repository and the use with `--out`; do not ask for the acceptance; write a stamp that says that the file is a trial rendering
- [x] T097 In `tests/test_repo.py`: the test of the stamps fails for a trial rendering in the repository
- [x] T098 Write `factory/sota-research/prompts/plan-review.md`: the task of a reviewer that answers fixed questions from seven viewpoints with a file and a line, and ends with findings that each have a viewpoint and a route
- [x] T099 In `factory/sota-research/scripts/aspect.py` and `sample.py`: read `trial.md` with the tables "Trials" and "Findings", and the field "Targets" of section 1; give the sample one trial, two findings and one target
- [x] T100 In `factory/sota-research/scripts/check.py`: fail for a finding with an unknown trial, viewpoint or route, an empty text or a wrong status; list the open findings and a recipe without a trial under "What remains"
- [x] T101 In `factory/sota-research/scripts/check.py`: fail for a field "Targets" without a target and without `(none found)`, and for a target without a source; do not examine the field with `--scope`
- [x] T102 In `factory/sota-research/scripts/render.py`: put the targets into `SKILL.md`, and tell the agent to give in the plan the level of each target and what stops the next level
- [x] T103 In `.specify/templates/overrides/aspect-spec-template.md`: add the field "Targets" to section 1 and `trial.md` to "Files beside this specification"
- [x] T104 In `factory/sota-research/references/procedure.md`: add the part "The trial of a recipe" after phase 3, refer to it from phase 3 and from "The refresh", and find the targets in phase 2
- [x] T105 In `docs/sota-research.md` and `CHANGELOG.md`: the trial, the review, the record of the trials and the measured targets

## Phase 17: The intent of the owner and input without bias

**Purpose**: FR-038 to FR-042. An audit of two trials of the tooling for one aspect found
biased input. The repository of the trial was a copy of this kit, and its texts came back as
findings. Both specifications repeated the example names of the template. Phase 1 did not ask
for the intent of the owner, so the research took the meaning of the aspect from the
literature that carries its name. 11 of 180 answers of risk and reward named a source, and no
report gave that share. Direction of the owner, 2026-10-10: the factory finds the stakeholders
and their concerns itself, and does not ask the owner for them.

- [x] T106 In `.specify/templates/overrides/aspect-spec-template.md`: replace each example that names a real concern, dimension, context, level reason or risk with a neutral placeholder; do the same in `factory/sota-research/references/procedure.md`, `prompts/reader.md`, `prompts/risk-answers.md` and `docs/sota-research.md`
- [x] T107 In `factory/sota-research/scripts/check.py`: an example shows that each line of the research in the template has the placeholder `[name]`, and that `--scope` passes on a copy of the template with the fields of phase 1 filled
- [x] T108 Add `factory/sota-research/scripts/export.py`: write a neutral kit into a new or empty folder outside each git repository; leave out the sample and the task of the reviewer; make the two instruction files; refuse a kit that holds a word of `--words`, with the file and the line
- [x] T109 Verify in a scratch folder outside the repository: export, make a repository with one commit, and run `check.py`, `models.py detect` and `render.py` with `uv run`
- [x] T110 In `.specify/templates/overrides/aspect-spec-template.md`: add the field "Intent of the owner" to the part of section 1 that is settled before the research, and the field "Stakeholders" with the form `(stakeholders: <name>, <name>)` in the line of a view to the part that the research finds
- [x] T111 In `factory/sota-research/scripts/aspect.py` and `sample.py`: read the intent, the stakeholders and the stakeholders of each view; give the sample an intent with three lines and two stakeholders
- [x] T112 In `factory/sota-research/scripts/check.py`: with `--scope` and without it, fail for an intent that is absent or empty and for an answer without a date; list an intent that was not asked under "What remains"
- [x] T113 In `factory/sota-research/scripts/check.py`: outside `--scope`, fail for no stakeholder, a stakeholder without a concern or a source, a view without a stakeholder and a view with an unknown stakeholder; list the stakeholders that are in no view under "What remains"; give the number of stakeholders of each view
- [x] T114 In `factory/sota-research/scripts/check.py`: report the number of answers of risk and reward with a source and by judgement, in the text report and with `--json`; `place.py` takes the names of the answers from `check.py`
- [x] T115 In `factory/sota-research/scripts/render.py`: show the stakeholders of each view in the table of the views in `SKILL.md`
- [x] T116 In `factory/sota-research/references/procedure.md`: phase 1 asks the three questions of the intent and does not ask for stakeholders or viewpoints; phase 2 finds the stakeholders and compares the intent with the sources; phase 3 gives the intent first and the line of the answers with the checklist; a trial of the tooling starts with `export.py`, and the reviewer gets its task from the repository of the factory
- [x] T117 In `docs/sota-research.md` and `CHANGELOG.md`: the intent of the owner, the stakeholders, the line of the answers and the export of a neutral kit

---

## Phase 18: A neutral environment, the seeds, and a skill that works alone

**Purpose**: FR-043 to FR-047. Decision of the owner, 2026-10-10: the factory can use the
personal environment of the owner and this repository; a skill that the factory creates must
work alone; the repository must be able to set up a neutral environment of the factory again
and to retrieve the seed documents and standards.

- [x] T118 Add `factory/sota-research/references/seeds.md`: the table of the seeds, the table of the bodies of knowledge of each field, how to retrieve the seeds, how to read the SWEBOK Guide and how to add a row; move the row of `references/bodies-of-knowledge.md` into it and remove that file
- [x] T119 Add `factory/sota-research/scripts/seed.py`: `list` prints the rows and fails for a malformed row; `get` retrieves each seed into a work folder outside each git repository, with `--file`, `--from`, `--today` and `--fresh`, reuses the functions of `pdf.py`, continues after a seed that fails, reports a changed digest and writes `seeds.json`
- [x] T120 In `factory/sota-research/scripts/export.py`: the function `write` writes the files of a kit; add `references/viewpoints.txt` to the files that are left out
- [x] T121 Add `factory/sota-research/scripts/init.py`: export the kit, write the marker `.factory-kit` with the commit, make the git repository, retrieve the seeds and print the next steps; `--again` removes only a folder with the marker and keeps the work folder
- [x] T122 In `factory/sota-research/scripts/render.py`: write nothing when a rendered file refers to the factory, to this repository or to an absolute path, and give the file, the line and the text
- [x] T123 Add `factory/sota-research/references/viewpoints.txt`; in `factory/sota-research/scripts/check.py`, read the names from it, skip the check of the viewpoint when the file is absent and list the findings under "What remains"; keep the names out of the examples of `check.py` and `aspect.py`
- [x] T124 In `factory/sota-research/references/procedure.md`: `init.py` and `seed.py get` before the first run; the bodies of knowledge from the converted files through a file reader; `seed.py get --from --fresh` in the refresh; the trial project gets only the rendered skill folder, and its session starts in a clean environment
- [x] T125 In `docs/sota-research.md` and `CHANGELOG.md`: the seeds, the setup of a neutral environment and the rule that a created skill works alone
- [x] T126 Verify in a scratch folder outside each repository: `init.py` with the file of the SWEBOK Guide, `init.py --again`, and `seed.py get` a second time; the kit holds no file of the guide

---

## Dependencies & Execution Order

- **Phase 1 → Phase 2 → US1**: in this order. US1 is the MVP.
- **US2** needs US1 (the renderer runs the rules of the check).
- **US3** needs Phase 2 only. Its Level cells are read by the check of US1.
- **US4** needs Phase 2 only. The check of US1 reads its confirmations.
- **US5** needs US1 to US4.
- **Phase 8** needs all stories.

US3 and US4 can be built in parallel after US1. In each story: fixtures and tests first, and
they must fail before the implementation.

## Parallel example: User Story 1

```text
T010 defect fixtures            (files in tests/sota-research/fixture/defect-*/)
T011 fixtures for --previous    (files in tests/sota-research/fixture/previous/)
```

## Implementation Strategy

1. Phases 1 and 2, then US1 to US5 and Phase 8, one commit for each phase, on the working
   branch.
2. Merge the working branch as a whole into `002-research-tooling`.
3. Deliver `factory/`, `tests/`, `docs/` and the rule files to `main` in one pull request.
4. Then apply the tooling to the specification 001 on its branch (the checkpoints of US1 and
   US4, T044), and do the trial run with the owner (T045).
