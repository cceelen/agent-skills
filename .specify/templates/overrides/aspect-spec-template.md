# Aspect specification: [MAJOR ASPECT]

**Branch**: `[###-name]` | **Research date**: [DATE] | **Supersedes**: [the research date of the earlier revision, or none]

Layer one of the factory: the exploration of one major aspect of software engineering. This
specification is the source of the recipe for the aspect, a strategy and a generic checklist
that hold the global state of the art (SOTA): the best practices that the industry has produced
so far. A helper renders the recipe skill from it. The implementation skills for single products
are layer two: each set gets its own specification through the Spec Kit product flow. Keep this
file high level. It holds nothing that an agent can learn from the project or from a source.

## 1. Aspect

- **Aspect**: [one major aspect, in one line]
- **Field and disciplines**: [the field it belongs to; the disciplines it covers or cuts across]
- **Contexts**: [the values of each dimension that change the strategy: use case; how the
  software reaches its users; exposure (who depends on the project); team; industry and
  regulation; data; forge; stack]
- **Boundaries**: [what neighbouring aspects own, one line each]
- **Agreed with the owner on**: [DATE; what to build and for whom]

## 2. Sources

No single source gates the recipe: the recipe is the fixed side, and each source supports the
items that cite it. **Class** decides the route of admission. The fast lane: `standard`
(standards bodies and regulators), `foundation` (open foundations), `vendor` (a platform vendor
on its own platform), `research` (peer-reviewed research and recognized books), `trusted-data`
(a recorded data source marked as trusted). Every other source is `independent` and passes the
source vetting first. **Read**: full, part or no. A paid source is cited from its official
preview and marked part.

| Id | Source | Issuer | Version or date | Class | License | Read | URL |
|---|---|---|---|---|---|---|---|
| S-01 | | | | | | | |

## 3. Strategy

High level, for the agent that runs the work. One page.

### 3.1 Goals

[What "done well" means for this aspect, in three to six lines.]

### 3.2 Order of the work

1. [step: what, and why at this point]

### 3.3 Decisions that depend on context

| Decision | Depends on | Options | Sources |
|---|---|---|---|

### 3.4 Where the sources disagree

| Question | Positions | How this recipe handles it | Sources |
|---|---|---|---|

## 4. Checklist

Generic items, valid across contexts, from a single maintainer to a company. One short sentence
each. An item that holds only in some contexts belongs in 3.3; an item for one product belongs
in an implementation skill. There is no fixed number of items: distil until each item earns its
place.

- **Level**: 1, 2 or 3, cumulative. The risk and reward calculation places the item: the best
  return at the lowest cost is level 1. The exposure of a project decides which level the
  project aims for; section 3.3 says how.
- **Admitted by**: `authority` (a fast-lane source states it; name how many agree), `practice`
  (vetted independent sources demonstrate it) or `own rule` (a rule of this kit, with its
  principle).
- **Check**: the cheap, deterministic check that shows the item is met, or `judgement`.
- **Source**: the unit of a source by its identifier where it has one. No text of a source is
  copied here; the evidence record says what the source contributes.

| Id | Item | Why | Level | Admitted by | Check | Source |
|---|---|---|---|---|---|---|
| C-01 | | | | | | [S-01 PW.4.1] |

**Selection.** The kit recommends; the user decides. For a project, the user picks a target
level and declines single items with a reason. The selection is a Markdown checklist that is
committed in the project, and the recipe skill shows and changes it on request. A declined item
keeps its reason, and a refresh shows the declined items whose source changed. The distance of
a project is the list of adopted items whose check fails.

## 5. Skill set to define

What the recipe skill and its agent wrapper do, and which implementation skills layer two must
work out.

### Recipe skill and agent: [name]

- **Goal**: [the state it brings a case to]
- **Reads first**: [the contexts of section 1 it finds out; the selection of the project]
- **Applies**: [the strategy of section 3; the checklist items it judges]
- **Delegates**: [capabilities, each provided by an implementation skill]
- **Stops when**: [goal reached; blocked; a decision of section 3.3 needs a person]

### Implementation skills (layer two)

One line per product or tool that needs a skill. A skill holds knowledge and pointers, never a
copy of what the product's own catalog maintains: how and what to query in the catalog; how to
identify trustworthy entries; lighthouse projects, chosen by measurable criteria and dated; how the product works and how to get the work
done; settings as a file from the current documentation; common traps and points to review;
which review tools work with it and how to apply their corrections. A skill that cannot reach
its sources says what it could not verify.

| Product or tool | Capability | Checklist items it implements | Helper software it needs |
|---|---|---|---|

## 6. Watch list

| Signal | Where to read it | Cadence |
|---|---|---|

## 7. Decisions and changes

Dated. A reversed decision stays and is marked superseded. Name the models that made or
suggested a judgement, and the person who reviewed the findings and accepted the recipe.

| Date | Decision or change | Reason | Revisit when |
|---|---|---|---|

## 8. Glossary

Terms that mean different things in the sources. One preferred form per meaning.

| Term | Meaning here | Other meanings in the sources |
|---|---|---|

## Files beside this specification

- `evidence.md`: for each source a summary of what it contributes, where in the source that
  is, the rows of this specification that it supports, and the date read. The summary is in
  Simplified Technical English and in the words of this kit. A second reader compares each
  line with the source. A quote stays only where the wording itself is the point, for example
  a legal definition.
- `vetting.md`: for each independent source the measured signals, the result of the rubric and
  the owner's confirmation; for each item the answers of the risk and reward calculation.
