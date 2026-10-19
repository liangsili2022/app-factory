"""Tests for CLI and pipeline orchestrator."""

import os
import shutil
import tempfile
import unittest
from app_factory.orchestrator import PipelineOrchestrator


class TestCLI(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_pipeline_orchestrator_initial_state(self):
        orch = PipelineOrchestrator(self.test_dir)
        state = orch.load_state()
        self.assertEqual(state.get("current_gate"), 1)

    def test_pipeline_run_halts_at_gate1_if_empty(self):
        orch = PipelineOrchestrator(self.test_dir)
        results = orch.run_all_gates()
        self.assertEqual(len(results), 1)
        self.assertFalse(results[0]["passed"])
        self.assertEqual(results[0]["gate"], 1)


if __name__ == "__main__":
    unittest.main()
