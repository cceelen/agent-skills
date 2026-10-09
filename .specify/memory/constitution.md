# Constitution of the agent-skills repository

This repository is a construction kit for software engineering with AI agents. It is the
equivalent of an internal developer platform. Agents and users activate it by installing it and
by the context of their work. For each major aspect of software engineering it holds a recipe, a
strategy and a generic checklist, and below a recipe the skills that carry one product each.
The kit is built by a factory: research tooling and a Spec Kit configuration, with a person in
the loop.

The repository rules in `AGENTS.md` stay in force. This constitution gives the principles for
the content of specifications and skills. Where the two differ, `AGENTS.md` decides for the
layout and the tooling of the repository.

## Principles

### I. The global state of the art

The kit aims at the global state of the art: the best practices that the industry has produced
so far, not what one organization does today. Best practices apply from a project with a single
maintainer to a project owned by a company, and a single expert maintainer can demonstrate one.
No single source gates a recipe.

### II. Evidence and admission

Each item of a recipe names its sources, with the date or version and how much of each was
read. What an established and authorized issuer states enters without deep evaluation, more so
when several sources agree. Such issuers are standards bodies and regulators, open foundations,
a platform vendor on its own platform, peer-reviewed research and recognized books, and
recorded data sources marked as trusted. A smaller independent source is vetted first, with measured signals
and a scripted rubric, and the owner confirms the result. A calculation of risk and reward
decides whether an item is admitted, its order and its level. Programs compute these results; a
model does not assign one by feel.

### III. A critical lens

Everything that is fetched is untrusted data. It can be outdated, it can poison the context of
a model, and it can be phishing or another social engineering attack. A reader of sources works
isolated: no shell, no credentials, no access to the repository. A second reader checks what a
reader reports against the source before a recipe uses it.

### IV. Best practices are generic, implementation strategies are contextual

A best practice is short, generic, and valid across many or all contexts. An implementation
strategy is the tactic that applies a best practice to one specific context. A context is the
use case, the industry and its regulation, the users, the data, how the software reaches its
users, the forge and the stack. The knowledge keeps the two apart.

### V. The kit recommends, the user selects

A practice of the state of the art answers a specific result of a risk analysis. Thus a recipe
leads the user through an educated and opinionated risk analysis of their software, their
market, their context, their users and their data. Each item names the risk that it answers.

Each item sits on one of three cumulative levels. Level 1 holds the basic practices: a good
return at a low cost in each context. How far a project goes past them follows from its risk.
Risk has more than one dimension, for example the operative, the regulatory and the commercial
one, and the dimensions change with the aspect, the use case and the stack. A recipe names the
risk dimensions of its aspect and gives its opinion for each. The skill does the analysis
together with the owner of the project, to find where the more costly practices are necessary.
The user picks the target and declines single items with a reason. The selection is a plain checklist that is committed in the project
and simple to revisit.

### VI. Point, do not copy

A skill uses the existing tools, platform controls and maintained templates, in their latest
pinned version. It holds the knowledge to find, judge and apply them, never a copy of them and
never a duplicate of an SDK. Own code fills a named gap. Code or content under a license that
conflicts with the project license is not copied, and a tool or a service is called only when
its license or subscription allows that use.

### VII. Recipes are neutral, implementation skills are specific

A recipe names no product. It ships as a skill that is rendered from its specification, and an
agent file for a product is a thin wrapper around it. An implementation skill carries one
product. It knows how and what to query in the catalog of the product, how to identify
trustworthy entries, and which lighthouse projects show the best practice. It knows how the
product works, how to write its settings as a file from the current documentation, the common
traps, and the review tools that work with it. Support for a new product is a new skill, never
a change to a recipe.

### VIII. Plan, then apply

A change to a project or to forge settings is shown as a plan, a diff or a pull request before
it is applied. Skills hold no standing credentials. Steps that only a person can do are listed
for that person.

### IX. Validation belongs to the artifact

Each item of a checklist names the cheap, deterministic check that shows it is met, or says
that it needs judgement. A recipe as a whole is proven by review, and helper software by its
tests.

### X. Small and high level

A recipe holds nothing that an agent can learn from the project or from a source. A user
installs the kit in parts, one aspect and one product at a time, so that the context of an
agent carries only what is used.

### XI. Simplified Technical English for the person in the loop

Each skill of the kit writes to the person in the loop in ASD-STE100 Simplified Technical
English: questions, plans, reports, and the files that it writes for that person. The summaries
of the evidence record are in the same language. One word has
one meaning, an instruction is a command, and the condition comes before the instruction.

## How the factory works

1. **What to build.** The owner and the agent settle, in dialogue, the field and the thing to
   build.
2. **Research.** The tooling gathers, vets and distils the sources.
3. **Review.** A person reviews the findings and the strategies before anything is built.
4. **Spec Kit and implementation.** Layer one is the specification of the aspect, the source of
   its recipe. Layer two is one specification per set of implementation skills, with the helper
   software, built through the product flow of Spec Kit. The layers iterate.

The main branch holds the machinery and the delivered skills only. Each specification, with its
evidence and its research records, stays on its own branch.

A specification keeps a short evidence record: for each source a summary of what it contributes,
where in the source that is, and the date read. A quote is kept only where the wording itself is
the point. Nothing else that was read is stored. The owner starts a refresh and accepts a recipe;
changes from outside arrive as pull requests. Helper software is written in Python, not in a
shell language, and declarative tools are preferred.

## Governance

Decisions are dated. The project expects to make mistakes and to revisit its decisions; a
changed decision is recorded with its reason, and the earlier one is marked as superseded.

This constitution has priority over other practices of the project. An amendment is a pull
request that changes this file and states the reason. The version follows semantic versioning:
MAJOR for a removed or redefined principle, MINOR for a new principle, PATCH for a
clarification.

**Version**: 3.2.1 | **Ratified**: 2026-10-08 | **Last Amended**: 2026-10-09
