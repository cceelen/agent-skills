#!/bin/sh
# Install skills from this repository.
#   ./install.sh                         all skills, for Claude Code (~/.claude/skills)
#   ./install.sh --agent codex           all skills, for OpenAI Codex (~/.agents/skills)
#   ./install.sh --dir PATH [SKILL ...]  the named skills (default: all) into PATH
#   ./install.sh --rules FILE            also put the rules of the kit into this instruction file
#   ./install.sh --no-rules              do not change an instruction file
# With --agent, or with no option, the rules go into the instruction file of the user for that
# agent. To remove them: python3 rules/apply.py --remove FILE
set -e
here=$(cd "$(dirname "$0")" && pwd)
dest="$HOME/.claude/skills"
rules_set=""
dir_set=""
rules=""
agent_rules="$HOME/.claude/CLAUDE.md"
while [ $# -gt 0 ]; do
  case "$1" in
    --agent)
      case "$2" in
        claude) dest="$HOME/.claude/skills"; agent_rules="$HOME/.claude/CLAUDE.md" ;;
        codex) dest="$HOME/.agents/skills"; agent_rules="$HOME/.codex/AGENTS.md" ;;
        *) echo "unknown agent: $2 (use claude or codex, or --dir PATH)" >&2; exit 2 ;;
      esac
      shift 2 ;;
    --dir) dest="$2"; dir_set=1; shift 2 ;;
    --rules) rules="$2"; rules_set=1; shift 2 ;;
    --no-rules) rules=""; rules_set=1; shift ;;
    -h|--help) sed -n '2,9p' "$0"; exit 0 ;;
    *) break ;;
  esac
done
# The instruction file: the one that was named, or the one of the agent. None for --dir.
if [ -z "$rules_set" ] && [ -z "$dir_set" ]; then rules="$agent_rules"; fi
if [ $# -eq 0 ]; then
  for d in "$here"/skills/*/; do
    d=${d%/}
    set -- "$@" "${d##*/}"
  done
fi
mkdir -p "$dest"
for name in "$@"; do
  [ -f "$here/skills/$name/SKILL.md" ] || { echo "no such skill: $name" >&2; exit 2; }
  rm -rf "${dest:?}/$name"
  cp -R "$here/skills/$name" "$dest/$name"
  echo "installed: $dest/$name"
done
if [ -n "$rules" ]; then
  python3 "$here/rules/apply.py" --write "$rules"
else
  echo "no instruction file changed; to add the rules: ./install.sh --rules FILE"
fi
