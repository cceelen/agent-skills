# Plan: DevSecOps

**Status: PROPOSED, not accepted.** It follows the proposed selection in
[devsecops.md](devsecops.md). No file of the project was changed but the
selection and this plan. After the owner accepts the plan, it is applied on a
new branch and given to the owner as a diff or a pull request.

Run of the checks: 2026-10-12, on the commit `09d41ab` of `main`.

## What the owner decides first

1. **Where are the pipeline files?** The documents of the tree refer to files
   that the tree does not have: `SECURITY.md`, `docs/releases.md`,
   `.github/workflows/` (`ci.yml`, `coverage.yml`, `fuzz.yml`, `review.yml`,
   `release-nix.yml`), `.obs/workflows.yml`, the pre-commit configuration, and
   the configurations of the release tool, of Packit and of the update tool.
   The references are in `README.md` (Where to start, NixOS), `CONTRIBUTING.md`
   (first table, Build and test, Coverage, Fuzzing, Rules for changes),
   `flake.nix` (comments) and `packaging/obs/README.md` (Release). If these
   files exist in a different copy of the project, the plan restores and
   examines them. If not, the plan writes them. Most of the distance below
   depends on this answer. The plan assumes that they are written anew.
2. The proposed answers, target levels and decisions of the selection, with the
   four proposed declines (C-19, C-28, C-48, C-49).
3. The answer on regulation. The agent read none.

## What stops an implementation

- No implementation skill is installed for any capability of the table "What to
  delegate" (pipeline definition on GitHub, provenance, signing, scan of
  dependencies, score of the security checks). The work is thus done with the
  tools of the project, and each setting of a component is read from the
  documentation of that component at the time of use. This plan names the
  capability and writes no setting.
- The repository has no remote. No setting of the host can be read or set.
- Each pipeline step below keeps the build, the test and the packaging in
  separate jobs, and no job gets a credential that its task does not need. A
  step that cannot keep this rule is not applied; the owner gets it as a
  question.

## Steps, in the order of the work

The order: source, secrets, hosted build with separate jobs, tests and scans on
each change, provenance and its verification, automated publication,
measurement. Step 8 of the recipe (telemetry, incidents) has no adopted item.

| Step | Content                                                      | Items                                                |
| ---- | ------------------------------------------------------------ | ---------------------------------------------------- |
| 1    | Create the repository on GitHub and protect `main`           | C-01, C-02, C-03, C-16, C-43                         |
| 2    | Secret scan; a rule for each credential of the pipeline      | C-04, C-15                                           |
| 3    | Pipeline for a change: build, test, lint as separate jobs    | C-05, C-08, C-33, C-37, C-40, C-14, C-39             |
| 4    | Scans and updates of the dependencies; pins                  | C-10, C-11, C-51, C-20                               |
| 5    | Release pipeline with provenance and SBOM: build level L2    | C-06, C-09, C-24, C-32, C-23, C-17, C-25             |
| 6    | Isolate the build from the signing: build level L3           | C-07, C-21                                           |
| 7    | Documents                                                    | C-12, C-13, C-18, C-34, C-35, C-38, C-41, C-42, C-45, C-47 |
| 8    | Measure and record                                           | C-22, C-52                                           |

Step 7 does not depend on the pipeline. `SECURITY.md` (C-12) and
`docs/releases.md` come first in it, because two documents link to them now.

## View: security

