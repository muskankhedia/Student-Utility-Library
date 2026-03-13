"""
Basic Mathematical Operations Module

This module provides simple mathematical utility functions.
Students can contribute by improving or adding new functions.

Author: Student Contributors
Last Updated: March 2026
"""

from typing import Union


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    Factorial of n (written as n!) is the product of all positive
    integers less than or equal to n. By definition, 0! = 1.

    Args:
        n (int): Non-negative integer

    Returns:
        int: factorial of n

    Raises:
        ValueError: If n is negative

    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if n <= 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


def power(base: Union[int, float], exponent: int) -> Union[int, float]:
    """
    Calculate base raised to the power of exponent.

    This function implements exponentiation without using ** or pow().

    Args:
        base (Union[int, float]): base value
        exponent (int): exponent value

    Returns:
        Union[int, float]: result of base^exponent

    Examples:
        >>> power(2, 3)
        8
        >>> power(5, 0)
        1
        >>> power(2, -2)
        0.25
    """

    if exponent == 0:
        return 1

    result = 1
    exp = abs(exponent)

    for _ in range(exp):
        result *= base

    if exponent < 0:
        return 1 / result

    return result


def square_root(number: Union[int, float], precision: float = 1e-10) -> float:
    """
    Calculate the square root using Newton's Method.

    Args:
        number (Union[int, float]): number to compute square root
        precision (float): acceptable error tolerance

    Returns:
        float: square root of the number

    Raises:
        ValueError: if number is negative

    Examples:
        >>> square_root(16)
        4.0
        >>> square_root(2)
        1.414213562...
    """

    if number < 0:
        raise ValueError("Square root is not defined for negative numbers")

    if number == 0:
        return 0.0

    x = number

    while True:
        new_x = (x + number / x) / 2
        if abs(new_x - x) < precision:
            return new_x
        x = new_x