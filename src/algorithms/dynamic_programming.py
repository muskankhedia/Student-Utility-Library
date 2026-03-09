"""
Dynamic Programming Algorithms Module

This module contains simple implementations of popular
Dynamic Programming algorithms for learning purposes.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import List


def fibonacci_dp(n: int) -> int:
    """
    Return the nth Fibonacci number using Dynamic Programming.
    Example: 0, 1, 1, 2, 3, 5, 8 ...
    """

    # Base cases
    if n <= 1:
        return n

    # Create a list to store Fibonacci values
    fib = [0] * (n + 1)

    # First two Fibonacci numbers
    fib[0] = 0
    fib[1] = 1

    # Calculate remaining Fibonacci numbers
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


def longest_common_subsequence(str1: str, str2: str) -> int:
    """
    Find the length of the Longest Common Subsequence (LCS)
    between two strings.
    """

    len1 = len(str1)
    len2 = len(str2)

    # Create DP table
    dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    # Fill the DP table
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):

            # If characters match
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            # If characters do not match
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len1][len2]


def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Solve the 0/1 Knapsack problem using Dynamic Programming.

    weights  -> list of item weights
    values   -> list of item values
    capacity -> maximum weight the bag can hold
    """

    number_of_items = len(weights)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(number_of_items + 1)]

    # Build the table
    for i in range(1, number_of_items + 1):
        for current_capacity in range(capacity + 1):

            # If current item weight fits in the bag
            if weights[i - 1] <= current_capacity:
                include_item = values[i - 1] + dp[i - 1][current_capacity - weights[i - 1]]
                exclude_item = dp[i - 1][current_capacity]

                dp[i][current_capacity] = max(include_item, exclude_item)

            # If item cannot be included
            else:
                dp[i][current_capacity] = dp[i - 1][current_capacity]

    return dp[number_of_items][capacity]
