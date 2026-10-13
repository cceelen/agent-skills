# Aspect specification: DevSecOps

**Branch**: `001-devsecops` | **Research date**: 2026-10-13 | **Supersedes**: none | **Accepted**: pending

Layer one of the factory: the exploration of one major aspect of software engineering. This
specification is the source of the recipe for the aspect, a strategy and a generic checklist
that hold the global state of the art (SOTA): the best practices that the industry has produced
so far. A helper renders the recipe skill from it. The implementation skills for single products
are layer two: each set gets its own specification through the Spec Kit product flow. Keep this
file high level. It holds nothing that an agent can learn from the project or from a source.

## 1. Aspect

Settled with the owner before the research. Only the field, the thing to build and the intent
of the owner: no use case, no first user, no stakeholder, nothing narrower.

- **Aspect**: DevSecOps: the shift left of operational, security and quality concerns.
- **Field and disciplines**: software engineering; it cuts across the disciplines of operations, security and quality.
- **Intent of the owner**: the answers of the owner to the questions of phase 1. One line each:
  the words of the owner as a quote, with the date, or `(no answer)`.
  - `meaning`: "DevSecOps is about doing shift left of operational, security, and quality concerns." (2026-10-10)
  - `result`: "we need to check for covering essential and non negotiable basics of each of those 3 points of views." (2026-10-10); "we need to be able to iterate the spec with the sota research and speckit setup so that we can achieve SLSA draft highest levels" (2026-10-10); "the slsa L2 should be a baseline. L3 the goal. beyond L3 aspirational (e.g. hermetic repeatable build, or in the asus zenbook case the usage of a build service)." (2026-10-11)
  - `not wanted`: "running build, test, and packaging in the same step and exposing credentials is a no no. See SLSA build track." (2026-10-11)
- **Agreed with the owner on**: 2026-10-11; the field is software engineering, and the thing to build is the aspect specification and the recipe skill `devsecops` ("do the DevSecOps research and generate a skill", 2026-10-10).

Found by the research, and reviewed by the owner with the other findings. Each line names its
source, or says `(judgement)`. A use case is chosen only when the recipe is applied to a project.

- **Stakeholders**: each group of persons that has an interest in the result or carries a duty
  for it. The research finds them in the body of knowledge of the field and in the sources.
  One line each: a short name, the concerns of the stakeholder for this aspect, and the source.
  - `software engineers`: they build the security and the quality into the software, and they use the operations services to deploy it; developers, maintainers and contributors are in this group (S-01 pages 153, 264; S-05 Principle 2)
  - `operations engineers`: they deploy, monitor and restore the service, and they want software that is prepared for operation; site reliability engineering and platform engineering are in this group (S-01 pages 152-153; S-14 chapter 8)
  - `security team`: it wants the threats known, the controls automated and the vulnerabilities handled, without a block of the delivery (S-01 pages 266, 268; S-04 page 21)
  - `quality assurance`: it wants an objective view on the quality of the product and of the process; testers, reviewers, the quality assurance function and the independent verification are in this group (S-01 pages 255, 257-259)
  - `management`: it sets the policy and the risk tolerance, gives the resources and carries the last responsibility; the organization that makes the product is in this group (S-01 pages 159, 162; S-03 page 16; S-12 page 11)
  - `users and customers`: they want a product that is safe to use, updates for it, and a way to verify what they get (S-02 pages 1, 3; S-03 page 11; S-06 page 12)
  - `suppliers`: the providers of components, of a build platform or of a service, whose practices become a part of the product (S-01 pages 157-158; S-02 pages 1-4; S-12 page 18)
  - `regulators and auditors`: the authorities, the assessors and the auditors that ask for evidence of conformity (S-01 pages 124, 187, 259; S-06 pages 13-14; S-12 page 17)
- **Views**: the points of view that the aspect brings together. A view is a set of concerns
  of the aspect. The research aggregates the concerns of the stakeholders into the views. A
  concern that the owner named in the intent is in a view, or section 7 says why it is not.
  One line each: a short name, what the view is concerned with, the stakeholders whose
  concerns the view holds, and the source. Name the stakeholders in this form, before the
  source: `(stakeholders: [name], [name])`. Use the names of the field "Stakeholders".
  - `operations`: the release, the deployment, the rollback, the monitoring, the incident response and the continuity of the running software, prepared in the development (stakeholders: operations engineers, software engineers, management, users and customers, suppliers, regulators and auditors) (S-01 pages 151-164; S-14; S-12)
  - `security`: the integrity of the source, of the build and of the artifacts, the secure development, the dependencies and the handling of vulnerabilities (stakeholders: security team, software engineers, management, users and customers, suppliers, regulators and auditors) (S-01 pages 264-269; S-02; S-03; S-04)
  - `quality`: the tests, the reviews, the measurable quality requirements and the assurance of the product and of the process, with quick feedback (stakeholders: quality assurance, software engineers, management, users and customers, regulators and auditors) (S-01 pages 246-260; S-16; S-15)
- **Contexts**: the values of each dimension that change the strategy. One line each.
  - `kind of delivery`: a service that the team operates; a product or a library that other persons install (S-01 page 155; S-06 page 9; S-14 chapter 4)
  - `size of the organization`: a very small organization, to 25 persons; a larger organization; a microenterprise in the sense of a regulation (S-01 page 163; S-12 page 11)
  - `openness`: an open project with changes from persons outside; a closed project with trusted persons only (S-09 CICD-SEC-04; S-04 page 27; S-11 level headings)
  - `build platform`: a hosted platform of a provider; build machines that the project operates (S-02 page 3; S-19 Self-hosted runners)
  - `binding rules`: no binding rule; a regulation for products; a regulation for a sector; a rule of an industry (S-06 page 9; S-12 pages 8-9; S-07 page 9)
  - `rhythm of the releases`: continuous delivery from the main line; planned releases with a freeze and with release candidates (S-05 Principle 6; S-25 release procedure; S-01 page 59)
- **Risk dimensions**: the dimensions on which the risk of a project differs for this aspect.
  One line each: the name, the question that finds it out, the opinion of the kit on the
  answer, and the source.
  - `regulatory`: Does a law, a regulation or a rule of an industry bind the product or the organization? [Opinion: if yes, do each item that the binding rule asks for, and do not decline it; write the rule and its owner first.] (S-06 page 9; S-07 page 9; S-12 pages 8-9)
  - `exposure`: Can a public network reach the software or its pipeline, or does the software handle private or sensitive data? [Opinion: if yes, do the items of the security view on each level before the first public release.] (S-01 page 162; S-09 CICD-SEC-07; S-05 collection page)
  - `criticality`: What is the damage if the software fails or gives a wrong result? [Opinion: the higher the damage, the more independent the verification and the slower the rollout; for a low damage, level 1 is sufficient at first.] (S-01 pages 136, 251; S-14 chapter 17)
  - `reach`: Do other projects, customers or the public use the artifacts that the project releases? [Opinion: if yes, reach the baseline of the build integrity scale first and then its goal, because one bad release reaches each consumer.] (S-02 pages 1-2; S-11 level headings; S-18 page 8)
