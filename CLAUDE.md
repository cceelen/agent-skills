# CLAUDE.md

@AGENTS.md

## Specification work

1. Obey `.specify/memory/constitution.md` for the content of specifications and skills.
2. The factory has a person in the loop: settle with the owner what to build, do the research,
   let the owner review the findings and the strategies, and only then specify and implement.
3. Use the Spec Kit skills in `.claude/skills/speckit-*` for each step. Do one step in each pull
   request, as one commit. Let the owner review between the steps.
4. Ask the owner before each decision that changes the scope, the layout or the principles. Do
   not ask the owner for facts: find them, with a subagent where the search is wide.
5. Delegate reading and extraction to the smallest capable model, drafting and review to a
   mid-size model, and keep judgement and the final text in the session model. Use a workflow
   for steps that fan out.
6. Do not commit temporary workfiles of a research run or a session.