| Item | What the check found | Change | Files | Only the owner |
| ---- | -------------------- | ------ | ----- | -------------- |
| C-01 | Part passes: the tree is a git repository. Fails: no host, thus no protected branch. The one commit has an author address of a test domain and no signature (`git log`). | Step 1. A rule for `main`: no forced push, no deletion, changes only through a pull request. | none in the tree | Creates the repository, sets the rule. Decides on signed commits and on the identity of the first commit. |
| C-02 | Fails: no setting can be read; no pipeline job exists that could state its permissions. | Step 1 and 3. Each workflow states its permissions, with read-only as the default and the write permission on the one job that needs it. | `.github/workflows/*.yml` (new) | Second factor on the account; the default permission of the workflow token in the settings; the same for the accounts at OBS, COPR, Cachix, Codecov and the Alpine GitLab. |
| C-03 | Fails: no protected branch. With one maintainer, no different person exists. `CONTRIBUTING.md` (Rules for changes) describes an AI reviewer that approves the pull requests of the owner. | Step 1. A pull request and passed checks for each change. The check stays failed; the selection records why. If the AI reviewer is kept, its approval must not be the only gate, and it is examined under C-15. | `CONTRIBUTING.md` | Decides if a second maintainer is looked for. |
| C-04 | Part passes: a search of the tracked files for patterns of keys and tokens found nothing. Limits: no secret scanner is installed, and the history is one commit. One token is in a badge address (`README.md` line 5, `CONTRIBUTING.md` line 129, parameter `token` of the Codecov graph). Fails: no scan in a pipeline. | Step 2. A secret scan as a hook and as a job. A table of the credentials: name, holder job, reach, life time. Where the platform gives a short-lived identity token, use it in place of a stored secret. | pre-commit configuration (new), `.github/workflows/*.yml` (new), `docs/releases.md` (new) | Confirms that the Codecov token is the public one for graphs. Turns on the secret scan and the push protection of the host. Creates each secret. |
| C-05 | Fails: no pipeline definition in the tree. | Step 3 and 5. | `.github/workflows/*.yml` (new) | Turns the pipeline on. |
| C-06 | Fails: no build makes provenance. `README.md` (NixOS, last paragraph) and `CHANGELOG.md` (0.4.0, 0.5.0) say that releases had attestations; no file of the tree makes them. | Step 5. The release job makes signed provenance for the source archive and for each package that the pipeline builds, with the attestation capability of the platform. | release workflow (new) | none |
| C-07 | Fails: not verifiable without a platform. | Step 6. The build runs in a workflow that is used again, so that the signing identity belongs to the platform and to that workflow, not to a step of the calling job. The implementation reads at the time of use which arrangement the platform states for L3. | release workflow, one reusable workflow (new) | none |
| C-08 | Fails: no pipeline. | Step 3 and 5. Jobs: build, test, package, publish. Only the publish job has the publication credentials, and it runs no code of the tree but the upload. The jobs that push to aports and to the Nix cache are each their own job with their own credential. | `.github/workflows/*.yml` (new) | A protected environment for the publish job, with the owner as the approver. |
| C-09 | Part passes: the list of components exists (`Cargo.lock`, `flake.lock`, `*/THIRD-PARTY-NOTICES.txt`), and `flake.nix` has an output `sboms` in the CycloneDX format. Fails: no release job makes a bill of materials. | Step 5. The release job makes an SBOM for the source archive and for each package, and attaches it to the release. | release workflow (new) | none |
| C-10 | Part passes: `Cargo.lock` has a checksum for each crate that is not of the tree; `flake.lock` has a revision and a hash for each input; each `FROM` in `dev/containers/*.Dockerfile` has a digest. Fails: `fuzz/` has no lock file (`.gitignore`, `CONTRIBUTING.md` Fuzzing); `packaging/arch/PKGBUILD` key `sha256sums` skips the check; `packaging/alpine/APKBUILD` has no checksum line; no pipeline file exists. | Step 4. Pin each pipeline component by the digest of a commit. Decide for `fuzz/`: commit a lock file, or record why not. For the Arch and Alpine recipes: let the release job write the checksum of the release archive, or record that OBS and aports do it. | `.github/workflows/*.yml`, `fuzz/`, `packaging/arch/PKGBUILD`, `packaging/alpine/APKBUILD`, release tool configuration | Decides the two cases. |
| C-11 | Fails: no scan and no stated time in the tree. | Step 4. A scan of the crates, the Nix inputs, the container images and the pipeline components, on each change and on a schedule, with a public vulnerability data service. The time limits of the selection go into `SECURITY.md`. | scan workflow (new), `SECURITY.md` (new) | Sets the time limits. Turns on the alerts of the host. |
| C-12 | Fails: `SECURITY.md` is not in the tree; `README.md` and `CONTRIBUTING.md` link to it. | Step 7, first. A security policy with the private reporting of the host as the contact, the supported versions, and the time limits. | `SECURITY.md` (new) | Turns on private vulnerability reporting. Publishes advisories. |
| C-13 | Fails: no threat model. Only `keyboard-state/README.md` has a section on safety. | Step 7. One document: the assets (root service, udev helpers, BPF program, extensions, release path), the trust boundaries (sysfs, `/dev/kmsg`, the configuration file, the HID device, the pipeline), the threats and the security requirements. The fuzz targets and the hardening of the unit are linked as the answers. | `docs/threat-model.md` (new) | Reviews it: the owner knows the design. |
| C-14 | Fails: no pipeline. The tree has the means: `Cargo.toml` (keys `workspace.lints`), `keyboard-bpf/.clang-tidy`, `fuzz/`, the option `unit_checks` in `meson.options`. | Step 3. A static analysis job and a security test job (seeds of the fuzz targets, check of the unit), with a stated severity that fails the run. | `.github/workflows/*.yml` (new) | Turns on code scanning of the host, if wanted. |
| C-15 | Fails: no pipeline. The documents describe three events with risk: a reviewer that reads each pull request, a nightly fuzz job that writes advisories, and an update tool. | Step 2 and 3. The workflow for pull requests has no secret and no write permission. No workflow that has a secret checks out or runs the code of a pull request. No step puts a title, a branch name or other outside text into a command. The AI reviewer is added only if it can keep these rules; else it is left out and the owner is told. | `.github/workflows/*.yml` (new) | Sets that workflows of new contributors need an approval. |
| C-16 | Fails: no record of the platform settings. | Step 1. A list of the settings that the project depends on, in the document for releases, so that a change of a setting can be seen. Hosted runners only. | `docs/releases.md` (new) | Reads and sets the settings; keeps the audit log as far as the plan of the account gives one. |
| C-17 | Fails: `README.md` links to `docs/releases.md#check-a-released-file`, which is not in the tree. `packaging/arch/PKGBUILD` does not check the archive. | Step 5. Instructions for users to verify the provenance of a released file against the repository and the workflow. A job after the release that does the same verification and fails if it does not pass. | `docs/releases.md` (new), release workflow | none |
| C-18 | Part passes: a search found no cryptographic primitive in the code and no cryptography crate in `Cargo.lock`. The unit of the guard has hardening settings (`tcc-guard/systemd/asus-ux8406-tcc-guard.service.in`). Fails: the project has no hardening guide to pass, and the check of the unit is off by default (`meson.options`, option `unit_checks`). | Step 7. A short section that states the secure defaults (the unit, the limits of the configuration, `unsafe_code` in `Cargo.toml`), and the unit check as a job of step 3. | `docs/threat-model.md` or `tcc-guard/README.md`, `.github/workflows/*.yml` | none |
| C-20 | Fails: the rule is one line (`CONTRIBUTING.md`, Rules for changes, "established crates") and the accepted licences (`about.toml` key `accepted`). No record for each dependency. | Step 4. Written criteria (maintained, licence, number of users, no build script that fetches), and the rule that the pull request that adds a dependency gives the examination. | `CONTRIBUTING.md` | none |
| C-21 | Part passes: the means exist (`meson.options` option `offline`, `build-aux/dist-vendor.sh`, `packaging/obs/README.md` on builds without network). Fails: no second build was compared, and no build was run without network in this session. | Step 6. A job that builds the packages from the release archive without network access. A second job that builds the archive twice and compares the digests; if they differ, the cause is recorded. | release workflow | none |
| C-22 | Fails: no recorded result. `README.md` shows badges of two scales; the agent did not read their values. | Step 8. After the repository is public: run the program of the score of the security checks, and record the result with its date. | `.agents/kit/devsecops.md` | Makes the repository public; answers the criteria of the badge. |
| C-23 | Fails: not verifiable without a host. | Step 5. Releases that cannot be changed after the publication, a tag rule, and a stated time for the records of the build. | `docs/releases.md` | Sets the release and tag rules. |

