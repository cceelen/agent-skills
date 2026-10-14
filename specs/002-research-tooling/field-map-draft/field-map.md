# Field map: software engineering

This file tells what the factory knows about the field before it researches one aspect.

- Source: the seed `swebok` of `factory/sota-research/references/seeds.md`. The row of the seed
  gives the document, the issuer, the version and the terms.
- Read on: 2026-10-10, by 20 file readers. Each reader read one range of pages of the converted
  file. `evidence.md` gives the range and the point of the report that supports each row.
- The text is in the words of this kit. It is not the text of the guide.
- A page number is the number of the heading `## Page N` of the converted file. It is not the
  page number that the guide prints.
- "KA" is "knowledge area".

## Knowledge areas

The guide has 18 knowledge areas (page 40, page 402). The first 15 are areas of software
engineering. The last three are foundation areas (page 40).

| Row | Knowledge area | What it covers | Pages |
|---|---|---|---|
| KA-01 | Software Requirements | What a requirement is and its categories. How to elicit, analyse, specify and validate requirements. The management of requirements and the tools. | 43-66 |
| KA-02 | Software Architecture | The stakeholders and their concerns. The description of an architecture with views and viewpoints. The process of architecture and the evaluation of an architecture. | 67-82 |
| KA-03 | Software Design | The principles, the processes and the qualities of design. How to record a design. The strategies and methods of design, and the analysis of the quality of a design. | 83-98 |
| KA-04 | Software Construction | How software is made and kept in detail: coding, verification, unit tests, integration tests and debugging. The management, the technologies and the tools of construction. | 99-116 |
| KA-05 | Software Testing | The fundamentals, the levels and the techniques of tests. The measures and the process of tests. Tests in development processes and in application domains. The tools. | 117-150 |
| KA-06 | Software Engineering Operations | The activities that deploy, operate and support a software system and keep its integrity and stability. Planning, delivery and control of operations. | 151-166 |
| KA-07 | Software Maintenance | Why maintenance is necessary and its categories. The technical and the management issues, the costs, the processes, the techniques and the tools. | 167-184 |
| KA-08 | Software Configuration Management | The management of the process, identification, change control, status accounting, audits, the management of releases and delivery, and the tools. | 185-201 |
| KA-09 | Software Engineering Management | Planning, estimation, measurement, control, coordination, leadership and risk management for software projects. | 202-220 |
| KA-10 | Software Engineering Process | Definitions of process, life cycle models, categories of processes, the management and the adaptation of a life cycle, and the assessment and improvement of processes. | 221-232 |
| KA-11 | Software Engineering Models and Methods | Modelling, the types of models, the analysis of models, and methods: heuristic, formal, prototyping and agile. | 233-245 |
| KA-12 | Software Quality | The fundamentals of quality, the process of quality management, the process of quality assurance, and the tools. | 246-263 |
| KA-13 | Software Security | The fundamentals, the management and organization of security, security engineering and its processes, the tools, and security for specific domains. | 264-273 |
| KA-14 | Software Engineering Professional Practice | Professionalism, group dynamics and psychology, and communication skills. | 274-287 |
| KA-15 | Software Engineering Economics | Economic decisions in the full life cycle of a software product: the fundamentals, a decision process of six steps, estimation and related concepts. | 288-311 |
| KA-16 | Computing Foundations | Computer architecture, data structures and algorithms, programming, operating systems, databases, networks, human factors, and artificial intelligence. | 312-344 |
| KA-17 | Mathematical Foundations | Logic, proof techniques, sets, graphs, state machines, grammars, number theory, counting, probability, numerical precision, algebraic structures and calculus. | 345-366 |
| KA-18 | Engineering Foundations | The engineering process, engineering design, abstraction, empirical methods, statistics, modelling, measurement, standards and root cause analysis. | 367-386 |
| KA-19 | Appendices (not a knowledge area) | Appendix A: how the description of a knowledge area is written. Appendix B: the relation of IEEE and ISO/IEC standards to the guide. Appendix C: the consolidated list of the recommended references for the knowledge areas. | 387-411 |

## Stakeholders

A stakeholder is a person, a group or an organization that takes part in the project, gets an
effect from it or can influence it (page 48). The interests of a stakeholder are named
concerns (page 69). An interest can be stated or implied (pages 233-234).

