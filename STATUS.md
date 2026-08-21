# Status

Last updated: 2026-08-21 (isolated EWM ENTER/HARVEST proven)

## In flight (org)

- **Shared agent context** — this repo. Daniel's machine is installed. Prabu was notified (GitHub issue, email, Buzz @Prabu/@Galadriel) and still needs to clone and run `install.sh`.
- **GitHub Code Security** — enabled on every Zero-State-LLC repository (code scanning default setup, secret scanning + push protection, Dependabot alerts + security updates). New-repo org defaults are still off (CLI lacks `admin:org`); apply GitHub recommended config in the org UI if we want new repos to inherit this automatically.
- **Partner in-game Admin** — GitHub org admin was already granted. Locked Admin mailbox `prabu.openclaw@gmail.com` is live (`Noema#448`). Inhabit is a separate agent via CONNECT.
- **GitHub admin bypass** — Partner Agents / both org admins may `gh pr merge --admin` on protected `main` without turning reviews off. Required reviews + code owners remain.

## Product work

- **Noema** — Isolated EWM ENTER/HARVEST proven (`#455` / `cfc483b0`). Live PLAY still `dbeb43d198ce81b1` seq 455. Same-id cutover still forbidden.
- **Noema-Specs** — remaining-work `#227` still current for live HARVEST/CONSTRUCT cargo.
