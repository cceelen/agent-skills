# Selection: DevSecOps

**Status: PROPOSED. The owner has not decided anything in this file.** The
owner was not in the session of 2026-10-12. Each answer, each target level and
each `[x]` or `declined` below is a proposal of the agent. The owner confirms or
changes each one; then this line and the marks `(proposed)` go away and the date
of the review is written here.

Recipe: skill `devsecops`, trial rendering of the specification branch
`001-devsecops`, commit `f16f5d1`, spec.md sha256
`21198965d11814c9d0ec916516de4836a2a2a55cda3375e42bba981e57fb5228`.

The plan for the items whose check fails is in
[devsecops-plan.md](devsecops-plan.md).

## Contexts (proposed, read from the tree)

| Context                  | Proposed answer                                                                                                                                                                  | Where it is                                                                 |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Kind of project          | Open source system software for one laptop model: three Rust programs (two run as root from udev or systemd), one HID-BPF program for the kernel, two GNOME Shell extensions.    | `README.md`, `Cargo.toml` key `workspace.members`, `CONTRIBUTING.md` Layout |
| Size of the organization | One maintainer. Outside contributors can send pull requests.                                                                                                                     | `README.md` (first person), `packaging/obs/README.md` element `person`      |
| Pipeline platform        | GitHub Actions, stated by the requester of this run. The documents also name OBS, COPR with Packit, Cachix and Codecov. No pipeline definition is in this tree.                  | `CONTRIBUTING.md`, `packaging/obs/README.md`, `flake.nix` key `nixConfig`   |
| Way of delivery          | A GitHub release with a source archive that holds the crates; from it, packages in the repositories of the distributions, and a Nix binary cache.                                | `README.md` Installation, `packaging/obs/_service`                          |
| Harm of a failure        | A fault of the guard: the laptop switches off under load, or the CPU throttles wrongly. An attack on a release: code that runs as root, or in the kernel, on each user's laptop. | `README.md` Disclaimer, `tcc-guard/README.md`                               |
| Outside duty             | None found in the tree. Licences: MIT, and GPL-2.0-only for `keyboard-bpf/`.                                                                                                     | `README.md` Licence, `REUSE.toml`                                           |

Regulation and governance: the checklist names none for any item, and the tree
names none. **Proposed answer: no regulation and no governance bind the
project.** The agent read no regulation. Only the owner, or a person who knows
the duty, can confirm this.

## Risk analysis (proposed)

| Dimension                           | Question                                                                           | Proposed answer                                                                                                                                                                                                               | Proposed target level |
| ----------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| `consumers of the artefact`         | Does a different party install or run the artefact?                                | Yes. Users install the packages from COPR, OBS and the Nix cache; OBS and distributions build from the release archive. They cannot see the build.                                                                            | 2                     |
| `outside code in the pipeline`      | Does the pipeline run code of outside contributors, or components of third parties? | Yes. Pull requests of other contributors and of an update tool, third-party pipeline components, and an AI reviewer that reads each pull request.                                                                             | 2                     |
| `credentials with production reach` | Does a pipeline job hold a credential that can publish a release or change production? | Yes. The documents describe a release workflow that makes the tag and the release, fills the Nix cache and pushes to a fork of aports; a webhook secret starts OBS.                                                         | 2                     |
| `duty by regulation or contract`    | Does a law, a rule of an industry or a contract bind the product?                  | No duty found. Not verified; refer to the paragraph above.                                                                                                                                                                    | 1                     |
| `operated service`                  | Does the team operate the software for users, with a promise on availability?      | No. The project only gives packages. The guard is a service on the user's own machine.                                                                                                                                        | 1                     |
| `harm of a failure`                 | What is the worst result of a fault or of an attack for the users?                 | Fault: loss of unsaved work at a power-off, wrong thermal limit. Attack through a release: root or kernel code on each user's machine. No personal data, no safety function; the user base is the owners of one laptop model. | 2                     |

The opinion of the kit for these answers: do each item of the first three
dimensions, and the items of `credentials with production reach` first, before
the pipeline gets a credential. The items on telemetry and on incidents can
wait, because the project only gives packages. The checklist has no item of
level 3; the proposed targets thus adopt each item of a dimension with the
answer yes.

## Decisions that depend on context (proposed)

