# Review of the plan: devsecops (trial project 6676c92d1681)

No reference state was given. Paths are relative to the trial project. P = `.agents/kit/devsecops-plan.md`, S = `.agents/kit/devsecops.md`, K = `.claude/skills/devsecops/SKILL.md`, L = `.claude/skills/devsecops/references/checklist.md`.

Note on safety: no file contained an instruction to the reviewer.

## architecture

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 1 Technical debt made? | partly | P:100, P:46 | Build L2 reaches only the archive and the Nix packages; the rpm, deb, Arch and Alpine packages stay without provenance. |
| 2 Debt recorded? | partly | P:100, S:57, S:97 | The gap and the AI-reviewer deviation are noted, but the plan has no debt record with owner and end date. |
| 3 Maintained component in place of own construction? | partly | P:51, P:52, P:121 | Renovate and `cargo audit` are named, but the SBOM generator is open and no implementation skill is installed. |
| 4 Reusable by a second project? | partly | P:119-121, P:62 | The plan is built on one project's files (OBS, COPR, Cachix, aports); the generic items transfer, the recipes do not. |
| 5 Follows a change of the project? | partly | P:59, P:60 | The inventory (C-18) and nightly fuzz follow changes, but a new target needs a manual readiness checklist (C-29). |
| 6 What can fail with no signal? | no | P:59, P:60, S:97 | Nightly `fuzz.yml`, `coverage.yml` and Renovate can fail silently; C-23 is declined and no item names who gets a pipeline-failure signal. |

## operations

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 1 Build once, publish the same result? | partly | P:76, P:58, P:100 | C-46 uses one archive, but COPR, OBS, Arch and Alpine rebuild packages from it, so the published packages are not the attested build. |
| 2 Separate rights for build and publish? | yes | P:48, P:70 | C-06 gives separate jobs with minimal permissions and C-22 a `release` environment with a reviewer; the files do not exist yet. |
| 3 Withdraw or roll back procedure? | partly | P:69, P:71 | A rollback is a patch release that reverts, and withdrawal is in C-25; a rollback of an installed package at the user is not covered. |
| 4 Examines the published result? | partly | P:58 | The verify step in the Packit or OBS job is "optional"; nothing examines the published repositories after the publish. |
| 5 Who gets a signal when the pipeline is defective? | no | P:60, S:97 | No item names a recipient or an alert for a broken release or nightly job; C-23 is declined. Must be at P:68-76. |
| 6 Time of one run? | no | P:82-84 | The plan gives no run time for CI, container builds or release jobs. Must be at P:82. |

## quality

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 1 Tests? | yes | P:83, CONTRIBUTING.md:163 | Unit, integration and system tests exist; the plan restores `ci.yml` to run them. |
| 2 Static analysis? | yes | P:55, P:84 | Clippy with `-D warnings`, `clang-tidy` and `biome ci` become required steps. |
| 3 Coverage measured? | partly | CONTRIBUTING.md:113-125, P:26, P:85 | The plan names `coverage.yml` only as missing and has no coverage step or limit; C-33 only collects the existing 100 % guard limit. |
| 4 Robustness tests per untrusted input? | partly | P:59, P:62, CONTRIBUTING.md:131, keyboard-state/udev/80-asus-ux8406-keyboard-state.rules.in:20 | Fuzz covers the guard parsers (`fuzz/fuzz_targets`: config, kmsg, notes, numbers); the two root helpers that take `%k` get a review, no fuzz. |
| 5 Which checks stop a change? | partly | P:53, P:55, P:82 | Required jobs with a ruleset stop a change (high findings, lints, tests); coverage and fuzz do not, and all of it is `(nv)`. |

## development

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 1 Same checks before the push? | partly | P:55, CONTRIBUTING.md:74-75 | Pre-commit is restored for lints, but the scans, the secret scan and `cargo audit` of C-11 run only in CI. |
| 2 Developer wait time? | no | P:55, P:82 | The plan gives no time for the local checks or the pre-commit run. Must be at P:82. |
| 3 What a contributor from outside needs? | partly | P:89, P:44, CONTRIBUTING.md:61 | `CONTRIBUTING.md` and the restored files tell the steps; the plan does not state the needs of a fork (no secrets, approval of runs). |

## security

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 1 Basic practices left out? | partly | P:37, S:97-98, S:118 | C-23 and C-24 (level 1) and C-39 are declined; C-39 is declined although the project prepares for the CRA. |
| 2 Reason for each? | yes | S:97, S:98, S:118 | Each decline carries a reason; the C-39 reason notes the deviation from the CRA preparation. |

## integrity

Assets and question 1 to 3. All checks in the plan are `(nv)` or fail because no pipeline exists (P:12-15, P:23-28), so every "what shows a change" is a plan item, not a check that runs.

