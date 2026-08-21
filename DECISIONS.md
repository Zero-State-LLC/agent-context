# Decisions

## 2026-08-21 — Partner Agents may admin-bypass required reviews

**Decision:** Keep 1 review + code owners on every protected `main`. Grant `bypass_pull_request_allowances` to users `scrimshawlife-ctrl`, `prabu-openclaw` and team `partner-agents`. Do not set `enforce_admins` false and do not drop the review count.

**Why:** Two-person org: the PR author cannot approve their own PR, so agents deadlock. Temporarily zeroing reviews was worse than a named admin bypass.

**Implications:**

- `gh pr merge --admin` (or GitHub UI admin merge) is the solo-ship path
- Prefer a partner review when both are around
- Applied on every Zero-State-LLC repo that already had this protection (not `agent-context` / `Hollersports`, which were unprotected)

## 2026-08-21 — Partner Admin is control-plane; inhabit is a separate agent

**Decision:** Prabu gets in-game Admin via a locked mailbox (`prabu.openclaw@gmail.com`). He does **not** inherit Player. His agent inhabits through `/connect` and the official client.

**Why:** RFC-0120 and ADMIN-LIVE-OPERATIONS forbid Admin-as-Player. GitHub org admin was already true and is the repo-update path. Inside-play is a different principal.

**Implications:**

- Magic link `/admin/login` from that mailbox is Recover/overview/operator Watch only
- Dual-agent debugging starts when both Controllers ENTER `world.perihelion-reach-2`
- Findings update Specs remaining-work and product PRs, not session logs
- `main` still has one Partner Agents review for non-bypass actors; org admins may `--admin` merge

## 2026-08-21 — Adapt leftover unique work onto current surfaces

**Decision:** Remaining unique intent from stale branches is rewritten onto today's product surfaces (Watch, successor DO load, official client), not merged as historical trees.

**Why:** PLAY Chamber HTML is deleted under RFC-0120. Harvest must not be invented from INFRASTRUCTURE labels. Frozen first world must not be reseeded.

**Implications:**

- Live successor harvest node is an idempotent DO-load fill (`entity.salvage-cache`), not a genesis reseed
- Phone Here sheet is a Watch spectator control, not a restored inhabit chamber
- Client 0.1.11 only splits `message <handle> <text>`; policy stays fail-closed

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
