#!/usr/bin/env python3
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Agent files for the three isolated readers of the research tooling. Standard library only.

  models.py detect [--host H]   print the agent product and the proposed model of each role
  models.py apply [--host H] [--source-reader M] [--second-reader M] [--file-reader M] [--root DIR]
                                write the agent files into the project of this repository, or
                                of the folder DIR, and install the hook for the file reader
  models.py show [--host H]     print the agent files and the hook, and write nothing

Roles: "source-reader" reads one source, so it gets the smallest capable model and the tools web
search and web fetch. "second-reader" compares summaries with sources, so it gets a mid-size
model and web fetch only. "file-reader" reads one converted file of the work folder, so it gets
the smallest capable model and the read tool only. No role gets a shell, a tool that writes or a
search in files, and the two web readers get no file tool.

A list of tools cannot limit the read tool to one folder. Thus `apply` installs the program
guard.py as a hook of the agent product: it merges one entry into the settings file of the
project and keeps each other key of that file. The entry runs `python3` with the absolute path
of guard.py: the hook runs before each read, thus it must start fast and must not need the
network. If the agent product has no such hook, this program does not write the agent file of
the file reader and says so: a PDF source then cannot be read.

The names of the tools and the detection of the agent product come from the program models.py
of the skill library-vetting. If the agent product has no agent files, this program writes
nothing and says so: the tools of an agent then cannot be limited.
"""

import doctest
import importlib.util
import json
import pathlib
import re
import shlex
import sys

import guard

TOOLING = pathlib.Path(__file__).resolve().parent.parent
SHARED = TOOLING.parents[1] / "skills/library-vetting/scripts/models.py"
GUARD = TOOLING / "scripts/guard.py"
ROLES = ("source-reader", "second-reader", "file-reader")
TOOLS = {"source-reader": ("search", "fetch"), "second-reader": ("fetch",), "file-reader": ("read",)}
# The tools that a role must not get. Only the file reader gets the read tool, and the hook
# limits it to the converted files.
NEVER = ("shell", "write", "grep", "glob")
FORBIDDEN = {
    "source-reader": (*NEVER, "read"),
    "second-reader": (*NEVER, "read"),
    "file-reader": (*NEVER, "fetch", "search"),
}
# The proposed model of each role, by agent product. "inherit" selects no model.
DEFAULTS = {"claude": {"source-reader": "haiku", "second-reader": "sonnet", "file-reader": "haiku"}}
# The hook that runs before a call of a tool, by agent product: the settings file of the
# project and the name of the event. An agent product that is not here has no such hook.
HOOKS = {"claude": {"settings": ".claude/settings.json", "event": "PreToolUse"}}
# The role whose agent file is written only together with the hook: the agent that the guard
# limits.
GUARDED = guard.AGENT.removeprefix("sota-")

MESSAGES = {
    "no-files": "This agent product has no agent files. The tools of a reader cannot be limited.",
    "no-hook": "This agent product has no hook that limits the read tool. "
    "A PDF source cannot be read in this agent product.",
    "bad-model": "This is not a model name: {0}",
    "no-shared": "The program models.py of the skill library-vetting is absent.",
    "bad-settings": "The settings file cannot be changed, because it is not a JSON object with hooks: {0}",
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

    The reader of sources and the reader of files get the smallest capable model, the second
    reader a mid-size model.

    >>> mapping = mapping_for("claude", [])
    >>> sorted(mapping), mapping["source-reader"] != mapping["second-reader"]
    (['file-reader', 'second-reader', 'source-reader'], True)
    >>> mapping["file-reader"] == mapping["source-reader"]
    True
    >>> mapping_for("claude", ["--second-reader", "inherit"])["second-reader"]
    'inherit'
    >>> mapping_for("other", [])
    {'source-reader': 'inherit', 'second-reader': 'inherit', 'file-reader': 'inherit'}
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
    >>> models = {"source-reader": "small", "second-reader": "mid", "file-reader": "small"}
    >>> files = render("claude", models, lib.HOSTS)
    >>> sorted(files)
    ['sota-file-reader.md', 'sota-second-reader.md', 'sota-source-reader.md']
    >>> print("\n".join(line[:60] for line in files["sota-source-reader.md"].splitlines()[:6]))
    ---
    name: sota-source-reader
    description: Reads one source for the sota-research tooling
    tools: WebSearch, WebFetch
    model: small
    ---

    A web reader gets web tools only: no shell, no file tool and no search in files. The second
    reader gets the web fetch tool only. The file reader gets the read tool only. No file has a
    tool that its role must not get.

    >>> def tools(text):
    ...     return next(line for line in text.splitlines() if line.startswith("tools: "))[7:].split(", ")
    >>> tools(files["sota-second-reader.md"]), tools(files["sota-file-reader.md"])
    (['WebFetch'], ['Read'])
    >>> def forbidden(role):
    ...     return {lib.HOSTS["claude"]["tools"][t] for t in FORBIDDEN[role]}
    >>> texts = {role: files[f"sota-{role}.md"] for role in ROLES}
    >>> [r for r in ROLES if forbidden(r) & set(tools(texts[r])) or "{{" in texts[r]]
    []
    >>> ["read" in FORBIDDEN[role] for role in ROLES]
    [True, True, False]

    The agent file of the file reader has the name that the guard limits.

    >>> files[f"{guard.AGENT}.md"].splitlines()[1] == f"name: {guard.AGENT}" == f"name: sota-{GUARDED}"
    True

    An agent product with agent files and without a hook gets no file reader: nothing can limit
    its read tool to the work folder.

    >>> sorted(render("plain", models, {"plain": lib.HOSTS["claude"]}))
    ['sota-second-reader.md', 'sota-source-reader.md']

    An agent product without agent files, or one that is not known, gets no file.

    >>> render("codex", mapping_for("codex", []), lib.HOSTS), render("other", {}, lib.HOSTS)
    ({}, {})
    """
    entry = hosts.get(host)
    if not entry or not entry["agents"]:
        return {}
    roles = [role for role in ROLES if role != GUARDED or host in HOOKS]
    values = {}
    for role in roles:
        key = role.upper().replace("-", "_")
        values[f"{{{{{key}_TOOLS}}}}"] = ", ".join(entry["tools"][t] for t in TOOLS[role])
        values[f"{{{{{key}_MODEL}}}}"] = f"model: {mapping[role]}\n"
    out = {}
    for role in sorted(roles):
        text = (TOOLING / "agent-templates" / f"sota-{role}.md").read_text(encoding="utf-8")
        for placeholder, value in values.items():
            text = text.replace(placeholder, value)
        out[f"sota-{role}.md"] = text
    return out


