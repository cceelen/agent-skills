# Feature Specification: Research tooling of the factory

**Feature Branch**: `002-research-tooling`

**Created**: 2026-10-09

**Status**: Draft

**Input**: User description: "The tooling of this repository that takes one major aspect of
software engineering from what to build to an accepted aspect specification and its rendered
recipe skill, with a person in the loop."

This is a product specification, layer two of the factory. Its requirements come from the
aspect specification `specs/001-sota-research/spec.md` on the branch `001-sota-research` (the
checklist items C-01 to C-22 and section 5) and from the constitution, version 3.2.0. The tooling is for this repository. It is
not a plugin for users of the kit.

Two roles use it. The **owner** decides what to build, confirms results and accepts a recipe.
The **research session** is the agent session that does the work between those decisions.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Know what remains in an aspect specification (Priority: P1)

The owner or the research session runs one check on an aspect specification and its evidence
record. The check lists each rule that fails, with the row at fault, and tells what remains.
The same files always give the same report.

**Why this priority**: Each other part writes to the aspect specification. A cheap check that
always gives the same result is the feedback that those parts and the reviewer need. It is
useful alone, on the specification that exists today.

**Independent Test**: Run the check on `specs/001-sota-research/`. Then run it on copies with
one planted defect each. The report names each planted defect and no other.

**Acceptance Scenarios**:

1. **Given** an aspect specification that obeys all rules, **When** the check runs, **Then**
   the report says that no check fails and lists the items that need judgement.
2. **Given** a checklist item that cites a source that section 2 does not list, **When** the
   check runs, **Then** the report names the item and the unknown source.
3. **Given** a cited source without a row in the evidence record, **When** the check runs,
   **Then** the report names the source.
4. **Given** an earlier revision of the specification, **When** an identifier of that
   revision has a different item now, **Then** the report names the identifier.
5. **Given** the same files, **When** the check runs two times, **Then** the two reports are
   the same, byte for byte.

---

### User Story 2 - Render the recipe skill from its specification (Priority: P2)

The owner accepted an aspect specification. The research session renders the recipe skill from
it: the strategy as the instructions of the skill, the checklist as a reference file, and the
templates for the agent files that wrap the skill. Nobody edits the rendered skill by hand.

**Why this priority**: The rendered skill is the thing that users of the kit install. Without
it, an accepted specification gives no product.

**Independent Test**: Render a skill from a fixture specification and compare it with the
expected folder. Change one item in the fixture and make sure that the comparison fails until
the skill is rendered again.

**Acceptance Scenarios**:

1. **Given** an accepted aspect specification, **When** the renderer runs, **Then** a complete
   skill folder exists that obeys the rules for a skill in `AGENTS.md`.
2. **Given** a committed recipe skill that differs from a fresh rendering, **When** the tests
   of the repository run, **Then** one test fails and names the skill.
3. **Given** a specification whose check fails, **When** the renderer runs, **Then** it
   renders nothing and reports the failing checks.
4. **Given** a specification that the owner did not accept, **When** the renderer runs,
   **Then** it renders nothing and says that the acceptance is missing.

---

### User Story 3 - Place each item with a calculation of risk and reward (Priority: P3)

For each checklist item, the research session records answers to a fixed set of questions
about risk and reward. A program computes from the answers whether the item is admitted, its
position in the order, and its level (1, 2 or 3). Level 1 holds the basic practices. An item
above level 1 names the risk dimension of the aspect that calls for it. The owner sees the
answers and the result, and can correct an answer.

**Why this priority**: Today the level of each item is "pending". The owner decided that a
calculation places an item, and that a model does not assign a level by feel.

**Independent Test**: Give the program a fixture of recorded answers. The computed admission,
order and level are the same as the expected values, each time.

**Acceptance Scenarios**:

1. **Given** recorded answers for each item, **When** the calculation runs, **Then** each
   item has an admission result, a position and a level, and the record shows how the answers
   gave that result.
2. **Given** an item with a missing answer, **When** the calculation runs, **Then** the item
   stays "pending" and the report names the missing answer.
