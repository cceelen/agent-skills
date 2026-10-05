---
name: "library-vetting"
description: "Vet, evaluate or compare open source libraries and packages in any ecosystem (C/C++, Rust, Go, Python, npm, JVM, .NET, Ruby, PHP and more) for adoption or continued use. Asks for usage, use case, market and requirements first, scores 15 dimensions with a scripted rubric, and writes a report with a tier (ADOPT to AVOID), an overall score, guardrails, an exit or migration plan and a list of candidate alternatives to vet. When several libraries are compared, each gets a full independent vetting before any comparison is written. Use whenever the user asks to vet, assess, audit or compare a library or dependency, asks \"should we use X\" or \"is X safe/maintained/production-ready\", wants a dependency or supply-chain review, or is choosing between libraries, even without the word \"vetting\"."
---

# Library vetting (any ecosystem)

Produce an evidence-based adoption assessment of an open source library: C/C++, Rust, Go, Python,
JavaScript/TypeScript, JVM, .NET, Ruby, PHP, Elixir, Dart, Swift, or anything with a source
repository. Output: one Markdown report per library and a verdict of under ten lines in chat. The flow
is: ask for the frame, collect, judge, score, write. When several libraries are compared, every
one of them goes through that whole flow on its own first (see Comparing several libraries).

The design has one rule behind it: **scripts gather and compute, a small model reads and
extracts, the session model only judges and writes.**

- `collect.py` gathers every mechanical fact in one call (registry record, one shallow clone,
  git history, tree and CI scan, dependency screen, Scorecard, advisories) into `facts.json`.
  It also reads the release provenance from the CI files (known generators, identity token,
  self-hosted runners), and screens the base stack: each CI action, toolchain version and base
  image, with its pin, the latest release, known vulnerabilities in the version used, and the
  advisory history. If the helper programs `pipeline_check` or `plumber` are installed, it adds
  their findings; nothing depends on them.
  What the shell cannot reach it lists as a `fetch_plan` of exact URLs, so the web tool is used
  for those and nothing else.
- `score.py` answers about a third of the rubric from the facts alone and computes dimension
  scores, category results, the overall score, disqualifiers, the tier, and the report tables.
  The session model never does arithmetic and never picks a score or a tier by feel.

## Step 0. Locate the scripts

The scripts are in `scripts/` next to this file: `collect.py`, `score.py`, `models.py` and
`rubric.txt`. Set
`LV` to the absolute path of that directory (the folder this SKILL.md was loaded from, plus
`/scripts`) and check it with `ls "$LV"`. They need only `python3` and `git`. Work in
`vet/<library>/` under the working directory; every file named below lives there.

## Models and agents (set up one time)

The skill uses two roles. The **evidence** role reads and extracts, so it gets the smallest
capable model. The **vetter** role judges and writes, so it gets the model of the session. Model
names are different in each agent product. Thus `scripts/models.py` keeps a mapping for the
local installation.

1. Run `python3 $LV/models.py show`. If it prints a mapping, use it and go to Step 1.
2. If there is no mapping, run `python3 $LV/models.py detect`. It prints the host, the model
   settings that it found in the local configuration, and a proposed model for each role.
3. Show the proposal to the user together with the intake questions of Step 1. The user can
   accept it or give a different model name for a role. If the user is not there, accept the
   proposal.
4. Run `python3 $LV/models.py apply --evidence <model> --vetter <model>`. Add `--scope project`
   if the user wants the mapping only for this project. The command saves the mapping. On
   hosts that support agent files, it also writes the agents `library-evidence-collector` and
   `library-vetter` with the correct model and tool names.

How to start an agent for a role:

- If an agent with the name `library-evidence-collector` or `library-vetter` is available in
  this session, use it. A new agent file is usually available only after the host starts again.
- If it is not available, start a general subagent and select the model from the mapping. The
  value `inherit` means: do not select a model.
- If the host rejects the model, start the agent again without a model. Then run
  `models.py apply` with `inherit` for that role, and tell the user. If `models.py show` printed
  the scope `project`, add `--scope project`. If not, the project mapping continues to win.
- If the host cannot start subagents or cannot select a model, do the steps yourself. The
  scripts and the scores do not change.

## Step 1. Frame: ask before collecting (session model)

