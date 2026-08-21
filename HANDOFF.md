# Handoff

Updated: 2026-08-21 by Daniel (`scrimshawlife-ctrl`)

## Now

PLAY is **EWM_ENHANCED** on `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`. Worker **`31e7c436`**. `/watch/map` live. No force reseed.

Official client **0.1.13** forwarded Semantic + Deep Time LOOK fields: [noema-client #16](https://github.com/scrimshawlife-ctrl/noema-client/pull/16).

Tester HARVEST×3 succeeded on Civic Exchange; LOOK after did not yet show `scars` (fragments=1). Isolated tests still pass. Possible durable-head restore dropping new Deep Time fields — investigate before relying on live scar residue.

## Next packet

- Prabu ENTER via `/connect`
- Trace why live HARVEST did not persist `WorldRuntime.scars` (canonical head vs DO)
- PyPI publish 0.1.13 if you want agents on the new client

## Do not

- Reseed `genesis.ef578f4ffceeccd0` or PLAY `world-01`
- `force:true` on production
- Same-id activate on `world.perihelion-reach-2`
- Treat Admin JWT as a Player token
- Put image/reputation on public WATCH
- Rewrite the canonical ledger from reconstruction
- Replace lightweight `/watch` theater
