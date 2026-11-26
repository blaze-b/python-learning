"""Smoke-run every numbered lesson script so they exit cleanly."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]

LESSON_DIRS = [
    "01_fundamentals",
    "02_core",
    "03_modularity",
    "04_objects_types",
    "05_collections",
    "06_exceptions",
    "07_iterations",
    "08_classes",
    "09_io_file",
]

# Scripts that need CLI args when run as a process.
SCRIPT_ARGS: dict[str, list[str]] = {
    "03_modularity/samples/words_extract.py": [
        "http://sixty-north.com/c/t.txt",
    ],
}


def _discover_scripts() -> list[Path]:
    scripts: list[Path] = []
    for folder in LESSON_DIRS:
        root = REPO_ROOT / folder
        # Numbered lesson scripts at the folder root
        scripts.extend(sorted(root.glob("[0-9][0-9]_*.py")))
        # Runnable sample entry points (have __main__ guards / are demos)
        samples = root / "samples"
        if samples.is_dir():
            for name in ("words.py", "words_extract.py", "word.py"):
                candidate = samples / name
                if candidate.exists():
                    scripts.append(candidate)
    return scripts


SCRIPTS = _discover_scripts()


@pytest.mark.parametrize(
    "script",
    SCRIPTS,
    ids=[str(p.relative_to(REPO_ROOT)) for p in SCRIPTS],
)
def test_lesson_script_runs(script: Path, tmp_path: Path) -> None:
    rel = str(script.relative_to(REPO_ROOT))
    args = [sys.executable, str(script), *SCRIPT_ARGS.get(rel, [])]

    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"
    # Ensure non-interactive path for scripts that check isatty()
    env.setdefault("TERM", "dumb")

    result = subprocess.run(
        args,
        cwd=REPO_ROOT,
        env=env,
        capture_output=True,
        text=True,
        timeout=120,
        input="",
        check=False,
    )
    assert result.returncode == 0, (
        f"{rel} failed with exit {result.returncode}\n"
        f"--- stdout ---\n{result.stdout}\n"
        f"--- stderr ---\n{result.stderr}"
    )
