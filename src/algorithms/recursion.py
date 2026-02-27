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
    
    # Base Case: if string has 0 or 1 character, it is a palindrome
    if len(s) <= 1:
        return True
    
    # If first and last characters are not equal, not a palindrome
    if s[0] != s[-1]:
        return False
    
    # Recursive call on the substring excluding first and last characters
    return is_palindrome_recursive(s[1:-1])


def tower_of_hanoi(n: int, source: str, destination: str, auxiliary: str) -> List[str]:
    """
    Solve the Tower of Hanoi problem.
    
    Move n disks from source rod to destination rod using auxiliary rod.
    
    Args:
        n (int): Number of disks
        source (str): Source rod name
        destination (str): Destination rod name
        auxiliary (str): Auxiliary rod name
        
    Returns:
        List[str]: List of moves (strings describing each move)
    """
    
    moves = []
    
    def solve(n, source, destination, auxiliary):
        # Base Case
        if n == 1:
            moves.append(f"Move disk 1 from {source} to {destination}")
            return
        
        # Move n-1 disks to auxiliary rod
        solve(n - 1, source, auxiliary, destination)
        
        # Move the largest disk to destination
        moves.append(f"Move disk {n} from {source} to {destination}")
        
        # Move n-1 disks from auxiliary to destination
        solve(n - 1, auxiliary, destination, source)
    
    solve(n, source, destination, auxiliary)
    return moves