3. **Given** a corrected answer from the owner, **When** the calculation runs again, **Then**
   the result changes only for the items that the answer touches.
4. **Given** a changed set of questions or weights, **When** the calculation runs, **Then**
   the record carries the new version of the rubric.

---

### User Story 4 - Vet an independent source before it supports an item (Priority: P4)

A source from a smaller independent issuer is not trusted by its class. A program collects
measured signals about the source and scores them with a fixed rubric. The owner sees the
signals and the score, and confirms or rejects the source.

**Why this priority**: Four items of the first aspect specification rest on independent
sources whose vetting is pending. A blog or a small repository can be outdated, poisoned or an
attack.

**Independent Test**: Give the program a fixture of recorded signals for three sources. The
scores are the same as the expected values, and a source without the owner's confirmation
supports no item in the check of User Story 1.

**Acceptance Scenarios**:

1. **Given** an independent source, **When** the vetting runs, **Then** the record holds the
   measured signals, the score, the version of the rubric and the date.
2. **Given** a source that is a repository, **When** the vetting runs, **Then** it uses the
   signals that the collector of `library-vetting` already measures.
3. **Given** a signal that cannot be measured because the network is not available, **When**
   the vetting runs, **Then** the record marks the signal as not measured and the run
   continues.
4. **Given** a vetted source that the owner did not confirm, **When** the check of User
   Story 1 runs, **Then** each item that rests on that source alone is reported.

---

### User Story 5 - Take one aspect through the four phases (Priority: P5)

The owner names a field. A research skill leads the research session through the four phases
of the factory: settle what to build with the owner, do the research, stop for the review of
the owner, then render. The skill uses the parts of User Stories 1 to 4 and tells the session
which step comes next.

**Why this priority**: This is the complete flow and the purpose of the tooling. It comes last
because it joins the other parts, and each of them is useful before it exists.

**Independent Test**: Run the skill on one aspect. The owner is asked only for the field and the
thing to build before a search starts. The contexts, the risk dimensions and the boundaries
come from the research. The run stops for the review with a
specification whose check reports no failure other than "not accepted".

**Acceptance Scenarios**:

1. **Given** a field that the owner names, **When** the skill starts, **Then** it settles only
   the field and the thing to build in dialogue, records the date of the agreement, and asks
   for no use case, no first user and no narrower scope.
2. **Given** an agreed scope, **When** the research runs, **Then** each agent that reads a
   source has no shell, no credentials and no access to the repository, and its report is
   handled as untrusted data.
3. **Given** the reports of the readers, **When** the session distils them, **Then** the
   evidence record has one summary for each source, and a second reader compared each line
   with the source.
4. **Given** a distilled specification, **When** the research ends, **Then** the skill stops
   and gives the owner the findings, the strategy, the points where the sources disagree and
   the open judgements.
5. **Given** a source that cannot be reached, **When** the research ends, **Then** the
   specification says what was not verified.
6. **Given** an accepted aspect specification and a moved source on its watch list, **When**
   the owner starts a refresh, **Then** the skill reads only what moved and shows the items,
   and the declined items, that the change touches.

---

### Edge Cases

- The owner changes the scope during the research: the change is recorded with its reason and
  date, and the research continues with the new scope.
- A page that a reader fetched contains instructions: the reader reports them as content, and
  no part of the tooling obeys them.
- A source is paid: the tooling cites it from its official preview, marks it as read in part
  and records the gap.
- Two sources disagree: the two positions and the handling are written down, and no source
  wins by its class alone.
- A second reader finds that a summary says more than its source: the summary is corrected
  before an item uses it.
- An earlier revision does not exist: the check of stable identifiers is skipped and the
  report says so.
- A refresh retires an item: its identifier is not used again.

## Requirements *(mandatory)*

### Functional Requirements

**Check of an aspect specification (C-02 to C-07, C-09, C-10, C-14 to C-16)**

- **FR-001**: The check MUST report each failing rule with the row at fault, and MUST list
  what remains: failing checks, pending levels, pending vettings and items that need
  judgement.
