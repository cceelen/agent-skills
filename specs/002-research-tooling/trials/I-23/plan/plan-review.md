# Review of the plan: devsecops

Paths: `P` = `.agents/kit/devsecops-plan.md`, `S` = `.agents/kit/devsecops.md`, `C` = `.claude/skills/devsecops/references/checklist.md`, `K` = `.claude/skills/devsecops/SKILL.md`, all in the trial project. Other files are given with their path. No reference state: its questions are `not applicable`.

Note on the files: no file contains an instruction to an agent that I must report. The plan and the selection say that the owner decided nothing (P:3, S:3).

## architecture

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 1. Does the plan make technical debt? | yes | P:67, P:74, P:92 | C-03 stays failed, the Arch and Alpine checksums and the `fuzz/` lock file are left as open owner decisions, and four items are declined. |
| 2. Does the plan record each debt it makes? | partly | S:154-164, P:67, S:92 | The failed C-03 and the declines are recorded; no list of debt exists, and the open C-10 cases have no record place. |
| 3. Maintained component in place of own construction? | no | P:29-34, P:94, P:145, C:41 | The plan names no component for any capability, though C-33 asks that each step names one or says why none is used. |
| 4. Can a second project use the result without change? | partly | P:71, P:94 | Only one reusable workflow is planned; the other workflows, the release document and the threat model are specific to this project. |
| 5. Does the result follow a change (component, target, tool version)? | partly | P:113, P:96, P:74 | The update tool covers crates, Nix inputs, images and components; a new package target is caught only by the C-35 list comparison. |
| 6. Which part can fail and give no signal? | no | P:75, P:110, P:78 | The plan does not say; the scheduled scan, the coverage upload, the link check and the proposed review each six months can stop with no signal. |

## operations

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 1. Build once, publish that result? | yes | P:92 | The archive is built one time; later jobs and outside builders take that file and its digest is compared. |
| 2. Separate rights for build and publish? | yes | P:72 | Only the publish job has the publication credentials, and the aports and Nix cache pushes are separate jobs with own credentials. |
| 3. Procedure to withdraw or go back? | yes | P:93, S:62 | C-25 gives a withdraw and rollback procedure, run once with a pre-release. |
| 4. Does the plan examine the published result? | partly | P:81, P:84 | A job after the release verifies provenance; no step installs or tests the published packages, the Nix cache content or the aports change. |
| 5. Who gets a signal when the pipeline is defective? | no | P:35-39, P:109 | The plan names no receiver or alert for a failed or silent pipeline; C-28 is declined (S:109) and C-52 is a review each six months. |
| 6. What time does one run need? | partly | S:60 | Only a proposed target exists (tests under ten minutes); the plan has no measured time and no job gives a time. |

## quality

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 1. Tests? | yes | P:103, P:104 | `meson test` ran 12 of 12 tests; the plan makes it a required job and adds a test-plan table. |
| 2. Static analysis? | yes | P:78, P:105 | C-14 adds a static analysis job and C-40 a lint job that treats a warning as an error. |
| 3. Measures coverage? | yes | P:110 | A coverage job shows the values in the run summary and keeps the limit of the guard. |
| 4. Robustness tests for each part that reads untrusted input? | partly | P:78, fuzz/Cargo.toml:1, fuzz/Cargo.toml:25 | Fuzz seeds run, but the targets cover only the guard parsers; sysfs reads of `second-screen/src/sysfs.rs` and `keyboard-state/src/device.rs` have none. |
| 5. Which checks stop a change? | partly | P:103, P:105, P:78, P:110 | Test, lint and a severity limit on analysis are meant to fail a run; the plan gives no list of required checks, and the coverage limit applies to the guard only. |

## development

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 1. Same checks before the push? | partly | P:68, P:105, CONTRIBUTING.md:69-75 | The pre-commit file is planned for secrets, lint and links; the test, analysis, scan and coverage jobs have no local command in the plan. |
| 2. Time a developer waits? | partly | S:60 | Only the proposed targets exist; the plan measures nothing and does not set a limit for the pre-commit run. |
| 3. What does an outside contributor need? | partly | P:79, P:20-22, CONTRIBUTING.md:163-172 | The rules exist in `CONTRIBUTING.md`; the plan adds approval for new contributors but does not say how a fork gets the checks without a credential. |

## security

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 1. Which basic practices does the plan leave out? | yes (it gives the answer) | S:92, S:109, S:133, S:77 | C-19, C-28 and C-48 (all level 1) are declined, and C-03 cannot pass with one maintainer. |
| 2. Reason for each practice left out? | partly | S:92, S:109, S:133, S:142 | Each decline has a reason, but every reason is only a proposal of the agent; the owner gives no reason, and C-03 only notes the cause. |

