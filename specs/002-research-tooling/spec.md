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
- **FR-032**: For a source that is a PDF file, the tooling MUST write the text of the file,
  with one heading for each page, into a work folder outside the repository. The session MUST
  NOT read that text. A reader that has the read tool only MUST read it and give the page as
  the location. The agent product MUST enforce that this reader reads only converted files of
  the work folder: a hook does that, not a written rule. Where the agent product has no such
  hook, the tooling MUST NOT write this reader, and MUST say that a PDF source cannot be read.

**All parts**

- **FR-028**: Each part MUST write to the person in the loop in ASD-STE100 Simplified
  Technical English.
- **FR-029**: Each program MUST give the same output for the same input, MUST sort its
  output, and MUST have tests that do not use the network.
- **FR-030**: The tooling MUST obey the rules of `AGENTS.md` for a skill, for the programs
  and for the tests.

**Views of an aspect**

- **FR-031**: The skill MUST find the views of the aspect in the sources, and MUST read
  sources that hold the state of the art of each view. A view is a set of concerns of the
  aspect. Each item MUST name one view of section 1. The check MUST fail for an item without
  a known view, for a view without an item, and for a view without an item on level 1 when no
  level is pending. The check MUST report, for each view, the number of items on each level
  and the number of sources that they cite. The rendered skill MUST show the view of each
  item, and MUST tell its agent to show the selection in groups by view.

**The trial of a recipe**

- **FR-033**: The renderer MUST have a trial rendering. It renders a specification that the
  owner did not accept, only into a folder that is outside each git repository. The check of
  the specification MUST pass. The stamp of each file MUST say that the file is a trial
  rendering, so that nobody takes a trial file for a delivered file. Without the option, the
  renderer MUST behave as before.
- **FR-034**: The tooling MUST hold the task for a reviewer that did not write the plan. The
  reviewer reads the plan and the selection in the trial project and, if there is one, a
  reference state of the same project. It answers fixed questions from seven viewpoints:
  architecture, operations, quality, development, security, product owner, and the views of
  the recipe. Each answer MUST be `yes`, `partly`, `no` or `not applicable`, with a file and a
  line of the trial project and one sentence. The reviewer MUST end with a list of findings,
  each with its viewpoint and a proposed route: `recipe`, `tooling` or `implementation skill`.
  The reviewer MUST NOT correct anything.
- **FR-035**: An aspect specification MAY have a record of the trials, `trial.md`, with the
  table of the trials and the table of the findings. The check MUST fail for a finding with an
  unknown trial, an unknown viewpoint, an empty text, an unknown route or a status that is not
  `open`, `corrected in <revision or commit>` or `declined: <reason>`. The check MUST list the
  findings that are open under "What remains". Without the file, the check MUST say under
  "What remains" that the recipe has no trial, and MUST NOT fail.
- **FR-036**: An aspect specification MUST name the measured targets of its aspect in
  section 1: for each target the name, the scale, what measures it, and the source. The value
  `(none found)` is permitted. The check MUST fail for an empty field and for a target without
  a source, but not in the check of phase 1. The rendered skill MUST hold the targets, and
  MUST tell its agent to give, in the plan, the level of each target that the plan reaches and
  what stops the next level.
- **FR-037**: The procedure MUST have the trial of a recipe: a trial rendering, a copy of a
  project that the owner names as a new repository without its history, a new session that
  only uses the skill and stops at the plan, a reviewer that did not see the research, the
  record of the findings, and the decision of the owner for each finding. A finding with the
  route `recipe` MUST lead to more research for its view or question, and to a new trial.

**The intent of the owner and input without bias**

- **FR-038**: The template of an aspect specification, the procedure, the prompts and the
  documentation of the tooling MUST NOT hold an example that names a real concern, dimension,
  context, level reason or risk. A placeholder MUST be neutral, for example `[name]`. The
  check MUST NOT depend on a word of the template. The sample specification of the examples
  is permitted: a session of the research does not get it.
- **FR-039**: The tooling MUST have an export of a neutral kit for a trial of the tooling
  itself. The export writes, only into a new or empty folder outside each git repository: the
  tooling without the sample specification and without the task of the reviewer of a plan,
  the template of an aspect specification, the rules of the kit, the programs of a different
  skill that the tooling loads, and two instruction files that hold only the language for the
  owner, the rule for commit messages, the rules of the kit and where the procedure is. It
  MUST NOT write documentation, tests, specifications or a different skill. Given a list of
  words, it MUST write nothing when an exported file holds a word, and MUST give the file and
  the line. The procedure MUST work in such a kit.
