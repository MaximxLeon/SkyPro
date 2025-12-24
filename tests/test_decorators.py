import pathlib

import pytest

from src.decorators import log


@log()
def add(a: int, b: int) -> int:
    return a + b


@log()
def divide(a: int, b: int) -> float:
    return a / b


def test_add_success(capsys: pytest.CaptureFixture[str]) -> None:
    result = add(2, 3)
    assert result == 5
    captured = capsys.readouterr()
    assert "add ok" in captured.out


def test_divide_success(capsys: pytest.CaptureFixture[str]) -> None:
    result = divide(10, 2)
    assert result == 5
    captured = capsys.readouterr()
    assert "divide ok" in captured.out


def test_divide_error(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError" in captured.out


def test_file_logging(tmp_path: pathlib.Path) -> None:
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def multiply(a: int, b: int) -> int:
        return a * b

    multiply(3, 4)
    content = log_file.read_text()
    assert "multiply ok" in content
