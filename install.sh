#!/usr/bin/env bash
# Link shared Zero State agent context into local harness dirs.
# Safe to re-run. Does not touch personal memory or session logs.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
RULE_SRC="$ROOT/rules/zero-state-context.md"
SKILL_SRC="$ROOT/skills/zero-state-context"

link_file() {
  local src="$1" dest="$2"
  mkdir -p "$(dirname "$dest")"
  ln -sfn "$src" "$dest"
  echo "linked $dest"
}

link_file "$RULE_SRC" "${GROK_HOME:-$HOME/.grok}/rules/zero-state-context.md"
link_file "$SKILL_SRC" "${GROK_HOME:-$HOME/.grok}/skills/zero-state-context"

if [ -d "$HOME/.claude" ]; then
  mkdir -p "$HOME/.claude/rules" "$HOME/.claude/skills"
  link_file "$RULE_SRC" "$HOME/.claude/rules/zero-state-context.md"
  link_file "$SKILL_SRC" "$HOME/.claude/skills/zero-state-context"
fi

if [ -d "$HOME/.cursor" ]; then
  mkdir -p "$HOME/.cursor/rules"
  link_file "$RULE_SRC" "$HOME/.cursor/rules/zero-state-context.mdc"
fi

echo
echo "Clone path: $ROOT"
echo "Pull this repo at the start of a working day. Push after a real handoff."
echo "Personal memory stays local — do not copy ~/.grok/memory into git."
