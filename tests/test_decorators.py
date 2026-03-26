import pytest

from src.decorators import log


def test_log(capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def some_text() -> str:
        return "Какой то текст"

    @log()
    def some_err() -> float:
        return 1000 / 0

    @log()
    def some_err2(i_in: int, i_in2: int) -> float:
        return i_in / 0

    some_text()
    captured = capsys.readouterr()
    assert captured.out == "some_text Ок\n"
    some_err()
    captured = capsys.readouterr()
    assert captured.out == "some_err error:division by zero . Inputs:() {}\n"
    some_err2(1001, 1)
    captured = capsys.readouterr()
    assert captured.out == "some_err2 error:division by zero . Inputs:(1001, 1) {}\n"
