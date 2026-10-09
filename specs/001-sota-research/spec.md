# Aspect specification: Distilling the state of the art of a major aspect

**Branch**: `001-sota-research` | **Research date**: 2026-10-09 | **Supersedes**: the draft of 2026-10-08

This is the first specification of the kit, and it covers the method itself: how the existing
descriptions of the state of the art (SOTA) of a major aspect of software engineering are
found, distilled into one recipe (a strategy and a generic checklist), checked, and kept
current. Every later aspect specification is made with this recipe. DevSecOps is the example that the
factory is improved with.

## 1. Aspect

- **Aspect**: distilling the SOTA of one major aspect of software engineering into a recipe
  that agents and people can apply.
- **Field and disciplines**: evidence synthesis and knowledge curation; it cuts across every
  field of software engineering.
- **Contexts**: how much rides on the aspect (regulated or not); how fast the aspect moves;
  whether authoritative descriptions exist or only practice sources; whether the sources can be
  reached and read; the agent product that runs the work.
- **Risk dimensions**: what depends on the recipe (the harm of a wrong item); regulation of
  the aspect. The question for each: who acts on the recipe without a second check?
- **Boundaries**: the content of each aspect belongs to its own specification. This one owns
  only the method.
- **Agreed with the owner on**: 2026-10-09; the factory first, with DevSecOps as its example.

## 2. Sources

