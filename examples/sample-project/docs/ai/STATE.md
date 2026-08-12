# Project State

> Illustrative workflow-state example: the referenced implementation and test results demonstrate the STATE format; runnable sample-project source is not included in this kit.

## Operating Rules

- Repository/Git/remote/CI/test evidence overrides stale STATE.md claims; report the mismatch and correct STATE.md during a bounded state update.
- Next Action is exactly one atomic, independently verifiable operation.
- Do not create a STATE-only commit merely to chase metadata changed by the previous STATE commit. A STATE-only commit may be appropriate at a meaningful project or handoff boundary when it records stable truth that remains true after the commit.
- Prefer durable facts over self-invalidating details such as exact current HEAD hashes; STATE.md must not become a workflow manual.
- Fast Path = contained, clear, low-risk, easy to verify.
- Deliberate Path = ambiguous, architectural, risky, cross-cutting, or consequential.

## Current Status
Baseline project is healthy. No implementation task is active.

## Completed Recently
Initial command and unit tests are complete.

## In Progress
Nothing currently in progress.

## Blockers / Risks
None known.

## Verification
`python -m unittest -v` passed on the last development session.

## Working Tree Notes
Working tree was clean when this state was recorded.

## Next Action
Implement a `--version` flag in the CLI entry point.

## Updated
2026-08-10 — example state
