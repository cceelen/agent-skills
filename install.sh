#!/bin/sh
# Install skills from this repository.
#   ./install.sh                         all skills, for Claude Code (~/.claude/skills)
#   ./install.sh --agent codex           all skills, for OpenAI Codex (~/.agents/skills)
#   ./install.sh --dir PATH [SKILL ...]  the named skills (default: all) into PATH
set -e
here=$(cd "$(dirname "$0")" && pwd)
dest="$HOME/.claude/skills"
while [ $# -gt 0 ]; do
  case "$1" in
    --agent)
      case "$2" in
        claude) dest="$HOME/.claude/skills" ;;
        codex) dest="$HOME/.agents/skills" ;;
        *) echo "unknown agent: $2 (use claude or codex, or --dir PATH)" >&2; exit 2 ;;
      esac
      shift 2 ;;
    --dir) dest="$2"; shift 2 ;;
    -h|--help) sed -n '2,5p' "$0"; exit 0 ;;
    *) break ;;
  esac
done
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
