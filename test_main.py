
"""Unit tests for the command-line interface."""

from unittest.mock import patch

from main import main


def test_confirmed_membership():
    """A confirmed basic membership returns 30."""
    answers = ["BASIC", "NONE", "1", "y"]

    with patch("builtins.input", side_effect=answers):
        result = main()

    assert result == 30


def test_cancelled_membership():
    """A cancelled quotation returns -1."""
    answers = ["BASIC", "NONE", "1", "n"]

    with patch("builtins.input", side_effect=answers):
        result = main()

    assert result == -1


def test_invalid_members():
    """Non-numeric members return -1."""
    answers = ["BASIC", "NONE", "abc"]

    with patch("builtins.input", side_effect=answers):
        result = main()

    assert result == -1


def test_invalid_plan():
    """An unknown plan returns -1."""
    answers = ["GOLD", "NONE", "1"]

    with patch("builtins.input", side_effect=answers):
        result = main()

    assert result == -1
