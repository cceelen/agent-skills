# Charter of the field software engineering (draft)

**State**: draft for the review of the owner. The owner did not accept it.

This charter is above the charter of each aspect. An aspect gets its lines unchanged and adds
its own. The lines apply in two places: to each recipe that the factory makes, and to the way
the factory itself works.

Words of the owner, 2026-10-11: "shift left, rapid iteration, rapid prototyping, early
evaluation and testing of assumptions are very normal and common practices in all SWE aspects.
so they should be ingrained into the factory"

## Principles

The order is a proposal of the agent. The owner gave no order.

| Priority | Id | Principle | For a recipe | For the work of the factory |
|---|---|---|---|---|
| 1 | F-1 | Test an assumption early. | A recipe asks a project to check an assumption before it builds on it. | Each iteration names its assumption and the cheapest test of it, before a full run. |
| 2 | F-2 | Evaluate early. | A recipe puts a check at the earliest step where it can find the defect. | A stage is tested alone with recorded input of an earlier trial, before a run of all stages. |
| 3 | F-3 | Shift left. | A concern is handled at the earliest step of the work. | A defect of a specification is found by the check, not by a trial; a defect of a trial is found by its registration, not by its result. |
| 4 | F-4 | Iterate fast. | A recipe prefers a small step with a result to a large step. | One change in each iteration; a short trial before a long one. |
| 5 | F-5 | Prototype fast. | A recipe lets a project start with a small, complete slice. | A recipe is rendered and tried as a plan early, also from an incomplete specification. |

## What follows for the factory, as the agent reads it

- **Stage trials.** The research has stages: reading, register, triage, rendering, plan. A change
  of one stage is tried first on the recorded output of the stage before it, from an earlier
  trial. This takes minutes and no reader agents. A full run follows only when the stage trial
  shows a difference.
- **An assumption for each iteration.** The row of an iteration in `iterations.md` names the
  assumption, the cheapest test, and its result, before the full trial.
- **An early plan.** The trial of a plan on a project does not wait for a complete
  specification.
- **A small run first.** A run with one view and a small set of sources comes before a run with
  all views.

## Questions for the owner

1. Is this a charter of the field, above each aspect, or a part of the constitution?
2. Is the order correct?
3. Which words must change?
