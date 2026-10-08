"""Checks that apply to every artifact in the repository."""

import json
import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
# One top-level folder for each artifact type. AGENTS.md defines them.
ARTIFACT_TYPES = ("agents", "skills", "processes", "template-sets")
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
