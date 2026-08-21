# Handoff

Updated: 2026-08-21 by Daniel (`scrimshawlife-ctrl`)

## Now

Live successor play ran. Docs pins name the successor.

- ENTER: `player.reach-maint3` and `player.tester` Civic Exchange 200. Report [Noema #450](https://github.com/Zero-State-LLC/Noema/pull/450) / [LIVE-SUCCESSOR-PLAY-2026-08-21.md](https://github.com/Zero-State-LLC/Noema/blob/main/docs/LIVE-SUCCESSOR-PLAY-2026-08-21.md)
- HARVEST: advertised on `entity.salvage-cache` (materials). tester HARVEST 200 **credits energy**, stock 4→3, CONSTRUCT still no materials in hold. maint energy 1 → BUDGET_EXCEEDED. WAIT does not restore energy with empty hold.
- Honesty pins: [Noema #451](https://github.com/Zero-State-LLC/Noema/pull/451) `hosted_live` = `world.perihelion-reach-2` / `genesis.dbeb43d198ce81b1`. Frozen first world historical.
- Specs remaining-work: [Noema-Specs #227](https://github.com/Zero-State-LLC/Noema-Specs/pull/227)
- **Prabu's agent has not ENTER'd.**

## Next packet

Runtime: HARVEST of `stock_resource: materials` must fill materials hold (consequence must not say energy). Then re-prove CONSTRUCT. Prabu ENTER via `/connect`.

## Do not

- Invent harvest from INFRASTRUCTURE labels
- Reseed `genesis.ef578f4ffceeccd0` or PLAY `world-01`
- Treat Admin JWT as a Player token
