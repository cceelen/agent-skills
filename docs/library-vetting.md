# library-vetting

This skill examines an open source library. It tells you if you can adopt the library, or if
you can continue to use it. It works for each ecosystem that has a source repository. Examples
are C and C++, Rust, Go, Python, npm, JVM, .NET, Ruby and PHP.

## Result

The skill writes one report for each library. The report contains these items:

- A tier: ADOPT, ADOPT WITH GUARDRAILS, LIMIT, REPLACE, OWN IT or AVOID.
- A total score, and four scorecards that contain 15 dimensions.
- A SLSA level for each of three tracks: Build, Source and Dependency.
- A summary of the findings. Each finding points to the action that follows from it.
- The guardrails that apply to this library only.
- An exit plan or a migration plan.
- A list of alternative libraries that you can examine.
- A table of the evidence.

The skill also keeps a file with the answer to each criterion. The name of the file is
`evidence-ledger.md`.

## Examples

- "Vet https://github.com/madler/zlib for our C++ service."
- "Should we continue to use rapidjson? It reads our lock files."
- "Compare simdjson, yyjson and nlohmann/json. The input is not trusted."

You can give a registry package as `npm:express`, `pypi:requests` or `cargo:serde`.

## Procedure of the skill

1. **The skill asks you about the use.** The result depends on the use. The skill asks four
   questions before it collects data:
   - Is the library new for you, or do you use it now?
   - What data does the library receive?
   - How do you supply your product, and to which market?
   - What are your requirements?

   If you do not answer, the skill makes assumptions. Then the report shows that the tier is
   provisional.
2. **A program collects the facts.** `collect.py` makes one shallow clone of the repository. It
   reads the history, the files, the CI configuration and the registry data.
3. **A small model reads the evidence.** It answers each evidence criterion with `yes`, `no`,
   `unknown` or `na`. Each `yes` and each `no` must have evidence.
4. **The main model makes the decisions.** It answers approximately 20 criteria that need a
   decision. It also answers the disqualifiers.
5. **A program calculates the result.** `score.py` calculates the scores and the tier, and it
   writes the tables of the report. The same facts and answers always give the same result.
6. **The main model writes the text of the report.**

## Models and agents

The skill uses two roles:

| Role | Function | Model |
|---|---|---|
| Evidence | Reads the clone and the web pages. Answers the evidence criteria. | The smallest capable model. |
| Vetter | Makes the decisions and writes the report. | The model of the session. |

The names of the models are different in each agent product. Thus the skill does a setup one
time for each installation:

1. The program `models.py` finds the agent product and reads its local configuration.
2. The skill shows you a proposed model for each role.
3. You accept the proposal, or you give a different model name.
4. The skill saves the mapping. If the agent product supports agent files, the skill also writes
   two agents: `library-evidence-collector` and `library-vetter`.

| Agent product | Proposed model for evidence | Agent files |
|---|---|---|
| Claude Code | `haiku` | `.claude/agents/` or `~/.claude/agents/` |
| OpenAI Codex | The model of the session | None |
| Other | The model of the session | None |

The mapping is in `~/.config/library-vetting/models.json`. For one project, the mapping is in
`.claude/library-vetting/models.json`.

To do the setup manually, use these commands:

```bash
LV=skills/library-vetting/scripts
python3 $LV/models.py detect
python3 $LV/models.py apply --evidence haiku --vetter inherit
python3 $LV/models.py show
```

The value `inherit` means that the role uses the model of the session.

The program reads only local files and environment variables. It cannot know if your account
can use a model. If the agent product rejects a model, the skill uses the model of the session
and tells you.

## Rules that the skill obeys

- **Limited use of the web.** In quick mode, the skill makes a maximum of nine web requests for
  each library.
- **No recommendation without a report.** The skill recommends an alternative library only if
  that library has its own report.
- **A full examination for each library in a comparison.** The skill examines each library
  fully and independently. Then it writes the comparison from the completed results.
