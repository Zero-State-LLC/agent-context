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

Code structure still lives in each product repo (`AGENTS.md` + `graft/`). Do not copy code maps here.

## Install (each person, each machine)

```bash
gh repo clone Zero-State-LLC/agent-context ~/agent-context
~/agent-context/install.sh
```

Then `git pull` in `~/agent-context` at the start of a working day. After a session that changed team status, update the files here and `git push`.

`install.sh` only **symlinks** the shared rule and skill into your local Grok / Claude / Cursor dirs (`alwaysApply` on the Cursor `.mdc`). It does not copy personal memory.

Cursor Cloud VMs do not inherit `~/.cursor`. Clone this repo (or `gh repo clone Zero-State-LLC/agent-context ~/agent-context`) and read `HANDOFF.md` at session start.

## What stays private

- `~/.grok/memory/`, Claude/Cursor/OpenClaw session logs
- Preferences, unfinished rabbit holes
- Tokens, keys, `.env`, anything that could authenticate