def hook_entry(host, hosts):
    """The entry of the settings file that runs the guard before each call of the read tool.

    The command uses `python3` and the absolute path of the guard. It needs no network and no
    environment of a project, and it does not depend on the current folder of the agent product.

    >>> entry = hook_entry("claude", shared().HOSTS)
    >>> entry["matcher"], [sorted(h) for h in entry["hooks"]], entry["hooks"][0]["type"]
    ('Read', [['command', 'type']], 'command')
    >>> command = shlex.split(entry["hooks"][0]["command"])
    >>> command[0], pathlib.Path(command[1]).is_absolute(), pathlib.Path(command[1]) == GUARD
    ('python3', True, True)
    """
    command = f"python3 {shlex.quote(str(GUARD))}"
    return {"matcher": hosts[host]["tools"]["read"], "hooks": [{"type": "command", "command": command}]}


def is_guard(entry):
    """True if an entry of the settings file runs the guard of this tooling, from any folder.

    >>> is_guard(hook_entry("claude", shared().HOSTS))
    True
    >>> is_guard({"hooks": [{"command": "python3 /old/factory/sota-research/scripts/guard.py"}]})
    True
    >>> is_guard({"hooks": [{"command": "python3 /other/guard.py"}]}), is_guard("text"), is_guard({})
    (False, False, False)
    """
    hooks = entry.get("hooks") if isinstance(entry, dict) else None
    commands = [h.get("command") for h in hooks if isinstance(h, dict)] if isinstance(hooks, list) else []
    return any(isinstance(c, str) and "sota-research/scripts/guard.py" in c for c in commands)


