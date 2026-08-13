# Project State

> Fast-changing operational truth. Keep this concise enough that a returning human or agent can understand the current state in a few minutes.

## Operating Rules

- Repository/Git/remote/CI/test evidence overrides stale STATE.md claims. Report the mismatch; correct STATE.md during a bounded state/work update.
- STATE preserves conclusions and load-bearing evidence; investigation history belongs primarily in Git history, commits, PR discussions, test output, CI logs, or durable references.
- `## Next Action` records exactly one bounded outcome with one independently verifiable completion state. The outcome may contain multiple safe execution steps and routine lifecycle steps; unrelated goals remain separate.
- A BOUNDED EXECUTION WINDOW makes the approved goal, scope, constraints, acceptance, verification, furthest authorized lifecycle boundary, and applicable STOP CONDITIONS unambiguous.
- Reconcile STATE at a meaningful project or handoff boundary. Durable semantic state — completion, blockers, required human decisions, authorization boundary, and the single Next Action — must remain true at that boundary. Routine forensic evidence such as old SHAs, branches, test counts, CI numbers, timestamps, or exact HEAD details may remain stale until the next meaningful update. Do not create a STATE-only commit merely to chase metadata changed by the previous STATE commit; a meaningful semantic reconciliation is different from metadata chasing.
- Prefer durable facts over self-invalidating details such as exact current HEAD hashes; STATE.md must not become a workflow manual.
- Fast Path = contained, clear, low-risk, easy to verify.
- Deliberate Path = ambiguous, architectural, risky, cross-cutting, or consequential.

## Lifecycle Position
Record the current gate, such as G0 PREFLIGHT, G1 UNDERSTAND / SCOPE, G2 IMPLEMENT, G3 VERIFY, G4 REVIEW, G5 PUBLISH, G6 CI / EXTERNAL VALIDATION, G7 MERGE / SYNCHRONIZE, or G8 DURABLE STATE / HANDOFF.

## Current Status
Record the current milestone or bounded outcome, whether work is clean/in progress/blocked, and the branch or worktree context when relevant.

## Completed Recently
List only recent work that materially affects what happens next.

## In Progress
Record unfinished work, partial changes, active experiments, and anything that must not be mistaken for completed behavior.

## Blockers / Risks
Record known blockers, unresolved failures, uncertain assumptions, or STOP CONDITIONS that could change implementation decisions. A queued external gate is not failure; report `PAUSED AT EXTERNAL GATE` when the environment cannot remain active or retrieve its result.

## Verification
Record concise, load-bearing evidence such as test counts/results, build status, CI result, artifact hash, accepted PR, or no current blocker. Distinguish verified facts from unverified claims.

## Working Tree Notes
Record intentional uncommitted changes or files that must be preserved before switching tasks or agents.

## Next Action
Write exactly one bounded outcome with one independently verifiable completion state. Include concise `Acceptance:`, `Scope:`, and `Path:` details when useful. Multiple safe execution steps and routine lifecycle steps may be included inside the authorized BOUNDED EXECUTION WINDOW; do not bundle unrelated goals, choose product/architecture decisions for the human, or continue beyond the furthest authorized lifecycle boundary.

## Updated
Record the date and, when useful, the agent or human who updated this state.

## Bounded Execution Window
The current window authorizes only the stated goal, scope, constraints, verification, and furthest boundary. Routine progression through G0–G8 may continue without an automatic human handoff when evidence supports it. Stop for global safety rules, task-specific STOP CONDITIONS, material scope expansion, unresolved human decisions, failed required validation, unexpected divergence/conflict, or unauthorized destructive action.
