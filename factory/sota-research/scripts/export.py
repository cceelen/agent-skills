#!/usr/bin/env python3
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Export of a neutral kit for a trial of the research tooling. Standard library only.

  export.py DIR [--words FILE]

  DIR           the folder to write into. It must be outside each git repository, and it must be
                new or empty.
  --words FILE  words that the kit must not hold, one word or phrase in each line. If an exported
                file holds one, the program writes nothing and gives the file and the line.

The program writes only what a session needs to do the procedure: the tooling, the template of an
aspect specification, the rules of the kit, the two programs of the skill library-vetting that the
tooling loads, and two instruction files that the program makes. It does not write the sample
specification, the task of the reviewer of a plan and the list of the viewpoints of the review.
It writes the manifest of the seeds, and no seed document. It writes no documentation, no test, no
specification and no other skill: a text about a different subject must not become a finding of
the research.

The program prints each exported file, sorted. Result code 0: done. Result code 1: nothing was
exported. Result code 2: the input cannot be read.
"""

import pathlib
import re
import sys

import aspect
import check
import models
import render
import vet

ROOT = pathlib.Path(__file__).resolve().parents[3]
TOOLING = "factory/sota-research"
TEMPLATE = ".specify/templates/overrides/aspect-spec-template.md"
# Files of the tooling that a session of the research does not get. Only the examples of the
# programs use the sample. The task of the reviewer and the list name the viewpoints of the review.
LEFT_OUT = ("scripts/sample.py", "prompts/plan-review.md", "references/viewpoints.txt")
# The programs of a different skill that the tooling loads when it runs.
LOADED = (vet.COLLECTOR_PROGRAM, models.SHARED)

# The instruction file of the exported kit. {rules} is the block of the rules of the kit.
AGENTS = """\
# AGENTS.md

- Write to the owner in ASD-STE100 Simplified Technical English.
- The procedure is in `factory/sota-research/SKILL.md`. Read it and do its steps.

## Commit messages

- Use the Conventional Commits format: `type(scope): subject`. The scope is optional.
- Do not add a footer line.

