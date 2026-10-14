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
- **Field and disciplines**: software engineering; the aspect cuts across the disciplines of the
  operational, the security and the quality concerns
- **Intent of the owner**: the answers of the owner to the questions of phase 1. One line each:
  the words of the owner as a quote, with the date, or `(no answer)`.
  - `meaning`: "DevSecOps is about doing shift left of operational, security, and quality concerns." (2026-10-10)
  - `result`: "achieve SLSA draft highest levels" (2026-10-10)
  - `not wanted`: (no answer)
- **Agreed with the owner on**: 2026-10-11; the field: software engineering; the thing to build:
  the aspect specification and the recipe skill `devsecops`. The owner was not in the session:
  see section 7.

Found by the research, and reviewed by the owner with the other findings. Each line names its
source, or says `(judgement)`. A use case is chosen only when the recipe is applied to a project.

- **Stakeholders**: each group of persons that has an interest in the result or carries a duty
  for it. The research finds them in the body of knowledge of the field and in the sources.
  One line each: a short name, the concerns of the stakeholder for this aspect, and the source.
  - `developers`: to get the result of each check early and near the change; to have clear limits of their security and operations duties (S-03 PO.2.1; S-13 page 33; S-09 pervasive security)
  - `operators`: to plan the operation early; to get software that can be deployed, monitored and rolled back; alerts that need an action (S-01 pages 153, 156; S-10 chapter 1; S-09 monitoring and observability)
  - `security team`: to give the security requirements and the review at the design; to see the results of the security tests; to set the policy for trusted sources of open-source code (S-01 page 266; S-04 pages 21, 28; S-09 pervasive security)
  - `maintainers`: to protect the repository and the pipeline; to approve or isolate the pipeline runs of contributors from outside; to show the security state of the project (S-04 page 27; S-12 maintainers page; S-13 pages 12-13)
  - `product owners`: to agree the tolerance of risk and the service levels with the engineers (S-01 page 162; S-10 chapter 3)
  - `management`: to commit to secure development; to set the policy and the tolerance of risk; to assign the roles and the training (S-01 page 159; S-03 PO.2.3; S-08 strategy and metrics)
  - `quality assurance`: to start the verification early; to keep the tests reliable; to give an assurance that is independent of the development (S-01 pages 255, 257; S-09 test automation)
  - `consumers`: to verify that a release is authentic and not changed; to know the components of a release; to judge the security state of a dependency (S-02 verifying-artifacts; S-03 PS.2.1; S-11 repository page)
  - `suppliers`: to give the provenance and the integrity data of the components that they supply; the operators of the build platform must isolate the builds and sign the provenance (S-02 build-track-basics; S-03 PO.1.3; S-13 page 17)
  - `auditors and regulators`: to get the evidence that each change was authorized and each release was made by the defined process (S-01 pages 187, 189; S-08 policy and compliance; S-09 streamlining change approval)
- **Views**: the points of view that the aspect brings together. A view is a set of concerns
  of the aspect. The research aggregates the concerns of the stakeholders into the views. A
  concern that the owner named in the intent is in a view, or section 7 says why it is not.
  One line each: a short name, what the view is concerned with, the stakeholders whose
  concerns the view holds, and the source. Name the stakeholders in this form, before the
  source: `(stakeholders: [name], [name])`. Use the names of the field "Stakeholders".
  - `operations`: the readiness for production before the release: one source for the code and the environments, automated deployment, service levels, monitoring, rollback (stakeholders: operators, developers, product owners) (S-01 pages 151-166; S-10 chapters 3, 4, 6, 8, 27, 32; S-09 deployment automation)
  - `security`: security in each phase of the work: the threat model at the design, secure code, automated security tests on each change, secrets, the response to vulnerabilities (stakeholders: security team, developers, management, auditors and regulators) (S-01 pages 264-273; S-03 groups PO, PW, RV; S-08 model; S-06 overview)
  - `quality`: defects are found at the earliest point: requirements for quality at the start, automated tests and static analysis on each change, reviews, a regression test for each defect (stakeholders: quality assurance, developers, product owners) (S-01 pages 139-140, 246-263; S-09 test automation, continuous integration; S-14)
  - `supply chain`: the integrity of the path from the source to the released artifact: protected source, a build that is automated and isolated, provenance, dependencies, verification by the consumer (stakeholders: maintainers, consumers, suppliers, auditors and regulators) (S-02 tracks; S-04 pages 11, 13; S-13 pages 11-38; S-01 pages 103-104, 192)
- **Contexts**: the values of each dimension that change the strategy. One line each.
  - `team`: one maintainer; two or more maintainers; an organization with separate roles for security and operations (S-12 levels; S-08 about; S-03 page 12)
  - `delivery`: a library or a package that others install; a service that the team operates; software that is delivered to an acquirer (S-10 chapter 32; S-12 levels; S-03 page 12)
  - `contribution`: a private repository with a full-time team; a public repository with contributors from outside (S-04 page 27; S-14 "When we should not use Continuous Integration")
  - `build platform`: a hosted build platform; builds on the machines of the team; the platform decides the highest build level that is possible (S-02 build-track-basics, build-env-track-basics; S-13 page 22)
  - `regulation`: none; a regulated or safety-critical domain with a duty of evidence (S-01 pages 250-251; S-09 continuous delivery; S-13 pages 7-8)
  - `code base`: new software; existing software without tests (S-09 test automation; S-10 chapter 17)
