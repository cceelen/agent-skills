"""Offline tests for the library-vetting collector. Run: uv run pytest"""

import importlib.util
import json
import pathlib
import subprocess
from datetime import timedelta

SKILL = pathlib.Path(__file__).resolve().parents[2] / "skills" / "library-vetting"
spec = importlib.util.spec_from_file_location("collect", SKILL / "scripts" / "collect.py")
collect = importlib.util.module_from_spec(spec)
spec.loader.exec_module(collect)


def git(cwd, *args):
    subprocess.run(
        ["git", "-c", "user.name=t", "-c", "user.email=t@example.org", *args],
        cwd=cwd,
        check=True,
        capture_output=True,
    )


def test_free_mail_matches_only_at_a_label_boundary():
    for personal in ("gmail.com", "users.noreply.github.com", "protonmail.com", "mail.ru", "me.com"):
        assert collect.free_mail(personal)
    for employer in ("acme.com", "chrome.com", "olive.io", "example.org"):
        assert not collect.free_mail(employer)


def test_within_counts_a_date_of_today():
    assert collect.within(collect.NOW.isoformat(), 0)
    assert collect.within((collect.NOW - timedelta(days=30)).isoformat(), 30)
    assert not collect.within((collect.NOW - timedelta(days=31)).isoformat(), 30)
    assert not collect.within(None, 30)


def test_reused_clone_follows_the_remote_head(tmp_path):
    origin, dest = tmp_path / "origin", tmp_path / "src"
    origin.mkdir()
    git(origin, "init", "-q")
    git(origin, "commit", "-q", "--allow-empty", "-m", "one")
    url = origin.as_uri()
    assert collect.clone(url, str(dest)).startswith("shallow")
    git(origin, "commit", "-q", "--allow-empty", "-m", "two")
    head = collect.sh(["git", "rev-parse", "HEAD"], str(origin)).strip()
    assert collect.clone(url, str(dest)) == "reused, updated to the remote head"
    assert collect.history(str(dest))["head"] == head


def test_repository_address_keeps_gitlab_subgroups():
    for given, expected in (
        ("git+https://github.com/a/b.git", "https://github.com/a/b"),
        ("https://github.com/a/b/tree/main/docs", "https://github.com/a/b"),
        ("git@gitlab.com:group/sub/project.git", "https://gitlab.com/group/sub/project"),
        ("https://gitlab.com/group/sub/project/-/tree/main", "https://gitlab.com/group/sub/project"),
        ("https://gitlab.example.org/group/project/issues", "https://gitlab.example.org/group/project"),
        (
            "https://chromium.googlesource.com/chromium/src/third_party/zlib/+/refs/heads/main/README.chromium",
            "https://chromium.googlesource.com/chromium/src/third_party/zlib",
        ),
        ("https://github.com/a", None),
        (None, None),
    ):
        assert collect.norm_repo(given) == expected


def test_pypi_repository_is_not_a_sponsor_page():
    urls = {
        "Funding": "https://github.com/sponsors/someone",
        "Source": "https://github.com/a/b",
        "Docs": "https://a.example.org",
    }
    assert collect.pypi_repo(urls) == "https://github.com/a/b"
    assert collect.pypi_repo({"Funding": "https://github.com/sponsors/someone"}) is None


def test_tree_scan_reads_policy_and_os_names_exactly(tmp_path):
    files = {"docs/topics/security.md": "x", ".travis.yml": "os: linux\n# test scenarios\n"}
    for name, text in files.items():
        (tmp_path / name).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / name).write_text(text)
    git(tmp_path, "init", "-q")
    git(tmp_path, "add", "-A")
    git(tmp_path, "commit", "-q", "-m", "one")
    t = collect.tree(str(tmp_path))
    assert t["security_policy"] == []
    assert t["ci"]["os_matrix"] == []

    (tmp_path / ".github").mkdir()
    (tmp_path / ".github" / "SECURITY.md").write_text("x")
    (tmp_path / ".travis.yml").write_text("os: [ios, macos-14]\n")
    git(tmp_path, "add", "-A")
    t = collect.tree(str(tmp_path))
    assert t["security_policy"] == [".github/SECURITY.md"]
    assert t["ci"]["os_matrix"] == ["ios", "macos"]


