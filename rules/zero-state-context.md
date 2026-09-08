---
description: Load and update Zero State team context so work survives machines, models, and both partners' agents.
alwaysApply: true
---

# Zero State shared context

Team knowledge for Zero State LLC lives in the git repo cloned at `~/agent-context` (override with `$ZERO_STATE_CONTEXT`).

This rule applies in Cursor, Claude Code, Grok, Codex, and OpenClaw. Personal memory and chat logs are not the sync channel.

Use the [shared-context skill](../skills/zero-state-context/SKILL.md)'s
Safe shared-context workflow: confirm repo/remote/branch, require a clean tree,
fetch and fast-forward before reading/drafting, reconcile concurrent handoffs,
review precisely staged files for secrets, and publish only with current user
authorization. Verify the exact remote commit after an authorized push.
Do not copy personal memory, raw transcripts, or secrets into team context.
