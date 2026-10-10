# Aspect specification: DevSecOps

**Branch**: `001-devsecops` | **Research date**: 2026-10-11 | **Supersedes**: none | **Accepted**: pending

Layer one of the factory: the exploration of one major aspect of software engineering. This
specification is the source of the recipe for the aspect, a strategy and a generic checklist
that hold the global state of the art (SOTA): the best practices that the industry has produced
so far. A helper renders the recipe skill from it. The implementation skills for single products
are layer two: each set gets its own specification through the Spec Kit product flow. Keep this
file high level. It holds nothing that an agent can learn from the project or from a source.

## 1. Aspect

Settled with the owner before the research. Only the field, the thing to build and the intent
of the owner: no use case, no first user, no stakeholder, nothing narrower.

- **Aspect**: DevSecOps
- **Field and disciplines**: software engineering; the disciplines of the concerns that the
  owner names in the line `meaning`: operation, security and quality
- **Intent of the owner**: the answers of the owner to the questions of phase 1. One line each:
  the words of the owner as a quote, with the date, or `(no answer)`.
  - `meaning`: "DevSecOps is about doing shift left of operational, security, and quality concerns." (2026-10-10)
  - `result`: "achieve SLSA draft highest levels" (2026-10-10)
  - `not wanted`: (no answer)
- **Agreed with the owner on**: 2026-10-11; the field: software engineering; the thing to
  build: the aspect specification and the recipe skill `devsecops`. The owner gave the thing to
  build on 2026-10-10: "do the DevSecOps research and generate a skill". The owner was not in
  the session of 2026-10-11.

Found by the research, and reviewed by the owner with the other findings. Each line names its
source, or says `(judgement)`. A use case is chosen only when the recipe is applied to a project.

- **Stakeholders**: each group of persons that has an interest in the result or carries a duty
  for it. The research finds them in the body of knowledge of the field and in the sources.
  One line each: a short name, the concerns of the stakeholder for this aspect, and the source.
  - `developers`: the persons who write and integrate the code. They want fast feedback on a change, and they must find defects and vulnerabilities before the merge. (S-01 pages 107 and 153; S-03 page 11; S-08 capability "continuous integration")
  - `quality engineers`: the testers, the reviewers and the persons of quality assurance. They want tests and reviews from the start of the work, and thresholds for each quality requirement. (S-01 pages 138, 211 and 255; S-08 capability "test automation")
  - `operations engineers`: the persons who deploy, operate and support the software, also site reliability engineers and persons on call. They want availability, monitoring, a safe deployment, a rollback and a recovery. (S-01 pages 152 to 153; S-09 chapter "Monitoring Distributed Systems")
  - `security staff`: the security team, the security experts and the security champions. They want the threats and the vulnerabilities found early, and security tests that have an authorization. (S-01 pages 266 and 268; S-03 pages 15 and 20)
  - `management`: the senior management, the project managers and the organization. They carry the duty for the security policy, the commitment, the risk and the compliance. (S-01 pages 159 and 265; S-03 task PO.2.3)
  - `platform operators`: the persons who operate the build platform, the source control system and the toolchain. They want isolated builds, protected signing keys and records that can be audited. (S-02 v1.2 "build-track-basics"; S-03 page 11; S-04 page 24)
  - `consumers`: the acquirers and the users of the software, and the projects that depend on it. They want to verify the integrity and the origin of an artifact, and to get the information about its components and its vulnerabilities. (S-03 pages 4 to 5; S-02 v1.2 "verifying-artifacts"; S-04 pages 13 and 25; S-07 README)
  - `maintainers`: the persons who keep the software usable and secure after the delivery, also the maintainers of an open source project. They want controlled changes and a process for the reports of users. (S-01 page 179; S-04 page 27; S-07 README)
- **Views**: the points of view that the aspect brings together. A view is a set of concerns
  of the aspect. The research aggregates the concerns of the stakeholders into the views. A
  concern that the owner named in the intent is in a view, or section 7 says why it is not.
  One line each: a short name, what the view is concerned with, the stakeholders whose
  concerns the view holds, and the source. Name the stakeholders in this form, before the
  source: `(stakeholders: [name], [name])`. Use the names of the field "Stakeholders".
  - `security`: the threats to the software and its vulnerabilities, treated from the requirements to the response after the release. (stakeholders: developers, security staff, management) (S-01 pages 264 to 269, knowledge area "Software Security"; S-03 section 2)
  - `quality`: the tests, the reviews, the analysis and the integration of each change, done early and continuously. (stakeholders: developers, quality engineers, maintainers) (S-01 pages 117 to 143 and 246 to 261, knowledge areas "Software Testing" and "Software Quality"; S-13 chapter 1 "Shifting Left")
  - `operation`: the deployment, the monitoring, the reliability and the recovery of the software, planned while the software is developed. (stakeholders: operations engineers, developers, management, maintainers) (S-01 pages 151 to 166, knowledge area "Software Engineering Operations"; S-09)
  - `supply chain`: the integrity of the source, of the build, of the dependencies and of the released artifacts. The owner named this concern with the target of the line `result`. (stakeholders: platform operators, consumers, developers, security staff, maintainers) (S-01 pages 103 and 192 to 198, knowledge areas "Software Construction" and "Software Configuration Management"; S-02; S-04)
- **Contexts**: the values of each dimension that change the strategy. One line each.
  - `team size`: one maintainer; a team; an organization with many teams. (S-12 "When we should not use Continuous Integration"; S-02 v1.2 "source-requirements" level 4; S-07 "checks.md" check Contributors)
  - `type of delivery`: a service that the team operates; a product or a package that consumers install; a library. (S-09 "Reliable Product Launches"; S-02 v1.2 "verifying-artifacts"; S-03 page 12)
  - `operator of the build platform`: a hosted platform of a provider; a platform that the organization operates. (S-02 v1.2 "build-requirements"; S-03 page 12)
  - `contributors`: only members of the team; also persons from outside who send changes. (S-04 pages 19 and 27; S-07 "checks.md")
  - `regulation`: no rule from outside; a law, a contract or an acquirer asks for evidence. (S-03 page 33; S-08 capability "streamlining change approval"; S-04 page 20)
  - `lifetime`: a project with a short life; a project that lives for years. (S-13 chapter 1 "Software Engineering Versus Programming")
