"""Offline tests for the library-vetting scorer. Run: uv run pytest"""

import json
import pathlib
import shutil
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[2]
SKILL = ROOT / "skills" / "library-vetting"
SCORE = str(SKILL / "scripts" / "score.py")
FIXTURE = pathlib.Path(__file__).parent / "fixture"


@pytest.fixture
def work(tmp_path):
    for f in FIXTURE.iterdir():
        shutil.copy(f, tmp_path)
    return tmp_path


def run(d, *args):
    return subprocess.run([sys.executable, SCORE, str(d), *args], capture_output=True, text=True)


def scored(d):
    return json.loads((d / "scored.json").read_text())


def edit(d, name, change):
    data = json.loads((d / name).read_text())
    change(data)
    (d / name).write_text(json.dumps(data))


def test_fixture_result(work):
    r = run(work)
    assert r.returncode == 0, r.stderr
    s = scored(work)
    assert s["tier"] == "LIMIT"
    assert (s["overall_earned"], s["overall_attainable"]) == (49.3, 98)
    assert s["unanswered"] == []
    report = (work / "report.md").read_text()
    assert [(x["track"], x["level"]) for x in s["slsa"]] == [("Build", 0), ("Source", 1), ("Dependency", 1)]
    assert s["slsa"][2]["base_stack_only"] and "shows only its base stack" in (work / "report.md").read_text()
    for heading in (
        "## Bottom line",
        "## Findings at a glance",
        "## Scorecards",
        "## SLSA levels",
        "## Exit cost",
        "## Alternatives",
        "## Evidence",
    ):
        assert heading in report


def test_same_input_same_output(work):
    run(work)
    first = (work / "scored.json").read_bytes()
    run(work)
    assert (work / "scored.json").read_bytes() == first


def test_missing_answer_blocks_tier(work):
    edit(work, "answers.json", lambda a: a.pop("DQ.license"))
    run(work)
    assert scored(work)["tier"] == "PENDING"


def test_invalid_answer_rejected(work):
    edit(work, "answers.json", lambda a: a.update({"D6.signed": {"a": "partial"}}))
    r = run(work)
    assert r.returncode != 0
    assert "D6.signed" in r.stderr


@pytest.mark.parametrize(
    "usage,candidates,tier",
    [("new", [], "AVOID"), ("existing", ["x"], "REPLACE"), ("existing", [], "OWN IT")],
)
def test_disqualifier_depends_on_usage(work, usage, candidates, tier):
    edit(work, "answers.json", lambda a: a.update({"DQ.no_fix_supply": {"a": "yes", "ev": "t"}}))
    edit(work, "frame.json", lambda f: f.update(usage=usage, candidates=candidates))
    run(work)
    assert scored(work)["tier"] == tier


def test_todo_lists_only_known_criteria(work):
    (work / "answers.json").write_text("{}")
    out = run(work, "--todo").stdout
    ids = {
        line.split(" | ")[0]
        for line in (SKILL / "scripts" / "rubric.txt").read_text().splitlines()
        if not line.startswith("#")
    }
    listed = {line.split(" | ")[0] for line in out.splitlines() if " | " in line}
    assert listed and all(
        i.split("~")[0] in {x.split("~")[0] for x in ids} or i.startswith(("DQ.", "CAP.")) for i in listed
    )


def test_registry_without_release_dates_is_scored(work):
    edit(
        work,
        "facts.json",
        lambda f: f.update(registry={"ecosystem": "pypi", "name": "x", "last_releases": []}),
    )
    assert run(work).returncode == 0


def test_release_age_does_not_depend_on_the_day_of_the_run(work):
    def old_facts(f):
        f["collected_at"] = "2020-06-01T00:00:00+00:00"
        f["history"]["days_since_last_tag"] = None
        f["registry"] = {"ecosystem": "pypi", "name": "x", "last_releases": ["2020-01-01T00:00:00Z"]}

    edit(work, "facts.json", old_facts)
    run(work)
    assert scored(work)["answers"]["D1.release"]["a"] == "yes"


@pytest.mark.parametrize(
    "registry,host,answer",
    [
        ("Apache 2.0", "Zlib", "yes"),
        (None, "NOASSERTION", "yes"),
        ({"type": "MIT"}, None, "yes"),
        ("MIT OR Apache-2.0", "MIT", None),
        ("Proprietary", "NOASSERTION", "no"),
    ],
)
def test_license_identifier_wins_over_free_text(work, registry, host, answer):
    def licenses(f):
        f["registry"] = {"ecosystem": "pypi", "name": "x", "license": registry}
        f["github"] = {"license": host}
        f["tree"]["license_spdx_guess"] = None if answer == "no" else "Zlib"

    edit(work, "facts.json", licenses)
    assert run(work).returncode == 0
    assert scored(work)["answers"].get("D10.osi", {}).get("a") == answer


