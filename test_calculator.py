import pytest
class Calculator:
    def __init__(self, op1: float, op2: float):
        self.__op1 = op1
        self.__op2 = op2

import pytest
from calculator import Calculator
def test_sum():
    calc = Calculator(10, 5)
    assert calc.sum() == 15

def test_subtract():
    calc = Calculator(10, 5)
    assert calc.subtract() == 5

def test_multiply():
    calc = Calculator(10, 5)
    assert calc.multiply() == 50

def test_divide():
    calc = Calculator(10, 5)
    assert calc.divide() == 2

def test_divide_by_zero():
    calc = Calculator(10, 0)
    with pytest.raises(ZeroDivisionError):
        calc.divide()

@pytest.mark.parametrize("op1, op2, expected", [
    (3.5, 2.5, 6.0),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_sum_parametrized(op1, op2, expected):
    calc = Calculator(op1, op2)
    assert calc.sum() == expected
