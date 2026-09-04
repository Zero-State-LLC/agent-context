# Handoff

Updated: 2026-09-04 by Danny (Cursor Grok) — agent-context is now the canonical
template home for product-repo multi-agent collab.

## Now

Danny authorized sealing `templates/` as the copy-pack for product repos.

- `templates/AGENTS.md.template` — short router (identity, commands, invariants,
  graft/docs, **Escalation**, gotchas pointer, shared HANDOFF pack, skills).
- `templates/CLAUDE.md.template` — one-line adapter.
- `templates/AGENT-GOTCHAS.md.template` — environment notes that used to live
  in `AGENTS.md`.
- `templates/spec-Workflows-section.md.template` — Workflows lock (existing
  Grok Bot skills + owner specialist + Actions). Defaults: `anti-slop-code`,
  `production-systems`, `google-developer-style`.
- `scripts/check-agents-md.sh` — fail if `AGENTS.md` is missing, over 12 KB,
  or has no Escalation heading.
- Dated lock in `DECISIONS.md` (2026-09-04 PT).

Root `AGENTS.md` and `README.md` point at `templates/`.

## Next

1. Review and merge the templates PR.
2. Apply the pack to a product repo in a **separate** PR in that repo
   (copy slim `AGENTS.md`, Claude adapter, move gotchas, add Workflows to
   `spec.md`). Do not apply from this session unless asked.
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
