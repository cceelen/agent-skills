# Selection: DevSecOps

Recipe: `devsecops`, rendered from the specification branch `001-devsecops`, commit
`8f2ce19`, spec.md sha256
`13773da1eb9259f72b61c2d2677f1ac04c41e9293520d4a5c707c7b0fe7d96d2` (trial rendering).

Written: 2026-10-14, by an agent, in a session without the owner.

**Status: PROPOSED. The owner did not take part in this session. Each answer, each target
level and each decision below is a proposal of the agent. Nothing here is a decision of the
owner until the owner confirms it.** The proposals are marked `(proposed)`.

## Contexts of the project

The agent read these from the tree. The sources are given; the values are in the files.

| Context | Finding | Where |
|---|---|---|
| Kind of delivery | Distribution packages (rpm, deb, Arch, Alpine, Nix) and a source archive; no service that the project runs | `README.md`, section Installation; `packaging/` |
| Size of the organization | One maintainer; outside contributors through pull requests | `README.md`, section "Contact and contributions"; `CONTRIBUTING.md` |
| Openness | Open source, MIT and GPL-2.0-only, public repository on GitHub | `LICENSE`, `REUSE.toml`, `README.md` section Licence |
| Commercial activity | None stated: "a community project", no warranty | `README.md`, section Disclaimer |
| Build platform | GitHub Actions (named, not in the tree), Packit/COPR, openSUSE Build Service, Cachix, Alpine aports | `CONTRIBUTING.md`; `packaging/obs/README.md`; `flake.nix` key `nixConfig` |
| Rhythm of the releases | Release Please from Conventional Commits titles; five releases in two days | `CHANGELOG.md`; `CONTRIBUTING.md` section "Rules for changes" |
| Privilege of the product | The guard runs as root and writes a CPU thermal limit; two helpers run as root from udev | `tcc-guard/systemd/asus-ux8406-tcc-guard.service.in`; `second-screen/udev/`, `keyboard-state/udev/` |
| Pipeline definitions, security policy, release procedure | Named by the documents but **absent from the tree**: `.github/workflows/*.yml`, `SECURITY.md`, `docs/releases.md`, `.obs/workflows.yml`, the Renovate, pre-commit and Packit configurations | `README.md` table "Where to start"; `CONTRIBUTING.md`; `packaging/obs/README.md` |
| Remote | None. Repository settings, branch protection and access lists cannot be read | `git remote -v` (empty) |

## Regulation and governance

The owner cannot know where the product is used: it is an open project. Thus the answer
is not "none". (proposed)

| Regulation or governance | Binds the project? | Binds a user of the product? | Prepare for it? |
|---|---|---|---|
| Regulation (EU) 2024/2847 (Cyber Resilience Act) | No (proposed): free and open-source software outside a commercial activity; no steward | Possibly: a distributor or integrator who makes it available in a commercial activity | **Yes, prepare** (proposed): the packages are redistributed by distributions, and the items are good practice for software that runs as root |
| Directive (EU) 2024/2853 on product liability | No (proposed): excluded outside a commercial activity | Possibly, as above | No (proposed): its two items, C-15 and C-41, are prepared through the CRA |
| Regulation (EU) 2022/2554 (DORA) | No: the project is not a financial entity or an ICT third-party service provider | Possibly: a financial entity that installs the packages on laptops; its duties are on its own ICT risk management | No (proposed) |
| PCI DSS | No: the project does not handle cardholder data | Unlikely: the product handles no cardholder data | No (proposed) |

Owner of the binding duties: none named. Proposed owner: the maintainer (proposed).

## Risk analysis

| Dimension | Question | Answer (proposed) | Opinion of the kit | Target level |
|---|---|---|---|---|
| `regulatory` | Does a law, a regulation or a rule of an industry bind the product or the organization? | No known rule binds the project; the CRA can bind a user who redistributes commercially; the project prepares for the CRA | Do each item that a binding rule asks for; write the rule and its owner first | 1 (proposed) |
| `exposure` | Can a public network reach the software or its pipeline, or does the software handle private or sensitive data? | Yes for the pipeline: a public repository with pull requests from forks, and release credentials for OBS, COPR, Cachix and aports. The product opens no network port, but it runs as root and reads `/dev/kmsg`, which user space can write | Do the items of the security view on each level before the first public release | 1 (proposed); all security items are level 1 |
| `criticality` | What is the damage if the software fails or gives a wrong result? | Medium: a wrong guard lets the laptop power off under load (data loss) or throttles the CPU; a wrong helper switches a screen off. No damage to third parties | For a low damage, level 1 is sufficient at first | 1 (proposed) |
| `reach` | Do other projects, customers or the public use the artifacts that the project releases? | Yes: public package repositories, a public Nix binary cache, a merge request to Alpine | Reach the baseline of the build integrity scale first, then its goal | Build L2 baseline, Build L3 goal (proposed) |

