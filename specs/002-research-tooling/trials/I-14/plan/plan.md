# Plan: DevSecOps

**Status: PROPOSED, not accepted, not applied. It rests on the proposed
[selection](devsecops.md). No file of the project was changed but the selection
and this plan.**

- Written: 2026-10-11, against commit `ec6e8ce` of `main`.
- No implementation skill is installed. Thus the plan names each capability and
  the files that a change touches. It writes no setting of a platform.
- The project has no remote. Nothing was pushed.

## The main finding

The documents of the tree describe a pipeline, a security policy and a release
procedure. The files are not in the repository:

| The documents name | Named in | In the tree |
|---|---|---|
| `.github/workflows/` with `ci.yml`, `coverage.yml`, `fuzz.yml`, `review.yml`, `release-nix.yml`, and a release workflow | `CONTRIBUTING.md` (Coverage, Fuzzing, Rules for changes), `flake.nix`, `packaging/obs/README.md` | not there; `.github/` holds only `ISSUE_TEMPLATE/` |
| `SECURITY.md` | `README.md` (Where to start), `CONTRIBUTING.md` (first table) | not there |
| `docs/releases.md` | `README.md`, `CONTRIBUTING.md`, `packaging/obs/README.md`, `flake.nix` | not there; `docs/` is empty and not tracked |
| a configuration of pre-commit | `CONTRIBUTING.md` (Build and test) | not there |
| a configuration of Renovate | each file of `dev/containers/*.Dockerfile`, `CONTRIBUTING.md` | not there |
| `.obs/workflows.yml` | `packaging/obs/README.md` (Release) | not there |
| a configuration of the release tool and of the COPR builds | `CHANGELOG.md` (entries of 0.1.2 and 0.1.3) | not there |

Of the 19 failed checks, 13 have this one cause (C-01, C-05, C-06, C-07, C-08,
C-09, C-11, C-12, C-24, C-35, C-41, C-43, C-62), 5 have it in part (C-10, C-14,
C-22, C-25, C-29), and 1 does not (C-37). **Only the owner can say if
these files exist in a different place.** Proposed answer: they exist, and the
first step of the work is to bring them into this repository, not to write them
again. The plan below says "bring in or write" for each one. If the owner brings
them in, the checks must run again, because the result of each item below can
change.

## Order

The order of the recipe, applied to the failed items:

1. Owner: decide the selection and the question of the main finding.
2. Protect the repository when it is made on GitHub (C-02, C-21, C-22, C-35).
3. Pipeline for each change: build and tests (C-01, C-05, C-41).
4. Separate jobs and their permissions, before a release job gets a right to
   sign (C-07, C-23).
5. Release on the hosted platform with signed provenance, and the verification
   by the user (C-06, C-08, C-10, C-11, C-12).
6. Analyses and the policy for findings (C-14, C-24, C-25, C-29, C-43).
7. Complete the release: procedure and governance (C-62, C-37).
8. Not applicable: no operated service.
9. Isolated builds (C-09).
10. Measure again and write the distance into the selection.

## Changes by view

### Pipeline

| Item | Evidence of the failure | Change | Files | Only the owner can |
|---|---|---|---|---|
| C-01 | The build definition is in the tree (`meson.build`, `Cargo.toml`). No pipeline definition is in the tree. No tag exists, thus no release can be tied to a commit. | Bring in or write the pipeline definition. Capability: setup of the pipeline platform. | `.github/workflows/*`, `.obs/workflows.yml`, the configurations of the release tool and of the COPR builds | say where the files are; make the tags of the releases that `CHANGELOG.md` lists available in this repository |
| C-05 | No pipeline definition; no run exists. | A workflow that starts on each change of the primary branch and on each pull request, and runs the command of C-04. | `.github/workflows/` | — |
| C-07 | No pipeline definition. | Build, test and packaging as separate jobs. Each job states its permissions; the build job and the test job get no secret. The secrets that the documents imply (the two build services, the binary cache, the coverage service, the Alpine fork, the AI reviewer) go only to the job that uses each one. | `.github/workflows/` | make the secrets and bind each one to an environment of the release |
| C-06 | No pipeline definition; no release artifact is reachable. | The release job makes the source archive with the command that `CONTRIBUTING.md` gives (Notices and source archive). | `.github/workflows/` | — |
| C-12 | No pipeline definition. | The release job gives out the archive that the test job tested: one build, and the digest of the tested archive is compared before the upload. The packages of the distributions are built again by their services from that archive; this is outside the check. | `.github/workflows/` | — |
| C-08 | `CHANGELOG.md` (0.5.0, first entry) says that a provenance bundle is put on the release. No definition and no bundle is in the tree. | Capability: signed build provenance that is tied to the source repository, with the attestation function of the platform. | `.github/workflows/` | — |
| C-10 | The version is in `meson.build` (`version`), `Cargo.toml` (`workspace.package.version`) and the recipes; `CHANGELOG.md` exists. No digest file and no signature is reachable. `packaging/arch/PKGBUILD` (`sha256sums`) skips the check of the archive; `packaging/alpine/APKBUILD` has no checksum line. | The release job writes a digest file beside the archive. The release step sets the digest in the two recipes. | `.github/workflows/`, `packaging/arch/PKGBUILD`, `packaging/alpine/APKBUILD` | — |
| C-11 | The installation commands of `README.md` add the signing key of each package repository, thus the package manager verifies the packages. For the source archive, `README.md` (NixOS, last paragraph) refers to a section of `docs/releases.md`, and that file is not there. | Bring in or write the section "Check a released file": one command that verifies the provenance of the archive and fails on a wrong one. | `docs/releases.md` | — |
| C-14 | Pass: `Cargo.lock` and `flake.lock` are in the tree; each base image of `dev/containers/*.Dockerfile` has a digest. Fail: no configuration of an update tool; no pipeline, thus no fixed reference to its tools. `.gitignore` leaves out `fuzz/Cargo.lock` on purpose. | Bring in or write the configuration of the update tool that the Dockerfiles name. Refer to each action of the pipeline by a digest. | configuration of the update tool, `.github/workflows/` | install the update tool on the repository |
| C-09 | No pipeline definition. | After Build L2 works: generate the provenance outside the steps that the project defines. | `.github/workflows/` | choose the component; refer to "Decisions" |

