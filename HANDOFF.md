# Handoff

Updated: 2026-08-21 by Daniel (`scrimshawlife-ctrl`)

## Now

Leftover unique Noema work is **adapted onto current surfaces** and live.

- Runtime: https://github.com/Zero-State-LLC/Noema/pull/447 merged
- Client: https://github.com/scrimshawlife-ctrl/noema-client/pull/14 merged; release `v0.1.11`
- Production Worker `noema-gateway` version `0c6e470f-5ceb-4556-adf0-0c56e3283f93`
- Live `/ready`: ACTIVE `world.perihelion-reach-2` / `genesis.dbeb43d198ce81b1`
- Watch HTML now has `watch-here-open` / `watch-here-sheet`

## Adapted (not abandoned)

Stale branches were **not** merged as-is. Unique intent was rewritten onto today's architecture:

| Leftover | Adapt |
|---|---|
| #445 salvage-cache on live play | `ensureSuccessorMaterialsCache` on successor DO load. Frozen `world-01` untouched. |
| PLAY phone Here sheet (`play.ts`) | PLAY HTML is gone (RFC-0120). Same sheet now on **Watch**: map stays, Recently is the sheet. |
| Client `message hermes hi` | 0.1.11 splits handle vs text so `player.` prefixing works. |
| GC1-S2 plan/design docs | Landed (runtime already hosted). |
| graft AGENTS.md | Landed; `graft/` stays gitignored. |

Already on `main` from earlier squash/packets: device enrollment, tenant tester, two-door CONNECT, Phosphor, RFC-0120 identity, cargo, admin brief, `/ready` play_blocked, Deep Time fixtures, operator-env 0600, INVALID_REQUEST.

## Deliberately not restored

- Invented harvest from INFRASTRUCTURE labels (explicit `stock_resource` instead)
- Hosted PLAY inhabit chamber HTML
- Client org/contest/access fail-open defaults

## Prabu

Still needs to clone `agent-context`, run `install.sh`, and comment on https://github.com/Zero-State-LLC/agent-context/issues/1.

## Do not

- Commit `~/.grok/memory` or OpenClaw/Claude session files
- Merge stale Noema branches as-is
- Reseed `genesis.ef578f4ffceeccd0` or point PLAY at `world-01`
