import runpy
from pathlib import Path
from unittest.mock import patch


def _run(value):
    with patch("builtins.input", return_value=value), patch("builtins.print") as mocked_print:
        runpy.run_path(Path(__file__).with_name("app.py"), run_name="__main__")
    return mocked_print


def test_returns_time_for_fun_time():
    mocked_print = _run("fun&!! time")
    mocked_print.assert_called_once_with("time")


def test_returns_love_for_i_love_dogs():
    mocked_print = _run("I love dogs")
    mocked_print.assert_called_once_with("love")


def test_returns_world123_when_present():
    mocked_print = _run("Hello world123 567")
    mocked_print.assert_called_once_with("world123")


def test_returns_abc123_for_abc123_abc():
    mocked_print = _run("abc123 abc")
    mocked_print.assert_called_once_with("abc123")


def test_returns_first_longest_on_tie():
    mocked_print = _run("abc def ghi")
    mocked_print.assert_called_once_with("abc")
