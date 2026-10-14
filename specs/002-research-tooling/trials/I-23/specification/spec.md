# Aspect specification: DevSecOps

**Branch**: `001-devsecops` | **Research date**: 2026-10-12 | **Supersedes**: none | **Accepted**: pending

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
  - `software engineers`: build quality and security into the code early, get fast results from the tests, and design the software for its operation (S-01 pages 151-152, 164, 248, 264)
  - `operations engineers`: deploy, configure, monitor and restore the software, and take part in the work from its start; site reliability engineers and platform engineers are in this group (S-01 pages 152-153)
  - `security engineers`: find and decrease the security risks through the life cycle in small steps, and operate the analysis tools (S-01 pages 266, 268)
  - `quality assurance staff`: plan and do the tests, the reviews and the audits, and keep their records (S-01 pages 138, 254-255)
  - `managers`: give the policy, the resources and the roles, and decide on risk (S-01 pages 159, 251-252, 265)
  - `project maintainers`: keep an open project secure with few persons: access, reviews, releases and reports of vulnerabilities (S-09 FAQ; S-11 silver items governance and roles_responsibilities)
  - `build platform operators`: operate the platform that builds, isolates the builds and signs the provenance, and protect that platform (S-02 build track, requirements for build platforms)
  - `consumers`: know what an artefact contains and where it comes from, and verify it before use; users and customers also need the availability that was promised (S-02 verifying-artifacts; S-01 page 158)
  - `suppliers`: deliver components and services that the project controls and monitors (S-01 pages 156-157, 189)
  - `regulators and auditors`: need evidence that the practices are done; an external regulator can set constraints (S-01 pages 124, 187, 196)
- **Views**: the points of view that the aspect brings together. A view is a set of concerns
  of the aspect. The research aggregates the concerns of the stakeholders into the views. A
  concern that the owner named in the intent is in a view, or section 7 says why it is not.
  One line each: a short name, what the view is concerned with, the stakeholders whose
  concerns the view holds, and the source. Name the stakeholders in this form, before the
  source: `(stakeholders: [name], [name])`. Use the names of the field "Stakeholders".
  - `security`: the integrity of the source, of the build and of the artefacts, the secrets, the vulnerabilities and the threats, from the first change to the use of the artefact (stakeholders: software engineers, operations engineers, security engineers, managers, project maintainers, build platform operators, consumers, regulators and auditors) (S-01 pages 264-273, the knowledge area Software Security; S-03; S-02)
  - `operations`: the delivery, the release, the environments, the telemetry, the incidents and the configuration of the software, planned with its development (stakeholders: software engineers, operations engineers, security engineers, managers, project maintainers, build platform operators, consumers) (S-01 pages 151-166 and 185-201, the knowledge areas Software Engineering Operations and Software Configuration Management; S-23)
  - `quality`: the tests, the reviews, the code standards, the quality requirements and the quality plan, done early and on each change (stakeholders: software engineers, operations engineers, security engineers, quality assurance staff, managers, project maintainers, build platform operators, consumers, suppliers, regulators and auditors) (S-01 pages 117-150 and 246-263, the knowledge areas Software Testing and Software Quality; S-24)
- **Contexts**: the values of each dimension that change the strategy. One line each.
  - `kind of project`: an open project with few maintainers; an open project with many users; a product of an organization (S-09 versions page, Other Elements; S-11 gold items)
  - `size of the organization`: a very small organization of 25 persons or fewer; a larger organization with separate teams for operations, security and quality (S-01 page 163)
  - `pipeline platform`: no platform, the build is on the computer of a person; a hosted platform of a vendor; a platform that the organization operates (S-02 build-track-basics, the build levels; S-20 the part on runners)
  - `way of delivery`: a service that the team operates for its users; a package, a binary or an image that other persons install (judgement)
  - `harm of a failure`: the integrity level of the software, which the acquirer, the supplier and the developer agree on (S-01 page 251)
  - `outside duty`: no outside duty; a contract with an acquirer; a regulator that sets constraints (S-01 page 187)
- **Risk dimensions**: the dimensions on which the risk of a project differs for this aspect.
  One line each: the name, the question that finds it out, the opinion of the kit on the
  answer, and the source.
  - `consumers of the artefact`: Does a different party install or run the artefact? Opinion: if yes, do each item of this dimension, because that party cannot see the build. (S-02 build-track-basics)
  - `outside code in the pipeline`: Does the pipeline run code of outside contributors, or components of third parties? Opinion: if yes, do each item of this dimension before the pipeline gets a credential. (S-06 CICD-SEC-03 and CICD-SEC-04; S-20 Using third-party actions)
  - `credentials with production reach`: Does a pipeline job hold a credential that can publish a release or change production? Opinion: if yes, do each item of this dimension first. This is the constraint K-2 of the charter. (S-06 CICD-SEC-06; S-20 the part on secrets)
  - `duty by regulation or contract`: Does a law, a rule of an industry or a contract bind the product? Opinion: if yes, do each item of this dimension and keep the records. The regulation of this research was not read, thus ask a person who knows the duty. (S-01 pages 187, 196)
  - `operated service`: Does the team operate the software for users, with a promise on availability? Opinion: if yes, do each item of this dimension. If the project only gives a package, the items on telemetry and on incidents can wait. (S-01 page 158; S-23 the chapter Service Level Objectives)
  - `harm of a failure`: What is the worst result of a fault or of an attack for the users? Opinion: the higher the harm, the earlier the items of this dimension are done and the stricter their checks. (S-01 pages 250-251)
- **Boundaries**: what each neighbouring aspect owns, and what this aspect keeps. One line each:
  a short name, what the neighbouring aspect owns and what this aspect keeps, the state, and
  the source. A boundary has one of two states. Write the state in one of these forms, before
  the source. `(proposed)`: the research proposes the boundary, and it takes no requirement.
  `(decided by the owner on <YYYY-MM-DD>)`: the owner decided the boundary on that date, and
  a requirement can go to it. Only the owner decides a boundary. A line without a state is
  proposed.
  - `requirements engineering`: It owns how requirements are found, written and examined. This aspect keeps the security requirements and the quality requirements that must be stated early. (proposed) (S-01 pages 43-66)
  - `architecture and design`: It owns the structure of the software and its design decisions. This aspect keeps the threat model and the design for operation. (proposed) (S-01 pages 67-98)
  - `project management and process`: It owns planning, estimation, measurement, the life cycle process and the economics. This aspect keeps the plan of the quality gates and the measures of the delivery. (proposed) (S-01 pages 202-245, 288-311)
  - `professional practice`: It owns the training, the ethics and the base knowledge of the persons. This aspect keeps the assigned roles for security. (proposed) (S-01 pages 274-287, 312-386)
  - `project governance`: It owns the license, the roles, the rules for a contribution and the continuity of an open project. This aspect keeps the access rules and the review of changes. (proposed) (S-11 passing and silver items; S-09 versions page)
  - `software maintenance`: It owns the maintenance after the delivery and the end of support. This aspect keeps the correction of vulnerabilities and the release. (proposed) (S-01 pages 167-184)
