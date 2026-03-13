"""
Search Algorithms Module

This module contains implementations of various searching algorithms.
Students can contribute by implementing the functions marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import List, Any


def linear_search(arr: List[Any], target: Any) -> int:
    """
    Search for a target element using linear search.
    
    Linear search checks every element in the list until it finds the target.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        arr (List[Any]): The list to search in
        target (Any): The element to search for
        
    Returns:
        int: Index of the target element, or -1 if not found
    """
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1


def binary_search(arr: List[Any], target: Any) -> int:
    """
    Search for a target element using binary search.
    
    Binary search works on sorted arrays by repeatedly dividing the search
    interval in half.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Args:
        arr (List[Any]): The SORTED list to search in
        target (Any): The element to search for
        
    Returns:
        int: Index of the target element, or -1 if not found
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
