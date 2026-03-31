import runpy
from pathlib import Path
from unittest.mock import patch


def _run(value):
    with patch("builtins.input", return_value=value), patch("builtins.print") as mocked_print:
        runpy.run_path(Path(__file__).with_name("app.py"), run_name="__main__")
    return mocked_print


def test_reverses_coderbyte():
    mocked_print = _run("coderbyte")
    mocked_print.assert_called_once_with("etybredoc")


def test_reverses_i_love_code():
    mocked_print = _run("I Love Code")
    mocked_print.assert_called_once_with("edoC evoL I")
