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
- **Field and disciplines**: software engineering; the disciplines of operations, security and quality
- **Intent of the owner**: the answers of the owner to the questions of phase 1. One line each:
  the words of the owner as a quote, with the date, or `(no answer)`.
  - `meaning`: "DevSecOps is about doing shift left of operational, security, and quality concerns." (2026-10-10)
  - `result`: "achieve SLSA draft highest levels" (2026-10-10)
  - `not wanted`: (no answer)
- **Agreed with the owner on**: 2026-10-11; the field: software engineering; the thing to build: "do the DevSecOps research and generate a skill" (2026-10-10), with the short name `devsecops`

Found by the research, and reviewed by the owner with the other findings. Each line names its
source, or says `(judgement)`. A use case is chosen only when the recipe is applied to a project.

- **Stakeholders**: each group of persons that has an interest in the result or carries a duty
  for it. The research finds them in the body of knowledge of the field and in the sources.
  One line each: a short name, the concerns of the stakeholder for this aspect, and the source.
  - `developers`: the persons who write and change the software; they build security and quality into the code, test their work and keep it easy to change (S-01 pages 101, 102, 107, 264, 266; S-09 page 11)
  - `operations engineers`: the persons who keep the product in operation; they deploy, monitor, respond to incidents and recover (S-01 pages 152, 153; S-07 Introduction)
  - `security specialists`: the security team and the persons who respond to vulnerabilities; they define security requirements, assess risks and examine designs and code (S-01 pages 265, 266; S-09 PO.2.1; S-10 capability pervasive security)
  - `quality engineers`: testers, reviewers and quality assurance staff; they plan and do verification, validation, reviews and measurement (S-01 pages 138, 255, 258; S-10 capability test automation)
  - `maintainers`: the persons who own a repository and its releases and authorize changes; they control access, changes and the release process (S-01 pages 168, 177, 179; S-04 lexicon; S-06)
  - `managers`: senior management, project managers and product owners; they set policy, accept risk, give resources and agree objectives (S-01 pages 159, 162, 251, 265; S-07 Embracing Risk; S-09 PO.2.3)
  - `users`: users, customers, acquirers and consumers of the software and its artifacts; they need a product that is reliable, safe and secure, and proof that an artifact is authentic (S-01 pages 158, 246, 251; S-02 verifying-artifacts; S-09 PS.2.1)
  - `suppliers`: third parties that give components, services or dependencies; their products go into the product and must meet its requirements (S-01 pages 156, 209, 212; S-09 PO.1.3; S-11 CICD-SEC-8)
  - `platform engineers`: the persons who give the build platform, the source control system and the pipeline; they isolate builds, sign provenance and limit permissions (S-01 page 152; S-02 build-requirements; S-15 page 24)
  - `auditors`: regulators, auditors, certification bodies and independent assurance; they need evidence that controls work and that rules are met (S-01 pages 187, 196, 251, 259; S-10 capability pervasive security)
  - `vulnerability reporters`: security researchers and other persons who report a vulnerability; they need a private channel and a response (S-09 RV.1.3; S-14 "Who's a vulnerability reporter")
- **Views**: the points of view that the aspect brings together. A view is a set of concerns
  of the aspect. The research aggregates the concerns of the stakeholders into the views. A
  concern that the owner named in the intent is in a view, or section 7 says why it is not.
  One line each: a short name, what the view is concerned with, the stakeholders whose
  concerns the view holds, and the source. Name the stakeholders in this form, before the
  source: `(stakeholders: [name], [name])`. Use the names of the field "Stakeholders".
  - `operations`: to plan the operation during development and to keep the product in operation: service levels, telemetry, rollback, recovery, incidents and their review (stakeholders: operations engineers, developers, managers, users) (S-01 chapter 6, pages 151 to 164; S-07; S-12)
  - `security`: to build security into each stage: security requirements, threat analysis, automated security analysis, secrets, access, and the response to vulnerabilities (stakeholders: developers, security specialists, managers, vulnerability reporters, users) (S-01 chapter 13, pages 264 to 269; S-09; S-04)
  - `quality`: to plan quality early and to examine it at each step: reviews, automated tests, static analysis, measurable thresholds and measurement (stakeholders: developers, quality engineers, managers, users, auditors) (S-01 chapter 12, pages 246 to 260, and chapter 5, pages 117 to 141; S-08; S-16)
  - `supply-chain`: the integrity of source, dependencies, build and release: protected branches, pinned dependencies, hosted builds, provenance, signatures and bills of materials (stakeholders: maintainers, platform engineers, suppliers, users, auditors) (S-01 pages 103, 192, 197, 212; S-02; S-15)
  - `delivery`: the automated path of a change from the repository to production: version control of all inputs, small changes, automated build and deployment, a secure pipeline and its measures (stakeholders: developers, operations engineers, platform engineers, maintainers) (S-01 pages 101, 103, 162, 180; S-10; S-08; S-15)
- **Contexts**: the values of each dimension that change the strategy. One line each.
  - `delivery form`: a hosted service; a package or a library that other parties install; embedded or client software that the project does not deploy itself (S-01 page 41; S-10 capability continuous delivery; S-08 Continuous Delivery)
  - `organization size`: one maintainer; a small team (25 persons or less); a large organization with separate teams for operations and security (S-01 pages 163, 198; S-04 "Maturity levels"; S-05 about)
  - `openness`: open source with external contributors; closed source (S-01 pages 41, 212; S-04; S-11 CICD-SEC-4)
  - `life cycle`: predictive with phases; iterative or agile; continuous delivery (S-01 pages 102, 103, 209, 225)
  - `pipeline platform`: a hosted platform for source and build; a self-managed platform (S-11 CICD-SEC-7; S-02 build-requirements)
  - `regulation`: no external rule; a contract, a law or a regulator that imposes standards and independent assurance (S-01 pages 124, 187, 250, 251)
  - `product age`: a new product; an existing product without the practices (S-10 capability test automation; S-08 Static Analysis)
