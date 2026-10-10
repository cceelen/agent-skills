# CLAUDE.md

@AGENTS.md

## Specification work

1. Obey `.specify/memory/constitution.md` for the content of specifications and skills.
2. The factory has a person in the loop: settle with the owner what to build, do the research,
   let the owner review the findings and the strategies, and only then specify and implement.
3. Use the Spec Kit skills in `.claude/skills/speckit-*` for each step. Do one step in each pull
   request, as one commit. Let the owner review between the steps. A step goes into the branch
   of its specification, not into `main`: see "Branches" in `AGENTS.md`.
4. Ask the owner before each decision that changes the scope, the layout or the principles. Do
   not ask the owner for facts: find them, with a subagent where the search is wide.
5. Delegate reading and extraction to the smallest capable model, drafting and review to a
   mid-size model, and keep judgement and the final text in the session model. Use a workflow
   for steps that fan out.
6. Do not commit temporary workfiles of a research run or a session.
7. Start each Spec Kit step and each phase of the research in a new session. Give the session
   the paths of its input files. Do not give it a summary of their content.
8. If a session had a compaction, read each input file of the step again before you write.
9. In the task for a subagent, name the files and the keys. Do not write a value that the
   subagent can read.
10. Before the owner reviews a step, compare each "read" or "verified" in your report with the
    tool calls of the session. Remove each statement that has no tool call.
11. When you add a rule for agents to a skill, a prompt or this repository, write only the
    rule into the file. State its measured effect in the pull request: the number of runs and
    the result. If there is no test, write "not tested".

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