A verdict depends on who is asking. The same library can be AVOID for new untrusted-input use
and a managed risk where it already ships on trusted input. So the frame is established first,
from memory or from the user, never silently assumed.

Memory lives in `.claude/library-vetting/` in the working repo (also read a legacy
`.claude/cpp-vetting/` if present): `project-profile.md`, `orgs/<org>.md`, `peers.md`, and
`vetted/<library>.md` with `vetted/<library>.prior.yaml` and `vetted/<library>.ledger.md`. Read
memory first. If the working directory is a project repo with no profile, build one from its
manifests, CI config and LICENSE and tell the user what was recorded.

**Intake.** Every item below must come from the profile, from the user's request, or from the
user's answer. Ask for whatever is missing in ONE batch (a question tool if you have one, else
plain text), before running the collector. Offer concrete options so each answer is a click:

1. **Usage.** New adoption being considered / already in use (where, roughly how much code,
   which version or commit) / already decided to migrate away.
2. **Use case and data.** What the library does in the product and what reaches it: untrusted
   input (network, uploaded files), trusted or locally produced data, compile-time only, none.
3. **Product and market.** How the product ships (internal service, proprietary binary, open
   source, embedded device) and who it is sold to, where that brings a regime: regulated
   industry, public sector, CRA, export or sovereignty constraints.
4. **Requirements.** Language standard and toolchain, target platforms, performance or
   footprint needs, license constraints, anything the library must do that a replacement would
   also have to do.

If the user is not there to answer (scheduled or unattended run) or says "just proceed", continue
with assumptions, set `framed_by: "assumed"`, and the report carries "provisional: use case
assumed" on its tier. Never present an assumed frame as fact. Save answers to
`project-profile.md` so they are asked once.

Write `frame.json`. Closed choices, so two runs frame the library alike:

| Field | Values | Effect |
|---|---|---|
| `name`, `version`, `parent`, `prior` | text | report header; `version` is the one in use or to be adopted |
| `usage` | `new` / `existing` / `migrating` | under a disqualifier: `new` gives AVOID, the others REPLACE or OWN IT; decides whether the report has an Exit and migration section |
| `usage_detail`, `context`, `requirements` | one line each | header rows: where it is used, use case and market, requirements |
| `framed_by` | `profile` / `user` / `assumed` | `assumed` marks the result provisional |
| `reach` | `ships` / `build` / `dev` | `build` and `dev` make D2, D3, D4 n/a |
| `exposure` | `untrusted` / `trusted` / `compile_time` / `none` | `compile_time`: D2, D3 n/a. `none`: D2 n/a |
| `category` | `crypto` / `parser` / `buildtool` / `runtime` / `general` | fixed weight uplifts |
| `embedded`, `regulated`, `sovereign` | true / false | fixed uplifts |
| `regime` | text or absent | absent makes D11 n/a |
| `perf_required` | true / false | false makes D7 n/a |
| `candidates` | list of alternative libraries to vet | listed in the report, never recommended |
| `alternative_vetted` | `{name, tier, report}` or absent | the only way a replacement may be named as a recommendation |
| `mode` | `quick` / `deep` | `deep` enables the `[deep]` rubric lines |
| `guardrails` | list of library-specific guardrail labels | set in step 3; hygiene never counts |

Reach and exposure are judged from how the consumer uses the library, not from its README.

Modes. **Quick** (default): collector, clone reading, the web budget below. **Deep**: add a build
attempt, the ecosystem's own audit and analysis tools (`cargo audit`/`geiger`, `npm audit`,
`pip-audit`, `govulncheck`, `cppcheck`, a license scanner), and reproducing the published
artifact from the tag. Use deep when asked, or for crypto and untrusted-input parsers.

## Step 2. Evidence (delegate to the smallest model)

Spawn one evidence agent per library, as the section Models and agents specifies.
Candidates listed in a single-library report and dependencies never get an agent; libraries the
user asked to compare always do. If no subagent tool exists, do the same steps inline, in the
same order. Do not read source files, CI configs or fetched pages in the session model: that is
the agent's job, and its output is `answers.json` and `notes.md`, not a transcript.

