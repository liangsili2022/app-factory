"""Subprocess and AI CLI execution adapter with verifiable exit codes."""

import subprocess
import time
from typing import Dict, List, Optional, Tuple


def execute_shell(
    cmd: List[str],
    workdir: Optional[str] = None,
    env: Optional[Dict[str, str]] = None,
    timeout: int = 300,
) -> Tuple[int, str, str, float]:
    """Execute a command locally, capturing stdout, stderr, exit code and duration."""
    start_time = time.time()
    try:
        proc = subprocess.run(
            cmd,
            cwd=workdir,
            env=env,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        duration = time.time() - start_time
        return proc.returncode, proc.stdout, proc.stderr, duration
    except subprocess.TimeoutExpired as e:
        duration = time.time() - start_time
        stdout = e.stdout.decode() if isinstance(e.stdout, bytes) else (e.stdout or "")
        stderr = e.stderr.decode() if isinstance(e.stderr, bytes) else (e.stderr or "")
        return -1, stdout, stderr + f"\n[TIMEOUT] Command timed out after {timeout}s", duration
    except Exception as e:
        duration = time.time() - start_time
        return -2, "", str(e), duration