- **Risk dimensions**: the dimensions on which the risk of a project differs for this aspect.
  One line each: the name, the question that finds it out, the opinion of the kit on the
  answer, and the source.
  - `assurance`: How bad is it for the consumers if a released artifact or the source was changed without authority? Opinion: a project with consumers that it does not know aims for the highest levels of the released version of the supply chain scale. The tracks that are only in the draft are a target only if the project accepts that they can change. (S-13 pages 7-8; S-02 draft home page, spec-stages)
  - `exposure`: Does the software handle personal data, money or critical functions, or does it accept input from parties that are not trusted? Opinion: if yes, adopt the security items above level 1 and make the threat model more rigorous for the high-risk areas. (S-13 pages 7-8; S-03 PW.1.1; S-08 threat assessment)
  - `operative`: Does the team operate the software as a service, and what does an outage cost the users? Opinion: a team that operates a service adopts the operations items above level 1 before the first launch. A library does not need them. (S-10 chapters 3, 32; S-01 page 158)
  - `regulatory`: Must the project show evidence to an acquirer, an auditor or a regulator? Opinion: if yes, keep the evidence of each change and each release as a product of the pipeline, not as work by hand. (S-01 pages 250-251; S-09 streamlining change approval; S-08 policy and compliance)
- **Boundaries**: what each neighbouring aspect owns, and what this aspect keeps. One line each.
  - `architecture and design`: it owns the design of the software and its review. This aspect keeps the security and operations questions that the design must answer before the construction. (S-04 page 12; S-01 pages 7-8)
  - `operation and incident response`: it owns the on-call work, the handling of incidents and the capacity. This aspect keeps what the team prepares before the release. (S-01 pages 151, 167; S-10 chapter 32)
  - `legal compliance`: it owns the interpretation of the law and of the licences. This aspect keeps the evidence that the pipeline makes. (S-08 policy and compliance; S-13 page 19)
  - `key management`: it owns the root of trust and the ceremony for the keys. This aspect keeps the rule that each release is signed and verified. (S-13 pages 33, 40; S-04 pages 10-11)
  - `runtime protection`: it owns the access control and the identity of the running services. This aspect ends at the verified deployment. (S-04 pages 11-12)
- **Targets**: the measurable results that a project reaches when it applies the recipe. The
  targets come from the sources in the research; the owner can name one in the intent. One
  line each: the name, the scale with its levels, the program or the method that measures it,
  and the source of the scale. If the sources give no target, write `(none found)` in place
  of the lines.
  - `supply chain levels`: the target that the owner named. The draft has four tracks, each with its levels: Build L0 to L3, Source L1 to L4, Build Environment L0 to L3, Dependency L0 to L3. The highest levels are Build L3, Source L4, Build Environment L3 and Dependency L3. Method: a verifier examines the provenance and the attestations of an artifact against its expectations; the draft names one verifier program as an example. (S-02 build-track-basics, source-requirements, build-env-track-basics, dependency-track, verifying-artifacts)
  - `repository score`: each check gives 0 to 10; the total is an average with a weight for the risk of each check. Method: a program examines the repository. (S-11 repository page)
  - `project security baseline`: three levels. Level 1 is for each project, level 2 for a code project with two or more maintainers, level 3 for a code project with many users. Method: the project attests itself; a program checks some controls. (S-12 version page, FAQ, maintainers page)
  - `delivery performance`: five measures: change lead time, deployment frequency, failed deployment recovery time, change fail rate, deployment rework rate. The source gives no levels. Method: data of the systems of the project, for one application at a time. (S-09 metrics guide)
  - `service level objectives`: a target value for each service level indicator, for example the part of the requests that succeed; the error budget is one minus the objective. Method: the monitoring of the service. (S-10 chapters 3, 4)
  - `security maturity`: three levels for each of two streams of fifteen practices, by a self-assessment with questions; a second model gives each activity a level from 1 to 5. (S-08 model, assessment; S-07 model data)

## 2. Sources

No single source gates the recipe: the recipe is the fixed side, and each source supports the
items that cite it. **Class** decides the route of admission. The fast lane: `standard`
(standards bodies and regulators), `foundation` (open foundations), `vendor` (a platform vendor
on its own platform), `research` (peer-reviewed research and recognized books), `trusted-data`
(a recorded data source marked as trusted). Every other source is `independent` and passes the
source vetting first. **Read**: full, part or no. A paid source is cited from its official
preview and marked part.

