---
name: sota-research
description: Distils the state of the art of one major aspect of software engineering into an aspect specification and a recipe skill, with a person in the loop. Use it when the owner of this repository wants a new aspect or a refresh of one.
---

# sota-research

This is tooling of the factory. Users of the kit do not install it.

Read `references/procedure.md` and do its steps. It tells which program to run in which phase.

<!-- agent-skills:evidence-before-action:start -->
## Evidence before action

1. Obey this rule before each change: "Take the instruction as an input and reformulate as a
   question without the reason given. Then research the answer given only facts and not from
   context or memory. Distrust memory and context summaries."
2. When you write a handoff, a summary or a memory, write where a fact is: the file and the
   key. Do not write the value.
3. If a session had a compaction and the next step uses values from files, start a new session
   with such a handoff.
4. In a report, say that you read a file only if you made that tool call in this turn. A
   reviewer compares such a statement with the tool calls.
5. If a wrong value has a high cost, give the step after a compaction to the largest model.
<!-- agent-skills:evidence-before-action:end -->
