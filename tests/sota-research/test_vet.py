"""The vetting scores a source from recorded signals, without the network."""

import json
import shutil

from helpers import FIXTURE, ROOT, SCRIPTS, module, run

GOOD = FIXTURE / "good"
SIGNALS = FIXTURE / "signals"
PAGES = FIXTURE / "pages"
vet = module("vet")

S03_ROW = "| S-03 | page | pass | reachable yes; date 2025-06-01; age 223 d; author yes; links out 6 |"


def workspace(tmp_path, **changes):
    """A copy of the specification and of the signal files. changes: source id -> new signals."""
    spec, work = tmp_path / "spec", tmp_path / "work"
    shutil.copytree(GOOD, spec)
    shutil.copytree(SIGNALS, work)
    for ident, signals in changes.items():
        path = work / f"{ident.replace('_', '-')}.json"
        record = json.loads(path.read_text())
        record["signals"].update(signals)
        path.write_text(json.dumps(record))
    return spec, work


def edit(path, old, new):
    text = path.read_text()
    assert text.count(old) == 1, old
    path.write_text(text.replace(old, new))


def test_expected_scores_of_the_fixture():
    code, out, _ = run("vet", "score", GOOD, "--work", SIGNALS)
    assert code == 0
    assert out.splitlines() == [
        "S-03: page, gates pass, score 9 of 10. Confirmed by: A. Person, 2026-01-15.",
        "S-04: repository, gates pass, score 8 of 10. Confirmed by: A. Person, 2026-01-15.",
        "Rubric version 1. Confirmed: 2. Wait for the owner: 0. Rejected: 0. Not scored: 0.",
    ]


def test_score_uses_no_network(tmp_path, monkeypatch):
    def no_network(*args, **kwargs):
        raise AssertionError("the scoring must not use the network")

    monkeypatch.setattr(vet.urllib.request, "urlopen", no_network)
    monkeypatch.setattr(vet, "fetch", no_network)
    monkeypatch.setattr(vet.subprocess, "run", no_network)
    spec, work = workspace(tmp_path)
    assert vet.cmd_score(vet.aspect.load(spec), ["--work", str(work)]) == 0


def test_gate_no_date(tmp_path):
    spec, work = workspace(tmp_path, S_03={"date": None, "age_days": None})
    edit(spec / "spec.md", "| A. Writer | 2025-06-01 |", "| A. Writer | not dated |")
    code, out, _ = run("vet", "score", spec, "--work", work)
    assert code == 1 and "S-03: page, rejected by a gate: no date." in out


def test_a_date_of_section_2_is_used_when_the_page_gives_none(tmp_path):
    spec, work = workspace(tmp_path, S_03={"date": None, "age_days": None})
    code, out, _ = run("vet", "score", spec, "--work", work)
    assert code == 0 and "S-03: page, gates pass, score 9 of 10." in out


def test_gate_too_old(tmp_path):
    spec, work = workspace(tmp_path, S_03={"date": "2022-01-01", "age_days": 1470})
    code, out, _ = run("vet", "score", spec, "--work", work)
    assert code == 1 and "rejected by a gate: older than 1095 days." in out
    code, out, _ = run("vet", "score", spec, "--work", work, "--max-age", "2000")
    assert code == 0 and "S-03: page, gates pass, score 7 of 10." in out


def test_gate_not_reachable_and_no_author(tmp_path):
    spec, work = workspace(tmp_path, S_03={"reachable": False}, S_04={"author": None})
    edit(spec / "spec.md", "| backup-examples | example-org |", "| backup-examples | unknown |")
    code, out, _ = run("vet", "score", spec, "--work", work)
    assert code == 1
    assert "S-03: page, rejected by a gate: not reachable." in out
    assert "S-04: repository, rejected by a gate: no author or issuer." in out
    assert "Rejected: 2." in out


def test_a_low_score_is_rejected(tmp_path):
    spec, work = workspace(tmp_path, S_03={"links_out": 0, "date": "2023-06-01", "age_days": 954})
    edit(spec / "vetting.md", "record: yes (https://writer.example/about)", "record: no")
    code, out, _ = run("vet", "score", spec, "--work", work)
    assert code == 1 and "S-03: page, rejected: the score 2 is below 5." in out


def test_a_signal_that_was_not_measured(tmp_path):
    spec, work = workspace(tmp_path, S_03={"reachable": None})
    code, out, _ = run("vet", "score", spec, "--work", work)
    assert code == 1
    assert "S-03: not scored. The signal 'reachable' was not measured." in out
    assert "S-04: repository, gates pass" in out


def test_missing_signals_missing_row_and_missing_answer(tmp_path):
    spec, work = workspace(tmp_path)
    (work / "S-03.json").unlink()
    edit(spec / "vetting.md", "record: yes (https://forge.example/example-org); ", "")
    code, out, _ = run("vet", "score", spec, "--work", work)
    assert code == 1
    assert "S-03: not scored. Run the collection for this source first." in out
    assert "S-04: not scored. The answer 'record' is missing" in out
    lines = [x for x in (spec / "vetting.md").read_text().splitlines() if not x.startswith("| S-04 ")]
    (spec / "vetting.md").write_text("\n".join(lines) + "\n")
    _, out, _ = run("vet", "score", spec, "--work", work)
    assert "S-04: not scored. Add a row for this source" in out


