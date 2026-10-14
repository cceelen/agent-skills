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
  - `software engineers`: they write the code and its tests, and they share the duties of test, rollback and security with operations (S-01 pages 151, 160, 248; S-04 page 11)
  - `operations engineers`: they deploy, configure, monitor and troubleshoot the software, and they handle incidents; site reliability engineers and platform engineers are in this group (S-01 pages 151, 152; S-04 page 11)
  - `security roles`: the staff with significant security roles; they set the policy for trusted sources, do the security tests and need training (S-01 pages 159, 266, 268; S-03 page 15; S-04 page 21)
  - `quality assurance`: the testers and the quality assurance function; they need test resources and criteria that tell when the testing is sufficient, and for critical systems the function can be independent of the project (S-01 pages 136, 138, 255)
  - `producers`: the persons or the organization that own a project and release its software; they select the build platform, protect the repository and distribute the provenance (S-02 Build: Requirements, Producer; S-03 page 5; S-06 Maintainers; S-07 home page)
  - `platform providers`: the persons who provide the build platform or the source control system; they generate the provenance, isolate the builds and protect the signing secrets (S-02 Build: Requirements, Build Platform; S-02 Source: Requirements)
  - `consumers`: the persons who receive and use the software; they verify the provenance and need the list of components and the service commitments (S-02 Build: Track Basics, Build L2; S-03 page 5; S-04 page 13; S-01 page 158)
  - `management`: the persons who decide on policy, risk and resources; they commit to secure development and to quality (S-01 pages 159, 249; S-03 page 16)
  - `auditors and regulators`: the persons who examine compliance; they need evidence from the configuration records and from the pipeline (S-01 pages 124, 187, 196, 259; S-04 page 20)
- **Views**: the points of view that the aspect brings together. A view is a set of concerns
  of the aspect. The research aggregates the concerns of the stakeholders into the views. A
  concern that the owner named in the intent is in a view, or section 7 says why it is not.
  One line each: a short name, what the view is concerned with, the stakeholders whose
  concerns the view holds, and the source. Name the stakeholders in this form, before the
  source: `(stakeholders: [name], [name])`. Use the names of the field "Stakeholders".
  - `operations`: the concerns of the knowledge area Software Engineering Operations that a project handles before the delivery: the plan of the operation, deployment, rollback, monitoring, incidents, recovery and service levels. The owner named this view. (stakeholders: operations engineers, software engineers, management, consumers) (S-01 pages 151 to 166; S-09)
  - `security`: the concerns of the knowledge area Software Security and of the secure development of software: requirements, access, secrets, analysis of code and dependencies, vulnerabilities and evidence. The owner named this view. (stakeholders: security roles, producers, management, consumers, auditors and regulators, software engineers) (S-01 pages 264 to 269; S-03; S-05; S-07)
  - `quality`: the concerns of the knowledge areas Software Quality and Software Testing that a project handles early: automated tests with each change, reviews, static analysis, defects and the plan of quality assurance. The owner named this view. (stakeholders: quality assurance, software engineers, management) (S-01 pages 117 to 141 and 246 to 260; S-12; S-13)
  - `pipeline`: the integrity of the path from a change of the source to a released artifact: version control, build, provenance, release and verification. The research found this view in the knowledge area Software Configuration Management and in the sources of the target of the owner; the owner did not name it as a view. (stakeholders: producers, platform providers, consumers, software engineers, auditors and regulators) (S-01 pages 185 to 198; S-02; S-04)
- **Contexts**: the values of each dimension that change the strategy. One line each.
  - `team size`: one maintainer; two or more maintainers; an organization with separate roles for development, operations and security (S-07 version page, Level 1 to Level 3; S-06 Code-Review check; S-01 page 163)
  - `users of the product`: few users; a small and consistent group of users; a large and consistent group of users (S-07 version page, Level 2 and Level 3)
  - `kind of delivery`: a library or a package for other projects; a service that the team operates; software that the customer installs and operates (S-03 page 12; S-06 Maintained check; S-01 page 156; the three values are a judgement)
  - `openness of the repository`: a public repository that takes changes from persons outside; a private repository with known contributors (S-05 CICD-SEC-4; S-04 pages 20, 21)
  - `build platform`: the computer of one person; a hosted build platform; a hosted build platform with isolated builds (S-02 Build: Track Basics, Build L0 to Build L3)
  - `duty from outside`: no duty; a regulation, a contract or a sponsor that demands a level or evidence (S-07 FAQ; S-04 page 20; S-03 page 8; S-01 page 187)
  - `development model`: a classic life cycle; an agile life cycle with DevOps (S-03 page 11; S-01 page 139)
- **Risk dimensions**: the dimensions on which the risk of a project differs for this aspect.
  One line each: the name, the question that finds it out, the opinion of the kit on the
  answer, and the source.
  - `exposure`: Do other projects or other persons build on your artifacts, or do persons from outside change your source? Opinion: if the answer is yes, go to the items of this dimension; a project with one maintainer and few users can stay on level 1. (S-02 Build: Track Basics; S-07 version page, Level 2 and Level 3; S-05 CICD-SEC-4)
  - `criticality`: How large is the harm to users when the software fails or the service stops? Opinion: a service that a team operates for other persons goes to the items of this dimension in the view `operations`; a library does not need most of them. (S-01 pages 162, 251; S-03 page 12)
  - `evidence duty`: Does a law, a contract or a sponsor ask you to show what you did? Opinion: if the answer is yes, keep the results of the pipeline as evidence from the start, because evidence cannot be made later. (S-01 pages 124, 187, 196; S-07 FAQ; S-04 page 20)
- **Boundaries**: what each neighbouring aspect owns, and what this aspect keeps. One line each:
  a short name, what the neighbouring aspect owns and what this aspect keeps, the state, and
  the source. A boundary has one of two states. Write the state in one of these forms, before
  the source. `(proposed)`: the research proposes the boundary, and it takes no requirement.
  `(decided by the owner on <YYYY-MM-DD>)`: the owner decided the boundary on that date, and
  a requirement can go to it. Only the owner decides a boundary. A line without a state is
  proposed.
  - `requirements engineering`: it owns the elicitation, the specification and the validation of requirements; this aspect keeps the security requirements and the quality requirements with their measures. (proposed) (S-01 pages 43 to 66)
  - `architecture and design`: it owns the description and the evaluation of the architecture and the design; this aspect keeps the design review for security risks and the design for operation. (proposed) (S-01 pages 67 to 98)
  - `software construction`: it owns the methods, the languages and the tools of construction; this aspect keeps secure coding, the one-command build and the automated analysis of each change. (proposed) (S-01 pages 99 to 116)
  - `software maintenance`: it owns the process, the techniques and the measures of maintenance; this aspect keeps the plan of the operation and the handling of vulnerabilities. (proposed) (S-01 pages 167 to 184)
  - `project management`: it owns planning, estimation, control, staff and acquisition; this aspect keeps the decision by risk on the security practices. (proposed) (S-01 pages 202 to 220)
  - `software process`: it owns the life cycle models and the assessment and improvement of the process; this aspect keeps the practices of the pipeline. (proposed) (S-01 pages 221 to 245)
  - `professional practice`: it owns the professional, legal and ethical duties and the work in teams; this aspect keeps the governance documents of a project. (proposed) (S-01 pages 275 to 287)
  - `software economics`: it owns the economic analysis of decisions; this aspect keeps the calculation of risk and reward for its own items. (proposed) (S-01 pages 288 to 311)
  - `engineering foundations`: it owns the foundations of computing, mathematics and engineering; this aspect keeps nothing of them. (proposed) (S-01 pages 312 to 386)
  - `making of the body of knowledge`: it owns the rules for the authors and the editors of the body of knowledge; they are not requirements for a project, and this aspect keeps nothing of them. (proposed) (S-01 pages 26 to 42 and 387 to 411)
