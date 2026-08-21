# Status

Last updated: 2026-08-21 (client 0.1.13; PLAY 31e7c436)

## In flight (org)

- **Shared agent context** — this repo. Daniel's machine is installed. Prabu was notified (GitHub issue, email, Buzz @Prabu/@Galadriel) and still needs to clone and run `install.sh`.
- **GitHub Code Security** — enabled on every Zero-State-LLC repository (code scanning default setup, secret scanning + push protection, Dependabot alerts + security updates). New-repo org defaults are still off (CLI lacks `admin:org`); apply GitHub recommended config in the org UI if we want new repos to inherit this automatically.
- **Partner in-game Admin** — GitHub org admin was already granted. Locked Admin mailbox `prabu.openclaw@gmail.com` is live (`Noema#448`). Inhabit is a separate agent via CONNECT.
- **GitHub admin bypass** — Partner Agents / both org admins may `gh pr merge --admin` on protected `main` without turning reviews off. Required reviews + code owners remain.

## Product work

- **Noema** — PLAY is `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`. Worker `31e7c436`. Deep Time + `/watch/map` live. Isolated scar tests pass; live HARVEST×3 did not yet show LOOK scars.
- **noema-client** — 0.1.13 `#16` forwards Semantic/Deep Time LOOK fields.
- **Noema-Specs** — WATCH mapping `#235` merged. Remaining live packet is Prabu ENTER.