| Id | Source | Issuer | Version or date | Class | License | Read | URL |
|---|---|---|---|---|---|---|---|
| S-01 | Guidelines for performing systematic literature reviews in software engineering, EBSE-2007-01 (Kitchenham and Charters) | Keele University, University of Durham | Version 2.3, 2007-07-09 | research | © Kitchenham 2007; no license stated | full | https://legacyfileshare.elsevier.com/promis_misc/525444systematicreviewsguide.pdf |
| S-02 | The PRISMA 2020 statement (Page et al.) | BMJ | BMJ 2021;372:n71 | research | CC BY 4.0 | full | https://doi.org/10.1136/bmj.n71 |
| S-03 | PRISMA-S, reporting literature searches (Rethlefsen et al.) | Systematic Reviews | 2021, 10:39 | research | CC BY 4.0 | full | https://doi.org/10.1186/s13643-020-01542-z |
| S-04 | Guidelines for including grey literature and conducting multivocal literature reviews in software engineering (Garousi, Felderer, Mäntylä) | Information and Software Technology 106 | 2019; preprint read | research | preprint | full | https://arxiv.org/abs/1707.02553 |
| S-05 | Rapid reviews in software engineering (Cartaxo, Pinto, Soares) | Springer | 2020; preprint read | research | preprint | full | https://arxiv.org/abs/2003.10006 |
| S-06 | NIST IR 8477, Mapping relationships between documentary standards, regulations, frameworks, and guidelines | NIST | 2024-02 | standard | public, no copyright in the US | full | https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8477.pdf |
| S-07 | NIST SP 800-218, Secure Software Development Framework | NIST | Version 1.1, 2022-02 | standard | public, no copyright in the US | full | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf |
| S-08 | ISO/IEC Directives, Part 2, definition of "state of the art" (clause 3.4) | ISO, IEC | ninth edition, 2021 | standard | ISO copyright | part | https://www.iso.org/sites/directives/current/part2/index.xhtml |
| S-09 | Guideline "State of the art" in IT security, chapter 2 | TeleTrusT | English edition, 2025-09 | independent | not stated | full | https://www.teletrust.de/en/publikationen/broschueren/state-of-the-art-in-it-security/ |
| S-10 | BVerfGE 49, 89 (Kalkar I), marginal numbers 104 to 106 | Bundesverfassungsgericht; text from the DFR database, University of Bern | 1978-08-08 | standard | official work | full | https://www.servat.unibe.ch/dfr/bv049089.html |
| S-11 | SWEBOK Guide, introduction: "generally accepted" knowledge | IEEE Computer Society | v4.0a, released 2026-08 | standard | free for personal and academic use; no commercial reprint | part | https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf |
| S-12 | Guidance for the production and publication of Cochrane living systematic reviews | Cochrane | 2019-12 | foundation | not stated | part | https://community.cochrane.org/sites/default/files/uploads/inline-files/Transform/201912_LSR_Revised_Guidance.pdf |
| S-13 | Position statement on AI use in evidence synthesis (Flemyng et al.) | Cochrane, Campbell, JBI, CEE | 2025-11-06 | research | CC BY 4.0 | full | https://pmc.ncbi.nlm.nih.gov/articles/PMC12594113/ |
| S-14 | Cited but Not Verified: parsing and evaluating source attribution in LLM deep research agents (Onweller et al.) | arXiv 2605.06635 | v1, 2026-05-07 | independent | preprint | full | https://arxiv.org/abs/2605.06635 |
| S-15 | OWASP Top 10 for LLM applications, LLM01 prompt injection | OWASP | LLM01:2025 | foundation | CC BY-SA 4.0 | full | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ |
| S-16 | Agent Skills specification | agentskills.io | read 2026-10-09 | vendor | CC BY 4.0 | full | https://agentskills.io/specification |
| S-17 | Evaluating AGENTS.md: are repository-level context files helpful for coding agents? (Gloaguen et al.) | arXiv 2602.11988 | v3, 2026-09-29 | independent | preprint | full | https://arxiv.org/abs/2602.11988 |
| S-18 | ANSI/NISO Z39.19-2005 (R2010), Guidelines for the construction, format, and management of monolingual controlled vocabularies | NISO | 2005, reaffirmed 2010 | standard | © NISO; noncommercial reproduction with attribution | full | https://groups.niso.org/higherlogic/ws/public/download/12591/z39-19-2005r2010.pdf |
| S-19 | Documenting architecture decisions (Nygard) | Cognitect | 2011-11-15 | independent | CC0 1.0 | full | https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions |
| S-20 | OSPS Baseline, maintenance process | OpenSSF | read 2026-10-09 | foundation | Apache-2.0 | full | https://baseline.openssf.org/maintenance.html |
| S-21 | Exploring internal stickiness: impediments to the transfer of best practice within the firm (Szulanski) | Strategic Management Journal 17 | 1996 | research | paid | part | https://doi.org/10.1002/smj.4250171105 |
| S-22 | Introduction of surgical safety checklists in Ontario, Canada (Urbach et al.) | NEJM 370:1029 | 2014-03-13 | research | paid | part | https://doi.org/10.1056/NEJMsa1308261 |
| S-23 | A leader's framework for decision making (Snowden and Boone) | Harvard Business Review | 2007-11 | research | paid | part | https://hbr.org/2007/11/a-leaders-framework-for-decision-making |
| S-24 | Spec Kit, presets reference: file resolution | GitHub | read 2026-10-09 | vendor | MIT | full | https://github.com/github/spec-kit/blob/main/docs/reference/presets.md |
| S-25 | Guidelines for snowballing in systematic literature studies and a replication in software engineering (Wohlin) | ACM, EASE 2014 | 2014-05 | research | paid; author copy read | full | https://doi.org/10.1145/2601248.2601268 |
| S-26 | SLSA, specification stages and versioning | OpenSSF | read 2026-10-09 | foundation | Community Specification 1.0 | full | https://slsa.dev/spec-stages |
| S-27 | GRADE: an emerging consensus on rating quality of evidence and strength of recommendations (Guyatt et al.) | BMJ | BMJ 2008;336:924 | research | paid; open copy at PubMed Central read | full | https://doi.org/10.1136/bmj.39489.470347.AD |
| S-28 | The NIST Cybersecurity Framework (CSF) 2.0, NIST CSWP 29 | NIST | 2024-02-26 | standard | public, no copyright in the US | full | https://doi.org/10.6028/NIST.CSWP.29 |

## 3. Strategy

### 3.1 Goals

- One recipe for the aspect: a strategy and a generic checklist that an agent can apply and a
  person can review in one sitting.
- The recipe holds the global state of the art: the best practices that the industry has
  produced so far, each with a recommendation that the user can adopt or decline.
- Each statement traces to an existing description, cited by its own identifier, and was
  checked against the text of that description.
- The recipe is small enough to load when it is needed, and it says when it must be read again.

### 3.2 Order of the work

1. **What to build.** Settle with the owner, in dialogue, the aspect, its contexts and its
   boundaries. A scope that is fixed first reduces the bias of what the search finds.