def test_bus_factor_counts_the_authors_of_most_commits():
    assert collect.bus_factor([("a", 8), ("b", 1), ("c", 1)], 10) == 1
    assert collect.bus_factor([("a", 4), ("b", 3), ("c", 3)], 10) == 3
    assert collect.bus_factor([], 1) == 0


def test_dependency_status_gives_the_worst_reason_first():
    assert collect.dep_status({"deprecated": True, "publishers": 1}, 2000) == ("Red", "deprecated or yanked")
    assert collect.dep_status({"publishers": 3}, 1096) == ("Amber", "no release in 36 months")
    assert collect.dep_status({"publishers": 1}, 10) == ("Amber", "single publisher")
    assert collect.dep_status({"publishers": 2}, None) == ("Green", "")


def test_package_facts_without_the_network(monkeypatch):
    npm = {
        "dist-tags": {"latest": "2.0.0"},
        "maintainers": [{}, {}],
        "time": {
            "created": "2020-01-01T00:00:00Z",
            "1.0.0": "2020-01-02T00:00:00Z",
            "2.0.0": "2024-05-06T00:00:00Z",
        },
        "versions": {
            "2.0.0": {
                "license": {"type": "MIT"},
                "dependencies": {"b": "1", "a": "1"},
                "repository": {"url": "git+https://github.com/o/p.git"},
                "scripts": {"postinstall": "x", "test": "y"},
            }
        },
    }

    def get(url, payload=None, timeout=20):
        if url == "https://registry.npmjs.org/p":
            return npm
        raise OSError("no network")

    monkeypatch.setattr(collect, "get", get)
    F = collect.gather("npm:p", "unused", None, lite=True)
    assert F["repo"] == "https://github.com/o/p"
    assert F["registry"] == {
        "ecosystem": "npm",
        "name": "p",
        "version": "2.0.0",
        "license": "MIT",
        "versions": 2,
        "repo": "https://github.com/o/p",
        "released": "2024-05-06T00:00:00Z",
        "deprecated": False,
        "publishers": 2,
        "install_scripts": ["postinstall"],
        "provenance": False,
        "runtime_deps": ["a", "b"],
        "last_releases": ["2020-01-02T00:00:00Z", "2024-05-06T00:00:00Z"],
    }
    # each source that fails records its error, and the collection continues
    assert sorted(F["errors"]) == [
        "depsdev_project",
        "depsdev_version",
        "github",
        "github_private_reports",
        "osv",
        "scorecard",
    ]
    assert [x["id"] for x in F["fetch_plan"]] == ["scorecard", "nvd", "advisories"]
    assert "dep_screen" not in F and "history" not in F


def helper(folder, name, script):
    """A stand-in for a helper program on the PATH."""
    path = folder / name
    path.write_text("#!/bin/sh\n" + script)
    path.chmod(0o755)


