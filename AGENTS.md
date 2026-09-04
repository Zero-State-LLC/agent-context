# Agent contract — Zero State shared context

You are working in the Zero State LLC shared context repo, or you have the `zero-state-context` skill/rule loaded.

## Load

At the start of a session that needs org or partner context (Cursor, Claude, Grok, Codex, OpenClaw — same files):

1. `HANDOFF.md` — latest state another agent or person left
2. `STATUS.md` — what is in flight
3. `DECISIONS.md` — only if the task depends on a prior choice
4. `TEAM.md` — only if you need who-owns-what

If this clone is not the cwd, those files live at `~/agent-context/` (or `$ZERO_STATE_CONTEXT`). Pull `--ff-only` before trusting a local copy.

## Write

Before ending a session that changed team status, decisions, or work another person/agent must continue:

1. Update `HANDOFF.md` (overwrite; keep it current, not a diary)
2. Update `STATUS.md` if in-flight work changed
3. Append to `DECISIONS.md` only for a real decision
4. Commit and push this repo

## Do not

- Put secrets, tokens, or personal preferences here
- Dump raw chat transcripts here
- Duplicate a product repo's `graft/` or code conventions
- Copy product deploy or pin workflows into this pack

## Product-repo templates

Reusable collab files for a product repo live in [`templates/`](templates/).
`intent.md` is SDLC stage-0 (see [`templates/sdlc/README.md`](templates/sdlc/README.md)).
This repo stays team-context only. Apply the pack there; do not grow this
`AGENTS.md` into a product contract. Do not invent product intents here.
