"""
Sorting Algorithms Module

This module contains implementations of various sorting algorithms.
Students can contribute by implementing the functions marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import List, Any


def bubble_sort(arr: List[Any]) -> List[Any]:
    """
    Sort a list using the bubble sort algorithm.
    
    Bubble sort repeatedly steps through the list, compares adjacent elements
    and swaps them if they're in the wrong order.
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    
    Args:
        arr (List[Any]): The list to sort
        
    Returns:
        List[Any]: A new sorted list
        
    Examples:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
        >>> bubble_sort([5, 1, 4, 2, 8])
        [1, 2, 4, 5, 8]
    
    TODO: Implement bubble sort algorithm
    Hint: Use nested loops. Compare adjacent elements and swap if needed.
    """
    # TODO: Implement bubble sort
    # Step 1: Create a copy of the input array
    # Step 2: Use nested loops to compare adjacent elements
    # Step 3: Swap elements if they're in wrong order
    # Step 4: Return the sorted array
    pass


def selection_sort(arr: List[Any]) -> List[Any]:
    """
    Sort a list using the selection sort algorithm.
    
    Selection sort finds the minimum element and places it at the beginning,
    then finds the second minimum and places it in the second position, etc.
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    
    Args:
        arr (List[Any]): The list to sort
        
    Returns:
        List[Any]: A new sorted list
        
    Examples:
        >>> selection_sort([64, 25, 12, 22, 11])
        [11, 12, 22, 25, 64]
    
    TODO: Implement selection sort algorithm
    """
    # TODO: Implement selection sort
    pass


def merge_sort(arr: List[Any]) -> List[Any]:
    """
    Sort a list using the merge sort algorithm.
    
    Merge sort is a divide-and-conquer algorithm that divides the input array
    into two halves, sorts them recursively, and then merges them.
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Args:
        arr (List[Any]): The list to sort
        
    Returns:
        List[Any]: A new sorted list
        
    Examples:
        >>> merge_sort([38, 27, 43, 3, 9, 82, 10])
        [3, 9, 10, 27, 38, 43, 82]
    
    TODO: Implement merge sort algorithm
    Hint: You'll need a helper function to merge two sorted arrays
    """
    # TODO: Implement merge sort
    pass


def quick_sort(arr: List[Any]) -> List[Any]:
    """
    Sort a list using the quick sort algorithm.
    
    Quick sort picks a 'pivot' element and partitions the array around it,
    then recursively sorts the sub-arrays.
    
    Time Complexity: O(n log n) average, O(n²) worst case
    Space Complexity: O(log n)
    
    Args:
        arr (List[Any]): The list to sort
        
    Returns:
        List[Any]: A new sorted list
        
    Examples:
        >>> quick_sort([10, 7, 8, 9, 1, 5])
        [1, 5, 7, 8, 9, 10]
    
    TODO: Implement quick sort algorithm
    """
    # TODO: Implement quick sort
    pass


def bubble_sort(arr):
    """
    This function sorts a list using Bubble Sort
    and returns a new sorted list.
    """

    # Make a copy so original list is not changed
    new_list = arr.copy()

    n = len(new_list)

    # Bubble sort logic
    for i in range(n):
        for j in range(n - 1):
            if new_list[j] > new_list[j + 1]:
                # Swap elements
                temp = new_list[j]
                new_list[j] = new_list[j + 1]
                new_list[j + 1] = temp

    return new_list