| Row | Stakeholder | What it wants or is responsible for | Knowledge areas that name it | Pages |
|---|---|---|---|---|
| SH-01 | Client | Pays for the software. Usually imposes requirements. Examines in the validation that its needs are in the requirements. Frequently does not know what is necessary or possible. Gets progress reports. Wants to see value at the end of each iteration. | Requirements, Maintenance, Management, Quality, Economics, Professional Practice | 45, 48, 58, 171, 203, 214, 248, 278, 289 |
| SH-02 | Customer | Decides if the product goes into service. Wants to know when the system is ready and what it costs to build and to operate. Gives requirements, needs and concerns to the design. Can get early feedback from incremental integration. In agile work, sees frequent demonstrations of software that works. Agrees to the specifications in a predictive life cycle. Is a member of the team in XP. Is the last judge of quality in one view. Can ask for summaries, and needs training and documentation. | Introduction, Requirements, Architecture, Design, Construction, Testing, Maintenance, Configuration Management, Management, Process, Models and Methods, Quality, Professional Practice, Economics, Appendix B | 26, 38, 48, 69, 85, 107, 140, 175, 178, 185, 212-213, 225, 242, 246, 249, 282, 284-285, 292, 397 |
| SH-03 | User; end user | Uses the software directly or indirectly, and can be divided into classes of users. Wants to know what the system does and how to use it. Does acceptance tests or takes part in them. Asks for changes and reports problems. Needs the software to continue to satisfy its requirements. Gets training, assistance and documentation. Expects robust software and an interface that is easy to understand. | Requirements, Architecture, Design, Construction, Testing, Operations, Maintenance, Configuration Management, Management, Process, Models and Methods, Quality, Professional Practice, Computing Foundations, Engineering Foundations | 48-49, 58, 69, 94, 96, 102, 123, 124, 131, 146, 154, 156, 168, 169, 179, 185, 214, 226, 227, 233-234, 246, 248, 281, 335, 381 |
| SH-04 | Software engineer; engineer | Is the expert for the technology. Writes code and does the unit tests and integration tests of that code. Designs tests. Uses the operations services. Elicits the quality requirements. Defines the security properties of the software. Gives estimates that are realistic. Works ethically, keeps skills current and documents the work. Must know the applicable standards. | Requirements, Construction, Testing, Operations, Configuration Management, Management, Quality, Security, Professional Practice, Economics, Computing Foundations, Mathematical Foundations, Engineering Foundations | 47, 99, 105, 122, 129, 153, 160, 193, 204, 248, 256, 264, 265, 274, 277, 281, 285, 301, 313, 345, 367-368, 382 |
| SH-05 | Developer; programmer; implementer | Builds the software from the design. Wants to know if an algorithm satisfies the requirements. Manages dependencies. Should know good practices and common vulnerabilities. Does threat modelling for the security design. The developers that made the software are a source of knowledge for the maintainers. Takes the actions for satisfactory operation in the support stage. | Requirements, Architecture, Design, Construction, Testing, Operations, Maintenance, Process, Models and Methods, Quality, Security, Computing Foundations | 49, 69, 70, 85, 87, 103, 107, 108, 135, 152, 169, 174, 227, 229, 233-234, 251, 267, 268, 313 |
| SH-06 | Designer | Makes the design and communicates it. Is in the primary audience of an architecture description. | Architecture, Design | 69, 70, 90 |
| SH-07 | Architect | Makes the decisions that give the architecture its shape. | Architecture, Models and Methods | 73, 233-234 |
| SH-61 | System architect (of a computer system) | Analyses the application and selects the critical components and the architecture. | Computing Foundations | 314 |
| SH-08 | Tester; test team; independent test group | Finds faults in independent tests. The members of a test team can be internal or external. Works together with the developers in shift-left development. | Construction, Testing, Quality, Computing Foundations | 102, 135, 138, 144, 258, 325 |
| SH-09 | Operator; operations staff; operations engineer | Develops and gives the operations services: deployment, monitoring, capacity and security. Installs the software and verifies the installation. Shares the work to operate and to change the software with the maintainer. Sends modification requests and problem reports. | Requirements, Design, Operations, Maintenance, Configuration Management | 49, 96, 152, 153, 155, 172, 177, 195 |
| SH-10 | Maintainer; maintenance team | Does the maintenance. Must understand the software and its artifacts and change them. Gets a benefit from the recorded rationale of the design. Needs the documented assumptions of the program when these cannot be validated. Frequently is not the developer of the code. | Design, Maintenance, Security, Computing Foundations | 93, 96, 168-169, 178, 179, 267, 335 |
| SH-11 | Product support staff; support personnel; help desk | Gives support to the end users. Can install, operate and administer the software, as users also can, and needs documentation for this. | Requirements, Maintenance, Professional Practice | 49, 178, 281 |
| SH-12 | Subject matter expert; business domain expert | Is the expert for the policies and processes of the domain. Agrees on acceptance tests with the software engineers before construction. Can be one of the stakeholders that are identified for decisions with large consequences. | Requirements, Testing, Economics | 47, 49, 54, 55, 141, 292 |
| SH-13 | Regulator; regulatory agency; regulatory body | Can impose requirements and constraints, for example when the software can have an effect on public safety. Usually is the cause of compliance tests. | Requirements, Testing, Configuration Management, Professional Practice | 45, 49, 124, 187, 282 |
| SH-14 | Certifier; certifying authority; certification body | Gives the certification of conformity. Uses the body of knowledge to judge the knowledge of a person. | Architecture, Design, Testing, Models and Methods, Appendix B | 70, 96, 122, 233-234, 393 |
| SH-15 | Professional body; professional society | Defines, advances and regulates the profession, and publishes codes. Frequently gives the certification examinations. | Requirements, Professional Practice, Introduction | 40, 49, 276, 277 |
| SH-16 | Special interest group | The text lists it as a stakeholder and gives no interest. | Requirements | 49 |
| SH-17 | Persons who get a negative effect from the success of the project | The text lists them as stakeholders and gives no interest. | Requirements | 49 |
| SH-18 | Manager; project manager; program manager; software engineering manager | Wants the satisfaction of the stakeholders. Leads change and motivates the teams. Can use measurements to manage construction. Uses the measures of the test process to control the tests. Must handle software security as an issue of the enterprise. Should give documentation to other parts of the organization, together with the software engineers. Can use the status reports of configuration management. | Architecture, Construction, Testing, Configuration Management, Management, Security, Professional Practice, Appendix A | 79, 103, 135, 136, 195, 203, 204, 210, 214, 265, 281-284, 390 |
| SH-19 | Senior management; top management; executive management; organizational leadership | Defines and enforces the security policy. Does the business planning of the maintenance organization. Supports the quality management system and gives resources. Needs a clear view of the business model and of the intangible assets. | Operations, Maintenance, Process, Quality, Economics | 159, 178-179, 228, 251, 252, 300 |
| SH-20 | Organization | Wants to get to its business goals or strategic goals, with software as a lever. Can impose requirements. Many organizations must deliver and deploy software more frequently and more reliably. Does root cause analysis to take corrective action. | Requirements, Construction, Operations, Configuration Management, Economics, Engineering Foundations, Appendix A | 45, 101, 157, 187, 288, 382-383, 390 |
| SH-21 | Acquirer; buyer | Can agree with the supplier on provisions for configuration management in the contract. Agrees with the supplier and the developer on the integrity levels of the software. Standards give it and the supplier a shared understanding. | Configuration Management, Models and Methods, Quality, Engineering Foundations, Appendix B | 187, 233-234, 251, 381, 393 |
| SH-22 | Supplier; outsourcer | Is a party to agreements on scope, deliverables and quality requirements. Can take over the maintenance with a service-level agreement. Its performance is managed in operations. | Operations, Maintenance, Configuration Management, Management, Models and Methods, Quality, Professional Practice, Appendix B | 157, 174, 187, 212-213, 233-234, 251, 278, 282, 393 |
| SH-23 | Quality assurance team; SQA authority; quality analyst; software quality engineering team | Usually manages the items that do not conform. Can monitor the compliance of configuration management. For critical systems, takes part in the qualification of the products before delivery. | Requirements, Testing, Operations, Maintenance, Configuration Management, Quality | 54, 122, 163, 181, 187, 189, 195, 255, 258 |
| SH-24 | Independent third party; independent organization | Usually does the evaluation of an architecture. Can do a design review. Can do verification and validation for very critical software. Frequently does audits. | Architecture, Design, Quality | 76, 95, 254, 256, 259 |
| SH-25 | Configuration control board | Accepts, changes, rejects or defers a change. Decides what the next release contains. | Maintenance, Configuration Management | 179, 194 |
| SH-26 | Person or unit responsible for configuration management | Makes sure that the assigned staff does the tasks of configuration management correctly. | Configuration Management | 187, 189 |
| SH-27 | Requester of a change | Proposes a change and gets the decision. | Configuration Management | 193 |
| SH-28 | Auditor | Does the configuration audits. An audit needs defined roles and responsibilities for the auditors. | Configuration Management | 196 |
| SH-29 | Product owner | Agrees with the software engineers on the risk tolerance for alerts. Decides which items go into the product backlog in Scrum. | Operations, Models and Methods | 162, 242 |
| SH-30 | Product manager | For large systems, a schedule of changes can be necessary. It is planned with the product manager and the end users. | Operations | 161 |
| SH-31 | Scrum master | Manages the sprint. | Testing, Models and Methods | 138, 242 |
| SH-32 | Release manager | Monitors the development and the schedule of each release. Connects development and operations. | Models and Methods | 243 |
| SH-33 | Platform engineering role | Builds self-service platforms. | Operations | 152 |
| SH-58 | Site reliability engineering role | Monitors and improves operations for the non-functional aspects. | Operations | 152 |
| SH-34 | DevOps team; DevOps personnel | Takes part in deployment, in release engineering and in continuous tests. | Operations, Maintenance | 160, 163, 181 |
| SH-35 | Security specialist; security team; security expert | Must know how to apply the security methods. Works together with the developers. Security experts with skill in the application domain should do the dynamic security tests. | Operations, Configuration Management, Security | 159, 195, 265, 266, 268 |
| SH-36 | Attacker; threat actor | Is the source of the threats that the security requirements consider. | Security | 266, 269 |
| SH-37 | Consumer of security evaluation results | The results can help a consumer to decide if an IT product satisfies its security needs. | Security | 266 |
| SH-38 | The public; society | Can get a negative effect from software of low quality. Conformance to a standard lets an organization assure the public. Engineers work with members of the public. | Quality, Professional Practice, Economics, Engineering Foundations | 249, 282, 298, 381 |
| SH-39 | Employer | Has interests in confidentiality and in intellectual property. Software engineers must sign agreements on these. Uses the body of knowledge to judge the knowledge of a person. | Professional Practice, Appendix B | 278-279, 393 |
| SH-40 | Shareholder; investor; financial auditor | Gets the financial statements. | Economics | 303 |
| SH-41 | Competitor | Gets an effect when an asset of the organization is improved. | Economics | 300 |
| SH-42 | Decision-maker | Gets the business case. | Economics | 303 |
| SH-43 | Project steering committee | Gets the internal progress reports. | Management | 214 |
| SH-44 | Project Management Office | Has specialists for estimation. Their plans are integrated into the project plan. | Management | 211 |
| SH-45 | Measurement roles: data provider, measurement user, analyst, librarian | The data providers and the measurement users should take part in the review of the measurement data. | Management | 215, 217 |
| SH-46 | Database roles: user, architect, engineer, administrator | The engineers select how SQL and views are used. An administrator role does backups and patches. | Computing Foundations | 328, 329, 330 |
| SH-47 | Network roles: network manager, network architect | The network manager needs knowledge of time protocols and synchronization protocols. | Computing Foundations | 328, 334 |
| SH-48 | Data scientist | Works in one team with software engineers for systems with artificial intelligence. | Computing Foundations | 338 |
| SH-49 | Learner; researcher; educator; curriculum developer | The guide is made for learners, researchers and practitioners. It is a source for curricula. | Introduction, Appendix A, Appendix B | 26, 391, 393 |
| SH-50 | Licensing authority (governmental or statutory body) | Gives licenses and can enforce codes. | Professional Practice | 276, 277 |
| SH-59 | Accreditation body | Accredits programs. It is independent of the government. | Professional Practice | 275, 276 |
| SH-51 | Attorney; trade expert | Gives advice on legal matters and on trade compliance. | Professional Practice | 279, 280 |
| SH-52 | Service provider; system integrator; system administrator | Must know how to apply the security methods. | Security | 265 |
| SH-53 | Analyst | Has a common language of the domain with the designer. | Design | 95 |
| SH-54 | Team: project team, development team, design team | Does the processes of the life cycle. The approach to construction has an effect on the ability of the team to decrease complexity, to prepare for change and to build for verification. The development team should obey the procedures of configuration control. | Design, Construction, Management, Process, Security | 90, 103, 214, 223, 228, 266 |
| SH-55 | Community of interest of a standard | The makers of a standard look for its consensus, which gives a good probability that the standard is accepted widely. | Engineering Foundations | 382 |
| SH-56 | Gamer | Takes part in play tests. | Testing | 142 |
| SH-57 | Steering group of the guide | Made the baseline of the knowledge areas. | Appendix A | 388 |
| SH-60 | Team of the editors of the knowledge areas | Handles the change requests to the baseline of the knowledge areas. | Appendix A | 388, 392 |

