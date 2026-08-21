# Handoff

Updated: 2026-08-21 by Daniel (`scrimshawlife-ctrl`)

## Now

Noema unique unmerged work is on `main` and production.

- Runtime: https://github.com/Zero-State-LLC/Noema/pull/446 merged (`038fc25`)
- Client: https://github.com/scrimshawlife-ctrl/noema-client/pull/13 merged; GitHub release `v0.1.10` (PyPI publish on release)
- Production Worker `noema-gateway` version `d6a5abf1-1dd8-46ab-9e91-089ce7e98708` (2026-08-21T04:53:38Z)
- Live `/ready`: ACTIVE, `world.perihelion-reach-2` / `genesis.dbeb43d198ce81b1`, `Cache-Control: no-store`

## What was kept (not abandoned)

Closed PRs claimed a merge they did not do:

- Noema #445 (`e2e-play-fixes-2026-08`) — salvage-cache harvest seed. Branch was 157 commits behind; merging it wholesale would have reverted RFC-0121 successor genesis, Feature D, and structured affordances. Unique seed was ported onto successor Civic Exchange only.
- Client #12 — INSPECT label resolution, MESSAGE `player.` recipients, CLI `act ENTER_WORLD` without observe. Branch dropped 0.1.9 LOOK-field maps; those were kept.
- `jcode/noema-improvements` — JSON 400 INVALID_REQUEST, Cache-Control no-store, operator-env 0600. Ported without committing wrangler-generated `worker-configuration.d.ts`.

Stale feature branches remain as history. Do not merge them as-is.

## Live world

`entity.salvage-cache` is in **new** successor genesis, not injected into the already-cutover DO. Frozen first world unchanged. No reseed.

## Prabu

Still needs to clone `agent-context`, run `install.sh`, and comment on https://github.com/Zero-State-LLC/agent-context/issues/1.

## Do not

- Commit `~/.grok/memory` or OpenClaw/Claude session files
- Re-enable org-wide code-security defaults without `admin:org`
- Merge stale Noema branches (`e2e-play-fixes-2026-08`, `jcode/noema-improvements`, squash leftovers) onto `main`
- Reseed `genesis.ef578f4ffceeccd0` or the live successor DO
