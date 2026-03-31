import json
import runpy
from pathlib import Path
from unittest.mock import patch


def _run(payload):
    with patch("builtins.input", return_value=json.dumps(payload)), patch("builtins.print") as mocked_print:
        runpy.run_path(Path(__file__).with_name("app.py"), run_name="__main__")
    return mocked_print


def test_returns_0_1_for_first_case():
    mocked_print = _run({"nums": [2, 7, 11, 15], "target": 9})
    mocked_print.assert_called_once_with([0, 1])


def test_returns_1_2_for_second_case():
    mocked_print = _run({"nums": [3, 2, 4], "target": 6})
    mocked_print.assert_called_once_with([1, 2])
