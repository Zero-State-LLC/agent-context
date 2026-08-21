# Handoff

Updated: 2026-08-21 by Daniel (`scrimshawlife-ctrl`)

## Now

Isolated EWM world is **playable**. Live PLAY is unchanged.

- [#454](https://github.com/Zero-State-LLC/Noema/pull/454) EWM_ENHANCED on Worker
- Isolated `test.hosted-canonical.ewm-cutover` / `genesis.c683369b09acad07` ACTIVATED
- [#455](https://github.com/Zero-State-LLC/Noema/pull/455) isolated bootstrap (`WORLD_BOOTSTRAP` seq 0) deployed `cfc483b0-147e-4e19-a70a-27be8a374121`
- Isolated ENTER 200, HARVEST `Harvested 1 materials` (energy −2, hold +1, stock 8)
- Live PLAY: `world.perihelion-reach-2` / `genesis.dbeb43d198ce81b1` cycle 2 seq **455**

## Next packet

Live EWM cutover of reach-2 is still **409 ALREADY_ACTIVATED** / force 403. Needs a new `world_id` RFC, not a reseed. Optional: wire live LOOK into `verify_ewm_test_activation.py`; bounded patrol on the isolated DO.

## Do not

- Reseed `genesis.ef578f4ffceeccd0` or PLAY `world-01`
- `force:true` genesis on production
- Treat canned verifier PASS as production proof
- Treat Admin JWT as a Player token
