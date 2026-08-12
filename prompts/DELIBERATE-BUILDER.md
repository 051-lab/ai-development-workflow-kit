# Deliberate Path — Builder Handoff

Execute the scoped repository task below. The repository is the durable source of truth. Read `docs/ai/PROJECT.md`, `docs/ai/STATE.md`, and relevant decisions before editing.

## EVIDENCE RULES

- When verified repository/Git/remote/CI/test evidence conflicts with the handoff or stale STATE content, verified evidence wins.
- Report the mismatch explicitly.
- Stop if the mismatch materially changes scope or safety, and do not continue blindly.
- Do not rewrite STATE.md merely to silence the mismatch; correct it during a bounded state/work update when it reflects a genuine change.
- For routine stale documentation, report the mismatch and continue when it materially affects neither scope nor safety.
- STATE preserves conclusions and load-bearing evidence; investigation history belongs in Git, PR discussions, test output, CI logs, or durable references.
- A queued/running external gate is not failure. If the environment cannot remain active or retrieve its result, return `PAUSED AT EXTERNAL GATE` truthfully.

## GOAL
State the one bounded outcome the implementation must achieve.

## CURRENT STATE
Summarize the verified repository state, current lifecycle gate, and branch/worktree context relevant to this task.

## SCOPE
List the files, components, behaviors, and exclusions that may be changed. Treat work outside this scope as excluded unless required to satisfy acceptance criteria safely.

## CONSTRAINTS
List behavior that must not change, compatibility requirements, architectural decisions, dependency restrictions, and non-negotiable safety boundaries.

## ACCEPTANCE CRITERIA
List observable conditions that must be true for the bounded outcome to be complete.

## EXECUTION WINDOW
State the approved goal, scope, constraints, acceptance, verification, and furthest authorized lifecycle boundary. Proceed through routine gates inside this execution window without returning to the human merely because an intermediate safe step succeeded. Never exceed the boundary.

## STOP CONDITIONS
List task-specific stops in addition to the global rules: material scope expansion, unresolved architecture or human product decision, acceptance conflict, security/data-safety concern, unexpected divergence or merge conflict, failed required validation, credential exposure, destructive operation, or evidence contradicting the approved plan. Do not bypass failed validation.

## VERIFICATION
List the exact tests, builds, checks, CI observation, diff review, and evidence needed. Continue when queued/running is an observable external state; otherwise return `PAUSED AT EXTERNAL GATE` rather than claiming background monitoring.

## RETURN
When finished, return:
- outcome
- files changed
- verification
- lifecycle boundary reached
- problems encountered
- stop conditions encountered, if any
- decisions made inside delegated authority
- remaining risks
- durable-state update performed, if appropriate
- recommended next human decision or next bounded outcome

When verified evidence conflicts with this handoff or stale STATE content, do not silently choose one. For routine stale documentation, report the mismatch, continue when scope, constraints, acceptance criteria, architecture, and safety are unchanged, and correct durable state during an appropriate bounded update. Stop at a safe point and escalate when the conflict materially affects scope, constraints, acceptance criteria, architecture, safety, destructive-operation requirements, or a meaningful decision requiring human/planner approval.
