# AGENTS.md

These rules apply to each agent and each person who changes this repository.

## Purpose

This repository is a construction kit for software engineering with AI agents. For each major
aspect it holds a recipe, a strategy and a generic checklist, and the skills that carry one
product each. All of them are agent skills in the open `SKILL.md` format. Users install the
folders in `skills/` without a build step. Thus each skill folder must be complete.

## Structure

| Folder | Contents |
|---|---|
| `specs/<number>-<name>/` | One specification. An aspect specification is the source of a recipe; a product specification builds implementation skills and helper software. This folder is only on the branch of its specification, not on `main`. |
| `factory/<name>/` | The tooling of the factory, in the layout of a skill. Users do not install it. |
| `skills/<name>/` | One skill. A recipe skill is rendered from its aspect specification. An implementation skill carries one product. |
| `rules/` | The rules that the kit gives to the agent of a user, and the program that puts them into an instruction file. |
| `hooks/` | The hooks of the plugin. A hook puts the rules into the context of a session. |
| `.specify/` | Spec Kit. The template for an aspect specification is in `.specify/templates/overrides/`. Do not edit the other templates there: an upgrade of Spec Kit replaces them. |

To distil an aspect, read `factory/sota-research/SKILL.md` and do its steps.

Each skill has its documentation in `docs/<name>.md`. Its tests are examples in its programs, or
files in `tests/<name>/`. The agent
files that wrap a recipe skill for one agent product are templates inside the skill. Do not
edit a rendered recipe skill by hand: change its specification and render it again. The layout
of a skill is:

- `skills/<name>/SKILL.md`: the instructions for the agent that uses the skill.
- `skills/<name>/scripts/`: the programs of the skill.
- `skills/<name>/prompts/`: the tasks that the skill gives to its agents. The skill tells an
  agent to read one of these files. Do not copy a prompt into `SKILL.md`.
- `skills/<name>/agent-templates/`: the templates for agent files. A setup program fills in the
  model and the tool names for the local agent product.
- `docs/<name>.md`: the documentation for the user.
- `tests/<name>/`: the tests of the skill.
- `.claude-plugin/plugin.json`: the plugin manifest.
- `.github/workflows/test.yml`: the tests and the checks for each push and each pull request.
- `.github/workflows/release.yml`: the release with build provenance, for each version tag.
- `CHANGELOG.md`: the changes of each version, for the user.

## Commands

- Run the tests: `uv run pytest`
- Examine the code: `uv run ruff check`

Run the two commands before each commit. The two commands must pass.

- Run all checks: `uv run pre-commit run --all-files`
- Run the checks automatically before each commit: `uv run pre-commit install` (one time)

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

## Rules for a skill

- The folder name and the `name` in the front matter must be the same. Use lowercase letters,
  digits and hyphens.
- The `description` must tell the agent what the skill does and when to use it.
- Refer to the scripts with a path relative to `SKILL.md`, for example `scripts/score.py`.
- Do not name a tool of one agent only. Write "your subagent tool" and "your web fetch tool".
  If an example helps, give it in parentheses.
- Do not write a model name in `SKILL.md`, in a prompt or in a template. Put model names only in
  the table of `scripts/models.py`.
- Do not put secrets, personal data or absolute paths in a skill.
- Each `SKILL.md` holds the rules of `rules/evidence-before-action.md` between their two marker
  lines. To get the text, use the command `python3 rules/apply.py --print`.
- A skill holds instructions, knowledge and references (URLs with dates). Do not store the
  material that was read while writing it. A specification keeps only a short evidence record:
  a summary of what each source contributes.
- An implementation skill points at the maintained templates and tools of its product and uses
  their latest pinned version. Do not copy them into the skill.

## Rules for the programs

- Write helper software in Python. Do not write it in a shell language. Prefer a declarative
  tool where one exists.
- For a skill that users install, use Python 3.9 or later, and only the standard library.
- For the tooling in `factory/`, use the latest stable Python and only the standard library.
  Declare the version in the script header of each program. Run a program with `uv run`, and
  a tool with `uvx` or `uv run`.
- The tools for development (`pytest`, `ruff`, `pre-commit`) need Python 3.10 or later. The CI
  runs the tests of the programs on Python 3.9 also.
- A program must not stop when the network is not available. It must record the error and
  continue.