- **Targets**: the measurable results that a project reaches when it applies the recipe. The
  targets come from the sources in the research; the owner can name one in the intent. One
  line each: the name, the scale with its levels, the program or the method that measures it,
  and the source of the scale. If the sources give no target, write `(none found)` in place
  of the lines.
  - `build level`: four levels of the build track, L0 to L3: L1 provenance exists, L2 a hosted build platform signs the provenance, L3 the builds are hardened. A verifier examines the signature of the provenance, the digest of the artefact and the trusted level of the builder. The owner set L2 as the baseline, L3 as the goal and more than L3 as an aspiration (S-02 build-track-basics; S-02 v1.2/verifying-artifacts, Step 1)
  - `source level`: four levels of the source track, L1 to L4, without numbers. The source control system issues a summary attestation with the verified levels, and a verifier examines it (S-02 draft/source-requirements; S-02 draft/verifying-source, Step 1)
  - `baseline level of an open project`: three levels, 1 to 3. Level 1 is for each project, level 2 for a project with two or more maintainers and some users, level 3 for a project with many users. The project attests it itself (S-09 FAQ; S-09 versions page)
  - `score of the security checks`: a score from 0 to 10 for each check and one total score from 0 to 10 with weights by risk. A program computes it from the repository (S-10 checks page; S-10 repository page)
  - `badge of best practices`: three levels: passing, silver, gold. The project answers the criteria; the pages name no program for most of them (S-11 the three criteria pages)
  - `maturity of the security practices`: three maturity levels for each security practice, and one score that the toolbox of the model computes (S-08 practice pages; S-08 assessment page)
  - `software delivery performance`: five measures without fixed limits: change lead time, deployment frequency, failed deployment recovery time, change fail rate and deployment rework rate. A quick check of the research program gives a first value (S-25 the guide; S-25 the history of the metrics)
  - `test coverage`: a value from 0 to 100 percent: the covered elements divided by all elements. The sources disagree on a required value (S-01 page 132)

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
| S-01 | Guide to the Software Engineering Body of Knowledge (SWEBOK Guide) | IEEE Computer Society | 4.0a | research | copyright of the issuer; personal and educational use | full | all | https://www.computer.org/education/bodies-of-knowledge/software-engineering |
| S-02 | SLSA specification | SLSA project (The Linux Foundation) | v1.2, and the draft | foundation | Community Specification License 1.0 | part | security | https://slsa.dev/spec/ |
| S-03 | NIST SP 800-218, Secure Software Development Framework (SSDF) | NIST | Version 1.1, 2022-02 | standard | no license; not subject to copyright in the United States | full | security | https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-218.pdf |
| S-04 | NIST SP 800-204D, Strategies for the Integration of Software Supply Chain Security in DevSecOps CI/CD Pipelines | NIST | 2024-02 | standard | no license; not subject to copyright in the United States | full | security | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204D.pdf |
| S-05 | Defending Continuous Integration/Continuous Delivery (CI/CD) Environments | NSA and CISA | not verified; searched 2026-10-12 | standard | not verified | no | security | https://media.defense.gov/2023/Jun/28/2003249466/-1/-1/0/CSI_DEFENDING_CI_CD_ENVIRONMENTS.PDF |
| S-06 | OWASP Top 10 CI/CD Security Risks | OWASP Foundation | v1.0, 2022-10 | foundation | CC BY-SA 4.0 | part | security | https://owasp.org/www-project-top-10-ci-cd-security-risks/ |
| S-07 | OWASP DevSecOps Guideline | OWASP Foundation | folder current-version, read 2026-10-12 | foundation | not found | part | security, operations | https://owasp.org/www-project-devsecops-guideline/ |
| S-08 | OWASP Software Assurance Maturity Model (SAMM) | OWASP Foundation | 2.0 | foundation | CC BY-SA 4.0 | part | security | https://owaspsamm.org/model/ |
| S-09 | Open Source Project Security Baseline (OSPS Baseline) | OpenSSF | 2026.08.28 | foundation | not found | part | security | https://baseline.openssf.org/ |
| S-10 | OpenSSF Scorecard, documentation of the checks | OpenSSF | v5, read 2026-10-12 | foundation | Apache-2.0 | part | security | https://github.com/ossf/scorecard/blob/main/docs/checks.md |
| S-11 | OpenSSF Best Practices Badge, criteria | OpenSSF | read 2026-10-12 | foundation | not found | full | security, quality | https://www.bestpractices.dev/en/criteria/0 |
| S-12 | Software Supply Chain Best Practices v2 | CNCF TAG Security | v2, 2025 | foundation | CC BY 4.0 | full | security | https://tag-security.cncf.io/community/working-groups/supply-chain-security/supply-chain-security-paper-v2/sscbpv2/ |
| S-13 | Regulation (EU) 2024/2847 (Cyber Resilience Act) | European Union | not verified; searched 2026-10-12 | regulation | not verified | no | security | https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng |
| S-14 | Software Supply Chain Security Guidance Under Executive Order (EO) 14028 Section 4e | NIST | read 2026-10-12 | standard | not found | part | security | https://www.nist.gov/document/software-supply-chain-security-guidance-under-executive-order-eo-14028-section-4e |
| S-15 | Payment Card Industry Data Security Standard (PCI DSS) | PCI Security Standards Council | v4.0.1 | governance | not found | part | security | https://www.pcisecuritystandards.org/document_library/ |
| S-16 | ISO/IEC 27001:2022, Information security management systems, Requirements | ISO and IEC | 2022 | standard | paid; copyright of the issuer | part | security | https://www.iso.org/standard/27001 |
| S-17 | ISO/IEC/IEEE 32675:2022, DevOps: Building reliable and secure systems including application build, package and deployment | ISO, IEC and IEEE | 2022-09-08 | standard | paid; copyright of the issuer | part | operations | https://standards.ieee.org/ieee/32675/10995/ |
| S-18 | ISO/IEC 25010:2023, Product quality model | ISO and IEC | not verified; searched 2026-10-12 | standard | paid | no | quality | https://www.iso.org/standard/78176.html |
| S-19 | ISO/IEC/IEEE 29119 series, Software testing | ISO/IEC JTC 1/SC 7 | read 2026-10-12 | standard | paid | part | quality | https://committee.iso.org/sites/jtc1sc7/home/projects/flagship-standards/isoiecieee-29119-series.html |
| S-20 | GitHub Actions, Secure use reference | GitHub | read 2026-10-12 | vendor | not found | full | security | https://docs.github.com/en/actions/reference/security/secure-use |
| S-21 | GitHub Actions, Reusing workflow configurations and Reuse workflows | GitHub | read 2026-10-12 | vendor | not found | full | operations | https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations |
| S-22 | GitLab, CI/CD components | GitLab | read 2026-10-12 | vendor | CC BY-SA 4.0 | full | operations | https://docs.gitlab.com/ci/components/ |
| S-23 | Site Reliability Engineering (book), four chapters and one appendix | Google, published by O'Reilly Media | 2017 | research | CC BY-NC-ND 4.0 | part | operations | https://sre.google/sre-book/release-engineering/ |
| S-24 | Software Engineering at Google (book), six chapters | Google, published by O'Reilly Media | read 2026-10-12 | research | CC BY-NC-ND 4.0 | full | quality | https://abseil.io/resources/swe-book/html/toc.html |
| S-25 | DORA, metrics guide, capabilities and research program | DORA (Google Cloud) | 2026-01-05 | independent | CC BY 4.0 | part | operations, quality | https://dora.dev/guides/dora-metrics-four-keys/ |
| S-26 | AWS Well-Architected Framework, Operational Excellence | Amazon Web Services | read 2026-10-12 | vendor | not found | part | operations | https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html |
| S-27 | OSV.dev, documentation of the service | OSV project | read 2026-10-12 | vendor | not found | full | security | https://google.github.io/osv.dev/ |
| S-28 | State of the Software Supply Chain, 10th annual report | Sonatype | 2024 | independent | all rights reserved | part | security | https://www.sonatype.com/state-of-the-software-supply-chain/2024/introduction |
| S-29 | slsa-github-generator, README | SLSA framework project | v2.1.0, 2025-02 | foundation | Apache-2.0 | part | security | https://github.com/slsa-framework/slsa-github-generator |
| S-30 | SPEC 8, Securing the Release Process | Scientific Python team | 2026 | independent | not found | part | security | https://scientific-python.org/specs/spec-0008/ |
| S-31 | Tekton Chains, documentation | Tekton project | read 2026-10-12 | foundation | not found | part | security | https://tekton.dev/docs/chains/ |
| S-32 | Reproducible Builds, documentation | Reproducible Builds project | read 2026-10-12 | independent | CC BY-SA 4.0 | part | security | https://reproducible-builds.org/docs/ |
| S-33 | in-toto, home page and specification page | in-toto project | v1.0; page changed 2024-12-16 | foundation | CC BY 4.0 | part | security | https://in-toto.io/ |
| S-34 | Sigstore, documentation | Sigstore project | read 2026-10-12 | foundation | not found | part | security | https://docs.sigstore.dev/ |
| S-35 | Test automation maturity improves product quality: quantitative study of open source projects using continuous integration | Wang, Mantyla, Liu, Markkula | v1, 2022-02-07 | research | CC BY-NC-ND 4.0 | part | quality | https://arxiv.org/abs/2202.04068 |
| S-36 | The Effects of Continuous Integration on Software Development: a Systematic Literature Review | the authors of arXiv 2103.05451 | v3, 2022-01-10 | research | arXiv non-exclusive distribution license 1.0 | full | quality | https://arxiv.org/abs/2103.05451 |