## View: operations

| Item | What the check found | Change | Files | Only the owner |
| ---- | -------------------- | ------ | ----- | -------------- |
| C-24 | Fails: no pipeline. The design is right for it: OBS takes the released archive by its address (`packaging/obs/_service`, `packaging/rpm/*.spec` key `Source0`). | Step 5. The publication is a pipeline job. The archive is built one time; each later job and each outside builder takes that file, and its digest is compared. | release workflow, `.obs/workflows.yml` (new), Packit configuration (new) | The accounts and tokens at OBS, COPR, Cachix; the webhook of `packaging/obs/README.md`. |
| C-25 | Fails: the release document is not in the tree; no rollback step is recorded. | Step 5 and 7. A procedure to withdraw a release and to give the earlier version again, run one time in a test with a pre-release. | `docs/releases.md` (new) | Runs the test: it needs the accounts. |
| C-33 | Fails: no pipeline. | Step 3. Each step names a maintained component with its pin. Where the tree uses a few lines of shell in its place, the workflow says why. | `.github/workflows/*.yml` (new) | The allow-list of components in the settings. |
| C-34 | Fails: `docs/releases.md` is not in the tree. | Step 7. The document names the maintainer, where support is given (the issues), and which tasks of a release are automated. | `docs/releases.md` (new) | none |
| C-35 | Fails: no list. `REUSE.toml` and `meson dist` (committed files only) are a base. | Step 7. A list of the configuration items of a release (archive, packages, SBOMs, provenance, recipes), and a release job that compares the list with the content of the release. | `docs/releases.md`, release workflow | none |
| C-32 | Part passes: one version for the tree (`Cargo.toml` key `workspace.package.version`, the recipes agree) and `CHANGELOG.md` with a link to the commit of each change. Fails: the repository has no tag and no release; the notes have no place for corrected vulnerabilities. | Step 5. The release tool makes the tag and the notes from the pull request titles; a security correction names its advisory. | release tool configuration (new), `docs/releases.md` | none |