- The same input must give the same output. Sort the output. Do not write the current time into
  a result that a test compares.

## Rules for the tests

- Write the tests of a new program as examples (doctests) in the program itself. Do not add a
  test file when an example can do the work. Thus a user installs a program that validates
  itself, without test files.
- A program with examples runs them with the option `--selftest`. Keep the sample data that the
  examples use in a Python file beside the program, not in a fixture folder.
- `tests/test_repo.py` runs each program of `factory/` with `--selftest` under coverage. The
  coverage must be at or above the minimum in `pyproject.toml`. Ruff examines each new file.
- The tests must not use the network. For a skill that has test files, put the input data in
  `tests/<name>/fixture/`.
- If you change the scoring of `library-vetting`, update the expected values in the test and
  increase the rubric version in `score.py`.
- Do not change the identifier of a criterion in `rubric.txt`. Earlier reports refer to it.

## Rules for the documentation

Write the files for the user in ASD-STE100 Simplified Technical English. These files are
`README.md`, the files in `docs/`, and the text that a skill writes for the user.

- Use one word for one meaning.
- Use the active voice and simple verb tenses.
- Write instructions as commands. Give one instruction in each sentence.
- Use a maximum of 20 words in an instruction and 25 words in other sentences.
- Put the condition before the instruction.

## Rules for commit messages

- Use the Conventional Commits format: `type(scope): subject`. The scope is optional.
- Write the subject in ASD-STE100 Simplified Technical English.
- Give the purpose of the change. Do not tell the sequence of the work.
- Do not list files or single changes.
- Do not add a link to an agent session.
- Do not add a footer line, for example `Co-Authored-By`, unless the owner tells you to add it.

## Procedure to add a skill

1. Make the folder `skills/<name>/` with a `SKILL.md`. Put the rules of the kit into it: see
   "Rules for a skill".
2. Put the programs in `skills/<name>/scripts/`.
3. Write `docs/<name>.md`.
4. Add tests in `tests/<name>/`.
5. Add one row to the table of skills in `README.md`.
6. Increase the `version` in `pyproject.toml` and in the plugin manifest. The two versions
   must be the same.

## Releases

Use a version number of the form `major.minor.patch`. Increase the major number when a change
makes earlier reports not comparable.

This repository uses trunk-based development. There is no release branch. A release is a tag
on `main`.

## Branches

- `main` holds the machinery and the delivered skills only: `factory/`, `.specify/`, `skills/`,
  their documentation, their tests and the files of the repository.
- Each specification has one branch with the name of its folder, for example
  `001-sota-research`. The branch holds `specs/<number>-<name>/` with its evidence and its
  research records. It stays for the life of the specification. Do not merge it into `main`.
- One Spec Kit step is one short-lived branch and one pull request into the branch of its
  specification.
- A delivery is a short-lived branch from `main` and a pull request into `main`. It carries
  only machinery or delivered skills. A rendered recipe skill records the branch and the
  commit of the specification that it was rendered from.
- Merge `main` into the branch of a specification to get new machinery.
- To number a new specification, use the highest number of the specification branches plus
  one. The folder `specs/` on `main` is empty.

Procedure for a release:

1. Increase the `version` in `pyproject.toml` and in the plugin manifest. Run `uv lock`.
2. If the scoring changed, increase the rubric version in `score.py`.
3. Add a section for the version to `CHANGELOG.md`.
4. Make sure that the tests and the checks pass on the branch `main`.
5. Make a tag `v<version>` on that commit and push the tag.
6. The workflow `release.yml` makes the archive, the attestation and the GitHub release. Do not
   make a release by hand.

In a workflow, pin each action of a different project with the full commit digest. Write the
version in a comment after the digest.

## Settings of the repository on GitHub

The owner sets these one time. The files in the repository cannot set them.

- Private vulnerability reporting: on. `SECURITY.md` tells a reporter to use it.
- Dependabot alerts and Dependabot security updates: on.
- A ruleset for the branch `main`: a pull request is necessary, the checks `test` and `lint`
  must pass, and a force push is not permitted.
- A ruleset for tags `v*`: only the owner can make a tag, and a tag cannot be changed or deleted.
- Release immutability: on. The files and the tag of a published release cannot be changed.
  Thus a release with a defect gets a new version, not a correction.
- Actions: the default permission of the workflow token is "read".
