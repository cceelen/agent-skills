---
name: experiment-rigor
description: Makes a trial of an agent, a skill, a prompt or an instruction a registered experiment, with a prediction before the run, a clean environment, a blind judge and a verdict from registered limits. Use it before each run of an agent, a skill, a prompt or an instruction whose result is reported or used for a decision.
---

# experiment-rigor

This is tooling of the factory. Users of the kit do not install it.

Do these steps in this order. The program is `scripts/experiment.py`. Run it with `uv run`.

1. Write the question of the owner as a quote, with its date. Do not change the words.
2. Make a new folder for the experiment. Copy `references/registration-template.md` into it as
   `registration.md`. Fill in each field. Write each prompt file as the subject gets it.
3. Build each input folder from an empty folder. Put in only the files that the subject needs.
   Do not copy this repository.
4. Run `uv run scripts/experiment.py check <folder>`. Correct each line `FAIL`. Read the list
   "Loaded instructions".
5. Show the registration to the owner. Change it only before the seal.
6. Commit the folder. Then run `uv run scripts/experiment.py seal <folder> --today <date>`.
7. Run `uv run scripts/experiment.py run <folder> --work <work folder>`. Use a work folder
   outside each git repository. If the command says that runs remain, run it again.
   Do not look at a result before all runs are done. Do not add a run. Do not leave out a run.
8. Run `uv run scripts/experiment.py blind <folder> --work <work folder>`. If the command wrote
   packets, start a judge that did not see the registration (for example with your subagent
   tool). Tell the judge to read `prompts/judge.md`. Give it only the path of the folder
   `packets`. Copy the file `judgements.md` that the judge wrote into the folder of the
   experiment. Do not change it.
9. Run `uv run scripts/experiment.py score <folder>`.
10. Report the counts, the intervals and the verdict as `result.md` gives them. Mark each
    explanation as a guess.

Obey these rules in each step:

- Start a session of the subject only with the command `run`.
- Do not change a file of the folder after the seal. If a change is necessary, make a new
  folder with a new registration.
- Do not give the judge the registration, the key `blind-key.json` or the name of an arm.
- If the command `run` marks a run as not valid, do not correct the row. Run the command again.
- Do not report a verdict that `result.md` does not give.

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