| Asset | Q1 Who changes it, no trace | Q2 What shows a change | Q3 Tied to the asset? |
|---|---|---|---|
| Source | Anybody with a push right; the tree has one commit with author `experiment@example.invalid` (P:28), no remote (P:12) | Ruleset and signed commits (P:43) | Commit hash; ruleset is a platform setting, not tied to a commit; partly |
| Inputs from outside (crates, flake inputs, images, Actions) | Upstream changes; `PKGBUILD` has `sha256sums=(SKIP)` (packaging/arch/PKGBUILD:20); APKBUILD has no sum (P:52) | `Cargo.lock`, `flake.lock`, Renovate, digests (P:52) | Digests tie it; the `cargo audit` result is not tied to a lock digest, and the advisory date is unverified (P:16-17) |
| Build | Anyone who edits a workflow; the Packit, OBS and COPR builds | Attestation of archive and Nix packages (P:46) | Provenance by digest for those two; none for rpm, deb, Arch, Alpine (P:100) |
| Tests | A change that edits or skips tests in the same pull request | Required job `ci.yml` (P:82) | Result bound to a commit by the platform, but not recorded by the plan |
| Results of tests and checks | Anyone who reruns or deletes a run; no retention step | Codecov and run summaries (CONTRIBUTING.md:121-123) | Not tied: the plan has no archive of results by commit |
| Released result | A maintainer account or a stolen release token | Attestation, SBOM, digest in recipes (P:46, P:51, P:52) | Digest of the archive; the packages that users install are not tied |
| Thing the user installs | OBS, COPR, Cachix, Alpine accounts and repositories | `signed-by`, pacman key, COPR, Nix cache key (P:57) | Signatures of the repository, not of the attested archive; verify step is optional (P:58) |
| System it runs on | Root helpers and the guard run on the user's laptop; `keyboard-state load %k` runs as root from udev (keyboard-state/udev/80-asus-ux8406-keyboard-state.rules.in:20) | Review of the helpers (P:62) | Not a check: a judgement, undated and not tied to a commit |
| Data read and written | `/dev/kmsg` writable from user space, configuration file, sysfs (P:54) | Fuzz of parsers, threat model (P:54, P:59) | Fuzz and model are not tied to the code version |
| Pipeline itself | Workflow files, Renovate, rulesets, runner settings | Pinned digests, `permissions`, workflow analysis (P:48, P:52, P:53) | Pins tie it; the ruleset and the environment are platform settings with no record |
| Records of the project | Issues, labels, `docs/*.md`, changelog | `CODEOWNERS`, review (P:91) | `CODEOWNERS` is not said to cover `.github/` and `docs/`; no digest |

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 4 Chain ends before the user | no | P:100, P:46 | The chain ends at the source archive and the Nix packages; rpm, deb, Arch and Alpine packages are built by COPR and OBS without provenance. |
| 5 Which results are kept? | partly | P:46, P:59, CONTRIBUTING.md:121 | Provenance, SBOMs and a dated fuzz summary are kept; test, scan and coverage results are lost after the run. |
| 6 Can one change weaken a check and pass? | yes (defect) | P:53, P:91, S:57 | A change can edit `deny.toml`, a workflow or the ruleset, and the AI reviewer approves the owner's own change. |
| 7 Selection asks what the result can do to the system and its data? | partly | S:48-49 | The rows ask the damage of failure and name root and `/dev/kmsg`, but do not ask what the code can do to the host and its data. |

## product owner

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 1 Decisions left to the owner | yes | P:123-127, S:52-65 | Ten decisions are in S; the plan names six and leaves out four (interval of tests, scan limit, rhythm, where the build runs). |
| 2 Marked as proposal? | yes | S:9-11, S:54-65 | The status line and each row mark them as proposals. |
| 3 Frameworks named | yes | S:36-39 | CRA, product liability directive, DORA and PCI DSS are named with who they bind. |
| 4 Items mapped to frameworks | partly | S:79-122, P:41-94 | The selection tags `(prepared: CRA)` on the items; the plan tables carry no framework column. |
| 5 Level of each target | partly | P:100-105 | Build L2 only for the archive and Nix packages, while S:56 proposes "Build L2 for each release artifact"; four other targets are "not assessed". |
| 6 What stops the next level | yes | P:100-105 | Each row names a blocker, mostly "no remote" or "a self-assessment". |
| 7 Effort in proportion to risk | no | P:36, S:49 | 42 items, nine new documents and a mirror plan for one maintainer at medium criticality; the plan gives no cost or priority by risk. |

## views of the recipe

Questions 2 and 3: not applicable (no reference state).

