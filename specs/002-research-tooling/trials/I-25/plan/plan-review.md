# Review of the plan: devsecops

Trial project: `/tmp/claude-1000/-home-cceelen-src-dump-ideas-agent-skills/4de8d85c-4862-4641-bba8-1e7b41ac5e42/scratchpad/exp-i25-plan-work/runs/1ae0287a0508`
(paths below are relative to it). Abbreviations: P = `.agents/kit/devsecops-plan.md`, S = `.agents/kit/devsecops.md`,
K = `.claude/skills/devsecops/SKILL.md`, L = `.claude/skills/devsecops/references/checklist.md`.
No reference state was given. No instruction to an agent was found in the files that I read.

## architecture

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 1. Does the plan make technical debt? | yes | P:63, P:70, S:74 | The plan accepts "no second person" reviews, a skipped Arch checksum until fixed, and suppressed scan findings as debt. |
| 2. Does the plan record each technical debt that it makes? | no | P:63 (only record), S:74 | Only the missing second person is recorded; suppressions go to a record, but the plan has no debt register. |
| 3. Maintained component in place of own construction? | partly | P:70, P:71, P:165-175 | The plan names an update program, a scan and platform attestation, but names no product and no implementation skill. |
| 4. Can a second project use the result without a change? | no | P:62-79 | Files such as rulesets, workflows and `docs/security.md` hold facts of this project (guard, COPR, OBS). |
| 5. Does the result follow a change of the project? | partly | P:70, P:78, P:101 | Renovate follows tool versions and an inventory exists, but no check ties a new package or target to the pipeline. |
| 6. Which part can fail and give no signal? | yes | P:66, P:77, P:103 | COPR and OBS builds, the nightly fuzz run and the binary cache have no signal path in the plan. |

## operations

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 1. Build one time and publish that result? | partly | P:103, P:64 | The source archive is built once, but the distribution packages are rebuilt by COPR and OBS. |
| 2. Separate rights for build and publish? | yes | P:67, P:98 | Jobs declare minimum permissions and a protected release environment holds the publish credentials. |
| 3. Procedure to withdraw or go back? | yes | P:97, P:99 | Rollback is a new publication of the last good version, with a rehearsal and a withdrawal step in the incident plan. |
| 4. Does the plan examine the published result? | partly | P:76, P:97 | It verifies archive and packages against provenance and tests a release candidate, but never installs the published package. |
| 5. Who gets a signal when the pipeline is defective? | no | P:78 (inventory and logs only); S:117-118 (C-23, C-24 declined) | No item names a receiver of a failure signal of the pipeline itself. |
| 6. What time does one run need? | no | P:109-111 | The plan gives no duration for the build, the tests or the fuzz run. |

## quality

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 1. Tests? | yes | P:110 | Unit, command line, scenario and container tests exist and run in the pipeline; `meson test` passed 12 of 12. |
| 2. Static analysis? | yes | P:73, P:111, P:71 | Lints as errors, hook configuration and a required analysis step are planned. |
| 3. Test coverage measured? | no | P:14, P:112; CONTRIBUTING.md:123-127, CONTRIBUTING.md:172 | `coverage.yml` is absent and no item restores the coverage measurement or its 100 percent limit for the guard. |
| 4. Robustness tests for each reader of untrusted input? | partly | P:77, P:56; `fuzz/fuzz_targets` | Four fuzz targets get a run, but udev, BPF and extension input is unexamined because source was not read. |
| 5. Which checks stop a change? | partly | P:109, P:71 | Required pipeline checks and scan limit stop a change; fuzz and coverage do not, and the plan lists no set of stoppers. |

## development

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 1. Same checks before the push? | partly | P:111, P:73; CONTRIBUTING.md:69 | Hooks and `meson test` run locally, but scans, fuzz and provenance checks do not. |
| 2. What time does a developer wait? | no | P:109-111 | No duration for the pipeline or the hooks is given. |
| 3. What does an outside contributor need? | partly | P:63, P:114; CONTRIBUTING.md:163 | CONTRIBUTING.md names the checks but describes workflows that do not exist; the plan fixes this only by C-37. |

