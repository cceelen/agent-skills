# CLAUDE.md

@AGENTS.md

## Specification work

1. Obey `.specify/memory/constitution.md` for the content of specifications, skills and agents.
2. Use the Spec Kit skills in `.claude/skills/speckit-*` for each step. Do one step in each pull
   request. Let the owner review between the steps.
3. Ask the owner before each decision that changes the scope, the layout or the principles.
4. Delegate reading and extraction to the smallest capable model, drafting and review to a
   mid-size model, and keep judgement and the final text in the session model. Use a workflow
   for steps that fan out.
5. Do not commit temporary workfiles of a research run or a session. Commit specifications,
   skills, agents, their documentation and their tests.
