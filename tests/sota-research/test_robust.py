"""Input that is not as expected gives a finding or a result code, not a wrong write or a crash."""

import hashlib
import http.client
import json
import shutil

import pytest
from helpers import FIXTURE, module, run

GOOD = FIXTURE / "good"
SIGNALS = FIXTURE / "signals"
aspect = module("aspect")
check = module("check")
vet = module("vet")


def copy(tmp_path, name="spec"):
    target = tmp_path / name
    shutil.copytree(GOOD, target)
    return target


def edit(path, old, new, count=1):
    data = path.read_bytes().decode("utf-8")
    assert data.count(old) == count, old
    path.write_bytes(data.replace(old, new).encode("utf-8"))


# ---- lines and cells ----


@pytest.mark.parametrize("separator", [chr(0x2028), chr(0x2029), "\x0c", "\x0b", "\x85"])
def test_a_line_separator_character_does_not_move_the_write(tmp_path, separator):
    spec = copy(tmp_path)
    edit(spec / "spec.md", "A small specification", f"A small{separator}specification")
    edit(spec / "vetting.md", "Rubric for sources", f"Rubric{separator}for sources")
    before_spec, before_vetting = (spec / "spec.md").read_bytes(), (spec / "vetting.md").read_bytes()
    code, _, err = run("place", spec, "--write")
    assert code == 0 and err == ""
    # The results were in the files already: a write to the right rows changes no byte.
    assert (spec / "spec.md").read_bytes() == before_spec
    assert (spec / "vetting.md").read_bytes() == before_vetting


def test_crlf_files_keep_their_line_ends(tmp_path):
    spec = copy(tmp_path)
    for name in ("spec.md", "vetting.md", "evidence.md"):
        (spec / name).write_bytes((spec / name).read_bytes().replace(b"\n", b"\r\n"))
    edit(spec / "spec.md", "| 2, operative |", "| pending |")
    assert run("check", spec)[0] == 0
    code, _, err = run("place", spec, "--write")
    assert code == 0 and err == ""
    text = (spec / "spec.md").read_bytes()
    assert b"| 2, operative |" in text and text.count(b"\r\n") == text.count(b"\n")
    assert run("vet", "score", spec, "--work", SIGNALS, "--write")[0] == 0
    vetting = (spec / "vetting.md").read_bytes()
    assert vetting.count(b"\r\n") == vetting.count(b"\n")


def test_set_cell_refuses_a_cell_that_is_absent(tmp_path):
    path = tmp_path / "t.md"
    path.write_text("| a | b |\n|---|---|\n| short |\n")
    assert aspect.set_cell(path, 3, 1, "x") is False
    assert aspect.set_cell(path, 9, 0, "x") is False
    assert path.read_text() == "| a | b |\n|---|---|\n| short |\n"
    assert aspect.set_cell(path, 3, 0, "x | y") is True
    assert path.read_text() == "| a | b |\n|---|---|\n| x \\| y |\n"


def test_a_short_row_is_reported_and_not_a_crash(tmp_path):
    spec = copy(tmp_path)
    edit(
        spec / "spec.md",
        " | 1 | practice | the schedule of the program is in the repository | S-04 README; S-01 section 3 |",
        " |",
    )
    code, out, err = run("place", spec, "--write")
    assert code == 1 and "Traceback" not in err
    assert "The program cannot write the cell 'level'" in out
    assert run("check", spec)[0] == 1


@pytest.mark.parametrize("name", ["spec.md", "evidence.md", "vetting.md"])
def test_a_file_that_is_not_utf_8_gives_result_code_2(tmp_path, name):
    spec = copy(tmp_path)
    (spec / name).write_bytes((spec / name).read_bytes() + b"\xff\n")
    for command in (
        ["check", spec],
        ["place", spec],
        ["render", spec, "--commit", "0000000", "--out", tmp_path / "o"],
    ):
        code, _, err = run(*command)
        assert code == 2 and "Traceback" not in err and "not UTF-8" in err
    code, _, err = run("vet", "score", spec, "--work", SIGNALS)
    assert code == 2 and "Traceback" not in err