- **Risk dimensions**: the dimensions on which the risk of a project differs for this aspect.
  One line each: the name, the question that finds it out, the opinion of the kit on the
  answer, and the source.
  - `supply chain`: Who installs or runs the artifacts of the project, and what harm occurs if an artifact or a dependency was changed by an attacker? Opinion: a project whose artifacts other persons install goes to the highest levels of the target, because those persons trust the usual channel. A project without consumers stops at level 1. (S-04 pages 13 to 14; S-02 v1.2 "build-track-basics")
  - `security`: What does an attacker get from a vulnerability of the software: data, access or money? Opinion: choose the practices by this risk, and go past level 1 when the software holds data of other persons or is reachable from a public network. (S-03 pages 8 and 12; S-01 page 210)
  - `operative`: What does one hour of failure of the software cost its users? Opinion: a service with users who depend on it goes past level 1. More reliability than the users need is a cost without a return. (S-09 "Embracing Risk"; S-01 page 158)
  - `quality`: What does a defect cost when it reaches the users, compared with a defect that is found before the merge? Opinion: a project with a long life or with many contributors goes past level 1. A project with a short life can stop there. (S-13 chapter 1 "Shifting Left"; S-01 page 249)
  - `regulatory`: Does a law, a contract or an acquirer ask for evidence of the practices? Opinion: if yes, record each control in the platform, thus the evidence is made by a program and not by hand. (S-03 page 33; S-08 capability "streamlining change approval")
- **Boundaries**: what each neighbouring aspect owns, and what this aspect keeps. One line each.
  - `requirements engineering`: it owns how requirements are found, written and changed. This aspect keeps that the security requirements and the operations requirements are stated early. (S-01 pages 43 to 62)
  - `architecture`: it owns the structure of the system and its design documents. This aspect keeps the threat model, the review of the design and the demand for small, independent deployments. (S-01 pages 69 to 77 and 161; S-08 capability "deployment automation")
  - `incident management`: it owns the response to an incident in operation: the roles, the communication and the handoff. This aspect keeps the preparation in development: the rollback, the monitoring and the review after the incident. (S-09 "Managing Incidents"; S-06 practice "Incident Management")
  - `privacy`: it owns the lawful processing of personal data. This aspect keeps only that an incident review holds no data that identifies a user. (S-05 "02g-Privacy"; S-01 page 281)
  - `organization`: it owns the security policy, the roles, the staff and the training of the organization. This aspect keeps the commitment of the management to secure development as a condition. (S-01 pages 153 to 159; S-03 tasks PO.2.1 to PO.2.3)
  - `engineering management`: it owns the planning, the estimates, the measurement, the improvement of the process and the legal duties of the profession. This aspect keeps the thresholds for quality requirements. (S-01 pages 202 to 232 and 274 to 311)
  - `configuration management`: it owns the plan, the audits and the status accounting of configuration items. This aspect keeps the version control of all that builds and deploys the software, and the ability to make a release again. (S-01 pages 185 to 201)
  - `maintenance`: it owns the categories of maintenance, the impact analysis and the technical debt. This aspect keeps the tests of each change and the process for reports of users. (S-01 pages 167 to 184)
  - `procurement`: it owns the contracts with the suppliers of software and services. This aspect keeps the verification of what a supplier delivers. (S-03 page 8 and task PO.1.3; S-06 practice "Security Requirements")
  - `network operation`: it owns the security and the monitoring of networks. This aspect keeps nothing of it. (S-01 pages 333 to 335)
- **Targets**: the measurable results that a project reaches when it applies the recipe. The
  targets come from the sources in the research; the owner can name one in the intent. One
  line each: the name, the scale with its levels, the program or the method that measures it,
  and the source of the scale. If the sources give no target, write `(none found)` in place
  of the lines.
  - `SLSA draft highest levels`: the target of the owner. The working draft of the SLSA specification has these tracks with levels: Build (L0 to L3), Source (L1 to L4), Dependency (L0 to L3) and Build Environment (the pages that were read name only L3). The highest levels are thus Build L3, Source L4, Dependency L3 and Build Environment L3. The draft can change or be discarded. No program gives the level of a project: a level is defined by its requirements, the consumer verifies the provenance of an artifact, and the source control system issues a summary attestation for a revision. (S-02 "draft/levels", "draft/dependency-track", v1.2 "build-track-basics", "source-requirements" and "verifying-artifacts")
  - `SLSA released levels`: version 1.2 has the status "Approved". It has the Build track (L0 to L3) and the Source track (L1 to L4), and not the two other tracks. The method is the same as for the draft. (S-02 "spec" index, v1.2 "build-track-basics" and "source-requirements")
  - `Scorecard score`: 0 to 10 for each check, and a weighted average of the checks. The program OpenSSF Scorecard measures a repository. (S-07 README)
  - `software delivery performance`: five measured values: change lead time, deployment frequency, failed deployment recovery time, change fail rate and deployment rework rate. The source gives no levels and no thresholds. The team measures one application or service, and follows the trend. (S-08 guide "dora-metrics")
  - `service level objective`: a target value or range for a service level indicator that the project chooses, and the error budget that follows from it. Monitoring measures it over a time window. (S-09 "Service Level Objectives" and "Embracing Risk")
  - `test feedback time`: the time until the automated tests give feedback on a change, with ten minutes as the upper limit. The pipeline measures it. (S-08 capabilities "continuous integration" and "test automation"; S-12 "Keep the build fast")
  - `SAMM maturity`: three maturity levels for each of 15 security practices. An assessment with questions and quality criteria gives the score. (S-06 "model", "about" and "assessment")
  - `DSOMM maturity`: five maturity levels for the activities of each dimension. The team marks each activity that it has done. (S-10 repository file "meta.yaml" and README)

## 2. Sources

No single source gates the recipe: the recipe is the fixed side, and each source supports the
items that cite it. **Class** decides the route of admission. The fast lane: `standard`
(standards bodies and regulators), `foundation` (open foundations), `vendor` (a platform vendor
on its own platform), `research` (peer-reviewed research and recognized books), `trusted-data`
(a recorded data source marked as trusted). Every other source is `independent` and passes the
source vetting first. **Read**: full, part or no. A paid source is cited from its official
preview and marked part. **Views**: the views of section 1 that the source was read for, with a
comma between two names, or `all` for a body of knowledge. Each view has two or more sources
of its own field that were read.