## Requirements: how to find, to give priority and to decide a conflict

### How to find requirements

| Row | Statement | Knowledge area | Pages |
|---|---|---|---|
| RQ-01 | Requirements are elicited from many sources. Many projects get a benefit from an analysis of the stakeholders: it decreases the possibility of a bias to the stakeholders that are better represented. | Requirements | 49 |
| RQ-02 | Techniques with persons: interviews, meetings, joint sessions (JAD, JRP), protocol analysis, focus groups, questionnaires and surveys, exploratory prototypes, and user story mapping. | Requirements | 49 |
| RQ-03 | Sources that are not persons: earlier versions and their defect data, documents, other systems, the business context, the computing environment, benchmarks, literature, QFD, observation, usage scenarios, task analysis and design thinking. | Requirements | 49-50 |
| RQ-04 | The "5 whys" technique asks "why" again and again to find the true problem. | Requirements, Economics | 50, 292 |
| RQ-05 | The analysis examines each requirement for properties such as no ambiguity, testability and atomicity. The full set should be complete, concise, consistent and feasible. | Requirements | 50 |
| RQ-06 | The analysis of the architecture collects the requirements that are significant for the architecture. Its basis is the concerns and the context. Some requirements drive the architecture. Others are deferred to design or construction. | Architecture | 74, 75 |
| RQ-07 | Software engineers must elicit the quality requirements, also those that are not explicit at the start. Quality targets are defined so that they can be measured at acceptance. | Quality | 256 |
| RQ-08 | Security requirements engineering includes elicitation, specification and prioritization. It considers threats with misuse cases and abuse cases, threat actors and risk assessments. Security requirements can come from laws and regulations. | Security | 266 |
| RQ-09 | In operations, availability and continuity are non-functional requirements from the start of a project. Performance, reliability and load balancing are planned early. | Operations | 156, 158 |
| RQ-10 | In maintenance, modification requests and problem reports are recorded and tracked. A change request is analysed and translated into software terms. The maintenance plan tells how users ask for changes. | Maintenance | 168, 172, 179 |
| RQ-11 | In project management, a feasibility analysis comes first. The activities should include a review of the requirements, for example of elicitation, analysis, specification and validation. The requirements are captured in a project charter or a similar document. | Management | 207 |
| RQ-12 | The needs of the stakeholders are identified in the concept stage. The requirements are refined in the development stage. | Process | 227 |
| RQ-13 | Stakeholders are identified early, to capture their requirements. If there is uncertainty, engineers can read formal sources, interview stakeholders or ask peers. | Professional Practice | 283, 284 |
| RQ-14 | A prototype is a means to elicit requirements and to validate functional requirements. User-centered design has a step that collects the requirements of the users. | Design, Engineering Foundations | 94, 375 |
| RQ-15 | A software engineer analyses the problem for functional requirements, user interactions, performance, interfaces, security and the ability to upgrade. | Computing Foundations | 313 |

