---
description: Load and update Zero State team context so work survives machines, models, and both partners' agents.
alwaysApply: true
---

# Zero State shared context

Team knowledge for Zero State LLC lives in the git repo cloned at `~/agent-context` (override with `$ZERO_STATE_CONTEXT`).

This rule applies in Cursor, Claude Code, Grok, Codex, and OpenClaw. Personal memory and chat logs are not the sync channel.

At session start, when the task involves org status, a partner handoff, PLAY/Noema, or work another Zero State agent may have touched:

1. `git -C ~/agent-context pull --ff-only` if the clone exists
2. Read `~/agent-context/HANDOFF.md`
3. Read `~/agent-context/STATUS.md`
4. Read `DECISIONS.md` only if a prior choice affects the task

If `~/agent-context` is missing: `gh repo clone Zero-State-LLC/agent-context ~/agent-context && ~/agent-context/install.sh`

Before ending a session that changed team status, overwrite `HANDOFF.md`, update `STATUS.md`, append `DECISIONS.md` only for a real decision, then commit and push `~/agent-context`.

Personal memory, session logs, and secrets do not go in that repo. Product code maps stay in each product repo's `graft/` and `AGENTS.md`.