def install_hook(root, host, hosts):
    r"""Merge the entry for the guard into the settings file of the project. Returns the file.

    The function keeps each other key and each other hook of the file.

    >>> import tempfile
    >>> root = pathlib.Path(tempfile.mkdtemp(prefix="sota-hook-"))
    >>> lib = shared()
    >>> path = install_hook(root, "claude", lib.HOSTS)
    >>> path.relative_to(root).as_posix(), json.loads(path.read_text()) == {
    ...     "hooks": {"PreToolUse": [hook_entry("claude", lib.HOSTS)]}}
    ('.claude/settings.json', True)
    >>> other = {"matcher": "Bash", "hooks": [{"type": "command", "command": "true"}]}
    >>> moved = {"matcher": "Read", "hooks": [{"command": "python3 /old/sota-research/scripts/guard.py"}]}
    >>> _ = path.write_text(json.dumps({"model": "x", "hooks": {"Stop": [1], "PreToolUse": [other, moved]}}))
    >>> data = json.loads(install_hook(root, "claude", lib.HOSTS).read_text())
    >>> data["model"], data["hooks"]["Stop"]
    ('x', [1])
    >>> data["hooks"]["PreToolUse"] == [other, hook_entry("claude", lib.HOSTS)]
    True

    A second run changes nothing.

    >>> text = path.read_text()
    >>> install_hook(root, "claude", lib.HOSTS).read_text() == text, text.endswith("}\n")
    (True, True)

    The function does not replace a settings file that it cannot read.

    >>> for text in ("{ no JSON", "[]", '{"hooks": []}', '{"hooks": {"PreToolUse": {}}}'):
    ...     _ = path.write_text(text)
    ...     try:
    ...         install_hook(root, "claude", lib.HOSTS)
    ...     except SystemExit as stop:
    ...         print(str(stop.code)[:66], path.read_text() == text)
    The settings file cannot be changed, because it is not a JSON obje True
    The settings file cannot be changed, because it is not a JSON obje True
    The settings file cannot be changed, because it is not a JSON obje True
    The settings file cannot be changed, because it is not a JSON obje True
    """
    path = pathlib.Path(root) / HOOKS[host]["settings"]
    try:
        data = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
    except ValueError:
        data = None
    hooks = data.setdefault("hooks", {}) if isinstance(data, dict) else None
    entries = hooks.setdefault(HOOKS[host]["event"], []) if isinstance(hooks, dict) else None
    if not isinstance(entries, list):
        sys.exit(MESSAGES["bad-settings"].format(path))
    entries[:] = [entry for entry in entries if not is_guard(entry)] + [hook_entry(host, hosts)]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return path


def selftest():
    """Run the examples (doctests) of this program. Returns the result code."""
    result = doctest.testmod(optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)
    print(f"{result.attempted} examples, {result.failed} failed")
    return 1 if result.failed or not result.attempted else 0


