# Review of the plan of the recipe `devsecops`

- Trial project: `<trial project>`. A path without a prefix is in this folder.
- Reference state: `<reference>`. A path with the prefix `ref:` is in this folder.
- `plan` is `.agents/kit/devsecops-plan.md`. `selection` is `.agents/kit/devsecops.md`.
- `skill` is `.claude/skills/devsecops/SKILL.md`. `checklist` is `.claude/skills/devsecops/references/checklist.md`.
- The plan and the selection are present. The two files have the status "PROPOSED" (plan:3, selection:3).

## Instructions to an agent that the files contain

They were not obeyed. They are reported here as the task requires.

- skill:12-25 and skill:173-183 hold instructions to the agent that uses the skill.
- plan:160-165 tells what is done after the owner accepts the plan.
- `ref:.github/workflows/review.yml:55-56` holds a prompt for an AI reviewer ("You are a senior engineer ...").

## architecture

| # | Question | Result | Evidence | Sentence |
|---|---|---|---|---|
| 1 | Does the plan make technical debt? | yes | plan:68 | The component for isolated builds stays open, and plan:67 leaves `fuzz/Cargo.lock` out of the pins without a change. |
| 2 | Does the plan record each technical debt that it makes? | partly | plan:134 | The target table records what stops each next level, but the plan has no record of the debts of rows C-14, C-12 and C-29. |
| 3 | Maintained component in place of an own construction? | partly | plan:8 | The plan names capabilities, not components; plan:63 and plan:65 describe an own digest comparison and an own digest file. |
| 4 | Can a second project use the result without a change? | no | plan:59 | Each change is a file of this project (`.github/workflows/*`, the recipes); no shared or reusable part is planned. |
| 5 | Does the result follow a change of the project? | partly | plan:67 | The update tool follows new tool versions; nothing follows a new language (plan:85) or a new distribution target (plan:63). |
| 6 | Which part of the result can fail and give no signal? | no | plan:63 | The plan names no such part; the distribution builds are "outside the check", and scheduled analyses (plan:84) have no named receiver. |

## operations

| # | Question | Result | Evidence | Sentence |
|---|---|---|---|---|
| 1 | Build one time and publish that same result? | yes | plan:63 | The release job gives out the tested archive after a digest comparison; the distribution packages are built again by their services. |
| 2 | Separate rights for the build step and the publish step? | yes | plan:61 | Each job states its permissions, the build and test jobs get no secret, and each secret is bound to an environment. |
| 3 | Procedure to withdraw a release or to go back? | no | plan:118 | C-62 plans only the release procedure; selection:88 puts rollback (C-55) above the target, and selection:65 drops the rehearsed rollback. |
| 4 | Does the plan examine the published result? | partly | plan:66 | A user command verifies the provenance and plan:63 compares digests before upload; no step examines the release after publication. |
| 5 | Who gets a signal when the pipeline itself is defective? | no | plan:61 | The plan names no receiver and no check of the secrets, the build services or the schedules of the pipeline. |
| 6 | What time does one run need? | no | selection:62 | The selection proposes a fast first build and slower stages; the plan gives no time and no time limit. |

## quality

| # | Question | Result | Evidence | Sentence |
|---|---|---|---|---|
| 1 | Does the plan have tests? | yes | plan:60 | A workflow runs the build and test command of C-04 on each change; plan:127 records 12 correct tests. |
| 2 | Does the plan have static analysis? | yes | plan:85 | One security analysis job for each language (plan:85), lints that deny warnings (plan:86) and a pre-commit job (plan:103). |
| 3 | Does the plan measure the test coverage? | partly | plan:142 | Coverage is only in the target table; no change row, no file and no capability carries it. |
| 4 | Robustness tests for each part that reads untrusted input? | no | plan:155 | The fuzz targets exist (`CONTRIBUTING.md:133`) but no change runs them; selection:123 puts C-26 above the target. |
| 5 | Which of these checks stop a change? | partly | plan:109 | The test job (owner sets the rule) and the lint job (plan:86) stop a change; plan:85 leaves "block or are recorded" open. |

## development

| # | Question | Result | Evidence | Sentence |
|---|---|---|---|---|
| 1 | Can a developer run the same checks before the push? | partly | plan:103 | Pre-commit and the test command (plan:127) run locally; the plan says nothing for the security and dependency analyses. |
| 2 | What time does a developer wait for the result? | no | selection:62 | No time is given in the plan or the selection. |
| 3 | What does a contributor from outside need to make a change? | partly | plan:94 | The plan lists three points to examine for outside pull requests, but not the tools or the checks that such a contributor needs. |

## security

| # | Question | Result | Evidence | Sentence |
|---|---|---|---|---|
| 1 | Which basic practices of the aspect does the plan leave out? | partly | plan:91 | The plan has no list; C-21, C-23, C-34 and C-36 get no change, and selection:119-127 leaves out C-26, C-27, C-18, C-33. |
| 2 | Does the plan give the reason for each practice that it leaves out? | partly | selection:123 | The only reason is "above the target level"; selection:45 names a reason to adopt C-26 that the plan does not answer. |

