# Plan: DevSecOps

Date: 2026-10-13. Selection: `.agents/kit/devsecops.md`. State: **not accepted.
Nothing of this plan is applied.** The selection is a proposal, thus the plan is
a plan for the proposed selection. After the owner accepts it, it is applied on
a new branch and given to the owner as a diff.

## The main finding

The documents of the tree describe a pipeline that the tree does not have.

| The documents name                                                                   | Where                                                        | In the tree |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------ | ----------- |
| `.github/workflows/` with `ci.yml`, `coverage.yml`, `fuzz.yml`, `review.yml`, `release-nix.yml` | `CONTRIBUTING.md`, `flake.nix`                               | absent      |
| `SECURITY.md`                                                                        | `README.md`, `CONTRIBUTING.md`                               | absent      |
| `docs/releases.md` (release steps, check of a released file)                         | `README.md`, `CONTRIBUTING.md`, `packaging/obs/README.md`, `flake.nix` | absent; `docs/` is empty |
| the pre-commit hooks                                                                 | `CONTRIBUTING.md`                                            | no `.pre-commit-config.yaml` |
| `.obs/workflows.yml`                                                                 | `packaging/obs/README.md`                                    | absent      |
| the Packit configuration                                                             | `README.md`, `CHANGELOG.md`, `.gitignore`                    | absent      |
| Renovate, Release Please                                                             | `CONTRIBUTING.md`, `CHANGELOG.md`                            | no configuration |

The checks judge the tree, not the documents. Thus most checks fail. If the
owner has these files in a different place, the change of many items below is
"put the file back and examine it", not "write it". This is the first question
for the owner.

The repository has one commit, no tag and no remote. Thus each check that reads
the settings of the repository, the tracker, the releases or the history could
not run.

## Distance

42 items are adopted (proposed). Of them:

- 37 fail: C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-09, C-10, C-11, C-12,
  C-13, C-14, C-15, C-16, C-17, C-18, C-19, C-20, C-21, C-22, C-25, C-26, C-29,
  C-30, C-31, C-32, C-33, C-34, C-37, C-38, C-39, C-40, C-41, C-43, C-45, C-46.
  Six of them fail in part only: C-07, C-10, C-13, C-17, C-31, C-45.
- 4 could not be examined: C-08, C-35, C-36, C-42.
- 1 passes on judgement, with a limit: C-44.

## What was examined, and how

- Read in this session: `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`,
  `Cargo.toml`, `meson.build`, `meson.options`, `flake.nix`, `flake.lock`,
  `fuzz/Cargo.toml`, `.gitignore`, `.dockerignore`, `REUSE.toml`, `about.toml`,
  `build-aux/dist-vendor.sh`, `packaging/obs/README.md`, `packaging/obs/_service`,
  `dev/containers/compose.yaml`, `tcc-guard/systemd/asus-ux8406-tcc-guard.service.in`.
- Searched, not read in full: the `FROM` lines of `dev/containers/*.Dockerfile`,
  the source and checksum lines of the recipes in `packaging/`, the `source`
  and `checksum` lines of `Cargo.lock`.
- Run: `meson setup` and `meson test` in a directory outside the tree. 12 of 12
  tests passed.
- Secrets: a search of the one commit for the usual patterns of keys and
  tokens. No scan program was on the machine. The search found no secret.
- Not read: the source code, the tests, the READMEs of the parts.

## Security

