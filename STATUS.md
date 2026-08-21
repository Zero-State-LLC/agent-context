# Status

Last updated: 2026-08-21 (PR queues drained: Noema #479 merged, #478/#18 closed, Zero-State #38/#41 merged)

## In flight (org)

- **Shared agent context** — this repo. Daniel's and Prabu's machines are both installed (`install.sh` run 2026-08-21, symlinked into `~/.claude`/`~/.grok`). Issue #1 confirmed.
- **GitHub Code Security** — enabled on every Zero-State-LLC repository (code scanning default setup, secret scanning + push protection, Dependabot alerts + security updates). New-repo org defaults are still off (CLI lacks `admin:org`); apply GitHub recommended config in the org UI if we want new repos to inherit this automatically.
- **Partner in-game Admin** — GitHub org admin was already granted. Locked Admin mailbox `prabu.openclaw@gmail.com` is live (`Noema#448`). Inhabit is a separate agent via CONNECT.
- **GitHub admin bypass** — Partner Agents / both org admins may `gh pr merge --admin` on protected `main` without turning reviews off. Required reviews + code owners remain.

## Product work

- **Noema** — PLAY is `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`. Worker `ff6210bc`. Deep Time persist live. Maint-evolve library+CLI on `main`. Harness policy visibility `#479` on `main`. No open PRs. Worker CI red on reconstruction tests (pre-existing). RFC-0122.
- **noema-client** — 0.1.14 on main (LOOK fields, play/policy/ENTER). #18 closed as superseded. Repo still `scrimshawlife-ctrl/noema-client` (not transferred).
- **Noema-Specs** — WATCH mapping `#235` merged. No open PRs.
- **Zero-State website** — sitemap+robots `#41` and CI permission `#38` merged. No open PRs.
