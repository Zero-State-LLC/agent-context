# Status

Last updated: 2026-08-24 (client 0.1.14; `#21` still unfixed but **unblocked for this pass** — Aaron approved a fresh device code live, Prabu re-enrolled `player.device4c57643e2afd` and played a short real session at Civic Exchange on `world.perihelion-reach-3` (INSPECT/LOOK/MOVE; HARVEST correctly blocked, both local nodes near-depleted at ~0.03 stock — real scarcity). Human-approval side done without a browser tool by replicating the web app's magic-link consume call directly via `curl`. See HANDOFF.md top for the exact recovery steps; still a manual workaround each time a token expires, not an `#21` fix.)

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
