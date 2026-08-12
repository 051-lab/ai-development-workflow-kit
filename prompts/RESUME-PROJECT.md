# Resume Project Prompt

Help me resume this repository without reconstructing old chat history. A human may return days later with only the repository; the goal is to continue safely from repository evidence alone.

Follow this order:

1. Read `docs/ai/PROJECT.md`.
2. Read `docs/ai/STATE.md`.
3. Inspect current repository evidence: `git status`, current branch, recent commits, and CI/test output where available.
4. Determine whether `STATE.md` is current or stale relative to that evidence.
5. Treat verified repository evidence as authoritative and as overriding stale `STATE.md` content whenever they conflict.
6. Report every mismatch you find, with the evidence that supports it.
7. Do NOT create a STATE-only correction commit merely because `STATE.md` describes an operation that repository evidence shows is already complete. Mismatches are reported; correction happens during an appropriate bounded state/work update.
8. Identify exactly ONE atomic Next Action: one operation/outcome with one independently verifiable completion state, without bundling separate lifecycle operations with "and".
9. Classify that action as Fast Path or Deliberate Path, with one-sentence reasoning.

Then tell me:
1. Where the project currently stands.
2. Whether the working tree is clean or contains intentional/unexplained work.
3. The single atomic Next Action identified.
4. The Fast Path / Deliberate Path classification and reasoning.
5. Any mismatch between repository evidence and the state documentation that must be corrected before continuing.

Keep this operational. Do not redesign the project unless the recorded Next Action requires design work.
