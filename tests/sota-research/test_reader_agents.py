"""The two readers get web tools only."""

import json

from helpers import SCRIPTS, module, run

models = module("models")
lib = models.shared()


def front_matter(text):
    head = text.split("---\n")[1]
    return dict(line.split(": ", 1) for line in head.splitlines())


def test_each_agent_product_with_agent_files_gives_web_tools_only():
    checked = 0
    for host, entry in lib.HOSTS.items():
        files = models.render(host, models.mapping_for(host, []), lib.HOSTS)
        if not entry["agents"]:
            assert files == {}
            continue
        assert sorted(files) == ["sota-second-reader.md", "sota-source-reader.md"]
        forbidden = {entry["tools"][t] for t in models.FORBIDDEN}
        for text in files.values():
            assert "{{" not in text
            tools = set(front_matter(text)["tools"].split(", "))
            assert not tools & forbidden
            checked += 1
        reader = set(front_matter(files["sota-source-reader.md"])["tools"].split(", "))
        second = set(front_matter(files["sota-second-reader.md"])["tools"].split(", "))
        assert reader == {entry["tools"]["search"], entry["tools"]["fetch"]}
        assert second == {entry["tools"]["fetch"]}
    assert checked >= 2


def test_roles_get_different_models_and_a_given_model_wins():
    mapping = models.mapping_for("claude", [])
    assert mapping["source-reader"] != mapping["second-reader"]
    assert models.mapping_for("claude", ["--second-reader", "inherit"])["second-reader"] == "inherit"
    assert models.mapping_for("other", []) == {"source-reader": "inherit", "second-reader": "inherit"}


def test_show_writes_nothing(tmp_path):
    code, out, _ = run("models", "show", "--host", "claude")
    result = json.loads(out)
    assert code == 0 and result["writes_agent_files"] and "written" not in result
    assert "model: " in result["files"]["sota-source-reader.md"]


def test_a_product_without_agent_files_is_reported():
    code, out, _ = run("models", "show", "--host", "codex")
    result = json.loads(out)
    assert code == 1 and not result["writes_agent_files"]
    assert "cannot be limited" in result["note"]


def test_the_shared_program_is_where_this_program_expects_it():
    assert SCRIPTS.parents[2] / "skills/library-vetting/scripts/models.py" == models.SHARED
