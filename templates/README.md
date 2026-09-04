# Product-repo agent templates

This directory is the **canonical** copy-pack for multi-agent collab in a
Zero State product repo. Source of truth: `Zero-State-LLC/agent-context`.

This pack stays generic. No product secrets, no live world IDs, no deploy
runbooks. Do not dump another repo's Worker deploy or pin workflows here.

## What you get

| File | Role in the product repo |
|---|---|
| [`intent.md.template`](intent.md.template) | Stage-0 proto-spec. Before specify. |
| [`sdlc/README.md`](sdlc/README.md) | Zero State SDLC order (intent → specify → plan → tasks → implement → REVIEW → land). |
| [`AGENTS.md.template`](AGENTS.md.template) | Short router. Canonical contract. |
| [`CLAUDE.md.template`](CLAUDE.md.template) | Thin adapter. Claude reads this and follows `AGENTS.md`. |
| [`AGENT-GOTCHAS.md.template`](AGENT-GOTCHAS.md.template) | Long environment notes. Not the contract. |
| [`spec-Workflows-section.md.template`](spec-Workflows-section.md.template) | `## Workflows` lock for `spec.md`. |

Codex and Cursor already read `AGENTS.md`. If a harness still wants its own
file, copy the same one-liner as `CLAUDE.md` (for example `CODEX.md`).

## Apply to a product repo

From a clone of this pack:

```bash
SRC=~/agent-context/templates
DEST=/path/to/product-repo

cp "$SRC/AGENTS.md.template" "$DEST/AGENTS.md"
cp "$SRC/CLAUDE.md.template" "$DEST/CLAUDE.md"
cp "$SRC/AGENT-GOTCHAS.md.template" "$DEST/AGENT-GOTCHAS.md"
```

Then in the product repo:

1. Create `intent/` or `docs/intent/`. One committed intent file per change
   stream, copied from [`intent.md.template`](intent.md.template). Do not
   invent product intents in this pack — only the blank.
2. Replace `{{PLACEHOLDERS}}` in `AGENTS.md` with this product's identity,
   real commands, and two or three invariants. Leave the **Intent** and
   **Escalation** headings in place.
3. Leave `CLAUDE.md` as the thin adapter. Do not paste the contract into it.
4. Move every long environment note out of `AGENTS.md` into
   `AGENT-GOTCHAS.md`. Delete empty example rows.
5. Append [`spec-Workflows-section.md.template`](spec-Workflows-section.md.template)
   to `spec.md` (or the repo's spec entry file). Keep the default skills.
   Add one owner specialist only if that skill already exists. Name Actions
   this repo already runs or will add; do not invent bots.
6. Read [`sdlc/README.md`](sdlc/README.md) before specifying or implementing.
7. Optional size check:

   ```bash
   cp ~/agent-context/scripts/check-agents-md.sh "$DEST/scripts/"
   "$DEST/scripts/check-agents-md.sh" "$DEST/AGENTS.md"
   ```

The check fails if `AGENTS.md` is missing, larger than 12 KB, or has no
`## Escalation` heading.

## Rules that stay locked

- `intent.md` is SDLC stage-0. Specify next. Do not skip to code.
- One `AGENTS.md` contract. Thin Claude/Codex adapters only. Both say:
  read the active intent before editing; if a non-trivial change has no
  intent, draft it and wait for human accept.
- Procedural `AGENTS.md`. Gotchas live next door.
- Workflows live in the spec, not in a second agent-fleet doc.
- FORGE owns plan/tasks. Cloud agents implement. Human yes on deploy,
  spend, and legal.
- If CI or tests look wrong, open a labeled defect. Do not patch tests to green.
- No agent fleets. ECC catalog-only: name existing skills, do not invent them.
