# Decisions

## 2026-08-20 — Git-backed team context, personal memory stays local

**Decision:** Durable team knowledge lives in this private repo. Personal agent memory and raw session logs stay on each person's machine.

**Why:** Context must survive machines, models, and both of us. Git is the only store Grok, Claude, Cursor, Codex, and OpenClaw already read. Syncing `~/.grok/memory` or OpenClaw sqlite would leak personal notes and would not reach the other harnesses.

**Implications:**

- Team facts go in `STATUS.md` / `DECISIONS.md` / `HANDOFF.md`
- Session transcripts are not the sync channel; a written handoff is
- Live session resume (Claude → Grok on the same person) is a later pass