Not measurable, and what makes them measurable:

| Item | What is necessary | Only the owner can |
|---|---|---|
| C-02 | A rule on the primary branch that refuses a direct push, a forced push and a deletion. | set it on GitHub |
| C-03 | A rule that asks for one approval. With one maintainer it cannot hold for a change of the owner. | decide the proposal in the selection |
| C-15 | The record of the platform of who made and who approved each revision. | — (the platform gives it after C-02 and C-03) |

### Security

| Item | Evidence of the failure | Change | Files | Only the owner can |
|---|---|---|---|---|
| C-22 | A search of the one commit for the usual forms of keys and tokens found nothing. This was a search with patterns, not a scanner: none is installed here. One value needs a judgement: the key `token` in the badge URLs of `README.md` (line 5) and `CONTRIBUTING.md` (line 129). No scan runs on a change. | Capability: scan for secrets on each change, and one scan of the full history after the files of the main finding are in. | `.github/workflows/`, configuration of pre-commit | say if the badge token is of a kind that can be public; enable the secret scan with push protection of the platform |
| C-35 | `SECURITY.md` is not there; two documents link to it. | Bring in or write it, with a private contact and the process to answer and disclose. `CONTRIBUTING.md` (Fuzzing) already says that a failing input gets a private draft advisory. | `SECURITY.md` | name the private contact; enable private reporting on GitHub |
| C-25 | No job; no policy. `about.toml` (`accepted`) has the list of accepted licences. | Capability: analysis of dependencies for known vulnerabilities and licences, on each change and on a schedule. Write the policy with the limits that the selection proposes. | `.github/workflows/`, a policy section in `SECURITY.md` or `CONTRIBUTING.md` | decide the limits |
| C-24 | No job. The languages of the product: Rust, C for BPF, JavaScript; Python and shell in the tests and the build. | Capability: static analysis for security, one job for each language; the findings block or are recorded. `keyboard-bpf/.clang-tidy` already has the security groups for the C file. | `.github/workflows/` | enable code scanning on GitHub |
| C-29 | Pass: `Cargo.toml` forbids unsafe code (`workspace.lints.rust`) and sets `overflow-checks` (`profile.release`); `keyboard-bpf/meson.build` builds with `-Werror`; `keyboard-bpf/.clang-tidy` has `WarningsAsErrors`; the rules are in `CONTRIBUTING.md` (Rules for changes). Fail: the Rust lints have the level `warn` (`workspace.lints`), and nothing in the tree makes a warning an error. | The lint job of the pipeline denies warnings. Do not change the level in `Cargo.toml`: the distributions build with other compiler versions. | `.github/workflows/`, configuration of pre-commit | — |
| C-37 | `LICENSE`, `LICENSES/`, `CONTRIBUTING.md` exist. No file gives the roles or the period in which a release gets security corrections. | Add the two statements. | `SECURITY.md` (support period), `CONTRIBUTING.md` (roles) | state the support period |

Not measurable, and what makes them measurable:

| Item | What is necessary | Only the owner can |
|---|---|---|
| C-21 | Multi-factor authentication on each account with write rights; a short list of such accounts, of the tokens and of the deploy keys. | do and review it on GitHub and on the build services |
| C-23 | A pipeline definition to examine. Three points to examine first: the workflow of the AI reviewer, which reads each pull request; the webhook of the build service, which `packaging/obs/README.md` (Setup, step 5) sets for pull requests; each step that puts a title or a branch name of a pull request into a script. | — |
| C-34 | Releases that cannot be changed after the publication. | enable immutable releases on GitHub |
| C-36 | A record in the issue tracker or an advisory for each vulnerability, with the decision and the root cause. | — |