| Id | Source | Issuer | Version or date | Class | License | Read | Views | URL |
|---|---|---|---|---|---|---|---|---|
| S-01 | Guide to the Software Engineering Body of Knowledge (SWEBOK Guide) | IEEE Computer Society | 4.0a, 2026-08 | standard | Copyright IEEE; free for personal and academic use | full | all | https://www.computer.org/education/bodies-of-knowledge/software-engineering |
| S-02 | SLSA specification | The SLSA project (The Linux Foundation) | 1.2 (Approved) and the working draft, read 2026-10-11 | foundation | Community Specification License 1.0 | part | supply chain | https://slsa.dev/spec/ |
| S-03 | Secure Software Development Framework (SSDF), NIST SP 800-218 | National Institute of Standards and Technology | 1.1, 2022-02 | standard | Not subject to copyright in the United States | full | security | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf |
| S-04 | Strategies for the Integration of Software Supply Chain Security in DevSecOps CI/CD Pipelines, NIST SP 800-204D | National Institute of Standards and Technology | 2024-02 | standard | Not subject to copyright in the United States | full | supply chain | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204D.pdf |
| S-05 | OWASP DevSecOps Guideline | OWASP Foundation | v-0.2, read 2026-10-11 | foundation | CC BY-SA 4.0 | part | security | https://owasp.org/www-project-devsecops-guideline/ |
| S-06 | OWASP Software Assurance Maturity Model (SAMM) | OWASP Foundation | Version 2, read 2026-10-11 | foundation | CC BY-SA 4.0 | part | security | https://owaspsamm.org/model/ |
| S-07 | OpenSSF Scorecard | Open Source Security Foundation | read 2026-10-11 | foundation | Apache-2.0 | part | supply chain | https://github.com/ossf/scorecard |
| S-08 | DORA capabilities and software delivery performance metrics | DORA (a program of Google Cloud) | read 2026-10-11 | research | CC BY 4.0 | part | operation, quality | https://dora.dev/capabilities/ |
| S-09 | Site Reliability Engineering (online edition) | Google; O'Reilly Media | 2017 | research | CC BY-NC-ND 4.0 | part | operation | https://sre.google/sre-book/table-of-contents/ |
| S-10 | OWASP DevSecOps Maturity Model (DSOMM) | OWASP Foundation | read 2026-10-11 | foundation | GPL-3.0 (program); CC BY-SA (model) | part | security | https://owasp.org/www-project-devsecops-maturity-model/ |
| S-11 | ISO/IEC 25010:2023, Product quality model | ISO/IEC | 2023 | standard | Copyright ISO; paid | no | quality | https://www.iso.org/standard/78176.html |
| S-12 | Continuous Integration | Martin Fowler | 2024-01-18 | independent | Copyright of the author | full | quality | https://martinfowler.com/articles/continuousIntegration.html |
| S-13 | Software Engineering at Google (online edition) | Google; O'Reilly Media | read 2026-10-11 | research | CC BY-NC-ND 4.0 | part | quality | https://abseil.io/resources/swe-book/html/toc.html |
| S-14 | Minimum Viable Continuous Delivery (MinimumCD) | MinimumCD Authors | 2026-10-08 | independent | CC BY 4.0 | part | operation, quality | https://minimumcd.org/ |
| S-15 | DoD Enterprise DevSecOps Fundamentals | Department of Defense, Chief Information Officer | 2.5 | standard | not verified | no | security, operation | https://dodcio.defense.gov/Portals/0/Documents/Library/DoD%20Enterprise%20DevSecOps%20Fundamentals%20v2.5.pdf |

## 3. Strategy

High level, for the agent that runs the work. One page.

### 3.1 Goals

- A defect, a vulnerability or an operations problem is found at the earliest step where a
  program or a person can find it: before the commit, before the merge, before the release.
- Each change goes to the users through one automated path that builds, tests, verifies and
  deploys it, and each step of the path leaves a record.
- A consumer can verify where an artifact comes from and how it was built, up to the level
  of the target that the owner of the project chose.
- The persons who operate the software and the persons who secure it state their requirements
  when the work starts, not when it ends.
- The project measures the result with the targets of the aspect, and it goes past the basic
  practices only where its risk calls for that.

### 3.2 Order of the work

1. Find the contexts of the project and do the risk analysis along the risk dimensions. The
   answers decide the target levels, thus do this before a change.
2. Put all that builds, configures and deploys the software into version control, and protect
   the main branch. Each later step uses this record.
3. Make the automated build and its tests run on each commit, and make the team correct a
   broken build first. Without this feedback, a later check has no place to run.
4. Add the early checks to that path: secrets, static analysis, known vulnerabilities of the
   dependencies. They are cheap, and they stop the most frequent faults.
5. State the security requirements, the threat model and the operations requirements for the
   work that comes next. They tell which later tests and controls are necessary.
6. Make the release path: a hosted build, provenance, a signed release, the record of each
   dependency. Then go up the levels of the supply chain target one level at a time.
7. Make the operation path: one automated deployment, a rollback, monitoring of what users
   see. Add the service level objective and the staged release where the operative risk
   calls for them.
8. Close the loop: a process for vulnerability reports, a review after each incident, and
   the correction of the root cause in the process.
9. Measure with the targets, show the distance to the owner of the project, and repeat from
   step 4 for the next level.

### 3.3 Decisions that depend on context

| Decision | Depends on | Options | Sources |
|---|---|---|---|
| How many persons approve a change | team size; contributors; risk dimension supply chain | One maintainer with automated controls only. One reviewer for each change. Two trusted persons for each change of a protected branch, enforced by the source control system: this is the highest level of the Source track. | S-02 v1.2 "source-requirements"; S-13 chapter 9; S-08 capability "trunk-based development"; S-12 |
| Which build platform to use | operator of the build platform; the target level | A hosted platform that can reach the target level. A platform that the organization operates and hardens. With a provider, agree which party does each practice. | S-02 v1.2 "build-requirements"; S-03 pages 12 and 16 |
| Which security tests to run | type of delivery; risk dimension security | Static analysis and scans in the pipeline only. Also dynamic tests and fuzzing. Also tests by security experts, with an authorization. | S-03 tasks PW.7.1 and PW.8.1; S-05; S-01 page 268 |
| How much verification the software needs | risk dimensions quality and security; lifetime | The minimum tasks for the integrity level of the software. Also tests in an environment that is like production. Also manual and exploratory tests. | S-01 pages 251 and 257 to 258; S-14 "production-like-environments"; S-08 capability "test automation" |
| Which tests run before the merge | size of the code base; the time that the tests take | All tests on each change. Fast and reliable tests before the merge, slow tests after it. | S-13 chapter 23; S-08 capability "continuous integration"; S-04 page 28 |
| How to release a change to the users | type of delivery; risk dimension operative | Each change that passes the pipeline goes to production. A person decides on each release. A staged release to a part of the users first. Stop the releases when the error budget is spent. | S-09 "Embracing Risk" and "Reliable Product Launches"; S-08 capability "continuous delivery"; S-14 FAQ |
| Which service level to promise | type of delivery; the users and the business | No promise. An internal objective. A published objective that is less strict than the internal one. | S-09 "Service Level Objectives" |
| How to approve a change for production | regulation; team size; if agents make changes | A review by a peer that the platform records. An approval from outside the team for a change with a high risk. No manual approval: evidence from the pipeline. | S-08 capability "streamlining change approval"; S-14 "deterministic-pipeline" and "agentic-cd" |
| Which practices of a framework to apply | all risk dimensions | All practices that apply. A selection by risk, cost and feasibility. A target level for each practice of a maturity model. | S-03 pages 8 and 12; S-06 "about"; S-04 page 20 |
| How to treat a dependency without provenance | risk dimension supply chain | Build it from its source after a check of the source. Let the security team approve it. Do not use it. | S-03 task PW.4.1; S-04 page 21; S-02 "draft/dependency-track" |
| How to distribute updates | type of delivery | Through the package ecosystem. Through an own update system that uses a secure update framework. | S-04 pages 27 to 28 |

