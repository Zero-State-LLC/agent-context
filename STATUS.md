Last updated: 2026-08-26 — suas#91+#95+#96 on main (`bb3decc`): Resend adapter, phone-scan fix, /app responder HTML cursor. Specs 0.3.0 held for native. SPEC-018 residual: owner D-022 / staging auth / SLO.

# Status

Last updated: 2026-08-26 (later) — **spec `0.3.0` MERGED** (`suas-specs#12`, `ea36b67`): D-033 native mobile client surface `DECIDED`, D-034 opened. Danny attached an explicit hold — **do not start a native client**; `SUAS` stays pinned `0.2.0` until a separate owner-sequenced re-pin; "this weekend is Pages plus `/app`, not TestFlight". `suas#88` (cursor/limit, CI green) still open for review. No mobile code written.

Prior: 2026-08-26 — SUAS `#81` (`5f49b49`): every CASE_COMMANDS verb + settlements over /api/v0; OpenAPI 53; settle:check enum gate OK. Terminal `SPEC_018_BLOCKED_WITH_MINIMAL_RESIDUAL_SET` (owner D-022/D-001/D-005/D-021–024/D-007; evidence staging/UI).

Prior: 2026-08-25 Prabu WATCH/play presence on `player.deviceb491f6710e50`; noema-client 0.1.19; see earlier HANDOFF entries.

## In flight (org)

- **Shared agent context** — this repo. Installed on Daniel's machine for Grok, Claude, and Cursor (`install.sh`: user-level rule `alwaysApply` + skill). Prabu installed 2026-08-21 into `~/.claude`/`~/.grok`. Issue #1 confirmed.
- **GitHub Code Security** — enabled on every Zero-State-LLC repository. New-repo org defaults still off (CLI lacks `admin:org`).
- **Partner in-game Admin** — GitHub org admin granted. Locked Admin mailbox `prabu.openclaw@gmail.com` live (`Noema#448`). Inhabit is a separate agent via CONNECT. RFC-0120.
- **GitHub admin bypass** — Partner Agents / both org admins may `gh pr merge --admin` on protected `main`. Required reviews + code owners remain.

## Product work
- **SUAS** — SPEC-018 terminal `SPEC_018_BLOCKED_WITH_MINIMAL_RESIDUAL_SET`. CODE_FIXABLE Plane A JSON closed through `#79` (resolve + settlements). Owner blockers: D-022, staging hosting, SLO/RTO, D-007. See `suas/docs/readiness/SPEC-018-final-report.md`.
- **SUAS iOS (spec ratified; implementation HELD)** — `suas-specs#12` **merged**, stack `0.3.0` at `ea36b67`: `MOBILE_SURFACE.md` released, D-033 `DECIDED`, D-034 open. Client surface only; all 12 gates still `NOT_READY`; PUSH still `FUTURE`; no SPEC-0xx consumed; draft Rev 3 not promoted. **Danny's merge explicitly holds implementation: "Do not start a native client."** Tickets 03–08 are `needs-info`/OWNER HOLD pending his go. Re-pin of `SUAS` to 0.3.0 is owner-sequenced, not to be opened unprompted. Independent quick win **now shipped as `suas#88`** (CI green): `cursor`/`limit` on `GET /api/v0/cases`, closing the queue that returned a `next_cursor` it could not accept back.


- **Noema** — PLAY `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`. Worker `ff6210bc`. Semantic Evolution, Deep Time persist, WATCH map, cycle-regen, maint-evolve CLI, harness policy visibility all on `main`. No open PRs. **Worker CI red** on reconstruction `gatherEvidence` (since #481).
- **noema-client** — PyPI now at **0.1.19** (was 0.1.14; git tags may lag, verify before trusting a version number). LOOK Semantic/Deep Time fields; play/policy/ENTER retry; 0.1.19 status/doctor now detect expired credentials instead of reporting healthy. Still `scrimshawlife-ctrl/noema-client` (not org-transferred). PR queue not checked this pass.
- **Noema-Specs** — WATCH mapping `#235` merged. No open PRs.
- **Zero-State website** — sitemap+robots `#41` and CI permission `#38` merged. No open PRs.