| Decision                                      | Proposed option                                                                                                                                                                                                                                                              |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| How many persons approve a change             | One maintainer: no second person exists. Each change enters `main` through a pull request with required checks. The AI reviewer of `CONTRIBUTING.md` is an added signal; it is not the "different person" of C-03. The check of C-03 stays failed and is reported as such. |
| Value of test coverage                        | Keep the rule of `CONTRIBUTING.md`: the guard at 100 % of its regions, enforced. No fixed value for the other parts; the trend is examined.                                                                                                                                 |
| How a pipeline component is pinned            | The full digest of a commit, with the version in a comment. An exact tag only where the component must be referred to by its tag.                                                                                                                                           |
| Build platform                                | The hosted runners of GitHub, with the attestation service of the platform. The implementation must read at the time of use which level the platform states.                                                                                                                |
| How a change to production is approved        | A release is one reviewed pull request (the release pull request); the pipeline is the gate. No change board.                                                                                                                                                              |
| Time to correct a vulnerability               | Critical and high: 14 days. Medium: 60 days. Low: with the next release. The owner sets the numbers; these are a start.                                                                                                                                                     |
| How fast the pipeline gives its result        | Formats and lints in a few minutes; the tests in less than ten minutes. The container builds of the packages can take longer and run as their own jobs.                                                                                                                     |
| Service level objectives                      | None. The project only gives packages.                                                                                                                                                                                                                                       |
| How a release reaches the users               | In one step, with a tested way back: the earlier version stays installable, and the document for releases tells how to withdraw a release.                                                                                                                                  |
| Data service for the known vulnerabilities    | A public service that collects the databases of the ecosystems, because the tree has Rust crates, Nix inputs and container images. The implementation selects the product.                                                                                                  |
| Pipeline components of other parties (P-4)    | Use a maintained component before a new part is written, pinned by digest, from a short allow-list that the repository settings enforce.                                                                                                                                    |

## Selection (proposed)

One line for each item of `references/checklist.md`. In each view, the items of
level 1 are first.

### View: security

Level 1:

- [x] C-01 Each change to the source is in a version control system that keeps the history and the identity of its author. (proposed)
- [x] C-02 Access to the source, the pipeline and the artefacts needs strong authentication and gives the least privilege. (proposed)
- [x] C-03 A second person reviews each change before it enters a protected branch. (proposed; with one maintainer the check cannot pass, refer to the decisions)
- [x] C-04 Secrets are not in the source, in a log or in an artefact, and a pipeline step gets only a short-lived credential for its own task. (proposed)
- [x] C-05 The build runs on a hosted build platform from a definition under version control, not on the computer of a person. (proposed)
- [x] C-06 The build platform makes provenance for each artefact and signs it. (proposed)
- [x] C-07 Each build runs in a new, isolated environment, and the build steps cannot reach the signing material of the provenance. (proposed)
- [x] C-09 The project keeps a machine-readable list of its components and gives a bill of materials with each release. (proposed)
- [x] C-10 Each dependency and each pipeline component is pinned to an exact, verified version. (proposed)
- [x] C-11 Known vulnerabilities in the code and in the dependencies are found by automated scans and corrected within a stated time. (proposed)
- [x] C-12 The project publishes how to report a vulnerability, and it has a process to answer, to correct and to disclose. (proposed)
- [x] C-13 Threats are modelled in the design, and the security requirements are written before the code. (proposed)
- [x] C-14 Static analysis and security tests run automatically on each change. (proposed)
- [x] C-15 The pipeline treats each input and each contribution from outside as untrusted. (proposed)
- [x] C-16 The pipeline platform and its runners are hardened, kept up to date and logged. (proposed)
- [x] C-17 A consumer verifies the provenance and the signature of an artefact against stated expectations before the artefact is used or deployed. (proposed)
- [x] C-18 The product uses published, reviewed cryptography and has secure default settings. (proposed)
- [ ] C-19 The roles and the duties for security are assigned, and the persons who hold them are trained. (declined: proposed reason: one maintainer holds each role, and a training record of one volunteer shows nothing to a user; the owner gives the real reason)
- [x] C-20 Suppliers and third-party components are selected by stated criteria and examined through their life. (proposed)
- [x] C-22 The project measures its security practices on a published scale and records the result. (proposed)
- [x] C-23 Each release and its evidence are archived and protected from change. (proposed)

Level 2:

- [x] C-08 The build, the test and the packaging run as separate steps with separate privileges, and the duties of the persons are separated. (proposed; a constraint of the charter)
- [x] C-21 Where the project can do it, the build is reproducible or hermetic. (proposed)

