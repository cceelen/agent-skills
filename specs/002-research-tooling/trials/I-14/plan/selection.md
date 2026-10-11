# Selection: DevSecOps

**Status: PROPOSED. The owner was not in the session of 2026-10-11. Each answer,
each target level and each mark below is a proposal of the agent. The owner
decides; until then nothing here is a decision.**

- Recipe: skill `devsecops`, trial rendering. Stamp: specification branch
  `001-devsecops`, commit `17a400d`, spec.md sha256
  `e74ac62b72bc282049a23fe436e67182847855d269c77a71f3c2f333000e856d`.
- Written: 2026-10-11. Review by the owner: not done.
- Measured: commit `ec6e8ce` of the branch `main`, the only commit. The
  repository has no remote and no tag.
- Plan: [devsecops-plan.md](devsecops-plan.md).

## Contexts

Found in the tree. Not confirmed by the owner.

| Context | Finding | Where |
|---|---|---|
| Size of the team | One maintainer, who works with an AI assistant. | `REUSE.toml` (`SPDX-FileCopyrightText`), `README.md` (AI policy), `CONTRIBUTING.md` (Rules for changes) |
| Users | Owners of one laptop model who install packages from the package manager of their distribution. The guard runs as root; the helpers run from udev; one part is a BPF program in the kernel. | `README.md` (What the packages fix), `tcc-guard/systemd/asus-ux8406-tcc-guard.service.in` |
| Kind of delivery | A source archive for each release, and packages that build services of the distributions make from it. No service that the project operates. | `packaging/`, `packaging/obs/README.md`, `README.md` (Installation) |
| Openness | Open source, two licences. Changes from outside are invited. | `LICENSE`, `LICENSES/`, `CONTRIBUTING.md` |
| Build platform | GitHub, by the statement of the user and by the documents. No pipeline definition is in the tree. | `CONTRIBUTING.md` names workflow files; `.github/` holds only `ISSUE_TEMPLATE/` |
| Duty from outside | None found. The licences ask for notices of third parties. Two badges of voluntary programmes are in `README.md`. | `about.toml`, `README.md` lines 3 to 6 |
| Development model | Pull requests to one primary branch, titles in the form of Conventional Commits, releases from these titles. | `CONTRIBUTING.md` (Rules for changes) |

## Risk analysis

| Dimension | Question | Answer (proposed) | Target level (proposed) |
|---|---|---|---|
| `exposure` | Do other projects or other persons build on your artifacts, or do persons from outside change your source? | Yes. Other persons install the packages, and some parts run as root. Four build services of distributions build from the release archive. Persons from outside can send changes. | 2 |
| `criticality` | How large is the harm to users when the software fails or the service stops? | Limited to one laptop: the machine switches off under load, a screen stays dark, or keys do nothing. The project operates no service and holds no data of users. | 1 |
| `evidence duty` | Does a law, a contract or a sponsor ask you to show what you did? | No. The two badges are voluntary. | 1 |

Opinion of the kit, with the reason:

- `exposure`: the answer is yes, thus the items of this dimension apply. The
  number of maintainers alone would permit level 1, but programs that run as
  root on the machines of other persons do not.
- `criticality`: the product is a set of packages, not a service that a team
  operates. Thus most items of the view `operations` above level 1 do not apply.
  This is the proposal with the most effect: 30 items depend on it. A reason to
  go to level 2 is that the guard runs as root and reads input that user space
  can write. If the owner goes to level 2, the items C-26, C-27, C-18, C-40 and
  C-70 are the ones that agree with this product; the tree has material for
  C-26 (`fuzz/`) and for C-70 (`CONTRIBUTING.md`).
- `evidence duty`: the answer is no, thus level 1. The documents say that the
  project makes a list of components for the Nix packages (`flake.nix`, output
  `sboms`). If the owner wants to keep that as a duty, C-13 goes to adopted.

## Decisions that depend on context

All proposed.

