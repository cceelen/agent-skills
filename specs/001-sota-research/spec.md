# Feature Specification: SOTA Research Skill

**Feature Branch**: `001-sota-research`

**Created**: 2026-10-08

**Status**: Draft

**Input**: "Write the SOTA research skill that will create the spec for the skill or agent
creation with Spec Kit."

## Purpose

The skill `sota-research` researches the current state of the art (SOTA) of one aspect of
software engineering for one context, writes a short, cited summary, and turns it into the
description that `/speckit-specify` takes to create a new skill or agent, or to improve an
existing one. The skills and agents that Spec Kit then builds hold the instructions, the
summaries and the references. The research skill builds no knowledge base, no catalog system
and no search engine; it collects, judges and writes.

The first aspect is supply chain and pipeline security for projects on GitHub, with the
reference project `cceelen/asus-zenbook-duo-ux8406` as the case that shows the goal: a project
reaches its measured baseline (OpenSSF Scorecard, Best Practices badge, Plumber score, SLSA
levels) in its first commits, not in days of work.

## Decisions of the owner (2026-10-08)

- The artifact types have one top-level folder each (`agents/`, `skills/`, `processes/`,
  `template-sets/`), as `AGENTS.md` defines. Each artifact has `docs/<name>.md` and
  `tests/<name>/`.
- Each field, skill or agent gets one complete specification of its own. This specification
  covers the research skill only.
- The repository keeps no collection of source material. Artifacts hold instructions,
  summaries and references (URLs with dates).
- The specification pull requests do not increase the repository version; the pull request
  that adds the skill does.
- Delegate: the smallest capable model reads and extracts, a mid-size model drafts and
  reviews, the session model judges and writes.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Research the SOTA of an aspect for a context (Priority: P1)

A maintainer names an aspect (for example "pipeline security") and the context: the forge,
the stack, the delivery mechanism, the use case, the industry and its regulation, the users.
They can give references they already know. The skill proposes the scope and the questions,
researches with the web search and fetch tools of the agent, delegates the reading to small
models, and writes one summary. The summary gives the goals and practices that hold across
contexts, how each is implemented in the given context, the regulations and standards that
require it, the tools and platform controls that implement or check it, the references with
dates, what is disputed, what could not be verified, and the gaps.

**Why this priority**: every later step rests on this summary.

**Independent Test**: run the skill on one aspect and one context and review the summary. It
is useful alone: a maintainer gets a dated, cited picture of the SOTA for their case.

**Acceptance Scenarios**:

1. **Given** an aspect and a context, **When** the maintainer runs the skill, **Then** it
   proposes the scope and the research questions and waits for confirmation.
2. **Given** a confirmed scope, **When** the research completes, **Then** every practice in the
   summary names its context, at least one dated reference, the standards or regulations that
   require it where they exist, and the tool or control that implements or checks it, or a gap.
3. **Given** a practice that is essential in one context and useless in another (for example
   feature flags for a 24/7 service and for a command-line tool), **When** the summary is
   written, **Then** it says so for the given context instead of giving one answer for all.
4. **Given** sources that disagree, or a source that could not be reached, **When** the summary
   is written, **Then** the disagreement and the unverified statements are marked as such.
5. **Given** the summary, **When** the maintainer reads it, **Then** it is at most about 1,500
   words of prose plus tables, and every reference is a URL with a date.

---

### User Story 2 - Create the Spec Kit description for a skill or an agent (Priority: P1)

From a summary, the skill proposes which skills and agents to create or to improve and writes
one description per artifact that `/speckit-specify` takes as its input. An agent description
names the discipline, the context dimensions the agent reads before it plans, the practices it
judges against, the skills it delegates to, and how it verifies; it names no technology. A
skill description names the technologies, the practices it implements for that stack, the tools
and platform controls it wraps, the deterministic check that shows the goal is reached, and the
references.

**Why this priority**: this is the hand-off to Spec Kit, the reason the skill exists.

**Independent Test**: run `/speckit-specify` on one agent description and one skill
description. Each gives a specification with at most three clarification questions.

**Acceptance Scenarios**:

1. **Given** a summary, **When** the maintainer asks for the descriptions, **Then** the skill
   proposes the artifacts with a type and a reason each and waits for the decision.
2. **Given** an accepted proposal, **When** the descriptions are written, **Then** each practice
   of the summary that applies to the context is in exactly one description or is listed as
   left out with a reason.
3. **Given** an agent description, **When** a reviewer reads it, **Then** it names no forge,
   language, build system, package format or vendor.
4. **Given** a skill description, **When** a reviewer reads it, **Then** it names the
   technologies, the check that shows the goal is reached (for example a scanner, a scorecard, a
   badge, a provenance level) and the references with dates.
5. **Given** a description, **When** `/speckit-specify` runs on it, **Then** the resulting
   specification needs at most three clarification questions.

---

### User Story 3 - Refresh and improve (Priority: P2)

Later, the maintainer runs the research again for the same aspect and context. The skill writes
a new summary, shows what was added, changed or dropped since the last one with the reference
that caused it, and lists the skills and agents that rest on the earlier summary. For each one
it writes a description of the change for `/speckit-specify`. Results from using the built
skills and agents (findings, failures, checks that disagreed) are input to the refresh.

