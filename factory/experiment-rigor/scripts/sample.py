#!/usr/bin/env python3
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Sample data for the examples of experiment.py. Standard library only.

  folder(*edits, files=None)  writes a small and correct registration into a new temporary folder
  agent(reply, init, code)    a function in the place of subprocess.run: the stream of one session
  judge(folder, answer)       writes judgements.md for each code of blind-key.json

The examples (doctests) of experiment.py use this module. The program validates itself with the
option --selftest, and needs no test file. The experiment of the sample is invented.
"""

import doctest
import json
import pathlib
import sys
import tempfile
import types

REGISTRATION = """\
# Experiment: a polite prompt

## 1. Question

- **Quote**: "Does the word please change the answer?"
- **Date**: 2026-01-10
- **Decision**: what the owner does after each outcome.
  - `confirmed`: add the word to the prompt of the skill.
  - `refuted`: keep the prompt as it is.
  - `not decided`: run a larger experiment.

## 2. Hypothesis

- **Statement**: With the word please, more answers hold a greeting.
- **Forbidden result**: The arm polite has no more greetings than the arm plain.
- **Criterion**: C-1
- **Confirmed when**: `polite - plain >= 3`
- **Refuted when**: `polite - plain <= 0`

## 3. Measure

| Id | Question | Answered by | Pattern | Where |
|---|---|---|---|---|
| C-1 | Does the answer hold a greeting? | program | `(?i)\\bhello\\b` | final |
| C-2 | Is the answer friendly? | judge | | final |
| C-3 | Does the note hold a year? | judge | | file:note.txt |
| C-4 | Does the note hold a year? | program | `\\d{4}` | file:note.txt |

## 4. Arms

| Id | What differs | Prompt files | Input folder |
|---|---|---|---|
| plain | No word please. | prompts/plain.md | inputs/base |
| polite | The word please. | prompts/polite.md | inputs/base |

## 5. Subject

- **Product**: claude
- **Model**: small-model
- **Tools**: Read, Write
- **Runs for each arm**: 5
- **Time limit**: 60
- **Git repository**: no

## 6. Words of the expected answer

- `hello`

## 7. Predictions

| Arm | Criterion | Predicted count |
|---|---|---|
| plain | C-1 | 1 |
| plain | C-2 | 4 |
| plain | C-3 | 0 |
| plain | C-4 | 0 |
| polite | C-1 | 4 |
| polite | C-2 | 5 |
| polite | C-3 | 0 |
| polite | C-4 | 0 |

## 8. Environment

- **Plugins**: (none)
- **Connectors**: (none)
- **Skills**: (none)
- **Agents**: (none)
"""

FILES = {
    "prompts/plain.md": "Write one line to a new colleague.\n",
    "prompts/polite.md": "Write one line to a new colleague, please.\n",
    "inputs/base/note.txt": "A note for the colleague.\n",
}

INIT = {
    "type": "system",
    "subtype": "init",
    "claude_code_version": "0.0.0",
    "model": "small-model",
    "tools": ["Write", "Read"],
    "mcp_servers": [],
    "plugins": [{"name": "cc-plugin-telemetry", "path": "builtin"}],
    "skills": [],
    "agents": ["claude", "Plan"],
}


def folder(*edits, files=None):
    r"""Write the sample into a new temporary folder. Returns the path.

    Each edit is (old text, new text) for registration.md. `files` adds a file, or removes one
    with the value None.

    >>> path = folder(("small-model", "other-model"), files={"inputs/base/more.txt": "x", "prompts/plain.md": None})
    >>> sorted(p.relative_to(path).as_posix() for p in path.rglob("*") if p.is_file())
    ['inputs/base/more.txt', 'inputs/base/note.txt', 'prompts/polite.md', 'registration.md']
    >>> "- **Model**: other-model" in (path / "registration.md").read_text()
    True

    An edit that finds no text is an error of the example.

    >>> folder(("no such text", ""))
    Traceback (most recent call last):
        ...
    ValueError: the sample does not hold: no such text
    """
    text = REGISTRATION
    for old, new in edits:
        if old not in text:
            raise ValueError(f"the sample does not hold: {old}")
        text = text.replace(old, new)
    path = pathlib.Path(tempfile.mkdtemp(prefix="experiment-")).resolve()
    for name, content in {"registration.md": text, **FILES, **(files or {})}.items():
        if content is not None:
            (path / name).parent.mkdir(parents=True, exist_ok=True)
            (path / name).write_text(content, encoding="utf-8")
    return path


def greeting(prompt, folder):
    """The reply of the invented subject: a greeting only for the word please.

    >>> greeting("Write a line, please.", None), greeting("Write a line.", None)
    ('Hello and welcome.', 'Welcome.')
    """
    return "Hello and welcome." if "please" in prompt else "Welcome."


def agent(reply=greeting, init=None, code=0):
    r"""A function in the place of subprocess.run. It gives the stream of one session.

    `reply(prompt, folder)` gives the final text, or None for a session without a result.
    `init` changes keys of the first event.

    >>> done = agent()(["claude", "-p", "Say it, please."], cwd="/tmp")
    >>> done.returncode, [json.loads(line)["type"] for line in done.stdout.splitlines()]
    (0, ['system', 'result'])
    >>> json.loads(done.stdout.splitlines()[1])["result"]
    'Hello and welcome.'
    >>> done = agent(reply=lambda prompt, folder: None, init={"skills": ["own"]}, code=1)(["claude", "-p", "x"], cwd="/tmp")
    >>> done.returncode, [json.loads(line)["skills"] for line in done.stdout.splitlines()]
    (1, [['own']])
    """

    def run(command, **options):
        text = reply(command[2], pathlib.Path(options["cwd"]))
        events = [{**INIT, **(init or {})}]
        if text is not None:
            events.append({"type": "result", "is_error": False, "result": text})
        stream = "".join(json.dumps(event) + "\n" for event in events)
        return types.SimpleNamespace(returncode=code, stdout=stream, stderr="")

    return run


def judge(folder, answer=lambda arm, criterion: "yes"):
    r"""Write judgements.md: one row for each code of blind-key.json and each criterion of the judge.

    The judge of the sample knows the arm. A real judge does not.

    >>> path = folder_with_key = pathlib.Path(tempfile.mkdtemp(prefix="experiment-"))
    >>> _ = (path / "blind-key.json").write_text('{"P-1": {"arm": "plain", "run": 1}}')
    >>> judge(path, lambda arm, criterion: "no")
    >>> print((path / "judgements.md").read_text())
    | Code | Criterion | Answer | Evidence |
    |---|---|---|---|
    | P-1 | C-2 | no | final-1.md line 1 |
    | P-1 | C-3 | no | final-1.md line 1 |
    <BLANKLINE>
    """
    key = json.loads((folder / "blind-key.json").read_text(encoding="utf-8"))
    lines = ["| Code | Criterion | Answer | Evidence |", "|---|---|---|---|"]
    for code in sorted(key):
        for criterion in ("C-2", "C-3"):
            lines.append(
                f"| {code} | {criterion} | {answer(key[code]['arm'], criterion)} | final-1.md line 1 |"
            )
    (folder / "judgements.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def selftest():
    """Run the examples (doctests) of this module. Returns the result code."""
    result = doctest.testmod(optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)
    print(f"{result.attempted} examples, {result.failed} failed")
    return 1 if result.failed or not result.attempted else 0


if __name__ == "__main__":
    sys.exit(selftest())