## 3. Strategy

High level, for the agent that runs the work. One page.

### 3.1 Goals

- Each concern of operations, of security and of quality has a check that runs before the delivery, and a failed check stops the change.
- A released artefact comes from a hosted build with signed provenance (build level L2). The goal is an isolated build whose signing material the build steps cannot reach (build level L3).
- The build, the test and the packaging are separate steps, and no step shows a credential to code that does not need it.
- The team can show the state of each item with a record that a program made, not with a statement of a person.
- The pipeline is made of maintained parts that other projects use also, and it changes with the repository through reviewed changes.

### 3.2 Order of the work

1. Find out the contexts and the answers to the risk questions. They decide which items come first.
2. Protect the source: version control, strong authentication, least privilege and the review of each change. Each later step trusts the source.
3. Remove secrets from the source and from the logs, and give each pipeline step only the credential of its own task. Do this before the pipeline gets more tasks.
4. Move the build to a hosted platform with a definition under version control, and separate the build, the test and the packaging. This reaches the base of the build levels.
5. Add the automated tests, the static analysis and the scans of the dependencies to each change. A fault is cheapest here.
6. Make signed provenance and a bill of materials in the build, then isolate the build. Then let the deployment or the consumer verify them.
7. Automate the deployment with a tested way back, and make the environments from definitions.
8. Add the telemetry, the service level objectives and the incident procedure for a service that the team operates.
9. Measure the result on the scales of the targets, record it, and plan the next level.

### 3.3 Decisions that depend on context

| Decision | Depends on | Options | Sources |
|---|---|---|---|
| How many persons approve a change, and who can approve | kind of project; size of the organization | one approval of a person who is not the author; two trusted persons; a review of a share of the changes for a small project | S-09 versions page QA-07.01; S-02 draft/source-requirements, two-party review; S-11 gold item two_person_review; S-12 Source Code, Verification |
| Which value of test coverage the project sets, if it sets one | harm of a failure; the measuring tools of the language | no fixed value, with the trend examined; 80 percent of statements; 90 percent of statements and 80 percent of branches | S-11 silver item test_statement_coverage80 and gold items; S-24 A Note on Code Coverage; S-01 page 136 |
| How a pipeline component is pinned | pipeline platform; the rule of the component for its own reference | the full digest of a commit; an exact version tag where the component must be referred to by its tag | S-20 Using third-party actions; S-10 Pinned-Dependencies; S-29 Generate provenance, Referencing builders; S-30 the part on pinned actions |
| Which build platform reaches the build level of the target | pipeline platform; way of delivery | a hosted platform of a vendor that states its level; a platform that the organization operates and hardens | S-02 build-track-basics; S-02 the requirements for build platforms |
| How a change to production is approved | harm of a failure; outside duty | an automated gate for a change of low risk; a formal review for a release of high risk; a change board | S-07 2-5-1-Release; S-01 pages 161, 193-194 |
| Within which time a vulnerability is corrected | harm of a failure; outside duty | a time limit for each class of severity that the project sets | S-09 versions page, Other Elements; S-08 defect-management, stream A |
| How fast the pipeline gives its result | size of the test suite | a few minutes for the first result; less than ten minutes for the automated tests | S-25 the page on continuous integration; S-25 TA, How to implement automated testing; S-36, location not confirmed by the second reader |
| Which service level objectives the service has | way of delivery; the promise to the users | start with a loose objective and make it stricter with time; no objective for a project that only gives a package | S-23 chapter Service Level Objectives; S-01 page 158 |
| How a release reaches the users | way of delivery; harm of a failure | in stages to a part of the users first; behind a switch for each feature; in one step with a tested way back | S-01 page 160; S-24 chapter Continuous Delivery |
| Which data service gives the known vulnerabilities | the package ecosystems of the project; who operates the service and who pays for it | a public service that collects the databases of the ecosystems; the database of the ecosystem itself | S-27 FAQ; S-27 data sources page |

### 3.4 Where the sources disagree

