# Handoff

Updated: 2026-08-21 by Daniel (`scrimshawlife-ctrl`)

## Now

Isolated EWM verifier is **PASS**. Live PLAY is unchanged (same genesis).

- Isolated `test.hosted-canonical.ewm-cutover`: tester + `reach-maint3` ENTER. LOOK occupancy-weighted conc 50%. Verifier twice **`VERIFICATION: PASS`**.
- Unset `NOEMA_WORLD_ID` still `NOT_A_TEST_DO` exit 2.
- Live `/ready`: `world.perihelion-reach-2` / `genesis.dbeb43d198ce81b1` ACTIVE HEALTHY. Sequence 455→478 is ordinary PLAY, not a new genesis. No activate/force on that world.

## Next packet

Same-id EWM cutover of reach-2 is still forbidden (409 / force 403). Needs a new `world_id` RFC.

## Do not

- Reseed `genesis.ef578f4ffceeccd0` or PLAY `world-01`
- `force:true` genesis on production
- Treat canned verifier PASS as proof
- Treat Admin JWT as a Player token
