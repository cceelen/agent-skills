# Vetting record: DevSecOps

The signals and the scores of the independent sources, the answers of risk and reward for each
checklist item, the register of the requirements, the proposed boundaries and the record of
the reading. Programs compute the levels and the scores. Only the owner confirms a source.

## Searches

Each search query of phase 2, with the view that it serves. The date of each search is 2026-10-11.

- all views: `DevSecOps standard guidance shift left security operations quality software delivery (NIST OR DoD OR OWASP OR CNCF)`
- pipeline, target: `SLSA specification build track levels requirements current version`
- security: `secure software development framework practices for software producers standard`
- operations, statistics: `software delivery performance metrics deployment frequency change failure rate annual report`
- security, pipeline: `CI/CD pipeline security risks top 10 poisoned pipeline execution credential hygiene`
- quality: `continuous integration build pipeline quality gates automated testing static analysis before merge standard guidance`
- pipeline, security: `NIST SP 800-204D strategies integration software supply chain security DevSecOps CI/CD pipelines`
- security, tools that measure: `OpenSSF Scorecard checks automated security health open source projects; OpenSSF best practices baseline criteria`
- operations: `release engineering reliable deployment progressive rollout rollback monitoring observability best practices operations readiness before production`
- pipeline, components that a project can use again: `reusable workflows hardened build provenance generator open source project SLSA level 3 maintained`
- all views: `DoD Enterprise DevSecOps Fundamentals reference design CNCF software supply chain best practices paper`
- quality, operations: `ISO/IEC 25010 product quality model characteristics; ISO/IEC/IEEE 32675 DevOps building reliable and secure systems standard`
- operations, quality: `DORA capabilities catalog continuous integration test automation deployment automation monitoring observability dora.dev`
- security, tools that measure: `Open Source Project Security Baseline OSPS controls maturity levels OpenSSF`
- operations: `Site Reliability Engineering book release engineering hermetic builds chapter; service level objectives error budget launch checklist`
- all views, statistics: `state of software supply chain annual report open source security statistics; Octoverse OR "State of DevOps" 2025 survey`
- pipeline, projects that many projects depend on: `Kubernetes release process documentation signed artifacts provenance SBOM release engineering SIG Release`
- quality: `continuous integration practices self-testing build mainline every commit fix broken builds immediately article`

What the samples use, from the stored lines of the sample readers (S-14, S-15, S-16). The pattern lines that describe the same pattern are together under one name.

- `provenance from an isolated, trusted job`: the job that generates and signs the provenance is separate from the job that builds (S-14 "Isolated trusted reusable workflows", "Builder and generator split", "Build your own builder"; S-16 "Thin wrapper over shared action").
- `signing as a stage of its own`: the signing runs as its own stage of the release pipeline, with an identity of the workload and no long-lived key (S-15 "Dedicated signing pipeline stage", "Keyless signing with workload identities").
- `verification of artifacts`: the project shows how a user verifies the signature and the identity of the signer of an artifact, how a deployment refuses an image without a signature, and how an image is pinned by its digest (S-15 "Client-side artifact verification", "Verify release artifacts before use", "Admission-time signature verification", "Digest pinning in manifests").
- Principles of the projects are opinions of these projects. Two of them are in section 3.4 of `spec.md`: the sample S-14 says that its workflows alone do not reach Build Level 3, and that the project is no longer actively maintained. No principle of a sample is a checklist item for that reason alone.

## Sources

| Source | Kind | Answers | Gates | Signals | Score | Date | Confirmed by |
|---|---|---|---|---|---|---|---|
| S-10 | page | record: yes (https://dora.dev/research/); fast-lane references: 0 (the readers of the fast-lane sources reported no reference to this source by its name) | pass | reachable yes; date 2026-10-10; age 1 d; author yes; links out 9 | 8 of 10 | 2026-10-11 | |
| S-13 | page | record: yes (https://martinfowler.com/aboutMe.html); fast-lane references: 0 (the readers of the fast-lane sources reported no reference to this source) | pass | reachable yes; date 2026-10-10; age 1 d; author yes; links out 15 | 8 of 10 | 2026-10-11 | |

## Items

The six answers for each checklist item. The scales are in `factory/sota-research/scripts/rubric-items.txt`. An answer names its source in `evidence.md`, or says `(judgement)`.

| Item | Severity | Probability | Breadth | Adopt | Keep | Own risk | Dimension | Return | Cost | Score | Admitted | Level |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C-01 | 3 (judgement) | 3 (judgement) | 3 (S-07 Level 1) | 1 (judgement) | 1 (judgement) | 0 (judgement) |  | 27 | 2 | 135 | yes | 1 |
| C-02 | 3 (judgement) | 2 (judgement) | 3 (S-07 Level 1) | 1 (judgement) | 1 (judgement) | 0 (judgement) |  | 18 | 2 | 90 | yes | 1 |
| C-03 | 3 (judgement) | 2 (judgement) | 2 (S-06 Code-Review check) | 1 (judgement) | 2 (judgement) | 0 (judgement) | exposure | 12 | 3 | 40 | yes | 2, exposure |
| C-04 | 2 (judgement) | 3 (judgement) | 3 (judgement) | 2 (judgement) | 1 (judgement) | 0 (judgement) |  | 18 | 3 | 60 | yes | 1 |
| C-05 | 2 (judgement) | 3 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) |  | 18 | 4 | 45 | yes | 1 |
| C-06 | 3 (judgement) | 2 (judgement) | 3 (judgement) | 2 (S-02 Build L2) | 1 (judgement) | 0 (judgement) |  | 18 | 3 | 60 | yes | 1 |
| C-07 | 3 (judgement) | 2 (judgement) | 3 (judgement) | 2 (judgement) | 1 (judgement) | 1 (judgement) |  | 18 | 3 | 55 | yes | 1 |
| C-08 | 3 (judgement) | 2 (judgement) | 3 (judgement) | 2 (S-02 Build L2) | 1 (judgement) | 1 (judgement) |  | 18 | 3 | 55 | yes | 1 |
| C-09 | 3 (judgement) | 2 (judgement) | 2 (judgement) | 3 (S-02 Build L3) | 1 (judgement) | 1 (judgement) | exposure | 12 | 4 | 25 | yes | 2, exposure |
| C-10 | 2 (judgement) | 3 (judgement) | 3 (S-07 Level 1 and Level 2) | 1 (judgement) | 2 (judgement) | 0 (judgement) |  | 18 | 3 | 60 | yes | 1 |
| C-11 | 3 (judgement) | 2 (judgement) | 3 (judgement) | 2 (judgement) | 1 (judgement) | 1 (judgement) |  | 18 | 3 | 55 | yes | 1 |
| C-12 | 2 (judgement) | 2 (judgement) | 3 (judgement) | 2 (judgement) | 1 (judgement) | 0 (judgement) |  | 12 | 3 | 40 | yes | 1 |
| C-13 | 2 (judgement) | 2 (judgement) | 3 (judgement) | 2 (judgement) | 1 (judgement) | 1 (judgement) | evidence duty | 12 | 3 | 35 | yes | 2, evidence duty |
| C-14 | 3 (judgement) | 2 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 1 (judgement) |  | 18 | 4 | 40 | yes | 1 |
| C-15 | 3 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 1 (judgement) | 1 (judgement) | exposure | 12 | 3 | 35 | yes | 2, exposure |
| C-16 | 2 (judgement) | 2 (judgement) | 1 (judgement) | 3 (judgement) | 3 (judgement) | 1 (judgement) |  | 4 | 6 | 1 | no | not admitted |
| C-17 | 3 (judgement) | 1 (judgement) | 2 (judgement) | 3 (judgement) | 3 (judgement) | 1 (judgement) |  | 6 | 6 | 5 | no | not admitted |
| C-18 | 2 (judgement) | 2 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 12 | 4 | 30 | yes | 2, criticality |
| C-19 | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 8 | 4 | 20 | yes | 2, criticality |
| C-20 | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 8 | 4 | 20 | yes | 2, criticality |
| C-21 | 3 (judgement) | 2 (judgement) | 3 (S-07 Level 1) | 1 (judgement) | 1 (judgement) | 0 (judgement) |  | 18 | 2 | 90 | yes | 1 |
| C-22 | 3 (judgement) | 3 (judgement) | 3 (S-07 Level 1) | 1 (judgement) | 1 (judgement) | 0 (judgement) |  | 27 | 2 | 135 | yes | 1 |
| C-23 | 3 (judgement) | 2 (judgement) | 3 (S-07 Level 1) | 2 (judgement) | 1 (judgement) | 0 (judgement) |  | 18 | 3 | 60 | yes | 1 |
| C-24 | 2 (judgement) | 3 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 1 (judgement) |  | 18 | 4 | 40 | yes | 1 |
| C-25 | 3 (judgement) | 3 (judgement) | 3 (judgement) | 1 (judgement) | 2 (judgement) | 1 (judgement) |  | 27 | 3 | 85 | yes | 1 |
| C-26 | 3 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 1 (judgement) | criticality | 12 | 4 | 25 | yes | 2, criticality |
| C-27 | 3 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 12 | 4 | 30 | yes | 2, criticality |
| C-28 | 3 (judgement) | 2 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) |  | 18 | 4 | 45 | yes | 1 |
| C-29 | 2 (judgement) | 3 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) |  | 18 | 4 | 45 | yes | 1 |
| C-30 | 3 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 1 (judgement) | 0 (judgement) | exposure | 12 | 3 | 40 | yes | 2, exposure |
| C-31 | 3 (judgement) | 2 (judgement) | 2 (judgement) | 3 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 12 | 5 | 24 | yes | 3, criticality |
| C-32 | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | evidence duty | 8 | 4 | 20 | yes | 2, evidence duty |
| C-33 | 2 (judgement) | 2 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | evidence duty | 12 | 4 | 30 | yes | 2, evidence duty |
| C-34 | 2 (judgement) | 2 (judgement) | 3 (judgement) | 1 (judgement) | 1 (judgement) | 0 (judgement) |  | 12 | 2 | 60 | yes | 1 |
| C-35 | 3 (judgement) | 2 (judgement) | 3 (S-07 Level 1) | 1 (judgement) | 1 (judgement) | 0 (judgement) |  | 18 | 2 | 90 | yes | 1 |
| C-36 | 3 (judgement) | 3 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) |  | 27 | 4 | 67 | yes | 1 |
| C-37 | 1 (judgement) | 3 (judgement) | 3 (S-07 Level 1) | 1 (judgement) | 2 (judgement) | 0 (judgement) | exposure | 9 | 3 | 30 | yes | 2, exposure |
| C-38 | 3 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 12 | 4 | 30 | yes | 2, criticality |
| C-39 | 2 (judgement) | 3 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) |  | 18 | 4 | 45 | yes | 1 |
| C-40 | 2 (judgement) | 2 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 12 | 4 | 30 | yes | 2, criticality |
| C-41 | 2 (judgement) | 3 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) |  | 18 | 4 | 45 | yes | 1 |
| C-42 | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 8 | 4 | 20 | yes | 2, criticality |
| C-43 | 1 (judgement) | 3 (judgement) | 3 (judgement) | 1 (judgement) | 1 (judgement) | 0 (judgement) |  | 9 | 2 | 45 | yes | 1 |
| C-45 | 2 (judgement) | 2 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 12 | 4 | 30 | yes | 2, criticality |
| C-47 | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 8 | 4 | 20 | yes | 2, criticality |
| C-48 | 2 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 12 | 4 | 30 | yes | 2, criticality |
| C-49 | 2 (judgement) | 3 (judgement) | 3 (judgement) | 1 (judgement) | 2 (judgement) | 0 (judgement) |  | 18 | 3 | 60 | yes | 1 |
| C-50 | 2 (judgement) | 2 (judgement) | 3 (judgement) | 1 (judgement) | 1 (judgement) | 0 (judgement) |  | 12 | 2 | 60 | yes | 1 |
| C-51 | 2 (judgement) | 3 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) |  | 18 | 4 | 45 | yes | 1 |
| C-52 | 3 (judgement) | 2 (judgement) | 2 (judgement) | 3 (judgement) | 3 (judgement) | 0 (judgement) | criticality | 12 | 6 | 20 | yes | 3, criticality |
| C-53 | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 8 | 4 | 20 | yes | 2, criticality |
| C-54 | 2 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 1 (judgement) | 0 (judgement) | criticality | 12 | 3 | 40 | yes | 2, criticality |
| C-55 | 3 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 12 | 4 | 30 | yes | 2, criticality |
| C-56 | 3 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 1 (judgement) | criticality | 12 | 4 | 25 | yes | 2, criticality |
| C-57 | 3 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 1 (judgement) | criticality | 18 | 4 | 40 | yes | 2, criticality |
| C-58 | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 8 | 4 | 20 | yes | 2, criticality |
| C-59 | 3 (judgement) | 2 (judgement) | 3 (judgement) | 1 (judgement) | 2 (judgement) | 0 (judgement) |  | 18 | 3 | 60 | yes | 1 |
| C-60 | 3 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 12 | 4 | 30 | yes | 2, criticality |
| C-61 | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 8 | 4 | 20 | yes | 2, criticality |
| C-62 | 2 (judgement) | 3 (judgement) | 3 (judgement) | 2 (judgement) | 1 (judgement) | 0 (judgement) |  | 18 | 3 | 60 | yes | 1 |
| C-63 | 2 (judgement) | 2 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 1 (S-10 metrics guide) | criticality | 12 | 4 | 25 | yes | 2, criticality |
| C-64 | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 8 | 4 | 20 | yes | 2, criticality |
| C-65 | 3 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 12 | 4 | 30 | yes | 2, criticality |
| C-66 | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 8 | 4 | 20 | yes | 2, criticality |
| C-67 | 3 (judgement) | 2 (judgement) | 2 (judgement) | 3 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 12 | 5 | 24 | yes | 3, criticality |
| C-68 | 2 (judgement) | 3 (judgement) | 3 (judgement) | 3 (judgement) | 3 (judgement) | 0 (judgement) | criticality | 18 | 6 | 30 | yes | 3, criticality |
| C-69 | 2 (judgement) | 2 (judgement) | 3 (judgement) | 3 (judgement) | 3 (judgement) | 0 (judgement) | criticality | 12 | 6 | 20 | yes | 3, criticality |
| C-70 | 2 (judgement) | 2 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 12 | 4 | 30 | yes | 2, criticality |
| C-71 | 2 (judgement) | 2 (judgement) | 2 (judgement) | 3 (judgement) | 3 (judgement) | 0 (judgement) | criticality | 8 | 6 | 13 | no | not admitted |
| C-72 | 2 (judgement) | 3 (judgement) | 3 (judgement) | 3 (judgement) | 3 (judgement) | 0 (judgement) | criticality | 18 | 6 | 30 | yes | 3, criticality |
| C-73 | 2 (judgement) | 2 (judgement) | 2 (judgement) | 3 (judgement) | 3 (judgement) | 0 (judgement) | criticality | 8 | 6 | 13 | no | not admitted |
| C-74 | 3 (judgement) | 1 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 9 | 4 | 22 | yes | 2, criticality |
| C-75 | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | criticality | 8 | 4 | 20 | yes | 2, criticality |
| C-76 | 2 (judgement) | 1 (judgement) | 3 (judgement) | 3 (judgement) | 3 (judgement) | 0 (judgement) |  | 6 | 6 | 10 | no | not admitted |
| C-77 | 1 (judgement) | 1 (judgement) | 1 (judgement) | 3 (judgement) | 2 (judgement) | 0 (judgement) |  | 1 | 5 | 2 | no | not admitted |

## Requirements

One row for each requirement line of the reports of the readers. The sentence of a row is the sentence of the reader about the source. The stakeholder and the exit of each row are a judgement of this run.