- **Boundaries**: what each neighbouring aspect owns, and what this aspect keeps. One line each:
  a short name, what the neighbouring aspect owns and what this aspect keeps, the state, and
  the source. A boundary has one of two states. Write the state in one of these forms, before
  the source. `(proposed)`: the research proposes the boundary, and it takes no requirement.
  `(decided by the owner on <YYYY-MM-DD>)`: the owner decided the boundary on that date, and
  a requirement can go to it. Only the owner decides a boundary. A line without a state is
  proposed.
  - `requirements engineering`: a neighbouring aspect owns the elicitation, the analysis and the management of the functional requirements; this aspect keeps the security, operations and quality requirements and their trace to the tests (proposed) (S-01 pages 43-66)
  - `architecture and design`: a neighbouring aspect owns the structure of the software and its design methods; this aspect keeps the threat model, the design for operation and the secure defaults (proposed) (S-01 pages 67-98)
  - `project management`: a neighbouring aspect owns the planning, the estimation and the control of a project; this aspect keeps the roles and the measurement of delivery and quality (proposed) (S-01 pages 202-220)
  - `engineering economics`: a neighbouring aspect owns the decisions on cost and benefit; this aspect keeps the selection of the checklist items by risk (proposed) (S-01 pages 288-311)
  - `software maintenance`: a neighbouring aspect owns the maintenance process and the end of life; this aspect keeps the security updates and the support period (proposed) (S-01 pages 167-184)
  - `professional practice`: a neighbouring aspect owns the ethics, the contracts and the conduct of the profession; this aspect keeps the training that a role needs (proposed) (S-01 pages 274-287)
  - `foundations`: a neighbouring aspect owns the computing, mathematical and engineering foundations; this aspect keeps nothing of them (proposed) (S-01 pages 312-386)
  - `legal conformity`: a neighbouring aspect owns the duties of authorities, courts, importers and distributors, the procedures of conformity assessment and the liability rules; this aspect keeps the duties that a law puts on the development, the delivery and the handling of vulnerabilities (proposed) (S-06 pages 14-16; S-12 pages 7-9; S-18 pages 7-10)
  - `product security functions`: a neighbouring aspect owns the security functions inside the product, such as encryption, access control and the handling of payment data; this aspect keeps the secure defaults and the tests of these functions in the pipeline (proposed) (S-06 page 24; S-07 pages 243-256)
  - `platform and tool providers`: a neighbouring aspect owns the duties of the provider of a build platform, of a source control system, of a verifier or of a package ecosystem; this aspect keeps the choice of a platform that reaches the target level and the use of its evidence (proposed) (S-02 pages 2-4, 7-10)
  - `enterprise risk and resilience`: a neighbouring aspect owns the risk, continuity and third-party management of the whole organization; this aspect keeps the backup, the incident response and the supplier requirements of the software delivery (proposed) (S-12 pages 10-15)
- **Targets**: the measurable results that a project reaches when it applies the recipe. The
  targets come from the sources in the research; the owner can name one in the intent. One
  line each: the name, the scale with its levels, the program or the method that measures it,
  and the source of the scale. If the sources give no target, write `(none found)` in place
  of the lines.
  - `SLSA build track`: the levels Build L0 to Build L3; the owner names L2 as the baseline, L3 as the goal and more than L3 as an aspiration; a verifier measures it when it examines the provenance of an artifact against the expected builder and build (S-02 pages 1-3, 8-9)
  - `SLSA source track`: the levels Source L1 to Source L4; the source control system states the level in a summary attestation (S-02 pages 5-7)
  - `software delivery metrics`: five measured values without a level: change lead time, deployment frequency, failed deployment recovery time, change fail rate and deployment rework rate; computed from the data of the pipeline for one service (S-13 guide)
  - `repository practice score`: a score from 0 to 10 for each of 20 checks; a program computes it from the repository (S-10 section list)
  - `security baseline of an open project`: three maturity levels of controls; a self-assessment against the controls of one dated version (S-11 version page)
  - `maturity of software assurance`: three maturity levels for each of 15 practices; a self-assessment (S-08 about page, model page)

## 2. Sources

No single source gates the recipe: the recipe is the fixed side, and each source supports the
items that cite it. **Class** decides the route of admission. The fast lane: `standard`
(standards bodies and public authorities), `regulation` (laws and regulations), `governance`
(frameworks of governance and of audit, rules of an industry), `foundation` (open foundations), `vendor` (a platform vendor
on its own platform), `research` (peer-reviewed research and recognized books), `trusted-data`
(a recorded data source marked as trusted). Every other source is `independent` and passes the
source vetting first. **Read**: full, part or no. A paid source is cited from its official
preview and marked part. **Views**: the views of section 1 that the source was read for, with a
comma between two names, or `all` for a body of knowledge. Each view has two or more sources
of its own field that were read.

| Id | Source | Issuer | Version or date | Class | License | Read | Views | URL |
|---|---|---|---|---|---|---|---|---|
| S-01 | Guide to the Software Engineering Body of Knowledge (SWEBOK Guide) | IEEE Computer Society | 4.0a, 2025-09-25 | standard | no license name; individual use that is not commercial | full | all | https://www.computer.org/education/bodies-of-knowledge/software-engineering |
| S-02 | SLSA specification: the pages build track basics, build requirements, source requirements and verifying artifacts | The Linux Foundation (SLSA project) | 1.2, approved | foundation | Community Specification License 1.0 | full | security | https://slsa.dev/spec/v1.2/ |
| S-03 | Secure Software Development Framework (SSDF), NIST SP 800-218 | National Institute of Standards and Technology | 1.1, 2022-02 | standard | no license name; voluntary use | full | security, quality | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf |
| S-04 | Strategies for the Integration of Software Supply Chain Security in DevSecOps CI/CD Pipelines, NIST SP 800-204D | National Institute of Standards and Technology | 2024-02 | standard | no license name; voluntary use | full | security, operations | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204D.pdf |
| S-05 | Secure development and deployment guidance | National Cyber Security Centre, United Kingdom | 1.0, 2018-11-22 | standard | not found | part | security, operations, quality | https://www.ncsc.gov.uk/collection/developers-collection |
| S-06 | Regulation (EU) 2024/2847 (Cyber Resilience Act) | European Parliament and Council | 2024-10-23 | regulation | not found | part | security | https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng |
| S-07 | Payment Card Industry Data Security Standard: Requirements and Testing Procedures | PCI Security Standards Council | 4.0.1, 2024-06 | governance | not found; copyright notice only | part | security, operations | https://www.pcisecuritystandards.org/document_library/ |
| S-08 | OWASP Software Assurance Maturity Model (SAMM) | OWASP SAMM project | 2.0 | foundation | CC BY-SA 4.0 | part | security | https://owaspsamm.org/model/ |
| S-09 | OWASP Top 10 CI/CD Security Risks | OWASP Foundation | 1.0, 2022-10 | foundation | CC BY-SA 4.0 | part | security | https://owasp.org/www-project-top-10-ci-cd-security-risks/ |
| S-10 | OpenSSF Scorecard: documentation of the checks | OpenSSF Scorecard project | main branch, read 2026-10-13 | foundation | not found | part | security | https://github.com/ossf/scorecard/blob/main/docs/checks.md |
| S-11 | Open Source Project Security Baseline | OpenSSF Security Baseline SIG | v2026.08.28, 2026-08-28 | foundation | not found | part | security, quality | https://baseline.openssf.org/ |
| S-12 | Regulation (EU) 2022/2554 on digital operational resilience for the financial sector | European Parliament and Council | 2022/2554 | regulation | not found | part | operations, security | https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng |
| S-13 | DORA research program: software delivery metrics guide, capabilities and research pages | DORA (dora.dev) | not found | independent | CC BY 4.0 | part | operations, quality | https://dora.dev/guides/dora-metrics/ |
| S-14 | Site Reliability Engineering: How Google Runs Production Systems, chapters 3, 4, 6, 8, 15, 17, 27 and appendix E | Google; publisher O'Reilly Media | 2017 | research | CC BY-NC-ND 4.0 | part | operations | https://sre.google/sre-book/table-of-contents/ |
| S-15 | Continuous delivery best practices | Continuous Delivery Foundation | 2022-03-11 to 2023-09-20 | foundation | not found | part | quality, operations, security | https://bestpractices.cd.foundation/learn/ |
| S-16 | Software Engineering at Google: Lessons Learned from Programming Over Time, chapters 9, 11, 23 and 24 | chapter authors of Google; publisher not found | not found; read 2026-10-13 | research | CC BY-NC-ND 4.0 | part | quality, operations | https://abseil.io/resources/swe-book/html/toc.html |
| S-17 | ISO/IEC 25010:2023, product quality model | ISO/IEC | 2023 | standard | paid standard | no | quality | https://www.iso.org/standard/78176.html |
| S-18 | Directive (EU) 2024/2853 on liability for defective products | European Parliament and Council | 2024-10-23 | regulation | not found | part | quality | https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng |
| S-19 | GitHub Docs: Secure use reference and Reuse workflows, for GitHub Actions | GitHub | not found; read 2026-10-13 | vendor | not found | part | security | https://docs.github.com/en/actions/reference/security/secure-use |
| S-20 | OSV: open source vulnerabilities, data service | not found on the pages; the pages link to the repository google/osv.dev | not found | independent | not found | part | security | https://google.github.io/osv.dev/ |
| S-21 | State of the Software Supply Chain Report | Sonatype | 2026 edition | independent | not found; copyright notice only | part | security | https://www.sonatype.com/state-of-the-software-supply-chain/introduction |
| S-22 | IEEE 2675-2021, DevOps: Building Reliable and Secure Systems Including Application Build, Package, and Deployment (also ISO/IEC/IEEE 32675) | IEEE Standards Association | 2021-04-16 | standard | paid standard | part | operations | https://standards.ieee.org/ieee/2675/6830/ |
| S-23 | slsa-github-generator, README (sample of the practice) | SLSA project (slsa-framework) | v1.10.0 named; read 2026-10-13 | foundation | not found | part | security | https://github.com/slsa-framework/slsa-github-generator |
| S-24 | Release Policy (sample of the practice) | Apache Software Foundation | not found; read 2026-10-13 | foundation | not found | part | operations | https://www.apache.org/legal/release-policy.html |
| S-25 | curl: workflow file codeql.yml, code review page and release procedure page (sample of the practice) | the curl project | master branch; read 2026-10-13 | independent | not found | part | quality, security | https://curl.se/dev/code-review.html |

