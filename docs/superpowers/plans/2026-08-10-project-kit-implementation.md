# AI Development Workflow V1.1 Project Kit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a portable V1.1 Project Kit with canonical state templates, reusable prompts, safe initialization helpers, a standard tmux launcher, documentation, examples, and verification tests.

**Architecture:** Static Markdown files define durable project contracts and prompts. Small shell/PowerShell helpers copy those contracts into a target repository and create a predictable tmux workspace; they do not own project state or call AI services.

**Tech Stack:** Markdown, Bash, PowerShell, tmux, Python 3 standard library for test harness only.

## Global Constraints
- Repository state remains split into PROJECT.md, STATE.md, DECISIONS.md, REFERENCES.md, and INBOX.md.
- Initializers do not overwrite existing files unless `--force` / `-Force` is supplied.
- No network calls, package installation, automatic Git commits, or model-specific API requirements.
- tmux layout uses windows named `agent`, `test`, `git`, and `logs`.
- Herdr integration is optional and documented rather than required by scripts.

---

### Task 1: Contract tests and canonical state templates
**Files:** Create `tests/test_kit.py` and `templates/docs/ai/*.md`.
- [ ] Write failing tests for required files, headings, placeholder absence, and V1.1 invariants.
- [ ] Run tests and confirm RED because templates/scripts do not yet exist.
- [ ] Add minimal canonical templates.
- [ ] Run tests and confirm template checks pass.

### Task 2: Safe repository initialization
**Files:** Create `scripts/init-ai-workflow.sh`, `scripts/init-ai-workflow.ps1`.
- [ ] Add tests that initialize into a temporary repository, preserve existing files, and allow explicit force overwrite.
- [ ] Confirm RED.
- [ ] Implement Bash initializer and PowerShell equivalent.
- [ ] Run behavior and static-contract tests.

### Task 3: Standard tmux project workspace
**Files:** Create `scripts/start-ai-project.sh`.
- [ ] Add fake-tmux test verifying session/window commands.
- [ ] Confirm RED.
- [ ] Implement create-or-attach behavior with `agent/test/git/logs` windows.
- [ ] Run tests and `bash -n`.

### Task 4: Prompt library and operating documentation
**Files:** Create prompt Markdown files, `README.md`, and example state files.
- [ ] Add contract checks for prompt names and required instructions.
- [ ] Confirm RED.
- [ ] Add Fast Path, Deliberate Planner, Deliberate Builder, Review, and Resume prompts.
- [ ] Add README with capture routing, Herdr boundary, startup/shutdown ritual, and pilot instructions.
- [ ] Add filled example.
- [ ] Run all tests.

### Task 5: Packaging and final verification
- [ ] Run Python tests.
- [ ] Run Bash syntax checks.
- [ ] Scan for `TODO`, `TBD`, and accidental network/package commands.
- [ ] Create ZIP archive and inventory manifest.
