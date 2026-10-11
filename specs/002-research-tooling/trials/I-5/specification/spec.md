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
- **Field and disciplines**: software engineering; the operational, the security and the quality concerns
- **Intent of the owner**: the answers of the owner to the questions of phase 1. One line each:
  the words of the owner as a quote, with the date, or `(no answer)`.
  - `meaning`: "DevSecOps is about doing shift left of operational, security, and quality concerns." (2026-10-10)
  - `result`: "achieve SLSA draft highest levels" (2026-10-10)
  - `not wanted`: (no answer)
- **Agreed with the owner on**: 2026-10-11; the field: software engineering; the thing to build, in the
  words of the owner of 2026-10-10: "do the DevSecOps research and generate a skill". The owner was not
  in the session of 2026-10-11.

Found by the research, and reviewed by the owner with the other findings. Each line names its
source, or says `(judgement)`. A use case is chosen only when the recipe is applied to a project.

- **Stakeholders**: each group of persons that has an interest in the result or carries a duty
  for it. The research finds them in the body of knowledge of the field and in the sources.
  One line each: a short name, the concerns of the stakeholder for this aspect, and the source.
  - `developers`: write, review and integrate code; get fast feedback from the checks; manage the dependencies; take responsibility for the security of their systems (S-01 pages 101 to 107 and 266)
  - `operations engineers`: deploy, monitor and support the services; respond to incidents; keep the environments the same as production; some organizations use site reliability engineering and platform engineering for this work (S-01 pages 152 to 162)
  - `security staff`: define and examine the security properties; test the security; manage vulnerabilities; work faster and in smaller steps with the teams (S-01 pages 264 to 268)
  - `quality and test staff`: plan and automate the tests; set the criteria that a change must pass; for critical systems, possibly independent of the project (S-01 pages 135 to 138 and 255 to 258)
  - `release and configuration managers`: control the changes, the builds and the releases; reproduce earlier releases; keep the integrity of the delivered items (S-01 pages 186 to 198 and 243)
  - `management`: set the security policy; accept the risks; support training and the improvement after incidents (S-01 pages 159, 208 and 265)
  - `consumers`: the users, the customers and the acquirers that take the software: verify what they get; get advisories and updates; report problems (S-01 pages 156, 187 and 281; S-02 about)
  - `auditors and regulators`: get evidence that each release step was verified; set constraints for software that can affect public safety (S-01 pages 179, 187, 196 and 259)
  - `suppliers`: the third parties that supply components and services: get the requirements of the project; give provenance of what they deliver (S-01 pages 157 and 212; S-04 page 14)
- **Views**: the points of view that the aspect brings together. A view is a set of concerns
  of the aspect. The research aggregates the concerns of the stakeholders into the views. A
  concern that the owner named in the intent is in a view, or section 7 says why it is not.
  One line each: a short name, what the view is concerned with, the stakeholders whose
  concerns the view holds, and the source. Name the stakeholders in this form, before the
  source: `(stakeholders: [name], [name])`. Use the names of the field "Stakeholders".
  - `operations`: the deployment, the release, the rollback, the monitoring, the response to incidents and the service levels, and the planning of these during development (stakeholders: operations engineers, developers, management, consumers) (S-01 pages 151 to 164)
  - `security`: the security requirements, the secure construction, the security tests, the secrets and the management of vulnerabilities, through the whole life cycle (stakeholders: security staff, developers, management, consumers) (S-01 pages 264 to 269)
  - `quality`: the tests, the reviews, the static analysis and the criteria that each change must pass, as early as possible (stakeholders: quality and test staff, developers, auditors and regulators) (S-01 pages 117 to 141 and 246 to 260)
  - `supply chain`: the integrity and the origin of the source, the dependencies, the builds and the releases (stakeholders: release and configuration managers, developers, suppliers, consumers, auditors and regulators) (S-01 pages 103 and 185 to 198; S-02 about)
- **Contexts**: the values of each dimension that change the strategy. One line each.
  - `team`: one maintainer or a project of part-time contributors; one full-time team; an organization with separate security and operations staff (S-11 When we should not use Continuous Integration; S-07 Code-Review; S-01 page 163)
  - `delivery`: a service that the team deploys and operates; a package or an application that consumers install; a library (S-09 chapter 8, Deployment; S-10 chapter 24; S-13 item 12)
  - `platform of source and build`: a hosted platform that gives signed provenance and isolation; a build that the project operates itself (S-02 build-track-basics; S-03 build-env-track-basics)
  - `openness`: open source with outside contributors; closed source in one organization (S-13 items 14 and 15; S-05 page 27; S-07 CI-Tests)
  - `regulation`: no external rule; a contract, a law or a regulator that sets requirements (S-01 pages 187 and 394; S-06 2-g Privacy)
  - `criticality`: the integrity level of the software, from agreements among the acquirer, the supplier, the developer and other parties (S-01 page 251)