| Id | Source | Issuer | Version or date | Class | License | Read | URL |
|---|---|---|---|---|---|---|---|
| S-01 | Guide to the Software Engineering Body of Knowledge (SWEBOK Guide) | IEEE Computer Society | 4.0a | standard | Free for personal and educational use with the citation; no commercial reprint | part | https://www.computer.org/education/bodies-of-knowledge/software-engineering |
| S-02 | SLSA specification, working draft | The Linux Foundation (copyright holder) | working draft, read 2026-10-11; released version beside it: 1.2 | foundation | Community Specification License 1.0 | part | https://slsa.dev/spec/draft/ |
| S-03 | Secure Software Development Framework (SSDF), NIST SP 800-218 | National Institute of Standards and Technology | 1.1, 2022-02 | standard | Not subject to copyright in the United States | full | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf |
| S-04 | Strategies for the Integration of Software Supply Chain Security in DevSecOps CI/CD Pipelines, NIST SP 800-204D | National Institute of Standards and Technology | 2024-02 | standard | Not subject to copyright in the United States | full | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204D.pdf |
| S-05 | DoD Enterprise DevSecOps Strategy Guide | U.S. Department of Defense, Chief Information Officer | not verified | standard | not verified | no | https://dodcio.defense.gov/Portals/0/Documents/Library/DoDEnterpriseDevSecOpsStrategyGuide.pdf |
| S-06 | OWASP DevSecOps Guideline | OWASP Foundation | v-0.2 | foundation | CC BY-SA 4.0 | full | https://owasp.org/www-project-devsecops-guideline/latest/ |
| S-07 | OWASP DevSecOps Maturity Model (DSOMM) | OWASP Foundation | 5.0.2, 2026-09-17 | foundation | GPL-3.0 for the program; Attribution-ShareAlike for the content | part | https://owasp.org/www-project-devsecops-maturity-model/ |
| S-08 | OWASP Software Assurance Maturity Model (SAMM) | OWASP Foundation | 2.0 | foundation | CC BY-SA 4.0 | part | https://owaspsamm.org/model/ |
| S-09 | DORA capabilities and software delivery performance metrics | DORA, a program of Google Cloud | metrics guide updated 2026-01-05 | research | CC BY 4.0 | part | https://dora.dev/capabilities/ |
| S-10 | Site Reliability Engineering (book) | O'Reilly Media; copyright Google | 2017 | research | CC BY-NC-ND 4.0 | part | https://sre.google/sre-book/table-of-contents/ |
| S-11 | OpenSSF Scorecard, documentation of the checks | Open Source Security Foundation | read 2026-10-11; the pages give no version | foundation | Apache-2.0 | part | https://github.com/ossf/scorecard/blob/main/docs/checks.md |
| S-12 | Open Source Project Security Baseline (OSPS Baseline) | OpenSSF Security Baseline SIG; LF Projects | v2026.08.28 | foundation | not found | part | https://baseline.openssf.org/ |
| S-13 | Software Supply Chain Best Practices | CNCF Technical Advisory Group for Security | the file name has "v1"; the text gives no date | foundation | not found | full | https://project.linuxfoundation.org/hubfs/CNCF_SSCP_v1.pdf |
| S-14 | Continuous Integration (article) | Martin Fowler | revision 2024-01-18 | independent | Copyright of the author; no licence stated | part | https://martinfowler.com/articles/continuousIntegration.html |

## 3. Strategy

High level, for the agent that runs the work. One page.

### 3.1 Goals

- Each operational, security and quality concern has its check at the earliest point where the
  check is possible: the design, the change or the build. It is not left to the release.
- Each check runs by a program on each change, and its result goes to the person who made the
  change.
- A consumer can verify, without trust in a person, where a release comes from and how it was
  built.
- The project knows its level on each target that it selected, and a program measures it.
- The depth follows the risk of the project. The basic items apply to each project.

### 3.2 Order of the work

1. Find the contexts and do the risk analysis along the risk dimensions. The targets and the
   depth of each later step depend on it.
2. Put all that is necessary to build, test and deploy into version control, and protect the
   primary branch and the accounts. Each later check needs one trusted source.
3. Automate the build and the tests on each change. The other checks run in this pipeline.
4. Add the security checks and the quality checks to the pipeline, and write the requirements
   and the threat model for the design. The cost of a defect is lowest here.
5. Make the release a product of the pipeline: provenance, the list of components, signatures,
   and the instructions to verify them. Then increase the build level and the source level to
   the selected target.
6. For software that the team operates: agree the service levels, add the monitoring, automate
   the deployment and the rollback, and do the readiness review before the launch.
7. Measure the selected targets with their programs, and correct the items whose check fails.

### 3.3 Decisions that depend on context

| Decision | Depends on | Options | Sources |
|---|---|---|---|
| Which tracks and which version of the supply chain scale are the target | assurance; build platform | The released version, with the tracks that the source confirms for it: Build and Source. Or the draft, which adds the tracks Build Environment and Dependency and can change or be discarded. | S-02 draft home page, tracks, spec-stages |
| How changes are integrated | contribution; team | Each developer integrates into the main line at least daily, in small changes. Or short branches with a review before the merge, for a public repository with contributors from outside. | S-09 trunk-based development; S-14 "When we should not use Continuous Integration" |
| Who approves a change | team; regulation | The automated checks only, for one maintainer. Or a second trusted person. Or an external approval board, which the research source says to replace with peer review and evidence from the pipeline where the regulation permits. | S-02 source-requirements; S-09 streamlining change approval; S-12 OSPS-QA-07.01 |
| How far the operations items go | delivery | A service that the team operates: service levels, monitoring, staged rollout, readiness review. A library: the automated release only. | S-10 chapters 27, 32; S-01 pages 158-162 |
| When a release goes to production | regulation; delivery | Each change that passes the pipeline is deployed. Or the main line is always ready for a release, and a person decides when. | S-09 continuous delivery; S-14 "Common Questions" |
| Where to start in existing software | code base | Tests for the critical code and for each new or changed part first, and a smoke test for each release. Or full tests from the start for new software. | S-09 test automation; S-10 chapter 17 |
| Which practices of the secure development framework apply | team; delivery; exposure | The framework does not prioritize its practices: the project considers risk, cost, feasibility and applicability. With a hosted service or platform, the project should agree with the provider which party is responsible for each practice. | S-03 page 12 |

