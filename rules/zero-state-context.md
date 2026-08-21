# Zero State shared context

Team knowledge for Zero State LLC lives in the git repo cloned at `~/agent-context` (override with `$ZERO_STATE_CONTEXT`).

At session start, when the task involves org status, a partner handoff, or work another Zero State agent may have touched, read:

- `~/agent-context/HANDOFF.md`
- `~/agent-context/STATUS.md`

Before ending a session that changed team status, update those files (and `DECISIONS.md` if a decision was made), then commit and push `~/agent-context`.

Personal memory, session logs, and secrets do not go in that repo. Product code maps stay in each product repo's `graft/` and `AGENTS.md`.