- **Risk dimensions**: the dimensions on which the risk of a project differs for this aspect.
  One line each: the name, the question that finds it out, the opinion of the kit on the
  answer, and the source.
  - `supply chain integrity`: Do other persons or systems install, deploy or build on the artefacts of the project? Opinion: if yes, go above level 1 on the supply chain view: signed provenance from a hosted build is the first step, because consumers cannot verify an artefact without it. (S-02 about; S-02 build-track-basics)
  - `exposure`: Does the software accept input from parties that are not trusted, or hold personal or sensitive data? Opinion: if yes, go above level 1 on the security view; scale the measures to how critical the data is. (S-01 page 264; S-06 2-g Privacy)
  - `availability`: Do users depend on a running service that the project operates? Opinion: if no, stop at level 1 on the operations view; if yes, automate deployment and rollback before you set service levels. (S-09 chapter 4; S-01 page 158)
  - `regulation`: Does a contract, a law or a regulator set requirements for the software or for its evidence? Opinion: if yes, the external rule decides the minimum; this kit does not replace it. (S-01 pages 187 and 394)
  - `team size`: Can a second person with knowledge of the code examine each change before the merge? Opinion: if no, automated checks do the work of the second person, and the levels that need a review by two persons are out of reach. (S-07 Code-Review; S-02 source-requirements, Level 4; S-11 When we should not use Continuous Integration)
- **Boundaries**: what each neighbouring aspect owns, and what this aspect keeps. One line each:
  a short name, what the neighbouring aspect owns and what this aspect keeps, the state, and
  the source. A boundary has one of two states. Write the state in one of these forms, before
  the source. `(proposed)`: the research proposes the boundary, and it takes no requirement.
  `(decided by the owner on <YYYY-MM-DD>)`: the owner decided the boundary on that date, and
  a requirement can go to it. Only the owner decides a boundary. A line without a state is
  proposed.
  - `secure design`: the neighbouring aspect owns threat modelling and the review of the design; this aspect keeps the written security requirements and their automated tests (proposed) (S-05 page 41; S-04 pages 20 and 21)
  - `security management of the organization`: the neighbouring aspect owns the security policy, the roles, the training and the risk assessment of the organization; this aspect keeps what one project does in its repository and its pipeline (proposed) (S-01 pages 159 and 265; S-04 pages 15 and 16)
  - `platform operation`: the neighbouring aspect owns the capacity, the backup, and the build and compute platforms themselves; this aspect keeps what the project asks of a platform and how it uses it (proposed) (S-01 pages 157 to 159; S-03 build-env-track-basics)
  - `privacy`: the neighbouring aspect owns the inventory and the legal treatment of personal data; this aspect keeps the scans and the tests in the pipeline (proposed) (S-06 2-g Privacy; S-01 page 281)
- **Targets**: the measurable results that a project reaches when it applies the recipe. The
  targets come from the sources in the research; the owner can name one in the intent. One
  line each: the name, the scale with its levels, the program or the method that measures it,
  and the source of the scale. If the sources give no target, write `(none found)` in place
  of the lines.
  - `SLSA build level`: levels Build L0 to Build L3 of the approved version: L1 provenance exists, L2 a hosted build platform generates and signs the provenance or gives a different means to verify its authenticity, L3 the build platform is hardened; a consumer, a package ecosystem or a monitor verifies the provenance against expected values (the source names slsa-verifier) (S-02 build-track-basics; S-02 verifying-artifacts)
  - `SLSA source level`: levels Source L1 to Source L4 of the approved version: L1 version controlled, L2 history and provenance, L3 continuous technical controls, L4 two-party review; a revision without a summary attestation has the level L0; the source control system or a provider of attestations issues the summary attestation, and a consumer verifies it (S-02 source-requirements; S-02 verifying-source)
  - `highest levels of the SLSA draft`: the target that the owner named in the intent; the working draft has four tracks with these highest levels: Build L3, Source L4, Build Environment L3, Dependency L3; the draft can change or be discarded, and the tracks Build Environment and Dependency are not in the index of the approved version; verification is by signed attestations (S-03 tracks; S-03 build-requirements; S-03 source-requirements; S-03 build-env-track-basics; S-03 dependency-track)
  - `Scorecard checks`: 20 checks, each with a risk level from Low to Critical; some checks give points up to 10; the program OpenSSF Scorecard measures them from the repository; some checks say that a low score is not a definitive sign of risk (S-07 each check; S-07 CI-Tests)
  - `best practices badge`: levels passing, silver and gold; the OpenSSF Best Practices program measures them; for open source projects (S-13 item 14)
  - `software delivery performance`: five measured values without levels: change lead time, deployment frequency, failed deployment recovery time, change fail rate, deployment rework rate; measured for one application or service; the source warns not to set them as goals (S-08 dora-metrics)
  - `service level objectives`: for each service a small number of indicators, each with a target value and its method of measurement; the team sets the values (S-09 chapter 4)
  - `SAMM maturity`: maturity levels for each of 15 security practices; assessment questions with four answers give a score for each activity, and the scores are averaged for each practice (S-14 model; S-14 the pages of the practices; S-14 getting-started step 2)

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
| S-01 | Guide to the Software Engineering Body of Knowledge (SWEBOK Guide) | IEEE Computer Society | 4.0a, 2025-09-25 | standard | copyright IEEE; individual use that is not commercial | full | all | https://www.computer.org/education/bodies-of-knowledge/software-engineering |
| S-02 | SLSA specification, approved version | OpenSSF, The Linux Foundation | 1.2; read 2026-10-11 | foundation | Community Specification License 1.0 | part | supply chain | https://slsa.dev/spec/v1.2/ |
| S-03 | SLSA specification, working draft | OpenSSF, The Linux Foundation | working draft; read 2026-10-11 | foundation | Community Specification License 1.0 | part | supply chain | https://slsa.dev/spec/draft/ |
| S-04 | NIST SP 800-218, Secure Software Development Framework (SSDF) | NIST | 1.1, 2022-02 | standard | not subject to copyright in the United States | full | security, supply chain | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf |
| S-05 | NIST SP 800-204D, Strategies for the Integration of Software Supply Chain Security in DevSecOps CI/CD Pipelines | NIST | 2024-02 | standard | not subject to copyright in the United States | full | supply chain, security | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204D.pdf |
| S-06 | OWASP DevSecOps Guideline | OWASP Foundation | v0.2; read 2026-10-11 | foundation | CC BY-SA 4.0 | part | security | https://owasp.org/www-project-devsecops-guideline/latest/ |
| S-07 | OpenSSF Scorecard, documentation of the checks | OpenSSF | main branch; read 2026-10-11 | foundation | not found | part | supply chain, security | https://github.com/ossf/scorecard/blob/main/docs/checks.md |
| S-08 | DORA, software delivery performance metrics and capabilities | DORA, Google Cloud | 2026-01-05 | research | CC BY 4.0 | part | operations, quality, security | https://dora.dev/guides/dora-metrics/ |
| S-09 | Site Reliability Engineering (book, online edition) | Google; O'Reilly Media | 2017 | research | CC BY-NC-ND 4.0 | part | operations | https://sre.google/sre-book/table-of-contents/ |
| S-10 | Software Engineering at Google (book, online edition) | Google; O'Reilly Media | not found; read 2026-10-11 | research | CC BY-NC-ND 4.0 | part | quality | https://abseil.io/resources/swe-book/html/toc.html |
| S-11 | Continuous Integration (article) | Martin Fowler | 2024-01-18 | independent | not found; copyright of the author | part | quality | https://martinfowler.com/articles/continuousIntegration.html |
| S-12 | IEEE Std 2675-2021, DevOps: Building Reliable and Secure Systems Including Application Build, Package, and Deployment | IEEE Standards Association | 2021-04-16 | standard | paid; copyright IEEE | part | operations, security | https://standards.ieee.org/ieee/2675/6830/ |
| S-13 | Concise Guide for Developing More Secure Software | OpenSSF Best Practices Working Group | 2023-06-14 | foundation | not found | part | security, supply chain | https://best.openssf.org/Concise-Guide-for-Developing-More-Secure-Software |
| S-14 | OWASP Software Assurance Maturity Model (SAMM) | OWASP Foundation | 2.0; read 2026-10-11 | foundation | CC BY-SA 4.0 | part | security | https://owaspsamm.org/model/ |

