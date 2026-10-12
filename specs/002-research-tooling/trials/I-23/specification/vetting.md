# Vetting record: DevSecOps

## Sources

One row for each independent source. A program fills the cells Kind, Gates, Signals, Score and Date. Only the owner fills the cell "Confirmed by".

| Source | Kind | Answers | Gates | Signals | Score | Date | Confirmed by |
|---|---|---|---|---|---|---|---|
| S-25 | page | record: yes (https://dora.dev/research/); fast-lane references: 0 | pass | reachable yes; date 2026-10-11; age 1 d; author yes; links out 9 | 8 of 10 | 2026-10-12 | |
| S-28 | page | record: yes (https://www.sonatype.com/state-of-the-software-supply-chain/past-reports); fast-lane references: 0 | pass | reachable yes; date 2026-10-08; age 4 d; author yes; links out 11 | 8 of 10 | 2026-10-12 | |
| S-30 | page | record: yes (https://sethmlarson.dev); fast-lane references: 0 | pass | reachable yes; date 2026-01-01; age 284 d; author yes; links out 15 | 8 of 10 | 2026-10-12 | |
| S-32 | page | record: yes (https://www.sovereign.tech/tech/reproducible-builds); fast-lane references: 1 (S-02) | pass | reachable yes; date 2026-10-09; age 3 d; author yes; links out 8 | 9 of 10 | 2026-10-12 | |

## Searches

Each query of the research, with the view that it serves. A query with the word `catalogues:` is
a query of `catalog.py find`. The first queries of each view name no document, no project, no
organization and no product. A later query with a name was made only to find the page of the
issuer of a thing that a first query found.

- security: `shift left security operations quality software delivery pipeline standard guidance`
- operations: `shift left security operations quality software delivery pipeline standard guidance`
- quality: `shift left security operations quality software delivery pipeline standard guidance`
- security: `software supply chain build integrity levels provenance specification current version`
- security: `secure software development practices framework public authority recommendation build pipeline`
- security: `regulation cybersecurity requirements products with digital elements manufacturers vulnerability handling secure development`
- operations: `software delivery performance metrics multi-year survey report deployment frequency change failure rate`
- security: `continuous integration pipeline security risks top ten credentials poisoned pipeline execution`
- operations: `operations readiness observability incident response release rollback practices production software recommendation`
- quality: `software quality gates automated tests static analysis code review continuous integration standard model`
- operations: `reusable pipeline components shared workflow catalog continuous integration official documentation`
- security: `automated checks measure security posture open source repository score branch protection pinned dependencies`
- security: `public vulnerability database open source packages API who operates funding`
- security: `audit framework control requirements secure software development lifecycle change management industry rule payment software`
- security: `government agency guidance defending build and deployment environments recommendations hardening`
- security: `security baseline controls open source project maturity levels foundation`
- security: `NIST SP 800-218 Secure Software Development Framework csrc.nist.gov final publication`
- security: `NIST SP 800-204D strategies integration software supply chain security DevSecOps CI/CD pipelines`
- security: `OWASP Top 10 CI/CD Security Risks project page; OWASP SAMM model; OWASP DevSecOps Guideline`
- security: `Regulation (EU) 2024/2847 Cyber Resilience Act official text`
- operations: `DORA software delivery performance metrics guide and latest report`
- operations: `site reliability engineering book release engineering monitoring service level objectives postmortem`
- operations: `DevOps standard building reliable and secure systems including application build package and deployment IEEE ISO/IEC`
- quality: `product quality model characteristics systems and software quality requirements and evaluation international standard`
- security: `OSV open source vulnerabilities database about who operates`
- security: `widely used open source project release process signed artifacts provenance attestations security documentation how we release`
- security: `annual report open source software supply chain statistics malicious packages vulnerable downloads multi-year`
- security: `information security management standard controls secure development life cycle separation of development test production environments change management`
- security: `software supply chain security best practices paper foundation securing source code materials build pipelines artefacts deployments`
- security: `executive order improving cybersecurity software supply chain attestation secure development requirements federal`
- quality: `software testing standard test processes international standard ISO/IEC/IEEE 29119 overview`
- security: `security hardening for workflows secrets least privilege token third-party actions pin official docs; CI/CD components catalog official docs`
- security: `PCI DSS v4.0.1 document library requirement 6 develop and maintain secure systems and software`
- operations: `well-architected operational excellence pillar design principles operations as code observability safe deployments`
- quality: `Software Engineering at Google book online chapters testing overview code review continuous integration continuous delivery`
- security: `Kubernetes release artifacts signed SLSA provenance verify documentation; CPython release sigstore verification`
- security: `OpenSSF Best Practices badge criteria passing silver gold; OpenSSF Scorecard checks documentation`
- operations: `GitLab CI/CD components catalog documentation; GitHub reuse workflows documentation`
- security: `ISO/IEC 27001:2022 information security management systems requirements iso.org standard page`
- quality: `testing in continuous delivery test automation capability research code quality predictors survey`
- security, catalogues: `supply chain security`
- security, catalogues: `provenance attestation`
- operations, catalogues: `continuous integration`
- operations, catalogues: `pipeline components`
- operations, catalogues: `observability`
- security, catalogues: `vulnerability database`
- quality, catalogues: `static analysis`
- quality, catalogues: `testing quality`
- security, catalogues: `release signing`
- operations, catalogues: `incident response`
- security, catalogues: `policy enforcement`
- security, catalogues: `reproducible builds`
- security, catalogues: `security scorecard`

## Requirements

One row for each requirement line of the reports of the readers. The words of the cell "Requirement" are the words of the reader about the source.

| Id | Requirement | Stakeholder | View | Source | Goes to |
|---|---|---|---|---|---|
| R-0001 | Software engineers should be knowledgeable about the related disciplines that the Guide lists | software engineers | quality | S-01 page 40 | C-49 |
| R-0002 | Competent and capable software engineers should be equipped with the generally accepted knowledge for potential application | software engineers | quality | S-01 page 41 | C-49 |
| R-0003 | A software project must implement the requirements imposed by cross-cutting disciplines such as dependability and safety | software engineers | quality | S-01 page 39 | C-46 |
| R-0004 | Appropriate selection of generally accepted knowledge should be included in the study material for professional certification and licensing examinations | regulators and auditors | quality | S-01 page 41 | C-49 |
| R-0005 | Each requirement should be unambiguous, so that it can be read in only one way | software engineers | quality | S-01 page 50 | C-46 |
| R-0006 | Each requirement should be testable, quantified, so that compliance or noncompliance can be clearly demonstrated | software engineers | quality | S-01 page 50 | C-46 |
| R-0007 | Each requirement should be binding, so that clients are willing to pay for it | software engineers | quality | S-01 page 50 | C-46 |
| R-0008 | Each requirement should be atomic and represent a single decision | software engineers | quality | S-01 page 50 | C-46 |
| R-0009 | Each requirement should represent true, actual stakeholder needs | software engineers | quality | S-01 page 50 | C-46 |
| R-0010 | Each requirement should use stakeholder vocabulary | software engineers | quality | S-01 page 50 | C-46 |
| R-0011 | Each requirement should be acceptable to all stakeholders | software engineers | quality | S-01 page 50 | C-46 |
| R-0012 | The overall collection of requirements should be complete, addressing boundary, exception and security needs | software engineers | quality | S-01 page 50 | C-46 |
| R-0013 | The overall collection of requirements should be concise, with no extraneous content | software engineers | quality | S-01 page 50 | C-46 |
| R-0014 | The overall collection of requirements should be internally consistent, with no conflicts | software engineers | quality | S-01 page 50 | C-46 |
| R-0015 | The overall collection of requirements should be externally consistent, with no conflict with source material | software engineers | quality | S-01 page 50 | C-46 |
| R-0016 | The overall collection of requirements should be feasible within cost, schedule, staffing and other constraints | software engineers | quality | S-01 page 50 | C-46 |
| R-0017 | The software engineer should pay attention to positive and negative relationships between quality of service constraints | software engineers | quality | S-01 page 51 | C-41 |
| R-0018 | When a nonfunctional requirement is modified, the impact it may have on other requirements should be considered | software engineers | quality | S-01 page 46 | C-46 |
| R-0019 | Security requirements should be considered, using the Security KA for the kinds of security requirements that should be considered | security engineers | security | S-01 page 47 | C-13 |
| R-0020 | Documented software requirements should be subject to the same configuration management practices as other life cycle deliverables | operations engineers | operations | S-01 page 53 | C-35 |
| R-0021 | When practical, individual requirements are subject to configuration management and traceability, generally supported by a requirements management tool | software engineers | quality | S-01 page 53 | C-46 |
| R-0022 | Software engineers, business domain experts and possibly QA or test professionals meet before production work to agree on test cases that must pass | quality assurance staff | quality | S-01 pages 54 to 55 | C-46 |
| R-0023 | At least one acceptance test case must fail on the existing software before production code is created or modified | software engineers | quality | S-01 page 55 | C-46 |
| R-0024 | In waterfall and other plan-based life cycles, requirements scrubbing should occur just before the validation review | software engineers | quality | S-01 page 58 | C-46 |
| R-0025 | Review from multiple perspectives is preferred, with clients, customers and users checking that their wants and needs are represented | consumers | quality | S-01 page 58 | C-46 |
| R-0026 | Review from multiple perspectives is preferred, with other software engineers checking clarity and conformance to applicable standards | software engineers | quality | S-01 page 58 | C-46 |
| R-0027 | Review from multiple perspectives is preferred, with software engineers who will do architecture, design or construction checking sufficiency | software engineers | quality | S-01 page 58 | C-46 |
| R-0028 | Projects using waterfall or other plan-based life cycles should have an explicit requirements change control process | operations engineers | operations | S-01 page 59 | C-35 |
| R-0029 | The change control process should include a means to request changes | operations engineers | operations | S-01 page 59 | C-35 |
| R-0030 | The change control process should include an optional impact analysis stage | operations engineers | operations | S-01 page 59 | C-35 |
| R-0031 | The change control process should include a responsible person or group that accepts, rejects or defers each change | operations engineers | operations | S-01 page 59 | C-35 |
| R-0032 | The change control process should include a means to notify all affected stakeholders of the decision | operations engineers | operations | S-01 page 59 | C-35 |
| R-0033 | The change control process should include a means to track accepted changes to closure | operations engineers | operations | S-01 page 59 | C-35 |
| R-0034 | All stakeholders must understand and agree that accepting a change means accepting its impact on schedule, resources and scope elsewhere | managers | quality | S-01 page 59 | C-48 |
| R-0035 | Ideally the change in scope should be objectively quantifiable, in functional size units | managers | quality | S-01 page 59 | C-48 |
| R-0036 | In waterfall and other plan-based life cycles, scope matching should occur just before the validation review | managers | quality | S-01 page 59 | C-48 |
| R-0037 | Where possible, scope matching should be quantitative instead of qualitative, in functional size units | managers | quality | S-01 page 59 | C-48 |
| R-0038 | When scope exceeds cost, schedule or staffing constraints, scope must be reduced, capacity must be increased, or a combination must be negotiated | managers | quality | S-01 page 59 | C-48 |
| R-0039 | Defects against higher-priority requirements should probably be repaired before defects against lower-priority requirements | quality assurance staff | quality | S-01 page 60 | C-43 |
| R-0040 | The architecture should be documented to support its uses (shared understanding, design, analysis, reverse engineering, maintenance) | software engineers | quality | S-01 page 70 | C-47 |
| R-0041 | Notations should be chosen based on the need, purpose and utility of the choice for the stakeholders who need that information | software engineers | quality | S-01 page 70 | C-47 |
| R-0042 | A good architecture should address not only the distinct concerns of its stakeholders but also the consequences of their interactions | software engineers | quality | S-01 page 77 | C-47 |
| R-0043 | A program must be correct and should be efficient (quoted passage from a 1974 essay, reproduced as an illustration of separation of concerns) | software engineers | quality | S-01 page 69 | C-47 |
| R-0044 | The design must provide a guide to implementors on building the system | software engineers | quality | S-01 page 85 | C-47 |
| R-0045 | An SDD should be sufficient as a basis for verifying a design | software engineers | quality | S-01 page 86 | C-47 |
| R-0046 | A design should be sufficient for designers to show how requirements will be met | software engineers | quality | S-01 page 86 | C-47 |
| R-0047 | Design should be complete with respect to the modes and states of the software | software engineers | quality | S-01 page 86 | C-47 |
| R-0048 | Modules should be loosely or weakly coupled, as most design methods advocate | software engineers | quality | S-01 page 86 | C-47 |
| R-0049 | Modules should maximize their cohesion, as most design methods advocate | software engineers | quality | S-01 page 86 | C-47 |
| R-0050 | Each module should have a single responsibility, as David Parnas advocated | software engineers | quality | S-01 page 86 | C-47 |
| R-0051 | An algorithm that could be architecturally significant must be determined early in the life cycle | software engineers | quality | S-01 page 87 | C-47 |
| R-0052 | The high-level design definition should be sufficiently detailed for client designers or programmers to use services without reading the code | consumers | quality | S-01 page 87 | C-47 |
| R-0053 | The detailed design specifications should be sufficient to allow programmers to code each module | software engineers | quality | S-01 page 87 | C-47 |
| R-0054 | Projects should make conscious decisions about which design specifications are needed, based on audience, subject and intended usage | software engineers | quality | S-01 page 90 | C-47 |
| R-0055 | Ideally a program should have at least as many test cases as its number of linearly independent paths | software engineers | quality | S-01 page 100 | C-39 |
| R-0056 | Software engineers should build flexibility and adaptability into software so that changes are easier to incorporate | software engineers | quality | S-01 page 101 | C-47 |
| R-0057 | Software teams should embrace change by agile development, DevOps practice, and continuous delivery and deployment practices | software engineers | operations | S-01 page 101 | C-24 |
| R-0058 | Any dependency in the supply chain network should be managed by developers or tools | software engineers | quality | S-01 page 103 | C-51 |
| R-0059 | Unnecessary dependencies should be avoided to improve build efficiency | software engineers | quality | S-01 page 103 | C-44 |
| R-0060 | License conflicts between dependencies and software products should be avoided to reduce legal risk | security engineers | security | S-01 page 103 | C-20 |
| R-0061 | Propagation of dependency defects or vulnerabilities into software products should be avoided to improve quality | security engineers | security | S-01 page 103 | C-11 |
| R-0062 | Regulations and monitoring mechanisms should be developed to prevent developers from introducing untrusted external dependencies | software engineers | security | S-01 page 103 to 104 | C-20 |
| R-0063 | Programmers should know good practices and common vulnerabilities | software engineers | quality | S-01 page 107 | C-49 |
| R-0064 | Developers should encapsulate reusable code fragments into well-structured libraries or components to avoid code clones | software engineers | operations | S-01 page 106 | C-33 |
| R-0065 | An API should always include statements about the program effects or behaviours | software engineers | quality | S-01 page 108 | C-47 |
| R-0066 | API design should make the API easy to learn, readable, hard to misuse, easy to extend, complete, and backward compatible | software engineers | quality | S-01 page 108 | C-47 |
| R-0067 | An API should be straightforward and stable to facilitate client application development and maintenance | consumers | quality | S-01 page 108 | C-47 |
| R-0068 | The developers need to develop and build an application separately for each target platform | software engineers | quality | S-01 page 108 | C-44 |
| R-0069 | Exception-handling policies should be designed carefully following common principles | software engineers | quality | S-01 page 109 | C-47 |
| R-0070 | The design and construction processes should accommodate string and character set issues for multiple locales | software engineers | quality | S-01 page 110 | C-47 |
| R-0071 | Cloud-based software developers need to consider cloud infrastructure issues such as an API gateway and service registration | software engineers | quality | S-01 page 111 | C-47 |
| R-0072 | For each executed test case, it must be possible to decide whether the observed SUT outcomes match the expected outcomes | software engineers | quality | S-01 page 118 | C-38 |
| R-0073 | Software engineers must be aware that different test selection criteria might yield very different effectiveness | software engineers | quality | S-01 page 118 | C-38 |
| R-0074 | Faults that cause failures must be removed | quality assurance staff | quality | S-01 page 119 | C-43 |
| R-0075 | Testing needs to focus on specific mandatory prescriptions, such as requirements, laws and standards | software engineers | quality | S-01 page 120 | C-38 |
| R-0076 | Test cases should be generated and executed to give evidence of adherence to the selected prescriptions | software engineers | quality | S-01 page 120 | C-38 |
| R-0077 | Effective unit and integration testing should have identified many SUT defects | software engineers | quality | S-01 page 123 | C-38 |
| R-0078 | In some cases, a trade-off must be made between regression testing after every change and the resources that it needs | software engineers | quality | S-01 page 124 | C-37 |
| R-0079 | The testing environment needs to represent the actual operational environment for usage-based testing | operations engineers | operations | S-01 page 131 | C-26 |
| R-0080 | The sequence of test case execution should reproduce the use of the SUT by the target stakeholder | software engineers | quality | S-01 page 131 | C-38 |
| R-0081 | For the mutation technique to be effective, many mutants must be generated and executed automatically and systematically | software engineers | quality | S-01 page 131 | C-38 |
| R-0082 | For each specification-based, structure-based and experience-based technique, the coverage measures and the coverage evaluation procedure must be determined | software engineers | quality | S-01 page 132 | C-39 |
| R-0083 | Testing processes should allow the automation of the different testing phases | software engineers | quality | S-01 page 134 | C-37 |
| R-0084 | Testing processes should rely on controllability, traceability, replicability, and risk and cost estimation of the performed activities | software engineers | quality | S-01 page 134 | C-38 |
| R-0085 | Fault injection should be used with great care | software engineers | quality | S-01 page 134 | C-38 |
| R-0086 | Testing concepts, strategies, techniques and measures need to be integrated into a defined and controlled test planning process | software engineers | quality | S-01 page 134 | C-38 |
| R-0087 | In shift-left developments, a test strategy should include at least the purposes, objectives, scope, and environment and methods | software engineers | quality | S-01 page 135 | C-38 |
| R-0088 | Test activities should be organized, with people, tools, policies and measures, into a well-defined process that is integral to the life cycle | software engineers | quality | S-01 page 135 | C-38 |
| R-0089 | Test documentation should be produced and continuously updated with the same quality as other software engineering documentation | software engineers | quality | S-01 page 135 | C-38 |
| R-0090 | Test documentation should be under the control of software configuration management | operations engineers | operations | S-01 page 135 | C-35 |
| R-0091 | Monitor and control of testing must define the required data and information, and state how to obtain them | software engineers | quality | S-01 page 136 | C-39 |
| R-0092 | The resources spent on testing should be commensurate with the use and criticality of the application | software engineers | quality | S-01 page 136 | C-38 |
| R-0093 | A decision must be made about how much testing is enough and when a test stage can be completed | software engineers | quality | S-01 page 136 | C-38 |
| R-0094 | Suitable knowledge-based repositories should be configured and managed for test reusability, so that changes to requirements or design are reflected in the tests | software engineers | quality | S-01 page 136 | C-38 |
| R-0095 | Testing activities must be planned | software engineers | quality | S-01 page 137 | C-38 |
| R-0096 | The testing environment should be compatible with the other software engineering tools used | software engineers | quality | S-01 page 137 | C-38 |
| R-0097 | Execution of tests should follow the basic principle of controlled experimentation | software engineers | quality | S-01 page 137 | C-38 |
| R-0098 | Everything done during testing should be performed and documented clearly enough that another person could replicate the results | software engineers | quality | S-01 page 137 | C-38 |
| R-0099 | Testing should follow documented procedures and use a clearly defined version of the SUT | software engineers | quality | S-01 page 137 | C-38 |
| R-0100 | In shift-left-based development, different testing aspects should be considered | software engineers | quality | S-01 page 139 | C-38 |
| R-0101 | For IoT, security, privacy, communications and user or component interaction should be considered in the quality assessment | quality assurance staff | quality | S-01 page 141 | C-41 |
| R-0102 | For the legal domain, performance testing of the data repository, testing of accurate communication, integration testing, and consistency and compliance testing should also be done | software engineers | quality | S-01 page 141 | C-38 |
| R-0103 | For mobile applications, device-specific aspects such as screen resolution, GPS, operating systems and device manufacturers should also be considered during testing | software engineers | quality | S-01 page 141 | C-38 |
| R-0104 | For embedded systems, testing should assess the functional and non-functional attributes of both software and hardware | software engineers | quality | S-01 page 141 | C-38 |
| R-0105 | For healthcare, testing should ensure quality in areas such as secure and reliable data exchange, stable performance, privacy and safety | software engineers | quality | S-01 page 141 | C-38 |
| R-0106 | For healthcare, interoperability, usability, performance, compliance with industry regulations, and security and safety standards should also be considered | software engineers | quality | S-01 page 141 | C-38 |
| R-0107 | Software engineering operations must manage defects found after release, changes to the software environment and hardware, and new user requirements. | operations engineers | operations | S-01 page 151 | C-36 |
| R-0108 | Three aspects should be considered in defining bugs and testing AI, ML and DL systems: required conditions, including correctness, robustness, security and privacy; the AI items; and the testing activities. | software engineers | quality | S-01 page 142 | C-38 |
| R-0109 | Integration testing should be performed to check consistency when a blockchain works with other applications. | software engineers | quality | S-01 page 143 | C-38 |
| R-0110 | Strategies for many transactions should be conceived to guarantee a satisfactory performance level. | software engineers | quality | S-01 page 143 | C-38 |
| R-0111 | Qualitative and quantitative metrics, such as transaction validation latency and security, should also be considered for blockchain systems. | quality assurance staff | quality | S-01 page 143 | C-41 |
| R-0112 | Different aspects should be considered during the testing of a blockchain-based system under test. | software engineers | quality | S-01 page 143 | C-38 |
| R-0113 | Cloud testing should also focus on compatibility and interoperability among heterogeneous cloud resources. | software engineers | quality | S-01 page 143 | C-38 |
| R-0114 | Software must be thoroughly tested before it is released. | software engineers | quality | S-01 page 155 | C-37 |
| R-0115 | Testing must be automated as much as possible throughout the entire software process. | software engineers | quality | S-01 page 155 | C-37 |
| R-0116 | Software engineers and operations engineers need to troubleshoot hardware and software incidents found in production or in internal testing. | operations engineers | operations | S-01 page 155 | C-29 |
| R-0117 | The operations engineer must install software as part of its deployment. | operations engineers | operations | S-01 page 155 | C-24 |
| R-0118 | The operations engineer should replicate and verify reported problems by running the appropriate tests. | operations engineers | quality | S-01 page 155 | C-43 |
| R-0119 | Software engineers should be aware that operations processes can be adapted to small organizations. | software engineers | quality | S-01 page 163 | C-48 |
| R-0120 | Software organizations should address staff recruitment, resource planning, succession planning and training. | managers | quality | S-01 page 153 | C-49 |
| R-0121 | Operations engineers should be trained in the relevant aspects of service management. | operations engineers | quality | S-01 page 154 | C-49 |
| R-0122 | Operations engineers should develop their teamwork and leadership skills. | operations engineers | quality | S-01 page 154 | C-49 |
| R-0123 | A chronological training record should be maintained for each individual. | software engineers | quality | S-01 page 154 | C-49 |
| R-0124 | Software engineering operations planning should comprise part of the process of translating project requirements into services. | operations engineers | operations | S-01 page 156 | C-34 |
| R-0125 | Software engineering operations planning should provide a road map for directing progress. | operations engineers | operations | S-01 page 156 | C-34 |
| R-0126 | Suppliers must be well coordinated to ensure quality service. | security engineers | security | S-01 page 156 | C-20 |
| R-0127 | Operations planning should begin with the decision to develop a new software product and should consider maintenance and operations requirements early. | operations engineers | operations | S-01 page 156 | C-34 |
| R-0128 | A concept document should be developed, followed by an operations and maintenance plan. | operations engineers | operations | S-01 page 156 | C-34 |
| R-0129 | The concept document and the operations and maintenance plan should address the scope, the adaptation of the process and tools, the operations organization and the cost estimate. | operations engineers | operations | S-01 page 156 | C-34 |
| R-0130 | Operations engineers should document their operations steps and tools in any suitable form. | operations engineers | operations | S-01 page 156 | C-34 |
| R-0131 | The concept of operations should be prepared during software development and should specify how users request modifications and report problems. | consumers | operations | S-01 page 156 | C-34 |
| R-0132 | ISO/IEC/IEEE 20000-1 recommends that the operations plan addresses several planning perspectives, including roles, staffing, budgets and measurable expected outcomes. | operations engineers | operations | S-01 page 157 | C-34 |
| R-0133 | The operations organization must conduct business planning activities for budget, finance and human resources. | operations engineers | operations | S-01 page 157 | C-34 |
| R-0134 | Release or version planning requires operations engineers to set target dates, agree release content, identify conflicts, assess release risk, develop a rollback and data migration plan, and inform all stakeholders. | operations engineers | operations | S-01 page 157 | C-25 |
| R-0135 | The approach to supplier management should be determined by the nature of the products and services needed in a project. | security engineers | security | S-01 page 157 | C-20 |
| R-0136 | Engineers must ensure that the different environments are coherent and synchronized with the production environment. | software engineers | operations | S-01 pages 157–158 | C-26 |
| R-0137 | DevOps recommends that the creation of all environments be automated and built from a single code repository. | operations engineers | operations | S-01 page 158 | C-26 |
| R-0138 | All environments need to be built from the same code source. | operations engineers | operations | S-01 page 158 | C-26 |
| R-0139 | Service availability and continuity must be managed to ensure that customer commitments are met. | consumers | operations | S-01 page 158 | C-27 |
| R-0140 | Operations engineers will ensure that the proper infrastructure is planned, designed, implemented and tested. | operations engineers | operations | S-01 page 158 | C-30 |
| R-0141 | Business predictions and workload estimates should be translated into specific documented requirements. | operations engineers | operations | S-01 page 158 | C-30 |
| R-0142 | The reaction to variations in workload or environment should be predictable. | operations engineers | operations | S-01 page 158 | C-30 |
| R-0143 | Data on current and previous components and on resource use should be captured and analyzed. | operations engineers | operations | S-01 page 158 | C-28 |
| R-0144 | The capacity management process should directly support the development of new and changed services by sizing and modeling them. | operations engineers | operations | S-01 page 158 | C-30 |
| R-0145 | A capacity plan should be produced at a suitable frequency, at least annually. | operations engineers | operations | S-01 page 158 | C-30 |
| R-0146 | The capacity plan should document costed options and recommend solutions for the agreed service-level targets. | operations engineers | operations | S-01 page 158 | C-30 |
| R-0147 | The technical infrastructure and its current and projected capacities should be well understood. | operations engineers | operations | S-01 page 158 | C-30 |
| R-0148 | ISO/IEC/IEEE 20000-1 proposes that backups, documents, software, equipment and staff for service restoration should be quickly available after a major service failure or disaster. | operations engineers | operations | S-01 page 158 | C-30 |
| R-0149 | The need for successful recovery should influence which backup and recovery methods are used. | operations engineers | operations | S-01 page 158 | C-30 |
| R-0150 | Preparedness and regular testing of backup, disaster recovery and failover should be constantly rehearsed as the production environment changes. | operations engineers | operations | S-01 page 159 | C-30 |
| R-0151 | Software engineers should understand that failure is inevitable. | software engineers | quality | S-01 page 159 | C-49 |
| R-0152 | Software applications should include failure-handling logic, which must be planned during development. | software engineers | quality | S-01 page 159 | C-47 |
| R-0153 | Operations engineers should strive to enforce the information security controls listed in the source. | operations engineers | security | S-01 page 159 | C-19 |
| R-0154 | Senior management should define the information security policy, communicate it to staff and customers, and act to ensure its implementation. | managers | security | S-01 page 159 | C-19 |
| R-0155 | Information security management roles and responsibilities should be defined and allocated to post holders. | security engineers | security | S-01 page 159 | C-19 |
| R-0156 | A representative of the management team should be assigned the role of monitoring and maintaining the effectiveness of the information security policy. | managers | security | S-01 page 159 | C-19 |
| R-0157 | Staff with significant security roles should receive information security training. | security engineers | security | S-01 page 159 | C-19 |
| R-0158 | All staff should be made aware of the information security policy. | software engineers | security | S-01 page 159 | C-19 |
| R-0159 | Expert help on risk assessment and control implementation should be available. | security engineers | security | S-01 page 159 | C-19 |
| R-0160 | Changes should not compromise the effective operation of controls. | operations engineers | operations | S-01 page 159 | C-31 |
| R-0161 | Information security incidents should be reported following incident management procedures, and a response should be initiated. | operations engineers | operations | S-01 page 159 | C-29 |
| R-0162 | DevOps calls for automating the different deployment steps, including packaging, configuration, installation, launch and smoke testing. | operations engineers | operations | S-01 page 160 | C-24 |
| R-0163 | Software engineers ensure that a new version and its databases can be rolled back quickly if the version causes defects or product degradation. | software engineers | operations | S-01 page 160 | C-25 |
| R-0164 | Software applications or services must be architected to enable small, independent software deployments. | operations engineers | operations | S-01 page 161 | C-24 |
| R-0165 | Engineers should be informed about system quality and operational health with evidence. | software engineers | operations | S-01 page 161 | C-28 |
| R-0166 | Operations engineers must manage a number of risks. | operations engineers | quality | S-01 page 162 | C-48 |
| R-0167 | Operations engineers need to talk with product owners and software engineers to agree a level of risk tolerance. | operations engineers | quality | S-01 page 162 | C-48 |
| R-0168 | Operations engineers need to establish automated systems and tools for measurement, analysis, reporting and control. | operations engineers | operations | S-01 page 162 | C-28 |
| R-0169 | The overall operations process needs to be automated as much as possible to prevent incidents and problems. | operations engineers | operations | S-01 page 162 | C-34 |
| R-0170 | Automated testing needs to be integrated throughout the operations process. | software engineers | quality | S-01 page 162 | C-37 |
| R-0171 | Product telemetry should be implemented with analytics techniques to detect problems as early as possible. | operations engineers | operations | S-01 page 162 | C-28 |
| R-0172 | Data collected at all layers of the product stack must be collected and analyzed. | managers | quality | S-01 page 162 | C-52 |
| R-0173 | Testing must be automated as much as possible throughout the entire software delivery process, to give developers fast and constant feedback. | software engineers | quality | S-01 page 164 | C-37 |
| R-0174 | A testing strategy covering unit, integration, system and user acceptance tests must be defined, and tools to automate the testing phases must be selected. | software engineers | quality | S-01 page 164 | C-38 |
| R-0175 | Maintainers must understand and use software artifacts from development, such as code, tests and documentation, support them immediately, and evolve and maintain them over time. | project maintainers | operations | S-01 page 169 | C-36 |
| R-0176 | Software must be continually adapted, or it becomes progressively less satisfactory. | operations engineers | operations | S-01 page 169 | C-36 |
| R-0177 | A number of key issues must be dealt with to ensure the effective maintenance of software. | operations engineers | operations | S-01 page 171 | C-36 |
| R-0178 | To ensure a software modification is validated, the maintainer should replicate or verify changes by planning and executing the appropriate tests. | project maintainers | operations | S-01 page 171 | C-36 |
| R-0179 | Impact analysis tasks include developing an identification scheme for modification requests and problem reports. | operations engineers | operations | S-01 page 172 | C-36 |
| R-0180 | Impact analysis tasks include developing a scheme for categorizing and prioritizing modification requests and problem reports. | operations engineers | operations | S-01 page 172 | C-36 |
| R-0181 | Impact analysis tasks include determining the procedures for an operator to submit a modification request or problem report. | operations engineers | operations | S-01 page 172 | C-36 |
| R-0182 | Impact analysis tasks include identifying the information needs to be tracked and reported to users, and the measures that give feedback on them. | consumers | operations | S-01 page 172 | C-36 |
| R-0183 | Impact analysis tasks include determining how temporary work-arounds will be provided to operators. | operations engineers | operations | S-01 page 172 | C-36 |
| R-0184 | Impact analysis tasks include tracking the work-arounds through to removal. | operations engineers | operations | S-01 page 172 | C-36 |
| R-0185 | Impact analysis tasks include determining what follow-up feedback will be provided to users. | consumers | operations | S-01 page 172 | C-36 |
| R-0186 | Software engineers should strive to conduct impact analysis as cost-effectively as possible. | software engineers | operations | S-01 page 172 | C-36 |
| R-0187 | Maintainability should be specified, reviewed and controlled during software development activities. | operations engineers | operations | S-01 page 172 | C-36 |
| R-0188 | Organizational objectives and constraints must be balanced with software maintainability and engineering standards to avoid code decay and technical debt. | managers | operations | S-01 page 173 | C-36 |
| R-0189 | Software engineers must investigate three areas in depth when they address technical debt: code quality versus relevance, alignment with organizational objectives, and process loss. | software engineers | operations | S-01 page 173 | C-36 |
| R-0190 | The software architecture should reflect the goals of the organization. | software engineers | quality | S-01 page 173 | C-47 |
| R-0191 | Ensure complementary skills of the software engineers involved in addressing technical debt. | software engineers | quality | S-01 page 173 | C-49 |
| R-0192 | Outsourcers need to invest in good communication infrastructure and in an efficient help desk staffed with people who can communicate effectively with customers and users. | security engineers | security | S-01 page 174 | C-20 |
| R-0193 | The approach to supplier management should be determined by the nature of the products and services concerned. | managers | security | S-01 page 174 | C-20 |
| R-0194 | Software engineers must understand the different categories of software maintenance. | software engineers | operations | S-01 page 175 | C-36 |
| R-0195 | It is important that the organization delegates maintenance tasks to an experienced group or person and keeps quality documentation on maintenance tasks and all changes made to the software. | managers | operations | S-01 page 175 | C-36 |
| R-0196 | A handoff process must be put in place between developers and maintainers. | project maintainers | operations | S-01 page 175 | C-36 |
| R-0197 | Technical debt should not be handled in isolation but through an examination of its root causes. | quality assurance staff | quality | S-01 page 175 | C-43 |
| R-0198 | The codebase of a software product must remain maintainable, easily understood and easy to evolve further. | operations engineers | operations | S-01 page 175 | C-36 |
| R-0199 | Maintainers should determine which measures are appropriate for a specific organization, based on its needs. | project maintainers | operations | S-01 page 176 | C-36 |
| R-0200 | Maintainers must track requirements in their activities, as in development, and update documentation as baselines change. | project maintainers | operations | S-01 page 177 | C-35 |
| R-0201 | Software maintenance planning should begin with the decision to develop a new software product and should consider quality objectives. | operations engineers | operations | S-01 page 178 | C-36 |
| R-0202 | A concept document should be developed, followed by a maintenance plan. | operations engineers | operations | S-01 page 178 | C-36 |
| R-0203 | The maintenance plan should address the scope of software maintenance and the adaptation of the software maintenance processes and tools. | operations engineers | operations | S-01 page 178 | C-36 |
| R-0204 | The maintenance planning process must address the issues associated with a number of planning perspectives. | operations engineers | operations | S-01 page 178 | C-36 |
| R-0205 | When a maintainer uses a development process, the process must be tailored to meet specific needs. | project maintainers | operations | S-01 page 178 | C-36 |
| R-0206 | Release or version planning requires the maintainer to collect the dates of availability of individual requests. | project maintainers | operations | S-01 page 178 | C-32 |
| R-0207 | Release or version planning requires the maintainer to agree with users on the content of subsequent releases or versions. | project maintainers | operations | S-01 page 178 | C-32 |
| R-0208 | Release or version planning requires the maintainer to identify potential conflicts and develop alternatives. | project maintainers | operations | S-01 page 178 | C-32 |
| R-0209 | Release or version planning requires the maintainer to assess the risk of a given release and develop a back-out plan in case problems arise. | project maintainers | operations | S-01 page 178 | C-32 |
| R-0210 | Release or version planning requires the maintainer to inform all stakeholders. | project maintainers | operations | S-01 page 178 | C-32 |
| R-0211 | A software maintenance plan should be prepared during software development. | operations engineers | operations | S-01 page 179 | C-36 |
| R-0212 | A software maintenance plan should specify how users request modifications and report problems or issues. | consumers | operations | S-01 page 179 | C-36 |
| R-0213 | Maintainers should have an effective quality program. | project maintainers | quality | S-01 page 179 | C-42 |
| R-0214 | Maintainers must implement processes to support the continuous improvement of software maintenance processes. | project maintainers | quality | S-01 page 179 | C-52 |
| R-0215 | The activities and techniques for SQA, V&V, reviews and audits must be selected in concert with all the other processes to achieve the desired level of quality. | quality assurance staff | quality | S-01 page 179 | C-42 |
| R-0216 | It is recommended that software operations and maintenance adapt and use the output of software development, its techniques and deliverables, and test results. | operations engineers | operations | S-01 page 179 | C-36 |
| R-0217 | SCM procedures should provide for verification, validation and audit of each step required to identify, authorize, implement and release the software product and its IT assets undergoing change. | operations engineers | operations | S-01 page 179 | C-35 |
| R-0218 | Any change made to the software product and its underlying infrastructure must be controlled. | operations engineers | operations | S-01 page 179 | C-35 |
| R-0219 | The SCM activities should operationalize SCM process management and planning, configuration identification, change control, status accounting, auditing, and release management and delivery | operations engineers | operations | S-01 page 185 | C-35 |
| R-0220 | Branching and merging strategies should be carefully planned and communicated | operations engineers | operations | S-01 page 187 | C-35 |
| R-0221 | SCM process planning for a project should be consistent with the organizational context, applicable constraints, commonly accepted guidance and the nature of the project | operations engineers | operations | S-01 page 187 | C-35 |
| R-0222 | The SCM plan is subject to SQA review and audit | operations engineers | operations | S-01 page 187 | C-35 |
| R-0223 | SCM planning should consider the software development life cycle model chosen | operations engineers | operations | S-01 page 188 | C-35 |
| R-0224 | SCM activities must be planned accordingly for continuous integration build-test-deploy cycles | operations engineers | operations | S-01 page 188 | C-24 |
| R-0225 | Organizational roles must be clearly identified | operations engineers | operations | S-01 page 188 | C-35 |
| R-0226 | Responsibilities must be assigned to organizational entities | operations engineers | operations | S-01 page 188 | C-35 |
| R-0227 | The overall authority and reporting channels for SCM should be identified | operations engineers | operations | S-01 page 188 | C-35 |
| R-0228 | Tool selection and implementation should be carefully planned, using the listed questions | operations engineers | operations | S-01 page 188 | C-35 |
| R-0229 | The team must determine whether the SCM workbench will be open or integrated | software engineers | operations | S-01 page 188 | C-35 |
| R-0230 | Subcontractor SCM requirements and the means for monitoring compliance need to be established | security engineers | security | S-01 page 189 | C-20 |
| R-0231 | An SCMP should include the sections introduction, SCM management, SCM activities, SCM schedules, SCM resources and SCMP maintenance | operations engineers | operations | S-01 page 189 | C-35 |
| R-0232 | Teams implementing an SCMP need to develop more detailed subordinate procedures | software engineers | operations | S-01 page 189 | C-35 |
| R-0233 | The person responsible for SCM ensures that those with assigned responsibility perform the defined SCM tasks correctly | software engineers | operations | S-01 page 189 | C-35 |
| R-0234 | Care must be taken to keep surveillance focused on the insights gained from measurements | managers | quality | S-01 page 190 | C-52 |
| R-0235 | A balance must be achieved between adequate visibility for project control and a manageable number of controlled items when selecting SCIs | operations engineers | operations | S-01 page 190 | C-35 |
| R-0236 | Requirements and test cases should be linked with the code baselines developed | operations engineers | operations | S-01 page 192 | C-35 |
| R-0237 | The repository of binary objects should contain cryptographic hashes used to perform the PCA | operations engineers | operations | S-01 page 192 | C-35 |
| R-0238 | It is very important to identify the change control rules of the context and to adhere strictly to those rules | operations engineers | operations | S-01 page 193 | C-35 |
| R-0239 | An effective SCR process requires the use of supporting tools and procedures | operations engineers | operations | S-01 page 194 | C-35 |
| R-0240 | A CR application must include a CR form that describes the request and gives its rationale | operations engineers | operations | S-01 page 194 | C-35 |
| R-0241 | A CR application must include a change certification form when the CR is granted | operations engineers | operations | S-01 page 194 | C-35 |
| R-0242 | Humans are responsible for designing the CR forms | operations engineers | operations | S-01 page 194 | C-35 |
| R-0243 | A means for tracking which SCRs are incorporated into particular software versions and baselines must be provided | operations engineers | operations | S-01 page 194 | C-35 |
| R-0244 | Information about configuration status should be secured where relevant | operations engineers | operations | S-01 page 195 | C-35 |
| R-0245 | Configuration status information for the evolving configurations must be identified, collected and maintained | operations engineers | operations | S-01 page 195 | C-35 |
| R-0246 | The SCSA activity must be done by following the logical schemes defined for CIs, baselines and relationships | operations engineers | operations | S-01 page 195 | C-35 |
| R-0247 | How to conduct a configuration review and its expected result must be described in the quality plan or in a defined configuration auditing procedure | operations engineers | operations | S-01 page 196 | C-35 |
| R-0248 | Each audit must be carefully planned | operations engineers | operations | S-01 page 196 | C-35 |
| R-0249 | SCM must usually be able to reproduce previous releases for recovery, testing, maintenance or additional release purposes | operations engineers | operations | S-01 page 197 | C-35 |
| R-0250 | Supporting tools and associated build instructions must be under SCM control when an exact copy of a built SCI must be rebuilt | operations engineers | operations | S-01 page 197 | C-35 |
| R-0251 | Software must be supported and continuously improved throughout its life cycle. | operations engineers | operations | S-01 page 202; page 203 | C-36 |
| R-0252 | Activities should include software requirements review, covering elicitation, analysis, specification and validation. | software engineers | quality | S-01 page 207 | C-46 |
| R-0253 | While developing the work breakdown structure, engineers should consider all configuration items as tasks to have under control. | software engineers | operations | S-01 page 208 | C-35 |
| R-0254 | Stakeholders should agree on how requirements and scope are reviewed and revised. | software engineers | quality | S-01 page 208 | C-46 |
| R-0255 | When changes are accepted, forward or backward traceability analysis and risk analysis should be used to find their impact. | software engineers | quality | S-01 page 208 | C-46 |
| R-0256 | Software quality management processes should be planned along with project planning. | quality assurance staff | quality | S-01 page 208 | C-42 |
| R-0257 | The quality planning should establish procedures and responsibilities for SQA, verification and validation, reviews and audits. | quality assurance staff | quality | S-01 page 208 | C-42 |
| R-0258 | The work products of each project activity, such as design documents, inspection reports and tested software, should be identified and characterized. | managers | quality | S-01 page 209 | C-48 |
| R-0259 | Opportunities to reuse software components from previous projects, or to use off-the-shelf products, should be evaluated. | operations engineers | operations | S-01 page 209 | C-33 |
| R-0260 | Software procurement and the use of third parties to develop deliverables should be planned and suppliers selected. | security engineers | security | S-01 page 209 | C-20 |
| R-0261 | Automated tools for the project, including tools for software configuration management and software quality, should be planned for and acquired. | security engineers | security | S-01 page 209 | C-20 |
| R-0262 | Delivery speed and frequent modular upgrades should be balanced with risk management activities. | managers | quality | S-01 page 206 | C-48 |
| R-0263 | Particular attention should be paid to managing risks related to software quality requirements, such as safety or security. | managers | quality | S-01 page 210 | C-48 |
| R-0264 | Software quality requirements for a project and its work products should be identified, quantitatively and qualitatively. | quality assurance staff | quality | S-01 page 211 | C-41 |
| R-0265 | Thresholds for acceptable quality measurements should be set for each software quality requirement, based on stakeholder needs and expectations. | quality assurance staff | quality | S-01 page 211 | C-41 |
| R-0266 | Procedures for ongoing SQA and quality improvement, and for verifying and validating the deliverable software, should be specified during quality planning. | quality assurance staff | quality | S-01 page 211 | C-42 |
| R-0267 | Plans for supporting processes, such as documentation, software configuration management and problem resolution, should also be managed. | quality assurance staff | quality | S-01 page 211 | C-42 |
| R-0268 | Regardless of how components are obtained, verification, integration and validation of the components should be performed. | security engineers | security | S-01 page 212 | C-20 |
| R-0269 | Organizations should consider technical or procedural controls to reduce the risk from unfiltered access to external library repositories. | managers | security | S-01 page 212 | C-20 |
| R-0270 | After an agreement is in place, the project should be managed in compliance with the terms of the agreement. | managers | quality | S-01 page 213 | C-48 |
| R-0271 | Deliverables should be evaluated for their required characteristics, for example by inspection or by demonstrating working functionality. | quality assurance staff | quality | S-01 page 213 | C-42 |
| R-0272 | Adherence to software quality requirements should be evaluated. | quality assurance staff | quality | S-01 page 213 | C-42 |
| R-0273 | Outlier identification and analysis of quality and other measurement data, such as defect analysis, should be performed. | quality assurance staff | quality | S-01 page 213 | C-43 |
| R-0274 | In all cases, the software development team should adhere to software configuration control and software configuration management procedures. | software engineers | operations | S-01 page 214 | C-35 |
| R-0275 | Project materials should be archived under stakeholder-agreed rules, possibly including destruction of sensitive information and media. | security engineers | security | S-01 page 215 | C-23 |
| R-0276 | Consider measuring the software's internal quality to give an early indicator of potential issues. | quality assurance staff | quality | S-01 page 216 | C-41 |
| R-0277 | Software processes must be selected, adapted and applied as appropriate for each project and each organizational context | managers | quality | S-01 page 222 | C-48 |
| R-0278 | It is essential that software engineering process management is supported by empirical measurement | managers | quality | S-01 page 222 | C-48 |
| R-0279 | A life cycle should be defined following engineering principles that guide engineering as a discipline | managers | quality | S-01 page 224 | C-48 |
| R-0280 | The process specification should be useful to humans so that they can communicate using it | managers | quality | S-01 page 224 | C-48 |
| R-0281 | The life cycle specification should be easy to understand and correct, because it is the basis for technical and engineering management, quality management and measurement | managers | quality | S-01 page 224 | C-48 |
| R-0282 | A suitable life cycle will consider all the business and technical needs of the stakeholders | managers | quality | S-01 page 225 | C-48 |
| R-0283 | When a project process is defined in conformance with a life cycle, it is important to make sure that metrics and measure definitions allow realistic estimations and measurements | managers | quality | S-01 page 228 | C-48 |
| R-0284 | Project process and product measurements should always provide accurate information about the status of the process and the product while the life cycle process runs | managers | quality | S-01 page 228 to 229 | C-48 |
| R-0285 | Discussions about the life cycle should always be supported by realistic process and product estimations and measurements | managers | quality | S-01 page 229 | C-48 |
| R-0286 | If the accuracy of estimations and measurements is uncertain, a reflection should take place on the overall approach | managers | quality | S-01 page 229 | C-48 |
| R-0287 | Developers must monitor the execution of the software engineering process, assess whether the process objectives are met, and assess risks | software engineers | quality | S-01 page 229 | C-48 |
| R-0288 | Once a code unit has been tested successfully, this result should be recorded so that the rest of the team can be aware of it | software engineers | quality | S-01 page 229 | C-39 |
| R-0289 | The configuration management tool and the testing tool will have to be integrated | operations engineers | operations | S-01 page 229 | C-35 |
| R-0290 | Tools will, ideally, have to support the methods they serve and be integrated with them | managers | quality | S-01 page 229 | C-48 |
| R-0291 | Analysis of constructed models is needed to ensure that the models are complete, consistent and correct enough for their intended purpose | software engineers | quality | S-01 page 237 | C-47 |
| R-0292 | The model should be checked for documented assumptions | software engineers | quality | S-01 page 236 | C-47 |
| R-0293 | Model parts imported from another model or library must be examined for semantic assumptions that conflict with the new modeling environment | software engineers | quality | S-01 page 236 | C-47 |
| R-0294 | Traceability relationships must be mapped and controlled to demonstrate the consistency of software requirements with the software model | software engineers | quality | S-01 page 238 | C-46 |
| R-0295 | Release managers need to monitor the development process and the promotion schedule for each release | operations engineers | operations | S-01 page 243 | C-32 |
| R-0296 | The software process quality aspect must be made explicit. | managers | quality | S-01 page 247 | C-48 |
| R-0297 | Software quality should be planned early and assessed at many milestones during the software life cycle. | quality assurance staff | quality | S-01 page 248 | C-42 |
| R-0298 | The software requirements are expected to define the required software quality attributes. | quality assurance staff | quality | S-01 page 248 | C-41 |
| R-0299 | Software engineers are expected to share a commitment to software quality in the context of their industry and culture. | software engineers | quality | S-01 page 248 | C-49 |
| R-0300 | Software engineers should understand software quality concepts, characteristics and values and their application to development, maintenance and operation activities. | software engineers | quality | S-01 page 248 | C-49 |
| R-0301 | Software engineers should use the meaning of error and defect given by their standards. | software engineers | quality | S-01 page 248 | C-43 |
| R-0302 | Agreement on software quality for all stakeholders requires that the many aspects of quality be formally defined and communicated. | software engineers | quality | S-01 page 248 | C-41 |
| R-0303 | Software engineers should inform their administration of the risks they take when they are not fully committed to quality. | software engineers | quality | S-01 page 249 | C-48 |
| R-0304 | Software engineers should seek the optimal cost of software quality, the minimal total cost for a specified quality level. | software engineers | quality | S-01 page 249 | C-48 |
| R-0305 | Software engineers should know the key software engineering standards that apply to their specific industry. | software engineers | quality | S-01 page 249 | C-49 |
| R-0306 | Software engineers and their managers must understand the threats and issues and develop the skills needed to anticipate and prevent accidents before they occur. | managers | quality | S-01 page 250 | C-49 |
| R-0307 | Management sponsorship should be solicited frequently during software project review to ensure software quality activities are executed and nonconformities addressed. | quality assurance staff | quality | S-01 page 251 | C-42 |
| R-0308 | Management support is imperative for a QMS to be effective. | managers | quality | S-01 page 251 | C-48 |
| R-0309 | A QMS requires policies, procedures and processes to ensure that everyone involved understands what is expected for software process and product quality. | managers | quality | S-01 page 251 | C-48 |
| R-0310 | The software organization must commit to quality by establishing its quality management system, including policies, objectives and procedures. | managers | quality | S-01 page 252 | C-48 |
| R-0311 | Responsibility and authority for implementing the QMS must be assigned and be independent of current project management teams. | managers | quality | S-01 page 252 | C-48 |
| R-0312 | Software engineers should promote the use of formally approved processes and procedures that implement the quality policy. | software engineers | quality | S-01 page 252 | C-48 |
| R-0313 | Processes for a QMS used in improvement should be documented with the user in mind and identify where quality controls are to be verified. | quality assurance staff | quality | S-01 page 252 to 253 | C-42 |
| R-0314 | Software engineers should establish a meaningful defect classification taxonomy to describe and categorize anomalies. | software engineers | quality | S-01 page 254 | C-43 |
| R-0315 | It is important that corrective actions be documented and submitted when quality management objectives are not met. | quality assurance staff | quality | S-01 page 254 | C-43 |
| R-0316 | Project participants must have a way of reporting software engineering process and tool problems to an independent organization. | project maintainers | quality | S-01 page 254 | C-52 |
| R-0317 | The SQA activities should be conducted early in a software project life cycle to ensure quality. | quality assurance staff | quality | S-01 page 255 | C-42 |
| R-0318 | The SQA plan should not conflict with the software configuration management plan or any other relevant project planning artifact. | operations engineers | operations | S-01 page 255 | C-35 |
| R-0319 | The SQA activities and the SCM activities should be considered complementary activities. | operations engineers | operations | S-01 page 255 | C-35 |
| R-0320 | Software engineers should be aware of the need to plan and execute SQA activities at certain project milestones and keep records of their execution. | software engineers | quality | S-01 page 255 to 256 | C-42 |
| R-0321 | Software engineers should identify which work products and software artifacts require configuration management. | software engineers | operations | S-01 page 256 | C-35 |
| R-0322 | Software engineers should be familiar with source code versioning processes. | software engineers | security | S-01 page 256 | C-01 |
| R-0323 | Software engineers should know how to operate the version control tool kit. | software engineers | security | S-01 page 256 | C-01 |
| R-0324 | Software engineers are responsible for eliciting quality requirements that might not be explicit at the outset. | software engineers | quality | S-01 page 256 | C-41 |
| R-0325 | Software engineers should understand how to define quality requirements and quality targets so that they can be measured at the acceptance stage. | software engineers | quality | S-01 page 256 | C-41 |
| R-0326 | During project planning software engineers must keep quality requirements in mind and must anticipate potential additional development costs if safety, security and dependability are important. | software engineers | quality | S-01 page 256 | C-41 |
| R-0327 | Software engineers should know the software characteristics that can be planned, implemented and measured during software construction. | software engineers | quality | S-01 page 256 | C-41 |
| R-0328 | Software engineers should know that certain quality characteristics have conflicting impacts. | software engineers | quality | S-01 page 256 | C-41 |
| R-0329 | The software engineer must determine the real purpose of the software to be designed and constructed. | software engineers | quality | S-01 page 256 | C-46 |
| R-0330 | Sound engineering practice requires that intermediate work products relevant to quality be evaluated using work product reviews and inspections throughout the software engineering process. | quality assurance staff | quality | S-01 page 257 | C-42 |
| R-0331 | The verification process and the validation process should begin early in development or maintenance. | quality assurance staff | quality | S-01 page 257 | C-42 |
| R-0332 | Software engineers should choose and apply the proper V&V task depending on the software integrity level. | software engineers | quality | S-01 page 257 | C-38 |
| R-0333 | Software engineers should identify the product integrity level and ensure the minimum V&V tasks are assigned (the sentence continues on page 258). | software engineers | quality | S-01 page 257 to 258 | C-38 |
| R-0334 | Software engineers should plan the testing activities, including levels, techniques, measures and tools. | software engineers | quality | S-01 page 258 | C-38 |
| R-0335 | IEEE 730:2014 recommends that testing completion criteria be set. | software engineers | quality | S-01 page 258 | C-38 |
| R-0336 | A software quality engineering team, for critical systems, should be particularly involved in qualifying software products prior to delivery. | quality assurance staff | quality | S-01 page 258 | C-42 |
| R-0337 | Reviews should be part of the software engineering culture and should be planned, executed and documented during the software life cycle. | quality assurance staff | quality | S-01 page 259 | C-42 |
| R-0338 | Technical reviews and audits should be planned, approved and conducted. | quality assurance staff | quality | S-01 page 259 | C-42 |
| R-0339 | Software engineers should define the security properties of their software and maintain them throughout the software development life cycle. | software engineers | security | S-01 page 264 | C-13 |
| R-0340 | Security must be considered during software maintenance, because security faults can be introduced during maintenance. | operations engineers | operations | S-01 page 264 | C-36 |
| R-0341 | Software engineers should consider the mitigation of security threats as part of software development. | software engineers | security | S-01 page 265 | C-13 |
| R-0342 | Project managers need to raise software security from a stand-alone technical concern to an enterprise issue. | project maintainers | security | S-01 page 265 | C-19 |
| R-0343 | Organizations should use an information security management system to conduct risk assessments continually and to deploy an IT team that monitors the risks. | managers | quality | S-01 page 266 | C-48 |
| R-0344 | Agile teams need to understand and adopt security practices and take more responsibility for the security of their systems. | software engineers | security | S-01 page 266 | C-19 |
| R-0345 | Security professionals must learn to accept change, work faster and more iteratively, and manage security risks in incremental terms. | security engineers | quality | S-01 page 266 | C-49 |
| R-0346 | Security needs to become an enabler instead of a blocker. | software engineers | quality | S-01 page 266 | C-49 |
| R-0347 | Security must be built into software engineering to ensure software security. | security engineers | security | S-01 page 266 | C-13 |
| R-0348 | Software design should keep modules that need extra privileges as small as possible, and each module should perform only the tasks that need those privileges. | security engineers | security | S-01 page 267 | C-02 |
| R-0349 | Assumptions in a program should be validated, or documented for installers and maintainers when validation is not possible. | project maintainers | quality | S-01 page 267 | C-45 |
| R-0350 | A program should not share memory objects with any other program. | software engineers | quality | S-01 page 267 | C-47 |
| R-0351 | Every function error status should be checked, and the program should restore the earlier state and then terminate unless recovery has no security effect. | software engineers | quality | S-01 page 267 | C-40 |
| R-0352 | The source lists the practice of validating input, as one of the CERT/CC top 10 software security practices. | security engineers | security | S-01 page 268 | C-15 |
| R-0353 | The source lists the practice of heeding compiler warnings, as one of the CERT/CC top 10 software security practices. | software engineers | quality | S-01 page 268 | C-40 |
| R-0354 | The source lists the practice of architecting and designing for security policies, as one of the CERT/CC top 10 software security practices. | security engineers | security | S-01 page 268 | C-13 |
| R-0355 | The source lists the practice of keeping the design simple, as one of the CERT/CC top 10 software security practices. | software engineers | quality | S-01 page 268 | C-47 |
| R-0356 | The source lists the practice of default deny, as one of the CERT/CC top 10 software security practices. | security engineers | security | S-01 page 268 | C-18 |
| R-0357 | The source lists the practice of adhering to the principle of least privilege, as one of the CERT/CC top 10 software security practices. | security engineers | security | S-01 page 268 | C-02 |
| R-0358 | The source lists the practice of sanitizing data sent to other software, as one of the CERT/CC top 10 software security practices. | security engineers | security | S-01 page 268 | C-15 |
| R-0359 | The source lists the practice of defense in depth, as one of the CERT/CC top 10 software security practices. | security engineers | security | S-01 page 268 | C-13 |
| R-0360 | The source lists the practice of effective quality assurance techniques, as one of the CERT/CC top 10 software security practices. | quality assurance staff | quality | S-01 page 268 | C-42 |
| R-0361 | The source lists the practice of adopting a software construction security standard, as one of the CERT/CC top 10 software security practices. | software engineers | quality | S-01 page 268 | C-40 |
| R-0362 | Security experts skilled in the application domain should be engaged to perform dynamic security tests. | security engineers | security | S-01 page 268 | C-14 |
| R-0363 | Security tests should always be conducted within legal boundaries and with proper authorization. | security engineers | security | S-01 page 268 | C-14 |
| R-0364 | Security professionals are required to operate and configure security analysis tools properly and to verify their results. | security engineers | security | S-01 page 268 | C-14 |
| R-0365 | Comprehensive risk and threat analysis methods, and management tools for IoT platforms, are required. | security engineers | security | S-01 page 269 | C-13 |
| R-0366 | Software engineers must handle unique engineering problems to produce software with known characteristics and reliability. | software engineers | quality | S-01 page 274 | C-49 |
| R-0367 | A software engineer maintains professional practice by performing all work according to generally accepted practices, standards and guidelines of the applicable professional society. | software engineers | quality | S-01 page 274 | C-49 |
| R-0368 | It is crucial that engineers adhere to standards and generally accepted practices to protect against allegations of malpractice, negligence or incompetence. | software engineers | quality | S-01 page 280 | C-49 |
| R-0369 | All software professionals must be aware of legal restrictions on import, export and re-export of software, services and technology in the jurisdictions where they work. | software engineers | quality | S-01 page 280 | C-49 |
| R-0370 | Trade experts should be consulted for detailed compliance guidance. | software engineers | quality | S-01 page 280 | C-49 |
| R-0371 | Software engineers have a professional obligation to consider the threat of cybercrime and how the system security protects software and user information from accidental or malicious access, use, modification, destruction or disclosure. | software engineers | quality | S-01 page 280 to 281 | C-49 |
| R-0372 | Software engineers should avoid certifying or approving unacceptable products, disclosing confidential information, and falsifying facts or data. | software engineers | quality | S-01 page 281 | C-49 |
| R-0373 | Software engineers and their managers should provide documentation for other units of the software development organization, covering requirements, design, tools, test specifications and results, methods, and problems met during development. | managers | quality | S-01 page 281 | C-45 |
| R-0374 | Software documentation for external stakeholders should provide the information needed to decide whether the software is likely to meet customer and user needs. | software engineers | quality | S-01 page 281 | C-45 |
| R-0375 | Software documentation for external stakeholders should describe the safe and unsafe use of the software. | software engineers | quality | S-01 page 281 | C-45 |
| R-0376 | Software documentation for external stakeholders should explain how to protect sensitive information that the software creates or stores. | software engineers | quality | S-01 page 281 | C-45 |
| R-0377 | Software documentation for external stakeholders should clearly identify warnings and critical procedures. | software engineers | quality | S-01 page 281 | C-45 |
| R-0378 | If the customer acquires the source code or the right to modify it, the software engineer should provide documentation of the functional specifications, design, test suite and operating environment. | consumers | quality | S-01 page 281 to 282 | C-45 |
| R-0379 | Documents should be kept for at least as long as the software product life cycle or the time that organizational or regulatory requirements need. | software engineers | quality | S-01 page 282 | C-45 |
| R-0380 | A software engineer must conduct a trade-off analysis ethically, objectively and impartially when selecting criteria and assigning weights. | software engineers | quality | S-01 page 282 | C-49 |
| R-0381 | Any conflict of interest must be disclosed upfront in a trade-off analysis. | software engineers | quality | S-01 page 282 | C-49 |
| R-0382 | Stakeholders should provide support, information and feedback at all stages of the software life cycle. | managers | quality | S-01 page 283 | C-48 |
| R-0383 | In all cases, written software engineering products must be accessible, understandable and relevant to their intended audience. | software engineers | quality | S-01 page 285 | C-45 |
| R-0384 | Ensure realistic quantitative estimates of cost, scheduling, personnel, quality and outcomes, and provide an uncertainty assessment of these estimates | software engineers | quality | S-01 page 301 | C-48 |
| R-0385 | If the estimates of the smallest pieces lack allowances for significant cross-cutting factors, find a way to address those factors | managers | quality | S-01 page 302 | C-48 |
| R-0386 | Reducing rework involves proactive quality improvement: identify defects earlier, control defect cost growth, and prevent defects by using templates and checklists | quality assurance staff | quality | S-01 page 305 | C-43 |
| R-0387 | An SPLC should include risk management and synchronization with different suppliers, and should provide auditable decision-making information for compliance needs | managers | quality | S-01 page 306 | C-48 |
| R-0388 | Software engineering economics should be concerned with all SPLC activities, including those after the initial release | managers | quality | S-01 page 306 | C-48 |
| R-0389 | Indicators must be normalized and standardized to operate correctly | managers | quality | S-01 page 298 | C-48 |
| R-0390 | The problem has to be analyzed in detail for security, vulnerability, durability and upgradability requirements | software engineers | quality | S-01 page 313 | C-46 |
| R-0391 | Ideally, systems should be highly cohesive, so that each subsystem performs one specific task | software engineers | quality | S-01 page 313 | C-47 |
| R-0392 | Ideally, systems should be loosely coupled, so that each subsystem functions independently as far as possible | software engineers | quality | S-01 page 313 | C-47 |
| R-0393 | The hardware must be designed to support the software subsystems and satisfy all user requirements, especially user interfaces and performance | software engineers | quality | S-01 page 314 | C-47 |
| R-0394 | Contingencies should be built in for the computing resources required | software engineers | quality | S-01 page 314 | C-47 |
| R-0395 | Software engineers are expected to understand the interface of I/O devices with the system, and the device drivers used by applications | software engineers | quality | S-01 page 317 | C-49 |
| R-0396 | Algorithm logic has to be designed or chosen with consideration for system performance, security, portability, maintainability, scalability and simplicity | software engineers | quality | S-01 page 318 | C-47 |
| R-0397 | The software engineer must consider the purpose of the application and its performance requirements when selecting an algorithm | software engineers | quality | S-01 page 319 | C-47 |
| R-0398 | Learning the computation of asymptotic notations for different input sets is important | software engineers | quality | S-01 page 319 | C-49 |
| R-0399 | Software engineers are expected to know how high-level languages are translated, and the compilers, linkers, loaders and debuggers involved | software engineers | quality | S-01 page 322 | C-49 |
| R-0400 | Programs must be thoroughly tested for valid, invalid and boundary-value inputs and conditions to find errors | software engineers | quality | S-01 page 324 | C-38 |
| R-0401 | Logical errors must be traced and resolved with various data for each functionality | quality assurance staff | quality | S-01 page 324 | C-43 |
| R-0402 | Programs are expected to function properly and generate the expected output | software engineers | quality | S-01 page 324 | C-37 |
| R-0403 | Choose coding standards and guidelines that suit the application or system, as a practice to help adoption | managers | quality | S-01 page 325 | C-40 |
| R-0404 | Consider open standards created by community participation, and closed standards created by working groups, as a practice | managers | quality | S-01 page 325 | C-40 |
| R-0405 | Educate programmers to follow the adopted standards and guidelines, as a practice | managers | quality | S-01 page 326 | C-49 |
| R-0406 | Use tools and periodic reviews to ensure that adopted standards and guidelines are followed, as a practice | managers | quality | S-01 page 326 | C-40 |
| R-0407 | Review and revise standards and guidelines from time to time, learning from project execution, as a practice | managers | quality | S-01 page 326 | C-40 |
| R-0408 | Software engineers need to understand file system protection and security, and access control concepts | software engineers | quality | S-01 page 327 | C-49 |
| R-0409 | Engineers should be familiar with access control lists, access matrices, access control verification and authentication schemes | software engineers | quality | S-01 page 327 | C-49 |
| R-0410 | Software engineers should understand hardware security, external and operational security, password protection, access control, security kernels and the layered approach | software engineers | quality | S-01 page 328 | C-49 |
| R-0411 | Database updates for transactions must be carried out carefully, with commits at checkpoints, and must use undo, deferred update, immediate update, buffering or shadow paging | software engineers | quality | S-01 page 331 | C-47 |
| R-0412 | Databases must be backed up periodically to ensure data safety | operations engineers | operations | S-01 page 331 | C-30 |
| R-0413 | It is crucial to prevent data corruption, to recognize it immediately, and to recover the data | operations engineers | operations | S-01 page 331 | C-30 |
| R-0414 | The fundamental design goals of a network should include reliability, security, availability and manageability | software engineers | quality | S-01 page 333 | C-47 |
| R-0415 | Engineers should expect threats and intrusions at several levels, and design security at several levels | software engineers | security | S-01 page 333 | C-13 |
| R-0416 | Systems must be set up to monitor networks for proper and improper functioning, and to identify and fix faults, vulnerabilities and hacks quickly | operations engineers | operations | S-01 page 333 | C-28 |
| R-0417 | Engineers must understand and learn how to design a network with firewalls, VLANs, subnets, QoS, DMZ and access points | software engineers | quality | S-01 page 333 | C-49 |
| R-0418 | One has to be constantly vigilant for attacks and continuously upgrade systems, devices and tools | security engineers | security | S-01 page 333, continued on page 334 | C-16 |
| R-0419 | Many precautionary measures must be implemented and strictly followed to reduce wireless and mobile risks, such as changing default passwords, restricting access, encrypting data and installing firewalls | security engineers | security | S-01 page 335 | C-18 |
| R-0420 | Users must protect and hide the SSID, use effective antivirus software and keep it updated, use VPNs with care, and disable access after use | consumers | quality | S-01 page 335 | C-49 |
| R-0421 | Update access points, access controllers, gateways and other devices with security patches when they become available | security engineers | security | S-01 page 335 | C-16 |
| R-0422 | The system should allow users to interrupt processing and undo operations where possible | consumers | quality | S-01 page 335 | C-47 |
| R-0423 | The system should be able to regain its original state if there are errors | software engineers | quality | S-01 page 335 | C-47 |
| R-0424 | The software engineer needs to identify the user profile, system functions, input and output interfaces, fault tolerance and performance parameters | software engineers | quality | S-01 page 335 | C-46 |
| R-0425 | The user interface devices must be robust | software engineers | quality | S-01 page 335 | C-47 |
| R-0426 | Users expect software to be robust, secure, and to give fast and consistent responses | consumers | quality | S-01 page 335 | C-41 |
| R-0427 | Meaningful and comprehensive documentation is crucial at all stages of the software lifecycle | software engineers | quality | S-01 page 335 | C-45 |
| R-0428 | Define and adopt an apt coding standard for the project, and ensure that every team member implements it in spirit | project maintainers | quality | S-01 page 335 | C-40 |
| R-0429 | Code has to be written with more care, because other software engineers maintain it | software engineers | quality | S-01 page 335 | C-40 |
| R-0430 | Code has to be legible and easy to comprehend | software engineers | quality | S-01 page 335 | C-40 |
| R-0431 | Meaningful, consistent and detailed comments are essential for code readability | software engineers | quality | S-01 page 335 | C-40 |
| R-0432 | Software engineers should be aware of the limitations and challenges inherent to AI and ML, including uncertain and stochastic behaviour and the need for sufficiently labeled and structured datasets. | software engineers | quality | S-01 page 338 | C-49 |
| R-0433 | Software engineers working on AI are expected to know various other learning techniques and the key differences between the methods and their applications. | software engineers | quality | S-01 page 337 | C-49 |
| R-0434 | Software engineers are encouraged to learn other reasoning methods, such as metalevel, procedural numeric and formal reasoning. | software engineers | quality | S-01 page 337 | C-49 |
| R-0435 | Software engineers are encouraged to learn other AI models, such as Linear Discriminant Analysis, Learning Vector Quantization and K-nearest Neighbors. | software engineers | quality | S-01 page 338 | C-49 |
| R-0436 | There is a need for particular support of SE for AI, such as interdisciplinary collaborative teams of data scientists and software engineers. | software engineers | quality | S-01 page 338 | C-48 |
| R-0437 | Engineering decisions must consider various factors, for example financial criteria. | managers | quality | S-01 page 367 | C-48 |
| R-0438 | Be sure to identify all relevant selection criteria. | managers | quality | S-01 page 367 | C-48 |
| R-0439 | Consider multiple technically feasible solutions so that the optimal solution is among those considered. | managers | quality | S-01 page 367 | C-48 |
| R-0440 | Monitor the performance of the selected solution. | operations engineers | operations | S-01 page 367 to 368 | C-28 |
| R-0441 | It is essential to evaluate the real-world performance of the selected alternative and, if necessary and possible, decide whether another alternative might be better. | managers | quality | S-01 page 368 | C-52 |
| R-0442 | Engineers must understand how to create an experiment and analyse the results to evaluate proposed solutions or models. | software engineers | quality | S-01 page 370 | C-52 |
| R-0443 | Engineers need to understand how to formulate clear hypotheses. | software engineers | quality | S-01 page 371 | C-52 |
| R-0444 | Engineers must understand how product and process characteristics vary. | software engineers | quality | S-01 page 371 | C-52 |
| R-0445 | Engineers must understand statistical techniques for collecting and interpreting reliable data so that results can be generalised. | software engineers | quality | S-01 page 371 | C-52 |
| R-0446 | Researchers must base observations on units of analysis that are clearly identified and appropriate for the analysis. | software engineers | quality | S-01 page 371 | C-52 |
| R-0447 | Care must be taken to differentiate the study population and the target population. | managers | quality | S-01 page 372 | C-52 |
| R-0448 | The samples must be drawn so that draws are independent, and the sampling rules must be predefined. | managers | quality | S-01 page 372 | C-52 |
| R-0449 | Before a simulation can be run, the initial values of all state variables must be provided. | software engineers | quality | S-01 page 375 | C-47 |
| R-0450 | Prototype construction must have a clear purpose and must be planned, monitored and controlled. | managers | quality | S-01 page 375 | C-48 |
| R-0451 | Everyone involved in an engineering project must understand the measurement methods, the measurement results and how those results can and should be used. | project maintainers | quality | S-01 page 376 | C-52 |
| R-0452 | Engineers must appreciate the need to define measurements from an operational perspective. | software engineers | quality | S-01 page 376 | C-52 |
| R-0453 | The measurement method must be well defined, because vagueness in the method leads to ambiguity in the results. | managers | quality | S-01 page 376 | C-52 |
| R-0454 | Nonnumerical symbols are preferred for ordinal scales such as the CMMI staged maturity levels. | security engineers | security | S-01 page 377 | C-22 |
| R-0455 | Software engineers need to understand measurement theory and be on the lookout for inappropriate manipulations in code reviews. | software engineers | quality | S-01 page 379 | C-52 |
| R-0456 | Future programming languages should enforce measurement theory and not allow developers to manipulate measurements inappropriately. | software engineers | quality | S-01 page 379 | C-52 |
| R-0457 | A measurement should be made to support decision-making. | managers | quality | S-01 page 381 | C-52 |
| R-0458 | Some decision should be made as a result of the measurement. | managers | quality | S-01 page 381 | C-52 |
| R-0459 | Measurements that support no decision should be avoided. | managers | quality | S-01 page 381 | C-52 |
| R-0460 | Engineers are expected to be familiar with and use the appropriate standards for their discipline. | software engineers | quality | S-01 page 381 | C-49 |
| R-0461 | Standards provide requirements, specifications or guidelines that engineers must observe so that products, processes and materials are of acceptable quality. | software engineers | quality | S-01 page 381 | C-49 |
| R-0462 | For a standard to be useful, conformance must add real or perceived value to the product, process or effort. | managers | quality | S-01 page 381 | C-48 |
| R-0463 | Engineers must be aware of existing standards and keep abreast of changes to them over time. | software engineers | quality | S-01 page 382 | C-49 |
| R-0464 | Engineers must review all current standards related to a given endeavour and determine which must be met. | software engineers | quality | S-01 page 382 | C-49 |
| R-0465 | The design must incorporate all constraints imposed by the applicable standard. | software engineers | quality | S-01 page 382 | C-47 |
| R-0466 | Cause maps require evidence of the occurrence of causes and of the causality of effects. | quality assurance staff | quality | S-01 page 382 to 383 | C-43 |
| R-0467 | More than one candidate corrective action should be considered. | quality assurance staff | quality | S-01 page 383 | C-43 |
| R-0468 | Potential corrective actions should eliminate the cause, reduce the probability of the cause occurring, or disconnect the cause from the effect. | quality assurance staff | quality | S-01 page 383 | C-43 |
| R-0469 | Selected corrective actions should prevent recurrence, be within the organisation's ability to control, meet goals, and not cause other problems. | quality assurance staff | quality | S-01 page 383 | C-43 |
| R-0470 | Selected corrective actions should generate the greatest amount of control for the least cost. | quality assurance staff | quality | S-01 page 383 | C-43 |
| R-0471 | Observe the selected corrective actions to ensure efficiency and effectiveness. | quality assurance staff | quality | S-01 page 383 | C-43 |
| R-0472 | Measurement, quality and security must be incorporated into the proposed breakdown of topics of each KA. | managers | quality | S-01 page 388 | C-48 |
| R-0473 | The breakdown of topics within a KA must not presume specific software life cycle models, software technologies or software development methods. | managers | quality | S-01 page 388 | C-48 |
| R-0474 | Change requests to the baseline must be approved both by the SWEBOK Guide editors and by the KA editors team. | software engineers | operations | S-01 page 388 | C-35 |
| R-0475 | When software is the predominant system or element of interest, ISO/IEC/IEEE 12207 should be used. | managers | quality | S-01 page 396 | C-48 |
| R-0476 | Producer must select a build platform that can reach the desired SLSA Build Level. | project maintainers | security | S-02 build-requirements, Producer > Choose an appropriate build platform | C-05 |
| R-0477 | Producer must build artifacts consistently so verifiers can form expectations, and keep any required ecosystem configuration file complete and current. | project maintainers | security | S-02 build-requirements, Producer > Follow a consistent build process | C-17 |
| R-0478 | Producer must distribute provenance to consumers, or delegate this to an ecosystem that can distribute it. | project maintainers | security | S-02 build-requirements, Producer > Distribute provenance | C-06 |
| R-0479 | Producers must publish attestations in at least one place and should use more than one. | project maintainers | security | S-02 distributing-provenance, Where attestations are published | C-06 |
| R-0480 | Producers should include provenance in source repository releases. | project maintainers | security | S-02 distributing-provenance, Where attestations are published | C-06 |
| R-0481 | Attestations should be bound to artifacts, not releases. | build platform operators | security | S-02 distributing-provenance, Releases and attestations | C-06 |
| R-0482 | Ecosystems should support multiple attestations per release. | build platform operators | security | S-02 distributing-provenance, Releases and attestations | C-06 |
| R-0483 | Ecosystems should support a one-to-many relationship from artifacts to attestations. | build platform operators | security | S-02 distributing-provenance, Artifacts and attestations | C-06 |
| R-0484 | Provenance should accompany the artifact at publish time. | build platform operators | security | S-02 distributing-provenance, Artifacts and attestations | C-06 |
| R-0485 | Ecosystems should provide a way to map each artifact to its attestations, implicitly or explicitly. | build platform operators | security | S-02 distributing-provenance, Artifacts and attestations | C-06 |
| R-0486 | The provenance filename should relate directly to the artifact filename. | build platform operators | security | S-02 distributing-provenance, Artifacts and attestations | C-06 |
| R-0487 | A hash and index pointer should be published to a third-party transparency log. | consumers | security | S-02 distributing-provenance, Where attestations are published | C-06 |
| R-0488 | Registries should support uploading and distributing provenance alongside artifacts. | build platform operators | security | S-02 distributing-provenance, Where attestations are published | C-06 |
| R-0489 | Attestations should be immutable and must not be overwritten; a new release and new artifacts should be created instead. | build platform operators | security | S-02 distributing-provenance, Immutability | C-06 |
| R-0490 | The format should be in-toto SLSA Build Provenance; another format may be used if producer and consumer agree and it meets all other requirements. | consumers | security | S-02 distributing-provenance, Format | 5 |
| R-0491 | Intermediaries that distribute source archives should provide build provenance for those packages. | build platform operators | security | S-02 distributing-provenance, Source-based ecosystems | C-06 |
| R-0492 | Build platform must generate provenance that identifies the output by cryptographic digest and describes how it was produced, in an ecosystem-acceptable format. | build platform operators | security | S-02 build-requirements, Provenance generation, Provenance Exists (L1) | C-06 |
| R-0493 | Build platform should make provenance completeness best effort. | build platform operators | security | S-02 build-requirements, Provenance generation, Provenance Exists (L1) | C-06 |
| R-0494 | Build platform must make provenance authenticatable so that consumers can validate it. | build platform operators | security | S-02 build-requirements, Provenance generation, Provenance is Authentic (L2) | C-06 |
| R-0495 | Build platform should sign provenance with a key that only the generating component can access. | build platform operators | security | S-02 build-requirements, Provenance generation, Provenance is Authentic (L2) | C-06 |
| R-0496 | Provenance must come from the control plane, not from a tenant. | build platform operators | security | S-02 build-requirements, Provenance generation, Provenance is Authentic (L2) | C-07 |
| R-0497 | Provenance must be strongly resistant to forgery by tenants. | build platform operators | security | S-02 build-requirements, Provenance generation, Provenance is Unforgeable (L3) | C-07 |
| R-0498 | Signing secrets must stay out of user build steps. | build platform operators | security | S-02 build-requirements, Provenance generation, Provenance is Unforgeable (L3) | C-07 |
| R-0499 | The control plane must generate or verify every provenance field. | build platform operators | security | S-02 build-requirements, Provenance generation, Provenance is Unforgeable (L3) | C-07 |
| R-0500 | External parameters must be fully enumerated. | build platform operators | security | S-02 build-requirements, Provenance generation, Provenance is Unforgeable (L3) | C-06 |
| R-0501 | The signing key and secrets must be stored in a secure management system that only the build service account can access. | build platform operators | security | S-02 build-requirements, Provenance generation, notes | C-07 |
| R-0502 | All build steps must run on a hosted platform, not on an individual workstation. | build platform operators | security | S-02 build-requirements, Isolation strength: Hosted (L2, L3) | C-05 |
| R-0503 | Build environments must be isolated, ephemeral and free of unintended external influence, even within the same tenant project. | build platform operators | security | S-02 build-requirements, Isolation strength: Isolated (L3) | C-07 |
| R-0504 | Builds must not be able to access platform secrets, such as the provenance signing key. | build platform operators | security | S-02 build-requirements, Isolation strength: Isolated (L3) | C-07 |
| R-0505 | Overlapping builds must not be able to influence each other. | build platform operators | security | S-02 build-requirements, Isolation strength: Isolated (L3) | C-07 |
| R-0506 | One build must not persist into, or influence, the environment of a later build. | build platform operators | security | S-02 build-requirements, Isolation strength: Isolated (L3) | C-07 |
| R-0507 | Cache poisoning must be prevented, so that output is identical with or without the cache. | build platform operators | security | S-02 build-requirements, Isolation strength: Isolated (L3) | C-07 |
| R-0508 | No service must allow remote influence unless it is captured as externalParameters. | build platform operators | security | S-02 build-requirements, Isolation strength: Isolated (L3) | C-07 |
| R-0509 | The build platform must use industry security best practices, including access controls, secure communications, cryptographic secret management, frequent updates and prompt patching. | build platform operators | security | S-02 build-requirements, Build Platform: Security (all conformant levels) | C-16 |
| R-0510 | buildDefinition is required for Build L1. | consumers | security | S-02 build-provenance, Top-level predicate | 5 |
| R-0511 | runDetails is required for Build L1. | consumers | security | S-02 build-provenance, Top-level predicate | 5 |
| R-0512 | Consumers must ignore unrecognized fields unless otherwise noted. | consumers | security | S-02 build-provenance, Parsing rules | 5 |
| R-0513 | Unset, null and empty values must be treated as equivalent. | consumers | security | S-02 build-provenance, Parsing rules | 5 |
| R-0514 | buildType is required for Build L1 and should resolve to a human-readable specification. | consumers | security | S-02 build-provenance, BuildDefinition | 5 |
| R-0515 | externalParameters is required for Build L1, must be complete at Build L3, and should be kept minimal. | build platform operators | security | S-02 build-provenance, BuildDefinition | 5 |
| R-0516 | Verifiers should reject unrecognized or unexpected fields in externalParameters. | consumers | security | S-02 build-provenance, BuildDefinition | 5 |
| R-0517 | externalParameters must be included in the provenance and must be verified downstream. | build platform operators | security | S-02 build-provenance, Build model and other requirements | 5 |
| R-0518 | Build platforms should minimize externalParameters to ease verification. | build platform operators | security | S-02 build-provenance, Build model and other requirements | 5 |
| R-0519 | internalParameters is optional and may aid reproduction, debugging or incident response. | build platform operators | security | S-02 build-provenance, BuildDefinition | 5 |
| R-0520 | resolvedDependencies should be listed, and completeness is best effort through L3. | consumers | security | S-02 build-provenance, BuildDefinition | 5 |
| R-0521 | The same field name should not appear in both parameter objects. | project maintainers | security | S-02 build-provenance, BuildDefinition | 5 |
| R-0522 | Build platform communication with its control plane or caches should not influence the build definition; if it does, it should be recorded in resolvedDependencies. | build platform operators | security | S-02 build-provenance, Build model and other requirements | C-07 |
| R-0523 | The build platform should have a security model that defines its trust boundaries. | build platform operators | security | S-02 build-provenance, Build model and other requirements | C-16 |
| R-0524 | builder is required for Build L1. | consumers | security | S-02 build-provenance, RunDetails | 5 |
| R-0525 | builder.id is required for Build L1, should resolve to documentation of scope, claimed level, guarantees and unverified fields. | build platform operators | security | S-02 build-provenance, Builder | 5 |
| R-0526 | Different operating modes must have different builder.id values and should have different signer identities. | build platform operators | security | S-02 build-provenance, Builder | 5 |
| R-0527 | Consumers must accept only specific signer-builder pairs. | consumers | security | S-02 build-provenance, Builder | C-17 |
| R-0528 | byproducts should not include all intermediate files. | build platform operators | security | S-02 build-provenance, RunDetails | 5 |
| R-0529 | invocationId should be globally unique. | build platform operators | security | S-02 build-provenance, BuildMetadata | 5 |
| R-0530 | Extension field names should use the form vendor_fieldname. | project maintainers | security | S-02 build-provenance, Extension fields | 5 |
| R-0531 | Extensions must not change the meaning of other fields. | project maintainers | security | S-02 build-provenance, Extension fields | 5 |
| R-0532 | Extensions should follow the monotonic principle, so that ignoring them never turns a DENY into an ALLOW. | consumers | security | S-02 build-provenance, Extension fields | 5 |
| R-0533 | Verification should include the builder identity check, the envelope signature check, and the buildType and externalParameters check. | consumers | security | S-02 verifying-artifacts, verification steps | C-17 |
| R-0534 | Verifiers should verify provenance against the roots of trust, the subject digest and the predicateType. | consumers | security | S-02 verifying-artifacts, verification steps | C-17 |
| R-0535 | Any unrecognized externalParameters should cause verification to fail. | consumers | security | S-02 verifying-artifacts, verification steps | C-17 |
| R-0536 | Verifiers should perform equivalent checks if provenance is not in the recommended format. | consumers | security | S-02 verifying-artifacts, verification steps | C-17 |
| R-0537 | Verifiers should carefully choose which build platforms enter the roots of trust. | consumers | security | S-02 verifying-artifacts, roots of trust | C-20 |
| R-0538 | Verifiers should compare provenance against expected values for builder identity, source repository, buildType and externalParameters. | consumers | security | S-02 verifying-artifacts, verification steps | C-17 |
| R-0539 | Expectations should be sufficient to detect or prevent unofficial injected behavior. | consumers | security | S-02 verifying-artifacts, verification steps | C-17 |
| R-0540 | Verification tools should reject unrecognized fields. | software engineers | security | S-02 verifying-artifacts, verification steps | C-17 |
| R-0541 | At least one verification architecture (ecosystem, consumer or monitor) should be used. | consumers | security | S-02 verifying-artifacts, verification architectures | C-17 |
| R-0542 | Verification at upload time is recommended whenever possible. | build platform operators | security | S-02 verifying-artifacts, ecosystem architecture | C-17 |
| R-0543 | The verifier should provide an authenticated mechanism for producers to set expectations. | build platform operators | security | S-02 verifying-artifacts, producer model | C-17 |
| R-0544 | There should be some protection against unilateral modification of expectations by an adversary. | build platform operators | security | S-02 verifying-artifacts, producer model | C-17 |
| R-0545 | A monitor should publish its expectations for all packages it verifies. | consumers | security | S-02 verifying-artifacts, monitor architecture | C-17 |
| R-0546 | Consumers should consider at least five build-model elements: external parameters, control plane, build environments, caches and output storage. | consumers | security | S-02 assessing-build-platforms, Assessment prompts | C-20 |
| R-0547 | The assessment should account for the security model behind the builder.id transitive closure, including platform boundaries, actors and interfaces. | consumers | security | S-02 assessing-build-platforms, Assessment prompts | C-20 |
| R-0548 | Consumers should evaluate platform defenses against three adversary profiles: project contributors, project maintainers and build platform administrators. | consumers | security | S-02 assessing-build-platforms, Adversary profiles | C-20 |
| R-0549 | Build environments must be isolated from the control plane and from each other, including builds from the same tenant or project. | build platform operators | security | S-02 assessing-build-platforms, Build environments | C-07 |
| R-0550 | Build environments must have a means to fetch input artifacts. | build platform operators | security | S-02 assessing-build-platforms, Build environments | C-07 |
| R-0551 | Self-attestation evidence should be published online. | managers | security | S-02 assessing-build-platforms, Self-attestation | C-22 |
| R-0552 | The organization MUST select a source control system able to reach its target Source Level. | managers | security | S-02 draft/source-requirements, Choose an appropriate SCS | C-01 |
| R-0553 | The organization MUST restrict sensitive operations using the identity management of the source control system. | managers | security | S-02 draft/source-requirements, Access control and history | C-02 |
| R-0554 | The source control system MUST keep a reliable change history. If it does not do so by design, the organization MUST provide evidence of continuous enforcement. | managers | security | S-02 draft/source-requirements, Access control and history | C-01 |
| R-0555 | If the source control system supports tags, it MUST be configured to block moving or deleting them. | build platform operators | security | S-02 draft/source-requirements, Access control and history | C-01 |
| R-0556 | The source control system MAY allow removal of content from a repository and its history. | build platform operators | security | S-02 draft/source-requirements, Safe Expunging Process | C-01 |
| R-0557 | The organization MUST allow such removal only to meet legal or privacy compliance requirements. | managers | security | S-02 draft/source-requirements, Safe Expunging Process | C-01 |
| R-0558 | The organization MUST document the removal process and how removal requests are tracked. | managers | security | S-02 draft/source-requirements, Safe Expunging Process | C-01 |
| R-0559 | The organization SHOULD log removals. | managers | operations | S-02 draft/source-requirements, Safe Expunging Process | C-28 |
| R-0560 | The source control system SHOULD require an Administrator plus at least one trusted person to trigger removals. | build platform operators | security | S-02 draft/source-requirements, Safe Expunging Process | C-08 |
| R-0561 | Removal logs and application records MAY be private. | project maintainers | operations | S-02 draft/source-requirements, Safe Expunging Process | C-28 |
| R-0562 | Organizations SHOULD make removal logs public where possible. | managers | operations | S-02 draft/source-requirements, Safe Expunging Process | C-28 |
| R-0563 | The organization MUST provide evidence that every enforced control runs continuously for every control claimed in provenance attestations or VSAs. | managers | quality | S-02 draft/source-requirements, Continuous technical controls (L3) | C-42 |
| R-0564 | The organization MUST document what each enforced control means. | managers | quality | S-02 draft/source-requirements, Continuous technical controls (L3) | C-45 |
| R-0565 | If the organization claims that all revisions on the main branch were tested before acceptance, the source control system MUST enforce that claim. | managers | quality | S-02 draft/source-requirements, Continuous technical controls (L3) | C-37 |
| R-0566 | The source control system MUST give each repository a unique, stable identifier. | build platform operators | security | S-02 draft/source-requirements, Identity and repositories (L1 to L4) | C-01 |
| R-0567 | The source control system MUST define revision IDs that are unique within a repository and immutable. | build platform operators | security | S-02 draft/source-requirements, Identity and repositories (L1 to L4) | C-01 |
| R-0568 | If revision IDs are not content digests, the source control system MUST document how immutability is established. | build platform operators | security | S-02 draft/source-requirements, Identity and repositories (L1 to L4) | C-10 |
| R-0569 | The source control system MUST provide tooling that shows changes between revisions in human-readable form. | project maintainers | security | S-02 draft/source-requirements, Identity and repositories (L1 to L4) | C-01 |
| R-0570 | The source control system SHOULD also provide interpretations of changes to non-plain-text files. | project maintainers | security | S-02 draft/source-requirements, Identity and repositories (L1 to L4) | C-01 |
| R-0571 | The source control system MUST generate a Source VSA for any revision at L1 or above. | build platform operators | security | S-02 draft/source-requirements, Source VSAs | C-06 |
| R-0572 | If an authorized consumer requests it, the source control system MUST let them fetch the matching Source VSA. | consumers | security | S-02 draft/source-requirements, Source VSAs | C-06 |
| R-0573 | At L1 and L2, the source control system MAY base VSAs on its own understanding of the system. | build platform operators | security | S-02 draft/source-requirements, Source VSAs | C-06 |
| R-0574 | At L2 and above, the source control system MUST use its own source provenance when it issues VSAs. | build platform operators | security | S-02 draft/source-requirements, Source VSA issuance | C-06 |
| R-0575 | The source control system MUST record every change to Named References, including when it occurred, who made it, and the new revision ID. | build platform operators | security | S-02 draft/source-requirements, History (L2) | C-01 |
| R-0576 | If revisions have ancestry, the source control system MUST allow a branch to move only to a descendant of its current revision. | build platform operators | security | S-02 draft/source-requirements, History (L2) | C-01 |
| R-0577 | The source control system MUST provide identity management or another way to identify and authenticate actors. | build platform operators | security | S-02 draft/source-requirements, Identity management (L2) | C-02 |
| R-0578 | The source control system MUST let organizations specify which actors and roles may perform sensitive actions. | managers | security | S-02 draft/source-requirements, Identity management (L2) | C-02 |
| R-0579 | The source control system MUST document how actors are identified for attribution. | build platform operators | security | S-02 draft/source-requirements, Identity management (L2) | C-01 |
| R-0580 | Activities SHOULD be attributed to authenticated identities. | project maintainers | security | S-02 draft/source-requirements, Identity management (L2) | C-01 |
| R-0581 | The source control system MUST document the format and intent of each provenance attestation it produces. | build platform operators | security | S-02 draft/source-requirements, Source provenance (L2) | C-06 |
| R-0582 | Provenance MUST be created at the same time the branch is updated. | build platform operators | security | S-02 draft/source-requirements, Source provenance (L2) | C-06 |
| R-0583 | Authorized consumers MUST be able to access the provenance for a revision. | consumers | security | S-02 draft/source-requirements, Source provenance (L2) | C-06 |
| R-0584 | For each control claimed in a VSA, continuity MUST be established and tracked from a start revision. | build platform operators | security | S-02 draft/source-requirements, Continuity (L3) | C-01 |
| R-0585 | A lapse in continuity MUST be re-established from a new revision. | managers | security | S-02 draft/source-requirements, Continuity (L3) | C-01 |
| R-0586 | Continuity exceptions are allowed only through the Safe Expunging Process. | managers | security | S-02 draft/source-requirements, Continuity (L3) | C-01 |
| R-0587 | The source control system MUST let organizations enforce custom technical controls on Named References. | managers | security | S-02 draft/source-requirements, Protected Named References (L3) | C-03 |
| R-0588 | The source control system MUST let organizations mark which references are protected. | managers | security | S-02 draft/source-requirements, Protected Named References (L3) | C-03 |
| R-0589 | The source control system MUST record enforced controls in attestations tied to the revision. | build platform operators | security | S-02 draft/source-requirements, Protected Named References (L3) | C-06 |
| R-0590 | The source control system MUST let organizations add their own properties to the Source VSA when those controls are enforced. | managers | security | S-02 draft/source-requirements, Protected Named References (L3) | 5 |
| R-0591 | The source control system MUST let organizations distribute extra control-related attestations to authorized consumers. | consumers | security | S-02 draft/source-requirements, Protected Named References (L3) | C-06 |
| R-0592 | The source control system MUST reject organization-specified property names that do not begin with ORG_SOURCE_. | build platform operators | security | S-02 draft/source-requirements, Protected Named References (L3) | 5 |
| R-0593 | Changes to protected branches MUST be agreed to by two or more trusted persons before submission. | software engineers | security | S-02 draft/source-requirements, Two-party review (L4) | C-03 |
| R-0594 | Either the uploader and a reviewer are different trusted persons, or two different reviewers are trusted persons. | software engineers | security | S-02 draft/source-requirements, Two-party review (L4) | C-03 |
| R-0595 | Reviews SHOULD cover at least the security-relevant properties of the code. | software engineers | security | S-02 draft/source-requirements, Two-party review (L4) | C-03 |
| R-0596 | The approval MUST apply to the final submitted revision, and later changes MUST also be reviewed. | project maintainers | security | S-02 draft/source-requirements, Two-party review (L4) | C-03 |
| R-0597 | Approvals are context-specific. Moving reviewed content to another context still requires review, except well-understood automatic merges. | project maintainers | security | S-02 draft/source-requirements, Two-party review (L4) | C-03 |
| R-0598 | The source control system MUST show reviewers a clear picture of what accepting the change will do. | build platform operators | security | S-02 draft/source-requirements, Two-party review (L4) | C-03 |
| R-0599 | The organization MAY grant a trusted robot a permanent exception to the review policy. | managers | security | S-02 draft/source-requirements, Two-party review (L4) | C-03 |
| R-0600 | The subject URI of a Source VSA SHOULD point to a human-readable page for the revision. | build platform operators | security | S-02 draft/source-requirements, Source VSA format | 5 |
| R-0601 | The subject digest of a Source VSA MUST include the revision identifier and MAY include other digests. | build platform operators | security | S-02 draft/source-requirements, Source VSA format | 5 |
| R-0602 | Non-cryptographic revision IDs MUST have a canonical type that includes the repository. | build platform operators | security | S-02 draft/source-requirements, Source VSA format | 5 |
| R-0603 | The sourceRefs annotation of a Source VSA SHOULD list the references that pointed to the revision, and Git references MUST be fully qualified. | build platform operators | security | S-02 draft/source-requirements, Source VSA format | 5 |
| R-0604 | The resourceUri of a Source VSA MUST give the repository URI. | build platform operators | security | S-02 draft/source-requirements, Source VSA format | 5 |
| R-0605 | The verifiedLevels field MUST include the asserted level, and the source control system MUST list only the highest level met. | build platform operators | security | S-02 draft/source-requirements, Source VSA format | 5 |
| R-0606 | The dependencyLevels field MAY be empty. | build platform operators | security | S-02 draft/source-requirements, Source VSA format | 5 |
| R-0607 | Organization-defined properties MUST use the ORG_SOURCE_ prefix, or the ORG_SOURCE_INTERNAL_ prefix for internal-only properties, and the SCS MUST enforce the prefix. | build platform operators | security | S-02 draft/source-requirements, Source VSA format | 5 |
| R-0608 | The authority that issues VSAs MUST know which entity issues each provenance attestation type and MUST confirm that each one came from its expected issuer. | build platform operators | security | S-02 draft/source-requirements, Source provenance | C-17 |
| R-0609 | The source control system MUST document each provenance format and how it supports the properties of the revision. | build platform operators | security | S-02 draft/source-requirements, Source provenance | C-06 |
| R-0610 | Each part of the source MUST have a clearly identified set of experts. | project maintainers | security | S-02 draft/source-example-controls, Expert Code Review | C-03 |
| R-0611 | Each modified portion of a change MUST receive pre-approval from a member of the relevant expert set. | managers | security | S-02 draft/source-example-controls, Expert Code Review | C-03 |
| R-0612 | Prior approvals MUST be revoked if a proposal changes after approval. | security engineers | security | S-02 draft/source-example-controls, Review Every Single Revision | C-03 |
| R-0613 | A new approval MUST be obtained from all required reviewers. | managers | security | S-02 draft/source-example-controls, Review Every Single Revision | C-03 |
| R-0614 | Branch protection MUST allow a branch to point only to revisions with passing tests. | managers | quality | S-02 draft/source-example-controls, Automated Testing | C-37 |
| R-0615 | Automated tests SHOULD run in a trustworthy environment (SLSA Build Track). | managers | security | S-02 draft/source-example-controls, Automated Testing | C-05 |
| R-0616 | Test results, or an aggregate of them, MUST be collected in the review tool for verification. | managers | quality | S-02 draft/source-example-controls, Automated Testing | C-37 |
| R-0617 | Automated tests SHOULD run against a merge of the topic branch into the target branch. | managers | quality | S-02 draft/source-example-controls, Automated Testing | C-37 |
| R-0618 | Reviewers MUST receive a full, meaningful content diff, not only a note that a file changed. | software engineers | security | S-02 draft/source-example-controls, Every Revision Reachable From a Branch Was Approved | C-03 |
| R-0619 | The reviewed diff MUST be rebased or squashed into a single commit with one parent. | managers | security | S-02 draft/source-example-controls, Every Revision Reachable From a Branch Was Approved | C-01 |
| R-0620 | The change description and all related discussion SHOULD be recorded. | managers | security | S-02 draft/source-example-controls, Immutable Change Discussion | C-01 |
| R-0621 | The discussion MUST be linked to the revision, typically through commit metadata. | managers | security | S-02 draft/source-example-controls, Immutable Change Discussion | C-01 |
| R-0622 | Collected discussion content SHOULD be made immutable once the change is accepted. | managers | security | S-02 draft/source-example-controls, Immutable Change Discussion | C-23 |
| R-0623 | Update frequency to key protected branches MUST be kept under set limits. | managers | operations | S-02 draft/source-example-controls, Merge Trains | C-25 |
| R-0624 | The merge train process MUST be protected like other artifact build pipelines. | managers | security | S-02 draft/source-example-controls, Merge Trains | C-16 |
| R-0625 | An attestation MUST be issued that the final revision of a merge train is identical to sequentially applying each approved change, with no other content added or removed. | managers | security | S-02 draft/source-example-controls, Merge Trains | C-06 |
| R-0626 | Consumers SHOULD be able to verify that the process was followed, using summary or source provenance attestations. | consumers | security | S-02 draft/source-example-controls, Intro | C-17 |
| R-0627 | Consumers SHOULD assess the parts of a source control system described in the assessing page. | consumers | security | S-02 draft/assessing-source-systems, Introduction | C-20 |
| R-0628 | Consumers SHOULD evaluate how well the source control system defends against contributors, maintainers and SCS administrators. | consumers | security | S-02 draft/assessing-source-systems, Adversary profiles | C-20 |
| R-0629 | Consumers SHOULD consider at least five elements: control configuration, change management interface, control plane, verifier and storage. | consumers | security | S-02 draft/assessing-source-systems, Source Control System components | C-20 |
| R-0630 | The two elements control plane and verifier should typically be assessed together. | project maintainers | security | S-02 draft/assessing-source-systems, Control plane and verifier (note) | C-20 |
| R-0631 | Evidence for self-attestation should be published on the internet. | project maintainers | security | S-02 draft/assessing-source-systems, Source control system evaluation | C-22 |
| R-0632 | Different verifiers MAY use different roots of trust for repositories. | consumers | security | S-02 draft/verifying-source, Step 1 | C-17 |
| R-0633 | The verifier SHOULD compare the VSA against expected values for at least the verifier identity, subject digest, verification result, resource URI, sourceRefs and verifiedLevels. | consumers | security | S-02 draft/verifying-source, Step 2 | C-17 |
| R-0634 | Expectations SHOULD be sufficient to detect an unofficial revision. | consumers | security | S-02 draft/verifying-source, Step 2 | C-17 |
| R-0635 | Expectations SHOULD make it harder for an adversary to create a malicious official revision. | consumers | security | S-02 draft/verifying-source, Step 2 | C-17 |
| R-0636 | Source provenance claims and their mapping to VSA claims SHOULD be formed together with the SCS and the producer. | consumers | security | S-02 draft/verifying-source, Step 3 | C-17 |
| R-0637 | The verifier SHOULD provide an authenticated communication mechanism for producers to set expectations. | consumers | security | S-02 draft/verifying-source, Forming Expectations | C-17 |
| R-0638 | There SHOULD be some protection against an adversary unilaterally modifying expectations. | project maintainers | security | S-02 draft/verifying-source, Forming Expectations | C-17 |
| R-0639 | At least one verification point SHOULD be used: build system, package ecosystem, consumer or continuous monitoring. | consumers | security | S-02 draft/verifying-source, Architecture options | C-17 |
| R-0640 | All implementations MUST use industry security best practices to conform. | build platform operators | security | S-02 draft/build-requirements, Security Best Practices | C-16 |
| R-0641 | The producer MUST select a build platform capable of reaching the desired build level. | project maintainers | security | S-02 draft/build-requirements, Producer | C-05 |
| R-0642 | The producer MUST build consistently. | project maintainers | security | S-02 draft/build-requirements, Producer | C-21 |
| R-0643 | The producer MAY give explicit metadata about the build process. | project maintainers | security | S-02 draft/build-requirements, Producer | C-06 |
| R-0644 | If an ecosystem requires a configuration file, the producer MUST complete it and keep it current. | project maintainers | security | S-02 draft/build-requirements, Producer | 5 |
| R-0645 | The producer MUST distribute provenance. | project maintainers | security | S-02 draft/build-requirements, Producer | C-06 |
| R-0646 | The producer MAY delegate distribution of provenance to a capable package ecosystem. | project maintainers | security | S-02 draft/build-requirements, Producer | C-06 |
| R-0647 | The build process MUST generate provenance that identifies the output by digest and describes how it was produced. | build platform operators | security | S-02 draft/build-requirements, Provenance Exists (L1 to L3) | C-06 |
| R-0648 | The provenance format MUST be acceptable to the ecosystem or consumer. | build platform operators | security | S-02 draft/build-requirements, Provenance Exists (L1 to L3) | C-06 |
| R-0649 | The SLSA Provenance format is RECOMMENDED. | build platform operators | security | S-02 draft/build-requirements, Provenance Exists (L1 to L3) | 5 |
| R-0650 | Alternate provenance formats MUST carry equivalent information at each level and SHOULD be translatable. | build platform operators | security | S-02 draft/build-requirements, Provenance Exists (L1 to L3) | C-06 |
| R-0651 | Some provenance fields MAY be absent at L1. | build platform operators | security | S-02 draft/build-requirements, Provenance Exists (L1 to L3) | 5 |
| R-0652 | Consumers MUST be able to validate the authenticity of provenance (L2 and L3). | consumers | security | S-02 draft/build-requirements, Provenance is Authentic | C-06 |
| R-0653 | A digital signature from a key accessible only to the build platform SHOULD be used (L2 and L3). | build platform operators | security | S-02 draft/build-requirements, Provenance is Authentic | C-06 |
| R-0654 | Transparency logs or time stamping are RECOMMENDED (L2 and L3). | build platform operators | security | S-02 draft/build-requirements, Provenance is Authentic | C-06 |
| R-0655 | Provenance generation MUST occur in the control plane, not by a tenant (L2 and L3). | build platform operators | security | S-02 draft/build-requirements, Provenance is Authentic | C-07 |
| R-0656 | Builders SHOULD document the fields that a tenant generates (L2 and L3). | build platform operators | security | S-02 draft/build-requirements, Provenance is Authentic | C-06 |
| R-0657 | Provenance MUST resist forgery by tenants (L3). | build platform operators | security | S-02 draft/build-requirements, Provenance is Unforgeable | C-07 |
| R-0658 | Signing secrets MUST be stored in a secure system accessible only to the build service account and MUST NOT be reachable by user build steps (L3). | build platform operators | security | S-02 draft/build-requirements, Provenance is Unforgeable | C-07 |
| R-0659 | Every provenance field MUST be generated or verified by the trusted control plane of the platform (L3). | build platform operators | security | S-02 draft/build-requirements, Provenance is Unforgeable | C-07 |
| R-0660 | External parameters MUST be fully enumerated (L3). | build platform operators | security | S-02 draft/build-requirements, Provenance is Unforgeable | C-06 |
| R-0661 | All build steps run on a hosted platform, shared or dedicated, and not on an individual's workstation (L2 and L3). | build platform operators | security | S-02 draft/build-requirements, Isolation strength (Hosted) | C-05 |
| R-0662 | The platform MUST stop builds from accessing platform secrets, such as the provenance signing key (L3). | build platform operators | security | S-02 draft/build-requirements, Isolated | C-07 |
| R-0663 | The platform MUST stop overlapping builds from influencing one another (L3). | build platform operators | security | S-02 draft/build-requirements, Isolated | C-07 |
| R-0664 | Each build MUST get an ephemeral environment, so that no state persists between builds (L3). | build platform operators | security | S-02 draft/build-requirements, Isolated | C-07 |
| R-0665 | The platform MUST prevent cache poisoning, and output MUST be identical whether or not a cache is used (L3). | build platform operators | security | S-02 draft/build-requirements, Isolated | C-07 |
| R-0666 | No remote-influence service may be open unless it is captured as an external parameter (L3). | build platform operators | security | S-02 draft/build-requirements, Isolated | C-07 |
| R-0667 | The build system is deployed on compute that supports hardware-level measurement and attestation of system state (Build Environment track, L3). | build platform operators | security | S-02 draft/tracks, Build Environment Track | C-07 |
| R-0668 | The platform generates provenance for the build image and validates the build environment at boot against known-good values. | build platform operators | security | S-02 draft/tracks, Build Environment Track | C-07 |
| R-0669 | Other dependency verdicts MAY be recorded as transparency data (Dependency track, L1). | build platform operators | security | S-02 draft/tracks, Dependency Track | C-20 |
| R-0670 | Identity-verification verdicts MUST be verified (Dependency track, L2). | build platform operators | security | S-02 draft/tracks, Dependency Track | C-20 |
| R-0671 | Admission policies MUST be recorded in the provenance, and the platform signs the provenance (Dependency track, L2). | build platform operators | security | S-02 draft/tracks, Dependency Track | C-17 |
| R-0672 | Bypass of the ingestion path is structurally blocked, the upstream provenance verdict is recorded, and signing and cross-dependency ingestion are isolated (Dependency track, L3). | build platform operators | security | S-02 draft/tracks, Dependency Track | C-07 |
| R-0673 | Verifiers SHOULD check that the builder identity is in the trusted builder-to-level map. | consumers | security | S-02 v1.2/verifying-artifacts, How to verify | C-17 |
| R-0674 | Verifiers SHOULD verify the signature of the provenance envelope. | consumers | security | S-02 v1.2/verifying-artifacts, How to verify | C-17 |
| R-0675 | Verifiers SHOULD confirm that buildType and externalParameters match expected values. | consumers | security | S-02 v1.2/verifying-artifacts, How to verify | C-17 |
| R-0676 | The package ecosystem MAY allow an approved list of externalParameters to be ignored. | build platform operators | security | S-02 draft/verifying-artifacts, How to verify | C-17 |
| R-0677 | Any unrecognized externalParameters SHOULD cause verification to fail. | consumers | security | S-02 draft/verifying-artifacts, How to verify | C-17 |
| R-0678 | If provenance is not in the recommended format, verifiers SHOULD run equivalent checks on its fields. | consumers | security | S-02 draft/verifying-artifacts, How to verify | C-17 |
| R-0679 | Verifiers SHOULD carefully consider which build platforms are added to the roots of trust. | consumers | security | S-02 draft/verifying-artifacts, Step 1 | C-17 |
| R-0680 | Expectations SHOULD be sufficient to detect or prevent an adversary from injecting unofficial behavior. | consumers | security | S-02 draft/verifying-artifacts, Step 2 | C-17 |
| R-0681 | Verifiers SHOULD compare provenance against expected values for at least builder identity, canonical source repository, buildType and externalParameters. | consumers | security | S-02 draft/verifying-artifacts, Step 2 | C-17 |
| R-0682 | Verification tools SHOULD reject unrecognized fields in externalParameters. | consumers | security | S-02 draft/verifying-artifacts, Step 2 | C-17 |
| R-0683 | At least one verification location SHOULD be used: ecosystem, consumer or monitor. | consumers | security | S-02 draft/verifying-artifacts, Architecture options | C-17 |
| R-0684 | The verifier SHOULD provide an authenticated communication mechanism for the producer to set expectations. | project maintainers | security | S-02 draft/verifying-artifacts, Forming Expectations | C-17 |
| R-0685 | There SHOULD be some protection against an adversary unilaterally modifying expectations. | project maintainers | security | S-02 draft/verifying-artifacts, Forming Expectations | duplicate: R-0638 |
| R-0686 | Upload-time provenance verification by the package ecosystem is RECOMMENDED whenever possible. | build platform operators | security | S-02 draft/verifying-artifacts, Architecture options | C-17 |
| R-0687 | A monitor MAY verify a set of packages that mimics the packages published through one or more ecosystems. | consumers | security | S-02 draft/verifying-artifacts, Architecture options | C-17 |
| R-0688 | A monitor SHOULD publish its expectations for all packages it verifies. | consumers | security | S-02 draft/verifying-artifacts, Architecture options | C-17 |
| R-0689 | Organizations should integrate the SSDF throughout their existing software development practices | managers | quality | S-03 page 8 | C-48 |
| R-0690 | Organizations should express their secure software development requirements to third-party suppliers using SSDF conventions | managers | security | S-03 page 8 | C-20 |
| R-0691 | Organizations should acquire software that meets the practices described in the SSDF | managers | security | S-03 page 8 | C-20 |
| R-0692 | Organizations should ensure that their people, processes and technology are prepared to perform secure software development | managers | quality | S-03 page 8 | C-48 |
| R-0693 | Organizations should protect all components of their software from tampering and unauthorized access | managers | security | S-03 page 8 | C-02 |
| R-0694 | Organizations should produce well-secured software with minimal security vulnerabilities in its releases | managers | security | S-03 page 8 | C-11 |
| R-0695 | Organizations should identify residual vulnerabilities in their software releases and respond to them, and prevent similar ones in the future | managers | security | S-03 page 8 | C-12 |
| R-0696 | Organizations should adopt a risk-based approach to decide which practices are relevant, appropriate and effective | managers | quality | S-03 page 8 | C-48 |
| R-0697 | Organizations should consult the references and other resources for information on implementing the practices | managers | quality | S-03 page 8 | C-45 |
| R-0698 | Secure software development practices should be integrated throughout any SDLC model | managers | quality | S-03 page 10 | C-48 |
| R-0699 | Factors such as risk, cost, feasibility and applicability should be considered when deciding which practices to use and how much effort to spend | managers | quality | S-03 page 12 | C-48 |
| R-0700 | The tenant organization should establish an agreement with its providers that names the responsible party for each practice and task, and how each provider attests conformance | managers | security | S-03 page 12 | C-20 |
| R-0701 | Organizations should ensure that their people, processes and technology are prepared to perform secure software development at the organization level (PO group) | managers | quality | S-03 page 13 | C-48 |
| R-0702 | Organizations should protect all components of their software from tampering and unauthorized access (PS group) | managers | security | S-03 page 13 | C-02 |
| R-0703 | Organizations should produce well-secured software with minimal security vulnerabilities in its releases (PW group) | managers | security | S-03 page 13 | C-11 |
| R-0704 | Organizations should identify residual vulnerabilities and respond appropriately (RV group) | managers | security | S-03 page 13 | C-12 |
| R-0705 | Organizations adopting the SSDF should define the terms sensitive data, qualified person and well-secured in the context of their own environments | managers | quality | S-03 page 13 | C-48 |
| R-0706 | Organizations should enumerate their environments, which is necessary to secure them properly | managers | operations | S-03 page 13 | C-35 |
| R-0707 | Practice PO.1: ensure that security requirements for software development are known at all times and maintained over time | managers | security | S-03 page 14 | C-13 |
| R-0708 | Task PO.1.1: identify and document all security requirements for the organization's development infrastructures and processes, and maintain them over time | managers | security | S-03 page 14 | C-13 |
| R-0709 | Task PO.1.2: identify and document all security requirements for organization-developed software, and maintain them over time | managers | security | S-03 page 14 | C-13 |
| R-0710 | Task PO.1.3: communicate requirements to all third parties who provide commercial components for reuse | managers | security | S-03 page 14 | C-20 |
| R-0711 | Practice PO.2: ensure that everyone inside and outside the organization involved in the SDLC is prepared for their SDLC roles | security engineers | security | S-03 page 15 | C-19 |
| R-0712 | Task PO.2.1: create or alter roles so that all parts of the SDLC are covered, and review and maintain them | managers | security | S-03 page 15 | C-19 |
| R-0713 | Task PO.2.2: provide role-based training for all personnel with responsibilities that contribute to secure development, and review and update it | security engineers | security | S-03 page 15 | C-19 |
| R-0714 | Task PO.2.3: obtain upper management or the authorizing official's commitment to secure development and convey it to all with development-related roles | managers | security | S-03 page 16 | C-19 |
| R-0715 | Practice PO.3: use automation to reduce human effort and improve the accuracy, reproducibility, usability and coverage of security practices | managers | operations | S-03 page 16 | C-34 |
| R-0716 | Task PO.3.1: specify which tools or tool types must or should be in each toolchain to mitigate identified risks, and how the components integrate | managers | operations | S-03 page 16 | C-33 |
| R-0717 | Task PO.3.2: follow recommended security practices to deploy, operate and maintain tools and toolchains | managers | security | S-03 page 16 | C-16 |
| R-0718 | Task PO.3.3: configure tools to generate artifacts of their support for the organization's defined secure development practices | managers | quality | S-03 page 16 | C-42 |
| R-0719 | Practice PO.4: ensure that the software from the SDLC meets the organization's expectations by defining and using criteria for security checks during development | managers | quality | S-03 page 17 | C-42 |
| R-0720 | Task PO.4.1: define criteria for software security checks and track them throughout the SDLC | managers | quality | S-03 page 17 | C-42 |
| R-0721 | Task PO.4.2: implement processes and mechanisms to gather and safeguard the information needed for the criteria | managers | quality | S-03 page 17 | C-42 |
| R-0722 | Practice PO.5: ensure that all components of the development environments are strongly protected from internal and external threats | managers | security | S-03 page 17 | C-16 |
| R-0723 | Task PO.5.1: separate and protect each environment involved in software development | managers | security | S-03 page 17 | C-16 |
| R-0724 | Task PO.5.2: secure and harden development endpoints, using a risk-based approach, to perform development tasks | managers | security | S-03 page 18 | C-16 |
| R-0725 | Practice PS.1: protect all forms of code from unauthorized access and tampering | managers | security | S-03 page 18 | C-02 |
| R-0726 | Task PS.1.1: store all forms of code in a repository and restrict access based on least privilege | managers | security | S-03 page 18 | C-02 |
| R-0727 | Practice PS.2: help software acquirers ensure that the software they acquire is legitimate and has not been tampered with | managers | security | S-03 page 19 | C-06 |
| R-0728 | Task PS.2.1: make software integrity verification information available to software acquirers | managers | security | S-03 page 19 | C-06 |
| R-0729 | Practice PS.3: preserve software releases to help identify, analyze and eliminate vulnerabilities found after release | managers | security | S-03 page 19 | C-23 |
| R-0730 | Task PS.3.1: securely archive the necessary files and supporting data for each release, with read-only access for necessary personnel | managers | security | S-03 page 19 | C-23 |
| R-0731 | Task PS.3.2: collect, safeguard, maintain and share provenance data for all components of each release | managers | security | S-03 page 19 | C-06 |
| R-0732 | Practice PW.1: identify and evaluate security requirements and security risks, design to mitigate them, and justify any waived requirements | managers | security | S-03 page 20 | C-13 |
| R-0733 | Task PW.1.1: use forms of risk modeling to assess the security risk of the software and address it | managers | security | S-03 page 20 | C-13 |
| R-0734 | Task PW.1.2: track and maintain the software's security requirements, risks and design decisions | managers | security | S-03 page 20 | C-13 |
| R-0735 | Task PW.1.3: where appropriate, build in support for standardized security features and services instead of proprietary ones | managers | security | S-03 page 20 | C-18 |
| R-0736 | Practice PW.2: help ensure the software meets its security requirements and addresses the identified risk information | managers | security | S-03 page 21 | C-13 |
| R-0737 | Task PW.2.1: have a qualified person not involved in the design, or an automated toolchain process, review the design for compliance | managers | security | S-03 page 21 | C-03 |
| R-0738 | Practice PW.4: acquire and maintain well-secured reusable components rather than duplicating functionality | managers | security | S-03 page 21 | C-20 |
| R-0739 | Task PW.4.1: acquire and maintain well-secured third-party software components | managers | security | S-03 page 21 | C-20 |
| R-0740 | Task PW.4.2: create and maintain well-secured in-house components that follow the SDLC processes | managers | operations | S-03 page 21 | C-33 |
| R-0741 | Task PW.4.4: verify that acquired and all other third-party components comply with the organization's requirements throughout their life cycles | managers | security | S-03 page 22 | C-20 |
| R-0742 | Practice PW.5: create source code by following secure coding practices | managers | quality | S-03 page 22 | C-40 |
| R-0743 | Task PW.5.1: follow all secure coding practices that suit the languages and environment to meet the organization's requirements | managers | quality | S-03 page 22 | C-40 |
| R-0744 | Practice PW.6: configure compilers, interpreters and build processes to improve executable security | managers | quality | S-03 page 23 | C-40 |
| R-0745 | Task PW.6.1: use compiler, interpreter and build tools that offer features to improve executable security | managers | quality | S-03 page 23 | C-40 |
| R-0746 | Task PW.6.2: determine which tool features to use and how to configure them, then implement and use the approved configurations | managers | quality | S-03 page 23 | C-40 |
| R-0747 | Practice PW.7: help identify vulnerabilities so that they can be corrected before release | managers | security | S-03 page 23 | C-14 |
| R-0748 | Task PW.7.1: determine whether code review and/or code analysis should be performed, and how | managers | security | S-03 page 23 | C-14 |
| R-0749 | Task PW.7.2: perform code review and/or analysis based on secure coding standards, and record and triage all issues in the workflow or tracking system | managers | security | S-03 page 23 | C-14 |
| R-0750 | Practice PW.8: help identify vulnerabilities through testing, so that they can be corrected before release | managers | quality | S-03 page 24 | C-38 |
| R-0751 | Task PW.8.1: determine whether executable code testing should be performed, and which types | managers | quality | S-03 page 24 | C-38 |
| R-0752 | Task PW.8.2: scope, design, perform and document the testing, and record and triage all issues | managers | quality | S-03 page 24 | C-38 |
| R-0753 | Practice PW.9: help improve the security of the software at installation by making the default settings secure | managers | security | S-03 page 25 | C-18 |
| R-0754 | Task PW.9.1: define a secure baseline by determining how to configure each setting that affects security | managers | security | S-03 page 25 | C-18 |
| R-0755 | Task PW.9.2: implement the default settings and document each setting for software administrators | managers | security | S-03 page 25 | C-18 |
| R-0756 | Practice RV.1: help ensure that vulnerabilities are identified more quickly so that they can be remediated more quickly, according to risk | managers | security | S-03 page 25 | C-11 |
| R-0757 | Task RV.1.1: gather information on potential vulnerabilities from software acquirers, users and public sources, and investigate all credible reports | managers | security | S-03 page 25 | C-12 |
| R-0758 | Task RV.1.2: review, analyze and/or test the software's code to identify or confirm undetected vulnerabilities | managers | security | S-03 page 25 | C-11 |
| R-0759 | Practice RV.2 (Assess, Prioritize, and Remediate Vulnerabilities) helps ensure that vulnerabilities are remediated to reduce the window of opportunity for attackers. | security engineers | security | S-03 page 26 | C-11 |
| R-0760 | Analyze each vulnerability to gather sufficient information about its risk to plan its remediation or other risk response. | security engineers | security | S-03 page 26 (RV.2.1) | C-11 |
| R-0761 | Plan and implement risk responses for vulnerabilities, and prioritize the actions to be taken. | security engineers | security | S-03 page 27 (RV.2.2) | C-11 |
| R-0762 | Practice RV.3 (Analyze Vulnerabilities to Identify Their Root Causes) helps reduce the frequency of vulnerabilities in the future. | quality assurance staff | quality | S-03 page 27 | C-43 |
| R-0763 | Analyze identified vulnerabilities to determine their root causes. | quality assurance staff | quality | S-03 page 27 (RV.3.1) | C-43 |
| R-0764 | Analyze the root causes over time to identify patterns, such as a secure coding practice that is not followed consistently. | quality assurance staff | quality | S-03 page 27 (RV.3.2) | C-43 |
| R-0765 | Review the software for similar vulnerabilities to eradicate a class of vulnerabilities, and proactively fix them. | security engineers | security | S-03 page 27 (RV.3.3) | C-11 |
| R-0766 | Review the SDLC process, and update it if appropriate to prevent or reduce the likelihood of the root cause recurring. | managers | quality | S-03 page 27 (RV.3.4) | C-52 |
| R-0767 | Have a policy that addresses vulnerability disclosure and remediation, and implement the roles, responsibilities and processes needed to support that policy. | security engineers | security | S-03 page 26 (RV.1.3) | C-12 |
| R-0768 | SSC security assurance measures must be integrated into CI/CD pipelines. | security engineers | security | S-04 page 11 | C-14 |
| R-0769 | SSC security should account for discovering and tracking software security defects, not only for mitigating attacks. | quality assurance staff | quality | S-04 page 13 | C-43 |
| R-0770 | The software bill of materials must be shared with end users so that they can build inventories of software components. | consumers | security | S-04 page 13 | C-09 |
| R-0771 | Developer workstations should not be trusted as part of the build process. | security engineers | security | S-04 page 17 | C-05 |
| R-0772 | Companies should be aware of these risks and take appropriate measures to secure their SSC. | managers | quality | S-04 page 17 | C-48 |
| R-0773 | Organizations should be aware of cases of inadequate secrets management and take suitable measures to avoid such practices. | managers | security | S-04 page 17 | C-04 |
| R-0774 | Companies should identify potential risks and vulnerabilities, assess their security posture, and implement appropriate defensive measures. | managers | quality | S-04 page 18 | C-48 |
| R-0775 | It is essential to verify the provenance information of an ingested component, to confirm that it is what it says it is and comes from an expected source. | security engineers | security | S-04 page 18 | C-17 |
| R-0776 | Companies should identify critical assets and implement controls to protect them from unauthorized access. | managers | security | S-04 page 18 | C-02 |
| R-0777 | Organizations should regularly assess their security posture, identify potential weaknesses and vulnerabilities, and implement appropriate defensive measures. | managers | security | S-04 page 20 | C-22 |
| R-0778 | Organizations should also ensure that their SDLC environment remains compliant with applicable security and other relevant standards. | managers | security | S-04 page 20 | C-22 |
| R-0779 | All developer systems should meet a predefined minimum baseline for security, including current patches, protected unshared user accounts, and enforced access controls when interacting with SCM. | software engineers | security | S-04 page 20 | C-16 |
| R-0780 | Government and enterprise environments should establish and adhere to a well-defined security policy that meets regulatory requirements and industry best practices. | regulators and auditors | quality | S-04 page 20 | C-48 |
| R-0781 | Independent and open-source developers will need to follow best practices to protect their own systems. | project maintainers | security | S-04 page 20 | C-16 |
| R-0782 | Readers should refer to SP 800-53r5 for a more complete treatment of security policy. | managers | quality | S-04 page 20 | C-48 |
| R-0783 | The security team should establish a policy for trusted OSS sources, including review of minimum coding requirements, reputational standards, and distribution of source code in a digitally signed package. | security engineers | security | S-04 page 21 | C-20 |
| R-0784 | The security team should approve the merging of unverified sources of OSS. | security engineers | security | S-04 page 21 | C-20 |
| R-0785 | Developers should download OSS as source code rather than pre-compiled libraries or binaries, when available. | software engineers | security | S-04 page 21 | C-20 |
| R-0786 | Developers should verify digital signatures, run vulnerability scans, check for recent updates on newly downloaded OSS source-code packages, and generate an SBOM with dependency scanning on the first commit. | software engineers | security | S-04 page 21 | C-17 |
| R-0787 | Artifacts should be scanned in internal repositories for newly discovered or identified defects, with the ability to stop their use in builds based on criticality. | security engineers | security | S-04 page 21 | C-11 |
| R-0788 | CI/CD processes should be audited regularly, and automation should be introduced wherever possible. | operations engineers | operations | S-04 page 21 | C-24 |
| R-0789 | There should be an isolated CI/CD environment and elevated administrator credentials for the deployment of applications in clouds. | security engineers | security | S-04 page 21 | C-07 |
| R-0790 | There should be enhanced real-time monitoring and alerting mechanisms to detect suspicious activities in CI/CD servers. | operations engineers | operations | S-04 page 21 | C-28 |
| R-0791 | The proposed changes should adhere to the SDLC processes defined by the organization. | software engineers | quality | S-04 page 21 | C-42 |
| R-0792 | Write access to the SCM should be considered a high risk and tightly controlled. | security engineers | security | S-04 page 21 | C-02 |
| R-0793 | Another developer should perform a code review before the patch is merged. | software engineers | security | S-04 page 21 | C-03 |
| R-0794 | Code analysis tools should be implemented, and care should be taken not to overwhelm developers with false positives. | software engineers | security | S-04 page 21 | C-14 |
| R-0795 | The generation of provenance data should be accompanied by mechanisms to validate, authenticate, and leverage the data in policy decisions. | security engineers | security | S-04 page 22 | C-17 |
| R-0796 | The security assurance measures that need to be added include internal SSC security practices and practices for third-party software. | security engineers | security | S-04 page 22 | C-20 |
| R-0797 | Entities in SSC activities should be authenticated through verification of credentials, and authorized according to enterprise business policies. | security engineers | security | S-04 page 23 | C-02 |
| R-0798 | The integrity of artifacts and repositories should be ensured through verification of their digital signatures. | security engineers | security | S-04 page 23 | C-17 |
| R-0799 | The establishment of trust should be a recurring process throughout the CI/CD system. | security engineers | security | S-04 page 23 | C-16 |
| R-0800 | The inputs and outputs of each build step should be verified to ensure that the correct steps have been executed by the expected component or entity. | security engineers | security | S-04 page 23 | C-17 |
| R-0801 | Other artifacts used for security assurance, such as SBOMs, vulnerability reports, and model registries that use AI models, must also be trusted. | security engineers | security | S-04 page 23 | C-17 |
| R-0802 | Harden the CI/CD execution environment to reduce its attack surface. This is a prerequisite. | security engineers | security | S-04 page 24 | C-16 |
| R-0803 | Define roles for the actors who operate the CI/CD pipelines. | operations engineers | security | S-04 page 24 | C-02 |
| R-0804 | Identify the granular authorizations for generating and committing code, generating builds and packages, and checking artifacts into and out of repositories. | security engineers | security | S-04 page 24 | C-02 |
| R-0805 | Automate the entire CI/CD pipeline through the deployment of appropriate tools. | operations engineers | operations | S-04 page 24 | C-24 |
| R-0806 | Define CI/CD pipeline activities and security requirements for application code, infrastructure as code, and policy and configuration code. | security engineers | security | S-04 page 24 | C-13 |
| R-0807 | Goal: the CI framework should support both cloud-native and other types of applications. | operations engineers | operations | S-04 page 24 | C-33 |
| R-0808 | Goal: the CI framework should use standard-compliant evidence structures, such as metadata and digital signatures. | security engineers | security | S-04 page 24 | C-06 |
| R-0809 | Goal: the CI framework should support multiple hardware and software platforms. | operations engineers | operations | S-04 page 24 | C-33 |
| R-0810 | Goal: the CI framework should support infrastructures for generating evidence, such as SBOM and digital signature generators. | security engineers | security | S-04 page 24 | C-06 |
| R-0811 | Specify build policies covering a secure isolated build platform with hardened build servers, the build tools, and the authentication and authorization of developers who perform the build. | security engineers | security | S-04 page 25 | C-07 |
| R-0812 | Enforce the build policies with techniques such as an agent and a policy enforcement engine. | security engineers | security | S-04 page 25 | C-16 |
| R-0813 | Ensure the concurrent generation of evidence for build attestation during software delivery. | security engineers | security | S-04 page 25 | C-06 |
| R-0814 | Wrap CI tool commands with capabilities that gather evidence and create an evidence trail of the SDLC. This is named as a common technique. | security engineers | security | S-04 page 25 | C-06 |
| R-0815 | The build system should be able to confirm that its tools and processes run in an isolated environment. | security engineers | security | S-04 page 25 | C-07 |
| R-0816 | Evidence should include the hash of the final build artifact, its files, libraries, materials and events, signed by a trusted component that developers do not control. | security engineers | security | S-04 page 25 | C-06 |
| R-0817 | Evidence generation should be enabled by a process with higher trust or isolation than the build, and verified within the build as it occurs. | security engineers | security | S-04 page 25 | C-07 |
| R-0818 | Platform components used in the CI process, such as the compiler and interpreter, must be hardened, isolated and secure. | security engineers | security | S-04 page 25 | C-07 |
| R-0819 | Attestations must be cryptographically signed using a secure key. | security engineers | security | S-04 page 26 | C-06 |
| R-0820 | The storage location of attestations must be tamper-proof and protected by robust access control. | security engineers | security | S-04 page 26 | C-23 |
| R-0821 | Authentication for PULL and PUSH operations must be consistent with the role of the developer. | software engineers | security | S-04 page 26 | C-02 |
| R-0822 | The integrity of code in the repository must be checked so that it can be trusted for further updates. | security engineers | security | S-04 page 26 | C-01 |
| R-0823 | Developers with merge approval permissions cannot approve their own merges. | software engineers | security | S-04 page 26 | C-03 |
| R-0824 | The project maintainer should run automated checks on all artifacts covered in a pushed change, such as unit tests, linters, integrity tests and security checks. | project maintainers | quality | S-04 page 27 | C-37 |
| R-0825 | CI pipelines should be run with tools only when confidence is established in the trustworthiness of the source-code origin of those tools. | security engineers | security | S-04 page 27 | C-10 |
| R-0826 | The repository or SCM system should either run CI workflows in sandboxed environments with no network access, no privileged access and no access to secrets, or delay CI runs until a maintainer with write access approves them. | project maintainers | security | S-04 page 27 | C-15 |
| R-0827 | The built-in protection should apply when an outside contributor submits a pull request to a public repository, and be set at the strictest level, such as approval for all outside collaborators. | project maintainers | security | S-04 page 27 | C-15 |
| R-0828 | If the SCM has no built-in protection, external security tools are required that evaluate and enhance the security posture of the SCM, with or without a policy, and produce a status report with actionable recommendations. | security engineers | security | S-04 page 27 | C-16 |
| R-0829 | If the SCM has no built-in protection, external security tools are required that detect and remediate misconfigurations, security vulnerabilities and compliance issues. | security engineers | security | S-04 page 27 | C-16 |
| R-0830 | The framework should protect against all known attacks on metadata generation, the signing process, signing key management, the integrity of the signing authority, key validation and signature verification. | security engineers | security | S-04 page 28 | C-06 |
| R-0831 | The framework should minimise the impact of key compromise by supporting roles with multiple keys and threshold or quorum trust, except for minimally trusted roles that use a single key. | security engineers | security | S-04 page 28 | C-04 |
| R-0832 | Online keys should not be used for any role that clients ultimately trust for files they may install. | security engineers | security | S-04 page 28 | C-04 |
| R-0833 | When keys are online, they should be stored in an HSM and used only when the signed artifacts pass the policy. | security engineers | security | S-04 page 28 | C-04 |
| R-0834 | The framework should require the policy of section 5.1.1 to be satisfied before the signing operation is performed. | security engineers | security | S-04 page 28 | C-06 |
| R-0835 | The framework must be flexible enough to meet the needs of a wide variety of software update systems. | operations engineers | operations | S-04 page 28 | C-33 |
| R-0836 | The framework must be easy to integrate with software update systems. | operations engineers | operations | S-04 page 28 | C-33 |
| R-0837 | Appropriate forms of testing should be performed before code commits. | software engineers | quality | S-04 page 28 | C-37 |
| R-0838 | SAST and DAST tools covering all languages used in development should be run in CI/CD pipelines, with code coverage reports given to developers and security personnel. | security engineers | security | S-04 page 28 | C-14 |
| R-0839 | Open-source modules and libraries must be enumerated, understood and evaluated for policy, and the security conditions for their inclusion must be tested. | security engineers | security | S-04 page 29 | C-20 |
| R-0840 | Dependency file detectors should detect all dependencies, including transitive dependencies, preferably with no limit on depth. | security engineers | security | S-04 page 29 | C-09 |
| R-0841 | Committed code should be evaluated for policy adherence, including the absence of secrets; detected secrets should be displayed prominently, alerts should be generated, and remediation methods should be documented. | security engineers | security | S-04 page 29 | C-04 |
| R-0842 | Push protection should be enabled for all repositories assigned to an administrator, including verification of developer identity and authorization, enforcement of developer signing of commits, and file name verification. | build platform operators | security | S-04 page 29 | C-02 |
| R-0843 | A security scanning sub-feature should be invoked on code that is ready to be deployed, to detect secrets; the repository should be scanned for secrets even before it is populated with code. | security engineers | security | S-04 page 29 | C-04 |
| R-0844 | Before merging pull requests, it should be possible to view details of vulnerable versions through dependency review. | security engineers | security | S-04 page 29 | C-11 |
| R-0845 | It should be possible to specify that the artifact to be deployed must have been generated by the secure build process to be cleared for deployment. | operations engineers | operations | S-04 page 29 | C-24 |
| R-0846 | There should be evidence that the container image was scanned for vulnerabilities and attested for its findings. | security engineers | security | S-04 page 30 | C-11 |
| R-0847 | It should be possible to allow or block image deployment based on organization-defined policies. | managers | security | S-04 page 30 | C-17 |
| R-0848 | The release build scripts should be checked periodically for malicious code. | security engineers | security | S-04 page 30 | C-14 |
| R-0849 | A container image should be scanned for vulnerabilities as soon as it is built, even before it is pushed to a registry. | security engineers | security | S-04 page 30 | C-11 |
| R-0850 | Tools that interact with repositories of container images and language packages should be capable of integration with CD tools. | operations engineers | operations | S-04 page 30 | C-24 |
| R-0851 | The GitOps process should rely on automation rather than manual operations. | operations engineers | operations | S-04 page 30 | C-26 |
| R-0852 | Package managers that facilitate GitOps should preserve all data on released packages, including module version numbers, configuration files and metadata. | security engineers | security | S-04 page 30 | C-23 |
| R-0853 | Changes should not be applied manually at runtime; changes should be made in the code and a new release triggered. | operations engineers | operations | S-04 page 31 | C-26 |
| R-0854 | The Git repository should be pulled automatically and compared with the specified state, to monitor and remediate drift. | operations engineers | operations | S-04 page 31 | C-26 |
| R-0855 | For configurations that deviate from the specified state, administrators may choose to resync them automatically. | build platform operators | operations | S-04 page 31 | C-26 |
| R-0856 | For configurations that deviate from the specified state, notifications should be sent and manual remediation should be performed. | operations engineers | operations | S-04 page 31 | C-28 |
| R-0857 | Strategy: verify that software is built correctly through tamper-proof build pipelines with verified visibility into dependencies and steps. | security engineers | security | S-04 page 31 | C-05 |
| R-0858 | Strategy: specify checklists for each step of the delivery pipeline, and check and enforce compliance with them. | quality assurance staff | quality | S-04 page 31 | C-42 |
| R-0859 | Strategy: ensure integrity and provenance through digital signatures and attestations. | security engineers | security | S-04 page 31 | C-06 |
| R-0860 | Strategy: institute a build horizon, so that code older than a certain time period is not launched. | operations engineers | operations | S-04 page 31 | C-25 |
| R-0861 | Strategy: secure CI/CD clients to prevent malicious code from stealing confidential information or exfiltrating data. | security engineers | security | S-04 page 31 | C-16 |
| R-0862 | Mapped practice PO.1: define security requirements for software development so that they are known at all times. | security engineers | security | S-04 page 35 | C-13 |
| R-0863 | Mapped practice PO.2: ensure that everyone involved in the SDLC is prepared to perform their roles. | security engineers | security | S-04 page 36 | C-19 |
| R-0864 | Mapped practice PO.3: use automation for supporting toolchains to reduce human effort and improve accuracy and comprehensiveness. | operations engineers | operations | S-04 page 36 | C-34 |
| R-0865 | Mapped practice PO.4: define and use criteria for checking the security of software during development. | quality assurance staff | quality | S-04 page 37 | C-42 |
| R-0866 | Mapped practice PO.5: implement and maintain secure environments, strongly protected from internal and external threats. | security engineers | security | S-04 page 37 | C-16 |
| R-0867 | Mapped practice PS.1: protect all forms of code from unauthorized access and tampering. | security engineers | security | S-04 page 37 | C-02 |
| R-0868 | Mapped practice PS.2: provide a mechanism for verifying software release integrity. | security engineers | security | S-04 page 38 | C-17 |
| R-0869 | Mapped practice PS.3: archive and protect each software release. | security engineers | security | S-04 page 38 | C-23 |
| R-0870 | Mapped practice PW.5: create source code by adhering to secure coding practices. | software engineers | quality | S-04 page 39 | C-40 |
| R-0871 | Mapped practice PW.6: configure compilation, interpreter and build processes to improve executable security. | software engineers | quality | S-04 page 39 | C-40 |
| R-0872 | Mapped practice PW.8: test executable code to identify vulnerabilities and verify compliance with security requirements. | security engineers | security | S-04 page 40 | C-14 |
| R-0873 | Mapped practice PW.9: configure software to have secure settings by default. | security engineers | security | S-04 page 40 | C-18 |
| R-0874 | Set branch protection on branches that feed production or sensitive systems, and exempt no user or branch from it. | security engineers | security | S-06 CICD-SEC-01, Recommendations item 1 | C-03 |
| R-0875 | Do not let accounts that can push unreviewed code also trigger deployment pipelines for that repository. | security engineers | security | S-06 CICD-SEC-01, Recommendations item 2 | C-08 |
| R-0876 | Keep auto-merge rules to the smallest scope, review their logic so they cannot be bypassed, and keep third-party code out of them. | security engineers | security | S-06 CICD-SEC-01, Recommendations item 3 | C-20 |
| R-0877 | Where applicable, require extra approval before any account can trigger production build or deployment pipelines. | operations engineers | operations | S-06 CICD-SEC-01, Recommendations item 4 | C-31 |
| R-0878 | Let only artifacts created by a pre-approved CI service account move through the pipeline, and require secondary review for artifacts from other accounts. | security engineers | security | S-06 CICD-SEC-01, Recommendations item 5 | C-17 |
| R-0879 | Detect drift between production and its CI/CD origin, and correct any drifted resource. | operations engineers | operations | S-06 CICD-SEC-01, Recommendations item 6 | C-26 |
| R-0880 | Establish pipeline flow control so that no single human or program can ship sensitive code or artifacts without external verification. | managers | security | S-06 CICD-SEC-01, Recommendations item 7 | C-08 |
| R-0881 | Map all identities with their identity provider, granted permissions, used permissions and programmatic access methods. | security engineers | security | S-06 CICD-SEC-02, Recommendations item 1 | C-02 |
| R-0882 | Remove permissions that an identity no longer needs for its current work. | security engineers | security | S-06 CICD-SEC-02, Recommendations item 2 | C-02 |
| R-0883 | Define an inactivity period, and disable or delete accounts that exceed it. | security engineers | security | S-06 CICD-SEC-02, Recommendations item 3 | C-02 |
| R-0884 | Avoid local accounts in favour of a central identity provider; where local accounts remain, disable unneeded ones and enforce organizational policy on them. | security engineers | security | S-06 CICD-SEC-02, Recommendations item 4 | C-02 |
| R-0885 | Track external collaborators continuously, limit them to least privilege, set expiry dates where possible, and disable their access when the work ends. | security engineers | security | S-06 CICD-SEC-02, Recommendations item 5 | C-02 |
| R-0886 | Block personal or non-organizational email domains on source control, CI and pipeline platforms, monitor for them, and remove non-compliant users. | security engineers | security | S-06 CICD-SEC-02, Recommendations item 6 | C-02 |
| R-0887 | Disable self-registration and grant access only as needed. | security engineers | security | S-06 CICD-SEC-02, Recommendations item 7 | C-02 |
| R-0888 | Do not assign base permissions to all users or to large groups that users join automatically. | security engineers | security | S-06 CICD-SEC-02, Recommendations item 8 | C-02 |
| R-0889 | Avoid shared accounts; give each context its own account with only the permissions it requires. | security engineers | security | S-06 CICD-SEC-02, Recommendations item 9 | C-02 |
| R-0890 | Clients never fetch packages directly from the internet or from untrusted sources. | security engineers | security | S-06 CICD-SEC-03, Recommendations item 1 | C-15 |
| R-0891 | Route third-party packages through an internal proxy, not directly from the internet. | security engineers | security | S-06 CICD-SEC-03, Recommendations item 1 | C-10 |
| R-0892 | Where possible, block direct pulls from external repositories and point clients to internal, pre-vetted repositories. | security engineers | security | S-06 CICD-SEC-03, Recommendations item 3 | C-10 |
| R-0893 | Enforce the client configuration that points to internal repositories, using a verification mechanism. | operations engineers | operations | S-06 CICD-SEC-03, Recommendations item 4 | C-26 |
| R-0894 | Enable checksum and signature verification for pulled packages. | security engineers | security | S-06 CICD-SEC-03, Recommendations item 5 | C-17 |
| R-0895 | Do not configure clients to pull the latest version; pin pre-vetted versions or version ranges. | security engineers | security | S-06 CICD-SEC-03, Recommendations item 6 | C-10 |
| R-0896 | Lock package versions to stable, secure releases using each framework's techniques. | security engineers | security | S-06 CICD-SEC-03, Recommendations item 7 | C-10 |
| R-0897 | Register all private packages under the organization's scope. | security engineers | security | S-06 CICD-SEC-03, Recommendations item 8 | 5 |
| R-0898 | Make code that references a private package use that package's scope. | security engineers | security | S-06 CICD-SEC-03, Recommendations item 9 | 5 |
| R-0899 | Force clients to fetch organization-scoped packages only from the internal registry. | security engineers | security | S-06 CICD-SEC-03, Recommendations item 10 | C-10 |
| R-0900 | Run installation scripts in a separate context that has no access to secrets or sensitive resources. | security engineers | security | S-06 CICD-SEC-03, Recommendations item 11 | C-07 |
| R-0901 | Commit package manager configuration files to each internal project repository to override insecure client settings. | operations engineers | operations | S-06 CICD-SEC-03, Recommendations item 12 | C-26 |
| R-0902 | Do not publish the names of internal projects in public repositories. | security engineers | security | S-06 CICD-SEC-03, Recommendations item 13 | C-15 |
| R-0903 | Invest in detection, monitoring and mitigation, because fast incident identification limits damage. | operations engineers | operations | S-06 CICD-SEC-03, Recommendations item 14 | C-28 |
| R-0904 | Harden the relevant systems according to the CICD-SEC-07 guidance. | security engineers | security | S-06 CICD-SEC-03, Recommendations, last item | C-16 |
| R-0905 | Run pipelines that execute unreviewed code on isolated nodes that have no access to secrets or sensitive environments. | security engineers | security | S-06 CICD-SEC-04, Recommendations item 1 | C-07 |
| R-0906 | Assess whether pipelines must run for outside contributors on public repositories; avoid running pipelines from forks where possible; consider manual approval. | security engineers | security | S-06 CICD-SEC-04, Recommendations item 2 | C-15 |
| R-0907 | For pipelines that use secrets, give every branch that can trigger a pipeline a matching branch protection rule. | security engineers | security | S-06 CICD-SEC-04, Recommendations item 3 | C-03 |
| R-0908 | CI configuration files must be reviewed before the pipeline runs, or kept on a separate protected branch from the code being built. | security engineers | security | S-06 CICD-SEC-04, Must and should statements | C-03 |
| R-0909 | Remove source control repository permissions from users who do not need them. | security engineers | security | S-06 CICD-SEC-04, Recommendations item 5 | C-02 |
| R-0910 | Limit each pipeline to the credentials it needs, with the fewest privileges necessary. | security engineers | security | S-06 CICD-SEC-04, Recommendations item 6 | C-04 |
| R-0911 | Do not share one execution node across pipelines of different sensitivity levels; only pipelines with the same confidentiality level should share a node. | security engineers | security | S-06 CICD-SEC-05, Recommendations item 1 | C-07 |
| R-0912 | Scope secrets so that each pipeline and step can reach only the secrets it needs. | security engineers | security | S-06 CICD-SEC-05, Recommendations item 2 | C-04 |
| R-0913 | Reset each execution node to a clean state after every pipeline run. | security engineers | security | S-06 CICD-SEC-05, Recommendations item 3 | C-07 |
| R-0914 | Give the OS user that runs a job only the minimum permissions on the execution node. | security engineers | security | S-06 CICD-SEC-05, Recommendations item 4 | C-02 |
| R-0915 | Limit job permissions on the controller node, and run jobs on a separate dedicated node where applicable. | security engineers | security | S-06 CICD-SEC-05, Recommendations item 5 | C-02 |
| R-0916 | Keep execution nodes patched. | security engineers | security | S-06 CICD-SEC-05, Recommendations item 6 | C-16 |
| R-0917 | Segment the network so that execution nodes reach only the resources they need, and avoid unrestricted internet access where possible. | security engineers | security | S-06 CICD-SEC-05, Recommendations item 7 | C-16 |
| R-0918 | Run package installation scripts in a separate context that has no access to secrets or to resources from other build stages. | security engineers | security | S-06 CICD-SEC-05, Recommendations item 8 | C-07 |
| R-0919 | Continuously map credentials across the engineering ecosystem, and grant each one only the exact permissions its service needs. | security engineers | security | S-06 CICD-SEC-06, Recommendations item 1 | C-04 |
| R-0920 | Do not share the same credentials across multiple contexts. | security engineers | security | S-06 CICD-SEC-06, Recommendations item 2 | C-04 |
| R-0921 | Prefer temporary credentials; where static credentials are needed, rotate them on a schedule and detect stale ones. | security engineers | security | S-06 CICD-SEC-06, Recommendations item 3 | C-04 |
| R-0922 | Limit when credentials can be used, for example to a specific source IP or identity. | security engineers | security | S-06 CICD-SEC-06, Recommendations item 4 | C-04 |
| R-0923 | Detect secrets in code repositories with IDE plugins, scans on every push, and periodic scans of the repository and its past commits. | security engineers | security | S-06 CICD-SEC-06, Recommendations item 5 | C-04 |
| R-0924 | Scope CI/CD secrets so that each pipeline and step can access only what it requires. | security engineers | security | S-06 CICD-SEC-06, Recommendations item 6 | C-04 |
| R-0925 | Keep secrets out of build console output, and check that existing outputs contain no secrets. | security engineers | security | S-06 CICD-SEC-06, Recommendations item 7 | C-04 |
| R-0926 | Verify that secrets are removed from artifacts such as container image layers, binaries and Helm charts. | security engineers | security | S-06 CICD-SEC-06, Recommendations item 8 | C-04 |
| R-0927 | Understand where, how and by whom each credential is used, and whether pipelines can reach only the credentials they need. | security engineers | security | S-06 CICD-SEC-06, Description (imperative) | C-04 |
| R-0928 | Make credentials available only at run time, and only where they are needed. | security engineers | security | S-06 CICD-SEC-06, Description (imperative) | C-04 |
| R-0929 | Keep an inventory of every system and its version, each with a named owner, and check them continuously for known vulnerabilities. | security engineers | security | S-06 CICD-SEC-07, Recommendations item 1 | C-16 |
| R-0930 | When a security patch exists, apply it; when none exists, remove the component or limit access to it and its sensitive operations. | security engineers | security | S-06 CICD-SEC-07, Recommendations item 2 | C-11 |
| R-0931 | Restrict network access to each system so that it has only the access it needs. | security engineers | security | S-06 CICD-SEC-07, Recommendations item 3 | C-16 |
| R-0932 | Review all system configurations periodically, and confirm that each security-relevant setting is set optimally. | security engineers | security | S-06 CICD-SEC-07, Recommendations item 4 | C-16 |
| R-0933 | Grant pipeline execution nodes only the permissions they need. | security engineers | security | S-06 CICD-SEC-07, Recommendations item 5 | C-02 |
| R-0934 | Be cautious about giving engineers debug access to execution nodes. | software engineers | security | S-06 CICD-SEC-07, Recommendations item 6 | C-02 |
| R-0935 | Defenders must give strong attention to both the code and artifacts moving through the pipeline and the security posture of each system. | security engineers | security | S-06 CICD-SEC-07, Other must and should statements | C-16 |
| R-0936 | Organizations using SaaS CI/CD must still be highly diligent in configuring their solution securely. | managers | security | S-06 CICD-SEC-07, Other must and should statements | C-16 |
| R-0937 | Follow each CI/CD solution's unique security configurations and best practices. | security engineers | security | S-06 CICD-SEC-07, Other must and should statements | C-16 |
| R-0938 | Vet third parties before they get access to any part of the engineering ecosystem, and grant only the minimum permissions they need. | security engineers | security | S-06 CICD-SEC-08, Recommendations, Approval | C-20 |
| R-0939 | Keep continuous visibility into every third party connected to CI/CD, including how it connects, what permissions it holds and what it uses. | security engineers | security | S-06 CICD-SEC-08, Recommendations, Integration | C-20 |
| R-0940 | Limit each third party to the specific resources it needs, and remove unused or redundant permissions. | security engineers | security | S-06 CICD-SEC-08, Recommendations, Ongoing usage | C-02 |
| R-0941 | Build-integrated third parties should run inside a scoped context with limited access to secrets and code, with strict ingress and egress filtering. | security engineers | security | S-06 CICD-SEC-08, Recommendations, Build-time integrations | C-07 |
| R-0942 | Review integrated third parties periodically, and remove those no longer in use. | security engineers | security | S-06 CICD-SEC-08, Recommendations, Deprovisioning | C-20 |
| R-0943 | Governance controls should be implemented within every stage of the third-party lifecycle. | security engineers | security | S-06 CICD-SEC-08, Must and should statements | C-20 |
| R-0944 | Validate the integrity of resources at every stage, from development through production. | security engineers | security | S-06 CICD-SEC-09, Recommendations item 1 | C-17 |
| R-0945 | Sign each resource when it is generated, using external signing infrastructure. | security engineers | security | S-06 CICD-SEC-09, Recommendations item 2 | C-06 |
| R-0946 | Verify a resource's signature against its signing authority before later pipeline steps consume it. | security engineers | security | S-06 CICD-SEC-09, Recommendations item 3 | C-17 |
| R-0947 | Sign commits with a unique key per contributor, and block unsigned commits from moving down the pipeline. | security engineers | security | S-06 CICD-SEC-09, Recommendations item 4 | C-01 |
| R-0948 | Use signing and verification tools, such as in-toto, SLSA and Sigstore, to stop unverified software from advancing. | security engineers | security | S-06 CICD-SEC-09, Recommendations item 5 | C-06 |
| R-0949 | Detect configuration drift, such as cloud resources not managed by a signed infrastructure-as-code template. | operations engineers | operations | S-06 CICD-SEC-09, Recommendations item 6 | C-26 |
| R-0950 | Before using third-party resources fetched during build or deploy, compute their hash and compare it with the provider's officially published hash. | security engineers | security | S-06 CICD-SEC-09, Recommendations item 7 | C-10 |
| R-0951 | Organizations should consider the listed controls. | managers | quality | S-06 CICD-SEC-09, Must and should statements | C-48 |
| R-0952 | Catalogue every CI/CD system in use, including each instance of self-managed tools. | security engineers | security | S-06 CICD-SEC-10, Recommendations item 1 | C-16 |
| R-0953 | Enable the relevant log sources, because logging is not on by default, and cover both human and programmatic access. | operations engineers | operations | S-06 CICD-SEC-10, Recommendations item 2 | C-28 |
| R-0954 | Capture audit logs and application logs with equal priority. | operations engineers | operations | S-06 CICD-SEC-10, Recommendations item 3 | C-28 |
| R-0955 | Send logs to a central location, such as a SIEM, so that events can be correlated across systems. | operations engineers | operations | S-06 CICD-SEC-10, Recommendations item 4 | C-28 |
| R-0956 | Create alerts for anomalies and suspicious activity, both within each system and across the multi-system code-shipping process. | operations engineers | operations | S-06 CICD-SEC-10, Recommendations item 5 | C-28 |
| R-0957 | Security teams must build the ability to detect these attacks as they happen. | security engineers | operations | S-06 CICD-SEC-10, Description | C-28 |
| R-0958 | Consider the OWASP Proactive Controls as the starting point. | security engineers | security | S-07 project page | C-13 |
| R-0959 | Put security controls on building, deployment and automation software. | security engineers | security | S-07 project page | C-16 |
| R-0960 | Teams should combine one framework for baseline practices, one for maturity, one for pipeline adoption, and one for supply-chain security. | security engineers | security | S-07 0-3-Frameworks-and-Standards.md | C-22 |
| R-0961 | Teams should choose one maturity model, SAMM or DSOMM, and run a real assessment before buying tools. | security engineers | security | S-07 0-3-Frameworks-and-Standards.md | C-22 |
| R-0962 | Teams should map controls to SSDF mainly when there is a regulatory need, otherwise build the program first. | security engineers | security | S-07 0-3-Frameworks-and-Standards.md | C-22 |
| R-0963 | Teams should treat SLSA as an engineering target, start at Level 1, reach Level 2, and measure progress. | security engineers | security | S-07 0-3-Frameworks-and-Standards.md | C-22 |
| R-0964 | Teams should let the pipeline generate compliance evidence natively. | security engineers | security | S-07 0-3-Frameworks-and-Standards.md | C-23 |
| R-0965 | The source states that in-scope entities under NIS2 Article 21 must manage supply-chain security. | security engineers | security | S-07 0-3-Frameworks-and-Standards.md | C-20 |
| R-0966 | Developers should write secure code using the Proactive Controls. | software engineers | quality | S-07 1-1-2-Roles-and-Responsibilities.md | C-40 |
| R-0967 | Developers should run pre-commit hooks and IDE security plugins and fix findings before a pull request. | software engineers | security | S-07 1-1-2-Roles-and-Responsibilities.md | C-14 |
| R-0968 | Developers should take part in threat modeling and secure code review. | software engineers | security | S-07 1-1-2-Roles-and-Responsibilities.md | C-13 |
| R-0969 | Developers should write security acceptance criteria. | software engineers | security | S-07 1-1-2-Roles-and-Responsibilities.md | C-13 |
| R-0970 | Developers should review AI-generated code as rigorously as human-written code and remain accountable for it. | software engineers | security | S-07 1-1-2-Roles-and-Responsibilities.md | C-03 |
| R-0971 | AppSec should define security requirements, policies and gate thresholds. | security engineers | security | S-07 1-1-2-Roles-and-Responsibilities.md | C-13 |
| R-0972 | AppSec should own and tune the scanning tools. | security engineers | security | S-07 1-1-2-Roles-and-Responsibilities.md | C-14 |
| R-0973 | Platform engineers should harden CI/CD templates with least-privilege tokens and pinned dependencies. | build platform operators | operations | S-07 1-1-2-Roles-and-Responsibilities.md | C-33 |
| R-0974 | SRE and operations should own runtime security monitoring, SIEM alerting and incident runbooks. | operations engineers | operations | S-07 1-1-2-Roles-and-Responsibilities.md | C-29 |
| R-0975 | Security architects should design reusable secure patterns and sign off major architectural decisions. | security engineers | quality | S-07 1-1-2-Roles-and-Responsibilities.md | C-47 |
| R-0976 | Product owners should prioritise security work and ensure abuse cases are in the definition of done. | managers | security | S-07 1-1-2-Roles-and-Responsibilities.md | C-13 |
| R-0977 | GRC should map pipeline controls to frameworks and manage audit evidence and risk acceptances. | quality assurance staff | quality | S-07 1-1-2-Roles-and-Responsibilities.md | C-42 |
| R-0978 | The CISO should set strategy and risk appetite and fund security work. | security engineers | quality | S-07 1-1-2-Roles-and-Responsibilities.md | C-48 |
| R-0979 | A RACI matrix should be defined per activity. | security engineers | security | S-07 1-1-2-Roles-and-Responsibilities.md | C-19 |
| R-0980 | Platform teams should keep golden templates current, with clear ownership for updates. | build platform operators | operations | S-07 1-1-2-Roles-and-Responsibilities.md | C-33 |
| R-0981 | Threat modeling should run during design, before code is written. | security engineers | security | S-07 2-1-1-Threat-modeling.md | C-13 |
| R-0982 | Every trust-boundary crossing should be treated as a candidate threat. | security engineers | security | S-07 2-1-1-Threat-modeling.md | C-13 |
| R-0983 | The threat model should be updated when a change crosses a trust boundary, adds an integration, or handles new sensitive data. | security engineers | security | S-07 2-1-1-Threat-modeling.md | C-13 |
| R-0984 | Threat models should be stored as version-controlled code and integrated into CI. | security engineers | security | S-07 2-1-1-Threat-modeling.md | C-13 |
| R-0985 | Each identified threat should become a backlog item with an owner, and unmitigated threats need an explicit risk-acceptance decision. | security engineers | security | S-07 2-1-1-Threat-modeling.md | C-13 |
| R-0986 | Security-sensitive changes should get deeper review by a security champion or trained reviewer. | security engineers | security | S-07 2-2-3-Secure-Code-Review.md | C-03 |
| R-0987 | CI workflows, Dockerfiles, infrastructure manifests and release scripts should be reviewed as production code. | security engineers | security | S-07 2-2-3-Secure-Code-Review.md | C-03 |
| R-0988 | New or upgraded dependencies should be checked for provenance, maintainers and install scripts. | security engineers | security | S-07 2-2-3-Secure-Code-Review.md | C-20 |
| R-0989 | Large or unusual changes should be split or get a second reviewer. | security engineers | security | S-07 2-2-3-Secure-Code-Review.md | C-03 |
| R-0990 | The review checklist should be anchored to the OWASP Top 10 and ASVS. | security engineers | security | S-07 2-2-3-Secure-Code-Review.md | C-03 |
| R-0991 | Pull request templates should include a security section, and CODEOWNERS approval should be enforced on sensitive paths. | security engineers | security | S-07 2-2-3-Secure-Code-Review.md | C-03 |
| R-0992 | SAST, SCA and secret scanning should run on every pull request. | security engineers | security | S-07 2-2-3-Secure-Code-Review.md | C-14 |
| R-0993 | AI-generated code should be reviewed at least as strictly as code from an unknown contributor. | security engineers | security | S-07 2-2-3-Secure-Code-Review.md | C-03 |
| R-0994 | Authors must be able to explain their changes before merge. | software engineers | security | S-07 2-2-3-Secure-Code-Review.md | C-03 |
| R-0995 | A human with accountability should approve security-relevant changes, even when AI tools assist. | security engineers | security | S-07 2-2-3-Secure-Code-Review.md | C-03 |
| R-0996 | Independent approval should be enforced, and stale approvals should be dismissed when new commits arrive. | security engineers | security | S-07 2-2-3-Secure-Code-Review.md | C-03 |
| R-0997 | Secure coding training and periodic exercises should be provided. | security engineers | security | S-07 2-2-3-Secure-Code-Review.md | C-19 |
| R-0998 | Security gates should decide on risk such as severity, exploitability and reachability, not on raw finding counts. | security engineers | security | S-07 2-3-5-Security-Gates.md | C-14 |
| R-0999 | Existing issues should be baselined, and gates should block only on new findings. | security engineers | security | S-07 2-3-5-Security-Gates.md | C-14 |
| R-1000 | Blocked gates should explain what failed, where, and how to fix it. | security engineers | security | S-07 2-3-5-Security-Gates.md | C-14 |
| R-1001 | Risk acceptance should be documented, time-limited, and have a named owner. | software engineers | quality | S-07 2-3-5-Security-Gates.md | C-45 |
| R-1002 | False positives should be treated as defects in the gate. | security engineers | security | S-07 2-3-5-Security-Gates.md | C-14 |
| R-1003 | Advisory scans should run before blocking scans. | security engineers | security | S-07 2-3-5-Security-Gates.md | C-14 |
| R-1004 | Gates should block merges, artifact promotion, releases and deployments on defined severity thresholds. | software engineers | quality | S-07 2-3-5-Security-Gates.md | C-37 |
| R-1005 | Gate policy should be kept in one version-controlled config. | security engineers | security | S-07 2-3-5-Security-Gates.md | C-14 |
| R-1006 | Gates should roll out gradually: warn first, then block critical, then critical and high. | security engineers | security | S-07 2-3-5-Security-Gates.md | C-14 |
| R-1007 | A gate should fail closed when a scanner produces no report, and a scanner error should be distinct from a failed scan. | security engineers | security | S-07 2-3-5-Security-Gates.md | C-14 |
| R-1008 | Scanner output should be normalised, ideally to SARIF, before one gate decision. | security engineers | security | S-07 2-3-5-Security-Gates.md | C-14 |
| R-1009 | The exit-code meaning of each scanner should be checked. | security engineers | security | S-07 2-3-5-Security-Gates.md | C-14 |
| R-1010 | Required status checks should be enforced through branch protection. | security engineers | security | S-07 2-3-5-Security-Gates.md | C-03 |
| R-1011 | Scanner tools and CI actions should be pinned to versions or digests, not floating tags. | security engineers | security | S-07 2-3-5-Security-Gates.md | C-10 |
| R-1012 | Every suppression should be tracked in a central exception register. | operations engineers | operations | S-07 2-3-5-Security-Gates.md | C-31 |
| R-1013 | Emergency bypasses should use an audited path with platform-enforced approval and a ticket, never silent continue-on-error. | operations engineers | operations | S-07 2-3-5-Security-Gates.md | C-29 |
| R-1014 | Exceptions should expire automatically and record reason, approver, ticket and expiry date. | operations engineers | operations | S-07 2-3-5-Security-Gates.md | C-31 |
| R-1015 | Exceptions should not all be routed through the security team. | security engineers | security | S-07 2-3-5-Security-Gates.md | C-19 |
| R-1016 | SBOMs should be generated during the build. | security engineers | security | S-07 2-3-6-1-SBOM.md | C-09 |
| R-1017 | At least one standard SBOM format, SPDX or CycloneDX, should be published. | security engineers | security | S-07 2-3-6-1-SBOM.md | C-09 |
| R-1018 | SBOMs should be produced at several layers: lock files, container images and final artifacts. | security engineers | security | S-07 2-3-6-1-SBOM.md | C-09 |
| R-1019 | SBOMs should be stored with the artifact, ideally as signed attestations referencing images by digest. | security engineers | security | S-07 2-3-6-1-SBOM.md | C-06 |
| R-1020 | SBOMs should include the minimum data elements listed on the page. | security engineers | security | S-07 2-3-6-1-SBOM.md | C-09 |
| R-1021 | Stored SBOMs should be re-checked continuously against new vulnerability data. | security engineers | security | S-07 2-3-6-1-SBOM.md | C-11 |
| R-1022 | VEX documents should be published. | security engineers | security | S-07 2-3-6-1-SBOM.md | C-09 |
| R-1023 | SBOMs should be managed centrally and should be queryable before an incident. | security engineers | security | S-07 2-3-6-1-SBOM.md | C-09 |
| R-1024 | One SBOM format should be used across the toolchain, and static PDF SBOMs should be avoided. | security engineers | security | S-07 2-3-6-1-SBOM.md | C-09 |
| R-1025 | IAST should run in QA or test environments, not in production. | security engineers | security | S-07 2-4-1-Interactive-Application-Security-Testing.md | C-14 |
| R-1026 | IAST results should feed the security gates and the vulnerability dashboard, and IAST should be paired with DAST. | security engineers | security | S-07 2-4-1-Interactive-Application-Security-Testing.md | C-11 |
| R-1027 | Candidate IAST agents should be evaluated against the team's own stack before purchase. | security engineers | security | S-07 2-4-1-Interactive-Application-Security-Testing.md | C-20 |
| R-1028 | IAST agent versions should be pinned and updated on a schedule. | security engineers | security | S-07 2-4-1-Interactive-Application-Security-Testing.md | C-10 |
| R-1029 | Promotion should be blocked automatically when new high or critical findings appear, and tickets should be created. | software engineers | quality | S-07 2-4-1-Interactive-Application-Security-Testing.md | C-37 |
| R-1030 | Licensing terms should be clarified before a vendor is selected. | security engineers | security | S-07 2-4-1-Interactive-Application-Security-Testing.md | C-20 |
| R-1031 | IAST should be kept alongside SAST and not replace it. | security engineers | security | S-07 2-4-1-Interactive-Application-Security-Testing.md | C-14 |
| R-1032 | A final security gate should check for unresolved critical or high findings, unless exceptions are documented and approved. | quality assurance staff | quality | S-07 2-5-1-Release.md | C-42 |
| R-1033 | An SBOM and build provenance should be attached to each release artifact. | security engineers | security | S-07 2-5-1-Release.md | C-06 |
| R-1034 | Release artifacts should be cryptographically signed. | security engineers | security | S-07 2-5-1-Release.md | C-06 |
| R-1035 | Release approval should be recorded and linked to change management. | operations engineers | operations | S-07 2-5-1-Release.md | C-31 |
| R-1036 | Security release notes should be published, and customer-facing software should publish CSAF or VEX. | security engineers | security | S-07 2-5-1-Release.md | C-12 |
| R-1037 | Artifacts should be immutable, deployed by digest, and release tags protected. | security engineers | security | S-07 2-5-1-Release.md | C-10 |
| R-1038 | Registry pushes should be restricted to CI via OIDC, humans read-only, and stored images re-scanned. | security engineers | security | S-07 2-5-1-Release.md | C-04 |
| R-1039 | Artifacts should be built once and promoted, with signature and provenance re-verified before each promotion. | operations engineers | operations | S-07 2-5-1-Release.md | C-24 |
| R-1040 | Low-risk approvals may be automated, and high-risk releases should keep formal review. | operations engineers | operations | S-07 2-5-1-Release.md | C-31 |
| R-1041 | The git repository should be the single source of truth for deployments, changed through reviewed pull requests. | operations engineers | operations | S-07 2-6-1-Deploy.md | C-26 |
| R-1042 | A reconciler should correct drift, and rollback should use git revert. | operations engineers | operations | S-07 2-6-1-Deploy.md | C-25 |
| R-1043 | Images should be pinned by digest, not mutable tags. | security engineers | security | S-07 2-6-1-Deploy.md | C-10 |
| R-1044 | Rollouts should be gradual, using canary, blue-green, flags and automated rollback on health criteria. | operations engineers | operations | S-07 2-6-1-Deploy.md | C-25 |
| R-1045 | Deploy identities should be scoped to the target environment and workloads, with short-lived OIDC credentials. | security engineers | security | S-07 2-6-1-Deploy.md | C-04 |
| R-1046 | Secrets should never be baked into images or manifests, and should be injected at runtime. | security engineers | security | S-07 2-6-1-Deploy.md | C-04 |
| R-1047 | The same base image and configuration should be used in all environments, and controls should never be disabled in lower environments. | operations engineers | operations | S-07 2-6-1-Deploy.md | C-24 |
| R-1048 | Non-compliant images should be blocked at admission, not only flagged. | security engineers | security | S-07 2-6-1-Deploy.md | C-17 |
| R-1049 | Only signed artifacts with acceptable provenance should be admitted. | security engineers | security | S-07 2-6-1-Deploy.md | C-17 |
| R-1050 | A deadline should be set to move admission control from warn to enforce. | security engineers | security | S-07 2-6-1-Deploy.md | C-17 |
| R-1051 | Rollback should be tested in staging before major production deployments. | operations engineers | operations | S-07 2-6-1-Deploy.md | C-25 |
| R-1052 | Authentication, authorization, validation failures, admin changes, sensitive data access and deployment events should be logged. | security engineers | security | S-07 2-7-2-Logging-and-Monitoring.md | C-02 |
| R-1053 | Secrets, passwords, tokens, session cookies and card numbers should not be logged. | security engineers | security | S-07 2-7-2-Logging-and-Monitoring.md | C-04 |
| R-1054 | Logs should be structured, with consistent event names, correlation IDs and UTC timestamps. | operations engineers | operations | S-07 2-7-2-Logging-and-Monitoring.md | C-28 |
| R-1055 | Trace context should be propagated with OpenTelemetry. | operations engineers | operations | S-07 2-7-2-Logging-and-Monitoring.md | C-28 |
| R-1056 | Logs should be centralised in tamper-resistant append-only storage, clocks synchronised with NTP, and log gaps alerted. | operations engineers | operations | S-07 2-7-2-Logging-and-Monitoring.md | C-28 |
| R-1057 | Detection rules should be managed as code under version control and tested. | operations engineers | operations | S-07 2-7-2-Logging-and-Monitoring.md | C-26 |
| R-1058 | Detection rules should be mapped to MITRE ATT&CK techniques. | operations engineers | operations | S-07 2-7-2-Logging-and-Monitoring.md | C-28 |
| R-1059 | Every alert should be actionable, specific, calibrated and linked to a runbook. | operations engineers | operations | S-07 2-7-2-Logging-and-Monitoring.md | C-28 |
| R-1060 | DEBUG-level logging should be avoided in production. | operations engineers | operations | S-07 2-7-2-Logging-and-Monitoring.md | C-28 |
| R-1061 | Create a formal definition of the build process so that it is consistent and repeatable | software engineers | quality | S-08 /model/implementation/secure-build/, Stream A, Maturity 1 | C-44 |
| R-1062 | Automate the build pipeline and secure the tooling used, and add security checks to the pipeline | security engineers | security | S-08 /model/implementation/secure-build/, Stream A, Maturity 2 | C-05 |
| R-1063 | Define mandatory security checks in the build process, and make the build fail for non-compliant artifacts | software engineers | quality | S-08 /model/implementation/secure-build/, Stream A, Maturity 3 | C-37 |
| R-1064 | Create records of the Bill of Materials of applications and analyze them opportunistically | security engineers | security | S-08 /model/implementation/secure-build/, Stream B, Maturity 1 | C-09 |
| R-1065 | Evaluate used dependencies and react in time to situations that pose risk to applications | software engineers | quality | S-08 /model/implementation/secure-build/, Stream B, Maturity 2 | C-51 |
| R-1066 | Analyze used dependencies for security issues in a way comparable to the own code | security engineers | security | S-08 /model/implementation/secure-build/, Stream B, Maturity 3 | C-11 |
| R-1067 | Formalize the deployment process and secure its tooling and processes | operations engineers | operations | S-08 /model/implementation/secure-deployment/, Stream A, Level 1 | C-24 |
| R-1068 | Automate deployment across all stages and add sensible security verification tests | operations engineers | operations | S-08 /model/implementation/secure-deployment/, Stream A, Level 2 | C-24 |
| R-1069 | Automatically verify the integrity of all deployed software, whether built internally or externally | security engineers | security | S-08 /model/implementation/secure-deployment/, Stream A, Level 3 | C-17 |
| R-1070 | Adequately trained non-developers own deployment, to enforce separation of duties | software engineers | security | S-08 /model/implementation/secure-deployment/, Roles and concerns | C-08 |
| R-1071 | Add basic protections that limit access to production secrets | security engineers | security | S-08 /model/implementation/secure-deployment/, Stream B, Level 1 | C-04 |
| R-1072 | Inject secrets during deployment from hardened storage, and audit all human access to them | security engineers | security | S-08 /model/implementation/secure-deployment/, Stream B, Level 2 | C-04 |
| R-1073 | Improve the secret lifecycle by regularly regenerating secrets and ensuring they are used properly | security engineers | security | S-08 /model/implementation/secure-deployment/, Stream B, Level 3 | C-04 |
| R-1074 | Set up structured tracking of security defects and use that data for informed decisions | quality assurance staff | quality | S-08 /model/implementation/defect-management/, Stream A, Maturity 1 | C-43 |
| R-1075 | Apply one consistent severity rating across the organization and define remediation service levels for each severity class | security engineers | security | S-08 /model/implementation/defect-management/, Stream A, Maturity 2 | C-11 |
| R-1076 | Enforce those remediation service levels and connect the defect management system to other relevant tools | security engineers | security | S-08 /model/implementation/defect-management/, Stream A, Maturity 3 | C-11 |
| R-1077 | Periodically review past security defects and identify quick wins from basic metrics | quality assurance staff | quality | S-08 /model/implementation/defect-management/, Stream B, Maturity 1 | C-43 |
| R-1078 | Collect standardized defect management metrics and use them to prioritize centrally driven initiatives | managers | quality | S-08 /model/implementation/defect-management/, Stream B, Maturity 2 | C-52 |
| R-1079 | Continuously refine the metrics and correlate them with other data sources | managers | quality | S-08 /model/implementation/defect-management/, Stream B, Maturity 3 | C-52 |
| R-1080 | Identify application and infrastructure components and review them for basic security provisioning | software engineers | quality | S-08 /model/verification/architecture-assessment/, Stream A, Maturity 1 | C-47 |
| R-1081 | Validate the security mechanisms of the architecture | software engineers | quality | S-08 /model/verification/architecture-assessment/, Stream A, Maturity 2 | C-47 |
| R-1082 | Review the effectiveness of architecture components | software engineers | quality | S-08 /model/verification/architecture-assessment/, Stream A, Maturity 3 | C-47 |
| R-1083 | Review the architecture ad hoc for unmitigated security threats | security engineers | security | S-08 /model/verification/architecture-assessment/, Stream B, Maturity 1 | C-13 |
| R-1084 | Analyze the architecture for known threats | security engineers | security | S-08 /model/verification/architecture-assessment/, Stream B, Maturity 2 | C-13 |
| R-1085 | Feed review results back into enterprise architecture, design principles and patterns, security solutions and reference architectures | software engineers | quality | S-08 /model/verification/architecture-assessment/, Stream B, Maturity 3 | C-47 |
| R-1086 | Test for software security controls | software engineers | quality | S-08 /model/verification/requirements-driven-testing/, Stream A, Maturity 1 | C-38 |
| R-1087 | Derive test cases from known security requirements | software engineers | quality | S-08 /model/verification/requirements-driven-testing/, Stream A, Maturity 2 | C-46 |
| R-1088 | Perform regression testing with security unit tests | software engineers | quality | S-08 /model/verification/requirements-driven-testing/, Stream A, Maturity 3 | C-37 |
| R-1089 | Perform security fuzz testing | security engineers | security | S-08 /model/verification/requirements-driven-testing/, Stream B, Maturity 1 | C-14 |
| R-1090 | Create and test abuse cases and business logic flaw tests | security engineers | security | S-08 /model/verification/requirements-driven-testing/, Stream B, Maturity 2 | C-14 |
| R-1091 | Run denial-of-service and security stress testing | software engineers | quality | S-08 /model/verification/requirements-driven-testing/, Stream B, Maturity 3 | C-38 |
| R-1092 | Use automated security testing tools | security engineers | security | S-08 /model/verification/security-testing/, Stream A, Maturity 1 | C-14 |
| R-1093 | Employ application-specific security testing automation | security engineers | security | S-08 /model/verification/security-testing/, Stream A, Maturity 2 | C-14 |
| R-1094 | Integrate automated security testing into the build and deploy process | security engineers | security | S-08 /model/verification/security-testing/, Stream A, Maturity 3 | C-14 |
| R-1095 | Perform manual security testing of high-risk components | security engineers | security | S-08 /model/verification/security-testing/, Stream B, Maturity 1 | C-14 |
| R-1096 | Conduct manual penetration testing | security engineers | security | S-08 /model/verification/security-testing/, Stream B, Maturity 2 | C-14 |
| R-1097 | Integrate security testing into the development process | security engineers | security | S-08 /model/verification/security-testing/, Stream B, Maturity 3 | C-14 |
| R-1098 | Customize the automated tests for each application and run them more often | security engineers | security | S-08 /model/verification/security-testing/, Reader instructions | C-14 |
| R-1099 | Prioritize manual reviews by component risk, recent relevant changes, or upcoming major releases | security engineers | security | S-08 /model/verification/security-testing/, Reader instructions | C-14 |
| R-1100 | Consider external expertise through bug bounty programs | security engineers | security | S-08 /model/verification/security-testing/, Reader instructions | C-12 |
| R-1101 | Use available log data to perform best-effort detection of possible incidents | operations engineers | operations | S-08 /model/operations/incident-management/, Stream A, Maturity 1 | C-28 |
| R-1102 | Follow a documented, established detection process with emphasis on automated log evaluation | operations engineers | operations | S-08 /model/operations/incident-management/, Stream A, Maturity 2 | C-28 |
| R-1103 | Use a proactively managed detection process | operations engineers | operations | S-08 /model/operations/incident-management/, Stream A, Maturity 3 | C-29 |
| R-1104 | Identify roles and responsibilities for incident response | security engineers | security | S-08 /model/operations/incident-management/, Stream B, Maturity 1 | C-19 |
| R-1105 | Establish a formal response process and ensure staff are trained for their roles | operations engineers | operations | S-08 /model/operations/incident-management/, Stream B, Maturity 2 | C-29 |
| R-1106 | Employ a dedicated, well-trained incident response team | operations engineers | operations | S-08 /model/operations/incident-management/, Stream B, Maturity 3 | C-29 |
| R-1107 | Perform best-effort hardening using readily available information | security engineers | security | S-08 /model/operations/environment-management/, Stream A, Level 1 | C-16 |
| R-1108 | Perform consistent hardening that follows established baselines and guidance | security engineers | security | S-08 /model/operations/environment-management/, Stream A, Level 2 | C-16 |
| R-1109 | Actively monitor configurations for baseline non-conformance and handle detected cases as security defects | security engineers | security | S-08 /model/operations/environment-management/, Stream A, Level 3 | C-16 |
| R-1110 | Perform best-effort patching of system and application components | security engineers | security | S-08 /model/operations/environment-management/, Stream B, Level 1 | C-11 |
| R-1111 | Patch regularly across the full stack and deliver patches to customers in a timely way | security engineers | security | S-08 /model/operations/environment-management/, Stream B, Level 2 | C-11 |
| R-1112 | Actively monitor update status, treat missing patches as security defects, and proactively obtain vulnerability and update information | security engineers | security | S-08 /model/operations/environment-management/, Stream B, Level 3 | C-11 |
| R-1113 | Monitor vulnerability reports and perform orderly, timely patching across affected systems | security engineers | security | S-08 /model/operations/environment-management/, Practice description | C-11 |
| R-1114 | Implement basic data protection practices | security engineers | security | S-08 /model/operations/operational-management/, Stream A, Maturity 1 | C-18 |
| R-1115 | Develop a data catalog and establish a data protection policy | security engineers | security | S-08 /model/operations/operational-management/, Stream A, Maturity 2 | C-18 |
| R-1116 | Automate detection of policy non-compliance, audit compliance periodically, and regularly review and update the data catalog and policy | security engineers | security | S-08 /model/operations/operational-management/, Stream A, Maturity 3 | C-18 |
| R-1117 | Decommission unused applications and services as they are identified, and manage customer upgrades and migrations individually | operations engineers | operations | S-08 /model/operations/operational-management/, Stream B, Maturity 1 | C-36 |
| R-1118 | Develop repeatable decommissioning processes and manage legacy migration roadmaps for customers | operations engineers | operations | S-08 /model/operations/operational-management/, Stream B, Maturity 2 | C-36 |
| R-1119 | Proactively manage migration roadmaps for end-of-life dependencies and legacy versions of delivered software | operations engineers | operations | S-08 /model/operations/operational-management/, Stream B, Maturity 3 | C-36 |
| R-1120 | Answer No to a question if its quality criteria are not completely met | software engineers | security | S-08 /assessment/, Scoring input | C-22 |
| R-1121 | Read the Quick Start Guide before beginning | software engineers | quality | S-08 /assessment/, Instructions to the reader | C-45 |
| R-1122 | Read the Assessment Guide before starting a self-assessment | security engineers | security | S-08 /assessment/, Instructions to the reader | C-22 |
| R-1123 | Download a SAMM Toolbox version | security engineers | security | S-08 /assessment/, Instructions to the reader | C-22 |
| R-1124 | Evaluate each question's criteria in the Interview tab | security engineers | security | S-08 /assessment/, Instructions to the reader | C-22 |
| R-1125 | Optionally set improvement targets and build a roadmap in the Toolbox | security engineers | security | S-08 /assessment/, Instructions to the reader | C-22 |
| R-1126 | Consider sharing assessment data with the Benchmark initiative | security engineers | security | S-08 /assessment/, Instructions to the reader | C-22 |
| R-1127 | Projects should meet the controls to show a strong security posture. | project maintainers | security | S-09 home page, intro | C-22 |
| R-1128 | Projects should meet the controls to show a strong security posture. | project maintainers | security | S-09 FAQ, intro | duplicate: R-1127 |
| R-1129 | Projects are encouraged to adhere to Level 1 at minimum. | project maintainers | security | S-09 FAQ, Required level | C-22 |
| R-1130 | Foundations with maturity criteria should evaluate their lowest criteria tier for security and adjust it to match Level 1 where appropriate. | project maintainers | security | S-09 FAQ, Required level | C-22 |
| R-1131 | Projects are encouraged to state compliance as of a specific date, against a specific version and level. | project maintainers | security | S-09 FAQ, Expiration | C-22 |
| R-1132 | Adopters are strongly encouraged to review how a project implemented the Baseline and help it level up. | consumers | security | S-09 FAQ, what it should not be used for | C-22 |
| R-1133 | Downstream consumers should specify their compliance against a specific version. | consumers | security | S-09 home page, compliance statement | C-22 |
| R-1134 | Only the version labeled as current should be used for new compliance efforts. | project maintainers | security | S-09 home page, compliance statement | C-22 |
| R-1135 | Users who read or change sensitive resources in the authoritative repository must use multi-factor authentication. Levels 1 to 3. | consumers | security | S-09 versions page, Access Control, AC-01.01 | C-02 |
| R-1136 | New collaborators must receive manual permission assignment, or the lowest available privileges by default. Levels 1 to 3. | project maintainers | security | S-09 versions page, Access Control, AC-02.01 | C-02 |
| R-1137 | A direct commit to the primary branch must be blocked by an enforcement mechanism. Levels 1 to 3. | project maintainers | security | S-09 versions page, Access Control, AC-03.01 | C-03 |
| R-1138 | Deleting the primary branch must be treated as sensitive and must need explicit confirmation of intent. Levels 1 to 3. | project maintainers | security | S-09 versions page, Access Control, AC-03.02 | C-01 |
| R-1139 | CI/CD tasks with no permissions set must default to the lowest permissions granted in the pipeline. Levels 2 and 3. | project maintainers | security | S-09 versions page, Access Control, AC-04.01 | C-02 |
| R-1140 | Jobs that are granted permissions must receive only the minimum privileges they need. Level 3. | project maintainers | security | S-09 versions page, Access Control, AC-04.02 | C-02 |
| R-1141 | Pipelines that use untrusted metadata must sanitize and validate it before use. Levels 1 to 3. | project maintainers | security | S-09 versions page, Build and Release, BR-01.01 | C-15 |
| R-1142 | Pipelines that run untrusted code snapshots must not access privileged CI/CD credentials or assets. Levels 1 to 3. | project maintainers | security | S-09 versions page, Build and Release, BR-01.03 | C-15 |
| R-1143 | Pipelines that accept trusted collaborator input must sanitize and validate it. Level 3. | project maintainers | security | S-09 versions page, Build and Release, BR-01.04 | C-15 |
| R-1144 | Each official release must have a unique version identifier. Levels 2 and 3. | project maintainers | operations | S-09 versions page, Build and Release, BR-02.01 | C-32 |
| R-1145 | All assets in an official release must link to the release identifier or to a unique asset identifier. Level 3. | project maintainers | operations | S-09 versions page, Build and Release, BR-02.02 | C-32 |
| R-1146 | Official project URIs must be delivered only over encrypted channels. Levels 1 to 3. | project maintainers | security | S-09 versions page, Build and Release, BR-03.01 | C-18 |
| R-1147 | Official distribution channels must be protected against adversary-in-the-middle attacks by cryptographic authentication. Levels 1 to 3. | project maintainers | security | S-09 versions page, Build and Release, BR-03.02 | C-17 |
| R-1148 | Official releases must include a descriptive log of functional and security changes. Levels 2 and 3. | project maintainers | operations | S-09 versions page, Build and Release, BR-04.01 | C-32 |
| R-1149 | Build and release pipelines must use standardized dependency tooling where it is available. Levels 2 and 3. | project maintainers | quality | S-09 versions page, Build and Release, BR-05.01 | C-44 |
| R-1150 | Official releases must be signed, or listed in a signed manifest with the hashes of each asset. Levels 2 and 3. | project maintainers | security | S-09 versions page, Build and Release, BR-06.01 | C-06 |
| R-1151 | The project must prevent unencrypted sensitive data, such as secrets and credentials, from being stored in the VCS by accident. Level 1. | project maintainers | security | S-09 versions page, Build and Release, BR-07.01 | C-04 |
| R-1152 | The project must have a policy for managing secrets and credentials that covers storage, access and rotation. Level 3. | project maintainers | security | S-09 versions page, Build and Release, BR-07.02 | C-04 |
| R-1153 | After a release, the documentation must include user guides for all basic functions. Levels 1 to 3. | consumers | quality | S-09 versions page, Documentation, DO-01.01 | C-45 |
| R-1154 | After a release, the documentation must include a guide for reporting defects. Levels 1 to 3. | project maintainers | security | S-09 versions page, Documentation, DO-02.01 | C-12 |
| R-1155 | After a release, the documentation must explain how to verify the integrity and authenticity of release assets. Level 3. | project maintainers | security | S-09 versions page, Documentation, DO-03.01 | C-17 |
| R-1156 | After a release, the documentation must explain how to verify the expected identity of the author or process. Level 3. | project maintainers | security | S-09 versions page, Documentation, DO-03.02 | C-17 |
| R-1157 | After a release, the documentation must state the scope and duration of support for each release. Level 3. | project maintainers | operations | S-09 versions page, Documentation, DO-04.01 | C-36 |
| R-1158 | After a release, the documentation must state when releases or versions stop receiving security updates. Level 3. | project maintainers | operations | S-09 versions page, Documentation, DO-05.01 | C-36 |
| R-1159 | After a release, the documentation must describe how dependencies are selected, obtained and tracked. Levels 2 and 3. | project maintainers | security | S-09 versions page, Documentation, DO-06.01 | C-20 |
| R-1160 | The documentation must explain how to build the software, including its libraries, frameworks, SDKs and dependencies. Levels 2 and 3. | project maintainers | quality | S-09 versions page, Documentation, DO-07.01 | C-44 |
| R-1161 | The documentation must list the project members who have access to sensitive resources. Levels 2 and 3. | project maintainers | quality | S-09 versions page, Governance, GV-01.01 | C-50 |
| R-1162 | The documentation must describe the roles and responsibilities of project members. Levels 2 and 3. | project maintainers | quality | S-09 versions page, Governance, GV-01.02 | C-50 |
| R-1163 | The project must have one or more public discussion mechanisms for proposed changes and usage problems. Levels 1 to 3. | project maintainers | quality | S-09 versions page, Governance, GV-02.01 | C-50 |
| R-1164 | The documentation must explain the contribution process, or state that public contributions are not accepted. Levels 1 to 3. | project maintainers | quality | S-09 versions page, Governance, GV-03.01 | C-50 |
| R-1165 | The documentation must include a guide for code contributors that states the requirements for acceptable contributions. Levels 2 and 3. | project maintainers | quality | S-09 versions page, Governance, GV-03.02 | C-50 |
| R-1166 | The documentation must include a policy that requires review of code collaborators before they receive escalated permissions to sensitive resources. Level 3. | project maintainers | security | S-09 versions page, Governance, GV-04.01 | C-02 |
| R-1167 | The VCS must require every contributor to assert legal authority to contribute, on every commit. Levels 2 and 3. | project maintainers | quality | S-09 versions page, Legal, LE-01.01 | C-50 |
| R-1168 | The source code license must meet the OSI Open Source Definition or the FSF Free Software Definition. Levels 1 to 3. | project maintainers | quality | S-09 versions page, Legal, LE-02.01 | C-50 |
| R-1169 | The license for released software assets must meet the OSI or FSF definition. Levels 1 to 3. | project maintainers | quality | S-09 versions page, Legal, LE-02.02 | C-50 |
| R-1170 | The source code license must be kept in a LICENSE, COPYING, LICENSES/ or LICENSE/ location in the repository. Levels 1 to 3. | project maintainers | quality | S-09 versions page, Legal, LE-03.01 | C-50 |
| R-1171 | The license for released assets must be included in the released source code or next to the release assets. Levels 1 to 3. | project maintainers | quality | S-09 versions page, Legal, LE-03.02 | C-50 |
| R-1172 | The source repository must be publicly readable at a static URL. Levels 1 to 3. | project maintainers | security | S-09 versions page, Quality, QA-01.01 | C-01 |
| R-1173 | The VCS must keep a publicly readable record of all changes, their authors and their timestamps. Levels 1 to 3. | project maintainers | security | S-09 versions page, Quality, QA-01.02 | C-01 |
| R-1174 | Where the package system supports it, the repository must include a dependency list of direct language dependencies. Levels 1 to 3. | project maintainers | security | S-09 versions page, Quality, QA-02.01 | C-09 |
| R-1175 | Compiled released assets must be delivered with a software bill of materials. Level 3. | project maintainers | security | S-09 versions page, Quality, QA-02.02 | C-09 |
| R-1176 | Commits to the primary branch must have all automated status checks pass, or be bypassed manually. Levels 2 and 3. | project maintainers | quality | S-09 versions page, Quality, QA-03.01 | C-37 |
| R-1177 | Multi-repository projects must document a list of their codebases. Levels 1 to 3. | project maintainers | quality | S-09 versions page, Quality, QA-04.01 | C-45 |
| R-1178 | Subprojects compiled into a release must enforce security requirements at least as strict as the primary codebase. Level 3. | project maintainers | security | S-09 versions page, Quality, QA-04.02 | C-20 |
| R-1179 | The VCS must not contain generated executable artifacts. Levels 1 to 3. | project maintainers | quality | S-09 versions page, Quality, QA-05.01 | C-44 |
| R-1180 | The VCS must not contain binary artifacts that cannot be reviewed. Images and sound are not included. Levels 1 to 3. | project maintainers | quality | S-09 versions page, Quality, QA-05.02 | C-44 |
| R-1181 | Before a commit is accepted, CI/CD pipelines must run at least one automated test suite. Levels 2 and 3. | project maintainers | quality | S-09 versions page, Quality, QA-06.01 | C-37 |
| R-1182 | The documentation must clearly state when and how tests are run. Level 3. | project maintainers | quality | S-09 versions page, Quality, QA-06.02 | C-37 |
| R-1183 | The documentation must include a policy that major changes add or update tests. Level 3. | project maintainers | quality | S-09 versions page, Quality, QA-06.03 | C-38 |
| R-1184 | Commits to the primary branch must have at least one approval from a human who is not the author, before merge. Level 3. | project maintainers | security | S-09 versions page, Quality, QA-07.01 | C-03 |
| R-1185 | After a release, the documentation must include design documentation that shows all actions and actors in the system. Levels 2 and 3. | project maintainers | quality | S-09 versions page, Security Assessment, SA-01.01 | C-47 |
| R-1186 | After a release, the documentation must describe all external software interfaces of the released assets. Levels 2 and 3. | project maintainers | quality | S-09 versions page, Security Assessment, SA-02.01 | C-47 |
| R-1187 | After a release, the project must perform a security assessment of the most likely and most impactful security problems. Levels 2 and 3. | project maintainers | security | S-09 versions page, Security Assessment, SA-03.01 | C-13 |
| R-1188 | After a release, the project must perform threat modeling and attack surface analysis of critical code paths and interactions. Level 3. | project maintainers | security | S-09 versions page, Security Assessment, SA-03.02 | C-13 |
| R-1189 | The documentation must include a coordinated vulnerability disclosure policy with a clear response timeframe. Levels 2 and 3. | project maintainers | security | S-09 versions page, Vulnerability Management, VM-01.01 | C-12 |
| R-1190 | The documentation must list security contacts. Level 1. | security engineers | security | S-09 versions page, Vulnerability Management, VM-02.01 | C-12 |
| R-1191 | The documentation must provide a way to privately report vulnerabilities directly to the project's security contacts. Levels 2 and 3. | security engineers | security | S-09 versions page, Vulnerability Management, VM-03.01 | C-12 |
| R-1192 | The documentation must publicly publish data about discovered vulnerabilities. Levels 2 and 3. | project maintainers | security | S-09 versions page, Vulnerability Management, VM-04.01 | C-12 |
| R-1193 | Vulnerabilities in components that do not affect the project must be recorded in a VEX document with non-exploitability details. Level 3. | project maintainers | security | S-09 versions page, Vulnerability Management, VM-04.02 | C-09 |
| R-1194 | The documentation must include a policy that sets a remediation threshold for SCA findings on vulnerabilities and licenses. Level 3. | project maintainers | security | S-09 versions page, Vulnerability Management, VM-05.01 | C-11 |
| R-1195 | The documentation must include a policy for addressing SCA violations before any release. Level 3. | project maintainers | security | S-09 versions page, Vulnerability Management, VM-05.02 | C-11 |
| R-1196 | All codebase changes must be checked automatically against a documented policy for malicious dependencies and known vulnerabilities, and must be blocked on violations unless suppressed as non-exploitable. Level 3. | project maintainers | security | S-09 versions page, Vulnerability Management, VM-05.03 | C-11 |
| R-1197 | The documentation must include a policy that sets a remediation threshold for SAST findings. Level 3. | project maintainers | security | S-09 versions page, Vulnerability Management, VM-06.01 | C-11 |
| R-1198 | All codebase changes must be checked automatically by SAST against a documented policy for security weaknesses, and must be blocked on violations unless suppressed as non-exploitable. Level 3. | project maintainers | security | S-09 versions page, Vulnerability Management, VM-06.02 | C-14 |
| R-1199 | All proposed changes to the codebase must be checked automatically against a documented policy for known vulnerabilities, and must be blocked on violations. | project maintainers | security | S-09 versions page, Lexicon, Known Vulnerabilities | C-11 |
| R-1200 | An automated test suite must return an overall pass or fail result. | project maintainers | quality | S-09 versions page, Lexicon, Automated Test Suite | C-37 |
| R-1201 | The software bill of materials must include the listed data elements, such as license, supplier name and component name and version. | project maintainers | security | S-09 versions page, Lexicon, Software Bill of Materials | C-09 |
| R-1202 | For deployable and executable components, the software bill of materials should record their cryptographic hashes. | project maintainers | security | S-09 versions page, Lexicon, Software Bill of Materials | C-09 |
| R-1203 | Remove generated executables from the repository and build from source. | project maintainers | quality | S-10 Binary-Artifacts item | C-44 |
| R-1204 | Enable branch protection or rulesets that block force pushes and branch deletion. | project maintainers | security | S-10 Branch-Protection item | C-03 |
| R-1205 | Require reviews, status checks and admin enforcement as the tiers allow. | project maintainers | security | S-10 Branch-Protection item | C-03 |
| R-1206 | Script all tests in the repository and run them on every pull request through a CI system. | project maintainers | quality | S-10 CI-Tests item | C-37 |
| R-1207 | Enroll the project in the OpenSSF Best Practices program. | project maintainers | security | S-10 CII-Best-Practices item | C-22 |
| R-1208 | Recruit more maintainers to review changes. | project maintainers | security | S-10 Code-Review item | C-03 |
| R-1209 | Apply strict review to every pull request. | project maintainers | security | S-10 Code-Review item | C-03 |
| R-1210 | Make review mandatory, including for admins and code owners. | project maintainers | security | S-10 Code-Review item | C-03 |
| R-1211 | Encourage contributors to join their organizations; no other remediation is offered. | project maintainers | quality | S-10 Contributors item | C-50 |
| R-1212 | Avoid untrusted checkouts in privileged workflow triggers. | project maintainers | security | S-10 Dangerous-Workflow item | C-15 |
| R-1213 | Avoid injecting untrusted context values into scripts. | project maintainers | security | S-10 Dangerous-Workflow item | C-15 |
| R-1214 | Enable Dependabot or Renovate and place the configuration files where the tool expects them. | project maintainers | quality | S-10 Dependency-Update-Tool item | C-51 |
| R-1215 | Projects that maintain forks should check the Dependabot forks behaviour. | project maintainers | security | S-10 Dependency-Update-Tool item | C-15 |
| R-1216 | Integrate the project with OSS-Fuzz. | project maintainers | security | S-10 Fuzzing item | C-14 |
| R-1217 | Choose and apply a license, and name the license file as the page specifies. | project maintainers | quality | S-10 License item | C-50 |
| R-1218 | Use a LICENSES directory with SPDX identifiers where that is the chosen form. | project maintainers | quality | S-10 License item | C-50 |
| R-1219 | Users should judge whether the software needs active maintenance when the score is low. | consumers | security | S-10 Maintained item | C-20 |
| R-1220 | Publish a downloadable package through GitHub publishing mechanisms or release actions. | project maintainers | operations | S-10 Packaging item | C-32 |
| R-1221 | Declare exact versions and commit lock files. | project maintainers | security | S-10 Pinned-Dependencies item | C-10 |
| R-1222 | Pin Docker and workflow dependencies by hash, and use update tools after pinning. | project maintainers | security | S-10 Pinned-Dependencies item | C-10 |
| R-1223 | Run CodeQL in CI/CD. | project maintainers | security | S-10 SAST item | C-14 |
| R-1224 | Publish an SBOM as a release artifact, using platform tooling or CycloneDX or SPDX generators. | project maintainers | security | S-10 SBOM item | C-09 |
| R-1225 | Add a SECURITY.md file at the repository root with a vulnerability definition, a secure reporting route and disclosure guidance. | project maintainers | security | S-10 Security-Policy item | C-12 |
| R-1226 | Publish releases, generate a signing key, sign the archives and attach the signatures. | project maintainers | security | S-10 Signed-Releases item | C-06 |
| R-1227 | Set top-level workflow permissions to read-only, and grant only the needed write permissions per job. | project maintainers | security | S-10 Token-Permissions item | C-02 |
| R-1228 | Avoid write-all permissions. | project maintainers | security | S-10 Token-Permissions item | C-02 |
| R-1229 | Fix vulnerabilities in code and dependencies. | project maintainers | security | S-10 Vulnerabilities item | C-11 |
| R-1230 | Ignore a false positive only through a documented entry in the osv-scanner configuration. | project maintainers | security | S-10 Vulnerabilities item | 5 |
| R-1231 | Set a secret on webhooks where the service supports it; otherwise request token authentication from the service. | project maintainers | security | S-10 Webhooks item | C-04 |
| R-1232 | Use a CLI with a GitHub or GitLab token to avoid rate limits, and have Go installed. | consumers | security | S-10 Repository page, usage statements | 5 |
| R-1233 | Maintainers who want results on the REST API must set publish results to true in the GitHub Action. | project maintainers | security | S-10 Repository page, usage statements | 5 |
| R-1234 | Enable two-factor authentication on accounts, using a security key or recovery codes where possible. | consumers | security | S-10 Repository page, security statements | C-02 |
| R-1235 | Open an issue for stale API data; report bugs on the issue tracker; follow SECURITY.md for security issues. | consumers | security | S-10 Repository page, contributing statements | C-12 |
| R-1236 | Projects that want weekly scanning should follow the scorecard-infra contributing guide. | project maintainers | security | S-10 Repository page, usage statements | 5 |
| R-1237 | Website must state briefly what the software does and what problem it solves. | consumers | quality | S-11 passing item description_good | C-45 |
| R-1238 | Website must explain how to obtain the software, give feedback, and contribute. | consumers | quality | S-11 passing item interact | C-45 |
| R-1239 | Contribution process must be explained, such as whether pull requests are used. | project maintainers | quality | S-11 passing item contribution | C-50 |
| R-1240 | Contribution requirements should be listed, such as coding standards. | project maintainers | quality | S-11 passing item contribution_requirements | C-50 |
| R-1241 | Software must be released as FLOSS. | project maintainers | quality | S-11 passing item floss_license | C-50 |
| R-1242 | Required licenses suggested to be OSI-approved. | project maintainers | quality | S-11 passing item floss_license_osi | C-50 |
| R-1243 | License must be posted in a standard location in the repository. | project maintainers | quality | S-11 passing item license_location | C-50 |
| R-1244 | Basic documentation must exist; N/A allowed. | consumers | quality | S-11 passing item documentation_basics | C-45 |
| R-1245 | Reference documentation must describe inputs and outputs; N/A allowed. | consumers | quality | S-11 passing item documentation_interface | C-45 |
| R-1246 | Project sites must support HTTPS with TLS. | project maintainers | security | S-11 passing item sites_https | C-18 |
| R-1247 | Searchable, URL-addressable discussion must exist that newcomers can join without proprietary client software. | project maintainers | quality | S-11 passing item discussion | C-50 |
| R-1248 | Documentation should be in English, and bug reports and code comments should be accepted in English. | project maintainers | quality | S-11 passing item english | C-45 |
| R-1249 | Project must be actively maintained. | project maintainers | operations | S-11 passing item maintained | C-36 |
| R-1250 | Publicly readable version-controlled repository with a URL must exist. | project maintainers | security | S-11 passing item repo_public | C-01 |
| R-1251 | Repository must record what changed, who changed it, and when. | project maintainers | security | S-11 passing item repo_track | C-01 |
| R-1252 | Repository must include interim review versions between releases. | project maintainers | security | S-11 passing item repo_interim | C-01 |
| R-1253 | Common distributed version control, such as git, is suggested. | project maintainers | security | S-11 passing item repo_distributed | C-01 |
| R-1254 | Each user-facing release must have a unique version identifier. | consumers | operations | S-11 passing item version_unique | C-32 |
| R-1255 | SemVer or CalVer is suggested; CalVer users should include a micro value. | project maintainers | operations | S-11 passing item version_semver | C-32 |
| R-1256 | Releases are suggested to be identified in version control, such as with git tags. | project maintainers | operations | S-11 passing item version_tags | C-32 |
| R-1257 | Each release must have human-readable summaries of major changes; N/A allowed. | consumers | operations | S-11 passing item release_notes | C-32 |
| R-1258 | Release notes must list fixed publicly known run-time vulnerabilities that had a CVE or similar; N/A allowed. | consumers | operations | S-11 passing item release_notes_vulns | C-32 |
| R-1259 | Users must have a process to submit bug reports. | consumers | quality | S-11 passing item report_process | C-43 |
| R-1260 | An issue tracker should be used for individual issues. | project maintainers | quality | S-11 passing item report_tracker | C-43 |
| R-1261 | A majority of bug reports from the last 2 to 12 months must be acknowledged. | consumers | quality | S-11 passing item report_responses | C-43 |
| R-1262 | More than 50 percent of enhancement requests from the last 2 to 12 months should receive a response. | consumers | quality | S-11 passing item enhancement_responses | C-50 |
| R-1263 | Bug reports and responses must be publicly archived and searchable. | consumers | quality | S-11 passing item report_archive | C-43 |
| R-1264 | Vulnerability reporting process must be published on the project site. | project maintainers | security | S-11 passing item vulnerability_report_process | C-12 |
| R-1265 | If private vulnerability reporting is supported, instructions for private submission must be given; N/A allowed. | project maintainers | security | S-11 passing item vulnerability_report_private | C-12 |
| R-1266 | Initial response to vulnerability reports from the last 6 months must be within 14 days; N/A allowed. | project maintainers | security | S-11 passing item vulnerability_report_response | C-12 |
| R-1267 | Working build system must rebuild the software from source; N/A allowed. | project maintainers | quality | S-11 passing item build | C-44 |
| R-1268 | Common build tools are suggested; N/A allowed. | project maintainers | quality | S-11 passing item build_common_tools | C-44 |
| R-1269 | Project should be buildable using only FLOSS tools; N/A allowed. | project maintainers | quality | S-11 passing item build_floss_tools | C-44 |
| R-1270 | At least one FLOSS automated test suite must exist, and how to run it must be documented. | project maintainers | quality | S-11 passing item test | C-37 |
| R-1271 | Tests should run in a standard way for the language. | project maintainers | quality | S-11 passing item test_invocation | C-37 |
| R-1272 | Tests are suggested to cover most or ideally all branches, inputs and functionality. | project maintainers | quality | S-11 passing item test_most | C-38 |
| R-1273 | Changes are suggested to be integrated frequently, with automated tests run on the result. | project maintainers | quality | S-11 passing item test_continuous_integration | C-37 |
| R-1274 | A policy must exist to add tests for major new functionality. | project maintainers | quality | S-11 passing item test_policy | C-38 |
| R-1275 | Evidence must show the test policy was followed in recent major changes. | project maintainers | quality | S-11 passing item tests_are_added | C-38 |
| R-1276 | Test policy is suggested to be documented in change proposal instructions. | project maintainers | quality | S-11 passing item tests_documented_added | C-38 |
| R-1277 | Compiler warnings, a safe language mode or a linter must be enabled where a FLOSS tool exists; N/A allowed. | project maintainers | quality | S-11 passing item warnings | C-40 |
| R-1278 | Warnings must be addressed; N/A allowed. | project maintainers | quality | S-11 passing item warnings_fixed | C-40 |
| R-1279 | Warnings are suggested to be kept maximally strict where practical; N/A allowed. | project maintainers | quality | S-11 passing item warnings_strict | C-40 |
| R-1280 | At least one primary developer must know how to design secure software. | software engineers | quality | S-11 passing item know_secure_design | C-49 |
| R-1281 | A primary developer must know common vulnerability-causing errors and at least one mitigation for each. | software engineers | quality | S-11 passing item know_common_errors | C-49 |
| R-1282 | Default cryptography must use only publicly published, expert-reviewed protocols and algorithms; N/A allowed. | project maintainers | security | S-11 passing item crypto_published | C-18 |
| R-1283 | Dedicated vetted crypto software should be called rather than re-implemented; N/A allowed. | project maintainers | security | S-11 passing item crypto_call | C-18 |
| R-1284 | Cryptography-dependent functionality must be implementable with FLOSS; N/A allowed. | project maintainers | security | S-11 passing item crypto_floss | C-18 |
| R-1285 | Default keylengths must meet NIST minimums through 2030, and smaller ones must be fully disableable; N/A allowed. | project maintainers | security | S-11 passing item crypto_keylength | C-18 |
| R-1286 | Default mechanisms must avoid broken algorithms and inappropriate modes, except documented necessary interoperability; N/A allowed. | project maintainers | security | S-11 passing item crypto_working | C-18 |
| R-1287 | Default mechanisms should avoid algorithms or modes with known serious weaknesses; N/A allowed. | project maintainers | security | S-11 passing item crypto_weaknesses | C-18 |
| R-1288 | Key agreement should provide perfect forward secrecy; N/A allowed. | project maintainers | security | S-11 passing item crypto_pfs | C-18 |
| R-1289 | Stored external-user passwords must use salted, iterated, key-stretching hashes; N/A allowed. | project maintainers | security | S-11 passing item crypto_password_storage | C-18 |
| R-1290 | Keys and nonces must come from a cryptographically secure random generator; N/A allowed. | project maintainers | security | S-11 passing item crypto_random | C-18 |
| R-1291 | Delivery must use a mechanism that counters man-in-the-middle attacks, such as HTTPS or SSH plus SCP. | project maintainers | security | S-11 passing item delivery_mitm | C-18 |
| R-1292 | Hashes fetched over HTTP must not be used without checking a cryptographic signature. | project maintainers | security | S-11 passing item delivery_unsigned | C-17 |
| R-1293 | No unpatched medium-or-higher vulnerability may be publicly known for more than 60 days. | project maintainers | security | S-11 passing item vulnerabilities_fixed_60_days | C-11 |
| R-1294 | Critical vulnerabilities should be fixed rapidly after being reported. | project maintainers | security | S-11 passing item vulnerabilities_critical_fixed | C-11 |
| R-1295 | Public repositories must contain no valid private credentials meant to limit access. | project maintainers | security | S-11 passing item no_leaked_credentials | C-04 |
| R-1296 | At least one static analysis tool, beyond compiler warnings, must be applied before a major release, if a FLOSS tool exists for the language. | project maintainers | security | S-11 passing item static_analysis | C-14 |
| R-1297 | At least one static tool should check for common vulnerabilities; N/A allowed. | project maintainers | security | S-11 passing item static_analysis_common_vulnerabilities | C-14 |
| R-1298 | Confirmed medium-or-higher exploitable static-analysis findings must be fixed promptly; N/A allowed. | project maintainers | security | S-11 passing item static_analysis_fixed | C-11 |
| R-1299 | Static analysis is suggested to run on every commit or at least daily; N/A allowed. | project maintainers | security | S-11 passing item static_analysis_often | C-14 |
| R-1300 | At least one dynamic analysis tool is suggested to be applied before a major release. | project maintainers | security | S-11 passing item dynamic_analysis | C-14 |
| R-1301 | For memory-unsafe languages, a dynamic tool such as a fuzzer is suggested to run with memory-safety detection; N/A allowed. | project maintainers | security | S-11 passing item dynamic_analysis_unsafe | C-14 |
| R-1302 | Dynamic analysis is suggested to enable many assertions, which are usually disabled in production builds. | project maintainers | security | S-11 passing item dynamic_analysis_enable_assertions | C-14 |
| R-1303 | Confirmed medium-or-higher exploitable dynamic-analysis findings must be fixed promptly; N/A allowed. | project maintainers | security | S-11 passing item dynamic_analysis_fixed | C-11 |
| R-1304 | Project must reach the passing badge first. | project maintainers | security | S-11 silver item achieve_passing | C-22 |
| R-1305 | Contribution guidance must state what acceptable contributions must meet. | project maintainers | quality | S-11 silver item contribution_requirements | C-50 |
| R-1306 | A legal mechanism such as a DCO should confirm that contributors may submit their work. | project maintainers | quality | S-11 silver item dco | C-50 |
| R-1307 | Decision-making, including key roles, must be documented. | project maintainers | quality | S-11 silver item governance | C-50 |
| R-1308 | A code of conduct must be adopted and posted where people can find it. | project maintainers | quality | S-11 silver item code_of_conduct | C-50 |
| R-1309 | Key roles, their duties and their holders must be defined and published. | project maintainers | quality | S-11 silver item roles_responsibilities | C-50 |
| R-1310 | Project must keep working if one person leaves, so others can create and close issues, accept changes and release within a week. | project maintainers | quality | S-11 silver item access_continuity | C-50 |
| R-1311 | At least two people should be able to keep the project going. | project maintainers | quality | S-11 silver item bus_factor | C-50 |
| R-1312 | A roadmap covering at least the next year must be published. | consumers | quality | S-11 silver item documentation_roadmap | C-48 |
| R-1313 | High-level design must be documented; N/A if no software is produced. | project maintainers | quality | S-11 silver item documentation_architecture | C-47 |
| R-1314 | The security that users can and cannot expect must be stated. | consumers | quality | S-11 silver item documentation_security | C-45 |
| R-1315 | A quick-start guide for new users must be provided. | consumers | quality | S-11 silver item documentation_quick_start | C-45 |
| R-1316 | Documentation must stay consistent with the current release and known defects must be fixed. | consumers | quality | S-11 silver item documentation_current | C-45 |
| R-1317 | Earned achievements, including this badge, must be linked within 48 hours of recognition. | project maintainers | security | S-11 silver item documentation_achievements | C-22 |
| R-1318 | Accessibility practices should be followed so that persons with disabilities can take part and use results. | software engineers | quality | S-11 silver item accessibility_best_practices | C-41 |
| R-1319 | Software should be easy to localize where it produces user-facing text or sorts text. | project maintainers | quality | S-11 silver item internationalization | C-41 |
| R-1320 | External users' passwords must be stored as salted, iterated hashes with a key-stretching algorithm. | project maintainers | security | S-11 silver item sites_password_security | C-18 |
| R-1321 | Commonly used older versions must be maintained, or a documented upgrade path must be provided. | consumers | operations | S-11 silver item maintenance_or_update | C-36 |
| R-1322 | An issue tracker must be used for individual issues. | project maintainers | quality | S-11 silver item report_tracker | C-43 |
| R-1323 | Reporters of vulnerabilities resolved in the last 12 months must be credited, unless they want anonymity. | project maintainers | security | S-11 silver item vulnerability_report_credit | C-12 |
| R-1324 | A process for responding to vulnerability reports must be documented. | project maintainers | security | S-11 silver item vulnerability_response_process | C-12 |
| R-1325 | Style guides for primary languages must be named, and contributions must be expected to follow them. | project maintainers | quality | S-11 silver item coding_standards | C-40 |
| R-1326 | The chosen style must be enforced automatically where a FLOSS tool exists. | project maintainers | quality | S-11 silver item coding_standards_enforced | C-40 |
| R-1327 | Native builds must honor and pass through standard compiler and linker variables, adding but not replacing them. | project maintainers | quality | S-11 silver item build_standard_variables | C-44 |
| R-1328 | Debug information should be kept when build or install flags request it. | project maintainers | quality | S-11 silver item build_preserve_debug | C-44 |
| R-1329 | Recursive builds of subdirectories with cross-dependencies must not be used. | project maintainers | quality | S-11 silver item build_non_recursive | C-44 |
| R-1330 | Rebuilding from the same source must produce bit-for-bit identical output. | project maintainers | security | S-11 silver item build_repeatable | C-21 |
| R-1331 | Easy install and uninstall using a common convention must be provided. | consumers | operations | S-11 silver item installation_common | C-24 |
| R-1332 | Installation must honor standard conventions for choosing the destination directory. | project maintainers | operations | S-11 silver item installation_standard_variables | C-24 |
| R-1333 | Developers must be able to install quickly everything needed to make changes and run tests. | software engineers | quality | S-11 silver item installation_development_quick | C-44 |
| R-1334 | External dependencies must be listed in a machine-processable form. | project maintainers | security | S-11 silver item external_dependencies | C-09 |
| R-1335 | Dependencies must be monitored for known vulnerabilities, and exploitable ones must be fixed or verified. | project maintainers | security | S-11 silver item dependency_monitoring | C-11 |
| R-1336 | Reused components must be easy to identify and update, or standard system or language components must be used. | project maintainers | quality | S-11 silver item updateable_reused_components | C-51 |
| R-1337 | Deprecated or obsolete functions should be avoided when free alternatives exist for most users. | project maintainers | operations | S-11 silver item interfaces_current | C-36 |
| R-1338 | An automated test suite must run on each check-in to a shared branch, producing a pass or fail report. | project maintainers | quality | S-11 silver item automated_integration_testing | C-37 |
| R-1339 | Regression tests must be added for at least half of the bugs fixed in the last six months. | project maintainers | quality | S-11 silver item regression_tests_added50 | C-38 |
| R-1340 | At least 80 percent statement coverage must be achieved where a FLOSS measurement tool exists. | project maintainers | quality | S-11 silver item test_statement_coverage80 | C-39 |
| R-1341 | A written policy must require tests for major new functionality. | project maintainers | quality | S-11 silver item test_policy_mandated | C-38 |
| R-1342 | The test-for-new-functionality policy must be included in change-proposal instructions. | project maintainers | quality | S-11 silver item tests_documented_added | C-38 |
| R-1343 | The strictest practical compiler or tool warning settings must be used. | project maintainers | quality | S-11 silver item warnings_strict | C-40 |
| R-1344 | Secure design principles must be applied where applicable. | software engineers | security | S-11 silver item implement_secure_design | C-13 |
| R-1345 | Default security mechanisms must avoid algorithms or modes with known serious weaknesses. | consumers | security | S-11 silver item crypto_weaknesses | C-18 |
| R-1346 | Multiple cryptographic algorithms should be supported so that users can switch if one breaks. | consumers | security | S-11 silver item crypto_algorithm_agility | C-18 |
| R-1347 | Credentials and private keys must be stored separately from other data and updatable without recompiling. | project maintainers | security | S-11 silver item crypto_credential_agility | C-04 |
| R-1348 | Secure network protocols should be used by default, and insecure ones disabled unless explicitly enabled. | consumers | security | S-11 silver item crypto_used_network | C-18 |
| R-1349 | At least TLS 1.2 should be supported where TLS is used. | project maintainers | security | S-11 silver item crypto_tls12 | C-18 |
| R-1350 | TLS certificates must be verified by default, including for subresources. | project maintainers | security | S-11 silver item crypto_certificate_verification | C-18 |
| R-1351 | Certificates must be verified before HTTP headers containing private data are sent. | project maintainers | security | S-11 silver item crypto_verification_private | C-18 |
| R-1352 | Widely distributed releases must be cryptographically signed, with documented verification steps, and the private key kept off distribution sites. | consumers | security | S-11 silver item signed_releases | C-06 |
| R-1353 | Important version tags are suggested to be signed in version control. | project maintainers | security | S-11 silver item version_tags_signed | C-01 |
| R-1354 | All untrusted inputs must be validated with an allowlist, and invalid inputs must be rejected. | project maintainers | security | S-11 silver item input_validation | C-15 |
| R-1355 | Hardening mechanisms should be used so that defects are less likely to become vulnerabilities. | project maintainers | security | S-11 silver item hardening | C-11 |
| R-1356 | An assurance case must cover the threat model, trust boundaries, secure design, and countered implementation weaknesses. | project maintainers | security | S-11 silver item assurance_case | C-13 |
| R-1357 | At least one static analysis tool that checks for common vulnerabilities must be used. | project maintainers | security | S-11 silver item static_analysis_common_vulnerabilities | C-14 |
| R-1358 | For memory-unsafe languages, a dynamic tool such as a fuzzer must be run routinely with memory-safety detection. | project maintainers | security | S-11 silver item dynamic_analysis_unsafe | C-14 |
| R-1359 | Project must reach the silver badge first. | project maintainers | security | S-11 gold item achieve_silver | C-22 |
| R-1360 | A bus factor of at least 2 must be achieved. | project maintainers | quality | S-11 gold item bus_factor | C-50 |
| R-1361 | At least two significant contributors not affiliated with the project must exist. | project maintainers | quality | S-11 gold item contributors_unassociated | C-50 |
| R-1362 | Each source file must carry a copyright notice naming the holder. | project maintainers | quality | S-11 gold item copyright_per_file | C-50 |
| R-1363 | Each source file must carry a license statement. | project maintainers | quality | S-11 gold item license_per_file | C-50 |
| R-1364 | A common distributed version control system must be used. | project maintainers | security | S-11 gold item repo_distributed | C-01 |
| R-1365 | Small tasks suitable for newcomers must be labelled. | project maintainers | quality | S-11 gold item small_tasks | C-50 |
| R-1366 | Two-factor authentication must be required for developers who change the central repository or access sensitive data. | software engineers | security | S-11 gold item require_2FA | C-02 |
| R-1367 | Cryptographic two-factor authentication should be used to resist impersonation; SMS alone does not qualify. | software engineers | security | S-11 gold item secure_2FA | C-02 |
| R-1368 | The code review process, what is checked, and the acceptance criteria must be documented. | project maintainers | security | S-11 gold item code_review_standards | C-03 |
| R-1369 | At least half of proposed changes must be reviewed by someone other than the author before release. | software engineers | security | S-11 gold item two_person_review | C-03 |
| R-1370 | Reproducible builds must be produced; N/A if nothing is compiled. | project maintainers | security | S-11 gold item build_reproducible | C-21 |
| R-1371 | The test suite must be runnable in a standard way for the language. | project maintainers | quality | S-11 gold item test_invocation | C-37 |
| R-1372 | Changes must be integrated frequently, with automated tests run on the result. | project maintainers | quality | S-11 gold item test_continuous_integration | C-37 |
| R-1373 | At least 90 percent statement coverage must be achieved where a FLOSS tool can measure it. | project maintainers | quality | S-11 gold item test_statement_coverage90 | C-39 |
| R-1374 | At least 80 percent branch coverage must be achieved where a FLOSS tool can measure it. | project maintainers | quality | S-11 gold item test_branch_coverage80 | C-39 |
| R-1375 | Secure network protocols must be used by default, and insecure ones only if a user explicitly enables them. | consumers | security | S-11 gold item crypto_used_network | C-18 |
| R-1376 | At least TLS 1.2 must be supported wherever TLS is used. | project maintainers | security | S-11 gold item crypto_tls12 | C-18 |
| R-1377 | The project website, repository and download site must be served with strict security headers. | project maintainers | security | S-11 gold item hardened_site | C-16 |
| R-1378 | A security review covering security requirements and boundaries must be completed within the past 5 years. | project maintainers | security | S-11 gold item security_review | C-13 |
| R-1379 | Hardening mechanisms must be used so that defects are less likely to become vulnerabilities. | project maintainers | security | S-11 gold item hardening | C-11 |
| R-1380 | At least one dynamic analysis tool must be run on each proposed major release. | project maintainers | security | S-11 gold item dynamic_analysis | C-14 |
| R-1381 | Many run-time assertions should be included and checked during dynamic analysis. | project maintainers | security | S-11 gold item dynamic_analysis_enable_assertions | C-14 |
| R-1382 | Organizations should take steps to verify the provenance of the code. | security engineers | security | S-12 Part 3, Source Code (intro) | C-17 |
| R-1383 | Define protected branches and folders with named approvers. | security engineers | security | S-12 Part 3, Source Code, Verification, Declare protected repository namespaces | C-03 |
| R-1384 | Verify that each push is authorized, using signed pushes or a reference state log, and monitor audit logs. | security engineers | security | S-12 Part 3, Source Code, Verification, Authenticate and monitor repository activity | C-01 |
| R-1385 | Enforce independent two-party review: at least two individuals independent of the request approve it, one with write access. | security engineers | security | S-12 Part 3, Source Code, Verification, Enforce independent 2-party review | C-03 |
| R-1386 | Record policy checks as attestations that CI verifies before builds. | security engineers | security | S-12 Part 3, Source Code, Verification, Require verification attestations | C-17 |
| R-1387 | Keep secrets out of repositories unless encrypted. Tools like git-secrets or trufflehog can detect them through hooks or CI. Teams can extend default blocked-file lists. | security engineers | security | S-12 Part 3, Source Code, Automation, Prevent committing secrets | C-04 |
| R-1388 | Run unit, functional, end-to-end, SAST and DAST tests, and link scan metadata to artifact hashes. | security engineers | security | S-12 Part 3, Source Code, Automation, Automate security scanning and testing | C-14 |
| R-1389 | Set baseline repository rules and publish acceptable-contribution criteria. | managers | quality | S-12 Part 3, Source Code, Controlled Environments, Contribution policies | C-50 |
| R-1390 | Use roles with least privilege. | security engineers | security | S-12 Part 3, Source Code, Controlled Environments, Define roles | C-02 |
| R-1391 | MFA should be required at the VCS level for all software projects. | security engineers | security | S-12 Part 3, Source Code, Secure Authentication, Enforce MFA | C-02 |
| R-1392 | Prefer SSH keys or certificates over passwords; use tokens only if short-lived and issued by an out-of-band system. | security engineers | security | S-12 Part 3, Source Code, Secure Authentication, Use SSH keys | C-04 |
| R-1393 | Use ephemeral tokens for machines and avoid long-lived personal access tokens. | security engineers | security | S-12 Part 3, Source Code, Secure Authentication, Short-lived credentials | C-04 |
| R-1394 | Use risk management when accepting dependencies, and check the vulnerability-handling processes of suppliers. | security engineers | security | S-12 Part 3, Materials, Second and Third-Party Risk Management | C-20 |
| R-1395 | Consumers should review vendor changes and changelogs. | consumers | security | S-12 Part 3, Materials, Second and Third-Party Risk Management | C-20 |
| R-1396 | Check checksums and signatures of third-party artifacts in CI, and run SCA. | security engineers | security | S-12 Part 3, Materials, Verification, Verify third-party artifacts | C-10 |
| R-1397 | Where possible, require vendors to provide SBOMs and VEX statements. | security engineers | security | S-12 Part 3, Materials, Verification, Require SBOMs and VEX | C-09 |
| R-1398 | Signed build metadata should accompany the SBOM. | security engineers | security | S-12 Part 3, Materials, Verification, Require SBOMs and VEX | C-06 |
| R-1399 | Maintain an inventory of components and their vulnerabilities. | security engineers | security | S-12 Part 3, Materials, Verification, Track dependencies | C-09 |
| R-1400 | Build binaries from source where feasible. | software engineers | quality | S-12 Part 3, Materials, Verification, Build libraries from source | C-44 |
| R-1401 | Use vetted suppliers with documented processes and incident SLAs. | security engineers | security | S-12 Part 3, Materials, Verification, Define trusted package managers | C-20 |
| R-1402 | Highly regulated environments should minimize ingestion from public repositories. | security engineers | security | S-12 Part 3, Materials, Verification, Define trusted package managers | C-20 |
| R-1403 | Generate SBOMs at build time, not by scanning. | security engineers | security | S-12 Part 3, Materials, Verification, Generate immutable SBOM | C-09 |
| R-1404 | Analyze dependencies before intake and periodically, and triage using VEX or CVSS. | security engineers | security | S-12 Part 3, Materials, Automation, Scan for vulnerabilities | C-11 |
| R-1405 | Record licensing metadata in the SBOM. | security engineers | security | S-12 Part 3, Materials, Automation, Managing software licenses | C-09 |
| R-1406 | Run SCA on direct and transitive dependencies of ingested software. | security engineers | security | S-12 Part 3, Materials, Automation, Run SCA on ingested software | C-11 |
| R-1407 | Secure build steps, workers, tools and the orchestrator, and record signed build metadata externally. | security engineers | security | S-12 Part 3, Build Pipelines (intro) | C-16 |
| R-1408 | Build from hardened containers. | security engineers | security | S-12 Part 3, Build Pipelines (intro) | C-16 |
| R-1409 | Use in-toto layouts, SLSA maturity levels and OPA to check build metadata. | security engineers | security | S-12 Part 3, Build Pipelines, Verification, Enforcing policy | C-17 |
| R-1410 | Validate checksums and signatures at download and again at build time, and pin commit hashes. | security engineers | security | S-12 Part 3, Build Pipelines, Verification, Validate environments and dependencies | C-10 |
| R-1411 | Apply seccomp, AppArmor or SELinux to build workers, restrict kernel capabilities, and send findings to a SIEM. | security engineers | security | S-12 Part 3, Build Pipelines, Verification, Validate runtime security of build workers | C-16 |
| R-1412 | Lock and verify external requirements by vendoring or recording hashes, update them, and replace unverifiable dependencies. | security engineers | security | S-12 Part 3, Build Pipelines, Reproducible builds, Lock and verify external requirements | C-10 |
| R-1413 | Eliminate non-determinism such as timestamps, locale and file ordering. | security engineers | security | S-12 Part 3, Build Pipelines, Reproducible builds, Eliminate non-determinism | C-21 |
| R-1414 | Record tool versions and hashes of the build environment. | security engineers | security | S-12 Part 3, Build Pipelines, Reproducible builds, Record the build environment | C-21 |
| R-1415 | Script build environments with Vagrant or Dockerfiles. | operations engineers | operations | S-12 Part 3, Build Pipelines, Reproducible builds, Automate build environments | C-26 |
| R-1416 | Distribute builds across infrastructure so that attackers must compromise multiple rebuilders. | security engineers | security | S-12 Part 3, Build Pipelines, Reproducible builds, Distribute builds across infrastructure | C-21 |
| R-1417 | Automate all pipeline steps; only code reviews and sign-offs are manual. | security engineers | security | S-12 Part 3, Build Pipelines, Automation, Pipelines as code | C-05 |
| R-1418 | Use shared pipeline templates, and developers must not bypass them. | operations engineers | operations | S-12 Part 3, Build Pipelines, Automation, Standardize pipelines | C-33 |
| R-1419 | Provision a secured orchestration platform with IaC, hardware tokens for cluster admin credentials, and GitOps. | operations engineers | operations | S-12 Part 3, Build Pipelines, Automation, Provision a secured orchestration platform | C-26 |
| R-1420 | Build workers should be single use, and snapshot or quarantine them for forensics. | security engineers | security | S-12 Part 3, Build Pipelines, Automation, Build workers single use | C-07 |
| R-1421 | Allow minimal network connectivity, only to trusted sources, dependency repositories and signing infrastructure. | security engineers | security | S-12 Part 3, Build Pipelines, Controlled Environments, Minimal network connectivity | C-07 |
| R-1422 | Segregate duties by giving each worker one part of the build. | security engineers | security | S-12 Part 3, Build Pipelines, Controlled Environments, Segregate duties | C-08 |
| R-1423 | Pass a hermetic environment from the pipeline to workers, and keep worker logic minimal. | security engineers | security | S-12 Part 3, Build Pipelines, Controlled Environments, Pass in environment and commands | C-21 |
| R-1424 | Write outputs to storage separate from inputs, and let a separate process upload them. | security engineers | security | S-12 Part 3, Build Pipelines, Controlled Environments, Separate output storage | C-07 |
| R-1425 | Keep pipeline configuration immutable; admins cannot change running pipelines directly. | security engineers | security | S-12 Part 3, Build Pipelines, Secure Authentication and Access, Pipeline as code only | C-05 |
| R-1426 | No single user should be able to attest to the validity of a software release. | security engineers | security | S-12 Part 3, Build Pipelines, Secure Authentication and Access, Define user roles | C-08 |
| R-1427 | Define user roles, including Policy Administrators, Administrators and application developers. | security engineers | security | S-12 Part 3, Build Pipelines, Secure Authentication and Access, Define user roles | C-08 |
| R-1428 | Establish the root of trust from an offline source. | security engineers | security | S-12 Part 3, Build Pipelines, Secure Authentication and Access, Root of trust | C-17 |
| R-1429 | Use automated rotation for short-lived workload certificates. | security engineers | security | S-12 Part 3, Build Pipelines, Secure Authentication and Access, Short-lived workload certificates | C-04 |
| R-1430 | Watch for unexpected endpoint connections, especially at artifact-affecting stages. | security engineers | security | S-12 Part 3, Build Pipelines, Secure Authentication and Access, Monitor for malicious behavior | C-16 |
| R-1431 | Sign inputs, outputs and traces, and sign the bundle. | security engineers | security | S-12 Part 3, Build Pipelines, Secure Authentication and Access, Sign every step | C-06 |
| R-1432 | Hash and sign artifacts and metadata, and anchor keys to a secure root of trust. | security engineers | security | S-12 Part 3, Artifacts (intro) | C-17 |
| R-1433 | Sign and verify at each lifecycle stage. | security engineers | security | S-12 Part 3, Artifacts (intro) | C-17 |
| R-1434 | Verify signatures on attestations, images and SBOMs against policy. | security engineers | security | S-12 Part 3, Artifacts, Verification, Validate signatures at each step | C-17 |
| R-1435 | Add a release signature from a delegated validation key. | security engineers | security | S-12 Part 3, Artifacts, Verification, Additional checks | C-06 |
| R-1436 | Check attestations against the supply chain policy and the signer identity. | security engineers | security | S-12 Part 3, Artifacts, Verification, Policy | C-17 |
| R-1437 | Delegate signing to build servers or developers, using TUF. | security engineers | security | S-12 Part 3, Artifacts, Automation, Use TUF for signing | C-06 |
| R-1438 | Use a metadata store. | security engineers | security | S-12 Part 3, Artifacts, Automation, Use a metadata store | C-23 |
| R-1439 | Distribute in-toto metadata with TUF to prevent tampering and rollback attacks. | security engineers | security | S-12 Part 3, Artifacts, Automation, Distribute in-toto metadata with TUF | C-17 |
| R-1440 | Trust must expire at predefined intervals, unless renewed. | security engineers | security | S-12 Part 3, Artifacts, Controlled Environments, Limit certification scope | C-17 |
| R-1441 | Compartmentalize trust by task. | security engineers | security | S-12 Part 3, Artifacts, Controlled Environments, Limit certification scope | C-08 |
| R-1442 | Plan for key compromise, use multiple keys and thresholds, and minimize trust in online keys. | security engineers | security | S-12 Part 3, Artifacts, Controlled Environments, Rotate and revoke keys | C-04 |
| R-1443 | Use an OCI image-spec registry and the OCI artifact manifest. | security engineers | security | S-12 Part 3, Artifacts, Controlled Environments, OCI-compliant registry | 5 |
| R-1444 | Clients verify file integrity, metadata signatures and content against policy. | consumers | security | S-12 Part 3, Deployments and Distribution, Verification, Clients verify artifacts and metadata | C-17 |
| R-1445 | Clients verify freshness and detect outdated files and failed update retrieval. | consumers | security | S-12 Part 3, Deployments and Distribution, Verification, Clients verify freshness | C-17 |
| R-1446 | For air-gapped deployment, use copy time for expiry checks, verify before import, and attest to the verification. | security engineers | security | S-12 Part 3, Deployments and Distribution, Verification, Air-gapped deployment | C-17 |
| R-1447 | Verify at deployment, for example with a Kubernetes admission controller, and again at the end user. | security engineers | security | S-12 Part 3, Deployments and Distribution, Verification, Admission controller or deployment gate | C-17 |
| R-1448 | Use The Update Framework (TUF). | security engineers | security | S-12 Part 3, Deployments and Distribution, Automation, Use The Update Framework | 5 |
| R-1449 | Bootstrap in-toto trust with TUF. | security engineers | security | S-12 Part 3, Deployments and Distribution, Automation, TUF bootstraps in-toto trust | 5 |
| R-1450 | Track new vulnerabilities after deployment using SBOMs and VEX. | security engineers | security | S-12 Part 3, Deployments and Distribution, Automation, Continuous vulnerability scanning | C-11 |
| R-1451 | Per OMB M-22-18, federal acquirers are instructed to ensure that software producers have implemented and will attest to conformity with secure development practices. | regulators and auditors | security | S-14 Source B, attesting page, body | C-22 |
| R-1452 | The self-attestation must include the producer name, a description of the product or products, and a statement of secure development practice. | project maintainers | security | S-14 Source B, body, "Minimum self-attestation" | C-22 |
| R-1453 | Agencies should consider enhanced attestation beyond the minimum practices for the risk scenarios listed. | regulators and auditors | security | S-14 Source B, attesting page, body | C-20 |
| R-1454 | Agencies seeking more comprehensive attestation in higher-risk cases should consult the evolving standards guidance and Appendices D and E of SP 800-161r1. | regulators and auditors | security | S-14 Source B, body, "Further guidance" | C-20 |
| R-1455 | As in other contexts, standards should always be referred to with their full reference, for example certified to ISO/IEC 27001:2022. | security engineers | security | S-16 page 2 | C-22 |
| R-1456 | To show certification with the ISO logo, contact the certification body that issued the certificate. | quality assurance staff | quality | S-16 page 2 | C-42 |
| R-1457 | The requirement to use techniques to design test cases is specified by the test processes of Part 2. | software engineers | quality | S-19 introductory paragraph | C-38 |
| R-1458 | Use credentials with the fewest permissions needed | security engineers | security | S-20 Writing workflows: Use secrets for sensitive information, Least privilege | C-02 |
| R-1459 | Default GITHUB_TOKEN to read-only repository contents and raise permissions per job only when needed | security engineers | security | S-20 Writing workflows: Use secrets, GITHUB_TOKEN | 5 |
| R-1460 | Sensitive data must never be stored as plaintext in workflow files | security engineers | security | S-20 Writing workflows: Use secrets, Masking | C-04 |
| R-1461 | Mask non-secret sensitive values with the add-mask command | security engineers | security | S-20 Writing workflows: Use secrets, Masking | 5 |
| R-1462 | Delete any log that contains an unredacted secret | security engineers | security | S-20 Writing workflows: Use secrets, Exposed secrets | C-04 |
| R-1463 | Rotate a secret that appears unredacted in a log | security engineers | security | S-20 Writing workflows: Use secrets, Exposed secrets | C-04 |
| R-1464 | Do not put JSON, XML or YAML blobs in a single secret; create one secret per sensitive value | security engineers | security | S-20 Writing workflows: Use secrets, Structured data | 5 |
| R-1465 | Register each value derived from a secret as a secret too | security engineers | security | S-20 Writing workflows: Use secrets, Derived values | C-04 |
| R-1466 | Review how secrets are used in the repository and its actions | security engineers | security | S-20 Writing workflows: Use secrets, Auditing | C-04 |
| R-1467 | Review run logs after testing valid and invalid inputs | security engineers | security | S-20 Writing workflows: Use secrets, Auditing | C-04 |
| R-1468 | Remove registered secrets that are no longer needed, periodically | security engineers | security | S-20 Writing workflows: Use secrets, Ongoing hygiene | C-04 |
| R-1469 | Rotate secrets on a schedule | security engineers | security | S-20 Writing workflows: Use secrets, Ongoing hygiene | C-04 |
| R-1470 | Required reviewers can gate access to environment secrets | security engineers | security | S-20 Writing workflows: Use secrets, Reviews | 5 |
| R-1471 | Use a JavaScript action that takes the context value as an argument; for inline scripts, use an intermediate environment variable | security engineers | security | S-20 Writing workflows: Good practices for mitigating script injection, Preferred approach | C-15 |
| R-1472 | Assign untrusted values to an intermediate environment variable and reference that variable in inline scripts | security engineers | security | S-20 Writing workflows: Good practices for mitigating script injection, Inline scripts | C-15 |
| R-1473 | Quote shell variables to avoid word splitting | security engineers | security | S-20 Writing workflows: Good practices for mitigating script injection, Inline scripts | C-15 |
| R-1474 | Start from GitHub's or third-party code scanning workflow templates | security engineers | security | S-20 Writing workflows: Good practices for mitigating script injection, Code scanning templates | C-14 |
| R-1475 | Restrict token permissions to reduce the impact of an exposed token | security engineers | security | S-20 Writing workflows: Good practices for mitigating script injection, Token permissions | C-02 |
| R-1476 | Avoid pull_request_target unless the workflow needs privileged context | security engineers | security | S-20 Mitigating the risks of untrusted code checkout, Use sparingly | 5 |
| R-1477 | For privilege separation, prefer workflow_run | security engineers | security | S-20 Mitigating the risks of untrusted code checkout, Use sparingly | 5 |
| R-1478 | Workflows that use pull_request_target or workflow_run must not check out untrusted code, including from forks or repositories you do not control | security engineers | security | S-20 Mitigating the risks of untrusted code checkout, No untrusted checkout | 5 |
| R-1479 | Treat artifacts from other workflows with caution | security engineers | security | S-20 Mitigating the risks of untrusted code checkout, No untrusted checkout | C-15 |
| R-1480 | Enable CodeQL-based scanning of workflows | security engineers | security | S-20 Mitigating the risks of untrusted code checkout, Scanning | C-14 |
| R-1481 | Consider OpenSSF Scorecards | security engineers | security | S-20 Mitigating the risks of untrusted code checkout, Scanning | C-22 |
| R-1482 | Pin third-party actions to a full-length commit SHA, which is currently the only way to use an action as an immutable release | security engineers | security | S-20 Using third-party actions, Pin to full-length commit SHA | C-10 |
| R-1483 | The SHA should come from the action's own repository, not a fork | security engineers | security | S-20 Using third-party actions, Pin to full-length commit SHA | C-15 |
| R-1484 | Audit action source to confirm that secrets and repository content are not sent to unintended hosts or logged | security engineers | security | S-20 Using third-party actions, Audit action source | C-20 |
| R-1485 | Pin to a tag only if you trust the creator | security engineers | security | S-20 Using third-party actions, Tags | C-10 |
| R-1486 | The same practices apply to reusable workflows | security engineers | security | S-20 Using third-party actions, Reusable workflows | C-10 |
| R-1487 | Require designated reviewers through CODEOWNERS to approve changes to the workflows directory | security engineers | security | S-20 GitHub's security features, CODEOWNERS | C-03 |
| R-1488 | Use OIDC to authenticate to cloud providers without long-lived stored credentials | security engineers | security | S-20 GitHub's security features, OIDC | C-04 |
| R-1489 | Keep action references current with Dependabot version updates | software engineers | quality | S-20 GitHub's security features, Dependabot | C-51 |
| R-1490 | Choose whether Actions workflows may create or approve pull requests | security engineers | security | S-20 GitHub's security features, Pull request permissions | 5 |
| R-1491 | Self-hosted runners should almost never be used for public repositories | security engineers | security | S-20 GitHub's security features, Self-hosted runners | C-16 |
| R-1492 | Use caution with self-hosted runners on private and internal repositories | security engineers | security | S-20 GitHub's security features, Self-hosted runners | C-16 |
| R-1493 | Keep sensitive data and network access to sensitive services on self-hosted runners to a minimum | security engineers | security | S-20 GitHub's security features, Self-hosted runners | C-16 |
| R-1494 | Use runner groups to limit blast radius | security engineers | security | S-20 GitHub's security features, Self-hosted runners | 5 |
| R-1495 | Use just-in-time runners, which perform at most one job before removal | security engineers | security | S-20 GitHub's security features, Self-hosted runners | C-16 |
| R-1496 | Reused hardware needs automation to provide a clean environment | security engineers | security | S-20 GitHub's security features, Self-hosted runners | C-07 |
| R-1497 | Choose a runner management level (enterprise, organization or repository) that matches centralized or decentralized ownership | security engineers | security | S-20 GitHub's security features, Self-hosted runners | 5 |
| R-1498 | Maintainers of published actions can use the dependents view, private vulnerability reporting and repository security advisories | project maintainers | security | S-20 Protecting actions you've created | C-12 |
| R-1499 | Use OIDC for cloud access where the workflow needs a provider that supports it | security engineers | security | S-20 Introduction and GitHub's security features, OIDC | C-04 |
| R-1500 | Reuse workflows to avoid duplication. | operations engineers | operations | S-21 A: Reusable workflows | C-33 |
| R-1501 | Use a reusable workflow, not a composite action, when steps must run on a different machine type than the caller job. | operations engineers | operations | S-21 A: Reusable workflows versus composite actions | 5 |
| R-1502 | Steps cannot be added after a reusable workflow call in the same job. | operations engineers | operations | S-21 A: Reusable workflows versus composite actions | 5 |
| R-1503 | Pin reusable workflows by commit SHA. | security engineers | security | S-21 A: Workflow templates | C-10 |
| R-1504 | Verify trust before using a tag or branch of a reusable workflow. | security engineers | security | S-21 A: Workflow templates | C-10 |
| R-1505 | Store a reusable workflow file in the workflows directory. Subdirectories are not supported. | operations engineers | operations | S-21 B: Creating a reusable workflow | 5 |
| R-1506 | Include workflow_call in the on key of a reusable workflow. | operations engineers | operations | S-21 B: Creating a reusable workflow | 5 |
| R-1507 | Define inputs and secrets under on workflow_call, then reference them in the workflow. | operations engineers | operations | S-21 B: Using inputs and secrets in a reusable workflow | 5 |
| R-1508 | Set environment on the job to use environment secrets. | operations engineers | operations | S-21 B: Using inputs and secrets in a reusable workflow | 5 |
| R-1509 | Callers must still pass the environment secrets. | security engineers | security | S-21 B: Using inputs and secrets in a reusable workflow | C-04 |
| R-1510 | Set required to true on a secret to fail the run when the secret is missing. | security engineers | security | S-21 B: Using inputs and secrets in a reusable workflow | C-04 |
| R-1511 | Use uses at the job level, not in steps. | operations engineers | operations | S-21 B: Calling a reusable workflow | 5 |
| R-1512 | Pick a valid reference form when you call a reusable workflow. | operations engineers | operations | S-21 B: Calling a reusable workflow | 5 |
| R-1513 | Do not use contexts or expressions in the $/ and ./ reference forms. | operations engineers | operations | S-21 B: Calling a reusable workflow | 5 |
| R-1514 | Do not include @{ref} with the $/ form. | operations engineers | operations | S-21 B: Calling a reusable workflow | 5 |
| R-1515 | Do not use refs/heads or refs/tags prefixes in a same-repository reference. | operations engineers | operations | S-21 B: Calling a reusable workflow | 5 |
| R-1516 | Input data types must match the types that the called workflow declares: boolean, number or string. | operations engineers | operations | S-21 B: Passing inputs and secrets to a reusable workflow | 5 |
| R-1517 | Stay within the ten-level nesting limit and avoid loops. | operations engineers | operations | S-21 B: Nesting reusable workflows | 5 |
| R-1518 | Every workflow in a nested chain must be accessible to the caller. | operations engineers | operations | S-21 B: Nesting reusable workflows | 5 |
| R-1519 | Pass secrets explicitly at each level if deeper workflows need them. | operations engineers | operations | S-21 B: Passing secrets to nested workflows | 5 |
| R-1520 | Map step outputs to job outputs, then map job outputs to workflow outputs. | operations engineers | operations | S-21 B: Using outputs from a reusable workflow | 5 |
| R-1521 | Set value to a job-level output when you map workflow outputs. | operations engineers | operations | S-21 B: Using outputs from a reusable workflow | 5 |
| R-1522 | Set cache-mode to the least access needed. | operations engineers | operations | S-21 B: Controlling cache access in reusable workflows | 5 |
| R-1523 | A called workflow cannot request more cache access than the caller allows, or the run fails validation. | operations engineers | operations | S-21 B: Controlling cache access in reusable workflows | 5 |
| R-1524 | Use a commit SHA as the reference, which the page recommends for stability and security. | security engineers | security | S-21 B: version references (section not confirmed) | C-10 |
| R-1525 | Components have to be versioned with semantic versioning when released to the CI/CD Catalog | project maintainers | operations | S-22 Component versions; Publish a new release | C-32 |
| R-1526 | A project that is a catalog project must have a description, a README and components | project maintainers | operations | S-22 Publish a component project | 5 |
| R-1527 | The release must be created with the release keyword in a CI/CD job, not with the Releases API | project maintainers | operations | S-22 Publish a new release | 5 |
| R-1528 | The tag pipeline should test the components before the release job runs | project maintainers | quality | S-22 Publish a new release | C-37 |
| R-1529 | The tag must use semantic versioning | project maintainers | operations | S-22 Publish a new release | C-32 |
| R-1530 | To publish, a user must have the Owner role on the project | project maintainers | operations | S-22 Set a component project as a catalog project | 5 |
| R-1531 | To release, a user must have the Maintainer or Owner role on the project | project maintainers | operations | S-22 Publish a new release | C-32 |
| R-1532 | To use a component, a user must have the Reporter, Developer, Maintainer or Owner role | consumers | quality | S-22 CI/CD Catalog | C-47 |
| R-1533 | To view catalog analytics, a user must have the Maintainer or Owner role for one or more catalog resource projects | project maintainers | operations | S-22 CI/CD Catalog | 5 |
| R-1534 | To view component usage details, a user must have the Maintainer or Owner role on the catalog project | project maintainers | operations | S-22 CI/CD Catalog | C-33 |
| R-1535 | A component that needs different versioning should move to its own project | project maintainers | operations | S-22 Component project | C-32 |
| R-1536 | Each component project needs a README file and a top-level templates directory | project maintainers | operations | S-22 Directory structure | C-33 |
| R-1537 | Each component project should have a LICENSE file and a pipeline that tests and releases components | project maintainers | operations | S-22 Directory structure | C-33 |
| R-1538 | Components should be self-contained and must not depend on external files; spec include is not allowed | project maintainers | operations | S-22 Component spec section | 5 |
| R-1539 | Components should be tested, covering behavior and side effects, with authentication for private projects | project maintainers | quality | S-22 Write a component; Test the component | C-37 |
| R-1540 | Keep dependencies minimal, pin components from other projects to catalog releases, and update them regularly | project maintainers | security | S-22 Write a component, Manage dependencies | C-10 |
| R-1541 | Less-privileged tools should be preferred, such as Buildah over a privileged Docker daemon | project maintainers | security | S-22 Write a component (best practices) | C-02 |
| R-1542 | Inputs should be preferred over custom variables | project maintainers | operations | S-22 Write a component (best practices) | 5 |
| R-1543 | Hardcoded instance and project values, global keywords and hardcoded stage or job names should be avoided | project maintainers | operations | S-22 Write a component (best practices) | 5 |
| R-1544 | Stage and job names should be set through inputs, and instance values should use the predefined CI variables | project maintainers | operations | S-22 Replace hardcoded values | 5 |
| R-1545 | Components should be carefully reviewed before use in a project | consumers | security | S-22 CI/CD component security best practices, For component users | C-20 |
| R-1546 | Sensitive-data components should be audited before use | consumers | security | S-22 Use a component | C-20 |
| R-1547 | Source code should be audited, tokens should be minimal and short-lived, and SHAs should be pinned | consumers | security | S-22 Security, for users | C-04 |
| R-1548 | Ephemeral runners should be used, and cache and artifact sharing should be limited | consumers | security | S-22 Security, for users | C-07 |
| R-1549 | Access for CI_JOB_TOKEN should be restricted | consumers | operations | S-22 Security, for users | 5 |
| R-1550 | Two-factor authentication should be enabled | project maintainers | security | S-22 Security, for maintainers | C-02 |
| R-1551 | Protected branches should be used, and commits should be signed | project maintainers | security | S-22 Security, for maintainers | C-03 |
| R-1552 | The use of latest should be avoided when recommending a component | project maintainers | security | S-22 Security, for maintainers | C-10 |
| R-1553 | Merge request approvals should be required | project maintainers | security | S-22 Security, for maintainers | C-03 |
| R-1554 | Catalog-published versions should be used where possible | consumers | operations | S-22 Component versions | C-33 |
| R-1555 | Self-managed instances should allow outbound requests to gitlab.com to mirror components | build platform operators | operations | S-22 Self-managed mirror | 5 |
| R-1556 | Config names that could collide with component names should be checked unless the override is intended | consumers | operations | S-22 Use a component | 5 |
| R-1557 | Teams must be self-sufficient to work at scale. | managers | operations | S-23 Philosophy, Self-Service Model | C-34 |
| R-1558 | Build tools must allow consistency and repeatability. | security engineers | security | S-23 Philosophy, Hermetic Builds | C-21 |
| R-1559 | The build process must be self-contained and must not rely on services external to the build environment. | security engineers | security | S-23 Philosophy, Hermetic Builds | C-21 |
| R-1560 | Almost all changes to the codebase require a code review. | security engineers | security | S-23 Philosophy, Enforcement of Policies and Procedures | C-03 |
| R-1561 | Changes from a release branch are never merged back into the mainline. | operations engineers | operations | S-23 Continuous Build and Deployment, Branching | C-32 |
| R-1562 | Release engineering recommends that continuous build test targets correspond to the test targets that gate the release. | software engineers | quality | S-23 Continuous Build and Deployment, Testing | C-37 |
| R-1563 | Releases are recommended at the revision number of the last continuous test build. | operations engineers | operations | S-23 Continuous Build and Deployment, Testing | C-32 |
| R-1564 | The deployment process should fit the risk profile of each service. This is a stated goal. | operations engineers | operations | S-23 Continuous Build and Deployment, Deployment | C-24 |
| R-1565 | Project owners should consider the configuration distribution options and decide case by case. | project maintainers | operations | S-23 Configuration Management | C-26 |
| R-1566 | Developers and SREs should not need to worry about releasing software. | operations engineers | operations | S-23 Conclusions, It's Not Just for Googlers | C-34 |
| R-1567 | Companies should decide their versioning approach. | managers | operations | S-23 Conclusions, It's Not Just for Googlers | C-32 |
| R-1568 | Companies should decide their release cadence. | managers | operations | S-23 Conclusions, It's Not Just for Googlers | C-32 |
| R-1569 | Companies should decide their configuration management policies. | managers | operations | S-23 Conclusions, It's Not Just for Googlers | C-35 |
| R-1570 | All companies should define their release processes. | managers | operations | S-23 Conclusions, It's Not Just for Googlers | C-32 |
| R-1571 | Policies must first be defined before features are added to the tools. | managers | quality | S-23 Conclusions, It's Not Just for Googlers | C-48 |
| R-1572 | The way of thinking about release engineering must change as platforms and services grow. | managers | quality | S-23 Conclusions, It's Not Just for Googlers | C-48 |
| R-1573 | Teams should budget for release engineering resources at the beginning of the product development cycle. | managers | quality | S-23 Conclusions, Start Release Engineering at the Beginning | C-48 |
| R-1574 | It is essential that developers, SREs and release engineers work together. | operations engineers | operations | S-23 Conclusions, Start Release Engineering at the Beginning | C-34 |
| R-1575 | The release engineer needs to understand how the code should be built and deployed. | operations engineers | operations | S-23 Conclusions, Start Release Engineering at the Beginning | C-24 |
| R-1576 | Developers should not build results and throw them over the fence to release engineers. | software engineers | operations | S-23 Conclusions, Start Release Engineering at the Beginning | C-34 |
| R-1577 | SREs need binaries and configurations built in a reproducible, automated way. | operations engineers | security | S-23 section not confirmed; see point 8 | C-21 |
| R-1578 | Changes to any aspect of the release process should be intentional, rather than accidental. | operations engineers | operations | S-23 section not confirmed; see point 8 | C-32 |
| R-1579 | Validate configuration syntax and, where possible, semantics | operations engineers | operations | S-23 Appendix B, Fail Sanely | C-26 |
| R-1580 | Watch for empty, partial, or truncated configuration data | operations engineers | operations | S-23 Appendix B, Fail Sanely | C-26 |
| R-1581 | Alert well before delayed data expires | operations engineers | operations | S-23 Appendix B, Fail Sanely | C-28 |
| R-1582 | On implausible input, keep operating in the previous state and alert on the bad input; generally, await human approval before using new data | operations engineers | operations | S-23 Appendix B, Fail Sanely | C-30 |
| R-1583 | Nonemergency rollouts must proceed in stages, applied to small fractions of traffic and capacity | operations engineers | operations | S-23 Appendix B, Progressive Rollouts | C-25 |
| R-1584 | Stage rollouts across geographies to catch diurnal and regional traffic problems | operations engineers | operations | S-23 Appendix B, Progressive Rollouts | C-25 |
| R-1585 | Supervise rollouts through an engineer or, preferably, a reliable monitoring system | software engineers | operations | S-23 Appendix B, Progressive Rollouts | C-28 |
| R-1586 | On unexpected behavior, roll back first and diagnose afterward | operations engineers | operations | S-23 Appendix B, Progressive Rollouts | C-25 |
| R-1587 | Measure availability and performance in terms that matter to end users | consumers | operations | S-23 Appendix B, Define SLOs Like a User | C-27 |
| R-1588 | An error budget is 1 minus the SLO, usually tracked monthly | operations engineers | operations | S-23 Appendix B, Error Budgets | C-27 |
| R-1589 | When the error budget is spent, freeze changes except urgent security and bug fixes until the budget recovers or the period resets | operations engineers | operations | S-23 Appendix B, Error Budgets | C-27 |
| R-1590 | Services with SLOs above 99.99% should use quarterly budget resets | operations engineers | operations | S-23 Appendix B, Error Budgets | C-27 |
| R-1591 | Monitoring output is limited to pages, tickets, or logging | operations engineers | operations | S-23 Appendix B, Monitoring | C-28 |
| R-1592 | Anything important enough to need attention must page or become a bug | operations engineers | operations | S-23 Appendix B, Monitoring | C-28 |
| R-1593 | Keep postmortems blameless and focused on process and technology | operations engineers | operations | S-23 Appendix B, Postmortems | C-29 |
| R-1594 | Fix the environment, not the people: improve system design, make information available, and automatically validate operational decisions | operations engineers | operations | S-23 Appendix B, Postmortems | C-29 |
| R-1595 | Provision for an N+2 configuration so that peak traffic can be handled during simultaneous planned and unplanned outages | operations engineers | operations | S-23 Appendix B, Capacity Planning | C-30 |
| R-1596 | Validate demand forecasts against actual results | operations engineers | operations | S-23 Appendix B, Capacity Planning | C-30 |
| R-1597 | Use load testing, not tradition, to set resource-to-capacity ratios | operations engineers | operations | S-23 Appendix B, Capacity Planning | C-30 |
| R-1598 | Do not mistake launch-day load for steady-state load | operations engineers | operations | S-23 Appendix B, Capacity Planning | C-30 |
| R-1599 | Degrade gracefully and return reasonable, if suboptimal, results under overload | operations engineers | operations | S-23 Appendix B, Overloads and Failure | C-30 |
| R-1600 | Test clusters beyond rated capacity | operations engineers | operations | S-23 Appendix B, Overloads and Failure | C-30 |
| R-1601 | Practice graceful load shedding using well-behaved queuing and dynamic timeouts | operations engineers | operations | S-23 Appendix B, Overloads and Failure | C-30 |
| R-1602 | During cascading failures, drop a fraction of traffic upstream, including retries, once load exceeds capacity | operations engineers | operations | S-23 Appendix B, Overloads and Failure | C-30 |
| R-1603 | Every RPC client must use exponential backoff with jitter for retries | operations engineers | operations | S-23 Appendix B, Overloads and Failure | C-30 |
| R-1604 | Limit SRE operational work to 50% of time, and send overflow to the product development team | operations engineers | operations | S-23 Appendix B, SRE Teams | C-34 |
| R-1605 | Include product developers in on-call rotations and ticket handling | managers | operations | S-23 Appendix B, SRE Teams | C-34 |
| R-1606 | Hold regular SRE and development production meetings | operations engineers | operations | S-23 Appendix B, SRE Teams | C-34 |
| R-1607 | Staff on-call with at least eight people across two geographic sites | operations engineers | operations | S-23 Appendix B, SRE Teams | C-29 |
| R-1608 | Expect no more than two events per on-call shift | operations engineers | operations | S-23 Appendix B, SRE Teams | C-29 |
| R-1609 | Routinely practice hypothetical outages and keep incident documentation current | operations engineers | operations | S-23 Appendix B, SRE Teams | C-29 |
| R-1610 | SLOs should specify how they are measured and the conditions under which they are valid | operations engineers | operations | S-23 Chapter 4, Objectives | C-27 |
| R-1611 | Use multiple SLO targets to capture the shape of a performance curve | operations engineers | operations | S-23 Chapter 4, Objectives | C-27 |
| R-1612 | Heterogeneous workloads may need separate objectives per class | operations engineers | operations | S-23 Chapter 4, Objectives | C-27 |
| R-1613 | The error budget should be tracked daily or weekly | operations engineers | operations | S-23 Chapter 4, Objectives | C-27 |
| R-1614 | Error budget review for management is monthly or quarterly | managers | operations | S-23 Chapter 4, Objectives | C-27 |
| R-1615 | Use only a handful of representative SLIs, chosen from what users care about | operations engineers | operations | S-23 Chapter 4, Indicators in Practice | C-27 |
| R-1616 | Some indicators should be collected client-side | operations engineers | operations | S-23 Chapter 4, Indicators in Practice | C-28 |
| R-1617 | Percentiles are preferred over means, and normal distribution must not be assumed without verification | operations engineers | operations | S-23 Chapter 4, Indicators in Practice | C-27 |
| R-1618 | Standardize SLI definitions with reusable templates | operations engineers | operations | S-23 Chapter 4, Indicators in Practice | C-27 |
| R-1619 | Start from what users care about, not from what is easy to measure | operations engineers | operations | S-23 Chapter 4, Objectives in Practice | C-27 |
| R-1620 | Do not pick targets based on current performance | operations engineers | operations | S-23 Chapter 4, Objectives in Practice | C-27 |
| R-1621 | Keep SLI aggregations simple, avoid absolute requirements, and use as few SLOs as possible | operations engineers | operations | S-23 Chapter 4, Objectives in Practice | C-27 |
| R-1622 | Start with a loose target and tighten it over time | operations engineers | operations | S-23 Chapter 4, Objectives in Practice | C-27 |
| R-1623 | SLOs should drive prioritization for SREs and product developers | operations engineers | operations | S-23 Chapter 4, Objectives in Practice | C-27 |
| R-1624 | Use SLIs and SLOs in a loop: monitor SLIs, compare them to SLOs, decide whether action is needed, determine what action will meet the target, and act | operations engineers | operations | S-23 Chapter 4, Control Measures | C-27 |
| R-1625 | Keep a safety margin by using a tighter internal SLO than the published one | operations engineers | operations | S-23 Chapter 4, SLOs Set Expectations | C-27 |
| R-1626 | Do not overachieve against the SLO | operations engineers | operations | S-23 Chapter 4, SLOs Set Expectations | C-27 |
| R-1627 | Be conservative in what is advertised | operations engineers | operations | S-23 Chapter 4, Agreements in Practice | C-27 |
| R-1628 | SRE ensures that a global service meets, but does not significantly exceed, its SLO | operations engineers | operations | S-23 Chapter 4, Global Chubby Planned Outage (sidebar) | C-27 |
| R-1629 | Monitoring should address both what is broken and why. | operations engineers | operations | S-23 page 1, "Symptoms Versus Causes" | C-28 |
| R-1630 | Monitoring must not trigger an alert only because something seems a bit weird. | operations engineers | operations | S-23 page 1, "Why Monitor" | C-28 |
| R-1631 | Monitoring systems should be kept simple and comprehensible, especially the path from problem onset to paging. | operations engineers | operations | S-23 page 1, "Setting Reasonable Expectations for Monitoring" | C-28 |
| R-1632 | Elements that page humans should be very simple and robust, and alert rules should represent a clear failure. | operations engineers | operations | S-23 page 1, "Setting Reasonable Expectations for Monitoring" | C-28 |
| R-1633 | White-box monitoring should be used heavily and black-box monitoring in critical but limited ways. | operations engineers | operations | S-23 page 1, "Black-Box Versus White-Box" | C-28 |
| R-1634 | Dashboards should answer basic questions and should normally include the four golden signals. | operations engineers | operations | S-23 page 1, "The Four Golden Signals" | C-28 |
| R-1635 | All four golden signals should be measured, and a page should be sent when one is problematic. | operations engineers | operations | S-23 page 1, "The Four Golden Signals" | C-28 |
| R-1636 | Error latency should be tracked separately and errors should not be filtered out. | operations engineers | operations | S-23 page 1, "The Four Golden Signals" | C-28 |
| R-1637 | A utilization target should be used for saturation. | operations engineers | operations | S-23 page 1, "The Four Golden Signals" | C-28 |
| R-1638 | Distributions should be measured and not only means. | operations engineers | operations | S-23 page 1, "Worrying About Your Tail" | C-28 |
| R-1639 | Rules that catch the most common real incidents should be simple, predictable and reliable. | operations engineers | operations | S-23 page 1, "As Simple as Possible" | C-28 |
| R-1640 | Unused data and signals should be considered for removal. | operations engineers | operations | S-23 page 1, "As Simple as Possible" | C-28 |
| R-1641 | Monitoring-adjacent systems should be kept loosely coupled through stable integration points. | operations engineers | operations | S-23 page 1, "As Simple as Possible" | C-28 |
| R-1642 | Each page should be actionable, require intelligence and concern a novel problem. | operations engineers | operations | S-23 page 1, "Tying Principles Together" | C-28 |
| R-1643 | More effort should go into symptoms than into causes. | operations engineers | operations | S-23 page 1, "Tying Principles Together" | C-28 |
| R-1644 | Alerts that become frequent and rote should be automated or their root causes removed. | operations engineers | operations | S-23 page 1, "Monitoring for the Long Term" | C-34 |
| R-1645 | Rote, algorithmic paging responses should be treated as a red flag and escalated if the team resists automating them. | operations engineers | operations | S-23 page 1, Gmail case study | C-34 |
| R-1646 | Dashboards should be preferred over email alerts, and dashboards should be paired with logs for historical correlation. | operations engineers | operations | S-23 page 1, "Conclusion" | C-28 |
| R-1647 | A postmortem must be written for any significant undesirable event. The page says postmortems are "expected" for such events. | operations engineers | operations | S-23 page 2, "Google's Postmortem Philosophy" | C-29 |
| R-1648 | Postmortem criteria should be defined before an incident occurs. | operations engineers | operations | S-23 page 2, "Google's Postmortem Philosophy" | C-29 |
| R-1649 | A blameless postmortem must focus on contributing causes. | operations engineers | operations | S-23 page 2, "Blameless postmortems" | C-29 |
| R-1650 | A blameless postmortem should still identify where services can improve. | operations engineers | operations | S-23 page 2, "Blameless postmortems" | C-29 |
| R-1651 | Teams should avoid stigmatizing people or teams that produce frequent postmortems. | software engineers | operations | S-23 page 2, "Avoid Blame" | C-29 |
| R-1652 | Drafts should go through internal review, and postmortems should be shared as widely as useful. | operations engineers | operations | S-23 page 2, "Collaborate and Share Knowledge" | C-29 |
| R-1653 | End-user identifying information must not be included in postmortems, under Google's privacy rules. | operations engineers | operations | S-23 page 2, "Collaborate and Share Knowledge" | C-29 |
| R-1654 | Teams should hold regular review sessions, and completed postmortems should go into a repository. | software engineers | operations | S-23 page 2, "No Postmortem Left Unreviewed" | C-29 |
| R-1655 | Postmortem writing should be eased into the workflow, effective writing should be rewarded, and senior leadership should be encouraged to take part. | managers | operations | S-23 page 2, "Introducing a Postmortem Culture" | C-29 |
| R-1656 | Teams should survey people on whether the process supports their goals and whether it creates excess toil. | software engineers | quality | S-23 page 2, "Ask for Feedback" | C-52 |
| R-1657 | By default, one LGTM of a reviewer is required, and the author must resolve all comments before committing. | software engineers | security | S-24 ch09: Code Review Flow | C-03 |
| R-1658 | Authors should resolve all comments before they commit a change. | software engineers | security | S-24 ch09: Code Review Flow | C-03 |
| R-1659 | A change must include owner approval for each directory it touches. | managers | security | S-24 ch09: How Code Review Works at Google | C-03 |
| R-1660 | An engineer should confirm that a new feature is warranted before writing its code. | software engineers | quality | S-24 ch09: Code Is a Liability | C-48 |
| R-1661 | An engineer should search for existing utility code before writing a new utility, using Code Search. | software engineers | operations | S-24 ch09: Code Is a Liability | C-33 |
| R-1662 | Ideally, a design for anything new is communicated to the proper groups before any new code is written. | software engineers | quality | S-24 ch09: Code Is a Liability | C-47 |
| R-1663 | Reviews should not reopen design decisions that were already made. | software engineers | quality | S-24 ch09: Code Is a Liability, Note | C-47 |
| R-1664 | Teams should keep OWNERS lists relatively small and focused. | software engineers | quality | S-24 ch09: Ownership | C-50 |
| R-1665 | Teams should not use ownership as an initiation rite. | software engineers | quality | S-24 ch09: Ownership | C-50 |
| R-1666 | Departing members should transfer ownership as soon as practical. | managers | quality | S-24 ch09: Ownership | C-50 |
| R-1667 | Owners understand the owned code, or know who does. | managers | quality | S-24 ch09: Ownership, Responsibilities of owners | C-49 |
| R-1668 | Reviewers should check testing, design and function. | software engineers | security | S-24 ch09: Code Correctness | C-03 |
| R-1669 | Proposed alternatives should be limited to improvements in comprehension or function. | software engineers | security | S-24 ch09: Code Correctness | C-03 |
| R-1670 | Reviewers should approve changes that improve the codebase rather than wait for a perfect solution. | software engineers | security | S-24 ch09: Code Correctness, Guidance | C-03 |
| R-1671 | Reviewers should check that the code is comprehensible. | software engineers | security | S-24 ch09: Comprehension of Code | C-03 |
| R-1672 | An author should be ready to explain their code. | software engineers | security | S-24 ch09: Comprehension of Code | C-03 |
| R-1673 | Reviewer questions on comprehension should be treated as valid, and the author should explain more clearly if needed. | software engineers | security | S-24 ch09: Comprehension of Code | C-03 |
| R-1674 | Code should follow language standards and codebase patterns, and avoid unnecessary complexity. | software engineers | quality | S-24 ch09: Code Consistency | C-40 |
| R-1675 | Reviewers should defer to the author's approach unless the approach is deficient. | software engineers | security | S-24 ch09: Be Polite and Professional | C-03 |
| R-1676 | Feedback should stay professional. | software engineers | quality | S-24 ch09: Be Polite and Professional | C-49 |
| R-1677 | Reviewers should ask questions before they assume an approach is wrong. | software engineers | security | S-24 ch09: Be Polite and Professional | C-03 |
| R-1678 | Authors should treat each comment as a to-do item. | software engineers | security | S-24 ch09: Be Polite and Professional | C-03 |
| R-1679 | Authors should not resolve a comment while a disagreement about it is unresolved. | software engineers | security | S-24 ch09: Be Polite and Professional | C-03 |
| R-1680 | Owners should accept outside changes that improve the codebase. | managers | quality | S-24 ch09: Be Polite and Professional | C-50 |
| R-1681 | Reviewers should avoid piecemeal feedback. | software engineers | security | S-24 ch09: Be Polite and Professional, Guidance | C-03 |
| R-1682 | If feedback within 24 working hours is not possible, the reviewer should at least acknowledge the change. | software engineers | security | S-24 ch09: Be Polite and Professional | C-03 |
| R-1683 | Changes should be small, focused on one issue, and ideally about 200 lines. | operations engineers | operations | S-24 ch09: Write Small Changes | C-25 |
| R-1684 | The first line of a change description should summarize the change type. | security engineers | security | S-24 ch09: Write Good Change Descriptions | C-01 |
| R-1685 | The description should explain what changed and why. | security engineers | security | S-24 ch09: Write Good Change Descriptions | C-01 |
| R-1686 | Implementation details belong in code comments. | software engineers | quality | S-24 ch09: Write Good Change Descriptions | C-40 |
| R-1687 | Descriptions and comments should be updated when decisions change. | software engineers | quality | S-24 ch09: Write Good Change Descriptions | C-40 |
| R-1688 | Use one primary reviewer whose LGTM is needed. | security engineers | security | S-24 ch09: Keep Reviewers to a Minimum | C-03 |
| R-1689 | Additional reviewers should focus on different aspects. | software engineers | security | S-24 ch09: Keep Reviewers to a Minimum | C-03 |
| R-1690 | Mechanical checks should be automated, using presubmits for tests, linters and formatters. | security engineers | security | S-24 ch09: Automate Where Possible | C-14 |
| R-1691 | New code should be checked against an agreed design. | software engineers | quality | S-24 ch09: Greenfield Code Reviews | C-47 |
| R-1692 | In a greenfield review, reviewers check that all API endpoints have some form of unit test that fails when the assumptions of the code change. | software engineers | quality | S-24 ch09: Greenfield Code Reviews | C-38 |
| R-1693 | New code should have proper owners, comments and documentation where needed. | software engineers | quality | S-24 ch09: Greenfield Code Reviews | C-45 |
| R-1694 | New projects should be added to continuous integration. | software engineers | quality | S-24 ch09: Greenfield Code Reviews | C-37 |
| R-1695 | Extensive design review should happen separately from code review. | software engineers | quality | S-24 ch09: Greenfield Code Reviews | C-47 |
| R-1696 | Behavioral changes should update the relevant tests. | software engineers | quality | S-24 ch09: Behavioral Changes, Improvements, and Optimizations | C-38 |
| R-1697 | Changes should run in CI. | software engineers | quality | S-24 ch09: Behavioral Changes, Improvements, and Optimizations | C-37 |
| R-1698 | Bug fixes should address only the reported bug and update tests to catch it. | software engineers | quality | S-24 ch09: Bug Fixes and Rollbacks | C-38 |
| R-1699 | Reviewers should ask for test updates on bug fixes. | software engineers | security | S-24 ch09: Bug Fixes and Rollbacks | C-03 |
| R-1700 | Changes should be small and atomic so that rollbacks are safe. | operations engineers | operations | S-24 ch09: Bug Fixes and Rollbacks | C-25 |
| R-1701 | Automated changes still require review, by designated reviewers for low-risk changes or by individual engineers for riskier ones. | software engineers | security | S-24 ch09: Refactorings and Large-Scale Changes | C-03 |
| R-1702 | Reviewers should limit comments to concerns specific to their code. | software engineers | security | S-24 ch09: Refactorings and Large-Scale Changes | C-03 |
| R-1703 | Reviewers should not expand scope on automated changes. | software engineers | security | S-24 ch09: Refactorings and Large-Scale Changes | C-03 |
| R-1704 | Concerns about the tool or process should go to the LSC oversight group out of band. | managers | quality | S-24 ch09: Refactorings and Large-Scale Changes | C-48 |
| R-1705 | Do not use the review as an opportunity to introduce a new API design. | software engineers | quality | S-24 ch09: Instructions directed at readers | C-47 |
| R-1706 | Static analysis tools must scale to a multibillion-line codebase. | security engineers | security | S-24 ch20: Scalability | C-14 |
| R-1707 | Tool builders must track tool performance and act on developer feedback. | managers | quality | S-24 ch20: Developer Happiness | C-52 |
| R-1708 | Tool teams are responsible for updating tools alongside the workflow and code. | software engineers | operations | S-24 ch20: Usability | C-33 |
| R-1709 | Checks should be understandable to any engineer. | software engineers | security | S-24 ch20: Requirements, Tricorder checks | C-14 |
| R-1710 | Checks should be actionable and easy to fix, with guidance on how to fix the issue. | security engineers | security | S-24 ch20: Requirements, Tricorder checks | C-14 |
| R-1711 | Checks should produce fewer than 10% effective false positives. | security engineers | security | S-24 ch20: Requirements, Tricorder checks | C-14 |
| R-1712 | Checks should have potential for significant impact on code quality. | software engineers | quality | S-24 ch20: Requirements, Tricorder checks | C-40 |
| R-1713 | Analysis tools should only be deployed with low false-positive rates. | security engineers | security | S-24 ch20: Requirements, Warnings and fixes | C-14 |
| R-1714 | Existing issues should be highlighted only if they are particularly important. | security engineers | security | S-24 ch20: Requirements, Warnings and fixes | C-14 |
| R-1715 | Anything that can be fixed automatically should be fixed automatically, especially style issues. | software engineers | quality | S-24 ch20: Requirements, Warnings and fixes | C-40 |
| R-1716 | Fix guidance should be included in results. | security engineers | security | S-24 ch20: Requirements, Warnings and fixes | C-14 |
| R-1717 | Compiler checks must be fast so that they do not slow the build. | software engineers | quality | S-24 ch20: Requirements, Compiler checks | C-44 |
| R-1718 | Compiler errors should be actionable and easy to fix, ideally with a mechanically applied suggested fix. | software engineers | quality | S-24 ch20: Requirements, Compiler checks | C-40 |
| R-1719 | Compiler checks should produce no effective false positives. | software engineers | quality | S-24 ch20: Requirements, Compiler checks | C-40 |
| R-1720 | Compiler checks should never stop the build for correct code. | software engineers | quality | S-24 ch20: Requirements, Compiler checks | C-40 |
| R-1721 | Compiler checks should report only correctness issues, not style or best practices. | software engineers | quality | S-24 ch20: Requirements, Compiler checks | C-40 |
| R-1722 | Compiler-based checks must produce fixes so that the codebase can be cleaned up automatically. | software engineers | quality | S-24 ch20: Requirements, Compiler checks | C-40 |
| R-1723 | IDE analyses need quick run times. | security engineers | security | S-24 ch20: Requirements, IDE integration | C-14 |
| R-1724 | Developer feedback channels should be established and analyses tuned to reduce false positives. | managers | quality | S-24 ch20: Requirements, Process | C-52 |
| R-1725 | Developers should feel that a check flags a real issue at least 90% of the time. | software engineers | quality | S-24 ch20: Measurable Targets table, Warning review | C-52 |
| R-1726 | Static analysis should be made part of the core developer workflow. | security engineers | security | S-24 ch20: TL;DRs | C-14 |
| R-1727 | Developer happiness and build feedback channels should be the focus. | managers | quality | S-24 ch20: TL;DRs | C-52 |
| R-1728 | Users should be empowered to contribute analyses and checks. | managers | quality | S-24 ch20: TL;DRs | C-50 |
| R-1729 | Feedback from CI should be accessible to anyone and actionable | software engineers | quality | S-24 ch23, "Fast Feedback Loops" | C-37 |
| R-1730 | Teams should aim for fast feedback loops that catch bugs early | software engineers | quality | S-24 ch23, "Fast Feedback Loops" | C-37 |
| R-1731 | After a change is submitted, the team should run all relevant tests | software engineers | quality | S-24 ch23, "Automation / Continuous Build" | C-37 |
| R-1732 | Static configuration should be promoted with the release candidate and kept in version control | operations engineers | operations | S-24 ch23, "Automation / Continuous Delivery" | C-26 |
| R-1733 | Build artifacts should not be recompiled as they move between environments | operations engineers | operations | S-24 ch23, "Automation / Continuous Delivery" | C-24 |
| R-1734 | Presubmit should run only fast, reliable tests, limited mostly to the project's own tests | software engineers | quality | S-24 ch23, "Continuous Testing / Why presubmit isn't enough" | C-37 |
| R-1735 | Slower or less reliable tests should move to post-submit | software engineers | quality | S-24 ch23, "Continuous Testing / Why presubmit isn't enough" | C-37 |
| R-1736 | A comprehensive automated suite should run against each release candidate | software engineers | quality | S-24 ch23, "Continuous Testing / Release candidate testing and Production testing" | C-37 |
| R-1737 | The same comprehensive suite should run against production | software engineers | quality | S-24 ch23, "Continuous Testing / Release candidate testing and Production testing" | C-37 |
| R-1738 | Failing tests should be investigated before commits are accepted | software engineers | quality | S-24 ch23, "CI Is Alerting" | C-37 |
| R-1739 | Teams should be liberal in accepting changes that disable a test failing for irrelevant reasons | software engineers | quality | S-24 ch23, "CI Is Alerting" | C-38 |
| R-1740 | Teams should use hermetic tests on presubmit where stability matters most | software engineers | security | S-24 ch23, "Hermetic Testing" | C-21 |
| R-1741 | Teams should consider record/replay for large systems | software engineers | quality | S-24 ch23, "Hermetic Testing" | C-38 |
| R-1742 | Teams should track disabled or broken tests so they do not accumulate | software engineers | quality | S-24 ch23, "CI Challenges" | C-38 |
| R-1743 | Release-blocking failures should be fixed immediately | software engineers | quality | S-24 ch23, "CI Challenges" | C-37 |
| R-1744 | Teams should weigh the cost of production problems against the cost of building CI | software engineers | quality | S-24 ch23, "But I Can't Afford CI" | C-48 |
| R-1745 | Releases should be frequent and in small batches | operations engineers | operations | S-24 ch24, "Idioms of Continuous Delivery at Google" | C-25 |
| R-1746 | Repetitive overhead of frequent releases should be reduced or removed through automation | operations engineers | operations | S-24 ch24, "Idioms of Continuous Delivery at Google" | C-24 |
| R-1747 | A modular architecture that isolates changes should be built | software engineers | quality | S-24 ch24, "Idioms of Continuous Delivery at Google" | C-47 |
| R-1748 | Health indicators such as crashes and latency should be measured and kept improving | operations engineers | operations | S-24 ch24, "Idioms of Continuous Delivery at Google" | C-28 |
| R-1749 | A/B testing on health metrics should be used to ensure quality | operations engineers | operations | S-24 ch24, "Idioms of Continuous Delivery at Google" | C-28 |
| R-1750 | Changes should be rolled out to a few users before everyone | operations engineers | operations | S-24 ch24, "Idioms of Continuous Delivery at Google" | C-25 |
| R-1751 | Development should keep to head in the shared codebase, not branch in subteams | software engineers | operations | S-24 ch24, "Velocity Is a Team Sport" | C-35 |
| R-1752 | Quick operational fixes should be resisted in favour of long-term architectural investment | software engineers | quality | S-24 ch24, "Velocity Is a Team Sport" | C-47 |
| R-1753 | Migration to a microservice architecture, or a rewrite, should be considered to reduce risk | software engineers | quality | S-24 ch24, "Velocity Is a Team Sport" | C-47 |
| R-1754 | All changes should be flag guarded | operations engineers | operations | S-24 ch24, "Evaluating Changes in Isolation" | C-25 |
| R-1755 | A configuration service that manages safe flag rollouts should be invested in | operations engineers | operations | S-24 ch24, "Evaluating Changes in Isolation" | C-25 |
| R-1756 | A flag should not be enabled for all users at once | operations engineers | operations | S-24 ch24, "Evaluating Changes in Isolation" | C-25 |
| R-1757 | Release deadlines should be set, and new features should not be accepted after them except rarely | operations engineers | operations | S-24 ch24, "Striving for Agility" | C-32 |
| R-1758 | KPI thresholds should be defined so features can launch despite imperfections | operations engineers | operations | S-24 ch24, "Striving for Agility" | C-27 |
| R-1759 | Release frequency should be decided intentionally, separate from how often users receive releases | operations engineers | operations | S-24 ch24, "Ship Only What Gets Used" | C-32 |
| R-1760 | Code should be kept modular, with dynamic deployments so devices receive only needed code | software engineers | quality | S-24 ch24, "Ship Only What Gets Used" | C-47 |
| R-1761 | Dedicated teams should be staffed to improve product efficiency on an ongoing basis | managers | quality | S-24 ch24, "Ship Only What Gets Used" | C-52 |
| R-1762 | Representative testing should be used when comprehensive testing is infeasible | software engineers | quality | S-24 ch24, "Shifting Left" | C-38 |
| R-1763 | Staged rollouts to increasing user percentages should be used | operations engineers | operations | S-24 ch24, "Shifting Left" | C-25 |
| R-1764 | A/B releases should be automated, and change-neutral releases used when the userbase is too small | operations engineers | operations | S-24 ch24, "Shifting Left" | C-25 |
| R-1765 | New features should be isolated behind interfaces with strong contracts, rigorous testing and early communication | software engineers | quality | S-24 ch24, "Changing Team Culture" | C-47 |
| R-1766 | Binaries should be configurable in production, with configuration managed as code in version control | operations engineers | operations | S-24 ch24, "Conclusion" | C-26 |
| R-1767 | A toolchain with dry-run verification, rollback or rollforward, and reliable patching should be used | operations engineers | operations | S-24 ch24, "Conclusion" | C-25 |
| R-1768 | Error budgets should be used to balance velocity against stability, rather than pursuing perfection | operations engineers | operations | S-24 ch24, footnote 1 | C-27 |
| R-1769 | Developers should write automated tests for their code and treat them as production-quality code. | software engineers | quality | S-24 Benefits of Testing Code; Pitfalls of a Large Test Suite | C-37 |
| R-1770 | Engineers should write the smallest test that covers each behavior. | software engineers | quality | S-24 Test Size | C-38 |
| R-1771 | Small tests must run in one process, avoid sleeping, I/O and blocking calls, and use test doubles for heavy dependencies. | software engineers | quality | S-24 Small tests | C-38 |
| R-1772 | Medium tests must stay on one machine, with no network calls beyond localhost. | software engineers | quality | S-24 Medium tests | C-38 |
| R-1773 | Large tests should be reserved for end-to-end or legacy cases and run separately from fast suites. | software engineers | quality | S-24 Large tests | C-38 |
| R-1774 | All tests should be hermetic and make minimal assumptions about the environment or execution order. | security engineers | security | S-24 Properties common to all test sizes | C-21 |
| R-1775 | Tests should be simple and obvious, avoiding conditionals and loops. | software engineers | quality | S-24 Properties common to all test sizes | C-38 |
| R-1776 | Engineers should prefer real dependencies over doubles where feasible. | software engineers | quality | S-24 Test Scope | C-38 |
| R-1777 | Teams should keep a balanced mix of unit, integration and end-to-end tests, and avoid the ice-cream-cone and hourglass shapes. | software engineers | quality | S-24 Test Scope | C-38 |
| R-1778 | Teams should test everything they do not want to break, including performance, accessibility, security and failure handling. | software engineers | quality | S-24 The Beyoncé Rule; Testing for Failure | C-38 |
| R-1779 | Teams should simulate failures such as exceptions, RPC errors and latency, rather than wait for real ones. | software engineers | quality | S-24 Testing for Failure | C-38 |
| R-1780 | Teams should measure coverage only from small tests and not treat a coverage percentage as a goal or ceiling. | software engineers | quality | S-24 A Note on Code Coverage | C-39 |
| R-1781 | Teams should run tests continuously, fix broken tests within minutes, and not let failures accumulate. | software engineers | quality | S-24 Write, Run, React | C-37 |
| R-1782 | Teams should poll for state changes instead of using fixed sleeps. | software engineers | quality | S-24 Pitfalls of a Large Test Suite | C-38 |
| R-1783 | Teams should invest in linters, documentation and fewer frameworks to make bad tests harder to write. | software engineers | quality | S-24 Pitfalls of a Large Test Suite | C-38 |
| R-1784 | Teams should not skip tests when submitting changes. | software engineers | quality | S-24 Pitfalls of a Large Test Suite | C-37 |
| R-1785 | Every code change must go through review and include tests, and reviewers may block changes that lack them. | security engineers | security | S-24 Testing Culture Today; Story of GWS | C-03 |
| R-1786 | Teams should use automated tests for well-understood behaviors, and add an automated test whenever exploratory testing finds a defect. | software engineers | quality | S-24 The Limits of Automated Testing | C-38 |
| R-1787 | Projects should use one standard test framework and one standard mocking library per language. | project maintainers | quality | S-24 footnote 8 | C-38 |
| R-1788 | Test Certified level 1 requires a continuous build, coverage tracking, test-size classification, flaky-test identification and a fast test set. | security engineers | security | S-24 Test Certified | C-22 |
| R-1789 | Organizations and engineering policy-setters should prefer source-control solutions over dependency-management solutions when all else is equal. | managers | quality | S-24 Introduction | C-51 |
| R-1790 | Engineers should reuse existing software when it meets their requirements, as long as it is not trojaned. | software engineers | security | S-24 Importing Dependencies | C-20 |
| R-1791 | Dependency providers should be clear about compatibility, evolution, change handling and support duration. | build platform operators | operations | S-24 Compatibility Promises | C-36 |
| R-1792 | Google engineers should ask the external-project questions before importing: tests, pass status, provider, compatibility aimed for, supported usage, popularity, expected lifetime of the dependency, and frequency of breaking changes. | software engineers | security | S-24 Considerations When Importing | C-20 |
| R-1793 | Google engineers should ask the internal questions: build cost in-house, who keeps it up to date, and who performs upgrades. | software engineers | security | S-24 Considerations When Importing | C-20 |
| R-1794 | Engineers should consider the ongoing costs before importing, and recognize whether they do a programming task or a software engineering task. | software engineers | quality | S-24 Considerations When Importing | C-48 |
| R-1795 | Engineers adding open-source packages to third_party should confirm the package builds with the build system, check that no existing version is present, and get at least two engineers listed as OWNERS. | project maintainers | security | S-24 How Google Handles Importing Dependencies | C-20 |
| R-1796 | third_party leads and codebase maintainers should set a higher bar for ownership, make regular updates easier and more rewarding, and prevent packages from becoming both orphaned and important. | suppliers | quality | S-24 How Google Handles Importing Dependencies | C-51 |
| R-1797 | Maintainers should be cautious with popular projects that make no compatibility promises, and with upstream projects that do not prioritize stability. | project maintainers | security | S-24 How Google Handles Importing Dependencies | C-20 |
| R-1798 | Designers of dependency-management solutions should avoid conflicting requirements of any form, including diamond-dependency version conflicts, even as the ecosystem changes. | managers | quality | S-24 Dependency Management, In Theory | C-51 |
| R-1799 | Dependency management should stay flexible with time and scale, and should not assume indefinite stability of any node or that no new dependencies will be added. | security engineers | security | S-24 Dependency Management, In Theory | C-20 |
| R-1800 | Dependency management should ideally avoid assuming stable versions, fixed fan-out, cross-organization coordination or large compute resources. | software engineers | quality | S-24 Dependency Management, In Theory | C-51 |
| R-1801 | API providers should test changes against downstream dependents through CI before committing. | build platform operators | quality | S-24 Live at Head | C-37 |
| R-1802 | API providers should make breaking changes only after downstream users are updated, or after an automated update tool is provided; this is essential for closed-source consumers. | build platform operators | operations | S-24 Live at Head | C-36 |
| R-1803 | API consumers should keep their tests passing and use dependencies in supported ways. | consumers | quality | S-24 Live at Head | C-37 |
| R-1804 | Maintainers should publish clear statements of intent about compatibility, expected usage and breaking changes. | project maintainers | operations | S-24 Motivations | C-36 |
| R-1805 | Maintainers of breaking changes should treat a major-version bump as a new package; repackaging and renaming is a reasonable expectation. | project maintainers | operations | S-24 Motivations | C-32 |
| R-1806 | Organizations with large dependency networks should prepare for some chaos from human versioning error. | managers | quality | S-24 Motivations | C-48 |
| R-1807 | Package-manager users should move forward in the smallest feasible steps, choose the minimum version that satisfies requirements, and then test. | consumers | quality | S-24 The Limitations of SemVer / Minimum Version Selection | C-51 |
| R-1808 | Every dependency must provide unit tests. | project maintainers | quality | S-24 Dependency Management with Infinite Resources | C-37 |
| R-1809 | The dependency graph must be understood and indexed. | project maintainers | security | S-24 Dependency Management with Infinite Resources | C-09 |
| R-1810 | CI compute must be available. | project maintainers | quality | S-24 Dependency Management with Infinite Resources | C-37 |
| R-1811 | Dependencies should not be pinned to specific versions. | project maintainers | security | S-24 Dependency Management with Infinite Resources | C-10 |
| R-1812 | History and reputation should be factored into CI. | project maintainers | security | S-24 Dependency Management with Infinite Resources | C-20 |
| R-1813 | Change authors should match test effort to risk; pure internal refactorings may need only local and sampled tests, and removing deprecated interfaces or changing observable behavior warrants as much testing as affordable. | software engineers | quality | S-24 Dependency Management with Infinite Resources | C-38 |
| R-1814 | Organizations releasing code should prioritize community over code and should not release software without a plan and mandate to support it long term. | managers | operations | S-24 Exporting Dependencies | C-36 |
| R-1815 | Organizations should weigh the long-term risks before releasing anything. | managers | quality | S-24 Exporting Dependencies | C-48 |
| R-1816 | API designers should prefer languages with strong control over public and private API access. | software engineers | quality | S-24 Exporting Dependencies | C-47 |
| R-1817 | Providers should take greater responsibility for testing against users and clearly state expected change types. | software engineers | quality | S-24 Conclusion | C-38 |
| R-1818 | Engineers should choose well-maintained dependencies when long-term stability matters. | security engineers | security | S-24 footnote 13 | C-20 |
| R-1819 | Engineers should account for ongoing support costs when adding dependencies. | software engineers | quality | S-24 TL;DRs | C-51 |
| R-1820 | Engineers should use testing and CI as evidence that versions work together. | software engineers | quality | S-24 TL;DRs | C-37 |
| R-1821 | Engineers should prefer minimum-version update strategies. | software engineers | quality | S-24 TL;DRs | C-51 |
| R-1822 | Providers and consumers should both carry responsibilities in the dependency contract, and providers should state what they promise over time. | build platform operators | quality | S-24 TL;DRs | C-51 |
| R-1823 | Engineers should treat SemVer as a lossy estimate, not an absolute. | operations engineers | operations | S-24 TL;DRs | C-32 |
| R-1824 | Engineers should invest in unit testing, CI and compute, and shift responsibilities accordingly. | software engineers | quality | S-24 TL;DRs | C-37 |
| R-1825 | Organizations should not release code with throw-it-over-the-wall neglect, and should not release it without a stability plan. | managers | operations | S-24 TL;DRs | C-36 |
| R-1826 | Teams should identify multiple metrics, including some with a healthy amount of tension between them. | software engineers | quality | S-25 GUIDE, Requirements (must/should) | C-52 |
| R-1827 | Teams should make each change as small as possible. | software engineers | operations | S-25 GUIDE, Next steps | C-25 |
| R-1828 | Teams should start with continuous delivery, even if they do not adopt continuous deployment. | software engineers | operations | S-25 CD, section 9 | C-24 |
| R-1829 | Teams should minimise the test data needed for automated tests. | software engineers | quality | S-25 CD, section 9 | C-38 |
| R-1830 | Representatives from all teams should take part in value stream mapping. | software engineers | quality | S-25 CD, section 9 | C-48 |
| R-1831 | Teams should agree on a common toolchain and deployment processes. | software engineers | operations | S-25 CD, section 9 | C-33 |
| R-1832 | Nobody should have to work outside business hours to deploy or release. | operations engineers | operations | S-25 CD, section 9 | C-24 |
| R-1833 | You need close collaboration across the delivery process to achieve reliable releases. | operations engineers | operations | S-25 CD, section 9 | C-34 |
| R-1834 | Each commit should trigger a build of the software. | software engineers | quality | S-25 CI, Requirements | C-37 |
| R-1835 | Each commit should trigger automated tests that give feedback in a few minutes. | software engineers | quality | S-25 CI, Requirements | C-37 |
| R-1836 | The build process should be automated, and its packages should be numbered and repeatable. | software engineers | quality | S-25 CI, Requirements | C-44 |
| R-1837 | Builds and tests should run successfully at least once a day. | software engineers | quality | S-25 CI, Requirements | C-37 |
| R-1838 | Tests must run in a few minutes or less. | software engineers | quality | S-25 CI, Requirements | C-37 |
| R-1839 | Tests should be reliable and comprehensive, and all new functionality should be covered. | software engineers | quality | S-25 CI, Requirements | C-38 |
| R-1840 | Everything needed to build and configure the system should be in the repository. | operations engineers | operations | S-25 CI, Requirements | C-26 |
| R-1841 | The CI system should make build status visible to the team. | software engineers | quality | S-25 CI, Requirements | C-37 |
| R-1842 | Broken builds should be fixed or reverted quickly, and fixing them takes priority over other work. | software engineers | quality | S-25 CI, Requirements | C-37 |
| R-1843 | Developers should merge into trunk at least daily. | software engineers | operations | S-25 CI, Requirements | C-35 |
| R-1844 | Organizations need to break large changes into small, incremental steps. | managers | operations | S-25 CI, Requirements | C-25 |
| R-1845 | Teams should improve test efficiency, add compute resources, or split long tests into separate builds. | software engineers | quality | S-25 CI, Requirements | C-37 |
| R-1846 | Teams must stop and fix the build when automated tests fail. | software engineers | quality | S-25 CI, Groups | C-37 |
| R-1847 | Organisations should treat helping teams adopt CI as a top priority on the path to continuous delivery. | managers | quality | S-25 CI, Groups | C-48 |
| R-1848 | You must continually run both automated and manual tests throughout the delivery process. | software engineers | quality | S-25 TA, Requirements | C-37 |
| R-1849 | Perform all types of testing continuously throughout the software delivery lifecycle. | software engineers | quality | S-25 TA, Requirements | C-38 |
| R-1850 | Developers should get feedback from automated tests in less than ten minutes, on local workstations and from continuous integration. | software engineers | quality | S-25 TA, How to implement automated testing | C-37 |
| R-1851 | No one should be able to declare their work dev complete unless automated acceptance tests are passing. | software engineers | quality | S-25 TA, Requirements | C-37 |
| R-1852 | Developers should practise test-driven development by writing unit tests before writing production code. | software engineers | quality | S-25 TA, Requirements | C-38 |
| R-1853 | Keep the test suite fast. | software engineers | quality | S-25 TA, Requirements | C-37 |
| R-1854 | Tests should be reliable. | software engineers | quality | S-25 TA, Requirements | C-38 |
| R-1855 | Keep your test suites well-factored. | software engineers | quality | S-25 TA, Requirements | C-37 |
| R-1856 | Make sure you continue to invest in making your software easy to test. | software engineers | quality | S-25 TA, Requirements | C-38 |
| R-1857 | Developers should write unit and acceptance tests for any new functionality. | software engineers | quality | S-25 TA, Requirements | C-38 |
| R-1858 | When acceptance tests break, unit tests should be written. | software engineers | quality | S-25 TA, Requirements | C-38 |
| R-1859 | Flaky tests should not be tolerated. | software engineers | quality | S-25 TA, Requirements | C-37 |
| R-1860 | The InfoSec team should get involved in the design phase for all projects. | software engineers | quality | S-25 PS, section 5 | C-47 |
| R-1861 | Engagement with InfoSec should increase over time until the organisation agrees oversight is at the correct level. | software engineers | security | S-25 PS, section 5 | C-19 |
| R-1862 | Automated testing requires designing and developing automated security tests. | security engineers | security | S-25 PS, section 5 | C-14 |
| R-1863 | Pre-approved code should be used in areas where it applies. | operations engineers | operations | S-25 PS, section 5 | C-33 |
| R-1864 | Conduct a security review for all major features. | security engineers | security | S-25 PS, section 6 | C-13 |
| R-1865 | Security reviews should not slow down development. | security engineers | security | S-25 PS, section 5 | C-13 |
| R-1866 | Your teams should have health reporting, customer-state, business metrics, debugging and tracing tools. | software engineers | operations | S-25 MO, Requirements | C-28 |
| R-1867 | Monitoring should tell you what is broken and help you understand why. | operations engineers | operations | S-25 MO, Requirements | C-28 |
| R-1868 | Your system must be instrumented. | operations engineers | operations | S-25 MO, Requirements | C-28 |
| R-1869 | Your system should also contain a validation engine. | operations engineers | operations | S-25 MO, Requirements | C-28 |
| R-1870 | The result and metadata of each probe must be stored. | operations engineers | operations | S-25 MO, Requirements | C-28 |
| R-1871 | Changes should be tracked by means of review and approval. | operations engineers | operations | S-25 MO, Requirements | C-31 |
| R-1872 | Cardinality and dimensionality must be considered. | operations engineers | operations | S-25 MO, Requirements | C-28 |
| R-1873 | Avoid having a single monitoring person or dedicated team. | operations engineers | operations | S-25 MO, Common pitfalls | C-34 |
| R-1874 | Cause-based alerting should be avoided as much as possible. | operations engineers | operations | S-25 MO, Common pitfalls | C-28 |
| R-1875 | Focus on symptom-based alerting. | operations engineers | operations | S-25 MO, Common pitfalls | C-28 |
| R-1876 | Monitoring should not directly alert on-call engineers without user-facing symptoms. | operations engineers | operations | S-25 MO, Common pitfalls | C-28 |
| R-1877 | Alerts should have multiple pathways to on-call engineers. | operations engineers | operations | S-25 MO, Common pitfalls | C-28 |
| R-1878 | Alerts that are not actionable should be deleted. | operations engineers | operations | S-25 MO, Common pitfalls | C-28 |
| R-1879 | Alert silencing should be tracked very carefully. | operations engineers | operations | S-25 MO, Common pitfalls | C-28 |
| R-1880 | The deployment automation process must be created by developers and IT operations working together. | operations engineers | operations | S-25 DA, Requirements | C-34 |
| R-1881 | Packages should be deployable to any environment, including production. | operations engineers | operations | S-25 DA, Requirements | C-24 |
| R-1882 | Deployment steps should be idempotent and order independent where possible. | operations engineers | operations | S-25 DA, Requirements | C-24 |
| R-1883 | Services should keep operating in a degraded state when dependencies are unavailable. | operations engineers | operations | S-25 DA, Requirements | C-30 |
| R-1884 | You need to re-architect for deployability when automating a complex process. | software engineers | quality | S-25 DA, Requirements | C-47 |
| R-1885 | Services should be independently deployable, with no orchestration required. | operations engineers | operations | S-25 DA, Requirements | C-24 |
| R-1886 | Deployment processes that require manual console interaction should be targets for improvement. | operations engineers | operations | S-25 DA, Requirements | C-24 |
| R-1887 | Anyone with the necessary credentials should be able to deploy on demand without waiting for someone else. | operations engineers | operations | S-25 DA, Groups | C-24 |
| R-1888 | Deployment automation should be as simple as possible. | operations engineers | operations | S-25 DA, Groups | C-24 |
| R-1889 | Leadership should be fully invested in a CloudOps transformation with a suitable cloud operating model that incentivizes efficient teams and business outcomes. | managers | quality | S-26 Design principles, organize teams | C-48 |
| R-1890 | Establish key performance indicators and use observability telemetry to make informed decisions. | operations engineers | operations | S-26 Design principles, implement observability | C-28 |
| R-1891 | Take prompt action when business outcomes are at risk. | operations engineers | operations | S-26 Design principles, implement observability | C-29 |
| R-1892 | Proactively improve performance, reliability and cost based on actionable observability data. | operations engineers | operations | S-26 Design principles, implement observability | C-28 |
| R-1893 | Design workloads to be scalable and loosely coupled so that components can be updated regularly. | software engineers | quality | S-26 Design principles, small reversible changes | C-47 |
| R-1894 | Gamify operations to share best practices and educate teams. | software engineers | quality | S-26 Design principles, refine procedures | C-49 |
| R-1895 | Hold regular reviews and validate that all procedures are effective and that teams are familiar with them. | software engineers | operations | S-26 Design principles, refine procedures | C-30 |
| R-1896 | Update procedures where gaps are identified. | managers | quality | S-26 Design principles, refine procedures | C-52 |
| R-1897 | Communicate procedural updates to all stakeholders and teams. | software engineers | quality | S-26 Design principles, refine procedures | C-48 |
| R-1898 | Drive failure scenarios to understand the workload risk profile and its impact on business outcomes. | operations engineers | operations | S-26 Design principles, anticipate failure | C-30 |
| R-1899 | Test the effectiveness of procedures and team response against simulated failures. | operations engineers | operations | S-26 Design principles, anticipate failure | C-30 |
| R-1900 | Make informed decisions to manage open risks identified by testing. | managers | quality | S-26 Design principles, anticipate failure | C-48 |
| R-1901 | Drive improvement through lessons learned from all operational events and failures. | operations engineers | operations | S-26 Design principles, learn from events | C-29 |
| R-1902 | Share what is learned across teams and through the entire organization. | managers | quality | S-26 Design principles, learn from events | C-52 |
| R-1903 | Reduce operational burden by using AWS managed services where possible. | operations engineers | operations | S-26 Design principles, use managed services | 5 |
| R-1904 | Build operational procedures around interactions with those managed services. | operations engineers | operations | S-26 Design principles, use managed services | C-30 |
| R-1905 | Teams must have a shared understanding of the entire workload, their role in it, and shared business goals. | software engineers | operations | S-26 Organization, first section | C-34 |
| R-1906 | Evaluate internal and external customer needs with key stakeholders to decide where to focus efforts. | software engineers | quality | S-26 Organization, first section | C-46 |
| R-1907 | Verify awareness of governance guidelines and external obligations such as regulatory compliance and industry standards. | security engineers | security | S-26 Organization, first section | C-19 |
| R-1908 | Validate that mechanisms exist to identify changes to internal governance and external compliance requirements. | managers | quality | S-26 Organization, first section | C-48 |
| R-1909 | If no requirements are identified, validate that due diligence was applied to that finding. | managers | quality | S-26 Organization, first section | C-48 |
| R-1910 | Review priorities regularly so that they can be updated as needs change. | managers | quality | S-26 Organization, first section | C-48 |
| R-1911 | Evaluate threats to the business, including business risk and information security threats, and keep them in a risk registry. | managers | quality | S-26 Organization, second section | C-48 |
| R-1912 | Evaluate the impact of risks and of trade-offs between competing interests or approaches. | managers | quality | S-26 Organization, second section | C-48 |
| R-1913 | Manage benefits and risks to make informed decisions about where to focus efforts. | managers | quality | S-26 Organization, second section | C-48 |
| R-1914 | Teams must understand their part in achieving business outcomes, the roles of other teams, and have shared goals. | software engineers | operations | S-26 Organization, third section | C-34 |
| R-1915 | Verify that each application, workload, platform and infrastructure component has an identified owner. | managers | operations | S-26 Organization, ownership section | C-34 |
| R-1916 | Verify that each process and procedure has an owner responsible for its definition and for its performance. | managers | operations | S-26 Organization, ownership section | C-34 |
| R-1917 | Clearly define the responsibilities of team members and have mechanisms to identify responsibility and ownership. | software engineers | security | S-26 Organization, ownership section | C-19 |
| R-1918 | Have mechanisms to request additions, changes and exceptions so that innovation is not constrained. | operations engineers | operations | S-26 Organization, ownership section | C-31 |
| R-1919 | Define agreements between teams that describe how they support each other and the business outcomes. | software engineers | operations | S-26 Organization, ownership section | C-34 |
| R-1920 | Provide support for team members so that they can take action and support business outcomes. | software engineers | quality | S-26 Organization, support section | C-49 |
| R-1921 | Engaged senior leadership should set expectations and measure success. | managers | quality | S-26 Organization, support section | C-48 |
| R-1922 | Senior leadership should be the sponsor, advocate and driver for adoption of best practices and for the evolution of the organization. | managers | quality | S-26 Organization, support section | C-48 |
| R-1923 | Let team members take action when outcomes are at risk, and encourage them to escalate when they believe there is a risk. | software engineers | operations | S-26 Organization, support section | C-29 |
| R-1924 | Provide timely, clear and actionable communication of known risks and planned events. | managers | quality | S-26 Organization, support section | C-48 |
| R-1925 | Encourage experimentation to accelerate learning. | managers | quality | S-26 Organization, learning section | C-52 |
| R-1926 | Provide dedicated structured time for learning. | software engineers | quality | S-26 Organization, learning section | C-49 |
| R-1927 | Verify that team members have the tools and people they need to be successful and to scale. | software engineers | quality | S-26 Organization, learning section | C-49 |
| R-1928 | Leverage cross-organizational diversity to seek multiple perspectives. | software engineers | quality | S-26 Organization, learning section | C-49 |
| R-1929 | Grow inclusion, diversity and accessibility within teams. | software engineers | quality | S-26 Organization, learning section | C-49 |
| R-1930 | If external regulatory or compliance requirements apply, you should use the resources provided by AWS Cloud Compliance to educate teams. | operations engineers | operations | S-26 Organization, compliance section | 5 |
| R-1931 | Use tools or services that centrally govern environments across accounts, such as AWS Organizations. | operations engineers | operations | S-26 Organization, governance section | 5 |
| R-1932 | Take a balanced approach over the long term to build needed capabilities and manage risk. | managers | quality | S-26 Organization, intro to OPS 1 to 3 | C-48 |
| R-1933 | Recognize that an undesired result is a successful experiment that shows a path that will not lead to success. | managers | quality | S-26 Organization, intro to OPS 1 to 3 | C-52 |
| R-1934 | Design the workload to provide information on its internal state, such as metrics, logs, events and traces, across all components. | operations engineers | operations | S-26 Prepare, first section | C-28 |
| R-1935 | Revisit and refine the observability strategy as workloads evolve, which is essential. | operations engineers | operations | S-26 Prepare, first section | C-28 |
| R-1936 | Adopt approaches that improve the flow of changes into production and that achieve refactoring, fast quality feedback and bug fixing. | operations engineers | operations | S-26 Prepare, second section | C-25 |
| R-1937 | Adopt approaches that give fast quality feedback and rapid recovery from changes with undesired outcomes. | operations engineers | operations | S-26 Prepare, third section | C-25 |
| R-1938 | Plan for unsuccessful changes so that you can respond faster if necessary. | operations engineers | operations | S-26 Prepare, third section | C-25 |
| R-1939 | Test and validate the changes you make. | software engineers | quality | S-26 Prepare, third section | C-38 |
| R-1940 | Be aware of planned activities in your environments so that you can manage the risk of change to them. | operations engineers | operations | S-26 Prepare, third section | C-31 |
| R-1941 | Emphasize frequent, small, reversible changes. | operations engineers | operations | S-26 Prepare, third section | C-25 |
| R-1942 | Evaluate the operational readiness of the workload, processes, procedures and personnel. | operations engineers | operations | S-26 Prepare, fourth section | C-30 |
| R-1943 | Use a consistent process, with manual or automated checklists, to decide when the workload or a change is ready to go live. | operations engineers | operations | S-26 Prepare, fourth section | C-30 |
| R-1944 | Have runbooks that document routine activities and playbooks that guide issue resolution. | operations engineers | operations | S-26 Prepare, fourth section | C-30 |
| R-1945 | Understand the benefits and risks to make informed decisions about permitting changes into production. | operations engineers | operations | S-26 Prepare, fourth section | C-31 |
| R-1946 | Invest in implementing operations activities as code to maximize productivity, minimize error rates and achieve automated responses. | operations engineers | operations | S-26 Prepare, OPS 7 section | C-26 |
| R-1947 | Use pre-mortems to anticipate failure and create procedures where appropriate. | operations engineers | operations | S-26 Prepare, OPS 7 section | C-30 |
| R-1948 | Apply metadata with resource tags and resource groups under a consistent tagging strategy. | operations engineers | operations | S-26 Prepare, OPS 7 section | 5 |
| R-1949 | Tag resources for organization, cost accounting, access control and targeting of automated operations. | operations engineers | operations | S-26 Prepare, OPS 7 section | 5 |
| R-1950 | Plan what you will do with live systems that no longer comply when the checklists change. | managers | quality | S-26 Prepare, OPS 7 section | C-48 |
| R-1951 | Define clear baselines, set appropriate alert thresholds and actively monitor for deviations. | operations engineers | operations | S-26 Operate, first section | C-28 |
| R-1952 | Define expected outcomes, how success will be measured, and the metrics used to measure it. | operations engineers | operations | S-26 Operate, second section | C-27 |
| R-1953 | Establish metric baselines for improvement, investigation and intervention. | operations engineers | operations | S-26 Operate, second section | C-28 |
| R-1954 | Collect and analyze metrics, and validate the understanding of operations success as it changes over time. | operations engineers | operations | S-26 Operate, second section | C-28 |
| R-1955 | Use metrics to decide whether customer and business needs are met, and identify areas for improvement. | operations engineers | operations | S-26 Operate, second section | C-28 |
| R-1956 | Use established runbooks for well-understood events and playbooks for investigation and resolution. | operations engineers | operations | S-26 Operate, third section | C-29 |
| R-1957 | Prioritize responses to events by business and customer impact. | operations engineers | operations | S-26 Operate, third section | C-29 |
| R-1958 | Verify that an alert raised for an event has an associated process with a specifically identified owner. | managers | operations | S-26 Operate, third section | C-28 |
| R-1959 | Define in advance the personnel needed to resolve an event, and include escalation processes. | operations engineers | operations | S-26 Operate, third section | C-29 |
| R-1960 | Identify and engage individuals with the authority to decide courses of action that have business impact. | operations engineers | operations | S-26 Operate, third section | C-29 |
| R-1961 | Communicate operational status through dashboards and notifications tailored to the target audience. | operations engineers | operations | S-26 Operate, fourth section | C-28 |
| R-1962 | Align all collected metrics to a business need and the outcomes they support. | operations engineers | operations | S-26 Operate, closing paragraph | C-28 |
| R-1963 | Develop scripted responses to well-understood events and automate their performance. | operations engineers | operations | S-26 Operate, closing paragraph | C-29 |
| R-1964 | Prepare and validate procedures for responding to events to minimize their disruption to the workload. | operations engineers | operations | S-26 Operate, OPS 10 section | C-29 |
| R-1965 | Define, capture and analyze operations metrics to gain visibility of operations events. | operations engineers | operations | S-26 Operate, OPS 9 section | C-28 |
| R-1966 | Dedicate work cycles to nearly continuous incremental improvements. | managers | quality | S-26 Evolve, first section | C-52 |
| R-1967 | Perform post-incident analysis of all customer-impacting events. | operations engineers | operations | S-26 Evolve, first section | C-29 |
| R-1968 | Identify contributing factors and preventative actions to limit or prevent recurrence. | operations engineers | operations | S-26 Evolve, first section | C-29 |
| R-1969 | Communicate contributing factors with affected communities as appropriate. | operations engineers | operations | S-26 Evolve, first section | C-29 |
| R-1970 | Regularly evaluate and prioritize improvement opportunities for the workload and for operations procedures. | managers | quality | S-26 Evolve, first section | C-52 |
| R-1971 | Include feedback loops within procedures to identify improvements and capture learnings. | managers | quality | S-26 Evolve, second section | C-52 |
| R-1972 | Share lessons learned across teams. | software engineers | quality | S-26 Evolve, third section | C-52 |
| R-1973 | Analyze trends in lessons learned and perform cross-team retrospective analysis of operations metrics. | managers | quality | S-26 Evolve, third section | C-52 |
| R-1974 | Implement changes intended to bring improvement, and evaluate the results. | managers | quality | S-26 Evolve, third section | C-52 |
| R-1975 | Dedicate time and resources for nearly continuous incremental improvement. | managers | quality | S-26 Evolve, OPS 11 section | C-52 |
| R-1976 | Provide safe environments and time to experiment, develop and test improvements. | managers | quality | S-26 Evolve, closing paragraph | C-52 |
| R-1977 | Encourage learning from failures. | operations engineers | operations | S-26 Evolve, closing paragraph | C-29 |
| R-1978 | A reader who finds a bad record should fix it at the source. | consumers | quality | S-27 FAQ, Data section, question on wrong data | C-43 |
| R-1979 | The source asks the reader to file a data quality issue if the fix at the source does not solve the problem. | consumers | quality | S-27 FAQ, Data section, question on wrong data | C-43 |
| R-1980 | A reader should raise a missing or bad record with the home database that is responsible for the record. | consumers | quality | S-27 FAQ, Data section, question on missing records (exact question not confirmed by the tool output) | C-43 |
| R-1981 | The source asks the database maintainer to publish the database in the OSV format. | project maintainers | security | S-27 FAQ, Usage section, question on database maintainers | 5 |
| R-1982 | The source asks the project that publishes advisories to publish them in the OSV format so that they get imported. | project maintainers | security | S-27 FAQ, Background section, question on who OSV is for | 5 |
| R-1983 | The source asks the open source user to use the API, the scanner or a third-party integration to find known vulnerabilities. | consumers | security | S-27 FAQ, Usage section, question on open source users | C-11 |
| R-1984 | The source asks the contributor to follow the steps on the New Data Source page. | project maintainers | security | S-27 Data sources page, Contributing Data section | 5 |
| R-1985 | Organizations must embrace proactive dependency management, choose high-quality components and avoid malware risks | managers | security | S-28 Directives section | C-20 |
| R-1986 | Organizations must adapt their consumption practices to the rising malware threat | managers | security | S-28 Directives section | C-20 |
| R-1987 | Organizations must prioritize an advanced SCA tool that selects well-maintained components and addresses risk early | managers | security | S-28 Directives section | C-11 |
| R-1988 | Organizations should integrate SCA into CI/CD pipelines and throughout development | managers | security | S-28 Directives section | C-11 |
| R-1989 | Organizations should take proactive steps to update dependencies, since nearly all risk is preventable | managers | quality | S-28 Directives section | C-51 |
| R-1990 | Enterprises must aim to reduce wasted remediation effort | managers | security | S-28 Directives section | C-11 |
| R-1991 | Enterprises need SCA tools that provide high-quality component intelligence and integrate into development workflows | managers | security | S-28 Directives section | C-11 |
| R-1992 | Software manufacturers, consumers and regulators must adopt robust security practices | regulators and auditors | security | S-28 Directives section | C-19 |
| R-1993 | Organizations must evolve their security practices to avoid becoming victims of their own success | managers | quality | S-28 Directives section | C-48 |
| R-1994 | Projects should put the listed practices into place. | project maintainers | security | S-30 Implementation (intro) | C-22 |
| R-1995 | The release process should be clearly and fully documented in the developer documentation, including every step and the permissions needed. | project maintainers | operations | S-30 Implementation, Document the release process | C-32 |
| R-1996 | A dedicated page in the developer section of the documentation website is recommended for the release process. | project maintainers | operations | S-30 Implementation, Document the release process | C-32 |
| R-1997 | Publishing workflows should have run triggers that require intentional actions by the release team. | software engineers | operations | S-30 Implementation, Harden workflow environment permissions | C-31 |
| R-1998 | Release managers should strongly use signed commits. | operations engineers | security | S-30 Implementation, Harden workflow environment permissions | C-01 |
| R-1999 | The branch from which the release is made should be protected. | project maintainers | security | S-30 Implementation, Harden workflow environment permissions | C-03 |
| R-2000 | Default runner permissions should be restricted to the minimum possible, which is read access. | project maintainers | security | S-30 Implementation, Restrict CI runner permissions | C-02 |
| R-2001 | Permissions above read access should be granted at the job level. | project maintainers | security | S-30 Implementation, Restrict CI runner permissions | C-02 |
| R-2002 | The source suggests, as a reasonable default, allowing the actions of the organisation, GitHub-created actions and specified outside actions. | project maintainers | security | S-30 Implementation, Restrict permitted actions | C-10 |
| R-2003 | Publishing jobs should use a GitHub Actions environment, with review by at least one other release team maintainer. | software engineers | security | S-30 Implementation, Use GitHub Actions environments | C-08 |
| R-2004 | GitHub actions must be pinned using the full commit SHA corresponding to the release version being used. | project maintainers | security | S-30 Implementation, Pin actions to full commit SHAs | C-10 |
| R-2005 | Action updates should be handled as part of a reviewed process. | project maintainers | quality | S-30 Implementation, Pin actions to full commit SHAs | C-51 |
| R-2006 | The id-token: write permission is mandatory for trusted publishing. | project maintainers | security | S-30 Implementation, Adopt OIDC via PyPI Trusted Publishers | 5 |
| R-2007 | Enabling print-hash in the publish step is recommended. | project maintainers | security | S-30 Implementation, Adopt OIDC via PyPI Trusted Publishers | 5 |
| R-2008 | A user must first install the Sigstore client before use. | security engineers | security | S-34 How to use Sigstore | 5 |
| R-2009 | Researchers could examine more deeply how to adopt each standard test automation best practice. | software engineers | quality | S-35 section 5.2 Implications for researchers | C-52 |
| R-2010 | Researchers can build on these results to develop test automation maturity models. | software engineers | security | S-35 section 5.2 Implications for researchers | C-22 |
| R-2011 | Future efforts to give theoretical explanations for control-variable differences would be meaningful. | software engineers | quality | S-35 section 5.2 Implications for researchers | C-52 |
| R-2012 | Future research could also include test automation maturity as a determinant of CI success. | software engineers | security | S-35 section 5.2 Implications for researchers | C-22 |
| R-2013 | Researchers can consult this triangulated method for other test automation topics. | software engineers | quality | S-35 section 5.2 Implications for researchers | C-52 |
| R-2014 | Practitioners could assess and improve test automation practices against standard best practices. | software engineers | quality | S-35 section 5.3 Implications for practitioners | C-52 |
| R-2015 | Practitioners can also collect similar metric data to study maturity, quality, effort and release cycles. | software engineers | quality | S-35 section 5.3 Implications for practitioners | C-52 |
| R-2016 | Practitioners can weigh benefits in quality and short release cycles against test automation effort. | software engineers | quality | S-35 section 5.3 Implications for practitioners | C-48 |
| R-2017 | The recommendation to practitioners is to utilise standard test automation best practices to improve maturity. | software engineers | security | S-35 section 6 Conclusion | C-22 |
| R-2018 | Researchers must select projects in the same programming language. | software engineers | quality | S-35 section 5.4 Limitations | C-52 |
| R-2019 | When new control variables are identified, the replication of this study is required. | managers | quality | S-35 section 5.4 Limitations | C-52 |
| R-2020 | Future research is encouraged to extend the findings with more datasets, languages, CI servers and build tools. | software engineers | quality | S-35 section 5.4 Limitations | C-52 |
| R-2021 | Practitioners and tool builders should develop strategies for technical CI challenges, such as build environment setup. | software engineers | quality | S-36 Section 7.2 | C-37 |
| R-2022 | Practitioners should follow Duvall et al. guidance and implement a set of CI sub-practices daily, because partial adoption is insufficient. | software engineers | quality | S-36 Recommendations, For Practitioners | C-37 |
| R-2023 | Keep builds fast; the XP methodology recommends a limit of 10 minutes. | software engineers | quality | S-36 Recommendations, For Practitioners | C-37 |
| R-2024 | Treat fixing broken builds immediately as a core practice, so that the build stays green. | software engineers | quality | S-36 Recommendations, For Practitioners | C-37 |
| R-2025 | Practitioners and tool builders should develop strategies and tools to address CI technical challenges. | software engineers | quality | S-36 Section 7.2; Section 4.2.2 | C-37 |
| R-2026 | Studies disagree on whether CI speeds up pull request merging: two found shorter merge times, two found longer. | project maintainers | quality | S-36 Section 5.2.1 | C-52 |
| R-2027 | Researchers should clearly define and check how CI use is determined. | software engineers | quality | S-36 Recommendations, For Researchers | C-52 |
| R-2028 | Researchers should be more restrictive when they use build logs from CI servers as evidence of CI use. | software engineers | quality | S-36 Recommendations, For Researchers | C-52 |
| R-2029 | Researchers should identify which CI variant a project applies, as Ståhl and Bosch recommend. | software engineers | quality | S-36 Recommendations, For Researchers | C-52 |
| R-2030 | Researchers should use stronger designs, including statistical tests and control or comparison groups. | software engineers | quality | S-36 Recommendations, For Researchers | C-52 |
| R-2031 | Researchers should investigate the adverse effects of CI and its impact on automation and productivity more thoroughly. | software engineers | quality | S-36 Recommendations, For Researchers | C-52 |
| R-2032 | Researchers should make data and scripts available to support reproduction and replication. | software engineers | quality | S-36 Recommendations, For Researchers | C-52 |
| R-2033 | More studies are needed to understand the context and extent of negative effects. | managers | quality | S-36 Recommendations, For the Software Engineering Community | C-52 |
| R-2034 | The software engineering community should improve the reliability of empirical research on the development activities theme. | project maintainers | quality | S-36 Recommendations, For the Software Engineering Community | C-52 |
| R-2035 | Researchers should carefully define and measure productivity and confidence. | software engineers | quality | S-36 Section 5.2.2 | C-52 |
| R-2036 | Researchers should supply developers with objective criteria for judging a reliable CI environment. | software engineers | quality | S-36 Section 5.2.2 | C-52 |
| R-2037 | Classify which CI practices a project uses, and at what level, rather than only stating that CI is used. | managers | quality | S-36 Section 5.1 | C-52 |
| R-2038 | Verify CI adherence beyond self-declaration, for example by checking which practices subjects actually use. | managers | quality | S-36 Section 5.1 | C-52 |
| R-2039 | The community should study how CI implementations differ across domains and how those differences affect outcomes. | project maintainers | quality | S-36 Section 4.3.1 | C-52 |
| R-2040 | The community should strengthen metric definitions and concepts, and use comparison or control strategies. | project maintainers | quality | S-36 Section 4.3.3 | C-52 |
| R-2041 | Case study and action research authors should be more transparent about data and explain the rationale behind their conclusions. | software engineers | quality | S-36 Section 4.3.3 | C-52 |
| R-2042 | More studies are needed on CI and pull request lifetime that account for confounders such as project age and the number of open pull requests. | managers | quality | S-36 Section 5.2.1 | C-52 |
| R-2043 | Researchers could develop a CI maturity score or a consensus set of minimal practices. | software engineers | security | S-36 Section 7.2 | C-22 |
| R-2044 | Further studies should examine the trade-offs between adopting CI and overcoming its challenges. | managers | quality | S-36 Section 7.2 | C-52 |

## Proposed boundaries

| Boundary | Requirements that it would take | Stakeholders that it would leave with no requirement | Reason |
|---|---|---|---|
| requirements engineering | R-0003, R-0005 to R-0016, R-0018, R-0021 to R-0027, R-0252, R-0254, R-0255, R-0294, R-0329, R-0390, R-0424, R-1087, R-1906 | none | The body of knowledge has a knowledge area of its own for it (S-01 pages 43-66). The requirements of the item for written, traceable requirements come from that area. |
| architecture and design | R-0040 to R-0054, R-0056, R-0065 to R-0067, R-0069 to R-0071, R-0152, R-0190, R-0291 to R-0293, R-0350, R-0355, R-0391 to R-0394, R-0396, R-0397, R-0411, R-0414, R-0422, R-0423, R-0425, R-0449, R-0465, R-0975, R-1080 to R-1082, R-1085, R-1185, R-1186, R-1313, R-1532, R-1662, R-1663, R-1691, R-1695, R-1705, R-1747, R-1752, R-1753, R-1760, R-1765, R-1816, R-1860, R-1884, R-1893 | none | The body of knowledge has two knowledge areas for it (S-01 pages 67-98). |
| project management and process | R-0034 to R-0038, R-0119, R-0166, R-0167, R-0258, R-0262, R-0263, R-0270, R-0277 to R-0287, R-0290, R-0296, R-0303, R-0304, R-0308 to R-0312, R-0343, R-0382, R-0384, R-0385, R-0387 to R-0389, R-0436 to R-0439, R-0450, R-0462, R-0472, R-0473, R-0475, R-0689, R-0692, R-0696, R-0698, R-0699, R-0701, R-0705, R-0772, R-0774, R-0780, R-0782, R-0951, R-0978, R-1312, R-1571 to R-1573, R-1660, R-1704, R-1744, R-1794, R-1806, R-1815, R-1830, R-1847, R-1889, R-1897, R-1900, R-1908 to R-1913, R-1921, R-1922, R-1924, R-1932, R-1950, R-1993, R-2016 | none | The body of knowledge has four knowledge areas for it (S-01 pages 202-245 and 288-311). |
| professional practice | R-0001, R-0002, R-0004, R-0063, R-0120 to R-0123, R-0151, R-0191, R-0299, R-0300, R-0305, R-0306, R-0345, R-0346, R-0366 to R-0372, R-0380, R-0381, R-0395, R-0398, R-0399, R-0405, R-0408 to R-0410, R-0417, R-0420, R-0432 to R-0435, R-0460, R-0461, R-0463, R-0464, R-1280, R-1281, R-1667, R-1676, R-1894, R-1920, R-1926 to R-1929 | none | The body of knowledge has a knowledge area for it and three foundation areas (S-01 pages 274-287 and 312-386). |
| project governance | R-1161 to R-1165, R-1167 to R-1171, R-1211, R-1217, R-1218, R-1239 to R-1243, R-1247, R-1262, R-1305 to R-1311, R-1360 to R-1363, R-1365, R-1389, R-1664 to R-1666, R-1680, R-1728 | none | The criteria of the badge and of the baseline put these under governance and basics, not under the build or the release (S-11 passing and silver items; S-09 versions page). |
| software maintenance | R-0107, R-0175 to R-0189, R-0194 to R-0196, R-0198, R-0199, R-0201 to R-0205, R-0211, R-0212, R-0216, R-0251, R-0340, R-1117 to R-1119, R-1157, R-1158, R-1249, R-1321, R-1337, R-1791, R-1802, R-1804, R-1814, R-1825 | none | The body of knowledge has a knowledge area for it (S-01 pages 167-184). |

## Reading

The program `index.py unread --write` writes this table. Do not change it by hand.

| Source | Document | Pages | Given to readers | Not read |
|---|---|---|---|---|
| S-01 | swebok | 411 | 1-25, 26-42, 43-66, 67-82, 83-98, 99-116, 117-141, 142-166, 167-184, 185-201, 202-220, 221-245, 246-263, 264-287, 288-311, 312-335, 336-344, 345-366, 367-386, 387-411 | none |
| S-03 | S-03 | 36 | 1-25, 26-36 | none |
| S-04 | S-04 | 41 | 1-23, 24-41 | none |
| S-16 | S-16 | 4 | 1-4 | none |