| Id | Requirement | Stakeholder | View | Source | Goes to |
|---|---|---|---|---|---|
| R-0001 | For each executed test case it must be possible, though not always easy, to decide whether observed outcomes match the expected ones. | quality assurance | quality | S-01 page 118 | C-40 |
| R-0002 | Software engineers must be aware that different test selection criteria can yield very different degrees of effectiveness. | software engineers | quality | S-01 page 118 | C-40 |
| R-0003 | Testing needs to focus on specific mandatory prescriptions such as requirements, laws and standards. | quality assurance | quality | S-01 page 120 | C-40 |
| R-0004 | Test cases should be generated and executed to give evidence for evaluating or certifying adherence to the selected prescriptions. | quality assurance | quality | S-01 page 120 | C-40 |
| R-0005 | In some cases a trade-off must be made between the assurance from regression testing and the resources it needs. | quality assurance | quality | S-01 page 124 | C-40 |
| R-0006 | The testing environment needs to represent the actual operational environment for usage-based testing. | quality assurance | quality | S-01 page 131 | C-42 |
| R-0007 | Testing processes should allow automation of the different testing phases. | quality assurance | quality | S-01 page 134 | C-39 |
| R-0008 | Test activities should be organized into a well-defined process integral to the life cycle. | quality assurance | quality | S-01 page 135 | C-40 |
| R-0009 | The test strategy should include at least the purposes, objectives, scope, and environment and methods. | quality assurance | quality | S-01 page 135 | C-40 |
| R-0010 | Test documentation should be produced and continuously updated to the same quality as other software engineering documentation. | quality assurance | quality | S-01 page 135 | C-40 |
| R-0011 | Test documentation should be under software configuration management control. | quality assurance | quality | S-01 page 135 | C-50 |
| R-0012 | Testing should be performed following documented procedures using a clearly defined version of the SUT. | quality assurance | quality | S-01 page 137 | C-40 |
| R-0013 | Testing should be performed and documented clearly enough that another person could replicate the results. | quality assurance | quality | S-01 page 137 | C-41 |
| R-0014 | The testing environment should be compatible with the other software engineering tools used. | quality assurance | quality | S-01 page 137 | C-40 |
| R-0015 | Suitable knowledge-based repositories should be configured and managed so changes to requirements or design reach the tests. | quality assurance | quality | S-01 page 136 | C-50 |
| R-0016 | The resources spent on testing should be commensurate with the application's use and criticality. | management | quality | S-01 page 136 | C-47 |
| R-0017 | Monitor and control must define the required data and information and state how to obtain them. | quality assurance | quality | S-01 page 136 | C-40 |
| R-0018 | A decision must be made about how much testing is enough and when a test stage can be completed. | quality assurance | quality | S-01 page 136 | C-40 |
| R-0019 | Different testing aspects should be considered in shift-left developments. | quality assurance | quality | S-01 page 139 | C-40 |
| R-0020 | Security, privacy, communications and user or component interaction should be considered in IoT quality assessment. | quality assurance | quality | S-01 page 141 | C-52 |
| R-0021 | Testing needs to include very general processes and approaches applicable at system and process levels for avionics. | quality assurance | quality | S-01 page 141 | C-52 |
| R-0022 | Healthcare testing should ensure quality in secure and reliable data exchange, stable performance, privacy and safety. | quality assurance | quality | S-01 page 141 | C-52 |
| R-0023 | Performance testing of the legal data repository should also be done. | quality assurance | quality | S-01 page 141 | C-52 |
| R-0024 | The type of mobile application and its interactions need to be tested. | quality assurance | quality | S-01 page 141 | C-52 |
| R-0025 | Testing activity for embedded systems should assess functional and non-functional attributes of both software and hardware. | quality assurance | quality | S-01 page 141 | C-52 |
| R-0026 | The three main aspects of defining bugs and testing AI, ML or DL systems should be considered: required conditions, AI items, and testing activities. | quality assurance | quality | S-01 page 142 | C-52 |
| R-0027 | The set of requirements that should be satisfied determines the testing activity for each environment and organization. | quality assurance | quality | S-01 page 142 | C-40 |
| R-0028 | Different aspects of a blockchain-based system under test should be considered during testing, such as platform type, connections to other applications, and performance. | quality assurance | quality | S-01 page 143 | C-52 |
| R-0029 | Integration testing should be performed to check consistency when a blockchain works with various applications. | quality assurance | quality | S-01 page 143 | C-52 |
| R-0030 | Specific strategies to handle many transactions should be conceived to guarantee a satisfactory performance level. | quality assurance | quality | S-01 page 143 | C-52 |
| R-0031 | Qualitative and quantitative metrics, such as average transaction validation latency and security, should also be considered. | quality assurance | quality | S-01 page 143 | C-52 |
| R-0032 | Testing should also focus on compatibility and interoperability among heterogeneous cloud resources when different deployment models are used. | quality assurance | quality | S-01 page 143 | C-52 |
| R-0033 | Continuous integration and deployment force the testing process to include approaches for continuous test operation, injection, monitoring and reporting. | software engineers | pipeline | S-01 page 143 | C-05 |
| R-0034 | There is still a need for solutions that allow reuse of testing knowledge, architectures and code. | quality assurance | quality | S-01 page 143 | C-40 |
| R-0035 | Software engineering operations must manage any defects found, any changes to the system software and hardware over time, and any new user requirements. | operations engineers | operations | S-01 page 151 | C-65 |
| R-0036 | Nearly anything that impacts a software product directly or indirectly should be considered for representation as code. | operations engineers | operations | S-01 page 152 | C-54 |
| R-0037 | Software organizations should address staff recruitment for operations engineers, including validation of qualifications and identification of strengths and weaknesses. | operations engineers | operations | S-01 page 153 | C-64 |
| R-0038 | Software organizations should address resource planning for operations engineers, including staffing of new or expanded services and succession planning. | operations engineers | operations | S-01 page 153 | C-64 |
| R-0039 | Software organizations should address resource training and development for operations engineers, with timely delivery of operations services. | operations engineers | operations | S-01 page 154 | C-64 |
| R-0040 | Operations engineers should be trained in the relevant aspects of service management. | operations engineers | operations | S-01 page 154 | C-64 |
| R-0041 | A chronological training record should be maintained for each individual. | operations engineers | operations | S-01 page 154 | C-64 |
| R-0042 | Teamwork and leadership skills of operations engineers should be developed. | operations engineers | operations | S-01 page 154 | C-64 |
| R-0043 | Preparing for the operation requires defining an operation strategy. | operations engineers | operations | S-01 page 154 | C-53 |
| R-0044 | The operations engineer must install the software as part of its deployment. | operations engineers | operations | S-01 page 155 | C-54 |
| R-0045 | Software must be thoroughly tested before it is released. | quality assurance | quality | S-01 page 155 | C-40 |
| R-0046 | Testing must be automated as much as possible throughout the entire software process. | quality assurance | quality | S-01 page 155 | C-39 |
| R-0047 | Software engineers and operations engineers need to troubleshoot hardware and software incidents, including diagnostics, documentation, prioritization and impact assessment. | software engineers | operations | S-01 page 155 | C-59 |
| R-0048 | The operations engineer should replicate and verify problem reports by running the appropriate tests. | operations engineers | operations | S-01 page 155 | C-59 |
| R-0049 | Software engineering operations planning should comprise part of translating project requirements and developer and maintainer needs into services. | operations engineers | operations | S-01 page 156 | C-53 |
| R-0050 | Software engineering operations planning should provide a road map for directing progress. | operations engineers | operations | S-01 page 156 | C-53 |
| R-0051 | Suppliers must be well coordinated to ensure quality service. | operations engineers | operations | S-01 page 156 | C-66 |
| R-0052 | Software engineering operations planning should begin with the decision to develop a new product and should consider maintenance and operations requirements early. | operations engineers | operations | S-01 page 156 | C-53 |
| R-0053 | A concept document should be developed, followed by an operations and maintenance plan. | operations engineers | operations | S-01 page 156 | C-53 |
| R-0054 | The concept document and the operations and maintenance plan should address scope, adaptation of process and tools, organization, and cost estimates. | operations engineers | operations | S-01 page 156 | C-53 |
| R-0055 | Operations engineers should document their operations steps and tools, using any suitable form or medium. | operations engineers | operations | S-01 page 156 | C-64 |
| R-0056 | An operations plan or concept of operations should be prepared during software development and should specify how users request modifications and report problems. | consumers | operations | S-01 page 156 | C-53 |
| R-0057 | The operations organization must conduct business planning activities such as budgetary, financial and human resource planning. | operations engineers | operations | S-01 page 157 | C-53 |
| R-0058 | ISO/IEC/IEEE 20000-1 recommends that the operations plan addresses roles, contracts, staffing, capacity, finance, service acceptance criteria and measurable expected outcomes. | operations engineers | operations | S-01 page 157 | C-53 |
| R-0059 | Release or version planning requires that operations engineers identify target dates, agree release content, identify conflicts, assess release risk, develop a rollback plan, and inform all stakeholders. | operations engineers | operations | S-01 page 157 | C-56 |
| R-0060 | Engineers must ensure that the different environments are coherent and synchronized with the production environment. | operations engineers | operations | S-01 page 157 | C-54 |
| R-0061 | DevOps recommends that all environments are created automatically and built from a single code repository. | operations engineers | operations | S-01 page 158 | C-54 |
| R-0062 | All environments need to be built from the same code source. | operations engineers | operations | S-01 page 158 | C-54 |
| R-0063 | Service availability and continuity must be managed to ensure that customer commitments are met. | consumers | operations | S-01 page 158 | C-58 |
| R-0064 | Operations engineers will ensure that the proper infrastructure is planned, designed, implemented and tested. | operations engineers | operations | S-01 page 158 | C-61 |
| R-0065 | The current and expected business requirements for services should be understood. | operations engineers | operations | S-01 page 158 | C-53 |
| R-0066 | Business predictions and workload estimates should be translated into specific requirements and documented. | operations engineers | operations | S-01 page 158 | C-53 |
| R-0067 | The reaction to variations in workload or environment should be predictable. | operations engineers | operations | S-01 page 158 | C-61 |
| R-0068 | Data on components and resource utilization should be captured and analyzed. | operations engineers | operations | S-01 page 158 | C-61 |
| R-0069 | A capacity plan should be produced at a suitable frequency, at least annually. | operations engineers | operations | S-01 page 158 | C-61 |
| R-0070 | The capacity plan should document costed options for meeting business requirements and recommend solutions for the agreed service-level targets. | operations engineers | operations | S-01 page 158 | C-61 |
| R-0071 | The technical infrastructure and its current and projected capacities should be well understood. | operations engineers | operations | S-01 page 158 | C-61 |
| R-0072 | Backups, disaster recovery items and staff for service restoration should be quickly available after a major service failure. | operations engineers | operations | S-01 page 158 | C-60 |
| R-0073 | The need for successful recovery should influence which backup and recovery methods are used. | operations engineers | operations | S-01 page 158 | C-60 |
| R-0074 | Preparedness and regular tests of backup, disaster recovery and failover should be constantly rehearsed as production changes are made. | operations engineers | operations | S-01 page 159 | C-60 |
| R-0075 | Software engineers should understand that failure is inevitable. | software engineers | operations | S-01 page 159 | C-67 |
| R-0076 | Software applications should include failure-handling logic, which must be planned during development. | software engineers | operations | S-01 page 159 | C-67 |
| R-0077 | Operations engineers should strive to enforce the listed security controls. | operations engineers | security | S-01 page 159 | C-38 |
| R-0078 | Senior management should define the information security policy, communicate it to staff and customers, and act to ensure its implementation. | management | security | S-01 page 159 | C-38 |
| R-0079 | Information security management roles and responsibilities should be defined and allocated. | security roles | security | S-01 page 159 | C-19 |
| R-0080 | A representative of the management team should be assigned to monitor and maintain the effectiveness of the information security policy. | management | security | S-01 page 159 | C-38 |
| R-0081 | Staff with significant security roles should receive information security training. | security roles | security | S-01 page 159 | C-19 |
| R-0082 | All staff should be made aware of the information security policy. | security roles | security | S-01 page 159 | C-38 |
| R-0083 | Expert help on risk assessment and control implementation should be available. | security roles | security | S-01 page 159 | C-20 |
| R-0084 | Changes should not compromise the effective operation of controls. | operations engineers | operations | S-01 page 159 | C-65 |
| R-0085 | Information security incidents should be reported under incident management procedures, and a response should be initiated. | security roles | security | S-01 page 159 | C-38 |
| R-0086 | Software engineers ensure that new versions can be rolled back quickly and easily if a defect or degradation occurs. | software engineers | operations | S-01 page 160 | C-55 |
| R-0087 | DevOps calls for automating the different deployment steps. | operations engineers | operations | S-01 page 160 | C-54 |
| R-0088 | Proper analysis or post mortems must be conducted to find the source of an incident, and appropriate solutions must be implemented. | operations engineers | operations | S-01 page 161 | C-59 |
| R-0089 | Hope should not be a strategy for operations. | operations engineers | operations | S-01 page 161 | C-53 |
| R-0090 | Engineers should be informed about system quality and operational health with evidence, such as key performance indicators available in real time. | operations engineers | operations | S-01 page 161 | C-57 |
| R-0091 | Software applications or services must be architected to enable small, independent software deployments. | software engineers | operations | S-01 page 161 | C-67 |
| R-0092 | Operations engineers need to establish automated systems and tools for measurement, determine whether measures exist or need instrumentation, and select or develop a framework for coordination. | operations engineers | operations | S-01 page 162 | C-57 |
| R-0093 | The overall operations process needs to be automated as much as possible to prevent incidents and problems. | operations engineers | operations | S-01 page 162 | C-54 |
| R-0094 | Automated testing needs to be integrated throughout the process. | quality assurance | quality | S-01 page 162 | C-39 |
| R-0095 | Product telemetry should be implemented with analytics techniques to detect problems as early as possible. | operations engineers | operations | S-01 page 162 | C-57 |
| R-0096 | Data collected at all layers of the product stack must be collected and analyzed. | operations engineers | operations | S-01 page 162 | C-57 |
| R-0097 | Operations engineers must manage a number of risks. | operations engineers | operations | S-01 page 162 | C-65 |
| R-0098 | Operations engineers need to talk with product owners and software engineers to agree a risk tolerance level for alert triggers. | operations engineers | operations | S-01 page 162 | C-57 |
| R-0099 | Other perspectives are to choose a deployment process that suits the risk profile of a service and the risk of exposing private data. | operations engineers | operations | S-01 page 162 | C-56 |
| R-0100 | Software engineers should be aware that operations processes can be adapted to small organizations. | software engineers | operations | S-01 page 163 | C-53 |
| R-0101 | Testing must be automated as much as possible throughout the entire software delivery process. | quality assurance | quality | S-01 page 164 | C-39 |
| R-0102 | A testing strategy covering unit, integration, system and user acceptance tests must be defined. | quality assurance | quality | S-01 page 164 | C-40 |
| R-0103 | Tools to support and automate the test phases must be selected. | quality assurance | quality | S-01 page 164 | C-39 |
| R-0104 | Implementing monitoring solutions requires combining different techniques and tools to collect data at different layers. | operations engineers | operations | S-01 page 164 | C-57 |
| R-0105 | Maintainers must understand and use software artifacts from development, support them immediately, and progressively evolve and maintain them over time. | producers | operations | S-01 page 169 | C-71 |
| R-0106 | Maintainers should replicate or verify changes by planning and executing appropriate tests. | producers | operations | S-01 page 171 | C-71 |
| R-0107 | The change request must first be analyzed and translated into software terms. | producers | operations | S-01 page 172 | C-71 |
| R-0108 | Software engineers should strive to conduct impact analysis as cost-effectively as possible. | software engineers | operations | S-01 page 172 | C-71 |
| R-0109 | Maintainability should be specified, reviewed and controlled during software development activities. | software engineers | operations | S-01 page 172 | C-71 |
| R-0110 | Software engineering organizations must consider the advantages and disadvantages of each option for locating the maintenance function. | producers | operations | S-01 page 174 | C-71 |
| R-0111 | Software engineers must investigate three areas in depth when addressing technical debt. | software engineers | operations | S-01 page 173 | C-71 |
| R-0112 | Software engineers must understand the different categories of software maintenance. | software engineers | operations | S-01 page 175 | C-71 |
| R-0113 | The decision on how to organize maintenance should be made on a case-by-case basis. | management | operations | S-01 page 175 | C-71 |
| R-0114 | The source states that it is important that the organization delegates maintenance tasks to an experienced group or person and keeps quality documentation of maintenance tasks and all changes. | producers | operations | S-01 page 175 | C-71 |
| R-0115 | An estimate of software maintenance costs should be prepared early in the software planning process. | management | operations | S-01 page 175 | C-71 |
| R-0116 | The cost of software maintenance should be a function of the scope of maintenance activities. | management | operations | S-01 page 175 | C-71 |
| R-0117 | The cost estimating method should be described. | management | operations | S-01 page 176 | C-71 |
| R-0118 | Estimates should be amended as maintenance and development efforts progress. | management | operations | S-01 page 176 | C-71 |
| R-0119 | Historical measurement data should be used as inputs to estimate maintenance costs. | management | operations | S-01 page 176 | C-71 |
| R-0120 | Maintainers should determine which measures are appropriate for a specific organization, based on that organization's needs. | producers | operations | S-01 page 176 | C-71 |
| R-0121 | Maintainers must track requirements in their activities, as in development, and update documentation as baselines change. | producers | operations | S-01 page 177 | C-71 |
| R-0122 | When a maintainer uses a development process, the process must be tailored to meet specific needs. | producers | operations | S-01 page 178 | C-71 |
| R-0123 | Software maintenance planning should begin with the decision to develop a new software product and should consider quality objectives. | management | operations | S-01 page 178 | C-71 |
| R-0124 | A concept document should be developed, followed by a maintenance plan. | management | operations | S-01 page 178 | C-71 |
| R-0125 | The maintenance plan should address the scope, the adaptation of processes and tools, the maintenance organization, and the estimate of maintenance costs. | management | operations | S-01 page 178 | C-71 |
| R-0126 | The maintenance organization must conduct software maintenance business planning activities. | producers | operations | S-01 page 178 | C-71 |
| R-0127 | A software maintenance plan should be prepared during software development and should specify how users will request modifications and report problems. | producers | operations | S-01 page 179 | C-71 |
| R-0128 | Maintainers should have an effective quality program. | producers | quality | S-01 page 179 | C-47 |
| R-0129 | Maintainers must implement processes to support the continuous improvement of software maintenance processes. | producers | quality | S-01 page 179 | C-73 |
| R-0130 | The activities and techniques for SQA, V&V, reviews and audits must be selected together with all other processes to achieve the desired level of quality. | quality assurance | quality | S-01 page 179 | C-47 |
| R-0131 | It is also recommended that both software operations and maintenance adapt and use the output of the software development process, its techniques and deliverables. | producers | operations | S-01 page 179 | C-71 |
| R-0132 | Any change made to the software product and its underlying infrastructure must be controlled. | producers | pipeline | S-01 page 179 | C-16 |
| R-0133 | SCM procedures should provide for the verification, validation and audit of each step required to identify, authorize, implement and release the software product. | producers | pipeline | S-01 page 179 | C-16 |
| R-0134 | SCM activities should operationalize SCM process management and planning, identification, change control, status accounting, auditing, and release management and delivery. | producers | pipeline | S-01 page 185 | C-16 |
| R-0135 | Branching and merging strategies should be carefully planned and communicated. | software engineers | pipeline | S-01 page 187 | C-16 |
| R-0136 | SCM planning should consider the chosen software life cycle model, for example frequent build-test-deploy cycles. | software engineers | pipeline | S-01 page 188 | C-16 |
| R-0137 | SCM activities must be planned accordingly for frequent build-test-deploy cycles. | software engineers | pipeline | S-01 page 188 | C-16 |
| R-0138 | The following questions should be considered when tools are acquired: organization, tools, environment, legacy, financing, scope, ownership, future, change, branching and merging, integration, migration. | producers | pipeline | S-01 page 188 | C-16 |
| R-0139 | The SCM plan should include the sections introduction, SCM management, SCM activities, SCM schedules, SCM resources, and SCMP maintenance. | producers | pipeline | S-01 page 189 | C-16 |
| R-0140 | Care must be taken to keep surveillance focused on the insights gained from measurements. | producers | pipeline | S-01 page 190 | C-16 |
| R-0141 | A balance must be achieved between adequate visibility and a manageable number of controlled items when selecting SCIs. | producers | pipeline | S-01 page 190 | C-16 |
| R-0142 | Requirements and test cases should be linked with the code baselines developed. | software engineers | quality | S-01 page 192 | C-50 |
| R-0143 | The repository of binary objects should contain cryptographic hashes used to perform the physical configuration audit. | auditors and regulators | security | S-01 page 192 | C-34 |
| R-0144 | A change request application must include a CR form and a change certification form. | producers | pipeline | S-01 page 194 | C-16 |
| R-0145 | A CR form must describe the request and give the rationale for it. | producers | pipeline | S-01 page 194 | C-16 |
| R-0146 | The SCSA activity must be done by following the logical schemes defined for CIs, baselines and relationships. | producers | pipeline | S-01 page 195 | C-16 |
| R-0147 | Configuration status information should be secured where relevant. | producers | security | S-01 page 195 | C-34 |
| R-0148 | Each audit must be carefully planned. | auditors and regulators | pipeline | S-01 page 196 | C-16 |
| R-0149 | How to conduct the configuration review and the expected result must be described in the quality plan, or defined for the software configuration auditing activity if there is no quality plan. | auditors and regulators | pipeline | S-01 page 196 | C-16 |
| R-0150 | A configuration item must be reviewed whenever it must be reviewed during configuration auditing. | auditors and regulators | pipeline | S-01 page 196 | C-16 |
| R-0151 | Supporting tools and build instructions must be under SCM control to rebuild an exact copy of a previously built item. | software engineers | pipeline | S-01 page 197 | C-17 |
| R-0152 | Organizational software engineering managers should know the project management and software measurement knowledge of this KA. | management | quality | S-01 page 203 | C-72 |
| R-0153 | Organizational software engineering managers should also have some target domain knowledge. | management | quality | S-01 page 203 | C-72 |
| R-0154 | Software engineers should have a sound understanding of the management aspects unique to software projects. | software engineers | quality | S-01 page 204 | C-72 |
| R-0155 | Software engineers should also have some knowledge of general management aspects. | software engineers | quality | S-01 page 204 | C-72 |
| R-0156 | Software engineers must use both measurement and management to be effective. | software engineers | quality | S-01 page 205 | C-72 |
| R-0157 | The imperatives of delivery speed and frequent upgrades should be balanced with risk management activities. | management | quality | S-01 page 206 | C-72 |
| R-0158 | Activities should include software requirements review: elicitation, analysis, specification and validation. | software engineers | quality | S-01 page 207 | C-68 |
| R-0159 | Methods and techniques should be selected and applied with regard to the various stakeholder perspectives. | management | quality | S-01 page 207 | C-72 |
| R-0160 | An initial project and product scope statement, deliverables, duration constraints and resource estimate should be prepared. | management | quality | S-01 page 207 | C-72 |
| R-0161 | Stakeholders should agree on how requirements and scope will be reviewed and revised. | management | quality | S-01 page 208 | C-68 |
| R-0162 | Scope and requirements can and should be revisited at predetermined points. | management | quality | S-01 page 208 | C-68 |
| R-0163 | Forward or backward traceability and risk analysis should be used to assess accepted changes. | management | quality | S-01 page 208 | C-68 |
| R-0164 | Engineers should consider all configuration items as tasks to have under control while developing the work breakdown structure. | software engineers | pipeline | S-01 page 208 | C-16 |
| R-0165 | Selecting an appropriate SDLC model, possibly tailored, should be a key step in software project planning. | management | quality | S-01 page 208 | C-73 |
| R-0166 | Risk assessment should be an element of initial project planning in all SDLCs. | management | quality | S-01 page 208 | C-72 |
| R-0167 | The risk profile should be discussed and accepted by all relevant stakeholders. | management | quality | S-01 page 208 | C-72 |
| R-0168 | Software quality management processes should be planned along with project planning. | management | quality | S-01 page 208 | C-47 |
| R-0169 | Planning should establish procedures and responsibilities for SQA, verification and validation, reviews and audits. | management | quality | S-01 page 208 | C-47 |
| R-0170 | Processes and responsibilities for ongoing review and revision of the project plan should be clearly stated and agreed. | management | quality | S-01 page 208 | C-72 |
| R-0171 | Each project activity work product should be identified and characterized. | management | quality | S-01 page 209 | C-72 |
| R-0172 | Reuse of existing software components and off-the-shelf products should be evaluated. | management | quality | S-01 page 209 | C-72 |
| R-0173 | Software procurement and use of third parties should be planned and suppliers selected. | management | quality | S-01 page 209 | C-72 |
| R-0174 | Relevant methods and tools should be selected as part of planning. | software engineers | quality | S-01 page 209 | C-70 |
| R-0175 | Automated tools used throughout the project should be planned for and acquired. | management | quality | S-01 page 209 | C-72 |
| R-0176 | Many tools should be selected primarily on technical considerations. | management | quality | S-01 page 209 | C-72 |
| R-0177 | Software project managers should use multiple estimation approaches and reconcile the differences among the estimates. | management | quality | S-01 page 209 | C-72 |
| R-0178 | The estimate of effort, schedule and cost should be negotiated and revised among affected stakeholders until consensus is reached. | management | quality | S-01 page 210 | C-72 |
| R-0179 | Project managers should constantly monitor stakeholder requirements and changes and analyse their impact on cost and schedule. | management | quality | S-01 page 210 | C-72 |
| R-0180 | Risk management should be done not only at the beginning of a project but also at periodic intervals. | management | quality | S-01 page 210 | C-72 |
| R-0181 | Particular attention should be paid to managing risks related to software quality requirements such as safety or security. | management | security | S-01 page 210 | C-20 |
| R-0182 | Equipment, facilities and people should be allocated to the identified tasks. | management | quality | S-01 page 210 | C-72 |
| R-0183 | Where plans are used, plans should be developed and managed when change is expected. | management | quality | S-01 page 211 | C-72 |
| R-0184 | The magnitude of the planning effort should be determined partly by the risk of not developing the plan. | management | quality | S-01 page 211 | C-72 |
| R-0185 | The management of the project plan should itself be planned. | management | quality | S-01 page 211 | C-72 |
| R-0186 | Plans and processes should be systematically monitored, reviewed, reported and, when appropriate, revised. | management | quality | S-01 page 211 | C-72 |
| R-0187 | Plans associated with supporting processes should also be managed. | management | quality | S-01 page 211 | C-72 |
| R-0188 | Reporting, monitoring and control should fit within the selected SDLC and the realities of the project. | management | quality | S-01 page 211 | C-72 |
| R-0189 | Plans should account for the various artifacts that will be used to manage the project. | management | quality | S-01 page 211 | C-72 |
| R-0190 | In adaptive programs, the emphasis should be on selecting and retaining project information useful for control and future projects. | management | quality | S-01 page 211 | C-72 |
| R-0191 | Software quality requirements for a project and its work products should be identified, quantitatively and qualitatively. | quality assurance | quality | S-01 page 211 | C-45 |
| R-0192 | Thresholds for acceptable quality measurements should be set for each software quality requirement based on stakeholder needs. | management | quality | S-01 page 211 | C-45 |
| R-0193 | Procedures for ongoing SQA, quality improvement, and verification and validation of the deliverable should be specified during quality planning. | quality assurance | quality | S-01 page 211 | C-47 |
| R-0194 | Throughout enactment there should be a focus on adherence to the selected SDLC processes. | management | quality | S-01 page 212 | C-73 |
| R-0195 | Project activities should follow the project plan and supporting plans. | management | quality | S-01 page 212 | C-72 |
| R-0196 | Regardless of how components are obtained, verification, integration and validation of components should be performed. | producers | security | S-01 page 212 | C-28 |
| R-0197 | Organizations should consider introducing technical or procedural controls to minimize risk from unfiltered access to external library repositories. | producers | security | S-01 page 212 | C-28 |
| R-0198 | After an agreement is in place, project execution in compliance with its terms should be managed. | management | quality | S-01 page 213 | C-72 |
| R-0199 | The measurement process should be enacted during the software project to ensure relevant and useful data is collected. | management | quality | S-01 page 213 | C-72 |
| R-0200 | Adherence to the scope, project plan and related plans should be assessed continually and at predetermined intervals. | management | quality | S-01 page 213 | C-72 |
| R-0201 | Outputs and completion criteria for each task should be assessed. | management | quality | S-01 page 213 | C-72 |
| R-0202 | Deliverables should be evaluated for their required characteristics. | management | quality | S-01 page 213 | C-72 |
| R-0203 | Effort expenditure, schedule adherence, costs to date and resource use should be analysed. | management | quality | S-01 page 213 | C-72 |
| R-0204 | The project risk profile should be revisited. | management | quality | S-01 page 213 | C-72 |
| R-0205 | Adherence to software quality requirements should be evaluated. | quality assurance | quality | S-01 page 213 | C-47 |
| R-0206 | Measurement data should be analysed. | management | quality | S-01 page 213 | C-72 |
| R-0207 | Variance analysis should be conducted to determine deviation of actual from expected outcomes. | management | quality | S-01 page 213 | C-72 |
| R-0208 | Outlier identification and analysis of quality and other measurement data should be performed. | quality assurance | quality | S-01 page 213 | C-49 |
| R-0209 | Risk exposures should be recalculated. | management | quality | S-01 page 213 | C-72 |
| R-0210 | Outcomes should be reported as necessary or when thresholds have been exceeded. | management | quality | S-01 page 213 | C-72 |
| R-0211 | The software development team should adhere to software configuration control and software configuration management procedures. | software engineers | pipeline | S-01 page 214 | C-16 |
| R-0212 | Decisions should be documented and communicated to all relevant parties. | management | quality | S-01 page 214 | C-72 |
| R-0213 | Plans should be revisited and revised when necessary. | management | quality | S-01 page 214 | C-72 |
| R-0214 | Relevant data should be recorded. | management | quality | S-01 page 214 | C-72 |
| R-0215 | Requirements changes should be identified and appropriate actions should be taken (fragment partly lost in conversion). | software engineers | quality | S-01 page 214 | C-68 |
| R-0216 | Progress to date should be reported at specified and agreed-upon times, within the organization and to external stakeholders. | management | quality | S-01 page 214 | C-72 |
| R-0217 | Reports should focus on the information needs of the target audience. | management | quality | S-01 page 214 | C-72 |
| R-0218 | Progress toward stakeholder satisfaction should be assessed periodically. | management | quality | S-01 page 214 | C-72 |
| R-0219 | Progress should be assessed on achieving a major milestone or completing an iterative cycle. | management | quality | S-01 page 214 | C-72 |
| R-0220 | Overall progress toward objectives and stakeholder requirements should be evaluated at prespecified times and as needed. | management | quality | S-01 page 214 | C-72 |
| R-0221 | The various project methods, tools and techniques should be evaluated for effectiveness and appropriateness. | management | quality | S-01 page 214 | C-73 |
| R-0222 | The project process should be systematically and periodically assessed for relevance, utility and efficacy. | management | quality | S-01 page 214 | C-73 |
| R-0223 | Where appropriate, project changes should be made and managed. | management | quality | S-01 page 214 | C-72 |
| R-0224 | Effectiveness of the software process, personnel, tools and methods should be assessed regularly. | management | quality | S-01 page 214 | C-73 |
| R-0225 | Closure processes should involve relevant stakeholders and document relevant stakeholders acceptance. | management | quality | S-01 page 215 | C-72 |
| R-0226 | Any known problems should be documented at closure. | management | quality | S-01 page 215 | C-72 |
| R-0227 | Project materials should be archived in accordance with stakeholder agreed-upon rules. | management | quality | S-01 page 215 | C-72 |
| R-0228 | The organization measurement database should be updated with relevant project data. | management | quality | S-01 page 215 | C-72 |
| R-0229 | A project, phase or iteration retrospective analysis should be undertaken. | management | quality | S-01 page 215 | C-73 |
| R-0230 | Lessons learned should be drawn from the project and fed into organizational learning. | management | quality | S-01 page 215 | C-73 |
| R-0231 | Each measurement endeavor should be guided by organizational objectives. | management | quality | S-01 page 215 | C-72 |
| R-0232 | The project team should establish the organizational unit to which each measurement requirement is applied. | management | quality | S-01 page 215 | C-72 |
| R-0233 | The temporal scope of the measurement effort should be considered. | management | quality | S-01 page 215 | C-72 |
| R-0234 | The commitment to measurement should be formally established, communicated and supported by resources. | management | quality | S-01 page 215 | C-72 |
| R-0235 | Adequate funding, training, tools and support should be allocated to conduct the measurement process. | management | quality | S-01 page 216 | C-72 |
| R-0236 | The appropriate stakeholders should review and approve the measurement plan. | management | quality | S-01 page 216 | C-72 |
| R-0237 | Criteria for reviewing measurement artifacts should be established at the organizational unit level or higher and used as the basis for reviews. | management | quality | S-01 page 216 | C-72 |
| R-0238 | Criteria for reviewing measurement artifacts should consider experience, resource availability and potential disruption. | management | quality | S-01 page 216 | C-72 |
| R-0239 | Stakeholders should identify, prioritize, document, communicate and review information needs. | management | quality | S-01 page 216 | C-72 |
| R-0240 | The technical and business objectives of the organizational unit should influence evaluation criteria. | management | quality | S-01 page 216 | C-72 |
| R-0241 | Measurement procedures should be integrated into the software processes they measure. | management | quality | S-01 page 216 | C-72 |
| R-0242 | Data providers and measurement users should participate in reviewing the data. | management | quality | S-01 page 217 | C-72 |
| R-0243 | Measurement data should be collected and analysed. | management | quality | S-01 page 217 | C-72 |
| R-0244 | Data should be collected, verified and stored. | management | quality | S-01 page 217 | C-72 |
| R-0245 | Software processes must be selected, adapted and applied as appropriate for each project and each organizational context. | management | quality | S-01 page 222 | C-73 |
| R-0246 | It is essential that software engineering process management is supported by empirical measurement. | management | quality | S-01 page 222 | C-73 |
| R-0247 | A life cycle should be defined following engineering principles that guide engineering as a discipline. | management | quality | S-01 page 224 | C-73 |
| R-0248 | The process specification should be useful to humans so that they can communicate with one another. | software engineers | quality | S-01 page 224 | C-73 |
| R-0249 | The life cycle specification should be easy to understand and correct. | software engineers | quality | S-01 page 224 | C-73 |
| R-0250 | It is important to make sure that metrics and measure definitions can produce realistic process and product estimations and measurements, and that the level of precision and uncertainty is defined. | management | quality | S-01 page 228 | C-72 |
| R-0251 | Project process and product measurements should always provide accurate information about what is happening while the life cycle process is executed. | management | quality | S-01 pages 228 to 229 | C-72 |
| R-0252 | Developers must monitor the software engineering process execution, assess whether the process objectives are met, and assess risks. | software engineers | quality | S-01 page 229 | C-72 |
| R-0253 | A reflection should take place on the overall approach when estimations and measurements are uncertain. | management | quality | S-01 page 229 | C-72 |
| R-0254 | Tools will, ideally, have to support the process methods and be integrated with them. | software engineers | quality | S-01 page 229 | C-73 |
| R-0255 | The configuration management tool and the testing tool will have to be integrated. | software engineers | quality | S-01 page 229 | C-73 |
| R-0256 | The Agile Manifesto signatories claimed that the process should be open to change; this is reported as their claim, not as a requirement of the source. | software engineers | quality | S-01 page 226 | C-73 |
| R-0257 | Business needs, as identified by project stakeholders, should and do drive the choice of software engineering method. | management | quality | S-01 page 243 | C-73 |
| R-0258 | Release managers need to monitor the development process and the promotion schedule for each release. | operations engineers | operations | S-01 page 243 | C-62 |
| R-0259 | Assumptions made when simplifying a model should also be captured in the model. | software engineers | quality | S-01 page 235 | C-76 |
| R-0260 | The model should be checked for documented assumptions. | software engineers | quality | S-01 page 236 | C-76 |
| R-0261 | Analysis of constructed models is needed to ensure that the models are complete, consistent and correct. | software engineers | quality | S-01 page 237 | C-76 |
| R-0262 | Traceability relationships must be mapped and controlled to demonstrate the consistency of software requirements with the software model and work products. | software engineers | quality | S-01 page 238 | C-68 |
| R-0263 | Formal verification requires a rigorously specified model of the software and its operational environment. | software engineers | quality | S-01 page 241 | C-76 |
| R-0264 | Process quality must be made explicit. | quality assurance | quality | S-01 page 247 | C-47 |
| R-0265 | Agreeing on software quality and communicating it to software engineers requires that quality aspects be formally defined and communicated. | software engineers | quality | S-01 page 248 | C-45 |
| R-0266 | Software engineers should understand software quality concepts, characteristics and values and apply them to development, maintenance and operation. | software engineers | quality | S-01 page 248 | C-45 |
| R-0267 | The software requirements are expected to define the required software quality attributes. | software engineers | quality | S-01 page 248 | C-45 |
| R-0268 | Software quality should be planned early and assessed at many milestones during the software life cycle. | quality assurance | quality | S-01 page 248 | C-47 |
| R-0269 | Software engineers are expected to share a commitment to software quality in the context of their industry and culture. | software engineers | quality | S-01 page 248 | C-74 |
| R-0270 | Software engineers should use the meaning of error and defect given by their standards. | software engineers | quality | S-01 page 248 | C-49 |
| R-0271 | Software engineers should inform their administration of the risks they take when not fully committed to quality. | software engineers | quality | S-01 page 249 | C-74 |
| R-0272 | Software engineers should seek the optimal cost of software quality, the minimal total cost for a specified quality level. | software engineers | quality | S-01 page 249 | C-75 |
| R-0273 | Software engineers should know the key software engineering standards that apply to their specific industry. | software engineers | quality | S-01 page 249 | C-74 |
| R-0274 | Software engineers and their managers must understand threats and issues and develop the skills to anticipate and prevent accidents. | software engineers | quality | S-01 page 250 | C-74 |
| R-0275 | Safety-critical software requires the use of systematic methods and tools to ensure its high level of quality. | quality assurance | quality | S-01 page 250 | C-47 |
| R-0276 | A quality management system requires policies, procedures and processes so that everyone involved understands what is expected. | management | quality | S-01 page 251 | C-47 |
| R-0277 | For a quality management system to be effective, management support is imperative. | management | quality | S-01 page 251 | C-47 |
| R-0278 | Management sponsorship should be solicited frequently during software project review. | management | quality | S-01 page 251 | C-47 |
| R-0279 | The software organization must commit to quality by establishing its quality management system. | producers | quality | S-01 page 252 | C-47 |
| R-0280 | Responsibility and authority for the quality management system requires that they be assigned and independent of current project management teams. | management | quality | S-01 page 252 | C-47 |
| R-0281 | Software engineers should promote the use of formally approved processes and procedures that implement the quality policy. | software engineers | quality | S-01 page 252 | C-73 |
| R-0282 | Processes of a quality management system should be documented with their users in mind and identify where quality controls are to be verified. | quality assurance | quality | S-01 pages 252–253 | C-47 |
| R-0283 | The software quality management process is tasked with ensuring that report results are accurate and acted upon. | quality assurance | quality | S-01 page 252 | C-47 |
| R-0284 | Software engineers will periodically gather and analyze quality assurance evaluation results. | software engineers | quality | S-01 page 253 | C-49 |
| R-0285 | Software engineers should establish a meaningful defect classification taxonomy. | software engineers | quality | S-01 page 254 | C-49 |
| R-0286 | It is important that corrective actions be documented and submitted when quality management objectives are not met. | quality assurance | quality | S-01 page 254 | C-49 |
| R-0287 | Project participants require a way of reporting software process and tool problems to an independent organization. | software engineers | quality | S-01 page 254 | C-47 |
| R-0288 | The SQA plan should not conflict with the software configuration management plan or any other project planning artifact. | quality assurance | quality | S-01 page 255 | C-47 |
| R-0289 | The SQA plan and the SCM process should be considered complementary activities. | quality assurance | quality | S-01 page 255 | C-47 |
| R-0290 | SQA activities listed in IEEE 730 should be conducted early in a software project life cycle. | quality assurance | quality | S-01 page 255 | C-47 |
| R-0291 | Software engineers should be aware of the need to plan and execute SQA activities at certain project milestones and keep records of their execution. | software engineers | quality | S-01 pages 255–256 | C-47 |
| R-0292 | Software engineers are responsible for eliciting quality requirements that might not be explicit at the outset. | software engineers | quality | S-01 page 256 | C-68 |
| R-0293 | Software engineers should understand how to define quality requirements and quality targets so they can be measured at acceptance. | software engineers | quality | S-01 page 256 | C-45 |
| R-0294 | Software engineers must keep quality requirements in mind during project planning. | software engineers | quality | S-01 page 256 | C-45 |
| R-0295 | Software engineers must anticipate potential additional development costs if safety, security and dependability attributes are important. | software engineers | quality | S-01 page 256 | C-75 |
| R-0296 | Software engineers should identify which work products and software artifacts require configuration management. | software engineers | pipeline | S-01 page 256 | C-16 |
| R-0297 | Software engineers should be familiar with source code versioning processes. | software engineers | pipeline | S-01 page 256 | C-01 |
| R-0298 | Software engineers should know how to operate the version control tool kit. | software engineers | pipeline | S-01 page 256 | C-01 |
| R-0299 | Software engineers should know the many software characteristics that can be planned, implemented and measured during software construction. | software engineers | quality | S-01 page 256 | C-70 |
| R-0300 | Software engineers should know that certain quality characteristics have conflicting impacts. | software engineers | quality | S-01 page 256 | C-45 |
| R-0301 | Sound engineering practice requires that intermediate work products relevant to quality be evaluated using work product reviews and inspections. | quality assurance | quality | S-01 page 257 | C-48 |
| R-0302 | The verification process and the validation process should begin early in development or maintenance. | quality assurance | quality | S-01 page 257 | C-47 |
| R-0303 | Software engineers should identify the product integrity level and ensure the minimum V&V tasks are assigned for key product features. | software engineers | quality | S-01 page 257 | C-47 |
| R-0304 | Software engineers should choose and apply the proper V&V task depending on the software integrity level. | software engineers | quality | S-01 page 257 | C-47 |
| R-0305 | A software quality engineering team, for critical systems, should particularly be involved in qualifying software products before delivery. | quality assurance | quality | S-01 page 258 | C-47 |
| R-0306 | Software engineers should plan the testing activities, including levels, techniques, measures and tools. | software engineers | quality | S-01 page 258 | C-40 |
| R-0307 | Software engineers should plan, execute and record the many testing and retesting activities listed in IEEE 730. | software engineers | quality | S-01 page 258 | C-40 |
| R-0308 | IEEE 730 recommends that testing completion criteria be set. | quality assurance | quality | S-01 page 258 | C-40 |
| R-0309 | Technical reviews and audits should be planned, approved and conducted. | quality assurance | quality | S-01 page 259 | C-48 |
| R-0310 | Reviews should be part of the software engineering culture and should be planned, executed and documented during the software life cycle. | quality assurance | quality | S-01 page 259 | C-48 |
| R-0311 | Software engineers should be knowledgeable about the related disciplines listed in the Guide. | software engineers | quality | S-01 page 40 | C-77 |
| R-0312 | A software project must implement requirements imposed by cross-cutting disciplines such as dependability and safety. | software engineers | quality | S-01 page 39 | C-77 |
| R-0313 | Competent, capable software engineers should be equipped with the generally accepted knowledge for potential application. | software engineers | quality | S-01 page 41 | C-77 |
| R-0314 | Appropriate selection of generally accepted knowledge should be included in the study material for certification and licensing examinations. | software engineers | quality | S-01 page 41 | C-77 |
| R-0315 | Generally accepted knowledge should not be applied uniformly to all software engineering endeavors; each project's needs determine what to apply. | software engineers | quality | S-01 page 41 | C-77 |
| R-0316 | To design security into software, one must consider every development life cycle stage. | security roles | security | S-01 page 264 | C-38 |
| R-0317 | Security must be considered during software maintenance, because faults can be introduced then. | security roles | security | S-01 page 264 | C-38 |
| R-0318 | Software engineers should define the security properties of their software and maintain them throughout the software development life cycle. | software engineers | security | S-01 page 264 | C-18 |
| R-0319 | Software engineers should consider the mitigation of cyber threats as part of software development. | software engineers | security | S-01 page 265 | C-38 |
| R-0320 | Project managers need to raise software security from a technical concern to an enterprise issue. | management | security | S-01 page 265 | C-20 |
| R-0321 | Organizations should use an information security management system to assess risks continually and deploy an IT team to monitor them. | management | security | S-01 page 266 | C-38 |
| R-0322 | Agile teams need to understand and adopt security practices and take more responsibility for system security. | software engineers | security | S-01 page 266 | C-19 |
| R-0323 | Security professionals must learn to accept change, work faster and more iteratively, and manage security risks in incremental terms. | security roles | security | S-01 page 266 | C-19 |
| R-0324 | Security needs to become an enabler instead of a blocker. | security roles | security | S-01 page 266 | C-38 |
| R-0325 | Security must be built into software engineering to ensure software security. | software engineers | security | S-01 page 266 | C-38 |
| R-0326 | Traceability of security requirements through the development process is important. | software engineers | security | S-01 page 266 | C-18 |
| R-0327 | Developers conduct threat modeling to show how a system can be attacked and to specify the security design for mitigation. | software engineers | security | S-01 page 267 | C-27 |
| R-0328 | It is important to select cryptographic algorithms and key material with care, and to manage how material is created, distributed and managed. | software engineers | security | S-01 page 267 | C-38 |
| R-0329 | Structure the process so that sections needing extra privileges are small modules that do only the privileged tasks. | software engineers | security | S-01 page 267 | C-29 |
| R-0330 | Validate the assumptions in the program, or document them for installers and maintainers if validation is not possible. | software engineers | security | S-01 page 267 | C-29 |
| R-0331 | The program must not share objects in memory with any other program. | software engineers | security | S-01 page 267 | C-29 |
| R-0332 | Check every function error status. | software engineers | security | S-01 page 267 | C-29 |
| R-0333 | Do not recover from an error unless neither its cause nor its effects affect security. | software engineers | security | S-01 page 267 | C-29 |
| R-0334 | After an unrecovered error the program should restore the software state from before the process began and then terminate. | software engineers | security | S-01 page 267 | C-29 |
| R-0335 | Validate input. | software engineers | security | S-01 page 268 | C-29 |
| R-0336 | Heed compiler warnings. | software engineers | security | S-01 page 268 | C-29 |
| R-0337 | Architect and design for security policies. | software engineers | security | S-01 page 268 | C-27 |
| R-0338 | Keep the design simple. | software engineers | security | S-01 page 268 | C-27 |
| R-0339 | Use default deny. | software engineers | security | S-01 page 268 | C-30 |
| R-0340 | Apply the principle of least privilege. | software engineers | security | S-01 page 268 | C-29 |
| R-0341 | Sanitize data sent to other software. | software engineers | security | S-01 page 268 | C-29 |
| R-0342 | Practice defense in depth. | software engineers | security | S-01 page 268 | C-29 |
| R-0343 | Use effective quality assurance techniques. | software engineers | quality | S-01 page 268 | C-47 |
| R-0344 | Adopt a software construction security standard. | software engineers | security | S-01 page 268 | C-29 |
| R-0345 | Engage security experts skilled in the application domain to perform dynamic security tests. | security roles | security | S-01 page 268 | C-26 |
| R-0346 | Security tests should always be conducted within legal boundaries and with proper authorization. | security roles | security | S-01 page 268 | C-26 |
| R-0347 | The expertise of security professionals is required to operate and configure static analysis tools and to verify their results. | security roles | security | S-01 page 268 | C-24 |
| R-0348 | Comprehensive risk and threat analysis methods and management tools for IoT platforms are required. | security roles | security | S-01 page 269 | C-27 |
| R-0349 | Software engineers must handle unique engineering problems to produce software with known characteristics and reliability. | software engineers | quality | S-01 page 274 | C-76 |
| R-0350 | Software engineers need the proper knowledge, skills, training and experience for professional practice. | software engineers | quality | S-01 page 274 | C-74 |
| R-0351 | Software engineers maintain professional practice by following generally accepted practices, standards and guidelines of the applicable professional society. | software engineers | quality | S-01 page 274 | C-74 |
| R-0352 | Software engineers shall commit to making the analysis, specification, design, development, testing and maintenance of software a beneficial and respected profession. | software engineers | quality | S-01 page 277 | C-74 |
| R-0353 | Software engineers shall adhere to the ten principles of the IEEE Code of Ethics. | software engineers | quality | S-01 page 277 | C-74 |
| R-0354 | Engineers are responsible for continuing their studies to stay current in their professional practice. | software engineers | quality | S-01 page 277 | C-74 |
| R-0355 | Software engineers must consult attorneys who specialize in the type and jurisdiction of any identified legal issue. | software engineers | quality | S-01 page 279 | C-74 |
| R-0356 | Software engineers must operate within local, national and international legal frameworks. | software engineers | quality | S-01 page 280 | C-74 |
| R-0357 | Software engineers must know the legal requirements for registration and licensing, contractual agreements and noncontractual liability. | software engineers | quality | S-01 page 280 | C-74 |
| R-0358 | All software professionals must be aware of legal restrictions on import, export and re-export. | software engineers | quality | S-01 page 280 | C-74 |
| R-0359 | Trade experts should be consulted for detailed compliance guidance. | software engineers | quality | S-01 page 280 | C-74 |
| R-0360 | It is crucial that engineers adhere to standards and generally accepted practices to protect against malpractice allegations. | software engineers | quality | S-01 page 280 | C-74 |
| R-0361 | The software engineer has a professional obligation to consider the threat of cybercrime and how the system security protects software and user information. | software engineers | security | S-01 pages 280-281 | C-38 |
| R-0362 | Software engineers should avoid certifying or approving unacceptable products, disclosing confidential information, and falsifying facts or data. | software engineers | quality | S-01 page 281 | C-74 |
| R-0363 | Software engineers should be responsible for their actions and transparent with users, and should not manipulate users with deceptive interface patterns. | software engineers | quality | S-01 page 281 | C-74 |
| R-0364 | Software engineers should know that data privacy is a key legal requirement in many countries. | software engineers | security | S-01 page 281 | C-38 |
| R-0365 | Software engineers and their managers should provide internal documentation of requirements, design, tools, tests, methods and problems encountered. | software engineers | quality | S-01 page 281 | C-74 |
| R-0366 | Documentation for external stakeholders should describe whether the software meets needs, safe and unsafe use, how to protect sensitive information, and clear warnings and critical procedures. | consumers | security | S-01 page 281 | C-37 |
| R-0367 | Software engineers should provide documentation of functional specifications, design, test suite and operating environment if the customer acquires the source code or the right to modify it. | consumers | security | S-01 pages 281-282 | C-37 |
| R-0368 | Documents should be kept for at least as long as the product life cycle or the period required by organizational or regulatory requirements. | management | quality | S-01 page 282 | C-72 |
| R-0369 | A software engineer must conduct trade-off analysis ethically. | software engineers | quality | S-01 page 282 | C-75 |
| R-0370 | A software engineer should be objective and impartial when choosing comparison criteria and weights. | software engineers | quality | S-01 page 282 | C-75 |
| R-0371 | Any conflict of interest must be disclosed up front. | software engineers | quality | S-01 page 282 | C-74 |
| R-0372 | A software engineer should interact cooperatively and constructively with others to determine and meet needs and expectations. | software engineers | quality | S-01 page 282 | C-74 |
| R-0373 | Software engineers must work with others, inside engineering teams and with customers, the public, regulators and other stakeholders. | software engineers | quality | S-01 page 282 | C-74 |
| R-0374 | Software engineers must be able to work in multidisciplinary environments and varied application domains. | software engineers | quality | S-01 page 283 | C-74 |
| R-0375 | Stakeholders should provide support, information and feedback at all stages of the software life cycle. | consumers | quality | S-01 page 283 | C-74 |
| R-0376 | In the early stages it is critical to identify all stakeholders and discover how the product will affect them. | software engineers | quality | S-01 page 283 | C-68 |
| R-0377 | It is vital to maintain open and productive communication with stakeholders during the product life cycle. | software engineers | quality | S-01 page 284 | C-74 |
| R-0378 | Software engineers must deal with and resolve uncertainty and ambiguity while providing services and developing products. | software engineers | quality | S-01 page 284 | C-74 |
| R-0379 | The software engineer must reduce or eliminate any lack of clarity that is an obstacle to the work. | software engineers | quality | S-01 page 284 | C-74 |
| R-0380 | Team members must embrace tolerance of different cultural and social norms. | software engineers | quality | S-01 page 284 | C-74 |
| R-0381 | A software engineer must communicate well, both orally and in writing. | software engineers | quality | S-01 page 284 | C-74 |
| R-0382 | Engineers must establish clear communication with customers, supervisors, coworkers and suppliers. | software engineers | quality | S-01 page 284 | C-74 |
| R-0383 | Software engineers must be able to read and understand technical material. | software engineers | quality | S-01 page 285 | C-74 |
| R-0384 | Engineers who modify, extend or rewrite software must understand both its implementation and its design. | software engineers | operations | S-01 page 285 | C-71 |
| R-0385 | Written software engineering products must be accessible, understandable and relevant to their intended audience. | software engineers | quality | S-01 page 285 | C-74 |
| R-0386 | Stakeholders must be consulted, decisions must be made, and plans must be generated during the engineering effort. | management | quality | S-01 page 285 | C-72 |
| R-0387 | Knowledge about the product needs to be archived in slides, write-ups, white papers and other material. | software engineers | quality | S-01 page 286 | C-74 |
| R-0388 | Software engineering must be value-based. | management | quality | S-01 page 288 | C-75 |
| R-0389 | Software engineering decisions must also consider relevant unquantifiable criteria. | management | quality | S-01 page 289 | C-75 |
| R-0390 | The software engineer needs to close the loop on estimates by comparing them with actual outcomes. | management | quality | S-01 page 294 | C-72 |
| R-0391 | Software engineers must use their best judgment in deciding when they have enough candidates. | software engineers | quality | S-01 page 293 | C-75 |
| R-0392 | As much as possible, each criterion should be expressed objectively. | management | quality | S-01 page 293 | C-75 |
| R-0393 | When a selection criterion involves money, each alternative must be judged from the same viewpoint. | management | quality | S-01 page 296 | C-75 |
| R-0394 | Use the same basis for comparison, planning horizon and kinds of costs for all alternatives. | management | quality | S-01 page 296 | C-75 |
| R-0395 | The do-nothing alternative should be considered in most, but not all, situations. | management | quality | S-01 page 291 | C-75 |
| R-0396 | The greater the consequences of a wrong decision, the more selection criteria need to be considered. | management | quality | S-01 page 293 | C-75 |
| R-0397 | When the consequences of a wrong decision are significant, all steps should be completed thoroughly and carefully. | management | quality | S-01 page 292 | C-75 |
| R-0398 | Alternatives should be chosen only if their rate of return is at least the minimum acceptable rate of return. | management | quality | S-01 page 293 | C-75 |
| R-0399 | Software engineers must consider control of the organization part of their job by aligning software with business goals. | software engineers | quality | S-01 page 304 | C-75 |
| R-0400 | Software engineers must be conscious of the software as a driver of business accounts. | software engineers | quality | S-01 page 303 | C-75 |
| R-0401 | Estimates should be realistic and quantitative for cost, schedule, personnel, quality and outcomes (Code of Ethics item 3.09). | management | quality | S-01 page 301 | C-72 |
| R-0402 | Indicators must be normalized and standardized to operate correctly. | management | quality | S-01 page 298 | C-75 |
| R-0403 | All criteria must be considered to decide which software products should be developed for the client organization. | management | quality | S-01 page 300 | C-75 |
| R-0404 | Software engineering economics should be concerned with all SPLC activities, including those after the initial release. | software engineers | quality | S-01 page 306 | C-75 |
| R-0405 | The planning and controlling of costs should always be included in costing. | management | quality | S-01 page 306 | C-75 |
| R-0406 | An SPLC should include risk management and synchronization with different suppliers, and provide auditable decision-making information. | management | quality | S-01 page 305 | C-72 |
| R-0407 | Relevant stakeholders and the decision management strategy should be identified in high-consequence decisions. | management | quality | S-01 page 292 | C-75 |
| R-0408 | Professional software engineers must know the areas of knowledge that SWEBOK identifies. | software engineers | quality | S-01 page 313 | C-74 |
| R-0409 | Software engineers must internalize the difference between their role and that of a programmer. | software engineers | quality | S-01 page 313 | C-74 |
| R-0410 | Software engineers are expected to have deep and broad knowledge of computer science and apply it. | software engineers | quality | S-01 page 313 | C-76 |
| R-0411 | The problem to be solved has to be analyzed for functional requirements, user interactions, performance, device interfaces, security, vulnerability, durability and upgradability. | software engineers | quality | S-01 page 313 | C-68 |
| R-0412 | Ideally, systems should be highly cohesive. | software engineers | quality | S-01 page 313 | C-69 |
| R-0413 | Ideally, systems should be loosely coupled. | software engineers | quality | S-01 page 313 | C-69 |
| R-0414 | The hardware must be designed to support the software subsystems and satisfy all user requirements. | software engineers | quality | S-01 page 314 | C-69 |
| R-0415 | Software subsystem architects have to consider technology, tools, data structures, operating system, database, user interfaces, programming languages and algorithms. | software engineers | quality | S-01 page 314 | C-69 |
| R-0416 | Software engineers are expected to know the functioning and timing of different types of buses. | software engineers | quality | S-01 page 314 | C-76 |
| R-0417 | System architects must analyze the application and identify the critical components. | software engineers | quality | S-01 page 314 | C-69 |
| R-0418 | System architects must choose or design an appropriate computer architecture and organization. | software engineers | quality | S-01 page 314 | C-69 |
| R-0419 | Contingencies should be built in for the resources required. | management | quality | S-01 page 314 | C-72 |
| R-0420 | Software engineers need to know the different types of Flynn architecture, with examples. | software engineers | quality | S-01 page 316 | C-76 |
| R-0421 | Software engineers are also expected to know and apply other architectures. | software engineers | quality | S-01 page 316 | C-76 |
| R-0422 | Software engineers are expected to know the differences among architectures, with case studies, so that they can choose the right one. | software engineers | quality | S-01 page 316 | C-76 |
| R-0423 | System architects and engineers must know the components of the system and how they function. | software engineers | quality | S-01 page 316 | C-76 |
| R-0424 | Software engineers are expected to know the differences between multiple cores and multiple threads. | software engineers | quality | S-01 page 317 | C-76 |
| R-0425 | Software engineers are expected to understand the interface of I/O devices and device drivers. | software engineers | quality | S-01 page 317 | C-76 |
| R-0426 | Software engineers are expected to be aware of the different types of control units. | software engineers | quality | S-01 page 317 | C-76 |
| R-0427 | Software engineers working on performance-critical applications are expected to know the types of memory. | software engineers | quality | S-01 page 317 | C-76 |
| R-0428 | Software engineers must internalize data structures, their selection and their operations. | software engineers | quality | S-01 page 317 | C-76 |
| R-0429 | Software engineers are encouraged to learn the traversals of non-linear data structures. | software engineers | quality | S-01 page 318 | C-76 |
| R-0430 | Software engineers must understand the nuances of data types and their sizes in memory. | software engineers | quality | S-01 page 318 | C-76 |
| R-0431 | The algorithm has to be designed or chosen with consideration for performance, security, portability, maintainability, scalability and simplicity. | software engineers | quality | S-01 page 318 | C-76 |
| R-0432 | It is important to ensure that insertion or deletion does not violate the policy of the data set or database. | software engineers | quality | S-01 page 318 | C-76 |
| R-0433 | Learning the asymptotic notations for different sets of input data is important. | software engineers | quality | S-01 page 319 | C-76 |
| R-0434 | A software engineer has to know a few standard algorithms and relevant concepts. | software engineers | quality | S-01 page 319 | C-76 |
| R-0435 | The software engineer must consider application purpose and performance requirements to select an algorithm. | software engineers | quality | S-01 page 319 | C-76 |
| R-0436 | The software engineer must consider linear versus parallel programming and single versus multi-threading. | software engineers | quality | S-01 page 319 | C-76 |
| R-0437 | Software engineers should learn and accommodate preconditions and complexities of sorting algorithms. | software engineers | quality | S-01 page 321 | C-76 |
| R-0438 | Properties of hash functions must be understood and considered when designing or choosing a hash function. | software engineers | quality | S-01 page 321 | C-76 |
| R-0439 | Software engineers are expected to learn, implement and compare hashing algorithms and collision resolution techniques. | software engineers | quality | S-01 page 321 | C-76 |
| R-0440 | Software engineers must carefully consider various aspects before selecting a programming language. | software engineers | quality | S-01 page 321 | C-70 |
| R-0441 | Software engineers are expected to know how high-level languages are translated and the differences among compilers, interpreters and assemblers. | software engineers | quality | S-01 page 322 | C-76 |
| R-0442 | Software engineers are encouraged to learn about compiler phases. | software engineers | quality | S-01 page 322 | C-76 |
| R-0443 | Software engineers need to study multiple programming languages to choose the right one. | software engineers | quality | S-01 page 322 | C-70 |
| R-0444 | Software engineers are encouraged to understand where coroutines are useful and to use them. | software engineers | quality | S-01 page 323 | C-70 |
| R-0445 | Software engineers should know the differences among parameter-passing types and use them appropriately. | software engineers | quality | S-01 page 323 | C-70 |
| R-0446 | Software engineers are encouraged to understand, with case studies, how return addresses and parameters are stored. | software engineers | quality | S-01 page 323 | C-76 |
| R-0447 | It is important to establish exit criteria in recursive subprograms. | software engineers | quality | S-01 page 323 | C-70 |
| R-0448 | Programs are expected to function properly and generate the expected output. | software engineers | quality | S-01 page 324 | C-70 |
| R-0449 | Programs must be thoroughly tested for valid, invalid and boundary inputs and conditions. | quality assurance | quality | S-01 page 324 | C-40 |
| R-0450 | Logical errors must be traced and resolved with various data for each functionality. | software engineers | quality | S-01 page 324 | C-70 |
| R-0451 | It is important to recognize that using object-oriented programming requires a different mindset. | software engineers | quality | S-01 page 324 | C-70 |
| R-0452 | Carefully choose the coding standards and guidelines that suit the application or system. | producers | quality | S-01 page 325 | C-70 |
| R-0453 | Consider open standards created by community participation. | producers | quality | S-01 page 325 | C-70 |
| R-0454 | Educate programmers to follow adopted standards and guidelines. | producers | quality | S-01 page 326 | C-70 |
| R-0455 | Use tools and periodic reviews to ensure that adopted standards and guidelines are followed. | producers | quality | S-01 page 326 | C-43 |
| R-0456 | Review and revise standards and guidelines from time to time. | producers | quality | S-01 page 326 | C-70 |
| R-0457 | Software engineers are recommended to refer to the ISO/IEC JTC 1/SC 22 standards. | software engineers | quality | S-01 page 326 | C-70 |
| R-0458 | Software engineers need a good general understanding of operating systems and their objectives. | software engineers | quality | S-01 page 326 | C-76 |
| R-0459 | Software engineers must understand processor, process and address space concepts, and booting. | software engineers | quality | S-01 page 326 | C-76 |
| R-0460 | Software engineers should compare and contrast CPU scheduling concepts and algorithms. | software engineers | quality | S-01 page 326 | C-76 |
| R-0461 | A software engineer must have a deep understanding of inter-process communication. | software engineers | quality | S-01 page 326 | C-76 |
| R-0462 | Software engineers are required to study concurrent languages, processes and scheduling. | software engineers | quality | S-01 page 326 | C-76 |
| R-0463 | Software engineers have to analyze different types of operating systems to choose an appropriate one. | software engineers | quality | S-01 page 326 | C-76 |
| R-0464 | It is important to study examples of each operating system type and compare their benefits and limitations. | software engineers | quality | S-01 page 326 | C-76 |
| R-0465 | Software engineers should understand device drivers, their types and their interfaces. | software engineers | quality | S-01 page 327 | C-76 |
| R-0466 | Software engineers should understand that caching, scheduling and spooling issues arise for shared devices. | software engineers | quality | S-01 page 327 | C-76 |
| R-0467 | A software engineer must have good knowledge of different types of I/O devices. | software engineers | quality | S-01 page 327 | C-76 |
| R-0468 | A software engineer needs a very good understanding of how memory is managed. | software engineers | quality | S-01 page 327 | C-76 |
| R-0469 | Engineers must understand memory fragmentation and memory management concepts. | software engineers | quality | S-01 page 327 | C-76 |
| R-0470 | Software engineers need to understand process concepts, file system management and operating system views of files. | software engineers | quality | S-01 page 327 | C-76 |
| R-0471 | Engineers should be familiar with access control lists, access matrix, authentication and other access methods. | software engineers | quality | S-01 page 327 | C-76 |
| R-0472 | Engineers should compare and contrast polled, interrupt-driven and direct memory access I/O devices. | software engineers | quality | S-01 page 327 | C-76 |
| R-0473 | A network manager will need detailed knowledge of physical and logical time and synchronization protocols. | operations engineers | quality | S-01 page 328 | C-76 |
| R-0474 | Software engineers should understand hardware security, external security, operational security, password protection and access control. | software engineers | security | S-01 page 328 | C-38 |
| R-0475 | When selecting a database, software engineers should evaluate data models, storage models and database types. | software engineers | quality | S-01 page 328 | C-76 |
| R-0476 | The learners and users of the database system need to create two roles, review case studies and analyze information. | software engineers | quality | S-01 page 328 | C-76 |
| R-0477 | Computer science engineers must understand the types of relational database systems and their applications. | software engineers | quality | S-01 page 330 | C-76 |
| R-0478 | Database engineers are encouraged to understand normalization forms with examples and case studies. | software engineers | quality | S-01 page 330 | C-76 |
| R-0479 | Database engineers have to decide whether to use static, dynamic or combined SQL after weighing pros and cons. | software engineers | quality | S-01 page 330 | C-76 |
| R-0480 | Database engineers should know the differences between simple and complex views and use them appropriately. | software engineers | quality | S-01 page 330 | C-76 |
| R-0481 | Database engineers must know data mining techniques and how to apply them. | software engineers | quality | S-01 page 331 | C-76 |
| R-0482 | It is important for software engineers to understand the networking topics listed. | software engineers | quality | S-01 page 331 | C-76 |
| R-0483 | Practitioners of computer science engineering have to study computer networks and communication concepts. | software engineers | quality | S-01 page 331 | C-76 |
| R-0484 | It is crucial to prevent data corruption and, if it occurs, to recognize it immediately and recover the data. | software engineers | quality | S-01 page 331 | C-76 |
| R-0485 | Database updates must be carried out carefully, with commits at checkpoints, and must incorporate undo and shadow paging techniques. | software engineers | quality | S-01 page 331 | C-76 |
| R-0486 | Databases must be backed up periodically to ensure data safety. | operations engineers | operations | S-01 page 331 | C-60 |
| R-0487 | It is important to understand each network type, with examples, benefits, limitations and solutions. | software engineers | quality | S-01 page 332 | C-76 |
| R-0488 | Software engineers are expected to understand the functionalities required of layers, data modes and packet formation. | software engineers | quality | S-01 page 332 | C-76 |
| R-0489 | Engineers must understand each OSI layer, its functionality, and its input and output in each direction. | software engineers | quality | S-01 page 333 | C-76 |
| R-0490 | Engineers should analyze whether all seven layers are required for all protocols and what is needed to optimize performance. | software engineers | quality | S-01 page 333 | C-76 |
| R-0491 | Software engineers practicing in networking need to understand CASE and SASE application services. | software engineers | quality | S-01 page 333 | C-76 |
| R-0492 | It is critical to identify network requirements, both business goals and technical solutions, with a road map. | software engineers | quality | S-01 page 333 | C-68 |
| R-0493 | The fundamental design goals should include reliability, security, availability and manageability. | software engineers | quality | S-01 page 333 | C-69 |
| R-0494 | Engineers should expect threats and intrusions at multiple levels and design security at multiple levels. | software engineers | security | S-01 page 333 | C-27 |
| R-0495 | Systems must be set up to monitor networks for proper and improper functioning, and to identify and fix faults, vulnerabilities and hacks quickly. | operations engineers | operations | S-01 page 333 | C-57 |
| R-0496 | Engineers must understand and learn the design of networks with firewalls, VLANs, subnets, QoS and DMZ. | software engineers | quality | S-01 page 333 | C-76 |
| R-0497 | One has to be constantly vigilant for attacks and continuously upgrade systems, devices and tools. | operations engineers | security | S-01 pages 333 to 334 | C-38 |
| R-0498 | Engineers should analyze the PDU structures of each OSI layer, the Internet protocol suite and ATM. | software engineers | quality | S-01 page 333 | C-76 |
| R-0499 | Professional computer network architects and programmers need to understand IPv6 addressing, routing, transition and NAT64. | software engineers | quality | S-01 page 334 | C-76 |
| R-0500 | Software engineers are encouraged to learn the differences among 1G, 2G, 3G, 4G and 5G technologies. | software engineers | quality | S-01 page 334 | C-76 |
| R-0501 | Many precautionary measures must be implemented and strictly followed to reduce wireless risks. | consumers | security | S-01 page 335 | C-38 |
| R-0502 | Users must protect and hide the SSID, use effective antivirus software, and update it regularly. | consumers | security | S-01 page 335 | C-38 |
| R-0503 | Users must use VPNs, use file sharing with care, disable access after use, and apply security patches when available. | consumers | security | S-01 page 335 | C-38 |
| R-0504 | Users expect software to be robust, intuitive, secure and to give fast, consistent responses. | consumers | quality | S-01 page 335 | C-68 |
| R-0505 | The interface should help users use the system easily. | consumers | quality | S-01 page 335 | C-69 |
| R-0506 | The interface should be self-explanatory and enable self-learning. | consumers | quality | S-01 page 335 | C-69 |
| R-0507 | Messages about results and errors should be clear and complete. | consumers | quality | S-01 page 335 | C-69 |
| R-0508 | The system should be able to regain its original state after errors. | software engineers | operations | S-01 page 335 | C-67 |
| R-0509 | The system should allow users to interrupt processing and undo the operation where possible. | consumers | quality | S-01 page 335 | C-69 |
| R-0510 | The software engineer needs to identify the user profile, system functions, interfaces and performance parameters. | software engineers | quality | S-01 page 335 | C-68 |
| R-0511 | The user interface devices must be robust. | software engineers | quality | S-01 page 335 | C-76 |
| R-0512 | Code has to be written with more care for use by other programmers. | software engineers | quality | S-01 page 335 | C-70 |
| R-0513 | Meaningful and comprehensive documentation is crucial at all stages of the software lifecycle. | software engineers | quality | S-01 page 335 | C-70 |
| R-0514 | Adopting a coding standard for the project and ensuring every team member applies it is key. | software engineers | quality | S-01 page 335 | C-70 |
| R-0515 | Code has to be legible and easy to comprehend. | software engineers | quality | S-01 page 335 | C-70 |
| R-0516 | Meaningful, consistent and detailed comments are essential for code readability. | software engineers | quality | S-01 page 335 | C-70 |
| R-0517 | Engineers should be aware of the limits and challenges of AI and ML, including uncertain and stochastic behaviour and the need for sufficiently labelled and structured datasets. | software engineers | quality | S-01 page 338 | C-76 |
| R-0518 | Software engineers working on AI are expected to know various other learning techniques and the key differences between methods and where each works well. | software engineers | quality | S-01 page 337 | C-76 |
| R-0519 | Software engineers are encouraged to learn other reasoning methods. | software engineers | quality | S-01 page 337 | C-76 |
| R-0520 | Software engineers are encouraged to learn many other AI models. | software engineers | quality | S-01 page 338 | C-76 |
| R-0521 | There is a need for particular support of software engineering for AI, such as interdisciplinary collaborative teams of data scientists and software engineers, software evolution for large changing datasets, and ethics and equity requirements engineering. | software engineers | quality | S-01 pages 338 and 339 | C-76 |
| R-0522 | Recommended software engineering practices for AI are often formalised as patterns, such as ML software design patterns. | software engineers | quality | S-01 page 339 | C-69 |
| R-0523 | Engineering decisions must consider various factors, including financial criteria. | management | quality | S-01 page 367 | C-75 |
| R-0524 | Identify all relevant selection criteria. | software engineers | quality | S-01 page 367 | C-76 |
| R-0525 | Use root cause analysis techniques to discover the underlying problem that needs a solution. | software engineers | quality | S-01 page 367 | C-76 |
| R-0526 | Identify all reasonable, technically feasible solutions and consider several of them. | software engineers | quality | S-01 page 367 | C-76 |
| R-0527 | Evaluate each solution against the selection criteria. | software engineers | quality | S-01 page 367 | C-76 |
| R-0528 | Select the preferred solution that best meets the selection criteria. | software engineers | quality | S-01 page 367 | C-76 |
| R-0529 | Monitor the performance of the selected solution. | software engineers | quality | S-01 page 367 | C-76 |
| R-0530 | It is essential to evaluate the real-world performance of the selected alternative and, if necessary and possible, decide whether another alternative might be better. | software engineers | quality | S-01 page 368 | C-76 |
| R-0531 | Engineers must understand how to create an experiment and analyze its results to evaluate proposed solutions. | software engineers | quality | S-01 page 371 | C-76 |
| R-0532 | Engineers need to understand how to formulate clear hypotheses. | software engineers | quality | S-01 page 371 | C-76 |
| R-0533 | Engineers must understand how product and process characteristics vary. | software engineers | quality | S-01 page 371 | C-76 |
| R-0534 | Engineers must understand statistical techniques for collecting and interpreting reliable data. | software engineers | quality | S-01 page 371 | C-76 |
| R-0535 | Samples must be drawn so that draws are independent, and the sampling rules must be predefined so that selection probabilities are known beforehand. | software engineers | quality | S-01 page 372 | C-76 |
| R-0536 | Accept or reject the null hypothesis on the basis of the evidence obtained. | software engineers | quality | S-01 page 373 | C-76 |
| R-0537 | Aim to maximize the power of a test while keeping the probability of a type I error within a set value, typically 5 percent. | software engineers | quality | S-01 page 374 | C-76 |
| R-0538 | Remember that correlation does not imply causation. | software engineers | quality | S-01 page 374 | C-76 |
| R-0539 | Prototype construction must have a clear purpose and be planned, monitored and controlled. | software engineers | quality | S-01 page 375 | C-76 |
| R-0540 | A combination of direct and derived measures is necessary in software engineering. | software engineers | quality | S-01 page 376 | C-76 |
| R-0541 | Everyone involved in an engineering project must understand the measurement methods, the measurement results and how those results can and should be used. | software engineers | quality | S-01 page 376 | C-76 |
| R-0542 | Each step of measurement must be understood, communicated and properly performed to yield usable data. | software engineers | quality | S-01 page 376 | C-76 |
| R-0543 | Engineers must appreciate the need to define measurements from an operational perspective. | software engineers | quality | S-01 page 376 | C-76 |
| R-0544 | The measurement method must be well defined. | software engineers | quality | S-01 page 376 | C-76 |
| R-0545 | Nonnumerical labels are preferred to numbers for ordinal scales such as CMMI staged maturity levels. | software engineers | quality | S-01 page 377 | C-76 |
| R-0546 | Future programming languages should enforce measurement theory and not allow developers to manipulate measurements inappropriately. | software engineers | quality | S-01 page 379 | C-76 |
| R-0547 | Software engineers need to understand measurement theory and watch for inappropriate manipulations, for example in code reviews. | software engineers | quality | S-01 page 379 | C-76 |
| R-0548 | Standards provide requirements, specifications or guidelines that engineers must observe so that products, processes and materials are of acceptable quality. | software engineers | quality | S-01 page 381 | C-76 |
| R-0549 | Engineers are expected to be familiar with and use the appropriate standards for their discipline. | software engineers | quality | S-01 page 381 | C-76 |
| R-0550 | For a standard to be useful, conformance must add real or perceived value. | software engineers | quality | S-01 page 381 | C-76 |
| R-0551 | Engineers must be aware of existing standards and keep abreast of changes to them over time. | software engineers | quality | S-01 page 382 | C-76 |
| R-0552 | The engineer must review all current standards related to a given endeavor and determine which must be met. | software engineers | quality | S-01 page 382 | C-76 |
| R-0553 | The design must incorporate all constraints imposed by the applicable standard. | software engineers | quality | S-01 page 382 | C-76 |
| R-0554 | Cause maps require evidence of the occurrence of causes and of the causality of effects. | software engineers | quality | S-01 page 382 | C-76 |
| R-0555 | Clearly define the problem and its significance when selecting the problem to solve. | software engineers | quality | S-01 page 383 | C-76 |
| R-0556 | Gather evidence about the problem and its causes. | software engineers | quality | S-01 page 383 | C-76 |
| R-0557 | Identify the root cause using one or more root cause analysis techniques. | software engineers | quality | S-01 page 383 | C-76 |
| R-0558 | Select corrective actions that prevent recurrence, are within the organization's ability to control, meet organizational goals and do not cause other problems. | software engineers | quality | S-01 page 383 | C-76 |
| R-0559 | More than one candidate corrective action should be considered. | software engineers | quality | S-01 page 383 | C-76 |
| R-0560 | Selected corrective actions should generate the greatest amount of control for the least cost. | software engineers | quality | S-01 page 383 | C-76 |
| R-0561 | Implement the selected corrective actions. | software engineers | quality | S-01 page 383 | C-76 |
| R-0562 | Observe the selected corrective actions to ensure efficiency and effectiveness. | software engineers | quality | S-01 page 383 | C-76 |
| R-0563 | Each KA breakdown must incorporate the common themes of measurement, quality and security. | producers | quality | S-01 page 388 | C-77 |
| R-0564 | The breakdown of topics should be at most two or three levels deep. | producers | quality | S-01 page 388 | C-77 |
| R-0565 | Topic names must be significant enough to be meaningful outside the Guide. | producers | quality | S-01 page 388 | C-77 |
| R-0566 | The breakdown of topics within a KA must decompose the generally recognized subset of the SWEBOK. | producers | quality | S-01 page 388 | C-77 |
| R-0567 | The breakdown of topics within a KA must not presume specific application domains, business needs, organization sizes, structures, management philosophies, life cycle models, technologies or methods. | producers | quality | S-01 page 388 | C-77 |
| R-0568 | The breakdown of topics within a KA must be compatible with the various schools of thought, as far as possible. | producers | quality | S-01 page 388 | C-77 |
| R-0569 | The breakdown of topics within a KA must be compatible with the breakdown found in industry and in the literature and standards. | producers | quality | S-01 page 388 | C-77 |
| R-0570 | Topic descriptions must not be prescriptive. | producers | quality | S-01 page 388 | C-77 |
| R-0571 | The description of a KA will include a tree-form chart of the breakdown. | producers | quality | S-01 page 388 | C-77 |
| R-0572 | Change requests to the baseline must be approved by the Guide editors and by the team before implementation. | producers | quality | S-01 page 388 | C-77 |
| R-0573 | KA editors are instructed to refine the baseline breakdown of topics for KAs that continue from the previous version. | producers | quality | S-01 page 388 | C-77 |
| R-0574 | Emphasis should be put on the selection of topics rather than on their hierarchy. | producers | quality | S-01 page 388 | C-77 |
| R-0575 | Reference material must be generally available and must not be confidential. | producers | quality | S-01 page 389 | C-77 |
| R-0576 | Reference material must be in English. | producers | quality | S-01 page 389 | C-77 |
| R-0577 | The Consolidated Reference List should be complete, sufficient, consistent, credible, current and succinct. | producers | quality | S-01 page 389 | C-77 |
| R-0578 | Recommended reference material must be identified for each topic. | producers | quality | S-01 page 389 | C-77 |
| R-0579 | Each recommended reference should be as precise as possible about the relevant chapter or section. | producers | quality | S-01 page 389 | C-77 |
| R-0580 | A matrix of reference material against topics must be provided. | producers | quality | S-01 page 389 | C-77 |
| R-0581 | The latest versions or editions should be used as recommended references. | producers | quality | S-01 page 389 | C-77 |
| R-0582 | A reasonable amount of recommended reference material must be identified for each KA. | producers | quality | S-01 page 389 | C-77 |
| R-0583 | KA editors should bring in additional reference material only where it is necessary to the discussion. | producers | quality | S-01 page 390 | C-77 |
| R-0584 | Further readings must relate to the topics in the breakdown and must be annotated, one paragraph per item. | producers | quality | S-01 page 390 | C-77 |
| R-0585 | A general guideline is to be followed of 10 or fewer further readings per KA. | producers | quality | S-01 page 390 | C-77 |
| R-0586 | KA descriptions should use the common structure given in the Guide. | producers | quality | S-01 page 390 | C-77 |
| R-0587 | A balance must be maintained between readability and technical excellence. | producers | quality | S-01 page 390 | C-77 |
| R-0588 | KA descriptions are to be roughly 10 to 20 pages in length. | producers | quality | S-01 page 391 | C-77 |
| R-0589 | KA editors are expected to be somewhat forward-looking in their interpretation. | producers | quality | S-01 page 391 | C-77 |
| R-0590 | Special care will be taken to keep the Guide compatible with ISO/IEC/IEEE 12207. | producers | quality | S-01 page 391 | C-77 |
| R-0591 | KA editors must sign a copyright release form. | producers | quality | S-01 page 392 | C-77 |
| R-0592 | Guide editors and copy editors will edit the KA descriptions. | producers | quality | S-01 page 392 | C-77 |
| R-0593 | Writers should avoid footnotes and put their content in the main text. | producers | quality | S-01 page 392 | C-77 |
| R-0594 | Writers should use explicit references to standards. | producers | quality | S-01 page 392 | C-77 |
| R-0595 | Text that accompanies figures and tables should be self-explanatory or have enough related text. | producers | quality | S-01 page 392 | C-77 |
| R-0596 | Writers should avoid naming tools and products directly and should name their functions instead. | producers | quality | S-01 page 392 | C-77 |
| R-0597 | When referencing the Guide, the title SWEBOK Guide must be used. | producers | quality | S-01 page 392 | C-77 |
| R-0598 | The Guide will continue to be available free of charge in the public domain in at least one format. | producers | quality | S-01 page 392 | C-77 |
| R-0599 | Process standards should not be confused with procedures or instructions. | producers | quality | S-01 page 394 | C-73 |
| R-0600 | When a standard is incorporated in contracts or agreements, compliance becomes mandatory. | management | quality | S-01 page 394 | C-72 |
| R-0601 | When software is the predominant system of interest, ISO/IEC/IEEE 12207 should be used. | producers | quality | S-01 page 396 | C-73 |
| R-0602 | The ethical-values standard requires consideration of values relevant to the culture where the system is deployed. | producers | quality | S-01 page 400 | C-74 |
| R-0603 | Users of standards should look for the most recent version and for newer titles. | producers | quality | S-01 page 403 | C-77 |
| R-0604 | The what is and hows of requirements work should be set by the nature of the software, not by the life cycle. | software engineers | quality | S-01 page 44 | C-68 |
| R-0605 | Downstream maintainers should not be able to tell the earlier life cycle from the form of the requirements alone. | producers | quality | S-01 page 44 | C-68 |
| R-0606 | Whenever a nonfunctional requirement is changed, the impact on other requirements should be considered. | software engineers | quality | S-01 page 46 | C-68 |
| R-0607 | The kinds of security requirements that should be considered are described in the Security KA. | software engineers | security | S-01 page 47 | C-18 |
| R-0608 | All potential requirements sources should be identified and evaluated. | software engineers | quality | S-01 page 48 | C-68 |
| R-0609 | The software engineer must work hard to elicit the right information, because elicitation is not passive. | software engineers | quality | S-01 page 49 | C-68 |
| R-0610 | The overall collection of requirements should be complete, concise, internally consistent, externally consistent and feasible. | software engineers | quality | S-01 page 50 | C-68 |
| R-0611 | Each requirement should be unambiguous, testable, binding, atomic, represent true stakeholder needs, use stakeholder vocabulary and be acceptable to all stakeholders. | software engineers | quality | S-01 page 50 | C-68 |
| R-0612 | Where a choice is unwise for one person alone, stakeholders should be consulted to reach consensus. | software engineers | quality | S-01 page 52 | C-68 |
| R-0613 | The software engineer should pay particular attention to positive and negative relationships between quality of service constraints. | software engineers | quality | S-01 page 51 | C-68 |
| R-0614 | Documented software requirements should be subject to the same configuration management practices as the other deliverables. | software engineers | pipeline | S-01 page 53 | C-16 |
| R-0615 | The effect of the chosen life cycle should be limited to the completeness of the requirements at any point in the project. | software engineers | quality | S-01 page 53 | C-68 |
| R-0616 | The most basic recommendation for requirements documentation is to base decisions on an audience analysis. | software engineers | quality | S-01 page 53 | C-68 |
| R-0617 | Requirements scrubbing should occur just before the validation review. | software engineers | quality | S-01 page 58 | C-68 |
| R-0618 | Review from multiple perspectives is preferred. | quality assurance | quality | S-01 page 58 | C-48 |
| R-0619 | Projects using waterfall or other plan-based life cycles should have an explicit requirements change control process. | management | pipeline | S-01 page 59 | C-16 |
| R-0620 | The change control process should include a means to request changes, an optional impact analysis, a responsible decider, a means to notify stakeholders and a means to track accepted changes. | management | pipeline | S-01 page 59 | C-16 |
| R-0621 | All stakeholders must understand and agree that accepting a change means accepting its impact on schedule, resources and scope. | management | quality | S-01 page 59 | C-68 |
| R-0622 | Ideally the change in scope should be objectively quantifiable, in functional size units. | management | quality | S-01 page 59 | C-72 |
| R-0623 | When scope exceeds cost, schedule or staffing constraints, the scope must be reduced, the capacity must be increased, or a combination must be negotiated. | management | quality | S-01 page 59 | C-72 |
| R-0624 | Where possible, scope matching should be quantitative instead of qualitative. | management | quality | S-01 page 59 | C-72 |
| R-0625 | In plan-based life cycles, scope matching should occur just before the validation review. | management | quality | S-01 page 59 | C-72 |
| R-0626 | Defects raised against higher-priority requirements should probably be repaired before defects raised against lower-priority ones. | software engineers | quality | S-01 page 60 | C-68 |
| R-0627 | Prioritization must weigh both the satisfaction from features and the dissatisfaction from missing features. | software engineers | quality | S-01 page 60 | C-68 |
| R-0628 | Once priorities are determined, they must be specified in a way that can be communicated to all stakeholders. | software engineers | quality | S-01 page 60 | C-68 |
| R-0629 | Planguage recommends documenting attributes such as scale, meter, minimum, target and trend for requirements. | software engineers | quality | S-01 page 57 | C-45 |
| R-0630 | The architecture should be documented to support its shared understanding, analysis and reverse architecting uses. | software engineers | quality | S-01 page 70 | C-69 |
| R-0631 | Notations for architecture descriptions should be chosen by the need, purpose and utility for the stakeholders who need the information. | software engineers | quality | S-01 page 70 | C-69 |
| R-0632 | A good architecture should address the distinct concerns of its stakeholders and also the consequences of their interactions. | software engineers | quality | S-01 page 77 | C-69 |
| R-0633 | Quoted from Dijkstra: a program must be correct and should be efficient, used to illustrate separation of concerns; not a requirement of the source itself. | software engineers | quality | S-01 page 69 | C-69 |
| R-0634 | The design must solve the problems that the software requirements establish. | software engineers | quality | S-01 page 85 | C-69 |
| R-0635 | The software design must provide a guide to implementers on building the system. | software engineers | quality | S-01 page 85 | C-69 |
| R-0636 | Design should be complete with respect to the modes and states of the software. | software engineers | quality | S-01 page 86 | C-69 |
| R-0637 | A design should be sufficient for designers to demonstrate how requirements will be met. | software engineers | quality | S-01 page 86 | C-69 |
| R-0638 | A software design description should be sufficient as a basis for verifying a design. | software engineers | quality | S-01 page 86 | C-69 |
| R-0639 | The detailed design specifications should be sufficient to allow programmers to code each module. | software engineers | quality | S-01 page 87 | C-69 |
| R-0640 | The high-level design specification should be sufficiently detailed to allow designers or programmers of client components to access each service without reading its code. | software engineers | quality | S-01 page 87 | C-69 |
| R-0641 | Projects should make conscious decisions about which design specifications are needed, based on stakeholder audience, subject and intended usage. | software engineers | quality | S-01 page 90 | C-69 |
| R-0642 | Architecturally significant decisions must be determined early in the life cycle. | software engineers | quality | S-01 page 87 | C-69 |
| R-0643 | Most design methods advocate that modules should be loosely or weakly coupled. | software engineers | quality | S-01 page 86 | C-69 |
| R-0644 | Most design methods advocate that modules should maximize their cohesion. | software engineers | quality | S-01 page 86 | C-69 |
| R-0645 | Any dependency in the supply chain network should be managed by developers or tools. | software engineers | pipeline | S-01 page 103 | C-14 |
| R-0646 | Unnecessary dependencies should be avoided to improve build efficiency. | software engineers | pipeline | S-01 page 103 | C-14 |
| R-0647 | License conflicts between dependencies and software products should be avoided to reduce legal risk. | software engineers | security | S-01 page 103 | C-25 |
| R-0648 | Propagation of dependency defects or vulnerabilities into software products should be avoided to improve software quality. | software engineers | security | S-01 page 103 | C-25 |
| R-0649 | Regulations and monitoring mechanisms should be developed to prevent developers from introducing untrusted external dependencies. | software engineers | security | S-01 page 103 and page 104 | C-28 |
| R-0650 | Software engineers should be careful to build flexibility and adaptability into software. | software engineers | quality | S-01 page 101 | C-70 |
| R-0651 | Software teams should embrace change by adopting agile development, DevOps and continuous delivery and deployment practices. | software engineers | operations | S-01 page 101 | C-62 |
| R-0652 | Programmers should know good practices and common vulnerabilities. | software engineers | security | S-01 page 107 | C-29 |
| R-0653 | Developers should encapsulate reusable code fragments into well-structured libraries or components to avoid code clones. | software engineers | quality | S-01 page 106 | C-70 |
| R-0654 | Exception-handling policies should be carefully designed following common principles. | software engineers | quality | S-01 page 109 | C-70 |
| R-0655 | An API should always include statements about the program's effects and behaviors. | software engineers | quality | S-01 page 108 | C-70 |
| R-0656 | API design should make the API easy to learn, readable, hard to misuse, easy to extend, complete and backward compatible. | software engineers | quality | S-01 page 108 | C-70 |
| R-0657 | An API should be straightforward and stable. | software engineers | quality | S-01 page 108 | C-70 |
| R-0658 | Ideally, there should be at least as many test cases as the cyclomatic complexity count. | quality assurance | quality | S-01 page 100 | C-40 |
| R-0659 | Design and construction processes should accommodate string and character set issues for internationalization. | software engineers | quality | S-01 page 110 | C-70 |
| R-0660 | Follow a consistent build process. | producers | pipeline | S-02 Build L1 | C-04 |
| R-0661 | Run builds on an L1-compliant build platform. | producers | pipeline | S-02 Build L1 | C-06 |
| R-0662 | Distribute provenance to consumers, preferably using the package ecosystem's convention. | producers | pipeline | S-02 Build L1 | C-08 |
| R-0663 | Automatically generate provenance covering the builder, the build process, and the top-level build inputs. | platform providers | pipeline | S-02 Build L1 | C-08 |
| R-0664 | Run builds on a hosted build platform that meets L2 requirements. | producers | pipeline | S-02 Build L2 | C-06 |
| R-0665 | Generate and sign the provenance, either during the build or through an equivalent trust mechanism. | platform providers | pipeline | S-02 Build L2 | C-08 |
| R-0666 | Validate the provenance's authenticity. | consumers | pipeline | S-02 Build L2 | C-11 |
| R-0667 | Run builds on a hosted build platform that meets L3 requirements. | producers | pipeline | S-02 Build L3 | C-06 |
| R-0668 | Strongly prevent runs from influencing one another, even within the same project. | platform providers | pipeline | S-02 Build L3 | C-09 |
| R-0669 | Prevent provenance-signing secrets from being reachable by user-defined build steps. | platform providers | pipeline | S-02 Build L3 | C-09 |
| R-0670 | Build L0 has no requirements. | producers | pipeline | S-02 Build L0 | C-06 |
| R-0671 | The build platform must strengthen its controls to reach a given level. | platform providers | pipeline | S-02 Overview, Build levels | C-06 |
| R-0672 | The producer must pick a platform able to reach that level and apply its required controls. | producers | pipeline | S-02 Overview, Build levels | C-06 |
| R-0673 | All implementations must follow industry security best practices to conform. | platform providers | security | S-02 Overview, Security Best Practices | C-38 |
| R-0674 | The producer must select a platform that can reach its target Build Level. | producers | pipeline | S-02 Producer, Choose an appropriate build platform | C-06 |
| R-0675 | A producer targeting Build Level 3 must use a builder that can produce Level 3 provenance. | producers | pipeline | S-02 Producer, Choose an appropriate build platform | C-08 |
| R-0676 | The producer must build in a consistent way so verifiers can form expectations. | producers | pipeline | S-02 Producer, Follow a consistent build process | C-04 |
| R-0677 | If an ecosystem requires a build configuration file, the producer must complete it and keep it current. | producers | pipeline | S-02 Producer, Follow a consistent build process | C-04 |
| R-0678 | The producer must deliver provenance to consumers, though it may delegate this to an ecosystem that can distribute it. | producers | pipeline | S-02 Producer, Distribute provenance | C-08 |
| R-0679 | The build must generate provenance that identifies the output by cryptographic digest and describes how it was produced. | platform providers | pipeline | S-02 Build Platform, Provenance Exists (L1) | C-08 |
| R-0680 | The provenance format must be acceptable to the ecosystem and/or consumer. | platform providers | pipeline | S-02 Build Platform, Provenance Exists (L1) | C-08 |
| R-0681 | An alternate format must carry the same information as SLSA Provenance at each level and should be translatable to it in both directions. | platform providers | pipeline | S-02 Build Platform, Provenance Exists (L1) | C-08 |
| R-0682 | L1 provenance should contain enough information to catch mistakes, and its contents should match across levels. | platform providers | pipeline | S-02 Build Platform, Provenance Exists (L1) | C-08 |
| R-0683 | Consumers must be able to validate provenance authenticity to check integrity and identify the trusted build platform. | consumers | pipeline | S-02 Build Platform, Provenance is Authentic (L2) | C-11 |
| R-0684 | Authenticity should be proven by a digital signature from a key only the build platform component can access. | platform providers | pipeline | S-02 Build Platform, Provenance is Authentic (L2) | C-08 |
| R-0685 | The provenance must be generated by the control plane, not by a tenant, and its data must come from the build platform. | platform providers | pipeline | S-02 Build Platform, Provenance is Authentic (L2) | C-08 |
| R-0686 | The build platform must have some control to stop tenants from tampering with provenance. | platform providers | pipeline | S-02 Build Platform, Provenance is Authentic (L2) | C-08 |
| R-0687 | Builders should document any fields that tenants are allowed to generate. | platform providers | pipeline | S-02 Build Platform, Provenance is Authentic (L2) | C-08 |
| R-0688 | Provenance should be complete. | platform providers | pipeline | S-02 Build Platform, Provenance is Authentic (L2) | C-08 |
| R-0689 | Provenance must strongly resist forgery by tenants. | platform providers | pipeline | S-02 Build Platform, Provenance is Unforgeable (L3) | C-08 |
| R-0690 | Signing secrets must be stored in a proper secret management system, accessible only to the build service account. | platform providers | security | S-02 Build Platform, Provenance is Unforgeable (L3) | C-22 |
| R-0691 | Those secrets must not be reachable from the user-defined build steps. | platform providers | pipeline | S-02 Build Platform, Provenance is Unforgeable (L3) | C-09 |
| R-0692 | Every provenance field must be generated or verified by the build platform's trusted control plane. | platform providers | pipeline | S-02 Build Platform, Provenance is Unforgeable (L3) | C-08 |
| R-0693 | User build steps must not be able to inject or change provenance contents. | platform providers | pipeline | S-02 Build Platform, Provenance is Unforgeable (L3) | C-08 |
| R-0694 | External parameters must be fully listed. | platform providers | pipeline | S-02 Build Platform, Provenance is Unforgeable (L3) | C-08 |
| R-0695 | Provenance should be complete. | platform providers | pipeline | S-02 Build Platform, Provenance is Unforgeable (L3) | duplicate: R-0688 |
| R-0696 | The build platform must guarantee that a build cannot access platform secrets, such as the signing key. | platform providers | pipeline | S-02 Build Platform, Isolation strength (L3) | C-09 |
| R-0697 | The build platform must guarantee that overlapping builds cannot affect each other, even on the same machine. | platform providers | pipeline | S-02 Build Platform, Isolation strength (L3) | C-09 |
| R-0698 | The build platform must guarantee that a build cannot persist or affect the environment of a later build. | platform providers | pipeline | S-02 Build Platform, Isolation strength (L3) | C-09 |
| R-0699 | The build platform must guarantee that each build gets a fresh, ephemeral environment. | platform providers | pipeline | S-02 Build Platform, Isolation strength (L3) | C-09 |
| R-0700 | The build platform must guarantee that a build cannot poison the cache of another build. | platform providers | pipeline | S-02 Build Platform, Isolation strength (L3) | C-09 |
| R-0701 | The build platform must guarantee that build output is identical whether or not the cache is used. | platform providers | pipeline | S-02 Build Platform, Isolation strength (L3) | C-17 |
| R-0702 | The build platform must guarantee that it does not expose remote-access services unless every such interaction is recorded as an external parameter. | platform providers | pipeline | S-02 Build Platform, Isolation strength (L3) | C-09 |
| R-0703 | The build platform must guarantee that these isolation guarantees hold even between builds within the same tenant project. | platform providers | pipeline | S-02 Build Platform, Isolation strength (L3) | C-09 |
| R-0704 | Choose an SCS able to reach the desired level. | producers | pipeline | S-02 Organization requirements | C-15 |
| R-0705 | Control access through SCS identity management. | producers | security | S-02 Organization requirements | C-21 |
| R-0706 | Configure the SCS to produce reliable Change History; if the SCS cannot do this by design, provide evidence of continuous enforcement. | producers | pipeline | S-02 Organization requirements | C-15 |
| R-0707 | Prevent moved or deleted tags, where tags are supported. | producers | pipeline | S-02 Organization requirements | C-02 |
| R-0708 | Expunge history only for legal or privacy compliance. | producers | pipeline | S-02 Organization requirements | C-02 |
| R-0709 | Document the expunging process. | producers | pipeline | S-02 Organization requirements | C-02 |
| R-0710 | Log each removal; this should occur. | producers | security | S-02 Organization requirements | C-32 |
| R-0711 | Require an Administrator plus another trusted person for expunging; this should be required. | producers | pipeline | S-02 Organization requirements | C-02 |
| R-0712 | Keep expunge logs public where possible; logs may be private. | producers | security | S-02 Organization requirements | C-32 |
| R-0713 | Provide evidence of continuous enforcement of technical controls. | producers | security | S-02 Organization requirements | C-33 |
| R-0714 | Document what the continuous controls mean. | producers | security | S-02 Organization requirements | C-33 |
| R-0715 | Give each repository a unique, stable locator. | platform providers | pipeline | S-02 Source Control System section | C-15 |
| R-0716 | Make revisions immutable and uniquely identifiable; non-digest IDs need documented immutability. | platform providers | pipeline | S-02 Source Control System section | C-15 |
| R-0717 | Show a human-readable change display for plain text. | platform providers | quality | S-02 Source Control System section | C-48 |
| R-0718 | Show a human-readable change display for non-plain-text content using interpretive tooling; this should be done. | platform providers | quality | S-02 Source Control System section | C-48 |
| R-0719 | Issue Source VSAs for revisions at Level 1 or higher. | platform providers | pipeline | S-02 Source Control System section | C-15 |
| R-0720 | Make Source VSAs fetchable by authorized consumers. | platform providers | pipeline | S-02 Source Control System section | C-15 |
| R-0721 | Treat revisions without a VSA as Level 0. | platform providers | pipeline | S-02 Source Control System section | C-15 |
| R-0722 | At Levels 1 and 2, VSAs may rely on design reviews. | platform providers | pipeline | S-02 Source Control System section | C-15 |
| R-0723 | At Level 2 or higher, VSAs must use SCS-issued provenance. | platform providers | pipeline | S-02 Source Control System section | C-15 |
| R-0724 | Record all changes to Named References. | platform providers | pipeline | S-02 History section | C-15 |
| R-0725 | Allow branches to move only to descendant revisions where ancestry exists. | platform providers | pipeline | S-02 History section | C-02 |
| R-0726 | Establish continuity from a start revision. | platform providers | pipeline | S-02 Continuity section | C-15 |
| R-0727 | Re-establish continuity after any lapse. | platform providers | pipeline | S-02 Continuity section | C-15 |
| R-0728 | Provide identity and authentication. | platform providers | security | S-02 Identity management section | C-21 |
| R-0729 | Let organizations specify actors and roles. | producers | security | S-02 Identity management section | C-21 |
| R-0730 | Document attribution. | platform providers | pipeline | S-02 Identity management section | C-15 |
| R-0731 | Attribute activities to authenticated identities; this should be done. | platform providers | pipeline | S-02 Identity management section | C-15 |
| R-0732 | Document the format and intent of source provenance. | platform providers | pipeline | S-02 Source provenance section | C-15 |
| R-0733 | Create source provenance at the same time as branch updates. | platform providers | pipeline | S-02 Source provenance section | C-15 |
| R-0734 | Make source provenance available to authorized consumers. | platform providers | pipeline | S-02 Source provenance section | C-15 |
| R-0735 | Provide controls for protected Named References. | platform providers | pipeline | S-02 Protected Named References section | C-02 |
| R-0736 | Provide a way to mark references as protected. | platform providers | pipeline | S-02 Protected Named References section | C-02 |
| R-0737 | Record enforced controls in attestations. | platform providers | pipeline | S-02 Protected Named References section | C-15 |
| R-0738 | Allow organization properties in VSAs. | platform providers | pipeline | S-02 Protected Named References section | 5 |
| R-0739 | Allow distribution of extra attestations. | platform providers | pipeline | S-02 Protected Named References section | C-15 |
| R-0740 | Enforce the ORG_SOURCE_ prefix for organization properties. | platform providers | pipeline | S-02 Protected Named References section | 5 |
| R-0741 | Require two or more trusted persons to agree before submission. | quality assurance | pipeline | S-02 Two-party review section | C-03 |
| R-0742 | Make the review cover security-relevant properties; this should be done. | quality assurance | quality | S-02 Two-party review section | C-48 |
| R-0743 | Require review of the final revision. | quality assurance | pipeline | S-02 Two-party review section | C-03 |
| R-0744 | Scope approvals to the context. | producers | pipeline | S-02 Two-party review section | C-03 |
| R-0745 | Show reviewers a clear representation of the change. | quality assurance | quality | S-02 Two-party review section | C-48 |
| R-0746 | A trusted robot may get a perpetual policy exception. | producers | pipeline | S-02 Two-party review section | C-03 |
| R-0747 | Include subject.uri in the Source VSA; this should be done. | producers | pipeline | S-02 Source VSA format section | 5 |
| R-0748 | Include subject.digest with the revision ID in the Source VSA. | producers | pipeline | S-02 Source VSA format section | 5 |
| R-0749 | Include sourceRefs as fully qualified git refs in the Source VSA; this should be done. | producers | pipeline | S-02 Source VSA format section | 5 |
| R-0750 | Include resourceUri in the Source VSA. | producers | pipeline | S-02 Source VSA format section | 5 |
| R-0751 | List only the highest level met in verifiedLevels. | producers | pipeline | S-02 Source VSA format section | 5 |
| R-0752 | Dependency levels in the VSA may be given. | consumers | pipeline | S-02 Source VSA format section | 5 |
| R-0753 | Enforce the ORG_SOURCE_ prefix on organization properties. | producers | pipeline | S-02 Source VSA format section | 5 |
| R-0754 | Organization properties for internal use may use the ORG_SOURCE_INTERNAL_ prefix. | producers | pipeline | S-02 Source VSA format section | 5 |
| R-0755 | An untrusted person may read and propose or review changes. | software engineers | security | S-02 Roles section | C-21 |
| R-0756 | An untrusted person may not approve or perform privileged actions. | software engineers | security | S-02 Roles section | C-21 |
| R-0757 | Build L4 could further harden the build platform and enable corroboration of provenance. | platform providers | pipeline | S-02 Build L4 | C-17 |
| R-0758 | The v0.1 "SLSA 4" requirements may or may not appear in a future Build L4; pinned dependencies, so each build uses the same inputs. | platform providers | pipeline | S-02 Build L4 | C-17 |
| R-0759 | The v0.1 "SLSA 4" requirements may or may not appear in a future Build L4; hermetic builds, with no extraneous dependencies. | platform providers | pipeline | S-02 Build L4 | C-17 |
| R-0760 | The v0.1 "SLSA 4" requirements may or may not appear in a future Build L4; all dependencies listed in provenance, so verifiers can apply SLSA recursively. | platform providers | pipeline | S-02 Build L4 | C-17 |
| R-0761 | The v0.1 "SLSA 4" requirements may or may not appear in a future Build L4; reproducible builds, so other platforms can corroborate provenance. | platform providers | pipeline | S-02 Build L4 | C-17 |
| R-0762 | A future Platform Operations track could offer assurances about hardening build or source platforms during operation. | platform providers | security | S-02 Platform Operations track | C-31 |
| R-0763 | Approval, logging and auditing of physical and remote access to platform infrastructure, cryptographic secrets and privileged debugging interfaces may or may not be a future requirement. | platform providers | security | S-02 Platform Operations track | C-32 |
| R-0764 | Conformance to security best practices to minimise the risk of compromise may or may not be a future requirement. | platform providers | security | S-02 Platform Operations track | C-31 |
| R-0765 | Protection of cryptographic secrets used by the build platform may or may not be a future requirement. | platform providers | pipeline | S-02 Platform Operations track | C-09 |
| R-0766 | Organizations should ensure that their people, processes and technology are prepared to perform secure software development. | producers | security | S-03 page 8 | C-20 |
| R-0767 | Organizations should protect all components of their software from tampering and unauthorized access. | producers | security | S-03 page 8 | C-34 |
| R-0768 | Organizations should produce well-secured software with minimal security vulnerabilities in its releases. | producers | security | S-03 page 8 | C-38 |
| R-0769 | Organizations should identify residual vulnerabilities in their software releases and respond appropriately to address them and prevent similar ones. | producers | security | S-03 page 8 | C-36 |
| R-0770 | Organizations should integrate the SSDF throughout their existing software development practices. | producers | quality | S-03 page 8 | C-73 |
| R-0771 | Organizations should express their secure software development requirements to third-party suppliers using SSDF conventions. | consumers | operations | S-03 page 8 | C-66 |
| R-0772 | Organizations should acquire software that meets the practices described in the SSDF. | consumers | security | S-03 page 8 | C-28 |
| R-0773 | Organizations should consult the references and other resources for information on implementing the practices. | producers | quality | S-03 page 8 | C-73 |
| R-0774 | Organizations should adopt a risk-based approach to determine which practices are relevant, appropriate and effective. | management | security | S-03 page 8 | C-20 |
| R-0775 | Secure software development practices should be integrated throughout the SDLC, whichever SDLC model is used. | producers | quality | S-03 page 10 | C-73 |
| R-0776 | The practices should not negatively affect organizations that already have robust secure software development practices. | producers | quality | S-03 page 11 | C-73 |
| R-0777 | Factors such as risk, cost, feasibility and applicability should be considered when deciding which practices to use and how much effort to give each. | management | security | S-03 page 12 | C-20 |
| R-0778 | The tenant organization should establish an agreement with providers that states which party is responsible for each practice and task and how each provider attests to conformance. | consumers | operations | S-03 page 12 | C-66 |
| R-0779 | Organizations adopting the SSDF should define the terms sensitive data, qualified person and well-secured in their own environments and use cases. | producers | security | S-03 page 13 | C-38 |
| R-0780 | Practice group PO: organizations should ensure that their people, processes and technology are prepared for secure development at the organization level. | producers | security | S-03 page 13 | C-19 |
| R-0781 | Practice group PS: organizations should protect all components of their software from tampering and unauthorized access. | producers | security | S-03 page 13 | C-34 |
| R-0782 | Practice group PW: organizations should produce well-secured software with minimal security vulnerabilities in its releases. | producers | security | S-03 page 13 | C-38 |
| R-0783 | Practice group RV: organizations should identify residual vulnerabilities and respond appropriately to them. | producers | security | S-03 page 13 | C-36 |
| R-0784 | PO.1.1: Identify and document all security requirements for organization software development, including internal and external sources, and maintain them over time. | producers | security | S-03 page 14 | C-18 |
| R-0785 | PO.1.2: Identify and document all security requirements for organization-developed software, and maintain them over time. | producers | security | S-03 page 14 | C-18 |
| R-0786 | PO.1.3: Communicate requirements to all third parties who provide commercial software components for reuse by the organization. | producers | operations | S-03 page 14 | C-66 |
| R-0787 | PO.2.1: Create new roles and alter responsibilities as needed to cover all parts of the SDLC, and review and maintain them periodically. | producers | security | S-03 page 15 | C-19 |
| R-0788 | PO.2.2: Provide role-based training for all personnel with responsibilities that contribute to secure development, and review proficiency and training periodically. | security roles | security | S-03 page 15 | C-19 |
| R-0789 | PO.2.3: Obtain upper management or authorizing official commitment to secure development and convey it to all with development-related roles. | management | security | S-03 page 16 | C-20 |
| R-0790 | PO.3.1: Specify which tools or tool types must or should be included in each toolchain to mitigate identified risks, and how the components are integrated. | producers | security | S-03 page 16 | C-33 |
| R-0791 | PO.3.2: Follow recommended security practices to deploy, operate and maintain tools and toolchains. | producers | security | S-03 page 16 | C-31 |
| R-0792 | PO.3.3: Configure tools to generate artifacts of their support of secure software development practices as defined by the organization. | producers | security | S-03 page 16 | C-33 |
| R-0793 | PO.4.1: Define criteria for software security checks and track them throughout the SDLC. | producers | security | S-03 page 17 | C-33 |
| R-0794 | PO.4.2: Implement processes and mechanisms to gather and safeguard the information needed to support the criteria. | producers | security | S-03 page 17 | C-33 |
| R-0795 | PO.5.1: Separate and protect each environment involved in software development. | producers | security | S-03 page 17 | C-31 |
| R-0796 | PO.5.2: Secure and harden development endpoints to perform development tasks using a risk-based approach. | software engineers | security | S-03 page 18 | C-31 |
| R-0797 | PS.1.1: Store all forms of code in a repository and restrict access based on the nature of the code and the principle of least privilege. | producers | security | S-03 page 18 | C-21 |
| R-0798 | PS.2.1: Make software integrity verification information available to software acquirers. | consumers | pipeline | S-03 page 19 | C-10 |
| R-0799 | PS.3.1: Securely archive the necessary files and supporting data for each software release, and allow read-only access to necessary personnel. | producers | security | S-03 page 19 | C-34 |
| R-0800 | PS.3.2: Collect, safeguard, maintain and share provenance data for all components of each software release. | producers | pipeline | S-03 page 19 | C-08 |
| R-0801 | PW.1.1: Use forms of risk modeling to assess the security risk for the software. | producers | security | S-03 page 20 | C-27 |
| R-0802 | PW.1.2: Track and maintain the software security requirements, risks and design decisions. | producers | security | S-03 page 20 | C-18 |
| R-0803 | PW.1.3: Where appropriate, build in support for standardized security features and services instead of proprietary implementations. | producers | security | S-03 page 20 | C-29 |
| R-0804 | PW.2.1: Have a qualified person or automated processes in the toolchain review the software design to confirm compliance with security requirements and risk information. | producers | security | S-03 page 21 | C-27 |
| R-0805 | PW.4.1: Acquire and maintain well-secured software components from commercial, open-source and other third-party developers. | producers | security | S-03 page 21 | C-28 |
| R-0806 | PW.4.2: Create and maintain well-secured components in-house to meet common internal needs that third-party components cannot better meet. | producers | security | S-03 page 21 | C-28 |
| R-0807 | PW.4.4: Verify that acquired third-party components comply with the organization requirements throughout their life cycles. | producers | security | S-03 page 22 | C-28 |
| R-0808 | PW.5.1: Follow all secure coding practices appropriate to the development languages and environment to meet the organization requirements. | software engineers | security | S-03 page 22 | C-29 |
| R-0809 | PW.6.1: Use compiler, interpreter and build tools that offer features to improve executable security. | producers | security | S-03 page 23 | C-29 |
| R-0810 | PW.6.2: Determine which compiler, interpreter and build tool features should be used and how each should be configured, then implement the approved configurations. | producers | security | S-03 page 23 | C-29 |
| R-0811 | PW.7.1: Determine whether code review and/or code analysis should be performed and how. | producers | quality | S-03 page 23 | C-48 |
| R-0812 | PW.7.2: Perform code review and/or code analysis based on the organization secure coding standards, and record and triage all issues and remediations. | producers | security | S-03 page 23 | C-24 |
| R-0813 | PW.8.1: Determine whether executable code testing should be performed to find vulnerabilities not found by earlier reviews, analysis or testing. | producers | security | S-03 page 24 | C-26 |
| R-0814 | PW.8.2: Scope and design the tests, perform them, and document the results, including recording and triaging all issues and remediations. | producers | security | S-03 page 24 | C-26 |
| R-0815 | PW.9.1: Define a secure baseline by determining how to configure each setting that affects security. | producers | security | S-03 page 25 | C-30 |
| R-0816 | PW.9.2: Implement the default settings and document each setting for software administrators. | producers | security | S-03 page 25 | C-30 |
| R-0817 | RV.1.1: Gather information from software acquirers, users and public sources on potential vulnerabilities, and investigate all credible reports. | producers | security | S-03 page 25 | C-35 |
| R-0818 | RV.1.2: Review, analyze and/or test the software code to identify or confirm previously undetected vulnerabilities. | producers | security | S-03 page 25 | C-26 |
| R-0819 | Have a policy that addresses vulnerability disclosure and remediation, and implement the roles, responsibilities and processes that support it. | producers | security | S-03 page 26 (RV.1.3) | C-35 |
| R-0820 | Establish a vulnerability disclosure program that makes it easy for security researchers to learn about it and report possible vulnerabilities. | producers | security | S-03 page 26 (RV.1.3, Example 1) | C-35 |
| R-0821 | Have a Product Security Incident Response Team and processes that handle responses to vulnerability reports and incidents, including communication plans for all stakeholders. | security roles | security | S-03 page 26 (RV.1.3, Example 2) | C-35 |
| R-0822 | Have a security response playbook for a generic reported vulnerability, a zero-day report, a vulnerability exploited in the wild, and a major ongoing multi-party incident involving open-source components. | security roles | security | S-03 page 26 (RV.1.3, Example 3) | C-35 |
| R-0823 | Periodically conduct exercises of the product security incident response processes. | security roles | security | S-03 page 26 (RV.1.3, Example 4) | C-38 |
| R-0824 | Analyze each vulnerability to gather enough information about risk to plan its remediation or other risk response. | security roles | security | S-03 page 26 (RV.2.1) | C-36 |
| R-0825 | Use existing issue tracking software to record each vulnerability. | software engineers | security | S-03 page 26 (RV.2.1, Example 1) | C-36 |
| R-0826 | Perform risk calculations for each vulnerability based on estimates of its exploitability, potential impact and other relevant characteristics. | security roles | security | S-03 page 26 (RV.2.1, Example 2) | C-36 |
| R-0827 | Plan and implement risk responses for vulnerabilities. | security roles | security | S-03 page 27 (RV.2.2) | C-36 |
| R-0828 | Make a risk-based decision whether each vulnerability is remediated or addressed by other means such as risk acceptance or transference, and prioritize the actions. | management | security | S-03 page 27 (RV.2.2, Example 1) | C-36 |
| R-0829 | If no permanent mitigation exists, determine a temporary mitigation and add it to the plan. | security roles | security | S-03 page 27 (RV.2.2, Example 2) | C-36 |
| R-0830 | Develop and release security advisories that give acquirers the information needed about the vulnerabilities, how to find affected instances, and how to address them. | consumers | security | S-03 page 27 (RV.2.2, Example 3) | C-35 |
| R-0831 | Deliver remediations to acquirers through an automated and trusted delivery mechanism. | consumers | security | S-03 page 27 (RV.2.2, Example 4) | C-36 |
| R-0832 | Update records of design decisions, risk responses and approved exceptions as needed. | security roles | security | S-03 page 27 (RV.2.2, Example 5) | C-27 |
| R-0833 | Analyze identified vulnerabilities to determine their root causes. | security roles | security | S-03 page 27 (RV.3.1) | C-36 |
| R-0834 | Record the root cause of discovered issues. | security roles | security | S-03 page 27 (RV.3.1, Example 1) | C-36 |
| R-0835 | Record lessons learned from root cause analysis in a wiki that developers can access and search. | software engineers | security | S-03 page 27 (RV.3.1, Example 2) | C-36 |
| R-0836 | Analyze root causes over time to identify patterns, such as a secure coding practice that is not followed consistently. | security roles | security | S-03 page 27 (RV.3.2) | C-36 |
| R-0837 | Add mechanisms to the toolchain that automatically detect future instances of a root cause. | security roles | security | S-03 page 27 (RV.3.2, Example 2) | C-24 |
| R-0838 | Update manual processes to detect future instances of a root cause. | security roles | security | S-03 page 27 (RV.3.2, Example 3) | C-36 |
| R-0839 | Review the software for similar vulnerabilities to eradicate a class of vulnerabilities, and fix them proactively rather than wait for external reports. | security roles | security | S-03 page 27 (RV.3.3) | C-36 |
| R-0840 | Review the SDLC process and update it if appropriate to prevent or reduce the likelihood of a root cause recurring. | management | quality | S-03 page 27 (RV.3.4) | C-73 |
| R-0841 | Plan and implement changes to the appropriate SDLC practices. | management | quality | S-03 page 27 (RV.3.4, Example 2) | C-73 |
| R-0842 | Thus, SSC security assurance measures must be integrated into CI/CD pipelines in the context of cloud-native applications. | producers | security | S-04 page 11 | C-33 |
| R-0843 | The SBOM must be shared with end users so that they can build inventories of software components. | consumers | pipeline | S-04 page 13 | C-13 |
| R-0844 | SSC security should also account for discovering and tracking software security defects rather than only mitigating attacks. | security roles | security | S-04 page 13 | C-36 |
| R-0845 | Companies should be aware of supply chain risks and take appropriate measures. | management | security | S-04 page 17 | C-20 |
| R-0846 | Organizations should be aware of insider situations and take suitable measures to avoid poor practices. | management | security | S-04 page 17 | C-20 |
| R-0847 | Developer workstations should not be trusted as part of the build process. | software engineers | pipeline | S-04 page 17 | C-06 |
| R-0848 | Companies should identify potential risks and vulnerabilities, assess their security posture and implement defensive measures. | management | security | S-04 page 18 | C-20 |
| R-0849 | It is essential to verify the provenance information of a component that is used. | consumers | pipeline | S-04 page 18 | C-11 |
| R-0850 | Companies should identify critical assets and implement controls to protect them. | management | security | S-04 page 18 | C-20 |
| R-0851 | Organizations should regularly assess their security posture, identify weaknesses and implement defensive measures. | management | security | S-04 page 20 | C-20 |
| R-0852 | Organizations should ensure that their SDLC environment remains compliant with security and other relevant standards. | auditors and regulators | security | S-04 page 20 | C-33 |
| R-0853 | All developer systems should meet a predefined minimum baseline for security. | software engineers | security | S-04 page 20 | C-31 |
| R-0854 | Government and enterprise environments should establish and adhere to a well-defined security policy. | management | security | S-04 page 20 | C-38 |
| R-0855 | Readers should refer to SP 800-53r5 for a more complete treatment of security policy. | management | security | S-04 page 20 | C-38 |
| R-0856 | The security team should establish a policy for trusted sources of open-source software. | security roles | security | S-04 page 21 | C-28 |
| R-0857 | The security team should approve the merging of unverified sources of open-source software. | security roles | security | S-04 page 21 | C-28 |
| R-0858 | Developers should download open-source software as source code, when available. | software engineers | security | S-04 page 21 | C-28 |
| R-0859 | Developers should verify digital signatures, run vulnerability scans and generate an SBOM on the first commit. | software engineers | security | S-04 page 21 | C-28 |
| R-0860 | Artifacts should be scanned in internal repositories, and their use in builds should be stopped based on criticality. | security roles | security | S-04 page 21 | C-25 |
| R-0861 | CI/CD processes should be audited regularly, and automation should be introduced where possible. | security roles | security | S-04 page 21 | C-32 |
| R-0862 | There should be an isolated CI/CD environment and elevated administrator credentials for cloud deployment. | operations engineers | security | S-04 page 21 | C-31 |
| R-0863 | There should be enhanced real-time monitoring and alerting to detect suspicious activity in CI/CD servers. | operations engineers | security | S-04 page 21 | C-32 |
| R-0864 | Write access to the SCM should be considered a high risk and tightly controlled. | platform providers | security | S-04 page 21 | C-21 |
| R-0865 | Another developer should perform a code review before a patch is merged. | software engineers | pipeline | S-04 page 21 | C-03 |
| R-0866 | Code analysis tools should be implemented, and care should be taken to avoid too many false positives. | software engineers | security | S-04 page 21 | C-24 |
| R-0867 | The generation of provenance data should be accompanied by mechanisms to validate, authenticate and use them in policy decisions. | platform providers | security | S-04 page 22 | C-33 |
| R-0868 | The entities that perform SSC activities should be authenticated through verification of credentials. | platform providers | security | S-04 page 23 | C-21 |
| R-0869 | Permissions or access rights should be assigned to those entities through authorization under enterprise policies. | platform providers | security | S-04 page 23 | C-21 |
| R-0870 | The integrity of artifacts and repositories should be ensured through verification of digital signatures. | consumers | pipeline | S-04 page 23 | C-11 |
| R-0871 | The establishment of trust should be a recurring process throughout the CI/CD system. | platform providers | security | S-04 page 23 | C-33 |
| R-0872 | The inputs and outputs of each build step should be verified to ensure the correct steps were executed by the expected entity. | consumers | pipeline | S-04 page 23 | C-11 |
| R-0873 | Harden the CI/CD execution environment to reduce its attack surface. | platform providers | security | S-04 page 24 | C-31 |
| R-0874 | Define roles for the actors who operate the CI/CD pipelines, such as application updaters, package managers and deployment specialists. | operations engineers | security | S-04 page 24 | C-19 |
| R-0875 | Identify the granular authorizations for tasks such as generating and committing code, generating builds and packages, and checking artifacts into and out of repositories. | operations engineers | security | S-04 page 24 | C-21 |
| R-0876 | Automate the entire CI/CD pipeline through appropriate tools. | operations engineers | operations | S-04 page 24 | C-62 |
| R-0877 | Define CI/CD pipeline activities and security requirements for application code, infrastructure as code, and policy and configuration code. | software engineers | security | S-04 page 24 | C-18 |
| R-0878 | Specify build policies covering a secure isolated build platform, hardened build servers, the build tools, and authentication and authorization of developers. | platform providers | pipeline | S-04 page 25 | C-09 |
| R-0879 | Enforce the build policies with techniques such as an agent and a policy enforcement engine. | platform providers | security | S-04 page 25 | C-33 |
| R-0880 | Ensure that evidence for build attestation is generated concurrently during software delivery. | platform providers | pipeline | S-04 page 25 | C-08 |
| R-0881 | The build platform components, such as the compiler and interpreter, must be hardened, isolated and secure. | platform providers | security | S-04 page 25 | C-31 |
| R-0882 | Evidence should be generated by a process with a higher level of trust or isolation than the build itself. | platform providers | pipeline | S-04 page 25 | C-08 |
| R-0883 | Process attestation should be considered best effort. | platform providers | pipeline | S-04 page 25 | C-08 |
| R-0884 | The build system should confirm that the tools or processes used run in an isolated environment. | platform providers | pipeline | S-04 page 25 | C-09 |
| R-0885 | The hash of the final build artifact and its materials should be gathered and signed by a trusted component that the developers do not control. | platform providers | pipeline | S-04 page 25 | C-08 |
| R-0886 | Attestations must be cryptographically signed using a secure key. | platform providers | pipeline | S-04 page 26 | C-08 |
| R-0887 | The storage location for attestations must be tamper-proof and protected by robust access control. | platform providers | security | S-04 page 26 | C-34 |
| R-0888 | The type of authentication for developers who pull and push code must be consistent with their role. | software engineers | security | S-04 page 26 | C-21 |
| R-0889 | Developers with merge approval permissions cannot approve their own merges. | software engineers | pipeline | S-04 page 26 | C-03 |
| R-0890 | Checks on the integrity of repository code are required, so that the code can be trusted for further updates. | platform providers | pipeline | S-04 page 26 | C-15 |
| R-0891 | The project maintainer should run automated checks on all artifacts covered by the change being pushed, such as unit tests, linters, integrity tests and security checks. | producers | quality | S-04 page 27 | C-39 |
| R-0892 | CI pipelines should only be run with tools when confidence is established in the trustworthiness of the source-code origin of those tools. | platform providers | security | S-04 page 27 | C-23 |
| R-0893 | The repository or SCM system should either run CI workflows in sandboxed environments without network access, privileged access or the ability to read secrets, or have built-in protection that delays CI runs until a maintainer with write access approves them. | platform providers | security | S-04 page 27 | C-23 |
| R-0894 | The built-in protection should take effect when an outside contributor submits a pull request to a public repository. | platform providers | security | S-04 page 27 | C-23 |
| R-0895 | The protection setting should be at the strictest level, such as requiring approval for all outside collaborators. | platform providers | security | S-04 page 27 | C-23 |
| R-0896 | If the SCM system has no built-in protection, external security tools are required that evaluate and enhance the SCM security posture, with or without a policy, and produce a status report with recommendations. | platform providers | security | S-04 page 27 | C-33 |
| R-0897 | If the SCM system has no built-in protection, external security tools are required that detect and remediate misconfigurations, security vulnerabilities and compliance issues. | platform providers | security | S-04 page 27 | C-33 |
| R-0898 | The software update framework should protect the signing operation by requiring the build policy to be satisfied before signing. | producers | security | S-04 page 28 | C-33 |
| R-0899 | The framework should protect against all known attacks on the tasks performed by software update systems. | producers | pipeline | S-04 page 28 | 5 |
| R-0900 | The framework should minimize the impact of key compromise by supporting roles with multiple keys and threshold or quorum trust, except for minimally trusted roles that use a single key. | producers | pipeline | S-04 page 28 | 5 |
| R-0901 | Online keys should not be used for any role that clients ultimately trust for files they may install. | producers | security | S-04 page 28 | C-22 |
| R-0902 | When keys are online, exceptional care should be taken, such as storing them in a hardware security module and using them only if the signed artifacts pass the build policy. | producers | security | S-04 page 28 | C-22 |
| R-0903 | The framework must be flexible enough to meet the needs of a wide variety of software update systems. | producers | pipeline | S-04 page 28 | 5 |
| R-0904 | The framework must be easy to integrate with software update systems. | producers | pipeline | S-04 page 28 | 5 |
| R-0905 | Appropriate forms of testing should be performed before code commits. | software engineers | quality | S-04 page 28 | C-39 |
| R-0906 | SAST and DAST tools covering all languages used in development should run in CI/CD pipelines, with code coverage reports provided to developers and security personnel. | software engineers | security | S-04 page 28 | C-24 |
| R-0907 | Dependencies of open-source modules and libraries must be enumerated, understood and evaluated for policy, potentially with SCA tools. | software engineers | security | S-04 page 29 | C-25 |
| R-0908 | The security conditions for including open-source dependencies must be tested. | security roles | security | S-04 page 29 | C-25 |
| R-0909 | Dependency file detectors should detect all dependencies, including transitive dependencies, preferably with no depth limit. | software engineers | security | S-04 page 29 | C-25 |
| R-0910 | Prevention of secrets in committed code is required. | software engineers | security | S-04 page 29 | C-22 |
| R-0911 | Committed code should be evaluated for adherence to organizational policy, including the absence of secrets such as keys and API tokens. | software engineers | security | S-04 page 29 | C-22 |
| R-0912 | Detected secrets should be displayed prominently, alerts should be generated on policy violations, and documented methods to remediate violations should exist. | security roles | security | S-04 page 29 | C-22 |
| R-0913 | Push protection should be enabled for all repositories assigned to an administrator. | operations engineers | security | S-04 page 29 | C-22 |
| R-0914 | Push protection should verify developer identity and authorization, enforce developer signing of code commits, and verify file names. | software engineers | pipeline | S-04 page 29 | C-15 |
| R-0915 | For code ready for deployment, a security scanning sub-feature should be invoked to detect secrets such as keys and access tokens. | software engineers | security | S-04 page 29 | C-22 |
| R-0916 | The repository should be scanned for secrets even before it is populated with code. | software engineers | security | S-04 page 29 | C-22 |
| R-0917 | Before merging pull requests, it should be possible to view details of vulnerable versions through dependency review. | software engineers | security | S-04 page 29 | C-25 |
| R-0918 | It should be possible to specify that a deployed artifact, such as a container image, must have been generated by the secure build process to be cleared for deployment. | operations engineers | pipeline | S-04 page 29 | C-11 |
| R-0919 | There should be evidence that the container image was scanned for vulnerabilities and attested for the findings. | security roles | security | S-04 page 30 | C-33 |
| R-0920 | It should be possible to allow or block image deployment based on organization-defined policies. | operations engineers | security | S-04 page 30 | C-33 |
| R-0921 | Release build scripts should be checked periodically for malicious code. | security roles | security | S-04 page 30 | C-32 |
| R-0922 | A container image should be scanned for vulnerabilities as soon as it is built, even before it is pushed to a registry. | operations engineers | security | S-04 page 30 | C-25 |
| R-0923 | Tools that interact with repositories of container images and language packages should be capable of integration with CD tools. | operations engineers | operations | S-04 page 30 | C-54 |
| R-0924 | The GitOps process should rely on automation rather than manual operations. | operations engineers | operations | S-04 page 30 | C-54 |
| R-0925 | Package managers that facilitate GitOps should preserve all data on released packages, including module version numbers, configuration files and metadata. | operations engineers | pipeline | S-04 page 30 | C-10 |
| R-0926 | Changes should not be applied manually at runtime; changes should be made in the code and a new release triggered. | operations engineers | operations | S-04 page 31 | C-54 |
| R-0927 | The Git repository should be pulled automatically and compared with the specified configuration state, to monitor and remediate drift. | operations engineers | operations | S-04 page 31 | C-54 |
| R-0928 | Administrators can choose to resync configurations automatically to the defined state. | operations engineers | operations | S-04 page 31 | C-54 |
| R-0929 | Notifications should be sent about configuration differences, and manual remediation should be performed. | operations engineers | operations | S-04 page 31 | C-54 |
| R-0930 | The entire CI/CD pipeline must be automated through appropriate tools as a prerequisite for activating CI/CD pipelines. | operations engineers | operations | S-04 page 36 | C-62 |
| R-0931 | Check for evidence that the container image was scanned for vulnerabilities and attested for the findings. | consumers | security | S-04 page 36 | C-25 |
| R-0932 | Online keys must not be used for any role that clients ultimately trust for files they may install. | producers | pipeline | S-04 page 37 | 5 |
| R-0933 | SAST and DAST tools used in CI/CD pipelines must provide coverage for the different language systems used in cloud-native applications. | security roles | security | S-04 page 40 | C-24 |
| R-0934 | PULL-PUSH-REQ-3 in the table: the repository or SCM system should have built-in protection that delays CI runs until a maintainer with write access approves them. | platform providers | security | S-04 page 39 | C-23 |
| R-0935 | PULL-PUSH-REQ-2 in the table: CI pipelines should only use external tools, such as Jenkins, when confidence is established in the trustworthiness of the source-code origin. | producers | security | S-04 page 39 | C-23 |
| R-0936 | Map credentials across the ecosystem and apply least privilege. | security roles | security | S-05 CICD-SEC-6 page, Recommendations | C-21 |
| R-0937 | Avoid sharing one credential set across multiple contexts. | security roles | security | S-05 CICD-SEC-6 page, Recommendations | C-21 |
| R-0938 | Prefer temporary credentials; if static credentials are needed, rotate them periodically and detect stale ones. | security roles | security | S-05 CICD-SEC-6 page, Recommendations | C-22 |
| R-0939 | Restrict credential use to predetermined conditions, such as source IP or identity. | security roles | security | S-05 CICD-SEC-6 page, Recommendations | C-21 |
| R-0940 | Detect secrets in repositories through IDE plugins, push-time scanning, and scans of past commits. | software engineers | security | S-05 CICD-SEC-6 page, Recommendations | C-22 |
| R-0941 | Scope CI/CD secrets so that each pipeline and each step gets only what it needs. | software engineers | pipeline | S-05 CICD-SEC-6 page, Recommendations | C-07 |
| R-0942 | Prevent secrets from appearing in console output, and verify that image layers, binaries and Helm charts contain no secrets. | software engineers | security | S-05 CICD-SEC-6 page, Recommendations | C-22 |
| R-0943 | Pipelines that run unreviewed code should run on isolated nodes that are not exposed to secrets or sensitive environments. | platform providers | security | S-05 CICD-SEC-4 page, Statements on Secrets and Credentials | C-23 |
| R-0944 | Sensitive pipelines should have branch protection rules that match each CI-triggering branch. | producers | pipeline | S-05 CICD-SEC-4 page, Statements on Secrets and Credentials | C-02 |
| R-0945 | Each pipeline should access only the credentials it needs, with the minimum required privileges. | software engineers | pipeline | S-05 CICD-SEC-4 page, Statements on Secrets and Credentials | C-07 |
| R-0946 | Maintainers should enable branch protection settings in the source hosting provider. | producers | pipeline | S-06 Branch-Protection check, remediation | C-02 |
| R-0947 | Branch protection must prevent force pushes and branch deletion to reach Tier 1. | producers | pipeline | S-06 Branch-Protection check, tier 1 | C-02 |
| R-0948 | Branch protection must require at least one approving reviewer before merge to reach Tier 2. | producers | pipeline | S-06 Branch-Protection check, tier 2 | C-03 |
| R-0949 | Branch protection must require at least one passing status check to reach Tier 3. | producers | quality | S-06 Branch-Protection check, tier 3 | C-39 |
| R-0950 | Branch protection must require at least two reviewers and review from code owners to reach Tier 4. | producers | pipeline | S-06 Branch-Protection check, tier 4 | C-03 |
| R-0951 | Administrators must be included in review, and stale approvals must be dismissed on new pushes, to reach Tier 5. | producers | pipeline | S-06 Branch-Protection check, tier 5 | C-03 |
| R-0952 | Code reviews must be made mandatory in the repository configuration. | producers | pipeline | S-06 Code-Review check, remediation | C-03 |
| R-0953 | Code review rules must be enforced for administrators and code owners. | producers | pipeline | S-06 Code-Review check, remediation | C-03 |
| R-0954 | Strict reviews must be performed for every pull request. | producers | pipeline | S-06 Code-Review check, remediation | C-03 |
| R-0955 | Reviewers must be human to count as a review. | quality assurance | pipeline | S-06 Code-Review check | C-03 |
| R-0956 | Maintainers should ask contributors to join their organizations if they have not already. | producers | security | S-06 Contributors check, remediation | C-37 |
| R-0957 | Projects should set top-level workflow permissions to read-all or contents read. | producers | pipeline | S-06 Token-Permissions check, remediation | C-07 |
| R-0958 | Projects should set required write permissions at job level. | producers | pipeline | S-06 Token-Permissions check, remediation | C-07 |
| R-0959 | Projects must not set permissions write-all at job level. | producers | pipeline | S-06 Token-Permissions check, remediation | C-07 |
| R-0960 | Maintainers should generate a signing key, sign the release archive, and attach the signature file. | producers | pipeline | S-06 Signed-Releases check, remediation | C-10 |
| R-0961 | Maintainers should avoid the dangerous workflow patterns. | producers | security | S-06 Dangerous-Workflow check, remediation | C-23 |
| R-0962 | Maintainers should declare dependencies with specific versions. | producers | pipeline | S-06 Pinned-Dependencies check, remediation | C-14 |
| R-0963 | Maintainers should check in lock files. | producers | pipeline | S-06 Pinned-Dependencies check, remediation | C-14 |
| R-0964 | Maintainers should pin Docker and workflow dependencies by hash. | producers | pipeline | S-06 Pinned-Dependencies check, remediation | C-14 |
| R-0965 | Maintainers should use dependency update tools. | producers | pipeline | S-06 Pinned-Dependencies check, remediation | C-14 |
| R-0966 | Maintainers should recruit more maintainers if review capacity is thin. | producers | security | S-06 Stakeholders and Roles, Maintainers | C-37 |
| R-0967 | The project must require multi-factor authentication to read or change sensitive resources in the authoritative repository. | producers | security | S-07 version page, Level 1, AC-01.01 | C-21 |
| R-0968 | The project must assign permissions to new collaborators manually, or must give them the lowest privileges by default. | producers | security | S-07 version page, Level 1, AC-02.01 | C-21 |
| R-0969 | The project must block direct commits to the primary branch. | producers | pipeline | S-07 version page, Level 1, AC-03.01 | C-02 |
| R-0970 | The project must treat deletion of the primary branch as a sensitive action and must require explicit confirmation. | producers | pipeline | S-07 version page, Level 1, AC-03.02 | C-02 |
| R-0971 | The project must sanitize and validate untrusted metadata, such as branch names and pull request titles, before pipeline use. | producers | security | S-07 version page, Level 1, BR-01.01 | C-23 |
| R-0972 | The project must keep untrusted code snapshots away from privileged CI/CD credentials and assets. | producers | security | S-07 version page, Level 1, BR-01.03 | C-23 |
| R-0973 | The project must deliver official URIs only over encrypted channels. | producers | security | S-07 version page, Level 1, BR-03.01 | C-34 |
| R-0974 | The project must protect official distribution channels against man-in-the-middle attacks. | producers | security | S-07 version page, Level 1, BR-03.02 | C-34 |
| R-0975 | The project must prevent unencrypted secrets and credentials from being committed to version control. | producers | security | S-07 version page, Level 1, BR-07.01 | C-22 |
| R-0976 | The project must provide user guides for basic functionality after a release. | producers | security | S-07 version page, Level 1, DO-01.01 | C-37 |
| R-0977 | The project must provide a guide for reporting defects after a release. | producers | security | S-07 version page, Level 1, DO-02.01 | C-35 |
| R-0978 | The project must provide at least one public discussion mechanism. | producers | security | S-07 version page, Level 1, GV-02.01 | C-37 |
| R-0979 | The project must explain its contribution process, or must state that contributions are not accepted. | producers | security | S-07 version page, Level 1, GV-03.01 | C-37 |
| R-0980 | The source license must meet the OSI or FSF free-software definition. | producers | security | S-07 version page, Level 1, LE-02.01 | C-37 |
| R-0981 | The released-asset license must meet the OSI or FSF definition. | producers | security | S-07 version page, Level 1, LE-02.02 | C-37 |
| R-0982 | The source license must be in a standard license file or directory in the repository. | producers | security | S-07 version page, Level 1, LE-03.01 | C-37 |
| R-0983 | The release license must ship with the source or alongside the release assets. | producers | security | S-07 version page, Level 1, LE-03.02 | C-37 |
| R-0984 | The repository must be publicly readable at a static URL. | producers | pipeline | S-07 version page, Level 1, QA-01.01 | C-01 |
| R-0985 | The project must keep a public, attributable change history that shows who, what and when. | producers | pipeline | S-07 version page, Level 1, QA-01.02 | C-15 |
| R-0986 | The repository must include a direct-dependency list where the package system supports it. | producers | pipeline | S-07 version page, Level 1, QA-02.01 | C-13 |
| R-0987 | Multi-repository projects must document their codebases. | producers | security | S-07 version page, Level 1, QA-04.01 | C-37 |
| R-0988 | The repository must not contain generated executables. | producers | pipeline | S-07 version page, Level 1, QA-05.01 | C-01 |
| R-0989 | The repository must not contain unreviewable binary artifacts. | producers | pipeline | S-07 version page, Level 1, QA-05.02 | C-01 |
| R-0990 | The project must document its security contacts. | producers | security | S-07 version page, Level 1, VM-02.01 | C-35 |
| R-0991 | CI/CD tasks with no permissions specified must default to the pipeline's lowest permissions. | producers | pipeline | S-07 version page, Level 2, AC-04.01 | C-07 |
| R-0992 | Each official release must get a unique version identifier. | producers | pipeline | S-07 version page, Level 2, BR-02.01 | C-10 |
| R-0993 | Each release must include a change log of functional and security changes. | producers | pipeline | S-07 version page, Level 2, BR-04.01 | C-10 |
| R-0994 | Build pipelines must use standard dependency tooling. | producers | pipeline | S-07 version page, Level 2, BR-05.01 | C-14 |
| R-0995 | Releases must be signed, or must be listed with hashes in a signed manifest. | producers | pipeline | S-07 version page, Level 2, BR-06.01 | C-10 |
| R-0996 | The project must document how dependencies are selected, obtained and tracked. | producers | security | S-07 version page, Level 2, DO-06.01 | C-28 |
| R-0997 | The project must document build instructions, including libraries, SDKs and dependencies. | producers | pipeline | S-07 version page, Level 2, DO-07.01 | C-04 |
| R-0998 | The project must list the members who have access to sensitive resources. | producers | security | S-07 version page, Level 2, GV-01.01 | C-21 |
| R-0999 | The project must describe member roles and responsibilities. | producers | security | S-07 version page, Level 2, GV-01.02 | C-37 |
| R-1000 | The contributor guide must state the requirements for acceptable contributions. | producers | security | S-07 version page, Level 2, GV-03.02 | C-37 |
| R-1001 | The project must require contributors to assert legal authority on every commit, by DCO or CLA. | producers | security | S-07 version page, Level 2, LE-01.01 | C-37 |
| R-1002 | Status checks must pass, or must be bypassed manually, before commits to the primary branch. | producers | quality | S-07 version page, Level 2, QA-03.01 | C-39 |
| R-1003 | CI must run at least one automated test suite before acceptance. | producers | quality | S-07 version page, Level 2, QA-06.01 | C-39 |
| R-1004 | Design documentation must cover all actors and actions. | producers | security | S-07 version page, Level 2, SA-01.01 | C-27 |
| R-1005 | The project must document all external interfaces of released assets. | producers | quality | S-07 version page, Level 2, SA-02.01 | C-69 |
| R-1006 | The project must perform a security assessment of likely, high-impact problems. | producers | security | S-07 version page, Level 2, SA-03.01 | C-27 |
| R-1007 | The project must publish a coordinated vulnerability disclosure policy with response timeframes. | producers | security | S-07 version page, Level 2, VM-01.01 | C-35 |
| R-1008 | The project must offer private vulnerability reporting directly to security contacts. | producers | security | S-07 version page, Level 2, VM-03.01 | C-35 |
| R-1009 | The project must publicly publish data on discovered vulnerabilities. | producers | security | S-07 version page, Level 2, VM-04.01 | C-35 |
| R-1010 | Jobs must get only the minimum privileges they need. | producers | pipeline | S-07 version page, Level 3, AC-04.02 | C-07 |
| R-1011 | Manual inputs from trusted collaborators must be validated before pipeline use. | producers | security | S-07 version page, Level 3, BR-01.04 | C-23 |
| R-1012 | Every release asset must be tied to the release ID or to its own unique ID. | producers | pipeline | S-07 version page, Level 3, BR-02.02 | C-10 |
| R-1013 | The project must maintain a secrets policy covering storage, access and rotation. | producers | security | S-07 version page, Level 3, BR-07.02 | C-22 |
| R-1014 | The project must document how to verify release-asset integrity and authenticity. | consumers | pipeline | S-07 version page, Level 3, DO-03.01 | C-11 |
| R-1015 | The project must document how to verify the expected identity of the release author or process. | consumers | pipeline | S-07 version page, Level 3, DO-03.02 | C-11 |
| R-1016 | The project must state the support scope and duration per release. | consumers | security | S-07 version page, Level 3, DO-04.01 | C-37 |
| R-1017 | The project must state when releases stop receiving security updates. | consumers | security | S-07 version page, Level 3, DO-05.01 | C-37 |
| R-1018 | Policy must require collaborator review before escalated access to sensitive resources. | producers | security | S-07 version page, Level 3, GV-04.01 | C-21 |
| R-1019 | Compiled assets must ship with an SBOM. | producers | pipeline | S-07 version page, Level 3, QA-02.02 | C-13 |
| R-1020 | Subprojects must meet security requirements at least as strict as the primary codebase. | producers | security | S-07 version page, Level 3, QA-04.02 | C-18 |
| R-1021 | The project must document when and how tests run. | producers | quality | S-07 version page, Level 3, QA-06.02 | C-40 |
| R-1022 | Policy must require major changes to add or update tests. | producers | quality | S-07 version page, Level 3, QA-06.03 | C-39 |
| R-1023 | At least one non-author human approval must be required before merging to the primary branch. | producers | pipeline | S-07 version page, Level 3, QA-07.01 | C-03 |
| R-1024 | The project must perform threat modeling and attack-surface analysis. | producers | security | S-07 version page, Level 3, SA-03.02 | C-27 |
| R-1025 | The project must publish a VEX document for vulnerabilities that do not affect the project. | consumers | security | S-07 version page, Level 3, VM-04.02 | C-36 |
| R-1026 | Policy must set a remediation threshold for SCA findings, covering vulnerabilities and licenses. | producers | security | S-07 version page, Level 3, VM-05.01 | C-25 |
| R-1027 | Policy must address SCA violations before any release. | producers | security | S-07 version page, Level 3, VM-05.02 | C-25 |
| R-1028 | Every change must be scanned automatically for malicious or known-vulnerable dependencies, and violations must be blocked unless suppressed. | producers | security | S-07 version page, Level 3, VM-05.03 | C-25 |
| R-1029 | Policy must set a remediation threshold for SAST findings. | producers | security | S-07 version page, Level 3, VM-06.01 | C-24 |
| R-1030 | Every change must be scanned automatically for security weaknesses, and violations must be blocked unless suppressed. | producers | security | S-07 version page, Level 3, VM-06.02 | C-24 |
| R-1031 | Teams should budget for release engineering resources at the beginning of the product development cycle. | management | operations | S-09 Start Release Engineering at the Beginning | C-53 |
| R-1032 | Be sure that you consider the role of release engineering as applied to the entire lifecycle. | operations engineers | operations | S-09 Start Release Engineering at the Beginning | C-62 |
| R-1033 | Developers shouldn't build and throw the results over the fence. | software engineers | operations | S-09 Start Release Engineering at the Beginning | C-62 |
| R-1034 | Developers must collaborate with release engineers rather than hand off builds. | software engineers | operations | S-09 Enforcement of Policies; Start Release Engineering at the Beginning (wording from summary) | C-62 |
| R-1035 | All companies should take the effort to define their release processes. | management | operations | S-09 Conclusions (It's Not Just for Googlers) | C-62 |
| R-1036 | SLOs should drive the work prioritization of product developers and SREs. | operations engineers | operations | S-09 Choosing Targets | C-58 |
| R-1037 | A good SLO should act as a forcing function for the development team. | software engineers | operations | S-09 Choosing Targets | C-58 |
| R-1038 | Monitoring should be designed with simplicity in mind. | operations engineers | operations | S-09 Setting Reasonable Expectations / As Simple as Possible, No Simpler | C-57 |
| R-1039 | Every page should be actionable. | operations engineers | operations | S-09 Tying These Principles Together | C-57 |
| R-1040 | An alert should never be triggered simply because something seems a bit weird. | operations engineers | operations | S-09 Setting Reasonable Expectations (summary; heading not confirmed) | C-57 |
| R-1041 | Pages should be urgent, actionable, require intelligence, and concern novel problems. | operations engineers | operations | S-09 Tying These Principles Together | C-57 |
| R-1042 | Rare alerts that become frequent should lead to root-cause fixes or full automation. | management | operations | S-09 Monitoring for the Long Term | C-59 |
| R-1043 | Monitoring should use dashboards rather than email alerts for non-urgent signals. | operations engineers | operations | S-09 Conclusion | C-57 |
| R-1044 | Page frequency should be reviewed in quarterly management reports. | management | operations | S-09 The Long Run | C-57 |
| R-1045 | Test deployments and drained traffic should be filtered out of alerts. | operations engineers | operations | S-09 Definitions (summary; heading not confirmed) | C-57 |
| R-1046 | Development, operations and release teams should share all five metrics. | operations engineers | operations | S-10 section 2 | C-63 |
| R-1047 | Build security into the software development lifecycle without compromising delivery speed. | security roles | security | S-10 Pervasive security entry, catalog list | C-18 |
| R-1048 | Replace heavyweight approval with peer review, and keep releases reliable and compliant without losing speed. | management | operations | S-10 Streamlining change approval entry, catalog list | C-65 |
| R-1049 | Engineers must be triaged when a bug is found late, because late bugs cost more to fix. | software engineers | quality | S-12 Chapter, Section on cost | C-49 |
| R-1050 | Teams should aim to continuously integrate dependency changes that come from beyond the codebase. | software engineers | pipeline | S-12 Chapter, Section on distributed systems | C-05 |
| R-1051 | Dependencies should be considered as part of the system under test. | quality assurance | quality | S-12 Chapter, Section on distributed systems | C-40 |
| R-1052 | Static configuration should be promoted as part of the release candidate. | operations engineers | operations | S-12 Chapter, Section on configuration | C-54 |
| R-1053 | Release artifacts ideally should not be recompiled or rebuilt. | software engineers | pipeline | S-12 Chapter, Section on continuous delivery | C-12 |
| R-1054 | Feedback from CI tests should be actionable, not only accessible. | software engineers | pipeline | S-12 Chapter, Section on feedback | C-05 |
| R-1055 | Tests should fail only when the important underlying invariant is violated. | quality assurance | quality | S-12 Chapter, Section on test design | C-41 |
| R-1056 | Hermetic test success should not depend on the user who runs the test. | quality assurance | quality | S-12 Chapter, Section on hermetic tests | C-41 |
| R-1057 | Production problems should not affect hermetic tests, and hermetic tests should not affect production. | quality assurance | quality | S-12 Chapter, Section on hermetic tests | C-41 |
| R-1058 | The same suite of tests should run against production. | quality assurance | quality | S-12 Chapter, Section on production | C-42 |
| R-1059 | A change that breaks the build must be fixed quickly. | software engineers | pipeline | S-12 Chapter, Section on Build Cop | C-05 |
| R-1060 | Non-release-blocking failures should be fixed, and should also be prioritised. | software engineers | pipeline | S-12 Chapter, Section on release | C-05 |
| R-1061 | Failures should be investigated before a change is committed. | software engineers | quality | S-12 Chapter, Section on presubmit | C-39 |
| R-1062 | Accepting changes that disable a failed test should be more liberal. | quality assurance | quality | S-12 Chapter, Section on disabled tests | C-39 |
| R-1063 | Blocking all commits on a red CI build is probably misguided. | software engineers | pipeline | S-12 Chapter, Section on release | C-05 |
| R-1064 | CI should optimise for quicker, more reliable tests on presubmit. | software engineers | pipeline | S-12 Chapter, Section on presubmit | C-05 |
| R-1065 | A CI system should be adjusted to meet the changing demands of its application. | software engineers | pipeline | S-12 Chapter, Section on evolution | C-05 |
| R-1066 | Aiming for 100 percent uptime is the wrong target. | operations engineers | operations | S-12 Chapter, footnote on uptime | C-58 |
| R-1067 | Engineers write, run and quickly fix tests for their own code. | software engineers | quality | S-12 Why Do We Write Tests?; Write, Run, React | C-39 |
| R-1068 | In an earlier policy of one team, all new code changes were required to include tests; every change is now expected to include tests. | software engineers | quality | S-12 The Story of Google Web Server | C-39 |
| R-1069 | Code reviewers may block changes that lack tests. | quality assurance | quality | S-12 Simpler Reviews; Testing Culture Today | C-48 |
| R-1070 | Infrastructure teams must fix and add tests when their cross-codebase changes break a product. | software engineers | quality | S-12 The Beyoncé Rule | C-39 |
| R-1071 | Team leads and managers reward test quality, set performance goals and refactor slow or brittle tests. | management | quality | S-12 Pitfalls of a Large Test Suite | C-40 |
| R-1072 | Readers should write the test they would like to read. | software engineers | quality | S-12 Properties Common to All Test Sizes | C-40 |
| R-1073 | Readers should treat their tests like production code. | software engineers | quality | S-12 Pitfalls of a Large Test Suite | C-50 |
| R-1074 | Google requires review for nearly every change. | quality assurance | quality | S-12 summary, "Overview" (the page location is not available) | C-48 |
| R-1075 | Reviewers should give initial feedback within 24 working hours. | quality assurance | quality | S-12 summary, "Best practices" | C-48 |
| R-1076 | Authors and reviewers should be polite and professional. | quality assurance | quality | S-12 summary, "Best practices" | C-74 |
| R-1077 | Changes should be kept small, around 200 lines. | software engineers | quality | S-12 summary, "Best practices" | C-51 |
| R-1078 | Change descriptions should have a summary first line and a rationale in the body. | software engineers | quality | S-12 summary, "Best practices" | C-48 |
| R-1079 | Reviewers should avoid expanding the scope of a change. | quality assurance | quality | S-12 summary, "Types of reviews" | C-48 |
| R-1080 | New code should be justified, and existing utilities should be checked first. | quality assurance | quality | S-12 summary, "Overview" | C-48 |
| R-1081 | Developers should commit to the mainline every day. | software engineers | quality | S-13 "Everyone Pushes Commits To the Mainline Every Day" | C-51 |
| R-1082 | Developers should update, resolve conflicts, and build locally before pushing. | software engineers | quality | S-13 "Everyone Pushes Commits To the Mainline Every Day" | C-51 |
| R-1083 | Every commit should be verified in a reference environment. | software engineers | pipeline | S-13 "Every Push to Mainline Should Trigger a Build" | C-05 |
| R-1084 | The CI service should monitor only the single mainline branch. | software engineers | pipeline | S-13 "Every Push to Mainline Should Trigger a Build" | C-05 |
| R-1085 | A broken mainline build should be fixed right away. | software engineers | pipeline | S-13 "Fix Broken Builds Immediately" | C-05 |
| R-1086 | A team should rarely see a red mainline. | software engineers | pipeline | S-13 "Fix Broken Builds Immediately" | C-05 |
| R-1087 | Build time should stay within about ten minutes. | software engineers | pipeline | S-13 "Keep the Build Fast" | C-05 |
| R-1088 | Later-stage failures should lead to new commit-build tests. | software engineers | quality | S-13 "Keep the Build Fast" | C-39 |
| R-1089 | Dependencies should be checked for updates, usually daily. | software engineers | pipeline | S-13 "Keep the Build Fast" | C-14 |
| R-1090 | Build steps should be automated, not manual. | software engineers | pipeline | S-13 "Automate the Build" | C-04 |
| R-1091 | Build instructions must live in the repository as text. | software engineers | pipeline | S-13 "Automate the Build" | C-01 |
| R-1092 | Anyone should be able to build from a clean machine with a single command. | software engineers | pipeline | S-13 "Automate the Build" | C-04 |
| R-1093 | The build should support alternative targets. | software engineers | quality | S-13 "Automate the Build" | C-70 |
| R-1094 | Store everything needed to build, but not the build products. | software engineers | pipeline | S-13 "Put everything in a version controlled mainline" | C-01 |
| R-1095 | Each programming task should include the tests that prove it. | software engineers | quality | S-13 "Make the Build Self-Testing" | C-39 |
| R-1096 | Teams should evaluate linters and security scanners for the verification process. | software engineers | quality | S-13 "Make the Build Self-Testing" | C-43 |
| R-1097 | The test environment should mimic production as closely as possible. | quality assurance | quality | S-13 "Test in a Clone of the Production Environment" | C-42 |
| R-1098 | The pipeline should test all target environments in parallel. | quality assurance | quality | S-13 "Test in a Clone of the Production Environment" | C-42 |
| R-1099 | Teams should always be able to roll back when introducing a feature. | operations engineers | operations | S-13 "Hide Work-in-Progress" | C-55 |
| R-1100 | Version information should be visible in the running product. | operations engineers | operations | S-13 "Automate Deployment" | C-54 |
| R-1101 | Teams should consider notifying on success as well as failure. | software engineers | pipeline | S-13 "Everyone can see what's happening" | C-05 |
| R-1102 | Teams should keep an eye on build times. | software engineers | pipeline | S-13 "Introducing Continuous Integration" | C-05 |
| R-1103 | Teams should get help from someone experienced with CI. | software engineers | quality | S-13 "Introducing Continuous Integration" | C-73 |
| R-1104 | Teams should not confuse the tool with the practice. | software engineers | quality | S-13 "Can we run a CI Service on our feature branches?" | C-73 |
| R-1105 | Teams should reassess review practices built for open source when applied to full-time teams. | software engineers | quality | S-13 "How do we do pull requests and code reviews?" | C-48 |

## Proposed boundaries

| Boundary | Requirements that it would take | Stakeholders that it would leave with no requirement | Reason |
|---|---|---|---|
| requirements engineering | R-0158, R-0161 to R-0163, R-0215, R-0262, R-0292, R-0376, R-0411, R-0492, R-0504, R-0510, R-0604 to R-0606, R-0608 to R-0613, R-0615 to R-0617, R-0621, R-0626 to R-0628 | none | The body of knowledge has a knowledge area of its own for software requirements (S-01 pages 43 to 66). These requirements state no practice of the pipeline. Until the owner decides, they go to item C-68. |
| architecture and design | R-0412 to R-0415, R-0417, R-0418, R-0493, R-0505 to R-0507, R-0509, R-0522, R-0630 to R-0644, R-1005 | none | The body of knowledge has knowledge areas of their own for software architecture and software design (S-01 pages 67 to 98). Until the owner decides, the requirements go to item C-69. |
| software construction | R-0174, R-0299, R-0440, R-0443 to R-0445, R-0447, R-0448, R-0450 to R-0454, R-0456, R-0457, R-0512 to R-0516, R-0650, R-0653 to R-0657, R-0659, R-1093 | none | The body of knowledge has a knowledge area of its own for software construction (S-01 pages 99 to 116). Until the owner decides, the requirements go to item C-70. |
| software maintenance | R-0105 to R-0127, R-0131, R-0384 | none | The body of knowledge has a knowledge area of its own for software maintenance (S-01 pages 167 to 184). Until the owner decides, the requirements go to item C-71. |
| project management | R-0152 to R-0157, R-0159, R-0160, R-0166, R-0167, R-0170 to R-0173, R-0175 to R-0180, R-0182 to R-0190, R-0195, R-0198 to R-0204, R-0206, R-0207, R-0209, R-0210, R-0212 to R-0214, R-0216 to R-0220, R-0223, R-0225 to R-0228, R-0231 to R-0244, R-0250 to R-0253, R-0368, R-0386, R-0390, R-0401, R-0406, R-0419, R-0600, R-0622 to R-0625 | none | The body of knowledge has a knowledge area of its own for software engineering management (S-01 pages 202 to 220). Until the owner decides, the requirements go to item C-72. |
| software process | R-0129, R-0165, R-0194, R-0221, R-0222, R-0224, R-0229, R-0230, R-0245 to R-0249, R-0254 to R-0257, R-0281, R-0599, R-0601, R-0770, R-0773, R-0775, R-0776, R-0840, R-0841, R-1103, R-1104 | none | The body of knowledge has knowledge areas of their own for the software engineering process and for models and methods (S-01 pages 221 to 245). Until the owner decides, the requirements go to item C-73. |
| professional practice | R-0269, R-0271, R-0273, R-0274, R-0350 to R-0360, R-0362, R-0363, R-0365, R-0371 to R-0375, R-0377 to R-0383, R-0385, R-0387, R-0408, R-0409, R-0602, R-1076 | none | The body of knowledge has a knowledge area of its own for professional practice (S-01 pages 275 to 287). Until the owner decides, the requirements go to item C-74. |
| software economics | R-0272, R-0295, R-0369, R-0370, R-0388, R-0389, R-0391 to R-0400, R-0402 to R-0405, R-0407, R-0523 | none | The body of knowledge has a knowledge area of its own for software engineering economics (S-01 pages 288 to 311). Until the owner decides, the requirements go to item C-75. |
| engineering foundations | R-0259 to R-0261, R-0263, R-0349, R-0410, R-0416, R-0420 to R-0439, R-0441, R-0442, R-0446, R-0458 to R-0473, R-0475 to R-0485, R-0487 to R-0491, R-0496, R-0498 to R-0500, R-0511, R-0517 to R-0521, R-0524 to R-0562 | none | The body of knowledge has three knowledge areas for the foundations of computing, mathematics and engineering (S-01 pages 312 to 386). They state what an engineer knows, not what a pipeline does. Until the owner decides, the requirements go to item C-76. |
| making of the body of knowledge | R-0311 to R-0315, R-0563 to R-0598, R-0603 | none | The front part and the appendices of the body of knowledge state rules for the authors and the editors of the guide (S-01 pages 26 to 42 and 387 to 411). They are not requirements for a project. The cell Stakeholder of these rows is a judgement, because the list of section 1 has no such group. Until the owner decides, the requirements go to item C-77. |

## Reading

The program `index.py unread --write` writes this table. Do not change it by hand.

| Source | Document | Pages | Given to readers | Not read |
|---|---|---|---|---|
| S-01 | swebok | 411 | 1-25, 26-42, 43-66, 67-82, 83-98, 99-116, 117-141, 142-166, 167-184, 185-201, 202-220, 221-245, 246-263, 264-287, 288-311, 312-335, 336-344, 345-366, 367-386, 387-411 | none |
| S-03 | S-03 | 36 | 1-25, 26-36 | none |
| S-04 | S-04 | 41 | 1-23, 24-41 | none |