## security

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 1. Which basic practices does the plan leave out? | partly | P:81-85, P:121-126, S:148-155 | Security has no declined item, but C-08 has no table row, and C-35, C-36, C-42 get no change. |
| 2. Reason for each practice left out? | partly | S:117, S:118, S:121; P:121-126 | C-23, C-24, C-27 have reasons (proposals); C-35, C-36, C-42 have only "could not be examined". |

## integrity

Assets and the three questions. Q1 who can change without trace; Q2 what shows it; Q3 is the check tied to the asset.

| Asset | Q | Result | Evidence | Sentence |
|---|---|---|---|---|
| Source | 1 | partly | P:62, P:10-29 | The repository has no remote and one unsigned commit; today any local user can rewrite it. |
| Source | 2 | partly | P:62 | Planned ruleset, signed commits and linear history show a change. |
| Source | 3 | partly | P:62, P:100 | Signatures bind to the commit; the ruleset file is not bound to the live setting. |
| Inputs from outside (crates, flake inputs, images, actions, Arch archive) | 1 | yes | P:70 | The Arch recipe skips the checksum and `fuzz/` has a version range without a lock file. |
| Inputs from outside | 2 | partly | P:70, P:69 | Lock files, digests, pinned actions and a bill of materials show a change, after the fixes. |
| Inputs from outside | 3 | yes | P:70 | Lock entries and digests bind to the input; the update program needs an owner to review its pull requests. |
| Build | 1 | yes | P:64, P:66 | Today builds run on a computer with no record; COPR and OBS builds are outside this project. |
| Build | 2 | partly | P:65, P:66 | Platform attestation covers the archive; no provenance of this project covers OBS and COPR packages. |
| Build | 3 | partly | P:65, P:102 | Provenance binds to the archive digest; the packages have no such binding. |
| Tests | 1 | yes | P:109-111 | A maintainer can edit or delete a test in a change that the same person approves. |
| Tests | 2 | partly | P:63, P:110 | Review and a required pipeline show it, but with one maintainer the review is not independent. |
| Tests | 3 | no | P:110, P:109 | No check ties a test run to the digest of the released archive. |
| Results of tests and checks | 1 | yes | P:71, P:110 | Run logs of the hosted platform expire and no copy is planned. |
| Results of tests and checks | 2 | partly | P:77, P:100 | Only the dated fuzz summary and the release record are kept. |
| Results of tests and checks | 3 | partly | P:100 | The release record names the commit and the run, but scan and coverage results are not in it. |
| Released result (source archive) | 1 | partly | P:103 | A release that cannot be changed is planned; today there is no store. |
| Released result | 2 | yes | P:65, P:103 | Provenance, digest and a second build from the signed tag (P:102) show a change. |
| Released result | 3 | yes | P:102, P:103 | Tag, digest and provenance bind to the archive. |
| Thing the user gets (distribution packages, Nix cache) | 1 | yes | P:66, P:103 | COPR, OBS and the cache builders can change a package and leave no record of this project. |
| Thing the user gets | 2 | partly | P:76, P:103 | Package-repository keys and a document tell the user to verify; nothing enforces it. |
| Thing the user gets | 3 | no | P:103, P:148 | The archive digest is checked; the built package has no digest or provenance tied to it. |
| System on which it runs (root, kernel, sysfs, thermal limits) | 1 | yes | S:33, P:72 | The guard runs as root; the plan does not record a change of the host configuration. |
| System on which it runs | 2 | partly | P:72, P:73 | A threat model, the unit check and default settings are planned; the code was not read. |
| System on which it runs | 3 | not applicable | S:33 | Host state is outside the pipeline; no check is tied to a host. |
| Data read and written (thermal offset, sysfs, /dev/kmsg, notes directory) | 1 | yes | S:33, P:89-90 | The guard writes to sysfs as root; the plan did not read the source to find other writers. |
| Data read and written | 2 | partly | P:72, P:77 | Threat model and fuzz targets for kmsg, notes, config and numbers show faults, not changes. |
| Data read and written | 3 | partly | P:77 | Fuzz seeds bind to named parsers, not to data on a machine. |
| The pipeline itself | 1 | yes | P:62, P:63 | One maintainer can change workflows, ruleset and CODEOWNERS; a UI change of a ruleset leaves no file diff. |
| The pipeline itself | 2 | partly | P:62, P:70 | Rules as a file and pinned components show a change in the repository, not in the live setting. |
| The pipeline itself | 3 | no | P:62 | Nothing compares the ruleset file with the live platform setting. |
| Records (selection, plan, CHANGELOG, docs) | 1 | yes | P:99, P:100 | Records are plain files that the one maintainer edits. |
| Records | 2 | partly | P:100, P:116-118 | Git history and a release record show a change; no dated review of governance records is bound to a commit. |
| Records | 3 | partly | P:100 | The release record names the commit; governance documents do not. |

