"""Checks that apply to every skill in the repository."""

import json
import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILLS = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())


@pytest.mark.parametrize("skill", SKILLS, ids=lambda p: p.name)
def test_skill_layout(skill):
    text = (skill / "SKILL.md").read_text()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    assert m, "SKILL.md must start with YAML front matter"
    front = m.group(1)
    name = re.search(r'^name:\s*"?([a-z0-9-]+)"?\s*$', front, re.M)
    assert name and name.group(1) == skill.name, "front matter name must equal the folder name"
    assert re.search(r"^description:\s*\S", front, re.M)
    assert (ROOT / "docs" / f"{skill.name}.md").exists(), "each skill has a page in docs/"
    assert (ROOT / "tests" / skill.name).is_dir(), "each skill has tests in tests/<name>/"


def test_plugin_manifest_has_the_project_version():
    manifest = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
    project = re.search(r'^version = "([^"]+)"', (ROOT / "pyproject.toml").read_text(), re.M)
    assert manifest["version"] == project.group(1)