| Question | Positions | How this recipe handles it | Sources |
|---|---|---|---|
| Does the name of the aspect mean what the owner means? | The sources with the name: DevSecOps integrates security early and through the whole process (S-01), and the guidance with the name is about the security of the supply chain in the pipeline (S-04, S-07). The owner: the shift left of operational, security and quality concerns. | The recipe follows the owner. The view operations takes its requirements from S-01, S-17, S-23 and S-26. The view quality takes its requirements from S-01, S-11, S-24, S-35 and S-36. | S-01 page 159; S-04 pages 1-23; S-07 project page |
| Must the build, the test and the packaging be separate steps? | The owner: they must not run in the same step, and no step exposes credentials (K-2). The sources that were read: an isolated build whose steps cannot reach the signing material (S-02), separated duties and no single person who can ship alone (S-06, S-12). No reader reported a requirement that names the three steps. | The item C-08 keeps the words of the owner. A constraint of the charter is not traded. The ladder puts the item on the level of its sources; the owner can move it. | S-02 build-track-basics; S-06 CICD-SEC-01; S-12 Part 3, Build Pipelines |
| Which is the highest level of the scale of the target? | The owner: the highest levels of the draft. The source: the build track has the levels L0 to L3 in the approved version and in the draft, and the source track has the levels L1 to L4. | The targets name the two tracks. The parts T-1 and T-2 of the charter are read as levels of the build track, because the owner refers to the build track. The owner confirms this in the review. | S-02 build-track-basics; S-02 draft/source-requirements |
| Is a reproducible build a requirement? | S-11: a rebuild that gives the same bits is a must for the level silver, and a reproducible build is a must for the level gold. S-02: the levels of the build track end at L3 and ask for a hosted, isolated build. The charter: more than L3 is an aspiration, with the hermetic repeatable build as the example (T-3). | The item C-21 asks for it only where the project can do it. T-3 of the charter decides. | S-11 silver item build_repeatable and gold item build_reproducible; S-02 build-track-basics |
| Is a fixed value of test coverage a requirement? | S-11: 80 percent of statements for silver, 90 percent of statements and 80 percent of branches for gold. S-24: a team should not treat a percentage of coverage as a goal. S-01: the measures of thoroughness help the decision to stop testing, and they are not sufficient alone. | The item C-39 names no value. The value is a decision that depends on context. | S-11 silver item test_statement_coverage80, gold items test_statement_coverage90 and test_branch_coverage80; S-24 A Note on Code Coverage; S-01 page 136 |
| Is a pipeline component pinned by a digest or by a version tag? | S-20, S-10 and S-30: by the full digest of a commit. S-29: by a full version tag, not by a shorter tag or a digest, because of limits of the platform. S-06: by a version or a range of versions that was examined. | The item C-10 asks for an exact, verified version. The form is a decision that depends on context, and the exception of one component is knowledge for an implementation skill. | S-20 Using third-party actions; S-10 Pinned-Dependencies; S-30 the part on pinned actions; S-29 Generate provenance, Referencing builders; S-06 CICD-SEC-03 |
| Does a board approve a change, or does the pipeline? | S-01: a change control board decides on a change request. S-07: the approval of a change of low risk can be automated, and a release of high risk keeps a formal review. | The principle P-1 decides: the checks are in the pipeline, before the delivery. The item C-31 asks for an approval by the class of the change. The order of the principles is not confirmed, thus the owner gets this case as a question. | S-01 pages 193-194; S-07 2-5-1-Release |
| Does the project use pipeline components of other parties, or does it limit them? | S-21, S-22 and S-07: use components and templates that are shared. S-06 and S-20: a component of a third party is a risk; pin it, examine it and limit which ones can run. | The principle P-4 decides to use a maintained component first. The items C-10 and C-20 give the conditions. The order of the principles is not confirmed, thus the owner gets this case as a question. | S-21 Reuse workflows; S-22 CI/CD components; S-06 CICD-SEC-03; S-20 Using third-party actions |
| Is a component that makes provenance maintained? | S-29: the page of the project says that the project is no longer actively maintained, and it points to the attestations of the platform. The principle P-4 of the charter asks for maintained components. | The recipe names no component. An implementation skill must read the state of a component at the time of use. | S-29 Banner |

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
| C-01 | Each change to the source is in a version control system that keeps the history and the identity of its author. | A change that cannot be traced to a person and a time cannot be examined after an attack. | security | 1 | standard (S-04) | the repository keeps each revision, and the history of the protected branch cannot be rewritten | S-04 page 26; S-02 draft/source-requirements, Choose an appropriate SCS; S-06 CICD-SEC-09, Recommendations item 4; S-09 versions page, Access Control, AC-03.02; S-11 passing item repo_public; S-12 Part 3, Source Code, Verification, Authenticate and monitor reposit...; S-01 page 256; S-24 ch09: Write Good Change Descriptions |
| C-02 | Access to the source, the pipeline and the artefacts needs strong authentication and gives the least privilege. | One stolen account or one broad permission lets an attacker change the product. | security | 1 | standard (S-03, S-04) | the settings need a second factor for each person with write access, and each pipeline job states its permissions | S-03 page 8; S-04 page 18; S-02 draft/source-requirements, Access control and history; S-06 CICD-SEC-02, Recommendations item 1; S-07 2-7-2-Logging-and-Monitoring.md; S-09 versions page, Access Control, AC-01.01; S-10 Token-Permissions item; S-11 gold item require_2FA |
| C-03 | A second person reviews each change before it enters a protected branch. | One person, or one stolen account, can put a harmful change into the product. | security | 1 | standard (S-03, S-04) | the protected branch refuses a change without an approval of a different person | S-03 page 21; S-04 page 21; S-02 draft/source-requirements, Protected Named References (L3); S-06 CICD-SEC-01, Recommendations item 1; S-07 1-1-2-Roles-and-Responsibilities.md; S-09 versions page, Access Control, AC-03.01; S-10 Branch-Protection item; S-11 gold item code_review_standards |
| C-04 | Secrets are not in the source, in a log or in an artefact, and a pipeline step gets only a short-lived credential for its own task. | A secret that a step can read is a secret that each program of that step can send out. | security | 1 | standard (S-04) | a secret scan of the repository and of the pipeline files finds nothing, and no step that runs outside code has a credential | S-04 page 17; S-06 CICD-SEC-04, Recommendations item 6; S-07 2-5-1-Release.md; S-08 /model/implementation/secure-deployment/, Stream B, Level 1; S-09 versions page, Build and Release, BR-07.01; S-10 Webhooks item; S-11 passing item no_leaked_credentials; S-12 Part 3, Source Code, Automation, Prevent committing secrets |
| C-05 | The build runs on a hosted build platform from a definition under version control, not on the computer of a person. | A build on the computer of a person has no witness, and nobody can repeat it. | security | 1 | standard (S-04) | each released artefact comes from a run of the pipeline, and the pipeline definition is in the repository | S-04 page 17; S-02 build-requirements, Producer > Choose an appropriate build platform; S-08 /model/implementation/secure-build/, Stream A, Maturity 2; S-12 Part 3, Build Pipelines, Automation, Pipelines as code |
| C-06 | The build platform makes provenance for each artefact and signs it. | Without provenance, a consumer cannot know from which source and by which build an artefact came. | security | 1 | standard (S-03, S-04) | each released artefact has a signed provenance statement that names the source revision and the build definition | S-03 page 19; S-04 page 24; S-02 build-requirements, Producer > Distribute provenance; S-06 CICD-SEC-09, Recommendations item 2; S-07 2-3-6-1-SBOM.md; S-09 versions page, Build and Release, BR-06.01; S-10 Signed-Releases item; S-11 silver item signed_releases |
| C-07 | Each build runs in a new, isolated environment, and the build steps cannot reach the signing material of the provenance. | A build that shares state with a different build, or that can read the signing key, can forge an artefact or its provenance. | security | 1 | standard (S-04) | the build platform documents isolated, ephemeral runs, and the signing identity belongs to the platform and not to a step | S-04 page 21; S-02 build-requirements, Provenance generation, Provenance is Authentic...; S-06 CICD-SEC-03, Recommendations item 11; S-12 Part 3, Build Pipelines, Automation, Build workers single use; S-20 GitHub's security features, Self-hosted runners; S-22 Security, for users |
| C-08 | The build, the test and the packaging run as separate steps with separate privileges, and the duties of the persons are separated. | A step that builds, tests and publishes at one time gives the publishing credential to each program that the tests run. | security | 2, credentials with production reach | foundation (S-02, S-06, S-08, S-12) | the pipeline definition has separate jobs for build, test and publication, and only the publication job has the publication credential | S-02 draft/source-requirements, Safe Expunging Process; S-06 CICD-SEC-01, Recommendations item 2; S-08 /model/implementation/secure-deployment/, Roles and concerns; S-12 Part 3, Build Pipelines, Controlled Environments, Segregate duties; S-30 Implementation, Use GitHub Actions environments |
| C-09 | The project keeps a machine-readable list of its components and gives a bill of materials with each release. | A project that does not know its components cannot tell if a published vulnerability touches it. | security | 1 | standard (S-04) | each release has a bill of materials in a standard format, made by the build | S-04 page 13; S-07 2-3-6-1-SBOM.md; S-08 /model/implementation/secure-build/, Stream B, Maturity 1; S-09 versions page, Quality, QA-02.01; S-10 SBOM item; S-11 silver item external_dependencies; S-12 Part 3, Materials, Verification, Require SBOMs and VEX; S-24 Dependency Management with Infinite Resources |
| C-10 | Each dependency and each pipeline component is pinned to an exact, verified version. | A dependency that can change without a change of the project lets a stranger change the product. | security | 1 | standard (S-04) | no pipeline file and no manifest refers to a component by a name that can move, and a lock file with digests is in the repository | S-04 page 27; S-02 draft/source-requirements, Identity and repositories (L1 to L4); S-06 CICD-SEC-03, Recommendations item 1; S-07 2-3-5-Security-Gates.md; S-10 Pinned-Dependencies item; S-12 Part 3, Materials, Verification, Verify third-party artifacts; S-20 Using third-party actions, Pin to full-length commit SHA; S-21 A: Workflow templates |
| C-11 | Known vulnerabilities in the code and in the dependencies are found by automated scans and corrected within a stated time. | A known vulnerability that stays in a release is the attack that costs the attacker the least. | security | 1 | standard (S-03, S-04) | a scan of the dependencies runs on each change and on a schedule, and the open findings are younger than the stated time | S-03 page 8; S-04 page 21; S-06 CICD-SEC-07, Recommendations item 2; S-07 2-3-6-1-SBOM.md; S-08 /model/implementation/secure-build/, Stream B, Maturity 3; S-09 versions page, Vulnerability Management, VM-05.01; S-10 Vulnerabilities item; S-11 passing item vulnerabilities_fixed_60_days |
| C-12 | The project publishes how to report a vulnerability, and it has a process to answer, to correct and to disclose. | A finder who has no private way to report publishes the weakness or stays silent. | security | 1 | standard (S-03) | the repository has a security policy with a private contact, and published advisories exist for corrected vulnerabilities | S-03 page 8; S-07 2-5-1-Release.md; S-08 /model/verification/security-testing/, Reader instructions; S-09 versions page, Documentation, DO-02.01; S-10 Security-Policy item; S-11 passing item vulnerability_report_process; S-20 Protecting actions you've created |
| C-13 | Threats are modelled in the design, and the security requirements are written before the code. | A weakness of the design cannot be removed by a scan of the code. | security | 1 | standard (S-03, S-04) | a threat model and a list of security requirements are in the repository and are newer than the last change of the design | S-03 page 14; S-04 page 24; S-07 project page; S-08 /model/verification/architecture-assessment/, Stream B, Maturity 1; S-09 versions page, Security Assessment, SA-03.01; S-11 silver item implement_secure_design; S-01 page 47; S-25 PS, section 6 |
| C-14 | Static analysis and security tests run automatically on each change. | A weakness that a program can find is found late, or by an attacker, if no program looks for it. | security | 1 | standard (S-03, S-04) | the pipeline has a static analysis job and a security test job, and a finding above the stated severity fails the run | S-03 page 23; S-04 page 11; S-07 1-1-2-Roles-and-Responsibilities.md; S-08 /model/verification/requirements-driven-testing/, Stream B, Maturity 1; S-09 versions page, Vulnerability Management, VM-06.02; S-10 Fuzzing item; S-11 passing item static_analysis; S-12 Part 3, Source Code, Automation, Automate security scanning and tes... |
| C-15 | The pipeline treats each input and each contribution from outside as untrusted. | A pipeline that runs the code of a stranger with its own privileges gives the stranger those privileges. | security | 1 | standard (S-04) | no job that is started by an outside contribution has a secret or a write permission, and no script puts outside text into a command | S-04 page 27; S-06 CICD-SEC-03, Recommendations item 1; S-09 versions page, Build and Release, BR-01.01; S-10 Dangerous-Workflow item; S-11 silver item input_validation; S-01 page 268; S-20 Writing workflows: Good practices for mitigating script injection,... |
| C-16 | The pipeline platform and its runners are hardened, kept up to date and logged. | The pipeline is a production system with write access to the product, and an attacker treats it as one. | security | 1 | standard (S-03, S-04) | the configuration of the platform is recorded, its audit log is kept, and its software is at a supported version | S-03 page 16; S-04 page 20; S-02 build-requirements, Build Platform: Security (all conformant levels); S-06 CICD-SEC-03, Recommendations, last item; S-07 project page; S-08 /model/operations/environment-management/, Stream A, Level 1; S-11 gold item hardened_site; S-12 Part 3, Build Pipelines (intro) |
| C-17 | A consumer verifies the provenance and the signature of an artefact against stated expectations before the artefact is used or deployed. | Provenance that nobody verifies stops nobody. | security | 1 | standard (S-04) | the deployment step, or the instructions for users, verifies the signature and the provenance, and a failed verification stops the step | S-04 page 18; S-02 build-requirements, Producer > Follow a consistent build process; S-06 CICD-SEC-01, Recommendations item 5; S-07 2-6-1-Deploy.md; S-08 /model/implementation/secure-deployment/, Stream A, Level 3; S-09 versions page, Build and Release, BR-03.02; S-11 passing item delivery_unsigned; S-12 Part 3, Source Code (intro) |
| C-18 | The product uses published, reviewed cryptography and has secure default settings. | Cryptography of the project's own design and an open default setting fail without a sign. | security | 1 | standard (S-03, S-04) | no cryptographic primitive is implemented in the project, and the default configuration passes the hardening guide of the project | S-03 page 20; S-04 page 40; S-08 /model/operations/operational-management/, Stream A, Maturity 1; S-09 versions page, Build and Release, BR-03.01; S-11 passing item sites_https; S-01 page 268 |
| C-19 | The roles and the duties for security are assigned, and the persons who hold them are trained. | A duty that nobody holds is not done. | security | 1 | standard (S-03, S-04) | a document names the roles and their holders, and a record of the training exists | S-03 page 15; S-04 page 36; S-07 1-1-2-Roles-and-Responsibilities.md; S-08 /model/operations/incident-management/, Stream B, Maturity 1; S-01 page 159; S-26 Organization, first section; S-25 PS, section 5; S-28 Directives section |
| C-20 | Suppliers and third-party components are selected by stated criteria and examined through their life. | The weakest supplier sets the security of the product. | security | 1 | standard (S-03, S-04, S-14) | a written rule for the selection of a dependency exists, and each new dependency has a record of the examination | S-03 page 8; S-04 page 21; S-14 Source B, attesting page, body; S-02 verifying-artifacts, roots of trust; S-06 CICD-SEC-01, Recommendations item 3; S-07 0-3-Frameworks-and-Standards.md; S-09 versions page, Documentation, DO-06.01; S-10 Maintained item |
| C-21 | Where the project can do it, the build is reproducible or hermetic. | A build that takes input from the network at build time, or that gives a different output each time, cannot be verified by a second party. | security | 2, consumers of the artefact | foundation (S-02, S-11, S-12) | a second build from the same source gives the same digest, or the build runs without network access | S-02 draft/build-requirements, Producer; S-11 silver item build_repeatable; S-12 Part 3, Build Pipelines, Reproducible builds, Eliminate non-determi...; S-23 Philosophy, Hermetic Builds; S-24 ch23, "Hermetic Testing" |
| C-22 | The project measures its security practices on a published scale and records the result. | Without a measured level, the project and its users cannot tell how far the project is. | security | 1 | standard (S-04, S-14, S-16) | the result of an assessment on a published scale is recorded with its date | S-04 page 20; S-14 Source B, attesting page, body; S-16 page 2; S-02 assessing-build-platforms, Self-attestation; S-07 0-3-Frameworks-and-Standards.md; S-08 /assessment/, Scoring input; S-09 home page, intro; S-10 CII-Best-Practices item |
| C-23 | Each release and its evidence are archived and protected from change. | An artefact or a record that can be changed after the release proves nothing. | security | 1 | standard (S-03, S-04) | the artefact store refuses to overwrite a released version, and the records of the build are kept for a stated time | S-03 page 19; S-04 page 26; S-02 draft/source-example-controls, Immutable Change Discussion; S-07 0-3-Frameworks-and-Standards.md; S-12 Part 3, Artifacts, Automation, Use a metadata store; S-01 page 215 |
| C-24 | The deployment is automated, and the same artefact goes through each environment. | A manual deployment is done differently each time, and an artefact that is built again for production is not the artefact that was tested. | operations | 1 | standard (S-04) | the deployment is a pipeline job, and the digest of the artefact is the same in each environment | S-04 page 21; S-07 2-5-1-Release.md; S-08 /model/implementation/secure-deployment/, Stream A, Level 1; S-11 silver item installation_common; S-01 page 101; S-23 Continuous Build and Deployment, Deployment; S-24 ch23, "Automation / Continuous Delivery"; S-25 CD, section 9 |
| C-25 | Changes are small and reversible, and a tested way back exists for each release. | A large change that cannot be reverted makes each failure an outage. | operations | 1 | standard (S-04) | the release procedure has a rollback step that was run in a test, and the releases are made in stages | S-04 page 31; S-02 draft/source-example-controls, Merge Trains; S-07 2-6-1-Deploy.md; S-01 page 157; S-23 Appendix B, Progressive Rollouts; S-24 ch09: Write Small Changes; S-26 Prepare, second section; S-25 GUIDE, Next steps |
| C-26 | The environments and their configuration are made from definitions under version control. | An environment that a person made by hand cannot be made again, and it differs from the environment that was tested. | operations | 1 | standard (S-04) | the environments are created by a program from files of the repository | S-04 page 30; S-06 CICD-SEC-01, Recommendations item 6; S-07 2-6-1-Deploy.md; S-12 Part 3, Build Pipelines, Reproducible builds, Automate build enviro...; S-01 page 131; S-23 Configuration Management; S-24 ch23, "Automation / Continuous Delivery"; S-26 Prepare, OPS 7 section |
| C-27 | The service has stated service level objectives, and measurements show if it meets them. | Without a stated objective, nobody can decide if the service is reliable enough or if a release is too risky. | operations | 2, operated service | vendor (S-26) | a document states the objectives, and a report compares the measured values with them | S-01 page 158; S-23 Appendix B, Define SLOs Like a User; S-24 ch24, "Striving for Agility"; S-26 Operate, second section |
| C-28 | Logs, metrics and traces are collected, and each alert goes to a person who can act. | A failure that no signal shows is found by the users. | operations | 1 | standard (S-04) | the telemetry of the service is collected in each environment, and each alert names its receiver and its procedure | S-04 page 21; S-02 draft/source-requirements, Safe Expunging Process; S-06 CICD-SEC-03, Recommendations item 14; S-07 2-7-2-Logging-and-Monitoring.md; S-08 /model/operations/incident-management/, Stream A, Maturity 1; S-01 page 158; S-23 Appendix B, Fail Sanely; S-24 ch24, "Idioms of Continuous Delivery at Google" |
| C-29 | An incident has a defined response, and each incident gets a review without blame that gives recorded actions. | An incident without a prepared response lasts longer, and an incident without a review comes back. | operations | 2, operated service | foundation (S-07, S-08) | an incident procedure exists, and each incident of the stated severity has a written review with actions that have owners | S-07 1-1-2-Roles-and-Responsibilities.md; S-08 /model/operations/incident-management/, Stream A, Maturity 3; S-01 page 155; S-23 Appendix B, Postmortems; S-26 Design principles, implement observability |
| C-30 | The operational readiness is examined before a release: procedures, capacity, backup and restore. | A service that goes into production without a procedure, without capacity or without a tested restore fails at its first bad day. | operations | 2, operated service | vendor (S-26) | a readiness review is recorded for each new service, and a restore from a backup was tested | S-01 page 158; S-23 Appendix B, Fail Sanely; S-26 Design principles, refine procedures; S-25 DA, Requirements |
| C-31 | Each change to production is recorded, classified by its risk and approved as its class needs. | A change that nobody recorded cannot be linked to the failure that it causes. | operations | 2, operated service | foundation (S-06, S-07) | each deployment has a record with the change, its class and its approval | S-06 CICD-SEC-01, Recommendations item 4; S-07 2-3-5-Security-Gates.md; S-01 page 159; S-26 Organization, ownership section; S-25 MO, Requirements; S-30 Implementation, Harden workflow environment permissions |
| C-32 | Each release is planned, has a unique version identifier and release notes, and can be traced to its source. | A user cannot tell what a release holds or whether a correction is in it. | operations | 2, consumers of the artefact | foundation (S-09, S-10, S-11) | each release has a unique version, notes that name the changes and the corrected vulnerabilities, and a link to its source revision | S-09 versions page, Build and Release, BR-02.01; S-10 Packaging item; S-11 passing item version_unique; S-01 page 178; S-22 Component versions; Publish a new release; S-23 Continuous Build and Deployment, Branching; S-24 ch24, "Striving for Agility"; S-30 Implementation, Document the release process |
| C-33 | The pipeline is made of maintained, versioned components that are used again across projects, before a new part is written. | A pipeline that each project writes for itself is maintained by nobody and differs in each project. | operations | 1 | standard (S-03, S-04) | each step of the pipeline names a maintained component with its version, or the plan says why none is used | S-03 page 16; S-04 page 24; S-07 1-1-2-Roles-and-Responsibilities.md; S-12 Part 3, Build Pipelines, Automation, Standardize pipelines; S-01 page 106; S-21 A: Reusable workflows; S-22 CI/CD Catalog; S-24 ch09: Code Is a Liability |
| C-34 | The operation of the software is planned with its development: owners, support and the work that can be automated. | Software that is made without its operators gets operations as a late cost. | operations | 1 | standard (S-03, S-04) | an operations plan names the owner of the service, the support and the tasks that are automated | S-03 page 16; S-04 page 36; S-01 page 156; S-23 Philosophy, Self-Service Model; S-26 Organization, first section; S-25 CD, section 9 |
| C-35 | The configuration items, the baselines and their status are identified, controlled and audited. | Nobody can say what is in a release when its parts are not identified and controlled. | operations | 1 | standard (S-03) | a list of the configuration items and of the baselines exists, and an audit of a release compares the list with the content | S-03 page 13; S-01 page 53; S-23 Conclusions, It's Not Just for Googlers; S-24 ch24, "Velocity Is a Team Sport"; S-25 CI, Requirements |
| C-36 | The maintenance of the software and the end of its support are planned and published. | A user who does not know the end of support runs software that gets no more corrections. | operations | 2, operated service | foundation (S-08, S-09, S-11) | a document states the supported versions, the support period and the way to migrate | S-08 /model/operations/operational-management/, Stream B, Maturity 1; S-09 versions page, Documentation, DO-04.01; S-11 passing item maintained; S-01 page 151; S-24 Compatibility Promises |
| C-37 | An automated test suite runs on each change, and a failed run stops the change. | A fault that enters the main branch is found by a different person, later and at a higher cost. | quality | 1 | standard (S-04) | the protected branch needs a passed run of the pipeline, and the run includes the test suite | S-04 page 27; S-02 draft/source-requirements, Continuous technical controls (L3); S-07 2-3-5-Security-Gates.md; S-08 /model/implementation/secure-build/, Stream A, Maturity 3; S-09 versions page, Quality, QA-03.01; S-10 CI-Tests item; S-11 passing item test; S-01 page 124 |
| C-38 | The tests cover each test level and each quality characteristic that matters, and a change of function or a corrected fault adds a test. | A test suite that looks at one level only lets the faults of the other levels through. | quality | 1 | standard (S-03, S-19) | the test plan names the levels and the characteristics, and a change of function without a test fails the review | S-03 page 24; S-19 introductory paragraph; S-08 /model/verification/requirements-driven-testing/, Stream A, Maturity 1; S-09 versions page, Quality, QA-06.03; S-11 passing item test_most; S-01 page 118; S-24 ch09: Greenfield Code Reviews; S-26 Prepare, third section |
| C-39 | The measures of the tests are recorded and examined, without a fixed number in this recipe. | A test suite that nobody measures decays, and a number that is a goal is gamed. | quality | 2, harm of a failure | foundation (S-11) | the pipeline reports the coverage and the other measures that the project selected, and the trend is looked at | S-11 silver item test_statement_coverage80; S-01 page 100; S-24 A Note on Code Coverage |
| C-40 | The code obeys a written coding standard, and the warnings of the compiler and of the analysis tools are on and are corrected. | Code that each person writes differently hides faults, and a warning that is off hides a known fault class. | quality | 1 | standard (S-03, S-04) | the pipeline runs the formatter and the linter with the strict settings, and a new warning fails the run | S-03 page 22; S-04 page 39; S-07 1-1-2-Roles-and-Responsibilities.md; S-11 passing item warnings; S-01 page 267; S-24 ch09: Code Consistency |
| C-41 | The quality requirements are stated early, in measurable terms, from a quality model. | A quality that is not stated is not built and not tested. | quality | 2, harm of a failure | foundation (S-11) | a document states each quality requirement with its measure and its acceptance criterion | S-11 silver item accessibility_best_practices; S-01 page 51 |
| C-42 | A quality plan names the reviews, the audits and the gates through the life cycle, and records show that they were done. | Quality that is examined only at the end is examined too late to change the product. | quality | 1 | standard (S-03, S-04, S-16) | a quality plan exists, and each gate of the pipeline maps to an entry of the plan | S-03 page 16; S-04 page 21; S-16 page 2; S-02 draft/source-requirements, Continuous technical controls (L3); S-07 1-1-2-Roles-and-Responsibilities.md; S-01 page 179 |
| C-43 | Each defect is recorded in a tracker, classified, and its cause is analysed. | A defect that is not recorded is corrected two times or not at all, and its cause makes the next defect. | quality | 1 | standard (S-03, S-04) | a public or internal tracker holds the defects with their class and their state | S-03 page 27; S-04 page 13; S-08 /model/implementation/defect-management/, Stream A, Maturity 1; S-11 passing item report_process; S-01 page 60; S-27 FAQ, Data section, question on wrong data |
| C-44 | The project builds from its source with a documented, common build system. | A project that only one person can build cannot be verified, corrected or handed over. | quality | 2, harm of a failure | foundation (S-08, S-09, S-10, S-11, S-12) | a clean computer builds the project with the documented commands | S-08 /model/implementation/secure-build/, Stream A, Maturity 1; S-09 versions page, Build and Release, BR-05.01; S-10 Binary-Artifacts item; S-11 passing item build; S-12 Part 3, Materials, Verification, Build libraries from source; S-01 page 103; S-24 ch20: Requirements, Compiler checks; S-25 CI, Requirements |
| C-45 | The documentation for users and for contributors exists and is kept with the code. | A user who cannot find out how to use, to configure or to change the software uses it wrongly. | quality | 1 | standard (S-03) | the repository has the documents for use, for installation and for contribution, and a change of an interface changes its document | S-03 page 8; S-02 draft/source-requirements, Continuous technical controls (L3); S-07 2-3-5-Security-Gates.md; S-08 /assessment/, Instructions to the reader; S-09 versions page, Documentation, DO-01.01; S-11 passing item description_good; S-01 page 267; S-24 ch09: Greenfield Code Reviews |
| C-46 | The requirements are written, examined and traceable to the tests. | A product that meets no stated requirement cannot be shown to be correct. | quality | 2, duty by regulation or contract | foundation (S-08) | each requirement has an identifier, and a test or a review names it | S-08 /model/verification/requirements-driven-testing/, Stream A, Maturity 2; S-01 page 39; S-26 Organization, first section |
| C-47 | The architecture and the design are described and are evaluated against the quality attributes. | A structure that nobody described cannot be reviewed for the qualities that it must give. | quality | 2, harm of a failure | foundation (S-07, S-08, S-09, S-11) | a description of the architecture exists with the decisions and their reasons | S-07 1-1-2-Roles-and-Responsibilities.md; S-08 /model/verification/architecture-assessment/, Stream A, Maturity 1; S-09 versions page, Security Assessment, SA-01.01; S-11 silver item documentation_architecture; S-01 page 70; S-22 CI/CD Catalog; S-24 ch09: Code Is a Liability; S-26 Design principles, small reversible changes |
| C-48 | The work is planned, estimated and measured, its risks are managed, and its process is defined. | A project without a plan and without measures finds its problems when they cannot be corrected. | quality | 1 | standard (S-03, S-04) | a plan with the risks exists and is updated, and the selected measures are collected | S-03 page 8; S-04 page 17; S-06 CICD-SEC-09, Must and should statements; S-07 1-1-2-Roles-and-Responsibilities.md; S-11 silver item documentation_roadmap; S-01 page 59; S-23 Conclusions, It's Not Just for Googlers; S-24 ch09: Code Is a Liability |
| C-49 | Each person has the training and the knowledge that the role needs and works to the standards of the profession. | A person who does not know the practice cannot do it, and a tool does not replace the knowledge. | quality | 2, harm of a failure | foundation (S-11) | a record shows the training for each role | S-11 passing item know_secure_design; S-01 page 40; S-24 ch09: Ownership, Responsibilities of owners; S-26 Design principles, refine procedures |
| C-50 | The project has a stated governance: a license, roles, rules for a contribution and continuity when a person leaves. | A project that depends on one person, or that has no clear license, can stop or cannot be used. | quality | 2, duty by regulation or contract | foundation (S-09, S-10, S-11, S-12) | the repository has a license file, the rules for a contribution and a list of the persons with their roles | S-09 versions page, Governance, GV-01.01; S-10 Contributors item; S-11 passing item contribution; S-12 Part 3, Source Code, Controlled Environments, Contribution policies; S-24 ch09: Ownership |
| C-51 | The dependencies are kept current by a stated rule, and a dependency that is not maintained is replaced. | An old dependency collects known faults, and a late update is a large, risky change. | quality | 2, outside code in the pipeline | foundation (S-08, S-10, S-11) | an update tool or a schedule proposes the updates, and no dependency is older than the stated rule permits | S-08 /model/implementation/secure-build/, Stream B, Maturity 2; S-10 Dependency-Update-Tool item; S-11 silver item updateable_reused_components; S-01 page 103; S-20 GitHub's security features, Dependabot; S-24 Introduction; S-28 Directives section; S-30 Implementation, Pin actions to full commit SHAs |
| C-52 | The team examines the effect of its practices with data and corrects them. | A practice that is kept without a look at its effect costs effort and can do harm. | quality | 1 | standard (S-03) | a record of the periodic review of the practices exists, with the data and the decided changes | S-03 page 27 (RV.3.4); S-08 /model/implementation/defect-management/, Stream B, Maturity 2; S-01 page 162; S-23 page 2, "Ask for Feedback"; S-24 ch20: Developer Happiness; S-26 Design principles, refine procedures; S-35 section 5.2 Implications for researchers; S-36 Section 5.2.1 |

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

