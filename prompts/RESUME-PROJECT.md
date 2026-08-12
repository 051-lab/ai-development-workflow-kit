# Resume Project Prompt

Help me resume this repository without reconstructing old chat history. A human may return days later with only the repository; the goal is to continue safely from repository evidence alone.

Follow this order:

1. Read `docs/ai/PROJECT.md`.
2. Read `docs/ai/STATE.md`.
3. Inspect current repository evidence: `git status`, current branch, recent commits, and CI/test output where available.
4. Determine whether `STATE.md` is current or stale relative to that evidence.
5. Treat verified repository evidence as authoritative and as overriding stale `STATE.md` content whenever they conflict.
6. Report every mismatch you find, with the evidence that supports it.
7. Do NOT create a STATE-only correction commit merely because `STATE.md` describes an operation that repository evidence shows is already complete. Reconcile it during an appropriate bounded state/work update.
8. Identify or resume exactly one bounded Next Action: one coherent outcome with one independently verifiable completion state. Determine its current lifecycle position rather than reducing it to a microscopic command.
9. Identify the safe execution window and furthest authorized boundary where available. Do not invent merge, publish, destructive, or product authorization merely because repository evidence reached a later gate.
10. Decide whether human input is actually required. A human chooses product priorities, architecture, compatibility breaks, consequential tradeoffs, destructive actions, and release scope.
11. Classify the bounded outcome as Fast Path or Deliberate Path, with one-sentence reasoning.

If an external gate is queued/running, an active capable session may recheck it. If this environment cannot remain active or retrieve the result, report `PAUSED AT EXTERNAL GATE`; do not pretend background monitoring continues.

Then tell me:
1. Where the project currently stands and its verified lifecycle position.
2. Whether the working tree is clean or contains intentional/unexplained work.
3. The bounded Next Action, its acceptance, and its execution window.
4. The furthest authorized boundary and what remains outside it.
5. The Fast Path / Deliberate Path classification and reasoning.
6. Any mismatch between repository evidence and state documentation.
7. Whether a human decision is required now.

Keep this operational. Do not redesign the project unless the recorded bounded outcome requires design work.
