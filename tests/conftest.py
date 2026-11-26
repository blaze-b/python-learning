"""Shared pytest fixtures for the learning-repo test suite."""

from __future__ import annotations

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]

# Lesson folders that contain importable `samples/` packages used by unit tests.
SAMPLE_ROOTS = {
    "words": REPO_ROOT / "03_modularity",
    "air_travel": REPO_ROOT / "08_classes",
}


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return REPO_ROOT


@pytest.fixture
def words_path(monkeypatch: pytest.MonkeyPatch) -> Path:
    root = SAMPLE_ROOTS["words"]
    monkeypatch.syspath_prepend(str(root))
    return root


@pytest.fixture
def air_travel_path(monkeypatch: pytest.MonkeyPatch) -> Path:
    root = SAMPLE_ROOTS["air_travel"]
    monkeypatch.syspath_prepend(str(root))
    return root


@pytest.fixture
def sample_text_url(tmp_path: Path) -> str:
    """A file:// URL that urlopen can read without network access."""
    text = (
        "It was the best of times\n"
        "it was the worst of times\n"
        "it was the age of wisdom\n"
    )
    path = tmp_path / "story.txt"
    path.write_text(text, encoding="utf-8")
    return path.as_uri()