## View: quality

| Item | What the check found | Change | Files | Only the owner |
| ---- | -------------------- | ------ | ----- | -------------- |
| C-37 | Fails: no protected branch and no pipeline. The suite exists: `meson test` ran 12 of 12 tests with success in this session. | Step 3. The test job as a required check of `main`. | `.github/workflows/*.yml` (new) | Sets the required checks. |
| C-38 | Fails: no test plan names the levels and the characteristics. The levels exist in the tree (`*/tests/unit`, `*/tests/cli`, `tcc-guard/tests/scenarios`, `fuzz/`, the package tests, the container builds), and each part README has a section "Test". | Step 7. One table: test level, part, characteristic, command. The rule "a change of function adds a test" in the rules for changes. | `CONTRIBUTING.md` | none |
| C-40 | Part passes: the standards are configured (`Cargo.toml` keys `workspace.lints`, `biome.json`, `keyboard-bpf/.clang-format`, `.clang-tidy`, `_typos.toml`, `.markdownlint-cli2.yaml`). Fails: the pre-commit configuration that `CONTRIBUTING.md` names is not in the tree, and no pipeline makes a new warning fail. | Step 3. The pre-commit configuration, and a lint job that treats a warning as an error. | pre-commit configuration (new), `.github/workflows/*.yml` | none |
| C-42 | Fails: no quality plan. | Step 7. One table that maps each gate of the pipeline to its entry: review, tests, lints, coverage, container builds, release checks. | `CONTRIBUTING.md` or `docs/quality.md` (new) | none |
| C-43 | Fails: the tracker is named (`CONTRIBUTING.md`) but does not exist for this repository. One issue form exists, for hardware reports. | Step 1. A form for a defect, and labels for the class. | `.github/ISSUE_TEMPLATE/` | Creates the labels. |
| C-45 | Fails: the documents for use, installation and contribution exist, but two linked documents are not in the tree (`SECURITY.md`, `docs/releases.md`). | Step 7. Write the two documents; a link check as a hook. | `SECURITY.md`, `docs/releases.md` (new) | none |
| C-52 | Fails: no record of a review. | Step 8. The owner reviews the selection at a stated interval (proposed: each six months) and writes the date, the measured targets and the decided changes into it. | `.agents/kit/devsecops.md` | Does the review. |
| C-39 | Fails: no pipeline reports the measures. `CONTRIBUTING.md` (Coverage) gives the command and the limit for the guard; the agent did not measure the coverage. | Step 3. A coverage job that shows the values in the summary of the run and keeps the limit of the guard. An outside coverage service only with a credential that the job for pull requests of forks does not get. | `.github/workflows/*.yml` (new) | The account of the coverage service. |
| C-41 | Fails: the requirements are in different places (coverage of the guard and the limit of the unit check in `CONTRIBUTING.md`, the compiler version in `Cargo.toml`). | Step 7. One list of the quality requirements with a measure and an acceptance criterion for each: reliability of the guard, security of the root programs, portability to the distributions of the compatibility table, installability. | `docs/quality.md` (new) | Confirms the criteria. |
| C-47 | Fails: each part README tells how the part operates, but no document describes the whole with the decisions and their reasons. | Step 7. A short description of the architecture: the parts, their privileges, their interfaces to the kernel and the desktop, and the decisions (Rust for the programs, a BPF program in place of a kernel driver, one archive with the crates). | `docs/architecture.md` (new) | Gives the reasons that the tree does not show. |
| C-51 | Fails: `CONTRIBUTING.md` names an update tool, but no configuration is in the tree, and no rule is stated. | Step 4. The configuration of the update tool for the crates, the Nix inputs, the image digests and the pipeline components, and the rule (proposed: updates proposed each week, security updates at once). | update tool configuration (new), `CONTRIBUTING.md` | Installs the application of the update tool. |

