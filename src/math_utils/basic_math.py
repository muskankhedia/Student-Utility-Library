"""
Basic Mathematical Operations Module

This module contains basic mathematical utility functions.
Students can contribute by implementing the functions marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import Union


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    """
    Calculate the factorial of a non-negative integer.
    
    Factorial of n (denoted as n!) is the product of all positive integers 
    less than or equal to n. By definition, 0! = 1.
    
    Args:
        n (int): Non-negative integer to calculate factorial for
        
    Returns:
        int: The factorial of n
        
    Raises:
        ValueError: If n is negative
        
    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
        >>> factorial(1)
        1
    
    # TODO: Implement this function
    # Hint: You can use recursion or iteration. Don't forget to handle edge cases!
    """
    # Step 1: Check if n is negative and raise ValueError if so
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    # Step 2: Handle base cases (0 and 1)
    if n <= 1:
        return 1
    # Step 3: Calculate factorial using a loop
main
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def power(base: Union[int, float], exponent: int) -> Union[int, float]:
    if exponent == 0:
        return 1
    elif exponent > 0:
        result = 1
        for _ in range(exponent):
            result *= base
        return result
    else:
        # Handle negative exponents
        result = 1
        for _ in range(-exponent):
            result *= base
        return 1 / result


def square_root(number: Union[int, float], precision: float = 1e-10) -> float:
    """
    Calculate the square root of a number using Newton's method.
    
    This implements square root calculation without using built-in functions.
    
    Args:
        number (Union[int, float]): The number to find square root of
        precision (float): The desired precision (default: 1e-10)
        
    Returns:
        float: The square root of the number
        
    Raises:
        ValueError: If number is negative
        
    Examples:
        >>> square_root(16)
        4.0
        >>> square_root(2)  # approximately
        1.4142135623730951
    
    TODO: Implement this function
    Hint: Use Newton's method: x_new = (x + number/x) / 2
    """
    pass