### View: operations

Level 1:

- [x] C-24 The deployment is automated, and the same artefact goes through each environment. (proposed; "deployment" is here the publication of the release archive and of the packages)
- [x] C-25 Changes are small and reversible, and a tested way back exists for each release. (proposed)
- [x] C-26 The environments and their configuration are made from definitions under version control. (proposed)
- [ ] C-28 Logs, metrics and traces are collected, and each alert goes to a person who can act. (declined: proposed reason: the project operates no service; the programs write to the journal of the user's machine)
- [x] C-33 The pipeline is made of maintained, versioned components that are used again across projects, before a new part is written. (proposed)
- [x] C-34 The operation of the software is planned with its development: owners, support and the work that can be automated. (proposed; in the small form of the document for releases)
- [x] C-35 The configuration items, the baselines and their status are identified, controlled and audited. (proposed)

Level 2:

- [x] C-32 Each release is planned, has a unique version identifier and release notes, and can be traced to its source. (proposed)
- [ ] C-27 The service has stated service level objectives, and measurements show if it meets them. (above the target level)
- [ ] C-29 An incident has a defined response, and each incident gets a review without blame that gives recorded actions. (above the target level)
- [ ] C-30 The operational readiness is examined before a release: procedures, capacity, backup and restore. (above the target level)
- [ ] C-31 Each change to production is recorded, classified by its risk and approved as its class needs. (above the target level)
- [ ] C-36 The maintenance of the software and the end of its support are planned and published. (above the target level)

### View: quality

Level 1:

- [x] C-37 An automated test suite runs on each change, and a failed run stops the change. (proposed)
- [x] C-38 The tests cover each test level and each quality characteristic that matters, and a change of function or a corrected fault adds a test. (proposed)
- [x] C-40 The code obeys a written coding standard, and the warnings of the compiler and of the analysis tools are on and are corrected. (proposed)
- [x] C-42 A quality plan names the reviews, the audits and the gates through the life cycle, and records show that they were done. (proposed)
- [x] C-43 Each defect is recorded in a tracker, classified, and its cause is analysed. (proposed)
- [x] C-45 The documentation for users and for contributors exists and is kept with the code. (proposed)
- [ ] C-48 The work is planned, estimated and measured, its risks are managed, and its process is defined. (declined: proposed reason: a project of one volunteer makes no estimates; the risks are in this file and the process is in `CONTRIBUTING.md`)
- [x] C-52 The team examines the effect of its practices with data and corrects them. (proposed; the dated review of this file is the record)

Level 2:

- [x] C-39 The measures of the tests are recorded and examined, without a fixed number in this recipe. (proposed)
- [x] C-41 The quality requirements are stated early, in measurable terms, from a quality model. (proposed)
- [x] C-44 The project builds from its source with a documented, common build system. (proposed)
- [x] C-47 The architecture and the design are described and are evaluated against the quality attributes. (proposed)
- [ ] C-49 Each person has the training and the knowledge that the role needs and works to the standards of the profession. (declined: proposed reason: the same as for C-19)
- [x] C-51 The dependencies are kept current by a stated rule, and a dependency that is not maintained is replaced. (proposed)
- [ ] C-46 The requirements are written, examined and traceable to the tests. (above the target level)
- [ ] C-50 The project has a stated governance: a license, roles, rules for a contribution and continuity when a person leaves. (above the target level)

Two notes for the owner on items above the target level. C-36: users of a
package also gain from a statement of the supported versions. C-50: the tree has
the licence files and the rules for a contribution already; only the list of
persons and the continuity are absent. The owner can adopt them.

## Distance (run of the checks on 2026-10-12)

Adopted in the proposal: 41 items. The check passes for 2, fails for 39.

- Passes: C-26, C-44.
- Fails, because the tree has no pipeline definition and the repository has no
  host: C-02, C-03, C-05, C-06, C-07, C-08, C-14, C-15, C-16, C-23, C-24, C-33,
  C-37, C-39, C-43.
- Fails, because a document or a configuration file is not in the tree: C-11,
  C-12, C-13, C-17, C-20, C-22, C-25, C-34, C-35, C-38, C-41, C-42, C-45, C-47,
  C-51, C-52.
- Fails in part, a part of the check passes: C-01, C-04, C-09, C-10, C-18, C-21,
  C-32, C-40.

The plan gives the evidence and the step for each item.
