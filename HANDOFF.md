# Handoff

Updated: 2026-08-21 by Daniel (`scrimshawlife-ctrl`)

## Now

EWM_ENHANCED is **on the Worker**, not on live PLAY.

- [#454](https://github.com/Zero-State-LLC/Noema/pull/454) merged+deployed (`0984d583-ca8e-415b-9b6c-370db0a978a5`). Rebased #453 onto current main (did not revert RFC-0121 / materials HARVEST). #453 closed.
- Isolated genesis **activated**: `test.hosted-canonical.ewm-cutover` / `genesis.c683369b09acad07` / EWM_ENHANCED / salvage-cache materials×8 regen 1.15 / three archetypes / production node. Preview `live_world_unchanged`.
- Isolated ENTER is blocked: `NONCONTIGUOUS_SEQUENCE` on `/v1/operator/test-world/command`.
- Live PLAY unchanged: `world.perihelion-reach-2` / `genesis.dbeb43d198ce81b1` cycle 2 seq 455 ACTIVE HEALTHY.

## Next packet

1. Fix isolated test-world settlement (NONCONTIGUOUS_SEQUENCE) so ENTER/HARVEST can prove regen.
2. Do **not** force-activate EWM onto live reach-2 (409 ALREADY_ACTIVATED; force 403). Live promotion needs a new `world_id` RFC.

## Do not

- Reseed `genesis.ef578f4ffceeccd0` or PLAY `world-01`
- `force:true` genesis on production
- Treat canned `verify_ewm_test_activation.py` as a test-DO proof
- Treat Admin JWT as a Player token