def main(argv=None, hosts=None):
    """The command line. See the text at the start of this file.

    >>> import contextlib, io, tempfile
    >>> def run(*args, hosts=None):
    ...     out = io.StringIO()
    ...     with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
    ...         try:
    ...             main(list(args), hosts=hosts)
    ...         except SystemExit as stop:
    ...             code = stop.code
    ...     return code, json.loads(out.getvalue()) if out.getvalue().startswith("{") else None

    The command show prints the agent files and the hook, and writes nothing.

    >>> code, result = run("show", "--host", "claude")
    >>> code, result["writes_agent_files"], result["reads_converted_files"], "written" in result
    (0, True, True, False)
    >>> sorted(result["files"])
    ['sota-file-reader.md', 'sota-second-reader.md', 'sota-source-reader.md']
    >>> result["hook"] == {"file": ".claude/settings.json", "event": "PreToolUse",
    ...                    "entry": hook_entry("claude", shared().HOSTS)}
    True

    The command apply writes the files into the project folder of the agent product, and the
    hook into the settings file of the project.

    >>> root = pathlib.Path(tempfile.mkdtemp(prefix="sota-agents-"))
    >>> code, result = run("apply", "--host", "claude", "--root", root)
    >>> code, [pathlib.Path(p).relative_to(root).as_posix() for p in result["written"]]
    (0, ['.claude/agents/sota-file-reader.md', '.claude/agents/sota-second-reader.md',
         '.claude/agents/sota-source-reader.md', '.claude/settings.json'])
    >>> (root / ".claude/agents/sota-source-reader.md").read_text(encoding="utf-8").splitlines()[3]
    'tools: WebSearch, WebFetch'
    >>> (root / ".claude/agents/sota-file-reader.md").read_text(encoding="utf-8").splitlines()[3]
    'tools: Read'
    >>> settings = json.loads((root / ".claude/settings.json").read_text())
    >>> settings["hooks"]["PreToolUse"] == [result["hook"]["entry"]]
    True

    If the settings file cannot be changed, the program stops before it writes an agent file:
    the file reader does not exist without its hook.

    >>> root = pathlib.Path(tempfile.mkdtemp(prefix="sota-agents-"))
    >>> (root / ".claude").mkdir()
    >>> _ = (root / ".claude/settings.json").write_text("[]")
    >>> run("apply", "--host", "claude", "--root", root)[0][:32], (root / ".claude/agents").exists()
    ('The settings file cannot be chan', False)

    If the agent product has agent files and no hook, the program writes the two web readers
    only, and says that a PDF source cannot be read.

    >>> plain = {"plain": shared().HOSTS["claude"]}
    >>> root = pathlib.Path(tempfile.mkdtemp(prefix="sota-agents-"))
    >>> code, result = run("apply", "--host", "plain", "--root", root, hosts=plain)
    >>> code, result["reads_converted_files"], "hook" in result, result["note"]
    (0, False, False, 'This agent product has no hook that limits the read tool. A PDF source cannot be read
    in this agent product.')
    >>> sorted(p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file())
    ['.claude/agents/sota-second-reader.md', '.claude/agents/sota-source-reader.md']
    >>> run("show", "--host", "plain", hosts=plain)[1]["note"] == result["note"]
    True

    If the agent product has no agent files, the tools of a reader cannot be limited. The program
    says so, writes nothing and gives the result code 1. The procedure then stops.

    >>> code, result = run("apply", "--host", "codex", "--root", root)
    >>> code, result["writes_agent_files"], result["note"], "written" in result
    (1, False, 'This agent product has no agent files. The tools of a reader cannot be limited.', False)
    >>> result["reads_converted_files"]
    False
    >>> detected = run("detect", "--host", "claude")[1]
    >>> detected["mapping"] == mapping_for("claude", []), detected["reads_converted_files"]
    (True, True)
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
    hosts = lib.HOSTS if hosts is None else hosts
    host = option(args, "--host") or lib.detect_host()[0]
    mapping = mapping_for(host, args)
    files = render(host, mapping, hosts)
    guarded = f"sota-{GUARDED}.md" in files
    result = {
        "host": host,
        "mapping": mapping,
        "writes_agent_files": bool(files),
        "reads_converted_files": guarded,
    }
    if not files:
        result["note"] = MESSAGES["no-files"]
    elif not guarded:
        result["note"] = MESSAGES["no-hook"]
    if guarded:
        result["hook"] = {
            "file": HOOKS[host]["settings"],
            "event": HOOKS[host]["event"],
            "entry": hook_entry(host, hosts),
        }
    if args[0] == "show":
        result["files"] = files
    if args[0] == "apply" and files:
        # The agent files go into this repository, whatever the current folder is. The hook is
        # written first: the file reader must not exist without it.
        root = pathlib.Path(option(args, "--root") or TOOLING.parents[1])
        written = [install_hook(root, host, hosts)] if guarded else []
        folder = root / hosts[host]["agents"]["project"]
        folder.mkdir(parents=True, exist_ok=True)
        for name, text in files.items():
            (folder / name).write_text(text, encoding="utf-8")
        result["written"] = sorted(str(path) for path in [*written, *(folder / name for name in files)])
    print(json.dumps(result, indent=1, sort_keys=True))
    sys.exit(0 if files else 1)


if __name__ == "__main__":
    main()
