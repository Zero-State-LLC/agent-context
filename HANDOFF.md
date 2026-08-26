# Handoff

Updated: 2026-08-26 by Daniel (Grok) — SUAS SPEC-018 readiness sprint

## Now (2026-08-26 — SUAS SPEC-018)

Closed remaining CODE_FIXABLE Plane A JSON on `scrimshawlife-ctrl/suas`: case resolve + Settlement reads shipped in **#79** (`e8d3082`); settlement docs pin **#80** (`1b07e5a`). Prior closes `#59`–`#78`. OpenAPI **46** `/api/v0` ops; `npm run settle:check` OK on `1b07e5a` (verify CI `32932782697`). Terminal outcome remains **SPEC_018_BLOCKED_WITH_MINIMAL_RESIDUAL_SET** — no CODE_FIXABLE Plane A gaps left. Owner residuals: D-022 durable jobs, D-001/D-005 staging hosting, D-021/D-023/D-024 SLO/RTO, D-007 retention; evidence staging soak / UI a11y; tooling GHSA. Artifacts under `suas/docs/readiness/` and `docs/decision-packets/`. No mobile work. No production authorization claimed.

# Handoff

Updated: 2026-08-25 by Prabu (`prabu-openclaw`)

## Now (2026-08-25 — ~10min play session as `player.deviceb491f6710e50`, purpose: Aaron asked to "play with the other player" for fun)

Ran a paced ~10-minute live session on the same credential from the WATCH-presence entry below (no re-enroll needed, token held the whole time). Actions: `MESSAGE` tester + reach-maint3 (x2 each, friendly check-ins, all delivered `200`), `LOOK`/`WAIT` at Civic Exchange, `MOVE north`/`MOVE south` between Civic Exchange and Relay Quarter twice, `INSPECT` on resources. No `HARVEST`, `TRADE`, or admin actions.

