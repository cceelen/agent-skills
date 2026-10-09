import shutil

import pytest
from helpers import FIXTURE, module

aspect = module("aspect")
GOOD = FIXTURE / "good"


def test_head_and_aspect_fields():
    data = aspect.load(GOOD)
    assert data["is_aspect"]
    assert data["title"] == "Backups of project data"
    assert data["head"]["branch"] == "900-backups"
    assert data["head"]["accepted"] == "A. Person, 2026-01-15"
    assert data["aspect"]["agreed with the owner on"]["value"].startswith("2026-01-05")
    # A field that continues on the next line is one value.
    assert data["aspect"]["contexts"]["value"].endswith("the place where the data is.")
    assert [d["name"] for d in data["risk_dimensions"]] == ["operative", "regulatory"]
    assert data["risk_dimensions"][1]["text"].startswith("Is personal data in the backup?")


def test_tables_by_header_name():
    data = aspect.load(GOOD)
    assert [s["id"] for s in data["sources"]] == ["S-01", "S-02", "S-03", "S-04"]
    assert data["sources"][2]["class"] == "independent"
    assert data["sources"][0]["version or date"] == "2.0, 2025-03"
    assert [c["id"] for c in data["checklist"]] == ["C-01", "C-02", "C-03", "C-04", "C-05"]
    assert data["checklist"][1]["level"] == "2, operative"
    assert data["checklist"][0]["_file"] == "spec.md"
    assert len(data["context_decisions"]) == 1
    assert len(data["disagreement"]) == 1
    assert len(data["watch"]) == 1
    assert len(data["decisions"]) == 2
    assert data["glossary"][0]["term"] == "backup"
    assert data["implementation_skills"][0]["product or tool"] == "A backup tool"


def test_skill_block_and_strategy():
    data = aspect.load(GOOD)
    assert data["skill_name"] == "backups"
    assert data["skill"]["goal"]["value"].startswith("Each record")
    assert "target folder" not in data["skill"]
    assert data["goals"].startswith("A lost record")
    assert data["order"].startswith("1. Find out")


def test_evidence_and_vetting():
    data = aspect.load(GOOD)
    assert [e["source"] for e in data["evidence"]] == ["S-01", "S-02", "S-03", "S-04"]
    assert data["has_vetting"]
    assert [v["source"] for v in data["vetting_sources"]] == ["S-03", "S-04"]
    assert data["vetting_items"][0]["severity"] == "3 (S-02 abstract)"


def test_identifiers_in_a_cell():
    assert aspect.source_ids("S-03 items 1, 13; S-04 guideline 11; S-03") == ["S-03", "S-04"]
    assert aspect.principles("constitution IV; S-21 abstract") == ["IV"]
    assert aspect.item_ids("C-02 to C-04, C-09; 3.3 depth") == ["C-02", "C-03", "C-04", "C-09"]
    assert aspect.level_of("2, operative") == (2, "operative")
    assert aspect.level_of("1") == (1, None)
    assert aspect.level_of("pending") == ("pending", None)
    assert aspect.level_of("high") == (None, None)


def test_escaped_pipe_is_one_cell():
    assert aspect.split_row(r"| a \| b | c |") == ["a | b", "c"]


def test_absent_files(tmp_path):
    with pytest.raises(aspect.Unreadable):
        aspect.load(tmp_path)
    shutil.copy(GOOD / "spec.md", tmp_path / "spec.md")
    data = aspect.load(tmp_path)
    assert data["evidence"] == [] and data["vetting_items"] == [] and not data["has_vetting"]


def test_set_cell_changes_one_cell_only(tmp_path):
    shutil.copy(GOOD / "spec.md", tmp_path / "spec.md")
    before = (tmp_path / "spec.md").read_text()
    row = aspect.load(tmp_path)["checklist"][3]
    aspect.set_cell(tmp_path / "spec.md", row["_line"], 3, "pending")
    after = (tmp_path / "spec.md").read_text()
    assert aspect.load(tmp_path)["checklist"][3]["level"] == "pending"
    assert after == before.replace("| not admitted |", "| pending |")