### 3.4 Where the sources disagree

| Question | Positions | How this recipe handles it | Sources |
|---|---|---|---|
| What does "DevSecOps" cover? | The owner: the shift left of operational, security and quality concerns. The sources that carry the name: the automation of security in each phase of DevOps. | The recipe follows the owner. It takes the operation view and the quality view from the sources of those fields. | S-01 pages 159, 206 and 266; S-04 page 10; S-05; S-08; S-09; S-13 |
| Which SLSA version is the target? | The owner: the highest levels of the draft. The issuer: version 1.2 is approved, and the draft is a working draft that can change or be discarded. The draft has two tracks more than version 1.2. | The recipe follows the owner and names the draft levels as the target. It names the released levels as a second target, and the watch list follows the draft. The owner decides in the review. | S-02 "spec" index, "draft" and "draft/levels" |
| Must each project reach the highest level? | The owner: the highest levels. The frameworks: choose the practices by risk, and not each organization needs the highest maturity level. | The supply chain target follows the owner. For each other target, the risk analysis of the project proposes the level. | S-03 pages 8 and 12; S-06 "about" |
| Does a target of one view measure the aspect? | The owner gives one target, and it measures the supply chain only. The sources give different measures for security, quality and operation. | The recipe keeps one target or more for each view. A project does not show the aspect with the supply chain target alone. | S-02; S-06; S-08 guide "dora-metrics"; S-09 |
| Is a manual approval of a change good? | One position: a maintainer or a second trusted person approves each change. The other position: remove manual approvals from the critical path, and do not add process when production is not stable. | A review by a peer before the merge counts as the approval, and the platform records it. An approval from outside the team is a decision that depends on context. | S-02 v1.2 "source-requirements"; S-04 pages 21 and 27; S-14 "deterministic-pipeline"; S-08 capability "streamlining change approval" |
| Pin the dependencies, or update them all the time? | One position: always use lock files, never a range of versions. A second position: update the dependencies frequently, usually each day or more. A third position: balance the pinning against the delay of updates. | Pin each dependency with its digest, and let a program propose each update as a change that goes through the pipeline. | S-14 "deterministic-pipeline"; S-12 "Keep the build fast"; S-07 "checks.md" check Pinned-Dependencies |
| Which values measure the delivery? | The body of knowledge: four indicators with the mean time to restore service. The research program: five metrics, and the recovery time of a failed deployment replaced the mean time to restore. | The recipe uses the five names of the research program. | S-01 pages 77 and 133; S-08 guide "dora-metrics" |
| Is continuous integration for each project? | One position: teams that perform well integrate the work of each developer each day, and trunk-based development is a required practice for continuous integration. The other position: it is a poor match for a classical open source project, where one or two maintainers work a few hours a week and many persons contribute. | The item is not on level 1. The risk dimension quality and the team size decide. | S-08 capability "trunk-based development"; S-12 "When we should not use Continuous Integration" |

## 4. Checklist

Generic items, valid across the contexts of section 1. One short sentence each. An item that
holds only in some contexts belongs in 3.3; an item for one product belongs in an
implementation skill. There is no fixed number of items: distil until each item earns its
place.

- **Why**: the risk that the item answers, in one line. A practice of the state of the art
  answers a specific result of a risk analysis.
- **View**: one view name of section 1: the view that the item belongs to. Each view has an
  item on level 1: the practices that are basic and not negotiable in that view.
- **Level**: 1, 2 or 3, cumulative. The risk and reward calculation places the item: a good
  return at a low cost in each context is level 1, the basic practices. An item above level 1
  names the risk dimension of section 1 that calls for it, in the form
  `2, [risk dimension]`. The risk of a project on each dimension decides how far the project
  goes past level 1.
- **Admitted by**: `authority` (a fast-lane source states it; name how many agree), `practice`
  (vetted independent sources demonstrate it) or `own rule` (a rule of this kit, with its
  principle).
- **Check**: the cheap, deterministic check that shows the item is met, or `judgement`.
- **Source**: the unit of a source by its identifier where it has one. No text of a source is
  copied here; the evidence record says what the source contributes.

