"""App Factory Pipeline Orchestrator."""

import json
import os
import time
from typing import Dict, List, Optional
from app_factory.gates.gate1_architecture import run_gate1
from app_factory.gates.gate2_implementation import run_gate2
from app_factory.gates.gate3_review import run_gate3
from app_factory.gates.gate4_shipping import run_gate4


class PipelineOrchestrator:
    """Manages the 4-Gate Lifecycle for a project directory."""

    def __init__(self, project_dir: str):
        self.project_dir = os.path.abspath(project_dir)
        self.state_file = os.path.join(self.project_dir, ".app-factory-state.json")

    def load_state(self) -> Dict:
        """Load persistent pipeline state."""
        if os.path.isfile(self.state_file):
            try:
                with open(self.state_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {
            "current_gate": 1,
            "gate_history": {},
            "created_at": time.time(),
            "updated_at": time.time(),
        }

    def save_state(self, state: Dict) -> None:
        """Save persistent pipeline state."""
        state["updated_at"] = time.time()
        with open(self.state_file, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)

    def verify_gate(self, gate_num: int, **kwargs) -> Dict:
        """Run verification for a specific gate (1 to 4)."""
        if gate_num == 1:
            passed, errors = run_gate1(self.project_dir)
            name = "Gate 1: Architecture & PRD"
        elif gate_num == 2:
            test_cmd = kwargs.get("test_cmd", "pytest")
            passed, errors = run_gate2(self.project_dir, test_cmd=test_cmd)
            name = "Gate 2: Implementation & TDD"
        elif gate_num == 3:
            passed, errors = run_gate3(self.project_dir)
            name = "Gate 3: Security & Code Review"
        elif gate_num == 4:
            build_cmd = kwargs.get("build_cmd")
            passed, errors = run_gate4(self.project_dir, build_cmd=build_cmd)
            name = "Gate 4: Native Shipping & Compilation"
        else:
            raise ValueError(f"Invalid gate number: {gate_num}")

        return {
            "gate": gate_num,
            "name": name,
            "passed": passed,
            "errors": errors,
            "timestamp": time.time(),
        }

    def run_all_gates(self, **kwargs) -> List[Dict]:
        """Run all 4 gates sequentially until one fails or all pass."""
        results = []
        state = self.load_state()

        for g in range(1, 5):
            res = self.verify_gate(g, **kwargs)
            results.append(res)
            state["gate_history"][str(g)] = {
                "passed": res["passed"],
                "timestamp": res["timestamp"],
            }
            if not res["passed"]:
                state["current_gate"] = g
                self.save_state(state)
                break
        else:
            state["current_gate"] = 4
            state["completed"] = True
            self.save_state(state)

        return results