### How to give priority

| Row | Statement | Knowledge area | Pages |
|---|---|---|---|
| RQ-20 | Factors that can be relevant to a priority are: value, undesirability, cost to deliver, cost to maintain, technical risk, and the risk that the function is not used. | Requirements | 60 |
| RQ-21 | The Kano model shows that value alone can give a wrong priority. | Requirements | 60 |
| RQ-22 | One example of a function is: priority = value × (1 − risk). The text gives it as an example only. | Requirements | 60 |
| RQ-23 | A priority can be given in different ways, which include a scale of named values, a number, or a sorted list. It helps to put requirements with similar priorities into groups. | Requirements | 60 |
| RQ-24 | In agile work, only the requirements with the highest priority go into a sprint. In XP, stories get a priority and an estimate. In Scrum, the product owner decides which items go into the product backlog. Stakeholders can change priorities during development. | Requirements, Management, Models and Methods, Professional Practice | 59, 208, 242, 283 |
| RQ-25 | Requirements can be ranked to deliver the most value in the limits of schedule, budget and technology. The text refers to the Software Requirements KA for the method. | Economics | 306 |
| RQ-26 | Maintainers need a scheme to put requests and reports into categories and to give them a priority. Maintainers frequently use the severity of a problem report as a guide for how and when it is corrected. In practice, new features frequently get a higher priority than other maintenance work. | Maintenance | 172, 173 |
| RQ-27 | In operations, a change request is recorded and gets a class, for example emergency, urgent, major or minor. | Operations | 161 |
| RQ-28 | A change request can have a requested priority, which the requester proposes. | Configuration Management | 193 |
| RQ-29 | Integrity levels are set by agreement between acquirer, supplier and developer. A higher risk can make stricter reviews or more formal verification and validation necessary. | Quality | 250, 251 |
| RQ-30 | A trade-off analysis identifies the requirements that compete and those that complement each other, and gives priorities to the final set. The steps: set the design goals and their relative importance, then find the solution that is nearest to them. | Professional Practice | 282 |
| RQ-31 | For security requirements, the text names prioritization methods but does not describe them. IEEE 7000 has a step that elicits ethical values and gives them a priority. | Security, Appendix B | 266, 403 |

