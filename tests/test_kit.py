from pathlib import Path
import os
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates" / "docs" / "ai"
SCRIPTS = ROOT / "scripts"
PROMPTS = ROOT / "prompts"

STATE_FILES = ["PROJECT.md", "STATE.md", "DECISIONS.md", "REFERENCES.md", "INBOX.md"]
PROMPT_FILES = [
    "FAST-PATH.md",
    "DELIBERATE-PLANNER.md",
    "DELIBERATE-BUILDER.md",
    "REVIEW.md",
    "RESUME-PROJECT.md",
    "OPERATOR.md",
]

class KitContractTests(unittest.TestCase):
    def test_required_templates_exist_and_have_no_placeholders(self):
        for name in STATE_FILES:
            path = TEMPLATES / name
            self.assertTrue(path.exists(), name)
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("TBD", text)
            self.assertNotIn("TODO", text)
            self.assertGreater(len(text.strip()), 120)

    def test_state_template_contains_next_action_and_verification(self):
        text = (TEMPLATES / "STATE.md").read_text(encoding="utf-8")
        self.assertIn("Next Action", text)
        self.assertIn("Verification", text)
        self.assertIn("Current Status", text)

    def test_prompt_library_exists(self):
        for name in PROMPT_FILES:
            path = PROMPTS / name
            self.assertTrue(path.exists(), name)
            text = path.read_text(encoding="utf-8")
            self.assertGreater(len(text.strip()), 180)

    def test_fast_path_requires_state_update_and_verification(self):
        text = (PROMPTS / "FAST-PATH.md").read_text(encoding="utf-8")
        self.assertIn("STATE.md", text)
        self.assertIn("verify", text.lower())
        self.assertIn("escalat", text.lower())

    def test_deliberate_handoffs_define_execution_window_and_stops(self):
        planner = (PROMPTS / "DELIBERATE-PLANNER.md").read_text(encoding="utf-8")
        builder = (PROMPTS / "DELIBERATE-BUILDER.md").read_text(encoding="utf-8")
        operator = (PROMPTS / "OPERATOR.md").read_text(encoding="utf-8")
        for term in ["GOAL", "CURRENT STATE", "SCOPE", "CONSTRAINTS", "ACCEPTANCE CRITERIA", "VERIFICATION", "RETURN"]:
            self.assertIn(term, planner)
            self.assertIn(term, builder)
        for term in [
            "routine gates",
            "execution window",
            "lifecycle boundary reached",
            "stop conditions encountered",
            "decisions made inside delegated authority",
            "durable-state update performed",
        ]:
            self.assertIn(term, builder)
        for term in [
            "EXECUTION CONTINUITY",
            "FURTHEST LIFECYCLE BOUNDARY",
            "ROUTINE REVERSIBLE ENVIRONMENT RECOVERY",
            "EXTERNAL GATE HONESTY",
            "human decides",
        ]:
            self.assertIn(term, operator)

    def test_state_template_contains_evidence_authority_wording(self):
        text = (TEMPLATES / "STATE.md").read_text(encoding="utf-8")
        self.assertIn("evidence overrides stale STATE.md claims", text)
        self.assertIn("Report the mismatch", text)
        self.assertIn("Do not create a STATE-only commit merely to chase metadata changed by the previous STATE commit", text)
        self.assertIn("meaningful project or handoff boundary", text)
        self.assertIn("STATE.md must not become a workflow manual", text)

    def test_state_template_defines_bounded_next_action(self):
        text = (TEMPLATES / "STATE.md").read_text(encoding="utf-8")
        for term in [
            "one bounded outcome",
            "one independently verifiable completion state",
            "multiple safe execution steps",
            "BOUNDED EXECUTION WINDOW",
            "furthest authorized lifecycle boundary",
            "G0",
            "G8",
            "STOP CONDITIONS",
            "STATE preserves conclusions and load-bearing evidence",
        ]:
            self.assertIn(term, text)
        self.assertNotIn("one atomic next action", text.lower())

    def test_state_template_preserves_concise_boundary_guidance(self):
        text = (TEMPLATES / "STATE.md").read_text(encoding="utf-8")
        self.assertIn("meaningful project or handoff boundary", text)
        self.assertIn("routine lifecycle steps", text)
        self.assertIn("unrelated goals", text)
        self.assertIn("human", text.lower())

    def test_state_template_contains_fast_and_deliberate_definitions(self):
        text = (TEMPLATES / "STATE.md").read_text(encoding="utf-8")
        self.assertIn("Fast Path = contained, clear, low-risk, easy to verify.", text)
        self.assertIn("Deliberate Path = ambiguous, architectural, risky, cross-cutting, or consequential.", text)

    def test_fast_path_requires_bounded_execution_continuity(self):
        text = (PROMPTS / "FAST-PATH.md").read_text(encoding="utf-8")
        for term in [
            "bounded outcome",
            "execution window",
            "authorized lifecycle boundary",
            "routine lifecycle gates",
            "meaningful boundary",
            "STOP",
            "PAUSED AT EXTERNAL GATE",
        ]:
            self.assertIn(term, text)
        self.assertNotIn("without bundling separate lifecycle operations", text)

    def test_resume_project_evidence_overrides_stale_state(self):
        text = (PROMPTS / "RESUME-PROJECT.md").read_text(encoding="utf-8")
        self.assertIn("verified repository evidence as authoritative", text)
        self.assertIn("overriding stale", text)

    def test_resume_project_defines_bounded_resume_and_external_honesty(self):
        text = (PROMPTS / "RESUME-PROJECT.md").read_text(encoding="utf-8")
        for term in [
            "bounded Next Action",
            "current lifecycle position",
            "furthest authorized boundary",
            "human input is actually required",
            "PAUSED AT EXTERNAL GATE",
            "Do NOT create a STATE-only correction commit",
        ]:
            self.assertIn(term, text)
        self.assertNotIn("without bundling separate lifecycle operations", text)

    def test_deliberate_builder_contains_evidence_and_state_discipline(self):
        text = (PROMPTS / "DELIBERATE-BUILDER.md").read_text(encoding="utf-8")
        self.assertIn("EVIDENCE RULES", text)
        self.assertIn("verified evidence wins", text)
        self.assertIn("silence the mismatch", text)
        self.assertIn("routine stale documentation", text)
        self.assertIn("materially affects scope", text)

    def test_operator_prompt_distinguishes_stale_documentation_from_unexpected_state(self):
        text = (PROMPTS / "OPERATOR.md").read_text(encoding="utf-8")
        self.assertIn("Routine stale `STATE.md` documentation", text)
        self.assertIn("does not automatically require STOP", text)
        self.assertIn("unexpected or unexplained state", text)
        self.assertIn("STOP and report", text)

    def test_operator_prompt_exists_and_is_registered(self):
        self.assertIn("OPERATOR.md", PROMPT_FILES)
        path = PROMPTS / "OPERATOR.md"
        self.assertTrue(path.exists(), "OPERATOR.md")
        self.assertGreater(len(path.read_text(encoding="utf-8").strip()), 180)

    def test_operator_prompt_defines_roles_and_is_tool_agnostic(self):
        text = (PROMPTS / "OPERATOR.md").read_text(encoding="utf-8")
        for role in ["HUMAN", "PLANNER / REVIEWER", "OPERATOR"]:
            self.assertIn(role, text)
        self.assertIn("tool-agnostic", text.lower())
        for lockin in ["ChatGPT", "OpenCode", "Codex", "Claude"]:
            self.assertNotIn(lockin, text)

    def test_operator_prompt_describes_bounded_normal_operations(self):
        text = (PROMPTS / "OPERATOR.md").read_text(encoding="utf-8")
        self.assertIn("Bounded Normal Operations", text)
        for cmd in ["git status", "git diff", "git log", "git show", "running tests", "reviewed staging"]:
            self.assertIn(cmd, text)

    def test_operator_prompt_contains_explicit_safety_boundaries(self):
        text = (PROMPTS / "OPERATOR.md").read_text(encoding="utf-8")
        for boundary in [
            "git reset --hard",
            "git clean",
            "force push",
            "branch deletion",
            "global Git configuration",
            "discarding unexplained changes",
        ]:
            self.assertIn(boundary, text)
        self.assertIn("STOP and report", text)

    def test_reference_contains_p0_operating_contract(self):
        text = (ROOT / "reference" / "ai-development-workflow-v1.2.html").read_text(encoding="utf-8")
        text = " ".join(text.split())
        for term in [
            "Evidence hierarchy",
            "Stable STATE discipline",
            "Atomic Next Action",
            "Roles: Human, Planner/Reviewer, Operator",
            "Operator safety boundary",
            "Independent review",
            "Strengthened resume behavior",
            "There is no automatic correction loop",
            "one independently verifiable completion state",
            "STOP and report",
        ]:
            self.assertIn(term, text)

    def test_review_prompt_requires_bounded_outcome_contract(self):
        text = (PROMPTS / "REVIEW.md").read_text(encoding="utf-8")
        for term in [
            "bounded outcome",
            "EXECUTION-WINDOW COMPLIANCE",
            "STOP-CONDITION COMPLIANCE",
            "furthest authorized lifecycle boundary",
            "unauthorized publish/merge/destructive behavior",
            "unnecessarily at a routine safe gate",
            "PASS", "PASS WITH FOLLOW-UP", "FIX REQUIRED",
        ]:
            self.assertIn(term, text)
        self.assertNotIn("exactly one atomic operation", text)

    def test_readme_and_reference_describe_v13_working_contract(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        reference = (ROOT / "reference" / "ai-development-workflow-v1.3.html").read_text(encoding="utf-8")
        for text in [readme, reference]:
            for term in ["Bounded Execution Window", "furthest authorized lifecycle boundary", "G0", "G8", "STOP CONDITIONS"]:
                self.assertIn(term, text)
        self.assertIn("working reference candidate", reference)
        self.assertIn("not a V1.3.0 release", reference)

        texts = [
            (ROOT / "README.md").read_text(encoding="utf-8"),
            (ROOT / "reference" / "ai-development-workflow-v1.2.html").read_text(encoding="utf-8"),
        ]
        for text in texts:
            self.assertIn("git hash-object --path", text)
            self.assertIn("git rev-parse HEAD:", text)
            self.assertIn("git config --global core.autocrlf", text)
            self.assertIn(".gitattributes", text)
            self.assertIn("diagnos", text.lower())
            self.assertIn("git update-index --refresh", text)
        self.assertIn("discarding changes", texts[0])

    def test_global_stop_model_is_owned_by_active_safety_contracts(self):
        operator = (PROMPTS / "OPERATOR.md").read_text(encoding="utf-8")
        builder = (PROMPTS / "DELIBERATE-BUILDER.md").read_text(encoding="utf-8")
        fast = (PROMPTS / "FAST-PATH.md").read_text(encoding="utf-8")
        review = (PROMPTS / "REVIEW.md").read_text(encoding="utf-8")
        for term in [
            "unexplained working-tree",
            "unexpected repository/worktree context",
            "material scope expansion",
            "unresolved architecture",
            "acceptance conflict",
            "security/data-safety",
            "unexpected remote divergence",
            "merge conflict",
            "credential/secret exposure",
            "material evidence contradicting",
        ]:
            self.assertIn(term, operator)
        for term in [
            "git reset --hard", "git clean", "force push", "branch deletion",
            "history rewriting", "global Git configuration",
            "discarding unexplained changes", "destructive broad file deletion",
            "bypassing failed validation",
        ]:
            self.assertIn(term, operator)
        for term in ["failed required validation", "destructive operation", "evidence contradicting the approved plan"]:
            self.assertIn(term, builder)
        self.assertIn("escalate safely to the Deliberate Path", fast)
        self.assertIn("unauthorized publish/merge/destructive behavior", review)

    def test_human_decision_authority_is_not_delegated(self):
        operator = (PROMPTS / "OPERATOR.md").read_text(encoding="utf-8")
        resume = (PROMPTS / "RESUME-PROJECT.md").read_text(encoding="utf-8")
        sample = (ROOT / "examples" / "sample-project" / "docs" / "ai" / "STATE.md").read_text(encoding="utf-8")
        for text in [operator, resume]:
            for term in ["product", "architecture", "compatibility", "destructive", "release scope"]:
                self.assertIn(term, text.lower())
        self.assertIn("human chooses product priorities", resume)
        self.assertIn("human still chooses the next product priority", sample.lower())
        self.assertIn("does not select a feature autonomously", sample.lower())
        self.assertIn("branch deletion", operator)

    def test_lifecycle_authorization_is_a_ceiling_not_a_mandate(self):
        operator = (PROMPTS / "OPERATOR.md").read_text(encoding="utf-8")
        builder = (PROMPTS / "DELIBERATE-BUILDER.md").read_text(encoding="utf-8")
        resume = (PROMPTS / "RESUME-PROJECT.md").read_text(encoding="utf-8")
        for boundary in ["LOCAL IMPLEMENTATION BOUNDARY", "PR BOUNDARY", "MERGED / SYNCHRONIZED MAIN BOUNDARY"]:
            self.assertIn(boundary, operator)
        self.assertIn("Never advance beyond the boundary", operator)
        self.assertIn("only when the current boundary explicitly authorizes them", operator)
        self.assertIn("stop before merge unless merge is authorized", operator)
        self.assertIn("Never exceed the boundary", builder)
        self.assertIn("Do not invent merge, publish, destructive, or product authorization", resume)
        self.assertIn("branch deletion", operator)

    def test_gates_define_continuity_without_eight_handoffs(self):
        texts = [
            (ROOT / "README.md").read_text(encoding="utf-8"),
            (ROOT / "reference" / "ai-development-workflow-v1.3.html").read_text(encoding="utf-8"),
            (PROMPTS / "OPERATOR.md").read_text(encoding="utf-8"),
        ]
        gates = [
            "G0 PREFLIGHT", "G1 UNDERSTAND / SCOPE", "G2 IMPLEMENT", "G3 VERIFY",
            "G4 REVIEW", "G5 PUBLISH", "G6 CI / EXTERNAL VALIDATION",
            "G7 MERGE / SYNCHRONIZE", "G8 DURABLE STATE / HANDOFF",
        ]
        for gate in gates:
            self.assertTrue(any(gate in text for text in texts), gate)
        self.assertIn("Routine progression continues without a human handoff", texts[0])
        self.assertIn("not by itself a human handoff", texts[2])
        self.assertIn("Do not stop merely because one routine lifecycle step completed", texts[2])

    def test_external_gate_honesty_contract(self):
        texts = [
            (PROMPTS / "FAST-PATH.md").read_text(encoding="utf-8"),
            (PROMPTS / "DELIBERATE-BUILDER.md").read_text(encoding="utf-8"),
            (PROMPTS / "OPERATOR.md").read_text(encoding="utf-8"),
            (PROMPTS / "RESUME-PROJECT.md").read_text(encoding="utf-8"),
            (TEMPLATES / "STATE.md").read_text(encoding="utf-8"),
        ]
        for text in texts:
            self.assertIn("PAUSED AT EXTERNAL GATE", text)
        self.assertIn("queued/running", texts[0])
        self.assertIn("active capable session", texts[3])
        self.assertIn("never imply monitoring continues", texts[2])
        self.assertNotIn("background monitoring continues", texts[0])

    def test_routine_environment_recovery_stays_session_only(self):
        operator = (PROMPTS / "OPERATOR.md").read_text(encoding="utf-8")
        for allowed in [
            "already-installed version manager", "already-installed project-required runtime",
            "refresh Git stat metadata", "fetch remote metadata", "session-only correction",
        ]:
            self.assertIn(allowed, operator)
        for forbidden in [
            "installing global tools", "new runtimes", "persistent PATH",
            "shell profiles", "changing dependencies", "global Git configuration",
            "rewriting history",
        ]:
            self.assertIn(forbidden, operator)

    def test_v13_scenarios_are_encoded_by_authoritative_contracts(self):
        fast = (PROMPTS / "FAST-PATH.md").read_text(encoding="utf-8")
        planner = (PROMPTS / "DELIBERATE-PLANNER.md").read_text(encoding="utf-8")
        builder = (PROMPTS / "DELIBERATE-BUILDER.md").read_text(encoding="utf-8")
        operator = (PROMPTS / "OPERATOR.md").read_text(encoding="utf-8")
        resume = (PROMPTS / "RESUME-PROJECT.md").read_text(encoding="utf-8")
        state = (TEMPLATES / "STATE.md").read_text(encoding="utf-8")
        scenarios = {
            "A": [(fast, "routine lifecycle gate"), (fast, "meaningful boundary")],
            "B": [(planner, "MERGED / SYNCHRONIZED MAIN"), (operator, "merge/synchronization only when")],
            "C": [(builder, "failed required validation"), (operator, "bypassing failed validation")],
            "D": [(planner, "material scope expansion"), (operator, "material scope expansion")],
            "E": [(fast, "verified evidence"), (state, "stale STATE.md claims")],
            "F": [(operator, "branch deletion"), (resume, "destructive")],
            "G": [(operator, "session-only correction"), (operator, "already-installed project-required runtime")],
            "H": [(resume, "human chooses product priorities"), (state, "human" )],
        }
        for scenario, requirements in scenarios.items():
            for text, term in requirements:
                self.assertIn(term, text, scenario)

    def test_contracts_preserve_five_file_and_release_compatibility(self):
        self.assertEqual(STATE_FILES, ["PROJECT.md", "STATE.md", "DECISIONS.md", "REFERENCES.md", "INBOX.md"])
        self.assertEqual((ROOT / "VERSION").read_text(encoding="utf-8"), "1.2.0\n")
        self.assertTrue((ROOT / "reference" / "ai-development-workflow-v1.2.html").exists())
        self.assertTrue((ROOT / "reference" / "ai-development-workflow-v1.3.html").exists())
        self.assertIn("preserve", (ROOT / "README.md").read_text(encoding="utf-8").lower())
        self.assertIn("written/preserved counts", (ROOT / "README.md").read_text(encoding="utf-8").lower())

    def test_sample_state_preserves_five_file_operating_contract(self):
        text = (ROOT / "examples" / "sample-project" / "docs" / "ai" / "STATE.md").read_text(encoding="utf-8")
        for heading in [
            "Operating Rules", "Current Status", "Completed Recently", "In Progress",
            "Blockers / Risks", "Verification", "Working Tree Notes", "Next Action", "Updated",
        ]:
            self.assertIn(f"## {heading}", text)
        self.assertIn("Illustrative workflow-state example", text)
        self.assertIn("runnable sample-project source is not included", text)
        self.assertIn("evidence overrides stale STATE.md claims", text)
        self.assertIn("one bounded outcome", text)
        self.assertIn("execution window", text.lower())
        self.assertIn("furthest authorized lifecycle boundary", text)
        self.assertIn("STOP CONDITIONS", text)
        self.assertNotIn("TODO", text)
        self.assertNotIn("TBD", text)

class BashInitializerTests(unittest.TestCase):
    def run_init(self, repo: Path, *extra):
        return subprocess.run(
            ["bash", str(SCRIPTS / "init-ai-workflow.sh"), str(repo), *extra],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

    def test_initializer_reports_write_preserve_and_summary(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "repo"
            repo.mkdir()
            first = self.run_init(repo)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertIn("summary   written: 5", first.stdout)
            self.assertIn("summary   preserved: 0", first.stdout)
            self.assertEqual(first.stdout.count("write     "), 5)
            self.assertTrue(first.stdout.rstrip().splitlines()[-1].startswith("ready     "))

            sentinel = repo / "docs" / "ai" / "STATE.md"
            sentinel.write_text("KEEP-ME\n", encoding="utf-8")
            rerun = self.run_init(repo)
            self.assertEqual(rerun.returncode, 0, rerun.stderr)
            self.assertIn("existing  workflow state detected", rerun.stdout)
            self.assertIn("summary   written: 0", rerun.stdout)
            self.assertIn("summary   preserved: 5", rerun.stdout)
            self.assertIn("--force", rerun.stdout)
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "KEEP-ME\n")

            forced = self.run_init(repo, "--force")
            self.assertEqual(forced.returncode, 0, forced.stderr)
            self.assertIn("force     replacing", forced.stdout)
            self.assertIn("summary   written: 5", forced.stdout)
            self.assertIn("summary   preserved: 0", forced.stdout)
            self.assertNotEqual(sentinel.read_text(encoding="utf-8"), "KEEP-ME\n")


        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "repo"
            repo.mkdir()
            result = self.run_init(repo)
            self.assertEqual(result.returncode, 0, result.stderr)
            for name in STATE_FILES:
                self.assertTrue((repo / "docs" / "ai" / name).exists(), name)

    def test_initializer_preserves_existing_file_without_force(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "repo"
            target = repo / "docs" / "ai"
            target.mkdir(parents=True)
            existing = target / "STATE.md"
            existing.write_text("KEEP-ME\n", encoding="utf-8")
            result = self.run_init(repo)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(existing.read_text(encoding="utf-8"), "KEEP-ME\n")

    def test_initializer_force_overwrites_existing_file(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "repo"
            target = repo / "docs" / "ai"
            target.mkdir(parents=True)
            existing = target / "STATE.md"
            existing.write_text("OLD\n", encoding="utf-8")
            result = self.run_init(repo, "--force")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertNotEqual(existing.read_text(encoding="utf-8"), "OLD\n")

class TmuxLauncherTests(unittest.TestCase):
    def test_launcher_creates_standard_windows(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            repo = tmp / "sample-project"
            repo.mkdir()
            fakebin = tmp / "bin"
            fakebin.mkdir()
            log = tmp / "tmux.log"
            fake_tmux = fakebin / "tmux"
            fake_tmux.write_text(
                "#!/usr/bin/env bash\n"
                "echo \"$*\" >> \"$TMUX_TEST_LOG\"\n"
                "if [[ \"$1\" == \"has-session\" ]]; then exit 1; fi\n"
                "exit 0\n",
                encoding="utf-8",
            )
            fake_tmux.chmod(0o755)
            env = os.environ.copy()
            env["PATH"] = str(fakebin) + os.pathsep + env["PATH"]
            env["TMUX_TEST_LOG"] = str(log)
            result = subprocess.run(
                ["bash", str(SCRIPTS / "start-ai-project.sh"), str(repo)],
                cwd=ROOT,
                env=env,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            calls = log.read_text(encoding="utf-8")
            self.assertIn("new-session", calls)
            for name in ["agent", "test", "git", "logs"]:
                self.assertIn(name, calls)
            self.assertIn("attach-session", calls)

class PowerShellContractTests(unittest.TestCase):
    def test_workspace_launcher_contract(self):
        path = SCRIPTS / "start-ai-project.ps1"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        for term in ["RepositoryPath", "SessionName", "Distribution", "wsl.exe", "wslpath", "start-ai-project.sh", "LASTEXITCODE"]:
            self.assertIn(term, text)
        self.assertNotIn("Invoke-Expression", text)
        self.assertNotIn("bash -c", text)
        for provider in ["Codex", "OpenCode", "Claude"]:
            self.assertNotIn(provider, text)
        for window in ["agent", "test", "git", "logs"]:
            self.assertNotIn(f"-n {window}", text)


    def test_initializer_powershell_contract(self):
        path = SCRIPTS / "init-ai-workflow.ps1"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn("[switch]$Force", text)
        self.assertIn('$written = 0', text)
        self.assertIn('$preserved = 0', text)
        self.assertIn('existing  workflow state detected', text)
        self.assertIn('summary   written:', text)
        self.assertIn('summary   preserved:', text)
        self.assertIn('use -Force only', text)
        self.assertIn('force     replacing', text)
        self.assertIn("PROJECT.md", text)
        self.assertIn("STATE.md", text)
        self.assertNotIn("Invoke-WebRequest", text)
        self.assertNotIn("irm ", text.lower())


class PackageHygieneTests(unittest.TestCase):
    def test_gitignore_excludes_python_cache(self):
        text = (ROOT / ".gitignore").read_text(encoding="utf-8")
        self.assertIn("__pycache__/", text)
        self.assertIn("*.py[cod]", text)

    def test_release_checklist_contract(self):
        path = ROOT / "docs" / "RELEASE-CHECKLIST.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        for term in [".git/", "__pycache__/", "*.pyc", "temporary", "Extract the ZIP", "Regenerate `MANIFEST.txt`", "VERSION"]:
            self.assertIn(term, text)


class FinalReleaseContractTests(unittest.TestCase):
    def test_v12_version_and_reference_alignment(self):
        version = (ROOT / "VERSION").read_text(encoding="utf-8")
        self.assertEqual(version, "1.2.0" + chr(10))
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("AI Development Workflow V1.2", readme)
        self.assertIn("reference/ai-development-workflow-v1.2.html", readme)
        self.assertTrue((ROOT / "reference" / "ai-development-workflow-v1.2.html").exists())
        self.assertFalse((ROOT / "reference" / "ai-development-workflow-v1.1.html").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