2. **Research.** List what exists: the SOTA of most aspects is already written down. Search
   and fetch openly, with isolated readers. Give each source its class. Vet each independent
   source. Distil: a statement that holds across contexts becomes a checklist item, one that
   depends on context becomes a decision of the strategy, one about a single product goes to an
   implementation skill, and what an agent can learn elsewhere is left out. Write for each
   source a summary of what it contributes, and let a second reader check it. Run the calculation of risk and reward. Record where the sources disagree.
3. **Review.** A person reviews the findings and the strategies. A model does not accept a
   recipe.
4. **Spec Kit and implementation.** Render the recipe skill. Name the implementation skills
   that layer two must work out. Then watch the sources, and refresh when one moved.

### 3.3 Decisions that depend on context

| Decision | Depends on | Options | Sources |
|---|---|---|---|
| Depth of the review | what rides on the aspect; time | a rapid review with every concession written in the scope, or a full review with a second reviewer | S-01, S-05 |
| Practice sources next to standards and research | whether authoritative descriptions cover the aspect | include them when the context is important or formal evidence is thin, leave them out for a mature and bounded research topic, and assess each on producer, method, objectivity, date, novelty, impact and outlet | S-04 guideline 3, table 4, guideline 11 |
| Route of admission of an item | the class of its sources | fast lane for a standard, foundation, vendor, research or trusted-data source, more so when several agree; vetting first for an independent source | constitution II |
| Where a person decides | the risk of a wrong item | the source asks for human oversight and keeps the authors accountable; this kit sets: always what to build, and the review of the findings and strategies | S-13 |
| What goes into the recipe and what into reference files | the size of the result; the agent product | the skill body holds the strategy; the checklist loads on demand from a reference file; the specification is the source of both | S-16, S-17 |
| How far a project goes past level 1 | the risk of the project on each risk dimension of the aspect | assessed with the owner of the project, by each aspect; for this aspect the owner of the kit adopts or declines the items | constitution V |
| Refresh cadence | how fast the aspect moves | a fixed interval, or a refresh when new information is likely to change the result; stop when no relevant change emerges any more or the question lost its priority | S-12 sections 4.1, 8.1 |

### 3.4 Where the sources disagree

| Question | Positions | How this recipe handles it | Sources |
|---|---|---|---|
| Which level "state of the art" names | The consolidated stage (ISO: consolidated findings; SWEBOK: generally accepted knowledge). Or the stage ahead of the accepted rules: at the front of development (Kalkar), between research and the generally accepted rules, and proven in practice (TeleTrusT). | This kit aims at the global state of the art: the best practices that the industry has produced so far, which can be ahead of what is generally accepted and of what one organization does today. An item enters on two questions: is it recognized by experts, and is it proven in practice. Spread and newness do not count. | S-08, S-09, S-10, S-11 |
| Whether "best practice" exists outside simple contexts | Best practice is past practice and is often appropriate in simple contexts; in complicated contexts good practice is more appropriate, and complex and chaotic contexts need other approaches. Or a framework states outcome practices and adds examples that are not required. | Checklist items are generic and say what, not how. Everything that depends on context is a decision of the strategy. | S-23, S-07 |
| Protocol first, or search that follows the sources | A protocol before the search reduces researcher bias, and its stages iterate. Protocol-driven database search alone is not necessarily the most efficient way to find sources. | Scope first. Changes of the scope during the work are allowed and recorded with their reason. | S-01 section 5.4; S-25 section 1; S-02 item 24c |
| Update in place, or a new version | A living review shows its status and last search date in a status table and publishes a new version when new information is likely to change the result or on a fixed schedule. A reversed decision record is kept and marked superseded. | A refresh without change updates the research date. A changed item or decision gets a row in section 7, and the earlier one is marked superseded. | S-12, S-19 |
| Whether instruction files help agents | No general gain in task success, and over 20 % more cost. Useful for practices that are not standard. | Keep only what the agent cannot learn elsewhere, and test a recipe on a real case before it is relied on. | S-17 |

## 4. Checklist

For this aspect, the thing that is checked is an aspect specification made with this recipe.

