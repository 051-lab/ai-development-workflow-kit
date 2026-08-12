# Fast Path — Builder Prompt

Use this when the task is contained, well understood, low-risk, and easy to verify.

Read `docs/ai/PROJECT.md` and `docs/ai/STATE.md` before changing files. Read `docs/ai/DECISIONS.md` when the task could touch an existing architectural or compatibility decision.

Reconcile evidence before changing files: if repository/Git/remote/CI/test evidence conflicts with `STATE.md`, treat verified evidence as authoritative, report the mismatch, and correct `STATE.md` during a bounded state update. Do not create a STATE-only commit merely to chase metadata changed by the previous STATE commit.

For the task I provide:
1. Inspect the relevant code before proposing changes.
2. State a brief in-session plan appropriate to the size of the task.
3. Implement only the requested scope.
4. Run the relevant verification from `PROJECT.md` plus any focused checks needed for the changed behavior.
5. Review the actual diff for unintended changes.
6. Update `docs/ai/STATE.md` with what changed, verification results, unresolved risks, and exactly one atomic Next Action — one operation/outcome with one independently verifiable completion state, without bundling separate lifecycle operations.
7. Report the files changed and verification results concisely.

Escalate instead of improvising if you discover unclear architecture, hidden cross-cutting dependencies, repeated verification failure, a security/data-safety concern, a destructive or history-rewriting operation, or a decision with meaningful long-term consequences. In that case, stop implementation at a safe point, update `STATE.md`, explain why the task now needs the Deliberate Path, and identify the decision that must be made.

Task follows below:
