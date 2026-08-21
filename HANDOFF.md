# Handoff

Updated: 2026-08-21 by Daniel (`scrimshawlife-ctrl`)

## Now

GitHub **admin bypass** is on for Partner Agents (org admins `scrimshawlife-ctrl` and `prabu-openclaw`). `gh pr merge --admin` works without zeroing review count. Required reviews + code owners stay on for everyone else. Proved on Noema `#449`.

Two-partner inside-play is unblocked. Specs match live.

- GitHub: Prabu (`prabu-openclaw`) **already was** org admin (same as Daniel). Admin on Noema + Noema-Specs. Partner Agents maintainer.
- In-game Admin: locked mailbox `prabu.openclaw@gmail.com` (runtime `#448`, Worker `01893b15-3638-4b65-a5e0-6b599b69649d`). Magic link at `https://noema.guru/admin/login`. **Admin is not a Player.**
- Inhabit: `/connect` + `noema-client` 0.1.12. How-to: [PARTNER-OPERATOR.md](https://github.com/Zero-State-LLC/Noema/blob/main/docs/PARTNER-OPERATOR.md)
- Specs truth: [REMAINING-WORK-2026-08-21.md](https://github.com/Zero-State-LLC/Noema-Specs/blob/main/docs/REMAINING-WORK-2026-08-21.md) (PR `#226`)
- Live PLAY: `world.perihelion-reach-2` / `genesis.dbeb43d198ce81b1`, Civic Exchange. `/ready` 0 players until both agents ENTER.

## Next packet

Both agents ENTER successor, HARVEST/LOOK/MESSAGE, write findings as PRs + remaining-work deltas. Not chat transcripts.

## Prabu still needs

Clone `agent-context`, run `install.sh`, comment on https://github.com/Zero-State-LLC/agent-context/issues/1.

## Do not

- Treat Admin JWT as a Player token
- Reseed `genesis.ef578f4ffceeccd0` or PLAY `world-01`
- Merge stale Noema branches as-is
- Commit `~/.grok/memory` or session files
