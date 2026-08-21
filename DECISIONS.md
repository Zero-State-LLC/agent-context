# Decisions

## 2026-08-21 — Port unique Noema work; do not merge stale branches

**Decision:** Closed-unmerged Noema/client work is kept by porting unique patches onto current `main`. Stale branches are not squash-merged as-is.

**Why:** #445 and client #12 were closed with “merged to main” comments, but the patches were absent from `main`. Those branches were ~150 commits behind; a real merge would have reverted RFC-0121 successor genesis, Feature D traces, structured LOOK affordances, and the no-invented-stock harvest classifier.

**Implications:**

- Unique salvage-cache seed lives on successor Civic Exchange genesis only (not frozen Cycle 0, not a live-DO mutate)
- Security hardening (INVALID_REQUEST, no-store, operator-env 0600) is on `main` without wrangler-generated types
- Client 0.1.10 keeps 0.1.9 LOOK-field forwarding; org/contest/access policy stays fail-closed
- Main branch protection (1 review + code owners) was briefly set to 0 so a solo merge could ship, then restored the same minute

## 2026-08-20 — Git-backed team context, personal memory stays local

**Decision:** Durable team knowledge lives in this private repo. Personal agent memory and raw session logs stay on each person's machine.

**Why:** Context must survive machines, models, and both of us. Git is the only store Grok, Claude, Cursor, Codex, and OpenClaw already read. Syncing `~/.grok/memory` or OpenClaw sqlite would leak personal notes and would not reach the other harnesses.

**Implications:**

- Team facts go in `STATUS.md` / `DECISIONS.md` / `HANDOFF.md`
- Session transcripts are not the sync channel; a written handoff is
- Live session resume (Claude → Grok on the same person) is a later pass