def test_other_files_that_are_not_utf_8(tmp_path):
    bad = tmp_path / "bad.txt"
    bad.write_bytes(b"\xff\xfe")
    assert run("check", GOOD, "--words", bad)[0] == 2
    assert run("check", GOOD, "--previous", bad)[0] == 2
    assert run("place", GOOD, "--rubric", bad)[0] == 2
    assert run("vet", "score", GOOD, "--work", SIGNALS, "--rubric", bad)[0] == 2


def test_a_byte_order_mark_is_accepted(tmp_path):
    spec = copy(tmp_path)
    (spec / "spec.md").write_bytes(b"\xef\xbb\xbf" + (spec / "spec.md").read_bytes())
    assert aspect.load(spec)["is_aspect"]
    assert run("check", spec)[0] == 0


# ---- the check ----


def test_an_empty_checklist_and_no_sources_fail(tmp_path):
    spec = copy(tmp_path)
    lines = [x for x in (spec / "spec.md").read_text().splitlines() if not x.startswith(("| C-0", "| S-0"))]
    (spec / "spec.md").write_text("\n".join(lines) + "\n")
    code, out, _ = run("check", spec)
    assert code == 1 and "FAIL checklist-empty" in out and "FAIL sources-empty" in out
    assert run("render", spec, "--commit", "0000000", "--out", tmp_path / "o")[0] == 1


def test_an_unread_source_and_a_pending_source_together_wait(tmp_path):
    spec = copy(tmp_path)
    # C-04 cites S-03 only. Add S-02 as a source that was not read, and make S-03 pending.
    edit(spec / "spec.md", '| S-03 "After the drill" |', '| S-03 "After the drill"; S-02 section 9 |')
    edit(spec / "spec.md", "| CC BY 4.0 | full |", "| CC BY 4.0 | no |")
    edit(
        spec / "evidence.md",
        "| abstract; section 4 | C-01, C-02;",
        "| abstract; section 4 | C-01, C-02, C-04;",
    )
    edit(
        spec / "vetting.md",
        "| 9 of 10 | 2026-01-10 | A. Person, 2026-01-15 |",
        "| 9 of 10 | 2026-01-10 | pending |",
    )
    _, out, _ = run("check", spec, "--json")
    result = json.loads(out)
    assert "C-04" in result["remains"]["waiting"]
    # C-02 cites only S-02, which was not read.
    assert ("only-unread-source", "C-02") in [(f["rule"], f["id"]) for f in result["findings"]]


def test_a_gate_rejection_is_stronger_than_an_old_confirmation(tmp_path):
    spec = copy(tmp_path)
    edit(spec / "vetting.md", "| S-03 | page | pass |", "| S-03 | page | rejected: no date |")
    code, out, _ = run("check", spec, "--json")
    result = json.loads(out)
    assert code == 1
    assert [(f["rule"], f["id"]) for f in result["findings"]] == [("only-rejected-source", "C-04")]
    assert result["remains"]["vettings"] == ["S-03"]


@pytest.mark.parametrize(
    ("value", "accepted"),
    [
        ("A. Person, 2026-01-15", True),
        ("pending", False),
        ("no", False),
        ("A. Person", False),
        ("2026-01-15", False),
    ],
)
def test_the_acceptance_needs_a_person_and_a_date(value, accepted):
    assert check.is_accepted({"head": {"accepted": value}}) is accepted


def test_a_principle_is_found_in_each_case():
    assert aspect.principles("Constitution iii; constitution IX") == ["III", "IX"]


# ---- the calculation ----


@pytest.mark.parametrize("answer", ["2.5 (judgement)", "1/2 (judgement)", "2,5", "two"])
def test_an_answer_that_is_not_a_whole_number_is_missing(tmp_path, answer):
    spec = copy(tmp_path)
    edit(spec / "vetting.md", "| C-05 | 2 (judgement) |", f"| C-05 | {answer} |")
    code, out, _ = run("place", spec)
    assert code == 1 and "C-05: pending. The answer 'severity' is missing." in out


def test_a_rubric_scale_that_can_give_a_cost_of_zero_is_refused(tmp_path):
    rubric = tmp_path / "rubric.txt"
    text = (
        module("place").__file__
        and (GOOD.parents[3] / "factory/sota-research/scripts/rubric-items.txt").read_text()
    )
    rubric.write_text(text.replace("question adopt 1-3", "question adopt 0-3"))
    code, _, err = run("place", GOOD, "--rubric", rubric)
    assert code == 2 and "must start at 1" in err


