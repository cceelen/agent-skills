#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""library-vetting collector. Stdlib + git only. One call gathers every mechanical fact.

  collect.py <repo-url | owner/repo | eco:name[@version]> [--out DIR] [--repo URL] [--lite]
             [--max-age DAYS]
  eco: npm pypi cargo go maven nuget gem composer hex pub   (maven name = group:artifact)

Writes DIR/facts.json (+ DIR/src = shallow clone unless --lite). Never aborts: each source
records its own error, and unreachable JSON sources are listed in facts["fetch_plan"] as exact
URLs for the web tool. Output is sorted and windowed on fixed dates so reruns agree.

Optional helpers, used only if the program is on the PATH: pipeline-check (reads the CI files of
the clone) and plumber (reads the settings of the repository on GitHub, GitLab or an own
instance of them; it needs a token for the host or a login of the gh program). Without them
the facts have no "pipeline_check" and no "plumber" section.
"""

import itertools
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone

NOW = datetime.now(timezone.utc)
COLLECTOR = 5  # increase when the facts change, so that facts of an earlier collector are not reused
UA = {"User-Agent": "library-vetting/1.0"}
FREE_MAIL = (
    "gmail.",
    "users.noreply",
    "outlook.",
    "hotmail.",
    "yahoo.",
    "proton",
    "icloud.",
    "googlemail.",
    "qq.com",
    "163.com",
    "me.com",
    "live.",
    "gmx.",
    "mail.",
    "fastmail.",
    "localhost",
)
DEEP_PATH_PAGES = ("-", "+", "tree", "blob", "issues", "merge_requests", "commits", "tags", "releases")
BOTS = re.compile(r"\[bot\]|dependabot|renovate|github-actions|greenkeeper", re.I)
MANIFESTS = {  # file -> ecosystem
    "package.json": "npm",
    "pyproject.toml": "pypi",
    "setup.py": "pypi",
    "setup.cfg": "pypi",
    "Cargo.toml": "cargo",
    "go.mod": "go",
    "pom.xml": "maven",
    "build.gradle": "maven",
    "build.gradle.kts": "maven",
    "Gemfile": "gem",
    "composer.json": "composer",
    "mix.exs": "hex",
    "pubspec.yaml": "pub",
    "Package.swift": "swift",
    "CMakeLists.txt": "c-cpp",
    "meson.build": "c-cpp",
    "configure.ac": "c-cpp",
    "Makefile": "c-cpp",
    "BUILD.bazel": "bazel",
    "MODULE.bazel": "bazel",
    "conanfile.py": "c-cpp",
    "vcpkg.json": "c-cpp",
    "build.zig": "zig",
}
LOCKS = (
    "package-lock.json",
    "yarn.lock",
    "pnpm-lock.yaml",
    "Cargo.lock",
    "go.sum",
    "poetry.lock",
    "uv.lock",
    "Pipfile.lock",
    "Gemfile.lock",
    "composer.lock",
    "mix.lock",
    "pubspec.lock",
    "gradle.lockfile",
    "MODULE.bazel.lock",
    "flake.lock",
    "conan.lock",
    "packages.lock.json",
    "Package.resolved",
)
LANG = {
    ".c": "c",
    ".h": "c",
    ".cc": "cpp",
    ".cpp": "cpp",
    ".cxx": "cpp",
    ".hpp": "cpp",
    ".rs": "rust",
    ".go": "go",
    ".py": "python",
    ".js": "javascript",
    ".mjs": "javascript",
    ".cjs": "javascript",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".java": "java",
    ".kt": "kotlin",
    ".scala": "scala",
    ".cs": "csharp",
    ".rb": "ruby",
    ".php": "php",
    ".swift": "swift",
    ".ex": "elixir",
    ".exs": "elixir",
    ".dart": "dart",
    ".zig": "zig",
    ".m": "objc",
    ".lua": "lua",
}
BINEXT = (".exe", ".dll", ".so", ".dylib", ".a", ".o", ".jar", ".class", ".pyc", ".wasm", ".node")
VENDOR = (
    "third_party",
    "third-party",
    "thirdparty",
    "vendor",
    "vendored",
    "deps",
    "external",
    "extern",
    "_vendor",
)
# fixed risky-construct patterns per language: (label, regex)
RISK = {
    "c": [
        ("unbounded-copy", r"\b(strcpy|strcat|sprintf|vsprintf|gets)\s*\("),
        ("alloca", r"\balloca\s*\("),
        ("system", r"\b(system|popen)\s*\("),
    ],
    "cpp": [
        ("raw-new-delete", r"\b(new\s+\w|delete(\[\])?\s+\w)"),
        ("reinterpret_cast", r"\breinterpret_cast\b"),
        ("unbounded-copy", r"\b(strcpy|sprintf|memcpy)\s*\("),
    ],
    "rust": [("unsafe", r"\bunsafe\s*(\{|fn|impl)"), ("transmute", r"\btransmute\b")],
    "go": [
        ("unsafe", r"\"unsafe\"|\bunsafe\.Pointer"),
        ("cgo", r"import\s+\"C\""),
        ("exec", r"\bexec\.Command"),
    ],
    "python": [
        ("eval-exec", r"\b(eval|exec)\s*\("),
        ("pickle", r"\bpickle\.loads?\b"),
        ("shell", r"shell\s*=\s*True|os\.system\("),
        ("yaml-load", r"yaml\.load\("),
        ("ffi", r"\b(ctypes|cffi)\b"),
    ],
    "javascript": [
        ("eval", r"\b(eval|new Function)\s*\("),
        ("child_process", r"child_process"),
        ("vm", r"require\(['\"]vm['\"]\)"),
    ],
    "java": [
        ("deserialization", r"ObjectInputStream|readObject\("),
        ("exec", r"Runtime\.getRuntime\(\)\.exec|ProcessBuilder"),
        ("unsafe-jni", r"sun\.misc\.Unsafe|\bnative\s+\w"),
    ],
    "csharp": [("unsafe", r"\bunsafe\b"), ("binaryformatter", r"BinaryFormatter"), ("pinvoke", r"DllImport")],
    "ruby": [
        ("eval", r"\b(eval|instance_eval|send)\b\s*\(?"),
        ("marshal", r"Marshal\.load"),
        ("shell", r"`[^`]+`|\bsystem\("),
    ],
    "php": [
        ("eval", r"\beval\s*\("),
        ("unserialize", r"\bunserialize\s*\("),
        ("shell", r"\b(exec|system|passthru|shell_exec)\s*\("),
    ],
}
RISK["typescript"] = RISK["javascript"]
RISK["kotlin"] = RISK["java"]
CI_PROBES = {  # label -> regex searched in CI config text; the fact is true or false
    "sanitizers": r"fsanitize|\bASAN\b|\bUBSAN\b|\bmiri\b|-race\b|valgrind|address,undefined",
    "fuzzing": r"\bfuzz|oss-fuzz|cifuzz|atheris|jazzer|hypothesis",
    "coverage": r"codecov|coveralls|\bcoverage\b|llvm-cov|tarpaulin|jacoco|\bnyc\b|--cov",
    "sast": r"codeql|semgrep|sonar|coverity|clang-tidy|cppcheck|clippy|golangci|staticcheck|"
    r"bandit|\bruff\b|eslint|spotbugs|errorprone|phpstan|psalm|rubocop|brakeman|mypy|pyright",
    "warnings_as_errors": r"-Werror|-D warnings|--max-warnings[ =]0|TreatWarningsAsErrors|/WX",
    "tests": r"\b(ctest|make check|cargo test|go test|pytest|tox|nox|npm test|yarn test|"
    r"pnpm test|mvn\b.*(test|verify)|gradle\w*\b.*(test|check)|dotnet test|rspec|"
    r"phpunit|mix test|flutter test|bazel test|meson test|jest|vitest|mocha|"
    r"(npm|yarn|pnpm) run test[\w:-]*|unittest)\b",
    "provenance": r"attest-build-provenance|slsa-github-generator|--provenance|sigstore|"
    r"cosign|id-token:\s*write|pypa/gh-action-pypi-publish|trusted.publish",
    "publish": r"npm publish|cargo publish|twine upload|gh-action-pypi-publish|"
    r"gradle\w*\b.*publish|mvn\b.*deploy|gem push|dotnet nuget push|gh release|"
    r"softprops/action-gh-release|goreleaser",
    "sbom": r"sbom|cyclonedx|spdx-sbom|syft",
    "dep_review": r"dependency-review-action|osv-scanner|cargo[- ]audit|cargo[- ]deny|"
    r"npm audit|pip-audit|govulncheck|snyk|trivy",
}
CI_MATRIX = {  # label -> regex searched in CI config text; the fact is the list of names found
    "os_matrix": r"ubuntu|macos|windows|freebsd|alpine|android|(?<![a-z])ios(?![a-z])",
    "arch_matrix": r"aarch64|arm64|armv7|riscv|ppc64|s390x|i686|wasm",
}
USES = r"uses:\s*[\"']?"  # an action or a reusable workflow; the reference can be in quotes
# provenance generator -> (regex in the CI text, what its provenance proves). "isolated": the
# maintainers cannot change the builder. "signed": the hosted build platform signs. "unsigned":
# the build writes provenance that the maintainers can change.
SLSA_GENERATORS = {
    "slsa-github-generator": (USES + r"slsa-framework/slsa-github-generator/\.github/workflows/", "isolated"),
    "github attestation": (USES + r"actions/attest(-build-provenance)?@", "signed"),
    "npm provenance": (r"npm publish\b[^\n]*--provenance|NPM_CONFIG_PROVENANCE", "signed"),
    "pypi trusted publishing": (USES + r"pypa/gh-action-pypi-publish@", "signed"),
    "buildkit provenance": (r"provenance:\s*(true|mode=)", "unsigned"),
    "gitlab runner metadata": (r"RUNNER_GENERATE_ARTIFACTS_METADATA", "unsigned"),
}
ACTION_USE = USES + r"([^\s#\"']+)[\"']?[ \t]*(?:#[ \t]*(\S+))?"  # reference, comment
RELEASE = r"v?\d+(\.\d+)*"
# file with a toolchain version -> (product name at endoflife.date, parts of a release cycle)
TOOLCHAIN_FILES = {
    ".nvmrc": ("nodejs", 1),
    ".node-version": ("nodejs", 1),
    ".python-version": ("python", 2),
    ".ruby-version": ("ruby", 2),
    "go.mod": ("go", 2),
}
SOURCE_ATTESTERS = USES + r"slsa-framework/(source-actions|slsa-source-poc|source-tool)"
SELF_HOSTED = r"runs-on:[^\n]*self-hosted|^\s*-\s*self-hosted\s*$"
VERIFY_DOCS = (
    r"^(readme|security|install|verify|verification|release)[^/]*$|"
    r"^docs?/[^/]+\.(md|rst|txt)$"
)
VERIFY_COMMANDS = (
    r"gh attestation verify|slsa-verifier|cosign verify[\w-]*|npm audit signatures|"
    r"pypi-attestations verify|sigstore verify|gpg --verify|minisign -V"
)
CI_FILES = (
    r"^\.github/workflows/[^/]+\.ya?ml$|^\.gitlab-ci\.yml$|^\.circleci/config\.yml$|"
    r"^azure-pipelines\.yml$|^\.travis\.yml$|^Jenkinsfile$|^\.cirrus\.yml$|"
    r"^\.buildkite/|^appveyor\.yml$|^\.woodpecker|^\.drone\.yml$|^\.forgejo/workflows/"
)
PATH_PROBES = {  # fact -> (regex searched in each path, case ignored; maximum number of paths)
    "security_policy": (r"^(\.github/|docs/)?security(\.md|\.txt|\.rst)?$", 8),
    "license_files": (r"^(licen[sc]e|copying|unlicense|notice)[^/]*$", 8),
    "nested_license_files": (r"/(licen[sc]e|copying)[^/]*$", 8),
    "governance": (r"(^|/)(governance|maintainers|owners|codeowners|steering)[^/]*$", 8),
    "funding": (r"(^|/)funding\.ya?ml$|sponsors", 8),
    "contributing": (r"(^|/)contributing[^/]*$", 8),
    "changelog": (r"^(changelog|changes|news|history|releasenotes)[^/]*$", 8),
    "coding_standard": (
        r"(^|/)(\.clang-format|\.editorconfig|rustfmt\.toml|"
        r"\.prettierrc[^/]*|\.rubocop\.yml|style[^/]*\.md)$",
        8,
    ),
    "sbom_files": (r"(sbom|\.spdx|cyclonedx|bom\.json)", 8),
    "fuzz_paths": (r"(^|/)fuzz(ing|ers?|_targets)?(/|$)|fuzz[^/]*\.(c|cc|cpp|rs|go|py)$", 8),
    "bench_paths": (r"(^|/)bench(marks?)?(/|$)", 4),
    "update_bot": (r"(^|/)(\.github/dependabot\.ya?ml|renovate\.json5?|\.renovaterc[^/]*)$", 8),
}
TEST_PATHS = r"(^|/)(tests?|spec|__tests__|testing)/|_test\.(go|py|rs|c|cc)$|\.test\.[jt]sx?$"
NOT_PRODUCT = r"(^|/)(tests?|spec|__tests__|examples?|docs?|bench\w*|fuzz\w*)/"
TOOLCHAIN_PINS = (
    "rust-toolchain",
    "rust-toolchain.toml",
    ".nvmrc",
    ".node-version",
    ".python-version",
    ".tool-versions",
    ".ruby-version",
    "global.json",
    ".bazelversion",
    "flake.nix",
    ".sdkmanrc",
    "mise.toml",
)
BUILD_SCRIPTS = ("build.rs", "binding.gyp", "setup.py", "configure.ac", "build.zig")
INSTALL_SCRIPTS = ("preinstall", "install", "postinstall")
NATIVE_LANGUAGES = ("c", "cpp", "zig", "objc", "rust", "go")
LICENSE_TEXTS = (  # (regex, identifier); without an identifier, group 1 of the match is it
    (r"JSON License|shall be used for Good, not Evil", "JSON (non-OSI)"),
    (r"SPDX-License-Identifier:\s*([\w.\-+ ()]+)", None),
    (r"Apache License\s+Version 2", "Apache-2.0"),
    (r"GNU AFFERO", "AGPL-3.0"),
    (r"GNU LESSER", "LGPL"),
    (r"GNU GENERAL PUBLIC LICENSE\s+Version 3", "GPL-3.0"),
    (r"GNU GENERAL PUBLIC LICENSE\s+Version 2", "GPL-2.0"),
    (r"Mozilla Public License,? v(ersion)?\.? ?2", "MPL-2.0"),
    (r"Permission is hereby granted, free of charge", "MIT"),
    (r"Boost Software License", "BSL-1.0"),
    (r"Redistribution and use in source and binary", "BSD"),
    (r"This is free and unencumbered software", "Unlicense"),
    (r"freely, subject to the following restrictions", "Zlib"),
    (r"Business Source License|Server Side Public|Elastic License", "NON-OSI-SOURCE-AVAILABLE"),
    (r"ISC License|Permission to use, copy, modify, and/or distribute", "ISC"),
)
OSV_ECOSYSTEM = {
    "npm": "npm",
    "pypi": "PyPI",
    "cargo": "crates.io",
    "go": "Go",
    "maven": "Maven",
    "nuget": "NuGet",
    "gem": "RubyGems",
    "composer": "Packagist",
    "hex": "Hex",
    "pub": "Pub",
}
DEPSDEV_SYSTEM = {"gem": "rubygems", "composer": "packagist"}  # where the name is not ours
# CI system -> (path flag of pipeline-check, path in the clone)
PIPELINE_CHECK = {
    "github": ("--gha-path", ".github/workflows"),
    "gitlab": ("--gitlab-path", ".gitlab-ci.yml"),
}
TARGET = re.compile(rf"({'|'.join(OSV_ECOSYSTEM)}):(.+?)(?:@([\w.\-+]+))?")


def sh(cmd, cwd=None, timeout=600):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout, errors="replace")
    if r.returncode:
        raise RuntimeError(f"{' '.join(cmd[:3])}: {r.stderr.strip()[:200]}")
    return r.stdout


def get(url, payload=None, timeout=20):
    h = dict(UA)
    # the token goes to that host only; a package name can contain the text "api.github.com"
    if urllib.parse.urlsplit(url).hostname == "api.github.com" and os.environ.get("GITHUB_TOKEN"):
        h["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    data = None
    if payload is not None:
        data, h["Content-Type"] = json.dumps(payload).encode(), "application/json"
    with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=h), timeout=timeout) as r:
        return json.loads(r.read().decode())


def days(iso):
    try:
        d = datetime.fromisoformat(str(iso).replace("Z", "+00:00"))
        return (NOW - (d if d.tzinfo else d.replace(tzinfo=timezone.utc))).days
    except Exception:
        return None


def within(iso, n):
    """True if the date is at most n days old. A date that cannot be read is not."""
    d = days(iso)
    return d is not None and d <= n


def free_mail(domain):
    """True for a personal mail domain. A pattern must start the domain or one of its labels."""
    return any(domain.startswith(f) or "." + f in domain for f in FREE_MAIL)


def norm_repo(u):
    if not u:
        return None
    u = re.sub(r"^(git\+|scm:git:)", "", str(u)).replace("git://", "https://")
    u = re.sub(r"^git@([^:]+):", r"https://\1/", u).replace("ssh://git@", "https://")
    m = re.match(r"(https?://[^/]+)/([^\s#]+)", u)
    if not m:
        return None
    host, segs = m.group(1), [x for x in m.group(2).split("/") if x]
    if "gitlab" in host or "googlesource" in host:  # the project path can be deep; a page ends it
        segs = segs[: next((i for i, x in enumerate(segs) if x in DEEP_PATH_PAGES), len(segs))]
    else:
        segs = segs[:2]
    return re.sub(r"\.git$", "", "/".join([host, *segs])) if len(segs) >= 2 else None


def pypi_repo(urls):
    """The source repository from the project URLs of PyPI. A sponsor or profile page is not."""
    return next(
        (
            norm_repo(u)
            for k, u in sorted(urls.items())
            if re.search(r"github|gitlab|codeberg|bitbucket", u or "")
            and not re.search(r"//[^/]+/(sponsors|orgs|users)/", u)
        ),
        None,
    )


# ---------- registries: one normalized record ----------
def install_scripts(pkg):
    """The npm scripts of a package manifest that run at installation."""
    return sorted(k for k in (pkg.get("scripts") or {}) if k in INSTALL_SCRIPTS)


def last_ten(dates):
    return sorted(dates)[-10:]


def npm_license(vd):
    lic = vd.get("license") or vd.get("licenses")
    lic = [lic] if isinstance(lic, (str, dict)) else lic or []
    return " OR ".join(sorted(str(x.get("type") if isinstance(x, dict) else x) for x in lic)) or None


def registry_npm(name, version, with_deps=True):
    d = get(f"https://registry.npmjs.org/{name.replace('/', '%2f')}")
    v = version or d.get("dist-tags", {}).get("latest")
    vd = d.get("versions", {}).get(v, {})
    times = {k: t for k, t in d.get("time", {}).items() if k not in ("created", "modified")}
    repo = vd.get("repository")
    return {
        "version": v,
        "license": npm_license(vd),
        "repo": norm_repo(repo.get("url") if isinstance(repo, dict) else repo),
        "released": times.get(v),
        "versions": len(times),
        "deprecated": bool(vd.get("deprecated")),
        "publishers": len(d.get("maintainers", [])),
        "install_scripts": install_scripts(vd),
        "provenance": bool(vd.get("dist", {}).get("attestations")),
        "runtime_deps": sorted((vd.get("dependencies") or {}).keys()),
        "last_releases": last_ten(times.values()),
    }


def registry_pypi(name, version, with_deps=True):
    d = get(
        f"https://pypi.org/pypi/{name}/json"
        if not version
        else f"https://pypi.org/pypi/{name}/{version}/json"
    )
    i, files = d["info"], d.get("urls", [])
    rel = {k: v[0]["upload_time_iso_8601"] for k, v in d.get("releases", {}).items() if v}
    return {
        "version": i["version"],
        "license": i.get("license_expression") or (i.get("license") or "")[:60] or None,
        "repo": pypi_repo(i.get("project_urls") or {}),
        "released": files[0]["upload_time_iso_8601"] if files else None,
        "versions": len(rel),
        "deprecated": bool(i.get("yanked")),
        "has_sdist": any(f["packagetype"] == "sdist" for f in files),
        "native_wheels": any(
            "none-any" not in f["filename"] for f in files if f["packagetype"] == "bdist_wheel"
        ),
        "runtime_deps": sorted(
            {re.split(r"[ ;<>=!~\[(]", x)[0] for x in (i.get("requires_dist") or []) if "extra ==" not in x}
        ),
        "last_releases": last_ten(rel.values()),
    }


def registry_cargo(name, version, with_deps=True):
    d = get(f"https://crates.io/api/v1/crates/{name}")
    c, vs = d["crate"], d.get("versions", [])
    v = version or c.get("max_stable_version") or c.get("max_version")
    vd = next((x for x in vs if x["num"] == v), vs[0] if vs else {})
    r = {
        "version": v,
        "license": vd.get("license"),
        "repo": norm_repo(c.get("repository")),
        "released": vd.get("created_at"),
        "versions": len(vs),
        "deprecated": bool(vd.get("yanked")),
        "downloads_recent": c.get("recent_downloads"),
        "last_releases": last_ten(x["created_at"] for x in vs),
    }
    if with_deps:  # one more request; the dependency screen does not read the result
        try:
            dd = get(f"https://crates.io/api/v1/crates/{name}/{v}/dependencies")
            r["runtime_deps"] = sorted(
                x["crate_id"] for x in dd["dependencies"] if x["kind"] == "normal" and not x["optional"]
            )
        except Exception:
            pass
    return r


def depsdev_package(eco, name):
    return (
        f"https://api.deps.dev/v3/systems/{DEPSDEV_SYSTEM.get(eco, eco)}/packages/"
        f"{urllib.parse.quote(name, safe='')}"
    )


def depsdev_version(eco, name, version):
    return f"{depsdev_package(eco, name)}/versions/{urllib.parse.quote(version, safe='')}"


def registry_depsdev(eco, name, version):
    vs = get(depsdev_package(eco, name)).get("versions", [])
    dv = next((x for x in vs if x.get("isDefault")), vs[-1] if vs else {})
    return {
        "version": version or dv.get("versionKey", {}).get("version"),
        "versions": len(vs),
        "released": dv.get("publishedAt"),
        "last_releases": last_ten(x["publishedAt"] for x in vs if x.get("publishedAt")),
    }


REGISTRIES = {"npm": registry_npm, "pypi": registry_pypi, "cargo": registry_cargo}


def registry(eco, name, version, with_deps=True):
    """One record of the same shape for each registry. deps.dev serves every other ecosystem."""
    fields = (
        REGISTRIES[eco](name, version, with_deps)
        if eco in REGISTRIES
        else registry_depsdev(eco, name, version)
    )
    return {"ecosystem": eco, "name": name, **fields}


# ---------- git history ----------
def git(src, *args, timeout=600):
    return sh(["git", *args], src, timeout)


def git_rows(src, *args):
    """The output lines of a git command, each split at the unit separator."""
    return [line.split("\x1f") for line in git(src, *args).splitlines() if line]


def clone(url, dest):
    if os.path.isdir(os.path.join(dest, ".git")):  # an old clone must follow the remote head
        try:
            git(dest, "remote", "set-url", "origin", url)
            try:
                git(dest, "fetch", "-q", "--shallow-since=25 months ago", "origin", "HEAD", timeout=900)
            except Exception:
                git(dest, "fetch", "-q", "--depth", "1", "origin", "HEAD", timeout=900)
            git(dest, "reset", "-q", "--hard", "FETCH_HEAD")
            return "reused, updated to the remote head"
        except Exception as e:
            return "reused, not updated: " + str(e)[:120]
    try:
        sh(
            ["git", "clone", "-q", "--filter=blob:none", "--shallow-since=25 months ago", url, dest],
            timeout=900,
        )
        return "shallow-since-25mo"
    except Exception:
        sh(["git", "clone", "-q", "--depth", "1", url, dest], timeout=900)
        return "depth-1 (no commit in 25 months, or host rejects shallow-since)"


def bus_factor(ranked, total):
    """The smallest number of authors who together made 80 % of the commits."""
    cum = 0
    for n, (_, commits) in enumerate(ranked, 1):
        cum += commits
        if cum / total >= 0.8:
            return n
    return len(ranked)


def org_commits(rows):
    """Commits for each employer domain. A personal mail domain is not an employer."""
    doms = Counter()
    for _, _name, mail in rows:
        d = mail.split("@")[-1].lower()
        if d and not free_mail(d):
            doms[".".join(d.split(".")[-2:])] += 1
    return doms


def commit_facts(src):
    head, last, authored = git(src, "log", "-1", "--format=%H\x1f%cI\x1f%aI").strip().split("\x1f")
    rows = [
        r
        for r in git_rows(src, "log", "--no-merges", "--since=24 months ago", "--format=%aI\x1f%aN\x1f%aE")
        if len(r) == 3 and not BOTS.search(r[1] + r[2])
    ]
    age = [days(r[0]) for r in rows]
    cnt = Counter(r[1] for r in rows)
    ranked = sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))
    total, doms = len(rows) or 1, org_commits(rows)
    return {
        "head": head,
        "last_commit": last,
        "days_since_last_commit": days(last),
        "last_commit_authored": authored,
        "commits_90d": sum(a is not None and a <= 90 for a in age),
        "commits_12m": sum(a is not None and a <= 365 for a in age),
        "commits_24m": len(rows),
        "authors_24m": len(cnt),
        "bus_factor_24m": bus_factor(ranked, total),
        "top_authors_24m": [{"name": n, "share_pct": round(100 * c / total)} for n, c in ranked[:5]],
        "orgs_over_5pct_24m": sorted(d for d, c in doms.items() if c / total >= 0.05),
        "top_org_share_pct": round(100 * max(doms.values()) / total) if doms else 0,
    }


def release_tags(refs):
    """The release tags in the output of git ls-remote, newest version first.

    The sort of git puts 2.3.3 below v2.0.0, so the versions are compared here."""
    names = (line.split("refs/tags/")[-1] for line in refs.splitlines() if "refs/tags/" in line)
    return sorted((t for t in names if re.fullmatch(r"v?\d+(\.\d+)+", t)), key=version_tuple, reverse=True)


def fetch_newest_tags(src):
    """Fetch the five newest release tags that the clone does not have.

    A clone of the default branch has no tag of a release that was made on a different branch."""
    try:
        here = set(git(src, "tag", "-l").split())
        for n in release_tags(git(src, "ls-remote", "--tags", "--refs", "origin"))[:5]:
            if n not in here:
                git(src, "fetch", "-q", "--depth", "1", "origin", "tag", n, timeout=120)
    except Exception:
        pass


def tag_facts(src):
    tags = git_rows(
        src,
        "for-each-ref",
        "refs/tags",
        "--sort=-creatordate",
        "--format=%(refname:short)\x1f%(creatordate:iso-strict)\x1f%(objecttype)"
        "\x1f%(objectname)\x1f%(*objectname)",  # an annotated tag has the commit in the last field
    )[:15]
    out = {
        "tags": [
            {"tag": t[0], "date": t[1], "annotated": t[2] == "tag", "commit": t[4] or t[3]}
            for t in tags
            if len(t) == 5
        ]
    }
    out["days_since_last_tag"] = days(tags[0][1]) if tags and len(tags[0]) == 5 else None
    recent = [t["tag"] for t in out["tags"] if within(t["date"], 730)]
    out["tags_24m"] = len(recent)
    try:  # without a revision, git log reads HEAD
        out["release_actors_24m"] = (
            len({n.strip() for n in git(src, "log", "--no-walk", "--format=%cN", *recent).splitlines()})
            if recent
            else 0
        )
    except Exception:
        out["release_actors_24m"] = None
    try:
        sig = git(src, "tag", "-l", "--format=%(contents:signature)", tags[0][0])
        out["latest_tag_signed"] = "BEGIN" in sig
    except Exception:
        out["latest_tag_signed"] = None
    return out


def history(src):
    out = commit_facts(src)
    fetch_newest_tags(src)
    out.update(tag_facts(src))
    return out


# ---------- tree scan ----------
def read(p, lim=400_000):
    try:
        with open(p, errors="replace") as f:
            return f.read(lim)
    except Exception:
        return ""


def matching(files, rx, lim=8):
    """The first paths, in sorted order, that match the pattern. Case does not count."""
    return sorted(f for f in files if re.search(rx, f, re.I))[:lim]


def named(files, names, lim=8):
    """The first paths, in sorted order, whose file name is one of the names."""
    return sorted(f for f in files if f.split("/")[-1] in names)[:lim]


def lang_of(path):
    return LANG.get(os.path.splitext(path)[1].lower())


def in_vendor(path):
    return any(seg.lower() in VENDOR for seg in path.split("/")[:-1])


def vendored_dirs(files):
    found = set()
    for f in files:
        parts = f.split("/")
        found.update(
            "/".join(parts[: i + 2])
            for i, seg in enumerate(parts[:-1])
            if seg.lower() in VENDOR and len(parts) > i + 2
        )
    return sorted(found)[:25]


def path_facts(files):
    """What the file names alone tell."""
    root = [f for f in files if "/" not in f]
    t = {key: matching(files, rx, lim) for key, (rx, lim) in PATH_PROBES.items()}
    t["file_count"] = len(files)
    t["test_paths"] = sorted({f.split("/")[0] for f in files if re.search(TEST_PATHS, f)})[:8]
    t["lockfiles"] = named(files, LOCKS)
    t["manifests"] = sorted(f for f in root if f in MANIFESTS)
    t["toolchain_pins"] = sorted(f for f in root if f in TOOLCHAIN_PINS)
    t["ecosystems"] = sorted({MANIFESTS[f] for f in t["manifests"]})
    t["submodules"] = any(f.lower() == ".gitmodules" for f in files)
    t["vendored_dirs"] = vendored_dirs(files)
    t["checked_in_binaries"] = sorted(f for f in files if f.lower().endswith(BINEXT))[:10]
    t["build_scripts"] = named(files, BUILD_SCRIPTS)
    return t


def language_facts(files, ecosystems):
    loc = Counter(lang_of(f) for f in files if not in_vendor(f))
    loc.pop(None, None)
    by_language = dict(sorted(loc.items(), key=lambda kv: (-kv[1], kv[0])))
    primary = next(iter(by_language), None)
    if primary in NATIVE_LANGUAGES and len(ecosystems) > 1:  # package.json is tooling there
        ecosystems = [e for e in ecosystems if e != "npm"]
    return {"source_files_by_language": by_language, "primary_language": primary, "ecosystems": ecosystems}


def risk_facts(src, files, langs):
    """Size and risky constructs of the first-party source, in at most 4000 files."""
    product = (
        f for f in files if lang_of(f) in langs and not in_vendor(f) and not re.search(NOT_PRODUCT, f, re.I)
    )
    risk, sloc = Counter(), 0
    for f in itertools.islice(product, 4000):
        txt = read(os.path.join(src, f))
        sloc += txt.count("\n")
        for label, rx in RISK.get(lang_of(f), []):
            n = sum(1 for _ in re.finditer(rx, txt))
            if n:
                risk[f"{lang_of(f)}:{label}"] += n
    return {"first_party_sloc": sloc, "risky_constructs": dict(sorted(risk.items()))}


def slsa_facts(text):
    """What the CI text shows about provenance, for the SLSA Build and Source tracks."""
    kinds = {name: kind for name, (rx, kind) in SLSA_GENERATORS.items() if re.search(rx, text)}
    return {
        "generators": sorted(kinds),
        "strongest": next((k for k in ("isolated", "signed", "unsigned") if k in kinds.values()), "none"),
        "oidc": bool(re.search(r"id-token:\s*write", text)),
        "self_hosted": bool(re.search(SELF_HOSTED, text, re.M)),
        "source_attestation": bool(re.search(SOURCE_ATTESTERS, text)),
    }


def verification_docs(src, files):
    """Where the documents tell a consumer how to verify a release: "file: command"."""
    found = set()
    for f in sorted(f for f in files if re.search(VERIFY_DOCS, f, re.I))[:30]:
        found.update(
            f"{f}: {m.lower()}"
            for m in re.findall(VERIFY_COMMANDS, read(os.path.join(src, f), 200_000), re.I)
        )
    return sorted(found)[:8]


def version_tuple(v):
    m = re.match(r"v?(\d+(?:\.\d+)*)", v or "")
    return tuple(int(x) for x in m.group(1).split(".")) if m else None


def action_refs(text):
    """The actions of other projects that the CI uses: name, reference, version, kind of pin."""
    rows = {}
    for ref, note in re.findall(ACTION_USE, text):
        if ref.startswith(("./", "docker://")) or "@" not in ref:
            continue
        path, at = ref.rsplit("@", 1)
        digest = bool(re.fullmatch(r"[0-9a-f]{40}", at))
        version = next((v for v in ((note,) if digest else (at,)) if re.fullmatch(RELEASE, v)), None)
        name = "/".join(path.split("/")[:2])
        rows[(name, at)] = {
            "kind": "action",
            "name": name,
            "ref": at[:12],
            "version": version,
            "pin": "digest" if digest else "tag" if version else "branch",
        }
    return [rows[k] for k in sorted(rows)]


def toolchain_versions(src, files):
    """The toolchain versions that the files in the root of the clone pin."""
    rows = []
    for f in sorted(f for f in files if f in TOOLCHAIN_FILES):
        m = re.search(
            r"^go\s+(\d+(?:\.\d+)*)" if f == "go.mod" else r"(\d+(?:\.\d+)*)",
            read(os.path.join(src, f), 4000),
            re.M,
        )
        rows.append(
            {
                "kind": "toolchain",
                "name": TOOLCHAIN_FILES[f][0],
                "ref": f,
                "version": m.group(1) if m else None,
                "pin": "file",
            }
        )
    return rows


def base_images(src, files):
    """The base images of the container files in the root of the clone."""
    rows = {}
    for f in sorted(f for f in files if re.fullmatch(r"(Dockerfile|Containerfile)[^/]*", f))[:5]:
        for image in re.findall(r"^FROM\s+(?:--\S+\s+)*(\S+)", read(os.path.join(src, f)), re.M | re.I):
            name, _, digest = image.partition("@")
            tag = name.rsplit(":", 1)[1] if ":" in name.split("/")[-1] else None
            if image.lower() != "scratch" and "$" not in image:
                rows[image] = {
                    "kind": "image",
                    "name": name.rsplit(":", 1)[0] if tag else name,
                    "ref": f,
                    "version": tag,
                    "pin": "digest" if digest else "tag" if tag and tag != "latest" else "branch",
                }
    return [rows[k] for k in sorted(rows)]


def ci_facts(src, files):
    ci_files = sorted(f for f in files if re.search(CI_FILES, f))
    text = "\n".join(read(os.path.join(src, f), 200_000) for f in ci_files[:60])
    ci = {"files": ci_files[:30], "count": len(ci_files)}
    for label, rx in CI_PROBES.items():
        ci[label] = bool(re.search(rx, text, re.I))
    for label, rx in CI_MATRIX.items():
        ci[label] = sorted({m.lower() for m in re.findall(rx, text, re.I)})[:8]
    ext = [u for u in re.findall(USES + r"([^\s#\"']+)", text) if not u.startswith("./") and "@" in u]
    ci["publish"] = ci["publish"] or any(re.search(r"publish|release|deploy", f, re.I) for f in ci_files)
    ci["actions_total"] = len(ext)
    ci["actions_sha_pinned"] = sum(bool(re.search(r"@[0-9a-f]{40}$", u)) for u in ext)
    ci["dangerous_triggers"] = bool(re.search(r"pull_request_target|workflow_run", text))
    ci["compilers"] = sorted({m.lower() for m in re.findall(r"\b(gcc|clang|msvc)\b", text, re.I)})
    ci["slsa"] = slsa_facts(text)
    ci["action_refs"] = action_refs(text)
    return ci


def manifest_facts(src):
    """Direct runtime dependencies from the manifests, for an ecosystem without a registry record."""
    out, deps = {}, []
    package_json = read(os.path.join(src, "package.json"))
    if package_json:
        try:
            pkg = json.loads(package_json)
            deps += sorted((pkg.get("dependencies") or {}).keys())
            out["npm_install_scripts"] = install_scripts(pkg)
        except Exception:
            pass
    deps += sorted(
        set(
            re.findall(
                r"^\s*([\w.\-/]+\.[\w.\-/]+)\s+v[\w.\-+]+\s*$", read(os.path.join(src, "go.mod")), re.M
            )
        )
    )
    m = re.search(
        r"^\[dependencies\]\s*\n(.*?)(?=^\[|\Z)", read(os.path.join(src, "Cargo.toml")), re.S | re.M
    )
    if m:
        deps += sorted(set(re.findall(r"^([\w\-]+)\s*=", m.group(1), re.M)))
    out["manifest_runtime_deps"] = deps[:80]
    return out


def tree(src):
    files = git(src, "ls-files").splitlines()
    t = path_facts(files)
    t["submodule_list"] = re.findall(r"url\s*=\s*(\S+)", read(os.path.join(src, ".gitmodules")))
    t.update(language_facts(files, t["ecosystems"]))
    t.update(risk_facts(src, files, list(t["source_files_by_language"])[:2]))
    t["ci"] = ci_facts(src, files)
    t["verification_docs"] = verification_docs(src, files)
    t["toolchain_versions"] = toolchain_versions(src, files)
    t["base_images"] = base_images(src, files)
    t.update(manifest_facts(src))
    return t


def spdx_guess(src, names, every=False):
    """The license that the first two files name: the first match, or with every, all of them."""
    found = []
    for n in names[:2]:
        s = read(os.path.join(src, n), 40000 if every else 6000)
        for rx, sid in LICENSE_TEXTS:
            m = re.search(rx, s, re.I)
            if m and every:
                found.append(sid or m.group(1).strip())
            elif m and sid != "JSON (non-OSI)":
                return sid or m.group(1).strip()
    return sorted(set(found)) if every else None


# ---------- one section of facts.json each ----------
def opt(args, flag, default=None):
    return args[args.index(flag) + 1] if flag in args else default


def load_facts(path):
    try:
        with open(path) as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def reusable(old, target, lite, max_age):
    """True if the old facts answer the same request, are of this collector and are young enough."""
    return (
        isinstance(old, dict)
        and old.get("collector") == COLLECTOR
        and old.get("target") == target
        and (lite or "history" in old)
        and within(old.get("collected_at"), int(max_age))
    )


def add_depsdev_version(F, eco, name, version, repo):
    """Record what deps.dev says about the version. Return the repository, known or found there."""
    try:
        dv = get(depsdev_version(eco, name, version))
        F["depsdev_version"] = {
            "licenses": dv.get("licenses"),
            "deprecated": dv.get("isDeprecated"),
            "advisories": sorted(k["id"] for k in dv.get("advisoryKeys", [])),
            "slsa_provenance": bool(dv.get("slsaProvenances")),
            "attestations": bool(dv.get("attestations")),
        }
        # registries read through deps.dev give no repository in the package record
        return repo or next(
            (norm_repo(x.get("url")) for x in dv.get("links") or [] if x.get("label") == "SOURCE_REPO"), None
        )
    except Exception as e:
        F["errors"]["depsdev_version"] = str(e)[:120]
        return repo


def resolve_target(F, target, repo_given):
    """Record the registry facts of a package target. Return (ecosystem, name, repository)."""
    m = TARGET.fullmatch(target)
    if not m:
        return None, None, norm_repo(target if "://" in target else "https://github.com/" + target) or target
    eco, name, version = m.groups()
    repo = None
    try:
        F["registry"] = registry(eco, name, version)
        repo, version = F["registry"].get("repo"), F["registry"].get("version")
    except Exception as e:
        F["errors"]["registry"] = (
            str(e)[:160] + " | registry unreachable from this shell: "
            "rerun with --repo <source repo URL>; take version and "
            "release dates from git tags"
        )
    repo = norm_repo(repo_given) or repo
    if eco == "go" and not repo and name.startswith(("github.com/", "gitlab.com/")):
        repo = "https://" + "/".join(name.split("/")[:3])
    if version:
        repo = add_depsdev_version(F, eco, name, version, repo)
    return eco, name, repo


def tool_json(cmd, cwd=None, out_file=None, timeout=300):
    """Run a helper program that reports in JSON. Exit code 1 is a failed gate, not an error."""
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout, errors="replace")
    if r.returncode not in (0, 1):
        raise RuntimeError(f"exit code {r.returncode}: {r.stderr.strip()[-200:]}")
    if out_file:
        with open(out_file, encoding="utf-8") as f:
            return json.load(f)
    return json.loads(r.stdout)


def pipeline_check_record(report):
    """The failed checks of one pipeline-check report, for each SLSA control."""
    failed = {}
    for finding in report.get("findings", []):
        if not finding.get("passed"):
            for control in finding.get("controls") or [{"control_id": "no SLSA control"}]:
                failed.setdefault(control["control_id"], set()).add(finding["check_id"])
    score = report.get("score") or {}
    return {
        "version": report.get("tool_version"),
        "score": score.get("score"),
        "grade": score.get("grade"),
        "complete": (report.get("scan_status") or {}).get("complete"),
        "failed_checks": {k: sorted(v) for k, v in sorted(failed.items())},
    }


def add_pipeline_check(F, src):
    """Optional helper pipeline-check: the CI files against the SLSA Build track, without network."""
    exe = shutil.which("pipeline_check") or shutil.which("pipeline-check")
    found = {ci: x for ci, x in PIPELINE_CHECK.items() if os.path.exists(os.path.join(src, x[1]))}
    if not exe or not found:
        return
    try:  # the CI system is always named: without a name the tool can read a cloud account
        F["pipeline_check"] = {
            ci: pipeline_check_record(
                tool_json(
                    [
                        exe,
                        "--pipeline",
                        ci,
                        flag,
                        path,
                        "--standard",
                        "slsa",
                        "--no-resolve-remote",
                        "--output",
                        "json",
                    ],
                    cwd=src,
                )
            )
            for ci, (flag, path) in sorted(found.items())
        }
    except Exception as e:
        F["errors"]["pipeline_check"] = str(e)[:200]


def plumber_record(report):
    controls = {
        v["controlName"]: {
            "status": v.get("status"),
            "issues": sorted({i.get("code", "") for i in v.get("issues") or []}),
        }
        for v in report.values()
        if isinstance(v, dict) and v.get("controlName")
    }
    return {
        "score": report.get("plumberScore"),
        "ci_valid": report.get("ciValid"),
        "commit": report.get("headCommitSha"),
        "controls": dict(sorted(controls.items())),
    }


def signed_in(host_path):
    """True if plumber can sign in to the host of the repository: a token, or a gh login."""
    host = host_path.split("/")[0]
    github = ("GH_TOKEN", "GITHUB_TOKEN") if host == "github.com" else ("GH_ENTERPRISE_TOKEN",)
    # a host with a different name can be GitLab or GitHub Enterprise: plumber finds out
    names = github if host == "github.com" else (*github, "GITLAB_TOKEN")
    if any(os.environ.get(n) for n in names):
        return True
    gh = shutil.which("gh")
    return (
        bool(gh)
        and subprocess.run(
            [gh, "auth", "token", "--hostname", host], capture_output=True, timeout=30
        ).returncode
        == 0
    )


def add_plumber(F, host_path):
    """Optional helper plumber: the pipeline and the settings of the repository, through its API."""
    exe = shutil.which("plumber")
    if not exe or not signed_in(host_path):
        return
    try:
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "plumber.json")
            F["plumber"] = plumber_record(
                tool_json([exe, "analyze", host_path, "--output", out, "--print=false"], out_file=out)
            )
    except Exception as e:
        F["errors"]["plumber"] = str(e)[:200]


def latest_release_tag(repo_url):
    """The newest release tag of a repository, read without an API."""
    tags = release_tags(sh(["git", "ls-remote", "--tags", "--refs", repo_url], timeout=60))
    return tags[0] if tags else None


def affects(vuln, version):
    """True if an OSV advisory applies to the version. A tag like v4 is the newest 4.x release."""
    used = version_tuple(version)
    if len(used) == 1:
        used += (10**9,)
    for affected in vuln.get("affected", []):
        if version.lstrip("v") in affected.get("versions", []):
            return True
        # a range without an end can have its end here, for example "< 3.0.0"
        limit = re.fullmatch(
            r"\s*(<=?)\s*v?(\d+(?:\.\d+)*)\s*",
            (affected.get("database_specific") or {}).get("last_known_affected_version_range") or "",
        )
        for r in affected.get("ranges", []):
            if r.get("type") in ("ECOSYSTEM", "SEMVER") and in_range(r.get("events", []), used, limit):
                return True
    return False


def in_range(events, used, limit=None):
    """True if the version is in one of the intervals that the events of an OSV range make."""
    start = None
    for e in events:
        if "introduced" in e:
            start = version_tuple(e["introduced"]) or ()
        elif start is not None:
            fixed, last = version_tuple(e.get("fixed")), version_tuple(e.get("last_affected"))
            if (fixed and start <= used < fixed) or (last and start <= used <= last):
                return True
            start = None
    if start is None or used < start:
        return False
    if limit:  # the interval has no end in the events
        end = version_tuple(limit.group(2))
        return used <= end if limit.group(1) == "<=" else used < end
    return True


def stack_status(issues):
    if "vulnerable" in issues or "end of life" in issues:
        return "Red"
    return "Amber" if issues else "Green"


def screen_action(row, lookup):
    """Rate one action: a floating reference, how old it is, and what the advisories say."""
    vulns, latest = lookup(row["name"])
    issues = ["floating reference"] if row["pin"] == "branch" else []
    notes = []
    if row["version"]:
        hits = sorted(v["id"] for v in vulns if affects(v, row["version"]))
        if hits:
            issues.append("vulnerable")
            notes.append("known vulnerability in this version: " + ", ".join(hits[:3]))
        behind = (version_tuple(latest)[0] - version_tuple(row["version"])[0]) if latest else 0
        if behind > 0:
            issues.append("outdated")
            notes.append(f"{behind} major version(s) behind {latest}")
    if len(vulns) >= 2:
        issues.append("advisory history")
        notes.append(f"{len(vulns)} advisories in its history")
    if row["pin"] == "branch":
        notes.insert(0, "the reference can change")
    rated = row["version"] or row["pin"] == "branch"
    return {
        **row,
        "latest": latest,
        "advisories": len(vulns),
        "issues": issues,
        "status": stack_status(issues) if rated else "unknown",
        "why": "; ".join(notes) if rated else "the version behind the digest is not known",
    }


def screen_toolchain(row, cycles_of):
    product, parts = next(v for v in TOOLCHAIN_FILES.values() if v[0] == row["name"])
    used = version_tuple(row["version"])
    if not used or len(used) < parts:
        return {**row, "issues": [], "status": "n/a", "why": "no exact version in the file"}
    cycle = ".".join(str(x) for x in used[:parts])
    found = next((c for c in cycles_of(product) if str(c.get("cycle")) == cycle), None)
    if not found:
        return {**row, "issues": [], "status": "unknown", "why": f"release {cycle} is not known"}
    eol = found.get("eol")
    ended = isinstance(eol, str) and eol <= NOW.date().isoformat()
    return {
        **row,
        "latest": found.get("latest"),
        "issues": ["end of life"] if ended else [],
        "status": "Red" if ended else "Green",
        "why": f"end of life since {eol}" if ended else "",
    }


def screen_image(row):
    floating = row["pin"] == "branch"
    return {
        **row,
        "issues": ["floating reference"] if floating else [],
        "status": "Amber" if floating else "Green",
        "why": "the tag can change; no vulnerability data for images"
        if floating
        else "no vulnerability data for images",
    }


def cached(fetch):
    """Call fetch one time for each key. A failure is kept as the result."""
    results = {}

    def lookup(key):
        if key not in results:
            try:
                results[key] = fetch(key)
            except Exception as e:
                results[key] = e
        if isinstance(results[key], Exception):
            raise results[key]
        return results[key]

    return lookup


def add_base_stack(F):
    """Screen what makes the library: the CI actions, the toolchain and the base images."""
    t = F.get("tree") or {}
    actions = (t.get("ci") or {}).get("action_refs", [])
    names = sorted({r["name"] for r in actions})[:12]
    advisories = cached(
        lambda name: (
            get(
                "https://api.osv.dev/v1/query", {"package": {"name": name, "ecosystem": "GitHub Actions"}}
            ).get("vulns", []),
            latest_release_tag("https://github.com/" + name),
        )
    )
    cycles = cached(lambda product: get(f"https://endoflife.date/api/{product}.json"))
    rows = []
    for row, screen in (
        [(r, lambda r: screen_action(r, advisories)) for r in actions if r["name"] in names]
        + [(r, lambda r: screen_toolchain(r, cycles)) for r in t.get("toolchain_versions", [])]
        + [(r, screen_image) for r in t.get("base_images", [])]
    ):
        try:
            rows.append(screen(row))
        except Exception as e:
            rows.append({**row, "issues": [], "status": "unknown", "why": str(e)[:80]})
    F["base_stack"] = {
        "depth": f"{len(names)} of {len({r['name'] for r in actions})} CI actions, alphabetically; "
        "toolchain versions and base images from files in the root; advisories from OSV, "
        "end of life from endoflife.date",
        "rows": rows,
    }


def add_source(F, repo, src, detect):
    try:
        F["clone"] = clone(repo, src)
        F["history"] = history(src)
        F["tree"] = tree(src)
        F["tree"]["license_spdx_guess"] = spdx_guess(src, F["tree"]["license_files"])
        F["tree"]["licenses_named_in_root_file"] = spdx_guess(src, F["tree"]["license_files"], every=True)
        if detect and F["tree"]["ecosystems"]:
            F["detected_ecosystems"] = F["tree"]["ecosystems"]
    except Exception as e:
        F["errors"]["clone"] = str(e)[:300]
        return
    add_base_stack(F)
    add_pipeline_check(F, src)


def fetch_fact(F, key, url, keep, extract=None):
    """Store keep(response) as F[key]. Record a failure; with extract, plan the URL for the web tool."""
    try:
        F[key] = keep(get(url))
    except Exception as e:
        F["errors"][key] = str(e)[:120]
        if extract:
            F["fetch_plan"].append({"id": key, "url": url, "extract": extract})


def scorecard_record(d):
    return {
        "score": d.get("score"),
        "date": d.get("date"),
        "checks": {c["name"]: c.get("score") for c in d.get("checks", [])},
    }


def depsdev_project_record(d):
    return {
        "stars": d.get("starsCount"),
        "license": d.get("license"),
        "open_issues": d.get("openIssuesCount"),
        "oss_fuzz": d.get("ossFuzz"),
    }


def github_record(r):
    keys = ("archived", "fork", "stargazers_count", "open_issues_count", "pushed_at")
    return {**{k: r.get(k) for k in keys}, "license": (r.get("license") or {}).get("spdx_id")}


def add_project_sources(F, host_path):
    """Remote JSON sources about the repository. A failed scorecard request goes to fetch_plan."""
    fetch_fact(
        F,
        "scorecard",
        f"https://api.scorecard.dev/projects/{host_path}",
        scorecard_record,
        extract="overall score, date, every check name with its score",
    )
    fetch_fact(
        F,
        "depsdev_project",  # direct only: deps.dev refuses the web tool
        "https://api.deps.dev/v3/projects/" + urllib.parse.quote(host_path, safe=""),
        depsdev_project_record,
    )
    if host_path.startswith("github.com/"):
        api = "https://api.github.com/repos/" + host_path.split("/", 1)[1]
        fetch_fact(F, "github", api, github_record)
        fetch_fact(  # can a reporter send a vulnerability report in private
            F, "github_private_reports", api + "/private-vulnerability-reporting", lambda d: d.get("enabled")
        )


def osv_record(vulns, package):
    vulns = sorted(vulns, key=lambda v: v.get("published") or "", reverse=True)
    return {
        "count": len(vulns),
        "query": package,
        "recent": [
            {
                "id": v["id"],
                "aliases": sorted(v.get("aliases", []))[:3],
                "published": (v.get("published") or "")[:10],
                "summary": (v.get("summary") or "")[:120],
                "fixed": sorted(
                    {
                        e.get("fixed")
                        for a in v.get("affected", [])
                        for r in a.get("ranges", [])
                        for e in r.get("events", [])
                        if e.get("fixed")
                    }
                )[:4],
            }
            for v in vulns[:25]
        ],
    }


def advisory_fetch_plan(keyword, host_path):
    """What the web tool reads when OSV does not answer."""
    plan = [
        {
            "id": "nvd",
            "url": "https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch="
            + urllib.parse.quote(keyword)
            + "&resultsPerPage=20",
            "extract": "totalResults; each CVE id, published date, CVSS score, one-line "
            "description, fixed version if stated. Keep only CVEs in this library "
            "itself, not in products that embed it",
        }
    ]
    if host_path.startswith("github.com/"):
        plan.append(
            {
                "id": "advisories",
                "url": f"https://{host_path}/security/advisories",
                "extract": "each published advisory: GHSA id, severity, date; or 'none "
                "published'. Then for the most recent id fetch "
                "https://api.osv.dev/v1/vulns/<id> for published date and fixed "
                "versions (counts toward the fetch_plan)",
            }
        )
    return plan


def commit_advisories(history):
    """The OSV advisories that apply to the head or to a release tag of a repository.

    A library without a registry has no package name in OSV. Its advisories name commits."""
    points = [("HEAD", history["head"])] + [
        (t["tag"], t["commit"]) for t in history.get("tags", []) if t.get("commit")
    ]
    results = get("https://api.osv.dev/v1/querybatch", {"queries": [{"commit": c} for _, c in points]})
    affects = {}
    for (label, _), result in zip(points, results["results"]):
        for v in result.get("vulns", []):
            affects.setdefault(v["id"], []).append(label)
    vulns = [get("https://api.osv.dev/v1/vulns/" + vid) for vid in sorted(affects)[:25]]
    record = osv_record(vulns, {"commits": [label for label, _ in points]})
    record["count"] = len(affects)
    for row in record["recent"]:
        row["affects"] = affects[row["id"]]
    newest = points[1][0] if len(points) > 1 else None
    record["affects_head"] = sorted(i for i, labels in affects.items() if "HEAD" in labels)
    record["affects_latest_release"] = sorted(i for i, labels in affects.items() if newest in labels)
    return record


def add_advisories(F, eco, name, short_name, host_path):
    try:
        if eco in OSV_ECOSYSTEM:
            package = {"name": name, "ecosystem": OSV_ECOSYSTEM[eco]}
            vulns = get("https://api.osv.dev/v1/query", {"package": package}).get("vulns", [])
            F["osv"] = osv_record(vulns, package)
            return
        if F.get("history"):
            F["osv"] = commit_advisories(F["history"])
        else:  # no clone: the name in the OSS-Fuzz records is the only handle
            package = {"name": short_name, "ecosystem": "OSS-Fuzz"}
            vulns = get("https://api.osv.dev/v1/query", {"package": package}).get("vulns", [])
            F["osv"] = osv_record(vulns, package)
    except Exception as e:
        F["errors"]["osv"] = str(e)[:120]
        F["fetch_plan"] += advisory_fetch_plan(name or short_name, host_path)
        return
    if not F["osv"]["count"]:  # OSV does not have each CVE of a library without a registry
        F["osv"]["note"] = "no advisory in OSV; this is not evidence of no history, see fetch_plan"
        F["fetch_plan"] += advisory_fetch_plan(short_name, host_path)


def dep_status(record, age):
    if record.get("deprecated"):
        return "Red", "deprecated or yanked"
    if age is not None and age > 1095:
        return "Amber", "no release in 36 months"
    if record.get("publishers") == 1:
        return "Amber", "single publisher"
    return "Green", ""


def screen_dep(eco, dep):
    try:
        r = registry(eco, dep, None, with_deps=False)
        age = days((r.get("last_releases") or [None])[-1])
        status, why = dep_status(r, age)
        return {
            "name": dep,
            "version": r.get("version"),
            "status": status,
            "why": why,
            "last_release_days": age,
            "license": r.get("license"),
            "publishers": r.get("publishers"),
        }
    except Exception as e:
        return {"name": dep, "status": "unknown", "why": str(e)[:80]}


def dep_screen(eco, deps):
    rows = [screen_dep(eco, dep) for dep in sorted(deps)[:10]]
    return {
        "depth": f"direct runtime deps, first {len(rows)} of {len(deps)} alphabetically; "
        "registry metadata only, advisories not checked",
        "rows": rows,
    }


def print_summary(F, fpath):
    h, t = F.get("history", {}), F.get("tree", {})
    print(
        f"wrote {fpath}\n repo={F['repo']} head={h.get('head', '')[:10]} "
        f"commits_12m={h.get('commits_12m')} bus24={h.get('bus_factor_24m')} "
        f"last_tag_days={h.get('days_since_last_tag')} lang={t.get('primary_language')} "
        f"sloc={t.get('first_party_sloc')}\n errors={sorted(F['errors'])} "
        f"web_fetches_needed={len(F['fetch_plan'])}"
    )


def gather(target, out, repo_given, lite):
    """Gather every section. A source that fails records its error, and the others continue."""
    F = {"target": target, "collected_at": NOW.isoformat(timespec="seconds"), "collector": COLLECTOR}
    F.update(errors={}, fetch_plan=[])
    eco, name, repo = resolve_target(F, target, repo_given)
    F["repo"] = repo
    host_path = re.sub(r"^https?://", "", repo or "")
    if repo and not lite:
        add_source(F, repo, os.path.join(out, "src"), detect=not eco)
    elif not repo:
        F["errors"]["repo"] = "no source repository resolved; pass the repo URL explicitly"
    if host_path:
        add_project_sources(F, host_path)
        add_plumber(F, host_path)
    add_advisories(F, eco, name, (repo or target).rstrip("/").split("/")[-1], host_path)
    deps = (F.get("registry") or {}).get("runtime_deps")
    if eco and deps is not None and not lite:
        F["dep_screen"] = dep_screen(eco, deps)
    return F


def main():
    a = sys.argv[1:]
    pos = [
        x
        for i, x in enumerate(a)
        if not x.startswith("--") and (i == 0 or a[i - 1] not in ("--out", "--max-age", "--repo"))
    ]
    if not pos:
        sys.exit(__doc__)
    target, lite = pos[0], "--lite" in a
    slug = re.sub(r"[^\w.\-]+", "_", target.split("://")[-1]).strip("_")[-60:]
    out = opt(a, "--out", os.path.join("vet", slug))
    os.makedirs(out, exist_ok=True)
    fpath = os.path.join(out, "facts.json")
    # Reuse only facts of the same request. --repo is a correction, so it collects again.
    if (
        "--max-age" in a
        and not opt(a, "--repo")
        and reusable(load_facts(fpath), target, lite, opt(a, "--max-age"))
    ):
        print(f"reused {fpath}")
        return
    F = gather(target, out, opt(a, "--repo"), lite)
    with open(fpath, "w") as f:
        json.dump(F, f, indent=1, sort_keys=True)
    print_summary(F, fpath)


if __name__ == "__main__":
    main()