### 3.4 Where the sources disagree

| Question | Positions | How this recipe handles it | Sources |
|---|---|---|---|
| What does the name of the aspect mean? | The sources that carry the name are mainly about security in the delivery pipeline: one is about the security of the supply chain in the pipelines, one gives operations and quality only some statements. One maturity model with the name includes activities for operations and tests also. The owner means the early handling of operational, security and quality concerns. | The recipe follows the owner. It takes the operational concerns from the sources of operations and delivery, and the quality concerns from the body of knowledge and the sources of delivery. | S-04 pages 10, 11; S-06 overview; S-07 model data; S-10; S-09; S-01 |
| Must a second person approve each change before the merge? | The supply chain sources demand a review by two trusted persons, or an approval by a person who is not the author, on their highest levels. The delivery sources warn that heavy or asynchronous review makes the changes large and late, and give pair work as an alternative. | The item for the second person is above level 1 and depends on the dimension `assurance`. The recipe tells the project to keep the changes small and the review fast. | S-02 source-requirements; S-12 OSPS-QA-07.01; S-13 page 14; S-09 trunk-based development; S-14 "Common Questions" |
| Is a list of components sufficient for the supply chain? | Three sources ask for a list of components for each release. One source says that the list alone is not sufficient for the management of vulnerabilities and gives no integrity. | The recipe asks for the list and for the provenance, as two items. | S-03 PS.3.2; S-12 OSPS-QA-02.02; S-13 page 18; S-04 page 13 |
| Which practices are basic? | The baseline for open source projects puts the security assessment and the automated tests before a merge on its level 2, and the threat model on its level 3. One maturity model puts the threat model on its level 1. The paper of the cloud foundation makes signed commits a part of its baseline. The secure development framework does not prioritize its practices. | The calculation of risk and reward places each item. The owner sees the answers in the review. | S-12 OSPS-SA-03.01, OSPS-SA-03.02, OSPS-QA-06.01; S-07 model data; S-13 page 11; S-03 page 12 |
| How far must a typical project go on the supply chain scale? | The owner wants the highest levels of the draft. The paper of the cloud foundation limits the most expensive practices, such as builds from source and reproducible builds, to a high assurance or a high risk. The draft says that its content can change or be discarded. | The items for the highest levels are in the checklist. The calculation places them above level 1 or does not admit them for a typical project. The owner decides in the review if the recipe makes them a fixed target. | S-02 draft home page; S-13 pages 7, 17 |

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
| C-01 | All that is necessary to build, test, deploy and configure the software is in version control. | Risk: a state of the software or of its environment cannot be made again or restored. | operations | 1 | authority (4) | a new clone builds and passes its tests in the pipeline with no step by hand | S-09 version control; S-10 chapter 27; S-01 page 158; S-03 PS.1.1; S-14 "Put everything in a version controlled mainline" |
| C-02 | The release or the deployment is automated and uses the same process for each environment. | Risk: a manual step fails or differs between the test and the production. | operations | 1 | authority (4) | the last release was made by the pipeline; the same definition deploys each environment | S-09 deployment automation; S-10 chapters 8, 27; S-01 pages 154-158; S-08 secure deployment; S-14 "Automate Deployment" |
| C-03 | The environments are defined as code in version control, and no person changes a running environment by hand. | Risk: the environments drift apart, and a test result does not hold in production. | operations | 2, operative | authority (4) | the definition of each environment is in the repository; a drift check reports no difference | S-01 page 158; S-04 pages 30-31; S-13 pages 31-32; S-03 PO.3.2 (an example) |
| C-04 | The service levels are agreed with the product owners before the launch, and the monitoring measures them. | Risk: the team invests too much or too little in reliability, and the users form their own expectations. | operations | 2, operative | authority (2) | a document states each objective with its measurement; a report compares the measured values with it | S-10 chapters 3, 4, 32; S-01 pages 158, 162 |
| C-05 | The monitoring of the failures that users see exists before the launch, and each alert needs an action. | Risk: the team learns of a failure from its users, or real failures hide in alerts that nobody reads. | operations | 2, operative | authority (3) | the alert rules are in the repository; each rule names its action | S-10 chapters 6, 32; S-09 monitoring and observability; S-01 pages 161-162 |
| C-06 | A readiness review before the launch examines the capacity, the failure modes, the dependencies and the steps that are done by hand. | Risk: a launch fails for a cause that was known and not examined. | operations | 2, operative | authority (1) | judgement | S-10 chapters 27, 32 |
| C-07 | A change goes to the users in stages, and a rollback is automated and rehearsed. | Risk: a faulty release reaches all users, and the return to the last good state takes too long. | operations | 3, operative | authority (3) | the deployment definition has the stages; the record of the last rollback rehearsal has a date | S-10 chapters 17, 27; S-01 pages 159-160; S-07 model data |
| C-08 | Version control holds no secret, and a program examines each change for secrets before or at the push. | Risk: a credential leaks with the source and gives access to the systems of the project. | security | 1 | authority (4) | the secret scan is a required job of the pipeline and passes | S-12 OSPS-BR-07.01; S-04 page 29; S-13 page 12; S-06 secrets management |
| C-09 | The project publishes how to report a vulnerability, and it has a process to handle a report. | Risk: a person who finds a vulnerability cannot tell the project, or tells the public first. | security | 1 | authority (3) | the repository has a security policy with a contact | S-12 OSPS-VM-02.01; S-03 RV.1.3; S-11 Security-Policy |
| C-10 | A static analysis for security weaknesses runs on each change. | Risk: a common coding weakness reaches the release because nobody looked for it. | security | 1 | authority (6) | the analysis is a job of the pipeline for each change | S-03 PW.7.2; S-04 page 28; S-13 page 13; S-06 static application security testing; S-08 security testing; S-11 SAST |
| C-11 | Each change is examined by a program for dependencies with known vulnerabilities, and a finding above the agreed threshold stops the change. | Risk: the software ships a component with a vulnerability that is public. | security | 1 | authority (6) | the dependency scan is a required job of the pipeline; the threshold is in the repository | S-12 OSPS-VM-05.03; S-04 page 29; S-13 page 19; S-06 software composition analysis; S-08 secure build; S-11 Vulnerabilities |
| C-12 | A threat model of the design exists before the construction, and it is updated when the design changes. | Risk: a flaw of the design is found after the release, when its correction costs the most. | security | 1 | authority (6) | judgement | S-03 PW.1.1; S-06 threat modeling; S-08 threat assessment; S-12 OSPS-SA-03.02; S-01 pages 266-267; S-09 pervasive security |
| C-13 | The roles for security are defined, and each check, each exception and each correction has an owner. | Risk: all persons own security, thus nobody does the work. | security | 2, exposure | authority (3) | judgement | S-03 PO.2.1 (the examples); S-01 page 266; S-08 strategy and metrics |
| C-14 | Dynamic security tests run in the pipeline against a deployed test instance. | Risk: a weakness that shows only in the running software is not found before the release. | security | not admitted | authority (4) | the dynamic test is a job of the pipeline and its report is kept | S-03 PW.8.2; S-04 page 28; S-06 dynamic application security testing; S-08 secure deployment |
| C-15 | Automated tests run on each change before the merge, and a build that fails is corrected before other work. | Risk: a defect is found late, when its cause is hard to find and others built on it. | quality | 1 | authority (5) | the test job is required for a merge; the primary branch is green | S-09 continuous integration, test automation; S-12 OSPS-QA-06.01; S-10 chapter 17; S-01 pages 107, 139-140; S-11 CI-Tests; S-14 "Make the Build Self-Testing" |
| C-16 | The static checks of the code run on each change, and the build treats a warning as an error. | Risk: defects that a program can find stay in the code and cost a test or a user to find. | quality | 1 | authority (4) | the lint job is required for a merge; the build has no warning | S-03 PW.6.2 (an example); S-04 page 27; S-06 linting code; S-01 page 107 |
| C-17 | Each defect that is reported or found in production becomes an automated test. | Risk: the same defect comes back. | quality | 1 | authority (2) | judgement | S-10 chapter 17; S-08 requirements-driven testing |
| C-18 | The requirements for quality, security and operation are written at the start, each with its acceptance check. | Risk: a requirement that is not functional is forgotten, and the correction is rework. | quality | 1 | authority (3) | judgement | S-01 pages 43, 46-47, 248; S-08 security requirements; S-03 PW.1 |
| C-19 | The primary branch is protected: no direct commit, no forced push, and each change passes the required checks. | Risk: a change goes around the checks, or the history is rewritten. | supply chain | 1 | authority (5) | the protection rules of the primary branch show these settings | S-12 OSPS-AC-03.01; S-02 source-requirements; S-04 page 27; S-13 page 14; S-11 Branch-Protection |
| C-20 | Each account that can change the repository or the pipeline uses multi-factor authentication. | Risk: one stolen password lets an attacker change the source or the release. | supply chain | 1 | authority (4) | the setting of the hosting organization requires it | S-12 OSPS-AC-01.01; S-13 page 14; S-03 PO.5.2 (an example); S-04 page 18 (an example) |
| C-21 | The jobs of the pipeline have the least privileges, and code that is not trusted cannot reach the credentials of the pipeline. | Risk: a contribution from outside takes the secrets of the pipeline or changes a release. | supply chain | 1 | authority (3) | each pipeline definition declares its permissions; a program examines the definitions for dangerous patterns | S-12 OSPS-BR-01.03, OSPS-AC-04.02; S-11 Token-Permissions, Dangerous-Workflow; S-04 pages 19, 27 |
| C-22 | The release build is automated, is defined as code, and runs on a hosted build platform, not on the machine of a person. | Risk: a release cannot be repeated, or the machine of one person changes it. | supply chain | 1 | authority (5) | the build definition is in the repository; the release artifacts come from the platform | S-02 build-track-basics; S-04 pages 17, 24; S-13 page 30; S-08 secure build; S-10 chapter 8 |
| C-23 | Each release has provenance that the build platform makes and signs: it identifies the artifact by its digest and tells how the artifact was built. | Risk: nobody can show where an artifact comes from, thus a changed artifact is not found. | supply chain | 2, assurance | authority (4) | a verifier program accepts the provenance of the last release | S-02 build-track-basics, build-requirements; S-03 PS.3.2; S-04 pages 25-26; S-13 page 35 |
| C-24 | Each release has a list of its components that the build makes. | Risk: when a component gets a known vulnerability, nobody knows which releases have it. | supply chain | 2, assurance | authority (5) | the last release has the list as an asset | S-03 PS.3.2; S-12 OSPS-QA-02.01, OSPS-QA-02.02; S-13 page 18; S-08 secure build; S-01 page 192 |
| C-25 | Each dependency of the build and of the release is pinned to a version that can be verified, and a program proposes the updates. | Risk: a dependency changes without notice, or stays old with known vulnerabilities. | supply chain | 1 | authority (3) | a program reports no dependency that is not pinned; the update program is enabled | S-11 Pinned-Dependencies, Dependency-Update-Tool; S-13 pages 29, 40-43; S-07 model data |
| C-26 | The project tells the consumers how to verify the integrity and the origin of a release, and the verification succeeds. | Risk: the provenance exists and nobody uses it, thus a changed artifact is accepted. | supply chain | 2, assurance | authority (4) | the documented command verifies the last release | S-02 verifying-artifacts; S-12 OSPS-DO-03.01, OSPS-DO-03.02; S-03 PS.2.1; S-13 page 37 |
| C-27 | The release builds are isolated: one run cannot influence a different run, and the build steps cannot reach the signing secrets. | Risk: a compromised build step forges the provenance or changes a different build. | supply chain | 2, assurance | authority (2) | the provenance names a build platform that the verifier trusts for the highest build level | S-02 build-track-basics, build-requirements; S-13 pages 31-33 |
| C-28 | A change to a protected branch needs the approval of a second trusted person who is not its author. | Risk: one person, or one stolen account, puts a harmful change into the release. | supply chain | 2, assurance | authority (5) | the protection rules require one approval that is not from the author | S-02 source-requirements; S-12 OSPS-QA-07.01; S-13 page 14; S-04 page 26; S-11 Code-Review |
| C-29 | Each dependency enters the build only through a controlled path that verifies it, examines it and records the result. | Risk: a harmful or changed dependency enters the build unseen. | supply chain | not admitted | authority (3) | the build cannot reach a source of dependencies outside the path; each dependency has a signed record | S-02 dependency-track; S-13 pages 16-19; S-04 pages 18, 21 |
| C-30 | The build environment is made from an image with verified provenance, and its start state is attested. | Risk: a changed build image or host changes each build that runs on it. | supply chain | not admitted | authority (1) | the attestation of the build environment is verified before each build | S-02 build-env-track-basics |

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