- **Goal**: The project has a selection of checklist items with a target level for each risk dimension, and a plan that names, for each selected item whose check fails, the step that corrects it. The plan reaches the build level L2 first and the build level L3 next.
- **Reads first**: The kind of project, the size of the organization, the pipeline platform, the way of delivery, the harm of a failure and the outside duty. Then the answers to the six risk questions, the pipeline definitions, the settings of the repository that the session can read, and the committed selection of the project, if one exists.
- **Applies**: The order of the work: source, secrets, hosted build with separate steps, tests and scans on each change, provenance and its verification, automated deployment, telemetry, measurement. It judges each selected item with its check and reports the items whose check fails.
- **Delegates**: The pipeline definition on the platform of the project; the making and the verification of provenance; the scan of dependencies with a public vulnerability data service; the signing of artefacts; the measurement on a published scale. Each one is given by an implementation skill. Without that skill, the recipe skill names the capability and the maintained component to look for, and writes no setting from memory.
- **Stops when**: The plan is written; this is a sufficient result. It stops also when a decision that depends on context needs a person, when a credential or a setting cannot be read, or when a step would put the build, the test and the packaging into one step or would show a credential.

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
| SLSA provenance format and its verifier | write, distribute and verify provenance with the correct fields | C-06, C-17 | a verifier of provenance |
| GitHub Actions | the pipeline definition on this platform: permissions of the token, secrets, pinned components, workflows that are used again, attestations | C-02, C-04, C-08, C-10, C-15, C-33 | none |
| GitLab CI/CD | the pipeline definition on this platform: components, the catalog and their versions | C-10, C-32, C-33 | none |
| AWS operations services | the operation of a workload on this platform: managed services, resource tags, central governance of accounts | C-26, C-34 | none |
| OSV | the query of known vulnerabilities and the format of an advisory | C-11, C-12 | a scanner that reads the service |
| Sigstore | the signing of an artefact and the public log of signatures | C-06, C-17 | the client of the service |
| OpenSSF Scorecard | the measurement of a repository on the score of the security checks | C-22 | the program of the project |
| Tekton Chains | provenance that an observer of the pipeline run makes, signs and stores | C-06 | none |
| The Update Framework and OCI registries | the distribution of artefacts and of their metadata with roles and with trust that ends | C-17, C-23 | none |
| Package registries with scopes | private packages under the scope of the organization | C-10 | none |