- **Risk dimensions**: the dimensions on which the risk of a project differs for this aspect.
  One line each: the name, the question that finds it out, the opinion of the kit on the
  answer, and the source.
  - `criticality`: Which harm does a failure or a compromise of the product cause to persons, data or money? Opinion: with harm to persons or large loss, go past level 1 in the views `security` and `quality`, and use independent assurance. (S-01 pages 250, 251, 257)
  - `availability`: Which interruption of the service do the users accept? Opinion: if users rely on the service continuously, go past level 1 in the view `operations`. (S-07 Embracing Risk; S-01 page 158)
  - `distribution`: How many other parties install, build on or redistribute the artifacts of the project? Opinion: with many consistent users or redistribution, go past level 1 in the view `supply-chain`. (S-04 "Maturity levels"; S-02 build-track-basics)
  - `third-party`: How much code and how many services of third parties does the product and its pipeline use? Opinion: with many dependencies or integrations, go past level 1 in the views `supply-chain` and `delivery`. (S-01 pages 103, 212; S-11 CICD-SEC-3, CICD-SEC-8)
  - `regulatory`: Does a law, a contract or a regulator impose rules on the product or on its development? Opinion: if yes, the imposed rules decide the level, and evidence must be kept. (S-01 pages 124, 187, 394)
- **Boundaries**: what each neighbouring aspect owns, and what this aspect keeps. One line each.
  - `requirements`: owns elicitation, specification, priority and tracing of requirements; this aspect keeps that security and quality requirements exist and have measurable thresholds (S-01 chapter 1, pages 43 to 66)
  - `architecture`: owns the structure and the design decisions of the software, also for resilience and secure defaults; this aspect keeps the examination of a design for threats and for operation (S-01 chapters 2 and 3, pages 67 to 98)
  - `management`: owns planning, estimates, roles, training, acquisition contracts and economic decisions; this aspect keeps the assessment of risk and the use of measures (S-01 chapters 9, 10 and 15)
  - `professional-practice`: owns law, licences, ethics, privacy rules and communication; this aspect keeps nothing of it (S-01 chapter 14, pages 274 to 287)
  - `service-operation`: owns the daily operation of a service: capacity plans, on-call staffing, agreements with customers and business planning; this aspect keeps what development must prepare for operation (S-01 pages 157, 158; S-07 Service Best Practices)
  - `platform-provider`: owns the internals of a build platform, a source control system or a package ecosystem; this aspect keeps the selection and the configuration of the platform (S-02 build-requirements, source-requirements; S-03 build-env-track-basics)
  - `maintenance`: owns the maintenance process, its cost and technical debt; this aspect keeps security and quality during maintenance (S-01 chapter 7, pages 167 to 184)
  - `domain`: owns the special techniques of one application domain or system type; this aspect keeps only the generic practices (S-01 pages 41, 140 to 144, 269)
  - `foundations`: owns the knowledge of computing, mathematics and engineering that an engineer needs; this aspect keeps nothing of it (S-01 chapters 16 to 18, pages 312 to 386)
- **Targets**: the measurable results that a project reaches when it applies the recipe. The
  targets come from the sources in the research; the owner can name one in the intent. If
  the sources give no target, write `(none found)` in place of the lines.
  - `SLSA build level`: Build L0 to L3 (L1 provenance exists, L2 hosted platform with signed provenance, L3 hardened build); a verifier examines the provenance of an artifact against its trusted builders and its expectations (S-02 build-track-basics, verifying-artifacts)
  - `SLSA source level`: Source L1 to L4 (L1 version controlled, L2 history and provenance, L3 continuous technical controls, L4 two-party review); a consumer examines the verification summary that the source control system issues for a revision (S-02 source-requirements, verifying-source)
  - `SLSA draft tracks`: the target of the owner, "SLSA draft highest levels"; the working draft has four tracks with these highest levels: Build L3, Source L4, Build Environment L3 and Dependency L3; the approved version defines only the tracks Build and Source; the method is the verification of attestations (S-03 tracks, build-env-track-basics, dependency-track; S-02 tracks)
  - `baseline level`: levels 1 to 3 of a security baseline for open source projects, by the number of maintainers and users; an assessment of the project against the controls of the level, by a person or by a program (S-04 "Maturity levels", maintainers page)
  - `repository score`: 0 to 10 for each of 20 automated checks of a repository, and a weighted mean; a program computes it (S-06 checks, README)
  - `best practices badge`: the levels passing, silver and gold; the project answers each criterion with evidence or a reason (S-16 criteria index)
  - `security maturity`: maturity levels 1 to 3 for a security practice of a model with 15 practices, read for one practice; a self-assessment with a list of questions for each activity (S-05 model, model/governance/strategy-and-metrics, assessment)
  - `delivery measures`: change lead time, deployment frequency, failed deployment recovery time, change fail rate and deployment rework rate, measured for one application or service; the source gives no levels (S-10 guide to the delivery metrics)
  - `service level`: the share of successful requests in a period against an objective, and the error budget that remains (S-07 Embracing Risk, Service Level Objectives)

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
| S-01 | Guide to the Software Engineering Body of Knowledge (SWEBOK Guide) | IEEE Computer Society | V4.0a | standard | IEEE copyright; free for personal and academic use with a citation (page 5) | full | all | https://www.computer.org/education/bodies-of-knowledge/software-engineering |
| S-02 | SLSA specification, approved version | SLSA project (The Linux Foundation, OpenSSF) | v1.2 | foundation | Community Specification License 1.0 | part | supply-chain | https://slsa.dev/spec/v1.2/ |
| S-03 | SLSA specification, working draft | SLSA project (The Linux Foundation, OpenSSF) | working draft, read 2026-10-11 | foundation | Community Specification License 1.0 | part | supply-chain | https://slsa.dev/spec/draft/ |
| S-04 | Open Source Project Security Baseline | OpenSSF Security Baseline SIG | v2026.08.28 | foundation | not found | part | supply-chain, security | https://baseline.openssf.org/versions/2026-08-28.html |
| S-05 | OWASP Software Assurance Maturity Model (SAMM) | OWASP | v2 | foundation | CC BY-SA 4.0 | part | security | https://owaspsamm.org/model/ |
| S-06 | OpenSSF Scorecard, documentation of the checks | OpenSSF | main branch, read 2026-10-11 | foundation | not found | part | supply-chain, security | https://github.com/ossf/scorecard/blob/main/docs/checks.md |
| S-07 | Site Reliability Engineering (book, web edition) | O'Reilly Media; Google | 2017 | research | CC BY-NC-ND 4.0 | part | operations, delivery | https://sre.google/sre-book/table-of-contents/ |
| S-08 | Software Engineering at Google (book, web edition) | not found on the pages; published at abseil.io | web edition, read 2026-10-11 | research | CC BY-NC-ND 4.0 | part | quality, delivery | https://abseil.io/resources/swe-book/html/toc.html |
| S-09 | NIST SP 800-218, Secure Software Development Framework (SSDF) | NIST | Version 1.1, 2022-02 | standard | not subject to copyright in the United States (page 3) | full | security | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf |
| S-10 | DORA, guide to the software delivery metrics and catalogue of capabilities | DORA (Google Cloud) | guide updated 2026-01-05 | independent | CC BY 4.0 | part | delivery, quality | https://dora.dev/guides/dora-metrics-four-keys/ |
| S-11 | OWASP Top 10 CI/CD Security Risks | OWASP Foundation | no version found, read 2026-10-11 | foundation | not found | full | security, supply-chain | https://owasp.org/www-project-top-10-ci-cd-security-risks/ |
| S-12 | AWS Well-Architected Framework, Operational Excellence Pillar | Amazon Web Services | 2024-11-06 | vendor | not found | part | operations | https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html |
| S-13 | IEEE Std 2675-2021, IEEE Standard for DevOps | IEEE Standards Association | 2021-04-16 | standard | paid; read from the public page | part | delivery | https://standards.ieee.org/ieee/2675/6830/ |
| S-14 | Guide to implementing a coordinated vulnerability disclosure process for open source projects | OpenSSF Vulnerability Disclosures Working Group | no version found, read 2026-10-11 | foundation | not found | part | security | https://oss-vulnerability-guide.openssf.org/maintainer-guide.html |
| S-15 | NIST SP 800-204D, Strategies for the Integration of Software Supply Chain Security in DevSecOps CI/CD Pipelines | NIST | 2024-02 | standard | not subject to copyright in the United States (page 3) | full | supply-chain, delivery | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204D.pdf |
| S-16 | OpenSSF Best Practices Badge, criteria | OpenSSF (LF Projects) | no version found, read 2026-10-11 | foundation | not found | part | quality, security | https://www.bestpractices.dev/en/criteria/0 |
| S-17 | ISO/IEC 25010, Product quality model | ISO/IEC | 2023 | standard | paid | no | quality | https://www.iso.org/standard/78176.html |

