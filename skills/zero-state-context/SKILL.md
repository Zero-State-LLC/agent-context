---
name: zero-state-context
description: Load and update Zero State team context so work survives machines, models, and both partners' agents.
---

# Zero State shared context

Team durable knowledge is the git repo at `~/agent-context` (or `$ZERO_STATE_CONTEXT`).

## When to load

Any session that continues org work, partner work, or a prior agent session.

## Safe shared-context workflow

Resolve `${ZERO_STATE_CONTEXT:-$HOME/agent-context}` to the intended repository.
Confirm `git remote -v`, the named branch (`git branch --show-current`), its
upstream (`git rev-parse --abbrev-ref '@{upstream}'`), and the user's allowed
publication scope. Stop if detached, no upstream, wrong remote, or any dirty or
staged changes (`git status --porcelain`); never stash or discard teammates' work.

Before reading or drafting, fetch the confirmed remote and fast-forward only:
`git fetch <confirmed-remote>` then `git merge --ff-only '@{upstream}'`.
Stop on divergence or fetch failure; offline context must be labeled stale.
Require `git rev-parse HEAD` to equal `git rev-parse '@{upstream}'` after
fast-forwarding; stop on unreviewed local-ahead commits so they cannot hitchhike.
Coordinate one local editor per clone; if another editor changes the draft,
repeat content review and obtain fresh authorization.
Record `git rev-parse HEAD` as the baseline. Read HANDOFF.md, STATUS.md, and
DECISIONS.md only as relevant. Reconcile the partner's baton; do not blindly
replace content just because a textual merge would succeed.

Draft only changes needed for the present handoff. HANDOFF.md stays concise,
STATUS.md tracks in-flight work, and DECISIONS.md is append-only for real decisions.
Before committing, fetch again and compare `git rev-parse '@{upstream}'` with the
recorded baseline. If it moved, stop: preserve the draft separately, reconcile
against the new handoff with the operator, and repeat review. No force push.

Stage only the actual named context files, for example
`git add -- HANDOFF.md STATUS.md` (include DECISIONS.md only when edited).
Review `git diff --cached --check`, `git diff --cached --name-only`, and the full
`git diff --cached` for accidental deletion, secrets, tokens, personal data and
raw transcripts. Do not commit until the reviewed file list and content match
scope. If secrets are found, stop and arrange rotation; never publish them.
Commit locally. Publication requires explicit current user authorization for the
confirmed remote and branch; without it report the local commit and do not push.

When authorized, push the explicit destination:
`git push <confirmed-remote> HEAD:refs/heads/<confirmed-branch>`.
On rejection, stop and reconcile; do not force. Read back that exact remote ref
with `git ls-remote <confirmed-remote> refs/heads/<confirmed-branch>` and compare
the returned SHA to `git rev-parse HEAD`. Only an exact match verifies publication;
a newer/different SHA needs reconciliation, not a success claim.

These are operator-resolved placeholders, not literal commands to paste before
confirming repository/remote/branch. No network publication is part of installation.