## 6. Watch list

| Signal | Where to read it | Cadence |
|---|---|---|
| A new version of the specification of the build levels, or a level above L3 in its draft | S-02, https://slsa.dev/spec/ | each refresh |
| A new version of the baseline for open projects | S-09, https://baseline.openssf.org/ | each refresh |
| A new version of the secure development framework or of the pipeline guidance | S-03 and S-04, https://csrc.nist.gov/projects/ssdf | each refresh |
| The regulation that was not read becomes readable, and its dates of application | S-13, https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng | each refresh |
| A new version of the body of knowledge; the cell sha256 of the seed | factory/sota-research/references/seeds.md, row swebok | each refresh |
| The maintenance state of the components that make provenance | S-29, the banner of the page; S-31 | each refresh |
| A change of the measures of delivery performance | S-25, https://dora.dev/insights/dora-metrics-history/ | each refresh |
| A new edition of the yearly statistics | S-25 https://dora.dev/research/; S-28 | each year |

## 7. Decisions and changes

Dated. A reversed decision stays and is marked superseded. Name the models that made or
suggested a judgement, and the person who reviewed the findings and accepted the recipe.

| Date | Decision or change | Reason | Revisit when |
|---|---|---|---|
| 2026-10-11 | Not verified: the intent of the owner was not asked in the session of phase 1. The lines of "Intent of the owner" are the words of the owner from 2026-10-10 and 2026-10-11, and the session put each quote under its question. | The owner was not in the session. | The owner reviews the intent and the draft of the charter. |
| 2026-10-12 | The research has three views: security, operations and quality. | The owner named these three points of view. The body of knowledge has a knowledge area for each one (S-01 pages 151-166, 246-263, 264-273). | The owner adds, removes or renames a view. |
| 2026-10-12 | The knowledge area Software Testing is in the view quality. The knowledge area Software Configuration Management is in the view operations, and its concerns of integrity are in the view security. They are not views of their own. | Judgement of the session. The owner named three points of view. | The owner wants a view for tests or for configuration management. |
| 2026-10-12 | The body of knowledge S-01 has the class research, not standard. | Judgement of the session: it is a guide of a professional society, and it states no conformance. This class changes the level of each item that only S-01 and the books ask for. | The owner decides that S-01 has the class standard. |
| 2026-10-12 | ISO/IEC 27001 (S-16) has the class standard, not governance. | Judgement of the session: a standards body issues it. No requirement of the practice was read from it, thus the class changes no level. | The full text is read. |
| 2026-10-12 | The task for the readers of S-01 limited the requirement lines to the aspect: operations, security, quality, testing, build, integration, delivery, release, configuration management and supply chain. | S-01 covers the whole field. The readers reported also requirements of other knowledge areas; each one has a row. | A refresh reads S-01 again. |
| 2026-10-12 | Each reader was started as a session of its agent type from the command line of the agent product, not with the agent tool of the session. | The agent types that models.py wrote were not loaded in the running session. A test showed that such a session has only the tools of its agent file and that the hook refuses a file of the repository. | The procedure is started in a new session after models.py. |
| 2026-10-12 | A program gave each of the 2044 requirement lines a first exit by words and, for S-01, by the page of the knowledge area. A model of mid size then examined each line in seven parts and changed 1029 exits. The session set 19 exits by hand. The session wrote the items, and did not examine each of the 2044 rows itself. | The number of the lines. Step 10 of phase 2. | The owner or a trial finds a requirement at a wrong item. |
| 2026-10-12 | The stakeholder of a requirement row comes from the group that the reader reported. If the reader reported no group, it comes from the source and from the view of the item. | 1180 of the lines have no group in the source. | The owner changes a stakeholder. |
| 2026-10-12 | Requirements that are far from the aspect have items of their own: C-36 and C-46 to C-50. The research proposes a boundary for each of them. | A requirement cannot go to a boundary that the owner did not decide, and no requirement is dropped. | The owner decides or declines each boundary. |
| 2026-10-12 | No item for the measurement of the delivery performance. The five measures are a target of section 1. | The readers reported the measures (S-25), and no reader reported a requirement to measure them. An item must hold a requirement. | A reader reports such a requirement. |
| 2026-10-12 | The item C-08 holds the constraint K-2 of the charter. The ladder puts it on the level of its sources. | A level is not written by hand. The requirements that go to C-08 are about separated duties (S-02, S-06, S-08, S-12, S-30), not about the three steps. | The owner sets the level of C-08 in the review. |
| 2026-10-12 | The order of the principles of the charter decided two cases of section 3.4: P-1 for the approval of a change, and P-4 for the use of components of other parties. | The owner did not confirm the charter or the order of its principles. | The owner confirms or changes the order. |
| 2026-10-12 | Not verified: S-05 (the server refused the request), S-13 (the pages of the issuer came back empty to the reader and to the two converters) and S-18 (the server refused the request). No statement of these sources is in the recipe. The view security has no regulation that was read. | Step 17 of phase 2. | The owner gives the files, or a refresh can retrieve them. |
| 2026-10-12 | Not verified: the full text of S-15, S-16, S-17 and S-19. Only the pages of the issuers were read. S-15 and S-17 gave no requirement line. | Paid sources. | The owner gives the texts. |
| 2026-10-12 | Not verified: the date of S-01. The seed manifest and the reader of pages 1 to 25 give different dates. Compare the cell 'Version or date' of the row swebok in factory/sota-research/references/seeds.md with point 1 of the report S-01-1 in the work folder. | Two different values in two places. | The owner looks at the file of the seed. |
| 2026-10-12 | Not verified: the references that S-01 names for the knowledge areas of the views were not all retrieved (step 8 of phase 2): ISO/IEC/IEEE 20000-1, ISO/IEC/IEEE 12207, ISO/IEC 20246, IEEE 1012, the ISO/IEC 29110 series and the books that S-01 names for operations. The commands index.py refs and index.py cited were not run. S-17, S-18, S-19 and S-23 are such references and were given to readers. | The time of the run and paid sources. | A refresh does step 8 for each view. |
| 2026-10-12 | Not verified: who pays for the public data services S-27 and S-34. The pages do not say it. The page of S-27 names no operator. | Step 4 of phase 2 asks for the operator and the payer. | A refresh. |
| 2026-10-12 | Not verified: the web readers got each page through a tool that gives a summary of the page, not its words. A location in a web source is the heading that the reader reported. | The reports of the readers say this. | A source is converted and read as a file. |
| 2026-10-12 | Not verified: the vetting answer 'record' of S-30. The reader named a page of one author and did not fetch it. | Point 6 of the report S-30-2. | The owner confirms or rejects S-30. |
| 2026-10-12 | The catalogue queries found candidates that were not given to a reader, for example the entries for policy enforcement and for observability products. | A landscape lists products; the recipe names no product. The samples S-29 to S-34 came from the catalogues and from the searches. | An implementation skill needs a product. |
| 2026-10-12 | Two groups of synonyms are in the file synonyms.txt of the work folder: the two names of the bill of materials and the two names of the build platform. | The glossary has two names for each of these terms, and the sources use the two names. | A refresh makes a new work folder. |
| 2026-10-12 | The second reading: the evidence record has 36 rows. Second readers examined 33 rows. The second reading corrected 24 rows, and 9 rows had no finding. The other 3 rows say only that the source was not read (S-05, S-13, S-18), and no reader examined them. | Step 12 of phase 2. Each second reader was a new session that did not read the source before. | A refresh. |
| 2026-10-12 | The corrections of the second reading changed 25 requirement lines in 15 reports, and the rows of the table Requirements with them. The reports were stored again with index.py take. The first form of each report is in the folder reports-first of the work folder. | The check compares the rows with the lines of the index. Step 12 asks for the correction of each row that says the same. | none |
| 2026-10-12 | Not verified: the document of S-14. The second reader could not read the file at its address. The two requirement lines of S-14 were examined on the second page of the source only. | The report of the second reader of S-14. | The file is converted and read. |
| 2026-10-12 | Roles of the models: a small model read each source and each page range (readers). A mid-size model did the second reading of the evidence record and examined the exits of the requirements. The largest model of the session made the searches, wrote the items, the strategy and section 1, and made each judgement that this table names. | Step 14 of phase 2. | none |

## 8. Glossary

Terms that mean different things in the sources. One preferred form per meaning.

| Term | Meaning here | Other meanings in the sources |
|---|---|---|
| DevSecOps | the shift left of operational, security and quality concerns, in the words of the owner | the integration of security early and through the whole process (S-01 page 159); the security of the supply chain in the pipeline (S-04) |
| provenance | a signed statement that says from which source, by which build definition and on which platform an artefact was built (S-02) | the history of a configuration item in status accounting (S-01 pages 195-196) |
| build platform | the hosted system that runs the builds and signs the provenance (S-02) | build service (S-02); CI/CD system (S-04, S-06) for the system that runs each step of the pipeline |
| release | the distribution of the software outside the development, also inside the organization (S-01 page 197) | the deployment of a change to the users (S-24) |
| level | the level 1, 2 or 3 of a checklist item of this recipe | build level and source level (S-02); baseline level (S-09); maturity level (S-08); integrity level (S-01 page 251) |
| verification | the examination of the provenance and of the signature of an artefact by its consumer (S-02) | verification and validation of a work product (S-01 pages 257-258) |
| bill of materials | the machine-readable list of the components of a release (S-01 page 192) | SBOM (S-04, S-07, S-12); software bill of materials (S-04, S-09) |

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