## 3. Strategy

High level, for the agent that runs the work. One page.

### 3.1 Goals

- A concern of operation, security or quality is examined at the earliest step where it can be found: in the requirements, in the design, on each change, and before each release.
- Each change goes through one automated path that reviews, tests, analyses, builds and deploys it, and the path itself is protected.
- A user can verify where a release came from and what is in it.
- The product is ready for operation before it is in production: it can be observed, rolled back and recovered.
- Each incident and each vulnerability improves the process.
- The project goes past the basic level only where its risk calls for it.

### 3.2 Order of the work

1. Find the contexts and the risk of the project on each risk dimension: they decide the target level of each view and the decisions that follow.
2. Put all inputs of build, test, deployment and configuration into version control, and protect the primary branch and the access: each later control relies on this base.
3. Automate the build, and run review, tests and static analysis on each change: this gives the path that carries all other checks.
4. Add the security checks to the same path: secrets, dependencies, security analysis, and the minimum permissions of the pipeline.
5. Make the release verifiable: hosted build, pinned dependencies, provenance, signatures and a bill of materials. Then go up the levels of the supply chain target by risk.
6. Prepare the operation before the first production release: objectives, telemetry, rollback, recovery and the incident procedure, with a readiness review.
7. Close the loops: reviews after incidents, the response to vulnerabilities with root cause analysis, and measures that guide improvement.

### 3.3 Decisions that depend on context

| Decision | Depends on | Options | Sources |
|---|---|---|---|
| Release pace | delivery form; availability; the state of the error budget | on demand behind flags; a fixed release schedule; release branches with selected corrections; a stop of changes when the budget is used | S-07 Release Engineering; S-08 Continuous Delivery; S-15 page 31 |
| Automatic deployment | delivery form; criticality | each change deploys automatically; a person approves the deployment to production | S-10 capability continuous delivery; S-11 CICD-SEC-1 |
| Depth of verification | criticality; regulatory; the cost of quality | the basic tests and analysis; more techniques, coverage goals and a design review by the integrity level of the product | S-01 pages 249, 257; S-09 PW.7.1, PW.8.1; S-16 test_statement_coverage80 |
| Independence of assurance | criticality; regulatory | review by a peer; a separate quality or security team; assurance or audit by an independent party | S-01 pages 196, 255, 258, 259; S-16 security_review |
| SLSA level for each track | distribution; third-party; pipeline platform | Build L1, L2 or L3; Source L1 to L4; the draft tracks for dependencies and for the build environment when they are approved | S-02 build-requirements, source-requirements; S-03 dependency-track, build-env-track-basics |
| Form of change control | life cycle; regulatory; organization size | automated checks and review on each change; a formal change request with a control board and status accounting | S-01 pages 59, 179, 185, 194; S-15 page 21 |
| Who operates the product | organization size | the developers operate the product; a separate operations or reliability team with a handover and shared duties | S-01 page 163; S-07 Service Best Practices, Evolving SRE Engagement Model; S-10 capability deployment automation |
| Service level objective | availability; the users and their alternatives | a loose first target that becomes tighter; an internal target that is tighter than the published one | S-07 Service Level Objectives, Embracing Risk |
| Embargo of a vulnerability | openness; the ecosystem of vendors that redistribute the product | disclosure without an embargo list; a time-limited embargo with early notice to a list of providers | S-14 response steps 3 and 8 |
| Tests before and after the merge | the duration and the reliability of the test suites | all tests before the merge; only fast and reliable tests before the merge, and the others after it | S-08 Continuous Integration, Testing Overview; S-10 capability test automation |
| Adoption for an existing product | product age | a baseline of the existing findings, and the rules apply to new and changed code; tests for the functions of high value first | S-08 Static Analysis; S-10 capability test automation |
| Applicable standards | regulatory; the application domain | no external standard; the standards that a contract, a law or a regulator imposes, with evidence of conformance | S-01 pages 120, 249, 382, 394; S-15 page 20 |