## product owner

| # | Question | Result | Evidence | Sentence |
|---|---|---|---|---|
| 1 | Which decisions does the plan leave to the owner? | yes | plan:29 | The main finding, the column "Only the owner can" (plan:57), the coverage limit (plan:142) and the selection (plan:162). |
| 2 | Is each of these decisions marked as a proposal? | partly | plan:3 | The status marks the whole plan; plan:86 ("Do not change the level") and plan:63 ("outside the check") are decisions without a mark. |
| 3 | Which frameworks or rules of governance does the plan name? | partly | plan:136 | The plan uses the levels "Build L2", "Source L2" and "baseline level" but gives no framework by its name. |
| 4 | Does the plan map each of its items to these frameworks or rules? | no | plan:57 | No row has a source unit, although skill:42 says that the skill names the source unit of each item. |
| 5 | Which level of each measured target does the plan reach? | partly | plan:134 | Build L2, Source L2 and baseline Level 1 are given; `check scores`, `test coverage` and `process capability` get no value. |
| 6 | What stops the next level of each measured target? | partly | plan:138 | Given for build, source and coverage; the baseline row gives what stops the evaluation, and plan:139 gives "—". |
| 7 | Is the effort in proportion to the risk that the plan removes? | partly | plan:57 | The target levels limit the scope (selection:33-35), but no row gives an effort, thus the proportion cannot be shown. |

## views of the recipe

| View | # | Question | Result | Evidence | Sentence |
|---|---|---|---|---|---|
| operations | 1 | Level 1 items in the plan? | yes | plan:118 | C-62 has a change; C-59 has a proposal at plan:120. |
| operations | 2 | What the reference has and the plan does not | yes | plan:118; `ref:.github/workflows/doctor.yml:1` | A daily check of the services and credentials of the release, and package builds that stop a release (`ref:.github/workflows/release.yml:109`). |
| operations | 3 | What the plan has and the reference does not | yes | plan:120; `ref:docs/releases.md:38` | A label and an analysis for a release that harmed users; the reference release document has no incident record. |
| security | 1 | Level 1 items in the plan? | partly | plan:93 | All ten items are present; C-21, C-23, C-34 and C-36 have only "what is necessary", no change and no file. |
| security | 2 | What the reference has and the plan does not | yes | plan:155; `ref:.github/workflows/fuzz.yml:71` | Nightly fuzzing with private advisories (`ref:fuzz.yml:94`), analysis of the workflows (`ref:ci.yml:174`) and attested SBOMs (`ref:release-nix.yml:85`). |
| security | 3 | What the plan has and the reference does not | yes | plan:84; `ref:SECURITY.md:13` | A written policy with a limit for each finding, and the roles (plan:87); the reference policy has only the support period. |
| quality | 1 | Level 1 items in the plan? | yes | plan:102 | C-41 and C-43 have changes; C-39, C-49, C-50 and C-51 are at plan:109-112 and plan:130. |
| quality | 2 | What the reference has and the plan does not | yes | plan:103; `ref:.github/workflows/ci.yml:100` | A check with the oldest compiler, a check of the notices (`ref:ci.yml:95`) and coverage of all programs to a service (`ref:ci.yml:245`). |
| quality | 3 | What the plan has and the reference does not | yes | plan:102; `ref:.github/workflows/ci.yml:207` | A report of tests that pass only on a retry, and a limit for the age of branches (plan:112). |
| pipeline | 1 | Level 1 items in the plan? | yes | plan:59 | All eleven items are at plan:59-67, plan:74 and plan:127. |
| pipeline | 2 | What the reference has and the plan does not | yes | plan:68; `ref:.github/workflows/release-files.yml:4` | A reusable workflow with an attest job alone (`ref:release-files.yml:32`), a verification before upload (`ref:release.yml:133`), and automated version changes (`ref:release.yml:36`). |
| pipeline | 3 | What the plan has and the reference does not | yes | plan:65; `ref:packaging/arch/PKGBUILD:20` | A digest file and digests in the two recipes; a comparison with the tested archive (plan:63), which the reference builds again (`ref:release.yml:87`). |

Remark on pipeline, question 2: plan:60 starts the pipeline on each change of the primary branch. The
reference does not (`ref:.github/workflows/ci.yml:1-3`): its ruleset requires the checks on the pull request
and a current branch (`ref:docs/releases.md:125-131`).

## Findings

