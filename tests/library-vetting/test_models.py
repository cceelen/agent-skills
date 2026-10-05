"""Offline tests for the model mapping. Run: uv run pytest"""

import json
import pathlib
import subprocess
import sys

SKILL = pathlib.Path(__file__).resolve().parents[2] / "skills" / "library-vetting"
MODELS = str(SKILL / "scripts" / "models.py")


def run(cwd, *args):
    env = {"HOME": str(cwd), "XDG_CONFIG_HOME": str(cwd / "cfg"), "PATH": "/usr/bin:/bin"}
    r = subprocess.run([sys.executable, MODELS, *args], capture_output=True, text=True, cwd=cwd, env=env)
    return r


def test_detect_unknown_host_inherits(tmp_path):
    out = json.loads(run(tmp_path, "detect").stdout)
    assert out["host"] == "unknown"
    assert out["proposal"] == {"evidence": "inherit", "vetter": "inherit"}


def test_detect_reads_claude_settings(tmp_path):
    (tmp_path / ".claude").mkdir()
    (tmp_path / ".claude" / "settings.json").write_text(json.dumps({"model": "opus"}))
    out = json.loads(run(tmp_path, "detect").stdout)
    assert out["host"] == "claude"
    assert out["configured"]["session_model"].startswith("opus")
    assert out["proposal"]["evidence"] == "haiku"


def test_apply_writes_agents(tmp_path):
    r = run(tmp_path, "apply", "--host", "claude", "--scope", "project")
    assert r.returncode == 0, r.stderr
    ev = (tmp_path / ".claude/agents" / "library-evidence-collector.md").read_text()
    vt = (tmp_path / ".claude/agents" / "library-vetter.md").read_text()
    assert "model: haiku" in ev and "{{" not in ev and "{{" not in vt
    assert "tools: Bash, Read, Write, Grep, Glob\nmodel: inherit\n" in vt.split("---")[1]
    shown = json.loads(run(tmp_path, "show", "--host", "claude").stdout)
    assert shown["scope"] == "project" and shown["mapping"]["vetter"] == "inherit"


def test_apply_accepts_user_choice_and_rejects_bad_name(tmp_path):
    run(tmp_path, "apply", "--host", "claude", "--evidence", "sonnet", "--scope", "project")
    assert "model: sonnet" in (tmp_path / ".claude/agents/library-evidence-collector.md").read_text()
    assert run(tmp_path, "apply", "--host", "claude", "--evidence", "bad name; rm").returncode != 0


def test_apply_keeps_the_saved_model_of_the_other_role(tmp_path):
    run(tmp_path, "apply", "--host", "claude", "--vetter", "opus", "--scope", "project")
    run(tmp_path, "apply", "--host", "claude", "--evidence", "inherit", "--scope", "project")
    shown = json.loads(run(tmp_path, "show", "--host", "claude").stdout)
    assert shown["mapping"] == {"evidence": "inherit", "vetter": "opus"}


def test_apply_rejects_unknown_scope(tmp_path):
    r = run(tmp_path, "apply", "--host", "claude", "--scope", "global")
    assert r.returncode != 0 and not (tmp_path / "cfg").exists()


def test_codex_gets_mapping_but_no_agent_files(tmp_path):
    out = json.loads(run(tmp_path, "apply", "--host", "codex", "--scope", "project").stdout)
    assert len(out["written"]) == 1


def test_prompt_files_exist():
    text = (SKILL / "SKILL.md").read_text()
    for name in ("evidence.md", "usage-inventory.md", "vetter.md"):
        assert (SKILL / "prompts" / name).exists() and f"prompts/{name}" in text