def test_pipeline_check_is_used_only_if_it_is_installed(tmp_path, monkeypatch):
    src, bin_dir = tmp_path / "src", tmp_path / "bin"
    (src / ".github" / "workflows").mkdir(parents=True)
    bin_dir.mkdir()
    monkeypatch.setenv("PATH", str(bin_dir))
    F = {"errors": {}}
    collect.add_pipeline_check(F, str(src))
    assert F == {"errors": {}}

    report = {
        "tool_version": "9",
        "score": {"score": 80, "grade": "B"},
        "scan_status": {"complete": True},
        "findings": [
            {
                "check_id": "GHA-024",
                "passed": False,
                "controls": [{"control_id": "Build.L2.Signed"}, {"control_id": "Build.L1.Provenance"}],
            },
            {"check_id": "GHA-006", "passed": False, "controls": [{"control_id": "Build.L2.Signed"}]},
            {"check_id": "GHA-015", "passed": False, "controls": []},
            {"check_id": "GHA-001", "passed": True, "controls": [{"control_id": "x"}]},
        ],
    }
    (tmp_path / "report.json").write_text(json.dumps(report))
    # the stand-in fails if the CI system is not named, as the real program then reads a cloud account
    helper(
        bin_dir,
        "pipeline_check",
        f'[ "$1 $2 $3 $4" = "--pipeline github --gha-path .github/workflows" ] '
        f"|| exit 2\n/bin/cat {tmp_path}/report.json\nexit 1\n",
    )
    collect.add_pipeline_check(F, str(src))
    assert F == {
        "errors": {},
        "pipeline_check": {
            "github": {
                "version": "9",
                "score": 80,
                "grade": "B",
                "complete": True,
                "failed_checks": {
                    "Build.L1.Provenance": ["GHA-024"],
                    "Build.L2.Signed": ["GHA-006", "GHA-024"],
                    "no SLSA control": ["GHA-015"],
                },
            }
        },
    }

    helper(bin_dir, "pipeline_check", "echo broken >&2\nexit 2\n")
    F = {"errors": {}}
    collect.add_pipeline_check(F, str(src))
    assert "pipeline_check" not in F and "exit code 2: broken" in F["errors"]["pipeline_check"]


def test_plumber_needs_the_program_and_a_token(tmp_path, monkeypatch):
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    report = {
        "plumberScore": "C",
        "ciValid": True,
        "headCommitSha": "abc",
        "projectPath": "o/p",
        "branchResult": {
            "controlName": "branchMustBeProtected",
            "status": "failed",
            "issues": [{"code": "ISSUE-501"}, {"code": "ISSUE-501"}],
        },
        "imageResult": {"controlName": "imageMustBePinned", "status": "passed", "issues": []},
    }
    (tmp_path / "report.json").write_text(json.dumps(report))
    helper(
        bin_dir,
        "plumber",
        f'[ "$1 $2 $3" = "analyze github.com/o/p --output" ] || exit 2\n'
        f'/bin/cp {tmp_path}/report.json "$4"\n',
    )
    monkeypatch.setenv("PATH", str(bin_dir))
    for name in ("GH_TOKEN", "GITHUB_TOKEN", "GH_ENTERPRISE_TOKEN", "GITLAB_TOKEN"):
        monkeypatch.delenv(name, raising=False)
    F = {"errors": {}}
    collect.add_plumber(F, "github.com/o/p")
    assert F == {"errors": {}}
    monkeypatch.setenv("GITLAB_TOKEN", "t")  # a token for a different host is not sufficient
    collect.add_plumber(F, "github.com/o/p")
    assert F == {"errors": {}}
    assert collect.signed_in("gitlab.com/g/p") and collect.signed_in("git.example.org/g/sub/p")
    monkeypatch.delenv("GITLAB_TOKEN")
    assert not collect.signed_in("git.example.org/g/p")
    monkeypatch.setenv("GH_ENTERPRISE_TOKEN", "t")
    assert collect.signed_in("github.example.org/o/p") and not collect.signed_in("github.com/o/p")
    monkeypatch.setenv("GH_TOKEN", "t")
    collect.add_plumber(F, "github.com/o/p")
    assert F == {
        "errors": {},
        "plumber": {
            "score": "C",
            "ci_valid": True,
            "commit": "abc",
            "controls": {
                "branchMustBeProtected": {"status": "failed", "issues": ["ISSUE-501"]},
                "imageMustBePinned": {"status": "passed", "issues": []},
            },
        },
    }