### Quality

| Item | Evidence of the failure | Change | Files | Only the owner can |
|---|---|---|---|---|
| C-41 | No pipeline reports a test that changes its result. One run in this session was correct; one run shows nothing about stability. | The test job reports each test that passes only on a retry. The list is empty or has an owner. | `.github/workflows/` | — |
| C-43 | The configurations exist: `Cargo.toml` (`workspace.lints`), `keyboard-bpf/.clang-tidy`, `keyboard-bpf/.clang-format`, `biome.json`, `_typos.toml`, `.markdownlint-cli2.yaml`. No job runs them, and the configuration of pre-commit that `CONTRIBUTING.md` names is not there. | Bring in or write the configuration of pre-commit; one job runs it on each change. | configuration of pre-commit, `.github/workflows/` | — |

Not measurable, and what makes them measurable:

| Item | What is necessary | Only the owner can |
|---|---|---|
| C-39 | A rule that requires the test job before a merge. | set it on GitHub |
| C-49 | Defects in the issue tracker with their cause; a count for each release. `CHANGELOG.md` already lists the corrections of each release. | — |
| C-50, second part | A history: a change names its tests. | — |
| C-51 | A limit, and a history. | set the limit |

### Operations

| Item | Evidence of the failure | Change | Files | Only the owner can |
|---|---|---|---|---|
| C-62 | `docs/releases.md` is not there; four files link to it. No pipeline definition. | Bring in or write the procedure; the pipeline makes the release from a tag or a decision. | `docs/releases.md`, `.github/workflows/` | — |

Not measurable: C-59 needs records in the issue tracker. Proposed: a label for
a release that harmed the machines of users, with the analysis in the issue.

## What passed, with its evidence

| Item | Evidence |
|---|---|
| C-04 | In this session: a new clone, then the two commands of `CONTRIBUTING.md` (Build and test), without the pre-commit command. The setup ended without an error and all 12 tests were correct. The build took the crates from the network or from the local cache of cargo; the build without network from a source archive was not tried. |
| C-28 | `Cargo.lock`: each of the 115 packages from outside has the same registry as `source` and has a `checksum`. `meson.build` (`cargo_args`) builds with `--locked`. `flake.lock` has a `narHash` for each input. Each `FROM` of `dev/containers/*.Dockerfile` has a digest. |
| C-30 | `tcc-guard/asus-ux8406-tcc-guard.toml.example` gives each setting with its default and the rules for the file. `tcc-guard/systemd/asus-ux8406-tcc-guard.service.in` gives each hardening setting and the reason for the ones that are not set. Judged for the guard only; the other parts have no security setting that was found. |
| C-50 | The tests of each part are in the tree (`*/tests/`, `fuzz/`), and `tcc-guard/README.md` (Test) tells what they examine. The README files of the other parts were not read. |

## Measured targets

| Target | Now | The plan reaches | What stops the next level |
|---|---|---|---|
| `build level` | Build L0, measured: no provenance can be verified from this repository. | Build L2: the hosted platform builds the archive and signs the provenance (C-06, C-08). | Build L3 needs C-09. The component is not chosen, and no implementation skill is installed to examine one. |
| `source level` | Source L1: version control exists. | Source L2, when the repository is on the platform and the history of the primary branch is protected (C-02). | Source L3 needs the signed summary of the platform (C-15); the capability has no implementation skill here. Source L4 needs two reviewers; the project has one maintainer. |
| `baseline level` | Not evaluated. | Level 1 is the aim: C-01, C-02, C-21, C-22 and C-35 are its items in this recipe. | The evaluation is a delegated capability, and no implementation skill is installed. |
| `check scores` | Not measured: a program computes them from a public repository. | Measured after the first push. | — |
| `delivery performance` | Not selected (C-63 is above the target). | — | — |
| `service level` | Not applicable: no service. | — | — |
| `test coverage` | Not measured in this session; the coverage tool is not installed. `CONTRIBUTING.md` (Coverage) states a limit for the guard and none for the other programs. | The pipeline measures it on each change and holds the limit of the guard. | A limit for the other two programs and the extensions is a decision of the owner. |
| `process capability` | Not measured. | No assessment is planned. | An assessment needs an assessor. |

## Not verified

- Each setting of GitHub, of the build services and of the binary cache. No
  remote exists.
- The repository that the URLs of `README.md` name. It was not opened: the user
  said that this project has no remote yet.
- The statements of `CONTRIBUTING.md` and `CHANGELOG.md` about workflows,
  attestations, lists of components and coverage. They are statements about
  files that are not in the tree.
- The secret search was a pattern search over one commit, not a scanner.
- The pre-commit command, the container builds, the fuzz targets and the
  coverage were not run.
- Files not read: the Rust, C and JavaScript sources, the README files of four
  parts, most of `packaging/`.

## Next step

The owner decides the selection: the three target levels first, then the
decisions that depend on context, then the question of the main finding. After
the owner accepts this plan, it is applied on a new branch and given back as a
diff or a pull request.