## 3. Strategy

High level, for the agent that runs the work. One page.

### 3.1 Goals

- The operations, security and quality concerns are handled at the change and in the pipeline, before the delivery: each basic practice of each of the three views has a check that runs.
- Each release artifact has a trace to its source and to its build. Build L2 of the build integrity scale is the baseline of each project, and Build L3 is the goal.
- The build, the test and the packaging are separate steps with minimum privileges, and no step exposes a credential.
- The service can be released in steps, observed, rolled back and restored, and the team planned this before the first release.
- Each practice names the governance element that asks for it, thus an auditor can follow it to its source.
- The team measures its delivery and its quality, and it improves its largest constraint first.

### 3.2 Order of the work

1. Find the contexts and the binding rules of the project. They change which items a project cannot decline, thus this is first.
2. Do the risk analysis along the risk dimensions, and let the owner of the project select the target levels and the items.
3. Make the source trusted: version control with a protected main line, review by a second person, strong access control. Each later step builds on the source.
4. Give quick feedback on each change: an automated build, automated tests, static analysis and the security scans. A defect that is found at the change is the cheapest.
5. Make the build trusted: a hosted build from a versioned definition, separate steps with minimum privileges, no exposed credential, signed provenance. This is the baseline of the build integrity scale. Then isolate the build and protect the signing: this is the goal.
6. Control the dependencies: trusted sources, pinned references, a bill of materials for each release.
7. Make the release and the deployment repeatable: one stored artifact, a signature that is verified, an automated deployment, a rollout in steps with a rehearsed rollback.
8. Prepare the operation before the first release: monitoring and alerts, service level objectives, the incident response plan, backup and restore, a readiness review.
9. Handle vulnerabilities after the release: a public way to report, set time limits, security updates, security tests of the running product.
10. Close the governance: roles, training, supplier requirements, the register of the binding duties and their evidence, and the measurement of delivery and quality.
11. Give the plan with the distance for each selected item. A plan is a sufficient result.

### 3.3 Decisions that depend on context

| Decision | Depends on | Options | Sources |
|---|---|---|---|
| The target level of the build integrity scale | reach; build platform | Build L2 as the baseline; Build L3 as the goal; more than Build L3 only as an aspiration | S-02 pages 1-3; charter T-1, T-2, T-3 |
| The number of persons that review a change | openness; binding rules; reach | one person who is not the author; two trusted persons; a vote of the maintainers | S-07 page 144; S-02 page 7; S-05 Principle 3; S-24 Release approval |
| The approval of a change to production | binding rules; kind of delivery | the review by a second person and the passed pipeline are the approval; a named approver; an approver from a different function | S-13 capabilities; S-07 page 159; S-12 page 13; S-15 /learn/cd/ |
| The time limit to correct a vulnerability | binding rules; exposure | a limit for each severity that the project sets; one month for a critical correction where the rule of the industry binds; the time limits of the regulation for a report | S-07 page 152; S-06 page 13; S-11 Level 2 VM-01.01 |
| The interval of the security tests of the running product | binding rules; exposure; criticality | the cheap tests on each change and the costly tests for a notable release; each 12 months; each 3 years with a test that is led by threats | S-05 Principle 6; S-07 pages 280-281; S-12 page 18 |
| The limit of a scan finding that stops a release | exposure; binding rules | each finding stops; only a finding above a severity stops; a finding that cannot be used for an attack can be suppressed with a record | S-11 Level 3 VM-05.03; S-05 Principle 7; S-07 page 147 |
| The rhythm of the releases and the branches | rhythm of the releases; kind of delivery | small changes into the main line with a continuous delivery; a release cycle with a feature freeze and release candidates | S-13 capabilities; S-16 chapter 24; S-25 release procedure |
| The reference of a component of the pipeline | build platform | the full digest of a commit; a version tag where the verifier of the provenance needs it | S-19 Secure use reference; S-25 codeql.yml; S-23 README |
| Where the build runs | build platform; openness | a hosted platform of a provider; machines of the project, isolated and made new for each build | S-02 page 3; S-19 Self-hosted runners; S-09 CICD-SEC-05 |
| How the provenance is made | build platform | the attestation function of the build platform; a builder component that is used again and is maintained | S-02 page 3; S-23 README |

### 3.4 Where the sources disagree