| Decision | Proposal | Reason |
|---|---|---|
| Which build level to reach first | Build L2 on the hosted platform, then Build L3. | The recipe gives L2 as the baseline and L3 as the goal. |
| How a change gets its approval | A share of reviewed changes: the owner approves each change from outside; a change of the owner has no second person. | One maintainer. The AI reviewer that `CONTRIBUTING.md` describes is a program, not a person who is not the author. |
| What the team does when the build of the primary branch fails | Correct the build at once; do not stop each commit. | One maintainer, few changes each day. |
| How fast the build of a change must be | A fast first build and slower later stages. | The container builds of the packages, the coverage and the fuzzing are slow; `CONTRIBUTING.md` puts two of them in a nightly run. |
| How large one change can be | No limit of lines; review of each change. The owner sets an age limit for open branches. | Without a limit, the check of C-51 has no measure. |
| How a change to production gets its approval | Not applicable: no production environment. | |
| How a new release reaches the users | One release for all users, through the repositories of the distributions. | The project does not control the stages of these repositories. |
| Which limit applies to a finding of an analysis | The project writes its limits into a policy. Proposed limits: a known vulnerability in a crate that goes into a program blocks a release when a corrected version exists; a licence that is not in the key `accepted` of `about.toml` blocks a change. | No source gives a number. |
| How the delivery measures are used | Not used: C-63 is above the target. | |
| How the provenance reaches the user | Beside the release artifacts. | The artifact of the project is the source archive; the distributions sign their own packages. |
| Which component generates the provenance | The attestation function of the platform for Build L2. The component for Build L3 is open. | No implementation skill is installed; the recipe says that the sample reusable workflow is no longer actively maintained. |

## Items

Result of the check on 2026-10-11, in brackets after each adopted item:
`pass`, `fail`, or `not measurable` (the check needs the remote repository, the
issue tracker or a history, and none is reachable).

### Operations

Level 1:

- [x] C-59 Each incident is recorded and analysed after it ends, and the corrections are done. [not measurable: no issue tracker reachable. Proposed meaning for this product: a release that harms the machines of users.]
- [x] C-62 The release process is defined, automated and usable by the team without a specialist. [fail]

Above level 1:

- [ ] C-54 The deployment is automated, and each environment is made from the same definition in version control. (above the target level)
- [ ] C-57 Monitoring and telemetry collect data at each layer of the service, and an alert goes to a person only when action is necessary. (above the target level)
- [ ] C-55 Each release can be rolled back, and the rollback is rehearsed before the deployment to production. (above the target level)
- [ ] C-60 Backup, recovery and failover exist and are tested at regular intervals. (above the target level)
- [ ] C-65 The risks of operation are managed, and a change to production does not weaken a control. (above the target level)
- [ ] C-56 A new release reaches the users in a controlled way that limits the harm of a fault. (above the target level)
- [ ] C-63 The project measures its delivery performance for each service: throughput and instability. (above the target level)
- [ ] C-53 The operation is planned from the start of the development, with the requirements for operation and maintenance. (above the target level)
- [ ] C-58 The service has agreed service level targets, and the project measures them. (above the target level)
- [ ] C-61 The capacity and the availability of the service are planned from measured data. (above the target level)
- [ ] C-64 The operations work has documented procedures, assigned roles and trained staff. (above the target level)
- [ ] C-66 The suppliers that the service depends on are known and coordinated. (above the target level)
- [ ] C-67 The software is designed for operation: it handles failures and can be deployed in small independent parts. (above the target level)

### Security

Level 1:

- [x] C-22 No secret is in the repository or in the output of the pipeline, and an automated scan looks for secrets in each change. [fail]
- [x] C-21 Access to the repository, the pipeline and the release needs multi-factor authentication and the least privilege. [not measurable: no remote]
- [x] C-35 The project publishes how to report a vulnerability, and has a process to answer and to disclose. [fail]
- [x] C-25 An automated analysis looks for known vulnerabilities and license problems in the dependencies, and a policy says how to act on a finding. [fail]
- [x] C-36 Each vulnerability is recorded, assessed by risk and corrected, and its root cause is removed. [not measurable: no issue tracker reachable]
- [x] C-23 The pipeline does not give credentials or privileged resources to code or input that is not trusted. [not measurable: no pipeline definition to examine]
- [x] C-34 Each release is archived with its integrity data and is protected against a change. [not measurable: no remote]
- [x] C-28 Third-party components come from a known origin, and the project verifies them before use. [pass]
- [x] C-29 The code follows secure coding practices and uses the protective features of the compiler and the build tools. [fail]
- [x] C-24 An automated static analysis looks for security weaknesses in each change. [fail]

Above level 1:

- [x] C-30 The software has secure default settings, and they are documented. [pass]
- [x] C-37 The project documents its governance: roles, how to contribute, the license, and how long a release gets security corrections. [fail]
- [ ] C-18 The security requirements of the software and of its development are written and kept current. (above the target level)
- [ ] C-27 The design is examined for security risks before the construction, and the result is recorded. (above the target level)
- [ ] C-33 The project defines the security checks that a release must pass, and keeps the results as evidence. (above the target level)
- [ ] C-38 An information security policy exists, the staff know it, and security incidents go through the incident process. (above the target level)
- [ ] C-26 The executable software is tested for vulnerabilities, with methods chosen by risk. (above the target level)
- [ ] C-19 The roles and the duties for security are assigned, and these persons get training. (above the target level)
- [ ] C-20 The management decides by risk which security practices apply, and commits resources to them. (above the target level)
- [ ] C-32 The pipeline keeps a log of its actions and of the access to it, and a person or a program examines the log. (above the target level)
- [ ] C-31 The environments for development, build and distribution are separated and hardened. (above the target level)

