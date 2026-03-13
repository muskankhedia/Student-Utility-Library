"""
Binary Tree Data Structure Module

This module contains the BinaryTree and TreeNode implementations.
Students can contribute by implementing the class methods marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import Any, List


class TreeNode:
    """
    A node class for binary tree implementation.
    """

    def __init__(self, data: Any):
        """
        Initialize a tree node.
        """
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """
    A binary tree implementation.

    Each node has at most two children: left and right.
    """

    def __init__(self):
        """Initialize an empty binary tree."""
        self.root = None

    def insert(self, data: Any) -> None:
        """Insert a new node into the binary search tree."""
        
        new_node = TreeNode(data)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, data: Any) -> bool:
        """Search for a value in the tree."""

        current = self.root

        while current:
            if current.data == data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right

        return False

    def inorder_traversal(self) -> List[Any]:
        """Left -> Root -> Right"""
        
        result = []

        def traverse(node):
            if node:
                traverse(node.left)
                result.append(node.data)
                traverse(node.right)

        traverse(self.root)
        return result

    def preorder_traversal(self) -> List[Any]:
        """Root -> Left -> Right"""

        result = []

        def traverse(node):
            if node:
                result.append(node.data)
                traverse(node.left)
                traverse(node.right)

        traverse(self.root)
        return result

    def postorder_traversal(self) -> List[Any]:
        """Left -> Right -> Root"""

        result = []

        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                result.append(node.data)

        traverse(self.root)
        return result
