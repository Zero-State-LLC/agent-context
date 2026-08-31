# Handoff

Updated: 2026-08-30 by Prabu (Claude Opus 5) — Noema LCA-2 audit; 3 PRs merged, Gate B waits on owner deploy + release + approvals

## Now (2026-08-30 — Noema audited; everything mechanical is green)

Live: Worker `87938f7a-ed2c-4984-a4f2-d432ef7b0013` (deployed 2026-08-28), `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`, ACTIVE, settlement HEALTHY, **cycle 6938**, players 0.

Verified: Worker suite **222 files / 1590 tests**, typecheck clean. All four Specs validators pass. **Noema CI on `main` is green — the old `gatherEvidence` red is fixed** (#595/#596). Campaign is **LCA-2 / Gate B**; Gate A promoted (Specs #300); Gates C–F unproven.

### Merged this pass (Danny reviewed + squashed all three)

1. **`Noema#601`** — **the approval window.** Six Gate B enrollments had expired unapproved at 600s. Specs never pinned the value (`AUTH-AND-IDENTITY` / `SECURITY-SEQUENCES` require `expires_in` + `interval`, no numbers), so CODE_FIXABLE, no spec change. There were **two independent 600s**: `DEVICE_TTL_MS` set the real expiry while the response returned a hardcoded `expires_in: 600`. The client derives its poll deadline from `expires_in` (600 is only its fallback), so raising the TTL alone would have left it giving up at 10 min against a still-valid code. Now **30 min**, with `expires_in`/`interval` derived from the constants and a regression test asserting they stay equal. **Client honors `expires_in`, so no client release is needed for the window.**
2. **`Noema-Specs#310`** — live pin had gone stale across two deploys and both validators reported OK: `validate_freshness` fetched `/version` but never compared it, `validate_direction` hardcoded the stale UUID so *correcting* the file would have failed. Both now check invariants.
3. **`noema-client#32`** — 0.1.20. Tag `v0.1.19` is `6b2c054` (#28); #29/#30/#31 landed after with no bump, so repo and PyPI `0.1.19` were **different builds** under one string.

### Also this pass

- **`Noema#600`** — ran the official-client E2E that CI structurally cannot run (it self-skips without a client checkout, so CI's "90 passed, 1 skipped" excluded the only real integration test). With a checkout: **91 passed, 0 skipped**, at both client `main` and 0.1.20. Evidence posted. My three earlier comment-only reviews are superseded.
- **`Noema-Specs#302`** — retargeted to `main` (its base #301 had merged) and **reconciled with a second artifact for the same gap**: `RFC-PROPOSAL-GC7-CRIME-PAYLOAD-VICTIM-RECONCILIATION.md` landed on main after #302 was drafted. B7a lists two exits; that note restates both without choosing, RFC-0129 specifies the first. Note marked superseded so B7a has one authority. Re-verified the defect still exists on main (payload still `additionalProperties: false`, no `victim_id`, no `visibility`). `validate=SUCCESS`. Awaiting Danny's two **Decision required** calls: amend a closed catalog payload at all, and whether `visibility` declares `"default": "PARTIES"`.
- **`Noema-Specs#291`** — recommended closing (it is Danny's, so untouched). Merging it would regress canon: it asserts "Gate A is not complete" and reverts the live pin to `d86352b2`. Its content now fails both validators on merged main — the freshness failure is the check #310 repaired.

### Gate B: what is actually left

Danny's #601 review says it explicitly: **"This does not open Gate B and does not publish the Worker."** All three remaining steps are owner-sequenced:

1. **Deploy + pin the Worker.** #601 is on `main` but live is still `87938f7a` from 2026-08-28, so the 30-min window is **not in production yet**. Approving enrollments before this deploy just reproduces the 600s failure.
2. **Tag + publish `v0.1.20`.** Merged but not released — PyPI is still `0.1.19`, no `v0.1.20` tag. `publish.yml` fires on `release: published`. Until then treat client version as unpinned in any Gate B evidence.
3. **Approve three independently controlled Controllers.** Needs an authenticated human principal; agents cannot. Isolated cohort is `NOT_COMPUTABLE` by design and can never promote the gate.

### What not to redo

- **Don't re-run the Noema audit** — runtime, CI, and specs validation green as of 2026-08-30.
- **Don't re-review `Noema#600` on the old rationale** — the "unclaimed acceptance run" objection is closed by the E2E above. Still wants a human read of the credential/isolation paths in `cohort.py`.
- **Don't move the successor pins.** `production_successor_runtime` / `advanced_worker_runtime` read `61234cc` while live runs `0b902c28` — **22 commits later**, and `61234cc` is an ancestor. Recorded as `OPEN_RECONCILIATION` in `current-state.v1.yaml`; re-deriving needs a new evidence packet. **Owner-sequenced.**
- **Pre-existing, out of scope:** `test_validate_all` markdown-link unittest fails on clean Specs `main`; `validation/run.sh` runs that suite but `spec-validation.yml` does not. Worth checking whether the validator silently stopped detecting broken links.
- **CI gotcha:** `spec-validation` only runs on PRs targeting `main`. A stacked PR never runs it, and retargeting fires `edited`, which is not a default trigger — close/reopen to fire `reopened`.

Open queues: **Noema** #600 (+ issue #590 Gate B). **Noema-Specs** #302, #291 (+ issue #290). **noema-client** empty. **Zero-State website** empty.

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
