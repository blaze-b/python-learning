"""Unit tests for the words sample modules."""

from __future__ import annotations


def test_fetch_words_from_file_url(words_path, sample_text_url):
    from samples.words import fetch_words

    words = fetch_words(sample_text_url)
    assert "best" in words
    assert "worst" in words
    assert words[0] == "It"


def test_print_words(capsys, words_path):
    from samples.words import print_words

    print_words(["alpha", "beta"])
    captured = capsys.readouterr()
    assert captured.out == "alpha\nbeta\n"


def test_words_extract_fetch(words_path, sample_text_url):
    from samples.words_extract import fetch_words

    words = fetch_words(sample_text_url)
    assert len(words) >= 10
    assert "times" in words
