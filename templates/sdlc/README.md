# Zero State SDLC order

Canonical stage chain for a product repo. Artifacts, not agent fleets.
Copy templates from the parent `templates/` directory. Do not invent
product intents, skills, or bots in this pack.

Anthropic AI-Native SDLC playbook (artifact per stage):

`intent.md` → `spec.md` → `plan.md` → `AGENTS.md` / `CLAUDE.md` → `REVIEW.md`
→ build / maintain.

Danny's spec-kit lock (Zero State order):

1. **intent.md** — proto-spec. Why, done-looks-like, locks, open questions.
   Human accepts before specify.
2. **constitution** — only if the product needs a standing constitution
   change. Skip when the existing constitution already covers the work.
3. **specify** — `spec.md` plus `## Workflows` (existing Grok Bot skills +
   owner specialist + Actions to reuse or add). See
   [`../spec-Workflows-section.md.template`](../spec-Workflows-section.md.template).
4. **plan** — how the spec becomes work. **FORGE owns plan.**
5. **tasks** — sliced work. **FORGE owns tasks.**
6. **implement** — cloud agents execute the accepted plan/tasks. No extra
   bots. Do not stand up an agent fleet.
7. **REVIEW / evidence** — `REVIEW.md` plus whatever evidence the spec
   named. Escalation still applies: if CI or tests look wrong, open a
   labeled defect; do not patch tests to green.
8. **land** — merge. Human yes on deploy, spend, and legal. Agents do not
   dispatch production deploys or buy things.

## Intent files

Keep committed intents in `intent/` or `docs/intent/`.
One intent file per change stream. Name the file after that stream, not
`intent.md` at the repo root, unless the repo has a single active stream.

For a non-trivial change: draft intent, wait for human accept, then
specify. Do not skip to code.

## Ownership

| Stage | Owner |
|---|---|
| intent, specify, REVIEW | humans + implementing agent (draft); human accept |
| plan, tasks | FORGE |
| implement | cloud agents |
| deploy / spend / legal | human yes |

## What this pack does not do

- Invent a product intent
- Invent skills or bots (ECC catalog-only)
- Copy product deploy-worker or pin workflows into `agent-context`