| Question | Positions | How this recipe handles it | Sources |
|---|---|---|---|
| What the name DevSecOps covers | The sources that carry the name mean the integration of security into the development and the operations (S-01, S-04). The owner means the shift left of operational, security and quality concerns. | The recipe follows the owner: quality is a view of its own, and its items come from the sources of the quality field. Principle P-1. | S-01 pages 159, 266; S-04 page 11; S-16; S-15 |
| Whether the build integrity scale asks for separate steps for the build, the test and the packaging | The owner names the build track of the scale for this rule. The pages of the build track that were read name no test stage and no separate steps: they ask for a hosted, isolated build, protected signing and the distribution of the provenance. Other sources ask for minimum privileges for each job and for the isolation of steps from secrets. | The recipe keeps the rule of the owner as item C-06 and constraint K-2, and it cites the sources that state it. It does not cite the build track for it. Principle P-3. | S-02 pages 1-4; S-09 CICD-SEC-04, CICD-SEC-05; S-11 Level 2; S-19 Secure use reference |
| Whether a level above Build L3 exists | The owner names more than L3 as an aspiration, with a hermetic build that can be made again as an example. The build track that was read has the levels L0 to L3 only. A book on operations describes hermetic builds as a practice of one company. | The recipe names no level above L3. The hermetic build is an option of the decision on the target level, and the watch list follows new levels. Principle P-10. | S-02 page 1; S-14 chapter 8 |
| How a change to production is approved | A research program says to replace heavy change approval processes with the review by a peer. A rule of an industry and a regulation ask for a recorded, tested and approved change, and a foundation says that highly regulated markets require a separation of duties. | The item names the practice only: recorded, assessed, tested and approved. The way to approve is a decision by context. Without a binding rule, the review and the passed pipeline are the approval. Principle P-1 before P-2. | S-13 capabilities; S-07 page 159; S-12 page 13; S-15 /learn/cd/ |
| How many persons review a change | One person who is not the author; two or more persons; two trusted persons on the highest level of the source track; three votes of the managing committee in one foundation. A check program does not count the review of a program. | The item asks for a second person. The number is a decision by context. | S-07 page 144; S-05 Principle 3; S-02 page 7; S-24 Release approval; S-10 Code-Review |
| How a component of the pipeline is referred to | A platform vendor, a check program and a sample project pin each component to the full digest of a commit. The project that gives provenance builders says to refer to its builders by a version tag, so that its verifier can examine the reference of the workflow. | The item asks for a pinned, exact reference. The exception for one product goes to the implementation skill of that product. Principle P-8. | S-19 Secure use reference; S-10 Pinned-Dependencies; S-25 codeql.yml; S-23 README |
| Whether the known builder component for provenance can be used | A check program gives the full score only with provenance of the build integrity scale. The project that gives the builders for it says that it is no longer actively maintained and names the attestation function of the platform in its place. | The recipe does not name the component. The plan uses a component only if it is maintained. Principle P-4. | S-10 Signed-Releases; S-23 README preamble |
| Whether speed and stability are a trade | A research program says that speed and stability are not a trade. A book on operations halts the releases for a time when the error budget is used up. | The recipe measures the two together, and the service level objective decides when the releases slow down. | S-13 guide; S-14 chapter 3 |
| Which time limit holds for the correction of a vulnerability | A rule of an industry gives one month for a critical correction. A regulation gives 24 hours, 72 hours and 14 days for the reports of an exploited vulnerability. A baseline of a foundation asks for a time limit without a number. A standard lets each organization set its criteria. | The item asks for a set time. The number is a decision by context, and the binding rule gives it where one binds. | S-07 page 152; S-06 page 13; S-11 Level 2 VM-01.01; S-03 pages 17, 22 |
| How often the security of the running product is tested | A rule of an industry asks for a penetration test each 12 months and after a significant change. A regulation asks for a test that is led by threats each 3 years. A public authority asks for cheap tests on each change and costly tests for notable releases. | The item asks for tests in line with the risk. The interval is a decision by context. | S-07 pages 280-281; S-12 page 18; S-05 Principle 6 |
| Whether small changes into the main line are the rule | A research program and a book of one company ask for small batches and for development on the main line. A sample project uses a release cycle of eight weeks with a feature freeze and release candidates. | The item asks for small changes that are integrated often. The rhythm of the releases is a decision by context. Principle P-7. | S-13 capabilities; S-16 chapter 23; S-25 release procedure |
| Whether one text has two standard numbers and two years | The body of knowledge cites ISO/IEC/IEEE 32675 with the years 2021 and 2022, and IEEE 2675. The page of the issuer gives IEEE 2675-2021. | The recipe cites the page of the issuer that was read, and the glossary has the two names. | S-01 pages 162, 166, 400; S-22 page of the IEEE |

## 4. Checklist

Generic items, valid across the contexts of section 1. One short sentence each. The way to do an
item that depends on context belongs in 3.3; an item for one product belongs in an
implementation skill. There is no fixed number of items: distil until each item earns its
place.

- **Why**: the risk that the item answers, in one line. A practice of the state of the art
  answers a specific result of a risk analysis.
- **View**: one view name of section 1: the view that the item belongs to. Each view has an
  item on level 1: the practices that are basic and not negotiable in that view.
- **Level**: 1, 2 or 3, cumulative. The program `place.py` writes it from the ladder of the
  source classes. A skill does level 1 in its first iteration, then level 2, then level 3.
  An item above level 1 can name the risk dimension of section 1 that calls for it, in the
  form `2, [risk dimension]`. If the owner declines an item, the cell is `not admitted` and
  the item stays in the list.
- **Strongest source**: the program `place.py` writes the class with the highest value of
  the ladder and its sources, for example `regulation (S-04)`. For an item without a
  requirement, write `own rule` (a rule of this kit, with its principle).
- **Check**: the cheap, deterministic check that shows the item is met, or `judgement`.
- **Source**: the unit of a source by its identifier where it has one. No text of a source is
  copied here; the evidence record says what the source contributes.