## integrity

Assets (found in P, S, README.md, CONTRIBUTING.md, `packaging/`, `flake.nix`): source, outside inputs, build, tests, check results, released archive, packages (OBS, COPR, Nix cache, aports), user system and data, pipeline, records. Questions 1 to 3 per asset.

| Asset | Q1: change with no trace | Q2: what shows a change | Q3: tied to the asset? |
|---|---|---|---|
| Source | The owner, alone: one maintainer, no second reviewer (P:67); the one commit has no signature (P:65). | Protected branch and pull request (P:65); no signed commits planned. | partly: the pull request is tied to a commit, the one approver is the author. |
| Outside inputs: crates, Nix inputs, image digests | A lock file entry changed by one update pull request (P:113); `fuzz/` has no lock file (P:74). | Lock files, the scan, the update tool (P:75, P:113). | partly: a digest ties `Cargo.lock` and `flake.lock`; `fuzz/` and the Arch and Alpine recipes are not tied (P:74). |
| Outside inputs: pipeline components | A moving reference in a workflow. | Pin by commit digest (P:74, S:56). | yes: the pin is tied to a commit. |
| Build | The platform and the runner; the platform record is a list the owner keeps by hand (P:80). | Provenance and the L3 workflow (P:70, P:71). | yes for the archive and packages the pipeline builds; OBS and COPR rebuilds are outside (P:126). |
| Tests | A change of a test or fixture in the same pull request as the code. | Pull request checks (P:103). | no: the plan does not tie a result to the source revision or fail on a deleted test. |
| Check results (tests, scans, coverage) | Anyone who can edit a workflow; the run logs expire. | The run summary (P:110); no archive. | no: summaries are not tied by a digest to an artefact. |
| Released archive | The release job; a tag moved after the release (P:86). | Provenance, immutable releases, tag rule (P:70, P:86). | yes: provenance names the digest and the source revision. |
| Packages (OBS, COPR, Nix cache, aports) | OBS, COPR and Cachix accounts and their tokens (P:66, P:92). | Provenance only for packages the pipeline builds (P:70); nothing for the others. | no: the plan names no check that ties the package a user gets to the archive digest, beyond a rebuild in OBS. |
| System where it runs (root service, udev, BPF) | A root program or kernel program with a fault or an attack (S:41). | Threat model and unit hardening check (P:77, P:82). | no: no check ties the installed unit and program to the released file. |
| Data it reads and writes (sysfs, `/dev/kmsg`, config file, HID) | Hardware or a local user writes input. | Fuzz seeds for the guard parsers only (P:78). | partly: the guard is covered; the other programs are not. |
| Pipeline (workflows, settings, allow-list, secrets) | The owner, or an update pull request, edits a workflow; a platform setting changes with no diff (P:80). | Pull request and required checks (P:65); settings list in a document (P:80). | no: the settings list is a text file, not a read of the real settings, and the repository has no remote (P:35-39). |
| Records (selection, plan, release notes, `docs/*`) | The owner edits `S` and `P` freely; the C-22 result is written by hand (P:85). | Git history; a dated review (P:109). | no: the dated record is a statement of a person, not a program record (K:34). |

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 4. Where does the chain of evidence end before the user? | yes (the plan gives the answer) | P:126 | It ends at the archive, the Nix packages and the packages built by the pipeline; OBS and COPR packages carry the evidence of those services. |
| 5. Which check results are kept, which lost? | partly | P:86, P:110 | Only "a stated time for the records of the build" is kept; test, scan, lint and coverage results stay in run logs and summaries. |
| 6. Can one change weaken a check and pass? | yes (it can) | P:67, P:79, P:110 | One maintainer can change a workflow, a test, a severity limit or the coverage limit in a pull request and approve it; the plan has no rule against it. |
| 7. Does the risk analysis ask what the result does to the system and its data? | partly | S:41, S:24, P:77 | One row asks about harm and names root and kernel code; it asks nothing about what the programs can write to the system or the files. |

## product owner

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 1. Decisions left to the owner? | yes | P:10-25, P:65-85, P:74 | The plan lists three first decisions and an "only the owner" cell for each item. |
| 2. Is each marked as a proposal? | yes | P:3, S:3 | The status line of both files says that all answers and targets are proposals. |
| 3. Which frameworks or rules does the plan name? | yes | P:124-133 | Build and source levels, the baseline of an open project, the score of the security checks, a badge and test coverage; no regulation (P:24-25). |
| 4. Does the plan map each item to them? | no | C:16-67, P:63-113 | The checklist column for regulation and governance is empty, and the plan tables have no framework column. |
| 5. Which level of each measured target does the plan reach? | yes | P:124-133 | L2 then L3 of build, the first level of source, baseline 1, a first score, passing; the other three are "not planned". |
| 6. What stops the next level? | yes | P:126-133 | Each row gives a reason; three rows say "a decision of the owner" with no reason. |
| 7. Effort in proportion to the risk? | partly | P:47-56, S:154 | 41 items in 8 steps for one maintainer; the order follows the credential risk, but the plan gives no effort count or cut-off. |

## views of the recipe

Question 2 and 3: `not applicable` (no reference state given). The files for the answer are only the plan and the selection.

| View | Q1: items of level 1 in the plan? | Q2 | Q3 |
|---|---|---|---|
| security | partly: 19 of 20 level-1 items adopted; C-19 declined, C-03 cannot pass (S:77, S:92, P:67). | not applicable | not applicable |
| operations | partly: 5 of 6 level-1 items adopted; C-28 declined (S:104-110, P:90-97). | not applicable | not applicable |
| quality | partly: 7 of 8 level-1 items adopted; C-48 declined (S:125-134, P:99-113). | not applicable | not applicable |

## Findings

1. The plan has no signal or owner for a defective or silent pipeline (scheduled scan, coverage upload, fuzz run); evidence P:35-39, P:109 and S:109. Viewpoint: operations. Route: recipe.
2. The plan names no maintained component for any capability, though C-33 needs a name or a reason; evidence P:29-34, P:94, C:41. Viewpoint: architecture. Route: implementation skill.
3. Packages in the Nix cache, the aports push and the OBS and COPR rebuilds have no check tied to the archive digest; evidence P:70, P:126. Viewpoint: integrity. Route: recipe.
4. One maintainer can weaken a workflow, a test or a limit and approve it; the plan has no rule against it; evidence P:67, P:79, P:110. Viewpoint: integrity. Route: recipe.
5. Results of tests, scans, lint and coverage are not kept as evidence; only the build records get a stated time; evidence P:86, P:110. Viewpoint: integrity. Route: recipe.
6. The settings of the platform are recorded by hand in a text file; no check compares them with the real settings, and the repository has no remote; evidence P:35-39, P:80. Viewpoint: integrity. Route: tooling.
7. The risk analysis does not ask what the root and kernel programs can do to the system and the data they change; evidence S:35-41. Viewpoint: integrity. Route: recipe.
8. Three level-1 items (C-19, C-28, C-48) are declined, one per view, with reasons that are only proposals of the agent; evidence S:92, S:109, S:133. Viewpoint: views of the recipe. Route: recipe.
9. The plan holds no list of technical debt; the open cases for the `fuzz/` lock file and the Arch and Alpine checksums have no place of record; evidence P:74, S:154-164. Viewpoint: architecture. Route: tooling.
10. Robustness tests cover the guard parsers only; the sysfs, BPF and extension readers of the other parts have none in the plan; evidence fuzz/Cargo.toml:1, P:78. Viewpoint: quality. Route: recipe.
11. The plan does not map the items to the frameworks it names, and the checklist column for them is empty; evidence C:16-67, P:63-113. Viewpoint: product owner. Route: recipe.
12. The published result is verified for provenance only; no step tests that the packages install and run; evidence P:81, P:84. Viewpoint: operations. Route: implementation skill.
13. The plan gives no list of required checks and no measured run time, and the local checks are only the pre-commit file; evidence P:103, P:105, P:68, S:60. Viewpoint: development. Route: tooling.
14. The documents describe a nightly fuzz run (`fuzz.yml`) and nightly coverage; the plan does not plan either as a job; evidence CONTRIBUTING.md:143-147, P:14-17, P:78. Viewpoint: quality. Route: tooling.

Count: 14 findings.

## Files read

- `.agents/kit/devsecops-plan.md`
- `.agents/kit/devsecops.md`
- `.claude/skills/devsecops/SKILL.md`
- `.claude/skills/devsecops/references/checklist.md`
- `CONTRIBUTING.md` (lines 105-130, 150-180, and matches for fuzz, pre-commit and coverage), `README.md` (lines 1-10), `Cargo.toml` (lines 1-40), `.gitignore` (match lines), `fuzz/Cargo.toml` (lines 1-30), and file listings of the project; `packaging/arch/PKGBUILD` and `packaging/alpine/APKBUILD` only by search for the checksum lines.

Not verified: the run of any check, the contents of the `src/` files of `keyboard-state` and `second-screen` beyond a search, the other packaging files, the git history beyond `git log --oneline`, any setting of a host, and the claim in P:65 about the author address of the commit.
