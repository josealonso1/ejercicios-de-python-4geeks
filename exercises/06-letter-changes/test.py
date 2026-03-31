import runpy
from pathlib import Path
from unittest.mock import patch


def _run(value):
    with patch("builtins.input", return_value=value), patch("builtins.print") as mocked_print:
        runpy.run_path(Path(__file__).with_name("app.py"), run_name="__main__")
    return mocked_print


def test_transforms_hello_3():
    mocked_print = _run("hello*3")
    mocked_print.assert_called_once_with("ifmmp*3")


def test_transforms_fun_times():
    mocked_print = _run("fun times!")
    mocked_print.assert_called_once_with("gvO Ujnft!")


def test_handles_z_wraparound():
    mocked_print = _run("abc xyz")
    mocked_print.assert_called_once_with("bcd yzA")