- **Goal**: The project has a selection of checklist items that its owner made with a risk
  analysis, and a plan that brings each selected item to a check that passes. The operational,
  security and quality concerns have their checks at the design, at the change and at the build.
- **Reads first**: The contexts of the project: the team, the delivery, the contribution, the
  build platform, the regulation and the state of the code base. The answers of the owner of
  the project on the risk dimensions. The selection of the project, if one is committed. The
  repository, the pipeline definitions and the protection rules as they are.
- **Applies**: The order of the work of the strategy, and the decisions that depend on context.
  It judges each selected checklist item by its check, and it measures the selected targets
  with their programs. It gives the opinion of the kit for each risk dimension and proposes a
  target level; the owner of the project decides.
- **Delegates**: The examination of a repository for its security settings. The making and the
  verification of provenance and signatures. The list of components of a release. The scans for
  secrets, for weaknesses and for dependencies with known vulnerabilities. The definition of
  the pipeline for one hosting product. The monitoring and the staged deployment for one
  platform.
- **Stops when**: The plan is written and the owner of the project must decide on it. A
  decision that depends on context needs a person. The project has no hosted build platform
  and the selected build level needs one. A source or a program for a check cannot be reached.

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
| OpenSSF Scorecard | examines a repository and gives the repository score | C-08 to C-11, C-19, C-21, C-25, C-28 | the program of the product; a token for the hosting product |
| slsa-verifier | verifies the provenance of an artifact against the expected builder and source | C-23, C-26, C-27 | the program of the product |
| The hosting product and its pipeline (one skill for each product) | the protection rules, the accounts, the pipeline definitions, the hosted build | C-01, C-02, C-15, C-16, C-19 to C-22, C-28 | the command line program of the hosting product |
| Sigstore | signs artifacts and provenance with an identity | C-23, C-26 | the client program of the product |
| A generator of a list of components (one skill for each format) | makes the list of components from the build | C-24 | the generator program |
| Dependabot or Renovate | proposes the updates of dependencies | C-25 | none; the hosting product runs it |
| Privateer plugin for the OSPS Baseline | examines some controls of the project security baseline | C-08, C-19, C-20 | the program of the product |
| SAMM Assessment Toolbox | gives the security maturity from the answers of a self-assessment | C-12, C-13, C-18 | a spreadsheet program |
| A monitoring platform (one skill for each product) | measures the service level indicators and sends the alerts | C-04, C-05, C-07 | the client of the platform |

