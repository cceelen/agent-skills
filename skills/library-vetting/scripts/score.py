#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""library-vetting scorer. Same facts + same answers => same scores, tier and tables.

  score.py DIR            reads DIR/facts.json, DIR/frame.json, DIR/answers.json
                          writes DIR/scored.json, DIR/report.md (skeleton), DIR/prior.yaml,
                          DIR/evidence-ledger.md (every criterion answer; not part of the report)
  score.py DIR --todo     lists the criteria still unanswered, grouped by who answers them

rubric.txt beside this script (shipped in the library-vetting skill) is the single scoring
authority. Line format:
  id | points | who | text          who: A auto from facts, E evidence agent, J judge
Suffixes on id:  ~g  = exclusive group g (highest "yes" in the group counts)
Tags in text:    [native] [managed] [registry] [big] [deep] restrict when a line applies
Special points:  capN = cap the dimension at N when answered yes; zero = dimension is 0
"""

import json
import os
import re
import sys
from datetime import datetime, timezone

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "rubric.txt"), encoding="utf-8") as _f:
    RUBRIC = _f.read()
RUBRIC_VERSION = "library-vetting v1"
DQ = {  # disqualifiers, answered by J (yes/no). Any yes => REPLACE / OWN IT / AVOID
    "DQ.no_fix_supply": "A fix unreleased > 90 days, median fix time > 90 days, "
    "or no channel to learn a fix exists",
    "DQ.unfixed_vuln": "Publicly known unfixed vulnerability in code this consumer executes",
    "DQ.stale_backlog": "No release in 24 months AND open defect backlog or unanswered reports",
    "DQ.red_dep": "A Red required runtime dependency the consumer cannot route around",
    "DQ.license": "License incompatible with the consumer's distribution model",
    "DQ.compromised": "Unresolved malicious release, account takeover, or deprecated/archived upstream",
    "CAP.pin": "Consumer pins a version off any maintained line, or behind fixes its own use reaches "
    "(caps at LIMIT)",
}
NATIVE = {"c", "cpp", "zig", "objc"}
UPLIFT = {
    "crypto": {"D2": 4, "D3": 3, "D11": 4, "D4": 2},
    "parser": {"D4": 4, "D5": 3, "D2": 2},
    "buildtool": {"D10": 2, "D13": 4, "D1": 3},
    "runtime": {"D7": 3, "D15": 3},
    "embedded": {"D15": 2, "D7": 2},
    "regulated": {"D11": 3},
    "sovereign": {"D14": 3, "D12": 2},
}
SC_SUBSET = (
    "Maintained",
    "Code-Review",
    "Branch-Protection",
    "Dependency-Update-Tool",
    "License",
    "Binary-Artifacts",
    "Vulnerabilities",
)
PERMISSIVE_PATENT = (
    "Apache-2.0",
    "MPL-2.0",
    "GPL-3.0",
    "LGPL-3.0",
    "AGPL-3.0",
    "Unlicense",
    "CC0-1.0",
    "0BSD",
    "EPL-2.0",
)
OSI = re.compile(
    r"^(MIT|ISC|Zlib|BSL-1\.0|Unlicense|0BSD|Apache-2\.0|MPL-2\.0|EPL-[12]\.0|"
    r"BSD(-[23]-Clause)?|(L|A)?GPL(-[23]\.[01])?(-only|-or-later|\+)?|"
    r"Python-2\.0|PSF-2\.0|Artistic-2\.0|PostgreSQL|curl|OpenSSL|blessing)$",
    re.I,
)
COMPOUND = re.compile(r" (AND|OR|WITH) ")
SELF_HOSTED_CHECKS = {"GHA-012", "GL-014"}  # pipeline-check: self-hosted runner, not ephemeral
SAME_ANSWER = {"D4.fuzz_prop": "D4.fuzz_any", "D3.policy": "D2.policy"}  # criterion -> its source
# lines that ask no question if no advisory was ever published
NO_HISTORY_NA = ("D2.fix30", "D2.fix90", "D2.backports", "D2.credit")
TIER_ORDER = ["ADOPT", "ADOPT WITH GUARDRAILS", "LIMIT", "REPLACE"]
COLOURS = ("green", "yellow", "red")
COLOUR_WORDS = {"green": "good", "yellow": "moderate", "red": "poor"}
DOTS = {"green": "🟢", "yellow": "🟡", "red": "🔴", "n/a": "⚪"}
DEP_DOTS = {"Green": "🟢", "Amber": "🟡", "Red": "🔴", "unknown": "⚪"}
# SLSA track -> (specification, levels). A level is (name, requirements). A requirement is a
# tuple of criteria: one "yes" among them is sufficient. "fact:history" is true for a clone.
SLSA_TRACKS = {
    "Build": (
        "SLSA v1.2",
        (
            ("Provenance exists", (("D12.scripted",), ("D12.generated",))),
            ("Hosted build platform", (("D12.provenance",),)),
            ("Hardened builds", (("D12.isolated",),)),
        ),
    ),
    "Source": (
        "SLSA v1.2",
        (
            ("Version controlled", (("fact:history",),)),
            ("History and provenance", (("D12.source_attested",),)),
            ("Continuous technical controls", (("D12.protected",),)),
            ("Two-party review", (("D12.two_party",),)),
        ),
    ),
    # The dependencies of a library are its packages and its base stack: the toolchain and the
    # CI actions. Without packages, the D6 answers are yes and the base stack decides the level.
    "Dependency": (
        "SLSA draft, applied to the dependencies of the library",
        (
            ("Inventoried", (("D6.pinned", "D6.sbom"),)),
            (
                "Controlled",
                (
                    ("D6.pinned",),
                    ("D6.update_bot",),
                    ("D12.ci_hardened", "D13.hermetic"),
                    ("D6.stack_current",),
                ),
            ),
            ("Screened", (("D6.screened",), ("D13.toolchain", "D13.hermetic"), ("D6.stack_clean",))),
        ),
    ),
}
CATEGORY_NAMES = {
    "A": "Fit for our use",
    "B": "Project health",
    "C": "Security and response",
    "D": "Supply chain and rigor",
}


def pick_license(*sources):
    """The first source that gives an SPDX identifier or expression, else the first text.

    A registry field can hold free text and a host can answer NOASSERTION. Such a value must
    not hide an identifier that a later source gives."""
    texts = [x.strip() for x in sources if isinstance(x, str) and x.strip() and x.strip() != "NOASSERTION"]
    return next((x for x in texts if OSI.match(x) or COMPOUND.search(x)), texts[0] if texts else None)


def parse():
    dims, crit = {}, []
    for line in RUBRIC.strip().splitlines():
        p = [x.strip() for x in line.split("|")]
        if line.startswith("#"):
            d, name = p[0][2:].split(" ", 1)
            dims[d] = {"name": name, "weight": int(p[1]), "cat": p[2]}
        else:
            cid, grp = ([*p[0].split("~"), None])[:2]
            crit.append(
                {
                    "id": cid,
                    "dim": cid.split(".")[0],
                    "group": grp,
                    "pts": p[1],
                    "who": p[2],
                    "text": p[3],
                    "tags": set(re.findall(r"\[(\w+)\]", p[3])),
                }
            )
    return dims, crit


def ci_hardened(ci):
    """Answer for D12.ci_hardened. A CI system that has no actions gives no answer."""
    if not ci.get("count"):
        return None
    if ci.get("dangerous_triggers"):
        return "no"
    total = ci.get("actions_total") or 0
    if total:
        return "yes" if (ci.get("actions_sha_pinned") or 0) / total >= 0.8 else "no"
    return "yes" if any("/workflows/" in f for f in ci.get("files") or []) else None


# ---------- automatic answers from the facts ----------
def yn(v):
    return None if v is None else ("yes" if v else "no")


def at_most(v, n):
    return None if v is None else v <= n


def at_least(v, n):
    return None if v is None else v >= n


def chk_all(sc):
    return {k: v for k, v in (sc.get("checks") or {}).items() if isinstance(v, (int, float))}


def check_at_least(chk, name, n):
    """Answer from one Scorecard check. A check that did not run gives no answer."""
    return yn(chk[name] >= n) if chk.get(name, -1) >= 0 else None


def days_at_collection(iso, collected_at):
    """Age of a date in days at the time of the collection, so a later run scores the same."""

    def stamp(x):
        d = datetime.fromisoformat(str(x).replace("Z", "+00:00"))
        return d if d.tzinfo else d.replace(tzinfo=timezone.utc)

    try:
        return (stamp(collected_at) - stamp(iso)).days
    except ValueError:
        return None


def sections(F):
    """The sections of facts.json that the answers read. A missing section is empty."""
    t = F.get("tree") or {}
    return (
        F.get("history") or {},
        t,
        t.get("ci") or {},
        F.get("registry") or {},
        F.get("github") or {},
        F.get("depsdev_version") or {},
    )


def license_of(F):
    _, t, _, reg, gh, _ = sections(F)
    return pick_license(reg.get("license"), gh.get("license"), t.get("license_spdx_guess"))


def last_release_days(F, h, reg):
    reg_rel = days_at_collection((reg.get("last_releases") or [None])[-1], F.get("collected_at"))
    return min([x for x in (h.get("days_since_last_tag"), reg_rel) if x is not None], default=None)


def has_build_script(t, names):
    return any(f.split("/")[-1] in names for f in t.get("build_scripts", []))


def install_executes(t, reg):
    """True if the installation of the package runs code of the package."""
    return bool(
        reg.get("install_scripts")
        or t.get("npm_install_scripts")
        or has_build_script(t, ("build.rs", "binding.gyp"))
        or (
            reg.get("ecosystem") == "pypi"
            and reg.get("has_sdist")
            and "setup.py" in t.get("manifests", [])
            and "pyproject.toml" not in t.get("manifests", [])
        )
    )


def deps_pinned(t, reg):
    return bool(t.get("lockfiles") or t.get("submodules")) or (
        not t.get("manifest_runtime_deps") and not reg.get("runtime_deps") and not t.get("vendored_dirs")
    )


def health_answers(F, h, reg, gh, dv):
    busy = h.get("commits_24m", 0) >= 20
    return {
        "D1.commits": yn(at_most(h.get("days_since_last_commit"), 90)),
        "D1.release": yn(at_most(last_release_days(F, h, reg), 365)),
        "D1.bus3": yn(at_least(h.get("bus_factor_24m"), 3) and busy),
        "D1.bus5": yn(at_least(h.get("bus_factor_24m"), 5) and busy),
        "D1.releasers": yn(
            at_least(
                max(h.get("release_actors_24m") or 0, reg.get("publishers") or 0) if h or reg else None, 2
            )
        ),
        "D1.zero_dead": "yes"
        if (gh.get("archived") or reg.get("deprecated") or dv.get("deprecated"))
        else ("no" if at_most(h.get("days_since_last_commit"), 730) else None),
    }


def tree_answers(F, t, ci, reg):
    """Answers that need the file tree. Without a clone there is none."""
    if not t:
        return {}
    install_exec = install_executes(t, reg)
    A = {
        "D4.fuzz_any": yn(
            bool(ci.get("fuzzing") or t.get("fuzz_paths") or (F.get("depsdev_project") or {}).get("oss_fuzz"))
        ),
        "D5.standard": yn(bool(t.get("coding_standard"))),
        "D6.pinned": yn(deps_pinned(t, reg)),
        "D6.sbom": yn(bool(t.get("sbom_files") or ci.get("sbom"))),
        "D6.no_binaries": yn(not t.get("checked_in_binaries")),
        "D6.update_bot": yn(bool(t.get("update_bot"))),
        "D6.no_install_exec": yn(not install_exec),
        "D12.scripted": yn(bool(ci.get("count"))),
        "D13.locked": yn(bool(t.get("lockfiles"))),
        "D13.toolchain": yn(bool(t.get("toolchain_pins"))),
        "D13.declarative": yn(not install_exec and not has_build_script(t, ("configure.ac", "setup.py"))),
        "D13.hermetic": yn("bazel" in t.get("ecosystems", []) or "flake.nix" in t.get("toolchain_pins", [])),
    }
    if not t.get("risky_constructs"):  # with hits, E must read them
        A["D4.unsafe_surface"] = A["D4.dyn_exec"] = "yes"
    return A


def ci_answers(ci):
    """Answers that need the CI configuration. Without CI files there is none."""
    if not ci:
        return {}
    systems, archs = len(ci.get("os_matrix", [])), len(ci.get("arch_matrix", []))
    return {
        "D4.sanitizers": yn(ci.get("sanitizers")),
        "D5.tests_ci": yn(ci.get("tests")),
        "D6.ci_release": yn(ci.get("publish")),
        "D12.ci_hardened": ci_hardened(ci),
        "D13.floor": yn(ci.get("tests")),
        "D15.os3": yn(systems >= 3),
        "D15.os5": yn(systems >= 5),
        "D15.arch2": yn(archs >= 1),  # + default x86-64
        "D15.arch4": yn(archs >= 3),
    }


def plumber_answer(F, control):
    """Answer from one control of the helper program plumber, which reads the repository settings."""
    status = ((F.get("plumber") or {}).get("controls") or {}).get(control, {}).get("status")
    return {"passed": "yes", "failed": "no"}.get(status)


def self_hosted_runner(F, slsa):
    """True if a build can run on a machine of the maintainers: no proof of a hosted platform."""
    flagged = {
        check
        for r in (F.get("pipeline_check") or {}).values()
        for checks in r["failed_checks"].values()
        for check in checks
    }
    return bool(slsa.get("self_hosted") or flagged & SELF_HOSTED_CHECKS)


def provenance_answers(F, t, ci, reg, dv):
    """The SLSA criteria of D12 that the registry record and the CI text can answer."""
    attested = bool(reg.get("provenance") or dv.get("slsa_provenance") or dv.get("attestations"))
    if not t:
        return {"D12.generated": "yes", "D12.provenance": "yes"} if attested else {}
    slsa = ci.get("slsa") or {}  # empty for facts of a collector that did not read generators
    kind = slsa.get("strongest", "none")
    # a word like cosign in the CI text is a lead only: E reads the workflow
    lead = bool(ci.get("provenance")) or kind != "none"
    hosted = bool(slsa.get("oidc")) and not self_hosted_runner(F, slsa)
    generated = "yes" if attested or kind != "none" else None if lead else "no"
    A = {
        "D12.generated": generated,
        "D12.provenance": "yes"
        if attested or (kind in ("signed", "isolated") and hosted)
        else None
        if lead
        else "no",
        "D12.isolated": "yes" if kind == "isolated" and hosted else "no" if generated == "no" else None,
        "D12.verifiable": "yes" if t.get("verification_docs") else None,
    }
    if "slsa" in ci:
        A["D12.source_attested"] = yn(slsa["source_attestation"])
    elif ci.get("provenance") and not attested:  # earlier facts: a CI step counted as provenance
        A["D12.generated"] = "yes"
    return A


def cross_source_answers(F, t, ci, reg, dv, chk):
    """Answers that one of several sources can give."""
    return {
        "D2.channel": "yes" if F.get("github_private_reports") is True else None,
        "D2.policy": "yes" if t.get("security_policy") or (chk.get("Security-Policy") or 0) >= 5 else None,
        "D5.sast_ci": "yes" if ci.get("sast") or (chk.get("SAST") or 0) >= 7 else "no" if ci else None,
        "D5.review": check_at_least(chk, "Code-Review", 7),
        "D12.protected": check_at_least(chk, "Branch-Protection", 5)
        or plumber_answer(F, "branchMustBeProtected"),
        "D12.two_party": check_at_least(chk, "Code-Review", 8)
        or plumber_answer(F, "mrApprovalRulesMustRequireMinimumNumberOfApprovals"),
        "D13.packaging": yn(bool(reg or t.get("manifests"))) if (t or reg) else None,
    }


def license_answers(lic, t):
    if not lic:
        return {}
    one = not COMPOUND.search(lic) and len(t.get("licenses_named_in_root_file") or []) <= 1
    return {
        "D10.osi": yn(bool(OSI.match(lic))) if one else None,
        "D10.patent": yn(any(lic.startswith(p) for p in PERMISSIVE_PATENT)),
    }


def no_dependencies(t, reg):
    """True if the clone shows that the library has no dependency of any kind."""
    return bool(t) and not (
        reg.get("runtime_deps")
        or t.get("manifest_runtime_deps")
        or t.get("vendored_dirs")
        or t.get("submodules")
    )


def dep_screen_answers(F, t, reg):
    status = [r["status"] for r in (F.get("dep_screen") or {}).get("rows", [])]
    if F.get("dep_screen") is not None and "unknown" not in status:
        return {
            "D6.screened": yn(all(x == "Green" for x in status)),
            "D6.cap_red": yn("Red" in status),
            "D6.cap_amber": yn("Amber" in status),
        }
    if no_dependencies(t, reg):
        return {"D6.screened": "yes", "D6.cap_red": "no", "D6.cap_amber": "no"}
    return {}


def base_stack_answers(F):
    """Answers from the screen of the CI actions, the toolchain and the base images."""
    rows = (F.get("base_stack") or {}).get("rows", [])
    if not rows or any(r["status"] == "unknown" for r in rows):
        return {}  # nothing to rate, or a lookup did not work: E reads the files
    issues = {i for r in rows for i in r["issues"]}
    return {
        "D6.stack_current": yn(not issues & {"outdated", "floating reference", "end of life"}),
        "D6.stack_clean": yn("vulnerable" not in issues),
    }


def auto(F):
    """Deterministic answers from facts. A criterion without an answer stays for E."""
    h, t, ci, reg, gh, dv = sections(F)
    A = {
        **health_answers(F, h, reg, gh, dv),
        **tree_answers(F, t, ci, reg),
        **ci_answers(ci),
        **cross_source_answers(F, t, ci, reg, dv, chk_all(F.get("scorecard") or {})),
        **provenance_answers(F, t, ci, reg, dv),
        **license_answers(license_of(F), t),
        **dep_screen_answers(F, t, reg),
        **base_stack_answers(F),
    }
    for alias, source in SAME_ANSWER.items():
        A[alias] = A.get(source)
    return {k: v for k, v in A.items() if v is not None}


# ---------- frame ----------
def reach(frame):
    return frame.get("reach", "ships")


def exposure(frame):
    return frame.get("exposure", "untrusted")


def usage_of(frame):
    return frame.get("usage") or ("existing" if frame.get("already_dependency") else "new")


def applicable_dims(frame):
    na = {}
    if reach(frame) in ("dev", "build"):
        for d in ("D2", "D3", "D4"):
            na[d] = f"{reach(frame)}-time only: no runtime attack surface"
    elif exposure(frame) == "compile_time":
        na["D2"] = na["D3"] = "compile-time only: no runtime data"
    elif exposure(frame) == "none":
        na["D2"] = "no external data reaches it"
    if not frame.get("regime"):
        na["D11"] = "no compliance regime stated"
    if not frame.get("perf_required"):
        na["D7"] = "no performance requirement for this use"
    return na


def context(F, frame):
    """The language, and the tags that decide if a criterion applies."""
    t, reg = F.get("tree") or {}, F.get("registry") or {}
    lang = frame.get("language") or t.get("primary_language")
    ndeps = len(reg.get("runtime_deps") or t.get("manifest_runtime_deps") or [])
    big = (
        not (0 < (t.get("first_party_sloc") or 0) < 5000 and ndeps <= 2)
        if "small" not in frame
        else not frame["small"]
    )
    return lang, {
        "native": lang in NATIVE,
        "managed": lang not in NATIVE,
        "registry": bool(reg),
        "big": big,
        "deep": frame.get("mode") == "deep",
    }


def uplifts(frame):
    """The weight that the category and the flags of the frame add to a dimension."""
    up = {}
    for key in [frame.get("category")] + [k for k in ("embedded", "regulated", "sovereign") if frame.get(k)]:
        for dd, w in UPLIFT.get(key, {}).items():
            up[dd] = up.get(dd, 0) + w
    return up


# ---------- answers ----------
def load(d, name):
    try:
        with open(os.path.join(d, name), encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save(d, name, text):
    with open(os.path.join(d, name), "w", encoding="utf-8") as f:
        f.write(text)


def said_yes(answers, key):
    return answers.get(key, {}).get("a") == "yes"


def check_answers(given):
    bad = sorted(
        k
        for k, v in given.items()
        if not k.startswith("_")
        and (not isinstance(v, dict) or v.get("a") not in ("yes", "no", "unknown", "na"))
    )
    if bad:
        sys.exit("answers.json: answer must be yes/no/unknown/na for: " + ", ".join(bad))


def apply_corrections(F, given):
    if given.get("_scorecard"):  # E pasted the fetch_plan result: {"score":..,"date":..,"checks":{..}}
        F["scorecard"] = given["_scorecard"]
    for k, v in (given.get("_facts") or {}).items():  # E corrections to facts, for example
        if isinstance(v, dict) and isinstance(F.get(k), dict):  # {"github": {"archived": true}}
            F[k] = {**F[k], **v}  # a correction of one key keeps the other keys of the section
        else:
            F[k] = v


def merge_answers(crit, given, A):
    """An explicit answer beats an automatic answer."""
    ans = {}
    for c in crit:
        g = given.get(c["id"])
        if g:
            ans[c["id"]] = {
                "a": g["a"],
                "ev": g.get("ev", ""),
                "by": g.get("by", c["who"]),
                "overrode_auto": c["id"] in A and A[c["id"]] != g["a"],
            }
        elif c["id"] in A:
            ans[c["id"]] = {"a": A[c["id"]], "ev": "facts.json", "by": "A"}
    return ans


def print_todo(live, ans, given):
    for who in "EJ":
        print(f"== {who} ==")
        for c in live:
            if c["id"] not in ans and (c["who"] == who or (who == "E" and c["who"] == "A")):
                print(f"{c['id']} | {c['pts']} | {c['text']}")
    print("== J: disqualifiers ==")
    for k, v in DQ.items():
        if k not in given:
            print(f"{k} | {v}")


# ---------- scores ----------
def band(value, high, low, names):
    return names[0] if value >= high else names[1] if value >= low else names[2]


def scorecard_row(sc, frame):
    """D8 is the Scorecard aggregate. A use at build time takes the mean of the checks that apply."""
    if sc.get("score") is None:
        return {"status": "n/m", "note": "Scorecard not retrieved"}
    aggregate = f"aggregate {sc['score']} ({str(sc.get('date'))[:10]})"
    if reach(frame) in ("dev", "build") or exposure(frame) == "compile_time":
        checks = {k: v for k, v in chk_all(sc).items() if v >= 0}
        sub = [checks[k] for k in SC_SUBSET if k in checks]
        return {
            "status": "scored",
            "score": round(sum(sub) / len(sub)) if sub else 0,
            "conf": "High",
            "note": f"applicable-subset mean of {len(sub)} checks; {aggregate}",
        }
    return {"status": "scored", "score": int(sc["score"] + 0.5), "conf": "High", "note": aggregate}


def set_aside(ans):
    """The D2 lines that ask no question, because no advisory was ever published.

    A silent fix shows that there was a defect to publish. Then the line for advisories counts."""
    if not said_yes(ans, "D2.no_history"):
        return ()
    silent_fix = ans.get("D2.no_silent", {}).get("a") == "no"
    return NO_HISTORY_NA if silent_fix else (*NO_HISTORY_NA, "D2.advisories")


def tally(dd, criteria, ans, not_applicable):
    """Add up the criteria of one dimension. In an exclusive group, the highest yes counts."""
    earned = mx = known = total = 0
    caps, zero, groups, missing = [], False, {}, []
    for c in criteria:
        a = ans.get(c["id"], {}).get("a", "unknown")
        if c["id"] in not_applicable:
            a = "na"
        if c["pts"] == "zero" or c["pts"].startswith("cap"):
            if a == "yes" and c["pts"] == "zero":
                zero = True
            elif a == "yes":
                caps.append(int(c["pts"][3:]))
            continue
        if a == "na":
            continue
        p = int(c["pts"])
        if c["group"]:
            g = groups.setdefault(c["group"], {"max": 0, "got": 0, "known": False})
            g["max"] = max(g["max"], p)
            g["got"] = max(g["got"], p if a == "yes" else 0)
            g["known"] |= a in ("yes", "no")
        else:
            mx += p
            total += 1
            earned += p if a == "yes" else 0
            known += a in ("yes", "no")
            if a == "unknown":
                missing.append(c["id"])
    for name, g in groups.items():
        mx += g["max"]
        earned += g["got"]
        total += 1
        known += g["known"]
        if not g["known"]:
            missing.append(f"{dd}.~{name}")
    return {
        "earned": earned,
        "max": mx,
        "known": known,
        "total": total,
        "caps": caps,
        "zero": zero,
        "missing": missing,
    }


def criteria_row(dd, t):
    mx = 10 if dd == "D11" else t["max"]
    if dd == "D7" and t["known"] == 0:
        return {"status": "n/m", "note": "no performance evidence gathered"}
    if mx == 0:
        return {"status": "n/a", "note": "no applicable criteria"}
    share = t["known"] / t["total"] if t["total"] else 0
    return {
        "status": "scored",
        "raw": f"{t['earned']}/{mx}",
        "caps": t["caps"],
        "zero": t["zero"],
        "score": 0 if t["zero"] else min([int(10 * t["earned"] / mx + 0.5)] + t["caps"]),
        "unknown": t["missing"],
        "conf": band(share, 0.8, 0.5, ("High", "Med", "Low")),
    }


def score_dimensions(dims, live, ans, sc, frame, na_dims, up):
    not_applicable = set_aside(ans)
    out = {}
    for dd, meta in dims.items():
        row = {
            "id": dd,
            "name": meta["name"],
            "cat": meta["cat"],
            "weight": meta["weight"] + up.get(dd, 0),
            "uplift": up.get(dd, 0),
        }
        if dd in na_dims:
            row.update(status="n/a", note=na_dims[dd])
        elif dd == "D8":
            row.update(scorecard_row(sc, frame))
        else:
            row.update(criteria_row(dd, tally(dd, [c for c in live if c["dim"] == dd], ans, not_applicable)))
        if row["status"] == "scored":
            row["colour"] = band(row["score"], 8, 5, COLOURS)
        out[dd] = row
    return out


def category_totals(out):
    cats = {}
    for row in out.values():
        c = cats.setdefault(row["cat"], {"earned": 0.0, "attainable": 0, "pending": 0})
        if row["status"] == "scored":
            c["earned"] += row["score"] / 10 * row["weight"]
            c["attainable"] += row["weight"]
        elif row["status"] == "n/m":
            c["pending"] += row["weight"]
    for c in cats.values():
        c["earned"] = round(c["earned"], 1)
        c["pct"] = round(100 * c["earned"] / c["attainable"]) if c["attainable"] else None
        c["colour"] = "n/a" if c["pct"] is None else band(c["pct"], 70, 50, COLOURS)
    return cats


def overall_score(out, cats):
    """The overall line of the report, the points earned and the points attainable."""
    scale = sum(r["weight"] for r in out.values())
    earned = round(sum(c["earned"] for c in cats.values()), 1)
    attainable = sum(c["attainable"] for c in cats.values())
    pending = sum(c["pending"] for c in cats.values())
    text = (
        f"{earned:g} of {attainable} attainable (scale {scale}; n/a -{scale - attainable - pending}"
        + (f"; {pending} pending" if pending else "")
        + ")"
    )
    return text, earned, attainable


# ---------- SLSA levels ----------
def slsa_track(track, ans):
    """The highest level of which each requirement has a yes, and what stops the next level."""
    spec, levels = SLSA_TRACKS[track]
    level, stops = 0, []
    for _, requirements in levels:
        stops = [
            {"criteria": list(r), "answers": [ans.get(c, "unknown") for c in r]}
            for r in requirements
            if not any(ans.get(c) == "yes" for c in r)
        ]
        if stops:
            break
        level += 1
    return {
        "track": track,
        "specification": spec,
        "level": level,
        "name": levels[level - 1][0] if level else "",
        "stops_next_level": stops,
    }


def slsa_levels(F, ans):
    """The SLSA level for each track, from the same answers as the scores."""
    t, reg = F.get("tree") or {}, F.get("registry") or {}
    known = {cid: a["a"] for cid, a in ans.items()}
    known["fact:history"] = "yes" if F.get("history") else "unknown"
    tracks = [slsa_track(track, known) for track in SLSA_TRACKS]
    tracks[-1]["base_stack_only"] = no_dependencies(t, reg)
    return tracks


def slsa_text(tracks):
    return ", ".join(f"{x['track']} L{x['level']}" for x in tracks)


# ---------- tier: mechanical ----------
def disqualifiers(given, cats, out, frame):
    dq = [k for k in DQ if k.startswith("DQ.") and said_yes(given, k)]
    if (
        cats.get("C", {}).get("colour") == "red"
        and exposure(frame) == "untrusted"
        and reach(frame) == "ships"
    ):
        dq.append("DQ.security_red_on_untrusted_input")
    zeroed = [dd for dd, row in out.items() if row.get("zero")]
    if zeroed:
        dq.append("DQ.zero_dimension:" + ",".join(zeroed))
    return dq


def computed_tier(dq, reds, frame, given, todo):
    if todo:  # every criterion needs an explicit yes/no/unknown/na before a tier exists
        return "PENDING"
    guardrails = frame.get("guardrails", [])  # library-specific only; hygiene never counts
    if dq:
        replaceable = frame.get("alternative_vetted") or frame.get("candidates") or frame.get("alternative")
        return "AVOID" if usage_of(frame) == "new" else "REPLACE" if replaceable else "OWN IT"
    if len(reds) >= 2 or ("D" in reds and exposure(frame) == "untrusted"):
        return "LIMIT"
    if len(reds) == 1 and not guardrails:
        return "LIMIT"
    if said_yes(given, "CAP.pin"):  # a pin off the maintained line caps the tier
        return "LIMIT"
    return "ADOPT WITH GUARDRAILS" if guardrails else "ADOPT"


def overridden(tier, override):
    """The frame can move the tier one step, and only with a reason: {"tier":..., "reason":...}."""
    if (
        override
        and override.get("reason")
        and tier in TIER_ORDER
        and override.get("tier") in TIER_ORDER
        and abs(TIER_ORDER.index(tier) - TIER_ORDER.index(override["tier"])) == 1
    ):
        return override["tier"]
    return tier


def summarize(F, frame, lang, ctx, ans, given, todo, out, cats):
    """The content of scored.json."""
    reg, h = F.get("registry") or {}, F.get("history") or {}
    dq = disqualifiers(given, cats, out, frame)
    dq_open = [k for k in DQ if k not in given]
    reds = sorted(k for k, c in cats.items() if c["colour"] == "red")
    computed = computed_tier(dq, reds, frame, given, todo)
    overall, earned, attainable = overall_score(out, cats)
    framed = frame.get("framed_by", "assumed")
    return {
        "library": frame.get("name") or reg.get("name") or F.get("target"),
        "version": frame.get("version") or reg.get("version") or h.get("head", "")[:12],
        "assessed": str(F.get("collected_at"))[:10],
        "rubric": RUBRIC_VERSION,
        "mode": frame.get("mode", "quick"),
        "language": lang,
        "license": license_of(F),
        "context": ctx,
        "frame": frame,
        "usage": usage_of(frame),
        "framed_by": framed,
        "dimensions": out,
        "categories": cats,
        "overall": overall,
        "overall_earned": earned,
        "overall_attainable": attainable,
        "disqualifiers": dq,
        "disqualifiers_unanswered": dq_open,
        "unanswered": todo,
        "red_categories": reds,
        "tier_computed": computed,
        "slsa": slsa_levels(F, ans),
        "tier": overridden(computed, frame.get("tier_override")),
        "provisional": any(r["status"] == "n/m" for r in out.values())
        or bool(dq_open)
        or framed == "assumed",
        "answers": ans,
    }


# ---------- report skeleton ----------
def fill(text=""):
    """A place in the report that the judge fills in."""
    return f"<!-- FILL: {text} -->" if text else "<!-- FILL -->"


def day(x):
    return str(x)[:10]


def tier_line(S):
    return S["tier"] + (
        " (provisional: the use case is an assumption)" if S["framed_by"] == "assumed" else ""
    )


def header_lines(S, F):
    frame, h = S["frame"], F.get("history") or {}
    t, reg = F.get("tree") or {}, F.get("registry") or {}
    assumed = (
        " (there is no profile and there are no answers; each frame field is an assumption)"
        if S["framed_by"] == "assumed"
        else ""
    )
    usage_detail = frame.get("usage_detail", fill("where and how it is used, call sites, version pinned"))
    requirements = frame.get("requirements", fill("toolchain, targets, performance, compliance"))
    return [
        f"# Vetting report: {S['library']}",
        "",
        "| | |",
        "|---|---|",
        f"| Repo | {F.get('repo')} |",
        f"| Version assessed | {S['version']} (HEAD {h.get('head', '')[:10]}, authored "
        f"{day(h.get('last_commit_authored'))}, committed {day(h.get('last_commit'))}) |",
        f"| Assessed | {S['assessed']}, {S['mode']} mode, {S['rubric']} |",
        f"| Ecosystem | {reg.get('ecosystem') or ', '.join(t.get('ecosystems', [])) or '?'}"
        f" / {S['language']} |",
        f"| Our usage | {S['usage']}: {usage_detail} |",
        f"| Use case and market | {frame.get('context', fill())} |",
        f"| Requirements | {requirements} |",
        f"| Frame source | {S['framed_by']}{assumed} |",
        f"| Dependency class | reach: {reach(frame)}; data exposure: {exposure(frame)} |",
        f"| Parent project | {frame.get('parent', 'none')} |",
        f"| Prior assessment | {frame.get('prior', 'first assessment')} |",
        f"| SLSA levels | {slsa_text(S['slsa'])} |",
        f"| Result | **{tier_line(S)}**, {S['overall']} |",
        "",
    ]


def findings_lines():
    return [
        "## Bottom line",
        "",
        fill(
            "one or two bold sentences with the decision. Name a replacement only if it has "
            "its own vetting report; otherwise say candidates must be vetted first"
        ),
        "",
        "## Findings at a glance",
        "",
        "| # | Finding | Dimension | Severity | Leads to |",
        "|---|---|---|---|---|",
        fill(
            "one row per finding, worst first. Severity: tier-driving / high / medium / note. "
            "'Leads to' names the guardrail (G1), migration step, or section that acts on it, "
            "as a link to that heading"
        ),
        "",
        "## Key findings",
        "",
        fill(
            "one '### F<n>. <name> (D<x> <dimension name>)' block per row above, with "
            "**Facts** (linked), **Risk**, **Recommendation**"
        ),
        "",
    ]


def category_heading(k, c):
    pending = f", {c['pending']} pending" if c["pending"] else ""
    if c["pct"] is None:
        return f"### {k}. {CATEGORY_NAMES[k]}: " + (
            f"not measured, {c['pending']} pending"
            if c["pending"]
            else "not applicable to this dependency class"
        )
    return (
        f"### {k}. {CATEGORY_NAMES[k]}: {c['earned']:g} of {c['attainable']} attainable"
        f" ({c['pct']}%, {COLOUR_WORDS[c['colour']]}){pending}"
    )


def dimension_line(dd, r):
    if r["status"] != "scored":
        return f"| ⚪ | {r['name']} ({dd}) | {r['weight']} | {r['status']} | | {r['note']} |"
    note = r.get("note") or (fill() + (f" (capped at {min(r['caps'])})" if r.get("caps") else ""))
    return (
        f"| {DOTS[r['colour']]} | {r['name']} ({dd}) | {r['weight']} | {r['score']} | {r['conf']} | {note} |"
    )


def scorecard_lines(S, up):
    uplift = " Weight uplifts: " + ", ".join(f"{k} +{v}" for k, v in sorted(up.items())) + "." if up else ""
    L = ["## Scorecards", "", f"Overall: **{S['overall']}**.{uplift}", ""]
    for k in "ABCD":
        c = S["categories"][k]
        L += [category_heading(k, c), ""]
        if c["pct"] is None and not c["pending"]:
            continue
        L += ["| | Dimension | Weight | Score | Conf. | Key evidence |", "|---|---|---|---|---|---|"]
        L += [dimension_line(dd, r) for dd, r in S["dimensions"].items() if r["cat"] == k]
        L.append("")
    return L


def helper_lines(F):
    """What the optional helper programs found. They are evidence; they do not set a level."""
    L = []
    for ci, r in sorted((F.get("pipeline_check") or {}).items()):
        failed = (
            "; ".join(f"{control}: {', '.join(checks)}" for control, checks in r["failed_checks"].items())
            or "none"
        )
        L.append(
            f"- pipeline-check {r['version']} on the {ci} files: grade {r['grade']} "
            f"({r['score']}). Failed checks for each control: {failed}."
        )
    plumber = F.get("plumber")
    if plumber:
        failed = sorted(k for k, c in plumber["controls"].items() if c["status"] == "failed")
        L.append(
            f"- plumber: score {plumber['score']}. Failed controls: " + (", ".join(failed) or "none") + "."
        )
    return [*L, ""] if L else []


def slsa_lines(S, F, crit):
    text = {c["id"]: re.sub(r"\[\w+\]\s*", "", c["text"]).split(" (")[0] for c in crit}
    text["fact:history"] = "The source is in a version control system"
    L = [
        "## SLSA levels",
        "",
        "A track has a level only if each criterion of that level has the answer `yes`. The "
        "Dependency track is a draft of SLSA. Here it shows how the library controls its own "
        "dependencies: its packages and its base stack.",
        "",
        "| Track | Level | Specification | The next level needs |",
        "|---|---|---|---|",
    ]
    for x in S["slsa"]:
        needs = "; ".join(
            " or ".join(f"{text.get(c, c)} ({a})" for c, a in zip(stop["criteria"], stop["answers"]))
            for stop in x["stops_next_level"]
        )
        level = f"L{x['level']} {x['name']}".strip()
        L.append(f"| {x['track']} | {level} | {x['specification']} | {needs or 'nothing more'} |")
    if S["slsa"][-1]["base_stack_only"]:
        L += [
            "",
            "The library has no packages as dependencies. Thus the Dependency level shows "
            "only its base stack: the toolchain and the CI actions.",
        ]
    return [*L, "", *helper_lines(F)]


def dep_table(F):
    ds = F.get("dep_screen")
    if not ds:
        return [
            fill(
                "no registry dependency list. Table from notes.md: | | Dependency | Role | "
                "Reach | Version policy | Key risk |, or 'no required runtime dependencies'"
            )
        ]
    L = [
        f"Depth: {ds['depth']}.",
        "",
        "| | Dependency | Version | Last release | License | Note |",
        "|---|---|---|---|---|---|",
    ]
    for r in ds["rows"]:
        age = r.get("last_release_days")
        L.append(
            f"| {DEP_DOTS[r['status']]} | {r['name']} | {r.get('version', '')} | "
            f"{'' if age is None else str(round(age / 30.4)) + ' months ago'} | "
            f"{r.get('license') or ''} | {r.get('why', '')} |"
        )
    return L


def base_stack_table(F):
    stack = F.get("base_stack")
    if not stack or not stack["rows"]:
        return [
            fill(
                "the collector did not screen the base stack. Table from notes.md: | | Component "
                "| Kind | Version | Pin | Latest | Note |"
            )
        ]
    L = [
        f"Depth: {stack['depth']}.",
        "",
        "| | Component | Kind | Version | Pin | Latest | Note |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in stack["rows"]:
        L.append(
            f"| {DEP_DOTS.get(r['status'], '⚪')} | {r['name']} | {r['kind']} | "
            f"{r.get('version') or r['ref']} | {r['pin']} | {r.get('latest') or ''} "
            f"| {r.get('why', '')} |"
        )
    return L


def recommendation_lines(S, F):
    moved = (
        f" (computed {S['tier_computed']}; moved one tier: {S['frame']['tier_override']['reason']})"
        if S["tier"] != S["tier_computed"]
        else ""
    )
    return [
        "## Recommendation",
        "",
        f"**Recommended: {tier_line(S)}**, score **{S['overall']}**{moved}",
        "",
        "Disqualifiers: " + (", ".join(S["disqualifiers"]) or "none") + ".",
        "",
        fill(
            "one imperative sentence (what to do Monday); 2-4 sentences on the driving "
            "findings, by F-number; **Replaceable?** one line; **Worth it?** one line; then "
            "the guardrail table (Guardrail | Action | Mitigates | Cost | Verify by), "
            "library-specific guardrails only"
        ),
        "",
        "## Dependency screening",
        "",
        *dep_table(F),
        "",
        "### Base stack",
        "",
        *base_stack_table(F),
        "",
    ]


def exit_lines(usage):
    if usage == "new":
        return [
            "## Exit cost",
            "",
            fill(
                "what leaving this library later would cost: API surface we would bind to, "
                "data formats, wrap-or-not advice"
            ),
            "",
        ]
    return [
        "## Exit and migration",
        "",
        fill(
            "(1) usage inventory from the consumer repo: files, call sites, API surface used, "
            "pinned version; (2) what a replacement must provide for that usage; (3) migration "
            "effort and sequencing; (4) containment until then. Written for every existing "
            "use, whatever the tier"
        ),
        "",
    ]


def alternatives_lines(S):
    alt = S["frame"].get("alternative_vetted") or {}
    vetted = (
        f"Vetted alternative: **{alt.get('name')}**, {alt.get('tier')} under "
        f"{alt.get('rubric', S['rubric'])} ({alt.get('report', 'report in memory')})."
        if alt
        else "No alternative has a vetting report for this rubric. Thus **this report does "
        "not recommend an alternative**. The table shows the candidates that you can vet."
    )
    return [
        "## Alternatives",
        "",
        vetted,
        "",
        "| Candidate | License | Last release | Commits 12 mo | Bus factor 24 mo "
        "| Security policy | Vetted? |",
        "|---|---|---|---|---|---|---|",
        fill(
            "one row per candidate in frame.json 'candidates', alphabetical, figures from "
            "collect.py only. No ranking, no adjectives. Then one line: which candidates to "
            "vet next and why that is the user's call"
        ),
        "",
    ]


def safe_use_lines():
    return [
        "## Using it safely",
        "",
        "### Baseline hygiene",
        "",
        fill("one line"),
        "",
        "### Architecture guidance",
        "",
        fill("wrap or use directly; where the seam goes"),
        "",
        "### Residual risk statement (drafted for sign-off)",
        "",
        fill("what remains after guardrails, monitoring feeds, re-evaluation triggers"),
        "",
    ]


def gap_lines(out, crit):
    text = {c["id"]: re.sub(r"\[\w+\]\s*", "", c["text"]) for c in crit}
    text.update({f"{c['dim']}.~{c['group']}": text[c["id"]] for c in reversed(crit) if c["group"]})
    L = ["## Gaps and follow-ups", ""]
    for dd, r in out.items():
        if r["status"] == "n/m":
            L.append(f"- **{r['name']} ({dd})**: {r['note']}.")
        elif r.get("unknown"):
            L.append(
                f"- **{r['name']} ({dd})**, not verified: "
                + "; ".join(text.get(u, u).split(":")[0].split(" (")[0] for u in r["unknown"])
                + "."
            )
    return [*L, fill("add what would resolve each gap, and any correction made during review"), ""]


def closing_lines(framed):
    required = ". REQUIRED: the frame was assumed" if framed == "assumed" else ""
    return [
        "## Assumptions and open questions",
        "",
        fill("every frame field that was assumed, and which answer would change the tier" + required),
        "",
        "## Evidence",
        "",
        "| What it shows | Source | Date |",
        "|---|---|---|",
        fill(
            "10 to 20 rows grouped under bold label rows (Project signals, Vulnerabilities, "
            "Our own probes). Only evidence a finding or score cell relies on. The full "
            "criterion ledger stays in evidence-ledger.md"
        ),
        "",
    ]


def report_lines(S, F, up, crit):
    return (
        header_lines(S, F)
        + findings_lines()
        + scorecard_lines(S, up)
        + slsa_lines(S, F, crit)
        + recommendation_lines(S, F)
        + exit_lines(S["usage"])
        + alternatives_lines(S)
        + safe_use_lines()
        + gap_lines(S["dimensions"], crit)
        + closing_lines(S["framed_by"])
    )


def criterion_order(cid):
    return int(re.sub(r"\D", "", cid.split(".")[0]) or 0), cid


def ledger_lines(S, F, given):
    head = (F.get("history") or {}).get("head", "")[:10]
    L = [
        "# Evidence ledger: " + str(S["library"]),
        "",
        f"{S['rubric']}, {S['assessed']}, HEAD {head}. Every criterion answer behind the scores.",
        "",
        "| Criterion | Answer | By | Evidence |",
        "|---|---|---|---|",
    ]
    for cid in sorted(S["answers"], key=criterion_order):
        a = S["answers"][cid]
        ev = str(a["ev"]).replace("|", "/").replace("\n", " ")
        by = a["by"] + (" (overrides auto)" if a.get("overrode_auto") else "")
        L.append(f"| {cid} | {a['a']} | {by} | {ev} |")
    for k in DQ:
        if k in given:
            ev = str(given[k].get("ev", "")).replace("|", "/")
            L.append(f"| {k} | {given[k].get('a')} | J | {ev} |")
    return L


def prior_yaml(S, F):
    """What a later vetting of the same library compares with."""
    fields = (
        ("library", S["library"]),
        ("repo", F.get("repo")),
        ("assessed", S["assessed"]),
        ("rubric", S["rubric"]),
        ("mode", S["mode"]),
        ("version", S["version"]),
        ("head", (F.get("history") or {}).get("head", "")),
        ("usage", S["usage"]),
        ("framed_by", S["framed_by"]),
        ("tier", S["tier"]),
        ("score", S["overall"]),
        ("categories", " ".join(f"{k}={S['categories'][k]['pct']}" for k in "ABCD")),
        ("slsa", slsa_text(S["slsa"])),
        ("provisional", str(S["provisional"]).lower()),
    )
    return "\n".join(f'{k}: "{v}"' for k, v in fields) + "\n"


def print_summary(S):
    print(f"{S['library']} {S['version']}: {tier_line(S)}, {S['overall']}")
    for k in "ABCD":
        c = S["categories"][k]
        print(
            f" {k} {CATEGORY_NAMES[k]:24} {c['colour']:6} {c['earned']:g}/{c['attainable']}"
            + (f" pending {c['pending']}" if c["pending"] else "")
        )
    print(" " + " ".join(f"{dd}={r.get('score', r['status'])}" for dd, r in S["dimensions"].items()))
    print(f" SLSA: {slsa_text(S['slsa'])}")
    if S["disqualifiers"]:
        print(f" disqualifiers={S['disqualifiers']}")
    if S["unanswered"]:
        print(f" PENDING: {len(S['unanswered'])} criteria unanswered; run with --todo")


def main():
    pos = [x for x in sys.argv[1:] if not x.startswith("--")]
    if len(pos) != 1:
        sys.exit(__doc__)
    d = pos[0]
    F, frame, given = load(d, "facts.json"), load(d, "frame.json"), load(d, "answers.json")
    dims, crit = parse()
    check_answers(given)
    apply_corrections(F, given)
    lang, ctx = context(F, frame)
    na_dims, up = applicable_dims(frame), uplifts(frame)
    ans = merge_answers(crit, given, auto(F))
    live = [c for c in crit if c["dim"] not in na_dims and all(ctx[x] for x in c["tags"])]
    if "--todo" in sys.argv:
        print_todo(live, ans, given)
        return
    todo = [c["id"] for c in live if c["id"] not in ans] + [k for k in DQ if k not in given]
    out = score_dimensions(dims, live, ans, F.get("scorecard") or {}, frame, na_dims, up)
    S = summarize(F, frame, lang, ctx, ans, given, todo, out, category_totals(out))
    save(d, "scored.json", json.dumps(S, indent=1, sort_keys=True))
    save(d, "report.md", "\n".join(report_lines(S, F, up, crit)) + "\n")
    save(d, "evidence-ledger.md", "\n".join(ledger_lines(S, F, given)) + "\n")
    save(d, "prior.yaml", prior_yaml(S, F))
    print_summary(S)


if __name__ == "__main__":
    main()
