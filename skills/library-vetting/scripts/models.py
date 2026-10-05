#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Model mapping for the library-vetting agents. Stdlib only.

  models.py detect [--host H]     print the host, what its local configuration shows, and a
                                  proposed model for each role (JSON)
  models.py apply [--host H] [--evidence M] [--vetter M] [--scope user|project]
                                  save the mapping and write the two agent files for the host
  models.py show                  print the saved mapping (project scope wins over user scope)

Roles: "evidence" reads and extracts, so it gets the smallest capable model. "vetter" judges and
writes, so it gets the model of the session. A value of "inherit" means: do not select a model.
The script reads local files and environment variables only. It cannot tell if an account may
use a model; the skill finds that out at the first spawn and falls back to "inherit".
"""

import json
import os
import pathlib
import re
import sys

HOME = pathlib.Path.home()
SKILL = pathlib.Path(__file__).resolve().parent.parent
ROLES = ("evidence", "vetter")

# One entry per host. "tools" maps a generic tool to the name the host uses in an agent file.
HOSTS = {
    "claude": {
        "label": "Claude Code",
        "env": ("CLAUDECODE", "CLAUDE_CODE_ENTRYPOINT"),
        "home": HOME / ".claude",
        "agents": {"user": HOME / ".claude" / "agents", "project": pathlib.Path(".claude/agents")},
        "tools": {
            "shell": "Bash",
            "read": "Read",
            "write": "Write",
            "grep": "Grep",
            "glob": "Glob",
            "fetch": "WebFetch",
            "search": "WebSearch",
        },
        "default": {"evidence": "haiku", "vetter": "inherit"},
        "note": "The aliases haiku, sonnet and opus follow the provider settings of the session.",
    },
    "codex": {
        "label": "OpenAI Codex",
        "env": ("CODEX_HOME", "CODEX_SANDBOX"),
        "home": HOME / ".codex",
        "agents": None,  # no agent files are written for this host
        "tools": {},
        "default": {"evidence": "inherit", "vetter": "inherit"},
        "note": "This script does not write agent files for Codex. One model does all steps "
        "unless you give a model name that your Codex setup accepts.",
    },
}
UNKNOWN = {
    "label": "unknown host",
    "agents": None,
    "tools": {},
    "default": {"evidence": "inherit", "vetter": "inherit"},
    "note": "The host is not known. The session model does all steps.",
}
EVIDENCE_TOOLS = ("shell", "read", "write", "grep", "glob", "fetch", "search")
VETTER_TOOLS = ("shell", "read", "write", "grep", "glob")


def detect_host():
    for name, h in HOSTS.items():
        if any(os.environ.get(v) for v in h["env"]):
            return name, "environment"
    found = [name for name, h in HOSTS.items() if h["home"].is_dir()]
    if len(found) == 1:
        return found[0], "configuration folder"
    return ("unknown", f"cannot decide between {found}" if found else "no known configuration folder")


def settings(paths):
    """The settings files that can be read, each with its content."""
    for p in paths:
        try:
            yield p, json.loads(p.read_text())
        except (OSError, ValueError):
            continue


def note_session_model(out, p, data):
    if data.get("model"):
        out.setdefault("session_model", f"{data['model']} ({p})")


def configured_claude():
    out = {}
    for p, data in settings(
        (
            pathlib.Path(".claude/settings.local.json"),
            pathlib.Path(".claude/settings.json"),
            HOME / ".claude" / "settings.json",
        )
    ):
        note_session_model(out, p, data)
        for k, v in (data.get("env") or {}).items():
            if "MODEL" in k or k in ("CLAUDE_CODE_USE_BEDROCK", "CLAUDE_CODE_USE_VERTEX"):
                out.setdefault(k, f"{v} ({p})")
    for k in (
        "ANTHROPIC_MODEL",
        "ANTHROPIC_DEFAULT_HAIKU_MODEL",
        "ANTHROPIC_SMALL_FAST_MODEL",
        "CLAUDE_CODE_SUBAGENT_MODEL",
        "CLAUDE_CODE_USE_BEDROCK",
        "CLAUDE_CODE_USE_VERTEX",
    ):
        if os.environ.get(k):
            out[k] = f"{os.environ[k]} (environment)"
    return out


def configured_codex():
    p = pathlib.Path(os.environ.get("CODEX_HOME") or HOME / ".codex") / "config.toml"
    try:
        m = re.search(r'^\s*model\s*=\s*"([^"]+)"', p.read_text(), re.M)
    except OSError:
        return {}
    return {"session_model": f"{m.group(1)} ({p})"} if m else {}


CONFIGURED = {"claude": configured_claude, "codex": configured_codex}


def configured(host):
    """What the local configuration says about models. Facts only, no guesses."""
    return CONFIGURED[host]() if host in CONFIGURED else {}


def propose(host):
    h = HOSTS.get(host, UNKNOWN)
    conf = configured(host)
    notes = [h["note"]]
    if host == "claude" and "CLAUDE_CODE_SUBAGENT_MODEL" in conf:
        notes.append("CLAUDE_CODE_SUBAGENT_MODEL is set. It overrides the model of each subagent.")
    return {
        "host": host,
        "label": h["label"],
        "configured": conf,
        "proposal": dict(h["default"]),
        "writes_agent_files": bool(h["agents"]),
        "notes": notes,
    }


def mapping_path(scope):
    if scope == "project":
        return pathlib.Path(".claude/library-vetting/models.json")
    return (
        pathlib.Path(os.environ.get("XDG_CONFIG_HOME") or HOME / ".config")
        / "library-vetting"
        / "models.json"
    )


def tool_list(h, wanted):
    """The tools of an agent file, in the names of the host."""
    return ", ".join(h["tools"][t] for t in wanted)


def render(host, mapping):
    """Return {file name: text} of the agent files for the host, or {} if it has none."""
    h = HOSTS.get(host, UNKNOWN)
    if not h["agents"]:
        return {}
    values = {
        "{{EVIDENCE_TOOLS}}": tool_list(h, EVIDENCE_TOOLS),
        "{{VETTER_TOOLS}}": tool_list(h, VETTER_TOOLS),
        "{{EVIDENCE_MODEL}}": f"model: {mapping['evidence']}\n",  # "inherit" is a value too
        "{{VETTER_MODEL}}": f"model: {mapping['vetter']}\n",
    }
    out = {}
    for f in sorted((SKILL / "agent-templates").glob("*.md")):
        text = f.read_text()
        for placeholder, value in values.items():
            text = text.replace(placeholder, value)
        out[f.name] = text
    return out


def opt(args, flag, default=None):
    return args[args.index(flag) + 1] if flag in args else default


def host_of(args):
    return opt(args, "--host") or detect_host()[0]


def read_mapping(scope):
    p = mapping_path(scope)
    return json.loads(p.read_text()) if p.exists() else {}


def write_agent_files(host, scope, mapping):
    """Write the agent files of the host. Return the paths."""
    files = render(host, mapping)
    if not files:
        return []
    d = HOSTS[host]["agents"][scope]
    d.mkdir(parents=True, exist_ok=True)
    for name, text in files.items():
        (d / name).write_text(text)
    return [str(d / name) for name in files]


def cmd_detect(args):
    host, how = (opt(args, "--host"), "given") if opt(args, "--host") else detect_host()
    print(json.dumps({**propose(host), "detected_by": how}, indent=1))


def cmd_apply(args):
    host, scope = host_of(args), opt(args, "--scope", "user")
    if scope not in ("user", "project"):
        sys.exit(f"not a scope: {scope} (use user or project)")
    data = read_mapping(scope)
    # A role that the command does not give keeps its saved model.
    saved, default = data.get(host) or {}, HOSTS.get(host, UNKNOWN)["default"]
    mapping = {r: opt(args, f"--{r}") or saved.get(r) or default[r] for r in ROLES}
    bad = [v for v in mapping.values() if not re.fullmatch(r"[A-Za-z0-9._:/@-]+", v)]
    if bad:
        sys.exit(f"not a model name: {bad}")
    p = mapping_path(scope)
    p.parent.mkdir(parents=True, exist_ok=True)
    data[host] = mapping
    p.write_text(json.dumps(data, indent=1, sort_keys=True) + "\n")
    written = [str(p), *write_agent_files(host, scope, mapping)]
    print(json.dumps({"host": host, "scope": scope, "mapping": mapping, "written": written}, indent=1))


def cmd_show(args):
    host = host_of(args)
    for scope in ("project", "user"):
        data = read_mapping(scope)
        if host in data:
            print(json.dumps({"host": host, "scope": scope, "mapping": data[host]}))
            return
    print(json.dumps({"host": host, "scope": None, "mapping": None}))


COMMANDS = {"detect": cmd_detect, "apply": cmd_apply, "show": cmd_show}


def main():
    args = sys.argv[1:]
    if not args or args[0] not in COMMANDS:
        sys.exit(__doc__)
    COMMANDS[args[0]](args)


if __name__ == "__main__":
    main()
