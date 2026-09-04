# Handoff

Updated: 2026-09-04 by Danny (Cursor Grok) — agent-context is now the canonical
template home for product-repo multi-agent collab.

## Now

Danny authorized sealing `templates/` as the copy-pack for product repos,
then required `intent.md` as SDLC stage-0.

- `templates/intent.md.template` — proto-spec before specify (problem,
  observable done, users/systems, locks/non-goals, open questions,
  `[verified]` / `[assumed]` claims, author/date). Next stage is `spec.md`.
- `templates/sdlc/README.md` — Zero State order: intent → constitution
  (if needed) → specify (`spec.md` + Workflows) → plan → tasks →
  implement (cloud agents) → REVIEW/evidence → land. FORGE owns plan/tasks.
  Human yes on deploy/spend/legal. No extra bots.
- `templates/AGENTS.md.template` — short router plus **Intent** (read
  active intent; if missing on a non-trivial change, draft and wait) and
  **Escalation**.
- `templates/CLAUDE.md.template` — thin adapter: follow `AGENTS.md`; same
  intent gate.
- `templates/AGENT-GOTCHAS.md.template` — environment notes.
- `templates/spec-Workflows-section.md.template` — Workflows lock.
  Defaults: `anti-slop-code`, `production-systems`, `google-developer-style`.
- `scripts/check-agents-md.sh` — fail if `AGENTS.md` is missing, over 12 KB,
  or has no Escalation heading.
- Dated locks in `DECISIONS.md` (2026-09-04 PT): template home + intent
  as stage-0.

Root `AGENTS.md` and `README.md` point at `templates/`. No product intents
were invented — blanks only.

Root `AGENTS.md` and `README.md` point at `templates/`.

## Next

1. Review and merge the templates PR (`agent-context#2`).
2. Apply the pack to a product repo in a **separate** PR in that repo
   (copy slim `AGENTS.md`, Claude adapter, move gotchas, add Workflows to
   `spec.md`, stand up `intent/` or `docs/intent/`). Do not apply from
   this session unless asked. Do not invent product intents here.
3. Product queues (SS reboot, HexWire PRs, Noema Gate B) are unchanged.
   Read `STATUS.md` for those; do not restart those audits.

## Do not

- Dump Noema `deploy-worker-pin-pr` / `pin-currency` (or any product deploy)
  into this repo again. This pack is team-context only.
- Invent skills, bots, or agent fleets. ECC is catalog-only.
- Patch tests to green when CI looks wrong — open a labeled defect.
- Grow this repo's `AGENTS.md` into a product contract.

## Note on `.github/workflows/`

`fc8f292` added Noema-shaped deploy/pin workflows plus generic GitHub
templates to this repo. Left untouched in the templates PR (docs-only).
Remove those product workflows in a follow-up if Danny wants this tree
clean of deploy YAML.