Questions 4 to 7.

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 4. Where does the evidence chain end? | yes | P:66, P:103, P:148 | It ends at the source archive; packages from COPR, OBS and the cache, and the install on a machine, have no chain. |
| 5. Which results are kept, which lost? | partly | P:65, P:69, P:77, P:100 | Provenance, bills of materials, fuzz summary and release record are kept; test, scan and coverage results are lost after the run. |
| 6. Can one change weaken a check and pass? | yes | P:63, P:70, S:74; K:70 | One maintainer can edit a limit, a suppression record or the ruleset and approve it alone. |
| 7. Does the risk analysis ask what the result does to the system and data? | partly | S:32-33; K:70-71 | The dimensions ask about private data and failure damage; the selection answers it, but the recipe does not ask it. |

## product owner

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 1. Decisions left to the owner? | yes | P:128-139 | Five decisions are listed, with the ten decisions of the selection (S:63-78). |
| 2. Marked as proposal? | partly | P:3-5, S:9-12, S:65 | The plan and the selection are marked as a proposal; the list in P:128-139 is not marked item by item. |
| 3. Frameworks named? | partly | S:56-61, P:146-153 | The selection names four regulations; the plan names only generic target names. |
| 4. Items mapped to frameworks? | partly | S:56-61; P:60 | The selection maps items to the four; the plan tables have no such column. |
| 5. Level of each target reached? | partly | P:146-153 | Levels are given for six targets, but the weekly practice score has no item in the plan that produces it. |
| 6. What stops the next level? | yes | P:146-153 | Each row names the stop, such as one maintainer for Source L4. |
| 7. Effort in proportion to risk? | no | P:33-37, P:153, S:33 | 37 failing items for one maintainer and a medium, single-machine risk; the plan gives no counts of files or work. |

## views of the recipe