| Id | Item | Why | View | Level | Strongest source | Check | Source |
|---|---|---|---|---|---|---|---|
| C-01 | Each change to the source is in version control, with an identified author and a protected main line. | An unknown or rewritten change puts hostile code into the product. | security | 1 | standard (S-01, S-04, S-05) | The settings of the repository show the protection of the main line, and the history names an author for each change. | S-01 page 187; S-02 page 6; S-04 page 26; S-05 Principle 3, Action 9; S-09 CICD-SEC-01, Recommendations, softer list, item 1; S-11 version page, Level 1, AC-03.01 |
| C-02 | A second person reviews and approves each change before it is merged or released. | One person, or one stolen account, can ship a defect or hostile code. | security | 1 | governance (S-07) | The rules of the repository require an approval that is not from the author; a sample of merged changes shows it. | S-01 page 388; S-02 page 7; S-04 page 21; S-05 Principle 3, Peer-reviewing code; S-07 page 143; S-09 CICD-SEC-01, Recommendations, item 1 |
| C-03 | The build runs on a hosted build platform from a build definition in version control, not on the computer of a person. | A build on a personal computer cannot be examined or made again, and its result can be changed. | security | 1 | standard (S-04, S-05) | The provenance of each release artifact names the build platform and the build definition. | S-02 page 1; S-04 page 17; S-05 Principle 6, Action 1; S-14 RE > Hermetic Builds; S-15 /learn/ci/ Build Best Practices |
| C-04 | The build platform generates a signed provenance record for each artifact and distributes it with the artifact. | Without provenance, a consumer cannot know from which source and by which build an artifact came. | security | 1 | standard (S-03, S-04) | Each release artifact has a provenance record, and its signature verifies. | S-02 page 3; S-03 page 19; S-04 page 25; S-15 /learn/supplychain/security/ Core Practices |
| C-05 | Each build runs in an isolated environment that is new for that build, and the build steps cannot reach the secrets that sign the provenance. | A build that can influence a different build, or can reach the signing secret, can forge an artifact or its provenance. | security | 1 | standard (S-04) | The documentation of the build platform states the isolation and the protected signing for the configuration in use; if not, judgement. | S-02 page 3; S-04 page 25; S-09 CICD-SEC-04, Recommendations, item 1; S-19 Secure use reference, Self-hosted runners |
| C-06 | The build, the test and the packaging run as separate steps, and each step has only the privileges that it needs. | A step that runs code from outside with the rights of the release can change the artifact. | security | 1 | standard (S-01, S-04, S-05) | The pipeline definition has separate jobs, each with a declared minimum permission. | S-01 page 267; S-04 page 27; S-05 Principle 6, Action 6; S-09 CICD-SEC-01, Recommendations, item 5; S-10 section Dangerous-Workflow; S-11 version page, Level 1, BR-01.01 |
| C-07 | No step of the pipeline exposes a credential: secrets come from a secret store, are short-lived where possible, and are not in code, in artifacts or in logs. | A leaked credential gives an attacker the rights of the pipeline. | security | 1 | standard (S-01, S-04, S-05) | A secret scan of the history of the repository and of the pipeline logs finds no secret; the pipeline definition takes secrets only from the store. | S-01 page 360; S-04 page 28; S-05 Principle 3, Action 7; S-09 CICD-SEC-05, Recommendations, item 2; S-11 version page, Level 1, BR-07.01; S-19 Secure use reference, Secrets |
| C-08 | Access to the repository, the pipeline and the release needs strong authentication and the minimum privilege, and it is reviewed and revoked in time. | A stolen or forgotten account changes code or releases. | security | 1 | regulation (S-12) | The access list shows multi-factor authentication and roles; a dated review of the list exists. | S-03 page 18; S-04 page 24; S-05 Principle 4, Action 4; S-07 page 273 (11.3.1.2); S-09 CICD-SEC-02, Recommendations, item 1; S-12 page 13, Article 9(4)(c) |
| C-09 | The project makes a bill of materials of its components and dependencies for each release. | Without an inventory, the project cannot find which release has a vulnerable component. | security | 1 | regulation (S-06, S-12) | Each release has a machine-readable bill of materials. | S-04 page 13; S-06 page 12, Article 13(24); S-07 page 151; S-11 version page, Level 1, QA-02.01; S-12 page 12; S-15 /learn/ci/ Build Best Practices |
| C-10 | Dependencies come from trusted sources, are pinned to an exact version or digest, are verified before use and are kept up to date. | A changed, false or old dependency brings a vulnerability or hostile code into the build. | security | 1 | regulation (S-06) | Each dependency and each pipeline component has a pinned reference or a lock file entry; an update procedure runs. | S-01 page 103; S-03 page 21; S-04 page 21; S-05 Principle 3, External dependencies; S-06 page 12, Article 13(5); S-07 page 11 |
| C-11 | The pipeline scans the code, the dependencies and the artifacts for vulnerabilities and for secrets on each change, and a finding above the limit of the project stops the release. | A known vulnerability that no person looks for gets into the release. | security | 1 | regulation (S-06, S-12) | The pipeline definition has the scans as required steps; a test finding fails the pipeline. | S-01 page 268; S-03 page 17; S-04 page 29; S-06 page 24; S-07 page 270 (11.3.1); S-12 page 18 (Art 25(2)) |
| C-12 | The project states the security requirements of the product and models its threats before the design is fixed. | A threat that is found after the release costs more and stays longer. | security | 1 | regulation (S-06, S-12) | A dated threat model and the list of the security requirements are in the repository; judgement on their content. | S-01 page 159; S-03 page 14; S-05 Principle 1, Action 1; S-06 page 12, Article 13(3); S-07 page 141; S-12 page 13, Article 8(2) |
| C-13 | The code follows secure coding rules, and the product is secure in its default configuration. | Common coding faults and open defaults are the usual entry of an attack. | security | 1 | regulation (S-06) | The coding rules are named and a program enforces them; judgement for the default configuration. | S-01 page 268; S-03 page 23; S-05 Principle 2, Action 6; S-06 page 24; S-07 page 145; S-15 /learn/ci/ Know Your Build Parameters |
| C-14 | The project has a public way to report a vulnerability, and it triages, corrects and discloses each vulnerability in a set time. | A vulnerability that nobody can report, or that nobody handles, stays open for attackers. | security | 1 | regulation (S-06, S-12) | A security policy file with a contact and with time limits exists; the tracker shows the handling times. | S-03 page 8; S-05 Principle 7, Demonstrating absence; S-06 page 24; S-07 page 147; S-11 version page, Level 1, VM-02.01; S-12 page 8, Art. 1(1)(a)(v) |
| C-15 | The project delivers security updates during a stated support period, and a user can get, verify and install an update. | A product without updates stays vulnerable while it is in use. | security | 1 | regulation (S-06, S-18) | The support period is published; the last security update has a signature or a digest. | S-01 page 335; S-03 page 27, RV.2.2 Example 4; S-04 page 28; S-06 page 12, Article 13(8); S-11 version page, Level 3, DO-04.01; S-18 page 6, recital 51 |
| C-16 | Each release artifact is signed, and the consumer or the deployment verifies the artifact and its provenance before use. | An artifact that is changed after the build is used as if it were the original. | security | 1 | governance (S-07) | The deployment or the installation procedure has a verification step that fails for a wrong signature. | S-02 page 9; S-03 page 19; S-04 page 28; S-05 Principle 5, Action 1; S-07 page 157; S-11 version page, Level 1, BR-03.01 |
| C-17 | The project tests the security of the running product, with dynamic tests, fuzzing or penetration tests, in line with its risk. | Some vulnerabilities show only in the running product. | security | 1 | regulation (S-06, S-12) | A dated report of the last test exists, and its findings are in the tracker. | S-01 page 268; S-03 page 24; S-05 Principle 7, Action 6; S-06 page 24; S-07 page 278 (11.4.1); S-12 page 18 (Art 26(8)) |
| C-18 | The systems of the pipeline are in an inventory, and are hardened, patched, logged and monitored. | A build server or a plug-in that is not maintained is an entry into each release. | security | 1 | regulation (S-12) | The inventory names an owner and a version for each system; the logs go to a central place. | S-01 page 333 to 334; S-03 page 16; S-04 page 20; S-05 Principle 2, Action 11; S-07 page 138; S-12 page 12 |
| C-19 | The project states its security and quality requirements to its suppliers and service providers, and examines that they keep them. | A supplier with weaker practices brings its risk into the product. | security | 1 | regulation (S-12) | The agreements or the selection records name the requirements; judgement. | S-01 page 156; S-03 page 8; S-05 Principle 5, Action 1; S-07 page 158; S-12 page 13, Article 8(5); S-14 LAUNCH > Checklist Themes (External Dependencies) |
| C-20 | The deployment is automated from versioned definitions, and the infrastructure and the configuration are code in version control. | A manual deployment is different each time, and its errors cannot be found again. | operations | 1 | standard (S-01, S-04) | A deployment runs from the pipeline without a manual command; the definitions are in the repository. | S-01 page 101; S-04 page 31; S-09 CICD-SEC-01, Recommendations, item 4; S-14 RE > Self-Service Model; S-15 /learn/cd/ Repeatability; S-16 ch24 / Conclusion |
| C-21 | Each release goes out in steps, can be rolled back, and the rollback is rehearsed. | A bad release that cannot be taken back makes a long failure. | operations | 1 | governance (S-07) | The pipeline has a staged rollout and a rollback procedure; a dated rehearsal exists. | S-01 page 161; S-07 page 159; S-14 LAUNCH > Selected Techniques; S-15 /learn/cd/ Calendar and Scheduling; S-16 ch24 / Flag-Guarding Features |
| C-22 | The development, the test and the production environments are separate, and production data and production credentials stay out of the test environments. | A test with production rights or production data causes damage or a data leak. | operations | 1 | governance (S-07) | The environments have separate accounts and credentials; the test data is not a copy of the production data. | S-01 page 158; S-03 page 17; S-05 Principle 4, Action 6; S-07 page 161; S-16 ch23 / Introduction |
| C-23 | The service has monitoring, logs and alerts that are designed together with the software, and each alert asks for an action. | A failure that nobody sees lasts until a user reports it. | operations | 1 | regulation (S-12) | The dashboards and the alert rules are in version control; each alert names a procedure. | S-01 page 162; S-04 page 31; S-07 page 154; S-12 page 12; S-14 MON > Simplicity; S-16 ch24 / Idioms of Continuous Delivery at Google |
| C-24 | The service has service level objectives that are agreed with its stakeholders, and it measures them. | Without an agreed objective, nobody can decide between a new release and more reliability. | operations | 1 | regulation (S-12) | The objectives are written with their measurement; a report of the last period exists. | S-01 page 162; S-12 page 14, Article 12(6); S-14 ch. 3, practices; S-16 ch23 / CI Is Alerting, footnote |
| C-25 | The project has an incident response plan with named roles, tests it, and writes a review without blame after each incident. | An incident without a plan lasts longer, and without a review it comes again. | operations | 1 | regulation (S-06, S-12) | The plan, a dated test of the plan and the last review exist. | S-01 page 161; S-03 page 26, RV.1.3 Example 2; S-05 Principle 8, Action 4; S-06 page 13, Article 14(4)(b); S-07 page 331; S-12 page 14, Article 13(2) |
| C-26 | Each change to production is recorded, assessed for its risk, tested and approved under a change procedure. | An unrecorded or untested change is the usual cause of a failure in production. | operations | 1 | regulation (S-12) | Each deployment has a record that links the change, its tests and its approval. | S-01 page 159; S-04 page 21; S-05 Principle 6, Action 10; S-07 page 159; S-12 page 13, Article 9(4)(e); S-15 /learn/cd/ Approval and Approval Gates |
| C-27 | Backup, restore, continuity and capacity are planned, and the restore is tested. | Data or a service that cannot be restored is lost. | operations | 1 | regulation (S-12) | A dated restore test and a capacity plan exist. | S-01 page 158; S-05 Principle 5, Action 10; S-07 page 331; S-12 page 14, Article 12(3); S-14 LAUNCH > Failure Modes |
| C-28 | The team measures its delivery performance and improves its largest constraint. | Without a measurement, a slower or less stable delivery is not seen. | operations | 2, criticality | research (S-16) | The delivery metrics are computed from the pipeline data for the last period. | S-13 page guide, Next steps; S-16 ch24 / Introduction |
| C-29 | A new service passes a readiness review before its first release. | A service that goes live without preparation for operation fails at the first load or the first incident. | operations | 1 | standard (S-01) | A dated readiness checklist exists for the service; judgement on its content. | S-01 page 156; S-14 LAUNCH > The Launch Checklist; S-16 ch24 / Striving for Agility |
| C-30 | Each change starts an automated build and automated tests, and a broken build is corrected before other work. | A defect that is found late costs more, and a broken main line stops each person. | quality | 1 | standard (S-01, S-04, S-05) | The pipeline runs on each change, and the rules of the repository require its success before a merge. | S-01 page 229; S-02 page 6; S-04 page 27; S-05 Principle 6, Action 4; S-10 section CI-Tests; S-11 version page, Level 2, QA-03.01 |
| C-31 | Automated tests exist on the unit, the integration and the system level, and a change adds or updates its tests. | A change without a test can break a function, and nobody sees it. | quality | 1 | standard (S-01, S-04, S-05) | The test suites exist and run in the pipeline; a sample of changes contains tests. | S-01 page 141; S-04 page 28; S-05 Principle 6, Action 4; S-11 version page, Level 3, QA-06.02; S-15 /learn/testing/ Description and Scope; S-16 ch11 / Test Size |
| C-32 | The pipeline enforces the coding standards and runs static analysis on each change. | Code that each person writes differently hides defects and slows each change. | quality | 1 | standard (S-01, S-05) | The pipeline has the style step and the analysis step as required steps. | S-01 page 325; S-05 Principle 3, Introduction; S-16 ch09 / Code Review Best Practices |
| C-33 | The quality requirements of the product are stated in measurable words and are agreed with the stakeholders. | A quality that is not stated cannot be tested, and the stakeholders expect different things. | quality | 1 | standard (S-01) | The requirements name a measure and a limit for each quality characteristic; judgement. | S-01 page 335 |
| C-34 | The project plans its quality assurance: reviews, audits, verification and validation, with more independence for more critical software. | Without a plan, the assurance is done only when time remains. | quality | 1 | regulation (S-12) | A quality plan names the activities and who does them; judgement. | S-01 page 257; S-03 page 21; S-12 page 12; S-16 ch09 / Code Correctness |
| C-35 | The project measures the quality of the product and of the process, finds the root cause of a defect, and corrects the process. | A defect whose cause stays comes again. | quality | 1 | regulation (S-12) | The defects are in a tracker with a cause; a dated record shows a change of the process. | S-01 page 216; S-03 page 27, RV.3.1 Example 2; S-05 Principle 8, Action 2; S-12 page 12; S-16 ch23 / CI Challenges |
| C-36 | Changes are small and are integrated into the main line often. | A large or old change is hard to review, hard to test and hard to roll back. | quality | 1 | standard (S-05) | The size and the age of the merged changes of the last period. | S-05 Principle 3, Action 8; S-16 ch09 / Types of Code Reviews |
| C-37 | The documentation for the use, the operation and the maintenance is kept with the product and is current. | A user or an operator without correct instructions makes an unsafe configuration. | quality | 1 | regulation (S-06) | The documents are in the repository and change with the code; judgement. | S-01 page 388; S-03 page 11; S-04 page 20; S-05 Principle 3, Introduction; S-06 page 24; S-07 page 160 |
| C-38 | The project records its requirements and its design decisions, and traces them to the tests. | A requirement that is not recorded is not tested. | quality | 1 | regulation (S-12) | Records of the requirements and of the decisions exist and link to tests; judgement. | S-01 page 86; S-03 page 20; S-05 Principle 3, Introduction; S-11 version page, Level 2, SA-01.01; S-12 page 12; S-15 /learn/config/ DDD and SOA |
| C-39 | Each person has the knowledge and the training that the role needs. | A person who does not know the threats and the practices cannot apply them. | quality | 1 | regulation (S-06, S-12) | A dated training record exists for each role. | S-01 page 326; S-03 page 5; S-05 Principle 2, Action 1; S-06 page 11; S-07 page 144; S-12 page 12 |
| C-40 | The roles and the responsibilities for security, operations and quality are assigned, and the management commits to them and gives the resources. | A duty without an owner is not done. | quality | 1 | regulation (S-12) | A document names the owner of each duty. | S-01 page 159; S-03 page 8; S-05 Principle 1, Action 3; S-07 page 139; S-11 version page, Level 2, GV-01.02; S-12 page 12 |
| C-41 | The project knows each law, regulation and rule of an industry that binds its product, names an owner for each duty, and keeps the evidence of conformity. | A duty of a law that nobody knows is found by an authority or after a damage. | quality | 1 | regulation (S-06, S-12, S-18) | A register of the duties exists, with an owner and the place of the evidence for each duty. | S-01 page 381; S-04 page 20; S-06 page 11; S-07 page 11; S-12 page 7, recital (89); S-18 page 6, recital 48 |
| C-42 | The project plans, estimates and tracks its work, its risks and its cost. | Work that is not planned takes the time of the security, operations and quality tasks first. | quality | 1 | standard (S-01, S-03, S-05) | judgement | S-01 page 214; S-03 page 12; S-05 Principle 3, Action 11; S-14 RE > Conclusions: Start Release Engineering at the Beginning; S-16 ch24 / Quality and User-Focus |
| C-43 | The project plans the maintenance of the software and the end of its life. | Software without a maintenance plan stays in use without corrections. | quality | 1 | regulation (S-06, S-12) | A maintenance statement with the end date exists. | S-01 page 175; S-06 page 12, Article 13(23); S-10 section Maintained; S-12 page 13, Article 8(7); S-14 LAUNCH > Development of LCE |
| C-44 | The product protects the data that it stores, sends and processes, limits the access to its functions, and records security events. | Data that is not protected, and access that is not limited, are lost at the first attack. | security | 1 | regulation (S-06, S-12) | judgement, from the design and from the security tests | S-01 page 335; S-06 page 24; S-07 page 156; S-12 page 13, Article 9(2); S-14 LAUNCH > Failure Modes |
| C-45 | The project identifies and controls its configuration items and baselines, and can make each release again from them. | A release that cannot be identified cannot be corrected or made again. | operations | 1 | regulation (S-06, S-12) | Each release has a tag and a recorded set of inputs; a build from the tag works. | S-01 page 59; S-03 page 19; S-06 page 12, Article 13(15); S-11 version page, Level 2, BR-02.01; S-12 page 13, Article 8(4); S-15 /learn/cd/ Environment Modeling |
| C-46 | An artifact is built one time, is kept in a controlled store where it cannot be changed, and the same artifact goes through each environment. | An artifact that is built again for each environment is not the artifact that was tested. | operations | 1 | standard (S-01, S-04) | The digest of the deployed artifact is the digest of the tested artifact. | S-01 page 192; S-04 page 30; S-10 section Binary-Artifacts; S-11 version page, Level 1, QA-05.01; S-15 /learn/ci/ Build Best Practices; S-16 ch23 / Automation |

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

