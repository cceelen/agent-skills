"""The calculation of risk and reward gives the same admission, order and level each time."""

import shutil

from helpers import FIXTURE, SCRIPTS, module, run

GOOD = FIXTURE / "good"
place = module("place")
aspect = module("aspect")

EFFORT = "2 (judgement) | 2 (judgement) | 2 (judgement)"
C02 = f"| C-02 | 3 (S-02 section 4) | 2 (S-02 section 4) | {EFFORT} | 0 (judgement) |"


def copy_with(tmp_path, old=None, new=None):
    target = tmp_path / "spec"
    shutil.copytree(GOOD, target)
    if old:
        text = (target / "vetting.md").read_text()
        assert text.count(old) == 1
        (target / "vetting.md").write_text(text.replace(old, new))
    return target


def results(folder):
    rubric = place.read_rubric(SCRIPTS / "rubric-items.txt")
    return {r["id"]: r for r in place.place(aspect.load(folder), rubric)}


def test_expected_values_of_the_fixture():
    got = results(GOOD)
    table = {k: (r["return"], r["cost"], r["score"], r["level"], r.get("position")) for k, r in got.items()}
    assert table == {
        "C-01": (27, 2, 135, "1", 1),
        "C-02": (12, 4, 30, "2, operative", 3),
        "C-03": (12, 6, 20, "3, regulatory", 4),
        "C-04": (2, 5, -1, "not admitted", None),
        "C-05": (18, 3, 60, "1", 2),
    }
    assert got["C-04"]["state"] == "not admitted"


def test_report_and_result_code():
    code, out, _ = run("place", GOOD)
    assert code == 0
    assert out.splitlines()[0] == "C-01: return 27, cost 2, score 135, admitted yes, level 1, position 1."
    assert "C-04: return 2, cost 5, score -1, not admitted." in out
    assert out.splitlines()[-1] == "Rubric version 1. Items placed: 5. Items pending: 0."


def test_a_missing_answer_keeps_the_item_pending(tmp_path):
    spec = copy_with(tmp_path, C02, C02.replace("| 2 (S-02 section 4) |", "| |"))
    code, out, _ = run("place", spec)
    assert code == 1
    assert "C-02: pending. The answer 'probability' is missing." in out
    assert "Items pending: 1." in out


def test_an_answer_out_of_its_scale_is_reported(tmp_path):
    spec = copy_with(tmp_path, C02, C02.replace("| 3 (S-02 section 4) |", "| 4 (S-02 section 4) |"))
    code, out, _ = run("place", spec)
    assert code == 1 and "The answer 'severity' is 4. The scale is 1 to 3." in out


def test_an_item_above_level_1_needs_a_dimension(tmp_path):
    spec = copy_with(tmp_path, "0 (judgement) | operative |", "0 (judgement) | |")
    code, out, _ = run("place", spec)
    assert code == 1 and "C-02: pending. The item is above level 1." in out
    spec2 = copy_with(tmp_path / "b", "0 (judgement) | operative |", "0 (judgement) | commercial |")
    code, out, _ = run("place", spec2)
    assert code == 1 and "The risk dimension 'commercial' is not in section 1" in out


def test_an_item_without_a_row_is_pending(tmp_path):
    spec = copy_with(tmp_path, C02 + " operative | 12 | 4 | 30 | yes | 2, operative |\n", "")
    code, out, _ = run("place", spec)
    assert code == 1 and "C-02: pending. The table Items of vetting.md has no row" in out


def test_without_write_no_file_changes(tmp_path):
    spec = copy_with(tmp_path, "| 27 | 2 | 135 | yes | 1 |", "| | | | | |")
    before = {p.name: p.read_text() for p in spec.iterdir()}
    run("place", spec)
    assert {p.name: p.read_text() for p in spec.iterdir()} == before


def test_write_fills_only_the_computed_cells(tmp_path):
    spec = copy_with(tmp_path)
    good_vetting, good_spec = (spec / "vetting.md").read_text(), (spec / "spec.md").read_text()
    # Empty the computed cells and one level, then compute again: the files are the same as before.
    emptied = good_vetting.replace("| 27 | 2 | 135 | yes | 1 |", "| | | | | |")
    (spec / "vetting.md").write_text(emptied)
    (spec / "spec.md").write_text(good_spec.replace("| 1 | authority (2) |", "| pending | authority (2) |"))
    code, out, _ = run("place", spec, "--write")
    assert code == 0 and out.splitlines()[-1] == "The program wrote the results to vetting.md and spec.md."
    assert (spec / "spec.md").read_text() == good_spec
    assert (spec / "vetting.md").read_text() == good_vetting


def test_a_corrected_answer_changes_only_its_item(tmp_path):
    spec = copy_with(
        tmp_path,
        C02,
        C02.replace(EFFORT, "3 (owner) | 1 (owner) | 1 (owner)"),
    )
    before, after = results(GOOD), results(spec)
    assert after["C-02"]["score"] == 90 and after["C-02"]["level"] == "1"
    for ident in ("C-03", "C-04"):
        assert {k: v for k, v in after[ident].items() if k != "position"} == {
            k: v for k, v in before[ident].items() if k != "position"
        }


def test_the_record_carries_the_version_of_the_rubric(tmp_path):
    spec = copy_with(tmp_path)
    rubric = tmp_path / "rubric.txt"
    rubric.write_text((SCRIPTS / "rubric-items.txt").read_text().replace("version: 1", "version: 7"))
    code, out, _ = run("place", spec, "--write", "--rubric", rubric)
    assert code == 0 and "Rubric version 7." in out
    assert "Rubric for items: version 7." in (spec / "vetting.md").read_text()
    assert "Rubric for sources: version 1." in (spec / "vetting.md").read_text()


def test_a_rubric_that_is_not_complete(tmp_path):
    rubric = tmp_path / "rubric.txt"
    rubric.write_text("version: 1\n")
    code, _, err = run("place", GOOD, "--rubric", rubric)
    assert code == 2 and "The rubric cannot be read" in err


def test_two_runs_give_the_same_bytes():
    assert run("place", GOOD) == run("place", GOOD)


def test_input_that_cannot_be_read(tmp_path):
    code, _, err = run("place", tmp_path)
    assert code == 2 and "cannot be read" in err