| Id   | Result of the check                                                                                                                                                                                                                  | Change                                                                                                                                                                                                                             | Files                                                                      | Only the owner can                                                                                 |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| C-01 | Fails. No remote, thus no protected main line. The one commit has the author `experiment@example.invalid` and no signature.                                                                                                          | Protect the main line: no direct push, no forced push, no deletion, a linear history, signed commits. Keep the rules as a file, thus a diff shows a change of them.                                                                | `.github/rulesets/main.json`                                               | Create the repository, load the rules, set the author identity and the signing key.                |
| C-02 | Fails. No rule asks for an approval. `CONTRIBUTING.md` describes an automated reviewer that approves the changes of the owner; it is not a second person.                                                                            | Require one approval that is not from the author, and name the code owners. Until a second maintainer exists, record each change of the owner as "no second person" and keep the automated review and the pipeline as required.    | `.github/CODEOWNERS`, `.github/rulesets/main.json`, `CONTRIBUTING.md`      | Decide the number of reviewers. Find a second maintainer.                                          |
| C-03 | Fails. No build definition is in the tree.                                                                                                                                                                                           | A release workflow on the hosted platform that builds the source archive with `meson dist` and starts the package builds from it. No release from the computer of a person.                                                        | `.github/workflows/release.yml`, `.packit.yaml`, `.obs/workflows.yml`      | Enable the pipeline. Connect COPR, OBS and the cache.                                              |
| C-04 | Fails. `CHANGELOG.md` and `README.md` name attestations; no definition makes them.                                                                                                                                                   | The attestation function of the build platform makes a signed provenance record for the source archive, for each package that the pipeline builds and for each bill of materials. The record goes on the release.                 | `.github/workflows/release.yml`                                            | —                                                                                                  |
| C-05 | Fails. No build platform is configured, thus no documentation applies.                                                                                                                                                               | Hosted runners that are new for each build. For Build L3: the build is one workflow that is used again, and only it gets the permission to attest. Cite the statement of the platform in the release document.                     | `.github/workflows/build.yml`, `docs/releases.md`                          | Judge the isolation of COPR and OBS: they build the packages, and their provenance is not ours.    |
| C-06 | Fails. No pipeline definition.                                                                                                                                                                                                       | Separate jobs for build, test, packaging, attestation and publication. No permission by default; each job declares its minimum. A job that runs the code of a pull request gets no write permission and no secret.                 | `.github/workflows/*.yml`                                                  | —                                                                                                  |
| C-07 | Fails in part. The search of the commit found no secret. `README.md` and `CONTRIBUTING.md` have a token in the URLs of the coverage badges. No pipeline definition and no logs exist.                                                | Secrets only from the secret store, in a protected release environment. Identity tokens with a short life where the target accepts them. A secret scan of the history as a step.                                                   | `.github/workflows/*.yml`, `README.md`, `CONTRIBUTING.md`                  | Confirm that the badge token gives read access to the graphs only. Create and store each secret.   |
| C-09 | Fails. `flake.nix` has an output `sboms` for the Nix packages. Nothing makes a bill of materials for a release, and none exists for the other packages.                                                                              | The release makes one machine-readable bill of materials for the source archive with its crates, and one for each Nix package, and puts them on the release with an attestation.                                                   | `.github/workflows/release.yml`, `docs/releases.md`                        | —                                                                                                  |
| C-10 | Fails in part. Passes: `Cargo.lock` has a checksum for each crate of the registry and one source; `flake.lock` has revisions and hashes; each base image has a digest; cargo runs with `--locked`. Fails: `packaging/arch/PKGBUILD` skips the checksum of the archive; `fuzz/` has no lock file and a version range; no update procedure is in the tree. | A configuration of the update program for crates, flake inputs, image digests and pipeline components. Each pipeline component by the full digest of a commit. A checksum, or a check of the attestation, for the archive in the Arch recipe. A lock file for `fuzz/`. | `renovate.json`, `packaging/arch/PKGBUILD`, `fuzz/Cargo.lock`, `.gitignore`, `.github/workflows/*.yml` | Install the update program on the repository.                                                      |
| C-11 | Fails. No scan is in the tree.                                                                                                                                                                                                       | Required steps on each change: a scan of the dependencies against the public data of known vulnerabilities, a licence and source check of the crates, a secret scan, static analysis. A finding above the limit fails the step.    | `.github/workflows/ci.yml`, `deny.toml`                                    | Decide the limit. Make the steps required.                                                         |
| C-12 | Fails. No threat model and no list of security requirements. The comments of the unit file give reasons for single settings.                                                                                                         | A dated document: the assets (root, the thermal offset, sysfs, `/dev/kmsg`, udev events, the keyboard as an input device), the trust borders, the threats, the security requirements, and for each the test or the setting.        | `docs/security.md`                                                         | Judge the content.                                                                                 |
| C-13 | Fails in part. The rules are named: `Cargo.toml` forbids unsafe code and warns for clippy; `keyboard-bpf/.clang-tidy` and `biome.json` exist. No program enforces them: no pipeline, no hook configuration, and the lints are warnings. The default configuration of the guard passes on judgement: the unit has no network, one capability and a closed device policy. | The pipeline runs the lints with warnings as errors, and the check of the unit (`-Dunit_checks=enabled`).                                                                                                                          | `.github/workflows/ci.yml`, `.pre-commit-config.yaml`                      | —                                                                                                  |
| C-14 | Fails. `SECURITY.md` is absent; two documents link to it.                                                                                                                                                                            | A security policy: the private way to report, the time limits, how a correction is disclosed.                                                                                                                                      | `SECURITY.md`                                                              | Decide the time limits. Enable private reports on the platform. Do the triage.                     |
| C-15 | Fails. No support period is published.                                                                                                                                                                                               | State which versions get security updates and until when. State how a user gets an update and verifies it.                                                                                                                         | `SECURITY.md`, `docs/releases.md`                                          | Decide the support period.                                                                         |
| C-16 | Fails. `README.md` has the keys of the package repositories for apt and pacman; the check of a released file is in `docs/releases.md`, which is absent; the Arch recipe skips the checksum.                                          | Write the verification of the source archive and of each package against its provenance. The package builds verify the archive before they use it. The container builds get a test with a wrong archive that must fail.            | `docs/releases.md`, `.github/workflows/release.yml`, `packaging/arch/PKGBUILD`, `packaging/obs/_service` | Hold the keys of the package repositories.                                                         |
| C-17 | Fails in part. Four fuzz targets with seeds are in `fuzz/`. Nothing runs them, and no dated report exists.                                                                                                                           | The seeds on each change, a fuzz run each night, a dated summary of each run, each failure as a private report.                                                                                                                    | `.github/workflows/fuzz.yml`, `.github/workflows/ci.yml`                   | Decide the interval.                                                                               |
| C-18 | Fails. No inventory.                                                                                                                                                                                                                 | An inventory: the build platform, COPR with Packit, OBS, the binary cache, the coverage service, the update program, the automated reviewer; for each an owner, the version or the plan, where its logs are.                       | `docs/governance.md`                                                       | Confirm the list. Examine the accounts.                                                            |
| C-19 | Fails. No record.                                                                                                                                                                                                                    | A selection record for each provider of the inventory and for the sources of the dependencies: what the project needs from it, and how the project examines it.                                                                    | `docs/governance.md`                                                       | Judge each provider.                                                                               |