| Id | Item | Why | Level | Admitted by | Check | Source |
|---|---|---|---|---|---|---|
| C-01 | The aspect, its contexts and its boundaries are written and confirmed before the search. | Risk: the search steers the scope. A scope that is fixed first reduces the bias of what the search finds. | pending | authority (1) | section 1 is filled and names the date of the agreement | S-01 sections 5.3, 5.4 |
| C-02 | The existing descriptions of the aspect are listed with issuer, version or date, class, license and how much was read. | Risk: the recipe invents again what exists, or misses it. The SOTA of most aspects is already written down; the work is to distil it. The search record names each source and its date; the other cells are this kit's addition. | pending | authority (2) | every row of section 2 has every cell | S-03 items 1, 13 (source and date); S-04 guideline 11 |
| C-03 | Each source has a class, and each item names the sources that support it; no single source gates the recipe. | A recipe that follows one description inherits its limits. A mapping holds only for the use it was made for. | pending | own rule (I) | every row of section 2 has a class; every Source cell names an S-id of section 2 or a principle of the constitution | constitution I; S-06 section 4 |
| C-04 | Each checklist item is one short sentence that holds across contexts. | Risk: an item that holds in one context only misleads in the others. The outcome holds across contexts; the way to reach it must be adapted. | pending | authority (2) | no item names a technology, a tool or a vendor from the word list of the aspect | S-07 sections 1, 2; S-23 |
| C-05 | Each item cites the unit of its source by identifier, and no text of a source is copied. | Some descriptions limit redistribution; an identifier stays valid when the issuer does not reuse it. | pending | authority (2) | every Source cell names an S-id of section 2 or a principle of the constitution | S-11 copyright notice; S-20 "Identifiers" |
| C-06 | Each item names the check that shows it is met, or says that it needs judgement. | Risk: nobody can tell cheaply if an item is met. An agent needs cheap feedback on what remains. | pending | own rule (IX) | no Check cell is empty | constitution IX |
| C-07 | Each cited source was read, and the item says no more than the source says. | Research agents cite pages that exist far more often than pages that support the claim. | pending | practice, vetting pending | `evidence.md` has a row for each cited source, and the row names the item; a source read "no" carries no item alone. Whether the summary matches the source: judgement, by a second reader | S-14 abstract, finding 1 |
| C-08 | An item is in the checklist because experts recognize it and practice has proven it. | Risk: a popular or new practice enters without proof. Recognition and proof in practice set the level of a measure, not its spread or its newness. | pending | practice, vetting pending | judgement | S-09 sections 2.1, 2.2 |
| C-09 | Where sources disagree, both positions and the handling are written down. | Risk: a hidden disagreement looks like agreement. Contradictions and ambiguities that are recorded help the next revision. | pending | authority (1) | section 3.4 is present; "none found" is an allowed entry | S-06 section 4 (contrary), section 5 |
| C-10 | A term that the sources use with several meanings has one preferred form and its other meanings listed. | Risk: the reader picks the wrong meaning of a term. In a controlled vocabulary each term has one meaning only. | pending | authority (1) | each term of the glossary has both cells | S-18 sections 5.3.1, 6.2.2 |
| C-11 | Each use of a model that made or suggested a judgement is reported, and a named person accepted the result. | Risk: a judgement of a model passes as the judgement of a person. The people who publish the result stay accountable for it. | pending | authority (1) | section 7 names the model roles and the person who accepted | S-13 key messages |
| C-12 | Text read from a source is handled as untrusted data and kept apart from instructions. | Injected text can steer a model, and it is not clear that a method prevents it fully. | pending | authority (1) | each prompt of the skill states the rule | S-15 "Prevention and Mitigation Strategies", introduction, mitigation 6 |
| C-13 | The recipe holds nothing that an agent can learn from the project or from the source itself. | Risk: the recipe overloads the context of the agent. Extra context costs and does not raise success. | pending | practice, vetting pending | judgement | S-17 abstract, section 1 |
| C-14 | Identifiers stay stable: a substantial change of meaning gets a new identifier, and a retired one is not used again. | Risk: a reference points at an item that changed. Skills, agents and earlier reports point at the identifiers. | pending | authority (2) | no identifier of the previous revision has a different item | S-20 "Identifiers"; S-26 "Versioning" |
| C-15 | Each decision is a record with a date; a reversed decision stays and is marked superseded. | Risk: a decision is repeated or reversed without its reason. The motivation behind a decision is one of the hardest things to track. The date is this kit's addition. | pending | practice, vetting pending | every row of section 7 has a date | S-19 "Context", "Decision" |
| C-16 | The watch list names what to read again and when, with the version of every source. | A source that moved makes an item wrong without notice. | pending | authority (2) | every source of section 2 has a version or date; section 6 has at least one row | S-12 section 4.1; S-20 "Versions/releases" |
| C-17 | A practice taken from another aspect or field states the problem it solves there and what would show that it does not work here. | A practice whose cause is not understood is hard to transfer, and one large adoption of checklists brought no significant decrease of deaths or complications. The item itself is this kit's rule. | pending | own rule (IV) | judgement | constitution IV; S-21 abstract; S-22 abstract |
| C-18 | Each item carries a level that a calculation of risk and reward assigns, set apart from how well the item is evidenced. | Risk: the level of an item follows the amount of its evidence, not its return. Good evidence does not always mean a strong recommendation, and a strong recommendation can rest on weak evidence. | pending | authority (1) | no Level cell is empty; `vetting.md` has the answers of the calculation | S-27 |
| C-19 | The user selects: a target level for each risk dimension, and single items declined with a reason, kept as a checklist with the project and simple to revisit. | Risk: a project adopts items that do not fit its risk. The outcomes that count are the ones that the user selected and ranked for the project. | pending | authority (1) | the recipe skill block names the selection as its target | S-28 section 3 |
| C-20 | A source from a smaller independent issuer is vetted with measured signals before it supports an item, and the owner confirms the result. | A blog or a small repository can be outdated, poisoned or an attack; the trust in a source must be measured as the trust in a library is. | pending | own rule (II) | `vetting.md` has an entry for each source of class independent | constitution II |
| C-21 | A reader of sources works without a shell, without credentials and without access to the repository. | The moment a model reads a page is the moment hostile content can act. | pending | own rule (III) | the reader role lists no such tool | constitution III; S-15 |
| C-22 | A person settles what to build before the research and reviews the findings and the strategies before anything is built. | Risk: the factory builds the wrong thing, or builds on wrong findings. Automation in evidence work is used with human oversight. | pending | authority (1) | section 7 names the person and both dates | S-13 key messages |

