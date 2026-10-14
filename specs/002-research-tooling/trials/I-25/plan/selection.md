# Selection: DevSecOps

Recipe: skill `devsecops`, a trial rendering of the specification branch
`001-devsecops`, commit `8d28b6b`, spec.md sha256
`13773da1eb9259f72b61c2d2677f1ac04c41e9293520d4a5c707c7b0fe7d96d2`.

Date of the risk analysis: 2026-10-13. No review yet.

**Each answer, each target level and each mark in this file is PROPOSED. The
owner was not in the session of the risk analysis and decided nothing.** An
agent wrote the proposals from the files of the repository. The owner accepts
or changes each of them; then remove the word "proposed" and give the date.

## Contexts

Found in the repository, not asked:

| Context            | Finding                                                                                                                       | Where                                                              |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Kind of delivery   | Packages for the package managers of distributions. Software for one machine: a root service, udev helpers, a HID-BPF program, two GNOME Shell extensions. The project operates no service. | `README.md`, `meson.build`, `packaging/`                           |
| Size               | One maintainer.                                                                                                               | `README.md` ("AI policy"), `REUSE.toml`, `CONTRIBUTING.md`         |
| Openness           | Open source, MIT and GPL-2.0-only. Public contributions by pull request.                                                      | `README.md` ("Licence"), `CONTRIBUTING.md`                         |
| Build platform     | The documents name GitHub Actions, Packit with COPR, OBS and a Cachix cache. The tree has no pipeline definition.             | `CONTRIBUTING.md`, `packaging/obs/README.md`, `flake.nix`          |
| Binding rules      | None named in the tree.                                                                                                       | no file                                                            |
| Rhythm of releases | Small releases from the titles of the pull requests; several on one day.                                                      | `CHANGELOG.md`, `CONTRIBUTING.md` ("Rules for changes")            |

## Risk analysis

| Dimension     | Question                                                                                                              | Answer (proposed)                                                                                                                                                                                                 | Target level (proposed)                         |
| ------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| `regulatory`  | Does a law, a regulation or a rule of an industry bind the product or the organization?                               | No rule is known to bind the project. Where the product is used is not known: the project is open, and each person can install the packages. Thus the answer is "not known", not "none". | 1                                               |
| `exposure`    | Can a public network reach the software or its pipeline, or does the software handle private or sensitive data?       | The software: no. It opens no network connection and handles no private data; the unit of the guard has no network. The pipeline: yes, it is on a public platform and takes pull requests from the public.        | 1                                               |
| `criticality` | What is the damage if the software fails or gives a wrong result?                                                     | Medium, on one machine. The guard runs as root and writes the thermal offset of the CPU. A failure switches the laptop off under load, and work that is not saved is lost. No danger to persons is known.         | 1                                               |
| `reach`       | Do other projects, customers or the public use the artifacts that the project releases?                               | Yes. The public installs the packages from four package repositories and a binary cache, and the packages run code as root.                                                                                       | 1; build integrity scale: Build L2 now, Build L3 as the goal |

Opinion of the kit for these answers:

- `regulatory`: no item is necessary because of a binding rule. Write the
  register (C-41) first, because the answer is "not known".
- `exposure`: the pipeline is reachable, thus do the items of the security view
  before the next public release.
- `criticality`: level 1 is sufficient at first. C-28 is above the target.
- `reach`: reach Build L2 first, then Build L3. One bad release reaches each
  user, with root rights.

## Regulation and governance

Binds the project (proposed): none known. The owner must confirm this; an agent
cannot decide a question of law.

Binds a user of the product: not known, and it cannot be known for an open
project.

Prepares for (proposed):

