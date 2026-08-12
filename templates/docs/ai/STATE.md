# Project State

> Fast-changing operational truth. Keep this concise enough that a returning human or agent can understand the current state in a few minutes.

## Operating Rules

- Repository/Git/remote/CI/test evidence overrides stale STATE.md claims. Report the mismatch; correct STATE.md during a bounded state/work update.
- Next Action is exactly one atomic, independently verifiable operation.
- Do not create a STATE-only commit merely to chase metadata changed by the previous STATE commit. A STATE-only commit may be appropriate at a meaningful project or handoff boundary when it records stable truth that remains true after the commit.
- Prefer durable facts over self-invalidating details such as exact current HEAD hashes; STATE.md must not become a workflow manual.
- Fast Path = contained, clear, low-risk, easy to verify.
- Deliberate Path = ambiguous, architectural, risky, cross-cutting, or consequential.

## Current Status
Record the current milestone or task, whether work is clean/in progress/blocked, and the branch or worktree context when relevant.

## Completed Recently
List only recent work that materially affects what happens next.

## In Progress
Record unfinished work, partial changes, active experiments, and anything that must not be mistaken for completed behavior.

## Blockers / Risks
Record known blockers, unresolved failures, uncertain assumptions, or risks that could change implementation decisions.

## Verification
Record the latest commands/checks run and their results. Distinguish verified facts from unverified claims.

## Working Tree Notes
Record intentional uncommitted changes or files that must be preserved before switching tasks or agents.

## Next Action
Write exactly one atomic next action: one operation/outcome with one independently verifiable completion state. Do not bundle separate lifecycle operations with "and". If more work remains, leave it in planning context, Blockers / Risks, or INBOX, and choose it only after the current action is verified.

## Updated
Record the date and, when useful, the agent or human who updated this state.