| Id | Item | Why | View | Level | Admitted by | Check | Source |
|---|---|---|---|---|---|---|---|
| C-01 | State the security requirements of the software and keep them current through its life. | A requirement that nobody stated is not built and not tested. | security | 1 | authority (3 agree) | a file with the security requirements is in the repository | S-03 tasks PO.1.1, PO.1.2 and PW.1.2; S-01 pages 50 and 264; S-06 practice "Security Requirements" |
| C-02 | Model the threats to a design as early as possible, and again when the design changes. | A weakness of the design is found only after an attack. | security | 1 | authority (3 agree) | a threat model is in the repository, and it is newer than the last change of the design | S-03 task PW.1.1; S-05 "00b-Threat-modeling"; S-01 page 265 |
| C-03 | Let a qualified person who did not make the design, or an automated process, review the design against the security requirements. | The author of a design does not see its own gaps. | security | 2, security | authority (2 agree) | judgement | S-03 task PW.2.1; S-08 capability "pervasive security" |
| C-04 | Keep secrets out of the source code, scan each commit and the repository for secrets, and revoke a secret that leaked. | A secret in the repository gives an attacker access. | security | 1 | authority (2 agree) | the pipeline has a step that scans for secrets and stops on a finding | S-05 "01a-Secrets-Management"; S-04 page 29 |
| C-05 | Follow a secure coding standard, and check each change with static analysis whose findings are recorded and triaged. | A known type of fault enters the code again and again. | security | 1 | authority (4 agree) | the pipeline has a static analysis step on each change | S-03 tasks PW.5.1 and PW.7.2; S-04 pages 21 and 28; S-01 pages 197 and 325; S-13 chapter 20 |
| C-06 | Scan the dependencies and the built images for known vulnerabilities on each change and on a schedule. | A known vulnerability of a component goes into the product. | security | 1 | authority (3 agree) | the pipeline has a scan step for known vulnerabilities, and a schedule runs it | S-03 task PW.4.4; S-04 pages 29 to 30; S-05 "02d-Software-Composition-Analysis"; S-01 page 103 |
| C-07 | Test the running software for vulnerabilities before a release, and record and triage each issue. | A vulnerability that only shows at run time reaches the users. | security | 2, security | authority (3 agree) | judgement | S-03 tasks PW.8.2 and RV.1.2; S-01 pages 125, 128 and 268; S-05 "02b-Dynamic-Application-Security-Testing" |
| C-08 | Give each person and each program only the access to code, pipelines and environments that the role needs, with strong authentication. | One stolen account can change the code or the release. | security | 1 | authority (3 agree) | the settings of the repository show the roles, and each account has a second factor | S-03 tasks PS.1.1 and PO.5.2; S-04 pages 21 and 23; S-07 README |
| C-09 | Publish how to report a vulnerability, and analyse and answer each report with a planned response. | A reported vulnerability stays open, or the reporter publishes it without a correction. | security | 1 | authority (2 agree) | a security policy file with a contact is in the repository | S-03 tasks RV.1.1, RV.1.3, RV.2.1 and RV.2.2; S-07 "checks.md" check Security-Policy |
| C-10 | Find the root cause of each vulnerability, and change the process so that the cause does not come back. | The same type of vulnerability occurs again. | security | 1 | authority (2 agree) | judgement | S-03 tasks RV.3.1 to RV.3.4; S-01 page 383 |
| C-11 | Integrate the work of each developer into the main line one time each day or more, in small changes. | Work that stays apart for a long time breaks when it is merged. | quality | 2, quality | authority (2 agree) | the age of each open branch is less than one day | S-08 capabilities "continuous integration" and "trunk-based development"; S-12 "Everyone Pushes Commits To the Mainline Every Day"; S-14 "continuous-integration" |
| C-12 | Build and test automatically on each commit, show the result to the team, and keep the feedback fast. | A fault is found late, when its cause is hard to find. | quality | 1 | authority (3 agree) | the pipeline runs on each commit, and its run time is below the limit of the team | S-08 capabilities "continuous integration" and "test automation"; S-01 pages 134 and 155; S-13 chapter 23; S-12 "Keep the build fast" |
| C-13 | When the main build or its tests fail, correct or revert the change before other work. | A broken main line stops the feedback for each other change. | quality | 1 | authority (2 agree) | the main branch has no failed run that is older than the limit of the team | S-08 capabilities "continuous integration" and "trunk-based development"; S-09 "Testing for Reliability"; S-12 "Fix broken builds immediately"; S-14 "continuous-integration" |
| C-14 | Put the automated tests of a change into the same change. | A change of behaviour without a test breaks later, and nobody sees it. | quality | 1 | authority (3 agree) | a change of the code without a change of the tests gets a warning in the review | S-13 chapters 9 and 11; S-08 capability "test automation"; S-01 pages 120 and 171 |
| C-15 | Let a second person review each change before the merge, and record the review in the platform. | One person alone can bring in a defect or malicious code. | quality | 2, quality | authority (4 agree) | the protection of the main branch demands one approval or more | S-04 page 21; S-13 chapter 9; S-08 capability "streamlining change approval"; S-01 page 259 |
| C-16 | Do not accept a test that fails at random: correct it, put it apart or delete it. | Persons stop to trust the tests and go around them. | quality | 1 | authority (2 agree) | the list of tests that were run again after a failure is empty | S-08 capability "test automation"; S-13 chapters 11 and 23; S-14 "deterministic-pipeline" |
| C-17 | Plan the quality with the project: set a threshold for each quality requirement, and report when a result is past it. | Quality is examined only at the end, when a correction costs most. | quality | 2, quality | authority (2 agree) | a file names the thresholds, and the pipeline fails when a result is past one | S-01 pages 208, 211, 213 and 248; S-03 tasks PO.4.1 and PO.4.2 |
| C-18 | Keep all that is necessary to build, configure, test and deploy the software in version control. | An environment or a release cannot be made again, and a change leaves no record. | operation | 1 | authority (3 agree) | a new copy of the repository builds and deploys without a file from a different place | S-08 capabilities "version control" and "continuous integration"; S-01 page 197; S-12 "Put everything in a version controlled mainline"; S-14 "application-configuration" |
| C-19 | Deploy with one automated process that is the same for each environment, and deploy only what passed the pipeline. | A manual step makes an error, and the environments drift apart. | operation | 1 | authority (3 agree) | each deployment in the record was started by the pipeline | S-08 capability "deployment automation"; S-01 pages 158 and 162; S-04 pages 30 to 31; S-14 "single-path-to-production" |
| C-20 | Be able to roll back a deployment on demand, and test the rollback as you test a deployment. | A bad release stays in production while the team looks for a correction. | operation | 2, operative | authority (1), practice | the record shows a rollback test that is newer than the limit of the team | S-09 "Emergency Response"; S-14 "rollback" |
| C-21 | Instrument the software, monitor what the users see, and alert a person only for a problem that needs an action. | A failure is found by the users, or the alerts are ignored. | operation | 2, operative | authority (3 agree) | the monitoring configuration is in the repository, and each alert names an action | S-08 capability "monitoring and observability"; S-09 "Monitoring Distributed Systems"; S-01 pages 161 to 162 |
| C-22 | State a service level objective for a service, with how it is measured and when it is valid. | Nobody knows if the service is reliable enough, and releases are decided by opinion. | operation | 2, operative | authority (2 agree) | a file states the objective, and a dashboard shows the measured value | S-09 "Service Level Objectives" and "Embracing Risk"; S-01 page 158 |
| C-23 | After each significant incident, write a review that blames no person, share it, and follow its actions to the end. | The same failure occurs again, and persons hide incidents. | operation | 1 | authority (1) | each incident in the record has a review with closed actions | S-09 "Postmortem Culture" and "Emergency Response" |
| C-24 | Plan the operation when the development starts: state the operations requirements, the handling of failures and the way users report problems. | The software is built in a way that cannot be operated. | operation | 1 | authority (2 agree) | a file with the operations requirements is in the repository | S-01 pages 156, 159 and 179; S-09 "Release Engineering" |
| C-25 | Release a change to a small part of the users first, and stop the rollout when the monitoring shows a problem. | A fault of a release reaches all users at the same time. | operation | 3, operative | authority (2 agree) | the deployment configuration has stages with a check between them | S-09 "Emergency Response" and "Testing for Reliability"; S-01 pages 160 to 161 |
| C-26 | Rehearse the backup, the recovery and the failover regularly, and write the steps so that each member of the team can do them. | The recovery fails at the time when it is necessary. | operation | 2, operative | authority (3 agree) | the record shows a recovery exercise that is newer than the limit of the team | S-01 page 159; S-09 "Emergency Response"; S-08 capability "version control" |
| C-27 | Keep the source in a source control system that keeps the history of each protected branch and identifies each person who changes it. | A change of the source cannot be traced, or the history is written again. | supply chain | 1 | authority (3 agree) | the main branch refuses a forced push and a deletion | S-02 v1.2 "source-requirements" levels 1 and 2; S-04 page 21; S-07 "checks.md" check Branch-Protection |
| C-28 | Build each release on a hosted build platform, not on the computer of a person. | A computer of a developer that an attacker controls changes the release. | supply chain | 1 | authority (2 agree) | the provenance of the release names a hosted builder | S-02 v1.2 "build-requirements" level 2; S-04 page 17 |
| C-29 | Generate provenance for each released artifact, and give it to the consumers. | A consumer cannot know how and from what an artifact was built. | supply chain | 1 | authority (3 agree) | each release has a provenance file that names the digest of the artifact | S-02 v1.2 "build-requirements" level 1; S-03 task PO.3.3; S-04 pages 22 and 25 |
| C-30 | Use a build platform that signs the provenance, isolates each build and keeps the signing key away from the steps of the build. | A build step forges the provenance, or one build changes a different build. | supply chain | 2, supply chain | authority (2 agree) | the build platform states that it meets the highest build level of the target | S-02 v1.2 "build-requirements" levels 2 and 3; S-04 pages 25 to 26 |
| C-31 | Sign each release, and publish the information that a consumer needs to verify its integrity. | A consumer installs an artifact that was changed after the build. | supply chain | 1 | authority (2 agree) | each release has a signature or a published digest | S-03 task PS.2.1; S-07 "checks.md" check Signed-Releases |
| C-32 | Record each dependency with its exact version and digest, also the indirect ones, and give the inventory with each release. | A build takes a different component than the one that was tested, and nobody can tell which components a release has. | supply chain | 1 | authority (4 agree) | a lock file with digests is in the repository, and each release has an inventory of its components | S-04 pages 13, 20 and 29; S-03 task PS.3.2; S-02 "draft/dependency-track" level 1; S-14 "deterministic-pipeline"; S-06 practice "Secure Build" |
| C-33 | Verify the integrity and the origin of each dependency and each tool before the pipeline uses it. | A changed component or tool runs with the rights of the build. | supply chain | 1 | authority (3 agree) | the pipeline fails when a digest or a signature does not agree | S-03 tasks PO.3.2 and PW.4.1; S-04 pages 21 and 27; S-02 "draft/dependency-track" level 2 |
| C-34 | Take each dependency only through one controlled path that verifies it, records it and blocks each other path. | A build gets a component from a place that nobody examined. | supply chain | not admitted | authority (3 agree) | the build has no access to a package source other than the controlled one | S-02 "draft/dependency-track" levels 2 and 3; S-04 page 21; S-01 page 212 |
| C-35 | Let the source control system enforce the controls of a protected branch, also the agreement of two trusted persons, and record them for each revision. | A person or a program with access changes the source alone and goes around a control. | supply chain | 2, supply chain | authority (1) | the source control system issues an attestation with the highest source level for each revision | S-02 v1.2 "source-requirements" levels 3 and 4 |
| C-36 | Verify the provenance of an artifact against the expected builder and source before it is deployed or used. | Provenance that nobody examines stops no attack. | supply chain | 1 | authority (2 agree) | the deployment fails for an artifact without valid provenance | S-02 v1.2 "verifying-artifacts"; S-04 pages 22, 23 and 29 |
| C-37 | Give each job of the pipeline the least permissions, and do not run the pipeline for a change from outside before a maintainer approves it. | A change from outside takes the secrets of the pipeline. | supply chain | 1 | authority (3 agree) | the pipeline files set the permissions of each job, and runs for changes from outside wait for an approval | S-04 pages 21, 27 and 30; S-05 home page; S-07 "checks.md" checks Token-Permissions and Dangerous-Workflow |
| C-38 | Separate the environments for development, build, test and production, and protect each one. | An attacker goes from a weak environment to the build or to production. | supply chain | 2, supply chain | authority (2 agree) | judgement | S-03 task PO.5.1; S-04 page 21 |
| C-39 | Archive each release with what is necessary to build it again, and make the build repeatable. | A release cannot be examined or made again after an incident. | supply chain | 1 | authority (4 agree) | a second build of the same revision gives the same artifact | S-03 task PS.3.1; S-01 page 197; S-09 "Release Engineering"; S-06 practice "Secure Build"; S-14 "immutable-artifacts" |

