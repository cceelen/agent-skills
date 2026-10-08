# Constitution of the agent-skills repository

This repository holds skills and agents that bring software projects to the current state of
the art (SOTA) of engineering practice. Spec Kit builds them from specifications. The first
skill, `sota-research`, researches the SOTA of one aspect for one context and writes the
description from which Spec Kit creates or improves a skill or an agent.

The repository rules in `AGENTS.md` stay in force. This constitution gives the principles for
the content of specifications, skills and agents. Where the two differ, `AGENTS.md` decides for
the layout and the tooling of the repository.

## Principles

### I. Evidence

A statement about the state of the art names its source, with the date or version of the
source. A statement that was not verified is marked as not verified. The project does not
invent standards; it records the existing ones and names a gap where none exists.

### II. Best practices are generic, implementation strategies are contextual

A best practice is short, generic, and valid across many or all contexts. An implementation
strategy is the tactic that applies a best practice to one specific context: the use case, the
industry and its regulation, the users, the data, the delivery mechanism, the forge and the
stack. The knowledge keeps the two apart. A best practice that is essential in one context can
be useless in another; the implementation strategy says where it applies, and the knowledge
says so instead of giving one answer for all.

### III. Wrap, do not rebuild

A skill uses an existing tool, platform control or template when one covers the need. Own code
fills a named gap. Platform-native controls come before third-party tools. Code or content
under a license that conflicts with the project license is not copied. Calling a tool or a
service is allowed only when its license or subscription allows that use.

### IV. Roles are neutral, tools are specific

An agent covers one discipline, finds out the context of the case in front of it, plans the work
against the SOTA for that context, delegates to skills and verifies the result. It names no
technology. A skill does one task on named technologies and carries the best practices of that
stack. Support for a new technology is a new skill, never a change to an agent.

### V. Plan, then apply

A change to a project or to forge settings is shown as a plan, a diff or a pull request before
it is applied. Skills hold no standing credentials. Steps that only a person can do are listed
for that person.

### VI. Validation belongs to the artifact

Each skill and each agent names the deterministic check that shows its goal is reached and what
remains: an existing checker, a score, a badge, a provenance level or a program. The check is
cheap and runs without a model, so that a process gets fast feedback. The research skill
specifies this check in the description of each skill or agent it proposes.

## What an artifact keeps

A skill or an agent holds explicit instructions, summaries and the references it rests on. It
does not hold the material that was read while writing it. Each reference is a URL with its
date, kept next to the artifact that uses it. A SOTA summary records its research date and
shows at a refresh what changed.

## Governance

This constitution has priority over other practices of the project. An amendment is a pull
request that changes this file and states the reason. The version follows semantic versioning:
MAJOR for a removed or redefined principle, MINOR for a new principle, PATCH for a
clarification.

**Version**: 2.0.1 | **Ratified**: 2026-10-08 | **Last Amended**: 2026-10-08
