# Handoff

Updated: 2026-08-21 by Daniel (`scrimshawlife-ctrl`) after merge with Prabu's ENTER packet

## Now

PLAY is **EWM_ENHANCED** on `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`. Worker **`ff6210bc`**. Client **0.1.14**. No force reseed.

Live (`tester` + `reach-maint3`, Civic Exchange, cycle 153):
- Cycle production regen (#484): WAIT 150→151 stock 0.15→**1.15**
- HARVEST salvage at cycle 153: **MICRO_GENESIS_CAPACITY** `max_stock 18 -> 20` on salvage-cache
- TRADE `trade.0480` propose+accept **settled** (tester energy→maint compute)

## Next packet

Optional: maint-evolve `supervisor.py` `__main__`.

## Do not

- Reseed `genesis.ef578f4ffceeccd0` or PLAY `world-01`
- `force:true` on production
- Same-id activate on `world.perihelion-reach-2`
- Treat Admin JWT as a Player token
- Put image/reputation on public WATCH
- Auto-import `plugins/proposed/`
- Run maint_evolve against PLAY until `__main__` exists