## 3. Strategy

High level, for the agent that runs the work. One page.

### 3.1 Goals

- Each concern of operation, security and quality has a check at the earliest point where a program can
  make it: before the commit, before the merge, in the build, before the release.
- Each release can be traced to its source revision, its build and its components, and a consumer can
  verify that.
- The project knows its vulnerabilities and its incidents, answers them, and adds a check after each one.
- A change reaches the users through one automated path that can be repeated and reverted.
- The effort follows the risk of the project: level 1 for each project, more only where a risk dimension
  calls for it.

### 3.2 Order of the work

1. Find out the contexts and the risk of the project on each risk dimension. This decides how far the
   project goes above level 1.
2. Put all inputs of the build into version control and protect the main branch and the access. Each later
   step relies on a source that is known.
3. Make the build and the tests run on each change, with a definition of the checks in the repository. The
   other checks need this pipeline.
4. Add the security checks to the pipeline: secrets, dependencies, static analysis. They are cheap when the
   pipeline exists.
5. Publish how to report a vulnerability, and decide how the project answers one.
6. Make the release build run on a hosted platform, then add provenance, then its signature. This is the
   order of the levels of the build track.
7. For a service that the project operates: automate the deployment and the rollback, then add signals and
   alerts, then service levels and rehearsals.
8. After each vulnerability and each incident, add a check at an earlier stage.

### 3.3 Decisions that depend on context

