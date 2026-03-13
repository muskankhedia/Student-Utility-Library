"""
Basic File Operations Module

This module contains basic file input/output operations.

Author: Student Contributors
Last Updated: February 2026
"""

import os
import shutil


def read_file(file_path: str, encoding: str = 'utf-8') -> str:
    """
    Read the entire content of a text file.
    """
    try:
        # Step 1: Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} does not exist")

        # Step 2: Open file and read content
        with open(file_path, 'r', encoding=encoding) as file:
            content = file.read()

        # Step 3: Return content
        return content

    except IOError as e:
        print("Error reading file:", e)
        raise


def write_file(file_path: str, content: str, encoding: str = 'utf-8', append: bool = False) -> None:
    """
    Write content to a text file.
    """
    try:
        # Choose mode
        mode = 'a' if append else 'w'

        # Write content
        with open(file_path, mode, encoding=encoding) as file:
            file.write(content)

    except IOError as e:
        print("Error writing file:", e)
        raise


def copy_file(source: str, destination: str, overwrite: bool = False) -> bool:
    """
    Copy a file from source to destination.
    """
    try:
        if not os.path.exists(source):
            print("Source file does not exist")
            return False

        if os.path.exists(destination) and not overwrite:
            print("Destination file already exists")
            return False

        shutil.copy(source, destination)
        return True

    except IOError as e:
        print("Error copying file:", e)
        return False


def move_file(source: str, destination: str, overwrite: bool = False) -> bool:
    """
    Move (or rename) a file from source to destination.
    """
    try:
        if not os.path.exists(source):
            print("Source file does not exist")
            return False

        if os.path.exists(destination) and not overwrite:
            print("Destination file already exists")
            return False

        shutil.move(source, destination)
        return True

    except IOError as e:
        print("Error moving file:", e)
        return False


def delete_file(file_path: str) -> bool:
    """
    Delete a file.
    """
    try:
        if not os.path.exists(file_path):
            print("File does not exist")
            return False

        os.remove(file_path)
        return True

    except IOError as e:
        print("Error deleting file:", e)
        return False
