# Decisions

## 2026-09-04 — intent.md is SDLC stage-0

**Decision:** Every product-repo change stream starts with a committed
`intent.md` (proto-spec) **before** spec-kit specify. The blank lives at
`templates/intent.md.template`. Product repos keep accepted intents in
`intent/` or `docs/intent/` — one file per change stream. Do not invent
product intents in this pack.

**Why:** Anthropic AI-Native SDLC and Danny's spec-kit lock both put
intent before spec. Agents that skip to code reopen locks in the PR.
A dated proto-spec with labeled claims (`[verified: …]` / `[assumed: …]`)
is cheaper than a green implementation of the wrong outcome.

**Implications:**

- Stage chain: `intent.md` → constitution (if needed) → specify
  (`spec.md` + `## Workflows`) → plan → tasks → implement → REVIEW /
  evidence → land.
- FORGE owns plan and tasks. Cloud agents implement. No extra bots.
- Human yes on deploy, spend, and legal.
- Thin `AGENTS.md` / `CLAUDE.md` adapters: read the active intent before
  editing. If a non-trivial change has no intent, draft `intent.md` and
  wait for human accept. Do not skip to code.
- Order of work is documented in `templates/sdlc/README.md`.

## 2026-09-04 — agent-context is the canonical product-repo template home

**Decision:** `Zero-State-LLC/agent-context` is the canonical home for
multi-agent repo collab setup. Product repos copy from `templates/`. This pack
stays team-context only.

**Why:** Product `AGENTS.md` files grew into environment diaries (Noema is the
example). Harnesses then forked the contract (`CLAUDE.md` vs `AGENTS.md`).
Agents patched tests to stay green and invented skills or fleets. One short
router plus a dated lock here stops that drift.

**Implications:**

- One `AGENTS.md` contract per product repo. `CLAUDE.md` / optional `CODEX.md`
  are thin adapters only (`@AGENTS.md` or one line pointing at `AGENTS.md`).
- Procedural `AGENTS.md` (about 80 lines; 12 KB ceiling). Long environment
  notes move to `AGENT-GOTCHAS.md`.
- `## Workflows` lives in the product `spec.md`: existing Grok Bot skills,
  one owner specialist if it already exists, and GitHub Actions to reuse or
  add. Defaults: `anti-slop-code`, `production-systems`,
  `google-developer-style`.
- **Escalation:** if CI or tests look wrong, open a labeled defect. Do not
  patch tests to green.
- No agent fleets. ECC is catalog-only — name existing skills, do not invent
  new skills or bots.
- Do not copy product deploy-worker or pin workflows into this repo.

## 2026-08-27 — D-007 retention/deletion (STAGING policy)

**Decision:** Soft-delete operational identity rows on deletion request; **retain Domain Events, Audit Events, and consent history for 365 days** (STAGING synthetic policy). No provider-side erase claim. No HIPAA claim.

**Why:** Matches the shipped synthetic deletion drill (soft-delete + event retention) and gives PRIVACY a concrete duration for STAGING rehearsal. PRODUCTION purge/export package remains separate / SPEC-018.

**Implications:**

- `D_007_RETENTION` is no longer `DECISION_PENDING` for STAGING
- Staging deletion rehearsal may run against synthetic Neon under `SUAS_ENV=STAGING` (fail closed on PRODUCTION / prod URL markers)
- Formal purge after 365 days is a later ops package, not invented here

## 2026-08-26 — D-022 durable jobs = Postgres outbox

**Decision:** SUAS STAGING/PRODUCTION durable async work uses a **Postgres-backed outbox / SKIP LOCKED worker** behind `DurableJobQueuePort` (decision packet option 2). LOCAL/TEST may keep the in-memory fake.

**Why:** Same system of record as domain state; backup/RPO tied to Neon; no new vendor for first durable cut. Revisit managed queue if multi-region/volume demands it.

**Implications:**

- Eng implements `job_outbox` (+ lease worker) and wires factory for STAGING/PRODUCTION
- Formal `SUAS_ENV=STAGING` unblocked once adapter + topology land
- Specs/manifest naming can follow in a later pin; runtime may land under 0.2.0 with D-022 DECIDED recorded here

## 2026-08-21 — PLAY identity is perihelion-reach-3

**Decision:** Live PLAY is `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`. Do not ENTER, activate, or same-id EWM `world.perihelion-reach-2`. Frozen first world remains `world-01` / `genesis.ef578f4ffceeccd0`.

**Why:** RFC-0122 flipped the hosted default with two deploys (admit+activate, then `DEFAULT_WORLD_ID`). An earlier note in this file said dual-agent debugging starts on reach-2; that world is retired for PLAY.

**Implications:**

- Isolated maint-evolve probes use `test.*` world ids only
- Same-id activate on reach-2 is 409/403 and must not be forced

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