## 6. Watch list

| Signal | Where to read it | Cadence |
|---|---|---|
| The draft of the supply chain specification changes: a track, a level or its stage | https://slsa.dev/spec/draft/whats-new and https://slsa.dev/spec-stages | at each refresh; before a project selects a draft track |
| A new released version of the supply chain specification | https://slsa.dev/spec/draft/ (the line that names the current version) | at each refresh |
| A new version of the project security baseline | https://baseline.openssf.org/ (the list of versions) | at each refresh |
| A revision of the secure development framework | https://csrc.nist.gov/pubs/sp/800/218/final | at each refresh |
| A new version of the two maturity models | https://owaspsamm.org/model/ and the file `generated/model.yaml` of the data repository of S-07 | at each refresh |
| A change of the checks of the repository score | https://github.com/ossf/scorecard/blob/main/docs/checks.md | at each refresh |
| A change of the delivery performance metrics | https://dora.dev/guides/dora-metrics/ (the date of the last update) | at each refresh |
| A new version of the body of knowledge | `factory/sota-research/references/seeds.md`, the row `swebok` | at each refresh |

## 7. Decisions and changes

Dated. A reversed decision stays and is marked superseded. Name the models that made or
suggested a judgement, and the person who reviewed the findings and accepted the recipe.

| Date | Decision or change | Reason | Revisit when |
|---|---|---|---|
| 2026-10-11 | Not verified: the intent of the owner was not asked in the session of phase 1. The lines `meaning` and `result` of the field "Intent of the owner" hold the words that the owner gave on 2026-10-10. The owner gave no answer for the line `not wanted`. | The owner was not in the session. The task of the session gave the words of the owner with their dates. | The owner is in a session: ask the question of the line `not wanted`, and let the owner confirm the lines `meaning` and `result`. |
| 2026-10-11 | Not verified: the owner did not name the field and the disciplines. The field "Field and disciplines" has the field of this factory, from the head text of the template. Its disciplines are from the line `meaning` of the intent. The owner did not confirm the field "Agreed with the owner on". | The owner was not in the session, and the task of the session did not permit a question. | The review of the owner in phase 3, or earlier if the owner is in a session. |
| 2026-10-11 | Second reading of the evidence record: rows corrected: 9. Rows in the record: 13. The corrected rows are S-01, S-02, S-03, S-04, S-06, S-07, S-12, S-13 and S-14. The rows S-08, S-09, S-10 and S-11 had no finding. Each row of this specification that said the same was corrected also. | Step 11 of the research. Most findings were of the type `overstated`: the summary made an example of a source into a task, or dropped a limit. | Each refresh: the second reading runs again for the rows that change. |
| 2026-10-11 | Not verified: the source S-05 was not read. The address answered with the error 403 to the converter. No item cites S-05. | The host refused the download. S-05 is one of the sources that carry the name of the aspect, for the context of defence. | The owner gives the file, or a different address is found. |
| 2026-10-11 | Not verified: the source S-01 was read in part. The first reader gave the pages that it read and the pages that it did not read; the areas architecture and design, the foundations and the appendices were not read. The date of the guide in the report of the reader is different from the date in the row `swebok` of `factory/sota-research/references/seeds.md`. Section 2 gives only the version. | The converted file is too large for one reader. The second reader read the pages of the evidence row. | A refresh: give the pages that were not read to a new file reader, and compare the two dates. |
| 2026-10-11 | Not verified: the web tool of the readers returns a summary of a page, not its text. Thus the sources S-02, S-07, S-08, S-09, S-10, S-11, S-12 and S-14 have `part` in the cell Read, and no quote of them is in this specification. The reader of S-06 reported `full` through the same tool. | The reports of the readers say so. | A reader with a tool that returns the text of a page. |
| 2026-10-11 | Not verified: the two readers of S-02 disagree on what Build L1 demands of the provenance. The evidence row and the item C-23 use the narrower statement of the second reader. The first reader reported that the Build track does not cover an insider of the platform and typosquatting; the second reader did not find this, and the sentence was removed. | The readers read different pages of the draft through a tool that summarizes. | Before a project selects a build level: read the page of the build requirements again. |
| 2026-10-11 | Not verified: if the released version of the supply chain specification has the tracks Build Environment and Dependency. The reader confirmed the tracks Build and Source for the released version. The two pages that the reader read disagree on which version added the Source track. | The pages of the released version for these tracks were not read. | The review of the owner; the decision on the tracks in 3.3. |
| 2026-10-11 | Decision for the owner: the intent says "achieve SLSA draft highest levels". The calculation of risk and reward places the items for Build L3 (C-27) and Source L4 (C-28) on level 2 with the dimension `assurance`, and it does not admit the items for the draft tracks Dependency (C-29) and Build Environment (C-30). The checklist keeps the four items. The owner decides if the recipe makes the highest levels a fixed target, and if the draft tracks are a part of it. | The procedure tells to follow the owner and to let the calculation place the items. The answers for these items are by judgement for a typical project. | The review of the owner in phase 3. |
| 2026-10-11 | The view `supply chain` was added to the three concerns that the owner named. The concerns operational, security and quality are each a view. Each stakeholder is in a view. | The line `result` of the intent names a supply chain scale, and four sources hold these concerns as a set of their own. | The review of the owner. |
| 2026-10-11 | The knowledge areas of S-01 that the aspect touches and that are not a view of their own: requirements, construction, testing, maintenance, configuration management, management, process, models and methods. Their concerns are in the four views: testing and requirements in `quality`, configuration management and construction in `supply chain` and `quality`, management and process in `security` and in the strategy. | A view for each knowledge area gives views with one or two items and no stakeholder of their own. | The owner adds a view. |
| 2026-10-11 | Requirements of the sources that are not checklist items: the daily integration into the main line and the review style (a decision in 3.3, they depend on context); the ten-minute build; signed commits; fuzzing; the analysis of root causes of vulnerabilities; role-based training; privacy; scans of infrastructure and containers; licence scans (boundary `legal compliance`); reproducible builds and builds from source (one source limits them to a high assurance). | They depend on context, belong to a neighbouring aspect, or one source only states them. They were not put through the calculation. | The owner asks for one of them as an item; a trial finds a gap. |
| 2026-10-11 | Not verified: the item C-14 is not admitted by the calculation, although four fast-lane sources state it. The answer for the effort to keep it rests on one page of S-06. | The calculation decides. The owner can correct the answer. | The review of the owner. |
| 2026-10-11 | Not verified: the vetting of S-14. The program measured a date of the page that is different from the revision date that the reader reported; with the revision date the score for the age is lower. The reader did not verify if a fast-lane source refers to the article, thus the answer is 0. Only the items C-01, C-02 and C-15 cite S-14, each beside fast-lane sources. | The collector reads the date that the server gives. | The confirmation of the owner. |
| 2026-10-11 | Not verified: no source of a regulator was read for the context `regulation`. The context rests on S-01, S-09 and S-13. One search result named a new draft revision of S-03; it was not read, and section 2 has the version that the reader read. | The search was for the aspect and its views, not for one jurisdiction. | The owner names a regulation; a refresh reads the revision of S-03. |
| 2026-10-11 | Roles of the models: the model of the session did the searches, distilled the findings, the strategy and the checklist, and gave the answers of risk and reward. Of the 180 answers, the check counts those with a source and those by judgement. Small models read the sources as first readers. A mid-size model did the second reading of the web sources, and small models did the second reading of the converted files, each in a new agent. No person reviewed the findings yet. | The procedure asks for the roles. | The review and the acceptance of the owner. |