- **Targets**: the measurable results that a project reaches when it applies the recipe. The
  targets come from the sources in the research; the owner can name one in the intent. One
  line each: the name, the scale with its levels, the program or the method that measures it,
  and the source of the scale. If the sources give no target, write `(none found)` in place
  of the lines.
  - `build level`: Build L0 (no guarantee), Build L1 (provenance exists), Build L2 (a hosted build platform signs the provenance), Build L3 (hardened builds); the method is the set of requirements of each level, and the verification of the provenance of an artifact. The owner named this target: Build L2 is the baseline and Build L3 is the goal. The source gives no approved level above Build L3. (S-02 Build: Track Basics; S-02 Future directions)
  - `source level`: Source L0 to Source L4: version control (L1), preserved history and provenance of the source (L2), enforced technical controls on named references (L3), review by two parties (L4); the source control system claims the level in a signed summary. (S-02 Source: Requirements)
  - `baseline level`: maturity Level 1 to Level 3, by the number of maintainers and the group of users; the method is a statement of the project about itself, which programs can evaluate; the source says that the scale is not for the comparison of projects. (S-07 version page; S-07 FAQ; S-07 maintainer guidance)
  - `check scores`: a score from 0 to 10 for each automated check of the practices of a repository; a program computes it from public data of the repository. (S-06 checks documentation)
  - `delivery performance`: five measures in two groups, throughput and instability; no levels; the source says that the measures are not goals. (S-10 metrics guide; S-01 page 133)
  - `service level`: a target or a range for a measured indicator of the service, for example availability; the project sets the value. (S-09 Service Level Objectives; S-01 page 158)
  - `test coverage`: 0 to 100 percent of covered statements, branches or requirements; a coverage program measures it. (S-01 pages 129, 132)
  - `process capability`: level 0 to level 5 of a process; a process assessment measures it. (S-01 page 253)

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
| S-01 | Guide to the Software Engineering Body of Knowledge (SWEBOK Guide) | IEEE Computer Society | 4.0a, 2025-09-25 | standard | IEEE copyright; individual use that is not commercial | full | all | https://www.computer.org/education/bodies-of-knowledge/software-engineering |
| S-02 | SLSA specification: Build track basics, Build requirements, Source requirements, Future directions | SLSA project, The Linux Foundation | 1.2, approved | foundation | Community Specification License 1.0 | part | pipeline, security | https://slsa.dev/spec/v1.2/build-track-basics |
| S-03 | Secure Software Development Framework (SSDF), NIST SP 800-218 | National Institute of Standards and Technology | 1.1, 2022-02 | standard | not subject to copyright in the United States | full | security | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf |
| S-04 | Strategies for the Integration of Software Supply Chain Security in DevSecOps CI/CD Pipelines, NIST SP 800-204D | National Institute of Standards and Technology | 2024-02 | standard | not subject to copyright in the United States | full | pipeline, security | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204D.pdf |
| S-05 | OWASP Top 10 CI/CD Security Risks | OWASP Foundation | no version found; read 2026-10-11 | foundation | not found on the main page | part | security, pipeline | https://owasp.org/www-project-top-10-ci-cd-security-risks/ |
| S-06 | OpenSSF Scorecard, documentation of the checks | Open Source Security Foundation | no version found; read 2026-10-11 | foundation | not found on the page | part | security, pipeline | https://github.com/ossf/scorecard/blob/main/docs/checks.md |
| S-07 | Open Source Project Security Baseline (OSPS Baseline) | Open Source Security Foundation | 2026-08-28 | foundation | not found | part | security, pipeline, quality | https://baseline.openssf.org/ |
| S-08 | ISO/IEC/IEEE 32675:2022, DevOps: building reliable and secure systems | ISO, IEC and IEEE | 2022 | standard | paid | no | operations | https://www.iso.org/standard/83670.html |
| S-09 | Site Reliability Engineering, chapters Release Engineering, Service Level Objectives, Monitoring Distributed Systems | Google; O'Reilly Media | 2017 | research | CC BY-NC-ND 4.0 | part | operations | https://sre.google/sre-book/release-engineering/ |
| S-10 | DORA: guide to the software delivery performance metrics, and the catalog of capabilities | DORA, a program of Google Cloud | updated 2026-01-05 | independent | CC BY 4.0 | part | operations, quality | https://dora.dev/guides/dora-metrics-four-keys/ |
| S-11 | ISO/IEC 25010:2023, product quality model | ISO and IEC | 2023 | standard | paid | no | quality | https://www.iso.org/standard/78176.html |
| S-12 | Software Engineering at Google, chapters Code Review, Testing Overview, Continuous Integration | Google; O'Reilly Media | no date found; read 2026-10-11 | research | CC BY-NC-ND 4.0 | part | quality, pipeline | https://abseil.io/resources/swe-book/html/ch23.html |
| S-13 | Continuous Integration (article) | Martin Fowler | 2024-01-18 | independent | not found | part | quality, pipeline | https://martinfowler.com/articles/continuousIntegration.html |
| S-14 | slsa-github-generator, the documentation of the project (sample) | SLSA project | no version found; read 2026-10-11 | foundation | Apache-2.0 | part | pipeline | https://github.com/slsa-framework/slsa-github-generator |
| S-15 | Kubernetes: design note KEP-3031 and the page about signed artifacts (sample) | Kubernetes project, Cloud Native Computing Foundation | no version found; read 2026-10-11 | foundation | not found | part | pipeline | https://www.kubernetes.dev/resources/keps/3031/ |
| S-16 | attest-build-provenance, the documentation of the project (sample) | GitHub | no version found; read 2026-10-11 | vendor | not found | part | pipeline | https://github.com/actions/attest-build-provenance |

## 3. Strategy

High level, for the agent that runs the work. One page.

### 3.1 Goals

- Each concern of operation, security and quality has a check that runs before the delivery, in the pipeline or earlier.
- The path from a change of the source to a released artifact can be verified by a person who did not make it: the artifact has signed provenance from a hosted build platform.
- The build, the test and the packaging are separate steps, and no step gets a credential that it does not need.
- Each view has its basic practices on level 1. The risk of the project on each dimension decides how far the project goes past level 1.
- The project knows its distance to each target as a list of adopted items whose check fails.

### 3.2 Order of the work

1. Find the contexts and the answers to the questions of the risk dimensions: they decide which items apply, thus this is the first step.
2. Protect the repository: version control for each file, a protected primary branch, strong authentication, no secret in the repository. Each later step trusts the repository.
3. Make the build automated, and start it with its tests on each change. A check can only move to the start of the work if a program runs it.
4. Separate the steps of the pipeline, and give each step only its credentials. Do this before the release job gets signing rights.
5. Build each release on a hosted build platform with signed provenance: this is the baseline level of the target. Add the verification by the user of the artifact.
6. Add the automated analyses to the pipeline: secrets, static analysis, dependencies. Write the policy for the findings.
7. Complete the release: version, record of changes, list of components, archive.
8. For a service that the team operates: plan the operation, automate the deployment, and add rollback, monitoring, incident analysis and recovery tests.
9. Isolate the builds from each other and from the signing secrets: this is the goal level of the target. It can need a different build platform, thus it comes after the basics.
10. Measure the project against the targets, and write the plan for the items whose check fails.

### 3.3 Decisions that depend on context

