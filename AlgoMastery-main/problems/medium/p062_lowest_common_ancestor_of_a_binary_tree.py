"""
Task 62: Lowest Common Ancestor of a Binary Tree

Given a binary tree and two nodes p and q, find the lowest common ancestor (LCA) of the two nodes.
The lowest common ancestor is defined as the lowest node in the tree that has both p and q as descendants
(a node can be a descendant of itself).

Example:
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    lowest_common_ancestor_of_a_binary_tree(root, root.left, root.left.right.right) -> TreeNode(5)
"""

from typing import Any

def lowest_common_ancestor_of_a_binary_tree(root: Any, p: Any, q: Any) -> Any:
    """
    Find the lowest common ancestor of two nodes in a binary tree.

    Args:
        root (Any): Root node of the binary tree
        p (Any): First target node
        q (Any): Second target node

    Returns:
        Any: Lowest common ancestor node
    """
    # TODO: implement
    pass
