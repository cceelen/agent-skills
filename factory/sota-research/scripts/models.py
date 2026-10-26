#!/usr/bin/env python3
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Agent files for the two isolated readers of the research tooling. Standard library only.

  models.py detect [--host H]   print the agent product and the proposed model of each role
  models.py apply [--host H] [--source-reader M] [--second-reader M] [--root DIR]
                                write the two agent files into the project of this repository,
                                or of the folder DIR
  models.py show [--host H]     print the agent files, and write nothing

Roles: "source-reader" reads one source, so it gets the smallest capable model and the tools web
search and web fetch. "second-reader" compares summaries with sources, so it gets a mid-size
model and web fetch only. No role gets a shell, a file tool or a search in files.

The names of the tools and the detection of the agent product come from the program models.py
of the skill library-vetting. If the agent product has no agent files, this program writes
nothing and says so: the tools of an agent then cannot be limited.
"""

import doctest
import importlib.util
import json
import pathlib
import re
import sys

TOOLING = pathlib.Path(__file__).resolve().parent.parent
SHARED = TOOLING.parents[1] / "skills/library-vetting/scripts/models.py"
ROLES = ("source-reader", "second-reader")
TOOLS = {"source-reader": ("search", "fetch"), "second-reader": ("fetch",)}
FORBIDDEN = ("shell", "read", "write", "grep", "glob")
# The proposed model of each role, by agent product. "inherit" selects no model.
DEFAULTS = {"claude": {"source-reader": "haiku", "second-reader": "sonnet"}}

MESSAGES = {
    "no-files": "This agent product has no agent files. The tools of a reader cannot be limited.",
    "bad-model": "This is not a model name: {0}",
    "no-shared": "The program models.py of the skill library-vetting is absent.",
}


def shared():
    """The module models.py of library-vetting: the host table and the detection.

    >>> lib = shared()
    >>> sorted(lib.HOSTS), sorted(lib.HOSTS["claude"]["tools"])
    (['claude', 'codex'], ['fetch', 'glob', 'grep', 'read', 'search', 'shell', 'write'])

    Without that program this one stops and says why.

    >>> module = sys.modules[shared.__module__]
    >>> saved = module.SHARED
    >>> module.SHARED = pathlib.Path("absent.py")
    >>> shared()
    Traceback (most recent call last):
        ...
    SystemExit: The program models.py of the skill library-vetting is absent.
    >>> module.SHARED = saved
    """
    if not SHARED.is_file():
        sys.exit(MESSAGES["no-shared"])
    spec = importlib.util.spec_from_file_location("library_vetting_models", SHARED)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def option(args, flag, default=None):
    """The value after an option in the arguments, or the default.

    >>> option(["show", "--host", "claude"], "--host"), option(["show"], "--host", "x")
    ('claude', 'x')
    >>> option(["--host"], "--host") is None
    True
    """
    return args[args.index(flag) + 1] if flag in args and args.index(flag) + 1 < len(args) else default


def mapping_for(host, args):
    """The model of each role: the given one, or the proposal for the agent product, or "inherit".

    The two roles get different models: the reader of sources the smallest capable model, the
    second reader a mid-size model.

    >>> mapping = mapping_for("claude", [])
    >>> sorted(mapping), mapping["source-reader"] != mapping["second-reader"]
    (['second-reader', 'source-reader'], True)
    >>> mapping_for("claude", ["--second-reader", "inherit"])["second-reader"]
    'inherit'
    >>> mapping_for("other", [])
    {'source-reader': 'inherit', 'second-reader': 'inherit'}
    >>> mapping_for("claude", ["--source-reader", "a model; rm"])
    Traceback (most recent call last):
        ...
    SystemExit: This is not a model name: a model; rm
    """
    proposal = DEFAULTS.get(host, {})
    mapping = {role: option(args, f"--{role}") or proposal.get(role, "inherit") for role in ROLES}
    bad = [m for m in mapping.values() if not re.fullmatch(r"[A-Za-z0-9._:/@-]+", m)]
    if bad:
        sys.exit(MESSAGES["bad-model"].format(", ".join(bad)))
    return mapping


def render(host, mapping, hosts):
    r"""{file name: text} of the agent files for the agent product, or {} if it has none.

    >>> lib = shared()
    >>> files = render("claude", {"source-reader": "small", "second-reader": "mid"}, lib.HOSTS)
    >>> sorted(files)
    ['sota-second-reader.md', 'sota-source-reader.md']
    >>> print("\n".join(line[:60] for line in files["sota-source-reader.md"].splitlines()[:6]))
    ---
    name: sota-source-reader
    description: Reads one source for the sota-research tooling
    tools: WebSearch, WebFetch
    model: small
    ---

    A reader gets web tools only: no shell, no file tool and no search in files. The second
    reader gets the web fetch tool only.

    >>> def tools(text):
    ...     return next(line for line in text.splitlines() if line.startswith("tools: "))[7:].split(", ")
    >>> tools(files["sota-second-reader.md"])
    ['WebFetch']
    >>> forbidden = {lib.HOSTS["claude"]["tools"][t] for t in FORBIDDEN}
    >>> [name for name, text in files.items() if forbidden & set(tools(text)) or "{{" in text]
    []

    An agent product without agent files, or one that is not known, gets no file.

    >>> render("codex", mapping_for("codex", []), lib.HOSTS), render("other", {}, lib.HOSTS)
    ({}, {})
    """
    entry = hosts.get(host)
    if not entry or not entry["agents"]:
        return {}
    values = {}
    for role in ROLES:
        key = role.upper().replace("-", "_")
        values[f"{{{{{key}_TOOLS}}}}"] = ", ".join(entry["tools"][t] for t in TOOLS[role])
        values[f"{{{{{key}_MODEL}}}}"] = f"model: {mapping[role]}\n"
    out = {}
    for template in sorted((TOOLING / "agent-templates").glob("sota-*.md")):
        text = template.read_text(encoding="utf-8")
        for placeholder, value in values.items():
            text = text.replace(placeholder, value)
        out[template.name] = text
    return out


def selftest():
    """Run the examples (doctests) of this program. Returns the result code."""
    result = doctest.testmod(optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)
    print(f"{result.attempted} examples, {result.failed} failed")
    return 1 if result.failed or not result.attempted else 0


def main(argv=None):
    """The command line. See the text at the start of this file.

    >>> import contextlib, io, tempfile
    >>> def run(*args):
    ...     out = io.StringIO()
    ...     with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
    ...         try:
    ...             main(list(args))
    ...         except SystemExit as stop:
    ...             code = stop.code
    ...     return code, json.loads(out.getvalue()) if out.getvalue().startswith("{") else None

    The command show prints the agent files and writes nothing.

    >>> code, result = run("show", "--host", "claude")
    >>> code, result["writes_agent_files"], "written" in result, sorted(result["files"])
    (0, True, False, ['sota-second-reader.md', 'sota-source-reader.md'])

    The command apply writes the files into the project folder of the agent product.

    >>> root = pathlib.Path(tempfile.mkdtemp(prefix="sota-agents-"))
    >>> code, result = run("apply", "--host", "claude", "--root", root)
    >>> code, [pathlib.Path(p).relative_to(root).as_posix() for p in result["written"]]
    (0, ['.claude/agents/sota-second-reader.md', '.claude/agents/sota-source-reader.md'])
    >>> (root / ".claude/agents/sota-source-reader.md").read_text(encoding="utf-8").splitlines()[3]
    'tools: WebSearch, WebFetch'

    If the agent product has no agent files, the tools of a reader cannot be limited. The program
    says so, writes nothing and gives the result code 1. The procedure then stops.

    >>> code, result = run("apply", "--host", "codex", "--root", root)
    >>> code, result["writes_agent_files"], result["note"], "written" in result
    (1, False, 'This agent product has no agent files. The tools of a reader cannot be limited.', False)
    >>> run("detect", "--host", "claude")[1]["mapping"] == mapping_for("claude", [])
    True
    >>> run()
    (2, None)

    No model name is in the text for agents: the names are only in this file.

    >>> names = {model for roles in DEFAULTS.values() for model in roles.values()} - {"inherit"}
    >>> texts = [TOOLING / "SKILL.md", *TOOLING.glob("references/*.md"), *TOOLING.glob("prompts/*.md")]
    >>> texts += TOOLING.glob("agent-templates/*.md")
    >>> len(names) > 0, len(texts) > 5
    (True, True)
    >>> [f"{t.name}: {n}" for t in texts for n in sorted(names) if n in t.read_text(encoding="utf-8")]
    []
    """
    args = list(sys.argv[1:] if argv is None else argv)
    if args[:1] == ["--selftest"]:
        sys.exit(selftest())
    if not args or args[0] not in ("detect", "apply", "show"):
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    lib = shared()
    host = option(args, "--host") or lib.detect_host()[0]
    mapping = mapping_for(host, args)
    files = render(host, mapping, lib.HOSTS)
    result = {"host": host, "mapping": mapping, "writes_agent_files": bool(files)}
    if not files:
        result["note"] = MESSAGES["no-files"]
    if args[0] == "show":
        result["files"] = files
    if args[0] == "apply" and files:
        # The agent files go into this repository, whatever the current folder is.
        root = pathlib.Path(option(args, "--root") or TOOLING.parents[1])
        folder = root / lib.HOSTS[host]["agents"]["project"]
        folder.mkdir(parents=True, exist_ok=True)
        for name, text in files.items():
            (folder / name).write_text(text, encoding="utf-8")
        result["written"] = sorted(str(folder / name) for name in files)
    print(json.dumps(result, indent=1, sort_keys=True))
    sys.exit(0 if files else 1)


if __name__ == "__main__":
    main()