| Decision | Depends on | Options | Sources |
|---|---|---|---|
| Which build level to reach first | exposure; build platform | Build L1 with the current platform; Build L2 on a hosted platform; Build L3 on a platform with isolated builds | S-02 Build: Track Basics |
| How a change gets its approval | team size; openness of the repository | approval by one person who is not the author; review by two trusted persons; a share of reviewed changes when the project has one maintainer | S-02 Source: Requirements; S-06 Code-Review check; S-07 version page, Level 3; S-13 |
| What the team does when the build of the primary branch fails | team size; number of changes each day | stop each merge until the build is correct; correct the build at once and do not stop each commit | S-13 Fix Broken Builds Immediately; S-12 Continuous Integration |
| How fast the build of a change must be | size of the product | one fast build with a time limit; a fast first build and slower later stages | S-13 Keep the Build Fast |
| How large one change can be | team size | a limit of lines that the team sets; no limit, with a review of each change | S-12 Code Review |
| How a change to production gets its approval | duty from outside; criticality | peer review and automated checks; a formal change request with a control board | S-10 catalog of capabilities; S-01 pages 193, 194 |
| How a new release reaches the users | kind of delivery; criticality | release in stages to a part of the users; a switch for each new function; one release for all users with a rehearsed rollback | S-01 page 160; S-13 |
| Which limit applies to a finding of an analysis | criticality; duty from outside | the project writes its limits into a policy; no source gives a number | S-07 version page, Level 3 |
| How the delivery measures are used | none | as information for each service; not as a goal and not for the comparison of teams | S-10 metrics guide |
| How the provenance reaches the user | kind of delivery | through the package ecosystem; beside the release artifacts | S-02 Build: Requirements, Producer; S-14 |
| Which component generates the provenance | build platform | the attestation function of the platform; a reusable workflow of a foundation project; a builder of the project in an isolated job | S-14; S-16; S-15 |

### 3.4 Where the sources disagree

| Question | Positions | How this recipe handles it | Sources |
|---|---|---|---|
| What DevSecOps means | The body of knowledge and the NIST publication use the name for the integration of security into development and operations, with automation. The owner means the shift left of three concerns: operations, security and quality. | The recipe follows the owner. The view `quality` comes from the sources of its own field: the knowledge areas of quality and testing, and the practice sources of continuous integration. | S-01 pages 159, 266; S-04 page 11; S-01 pages 139, 247; S-12; S-13 |
| If the build track asks for separate steps for build, test and packaging | The owner refers to the SLSA build track for this rule. The readers found no such rule on the pages of the build track: the track asks that a build cannot reach the signing secrets and that builds do not influence each other. Other sources ask that each pipeline and each step gets only the credentials that it needs, and that code that is not trusted gets no credentials. | The rule stays, because it is constraint K-2 of the charter. Item C-07 holds it, with the requirements about credentials. The recipe does not cite the build track for the separation of the steps. | S-02 Build: Track Basics; S-02 Build: Requirements; S-05 CICD-SEC-4, CICD-SEC-6; S-07 version page, Level 1 |
| If each change needs the approval of a second person before the merge | The baseline, the scorecard and the source track ask for an approval by a person who is not the author. The article about continuous integration tells teams to think again about a review practice that was made for open source. The scorecard says that a review of all changes is not feasible for some projects, such as a project with one active participant. | Principle P-3 decides: the item follows the governance sources. Item C-03 is above level 1 on the dimension `exposure`, and a decision of section 3.3 gives the options for one maintainer. | S-07 version page, Level 3; S-06 Code-Review check; S-02 Source: Requirements; S-13 |
| If a failed test or a failed build stops each change | The article says that a broken build of the primary branch is corrected at once. The baseline says that the checks pass before a commit to the primary branch. The book says that to stop all commits on a failed build is probably wrong, and that a change that disables a failed test can be accepted more easily. | Principle P-1 decides against principle P-7: the check stays before the merge (items C-05 and C-39). The items name the practice only; a decision of section 3.3 gives the options. | S-13 Fix Broken Builds Immediately; S-07 version page, Level 2; S-12 Continuous Integration |
| How a change to production is approved | The body of knowledge describes change requests that a control board approves. The catalog of capabilities says: replace a heavyweight change approval with peer review. | Principle P-3 decides against principle P-7 where a duty from outside asks for a formal approval; in other contexts the lighter option applies. Item C-65 names the practice only; a decision of section 3.3 gives the options. | S-01 pages 193, 194; S-10 catalog of capabilities |
| If a scale is used to compare projects | The scorecard gives a score for each check. The baseline says that it is not a tool for scores and that it is not for the comparison of projects. The delivery guide says that its measures are not goals. | The recipe uses each scale to find the distance of one project to its own target. It does not compare projects, and it does not make a delivery measure a goal. | S-06 checks documentation; S-07 FAQ; S-10 metrics guide |
| If a hermetic build that can be reproduced is a requirement | The NIST framework names reproducible builds as an example of a task. The SLSA specification says that hermetic and reproducible builds may or may not become a requirement of a future level. The owner names them as an aspiration beyond the goal. | Item C-17 holds the practice. The calculation does not admit it; the owner can admit it. No approved level of the target asks for it. | S-03 page 16; S-02 Future directions; S-09 Release Engineering |
| If a reusable component for provenance reaches the goal level alone | The specification says that Build L3 needs a platform with isolated builds. The sample project says that its reusable workflows alone do not meet all requirements of Build L3, because they do not cover distribution and verification, and that the project is no longer actively maintained. | The recipe judges the practice (items C-08, C-09, C-11), not the component. The selection of a component is knowledge of one product and goes to an implementation skill, which examines the maintenance state of the component. | S-02 Build: Track Basics; S-14 |
| How long one build can take, and how large one change can be | One source gives about ten minutes for the build of a change. One source gives about 200 lines for a change. No second source gives a number. | The items C-05 and C-51 name no number. Two decisions of section 3.3 hold the options. | S-13 Keep the Build Fast; S-12 Code Review |

## 4. Checklist

