"""The check reports each planted defect, and no other."""

import json
import shutil

import pytest
from helpers import FIXTURE, run

GOOD = FIXTURE / "good"

# name of the rule -> (file, text in the good fixture, replacement, identifier in the finding)
DEFECTS = {
    "accepted-missing": ("spec.md", " | **Accepted**: A. Person, 2026-01-15", "", ""),
    "aspect-field-empty": (
        "spec.md",
        "- **Boundaries**: the recovery of a complete site belongs to a different aspect.",
        "- **Boundaries**:",
        "",
    ),
    "agreed-without-date": (
        "spec.md",
        "2026-01-05; a recipe for small teams.",
        "in January; a recipe for small teams.",
        "",
    ),
    "risk-dimension-empty": (
        "spec.md",
        "  - `operative`: Can a lost record be made again? Opinion: if not, go past level 1.",
        "  - `operative`:",
        "operative",
    ),
    "source-cell-empty": ("spec.md", "| Example Journal |", "| |", "S-02"),
    "source-without-version": ("spec.md", "| 2.0, 2025-03 |", "| |", "S-01"),
    "class-unknown": ("spec.md", "| 2024 | research |", "| 2024 | paper |", "S-02"),
    "read-unknown": ("spec.md", "| CC BY 4.0 | full |", "| CC BY 4.0 | yes |", "S-02"),
    "source-id-twice": (
        "spec.md",
        "| S-02 | A study",
        "| S-01 | A copy | Example | 2020 | standard | public | full | u |\n| S-02 | A study",
        "S-01",
    ),
    "unknown-source": ("spec.md", "| S-02 section 4 |", "| S-09 section 4 |", "C-02"),
    "item-without-source": ("spec.md", "| S-02 section 4 |", "| a talk |", "C-02"),
    "check-empty": ("spec.md", "| the record of the last restore has a date |", "| |", "C-02"),
    "why-empty": ("spec.md", "| Risk: a backup that cannot be restored is found too late. |", "| |", "C-02"),
    "level-unknown": ("spec.md", "| 2, operative |", "| high |", "C-02"),
    "level-without-dimension": ("spec.md", "| 2, operative |", "| 2 |", "C-02"),
    "dimension-unknown": ("spec.md", "| 2, operative |", "| 2, commercial |", "C-02"),
    "no-evidence-row": ("evidence.md", "| S-03 | A written review", "| S-07 | A written review", "C-04"),
    "evidence-does-not-name-item": (
        "evidence.md",
        '| "After the drill" | C-04 |',
        '| "After the drill" | 3.3 frequency |',
        "C-04",
    ),
    "evidence-without-date": (
        "evidence.md",
        "| README | C-05 | 2026-01-10 |",
        "| README | C-05 | yes |",
        "S-04",
    ),
    "no-disagreement-section": (
        "spec.md",
        "### 3.4 Where the sources disagree",
        "### Where the sources disagree",
        "",
    ),
    "glossary-cell-empty": ("spec.md", "| a copy that is kept to make lost data again |", "| |", "backup"),
    "decision-without-date": (
        "spec.md",
        "| 2026-01-05 | The recipe is for small teams.",
        "| January | The recipe is for small teams.",
        "",
    ),
    "watch-list-empty": (
        "spec.md",
        "| A new version of S-01 | the page of the issuer | at each refresh |\n",
        "",
        "",
    ),
    "only-unread-source": ("spec.md", "| CC BY 4.0 | full |", "| CC BY 4.0 | no |", "C-02"),
    "only-rejected-source": (
        "vetting.md",
        "fast-lane references: 1 (S-02) | | | A. Person, 2026-01-15 |",
        "fast-lane references: 1 (S-02) | | | rejected |",
        "C-04",
    ),
}


def copy_with(tmp_path, file=None, old=None, new=None):
    target = tmp_path / "spec"
    shutil.copytree(GOOD, target)
    if file:
        text = (target / file).read_text()
        assert text.count(old) == 1, f"the fixture must hold the text one time: {old}"
        (target / file).write_text(text.replace(old, new))
    return target


def findings(*args):
    code, out, _ = run("check", *args, "--json")
    return code, json.loads(out)


def test_good_fixture_has_no_finding():
    code, result = findings(GOOD)
    assert code == 0
    assert result["findings"] == []
    assert result["accepted"] is True
    assert result["remains"] == {
        "changed": [],
        "judgement": ["C-04"],
        "levels": [],
        "vettings": [],
        "waiting": [],
    }


@pytest.mark.parametrize("rule", sorted(DEFECTS))
def test_each_planted_defect_is_reported_and_no_other(tmp_path, rule):
    file, old, new, ident = DEFECTS[rule]
    code, result = findings(copy_with(tmp_path, file, old, new))
    assert code == 1
    assert [(f["rule"], f["id"]) for f in result["findings"]] == [(rule, ident)]
    assert result["findings"][0]["line"] >= 0 and result["findings"][0]["text"]


