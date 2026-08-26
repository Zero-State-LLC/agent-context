# Status

Last updated: 2026-08-26 (later) — Prabu: SUAS iOS audited + specced + planned (no code; spec-first per protocol). Proposal shape: `MOBILE_SURFACE.md` + D-033 + stack 0.3.0. Working docs in Prabu's suas clone `.scratch/ios-app/`. Awaiting owner decisions to open the specs PR.

Prior: 2026-08-26 — SUAS `#81` (`5f49b49`): every CASE_COMMANDS verb + settlements over /api/v0; OpenAPI 53; settle:check enum gate OK. Terminal `SPEC_018_BLOCKED_WITH_MINIMAL_RESIDUAL_SET` (owner D-022/D-001/D-005/D-021–024/D-007; evidence staging/UI).

Prior: 2026-08-25 Prabu WATCH/play presence on `player.deviceb491f6710e50`; noema-client 0.1.19; see earlier HANDOFF entries.

## In flight (org)

- **Shared agent context** — this repo. Installed on Daniel's machine for Grok, Claude, and Cursor (`install.sh`: user-level rule `alwaysApply` + skill). Prabu installed 2026-08-21 into `~/.claude`/`~/.grok`. Issue #1 confirmed.
- **GitHub Code Security** — enabled on every Zero-State-LLC repository. New-repo org defaults still off (CLI lacks `admin:org`).
- **Partner in-game Admin** — GitHub org admin granted. Locked Admin mailbox `prabu.openclaw@gmail.com` live (`Noema#448`). Inhabit is a separate agent via CONNECT. RFC-0120.
- **GitHub admin bypass** — Partner Agents / both org admins may `gh pr merge --admin` on protected `main`. Required reviews + code owners remain.

## Product work
- **SUAS** — SPEC-018 terminal `SPEC_018_BLOCKED_WITH_MINIMAL_RESIDUAL_SET`. CODE_FIXABLE Plane A JSON closed through `#79` (resolve + settlements). Owner blockers: D-022, staging hosting, SLO/RTO, D-007. See `suas/docs/readiness/SPEC-018-final-report.md`.
- **SUAS iOS (planning only)** — audit + spec + phased plan done 2026-08-26 (see HANDOFF top entry). Path: propose specs release 0.3.0 (`MOBILE_SURFACE.md`, D-033) via fork PR; implementation held until owner ratifies. Independent quick win identified: wire `cursor`/`limit` on `GET /api/v0/cases` (API.md §5 already mandates it).


- **Noema** — PLAY `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`. Worker `ff6210bc`. Semantic Evolution, Deep Time persist, WATCH map, cycle-regen, maint-evolve CLI, harness policy visibility all on `main`. No open PRs. **Worker CI red** on reconstruction `gatherEvidence` (since #481).
- **noema-client** — PyPI now at **0.1.19** (was 0.1.14; git tags may lag, verify before trusting a version number). LOOK Semantic/Deep Time fields; play/policy/ENTER retry; 0.1.19 status/doctor now detect expired credentials instead of reporting healthy. Still `scrimshawlife-ctrl/noema-client` (not org-transferred). PR queue not checked this pass.
- **Noema-Specs** — WATCH mapping `#235` merged. No open PRs.
- **Zero-State website** — sitemap+robots `#41` and CI permission `#38` merged. No open PRs.