# ---- the renderer ----


def test_the_description_is_a_valid_string_for_each_title(tmp_path):
    spec = copy(tmp_path)
    edit(
        spec / "spec.md",
        "# Aspect specification: Backups of project data",
        '# Aspect specification: Backups: "data" #1 * and more',
    )
    out = tmp_path / "o"
    assert run("render", spec, "--commit", "0000000", "--out", out)[0] == 0
    line = (out / "skills/backups/SKILL.md").read_text().splitlines()[2]
    assert line.startswith('description: "')
    assert 'Backups: "data" #1 * and more' in json.loads(line.removeprefix("description: "))


@pytest.mark.parametrize("target", ["../../escape/", "/etc/x", "skills/../../x", "a b"])
def test_a_target_folder_outside_the_repository_is_refused(tmp_path, target):
    spec = copy(tmp_path)
    edit(
        spec / "spec.md",
        "- **Goal**: Each record",
        f"- **Target folder**: `{target}`\n- **Goal**: Each record",
    )
    out = tmp_path / "o" / "deep" / "root"
    code, text, _ = run("render", spec, "--commit", "0000000", "--out", out)
    assert code == 1 and "must be a folder inside the repository" in text
    assert not (tmp_path / "o").exists()


@pytest.mark.parametrize("args", [["--commit", "x -->`evil"], ["--commit", "0000000", "--branch", "a`b -->"]])
def test_a_commit_or_a_branch_that_can_break_the_stamp_is_refused(tmp_path, args):
    code, out, _ = run("render", GOOD, *args, "--out", tmp_path / "o")
    assert code == 1 and "Nothing" not in out and not (tmp_path / "o").exists()


def test_a_pending_level_stops_the_rendering(tmp_path):
    spec = copy(tmp_path)
    edit(spec / "spec.md", "| 3, regulatory |", "| pending |")
    code, out, _ = run("render", spec, "--commit", "0000000", "--out", tmp_path / "o")
    assert code == 1 and "these items have no level" in out and "C-03" in out


def test_the_digest_is_the_same_for_a_different_line_end(tmp_path):
    lf, crlf = copy(tmp_path, "lf"), copy(tmp_path, "crlf")
    (crlf / "spec.md").write_bytes((crlf / "spec.md").read_bytes().replace(b"\n", b"\r\n"))
    for spec in (lf, crlf):
        assert run("render", spec, "--commit", "0000000", "--out", tmp_path / f"o-{spec.name}")[0] == 0
    a = (tmp_path / "o-lf/skills/backups/SKILL.md").read_text()
    assert a == (tmp_path / "o-crlf/skills/backups/SKILL.md").read_text()
    assert hashlib.sha256((lf / "spec.md").read_bytes()).hexdigest() in a


# ---- the vetting ----


def test_a_page_cannot_give_a_date_that_does_not_exist_or_is_in_the_future():
    page = '<meta name="date" content="2026-13-45"><meta name="date" content="2099-01-01">'
    page += '<time datetime="2025-03-04">'
    assert vet.page_signals(page, "https://a.example/", None, "2026-01-10")["date"] == "2025-03-04"
    assert (
        vet.page_signals('<meta name="date" content="2099-01-01">', "https://a.example/", None, "2026-01-10")[
            "date"
        ]
        is None
    )
    assert vet.age_days("2099-01-01", "2026-01-10") is None
    assert vet.age_days("2024-02-30", "2026-01-10") is None


@pytest.mark.parametrize(
    ("cell", "date"),
    [
        ("2.0, 2025-03", "2025-03-01"),
        ("2024", "2024-01-01"),
        ("commit of 2025-11-02", "2025-11-02"),
        ("RFC 9110", None),
        ("v2.0.1234", None),
        ("0000", None),
        ("2024-02-30", None),
        ("version 3", None),
    ],
)
def test_the_date_of_section_2(cell, date):
    assert vet.recorded_date({"version or date": cell}, "2026-01-10") == date


