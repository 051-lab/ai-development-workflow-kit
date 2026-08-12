# Independent Review Prompt

Review the completed change using verified repository evidence rather than the builder's narrative alone.

Read `docs/ai/PROJECT.md`, `docs/ai/STATE.md`, relevant entries in `docs/ai/DECISIONS.md`, the requested acceptance criteria, the actual diff, and available Git, remote, CI, test, and build evidence.

Evaluate:
1. Whether the implementation satisfies the requested scope and acceptance criteria.
2. Whether it violates any recorded constraint or decision.
3. Whether verification is sufficient and actually supports the completion claim.
4. Whether there are regressions, edge cases, unsafe assumptions, unnecessary complexity, or unrelated changes.
5. Whether `STATE.md` is accurate relative to verified repository/Git/remote/CI/test evidence.
6. Whether stale STATE claims were reported and reconciled appropriately rather than treated as authoritative.
7. Whether the recorded Next Action is exactly one atomic operation with one independently verifiable completion state.
8. Whether STATE discipline avoids recursive metadata-chasing commits.
9. Whether any material scope, safety, acceptance, architecture, or validation conflict was surfaced and escalated rather than hidden.

Verified repository/Git/remote/CI/test evidence overrides stale STATE claims. A routine stale-state mismatch should be reported but does not automatically require `FIX REQUIRED` when implementation and safety remain correct. A material conflict may justify `FIX REQUIRED`. Do not invent failures unsupported by repository evidence.

Return one verdict: `PASS`, `PASS WITH FOLLOW-UP`, or `FIX REQUIRED`.

For every issue, cite the exact file/behavior/evidence involved and state the smallest useful corrective action. Do not turn independent review into implementation, planning, or workflow management.
