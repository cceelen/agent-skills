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


def main():
    args = sys.argv[1:]
    if not args or args[0] not in ("detect", "apply", "show"):
        sys.exit(__doc__)
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
        folder = lib.HOSTS[host]["agents"]["project"]
        folder.mkdir(parents=True, exist_ok=True)
        for name, text in files.items():
            (folder / name).write_text(text, encoding="utf-8")
        result["written"] = sorted(str(folder / name) for name in files)
    print(json.dumps(result, indent=1, sort_keys=True))
    sys.exit(0 if files else 1)


if __name__ == "__main__":
    main()