The evidence prompt is the file `prompts/evidence.md` next to this file. Give the agent this
task and nothing more: "Read `<skill folder>/prompts/evidence.md` and do it. dir=`<dir>`,
LV=`<LV>`, target=`<target>`, name=`<name>`, mode=`<mode>`." Do not copy or shorten the prompt
into your own words.

**Usage inventory (only when `usage` is `existing` or `migrating` and the consumer repository
is available).** Start a second agent of the same kind with this task: "Read
`<skill folder>/prompts/usage-inventory.md` and do it. name=`<name>`, repo=`<consumer repo>`."
It writes `usage.md`. Without a consumer repository, the usage answer from intake stands and the
report says that the inventory was not possible.

### Web budget (hard caps, per library)

| Item | Quick | Deep |
|---|---|---|
| `fetch_plan` URLs (only what the shell could not reach) | at most 4 | at most 4 |
| Discretionary fetches and searches | 3 | 9 |
| Candidate index lookup | 1 | 1 |
| Dependency screening, candidate facts | 0 | 0 |
| Session model | 0, or 1 to resolve a tier-deciding unknown | 2 |

In a comparison every library has this budget in full; the budget is never shared or thinned.

Never fetch from the web what the clone contains (README, SECURITY.md, LICENSE, CI config,
changelog, manifests). When the budget is spent, remaining criteria stay `unknown` and appear in
Gaps; that is a correct result, not a failure. Reuse `facts.json` younger than 30 days and org
notes younger than 90 days instead of collecting again.

## Step 3. Judge (session model)

Read `facts.json` (it is small), `notes.md` and the `== J ==` list from
`score.py <dir> --todo`. Add to `answers.json` an answer for every J line and every disqualifier,
with `"by": "J"` and one line of evidence. This is the only place judgment enters, so apply
these rules the same way every time:

- **Answer the criterion as written.** A criterion that cannot be evidenced is `unknown`, never
  a charitable `yes`. `na` needs a reason that the criterion asks no question here.
- **Spot-check the agent.** Read the evidence strings in `answers.json`. Where a `yes` or `no`
  cites nothing checkable, or contradicts `facts.json`, set it to `unknown` or correct it. Check
  the CVE list at the top of `notes.md` against the D2 answers before anything else.
