# Structure note: The Integrated Architecture Framework Explained

Source: the book with this title (Springer, 2010; pages 1, 2). A page is a `## Page N` heading
of the converted file. Pages given to the readers: 1-12, 13-36, 55-76, 209-231. The note tells
how the book organises the work of an architect. `evidence.md` gives the report for each line.

## Levels and their questions

- L1. The book names four levels: contextual, conceptual, logical and physical (page 36).
- L2. The contextual level answers "why". The conceptual level answers "what". The logical
  level answers "how". The physical level answers "with what" (page 36).
- L3. The "why" level holds the drivers, the objectives, the principles and the scope. It
  comes first (pages 13, 27).
- L4. The "what" level defines the requirements. The "how" level makes the logical structure.
  The "with what" level allocates logical components to physical things (page 36).

## Areas

- A1. The levels lie horizontally across the topics. The aspect areas lie vertically (page 27).
- A2. The main aspect areas are business, information, information systems and technology
  infrastructure (pages 37, 219).
- A3. The aspect areas cover the levels "what", "how" and "with what". They do not cover the
  "why" level, because its drivers apply to all areas (page 27).
- A4. Some aspects are a part of each aspect area, but the book handles them separately for
  completeness and consistency. It calls them the third dimension. Examples are quality,
  security and governance (pages 27, 28).

## What is recorded at each level

- W1. Contextual level: a context diagram, policies, architecture objectives, principles,
  constraints, scope, assumptions, technology strategy, standards with rules and guidelines,
  the project portfolio and the baseline of the current state (pages 55-60).
- W2. A principle has an owner, a description, a motivation, an implication, an assurance and
  a priority (pages 56-57).
- W3. Services are the basic building blocks. A service tells what it does, not how. Services
  are defined at the "what" level (page 28).
- W4. Components are sets of services. They are defined at the "how" level and the
  "with what" level (page 28).
- W5. Collaboration contracts tell how services and components interact. They hold the
  non-functional aspects (page 28).
- W6. Views put artifacts in order by a criterion. Interaction models show relations in one
  aspect area. Cross-references show relations between aspect areas (page 29).
- W8. In the deliverables of a solution, the conceptual level typically holds the detailed
  requirements. The logical level holds the architecture, the reasons for decisions and the
  solution alternatives. The physical level holds specifications, products, standards and
  guidelines (page 212).

## How one level is derived from the level above

- D1. The sequence is "why", "what", "how", "with what". Each step needs the step before it
  (pages 13, 14).
- D2. The "what" step changes the "why" into functional and non-functional requirements and a
  concept of the solution (page 13). The "how" step designs a logical solution for the
  requirements, and solution alternatives are examined there (pages 13, 14). The "with what"
  step allocates physical things to the logical solution (pages 14, 15).
- D3. Principles are typically derived from the vision, mission, strategy, objectives and
  drivers of the business, and from the assumptions, scope, constraints and objectives
  (page 57).
- D4. A business service is the combination of one activity, one role and one goal (page 63).
- D5. For components, the architect first defines services without a hierarchy, then makes
  grouping criteria from the principles, then groups the services (page 33).
- D6. Cross-references are an important means for traceability and for the reasons of a
  decision (page 29). It is best practice to base solution alternatives on the principles
  (page 31). The alternatives should be traceable to business principles (page 227).
- D7. The book calls the framework a content framework, not a process framework (page 212).
  One roadmap starts with the context, then does the business area, the information area and
  the information systems area. All logical results are then the basis for the physical
  iterations (page 218).

## How needs are brought together and a conflict is decided

- N1. Principles help to design an architecture that is satisfactory for all stakeholders,
  and they help to resolve conflicting requirements (page 20). Typically, specified
  stakeholders own and validate the principles (pages 56-57).
- N2. The priorities of the principles help the architect to resolve a conflict between
  principles or requirements (page 57).
- N3. A constraint cannot be violated and has no weight. Thus conflicting constraints are not
  weighed (page 57).
- N4. Standards and rules are usually not negotiable. Senior business management decides on a
  breach (page 28). A guideline that cannot be followed needs a waiver (page 29).
- N5. No one solution meets all requirements. Each alternative is a trade-off (pages 14, 24).
  The architect shows the best alternatives, and the stakeholders select (page 15).
- N6. Alternatives are compared in two ways: scores for each criterion, or scores with a
  weight for each criterion (page 31).
- N7. Assumptions are agreed with stakeholders and have an owner. The architect does not make
  them alone (pages 58-59).

## Use for a part of the whole

- P1. The scope includes the enterprise, the business unit and the solution (page 16). The
  types of architecture are enterprise, domain, solution and software, and the size of the
  topics is different for each (page 21).
- P2. Scope and objectives are very important for the selection of the areas of the framework
  and of the level of detail (pages 58, 210).
- P3. The architect can define services in more detail in one area ("zooming in"), and must
  tell the readers about the mixed detail (page 70).
- P4. For a solution architecture, the enterprise architecture should have a scope that agrees
  with the scope of the solution. Its standards and guidelines govern the solution
  architectures (page 211).

## How a result is checked

- C1. The architecture should always be justified in business terms and traced to the
  business requirements (page 16).
- C2. The framework must give mechanisms that show completeness and consistency (page 25).
  For services, the check is the combination of activities, goals and roles (pages 63-64).
- C3. The contextual views are used to validate artifacts (page 61). A view helps to find
  gaps (page 29). One view compares the services of the current state with the services of
  the future state (page 76).
- C5. A design authority can validate the fit to the functional requirements, the standards,
  the readiness of the organization and the economics (page 216).
- C6. Assumptions are validated with the key stakeholders (page 224).

## Not verified

- Pages 37-54, 77-208 and 232-251 were not given to a reader. Page 37 in A2 is from the
  second reading only.
- No reader reported a statement that the full framework is applied again to a part.
- No reader reported how a conflict between two groups of stakeholders is decided, apart
  from N1, N2, N5 and N6.
- The contents list (pages 4-6) also lists quality as a chapter of the areas. No reader
  reported the text of that chapter.
- One report gave statements from page 54, which is not in its range. They are not used.
- One point of the reader of pages 209-231 (page 210) did not agree with page 36. It is not
  used.