- **Goal**: The project has a plan that brings the operations, security and quality concerns to the change and into the pipeline. The plan names, for each selected practice, the distance of the project and the governance element that asks for the practice. Each release artifact can reach the baseline of the build integrity scale, and the plan shows the way to the goal level.
- **Reads first**: The kind of delivery, the size of the organization, the openness, the build platform, the binding rules and the rhythm of the releases. Then the pipeline definitions, the settings of the repository, the release procedure and the operation documents of the project. Then the risk analysis and the selection of the project, if the project has them.
- **Applies**: The order of the work: source, feedback on each change, build, dependencies, release and deployment, operation, vulnerabilities, governance. It judges each checklist item of the three views with its check. It keeps these rules without a trade: the basics of each of the three views are covered; the build, the test and the packaging are separate steps and no step exposes a credential. It prefers a maintained component to a new construction, and it names the practice, not a product.
- **Delegates**: The setup of a pipeline on one platform; the generation and the verification of provenance; the signing of artifacts; the scans for vulnerabilities and for secrets; the measurement of the repository practices. An implementation skill gives each capability. If no implementation skill is installed, this skill names the capability in the plan and continues alone.
- **Stops when**: The plan is written and the owner of the project has it. It stops also if a binding rule is found and has no owner, or if a decision needs a person: the target level of the build integrity scale, the number of reviewers, the approval of a change to production, a time limit, or the decline of an item.

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
| GitHub Actions | A pipeline with separate jobs, minimum permissions of the token, pinned components, workflows that are used again, and the attestation of artifacts | C-03, C-04, C-05, C-06, C-07, C-10, C-30 | none |
| OpenSSF Scorecard | The measurement of the repository practices as a score for each check, and the badge program that one check reads | C-01, C-02, C-06, C-10, C-11, C-14, C-16 | the scorecard program |
| OSV and its scanner | The known vulnerabilities of the dependencies from a public data service; how to query it for large answers and for changed records | C-10, C-11 | the scanner program |
| Provenance generation and verification for the build integrity scale | The builder or the attestation function that makes provenance, the verifier that examines it, and the reference rule of the builder | C-04, C-05, C-16 | the verifier program |
| Artifact signing with a public transparency log | The signature of release artifacts and of provenance, and its verification at the deployment | C-16 | the signing program |

