# Handoff

Updated: 2026-08-30 by Prabu (Claude Opus 5) — Noema LCA-2 audit; 5 PRs merged + RFC-0129 Accepted; #600 security finding; Gate B waits on owner deploy + release + approvals

## Now (2026-08-30 — Noema audited; everything mechanical is green)

Live: Worker `87938f7a-ed2c-4984-a4f2-d432ef7b0013` (deployed 2026-08-28), `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`, ACTIVE, settlement HEALTHY, **cycle 6938**, players 0.

Verified: Worker suite **222 files / 1590 tests**, typecheck clean. All four Specs validators pass. **Noema CI on `main` is green — the old `gatherEvidence` red is fixed** (#595/#596). Campaign is **LCA-2 / Gate B**; Gate A promoted (Specs #300); Gates C–F unproven.

### Merged this pass (Danny reviewed + squashed all three)

1. **`Noema#601`** — **the approval window.** Six Gate B enrollments had expired unapproved at 600s. Specs never pinned the value (`AUTH-AND-IDENTITY` / `SECURITY-SEQUENCES` require `expires_in` + `interval`, no numbers), so CODE_FIXABLE, no spec change. There were **two independent 600s**: `DEVICE_TTL_MS` set the real expiry while the response returned a hardcoded `expires_in: 600`. The client derives its poll deadline from `expires_in` (600 is only its fallback), so raising the TTL alone would have left it giving up at 10 min against a still-valid code. Now **30 min**, with `expires_in`/`interval` derived from the constants and a regression test asserting they stay equal. **Client honors `expires_in`, so no client release is needed for the window.**
2. **`Noema-Specs#310`** — live pin had gone stale across two deploys and both validators reported OK: `validate_freshness` fetched `/version` but never compared it, `validate_direction` hardcoded the stale UUID so *correcting* the file would have failed. Both now check invariants.
3. **`noema-client#32`** — 0.1.20. Tag `v0.1.19` is `6b2c054` (#28); #29/#30/#31 landed after with no bump, so repo and PyPI `0.1.19` were **different builds** under one string.

### Also this pass

- **`Noema#600`** — ran the official-client E2E that CI structurally cannot run (it self-skips without a client checkout, so CI's "90 passed, 1 skipped" excluded the only real integration test). With a checkout: **91 passed, 0 skipped**, at both client `main` and 0.1.20.
  Then did the credential/process-isolation read I had been deferring. Code is genuinely careful (`lstat`+symlink rejection+exact-mode+uid checks, allowlist env, `HOME`/`TMPDIR`/`XDG_CONFIG_HOME` redirected per participant, process-group kill, no `shell=True`, structural redaction). **One finding that matters for Gate B: `PYTHONPATH` is inherited from the orchestrator into all three Controllers, identically, in live mode too** — arbitrary code execution in every Controller via `sitecustomize.py`, which is exactly how this PR's own E2E hooks `decide()` in all three. That is the shared-planner channel the independence contract forbids, and it fails **open**. Suggested: drop `PYTHONPATH`/`VIRTUAL_ENV` from `keep` in live mode, or route via the per-participant `env_from`. Second, minor: `_atomic_json` writes tmp at `0644` before `chmod 0600` (mitigated by the `0700` run dir). **Fix finding 1 before any live Gate B run — it would not show up in the resulting evidence.**
- **`Noema#602`** (open, CI green) — finding 1 fixed. **Stacked on `feat/lca2-isolated-cohort-runner`, not `main`**, because `cohort.py` exists only on Danny's branch and his in-flight work is not mine to push into. Live mode drops `PYTHONPATH`/`VIRTUAL_ENV` and rejects them as `env_from` targets so the channel cannot return under another name; isolated mode untouched so the E2E observer hook still works. New test verified to fail without the fix. 91 cohort tests + official-client E2E pass. Finding 2 (`_atomic_json` 0644 window) deliberately left out as a nit.
- **`Noema-Specs#302` — MERGED, RFC-0129 now `Accepted`.** I retargeted it onto `main` (base #301 had merged) and reconciled it with a second artifact for the same gap (`RFC-PROPOSAL-GC7-...` landed after it was drafted; marked superseded so B7a has one authority). Danny then made both **Decision required** calls and landed the rest himself: optional `victim_id` + `visibility` (`PARTIES`|`PUBLIC`), **no default** (absent means not public, as `AGREEMENT_BROKEN`), co-extensiveness stands. **B7a is now `CLOSED_BY_RFC`.** Catalog stays 32 / Chamber 0.1 stays 24; no producer, verb, Genesis, or 0.3.
- **`Noema-Specs#291`** — still open; recommended closing (it is Danny's, so untouched). Merging it would regress canon: it asserts "Gate A is not complete" and reverts the live pin to `d86352b2`. Its content fails both validators on merged main — the freshness failure is the check #310 repaired.
- **`Noema-Specs#311` — MERGED.** `check_markdown_links` compared resolved link targets against an **unresolved** `ROOT`. Where ROOT holds a symlink (macOS `/var` -> `/private/var`) every target looked outside the tree and the scan silently checked nothing. The louder half: the neighbouring "ignores external/anchor/outside" test asserts `fail` is not called, so on macOS it passed **vacuously**. Fixed by resolving the root once; verified non-vacuous afterwards.

### Gate B: what is actually left

Danny's #601 review says it explicitly: **"This does not open Gate B and does not publish the Worker."** All three remaining steps are owner-sequenced:

1. **Deploy + pin the Worker.** #601 is on `main` but live is still `87938f7a` from 2026-08-28, so the 30-min window is **not in production yet**. Approving enrollments before this deploy just reproduces the 600s failure.
2. **Tag + publish `v0.1.20`.** Merged but not released — PyPI is still `0.1.19`, no `v0.1.20` tag. `publish.yml` fires on `release: published`. Until then treat client version as unpinned in any Gate B evidence.
3. **Approve three independently controlled Controllers.** Needs an authenticated human principal; agents cannot. Isolated cohort is `NOT_COMPUTABLE` by design and can never promote the gate.

### What not to redo

- **Don't re-run the Noema audit** — runtime, CI, and specs validation green as of 2026-08-30.
- **Don't re-review `Noema#600` on the old rationale** — the "unclaimed acceptance run" objection is closed by the E2E above. Still wants a human read of the credential/isolation paths in `cohort.py`.
- **Don't move the successor pins.** `production_successor_runtime` / `advanced_worker_runtime` read `61234cc` while live runs `0b902c28` — **22 commits later**, and `61234cc` is an ancestor. Recorded as `OPEN_RECONCILIATION` in `current-state.v1.yaml`; re-deriving needs a new evidence packet. **Owner-sequenced.**
- **CORRECTION to my earlier note:** I said `spec-validation.yml` does not run the validator unittests. **That was wrong** — it runs them as "Run validator smoke tests"; I had grepped only for the `validate_*.py` invocations and missed the step. Nothing needs adding to CI.
- **Also corrected:** the markdown-link unittest failure was **not** a validator regression. The real-repo scan works (verified by injecting a broken link into `docs/ROADMAP.md` and watching `validate_all` fail, then restoring). It was macOS-only; Linux CI was legitimately green. Fixed in #311.
- **CI gotcha (still true):** `spec-validation` only runs on PRs targeting `main`. A stacked PR never runs it, and retargeting fires `edited`, which is not a default trigger — close/reopen to fire `reopened`. This is why #302 sat five days unvalidated.

Open queues: **Noema** #600, #602 (+ issue #590 Gate B). **Noema-Specs** #311, #291 (+ issue #290). **noema-client** empty. **Zero-State website** empty.

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
