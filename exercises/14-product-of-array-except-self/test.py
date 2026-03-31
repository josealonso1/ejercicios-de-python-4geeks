import json
import runpy
from pathlib import Path
from unittest.mock import patch


def _run(data):
    with patch("builtins.input", return_value=json.dumps(data)), patch("builtins.print") as mocked_print:
        runpy.run_path(Path(__file__).with_name("app.py"), run_name="__main__")
    return mocked_print


def test_returns_expected_products_for_simple_array():
    mocked_print = _run([1, 2, 3, 4])
    mocked_print.assert_called_once_with([24, 12, 8, 6])


def test_handles_zero_in_array():
    mocked_print = _run([-1, 1, 0, -3, 3])
    mocked_print.assert_called_once_with([0, 0, 9, 0, 0])