| Decision | Depends on | Options | Sources |
|---|---|---|---|
| Which review a change gets before the merge | team; openness | approval of a second person before the merge; work in pairs; review after the merge; automated checks only, for one maintainer | S-10 chapter 9; S-11 Common Questions; S-02 source-requirements; S-07 Code-Review |
| Which security scans the pipeline runs | delivery; the technology of the project | dynamic tests of the running software; scans of container images and of infrastructure definitions; fuzzing; interactive tests | S-06 2 Vulnerability Scanning; S-05 page 30; S-07 Fuzzing |
| How to release to users | delivery; availability | each passing build goes to production; releases at fixed intervals; a release to a small part first; unfinished work behind flags; versions and a deprecation process for installed software | S-09 chapter 8; S-10 chapter 24; S-11 Hide Work-in-Progress; S-13 item 12 |
| Which service levels to set | availability; the type of the service | no objective for software that the project does not operate; a small number of indicators with loose targets first; an error budget | S-09 chapter 4; S-01 page 158 |
| How fast to take dependency updates | supply chain integrity; exposure | take a correction of a known vulnerability at once; delay other updates for some days; update by a program with review | S-13 item 8; S-07 Dependency-Update-Tool |
| Which SLSA tracks and levels to aim for | platform of source and build; supply chain integrity | the build track of the approved version; the source track of the approved version; the tracks of the draft, which only a platform with attested build environments can reach | S-02 build-track-basics; S-02 source-requirements; S-03 build-env-track-basics; S-03 dependency-track |
| How to branch | team; delivery | integration into one main line each day; short branches with a merge request; release branches with selected corrections from the main line | S-11 Common Questions; S-09 chapter 8, Branching; S-10 chapter 24; S-01 page 188 |
| Which tests the project keeps | criticality; the architecture of the software | mostly small tests with some integration and end-to-end tests; manual exploratory tests; tests against production | S-10 chapter 11; S-08 test-automation; S-01 page 258 |
| How to organize the security work | team; regulation | the developers carry the security work; a security person in each team; a security team that gives approved tools and reviews | S-01 page 266; S-08 pervasive-security; S-14 education-and-guidance; S-04 pages 15 and 16 |
| How to prepare the operation | availability; team | no preparation for software that others operate; a plan for capacity, support and training; rehearsals of emergencies | S-01 pages 156 to 159; S-09 chapter 13 |
| Which data protection measures apply | regulation; exposure | no personal data; measures scaled to how critical the data is; privacy by design for much personal data | S-06 2-g Privacy; S-01 page 281 |
| How to measure the progress | openness; the application | the levels of a public scale; the delivery metrics of one application as a signal, not as a goal; a maturity assessment | S-08 dora-metrics; S-13 items 14 and 15; S-14 getting-started step 2 |

### 3.4 Where the sources disagree