| Regulation or governance                                                    | Items of the checklist                                                                                                                                             | Prepare? (proposed)                                                                                                                         |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Regulation (EU) 2024/2847 (Cyber Resilience Act)                            | C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-17, C-25, C-37, C-39, C-41, C-43, C-44, C-45                                                                           | Yes. The packages are public software and can be installed in the EU. Whether the regulation binds an open project without a commercial activity is a question for the owner. |
| Directive (EU) 2024/2853 on liability for defective products                | C-15, C-41                                                                                                                                                         | Yes. The two items are also items of the Cyber Resilience Act.                                                                              |
| Payment Card Industry Data Security Standard                                | C-02, C-08, C-09, C-10, C-11, C-12, C-13, C-14, C-16, C-17, C-18, C-19, C-21, C-22, C-23, C-25, C-26, C-27, C-37, C-39, C-40, C-41, C-44                           | No. The product handles no payment data.                                                                                                    |
| Regulation (EU) 2022/2554 on digital operational resilience (DORA)          | C-08, C-09, C-11, C-12, C-14, C-17, C-18, C-19, C-23, C-24, C-25, C-26, C-27, C-34, C-35, C-38, C-39, C-40, C-41, C-43, C-44, C-45                                 | No. The project is not a financial entity and not its service provider.                                                                     |

## Decisions that depend on context

All proposed. Each of them needs the owner.

| Decision                                         | Proposal                                                                                                                                                        |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Target level of the build integrity scale        | Build L2 as the baseline, Build L3 as the goal.                                                                                                                 |
| Number of persons that review a change           | One person who is not the author. With one maintainer this check fails for each change of the owner. An automated reviewer is not a second person.              |
| Approval of a change to production               | The review and the passed pipeline are the approval. No binding rule asks for more.                                                                             |
| Time limit to correct a vulnerability            | Answer to a report in 7 days. Correction of a critical or high vulnerability in 30 days, of the others in 90 days. Disclosure with the correction.              |
| Interval of the security tests                   | The seeds of the fuzz targets on each change, a fuzz run each night. No penetration test.                                                                       |
| Limit of a scan finding that stops a release     | A finding of high severity or above stops. A finding that cannot be used for an attack can be suppressed with a record in the repository.                       |
| Rhythm of the releases and the branches          | Small changes into the main line, a release when a change is ready.                                                                                             |
| Reference of a component of the pipeline         | The full digest of a commit.                                                                                                                                    |
| Where the build runs                             | A hosted platform of a provider.                                                                                                                                |
| How the provenance is made                       | The attestation function of the build platform.                                                                                                                 |

## Items

`[x]` is "adopt (proposed)". The reasons of the declined items are proposals
too: the skill asks the owner for the reason.

### Security

Level 1:

- [x] C-01 Each change to the source is in version control, with an identified author and a protected main line.
- [x] C-02 A second person reviews and approves each change before it is merged or released.
- [x] C-03 The build runs on a hosted build platform from a build definition in version control, not on the computer of a person.
- [x] C-04 The build platform generates a signed provenance record for each artifact and distributes it with the artifact.
- [x] C-05 Each build runs in an isolated environment that is new for that build, and the build steps cannot reach the secrets that sign the provenance.
- [x] C-06 The build, the test and the packaging run as separate steps, and each step has only the privileges that it needs.
- [x] C-07 No step of the pipeline exposes a credential: secrets come from a secret store, are short-lived where possible, and are not in code, in artifacts or in logs.
- [x] C-08 Access to the repository, the pipeline and the release needs strong authentication and the minimum privilege, and it is reviewed and revoked in time.
- [x] C-09 The project makes a bill of materials of its components and dependencies for each release.
- [x] C-10 Dependencies come from trusted sources, are pinned to an exact version or digest, are verified before use and are kept up to date.
- [x] C-11 The pipeline scans the code, the dependencies and the artifacts for vulnerabilities and for secrets on each change, and a finding above the limit of the project stops the release.
- [x] C-12 The project states the security requirements of the product and models its threats before the design is fixed.
- [x] C-13 The code follows secure coding rules, and the product is secure in its default configuration.
- [x] C-14 The project has a public way to report a vulnerability, and it triages, corrects and discloses each vulnerability in a set time.
- [x] C-15 The project delivers security updates during a stated support period, and a user can get, verify and install an update.
- [x] C-16 Each release artifact is signed, and the consumer or the deployment verifies the artifact and its provenance before use.
- [x] C-17 The project tests the security of the running product, with dynamic tests, fuzzing or penetration tests, in line with its risk.
- [x] C-18 The systems of the pipeline are in an inventory, and are hardened, patched, logged and monitored.
- [x] C-19 The project states its security and quality requirements to its suppliers and service providers, and examines that they keep them.
- [x] C-44 The product protects the data that it stores, sends and processes, limits the access to its functions, and records security events.

