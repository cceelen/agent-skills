# Changelog

This file shows the changes of each version. A change of the major number means that earlier
reports are not comparable with new reports.

## Next version

- The kit gives the agent five rules for evidence before action. The rules are in each skill.
  The plugin puts them into each session. `install.sh` adds them to the instruction file of the
  user. The section "The rules of the kit" in `README.md` tells you how to prevent this.
- The repository gets the tooling of the factory in `factory/sota-research/`. It distils the
  state of the art of one aspect of software engineering into a recipe skill. Users of the
  kit do not install it.
- The tooling uses the latest stable Python and runs with `uv`.
- The tooling converts a web page into a converted file with `web.py`. The readers get the text
  of a web source through the index, as for a PDF source.
- The tooling can try a recipe on a project before the owner accepts it. A reviewer examines
  the plan from eight viewpoints, and the check reports the findings that are open. One
  viewpoint is the integrity of each asset, from the source to the system of the user.
- The cost of a checklist item is the number of elements that a project changes to adopt the
  item and to keep it. It is not an estimate of time.
- The answer "Probability" of a checklist item says how strongly regulations and standards ask
  for the item. The requirement rows of the item give the answer. The rubric for items has the
  version 4.
- A source can have the class `regulation` or `governance`. The checklist of a recipe names
  the regulation and the governance that ask for each item. The recipe asks you which of them
  bind your project.
- The research searches also for the regulation, the governance and the public recommendations
  of an aspect.
- The check names each item whose harm has no source. The rendered checklist marks a level
  that rests on no source.
- An aspect specification names the measured targets of its aspect. The check fails for an
  empty field `Targets`.
- The tooling asks the owner for the intent before the research, and compares it with the
  sources. The check fails for an aspect specification without the field `Intent of the owner`.
- The research finds the stakeholders of an aspect. Each view names its stakeholders. The check
  fails for an aspect specification without the field `Stakeholders`.
- The check gives the number of answers of risk and reward with a source and by judgement.
- The research records each requirement that a source states in the table `Requirements` of
  `vetting.md`. Each requirement goes to a checklist item, or leaves by one of three named
  exits. The check fails for an aspect specification without this table.
- Each source names the views that it was read for, in the cell `Views`. The check lists each
  view with fewer than two sources of its own field.
- Only the owner decides a boundary of an aspect. Each boundary has a state: `(proposed)`
  or `(decided by the owner on <date>)`. The check fails for a requirement that goes to a
  boundary that the owner did not decide. The table `Proposed boundaries` of `vetting.md`
  shows the requirements that each proposed boundary would take.
- The template of an aspect specification holds no example of a real concern.
- `export.py` writes a neutral kit for a trial of the tooling.
- `seed.py` retrieves the seed documents and standards of the factory into a work folder. The
  manifest `references/seeds.md` names them. It replaces `references/bodies-of-knowledge.md`.
- `init.py` sets up a neutral environment of the factory again: the kit, a git repository and
  the seeds.
- `render.py` renders nothing when a rendered file refers to the factory, to this repository or
  to an absolute path. A created skill works alone.
- The names of the viewpoints of the review are in `references/viewpoints.txt`. A neutral kit
  does not hold this file. There, the check does not examine the viewpoint of a finding.
- `index.py` makes an index of the converted documents of a work folder. It finds pages by
  words, by synonyms and by references. It gives the page ranges for the readers. It prints
  pointers only, not the text of a document.
- `seed.py get` and `init.py` build this index at their end. The file `references/synonyms.txt`
  holds the synonyms of the factory.
- The research reads each converted source in the page ranges of the index. One reader gets one
  range. `index.py given` records each range, and `index.py unread` gives the pages that no
  reader got.
- `index.py unread --write` writes the table `Reading` into `vetting.md`. The check fails for
  a source that says `full` and has pages that no reader got. It lists each such source.
- The research finds the pages of a concern with `index.py search`, and the references of a
  view with `index.py refs` and `index.py cited`.
- `index.py build` reads the file `synonyms.txt` of the work folder, if the file is there.
- `check.py --index` compares the register of the requirements with the requirement lines
  that the readers reported. A requirement that was lost, added or changed fails.
- `index.py take` records the lines `REQ` and `USE` of the report of a reader. `index.py lines`
  gives the recorded lines as tables. The research writes the table `Requirements` from them.
- An aspect specification can have a charter of the owner in `charter.md`: the target, the
  principles with their priority, and the constraints. The agent drafts it in phase 1 from what you say in the
  session, and you confirm or correct it before the research. The agent reads it before the triage,
  and you get it first in the review.

## 1.0.3

The skill did not change.

- A published release cannot be changed. The files and the tag of the release are permanent.
- The tags `v1.0.1` and `v1.0.2` have no release. Do not use them.

## 1.0.0

The first public version. It contains one skill, `library-vetting`, with the rubric
`library-vetting v1`.

- The skill examines an open source library in 15 dimensions and gives a tier.
- `collect.py` collects the facts: the registry record, the history, the files, the CI
  configuration, the advisories, the OpenSSF Scorecard and the base stack.
- `score.py` calculates the scores, the tier and the SLSA levels for the Build track, the
  Source track and the Dependency track.
- `models.py` saves the model for each role of the skill.
- The skill can use the programs pipeline-check and Plumber if they are installed.