**Selection.** The kit recommends; the user decides. The recipe skill leads the owner of the
project through a risk analysis of the project, along the risk dimensions of section 1. It
gives the opinion of the kit and proposes a target level for each dimension. The user picks
the targets and declines single items with a reason. The selection is a Markdown checklist
that is committed in the project, and the recipe skill shows and changes it on request. A
declined item keeps its reason, and a refresh shows the declined items whose source changed.
The distance of a project is the list of adopted items whose check fails.

## 5. Skill set to define

What the recipe skill and its agent wrapper do, and which implementation skills layer two must
work out. Each skill of the set holds the rules of the kit, `rules/evidence-before-action.md`,
and reads a source in the turn in which it uses a value from it. The renderer copies the fields
of the recipe skill into the skill as they are. Thus write them for the reader of the skill,
and do not refer to a section of this specification.

### Recipe skill and agent: devsecops

- **Goal**: A project where operation, security and quality concerns are treated at the
  earliest step, where each change goes through one automated path with records, and where a
  consumer can verify the origin of each artifact up to the target level that the owner of
  the project chose.
- **Reads first**: The contexts of the project: the team size, the type of delivery, the
  operator of the build platform, the contributors, the regulation and the lifetime. Then the
  risk analysis of the project along the five risk dimensions, and the committed selection
  of checklist items, if the project has one.
- **Applies**: The order of the work of the strategy, and the checklist items that the
  selection of the project adopts. It judges each item with its check, and it gives the
  distance of the project as the list of adopted items whose check fails. It stops at a plan:
  it does not change the project before the owner of the project agrees.
- **Delegates**: The pipeline of the hosting platform; the scan for secrets; the static
  analysis; the scan for known vulnerabilities; the generation and the verification of
  provenance; the signing of releases; the inventory of components; the deployment and the
  rollback; the monitoring. An implementation skill provides each one.
- **Stops when**: The checks of all adopted items pass; or a check cannot be made with the
  access that the agent has; or a decision that depends on the context of the project needs a
  person, for example how many persons approve a change or which build platform to use.

