# AI Development Workflow V1.1 Project Kit — Design

## Goal
Turn the approved AI Development Workflow V1.1 into a portable, repository-first starter kit that can be copied into any software project without introducing a service, database, model lock-in, or workflow manager.

## Canonical principles
1. The repository is the durable source of project truth; AI conversations are temporary working surfaces.
2. Use the lightest correct execution path: Fast Path for contained work; Deliberate Path when planning, ambiguity, risk, or review justify separation.
3. ChatGPT + OpenCode is the default daily pair, not a lock-in.
4. Notebook remains the formative-thinking tool; Handy is the shortcut for quick capture and in-session bug descriptions.
5. Project state stays separated into PROJECT.md, STATE.md, DECISIONS.md, REFERENCES.md, and INBOX.md.
6. One tmux session per active project, with agent/test/git/logs windows.
7. Browser tabs are temporary context; durable links belong in REFERENCES.md.
8. No more than two active development projects at once.
9. The human remains the decision-maker instead of the message courier.

## Kit architecture
- `templates/docs/ai/`: canonical project-state templates.
- `prompts/`: reusable Fast Path, Deliberate planning/build, review, and resume prompts.
- `scripts/`: safe initialization and tmux workspace helpers for WSL/Linux plus a PowerShell initializer.
- `examples/`: a filled example showing how the files relate.
- `tests/`: contract and behavior tests for templates and scripts.
- `README.md`: operating instructions and adoption path.

## Safety and portability
- Initializers never overwrite existing state files unless explicitly forced.
- No network calls, package installation, repository mutation beyond requested file creation, or Git commits.
- tmux helper operates only inside the selected repository and creates/attaches a named tmux session.
- Herdr integration is documented, not hard-coded into UI keystrokes. The kit remains usable with or without Herdr.

## Success criteria
A user can unpack the kit, initialize a repository, start the standard tmux layout, open the appropriate prompt, and resume work later from STATE.md without needing prior chat history.
