"""
Basic File Operations Module

This module contains basic file input/output operations.
Students can contribute by implementing the functions marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

import os
import shutil


def read_file(file_path: str, encoding: str = 'utf-8') -> str:
    """
    Read the entire content of a text file.
    """
    # Step 1: Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        # Step 2: Open file with proper encoding
        with open(file_path, 'r', encoding=encoding) as file:
            # Step 3: Read and return content
            content = file.read()
            return content
    except IOError as e:
        # Step 4: Handle exceptions
        raise IOError(f"Error reading file: {e}")


def write_file(file_path: str, content: str, encoding: str = 'utf-8', append: bool = False) -> None:
    """
    Write content to a text file.
    """
    mode = 'a' if append else 'w'

    try:
        with open(file_path, mode, encoding=encoding) as file:
            file.write(content)
    except IOError as e:
        raise IOError(f"Error writing to file: {e}")


def copy_file(source: str, destination: str, overwrite: bool = False) -> bool:
    """
    Copy a file from source to destination.
    """
    try:
        if not os.path.exists(source):
            return False

        if os.path.exists(destination) and not overwrite:
            return False

        shutil.copy2(source, destination)
        return True
    except Exception:
        return False


def move_file(source: str, destination: str, overwrite: bool = False) -> bool:
    """
    Move (or rename) a file from source to destination.
    """
    try:
        if not os.path.exists(source):
            return False

        if os.path.exists(destination):
            if overwrite:
                os.remove(destination)
            else:
                return False

        shutil.move(source, destination)
        return True
    except Exception:
        return False


def delete_file(file_path: str) -> bool:
    """
    Delete a file.
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False
    except Exception:
        return False