**Selection.** For this aspect the user is the owner of the kit, who adopts or declines the
items above for the kit as a whole. Section 7 records it when the review is done.

## 5. Skill set to define

### Recipe skill and agent: sota-research

Tooling of this repository, not a plugin of the marketplace.

- **Goal**: one reviewed aspect specification, made with this recipe.
- **Reads first**: the contexts of section 1 for the aspect; what the owner already trusts;
  whether an earlier revision exists; whether the sources can be reached.
- **Applies**: the strategy of section 3; it judges C-08, C-13 and C-17.
- **Delegates**: the reading and quoting of each source, the vetting of sources, the calculation
  of risk and reward, the check of the specification, and the rendering of the recipe skill.
- **Stops when**: the owner accepted the specification; the sources cannot be reached, so the
  result is incomplete and says so; or a decision of 3.3 needs the owner.

### Implementation skills (layer two)

| Product or tool | Capability | Checklist items it implements | Helper software it needs |
|---|---|---|---|
| Spec Kit | the layer-one command and template beside the unchanged product flow | C-01, C-22 | none: Spec Kit resolves a project-local template first (S-24) |
| The collector of `library-vetting` | measured signals for an independent source | C-20 | a rubric for sources and a program that scores it |
| This repository | the calculation of risk and reward | C-18 | a rubric and a program that computes admission, order and level |
| This repository | the check of an aspect specification and its evidence record | C-02 to C-07, C-09, C-10, C-14 to C-16 | a program that reports each failing check and what remains |
| This repository | render the recipe skill from its specification | C-13, C-19 | a program, with a test that fails when a skill differs from a fresh rendering |

## 6. Watch list

| Signal | Where to read it | Cadence |
|---|---|---|
| A new version or a changed status of a source of section 2 | the issuer's own page | at each refresh |
| New guidance on the use of models in evidence synthesis | Cochrane, JBI and Campbell | at each refresh |
| New measurements of how well research agents cite | the preprint servers | at each refresh |
| A change of the skill format or of the specification tool | agentskills.io; the Spec Kit repository | at each refresh |

## 7. Decisions and changes