def test_provenance_generators_in_the_ci_text():
    def facts(text):
        f = collect.slsa_facts(text)
        return f["strongest"], f["generators"], f["oidc"], f["self_hosted"], f["source_attestation"]

    assert facts("run: make\n") == ("none", [], False, False, False)
    assert facts("run: cosign sign-blob x\n")[0] == "none"  # a signature is not provenance
    assert facts('permissions:\n  id-token: write\nsteps:\n- uses: "pypa/gh-action-pypi-publish@abc"\n') == (
        "signed",
        ["pypi trusted publishing"],
        True,
        False,
        False,
    )
    assert facts("- uses: actions/attest-build-provenance@v2\n- run: npm publish --provenance\n")[:2] == (
        "signed",
        ["github attestation", "npm provenance"],
    )
    assert facts(
        "uses: slsa-framework/slsa-github-generator/.github/workflows/generator_generic_slsa3.yml@v2\n"
        "with:\n  provenance: mode=max\n"
    )[:2] == ("isolated", ["buildkit provenance", "slsa-github-generator"])
    assert facts("variables:\n  RUNNER_GENERATE_ARTIFACTS_METADATA: 'true'\n")[0] == "unsigned"
    assert facts("runs-on: [self-hosted, linux]\n")[3] and facts("runs-on:\n  - self-hosted\n")[3]
    assert not facts("runs-on: ubuntu-latest\n")[3]
    assert facts("- uses: slsa-framework/source-actions/actions/slsa_with_provenance@main\n")[4]


def test_tree_scan_finds_verify_commands_and_quoted_actions(tmp_path):
    sha = "a" * 40
    files = {
        "README.md": "Verify:\n\n    gh attestation verify x.tar.gz --owner o\n",
        "docs/verify.md": "Use slsa-verifier or cosign verify-blob.",
        "src/deep/README.md": "gpg --verify is not read at this depth",
        ".github/workflows/release.yml": f'steps:\n- uses: "actions/checkout@{sha}"\n'
        "- uses: actions/setup-go@v5\n",
    }
    for name, text in files.items():
        (tmp_path / name).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / name).write_text(text)
    git(tmp_path, "init", "-q")
    git(tmp_path, "add", "-A")
    t = collect.tree(str(tmp_path))
    assert t["verification_docs"] == [
        "README.md: gh attestation verify",
        "docs/verify.md: cosign verify-blob",
        "docs/verify.md: slsa-verifier",
    ]
    assert (t["ci"]["actions_total"], t["ci"]["actions_sha_pinned"]) == (2, 1)


def test_action_references_with_their_pins():
    sha = "b" * 40
    rows = collect.action_refs(
        f"- uses: actions/checkout@{sha} # v4.1.1\n- uses: 'o/a/sub@v3'\n"
        f"- uses: o/b@main\n- uses: o/c@{sha}\n- uses: ./local\n- uses: docker://x@y\n"
    )
    assert [(r["name"], r["version"], r["pin"]) for r in rows] == [
        ("actions/checkout", "v4.1.1", "digest"),
        ("o/a", "v3", "tag"),
        ("o/b", None, "branch"),
        ("o/c", None, "digest"),
    ]


def test_advisory_ranges():
    def vuln(*events, versions=()):
        return {
            "affected": [
                {"versions": list(versions), "ranges": [{"type": "ECOSYSTEM", "events": list(events)}]}
            ]
        }

    fixed = vuln({"introduced": "0"}, {"fixed": "4.1.2"})
    assert collect.affects(fixed, "v4.1.1") and not collect.affects(fixed, "4.1.2")
    assert not collect.affects(fixed, "v4")  # the tag v4 is the newest 4.x release
    assert collect.affects(vuln({"introduced": "0"}, {"fixed": "5.0.0"}), "v4")
    two = vuln(
        {"introduced": "1.0.0"}, {"fixed": "1.2.0"}, {"introduced": "2.0.0"}, {"last_affected": "2.3.0"}
    )
    assert [collect.affects(two, v) for v in ("1.1", "1.5", "2.3.0", "2.4")] == [True, False, True, False]
    assert collect.affects(vuln({"introduced": "3.0.0"}), "3.1") and not collect.affects(
        vuln({"introduced": "3.0.0"}), "2.9"
    )
    assert collect.affects(vuln(versions=["9.9.9"]), "v9.9.9")
    assert not collect.affects(
        {"affected": [{"ranges": [{"type": "GIT", "events": [{"introduced": "0"}]}]}]}, "1.0"
    )


