# Handoff

Updated: 2026-08-21 by Daniel (`scrimshawlife-ctrl`)

## Now

Isolated EWM live-LOOK verifier is wired. Live PLAY is unchanged.

- Isolated `test.hosted-canonical.ewm-cutover` / `genesis.c683369b09acad07`: ENTER/LOOK/HARVEST 200, `Harvested 1 materials`
- `verify_ewm_test_activation.py` ingests operator LOOK. Unset → `VERIFICATION: NOT_A_TEST_DO` exit 2. Set → twice `VERIFICATION: NEEDS_ATTENTION` (velocity 2.00, conc 100%, th 5.00, HIGH_CONCENTRATION). Not canned 12/15/3.8.
- Live `/ready`: `world.perihelion-reach-2` / `genesis.dbeb43d198ce81b1` seq **455** ACTIVE HEALTHY. No genesis activate / force on that world.

## Next packet

Same-id EWM cutover of reach-2 is still forbidden (409 / force 403). Needs a new `world_id` RFC. Isolated health NEEDS_ATTENTION is one-agent concentration, not a reseed trigger.

## Do not

- Reseed `genesis.ef578f4ffceeccd0` or PLAY `world-01`
- `force:true` genesis on production
- Treat canned verifier PASS as proof
- Treat Admin JWT as a Player token
