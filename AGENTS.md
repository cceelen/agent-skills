# AGENTS.md

These rules apply to each agent and each person who changes this repository.

## Purpose

This repository is a collection of agent skills in the open `SKILL.md` format. Users install
the folders in `skills/` without a build step. Thus each skill folder must be complete.

## Structure

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

## Rules for the programs

- Use Python 3.9 or later, and only the standard library.
- The tools for development (`pytest`, `ruff`, `pre-commit`) need Python 3.10 or later. The CI
  runs the tests of the programs on Python 3.9 also.
- A program must not stop when the network is not available. It must record the error and
  continue.
- The same input must give the same output. Sort the output. Do not write the current time into
  a result that a test compares.

## Rules for the tests

- The tests must not use the network. Put the input data in `tests/<name>/fixture/`.
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

## Procedure to add a skill

1. Make the folder `skills/<name>/` with a `SKILL.md`.
2. Put the programs in `skills/<name>/scripts/`.
3. Write `docs/<name>.md`.
4. Add tests in `tests/<name>/`.
5. Add one row to the table of skills in `README.md`.
6. Increase the `version` in `pyproject.toml` and in the plugin manifest. The two versions
   must be the same.

## Releases

Use a version number of the form `major.minor.patch`. Increase the major number when a change
makes earlier reports not comparable.

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
- A ruleset for tags `v*`: only the owner can make or delete a tag.
- Actions: the default permission of the workflow token is "read".