Could not be examined: C-08. It needs the access list of the repository, of
COPR, of OBS and of the cache. The change: multi-factor authentication on each
account, tokens with the minimum scope and an end date (`packaging/obs/README.md`
asks for a fine-grained token already), and a dated review of the list in
`docs/governance.md`. Only the owner can do it.

Passes on judgement: C-44, from the unit file only. The guard has no network,
keeps its notes in a directory with mode 0700 and writes to the journal. The
names of the tests show refusals of paths outside `/sys`. The limit: the source
code was not read, and no dated security test exists (C-17).

## Operations

| Id   | Result of the check                                                                                                                                                                     | Change                                                                                                                                                                                                                  | Files                                                                    | Only the owner can                                               |
| ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| C-20 | Fails. Only `packaging/obs/_service` is in the tree. The trigger of OBS, the configuration of Packit and the release workflow are absent. `packaging/obs/README.md` has manual steps for the setup. | The publication to each package repository starts from the release, without a manual command. The definitions are in the repository.                                                                                    | `.github/workflows/release.yml`, `.packit.yaml`, `.obs/workflows.yml`    | Do the setup of OBS and COPR one time.                           |
| C-21 | Fails. No rollout in steps, no rollback procedure, no rehearsal.                                                                                                                        | Step 1: a release candidate that the container builds install. Step 2: the release, after a test on the hardware. Rollback: publish the last good version again as a new version; write how a user goes back. Rehearse it one time and give the date. | `docs/releases.md`, `.github/workflows/release.yml`                      | Do the test on the hardware and the rehearsal.                   |
| C-22 | Fails. No environments are defined.                                                                                                                                                     | A protected release environment holds the credentials of the publication. The jobs of a pull request cannot reach it.                                                                                                   | `.github/workflows/*.yml`, `docs/releases.md`                            | Create the environment and its rule.                             |
| C-25 | Fails. No plan.                                                                                                                                                                         | A short plan: a bad release, a stolen account or key, a vulnerability that is used. Who acts, how a package is withdrawn, how users are told, and a review without blame after it. One dated exercise.                   | `SECURITY.md`, `docs/releases.md`                                        | Take the role. Do the exercise.                                  |
| C-26 | Fails. `CHANGELOG.md` links each release to its commits; no record links a publication to its tests and its approval.                                                                   | The release record names the commit, the pipeline run that passed and the approval. The decision "review and passed pipeline are the approval" is written.                                                              | `docs/releases.md`, `.github/workflows/release.yml`                      | Decide the way of the approval.                                  |
| C-29 | Fails. No readiness checklist.                                                                                                                                                          | A checklist for a new package or a new distribution: recipe lint, install and removal in a container, the row in the compatibility table, the way back. Dated at each use.                                              | `docs/releases.md`                                                       | Judge the content.                                               |
| C-45 | Fails in part. The version is in `Cargo.toml`, `meson.build` and the recipes; the lock files record the inputs; `meson dist` uses the committed files. The repository has no tag, thus no build from a tag could run. | Each release has a signed tag. The pipeline builds the archive from the tag a second time and compares it.                                                                                                              | `.github/workflows/release.yml`, `docs/releases.md`                      | Push the tags of the former releases, if they exist.             |
| C-46 | Fails. No store and no digest to compare.                                                                                                                                               | The source archive is built one time and kept on the release, which cannot be changed after the publication. Each package build takes this archive and examines its digest. State that the packages of the distributions are built from it by their own builders. | `.github/workflows/release.yml`, `docs/releases.md`, `packaging/`        | Switch on releases that cannot be changed.                       |