### How to decide a conflict

| Row | Statement | Knowledge area | Pages |
|---|---|---|---|
| RQ-40 | In most cases, the engineer should not decide a conflict alone. The engineer negotiates with the stakeholders to get a consensus. For contractual reasons, it is frequently important that a decision can be traced to the customer. | Requirements | 52 |
| RQ-41 | The product family approach divides requirements into those on which all agree (invariant) and those with a conflict (variant). | Requirements | 52 |
| RQ-42 | If the scope is larger than cost, schedule or staff permit: decrease the scope (remove the items with the lowest priority), increase the capacity, or negotiate a mix of the two. | Requirements | 59 |
| RQ-43 | If requirements and constraints cannot be satisfied without an effect on cost or schedule, a negotiation changes the incoming needs. Trade-offs between quality requirements that compete are frequently the basis for design decisions. The ATAM method uses a utility tree and scenarios to analyse them. | Architecture | 73, 75, 77 |
| RQ-44 | A trade-off analysis weighs risks, costs and benefits together with the stakeholders. If a project is late or above its budget, requirements can be relaxed or removed after such an analysis. The engineer must be objective when setting criteria and weights, and must first disclose conflicts of interest. | Professional Practice | 282 |
| RQ-45 | A change request for the software gets a technical evaluation (an impact analysis). Then an authority for the baseline (the configuration control board) accepts, changes, rejects or defers it. For a change of a requirement, an impact analysis is an optional step; the responsible person or group decides, and the stakeholders that the change touches are told. A deviation or a waiver is a formal written permission not to satisfy a requirement. | Requirements, Configuration Management | 59, 193, 194, 195 |
| RQ-46 | Release planning identifies conflicts and develops alternatives. In maintenance, the content is agreed with the users, and configuration control boards decide the content of the next release. | Operations, Maintenance | 157, 178, 179 |
| RQ-47 | A change follows the change management and the trade-off procedures that the stakeholders agreed. Traceability and risk analysis show the effect of an accepted change. | Management | 208 |
| RQ-48 | Consistency checks find requirements that conflict, with a tool or in a review. | Models and Methods | 238 |
| RQ-49 | Some quality characteristics conflict; the example is encryption against performance. Trade-offs between cost, schedule and quality are a basic principle of engineering. | Quality | 248, 256 |
| RQ-50 | For decision criteria (not for requirements), there are techniques that let one criterion compensate a different one (for example additive weighting, the analytic hierarchy process) and techniques that do not (dominance, satisficing, lexicography). | Economics | 297 |
| RQ-51 | A predictive life cycle can fix the requirements after the customer agrees. An open life cycle permits a change at each point, by negotiation. | Process | 225 |

## Viewpoints, views and concerns

| Row | Statement | Knowledge area | Pages |
|---|---|---|---|
| VW-01 | A concern is an interest of a stakeholder. Concerns come from requirements, quality attributes, emergent properties and constraints. They change during the life cycle. A concern can be functional, non-functional or a constraint. | Architecture | 69 |
| VW-02 | A view shows aspects of an architecture to answer concerns. Different views answer different concerns. Examples: the logical, the process, the physical and the development view. | Architecture | 71 |
| VW-03 | A viewpoint gives the conventions for a view. It connects the concerns of stakeholders with a set of conventions. | Architecture | 71 |
| VW-04 | Common viewpoints include: module, component and connector, logical, scenarios or use cases, information, and deployment. Other viewpoints are for properties such as availability, performance, reliability, safety and security. | Architecture | 71 |
| VW-05 | Viewpoints are put into three classes (viewtypes): module, component and connector, and allocation. | Architecture | 71 |
| VW-06 | There are two approaches to make and combine views. Synthetic: the views are made and then integrated with correspondence rules. Projective: each view is derived from one common model. | Architecture | 71 |
| VW-07 | More than one view can cause inconsistency (the multiple views problem). In the synthetic approach, traceability connects the views to get consistency. A viewpoint can include consistency rules. | Architecture | 72 |
| VW-08 | The 4+1 model describes the software as end users, developers and project managers see it. | Architecture | 79 |
| VW-09 | In design, a concern is an area of interest that is relevant to one or more stakeholders. Concerns are separated, thus the designer can work on one at a time. Aspects are concerns that go across the functional decomposition. The design qualities are an important subclass of the concerns. | Design | 85, 86, 88 |
| VW-10 | Design notations are in two groups: structural descriptions (the static view) and behavioural descriptions (the dynamic behaviour). | Design | 91, 92 |
| VW-11 | A model gives views of the software, with defined rules for each view. Examples: structural, behavioural, temporal and organizational. A view puts the focus on specific concerns. More than one view can be necessary. A complete model can be a union of submodels, each made for one purpose. | Models and Methods | 234, 235, 236 |
| VW-12 | Structured analysis works from a functional or behavioural viewpoint. Data modelling works from the viewpoint of the data. | Models and Methods | 239 |
| VW-13 | Requirements can depend on the perspective: a requirement for one team can be a design decision for a different team. Stakeholders with similar perspectives and needs are put into classes. A review from more than one perspective is preferred. | Requirements | 48, 49, 58 |
| VW-14 | A perspective-based review takes one technical perspective. A role-based review takes the view of different stakeholder roles. Quality is seen from two sides: the product and the process. | Quality | 247, 259 |
| VW-15 | Different abstractions of the same software on one level (for example a class diagram, a state chart and a sequence diagram) complement each other. They do not make a hierarchy. | Engineering Foundations | 370 |
| VW-16 | For money criteria, each alternative must be judged from the same viewpoint. A business case summarizes a decision from different perspectives, such as cost, benefit and risk. | Economics | 293, 303 |
| VW-17 | Tests can be considered from the viewpoint of quality analysts and of certifiers. Test measures can be put into classes from different viewpoints. | Testing | 122, 132-133 |
| VW-18 | The definitions of viewpoint and of architecture framework cite a reference by its number. The first reader reported that this reference is ISO/IEC/IEEE 42010:2011 in the reference list of the chapter. | Architecture | 71, 73, 81 |

