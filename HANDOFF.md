# Handoff

Updated: 2026-08-21 by Daniel (`scrimshawlife-ctrl`). Grok session compacted; continuing in **Cursor**.

## Start here (Cursor)

```bash
git -C ~/agent-context pull --ff-only
```

Open **Zero-State-LLC/Noema**. First actions: this file, then `STATUS.md`. For code, use `graft ask` before grep (`AGENTS.md` / `.cursor/rules/graft.mdc`). Do not treat Grok/Claude session logs as source of truth.

## Now

PLAY is **EWM_ENHANCED** on `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`. Production Worker **`ff6210bc`** (`noema-gateway`). Official client **noema-client 0.1.14** (PyPI + git tag `v0.1.14`). Hosted `https://noema.guru`. No force reseed.

Open PR queues for **Noema / Noema-Specs / noema-client / Zero-State website are empty**.

Repos:

| Thing | Where |
|---|---|
| Worker + harness + maint-evolve | `Zero-State-LLC/Noema` (`workers/noema`, `src/noema/harness`, `ops/maint_evolve`) |
| Specs | `Zero-State-LLC/Noema-Specs` |
| Official client | `scrimshawlife-ctrl/noema-client` — **not** transferred to the org |
| Website | `Zero-State-LLC/Zero-State` |
| This baton | `Zero-State-LLC/agent-context` |

## Live (already proven — do not re-prove unless regressing)

Dual-agent inhabit: `tester` + `reach-maint3` at Civic Exchange. Prabu ENTER as `player.devicedda6be5c9f55`.

- Cycle production regen (#484): WAIT 150→151 stock **0.15→1.15**
- HARVEST cycle 153: **MICRO_GENESIS_CAPACITY** `max_stock 18→20` on salvage-cache
- TRADE `trade.0480` propose+accept **settled** (tester energy → maint compute)
- MESSAGE tester↔reach-maint3 `protocol_strength` 2
- Civic Exchange public economic scar after HARVEST; RECONSTRUCT eased then later harvest raised it
- `Cache-Control: no-store` on `/ready`

## Shipped on `main` this arc (do not reimplement)

- Semantic Evolution + Deep Time + WATCH mapping runtime (`/v1/watch/map`, no image/reputation on public WATCH)
- Deep Time persist in `co_evolution.deep_time` blob (#473)
- RECONSTRUCT: empty evidence kinds → `LIVE_INSPECT` if inspected (#481)
- LOOK persist `regen_rate`/`max_stock`; load defaults; warm-DO `migrateWorldRuntime` (#481–#483)
- Cycle-commit regen on **all** `stock_resource` nodes toward `max_stock` (#484)
- Maint-evolve library + CLI (#480/#485): `python -m maint_evolve.supervisor` → `halt_inhabit: false`, `spawn_patrol: false`. Probe refuses PLAY / `world-01` / reach-2. Live copy `~/.config/noema/maint_evolve/`
- Client 0.1.14: default play skips WAIT-first; `ClientPolicy` `allow_org_create`/`allow_contest` default **True**; `doctor`/`status` `policy_blocked_actions`; `NOT_IN_WORLD` → `ensure_in_world()`
- Harness #479: `HarnessPolicy.blocked()` visibility only (`permits()` still defaults org/contest/access **False**)
- Specs WATCH mapping #235

RFC-0122 PLAY default is reach-3 (two-deploy admit+activate then `DEFAULT_WORLD_ID`). Same-id EWM on reach-2 is 409/403.

## Next packet (pick one)

1. **Fix Noema worker CI** — `main` is red. Reconstruction `gatherEvidence` expected true, got false (`test/reconstruction.test.ts`, `test/agent-reconstruct.test.ts`) since Deep Time / #481. Unrelated to harness #479. Do this before treating CI as a merge gate.
2. Isolated live probe: `--world-id test.hosted-canonical.ewm-cutover` with **Player** tester token. Not PLAY. Do not `--spawn-patrol` until you mean it.
3. Org-wide leftover (not Noema): Prabu CI clones (`repository-projects`, CodeQL-free scanning) on Kubrick/Hyperlex/NeonGenie/etc. Batch only if asked.

## Do not

- Reseed `genesis.ef578f4ffceeccd0` or PLAY `world-01`
- `force:true` on production
- Same-id activate on `world.perihelion-reach-2` (PLAY is **reach-3**)
- Treat Admin JWT as a Player token (RFC-0120). Prabu Admin mailbox `prabu.openclaw@gmail.com` is control-plane only; inhabit is CONNECT + official client
- Put `image_score` / reputation scalars on public WATCH (GC3)
- Auto-import `ops/maint_evolve/plugins/proposed/`
- Run maint_evolve PLAY inhabit with Admin JWT
- Merge stale historical branches as-is; port unique patches onto current `main`
- Put secrets, tokens, or session transcripts in this repo

## Merge path

Protected `main` keeps 1 review + code owners. Partner Agents / org admins may `gh pr merge --admin`. Prefer a partner review when both are around.