### Implementation skills (layer two)

One line per product or tool that needs a skill. A skill holds knowledge and pointers, never a
copy of what the product's own catalog maintains: how and what to query in the catalog; how to
identify trustworthy entries; lighthouse projects, chosen by measurable criteria and dated; how the product works and how to get the work
done; settings as a file from the current documentation; common traps and points to review;
which review tools work with it and how to apply their corrections. A skill that cannot reach
its sources says what it could not verify. A skill writes a setting only from the documentation
that it read in the same turn, not from memory.

| Product or tool | Capability | Checklist items it implements | Helper software it needs |
|---|---|---|---|
| The pipeline of the hosting platform of the project | Build, test and deploy on each commit; permissions of jobs; approval of runs for changes from outside | C-12, C-13, C-19, C-28, C-37 | none |
| The branch protection of the source control system | History, identity, review and enforced controls of a protected branch | C-15, C-27, C-35 | none |
| A scanner for secrets | Scan of commits and of the repository; protection at the push | C-04 | none |
| A static analysis tool for the language of the project | Analysis of each change with triage of the findings | C-05 | none |
| A scanner for known vulnerabilities of dependencies and images | Scan on each change and on a schedule; proposals for updates | C-06, C-32 | none |
| A generator and a verifier of SLSA provenance | Provenance in the format of the SLSA specification; verification against the expected builder and source | C-29, C-30, C-36 | none |
| A tool that signs releases | Signature and digest of each release | C-31 | none |
| A generator of a software bill of materials | Inventory of the components of each release | C-32 | none |
| OpenSSF Scorecard | Measurement of the Scorecard score of a repository | C-08, C-09, C-27, C-31, C-37 | none |
| A dependency ingestion platform | One controlled path for dependencies, as the draft Dependency track describes it | C-33, C-34 | none |
| A monitoring system | Instrumentation, alerts, service level objectives | C-21, C-22 | none |
| A secure update framework | Protected distribution of updates for a project with an own update system | C-31 | none |

## 6. Watch list

| Signal | Where to read it | Cadence |
|---|---|---|
| A new version of the SLSA specification, or a change of the tracks and levels of the working draft | https://slsa.dev/spec/ and https://slsa.dev/spec/draft/ | at each refresh |
| A new version of NIST SP 800-218 | https://csrc.nist.gov/pubs/sp/800/218/final | at each refresh |
| A new version of NIST SP 800-204D | https://csrc.nist.gov/pubs/sp/800/204/d/final | at each refresh |
| A new version of the SWEBOK Guide | https://www.computer.org/education/bodies-of-knowledge/software-engineering | at each refresh |
| A change of the DORA metrics or of the capability pages | https://dora.dev/guides/dora-metrics/ and https://dora.dev/capabilities/ | at each refresh |
| A new version of OWASP SAMM, of the OWASP DevSecOps Guideline or of the OWASP DevSecOps Maturity Model | https://owaspsamm.org/model/ , https://owasp.org/www-project-devsecops-guideline/ and https://owasp.org/www-project-devsecops-maturity-model/ | at each refresh |
| A change of the checks of OpenSSF Scorecard | https://github.com/ossf/scorecard/blob/main/docs/checks.md | at each refresh |
| A change of the practices of MinimumCD | https://minimumcd.org/ | at each refresh |

## 7. Decisions and changes

Dated. A reversed decision stays and is marked superseded. Name the models that made or
suggested a judgement, and the person who reviewed the findings and accepted the recipe.

