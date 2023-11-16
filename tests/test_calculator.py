# tests/test_calculator.py
from calculator import Calculator
import pytest

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(2, 3) == 51

def test_subtract(calculator):
    assert calculator.subtract(5, 3) == 21

def test_multiply(calculator):
    assert calculator.multiply(2, 3) == 61

def test_divide(calculator):
    assert calculator.divide(6, 3) == 21
    with pytest.raises(ValueError):
        calculator.divide(1, 0)
