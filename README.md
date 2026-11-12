# Agent skills

[![test](https://github.com/cceelen/agent-skills/actions/workflows/test.yml/badge.svg)](https://github.com/cceelen/agent-skills/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/cceelen/agent-skills/graph/badge.svg)](https://codecov.io/gh/cceelen/agent-skills)

This repository contains agent skills in the open `SKILL.md` format. Each skill is one folder
in `skills/`. You can use the skills with Claude, with OpenAI Codex, and with other agents
that read `SKILL.md` files.

| Skill | Function | Documentation |
|---|---|---|
| `library-vetting` | Supply chain risk analysis of software projects and libraries. | [docs/library-vetting.md](docs/library-vetting.md) |

More skills will follow.

## Requirements

- `python3`, version 3.9 or later. The scripts use only the standard library.
- `git`.

## Installation

### Claude Code

Install the repository as a plugin, or copy the skills.

- To copy all skills for one user, do these steps:
  1. `git clone https://github.com/cceelen/agent-skills`
  2. `cd agent-skills`
  3. `./install.sh`
- To copy the skills into one project, use this command:
  `./install.sh --dir /path/to/project/.claude/skills`
- To install only one skill, add its name: `./install.sh --dir PATH library-vetting`

### Claude apps

1. Make a ZIP file of one skill folder, for example `skills/library-vetting`.
2. Open the settings of the Claude app.
3. Upload the ZIP file as a skill.

### OpenAI Codex

Codex reads skills from `~/.agents/skills` for one user and from `.agents/skills` in a
repository.

- To copy all skills for one user, use this command: `./install.sh --agent codex`
- To copy the skills into one repository, use this command:
  `./install.sh --dir /path/to/repository/.agents/skills`

Start Codex again after the installation. To start a skill by name, type `$library-vetting`
and then your request.

### Other agents

1. Find the skills directory of your agent in its documentation.
2. Use the command `./install.sh --dir <skills directory>`.

If your agent cannot load skills, tell it to read `skills/<skill name>/SKILL.md` and to obey
it.

### The rules of the kit

An agent can use a value from its context that is not correct now. The kit gives the agent
five rules against this error. The rules are in `rules/evidence-before-action.md`.

- Each skill holds the rules. They apply when the agent uses the skill.
- The plugin puts the rules into the context at the start of a session and after a compaction.
- `./install.sh` adds the rules to the instruction file of the user: `~/.claude/CLAUDE.md` for
  Claude Code, `~/.codex/AGENTS.md` for Codex. The rules are between two marker lines.
- If you use `--dir`, the program changes no instruction file. To name one, add
  `--rules /path/to/project/AGENTS.md`.
- To see the change first, use the command `python3 rules/apply.py FILE`.
- To prevent the change, add `--no-rules`.
- To remove the rules, use the command `python3 rules/apply.py --remove FILE`.

## Use

Tell the agent what you want in your own words. Each page in `docs/` gives examples.

## Repository structure

| Path | Contents |
|---|---|
| `skills/<name>/SKILL.md` | The instructions for the agent. |
| `skills/<name>/scripts/` | The programs that the skill uses. |
| `skills/<name>/prompts/` | The tasks that the skill gives to its agents. |
| `skills/<name>/agent-templates/` | The templates for the agent files. |
| `docs/<name>.md` | The documentation for the user. |
| `tests/<name>/` | The tests for the skill. The tests do not use the network. |
| `rules/` | The rules that the kit gives to the agent, and the program that installs them. |
| `hooks/` | The hook of the plugin that puts the rules into a session. |
| `AGENTS.md` | The rules for agents and persons who change this repository. |

There is no build step. The files in `skills/` are the source and the product.

## Tests

1. Install [uv](https://docs.astral.sh/uv/).
2. Use the command `uv run pytest`.
3. Use the command `uv run ruff check`.
4. To run all checks before each commit, use the command `uv run pre-commit install` one time.

## How to verify a release

Each release has an archive of this repository and a build provenance attestation. GitHub signs
the attestation. To verify an archive, use the GitHub CLI:

```bash
gh attestation verify agent-skills-v1.0.3.tar.gz --repo cceelen/agent-skills
```

The command shows the workflow and the commit that made the archive. If the command fails, do
not use the archive.

## Contributions and contact

Use the GitHub issues of this repository for each contribution and each question.

- To report a defect or to propose a change, open an issue.
- To report a vulnerability, obey [SECURITY.md](SECURITY.md). Do not open a public issue.
- Before you write a change, read [CONTRIBUTING.md](CONTRIBUTING.md) and `AGENTS.md`.
- The changes of each version are in [CHANGELOG.md](CHANGELOG.md).

## License

MIT. Refer to [LICENSE](LICENSE).

## Skill: Library Vetting

If the source code of a project is available to the agent, the skill makes a risk analysis for
the use of that project in your software supply chain. The analysis shows how the project is
maintained, how it is built and tested, and how it handles security problems. It also gives an
estimate of the SLSA level for the Build track, the Source track and the Dependency track. The
estimate comes from public evidence. It is not a certification.

This skill aggregates data and gives you recommendations. The decisions are your responsibility.
