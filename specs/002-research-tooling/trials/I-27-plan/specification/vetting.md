# Vetting record: DevSecOps

## Sources

One row for each source of the class `independent`. The cell "Answers" holds the two answers of the reader, each with its evidence. Programs fill the cells Kind, Gates, Signals, Score and Date. Only the owner fills the cell "Confirmed by".

| Source | Kind | Gates | Signals | Score | Date | Answers | Confirmed by |
|---|---|---|---|---|---|---|---|
| S-13 | page | pass | reachable yes; date 2026-10-13; age 0 d; author yes; links out 9 | 9 of 10 | 2026-10-13 | record: yes (https://dora.dev/research/2014/2014-state-of-devops-report.pdf); fast-lane references: 1 (S-15) |  |
| S-20 | page | pass | reachable yes; date 2026-10-13; age 0 d; author yes; links out 5 | 9 of 10 | 2026-10-13 | record: yes (https://openssf.org/projects/osv-schema/); fast-lane references: 1 (S-10) |  |
| S-21 | page | pass | reachable yes; date 2026-10-08; age 5 d; author yes; links out 11 | 8 of 10 | 2026-10-13 | record: yes (https://www.sonatype.com/en/press-releases/sonatypes-10th-annual-state-of-the-software-supply-chain-report); fast-lane references: 0 |  |
| S-25 | page | pass | reachable yes; date 2026-08-04; age 70 d; author yes; links out 1 | 7 of 10 | 2026-10-13 | record: yes (https://curl.se/docs/history.html); fast-lane references: 0 |  |


## Searches

One line for each query of the research, with the view that it serves. A line with the word `catalogues:` is a query of the catalogues of the work folder.

- security: `secure software development practices integrated into delivery pipeline standard guidance`
- security: `regulation software products security requirements vulnerability handling manufacturers obligations`
- security: `build integrity levels provenance software artifacts framework specification`
- operations: `software delivery performance metrics multi-year survey deployment frequency change failure rate report`
- operations: `operational readiness reliability practices production service release engineering monitoring incident response book`
- quality: `software product quality model characteristics international standard maintainability reliability`
- operations: `regulation digital operational resilience ICT change management testing requirements financial entities official text`
- security: `public authority recommendation defending continuous integration continuous delivery environments`
- security: `maturity model software security assurance practices levels open framework`
- security: `automated checks security health open source project score tool`
- security: `public vulnerability database open source packages who operates funding`
- quality: `audit framework IT governance controls change management software development separation of duties`
- operations: `reusable hardened pipeline components continuous integration maintained catalog security scanning steps`
- quality: `software quality assurance processes standard requirements reviews audits verification validation life cycle`
- quality: `law liability defective software product quality obligations producers directive official text`
- security: `annual report state of software supply chain open source vulnerabilities downloads multi-year data`
- security: `how a widely used open source project signs releases and reviews changes release process documentation`
- quality: `continuous delivery best practices vendor-neutral foundation guide version control continuous integration testing deployment`
- quality: `code review testing continuous integration engineering practices large company book free online`
- operations: `service management standard operations requirements release deployment management incident management change enablement`
- security: `security baseline controls open source projects maturity levels criteria foundation`
- operations: `tool measure four key delivery metrics from pipeline events open source`
- security, catalogues: `devsecops`
- security, catalogues: `supply chain security`
- security, catalogues: `vulnerability scan`
- security, catalogues: `provenance`
- security, catalogues: `attestation`
- security, catalogues: `signing`
- security, catalogues: `sbom`
- security, catalogues: `policy`
- security, catalogues: `secret`
- security, catalogues: `scorecard`
- security, catalogues: `vulnerability database`
- security, catalogues: `fuzzing`
- operations, catalogues: `pipeline`
- operations, catalogues: `continuous delivery`
- operations, catalogues: `observability`
- operations, catalogues: `incident`
- operations, catalogues: `deployment`
- operations, catalogues: `monitoring`
- operations, catalogues: `release`
- quality, catalogues: `static analysis`
- quality, catalogues: `code quality`
- quality, catalogues: `test`

## Requirements

| Id | Requirement | Stakeholder | View | Source | Goes to |
|---|---|---|---|---|---|
| R-0001 | A software project must implement requirements imposed by cross-cutting disciplines such as dependability and safety. | software engineers | quality | S-01 page 39 | C-33 |
| R-0002 | Software engineers should, of course, be knowledgeable about the eleven related disciplines that the Guide lists. | software engineers | quality | S-01 page 40 | C-39 |
| R-0003 | Competent, capable software engineers should be equipped with the generally accepted knowledge for potential application. | software engineers | quality | S-01 page 41 | C-39 |
| R-0004 | Appropriate selection of generally accepted knowledge should be included in the study material for certification and licensing examinations. | software engineers | quality | S-01 page 41 | C-39 |
| R-0005 | Requirements should be viewed as an expression of needs and constraints and as the activities to develop and maintain them. | software engineers | quality | S-01 page 43 | C-38 |
| R-0006 | The whats and hows of requirements work should be determined by the nature of the software constructed, not by the life cycle used. | software engineers | quality | S-01 page 44 | C-38 |
| R-0007 | Downstream maintainers should not be able to discern the life cycle used in earlier development from the form of the requirements alone. | software engineers | quality | S-01 page 53 | C-37 |
| R-0008 | The effect of the chosen life cycle should be limited to the completeness of the requirements at any point in the project. | software engineers | quality | S-01 page 53 | C-38 |
| R-0009 | Documented software requirements should be subject to the same configuration management practices as the other deliverables of the life cycle processes. | software engineers | operations | S-01 page 53 | C-45 |
| R-0010 | All potential requirements sources should be identified and evaluated. | software engineers | quality | S-01 page 48 | C-38 |
| R-0011 | Whenever a nonfunctional requirement is modified, the impact it may cause on others should be considered. | software engineers | quality | S-01 page 46 | C-33 |
| R-0012 | The software engineer must work hard to elicit the right information. | software engineers | quality | S-01 page 49 | C-38 |
| R-0013 | The overall collection of requirements should be complete, concise, internally consistent, externally consistent and feasible. | software engineers | quality | S-01 page 50 | C-38 |
| R-0014 | Each requirement should be unambiguous, testable (quantified), binding, atomic, true to stakeholder needs, in stakeholder vocabulary, and acceptable to all stakeholders. | software engineers | quality | S-01 page 50 | C-33 |
| R-0015 | The software engineer should pay particular attention to the positive and negative relationships between quality of service constraints. | software engineers | quality | S-01 page 51 | C-33 |
| R-0016 | Acceptance test cases must pass to show that a unit of functionality has been correctly implemented; they are agreed before production design or construction work. | software engineers | quality | S-01 pages 54–55 | C-31 |
| R-0017 | At least one of the acceptance test cases must fail on the existing software. | quality assurance | quality | S-01 page 55 | C-31 |
| R-0018 | Requirements scrubbing should occur just before the validation review in waterfall and other plan-based life cycles. | software engineers | quality | S-01 page 58 | C-38 |
| R-0019 | Projects using waterfall or other plan-based life cycles should have an explicit requirements change control process. | software engineers | operations | S-01 page 59 | C-45 |
| R-0020 | The change control process should include a means to request changes, an optional impact analysis, a responsible person or group to decide, a means to notify stakeholders, and a means to track accepted changes to closure. | software engineers | operations | S-01 page 59 | C-45 |
| R-0021 | All stakeholders must understand and agree that accepting a change means accepting its impact on schedule, resources and scope. | management | quality | S-01 page 59 | C-42 |
| R-0022 | The change in scope should ideally be objectively quantifiable in functional size units. | management | quality | S-01 page 59 | C-42 |
| R-0023 | Scope matching should be quantitative instead of qualitative where possible. | management | quality | S-01 page 59 | C-42 |
| R-0024 | In waterfall and other plan-based life cycles, scope matching should occur just before the validation review. | management | quality | S-01 page 59 | C-42 |
| R-0025 | When requirements scope exceeds cost, schedule or staffing constraints, scope must be reduced, capacity must be increased, or a combination must be negotiated. | management | quality | S-01 page 59 | C-42 |
| R-0026 | Prioritization must weigh both the satisfaction and the dissatisfaction that stakeholders would feel. | management | quality | S-01 page 60 | C-38 |
| R-0027 | Defects raised against higher-priority requirements should probably be repaired before defects raised against lower-priority ones. | software engineers | quality | S-01 page 60 | C-35 |
| R-0028 | Priorities must be specified in a way that can be communicated to all stakeholders. | management | quality | S-01 page 60 | C-38 |
| R-0029 | The architecture should be documented to support its uses, such as shared understanding, analysis and reverse engineering. | software engineers | quality | S-01 page 70 | C-38 |
| R-0030 | Notations should be chosen on the basis of need, purpose and utility for the stakeholders who need the information. | software engineers | quality | S-01 page 70 | C-38 |
| R-0031 | An application architecture should conform to an enterprise architecture. | software engineers | quality | S-01 page 76 | C-38 |
| R-0032 | In a system of systems, the architecture of each constituent system should conform to the system-of-systems architecture. | software engineers | quality | S-01 page 76 | C-38 |
| R-0033 | In such cases, the relations between architectures need to be reflected as architecturally significant requirements on the software being architected. | software engineers | quality | S-01 page 76 | C-38 |
| R-0034 | The software design must provide a guide to implementors on building the system. | software engineers | quality | S-01 page 84 | C-38 |
| R-0035 | An SDD should be sufficient as a basis for verifying a design. | quality assurance | quality | S-01 page 86 | C-38 |
| R-0036 | Design should be complete with respect to the modes and states of the software. | software engineers | quality | S-01 page 86 | C-38 |
| R-0037 | A design should be sufficient for designers to demonstrate how requirements will be met and how subsequent work will satisfy those requirements. | software engineers | quality | S-01 page 86 | C-38 |
| R-0038 | Most design methods advocate that modules should be loosely or weakly coupled. | software engineers | quality | S-01 page 86 | C-38 |
| R-0039 | Most design methods advocate that modules should maximize their cohesion. | software engineers | quality | S-01 page 86 | C-38 |
| R-0040 | The existence of a suitable algorithm, for some systems, must be determined early in the life cycle. | software engineers | quality | S-01 page 87 | C-38 |
| R-0041 | Each design stage creates an obligation upon the next stage. | software engineers | quality | S-01 page 87 | C-38 |
| R-0042 | The detailed design specifications should be sufficient to allow programmers to code each module. | software engineers | quality | S-01 page 87 | C-38 |
| R-0043 | Projects should make conscious decisions about which design specifications are needed, based upon stakeholder audience, subject and intended usage. | software engineers | quality | S-01 page 90 | C-38 |
| R-0044 | Ideally, a program should have at least as many test cases as its cyclomatic complexity number. | quality assurance | quality | S-01 page 100 | C-31 |
| R-0045 | Software engineers should build flexibility and adaptability into software, so that changes can be made with less difficulty. | software engineers | quality | S-01 page 101 | C-38 |
| R-0046 | Software teams should embrace change by adopting agile development, practicing DevOps, and adopting continuous delivery and deployment practices. | software engineers | operations | S-01 page 101 | C-20 |
| R-0047 | Unnecessary dependencies should be avoided to improve build efficiency. | software engineers | security | S-01 page 103 | C-10 |
| R-0048 | License conflicts between dependencies and software products should be avoided to reduce legal risk. | software engineers | quality | S-01 page 103 | C-41 |
| R-0049 | Propagation of dependency defects or vulnerabilities into software products should be avoided to improve software quality. | software engineers | security | S-01 page 103 | C-10 |
| R-0050 | Any dependency in the supply chain network should be managed by developers or by tools, because it can introduce risk. | software engineers | security | S-01 page 103 | C-10 |
| R-0051 | Regulations and monitoring mechanisms should be developed to prevent developers from introducing untrusted external dependencies. | management | security | S-01 pages 103 to 104 | C-10 |
| R-0052 | Exception-handling policies should be designed carefully, following common principles. | software engineers | security | S-01 page 109 | C-13 |
| R-0053 | Programmers should know good practices and common vulnerabilities. | software engineers | quality | S-01 page 107 | C-39 |
| R-0054 | API design should make the API easy to learn and memorize, lead to readable code, be difficult to misuse, be easy to extend, be complete, and maintain backward compatibility. | software engineers | quality | S-01 page 108 | C-38 |
| R-0055 | An API should be straightforward and stable, to facilitate client application development and maintenance. | software engineers | quality | S-01 page 108 | C-38 |
| R-0056 | An API should always include statements about the effects or behaviors of the program. | software engineers | quality | S-01 page 108 | C-38 |
| R-0057 | Software engineers must be aware that different selection criteria might yield vastly different degrees of effectiveness. | quality assurance | quality | S-01 page 118 | C-31 |
| R-0058 | For each executed test case, it must be possible to decide whether the observed SUT outcomes match the expected ones. | quality assurance | quality | S-01 page 118 | C-31 |
| R-0059 | Faults that cause failures can and must be removed. | software engineers | quality | S-01 page 119 | C-35 |
| R-0060 | Testing needs to focus on specific mandatory prescriptions, such as requirements, laws and standards. | quality assurance | quality | S-01 page 120 | C-31 |
| R-0061 | Test cases should be generated and executed to provide evidence for evaluating or certifying adherence to the selected prescriptions. | quality assurance | quality | S-01 page 120 | C-41 |
| R-0062 | It is important to ensure that both typical and alternate workflows are also tested. | quality assurance | quality | S-01 page 128 | C-31 |
| R-0063 | Testing processes should allow the automation of different testing phases. | quality assurance | quality | S-01 page 134 | C-31 |
| R-0064 | Testing processes should rely on the controllability, traceability, replicability and risk or cost estimation of the performed activities. | quality assurance | quality | S-01 page 134 | C-31 |
| R-0065 | Test activities should be organized into a well-defined process that is integral to the life cycle. | quality assurance | quality | S-01 page 135 | C-34 |
| R-0066 | A test strategy should include at least the purposes, the objectives, the scope, and the environment and methods. | quality assurance | quality | S-01 page 135 | C-31 |
| R-0067 | Test documentation should be produced and continuously updated with the same quality as other software engineering documentation. | quality assurance | quality | S-01 page 135 | C-37 |
| R-0068 | Test documentation should be under the control of software configuration management. | quality assurance | operations | S-01 page 135 | C-45 |
| R-0069 | The resources spent on testing should be commensurate with the application's use and criticality. | quality assurance | quality | S-01 page 136 | C-34 |
| R-0070 | Suitable knowledge-based repositories should be configured and managed to test reusability. | quality assurance | quality | S-01 page 136 | C-31 |
| R-0071 | Test execution should embody a basic principle of scientific controlled experimentation. | quality assurance | quality | S-01 page 137 | C-31 |
| R-0072 | Testing should be performed following documented procedures using a clearly defined version of the SUT. | quality assurance | quality | S-01 page 137 | C-31 |
| R-0073 | The testing environment should be compatible with the other software engineering tools used. | quality assurance | quality | S-01 page 137 | C-31 |
| R-0074 | For the fault-based technique to be effective, many mutants must be automatically generated and executed systematically. | quality assurance | quality | S-01 page 131 | C-31 |
| R-0075 | The testing environment needs to represent the actual operational environment. | quality assurance | quality | S-01 page 131 | C-31 |
| R-0076 | The sequence of test case execution should reproduce the SUT usage by the target stakeholder. | quality assurance | quality | S-01 page 131 | C-31 |
| R-0077 | In shift-left-based development, different testing aspects should be considered. | quality assurance | quality | S-01 page 139 | C-31 |
| R-0078 | In the IoT domain, security, privacy, communications and user or component interaction should be considered in the quality assessment. | quality assurance | quality | S-01 page 141 | C-31 |
| R-0079 | In the legal domain, performance, accurate communication, integration, consistency and compliance testing should also be done. | quality assurance | quality | S-01 page 141 | C-31 |
| R-0080 | Healthcare domain testing should ensure quality in areas such as secure and reliable data exchange, stable performance, privacy and safety. | quality assurance | quality | S-01 page 141 | C-31 |
| R-0081 | Healthcare standards such as HL7, FHIR, DICOM, HIPAA and GDPR should also be considered. | quality assurance | quality | S-01 page 141 | C-31 |
| R-0082 | Embedded domain testing should assess functional and non-functional attributes of both software and hardware. | quality assurance | quality | S-01 page 141 | C-31 |
| R-0083 | In the mobile domain, the type of mobile applications and their interactions need to be tested. | quality assurance | quality | S-01 page 141 | C-31 |
| R-0084 | Avionics testing needs to include very general processes and approaches applicable at both the system and the process levels. | quality assurance | quality | S-01 page 141 | C-31 |
| R-0085 | Software engineering operations planning should comprise part of translating project requirements into services | operations engineers | operations | S-01 page 156 | C-29 |
| R-0086 | Operations planning should begin with the decision to develop a new product and should consider maintenance and operations requirements early | operations engineers | operations | S-01 page 156 | C-29 |
| R-0087 | A concept document should be developed, followed by an operations and maintenance plan | operations engineers | operations | S-01 page 156 | C-29 |
| R-0088 | The operations plan should be prepared during software development and should specify how users request modifications and report problems | operations engineers | operations | S-01 page 156 | C-29 |
| R-0089 | Products and services of suppliers must be well coordinated to ensure quality service | operations engineers | security | S-01 page 156 | C-19 |
| R-0090 | Operations engineers should document their operations steps and tools in any suitable form | operations engineers | quality | S-01 page 156 | C-37 |
| R-0091 | Software organizations should address staff recruitment, resource planning and training | management | quality | S-01 page 153 | C-39 |
| R-0092 | Operations engineers should be trained in relevant aspects of service management | operations engineers | quality | S-01 page 154 | C-39 |
| R-0093 | Operations engineers should develop teamwork and leadership skills | operations engineers | quality | S-01 page 154 | C-39 |
| R-0094 | A chronological training record should be maintained for each individual | management | quality | S-01 page 154 | C-39 |
| R-0095 | Operations engineers should replicate and verify problem reports by running appropriate tests | operations engineers | operations | S-01 page 155 | C-25 |
| R-0096 | Software testing must be automated as much as possible throughout the entire software process | software engineers | quality | S-01 page 155 | C-31 |
| R-0097 | Software must be thoroughly tested before it is released | quality assurance | quality | S-01 page 155 | C-31 |
| R-0098 | Engineers must ensure that the different environments are coherent and synchronized with production | operations engineers | operations | S-01 page 158 | C-22 |
| R-0099 | Service availability and continuity must be managed | operations engineers | operations | S-01 page 158 | C-27 |
| R-0100 | The capacity plan should be produced at a suitable frequency, at least annually | operations engineers | operations | S-01 page 158 | C-27 |
| R-0101 | The capacity plan should document costed options for meeting business requirements | operations engineers | operations | S-01 page 158 | C-27 |
| R-0102 | The reaction to variations in workload should be predictable | operations engineers | operations | S-01 page 158 | C-27 |
| R-0103 | Operations engineers should strive to enforce the listed information security controls | operations engineers | quality | S-01 page 159 | C-40 |
| R-0104 | Senior management should define the information security policy and communicate it | management | quality | S-01 page 159 | C-40 |
| R-0105 | Information security roles and responsibilities should be defined and allocated | management | quality | S-01 page 159 | C-40 |
| R-0106 | A representative of the management team should monitor and maintain the policy | management | quality | S-01 page 159 | C-40 |
| R-0107 | Staff with significant security roles should receive information security training | security team | quality | S-01 page 159 | C-39 |
| R-0108 | All staff should be made aware of the information security policy | management | quality | S-01 page 159 | C-39 |
| R-0109 | Expert help on risk assessment and control implementation should be available | security team | security | S-01 page 159 | C-12 |
| R-0110 | Changes should not compromise the effective operation of controls | operations engineers | operations | S-01 page 159 | C-26 |
| R-0111 | Information security incidents should be reported and a response should be initiated | security team | operations | S-01 page 159 | C-25 |
| R-0112 | Preparedness and regular tests of backup, disaster recovery and failover should be constantly rehearsed | operations engineers | operations | S-01 page 159 | C-27 |
| R-0113 | Software applications should include failure-handling logic, which must be planned during development | software engineers | operations | S-01 page 159 | C-27 |
| R-0114 | Software engineers should understand that failure is inevitable | software engineers | operations | S-01 page 159 | C-27 |
| R-0115 | Software engineers should be aware that operations processes can be adapted to small organizations | software engineers | operations | S-01 page 163 | C-29 |
| R-0116 | Testing must be automated throughout development and operations | software engineers | quality | S-01 page 164 | C-31 |
| R-0117 | A testing strategy covering unit, integration, system and acceptance tests must be defined and tools must be selected | quality assurance | quality | S-01 page 164 | C-31 |
| R-0118 | Software applications or services must be architected to enable small, independent deployments | software engineers | operations | S-01 page 161 | C-21 |
| R-0119 | Proper post-mortems must be conducted when an incident occurs | operations engineers | operations | S-01 page 161 | C-25 |
| R-0120 | Appropriate solutions must be implemented to prevent similar incidents | operations engineers | operations | S-01 page 161 | C-25 |
| R-0121 | Engineers should be informed about system quality and operational health with evidence | software engineers | operations | S-01 page 161 | C-23 |
| R-0122 | Operations engineers must manage a number of risks | operations engineers | quality | S-01 page 162 | C-42 |
| R-0123 | Product telemetry should be implemented with proper analytics | operations engineers | operations | S-01 page 162 | C-23 |
| R-0124 | Data collected at all layers of the product stack must be collected and analyzed | operations engineers | operations | S-01 page 162 | C-23 |
| R-0125 | Operations engineers should keep the risk tolerance agreed with product owners and software engineers | operations engineers | operations | S-01 page 162 | C-24 |
| R-0126 | The requirement that the operations process must be automated is stated with needs to, not must | operations engineers | operations | S-01 page 162 | C-20 |
| R-0127 | Testing should also focus on compatibility and interoperability of cloud resources | quality assurance | quality | S-01 page 143 | C-31 |
| R-0128 | Integration testing should be performed to check consistency with applications | quality assurance | quality | S-01 page 143 | C-31 |
| R-0129 | Specific strategies should be conceived to handle many transactions | quality assurance | quality | S-01 page 143 | C-31 |
| R-0130 | Qualitative and quantitative metrics should also be considered for blockchain testing | quality assurance | quality | S-01 page 143 | C-31 |
| R-0131 | Three main aspects should be considered in defining bugs and testing for AI, ML and DL | quality assurance | quality | S-01 page 142 | C-31 |
| R-0132 | The testing activity varies according to the environment, organization and requirements that should be satisfied | quality assurance | quality | S-01 page 142 | C-31 |
| R-0133 | Different aspects should be considered during the testing of a blockchain-based system | quality assurance | quality | S-01 page 143 | C-31 |
| R-0134 | Impact analysis should be done as cost-effectively as possible | software engineers | quality | S-01 page 172 | C-43 |
| R-0135 | The maintainer should replicate or verify changes by planning and executing the appropriate tests, including regression testing | software engineers | quality | S-01 page 171 | C-31 |
| R-0136 | Maintainability should be specified, reviewed and controlled during software development activities | software engineers | quality | S-01 page 172 | C-33 |
| R-0137 | Software engineers must investigate three areas in depth when they address technical debt: code quality versus relevance, alignment with organizational objectives, and process loss | software engineers | quality | S-01 page 173 | C-43 |
| R-0138 | Organizational objectives and constraints must be balanced with software maintainability and engineering standards to avoid code decay and technical debt | management | quality | S-01 page 173 | C-43 |
| R-0139 | Organizations need to design development and maintenance teams and roles carefully and provide professional development opportunities for their staff | management | quality | S-01 page 174 | C-39 |
| R-0140 | Outsourcers need to invest in good communication infrastructure and in an efficient help desk staffed with people who can communicate effectively | suppliers | security | S-01 page 174 | C-19 |
| R-0141 | Software engineering organizations must consider the advantages and disadvantages of each alternative when deciding where the maintenance function will be located | management | quality | S-01 page 175 | C-43 |
| R-0142 | It is important that the organization delegates maintenance tasks to an experienced group or person and keeps quality documentation on maintenance tasks and all changes | management | quality | S-01 page 175 | C-37 |
| R-0143 | A handoff process must be put in place between developers and maintainers | software engineers | operations | S-01 page 175 | C-29 |
| R-0144 | Software engineers must understand the different categories of software maintenance | software engineers | quality | S-01 page 175 | C-43 |
| R-0145 | The codebase of a software product must remain maintainable, easily understood, and easy to further evolve | software engineers | quality | S-01 page 175 | C-43 |
| R-0146 | An estimate of software maintenance costs should be prepared early in the software planning process | management | quality | S-01 page 175 | C-42 |
| R-0147 | The costs of software maintenance should be a function of the scope of the maintenance activities | management | quality | S-01 page 175 | C-42 |
| R-0148 | Historical measurement data should be used as inputs to estimate maintenance costs | management | quality | S-01 page 176 | C-42 |
| R-0149 | The cost estimating method should be described | management | quality | S-01 page 176 | C-42 |
| R-0150 | Cost estimates should be amended as maintenance and development efforts progress | management | quality | S-01 page 176 | C-42 |
| R-0151 | Maintainers should determine which measures are appropriate for a specific organization, based on that organization's needs | software engineers | quality | S-01 page 176 | C-35 |
| R-0152 | Maintainers must understand and use software artifacts from development, support them immediately, and progressively evolve and maintain them over time | software engineers | quality | S-01 page 169 | C-43 |
| R-0153 | Maintainers must track requirements in their activities and update documentation as baselines change | software engineers | quality | S-01 page 177 | C-38 |
| R-0154 | When a maintainer uses a development process, the process must be tailored to meet specific needs | software engineers | quality | S-01 page 178 | C-43 |
| R-0155 | Software maintenance planning should begin with the decision to develop a new software product and should consider quality objectives | software engineers | quality | S-01 page 178 | C-43 |
| R-0156 | A concept document should be developed, followed by a maintenance plan that addresses scope, process and tool adaptation, the maintenance organization, and cost estimates | software engineers | quality | S-01 page 178 | C-43 |
| R-0157 | The release or version planning activity requires that the maintainer collect release dates, agree content with users, identify conflicts, assess risk with a back-out plan, and inform all stakeholders | software engineers | operations | S-01 page 178 | C-21 |
| R-0158 | A software maintenance plan should be prepared during software development and should specify how users request modifications and report problems | software engineers | quality | S-01 page 179 | C-43 |
| R-0159 | The maintenance organization must conduct software maintenance business planning activities | management | quality | S-01 page 179 | C-43 |
| R-0160 | SCM procedures should provide for the verification, validation and audit of each step required to identify, authorize, implement and release the software product and its IT assets | quality assurance | operations | S-01 page 179 | C-45 |
| R-0161 | Any change made to the software product and its underlying infrastructure must be controlled | software engineers | operations | S-01 page 179 | C-26 |
| R-0162 | The activities and techniques for SQA, V&V, reviews and audits must be selected in concert with all other processes to achieve the desired level of quality | quality assurance | quality | S-01 page 179 | C-34 |
| R-0163 | It is recommended that both software operations and maintenance adapt and use the output of the software development process, its techniques and deliverables, and test results | software engineers | quality | S-01 page 179 | C-43 |
| R-0164 | Maintainers should have an effective quality program and must implement processes that support the continuous improvement of software maintenance processes | software engineers | quality | S-01 page 179 to page 180 | C-35 |
| R-0165 | Continuous integration often requires that the code be continuously refactored to augment its quality and reliability | software engineers | quality | S-01 page 179 to page 180 | C-32 |
| R-0166 | SCM activities must be planned accordingly for frequent build-test-deploy cycles of continuous integration | software engineers | operations | S-01 page 188 | C-45 |
| R-0167 | SCM process planning should be consistent with the organizational context, applicable constraints, guidance and the nature of the project | software engineers | operations | S-01 page 187 | C-45 |
| R-0168 | Where software is part of a larger system, SCM must be consistent with system-level CM | software engineers | operations | S-01 page 187 | C-45 |
| R-0169 | Branching and merging strategies should be carefully planned and communicated | software engineers | security | S-01 page 187 | C-01 |
| R-0170 | Organizational roles must be clearly identified to prevent confusion about who performs SCM tasks | management | quality | S-01 page 188 | C-40 |
| R-0171 | The tool selection questions on organization, tools, environment and the other listed topics should be considered | software engineers | operations | S-01 page 188 | C-45 |
| R-0172 | An SCM plan should include sections on introduction, SCM management, SCM activities, SCM schedules, SCM resources and plan maintenance | software engineers | operations | S-01 page 189 | C-45 |
| R-0173 | The SCM requirements for subcontracted software need to be established, with a means to monitor compliance | management | security | S-01 page 189 | C-19 |
| R-0174 | Care must be taken to keep SCM surveillance focused on the insights the measurements give | quality assurance | operations | S-01 page 190 | C-45 |
| R-0175 | A balance must be achieved between project visibility and a manageable number of controlled items when selecting SCIs | software engineers | operations | S-01 page 191 | C-45 |
| R-0176 | Requirements and test cases should be linked with the code baselines developed | software engineers | quality | S-01 page 192 | C-38 |
| R-0177 | The repository of binary objects should contain cryptographic hashes used for the physical configuration audit | software engineers | operations | S-01 page 192 | C-46 |
| R-0178 | Identifying and strictly adhering to the change rules of the sector or company is very important | software engineers | operations | S-01 page 193 | C-26 |
| R-0179 | A change request application must include a CR form that describes the request and gives its rationale | software engineers | operations | S-01 page 194 | C-26 |
| R-0180 | Supporting tools and build instructions must be under SCM control | software engineers | operations | S-01 page 197 | C-45 |
| R-0181 | Configuration status information should be secured where relevant | software engineers | operations | S-01 page 195 | C-45 |
| R-0182 | Each configuration audit must be carefully planned | quality assurance | operations | S-01 page 196 | C-45 |
| R-0183 | How to conduct the audit review and the expected result must be described in the quality plan, or defined for the configuration auditing activity if there is no quality plan | quality assurance | quality | S-01 page 196 | C-34 |
| R-0184 | The SCSA activity must be done by following the requirements (the source does not name which requirements in this sentence) | software engineers | operations | S-01 pages 195 to 196 | C-45 |
| R-0185 | Software is an enduring capability that must be supported and continuously improved throughout its life cycle | management | quality | S-01 page 203 | C-43 |
| R-0186 | Software organizational engineering managers should be conversant with the project management and software measurement knowledge in this KA | management | quality | S-01 page 203 | C-39 |
| R-0187 | Software organizational engineering managers should also possess some target domain knowledge | management | quality | S-01 page 203 | C-39 |
| R-0188 | Software engineers should have a sound understanding of the aspects of management unique to software projects | software engineers | quality | S-01 page 204 | C-39 |
| R-0189 | Software engineers should also have some knowledge of the general aspects of management, even in the first few years after graduation | software engineers | quality | S-01 page 204 | C-39 |
| R-0190 | It is important to provide an environment that attracts and retains good talent | management | quality | S-01 page 204 | C-40 |
| R-0191 | Software engineers must use both measurement and management to be effective | software engineers | quality | S-01 page 205 | C-35 |
| R-0192 | The imperatives of delivery speed, continuous adaptation and frequent upgrades should be balanced with risk management activities | management | quality | S-01 page 206 | C-42 |
| R-0193 | It is important to understand the difference between phases and activities | software engineers | quality | S-01 page 206 | C-42 |
| R-0194 | New software life cycles maybe required for AI-based software to manage the complexity it brings | management | quality | S-01 page 206 | C-42 |
| R-0195 | Activities should include software requirements review: elicitation, analysis, specification and validation | software engineers | quality | S-01 page 207 | C-38 |
| R-0196 | Methods and techniques should be selected and applied considering the various stakeholder perspectives | software engineers | quality | S-01 page 207 | C-38 |
| R-0197 | An initial project and product scope statement, deliverables, duration constraints and resource estimate should be prepared | management | quality | S-01 page 207 | C-42 |
| R-0198 | Stakeholders should agree on how requirements and scope will be reviewed and revised | management | quality | S-01 page 208 | C-38 |
| R-0199 | Scope and requirements should be revisited at predetermined points | management | quality | S-01 page 208 | C-42 |
| R-0200 | If changes are accepted, forward or backward traceability analysis should be used | software engineers | quality | S-01 page 208 | C-38 |
| R-0201 | If changes are accepted, risk analysis should be used | management | quality | S-01 page 208 | C-42 |
| R-0202 | Engineers should consider all configuration items as tasks to have under control while they develop the WBS | software engineers | operations | S-01 page 208 | C-45 |
| R-0203 | A key step in software project planning should be selecting an appropriate SDLC model and perhaps tailoring it | management | quality | S-01 page 208 | C-42 |
| R-0204 | In all SDLCs, risk assessment should be an element of initial project planning | management | quality | S-01 page 208 | C-42 |
| R-0205 | The risk profile should be discussed and accepted by all relevant stakeholders | management | quality | S-01 page 208 | C-42 |
| R-0206 | Software quality management processes should be planned along with project planning | quality assurance | quality | S-01 page 208 | C-34 |
| R-0207 | Project planning should establish procedures and responsibilities for SQA, verification and validation, reviews and audits | quality assurance | quality | S-01 page 208 | C-34 |
| R-0208 | Processes and responsibilities for ongoing review and revision of the project plan should be clearly stated and agreed upon | management | quality | S-01 page 208 to 209 | C-42 |
| R-0209 | Each project activity work product should be identified and characterized | software engineers | operations | S-01 page 209 | C-45 |
| R-0210 | Opportunities to reuse software components or use off-the-shelf products should be evaluated | software engineers | security | S-01 page 209 | C-10 |
| R-0211 | Software procurement and use of third parties should be planned and suppliers selected | management | security | S-01 page 209 | C-19 |
| R-0212 | Relevant methods should be selected as part of planning | software engineers | quality | S-01 page 209 | C-42 |
| R-0213 | Tools used throughout the project should be planned for and acquired | software engineers | quality | S-01 page 209 | C-42 |
| R-0214 | Software project managers should use multiple estimation approaches and reconcile the differences among them | management | quality | S-01 page 209 | C-42 |
| R-0215 | It is best to also use bottom-up estimation based on estimates from those who do the work and on historical data | management | quality | S-01 page 209 | C-42 |
| R-0216 | Effort, schedule and cost estimation should be negotiated and revised among affected stakeholders until consensus is reached | management | quality | S-01 page 210 | C-42 |
| R-0217 | Project managers should constantly monitor stakeholder requirements and changes and analyse their impact on cost and schedule | management | quality | S-01 page 210 | C-42 |
| R-0218 | Particular attention should be paid to managing risks related to software quality requirements such as safety or security | management | security | S-01 page 210 | C-12 |
| R-0219 | Risk management should be done not only at the beginning of a project but also at periodic intervals | management | quality | S-01 page 210 | C-42 |
| R-0220 | Equipment, facilities and people should be allocated to the identified tasks | management | quality | S-01 page 210 | C-42 |
| R-0221 | Software quality requirements should be identified, perhaps both quantitatively and qualitatively | quality assurance | quality | S-01 page 211 | C-33 |
| R-0222 | Thresholds for acceptable quality measurements should be set for each software quality requirement based on stakeholder needs and expectations | quality assurance | quality | S-01 page 211 | C-33 |
| R-0223 | Procedures for ongoing SQA and quality improvement should be specified during quality planning | quality assurance | quality | S-01 page 211 | C-34 |
| R-0224 | Plans should be developed and managed when change is expected | management | quality | S-01 page 211 | C-42 |
| R-0225 | The magnitude of planning effort and the plan content should be determined partly by the risk of not developing the plan | management | quality | S-01 page 211 | C-42 |
| R-0226 | The management of the project plan should itself be planned | management | quality | S-01 page 211 | C-42 |
| R-0227 | Plans and processes should be systematically monitored, reviewed, reported and when appropriate revised | management | quality | S-01 page 211 | C-42 |
| R-0228 | Plans for supporting processes such as documentation, configuration management and problem resolution should be managed | management | operations | S-01 page 211 | C-45 |
| R-0229 | Reporting, monitoring and controlling should fit within the selected SDLC and the realities of the project | management | quality | S-01 page 211 | C-42 |
| R-0230 | Plans should account for the various artifacts used to manage the project | management | quality | S-01 page 211 | C-42 |
| R-0231 | In adaptive programs the emphasis should be on selecting and retaining useful project information and establishing strategy, policies and procedures | management | quality | S-01 page 211 | C-40 |
| R-0232 | Project activities should follow the project plan and supporting plans | software engineers | quality | S-01 page 212 | C-42 |
| R-0233 | There should be a focus on adherence to the selected SDLC processes | software engineers | quality | S-01 page 212 | C-34 |
| R-0234 | Regardless of how components are obtained, verification, integration and validation activities should be performed | software engineers | security | S-01 page 212 | C-10 |
| R-0235 | Organizations should consider introducing technical or procedural controls to minimize risk from unfiltered access to external library repositories | management | security | S-01 page 212 | C-10 |
| R-0236 | Execution of the project in compliance with the terms of a supplier or customer agreement should be managed | management | security | S-01 page 213 | C-19 |
| R-0237 | The measurement process should be enacted during the project to ensure relevant and useful data is collected | management | quality | S-01 page 213 | C-35 |
| R-0238 | Adherence to scope, project plan and related plans should be assessed continually and at predetermined intervals | management | quality | S-01 page 213 | C-42 |
| R-0239 | Outputs and completion criteria for each task should be assessed | quality assurance | quality | S-01 page 213 | C-34 |
| R-0240 | Deliverables should be evaluated for their required characteristics | quality assurance | quality | S-01 page 213 | C-34 |
| R-0241 | Effort expenditure, schedule adherence, costs to date and resource use should be analyzed | management | quality | S-01 page 213 | C-42 |
| R-0242 | The project risk profile should be revisited | management | quality | S-01 page 213 | C-42 |
| R-0243 | Adherence to software quality requirements should be evaluated | quality assurance | quality | S-01 page 213 | C-35 |
| R-0244 | Measurement data should be analyzed | quality assurance | quality | S-01 page 213 | C-35 |
| R-0245 | Variance analysis should be conducted to find deviation from expected outcomes | management | quality | S-01 page 213 | C-42 |
| R-0246 | Outlier identification and analysis of quality and other measurement data should be performed | quality assurance | quality | S-01 page 213 | C-35 |
| R-0247 | Risk exposures should be recalculated | management | quality | S-01 page 213 | C-42 |
| R-0248 | Outcomes should be reported as necessary or when thresholds have been exceeded | management | quality | S-01 page 213 | C-42 |
| R-0249 | The software development team should adhere to software configuration control and software configuration management procedures | software engineers | operations | S-01 page 214 | C-45 |
| R-0250 | Decisions should be documented and communicated to all relevant parties, plans revised when necessary, and relevant data recorded | management | quality | S-01 page 214 | C-42 |
| R-0251 | Progress to date should be reported at specified and agreed times within the organization and to external stakeholders | management | quality | S-01 page 214 | C-42 |
| R-0252 | Reports should focus on the information needs of the target audience | management | quality | S-01 page 214 | C-42 |
| R-0253 | Overall progress and satisfaction of stakeholder requirements should be evaluated at prespecified times and as needed | management | quality | S-01 page 214 | C-42 |
| R-0254 | Effectiveness of the software process, personnel, tools and methods should be assessed regularly and as circumstances demand | management | quality | S-01 page 214 | C-35 |
| R-0255 | Progress toward stakeholder satisfaction should be assessed periodically | management | quality | S-01 page 214 | C-42 |
| R-0256 | Progress should be assessed upon achieving a major milestone or completing an iterative cycle | management | quality | S-01 page 214 | C-42 |
| R-0257 | Criteria for project, phase or iteration success should be evaluated | management | quality | S-01 page 214 | C-42 |
| R-0258 | The project process should be systematically and periodically assessed for relevance, utility and efficacy | management | quality | S-01 page 214 | C-35 |
| R-0259 | Project methods, tools and techniques should be evaluated for effectiveness and appropriateness | management | quality | S-01 page 214 | C-35 |
| R-0260 | Where appropriate, project changes should be made and managed | management | quality | S-01 page 214 | C-42 |
| R-0261 | Closure processes should involve relevant stakeholders and document their acceptance | management | quality | S-01 page 215 | C-42 |
| R-0262 | Known problems should be documented at closure | management | quality | S-01 page 215 | C-37 |
| R-0263 | Project materials should be archived in accordance with stakeholder agreed rules | management | operations | S-01 page 215 | C-45 |
| R-0264 | The organization measurement database should be updated with relevant project data | management | quality | S-01 page 215 | C-35 |
| R-0265 | A project, phase or iteration retrospective analysis should be undertaken | software engineers | quality | S-01 page 215 | C-35 |
| R-0266 | Lessons learned should be drawn from the project and fed into organizational learning | management | quality | S-01 page 215 | C-35 |
| R-0267 | Each measurement endeavor should be guided by organizational objectives and measurement requirements | management | quality | S-01 page 215 | C-35 |
| R-0268 | The project team should establish the organizational unit to which each measurement requirement is applied | management | quality | S-01 page 215 | C-35 |
| R-0269 | The commitment to measurement should be formally established, communicated and supported by resources | management | quality | S-01 page 215 | C-40 |
| R-0270 | Adequate funding, training, tools and support for the measurement process should be allocated | management | quality | S-01 page 215 | C-40 |
| R-0271 | Information needs should be identified, prioritized, documented, communicated and reviewed by stakeholders | management | quality | S-01 page 216 | C-35 |
| R-0272 | The appropriate stakeholders should review and approve the measurement plan | management | quality | S-01 page 216 | C-35 |
| R-0273 | Criteria for reviewing measurement artifacts should be established at organizational unit level or higher | quality assurance | quality | S-01 page 216 | C-35 |
| R-0274 | Review criteria should consider experience, resource availability and potential disruptions to projects | quality assurance | quality | S-01 page 216 | C-35 |
| R-0275 | Provide resources for measurement tasks | management | quality | S-01 page 216 | C-40 |
| R-0276 | Characterize the organizational unit as the context for measurement | management | quality | S-01 page 216 | C-35 |
| R-0277 | Identify information needs from organizational goals, constraints, risks and problems | management | quality | S-01 page 216 | C-35 |
| R-0278 | Select measures with clear links to information needs | management | quality | S-01 page 216 | C-35 |
| R-0279 | Define data collection, analysis and reporting procedures | management | quality | S-01 page 216 | C-35 |
| R-0280 | Select criteria for evaluating information products | management | quality | S-01 page 216 | C-35 |
| R-0281 | Consider measuring internal software quality to give an early indicator of potential issues | quality assurance | quality | S-01 page 216 | C-35 |
| R-0282 | Identify resources to be made available for the measurement tasks | management | quality | S-01 page 216 | C-40 |
| R-0283 | Acquire and deploy supporting technologies for measurement | management | quality | S-01 page 216 | C-35 |
| R-0284 | Consider the resources necessary for successful deployment of new procedures or measures | management | quality | S-01 page 216 | C-40 |
| R-0285 | Measurement procedures should be integrated into the software processes they measure | software engineers | quality | S-01 page 216 | C-35 |
| R-0286 | Consider morale issues and other human factors when integrating measurement procedures | management | quality | S-01 page 217 | C-35 |
| R-0287 | Measurement procedures should be communicated to those providing the data, with training and support | software engineers | quality | S-01 page 217 | C-35 |
| R-0288 | Measurement data should be collected and analyzed | quality assurance | quality | S-01 page 217 | C-35 |
| R-0289 | Data should be collected, verified and stored | quality assurance | quality | S-01 page 217 | C-35 |
| R-0290 | Data providers and measurement users should participate in reviewing the data | software engineers | quality | S-01 page 217 | C-35 |
| R-0291 | Information products should be documented and communicated to users and stakeholders | management | quality | S-01 page 217 | C-35 |
| R-0292 | Information products and the measurement process should be evaluated against specified criteria | quality assurance | quality | S-01 page 217 | C-35 |
| R-0293 | Lessons learned should be recorded in an appropriate database | management | quality | S-01 page 217 | C-35 |
| R-0294 | Potential improvements should be identified with their costs and benefits, and appropriate improvement actions reported | management | quality | S-01 page 217 | C-35 |
| R-0295 | Proposed improvements should be communicated to the measurement process owner and stakeholders for review and approval | management | quality | S-01 page 217 | C-35 |
| R-0296 | The lack of potential improvements should be communicated when the analysis fails to identify any | management | quality | S-01 page 217 | C-35 |
| R-0297 | Software processes must be selected, adapted and applied for each project and each organizational context | management | quality | S-01 page 222 | C-42 |
| R-0298 | Process management is essential to be supported by empirical measurement | management | quality | S-01 page 222 | C-35 |
| R-0299 | A life cycle should be defined following engineering principles | management | quality | S-01 page 224 | C-42 |
| R-0300 | The process specification should be useful to humans so that they can communicate with it | software engineers | quality | S-01 page 224 | C-37 |
| R-0301 | The life cycle specification should be easy to understand and correct | software engineers | quality | S-01 page 224 | C-37 |
| R-0302 | When a project process is defined in conformance with a life cycle, it is important to make sure that metrics and measure definitions will allow realistic estimates and measurements, and to define the level of precision and uncertainty | management | quality | S-01 page 228 | C-35 |
| R-0303 | Process and product measurements should always provide accurate information about the status of the process and the product while the life cycle is executed | management | quality | S-01 page 228 to 229 | C-35 |
| R-0304 | If the accuracy of estimations and measurements is uncertain, a reflection should take place on the overall approach | management | quality | S-01 page 229 | C-35 |
| R-0305 | Developers must monitor the software engineering process execution, assess whether the process objectives are met, and assess risks | software engineers | quality | S-01 page 229 | C-35 |
| R-0306 | Process monitoring requires assessing both process and product, with a joint approach | quality assurance | quality | S-01 page 229 | C-35 |
| R-0307 | Tools will, ideally, have to support the defined methods and be integrated with them | software engineers | quality | S-01 page 229 | C-30 |
| R-0308 | A successful unit test result should be recorded so that the rest of the team is aware of it | software engineers | quality | S-01 page 229 | C-30 |
| R-0309 | The configuration management tool and the testing tool will have to be integrated | software engineers | quality | S-01 page 229 | C-30 |
| R-0310 | The model should be checked for documented assumptions when it is reused | software engineers | quality | S-01 page 236 | C-38 |
| R-0311 | Model parts imported from another model or library must be examined for semantic assumptions that conflict with the new environment | software engineers | quality | S-01 page 236 | C-38 |
| R-0312 | Traceability relationships must be mapped and controlled to show that software requirements are consistent with the software model | software engineers | quality | S-01 page 238 | C-38 |
| R-0313 | The software engineer needs to choose an appropriate method or methods for the task at hand | software engineers | quality | S-01 page 239 | C-38 |
| R-0314 | Formal verification requires a rigorously specified model of the software and its operational environment | software engineers | quality | S-01 page 240 | C-34 |
| R-0315 | Release managers need to monitor the development process and the promotion schedule for each release | operations engineers | operations | S-01 page 243 | C-46 |
| R-0316 | Business needs should and do drive the choice of software engineering method | management | quality | S-01 page 243 | C-42 |
| R-0317 | The software process quality aspect must be made explicit | quality assurance | quality | S-01 page 247 | C-34 |
| R-0318 | Agreement on software quality requires that the many aspects of quality be formally defined and communicated | quality assurance | quality | S-01 page 248 | C-33 |
| R-0319 | Software engineers should understand software quality concepts, characteristics and values, and their application to development, maintenance and operation | software engineers | quality | S-01 page 248 | C-39 |
| R-0320 | The software requirements are expected to define the required software quality attributes | quality assurance | quality | S-01 page 248 | C-33 |
| R-0321 | Software quality should be planned early and assessed at many milestones during the software life cycle | quality assurance | quality | S-01 page 248 | C-34 |
| R-0322 | Software engineers are expected to share a commitment to software quality in the context of their industry | software engineers | quality | S-01 page 248 | C-40 |
| R-0323 | Software engineers should use the meaning of error and defect given by their standards | software engineers | quality | S-01 page 248 | C-39 |
| R-0324 | Software engineers should inform their administration of the risks they take when they are not fully committed to quality | software engineers | quality | S-01 page 249 | C-40 |
| R-0325 | Software engineers should seek the optimal cost of software quality, the minimal total cost for a specified quality level | software engineers | quality | S-01 page 249 | C-42 |
| R-0326 | Software engineers should know the key software engineering standards that apply to their industry | software engineers | quality | S-01 page 249 | C-39 |
| R-0327 | Software engineers and their managers must understand the threats and issues and develop the skills to prevent accidents | software engineers | quality | S-01 page 250 | C-39 |
| R-0328 | Software in safety-critical systems requires the use of systematic methods and tools to ensure its high quality | software engineers | quality | S-01 page 250 | C-34 |
| R-0329 | For a QMS to be effective, management support is imperative | management | quality | S-01 page 251 | C-40 |
| R-0330 | Management sponsorship should be requested frequently during software project reviews | management | quality | S-01 page 251 | C-40 |
| R-0331 | The software organization must commit to quality by establishing its quality management system | management | quality | S-01 page 252 | C-34 |
| R-0332 | Responsibility and authority for the QMS requires that they be assigned and be independent of current project management teams | management | quality | S-01 page 252 | C-40 |
| R-0333 | Software engineers should promote the use of formally approved processes and procedures that implement the quality policy | software engineers | quality | S-01 page 252 | C-34 |
| R-0334 | A QMS used for improvement should have its processes documented with its user in mind, and identify where quality controls are to be verified | quality assurance | quality | S-01 page 252 | C-34 |
| R-0335 | Software engineers will gather and analyze quality assurance evaluation results periodically | software engineers | quality | S-01 page 253 | C-35 |
| R-0336 | Software engineers should establish a meaningful defect classification taxonomy | software engineers | quality | S-01 page 254 | C-35 |
| R-0337 | It is important that corrective actions be documented and submitted when quality objectives are not met | quality assurance | quality | S-01 page 254 | C-35 |
| R-0338 | Project participants require a way of reporting software process and tool problems to an independent organization | software engineers | quality | S-01 page 254 | C-35 |
| R-0339 | The SQA plan should not conflict with the software configuration management plan or other project planning artifacts | quality assurance | quality | S-01 page 255 | C-34 |
| R-0340 | SQA activities should be considered complementary to the SCM process audit and the testing activities | quality assurance | quality | S-01 page 255 | C-34 |
| R-0341 | The quality assurance activities listed in IEEE 730 should be conducted early in a software project's life cycle | quality assurance | quality | S-01 page 255 | C-34 |
| R-0342 | Software engineers should be aware of the need to plan and execute SQA activities at certain project milestones and keep records of their execution | software engineers | quality | S-01 page 256 | C-34 |
| R-0343 | Software engineers are responsible for eliciting quality requirements that might not be explicit at the outset | software engineers | quality | S-01 page 256 | C-33 |
| R-0344 | Software engineers should understand how to define quality requirements and quality targets so that they can be measured at acceptance | software engineers | quality | S-01 page 256 | C-33 |
| R-0345 | Software engineers must keep quality requirements in mind during project planning | software engineers | quality | S-01 page 256 | C-33 |
| R-0346 | Software engineers must anticipate potential additional development costs if safety, security and dependability attributes are important | software engineers | quality | S-01 page 256 | C-42 |
| R-0347 | Software engineers should identify which work products and software artifacts require configuration management | software engineers | operations | S-01 page 256 | C-45 |
| R-0348 | Software engineers should be familiar with source code versioning processes | software engineers | quality | S-01 page 256 | C-39 |
| R-0349 | Software engineers should know how to operate the version control tool kit | software engineers | quality | S-01 page 256 | C-39 |
| R-0350 | Software engineers should know the software characteristics that can be planned, implemented and measured during construction | software engineers | quality | S-01 page 256 | C-39 |
| R-0351 | Software engineers should know that certain quality characteristics have conflicting impacts | software engineers | quality | S-01 page 256 | C-39 |
| R-0352 | Sound engineering practice requires that intermediate work products relevant to quality be evaluated using reviews and inspections | quality assurance | quality | S-01 page 257 | C-34 |
| R-0353 | Software engineers should identify the product integrity level and ensure that the minimum V&V tasks are assigned | quality assurance | quality | S-01 page 257 | C-34 |
| R-0354 | Software engineers should choose and apply the proper V&V task depending on the software integrity level | quality assurance | quality | S-01 page 257 | C-34 |
| R-0355 | The verification process and the validation process should begin early in development or maintenance | quality assurance | quality | S-01 page 257 | C-34 |
| R-0356 | Software engineers should plan the testing activities, including levels, techniques, measures and tools | quality assurance | quality | S-01 page 258 | C-31 |
| R-0357 | IEEE 730 recommends that testing completion criteria be set | quality assurance | quality | S-01 page 258 | C-31 |
| R-0358 | Software engineers should plan, execute and record the testing and retesting activities that IEEE 730 lists | quality assurance | quality | S-01 page 258 | C-31 |
| R-0359 | A software quality engineering team should be particularly involved in qualifying critical software products before delivery | quality assurance | quality | S-01 page 258 | C-34 |
| R-0360 | Reviews should be part of the software engineering culture and should be planned, executed and documented during the software life cycle | quality assurance | quality | S-01 page 259 | C-34 |
| R-0361 | Technical reviews and audits should be planned, approved and conducted | quality assurance | quality | S-01 page 259 | C-34 |
| R-0362 | Software engineers should define the security properties of their software and maintain them throughout the software development life cycle. | software engineers | security | S-01 page 264 | C-12 |
| R-0363 | Software engineers should consider the mitigation of threats as part of software development. | software engineers | security | S-01 page 265 | C-12 |
| R-0364 | Security must be considered during software maintenance. | software engineers | quality | S-01 page 264 | C-43 |
| R-0365 | Project managers need to elevate software security from a stand-alone technical concern to an enterprise issue. | management | quality | S-01 page 265 | C-40 |
| R-0366 | Organizations should use an ISMS to continually conduct risk assessments and deploy an IT team to monitor risks. | management | quality | S-01 page 266 | C-40 |
| R-0367 | Agile teams need to understand and adopt security practices and take more responsibility for their systems' security. | software engineers | quality | S-01 page 266 | C-40 |
| R-0368 | Security professionals must learn to accept change, work faster and more iteratively, and manage risks incrementally. | security team | quality | S-01 page 266 | C-40 |
| R-0369 | Security needs to become an enabler instead of a blocker. | security team | quality | S-01 page 266 | C-40 |
| R-0370 | Security must be built into software engineering to ensure software security. | software engineers | security | S-01 page 266 | C-13 |
| R-0371 | Comprehensive risk and threat analysis methods and management tools for IoT platforms are required. | security team | security | S-01 page 269 | C-12 |
| R-0372 | Recommended rule: structure the process so that all sections that need extra privileges are small modules that perform only those tasks. | software engineers | security | S-01 page 267 | C-06 |
| R-0373 | Recommended rule: validate program assumptions, or document them for installers and maintainers if validation is not possible. | software engineers | security | S-01 page 267 | C-13 |
| R-0374 | Recommended rule: ensure that the program does not share objects in memory with any other program. | software engineers | security | S-01 page 267 | C-13 |
| R-0375 | Recommended rule: check every function's error status, and restore the earlier state and terminate if recovery could affect security. | software engineers | security | S-01 page 267 | C-13 |
| R-0376 | Recommended practice: validate input. | software engineers | security | S-01 page 268 | C-13 |
| R-0377 | Recommended practice: heed compiler warnings. | software engineers | security | S-01 page 268 | C-13 |
| R-0378 | Recommended practice: architect and design for security policies. | software engineers | security | S-01 page 268 | C-12 |
| R-0379 | Recommended practice: keep it simple. | software engineers | security | S-01 page 268 | C-13 |
| R-0380 | Recommended practice: default deny. | software engineers | security | S-01 page 268 | C-13 |
| R-0381 | Recommended practice: adhere to the principle of least privilege. | software engineers | security | S-01 page 268 | C-13 |
| R-0382 | Recommended practice: sanitize data sent to other software. | software engineers | security | S-01 page 268 | C-13 |
| R-0383 | Recommended practice: practice defense in depth. | software engineers | security | S-01 page 268 | C-13 |
| R-0384 | Recommended practice: use effective quality assurance techniques. | software engineers | quality | S-01 page 268 | C-34 |
| R-0385 | Recommended practice: adopt a software construction security standard. | software engineers | security | S-01 page 268 | C-13 |
| R-0386 | Security experts should be engaged to perform dynamic security tests. | security team | security | S-01 page 268 | C-17 |
| R-0387 | Security tests should always be conducted within legal boundaries and with proper authorization. | security team | security | S-01 page 268 | C-17 |
| R-0388 | The expertise of security professionals is required to operate and configure analysis tools and to verify their results. | security team | security | S-01 page 268 | C-11 |
| R-0389 | Software engineers must handle unique engineering problems to produce software with known characteristics and reliability. | software engineers | quality | S-01 page 274 | C-39 |
| R-0390 | Software engineers shall commit themselves to making the analysis, specification, design, development, testing and maintenance of software a beneficial and respected profession. | software engineers | quality | S-01 page 277 | C-39 |
| R-0391 | Software engineers shall adhere to the ten principles of the IEEE Code of Ethics adopted in June 2020. | software engineers | quality | S-01 page 277 | C-39 |
| R-0392 | Software engineers are often required to sign nondisclosure or IP agreements as a precondition to working. | software engineers | quality | S-01 page 278 | C-41 |
| R-0393 | Software engineers must operate within local, national and international legal frameworks. | software engineers | quality | S-01 page 280 | C-41 |
| R-0394 | Software engineers must know the legal requirements for registration, licensing, trade and data privacy. | software engineers | quality | S-01 page 280 | C-41 |
| R-0395 | Software engineers have a professional obligation to consider the threat of cybercrime and how security protects software and user information. | software engineers | quality | S-01 page 280 | C-39 |
| R-0396 | Software engineers should avoid certifying unacceptable products, disclosing confidential information, and falsifying facts or data. | software engineers | quality | S-01 page 281 | C-39 |
| R-0397 | Software engineers should be responsible for their actions and transparent with users. | software engineers | quality | S-01 page 281 | C-39 |
| R-0398 | Software engineers should know that data privacy is a key legal requirement. | software engineers | quality | S-01 page 281 | C-41 |
| R-0399 | Software engineers and their managers should provide requirements, design, tool, test and problem documentation to other parts of the development organization. | software engineers | quality | S-01 page 281 | C-37 |
| R-0400 | Software documentation for external stakeholders should describe whether the software meets needs, safe and unsafe use, protection of sensitive information, and warnings and critical procedures. | users and customers | quality | S-01 page 281 | C-37 |
| R-0401 | Software engineers should document relevant facts, significant risks and trade-offs, warnings of dangerous consequences, and attribute, license and sourcing information. | software engineers | quality | S-01 page 281 | C-37 |
| R-0402 | Where the customer acquires the source code, the software engineer should provide documentation of the functional specifications, design, test suite and operating environment. | software engineers | quality | S-01 page 282 | C-37 |
| R-0403 | Documents should be kept for at least as long as the software product's life cycle or as organizational or regulatory requirements demand. | management | quality | S-01 page 282 | C-41 |
| R-0404 | The software engineer should be objective and impartial when selecting and weighting criteria, and any conflict of interest must be disclosed upfront. | software engineers | quality | S-01 page 282 | C-39 |
| R-0405 | A software engineer must ethically conduct a trade-off analysis. | software engineers | quality | S-01 page 282 | C-42 |
| R-0406 | Software engineers must work with others. | software engineers | quality | S-01 page 282 | C-39 |
| R-0407 | A software engineer should interact cooperatively and constructively with others. | software engineers | quality | S-01 page 282 | C-39 |
| R-0408 | Stakeholders should provide support, information and feedback at all stages of the software life cycle. | management | quality | S-01 page 283 | C-40 |
| R-0409 | Software engineers should deal with uncertainty by investigating it or, if it is a project risk, by adjusting estimates or pricing. | software engineers | quality | S-01 page 284 | C-42 |
| R-0410 | Software engineers must be able to read and understand technical material. | software engineers | quality | S-01 page 285 | C-39 |
| R-0411 | In all cases, written software engineering products must be accessible, understandable and relevant to their intended audience. | software engineers | quality | S-01 page 285 | C-37 |
| R-0412 | Software engineering decisions must also consider relevant unquantifiable criteria. | software engineers | quality | S-01 page 289 | C-42 |
| R-0413 | Engineers must evaluate a proposal from a financial perspective to make a meaningful decision about it. | software engineers | quality | S-01 page 290 | C-42 |
| R-0414 | The do-nothing alternative should be considered in most, but not all, situations. | software engineers | quality | S-01 page 291 | C-42 |
| R-0415 | All steps should be completed thoroughly and carefully when the consequences of a wrong decision are significant. | software engineers | quality | S-01 page 292 | C-42 |
| R-0416 | The source says to be sure not to skip any step of the decision process or execute it poorly. | software engineers | quality | S-01 page 292 | C-42 |
| R-0417 | ISO 12207 and ISO 15288 recommend defining a decision management strategy for high-consequence decisions. | management | quality | S-01 page 292 | C-42 |
| R-0418 | ISO 12207 and ISO 15288 recommend identifying relevant stakeholders for high-consequence decisions. | management | quality | S-01 page 292 | C-42 |
| R-0419 | More time, effort and care should be spent on high-consequence decisions. | software engineers | quality | S-01 page 292 | C-42 |
| R-0420 | Software engineers must use their best judgment in deciding when they have enough candidates. | software engineers | quality | S-01 page 293 | C-42 |
| R-0421 | As much as possible, each criterion should be expressed objectively. | software engineers | quality | S-01 page 293 | C-42 |
| R-0422 | When a selection criterion involves money, each alternative must be judged from the same viewpoint. | software engineers | quality | S-01 page 293 | C-42 |
| R-0423 | Use the same basis for comparison, the same planning horizon and the same kinds of costs for each alternative. | software engineers | quality | S-01 page 293 | C-42 |
| R-0424 | High-consequence decisions may benefit from formally recording the selected alternative and the justification. | software engineers | quality | S-01 page 294 | C-38 |
| R-0425 | The software engineer needs to close the loop on estimates by comparing them to actual outcomes. | software engineers | quality | S-01 page 294 | C-42 |
| R-0426 | The intangible assets must be explicitly considered in many decisions, particularly when the consequences of a wrong decision are high. | software engineers | quality | S-01 page 297 | C-42 |
| R-0427 | Indicators must be normalized and standardized to operate correctly. | software engineers | quality | S-01 page 298 | C-35 |
| R-0428 | All criteria must be considered to decide what software products should be developed for the client organization. | management | quality | S-01 page 300 | C-42 |
| R-0429 | Ensure realistic quantitative estimates of cost, scheduling, personnel, quality and outcomes. | software engineers | quality | S-01 page 301 | C-42 |
| R-0430 | Provide an uncertainty assessment of the estimates made on a project. | software engineers | quality | S-01 page 301 | C-42 |
| R-0431 | Software engineers must be conscious of the software's importance as a driver of business accounts. | software engineers | quality | S-01 page 303 | C-40 |
| R-0432 | Software engineers must be conscious of the importance of software to business finances. | software engineers | quality | S-01 page 304 | C-40 |
| R-0433 | Software engineers must consider control of the organization part of their job by ensuring alignment of their software with business goals. | software engineers | quality | S-01 page 304 | C-40 |
| R-0434 | Software engineering economics should be concerned with all SPLC activities. | management | quality | S-01 page 306 | C-42 |
| R-0435 | An SPLC should include risk management and synchronization with different suppliers. | management | quality | S-01 page 306 | C-42 |
| R-0436 | An SPLC should provide auditable decision-making information, for example to comply with product liability or governance regulations. | management | quality | S-01 page 306 | C-41 |
| R-0437 | Software engineers must understand how their role differs from that of a programmer. | software engineers | quality | S-01 page 313 | C-39 |
| R-0438 | Software engineers are expected to have deep and broad knowledge of computer science concepts and apply them. | software engineers | quality | S-01 page 313 | C-39 |
| R-0439 | The problem must be analyzed in more detail for functional, user, performance, interface, security, vulnerability, durability and upgradability needs. | software engineers | quality | S-01 page 313 | C-38 |
| R-0440 | Subsystems should be modular, highly cohesive and loosely coupled. | software engineers | quality | S-01 page 313 | C-38 |
| R-0441 | The hardware must be designed to support the software subsystems and meet all user requirements, including I/O and performance. | software engineers | quality | S-01 page 314 | C-38 |
| R-0442 | Software subsystem architects have to consider technology, tools, data structures, operating systems, databases, user interfaces, languages and algorithms. | software engineers | quality | S-01 page 314 | C-38 |
| R-0443 | Software engineers are expected to know the functioning and timing of different bus types. | software engineers | quality | S-01 page 314 | C-39 |
| R-0444 | Software engineers have to know the concepts needed to architect, design, construct, deploy and maintain high-quality software. | software engineers | quality | S-01 page 314 | C-39 |
| R-0445 | System architects must analyze the application, identify critical components and choose or design a suitable architecture. | software engineers | quality | S-01 page 314 | C-38 |
| R-0446 | Contingencies should be built in for the resources required. | management | quality | S-01 page 314 | C-42 |
| R-0447 | Software engineers need to know the different types of Flynn architecture, with examples. | software engineers | quality | S-01 page 316 | C-39 |
| R-0448 | Software engineers are expected to know the differences among architectures and case studies, so that they can choose the right one. | software engineers | quality | S-01 page 316 | C-39 |
| R-0449 | Software engineers are expected to know and apply other architectures, including .NET, Unix and virtual machine architectures. | software engineers | quality | S-01 page 316 | C-39 |
| R-0450 | System architects and engineers must know the system components and how they function. | software engineers | quality | S-01 page 316 | C-39 |
| R-0451 | Software engineers are expected to understand the interface of I/O devices, including memory-mapped and I/O-mapped devices, and device drivers. | software engineers | quality | S-01 page 317 | C-39 |
| R-0452 | Software engineers are expected to know the differences between multiple cores and multiple threads. | software engineers | quality | S-01 page 317 | C-39 |
| R-0453 | Software engineers are expected to know the types of control units and their benefits and challenges. | software engineers | quality | S-01 page 317 | C-39 |
| R-0454 | Software engineers working on performance-critical applications are expected to know the types of memory and their pros and cons. | software engineers | quality | S-01 page 317 | C-39 |
| R-0455 | Software engineers must internalize data structures, how to select them, and the operations on them for each application. | software engineers | quality | S-01 page 317 | C-39 |
| R-0456 | Algorithm design must consider system performance, security, portability, maintainability, scalability and simplicity. | software engineers | security | S-01 page 318 | C-13 |
| R-0457 | Software engineers must understand the data types, their sizes in memory, and how they are represented and operated on. | software engineers | quality | S-01 page 318 | C-39 |
| R-0458 | It is important to ensure that insertion or deletion does not break the policy of the database. | software engineers | security | S-01 page 318 | C-44 |
| R-0459 | Software engineers may need to understand strings and skip lists. | software engineers | quality | S-01 page 318 | C-39 |
| R-0460 | The software engineer must consider the application purpose and performance requirements when selecting an algorithm. | software engineers | quality | S-01 page 319 | C-38 |
| R-0461 | The software engineer must consider linear versus parallel programming and single-threaded versus multi-threaded designs. | software engineers | quality | S-01 page 319 | C-38 |
| R-0462 | A software engineer has to know a few standard algorithms and related concepts. | software engineers | quality | S-01 page 319 | C-39 |
| R-0463 | Learning the complexity notations for different input orders is important. | software engineers | quality | S-01 page 319 | C-39 |
| R-0464 | Software engineers should learn and accommodate the preconditions and complexity of sorting algorithms they use. | software engineers | quality | S-01 page 321 | C-39 |
| R-0465 | Software engineers are expected to learn, implement and compare hashing algorithms and collision resolution techniques. | software engineers | quality | S-01 page 321 | C-39 |
| R-0466 | Hash function properties must be understood and considered when designing or choosing a hash function. | software engineers | quality | S-01 page 321 | C-39 |
| R-0467 | Software engineers must carefully consider several aspects before they select a programming language. | software engineers | quality | S-01 page 321 | C-38 |
| R-0468 | Software engineers are expected to know how high-level languages are translated, and the types of compilers and their differences. | software engineers | quality | S-01 page 322 | C-39 |
| R-0469 | Software engineers need to study several programming languages to choose the right one for an application. | software engineers | quality | S-01 page 322 | C-39 |
| R-0470 | Software engineers should know the differences among programming paradigms and use them appropriately. | software engineers | quality | S-01 page 323 | C-39 |
| R-0471 | It is important to establish exit criteria in recursive subprograms. | software engineers | quality | S-01 page 323 | C-32 |
| R-0472 | Programs are expected to function properly and produce the expected output. | software engineers | quality | S-01 page 324 | C-31 |
| R-0473 | Programs must be tested thoroughly with valid, invalid and boundary-value inputs. | quality assurance | quality | S-01 page 324 | C-31 |
| R-0474 | Companies set rules that programmers and testers are to follow in their coding and testing. | software engineers | quality | S-01 page 325 | C-32 |
| R-0475 | Choose coding standards and guidelines that suit the application or system being built. | management | quality | S-01 page 325 | C-32 |
| R-0476 | Consider open standards from community groups and closed standards from working groups. | management | quality | S-01 page 325 | C-32 |
| R-0477 | Educate programmers to follow adopted standards and guidelines. | management | quality | S-01 page 326 | C-39 |
| R-0478 | Use tools and periodic reviews to make sure adopted standards and guidelines are followed. | management | quality | S-01 page 326 | C-32 |
| R-0479 | Review and revise standards and guidelines from time to time, using lessons from project execution. | management | quality | S-01 page 326 | C-35 |
| R-0480 | Software engineers need to understand the basic structure of operating systems, their types and design approaches. | software engineers | quality | S-01 page 326 | C-39 |
| R-0481 | Software engineers must understand processes, processors, address spaces, booting, threads and synchronization. | software engineers | quality | S-01 page 326 | C-39 |
| R-0482 | Software engineers should compare and contrast CPU scheduling concepts and algorithms. | software engineers | quality | S-01 page 326 | C-39 |
| R-0483 | Software engineers must have a deep understanding of inter-process communication and its types. | software engineers | quality | S-01 page 326 | C-39 |
| R-0484 | Software engineers need a deep understanding of deadlocks, including prevention, avoidance, detection and recovery. | software engineers | quality | S-01 page 326 | C-39 |
| R-0485 | Software engineers are required to study concurrent languages, process and scheduling concepts. | software engineers | quality | S-01 page 326 | C-39 |
| R-0486 | Software engineers have to analyze the types of operating systems to choose an appropriate one. | software engineers | quality | S-01 page 326 | C-39 |
| R-0487 | It is important to study examples of each operating system type and compare their benefits and limits. | software engineers | quality | S-01 page 326 | C-39 |
| R-0488 | Software engineers are recommended to refer to ISO/IEC JTC 1/SC 22 standards. | software engineers | quality | S-01 page 326 | C-39 |
| R-0489 | A software engineer needs a very good understanding of memory management, including fragmentation and paging. | software engineers | quality | S-01 page 327 | C-39 |
| R-0490 | Software engineers should understand device drivers, their types, and the interfaces to hardware devices. | software engineers | quality | S-01 page 327 | C-39 |
| R-0491 | Software engineers should understand that caching, scheduling, spooling and performance issues can arise for shared devices. | software engineers | quality | S-01 page 327 | C-39 |
| R-0492 | A software engineer must have good knowledge of the types of I/O devices and their buffering. | software engineers | quality | S-01 page 327 | C-39 |
| R-0493 | Engineers should compare polled, interrupt-driven and direct memory access I/O, and blocking and non-blocking I/O. | software engineers | quality | S-01 page 327 | C-39 |
| R-0494 | Software engineers need to understand processes, file systems, protection and security. | software engineers | quality | S-01 page 327 | C-39 |
| R-0495 | Engineers should be familiar with access control lists, the access matrix and access control verification. | software engineers | quality | S-01 page 327 | C-39 |
| R-0496 | Understanding logical addresses, partitions and free space management is important. | software engineers | quality | S-01 page 327 | C-39 |
| R-0497 | A network manager will need detailed knowledge of physical and logical time and synchronization protocols. | operations engineers | quality | S-01 page 328 | C-39 |
| R-0498 | Software engineers should understand hardware security, operational security, password protection, access control, security kernels and the layered approach. | software engineers | quality | S-01 page 328 | C-39 |
| R-0499 | When selecting a database, the software engineer should evaluate data models, storage models, database types and keys. | software engineers | quality | S-01 page 328 | C-38 |
| R-0500 | The learners and users of the database system need to create two roles, review case studies, and analyze the information. | software engineers | quality | S-01 page 328 | C-39 |
| R-0501 | Computer science engineers must understand the differences among types of RDBMS and be familiar with examples. | software engineers | quality | S-01 page 330 | C-39 |
| R-0502 | Database engineers are encouraged to understand normalization forms with examples and case studies. | software engineers | quality | S-01 page 330 | C-39 |
| R-0503 | Database engineers have to decide whether to use static or dynamic SQL, after weighing their pros and cons. | software engineers | quality | S-01 page 330 | C-39 |
| R-0504 | Database engineers should know the differences between simple and complex views and use them appropriately. | software engineers | quality | S-01 page 330 | C-39 |
| R-0505 | Database engineers must know data mining techniques and how to apply them. | software engineers | quality | S-01 page 331 | C-39 |
| R-0506 | Practitioners of computer science engineering have to study computer networks and communication concepts. | software engineers | quality | S-01 page 331 | C-39 |
| R-0507 | It is important for software engineers to understand the network topics listed in the knowledge area. | software engineers | quality | S-01 page 331 | C-39 |
| R-0508 | It is crucial to prevent data corruption and to recognize and recover from it immediately if it occurs. | software engineers | operations | S-01 page 331 | C-27 |
| R-0509 | Transactions must be updated carefully with commits at checkpoints, and must use techniques such as undo, deferred and immediate updates, caching and shadow paging. | software engineers | security | S-01 page 331 | C-44 |
| R-0510 | Databases must be backed up periodically to ensure data safety. | operations engineers | operations | S-01 page 331 | C-27 |
| R-0511 | It is important to understand each network type, with examples, benefits, limitations and solutions. | software engineers | quality | S-01 page 332 | C-39 |
| R-0512 | Software engineers are expected to understand the essential functions required, the data modes, and packet formation at peer levels. | software engineers | quality | S-01 page 332 | C-39 |
| R-0513 | Engineers must understand each OSI layer, its functions, and its inputs and outputs in both directions. | software engineers | quality | S-01 page 333 | C-39 |
| R-0514 | Engineers should analyze whether all seven OSI layers are needed for each protocol and what to optimize. | software engineers | quality | S-01 page 333 | C-39 |
| R-0515 | Software engineers practicing in networking need to understand the application services of the CASE and SASE types, with examples. | software engineers | quality | S-01 page 333 | C-39 |
| R-0516 | Engineers must understand the details of each layer, with examples. | software engineers | quality | S-01 page 333 | C-39 |
| R-0517 | Cross-layer optimization principles must be adhered to, and their applications must be learned. | software engineers | quality | S-01 page 333 | C-39 |
| R-0518 | Engineers should analyze the protocol data unit structures of each OSI layer, the Internet protocol suite and asynchronous transfer mode. | software engineers | quality | S-01 page 333 | C-39 |
| R-0519 | It is critical to identify network requirements, both business goals and technical solutions, with a roadmap for scalability. | software engineers | quality | S-01 page 333 | C-38 |
| R-0520 | The fundamental network design goals should include reliability, security, availability and manageability. | software engineers | quality | S-01 page 333 | C-33 |
| R-0521 | Engineers should expect threats and intrusions at multiple levels and design security at multiple levels. | software engineers | security | S-01 page 333 | C-12 |
| R-0522 | Systems must be set up to monitor networks for proper and improper functioning, and to find and fix faults, vulnerabilities and hacks quickly. | operations engineers | operations | S-01 page 333 | C-23 |
| R-0523 | Engineers must understand how to design networks with firewalls, VLANs, subnets, quality of service, DMZ, spanning tree, and physical and poll security. | operations engineers | security | S-01 page 333 | C-44 |
| R-0524 | One has to be constantly vigilant for attacks and continuously upgrade systems, devices and tools. | operations engineers | security | S-01 page 333 to 334 | C-18 |
| R-0525 | Professional network architects and programmers need to understand IPv6 addressing, routing, transition from IPv4, and NAT64. | software engineers | quality | S-01 page 334 | C-39 |
| R-0526 | It is important to know the differences among internet protocols and their use cases. | software engineers | quality | S-01 page 334 | C-39 |
| R-0527 | Software engineers are encouraged to learn the differences among 1G, 2G, 3G, 4G and 5G wireless technologies. | software engineers | quality | S-01 page 334 | C-39 |
| R-0528 | Many precautionary measures must be implemented and strictly followed to reduce wireless risks, including default and frequent password changes, access restriction, encryption and multiple firewall levels. | operations engineers | security | S-01 page 335 | C-44 |
| R-0529 | Users must protect and hide the wireless network identifier (SSID). | users and customers | security | S-01 page 335 | C-44 |
| R-0530 | Users must use effective antivirus software and update it regularly. | users and customers | security | S-01 page 335 | C-44 |
| R-0531 | Users must use VPNs, share files or systems with care, and disable access after use. | users and customers | security | S-01 page 335 | C-44 |
| R-0532 | Users must keep access points, controllers, gateways and other devices updated with security patches when they become available. | users and customers | security | S-01 page 335 | C-15 |
| R-0533 | The software engineer needs to identify user profiles, system functions, input and output interfaces, fault tolerance and performance parameters. | software engineers | quality | S-01 page 335 | C-33 |
| R-0534 | The interface should help users use the system easily. | users and customers | quality | S-01 page 335 | C-33 |
| R-0535 | The interface should be self-explanatory and enable self-learning. | users and customers | quality | S-01 page 335 | C-33 |
| R-0536 | Result and error messages should be clear and complete. | users and customers | quality | S-01 page 335 | C-33 |
| R-0537 | The system should be able to regain its original state after errors. | software engineers | quality | S-01 page 335 | C-33 |
| R-0538 | The system should let users interrupt processing and undo operations where possible. | users and customers | quality | S-01 page 335 | C-33 |
| R-0539 | User interface devices must be robust. | software engineers | quality | S-01 page 335 | C-33 |
| R-0540 | Code maintained by other engineers has to be written with more care and for use by other programmers. | software engineers | quality | S-01 page 335 | C-37 |
| R-0541 | Meaningful and comprehensive documentation is crucial at all stages of the software lifecycle. | software engineers | quality | S-01 page 335 | C-37 |
| R-0542 | Software engineers must define and adopt a suitable coding standard, and every team member must implement it. | software engineers | quality | S-01 page 335 | C-32 |
| R-0543 | Code must be legible and comprehensible, with meaningful, consistent and detailed comments. | software engineers | quality | S-01 page 335 | C-32 |
| R-0544 | Engineers should be aware of the limits of AI and ML, including uncertain and stochastic behaviour and the need for sufficiently labelled and structured datasets. | software engineers | quality | S-01 page 338 | C-39 |
| R-0545 | Software engineers working on AI are expected to know various other learning techniques and the key differences between them. | software engineers | quality | S-01 page 337 | C-39 |
| R-0546 | Software engineers are encouraged to learn other reasoning methods, such as metalevel, procedural numeric and formal reasoning. | software engineers | quality | S-01 page 337 | C-39 |
| R-0547 | Software engineers are encouraged to learn other AI models, such as Linear Discriminant Analysis, Learning Vector Quantization and K-nearest Neighbors. | software engineers | quality | S-01 page 338 | C-39 |
| R-0548 | There is a need for particular support of SE for AI, such as interdisciplinary teams of data scientists and software engineers, software evolution for changing datasets, and ethics and equity requirements engineering. | software engineers | quality | S-01 page 338 to 339 | C-40 |
| R-0549 | A software engineer must have a precise abstraction on complex, diverse application domains. | software engineers | quality | S-01 page 345 | C-39 |
| R-0550 | Logic and reasoning are the essence of the mathematics that a software engineer must address. | software engineers | quality | S-01 page 345 | C-39 |
| R-0551 | In the proof by induction, the step for the next greater integer must also hold. | software engineers | quality | S-01 page 348 | C-39 |
| R-0552 | If the contrapositive is shown true, the original implication must also be true. | software engineers | quality | S-01 page 348 | C-39 |
| R-0553 | When counting two tasks, one must subtract the number of ways to do both tasks. | software engineers | quality | S-01 page 360 | C-39 |
| R-0554 | A private key must be kept secret by a given party. | software engineers | security | S-01 page 360 | C-07 |
| R-0555 | A monoid must contain at least one element. | software engineers | quality | S-01 page 364 | C-39 |
| R-0556 | Engineering decisions must consider various factors, such as financial criteria. | software engineers | quality | S-01 page 367 | C-42 |
| R-0557 | Be sure to identify all relevant selection criteria. | software engineers | quality | S-01 page 367 | C-42 |
| R-0558 | It is essential to evaluate the selected alternative real-world performance and, if necessary and possible, decide whether another alternative might be better. | software engineers | quality | S-01 page 368 | C-42 |
| R-0559 | Engineers must understand how product and process characteristics vary. | software engineers | quality | S-01 page 371 | C-39 |
| R-0560 | Engineers must understand how to create an experiment and analyze the results to evaluate proposed solutions. | software engineers | quality | S-01 page 371 | C-39 |
| R-0561 | Engineers need to understand how to formulate clear hypotheses. | software engineers | quality | S-01 page 371 | C-39 |
| R-0562 | Engineers must understand statistical techniques for collecting and interpreting reliable data. | software engineers | quality | S-01 page 371 | C-39 |
| R-0563 | Samples must be drawn so that the draws are independent, and the rules of drawing must be predefined so that the probability of selecting a unit is known beforehand. | software engineers | quality | S-01 page 372 | C-39 |
| R-0564 | Care must be taken to differentiate the study population from the target population. | software engineers | quality | S-01 page 372 | C-39 |
| R-0565 | Prototype construction must have a clear purpose and must be planned, monitored and controlled. | software engineers | quality | S-01 page 375 | C-42 |
| R-0566 | Everyone involved in an engineering project must understand the measurement methods, the measurement results and how those results can and should be used. | software engineers | quality | S-01 page 376 | C-35 |
| R-0567 | Each step of a measurement must be understood, communicated and properly performed to yield usable data. | software engineers | quality | S-01 page 376 | C-35 |
| R-0568 | In software engineering, a combination of direct and derived measures is necessary. | software engineers | quality | S-01 page 376 | C-35 |
| R-0569 | Engineers must appreciate the need to define measurements from an operational perspective. | software engineers | quality | S-01 page 376 | C-35 |
| R-0570 | The measurement method must be well defined. | software engineers | quality | S-01 page 376 | C-35 |
| R-0571 | Future programming languages should enforce measurement theory and should not allow developers to manipulate measurements inappropriately. | software engineers | quality | S-01 page 379 | C-35 |
| R-0572 | Software engineers need to understand measurement theory and be on the lookout for inappropriate manipulations in code reviews. | software engineers | quality | S-01 page 379 | C-34 |
| R-0573 | Engineers must observe standards so that products, processes and materials are of acceptable quality. | software engineers | quality | S-01 page 381 | C-41 |
| R-0574 | Engineers are expected to be familiar with and use the appropriate standards for their specific discipline. | software engineers | quality | S-01 page 381 | C-41 |
| R-0575 | For a standard to be useful, conformance must add real or perceived value to the product, process or effort. | software engineers | quality | S-01 page 381 | C-41 |
| R-0576 | Some decision should be made as a result of a measurement. | software engineers | quality | S-01 page 381 | C-35 |
| R-0577 | Measurements that support no decision should be avoided. | software engineers | quality | S-01 page 381 | C-35 |
| R-0578 | Engineers must be aware of existing standards and keep abreast of changes to those standards over time. | software engineers | quality | S-01 page 382 | C-41 |
| R-0579 | The engineer must review all current standards related to a given endeavor and determine which must be met. | software engineers | quality | S-01 page 382 | C-41 |
| R-0580 | The design must incorporate all constraints imposed by the applicable standard. | software engineers | quality | S-01 page 382 | C-38 |
| R-0581 | More than one candidate corrective action should be considered. | software engineers | quality | S-01 page 383 | C-35 |
| R-0582 | Potential corrective actions should eliminate the cause, reduce the probability of the cause occurring or disconnect the cause from the effect. | software engineers | quality | S-01 page 383 | C-35 |
| R-0583 | Selected corrective actions should generate the greatest amount of control for the least cost. | software engineers | quality | S-01 page 383 | C-35 |
| R-0584 | Cause maps require evidence of the occurrence of causes and of the causality of effects. | software engineers | quality | S-01 page 383 | C-35 |
| R-0585 | KA editors must incorporate the common themes of measurement, quality and security into the breakdown of topics of each KA. | software engineers | quality | S-01 page 388 | C-37 |
| R-0586 | The breakdown of topics must decompose the generally recognized subset of the SWEBOK. | software engineers | quality | S-01 page 388 | C-37 |
| R-0587 | The breakdown of topics must not presume specific application domains, business needs, organization sizes or structures, management philosophies, life cycle models, technologies or methods. | software engineers | quality | S-01 page 388 | C-37 |
| R-0588 | The breakdown of topics must be as compatible as possible with the schools of thought within software engineering. | software engineers | quality | S-01 page 388 | C-37 |
| R-0589 | The breakdown of topics must be compatible with the breakdown of software engineering found in industry, literature and standards. | software engineers | quality | S-01 page 388 | C-37 |
| R-0590 | Topic names must be significant enough to be meaningful when cited outside the SWEBOK Guide. | software engineers | quality | S-01 page 388 | C-37 |
| R-0591 | The breakdown of topics should be at most two or three levels deep. | software engineers | quality | S-01 page 388 | C-37 |
| R-0592 | Emphasis should be put on the selection of the topics themselves rather than on their organization in a hierarchy. | software engineers | quality | S-01 page 388 | C-37 |
| R-0593 | Topic descriptions must not be prescriptive. | software engineers | quality | S-01 page 388 | C-37 |
| R-0594 | Topic descriptions must be sufficient for readers to select the reference material they need. | software engineers | quality | S-01 page 388 | C-37 |
| R-0595 | Change requests to the baseline must be approved by the SWEBOK Guide editors and by the KA editor team before implementation. | management | security | S-01 page 388 | C-02 |
| R-0596 | KA editors are instructed to refine the baseline breakdown of topics to reflect recent developments in the target area. | software engineers | quality | S-01 page 388 | C-37 |
| R-0597 | KA editors are instructed to use, as Recommended References, the references allocated to their KA by the Consolidated Reference List, to the level of section number. | software engineers | quality | S-01 page 388 | C-37 |
| R-0598 | The KA description will include a tree chart of the knowledge breakdown, typically as the first figure. | software engineers | quality | S-01 page 388 | C-37 |
| R-0599 | Reference material must be generally available, must not be confidential and must be in English. | software engineers | quality | S-01 page 389 | C-37 |
| R-0600 | The Consolidated Reference List should be complete, sufficient, consistent, credible, current and succinct. | software engineers | quality | S-01 page 389 | C-37 |
| R-0601 | Recommended reference material must be identified for each topic. | software engineers | quality | S-01 page 389 | C-37 |
| R-0602 | Each recommended reference should be as precise as possible, identifying the relevant chapter or section. | software engineers | quality | S-01 page 389 | C-37 |
| R-0603 | A matrix of reference material against topics must be provided. | software engineers | quality | S-01 page 389 | C-37 |
| R-0604 | The latest versions or editions should be used as Recommended References where several exist. | software engineers | quality | S-01 page 389 | C-37 |
| R-0605 | A reasonable amount of recommended reference material must be identified for each KA. | software engineers | quality | S-01 page 389 | C-37 |
| R-0606 | Further reading must be related to the topics of the breakdown and not to more advanced topics. | software engineers | quality | S-01 page 390 | C-37 |
| R-0607 | Each further reading item must be annotated, with one paragraph per reference explaining why it was included. | software engineers | quality | S-01 page 390 | C-37 |
| R-0608 | As a general guideline, a KA has ten or fewer further readings. | software engineers | quality | S-01 page 390 | C-37 |
| R-0609 | Additional reference material should be brought in by the KA editor only if it is necessary to the discussion. | software engineers | quality | S-01 page 390 | C-37 |
| R-0610 | A balance must be maintained between readability and technical excellence. | software engineers | quality | S-01 page 390 | C-37 |
| R-0611 | KA descriptions should use the common structure of acronyms, introduction, breakdown of topics with figure, matrix of topics against reference material, further reading and references. | software engineers | quality | S-01 page 390 | C-37 |
| R-0612 | KA descriptions are to be roughly 10 to 20 pages, excluding the reference materials themselves. | software engineers | quality | S-01 page 391 | C-37 |
| R-0613 | KA editors are expected to be forward-looking, taking into account what will be generally recognized in three to five years. | software engineers | quality | S-01 page 391 | C-37 |
| R-0614 | Authors should use explicit references to standards and not simply insert numbers that point to bibliography items. | software engineers | quality | S-01 page 392 | C-37 |
| R-0615 | Footnotes should be avoided and their content should be included in the main text. | software engineers | quality | S-01 page 392 | C-37 |
| R-0616 | Tools and products should not be named directly; their functions should be named instead. | software engineers | quality | S-01 page 392 | C-37 |
| R-0617 | Text that accompanies figures and tables should be self-explanatory or contain enough related text. | software engineers | quality | S-01 page 392 | C-37 |
| R-0618 | KA editors must sign a copyright release form. | software engineers | quality | S-01 page 392 | C-41 |
| R-0619 | When software is the predominant system or element of interest, ISO/IEC/IEEE 12207 should be used. | management | quality | S-01 page 396 | C-42 |
| R-0620 | The ethical values standard requires consideration of the values relevant to the culture where the system is to be deployed. | software engineers | quality | S-01 page 400 | C-39 |
| R-0621 | Users of standards should look for the most recent version and for newer titles on emerging topics. | software engineers | quality | S-01 page 403 | C-37 |
| R-0622 | At Build L1, the producer follows a consistent build process so that others can form expectations of a correct build. | software engineers | security | S-02 page 1 | C-03 |
| R-0623 | At Build L1, the producer runs builds on a build platform that meets Build L1 requirements. | software engineers | security | S-02 page 1 | C-03 |
| R-0624 | At Build L1, the producer distributes provenance to consumers, preferably by a convention of the package ecosystem. | software engineers | security | S-02 page 1 | C-04 |
| R-0625 | At Build L1, the build platform automatically generates provenance that describes the builder, the build process and the top-level build inputs. | suppliers | security | S-02 page 1 | C-04 |
| R-0626 | At Build L2, the producer runs builds on a hosted build platform that meets Build L2 requirements. | software engineers | security | S-02 page 1 | C-03 |
| R-0627 | At Build L2, the build platform generates and signs the provenance itself, or by an equivalent system that keeps the provenance trustworthy. | suppliers | security | S-02 page 1 | C-04 |
| R-0628 | At Build L2, the consumer validates the authenticity of the provenance. | users and customers | security | S-02 page 1 | C-16 |
| R-0629 | At Build L3, the producer runs builds on a hosted build platform that meets Build L3 requirements. | software engineers | security | S-02 page 2 | C-03 |
| R-0630 | At Build L3, the build platform implements strong controls to prevent runs from influencing one another, even within the same project. | suppliers | security | S-02 page 2 | C-05 |
| R-0631 | At Build L3, the build platform implements strong controls to keep the provenance signing secret from user-defined build steps. | suppliers | security | S-02 page 2 | C-05 |
| R-0632 | At all levels, implementations MUST use industry security best practices, including access control, secured communications, secret management, frequent updates and prompt fixes of known vulnerabilities. | suppliers | security | S-02 page 2 | C-18 |
| R-0633 | At all levels, the build platform MUST strengthen its security controls to reach the specific build level. | suppliers | security | S-02 page 2 | C-05 |
| R-0634 | At all levels, the producer MUST choose and adopt a build platform that can reach the desired build level. | software engineers | security | S-02 page 2 | C-03 |
| R-0635 | At all levels, the producer MUST build the artifact in a consistent manner so that verifiers can form expectations of the build process. | software engineers | security | S-02 page 2 | C-03 |
| R-0636 | At all levels, in some implementations the producer MAY give explicit build-process metadata to a verifier. | software engineers | security | S-02 page 2 | C-04 |
| R-0637 | At all levels, the producer MUST complete the build configuration file that the package ecosystem requires, and keep it up to date. | software engineers | security | S-02 page 3 | C-03 |
| R-0638 | At all levels, the producer MUST distribute provenance to consumers. | software engineers | security | S-02 page 3 | C-04 |
| R-0639 | At all levels, the producer MAY delegate provenance distribution to the package ecosystem, if the ecosystem can distribute provenance. | software engineers | security | S-02 page 3 | C-04 |
| R-0640 | At all levels, the build process MUST generate provenance that identifies the output package by cryptographic digest and describes how the package was produced. | suppliers | security | S-02 page 3 | C-04 |
| R-0641 | At all levels, the provenance format MUST be acceptable to the package ecosystem or the consumer. | suppliers | security | S-02 page 3 | C-04 |
| R-0642 | At all levels, the SLSA Provenance format is RECOMMENDED. | suppliers | security | S-02 page 3 | C-04 |
| R-0643 | At all levels, an alternate provenance format MUST contain information equivalent to SLSA Provenance at each level. | suppliers | security | S-02 page 3 | C-04 |
| R-0644 | At all levels, an alternate provenance format SHOULD be bi-directionally translatable to SLSA Provenance. | suppliers | security | S-02 page 3 | C-04 |
| R-0645 | At Build L1, the provenance SHOULD contain enough information to catch mistakes, and a few fields MAY be absent if they are prohibitively expensive. | suppliers | security | S-02 page 3 | C-04 |
| R-0646 | At Build L2, consumers MUST be able to validate the authenticity of the provenance attestation, to ensure integrity and to define trust. | users and customers | security | S-02 page 3 | C-16 |
| R-0647 | At Build L2 and L3, the provenance SHOULD be signed by a digital signature from a private key that only the build platform component that made the attestation can access. | suppliers | security | S-02 page 3 | C-04 |
| R-0648 | At Build L2 and L3, build platforms are RECOMMENDED to use signing methods that help detect and remediate key compromise, such as transparency logs or time stamping. | suppliers | security | S-02 page 3 | C-04 |
| R-0649 | At Build L2 and L3, the provenance MUST be generated by the control plane and not by a tenant of the build platform, except as noted. | suppliers | security | S-02 page 3 | C-05 |
| R-0650 | At Build L2 and L3, the data in the provenance MUST be obtained from the build platform. | suppliers | security | S-02 page 3 | C-04 |
| R-0651 | At Build L2 and L3, the build platform MUST have some security control to stop tenants from tampering with the provenance. No minimum strength is set. | suppliers | security | S-02 page 3 | C-05 |
| R-0652 | At Build L2, builders SHOULD document each field that a tenant generates. | suppliers | security | S-02 page 3 | C-04 |
| R-0653 | At Build L2, the provenance SHOULD be complete. | suppliers | security | S-02 page 3 | C-04 |
| R-0654 | At Build L2, there MAY be external parameters that the provenance does not capture sufficiently. | suppliers | security | S-02 page 3 | C-04 |
| R-0655 | At Build L3, the provenance MUST be strongly resistant to forgery by tenants. | suppliers | security | S-02 page 3 | C-05 |
| R-0656 | At Build L3, secret material for authenticating the provenance MUST be stored in a secure management system that only the build service account can access. | suppliers | security | S-02 page 3 | C-05 |
| R-0657 | At Build L3, that secret material MUST NOT be accessible to the environment that runs user-defined build steps. | suppliers | security | S-02 page 3 | C-05 |
| R-0658 | At Build L3, every provenance field MUST be generated or verified by the build platform in a trusted control plane, and user-controlled build steps MUST NOT inject or alter the contents, except as noted. | suppliers | security | S-02 page 3 | C-05 |
| R-0659 | At Build L3, the provenance SHOULD be complete. | suppliers | security | S-02 page 3 | C-04 |
| R-0660 | At Build L3, the external parameters MUST be fully enumerated. | suppliers | security | S-02 page 3 | C-04 |
| R-0661 | At Build L2 and L3, all build steps run on a hosted build platform, on shared or dedicated infrastructure, not on an individual workstation. | suppliers | security | S-02 page 3 | C-03 |
| R-0662 | At Build L3, the build platform MUST ensure that build steps run in an isolated environment, free of unintended external influence, and this MUST hold between builds in the same tenant project. | suppliers | security | S-02 page 3 | C-05 |
| R-0663 | At Build L3, the build platform MUST NOT let a build access any secrets of the build platform, such as the provenance signing key. | suppliers | security | S-02 page 3 | C-05 |
| R-0664 | At Build L3, the build platform MUST NOT let two overlapping builds influence one another. | suppliers | security | S-02 page 4 | C-05 |
| R-0665 | At Build L3, the build platform MUST NOT let one build persist or influence the environment of a later build, and an ephemeral build environment MUST be provisioned for each build. | suppliers | security | S-02 page 4 | C-05 |
| R-0666 | At Build L3, the build platform MUST NOT allow cache poisoning, and build output MUST be identical whether or not a cache is used. | suppliers | security | S-02 page 4 | C-05 |
| R-0667 | At Build L3, the build platform MUST NOT open services that allow remote influence, unless all such interactions are captured as external parameters in the provenance. | suppliers | security | S-02 page 4 | C-05 |
| R-0668 | Untrusted persons MAY read the source and MAY propose or review changes. They MAY NOT approve changes or perform privileged actions. | software engineers | security | S-02 page 4 | C-08 |
| R-0669 | At every Source level, an organization producing source revisions MUST select a source control system that can reach its desired source level. | management | security | S-02 page 5 | C-01 |
| R-0670 | From Source L2 upward, the organization MUST configure access controls to restrict sensitive operations on the source repository, using the identity management of the source control system. | management | security | S-02 page 5 | C-08 |
| R-0671 | From Source L2 upward, the source control system MUST be configured to produce a reliable change history; if it does not do so by design, the organization MUST provide evidence of continuous enforcement. | management | security | S-02 page 5 | C-01 |
| R-0672 | If the source control system supports tags, it MUST be configured to prevent tags from being moved or deleted. | management | security | S-02 page 5 | C-01 |
| R-0673 | Source control systems MAY allow the organization to expunge content from a repository and its change history without a public record. | suppliers | security | S-02 page 5 | C-01 |
| R-0674 | The organization MUST allow expunging only to meet legal or privacy compliance requirements. | management | quality | S-02 page 5 | C-41 |
| R-0675 | The organization MUST document the safe expunging process and describe how requests and actions are tracked, and SHOULD log that content was removed. | management | security | S-02 page 5 | C-01 |
| R-0676 | Source control systems SHOULD have technical mechanisms that require an Administrator plus at least one more trusted person to trigger any expunging. | suppliers | security | S-02 page 5 | C-08 |
| R-0677 | At Source L1, the source is stored and managed through a modern version control system. | software engineers | security | S-02 page 5 | C-01 |
| R-0678 | At Source L2, branch history is continuous, immutable and retained, and the source control system issues Source Provenance Attestations for each new source revision. | suppliers | security | S-02 page 5 | C-01 |
| R-0679 | At Source L3, the source control system is configured to enforce the organization's technical controls for specific named references. | suppliers | security | S-02 page 5 | C-01 |
| R-0680 | At Source L4, the source control system requires two trusted persons to review all changes to protected branches. | suppliers | security | S-02 page 5 | C-02 |
| R-0681 | Organization MAY keep Safe Expunging logs private, and SHOULD make them public where possible (levels: three marks, columns not shown) | management | security | S-02 page 6 | C-01 |
| R-0682 | Organization MUST give evidence of continuous enforcement of technical controls for each claim in Source Provenance attestations or VSAs (levels: two marks, columns not shown) | management | security | S-02 page 6 | C-01 |
| R-0683 | Organization MUST document the meaning of each enforced technical control | management | security | S-02 page 6 | C-01 |
| R-0684 | For a control built as a custom tool, organization MUST name the tool, state what it does, and show where its evidence is in the provenance attestation (example of the item above) | management | security | S-02 page 6 | C-01 |
| R-0685 | If organization claims that consumable revisions were tested before acceptance, this MUST be enforced explicitly in the SCS (example) | management | quality | S-02 page 6 | C-30 |
| R-0686 | SCS MUST make each repository ID unique within the SCS, with a stable locator (levels L1 to L4) | suppliers | security | S-02 page 6 | C-01 |
| R-0687 | SCS MUST make each revision ID unique within its repository (levels L1 to L4) | suppliers | security | S-02 page 6 | C-01 |
| R-0688 | If the revision ID is not a digest, SCS MUST document how revision immutability is established (levels L1 to L4) | suppliers | security | S-02 page 6 | C-01 |
| R-0689 | SCS MUST provide tooling that displays changes between revisions in human-readable form for all plain-text changes (levels L1 to L4) | suppliers | security | S-02 page 6 | C-02 |
| R-0690 | SCS SHOULD provide ways to show human-understandable interpretations of non-plain-text changes (levels L1 to L4) | suppliers | security | S-02 page 6 | C-02 |
| R-0691 | SCS MUST generate a Source VSA for any revision at Level 1 or above (levels L1 to L4) | suppliers | security | S-02 page 6 | C-04 |
| R-0692 | A consumer authorized to access a revision MUST be able to fetch its Source VSA (levels L1 to L4) | users and customers | security | S-02 page 6 | C-16 |
| R-0693 | At Levels 1 and 2, SCS MAY issue VSAs based on its understanding of the system, and at Level 2 and above SCS MUST use its own source provenance for VSAs (levels L1 to L4) | suppliers | security | S-02 page 6 | C-04 |
| R-0694 | SCS MUST record all changes to named references, including when, by whom, and the new revision ID (levels L1 to L3) | suppliers | security | S-02 page 6 | C-01 |
| R-0695 | If revisions have ancestry, SCS MUST allow a branch to move only to a descendant of its current revision (levels L1 to L3) | suppliers | security | S-02 page 6 | C-01 |
| R-0696 | For each technical control claimed in a VSA, continuity MUST be established and tracked from a start revision (levels L1 to L3) | suppliers | security | S-02 page 6 | C-01 |
| R-0697 | If continuity of a control lapses, continuity MUST be re-established from a new revision (levels L1 to L3) | suppliers | security | S-02 page 6 | C-01 |
| R-0698 | SCS MUST provide an identity management system, or another means, to identify and authenticate actors (levels L1 to L3) | suppliers | security | S-02 page 6 | C-08 |
| R-0699 | SCS MUST allow organizations to specify which actors and roles may perform sensitive actions in a repository (levels L1 to L3) | suppliers | security | S-02 page 6 | C-08 |
| R-0700 | SCS MUST document how actors are identified for attribution (levels L1 to L3) | suppliers | security | S-02 page 6 | C-01 |
| R-0701 | Activities on the SCS SHOULD be attributed to authenticated identities (levels L1 to L3) | suppliers | security | S-02 page 6 | C-01 |
| R-0702 | SCS MUST document the format and intent of all Source Provenance attestations it produces (levels L1 to L3) | suppliers | security | S-02 page 6 | C-04 |
| R-0703 | Source Provenance MUST be created at the same time as the branch update (levels L1 to L3) | suppliers | security | S-02 page 6 | C-04 |
| R-0704 | A consumer authorized to access a revision MUST be able to access its Source Provenance documents (levels L1 to L3) | users and customers | security | S-02 page 6 | C-16 |
| R-0705 | SCS MUST let an organization enforce customized technical controls on named references (levels L1 and L2) | suppliers | security | S-02 pages 6 to 7 | C-01 |
| R-0706 | SCS MUST provide a mechanism for organizations to indicate which named references are protected (levels L1 and L2) | suppliers | security | S-02 page 6 | C-01 |
| R-0707 | SCS MUST record technical controls enforced on named references in attestations made at the time of the revision (levels L1 and L2) | suppliers | security | S-02 page 7 | C-04 |
| R-0708 | SCS MUST let organizations add their own properties to the Source VSA when the corresponding controls are enforced (levels L1 and L2) | suppliers | security | S-02 page 7 | C-04 |
| R-0709 | SCS MUST let organizations send extra control attestations to consumers authorized to access the revision (levels L1 and L2) | suppliers | security | S-02 page 7 | C-04 |
| R-0710 | SCS MUST prevent organization-specified properties from starting with any prefix other than ORG_SOURCE_ (levels L1 and L2) | suppliers | security | S-02 page 7 | C-04 |
| R-0711 | Changes in protected branches MUST be agreed to by two or more trusted persons before submission (level: one mark, column not shown) | software engineers | security | S-02 page 7 | C-02 |
| R-0712 | The two parties MUST be different trusted persons, as uploader and reviewer, or as two different reviewers | software engineers | security | S-02 page 7 | C-02 |
| R-0713 | Reviews SHOULD cover at least the security-relevant properties of the code | quality assurance | security | S-02 page 7 | C-02 |
| R-0714 | Changes made during review MUST be reviewed as well, because approval applies to the final revision | quality assurance | security | S-02 page 7 | C-02 |
| R-0715 | Approval is for a specific context, and moving approved content to another context still requires review | quality assurance | security | S-02 page 7 | C-02 |
| R-0716 | SCS MUST present reviewers with a clear representation of the result of accepting the proposed change | suppliers | security | S-02 page 7 | C-02 |
| R-0717 | Organization MAY give a Trusted Robot a perpetual exception to a policy | management | security | S-02 page 7 | C-02 |
| R-0718 | Source VSA subject.uri SHOULD be set to a URI where a human can find details about the revision | suppliers | security | S-02 page 7 | C-04 |
| R-0719 | Source VSA subject.digest MUST include the revision identifier and MAY include other digests of the revision | suppliers | security | S-02 page 7 | C-04 |
| R-0720 | An SCS without cryptographic digests MUST define a canonical type for immutable revisions and MUST include the repository in that type | suppliers | security | S-02 page 7 | C-04 |
| R-0721 | Source VSA subject.annotations.sourceRefs SHOULD list the references that pointed to the revision, and the list MAY be non-exhaustive | suppliers | security | S-02 page 7 | C-04 |
| R-0722 | Git references in sourceRefs MUST be fully qualified | suppliers | security | S-02 page 7 | C-04 |
| R-0723 | Source VSA resourceUri MUST be set to the repository URI | suppliers | security | S-02 page 7 | C-04 |
| R-0724 | Source VSA verifiedLevels MUST include the SLSA source level that the SCS asserts, and MUST include only the highest level met | suppliers | security | S-02 page 7 | C-04 |
| R-0725 | Source VSA verifiedLevels MAY include additional properties asserted by the SCS | suppliers | security | S-02 page 7 | C-04 |
| R-0726 | Source VSA dependencyLevels MAY be empty | suppliers | security | S-02 page 7 | C-04 |
| R-0727 | Organization MAY mark properties with ORG_SOURCE_ for external consumers, or ORG_SOURCE_INTERNAL_ for internal use | management | security | S-02 page 7 | C-04 |
| R-0728 | Source VSA issuer MAY choose how to populate sourceRefs | suppliers | security | S-02 page 7 | C-04 |
| R-0729 | The authority that issues Source VSAs MUST know which entity should issue each provenance attestation type, and MUST ensure that all come from their expected issuers | suppliers | security | S-02 page 8 | C-04 |
| R-0730 | SCS MUST document each provenance format, and how each attestation supports reasoning about the revision properties | suppliers | security | S-02 page 8 | C-04 |
| R-0731 | Verification SHOULD include the following steps: check builder identity, verify signature, and match buildType and externalParameters | users and customers | security | S-02 page 8 | C-16 |
| R-0732 | Verifier SHOULD check that the builder identity is in its map of trusted builder IDs to SLSA Build level | users and customers | security | S-02 page 8 | C-16 |
| R-0733 | Verifier SHOULD verify the signature on the provenance envelope | users and customers | security | S-02 page 8 | C-16 |
| R-0734 | Verifier SHOULD ensure that buildType and externalParameters match the expected values | users and customers | security | S-02 page 8 | C-16 |
| R-0735 | A package ecosystem MAY allow an approved list of externalParameters to be ignored during verification | suppliers | security | S-02 page 8 | C-16 |
| R-0736 | Verifier SHOULD cause verification to fail on any unrecognized externalParameters | users and customers | security | S-02 page 8 | C-16 |
| R-0737 | If provenance is not in the recommended format, verifier SHOULD perform equivalent checks on the corresponding fields | users and customers | security | S-02 page 8 | C-16 |
| R-0738 | When bootstrapping, the verifier configures its roots of trust: recognized builder identities and the maximum SLSA Build level for each (no modal verb in source) | users and customers | security | S-02 page 8 | C-16 |
| R-0739 | Verifier verifies the envelope signature with the roots of trust and obtains the recognized public keys (no modal verb in source) | users and customers | security | S-02 page 9 | C-16 |
| R-0740 | Verifier verifies that the statement subject matches the artifact digest (no modal verb in source) | users and customers | security | S-02 page 9 | C-16 |
| R-0741 | Verifier verifies that the predicateType is https://slsa.dev/provenance/v1 (no modal verb in source) | users and customers | security | S-02 page 9 | C-16 |
| R-0742 | Verifier looks up the SLSA Build Level in the roots of trust, defaulting to SLSA Build L1 (no modal verb in source) | users and customers | security | S-02 page 9 | C-16 |
| R-0743 | SLSA Build L3 requires protection against compromise of the build process and provenance generation by an external adversary (level L3) | suppliers | security | S-02 page 9 | C-05 |
| R-0744 | Verifiers SHOULD carefully consider which build platforms are added to the roots of trust | users and customers | security | S-02 page 9 | C-16 |
| R-0745 | Verifier checks that the package provenance meets its expectations (no modal verb in source) | users and customers | security | S-02 page 9 | C-16 |
| R-0746 | Expectations SHOULD be sufficient to detect or prevent an adversary who can invoke builds and publish, but cannot write to the source repository | users and customers | security | S-02 page 9 | C-16 |
| R-0747 | Verifier SHOULD compare provenance against expected values for at least builder identity, canonical source repository, buildType and externalParameters | users and customers | security | S-02 page 9 | C-16 |
| R-0748 | Verification tools SHOULD reject unrecognized fields in externalParameters | users and customers | security | S-02 page 9 | C-16 |
| R-0749 | Step 3 is optional: verifier recursively checks resolvedDependencies as available and to the extent desired (no modal verb in source) | users and customers | security | S-02 page 9 | C-16 |
| R-0750 | For producer-defined expectations, the verifier SHOULD provide an authenticated communication mechanism for the producer | users and customers | security | S-02 page 9 | C-16 |
| R-0751 | For producer-defined expectations, there SHOULD be protection against an adversary who changes them unilaterally | users and customers | security | S-02 page 9 | C-16 |
| R-0752 | At least one provenance verification option (package ecosystem upload, consumer download, or monitor) SHOULD be used | users and customers | security | S-02 page 10 | C-16 |
| R-0753 | Package ecosystem upload-time verification is RECOMMENDED whenever possible | suppliers | security | S-02 page 10 | C-16 |
| R-0754 | Package ecosystem is responsible for making its expectations available, reliably redistributing artifacts and provenance, and providing tools for safe consumption (no modal verb in source) | suppliers | security | S-02 page 10 | C-16 |
| R-0755 | Consumer uses client-side verification to ensure the provenance matches its expectations before use (no modal verb in source) | users and customers | security | S-02 page 10 | C-16 |
| R-0756 | Monitor MAY verify provenance for a set of packages, and that set MAY mimic the set published through one or more ecosystems | users and customers | security | S-02 page 10 | C-16 |
| R-0757 | Monitor SHOULD publish its expectations for all the packages it verifies | users and customers | security | S-02 page 10 | C-16 |
| R-0758 | Organizations should integrate the SSDF throughout their existing software development practices | management | quality | S-03 page 8 | C-40 |
| R-0759 | Organizations should express their secure software development requirements to third-party suppliers using SSDF conventions | management | security | S-03 page 8 | C-19 |
| R-0760 | Organizations should acquire software that meets the practices described in the SSDF | management | security | S-03 page 8 | C-19 |
| R-0761 | Organizations should ensure that their people, processes, and technology are prepared to perform secure software development | management | quality | S-03 page 8 | C-40 |
| R-0762 | Organizations should protect all components of their software from tampering and unauthorized access | management | security | S-03 page 8 | C-18 |
| R-0763 | Organizations should produce well-secured software with minimal security vulnerabilities in its releases | management | security | S-03 page 8 | C-13 |
| R-0764 | Organizations should identify residual vulnerabilities in their releases and respond to them to prevent similar ones | management | security | S-03 page 8 | C-14 |
| R-0765 | Organizations should adopt a risk-based approach to decide which practices are relevant and effective | management | quality | S-03 page 8 | C-40 |
| R-0766 | Secure software development practices should be integrated throughout any SDLC model | management | quality | S-03 page 10 | C-40 |
| R-0767 | The SSDF should not negatively affect organizations that already have robust secure development practices | management | quality | S-03 page 11 | C-37 |
| R-0768 | Expertise in secure software development is required to implement the recommended practices | management | quality | S-03 page 5 | C-39 |
| R-0769 | The aim is that each software producer follows all applicable practices | management | quality | S-03 page 12 | C-40 |
| R-0770 | The tenant organization should agree with its providers which party is responsible for each practice and task | management | security | S-03 page 12 | C-19 |
| R-0771 | The tenant organization should require each provider to attest its conformance with the agreement | management | security | S-03 page 12 | C-19 |
| R-0772 | Factors such as risk, cost, feasibility, and applicability should be considered when choosing practices | management | quality | S-03 page 12 | C-42 |
| R-0773 | Organizations adopting the SSDF should define the undefined terms, such as sensitive data and qualified person, for their own environments | management | quality | S-03 page 13 | C-37 |
| R-0774 | Enumerating the environments is necessary to secure them and to prevent lateral movement between them | operations engineers | security | S-03 page 13 | C-18 |
| R-0775 | Identify and document all security requirements for software development, and maintain them over time | software engineers | security | S-03 page 14 | C-12 |
| R-0776 | Identify and document security requirements for organization-developed software, and maintain them over time | software engineers | security | S-03 page 14 | C-12 |
| R-0777 | Communicate security requirements to all third parties that provide commercial components reused by the organization | management | security | S-03 page 14 | C-19 |
| R-0778 | Create or alter roles and responsibilities to cover all parts of the SDLC, and review them periodically | management | quality | S-03 page 15 | C-40 |
| R-0779 | Provide role-based training for all personnel with responsibilities that contribute to secure development, and review it periodically | software engineers | quality | S-03 page 15 | C-39 |
| R-0780 | Obtain the official commitment of upper management or authorizing officials to secure development, and convey it to all with development roles | management | quality | S-03 page 16 | C-40 |
| R-0781 | Specify which tools or tool types must or should be included in each toolchain, and how they are integrated | operations engineers | security | S-03 page 16 | C-18 |
| R-0782 | Follow recommended security practices to deploy, operate, and maintain tools and toolchains | operations engineers | security | S-03 page 16 | C-18 |
| R-0783 | Configure tools to generate the artifacts that the organization defines for secure development | operations engineers | security | S-03 page 16 | C-18 |
| R-0784 | Define criteria for software security checks, and track them throughout the SDLC | security team | security | S-03 page 17 | C-11 |
| R-0785 | Implement processes and mechanisms to gather and protect the information needed for the criteria | security team | security | S-03 page 17 | C-11 |
| R-0786 | Separate and protect each environment involved in software development | operations engineers | operations | S-03 page 17 | C-22 |
| R-0787 | Secure and harden development endpoints using a risk-based approach | operations engineers | security | S-03 page 18 | C-18 |
| R-0788 | Store all forms of code in a protected manner, and restrict access based on least privilege | operations engineers | security | S-03 page 18 | C-08 |
| R-0789 | Make software integrity verification information available to software acquirers | users and customers | security | S-03 page 19 | C-16 |
| R-0790 | Securely archive the necessary files and supporting data for each software release | software engineers | operations | S-03 page 19 | C-45 |
| R-0791 | Collect, protect, maintain, and share provenance data for all components of each release | software engineers | security | S-03 page 19 | C-04 |
| R-0792 | Use forms of risk modeling to assess the security risk of the software and decide how the design mitigates it | security team | security | S-03 page 20 | C-12 |
| R-0793 | Justify any case where security requirements are relaxed or waived based on risk analysis | management | security | S-03 page 20 | C-12 |
| R-0794 | Track and maintain security requirements, risks, and design decisions, including approved exceptions | software engineers | quality | S-03 page 20 | C-38 |
| R-0795 | Where appropriate, build in support for standardized security features and services instead of proprietary ones | software engineers | security | S-03 page 20 | C-13 |
| R-0796 | Have a qualified person who was not involved in the design, or automated toolchain processes, review the design for security compliance | quality assurance | quality | S-03 page 21 | C-34 |
| R-0797 | Acquire and maintain well-secured reusable components from commercial, open-source, and other third-party sources | software engineers | security | S-03 page 21 | C-10 |
| R-0798 | Create and maintain well-secured in-house components that meet common internal needs | software engineers | security | S-03 page 21 | C-13 |
| R-0799 | Verify that acquired third-party components comply with the organization's requirements throughout their life cycles | software engineers | security | S-03 page 22 | C-10 |
| R-0800 | Follow all secure coding practices appropriate to the development languages and environment | software engineers | security | S-03 page 22 | C-13 |
| R-0801 | Use compiler, interpreter, and build tools that offer features that improve executable security | software engineers | security | S-03 page 23 | C-13 |
| R-0802 | Determine which tool features should be used, configure them, and use the approved configurations | software engineers | security | S-03 page 23 | C-13 |
| R-0803 | Determine whether code review or code analysis should be performed on human-readable code, and how | software engineers | security | S-03 page 23 | C-11 |
| R-0804 | Perform code review or code analysis based on secure coding standards, and record and triage all issues | software engineers | security | S-03 page 23 | C-11 |
| R-0805 | Determine whether executable code testing should be performed to find vulnerabilities not found earlier | security team | security | S-03 page 24 | C-17 |
| R-0806 | Scope, design, perform, and document testing, and record and triage all issues | security team | security | S-03 page 24 | C-17 |
| R-0807 | Define a secure baseline by determining how each security-relevant setting is configured so defaults are secure | software engineers | security | S-03 page 25 | C-13 |
| R-0808 | Implement the default settings, and document each setting for software administrators | software engineers | security | S-03 page 25 | C-13 |
| R-0809 | Gather information on potential vulnerabilities from acquirers, users, and public sources, and investigate all credible reports | security team | security | S-03 page 25 | C-14 |
| R-0810 | Review, analyze, or test the software code to identify or confirm undetected vulnerabilities | security team | security | S-03 page 25 | C-11 |
| R-0811 | Have a policy that addresses vulnerability disclosure and remediation, and implement the roles, responsibilities and processes that support it. | security team | security | S-03 page 26, RV.1.3 task | C-14 |
| R-0812 | Notional Example 1: establish a vulnerability disclosure program and make it easy for security researchers to learn about it and report possible vulnerabilities. | security team | security | S-03 page 26, RV.1.3 Example 1 | C-14 |
| R-0813 | Notional Example 2: have a PSIRT and processes to handle responses to vulnerability reports and incidents, including communications plans for all stakeholders. | security team | operations | S-03 page 26, RV.1.3 Example 2 | C-25 |
| R-0814 | Notional Example 3: have a security response playbook for a generic reported vulnerability, zero-day reports, exploitation in the wild, and a major ongoing multi-party incident involving open-source components. | security team | operations | S-03 page 26, RV.1.3 Example 3 | C-25 |
| R-0815 | Notional Example 4: periodically conduct exercises of the product security incident response processes. | security team | operations | S-03 page 26, RV.1.3 Example 4 | C-25 |
| R-0816 | Analyze each vulnerability to gather enough risk information to plan its remediation or other risk response, to reduce the window of opportunity for attackers. | security team | security | S-03 page 26, RV.2.1 task | C-14 |
| R-0817 | Notional Example 1: use existing issue tracking software to record each vulnerability. | security team | security | S-03 page 26, RV.2.1 Example 1 | C-14 |
| R-0818 | Notional Example 2: perform risk calculations for each vulnerability based on exploitability, potential impact and other relevant characteristics. | security team | security | S-03 page 26, RV.2.1 Example 2 | C-14 |
| R-0819 | Plan and implement risk responses for vulnerabilities. | security team | security | S-03 page 27, RV.2.2 task | C-14 |
| R-0820 | Notional Example 1: make a risk-based decision whether each vulnerability is remediated or addressed by other means, such as risk acceptance or transference, and prioritize the actions. | security team | security | S-03 page 27, RV.2.2 Example 1 | C-14 |
| R-0821 | Notional Example 2: if no permanent mitigation exists, determine a temporary mitigation and add it to the plan. | security team | security | S-03 page 27, RV.2.2 Example 2 | C-14 |
| R-0822 | Notional Example 3: develop and release security advisories that give software acquirers the information needed to find and address the vulnerabilities, including patch sources, changed settings and temporary workarounds. | security team | security | S-03 page 27, RV.2.2 Example 3 | C-14 |
| R-0823 | Notional Example 4: deliver remediations to acquirers by an automated and trusted delivery mechanism; one remediation may address several vulnerabilities. | users and customers | security | S-03 page 27, RV.2.2 Example 4 | C-15 |
| R-0824 | Notional Example 5: update records of design decisions, risk responses and approved exceptions as needed. | security team | quality | S-03 page 27, RV.2.2 Example 5 | C-38 |
| R-0825 | Analyze identified vulnerabilities to determine their root causes. | security team | security | S-03 page 27, RV.3.1 task | C-14 |
| R-0826 | Notional Example 1: record the root cause of discovered issues. | security team | security | S-03 page 27, RV.3.1 Example 1 | C-14 |
| R-0827 | Notional Example 2: record lessons learned from root cause analysis in a wiki that developers can access and search. | software engineers | quality | S-03 page 27, RV.3.1 Example 2 | C-35 |
| R-0828 | Analyze root causes over time to identify patterns, such as a secure coding practice not followed consistently. | security team | quality | S-03 page 27, RV.3.2 task | C-35 |
| R-0829 | Notional Example 1: record lessons learned from root cause analysis in a wiki that developers can access and search. | software engineers | quality | S-03 page 27, RV.3.2 Example 1 | C-35 |
| R-0830 | Notional Example 2: add mechanisms to the toolchain that detect future instances of the root cause automatically. | security team | security | S-03 page 27, RV.3.2 Example 2 | C-11 |
| R-0831 | Notional Example 3: update manual processes to detect future instances of the root cause. | security team | quality | S-03 page 27, RV.3.2 Example 3 | C-35 |
| R-0832 | Review the software for similar vulnerabilities to remove a class of vulnerabilities, and fix them proactively rather than waiting for external reports. | security team | security | S-03 page 27, RV.3.3 task | C-14 |
| R-0833 | Notional Example 1 is a cross-reference: see PW.7 and PW.8 for the related review tasks. | security team | security | S-03 page 27, RV.3.3 Example 1 | C-11 |
| R-0834 | Review the SDLC process, and update it if appropriate, to prevent or reduce the likelihood that the root cause recurs in updates or new software. | software engineers | quality | S-03 page 27, RV.3.4 task | C-35 |
| R-0835 | Notional Example 1: record lessons learned from root cause analysis in a wiki that developers can access and search. | software engineers | quality | S-03 page 27, RV.3.4 Example 1 | C-35 |
| R-0836 | Notional Example 2: plan and implement changes to the appropriate SDLC practices. | software engineers | quality | S-03 page 27, RV.3.4 Example 2 | C-35 |
| R-0837 | SSC security assurance measures must be integrated into CI/CD pipelines | software engineers | security | S-04 page 11 | C-11 |
| R-0838 | The software bill of materials must be shared with end users so that they can build inventories of software components | users and customers | security | S-04 page 13 | C-09 |
| R-0839 | Developer workstations should not be trusted as part of the build process | software engineers | security | S-04 page 17 | C-03 |
| R-0840 | Companies should be aware of threat actor risks and take appropriate measures to secure their software supply chain | management | security | S-04 page 17 | C-12 |
| R-0841 | Organizations should be aware of insecure secrets handling by engineers and take suitable measures to avoid it | software engineers | security | S-04 page 17 | C-07 |
| R-0842 | Companies should identify potential risks and vulnerabilities, assess their security posture, and implement appropriate defensive measures | management | security | S-04 page 18 | C-12 |
| R-0843 | It is essential to verify the provenance information of ingested components | software engineers | security | S-04 page 18 | C-10 |
| R-0844 | Companies should identify critical assets and implement controls to protect them from unauthorized access | management | security | S-04 page 18 | C-08 |
| R-0845 | It is crucial to assess security risks and implement appropriate defensive measures to protect software supply chains | management | security | S-04 page 19 | C-12 |
| R-0846 | Organizations should regularly assess their security posture, identify weaknesses and vulnerabilities, and implement defensive measures | management | security | S-04 page 20 | C-12 |
| R-0847 | Organizations should ensure that their SDLC environment remains compliant with applicable security and relevant standards | operations engineers | security | S-04 page 20 | C-18 |
| R-0848 | All developer systems should meet a predefined minimum baseline for security | operations engineers | security | S-04 page 20 | C-18 |
| R-0849 | Independent and open-source developers will need to follow best practices to protect their own systems | software engineers | security | S-04 page 20 | C-18 |
| R-0850 | Government and enterprise environments should establish and adhere to a well-defined security policy that meets regulatory requirements | management | quality | S-04 page 20 | C-41 |
| R-0851 | Readers should refer to SP 800-53 Revision 5 for a more complete treatment of security policy | software engineers | quality | S-04 page 20 | C-37 |
| R-0852 | The security team should establish a policy for trusted sources of open-source software, with minimum coding requirements, reputational standards, and digitally signed packages | security team | security | S-04 page 21 | C-10 |
| R-0853 | The security team should approve the merging of unverified sources of open-source software | security team | security | S-04 page 21 | C-10 |
| R-0854 | Developers should download open-source software as source code rather than pre-compiled binaries, when available | software engineers | security | S-04 page 21 | C-10 |
| R-0855 | Developers should verify digital signatures, run vulnerability scans, check for recent updates, and generate an SBOM with dependency scanning on the first commit | software engineers | security | S-04 page 21 | C-10 |
| R-0856 | Artifacts should be scanned in internal repositories for new defects, and their use in builds should be stoppable based on criticality | software engineers | security | S-04 page 21 | C-11 |
| R-0857 | CI/CD processes should be audited regularly, and automation should be introduced wherever possible | quality assurance | security | S-04 page 21 | C-18 |
| R-0858 | There should be an isolated CI/CD environment and elevated administrator credentials for deploying applications to clouds | operations engineers | security | S-04 page 21 | C-05 |
| R-0859 | There should be enhanced real-time monitoring and alerting to detect suspicious activities in CI/CD servers | operations engineers | security | S-04 page 21 | C-18 |
| R-0860 | Proposed changes should adhere to the SDLC processes defined by the organization | software engineers | operations | S-04 page 21 | C-26 |
| R-0861 | Write access to source control should be considered a high risk and tightly controlled | operations engineers | security | S-04 page 21 | C-08 |
| R-0862 | Another developer should perform a code review before a patch is merged | software engineers | security | S-04 page 21 | C-02 |
| R-0863 | Code analysis tools should be implemented to catch common mistakes | software engineers | security | S-04 page 21 | C-11 |
| R-0864 | Care should be taken to avoid inundating developers with false positives | software engineers | security | S-04 page 21 | C-11 |
| R-0865 | The generation of provenance data should be accompanied by mechanisms to validate, authenticate, and use the data in policy decisions | users and customers | security | S-04 page 22 | C-16 |
| R-0866 | Entities that perform SSC activities should be authenticated through verification of credentials, and given permissions through authorization | operations engineers | security | S-04 page 23 | C-08 |
| R-0867 | The integrity of artifacts and repositories should be ensured by verifying their digital signatures | users and customers | security | S-04 page 23 | C-16 |
| R-0868 | Establishing trust should be a recurring process throughout the CI/CD system | operations engineers | security | S-04 page 23 | C-16 |
| R-0869 | The inputs and outputs of each build step should be verified | software engineers | security | S-04 page 23 | C-04 |
| R-0870 | Harden the CI/CD execution environment to reduce its attack surface. | operations engineers | security | S-04 page 24 | C-18 |
| R-0871 | Define roles for the actors who operate the various CI/CD pipelines. | operations engineers | security | S-04 page 24 | C-08 |
| R-0872 | Identify the granular authorizations to perform tasks such as committing code, generating builds and packages, and checking artifacts into and out of repositories. | operations engineers | security | S-04 page 24 | C-08 |
| R-0873 | Automate the entire CI/CD pipeline through the deployment of appropriate tools. | operations engineers | security | S-04 page 24 | C-03 |
| R-0874 | Define CI/CD pipeline activities and security requirements for application code, infrastructure as code, and policy and configuration code. | operations engineers | operations | S-04 page 24 | C-20 |
| R-0875 | Specify build policies covering a secure isolated platform, hardened build servers, the build tools, and authentication and authorization of developers. | operations engineers | security | S-04 page 25 | C-05 |
| R-0876 | Enforce the build policies with an agent, a policy enforcement engine or some other means. | operations engineers | security | S-04 page 25 | C-18 |
| R-0877 | Ensure the concurrent generation of evidence for build attestation during software delivery. | operations engineers | security | S-04 page 25 | C-04 |
| R-0878 | Components of the build platform, such as compiler and interpreter, must be hardened, isolated and secure. | operations engineers | security | S-04 page 25 | C-05 |
| R-0879 | Evidence generation should be enabled by a process with a higher level of trust or isolation than the build, and it requires verification within the build as it occurs. | operations engineers | security | S-04 page 25 | C-05 |
| R-0880 | Evidence that tools or processes run in an isolated environment should be gathered. | operations engineers | security | S-04 page 25 | C-04 |
| R-0881 | Hash evidence of the build should be signed by a trusted build component that developers do not control. | operations engineers | security | S-04 page 25 | C-04 |
| R-0882 | The population of the process attestation should be considered best effort. | operations engineers | security | S-04 page 25 | C-04 |
| R-0883 | Attestations must be cryptographically signed using a secure key. | operations engineers | security | S-04 page 26 | C-04 |
| R-0884 | The storage location of attestations must be tamper-proof and protected by robust access control. | operations engineers | security | S-04 page 26 | C-04 |
| R-0885 | Two checks are required for PULL and PUSH operations: the authentication type must be consistent with the developer role. | operations engineers | security | S-04 page 26 | C-08 |
| R-0886 | Developers with merge approval permissions cannot approve their own merges. | software engineers | security | S-04 page 26 | C-02 |
| R-0887 | The integrity of the code in the repository must be trustable for further updates. | software engineers | security | S-04 page 26 | C-01 |
| R-0888 | The project maintainer should run automated checks on all artifacts covered in a pushed change, such as unit tests, linters, integrity tests and security checks. | software engineers | quality | S-04 page 27 | C-30 |
| R-0889 | CI pipelines should only be run with tools when confidence is established in the trustworthiness of the source-code origin of those tools. | software engineers | security | S-04 page 27 | C-10 |
| R-0890 | The SCM should run CI workflows in sandboxed environments without network access, privileged access or access to secrets, or have built-in protection that delays CI runs until a maintainer with write access approves them. | suppliers | security | S-04 page 27 | C-06 |
| R-0891 | The built-in protection should take effect when an outside contributor submits a pull request to a public repository. | software engineers | security | S-04 page 27 | C-06 |
| R-0892 | The protection setting should be at the strictest level, such as Require approval for all outside collaborators. | software engineers | security | S-04 page 27 | C-06 |
| R-0893 | If the SCM has no built-in protections, external security tools are required that evaluate and enhance the SCM security posture and detect and remediate misconfigurations, vulnerabilities and compliance issues. | security team | security | S-04 page 27 | C-18 |
| R-0894 | The framework should provide protection against all known attacks on metadata generation, signing, signing key management, signing authority, key validation and signature verification. | suppliers | security | S-04 page 28 | C-16 |
| R-0895 | The framework should protect the signing operation by requiring the policy of Sec. 5.1.1 to be satisfied before signing. | suppliers | security | S-04 page 28 | C-16 |
| R-0896 | The framework should provide a means to minimize the impacts of key compromise by supporting roles with multiple keys and threshold or quorum trust, except minimally trusted roles that use a single key. | suppliers | security | S-04 page 28 | C-07 |
| R-0897 | Online keys should not be used for any role that clients ultimately trust for files they may install. | suppliers | security | S-04 page 28 | C-16 |
| R-0898 | When keys are online, exceptional care should be taken, such as storing them in an HSM and allowing their use only if the signed artifacts pass the policy. | suppliers | security | S-04 page 28 | C-07 |
| R-0899 | The framework must be flexible enough to meet the needs of a wide variety of software update systems. | suppliers | security | S-04 page 28 | C-15 |
| R-0900 | The framework must be easy to integrate with software update systems. | suppliers | security | S-04 page 28 | C-15 |
| R-0901 | Appropriate forms of testing should be performed before code commits, and the listed requirements must be met. | software engineers | quality | S-04 page 28 | C-31 |
| R-0902 | SAST and DAST tools covering all languages used in development should be run in CI/CD pipelines, with code coverage reports provided to developers and security personnel. | software engineers | security | S-04 page 28 | C-11 |
| R-0903 | If open-source modules and libraries are used, dependencies must be enumerated, understood and evaluated for policy, potentially with SCA tools. | software engineers | security | S-04 page 29 | C-10 |
| R-0904 | The security conditions that dependencies should meet for inclusion must also be tested. | software engineers | security | S-04 page 29 | C-10 |
| R-0905 | Dependency file detectors should detect all dependencies, including transitive dependencies, preferably with no limit to the depth analyzed. | software engineers | security | S-04 page 29 | C-09 |
| R-0906 | Prevention of secrets in committed code is required, through a scanning feature for secrets (push protection). | software engineers | security | S-04 page 29 | C-11 |
| R-0907 | Push protection should satisfy COMMIT-REQ-1: evaluate committed code for policy, including the absence of secrets; display detected secrets prominently; generate alerts on violations; document remediation methods. | software engineers | security | S-04 page 29 | C-11 |
| R-0908 | Push protection features should be enabled for all repositories assigned to an administrator, including developer identity verification, developer signing of code commits, and file name verification. | operations engineers | security | S-04 page 29 | C-11 |
| R-0909 | Secret scanning should be invoked for code ready to be deployed, and the repository should be scanned for secrets even before it is populated. | software engineers | security | S-04 page 29 | C-11 |
| R-0910 | Before merging pull requests, it should be possible to view details of vulnerable versions through dependency review. | software engineers | security | S-04 page 29 | C-11 |
| R-0911 | If a secure build environment and process are established, it should be possible to specify that the deployed artifact must have been generated by that build process. | operations engineers | security | S-04 page 29 | C-16 |
| R-0912 | There should be evidence that a container image was scanned for vulnerabilities and attested for the findings. | security team | security | S-04 page 30 | C-11 |
| R-0913 | It should be possible to allow or block image deployment based on organization-defined policies. | management | security | S-04 page 30 | C-16 |
| R-0914 | The release build scripts should be periodically checked for malicious code. | security team | security | S-04 page 30 | C-11 |
| R-0915 | A container image should be scanned for vulnerabilities as soon as it is built, even before it is pushed to a registry. | software engineers | security | S-04 page 30 | C-11 |
| R-0916 | Tools that interact with repositories of container images and language packages should be capable of integration with CD tools. | suppliers | operations | S-04 page 30 | C-46 |
| R-0917 | The SSC security tasks should be applied when creating configuration data before deployment, capturing release data, modifying software at runtime, and monitoring. | software engineers | operations | S-04 page 30 | C-20 |
| R-0918 | The GitOps process should rely on automation rather than manual operations. | operations engineers | operations | S-04 page 30 | C-20 |
| R-0919 | Package managers that facilitate GitOps should preserve all data on released packages, including version numbers and configuration files. | suppliers | operations | S-04 page 30 | C-46 |
| R-0920 | Changes should not be manually applied at runtime; changes should be made to the code and a new release triggered. | operations engineers | operations | S-04 page 31 | C-20 |
| R-0921 | The Git repository should be pulled automatically and compared with the specified state, to monitor and remediate drift. | operations engineers | operations | S-04 page 31 | C-20 |
| R-0922 | Administrators may choose to resync configurations automatically to the defined state. | operations engineers | operations | S-04 page 31 | C-20 |
| R-0923 | Notifications should be sent about configuration differences, and manual remediation should be performed. | operations engineers | operations | S-04 page 31 | C-23 |
| R-0924 | Code older than a certain time period should not be launched (build horizon). | software engineers | security | S-04 page 31 | C-10 |
| R-0925 | Securing CI/CD clients should prevent malicious code from stealing confidential information. | operations engineers | security | S-04 page 31 | C-18 |
| R-0926 | The entire CI/CD pipeline must be automated through the deployment of appropriate tools as a prerequisite (Appendix A wording). | operations engineers | security | S-04 page 35 | C-03 |
| R-0927 | Online keys must not be used for any role that clients ultimately trust (Appendix A wording; the body on page 28 says should not). | suppliers | security | S-04 page 38 | C-16 |
| R-0928 | CI pipelines should only use external tools when confidence is established in the source-code origin (Appendix A wording, e.g. Jenkins). | software engineers | security | S-04 page 39 | C-10 |
| R-0929 | Both SAST and DAST tools used in CI/CD pipelines must provide coverage for the different language systems used in cloud-native applications. | software engineers | security | S-04 page 40 | C-11 |
| R-0930 | Dependencies must be detected using appropriate SCA tools, and the security conditions they should meet must also be tested. | software engineers | security | S-04 page 40 | C-11 |
| R-0931 | Every team should have security expertise, though not every member must be a security expert. | software engineers | quality | S-05 Principle 1, Integrating security | C-39 |
| R-0932 | Define security requirements at the start and during delivery, with top-down support. | software engineers | security | S-05 Principle 1, Action 1 | C-12 |
| R-0933 | Make security an essential skill for every delivery team member, as a daily practice. | software engineers | quality | S-05 Principle 1, Action 2 | C-39 |
| R-0934 | Encourage raising concerns, questions and challenge; people should be rewarded for caring about security. | software engineers | quality | S-05 Principle 1, Action 3 | C-40 |
| R-0935 | Do not push security aside for features or deadlines. | management | quality | S-05 Principle 1, Action 4 | C-40 |
| R-0936 | Involve security expertise in design and development at all times. | software engineers | quality | S-05 Principle 1, Action 5 | C-40 |
| R-0937 | Ask for help when knowledge is stretched, especially for security-critical components. | software engineers | quality | S-05 Principle 1, Action 6 | C-39 |
| R-0938 | Provide training, tools and development environments that support secure development. | management | quality | S-05 Principle 1, Action 7 | C-39 |
| R-0939 | Promote a no-blame culture so that issues are reported and fixed. | management | quality | S-05 Principle 1, Action 8 | C-40 |
| R-0940 | Keep security supporting delivery, not blocking it; security experts should be approachable, reasonable and practical. | security team | quality | S-05 Principle 1, Action 9 | C-40 |
| R-0941 | Regularly ask whether there is a security implication. | software engineers | security | S-05 Principle 1, Practical steps | C-12 |
| R-0942 | Senior members should lead by example. | software engineers | quality | S-05 Principle 1, Practical steps | C-40 |
| R-0943 | Security understanding must be regularly updated to stay useful. | software engineers | quality | S-05 Principle 2, Introduction | C-39 |
| R-0944 | Developers should know common threats to their code, such as injection. | software engineers | quality | S-05 Principle 2, Action 1 | C-39 |
| R-0945 | Provide resources to developers who lack knowledge of common threats. | management | quality | S-05 Principle 2, Action 1 | C-39 |
| R-0946 | Screen developer recruits for basic security awareness; if screening is not possible, allocate extra learning resources. | management | quality | S-05 Principle 2, Action 2 | C-39 |
| R-0947 | Give time and resources for ongoing security training. | management | quality | S-05 Principle 2, Action 3 | C-39 |
| R-0948 | Teach developers the threat types their code will face. | software engineers | quality | S-05 Principle 2, Action 4 | C-39 |
| R-0949 | Hold developers accountable for the security of their code. | software engineers | quality | S-05 Principle 2, Action 5 | C-40 |
| R-0950 | Take extra care writing defensive code for security-critical components. | software engineers | security | S-05 Principle 2, Action 6 | C-13 |
| R-0951 | Security specialists should identify which components are security-critical, so that developers know when to seek help. | security team | security | S-05 Principle 2, Action 7 | C-12 |
| R-0952 | Use established, well-tested security components rather than building your own. | software engineers | security | S-05 Principle 2, Action 8 | C-10 |
| R-0953 | Run sessions on mistakes, using real issues from the product where possible. | software engineers | quality | S-05 Principle 2, Action 9 | C-39 |
| R-0954 | Maintain a list of trusted security training resources relevant to the product. | management | quality | S-05 Principle 2, Action 10 | C-39 |
| R-0955 | Limit information on public profiles that attackers could use. | software engineers | security | S-05 Principle 2, Action 11 | C-18 |
| R-0956 | Keep up to date with security features of tools, languages and technologies; do not use old or deprecated APIs. | software engineers | security | S-05 Principle 2, Action 12 | C-13 |
| R-0957 | Two or more people should review code, and the review should be enforced in the deployment pipeline. | quality assurance | security | S-05 Principle 3, Peer-reviewing code | C-02 |
| R-0958 | Identified review issues should be fixed. | software engineers | security | S-05 Principle 3, Peer-reviewing code | C-02 |
| R-0959 | Code should be readable and self-documenting, with a clean, simple structure. | software engineers | quality | S-05 Principle 3, Introduction | C-32 |
| R-0960 | Use a sound architecture and a consistent coding style. | software engineers | quality | S-05 Principle 3, Introduction | C-38 |
| R-0961 | Maintain simple supporting material alongside the system as it evolves. | software engineers | quality | S-05 Principle 3, Introduction | C-37 |
| R-0962 | Document a specification before coding. | software engineers | quality | S-05 Principle 3, Introduction | C-38 |
| R-0963 | Layout code so that components have clear homes, allowing for expansion. | software engineers | quality | S-05 Principle 3, Action 1 | C-32 |
| R-0964 | Follow secure coding standards where they are available. | software engineers | security | S-05 Principle 3, Action 2 | C-13 |
| R-0965 | Class, method, function, file and folder names should be self-explanatory. | software engineers | quality | S-05 Principle 3, Action 3 | C-32 |
| R-0966 | Provide supportive developer tooling, such as IDE plugins, linting and security hints. | software engineers | quality | S-05 Principle 3, Action 4 | C-32 |
| R-0967 | Use a consistent coding style across contributors. | software engineers | quality | S-05 Principle 3, Action 5 | C-32 |
| R-0968 | Each code block should state its responsibilities, such as which component validates untrusted input. | software engineers | quality | S-05 Principle 3, Action 6 | C-38 |
| R-0969 | Keep passwords and private keys isolated from the codebase. | software engineers | security | S-05 Principle 3, Action 7 | C-07 |
| R-0970 | Make small, regular, clearly labelled commits. | software engineers | quality | S-05 Principle 3, Action 8 | C-36 |
| R-0971 | Code changes should be attributable to an author using strong authentication. | software engineers | security | S-05 Principle 3, Action 9 | C-01 |
| R-0972 | Reject complicated, confusing or insecure practices; use pull requests and comments for feedback. | quality assurance | security | S-05 Principle 3, Action 10 | C-02 |
| R-0973 | Team members on the same codebase should communicate regularly through strong channels. | software engineers | quality | S-05 Principle 3, Action 11 | C-42 |
| R-0974 | Keep documentation clear, concise and current. | software engineers | quality | S-05 Principle 3, Action 12 | C-37 |
| R-0975 | Give new team members good support and documentation for onboarding. | management | quality | S-05 Principle 3, Action 13 | C-39 |
| R-0976 | Check return values and handle errors at the point of the call. | software engineers | security | S-05 Principle 3, Action 14 | C-13 |
| R-0977 | Treat third-party frameworks and libraries like the code you write. | software engineers | security | S-05 Principle 3, External dependencies | C-10 |
| R-0978 | Ask about the security impact, maintenance and past vulnerability handling of each dependency. | software engineers | security | S-05 Principle 3, External dependencies | C-10 |
| R-0979 | Provide developers with the tools and environments they need, so they do not seek insecure workarounds. | management | security | S-05 Principle 4, Action 1 | C-18 |
| R-0980 | Trust developers and verify their actions through education and monitoring. | management | security | S-05 Principle 4, Action 2 | C-18 |
| R-0981 | Apply the NCSC end user device guidance to development environments; be pragmatic. | management | security | S-05 Principle 4, Action 3 | C-18 |
| R-0982 | Protect access credentials and secret keys with multi-factor authentication, least privilege and revocation. | software engineers | security | S-05 Principle 4, Action 4 | C-08 |
| R-0983 | Plan the controls that protect published products if a development environment is breached. | management | security | S-05 Principle 4, Action 5 | C-18 |
| R-0984 | Do not operate production systems from development environments; where unavoidable, limit exposure. | operations engineers | operations | S-05 Principle 4, Action 6 | C-22 |
| R-0985 | Constrain compromised devices with firewall rules that allow only intended services. | operations engineers | security | S-05 Principle 4, Action 7 | C-18 |
| R-0986 | Organisations should have an idea of what legitimate use of the development environment looks like, and use logs to spot unusual activity. | operations engineers | security | S-05 Principle 4, Action 8 | C-18 |
| R-0987 | Treat the development environment as compromised; add multi-factor authentication, automated security testing and multi-person review before the pipeline. | software engineers | security | S-05 Principle 4, Securing a flexible system | C-18 |
| R-0988 | Assess how the repository is administered and what infrastructure it runs on before you trust it. | software engineers | security | S-05 Principle 5, Action 1 | C-18 |
| R-0989 | Assess a hosting provider against the NCSC Cloud Security Principles. | management | security | S-05 Principle 5, Action 1 | C-19 |
| R-0990 | Consider cryptographic signing and verification of code. | software engineers | security | S-05 Principle 5, Action 1 | C-16 |
| R-0991 | Enforce least privilege technically for who can change the repository, and attribute all activity to a person. | operations engineers | security | S-05 Principle 5, Action 2 | C-08 |
| R-0992 | Private keys should be password protected; consider hardware tokens. | software engineers | security | S-05 Principle 5, Action 3 | C-07 |
| R-0993 | Keep secrets logically separate from source code, and define a process for injecting them at runtime. | software engineers | security | S-05 Principle 5, Action 4 | C-07 |
| R-0994 | Revoke access promptly when it is no longer required or when compromise is suspected. | operations engineers | security | S-05 Principle 5, Action 5 | C-08 |
| R-0995 | Include open code in the risk model; keep code that attackers could exploit in a private repository. | software engineers | security | S-05 Principle 5, Action 6 | C-12 |
| R-0996 | Require review before code merges into the master branch, especially branches used for production deployment. | quality assurance | security | S-05 Principle 5, Action 7 | C-02 |
| R-0997 | Review external changes and pull requests carefully, with extra care for code that runs in build and test. | quality assurance | security | S-05 Principle 5, Action 8 | C-02 |
| R-0998 | Keep backups of code so it can be restored. | operations engineers | operations | S-05 Principle 5, Action 10 | C-27 |
| R-0999 | Repository access must align with the joiners and leavers process. | operations engineers | security | S-05 Principle 5, Self assessment | C-08 |
| R-1000 | Use a trusted pipeline; assess how it and its infrastructure are administered. | operations engineers | security | S-05 Principle 6, Action 1 | C-03 |
| R-1001 | Peer review code before deployment, with technical controls so that review cannot be bypassed. | quality assurance | security | S-05 Principle 6, Action 2 | C-02 |
| R-1002 | Production should not deploy from untrusted repositories, forks or branches. | operations engineers | security | S-05 Principle 6, Action 3 | C-16 |
| R-1003 | Run automatic testing as part of deployments; do not ignore failing tests. | software engineers | quality | S-05 Principle 6, Action 4 | C-30 |
| R-1004 | Store, manage and inject secrets securely; consider rotating keys and automating rotation. | software engineers | security | S-05 Principle 6, Action 5 | C-07 |
| R-1005 | Enforce the full sequence from development to deployment, so that controls cannot be bypassed or reordered. | operations engineers | security | S-05 Principle 6, Action 6 | C-06 |
| R-1006 | The pipeline should enforce accept and reject rules that individuals cannot alter. | operations engineers | security | S-05 Principle 6, Action 7 | C-06 |
| R-1007 | Automated build and test tools should not let malicious code from third-party pull requests run. | operations engineers | security | S-05 Principle 6, Action 8 | C-06 |
| R-1008 | Include only intended dependencies from legitimate sources. | software engineers | security | S-05 Principle 6, Action 9 | C-10 |
| R-1009 | If confidence in the pipeline is low, consider requiring approval before production release. | operations engineers | operations | S-05 Principle 6, Action 10 | C-26 |
| R-1010 | Builds should pull only from an allow list of trusted third-party repositories over secure channels. | software engineers | security | S-05 Principle 6, Self assessment | C-10 |
| R-1011 | Security should support the delivery process rather than obstruct it. | management | quality | S-05 Principle 6, Introduction | C-40 |
| R-1012 | Run inexpensive tests on every change; save resource-intensive tests for notable releases. | software engineers | quality | S-05 Principle 6, Action 4 | C-31 |
| R-1013 | Align security testing with the software development lifecycle so that it runs at a comparable speed. | security team | quality | S-05 Principle 7, Action 1 | C-30 |
| R-1014 | Many common security tests and compliance checks can be done by automated tools, and such tests can act as a gate that blocks a deployment until they pass. | software engineers | quality | S-05 Principle 7, Action 2 | C-30 |
| R-1015 | Tailor tests to your application. | software engineers | quality | S-05 Principle 7, Action 3 | C-31 |
| R-1016 | When an issue is found, write a test to prevent it from reappearing. | software engineers | quality | S-05 Principle 7, Action 4 | C-31 |
| R-1017 | Make test results easy for developers to see and discuss. | software engineers | quality | S-05 Principle 7, Action 5 | C-30 |
| R-1018 | Direct specialist testers to work that cannot be automated. | security team | security | S-05 Principle 7, Action 6 | C-17 |
| R-1019 | Move slow or manual tests out of the build pipeline and run them in parallel, reporting failures back to the team. | software engineers | quality | S-05 Principle 7, Action 7 | C-30 |
| R-1020 | Fix or remove failing or noisy tests, after checking for real issues first. | software engineers | quality | S-05 Principle 7, Action 8 | C-30 |
| R-1021 | Test your tests in a safe environment, to find false negatives. | quality assurance | quality | S-05 Principle 7, Action 9 | C-31 |
| R-1022 | Build internal skills so that developers can write security tests. | management | quality | S-05 Principle 7, Action 10 | C-39 |
| R-1023 | Track which code is covered by testing and which is not. | quality assurance | quality | S-05 Principle 7, Action 11 | C-31 |
| R-1024 | Do not cast aside all forms of security testing. | security team | security | S-05 Principle 7, Introduction | C-17 |
| R-1025 | Make a plan for handling security flaws. | software engineers | security | S-05 Principle 7, Demonstrating absence | C-14 |
| R-1026 | Accept that flaws will exist, and make a plan to find and fix them. | software engineers | security | S-05 Principle 8, Introduction | C-14 |
| R-1027 | For widely used software and hardware, deploy patches and check for known weak configurations. | operations engineers | security | S-05 Principle 8, Action 1 | C-10 |
| R-1028 | Keep a register of security debt so that it can be addressed later. | software engineers | quality | S-05 Principle 8, Action 2 | C-35 |
| R-1029 | The product team should be able to identify security issues and get them fixed. | software engineers | security | S-05 Principle 8, Action 3 | C-14 |
| R-1030 | After any event, carry out a post-mortem, and address the root cause when possible. | software engineers | operations | S-05 Principle 8, Action 4 | C-25 |
| R-1031 | Provide a route for users and researchers to report flaws responsibly. | users and customers | security | S-05 Principle 8, Action 5 | C-14 |
| R-1032 | When a security issue is found, consider writing a new test for it. | software engineers | quality | S-05 Principle 8, Action 6 | C-31 |
| R-1033 | Specialist advice is recommended for products that handle highly sensitive data. | security team | security | S-05 Collection page, Summary | C-12 |
| R-1034 | The guidance should be revisited periodically, because systems and teams change. | management | quality | S-05 Collection page, Summary | C-35 |
| R-1035 | Products with digital elements shall be made available on the market only where they meet the essential cybersecurity requirements of Part I of Annex I, when properly installed, maintained and used, and where applicable necessary security updates are installed. | management | quality | S-06 page 11 | C-41 |
| R-1036 | Products with digital elements shall be made available on the market only where the processes put in place by the manufacturer comply with the essential cybersecurity requirements of Part II of Annex I. | management | quality | S-06 page 11 | C-41 |
| R-1037 | The manufacturer shall ensure that vulnerabilities of a product are handled effectively during the support period, in accordance with Part II of Annex I. | management | security | S-06 page 10 | C-14 |
| R-1038 | Member States shall ensure that compliance with Annex I, including the manufacturers' ability to handle vulnerabilities, is taken into consideration in procurement. | regulators and auditors | quality | S-06 page 11 | C-41 |
| R-1039 | Products that have the core functionality of an Annex III category shall be subject to the conformity assessment procedures referred to in Article 32(2) and (3). | management | quality | S-06 page 11 | C-41 |
| R-1040 | Products that have the core functionality of an Annex IV category shall be subject to the conformity assessment procedure referred to in Article 32(3), where no delegated act has been adopted. | management | quality | S-06 page 11 | C-41 |
| R-1041 | Member States shall not impede the making available on the market of compliant products. | regulators and auditors | quality | S-06 page 11 | C-41 |
| R-1042 | Member States shall not prevent presentation of non-compliant prototypes at trade fairs, if a visible sign indicates non-compliance and that the product is not to be made available until it complies. | regulators and auditors | quality | S-06 page 11 | C-41 |
| R-1043 | Member States shall not prevent making available unfinished software for a limited testing period, if a visible sign indicates non-compliance and it is not marketed for other purposes. | regulators and auditors | quality | S-06 page 11 | C-41 |
| R-1044 | The Commission shall consult and take into account the views of relevant stakeholders when preparing implementing measures. | regulators and auditors | quality | S-06 page 11 | C-41 |
| R-1045 | The Commission shall organise regular consultation and information sessions, at least once a year. | regulators and auditors | quality | S-06 page 11 | C-41 |
| R-1046 | The delegated acts shall provide a minimum transitional period of 12 months where appropriate, and of six months for critical products, unless shorter periods are justified by urgency. | regulators and auditors | quality | S-06 page 11 | C-41 |
| R-1047 | The Commission shall adopt an implementing act by 11 December 2025 specifying the technical descriptions of product categories. | regulators and auditors | quality | S-06 page 11 | C-41 |
| R-1048 | Member States shall promote measures and strategies to enhance skills for the needs of professionals in support of the Regulation. | regulators and auditors | quality | S-06 page 11 | C-39 |
| R-1049 | Manufacturers shall ensure that a product with digital elements is designed, developed and produced in line with the essential cybersecurity requirements of Annex I Part I | management | security | S-06 page 12, Article 13(1) | C-13 |
| R-1050 | Manufacturers shall assess the cybersecurity risks of a product and use the result in planning, design, development, production, delivery and maintenance to minimise risks, prevent incidents and minimise impact, including impact on health and safety | management | security | S-06 page 12, Article 13(2) | C-12 |
| R-1051 | Manufacturers shall document the cybersecurity risk assessment and update it as appropriate during the support period; it shall cover intended purpose, reasonably foreseeable use, conditions of use and expected length of use | management | security | S-06 page 12, Article 13(3) | C-12 |
| R-1052 | The risk assessment shall state whether and how the Annex I Part I point 2 security requirements apply and how Part I point 1 and the Part II vulnerability handling requirements are applied | management | security | S-06 page 12, Article 13(3) | C-12 |
| R-1053 | Manufacturers shall include the cybersecurity risk assessment in the technical documentation under Article 31 and Annex VII, and shall include a clear justification where essential requirements do not apply | management | quality | S-06 page 12, Article 13(4) | C-41 |
| R-1054 | Manufacturers shall exercise due diligence when integrating third-party components, including free and open-source components not made available in a commercial activity | management | security | S-06 page 12, Article 13(5) | C-10 |
| R-1055 | Manufacturers shall report a vulnerability in an integrated component to the person or entity that makes or maintains the component, and shall address and remediate it under Part II of Annex I | management | security | S-06 page 12, Article 13(6) | C-14 |
| R-1056 | Manufacturers shall share a software or hardware fix for a component with its maintainer, where appropriate in a machine-readable format | management | security | S-06 page 12, Article 13(6) | C-14 |
| R-1057 | Manufacturers shall systematically document cybersecurity aspects, including vulnerabilities and third-party information, in a manner proportionate to the risks, and shall update the risk assessment where applicable | management | security | S-06 page 12, Article 13(7) | C-12 |
| R-1058 | Manufacturers shall ensure, when placing a product on the market and for the support period, that vulnerabilities of the product and its components are handled effectively under Part II of Annex I | management | security | S-06 page 12, Article 13(8) | C-14 |
| R-1059 | Manufacturers shall determine the support period so that it reflects the expected length of use, and it shall be at least five years, or the expected use time if that is less than five years | management | security | S-06 page 12, Article 13(8) | C-15 |
| R-1060 | Manufacturers shall include in the technical documentation the information that they used to determine the support period | management | security | S-06 page 12, Article 13(8) | C-15 |
| R-1061 | Manufacturers shall have appropriate policies and procedures, including coordinated vulnerability disclosure policies, to process and remediate vulnerabilities reported from internal or external sources | management | security | S-06 page 12, Article 13(8) | C-14 |
| R-1062 | The Commission may adopt delegated acts that set a minimum support period for specific product categories where market surveillance data shows inadequate support periods | regulators and auditors | security | S-06 page 12, Article 13(8) | C-15 |
| R-1063 | Manufacturers shall ensure that each security update made available during the support period remains available for at least 10 years after issue, or for the rest of the support period if that is longer | management | security | S-06 page 12, Article 13(9) | C-15 |
| R-1064 | A manufacturer that places a substantially modified software version on the market may ensure compliance with Part II point 2 only for the last version, if earlier users can get that version free of charge and without extra cost to adapt their environment | management | security | S-06 page 12, Article 13(10) | C-15 |
| R-1065 | Manufacturers may maintain public software archives of historical versions, and users shall be clearly and easily informed about the risks of unsupported software | management | security | S-06 page 12, Article 13(11) | C-15 |
| R-1066 | Before placing a product on the market, manufacturers shall draw up the technical documentation under Article 31 and shall carry out, or have carried out, the chosen conformity assessment procedure under Article 32 | management | quality | S-06 page 12, Article 13(12) | C-41 |
| R-1067 | When conformity is shown, manufacturers shall draw up the EU declaration of conformity under Article 28 and affix the CE marking under Article 30 | management | quality | S-06 page 12, Article 13(12) | C-41 |
| R-1068 | Manufacturers shall keep the technical documentation and the EU declaration of conformity at the disposal of market surveillance authorities for at least 10 years or for the support period, whichever is longer | management | quality | S-06 page 12, Article 13(13) | C-41 |
| R-1069 | Manufacturers shall ensure that procedures are in place so that products in a series of production remain in conformity, and shall take into account changes in process, design, characteristics and harmonised standards | management | quality | S-06 page 12, Article 13(14) | C-41 |
| R-1070 | Manufacturers shall ensure that products bear a type, batch or serial number or other identifier, or that this information is given on the packaging or in an accompanying document | management | operations | S-06 page 12, Article 13(15) | C-45 |
| R-1071 | Manufacturers shall give their name, trade name or trademark, postal address, digital contact and, where applicable, website, on the product, its packaging or an accompanying document | management | quality | S-06 page 12, Article 13(16) | C-41 |
| R-1072 | Manufacturers shall include the contact details in the Annex II information, in a language that users and market surveillance authorities can easily understand | management | quality | S-06 page 12, Article 13(16) | C-41 |
| R-1073 | Manufacturers shall designate a single point of contact that users can easily identify, which allows users to choose their means of communication and is not limited to automated tools | management | security | S-06 page 12, Article 13(17) | C-14 |
| R-1074 | Manufacturers shall accompany each product with the Annex II information and instructions, in paper or electronic form, that allow secure installation, operation and use | management | quality | S-06 page 12, Article 13(18) | C-37 |
| R-1075 | Manufacturers shall keep the Annex II information at the disposal of users and market surveillance authorities for at least 10 years or for the support period, whichever is longer, and online information shall be accessible, user-friendly and available for the same period | management | quality | S-06 page 12, Article 13(18) | C-37 |
| R-1076 | Manufacturers shall state the end date of the support period, including at least month and year, clearly and understandably at the time of purchase, and on the product, its packaging or by digital means where applicable | management | security | S-06 page 12, Article 13(19) | C-15 |
| R-1077 | Where technically feasible, manufacturers shall display a notification to users that the product has reached the end of its support period | management | security | S-06 page 12, Article 13(19) | C-15 |
| R-1078 | Manufacturers shall provide a copy of the EU declaration of conformity or a simplified EU declaration of conformity with the product, and a simplified declaration shall contain the exact internet address of the full declaration | management | quality | S-06 page 12, Article 13(20) | C-41 |
| R-1079 | During the support period, manufacturers that know or have reason to believe that a product or their processes do not conform shall immediately take corrective measures, or withdraw or recall the product | management | quality | S-06 page 12, Article 13(21) | C-41 |
| R-1080 | On a reasoned request from a market surveillance authority, manufacturers shall provide the information and documentation needed to show conformity, in a language that the authority can easily understand | management | quality | S-06 page 12, Article 13(22) | C-41 |
| R-1081 | Manufacturers shall cooperate with a market surveillance authority, at its request, on measures to eliminate cybersecurity risks of their products | management | quality | S-06 page 12, Article 13(22) | C-41 |
| R-1082 | A manufacturer that ceases operations and cannot comply shall inform the market surveillance authorities before cessation takes effect, and shall inform users as far as possible | management | quality | S-06 page 12, Article 13(23) | C-43 |
| R-1083 | The Commission may, by implementing acts, specify the format and elements of the software bill of materials, taking into account European or international standards and best practices | regulators and auditors | security | S-06 page 12, Article 13(24) | C-09 |
| R-1084 | ADCO may decide to conduct a Union-wide dependency assessment, and market surveillance authorities may request software bills of materials from manufacturers for that purpose | regulators and auditors | security | S-06 page 12, Article 13(25) | C-09 |
| R-1085 | Chapter III Section 1, Chapters V and VII and Chapters IX to XI of Regulation (EU) 2023/988 shall apply to these products for aspects not covered by this Regulation, where no specific safety requirements of other Union harmonisation legislation apply | regulators and auditors | quality | S-06 page 12, Article 11 | C-41 |
| R-1086 | High-risk AI products that meet Annex I Part I and Part II and show the protection level in the EU declaration of conformity shall be deemed to comply with the cybersecurity requirements of Article 15 of Regulation (EU) 2024/1689 | regulators and auditors | quality | S-06 page 12, Article 12(1) | C-41 |
| R-1087 | For these products, the conformity assessment procedure under Article 43 of Regulation (EU) 2024/1689 shall apply | regulators and auditors | quality | S-06 page 12, Article 12(2) | C-41 |
| R-1088 | Important products in Annex III and critical products in Annex IV that are high-risk AI systems shall be subject to the conformity procedures of this Regulation as far as essential cybersecurity requirements are concerned | regulators and auditors | quality | S-06 page 12, Article 12(3) | C-41 |
| R-1089 | Manufacturers of these products may take part in the AI regulatory sandboxes under Article 57 of Regulation (EU) 2024/1689 | management | quality | S-06 page 12, Article 12(4) | C-41 |
| R-1090 | A manufacturer shall notify any actively exploited vulnerability, at the same time, to the CSIRT designated as coordinator and to ENISA, via the single reporting platform | management | security | S-06 page 13, Article 14(1) | C-14 |
| R-1091 | The early warning of an actively exploited vulnerability shall be sent without undue delay and within 24 hours of the manufacturer becoming aware of it, and shall indicate the Member States where the product is made available | management | security | S-06 page 13, Article 14(2)(a) | C-14 |
| R-1092 | The vulnerability notification shall be sent without undue delay and within 72 hours of the manufacturer becoming aware, unless the information was already provided | management | security | S-06 page 13, Article 14(2)(b) | C-14 |
| R-1093 | The vulnerability notification shall give general information, the nature of the exploit, corrective or mitigating measures, measures that users can take, and how sensitive the manufacturer considers the information | management | security | S-06 page 13, Article 14(2)(b) | C-14 |
| R-1094 | The final report shall be sent no later than 14 days after a corrective or mitigating measure is available, unless the information was already provided | management | security | S-06 page 13, Article 14(2)(c) | C-14 |
| R-1095 | The final report shall include the description of the vulnerability with severity and impact, information on any malicious actor where available, and details of the security update or other corrective measure | management | security | S-06 page 13, Article 14(2)(c) | C-14 |
| R-1096 | A manufacturer shall notify any severe incident that affects the security of the product, at the same time, to the CSIRT designated as coordinator and to ENISA, via the single reporting platform | management | operations | S-06 page 13, Article 14(3) | C-25 |
| R-1097 | The early warning of a severe incident shall be sent without undue delay and within 24 hours of the manufacturer becoming aware of it, and shall state whether unlawful or malicious acts are suspected | management | operations | S-06 page 13, Article 14(4)(a) | C-25 |
| R-1098 | The incident notification shall be sent without undue delay and within 72 hours of the manufacturer becoming aware, unless the information was already provided | management | operations | S-06 page 13, Article 14(4)(b) | C-25 |
| R-1099 | The incident notification shall give the nature of the incident, an initial assessment, and the corrective or mitigating measures taken and that users can take | management | operations | S-06 page 13, Article 14(4)(b) | C-25 |
| R-1100 | The final report shall be sent within one month after the incident notification and shall include a detailed description, the type of threat or root cause, and the mitigation measures applied and ongoing | management | operations | S-06 page 13, Article 14(4)(c) | C-25 |
| R-1101 | The CSIRT designated as coordinator may ask manufacturers for an intermediate report on status updates | regulators and auditors | quality | S-06 page 13, Article 14(6) | C-41 |
| R-1102 | Notifications shall be submitted through the endpoint of the CSIRT designated as coordinator in the Member State of the main establishment of the manufacturer, and where there is no main establishment, through the order of Member States in Article 14(7)(a) to (d) | management | quality | S-06 page 13, Article 14(7) | C-41 |
| R-1103 | After becoming aware of an actively exploited vulnerability or severe incident, the manufacturer shall inform the impacted users, and where appropriate all users, with mitigation and corrective measures, where appropriate in a structured machine-readable format | users and customers | security | S-06 page 13, Article 14(8) | C-14 |
| R-1104 | The Commission shall adopt, by 11 December 2025, delegated acts that specify the cybersecurity grounds for delaying dissemination of notifications under Article 16(2), and shall cooperate with the CSIRTs network and ENISA | regulators and auditors | quality | S-06 page 13, Article 14(9) | C-41 |
| R-1105 | The Commission may, by implementing acts, specify further the format and procedures of the notifications | regulators and auditors | quality | S-06 page 13, Article 14(10) | C-41 |
| R-1106 | Manufacturers and other natural or legal persons may notify vulnerabilities and cyber threats on a voluntary basis to a CSIRT designated as coordinator or to ENISA | management | security | S-06 page 13, Article 15(1) | C-14 |
| R-1107 | Manufacturers and other natural or legal persons may notify incidents and near misses on a voluntary basis to a CSIRT designated as coordinator or to ENISA | management | security | S-06 page 13, Article 15(2) | C-14 |
| R-1108 | The CSIRT designated as coordinator or ENISA shall process voluntary notifications under the procedure in Article 16, and the CSIRT may prioritise mandatory notifications | regulators and auditors | quality | S-06 page 13, Article 15(3) | C-41 |
| R-1109 | When a natural or legal person other than the manufacturer notifies an actively exploited vulnerability or severe incident, the CSIRT designated as coordinator shall inform the manufacturer without undue delay | regulators and auditors | quality | S-06 page 13, Article 15(4) | C-41 |
| R-1110 | The CSIRTs designated as coordinators and ENISA shall ensure the confidentiality and appropriate protection of the information provided by a notifying person | regulators and auditors | quality | S-06 page 13, Article 15(5) | C-41 |
| R-1111 | ENISA shall establish a single reporting platform and shall manage and maintain its day-to-day operations | regulators and auditors | quality | S-06 page 13, Article 16(1) | C-41 |
| R-1112 | The CSIRT that first receives a notification shall, without delay, disseminate it via the platform to the CSIRTs designated as coordinators in the Member States where the product is made available | regulators and auditors | quality | S-06 page 14, Article 16(2) | C-41 |
| R-1113 | In exceptional circumstances, the dissemination may be delayed for cybersecurity grounds for the time strictly necessary, and a CSIRT that withholds a notification shall immediately inform ENISA with the justification and the expected dissemination time | regulators and auditors | quality | S-06 page 14, Article 16(2) | C-41 |
| R-1114 | ENISA shall recommend dissemination of the full notification to the other CSIRTs and to ENISA itself where it finds a systemic risk to security in the internal market | regulators and auditors | quality | S-06 page 14, Article 16(2) | C-41 |
| R-1115 | The CSIRTs designated as coordinators shall give market surveillance authorities the notified information they need to fulfil their obligations | regulators and auditors | quality | S-06 page 14, Article 16(3) | C-41 |
| R-1116 | ENISA shall take appropriate and proportionate measures to manage risks to the security of the single reporting platform and shall notify any security incident affecting it to the CSIRTs network and the Commission without undue delay | regulators and auditors | quality | S-06 page 14, Article 16(4) | C-41 |
| R-1117 | ENISA with the CSIRTs network shall provide and implement specifications for the technical, operational and organisational measures of the platform | regulators and auditors | quality | S-06 page 14, Article 16(5) | C-41 |
| R-1118 | Vulnerabilities without corrective measures shall be shared under strict security protocols and on a need-to-know basis | regulators and auditors | quality | S-06 page 14, Article 16(5) | C-41 |
| R-1119 | A CSIRT designated as coordinator may delay dissemination of an actively exploited vulnerability found through coordinated vulnerability disclosure until the involved parties consent, and this shall not prevent manufacturers from notifying voluntarily | regulators and auditors | security | S-06 page 14, Article 16(6) | C-14 |
| R-1120 | ENISA may submit notified information to EU-CyCLONe where it is relevant to the coordinated management of large-scale incidents | regulators and auditors | quality | S-06 page 14, Article 17(1) | C-41 |
| R-1121 | Where public awareness is needed, the CSIRT designated as coordinator may inform the public, or require the manufacturer to do so, after consulting the manufacturer | regulators and auditors | quality | S-06 page 14, Article 17(2) | C-41 |
| R-1122 | ENISA shall prepare a technical report on emerging trends every 24 months and submit it to the Cooperation Group, and the first report shall be submitted within 24 months of the date of application of Article 14(1) and (3) | regulators and auditors | quality | S-06 page 14, Article 17(3) | C-41 |
| R-1123 | The mere act of notification shall not subject the notifying natural or legal person to increased liability | regulators and auditors | quality | S-06 page 14, Article 17(4) | C-41 |
| R-1124 | After a security update or other measure is available, ENISA shall, in agreement with the manufacturer, add the publicly known vulnerability to the European vulnerability database | regulators and auditors | security | S-06 page 14, Article 17(5) | C-14 |
| R-1125 | The CSIRTs designated as coordinators shall provide helpdesk support on the reporting obligations to manufacturers, in particular microenterprises and small or medium-sized enterprises | regulators and auditors | quality | S-06 page 14, Article 17(6) | C-41 |
| R-1126 | A manufacturer may appoint an authorised representative by a written mandate | management | quality | S-06 page 14, Article 18(1) | C-41 |
| R-1127 | The obligations in Article 13(1) to (11), Article 13(12) first subparagraph, and Article 13(14) shall not form part of the authorised representative mandate | management | quality | S-06 page 14, Article 18(2) | C-41 |
| R-1128 | The authorised representative shall perform the tasks in the mandate and shall provide a copy of the mandate to market surveillance authorities on request | management | quality | S-06 page 14, Article 18(3) | C-41 |
| R-1129 | The mandate shall allow the authorised representative to keep the EU declaration of conformity and the technical documentation at the disposal of market surveillance authorities for at least 10 years or the support period, whichever is longer | management | quality | S-06 page 14, Article 18(3)(a) | C-41 |
| R-1130 | The mandate shall allow the authorised representative to provide information and documentation on a reasoned request, and to cooperate with market surveillance authorities | management | quality | S-06 page 14, Article 18(3)(b) and (c) | C-41 |
| R-1131 | Importers shall place on the market only products that meet Annex I Part I, and only where the manufacturer processes meet Annex I Part II | suppliers | quality | S-06 page 14, Article 19(1) | C-41 |
| R-1132 | Before placing a product on the market, importers shall ensure that the conformity assessment was carried out, the technical documentation was drawn up, the CE marking, EU declaration and Annex II information are present, and the manufacturer met Article 13(15), (16) and (19) | suppliers | quality | S-06 page 14, Article 19(2) | C-41 |
| R-1133 | Importers shall be able to provide the documents that prove fulfilment of the Article 19 requirements | suppliers | quality | S-06 page 14, Article 19(2) | C-41 |
| R-1134 | An importer that considers a product or manufacturer process not in conformity shall not place the product on the market until conformity is achieved | suppliers | quality | S-06 page 14, Article 19(3) | C-41 |
| R-1135 | Where a product presents a significant cybersecurity risk, an importer shall inform the manufacturer and the market surveillance authorities | suppliers | quality | S-06 page 14, Article 19(3) | C-41 |
| R-1136 | Where an importer has reason to believe that a product presents a significant cybersecurity risk from non-technical risk factors, it shall inform the market surveillance authorities | suppliers | quality | S-06 page 14, Article 19(3) | C-41 |
| R-1137 | Importers shall indicate their name, trade name or trademark, postal address, digital contact and, where applicable, website, on the product, its packaging or an accompanying document | suppliers | quality | S-06 page 14, Article 19(4) | C-41 |
| R-1138 | Importers that know or have reason to believe that a product is not in conformity shall immediately take the corrective measures needed, or withdraw or recall the product | suppliers | quality | S-06 page 14, Article 19(5) | C-41 |
| R-1139 | On becoming aware of a vulnerability, importers shall inform the manufacturer without undue delay, and where the product presents a significant cybersecurity risk, shall immediately inform the market surveillance authorities | suppliers | quality | S-06 page 14, Article 19(5) | C-41 |
| R-1140 | Importers shall keep a copy of the EU declaration of conformity and make the technical documentation available to market surveillance authorities for at least 10 years or the support period, whichever is longer | suppliers | quality | S-06 page 14, Article 19(6) | C-41 |
| R-1141 | On a reasoned request, importers shall provide the information and documentation needed to show conformity, and shall cooperate with the authority on measures to eliminate cybersecurity risks | suppliers | quality | S-06 page 14, Article 19(7) | C-41 |
| R-1142 | An importer that becomes aware that the manufacturer has ceased operations shall inform the market surveillance authorities and, as far as possible, the users | suppliers | quality | S-06 page 14, Article 19(8) | C-41 |
| R-1143 | When making a product available on the market, distributors shall act with due care in relation to the requirements of the Regulation | suppliers | quality | S-06 page 14, Article 20(1) | C-41 |
| R-1144 | Before making a product available on the market, distributors shall verify that the product bears the CE marking | suppliers | quality | S-06 page 14, Article 20(2)(a) | C-41 |
| R-1145 | Distributor shall not make a product with digital elements available on the market until the product or the manufacturer's processes are brought into conformity. | suppliers | quality | S-06 page 15, paragraph 3 before Article 21 | C-41 |
| R-1146 | Distributor shall inform the manufacturer and the market surveillance authorities without undue delay where the product poses a significant cybersecurity risk. | suppliers | quality | S-06 page 15, paragraph 3 before Article 21 | C-41 |
| R-1147 | Distributor shall make sure that corrective measures are taken, or that the product is withdrawn or recalled if appropriate, where it knows or has reason to believe the product does not conform. | suppliers | quality | S-06 page 15, paragraph 4 before Article 21 | C-41 |
| R-1148 | Distributor shall inform the manufacturer without undue delay about a vulnerability that it becomes aware of. | suppliers | quality | S-06 page 15, paragraph 4 before Article 21 | C-41 |
| R-1149 | Distributor shall immediately inform the market surveillance authorities of the Member States where a product with significant cybersecurity risk is made available, with details of the non-compliance and corrective measures. | suppliers | quality | S-06 page 15, paragraph 4 before Article 21 | C-41 |
| R-1150 | Distributor shall provide, on reasoned request from a market surveillance authority, the information and documentation that show conformity, in a language that the authority can easily understand. | suppliers | quality | S-06 page 15, paragraph 5 before Article 21 | C-41 |
| R-1151 | Distributor shall cooperate with the market surveillance authority, at its request, on measures to remove cybersecurity risks of products that it made available. | suppliers | quality | S-06 page 15, paragraph 5 before Article 21 | C-41 |
| R-1152 | Distributor shall inform the relevant market surveillance authorities without undue delay where the manufacturer has ceased operations and cannot comply. | suppliers | quality | S-06 page 15, paragraph 6 before Article 21 | C-41 |
| R-1153 | Distributor shall inform users, by any means available and to the extent possible, where the manufacturer has ceased operations and cannot comply. | suppliers | quality | S-06 page 15, paragraph 6 before Article 21 | C-41 |
| R-1154 | Item (b) states a condition that the manufacturer and the importer have complied with listed obligations and given all necessary documents to the distributor; the lead-in is not in the range read. | suppliers | quality | S-06 page 15, item (b) before paragraph 3 | C-41 |
| R-1155 | An importer or distributor shall be considered a manufacturer and shall be subject to Articles 13 and 14 where it places a product on the market under its name or trademark, or carries out a substantial modification. | management | quality | S-06 page 15, Article 21 | C-41 |
| R-1156 | A person other than the manufacturer, importer or distributor that carries out a substantial modification and makes the product available shall be considered a manufacturer. | management | quality | S-06 page 15, Article 22(1) | C-41 |
| R-1157 | Such a person shall be subject to Articles 13 and 14 for the affected part of the product or, where the modification affects cybersecurity as a whole, for the entire product. | management | quality | S-06 page 15, Article 22(2) | C-41 |
| R-1158 | Economic operators shall provide, on request, to market surveillance authorities the name and address of any economic operator that supplied them a product. | suppliers | quality | S-06 page 15, Article 23(1)(a) | C-41 |
| R-1159 | Economic operators shall provide, where available, the name and address of any economic operator to which they supplied a product. | suppliers | quality | S-06 page 15, Article 23(1)(b) | C-41 |
| R-1160 | Economic operators shall be able to present this information for 10 years after they were supplied and for 10 years after they supplied the product. | suppliers | quality | S-06 page 15, Article 23(2) | C-41 |
| R-1161 | Open-source software stewards shall put in place and document in a verifiable manner a cybersecurity policy to foster secure development and effective vulnerability handling by the developers. | software engineers | security | S-06 page 15, Article 24(1) | C-14 |
| R-1162 | The policy shall foster voluntary reporting of vulnerabilities by the developers, as laid down in Article 15, and shall take into account the steward's nature and its legal and organisational arrangements. | software engineers | security | S-06 page 15, Article 24(1) | C-14 |
| R-1163 | The policy shall include aspects of documenting, addressing and remediating vulnerabilities. | software engineers | security | S-06 page 15, Article 24(1) | C-14 |
| R-1164 | The policy shall promote the sharing of information on discovered vulnerabilities within the open-source community. | software engineers | security | S-06 page 15, Article 24(1) | C-14 |
| R-1165 | Open-source software stewards shall cooperate with market surveillance authorities, at their request, to mitigate cybersecurity risks of free and open-source products. | software engineers | quality | S-06 page 15, Article 24(2) | C-41 |
| R-1166 | On reasoned request, open-source software stewards shall provide the policy documentation to the authority, in an easily understood language, in paper or electronic form. | software engineers | quality | S-06 page 15, Article 24(2) | C-41 |
| R-1167 | Article 14(1) shall apply to open-source software stewards to the extent that they are involved in developing the products. | software engineers | quality | S-06 page 15, Article 24(3) | C-41 |
| R-1168 | Article 14(3) and (8) shall apply to open-source software stewards where severe incidents affect network and information systems that they provide for development. | software engineers | quality | S-06 page 15, Article 24(3) | C-41 |
| R-1169 | The Commission shall publish guidance to assist economic operators in applying this Regulation, with a particular focus on microenterprises and small and medium-sized enterprises. | regulators and auditors | quality | S-06 page 15, Article 26(1) | C-41 |
| R-1170 | When preparing guidance, the Commission shall address at least the scope, the support periods, the guidance for products under other Union harmonisation legislation, and the concept of substantial modification. | regulators and auditors | quality | S-06 page 15, Article 26(2) | C-41 |
| R-1171 | The Commission shall maintain an easy-to-access list of the delegated and implementing acts adopted under this Regulation. | regulators and auditors | quality | S-06 page 15, Article 26(2), last paragraph | C-41 |
| R-1172 | The Commission shall consult relevant stakeholders when preparing the guidance. | regulators and auditors | quality | S-06 page 15, Article 26(3) | C-41 |
| R-1173 | The Commission shall request European standardisation organisations to draft harmonised standards for the essential cybersecurity requirements, and shall strive to take existing European and international standards into account. | regulators and auditors | quality | S-06 page 15, Article 27(1), second paragraph | C-41 |
| R-1174 | Implementing acts on common specifications shall be adopted only where the conditions in items (a) and (b) are fulfilled. | regulators and auditors | quality | S-06 page 15, Article 27(2) | C-41 |
| R-1175 | Those implementing acts shall be adopted in accordance with the examination procedure referred to in Article 62(2). | regulators and auditors | quality | S-06 page 16, Article 27(2), last paragraph | C-41 |
| R-1176 | Before preparing the draft implementing act, the Commission shall inform the committee referred to in Article 22 of Regulation (EU) No 1025/2012 that the conditions are fulfilled. | regulators and auditors | quality | S-06 page 16, Article 27(3) | C-41 |
| R-1177 | When preparing the draft implementing act, the Commission shall take into account the views of relevant bodies and shall consult all relevant stakeholders. | regulators and auditors | quality | S-06 page 16, Article 27(4) | C-41 |
| R-1178 | The Commission shall assess a proposed harmonised standard in accordance with Regulation (EU) No 1025/2012 before its reference is published. | regulators and auditors | quality | S-06 page 16, Article 27(6) | C-41 |
| R-1179 | When a reference to a harmonised standard is published, the Commission shall repeal the implementing acts that cover the same essential requirements. | regulators and auditors | quality | S-06 page 16, Article 27(6) | C-41 |
| R-1180 | A Member State that considers a common specification does not fully satisfy the essential requirements shall inform the Commission with a detailed explanation. | regulators and auditors | quality | S-06 page 16, Article 27(7) | C-41 |
| R-1181 | The Commission shall assess that detailed explanation. | regulators and auditors | quality | S-06 page 16, Article 27(7) | C-41 |
| R-1182 | The EU declaration of conformity shall be drawn up by the manufacturer and shall state that the fulfilment of the applicable essential cybersecurity requirements has been demonstrated. | management | quality | S-06 page 16, Article 28(1) | C-41 |
| R-1183 | The EU declaration of conformity shall have the model structure in Annex V and shall contain the elements of the relevant conformity assessment procedures in Annex VIII. | management | quality | S-06 page 16, Article 28(2) | C-41 |
| R-1184 | The EU declaration of conformity shall be updated as appropriate. | management | quality | S-06 page 16, Article 28(2) | C-41 |
| R-1185 | The EU declaration of conformity shall be made available in the languages required by the Member State where the product is placed or made available on the market. | management | quality | S-06 page 16, Article 28(2) | C-41 |
| R-1186 | The simplified EU declaration of conformity shall have the model structure in Annex VI and shall be made available in the languages required by the Member State. | management | quality | S-06 page 16, Article 28(2), second paragraph | C-41 |
| R-1187 | Where more than one Union legal act requires an EU declaration of conformity, a single declaration shall be drawn up that identifies the acts and their publication references. | management | quality | S-06 page 16, Article 28(3) | C-41 |
| R-1188 | By drawing up the EU declaration of conformity, the manufacturer shall assume responsibility for the compliance of the product. | management | quality | S-06 page 16, Article 28(4) | C-41 |
| R-1189 | The CE marking shall be subject to the general principles set out in Article 30 of Regulation (EC) No 765/2008. | management | quality | S-06 page 16, Article 29 | C-41 |
| R-1190 | The CE marking shall be affixed visibly, legibly and indelibly to the product with digital elements. | management | quality | S-06 page 16, Article 30(1) | C-41 |
| R-1191 | Where that is not possible, the CE marking shall be affixed to the packaging and to the EU declaration of conformity. | management | quality | S-06 page 16, Article 30(1) | C-41 |
| R-1192 | For software, the CE marking shall be affixed either to the EU declaration of conformity or on the website accompanying the software, and the relevant section shall be easily and directly accessible to consumers. | management | quality | S-06 page 16, Article 30(1) | C-41 |
| R-1193 | The CE marking shall be affixed before the product with digital elements is placed on the market. | management | quality | S-06 page 16, Article 30(3) | C-41 |
| R-1194 | The CE marking shall be followed by the identification number of the notified body where that body is involved under module H. | regulators and auditors | quality | S-06 page 16, Article 30(4) | C-41 |
| R-1195 | The identification number shall be affixed by the notified body itself or, under its instructions, by the manufacturer or its authorised representative. | regulators and auditors | quality | S-06 page 16, Article 30(4), second paragraph | C-41 |
| R-1196 | Member States shall build upon existing mechanisms to ensure correct application of the CE marking regime and shall take appropriate action in the event of improper use. | regulators and auditors | quality | S-06 page 16, Article 30(5) | C-41 |
| R-1197 | Where other Union harmonisation legislation also provides for CE marking, the CE marking shall indicate that the product also fulfils that legislation. | regulators and auditors | quality | S-06 page 16, Article 30(5) | C-41 |
| R-1198 | When preparing draft implementing acts on labels and marks, the Commission shall consult relevant stakeholders and ADCO. | regulators and auditors | quality | S-06 page 16, Article 30(6) | C-41 |
| R-1199 | The technical documentation shall contain all relevant data or details of the means used to ensure conformity with Annex I, and at least the elements set out in Annex VII. | management | quality | S-06 page 16, Article 31(1) | C-41 |
| R-1200 | The technical documentation shall be drawn up before the product with digital elements is placed on the market. | management | quality | S-06 page 16, Article 31(2) | C-41 |
| R-1201 | The technical documentation shall be continuously updated, where appropriate, at least during the support period. | management | quality | S-06 page 16, Article 31(2) | C-41 |
| R-1202 | For products also subject to other Union legal acts that require technical documentation, a single set of technical documentation shall be drawn up. | management | quality | S-06 page 16, Article 31(3) | C-41 |
| R-1203 | The technical documentation and the correspondence for a conformity assessment shall be drawn up in an official language of the Member State of the notified body, or in a language acceptable to that body. | management | quality | S-06 page 16, Article 31(4) | C-41 |
| R-1204 | The Commission shall strive to ensure that the administrative burden on microenterprises and small and medium-sized enterprises is proportionate when it adds elements to Annex VII. | regulators and auditors | quality | S-06 page 16, Article 31(5) | C-41 |
| R-1205 | The manufacturer shall perform a conformity assessment of the product and of the processes to determine whether the Annex I requirements are met. | management | quality | S-06 page 16, Article 32(1) | C-41 |
| R-1206 | The manufacturer shall demonstrate conformity by using one of the procedures: module A; module B followed by module C; module H; or a European cybersecurity certification scheme, where available and applicable. | management | quality | S-06 page 16, Article 32(1)(a) to (d) | C-41 |
| R-1207 | For an important product of class I, where the harmonised standards, common specifications or certification schemes are not applied, applied only in part, or do not exist, the product and the processes shall be submitted to module B followed by module C, or to module H. | management | quality | S-06 page 16, Article 32(2) | C-41 |
| R-1208 | For an important product of class II, the manufacturer shall demonstrate conformity by using module B followed by module C, module H, or a procedure under item (c) that is not complete in the range read. | management | quality | S-06 page 16, Article 32(3); item (c) continues on page 17, not read | C-41 |
| R-1209 | Products with digital elements shall be designed, developed and produced to ensure an appropriate level of cybersecurity based on the risks | software engineers | security | S-06 page 23 | C-12 |
| R-1210 | On the basis of the cybersecurity risk assessment and where applicable, products with digital elements shall be made available on the market without known exploitable vulnerabilities | software engineers | security | S-06 page 24 | C-11 |
| R-1211 | On the basis of the cybersecurity risk assessment and where applicable, products with digital elements shall be made available on the market with a secure by default configuration, unless agreed otherwise for a tailor-made product, including the possibility to reset to the original state | software engineers | security | S-06 page 24 | C-13 |
| R-1212 | Products with digital elements shall ensure that vulnerabilities can be addressed through security updates, including automatic security updates within an appropriate timeframe enabled by default, with an opt-out, notification and a postpone option | software engineers | security | S-06 page 24 | C-15 |
| R-1213 | Products with digital elements shall ensure protection from unauthorised access by appropriate control mechanisms, and shall report on possible unauthorised access | software engineers | security | S-06 page 24 | C-44 |
| R-1214 | Products with digital elements shall protect the confidentiality of stored, transmitted or processed data, for example by encryption by state of the art mechanisms | software engineers | security | S-06 page 24 | C-44 |
| R-1215 | Products with digital elements shall protect the integrity of data, commands, programs and configuration against unauthorised manipulation, and shall report corruptions | software engineers | security | S-06 page 24 | C-44 |
| R-1216 | Products with digital elements shall process only data that is adequate, relevant and limited to what is necessary for the intended purpose | software engineers | security | S-06 page 24 | C-44 |
| R-1217 | Products with digital elements shall protect the availability of essential and basic functions, also after an incident, including against denial-of-service attacks | software engineers | security | S-06 page 24 | C-44 |
| R-1218 | Products with digital elements shall minimise the negative impact they have on the availability of services of other devices or networks | software engineers | security | S-06 page 24 | C-44 |
| R-1219 | Products with digital elements shall be designed, developed and produced to limit attack surfaces, including external interfaces | software engineers | security | S-06 page 24 | C-13 |
| R-1220 | Products with digital elements shall be designed, developed and produced to reduce the impact of an incident by exploitation mitigation | software engineers | security | S-06 page 24 | C-13 |
| R-1221 | Products with digital elements shall record and monitor relevant internal activity and provide security related information, with an opt-out for the user | software engineers | security | S-06 page 24 | C-44 |
| R-1222 | Products with digital elements shall let users permanently and securely remove all data and settings, and transfer data securely where possible | software engineers | security | S-06 page 24 | C-44 |
| R-1223 | Manufacturers shall identify and document vulnerabilities and components, including a software bill of materials in a machine-readable format covering at least the top-level dependencies | software engineers | security | S-06 page 24 | C-09 |
| R-1224 | Manufacturers shall address and remediate vulnerabilities without delay, including by security updates, and shall provide new security updates separately from functionality updates where technically feasible | software engineers | security | S-06 page 24 | C-14 |
| R-1225 | Manufacturers shall apply effective and regular tests and reviews of the security of the product | software engineers | security | S-06 page 24 | C-17 |
| R-1226 | Manufacturers shall share and publicly disclose information about fixed vulnerabilities once a security update is available, with a delay allowed in duly justified cases until users can apply the patch | software engineers | security | S-06 page 24 | C-14 |
| R-1227 | Manufacturers shall put in place and enforce a policy on coordinated vulnerability disclosure | software engineers | security | S-06 page 24 | C-14 |
| R-1228 | Manufacturers shall take measures to facilitate sharing of information on potential vulnerabilities, including a contact address for reporting | software engineers | security | S-06 page 24 | C-14 |
| R-1229 | Manufacturers shall provide mechanisms to distribute updates securely and in a timely manner, automatically where applicable for security updates | software engineers | security | S-06 page 24 | C-15 |
| R-1230 | Manufacturers shall ensure that security updates are disseminated without delay, free of charge unless agreed otherwise for a tailor-made product, with advisory messages | software engineers | security | S-06 page 24 | C-15 |
| R-1231 | A product with digital elements shall be accompanied by the name, trade name or trademark, postal address, digital contact and, where available, website of the manufacturer | users and customers | quality | S-06 page 24 | C-37 |
| R-1232 | A product with digital elements shall be accompanied by a single point of contact for reporting and receiving vulnerability information, and the location of the coordinated disclosure policy | users and customers | security | S-06 page 24 | C-14 |
| R-1233 | A product with digital elements shall be accompanied by its name, type and any information that enables unique identification | users and customers | operations | S-06 page 24 | C-45 |
| R-1234 | A product with digital elements shall be accompanied by its intended purpose, the security environment provided by the manufacturer, its essential functionalities and its security properties | users and customers | quality | S-06 page 24 | C-37 |
| R-1235 | A product with digital elements shall be accompanied by any known or foreseeable circumstance that may lead to significant cybersecurity risks | users and customers | quality | S-06 page 24 | C-37 |
| R-1236 | A product with digital elements shall be accompanied, where applicable, by the internet address of the EU declaration of conformity | users and customers | quality | S-06 page 24 | C-41 |
| R-1237 | A product with digital elements shall be accompanied by the type of technical security support and the end date of the support period | users and customers | security | S-06 page 25 | C-15 |
| R-1238 | A product with digital elements shall be accompanied by detailed instructions on secure commissioning and use, the effect of changes on data security, how security updates are installed, secure decommissioning, how automatic security updates can be turned off, and, for integration, the information an integrator needs | users and customers | quality | S-06 page 25 | C-37 |
| R-1239 | Protect cardholder name, service code and expiration date when stored, processed or transmitted with PAN, under the cardholder data requirements. | management | security | S-07 page 9 | C-44 |
| R-1240 | If an entity stores, processes or transmits PAN, a CDE exists and PCI DSS requirements will apply. | management | quality | S-07 page 9 | C-41 |
| R-1241 | Requirements related to an incident response plan are applicable to all entities, to ensure that there are procedures to follow in the event of a suspected or actual breach. | operations engineers | operations | S-07 page 9 | C-25 |
| R-1242 | Sensitive authentication data must not be stored after authorization, even if encrypted. | management | security | S-07 page 10 | C-44 |
| R-1243 | If PAN is stored with other cardholder data, only the PAN must be rendered unreadable according to Requirement 3.5.1. | management | security | S-07 page 10 | C-44 |
| R-1244 | Entities are strongly encouraged to keep their software current and updated to the latest software versions available. | software engineers | security | S-07 page 11 | C-10 |
| R-1245 | The entity's PCI DSS assessment should include verification that the software is properly configured and securely implemented to support applicable PCI DSS requirements. | regulators and auditors | quality | S-07 page 11 | C-41 |
| R-1246 | If PCI-listed payment software has been customized, a more in-depth review will be required during the PCI DSS assessment. | regulators and auditors | quality | S-07 page 11 | C-41 |
| R-1247 | Entities that develop their own software are encouraged to refer to PCI SSC software security standards and consider the requirements as best practices. | software engineers | security | S-07 page 11 | C-13 |
| R-1248 | Entities that use software vendors to develop bespoke or custom software are responsible for ensuring those software vendors develop the software according to Requirement 6. | management | security | S-07 page 12 | C-19 |
| R-1249 | PCI DSS Requirement 6 fully applies to bespoke and custom software that has not been developed and maintained under a PCI SSC Software Security Framework standard. | management | quality | S-07 page 12 | C-41 |
| R-1250 | PCI DSS requirements apply to the cardholder data environment and to people, processes and system components that could impact the security of cardholder data or sensitive authentication data. | management | quality | S-07 page 13 | C-41 |
| R-1251 | Anti-phishing processes and automated mechanisms are in place to detect and protect personnel against phishing attacks | security team | security | S-07 page 136 | C-18 |
| R-1252 | Anti-phishing requirement becomes required after 31 March 2025 and must be fully considered during a PCI DSS assessment | management | quality | S-07 page 136 | C-41 |
| R-1253 | Vendor security patches must be installed by the entities that manage the systems | operations engineers | security | S-07 page 138 | C-18 |
| R-1254 | All system components must have all appropriate software patches | operations engineers | security | S-07 page 138 | C-18 |
| R-1255 | Security policies and operational procedures under Requirement 6 are documented, kept up to date, in use and known to all affected parties | management | quality | S-07 page 139 | C-40 |
| R-1256 | Roles and responsibilities for activities in Requirement 6 are documented, assigned and understood | management | quality | S-07 page 140 | C-40 |
| R-1257 | Bespoke and custom software is developed securely, based on industry standards or best practices, in accordance with PCI DSS, with security considered at each lifecycle stage | software engineers | security | S-07 page 141 | C-13 |
| R-1258 | Good practice: PCI DSS requirements must be considered when developing software, by design | software engineers | security | S-07 page 141 | C-12 |
| R-1259 | Software development personnel working on bespoke and custom software are trained at least once every 12 months | software engineers | quality | S-07 page 142 | C-39 |
| R-1260 | Bespoke and custom software is reviewed before release to production or customers, to identify and correct potential coding vulnerabilities | software engineers | security | S-07 page 143 | C-02 |
| R-1261 | Code reviews ensure code is developed according to secure coding guidelines | software engineers | security | S-07 page 143 | C-02 |
| R-1262 | Code reviews look for existing and emerging software vulnerabilities | software engineers | security | S-07 page 143 | C-02 |
| R-1263 | Appropriate corrections are implemented prior to release | software engineers | security | S-07 page 143 | C-02 |
| R-1264 | If manual code reviews are performed, changes are reviewed by individuals other than the originating code author | software engineers | security | S-07 page 144 | C-02 |
| R-1265 | If manual code reviews are performed, reviewers are knowledgeable about code-review techniques and secure coding practices | quality assurance | quality | S-07 page 144 | C-39 |
| R-1266 | If manual code reviews are performed, changes are reviewed and approved by management prior to release | quality assurance | security | S-07 page 144 | C-02 |
| R-1267 | Entities that rely solely on manual code review should ensure that reviewers maintain their skills through regular training | quality assurance | quality | S-07 page 144 | C-39 |
| R-1268 | Software engineering techniques or other methods are defined and in use to prevent or mitigate common software attacks and related vulnerabilities in bespoke and custom software | software engineers | security | S-07 page 145 | C-13 |
| R-1269 | The entity must ensure that code is developed focusing on the prevention or mitigation of common software attacks | software engineers | security | S-07 page 145 | C-13 |
| R-1270 | Developers should be familiar with different types of vulnerabilities and potential attacks, and use measures to avoid potential attack vectors | software engineers | quality | S-07 page 146 | C-39 |
| R-1271 | New security vulnerabilities are identified using industry-recognized sources, including alerts from international and national computer emergency response teams | security team | security | S-07 page 147 | C-14 |
| R-1272 | Vulnerabilities are assigned a risk ranking based on industry best practices and consideration of potential impact | security team | security | S-07 page 147 | C-14 |
| R-1273 | Risk rankings identify, at a minimum, all vulnerabilities considered high-risk or critical to the environment | security team | security | S-07 page 147 | C-14 |
| R-1274 | Vulnerabilities for bespoke and custom software and for third-party software are covered by the process | security team | security | S-07 page 147 | C-14 |
| R-1275 | When assigning risk rankings, an entity should consider using a formal, objective, justifiable methodology | security team | security | S-07 page 147 | C-14 |
| R-1276 | Risk rankings should, at a minimum, identify all vulnerabilities considered high risk to the environment | security team | security | S-07 page 147 | C-14 |
| R-1277 | Processes for managing vulnerabilities should be integrated with other management processes | security team | security | S-07 page 148 | C-14 |
| R-1278 | The vulnerability process should include multiple sources of vulnerability information | security team | security | S-07 page 148 | C-14 |
| R-1279 | Processes should support ongoing evaluation of vulnerabilities | security team | security | S-07 page 148 | C-14 |
| R-1280 | Processes should account for widely published exploits and zero-day attacks | security team | security | S-07 page 149 | C-14 |
| R-1281 | If software is developed in-house, the internal development team should consider sources of information about new vulnerabilities | software engineers | security | S-07 page 149 | C-14 |
| R-1282 | An inventory of bespoke and custom software, and of third-party components in it, is maintained to facilitate vulnerability and patch management. | software engineers | security | S-07 page 151 | C-09 |
| R-1283 | The inventory is used to identify and address vulnerabilities. | software engineers | security | S-07 page 151 | C-09 |
| R-1284 | The inventory should cover all payment software components and dependencies, including execution platforms, third-party libraries, services and other required functions. | software engineers | security | S-07 page 151 | C-09 |
| R-1285 | From 31 March 2025, requirement 6.3.2 is required and must be fully considered during a PCI DSS assessment. | management | quality | S-07 page 151 | C-41 |
| R-1286 | Patches or updates for critical vulnerabilities, ranked per 6.3.1, are installed within one month of release. | operations engineers | security | S-07 page 152 | C-14 |
| R-1287 | All other applicable security patches or updates are installed within an appropriate time frame, as determined by the risk criticality assessment done by the entity. | operations engineers | security | S-07 page 152 | C-14 |
| R-1288 | The patching cadence should factor in re-evaluation of vulnerabilities and later changes in criticality per requirement 6.3.1. | operations engineers | security | S-07 page 152 | C-14 |
| R-1289 | A targeted risk analysis per 12.3.1 is recommended to document the frequency of installing all other applicable security patches or updates. | operations engineers | security | S-07 page 153 | C-14 |
| R-1290 | Public-facing web applications are protected against known attacks, and new threats and vulnerabilities are addressed on an ongoing basis. | operations engineers | security | S-07 page 154 | C-44 |
| R-1291 | Option A: public-facing web applications are reviewed with manual or automated vulnerability assessment tools or methods at least once every 12 months and after significant changes. | security team | security | S-07 page 154 | C-17 |
| R-1292 | Option A: the review is done by an entity that specializes in application security. | security team | security | S-07 page 154 | C-17 |
| R-1293 | Option A: the review includes, at a minimum, all common software attacks in requirement 6.2.4. | security team | security | S-07 page 154 | C-17 |
| R-1294 | Option A: all vulnerabilities are ranked per requirement 6.3.1. | security team | security | S-07 page 154 | C-14 |
| R-1295 | Option A: all vulnerabilities are corrected. | software engineers | security | S-07 page 154 | C-14 |
| R-1296 | Option A: the application is re-evaluated after the corrections. | security team | security | S-07 page 154 | C-17 |
| R-1297 | Option B: an automated technical solution that continually detects and prevents web-based attacks is installed in front of public-facing web applications. | operations engineers | security | S-07 page 154 | C-44 |
| R-1298 | Option B: the solution is actively running and up to date as applicable. | operations engineers | security | S-07 page 154 | C-44 |
| R-1299 | Option B: the solution generates audit logs. | operations engineers | operations | S-07 page 154 | C-23 |
| R-1300 | Option B: the solution is configured to block web-based attacks or to generate an alert that is immediately investigated. | operations engineers | operations | S-07 page 154 | C-23 |
| R-1301 | For public-facing web applications, an automated technical solution is deployed that continually detects and prevents web-based attacks. | operations engineers | security | S-07 page 156 | C-44 |
| R-1302 | The solution is installed in front of public-facing web applications and is configured to detect and prevent web-based attacks. | operations engineers | security | S-07 page 156 | C-44 |
| R-1303 | The solution is actively running and up to date as applicable. | operations engineers | security | S-07 page 156 | C-44 |
| R-1304 | The solution generates audit logs. | operations engineers | operations | S-07 page 156 | C-23 |
| R-1305 | The solution is configured to block web-based attacks or to generate an alert that is immediately investigated. | operations engineers | operations | S-07 page 156 | C-23 |
| R-1306 | Requirement 6.4.2 is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | regulators and auditors | security | S-07 page 156 | C-44 |
| R-1307 | A method is implemented to confirm that each payment page script loaded and executed in the consumer browser is authorized. | software engineers | security | S-07 page 157 | C-10 |
| R-1308 | A method is implemented to assure the integrity of each such script. | software engineers | security | S-07 page 157 | C-16 |
| R-1309 | An inventory of all such scripts is maintained, with a written business or technical justification for each. | software engineers | security | S-07 page 157 | C-09 |
| R-1310 | Where authorization cannot occur before a script is changed or added, the authorization should be confirmed as soon as possible after the change. | software engineers | operations | S-07 page 157 | C-26 |
| R-1311 | The entity should expect the TPSP or payment processor to provide evidence that it meets requirement 6.4.3, per its own PCI DSS assessment and requirement 12.9. | management | security | S-07 page 158 | C-19 |
| R-1312 | Scripts in the TPSP or payment processor embedded payment page are the responsibility of the TPSP or payment processor to manage in accordance with this requirement. | suppliers | security | S-07 page 158 | C-19 |
| R-1313 | Requirement 6.4.3 is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | regulators and auditors | security | S-07 page 158 | C-10 |
| R-1314 | Changes to all system components in production are made according to established procedures that include the reason for and description of the change. | operations engineers | operations | S-07 page 159 | C-26 |
| R-1315 | The change procedures include documentation of security impact. | operations engineers | operations | S-07 page 159 | C-26 |
| R-1316 | The change procedures include documented change approval by authorized parties. | operations engineers | operations | S-07 page 159 | C-26 |
| R-1317 | The change procedures include testing to verify that the change does not adversely impact system security. | operations engineers | operations | S-07 page 159 | C-26 |
| R-1318 | For bespoke and custom software changes, all updates are tested for compliance with requirement 6.2.4 before being deployed into production. | software engineers | operations | S-07 page 159 | C-26 |
| R-1319 | The change procedures include procedures to address failures and return to a secure state. | operations engineers | operations | S-07 page 159 | C-21 |
| R-1320 | Changes should be approved by individuals with the appropriate authority and knowledge to understand the impact of the change. | operations engineers | operations | S-07 page 159 | C-26 |
| R-1321 | Upon completion of a significant change, all applicable PCI DSS requirements are confirmed to be in place on all new or changed systems and networks. | operations engineers | operations | S-07 page 160 | C-26 |
| R-1322 | Documentation is updated as applicable after a significant change. | software engineers | quality | S-07 page 160 | C-37 |
| R-1323 | Significant changes should also be captured and reflected in the annual PCI DSS scope confirmation per requirement 12.5.2. | management | quality | S-07 page 160 | C-41 |
| R-1324 | Pre-production environments are separated from production environments, and the separation is enforced with access controls. | operations engineers | operations | S-07 page 161 | C-22 |
| R-1325 | Organizations must clearly understand which environments are test or development environments and how they interact at network and application level. | operations engineers | operations | S-07 page 161 | C-22 |
| R-1326 | Pre-production environments need to be separated, logically or physically, from production environments so that their vulnerabilities do not adversely affect production systems. | operations engineers | operations | S-07 page 161 | C-22 |
| R-1327 | Roles and functions are separated between production and pre-production environments to provide accountability, so that only reviewed and approved changes are deployed. | operations engineers | security | S-07 page 162 | C-08 |
| R-1328 | Live PANs are not used in pre-production environments, except where those environments are in a CDE and protected per all applicable PCI DSS requirements. | operations engineers | operations | S-07 page 163 | C-22 |
| R-1329 | All PANs must be verified as unable to conduct payment transactions or pose fraud risk before they are excluded from PCI DSS scope. | operations engineers | operations | S-07 page 163 | C-22 |
| R-1330 | It is the responsibility of the entity to confirm that PANs are not live. | management | operations | S-07 page 163 | C-22 |
| R-1331 | Test data and test accounts are removed from system components before the system goes into production. | software engineers | security | S-07 page 164 | C-13 |
| R-1332 | Systems and processes must be in place to limit access to critical data based on need to know and job responsibilities. | operations engineers | security | S-07 page 165 | C-44 |
| R-1333 | Audit logs must exist for all system components. | operations engineers | operations | S-07 page 243 (10.2.1 summary) | C-23 |
| R-1334 | Audit logs are enabled and active for all system components and cardholder data. | operations engineers | operations | S-07 page 243 (10.2.1) | C-23 |
| R-1335 | Audit logs capture all individual user access to cardholder data. | operations engineers | operations | S-07 page 243 (10.2.1.1) | C-23 |
| R-1336 | Audit logs capture all actions taken by any individual with administrative access, including interactive use of application or system accounts. | operations engineers | operations | S-07 page 244 (10.2.1.2) | C-23 |
| R-1337 | Audit logs capture all access to audit logs. | operations engineers | operations | S-07 page 244 (10.2.1.3) | C-23 |
| R-1338 | Audit logs capture all invalid logical access attempts. | operations engineers | operations | S-07 page 244 (10.2.1.4) | C-23 |
| R-1339 | Audit logs capture all changes to identification and authentication credentials, including creation of accounts, elevation of privileges and changes to accounts with administrative access. | operations engineers | operations | S-07 page 246 (10.2.1.5) | C-23 |
| R-1340 | Audit logs capture all initialization, starting, stopping or pausing of audit logs. | operations engineers | operations | S-07 page 246 (10.2.1.6) | C-23 |
| R-1341 | Audit logs capture all creation and deletion of system-level objects. | operations engineers | operations | S-07 page 247 (10.2.1.7) | C-23 |
| R-1342 | Audit logs record user identification, type of event, date and time, success or failure, origination of event, and identity of affected data, component, resource or service, for each auditable event. | operations engineers | operations | S-07 page 247 (10.2.2) | C-23 |
| R-1343 | Read access to audit log files is limited to those with a job-related need. | operations engineers | operations | S-07 page 248 (10.3.1) | C-23 |
| R-1344 | Audit log files are protected from modification by individuals through access control, physical segregation and/or network segregation. | operations engineers | operations | S-07 page 249 (10.3.2) | C-23 |
| R-1345 | Audit log files, including those for external-facing technologies, are promptly backed up to a secure, central, internal log server or other media that is difficult to modify. | operations engineers | operations | S-07 page 249 (10.3.3) | C-23 |
| R-1346 | File integrity monitoring or change-detection mechanisms are used on audit logs so that existing log data cannot be changed without generating alerts. | operations engineers | operations | S-07 page 250 (10.3.4) | C-23 |
| R-1347 | The following audit logs are reviewed at least once daily: all security events; logs of system components that store, process or transmit CHD and/or SAD; logs of all critical system components; logs of servers and components that perform security functions. | operations engineers | operations | S-07 page 251 (10.4.1) | C-23 |
| R-1348 | Automated mechanisms are used to perform audit log reviews; this is a best practice until 31 March 2025, after which it will be required. | operations engineers | operations | S-07 page 252 (10.4.1.1) | C-23 |
| R-1349 | Logs of all other system components (not specified in 10.4.1) are reviewed periodically. | operations engineers | operations | S-07 page 253 (10.4.2) | C-23 |
| R-1350 | The frequency of periodic log reviews for other components is defined in the entity's targeted risk analysis, performed according to all elements of 12.3.1; this is a best practice until 31 March 2025. | operations engineers | operations | S-07 page 254 (10.4.2.1) | C-23 |
| R-1351 | Exceptions and anomalies identified during the review process are addressed. | operations engineers | operations | S-07 page 255 (10.4.3) | C-23 |
| R-1352 | Audit log history is retained for at least 12 months, with at least the most recent three months immediately available for analysis. | operations engineers | operations | S-07 page 256 (10.5.1) | C-23 |
| R-1353 | Information stored in audit logs is sensitive and should be protected per the requirements of this standard. | operations engineers | operations | S-07 page 243 (10.2.1 guidance) | C-23 |
| R-1354 | Care should be taken to store only essential information in audit logs to minimize risk. | operations engineers | security | S-07 page 243 (10.2.1 guidance) | C-44 |
| R-1355 | Audit logs should be protected on the originating systems as well as anywhere else they are stored. | operations engineers | operations | S-07 page 249 (10.3.2 purpose) | C-23 |
| R-1356 | Entities should attempt to prevent logs from being exposed in publicly accessible locations. | operations engineers | operations | S-07 page 249 (10.3.2 guidance) | C-23 |
| R-1357 | Software used to monitor audit logs should be configured to alert when existing log data or files are changed or deleted. | operations engineers | operations | S-07 page 250 (10.3.4 guidance) | C-23 |
| R-1358 | An entity that uses third-party service providers for log review is responsible for providing context about the entity's environment to them. | suppliers | security | S-07 page 251 (10.4.1 guidance) | C-19 |
| R-1359 | Entities should keep logging tools aligned with changes in their environment by periodically reviewing and updating tool settings. | operations engineers | operations | S-07 page 252 (10.4.1.1 guidance) | C-23 |
| R-1360 | Entities should consider how to record, rank, escalate and assign responsibility for exceptions and anomalies when they define their processes. | operations engineers | operations | S-07 page 255 (10.4.3 guidance) | C-23 |
| R-1361 | Internal vulnerability scans are performed at least once every three months. | security team | security | S-07 page 270 (11.3.1) | C-11 |
| R-1362 | Vulnerabilities that are high-risk or critical under the ranking of Requirement 6.3.1 are resolved after internal scans. | security team | security | S-07 page 270 (11.3.1) | C-11 |
| R-1363 | Rescans are performed to confirm that all high-risk and all critical vulnerabilities are resolved. | security team | security | S-07 page 270 (11.3.1) | C-11 |
| R-1364 | The internal scan tool is kept up to date with the latest vulnerability information. | security team | security | S-07 page 270 (11.3.1) | C-11 |
| R-1365 | Internal scans are performed by qualified personnel, and organisational independence of the tester exists. | security team | security | S-07 page 270 (11.3.1) | C-11 |
| R-1366 | Good practice: vulnerabilities posing the greatest risk should be resolved with the highest priority. | security team | security | S-07 page 270 (11.3.1) | C-14 |
| R-1367 | Good practice: vulnerabilities identified during internal scans should be part of a vulnerability management process that includes multiple vulnerability sources. | security team | security | S-07 page 270 (11.3.1) | C-14 |
| R-1368 | A network administrator should not be responsible for scanning the network. | operations engineers | security | S-07 page 271 (applicability notes) | C-08 |
| R-1369 | Other applicable vulnerabilities are addressed based on the risk defined in the targeted risk analysis of the entity, performed under Requirement 12.3.1. | security team | security | S-07 page 272 (11.3.1.1) | C-14 |
| R-1370 | Rescans are conducted as needed for other applicable vulnerabilities. | security team | security | S-07 page 272 (11.3.1.1) | C-11 |
| R-1371 | Lower-ranked vulnerabilities are addressed at a frequency in accordance with the risk of the entity. | security team | security | S-07 page 272 (11.3.1.1, customized approach objective) | C-14 |
| R-1372 | The timeframe for lower-risk vulnerabilities is subject to a risk analysis under Requirement 12.3.1 that includes minimally the assets being protected, threats, and likelihood or impact of a threat. | security team | security | S-07 page 272 (11.3.1.1, applicability notes) | C-14 |
| R-1373 | Internal vulnerability scans are performed via authenticated scanning. | security team | security | S-07 page 273 (11.3.1.2) | C-11 |
| R-1374 | Systems that are unable to accept credentials for authenticated scanning are documented. | security team | security | S-07 page 273 (11.3.1.2) | C-11 |
| R-1375 | Sufficient privileges are used for systems that accept credentials for scanning. | security team | security | S-07 page 273 (11.3.1.2) | C-11 |
| R-1376 | Accounts used for authenticated scanning that can be used for interactive login are managed in accordance with Requirement 8.2.2. | security team | security | S-07 page 273 (11.3.1.2) | C-08 |
| R-1377 | Good practice: the credentials used for these scans should be considered highly privileged and should be protected and controlled as such, following Requirements 7 and 8. | security team | security | S-07 page 273 (11.3.1.2) | C-08 |
| R-1378 | Internal vulnerability scans are performed after any significant change. | security team | security | S-07 page 274 (11.3.1.3) | C-11 |
| R-1379 | Vulnerabilities that are high-risk or critical under Requirement 6.3.1 are resolved after such scans. | security team | security | S-07 page 274 (11.3.1.3) | C-14 |
| R-1380 | Rescans are conducted as needed after significant change. | security team | security | S-07 page 274 (11.3.1.3) | C-11 |
| R-1381 | Scans after significant change are performed by qualified personnel, and organisational independence of the tester exists (not required to be a QSA or ASV). | security team | security | S-07 page 274 (11.3.1.3) | C-11 |
| R-1382 | Good practice: entities should perform scans after significant changes as part of the change process under Requirement 6.5.2 and before considering the change complete. | operations engineers | operations | S-07 page 274 (11.3.1.3, good practice) | C-26 |
| R-1383 | All system components affected by a change will need to be scanned. | security team | security | S-07 page 274 (11.3.1.3, good practice) | C-11 |
| R-1384 | External vulnerability scans are performed at least once every three months. | security team | security | S-07 page 275 (11.3.2) | C-11 |
| R-1385 | External vulnerability scans are performed by a PCI SSC Approved Scanning Vendor (ASV). | security team | security | S-07 page 275 (11.3.2) | C-11 |
| R-1386 | Vulnerabilities are resolved, and the ASV Program Guide requirements for a passing scan are met. | security team | security | S-07 page 275 (11.3.2) | C-11 |
| R-1387 | Rescans are performed as needed to confirm that vulnerabilities are resolved, per the ASV Program Guide. | security team | security | S-07 page 275 (11.3.2) | C-11 |
| R-1388 | For the initial assessment, four passing scans need not be completed within 12 months if the assessor verifies the three conditions stated in the source. | regulators and auditors | quality | S-07 page 275 (11.3.2, applicability notes) | C-41 |
| R-1389 | Good practice: vulnerabilities found by external scans should be part of a vulnerability management process that includes multiple sources. | security team | security | S-07 page 275 (11.3.2, good practice) | C-14 |
| R-1390 | For subsequent years after the initial assessment, passing scans at least every three months must have occurred. | regulators and auditors | quality | S-07 page 276 (11.3.2, applicability notes) | C-41 |
| R-1391 | Specifics about the target environment should be worked out between the ASV and the scan customer. | suppliers | security | S-07 page 276 (11.3.2, guidance) | C-19 |
| R-1392 | External vulnerability scans are performed after any significant change. | security team | security | S-07 page 277 (11.3.2.1) | C-11 |
| R-1393 | Vulnerabilities scored 4.0 or higher by CVSS are resolved after such scans. | security team | security | S-07 page 277 (11.3.2.1) | C-14 |
| R-1394 | Rescans are conducted as needed after significant change. | security team | security | S-07 page 277 (11.3.2.1) | C-11 |
| R-1395 | External scans after significant change are performed by qualified personnel, and organisational independence of the tester exists (not required to be a QSA or ASV). | security team | security | S-07 page 277 (11.3.2.1) | C-11 |
| R-1396 | Good practice: entities should include the need to perform scans after significant changes as part of the change process, before the change is considered complete. | operations engineers | operations | S-07 page 277 (11.3.2.1, good practice) | C-26 |
| R-1397 | A penetration testing methodology is defined, documented and implemented by the entity, and includes industry-accepted penetration testing approaches. | security team | security | S-07 page 278 (11.4.1) | C-17 |
| R-1398 | The penetration testing methodology covers the entire CDE perimeter and critical systems. | security team | security | S-07 page 278 (11.4.1) | C-17 |
| R-1399 | The penetration testing methodology includes testing from both inside and outside the network. | security team | security | S-07 page 278 (11.4.1) | C-17 |
| R-1400 | The penetration testing methodology includes testing to validate segmentation and scope-reduction controls. | security team | security | S-07 page 278 (11.4.1) | C-17 |
| R-1401 | The penetration testing methodology includes application-layer penetration testing to identify, at a minimum, the vulnerabilities listed in Requirement 6.2.4. | security team | security | S-07 page 278 (11.4.1) | C-17 |
| R-1402 | The penetration testing methodology includes network-layer penetration tests that cover all components that support network functions, as well as operating systems. | security team | security | S-07 page 278 (11.4.1) | C-17 |
| R-1403 | The penetration testing methodology includes review and consideration of threats and vulnerabilities experienced in the last 12 months. | security team | security | S-07 page 278 (11.4.1) | C-17 |
| R-1404 | The penetration testing methodology includes a documented approach to assessing and addressing the risk posed by exploitable vulnerabilities and security weaknesses found. | security team | security | S-07 page 278 (11.4.1) | C-17 |
| R-1405 | The penetration testing methodology includes retention of penetration testing results and remediation results for at least 12 months. | security team | security | S-07 page 278 (11.4.1) | C-17 |
| R-1406 | Good practice: penetration testing techniques should be suitable for the tested environment, and the type, depth and complexity of testing depend on that environment. | security team | security | S-07 page 278 (11.4.1, good practice) | C-17 |
| R-1407 | Internal penetration testing is performed per the methodology of the entity. | security team | security | S-07 page 280 (11.4.2) | C-17 |
| R-1408 | Internal penetration testing is performed at least once every 12 months. | security team | security | S-07 page 280 (11.4.2) | C-17 |
| R-1409 | Internal penetration testing is performed after any significant infrastructure or application upgrade or change. | security team | security | S-07 page 280 (11.4.2) | C-17 |
| R-1410 | Internal penetration testing is performed by a qualified internal resource or a qualified external third party, and organisational independence of the tester exists (not required to be a QSA or ASV). | security team | security | S-07 page 280 (11.4.2) | C-17 |
| R-1411 | External penetration testing is performed per the methodology of the entity. | security team | security | S-07 page 281 (11.4.3) | C-17 |
| R-1412 | External penetration testing is performed at least once every 12 months. | security team | security | S-07 page 281 (11.4.3) | C-17 |
| R-1413 | External penetration testing is performed after any significant infrastructure or application upgrade or change. | security team | security | S-07 page 281 (11.4.3) | C-17 |
| R-1414 | External penetration testing is performed by a qualified internal resource or a qualified external third party, and organisational independence of the tester exists (not required to be a QSA or ASV). | security team | security | S-07 page 281 (11.4.3) | C-17 |
| R-1415 | Good practice: when choosing a qualified resource, consider certifications and prior experience. | security team | security | S-07 page 281 (11.4.3, good practice) | C-17 |
| R-1416 | Exploitable vulnerabilities and security weaknesses found in penetration testing are corrected in accordance with the risk assessment of the entity under Requirement 6.3.1. | security team | security | S-07 page 282 (11.4.4) | C-14 |
| R-1417 | Penetration testing is repeated to verify the corrections. | security team | security | S-07 page 282 (11.4.4) | C-17 |
| R-1418 | Good practice: entities should consider how likely the vulnerability is to be exploited and whether other controls reduce the risk. | security team | security | S-07 page 282 (11.4.4, good practice) | C-14 |
| R-1419 | Good practice: any weaknesses that point to PCI DSS requirements not being met should be addressed. | security team | security | S-07 page 282 (11.4.4, good practice) | C-14 |
| R-1420 | If segmentation is used to isolate the CDE, penetration tests on segmentation controls are performed at least once every 12 months and after any changes to segmentation controls or methods. | security team | security | S-07 page 283 (11.4.5) | C-17 |
| R-1421 | Penetration tests on segmentation cover all segmentation controls or methods in use. | security team | security | S-07 page 283 (11.4.5) | C-17 |
| R-1422 | Penetration tests on segmentation follow the penetration testing methodology of the entity. | security team | security | S-07 page 283 (11.4.5) | C-17 |
| R-1423 | Penetration tests on segmentation confirm that segmentation controls are operational and effective, and isolate the CDE from all out-of-scope systems. | security team | security | S-07 page 283 (11.4.5) | C-17 |
| R-1424 | Segmentation penetration tests are performed by a qualified internal resource or a qualified external third party, and organisational independence of the tester exists (not required to be a QSA or ASV). | security team | security | S-07 page 283 (11.4.5) | C-17 |
| R-1425 | Good practice: confirm the effectiveness of any use of isolation to separate systems with differing security levels (see Requirement 2.2.3). | security team | security | S-07 page 283 (11.4.5, good practice) | C-17 |
| R-1426 | If segmentation is used, it is verified periodically by technical testing to be continually effective, including after any changes, in isolating the CDE from all out-of-scope systems. | security team | security | S-07 page 283 (11.4.5, customized approach objective) | C-17 |
| R-1427 | Service providers only: if segmentation is used to isolate the CDE, penetration tests on segmentation controls are performed at least once every six months and after any changes to segmentation controls or methods. | security team | security | S-07 page 284 (11.4.6) | C-17 |
| R-1428 | Service provider segmentation penetration tests cover all segmentation controls or methods, follow the defined methodology, and confirm the CDE is isolated from all out-of-scope systems. | security team | security | S-07 page 284 (11.4.6) | C-17 |
| R-1429 | Service provider segmentation penetration tests are performed by a qualified internal resource or a qualified external third party, with organisational independence of the tester (not required to be a QSA or ASV). | security team | security | S-07 page 284 (11.4.6) | C-17 |
| R-1430 | Good practice: segmentation validation should be performed as frequently as possible. | security team | security | S-07 page 284 (11.4.6, good practice) | C-17 |
| R-1431 | Multi-tenant service providers only: support their customers for external penetration testing per Requirements 11.4.3 and 11.4.4. | suppliers | security | S-07 page 285 (11.4.7) | C-19 |
| R-1432 | Multi-tenant service providers cannot forbid penetration testing. | suppliers | security | S-07 page 285 (11.4.7, customized approach objective) | C-19 |
| R-1433 | Multi-tenant service providers must support customer requests to conduct penetration testing or for penetration testing results. | suppliers | security | S-07 page 285 (11.4.7, customized approach objective) | C-19 |
| R-1434 | Multi-tenant service providers either provide evidence to customers that penetration testing was performed per Requirements 11.4.3 and 11.4.4, or provide prompt access so customers can perform their own penetration testing. | suppliers | security | S-07 page 286 (11.4.7, applicability notes) | C-19 |
| R-1435 | Evidence provided to customers can include redacted penetration testing results, but needs to include sufficient information to prove that all elements of Requirements 11.4.3 and 11.4.4 are met on the customer's behalf. | suppliers | security | S-07 page 286 (11.4.7, applicability notes) | C-19 |
| R-1436 | Maintain an incident response plan that is ready to activate for a suspected or confirmed security incident (12.10.1) | security team | operations | S-07 page 331 | C-25 |
| R-1437 | The incident response plan must be disseminated, read, and understood by the parties responsible (12.10.1) | security team | operations | S-07 page 331 | C-25 |
| R-1438 | The incident response plan must include roles, responsibilities, and communication and contact strategies, including notification of payment brands and acquirers at a minimum (12.10.1) | security team | operations | S-07 page 331 | C-25 |
| R-1439 | The incident response plan must include incident response procedures with containment and mitigation activities for different incident types (12.10.1) | security team | operations | S-07 page 331 | C-25 |
| R-1440 | The incident response plan must include business recovery and continuity procedures and data backup processes (12.10.1) | operations engineers | operations | S-07 page 331 | C-27 |
| R-1441 | The incident response plan must include analysis of legal requirements for reporting compromises (12.10.1) | security team | operations | S-07 page 331 | C-25 |
| R-1442 | The incident response plan must cover all critical system components and reference or include payment brand procedures (12.10.1) | security team | operations | S-07 page 331 | C-25 |
| R-1443 | The incident response plan should be thorough and contain all key elements for stakeholders such as legal and communications (guidance, 12.10.1) | security team | operations | S-07 page 331 | C-25 |
| R-1444 | Entities should consider how to address all compromises of data within the CDE in their incident response plans (guidance, 12.10.1) | security team | operations | S-07 page 331 | C-25 |
| R-1445 | The incident response plan must be reviewed and its content updated as needed, at least once every 12 months (12.10.2) | security team | operations | S-07 page 332 | C-25 |
| R-1446 | The incident response plan must be tested at least once every 12 months, including all elements of 12.10.1 (12.10.2) | security team | operations | S-07 page 332 | C-25 |
| R-1447 | Specific personnel must be designated to be available on a 24/7 basis to respond to suspected or confirmed security incidents (12.10.3) | operations engineers | operations | S-07 page 333 | C-25 |
| R-1448 | Personnel responsible for responding to incidents must be appropriately and periodically trained on their incident response responsibilities (12.10.4) | security team | quality | S-07 page 334 | C-39 |
| R-1449 | The training frequency must be defined in the entity's targeted risk analysis, performed per Requirement 12.3.1 (12.10.4.1, best practice until 31 March 2025) | security team | quality | S-07 page 334 | C-39 |
| R-1450 | The incident response plan must include monitoring and responding to alerts from security monitoring systems, as listed (12.10.5) | security team | operations | S-07 page 335 | C-25 |
| R-1451 | The incident response plan must be modified and evolved according to lessons learned and to incorporate industry developments (12.10.6) | security team | operations | S-07 page 336 | C-25 |
| R-1452 | The lessons-learned exercise should include all levels of personnel and should focus on how the response could be improved (guidance, 12.10.6) | security team | operations | S-07 page 336 | C-25 |
| R-1453 | Incident response procedures must be in place for stored PAN found where it is not expected, including retrieval, secure deletion, or migration into the defined CDE (12.10.7, best practice until 31 March 2025) | security team | operations | S-07 page 337 | C-25 |
| R-1454 | Analysis should determine whether sensitive authentication data is stored with PAN, identify the data source, and identify control gaps (guidance, 12.10.7) | security team | operations | S-07 page 337 | C-25 |
| R-1455 | Contributory factors should be addressed per this Requirement to prevent recurrence (guidance, 12.10.7) | security team | operations | S-07 page 337 | C-25 |
| R-1456 | Ensure no single human or programmatic entity can ship sensitive code or artifacts without external verification or validation. | software engineers | security | S-09 CICD-SEC-01, Recommendations, item 1 | C-02 |
| R-1457 | Prevent accounts from triggering production build and deployment pipelines without additional approval, where applicable. | software engineers | security | S-09 CICD-SEC-01, Recommendations, item 2 | C-02 |
| R-1458 | Prevent artifacts uploaded by other accounts from flowing through the pipeline without secondary review and approval. | software engineers | security | S-09 CICD-SEC-01, Recommendations, item 3 | C-02 |
| R-1459 | Detect and prevent drift between production code and its CI/CD origin, and fix any drifted resources. | operations engineers | operations | S-09 CICD-SEC-01, Recommendations, item 4 | C-20 |
| R-1460 | Ensure that where accounts can push unreviewed code, they cannot trigger the deployment pipelines for that repository. | operations engineers | security | S-09 CICD-SEC-01, Recommendations, item 5 | C-06 |
| R-1461 | Ensure auto-merge rules cannot be bypassed, after thorough code review of those rules. | software engineers | security | S-09 CICD-SEC-01, Recommendations, item 6 | C-02 |
| R-1462 | Configure branch protection on branches that feed production or sensitive systems, and avoid excluding users or branches where possible. | software engineers | security | S-09 CICD-SEC-01, Recommendations, softer list, item 1 | C-01 |
| R-1463 | Limit auto-merge rules to the smallest possible set of contexts. | software engineers | security | S-09 CICD-SEC-01, Recommendations, softer list, item 2 | C-02 |
| R-1464 | Avoid importing third-party code into the auto-merge process. | software engineers | security | S-09 CICD-SEC-01, Recommendations, softer list, item 3 | C-10 |
| R-1465 | Prefer allowing artifacts only when a pre-approved CI service account created them. | operations engineers | security | S-09 CICD-SEC-01, Recommendations, softer list, item 4 | C-16 |
| R-1466 | Continuously map all identities across systems, including the identity provider, granted permissions and used permissions, covering all programmatic access. | security team | security | S-09 CICD-SEC-02, Recommendations, item 1 | C-08 |
| R-1467 | Remove unnecessary permissions from every identity across all systems. | security team | security | S-09 CICD-SEC-02, Recommendations, item 2 | C-08 |
| R-1468 | Define an inactivity period and disable or remove identities that exceed it. | security team | security | S-09 CICD-SEC-02, Recommendations, item 3 | C-08 |
| R-1469 | Avoid local accounts, manage identities through a centralized identity provider, and disable local accounts that are no longer needed. | security team | security | S-09 CICD-SEC-02, Recommendations, item 4 | C-08 |
| R-1470 | Continuously map external collaborators, enforce least privilege, set expiry dates where possible, and disable accounts when work ends. | security team | security | S-09 CICD-SEC-02, Recommendations, item 5 | C-08 |
| R-1471 | Prohibit non-domain email addresses on SCM, CI and other CI/CD platforms, monitor for them, and remove non-compliant users. | security team | security | S-09 CICD-SEC-02, Recommendations, item 6 | C-08 |
| R-1472 | Do not allow self-registration, and grant access only as needed. | security team | security | S-09 CICD-SEC-02, Recommendations, item 7 | C-08 |
| R-1473 | Do not grant base permissions to all users or to large auto-assigned groups. | security team | security | S-09 CICD-SEC-02, Recommendations, item 8 | C-08 |
| R-1474 | Avoid shared accounts, and create dedicated accounts per context with the exact permissions required. | security team | security | S-09 CICD-SEC-02, Recommendations, item 9 | C-08 |
| R-1475 | Clients should not fetch packages directly from the internet or untrusted sources. | software engineers | security | S-09 CICD-SEC-03, Recommendations, item 1 | C-10 |
| R-1476 | Pull third-party packages through an internal proxy. | software engineers | security | S-09 CICD-SEC-03, Recommendations, item 2 | C-10 |
| R-1477 | Where applicable, disallow direct external pulls, configure clients to use internal pre-vetted repositories, and enforce that configuration. | software engineers | security | S-09 CICD-SEC-03, Recommendations, item 3 | C-10 |
| R-1478 | Enable checksum and signature verification for pulled packages. | software engineers | security | S-09 CICD-SEC-03, Recommendations, item 4 | C-10 |
| R-1479 | Avoid pulling latest versions, and pin and lock pre-vetted versions or version ranges. | software engineers | security | S-09 CICD-SEC-03, Recommendations, item 5 | C-10 |
| R-1480 | Register all private packages under the organization scope, reference them by that scope, and force clients to fetch scoped packages only from the internal registry. | software engineers | security | S-09 CICD-SEC-03, Recommendations, item 6 | C-10 |
| R-1481 | Run install scripts in a separate context without access to secrets or sensitive resources. | operations engineers | security | S-09 CICD-SEC-03, Recommendations, item 7 | C-06 |
| R-1482 | Commit package manager configuration files to project repositories to override insecure client settings. | software engineers | security | S-09 CICD-SEC-03, Recommendations, item 8 | C-10 |
| R-1483 | Do not publish internal project names in public repositories. | software engineers | security | S-09 CICD-SEC-03, Recommendations, item 9 | C-10 |
| R-1484 | Prioritize detection, monitoring and mitigation, and harden systems per CICD-SEC-7. | operations engineers | security | S-09 CICD-SEC-03, Recommendations, item 10 | C-18 |
| R-1485 | Run pipelines that execute unreviewed code on isolated nodes, not exposed to secrets or sensitive environments. | operations engineers | security | S-09 CICD-SEC-04, Recommendations, item 1 | C-05 |
| R-1486 | Evaluate whether external-contributor pipelines on public repositories are needed, and where possible do not run fork pipelines. | operations engineers | security | S-09 CICD-SEC-04, Recommendations, item 2 | C-06 |
| R-1487 | For sensitive pipelines, ensure each branch that triggers a pipeline has a matching branch protection rule in the SCM. | software engineers | security | S-09 CICD-SEC-04, Recommendations, item 3 | C-01 |
| R-1488 | Each CI configuration file must be reviewed before the pipeline runs, or be kept on a separate protected branch from the code being built. | software engineers | security | S-09 CICD-SEC-04, Recommendations, item 4 | C-02 |
| R-1489 | Remove SCM repository permissions from users who do not need them. | operations engineers | security | S-09 CICD-SEC-04, Recommendations, item 5 | C-08 |
| R-1490 | Each pipeline should have access only to the credentials it needs, with minimum required privileges. | operations engineers | security | S-09 CICD-SEC-04, Recommendations, item 6 | C-06 |
| R-1491 | Do not share execution nodes between pipelines with different sensitivity levels, and share them only among pipelines with identical confidentiality. | operations engineers | security | S-09 CICD-SEC-05, Recommendations, item 1 | C-05 |
| R-1492 | Scope CI/CD secrets so each pipeline and step gets only what it needs. | operations engineers | security | S-09 CICD-SEC-05, Recommendations, item 2 | C-07 |
| R-1493 | Reset execution nodes to a clean state after each run. | operations engineers | security | S-09 CICD-SEC-05, Recommendations, item 3 | C-05 |
| R-1494 | Give the pipeline operating system user only the minimum permissions on the execution node. | operations engineers | security | S-09 CICD-SEC-05, Recommendations, item 4 | C-18 |
| R-1495 | Limit pipeline job permissions on the controller node, and run jobs on separate dedicated nodes where possible. | operations engineers | security | S-09 CICD-SEC-05, Recommendations, item 5 | C-06 |
| R-1496 | Keep execution nodes patched. | operations engineers | security | S-09 CICD-SEC-05, Recommendations, item 6 | C-18 |
| R-1497 | Segment the network so execution nodes reach only required resources, and avoid unrestricted internet access where possible. | operations engineers | security | S-09 CICD-SEC-05, Recommendations, item 7 | C-18 |
| R-1498 | Isolate install scripts from secrets and sensitive resources used in other build stages. | operations engineers | security | S-09 CICD-SEC-05, Recommendations, item 8 | C-06 |
| R-1499 | Continuously map credentials across the engineering ecosystem and enforce least privilege. | operations engineers | security | S-09 CICD-SEC-06, Recommendations, item 1 | C-08 |
| R-1500 | Avoid sharing one set of credentials across multiple contexts. | operations engineers | security | S-09 CICD-SEC-06, Recommendations, item 2 | C-07 |
| R-1501 | Prefer temporary credentials over static ones, and if static credentials are needed, rotate them periodically and detect stale ones. | operations engineers | security | S-09 CICD-SEC-06, Recommendations, item 3 | C-07 |
| R-1502 | Limit credential use to predefined conditions, such as a specific source IP address or identity. | operations engineers | security | S-09 CICD-SEC-06, Recommendations, item 4 | C-07 |
| R-1503 | Detect secrets in repositories with IDE plugins, scans on each push, and periodic scans of history. | software engineers | security | S-09 CICD-SEC-06, Recommendations, item 5 | C-11 |
| R-1504 | Scope CI/CD secrets so each pipeline and step can access only what it requires. | operations engineers | security | S-09 CICD-SEC-06, Recommendations, item 6 | C-07 |
| R-1505 | Prevent secrets from being printed to console output using vendor or third-party tools, and check existing outputs. | operations engineers | security | S-09 CICD-SEC-06, Recommendations, item 7 | C-07 |
| R-1506 | Verify that secrets are removed from artifacts such as container image layers, binaries and Helm charts. | software engineers | security | S-09 CICD-SEC-06, Recommendations, item 8 | C-07 |
| R-1507 | Maintain an inventory of systems and versions with a named owner for each, continuously check for known vulnerabilities, and apply patches when available. | operations engineers | security | S-09 CICD-SEC-07, Recommendations, item 1 | C-18 |
| R-1508 | Where no patch exists, remove the component or restrict its access and sensitive operations. | operations engineers | security | S-09 CICD-SEC-07, Recommendations, item 1 | C-18 |
| R-1509 | Align network access with the principle of least access. | operations engineers | security | S-09 CICD-SEC-07, Recommendations, item 2 | C-18 |
| R-1510 | Periodically review all system configurations and ensure they are optimal. | operations engineers | security | S-09 CICD-SEC-07, Recommendations, item 3 | C-18 |
| R-1511 | Apply least privilege to pipeline execution nodes. | operations engineers | security | S-09 CICD-SEC-07, Recommendations, item 4 | C-18 |
| R-1512 | Vetting procedures should ensure third parties are approved before access is granted, with permissions aligned to least privilege. | operations engineers | security | S-09 CICD-SEC-08, Recommendations, item 1 | C-18 |
| R-1513 | Controls should maintain continuous visibility over all integrations, including the integration method, the permissions granted and the permissions used. | operations engineers | security | S-09 CICD-SEC-08, Recommendations, item 2 | C-18 |
| R-1514 | Each third party should be scoped to the specific resources it needs, and unused or redundant permissions should be removed. | operations engineers | security | S-09 CICD-SEC-08, Recommendations, item 3 | C-18 |
| R-1515 | Build-integrated third parties should run in a scoped context with limited access to secrets and code, and with strict ingress and egress filtering. | operations engineers | security | S-09 CICD-SEC-08, Recommendations, item 3 | C-18 |
| R-1516 | Integrations should be reviewed periodically, and those no longer in use should be removed. | operations engineers | security | S-09 CICD-SEC-08, Recommendations, item 4 | C-18 |
| R-1517 | Sign each resource with external signing infrastructure when it is generated, and verify it against the signing authority before later pipeline steps consume it. | operations engineers | security | S-09 CICD-SEC-09, Recommendations, first item (should) | C-16 |
| R-1518 | Sign commits with a per-contributor key, and block unsigned commits from moving down the pipeline. | software engineers | security | S-09 CICD-SEC-09, Recommendations, code signing (consider) | C-01 |
| R-1519 | Use signing and verification frameworks such as in-toto, SLSA and Sigstore. | operations engineers | security | S-09 CICD-SEC-09, Recommendations, artifact verification tools (consider) | C-16 |
| R-1520 | Detect resources that are not managed through signed infrastructure-as-code templates. | operations engineers | operations | S-09 CICD-SEC-09, Recommendations, configuration drift detection (consider) | C-20 |
| R-1521 | Calculate the hash of any third-party script or resource fetched during builds or deployments, and compare it with the provider's official published hash before use. | operations engineers | security | S-09 CICD-SEC-09, Recommendations, third-party resources (should) | C-10 |
| R-1522 | Inventory every CI/CD system in use, including every instance of self-managed tools. | operations engineers | security | S-09 CICD-SEC-10, Recommendations, item 1 | C-18 |
| R-1523 | Turn on audit and application logs, which are not enabled by default, and cover both human and programmatic access. | operations engineers | security | S-09 CICD-SEC-10, Recommendations, item 2 | C-18 |
| R-1524 | Ship logs to a central location such as a SIEM for correlation and investigation. | operations engineers | security | S-09 CICD-SEC-10, Recommendations, item 3 | C-18 |
| R-1525 | Create alerts for suspicious activity within each system and across the code-shipping process. | operations engineers | security | S-09 CICD-SEC-10, Recommendations, item 4 | C-18 |
| R-1526 | Protect default and release branches against force pushes, deletion, and unreviewed or unchecked merges. | software engineers | security | S-10 section Branch-Protection | C-01 |
| R-1527 | Run tests before pull requests are merged. | software engineers | quality | S-10 section CI-Tests | C-30 |
| R-1528 | Earn an OpenSSF Best Practices badge. | software engineers | security | S-10 section CII-Best-Practices | 5 |
| R-1529 | Require human code review before merging. | quality assurance | security | S-10 section Code-Review | C-02 |
| R-1530 | Have recent contributors from multiple organizations. | software engineers | quality | S-10 section Contributors | C-40 |
| R-1531 | Avoid untrusted code checkouts and script injection in GitHub Actions workflows. | software engineers | security | S-10 section Dangerous-Workflow | C-06 |
| R-1532 | Use an automated dependency update tool. | software engineers | security | S-10 section Dependency-Update-Tool | C-10 |
| R-1533 | Use fuzzing or property-based testing. | security team | security | S-10 section Fuzzing | C-17 |
| R-1534 | Publish a license for the project. | software engineers | quality | S-10 section License | C-41 |
| R-1535 | Keep the project actively maintained. | software engineers | quality | S-10 section Maintained | C-43 |
| R-1536 | Publish the project as a package so users receive updates. | software engineers | security | S-10 section Packaging | C-15 |
| R-1537 | Pin dependencies used in builds and releases to specific hashes or versions. | software engineers | security | S-10 section Pinned-Dependencies | C-10 |
| R-1538 | Run static application security testing. | security team | security | S-10 section SAST | C-11 |
| R-1539 | Maintain a Software Bill of Materials. | software engineers | security | S-10 section SBOM | C-09 |
| R-1540 | Publish a SECURITY.md file that explains how to report vulnerabilities. | software engineers | security | S-10 section Security-Policy | C-14 |
| R-1541 | Cryptographically sign release artifacts. | software engineers | security | S-10 section Signed-Releases | C-16 |
| R-1542 | Follow least privilege for workflow tokens. | software engineers | security | S-10 section Token-Permissions | C-06 |
| R-1543 | Fix open, unfixed vulnerabilities in the project or its dependencies. | software engineers | security | S-10 section Vulnerabilities | C-14 |
| R-1544 | Configure webhooks with a token to authenticate request origins. | operations engineers | security | S-10 section Webhooks | C-18 |
| R-1545 | Do not include generated executables in the source repository. | software engineers | operations | S-10 section Binary-Artifacts | C-46 |
| R-1546 | Require multi-factor authentication to read or change sensitive resources in the authoritative repository. | operations engineers | security | S-11 version page, Level 1, AC-01.01 | C-08 |
| R-1547 | Give new collaborators manual permission assignment or the lowest default privileges. | operations engineers | security | S-11 version page, Level 1, AC-02.01 | C-08 |
| R-1548 | Block direct commits to the primary branch. | software engineers | security | S-11 version page, Level 1, AC-03.01 | C-01 |
| R-1549 | Require explicit confirmation before the primary branch is deleted. | software engineers | security | S-11 version page, Level 1, AC-03.02 | C-01 |
| R-1550 | Sanitize and validate untrusted metadata that CI/CD uses. | software engineers | security | S-11 version page, Level 1, BR-01.01 | C-06 |
| R-1551 | Keep untrusted code snapshots away from privileged CI/CD credentials. | software engineers | security | S-11 version page, Level 1, BR-01.03 | C-06 |
| R-1552 | Deliver official project URIs only over encrypted channels. | users and customers | security | S-11 version page, Level 1, BR-03.01 | C-16 |
| R-1553 | Protect official distribution channels against interception with authenticated channels. | users and customers | security | S-11 version page, Level 1, BR-03.02 | C-16 |
| R-1554 | Prevent unencrypted secrets and credentials from being stored in version control. | software engineers | security | S-11 version page, Level 1, BR-07.01 | C-07 |
| R-1555 | After a release, provide user guides for basic functionality. | users and customers | quality | S-11 version page, Level 1, DO-01.01 | C-37 |
| R-1556 | After a release, provide a guide for reporting defects. | users and customers | quality | S-11 version page, Level 1, DO-02.01 | C-37 |
| R-1557 | Provide public discussion mechanisms for proposed changes and usage problems. | software engineers | quality | S-11 version page, Level 1, GV-02.01 | C-37 |
| R-1558 | Explain the contribution process, or state that contributions are not accepted. | software engineers | quality | S-11 version page, Level 1, GV-03.01 | C-37 |
| R-1559 | Use a source code license that meets the OSI or FSF definition. | software engineers | quality | S-11 version page, Level 1, LE-02.01 | C-41 |
| R-1560 | Use a released asset license that meets the OSI or FSF definition. | software engineers | quality | S-11 version page, Level 1, LE-02.02 | C-41 |
| R-1561 | Keep the source license in a standard license file or directory in the repository. | software engineers | quality | S-11 version page, Level 1, LE-03.01 | C-41 |
| R-1562 | Ship the released asset license with the source or the release assets. | software engineers | quality | S-11 version page, Level 1, LE-03.02 | C-41 |
| R-1563 | Keep the repository publicly readable at a static URL. | software engineers | security | S-11 version page, Level 1, QA-01.01 | C-01 |
| R-1564 | Keep a public record of changes, authors and timestamps in version control. | software engineers | security | S-11 version page, Level 1, QA-01.02 | C-01 |
| R-1565 | Keep a direct-dependency list in the repository where the package manager supports it. | software engineers | security | S-11 version page, Level 1, QA-02.01 | C-09 |
| R-1566 | Multi-repository projects document their codebases. | software engineers | quality | S-11 version page, Level 1, QA-04.01 | C-37 |
| R-1567 | Do not store generated executables in version control. | software engineers | operations | S-11 version page, Level 1, QA-05.01 | C-46 |
| R-1568 | Do not store unreviewable binary artifacts in version control. | software engineers | operations | S-11 version page, Level 1, QA-05.02 | C-46 |
| R-1569 | Document the security contacts. | software engineers | security | S-11 version page, Level 1, VM-02.01 | C-14 |
| R-1570 | CI/CD tasks with no permissions set default to the lowest pipeline permissions. | operations engineers | security | S-11 version page, Level 2, AC-04.01 | C-06 |
| R-1571 | Give each official release a unique version identifier. | software engineers | operations | S-11 version page, Level 2, BR-02.01 | C-45 |
| R-1572 | Include a changelog of functional and security changes with each official release. | software engineers | operations | S-11 version page, Level 2, BR-04.01 | C-45 |
| R-1573 | Build pipelines use standard dependency tooling where available. | software engineers | security | S-11 version page, Level 2, BR-05.01 | C-10 |
| R-1574 | Sign releases, or list them with hashes in a signed manifest. | software engineers | security | S-11 version page, Level 2, BR-06.01 | C-16 |
| R-1575 | After a release, document how dependencies are selected, obtained and tracked. | software engineers | security | S-11 version page, Level 2, DO-06.01 | C-10 |
| R-1576 | Document how to build, including libraries, SDKs and dependencies. | software engineers | quality | S-11 version page, Level 2, DO-07.01 | C-37 |
| R-1577 | Document the members who have access to sensitive resources. | operations engineers | security | S-11 version page, Level 2, GV-01.01 | C-08 |
| R-1578 | Document member roles and responsibilities. | management | quality | S-11 version page, Level 2, GV-01.02 | C-40 |
| R-1579 | The contributor guide states requirements for acceptable contributions. | software engineers | quality | S-11 version page, Level 2, GV-03.02 | C-37 |
| R-1580 | Require contributors to assert legal authority on every commit. | software engineers | quality | S-11 version page, Level 2, LE-01.01 | C-41 |
| R-1581 | Status checks pass, or are manually bypassed, before commits reach the primary branch. | software engineers | quality | S-11 version page, Level 2, QA-03.01 | C-30 |
| R-1582 | Run at least one automated test suite in CI/CD before accepting commits. | software engineers | quality | S-11 version page, Level 2, QA-06.01 | C-30 |
| R-1583 | After a release, design docs cover all actions and actors in the system. | software engineers | quality | S-11 version page, Level 2, SA-01.01 | C-38 |
| R-1584 | After a release, document all external software interfaces. | software engineers | quality | S-11 version page, Level 2, SA-02.01 | C-38 |
| R-1585 | Perform a security assessment of the most likely and most impactful problems. | security team | security | S-11 version page, Level 2, SA-03.01 | C-12 |
| R-1586 | Publish a coordinated vulnerability disclosure policy with a response timeframe. | software engineers | security | S-11 version page, Level 2, VM-01.01 | C-14 |
| R-1587 | Provide a private vulnerability reporting channel to security contacts. | software engineers | security | S-11 version page, Level 2, VM-03.01 | C-14 |
| R-1588 | Publish data about discovered vulnerabilities publicly. | users and customers | security | S-11 version page, Level 2, VM-04.01 | C-14 |
| R-1589 | Give jobs only the minimum privileges their activity needs. | operations engineers | security | S-11 version page, Level 3, AC-04.02 | C-06 |
| R-1590 | Sanitize and validate input from trusted collaborators in pipelines. | software engineers | security | S-11 version page, Level 3, BR-01.04 | C-06 |
| R-1591 | Tie all release assets to the release ID or a unique asset ID. | software engineers | operations | S-11 version page, Level 3, BR-02.02 | C-45 |
| R-1592 | Maintain a policy for storing, accessing and rotating secrets. | operations engineers | security | S-11 version page, Level 3, BR-07.02 | C-07 |
| R-1593 | Document how to verify release integrity and authenticity. | users and customers | security | S-11 version page, Level 3, DO-03.01 | C-16 |
| R-1594 | Document how to verify the expected identity of release authors. | users and customers | security | S-11 version page, Level 3, DO-03.02 | C-16 |
| R-1595 | Document the scope and duration of support for each release. | users and customers | security | S-11 version page, Level 3, DO-04.01 | C-15 |
| R-1596 | Document when releases stop receiving security updates. | users and customers | security | S-11 version page, Level 3, DO-05.01 | C-15 |
| R-1597 | Maintain a policy that requires collaborator review before escalated permissions are granted. | operations engineers | security | S-11 version page, Level 3, GV-04.01 | C-08 |
| R-1598 | Ship an SBOM with compiled released assets. | software engineers | security | S-11 version page, Level 3, QA-02.02 | C-09 |
| R-1599 | Subprojects enforce security requirements at least as strict as the primary codebase. | software engineers | quality | S-11 version page, Level 3, QA-04.02 | C-40 |
| R-1600 | Document when and how tests run. | software engineers | quality | S-11 version page, Level 3, QA-06.02 | C-31 |
| R-1601 | Maintain a policy that major changes add or update automated tests. | software engineers | quality | S-11 version page, Level 3, QA-06.03 | C-31 |
| R-1602 | Require at least one approval from a non-author human before merging to the primary branch. | quality assurance | security | S-11 version page, Level 3, QA-07.01 | C-02 |
| R-1603 | When the project has made a release, perform threat modeling and attack surface analysis. | security team | security | S-11 version page, Level 3, SA-03.02 | C-12 |
| R-1604 | Publish a VEX document for vulnerabilities that do not affect the project. | software engineers | security | S-11 version page, Level 3, VM-04.02 | C-14 |
| R-1605 | Set a policy with a remediation threshold for SCA findings, covering vulnerabilities and licenses. | security team | security | S-11 version page, Level 3, VM-05.01 | C-11 |
| R-1606 | Address SCA violations under the policy before any release. | security team | security | S-11 version page, Level 3, VM-05.02 | C-11 |
| R-1607 | Run automated SCA on every change, blocking violations unless suppressed as non-exploitable. | security team | security | S-11 version page, Level 3, VM-05.03 | C-11 |
| R-1608 | Set a policy with a remediation threshold for SAST findings. | security team | security | S-11 version page, Level 3, VM-06.01 | C-11 |
| R-1609 | Run automated SAST on every change, blocking violations unless suppressed as non-exploitable. | security team | security | S-11 version page, Level 3, VM-06.02 | C-11 |
| R-1610 | Financial entities must manage the risks from ICT third-party service providers themselves, including ongoing monitoring of their contracts with critical providers. | management | security | S-12 page 7, recital (92) | C-19 |
| R-1611 | The Oversight Framework should not affect the full responsibility of financial entities for complying with this Regulation. | management | quality | S-12 page 7, recital (92) | C-41 |
| R-1612 | It is crucial that critical ICT third-party service providers follow the recommendations of the Lead Overseer and address its concerns. | suppliers | quality | S-12 page 7, recital (80) | C-41 |
| R-1613 | A sanctioning regime for lack of cooperation by critical providers is necessary. | regulators and auditors | quality | S-12 page 7, recital (80) | C-41 |
| R-1614 | The need of the Lead Overseer to impose penalty payments should not be jeopardised by enforcement difficulties in third countries. | regulators and auditors | quality | S-12 page 7, recital (81) | C-41 |
| R-1615 | Critical providers that are established in a third country should undertake, within 12 months of designation, all necessary arrangements to set up a subsidiary in the Union. | suppliers | quality | S-12 page 7, recital (81) | C-41 |
| R-1616 | Critical providers should maintain an adequate business presence in the Union. | suppliers | quality | S-12 page 7, recital (81) | C-41 |
| R-1617 | Oversight activities should be first conducted on premises located in the Union and by interacting with entities located in the Union. | regulators and auditors | quality | S-12 page 7, recital (83) | C-41 |
| R-1618 | The Lead Overseer should also be able to exercise its oversight powers in third countries, framed by conditions such as the consent of the provider concerned. | regulators and auditors | quality | S-12 page 7, recital (83) | C-41 |
| R-1619 | The ESAs should conclude administrative cooperation arrangements with the relevant authorities of third countries. | regulators and auditors | quality | S-12 page 7, recital (83) | C-41 |
| R-1620 | Critical providers that are part of a group should designate one legal person as their coordination point. | suppliers | quality | S-12 page 7, recital (84) | C-41 |
| R-1621 | The Oversight Framework should be without prejudice to the competence of Member States to conduct their own oversight of providers that are important at national level. | regulators and auditors | quality | S-12 page 7, recital (85) | C-41 |
| R-1622 | The Joint Committee of the ESAs should continue to ensure overall cross-sectoral coordination on ICT risk matters. | regulators and auditors | quality | S-12 page 7, recital (86) | C-41 |
| R-1623 | The Joint Committee should be supported by a new subcommittee, the Oversight Forum, that carries out preparatory work. | regulators and auditors | quality | S-12 page 7, recital (86) | C-41 |
| R-1624 | The individual assignment of a critical provider to one ESA should result from an assessment of the preponderance of financial entities in that ESA's sectors. | regulators and auditors | quality | S-12 page 7, recital (87) | C-41 |
| R-1625 | Lead Overseers should be granted the necessary powers to conduct investigations, onsite and offsite inspections, and to obtain complete and updated information. | regulators and auditors | quality | S-12 page 7, recital (88) | C-41 |
| R-1626 | Before being designated, providers should have the right to submit a reasoned statement to the Lead Overseer. | suppliers | quality | S-12 page 7, recital (89) | C-41 |
| R-1627 | This Regulation should ensure that the rights of critical providers are observed throughout the Oversight Framework. | suppliers | quality | S-12 page 7, recital (89) | C-41 |
| R-1628 | Critical providers should be given the opportunity to explain the expected impact on customers outside the scope, and to formulate mitigating solutions, before recommendations are finalised. | suppliers | quality | S-12 page 7, recital (89) | C-41 |
| R-1629 | Critical providers that disagree with recommendations should submit a reasoned explanation of their intention not to endorse them. | suppliers | quality | S-12 page 7, recital (89) | C-41 |
| R-1630 | Where no reasoned explanation is submitted, or it is insufficient, the Lead Overseer should issue a public notice on the matter of non-compliance. | regulators and auditors | quality | S-12 page 7, recital (89) | C-41 |
| R-1631 | Competent authorities should verify substantive compliance with recommendations of the Lead Overseer as part of prudential supervision. | regulators and auditors | quality | S-12 page 7, recital (90) | C-41 |
| R-1632 | Competent authorities should be able to require financial entities to take additional measures for risks in the recommendations, and should issue notifications in due course. | regulators and auditors | quality | S-12 page 7, recital (90) | C-41 |
| R-1633 | Competent authorities should be able, on a voluntary basis and before adopting additional measures, to consult the competent authorities under Directive (EU) 2022/2555. | regulators and auditors | quality | S-12 page 7, recital (90) | C-41 |
| R-1634 | The exercise of oversight should be guided by close coordination among the ESAs through a joint oversight network. | regulators and auditors | quality | S-12 page 7, recital (91) | C-41 |
| R-1635 | The exercise of oversight should be consistent with Directive (EU) 2022/2555, and avoid duplication through voluntary consultation. | regulators and auditors | quality | S-12 page 7, recital (91) | C-41 |
| R-1636 | The exercise of oversight should apply diligence to minimise the risk of disruption to services for customers outside the scope. | regulators and auditors | quality | S-12 page 7, recital (91) | C-41 |
| R-1637 | Competent authorities should refrain from taking measures individually to monitor the risks of critical providers, and should rely on the Lead Overseer's assessment. | regulators and auditors | quality | S-12 page 7, recital (93) | C-41 |
| R-1638 | Any measures by competent authorities should be coordinated and agreed in advance with the Lead Overseer. | regulators and auditors | quality | S-12 page 7, recital (93) | C-41 |
| R-1639 | The ESAs should be encouraged to conclude cooperation arrangements with relevant third-country supervisory authorities. | regulators and auditors | quality | S-12 page 7, recital (94) | C-41 |
| R-1640 | The Lead Overseer should draw on national supervisory capabilities and set up dedicated examination teams for each critical provider. | regulators and auditors | quality | S-12 page 7, recital (95) | C-41 |
| R-1641 | Competent authorities should have all required supervisory, investigative and sanctioning powers. | regulators and auditors | quality | S-12 page 7, recital (97) | C-41 |
| R-1642 | Competent authorities should, in principle, publish notices of the administrative penalties they impose. | regulators and auditors | quality | S-12 page 7, recital (97) | C-41 |
| R-1643 | The application of this Regulation should be facilitated by close cooperation among competent authorities, including the ECB, and by consultation with the ESAs. | regulators and auditors | quality | S-12 page 7, recital (97) | C-41 |
| R-1644 | The power to adopt delegated acts should be delegated to the Commission to specify designation criteria and oversight fees. | regulators and auditors | quality | S-12 page 7, recital (98) | C-41 |
| R-1645 | The Commission should carry out appropriate consultations, including at expert level, during its preparatory work for delegated acts. | regulators and auditors | quality | S-12 page 7, recital (98) | C-41 |
| R-1646 | The European Parliament and the Council should receive all documents at the same time as Member States' experts. | regulators and auditors | quality | S-12 page 7, recital (98) | C-41 |
| R-1647 | The ESAs should develop draft regulatory technical standards that do not involve policy choices, for submission to the Commission. | regulators and auditors | quality | S-12 page 7, recital (99) | C-41 |
| R-1648 | The Commission and the ESAs should ensure that the standards can be applied by all financial entities in a manner proportionate to size and overall risk profile. | management | quality | S-12 page 7, recital (99) | C-41 |
| R-1649 | The ESAs should develop draft implementing technical standards with standard templates, forms and procedures for reporting major incidents, and standard templates for the register of information. | regulators and auditors | quality | S-12 page 7, recital (100) | C-41 |
| R-1650 | When developing the implementing technical standards, the ESAs should take into account the size and overall risk profile of the financial entity. | regulators and auditors | quality | S-12 page 7, recital (100) | C-41 |
| R-1651 | It is appropriate to mandate the ESAs to submit technical standards to the Commission that carry over and update existing ICT risk management rules. | regulators and auditors | quality | S-12 page 7, recital (101) | C-41 |
| R-1652 | The Regulations listed in recital (102) should be amended to clarify that the applicable ICT risk-related provisions are laid down in this Regulation. | regulators and auditors | quality | S-12 page 7, recital (102) | C-41 |
| R-1653 | The scope of the operational-risk articles in the regulations listed in recital (103) should be narrowed down, carrying over the digital operational resilience provisions into this Regulation. | regulators and auditors | quality | S-12 page 7, recital (103) | C-41 |
| R-1654 | The Commission should swiftly assess the need for reviewing the scope of this Regulation for payment systems. | regulators and auditors | quality | S-12 page 7, recital (104) | C-41 |
| R-1655 | Member States may draw inspiration from the requirements of this Regulation when applying rules to payment system operators supervised under their own jurisdictions. | regulators and auditors | quality | S-12 page 7, recital (104) | C-41 |
| R-1656 | This Regulation shall be considered a sector-specific Union legal act for essential or important entities under Directive (EU) 2022/2555. | management | quality | S-12 page 8, Art. 1(2) | C-41 |
| R-1657 | Financial entities must meet the requirements on ICT risk management. | management | quality | S-12 page 8, Art. 1(1)(a)(i) | C-41 |
| R-1658 | Financial entities must meet the requirements on reporting major ICT-related incidents; notifying significant cyber threats is voluntary. | management | operations | S-12 page 8, Art. 1(1)(a)(ii) | C-25 |
| R-1659 | Financial entities referred to in Art. 2(1)(a) to (d) must report major operational or security payment-related incidents to competent authorities. | management | operations | S-12 page 8, Art. 1(1)(a)(iii) | C-25 |
| R-1660 | Financial entities must meet the requirements on digital operational resilience testing. | management | security | S-12 page 8, Art. 1(1)(a)(iv) | C-17 |
| R-1661 | Financial entities must meet the requirements on information and intelligence sharing on cyber threats and vulnerabilities. | management | security | S-12 page 8, Art. 1(1)(a)(v) | C-14 |
| R-1662 | Financial entities must meet the requirements on the sound management of ICT third-party risk. | management | security | S-12 page 8, Art. 1(1)(a)(vi) | C-19 |
| R-1663 | Contractual arrangements between ICT third-party service providers and financial entities must meet the requirements of this Regulation. | suppliers | security | S-12 page 8, Art. 1(1)(b) | C-19 |
| R-1664 | Rules for the Oversight Framework of critical ICT third-party service providers must be established and conducted. | regulators and auditors | quality | S-12 page 8, Art. 1(1)(c) | C-41 |
| R-1665 | Rules on cooperation among competent authorities, and on their supervision and enforcement, must apply. | regulators and auditors | quality | S-12 page 8, Art. 1(1)(d) | C-41 |
| R-1666 | Member States may exclude from scope the entities in Art. 2(5) points (4) to (23) of Directive 2013/36/EU located in their territories. | regulators and auditors | quality | S-12 page 9, Art. 2(4) | C-41 |
| R-1667 | A Member State that uses this exclusion must inform the Commission, and of any later change. | regulators and auditors | quality | S-12 page 9, Art. 2(4) | C-41 |
| R-1668 | The Commission must make the information on exclusions publicly available. | regulators and auditors | quality | S-12 page 9, Art. 2(4) | C-41 |
| R-1669 | Financial entities shall implement the rules of Chapter II in line with proportionality, taking size and overall risk profile into account | management | quality | S-12 page 11 | C-41 |
| R-1670 | Application of Chapters III, IV and V, Section I, shall be proportionate to size, risk profile, nature, scale and complexity | management | quality | S-12 page 11 | C-41 |
| R-1671 | Competent authorities shall consider proportionality when they review the consistency of the ICT risk management framework | regulators and auditors | quality | S-12 page 11 | C-41 |
| R-1672 | Financial entities shall have an internal governance and control framework that ensures effective and prudent management of ICT risk | management | quality | S-12 page 11 | C-40 |
| R-1673 | The management body shall define, approve, oversee and be responsible for all arrangements of the ICT risk management framework | management | quality | S-12 page 11 | C-40 |
| R-1674 | The management body shall bear the ultimate responsibility for managing the financial entity's ICT risk | management | quality | S-12 page 11 | C-40 |
| R-1675 | The management body shall put in place policies that aim to keep high standards of availability, authenticity, integrity and confidentiality of data | management | quality | S-12 page 11 | C-40 |
| R-1676 | The management body shall set clear roles and responsibilities for all ICT-related functions, with communication, cooperation and coordination among them | management | quality | S-12 page 11 | C-40 |
| R-1677 | The management body shall bear the overall responsibility for setting and approving the digital operational resilience strategy and the ICT risk tolerance level | management | quality | S-12 page 11 | C-40 |
| R-1678 | The management body shall approve, oversee and periodically review the ICT business continuity policy and the ICT response and recovery plans | management | quality | S-12 page 11 to page 12 | C-40 |
| R-1679 | The management body shall approve and periodically review the ICT internal audit plans, ICT audits and material changes to them | management | quality | S-12 page 12 | C-40 |
| R-1680 | The management body shall allocate and periodically review an appropriate budget for digital operational resilience needs, including security awareness programmes, training and ICT skills for all staff | management | quality | S-12 page 12 | C-40 |
| R-1681 | The management body shall approve and periodically review the policy on the use of ICT services from ICT third-party service providers | management | quality | S-12 page 12 | C-40 |
| R-1682 | The management body shall put in place reporting channels at corporate level, so that it is informed of ICT third-party arrangements, planned material changes, and their impact | management | quality | S-12 page 12 | C-40 |
| R-1683 | The management body shall be informed of at least major ICT-related incidents and their impact, and of response, recovery and corrective measures | management | quality | S-12 page 12 | C-40 |
| R-1684 | Financial entities other than microenterprises shall establish a role to monitor ICT third-party arrangements, or shall designate a senior management member as responsible | management | quality | S-12 page 12 | C-40 |
| R-1685 | Members of the management body shall actively keep up to date with sufficient knowledge and skills to understand and assess ICT risk | management | quality | S-12 page 12 | C-39 |
| R-1686 | Members of the management body shall follow specific training on a regular basis, commensurate to the ICT risk managed | management | quality | S-12 page 12 | C-39 |
| R-1687 | Financial entities shall have a sound, comprehensive and well-documented ICT risk management framework as part of the overall risk management system | management | quality | S-12 page 12 | C-40 |
| R-1688 | The framework shall include at least strategies, policies, procedures, ICT protocols and tools to protect information assets and ICT assets, including physical components | management | quality | S-12 page 12 | C-40 |
| R-1689 | Financial entities shall deploy appropriate strategies, policies, procedures, ICT protocols and tools to minimise the impact of ICT risk | management | quality | S-12 page 12 | C-40 |
| R-1690 | Financial entities shall provide complete and updated information on ICT risk and the framework to competent authorities upon request | regulators and auditors | quality | S-12 page 12 | C-41 |
| R-1691 | Financial entities other than microenterprises shall assign managing and overseeing ICT risk to a control function with appropriate independence | management | quality | S-12 page 12 | C-40 |
| R-1692 | Financial entities shall ensure appropriate segregation and independence of ICT risk management, control and internal audit functions, per the three lines of defence model or an internal model | management | quality | S-12 page 12 | C-34 |
| R-1693 | The framework shall be documented and reviewed at least once a year, or periodically for microenterprises, and after major ICT-related incidents and supervisory or test or audit conclusions | management | quality | S-12 page 12 | C-40 |
| R-1694 | The framework shall be continuously improved on the basis of lessons from implementation and monitoring | management | quality | S-12 page 12 | C-35 |
| R-1695 | A report on the review of the framework shall be submitted to the competent authority upon its request | regulators and auditors | quality | S-12 page 12 | C-41 |
| R-1696 | The framework of financial entities other than microenterprises shall be subject to internal audit on a regular basis, in line with the audit plan | quality assurance | quality | S-12 page 12 | C-34 |
| R-1697 | Auditors shall have sufficient knowledge, skills and expertise in ICT risk, and appropriate independence | quality assurance | quality | S-12 page 12 | C-39 |
| R-1698 | The frequency and focus of ICT audits shall be commensurate to the ICT risk of the entity | quality assurance | quality | S-12 page 12 | C-34 |
| R-1699 | Financial entities shall establish a formal follow-up process, with rules for timely verification and remediation of critical ICT audit findings | management | quality | S-12 page 12 | C-35 |
| R-1700 | The framework shall include a digital operational resilience strategy that sets out how the framework is implemented | management | quality | S-12 page 12 | C-40 |
| R-1701 | The strategy shall explain how the framework supports the business strategy and objectives | management | quality | S-12 page 12 | C-40 |
| R-1702 | The strategy shall set the risk tolerance level for ICT risk and analyse the impact tolerance for ICT disruptions | management | quality | S-12 page 12 | C-40 |
| R-1703 | The strategy shall set clear information security objectives, including key performance indicators and key risk metrics | management | quality | S-12 page 12 | C-40 |
| R-1704 | The strategy shall explain the ICT reference architecture and any changes needed | management | quality | S-12 page 12 | C-38 |
| R-1705 | The strategy shall outline mechanisms to detect ICT-related incidents, prevent their impact and protect against it | operations engineers | operations | S-12 page 12 | C-23 |
| R-1706 | The strategy shall evidence the current situation from the number of major ICT-related incidents reported and the effectiveness of preventive measures | management | quality | S-12 page 12 | C-35 |
| R-1707 | The strategy shall implement digital operational resilience testing in accordance with Chapter IV | management | security | S-12 page 12 | C-17 |
| R-1708 | The strategy shall outline a communication strategy for ICT-related incidents whose disclosure is required under Article 14 | management | operations | S-12 page 12 | C-25 |
| R-1709 | Financial entities shall use and maintain updated ICT systems, protocols and tools that are appropriate, reliable, have sufficient capacity, and are technologically resilient | operations engineers | security | S-12 page 12 | C-18 |
| R-1710 | Financial entities shall identify, classify and adequately document all ICT-supported business functions, roles and responsibilities, information assets and ICT assets, and their dependencies | management | security | S-12 page 12 | C-09 |
| R-1711 | Financial entities shall review the adequacy of this classification and documentation as needed, and at least yearly | management | security | S-12 page 12 | C-09 |
| R-1712 | Financial entities shall, on a continuous basis, identify all sources of ICT risk, including risk exposure to and from other financial entities, and assess cyber threats and ICT vulnerabilities | security team | security | S-12 page 13, Article 8(2) | C-12 |
| R-1713 | Financial entities shall review on a regular basis, and at least yearly, the risk scenarios impacting them | security team | security | S-12 page 13, Article 8(2) | C-12 |
| R-1714 | Financial entities other than microenterprises shall perform a risk assessment upon each major change in the network and information system infrastructure, processes or procedures | security team | security | S-12 page 13, Article 8(3) | C-12 |
| R-1715 | Financial entities shall identify all information assets and ICT assets, including those on remote sites, network resources and hardware equipment, and shall map those considered critical | operations engineers | security | S-12 page 13, Article 8(4) | C-18 |
| R-1716 | Financial entities shall map the configuration of information assets and ICT assets, and the links and interdependencies between them | operations engineers | operations | S-12 page 13, Article 8(4) | C-45 |
| R-1717 | Financial entities shall identify and document all processes that are dependent on ICT third-party service providers | management | security | S-12 page 13, Article 8(5) | C-19 |
| R-1718 | Financial entities shall identify interconnections with ICT third-party service providers that support critical or important functions | management | security | S-12 page 13, Article 8(5) | C-19 |
| R-1719 | Financial entities shall maintain relevant inventories and update them periodically and every time a major change occurs | operations engineers | security | S-12 page 13, Article 8(6) | C-18 |
| R-1720 | Financial entities other than microenterprises shall conduct a specific ICT risk assessment on all legacy ICT systems on a regular basis and at least yearly | security team | quality | S-12 page 13, Article 8(7) | C-43 |
| R-1721 | Financial entities other than microenterprises shall conduct a specific ICT risk assessment in any case before and after connecting technologies, applications or systems | security team | security | S-12 page 13, Article 8(7) | C-12 |
| R-1722 | Financial entities shall continuously monitor and control the security and functioning of ICT systems and tools | operations engineers | operations | S-12 page 13, Article 9(1) | C-23 |
| R-1723 | Financial entities shall minimise the impact of ICT risk through the deployment of appropriate ICT security tools, policies and procedures | security team | security | S-12 page 13, Article 9(1) | C-18 |
| R-1724 | Financial entities shall design, procure and implement ICT security policies, procedures, protocols and tools that aim to ensure resilience, continuity and availability of ICT systems | security team | security | S-12 page 13, Article 9(2) | C-44 |
| R-1725 | Financial entities shall maintain high standards of availability, authenticity, integrity and confidentiality of data, whether at rest, in use or in transit | security team | security | S-12 page 13, Article 9(2) | C-44 |
| R-1726 | Financial entities shall use ICT solutions and processes that ensure the security of the means of transfer of data | security team | security | S-12 page 13, Article 9(3)(a) | C-44 |
| R-1727 | ICT solutions and processes shall minimise the risk of corruption or loss of data, unauthorised access and technical flaws that may hinder business activity | security team | security | S-12 page 13, Article 9(3)(b) | C-44 |
| R-1728 | ICT solutions and processes shall prevent lack of availability, impairment of authenticity and integrity, breaches of confidentiality and loss of data | security team | security | S-12 page 13, Article 9(3)(c) | C-44 |
| R-1729 | ICT solutions and processes shall ensure that data is protected from risks arising from data management, including poor administration, processing-related risks and human error | security team | security | S-12 page 13, Article 9(3)(d) | C-44 |
| R-1730 | Financial entities shall develop and document an information security policy defining rules to protect availability, authenticity, integrity and confidentiality of data, information assets and ICT assets | management | quality | S-12 page 13, Article 9(4)(a) | C-40 |
| R-1731 | Financial entities shall establish, following a risk-based approach, a sound network and infrastructure management structure, which may include automated mechanisms to isolate affected information assets in the event of cyber-attacks | operations engineers | security | S-12 page 13, Article 9(4)(b) | C-44 |
| R-1732 | Financial entities shall implement policies that limit physical or logical access to information assets and ICT assets to what is required for legitimate and approved functions and activities only | operations engineers | security | S-12 page 13, Article 9(4)(c) | C-08 |
| R-1733 | Financial entities shall establish policies, procedures and controls that address access rights and ensure a sound administration thereof | operations engineers | security | S-12 page 13, Article 9(4)(c) | C-08 |
| R-1734 | Financial entities shall implement policies and protocols for strong authentication mechanisms, based on relevant standards and dedicated control systems | operations engineers | security | S-12 page 13, Article 9(4)(d) | C-08 |
| R-1735 | Financial entities shall implement protection measures of cryptographic keys, whereby data is encrypted based on results of approved data classification and ICT risk assessment processes | security team | security | S-12 page 13, Article 9(4)(d) | C-44 |
| R-1736 | Financial entities shall implement documented policies, procedures and controls for ICT change management, based on a risk assessment approach, as part of the overall change management process | operations engineers | operations | S-12 page 13, Article 9(4)(e) | C-26 |
| R-1737 | ICT change management shall ensure that all changes to ICT systems are recorded, tested, assessed, approved, implemented and verified in a controlled manner | operations engineers | operations | S-12 page 13, Article 9(4)(e) | C-26 |
| R-1738 | Financial entities shall have appropriate and comprehensive documented policies for patches and updates | operations engineers | security | S-12 page 13, Article 9(4)(f) | C-18 |
| R-1739 | Financial entities shall design the network connection infrastructure so that it can be instantaneously severed or segmented in order to minimise and prevent contagion | operations engineers | security | S-12 page 13, Article 9, second subparagraph | C-44 |
| R-1740 | The ICT change management process shall be approved by appropriate lines of management and shall have specific protocols in place | management | operations | S-12 page 13, Article 9, third subparagraph | C-26 |
| R-1741 | Financial entities shall have in place mechanisms to promptly detect anomalous activities, including ICT network performance issues and ICT-related incidents | operations engineers | operations | S-12 page 13, Article 10(1) | C-23 |
| R-1742 | Financial entities shall identify potential material single points of failure | operations engineers | operations | S-12 page 13, Article 10(1) | C-27 |
| R-1743 | All detection mechanisms shall be regularly tested in accordance with Article 25 | operations engineers | operations | S-12 page 13, Article 10(1), second subparagraph | C-23 |
| R-1744 | Detection mechanisms shall enable multiple layers of control, define alert thresholds and criteria, and include automatic alert mechanisms for relevant staff in charge of ICT-related incident response | operations engineers | operations | S-12 page 13, Article 10(2) | C-23 |
| R-1745 | Financial entities shall devote sufficient resources and capabilities to monitor user activity, the occurrence of ICT anomalies and ICT-related incidents, in particular cyber-attacks | operations engineers | operations | S-12 page 13, Article 10(3) | C-23 |
| R-1746 | Data reporting service providers shall have systems that can effectively check trade reports for completeness, identify omissions and obvious errors, and request re-transmission of those reports | management | security | S-12 page 13, Article 10(4) | C-44 |
| R-1747 | Financial entities shall put in place a comprehensive ICT business continuity policy | management | operations | S-12 page 13, Article 11(1) | C-27 |
| R-1748 | Financial entities shall implement the ICT business continuity policy through dedicated, appropriate and documented arrangements, plans, procedures and mechanisms | management | operations | S-12 page 13, Article 11(2) | C-27 |
| R-1749 | These arrangements shall ensure the continuity of critical or important functions | management | operations | S-12 page 13, Article 11(2)(a) | C-27 |
| R-1750 | Financial entities shall quickly, appropriately and effectively respond to, and resolve, all ICT-related incidents in a way that limits damage and prioritises the resumption of activities and recovery actions | operations engineers | operations | S-12 page 13, Article 11(2)(b) | C-25 |
| R-1751 | Financial entities shall activate, without delay, dedicated plans that enable containment measures, processes and technologies suited to each type of ICT-related incident | operations engineers | operations | S-12 page 13, Article 11(2)(c) | C-25 |
| R-1752 | Financial entities shall estimate preliminary impacts, damages and losses | operations engineers | operations | S-12 page 13, Article 11(2)(d) | C-25 |
| R-1753 | Financial entities shall set out communication and crisis management actions, and report to competent authorities in accordance with Article 19 | operations engineers | operations | S-12 page 13, Article 11(2)(e) | C-25 |
| R-1754 | ICT response and recovery plans shall be subject to independent internal audit reviews | quality assurance | quality | S-12 page 13, Article 11(3) | C-34 |
| R-1755 | Financial entities shall put in place, maintain and periodically test appropriate ICT business continuity plans, notably for critical or important functions outsourced to ICT third-party service providers | operations engineers | operations | S-12 page 13, Article 11(4) | C-27 |
| R-1756 | Financial entities shall conduct a business impact analysis of their exposures to severe business disruptions | management | operations | S-12 page 13, Article 11(5) | C-27 |
| R-1757 | Financial entities shall ensure that ICT assets and ICT services are designed and used in full alignment with the business impact analysis, in particular with regard to ensuring the redundancy of all critical components | operations engineers | operations | S-12 page 13, Article 11(5) | C-27 |
| R-1758 | Financial entities shall test the ICT business continuity plans and the ICT response and recovery plans at least yearly, and in the event of any substantive changes to ICT systems supporting critical or important functions | operations engineers | operations | S-12 pages 13 to 14, Article 11(6)(a) | C-27 |
| R-1759 | Financial entities shall test the crisis communication plans established in accordance with Article 14 | operations engineers | operations | S-12 page 14, Article 11(6)(b) | C-25 |
| R-1760 | Financial entities other than microenterprises shall include in the testing plans scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities | operations engineers | operations | S-12 page 14, Article 11, second subparagraph of 6 | C-27 |
| R-1761 | Financial entities shall regularly review their ICT business continuity policy and ICT response and recovery plans, taking into account test results and recommendations from audit checks or supervisory reviews | management | operations | S-12 page 14, Article 11(6), third subparagraph | C-27 |
| R-1762 | Financial entities other than microenterprises shall have a crisis management function | management | operations | S-12 page 14, Article 11(7) | C-25 |
| R-1763 | Financial entities shall keep readily accessible records of activities before and during disruption events when their plans are activated | operations engineers | operations | S-12 page 14, Article 11(8) | C-25 |
| R-1764 | Central securities depositories shall provide the competent authorities with copies of the results of the ICT business continuity tests, or of similar exercises | management | quality | S-12 page 14, Article 11(9) | C-41 |
| R-1765 | Financial entities other than microenterprises shall report to the competent authorities, upon their request, an estimation of aggregated annual costs and losses caused by major ICT-related incidents | management | quality | S-12 page 14, Article 11(10) | C-41 |
| R-1766 | The ESAs, through the Joint Committee, shall by 17 July 2024 develop common guidelines on the estimation of aggregated annual costs and losses | regulators and auditors | quality | S-12 page 14, Article 11(11) | C-41 |
| R-1767 | Financial entities shall develop and document backup policies and procedures specifying the scope of the data that is subject to the backup and the minimum frequency of the backup, based on criticality or confidentiality | operations engineers | operations | S-12 page 14, Article 12(1)(a) | C-27 |
| R-1768 | Financial entities shall develop and document restoration and recovery procedures and methods | operations engineers | operations | S-12 page 14, Article 12(1)(b) | C-27 |
| R-1769 | Financial entities shall set up backup systems that can be activated in accordance with the backup policies and procedures, and restoration and recovery procedures and methods | operations engineers | operations | S-12 page 14, Article 12(2) | C-27 |
| R-1770 | The activation of backup systems shall not jeopardise the security of the network and information systems or the availability, authenticity, integrity or confidentiality of data | operations engineers | operations | S-12 page 14, Article 12(2) | C-27 |
| R-1771 | Testing of the backup procedures and restoration and recovery procedures and methods shall be undertaken periodically | operations engineers | operations | S-12 page 14, Article 12(2) | C-27 |
| R-1772 | When restoring backup data using own systems, financial entities shall use ICT systems that are physically and logically segregated from the source ICT system | operations engineers | operations | S-12 page 14, Article 12(3) | C-27 |
| R-1773 | Those ICT systems shall be securely protected from any unauthorised access or ICT corruption and allow for the timely restoration of services | operations engineers | operations | S-12 page 14, Article 12(3) | C-27 |
| R-1774 | For central counterparties, the recovery plans shall enable the recovery of all transactions at the time of disruption | management | operations | S-12 page 14, Article 12(3) | C-27 |
| R-1775 | Data reporting service providers shall maintain adequate resources and have back-up and restoration facilities in place in order to offer and maintain their services at all times | management | operations | S-12 page 14, Article 12(3) | C-27 |
| R-1776 | Financial entities other than microenterprises shall maintain redundant ICT capacities equipped with resources, capabilities and functions that are adequate to ensure business needs | operations engineers | operations | S-12 page 14, Article 12(4) | C-27 |
| R-1777 | Microenterprises shall assess the need to maintain redundant ICT capacities based on their risk profile | management | operations | S-12 page 14, Article 12(4) | C-27 |
| R-1778 | Central securities depositories shall maintain at least one secondary processing site endowed with adequate resources, capabilities, functions and staffing arrangements | management | operations | S-12 page 14, Article 12(5) | C-27 |
| R-1779 | The secondary processing site shall be located at a geographical distance from the primary processing site | management | operations | S-12 page 14, Article 12(5)(a) | C-27 |
| R-1780 | The secondary processing site shall be capable of ensuring the continuity of critical or important functions identically to the primary site, or of providing the necessary level of services | management | operations | S-12 page 14, Article 12(5)(b) | C-27 |
| R-1781 | The secondary processing site shall be immediately accessible to the financial entity's staff | management | operations | S-12 page 14, Article 12(5)(c) | C-27 |
| R-1782 | Financial entities shall take into account whether a function is critical or important when determining the recovery time and recovery point objectives for each function | management | operations | S-12 page 14, Article 12(6) | C-27 |
| R-1783 | Recovery time and recovery point objectives shall ensure that, in extreme scenarios, the agreed service levels are met | management | operations | S-12 page 14, Article 12(6) | C-24 |
| R-1784 | When recovering from an ICT-related incident, financial entities shall perform necessary checks, including multiple checks and reconciliations, to maintain the highest level of data integrity | operations engineers | operations | S-12 page 14, Article 12(7) | C-27 |
| R-1785 | These checks shall also be performed when reconstructing data from external stakeholders, to ensure that all data is consistent between systems | operations engineers | operations | S-12 page 14, Article 12(7) | C-27 |
| R-1786 | Financial entities shall have in place capabilities and staff to gather information on vulnerabilities and cyber threats and ICT-related incidents, and to analyse their impact | security team | security | S-12 page 14, Article 13(1) | C-14 |
| R-1787 | Financial entities shall put in place post ICT-related incident reviews after a major ICT-related incident disrupts their core activities | operations engineers | operations | S-12 page 14, Article 13(2) | C-25 |
| R-1788 | Financial entities other than microenterprises shall, upon request, communicate to the competent authorities the changes implemented following post ICT-related incident reviews | management | quality | S-12 page 14, Article 13(2) | C-41 |
| R-1789 | Post ICT-related incident reviews shall determine whether the established procedures were followed and the actions taken were effective | operations engineers | operations | S-12 page 14, Article 13(2) | C-25 |
| R-1790 | Lessons from digital operational resilience testing under Articles 26 and 27, from real ICT-related incidents, and from activation of plans shall be incorporated on a continuous basis into the ICT risk assessment process | management | quality | S-12 page 14, Article 13(3) | C-35 |
| R-1791 | Those findings shall form the basis for appropriate reviews of relevant components of the ICT risk management framework | management | quality | S-12 page 14, Article 13(3) | C-35 |
| R-1792 | Financial entities shall monitor the effectiveness of the implementation of their digital operational resilience strategy | management | quality | S-12 page 14, Article 13(4) | C-35 |
| R-1793 | Financial entities shall map the evolution of ICT risk over time and analyse the frequency, types, magnitude and evolution of ICT-related incidents | management | quality | S-12 page 14, Article 13(4) | C-35 |
| R-1794 | Financial entities shall enhance the cyber maturity and preparedness of the financial entity | management | quality | S-12 page 14, Article 13(4) | C-40 |
| R-1795 | Senior ICT staff shall report at least yearly to the management body on the findings and put forward recommendations | management | quality | S-12 page 14, Article 13(5) | C-40 |
| R-1796 | Financial entities shall develop ICT security awareness programmes and digital operational resilience training as compulsory modules in their staff training schemes | management | quality | S-12 page 14, Article 13(6) | C-39 |
| R-1797 | Those programmes and training shall be applicable to all employees and to senior management staff, and shall have a level of complexity commensurate to the remit of their functions | management | quality | S-12 page 14, Article 13(6) | C-39 |
| R-1798 | Where appropriate, financial entities shall include ICT third-party service providers in their relevant training schemes | suppliers | quality | S-12 page 14, Article 13(6) | C-39 |
| R-1799 | Financial entities other than microenterprises shall monitor relevant technological developments on a continuous basis | management | quality | S-12 page 14, Article 13(7) | C-39 |
| R-1800 | Financial entities other than microenterprises shall keep up-to-date with the latest ICT risk management processes, in order to effectively combat current or new forms of cyber-attacks | management | quality | S-12 page 14, Article 13(7) | C-39 |
| R-1801 | Financial entities shall have in place crisis communication plans enabling a responsible disclosure of major ICT-related incidents or vulnerabilities to clients and counterparts and to the public, as appropriate | management | security | S-12 page 14, Article 14(1) | C-14 |
| R-1802 | Financial entities shall implement communication policies for internal staff and for external stakeholders | management | operations | S-12 page 14, Article 14(2) | C-25 |
| R-1803 | Communication policies for staff shall differentiate between staff involved in ICT risk management, in particular staff responsible for response and recovery, and staff that needs to be informed | management | operations | S-12 page 14, Article 14(2) | C-25 |
| R-1804 | At least one person in the financial entity shall be tasked with implementing the communication strategy for ICT-related incidents and fulfil the public and media function | management | operations | S-12 page 14, Article 14(3) | C-25 |
| R-1805 | The ESAs, through the Joint Committee and in consultation with ENISA, shall develop common draft regulatory technical standards on the elements of ICT security policies, procedures, protocols and tools | regulators and auditors | quality | S-12 page 14, Article 15 (introduction); page 15, Article 15(a) | C-41 |
| R-1806 | The ESAs shall develop draft regulatory technical standards on access management rights, associated human resource policy, and monitoring of anomalous behaviour | regulators and auditors | quality | S-12 page 15, Article 15(b) | C-41 |
| R-1807 | The ESAs shall develop draft regulatory technical standards on the mechanisms for prompt detection of anomalous activities and the criteria for ICT-related incident detection and response | regulators and auditors | quality | S-12 page 15, Article 15(c) | C-41 |
| R-1808 | The ESAs shall develop draft regulatory technical standards that specify further the components of the ICT business continuity policy | regulators and auditors | quality | S-12 page 15, Article 15(d) | C-41 |
| R-1809 | The ESAs shall develop draft regulatory technical standards that specify the testing of ICT business continuity plans, including scenarios of deterioration or failure of a critical or important function and the impact of insolvency of ICT third-party service providers | regulators and auditors | quality | S-12 page 15, Article 15(e) | C-41 |
| R-1810 | The ESAs shall develop draft regulatory technical standards that specify the components of the ICT response and recovery plans | regulators and auditors | quality | S-12 page 15, Article 15(f) | C-41 |
| R-1811 | The ESAs shall develop draft regulatory technical standards that specify the content and format of the report on the review of the ICT risk management framework | regulators and auditors | quality | S-12 page 15, Article 15(g) | C-41 |
| R-1812 | When developing the draft regulatory technical standards, the ESAs shall take into account the size and the overall risk profile of the financial entity, and the nature, scale and complexity of its services, activities and operations | regulators and auditors | quality | S-12 page 15, Article 15, third paragraph | C-41 |
| R-1813 | The ESAs shall submit those draft regulatory technical standards to the Commission by 17 January 2024 | regulators and auditors | quality | S-12 page 15, Article 15, fourth paragraph | C-41 |
| R-1814 | Articles 5 to 15 shall not apply to the small and non-interconnected entities listed in Article 16(1) | management | quality | S-12 page 15, Article 16(1) | C-41 |
| R-1815 | Entities listed in Article 16(1) shall put in place and maintain a sound and documented ICT risk management framework that details mechanisms and measures for quick, efficient and comprehensive management of ICT risk | management | quality | S-12 page 15, Article 16(1)(a) | C-40 |
| R-1816 | Entities listed in Article 16(1) shall continuously monitor the security and functioning of all ICT systems | operations engineers | operations | S-12 page 15, Article 16(1)(b) | C-23 |
| R-1817 | Entities listed in Article 16(1) shall minimise the impact of ICT risk through the use of sound, resilient and updated ICT systems, protocols and tools | operations engineers | security | S-12 page 15, Article 16(1)(c) | C-18 |
| R-1818 | Entities listed in Article 16(1) shall allow sources of ICT risk and anomalies to be promptly identified and detected, and ICT-related incidents to be swiftly handled | operations engineers | operations | S-12 page 15, Article 16(1)(d) | C-23 |
| R-1819 | Entities listed in Article 16(1) shall identify key dependencies on ICT third-party service providers | management | security | S-12 page 15, Article 16(1)(e) | C-19 |
| R-1820 | Entities listed in Article 16(1) shall ensure the continuity of critical or important functions, through business continuity plans and response and recovery measures that include at least back-up and restoration measures | management | operations | S-12 page 15, Article 16(1)(f) | C-27 |
| R-1821 | Entities listed in Article 16(1) shall test on a regular basis the plans and measures referred to in point (f), and the effectiveness of the controls implemented under points (a) and (c) | operations engineers | operations | S-12 page 15, Article 16(1)(g) | C-27 |
| R-1822 | Entities listed in Article 16(1) shall implement, as appropriate, relevant operational conclusions from the tests and from post-incident analysis into the ICT risk assessment process | management | quality | S-12 page 15, Article 16(1)(h) | C-35 |
| R-1823 | Entities listed in Article 16(1) shall develop, according to needs and ICT risk profile, ICT security awareness programmes and digital operational resilience training for staff and management | management | quality | S-12 page 15, Article 16(1)(h) | C-39 |
| R-1824 | The ICT risk management framework shall be documented and reviewed periodically and upon the occurrence of major ICT-related incidents, in compliance with supervisory instructions | management | quality | S-12 page 15, Article 16(2) | C-40 |
| R-1825 | The ICT risk management framework shall be continuously improved on the basis of lessons derived from implementation and monitoring | management | quality | S-12 page 15, Article 16(2) | C-35 |
| R-1826 | A report on the review of the ICT risk management framework shall be submitted to the competent authority upon its request | management | quality | S-12 page 15, Article 16(2) | C-41 |
| R-1827 | The ESAs shall develop draft regulatory technical standards that specify the elements of the ICT risk management framework | regulators and auditors | quality | S-12 page 15, Article 16(3)(a) | C-41 |
| R-1828 | The ESAs shall develop draft regulatory technical standards that specify the elements for systems, protocols and tools to minimise the impact of ICT risk, with a view to ensuring the security of networks | regulators and auditors | quality | S-12 page 15, Article 16(3)(b) | C-41 |
| R-1829 | The ESAs shall develop draft regulatory technical standards that specify the components of the ICT business continuity plans | regulators and auditors | quality | S-12 page 15, Article 16(3)(c) | C-41 |
| R-1830 | The ESAs shall develop draft regulatory technical standards that specify the rules on the testing of business continuity plans, including scenarios of deterioration or failure of a critical or important function | regulators and auditors | quality | S-12 page 15, Article 16(3)(d) | C-41 |
| R-1831 | The ESAs shall develop draft regulatory technical standards that specify the content and format of the report on the review of the ICT risk management framework | regulators and auditors | quality | S-12 page 15, Article 16(3)(e) | C-41 |
| R-1832 | When developing the draft regulatory technical standards under Article 16(3), the ESAs shall take into account the size and the overall risk profile of the financial entity, and the nature, scale and complexity of its services | regulators and auditors | quality | S-12 page 15, Article 16, third paragraph | C-41 |
| R-1833 | The ESAs shall submit those draft regulatory technical standards to the Commission by 17 January 2024 | regulators and auditors | quality | S-12 page 15, Article 16, fourth paragraph | C-41 |
| R-1834 | Financial entities shall define, establish and implement an ICT-related incident management process to detect, manage and notify ICT-related incidents | operations engineers | operations | S-12 page 15, Article 17(1) | C-25 |
| R-1835 | Financial entities shall record all ICT-related incidents and significant cyber threats | operations engineers | operations | S-12 page 15, Article 17(2) | C-25 |
| R-1836 | Financial entities shall establish appropriate procedures and processes to ensure a consistent and integrated monitoring, handling and follow-up of ICT-related incidents | operations engineers | operations | S-12 page 15, Article 17(2) | C-25 |
| R-1837 | Those procedures shall ensure that root causes are identified, documented and addressed in order to prevent the occurrence of such incidents | operations engineers | quality | S-12 page 15, Article 17(2) | C-35 |
| R-1838 | The ICT-related incident management process shall put in place early warning indicators | operations engineers | operations | S-12 page 15, Article 17(3)(a) | C-23 |
| R-1839 | Financial entities shall classify ICT-related incidents and determine their impact using listed criteria | operations engineers | operations | S-12 page 16 (Art 18(1)) | C-25 |
| R-1840 | Financial entities shall classify cyber threats as significant based on criticality, number of targeted clients and geographic spread | operations engineers | operations | S-12 page 16 (Art 18(2)) | C-25 |
| R-1841 | ESAs shall, through the Joint Committee and with ECB and ENISA, develop draft technical standards on incident criteria, materiality thresholds and cyber threat thresholds | regulators and auditors | quality | S-12 page 16 (Art 18(3)) | C-41 |
| R-1842 | ESAs shall take into account Article 4(2) criteria and international standards from ENISA when developing draft standards | regulators and auditors | quality | S-12 page 16 (Art 18(4)) | C-41 |
| R-1843 | ESAs shall duly consider that microenterprises and small and medium-sized enterprises must mobilise sufficient resources to manage incidents swiftly | regulators and auditors | quality | S-12 page 16 (Art 18(4)) | C-41 |
| R-1844 | ESAs shall submit draft technical standards on incident classification to the Commission by 17 January 2024 | regulators and auditors | quality | S-12 page 16 (Art 18(4), second paragraph) | C-41 |
| R-1845 | Financial entities shall report major ICT-related incidents to the relevant competent authority | management | operations | S-12 page 16 (Art 19(1)) | C-25 |
| R-1846 | Member States shall designate a single competent authority where an entity is supervised by more than one national competent authority | regulators and auditors | quality | S-12 page 16 (Art 19(1), second paragraph) | C-41 |
| R-1847 | Significant credit institutions shall report major incidents to the designated national authority, which shall immediately transmit the report to the ECB | regulators and auditors | quality | S-12 page 16 (Art 19(1), third paragraph) | C-41 |
| R-1848 | Financial entities shall produce the initial notification and reports using the Article 20 templates and submit them to the competent authority | management | operations | S-12 page 16 (Art 19(1), fourth paragraph) | C-25 |
| R-1849 | Where a technical impossibility prevents template submission, financial entities shall notify the competent authority by alternative means | management | operations | S-12 page 16 (Art 19(1), fourth paragraph) | C-25 |
| R-1850 | Initial notification and reports shall include all information the competent authority needs to determine significance and cross-border impact | management | operations | S-12 page 16 (Art 19(1), fifth paragraph) | C-25 |
| R-1851 | Where a major incident affects clients' financial interests, financial entities shall inform clients without undue delay about the incident and mitigation measures | users and customers | operations | S-12 page 16 (Art 19(3)) | C-25 |
| R-1852 | For a significant cyber threat, financial entities shall, where applicable, inform potentially affected clients of protection measures | users and customers | operations | S-12 page 16 (Art 19(3), second paragraph) | C-25 |
| R-1853 | Financial entities shall submit an initial notification, intermediate reports and a final report within the time limits set under Article 20 | management | operations | S-12 page 16 (Art 19(4)) | C-25 |
| R-1854 | Financial entities shall submit updated intermediate reports when the incident status changes significantly and on request of the competent authority | management | operations | S-12 page 16 (Art 19(4)(b)) | C-25 |
| R-1855 | Financial entities shall submit a final report when root cause analysis is complete and actual impact figures are available | management | operations | S-12 page 16 (Art 19(4)(c)) | C-25 |
| R-1856 | Where reporting is outsourced, the financial entity shall remain fully responsible for fulfilling the incident reporting requirements | management | security | S-12 page 16 (Art 19(5)) | C-19 |
| R-1857 | Competent authorities shall, in a timely manner, pass incident details to EBA, ESMA or EIOPA, the ECB, competent authorities and CSIRTs, resolution authorities and the SRB, and other relevant public authorities | regulators and auditors | quality | S-12 page 16 to 17 (Art 19(6)) | C-41 |
| R-1858 | ESAs and ECB shall assess whether an incident is relevant for other Member States and inform them as soon as possible | regulators and auditors | quality | S-12 page 17 (Art 19(7)) | C-41 |
| R-1859 | The ECB shall notify members of the European System of Central Banks on issues relevant to the payment system | regulators and auditors | quality | S-12 page 17 (Art 19(7)) | C-41 |
| R-1860 | Competent authorities shall take all necessary measures to protect the immediate stability of the financial system | regulators and auditors | quality | S-12 page 17 (Art 19(7)) | C-41 |
| R-1861 | ESMA notification shall be without prejudice to the competent authority duty to urgently transmit details to the host Member State authority in the cases listed | regulators and auditors | quality | S-12 page 17 (Art 19(8)) | C-41 |
| R-1862 | ESAs shall develop draft technical standards on incident report content, time limits and significant cyber threat notification content | regulators and auditors | quality | S-12 page 17 (Art 20(a)) | C-41 |
| R-1863 | ESAs shall develop draft implementing technical standards on standard forms, templates and procedures for incident reporting | regulators and auditors | quality | S-12 page 17 (Art 20(b)) | C-41 |
| R-1864 | ESAs shall submit the draft standards in Article 20 to the Commission by 17 July 2024 | regulators and auditors | quality | S-12 page 17 (Art 20, second paragraph) | C-41 |
| R-1865 | ESAs shall prepare a joint report assessing feasibility of a single EU Hub for incident reporting | regulators and auditors | quality | S-12 page 17 (Art 21(1)) | C-41 |
| R-1866 | The joint report shall comprise at least the listed elements, including risks of concentration of sensitive information | regulators and auditors | quality | S-12 page 17 (Art 21(2)) | C-41 |
| R-1867 | ESAs shall submit the joint report to the European Parliament, the Council and the Commission by 17 January 2025 | regulators and auditors | quality | S-12 page 17 (Art 21(3)) | C-41 |
| R-1868 | Competent authorities shall acknowledge receipt of each initial notification and report | regulators and auditors | quality | S-12 page 17 (Art 22(1)) | C-41 |
| R-1869 | Financial entities shall remain fully responsible for handling and consequences of reported ICT-related incidents | management | quality | S-12 page 17 (Art 22(1)) | C-40 |
| R-1870 | ESAs shall report yearly on major ICT-related incidents on an anonymised and aggregated basis | regulators and auditors | quality | S-12 page 17 (Art 22(2)) | C-41 |
| R-1871 | ESAs shall issue warnings and produce high-level statistics to support threat and vulnerability assessments | regulators and auditors | quality | S-12 page 17 (Art 22(2), second paragraph) | C-41 |
| R-1872 | The chapter requirements shall apply to payment-related incidents of credit institutions, payment institutions, account information service providers and electronic money institutions | management | quality | S-12 page 17 (Art 23) | C-41 |
| R-1873 | Financial entities other than microenterprises shall establish, maintain and review a sound and comprehensive digital operational resilience testing programme | security team | security | S-12 page 17 (Art 24(1)) | C-17 |
| R-1874 | The testing programme shall include a range of assessments, tests, methodologies, practices and tools | security team | security | S-12 page 17 (Art 24(2)) | C-17 |
| R-1875 | Financial entities other than microenterprises shall follow a risk-based approach when conducting the testing programme | security team | security | S-12 page 18 (Art 24(3)) | C-17 |
| R-1876 | Financial entities other than microenterprises shall ensure that tests are undertaken by independent parties, internal or external | quality assurance | quality | S-12 page 18 (Art 24(4)) | C-34 |
| R-1877 | Where an internal tester is used, financial entities shall dedicate sufficient resources and avoid conflicts of interest in design and execution | quality assurance | quality | S-12 page 18 (Art 24(4)) | C-34 |
| R-1878 | Financial entities other than microenterprises shall establish procedures to prioritise, classify and remedy all issues found in tests | security team | quality | S-12 page 18 (Art 24(5)) | C-35 |
| R-1879 | Financial entities other than microenterprises shall establish internal validation methods to confirm that weaknesses are fully addressed | quality assurance | quality | S-12 page 18 (Art 24(5)) | C-34 |
| R-1880 | Financial entities other than microenterprises shall ensure, at least yearly, that appropriate tests are conducted on all ICT systems and applications supporting critical or important functions | security team | security | S-12 page 18 (Art 24(6)) | C-17 |
| R-1881 | The testing programme shall provide for appropriate tests, such as vulnerability scans, source code reviews where feasible, penetration testing and end-to-end testing | security team | security | S-12 page 18 (Art 25(1)) | C-17 |
| R-1882 | Central securities depositories and central counterparties shall perform vulnerability assessments before any deployment or redeployment of applications, infrastructure and ICT services supporting critical or important functions | security team | security | S-12 page 18 (Art 25(2)) | C-11 |
| R-1883 | Microenterprises shall perform tests by combining a risk-based approach with strategic planning of ICT testing | security team | security | S-12 page 18 (Art 25(3)) | C-17 |
| R-1884 | Financial entities other than microenterprises shall carry out advanced TLPT at least every 3 years | security team | security | S-12 page 18 (Art 26(1)) | C-17 |
| R-1885 | Each TLPT shall cover several or all critical or important functions and be performed on live production systems | security team | security | S-12 page 18 (Art 26(2)) | C-17 |
| R-1886 | Financial entities shall identify all relevant underlying ICT systems, processes and technologies, including those outsourced, that support critical or important functions | management | security | S-12 page 18 (Art 26(2), second paragraph) | C-09 |
| R-1887 | Financial entities shall assess which critical or important functions need TLPT coverage, and competent authorities shall validate the result | management | security | S-12 page 18 (Art 26(2), third paragraph) | C-17 |
| R-1888 | Where ICT third-party service providers are in TLPT scope, financial entities shall take measures to ensure their participation and remain fully responsible for compliance | management | security | S-12 page 18 (Art 26(3)) | C-19 |
| R-1889 | Pooled testing shall cover the relevant range of ICT services contracted to the provider and shall be considered TLPT for participating entities | security team | security | S-12 page 18 (Art 26(4), second paragraph) | C-17 |
| R-1890 | The number of entities in pooled testing shall be calibrated to the complexity and types of services involved | security team | security | S-12 page 18 (Art 26(4), third paragraph) | C-17 |
| R-1891 | Financial entities shall, with ICT providers and other parties, apply effective risk management controls to mitigate risks to data, assets and operations during TLPT | security team | security | S-12 page 18 (Art 26(5)) | C-17 |
| R-1892 | At the end of TLPT, financial entities and external testers shall provide the authority a summary of findings, remediation plans and documentation | security team | quality | S-12 page 18 (Art 26(6)) | C-41 |
| R-1893 | Financial entities shall notify the competent authority of the attestation, summary of findings and remediation plans | management | quality | S-12 page 18 (Art 26(7)) | C-41 |
| R-1894 | Financial entities shall remain fully responsible for the impact of the tests in Article 26(4) | management | quality | S-12 page 18 (Art 26(7), second paragraph) | C-40 |
| R-1895 | Financial entities shall contract testers for TLPT in accordance with Article 27 | security team | security | S-12 page 18 (Art 26(8)) | C-17 |
| R-1896 | Where internal testers are used for TLPT, financial entities shall contract external testers every three tests | security team | security | S-12 page 18 (Art 26(8)) | C-17 |
| R-1897 | Significant credit institutions shall use only external testers that meet Article 27(1)(a) to (e) | security team | security | S-12 page 18 (Art 26(8), second paragraph) | C-17 |
| R-1898 | Competent authorities shall identify financial entities required to perform TLPT based on impact, financial stability and ICT risk profile factors | regulators and auditors | security | S-12 page 18 (Art 26(8), third paragraph) | C-17 |
| R-1899 | ESAs shall, with the ECB, develop joint draft technical standards on TLPT under the TIBER-EU framework and submit them by 17 July 2024 | regulators and auditors | security | S-12 page 18 (Art 26(11)) | C-17 |
| R-1900 | Financial entities shall only use testers that have the highest suitability and reputability and specific expertise in threat intelligence, penetration testing and red team testing | management | security | S-12 page 18 (Art 27(1)) | C-17 |
| R-1901 | Reduce the batch size of changes. | software engineers | quality | S-13 page guide, Next steps | C-36 |
| R-1902 | Gather a cross-functional team that prioritizes, builds, delivers and operates the application. | software engineers | quality | S-13 page guide, Next steps | C-40 |
| R-1903 | Set a baseline with the DORA Quick Check. | software engineers | operations | S-13 page guide, Next steps | C-28 |
| R-1904 | Discuss friction points, optionally by mapping the delivery process. | software engineers | operations | S-13 page guide, Next steps | C-28 |
| R-1905 | Commit as a team to improve the most significant constraint or bottleneck. | software engineers | operations | S-13 page guide, Next steps | C-28 |
| R-1906 | Turn the commitment into a plan with leading indicators. | software engineers | operations | S-13 page guide, Next steps | C-28 |
| R-1907 | Check progress with the Quick Check, conversations and retrospectives, then repeat the cycle. | software engineers | operations | S-13 page guide, Next steps | C-28 |
| R-1908 | All five metrics should be shared across development, operations and release teams. | software engineers | operations | S-13 page guide, Common pitfalls | C-28 |
| R-1909 | Teams should use several metrics, with some healthy tension between them. | software engineers | operations | S-13 page guide, Common pitfalls | C-28 |
| R-1910 | Build security into the lifecycle without slowing delivery. | software engineers | security | S-13 page capabilities, core group, Pervasive security | C-13 |
| R-1911 | Use continuous delivery so that deployment to production is low-risk and on demand. | operations engineers | operations | S-13 page capabilities, core group | C-21 |
| R-1912 | Practice continuous integration and measure and improve its common mistakes. | software engineers | quality | S-13 page capabilities, core group | C-30 |
| R-1913 | Automate tests reliably across the delivery lifecycle. | quality assurance | quality | S-13 page capabilities, core group | C-31 |
| R-1914 | Automate deployment to reduce manual intervention in releases. | operations engineers | operations | S-13 page capabilities, core group | C-20 |
| R-1915 | Build monitoring and observability tooling to understand and debug production. | operations engineers | operations | S-13 page capabilities, core group | C-23 |
| R-1916 | Manage database changes so they do not cause problems or slow delivery. | software engineers | operations | S-13 page capabilities, core group | C-20 |
| R-1917 | Keep code easy to find, reuse and change, with up-to-date dependencies. | software engineers | security | S-13 page capabilities, core group | C-10 |
| R-1918 | Use version control for reproducibility and traceability. | software engineers | security | S-13 page capabilities, AI and core groups | C-01 |
| R-1919 | Work in small batches. | software engineers | quality | S-13 page capabilities, AI and core groups | C-36 |
| R-1920 | Replace heavy approval processes with peer review. | software engineers | security | S-13 page capabilities, core group | C-02 |
| R-1921 | Set up proactive failure notification that surfaces critical issues early. | operations engineers | operations | S-13 page capabilities, untagged group | C-23 |
| R-1922 | Use trunk-based development to avoid merge-conflict problems. | software engineers | quality | S-13 page capabilities, untagged group | C-36 |
| R-1923 | Limit work in process to focus on high-priority items. | software engineers | quality | S-13 page capabilities, untagged group | C-42 |
| R-1924 | Keep documentation accurate, organized and user-centric. | software engineers | quality | S-13 page capabilities, core group | C-37 |
| R-1925 | Use a clear AI policy to reduce risk and support safe experimentation. | management | quality | S-13 page capabilities, AI group | C-40 |
| R-1926 | Reliable services require reliable, reproducible and automated release processes. | operations engineers | operations | S-14 RE > Release Engineering (intro) | C-20 |
| R-1927 | Changes to the release process should be intentional. | operations engineers | operations | S-14 RE > Release Engineering (intro) | C-26 |
| R-1928 | Teams must be self-sufficient to operate at scale. | operations engineers | operations | S-14 RE > Self-Service Model | C-20 |
| R-1929 | Releases should require engineer involvement only when problems arise. | operations engineers | operations | S-14 RE > Self-Service Model | C-20 |
| R-1930 | Builds must be insensitive to host-installed software. | software engineers | security | S-14 RE > Hermetic Builds | C-03 |
| R-1931 | Builds must depend on pinned tool and library versions. | software engineers | security | S-14 RE > Hermetic Builds | C-10 |
| R-1932 | Builds must not rely on external services. | software engineers | security | S-14 RE > Hermetic Builds | C-03 |
| R-1933 | Almost all codebase changes require code review. | software engineers | security | S-14 RE > Enforcement of Policies and Procedures | C-02 |
| R-1934 | Gated operations require approval: source changes, release actions, release creation, integration proposals, cherry picks, deployment and build configuration. | software engineers | security | S-14 RE > Enforcement of Policies and Procedures | C-02 |
| R-1935 | Each release produces an archived change report. | operations engineers | operations | S-14 RE > Enforcement of Policies and Procedures | C-45 |
| R-1936 | Fixes go to mainline first, then are cherry picked into the release branch. | software engineers | operations | S-14 RE > Branching | C-45 |
| R-1937 | Release branches are never merged back. | software engineers | operations | S-14 RE > Branching | C-45 |
| R-1938 | A continuous test system runs unit tests on each submitted change. | software engineers | quality | S-14 RE > Testing | C-30 |
| R-1939 | Continuous build test targets should match release gating targets. | software engineers | quality | S-14 RE > Testing | C-30 |
| R-1940 | Releases should come from the last revision that fully passed continuous tests. | software engineers | quality | S-14 RE > Testing | C-30 |
| R-1941 | Unit tests are re-run on the release branch with an audit trail. | quality assurance | quality | S-14 RE > Testing | C-31 |
| R-1942 | System-level tests run independently on packaged artifacts. | quality assurance | quality | S-14 RE > Testing | C-31 |
| R-1943 | Packages are named, versioned with a unique hash, and signed. | software engineers | security | S-14 RE > Packaging | C-16 |
| R-1944 | Binaries expose a flag that shows build date, revision and build identifier. | software engineers | operations | S-14 RE > Building | C-45 |
| R-1945 | Teams should budget for release engineering at the start of product development. | management | quality | S-14 RE > Conclusions: Start Release Engineering at the Beginning | C-42 |
| R-1946 | Developers, SREs and release engineers must collaborate, not hand results over the fence. | software engineers | quality | S-14 RE > Conclusions: Start Release Engineering at the Beginning | C-40 |
| R-1947 | Release engineers and SREs jointly develop canarying strategies, non-disruptive rollouts and rollback procedures. | operations engineers | operations | S-14 RE > The Role of a Release Engineer | C-21 |
| R-1948 | Deployment strategy scales with risk. | operations engineers | operations | S-14 RE > Deployment | C-21 |
| R-1949 | Configuration is stored in the primary source repository with strict code review. | operations engineers | operations | S-14 RE > Configuration Management | C-20 |
| R-1950 | Dashboards should include the four golden signals. | operations engineers | operations | S-14 MON > Why Monitor | C-23 |
| R-1951 | Keep monitoring simple and avoid magic systems that learn thresholds or infer causality. | operations engineers | operations | S-14 MON > Setting Reasonable Expectations | C-23 |
| R-1952 | Keep the paging path simple and robust. | operations engineers | operations | S-14 MON > Setting Reasonable Expectations | C-23 |
| R-1953 | Monitoring should answer what is broken and why. | operations engineers | operations | S-14 MON > Symptoms Versus Causes | C-23 |
| R-1954 | Prioritise symptoms for paging. | operations engineers | operations | S-14 MON > Symptoms Versus Causes | C-23 |
| R-1955 | Use heavy white-box monitoring and modest black-box monitoring. | operations engineers | operations | S-14 MON > Black-Box Versus White-Box | C-23 |
| R-1956 | Track failed-request latency separately. | operations engineers | operations | S-14 MON > Four Golden Signals | C-23 |
| R-1957 | Set a utilisation target, since systems degrade before 100 percent. | operations engineers | operations | S-14 MON > Four Golden Signals | C-27 |
| R-1958 | Do not rely on means for latency. Use histograms. | operations engineers | operations | S-14 MON > Tail Latency | C-23 |
| R-1959 | Keep alerting rules simple and predictable. | operations engineers | operations | S-14 MON > Simplicity | C-23 |
| R-1960 | Remove rarely exercised alerting. | operations engineers | operations | S-14 MON > Simplicity | C-23 |
| R-1961 | Remove signals that feed no dashboard or alert. | operations engineers | operations | S-14 MON > Simplicity | C-23 |
| R-1962 | Keep monitoring loosely coupled from profiling, load testing and log analysis. | operations engineers | operations | S-14 MON > Simplicity | C-23 |
| R-1963 | Evaluate each alerting rule for urgency, actionability, user impact, possible automation and duplication. | operations engineers | operations | S-14 MON > Alerting Questions | C-23 |
| R-1964 | Every page should be actionable, require intelligence, and concern a novel problem. | operations engineers | operations | S-14 MON > Alerting Questions | C-23 |
| R-1965 | Frequent alerts with rote responses should be automated or have their root causes eliminated. | operations engineers | operations | S-14 MON > Long-Term Monitoring | C-23 |
| R-1966 | Pages with rote, algorithmic responses should be a red flag. | operations engineers | operations | S-14 MON > Long-Term Monitoring (Gmail case study) | C-23 |
| R-1967 | Favour dashboards over email alerts for subcritical problems. | operations engineers | operations | S-14 MON > Conclusion | C-23 |
| R-1968 | Pair dashboards with logs for historical correlation. | operations engineers | operations | S-14 MON > Conclusion | C-23 |
| R-1969 | A person should never trigger an alert only because something seems a bit weird. Security auditing is the exception. | operations engineers | operations | S-14 MON > Why Monitor | C-23 |
| R-1970 | The launch process should be lightweight, robust, thorough, scalable and adaptable. | operations engineers | operations | S-14 LAUNCH > Setting Up a Launch Process | C-29 |
| R-1971 | Each checklist question must be justified, ideally by a past launch disaster. | operations engineers | operations | S-14 LAUNCH > The Launch Checklist | C-29 |
| R-1972 | Each checklist instruction must be concrete and reasonable. | operations engineers | operations | S-14 LAUNCH > The Launch Checklist | C-29 |
| R-1973 | The full checklist is reviewed once or twice a year for obsolete items. | operations engineers | operations | S-14 LAUNCH > The Launch Checklist | C-29 |
| R-1974 | Keep the intent of each question in mind rather than applying it mechanically. | operations engineers | operations | S-14 LAUNCH > Launching the Unexpected | C-29 |
| R-1975 | For new product types, build a new checklist from first principles and consult domain experts. | operations engineers | operations | S-14 LAUNCH > Launching the Unexpected | C-29 |
| R-1976 | LCEs must meet the same technical bar as SREs. | operations engineers | quality | S-14 LAUNCH > Launch Coordination Engineering | C-39 |
| R-1977 | LCEs should identify and escalate pain points. | operations engineers | operations | S-14 LAUNCH > Driving Convergence and Simplification | C-29 |
| R-1978 | Use shared, hardened infrastructure instead of custom solutions. | operations engineers | security | S-14 LAUNCH > Driving Convergence and Simplification | C-18 |
| R-1979 | Document all manual processes so any team member can run them in an emergency. | operations engineers | quality | S-14 LAUNCH > Processes and Automation | C-37 |
| R-1980 | Automate building and releasing. | operations engineers | operations | S-14 LAUNCH > Processes and Automation | C-20 |
| R-1981 | Keep code and configuration in version control. Cut each release on its own release branch. | software engineers | operations | S-14 LAUNCH > Development Process | C-20 |
| R-1982 | Isolate user-facing requests from non-user-facing requests. | software engineers | operations | S-14 LAUNCH > Architecture and Dependencies | C-29 |
| R-1983 | Validate request-volume assumptions. | operations engineers | operations | S-14 LAUNCH > Architecture and Dependencies | C-29 |
| R-1984 | Set up DNS, load balancers and monitoring. | operations engineers | operations | S-14 LAUNCH > Integration | C-29 |
| R-1985 | Launch in one region first. | operations engineers | operations | S-14 LAUNCH > Capacity Planning | C-21 |
| R-1986 | Request datacenter and network resources well in advance. | operations engineers | operations | S-14 LAUNCH > Capacity Planning | C-27 |
| R-1987 | Load testing is required for most launches. | quality assurance | quality | S-14 LAUNCH > Overload and load tests | C-31 |
| R-1988 | Check for single points of failure. | operations engineers | operations | S-14 LAUNCH > Failure Modes | C-27 |
| R-1989 | Implement request deadlines and load shedding. | software engineers | operations | S-14 LAUNCH > Failure Modes | C-27 |
| R-1990 | Plan for degraded mode when dependencies fail. | software engineers | operations | S-14 LAUNCH > Failure Modes | C-27 |
| R-1991 | Prepare for DoS attacks. | operations engineers | security | S-14 LAUNCH > Failure Modes | C-44 |
| R-1992 | Clients should back off exponentially on failure and jitter automatic requests. | software engineers | operations | S-14 LAUNCH > Client Behavior | C-27 |
| R-1993 | Do not retry 4xx errors. Network errors usually warrant retry. | software engineers | operations | S-14 LAUNCH > Client Behavior | C-27 |
| R-1994 | Randomise periodic client timing. | software engineers | operations | S-14 LAUNCH > Selected Techniques | C-27 |
| R-1995 | Ship dormant features so they can be switched off without a new app release. | software engineers | operations | S-14 LAUNCH > Selected Techniques | C-21 |
| R-1996 | Roll out gradually: canary first, then one datacenter, then globally. Roll back automatically on failed validation. | operations engineers | operations | S-14 LAUNCH > Selected Techniques | C-21 |
| R-1997 | Apply gradual rollouts to mobile apps too. | operations engineers | operations | S-14 LAUNCH > Selected Techniques | C-21 |
| R-1998 | Increase feature exposure gradually, typically 1 to 10 percent. | operations engineers | operations | S-14 LAUNCH > Selected Techniques | C-21 |
| R-1999 | Failures in new code paths should not affect users. | software engineers | operations | S-14 LAUNCH > Selected Techniques | C-21 |
| R-2000 | Each change must be independently revertible and measurable. | software engineers | operations | S-14 LAUNCH > Selected Techniques | C-21 |
| R-2001 | Identify third-party code, data and services. Notify partners of launches. Plan for missed vendor deadlines. | operations engineers | security | S-14 LAUNCH > Checklist Themes (External Dependencies) | C-19 |
| R-2002 | Create a launch plan with a named owner for each item. Prepare contingencies for each risk. | operations engineers | operations | S-14 LAUNCH > Rollout Planning | C-29 |
| R-2003 | Back up persistent data and rate-limit to prevent abuse. | operations engineers | operations | S-14 LAUNCH > The Launch Checklist (example actions) | C-27 |
| R-2004 | SRE's goal is to keep operational work at or below 50 percent. | operations engineers | quality | S-14 LAUNCH > Development of LCE | C-40 |
| R-2005 | Infrastructure churn should be handled with automated migration tools. | operations engineers | quality | S-14 LAUNCH > Development of LCE | C-43 |
| R-2006 | Define SLIs carefully. | operations engineers | operations | S-14 SLO > Service Level Terminology | C-24 |
| R-2007 | Use only a few representative SLIs. | operations engineers | operations | S-14 SLO > Indicators in Practice | C-24 |
| R-2008 | Collect most indicators server-side. Use client-side collection where server metrics miss user-visible problems. | operations engineers | operations | S-14 SLO > Collecting Indicators | C-24 |
| R-2009 | Be careful with aggregation windows. | operations engineers | operations | S-14 SLO > Aggregation | C-24 |
| R-2010 | Prefer distributions and percentiles to averages. | operations engineers | operations | S-14 SLO > Aggregation | C-24 |
| R-2011 | Do not assume data is normally distributed without verifying it. | operations engineers | operations | S-14 SLO > Aggregation | C-24 |
| R-2012 | Standardise SLI definitions and build reusable templates. | operations engineers | operations | S-14 SLO > Standardize Indicators | C-24 |
| R-2013 | Specify how each SLO is measured and when it is valid. | operations engineers | operations | S-14 SLO > Defining Objectives | C-24 |
| R-2014 | Do not require 100 percent compliance. Use an error budget. | operations engineers | operations | S-14 SLO > Defining Objectives | C-24 |
| R-2015 | Track the error budget daily or weekly, with review monthly or quarterly by management. | management | operations | S-14 SLO > Defining Objectives | C-24 |
| R-2016 | Use separate objectives for throughput-oriented and latency-oriented clients. | operations engineers | operations | S-14 SLO > Defining Objectives | C-24 |
| R-2017 | Do not base targets on current performance. | operations engineers | operations | S-14 SLO > Choosing Targets | C-24 |
| R-2018 | Keep SLIs simple. Avoid absolutes. | operations engineers | operations | S-14 SLO > Choosing Targets | C-24 |
| R-2019 | Keep the SLO count minimal and defend each one. | operations engineers | operations | S-14 SLO > Choosing Targets | C-24 |
| R-2020 | Start loose and tighten over time. | operations engineers | operations | S-14 SLO > Choosing Targets | C-24 |
| R-2021 | Product and business considerations are involved in choosing targets. SRE advises on risk and viability. | management | operations | S-14 SLO > Choosing Targets | C-24 |
| R-2022 | Monitor SLIs, compare them to SLOs, decide whether action is needed, and take action. | operations engineers | operations | S-14 SLO > Control Measures | C-24 |
| R-2023 | Keep an internal SLO tighter than the published one as a safety margin. | operations engineers | operations | S-14 SLO > SLOs Set Expectations | C-24 |
| R-2024 | Do not overachieve. Occasionally take the system offline, throttle requests, or avoid being faster under light load. | operations engineers | operations | S-14 SLO > SLOs Set Expectations | C-24 |
| R-2025 | Use results to decide whether to invest in performance or redirect staff. | management | operations | S-14 SLO > SLOs Set Expectations | C-24 |
| R-2026 | Business and legal teams choose SLA consequences and penalties. SRE advises on likelihood and difficulty. | management | operations | S-14 SLO > Agreements in Practice | C-24 |
| R-2027 | Be conservative in what is advertised, since SLAs are hard to change once published. | management | operations | S-14 SLO > Agreements in Practice | C-24 |
| R-2028 | Ask what happens if the SLOs are not met. | management | operations | S-14 SLO > Agreements in Practice | C-24 |
| R-2029 | Correctness is usually not an SRE responsibility to meet. | operations engineers | operations | S-14 SLO > Indicators in Practice | C-24 |
| R-2030 | Keep global Chubby near its SLO but not far above it. Synthesise a controlled outage each quarter if no real failure breaches the target. | operations engineers | operations | S-14 SLO > sidebar: The Global Chubby Planned Outage | C-24 |
| R-2031 | Write a postmortem after any significant undesirable event. | operations engineers | operations | S-14 ch. 15, practices | C-25 |
| R-2032 | Define postmortem triggers before an incident occurs. | operations engineers | operations | S-14 ch. 15, practices | C-25 |
| R-2033 | Use objective triggers: user-visible downtime beyond a threshold, any data loss, on-call intervention, resolution time beyond a threshold, and monitoring failure. | operations engineers | operations | S-14 ch. 15, triggers | C-25 |
| R-2034 | Allow any stakeholder to request a postmortem. | operations engineers | operations | S-14 ch. 15, practices | C-25 |
| R-2035 | Keep postmortems blameless and focus on contributing causes. | operations engineers | operations | S-14 ch. 15, practices | C-25 |
| R-2036 | Have senior engineers review a draft for completeness before it is final. | operations engineers | operations | S-14 ch. 15, practices | C-25 |
| R-2037 | Hold regular review sessions so no postmortem stays unreviewed. | operations engineers | operations | S-14 ch. 15, practices | C-25 |
| R-2038 | Store finished postmortems in a team or organization repository. | operations engineers | operations | S-14 ch. 15, practices | C-25 |
| R-2039 | Exclude information that could identify end users from postmortems. | operations engineers | operations | S-14 ch. 15, practices | C-25 |
| R-2040 | Survey teams regularly on the postmortem process and its toil. | operations engineers | operations | S-14 ch. 15, practices | C-25 |
| R-2041 | Trial the postmortem process and reward good postmortems through performance management. | management | operations | S-14 ch. 15, practices | C-25 |
| R-2042 | Balance reliability against feature velocity and cost, not maximize uptime. | management | operations | S-14 ch. 3, practices | C-24 |
| R-2043 | Measure availability as request success rate over a rolling window for globally distributed services. | operations engineers | operations | S-14 ch. 3, practices | C-24 |
| R-2044 | Set availability targets per quarter and track performance weekly or daily. | operations engineers | operations | S-14 ch. 3, practices | C-24 |
| R-2045 | Define an error budget jointly by product and SRE teams, based on an SLO measured by monitoring. | management | operations | S-14 ch. 3, practices | C-24 |
| R-2046 | Halt releases for a time when the error budget is used up, and slow or roll back releases when it is nearly used up. | operations engineers | operations | S-14 ch. 3, practices | C-24 |
| R-2047 | Use canarying to test releases on a small subset of the workload. | operations engineers | operations | S-14 ch. 3, practices | C-21 |
| R-2048 | Give SRE teams authority to halt launches when the SLO is broken. | management | quality | S-14 ch. 3, conditions | C-40 |
| R-2049 | Offer infrastructure at defined service levels so clients can trade cost against risk. | operations engineers | operations | S-14 ch. 3, practices | C-24 |
| R-2050 | Document the architecture, server types and client request types. | operations engineers | quality | S-14 appendix E, architecture | C-38 |
| R-2051 | Plan machines, bandwidth, N+2 redundancy and network QoS. | operations engineers | operations | S-14 appendix E, machines and datacenters | C-27 |
| R-2052 | Estimate traffic including the launch spike and a six-month outlook, and run load and end-to-end tests. | operations engineers | operations | S-14 appendix E, volume, capacity and performance | C-27 |
| R-2053 | Define behavior when a machine, rack, cluster or inter-datacenter network fails. | operations engineers | operations | S-14 appendix E, system reliability and failover | C-27 |
| R-2054 | For each backend, define failure detection, safe restart, load balancing, rate limiting, timeouts, retries and error handling. | operations engineers | operations | S-14 appendix E, system reliability and failover | C-27 |
| R-2055 | Plan data backup, restore and disaster recovery. | operations engineers | operations | S-14 appendix E, system reliability and failover | C-27 |
| R-2056 | Monitor internal state and end-to-end behavior, manage alerts, and monitor the monitoring system. | operations engineers | operations | S-14 appendix E, monitoring and server management | C-23 |
| R-2057 | Complete a security design review and code audit. | security team | security | S-14 appendix E, security | C-12 |
| R-2058 | Address spam risk, authentication and SSL, control prelaunch visibility and access, and manage blacklists. | security team | security | S-14 appendix E, security | C-44 |
| R-2059 | Define change control for servers, data and configs. | operations engineers | operations | S-14 appendix E, automation and manual tasks | C-26 |
| R-2060 | Use a release process with repeatable builds, canary releases under live traffic and staged rollouts. | operations engineers | operations | S-14 appendix E, automation and manual tasks | C-21 |
| R-2061 | Maintain spare capacity and plan for 10x growth with growth alerts. | operations engineers | operations | S-14 appendix E, growth | C-27 |
| R-2062 | Assess third-party systems and degrade gracefully when they fail. | operations engineers | security | S-14 appendix E, external dependencies | C-19 |
| R-2063 | Define standard operating procedures for the service. | operations engineers | quality | S-14 appendix E, schedule and rollout | C-37 |
| R-2064 | Account for hard deadlines and external events in the launch schedule. | operations engineers | quality | S-14 appendix E, schedule and rollout | C-42 |
| R-2065 | Use tests to show that behavior is unchanged across code or configuration changes. | quality assurance | quality | S-14 ch. 17, practices | C-31 |
| R-2066 | Layer unit, integration and system tests. | quality assurance | quality | S-14 ch. 17, practices | C-31 |
| R-2067 | Run configuration, stress and canary tests in production. | quality assurance | quality | S-14 ch. 17, practices | C-31 |
| R-2068 | Turn every reported bug into a regression test. | quality assurance | quality | S-14 ch. 17, practices | C-31 |
| R-2069 | Use source control and a continuous build that notifies engineers at once when a change breaks the build. | software engineers | quality | S-14 ch. 17, practices | C-30 |
| R-2070 | Fix broken builds before other work. | software engineers | quality | S-14 ch. 17, practices | C-30 |
| R-2071 | Use dependency injection to mock complex dependencies. | software engineers | quality | S-14 ch. 17, practices | C-31 |
| R-2072 | Use monitoring probes in production and gate rollouts on problematic version combinations. | operations engineers | operations | S-14 ch. 17, practices | C-21 |
| R-2073 | Use barrier mechanisms so risky tools can reach only unhealthy replicas. | operations engineers | operations | S-14 ch. 17, practices | C-21 |
| R-2074 | Pair integration tests with deadline checks for configuration loading. | quality assurance | quality | S-14 ch. 17, practices | C-31 |
| R-2075 | Prefer bounded-runtime formats, or YAML with a safe parser. | software engineers | security | S-14 ch. 17, practices | C-13 |
| R-2076 | Have tools report problems rather than auto-remediate them. | operations engineers | operations | S-14 ch. 17, practices | C-23 |
| R-2077 | Provide a break-glass mechanism for urgent config pushes, with follow-up. | operations engineers | operations | S-14 ch. 17, practices | C-26 |
| R-2078 | Match test coverage to reliability needs; life-critical and revenue-critical systems need higher test quality and coverage. | quality assurance | quality | S-14 ch. 17, conditions | C-31 |
| R-2079 | Classify config files as MTTR-driven or release-driven and match test coverage to each. | quality assurance | quality | S-14 ch. 17, conditions | C-31 |
| R-2080 | Version control should be used to track changes to all files needed to build or run the system. | software engineers | security | S-15 /learn/version-control/ Definition | C-01 |
| R-2081 | Only a centralised or a distributed version control system is truly appropriate for production software. | software engineers | security | S-15 /learn/version-control/ Types of Version Control | C-01 |
| R-2082 | Define branch-management practices for merging. | software engineers | security | S-15 /learn/ci/ Best Practices in Action, Merging | C-01 |
| R-2083 | Every build should produce binaries and a versioned application package tied to the version tag. | software engineers | operations | S-15 /learn/ci/ Build Best Practices | C-46 |
| R-2084 | Every build should produce a bill of materials report. | software engineers | security | S-15 /learn/ci/ Build Best Practices | C-09 |
| R-2085 | A bill of materials report is required at minimum for production releases. | software engineers | security | S-15 /learn/ci/ Build Best Practices | C-09 |
| R-2086 | Every build should produce a difference report between two bills of materials, used to approve updates before release. | software engineers | security | S-15 /learn/ci/ Build Best Practices | C-09 |
| R-2087 | Build scripts should follow basic guidelines. | software engineers | security | S-15 /learn/ci/ Build Best Practices | C-03 |
| R-2088 | Do not use wildcard includes; list every file explicitly. | software engineers | security | S-15 /learn/ci/ Do not use wildcard includes | C-03 |
| R-2089 | Build flags such as debug settings should not reach production. | software engineers | security | S-15 /learn/ci/ Know Your Build Parameters | C-13 |
| R-2090 | Store and share binaries in a binary repository, tagged with the matching version-control tag. | software engineers | operations | S-15 /learn/ci/ Binary Repository | C-46 |
| R-2091 | All types of automated tests should run on every commit to version control. | software engineers | quality | S-15 /learn/testing/ Description and Scope | C-30 |
| R-2092 | Developers should run automated tests on their workstations as much as possible. | software engineers | quality | S-15 /learn/testing/ Description and Scope | C-31 |
| R-2093 | Testers should perform exploratory testing continuously against the latest CI builds. | quality assurance | quality | S-15 /learn/testing/ Description and Scope | C-31 |
| R-2094 | Testing should happen continuously, not only after a feature is dev complete. | quality assurance | quality | S-15 /learn/testing/ Definition | C-31 |
| R-2095 | Low-value tests should be removed or improved. | quality assurance | quality | S-15 /learn/testing/ Why Continuous Testing | C-31 |
| R-2096 | Testing in production requires strong automation and best practices. | quality assurance | quality | S-15 /learn/testing/ Testing in Production | C-31 |
| R-2097 | Keep environment-specific values separate from deployment logic. | operations engineers | operations | S-15 /learn/cd/ Repeatability | C-20 |
| R-2098 | Use reusable, templated tasks instead of ad hoc scripts. | operations engineers | operations | S-15 /learn/cd/ Automation to Reduce One-Off Scripting | C-20 |
| R-2099 | Maintain a logical view of endpoints, their owners and capabilities, and report on configuration differences. | operations engineers | operations | S-15 /learn/cd/ Environment Modeling | C-45 |
| R-2100 | Use notified, documented approvals for release stages, especially in regulated industries that require separation of duties. | operations engineers | operations | S-15 /learn/cd/ Approval and Approval Gates | C-26 |
| R-2101 | Track automated and manual steps, with logs showing who, when and where. | operations engineers | operations | S-15 /learn/cd/ Release Coordination and Auditing | C-26 |
| R-2102 | Record which artifacts run in which environments. | operations engineers | operations | S-15 /learn/cd/ Inventory Tracking | C-45 |
| R-2103 | Use an environment-based calendar to show scheduled releases. | operations engineers | operations | S-15 /learn/cd/ Calendar and Scheduling | C-21 |
| R-2104 | Keep release metadata and logic fixed so that deployments can be re-run with no manual changes. | operations engineers | operations | S-15 /learn/cd/ Immutable Deployments | C-20 |
| R-2105 | Support canary, blue/green and rolling blue/green releases. | operations engineers | operations | S-15 /learn/cd/ Deployment Models | C-21 |
| R-2106 | Encode organisational guardrails as rules that the automation enforces. | operations engineers | operations | S-15 /learn/cd/ Policies | C-20 |
| R-2107 | Identify every software asset that the product depends on, and verify its ongoing provenance. | software engineers | security | S-15 /learn/supplychain/security/ Core Practices | C-10 |
| R-2108 | Have systems that detect supply chain tampering and let you act on it immediately. | security team | security | S-15 /learn/supplychain/security/ Core Practices | C-18 |
| R-2109 | Secure the systems used to create the product, and detect and respond to attempts to subvert the build. | security team | security | S-15 /learn/supplychain/security/ Core Practices | C-18 |
| R-2110 | Ideally, provide customers with strong assurance of build integrity as provenance. | users and customers | security | S-15 /learn/supplychain/security/ Core Practices | C-04 |
| R-2111 | Use multiple peer reviews of code changes. | software engineers | security | S-15 /learn/supplychain/security/ Attack Vectors | C-02 |
| R-2112 | Audit all codebase changes against known work activity. | quality assurance | security | S-15 /learn/supplychain/security/ Attack Vectors | C-02 |
| R-2113 | Validate dependency provenance on every build, not only through one-off reviews. | software engineers | security | S-15 /learn/supplychain/security/ Attack Vectors | C-10 |
| R-2114 | Extend provenance into deployment, including customers' build and deployment processes and third-party mirrors. | users and customers | security | S-15 /learn/supplychain/security/ Attack Vectors | C-16 |
| R-2115 | Use local caching and manage its risks: stale data, slow response to new CVEs, cache poisoning. | software engineers | security | S-15 /learn/supplychain/security/ Attack Vectors | C-10 |
| R-2116 | Use defence in depth with multiple parallel security analysis tools. | security team | security | S-15 /learn/supplychain/security/ Attack Vectors | C-11 |
| R-2117 | Secure the ML training infrastructure. | security team | security | S-15 /learn/supplychain/security/ Attack Vectors | C-18 |
| R-2118 | Limit the number of people with full access to the product codebase, build and release governance, and audit trail. | security team | security | S-15 /learn/supplychain/security/ Governance and Separation of Concerns | C-08 |
| R-2119 | Add audit processes that monitor changes across all three governance areas. | quality assurance | security | S-15 /learn/supplychain/security/ Governance and Separation of Concerns | C-08 |
| R-2120 | Map relationships between artifacts, application versions and environments. | operations engineers | operations | S-15 /learn/config/ Dependency Management | C-45 |
| R-2121 | Identify vulnerabilities, licence usage and policy conformance in transitive open source dependencies. | software engineers | security | S-15 /learn/config/ Library Management | C-11 |
| R-2122 | Assess the blast radius of a change before release. | operations engineers | operations | S-15 /learn/config/ Impact Analysis | C-26 |
| R-2123 | Version key-value pairs and configuration maps per environment, store them centrally, and compare them across environments. | operations engineers | operations | S-15 /learn/config/ Variables Management | C-20 |
| R-2124 | Provide comparison reports, relationship reports and an audit log that records when, why, what and who changed something. | operations engineers | operations | S-15 /learn/config/ Configuration Reports | C-45 |
| R-2125 | Use Domain Driven Design to organise reusable services and limit service sprawl. | software engineers | quality | S-15 /learn/config/ DDD and SOA | C-38 |
| R-2126 | The source argues for automating configuration management within CD pipelines. | operations engineers | operations | S-15 /learn/config/ Description and Scope | C-20 |
| R-2127 | Practices require collaboration across functional teams. | management | quality | S-15 /learn/ (landing) | C-40 |
| R-2128 | Newcomers should start with the Overview section. | software engineers | quality | S-15 /learn/ (landing) | C-37 |
| R-2129 | Experienced readers should use the assessment tools to set priorities. | software engineers | quality | S-15 /learn/ (landing) | C-37 |
| R-2130 | Every change is reviewed before it is committed. | software engineers | security | S-16 ch09 / Code Review Flow | C-02 |
| R-2131 | One peer LGTM is required by default. | software engineers | security | S-16 ch09 / How Code Review Works at Google | C-02 |
| R-2132 | Authors must resolve all review comments before committing. | software engineers | security | S-16 ch09 / Code Review Flow | C-02 |
| R-2133 | Keep owner lists small and focused. | software engineers | quality | S-16 ch09 / Ownership | C-40 |
| R-2134 | Do not use ownership as an initiation rite. | software engineers | quality | S-16 ch09 / Ownership | C-40 |
| R-2135 | Departing members should hand off ownership promptly. | software engineers | quality | S-16 ch09 / Ownership | C-40 |
| R-2136 | Owners should understand their code or know who does. | software engineers | quality | S-16 ch09 / Ownership | C-40 |
| R-2137 | Justify a new feature before building it. | software engineers | quality | S-16 ch09 / Code Is a Liability | C-38 |
| R-2138 | Check for existing code before writing new code. | software engineers | quality | S-16 ch09 / Code Is a Liability | C-38 |
| R-2139 | Communicate designs to the relevant groups before writing new code. | software engineers | quality | S-16 ch09 / Code Is a Liability | C-38 |
| R-2140 | Code review is not the place to revisit prior design decisions. | software engineers | security | S-16 ch09 / Code Is a Liability | C-02 |
| R-2141 | Reviewers check testing, design, function and efficiency. | quality assurance | security | S-16 ch09 / Code Correctness | C-02 |
| R-2142 | Reviewers give deference to author approaches and propose alternatives only to improve comprehension or function. | quality assurance | security | S-16 ch09 / Code Correctness | C-02 |
| R-2143 | Reviewers approve changes that improve the codebase rather than wait for a perfect solution. | quality assurance | security | S-16 ch09 / Code Correctness | C-02 |
| R-2144 | Review is one layer of defence in depth, alongside automated tooling. | quality assurance | quality | S-16 ch09 / Code Correctness | C-34 |
| R-2145 | Authors seek reviewers with a different perspective. | software engineers | security | S-16 ch09 / Comprehension of Code | C-02 |
| R-2146 | Reviewers treat comprehension questions as valid and answer by explaining more clearly. | quality assurance | security | S-16 ch09 / Comprehension of Code | C-02 |
| R-2147 | Readability approvers must have per-language readability training. | software engineers | quality | S-16 ch09 / Code Consistency | C-39 |
| R-2148 | Keep feedback polite and professional. | software engineers | security | S-16 ch09 / Code Review Best Practices | C-02 |
| R-2149 | Ask why before assuming an approach is wrong. | quality assurance | security | S-16 ch09 / Code Review Best Practices | C-02 |
| R-2150 | Accept equally valid author preferences. | quality assurance | security | S-16 ch09 / Code Review Best Practices | C-02 |
| R-2151 | Treat review comments as TODO items. | software engineers | security | S-16 ch09 / Code Review Best Practices | C-02 |
| R-2152 | Use PTAL for follow-up review requests. | software engineers | security | S-16 ch09 / Code Review Best Practices | C-02 |
| R-2153 | Give initial feedback within 24 working hours. | quality assurance | security | S-16 ch09 / Code Review Best Practices | C-02 |
| R-2154 | If feedback is delayed, acknowledge receipt. | quality assurance | security | S-16 ch09 / Code Review Best Practices | C-02 |
| R-2155 | Avoid piecemeal feedback. | quality assurance | security | S-16 ch09 / Code Review Best Practices | C-02 |
| R-2156 | Write a change summary as the first line of the description. | software engineers | quality | S-16 ch09 / Code Review Best Practices | C-37 |
| R-2157 | Describe what changed and why in the change description. | software engineers | quality | S-16 ch09 / Code Review Best Practices | C-37 |
| R-2158 | Update the change description when decisions change. | software engineers | quality | S-16 ch09 / Code Review Best Practices | C-37 |
| R-2159 | Use presubmits, static analysis and auto-submit for simple changes. | software engineers | quality | S-16 ch09 / Code Review Best Practices | C-32 |
| R-2160 | Greenfield changes require a separate design review. | software engineers | quality | S-16 ch09 / Types of Code Reviews | C-38 |
| R-2161 | Greenfield changes must match the agreed API design. | software engineers | quality | S-16 ch09 / Types of Code Reviews | C-38 |
| R-2162 | Greenfield changes require full unit testing. | software engineers | quality | S-16 ch09 / Types of Code Reviews | C-31 |
| R-2163 | Greenfield changes require proper OWNERS entries. | software engineers | quality | S-16 ch09 / Types of Code Reviews | C-40 |
| R-2164 | Greenfield changes require adequate comments and documentation. | software engineers | quality | S-16 ch09 / Types of Code Reviews | C-37 |
| R-2165 | Greenfield changes require CI integration. | software engineers | quality | S-16 ch09 / Types of Code Reviews | C-30 |
| R-2166 | Behavioural changes update tests for the new behaviour. | software engineers | quality | S-16 ch09 / Types of Code Reviews | C-31 |
| R-2167 | Behavioural changes and optimizations run through CI. | software engineers | quality | S-16 ch09 / Types of Code Reviews | C-30 |
| R-2168 | Optimizations provide benchmarks. | software engineers | quality | S-16 ch09 / Types of Code Reviews | C-31 |
| R-2169 | Bug fixes fix only the stated bug. | software engineers | quality | S-16 ch09 / Types of Code Reviews | C-36 |
| R-2170 | Bug fixes update tests so that the tests catch the bug. | software engineers | quality | S-16 ch09 / Types of Code Reviews | C-31 |
| R-2171 | Bug fixes and rollbacks keep changes small and atomic. | software engineers | quality | S-16 ch09 / Types of Code Reviews | C-36 |
| R-2172 | Rollbacks still need review. | software engineers | security | S-16 ch09 / Types of Code Reviews | C-02 |
| R-2173 | Reviewers of large automated changes limit comments to concerns specific to their code. | quality assurance | security | S-16 ch09 / Types of Code Reviews | C-02 |
| R-2174 | Reviewers of large automated changes escalate tool concerns to the LSC oversight group out of band. | quality assurance | security | S-16 ch09 / Types of Code Reviews | C-02 |
| R-2175 | Large automated changes do not expand scope. | software engineers | quality | S-16 ch09 / Types of Code Reviews | C-36 |
| R-2176 | Code review is mandatory for almost every change, with rare exceptions for documentation and configuration. | software engineers | security | S-16 ch09 / Conditions and scope notes | C-02 |
| R-2177 | Each simple test has one behaviour under test, a specific input, an observable output and a controlled environment. | software engineers | quality | S-16 ch11 / Why Do We Write Tests? | C-31 |
| R-2178 | The test suite must stay healthy. | software engineers | quality | S-16 ch11 / Why Do We Write Tests? | C-31 |
| R-2179 | Systems must be testable so that they can change quickly. | software engineers | quality | S-16 ch11 / Testing Overview | C-31 |
| R-2180 | Tests are required for all new code changes. | software engineers | quality | S-16 ch11 / The Story of Google Web Server | C-31 |
| R-2181 | Automation is required, because manual validation does not scale. | software engineers | quality | S-16 ch11 / Testing at the Speed of Modern Development | C-31 |
| R-2182 | Write tests, run them frequently and react to failures. | software engineers | quality | S-16 ch11 / Write, Run, React | C-30 |
| R-2183 | Fix broken tests within minutes of failure. | software engineers | quality | S-16 ch11 / Write, Run, React | C-30 |
| R-2184 | Express tests as code so they run across environments and locales. | software engineers | quality | S-16 ch11 / Write, Run, React | C-31 |
| R-2185 | All code is reviewed by at least one other engineer before submission. | software engineers | security | S-16 ch11 / Benefits of Testing Code | C-02 |
| R-2186 | Small tests run in a single process, with no sleeping, I/O or blocking calls. | software engineers | quality | S-16 ch11 / Test Size | C-31 |
| R-2187 | Small tests make no network or disk access. | software engineers | quality | S-16 ch11 / Test Size | C-31 |
| R-2188 | Small tests use test doubles for heavy dependencies. | software engineers | quality | S-16 ch11 / Test Size | C-31 |
| R-2189 | Medium tests make network calls only to localhost. | software engineers | quality | S-16 ch11 / Test Size | C-31 |
| R-2190 | Large tests are reserved for end-to-end and legacy-component tests. | software engineers | quality | S-16 ch11 / Test Size | C-31 |
| R-2191 | Filesystem access in tests uses only a hermetic in-memory implementation. | software engineers | quality | S-16 ch11 / Test Size | C-31 |
| R-2192 | Tests should be hermetic and make minimal assumptions. | software engineers | quality | S-16 ch11 / Properties Common to All Test Sizes | C-31 |
| R-2193 | Tests should be obvious upon inspection. | software engineers | quality | S-16 ch11 / Properties Common to All Test Sizes | C-31 |
| R-2194 | Avoid conditionals and loops in tests. | software engineers | quality | S-16 ch11 / Properties Common to All Test Sizes | C-31 |
| R-2195 | Test everything you do not want to break. | software engineers | quality | S-16 ch11 / The Beyoncé Rule | C-31 |
| R-2196 | Infrastructure teams must fix the product breakage their changes cause and must add tests. | software engineers | quality | S-16 ch11 / The Beyoncé Rule | C-31 |
| R-2197 | Simulate failures such as exceptions, RPC errors and latency instead of waiting for real outages. | software engineers | security | S-16 ch11 / Testing for Failure | C-17 |
| R-2198 | Measure coverage only from small tests. | software engineers | quality | S-16 ch11 / A Note on Code Coverage | C-31 |
| R-2199 | Poll for state changes at a high frequency with timeouts instead of sleep. | software engineers | quality | S-16 ch11 / The Pitfalls of a Large Test Suite | C-31 |
| R-2200 | Treat tests like production code and invest in linters and documentation. | software engineers | quality | S-16 ch11 / The Pitfalls of a Large Test Suite | C-32 |
| R-2201 | Each supported language has one standard test framework and one standard mocking library. | software engineers | quality | S-16 ch11 / The Pitfalls of a Large Test Suite | C-31 |
| R-2202 | Every change includes feature code and tests. | software engineers | quality | S-16 ch11 / Testing Culture Today | C-31 |
| R-2203 | A security flaw found by a human can be added to an automated security testing system. | security team | security | S-16 ch11 / The Limits of Automated Testing | C-11 |
| R-2204 | Integrate upstream microservices, data, ML models, runtimes and devices as dependencies, continuously. | software engineers | quality | S-16 ch23 / Introduction | C-30 |
| R-2205 | Presubmit builds should not talk to real production backends. | operations engineers | operations | S-16 ch23 / Introduction | C-22 |
| R-2206 | Presubmit runs only fast, reliable tests limited to the affected project. | software engineers | quality | S-16 ch23 / Continuous Testing | C-30 |
| R-2207 | Engineers must sync to the true head before they submit, even when they sync to a green head. | software engineers | quality | S-16 ch23 / Automation | C-30 |
| R-2208 | Static configuration should be promoted as part of the release candidate, and it is in version control along with the code. | operations engineers | operations | S-16 ch23 / Automation | C-45 |
| R-2209 | Continuous delivery continuously assembles release candidates and promotes them through environments. | operations engineers | operations | S-16 ch23 / Automation | C-46 |
| R-2210 | Do not rebuild artifacts between environments. | operations engineers | operations | S-16 ch23 / Automation | C-46 |
| R-2211 | Use containers and orchestration to run the artifacts. | operations engineers | operations | S-16 ch23 / Automation | C-20 |
| R-2212 | Use experiments or feature flags for selective continuous deployment. | operations engineers | operations | S-16 ch23 / Automation | C-21 |
| R-2213 | Run a comprehensive suite against each release candidate. | quality assurance | quality | S-16 ch23 / Continuous Testing | C-31 |
| R-2214 | Run the same suite as probers in production. | operations engineers | operations | S-16 ch23 / Continuous Testing | C-23 |
| R-2215 | Combine multiple testing approaches as defence in depth. | quality assurance | quality | S-16 ch23 / Continuous Testing | C-31 |
| R-2216 | Use hermetic backends for larger tests, especially at presubmit. | software engineers | quality | S-16 ch23 / Hermetic Testing | C-31 |
| R-2217 | Test results must not depend on who runs the test. | software engineers | quality | S-16 ch23 / Hermetic Testing | C-31 |
| R-2218 | Canary: deploy to a small production subset first and watch for version skew. | operations engineers | operations | S-16 ch23 / CI Concepts | C-21 |
| R-2219 | Isolate risky changes with experiments and feature flags. | operations engineers | operations | S-16 ch23 / CI Concepts | C-21 |
| R-2220 | Logs exclude user personal data. | operations engineers | operations | S-16 ch23 / CI Concepts | C-23 |
| R-2221 | Feedback output is made readable and actionable. | software engineers | quality | S-16 ch23 / CI Concepts | C-30 |
| R-2222 | Tests should fail only when a meaningful invariant is violated. | software engineers | quality | S-16 ch23 / CI Is Alerting | C-30 |
| R-2223 | Do not require 100 percent green CI. | software engineers | quality | S-16 ch23 / CI Is Alerting | C-30 |
| R-2224 | Do not block commits when the root cause is understood and does not affect production. | software engineers | quality | S-16 ch23 / CI Is Alerting | C-30 |
| R-2225 | Accept changes that disable failing tests until CI can tag known-irrelevant failures. | software engineers | quality | S-16 ch23 / CI Is Alerting | C-30 |
| R-2226 | Aim for uptime of about 99.9 or 99.999 percent rather than 100 percent. | operations engineers | operations | S-16 ch23 / CI Is Alerting, footnote | C-24 |
| R-2227 | Temporarily remove flaky tests from presubmit and allow retries. | software engineers | quality | S-16 ch23 / CI Challenges | C-30 |
| R-2228 | Track disabled tests so that they do not pile up. | software engineers | quality | S-16 ch23 / CI Challenges | C-30 |
| R-2229 | Fix non-release-blocking bugs too. | software engineers | quality | S-16 ch23 / CI Challenges | C-35 |
| R-2230 | Use bug hotlists filed by on-call or release engineers, ideally auto-filed. | operations engineers | quality | S-16 ch23 / CI Challenges | C-35 |
| R-2231 | Each team has a Build Cop who must fix breakages promptly. | software engineers | quality | S-16 ch23 / CI at Google: TAP | C-30 |
| R-2232 | Rollback is preferred for a breakage. | operations engineers | operations | S-16 ch23 / CI at Google: TAP | C-21 |
| R-2233 | A CI system must evolve, because it is never complete. | software engineers | quality | S-16 ch23 / Conclusion | C-35 |
| R-2234 | Release early and often. | software engineers | quality | S-16 ch24 / Introduction | C-36 |
| R-2235 | Shorten the time between code completion and user feedback. | software engineers | operations | S-16 ch24 / Introduction | C-28 |
| R-2236 | Treat each launch as the start of a learning cycle. | software engineers | quality | S-16 ch24 / Introduction | C-35 |
| R-2237 | Release frequently in small batches. | software engineers | quality | S-16 ch24 / Idioms of Continuous Delivery at Google | C-36 |
| R-2238 | Automate repetitive release work. | operations engineers | operations | S-16 ch24 / Idioms of Continuous Delivery at Google | C-20 |
| R-2239 | Modularize the architecture. | software engineers | quality | S-16 ch24 / Idioms of Continuous Delivery at Google | C-38 |
| R-2240 | Measure health indicators such as crashes and latency. | operations engineers | operations | S-16 ch24 / Idioms of Continuous Delivery at Google | C-23 |
| R-2241 | Use A/B tests on health metrics. | operations engineers | operations | S-16 ch24 / Idioms of Continuous Delivery at Google | C-23 |
| R-2242 | Use phased rollouts. | operations engineers | operations | S-16 ch24 / Idioms of Continuous Delivery at Google | C-21 |
| R-2243 | Teams should be ready to deploy at any time, without necessarily deploying. | operations engineers | operations | S-16 ch24 / Idioms of Continuous Delivery at Google | C-21 |
| R-2244 | Avoid long-lived subteam branches. | software engineers | quality | S-16 ch24 / Velocity Is a Team Sport | C-36 |
| R-2245 | Develop at head in the shared codebase, with CI, automatic rollbacks and culprit finding. | software engineers | quality | S-16 ch24 / Velocity Is a Team Sport | C-36 |
| R-2246 | Invest in architecture change, microservice migration or rewrite where needed, rather than only slow the release cadence. | software engineers | quality | S-16 ch24 / Velocity Is a Team Sport | C-38 |
| R-2247 | Flag-guard all changes, with separate flag settings for development and release builds. | operations engineers | operations | S-16 ch24 / Flag-Guarding Features | C-21 |
| R-2248 | Strip disabled features from builds where the language allows. | operations engineers | operations | S-16 ch24 / Flag-Guarding Features | C-21 |
| R-2249 | Stage changes to flag settings with a rollout, using a configuration service. | operations engineers | operations | S-16 ch24 / Flag-Guarding Features | C-21 |
| R-2250 | Do not turn a flag on for 100 percent of users at once. | operations engineers | operations | S-16 ch24 / Flag-Guarding Features | C-21 |
| R-2251 | Use KPI metrics with clear thresholds to make launch decisions. | management | operations | S-16 ch24 / Striving for Agility | C-29 |
| R-2252 | Accept imperfection and weigh trade-offs in launch decisions. | management | quality | S-16 ch24 / Striving for Agility | C-42 |
| R-2253 | Enforce release cutoffs. | operations engineers | operations | S-16 ch24 / Meet Your Release Deadline | C-29 |
| R-2254 | Missed features should catch the next release train within hours. | operations engineers | operations | S-16 ch24 / Meet Your Release Deadline | C-21 |
| R-2255 | Ship only the code that users need, for example with dynamic deployments. | operations engineers | operations | S-16 ch24 / Quality and User-Focus | C-46 |
| R-2256 | Dedicated teams do ongoing efficiency work. | management | quality | S-16 ch24 / Quality and User-Focus | C-42 |
| R-2257 | Separate how often a release is created from how often users receive it, and choose the cadence on purpose. | operations engineers | operations | S-16 ch24 / Quality and User-Focus | C-21 |
| R-2258 | Use A/B experiments to weigh a feature cost against its user and business value. | management | quality | S-16 ch24 / Quality and User-Focus | C-42 |
| R-2259 | Use representative testing if comprehensive testing is infeasible. | software engineers | quality | S-16 ch24 / Shifting Left | C-31 |
| R-2260 | Use staged rollouts to growing percentages of users, and specialized testing tracks. | operations engineers | operations | S-16 ch24 / Shifting Left | C-21 |
| R-2261 | A/B test deployments, with the old version re-shipped as the baseline. | operations engineers | operations | S-16 ch24 / Shifting Left | C-21 |
| R-2262 | Automated pipelines advance rollouts when guardrail metrics are unaffected. | operations engineers | operations | S-16 ch24 / Shifting Left | C-21 |
| R-2263 | Use change-neutral releases with all new features flag-guarded for small user bases. | operations engineers | operations | S-16 ch24 / Shifting Left | C-21 |
| R-2264 | Always Be Deploying: keep releases frequent and close to a known good state. | software engineers | operations | S-16 ch24 / Changing Team Culture | C-28 |
| R-2265 | Release responsibility protects users and the product from developer urgency. | operations engineers | quality | S-16 ch24 / Changing Team Culture | C-40 |
| R-2266 | Release responsibility requires strong interface contracts, separation of concerns, rigorous testing, early and frequent communication, and feature acceptance conventions. | management | quality | S-16 ch24 / Changing Team Culture | C-40 |
| R-2267 | Make binaries configurable in production. | operations engineers | operations | S-16 ch24 / Conclusion | C-20 |
| R-2268 | Keep configuration as code in version control. | operations engineers | operations | S-16 ch24 / Conclusion | C-20 |
| R-2269 | Verify changes with a dry run. | operations engineers | operations | S-16 ch24 / Conclusion | C-26 |
| R-2270 | Provide rollback and rollforward mechanisms. | operations engineers | operations | S-16 ch24 / Conclusion | C-21 |
| R-2271 | Provide reliable patching. | software engineers | security | S-16 ch24 / Conclusion | C-15 |
| R-2272 | A developer or producer of software, including AI system providers, should be treated as a manufacturer. | management | quality | S-18 page 4, recital 13 | C-41 |
| R-2273 | Developing or contributing to free and open-source software should not be understood as making it available on the market. | software engineers | quality | S-18 page 4, recital 14 | C-41 |
| R-2274 | Providing free and open-source software on open repositories should not be considered as making it available on the market, unless it occurs in a commercial activity. | software engineers | quality | S-18 page 4, recital 14 | C-41 |
| R-2275 | Supply of free and open-source software by non-profit organisations should not be considered as taking place in a business-related context, unless it occurs in a commercial activity. | management | quality | S-18 page 4, recital 14 | C-41 |
| R-2276 | This Directive should apply where software is supplied for a price or for personal data used beyond security, compatibility or interoperability. | regulators and auditors | quality | S-18 page 4, recital 14 | C-41 |
| R-2277 | Where a manufacturer integrates free and open-source software that was supplied outside a commercial activity into a product, it should be possible to hold that manufacturer liable for damage caused by the defectiveness of the software, but not the manufacturer of the software. | management | quality | S-18 page 4, recital 15 | C-41 |
| R-2278 | Member States should not maintain or introduce provisions more or less stringent than this Directive, in matters within its scope. | regulators and auditors | quality | S-18 page 4, recital 8 | C-41 |
| R-2279 | Provisions of national law that serve effective protection should remain unaffected by this Directive. | regulators and auditors | quality | S-18 page 4, recital 9 | C-41 |
| R-2280 | The right to make claims for pharmaceutical damage under a special system should remain unaffected. | regulators and auditors | quality | S-18 page 4, recital 10 | C-41 |
| R-2281 | Amendments to special liability systems should not be precluded, as long as they do not undermine the effectiveness of this Directive. | regulators and auditors | quality | S-18 page 4, recital 10 | C-41 |
| R-2282 | Compensation schemes outside liability regimes should not be precluded. | regulators and auditors | quality | S-18 page 4, recital 11 | C-41 |
| R-2283 | Certain provisions of this Directive, in particular the definitions, should be aligned with Decision No 768/2008/EC. | regulators and auditors | quality | S-18 page 4, recital 12 | C-41 |
| R-2284 | Digital manufacturing files should be considered to be products where developed or supplied in a commercial activity. | regulators and auditors | quality | S-18 page 4, recital 16 | C-41 |
| R-2285 | Related digital services should be considered components of the product where they are within the control of the manufacturer. | management | quality | S-18 page 4, recital 17 | C-41 |
| R-2286 | Related services and software updates should be considered within the manufacturer's control where integrated, supplied, or authorised by the manufacturer. | management | quality | S-18 page 5, recital 18 | C-41 |
| R-2287 | A manufacturer should not be considered to have consented to integration merely by providing the technical possibility. | management | quality | S-18 page 5, recital 18 | C-41 |
| R-2288 | A product should be considered to remain within the manufacturer's control while the manufacturer retains the ability to supply updates or upgrades. | management | quality | S-18 page 5, recital 19 | C-41 |
| R-2289 | Destruction or corruption of data should also be compensated for. | users and customers | quality | S-18 page 5, recital 20 | C-41 |
| R-2290 | Damage to property used exclusively for professional purposes should not be compensated under this Directive. | users and customers | quality | S-18 page 5, recital 22 | C-41 |
| R-2291 | Destruction or corruption of data used for professional purposes should not be compensated under this Directive. | users and customers | quality | S-18 page 5, recital 22 | C-41 |
| R-2292 | Member States should provide full and proper compensation for material losses. | regulators and auditors | quality | S-18 page 5, recital 23 | C-41 |
| R-2293 | The rules on calculating compensation should be laid down by Member States. | regulators and auditors | quality | S-18 page 5, recital 23 | C-41 |
| R-2294 | Compensation for non-material losses should be provided in so far as national law allows. | users and customers | quality | S-18 page 5, recital 23 | C-41 |
| R-2295 | Other types of damage should not by themselves trigger liability under this Directive. | regulators and auditors | quality | S-18 page 5, recital 24 | C-41 |
| R-2296 | Damage to property owned by a natural person should be compensated. | users and customers | quality | S-18 page 5, recital 25 | C-41 |
| R-2297 | Property used exclusively for professional purposes should be excluded from the scope. | regulators and auditors | quality | S-18 page 5, recital 25 | C-41 |
| R-2298 | This Directive should apply to products placed on the market in the course of a commercial activity. | regulators and auditors | quality | S-18 page 5, recital 26 | C-41 |
| R-2299 | The right to compensation should apply to direct and indirect victims in so far as national law so provides. | users and customers | quality | S-18 page 5, recital 27 | C-41 |
| R-2300 | Member States should ensure that competent consumer protection authorities provide all relevant information to affected consumers. | regulators and auditors | quality | S-18 page 5, recital 28 | C-41 |
| R-2301 | The defectiveness of a product should be determined by reference to the lack of the safety that a person is entitled to expect. | users and customers | quality | S-18 page 5, recital 30 | C-41 |
| R-2302 | The assessment of defectiveness should involve an objective analysis of the safety the public at large is entitled to expect. | regulators and auditors | quality | S-18 page 5, recital 30 | C-41 |
| R-2303 | The assessment should take into account the intended purpose, foreseeable use, presentation, characteristics, expected lifespan and user group. | regulators and auditors | quality | S-18 page 5, recital 30 | C-41 |
| R-2304 | A court should be able to find a product defective where it belongs to the same production series as a product proven defective. | regulators and auditors | quality | S-18 page 5, recital 30 | C-41 |
| R-2305 | The assessment of defectiveness should take into account the presentation of the product. | regulators and auditors | quality | S-18 page 5, recital 31 | C-41 |
| R-2306 | The assessment should take into account the reasonably foreseeable effects of other products. | regulators and auditors | quality | S-18 page 5, recital 32 | C-41 |
| R-2307 | The effect of any ability to learn or acquire new features should be taken into account. | regulators and auditors | quality | S-18 page 5, recital 32 | C-41 |
| R-2308 | A manufacturer that designs a product with the ability to develop unexpected behaviour should remain liable for behaviour that causes harm. | management | quality | S-18 page 5, recital 32 | C-41 |
| R-2309 | The moment a product leaves the manufacturer's control should be taken into account. | regulators and auditors | quality | S-18 page 5, recital 32 | C-41 |
| R-2310 | The assessment of a product whose purpose is to prevent damage should take into account its failure to fulfil that purpose. | regulators and auditors | quality | S-18 page 5, recital 33 | C-41 |
| R-2311 | Relevant product safety requirements, including safety-relevant cybersecurity requirements, should be taken into account in the assessment of defectiveness. | regulators and auditors | quality | S-18 page 5, recital 34 | C-41 |
| R-2312 | Interventions by authorities or by economic operators should not in themselves create a presumption of defectiveness. | regulators and auditors | quality | S-18 page 5, recital 34 | C-41 |
| R-2313 | The existence of a better product should not in itself lead to the conclusion that a product is defective. | regulators and auditors | quality | S-18 page 5, recital 35 | C-41 |
| R-2314 | The supply of updates or upgrades should not in itself lead to the conclusion that a previous version is defective. | regulators and auditors | quality | S-18 page 5, recital 35 | C-41 |
| R-2315 | Where a manufacturer integrates a defective component, an injured person should be able to seek compensation from both manufacturers. | users and customers | quality | S-18 page 5, recital 36 | C-41 |
| R-2316 | Where a component is integrated outside the control of the product manufacturer, an injured person should be able to seek compensation from the component manufacturer. | users and customers | quality | S-18 page 5, recital 36 | C-41 |
| R-2317 | Fulfilment service providers should be liable only where no importer or authorised representative is established in the Union. | suppliers | quality | S-18 page 5, recital 37 | C-41 |
| R-2318 | Distributors should be liable only where they fail to promptly identify a relevant economic operator established in the Union. | suppliers | quality | S-18 page 5, recital 37 | C-41 |
| R-2319 | Online platforms should be subject to the same liability as the economic operator role they perform. | suppliers | quality | S-18 page 5, recital 38 | C-41 |
| R-2320 | Online platforms should be liable only where they present the product in a way that leads an average consumer to believe it is provided by the platform or a trader under its control. | suppliers | quality | S-18 page 5, recital 38 | C-41 |
| R-2321 | Online platforms should be liable only where they fail to promptly identify a relevant economic operator established in the Union. | suppliers | quality | S-18 page 5, recital 38 | C-41 |
| R-2322 | Provisions relating to distributors should apply analogously to such online platforms. | suppliers | quality | S-18 page 5, recital 38 | C-41 |
| R-2323 | A person that makes a substantial modification outside the original manufacturer's control should be liable as a manufacturer of the modified product. | management | quality | S-18 page 5, recital 39 | C-41 |
| R-2324 | Criteria for substantial modification should be determined on the basis of relevant Union and national product safety law. | regulators and auditors | quality | S-18 page 5, recital 39 | C-41 |
| R-2325 | Where no criteria exist, modifications that change intended functions or risk profile should be considered substantial. | regulators and auditors | quality | S-18 page 5, recital 39 | C-41 |
| R-2326 | The original manufacturer should not be able to avoid liability by arguing that the defectiveness arose after placing on the market. | management | quality | S-18 page 5, recital 39 | C-41 |
| R-2327 | An economic operator other than the original manufacturer should be exempted if it proves the damage relates to an unaffected part. | management | quality | S-18 page 5, recital 39 | C-41 |
| R-2328 | Economic operators that carry out repairs without substantial modification should not be subject to liability. | suppliers | quality | S-18 page 5, recital 39 | C-41 |
| R-2329 | The same principles should apply to modifications made by software update or upgrade as to other modifications. | regulators and auditors | quality | S-18 page 5, recital 40 | C-41 |
| R-2330 | A substantially modified product should be considered made available at the time that modification is actually made. | regulators and auditors | quality | S-18 page 5, recital 40 | C-41 |
| R-2331 | The claimant should bear the burden of proving the damage, the defectiveness and the causal link. | users and customers | quality | S-18 page 5, recital 42 | C-41 |
| R-2332 | National courts should ensure that access to evidence is limited to what is necessary and proportionate. | regulators and auditors | quality | S-18 page 5, recital 42 | C-41 |
| R-2333 | It should be possible for national courts to require evidence to be presented in an easily accessible and understandable manner. | regulators and auditors | quality | S-18 page 5, recital 42 | C-41 |
| R-2334 | Defendants should also have the possibility of accessing evidence. | regulators and auditors | quality | S-18 page 5, recital 44 | C-41 |
| R-2335 | National courts should ensure that defendant access to evidence is limited to what is necessary and proportionate. | regulators and auditors | quality | S-18 page 5, recital 44 | C-41 |
| R-2336 | National courts should be empowered to take specific measures to ensure the confidentiality of trade secrets. | regulators and auditors | quality | S-18 page 5, recital 45 | C-41 |
| R-2337 | Measures for trade secrets should include at least measures to restrict access to documents and hearings. | regulators and auditors | quality | S-18 page 5, recital 45 | C-41 |
| R-2338 | National courts should presume the defectiveness of a product where a defendant fails to comply with a disclosure obligation. | regulators and auditors | quality | S-18 page 5, recital 46 | C-41 |
| R-2339 | Non-compliance with mandatory safety requirements should also result in a presumption of defectiveness, including failure to equip a product with required logging means. | regulators and auditors | quality | S-18 page 5, recital 46 | C-41 |
| R-2340 | The same presumption should apply in the case of obvious malfunction. | regulators and auditors | quality | S-18 page 5, recital 46 | C-41 |
| R-2341 | The claimant should not be required to prove the causal link where the damage is typically caused by the defect. | users and customers | quality | S-18 page 5, recital 47 | C-41 |
| R-2342 | The existence of the causal link should be presumed where a defect is established and the damage is typically caused by it. | regulators and auditors | quality | S-18 page 5, recital 47 | C-41 |
| R-2343 | National courts should presume defectiveness or causal link where proof is excessively difficult despite disclosure. | regulators and auditors | quality | S-18 page 6, recital 48 | C-41 |
| R-2344 | The claimant should be required to demonstrate only that it is likely that the product was defective, or that the defect is a likely cause. | users and customers | quality | S-18 page 6, recital 48 | C-41 |
| R-2345 | Technical or scientific complexity should be determined by national courts on a case-by-case basis. | regulators and auditors | quality | S-18 page 6, recital 48 | C-41 |
| R-2346 | The assessment of excessive difficulties should be made by national courts on a case-by-case basis. | regulators and auditors | quality | S-18 page 6, recital 48 | C-41 |
| R-2347 | The claimant should provide arguments to demonstrate excessive difficulties. | users and customers | quality | S-18 page 6, recital 48 | C-41 |
| R-2348 | The claimant should not be required to explain the specific characteristics of an AI system to prove excessive difficulties. | users and customers | quality | S-18 page 6, recital 48 | C-41 |
| R-2349 | The defendant should have the possibility of contesting all elements of the claim. | management | quality | S-18 page 6, recital 48 | C-41 |
| R-2350 | Economic operators should be exempted from liability if they prove specific exonerating circumstances. | management | quality | S-18 page 6, recital 49 | C-41 |
| R-2351 | Manufacturers should be exempted where they prove it is probable the defect did not exist when placed on the market. | management | quality | S-18 page 6, recital 50 | C-41 |
| R-2352 | Manufacturers should remain liable for defectiveness arising after placing on the market from software or related services within their control. | management | quality | S-18 page 6, recital 50 | C-41 |
| R-2353 | Software or related services should be considered within the manufacturer's control where supplied by the manufacturer or authorised by it. | regulators and auditors | quality | S-18 page 6, recital 50 | C-41 |
| R-2354 | A manufacturer should remain liable, alongside a third-party application maker, for damage caused by a defective third-party application. | management | quality | S-18 page 6, recital 50 | C-41 |
| R-2355 | The possibility for economic operators to avoid liability should be restricted where the defect is a lack of security updates. | management | quality | S-18 page 6, recital 51 | C-41 |
| R-2356 | Manufacturers should not be exempted from liability where the defect results from failure to supply necessary security updates. | management | security | S-18 page 6, recital 51 | C-15 |
| R-2357 | Such liability should not apply where the supply or installation of the update is beyond the manufacturer's control. | management | quality | S-18 page 6, recital 51 | C-41 |
| R-2358 | Economic operators should be exempted from liability if they prove the state of knowledge could not reveal the defect. | management | quality | S-18 page 6, recital 52 | C-41 |
| R-2359 | All parties liable for the same damage should be held liable jointly and severally. | users and customers | quality | S-18 page 6, recital 53 | C-41 |
| R-2360 | Microenterprises and small enterprises that manufacture software should be able to agree contractually that the manufacturer will not seek recourse. | suppliers | quality | S-18 page 6, recital 54 | C-41 |
| R-2361 | Liability towards an injured person should never be limited or excluded by such a contractual agreement. | users and customers | quality | S-18 page 6, recital 54 | C-41 |
| R-2362 | The liability of an economic operator should not be reduced or disallowed by acts of a third party. | management | quality | S-18 page 6, recital 55 | C-41 |
| R-2363 | It should be possible to reduce or disallow liability where the injured person negligently contributed to the damage. | regulators and auditors | quality | S-18 page 6, recital 55 | C-41 |
| R-2364 | No contractual derogations from liability should be permitted. | regulators and auditors | quality | S-18 page 6, recital 56 | C-41 |
| R-2365 | Provisions of national law should not limit or exclude liability, including by financial ceilings. | regulators and auditors | quality | S-18 page 6, recital 56 | C-41 |
| R-2366 | Liability should be subject to a reasonable length of time, namely 10 years from placing on the market or putting into service. | regulators and auditors | quality | S-18 page 6, recital 57 | C-41 |
| R-2367 | The expiry period should be extended to 25 years where personal injury symptoms are slow to emerge. | regulators and auditors | quality | S-18 page 6, recital 57 | C-41 |
| R-2368 | A new expiry period should start after a substantial modification and subsequent making available. | regulators and auditors | quality | S-18 page 6, recital 58 | C-41 |
| R-2369 | Updates that do not amount to a substantial modification should not affect the expiry period of the original product. | regulators and auditors | quality | S-18 page 6, recital 58 | C-41 |
| R-2370 | A Member State should be able to derogate from the development risk defence by new or amended measures. | regulators and auditors | quality | S-18 page 6, recital 59 | C-41 |
| R-2371 | Use of a development risk derogation should be notified to the Commission. | regulators and auditors | quality | S-18 page 6, recital 59 | C-41 |
| R-2372 | The Commission should be able to issue non-binding opinions on proposed measures. | regulators and auditors | quality | S-18 page 6, recital 59 | C-41 |
| R-2373 | A Member State proposing such measures should hold them in abeyance for six months after notification, unless an opinion is issued earlier. | regulators and auditors | quality | S-18 page 6, recital 59 | C-41 |
| R-2374 | An opinion should be issued after close cooperation between the Member State and the Commission. | regulators and auditors | quality | S-18 page 6, recital 59 | C-41 |
| R-2375 | It should also be possible for a Member State to maintain existing derogations from the development risk defence. | regulators and auditors | quality | S-18 page 6, recital 59 | C-41 |
| R-2376 | Member States should be required to publish final court judgments on product liability under this Directive. | regulators and auditors | quality | S-18 page 6, recital 60 | C-41 |
| R-2377 | Member States should be required only to publish judgments of national courts of appeal or of the highest instance. | regulators and auditors | quality | S-18 page 6, recital 60 | C-41 |
| R-2378 | The Commission should set up and maintain a publicly available database of relevant judgments. | regulators and auditors | quality | S-18 page 6, recital 61 | C-41 |
| R-2379 | The Commission should carry out an evaluation of this Directive. | regulators and auditors | quality | S-18 page 6, recital 62 | C-41 |
| R-2380 | The evaluation should be based on five criteria: efficiency, effectiveness, relevance, coherence and value added. | regulators and auditors | quality | S-18 page 6, recital 62 | C-41 |
| R-2381 | The Commission should provide the methodology for the calculations used in its evaluation report. | regulators and auditors | quality | S-18 page 6, recital 62 | C-41 |
| R-2382 | The Commission should gather all relevant information in a way that avoids overregulation and an administrative burden. | regulators and auditors | quality | S-18 page 6, recital 62 | C-41 |
| R-2383 | This Directive shall apply to products placed on the market or put into service after 9 December 2026. | regulators and auditors | quality | S-18 page 6, Article 2(1) | C-41 |
| R-2384 | Member States shall not maintain or introduce provisions diverging from this Directive, including more or less stringent provisions. | regulators and auditors | quality | S-18 page 6, Article 3 | C-41 |
| R-2385 | Member States shall ensure that any natural person who suffers damage caused by a defective product is entitled to compensation under this Directive. | users and customers | quality | S-18 Article 5(1), page 8 | C-41 |
| R-2386 | Member States shall ensure that claims for compensation may also be brought by a person subrogated to the right of the injured person, or by a person acting on behalf of one or more injured persons. | users and customers | quality | S-18 Article 5(2), page 8 | C-41 |
| R-2387 | The right to compensation shall apply only to death or personal injury, to certain damage to property, and to destruction or corruption of data not used for professional purposes. | users and customers | quality | S-18 Article 6(1), page 8 | C-41 |
| R-2388 | The right to compensation shall cover all material losses from the damage, and non-material losses in so far as national law allows compensation. | users and customers | quality | S-18 Article 6(2), page 8 | C-41 |
| R-2389 | A product shall be considered defective where it does not provide the safety that a person is entitled to expect or that is required under Union or national law. | users and customers | quality | S-18 Article 7(1), page 8 | C-41 |
| R-2390 | In assessing defectiveness, all circumstances shall be taken into account, including the points listed in Article 7(2)(a) to (i). | regulators and auditors | quality | S-18 Article 7(2), page 8 | C-41 |
| R-2391 | A product shall not be considered defective for the sole reason that a better product, including updates or upgrades, has been or is later placed on the market. | management | quality | S-18 Article 7(3), page 8 | C-41 |
| R-2392 | Member States shall ensure that the manufacturer of a defective product is liable for damage under this Directive. | users and customers | quality | S-18 Article 8(1)(a), page 8 | C-41 |
| R-2393 | Member States shall ensure that the manufacturer of a defective component is liable where the component was integrated into or inter-connected with a product within the control of the manufacturer and caused the product to be defective. | users and customers | quality | S-18 Article 8(1)(b), page 8 | C-41 |
| R-2394 | Member States shall ensure that, for a manufacturer established outside the Union, the importer, the authorised representative, or where neither is established in the Union, the fulfilment service provider are liable. | users and customers | quality | S-18 Article 8(1)(c), pages 8 to 9 | C-41 |
| R-2395 | The liability of the manufacturer under Article 8(1)(a) shall also cover damage caused by a defective component integrated into or inter-connected with a product within the control of that manufacturer. | users and customers | quality | S-18 Article 8(1), second subparagraph, page 9 | C-41 |
| R-2396 | A natural or legal person that substantially modifies a product outside the control of the manufacturer, and then makes it available or puts it into service, shall be considered a manufacturer for Article 8(1). | users and customers | quality | S-18 Article 8(2), page 9 | C-41 |
| R-2397 | Member States shall ensure that where no economic operator established in the Union can be identified, each distributor is liable where the injured person requests identification and the distributor does not identify an operator or its own distributor within one month. | users and customers | quality | S-18 Article 8(3), page 9 | C-41 |
| R-2398 | Article 8(3) shall also apply to a provider of an online platform that allows consumers to conclude distance contracts with traders and that is not an economic operator, provided the conditions of Article 6(3) of Regulation (EU) 2022/2065 are met. | users and customers | quality | S-18 Article 8(4), page 9 | C-41 |
| R-2399 | Member States may use existing national sectoral compensation schemes, or establish new ones preferably not funded by public revenue, where victims cannot obtain compensation. | users and customers | quality | S-18 Article 8(5), page 9 | C-41 |
| R-2400 | Member States shall ensure that, at the request of a claimant who has presented facts and evidence sufficient to support the plausibility of the claim, the defendant is required to disclose relevant evidence at the disposal of the defendant. | users and customers | quality | S-18 Article 9(1), page 9 | C-41 |
| R-2401 | Member States shall ensure that, at the request of a defendant who has presented facts and evidence of a need for evidence, the claimant is required to disclose relevant evidence at the disposal of the claimant. | management | quality | S-18 Article 9(2), page 9 | C-41 |
| R-2402 | Member States shall ensure that disclosure of evidence is limited to what is necessary and proportionate. | regulators and auditors | quality | S-18 Article 9(3), page 9 | C-41 |
| R-2403 | Member States shall ensure that national courts consider the legitimate interests of all parties, including third parties, when deciding whether disclosure is necessary and proportionate. | regulators and auditors | quality | S-18 Article 9(4), page 9 | C-41 |
| R-2404 | Member States shall ensure that national courts are empowered to take specific measures to preserve the confidentiality of trade secrets when a defendant must disclose them. | regulators and auditors | quality | S-18 Article 9(5), page 9 | C-41 |
| R-2405 | Member States shall ensure that national courts are empowered to require evidence to be presented in an easily accessible and easily understandable manner, if proportionate in terms of costs and effort. | regulators and auditors | quality | S-18 Article 9(6), page 9 | C-41 |
| R-2406 | Member States shall ensure that a claimant is required to prove the defectiveness of the product, the damage suffered and the causal link between them. | users and customers | quality | S-18 Article 10(1), page 9 | C-41 |
| R-2407 | The defectiveness of the product shall be presumed where the defendant fails to disclose evidence under Article 9(1), or the claimant shows non-compliance with mandatory product safety requirements, or the claimant shows an obvious malfunction during reasonably foreseeable use. | users and customers | quality | S-18 Article 10(2), page 9 | C-41 |
| R-2408 | The causal link shall be presumed where the product is established as defective and the damage is of a kind typically consistent with the defect. | users and customers | quality | S-18 Article 10(3), page 9 | C-41 |
| R-2409 | A national court shall presume defectiveness, or the causal link, or both, where the claimant faces excessive difficulties and shows that the product is likely defective or that a causal link is likely. | users and customers | quality | S-18 Article 10(4), page 9 | C-41 |
| R-2410 | The defendant shall have the right to rebut any of the presumptions in Article 10(2), (3) and (4). | management | quality | S-18 Article 10(5), page 9 | C-41 |
| R-2411 | An economic operator shall not be liable if it proves that it did not place the product on the market or put it into service, or, for a distributor, that it did not make the product available. | management | quality | S-18 Article 11(1)(a) and (b), page 9 | C-41 |
| R-2412 | An economic operator shall not be liable if it proves that it is probable the defectiveness did not exist when the product was placed on the market, put into service or made available, or that it came into being later. | management | quality | S-18 Article 11(1)(c), page 9 | C-41 |
| R-2413 | An economic operator shall not be liable if it proves that the defectiveness is due to compliance of the product with legal requirements. | management | quality | S-18 Article 11(1)(d), page 9 | C-41 |
| R-2414 | An economic operator shall not be liable if it proves that the objective state of scientific and technical knowledge did not allow the defectiveness to be discovered at the relevant time. | management | quality | S-18 Article 11(1)(e), page 9 | C-41 |
| R-2415 | A manufacturer of a defective component shall not be liable if it proves that the defectiveness of the product is due to the design of that product or to instructions given by the product manufacturer. | suppliers | quality | S-18 Article 11(1)(f), page 9 | C-41 |
| R-2416 | A person that modifies a product shall not be liable if it proves that the defectiveness is related to a part of the product not affected by the modification. | management | quality | S-18 Article 11(1)(g), page 9 | C-41 |
| R-2417 | An economic operator shall not be exempted under Article 11(1)(c) where, within the control of the manufacturer, the defectiveness is due to a related service, software including updates or upgrades, a lack of software updates or upgrades necessary to maintain safety, or a substantial modification. | management | quality | S-18 Article 11(2), pages 9 to 10 | C-41 |
| R-2418 | Member States shall ensure that where two or more economic operators are liable for the same damage, they can be held liable jointly and severally. | users and customers | quality | S-18 Article 12(1), page 10 | C-41 |
| R-2419 | A manufacturer that integrates software as a component shall not have a right of recourse against a manufacturer of a defective software component that was a microenterprise or small enterprise when placed on the market, where the integrating manufacturer contractually agreed to waive that right. | suppliers | quality | S-18 Article 12(2), page 10 | C-41 |
| R-2420 | Member States shall ensure that the liability of an economic operator is not reduced or disallowed where the damage is caused both by the defectiveness and by an act or omission of a third party. | users and customers | quality | S-18 Article 13(1), page 10 | C-41 |
| R-2421 | The liability of an economic operator may be reduced or disallowed where the damage is caused both by the defectiveness and by the fault of the injured person or of a person for whom the injured person is responsible. | management | quality | S-18 Article 13(2), page 10 | C-41 |
| R-2422 | An economic operator that has compensated the injured person shall be entitled to pursue remedies against other liable economic operators under national law. | management | quality | S-18 Article 14, page 10 | C-41 |
| R-2423 | Member States shall ensure that the liability of an economic operator is not limited or excluded, in relation to the injured person, by a contractual provision or by national law. | users and customers | quality | S-18 Article 15, page 10 | C-41 |
| R-2424 | Member States shall ensure that a limitation period of three years applies to initiating proceedings, running from when the injured person became aware or should reasonably have become aware of the damage, the defectiveness and the identity of the liable economic operator. | users and customers | quality | S-18 Article 16(1), page 10 | C-41 |
| R-2425 | Member States shall ensure that an injured person is no longer entitled to compensation after 10 years from placing on the market or putting into service, unless proceedings were initiated in that time. | users and customers | quality | S-18 Article 17(1), page 10 | C-41 |
| R-2426 | For latent personal injury that could not be claimed within 10 years, the injured person shall no longer be entitled to compensation after 25 years, unless proceedings were initiated in that time. | users and customers | quality | S-18 Article 17(2), page 10 | C-41 |
| R-2427 | Any Member State wishing to maintain measures under Article 18(1) shall notify the text of the measures to the Commission no later than 9 December 2026. | regulators and auditors | quality | S-18 Article 18(1), page 10 | C-41 |
| R-2428 | The Commission shall inform the other Member States of notified measures. | regulators and auditors | quality | S-18 Article 18(1) and (4), page 10 | C-41 |
| R-2429 | Member States may introduce or amend measures under which economic operators are liable even if they prove the state of knowledge did not allow the defectiveness to be discovered. | regulators and auditors | quality | S-18 Article 18(2), page 10 | C-41 |
| R-2430 | Measures under Article 18(2) shall be limited to specific categories of products, justified by public interest objectives, and proportionate. | regulators and auditors | quality | S-18 Article 18(3), page 10 | C-41 |
| R-2431 | A Member State wishing to introduce or amend a measure under Article 18(2) shall notify the proposed text and a justification of its compliance with Article 18(3) to the Commission. | regulators and auditors | quality | S-18 Article 18(4), page 10 | C-41 |
| R-2432 | The Commission may, within six months of notification, issue an opinion on the proposed measure and its justification. | regulators and auditors | quality | S-18 Article 18(5), page 10 | C-41 |
| R-2433 | The Member State shall hold the proposed measure in abeyance for six months after notification, unless the Commission issues its opinion earlier. | regulators and auditors | quality | S-18 Article 18(5), page 10 | C-41 |
| R-2434 | Member States shall publish, in an easily accessible electronic format, any final judgment delivered by their national courts of appeal or highest instance in proceedings under this Directive. | regulators and auditors | quality | S-18 Article 19(1), page 10 | C-41 |
| R-2435 | Apply least privilege to repository secrets. | software engineers | security | S-19 Secure use reference, Secrets | C-08 |
| R-2436 | Set GITHUB_TOKEN to read-only repository contents by default, then raise permissions per job. | software engineers | security | S-19 Secure use reference, Secrets | C-06 |
| R-2437 | Never store sensitive data as plaintext in workflow files. | software engineers | security | S-19 Secure use reference, Secrets | C-07 |
| R-2438 | Mask non-secret values with the add-mask command. | software engineers | security | S-19 Secure use reference, Secrets | C-07 |
| R-2439 | If an unredacted secret reaches a log, delete the log and rotate the secret. | software engineers | security | S-19 Secure use reference, Secrets | C-07 |
| R-2440 | Do not use JSON, XML or YAML blobs as secrets. Create one secret per value. | software engineers | security | S-19 Secure use reference, Secrets | C-07 |
| R-2441 | Register derived values, such as signed JWTs, Base64 or URL-encoded strings, as secrets too. | software engineers | security | S-19 Secure use reference, Secrets | C-07 |
| R-2442 | Audit how secrets are used, including by third-party actions. | software engineers | security | S-19 Secure use reference, Secrets | C-07 |
| R-2443 | Review logs after valid and invalid inputs. | software engineers | security | S-19 Secure use reference, Secrets | C-07 |
| R-2444 | Periodically remove unneeded secrets and rotate the rest. | software engineers | security | S-19 Secure use reference, Secrets | C-07 |
| R-2445 | Consider required reviewers for environment secrets. | software engineers | security | S-19 Secure use reference, Secrets | C-08 |
| R-2446 | Prefer a JavaScript action that receives context values as arguments. | software engineers | security | S-19 Secure use reference, Script injection | C-06 |
| R-2447 | For inline scripts, pass untrusted values through intermediate environment variables and quote shell variables. | software engineers | security | S-19 Secure use reference, Script injection | C-06 |
| R-2448 | Use code scanning workflow templates, CodeQL or third-party. | security team | security | S-19 Secure use reference, Script injection | C-11 |
| R-2449 | Restrict token permissions. | software engineers | security | S-19 Secure use reference, Script injection | C-06 |
| R-2450 | Avoid pull_request_target unless required. Prefer workflow_run for privilege separation. | software engineers | security | S-19 Secure use reference, Untrusted code checkout | C-06 |
| R-2451 | Do not explicitly check out untrusted code in pull_request_target or workflow_run workflows. | software engineers | security | S-19 Secure use reference, Untrusted code checkout | C-06 |
| R-2452 | Treat artifacts from other workflows with caution. | software engineers | security | S-19 Secure use reference, Untrusted code checkout | C-06 |
| R-2453 | Lock workflow dependencies with a lockfile, which the page says supersedes SHA pinning where adopted. | software engineers | security | S-19 Secure use reference, Third-party actions and workflows | C-10 |
| R-2454 | If a lockfile is not possible, pin to a full-length commit SHA from the action's own repository, not a fork. | software engineers | security | S-19 Secure use reference, Third-party actions and workflows | C-10 |
| R-2455 | Pin to a tag only if you trust the creator, because tags can be moved or deleted. | software engineers | security | S-19 Secure use reference, Third-party actions and workflows | C-10 |
| R-2456 | Always audit action source code for secret handling. | software engineers | security | S-19 Secure use reference, Third-party actions and workflows | C-10 |
| R-2457 | Use CODEOWNERS on .github/workflows to require approval for workflow changes. | software engineers | security | S-19 Secure use reference, GitHub features and tooling | C-02 |
| R-2458 | Use OpenID Connect to avoid long-lived cloud credentials. | software engineers | security | S-19 Secure use reference, GitHub features and tooling | C-07 |
| R-2459 | Use Dependabot version and security updates. | software engineers | security | S-19 Secure use reference, GitHub features and tooling | C-10 |
| R-2460 | Restrict whether Actions can create or approve pull requests. | software engineers | security | S-19 Secure use reference, GitHub features and tooling | C-02 |
| R-2461 | Enable code scanning and OpenSSF Scorecards to detect risky workflow patterns. | security team | security | S-19 Secure use reference, GitHub features and tooling | C-11 |
| R-2462 | Review dependencies with the dependency graph and dependency review. | software engineers | security | S-19 Secure use reference, GitHub features and tooling | C-10 |
| R-2463 | Use the published SBOMs to review pre-installed software on GitHub-hosted runners. | operations engineers | security | S-19 Secure use reference, GitHub-hosted runners | C-18 |
| R-2464 | Self-hosted runners should almost never be used for public repositories. | operations engineers | security | S-19 Secure use reference, Self-hosted runners | C-18 |
| R-2465 | Use caution with self-hosted runners in private or internal repositories, since anyone who can open a pull request may compromise the runner. | operations engineers | security | S-19 Secure use reference, Self-hosted runners | C-18 |
| R-2466 | Keep sensitive data on self-hosted runner machines to a minimum and restrict access to cloud metadata services. | operations engineers | security | S-19 Secure use reference, Self-hosted runners | C-18 |
| R-2467 | Organize self-hosted runners into groups and restrict which repositories can use them. | operations engineers | security | S-19 Secure use reference, Self-hosted runners | C-18 |
| R-2468 | Use just-in-time runners, which run at most one job, and ensure a clean environment for each. | operations engineers | security | S-19 Secure use reference, Self-hosted runners | C-05 |
| R-2469 | Avoid passing secrets as command-line arguments, since other jobs can view them. | operations engineers | security | S-19 Secure use reference, Self-hosted runners | C-07 |
| R-2470 | Choose a management level (enterprise, organization or repository) based on whether management is centralized or decentralized. | operations engineers | security | S-19 Secure use reference, Self-hosted runners | C-18 |
| R-2471 | Prefer OIDC or short-lived tokens for cloud authentication. | operations engineers | security | S-19 Secure use reference, Self-hosted runners | C-07 |
| R-2472 | Monitor the security log, the audit log and Dependabot alerts. | security team | security | S-19 Secure use reference, Auditing and vulnerability management | C-18 |
| R-2473 | Use repository security advisories and private vulnerability reporting when maintaining published actions. | software engineers | security | S-19 Secure use reference, Auditing and vulnerability management | C-14 |
| R-2474 | Use the dependents view to see which projects depend on your action. | software engineers | security | S-19 Secure use reference, Auditing and vulnerability management | 5 |
| R-2475 | Reusable workflows are YAML files in .github/workflows. Subdirectories are not supported. | software engineers | security | S-19 Reuse workflows, Creating a reusable workflow | 5 |
| R-2476 | The on key must include workflow_call. | software engineers | security | S-19 Reuse workflows, Creating a reusable workflow | 5 |
| R-2477 | Inputs can be marked required and typed as boolean, number or string. The caller's value type must match. | software engineers | security | S-19 Reuse workflows, Inputs and secrets | 5 |
| R-2478 | Set environment on the job in the reusable workflow for environment secrets. The caller must still pass the secret, by name or with inherit. | software engineers | security | S-19 Reuse workflows, Inputs and secrets | 5 |
| R-2479 | Pin reusable workflow references to a commit SHA for stability and security. | software engineers | security | S-19 Reuse workflows, Calling workflows | C-10 |
| R-2480 | Limit cache access with cache-mode so called workflows get only what they need. | software engineers | security | S-19 Reuse workflows, Cache access control | C-05 |
| R-2481 | Limit permissions in callers. | software engineers | security | S-19 Reuse workflows, Security guidance | C-06 |
| R-2482 | Use inherit only within the same organization or enterprise, and prefer passing named secrets. | software engineers | security | S-19 Reuse workflows, Passing inputs and secrets | C-07 |
| R-2483 | Use environment secrets and required: true to prevent silent empty-secret runs. | software engineers | security | S-19 Reuse workflows, Inputs and secrets | 5 |
| R-2484 | Use the audit log API to monitor usage in Enterprise Cloud organizations. | operations engineers | security | S-19 Reuse workflows, Monitoring usage | C-18 |
| R-2485 | Report data problems to the authoritative source first, using its process, and use the Source or Import Source fields to find it. | users and customers | security | S-20 FAQ page, reader instructions | C-14 |
| R-2486 | If the source does not resolve a data problem, file a GitHub issue with the data quality label. | users and customers | security | S-20 FAQ page, reader instructions | C-14 |
| R-2487 | Use HTTP/2 for queries that may return large responses. | users and customers | security | S-20 FAQ page, reader instructions | 5 |
| R-2488 | Track the modified_id.csv entries to identify new or changed records since the last download. | users and customers | security | S-20 FAQ page, reader instructions | 5 |
| R-2489 | Create a GitHub issue for questions. | users and customers | quality | S-20 FAQ page, reader instructions | C-37 |
| R-2490 | Corrections belong at the original source, not in OSV. | suppliers | security | S-20 FAQ page, data handling section | C-14 |
| R-2491 | Transparency data (SBOMs, attestations, provenance) should be produced by the build in CI/CD rather than assembled afterward. | software engineers | security | S-21 not given by extract | C-04 |
| R-2492 | Organizations should make transparency operate within CI/CD so they can move faster with less friction. | management | security | S-21 not given by extract | C-04 |
| R-2493 | Registries should be operated as critical infrastructure, with security controls that match modern development. | suppliers | security | S-21 not given by extract | C-16 |
| R-2494 | AI-assisted dependency changes need guardrails and verified sources of truth. | software engineers | security | S-21 not given by extract | C-10 |
| R-2495 | Guardrails for AI are no longer optional. | management | security | S-21 not given by extract | C-10 |
| R-2496 | AI should not guess. | software engineers | security | S-21 not given by extract | C-10 |
| R-2497 | Security programs must separate urgent issues from noise. | security team | security | S-21 not given by extract | C-11 |
| R-2498 | Teams need to prioritise risk. | management | quality | S-21 not given by extract | C-42 |
| R-2499 | Readers who find or suspect a security problem should file a detailed report. | users and customers | security | S-25 security.html, Reporting statement | C-14 |

## Proposed boundaries

| Boundary | Requirements that it would take | Stakeholders that it would leave with no requirement | Reason |
|---|---|---|---|
| requirements engineering | R-0001, R-0005 to R-0006, R-0008, R-0010 to R-0015, R-0018 to R-0020, R-0026, R-0028, R-0195 to R-0196, R-0200, R-0221, R-0312, R-0318, R-0320, R-0343 to R-0344, R-0439, R-0533, R-0775 to R-0776, R-0794, R-0962, R-2137 | none | The classification of the requirement lines gave 31 requirements to this neighbour: a neighbouring aspect owns the elicitation, the analysis and the management of the functional requirements. (S-01 pages 43-66) |
| architecture and design | R-0029 to R-0043, R-0045, R-0052, R-0054 to R-0056, R-0113, R-0118, R-0310 to R-0311, R-0313, R-0378 to R-0379, R-0383, R-0440 to R-0442, R-0445, R-0519 to R-0521, R-0534 to R-0539, R-0792, R-0795 to R-0796, R-0798, R-0824, R-0899 to R-0900, R-0960, R-0963, R-0968, R-1566, R-1583 to R-1584, R-1704, R-1982 to R-1983, R-1988 to R-1990, R-1992 to R-1994, R-2050, R-2054, R-2125, R-2138 to R-2139, R-2160 to R-2161, R-2239, R-2246 | none | The classification of the requirement lines gave 72 requirements to this neighbour: a neighbouring aspect owns the structure of the software and its design methods. (S-01 pages 67-98) |
| project management | R-0021 to R-0025, R-0027, R-0091, R-0094, R-0139, R-0186 to R-0194, R-0197 to R-0199, R-0201 to R-0205, R-0208, R-0212 to R-0220, R-0224 to R-0232, R-0238, R-0241 to R-0242, R-0245, R-0247 to R-0248, R-0250 to R-0253, R-0255 to R-0257, R-0260 to R-0261, R-0297, R-0299, R-0316, R-0408 to R-0409, R-0429 to R-0430, R-0435, R-0446, R-0565, R-0619, R-0973, R-1923, R-1945, R-2064, R-2252, R-2256, R-2498 | none | The classification of the requirement lines gave 78 requirements to this neighbour: a neighbouring aspect owns the planning, the estimation and the control of a project. (S-01 pages 202-220) |
| engineering economics | R-0101, R-0146 to R-0150, R-0294, R-0325, R-0346, R-0405, R-0412 to R-0428, R-0431 to R-0434, R-0436, R-0556 to R-0558, R-0772, R-2258 | none | The classification of the requirement lines gave 37 requirements to this neighbour: a neighbouring aspect owns the decisions on cost and benefit. (S-01 pages 288-311) |
| software maintenance | R-0007, R-0134 to R-0138, R-0140 to R-0145, R-0151 to R-0159, R-0163 to R-0164, R-0185, R-0364, R-0540, R-1535, R-1595 to R-1596, R-1720, R-2005 | none | The classification of the requirement lines gave 31 requirements to this neighbour: a neighbouring aspect owns the maintenance process and the end of life. (S-01 pages 167-184) |
| professional practice | R-0003 to R-0004, R-0093, R-0319, R-0322 to R-0324, R-0326 to R-0327, R-0390 to R-0398, R-0404, R-0406 to R-0407, R-0410 to R-0411, R-0437, R-0548, R-0573 to R-0575, R-0578 to R-0580, R-0585 to R-0618, R-0620 to R-0621, R-0942, R-0955, R-1799 to R-1800, R-1976, R-2134, R-2142, R-2146, R-2148 to R-2150 | none | The classification of the requirement lines gave 78 requirements to this neighbour: a neighbouring aspect owns the ethics, the contracts and the conduct of the profession. (S-01 pages 274-287) |
| foundations | R-0002, R-0350 to R-0351, R-0389, R-0438, R-0443 to R-0444, R-0447 to R-0457, R-0459 to R-0473, R-0480 to R-0508, R-0511 to R-0518, R-0525 to R-0527, R-0544 to R-0547, R-0549 to R-0555, R-0559 to R-0564, R-0566 to R-0572, R-0576 to R-0577 | none | The classification of the requirement lines gave 99 requirements to this neighbour: a neighbouring aspect owns the computing, mathematical and engineering foundations. (S-01 pages 312-386) |
| legal conformity | R-1035 to R-1049, R-1053, R-1062, R-1066 to R-1069, R-1071 to R-1072, R-1078 to R-1081, R-1083 to R-1102, R-1104 to R-1160, R-1165 to R-1208, R-1236, R-1240, R-1245 to R-1246, R-1249 to R-1250, R-1252, R-1285, R-1306, R-1313, R-1323, R-1329, R-1385 to R-1386, R-1388, R-1390, R-1441, R-1534, R-1559 to R-1562, R-1580, R-1611 to R-1659, R-1664 to R-1671, R-1690, R-1695, R-1764 to R-1766, R-1788, R-1805 to R-1814, R-1826 to R-1833, R-1841 to R-1850, R-1853 to R-1855, R-1857 to R-1868, R-1870 to R-1872, R-1887, R-1892 to R-1893, R-1898 to R-1899, R-2272 to R-2434 | regulators and auditors | The classification of the requirement lines gave 448 requirements to this neighbour: a neighbouring aspect owns the duties of authorities, courts, importers and distributors, the procedures of conformity assessment and the liability rules. (S-06 pages 14-16; S-12 pages 7-9; S-18 pages 7-10) |
| product security functions | R-0458, R-0509, R-0523, R-0528 to R-0531, R-1213 to R-1218, R-1221 to R-1222, R-1239, R-1242 to R-1243, R-1290, R-1297 to R-1298, R-1301 to R-1303, R-1307 to R-1308, R-1332, R-1725 to R-1729, R-1735, R-1746, R-1991, R-2058 | none | The classification of the requirement lines gave 36 requirements to this neighbour: a neighbouring aspect owns the security functions inside the product, such as encryption, access control and the handling of payment data. (S-06 page 24; S-07 pages 243-256) |
| platform and tool providers | R-0625, R-0627, R-0630 to R-0633, R-0640 to R-0645, R-0647 to R-0667, R-0673, R-0676, R-0678 to R-0680, R-0686 to R-0691, R-0693 to R-0703, R-0705 to R-0710, R-0716, R-0718 to R-0726, R-0728 to R-0730, R-0735, R-0743, R-0753 to R-0754, R-0890, R-0894 to R-0898, R-0916, R-0919, R-0927, R-2493 | none | The classification of the requirement lines gave 88 requirements to this neighbour: a neighbouring aspect owns the duties of the provider of a build platform, of a source control system, of a verifier or of a package ecosystem. (S-02 pages 2-4, 7-10) |
| enterprise risk and resilience | R-0366, R-0765, R-0840, R-0842, R-0844 to R-0846, R-1251, R-1610, R-1660 to R-1663, R-1672 to R-1689, R-1691 to R-1694, R-1696 to R-1703, R-1706, R-1708 to R-1719, R-1721, R-1723 to R-1724, R-1730 to R-1734, R-1738 to R-1739, R-1742, R-1745, R-1747 to R-1749, R-1754 to R-1763, R-1767 to R-1786, R-1790 to R-1795, R-1798, R-1815 to R-1822, R-1824 to R-1825, R-1856, R-1869, R-1886, R-1888, R-1894 | none | The classification of the requirement lines gave 123 requirements to this neighbour: a neighbouring aspect owns the risk, continuity and third-party management of the whole organization. (S-12 pages 10-15) |

## Binding sources

One row for each source of the class `regulation` or `governance`. The two cells come from the report of a file reader that got the question "Whom does the source bind?".

| Source | Binds | Where |
|---|---|---|
| S-06 | The economic operators for products with digital elements that are made available on the market of the Union: manufacturers, importers, distributors, authorised representatives and open-source software stewards. The products are those with a direct or indirect logical or physical data connection. The products that Article 2(2) to (8) names are excluded. The source names no sector. | page 8, Article 1; page 9, Article 2(1) to (8) and Article 3(12) to (17) |
| S-07 | Each entity that stores, processes or transmits cardholder data or sensitive authentication data, or that could affect the security of these data: merchants, processors, acquirers, issuers and other service providers in the processing of payment accounts. The organizations that manage the compliance programs, such as the payment brands and the acquirers, decide if an entity must comply or validate. | page 8 |
| S-12 | The financial entities of the types of Article 2(1)(a) to (t), and the ICT third-party service providers of Article 2(1)(u). The groups that Article 2(3) names are excluded. Many duties do not apply to microenterprises. The source names no product. | page 8, Article 1(1) and Article 2(1)(a) to (p); page 9, Article 2(1)(q) to (u), Article 2(2) and Article 2(3); page 11, Article 3(60) |
| S-18 | The Member States: the directive is addressed to them. They must make sure that these economic operators are liable for the damage of a defective product: the manufacturers of a product or of a component, the providers of related services, authorised representatives, importers, fulfilment service providers and distributors. Developers and producers of software are treated as manufacturers. A product includes software. Free and open-source software that is developed or supplied outside a commercial activity is excluded. The source names no sector. | page 11, Article 24; pages 8-9, Article 8(1); page 7, Article 4(1) and Article 4(15); page 6, Article 2(1) and Article 2(2); page 4, recital 13 |

## Reading

The program `index.py unread --write` writes this table. Do not change it by hand.

| Source | Document | Pages | Given to readers | Not read |
|---|---|---|---|---|
| S-01 | swebok | 411 | 1-25, 26-42, 43-66, 67-82, 83-98, 99-116, 117-141, 142-166, 167-184, 185-201, 202-220, 221-245, 246-263, 264-287, 288-311, 312-335, 336-344, 345-366, 367-386, 387-411 | none |
| S-02 | S-02 | 10 | 1-5, 6-10 | none |
| S-03 | S-03 | 36 | 1-25, 26-36 | none |
| S-04 | S-04 | 41 | 1-23, 24-41 | none |
| S-06 | S-06 | 31 | 9-11, 12-14, 15-16, 23-25 | 1-8, 17-22, 26-31 |
| S-07 | S-07 | 397 | 9-14, 136-150, 151-165, 243-256, 270-286, 331-337 | 1-8, 15-135, 166-242, 257-269, 287-330, 338-397 |
| S-12 | S-12 | 33 | 7-9, 10-12, 13-15, 16-18 | 1-6, 19-33 |
| S-18 | S-18 | 14 | 4-6, 7-10 | 1-3, 11-14 |
