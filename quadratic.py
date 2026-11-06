from collections.abc import Callable

from scipy.integrate import quad


def average_value(f: Callable[[float], float], a: float, b: float) -> float:
    """Return the average value of f over the interval [a, b]."""
    if a == b:
        raise ValueError("The interval endpoints must be different.")

    integral, _error_estimate = quad(f, a, b)
    return integral / (b - a)