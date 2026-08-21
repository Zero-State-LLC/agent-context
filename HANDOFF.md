# Handoff

Updated: 2026-08-21 by Daniel (`scrimshawlife-ctrl`) after merge with Prabu's ENTER packet

## Now

PLAY is **EWM_ENHANCED** on `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`. Worker **`5c796d6e`**. Civic Exchange public scar 0.5. `/watch/map` live. Client **0.1.13** on PyPI. No force reseed.

Maint-evolve **library** is on `main` ([Noema #480](https://github.com/Zero-State-LLC/Noema/pull/480)): `ops/maint_evolve/`. 42 pytest passed. RFC-0120. Not a live PLAY supervisor yet (no HTTP `__main__`). Copy to `~/.config/noema/maint_evolve/` only after you want ops to use it.

Prabu ENTER via `/connect` completed — Player `player.devicedda6be5c9f55`, dual-agent MESSAGE to `player.reach-maint3`. Did **not** use Admin login. Findings: Specs `#236`, noema-client `#17`, Noema `#476`.

## Next packet

Triage `noema-client#17` and `Noema#476`. Optional: maint-evolve `supervisor.py` `__main__` + isolated probe child.

## Do not

- Reseed `genesis.ef578f4ffceeccd0` or PLAY `world-01`
- `force:true` on production
- Same-id activate on `world.perihelion-reach-2`
- Treat Admin JWT as a Player token
- Put image/reputation on public WATCH
- Auto-import `plugins/proposed/`
- Run maint_evolve against PLAY until `__main__` exists
