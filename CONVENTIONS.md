# Conventions

## Handoffs

`HANDOFF.md` is the current baton, not a log. Overwrite it. Include:

- What changed
- What the next agent should do first
- What not to redo
- Links to PRs / issues / product repos

If history matters, append a dated note to `DECISIONS.md` or the product repo instead.

## Pull before you write

Someone else may have pushed. Follow `skills/zero-state-context/SKILL.md` Safe shared-context workflow: clean-tree checks, confirmed upstream, freshness before and after drafting, reviewed named staging, authorized publication and exact remote read-back. Stop on divergence.

## Size

Keep `HANDOFF.md` and `STATUS.md` short enough to load every session. If a section grows past a screen, it belongs in a product repo.

## Secrets

Never. If a token leaked into a draft, delete it, rotate, and do not commit.