@pytest.mark.parametrize(
    "ci,answer",
    [
        ({"count": 1, "files": [".travis.yml"], "actions_total": 0}, None),
        ({"count": 1, "files": [".github/workflows/ci.yml"], "actions_total": 0}, "yes"),
        ({"count": 1, "files": [".travis.yml"], "actions_total": 0, "dangerous_triggers": True}, "no"),
        (
            {"count": 1, "files": [".github/workflows/ci.yml"], "actions_total": 5, "actions_sha_pinned": 4},
            "yes",
        ),
        (
            {"count": 1, "files": [".github/workflows/ci.yml"], "actions_total": 5, "actions_sha_pinned": 3},
            "no",
        ),
    ],
)
def test_ci_without_actions_gets_no_automatic_answer(work, ci, answer):
    edit(work, "facts.json", lambda f: f["tree"].update(ci=ci))
    edit(work, "answers.json", lambda a: a.pop("D12.ci_hardened", None))
    run(work)
    assert scored(work)["answers"].get("D12.ci_hardened", {}).get("a") == answer


def yes(*ids):
    return {i: {"a": "yes", "ev": "t", "by": "E"} for i in ids}


@pytest.mark.parametrize(
    "answers,levels",
    [
        ({}, {"Build": 0, "Source": 1, "Dependency": 0}),
        (yes("D12.generated"), {"Build": 1, "Source": 1, "Dependency": 0}),
        (yes("D12.generated", "D12.provenance"), {"Build": 2, "Source": 1, "Dependency": 0}),
        (yes("D12.generated", "D12.provenance", "D12.isolated"), {"Build": 3, "Source": 1, "Dependency": 0}),
        (yes("D12.provenance", "D12.isolated"), {"Build": 0, "Source": 1, "Dependency": 0}),
        (yes("D12.protected", "D12.two_party"), {"Build": 0, "Source": 1, "Dependency": 0}),
        (yes("D12.source_attested", "D12.protected"), {"Build": 0, "Source": 3, "Dependency": 0}),
        (
            yes("D12.source_attested", "D12.protected", "D12.two_party"),
            {"Build": 0, "Source": 4, "Dependency": 0},
        ),
        (yes("D6.sbom"), {"Build": 0, "Source": 1, "Dependency": 1}),
        (yes("D6.pinned", "D6.update_bot"), {"Build": 0, "Source": 1, "Dependency": 1}),
        (yes("D6.pinned", "D6.update_bot", "D12.ci_hardened"), {"Build": 0, "Source": 1, "Dependency": 1}),
        (
            yes("D6.pinned", "D6.update_bot", "D12.ci_hardened", "D6.stack_current"),
            {"Build": 0, "Source": 1, "Dependency": 2},
        ),
        (
            yes("D6.pinned", "D6.update_bot", "D13.hermetic", "D6.stack_current", "D6.screened"),
            {"Build": 0, "Source": 1, "Dependency": 2},
        ),
        (
            yes(
                "D6.pinned",
                "D6.update_bot",
                "D13.hermetic",
                "D6.stack_current",
                "D6.screened",
                "D6.stack_clean",
            ),
            {"Build": 0, "Source": 1, "Dependency": 3},
        ),
        (
            yes(
                "D6.pinned",
                "D6.update_bot",
                "D12.ci_hardened",
                "D6.stack_current",
                "D6.screened",
                "D6.stack_clean",
            ),
            {"Build": 0, "Source": 1, "Dependency": 2},
        ),
        (
            yes(
                "D6.pinned",
                "D6.update_bot",
                "D12.ci_hardened",
                "D6.stack_current",
                "D6.screened",
                "D6.stack_clean",
                "D13.toolchain",
            ),
            {"Build": 0, "Source": 1, "Dependency": 3},
        ),
    ],
)
def test_slsa_level_needs_each_lower_level(work, answers, levels):
    no = {
        i: {"a": "no", "ev": "t", "by": "E"}
        for i in (
            "D12.generated",
            "D12.provenance",
            "D12.isolated",
            "D12.source_attested",
            "D12.protected",
            "D12.two_party",
            "D6.sbom",
            "D6.pinned",
            "D6.update_bot",
            "D6.screened",
            "D12.ci_hardened",
            "D13.hermetic",
            "D13.toolchain",
            "D6.stack_current",
            "D6.stack_clean",
        )
    }
    edit(work, "facts.json", lambda f: f["tree"].update(manifest_runtime_deps=["x"]))
    edit(work, "answers.json", lambda a: a.update({**no, **answers}))
    assert run(work).returncode == 0
    assert {x["track"]: x["level"] for x in scored(work)["slsa"]} == levels