### 3.4 Where the sources disagree

| Question | Positions | How this recipe handles it | Sources |
|---|---|---|---|
| What the name of the aspect means | The owner means the shift left of operational, security and quality concerns. The sources that carry the name mean the integration of development, security and operations in one team and one pipeline, with security as the added part; they do not treat quality and operation as equal parts. | The recipe follows the owner. The concerns of operation and of quality come from the sources of their own fields, and each is a view. | S-01 pages 206, 266; S-15 page 10; S-07; S-08 |
| What "SLSA draft highest levels" asks for | The approved version defines the tracks Build (to L3) and Source (to L4). The working draft adds the tracks Build Environment (to L3) and Dependency (to L3), and says that it can be changed, replaced or discarded. One page of the draft calls the Source track new; the index page says that the approved version defines it. | The checklist uses the approved tracks. The draft tracks are a target and an option of the decision "SLSA level for each track". The owner decides if a project aims at draft levels. | S-02 tracks; S-03 index, whats-new, dependency-track, build-env-track-basics |
| Fixed levels or a selection by risk | One source says that its practices are not a checklist, have no priority, and are selected by risk. Other sources give fixed levels with mandatory controls. | Level 1 holds the practices that are basic in each context. Above it, the risk of the project on a named dimension decides. | S-09 pages 8, 12; S-04; S-16 |
| Speed against stability | One source finds that speed and stability go together for most teams. One source uses an error budget to slow or stop releases for reliability. | The recipe asks for small changes and automation first. The error budget is an item above level 1 for services with a high need of availability. | S-10 guide to the delivery metrics; S-07 Embracing Risk |
| A number for test coverage | One source requires 80 percent and then 90 percent statement coverage for its higher levels. Other sources warn that coverage and metrics become goals that are gamed. | The checklist has no coverage number. Coverage goals are an option of the decision "Depth of verification". | S-16 test_statement_coverage80, test_statement_coverage90; S-08 Testing Overview; S-10 guide to the delivery metrics |
| How many persons review a change | The sources ask for one reviewer who is not the author, for two trusted persons at the highest source level, or for a review of half of the changes at least. | The item asks for one person who is not the author. Two-party review is the top level of the decision "SLSA level for each track". | S-08 Code Review; S-04 OSPS-QA-07.01; S-02 source-requirements; S-16 two_person_review; S-15 page 21 |
| The times for the response to a vulnerability | The sources give "ideally 1 to 2 days" and 14 days for the first response, and 60 days for a correction, or they ask only for documented times. | The items ask for documented times. The project sets the values. | S-14 response step 1; S-16 vulnerability_report_response, vulnerabilities_fixed_60_days; S-04 OSPS-VM-01.01 |
| Online keys for signing | One source says "should not" in its text and "must not" in its appendix for online keys in a trusted role. | This is knowledge of one framework. It goes to an implementation skill. | S-15 pages 28, 38 |

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
| C-01 | The operation of the product is planned during development: how it is deployed, updated, supported and recovered, and how users report problems. | Risk: a product goes to production and no person can keep it in operation or correct it. | operations | 1 | authority (3) | a document of the project names the deployment, the support period and the channel for problem reports | S-01 page 156; S-12 OPS07-BP06; S-04 OSPS-DO-02.01 |
| C-02 | Service level objectives are defined in terms that users see, each with its measurement. | Risk: no person can tell if the service is sufficiently reliable. | operations | 2, availability | authority (3) | a file of the project lists each objective with its indicator and its period | S-07 Service Level Objectives; S-01 page 158; S-12 OPS04-BP01 |
| C-03 | The product gives telemetry, and each alert needs an action and has an owner and a procedure. | Risk: users find a failure before the team does, and alerts without an action hide the real ones. | operations | 2, availability | authority (3) | each alert rule names an owner and links to a procedure | S-07 Monitoring Distributed Systems; S-01 page 162; S-12 OPS08-BP04, OPS10-BP02; S-10 capability monitoring and observability |
| C-04 | Each change to production can be rolled back, and the rollback is tested. | Risk: a failed change stays in production because the way back is not known or does not work. | operations | 2, availability | authority (3) | the record of the last rollback test has a date | S-01 page 160; S-07 Reliable Product Launches; S-12 OPS06-BP01, OPS06-BP04 |
| C-05 | A change goes to production in stages, with a check between two stages. | Risk: a defect reaches all users at the same time. | operations | 2, availability | authority (3) | the deployment configuration has two stages or more, with a check between them | S-07 Service Best Practices; S-01 page 160; S-12 OPS06-BP03 |
| C-06 | Backup, recovery and failover are tested at regular intervals. | Risk: the recovery fails at the moment it is necessary. | operations | 2, availability | authority (2) | the record of the last recovery test has a date | S-01 page 159; S-07 Emergency Response; S-10 capability version control |
| C-07 | After each significant incident, a written review without blame finds the causes, and its actions are tracked to completion. | Risk: the same incident occurs again. | operations | 1 | authority (3) | each incident record links to a review and to its actions | S-01 page 161; S-07 Postmortem Culture; S-12 OPS11-BP02 |
| C-08 | An incident procedure names the roles, the escalation path and the communication before an incident occurs. | Risk: the response to an incident is slow and not coordinated. | operations | 2, availability | authority (3) | the procedure is in the repository and names a role for command and a role for communication | S-07 Managing Incidents; S-12 OPS10-BP01, OPS10-BP04; S-01 page 159 |
| C-09 | A review of operational readiness, with a checklist, is done before the first release to production. | Risk: gaps in monitoring, capacity or recovery are found only in production. | operations | 2, availability | authority (3) | the completed checklist of the review is in the records of the release | S-07 Reliable Product Launches; S-12 OPS07-BP02; S-01 page 158 |
| C-10 | An error budget that comes from the objective decides when changes stop. | Risk: the pace of releases uses up the reliability that users need. | operations | not admitted | authority (1) | a written policy tells what occurs when the budget is used | S-07 Embracing Risk, Service Best Practices |
| C-11 | The security requirements and the security risks of the product are identified at the start and kept current. | Risk: security is added late, at a high cost, or not at all. | security | 1 | authority (3) | a dated document lists the security requirements and the assessed risks | S-01 pages 208, 264; S-09 PO.1.2, PW.1.2; S-04 OSPS-SA-03.01 |
| C-12 | The design is examined for threats before the implementation, for the critical paths at least. | Risk: a weakness of the design cannot be corrected by code. | security | 2, criticality | authority (3) | a threat model with a date exists for the current design | S-09 PW.1.1, PW.2.1; S-04 OSPS-SA-03.02; S-01 page 265; S-10 capability pervasive security |
| C-13 | Automated security analysis of the code and of the dependencies runs on each change, and a finding above a set threshold blocks the change. | Risk: a vulnerability goes into a release because no check examined the change. | security | 1 | authority (5) | the pipeline configuration has a security analysis step that can fail the change | S-01 page 268; S-09 PW.7.2, PO.4.1; S-04 OSPS-VM-05.03, OSPS-VM-06.02; S-15 page 28; S-06 check SAST; S-10 capability pervasive security |
| C-14 | No secret is in version control, and secrets are scanned for, limited in scope and rotated. | Risk: a leaked credential gives an attacker the access of the project. | security | 1 | authority (4) | a secret scan of the repository and of its history finds nothing | S-04 OSPS-BR-07.01; S-11 CICD-SEC-6; S-15 page 29; S-16 no_leaked_credentials |
| C-15 | A published security policy tells how to report a vulnerability in private, who gets the report and when a response comes. | Risk: a person who finds a vulnerability cannot report it safely, and it becomes public without a correction. | security | 1 | authority (5) | the security policy file exists and names a private channel and a response time | S-04 OSPS-VM-01.01, OSPS-VM-02.01, OSPS-VM-03.01; S-09 RV.1.3; S-14 "Set up the vulnerability management infrastructure"; S-16 vulnerability_report_process; S-06 check Security-Policy |
| C-16 | Known vulnerabilities of the product and of its dependencies are monitored and corrected by risk in documented times. | Risk: a known vulnerability stays in the product and is exploited. | security | 1 | authority (5) | a scan for known vulnerabilities shows none that is older than the documented time | S-09 RV.1.1, RV.2.2; S-01 page 268; S-04 OSPS-VM-05.01; S-16 vulnerabilities_fixed_60_days; S-06 check Vulnerabilities |
| C-17 | The root cause of each vulnerability is analysed, and the development process is reviewed and, where applicable, updated. | Risk: vulnerabilities of the same type come back. | security | 2, criticality | authority (1) | judgement | S-09 RV.3.1, RV.3.4 |
| C-18 | Access to the repository and to the pipeline uses multi-factor authentication and least privilege, and it is reviewed. | Risk: one stolen or forgotten account can change the code or the releases. | security | 1 | authority (4) | the settings of the repository host show enforced multi-factor authentication and no administrator without a need | S-04 OSPS-AC-01.01, OSPS-AC-02.01; S-11 CICD-SEC-2; S-09 PS.1.1; S-15 page 21 |
| C-19 | Dynamic security tests, such as fuzzing or penetration tests, are done by the risk of the product, with authorization. | Risk: weaknesses that only show at run time stay hidden. | security | 2, criticality | authority (4) | the record of the last dynamic security test has a date | S-01 page 268; S-09 PW.8.2; S-06 check Fuzzing; S-16 dynamic_analysis |
| C-20 | A person who is not the author reviews each change before the merge. | Risk: one person can bring a defect or malicious code into the product without a second look. | quality | 2, distribution | authority (7) | the branch rule requires one approval that is not from the author | S-08 Code Review; S-04 OSPS-QA-07.01; S-15 page 21; S-02 source-requirements; S-07 Release Engineering; S-01 page 259; S-06 check Code-Review; S-16 two_person_review |
| C-21 | Automated tests run on each change before the merge, and a failed test is corrected before other work. | Risk: a defect is found late, when its correction costs much more. | quality | 1 | authority (4) | the branch rule requires a passed test run of the pipeline | S-08 Testing Overview, Continuous Integration; S-04 OSPS-QA-06.01; S-01 page 155; S-16 test; S-10 capability continuous integration |
| C-22 | New and changed behaviour comes with automated tests, and each defect that is found gets a test. | Risk: behaviour without a test breaks later and no person sees it. | quality | 1 | authority (4) | a written test policy exists, and the recent changes of behaviour include tests | S-08 Testing Overview; S-04 OSPS-QA-06.03; S-16 test_policy; S-01 page 257; S-10 capability test automation |
| C-23 | Quality is planned at the start, and each quality requirement has a measurable threshold that the stakeholders agreed. | Risk: no person can show that the product is sufficiently good, and quality is negotiated at the end. | quality | 2, criticality | authority (1) | the quality requirements list a threshold for each one | S-01 pages 50, 211, 248 |
| C-24 | Compiler warnings, linters and static analysis with few false positives are part of the work on each change. | Risk: defects that a tool can find reach review, tests or production. | quality | 1 | authority (5) | the pipeline runs a linter or a static analysis step, and warnings fail the build | S-08 Static Analysis; S-16 warnings, static_analysis; S-09 PW.5.1, PW.6.2; S-15 page 21; S-01 page 325 |
| C-26 | Quality data, such as defects and test results, are collected, analysed and used for decisions. | Risk: decisions on quality rely on opinion. | quality | 2, criticality | authority (2) | judgement | S-01 pages 213, 254, 376; S-12 OPS09-BP03 |
| C-27 | Dependencies are declared, pinned to versions with integrity hashes, and obtained with standard tooling. | Risk: a build takes a changed or malicious dependency and no person sees it. | supply-chain | 1 | authority (6) | a lock file with hashes is committed, and the build uses it | S-04 OSPS-QA-02.01, OSPS-BR-05.01; S-03 dependency-track; S-11 CICD-SEC-3; S-06 check Pinned-Dependencies; S-01 page 103; S-15 page 21 |
| C-28 | Releases come from a documented, scripted build on a hosted build platform, not from the computer of a developer. | Risk: a release cannot be made again, or a compromised computer changes it. | supply-chain | 1 | authority (5) | the release artifacts come from a run of the build platform | S-02 build-requirements; S-15 pages 17, 25; S-01 page 197; S-04 OSPS-DO-07.01; S-16 build |
| C-29 | Each release artifact has provenance that identifies the artifact by its digest and tells how it was built, signed by the build platform. | Risk: a user cannot tell if an artifact came from the official source and build. | supply-chain | 2, distribution | authority (3) | a provenance attestation is published with each artifact, and its signature verifies | S-02 build-requirements, distributing-provenance; S-15 pages 25, 26; S-11 CICD-SEC-9 |
| C-30 | Each release has a unique version and release notes, and is signed or listed with hashes in a signed manifest that users can verify. | Risk: a user installs a changed or a wrong release. | supply-chain | 2, distribution | authority (6) | the last release has a signature or a signed list of hashes, and the documentation tells how to verify it | S-04 OSPS-BR-06.01, OSPS-BR-02.01, OSPS-DO-03.01; S-09 PS.2.1; S-16 version_unique, delivery_mitm; S-06 check Signed-Releases; S-01 page 198; S-15 page 23 |
| C-31 | A bill of materials that lists all components, also transitive ones, is made for each release and given to users. | Risk: no person knows if a vulnerable component is in a release. | supply-chain | 2, distribution | authority (6) | the last release has a bill of materials as a release asset | S-01 pages 192, 197; S-04 OSPS-QA-02.02; S-15 page 13; S-09 PS.3.2; S-06 check SBOM; S-03 dependency-track |
| C-32 | The primary branch is protected: no direct commit, no forced push, no deletion, and its history is kept. | Risk: the source changes without a trace or without a review. | supply-chain | 1 | authority (5) | the rule of the primary branch blocks direct pushes, forced pushes and deletion | S-04 OSPS-AC-03.01, OSPS-AC-03.02; S-02 source-requirements; S-11 CICD-SEC-1; S-06 check Branch-Protection; S-16 repo_track |
| C-33 | The provenance and the signatures of artifacts and dependencies are verified against expectations before use or deployment. | Risk: provenance that no person verifies protects no person. | supply-chain | 2, third-party | authority (3) | the build or the deployment has a verification step that can fail | S-02 verifying-artifacts; S-15 pages 22, 29; S-03 dependency-track |
| C-34 | The release build is isolated: a new environment for each build, and provenance that the build cannot forge. | Risk: one build, or a person with access to the build, changes a different build or its provenance. | supply-chain | not admitted | authority (2) | the documentation of the build platform states the isolation that the project uses | S-02 build-requirements; S-15 page 25 |
| C-35 | No generated executable and no binary that cannot be reviewed is in version control. | Risk: code that no person can review goes into the product. | supply-chain | 1 | authority (2) | a scan of the repository finds no executable binary file | S-04 OSPS-QA-05.01, OSPS-QA-05.02; S-06 check Binary-Artifacts |
| C-36 | A new dependency or third party is examined before adoption: its maintenance, its licence, its known vulnerabilities and its access. | Risk: the product takes over the defects, the legal problems and the access of a third party. | supply-chain | 1 | authority (6) | the documentation tells how dependencies are selected, and a record exists for the last new dependency | S-01 pages 103, 212; S-09 PW.4.1, PW.4.4; S-08 Dependency Management; S-15 pages 21, 29; S-11 CICD-SEC-8; S-04 OSPS-DO-06.01 |
| C-37 | All that is necessary to build, test, deploy and configure the product is in version control. | Risk: an environment cannot be made again, and a change has no record. | delivery | 1 | authority (5) | a build and a deployment from a new copy of the repository are successful | S-01 pages 158, 179; S-07 Release Engineering; S-12 OPS05-BP01; S-08 Continuous Integration; S-15 page 31; S-10 capability version control |
| C-38 | The build and the deployment are automated, and the same process deploys to each environment. | Risk: manual steps cause errors, and production is different from what was tested. | delivery | 1 | authority (4) | a deployment needs no manual step other than an approval | S-01 page 162; S-12 OPS05-BP10; S-15 page 24; S-07 Release Engineering; S-10 capability deployment automation |
| C-39 | Changes are small and go into the main line frequently. | Risk: a large change hides defects and is hard to review, test and roll back. | delivery | 1 | authority (3) | the age of the oldest open branch is below the limit that the project sets | S-08 Continuous Delivery; S-12 OPS05-BP09; S-01 page 161; S-10 capability continuous integration |
| C-40 | The pipeline runs code that is not trusted without secrets and privileges, and each job has the minimum permissions. | Risk: a change from an external person takes the secrets or the release rights of the pipeline. | delivery | 1 | authority (5) | the pipeline configuration sets read-only permissions by default, and jobs for external changes get no secret | S-04 OSPS-BR-01.03, OSPS-AC-04.01; S-11 CICD-SEC-4, CICD-SEC-5; S-15 page 27; S-09 PO.5.1; S-06 check Token-Permissions |
| C-41 | The delivery of one product is measured: lead time, deployment frequency, failed changes and recovery time. The measures are not goals. | Risk: the team does not know if its delivery improves, or it games a number. | delivery | not admitted | authority (1) | judgement | S-01 pages 133, 381; S-10 guide to the delivery metrics |
| C-42 | The artifact that was tested is the artifact that is deployed; it is not built again between environments. | Risk: what runs in production is not what was tested. | delivery | 2, criticality | authority (2) | the digest of the deployed artifact is the digest of the tested artifact | S-08 Continuous Integration; S-11 CICD-SEC-1; S-10 capability deployment automation |
| C-43 | The activity in the repository and in the pipeline is logged, kept in a central place and monitored. | Risk: an attack on the pipeline is not found and cannot be examined afterward. | delivery | 2, third-party | authority (3) | the audit log of the repository host and of the pipeline is on and exported | S-11 CICD-SEC-10; S-15 page 21; S-09 PO.3.3 |

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