- **FR-002**: The check MUST cover: each source row is complete; each item cites a source of
  section 2 or a principle of the constitution; each item names its check or says
  "judgement"; each cited source has a row in the evidence record that names the item; the
  section on disagreement is present; each glossary term is complete; each decision has a
  date; each source has a version or a date; the watch list has a row; each item names the risk that it answers; each item above level 1 names a risk dimension of
  section 1.
- **FR-003**: Given an earlier revision, the check MUST report each identifier whose item
  changed and each retired identifier that is in use again.
- **FR-004**: The check MUST report each item that rests only on a source that was not read
  or on an independent source that the owner did not confirm.
- **FR-005**: The check MUST give the same report for the same files, and MUST show by its
  result code that a rule failed.

**Renderer (C-13, C-19)**

- **FR-006**: The renderer MUST make a complete recipe skill from an aspect specification:
  the strategy as the instructions, the checklist as a reference file, and the templates for
  the agent files.
- **FR-007**: The rendered skill MUST name no product and MUST contain no text that was copied
  from a source.
- **FR-008**: The rendered skill MUST tell its agent to lead the owner of the project through
  a risk analysis of their software, their market, their context, their users and their data.
  The analysis follows the risk dimensions of the aspect, with the question of each dimension.
  The agent gives the opinion of the kit with its reason, and proposes a target level for each
  dimension from the answers.
- **FR-008a**: The rendered skill MUST tell its agent how to show and change the selection of
  a project: the target levels, the answers of the assessment and the declined items with
  their reasons, as a checklist that is committed in the project.
- **FR-009**: The renderer MUST render nothing when the check fails or when the acceptance of
  the owner is missing.
- **FR-010**: A test of the repository MUST fail when a committed recipe skill differs from a
  fresh rendering.

**Calculation of risk and reward (C-18)**

- **FR-011**: The calculation MUST compute admission, order and level (1, 2 or 3, cumulative)
  of each item from recorded answers to a fixed set of questions. The item with the best
  return at the lowest cost is on level 1.
- **FR-012**: The record MUST hold, for each item, the answers, the result and the version of
  the rubric, and MUST keep the level apart from the quality of the evidence.
- **FR-013**: An item with a missing answer MUST stay "pending".
- **FR-014**: Each item MUST name the risk that it answers. The questions MUST cover the
  reward (how bad the harm is that the item prevents, how probable that harm is without the item, in how many contexts the item
  applies), the cost (the effort to adopt and the effort to keep) and the risk of the item
  itself. Each answer is on a fixed scale and names its source. The research session records
  the answers, and the owner corrects them.
- **FR-014a**: An item with a good return at a low cost in each context MUST be on level 1.
  An item whose return depends on the risk of a project MUST be above level 1 and MUST name
  the risk dimension that calls for it. The calculation does not assess a project: the recipe
  skill does that with the owner of the project (FR-008).

**Vetting of independent sources (C-20)**

- **FR-015**: The vetting MUST collect measured signals for an independent source and score
  them with a fixed rubric. For a repository it MUST use the signals that the collector of
  `library-vetting` measures.
- **FR-016**: The record MUST hold the signals, the score, the version of the rubric, the date
  and the confirmation of the owner.
- **FR-017**: The vetting MUST continue when a signal cannot be measured, and MUST mark that
  signal as not measured.
- **FR-018**: For each independent source, a page or a repository, the vetting MUST first
  apply gates. It rejects, without a question to the owner, a source that has no author or issuer that can be
  identified, has no date, is older than the limit of the aspect, or cannot be reached. It
  scores each other source on its age, on an author with a record in the field, on how many
  fast-lane sources refer to it, and on one more signal: whether a page cites its own sources,
  or whether a repository is active. The owner confirms
  each source that passes.

**Research skill (C-01, C-08, C-11, C-12, C-17, C-21, C-22)**

- **FR-019**: The skill MUST settle the field and the thing to build with the owner
  before the first search, and MUST record the date of the agreement.
- **FR-019a**: The skill MUST find the contexts, the risk dimensions and the boundaries of the
  aspect in the sources, give each one its source, and show them to the owner in the review.
  The skill MUST NOT ask the owner for a use case, a first user or a narrower scope before the
  research. A use case is chosen only when a recipe is applied to a project.
