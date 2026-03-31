import json
import runpy
from pathlib import Path
from unittest.mock import patch


def _run(data):
    with patch("builtins.input", return_value=json.dumps(data)), patch("builtins.print") as mocked_print:
        runpy.run_path(Path(__file__).with_name("app.py"), run_name="__main__")
    return mocked_print


def test_filters_example_list():
    mocked_print = _run(["Ryan", "Kieran", "Mark", "Miguel"])
    mocked_print.assert_called_once_with(["Ryan", "Mark"])


def test_returns_empty_list_for_no_friends():
    mocked_print = _run([])
    mocked_print.assert_called_once_with([])


def test_handles_all_4_letter_names():
    data = ["John", "Paul", "Ringo"]
    mocked_print = _run(data)
    mocked_print.assert_called_once_with([name for name in data if len(name) == 4])
