import runpy
from pathlib import Path
from unittest.mock import patch


def _run(value):
    with patch("builtins.input", return_value=value), patch("builtins.print") as mocked_print:
        runpy.run_path(Path(__file__).with_name("app.py"), run_name="__main__")
    return mocked_print


def test_returns_3_for_abcabcbb():
    mocked_print = _run("abcabcbb")
    mocked_print.assert_called_once_with(3)


def test_returns_1_for_bbbbb():
    mocked_print = _run("bbbbb")
    mocked_print.assert_called_once_with(1)