- **Simplified Technical English.** The skill writes the reports in ASD-STE100 Simplified
  Technical English.

## Tiers

| Tier | Meaning |
|---|---|
| ADOPT | Use the library. Usual care is sufficient. |
| ADOPT WITH GUARDRAILS | Use the library only with the conditions that the report gives. |
| LIMIT | Keep the current use. Do not add new use. |
| REPLACE | You use the library now, and a disqualifier applies. Plan the migration. |
| OWN IT | You use the library now, a disqualifier applies, and there is no alternative. You must do the maintenance. |
| AVOID | The library is new for you, and a disqualifier applies. Do not adopt it. |

## SLSA levels

SLSA is a specification for the security of the software supply chain. Refer to
[slsa.dev](https://slsa.dev/spec/). The report gives one level for each of these tracks:

| Track | Levels | Specification | Criteria |
|---|---|---|---|
| Build | L0 to L3 | SLSA v1.2 | `D12.scripted`, `D12.generated`, `D12.provenance`, `D12.isolated` |
| Source | L1 to L4 | SLSA v1.2 | `D12.source_attested`, `D12.protected`, `D12.two_party` |
| Dependency | L0 to L3 | SLSA draft | `D6.pinned`, `D6.sbom`, `D6.update_bot`, `D6.screened`, `D6.stack_current`, `D6.stack_clean`, `D12.ci_hardened`, `D13.toolchain`, `D13.hermetic` |

- A track has a level only if each criterion of that level has the answer `yes`.
- A level also needs each lower level.
- The answer `unknown` stops the level. The report shows the criterion that stops the next
  level.
- The levels do not change the score or the tier. The dimensions D6 and D12 contain the same
  criteria.

The Dependency track is a draft of SLSA, not an approved track. The draft describes how an
organization receives software from other parties. This skill applies the same idea to the
library: the level shows how the library controls its own dependencies.

The dependencies of a library are its packages and its base stack. The base stack is the
toolchain and the CI actions that make the library. Each library has a base stack. If the
library has no packages as dependencies, the level shows only the base stack.

The programs give the answers to these criteria where the facts are sufficient:

- `collect.py` finds the known provenance generators in the CI files. Examples are the SLSA
  generator workflows, the GitHub attestation actions, `npm publish --provenance` and the PyPI
  publish action.
- It records if the build has an identity token and if a runner is self-hosted.
- It reads the attestations in the registry record.
- It finds the commands to verify a release in the documents of the repository.
- `score.py` changes these facts into answers and into levels.

A model answers a criterion only if the facts are not sufficient.

### Base stack

The base stack is not the same in each library. Thus `collect.py` examines each part of it:

| Part | The program records | Source |
|---|---|---|
| CI action | The pin (digest, tag or floating reference), the version, the latest release, the known vulnerabilities in the version, and the number of advisories in its history | OSV and the tags of the repository of the action |
| Toolchain version | The version in `.nvmrc`, `.node-version`, `.python-version`, `.ruby-version` or `go.mod`, and its end of life | endoflife.date |
| Base image | The pin of each `FROM` line in a container file in the root | The file |

Each part gets a status:

- Red: the version has a known vulnerability, or it is past its end of life.
- Amber: the reference can change, the version is one major version or more behind, or the
  action has two or more advisories in its history.
- Green: the program found no problem.
- Unknown: the program could not get the data, or a digest has no version comment.

The report shows the parts in the table "Base stack". The criterion `D6.stack_current` is `no`
if a part is not current. The criterion `D6.stack_clean` is `no` if a part has a known
vulnerability. An advisory history alone does not change an answer.

The program examines a maximum of 12 actions. It has no data about vulnerabilities in base
images.

SLSA does not have a Release track. The facts about a release are part of the Build track.

A level in the report is an estimate from public evidence. It is not a certification.

### Optional helper programs

The skill can use two programs from other projects. The skill does not install them. If a
program is not installed, the skill gives the same levels from its own criteria.

| Program | Function | Conditions |
|---|---|---|
| [pipeline-check](https://pypi.org/project/pipeline-check/) | Examines the CI files of the clone against the SLSA Build track. It does not use the network. | The command `pipeline_check` is on the `PATH`. The program needs Python 3.11 or later. |
| [Plumber](https://getplumber.io/) | Examines the pipeline and the settings of the repository through the API of GitHub or GitLab. | The command `plumber` is on the `PATH`, and a sign-in for the host of the repository is available. For github.com, that is `GH_TOKEN`, `GITHUB_TOKEN` or `gh auth login`. For GitLab and for an instance of your own, that is `GITLAB_TOKEN`, `GH_ENTERPRISE_TOKEN` or `gh auth login --hostname`. |

- To install pipeline-check, use the command `uv tool install pipeline-check`.
- To install Plumber, obey the instructions on its website.

The programs of the skill use the findings in these ways:

- The report shows the failed checks of pipeline-check for each SLSA control.
- If pipeline-check finds a self-hosted runner that is not ephemeral, `score.py` does not
  answer `D12.provenance` and `D12.isolated` with `yes`.
- If the Scorecard has no result, the Plumber controls for branch protection and for approvals
  answer `D12.protected` and `D12.two_party`.

Other findings are evidence only. They do not set a level.

Plumber sends your token to the host of the repository. Use a token that can only read.

The integration of Plumber obeys its documentation. It was not tested with the program.

## Files

The skill writes its work files in `vet/<library>/`. In a project, the skill keeps its memory
in `.claude/library-vetting/`. The memory contains the profile of the project, the earlier
reports and their scores.

## Changes to the scoring

The file `skills/library-vetting/scripts/rubric.txt` contains the criteria. Each line contains
one criterion:

```
D2.fix30~fix | 2 | E | Median disclosure-to-fixed-release <= 30 days over the last <= 5 advisories
```

The fields are the identifier, the points, the source of the answer, and the criterion. The
source is `A` for the program, `E` for the small model, or `J` for the main model. The weights,
the disqualifiers and the rules for the tier are in `score.py`. Each report shows the version of
the rubric. Compare only reports that have the same version.

## Manual operation of the programs

```bash
LV=skills/library-vetting/scripts
python3 $LV/collect.py madler/zlib --out vet/zlib
python3 $LV/score.py vet/zlib --todo
```

The second command shows the criteria that do not have an answer.

## Network use

`collect.py` sends requests only to these hosts. It sends the name of the library, its version,
and commit identifiers. It sends no data of your project.

| Host | Purpose |
|---|---|
| The host of the repository (for example github.com) | The clone, the tags, and the tags of the CI actions |
| registry.npmjs.org, pypi.org, crates.io | The record of a package |
| api.deps.dev | The record of a package in a different registry, and the project record |
| api.osv.dev | Advisories for the library and for its CI actions |
| api.scorecard.dev | The OpenSSF Scorecard |
| api.github.com | The settings of a repository on GitHub |
| endoflife.date | The end of life of a toolchain version |

If `GITHUB_TOKEN` is set, the program sends it only to api.github.com. If a host does not
answer, the program records the error and continues. The small model can also read the pages
that `fetch_plan` lists, for example services.nvd.nist.gov.

## Limits

- The report helps you to make a decision. It does not make the decision.
- A statement about a license is analysis. It is not legal advice.
- The skill examines only the first ten direct runtime dependencies. It uses only the data of
  the registry for them.
- The skill reads npm, PyPI and crates.io directly. It reads other registries through deps.dev.
  If deps.dev is not available, the skill uses the source repository.
- The small model can make an error. Thus the main model examines its answers.
- If an agent product cannot start a second model, one model does all steps. The programs and
  the scoring stay the same.
- The setup for OpenAI Codex does not write agent files.
