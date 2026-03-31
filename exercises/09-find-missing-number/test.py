import json
import runpy
from pathlib import Path
from unittest.mock import patch


def _run(data):
    with patch("builtins.input", return_value=json.dumps(data)), patch("builtins.print") as mocked_print:
        runpy.run_path(Path(__file__).with_name("app.py"), run_name="__main__")
    return mocked_print


def test_finds_missing_number_6():
    mocked_print = _run([3, 7, 1, 2, 8, 4, 5])
    mocked_print.assert_called_once_with(6)


def test_finds_missing_number_3():
    mocked_print = _run([1, 2, 4, 5, 6])
    mocked_print.assert_called_once_with(3)