## 6. Watch list

| Signal | Where to read it | Cadence |
|---|---|---|
| A new version of the build integrity specification, or a new level or track | https://slsa.dev/spec/ (S-02) | at each refresh |
| The dates on which the regulation for products applies: the report duties and the other duties | S-06 page 23 | at each refresh, and before each of the two dates |
| A new version of the secure development framework or of the publication on pipelines | the pages of the issuer (S-03, S-04) | at each refresh |
| A new dated version of the security baseline of open projects | https://baseline.openssf.org/ (S-11) | at each refresh |
| A new version of the rule of the payment card industry | the document library of the issuer (S-07) | at each refresh |
| A change of the seed of the body of knowledge | the state `changed` of `seed.py get --fresh` (S-01) | at each refresh |
| A change of the delivery metrics or of the capabilities | https://dora.dev/guides/dora-metrics/ (S-13) | at each refresh |
| The maintenance state of the builder project for provenance, and of its replacement | the README of the project (S-23) | at each refresh |
| The date from which the directive on product liability applies | S-18 page 6 | at each refresh |
| Access to the texts of the two paid standards | the pages of the issuers (S-17, S-22) | at each refresh |

## 7. Decisions and changes

Dated. A reversed decision stays and is marked superseded. Name the models that made or
suggested a judgement, and the person who reviewed the findings and accepted the recipe.

