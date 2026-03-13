"""
Sorting Algorithms Module

This module contains implementations of various sorting algorithms.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import List, Any


def bubble_sort(arr: List[Any]) -> List[Any]:
    """
    Sort a list using the bubble sort algorithm.
    """
    sorted_arr = arr.copy()
    n = len(sorted_arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]

    return sorted_arr


def selection_sort(arr: List[Any]) -> List[Any]:
    """
    Sort a list using the selection sort algorithm.
    """
    sorted_arr = arr.copy()
    n = len(sorted_arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if sorted_arr[j] < sorted_arr[min_index]:
                min_index = j

        sorted_arr[i], sorted_arr[min_index] = (
            sorted_arr[min_index],
            sorted_arr[i],
        )

    return sorted_arr


def merge_sort(arr: List[Any]) -> List[Any]:
    """
    Sort a list using the merge sort algorithm.
    """
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left: List[Any], right: List[Any]) -> List[Any]:
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def quick_sort(arr: List[Any]) -> List[Any]:
    """
    Sort a list using the quick sort algorithm.
    """
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
