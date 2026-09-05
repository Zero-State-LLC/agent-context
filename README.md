# Zero State — shared agent context

Durable team knowledge for every agent, model, and machine that Daniel (`scrimshawlife-ctrl`) and Prabu (`prabu-openclaw`) run.

This repo is the **team** layer. Personal notes, raw chat logs, and secrets stay on each person's machine.

| File | Role |
|---|---|
| [TEAM.md](TEAM.md) | Who we are |
| [STATUS.md](STATUS.md) | What is in flight across the org |
| [DECISIONS.md](DECISIONS.md) | Dated decisions that should survive a new session |
| [CONVENTIONS.md](CONVENTIONS.md) | How to write and load this context |
| [HANDOFF.md](HANDOFF.md) | Latest cross-agent / cross-person handoff |
| [AGENTS.md](AGENTS.md) | Contract any agent must follow in this repo |
| [templates/](templates/) | Canonical copy-pack: `intent.md` (SDLC stage-0), slim `AGENTS.md`, Claude adapter, gotchas, spec Workflows |

Code structure still lives in each product repo (`AGENTS.md` + `graft/`). Do not copy code maps here.

This repo is also the **canonical template home** for multi-agent collab setup.
Copy from [`templates/`](templates/) into a product repo. Do not dump product
deploy-worker or pin workflows into this pack.

## Install (each person, each machine)

```bash
gh repo clone Zero-State-LLC/agent-context ~/agent-context
~/agent-context/install.sh
```

Follow the [safe shared-context workflow](skills/zero-state-context/SKILL.md) before reading or drafting. Publication is separately authorized, reviewed, and verified; installation does not grant push authority.

`install.sh` only **symlinks** the shared rule and skill into your local Hermes / Grok / Claude / Cursor dirs (`alwaysApply` on the Cursor `.mdc`). It does not copy personal memory.

Cursor Cloud VMs do not inherit `~/.cursor`. Clone this repo (or `gh repo clone Zero-State-LLC/agent-context ~/agent-context`) and read `HANDOFF.md` at session start.

## Hermes only

With Bash available, run `bash install.sh --hermes-only --dry-run` from the
reviewed checkout, inspect the destination, then `bash install.sh --hermes-only`.
The skill is linked at `${HERMES_HOME:-$HOME/.hermes}/skills/zero-state-context`.
Keep the clone at its installed path; restart Hermes and load
`skill_view(name="zero-state-context")`, checking its returned skill_dir.
Existing unrelated destinations are refused, not overwritten. To migrate,
review the old link/package and move it outside discovery before reinstalling.
`--dry-run` works for the multi-host default too and writes nothing.

## What stays private

- `~/.grok/memory/`, Claude/Cursor/OpenClaw session logs
- Preferences, unfinished rabbit holes
- Tokens, keys, `.env`, anything that could authenticate

Skill source selection, migration and safe checks: [SKILL_PROVENANCE.md](SKILL_PROVENANCE.md).
