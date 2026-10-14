#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Guard for the reader of converted files: a hook that the agent product runs before a read.

  guard.py < EVENT     decide on one call of a tool. EVENT is the JSON text of the hook.
  guard.py --selftest  run the examples of this program

The program models.py installs this program as a hook for the read tool. The agent product
gives the event on the standard input: the type of the agent that makes the call (`agent_type`),
the tool (`tool_name`) and the file (`tool_input.file_path`).

A call of a different agent, or of the session, passes: the guard limits one agent only. A call
of the agent `sota-file-reader` passes only if it reads a file whose folder holds the marker
`.reader-may-read`, and the file is not in a git repository. The converter pdf.py writes the
marker. Links are resolved first, thus a link in the work folder cannot lead out of it.

Result code 0: the call passes. Result code 2: the call is refused; the reason is on the
standard error output. The agent product runs this program with the Python of the computer, thus
the program uses only what Python 3.9 has, and it loads no other program of the tooling.
"""

import json
import os
import pathlib
import sys

AGENT = "sota-file-reader"
MARKER = ".reader-may-read"
TOOL = "Read"

MESSAGES = {
    "bad-input": "Refused: the guard cannot read the data of this call.",
    "not-read": "Refused: this agent has the read tool only.",
    "no-path": "Refused: the call names no file with an absolute path.",
    "no-marker": "Refused: this agent reads only a converted file of the work folder.",
    "in-repository": "Refused: this agent does not read a file of a git repository.",
}


def refusal(path):
    """The reason why the reader of converted files must not read a file, or None.

    A file passes if its folder holds the marker and no folder above it is a git repository.

    >>> import tempfile
    >>> work = pathlib.Path(tempfile.mkdtemp(prefix="sota-guard-")).resolve()
    >>> for name in ("work", "plain", "repo/.git", "repo/work"):
    ...     (work / name).mkdir(parents=True)
    >>> for name in ("work/a.md", "plain/a.md", "repo/work/a.md", "work/" + MARKER, "repo/work/" + MARKER):
    ...     _ = (work / name).write_text("")
    >>> refusal(str(work / "work/a.md")) is None
    True
    >>> refusal(str(work / "plain/a.md"))
    'Refused: this agent reads only a converted file of the work folder.'
    >>> refusal(str(work / "repo/work/a.md"))
    'Refused: this agent does not read a file of a git repository.'

    A link is resolved before the decision, and a path must be absolute.

    >>> (work / "work/link.md").symlink_to(work / "plain/a.md")
    >>> refusal(str(work / "work/link.md"))
    'Refused: this agent reads only a converted file of the work folder.'
    >>> refusal(str(work / "work/../plain/a.md")) == refusal(str(work / "plain/a.md"))
    True
    >>> refusal("work/a.md") == refusal("") == refusal(None) == MESSAGES["no-path"]
    True
    """
    if not isinstance(path, str) or not os.path.isabs(path):
        return MESSAGES["no-path"]
    resolved = pathlib.Path(os.path.realpath(path))
    if not (resolved.parent / MARKER).is_file():
        return MESSAGES["no-marker"]
    if any((folder / ".git").exists() for folder in resolved.parents):
        return MESSAGES["in-repository"]
    return None


def decide(text):
    """The reason why a call is refused, or None if it passes. The text is the event of the hook.

    A call that is not from the reader of converted files passes, whatever it does.

    >>> def event(**values):
    ...     return json.dumps(values)
    >>> decide(event(tool_name="Read", tool_input={"file_path": "/etc/hosts"})) is None
    True
    >>> decide(event(agent_type="sota-source-reader", tool_name="Bash")) is None
    True
    >>> decide("no JSON") is None and decide("[1]") is None and decide("") is None
    True

    The reader of converted files reads only a file that passes `refusal`.

    >>> import tempfile
    >>> work = pathlib.Path(tempfile.mkdtemp(prefix="sota-guard-")).resolve()
    >>> _ = (work / MARKER).write_text(""), (work / "a.md").write_text("")
    >>> def read(**values):
    ...     return decide(event(agent_type=AGENT, tool_name="Read", **values))
    >>> read(tool_input={"file_path": str(work / "a.md")}) is None
    True
    >>> read(tool_input={"file_path": "/etc/hosts"})
    'Refused: this agent reads only a converted file of the work folder.'
    >>> decide(event(agent_type=AGENT, tool_name="Bash", tool_input={"command": "ls"}))
    'Refused: this agent has the read tool only.'
    >>> read(tool_input="a.md")
    'Refused: the call names no file with an absolute path.'
    >>> read()
    'Refused: the call names no file with an absolute path.'

    Data that cannot be read is refused if it names the reader of converted files.

    >>> decide('{"agent_type": "sota-file-reader", "tool_name": ')
    'Refused: the guard cannot read the data of this call.'
    >>> decide('["sota-file-reader"]')
    'Refused: the guard cannot read the data of this call.'
    """
    try:
        event = json.loads(text)
    except ValueError:
        event = None
    if not isinstance(event, dict):
        return MESSAGES["bad-input"] if AGENT in text else None
    if event.get("agent_type") != AGENT:
        return None
    if event.get("tool_name") != TOOL:
        return MESSAGES["not-read"]
    tool_input = event.get("tool_input")
    return refusal(tool_input.get("file_path") if isinstance(tool_input, dict) else None)


def main(argv=None, stdin=None):
    """Decide on the event of the standard input. Returns the result code.

    >>> import contextlib, io
    >>> def run(text):
    ...     err = io.StringIO()
    ...     with contextlib.redirect_stderr(err):
    ...         code = main([], stdin=io.StringIO(text))
    ...     return code, err.getvalue().strip()
    >>> run('{"tool_name": "Read", "tool_input": {"file_path": "/etc/hosts"}}')
    (0, '')
    >>> run('{"agent_type": "sota-file-reader", "tool_name": "Read", "tool_input": {"file_path": "/a"}}')
    (2, 'Refused: this agent reads only a converted file of the work folder.')

    An argument gives the usage text and the result code 2.

    >>> run_help = io.StringIO()
    >>> with contextlib.redirect_stderr(run_help):
    ...     main(["--help"])
    2
    >>> run_help.getvalue().splitlines()[0]
    'Guard for the reader of converted files: a hook that the agent product runs before a read.'
    """
    args = list(sys.argv[1:] if argv is None else argv)
    if args:
        print(__doc__, file=sys.stderr)
        return 2
    reason = decide((stdin or sys.stdin).read())
    if reason:
        print(reason, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    if sys.argv[1:2] == ["--selftest"]:
        import aspect

        sys.exit(aspect.selftest())
    sys.exit(main())
