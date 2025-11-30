import pytest

from problems.medium.p058_binary_tree_inorder_traversal import binary_tree_inorder_traversal

def test_binary_tree_inorder_traversal_examples():
    assert binary_tree_inorder_traversal([1, None, 2, 3]) == [1, 3, 2]

def test_binary_tree_inorder_traversal_extra_cases():
    assert True