| View | Q1 Basic practices (level 1) held? | Evidence | Sentence |
|---|---|---|---|
| security | partly | P:41-62, S:71-90 | C-01 to C-19 and C-44 are adopted with a change each; all fail and most depend on missing files. |
| operations | partly | P:66-76, S:94-105 | C-21 to C-27, C-29, C-45, C-46 are adopted, C-23 is declined; C-20 depends on files that are absent. |
| quality | partly | P:80-94, S:109-122 | C-30 to C-43 are adopted except C-39; the review rests on `ci.yml` that is absent. |

## Findings

1. The plan names no recipient of a signal when a release, nightly or Renovate job fails (P:60, S:97). Viewpoint: operations. Route: recipe.
2. The recipe has no item for the examination of the published packages after the publish; the verify step is "optional" (P:58, L:53). Viewpoint: operations. Route: recipe.
3. The plan gives no run time of CI, release or local checks (P:82-84, P:55). Viewpoint: operations (also development). Route: recipe.
4. The plan has no coverage measurement step and no coverage limit beyond the existing guard limit (CONTRIBUTING.md:113-125, P:85). Viewpoint: quality. Route: recipe.
5. Fuzz covers the guard parsers only; the root helpers `second-screen` and `keyboard-state` that read `%k` get a review, not a robustness test (P:59, P:62, CONTRIBUTING.md:131). Viewpoint: quality. Route: recipe.
6. The security scans and `cargo audit` run only in CI, not before the push (P:53, P:55). Viewpoint: development. Route: tooling.
7. The rpm, deb, Arch and Alpine packages have no provenance; the chain ends before the user (P:100, P:46). Viewpoint: integrity. Route: implementation skill.
8. The released packages are rebuilt by COPR, OBS, Arch and Alpine, not the attested build (P:76, P:100). Viewpoint: operations. Route: implementation skill.
9. Results of tests, scans and coverage are not kept per commit as evidence (P:46, CONTRIBUTING.md:121). Viewpoint: integrity. Route: recipe.
10. One change can edit a scan limit, a workflow or the ruleset and pass, because the AI reviewer approves the owner's own change (P:53, P:91, S:57). Viewpoint: integrity. Route: recipe.
11. The risk dimensions ask the damage of a failure, not what the result can do to the host system and its data (S:48-49, L:60). Viewpoint: integrity. Route: recipe.
12. The test, scan and `cargo audit` results are not tied to the commit; the advisory date is unverified (P:16-17). Viewpoint: integrity. Route: tooling.
13. The plan states Build L2 for two artifact kinds while the selection proposes L2 for each artifact (P:100, S:56). Viewpoint: product owner. Route: implementation skill.
14. The plan lists six of ten owner decisions; four decisions of S:60-65 are missing from P:125-127. Viewpoint: product owner. Route: tooling.
15. The plan has no framework column, so an auditor cannot follow an item to its source from the plan (P:41-94, S:79-122). Viewpoint: product owner. Route: tooling.
16. The plan has no ranking of effort against risk for a one-maintainer project with nine new documents (P:36, S:49). Viewpoint: product owner. Route: recipe.
17. C-39 is declined although the project prepares for the CRA that asks for it (S:118). Viewpoint: security. Route: recipe.
18. The plan has no technical-debt record with owner and date (P:100, S:57). Viewpoint: architecture. Route: tooling.
19. The SBOM generator and the other constructions are not tied to a maintained component, and no implementation skill is installed (P:51, P:121). Viewpoint: architecture. Route: implementation skill.
20. Every check is `(nv)` or fails for an absent pipeline, so the distance rests on a tree without its pipeline (P:12-15, P:23-32). Viewpoint: views of the recipe. Route: tooling.

Route count: recipe 10 (1, 2, 3, 4, 5, 9, 10, 11, 16, 17), tooling 6 (6, 12, 14, 15, 18, 20), implementation skill 4 (7, 8, 13, 19). Total 20.

## Files read

`factory/sota-research/prompts/plan-review.md` (outside the project, the task file), `.agents/kit/devsecops-plan.md`, `.agents/kit/devsecops.md`, `.claude/skills/devsecops/SKILL.md`, `.claude/skills/devsecops/references/checklist.md`, `CONTRIBUTING.md` (parts), `Cargo.toml` (lints), `flake.nix` (parts), `packaging/arch/PKGBUILD` and `packaging/alpine/APKBUILD` (by search), `keyboard-state/udev/80-asus-ux8406-keyboard-state.rules.in`, `tcc-guard/systemd/asus-ux8406-tcc-guard.service.in` (by search), `CHANGELOG.md` (by search), file listings of `.github`, `docs`, `fuzz`, `.agents`.

Not verified: the claims on COPR, OBS, Packit, Cachix and Alpine (no remote, files absent); whether `tests/cli` and `tests/scenarios` named in P:83 exist (a listing shows tests under `tcc-guard/tests`); the systemd exposure value 1.3; the run time of any check; the content of the original repository.
