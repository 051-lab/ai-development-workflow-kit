# Independent Review Prompt

Review the completed change using repository evidence rather than the builder's narrative alone.

Read `docs/ai/PROJECT.md`, `docs/ai/STATE.md`, relevant entries in `docs/ai/DECISIONS.md`, the requested acceptance criteria, the actual diff, and available test/build output.

Evaluate:
1. Whether the implementation satisfies the requested scope and acceptance criteria.
2. Whether it violates any recorded constraint or decision.
3. Whether verification is sufficient and actually supports the completion claim.
4. Whether there are regressions, edge cases, unsafe assumptions, unnecessary complexity, or unrelated changes.
5. Whether `STATE.md` accurately reflects the repository.

Return one verdict: `PASS`, `PASS WITH FOLLOW-UP`, or `FIX REQUIRED`.

For every issue, cite the exact file/behavior/evidence involved and state the smallest useful corrective action. Do not invent failures that are not supported by the code or verification evidence.
