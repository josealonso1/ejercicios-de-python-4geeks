import runpy
from pathlib import Path
from unittest.mock import patch


def _run(value):
    with patch("builtins.input", return_value=value), patch("builtins.print") as mocked_print:
        runpy.run_path(Path(__file__).with_name("app.py"), run_name="__main__")
    return mocked_print


def test_returns_true_for_simple_pair():
    mocked_print = _run("()")
    mocked_print.assert_called_once_with(True)


def test_returns_false_for_mismatch():
    mocked_print = _run("({[)]}")
    mocked_print.assert_called_once_with(False)