{rules}"""
IMPORT = "@AGENTS.md\n"

MESSAGES = {
    "in-repository": "Nothing was exported: the folder must be outside each git repository.",
    "not-empty": "Nothing was exported: the folder '{0}' holds files. Give a new folder or an empty folder.",
    "word": "Nothing was exported: the file {0} uses the word '{1}' in line {2}.",
    "written": "Exported: {0}",
    "unreadable": "The input cannot be read: {0}",
}


def kit(root=ROOT):
    """The files of the kit: relative path -> (content in bytes, True for a program to run).

    >>> files = kit()
    >>> [path for path in sorted(files) if not path.startswith(TOOLING)]
    ['.specify/templates/overrides/aspect-spec-template.md', 'AGENTS.md', 'CLAUDE.md', 'rules/apply.py',
     'rules/evidence-before-action.md', 'skills/library-vetting/scripts/collect.py',
     'skills/library-vetting/scripts/models.py']

    The kit holds the tooling without the sample, without the task of the reviewer, without the
    list of the viewpoints of the review and without the files that Python makes when it runs.

    >>> tooling = {path.removeprefix(TOOLING + "/") for path in files if path.startswith(TOOLING)}
    >>> sorted(tooling & {"SKILL.md", "references/procedure.md", "scripts/check.py", "scripts/export.py"})
    ['SKILL.md', 'references/procedure.md', 'scripts/check.py', 'scripts/export.py']
    >>> sorted(tooling & set(LEFT_OUT)), [path for path in files if "__pycache__" in path]
    ([], [])
    >>> [(ROOT / TOOLING / path).is_file() for path in LEFT_OUT]
    [True, True, True]
    >>> "prompts/plan-review.md" in tooling, "references/viewpoints.txt" in tooling
    (False, False)

    No file of the kit holds the names of all viewpoints of the review. The kit holds the manifest
    of the seeds.

    >>> names = check.viewpoints()
    >>> len(names), [path for path, (text, _) in files.items() if all(n.encode() in text for n in names)]
    (7, [])
    >>> "references/seeds.md" in tooling
    True

    The kit holds the program of the index and the file of the synonyms.

    >>> sorted(tooling & {"scripts/index.py", "references/synonyms.txt"})
    ['references/synonyms.txt', 'scripts/index.py']

    No program needs a file that is left out: the examples of the programs load the sample, and
    no line of a program does.

    >>> programs = [text.decode() for path, (text, _) in files.items() if path.endswith(".py")]
    >>> [line for text in programs for line in text.splitlines() if line.strip() == "import sample"]
    []

    Each file that a program of the tooling loads from outside its folder is in the kit.

    >>> needed = [render.RULES_PROGRAM, vet.COLLECTOR_PROGRAM, models.SHARED, ROOT / TEMPLATE]
    >>> [path.relative_to(ROOT).as_posix() in files for path in needed]
    [True, True, True, True]

    A program keeps its mode. The instruction files hold the rules of the kit and no other rule
    of this repository.

    >>> files[TOOLING + "/scripts/check.py"][1], files[TOOLING + "/SKILL.md"][1], files["AGENTS.md"][1]
    (True, False, False)
    >>> agents = files["AGENTS.md"][0].decode()
    >>> render.rules_of_the_kit() in agents, files["CLAUDE.md"][0], len(agents.splitlines()) < 30
    (True, b'@AGENTS.md\\n', True)
    >>> aspect.long_sentences({"a": AGENTS.format(rules="")}), aspect.long_sentences(MESSAGES)
    ([], [])
    """
    root = pathlib.Path(root)
    sources = [p for p in sorted((root / TOOLING).rglob("*")) if p.is_file()]
    sources = [p for p in sources if p.relative_to(root / TOOLING).as_posix() not in LEFT_OUT]
    sources = [p for p in sources if "__pycache__" not in p.parts]
    rules = root / render.RULES_PROGRAM.parent.relative_to(ROOT)
    sources += [p for p in sorted(rules.iterdir()) if p.is_file()]
    sources += [root / TEMPLATE, *(root / p.relative_to(ROOT) for p in LOADED)]
    files = {}
    for path in sources:
        files[path.relative_to(root).as_posix()] = (path.read_bytes(), bool(path.stat().st_mode & 0o100))
    files["AGENTS.md"] = (AGENTS.format(rules=render.rules_of_the_kit()).encode("utf-8"), False)
    files["CLAUDE.md"] = (IMPORT.encode("utf-8"), False)
    return files


def words_in(files, words):
    """The message for each line of the kit that holds one of the words, sorted.

    >>> files = {"b.md": (b"No word here.\\nUse the Restore tool.\\n", False), "a.md": (b"A tool.", False)}
    >>> print("\\n".join(words_in(files, ["restore", "tool"])))
    Nothing was exported: the file a.md uses the word 'tool' in line 1.
    Nothing was exported: the file b.md uses the word 'restore' in line 2.
    Nothing was exported: the file b.md uses the word 'tool' in line 2.
    >>> words_in(files, ["rest"]), words_in(files, [])
    ([], [])
    """
    out = []
    for path, (content, _) in sorted(files.items()):
        for number, line in enumerate(content.decode("utf-8", errors="replace").splitlines(), 1):
            for word in words:
                if re.search(rf"(?<!\w){re.escape(word)}(?!\w)", line, re.I):
                    out.append(MESSAGES["word"].format(path, word, number))
    return out


def write(files, target):
    """Write the files of the kit into the folder. Returns the written paths, sorted.

    >>> import os, tempfile
    >>> target = pathlib.Path(tempfile.mkdtemp(prefix="sota-export-")) / "kit"
    >>> write({"b/run.py": (b"print(1)", True), "a.md": (b"text", False)}, target)
    ['a.md', 'b/run.py']
    >>> (target / "a.md").read_bytes(), [os.access(target / name, os.X_OK) for name in ("b/run.py", "a.md")]
    (b'text', [True, False])
    """
    target = pathlib.Path(target)
    for path, (content, runs) in sorted(files.items()):
        (target / path).parent.mkdir(parents=True, exist_ok=True)
        (target / path).write_bytes(content)
        (target / path).chmod(0o755 if runs else 0o644)
    return sorted(files)


def main(argv=None):
    r"""The command line. See the text at the start of this file.

    >>> import os, tempfile
    >>> import sample
    >>> outside = pathlib.Path(tempfile.mkdtemp(prefix="sota-export-"))
    >>> code, out, err = sample.run(main, outside / "kit")
    >>> code, err, out.splitlines() == [f"Exported: {path}" for path in sorted(kit())]
    (0, '', True)
    >>> out.splitlines()[:3]
    ['Exported: .specify/templates/overrides/aspect-spec-template.md', 'Exported: AGENTS.md',
     'Exported: CLAUDE.md']

    The folder holds the files of the kit and nothing more. A program can be run.

    >>> first = outside / "kit"
    >>> written = sorted(p.relative_to(first).as_posix() for p in first.rglob("*") if p.is_file())
    >>> written == sorted(kit()), os.access(first / TOOLING / "scripts/check.py", os.X_OK)
    (True, True)
    >>> absent = ("README.md", "docs", "tests", "specs", "pyproject.toml", "skills/library-vetting/SKILL.md")
    >>> [name for name in absent if (first / name).exists()]
    []

    The same input gives the same output.

    >>> _ = sample.run(main, outside / "second")
    >>> all((outside / "second" / path).read_bytes() == (first / path).read_bytes() for path in written)
    True

    The folder must be new or empty, and outside each git repository. If not, nothing is written.

    >>> sample.run(main, outside / "kit")[1].strip() == MESSAGES["not-empty"].format(outside / "kit")
    True
    >>> (outside / "empty").mkdir()
    >>> sample.run(main, outside / "empty")[0], (outside / "empty" / "AGENTS.md").is_file()
    (0, True)
    >>> (outside / "repo" / ".git").mkdir(parents=True)
    >>> code, out, _ = sample.run(main, outside / "repo" / "kit")
    >>> code, out.strip(), (outside / "repo" / "kit").exists()
    (1, 'Nothing was exported: the folder must be outside each git repository.', False)

    --words gives the words that the kit must not hold. A word in an exported file stops the
    export, and the program gives the file and the line.

    >>> words = outside / "words.txt"
    >>> _ = words.write_text("conventional commits\n", encoding="utf-8")
    >>> code, out, _ = sample.run(main, outside / "third", "--words", words)
    >>> code, out.splitlines()[0], (outside / "third").exists()
    (1, "Nothing was exported: the file AGENTS.md uses the word 'conventional commits' in line 8.", False)
    >>> _ = words.write_text("a word that no file " + "of the kit holds\n", encoding="utf-8")
    >>> sample.run(main, outside / "third", "--words", words)[0], (outside / "third" / "CLAUDE.md").is_file()
    (0, True)

    Input that cannot be read gives the result code 2. No argument prints the usage text.

    >>> _ = words.write_bytes(b"\xff\xfe")
    >>> code, _, err = sample.run(main, outside / "fourth", "--words", words)
    >>> code, err.startswith("The input cannot be read:"), (outside / "fourth").exists()
    (2, True, False)
    >>> code, _, err = sample.run(main)
    >>> code, "export.py DIR" in err, sample.run(main, "--words", words)[0]
    (2, True, 2)
    """
    args = list(sys.argv[1:] if argv is None else argv)
    if args[:1] == ["--selftest"]:
        sys.exit(aspect.selftest())
    words_file = check.option(args, "--words")
    target = next((a for a in args if not a.startswith("--")), "")
    if not target or args[0] in ("-h", "--help"):
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    try:
        words = check.read_words(words_file)
        files = kit()
    except (aspect.Unreadable, OSError) as e:
        print(MESSAGES["unreadable"].format(e), file=sys.stderr)
        sys.exit(2)
    target = pathlib.Path(target)
    reasons = words_in(files, words)
    if render.in_repository(target):
        reasons = [MESSAGES["in-repository"]]
    elif target.exists() and (not target.is_dir() or any(target.iterdir())):
        reasons = [MESSAGES["not-empty"].format(target)]
    if reasons:
        print("\n".join(reasons))
        sys.exit(1)
    for path in write(files, target):
        print(MESSAGES["written"].format(path))


if __name__ == "__main__":
    main()
