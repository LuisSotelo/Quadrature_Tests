import pytest

from quadratic import average_value


def test_average_of_constant_function():
    assert average_value(lambda x: 5, 0, 2) == pytest.approx(5)


def test_average_of_linear_function():
    # The average of f(x) = x over [0, 2] is 1.
    assert average_value(lambda x: x, 0, 2) == pytest.approx(1)


def test_average_of_quadratic_function():
    # The average of f(x) = x² over [0, 3] is 3.
    assert average_value(lambda x: x**2, 0, 3) == pytest.approx(3)


def test_equal_endpoints_raise_value_error():
    with pytest.raises(ValueError):
        average_value(lambda x: x, 1, 1)