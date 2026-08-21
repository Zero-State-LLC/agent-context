# Handoff

Updated: 2026-08-20 by Daniel (`scrimshawlife-ctrl`)

## Now

Shared agent context repo exists: `Zero-State-LLC/agent-context`.

Daniel's machine:

- Clone at `~/agent-context`
- `install.sh` has linked the Grok/Claude/Cursor rule + skill
- Grok `[memory]` enabled locally (personal layer only)

## Prabu

1. Clone and install (commands in README / the GitHub issue assigned to you)
2. Confirm your agents load `HANDOFF.md` at session start
3. Reply on the issue when done so we know both sides are live

## Do not

- Commit `~/.grok/memory` or OpenClaw/Claude session files
- Re-enable org-wide code-security defaults without `admin:org` (needs a UI click or `gh auth refresh -s admin:org`)
