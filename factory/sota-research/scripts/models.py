#!/usr/bin/env python3
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Agent files for the two isolated readers of the research tooling. Standard library only.

  models.py detect [--host H]   print the agent product and the proposed model of each role
  models.py apply [--host H] [--source-reader M] [--second-reader M]
                                write the two agent files into the project of this repository
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
    """The module models.py of library-vetting: the host table and the detection."""
    if not SHARED.is_file():
        sys.exit(MESSAGES["no-shared"])
    spec = importlib.util.spec_from_file_location("library_vetting_models", SHARED)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def option(args, flag, default=None):
    return args[args.index(flag) + 1] if flag in args and args.index(flag) + 1 < len(args) else default


def mapping_for(host, args):
    proposal = DEFAULTS.get(host, {})
    mapping = {role: option(args, f"--{role}") or proposal.get(role, "inherit") for role in ROLES}
    bad = [m for m in mapping.values() if not re.fullmatch(r"[A-Za-z0-9._:/@-]+", m)]
    if bad:
        sys.exit(MESSAGES["bad-model"].format(", ".join(bad)))
    return mapping


def render(host, mapping, hosts):
    """{file name: text} of the agent files for the agent product, or {} if it has none."""
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
        folder = TOOLING.parents[1] / lib.HOSTS[host]["agents"]["project"]
        folder.mkdir(parents=True, exist_ok=True)
        for name, text in files.items():
            (folder / name).write_text(text, encoding="utf-8")
        result["written"] = sorted(str(folder / name) for name in files)
    print(json.dumps(result, indent=1, sort_keys=True))
    sys.exit(0 if files else 1)


__test__ = {
    "the readers get web tools only": r"""
    >>> lib = shared()
    >>> def front_matter(text):
    ...     return dict(line.split(": ", 1) for line in text.split("---\n")[1].splitlines())
    >>> checked = 0
    >>> for host, entry in sorted(lib.HOSTS.items()):
    ...     files = render(host, mapping_for(host, []), lib.HOSTS)
    ...     if not entry["agents"]:
    ...         assert files == {}, host
    ...         continue
    ...     assert sorted(files) == ["sota-second-reader.md", "sota-source-reader.md"], host
    ...     forbidden = {entry["tools"][t] for t in FORBIDDEN}
    ...     tools = {name: set(front_matter(text)["tools"].split(", ")) for name, text in files.items()}
    ...     assert not any(t & forbidden for t in tools.values()), host
    ...     assert tools["sota-source-reader.md"] == {entry["tools"]["search"], entry["tools"]["fetch"]}, host
    ...     assert tools["sota-second-reader.md"] == {entry["tools"]["fetch"]}, host
    ...     assert not any("{{" in text for text in files.values()), host
    ...     checked += 1
    >>> checked >= 1
    True

    The two roles get different models. A given model wins. An unknown product selects no model.

    >>> mapping = mapping_for("claude", [])
    >>> mapping["source-reader"] != mapping["second-reader"]
    True
    >>> mapping_for("claude", ["--second-reader", "inherit"])["second-reader"]
    'inherit'
    >>> mapping_for("other", [])
    {'source-reader': 'inherit', 'second-reader': 'inherit'}

    No model name is in the text for agents: the names are only in this file.

    >>> names = {model for roles in DEFAULTS.values() for model in roles.values()} - {"inherit"}
    >>> texts = [TOOLING / "SKILL.md", *TOOLING.glob("references/*.md"), *TOOLING.glob("prompts/*.md")]
    >>> texts += TOOLING.glob("agent-templates/*.md")
    >>> len(names) > 0, len(texts) > 5
    (True, True)
    >>> [f"{t.name}: {n}" for t in texts for n in sorted(names) if n in t.read_text(encoding="utf-8")]
    []
    """,
    "the commands": r"""
    >>> import contextlib, io
    >>> def run(*args):
    ...     out = io.StringIO()
    ...     with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
    ...         try:
    ...             main(list(args))
    ...         except SystemExit as stop:
    ...             code = stop.code
    ...     return code, json.loads(out.getvalue()) if out.getvalue().startswith("{") else None

    The command show writes nothing.

    >>> code, result = run("show", "--host", "claude")
    >>> code, result["writes_agent_files"], "written" in result, sorted(result["files"])
    (0, True, False, ['sota-second-reader.md', 'sota-source-reader.md'])
    >>> code, result = run("detect", "--host", "codex")
    >>> code, result["writes_agent_files"], result["note"]
    (1, False, 'This agent product has no agent files. The tools of a reader cannot be limited.')
    >>> run("apply", "--host", "codex")[0], run()[0]
    (1, 2)
    >>> long = [s for text in MESSAGES.values() for s in text.split(". ") if len(s.split()) > 25]
    >>> long
    []
    """,
}


if __name__ == "__main__":
    main()