The readers reported no method that tells how to find concerns or viewpoints. The other
knowledge areas use "view", "viewpoint" or "perspective" only in the general sense.

## Life cycle processes and their stakeholders

| Row | Processes | Stakeholders that take part | Knowledge area | Pages |
|---|---|---|---|---|
| LC-01 | Four categories of processes, from ISO/IEC/IEEE 12207: agreement, organizational project-enabling, technical management, and technical. The guide does not include the agreement processes (acquisition and supply). | The text assigns no stakeholder to each process. It says that all interested parties take part in the life cycle. Executive management puts its focus on the organizational enabling processes. | Process, Appendix B | 224, 228, 397 |
| LC-02 | Stages of the life cycle: concept, development, production, utilization, support and retirement. A different model has: concept, development, operations and maintenance, and retirement. | Concept: the stakeholders, whose needs are identified. Utilization: the users. Support: the developers. Retirement: the team. | Process, Appendix B | 227, 228, 399, 400 |
| LC-03 | Life cycle models: predictive (waterfall), iterative, incremental, and open or agile. The life cycle decides when the requirements work is done. | Predictive: the customer agrees to the specifications. Agile: the communication between the team and the customer is essential. | Requirements, Construction, Process, Engineering Foundations | 44, 102-103, 225, 226, 377 |
| LC-04 | Requirements development (elicitation, analysis, specification, validation) and requirements management (scrubbing, change control, scope matching). Acceptance test driven development has three steps. | Elicitation: the stakeholders. Validation: clients, customers, users, other software engineers, and the engineers who build the software. Change control: the responsible person or group, and the stakeholders that the change touches. Acceptance tests: software engineers, business domain experts and possibly test professionals. | Requirements | 48, 49, 54, 58, 59 |
| LC-05 | Architectural design with three activities that repeat: analysis, synthesis and evaluation. Other processes: implementation, maintenance, management and knowledge management of the architecture. | Evaluation: usually third parties, at set milestones. The description is used by designers, engineers and programmers. | Architecture | 70, 75, 76 |
| LC-06 | Three stages of design: architectural design, high-level design and detailed design. Verification, validation and certification examine the quality of a design. | The output of detailed design goes to the programmers. Stakeholders can use design work products to plan verification and validation. | Design | 83, 87, 88, 90, 96 |
| LC-07 | Construction planning, coding and debugging, unit tests and integration tests, integration, continuous integration, and continuous delivery and deployment. | Planning assigns tasks to software engineers. The software engineer who wrote the code frequently does the unit tests and the integration tests. Incremental integration can give early feedback to developers and customers. | Construction | 99, 103, 105, 107 |
| LC-08 | Three layers of the test process: the organizational test process, the test management process (planning, monitoring and control, completion), and the dynamic test process (design and implementation, environment, execution, incident reports). | Test management: managers and the test team. Acceptance tests: generally done by the end users or with them. Incident reports and completion results: the relevant stakeholders. Agile tests: customers and team personnel. | Testing | 123, 134, 135, 136, 137, 138, 140 |
| LC-09 | Operations as three processes: planning, delivery and control. ISO/IEC/IEEE 12207 gives four activities: prepare, perform, manage results, and support the customer. ISO/IEC/IEEE 20000-1 gives five groups: service delivery, release, control, resolution and relationship. | Planning: operations engineers with customers, suppliers and the organization. Deployment: operations engineers and DevOps teams; the decision on a release is a business decision. Problem resolution: a team of software engineers and operations engineers can be necessary. Change management: for large systems, a schedule of changes can be necessary, planned with the product manager and the end users. Security controls: senior management. | Operations | 154, 155, 156, 157, 159, 160, 161 |
| LC-10 | Maintenance processes from ISO/IEC/IEEE 14764: prepare, perform, do logistics support, and manage the results. Also: transition, the help desk, release planning and configuration management. | The operator and the maintainer are responsible for the activities. Transition: from the developer to operations and the maintenance team. Release planning: the maintainer with the users. Business planning: top management. Maintainers take part in configuration control boards. | Maintenance | 177, 178, 179 |
| LC-11 | Configuration management is a process of the software life cycle. Its parts: management of the process, identification, change control, status accounting, audits, and the management of releases and delivery. | Change control: the requester, the assigned software engineer and the configuration control board. Status accounting: the teams for development, operations, security, maintenance, project management and quality. Audits: auditors; the SQA authority can also monitor the compliance. | Configuration Management | 185, 186, 189, 193, 194, 195, 196 |
| LC-12 | Project management as activities: initiation and scope definition, planning, enactment, review and evaluation, closure, and measurement. The text recommends no life cycle model. | Initiation: the stakeholders agree how requirements and scope are revised. Planning: the relevant stakeholders accept the risk profile and agree to the estimates. Enactment: customers and suppliers; reports go to the steering committee and to clients or users. Closure: the relevant stakeholders document their acceptance. Measurement: the applicable stakeholders approve the plan. | Management | 206, 207-208, 209-211, 212-214, 215-217 |
| LC-13 | Quality management process: plan, evaluate, and corrective and preventive actions. Quality assurance process: prepare, process assurance, product assurance, and verification and validation with tests. | Management sponsors the work. For critical systems, the SQA function can be independent of the project. An independent organization can do verification and validation for very critical software. Third parties frequently do audits. | Quality | 247, 251, 252-254, 255, 256, 258, 259 |
| LC-14 | Security is considered in requirements, design, construction, tests and maintenance. The secure development life cycle builds security in from the start. Vulnerability management frequently includes a disclosure process. | Security design: developers do threat modelling. Dynamic security tests: security experts. Requirements: security teams can include requirements specialists. | Security | 264, 266, 267, 268 |
| LC-15 | Agile methods and their roles: XP, Scrum, FDD (five phases), Lean. Release engineering covers build, assembly and delivery. | XP: the customer is in the team. Scrum: the Scrum master manages the sprint, the product owner decides which items go into the product backlog. Prototypes: the project stakeholders can evaluate them. Release managers connect development and operations. | Models and Methods | 241, 242, 243 |
| LC-16 | The product life cycle: define, build, operate, maintain and retire. The project life cycle with five process groups: initiating, planning, executing, monitoring and controlling, and closing. The engineering decision process with six steps. | For decisions with large consequences, the relevant stakeholders are identified. | Economics | 292, 293, 294, 305, 306 |
| LC-17 | Participation of stakeholders through the life cycle. | Early stages: the stakeholders are identified. Requirements reviews: software engineers, customers and teammates. Agile development: stakeholders can give feedback. Installation and operation: user groups and support personnel can take part. Contracts: customer, supplier and employer. | Professional Practice | 278-279, 281, 283, 285 |
| LC-18 | The engineering process: understand the problem, define criteria, identify solutions, evaluate, select and monitor. Root cause analysis as an improvement process. | The text names no stakeholder for each step. | Engineering Foundations | 367-368, 382-383 |

