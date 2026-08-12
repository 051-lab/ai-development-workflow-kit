# Deliberate Path — Builder Handoff

Execute the scoped repository task below. The repository is the durable source of truth. Read `docs/ai/PROJECT.md`, `docs/ai/STATE.md`, and relevant decisions before editing.

## EVIDENCE RULES

- When verified repository/Git/remote/CI/test evidence conflicts with the handoff or stale STATE content, verified evidence wins.
- Report the mismatch explicitly.
- Stop if the mismatch materially changes scope or safety, and do not continue blindly.
- Do not rewrite STATE.md merely to silence the mismatch; correct it during a bounded state/work update when it reflects a genuine change.
- Do not create a STATE-only commit merely to chase metadata changed by the previous STATE commit. A STATE-only commit may be appropriate at a meaningful project or handoff boundary when it records stable truth that remains true after the commit.

## GOAL
State the concrete outcome the implementation must achieve.

## CURRENT STATE
Summarize the verified repository state relevant to this task and identify the branch/worktree context when applicable.

## SCOPE
List the files, components, or behaviors that may be changed. Treat work outside this scope as excluded unless required to satisfy acceptance criteria safely.

## CONSTRAINTS
List behavior that must not change, compatibility requirements, architectural decisions, dependency restrictions, or other non-negotiable boundaries.

## ACCEPTANCE CRITERIA
List observable conditions that must be true for the work to be considered complete.

## VERIFICATION
List the exact tests, builds, checks, or manual validation that must be run. Add focused verification when the implementation reveals a relevant edge case.

## RETURN
When finished, return:
- files changed
- tests/checks run and their results
- problems encountered
- decisions made during implementation
- remaining risks or unverified assumptions
- recommended next action
- confirmation that `docs/ai/STATE.md` was updated
- confirmation that the Next Action recorded is exactly one atomic, independently verifiable operation

If verified evidence conflicts with this handoff or stale STATE content, do not silently choose one. For routine stale documentation, report the mismatch, continue when scope, constraints, acceptance criteria, architecture, and safety are unchanged, and correct durable state during an appropriate bounded update. Stop at a safe point and escalate when the conflict materially affects scope, constraints, acceptance criteria, architecture, safety, destructive-operation requirements, or a meaningful decision requiring human/planner approval.
