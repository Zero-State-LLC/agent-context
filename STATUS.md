# Status

Last updated: 2026-08-25 (client bumped to **0.1.19** on PyPI; `noema status`/`doctor` on 0.1.19 now correctly report `credential: expired` instead of silently "healthy" — `#21` detection may be partly fixed upstream, no auto-refresh yet though. Prabu enrolled a fresh device fully unattended — used `POST /v1/play/login/request` to trigger an on-demand magic-link email instead of waiting for one to already be sitting in the inbox — and entered `world.perihelion-reach-3` as new player `player.deviceb491f6710e50` at Civic Exchange, presence-only so Aaron can watch via public WATCH (no play actions beyond one confirming LOOK). See HANDOFF.md top for exact steps. Also flagging unreviewed same-day PRs: `Noema#589/#591/#592/#593`, `Noema-Specs#300-303`.)

## In flight (org)

- **Shared agent context** — this repo. Installed on Daniel's machine for Grok, Claude, and Cursor (`install.sh`: user-level rule `alwaysApply` + skill). Prabu installed 2026-08-21 into `~/.claude`/`~/.grok`. Issue #1 confirmed.
- **GitHub Code Security** — enabled on every Zero-State-LLC repository. New-repo org defaults still off (CLI lacks `admin:org`).
- **Partner in-game Admin** — GitHub org admin granted. Locked Admin mailbox `prabu.openclaw@gmail.com` live (`Noema#448`). Inhabit is a separate agent via CONNECT. RFC-0120.
- **GitHub admin bypass** — Partner Agents / both org admins may `gh pr merge --admin` on protected `main`. Required reviews + code owners remain.

## Product work

- **Noema** — PLAY `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`. Worker `ff6210bc`. Semantic Evolution, Deep Time persist, WATCH map, cycle-regen, maint-evolve CLI, harness policy visibility all on `main`. No open PRs. **Worker CI red** on reconstruction `gatherEvidence` (since #481).
- **noema-client** — PyPI now at **0.1.19** (was 0.1.14; git tags may lag, verify before trusting a version number). LOOK Semantic/Deep Time fields; play/policy/ENTER retry; 0.1.19 status/doctor now detect expired credentials instead of reporting healthy. Still `scrimshawlife-ctrl/noema-client` (not org-transferred). PR queue not checked this pass.
- **Noema-Specs** — WATCH mapping `#235` merged. No open PRs.
- **Zero-State website** — sitemap+robots `#41` and CI permission `#38` merged. No open PRs.
