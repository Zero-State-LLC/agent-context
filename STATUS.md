# Status

Last updated: 2026-08-30 — **Noema LCA-2 audit**: runtime + CI + specs validation all green; live Worker `87938f7a` (2026-08-28), reach-3 cycle 6938. Campaign at **LCA-2 / Gate B, blocked on human enrollment approval** (six codes expired; 600s window is too short to be workable). Opened `Noema-Specs#310` (stale live pin + two blind validators) and `noema-client#32` (0.1.20 — repo and PyPI `0.1.19` are different builds). Ran and posted the `Noema#600` cohort E2E that CI cannot run. SUAS unchanged this pass.

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


- **Noema** — PLAY `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`. Live Worker **`87938f7a`** (2026-08-28, source `0b902c28`). Campaign **LCA-2**; Gate A promoted (Specs #300), Gates B–F unproven. **Worker CI on `main` is green** — the old `gatherEvidence` red is fixed (#595/#596); local suite 222 files / 1590 tests pass. **Gate B blocked on a human approving device enrollment** (issue #590; six codes expired unapproved, 600s window). Needs three independently controlled external Controllers — isolated cohort is `NOT_COMPUTABLE` by design. Open: **#600** cohort runner (green; E2E now evidenced). OPEN RECONCILIATION: successor pins read `61234cc` while live runs `0b902c28`, 22 commits later — owner-sequenced.
- **noema-client** — **Version string is currently untrustworthy:** repo `main` declares `0.1.19` but tag `v0.1.19` is `6b2c054` (#28); #29/#30/#31 landed after with no bump, so repo `0.1.19` and PyPI `0.1.19` are **different builds**. `noema-client#32` bumps to **0.1.20**; an owner must tag + publish a release (`publish.yml` fires on `release: published`). Until then treat client version as unpinned in any Gate B evidence. Still `scrimshawlife-ctrl` (not org-transferred) — contribute by fork + cross-fork PR.
- **Noema-Specs** — Gate A promotion + GC campaign pass merged (#300–#309). Open: **#310** (fixes stale live-Worker pin and two validators that reported OK — `validate_freshness` never compared, `validate_direction` hardcoded the stale UUID), **#291** (stale, pins `d86352b2`), **#302** (stacked on merged #301, needs retarget). Issue #290 open. Known: `test_validate_all` markdown-link unittest fails on clean `main`; `spec-validation.yml` does not run that suite.
- **Zero-State website** — sitemap+robots `#41` and CI permission `#38` merged. No open PRs.
