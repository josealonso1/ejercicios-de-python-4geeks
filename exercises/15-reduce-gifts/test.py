import json
import runpy
from pathlib import Path
from unittest.mock import patch


def _run(payload):
    with patch("builtins.input", return_value=json.dumps(payload)), patch("builtins.print") as mocked_print:
        runpy.run_path(Path(__file__).with_name("app.py"), run_name="__main__")
    return mocked_print


def test_returns_1_for_first_case():
    payload = {"prices": [3, 2, 1, 4, 6, 5], "k": 3, "threshold": 14}
    mocked_print = _run(payload)
    mocked_print.assert_called_once_with(1)


def test_returns_2_for_second_case():
    payload = {"prices": [9, 6, 7, 2, 7, 2], "k": 3, "threshold": 14}
    mocked_print = _run(payload)
    mocked_print.assert_called_once_with(2)


def test_returns_0_when_no_removals_are_needed():
    payload = {"prices": [1, 1, 1, 1], "k": 3, "threshold": 10}
    mocked_print = _run(payload)
    mocked_print.assert_called_once_with(0)