| Question | Positions | How this recipe handles it | Sources |
|---|---|---|---|
| What does DevSecOps cover? | The sources that carry the name mean security in DevOps work and in its pipeline (S-06; S-05; S-01 pages 159 and 266). The owner means the shift left of operational, security and quality concerns. One page of the body of knowledge names tests and security as shifted left (S-01 page 206). | The recipe follows the owner. It takes the operational view and the quality view from the sources of those fields. | S-06 0-a Overview; S-05 page 11; S-01 pages 159, 206 and 266 |
| Does a review by a second person come before the merge? | Yes, for essentially each change (S-10; S-05; S-02 for Source L4). A review before the integration adds friction, and work in pairs or a review after the merge are alternatives (S-11). | The review before the merge is an item above level 1 that the dimension team size calls for. The decision of section 3.3 gives the alternatives. | S-10 chapter 9; S-05 page 21; S-02 source-requirements; S-11 Common Questions |
| How fast does a project take an update of a dependency? | Use a program that updates dependencies (S-07). Delay updates of components without known vulnerabilities for some days (S-13). | A decision of section 3.3. The checklist asks only that a program reports vulnerabilities and updates. | S-07 Dependency-Update-Tool; S-13 item 8 |
| Does a project publish a bill of materials? | Publish and consume one (S-13; S-07). No recommendation, because the specifications change, and the list alone is not sufficient for the management of vulnerabilities (S-05). | The item asks only that a program generates the list in the build. It is above level 1. | S-13 item 18; S-07 SBOM; S-05 pages 13 and 32 |
| Can a measured value be the target of a project? | The owner asks for a measurable target and names SLSA levels. Do not set the delivery metrics as goals (S-08). A SLSA level does not show secure coding or the quality of the code (S-02). A low Scorecard score is not a definitive sign of risk (S-07). | The recipe gives the scales as targets of single views. It does not give one number for the aspect. The SLSA levels measure the supply chain view only. | S-08 dora-metrics; S-02 about; S-07 CI-Tests |

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
| C-01 | All source code, build scripts and configuration are in one version control system, and no generated executable file is in it. | A change that is not recorded cannot be reviewed, reproduced or reverted. | supply chain | 1 | authority (5) | no build input is outside the repository; a search finds no executable file | S-02 source-requirements; S-04 page 18; S-07 Binary-Artifacts; S-09 chapter 8; S-01 page 197; S-11 Put everything in a version controlled mainline |
| C-02 | The main branch and the release tags are protected: no forced change of history, no deletion, no moved tag. | A person or a program can replace reviewed code without a trace. | supply chain | 1 | authority (2) | the settings of the repository forbid a forced push and the deletion of the branch and of tags | S-02 source-requirements; S-07 Branch-Protection |
| C-03 | A second person approves each change to a protected branch before the merge. | One person, or one stolen account, can add a fault or malicious code. | supply chain | 2, team size | authority (4) | the settings of the repository require one approval that is not of the author | S-02 source-requirements; S-05 pages 21 and 26; S-10 chapter 9; S-07 Code-Review |
| C-04 | Each dependency has an exact version and an integrity hash in a lock file that is in version control. | A dependency can change or be replaced between two builds. | supply chain | 1 | authority (2) | a lock file with hashes is in the repository, and the build fails without it | S-07 Pinned-Dependencies; S-03 dependency-track; S-11 Put everything in a version controlled mainline |
| C-05 | A program reports known vulnerabilities and available updates of the dependencies on each change and on a schedule. | Known faults of dependencies stay in the product and are exploited. | supply chain | 1 | authority (4) | the pipeline has a dependency scan that runs on changes and on a schedule | S-01 page 103; S-05 page 29; S-06 2-d Software Composition Analysis; S-07 Vulnerabilities |
| C-06 | A dependency is added only after an evaluation of its need, its origin, its licence and its maintenance. | An unnecessary or untrusted dependency brings vulnerabilities and legal risk. | supply chain | 1 | authority (4) | judgement | S-01 pages 103 and 212; S-04 pages 21 and 22; S-05 page 21; S-13 item 4 |
| C-07 | The release build runs from a script on a hosted build platform, not on the computer of a developer. | A build on a personal computer cannot be repeated or trusted. | supply chain | 1 | authority (4) | the release artefacts come from a pipeline run, and the build script is in the repository | S-02 build-track-basics; S-05 page 17; S-09 chapter 8; S-01 page 197; S-11 Automate the Build |
| C-08 | The build platform generates provenance for each release artefact: the builder, the source revision and the inputs. | Nobody can show from which source and by which process an artefact came. | supply chain | 2, supply chain integrity | authority (3) | each release has a provenance file that names the builder and the source revision | S-02 build-track-basics; S-04 page 19; S-05 pages 25 and 26 |
| C-09 | The build platform signs the provenance, and the release tells consumers how to verify it. | An artefact can be changed after the build, and the consumer cannot detect it. | supply chain | 2, supply chain integrity | authority (5) | the verification command of the release notes passes for the latest release | S-02 build-track-basics; S-02 verifying-artifacts; S-04 page 19; S-05 page 26; S-07 Signed-Releases; S-13 item 13 |
| C-10 | The release build runs on a platform that isolates each build and keeps the signing key away from the build steps. | A build step, or a different build, can change the artefact or forge the provenance. | supply chain | not admitted | authority (3) | the documentation of the build platform states isolation and protection of the key for the builder in use | S-02 build-track-basics; S-03 build-requirements; S-05 page 25 |
| C-11 | Each job of the pipeline has the least permissions, and code of an untrusted change does not run with secrets. | A change from outside can take the secrets or change the repository through the pipeline. | supply chain | 1 | authority (2) | the pipeline definition sets read permissions by default, and no job for outside changes gets secrets | S-07 Token-Permissions; S-07 Dangerous-Workflow; S-05 page 27 |
| C-12 | A program generates a list of the components of each release during the build. | After a new vulnerability, nobody knows which releases hold the component. | supply chain | 2, supply chain integrity | authority (4) | each release has a component list in a standard format | S-01 pages 192 and 197; S-05 pages 13 and 21; S-07 SBOM; S-13 item 18 |
| C-13 | Each person with write access to the repository or to the release uses multi-factor authentication. | One stolen password gives control of the source and of the releases. | supply chain | 1 | authority (3) | the settings of the organization or the repository require a second factor | S-13 item 1; S-04 page 18; S-05 page 21 |
| C-14 | A deployment admits only an artefact with verified provenance from the release build. | An artefact from a different source or a different build reaches production. | supply chain | not admitted | authority (2) | the deployment has a verification step that fails for an artefact without provenance | S-05 page 29; S-02 verifying-artifacts |
| C-15 | A program stops secrets before the commit, and scans the repository and the pipeline for secrets. | A secret in the history of a repository is public for each reader. | security | 1 | authority (3) | a secret scan is in the hooks or the pipeline, and a scan of the history finds nothing | S-06 1-a Secrets Management; S-05 page 29; S-13 item 9 |
| C-16 | Static analysis for security weaknesses runs on each change in the pipeline. | Common weaknesses reach the main branch and are found late or not at all. | security | 1 | authority (6) | the pipeline has a static analysis step on merge requests | S-01 pages 107 and 266; S-04 page 23; S-05 page 28; S-06 2-a Static Application Security Testing; S-07 SAST; S-13 item 3 |
| C-17 | The project publishes how to report a vulnerability in private and who answers. | A finder publishes the vulnerability, or does not report it. | security | 1 | authority (4) | a security policy file is in the root of the repository | S-07 Security-Policy; S-04 pages 25 and 26; S-01 page 268; S-13 item 11 |
| C-18 | Each confirmed vulnerability gets an analysis, a recorded risk decision and, for released software, an advisory to the consumers. | Known vulnerabilities stay open, and consumers do not know that they must update. | security | 1 | authority (4) | each closed vulnerability report has a decision, and each corrected release has an advisory | S-04 pages 26 and 27; S-07 Vulnerabilities; S-13 item 16; S-14 defect-management |
| C-19 | The security requirements of the software are written down, and automated tests examine them. | Security that is not specified is not built and not tested. | security | 1 | authority (4) | a document of security requirements is in the repository, and tests refer to it | S-01 page 264; S-04 page 14; S-08 pervasive-security; S-14 requirements-driven-testing |
| C-20 | Dynamic security tests run against the running software before a release. | A weakness that shows only at run time reaches the users. | security | 2, exposure | authority (4) | the pipeline has a dynamic test stage before the release | S-04 page 24; S-05 page 28; S-06 2-b Dynamic Application Security Testing; S-01 page 268 |
| C-21 | After each vulnerability, the team finds the root cause and adds a check for that class of fault. | The same class of vulnerability comes back. | security | 2, exposure | authority (1) | judgement | S-04 page 27 |
| C-22 | Each change starts an automated build and automated tests, and a failed check stops the merge. | A fault is found late, when its correction costs more. | quality | 1 | authority (5) | the pipeline runs on each merge request, and the branch rule requires that it passes | S-01 pages 107, 155 and 197; S-08 continuous-integration; S-10 chapter 23; S-07 CI-Tests; S-03 source-example-controls; S-11 Make the Build Self-Testing |
| C-23 | Each change holds tests for the behaviour that it adds or changes. | New behaviour is not protected, and a later change breaks it. | quality | 1 | authority (4) | judgement | S-10 chapter 11; S-08 test-automation; S-01 pages 171 and 257; S-13 item 6 |
| C-24 | A broken build of the main branch is repaired or reverted before other work continues. | Each person builds on a broken state, and new faults hide behind the first. | quality | 1 | authority (2) | judgement | S-08 continuous-integration; S-10 chapter 23; S-11 Fix Broken Builds Immediately |
| C-25 | The fast checks run before the merge; the slow checks run after it and before the release. | Slow feedback makes developers go around the checks. | quality | 2, team size | authority (2) | the pipeline has a short stage on merge requests and longer stages after the merge | S-10 chapter 23; S-01 page 164; S-11 Keep the Build Fast |
| C-26 | A defect that a later stage or a person finds gets an automated test in an earlier stage. | The same defect comes back and is found late again. | quality | 1 | authority (2) | judgement | S-08 test-automation; S-10 chapter 11; S-11 Keep the Build Fast |
| C-27 | An unreliable test is repaired or removed, and the removal is tracked. | The team stops to trust the tests and ignores true failures. | quality | 2, team size | authority (2) | each disabled test has a link to an open issue | S-08 test-automation; S-10 chapter 23 |
| C-28 | A program corrects style and format faults before the review. | Reviews use their time on what a program can find. | quality | 1 | authority (1) | the hooks or the pipeline run a formatter and a linter | S-10 chapters 9 and 20 |
| C-29 | The checks that a change must pass are defined in a file of the repository, and the pipeline enforces them. | The criteria are different for each person and each day. | quality | 1 | authority (4) | the pipeline definition and the branch rules are in the repository or are exported to it | S-04 pages 16 and 17; S-01 pages 211 and 256; S-10 chapter 20; S-02 source-requirements |
| C-30 | The deployment to each environment runs from a script in version control, and no change is applied by hand to the running system. | A manual step is forgotten or is different each time, and the running state is not known. | operations | 2, availability | authority (3) | the deployment is a pipeline job, and a comparison of the repository with the running state shows no difference | S-05 pages 30 and 31; S-01 pages 158 and 179; S-14 secure-deployment; S-11 Automate Deployment |
| C-31 | The return to the last good release is automated and is tested. | A bad release stays in production while the team looks for a way back. | operations | 2, availability | authority (3) | a rollback job exists and ran in a test in the last period | S-09 chapter 13; S-10 chapter 24; S-01 page 160 |
| C-32 | A release goes first to a small part of the systems or the users. | A fault reaches all users at the same time. | operations | not admitted | authority (2) | the deployment has a stage for a part of the systems before the full stage | S-09 chapter 13; S-01 page 160 |
| C-33 | The running software reports its version and gives signals of health and errors. | Nobody knows what runs or that it fails. | operations | 2, availability | authority (3) | a request to the running software gives the version, and a dashboard shows health and errors | S-09 chapters 6 and 8; S-08 monitoring-and-observability; S-01 pages 161 and 333; S-11 Automate Deployment |
| C-34 | An alert reaches a person only for a symptom that users see and that needs an action. | Persons who get too many alerts ignore the important one. | operations | 2, availability | authority (2) | judgement | S-09 chapter 6; S-08 monitoring-and-observability |
| C-35 | The service has written service level objectives, each with its method of measurement. | Without an agreed level, each fault is urgent or none is. | operations | not admitted | authority (1) | a document of the objectives is in the repository | S-09 chapter 4 |
| C-36 | An incident has a known response procedure, and a review without blame records the causes and the actions. | The response is slow, and the same incident occurs again. | operations | 1 | authority (3) | a response procedure is in the repository, and each incident has a review document | S-09 chapters 13 and 15; S-01 page 159; S-04 page 26 |
| C-37 | The plan of a change states how the change is deployed, observed and reverted. | Operational faults are found in production, where a correction costs most. | operations | 1 | authority (2) | judgement | S-01 pages 156, 159 and 178; S-09 chapter 8 |
| C-38 | The test environments are made from the same definitions as the production environment. | A test passes in an environment that is different from production. | operations | 2, availability | authority (2) | the environments are made from the same files with different parameters | S-01 pages 157 and 158; S-10 chapter 23; S-11 Test in a Clone of the Production Environment |
| C-39 | The recovery from a backup and the change to a second system are rehearsed. | The recovery fails at the moment when it is necessary. | operations | 2, availability | authority (1) | a record of the last rehearsal is not older than the agreed interval | S-01 pages 159 and 331 |

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