- **FR-040**: Before the research, the skill MUST ask the owner three questions about the
  intent, each one time and only if the owner did not answer it already: what the owner means
  by the aspect and which concerns it brings together; what a project must be able to show
  after it applied the recipe, and whether there is a measurable target; what the owner does
  not want. The skill MUST write each answer as a quote with its date into the field "Intent
  of the owner" of section 1, MUST NOT change the words, and MUST write `(no answer)` when
  there is none. It MUST NOT ask for and MUST NOT propose a use case, a first user, a
  reference project, an industry, a product, stakeholders, viewpoints, views, contexts, risk
  dimensions or boundaries, and MUST NOT write a project for a trial into the specification.
  In the research, the skill MUST compare the intent with the sources, record each difference
  in section 3.4 and follow the owner. Each concern that the owner named is a view, or section
  7 says why it is not. A target that the owner named is in the field "Targets" with
  `(judgement)` until a source gives its scale. In the review, the owner MUST get the intent
  first, beside the stakeholders, the views and the targets, with each difference. The check
  of phase 1 MUST fail when the field is absent or empty, or when an answer has no date. When
  each line says `(no answer)`, the check MUST pass and MUST list under "What remains" that
  the intent was not asked.
- **FR-041**: The skill MUST find the stakeholders of the aspect in the body of knowledge of
  the field and in the sources, not in the name of the aspect, and MUST NOT ask the owner for
  them. A stakeholder is a group of persons that has an interest in the result or carries a
  duty for it. Section 1 MUST name each stakeholder with its concerns and its source. The
  skill MUST aggregate the concerns into the views, and each view MUST name its stakeholders
  in a form that a program reads. The requirements of the stakeholders of a view are the
  candidates for its items; the calculation of risk and reward decides on them. FR-048
  gives the exits of a requirement and supersedes the row in section 7 for a requirement
  that was dropped before the calculation. Outside
  the check of phase 1, the check MUST fail when section 1 names no stakeholder, when a
  stakeholder names no concern or no source, when a view names no stakeholder, and when a
  view names a stakeholder that section 1 does not have. The check MUST list under "What
  remains" each stakeholder that is in no view, and MUST give the number of stakeholders of
  each view. The rendered skill MUST show the stakeholders of each view. In the review, the
  owner can add, remove or rename a stakeholder.
- **FR-042**: The check MUST report, in one line, how many answers of risk and reward in the
  table "Items" of `vetting.md` name a source and how many say `judgement`. The line MUST NOT
  fail the check, and MUST be in the JSON report. In the review, the owner MUST get this line
  with the checklist.

**A register of the requirements, and sources of the own field of a view**

Iteration I-3, 2026-10-11. The registered trial of I-2 was refuted, and its registration
fixed this change: how the research finds the basic practices of each view. The session
dropped requirements of the sources before the calculation, one requirement of the evidence
record became no item, and one view had no source of its own field.

- **FR-048**: `vetting.md` MUST hold a table "Requirements" with one row for each requirement
  that a source states for a stakeholder: the identifier `R-<nn>`, the requirement in one
  sentence, the stakeholder, the view, the source with its location, and the cell "Goes to".
  The reader of a source MUST report each requirement of the source as its own point, with
  the group of persons that it serves and the location. The session MUST record each one
  without a judgement. The cell "Goes to" MUST have one of five forms: `C-<nn>`, a checklist
  item; `3.3: <decision>`, a decision of section 3.3; `5`, an implementation skill;
  `boundary: <name>`, a boundary of section 1; `duplicate: R-<nn>`, a row that is not a
  duplicate. No other exit is permitted. A requirement that is basic in its view becomes an
  item also when its cost is high, and the calculation places it. The check MUST fail, outside
  the check of phase 1, when the table is absent or empty; when a cell is empty; when an
  identifier is used two times; when the cell "Goes to" has no such form or names a row that
  does not exist or an item that is retired; when a stakeholder or a view is not in section
  1; when the source is not in section 2; when an item that is not retired holds no
  requirement and is not admitted by `own rule`; and when a stakeholder of section 1 has no
  requirement. The report MUST give, for each view, the number of requirements and the number
  for each exit, also in the JSON report. The check MUST list under "What remains" each view
  with more than half of its requirements at a boundary. In the review, the owner MUST get
  this part with the views.
- **FR-049**: Each source of section 2 MUST name, in the cell `Views`, the views that it was
  read for, or `all` for a body of knowledge. For each view, the skill MUST find and read the
  references of the field of that view: the standards and references that the body of
  knowledge names for the knowledge areas of the view, and the results of a search in the
  words of the view. The check MUST fail when the cell names a view that section 1 does not
  have, and when the cell is present and empty. A specification without the cell MUST NOT
  fail for it. The check MUST list under "What remains" each view with fewer than two sources
  that were read in full or in part for it and do not say `all`, and MUST give this number in
  the part "Views".