## Quality

| Id   | Result of the check                                                                                                                                                                              | Change                                                                                                                                                                              | Files                                                  | Only the owner can                             |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------- |
| C-30 | Fails. No pipeline runs on a change.                                                                                                                                                             | A workflow for each pull request and each push to the main line: build, tests, lints, scans. Its success is required before a merge.                                                | `.github/workflows/ci.yml`, `.github/rulesets/main.json` | Make the checks required.                      |
| C-31 | Fails in part. The suites exist: unit, command line and scenario tests for the Rust programs, tests of the extensions, checks of the BPF object, and install tests in containers. `meson test` passed 12 of 12 here. They run in no pipeline, and the history has no sample of changes. | Run `meson test` and the container builds in the pipeline.                                                                                                                          | `.github/workflows/ci.yml`                             | —                                              |
| C-32 | Fails. The configurations of the tools exist (`.clang-format`, `.clang-tidy`, `biome.json`, `_typos.toml`, `.markdownlint-cli2.yaml`); the hook configuration and the pipeline do not.            | The hook configuration, and a required step that runs it.                                                                                                                           | `.pre-commit-config.yaml`, `.github/workflows/ci.yml`  | —                                              |
| C-33 | Fails. Some limits are written in single places: 100 % of the regions of the guard, an exposure of the unit of at most 1.3, the oldest Rust version. No list for each quality characteristic.     | One list: the characteristic, the measure, the limit, the test that examines it.                                                                                                    | `docs/quality.md`                                      | Agree the limits.                              |
| C-34 | Fails. `CONTRIBUTING.md` has parts of it; no plan names the activities and who does them.                                                                                                        | A quality plan: tests, review, hardware test, fuzzing, container builds; who does each; what is independent of the author.                                                          | `docs/quality.md`                                      | Judge the content.                             |
| C-37 | Fails. The documents are with the code, but two documents that other files link to are absent, and `CONTRIBUTING.md` describes workflows that the tree does not have.                            | Write the two documents (C-14, C-16). A link check as a hook.                                                                                                                       | `SECURITY.md`, `docs/releases.md`, `.pre-commit-config.yaml` | —                                              |
| C-38 | Fails. No record of requirements or of decisions.                                                                                                                                                | A short decision record for each design decision from now on, with the test that examines it. The list of C-33 links each requirement to its test.                                  | `docs/decisions/`, `docs/quality.md`                   | Write the decisions that are made already.     |
| C-39 | Fails. No record.                                                                                                                                                                                | A dated note for each role: what the role must know, and how the maintainer got it.                                                                                                 | `docs/governance.md`                                   | Give the facts.                                |
| C-40 | Fails. No document names the owner of a duty.                                                                                                                                                    | A table: security, operations, quality, releases, each account; the owner of each; who acts when the maintainer is absent.                                                          | `docs/governance.md`, `.github/CODEOWNERS`             | Take or give each role.                        |
| C-41 | Fails. No register.                                                                                                                                                                              | A register: each regulation of the selection, if it binds, who decided this and when, the duties, the place of the evidence. The licence duties (`REUSE.toml`, the notices) are in it too. | `docs/governance.md`                                   | Decide if each regulation binds.               |
| C-43 | Fails. No maintenance statement.                                                                                                                                                                 | A statement: who maintains the packages, until when, and what ends a part (for example the fix in the kernel).                                                                      | `README.md` or `SECURITY.md`                           | Decide the end date.                           |