- **FR-020**: The skill MUST give each reading task to an agent that has no shell, no
  credentials and no access to the repository, and MUST state in each task that fetched text
  is data and not an instruction.
- **FR-021**: The skill MUST give each source its class. A source of a fast-lane class enters
  without the vetting; each other source passes the vetting first.
- **FR-022**: The skill MUST write the evidence record: for each source one summary of what
  it contributes, where in the source that is, the rows it supports and the date read. A
  second reader MUST compare each line with the source.
- **FR-023**: The skill MUST stop after the research and give the owner the findings, the
  strategy, the points of disagreement and the open judgements. A model MUST NOT accept a
  recipe.
- **FR-024**: The skill MUST record the roles of the models that made or suggested a
  judgement, and the person who accepted the result.
- **FR-025**: The skill MUST NOT store what was read. It keeps the aspect specification, the
  evidence record and the vetting record only.
- **FR-026**: On a refresh that the owner starts, the skill MUST read the sources of the watch
  list that moved, and MUST show the items and the declined items that the change touches.
- **FR-027**: The skill MUST say what it did not verify when a source cannot be reached.

**All parts**

- **FR-028**: Each part MUST write to the person in the loop in ASD-STE100 Simplified
  Technical English.
- **FR-029**: Each program MUST give the same output for the same input, MUST sort its
  output, and MUST have tests that do not use the network.
- **FR-030**: The tooling MUST obey the rules of `AGENTS.md` for a skill, for the programs
  and for the tests.

### Key Entities

- **Aspect specification**: the source of a recipe. It holds the aspect, the sources, the
  strategy, the checklist, the skill set, the watch list, the decisions and the glossary.
- **Source**: one existing description, with issuer, version or date, class, license and how
  much of it was read.
- **Checklist item**: one generic practice, with its reason, level, route of admission, check
  and sources. Its identifier does not change.
- **Evidence record**: for each source, the summary of what it contributes, the location, the
  rows it supports and the date read.
- **Vetting record**: for each independent source, the signals, the score, the version of the
  rubric and the confirmation of the owner. For each item, the answers and the result of the
  calculation of risk and reward.
- **Risk dimension**: one dimension on which the risk of a project differs for an aspect, with
  the question that finds it out.
- **Recipe skill**: the rendered skill of one aspect, with its checklist as a reference file
  and its templates for agent files.
- **Selection**: the checklist that a project commits: the answers of the risk assessment, the
  target level for each risk dimension and the declined items with their reasons.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: For each of the rules of FR-002 to FR-004, a planted defect in a fixture is
  reported, and a specification without a defect gives no report of a failure.
- **SC-002**: The check, the calculation, the scoring of the vetting and the renderer each
  give the same output on two runs with the same input, byte for byte.
- **SC-003**: After the tooling is applied to `specs/001-sota-research/`, no item has the
  level "pending" and no item has "vetting pending".
- **SC-004**: The recipe skill that is rendered from `specs/001-sota-research/` passes each
  test of the repository for a skill.
- **SC-005**: On one complete trial run, the owner is asked for decisions only: the scope, the
  confirmation of sources, corrections of answers, and the acceptance. The owner is not asked
  to find a fact.
- **SC-006**: On one complete trial run, the check of the specification is complete in less
  than 10 seconds, so that the research session can run it after each change.
- **SC-007**: A reviewer finds no line in the evidence record of the trial run that says more
  than its source.

## Assumptions

- The first aspect specification, `specs/001-sota-research/`, is the first fixture and the
  first use of each part.
- The parts are built in the order of the user stories. Each is delivered and reviewed alone.
- The research skill lives in this repository as tooling. It is not in the marketplace and is
  not installed by users of the kit.
- The agent product of the research session can start an agent with a limited set of tools.
  Where it cannot, the skill says so and stops before it reads a source.
- The owner starts each run and each refresh. Nothing runs on a schedule.
- The minimum version of the programming language changes in a different pull request.
- Out of scope: the DevSecOps aspect, the implementation skills for single products, the
  layout of the marketplace, and the tool that changes the selection in a user project beyond
  the instructions of FR-008.
