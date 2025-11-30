"""
Task 74: Kth Smallest Element in a BST

Given the root of a binary search tree (BST) and an integer k,
return the kth smallest value (1st smallest is k=1) of all the values of the nodes in the tree.

Example:
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    kth_smallest_element_in_a_bst(root, 1) -> 1
    kth_smallest_element_in_a_bst(root, 3) -> 3
"""

from typing import Any

def kth_smallest_element_in_a_bst(root: Any, k: int) -> int:
    """
    Find the kth smallest element in a BST.

    Args:
        root (Any): Root node of the BST
        k (int): k-th position to find the smallest element

    Returns:
        int: The kth smallest element in the BST
    """
    # TODO: implement
    pass