## Standards that the guide names

| Row | Standard, as the guide writes it | What the guide uses it for | Knowledge area | Pages |
|---|---|---|---|---|
| ST-01 | ISO/IEC/IEEE 12207 (also: ISO/IEC 12207:2008, ISO/IEC/IEEE 12207:2017) | The processes of the software life cycle. It was the basis of version 3 of the guide. For this version, it is a key input, but the guide is not made to conform fully to it. The primary process standard. | Introduction, Design, Construction, Operations, Maintenance, Process, Quality, Economics, Appendix A, Appendix B | 27-28, 98, 116, 153, 154, 177, 228, 231, 249, 292, 391, 394, 396, 397 |
| ST-02 | ISO/IEC/IEEE 15288 | The processes of the system life cycle. Harmonized with 12207. | Maintenance, Economics, Appendix B | 183, 292, 310, 396 |
| ST-03 | ISO/IEC/IEEE 24765:2017 | The vocabulary. The reference for definitions, for example of a software requirement. | Introduction, Requirements, Architecture, Design, Configuration Management, Process, Quality, Appendix A, Appendix B | 38, 42, 44, 66, 81, 85, 86, 98, 185, 201, 231, 262, 391, 402 |
| ST-04 | ISO/IEC/IEEE 29148 | Requirements engineering. Templates for requirements documents. | Requirements, Appendix B | 53, 66, 399, 402 |
| ST-05 | ISO/IEC 25010 | Quality models and quality characteristics. | Requirements, Testing, Quality, Security, Appendix B | 46, 50, 66, 120, 256, 264, 271, 402 |
| ST-06 | ISO/IEC 25000 series; ISO/IEC 25000:2014; ISO/IEC 25030 | Quality attributes that agree with the needs of stakeholders (page 211). A definition of process cites 25000:2014 (pages 223, 231). The process for stakeholder needs and requirements refers to 25030 (page 399). | Management, Process, Appendix B | 211, 223, 231, 398, 399 |
| ST-07 | ISO/IEC/IEEE 42010 | The description of an architecture: the definitions of viewpoint and framework. | Architecture, Appendix B | 71, 73, 81, 399, 408 |
| ST-08 | ISO/IEC/IEEE 42020; ISO/IEC/IEEE 42030 | Architecture processes and architecture evaluation. | Appendix B | 399, 408 |
| ST-09 | IEEE Std 7000-2021 (also: ISO/IEC/IEEE 24748-7000) | A model process for ethical concerns during system design. | Design, Appendix B | 87, 98, 400, 403 |
| ST-10 | ISO/IEC/IEEE 29119 | The test process, test planning, test documentation and test roles. | Testing, Appendix B | 131, 134, 135, 137, 138, 149, 395 |
| ST-11 | IEEE Standard 829-2008 | Software test documentation. | Construction | 105 |
| ST-12 | ISO/IEC/IEEE 20000-1 (also: IEEE 20000) | The process groups of operations and service management. | Operations | 151, 154, 157, 158, 159, 162 |
| ST-13 | ISO/IEC/IEEE 32675 (also: IEEE 2675-2021) | DevOps. | Operations, Maintenance, Management, Process, Models and Methods, Appendix B | 154, 157, 162, 183, 206, 220, 227, 232, 245, 395 |
| ST-14 | ISO/IEC/IEEE 14764 | Maintenance: the definition, the categories and the processes. | Maintenance | 168, 170, 172, 175, 177, 178, 179, 180 |
| ST-15 | IEEE Standard 828-2012 | Configuration management in systems and software engineering. | Configuration Management | 186, 201 |
| ST-16 | ISO/IEC/IEEE 15939 | Measurement. The measurement part of the management area follows it. | Management | 211, 215, 219 |
| ST-17 | ISO/IEC 29110 series | Life cycle profiles for very small entities. | Operations, Process | 163, 228, 232 |
| ST-18 | ISO/IEC/IEEE 24748 series | Guides for life cycle management. | Process, Appendix B | 223, 227, 228, 232, 396, 398-400 |
| ST-19 | ISO/IEC/IEEE 24774 | The specification of a process description. | Process, Appendix B | 224, 232, 394 |
| ST-20 | ISO/IEC 33000 series (also: SPICE, ISO/IEC 15504); ISO/IEC 33001:2015; ISO/IEC TS 33061:2021 | The assessment of processes. | Maintenance, Process, Quality, Appendix B | 183, 230, 231, 253, 402, 403 |
| ST-21 | IEEE 730:2014 | The processes of software quality assurance. | Introduction, Quality | 28, 248, 253, 255, 258 |
| ST-22 | IEEE Standard 1012:2016 | Verification and validation. | Quality, Appendix B | 257, 395 |
| ST-23 | ISO 9001; ISO/IEC/IEEE 90003:2018 | Quality management, and its application to software. | Quality | 250, 251, 263 |
| ST-24 | ISO/IEC 20246:2017 | Reviews of work products. | Testing, Quality | 150, 259 |
| ST-25 | IEEE 1228:1994; IEEE 1633:2016; IEEE 982.1:2005 | Software safety plans, software reliability, and a dictionary of measures. | Quality | 249, 256 |
| ST-26 | DO-178C; EN 50128 | Domain standards: airborne systems and railway applications. | Quality | 250, 262 |
| ST-27 | ISO/IEC 15026-1:2019; IEC 60300-1:2014 | Assurance cases, and the management of dependability. | Quality | 250, 251, 262, 263 |
| ST-28 | ISO/IEC 27000:2018; ISO/IEC 27001:2022; ISO/IEC 27032:2012 | The vocabulary of information security, the information security management system, and guidelines for cybersecurity. | Quality, Security | 250, 264, 265, 271 |
| ST-29 | ISO/IEC 15408:2022; ISO/IEC 18045 | The Common Criteria for security evaluation and their method. The reference list of the chapter writes 18045 with the year 2008. Appendix B writes it with the year 2022. | Security, Appendix B | 266, 272, 404 |
| ST-30 | ISO/IEC 21827:2008; ISO/IEC 19770-1:2017 | The capability maturity model for security engineering, and the management of IT assets. | Security, Appendix B | 265, 271, 404, 405 |
| ST-31 | ISO/IEC 24773-1; ISO/IEC 24773-4 | The certification of software and systems engineering professionals. | Professional Practice | 276 |
| ST-32 | IEEE Std. 1517-2010 | Reuse processes of the software life cycle. | Construction | 116 |
| ST-33 | ISO/IEC 19505-1:2012 | The Unified Modeling Language (UML). | Models and Methods | 245 |
| ST-34 | ISO/IEC/IEEE 31320-1:2012 | The syntax and semantics of IDEF0. | Process | 229, 232 |
| ST-35 | ISO/IEC/IEEE 15289 | The information products of the life cycle. | Appendix B | 394 |
| ST-36 | ISO/IEC TR 19759 | The guide itself as a technical report. | Introduction | 36, 37 |
| ST-37 | CMMI | A model of maturity levels, not a standard. Named for process improvement and for configuration management practices. | Testing, Configuration Management, Process, Quality, Engineering Foundations | 139, 185, 200, 201, 230, 232, 250, 377, 379 |
| ST-38 | PMBOK Guide; Software Extension to the PMBOK Guide | Guides for project management, not standards. | Introduction, Management, Economics | 41, 204, 211, 305, 309 |
| ST-39 | ITIL | A library for IT infrastructure, not a standard. | Operations, Maintenance | 151, 183 |
| ST-40 | Codes of ethics: IEEE, ACM, IFIP; the Software Engineering Code of Ethics and Professional Practice | Ethical conduct. | Quality, Professional Practice, Economics | 249, 277, 287, 301, 310 |
| ST-41 | SQL standard of ANSI and ISO; OSI model of ISO; coding standards of the Software Engineering Institute (SEI) Computer Emergency Response Team (CERT) and of MISRA; CERT/CC guidelines | Standards for a database language, for network layers and for coding. | Security, Computing Foundations | 268, 326, 330, 332 |
| ST-42 | Appendix B of the guide | The list of the IEEE and ISO/IEC standards for each knowledge area (Table B.2). | Introduction, Appendix B | 25, 42, 402 |

