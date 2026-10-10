#!/usr/bin/env python3
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Setup of a neutral environment of the factory, from nothing. Standard library only.

  init.py KIT WORK [--file ID=PATH ...] [--today DATE] [--again] [--manifest FILE]

  KIT              the folder of the neutral kit. It must be new or empty.
  WORK             the work folder for the seed documents and their converted text
  --file ID=PATH   the file of one seed, for a seed that the owner gives
  --today DATE     the date for WORK/seeds.json (YYYY-MM-DD). The program does not read the clock.
  --again          remove a KIT that this program made, and make it again. WORK is kept: a seed
                   that is there is not retrieved again.
  --manifest FILE  a different manifest of the seeds, for tests

The two folders must be outside each git repository, and neither can be in the other.

The program does these steps in this order:

1. It writes the neutral kit into KIT, as export.py does.
2. It writes the marker file `.factory-kit` into KIT, with the commit of this repository.
3. It makes KIT a git repository with the branch `main` and one commit. Without the program
   `git`, it says so and continues.
4. It retrieves the seeds into WORK and builds the index of their text, as `seed.py get` does.
5. It prints what a person does next.

The program removes only a folder that holds the marker file. No seed document and no converted
text is written into KIT.

Result code 0: the kit is made, and each seed is retrieved or recorded. Result code 1: the kit is
made, and a seed failed, changed or waits for the owner. Result code 2: nothing was made, because
the arguments are wrong or the input cannot be read.
"""

import json
import os
import pathlib
import shutil
import subprocess
import sys

import aspect
import export
import pdf
import render
import seed

ROOT = export.ROOT
MARKER = ".factory-kit"
MARKER_TEXT = (
    "This folder is a kit of the factory. The program init.py made it.\nCommit of the repository: {0}\n"
)
NOT_KNOWN = "not known"
# Git gives these variables to a hook. A git command for a different folder must not get them.
HOOK_VARIABLES = ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_PREFIX", "GIT_OBJECT_DIRECTORY")
# The commit of the kit names no person, and it does not use the settings of one person.
GIT = ["git", "-c", "user.name=factory", "-c", "user.email=factory@localhost", "-c", "commit.gpgsign=false"]
STEPS = (
    ["init", "--quiet", "--initial-branch=main"],
    ["add", "--all"],
    ["commit", "--quiet", "--no-verify", "--message", "chore: make the kit of the factory"],
)

MESSAGES = {
    "in-repository": "Nothing was made: the folders KIT and WORK must be outside each git repository.",
    "nested": "Nothing was made: KIT and WORK must be two folders, and neither can be in the other.",
    "not-a-kit": (
        "Nothing was made: the folder '{0}' holds files and no marker of this program. "
        "It was not removed. Give a new folder."
    ),
    "is-a-kit": "Nothing was made: the folder '{0}' is a kit of this program. Add --again to make it again.",
    "removed": "Removed: the kit in {0}",
    "made": "Made: the kit in {0}, with {1} files, from the commit {2}.",
    "repository": "Made: a git repository in the kit, with the branch main and one commit.",
    "no-git": "The program git is not installed. The kit is not a git repository.",
    "git-failed": "The kit is not a complete git repository: git stopped with an error: {0}",
    "next-head": "Do these steps next:",
    "next-models": "- Go into the folder {0}. Run: uv run factory/sota-research/scripts/models.py apply",
    "next-file": (
        "- Get the file of the seed '{0}'. "
        "Then run: uv run factory/sota-research/scripts/seed.py get {1} --file {0}=PATH"
    ),
    "next-session": "- Start the session of the research in the folder {0}.",
    "unreadable": "The input cannot be read: {0}",
}


def git(run, folder, *args):
    r"""Run one git command in a folder. Returns (True, the output) or (False, the first line of the error).

    Without the program git, the result is (False, None).

    >>> class Done:
    ...     returncode, stdout, stderr = 0, "abc1234\n", ""
    >>> class Bad:
    ...     returncode, stdout, stderr = 128, "", "fatal: not a git repository\nmore\n"
    >>> def absent(*args, **options):
    ...     raise FileNotFoundError("git")
    >>> def show(args, **options):
    ...     print(args[-2:], sorted(set(HOOK_VARIABLES) & set(options["env"])), options["cwd"])
    ...     return Done
    >>> os.environ["GIT_DIR"] = "a hook gives this variable"
    >>> git(show, "folder", "rev-parse", "HEAD")
    ['rev-parse', 'HEAD'] [] folder
    (True, 'abc1234')
    >>> del os.environ["GIT_DIR"]
    >>> git(lambda *a, **k: Bad, ".", "status"), git(absent, ".", "status")
    ((False, 'fatal: not a git repository'), (False, None))
    """
    env = {name: value for name, value in os.environ.items() if name not in HOOK_VARIABLES}
    try:
        done = run([*GIT, *args], cwd=folder, env=env, capture_output=True, text=True, check=False)
    except OSError:
        return False, None
    if done.returncode:
        return False, (done.stderr.strip().splitlines() or [str(done.returncode)])[0]
    return True, done.stdout.strip()


def commit_of(run, root=ROOT):
    """The commit of this repository, or "not known" when git cannot tell.

    >>> class Done:
    ...     returncode, stdout, stderr = 0, "abc1234\\n", ""
    >>> class Bad:
    ...     returncode, stdout, stderr = 128, "", ""
    >>> commit_of(lambda *a, **k: Done), commit_of(lambda *a, **k: Bad)
    ('abc1234', 'not known')
    """
    passed, text = git(run, root, "rev-parse", "HEAD")
    return text if passed and text else NOT_KNOWN


def make_repository(run, kit):
    """Make the kit a git repository with the branch main and one commit. Returns the line to print.

    >>> calls = []
    >>> class Done:
    ...     returncode, stdout, stderr = 0, "", ""
    >>> def record(args, **options):
    ...     calls.append(args[len(GIT)])
    ...     return Done
    >>> make_repository(record, "kit"), calls
    ('Made: a git repository in the kit, with the branch main and one commit.', ['init', 'add', 'commit'])

    A step that fails stops the steps, and the line says so. The program continues.

    >>> class Bad:
    ...     returncode, stdout, stderr = 1, "", "error: no commit"
    >>> make_repository(lambda args, **options: Bad if "commit" in args else Done, "kit")
    'The kit is not a complete git repository: git stopped with an error: error: no commit'
    >>> def absent(*args, **options):
    ...     raise FileNotFoundError("git")
    >>> make_repository(absent, "kit")
    'The program git is not installed. The kit is not a git repository.'
    """
    for step in STEPS:
        passed, text = git(run, kit, *step)
        if not passed:
            return MESSAGES["no-git"] if text is None else MESSAGES["git-failed"].format(text)
    return MESSAGES["repository"]


def is_kit(folder):
    """True if this program made the folder: it holds the marker file.

    >>> import tempfile
    >>> folder = pathlib.Path(tempfile.mkdtemp(prefix="sota-init-"))
    >>> is_kit(folder), is_kit(folder / "absent")
    (False, False)
    >>> _ = (folder / MARKER).write_text(MARKER_TEXT.format("abc1234"), encoding="utf-8")
    >>> is_kit(folder)
    True
    """
    return (pathlib.Path(folder) / MARKER).is_file()


def refusal(kit, work, again):
    """The reason not to make the kit, or None. The two paths are resolved.

    >>> import tempfile
    >>> outside = pathlib.Path(tempfile.mkdtemp(prefix="sota-init-")).resolve()
    >>> refusal(outside / "kit", outside / "work", False)
    >>> (outside / "empty").mkdir()
    >>> refusal(outside / "empty", outside / "work", False)

    The two folders are outside each git repository, and neither is in the other.

    >>> (outside / "repo" / ".git").mkdir(parents=True)
    >>> def reason(a, b, again=False):
    ...     return refusal(outside / a, outside / b, again)
    >>> reason("repo/kit", "work") == reason("kit", "repo/work") == MESSAGES["in-repository"]
    True
    >>> reason("kit", "kit") == reason("kit", "kit/w", True) == reason("w/kit", "w") == MESSAGES["nested"]
    True

    A folder with files and without the marker is never removed. A file in the place of the folder
    is not removed also.

    >>> (outside / "other").mkdir()
    >>> _ = (outside / "other" / "notes.txt").write_text("private")
    >>> [refusal(outside / "other", outside / "work", again)[:60] for again in (False, True)] == [
    ...     MESSAGES["not-a-kit"].format(outside / "other")[:60]] * 2
    True
    >>> refusal(outside / "other" / "notes.txt", outside / "work", True)[:29]
    'Nothing was made: the folder '

    A kit of this program is made again only with --again. Such a kit is a git repository.

    >>> _ = (outside / "other" / MARKER).write_text("")
    >>> (outside / "other" / ".git").mkdir()
    >>> refusal(outside / "other", outside / "work", False) == MESSAGES["is-a-kit"].format(outside / "other")
    True
    >>> refusal(outside / "other", outside / "work", True)
    """
    if render.in_repository(kit.parent) or render.in_repository(work):
        return MESSAGES["in-repository"]
    if kit == work or kit in work.parents or work in kit.parents:
        return MESSAGES["nested"]
    if not kit.exists() or (kit.is_dir() and not any(kit.iterdir())):
        return None
    if not is_kit(kit):
        return MESSAGES["not-a-kit"].format(kit)
    return None if again else MESSAGES["is-a-kit"].format(kit)


def next_steps(kit, work):
    r"""The lines that tell a person what to do next. A seed that waits for the owner gets one line.

    >>> import tempfile
    >>> work = pathlib.Path(tempfile.mkdtemp(prefix="sota-init-"))
    >>> records = [{"id": "a", "state": seed.RETRIEVED}, {"id": "b", "state": seed.WAITS}]
    >>> _ = (work / "seeds.json").write_text(json.dumps({"seeds": records}))
    >>> print("\n".join(next_steps("KIT", work)).replace(str(work), "WORK"))
    Do these steps next:
    - Go into the folder KIT. Run: uv run factory/sota-research/scripts/models.py apply
    - Get the file of the seed 'b'. Then run: uv run factory/sota-research/scripts/seed.py get WORK
      --file b=PATH
    - Start the session of the research in the folder KIT.
    >>> aspect.long_sentences(MESSAGES), aspect.long_sentences({"a": MARKER_TEXT})
    ([], [])
    """
    records = json.loads(aspect.read_text(work / "seeds.json"))["seeds"]
    waiting = sorted(record["id"] for record in records if record["state"] == seed.WAITS)
    return [
        MESSAGES["next-head"],
        MESSAGES["next-models"].format(kit),
        *(MESSAGES["next-file"].format(ident, work) for ident in waiting),
        MESSAGES["next-session"].format(kit),
    ]


def main(argv=None, run=subprocess.run, download=pdf.download, ask=None):
    r"""The command line. See the text at the start of this file. Returns the result code.

    The examples use a manifest with three seeds, and functions in the place of git, of the
    converter and of the network.

    >>> import tempfile
    >>> import sample
    >>> outside = pathlib.Path(tempfile.mkdtemp(prefix="sota-init-")).resolve()
    >>> kit, work, manifest = outside / "kit", outside / "work", outside / "seeds.md"
    >>> head = "| Id | Document | Issuer | Version or date | Kind | Address | sha256 | Terms | Row read on |"
    >>> row = "| {0} | A guide | An issuer | 2.0 | {1} | https://a.example/{0} |  | public | 2026-01-05 |"
    >>> rows = [row.format("a", "pdf"), row.format("b", "owner file"), row.format("c", "page")]
    >>> _ = manifest.write_text("\n".join([head, "|---|---|---|---|---|---|---|---|---|", *rows]) + "\n")
    >>> calls = []
    >>> class Git:
    ...     returncode, stdout, stderr = 0, "abc1234\n", ""
    >>> class Converter:
    ...     returncode, stdout, stderr = 0, "one\x0ctwo\x0c".encode(), b""
    >>> def tools(args, **options):
    ...     calls.append(args[len(GIT)] if args[0] == "git" else args[0])
    ...     return Git if args[0] == "git" else Converter
    >>> def network(address):
    ...     calls.append(address)
    ...     return b"%PDF-1.7"
    >>> def init(*args, run=tools, download=network):
    ...     program = lambda argv: main(argv, run=run, download=download)
    ...     code, out, err = sample.run(program, kit, work, "--manifest", manifest, *args)
    ...     print((out + err).replace(str(outside), "OUTSIDE").strip())
    ...     return code
    >>> init("--today", "2026-01-05")
    Made: the kit in OUTSIDE/kit, with ... files, from the commit abc1234.
    Made: a git repository in the kit, with the branch main and one commit.
    a: retrieved: 2 pages, sha256 ...
    a: the manifest has no digest for this seed. Write this digest into its row: ...
    b: the owner must give the file. Get it from https://a.example/b. Then add --file b=PATH.
    c: recorded: a web reader reads the page https://a.example/c.
    Written: seeds.json
    Index: documents ...
    Do these steps next:
    - Go into the folder OUTSIDE/kit. Run: uv run factory/sota-research/scripts/models.py apply
    - Get the file of the seed 'b'. Then run: uv run factory/sota-research/scripts/seed.py get OUTSIDE/work
      --file b=PATH
    - Start the session of the research in the folder OUTSIDE/kit.
    1
    >>> calls
    ['rev-parse', 'init', 'add', 'commit', 'https://a.example/a', 'pdftotext']

    The kit holds the files of the export and the marker with the commit. It holds no seed.

    >>> written = sorted(p.relative_to(kit).as_posix() for p in kit.rglob("*") if p.is_file())
    >>> written == sorted([*export.kit(), MARKER]), (kit / MARKER).read_text().splitlines()[1]
    (True, 'Commit of the repository: abc1234')
    >>> sorted(p.relative_to(work).as_posix() for p in work.rglob("*") if p.is_file())
    ['converted/.reader-may-read', 'converted/a.md', 'index.sqlite', 'seeds.json', 'seeds/a.pdf']
    >>> json.loads((work / "seeds.json").read_text())["date"]
    '2026-01-05'

    Without --again, a kit is not made again. With --again, the kit is removed and made again.
    The work folder is kept: a seed that is there is not retrieved again.

    >>> _ = (kit / "old.txt").write_text("a file of the old kit")
    >>> init()
    Nothing was made: the folder 'OUTSIDE/kit' is a kit of this program. Add --again to make it again.
    2
    >>> given = outside / "b.pdf"
    >>> _ = given.write_bytes(b"%PDF-1.7 b")
    >>> def forbidden(address):
    ...     raise AssertionError("nothing is downloaded again")
    >>> init("--again", "--file", f"b={given}", download=forbidden)
    Removed: the kit in OUTSIDE/kit
    Made: the kit in OUTSIDE/kit, with ... files, from the commit abc1234.
    Made: a git repository in the kit, with the branch main and one commit.
    a: retrieved before: 2 pages, sha256 ... Nothing was retrieved again.
    a: the manifest has no digest for this seed. Write this digest into its row: ...
    b: retrieved: 2 pages, sha256 ...
    c: recorded: a web reader reads the page https://a.example/c.
    Written: seeds.json
    Index: documents ...
    Do these steps next:
    - Go into the folder OUTSIDE/kit. Run: uv run factory/sota-research/scripts/models.py apply
    - Start the session of the research in the folder OUTSIDE/kit.
    0
    >>> (kit / "old.txt").exists(), is_kit(kit), (work / "seeds/b.pdf").is_file()
    (False, True, True)

    A folder that this program did not make is never removed.

    >>> (kit / MARKER).unlink()
    >>> init("--again")
    Nothing was made: the folder 'OUTSIDE/kit' holds files and no marker of this program. It was not removed.
    Give a new folder.
    2
    >>> (kit / "AGENTS.md").is_file()
    True

    Without the program git, the kit is made, and the commit is not known.

    >>> def no_git(args, **options):
    ...     if args[0] == "git":
    ...         raise FileNotFoundError("git")
    ...     return Converter
    >>> shutil.rmtree(kit)
    >>> init(run=no_git)
    Made: the kit in OUTSIDE/kit, with ... files, from the commit not known.
    The program git is not installed. The kit is not a git repository.
    a: retrieved before...
    0
    >>> (kit / MARKER).read_text().splitlines()[1]
    'Commit of the repository: not known'

    Wrong arguments and input that cannot be read give the result code 2, and nothing is made.

    >>> shutil.rmtree(kit)
    >>> init("--file", "z=z.pdf"), init("--today", "tomorrow"), kit.exists()
    Nothing was retrieved: no seed has the identifier 'z'.
    Nothing was retrieved: write the date as YYYY-MM-DD.
    (2, 2, False)
    >>> _ = manifest.write_text("\n".join([head, "|---|---|---|---|---|---|---|---|---|", rows[0]]))
    >>> _ = manifest.write_text(manifest.read_text().replace("| pdf |", "| book |"))
    >>> init()
    seeds.md:3 a: The kind 'book' is not permitted. Use pdf, page or owner file.
    2
    >>> manifest.unlink()
    >>> init()
    The input cannot be read: OUTSIDE/seeds.md: No such file or directory
    2
    >>> [sample.run(main, *args)[0] for args in ((), ("--help",), (kit,), (kit, work, "more"))], kit.exists()
    ([2, 2, 2, 2], False)
    """
    args = [str(a) for a in (sys.argv[1:] if argv is None else argv)]
    manifest, today = seed.check.option(args, "--manifest"), seed.check.option(args, "--today")
    files, again = seed.given_files(args), "--again" in args
    names = [a for a in args if not a.startswith("--")]
    if len(names) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    kit, work = (pathlib.Path(name).resolve() for name in names)
    try:
        seeds, _, problems = seed.read_manifest(manifest or seed.MANIFEST)
        files_of_kit = export.kit()
    except (aspect.Unreadable, OSError) as e:
        print(MESSAGES["unreadable"].format(e), file=sys.stderr)
        return 2
    reason = "\n".join(problems) or refusal(kit, work, again) or seed.wrong_options(seeds, files, today)
    if reason:
        print(reason)
        return 2
    if is_kit(kit):
        shutil.rmtree(kit)
        print(MESSAGES["removed"].format(kit))
    commit = commit_of(run)
    files_of_kit[MARKER] = (MARKER_TEXT.format(commit).encode("utf-8"), False)
    print(MESSAGES["made"].format(kit, len(export.write(files_of_kit, kit)), commit))
    print(make_repository(run, kit))
    files = seed.ask_owner(seeds, files, work, ask if argv is not None else seed.person_at_the_keyboard())
    code, lines = seed.get(work, seeds, files, today, False, download, run)
    print("\n".join(lines + next_steps(kit, work)))
    return code


if __name__ == "__main__":
    if sys.argv[1:2] == ["--selftest"]:
        sys.exit(aspect.selftest())
    sys.exit(main())