| Date | Decision or change | Reason | Revisit when |
|---|---|---|---|
| 2026-10-11 | Not verified: the intent of the owner was not asked in the session of phase 1. The lines `meaning` and `result` hold answers that the owner gave on 2026-10-10. The line `not wanted` has no answer. The owner did not name the field and the disciplines. | The owner was not in the session. | The owner reviews section 1. |
| 2026-10-11 | The research found four views: `security`, `quality`, `operation` and `supply chain`. The three concerns of the line `meaning` are each a view. The view `supply chain` comes from the line `result`. The early treatment ("shift left") is not a view: it is the common principle of all four views. | The body of knowledge has a knowledge area for each view, and the target of the owner measures the supply chain only. The main agent of the research, a large language model, made this judgement. | The owner reviews the views. |
| 2026-10-11 | Decision of the owner that is open: which SLSA version the target takes. The specification follows the words of the owner and names the highest levels of the working draft. It names the levels of the approved version 1.2 as a second target. | The issuer says that the draft can change or be discarded. Version 1.2 does not have the Dependency track and the Build Environment track. | The owner reviews the targets; a new version of the SLSA specification. |
| 2026-10-11 | Decision of the owner that is open: item C-34 is necessary for the highest level of the draft Dependency track, but the calculation of risk and reward does not admit it. The answers are in the table "Items" of `vetting.md`. | The answers for a typical project give a score below the admission threshold. The level was not written by hand. | The owner corrects an answer or changes the target. |
| 2026-10-11 | Judgements on the class of a source: S-01 and S-15 have the class `standard`; S-08, S-09 and S-13 have the class `research`. | S-01 is a guide of a professional society. S-15 is a document of a government department. S-08 is a research program that a vendor operates. S-09 and S-13 are books that a publisher of the field printed. The main agent made these judgements. | The owner reviews the sources. |
| 2026-10-11 | Roles of the models: a small model read each source as a reader with web tools only, or with the read tool only for a converted file. A mid-size model did the second reading of the web sources, and a new small model did the second reading of each converted file. The main agent, a large language model, made the judgements on stakeholders, views, contexts, risk dimensions, boundaries, items, the exits of the requirements and the answers of risk and reward. | The procedure asks for the roles. | Not applicable. |
| 2026-10-11 | Not verified: S-11 (ISO/IEC 25010:2023) and S-15 (DoD Enterprise DevSecOps Fundamentals) were not read. No item cites them. | The page and the preview of S-11 gave the error 403 to the reader. The conversion of S-15 gave the error 403 for two addresses. | The owner gives the files, or a refresh can reach them. |
| 2026-10-11 | Not verified: the work folder holds a converted file with the name `S-13.md` from an earlier run. It is not a source of this specification, and no reader of this run read it. The source S-13 of this specification is a web source. | The file was in the folder before this run, and the program did not write it again. | A person removes the file from the work folder. |
| 2026-10-11 | Not verified for S-02: the pages of the levels of version 1.2, of the Source track basics and of the Build Environment track gave the error 404. The reader took the Source levels from the table of the requirements, and reports that the level of each Source requirement is approximate. The reader found only L3 as a name of a Build Environment level. The summary attestation of version 1.2 lists verified levels only to level 3, and the requirements have four levels. | The reader could not reach these pages. | A refresh reads the pages again. |
| 2026-10-11 | Not verified: the wording of the web sources S-02, S-05 to S-10 and S-12 to S-14. The fetch tool of the readers gave a summary of each page, not the text. Thus "must" and "should" in the requirements of these sources can be different in the source. | The readers reported this limit. | A refresh with a tool that gives the text of a page. |
| 2026-10-11 | Not verified: the list of the requirements of S-01 is not complete. The reader reports that it holds the "must" and "should" sentences on the subjects of the aspect, not each one of the 411 pages. The readers read S-02, S-05 to S-10, S-13 and S-14 in part. | The reports of the readers say so. | A refresh, or a finding of a trial. |
| 2026-10-11 | Not done: the standards that the body of knowledge names for the knowledge areas of the views were not read, for example ISO/IEC/IEEE 32675 (DevOps), ISO/IEC/IEEE 12207, ISO/IEC 27001, ISO/IEC/IEEE 29119 and ISO/IEC 20000-1. The regulation of the European Union on cyber resilience was found by a search and was not read. | These standards are paid, and one paid standard (S-11) could not be read from its preview. The time of the run was a limit for the regulation. | The owner gives the files or asks for these sources. |
| 2026-10-11 | Rule for the register of the requirements: a row is written for each requirement that a reader reported with "must", "should", "recommended", "required" or an imperative. A sentence with "may" or "can" only is not a row. A requirement about the product or the format of one issuer has the exit `5`. | "May" gives a permission, not a duty. The main agent made this judgement. | The owner reviews the part "Requirements". |
| 2026-10-11 | A risk dimension `quality` was added to the dimensions that the sources of the name of the aspect give. | The items of the view `quality` above level 1 need a dimension. The main agent made this judgement from S-13 chapter 1 and S-01 page 249. | The owner reviews the risk dimensions. |
| 2026-10-11 | Second reading of the evidence record: the second reading corrected 7 of the 13 rows (S-01, S-03, S-04, S-06, S-08, S-09 and S-12). In these 7 rows, 13 of the 92 sentences of the record were changed: 12 had the result "overstated", and 1 word was changed after a note of the reader. The 6 other rows had no finding (S-02, S-05, S-07, S-10, S-13 and S-14). No location of a statement was wrong. The same corrections were made in 5 rows of the table "Requirements" and in sections 2, 3.4 and 4 of `spec.md`. | The second readers found dropped limits: "in general", "can", "could", a condition, and a practice that the summary gave as a duty. Two sentences of S-07 and one sentence of S-12 could not be compared at the first attempt; a new second reader compared them. | A refresh. |
| 2026-10-11 | Not verified: the second readers of the web sources got quotes and summaries from the fetch tool, not the full text of a page. The names of the sections of S-12 are as the first reader gave them, apart from the two names that the second reader corrected. The second reading compared the evidence record, not each row of the table "Requirements". | The reports of the second readers say so. | A refresh. |
| 2026-10-11 | Difference for the owner: the date of S-01 in section 2 is the date that two readers found on page 1 of the converted file. The row `swebok` of `factory/sota-research/references/seeds.md` has a different date in the cell "Version or date". The row of the seed list was not changed. | Only the owner accepts a row of the seed list. | The owner reviews the row of the seed. |
| 2026-10-11 | For the confirmation of S-12: the date in the cell "Signals" of the row S-12 in `vetting.md` is the date that the program measured on the page. It is different from the date of the article in section 2. The age points of the score use the measured date. | The program takes the newest date that the page gives. | The owner confirms or rejects the source. |
| 2026-10-11 | The identifiers of the requirements have three digits (`R-001`), because the register has 668 rows. | A reader reported each row. | Not applicable. |

## 8. Glossary

Terms that mean different things in the sources. One preferred form per meaning.

| Term | Meaning here | Other meanings in the sources |
|---|---|---|
| DevSecOps | The treatment of operation, security and quality concerns at the earliest step of the work, as the owner states it. | The automation of security in each phase of DevOps (S-01 pages 159, 206 and 266; S-04 page 10). |
| shift left | To do a check or to state a requirement at an earlier step of the work. | Security work that is done earlier (S-03 page 10). Tests that are done earlier (S-01 pages 139 to 140). Continuous integration as the earlier form of an alert in production (S-13 chapter 23). |
| provenance | The record of how, where and from what an artifact was built. | Data about the origin of each component of a release, for example an inventory of components (S-03 task PS.3.2). |
| level | A level of a target of this aspect, with the name of its scale: a build level, a source level, a maturity level. The level of a checklist item is a different thing: 1, 2 or 3. | An integrity level that sets the minimum verification tasks (S-01 page 251). |
| build platform | The hosted system that runs the build and generates the provenance. | A pipeline, a build system (S-04). |
| consumer | A person or a project that installs, runs or depends on an artifact. | Acquirer, end user (S-03; S-04). Ingestor (S-02 "draft/dependency-track"). |
| time to restore | The recovery time of a failed deployment. | Mean time to restore service, mean time to resolve (S-01 pages 77 and 133; S-08 capability "monitoring and observability"). |

## Files beside this specification

- `evidence.md`: for each source a summary of what it contributes, where in the source that
  is, the rows of this specification that it supports, and the date read. The summary is in
  Simplified Technical English and in the words of this kit. A second reader compares each
  line with the source. A quote stays only where the wording itself is the point.
- `vetting.md`: for each independent source the measured signals, the result of the rubric and
  the owner's confirmation; for each item the answers of the risk and reward calculation.
  - The table "Requirements" has one row for each requirement that a source states for a
    stakeholder. Its columns are Id, Requirement, Stakeholder, View, Source and Goes to.
  - The cell "Goes to" has one of these forms: `C-<nn>`, `3.3: <decision>`, `5`,
    `boundary: <name>` or `duplicate: R-<nn>`. A requirement has no other exit.
  - Each checklist item holds a requirement, or its cell "Admitted by" is `own rule`.
- `trial.md`: the record of the trials of the recipe on a project. This file is optional.
  - The table "Trials" has one row for each trial. Its columns are Id, Date, Project, Commit
    of the specification, and Plan. The cell "Plan" holds where the plan is, or `not kept`.
  - The table "Findings" has one row for each finding of the review of a plan. Its columns
    are Id, Trial, Viewpoint, Finding, Route and Status.
  - The viewpoint is one of the viewpoints of the review. The reviewer gives it.
  - The route is `recipe`, `tooling` or `implementation skill`.
  - The status is `open`, `corrected in <revision or commit>` or `declined: <reason>`.