- **Goal**: A project examines its concerns of operation, security and quality at the earliest possible step. Each change goes through one protected, automated path of review, test, analysis, build and deployment. A user can verify each release. The project meets the checklist items of the target level that its owner selected for each view.
- **Reads first**: The contexts of the project: the delivery form, the size of the organization, open or closed source, the life cycle, the pipeline platform, the regulation and the age of the product. Then the risk of the project on each risk dimension: criticality, availability, distribution, third-party and regulatory. Then the selection of the project, if one is committed, with the declined items and their reasons.
- **Applies**: The order of the work: first the base in version control and access, then the automated path with review, tests and analysis, then the security checks, then the verifiable release, then the readiness for operation, then the loops of learning. It judges each checklist item of the selected levels with the check of the item, and reports the adopted items whose check fails. It shows the result as a plan and stops before it changes the project.
- **Delegates**: The configuration of the build platform and of the source control system. The generation and the verification of build provenance. The signing of releases. The generation of a bill of materials. The scan for secrets, for known vulnerabilities and for weaknesses of the code. The automated assessment of a repository against a baseline. The monitoring and the alert rules of a service. Each one is provided by an implementation skill for the product that the project uses.
- **Stops when**: Each adopted item of the selected levels passes its check. Or an item is blocked by a platform that cannot give the control. Or a person must decide: the target level of a view, the pace of releases, the depth of verification, the independence of assurance, the supply chain level for each track, the form of change control, who operates the product, the service level objective, the embargo of a vulnerability, or the standards that apply.

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
| The hosted source and build platform of the project (for example GitHub or GitLab, as S-02 and S-06 name them) | branch rules, access, pipeline permissions, secret scan, audit log | C-14, C-18, C-20, C-32, C-40, C-43 | the command line client of the platform |
| SLSA build provenance in the in-toto attestation format, and a verifier for it (S-02) | make, publish and verify provenance | C-29, C-33, C-34 | a provenance generator of the build platform; a verifier program |
| Sigstore (S-02, S-11) | signatures of artifacts and a transparency log | C-29, C-30 | the client of the signing service |
| The Update Framework (S-15) | secure updates with several keys and threshold trust | C-30 | a client library of the framework |
| SPDX and CycloneDX (S-04, S-06) | formats for a bill of materials | C-31 | a generator for the package manager of the project |
| OSV and its scanner (S-06, S-14) | known vulnerabilities of dependencies; publication of a vulnerability record | C-13, C-16 | the scanner program |
| OpenSSF Scorecard (S-06) | automated checks of a repository with a score | C-32, C-35, C-40 | the program or its pipeline action |
| A tool that updates dependencies, such as Dependabot or Renovate (S-06) | update requests for dependencies | C-16, C-27 | the configuration file of the tool |
| An assessment tool for the security baseline, with a machine-readable security file (S-04) | automated assessment against the baseline | C-15, C-18 | the plugin and the security information file |
| A fuzzing service, such as OSS-Fuzz or ClusterFuzzLite (S-06) | dynamic tests | C-19 | the build integration of the service |
| A statement of exploitability (VEX) (S-04) | tells users which vulnerabilities do not affect the product | C-16 | a generator for the format |