## 8. Glossary

Terms that mean different things in the sources. One preferred form per meaning.

| Term | Meaning here | Other meanings in the sources |
|---|---|---|
| DevSecOps | The early handling of the operational, the security and the quality concerns of software, with checks that programs run (the intent of the owner). | A paradigm of agile development for cloud-native applications with CI/CD pipelines (S-04). A delivery pipeline with security controls (S-06). |
| shift left | To put a check at the earliest point of the work where it is possible. | To put security into the daily work (S-09). To start the tests early (S-01). |
| level | The level of a checklist item in this kit: 1, 2 or 3. | The level of a track of the supply chain scale (S-02). The maturity level of a project (S-12), of a practice (S-08) or of an activity (S-07). |
| provenance | A record, made by the build platform, that identifies an artifact by its digest and tells how the artifact was built. | The data on the origin of each component, for example a list of components (S-03). |
| list of components | The list of the components of one release, made by the build. | Software bill of materials, SBOM (S-03, S-04, S-13); dependency list (S-12). |
| build platform | The hosted service that runs the release build and signs the provenance. | Build system, CI server, software factory (S-13, S-14). |
| consumer | A person or an organization that uses a release of the project. | Acquirer (S-03); verifier (S-02); end user (S-04). |

## Files beside this specification

- `evidence.md`: for each source a summary of what it contributes, where in the source that
  is, the rows of this specification that it supports, and the date read. The summary is in
  Simplified Technical English and in the words of this kit. A second reader compares each
  line with the source. A quote stays only where the wording itself is the point.
- `vetting.md`: for each independent source the measured signals, the result of the rubric and
  the owner's confirmation; for each item the answers of the risk and reward calculation.
- `trial.md`: the record of the trials of the recipe on a project. This file is optional.
  - The table "Trials" has one row for each trial. Its columns are Id, Date, Project, Commit
    of the specification, and Plan. The cell "Plan" holds where the plan is, or `not kept`.
  - The table "Findings" has one row for each finding of the review of a plan. Its columns
    are Id, Trial, Viewpoint, Finding, Route and Status.
  - The viewpoint is one of the viewpoints of the review. The reviewer gives it.
  - The route is `recipe`, `tooling` or `implementation skill`.
  - The status is `open`, `corrected in <revision or commit>` or `declined: <reason>`.
