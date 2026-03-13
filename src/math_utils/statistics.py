"""
Statistics Module

This module contains statistical calculation functions.
Students can contribute by implementing statistical functions.

Author: Student Contributors
Last Updated: March 2026
"""

from typing import List, Union


Number = Union[int, float]


def mean(numbers: List[Number]) -> float:
    """
    Calculate the arithmetic mean (average) of a list of numbers.
    """

    if not numbers:
        raise ValueError("The numbers list cannot be empty.")

    total = sum(numbers)
    count = len(numbers)

    return float(total) / count


def median(numbers: List[Number]) -> float:
    """
    Calculate the median of a list of numbers.
    """

    if not numbers:
        raise ValueError("The numbers list cannot be empty.")

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2

    if n % 2 == 1:
        return float(sorted_numbers[middle])
    else:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2


def mode(numbers: List[Number]) -> List[Number]:
    """
    Find the mode(s) of a list of numbers.
    """

    if not numbers:
        raise ValueError("The numbers list cannot be empty.")

    frequency = {}

    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    max_freq = max(frequency.values())

    modes = [num for num, freq in frequency.items() if freq == max_freq]

    return sorted(modes)


if __name__ == "__main__":
    data = [1, 2, 2, 3, 4, 4]

    print("Mean:", mean(data))
    print("Median:", median(data))
    print("Mode:", mode(data))