def test_base_stack_screen_without_the_network(monkeypatch):
    sha = "c" * 40
    vulns = {
        "o/bad": [
            {
                "id": "GHSA-1",
                "affected": [
                    {"ranges": [{"type": "ECOSYSTEM", "events": [{"introduced": "0"}, {"fixed": "2.0.0"}]}]}
                ],
            },
            {"id": "GHSA-2", "affected": []},
        ]
    }
    cycles = [
        {"cycle": "20", "eol": "2020-01-01", "latest": "20.9.9"},
        {"cycle": "22", "eol": "2999-01-01"},
        {"cycle": "1.26", "eol": False},
    ]
    asked = []

    def get(url, payload=None, timeout=20):
        asked.append(url)
        if "endoflife.date/api/ruby" in url:
            raise OSError("no network")
        return {"vulns": vulns.get(payload["package"]["name"], [])} if payload else cycles

    monkeypatch.setattr(collect, "get", get)
    monkeypatch.setattr(collect, "latest_release_tag", lambda url: "v3.1.0")
    F = {
        "tree": {
            "ci": {
                "action_refs": collect.action_refs(
                    f"uses: o/bad@v1.5.0\nuses: o/bad@v3\nuses: o/good@{sha} # v3.0.1\n"
                    f"uses: o/float@main\nuses: o/blind@{sha}\n"
                )
            },
            "toolchain_versions": [
                {"kind": "toolchain", "name": n, "ref": f, "version": v, "pin": "file"}
                for n, f, v in (
                    ("nodejs", ".nvmrc", "20.1.0"),
                    ("nodejs", ".node-version", "22"),
                    ("go", "go.mod", "1.26"),
                    ("python", ".python-version", "3"),
                    ("ruby", ".ruby-version", "3.3.1"),
                )
            ],
            "base_images": [
                {"kind": "image", "name": "alpine", "ref": "Dockerfile", "version": "latest", "pin": "branch"}
            ],
        }
    }
    collect.add_base_stack(F)
    assert [(r["name"], r["version"], r["status"], r["issues"]) for r in F["base_stack"]["rows"]] == [
        ("o/bad", "v1.5.0", "Red", ["vulnerable", "outdated", "advisory history"]),
        ("o/bad", "v3", "Amber", ["advisory history"]),
        ("o/blind", None, "unknown", []),
        ("o/float", None, "Amber", ["floating reference"]),
        ("o/good", "v3.0.1", "Green", []),
        ("nodejs", "20.1.0", "Red", ["end of life"]),
        ("nodejs", "22", "Green", []),
        ("go", "1.26", "Green", []),
        ("python", "3", "n/a", []),
        ("ruby", "3.3.1", "unknown", []),
        ("alpine", "latest", "Amber", ["floating reference"]),
    ]
    assert len([u for u in asked if "osv.dev" in u]) == 4  # one request for each action, not for each use