def test_risk_dimensions_missing(tmp_path):
    target = copy_with(tmp_path)
    text = (target / "spec.md").read_text()
    lines = [line for line in text.splitlines() if not line.startswith("  - `")]
    (target / "spec.md").write_text("\n".join(lines) + "\n")
    _, result = findings(target)
    rules = {f["rule"] for f in result["findings"]}
    assert "risk-dimensions-missing" in rules and "dimension-unknown" in rules


def test_product_word(tmp_path):
    words = tmp_path / "words.txt"
    words.write_text("Restic\nprogram\n")
    code, result = findings(GOOD, "--words", words)
    assert code == 1
    assert [(f["rule"], f["id"]) for f in result["findings"]] == [("product-word", "C-05")]


def test_remains_do_not_fail_the_check(tmp_path):
    target = copy_with(tmp_path, "spec.md", "| 2, operative |", "| pending |")
    text = (
        (target / "spec.md")
        .read_text()
        .replace("**Accepted**: A. Person, 2026-01-15", "**Accepted**: pending")
    )
    (target / "spec.md").write_text(text)
    vetting = (
        (target / "vetting.md")
        .read_text()
        .replace(
            "fast-lane references: 0 | | | A. Person, 2026-01-15", "fast-lane references: 0 | | | pending"
        )
    )
    (target / "vetting.md").write_text(vetting)
    code, result = findings(target)
    assert code == 0
    assert result["accepted"] is False
    assert result["remains"]["levels"] == ["C-02"]
    assert result["remains"]["vettings"] == ["S-04"]
    assert result["remains"]["waiting"] == []
    _, out, _ = run("check", target)
    assert "The owner did not accept the specification." in out
    assert "Levels that are pending: C-02." in out


def test_previous_revision(tmp_path):
    previous = tmp_path / "previous.md"
    text = (GOOD / "spec.md").read_text()
    # The earlier revision: C-02 had a different text, C-05 was retired, and it had an item C-06.
    text = text.replace("A restore from the backup was done and recorded.", "A restore was done.")
    text = text.replace("| 1 | practice | the schedule", "| retired | practice | the schedule")
    text = text.replace(
        "\n**Selection.**",
        "| C-06 | An old item. | Risk: none. | 1 | practice | judgement | S-01 |\n\n**Selection.**",
    )
    previous.write_text(text)
    code, result = findings(GOOD, "--previous", previous)
    assert code == 1
    assert sorted((f["rule"], f["id"]) for f in result["findings"]) == [
        ("id-removed", "C-06"),
        ("id-reused", "C-05"),
    ]
    assert result["remains"]["changed"] == ["C-02"]
    assert result["previous"] is True


def test_a_retired_item_is_not_checked(tmp_path):
    target = copy_with(
        tmp_path,
        "spec.md",
        "| 2, operative | authority (1) | the record of the last restore has a date |",
        "| retired | authority (1) | |",
    )
    code, result = findings(target)
    assert code == 0 and result["findings"] == []


def test_text_report_and_skipped_note():
    code, out, _ = run("check", GOOD)
    assert code == 0
    assert out.splitlines()[0] == "No check fails."
    assert "Accepted: A. Person, 2026-01-15." in out
    assert "The check of stable identifiers was skipped" in out


def test_text_report_names_the_place(tmp_path):
    file, old, new, _ = DEFECTS["unknown-source"]
    _, out, _ = run("check", copy_with(tmp_path, file, old, new))
    assert out.splitlines()[0].startswith("FAIL unknown-source spec.md:")
    assert "C-02: The row cites 'S-09'." in out.splitlines()[0]


def test_two_runs_give_the_same_bytes():
    assert run("check", GOOD, "--json") == run("check", GOOD, "--json")
    assert run("check", GOOD) == run("check", GOOD)


def test_input_that_cannot_be_read(tmp_path):
    code, out, err = run("check", tmp_path)
    assert code == 2 and out == "" and "cannot be read" in err


def test_no_argument_prints_the_usage():
    code, _, err = run("check")
    assert code != 0 and "check.py SPEC" in err


def test_an_item_that_waits_for_a_vetting_remains(tmp_path):
    old = "fast-lane references: 1 (S-02) | | | A. Person, 2026-01-15 |"
    target = copy_with(tmp_path, "vetting.md", old, "fast-lane references: 1 (S-02) | | | pending |")
    code, result = findings(target)
    assert code == 0
    assert result["remains"]["waiting"] == ["C-04"] and result["remains"]["vettings"] == ["S-03"]