def test_a_future_date_in_a_signal_file_is_not_used(tmp_path):
    spec, work = copy(tmp_path), tmp_path / "work"
    shutil.copytree(SIGNALS, work)
    record = json.loads((work / "S-03.json").read_text())
    record["signals"].update(date="2099-01-01", age_days=None)
    (work / "S-03.json").write_text(json.dumps(record))
    edit(spec / "spec.md", "| A. Writer | 2025-06-01 |", "| A. Writer | RFC 9110 |")
    code, out, err = run("vet", "score", spec, "--work", work)
    assert code == 1 and "Traceback" not in err
    assert "S-03: page, rejected by a gate: no date." in out


@pytest.mark.parametrize(
    "content", ["[]", '{"kind": "page"}', "not json", '{"kind": "x", "signals": {}, "today": "2026-01-10"}']
)
def test_a_signal_file_of_the_wrong_form_is_not_used(tmp_path, content):
    work = tmp_path / "work"
    shutil.copytree(SIGNALS, work)
    (work / "S-03.json").write_text(content)
    code, out, err = run("vet", "score", GOOD, "--work", work)
    assert code == 1 and "Traceback" not in err
    assert "S-03: not scored. Run the collection for this source first." in out


def test_signals_of_a_different_address_are_not_used(tmp_path):
    spec = copy(tmp_path)
    edit(spec / "spec.md", "https://writer.example/drills", "https://writer.example/new")
    _, out, _ = run("vet", "score", spec, "--work", SIGNALS)
    assert "S-03: not scored. Run the collection for this source first." in out


def test_wrong_options_give_result_code_2(tmp_path):
    assert run("vet", "score", GOOD, "--work", SIGNALS, "--max-age", "abc")[0] == 2
    assert run("vet", "score", GOOD)[0] == 2
    assert run("vet", "collect", GOOD, "--work", tmp_path / "w", "--today", "2026-13-45")[0] == 2
    assert not (tmp_path / "w").exists()


def test_a_source_identifier_cannot_leave_the_work_folder(tmp_path, monkeypatch):
    spec = copy(tmp_path)
    edit(
        spec / "spec.md", "| S-03 | Notes on restore drills |", "| ../../escaped | Notes on restore drills |"
    )
    monkeypatch.setattr(vet, "fetch", lambda url: ("", None))
    monkeypatch.setattr(vet, "COLLECTOR_PROGRAM", tmp_path / "absent.py")
    work = tmp_path / "a" / "b" / "work"
    code = vet.cmd_collect(aspect.load(spec), ["collect", "--work", str(work), "--today", "2026-01-10"])
    assert code == 1
    assert sorted(p.name for p in work.iterdir()) == ["S-04.json"]
    assert not list(tmp_path.rglob("escaped*"))


def test_a_named_source_that_does_not_exist_is_reported(tmp_path, capsys):
    code = vet.cmd_collect(
        aspect.load(GOOD), ["collect", "S-99", "--work", str(tmp_path / "w"), "--today", "2026-01-10"]
    )
    assert code == 1 and "no independent source with the identifier 'S-99'" in capsys.readouterr().out


@pytest.mark.parametrize(
    "error", [http.client.IncompleteRead(b""), http.client.InvalidURL("bad"), ValueError("bad")]
)
def test_each_error_of_a_page_is_recorded(monkeypatch, error):
    def fail(url):
        raise error

    monkeypatch.setattr(vet, "fetch", fail)
    signals, errors = vet.collect_page("https://a.example/", "2026-01-10")
    assert signals["reachable"] is None and "reachable" in errors


@pytest.mark.parametrize(
    "url",
    [
        "file:///etc/passwd",
        "ftp://a.example/",
        "http://127.0.0.1:8000/x",
        "http://localhost/",
        "http://169.254.169.254/",
        "http://10.0.0.1/",
        "http://[::1]/",
    ],
)
def test_only_a_public_http_address_is_fetched(url):
    assert vet.public_host(url) is False
    with pytest.raises(OSError, match="not a public"):
        vet.fetch(url)


def test_a_redirect_to_a_local_address_is_refused():
    handler = vet.OnlyHttp()
    assert handler.redirect_request(None, None, 302, "Found", {}, "http://127.0.0.1/admin") is None
    assert handler.redirect_request(None, None, 302, "Found", {}, "file:///etc/passwd") is None


def test_the_answer_record_is_not_found_inside_a_different_word():
    assert vet.RECORD.search("track record: no; record: yes").group(1) == "yes"
    assert vet.RECORD.search("track-record: no") is None
