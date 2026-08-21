# Handoff

Updated: 2026-08-21 by Daniel (`scrimshawlife-ctrl`) after PR queue drain

## Now

PLAY is **EWM_ENHANCED** on `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`. Worker **`ff6210bc`**. Client **0.1.14**. No force reseed.

Open PR queues for Noema / Noema-Specs / noema-client / Zero-State website are **empty**.

Just handled:
- Merged [Noema #479](https://github.com/Zero-State-LLC/Noema/pull/479) — harness `HarnessPolicy.blocked()` visibility (permits unchanged; twin of client #476)
- Closed [Noema #478](https://github.com/Zero-State-LLC/Noema/pull/478) — docs plan superseded by #477/#480/#485
- Closed [noema-client #18](https://github.com/scrimshawlife-ctrl/noema-client/pull/18) — superseded by #19 (`0.1.14` ENTER retry)
- Merged [Zero-State #41](https://github.com/Zero-State-LLC/Zero-State/pull/41) — sitemap.xml + robots.txt for zer0state.com
- Merged [Zero-State #38](https://github.com/Zero-State-LLC/Zero-State/pull/38) — valid `repository-projects` GITHUB_TOKEN key

Maint-evolve CLI is on `main` ([Noema #485](https://github.com/Zero-State-LLC/Noema/pull/485)). Smoke: `python -m maint_evolve.supervisor` → `halt_inhabit: false`, `spawn_patrol: false`. Probe still requires `test.*` world_id.

## Next packet

Isolated live probe (`--world-id test.hosted-canonical.ewm-cutover`) with tester token if you want scar persist on a test DO. Do not `--spawn-patrol` until you mean it.

Worker CI on Noema `main` is red (reconstruction `gatherEvidence` expected true got false) since Deep Time / #481. Unrelated to the harness merge. Fix the tests before treating CI green as a gate.

Org still has a copy-pasta stack of Prabu CI PRs (`repository-projects` + CodeQL-free scanning) across Kubrick/Hyperlex/NeonGenie/etc. Not Noema. Leave unless you want a batch merge.

## Do not

- Reseed `genesis.ef578f4ffceeccd0` or PLAY `world-01`
- `force:true` on production
- Same-id activate on `world.perihelion-reach-2`
- Treat Admin JWT as a Player token
- Put image/reputation on public WATCH
- Auto-import `plugins/proposed/`
- Run maint_evolve PLAY inhabit with Admin JWT
