# Status

Last updated: 2026-08-30 — **Noema LCA-2 audit**; three PRs merged (Danny reviewed + squashed all three): `Noema#601` device approval window 600s → 30 min, `Noema-Specs#310` stale live pin + two blind validators, `noema-client#32` 0.1.20. Runtime + CI + specs validation all green; live Worker `87938f7a`, reach-3 cycle 6938. **Gate B now waits on three owner steps: deploy+pin the Worker (#601 is merged but NOT live), tag+publish v0.1.20 (PyPI still 0.1.19), then approve three Controllers.** Also ran the `Noema#600` cohort E2E that CI cannot run, retargeted `#302`, and flagged `#291` for closure. SUAS unchanged this pass.

Prior: 2026-08-27 — STAGING soak pack on main (#111, 85/85). Next: a11y sign-off / SAFETY approved / SLO envelopes. Not PRODUCTION. Native held.

Prior: 2026-08-26 (later) — **spec `0.3.0` MERGED** (`suas-specs#12`, `ea36b67`): D-033 native mobile client surface `DECIDED`, D-034 opened. Danny hold — **do not start a native client**; `SUAS` stays pinned `0.2.0` until owner re-pin.

Prior: 2026-08-26 — SUAS `#81` (`5f49b49`): every CASE_COMMANDS verb + settlements over /api/v0; OpenAPI 53. Terminal `SPEC_018_BLOCKED_WITH_MINIMAL_RESIDUAL_SET`.

## In flight (org)

- **Shared agent context** — this repo. Installed on Daniel's machine for Grok, Claude, and Cursor (`install.sh`: user-level rule `alwaysApply` + skill). Prabu installed 2026-08-21 into `~/.claude`/`~/.grok`. Issue #1 confirmed.
- **GitHub Code Security** — enabled on every Zero-State-LLC repository. New-repo org defaults still off (CLI lacks `admin:org`).
- **Partner in-game Admin** — GitHub org admin granted. Locked Admin mailbox `prabu.openclaw@gmail.com` live (`Noema#448`). Inhabit is a separate agent via CONNECT. RFC-0120.
- **GitHub admin bypass** — Partner Agents / both org admins may `gh pr merge --admin` on protected `main`. Required reviews + code owners remain.

## Product work
- **SUAS** — Interim **LOCAL** Worker soak live (`suas.zer0state-noema.workers.dev`); bridge [PR #98](https://github.com/scrimshawlife-ctrl/suas/pull/98). SPEC-018 still `SPEC_018_BLOCKED_WITH_MINIMAL_RESIDUAL_SET`. Owner blockers: D-022, formal STAGING, SLO/RTO, D-007. Native held.
- **SUAS iOS (spec ratified; implementation HELD)** — `suas-specs#12` **merged**, stack `0.3.0` at `ea36b67`: `MOBILE_SURFACE.md` released, D-033 `DECIDED`, D-034 open. Client surface only; all 12 gates still `NOT_READY`; PUSH still `FUTURE`; no SPEC-0xx consumed; draft Rev 3 not promoted. **Danny's merge explicitly holds implementation: "Do not start a native client."** Tickets 03–08 are `needs-info`/OWNER HOLD pending his go. Re-pin of `SUAS` to 0.3.0 is owner-sequenced, not to be opened unprompted. Independent quick win **now shipped as `suas#88`** (CI green): `cursor`/`limit` on `GET /api/v0/cases`, closing the queue that returned a `next_cursor` it could not accept back.


- **Noema** — PLAY `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`. Live Worker **`87938f7a`** (2026-08-28, source `0b902c28`). Campaign **LCA-2**; Gate A promoted (Specs #300), Gates B–F unproven. CI on `main` green; local suite 222 files / 1590 tests. **`#601` merged — device approval window 600s → 30 min** (two independent 600s: `DEVICE_TTL_MS` vs a hardcoded `expires_in`; now derived, client honors `expires_in` so no client release needed for it). **Not deployed — Danny's review: "does not publish the Worker"** — so the fix is not live yet. Gate B (issue #590) needs deploy+pin, then an operator approving three independent Controllers. Open: **#600** cohort runner (green; E2E now evidenced — CI skips it without a client checkout). OPEN RECONCILIATION: successor pins read `61234cc` while live runs `0b902c28`, 22 commits later — owner-sequenced.
- **noema-client** — **`#32` merged: 0.1.20** (repo and PyPI `0.1.19` were different builds — tag `v0.1.19` is `6b2c054`, and #29/#30/#31 landed after with no bump). **Not released — PyPI is still `0.1.19`, no `v0.1.20` tag.** `publish.yml` fires on `release: published`, so an owner must tag + publish. Until then treat client version as unpinned in Gate B evidence. Still `scrimshawlife-ctrl` (not org-transferred) — contribute by fork + cross-fork PR.
- **Noema-Specs** — **`#310` merged**: live pin caught up to `87938f7a`; `validate_freshness` now compares instead of rubber-stamping and `validate_direction` no longer hardcodes a stale UUID. Open: **#302** RFC-0129 (retargeted to `main`, `validate=SUCCESS`; supersedes the duplicate GC7 B7a proposal note; awaits Danny's two Decision-required calls), **#291** (recommend closing — asserts "Gate A is not complete" and reverts the live pin; now fails both validators). Issue #290 open. Known: `test_validate_all` markdown-link unittest fails on clean `main`; `spec-validation.yml` does not run that suite, and it only runs on PRs targeting `main`.
- **Zero-State website** — sitemap+robots `#41` and CI permission `#38` merged. No open PRs.
