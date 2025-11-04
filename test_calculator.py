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

# Parametryzacja dla sum()
@pytest.mark.parametrize("op1, op2, expected", [
    (3.5, 2.5, 6.0),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_sum_parametrized(op1, op2, expected):
    calc = Calculator(op1, op2)
    assert calc.sum() == expected

# Parametryzacja dla pozostałych metod
@pytest.mark.parametrize("op1, op2, expected", [
    (10, 5, 5),
    (-3, -2, -1),
    (0, 7, -7)
])
def test_subtract_parametrized(op1, op2, expected):
    calc = Calculator(op1, op2)
    assert calc.subtract() == expected

@pytest.mark.parametrize("op1, op2, expected", [
    (10, 5, 50),
    (-3, 2, -6),
    (0, 7, 0)
])
def test_multiply_parametrized(op1, op2, expected):
    calc = Calculator(op1, op2)
    assert calc.multiply() == expected

@pytest.mark.parametrize("op1, op2, expected", [
    (10, 5, 2),
    (-6, 3, -2),
    (7.5, 2.5, 3)
])
def test_divide_parametrized(op1, op2, expected):
    calc = Calculator(op1, op2)
    assert calc.divide() == expected