def test_library_without_a_registry_gets_its_advisories_by_commit(monkeypatch):
    history = {"head": "h", "tags": [{"tag": "v2", "commit": "c2"}, {"tag": "v1", "commit": "c1"}]}
    by_commit = {"h": [], "c2": ["CVE-2"], "c1": ["CVE-1", "CVE-2"]}

    def get(url, payload=None, timeout=20):
        if url.endswith("/querybatch"):
            assert [q["commit"] for q in payload["queries"]] == ["h", "c2", "c1"]
            return {
                "results": [
                    {"vulns": [{"id": i} for i in by_commit[q["commit"]]]} for q in payload["queries"]
                ]
            }
        return {"id": url.rsplit("/", 1)[1], "published": "2026-01-02T00:00:00Z", "summary": "s"}

    monkeypatch.setattr(collect, "get", get)
    F = {"history": history, "errors": {}, "fetch_plan": []}
    collect.add_advisories(F, None, None, "lib", "github.com/o/lib")
    assert F["osv"]["count"] == 2 and F["fetch_plan"] == []
    assert [(r["id"], r["affects"]) for r in F["osv"]["recent"]] == [
        ("CVE-1", ["v1"]),
        ("CVE-2", ["v2", "v1"]),
    ]
    assert (F["osv"]["affects_head"], F["osv"]["affects_latest_release"]) == ([], ["CVE-2"])

    by_commit.update(c1=[], c2=[])  # nothing in OSV: the web tool must look, because that is no proof
    F = {"history": history, "errors": {}, "fetch_plan": []}
    collect.add_advisories(F, None, None, "lib", "github.com/o/lib")
    assert F["osv"]["count"] == 0 and "not evidence" in F["osv"]["note"]
    assert [x["id"] for x in F["fetch_plan"]] == ["nvd", "advisories"]


def test_facts_of_an_earlier_collector_are_not_reused():
    old = {
        "target": "t",
        "history": {},
        "collected_at": collect.NOW.isoformat(),
        "collector": collect.COLLECTOR,
    }
    assert collect.reusable(old, "t", False, "30")
    assert not collect.reusable({**old, "collector": collect.COLLECTOR - 1}, "t", False, "30")
    assert not collect.reusable({k: v for k, v in old.items() if k != "collector"}, "t", False, "30")


def test_release_tags_are_sorted_by_version_not_by_name():
    refs = "".join(
        f"abc\trefs/tags/{t}\n"
        for t in (
            "v2.0.0-RC2",
            "v2.0.0",
            "2.3.1",
            "2.10.0",
            "2.3.3",
            "v1.2.11.1_jtkv6",
            "nightly",
            "2.3.0-rc1",
        )
    )
    assert collect.release_tags(refs) == ["2.10.0", "2.3.3", "2.3.1", "v2.0.0"]


def test_advisory_range_without_an_end_takes_it_from_the_database_field():
    # GHSA-vqf5-2xx6-9wfm has this form: an introduced event only, and the end in a different field
    vuln = {
        "affected": [
            {
                "ranges": [{"type": "ECOSYSTEM", "events": [{"introduced": "2.26.11"}]}],
                "database_specific": {"last_known_affected_version_range": "< 3.0.0"},
            }
        ]
    }
    assert [collect.affects(vuln, v) for v in ("v2.27.0", "v3.0.0", "v4", "v4.38.0")] == [
        True,
        False,
        False,
        False,
    ]
    vuln["affected"][0]["database_specific"]["last_known_affected_version_range"] = "<= 3.28.2"
    assert collect.affects(vuln, "3.28.2") and not collect.affects(vuln, "3.28.3")


def test_github_token_goes_to_the_github_api_only(monkeypatch):
    sent = {}

    class Response:
        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def read(self):
            return b"{}"

    def urlopen(request, timeout=None):
        sent[request.full_url] = request.get_header("Authorization")
        return Response()

    monkeypatch.setenv("GITHUB_TOKEN", "secret")
    monkeypatch.setattr(collect.urllib.request, "urlopen", urlopen)
    for url in (
        "https://api.github.com/repos/o/p",
        "https://registry.npmjs.org/api.github.com",
        "https://example.org/?next=https://api.github.com/",
        "https://api.github.com.example.org/x",
    ):
        collect.get(url)
    assert sent == {
        "https://api.github.com/repos/o/p": "Bearer secret",
        "https://registry.npmjs.org/api.github.com": None,
        "https://example.org/?next=https://api.github.com/": None,
        "https://api.github.com.example.org/x": None,
    }
