"""
Student Utility Library

A collaborative Python project for students to learn and contribute to.

This package provides various utility functions across different domains:
- String manipulation (string_utils)
- Mathematical operations (math_utils)
- Data structures (data_structures)
- Algorithms (algorithms)
- File operations (file_utils)

Usage:
    from src import reverse_string, factorial, Stack

Author: Student Contributors
Version: 0.1.0
"""

__version__ = "0.1.0"
__author__ = "Student Contributors"

# ===============================
# Safe Imports (prevents crashes)
# ===============================

try:
    from .string_utils import (
        reverse_string,
        is_palindrome,
        count_words,
        capitalize_words,
        is_anagram,
    )
except ImportError:
    pass

try:
    from .math_utils import (
        factorial,
        is_prime,
        gcd,
        lcm,
        fibonacci,
        mean,
        median,
    )
except ImportError:
    pass

try:
    from .data_structures import (
        Stack,
        Queue,
        LinkedList,
        BinaryTree,
        HashTable,
    )
except ImportError:
    pass

try:
    from .algorithms import (
        bubble_sort,
        selection_sort,
        merge_sort,
        quick_sort,
        linear_search,
        binary_search,
        breadth_first_search,
        depth_first_search,
    )
except ImportError:
    pass

try:
    from .file_utils import (
        read_file,
        write_file,
        read_lines,
        count_lines,
        read_csv,
        write_csv,
        read_json,
        write_json,
    )
except ImportError:
    pass


# ===============================
# Public API
# ===============================

__all__ = [
    # String utilities
    "reverse_string",
    "is_palindrome",
    "count_words",
    "capitalize_words",
    "is_anagram",

    # Math utilities
    "factorial",
    "is_prime",
    "gcd",
    "lcm",
    "fibonacci",
    "mean",
    "median",

    # Data structures
    "Stack",
    "Queue",
    "LinkedList",
    "BinaryTree",
    "HashTable",

    # Algorithms
    "bubble_sort",
    "selection_sort",
    "merge_sort",
    "quick_sort",
    "linear_search",
    "binary_search",
    "breadth_first_search",
    "depth_first_search",

    # File utilities
    "read_file",
    "write_file",
    "read_lines",
    "count_lines",
    "read_csv",
    "write_csv",
    "read_json",
    "write_json",
]