## Not verified

The second reading compared each row with the pages of the row. It could not compare these
points:

| Row | What the second reading did not compare |
|---|---|
| All rows of all parts | The cell "Knowledge area" or "Knowledge areas that name it". The second readers did not get this cell. It is derived from the page numbers and the page ranges of the chapters. |
| All rows with a correction | The second readers did not read the corrected sentences again. Each correction uses the words of the finding. |
| KA-01 to KA-18 | The second reader compared each summary with the first three pages of the chapter only, not with all pages of the range. |
| SH-07, SH-33, SH-50, SH-57, SH-58 to SH-61 | These rows are the result of a split after the second reading. The second readers compared the sentences before the split. |
| Note below the table "Viewpoints, views and concerns" | The statement that the readers reported no method to find concerns or viewpoints. It is a statement about the reports, not about one page. |
| ST-37 | The words "not a standard" for CMMI on pages 377 and 379. These pages do not say if CMMI is a model or a standard. |
| ST-29 | The two years of ISO/IEC 18045. Two second readers found different years on different pages (272 and 404). The cause was not examined. |
| All rows | The second readers read the converted text, not the PDF file. The first readers reported that text in two columns is mixed in some places, thus a statement near the border of a page can be on the adjacent page. Figures and tables were compared as converted text only. |
