import runpy
from pathlib import Path
from unittest.mock import patch


def test_prints_once():
    with patch("builtins.print") as mocked_print:
        runpy.run_path(Path(__file__).with_name("app.py"), run_name="__main__")
    assert mocked_print.call_count == 1


def test_prints_233168():
    with patch("builtins.print") as mocked_print:
        runpy.run_path(Path(__file__).with_name("app.py"), run_name="__main__")
    mocked_print.assert_called_once_with(233168)
