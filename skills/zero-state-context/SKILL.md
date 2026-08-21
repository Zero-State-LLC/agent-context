---
name: zero-state-context
description: Load and update Zero State team context so work survives machines, models, and both partners' agents.
---

# Zero State shared context

Team durable knowledge is the git repo at `~/agent-context` (or `$ZERO_STATE_CONTEXT`).

## When to load

Any session that continues org work, partner work, or a prior agent session.

Read, in order:

1. `HANDOFF.md`
2. `STATUS.md`
3. `DECISIONS.md` only if a prior choice affects this task

## When to write

If this session changed what the other person or another model must know:

1. Overwrite `HANDOFF.md` with the current baton
2. Update `STATUS.md` if in-flight work changed
3. Append a dated entry to `DECISIONS.md` only for a real decision
4. `git pull --ff-only && git add … && git commit && git push` in that repo

Do not write secrets, personal preferences, or raw transcripts there.
