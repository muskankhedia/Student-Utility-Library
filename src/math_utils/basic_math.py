"""
Basic Mathematical Operations Module

This module contains basic mathematical utility functions.
Students can contribute by implementing the functions marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import Union


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.
    """
    # Step 1: Check if n is negative
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    # Step 2: Base cases
    if n <= 1:
        return 1

    # Step 3: Loop calculation
    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


def power(base: Union[int, float], exponent: int) -> Union[int, float]:
    """
    Calculate base raised to the power of exponent without using ** or pow().
    """

    # Base case
    if exponent == 0:
        return 1

    # Handle negative exponent
    if exponent < 0:
        base = 1 / base
        exponent = -exponent

    result = 1

    # Multiply base exponent times
    for _ in range(exponent):
        result *= base

    return result


def square_root(number: Union[int, float], precision: float = 1e-10) -> float:
    """
    Calculate square root using Newton's method.
    """

    if number < 0:
        raise ValueError("Square root is not defined for negative numbers")

    if number == 0:
        return 0.0

    # Initial guess
    x = number

    while True:
        new_x = (x + number / x) / 2

        if abs(new_x - x) < precision:
            return new_x

        x = new_x