## 6. Watch list

| Signal | Where to read it | Cadence |
|---|---|---|
| A new approved version of the SLSA specification, or a draft track that becomes approved | https://slsa.dev/spec/ | at each refresh |
| A new version of the security baseline | https://baseline.openssf.org/ | at each refresh |
| The final revision of NIST SP 800-218 | https://csrc.nist.gov/pubs/sp/800/218/final | at each refresh |
| A new version of the SWEBOK Guide | https://www.computer.org/education/bodies-of-knowledge/software-engineering | at each refresh |
| A change of the checks of the scorecard | https://github.com/ossf/scorecard/blob/main/docs/checks.md | at each refresh |
| A change of the delivery metrics or of the capability catalogue | https://dora.dev/guides/dora-metrics-four-keys/ | at each refresh |
| A new version of the list of pipeline risks | https://owasp.org/www-project-top-10-ci-cd-security-risks/ | at each refresh |
| A new version of the security maturity model | https://owaspsamm.org/model/ | at each refresh |
| A change of the badge criteria | https://www.bestpractices.dev/en/criteria | at each refresh |

## 7. Decisions and changes

Dated. A reversed decision stays and is marked superseded. Name the models that made or
suggested a judgement, and the person who reviewed the findings and accepted the recipe.

| Date | Decision or change | Reason | Revisit when |
|---|---|---|---|
| 2026-10-11 | Not verified: the intent of the owner was not asked in the session of phase 1. The lines `meaning` and `result` hold the words that the owner gave on 2026-10-10. The line `not wanted` has no answer. The field "Field and disciplines" was written without the owner. | The owner was not in the session. | The review of the owner in phase 3 |
| 2026-10-11 | Roles of the models: a research agent on the largest model of the agent product did phase 2. It selected the sources, wrote the views, the items, the decisions, the summaries of the evidence record and the answers of risk and reward. Reader agents with the read tool only or with web tools only, on a small model, read each source and reported. A second reader on a middle model, and file readers on a small model, compared the evidence record with the sources. No person reviewed the findings. | The procedure asks for the roles. | The review of the owner in phase 3 |
| 2026-10-11 | Five views: `operations`, `security`, `quality`, `supply-chain` and `delivery`. The three concerns that the owner named are views. The views `supply-chain` and `delivery` come from the target of the owner and from the sources. | The owner named operational, security and quality concerns and a supply chain target. The body of knowledge and the sources treat the pipeline and the supply chain as sets of concerns of their own. | The owner changes a view |
| 2026-10-11 | For the owner to decide: the target "SLSA draft highest levels". The checklist uses the tracks of the approved version. The draft tracks Build Environment and Dependency are a target line and an option of a decision only. | The draft says that it can be changed, replaced or discarded. Most requirements of the draft tracks are for a platform provider. | The review of the owner; a draft track becomes approved |
| 2026-10-11 | For the owner to decide: the classes of the sources. S-01 has the class `standard`, S-07 and S-08 have the class `research` as recognized books, S-12 has the class `vendor`, and S-10 has the class `independent`. | The page of S-10 says that a company runs the program; the reader found no peer review. The classes decide the route of admission. | The review of the owner |
| 2026-10-11 | Second reading of the evidence record: 13 of 16 rows were corrected. 3 rows had no finding (S-06, S-13, S-16). 32 of 110 sentences had a finding: 28 said more than the source, 2 had a wrong location, and 2 could be examined only in part. Each finding was corrected in `evidence.md`, and in the rows of `spec.md` and of the table "Requirements" that said the same. Not examined by the second reader: the clause of S-01 on page 104, the words "critical code paths" of S-04 OSPS-SA-03.02, and the streams of the SAMM practices other than Strategy and Metrics. | Step 12 of phase 2. | The next refresh |
| 2026-10-11 | For the owner to decide: the calculation of risk and reward does not admit the items C-10 (error budget), C-34 (isolated release build) and C-41 (delivery measures) with the answers of the research agent. C-34 holds the top build level of the target of the owner. Of the 252 answers, 241 are judgements of the research agent. | The program computes the admission from the answers. The sources give few values for severity, probability and cost. | The owner corrects an answer; then the placement program runs again |
| 2026-10-11 | Deviation: the table "Requirements" does not hold each statement of the reader reports. Left out: statements that a reader marked as a definition, a quotation, a rule for the editors of the guide or a learning need; criteria of S-16 that the reader reported by identifier only; best practices of S-12 and practices of S-05 that the reader reported by name only. Some requirements at one location of S-07, S-10 and S-12 are one row. | The reports give no requirement text for them, or the statement is not a requirement on a project. | The owner asks for the full register |
| 2026-10-11 | Deviation: the stakeholders come from the full reading of the body of knowledge by 20 readers with a question on the groups of persons. The search of the index for each stakeholder was not done. | Each page of the body of knowledge was read with that question; the reports name the groups with their pages. | The owner adds a stakeholder |
| 2026-10-11 | Deviation: the checklist has no item C-25. | A draft item on the depth of verification became the decision "Depth of verification" before the first commit. The identifier is not used. | Never |
| 2026-10-11 | Not verified: S-17 (ISO/IEC 25010). The two public addresses answered with a refusal (HTTP 403). No statement of this specification rests on it. | The source cannot be reached by the reader. | The owner gives the text, or the address is reachable |
| 2026-10-11 | Not verified: the references of the body of knowledge for the views, from `index.py refs`: ISO/IEC/IEEE 20000-1, ISO/IEC/IEEE 12207, ISO/IEC 27001, ISO/IEC 15408, ISO/IEC 18045, ISO 9001, ISO/IEC 15026-1, ISO/IEC/IEEE 29119, IEEE 982.1, IEEE 730, IEEE 1012, EN 50128, DO-178C, and the lists of CVE, CWE, CAPEC and CVSS. They were not retrieved. ISO/IEC/IEEE 32675 was read only from the public page of IEEE Std 2675 (S-13). | Most are paid standards. The time of this run was used for the open sources of each view. | The owner gives a file, or the next refresh |
| 2026-10-11 | Not verified: the exact words of the web sources S-02 to S-08, S-10 to S-14 and S-16. The web tool of the readers gives a summary of a page, not its text. The strength of a requirement (must, should) can be different in the source. | A limit of the tool of the readers. | A reader with the full text reads the source |
| 2026-10-11 | Not verified: parts of sources. S-02: the one-page form was not found, and the pages about, FAQ, terminology, provenance and future directions were not read. S-03: the one-page form was read in part, and 20 linked pages were not read. S-05: only the governance function and the assessment page were read; the practices of the other four functions are known by name only. S-06: the two pages were read from the raw copies of the same repository. S-07: 15 chapters and appendices were read. S-08: 7 chapters were read. S-12: the page of the design principles gave only its title, and only two detail pages of best practices were read. S-13: the public page only. S-14: one page. S-16: the pages of three levels, as summaries. | The readers report these limits. | The next refresh |
| 2026-10-11 | Not verified: the release date of S-01. The report of the reader gives one date for page 1; the row of the seed in `references/seeds.md` gives a different date in its cell "Version or date". The version is the same. Also not verified: the topic matrices of S-01, which the conversion mixed. | Two records disagree. | The owner compares the file with the row of the seed |
| 2026-10-11 | Not verified: the licence of S-04, S-06, S-11, S-12, S-14 and S-16, the version of S-06, S-11, S-14 and S-16, and the issuer of S-08. | The pages that the readers got do not give them. | The next refresh |
| 2026-10-11 | The two NIST sources were converted from their public PDF files into the work folder and read by file readers. No row was added to `references/seeds.md`. | They are sources of this aspect, not seeds of the factory. | The owner wants them as seeds |

