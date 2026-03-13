"""
Recursion Algorithms Module

This module contains implementations of recursive algorithms.
Students can contribute by implementing the functions marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import List


def is_palindrome_recursive(s: str) -> bool:
    """
    Check if a string is a palindrome using recursion.
    
    Args:
        s (str): The string to check
        
    Returns:
        bool: True if palindrome, False otherwise
        
    Examples:
        >>> is_palindrome_recursive("racecar")
        True
        >>> is_palindrome_recursive("hello")
        False
    """

    # Base case: if string length is 0 or 1
    if len(s) <= 1:
        return True

    # If first and last characters are different
    if s[0] != s[-1]:
        return False

    # Recursive call with middle substring
    return is_palindrome_recursive(s[1:-1])


def tower_of_hanoi(n: int, source: str, destination: str, auxiliary: str) -> List[str]:
    """
    Solve the Tower of Hanoi problem.
    """

    moves = []

    def solve(n, source, destination, auxiliary):
        # Base case
        if n == 1:
            moves.append(f"Move disk 1 from {source} to {destination}")
            return

        # Step 1: Move n-1 disks from source to auxiliary
        solve(n - 1, source, auxiliary, destination)

        # Step 2: Move nth disk to destination
        moves.append(f"Move disk {n} from {source} to {destination}")

        # Step 3: Move n-1 disks from auxiliary to destination
        solve(n - 1, auxiliary, destination, source)

    solve(n, source, destination, auxiliary)

    return moves
