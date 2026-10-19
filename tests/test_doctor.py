"""Tests for app_factory.doctor module."""

import unittest
from app_factory.doctor import check_command, run_doctor


class TestDoctor(unittest.TestCase):
    def test_check_python(self):
        ok, desc = check_command("python3", "--version")
        self.assertTrue(ok)
        self.assertIn("Python", desc)

    def test_check_git(self):
        ok, desc = check_command("git", "--version")
        self.assertTrue(ok)
        self.assertIn("git", desc.lower())

    def test_check_nonexistent_command(self):
        ok, desc = check_command("nonexistent_binary_xyz_123")
        self.assertFalse(ok)
        self.assertEqual(desc, "Not found in PATH")

    def test_run_doctor_structure(self):
        report = run_doctor()
        self.assertIn("Core Runtimes", report)
        self.assertIn("AI Agent CLIs", report)
        self.assertIn("Native Compilers & SDKs", report)


if __name__ == "__main__":
    unittest.main()
