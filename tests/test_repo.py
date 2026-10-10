"""Checks that apply to every artifact in the repository."""

import doctest
import importlib.util
import json
import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
# The folders that hold installable artifacts. AGENTS.md defines them.
ARTIFACT_TYPES = ("skills",)
ARTIFACTS = sorted(
    p for kind in ARTIFACT_TYPES if (ROOT / kind).is_dir() for p in (ROOT / kind).iterdir() if p.is_dir()
)
SKILLS = [p for p in ARTIFACTS if p.parent.name == "skills"]


@pytest.mark.parametrize("artifact", ARTIFACTS, ids=lambda p: f"{p.parent.name}/{p.name}")
def test_artifact_has_documentation_and_tests(artifact):
    assert re.fullmatch(r"[a-z0-9-]+", artifact.name), "names use lowercase letters, digits and hyphens"
    assert (ROOT / "docs" / f"{artifact.name}.md").exists(), "each artifact has a page in docs/"
    assert (ROOT / "tests" / artifact.name).is_dir(), "each artifact has tests in tests/<name>/"


@pytest.mark.parametrize("skill", SKILLS, ids=lambda p: p.name)
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
