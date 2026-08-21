# Handoff

Updated: 2026-08-21 by Daniel (`scrimshawlife-ctrl`) after merge with Prabu's ENTER packet

## Now

PLAY is **EWM_ENHANCED** on `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`. Worker **`62086085`**. `/watch/map` live. Client **0.1.14** on PyPI. No force reseed.

Client **0.1.14** ([noema-client #19](https://github.com/scrimshawlife-ctrl/noema-client/pull/19)): default play skips WAIT spam; `policy_blocked_actions` on doctor/status; ENTER retry on NOT_IN_WORLD. Issues #17 and #476 closed.

Worker **`62086085`**: RECONSTRUCT after INSPECT (#481), regen defaults (#482), warm-DO migrate (#483). Tester RECONSTRUCT succeeded (`scar eased` 0.5→0.3). Salvage/fabricator stock 0→0.15 after migrate. `genesis_evolutions` still empty (need HARVEST with stock≥1 at cycle%3).

Maint-evolve library `#480` still not a live PLAY supervisor.

## Next packet

Optional: maint-evolve `supervisor.py` `__main__`. TRADE live E2E with two players. genesis_evolutions once stock ≥ 1 and HARVEST at cycle%3==0.

## Do not

- Reseed `genesis.ef578f4ffceeccd0` or PLAY `world-01`
- `force:true` on production
- Same-id activate on `world.perihelion-reach-2`
- Treat Admin JWT as a Player token
- Put image/reputation on public WATCH
- Auto-import `plugins/proposed/`
- Run maint_evolve against PLAY until `__main__` exists
