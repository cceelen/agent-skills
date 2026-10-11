# Vetting record: DevSecOps

## Searches

Web searches of the session:

- `DevSecOps standard framework practices guidance`: all (the aspect by its name)
- `SLSA specification levels build track source track draft current version`: supply chain (the target of the owner)
- `secure software development practices standard producer verify integrity of releases vulnerability response`: security; supply chain
- `software delivery performance metrics deployment frequency change lead time failed deployment recovery time research`: operations
- `continuous testing quality gates pipeline static analysis test automation standard shift left testing`: quality
- `service level objectives monitoring incident response release engineering practices operations reliability`: operations

Searches in the index of the converted documents (the result is pages, not text):

- `DevSecOps`: all
- `supply chain`: supply chain
- `software bill of materials`: supply chain
- `service level`: operations
- `operations engineer`: operations (stakeholder)
- `security testing`: security

## Sources

Rubric for sources: version 1

| Source | Kind | Gates | Signals | Answers | Score | Date | Confirmed by |
|---|---|---|---|---|---|---|---|
| S-11 | page | pass | reachable yes; date 2026-10-10; age 1 d; author yes; links out 15 | record: yes (https://martinfowler.com/articles/continuousIntegration.html); fast-lane references: 2 (S-08, S-10) | 10 of 10 | 2026-10-11 | |

## Items

Rubric for items: version 1

| Item | Severity | Probability | Breadth | Adopt | Keep | Own risk | Dimension | Return | Cost | Score | Admitted | Level |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C-01 | 3 (judgement) | 2 (judgement) | 3 (judgement) | 1 (judgement) | 1 (judgement) | 0 (judgement) |  | 18 | 2 | 90 | yes | 1 |
| C-02 | 3 (S-07 Branch-Protection) | 2 (judgement) | 3 (judgement) | 1 (judgement) | 1 (judgement) | 0 (judgement) |  | 18 | 2 | 90 | yes | 1 |
| C-03 | 3 (S-07 Code-Review) | 2 (judgement) | 2 (S-07 Code-Review) | 2 (judgement) | 2 (judgement) | 1 (S-11 Common Questions) | team size | 12 | 4 | 25 | yes | 2, team size |
| C-04 | 2 (S-07 Pinned-Dependencies) | 2 (judgement) | 3 (judgement) | 1 (judgement) | 1 (judgement) | 0 (judgement) |  | 12 | 2 | 60 | yes | 1 |
| C-05 | 3 (S-07 Vulnerabilities) | 3 (judgement) | 3 (judgement) | 1 (judgement) | 2 (judgement) | 1 (S-05 page 21) |  | 27 | 3 | 85 | yes | 1 |
| C-06 | 3 (judgement) | 2 (judgement) | 3 (judgement) | 1 (judgement) | 2 (judgement) | 0 (judgement) |  | 18 | 3 | 60 | yes | 1 |
| C-07 | 2 (judgement) | 2 (judgement) | 3 (judgement) | 2 (judgement) | 1 (judgement) | 0 (judgement) |  | 12 | 3 | 40 | yes | 1 |
| C-08 | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 1 (judgement) | 1 (S-02 about) | supply chain integrity | 8 | 3 | 21 | yes | 2, supply chain integrity |
| C-09 | 3 (S-07 Signed-Releases) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 1 (judgement) | 1 (S-02 about) | supply chain integrity | 12 | 3 | 35 | yes | 2, supply chain integrity |
| C-10 | 3 (judgement) | 1 (judgement) | 2 (judgement) | 2 (judgement) | 1 (judgement) | 1 (S-02 verifying-artifacts) | supply chain integrity | 6 | 3 | 15 | no | not admitted |
| C-11 | 3 (S-07 Dangerous-Workflow) | 2 (judgement) | 3 (judgement) | 1 (judgement) | 1 (judgement) | 0 (judgement) |  | 18 | 2 | 90 | yes | 1 |
| C-12 | 2 (S-07 SBOM) | 2 (judgement) | 2 (judgement) | 1 (judgement) | 1 (judgement) | 1 (S-05 page 13) | supply chain integrity | 8 | 2 | 35 | yes | 2, supply chain integrity |
| C-13 | 3 (judgement) | 2 (judgement) | 3 (judgement) | 1 (judgement) | 1 (judgement) | 0 (judgement) |  | 18 | 2 | 90 | yes | 1 |
| C-14 | 3 (judgement) | 1 (judgement) | 2 (judgement) | 3 (judgement) | 1 (judgement) | 1 (S-02 verifying-artifacts) | supply chain integrity | 6 | 4 | 10 | no | not admitted |
| C-15 | 3 (judgement) | 3 (judgement) | 3 (judgement) | 1 (judgement) | 1 (judgement) | 1 (judgement) |  | 27 | 2 | 130 | yes | 1 |
| C-16 | 2 (S-07 SAST) | 3 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 1 (S-05 page 21) |  | 18 | 4 | 40 | yes | 1 |
| C-17 | 2 (S-07 Security-Policy) | 2 (judgement) | 3 (judgement) | 1 (judgement) | 1 (judgement) | 0 (judgement) |  | 12 | 2 | 60 | yes | 1 |
| C-18 | 3 (S-07 Vulnerabilities) | 2 (judgement) | 3 (judgement) | 1 (judgement) | 2 (judgement) | 0 (judgement) |  | 18 | 3 | 60 | yes | 1 |
| C-19 | 3 (judgement) | 2 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 1 (judgement) |  | 18 | 4 | 40 | yes | 1 |
| C-20 | 3 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 1 (judgement) | exposure | 12 | 4 | 25 | yes | 2, exposure |
| C-21 | 2 (judgement) | 2 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | exposure | 12 | 4 | 30 | yes | 2, exposure |
| C-22 | 2 (judgement) | 3 (judgement) | 3 (judgement) | 2 (judgement) | 1 (judgement) | 0 (judgement) |  | 18 | 3 | 60 | yes | 1 |
| C-23 | 2 (judgement) | 3 (judgement) | 3 (judgement) | 1 (judgement) | 2 (judgement) | 0 (judgement) |  | 18 | 3 | 60 | yes | 1 |
| C-24 | 2 (judgement) | 3 (judgement) | 3 (judgement) | 1 (judgement) | 2 (judgement) | 0 (judgement) |  | 18 | 3 | 60 | yes | 1 |
| C-25 | 1 (judgement) | 3 (judgement) | 3 (judgement) | 1 (judgement) | 2 (judgement) | 0 (judgement) | team size | 9 | 3 | 30 | yes | 2, team size |
| C-26 | 2 (judgement) | 2 (judgement) | 3 (judgement) | 1 (judgement) | 2 (judgement) | 0 (judgement) |  | 12 | 3 | 40 | yes | 1 |
| C-27 | 2 (judgement) | 2 (judgement) | 3 (judgement) | 1 (judgement) | 2 (judgement) | 1 (judgement) | team size | 12 | 3 | 35 | yes | 2, team size |
| C-28 | 1 (judgement) | 3 (judgement) | 3 (judgement) | 1 (judgement) | 1 (judgement) | 0 (judgement) |  | 9 | 2 | 45 | yes | 1 |
| C-29 | 2 (judgement) | 2 (judgement) | 3 (judgement) | 1 (judgement) | 1 (judgement) | 0 (judgement) |  | 12 | 2 | 60 | yes | 1 |
| C-30 | 3 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 1 (judgement) | 0 (judgement) | availability | 12 | 3 | 40 | yes | 2, availability |
| C-31 | 3 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 1 (judgement) | availability | 12 | 4 | 25 | yes | 2, availability |
| C-32 | 3 (judgement) | 2 (judgement) | 2 (judgement) | 3 (judgement) | 2 (judgement) | 1 (judgement) | availability | 12 | 5 | 19 | no | not admitted |
| C-33 | 2 (judgement) | 3 (judgement) | 2 (judgement) | 1 (judgement) | 1 (judgement) | 0 (judgement) | availability | 12 | 2 | 60 | yes | 2, availability |
| C-34 | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | availability | 8 | 4 | 20 | yes | 2, availability |
| C-35 | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 1 (judgement) | availability | 8 | 4 | 15 | no | not admitted |
| C-36 | 3 (judgement) | 2 (judgement) | 3 (judgement) | 1 (judgement) | 2 (judgement) | 0 (judgement) |  | 18 | 3 | 60 | yes | 1 |
| C-37 | 2 (judgement) | 2 (judgement) | 3 (judgement) | 1 (judgement) | 2 (judgement) | 0 (judgement) |  | 12 | 3 | 40 | yes | 1 |
| C-38 | 2 (judgement) | 3 (judgement) | 2 (judgement) | 2 (judgement) | 1 (judgement) | 0 (judgement) | availability | 12 | 3 | 40 | yes | 2, availability |
| C-39 | 3 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 2 (judgement) | 0 (judgement) | availability | 12 | 4 | 30 | yes | 2, availability |

## Requirements

| Id | Requirement | Stakeholder | View | Source | Goes to |
|---|---|---|---|---|---|
| R-01 | Teams should practise DevOps and adopt continuous delivery and deployment. | developers | operations | S-01 page 101 | 3.3: How to release to users |
| R-02 | Developers or tools should manage each dependency of the supply chain network. | developers | supply chain | S-01 page 103 | C-05 |
| R-03 | Unnecessary dependencies should be avoided. | developers | supply chain | S-01 page 103 | C-06 |
| R-04 | Licence conflicts between dependencies and the product should be avoided. | developers | supply chain | S-01 page 103 | C-06 |
| R-05 | The propagation of defects and vulnerabilities of dependencies into the product should be avoided. | developers | supply chain | S-01 page 103 | C-05 |
| R-06 | Rules and monitoring should prevent that developers add untrusted external dependencies. | security staff | supply chain | S-01 pages 103 and 104 | C-06 |
| R-07 | Programmers should know good practices and common vulnerabilities. | developers | security | S-01 page 107 | 3.3: How to organize the security work |
| R-08 | For usage-based test techniques, the test environment needs to represent the actual operational environment. | quality and test staff | quality | S-01 page 131 | C-38 |
| R-09 | Test processes should permit automation and rely on traceability and replication. | quality and test staff | quality | S-01 page 134 | C-22 |
| R-10 | Test documentation should be under configuration management. | quality and test staff | quality | S-01 page 135 | C-01 |
| R-11 | In shift-left development, the different aspects of testing should be considered. | quality and test staff | quality | S-01 page 139 | 3.3: Which tests the project keeps |
| R-12 | Software must be fully tested before release, and tests must be automated as much as possible. | operations engineers | quality | S-01 page 155 | C-22 |
| R-13 | Operations planning should start with the decision to develop the product. | operations engineers | operations | S-01 page 156 | C-37 |
| R-14 | The plan should tell how users request changes and report problems. | consumers | operations | S-01 page 156 | 3.3: How to prepare the operation |
| R-15 | Engineers must keep the environments coherent and synchronized with production. | operations engineers | operations | S-01 page 157 | C-38 |
| R-16 | A capacity plan should be made at least each year. | operations engineers | operations | S-01 page 158 | 3.3: How to prepare the operation |
| R-17 | Disaster recovery and failover should be rehearsed. | operations engineers | operations | S-01 page 159 | C-39 |
| R-18 | Applications must include logic for the handling of failures, planned during development. | developers | operations | S-01 page 159 | C-37 |
| R-19 | Senior management should define the information security policy. | management | security | S-01 page 159 | 3.3: How to organize the security work |
| R-20 | Staff with important security roles should get training, and all staff should know the policy. | management | security | S-01 page 159 | 3.3: How to organize the security work |
| R-21 | Security incidents should be reported, and a response should start. | operations engineers | security | S-01 page 159 | C-36 |
| R-22 | Applications or services must be built for small, independent deployments. | developers | operations | S-01 page 161 | 3.3: How to release to users |
| R-23 | Engineers should get evidence about quality and health. | operations engineers | operations | S-01 page 161 | C-33 |
| R-24 | Tests must be automated as much as possible, for fast feedback to developers. | developers | quality | S-01 page 164 | C-25 |
| R-25 | Maintainers should plan and do tests that verify changes. | quality and test staff | quality | S-01 page 171 | C-23 |
| R-26 | Maintenance should be planned during development. | operations engineers | operations | S-01 page 178 | C-37 |
| R-27 | Each change to the software and to its infrastructure must be controlled. | release and configuration managers | supply chain | S-01 page 179 | C-30 |
| R-28 | Configuration management procedures should verify, validate and audit each release step. | auditors and regulators | supply chain | S-01 page 179 | C-08 |
| R-29 | Branching and merging strategies should be planned and communicated. | release and configuration managers | supply chain | S-01 pages 187 and 188 | 3.3: How to branch |
| R-30 | The repository of binary objects should hold cryptographic hashes for the audit. | auditors and regulators | supply chain | S-01 page 192 | C-08 |
| R-31 | Requirements and test cases should be linked with the code baselines. | release and configuration managers | quality | S-01 page 192 | C-23 |
| R-32 | Status information of configurations must be collected, and secured where relevant. | release and configuration managers | supply chain | S-01 page 195 | C-12 |
| R-33 | To build an exact copy of an earlier item again, the tools and the instructions of the build must be under configuration control. | release and configuration managers | supply chain | S-01 page 197 | C-01 |
| R-34 | Configuration management must usually be able to reproduce earlier releases. | release and configuration managers | supply chain | S-01 page 197 | C-07 |
| R-35 | Risk management should be done at intervals in the life cycle, with attention to safety and security risks. | management | security | S-01 page 210 | 3.3: How to organize the security work |
| R-36 | Thresholds for acceptable quality measurements should be set for each quality requirement. | quality and test staff | quality | S-01 page 211 | C-29 |
| R-37 | Organizations should consider controls on access without filter to external library repositories. | security staff | supply chain | S-01 page 212 | C-06 |
| R-38 | Each acquired component should be verified, integrated and validated. | suppliers | supply chain | S-01 page 212 | C-06 |
| R-39 | Outcomes should be reported when thresholds are exceeded. | management | quality | S-01 page 213 | C-29 |
| R-40 | Release managers need to monitor the development process and the schedule of each release. | release and configuration managers | operations | S-01 page 243 | 3.3: How to release to users |
| R-41 | Quality should be planned early and assessed at milestones. | quality and test staff | quality | S-01 page 248 | C-29 |
| R-42 | Quality assurance activities should start early in the life cycle. | quality and test staff | quality | S-01 page 255 | C-22 |
| R-43 | Engineers should define quality requirements and targets that can be measured at acceptance. | quality and test staff | quality | S-01 page 256 | C-29 |
| R-44 | Verification and validation should start early in development or maintenance. | quality and test staff | quality | S-01 page 257 | C-23 |
| R-45 | Engineers should plan the test activities: levels, techniques, measures and tools. | quality and test staff | quality | S-01 page 258 | 3.3: Which tests the project keeps |
| R-46 | Reviews should be planned, done and documented. | quality and test staff | quality | S-01 page 259 | 3.3: Which review a change gets before the merge |
| R-47 | Technical reviews and audits should be planned, approved and conducted. | auditors and regulators | quality | S-01 page 259 | 3.3: Which review a change gets before the merge |
| R-48 | Engineers should define the security properties of the software and keep them through the life cycle. | security staff | security | S-01 page 264 | C-19 |
| R-49 | Security must be built into the engineering work. | security staff | security | S-01 page 266 | C-16 |
| R-50 | Organizations should continually assess risks, with a team that monitors them. | management | security | S-01 page 266 | 3.3: How to organize the security work |
| R-51 | Agile teams need to adopt security practices and take more responsibility for the security of their systems. | developers | security | S-01 page 266 | 3.3: How to organize the security work |
| R-52 | Security tests should be done within legal limits and with authorization, by security experts of the domain. | security staff | security | S-01 page 268 | C-20 |
| R-53 | Engineers should give external stakeholders documentation on safe use and on the protection of sensitive information. | consumers | security | S-01 page 281 | 3.3: Which data protection measures apply |
| R-54 | Programs must be tested for valid, invalid and boundary inputs. | quality and test staff | quality | S-01 page 324 | C-23 |
| R-55 | Databases must be backed up at intervals. | operations engineers | operations | S-01 page 331 | C-39 |
| R-56 | Systems must monitor the network, so that faults, vulnerabilities and attacks are found and corrected. | operations engineers | security | S-01 page 333 | C-33 |
| R-57 | The producer must follow a consistent build process and build on a platform of the target level. | release and configuration managers | supply chain | S-02 build-track-basics, Build L1 | C-07 |
| R-58 | The build platform must generate provenance with the builder, the build process and the top-level inputs. | release and configuration managers | supply chain | S-02 build-track-basics, Build L1 | C-08 |
| R-59 | The producer must distribute the provenance to consumers. | consumers | supply chain | S-02 build-track-basics, Build L1 | C-08 |
| R-60 | The build must run on a hosted platform that generates and signs the provenance, or gives a different means to verify its authenticity. | release and configuration managers | supply chain | S-02 build-track-basics, Build L2 | C-09 |
| R-61 | The consumer must validate the authenticity of the provenance. | consumers | supply chain | S-02 build-track-basics, Build L2 | C-09 |
| R-62 | The build platform must prevent that runs influence one another, and must keep the signing secret away from user-defined build steps. | release and configuration managers | supply chain | S-02 build-track-basics, Build L3 | C-10 |
| R-63 | Verification should examine the builder identity, the signature and the build parameters against expected values. | consumers | supply chain | S-02 verifying-artifacts, How to verify | C-14 |
| R-64 | A package ecosystem should publish its expectations and give tools to consumers. | consumers | supply chain | S-02 verifying-artifacts, Architecture options | 5 |
| R-65 | The organization chooses a source control system that can reach the target level. | release and configuration managers | supply chain | S-02 source-requirements, Requirements by actor | 3.3: Which SLSA tracks and levels to aim for |
| R-66 | The history of a branch is continuous and immutable, and the system records who changed each reference. | release and configuration managers | supply chain | S-02 source-requirements, Level 2 | C-02 |
| R-67 | The source control system enforces the controls of the organization on protected references, and supported tags cannot be moved or deleted. | release and configuration managers | supply chain | S-02 source-requirements, Level 3 | C-02 |
| R-68 | The organization documents each control and gives evidence of continuous enforcement. | auditors and regulators | supply chain | S-02 source-requirements, Level 3 | C-29 |
| R-69 | Two trusted persons agree to a change of a protected branch, and the final revision is reviewed. | developers | supply chain | S-02 source-requirements, Level 4 | C-03 |
| R-70 | The organization documents a safe process to remove content. | release and configuration managers | supply chain | S-02 source-requirements, Requirements by actor | 3.3: Which SLSA tracks and levels to aim for |
| R-71 | Consumers verify the summary attestation of a source revision, which the source control system or a provider of attestations issues. | consumers | supply chain | S-02 verifying-source, Consumer verification steps | C-14 |
| R-72 | The build must generate provenance that identifies the output by digest and tells how it was produced. | release and configuration managers | supply chain | S-03 build-requirements, Provenance Exists (L1) | duplicate: R-58 |
| R-73 | The external parameters of a build must be fully enumerated, and the trusted control plane generates or verifies each field of the provenance. | release and configuration managers | supply chain | S-03 build-requirements, Provenance is Unforgeable (L3) | C-10 |
| R-74 | The platform must guarantee that a build cannot get platform secrets, cannot influence a different build and cannot poison a cache. | release and configuration managers | supply chain | S-03 build-requirements, Isolated (L3) | duplicate: R-62 |
| R-75 | Consumers should assess a build platform before they trust it for Build L3. | consumers | supply chain | S-03 assessing-build-platforms, Introduction | 3.3: Which SLSA tracks and levels to aim for |
| R-76 | The producer of a build image must generate provenance for it, and the build platform must verify that provenance before it starts a build environment. | release and configuration managers | supply chain | S-03 build-env-track-basics, BuildEnv L1 | 3.3: Which SLSA tracks and levels to aim for |
| R-77 | Before a build, the build platform must verify a signed quote of the build environment, at the highest level from trusted hardware. | release and configuration managers | supply chain | S-03 build-env-track-basics, BuildEnv L2 and BuildEnv L3 | 3.3: Which SLSA tracks and levels to aim for |
| R-78 | The ingestor must distribute provenance for each dependency that contributes to a release. | suppliers | supply chain | S-03 dependency-track, Dep L1 | 3.3: Which SLSA tracks and levels to aim for |
| R-79 | The build must resolve dependencies through the ingestion platform, with pinned versions and integrity hashes. | developers | supply chain | S-03 dependency-track, Dep L2 | C-04 |
| R-80 | The ingestion platform blocks each path that does not go through it, and isolates its signing from the code of dependencies. | release and configuration managers | supply chain | S-03 dependency-track, Dep L3 | 3.3: Which SLSA tracks and levels to aim for |
| R-81 | If a proposal changes after an approval, the earlier approvals must be revoked. | developers | supply chain | S-03 source-example-controls, 2 | C-03 |
| R-82 | A branch protection rule must permit only revisions with passing test results. | quality and test staff | supply chain | S-03 source-example-controls, 3 | C-22 |
| R-83 | Identify, document and maintain the security requirements of the development and of the software. | security staff | security | S-04 page 14, PO.1.1 and PO.1.2 | C-19 |
| R-84 | Communicate the requirements to the third parties that supply components. | suppliers | supply chain | S-04 page 14, PO.1.3 | C-06 |
| R-85 | Define roles and responsibilities, give role-based training, and get the commitment of upper management. | management | security | S-04 pages 15 and 16, PO.2.1 to PO.2.3 | 3.3: How to organize the security work |
| R-86 | Specify the tools of each toolchain, operate them securely, and configure them to generate artefacts of the practices. | release and configuration managers | security | S-04 pages 16 and 17, PO.3.1 to PO.3.3 | C-29 |
| R-87 | Define the criteria for security checks and track them through the life cycle. | quality and test staff | security | S-04 page 17, PO.4.1 and PO.4.2 | C-29 |
| R-88 | Separate and protect each development environment, and harden the endpoints of developers. | developers | security | S-04 pages 17 and 18, PO.5.1 and PO.5.2 | C-13 |
| R-89 | Store all forms of code in a repository with restricted access. | release and configuration managers | supply chain | S-04 page 18, PS.1.1 | C-01 |
| R-90 | Give software acquirers the information to verify the integrity of a release. | consumers | supply chain | S-04 page 19, PS.2.1 | C-09 |
| R-91 | Archive the necessary files and the supporting data of each release. | release and configuration managers | supply chain | S-04 page 19, PS.3.1 | C-08 |
| R-92 | Collect, protect, maintain and share provenance data for all components of each release. | consumers | supply chain | S-04 page 19, PS.3.2 | C-12 |
| R-93 | Use risk modelling for the design, and track security requirements, risks and design decisions. | security staff | security | S-04 page 20, PW.1.1 and PW.1.2 | C-19 |
| R-94 | A qualified person who did not make the design, or a program, reviews the design. | security staff | security | S-04 page 21, PW.2.1 | 3.3: Which review a change gets before the merge |
| R-95 | Acquire well-secured components, and verify that they obey the requirements through their life. | suppliers | supply chain | S-04 pages 21 and 22, PW.4.1 and PW.4.4 | C-06 |
| R-96 | Follow the secure coding practices of the language and the environment. | developers | security | S-04 page 22, PW.5.1 | C-16 |
| R-97 | Use the security features of the compiler and the build tools, with approved configurations. | developers | security | S-04 page 23, PW.6.1 and PW.6.2 | C-16 |
| R-98 | Decide if code review or code analysis is used, do it, and record and triage each issue. | developers | security | S-04 page 23, PW.7.1 and PW.7.2 | C-16 |
| R-99 | Decide which tests of executable code are done, do them, and record and triage each issue. | quality and test staff | security | S-04 page 24, PW.8.1 and PW.8.2 | C-20 |
| R-100 | Define a secure default for each setting, and document the settings for administrators. | operations engineers | security | S-04 page 25, PW.9.1 and PW.9.2 | 3.3: How to prepare the operation |
| R-101 | Collect information on possible vulnerabilities from acquirers, users and public sources. | consumers | security | S-04 page 25, RV.1.1 | C-17 |
| R-102 | Review, analyse or test the code to find vulnerabilities that were not detected. | security staff | security | S-04 page 25, RV.1.2 | C-16 |
| R-103 | Have a vulnerability policy with roles and processes for disclosure and remediation. | security staff | security | S-04 page 26, RV.1.3 | C-17 |
| R-104 | Analyse each vulnerability, and plan and do the risk response. | security staff | security | S-04 pages 26 and 27, RV.2.1 and RV.2.2 | C-18 |
| R-105 | Find the root causes of vulnerabilities, look for the same class in the software, and change the process. | security staff | security | S-04 page 27, RV.3.1 to RV.3.4 | C-21 |
| R-106 | The bill of materials must be shared with end users. | consumers | supply chain | S-05 page 13, section 2.1 | C-12 |
| R-107 | Developer workstations should not be trusted as part of the build process. | release and configuration managers | supply chain | S-05 page 17, section 3.1.1 | C-07 |
| R-108 | The security team should set a policy for trusted open-source sources, and developers should verify signatures and scan new packages. | security staff | supply chain | S-05 page 21, section 3.2.1 | C-06 |
| R-109 | Developers should generate a bill of materials on the first commit. | developers | supply chain | S-05 page 21, section 3.2.1 | C-12 |
| R-110 | The pipeline should be audited at intervals, and monitoring should detect suspicious activity on its servers. | auditors and regulators | supply chain | S-05 page 21, section 3.2.1 | 3.3: How to organize the security work |
| R-111 | Write access to the source control system should be tightly controlled. | release and configuration managers | supply chain | S-05 page 21, section 3.2.2 | C-13 |
| R-112 | A second developer should review a patch before the merge. | developers | supply chain | S-05 page 21, section 3.2.2 | duplicate: R-69 |
| R-113 | Code analysis tools should find common mistakes, without so many false positives that developers stop to look. | developers | security | S-05 page 21, section 3.2.2 | C-16 |
| R-114 | The integrity of artefacts and repositories should be ensured by verification of their digital signatures. | consumers | supply chain | S-05 page 23, section 4.2 | C-09 |
| R-115 | Evidence of the build should come from a process with more trust or isolation than the build. | release and configuration managers | supply chain | S-05 page 25, section 5.1.1 | C-10 |
| R-116 | Attestations must be signed, and their storage must be protected against tampering. | release and configuration managers | supply chain | S-05 page 26, section 5.1.1 | C-09 |
| R-117 | Developers with the permission to approve merges cannot approve their own merges. | developers | supply chain | S-05 page 26, section 5.1.2 | C-03 |
| R-118 | Automated checks should run on all artefacts of a pushed change. | quality and test staff | supply chain | S-05 page 27, PULL-PUSH_REQ-1 | C-22 |
| R-119 | For a public repository, the source control system should run workflows of outside contributors in a sandbox, or wait for the approval of a maintainer. | release and configuration managers | supply chain | S-05 page 27, PULL-PUSH-REQ-3 | C-11 |
| R-120 | Online keys should not be used for a role that clients trust for the files that they install. | release and configuration managers | supply chain | S-05 page 28, section 5.1.3 | 5 |
| R-121 | Static and dynamic security test tools for all languages in use should run in the pipeline. | security staff | security | S-05 page 28, section 5.1.4 | C-16 |
| R-122 | If open-source modules are used, dependencies must be enumerated, with the transitive ones, and evaluated against policy. | developers | supply chain | S-05 page 29, section 5.1.4 | C-05 |
| R-123 | Committed code should be examined for secrets, with alerts on violations. | security staff | security | S-05 page 29, COMMIT-REQ-1 | C-15 |
| R-124 | Push protection should verify the identity of the developer and enforce signed commits. | release and configuration managers | supply chain | S-05 page 29, COMMIT-REQ-2 | C-13 |
| R-125 | If a secure build process is established, it should be possible to require that a deployed artefact came from it. | operations engineers | supply chain | S-05 page 29, DEPLOY-REQ-3 | C-14 |
| R-126 | A container image should be scanned when it is built, before a push to a registry, with evidence of the scan. | operations engineers | security | S-05 page 30, DEPLOY_REQ-4 | 3.3: Which security scans the pipeline runs |
| R-127 | The deployment should rely on automation, not on manual operations. | operations engineers | operations | S-05 page 30, GitOps-REQ-1 | C-30 |
| R-128 | Changes should not be applied by hand at run time; a change goes to the code and starts a new release. | operations engineers | operations | S-05 page 31, GitOps-REQ-3 | C-30 |
| R-129 | The repository should be pulled automatically and compared with the specified state, with notifications of differences. | operations engineers | operations | S-05 page 31, GitOps-REQ-4 | C-30 |
| R-130 | Security decisions should move to the persons with the most context. | developers | security | S-06 0-a Overview, What DevSecOps Means | 3.3: How to organize the security work |
| R-131 | Large security tests should be split into smaller tests that run in the pipeline. | security staff | security | S-06 0-a Overview, Shift-Left Security | C-16 |
| R-132 | Applications with much personal data should use privacy by design. | consumers | security | S-06 0-a Overview, Privacy | 3.3: Which data protection measures apply |
| R-133 | Threat modelling should start as early as possible in the design. | security staff | security | S-06 0-b Threat Modeling, Timing | C-19 |
| R-134 | Secrets should not be in source code, and commits and the repository should be scanned for sensitive data. | developers | security | S-06 1-a Secrets Management | duplicate: R-123 |
| R-135 | Leaked credentials should be invalidated. | security staff | security | S-06 1-a Secrets Management | C-15 |
| R-136 | Component analysis should run early, before the other security tests, and libraries should be monitored continuously. | developers | security | S-06 2-d Software Composition Analysis | C-05 |
| R-137 | Remove generated executable files from the repository, and build from source. | release and configuration managers | supply chain | S-07 Binary-Artifacts | C-01 |
| R-138 | Protect important branches against forced pushes and deletion. | release and configuration managers | supply chain | S-07 Branch-Protection | C-02 |
| R-139 | Run all tests in the pipeline on each pull request. | quality and test staff | quality | S-07 CI-Tests | C-22 |
| R-140 | Make the review of each pull request mandatory. | developers | supply chain | S-07 Code-Review | 3.3: Which review a change gets before the merge |
| R-141 | Do not check out untrusted code in risky triggers, and keep untrusted input out of executable code. | release and configuration managers | supply chain | S-07 Dangerous-Workflow | C-11 |
| R-142 | Use a tool that updates dependencies. | developers | supply chain | S-07 Dependency-Update-Tool | 5 |
| R-143 | Use fuzzing. | security staff | security | S-07 Fuzzing | 3.3: Which security scans the pipeline runs |
| R-144 | Declare exact versions, keep lock files, and pin images and pipeline actions by hash. | developers | supply chain | S-07 Pinned-Dependencies | duplicate: R-79 |
| R-145 | Run static analysis in the pipeline. | security staff | security | S-07 SAST | C-16 |
| R-146 | Generate a bill of materials. | consumers | supply chain | S-07 SBOM | C-12 |
| R-147 | Add a security policy file with a secure way to report. | security staff | security | S-07 Security-Policy | C-17 |
| R-148 | Sign the release, and attach the signature to it. | consumers | supply chain | S-07 Signed-Releases | C-09 |
| R-149 | Set the permissions of pipeline tokens to read by default, and to write only for a job that needs it. | release and configuration managers | supply chain | S-07 Token-Permissions | C-11 |
| R-150 | Correct open vulnerabilities as soon as possible. | security staff | security | S-07 Vulnerabilities | C-18 |
| R-151 | Set a secret on each webhook. | release and configuration managers | security | S-07 Webhooks | 5 |
| R-152 | Each commit should start a build and automated tests, with feedback in minutes. | developers | quality | S-08 continuous-integration, How to implement CI | C-22 |
| R-153 | Developers should merge into the trunk at least each day. | developers | quality | S-08 continuous-integration, How to implement CI | 3.3: How to branch |
| R-154 | The repair of a broken build has priority, and a build that cannot be repaired in minutes should be reverted. | developers | quality | S-08 continuous-integration, Common pitfalls | C-24 |
| R-155 | New or changed functions get unit tests and acceptance tests from the developers. | developers | quality | S-08 test-automation, Ways to improve test automation | C-23 |
| R-156 | When a pipeline does not catch a problem, the pipeline must be improved, and the fastest test category should catch an error. | quality and test staff | quality | S-08 test-automation, Common pitfalls | C-26 |
| R-157 | Tests should be reliable, and teams should not accept flaky tests. | quality and test staff | quality | S-08 test-automation, Common pitfalls | C-27 |
| R-158 | Teams should do manual tests, such as exploratory and usability tests, through the delivery. | quality and test staff | quality | S-08 test-automation, How to implement automated testing | 3.3: Which tests the project keeps |
| R-159 | Teams should have health reports, customer-experience reports, business metrics and debugging tools. | operations engineers | operations | S-08 monitoring-and-observability, introduction | C-33 |
| R-160 | Alerts should be on symptoms, and alerts without an action should be deleted. | operations engineers | operations | S-08 monitoring-and-observability, Common pitfalls | C-34 |
| R-161 | Monitoring should not be the work of one person or one team only. | developers | operations | S-08 monitoring-and-observability, Common pitfalls | 3.3: How to prepare the operation |
| R-162 | The security team should take part in the design of all projects, and review major features without a delay to development. | security staff | security | S-08 pervasive-security, Get InfoSec involved in software design | 3.3: How to organize the security work |
| R-163 | Automated testing requires that teams design and develop automated security tests, and the security requirements are tested in the automated tests. | security staff | security | S-08 pervasive-security, Develop automated testing | C-19 |
| R-164 | The security team builds approved libraries, packages and toolchains for developers and operations. | security staff | security | S-08 pervasive-security, Ways to improve security quality | 3.3: How to organize the security work |
| R-165 | Nobody should have to work outside business hours for deployments or releases. | operations engineers | operations | S-08 continuous-delivery, Measuring continuous delivery | 3.3: How to release to users |
| R-166 | Do not set the delivery metrics as goals, and do not compare vastly different applications. | management | operations | S-08 dora-metrics, Common pitfalls | 3.3: How to measure the progress |
| R-167 | Teams should define a small number of service level indicators and objectives, and say how each is measured. | operations engineers | operations | S-09 chapter 4, Defining Objectives | C-35 |
| R-168 | Teams should keep an error budget and track it. | operations engineers | operations | S-09 chapter 4, Defining Objectives | 3.3: Which service levels to set |
| R-169 | Targets should not come from the current performance, and should not be absolute. | management | operations | S-09 chapter 4, Choosing Targets | 3.3: Which service levels to set |
| R-170 | For a system with users, measure the four golden signals of the source, if no more can be measured. | operations engineers | operations | S-09 chapter 6, The Four Golden Signals | C-33 |
| R-171 | Each page to a person should need an action, and alerts favour symptoms above causes. | operations engineers | operations | S-09 chapter 6, Tying These Principles Together | duplicate: R-160 |
| R-172 | For frequent alerts, find and remove the root cause, or automate the response. | operations engineers | operations | S-09 chapter 6, Monitoring for the Long Term | C-34 |
| R-173 | Builds must be repeatable and must not depend on external services. | release and configuration managers | supply chain | S-09 chapter 8, Hermetic Builds | C-07 |
| R-174 | A system runs unit tests on each change, and a release uses the last revision that passed all tests. | quality and test staff | quality | S-09 chapter 8, Testing | duplicate: R-152 |
| R-175 | Access controls gate the release actions, and almost all changes need code review. | release and configuration managers | supply chain | S-09 chapter 8, Enforcement of Policies and Procedures | C-03 |
| R-176 | All configuration is in the primary repository, with strict review. | release and configuration managers | operations | S-09 chapter 8, Configuration Management | C-01 |
| R-177 | Binaries should report the build date, the revision and the build identifier. | operations engineers | operations | S-09 chapter 8, Building | C-33 |
| R-178 | Teams should budget release engineering at the start of the development. | release and configuration managers | operations | S-09 chapter 8, Conclusions | C-37 |
| R-179 | Preparation and regular hands-on training for emergencies are necessary, with the support of management. | management | operations | S-09 chapter 13, introduction | 3.3: How to prepare the operation |
| R-180 | The company of the source requires thorough tests of rollback procedures before large-scale tests. | operations engineers | operations | S-09 chapter 13, Test-Induced Emergency | C-31 |
| R-181 | Canary each change, also when its risk seems low. | operations engineers | operations | S-09 chapter 13, Change-Induced Emergency | C-32 |
| R-182 | Follow the incident response process, and write up the incident after the mitigation. | operations engineers | operations | S-09 chapter 13, All Problems Have Solutions | C-36 |
| R-183 | A postmortem is expected after each significant event, with criteria that are defined before, and without blame. | operations engineers | operations | S-09 chapter 15, Google's Postmortem Philosophy | C-36 |
| R-184 | Postmortems are reviewed and shared, without data that identifies end users. | management | operations | S-09 chapter 15, Collaborate and Share Knowledge | C-36 |
| R-185 | New code changes include tests, and engineers write and run the tests of their code. | developers | quality | S-10 chapter 11, Write, Run, React | duplicate: R-155 |
| R-186 | After a person finds an issue, an automated test should prevent the regression. | quality and test staff | quality | S-10 chapter 11, The Limits of Automated Testing | C-26 |
| R-187 | At the company of the source, essentially each change gets the approval of a second engineer and of an owner before the commit. | developers | quality | S-10 chapter 9, Code Review Flow | 3.3: Which review a change gets before the merge |
| R-188 | Changes should be small and about one issue. | developers | quality | S-10 chapter 9, Write Small Changes | 3.3: Which review a change gets before the merge |
| R-189 | Checks before the submit should do tests, linting and formatting before the review. | developers | quality | S-10 chapter 9, Automate Where Possible | C-28 |
| R-190 | What a program can correct should be corrected by a program. | developers | quality | S-10 chapter 20, Usability | C-28 |
| R-191 | A new check must be actionable with few false positives, and existing instances are cleaned before a check is enabled. | quality and test staff | quality | S-10 chapter 20, Compiler Integration | C-29 |
| R-192 | Only fast and reliable tests run before the submit; slower tests run after it. | quality and test staff | quality | S-10 chapter 23, Presubmit versus post-submit | C-25 |
| R-193 | A full automated test suite runs against a release candidate, and the same suite runs against production. | quality and test staff | quality | S-10 chapter 23, Release candidate testing | C-25 |
| R-194 | Configuration is tested with the code that uses it, and artefacts are not compiled again between environments. | release and configuration managers | quality | S-10 chapter 23, Continuous Delivery and release candidates | C-38 |
| R-195 | Changes that break tests must be corrected quickly, and teams do not commit on failing tests. | developers | quality | S-10 chapter 23, CI at Google | duplicate: R-154 |
| R-196 | A test that is disabled must be tracked. | quality and test staff | quality | S-10 chapter 23, CI Case Study | C-27 |
| R-197 | Engineers must guard all changes with flags. | developers | operations | S-10 chapter 24, Evaluating Changes in Isolation | 3.3: How to release to users |
| R-198 | Teams should develop at the head of the shared code, not on long-lived branches. | developers | quality | S-10 chapter 24, Velocity Is a Team Sport | 3.3: How to branch |
| R-199 | Teams should set up automatic rollbacks. | operations engineers | operations | S-10 chapter 24, Velocity Is a Team Sport | duplicate: R-180 |
| R-200 | Teams should release early and frequently, in small batches. | release and configuration managers | operations | S-10 chapter 24, Introduction | 3.3: How to release to users |
| R-201 | Keep all that is necessary for the build in version control, and nothing that is built. | developers | quality | S-11 Put everything in a version controlled mainline | C-01 |
| R-202 | Pin dependencies to specific versions. | developers | supply chain | S-11 Put everything in a version controlled mainline | duplicate: R-79 |
| R-203 | One command on a clean machine should give a running system. | developers | quality | S-11 Automate the Build | C-07 |
| R-204 | A full automated test suite should run before each integration. | developers | quality | S-11 Make the Build Self-Testing | duplicate: R-152 |
| R-205 | Each developer should commit to the mainline each day. | developers | quality | S-11 Everyone Pushes Commits To the Mainline Every Day | 3.3: How to branch |
| R-206 | The repair of a broken build should be urgent. | developers | quality | S-11 Fix Broken Builds Immediately | duplicate: R-154 |
| R-207 | When a later stage finds a bug, add a test to the commit build. | developers | quality | S-11 Keep the Build Fast | C-26 |
| R-208 | Test environments should mimic production as far as possible. | operations engineers | quality | S-11 Test in a Clone of the Production Environment | C-38 |
| R-209 | Script the deployment for each environment, and show the version in the running software. | operations engineers | operations | S-11 Automate Deployment | duplicate: R-127 |
| R-210 | Privileged developers use multi-factor authentication. | developers | security | S-13 item 1 | C-13 |
| R-211 | Use a combination of tools in the pipeline to find vulnerabilities; tools should not be the only means. | security staff | security | S-13 item 3 | C-16 |
| R-212 | Add a dependency only if it is necessary, evaluate it, and get it from the correct repository. | developers | supply chain | S-13 item 4 | C-06 |
| R-213 | The test suite is good enough to ship when it passes. | developers | quality | S-13 item 6 | C-23 |
| R-214 | Delay the update of components without known vulnerabilities, typically for about three days. | developers | supply chain | S-13 item 8 | 3.3: How fast to take dependency updates |
| R-215 | Do not push secrets to a repository, and use tools that detect it. | developers | security | S-13 item 9 | duplicate: R-123 |
| R-216 | Make updates easy for the users: semantic versions and a deprecation process. | consumers | supply chain | S-13 item 12 | 3.3: How to release to users |
| R-217 | Use standard tools and signing formats for the distribution. | consumers | supply chain | S-13 item 13 | C-09 |
| R-218 | An open source project gets at least the passing level of the best practices badge. | developers | security | S-13 item 14 | 3.3: How to measure the progress |
| R-219 | Publish security advisories with exact information. | consumers | security | S-13 item 16 | C-18 |
| R-220 | Improve the SLSA level. | release and configuration managers | supply chain | S-13 item 17 | 3.3: Which SLSA tracks and levels to aim for |
| R-221 | Publish and consume a bill of materials. | consumers | supply chain | S-13 item 18 | C-12 |
| R-222 | A released source package should hold only content of the version control system. | release and configuration managers | supply chain | S-13 item 27 | C-01 |
| R-223 | Staff in software development get security awareness training, and each development team has a security champion. | management | security | S-14 education-and-guidance, maturity 1 | 3.3: How to organize the security work |
| R-224 | Define the build process so that it is repeatable and holds no secrets, and keep a bill of materials of the dependencies. | release and configuration managers | security | S-14 secure-build, maturity 1 | C-07 |
| R-225 | Developers should not have the secrets of production and should not need direct access to production. | developers | security | S-14 secure-deployment, maturity 1 | C-30 |
| R-226 | Each security defect of an application must be visible at each moment. | security staff | security | S-14 defect-management, stream A, maturity 1 | C-18 |
| R-227 | Security tests must at least verify the controls for authentication, access, input validation, encoding and encryption. | security staff | security | S-14 requirements-driven-testing, stream A, maturity 1 | C-19 |
| R-228 | Teams should be able to find the versions of all components in use. | operations engineers | security | S-14 environment-management, stream B, maturity 1 | C-12 |

## Proposed boundaries

| Boundary | Requirements that it would take | Stakeholders that it would leave with no requirement | Reason |
|---|---|---|---|
| secure design | R-93, R-94, R-133 | none | The source for pipelines leaves certain practices of secure design out (S-05 page 41). The design work has its own practices (S-04 pages 20 and 21; S-06 0-b Threat Modeling). |
| security management of the organization | R-19, R-20, R-35, R-50, R-85, R-223 | none | These requirements are for the organization, not for one project: the body of knowledge gives them to senior management (S-01 pages 159 and 265), and the framework puts them into the group that prepares the organization (S-04 pages 15 and 16). |
| platform operation | R-16, R-55, R-76, R-77 | none | The operations organization and the platform carry these duties (S-01 pages 157 to 159). The draft gives the requirements of the build environment track to the image producer, the build platform and the compute platform, not to the project (S-03 build-env-track-basics). |
| privacy | R-132, R-53 | none | Privacy regulations impose the controls on personal data (S-06 2-g Privacy), and the body of knowledge treats data privacy as a legal subject of professional practice (S-01 page 281). |

## Reading

The program `index.py unread --write` writes this table. Do not change it by hand.

| Source | Document | Pages | Given to readers | Not read |
|---|---|---|---|---|
| S-01 | swebok | 411 | 1-25, 26-42, 43-66, 67-82, 83-98, 99-116, 117-141, 142-166, 167-184, 185-201, 202-220, 221-245, 246-263, 264-287, 288-311, 312-335, 336-344, 345-366, 367-386, 387-411 | none |
| S-04 | S-04 | 36 | 1-25, 26-36 | none |
| S-05 | S-05 | 41 | 1-23, 24-41 | none |