### Quality

Level 1:

- [x] C-49 Defects are recorded and measured, and their causes are analysed. [not measurable: no issue tracker reachable]
- [x] C-50 The test assets are in version control and are linked to the requirements and the code that they test. [pass for the first part of the check; the second part is not measurable with one commit]
- [x] C-39 Each change comes with automated tests, and the tests pass before the change enters the primary branch. [not measurable: no remote]
- [x] C-41 The tests give the same result on each run and do not depend on the person or the machine that runs them. [fail]
- [x] C-43 An automated analysis examines the code quality and the coding standards on each change. [fail]
- [x] C-51 Changes are small and are integrated into the primary branch one time each day or more. [not measurable: one commit, and no limit is set]

Above level 1:

- [ ] C-40 A test strategy names the test levels, the environments and the criteria that tell when the testing is sufficient. (above the target level)
- [ ] C-45 The quality requirements are written with a measure for each one. (above the target level)
- [ ] C-48 Work products get a review: requirements, design, code and tests. (above the target level)
- [ ] C-70 The construction follows planned methods, standards and tools. (above the target level)
- [ ] C-74 The engineers obey their professional, legal and ethical duties. (above the target level)
- [ ] C-42 The test environment is equivalent to the production environment. (above the target level)
- [ ] C-47 The project plans its quality assurance early, in proportion to the criticality of the software. (above the target level)
- [ ] C-75 Decisions use an economic analysis of cost, benefit and risk. (above the target level)
- [ ] C-68 The requirements are elicited, written, validated and managed. (above the target level)
- [ ] C-72 The project is planned, estimated, measured and controlled, with its risks. (above the target level)
- [ ] C-52 The tests cover the specific risks of the domain and the technology of the product. (above the target level)
- [ ] C-69 The architecture and the design are described and evaluated against the quality requirements. (above the target level)

### Pipeline

Level 1:

- [x] C-01 Each file that makes the product is in version control: source, tests, build definition and pipeline definition. [fail]
- [x] C-02 The primary branch is protected against a direct commit, a rewrite of its history and a deletion. [not measurable: no remote]
- [x] C-04 One automated command builds the product from a clean copy of the repository. [pass]
- [x] C-06 A hosted build platform builds each release artifact; no person builds a release on a personal computer. [fail]
- [x] C-10 Each release has a unique version, a record of its changes, and a digest or a signature for each artifact. [fail]
- [x] C-07 The build, the test and the packaging run as separate steps, and each step gets only the credentials that it needs. [fail]
- [x] C-08 The build platform generates provenance for each release artifact and signs it. [fail]
- [x] C-11 The user of an artifact verifies its signature or its provenance before the artifact is used or deployed. [fail]
- [x] C-05 Each change to the primary branch starts an automated build with tests, and the team corrects a broken build before other work. [fail]
- [x] C-12 The artifact that passed the tests is the artifact that is released; it is not built again. [fail]
- [x] C-14 The versions of the dependencies and of the build tools are pinned, and an automated process proposes their updates. [fail]

Above level 1:

- [x] C-03 A person who is not the author approves each change before it enters the primary branch. [not measurable: no remote. With one maintainer the check as written cannot pass for a change of the owner; refer to the decision above.]
- [x] C-15 The source control system records who made and who approved each change, and can give this record as evidence. [not measurable: no remote]
- [x] C-09 Each build runs in a new, isolated environment that cannot reach the signing secrets or change a different build. [fail]
- [ ] C-13 Each release has a list of its components, and the list is delivered with the release. (above the target level)

## Distance

34 items are adopted in this proposal. On 2026-10-11:

- 4 pass: C-04, C-28, C-30, C-50 (first part).
- 19 fail: C-01, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12, C-14, C-22,
  C-24, C-25, C-29, C-35, C-37, C-41, C-43, C-62.
- 11 are not measurable before the remote repository exists: C-02, C-03, C-15,
  C-21, C-23, C-34, C-36, C-39, C-49, C-51, C-59.

The evidence for each result and the change for each failed item are in the
[plan](devsecops-plan.md).
