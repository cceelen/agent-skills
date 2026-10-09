"""Checks that apply to every artifact in the repository."""

import doctest
import importlib.util
import json
import os
import pathlib
import re
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
# The folders that hold installable artifacts. AGENTS.md defines them.
ARTIFACT_TYPES = ("skills", "factory")
ARTIFACTS = sorted(
    p for kind in ARTIFACT_TYPES if (ROOT / kind).is_dir() for p in (ROOT / kind).iterdir() if p.is_dir()
)
# The tooling of the factory has the layout of a skill.
SKILLS = ARTIFACTS


@pytest.mark.parametrize("artifact", ARTIFACTS, ids=lambda p: f"{p.parent.name}/{p.name}")
def test_artifact_has_documentation_and_tests(artifact):
    assert re.fullmatch(r"[a-z0-9-]+", artifact.name), "names use lowercase letters, digits and hyphens"
    assert (ROOT / "docs" / f"{artifact.name}.md").exists(), "each artifact has a page in docs/"
    # A rendered recipe skill carries a stamp: the renderer covers it. A program with examples
    # validates itself with --selftest. Each other artifact has tests in tests/<name>/.
    rendered = "Rendered from the specification branch" in (artifact / "SKILL.md").read_text()
    programs = sorted((artifact / "scripts").glob("*.py"))
    self_validating = bool(programs) and all(">>> " in p.read_text() for p in programs)
    assert rendered or self_validating or (ROOT / "tests" / artifact.name).is_dir(), (
        "each artifact has examples in its programs or tests in tests/<name>/"
    )


@pytest.mark.parametrize("skill", SKILLS, ids=lambda p: f"{p.parent.name}/{p.name}")
def test_skill_layout(skill):
    text = (skill / "SKILL.md").read_text()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    assert m, "SKILL.md must start with YAML front matter"
    front = m.group(1)
    name = re.search(r'^name:\s*"?([a-z0-9-]+)"?\s*$', front, re.M)
    assert name and name.group(1) == skill.name, "front matter name must equal the folder name"
    assert re.search(r"^description:\s*\S", front, re.M)


def test_plugin_manifest_has_the_project_version():
    manifest = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
    project = re.search(r'^version = "([^"]+)"', (ROOT / "pyproject.toml").read_text(), re.M)
    assert manifest["version"] == project.group(1)


def rules_program():
    spec = importlib.util.spec_from_file_location("apply", ROOT / "rules" / "apply.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_rules_program():
    assert doctest.testmod(rules_program()).failed == 0


@pytest.mark.parametrize("skill", SKILLS, ids=lambda p: p.name)
def test_skill_holds_the_rules(skill):
    assert rules_program().block() in (skill / "SKILL.md").read_text(), "run rules/apply.py --print"


@pytest.mark.parametrize("name", ["AGENTS.md", "CLAUDE.md"])
def test_repository_rules_are_the_rules_of_the_kit(name):
    rules = (ROOT / "rules" / "evidence-before-action.md").read_text()
    assert rules in (ROOT / name).read_text(), f"{name} and rules/ must hold the same rules"


def test_plugin_hook_prints_the_rules():
    hooks = json.loads((ROOT / "hooks" / "hooks.json").read_text())["hooks"]["SessionStart"]
    assert "compact" in hooks[0]["matcher"]
    assert "rules/apply.py" in hooks[0]["hooks"][0]["command"]


# The programs of the factory hold their tests as examples (doctests) and need the latest Python.
FACTORY_PROGRAMS = sorted(ROOT.glob("factory/*/scripts/*.py"))
LATEST_PYTHON = sys.version_info >= (3, 14)


def test_each_factory_program_has_examples():
    for program in FACTORY_PROGRAMS:
        text = program.read_text()
        assert ">>> " in text and "selftest" in text, f"{program.name} must validate itself with --selftest"


@pytest.mark.skipif(not LATEST_PYTHON, reason="the tooling of the factory needs Python 3.14")
def test_factory_programs_validate_themselves_and_meet_the_coverage_minimum(tmp_path):
    """Run the examples of each program under coverage. The minimum is in pyproject.toml."""
    pytest.importorskip("coverage")
    coverage = [sys.executable, "-m", "coverage"]
    for program in FACTORY_PROGRAMS:
        data = tmp_path / f".coverage.{program.parents[1].name}.{program.stem}"
        done = subprocess.run(
            [*coverage, "run", f"--data-file={data}", str(program), "--selftest"],
            capture_output=True,
            text=True,
            check=False,
            cwd=ROOT,
        )
        assert done.returncode == 0, f"{program.name}:\n" + done.stdout[-4000:] + done.stderr[-2000:]
        assert " examples, 0 failed" in done.stdout, program.name
    combined = tmp_path / ".coverage"
    subprocess.run([*coverage, "combine", f"--data-file={combined}", str(tmp_path)], check=True, cwd=ROOT)
    report = subprocess.run(
        [*coverage, "report", f"--data-file={combined}"],
        capture_output=True,
        text=True,
        check=False,
        cwd=ROOT,
    )
    # The CI gives a path for the report that it sends to Codecov.
    if os.environ.get("COVERAGE_XML"):
        xml = pathlib.Path(os.environ["COVERAGE_XML"]).resolve()
        subprocess.run([*coverage, "xml", f"--data-file={combined}", "-o", str(xml)], check=True, cwd=ROOT)
    assert report.returncode == 0, "the coverage is below the minimum:\n" + report.stdout


def test_each_stamp_of_a_rendered_skill_has_the_right_form():
    stamp = re.compile(
        r"specification branch `[^`]*`, commit `[0-9a-f]{4,40}`, spec\.md sha256 `[0-9a-f]{64}`"
    )
    wrong = []
    for kind in ARTIFACT_TYPES:
        for skill in sorted((ROOT / kind).glob("*/SKILL.md")):
            text = skill.read_text()
            if "Rendered from the specification" in text and not stamp.search(text):
                wrong.append(str(skill.relative_to(ROOT)))
    assert not wrong


@pytest.mark.skipif(not LATEST_PYTHON, reason="the tooling of the factory needs Python 3.14")
def test_rendered_skills_are_fresh():
    """Only the branch of an aspect specification has the folder specs/. On main nothing is compared."""
    render = ROOT / "factory" / "sota-research" / "scripts" / "render.py"
    stale = []
    for spec in sorted(ROOT.glob("specs/*/spec.md")):
        head = spec.read_text()[:2000]
        if not head.startswith("# Aspect specification") or "**Accepted**: pending" in head:
            continue
        if "**Accepted**:" not in head:
            continue
        done = subprocess.run(
            [sys.executable, str(render), str(spec.parent), "--check", "--out", str(ROOT)],
            capture_output=True,
            text=True,
            check=False,
        )
        if done.returncode != 0:
            stale.append(f"{spec.parent.name}: {done.stdout.strip()}")
    assert not stale
