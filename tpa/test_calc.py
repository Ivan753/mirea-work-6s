import pytest
from calc import Calc

def test_sum_small():
    a = 0.0000001
    b = 0.00000007

    calc = Calc()

    assert calc.sum(a, b) == a+b


def test_sum_big():
    a = 700987100000
    b = 15700987100666

    calc = Calc()

    assert calc.sum(a, b) == a+b


def test_div_zero():
    calc = Calc()

    with pytest.raises(ZeroDivisionError):
        calc.div(1, 0)


def test_mult_zero():
    a = 15
    b = 0

    calc = Calc()

    assert calc.mult(a, b) == 0


def test_f_lz():
    calc = Calc()

    with pytest.raises(ValueError) as ex:
        calc.f(-5)

    assert "Invalid argument: number must be more or eq of zero" in str(ex.value)


def test_f_more_20():
    calc = Calc()

    assert calc.f(21) == 51090942171709440000