Questions 2 and 3: `not applicable`. The caller gave no reference state (task file `factory/sota-research/prompts/plan-review.md:131-132` and the caller's message).

| View | Question | Result | Evidence | Sentence |
|---|---|---|---|---|
| operations | 1 | partly | S:117, S:118, S:121; K:43 | Level 1 items C-23, C-24, C-27 are declined as proposals, so a basic practice is not held. |
| operations | 2 | not applicable | no reference state | None given. |
| operations | 3 | not applicable | no reference state | None given. |
| security | 1 | partly | P:62-79, P:81-85 | C-01 to C-19 and C-44 have changes; C-08 has no table row. |
| security | 2 | not applicable | no reference state | None given. |
| security | 3 | not applicable | no reference state | None given. |
| quality | 1 | partly | P:109-119, P:121-126 | C-30 to C-34, C-37 to C-41, C-43 have changes; C-35, C-36, C-42 have none. |
| quality | 2 | not applicable | no reference state | None given. |
| quality | 3 | not applicable | no reference state | None given. |

## Findings

1. The plan has no register of the technical debt that it makes. Only the missing second person is noted (P:63). Viewpoint: architecture. Route: `recipe`.
2. No check keeps the pipeline current when a package or a distribution is added; only a readiness checklist exists (P:101). Viewpoint: architecture. Route: `recipe`.
3. The capabilities have no named maintained component, and no implementation skill is installed (P:165-175). Viewpoint: architecture. Route: `implementation skill`.
4. COPR and OBS builds, and the binary cache, have no provenance of this project and no failure signal (P:66, P:103). Viewpoint: architecture. Route: `implementation skill`.
5. Packages are rebuilt by COPR and OBS, so the artifact that was tested is not the artifact that is published (P:103). Viewpoint: operations. Route: `implementation skill`.
6. The plan never examines a published package from a package repository after publication (P:76, P:97). Viewpoint: operations. Route: `implementation skill`.
7. No item gives a signal to a person when the pipeline itself fails, and C-23 is declined for a project without a service (P:78, S:117). Viewpoint: operations. Route: `recipe`.
8. The plan gives no run time and no wait time for the pipeline or the hooks (P:109-111). Viewpoint: operations. Route: `tooling`.
9. The coverage measurement and the 100 percent limit of the guard are not restored by any item (P:14, P:112; CONTRIBUTING.md:123-127). Viewpoint: quality. Route: `recipe`.
10. Robustness tests cover four parsers only; the source was not read, so other readers of untrusted input are unknown (P:56, P:77). Viewpoint: quality. Route: `tooling`.
11. The plan does not list which checks stop a change; fuzz and coverage do not (P:77, P:109). Viewpoint: quality. Route: `tooling`.
12. Local runs cover lints and tests only; scans, fuzz and provenance checks have no local form (P:111, P:71). Viewpoint: development. Route: `tooling`.
13. C-08 is outside the security table, so it has no files and no owner column (P:81-85). Viewpoint: security. Route: `tooling`.
14. Level 1 items C-35, C-36 and C-42 are adopted but have no change and no reason (P:121-126, S:148-155). Viewpoint: security. Route: `tooling`.
15. Level 1 items of operations C-23, C-24, C-27 are declined, which conflicts with the rule that the basics of each view are covered (S:117-121, K:43). Viewpoint: views of the recipe. Route: `recipe`.
16. The chain of evidence ends at the source archive; the packages that the user installs have no digest or provenance tied to them (P:103, P:148). Viewpoint: integrity. Route: `implementation skill`.
17. One maintainer can weaken the ruleset, a limit or a suppression and approve it alone; the live ruleset is not compared with its file (P:62-63, S:74). Viewpoint: integrity. Route: `recipe`.
18. Results of tests, scans and coverage are lost after the run; only provenance, bills of materials, a fuzz summary and the release record are kept (P:65, P:69, P:77, P:100). Viewpoint: integrity. Route: `recipe`.
19. The risk dimension `exposure` asks about private data, not about the data and the system that the result changes (S:32, K:70). Viewpoint: integrity. Route: `recipe`.
20. The plan tables carry no framework or rule per item, and the plan names no framework (P:60, P:146-153). Viewpoint: product owner. Route: `tooling`.
21. The repository practice score is a target level of the plan, but no item or file produces it (P:151, P:62-79). Viewpoint: product owner. Route: `tooling`.
22. The plan gives no counts of files or changes against the risk, for 37 failing items and one maintainer (P:33-37, P:153). Viewpoint: product owner. Route: `tooling`.

Counts by route: recipe 8 (findings 1, 2, 7, 9, 15, 17, 18, 19); tooling 9 (8, 10, 11, 12, 13, 14, 20, 21, 22); implementation skill 5 (3, 4, 5, 6, 16).

## Files read

- `.agents/kit/devsecops-plan.md`
- `.agents/kit/devsecops.md`
- `.claude/skills/devsecops/SKILL.md`
- `.claude/skills/devsecops/references/checklist.md`
- Searched or listed: `CONTRIBUTING.md` (lines 69-172 by search), `Cargo.toml` (lints), `packaging/arch/PKGBUILD` (checksum line), `.github/` and `docs/` (file lists), `fuzz/` (file list).

## Not verified

I did not verify the claim of 12 of 12 passing tests, the secret search, the digests in the Dockerfiles, the packaging recipes other than the Arch checksum line, the source code, or any setting of a platform.
