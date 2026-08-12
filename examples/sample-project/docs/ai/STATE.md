# Project State

> Illustrative workflow-state example: the referenced implementation and test results demonstrate the STATE format; runnable sample-project source is not included in this kit.

## Operating Rules

- Repository/Git/remote/CI/test evidence overrides stale STATE.md claims; report the mismatch and correct STATE.md during a bounded state update.
- STATE preserves conclusions and load-bearing evidence rather than becoming an incident transcript.
- Next Action is exactly one bounded outcome with one independently verifiable completion state; multiple safe execution steps may realize it, but unrelated goals remain separate.
- A BOUNDED EXECUTION WINDOW names the goal, scope, constraints, acceptance, verification, furthest authorized lifecycle boundary, and STOP CONDITIONS.
- Reconcile state at a meaningful project or handoff boundary; do not create metadata-chasing STATE-only commits.
- Fast Path = contained, clear, low-risk, easy to verify.
- Deliberate Path = ambiguous, architectural, risky, cross-cutting, or consequential.

## Lifecycle Position
G8 DURABLE STATE / HANDOFF — illustrative completed boundary.

## Current Status
Baseline project is healthy. No implementation task is active.

## Completed Recently
Initial command and unit tests are complete.

## In Progress
Nothing currently in progress.

## Blockers / Risks
None known. A human still chooses the next product priority; the agent does not select a feature autonomously.

## Verification
`python -m unittest -v` passed on the last development session; no current blocker.

## Working Tree Notes
Working tree was clean when this state was recorded.

## Next Action
Implement the next human-selected product priority as one bounded outcome with one independently verifiable completion state.

Acceptance: The selected outcome passes its authoritative verification.
Scope: The explicitly selected feature and required tests only.
Path: Fast Path if contained; otherwise Deliberate Path with an execution window.

## Updated
2026-08-10 — example state
