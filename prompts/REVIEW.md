# Independent Review Prompt

Review the completed change using verified repository evidence rather than the builder's narrative alone.

Read `docs/ai/PROJECT.md`, `docs/ai/STATE.md`, relevant entries in `docs/ai/DECISIONS.md`, the requested acceptance criteria, the actual diff, and available Git, remote, CI, test, and build evidence.

Evaluate:
1. Whether the implementation satisfies the requested bounded outcome and acceptance criteria.
2. Whether it violates any recorded constraint or decision.
3. Whether verification is sufficient and actually supports the completion claim.
4. Whether there are regressions, edge cases, unsafe assumptions, unnecessary complexity, unrelated changes, or silently expanded scope.
5. Whether `STATE.md` is accurate relative to verified Git/remote/CI/test evidence and preserves conclusions plus load-bearing evidence without becoming an incident transcript.
6. Whether stale STATE claims were reported and reconciled appropriately rather than treated as authoritative.
7. Whether the recorded Next Action is exactly one bounded outcome with one independently verifiable completion state, while allowing multiple safe steps and routine lifecycle transitions.
8. Whether the execution window was complied with: scope stayed bounded, the furthest authorized lifecycle boundary was respected, and no unauthorized publish/merge/destructive behavior occurred.
9. Whether STOP-CONDITION COMPLIANCE was correct: did the builder continue past something that should have stopped, or stop unnecessarily at a routine safe gate?
10. Whether external queued/running gates were represented honestly without implying unavailable background monitoring.
11. Whether destructive/history-changing actions remain explicitly protected and human product/architecture decisions remain human.

Verified repository/Git/remote/CI/test evidence overrides stale STATE claims. A routine stale-state mismatch should be reported but does not automatically require `FIX REQUIRED` when implementation and safety remain correct. A material conflict may justify `FIX REQUIRED`. Do not invent failures unsupported by repository evidence.

## EXECUTION-WINDOW COMPLIANCE

- Did the builder stay inside the approved goal, scope, constraints, and acceptance?
- Did it stay inside the furthest authorized lifecycle boundary?
- Did it perform unauthorized publish, merge, branch deletion, force push, history rewrite, or other destructive behavior?

## STOP-CONDITION COMPLIANCE

- Did the builder continue past a global or task-specific stop condition?
- Did it stop unnecessarily when the next routine gate was already authorized and evidence supported continuation?

Return one verdict: `PASS`, `PASS WITH FOLLOW-UP`, or `FIX REQUIRED`.

For every issue, cite the exact file/behavior/evidence involved and state the smallest useful corrective action. Do not turn independent review into implementation, planning, or workflow management.