Passed, no step: C-26 (the build environments come from
`dev/containers/*.Dockerfile`, `dev/containers/compose.yaml`, `flake.nix` and
the project definition in `packaging/obs/README.md`; the agent read the files
and did not run the containers) and C-44 (`meson setup` and `meson test` with
the commands of `CONTRIBUTING.md` built the tree and passed; the computer was
not a clean one and had network access).

## Measured targets

| Target | Now | Level that the plan reaches | What stops the next level |
| ------ | --- | --------------------------- | ------------------------- |
| `build level` | L0: no release comes from a build in this repository. | L2 with step 5, then L3 with step 6. | Past L3: the packages that users install are built again by OBS and COPR from the archive. Their provenance is that of those services, not of this pipeline. Only the archive, the Nix packages and the packages that the pipeline builds itself can carry the L3 claim. |
| `source level` | The first level: version control only. | The level that protected history and a rule for `main` give, with step 1. | The level with review by two persons: one maintainer. The summary attestation of the source control system: the implementation must find out if the host issues one. |
| `baseline level of an open project` | Not attested. | Level 1 (for each project), after steps 1, 2, 4 and 7. | Level 2 is for a project with two or more maintainers. |
| `score of the security checks` | Not measured: no remote, and the program is not installed. | A first recorded value in step 8. | The checks on review by a second person and on the number of contributors, with one maintainer. |
| `badge of best practices` | `README.md` shows a badge; its level was not read. | Passing. | The owner answers the criteria. The agent did not read the criteria of silver. |
| `maturity of the security practices` | Not assessed. | Not planned: proposed is one scale for C-22, the score of the security checks. | A decision of the owner. |
| `software delivery performance` | Not measured. `CHANGELOG.md` gives the dates of the releases. | Not planned for a project of one person. | A decision of the owner. |
| `test coverage` | Not measured in this session. The rule for the guard is in `CONTRIBUTING.md` (Coverage). | The values of each part in each run, with step 3. | A fixed value for the other parts is a decision of the owner; the proposal is none. |

## Not verified

- Any setting of GitHub, OBS, COPR, Cachix, Codecov or the Alpine GitLab.
- If a public repository of this project exists now, and what it holds. The
  agent made no request to the addresses in the documents.
- The values behind the badges of `README.md`.
- The container builds, the coverage, the fuzz targets, a build without
  network, a second build for comparison.
- The secret search used patterns, not a secret scanner.
- The regulation. The licences of the dependencies.
- The state of each pipeline component. No component is named here for that
  reason.
