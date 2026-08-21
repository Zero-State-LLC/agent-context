# Status

Last updated: 2026-08-21 (GitHub admin bypass)

## In flight (org)

- **Shared agent context** — this repo. Daniel's machine is installed. Prabu was notified (GitHub issue, email, Buzz @Prabu/@Galadriel) and still needs to clone and run `install.sh`.
- **GitHub Code Security** — enabled on every Zero-State-LLC repository (code scanning default setup, secret scanning + push protection, Dependabot alerts + security updates). New-repo org defaults are still off (CLI lacks `admin:org`); apply GitHub recommended config in the org UI if we want new repos to inherit this automatically.
- **Partner in-game Admin** — GitHub org admin was already granted. Locked Admin mailbox `prabu.openclaw@gmail.com` is live (`Noema#448`). Inhabit is a separate agent via CONNECT.
- **GitHub admin bypass** — Partner Agents / both org admins may `gh pr merge --admin` on protected `main` without turning reviews off. Required reviews + code owners remain.

## Product work

- **Noema** — Worker `01893b15-3638-4b65-a5e0-6b599b69649d`. Live successor. Partner operator hats documented in `docs/PARTNER-OPERATOR.md`.
- **Noema-Specs** — `docs/REMAINING-WORK-2026-08-21.md` is the live-state snapshot. Next packet: dual-agent inhabit + written reports.