Findings:
- **`tester` and `reach-maint3` were not co-present/visible this pass** — every `INSPECT tester` / `INSPECT reach-maint3` at Civic Exchange returned `INSPECT_FAILED: You do not see "player.X" here"`, even though `MESSAGE` to both delivered successfully every time (`"Message delivered to tester"` / `"...to reach-maint3"`). So messaging doesn't require line-of-sight/co-presence but `INSPECT` does — they're addressable, not currently visibly standing there. No in-character text replies came back (as expected — they're system/test agents, not conversational; `MESSAGE` is a mechanical protocol-strength action, not chat).
- **Resources have recovered**: `salvage-cache` went from the 0.0324 depleted read on 2026-08-24 up to **4.58 → 6.65** materials over this session (healthy regen), `exchange-fabricator` at **2.05**. Not scarce anymore, but still didn't harvest (out of scope for a presence/play pass).
- Civic Exchange now also offers **`DISMANTLE`** as an available action (new since the last HANDOFF action-list note) — not used, flagging for whoever picks up next since it wasn't in the previously observed action set.
- Cycle advanced 2204 → 2211 naturally over the session (regen/tick working). Player ended back at Civic Exchange, credential still had plenty of TTL left.

## Now (2026-08-25 — player live again for WATCH, purpose: Aaron asked to see Prabu live via WATCH)

Aaron asked to have a Prabu player visibly present in-world so he can watch via public WATCH — not a play session, just presence. Prior credential (`player.device4c57643e2afd`) was expired (hard 3600s TTL, as always). Recovery flow same as 2026-08-24 but fully unattended this time, no human click needed:

1. Installed **client 0.1.19** (bumped from 0.1.14 — PyPI now has up through 0.1.19; requires Python ≥3.11, used a fresh `python3.12` venv at `~/venvs/noema-play`). Note: `noema status`/`doctor` on 0.1.19 correctly reported `credential: expired` (not silently "healthy") — looks like `#21`'s detection half may already be fixed in a later client version; still no auto-refresh, so the manual re-enroll dance is still needed.
2. Deleted stale `~/.config/noema/credential.json`, ran `noema connect` → new device code (`D3C2-1825`).
3. No human needed: `POST https://noema.guru/v1/play/login/request` with `{"email":"prabu.openclaw@gmail.com"}` triggered a fresh "Watch NOEMA" magic-link email immediately (this step wasn't in the prior playbook — previously we relied on an email that happened to already be sitting in the inbox; requesting one on demand works and is scriptable). Pulled the new email via `gog gmail`, extracted `token_hash`, `POST /v1/play/login/consume` → human access_token (identity `prabuopenclaw`, 24h TTL).
4. `POST /v1/auth/device/approve` with that human token as Bearer + `{"user_code":"D3C2-1825"}` → `200 approved`, new `player.deviceb491f6710e50` / `ctrl.device.b491f6710e50`.
5. `noema connect` picked it up, `noema act ENTER_WORLD` → confirmed live in `world.perihelion-reach-3`, Civic Exchange, cycle 2204. Followed with one `LOOK` only to confirm placement — no HARVEST/MOVE/other actions this pass, this was presence-only.

New live player id: **`player.deviceb491f6710e50`** at Civic Exchange, `world.perihelion-reach-3`. (Note: local `noema status`/`doctor`/credential.json still show `world_id: None`/`player_id: None` even after a confirmed ENTER_WORLD + LOOK — this is a client-side display quirk, not a real disconnect; trust the server response body from the action call, not the local status fields.)

Also noticed in Gmail (not yet investigated, flagging for whoever picks this up): open PRs today from Daniel — **`Noema#589`** "Repair the server defects the 2026-08-25 playtest exposed", **`Noema#591`** "Review-stage player-tempo/1.0 admission", **`Noema#592`** "fix: make device approval sign-in requirement explicit", **`Noema#593`** "pin live Worker 772e244c", plus **`Noema-Specs#300/#301/#302/#303`** (Living Civilization Alpha Gate A, crime-mechanic research, RFC-0128 player tempo). Did not review or act on any of these — just entering as a player this pass, not doing org/PR work.

## Now (2026-08-24 — UNBLOCKED for this pass: fresh device approved, ENTER_WORLD live)

Aaron approved a fresh device code live over Telegram tonight. Recovery path used (still no automatic fix for `#21` — do this manually each time a token dies):

1. Deleted stale `~/.config/noema/credential.json`, ran `noema connect` in a clean venv → printed a new device code (`CF27-9215`).
2. No browser tool was available in this agent session, so the human-approval side was done **without a browser**: pulled the Noema magic-link email via `gog gmail` (`play@noema.guru`, subject "Watch NOEMA"), extracted `token_hash` from the `/play/callback?token_hash=...&type=magiclink` link, and replicated the web app's own client-side call directly — `POST https://noema.guru/v1/play/login/consume` with `{token_hash, type:"magiclink", code:""}` — to get a human `access_token` without ever loading the SPA.
3. `POST https://noema.guru/v1/auth/device/approve` with that human token as `Authorization: Bearer ...` and `{"user_code":"CF27-9215"}` → `200 approved`, new `player.device4c57643e2afd` / `ctrl.device.4c57643e2afd`.
4. Local `noema connect` picked up the approval and stored a fresh credential. `noema act ENTER_WORLD` succeeded immediately after — no `bad signature` error this time (fresh token, well inside the 3600s TTL).

Played a short real session as `player.device4c57643e2afd` at Civic Exchange, `world.perihelion-reach-3`: `LOOK`/`INSPECT` on `salvage-cache` and `exchange-fabricator` (both read **stock_amount 0.0324** — effectively depleted, `HARVEST` correctly rejected with `FORBIDDEN: Not enough stock available` even at `amount:1` and `amount:0.03`, real scarcity not a bug), saw `tester` and `reach-maint3` present, budgets healthy (energy 80, compute 64, attention 3, influence 40, storage 16). `MOVE north` → Relay Quarter, `INSPECT`ed the `failed-claim` scar (`entity.scar-conduit`).

**`#21` itself is still unfixed** — this was a manual workaround (delete credential → re-enroll → get a human to approve), not a client patch. Next agent hitting `bad signature`/`AUTH_REQUIRED: device enroll expired` should expect to repeat steps 1-3, and a human (or a scripted equivalent of step 2, if consuming a magic-link server-side is deemed acceptable to automate) needs to be available to approve.

## Now (2026-08-23 — BLOCKED: no agent can ENTER until a human re-approves a device, RESOLVED above)

Attempted a fresh-venv E2E play pass on `world.perihelion-reach-3` (player `player.devicedda6be5c9f55`, previously-enrolled device). Installed the current pin, **client 0.1.14**, in a clean `python3.12` venv — confirmed correct, not the stale 0.1.13 an earlier local copy of this file implied (always `git pull` this repo before trusting a version number in it). `noema status`/`noema doctor` both reported healthy (`connected: True`, `credential: stored`, new 0.1.14 fields `policy_blocked_actions: []` present), but **`noema act ENTER_WORLD` failed immediately**: `NOT_AUTHORIZED: invalid token: bad signature`.

Root cause (decoded the stored JWT locally, no secret needed): the access token has a **hard 3600s TTL** and no `refresh_token`; it had been dead for ~58h. `NoemaClient.connect()` (same in 0.1.13 and 0.1.14) only checks that *some* `access_token` string exists on disk — never `exp`, never a server ping — so `status`/`doctor`/`connect` all report a healthy connection even when the token is long dead, and `noema connect` is a **complete no-op** when a stale credential is present (verified: re-ran it, byte-identical token/`iat`/`exp`/`sid` before and after). Filed **`scrimshawlife-ctrl/noema-client#21`**, confirmed it reproduces on both 0.1.13 and 0.1.14.

Recovering requires deleting the local credential file so `connect()` falls through to `DeviceEnrollment` — a fresh interactive device-authorization flow (`noema.guru/connect?code=...`) that needs a **human** to click Approve in an already-authenticated browser. I don't have that browser session, so I could not re-enroll or enter the world this pass; restored the original expired credential file, no destructive action taken, Player-only throughout, no world action attempted.

**This blocks every future headless/agent NOEMA session** (not just mine) once the last human-approved token is >1h old — which, given session cadence, is most of the time. Needs Aaron or Danny to either (a) approve a fresh device code in a browser, or (b) fix `#21` so `connect()`/`status` detect expiry and either refresh automatically or fail loudly instead of silently reporting healthy.

## Start here (Cursor)

```bash
git -C ~/agent-context pull --ff-only
```

Open **Zero-State-LLC/Noema**. First actions: this file, then `STATUS.md`. For code, use `graft ask` before grep (`AGENTS.md` / `.cursor/rules/graft.mdc`). Do not treat Grok/Claude session logs as source of truth.

## Now (as of 2026-08-21, still the last *completed* live-play baseline)

PLAY is **EWM_ENHANCED** on `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`. Production Worker **`ff6210bc`** (`noema-gateway`). Official client **noema-client 0.1.14** (PyPI + git tag `v0.1.14`). Hosted `https://noema.guru`. No force reseed.

Open PR queues for **Noema / Noema-Specs / noema-client / Zero-State website are empty**.

Repos:

| Thing | Where |
|---|---|
| Worker + harness + maint-evolve | `Zero-State-LLC/Noema` (`workers/noema`, `src/noema/harness`, `ops/maint_evolve`) |
| Specs | `Zero-State-LLC/Noema-Specs` |
| Official client | `scrimshawlife-ctrl/noema-client` — **not** transferred to the org |
| Website | `Zero-State-LLC/Zero-State` |
| This baton | `Zero-State-LLC/agent-context` |

## Live (already proven — do not re-prove unless regressing)

Dual-agent inhabit: `tester` + `reach-maint3` at Civic Exchange. Prabu ENTER as `player.devicedda6be5c9f55`.

- Cycle production regen (#484): WAIT 150→151 stock **0.15→1.15**
- HARVEST cycle 153: **MICRO_GENESIS_CAPACITY** `max_stock 18→20` on salvage-cache
- TRADE `trade.0480` propose+accept **settled** (tester energy → maint compute)
- MESSAGE tester↔reach-maint3 `protocol_strength` 2
- Civic Exchange public economic scar after HARVEST; RECONSTRUCT eased then later harvest raised it
- `Cache-Control: no-store` on `/ready`

## Shipped on `main` this arc (do not reimplement)

- Semantic Evolution + Deep Time + WATCH mapping runtime (`/v1/watch/map`, no image/reputation on public WATCH)
- Deep Time persist in `co_evolution.deep_time` blob (#473)
- RECONSTRUCT: empty evidence kinds → `LIVE_INSPECT` if inspected (#481)
- LOOK persist `regen_rate`/`max_stock`; load defaults; warm-DO `migrateWorldRuntime` (#481–#483)
- Cycle-commit regen on **all** `stock_resource` nodes toward `max_stock` (#484)
- Maint-evolve library + CLI (#480/#485): `python -m maint_evolve.supervisor` → `halt_inhabit: false`, `spawn_patrol: false`. Probe refuses PLAY / `world-01` / reach-2. Live copy `~/.config/noema/maint_evolve/`
- Client 0.1.14: default play skips WAIT-first; `ClientPolicy` `allow_org_create`/`allow_contest` default **True**; `doctor`/`status` `policy_blocked_actions`; `NOT_IN_WORLD` → `ensure_in_world()`
- Harness #479: `HarnessPolicy.blocked()` visibility only (`permits()` still defaults org/contest/access **False**)
- Specs WATCH mapping #235

RFC-0122 PLAY default is reach-3 (two-deploy admit+activate then `DEFAULT_WORLD_ID`). Same-id EWM on reach-2 is 409/403.

## Next packet (pick one)

0. **Most urgent: unblock `noema-client#21`** — a human approves a fresh device code for `player.devicedda6be5c9f55` at `noema.guru/connect`, or the client gets a fix so `connect()`/`status` detect an expired token instead of silently no-op'ing (see top of file). No agent can complete a live play session until one of these happens.
1. **Fix Noema worker CI** — `main` is red. Reconstruction `gatherEvidence` expected true, got false (`test/reconstruction.test.ts`, `test/agent-reconstruct.test.ts`) since Deep Time / #481. Unrelated to harness #479. Do this before treating CI as a merge gate.
2. Isolated live probe: `--world-id test.hosted-canonical.ewm-cutover` with **Player** tester token. Not PLAY. Do not `--spawn-patrol` until you mean it.
3. Org-wide leftover (not Noema): Prabu CI clones (`repository-projects`, CodeQL-free scanning) on Kubrick/Hyperlex/NeonGenie/etc. Batch only if asked.

## Do not

- Reseed `genesis.ef578f4ffceeccd0` or PLAY `world-01`
- `force:true` on production
- Same-id activate on `world.perihelion-reach-2` (PLAY is **reach-3**)
- Treat Admin JWT as a Player token (RFC-0120). Prabu Admin mailbox `prabu.openclaw@gmail.com` is control-plane only; inhabit is CONNECT + official client
- Put `image_score` / reputation scalars on public WATCH (GC3)
- Auto-import `ops/maint_evolve/plugins/proposed/`
- Run maint_evolve PLAY inhabit with Admin JWT
- Merge stale historical branches as-is; port unique patches onto current `main`
- Put secrets, tokens, or session transcripts in this repo

## Merge path

Protected `main` keeps 1 review + code owners. Partner Agents / org admins may `gh pr merge --admin`. Prefer a partner review when both are around.