| Date | Decision or change | Reason | Revisit when |
|---|---|---|---|
| 2026-10-08 | Each artifact type has one top-level folder. | Owner. | a type does not fit |
| 2026-10-08 | The repository stores no source material; artifacts hold instructions and references. | Owner. |  |
| 2026-10-09 | The repository is a construction kit: one recipe (strategy and generic checklist) per major aspect, with technology skills below it. It stays high level. | Owner. | a recipe grows beyond one sitting |
| 2026-10-09 | One specification per major aspect. | Owner. | an aspect proves too wide for one recipe |
| 2026-10-09 | A checklist has no fixed number of items; it is distilled. | Owner. |  |
| 2026-10-09 | Delivery and deployment are different. How software reaches its users (deployed, distributed, fielded, world-wide rollout) is a context. CM means continuous monitoring. | Owner; the sources agree on delivery and deployment and split on CM. | the DevSecOps specification is written |
| 2026-10-09 | The first aspect is DevSecOps. | Owner. | |
| 2026-10-09 | The kit aims at the global state of the art: the best practices that the industry has produced so far. In one company the term can mean the best of what that company does today; that is not the measure here. The kit collects and recommends by use case, technology and stack, and the user selects what to adopt. The catalog as a whole works like the golden paths of a developer portal. | Owner. |  |
| 2026-10-09 | This revision supersedes the draft of 2026-10-08. That draft was written while most sources were blocked. A check against the text of 53 sources found that 18 of 87 citations supported their row in full, 58 in part and 11 not at all. This revision keeps only statements whose source was read, and two reviewers checked each citation of this revision against the text of its source. | C-07. |  |
| 2026-10-09 | Models used: a small model read the sources; a mid-size model judged each citation and each line of the evidence record against the text; the session model wrote this specification. Accepted by: pending, the owner. | C-11. |  |
| 2026-10-09 | The factory has a person in the loop: what to build is settled in dialogue, then the research runs, then a person reviews the findings and the strategies, then Spec Kit and the implementation follow. | Owner. |  |
| 2026-10-09 | Spec Kit works in layers. Layer one is the aspect specification, the source of the recipe. Layer two is one specification per set of implementation skills with their helper software, through the product flow. The layers iterate. DevSecOps is the example that the factory is improved with. | Owner. Fact: the tasks step of Spec Kit requires user stories, which an aspect specification does not have. | the first product specification is built |
| 2026-10-09 | The recipe ships as a skill, rendered from its specification; agent files are thin wrappers per product. The artifact types are skills and agent wrappers; processes and template sets leave the rules. | Owner. Fact: the skill format is the only one that all nine examined agent products read, and no standard exists for agents. |  |
| 2026-10-09 | An implementation skill holds knowledge and pointers, never copies: how to query the catalog of its product, how to identify trustworthy entries, lighthouse projects, how the product works, settings as a file from the current documentation, common traps, and the review tools that work with it. | Owner: forges maintain their own templates, and the software moves too fast to copy. |  |
| 2026-10-09 | The repository becomes a marketplace: one plugin per aspect and one per product set, under one version for the whole kit. | Owner. Fact: plugins switch on and off as a whole, and each installed skill costs context in every session. | a user must update for a change that did not touch them |
| 2026-10-09 | Items sit on three cumulative levels. A calculation of risk and reward decides admission, order and level of an item; the exposure of a project decides the level it aims for. The user picks a target level and declines single items with a reason. The selection is a Markdown checklist, committed in the project and simple to revisit. | Owner. This supersedes the scale strong, conditional, optional of the same day. | the calculation exists and was used once |
| 2026-10-09 | Admission: an established and authorized issuer enters by the fast lane (standards bodies and regulators, open foundations, a platform vendor on its own platform, peer-reviewed research and recognized books, recorded data sources marked as trusted). A smaller independent source is vetted with measured signals as a library is, and the owner confirms. No single source gates a recipe; the rule of one focal description is superseded. | Owner: one baseline had started to gate the rest. |  |
| 2026-10-09 | Gathering uses open search and open fetch. Readers are isolated: no shell, no credentials, no access to the repository. A second reader checks what a reader reports. | Owner: outdated information, context poisoning, phishing and social engineering. | a reader was steered by a page |
| 2026-10-09 | Superseded on the same day by the next row. Each specification keeps a short evidence record: per citation the quote of at most 40 words, its location and the date read. This amends the rule of 2026-10-08 that only references are kept. | Owner. Fact: checking the citations of this specification took about 2.4 million tokens of delegated reading. |  |
| 2026-10-09 | The evidence record holds, for each source, a summary of what it contributes, where in the source that is, the rows it supports and the date read. A quote stays only where the wording itself is the point. A second reader checks each line; no program confirms quotes. | Owner. A quote shows that words are present in a source, not that the source supports the item, and it is not knowledge that a later reader can use. | summaries drift from their sources at a refresh |
| 2026-10-09 | Level 1 holds the basic practices. How far a project goes past them follows from its risk on the risk dimensions of the aspect (for example operative, regulatory, commercial). Each aspect names its dimensions, and the recipe skill assesses them with the owner of the project. An item above level 1 names its dimension. This refines the decision on the three levels: exposure is one dimension of several. | Owner: the assessment differs by use case, project, stack and aspect; data safety has an operative side (reversible operations, backups), a regulatory side (personal data) and a commercial side (patent or other value). | the first aspect with real dimensions is distilled |
| 2026-10-09 | A practice of the state of the art answers a specific result of a risk analysis. A recipe skill leads the user through an educated and opinionated risk analysis of their software, their market, their context, their users and their data. Each item names the risk that it answers. | Owner. |  |
| 2026-10-09 | The main branch holds the machinery and the delivered skills only. Each specification stays on its own branch, with its evidence and its research records. A Spec Kit step is a pull request into that branch, and a delivery is a pull request into the main branch. The tooling of the factory is in the folder `factory/`. | Owner: a clean separation of research and delivered skills. | a recipe needs the specification of a different aspect |
| 2026-10-09 | Each skill that the factory makes writes to the person in the loop in ASD-STE100 Simplified Technical English. | Owner. |  |
| 2026-10-09 | The research skill is tooling of this repository, not a plugin. It gets its own product specification with user stories; the requirements that an earlier revision listed here move there. | Owner. | others ask to add aspects |
| 2026-10-09 | A recipe is proven by review, helper software by its tests. Measured proof on the reference case is not possible: its first commit already held most of its pipeline. | Owner; fact from the history of the reference project. |  |
| 2026-10-09 | Helper software is written in Python, not in a shell language; declarative tools are preferred. Helpers will require Python 3.11 or later, in a change of its own. | Owner. Fact: Python 3.9 reached end of life on 2025-10-31 and 3.10 on 2026-10-01. |  |
| 2026-10-09 | A declined item keeps its reason, and a refresh shows the declined items whose source changed. The owner starts a refresh and accepts a recipe; changes from outside arrive as pull requests. A paid source is cited from its official preview and marked as read in part. Lighthouse projects are chosen by measurable criteria, carry a date and are read again at a refresh. A skill that cannot reach its sources says what it could not verify. | Follows from the decisions above; the owner did not object. | |
| 2026-10-09 | The level of every item below is pending, and four items rest on independent sources whose vetting is pending, because the calculation and the vetting helper do not exist yet. | C-18, C-20. | the tooling is built |