Could not be examined:

- C-35: the tracker is not in the tree, and the tree has no dated record of a
  change of the process.
- C-36: the history is one commit.
- C-42: judgement, and the tracker is not in the tree.

## Decisions for the owner

1. Are the absent files (table above) in a different place?
2. Does a regulation bind the project? Which of the four does the project
   prepare for?
3. The four answers and the four target levels of the risk analysis.
4. The three declined items of the operations view (C-23, C-24, C-27) and
   their reasons.
5. The ten decisions by context in the selection. The skill stops for five of
   them: the target level of the build integrity scale, the number of
   reviewers, the approval of a change to production, the time limits, the
   decline of an item.

## Measured targets

Nothing was measured: the tree has no pipeline, no release and no remote. The
levels are what the plan reaches.

| Target                                | Now                                                                 | The plan reaches                                   | What stops the next level                                                                                                                             |
| ------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| SLSA build track                      | Build L0 in this tree: no provenance.                               | Build L2 for the source archive, then Build L3.    | L3 needs the build in a workflow that is used again, isolated from the caller. The packages from COPR and OBS have no provenance of this project.     |
| SLSA source track                     | Source L1: version control.                                         | Source L3: technical controls on the main line.    | Source L4 needs two trusted persons for each change. The project has one maintainer.                                                                  |
| Software delivery metrics             | Not computed: no data of a pipeline.                                | Not in the plan (C-28 is above the target).        | Data of the pipeline for a period.                                                                                                                    |
| Repository practice score             | Not measured: no remote, and the program was not on the machine. `README.md` has the badge. | A measurement in the pipeline each week.           | The review check needs a second person.                                                                                                               |
| Security baseline of an open project  | No self-assessment.                                                 | A self-assessment of the first level, with a date. | The second level asks for documents and controls that the plan makes only in part; assess after the plan is applied.                                  |
| Maturity of software assurance        | No self-assessment.                                                 | None.                                              | A self-assessment of 15 practices is much work for one maintainer; the owner decides.                                                                 |

## Order of the application

1. Source: C-01, C-02, C-08.
2. Feedback on each change: C-30, C-31, C-32, C-13, C-11, C-17.
3. Build: C-03, C-06, C-07, C-04, then C-05.
4. Dependencies: C-10, C-09.
5. Release and publication: C-45, C-46, C-16, C-20, C-22, C-21, C-26, C-29.
6. Vulnerabilities and incidents: C-14, C-15, C-25, C-12.
7. Governance: C-40, C-41, C-18, C-19, C-39, C-43, C-33, C-34, C-37, C-38.

## Capabilities without an implementation skill

No implementation skill is installed. The plan names the capability, and the
work is done with the tools of the project:

- a pipeline with separate jobs, minimum permissions, pinned components,
  workflows that are used again, and the attestation of artifacts;
- the measurement of the repository practices;
- the known vulnerabilities of the dependencies from a public data service;
- the verification of provenance;
- the signature of release artifacts and its verification.

## Not verified

- Each setting of a repository, a tracker, a release, a package repository or
  an account. The project has no remote.
- What the documents say about the pipeline, the attestations, the coverage
  and the nightly runs.
- The source code and the tests were not read. The secret search was a search
  for patterns, not a scan program.
- The questions of law in the selection.
- The two levels of the measured targets that depend on the platform were read
  from the pages of their issuers in this session: the names of the levels of
  the source track, and the statement that an attestation of the platform gives
  Build L2 and a workflow that is used again gives the isolation for Build L3.
  The levels of the last two targets are from the skill only.