## 8. Glossary

Terms that mean different things in the sources. One preferred form per meaning.

| Term | Meaning here | Other meanings in the sources |
|---|---|---|
| shift left | to examine a concern at an earlier step of the life cycle than before | the involvement of stakeholders in quality, security, privacy and verification earlier (S-01 page 400, "left shift"); the detection of defects earlier, where a correction is cheaper (S-08); the address of security earlier, "shifting left" (S-09 page 10); the use of staged rollouts in place of full tests (S-08 Continuous Delivery) |
| DevSecOps | the aspect as the owner states it: the shift left of operational, security and quality concerns | a culture that puts development, security and operations into one team (S-01 page 206); the integration of development, security and operations with culture, automation and platform design (S-01 page 266); the pipelines that build and deploy cloud software (S-15 page 10) |
| level | a level 1, 2 or 3 of the checklist of this recipe | a level of a track of SLSA (S-02); a maturity level of a baseline (S-04); a maturity level of a security practice (S-05); a level of a badge (S-16); an integrity level of software (S-01 page 251) |
| provenance | a signed statement that identifies an artifact by its digest and tells how and where it was built | the data on the origin of all components of a release (S-09 PS.3.2); the attestation of a source revision (S-02 source-requirements); the record of an admitted dependency (S-03 dependency-track) |
| post-incident review | a written review after an incident that finds causes and actions, without blame | postmortem (S-07); post-incident analysis (S-12); post mortem (S-01 page 161) |
| bill of materials | the list of the components of a release | SBOM (S-01 page 192; S-04; S-06) |
| pipeline | the automated path of a change from the repository to production | CI/CD pipeline (S-15); deployment pipeline (S-10); the continuous build (S-08) |
| error budget | the share of failures that an objective permits in a period | not used in the other sources |

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
