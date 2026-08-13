# Fast Path — Bounded Execution Prompt

Use this when the task is contained, well understood, low-risk, and easy to verify.

Read `docs/ai/PROJECT.md` and `docs/ai/STATE.md` before changing files. Read `docs/ai/DECISIONS.md` when the task could touch an existing architectural or compatibility decision.

Reconcile evidence before changing files: if repository/Git/remote/CI/test evidence conflicts with `STATE.md`, treat verified evidence as authoritative, report the mismatch, and correct `STATE.md` during a bounded state update. Do not create a STATE-only commit merely to chase metadata changed by the previous STATE commit.
A Fast Path task has one bounded outcome with one independently verifiable completion state. Before editing, make the BOUNDED EXECUTION WINDOW explicit in-session: approved goal, scope, constraints, acceptance criteria, verification, furthest authorized lifecycle boundary, and STOP CONDITIONS. The window may contain multiple safe steps and routine lifecycle gates; it is not unrestricted autonomy.

1. Perform G0 PREFLIGHT and G1 UNDERSTAND / SCOPE using repository evidence.
2. State a brief in-session plan and the bounded outcome.
3. Implement only the approved scope.
4. Run focused verification, then the authoritative project verification.
5. Review the actual diff and evidence.
6. Continue through routine G5 PUBLISH, G6 CI / EXTERNAL VALIDATION, or G7 MERGE / SYNCHRONIZE steps only when the execution window authorizes them and evidence supports continuation. Do not stop merely because one routine lifecycle gate succeeded.
7. Reconcile `docs/ai/STATE.md` once at a meaningful boundary. Record conclusions and load-bearing evidence, not an incident transcript.
8. Return the outcome, verification, lifecycle boundary reached, problems, stop conditions, remaining risks, and the next bounded outcome if work remains.

Stop and report for hidden architecture, material scope expansion, repeated meaningful failure, security/data-safety concerns, or consequential product/architecture choices; escalate safely to the Deliberate Path.

If CI or another external gate is queued/running, it is not failure. Recheck while the capable session remains active; if this environment cannot remain active or retrieve the result, return `PAUSED AT EXTERNAL GATE` rather than implying background monitoring.

9. Identify the project-authoritative runtime/toolchain before authoritative validation. Use an already-installed runtime through session-only recovery when authorized; otherwise label alternate-runtime results supplementary. Exact-head external validation under the required runtime may establish authoritative evidence when locally unavailable. Do not claim required validation passed without qualifying evidence.

10. At G8, leave durable semantic STATE correct: completion, blockers, required human decision, and the single Next Action must match the verified post-boundary position. Routine forensic metadata may remain stale until a meaningful update; do not create recursive metadata-chasing commits.

Task follows below:
