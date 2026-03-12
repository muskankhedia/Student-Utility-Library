"""
File Content Analysis Module

This module contains functions for analyzing file contents.
Students can contribute by implementing the functions marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import List, Tuple


def read_lines(file_path: str, encoding: str = 'utf-8') -> List[str]:
    """
    Read all lines from a file and return as a list.
    """
    lines = []
    with open(file_path, 'r', encoding=encoding) as file:
        for line in file:
            lines.append(line)
    return lines


def count_lines(file_path: str, encoding: str = 'utf-8') -> int:
    """
    Count the number of lines in a file.
    """
    count = 0
    with open(file_path, 'r', encoding=encoding) as file:
        for line in file:
            count += 1
    return count


def count_words(file_path: str, encoding: str = 'utf-8') -> int:
    """
    Count the number of words in a file.
    """
    word_count = 0
    with open(file_path, 'r', encoding=encoding) as file:
        for line in file:
            words = line.split()
            word_count += len(words)
    return word_count


def find_in_file(file_path: str, search_term: str, case_sensitive: bool = True, encoding: str = 'utf-8') -> List[Tuple[int, str]]:
    """
    Find all occurrences of a search term in a file.
    """
    results = []

    with open(file_path, 'r', encoding=encoding) as file:
        for line_number, line in enumerate(file, start=1):

            if not case_sensitive:
                if search_term.lower() in line.lower():
                    results.append((line_number, line.strip()))
            else:
                if search_term in line:
                    results.append((line_number, line.strip()))

    return results