## Decisions that need the owner (all proposed)

| Decision | Proposal |
|---|---|
| Target level of the build integrity scale | Build L2 for each release artifact now; Build L3 as the goal (GitHub-hosted runners with the attestation function) |
| Number of reviewers | One person who is not the author for a contribution; for the maintainer's own change, the AI reviewer and the passed pipeline as a recorded deviation until a second maintainer exists |
| Approval of a change to production (a release) | The review and the passed pipeline of the Release Please pull request are the approval |
| Time limit to correct a vulnerability | Acknowledge in 7 days; correct a critical or high finding in 30 days, others in 90 days |
| Interval of the security tests of the running product | Fuzzing each night (already named in `CONTRIBUTING.md`); a dated summary for each minor release |
| Limit of a scan finding that stops a release | A finding of high or critical severity stops; a finding that cannot be used for an attack is suppressed with a record |
| Rhythm of the releases | Small changes into the main line with continuous delivery (as now) |
| Reference of a pipeline component | The full commit digest |
| Where the build runs | Hosted platforms of providers |
| How the provenance is made | The attestation function of the build platform |

## Items

### Security

- [ ] C-01 Each change to the source is in version control, with an identified author and a protected main line. (proposed: adopt)
- [ ] C-02 A second person reviews and approves each change before it is merged or released. (proposed: adopt)
- [ ] C-03 The build runs on a hosted build platform from a build definition in version control, not on the computer of a person. (proposed: adopt)
- [ ] C-04 The build platform generates a signed provenance record for each artifact and distributes it with the artifact. (proposed: adopt)
- [ ] C-05 Each build runs in an isolated environment that is new for that build, and the build steps cannot reach the secrets that sign the provenance. (proposed: adopt)
- [ ] C-06 The build, the test and the packaging run as separate steps, and each step has only the privileges that it needs. (proposed: adopt; own rule, not tradable)
- [ ] C-07 No step of the pipeline exposes a credential: secrets come from a secret store, are short-lived where possible, and are not in code, in artifacts or in logs. (proposed: adopt; own rule, not tradable)
- [ ] C-08 Access to the repository, the pipeline and the release needs strong authentication and the minimum privilege, and it is reviewed and revoked in time. (proposed: adopt)
- [ ] C-09 The project makes a bill of materials of its components and dependencies for each release. (proposed: adopt) (prepared: Regulation (EU) 2024/2847 (Cyber Resilience Act))
- [ ] C-10 Dependencies come from trusted sources, are pinned to an exact version or digest, are verified before use and are kept up to date. (proposed: adopt) (prepared: Regulation (EU) 2024/2847 (Cyber Resilience Act))
- [ ] C-11 The pipeline scans the code, the dependencies and the artifacts for vulnerabilities and for secrets on each change, and a finding above the limit of the project stops the release. (proposed: adopt) (prepared: Regulation (EU) 2024/2847 (Cyber Resilience Act))
- [ ] C-12 The project states the security requirements of the product and models its threats before the design is fixed. (proposed: adopt) (prepared: Regulation (EU) 2024/2847 (Cyber Resilience Act))
- [ ] C-13 The code follows secure coding rules, and the product is secure in its default configuration. (proposed: adopt) (prepared: Regulation (EU) 2024/2847 (Cyber Resilience Act))
- [ ] C-14 The project has a public way to report a vulnerability, and it triages, corrects and discloses each vulnerability in a set time. (proposed: adopt) (prepared: Regulation (EU) 2024/2847 (Cyber Resilience Act))
- [ ] C-15 The project delivers security updates during a stated support period, and a user can get, verify and install an update. (proposed: adopt) (prepared: Regulation (EU) 2024/2847 (Cyber Resilience Act))
- [ ] C-16 Each release artifact is signed, and the consumer or the deployment verifies the artifact and its provenance before use. (proposed: adopt)
- [ ] C-17 The project tests the security of the running product, with dynamic tests, fuzzing or penetration tests, in line with its risk. (proposed: adopt) (prepared: Regulation (EU) 2024/2847 (Cyber Resilience Act))
- [ ] C-18 The systems of the pipeline are in an inventory, and are hardened, patched, logged and monitored. (proposed: adopt)
- [ ] C-19 The project states its security and quality requirements to its suppliers and service providers, and examines that they keep them. (proposed: adopt, in the form of a column of the inventory of C-18)
- [ ] C-44 The product protects the data that it stores, sends and processes, limits the access to its functions, and records security events. (proposed: adopt) (prepared: Regulation (EU) 2024/2847 (Cyber Resilience Act))

