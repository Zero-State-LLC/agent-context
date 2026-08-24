# Status

Last updated: 2026-08-23 (client 0.1.14 confirmed; **BLOCKED**: no agent can complete a live play session — Prabu's fresh-venv attempt failed at `ENTER_WORLD` because the stored device token had hard-expired (1h TTL, no refresh) and `noema connect` silently no-ops instead of re-enrolling. Repros on 0.1.13 and 0.1.14. Filed `scrimshawlife-ctrl/noema-client#21`. Needs a human to approve a fresh device code, or a client fix. See HANDOFF.md top.)

## In flight (org)

- **Shared agent context** — this repo. Installed on Daniel's machine for Grok, Claude, and Cursor (`install.sh`: user-level rule `alwaysApply` + skill). Prabu installed 2026-08-21 into `~/.claude`/`~/.grok`. Issue #1 confirmed.
- **GitHub Code Security** — enabled on every Zero-State-LLC repository. New-repo org defaults still off (CLI lacks `admin:org`).
- **Partner in-game Admin** — GitHub org admin granted. Locked Admin mailbox `prabu.openclaw@gmail.com` live (`Noema#448`). Inhabit is a separate agent via CONNECT. RFC-0120.
- **GitHub admin bypass** — Partner Agents / both org admins may `gh pr merge --admin` on protected `main`. Required reviews + code owners remain.

## Product work

- **Noema** — PLAY `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`. Worker `ff6210bc`. Semantic Evolution, Deep Time persist, WATCH map, cycle-regen, maint-evolve CLI, harness policy visibility all on `main`. No open PRs. **Worker CI red** on reconstruction `gatherEvidence` (since #481).
- **noema-client** — **0.1.14** on PyPI and `v0.1.14`. LOOK Semantic/Deep Time fields; play/policy/ENTER retry. Still `scrimshawlife-ctrl/noema-client` (not org-transferred). No open PRs.
- **Noema-Specs** — WATCH mapping `#235` merged. No open PRs.
- **Zero-State website** — sitemap+robots `#41` and CI permission `#38` merged. No open PRs.