## 8. Glossary

| Term | Meaning here | Other meanings in the sources |
|---|---|---|
| State of the art | global: the best practices that the industry has produced so far, recognized by experts and proven in practice | in one organization, the best of what it does today; the consolidated stage (ISO); the stage ahead of the accepted rules (Kalkar, TeleTrusT); in patent law, everything made public |
| Aspect | one major part of software engineering with its own recipe | knowledge area (SWEBOK); process (ISO/IEC/IEEE 12207); capability (DORA) |
| Item | one generic statement of a checklist | task (SSDF); control or requirement (OSPS Baseline); capability (DORA); practice |
| Check | a cheap, deterministic test of an item | review, audit |
| Read | the text of the source was read: full, part or no | verified, in the sense that a claim is true |
| Recipe | a strategy and a generic checklist for one aspect, shipped as a skill that is rendered from its specification | golden path, template |
| Level | 1, 2 or 3, cumulative; where the calculation of risk and reward places an item | maturity level by project size (OSPS Baseline); level of guarantees (SLSA); tier (Best Practices badge); strong and weak recommendation (GRADE) |
| Exposure | who depends on a project; it decides the level the project aims for | |
| Selection | the choice of one project: a target level for each risk dimension and the declined items, as a committed checklist | Current and Target Profile (NIST CSF); a baseline tailored from a catalog (OSCAL); exemption (scorecard products) |
| Fast lane | admission of an item without deep evaluation, because an established and authorized issuer states it | |
| Layer | one of the two kinds of specification: the aspect (layer one) and a set of implementation skills (layer two) | |
