#!/usr/bin/env bash
# Link shared Zero State agent context into local harness dirs.
# Safe to re-run. Does not touch personal memory or session logs.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
RULE_SRC="$ROOT/rules/zero-state-context.md"
SKILL_SRC="$ROOT/skills/zero-state-context"
DRY_RUN=0
HERMES_ONLY=0
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
    --hermes-only) HERMES_ONLY=1 ;;
    --help) printf '%s\n' 'Usage: install.sh [--hermes-only] [--dry-run]'; exit 0 ;;
    *) printf 'Unknown argument: %s\n' "$arg" >&2; exit 2 ;;
  esac
done

reject_symlink_ancestors() {
  local parent
  parent="$(dirname "$1")"
  # Do not canonicalize first: that would hide profile/skills redirects.
  while :; do
    if [[ -L "$parent" ]]; then
      printf 'Refusing symlink ancestor: %s\n' "$parent" >&2
      exit 1
    fi
    [[ "$parent" != / && "$parent" != . ]] || break
    parent="$(dirname "$parent")"
  done
}

link_file() {
  local src="$1" dest="$2"
  reject_symlink_ancestors "$dest"
  if [[ -e "$dest" || -L "$dest" ]]; then
    if [[ -L "$dest" && "$(readlink "$dest")" == "$src" ]]; then
      printf 'already linked %s\n' "$dest"
      return
    fi
    printf 'Refusing to replace existing destination: %s\n' "$dest" >&2
    exit 1
  fi
  if [[ "$DRY_RUN" == 1 ]]; then
    printf '[dry-run] link %s -> %s\n' "$dest" "$src"
    return
  fi
  mkdir -p "$(dirname "$dest")"
  reject_symlink_ancestors "$dest"
  ln -s "$src" "$dest"
  echo "linked $dest"
}

# Hermes is profile-scoped; keep the source checkout at this path.
link_file "$SKILL_SRC" "${HERMES_HOME:-$HOME/.hermes}/skills/zero-state-context"
[[ "$HERMES_ONLY" == 0 ]] || exit 0

# Grok
link_file "$RULE_SRC" "${GROK_HOME:-$HOME/.grok}/rules/zero-state-context.md"
link_file "$SKILL_SRC" "${GROK_HOME:-$HOME/.grok}/skills/zero-state-context"

# Claude Code (create dirs even if unused yet)
link_file "$RULE_SRC" "$HOME/.claude/rules/zero-state-context.md"
link_file "$SKILL_SRC" "$HOME/.claude/skills/zero-state-context"

# Cursor local IDE — user-level alwaysApply rule (.mdc) + skill
link_file "$RULE_SRC" "$HOME/.cursor/rules/zero-state-context.mdc"
link_file "$SKILL_SRC" "$HOME/.cursor/skills/zero-state-context"

echo
echo "Clone path: $ROOT"
echo "Follow the skill safe-sync workflow; publishing requires current user authorization."
echo "Personal memory stays local — do not copy ~/.grok/memory into git."
echo "Cursor Cloud does not see ~/.cursor; it must clone this repo or read HANDOFF via gh."