- **Goal**: The project has a committed selection of the checklist items, made from a risk analysis with
  the owner of the project, and a plan that lists each adopted item whose check fails.
- **Reads first**: The repository, the pipeline definition and the release process of the project; the
  contexts team, delivery, platform of source and build, openness, regulation and criticality; the answers
  of the owner of the project to the question of each risk dimension; an existing selection.
- **Applies**: The order of the work; the checklist items of level 1 for each project; the items above
  level 1 that the chosen risk dimensions call for; the check of each item, or a judgement with its reason.
- **Delegates**: The settings of the hosting platform of the repository; the pipeline definition; the
  generation and the verification of provenance; the scans for secrets, dependencies and weaknesses; the
  deployment and the monitoring. An implementation skill gives each one.
- **Stops when**: The plan is written and the owner of the project did not accept it; a decision that
  depends on context needs a person; a source cannot be reached; the target level is not possible on the
  platform of the project.

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
| The hosting platform of the repository | Branch and tag protection, required reviews, required checks, multi-factor authentication | C-02, C-03, C-13, C-29 | none |
| The pipeline platform | Builds and tests on each change, permissions of jobs, hosted release builds | C-07, C-11, C-22, C-25 | none |
| A provenance generator and verifier for the build platform (the specification names slsa-verifier and slsa-github-generator) | Signed provenance of release artefacts and its verification | C-08, C-09, C-10, C-14 | the verifier program |
| OpenSSF Scorecard | A measurement of the repository against its checks | C-02, C-04, C-11, C-17 | the Scorecard program |
| A dependency scanner and update tool | Reports of vulnerabilities and updates, lock files, a component list | C-04, C-05, C-12 | the scanner program |
| A secret scanner | Hooks before the commit and scans of the history | C-15 | the scanner program |
| A static analysis tool and a linter for the languages of the project | Weaknesses and style faults on each change | C-16, C-28 | the analysis program |
| The deployment and monitoring tools of the service | Scripted deployment, rollback, signals and alerts | C-30, C-31, C-33, C-34 | none |