def test_ci_step_alone_does_not_prove_signed_provenance(work):
    edit(work, "facts.json", lambda f: f["tree"]["ci"].update(provenance=True))
    edit(work, "answers.json", lambda a: [a.pop(k, None) for k in ("D12.generated", "D12.provenance")])
    r = run(work, "--todo")
    assert "D12.provenance |" in r.stdout and "D12.generated |" not in r.stdout
    edit(
        work, "facts.json", lambda f: f.update(registry={"ecosystem": "npm", "name": "x", "provenance": True})
    )
    run(work)
    assert scored(work)["answers"]["D12.provenance"] == {"a": "yes", "ev": "facts.json", "by": "A"}


def slsa(strongest="none", oidc=False, self_hosted=False, source_attestation=False):
    return {
        "generators": [],
        "strongest": strongest,
        "oidc": oidc,
        "self_hosted": self_hosted,
        "source_attestation": source_attestation,
    }


D12_AUTO = ("D12.generated", "D12.provenance", "D12.isolated", "D12.source_attested", "D12.verifiable")


@pytest.mark.parametrize(
    "ci,extra,expected,build",
    [
        # generated, signed by the platform, isolated builder, source attested, verifiable; Build level
        ({"slsa": slsa()}, {}, ("no", "no", "no", "no", None), 0),
        ({"slsa": slsa(), "provenance": True}, {}, (None, None, None, "no", None), 0),
        ({"slsa": slsa("unsigned")}, {}, ("yes", None, None, "no", None), 1),
        ({"slsa": slsa("signed")}, {}, ("yes", None, None, "no", None), 1),
        ({"slsa": slsa("signed", oidc=True)}, {}, ("yes", "yes", None, "no", None), 2),
        ({"slsa": slsa("signed", oidc=True, self_hosted=True)}, {}, ("yes", None, None, "no", None), 1),
        (
            {"slsa": slsa("isolated", oidc=True, source_attestation=True)},
            {},
            ("yes", "yes", "yes", "yes", None),
            3,
        ),
        (
            {"slsa": slsa("isolated", oidc=True)},
            {"pipeline_check": {"github": {"failed_checks": {"Build.L3.Ephemeral": ["GHA-012"]}}}},
            ("yes", None, None, "no", None),
            1,
        ),
        (
            {"slsa": slsa()},
            {"registry": {"ecosystem": "npm", "name": "x", "provenance": True}},
            ("yes", "yes", None, "no", None),
            2,
        ),
        (
            {"slsa": slsa()},
            {"verification_docs": ["README.md: slsa-verifier"]},
            ("no", "no", "no", "no", "yes"),
            0,
        ),
    ],
)
def test_program_answers_the_provenance_criteria(work, ci, extra, expected, build):
    def facts(f):
        f["tree"]["ci"].update(ci)
        f["tree"]["verification_docs"] = extra.pop("verification_docs", [])
        f.update(extra)

    edit(work, "facts.json", facts)
    edit(work, "answers.json", lambda a: [a.pop(k, None) for k in D12_AUTO])
    run(work)
    s = scored(work)
    assert tuple(s["answers"].get(k, {}).get("a") for k in D12_AUTO) == expected
    assert s["slsa"][0]["level"] == build


def test_plumber_answers_if_the_scorecard_does_not(work):
    def facts(f):
        f["plumber"] = {
            "controls": {
                "branchMustBeProtected": {"status": "passed", "issues": []},
                "mrApprovalRulesMustRequireMinimumNumberOfApprovals": {
                    "status": "failed",
                    "issues": ["ISSUE-502"],
                },
            }
        }

    edit(work, "facts.json", facts)
    edit(
        work,
        "answers.json",
        lambda a: [a.pop(k, None) for k in ("D12.protected", "D12.two_party", "_scorecard")],
    )
    run(work)
    answers = scored(work)["answers"]
    assert (answers["D12.protected"]["a"], answers["D12.two_party"]["a"]) == ("yes", "no")


