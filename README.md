# AI Development Workflow V1.1 — Project Kit

This kit turns the V1.1 workflow into reusable repository files and small local helpers. It intentionally does **not** become a workflow manager. Markdown owns durable state; Git owns code history; your AI tools remain interchangeable.

## What This Kit Establishes

- Repository state lives in `docs/ai/`.
- ChatGPT + OpenCode is the default daily pair, not a lock-in.
- Small contained tasks use the Fast Path.
- Ambiguous, architectural, risky, or cross-cutting tasks use the Deliberate Path.
- Notebook stays the formative-thinking tool.
- Handy shortcuts quick thoughts into `INBOX.md` or the current coding-agent session.
- One tmux session maps to one active project with `agent`, `test`, `git`, and `logs` windows.
- Browser research that matters later is promoted into `REFERENCES.md`.
- Keep no more than two development projects active at once.

## Kit Layout

```text
ai-development-workflow-project-kit-v1.1/
├── README.md
├── VERSION
├── templates/docs/ai/
│   ├── PROJECT.md
│   ├── STATE.md
│   ├── DECISIONS.md
│   ├── REFERENCES.md
│   └── INBOX.md
├── prompts/
│   ├── FAST-PATH.md
│   ├── DELIBERATE-PLANNER.md
│   ├── DELIBERATE-BUILDER.md
│   ├── REVIEW.md
│   └── RESUME-PROJECT.md
├── scripts/
│   ├── init-ai-workflow.sh
│   ├── init-ai-workflow.ps1
│   ├── start-ai-project.sh
│   └── start-ai-project.ps1
├── docs/RELEASE-CHECKLIST.md
├── examples/
└── tests/
```

## 1. Initialize a Repository

### From WSL / Linux

```bash
/path/to/project-kit/scripts/init-ai-workflow.sh /path/to/your/repo
```

Existing `docs/ai/*.md` files are preserved. To intentionally replace them with fresh templates:

```bash
/path/to/project-kit/scripts/init-ai-workflow.sh /path/to/your/repo --force
```

### From PowerShell

```powershell
& "C:\path\to\project-kit\scripts\init-ai-workflow.ps1" "C:\path\to\your\repo"
```

Use `-Force` only when you intentionally want to replace existing V1.1 state files.

On every run, the initializer reports per-file `write` or `preserve` actions, then prints one final `ready` line for the `docs/ai/` directory. Reruns preserve existing files by default and summarize written/preserved counts; use `--force` / `-Force` only for intentional replacement.

### Windows / Git / EOL diagnosis

If a tracked file appears unexpectedly modified on Windows, diagnose before cleanup. Inspect `git status --short`, focused `git diff -- <path>` / `git diff --cached -- <path>`, `git ls-files --eol -- <path>`, and `git check-attr -a -- <path>`. Compare `git hash-object --path=<path> <path>` with `git rev-parse HEAD:<path>`: matching hashes strongly indicate equivalent stored content after applicable clean/EOL handling, but do not authorize discarding changes or changing configuration. `git update-index --refresh` and `git status` are non-destructive follow-up checks. Do not casually change `git config --global core.autocrlf`; global configuration requires explicit authorization. A repository-local `.gitattributes` may be appropriate only when the project chooses a policy based on platforms, generated files, tools, and existing conventions. Preserve unexplained changes and obtain authorization before destructive restoration. See the reference workflow for the fuller playbook.



Start with `PROJECT.md`. Record verified architecture, stack, constraints, supported environments, and authoritative verification commands.

Then update `STATE.md` so it tells a returning human or agent where work stands and gives exactly one Next Action. Add durable decisions and references only when they exist; do not manufacture history just to fill the files.

## 3. Start the Standard tmux Workspace

From WSL/Linux:

```bash
/path/to/project-kit/scripts/start-ai-project.sh /path/to/your/repo
```

This creates or attaches a project-named session with:

```text
agent | test | git | logs
```

### From PowerShell / Windows

```powershell
& ".\scripts\start-ai-project.ps1" "C:\path\to\your\repo"
& ".\scripts\start-ai-project.ps1" "C:\path\to\your\repo" -SessionName "my-project" -Distribution "Ubuntu"
```

This is a thin Windows front-end: PowerShell → WSL → `start-ai-project.sh` → tmux. The Bash launcher remains the single implementation of the `agent`, `test`, `git`, and `logs` workspace; it does not launch an AI provider automatically. WSL and tmux must be available.


### Herdr Boundary

Herdr is compatible with this kit because it is itself a terminal-based agent multiplexer with persistent workspaces/tabs/panes. The kit does not automate Herdr keybindings or force Herdr to own project state. Use Herdr inside the `agent` workspace, or use it as your higher-level terminal workspace while keeping the same repository-state contract. The Markdown files remain authoritative either way.

## 4. Choose the Execution Path

### Fast Path
Use `prompts/FAST-PATH.md` when the next task is contained, clear, low-risk, and easy to verify.

If hidden architecture, ambiguity, repeated failures, or consequential decisions appear, stop and escalate.

### Deliberate Path
Use `prompts/DELIBERATE-PLANNER.md` with ChatGPT for deeper planning. Turn the result into the contract in `prompts/DELIBERATE-BUILDER.md`, then give that scoped handoff to OpenCode, Codex, or the chosen builder.

Use `prompts/REVIEW.md` for independent review based on the actual diff, acceptance criteria, recorded constraints/decisions, verification evidence, and authoritative repository state. It checks stale STATE reconciliation, one atomic Next Action, and stable STATE discipline without inventing unsupported failures.



## 5. Capture Routing

```text
Large / formative idea
Notebook → Qwen transcription → INBOX.md → planning

Quick thought
Handy → INBOX.md

Bug discovered while coding
Handy → current builder session

Durable research discovery
Browser → REFERENCES.md
```

## 6. Shutdown Ritual

Before switching projects:

1. Update `STATE.md`.
2. Record exactly one Next Action.
3. Record the latest verification result.
4. Commit completed work or clearly describe intentional WIP.
5. Promote important browser material into `REFERENCES.md`.
6. Detach the tmux/Herdr workspace.
7. Close the project browser group.

## 7. Resume Ritual

1. Attach the project workspace.
2. Read `PROJECT.md` and `STATE.md`.
3. Check Git status/current branch.
4. Resolve any mismatch between repository evidence and `STATE.md`.
5. Choose Fast Path or Deliberate Path for the recorded Next Action.

See `prompts/RESUME-PROJECT.md` for the full evidence-first resume sequence. Report stale STATE claims, trust verified repository evidence, and correct state only during an appropriate bounded update.

## Pilot Rule

Do not retrofit every repository on day one. Pilot this kit on one actively developed project for several real sessions. Judge it by whether you reopen fewer tabs, copy less between AIs, resume work faster, and trust `STATE.md` enough to avoid rereading old conversations.

## Principle

The workflow becomes lighter without becoming looser. **The human remains the decision-maker instead of the message courier.**
