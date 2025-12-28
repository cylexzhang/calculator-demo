import pytest
from calculator import add, sub, mul, div, CalculatorError


def test_add():
    assert add(1, 2) == 3


def test_sub():
    assert sub(5, 3) == 2


def test_mul():
    assert mul(2, 4) == 8


def test_div():
    assert div(8, 2) == 4


def test_div_by_zero():
    with pytest.raises(CalculatorError):
        div(1, 0)
