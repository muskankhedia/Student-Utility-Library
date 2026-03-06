"""
Dynamic Programming Algorithms Module

This module contains implementations of dynamic programming algorithms.
Students can contribute by implementing the functions marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import List


def fibonacci_dp(n: int) -> int:
    """
    Calculate the nth Fibonacci number using dynamic programming.
    """
    if n <= 1:
        return n

    # Create DP table
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    # Fill the table
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def longest_common_subsequence(str1: str, str2: str) -> int:
    """
    Find the length of the longest common subsequence between two strings.
    """
    m = len(str1)
    n = len(str2)

    # Create DP table (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Solve the 0/1 Knapsack problem using dynamic programming.
    """
    n = len(weights)

    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]