def test_a_source_waits_for_the_owner(tmp_path):
    spec, work = workspace(tmp_path)
    edit(
        spec / "vetting.md",
        "| 9 of 10 | 2026-01-10 | A. Person, 2026-01-15 |",
        "| 9 of 10 | 2026-01-10 | pending |",
    )
    code, out, _ = run("vet", "score", spec, "--work", work)
    assert code == 1 and "Wait for the owner: 1." in out
    # The check then lists the item that rests only on this source.
    _, report, _ = run("check", spec)
    assert "Items that rest only on sources with a pending vetting: C-04." in report


def test_write_fills_the_cells_and_never_the_confirmation(tmp_path):
    spec, work = workspace(tmp_path)
    good = (spec / "vetting.md").read_text()
    assert S03_ROW in good
    emptied = good.replace(S03_ROW, "| S-03 | | | |").replace(
        "| 9 of 10 | 2026-01-10 | A. Person, 2026-01-15 |", "| | | pending |"
    )
    (spec / "vetting.md").write_text(emptied)
    code, out, _ = run("vet", "score", spec, "--work", work, "--write")
    assert code == 1 and out.splitlines()[-1] == "The program wrote the results to vetting.md."
    assert (spec / "vetting.md").read_text() == good.replace(
        "| 9 of 10 | 2026-01-10 | A. Person, 2026-01-15 |", "| 9 of 10 | 2026-01-10 | pending |"
    )


def test_page_signals_from_a_saved_page():
    signals = vet.page_signals((PAGES / "article.html").read_text(), "https://writer.example/drills")
    assert signals == {"author": "A. Writer", "date": "2025-06-01", "links_out": 2}
    bare = vet.page_signals((PAGES / "bare.html").read_text(), "https://writer.example/x", "2024-02-03")
    assert bare == {"author": None, "date": "2024-02-03", "links_out": 0}
    assert vet.age_days("2025-06-01", "2026-01-10") == 223


def test_kind_of_a_source():
    assert vet.kind_of(None, "https://github.com/example-org/backup-examples") == "repository"
    assert vet.kind_of(None, "https://github.com/example-org/backup-examples/blob/main/README.md") == "page"
    assert vet.kind_of({"kind": "repository"}, "https://forge.example/a/b") == "repository"
    assert vet.kind_of(None, "https://writer.example/drills") == "page"


def test_collect_records_a_network_error_and_continues(tmp_path, monkeypatch):
    def fail(url):
        raise OSError("the network is not available")

    monkeypatch.setattr(vet, "fetch", fail)
    monkeypatch.setattr(vet, "COLLECTOR_PROGRAM", tmp_path / "absent.py")
    work = tmp_path / "work"
    code = vet.cmd_collect(vet.aspect.load(GOOD), ["collect", "--work", str(work), "--today", "2026-01-10"])
    assert code == 0
    page = json.loads((work / "S-03.json").read_text())
    assert page["signals"]["reachable"] is None
    assert page["errors"] == {"reachable": "the network is not available"}
    repository = json.loads((work / "S-04.json").read_text())
    assert repository["kind"] == "repository" and "absent" in repository["errors"]["reachable"]


def test_collect_reads_a_page_and_does_not_read_the_clock(tmp_path, monkeypatch):
    monkeypatch.setattr(vet, "fetch", lambda url: ((PAGES / "article.html").read_text(), None))
    work = tmp_path / "work"
    args = ["collect", "S-03", "--work", str(work), "--today", "2026-01-10"]
    vet.cmd_collect(vet.aspect.load(GOOD), list(args))
    first = (work / "S-03.json").read_text()
    vet.cmd_collect(vet.aspect.load(GOOD), list(args))
    assert (work / "S-03.json").read_text() == first
    record = json.loads(first)
    assert record["signals"] == {
        "age_days": 223,
        "author": "A. Writer",
        "date": "2025-06-01",
        "links_out": 2,
        "reachable": True,
    }
    assert not (work / "S-04.json").exists()


def test_the_collector_of_library_vetting_is_where_the_program_expects_it():
    assert vet.COLLECTOR_PROGRAM == ROOT / "skills/library-vetting/scripts/collect.py"
    assert vet.COLLECTOR_PROGRAM.is_file()


def test_a_rubric_that_is_not_complete(tmp_path):
    rubric = tmp_path / "rubric.txt"
    rubric.write_text("version: 1\n")
    code, _, err = run("vet", "score", GOOD, "--work", SIGNALS, "--rubric", rubric)
    assert code == 2 and "The rubric cannot be read" in err


def test_the_rubric_file_is_complete():
    rubric = vet.read_rubric(SCRIPTS / "rubric-sources.txt")
    assert rubric["version"] == 1 and rubric["pass score"] == 5
    assert vet.points(rubric["weights"]["age-days"], 400) == 2
    assert vet.points(rubric["weights"]["record"], "yes") == 3


def test_two_runs_give_the_same_bytes():
    assert run("vet", "score", GOOD, "--work", SIGNALS) == run("vet", "score", GOOD, "--work", SIGNALS)


def test_input_that_cannot_be_read(tmp_path):
    code, _, err = run("vet", "score", tmp_path, "--work", tmp_path)
    assert code == 2 and "cannot be read" in err