## 6. Watch list

| Signal | Where to read it | Cadence |
|---|---|---|
| A new approved version of the SLSA specification, or a track that moves from the draft to an approved version | https://slsa.dev/spec/ (S-02, S-03) | at each refresh |
| A new version of NIST SP 800-218 or of NIST SP 800-204D | https://csrc.nist.gov/publications/sp800 (S-04, S-05) | at each refresh |
| A change of the Scorecard checks | https://github.com/ossf/scorecard/blob/main/docs/checks.md (S-07) | at each refresh |
| A new version of the OWASP DevSecOps Guideline or of SAMM | the pages of the projects (S-06, S-14) | at each refresh |
| A change of the delivery metrics or a new yearly report of DORA | https://dora.dev/ (S-08) | each year |
| A new version of the SWEBOK Guide, or of the DevOps standard that it cites | the page of the issuer (S-01, S-12) | at each refresh |

## 7. Decisions and changes

Dated. A reversed decision stays and is marked superseded. Name the models that made or
suggested a judgement, and the person who reviewed the findings and accepted the recipe.

| Date | Decision or change | Reason | Revisit when |
|---|---|---|---|
| 2026-10-11 | Not verified: the intent of the owner was not asked in the session of phase 1. The lines `meaning` and `result` hold words of the owner of 2026-10-10 that the session got as text. The question `not wanted` has no answer. The owner did not confirm the fields "Aspect", "Field and disciplines" and "Agreed with the owner on" as they are written. | The owner was not in the session. | The owner reads section 1, at the latest in the review of phase 3. |
| 2026-10-11 | The views are `operations`, `security`, `quality` and `supply chain`. | The owner named the operational, the security and the quality concerns. The fourth view comes from the sources: the target that the owner named (SLSA) measures the integrity of the supply chain, and the body of knowledge has it in the area of configuration management (S-01 pages 185 to 198). | The owner reviews the views. |
| 2026-10-11 | The target of the owner, "achieve SLSA draft highest levels", is recorded as the target `highest levels of the SLSA draft`. Not verified: which document the owner means by "draft". The session took the working draft at https://slsa.dev/spec/draft/. | The working draft has four tracks. The approved version 1.2 has two. The draft can change or be discarded (S-03 index). | The owner reviews the targets. |
| 2026-10-11 | Decision of the owner that is necessary: the calculation of risk and reward does not admit the items C-10, C-14, C-32 and C-35 with the answers of this session. The highest build level, which the target of the owner needs, rests on C-10 and C-14. | A program computes the admission from the answers. The session did not change an answer to get a result. The answers are by judgement of a model, for a typical project. | The owner corrects the answers in the review, or accepts the result. |
| 2026-10-11 | Decision of the owner that is necessary: four boundaries are proposed (`secure design`, `security management of the organization`, `platform operation`, `privacy`). No requirement goes to them. | Only the owner decides a boundary. | The owner decides or declines each boundary. |
| 2026-10-11 | Judgement: the classes of the sources. S-01 has the class `standard` (the issuer is a standards body), S-08 has the class `research` (a research program), S-09 and S-10 have the class `research` (recognized books). S-11 is the only `independent` source. | The class decides the route of admission. | The owner reviews the sources. |
| 2026-10-11 | Judgement: the group `operations engineers` holds the persons who do site reliability engineering and platform engineering, which the body of knowledge names as concepts of some organizations (S-01 page 152). The group `consumers` holds users, customers and acquirers. | One line for each group with the same concerns for this aspect. | The owner reviews the stakeholders. |
| 2026-10-11 | Requirements that the readers reported and that the table Requirements does not hold: the requirements of the body of knowledge that are not about a concern of this aspect (for example about the form of requirements documents, mathematics, economics, design notations and the duties of the editors of the guide), the notional examples of S-04, the requirements of S-02 and S-03 for verifiers, consumers and the formats of attestations, the steps of the privacy page of S-06, and the detail requirements of S-08, S-09 and S-10 that say the same as a row of the table in more words. | The table holds the requirements for the concerns of the aspect. This is a selection by a model, and the procedure says to record each requirement. | The owner asks for the complete list, or accepts the selection. |
| 2026-10-11 | The web readers got summaries of the pages from their tool, not the text of the pages. Each web source has `part` in the cell Read. Not verified: the words `must` and `should` of the web sources, the date of S-08 and of S-13, and the licence of S-07, S-11 and S-13. | The tool of the readers gives a summary. The readers said so in each report. | A reader with the text of the pages reads the sources again. |
| 2026-10-11 | Not verified: the page `levels` of S-02 (the address gave `not found`); the pages of S-02 and S-03 on threats, attestation formats and verified properties; chapter 14 of S-09; the text of S-12 (paid; only the public page was read); if the approved version of SLSA has the tracks Build Environment and Dependency on a page that was not read. | The readers did not read these parts. | The next refresh. |
| 2026-10-11 | Not verified: the references that the body of knowledge names for the views and that are paid or were not retrieved: ISO/IEC/IEEE 32675, ISO/IEC 20000-1, ISO/IEC/IEEE 12207, ISO/IEC 27001, ISO/IEC 25010, ISO/IEC/IEEE 29119, IEEE 828, IEEE 730, IEEE 1012, ISO/IEC 15408-1, the DoD Enterprise DevSecOps Fundamentals, and the books that it cites for DevOps and continuous delivery. | Paid standards. The run did not retrieve the other documents. | The owner gives a file, or a refresh retrieves a public one. |
| 2026-10-11 | The version cell of S-01 holds the version and the date of the manifest of the seeds. The reader of the first pages reported a different release date from page 1, and a copyright range to 2025 from page 5. | The two values of the reader do not agree with each other. The session did not read the page. | The owner examines the manifest row of the seed. |
| 2026-10-11 | Readers read lines outside their range: the reader of S-01 pages 99 to 116 read also lines of pages 117 to 121, and the reader of S-04 pages 1 to 25 read also the 8 lines above page 1. They did not use that text. The recorded ranges were not changed. | Each of those pages was in the range of a different reader, or is the head of the file. | No action. |
| 2026-10-11 | Roles of the models: the smallest model of the agent product read the sources (one reader for each range or each source). The mid-size model and new readers of the smallest model made the second reading. The largest model, as the session, selected the sources, named the stakeholders and the views, wrote the requirements in the words of the kit, distilled the items and gave the answers of risk and reward. | The procedure asks for the roles. | No action. |
| 2026-10-11 | The second reading corrected 11 rows of the evidence record. The evidence record has 14 rows. Of 161 sentences in these rows, the second reading corrected 47 (41 overstated, 6 with a wrong location) and could not check 2. The rows of S-11, S-12 and S-13 had no finding. Each correction is also in the rows of spec.md and of the table Requirements that said the same. | The procedure asks for the second reading. The task of the session asks for the two numbers. | No action. |
| 2026-10-11 | Not verified by the second reading: the end of the list of parties that agree an integrity level (S-01 page 251, the list continues on the next page); that the pages of S-06 which the second reader did not read give no scale; the highest maturity level of S-14 (the first reader reported the levels 1 to 3, the second reader did not see level 3). The evidence record does not hold statements of absence that a second reader could not find in the text of a source. | The second readers reported these points as not checked or not found. | The next refresh. |
| 2026-10-11 | The vetting program measured the date 2026-10-10 on the page of S-11. The reader reported 2024-01-18 as the date of the last revision of the article. The score of S-11 in vetting.md uses the measured date. | The program takes the date from the page data. The two values do not agree, and the age changes the score. | The owner examines the date before the confirmation of S-11. |
| 2026-10-11 | The session of phase 2 did not ask the owner a question. The owner did not confirm a source, did not decide a boundary and did not accept the recipe. | The owner was not in the session. | The review of the owner in phase 3. |