### Operations

Level 1:

- [x] C-20 The deployment is automated from versioned definitions, and the infrastructure and the configuration are code in version control.
- [x] C-21 Each release goes out in steps, can be rolled back, and the rollback is rehearsed.
- [x] C-22 The development, the test and the production environments are separate, and production data and production credentials stay out of the test environments.
- [ ] C-23 The service has monitoring, logs and alerts that are designed together with the software, and each alert asks for an action. (declined: proposed reason: the project operates no service; the programs run on the machine of the user and write to its journal)
- [ ] C-24 The service has service level objectives that are agreed with its stakeholders, and it measures them. (declined: proposed reason: the project operates no service and has no agreement with its users)
- [x] C-25 The project has an incident response plan with named roles, tests it, and writes a review without blame after each incident.
- [x] C-26 Each change to production is recorded, assessed for its risk, tested and approved under a change procedure.
- [ ] C-27 Backup, restore, continuity and capacity are planned, and the restore is tested. (declined: proposed reason: the project holds no data of users and operates no service; the source is in each clone of the repository)
- [x] C-29 A new service passes a readiness review before its first release.
- [x] C-45 The project identifies and controls its configuration items and baselines, and can make each release again from them.
- [x] C-46 An artifact is built one time, is kept in a controlled store where it cannot be changed, and the same artifact goes through each environment.

Level 2:

- [ ] C-28 The team measures its delivery performance and improves its largest constraint. (above the target level)

How the proposal reads the items for a project without a service:
"production" is the four package repositories and the binary cache; a
"deployment" is a publication to them; a "service" in C-29 is a new package or
a new distribution.

The skill keeps one rule without a trade: the basic practices of each view are
covered. Three declined items of level 1 are in this view. The owner decides if
the three reasons hold.

### Quality

Level 1:

- [x] C-30 Each change starts an automated build and automated tests, and a broken build is corrected before other work.
- [x] C-31 Automated tests exist on the unit, the integration and the system level, and a change adds or updates its tests.
- [x] C-32 The pipeline enforces the coding standards and runs static analysis on each change.
- [x] C-33 The quality requirements of the product are stated in measurable words and are agreed with the stakeholders.
- [x] C-34 The project plans its quality assurance: reviews, audits, verification and validation, with more independence for more critical software.
- [x] C-35 The project measures the quality of the product and of the process, finds the root cause of a defect, and corrects the process.
- [x] C-36 Changes are small and are integrated into the main line often.
- [x] C-37 The documentation for the use, the operation and the maintenance is kept with the product and is current.
- [x] C-38 The project records its requirements and its design decisions, and traces them to the tests.
- [x] C-39 Each person has the knowledge and the training that the role needs.
- [x] C-40 The roles and the responsibilities for security, operations and quality are assigned, and the management commits to them and gives the resources.
- [x] C-41 The project knows each law, regulation and rule of an industry that binds its product, names an owner for each duty, and keeps the evidence of conformity.
- [x] C-42 The project plans, estimates and tracks its work, its risks and its cost.
- [x] C-43 The project plans the maintenance of the software and the end of its life.

## Distance

The distance on 2026-10-13 is in `.agents/kit/devsecops-plan.md`, section
"Distance".