1. The plan has no procedure to withdraw a release or to go back to the release before (plan:118, selection:88). Viewpoint: operations. Route: `recipe`.
2. The plan names no receiver of a signal for a defective pipeline, expired secret or stopped build service (plan:61). Viewpoint: operations. Route: `recipe`.
3. The plan gives no run time and no time limit for a run or for the wait of a developer (selection:62). Viewpoint: operations, development. Route: `recipe`.
4. No step of the plan examines the release after its publication (plan:66). Viewpoint: operations. Route: `recipe`.
5. The plan runs no robustness test, although the fuzz targets are in the tree and the guard reads untrusted input (plan:155, selection:45). Viewpoint: quality. Route: `recipe`.
6. Test coverage has no change row, file or capability; it is only a line of the target table (plan:142). Viewpoint: quality. Route: `recipe`.
7. The plan does not list which checks stop a change; plan:85 leaves "block or are recorded" open. Viewpoint: quality. Route: `tooling`.
8. The plan names capabilities and no maintained component, and it describes an own digest comparison and digest file (plan:8, plan:63, plan:65). Viewpoint: architecture. Route: `implementation skill`.
9. The component for isolated builds (C-09, Build L3) is open, thus the goal level of the owner has no route (plan:68, plan:136). Viewpoint: architecture. Route: `implementation skill`.
10. The plan records the debts of its rows only in part; `fuzz/Cargo.lock` stays out of the pins without a record (plan:67). Viewpoint: architecture. Route: `tooling`.
11. The result is for this project only and does not follow a new language or a new distribution target (plan:59, plan:85). Viewpoint: architecture. Route: `recipe`.
12. The plan names no part that can fail without a signal; the distribution builds are "outside the check" (plan:63). Viewpoint: architecture. Route: `tooling`.
13. The plan does not say if a developer can run the security and dependency analyses before the push (plan:103). Viewpoint: development. Route: `recipe`.
14. The plan does not say what a contributor from outside needs: tools, checks without secrets, approval (plan:94). Viewpoint: development. Route: `recipe`.
15. The plan has no list of the practices that it leaves out, and "above the target level" is the only reason (plan:91, selection:123). Viewpoint: security. Route: `tooling`.
16. Four level 1 security items (C-21, C-23, C-34, C-36) get no change and no file (plan:93-96). Viewpoint: security, views of the recipe. Route: `tooling`.
17. Two decisions inside change rows are not marked as proposals (plan:63, plan:86). Viewpoint: product owner. Route: `tooling`.
18. The plan names no framework and maps no item to a source unit, although skill:42 promises this; the checklist has no such column (plan:57, checklist:11). Viewpoint: product owner. Route: `tooling`.
19. Three measured targets get no level or value, and two rows do not give what stops the next level (plan:138-143). Viewpoint: product owner. Route: `implementation skill`.
20. No row of the plan gives an effort, thus the owner cannot compare effort and risk (plan:57). Viewpoint: product owner. Route: `tooling`.
21. The plan lacks what the reference has for the pipeline: an attest job alone in a reusable workflow, and a verification before upload (plan:68, `ref:.github/workflows/release-files.yml:32`). Viewpoint: views of the recipe. Route: `implementation skill`.
22. The plan lacks the daily check of the delivery services and the package builds that stop a release (plan:118, `ref:.github/workflows/doctor.yml:1`). Viewpoint: views of the recipe. Route: `recipe`.

## Files read, and what was not verified

Files read in full (trial project): `.agents/kit/devsecops-plan.md`, `.agents/kit/devsecops.md`, `.claude/skills/devsecops/SKILL.md`, `.claude/skills/devsecops/references/checklist.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `Cargo.toml`, `.gitignore`, `about.toml`, `flake.nix`, `packaging/obs/README.md`, `keyboard-bpf/.clang-tidy`; in part: `README.md` (lines 1-150, then a pattern search), `fuzz/Cargo.toml` (lines 1-50); pattern search only: `meson.build`, `*/meson.build`, `packaging/arch/PKGBUILD`, `packaging/alpine/APKBUILD`, `dev/containers/*.Dockerfile`. Files read in full (reference): `SECURITY.md`, `docs/releases.md`, `.github/workflows/ci.yml`, `release.yml`, `release-files.yml`, `codeql.yml`, `scorecard.yml`, `coverage.yml`, `.pre-commit-config.yaml`, `renovate.json`, `codecov.yml`, `.obs/workflows.yml`, `.packit.yaml`, `.plumber.yaml`; in part: `fuzz.yml` (lines 1-70, then a pattern search), `review.yml` (lines 1-56), `doctor.yml` (lines 1-35), `packages.yml` (lines 1-30); pattern search only: `release-nix.yml`, `aports.yml`, `plumber.yml`, `watch.yml`, `packaging/arch/PKGBUILD`, `packaging/alpine/APKBUILD`, and a search of the `.md`, `.yml`, `.yaml`, `.json` and `.toml` files for six words (incident, flaky, retry, severity, roles, rollback).

Not verified: each setting of GitHub and of the build services; that the reference working tree is equal to its last commit beyond `git status --short`; the source code, the tests, `agent-templates/devsecops.md`, `.github/zizmor.yml`, `.github/actionlint.yaml`, `release-please-config.json`, `.bumpversion.toml` and most of `packaging/` in the two folders; the statements of the plan about its own session (the clone, the 12 tests, the count of 115 packages, the secret search); the absence of a thing in the reference where only a pattern search was made (incident record, roles, retry report, digest file, severity policy); no test, build or tool was run.
