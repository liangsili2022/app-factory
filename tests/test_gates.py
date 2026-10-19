"""Tests for App Factory 4-Gate verification logic."""

import os
import shutil
import tempfile
import unittest
from app_factory.gates.gate1_architecture import run_gate1
from app_factory.gates.gate2_implementation import run_gate2
from app_factory.gates.gate3_review import run_gate3, scan_for_secrets
from app_factory.gates.gate4_shipping import detect_build_command, run_gate4


class TestGates(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_gate1_missing_files(self):
        passed, errors = run_gate1(self.test_dir)
        self.assertFalse(passed)
        self.assertTrue(any("Missing docs/PRD.md" in e for e in errors))
        self.assertTrue(any("Missing docs/TASKS.md" in e for e in errors))

    def test_gate1_valid_files(self):
        docs_dir = os.path.join(self.test_dir, "docs")
        os.makedirs(docs_dir, exist_ok=True)
        with open(os.path.join(docs_dir, "PRD.md"), "w") as f:
            f.write("# PRD\n## Target User\nDevs\n## Core Value\nSpeed\n## Out of Scope\nNone\n## Acceptance Criteria\nDone")
        with open(os.path.join(docs_dir, "TASKS.md"), "w") as f:
            f.write("# Tasks\n- [ ] Task 1: Initialize")

        passed, errors = run_gate1(self.test_dir)
        self.assertTrue(passed)
        self.assertEqual(len(errors), 0)

    def test_gate3_secret_detection(self):
        leaky_file = os.path.join(self.test_dir, "leaky.py")
        # concatenate to prevent scanner from triggering on test source code
        dummy_secret = "sk-" + "1234567890" * 3
        with open(leaky_file, "w") as f:
            f.write(f"api_key = '{dummy_secret}'")

        findings = scan_for_secrets(self.test_dir)
        self.assertEqual(len(findings), 1)
        self.assertIn("OpenAI/CPA Secret Key found", findings[0])

        passed, errors = run_gate3(self.test_dir)
        self.assertFalse(passed)

    def test_gate4_compiler_detection(self):
        with open(os.path.join(self.test_dir, "pubspec.yaml"), "w") as f:
            f.write("name: test_app\n")
        cmd = detect_build_command(self.test_dir)
        self.assertEqual(cmd, "flutter analyze")

        passed, _ = run_gate4(self.test_dir, build_cmd="python3 -c 'print(1)'")
        self.assertTrue(passed)


if __name__ == "__main__":
    unittest.main()
