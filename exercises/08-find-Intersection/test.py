import json
import runpy
from pathlib import Path
from unittest.mock import patch


def _run(data):
    with patch("builtins.input", return_value=json.dumps(data)), patch("builtins.print") as mocked_print:
        runpy.run_path(Path(__file__).with_name("app.py"), run_name="__main__")
    return mocked_print


def test_finds_intersection():
    mocked_print = _run(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"])
    mocked_print.assert_called_once_with("1,4,13")


def test_returns_false_when_no_intersection():
    mocked_print = _run(["1, 3, 9, 10, 17, 18", "2, 4, 6"])
    mocked_print.assert_called_once_with(False)