def stack_row(status, *issues, name="o/a"):
    return {
        "kind": "action",
        "name": name,
        "ref": "v1",
        "version": "v1",
        "pin": "tag",
        "latest": "v2.0.0",
        "status": status,
        "issues": list(issues),
        "why": "; ".join(issues),
    }


@pytest.mark.parametrize(
    "rows,current,clean",
    [
        ([stack_row("Green")], "yes", "yes"),
        ([stack_row("Green"), stack_row("Amber", "outdated")], "no", "yes"),
        ([stack_row("Amber", "floating reference")], "no", "yes"),
        ([stack_row("Amber", "advisory history")], "yes", "yes"),
        ([stack_row("Red", "end of life")], "no", "yes"),
        ([stack_row("Red", "vulnerable", "outdated")], "no", "no"),
        ([stack_row("Green"), stack_row("unknown")], None, None),
        ([], None, None),
    ],
)
def test_base_stack_screen_answers_two_criteria(work, rows, current, clean):
    edit(work, "facts.json", lambda f: f.update(base_stack={"depth": "d", "rows": rows}))
    edit(work, "answers.json", lambda a: [a.pop(k) for k in ("D6.stack_current", "D6.stack_clean")])
    run(work)
    answers = scored(work)["answers"]
    assert answers.get("D6.stack_current", {}).get("a") == current
    assert answers.get("D6.stack_clean", {}).get("a") == clean
    report = (work / "report.md").read_text()
    assert ("| 🔴 | o/a | action | v1 | tag | v2.0.0 | vulnerable; outdated |" in report) is (clean == "no")
    assert ("<!-- FILL: the collector did not screen the base stack" in report) is (rows == [])


def test_helper_findings_are_in_the_report(work):
    edit(
        work,
        "facts.json",
        lambda f: f.update(
            pipeline_check={
                "github": {
                    "version": "1",
                    "score": 97,
                    "grade": "A",
                    "complete": True,
                    "failed_checks": {"Build.L2.Signed": ["GHA-006", "GHA-024"]},
                }
            },
            plumber={
                "score": "B",
                "ci_valid": True,
                "commit": "c",
                "controls": {
                    "branchMustBeProtected": {"status": "failed", "issues": ["ISSUE-501"]},
                    "other": {"status": "passed", "issues": []},
                },
            },
        ),
    )
    run(work)
    report = (work / "report.md").read_text()
    assert (
        "- pipeline-check 1 on the github files: grade A (97). Failed checks for each control: "
        "Build.L2.Signed: GHA-006, GHA-024." in report
    )
    assert "- plumber: score B. Failed controls: branchMustBeProtected." in report


def test_fact_correction_keeps_the_other_keys(work):
    run(work)
    before = scored(work)["answers"]
    edit(work, "answers.json", lambda a: a.update(_facts={"tree": {"sbom_files": ["bom.json"]}}))
    run(work)
    after = scored(work)["answers"]
    assert after["D6.sbom"]["a"] == "yes"
    assert {k: v for k, v in after.items() if k != "D6.sbom"} == {
        k: v for k, v in before.items() if k != "D6.sbom"
    }


def test_usage_without_a_folder():
    r = subprocess.run([sys.executable, SCORE, "--todo"], capture_output=True, text=True)
    assert r.returncode != 0 and "score.py DIR" in r.stderr


@pytest.mark.parametrize("fact,answer", [(True, "yes"), (False, None), (None, None)])
def test_private_reports_on_github_are_a_report_channel(work, fact, answer):
    edit(work, "facts.json", lambda f: f.update(github_private_reports=fact))
    edit(work, "answers.json", lambda a: a.pop("D2.channel"))
    run(work)
    assert scored(work)["answers"].get("D2.channel", {}).get("a") == answer


@pytest.mark.parametrize(
    "silent,raw,unknown",
    [
        # points for policy (2), channel (1), no silent fix (1), and advisories (2) only after a silent fix
        ("yes", "1/4", []),
        ("no", "0/6", []),
        ("unknown", "0/4", ["D2.no_silent"]),
    ],
)
def test_silent_fix_counts_without_an_advisory_record(work, silent, raw, unknown):
    def answers(a):
        for k in [k for k in a if k.startswith("D2.")]:
            a[k] = {"a": "no", "ev": "t"}
        a["D2.no_history"] = {"a": "yes", "ev": "t"}
        a["D2.no_silent"] = {"a": silent, "ev": "t"}

    edit(work, "answers.json", answers)
    run(work)
    d2 = scored(work)["dimensions"]["D2"]
    assert (d2["raw"], d2["unknown"], d2["caps"]) == (raw, unknown, [7])