## 8. Glossary

Terms that mean different things in the sources. One preferred form per meaning.

| Term | Meaning here | Other meanings in the sources |
|---|---|---|
| DevSecOps | The shift left of the operational, the security and the quality concerns of a project, as the owner states it. | The integration of security into DevOps and its pipeline (S-06 0-a Overview; S-01 page 266); written Dev/Sec/Ops in S-01 page 206. |
| shift left | To do a check at an earlier point of the life cycle. | Early testing (S-01 page 139); early involvement of stakeholders, written left shift (S-01 page 400; S-12); earlier decisions from data (S-10 chapter 24). |
| provenance | The record of the build platform that tells which builder made an artefact from which source and inputs. | Data on the origin, the development, the ownership and the changes of a component (S-05 page 22; S-04 page 19); the record of a source control system for a revision (S-02 source-requirements). |
| bill of materials | The list of the components of one release that a program generates. | A record of the supply chain relationships of configuration items (S-01 page 192); written SBOM in S-05, S-07 and S-13. |
| consumer | A person or a system that takes the software: a user, a customer or an acquirer. | Software acquirer (S-04 page 19); end user (S-05 page 13); software consumer (S-02 about). |
| continuous delivery | Frequent automated releases to an environment, with a decision of a person before production. | Continuous deployment is the automated deployment of each change to production (S-01 page 163). |

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
