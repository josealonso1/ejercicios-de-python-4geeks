import runpy
from pathlib import Path
from unittest.mock import patch


def _calls():
    with patch("builtins.print") as mocked_print:
        runpy.run_path(Path(__file__).with_name("app.py"), run_name="__main__")
    return mocked_print.call_args_list


def test_prints_100_times():
    assert len(_calls()) == 100


def test_prints_tic_for_multiples_of_3():
    calls = _calls()
    assert calls[2].args[0] == "Tic"
    assert calls[5].args[0] == "Tic"
    assert calls[8].args[0] == "Tic"


def test_prints_toc_for_multiples_of_5():
    calls = _calls()
    assert calls[4].args[0] == "Toc"
    assert calls[9].args[0] == "Toc"


def test_prints_tictoc_for_multiples_of_both():
    calls = _calls()
    assert calls[14].args[0] == "TicToc"
    assert calls[29].args[0] == "TicToc"


def test_prints_numbers_otherwise():
    calls = _calls()
    assert calls[0].args[0] == 1
    assert calls[1].args[0] == 2
    assert calls[3].args[0] == 4
