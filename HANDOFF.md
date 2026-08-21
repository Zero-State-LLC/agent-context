# Handoff

Updated: 2026-08-21 by Prabu (`prabu-openclaw`)

## Now

PLAY is **EWM_ENHANCED** on `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`. Worker **`5c796d6e`**. Civic Exchange public scar 0.5. `/watch/map` live. No force reseed.

Official client **0.1.13** is on PyPI (`pip install noema-client==0.1.13`). GitHub release [v0.1.13](https://github.com/scrimshawlife-ctrl/noema-client/releases/tag/v0.1.13). Hosted pin `official_client` updated.

`agent-context` installed on Prabu's machine (symlinked into `~/.claude`, `~/.grok`). Commented on issue #1.

Prabu ENTER via `/connect` completed — device-flow enrolled, entered world.perihelion-reach-3 as Player (`player.devicedda6be5c9f55`), ran a traced session (LOOK/INSPECT/MOVE/WAIT/MESSAGE/TRADE/ORG_CREATE/CONTEST_DECLARE/AGREEMENT_FORM + bounded `play()` loop), and **completed the P0 dual-agent MESSAGE** to `player.reach-maint3` ("Message delivered to reach-maint3."). Did **not** attempt `/admin/login` with the locked `prabu.openclaw@gmail.com` mailbox — correctly kept Admin and Player separate per the "Do not" below.

Findings routed properly this time: Buzz #general post was a heads-up only. Per `DECISIONS.md` ("findings update Specs remaining-work and product PRs, not session logs"), filed:
- `Zero-State-LLC/Noema-Specs#236` — marks `REMAINING-WORK-2026-08-21-worker-pin.md` P0 done, adds the two issues below
- `scrimshawlife-ctrl/noema-client#17` — root-caused: `cli.py::cmd_act` silently swallows a `NOT_IN_WORLD` re-observe failure (the in-world session expires independently of the JWT), producing misleading `"<ACTION> is not advertised"` errors instead of surfacing the real re-entry-needed state. Confirmed fix in-process: re-running `ENTER_WORLD` recovers immediately.
- `Zero-State-LLC/Noema#476` — `ClientPolicy` gates `ORG_CREATE`/`CONTEST_DECLARE`/`AGREEMENT_FORM` client-side with no `doctor`/`status` signal, even though the server advertises them.

## Findings from Prabu's E2E pass (2026-08-21)

- Default `noema play` adapter (`FirstValidAffordanceAdapter`) always fires the first-listed affordance. In Civic Exchange that's `WAIT` every turn — 15/15 turns were `WAIT`, world `sequence` stopped advancing after `attention` hit its cap (8). Likely explains low-quality idle bots seen on Buzz (e.g. reach-maint3). No issue filed yet — flagging as P2 in the Specs doc, not urgent.
- Full raw trace (20+ traced actions): `state/noema-full-run-log.json` on Prabu's machine — not committed here (session log, not team-status).

## Next packet

Danny/Grok: triage `noema-client#17` and `Noema#476`. P0 is done; nothing else blocking on Prabu's side.

## Do not

- Reseed `genesis.ef578f4ffceeccd0` or PLAY `world-01`
- `force:true` on production
- Same-id activate on `world.perihelion-reach-2`
- Treat Admin JWT as a Player token
- Put image/reputation on public WATCH
- Rewrite the canonical ledger from reconstruction
- Replace lightweight `/watch` theater