**A neutral environment, the seeds, and a skill that works alone**

Decision of the owner, 2026-10-10: the factory can use the personal environment of the owner
and this repository. A skill that the factory creates must work alone. The repository must be
able to set up a neutral environment of the factory again, and to retrieve the seed documents
and standards.

- **FR-043**: The tooling MUST hold a manifest of the seeds: the documents and standards that
  the factory starts from. Each row names the identifier, the document, the issuer, the
  version or the date, the kind, the address, the digest of the file, the terms of the issuer
  and the date when the row was read. The kind is `pdf`, `page` or `owner file`. The digest
  can be empty. The manifest MUST say which seeds are the bodies of knowledge of which field.
  It MUST NOT hold the content of a seed. A row enters the manifest only from the page of the
  issuer, read in the same turn, and after the owner accepts it. A program MUST print the
  rows, sorted, and MUST fail for a row with an unknown kind, an address that is not `http` or
  `https`, a digest that is not 64 hexadecimal characters, or an absent cell.
- **FR-044**: A program MUST retrieve the seeds into a work folder outside each git
  repository. For the kind `pdf`, it downloads the file with the limits and the rules of the
  converter of FR-032, keeps it, and writes its text as that converter does. For the kind
  `owner file`, it uses the file that the owner gives; without one, it reports that the owner
  must give the file, with the address. For the kind `page`, it only records the seed. Given
  the folder of an aspect specification, it MUST retrieve also each source of section 2 whose
  address ends in `.pdf`. One seed that fails MUST NOT stop the program. The program MUST
  write one sorted record with the state of each seed: `retrieved`, `owner must give the
  file`, `recorded`, `failed: <reason>` or `changed`. The record holds no current time. When
  the digest of a file is not the digest of the manifest or of the last run, the state MUST
  be `changed`, the file MUST be converted, and the result code MUST be 1. Without a digest in
  the manifest, the program MUST print the digest. A file that is in the work folder MUST NOT
  be retrieved again, unless an option tells the program to download each file again.
- **FR-045**: A program MUST set up a neutral environment of the factory from nothing, in two
  folders outside each git repository, neither in the other. It writes the neutral kit of
  FR-039, a marker file with the commit of this repository, a git repository in the kit with
  the branch `main` and one commit, and the seeds of FR-044 in the work folder. Then it MUST
  print what a person does next. Without the program `git`, it MUST say so and continue. With
  an option, it MUST remove a kit that holds the marker file and make it again, and MUST keep
  the work folder. It MUST NOT remove a folder without the marker file. The kit MUST NOT hold
  a seed document or its converted text.
- **FR-046**: A rendered skill MUST work alone, without the factory and without this
  repository. The renderer MUST write nothing when a rendered file refers to a path that
  starts with `factory/`, `specs/`, `.specify/`, `rules/` or `tests/`, uses the word
  `constitution`, or holds an absolute path. It MUST give the file, the line and the text.
  The rules of the kit are text in the skill. In a trial, the trial project MUST get only the
  folder of the rendered skill, and the session of the trial MUST start in a clean
  environment: no personal plugin, connector, skill or instruction file.
- **FR-047**: The names of the viewpoints of the review MUST be in a data file that the
  export of FR-039 leaves out, as it leaves out the task of the reviewer. No program that is
  exported holds the list. When the file is absent, the check MUST NOT examine the viewpoint
  of a finding, and MUST list under "What remains" the findings whose viewpoint was not
  checked.

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
- **Intent of the owner**: the answers of the owner to three questions before the research,
  each as a quote with its date.
- **Stakeholder**: one group of persons that has an interest in the result or carries a duty
  for it, with its concerns for the aspect and its source.
- **View**: one set of concerns that an aspect brings together, with its stakeholders and its
  source. Each checklist item belongs to one view.
- **Requirement**: one thing that a source says a project must or should do, with its
  stakeholder, its view, its source and its one exit.
- **Risk dimension**: one dimension on which the risk of a project differs for an aspect, with
  the question that finds it out.
- **Target**: one measurable result that a project reaches when it applies the recipe, with
  its scale, what measures it, and its source.
- **Trial**: one application of a recipe that is not delivered to a copy of a project, up to
  the plan.
- **Trial finding**: one defect of a plan that a reviewer found, with its viewpoint, its route
  and its status.
- **Seed**: one document or standard that the factory starts from, with its issuer, version,
  kind, address, digest and terms. The repository holds the row, not the document.
- **Work folder**: a folder outside each git repository that holds the retrieved seeds, their
  converted text and the record of their states.
- **Kit**: a neutral copy of the tooling in a folder outside each git repository, with a
  marker file that names the commit that it comes from.
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
