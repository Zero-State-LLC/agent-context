# Handoff

Updated: 2026-08-30 by Prabu (Claude Opus 5) — Noema LCA-2 audit; 2 PRs open, Gate B blocked on a human click

## Now (2026-08-30 — Noema audit: runtime green, Gate B blocked on approval)

Audited Noema runtime + specs end to end. **Everything mechanical is green. The only blocker is a person.**

Live: Worker `87938f7a-ed2c-4984-a4f2-d432ef7b0013` (deployed 2026-08-28), `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`, ACTIVE, settlement HEALTHY, **cycle 6938**, players 0.

Verified locally: Worker suite **222 files / 1590 tests pass**, typecheck clean. Specs `validate_all` / `validate_direction` / `validate_freshness` / `validate_gateb_traceability` all pass. **Noema CI on `main` is green — the `gatherEvidence` red noted in older handoffs is fixed** (#595/#596).

Campaign is **LCA-2 / Gate B**. Gate A promoted and accepted (Specs #300). Gates C–F unproven.

### Gate B is blocked on one human action

Danny's agent has generated **six** device-enrollment codes; every one expired unapproved. The window is **600 seconds**, so an agent minting a code and a human approving asynchronously will essentially never coincide. **This is a process design mismatch, not bad luck.** Fix the window or add an out-of-band approval path before the next attempt, then agree a live window with Danny.

Gate B also needs **three independently controlled external Controllers**, not one. The isolated cohort is deliberately `NOT_COMPUTABLE` and can never promote the gate.

### Three things I did

1. **`Noema-Specs#310`** (open, CI green, mergeable) — `current-state.v1.yaml` recorded live Worker `01ebc196` while live has been `87938f7a` since 2026-08-28; it missed two deployments (#593, #599) and carried a false present-tense `pin_note`. **Both validators were ineffective in opposite ways:** `validate_freshness` fetched `/version` but only asserted the field was non-empty, never comparing it to the pin — so the 6-hourly Direction Freshness drift monitor stayed green while the pin was wrong; `validate_direction` hardcoded the literal string `01ebc196-...` as a required marker, so *correcting* the file would have failed validation. Fixed the pin, added `live_source_commit`, and replaced both checks with invariants that cannot rot. Three negative tests included to prove they now bite.
2. **`scrimshawlife-ctrl/noema-client#32`** (open, CI green, cross-fork) — bump to **0.1.20**. Tag `v0.1.19` is `6b2c054` (#28); #29/#30/#31 landed after it with no bump, so **repo `0.1.19` and PyPI `0.1.19` are different builds under one string**. Since #31 routes the version into protocol envelopes, user agent, and **evidence receipts**, a Gate B run today would record `client_version` ambiguously.
3. **`Noema#600`** — ran the E2E that CI structurally cannot run and posted the evidence.

### What not to redo

- **Don't re-run the Noema audit.** Runtime, CI, and specs validation are green as of 2026-08-30; findings are filed.
- **Don't re-review `Noema#600` on the old rationale.** My three earlier comment-only reviews held on "the genuine official-client acceptance run remains unclaimed" and on dependencies that had already merged. I ran it: `tests/test_gate_b_cohort_local_e2e.py` self-skips unless you supply an official client checkout, so CI's "90 passed, 1 skipped" excluded the only real integration test. With a checkout it is **91 passed, 0 skipped**, passing at both client `main` and the proposed 0.1.20. That objection is closed. Still wants a human read of the credential/isolation paths in `cohort.py`.
- **Don't trust the client version string** until 0.1.20 is published. Installing the checkout reports `0.1.19` — the same string PyPI serves for a *different, pre-#29* build.
- **Don't move the successor pins.** `production_successor_runtime` / `advanced_worker_runtime` still pin `61234cc` while live runs `0b902c28` — **22 commits later**, and `61234cc` is an ancestor of it. Production has advanced past the recorded successor candidate. Those are promotion evidence cross-checked against the Gate A `proof_state`; re-deriving needs a new evidence packet. Left as `OPEN RECONCILIATION` in the file — **owner-sequenced.**

### Next

1. **Owner: approve enrollments** (needs an authenticated human principal — agents cannot). Coordinate a live window with Danny. Fix the 600s window first.
2. **Owner: tag + publish `v0.1.20`** after #32 — `publish.yml` fires on `release: published`, so the PR alone does not ship it.
3. Review/merge `Noema-Specs#310` and `Noema#600`.
4. Housekeeping: `Noema-Specs#291` is stale (pins `d86352b2`, two deploys behind); `#302` is stacked on already-merged `#301` and needs retargeting to `main`.
5. Pre-existing, out of scope: `test_validate_all.MarkdownLinkValidationTests` fails on clean Specs `main`. `validation/run.sh` runs the unittests but `spec-validation.yml` does not — worth checking whether the validator regressed and is silently missing broken links.

Open queues: **Noema** #600 (+ issue #590 Gate B). **Noema-Specs** #291, #302, #310 (+ issue #290). **noema-client** #32. **Zero-State website** empty.

## Repos

| Thing | Where |
|---|---|
| Worker + harness + maint-evolve | `Zero-State-LLC/Noema` (`workers/noema`, `src/noema/harness`, `ops/maint_evolve`) |
| Specs | `Zero-State-LLC/Noema-Specs` |
| Official client | `scrimshawlife-ctrl/noema-client` — **not** org-transferred; contribute by fork + cross-fork PR |
| Website | `Zero-State-LLC/Zero-State` |
| This baton | `Zero-State-LLC/agent-context` |

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

Protected `main` keeps 1 review + code owners. Partner Agents / org admins may `gh pr merge --admin`. Prefer a partner review when both are around. Don't merge your own PRs.

## Start here

```bash
git -C ~/agent-context pull --ff-only
```

Then `STATUS.md`. For Noema code, use `graft ask` before grep (`AGENTS.md` / `.cursor/rules/graft.mdc`). Do not treat Grok/Claude session logs as source of truth.

---

# Handoff

Updated: 2026-08-27 by Daniel (Grok) — #111 merged; STAGING soak pack on main

## Now (2026-08-27)

- Formal STAGING live (postgres-outbox). D-022 + D-007 shipped.
- **#111 merged** — STAGING soak evidence 85/85 at `docs/readiness/evidence/staging-soak-2026-08-27/`
- **Next 5 (readiness):** (1 done soak pack) → owner a11y sign-off → SAFETY approved copy → D-021/023/024 → privacy purge/export
- Native held. Not PRODUCTION.

## Next

1. Owner UI_CONFORMANCE sign-off (focus/reflow/SR) + live screenshots
2. SAFETY `approved` copy checklist on STAGING
3. D-021/023/024 SLO–RTO (owner) or keep SCALE NOT_COMPUTABLE
4. Privacy purge/export for 365d retention
5. Not native / not PRODUCTION
