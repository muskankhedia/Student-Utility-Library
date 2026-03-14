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
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' does not exist")

        with open(file_path, 'r', encoding=encoding) as file:
            content = file.read()

        return content

    except FileNotFoundError:
        raise
    except IOError as e:
        raise IOError(f"Error reading file: {e}")


def write_file(file_path: str, content: str, encoding: str = 'utf-8', append: bool = False) -> None:
    """
    Write content to a text file.
    """
    try:
        mode = 'a' if append else 'w'

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
            print("Source file does not exist.")
            return False

        if os.path.exists(destination) and not overwrite:
            print("Destination file already exists. Set overwrite=True to replace.")
            return False

        shutil.copy2(source, destination)
        return True

    except Exception as e:
        print(f"Error copying file: {e}")
        return False


def move_file(source: str, destination: str, overwrite: bool = False) -> bool:
    """
    Move (or rename) a file from source to destination.
    """
    try:
        if not os.path.exists(source):
            print("Source file does not exist.")
            return False

        if os.path.exists(destination) and not overwrite:
            print("Destination file already exists. Set overwrite=True to replace.")
            return False

        shutil.move(source, destination)
        return True

    except Exception as e:
        print(f"Error moving file: {e}")
        return False


def delete_file(file_path: str) -> bool:
    """
    Delete a file.
    """
    try:
        if not os.path.exists(file_path):
            print("File does not exist.")
            return False

        os.remove(file_path)
        return True

    except Exception as e:
        print(f"Error deleting file: {e}")
        return False