- **Overriding an automatic answer** is allowed only with evidence the scan could not see: a
  parent project that supplies the control (cite the parent's page), CI on a system the scan
  does not parse, or the finished-library allowance written into D1. The override is logged.
- **Parent projects.** If a foundation, umbrella or distribution performs review, release
  management, CI or disclosure for this library today, its mechanism counts as the library's.
  Record what it covers in `orgs/<org>.md`, including negative results, and reuse it.
- **Score the project, not the consumer.** Pinning, partial compilation, wrappers and the
  consumer's own tests never turn a `no` into a `yes`. They belong in guardrails and residual
  risk. Pinning defends against substitution, never against a project that ships no fixes.
- **Score the present.** A past incident counts only through what is still true today, and in
  one dimension, not four. One well-handled incident is not a track record: `D2.fix30` needs at
  least two advisories, otherwise answer `D2.fix90` at most.
- **Project failure or consumption failure.** A healthy project consumed at an abandoned version
  is `CAP.pin`, not a disqualifier.
- **Guardrails are library-specific or absent.** A named API to avoid, a backend to select, a
  feature to disable, a defect to work around. Pin, watch, review bumps: hygiene, never listed.
  Put the labels in `frame.json` `guardrails`; with none, the tier is plain ADOPT.

Ecosystem cues for the judgment lines (the evidence agent's notes follow the same list):

| Stack | D4 focus | Supply-chain focus (D6, D12, D13) |
|---|---|---|
| C, C++, Zig | ownership discipline, size arithmetic, fuzz coverage of parsers | vendored copies, submodule pins, signed tarball equals tag, ambient build discovery |
| Rust | `unsafe` blocks and their invariants, FFI, `miri` | `build.rs` and proc-macros run at build time, `cargo vet`/`deny`, trusted publishing |
| Go | `unsafe`, cgo, `go:linkname` | module proxy and sumdb, retractions, `govulncheck` |
| Python | `eval`, `pickle`, `yaml.load`, C extensions | sdist `setup.py` execution, wheels not built from the tag, trusted publishing, attestations |
| JS, TS | `eval`, prototype pollution, ReDoS, `child_process` | install scripts, publisher count and 2FA, npm provenance, lockfile, transitive count |
| JVM | deserialization, reflection, JNI, XXE defaults | signed Maven Central artifacts, shaded dependencies, reproducible builds |
| .NET | `unsafe`, `BinaryFormatter`, P/Invoke | signed packages, lock files, source link |
| Ruby, PHP | `eval`, `Marshal`/`unserialize`, shelling out | gem or Packagist publisher MFA, native extensions, install hooks |

## Step 4. Score

`python3 $LV/score.py <dir>` prints the tier, the overall score, category results and dimension
scores, and writes `scored.json`, the `report.md` skeleton, `prior.yaml` and
`evidence-ledger.md`. `PENDING` means a criterion has no answer: answer it. The mechanics, all in
the script: a dimension is 10 x earned / attainable points over its applicable lines, rounded,
then capped; `unknown` earns nothing and lowers confidence; `na` leaves the denominator.
Categories are good from 70%, moderate from 50%, poor below. The overall score is the weighted
sum, printed as "E of A attainable (scale S; n/a -w)"; it summarises and never decides. Tier: any
disqualifier gives AVOID for new use, and for existing use REPLACE (candidates exist) or OWN IT
(none do); two poor categories, or D poor on untrusted input, give LIMIT; one poor category needs
a guardrail that closes it or it is LIMIT; otherwise ADOPT, with guardrails if any are listed.

**SLSA levels.** The script also derives a level for three SLSA tracks from the same answers,
and prints them in the header, in the section SLSA levels and in `scored.json` (`slsa`). Build
(L0 to L3) and Source (L1 to L4) follow SLSA v1.2. Dependency (L0 to L3) follows the SLSA draft
and describes how the library controls its own dependencies: its packages and its base stack
(the toolchain and the CI actions). A library without packages is rated on the base stack alone. A level counts only when every
criterion of it and of each lower level is `yes`; `unknown` stops the level. The script answers
these criteria itself wherever the facts decide them; an agent answers only what `--todo` lists. The levels do not
change the score or the tier: the criteria behind them are already scored in D6 and D12. Never
state a level that the script did not print, and never call the Dependency level an approved
SLSA level.

The tier may be moved **one step** by setting `tier_override: {"tier", "reason"}` in
`frame.json` and re-running; the report prints both. If the scores themselves look wrong, the
fix is a criterion answer with evidence, never an edited number.

## Step 5. Report (session model fills the skeleton)

Copy `report.md` to `<library>-vetting-report.md` and replace every `<!-- FILL -->`. Leave the
script's tables, scores, tier and section order untouched. The order is fixed: header, Bottom
line, Findings at a glance, Key findings, Scorecards, SLSA levels, Recommendation, Dependency screening
(with the Base stack table),
Exit and migration (or Exit cost), Alternatives, Using it safely, Gaps, Assumptions, Evidence.

- **Findings at a glance** is the forward-pointing summary: one row per finding, worst first,
  with its dimension, severity and the guardrail, migration step or section that acts on it,
  linked. Every finding in Key findings has a row and every row has a finding.
- **Key findings**: only dimensions at 6 or below, surprising, or tier-driving. Each is a
  `### F<n>. <name> (D<x> <dimension>)` block with **Facts** (linked), **Risk**,
  **Recommendation**. For release integrity, say in plain words what an attacker could do and
  what the consumer cannot check.
- **Scorecard evidence cells**: one clause naming the deciding fact.
- **Exit and migration** is written for every existing use, whatever the tier: the usage
  inventory from `usage.md`, what a replacement must provide for that usage, effort and
  sequencing, and containment until then. For new use the section is Exit cost.
- **Evidence**: 10 to 20 rows a reader can audit, grouped, each naming what it shows. The full
  criterion ledger stays in `evidence-ledger.md` and is not pasted into the report.

**Alternatives are candidates, not recommendations.** Popularity is not evidence, and naming a
replacement that has not been through this rubric is the word-of-mouth this skill exists to
replace. Therefore, in a single-library report:

- Build the candidate list from `peers.md`, the user's own list, and one neutral index lookup
  by the evidence agent (the ecosystem's registry category or a packaging index such as
  Repology, vcpkg or conan-center), then save it to `peers.md`. Include every credible library
  in the space, up to 8, not the two best known. List alphabetically.
- For each candidate run `collect.py <target> --out <dir>/cand/<name>` (clone only, no agent,
  no web calls) and fill the Alternatives table from those facts alone. No ranking, no
  adjectives, no performance claims. This table is a list of what to vet, never a vetting.
- The Bottom line and Recommendation may name a replacement only when `alternative_vetted` is
  set, meaning a full report under this rubric and this frame exists in `vetted/`. Otherwise
  they say that candidates must be vetted first, and the chat reply offers to run a comparison
  (next section) of the candidates the user picks.

**Language: ASD-STE100 Simplified Technical English.** Write the report, the comparison file
and the chat reply in STE. Apply these rules to all text that you write. Do not change names,
quotations, code, commands or the script's tables.

- Use one word for one meaning, and the same term for the same thing in the whole report.
- Use simple verb tenses: present, past and future. Use the active voice. Name the actor.
- Do not use an -ing word as a verb or as a noun. Do not use contractions.
- Write instructions as commands. Give one instruction in each sentence.
- Put the condition before the instruction: "If the input is not trusted, set the depth limit."
- Keep a sentence that gives an instruction to 20 words or fewer, and other sentences to 25.
- Give one topic in each sentence, and no more than six sentences in each paragraph.
- Use articles (a, an, the). Do not make a noun cluster of more than three words.
- Do not omit words to make a sentence shorter. Use a vertical list for a long series.
- Use numbers and facts. Do not use words that give an opinion without a fact.

Length: 400 to 700 words of prose in quick mode, 1000 in deep; tables do not count. Give each
fact in one place. Every fact has a link or a `path:line`. A statement about a license is
analysis, not legal advice. Do not put YAML front matter in the report.

Then: copy the report, `prior.yaml` and `evidence-ledger.md` to `vetted/` in memory, save org
notes, and reply in chat with the tier, the overall score, the category results, the two or
three driving findings, the most important guardrail or migration step, and the file path. Do
not paste the report.

Re-vetting: if `prior.yaml` exists with the same `head`, the same rubric version and the same
frame, and is younger than 90 days, reuse it and report "unchanged". Otherwise put the old and
new tier, score and frame side by side in the Prior assessment row and explain every change of
tier by naming what changed: the facts, the frame, or the rubric.

## Comparing several libraries

When the user asks to compare, choose between, rank or vet several libraries, **every library
gets the complete vetting above, on its own, before anything is compared.** A comparison is the
last step over finished results. It is never a lighter procedure, and no library in it is
assessed from `--lite` facts, an Alternatives table, a peer table or prior knowledge. If the
budget does not allow full vettings for all of them, say so and ask which to drop; do not
thin the depth.

1. **One frame.** Do Step 1 once. All libraries share the use case, market, requirements,
   reach, exposure, category and mode; only `name`, `version` and `usage` differ (the incumbent
   is `existing`, the others `new`). If one library needs deep mode, all run deep.
2. **Reuse what is valid.** A library with a report in `vetted/` under the same rubric version,
   the same frame and the same `head`, younger than 90 days, is reused as it stands. Everything
   else is vetted fresh. List in the comparison which results were reused and from when.
3. **Vet each in isolation.** Each library is handled by its own subagents, which see the frame,
   the scripts and that library's `vet/<library>/` directory and nothing about the others:
   - the evidence agent of Step 2, one per library, all spawned in one message;
   - then one vetting agent per library (see Models and agents), all spawned in one message,
     with this task and nothing more: "Read `<skill folder>/prompts/vetter.md` and do it.
     skill=`<skill folder>`, dir=`<dir>`, LV=`<LV>`, name=`<name>`."
   The orchestrating session answers no criteria and opens no report until all are finished.
   Without a subagent tool, vet the libraries one after another, each to a finished report
   before the next starts, never revising a finished one in light of a later one, and say in
   the comparison that isolation was by procedure only.
4. **Gate.** Compare only when every library has a `scored.json` with a tier other than
   `PENDING`, the same rubric version, the same frame, and a report with no `FILL` left. The
   command in point 5 prints these checks. A library that fails the gate is finished, not
   compared around.
5. **Compare.** Write `<topic>-comparison.md` from the `scored.json` files and the finished
   reports only; no new research. Generate the tables with:

   ```bash
   python3 - vet/*/scored.json <<'PY'
   import json, sys
   rows = sorted((json.load(open(p)) for p in sys.argv[1:]), key=lambda s: str(s["library"]))
   print("| Library | Version | Tier | Overall | A Fit | B Health | C Security | D Supply chain | Disqualifiers |")
   print("|---|---|---|---|---|---|---|---|---|")
   for s in rows:
       c = s["categories"]
       print(f"| {s['library']} | {s['version']} | {s['tier']} | {s['overall_earned']:g} of {s['overall_attainable']} | "
             + " | ".join("n/a" if c[k]["pct"] is None else f"{c[k]['pct']}%" for k in "ABCD")
             + f" | {', '.join(s['disqualifiers']) or 'none'} |")
   print("\n| Dimension | " + " | ".join(str(s["library"]) for s in rows) + " |")
   print("|---|" + "---|" * len(rows))
   dims = rows[0]["dimensions"]
   for d in sorted(dims, key=lambda x: int(x[1:])):
       print(f"| {dims[d]['name']} ({d}) | " + " | ".join(
           str(s["dimensions"][d].get("score", s["dimensions"][d]["status"])) for s in rows) + " |")
   skip = ("name", "version", "usage", "usage_detail", "prior", "parent", "guardrails",
           "tier_override", "candidates", "alternative_vetted")
   print("\nframes equal:", len({json.dumps({k: v for k, v in s["frame"].items() if k not in skip},
         sort_keys=True) for s in rows}) == 1, "| rubrics:", sorted({s["rubric"] for s in rows}),
         "| pending:", [s["library"] for s in rows if s["tier"] == "PENDING"])
   PY
   ```

   The comparison file contains, in this order: the shared frame; the summary table; the
   dimension matrix; **What separates them**, covering only dimensions where scores differ by 3
   or more, each with the deciding evidence cited from the individual reports; **Fit against
   the requirements**, one line per stated requirement and library; then the recommendation.
   Because every library here is fully vetted, the comparison may recommend among them. Order
   by tier first, then disqualifiers, then requirement fit; the overall score breaks ties and
   never decides alone. Say so plainly when two libraries cannot be separated on the evidence.
6. **Scores are settled before the comparison.** The comparison changes no score and no tier.
   If it shows the same evidence answered differently in two reports, send that criterion back
   to both vetting agents, re-score, and note the correction in both reports and the
   comparison.
7. **Afterwards.** Save every report to `vetted/`, and record the comparison's outcome so later
   single-library runs can set `alternative_vetted`. A dependency of one compared library that
   is itself in the comparison is cited by its own report, not re-screened. If over half the
   libraries land on one tier, re-check the disqualifier answers and state why the spread is
   real.

## Why results repeat

- The frame is asked for and recorded, never guessed, so two runs judge the same use.
- Facts come from one script with fixed windows (90 days, 12 and 24 months), sorted output, and
  the assessed commit recorded.
- Every criterion gets an explicit `yes` / `no` / `unknown` / `na` with evidence; nothing is
  scored on impression, and unanswered criteria block the tier.
- Applicability, uplifts, caps, category results, the overall score and the tier are computed,
  not chosen.
- Search queries, probe order, dependency screening order and depth, candidate lists and web
  budgets are fixed.
- In a comparison each library is judged without sight of the others, so no result is pulled
  toward its neighbours.
- The rubric version is printed in every report; compare reports only within one version.

## Rubric

The scoring authority is `scripts/rubric.txt`, read by `score.py`; `score.py <dir> --todo` prints
the lines that still need an answer, so there is no need to read the whole file. Line format:
`id | points | who | text`. `who` is `A` (answered from facts by the script), `E` (evidence
agent) or `J` (session model). `~g` after an id marks an exclusive group where the highest `yes`
counts. Tags restrict a line: `[native]` memory-unsafe languages, `[managed]` all others,
`[registry]` registry packages, `[big]` not a small library (under 5000 lines with at most 2
dependencies), `[deep]` deep mode. `capN` caps the dimension at N when answered `yes`; `zero`
sets it to 0. Header lines give dimension, weight and category (A Fit, B Project health, C
Security and response, D Supply chain and rigor). D8 is computed from the Scorecard aggregate.
Change scoring only by editing those lines.
