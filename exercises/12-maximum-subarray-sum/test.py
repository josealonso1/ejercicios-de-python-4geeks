import json
import runpy
from pathlib import Path
from unittest.mock import patch


def _run(data):
    with patch("builtins.input", return_value=json.dumps(data)), patch("builtins.print") as mocked_print:
        runpy.run_path(Path(__file__).with_name("app.py"), run_name="__main__")
    return mocked_print


def test_returns_6_for_example_array():
    mocked_print = _run([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    mocked_print.assert_called_once_with(6)


def test_returns_23_for_second_array():
    mocked_print = _run([5, 4, -1, 7, 8])
    mocked_print.assert_called_once_with(23)