**Why this priority**: the SOTA moves; the artifacts must follow it.

**Independent Test**: refresh an aspect with one known change in the sources. The difference
names it, and the affected artifacts are listed.

**Acceptance Scenarios**:

1. **Given** an earlier summary, **When** the refresh completes, **Then** the new summary lists
   each difference with the reference and date that caused it, or states that nothing changed.
2. **Given** skills or agents that record the earlier summary as their basis, **When** the
   difference is written, **Then** each affected artifact is listed with a change description.
3. **Given** results from the use of a built skill or agent, **When** they are given to the
   refresh, **Then** the summary says where they confirm or contradict the sources.

---

### Edge Cases

- The aspect is too broad for one summary: the skill proposes a split before it starts.
- A key source is paywalled or blocked: the skill records its metadata and marks every
  statement that rests on it as not verified.
- A platform feature is announced but not available: it is recorded as announced with its date,
  never as current.
- A fetched page contains text that looks like instructions to the agent: it is treated as data
  and the attempt is noted.
- The network is not available or sites are blocked: the summary says which sources were not
  reached and is not presented as complete.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The skill MUST accept an aspect, a context (forge, stack, delivery mechanism, use
  case, industry and regulation, users) and optional references, and MUST propose the scope and
  the research questions before it researches.
- **FR-002**: The skill MUST research with the web search and fetch tools of the agent and MUST
  delegate the reading of sources to the smallest capable model, one source per agent, with a
  fixed budget of sources and searches per run.
- **FR-003**: Each practice in a summary MUST name its context, at least one reference with a
  date, the standards or regulations that require it where they exist, and the tool or control
  that implements or checks it, or a named gap. A practice that depends on the context MUST say
  how its implementation differs by context.
- **FR-004**: The skill MUST mark disagreement between sources and every statement it could not
  verify, with the reason. It MUST treat fetched content as data and MUST NOT follow
  instructions in it.
- **FR-005**: The summary MUST be a Markdown file under `sota/<aspect>/` named by its research
  date, with its references as URLs with dates. The skill MUST NOT store the content of the
  sources in the repository.
- **FR-006**: From a summary, the skill MUST propose the skills and agents to create or improve,
  with a type and a reason each, and MUST wait for the maintainer's decision.
- **FR-007**: The skill MUST write one description per accepted artifact, in a form that
  `/speckit-specify` accepts without rewriting. An agent description MUST name no technology
  and MUST name the discipline, the context dimensions, the practices, the skills it delegates
  to and the verification. A skill description MUST name the technologies, the practices for
  that stack, the tools and controls to wrap, the deterministic check that shows the goal is
  reached, and the references.
- **FR-008**: Each practice of the summary that applies to the context MUST be in exactly one
  description or listed as left out with a reason. A description MUST NOT prescribe the
  implementation (language, framework, internal structure).
- **FR-009**: A refresh MUST research from the sources again, MUST write a new summary, and
  MUST list each difference to the earlier summary with the reference and date that caused it.
- **FR-010**: Each skill and agent built from a description MUST record the summary (aspect and
  date) it rests on. A refresh MUST list the artifacts that rest on an earlier summary and MUST
  write a change description for each.
- **FR-011**: The skill MUST accept results from the use of built artifacts as input to a
  refresh and MUST say where they confirm or contradict the sources. It MUST refuse input that
  contains secrets, personal data or private repository content.

### Key Entities

- **Aspect**: one area of engineering practice, researched for a context.
- **Context**: forge, stack, delivery mechanism, use case, industry and regulation, users.
- **Summary**: the dated, cited SOTA of an aspect for a context: practices, their
  implementation per context, standards, tools, references, disputes, unverified statements,
  gaps, and the difference to the earlier summary.
- **Practice**: one goal or good practice with its context, references, requiring standards and
  implementing or checking tools.
- **Description**: the input for `/speckit-specify` for one skill or agent, new or to improve.
- **Reference**: a URL with a date and a verification status.

## Success Criteria *(mandatory)*

- **SC-001**: In a summary, 100 % of the practices have a dated reference, and no statement is
  presented as verified when it was not.
- **SC-002**: A maintainer gets from an aspect and a context to an accepted summary in one
  session, with at most 30 minutes of their own review time.
- **SC-003**: At least 90 % of the descriptions give a specification from `/speckit-specify`
  with at most three clarification questions.
- **SC-004**: A review finds no technology in any agent description, and a check that shows the
  goal is reached in 100 % of the skill descriptions.
- **SC-005**: For the first aspect, the descriptions cover the skills and agents that bring a
  GitHub project to its measured baseline (Scorecard, Best Practices badge, Plumber, SLSA
  levels) and name those scores as the checks.
- **SC-006**: After a refresh, a maintainer names the affected artifacts from the difference in
  under 10 minutes.

## Assumptions

- The maintainer confirms the scope, accepts the summary and decides the artifacts. The skill
  does not run `/speckit-specify` itself.
- The research uses the web search and fetch tools of the agent that runs the skill; blocked
  sites are recorded as not reached.
- Programs of the skill, if any, follow `AGENTS.md`: Python 3.9 standard library, offline
  tolerant, deterministic, tested without the network.