### Operations

- [ ] C-20 The deployment is automated from versioned definitions, and the infrastructure and the configuration are code in version control. (proposed: adopt; the deployment is the publication to OBS, COPR, Cachix and aports)
- [ ] C-21 Each release goes out in steps, can be rolled back, and the rollback is rehearsed. (proposed: adopt)
- [ ] C-22 The development, the test and the production environments are separate, and production data and production credentials stay out of the test environments. (proposed: adopt; production is the set of release credentials)
- [ ] C-23 The service has monitoring, logs and alerts that are designed together with the software, and each alert asks for an action. (declined: the project runs no service; the failures of the publication are covered by C-20 and C-21) (proposed)
- [ ] C-24 The service has service level objectives that are agreed with its stakeholders, and it measures them. (declined: the project runs no service and has no agreed stakeholders) (proposed)
- [ ] C-25 The project has an incident response plan with named roles, tests it, and writes a review without blame after each incident. (proposed: adopt; the incident is a compromised or broken release) (prepared: Regulation (EU) 2024/2847 (Cyber Resilience Act))
- [ ] C-26 Each change to production is recorded, assessed for its risk, tested and approved under a change procedure. (proposed: adopt)
- [ ] C-27 Backup, restore, continuity and capacity are planned, and the restore is tested. (proposed: adopt; continuity of the repository, the accounts and the signing keys)
- [ ] C-28 The team measures its delivery performance and improves its largest constraint. (above the target level)
- [ ] C-29 A new service passes a readiness review before its first release. (proposed: adopt; for each new package or distribution channel)
- [ ] C-45 The project identifies and controls its configuration items and baselines, and can make each release again from them. (proposed: adopt) (prepared: Regulation (EU) 2024/2847 (Cyber Resilience Act))
- [ ] C-46 An artifact is built one time, is kept in a controlled store where it cannot be changed, and the same artifact goes through each environment. (proposed: adopt; the source archive)

### Quality

- [ ] C-30 Each change starts an automated build and automated tests, and a broken build is corrected before other work. (proposed: adopt)
- [ ] C-31 Automated tests exist on the unit, the integration and the system level, and a change adds or updates its tests. (proposed: adopt)
- [ ] C-32 The pipeline enforces the coding standards and runs static analysis on each change. (proposed: adopt)
- [ ] C-33 The quality requirements of the product are stated in measurable words and are agreed with the stakeholders. (proposed: adopt)
- [ ] C-34 The project plans its quality assurance: reviews, audits, verification and validation, with more independence for more critical software. (proposed: adopt)
- [ ] C-35 The project measures the quality of the product and of the process, finds the root cause of a defect, and corrects the process. (proposed: adopt)
- [ ] C-36 Changes are small and are integrated into the main line often. (proposed: adopt)
- [ ] C-37 The documentation for the use, the operation and the maintenance is kept with the product and is current. (proposed: adopt) (prepared: Regulation (EU) 2024/2847 (Cyber Resilience Act))
- [ ] C-38 The project records its requirements and its design decisions, and traces them to the tests. (proposed: adopt)
- [ ] C-39 Each person has the knowledge and the training that the role needs. (declined: one maintainer and no roles to train; the rules for contributors are in `CONTRIBUTING.md`) (proposed; note: the CRA asks for it, so a decline is a deviation from the preparation)
- [ ] C-40 The roles and the responsibilities for security, operations and quality are assigned, and the management commits to them and gives the resources. (proposed: adopt)
- [ ] C-41 The project knows each law, regulation and rule of an industry that binds its product, names an owner for each duty, and keeps the evidence of conformity. (proposed: adopt) (prepared: Regulation (EU) 2024/2847 (Cyber Resilience Act))
- [ ] C-42 The project plans, estimates and tracks its work, its risks and its cost. (proposed: adopt)
- [ ] C-43 The project plans the maintenance of the software and the end of its life. (proposed: adopt) (prepared: Regulation (EU) 2024/2847 (Cyber Resilience Act))

Note on the format: an adopted item is written `- [x]` after the owner confirms it. Until
then each proposed adoption stays `- [ ]` with `(proposed: adopt)`.

## Reviews

- 2026-10-14: first proposal, by an agent, without the owner.