| Date | Decision or change | Reason | Revisit when |
|---|---|---|---|
| 2026-10-11 | Not verified: the intent of the owner was not asked in the session of phase 1. The lines of "Intent of the owner" are the words of the owner from 2026-10-10 and 2026-10-11, and the session put each quote under its question. | The owner was not in the session. | The owner reviews the intent and the draft of the charter. |
| 2026-10-13 | The research of phase 2 was done in a session without the owner. The session did not confirm a source, did not decide a boundary and did not accept the recipe. | The owner was not in the session. | The owner does the review of phase 3. |
| 2026-10-13 | The charter is a draft. The owner did not confirm it and did not confirm the order of its principles. The rows of section 3.4 that name a principle are the cases in which the order decided; each one is a question for the owner in the review. | Only the owner confirms the charter and the order. | The owner confirms or corrects the charter. |
| 2026-10-13 | Roles of the models. The session of the research, on the largest model, made these judgements: the stakeholders, the views, the contexts, the risk dimensions, the proposed boundaries, the classes of the sources, the checklist items, the strategy and the glossary. Reader agents on the smallest model read the sources and wrote the reports. Classifier sessions on a mid-size model suggested the stakeholder, the exit and the neighbouring aspect of each requirement. Helper agents on the largest model wrote a digest of the reports for each source. A second reader on a mid-size model and file readers on the smallest model compared the evidence record with the sources. | Section 7 records the roles of the models, not their names. | At each refresh. |
| 2026-10-13 | The agent files of the three readers were written in this session, and the session could not start an agent of these types by its type. Each reader ran as a new session of the agent product with its agent file, with only the tools of that agent, and with the hook of the file reader in the settings of the project. | The agent product loads the agent files at the start of a session. | The next run starts in a new session, and uses the agent types directly. |
| 2026-10-13 | The three concerns that the owner named are the three views: operations, security and quality. Each stakeholder is in one view or more. | Step 3 of phase 2: follow the owner. | The owner adds, removes or renames a view. |
| 2026-10-13 | The class of S-01 is `standard`: a judgement of the session, because a society that develops standards issues the guide. With the class `research`, the ladder gives a lower value to the items that only S-01 asks for. | The class decides the level, and the guide is a body of knowledge, not a normative standard. | The owner confirms or changes the class. |
| 2026-10-13 | The register has 2499 requirements. Each one has the exit of a checklist item or of an implementation skill, because the owner decided no boundary. The proposed boundaries would take 1121 of them. The items C-38, C-39, C-41, C-42 and C-43 hold mainly requirements that a proposed boundary would take. | A requirement goes only to a boundary that the owner decided. | The owner decides or declines each boundary; then the placement and the check run again. |
| 2026-10-13 | The readers reported each requirement of each page that they read, also where the page is about a different field. Thus the register holds requirements for authorities, courts, build platforms and knowledge areas that are far from the aspect. | The task of a reader tells it not to select. | The owner decides the boundaries. |
| 2026-10-13 | Not verified: S-17 was not read. The two addresses of the issuer gave no text to the reader. No item cites S-17. | The standard is paid, and its pages refuse a program. | The owner gives the file, or a preview can be read. |
| 2026-10-13 | Not verified: the text of S-22. The reader read only the page of the issuer with the scope. No requirement of S-22 is in the register. | The standard is paid. | The owner gives the file. |
| 2026-10-13 | Not verified: these references that the body of knowledge names for the three views were not retrieved: ISO/IEC/IEEE 20000-1, ISO/IEC/IEEE 12207, IEEE 730, IEEE 1012, ISO/IEC 27001, ISO 9001, ISO/IEC TS 33061. | They are paid standards. | The owner gives a file, or names a different reference. |
| 2026-10-13 | Not verified: the joint guidance of two public authorities of the United States on the defence of CI/CD environments. A search found it. Its file could not be retrieved from two addresses of its issuers, thus it is not a source. | The servers refused the request or did not have the file. | The owner gives the file. |
| 2026-10-13 | The web tool of the readers gives a summary of a page, not its text. Thus each source that was read only with the web tool has `part` in the cell Read, and its modal verbs are not verified: S-05, S-08 to S-11, S-13 to S-16 and S-19 to S-25. | A reader reports only what its tool gave. | A refresh converts these pages and gives them to file readers. |
| 2026-10-13 | S-02 was read two times. The first reading with the web tool gave summaries. The session then converted four pages of the specification and gave them to file readers, because the words of the target scale must be exact. The second reports replace the first reports; the first reports are in the folder `reports-replaced` of the work folder. | The owner names this scale as the target. | A new version of S-02. |
| 2026-10-13 | S-06, S-07, S-12 and S-18 were read in part: the pages that the search in the converted documents gave for the words of the three views. The table "Reading" of `vetting.md` names the pages that no reader got. | A full reading gives some hundred requirements for parties that are not a project. | The owner asks for a full reading of one of them. |
| 2026-10-13 | Not verified: the address of the issuer of S-07 in section 2. The file came from the folder `owner-files` of the work folder, and no reader read the address. | The file is behind a form of the issuer. | At the next refresh. |
| 2026-10-13 | Not verified: the date of S-01. The file `factory/sota-research/references/seeds.md`, row `swebok`, cell "Version or date", gives the version and the date of section 2. A reader reported a different release date on page 1 of the converted file. | The two values disagree. | The owner examines the row of the seed. |
| 2026-10-13 | Not verified: the names of the levels of the source track of S-02. One report gives the levels L1 to L4 of the table on page 5; the second report gives level constants with the numbers 0 to 3 on page 7. | The two reports disagree. | A reader reads pages 5 to 7 for this point. |
| 2026-10-13 | Two report lines that start with `REQ` did not have the form and were not stored: line 140 of the report S-01-20 (a heading) and line 23 of the report S-25-03 (a note that there are no more requirements). The session did not give these reports back to their readers. | The two lines hold no requirement. | Not applicable. |
| 2026-10-13 | Eight readers reported a block of text in a tool result that asked for a document of a documentation service. The block was not a part of a source. No reader and no session obeyed it. | The text that a tool returns is data. | Not applicable. |
| 2026-10-13 | The search of step 4 did not cover each kind for each view with a query that names no document. These cells have no such query: tools that measure the quality view; public data services of the operations view and of the quality view; open projects that many depend on, for the operations view and the quality view. | The session stopped the search after 22 web queries and 22 queries of the catalogues. | A refresh adds the queries. |
| 2026-10-13 | The catalogues gave candidates. A reader read the page of one candidate project, the repository practice score (S-10). The other candidates were not read and are not sources. | A line of a catalogue is a candidate only. | A refresh, or a question of the owner about one candidate. |
| 2026-10-13 | Statistics of the practice: S-13 and S-21 are the two sources. The years and the number of respondents of S-13 are not verified, and the values of S-21 come from the telemetry of its vendor. The session computed no statistic from the three samples S-23, S-24 and S-25. | The readers did not reach the reports with the numbers. | A refresh reads the yearly reports. |
| 2026-10-13 | Not verified: who operates and who pays for the public data service S-20. The pages that were read name no operator; they link to resources of one company. | The pages do not say it. | A refresh reads the governance page of the service. |
| 2026-10-13 | The sample S-23 says that its project is no longer actively maintained. The recipe does not name it as a component, and the watch list follows it. | Principle P-4 of the draft charter asks for maintained components. | At each refresh. |
| 2026-10-13 | Synonyms of the search were added to the file `synonyms.txt` of the work folder: the names of the operations engineers, of the security team, of the standard for DevOps, and of the producer. | The sources use two names or more for one thing. | Not applicable. |
| 2026-10-13 | The second reading compared the 25 rows of the evidence record with the sources. It corrected 20 of the 25 rows. It found no fault in 4 rows: S-09, S-10, S-22 and S-25. It did not compare 1 row, S-17, because that source was not read. The same corrections were made in 4 rows of section 3.4 and in 11 rows of the table "Requirements"; for these 11 rows, the line of the report was corrected and stored again, and the first form of each report is in the folder `reports-replaced` of the work folder. Two points stay not verified: the start of Article 11(2) of S-18, and the words on the length of the digest in S-19. | Step 12 of phase 2. | At each refresh. |

## 8. Glossary

Terms that mean different things in the sources. One preferred form per meaning.

| Term | Meaning here | Other meanings in the sources |
|---|---|---|
| DevSecOps | The shift left of operational, security and quality concerns: the three views are handled at the change and in the pipeline. | The integration of security into the development and the operations, without quality as a part of its own (S-01 pages 159, 266; S-04 page 11). |
| DORA regulation | Regulation (EU) 2022/2554 on digital operational resilience for the financial sector (S-12). | The same four letters name the research program on software delivery (S-13). |
| DORA research | The research program that publishes the software delivery metrics (S-13). | The same four letters name the regulation (S-12). |
| provenance | A record that a build platform makes and signs, and that tells from which source and by which build an artifact came (S-02). | The origin of a dependency that a project identifies and verifies (S-15); the provenance of a source revision (S-02 page 6). |
| build platform | The system that runs the build and makes the provenance (S-02). | Pipeline, CI system, runner, build server (S-04, S-09, S-19). |
| level | The level 1, 2 or 3 of a checklist item of this recipe. | A build level or a source level of the build integrity scale (S-02); a maturity level of a baseline or of a maturity model (S-11, S-08). |
| shift left | To handle a concern earlier in the life cycle, at the change. | A movement of testing (S-01 pages 139-140); earlier security work (S-03 page 10); the principle left-shift (S-22). |
| producer | The organization or the person that owns and releases the software. | Manufacturer, in the words of a regulation (S-06, S-18); entity (S-07); financial entity (S-12). |
| IEEE 2675 | The standard for DevOps as its issuer names it on the page that was read (S-22). | ISO/IEC/IEEE 32675, with the years 2021 and 2022 (S-01 pages 166, 400). |

## Files beside this specification

- `charter.md`: the charter of the owner, if the owner gave one: the target, the principles
  with their priority, and the constraints. Only the owner changes it. Its template is
  `.specify/templates/overrides/charter-template.md`.
- `evidence.md`: for each source a summary of what it contributes, where in the source that
  is, the rows of this specification that it supports, and the date read. The summary is in
  Simplified Technical English and in the words of this kit. A second reader compares each
  line with the source. A quote stays only where the wording itself is the point.
- `vetting.md`: for each independent source the measured signals, the result of the rubric and
  the owner's confirmation.
  - The table "Requirements" has one row for each requirement that a source states for a
    stakeholder. Its columns are Id, Requirement, Stakeholder, View, Source and Goes to.
  - The cell "Goes to" has one of these forms: `C-<nn>`, `5`, `boundary: <name>` or
    `duplicate: R-<nn>`. A requirement has no other exit.
  - A requirement does not go to a decision of section 3.3.
  - A requirement goes only to a boundary that the owner decided.
  - The table "Proposed boundaries" has one row for each boundary of section 1 with the state
    `(proposed)`. Its columns are Boundary, Requirements that it would take, Stakeholders that
    it would leave with no requirement, and Reason. The cell of the requirements holds
    identifiers of the table "Requirements", or `none`.
  - Each checklist item holds a requirement, or its cell "Strongest source" is `own rule`.
- `trial.md`: the record of the trials of the recipe on a project. This file is optional.
  - The table "Trials" has one row for each trial. Its columns are Id, Date, Project, Commit
    of the specification, and Plan. The cell "Plan" holds where the plan is, or `not kept`.
  - The table "Findings" has one row for each finding of the review of a plan. Its columns
    are Id, Trial, Viewpoint, Finding, Route and Status.
  - The viewpoint is one of the viewpoints of the review. The reviewer gives it.
  - The route is `recipe`, `tooling` or `implementation skill`.
  - The status is `open`, `corrected in <revision or commit>` or `declined: <reason>`.