Generic items, valid across the contexts of section 1. One short sentence each. The way to do an
item that depends on context belongs in 3.3; an item for one product belongs in an
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
| C-01 | Each file that makes the product is in version control: source, tests, build definition and pipeline definition. | A change that is not recorded cannot be reviewed, built again or undone. | pipeline | 1 | authority (2) | The repository holds the build definition and the pipeline definition; the release is built from a commit. | S-01 page 256; S-07 Level 1, QA-01.01, Level 1, QA-05.01 and more; S-13 Automate the Build, Put everything in a version controlled mainline |
| C-02 | The primary branch is protected against a direct commit, a rewrite of its history and a deletion. | One account can change the released source without a trace. | pipeline | 1 | authority (4) | The settings of the repository refuse a direct push, a forced push and a deletion on the primary branch. | S-02 Organization requirements, History section and more; S-05 CICD-SEC-4, Statements on Secrets and; S-06 Branch-Protection check, remediation, Branch-Protection check, tier 1; S-07 Level 1, AC-03.01, Level 1, AC-03.02 |
| C-03 | A person who is not the author approves each change before it enters the primary branch. | One person or one stolen account can put a fault or malicious code into the product. | pipeline | 2, exposure | authority (4) | The settings of the repository require one approval or more from a person who is not the author. | S-02 Two-party review section; S-04 pages 21, 26; S-06 Branch-Protection check, tier 2, Branch-Protection check, tier 4 and more; S-07 Level 3, QA-07.01 |
| C-04 | One automated command builds the product from a clean copy of the repository. | A build that depends on a person or on one machine cannot be repeated or verified. | pipeline | 1 | authority (2) | A new clone and the documented command give the artifacts without a manual step. | S-02 Build L1, Producer, Follow a consistent build process; S-07 Level 2, DO-07.01; S-13 Automate the Build |
| C-05 | Each change to the primary branch starts an automated build with tests, and the team corrects a broken build before other work. | Faults of integration stay hidden and become expensive. | pipeline | 1 | authority (2) | The pipeline definition starts on each change of the primary branch; the last run of the primary branch is green. | S-01 page 143; S-12 Chapter, Section on distributed systems, Chapter, Section on feedback and more; S-13 Every Push to Mainline Should Trigger a Build, Fix Broken Builds Immediately and more |
| C-06 | A hosted build platform builds each release artifact; no person builds a release on a personal computer. | A release from a personal computer has no verifiable origin and can be changed after the build. | pipeline | 1 | authority (2) | The release artifacts come from a run of the hosted pipeline; the provenance names the platform. | S-02 Build L1, Build L2 and more; S-04 page 17 |
| C-07 | The build, the test and the packaging run as separate steps, and each step gets only the credentials that it needs. | Code that runs in the build or in the tests can steal the credentials of the release. | pipeline | 1 | authority (3) | The pipeline definition has separate jobs; the permissions are set for each job; no secret is given to the build job or the test job. | S-05 CICD-SEC-6, Recommendations, CICD-SEC-4, Statements on Secrets and; S-06 Token-Permissions check, remediation; S-07 Level 2, AC-04.01, Level 3, AC-04.02 |
| C-08 | The build platform generates provenance for each release artifact and signs it. | A consumer cannot know where and how an artifact was built, and a changed artifact is not found. | pipeline | 1 | authority (3) | Each release artifact has a signed provenance file that names the builder, the source and the digest. | S-02 Build L1, Build L2 and more; S-03 page 19; S-04 pages 25, 26 |
| C-09 | Each build runs in a new, isolated environment that cannot reach the signing secrets or change a different build. | A build can forge the provenance or poison a later build. | pipeline | 2, exposure | authority (2) | The build platform documents an isolated, ephemeral environment for each run; the signing runs outside the steps that the project defines. | S-02 Build L3, Build Platform, Provenance is Unforgeable (L3) and more; S-04 page 25 |
| C-10 | Each release has a unique version, a record of its changes, and a digest or a signature for each artifact. | Users cannot tell which release they have, what changed, or if the file is complete. | pipeline | 1 | authority (4) | Each release has a version identifier, a change log and a digest or signature file. | S-03 page 19; S-04 page 30; S-06 Signed-Releases check, remediation; S-07 Level 2, BR-02.01, Level 2, BR-04.01 and more |
| C-11 | The user of an artifact verifies its signature or its provenance before the artifact is used or deployed. | A signature that nobody verifies stops no attack. | pipeline | 1 | authority (3) | The deployment or the installation instruction has a verification step that fails on a wrong signature. | S-02 Build L2, Build Platform, Provenance is Authentic (L2); S-04 pages 18, 23, 29; S-07 Level 3, DO-03.01, Level 3, DO-03.02 |
| C-12 | The artifact that passed the tests is the artifact that is released; it is not built again. | A second build can differ from the tested one. | pipeline | 1 | authority (1) | The digest of the released artifact is equal to the digest of the tested artifact. | S-12 Chapter, Section on continuous delivery |
| C-13 | Each release has a list of its components, and the list is delivered with the release. | Users cannot find out if a vulnerable component is in the product. | pipeline | 2, evidence duty | authority (2) | Each release has a component list in a standard format. | S-04 page 13; S-07 Level 1, QA-02.01, Level 3, QA-02.02 |
| C-14 | The versions of the dependencies and of the build tools are pinned, and an automated process proposes their updates. | A dependency that changes without notice breaks or compromises the build; a pinned version that is not updated keeps known faults. | pipeline | 1 | authority (3) | Lock files are in the repository; the pipeline refers to its tools by a fixed version or digest; an update tool is configured. | S-01 page 103; S-06 Pinned-Dependencies check, remediation; S-07 Level 2, BR-05.01; S-13 Keep the Build Fast |
| C-15 | The source control system records who made and who approved each change, and can give this record as evidence. | The history of the source can be disputed or forged. | pipeline | 2, exposure | authority (3) | The source control system gives an attestation or a log of identity and approval for each revision of the primary branch. | S-02 Organization requirements, Source Control System section and more; S-04 pages 26, 29; S-07 Level 1, QA-01.02 |
| C-16 | The configuration items, their baselines and their change requests are identified, controlled and audited. | A delivered configuration does not agree with its specification, and nobody can show what was delivered. | pipeline | not admitted | authority (1) | A configuration management plan exists; the records of the audits exist. | S-01 pages 53, 59, 179, 185, 187, 188, 189, 190 and more |
| C-17 | The build is hermetic and can be reproduced. | A build that reads from the network or from the machine can get an input that nobody examined, and a second party cannot confirm the result. | pipeline | not admitted | authority (2) | Two builds of one commit give the same digest; the build runs without network access. | S-01 page 197; S-02 Build Platform, Isolation strength (L3), Build L4 |
| C-18 | The security requirements of the software and of its development are written and kept current. | Security is added late or not at all, because nobody stated what is necessary. | security | 2, criticality | authority (4) | A document of security requirements exists and has a date of review. | S-01 pages 47, 264, 266; S-03 pages 14, 20; S-04 page 24; S-07 Level 3, QA-04.02; S-10 Pervasive security entry, catalog list |
| C-19 | The roles and the duties for security are assigned, and these persons get training. | Nobody is responsible for a security task, or the responsible person cannot do it. | security | 2, criticality | authority (3) | A document names the roles; a record of training exists. | S-01 pages 159, 266; S-03 pages 13, 15; S-04 page 24 |
| C-20 | The management decides by risk which security practices apply, and commits resources to them. | The practices are chosen at random or are not funded. | security | 2, criticality | authority (3) | A recorded decision names the selected practices and the accountable person. | S-01 pages 159, 210, 265; S-03 pages 8, 12, 16; S-04 pages 17, 18, 20 |
| C-21 | Access to the repository, the pipeline and the release needs multi-factor authentication and the least privilege. | One stolen password gives control of the product. | security | 1 | authority (5) | The settings require multi-factor authentication; the list of accounts with write or administrator rights is short and reviewed. | S-02 Organization requirements, Identity management section and more; S-03 page 18; S-04 pages 21, 23, 24, 26; S-05 CICD-SEC-6, Recommendations; S-07 Level 1, AC-01.01, Level 1, AC-02.01 and more |
| C-22 | No secret is in the repository or in the output of the pipeline, and an automated scan looks for secrets in each change. | A secret in the history of a repository stays readable and is used for an attack. | security | 1 | authority (4) | A secret scan runs on each change and blocks a finding; a scan of the history finds nothing. | S-02 Build Platform, Provenance is Unforgeable (L3); S-04 pages 28, 29; S-05 CICD-SEC-6, Recommendations; S-07 Level 1, BR-07.01, Level 3, BR-07.02 |
| C-23 | The pipeline does not give credentials or privileged resources to code or input that is not trusted. | A contribution from outside runs in the pipeline and takes the secrets. | security | 1 | authority (4) | The pipeline definition gives no secret to a run that a change request from outside starts; inputs are not put into a script without a check. | S-04 pages 27, 39; S-05 CICD-SEC-4, Statements on Secrets and; S-06 Dangerous-Workflow check, remediation; S-07 Level 1, BR-01.01, Level 1, BR-01.03 and more |
| C-24 | An automated static analysis looks for security weaknesses in each change. | Known types of weakness reach the release although a program can find them. | security | 1 | authority (4) | The pipeline has a static analysis job for each language of the product; its findings block or are recorded. | S-01 page 268; S-03 pages 23, 27; S-04 pages 21, 28, 40; S-07 Level 3, VM-06.01, Level 3, VM-06.02 |
| C-25 | An automated analysis looks for known vulnerabilities and license problems in the dependencies, and a policy says how to act on a finding. | The product ships a component with a known vulnerability. | security | 1 | authority (3) | The pipeline has a dependency analysis job; a written policy gives the limit for each severity. | S-01 page 103; S-04 pages 21, 29, 30, 36; S-07 Level 3, VM-05.01, Level 3, VM-05.02 and more |
| C-26 | The executable software is tested for vulnerabilities, with methods chosen by risk. | Weaknesses that only show at run time are not found before an attacker finds them. | security | 2, criticality | authority (2) | A dynamic test, a fuzz test or a penetration test has a recorded result for the release. | S-01 page 268; S-03 pages 24, 25 |
| C-27 | The design is examined for security risks before the construction, and the result is recorded. | A weakness of the design is expensive to correct after the construction. | security | 2, criticality | authority (3) | A threat model or a record of the design review exists and is not older than the last major change. | S-01 pages 267, 268, 269, 333; S-03 pages 20, 21, 27; S-07 Level 2, SA-01.01, Level 2, SA-03.01 and more |
| C-28 | Third-party components come from a known origin, and the project verifies them before use. | A malicious or changed component enters the product. | security | 1 | authority (4) | The project takes components only from named registries; the build verifies digests or signatures. | S-01 pages 103, 212; S-03 pages 8, 21, 22; S-04 page 21; S-07 Level 2, DO-06.01 |
| C-29 | The code follows secure coding practices and uses the protective features of the compiler and the build tools. | Avoidable weaknesses are written into the code. | security | 1 | authority (2) | The build enables the documented protective options and treats warnings as errors; the coding rules are written. | S-01 pages 107, 267, 268; S-03 pages 20, 22, 23 |
| C-30 | The software has secure default settings, and they are documented. | An installation with default settings is open to attack. | security | 2, exposure | authority (2) | The documentation lists each security setting with its default. | S-01 page 268; S-03 page 25 |
| C-31 | The environments for development, build and distribution are separated and hardened. | An attacker moves from a weak environment to the build or to production. | security | 3, criticality | authority (3) | An inventory names each environment, its access rules and its separation. | S-02 Platform Operations track; S-03 pages 16, 17, 18; S-04 pages 20, 21, 24, 25 |
| C-32 | The pipeline keeps a log of its actions and of the access to it, and a person or a program examines the log. | An attack on the pipeline is not seen. | security | 2, evidence duty | authority (2) | The logs of the pipeline are kept for a stated time; an alert rule or a review record exists. | S-02 Organization requirements, Platform Operations track; S-04 pages 21, 30 |
| C-33 | The project defines the security checks that a release must pass, and keeps the results as evidence. | Nobody can show that a release passed its checks. | security | 2, evidence duty | authority (3) | A written list of release criteria exists; each release has the stored results. | S-02 Organization requirements; S-03 pages 16, 17; S-04 pages 11, 20, 22, 23, 25, 27, 28, 30 |
| C-34 | Each release is archived with its integrity data and is protected against a change. | An old release cannot be examined, or is replaced without a trace. | security | 1 | authority (4) | The store of the releases is immutable or protected; each archived release has its digest. | S-01 pages 192, 195; S-03 pages 8, 13, 19; S-04 page 26; S-07 Level 1, BR-03.01, Level 1, BR-03.02 |
| C-35 | The project publishes how to report a vulnerability, and has a process to answer and to disclose. | A finder has no safe way to report, and the vulnerability becomes public before a correction. | security | 1 | authority (2) | A security policy file with a private contact exists. | S-03 pages 25, 26, 27; S-07 Level 1, DO-02.01, Level 1, VM-02.01 and more |
| C-36 | Each vulnerability is recorded, assessed by risk and corrected, and its root cause is removed. | The same type of vulnerability returns. | security | 1 | authority (3) | The issue tracker has a record for each vulnerability, with the decision and the root cause. | S-03 pages 8, 13, 26, 27; S-04 page 13; S-07 Level 3, VM-04.02 |
| C-37 | The project documents its governance: roles, how to contribute, the license, and how long a release gets security corrections. | Users and contributors cannot judge the project or their own duties. | security | 2, exposure | authority (3) | The repository has the files for license, contribution, roles and support period. | S-01 page 281; S-06 Contributors check, remediation, Stakeholders and Roles, Maintainers; S-07 Level 1, DO-01.01, Level 1, GV-02.01 and more |
| C-38 | An information security policy exists, the staff know it, and security incidents go through the incident process. | A security incident gets no response, or a change removes a control. | security | 2, criticality | authority (4) | The policy document exists; the incident records include security incidents. | S-01 pages 159, 264, 265, 266, 267, 281, 328, 335; S-02 Overview, Security Best Practices; S-03 pages 8, 13, 26; S-04 page 20 |
| C-39 | Each change comes with automated tests, and the tests pass before the change enters the primary branch. | A fault enters the primary branch and is found late. | quality | 1 | authority (5) | The settings of the repository require the test job to pass before a merge. | S-01 pages 134, 155, 162, 164; S-04 pages 27, 28; S-06 Branch-Protection check, tier 3; S-07 Level 2, QA-03.01, Level 2, QA-06.01 and more; S-12 Chapter, Section on presubmit, Chapter, Section on disabled tests and more; S-13 Keep the Build Fast, Make the Build Self-Testing |
| C-40 | A test strategy names the test levels, the environments and the criteria that tell when the testing is sufficient. | The testing is too little or without a goal. | quality | 2, criticality | authority (3) | A test strategy document exists and names levels, environments and completion criteria. | S-01 pages 100, 118, 120, 124, 135, 136, 137, 139 and more; S-07 Level 3, QA-06.02; S-12 Chapter, Section on distributed systems, Pitfalls of a Large Test Suite and more |
| C-41 | The tests give the same result on each run and do not depend on the person or the machine that runs them. | Unstable tests hide real faults, and the team stops to trust the pipeline. | quality | 1 | authority (2) | The pipeline reports the tests that change their result without a change of the code; the list is empty or has an owner. | S-01 page 137; S-12 Chapter, Section on test design, Chapter, Section on hermetic tests |
| C-42 | The test environment is equivalent to the production environment. | A fault shows only in production. | quality | 2, criticality | authority (2) | The test environment and the production environment are made from the same definition. | S-01 page 131; S-12 Chapter, Section on production; S-13 Test in a Clone of the Production Environment |
| C-43 | An automated analysis examines the code quality and the coding standards on each change. | Reviews spend time on what a program can find. | quality | 1 | authority (1) | The pipeline has a job for the static analysis of style and quality. | S-01 page 326; S-13 Make the Build Self-Testing |
| C-45 | The quality requirements are written with a measure for each one. | Nobody can tell if the product is good enough. | quality | 2, criticality | authority (1) | A list of quality requirements exists; each one names its measure. | S-01 pages 57, 211, 248, 256 |
| C-47 | The project plans its quality assurance early, in proportion to the criticality of the software. | Quality work starts too late, or its depth does not agree with the risk. | quality | 2, criticality | authority (1) | A quality plan exists and names the criticality of the software. | S-01 pages 136, 179, 208, 211, 213, 247, 248, 250 and more |
| C-48 | Work products get a review: requirements, design, code and tests. | A defect in an early work product goes into each later one. | quality | 2, criticality | authority (4) | Review records exist for the work products of the last release. | S-01 pages 58, 257, 259; S-02 Source Control System section, Two-party review section; S-03 page 23; S-12 Simpler Reviews, summary, Overview (the page location is not and more; S-13 How do we do pull requests and code reviews? |
| C-49 | Defects are recorded and measured, and their causes are analysed. | The same defects return, and nobody knows the trend. | quality | 1 | authority (2) | The issue tracker has the defects with their cause; a count for each release exists. | S-01 pages 213, 248, 253, 254; S-12 Chapter, Section on cost |
| C-50 | The test assets are in version control and are linked to the requirements and the code that they test. | Tests and code go out of step, and a requirement stays without a test. | quality | 1 | authority (2) | The tests are in the repository; a requirement or a change names its tests. | S-01 pages 135, 136, 192; S-12 Pitfalls of a Large Test Suite |
| C-51 | Changes are small and are integrated into the primary branch one time each day or more. | Large changes that are integrated late cause conflicts and hide faults. | quality | 1 | authority (1) | The age of the open branches and the size of the merged changes are below the limit that the team set. | S-12 summary, Best practices; S-13 Everyone Pushes Commits To the Mainline Every |
| C-52 | The tests cover the specific risks of the domain and the technology of the product. | A risk of the domain is not tested, because the general tests do not know it. | quality | 3, criticality | authority (1) | The test strategy names the domain risks and their tests. | S-01 pages 141, 142, 143 |
| C-53 | The operation is planned from the start of the development, with the requirements for operation and maintenance. | The product cannot be operated as it was built. | operations | 2, criticality | authority (2) | An operations plan or a concept of operations exists before the first release. | S-01 pages 154, 156, 157, 158, 161, 163; S-09 Start Release Engineering at the Beginning |
| C-54 | The deployment is automated, and each environment is made from the same definition in version control. | Manual steps and different environments cause faults in production. | operations | 2, criticality | authority (3) | The repository holds the definition of the environments; the deployment runs from the pipeline. | S-01 pages 152, 155, 157, 158, 160, 162; S-04 pages 30, 31; S-12 Chapter, Section on configuration; S-13 Automate Deployment |
| C-55 | Each release can be rolled back, and the rollback is rehearsed before the deployment to production. | A bad release cannot be removed fast. | operations | 2, criticality | authority (1) | A rollback procedure exists; a record of its last rehearsal exists. | S-01 page 160; S-13 Hide Work-in-Progress |
| C-56 | A new release reaches the users in a controlled way that limits the harm of a fault. | A fault reaches all users at the same time. | operations | 2, criticality | authority (1) | The deployment definition has stages or a switch for each new function. | S-01 pages 157, 162 |
| C-57 | Monitoring and telemetry collect data at each layer of the service, and an alert goes to a person only when action is necessary. | A failure is not seen, or the staff ignore alerts because there are too many. | operations | 2, criticality | authority (2) | Dashboards and alert rules are in version control; each alert names an action. | S-01 pages 161, 162, 164, 333; S-09 Setting Reasonable Expectations / As Simple as, Tying These Principles Together and more |
| C-58 | The service has agreed service level targets, and the project measures them. | Nobody knows if the service is reliable enough. | operations | 2, criticality | authority (3) | A document gives the targets; a report gives the measured values. | S-01 page 158; S-09 Choosing Targets; S-12 Chapter, footnote on uptime |
| C-59 | Each incident is recorded and analysed after it ends, and the corrections are done. | The same incident occurs again. | operations | 1 | authority (2) | Incident records with their analysis and their actions exist. | S-01 pages 155, 161; S-09 Monitoring for the Long Term |
| C-60 | Backup, recovery and failover exist and are tested at regular intervals. | Data or the service cannot be restored. | operations | 2, criticality | authority (1) | A record of the last restore test exists and is not older than the stated interval. | S-01 pages 158, 159, 331 |
| C-61 | The capacity and the availability of the service are planned from measured data. | The service fails under a load that was foreseeable. | operations | 2, criticality | authority (1) | A capacity plan exists and refers to measured data. | S-01 page 158 |
| C-62 | The release process is defined, automated and usable by the team without a specialist. | A release depends on one person and is done differently each time. | operations | 1 | authority (3) | A documented release procedure exists; the pipeline does the release from a tag or a decision. | S-01 pages 101, 243; S-04 pages 24, 36; S-09 Start Release Engineering at the Beginning, Enforcement of Policies and more |
| C-63 | The project measures its delivery performance for each service: throughput and instability. | The team cannot see if its delivery gets better or worse. | operations | 2, criticality | practice | A report gives the measures for the last period. | S-10 section 2 |
| C-64 | The operations work has documented procedures, assigned roles and trained staff. | The operation depends on the memory of single persons. | operations | 2, criticality | authority (1) | Documents of the procedures and of the roles exist. | S-01 pages 153, 154, 156 |
| C-65 | The risks of operation are managed, and a change to production does not weaken a control. | A change causes an outage or opens a gap. | operations | 2, criticality | authority (1) | Each change to production has a record with its risk and its approval or its automated checks. | S-01 pages 151, 159, 162; S-10 Streamlining change approval entry, catalog list |
| C-66 | The suppliers that the service depends on are known and coordinated. | A supplier fails, and nobody knows the effect or the contact. | operations | 2, criticality | authority (2) | A list of suppliers with their service and contact exists. | S-01 page 156; S-03 pages 8, 12, 14 |
| C-67 | The software is designed for operation: it handles failures and can be deployed in small independent parts. | One failure stops the whole service, and each deployment is a large risk. | operations | 3, criticality | authority (1) | The design document describes the failure handling and the units of deployment. | S-01 pages 159, 161, 335 |
| C-68 | The requirements are elicited, written, validated and managed. | The team builds the wrong product. | quality | 3, criticality | authority (1) | A list of requirements exists, with a record of its validation. | S-01 pages 44, 46, 48, 49, 50, 51, 52, 53 and more |
| C-69 | The architecture and the design are described and evaluated against the quality requirements. | The structure of the product cannot meet its quality requirements. | quality | 3, criticality | authority (2) | An architecture description and a record of its evaluation exist. | S-01 pages 69, 70, 77, 85, 86, 87, 90, 313 and more; S-07 Level 2, SA-02.01 |
| C-70 | The construction follows planned methods, standards and tools. | The code is inconsistent and hard to change. | quality | 2, criticality | authority (1) | The coding standards and the construction tools are documented. | S-01 pages 101, 106, 108, 109, 110, 209, 256, 321 and more; S-13 Automate the Build |
| C-71 | The maintenance is planned, with its process, its techniques and its measures. | The product cannot be changed after its release at a reasonable cost. | operations | not admitted | authority (1) | A maintenance plan exists. | S-01 pages 169, 171, 172, 173, 174, 175, 176, 177 and more |
| C-72 | The project is planned, estimated, measured and controlled, with its risks. | The project fails on time, cost or scope. | quality | 3, criticality | authority (1) | A project plan with estimates, measures and a list of risks exists. | S-01 pages 59, 203, 204, 205, 206, 207, 208, 209 and more |
| C-73 | The life cycle process and its models are defined, assessed and improved. | The team repeats the faults of its process. | quality | not admitted | authority (2) | A description of the process and a record of its last assessment exist. | S-01 pages 179, 208, 212, 214, 215, 222, 224, 226 and more; S-03 pages 8, 10, 11, 27; S-13 Introducing Continuous Integration, Can we run a CI Service on our feature branches? |
| C-74 | The engineers obey their professional, legal and ethical duties. | The work causes harm to persons or a legal consequence. | quality | 2, criticality | authority (2) | judgement | S-01 pages 248, 249, 250, 274, 277, 279, 280, 281 and more; S-12 summary, Best practices |
| C-75 | Decisions use an economic analysis of cost, benefit and risk. | Money and time go to the wrong work. | quality | 2, criticality | authority (1) | judgement | S-01 pages 249, 256, 282, 288, 289, 291, 292, 293 and more |
| C-76 | The engineers apply the foundations of computing, mathematics and engineering. | Basic technical faults enter the product. | quality | not admitted | authority (1) | judgement | S-01 pages 235, 236, 237, 241, 274, 313, 314, 316 and more |
| C-77 | A description of knowledge names its scope, its sources and its references. | A reader cannot examine the statements of the description. | quality | not admitted | authority (1) | judgement | S-01 pages 39, 40, 41, 388, 389, 390, 391, 392 and more |

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

- **Goal**: The project has a committed selection of the checklist items, a measured distance to each target that it selected, and a plan that brings the checks of operation, security and quality to the start of the work.
- **Reads first**: The contexts of the project: the size of the team, the users of the product, the kind of delivery, the openness of the repository, the build platform, a duty from outside and the development model. Then the answers of the owner of the project to the three risk questions (exposure, criticality, evidence duty), and the selection file of the project if it exists.
- **Applies**: The order of the work of the strategy, and each checklist item that the project adopted. For each item it runs the check or asks for a judgement, and it names the source unit that the item complies with. It keeps the build, the test and the packaging in separate steps and gives no step a credential that it does not need.
- **Delegates**: The setup of one pipeline platform; the generation and the signing of provenance; the signing and the verification of artifacts; the scan for secrets; the static analysis; the analysis of dependencies and their updates; the list of components; the measurement of the repository against a scale. An implementation skill provides each capability. The skill works alone when no implementation skill is installed: it then names the capability in the plan and does not write a setting.
- **Stops when**: The plan is written and shown to the owner of the project: the skill does not apply the plan. It stops also when a decision that depends on context needs a person, or when a source that it must read cannot be reached.

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
| The pipeline platform of the project (one skill for each platform) | Separate jobs, permissions for each job, protected branches, hosted release builds | C-02, C-03, C-05, C-06, C-07, C-21, C-23 | The command-line client of the platform |
| The artifact attestation function of the hosting platform (S-16) | Signed build provenance that is tied to the source repository | C-08, C-11 | The command-line client of the platform |
| slsa-github-generator (S-14) | Reusable workflows that generate provenance in an isolated job. The sample says that the project is no longer actively maintained: the skill examines this state before it proposes the component. | C-08, C-09 | The verifier program of the same project |
| Sigstore and cosign (S-15) | Signing of release artifacts without a long-lived key, and verification of the signature and of the identity of the signer | C-10, C-11 | none |
| OpenSSF Scorecard (S-06) | Scores of the checks of a repository, for the target `check scores` | C-02, C-03, C-07, C-10, C-14 | none |
| The programs that evaluate the OSPS Baseline (S-07 maintainer guidance) | Evaluation of a repository against the target `baseline level` | C-01, C-02, C-21, C-22, C-35 | A file with the security data of the project |
| The format of the source attestation of the SLSA source track (S-02 Source: Requirements) | The fields of the signed summary of the source level (requirements R-0738, R-0740, R-0747 to R-0754) | C-15 | none |
| The update framework that NIST SP 800-204D describes (S-04 pages 28, 37) | Protected distribution of updates with roles and keys (requirements R-0899, R-0900, R-0903, R-0904, R-0932) | C-11, C-34 | none |
| A secret scanner, a static analyser, a dependency analyser and a dependency update tool (one skill for each product that a project selects) | The automated analyses of each change | C-14, C-22, C-24, C-25 | none |
| A generator of the list of components (S-15 names one format) | The list of components of each release | C-13 | none |

## 6. Watch list

| Signal | Where to read it | Cadence |
|---|---|---|
| A new version of the SLSA specification, or a level above Build L3 | https://slsa.dev/spec/ | at each refresh |
| A new version of the OSPS Baseline | https://baseline.openssf.org/ | at each refresh |
| A revision of NIST SP 800-218 or NIST SP 800-204D | https://doi.org/10.6028/NIST.SP.800-218 and https://csrc.nist.gov/pubs/sp/800/204/d/final | at each refresh |
| A change of the list of risks | https://owasp.org/www-project-top-10-ci-cd-security-risks/ | at each refresh |
| A change of the checks or of their scores | https://github.com/ossf/scorecard/blob/main/docs/checks.md | at each refresh |
| A new version of the SWEBOK Guide | https://www.computer.org/education/bodies-of-knowledge/software-engineering | at each refresh |
| A change of the delivery measures | https://dora.dev/guides/dora-metrics-four-keys/ | at each refresh |
| The maintenance state of the sample projects | https://github.com/slsa-framework/slsa-github-generator and https://github.com/actions/attest-build-provenance | at each refresh |
| Access to the two ISO standards that no reader reached | https://www.iso.org/standard/83670.html and https://www.iso.org/standard/78176.html | at each refresh |

## 7. Decisions and changes

Dated. A reversed decision stays and is marked superseded. Name the models that made or
suggested a judgement, and the person who reviewed the findings and accepted the recipe.

| Date | Decision or change | Reason | Revisit when |
|---|---|---|---|
| 2026-10-11 | Not verified: the intent of the owner was not asked in the session of phase 1. The lines of "Intent of the owner" are the words of the owner from 2026-10-10 and 2026-10-11, and the session put each quote under its question. | The owner was not in the session. | The owner reviews the intent and the draft of the charter. |
| 2026-10-11 | For the review of the owner: the charter is a draft. The owner did not confirm its rows, and did not confirm the order of its principles. The research used the draft as it is and did not change it. | The owner was not in the session of phase 2. Only the owner changes the charter. | The owner reviews the charter in phase 3. |
| 2026-10-11 | For the review of the owner: in two rows of section 3.4 the order of the principles decided between two requirements. Question 1: is it correct that P-1 wins against P-7, so that a failed test or a failed build stops a change before the merge? Question 2: is it correct that P-3 wins against P-7, so that a change to production gets a formal approval where a duty from outside asks for it? | The owner did not confirm the order of the principles. | The owner confirms or changes the order. Then step 10 of phase 2 is done again. |
| 2026-10-11 | For the review of the owner: the research found a fourth view, `pipeline`, beside the three views that the owner named. The items of the target of the owner (build level) are in this view. | The body of knowledge has a knowledge area of its own for configuration management, build and release (S-01 pages 185 to 198), and the sources of the target are sources of this field (S-02; S-04). | The owner keeps, renames or removes the view. |
| 2026-10-11 | For the review of the owner: constraint K-2 of the charter refers to the SLSA build track for the separation of build, test and packaging. The readers found no such rule on the two pages of the build track that they read. Item C-07 holds the rule with the requirements about credentials of S-05, S-06 and S-07. | See section 3.4. | The owner confirms the wording of K-2, or names the place in the source. |
| 2026-10-11 | For the review of the owner: the calculation does not admit item C-17 (a hermetic build that can be reproduced). Part T-3 of the charter names this practice as an aspiration that is not a duty. The owner can admit the item. | The answers of risk and reward give a score below the admission threshold; the source of the target has no approved level that asks for the practice (S-02 Future directions). | The owner decides in phase 3. |
| 2026-10-11 | Ten boundaries are proposed, and no boundary is decided. Each requirement of the body of knowledge that belongs to a neighbouring field has an exit to one of the items C-68 to C-77, and the table "Proposed boundaries" of `vetting.md` names the requirements that each boundary would take. | The readers reported each requirement of the body of knowledge, also from the chapters outside the aspect. Only the owner decides a boundary. | The owner decides or declines each boundary. |
| 2026-10-11 | The identifiers C-44 and C-46 are not used. Two draft items (a measure of the tests, and tests of non-functional properties before a release) had no requirement line of a reader and were removed before the first commit. | An item without a requirement is not permitted, except an own rule. | A refresh finds a requirement for these practices. |
| 2026-10-11 | Judgement: the session (the largest model, in the role of the researcher) named the views, the stakeholders, the contexts, the risk dimensions, the boundaries and the checklist items, and gave the answers of risk and reward. Six helper agents (a mid-size model, in the role of a classifier) suggested the item and the stakeholder of each requirement line; the session examined samples of the result and changed one row. The readers of the sources and the second readers of the converted files were a small model; the second reader of the web sources was a mid-size model. | The procedure asks for the roles of the models that made or suggested a judgement. | A refresh. |
| 2026-10-11 | The agent types of the three readers were written in this session (step 3 of "Before the first run") and could not be started as sub-agents of the same session. Each reader ran as a new session of the agent product with the agent file of its type: the same tools and the same hook. | The agent product loads the agent files at the start of a session. | A new session loads the agent files. |
| 2026-10-11 | Not verified: ISO/IEC/IEEE 32675:2022 (S-08) and ISO/IEC 25010:2023 (S-11). The page of the issuer refused each reader (HTTP 403). No item cites these sources. The body of knowledge names both as references of its knowledge areas of operations and of quality. | The standards are paid, and the preview page cannot be read by a program. | The owner gives a file of the standard or of its preview. |
| 2026-10-11 | Not verified: DoD Enterprise DevSecOps Fundamentals, version 2.5. The conversion program could not retrieve the PDF file (HTTP 403). The document is not a source of section 2. | The address refuses a program. | The owner gives the file. |
| 2026-10-11 | Not verified: the exact words of each web source (S-02, S-05, S-06, S-07, S-09, S-10, S-12, S-13, S-14, S-15, S-16). The web tool of a reader returns a summary of a page and not its text. The cell Read of these sources is `part`. For S-05 the readers read the main page and the pages of two of the ten risks. For S-07 the readers did not read the checklist, the crosswalk and the earlier versions. | A limit of the web tool of the agent product. | A reader gets a converted file of the source. |
| 2026-10-11 | Not verified: the date of the start and of the last release of the three sample projects (S-14, S-15, S-16). The readers could not read the release lists. The published statistics of the practice were searched, and no source of statistics was read; the delivery guide (S-10) gives its measures without numbers. | The pages of the releases came back empty to the reader. | A refresh, or the vetting of an implementation skill. |
| 2026-10-11 | Not verified: the other standards and books that the body of knowledge names for the knowledge areas of the views (for example ISO/IEC/IEEE 12207, ISO/IEC 20000-1, IEEE 730, IEEE 1012, IEEE 828, ISO/IEC 27001, and the books that the reference lists on pages 166, 201, 262, 263 name). They were not retrieved. The book Site Reliability Engineering from the list on page 166 was read as S-09. | The standards are paid; the books are not public. | The owner gives a file. |
| 2026-10-11 | Not verified: the date of the body of knowledge (S-01). The manifest of the seeds (`factory/sota-research/references/seeds.md`, row `swebok`, cell "Version or date") gives one date, and the reader of pages 1 to 25 reports a different release date from page 1 of the converted file. Section 2 has the value of the manifest. | The session does not read a converted file, and the owner accepted the row of the manifest. | The owner examines page 1 of the file. |
| 2026-10-11 | The cell Stakeholder of each row of the table "Requirements" is a judgement where the reader reported the group as `not named`. The stakeholder `auditors and regulators` has five requirements; none of them is at a proposed boundary. | The sources name no group for most requirements. | The owner changes a stakeholder in phase 3. |
| 2026-10-11 | The second reading (step 12 of phase 2) corrected 9 of the 14 rows of the evidence record. The second readers reported 17 faults: 15 sentences that said more than the source, and 2 wrong locations. The rows of S-01, S-02, S-03, S-06, S-07, S-10, S-12, S-13 and S-15 were corrected. The rows of S-04, S-05, S-09, S-14 and S-16 had no fault. The same corrections were made in section 1, section 3.3, section 3.4 and section 5 of `spec.md`, in the list of the samples of `vetting.md`, and in 1 row of the table "Requirements" (R-1068). For the web sources the second reader had the same limit as the first reader: the web tool returns a summary. For S-07 the second reader did not get the last part of the version page. | The procedure asks for a second reader that did not read the source. | A refresh. |

## 8. Glossary

Terms that mean different things in the sources. One preferred form per meaning.

| Term | Meaning here | Other meanings in the sources |
|---|---|---|
| DevSecOps | The shift left of operational, security and quality concerns: the words of the owner. | The integration of security into development and operations, early and with automation (S-01 pages 159, 266; S-04 page 11). |
| level | A level of the checklist of this specification: 1, 2 or 3. | A build level or a source level of the target (S-02); a maturity level of the baseline (S-07); a capability level of a process (S-01 page 253). The recipe writes the full name of each scale. |
| provenance | The signed record of where and how an artifact was built: build provenance. | The record of how a revision of the source was made: source provenance (S-02 Source: Requirements). |
| producer | The person or the organization that owns a project and releases its software. | "Software producer" (S-03 page 5); "maintainer" and "project maintainer" for an open project (S-06; S-07). |
| hermetic | A build that gets each input from a declared place and gives the same result on a different machine (S-09 Release Engineering). | A test that does not depend on the user or on production (S-12 Continuous Integration). |
| pipeline | The automated path from a change of the source to a released artifact. | "CI/CD pipeline" (S-04; S-05); "toolchain" (S-03 page 16). |
| change failure rate | The share of deployments that cause a failure: one of the delivery measures. | "Change fail rate" (S-10 metrics guide); "change failure rate" (S-01 page 133). |

## Files beside this specification

- `charter.md`: the charter of the owner, if the owner gave one: the target, the principles
  with their priority, and the constraints. Only the owner changes it. Its template is
  `.specify/templates/overrides/charter-template.md`.
- `evidence.md`: for each source a summary of what it contributes, where in the source that
  is, the rows of this specification that it supports, and the date read. The summary is in
  Simplified Technical English and in the words of this kit. A second reader compares each
  line with the source. A quote stays only where the wording itself is the point.
- `vetting.md`: for each independent source the measured signals, the result of the rubric and
  the owner's confirmation; for each item the answers of the risk and reward calculation.
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
  - Each checklist item holds a requirement, or its cell "Admitted by" is `own rule`.
- `trial.md`: the record of the trials of the recipe on a project. This file is optional.
  - The table "Trials" has one row for each trial. Its columns are Id, Date, Project, Commit
    of the specification, and Plan. The cell "Plan" holds where the plan is, or `not kept`.
  - The table "Findings" has one row for each finding of the review of a plan. Its columns
    are Id, Trial, Viewpoint, Finding, Route and Status.
  - The viewpoint is one of the viewpoints of the review. The reviewer gives it.
  - The route is `recipe`, `tooling` or `implementation skill`.
  - The status is `open`, `corrected in <revision or commit>` or `declined: <reason>`.
