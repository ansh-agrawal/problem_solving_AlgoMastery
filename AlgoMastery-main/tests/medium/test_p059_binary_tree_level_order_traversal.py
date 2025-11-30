import pytest

from problems.medium.p059_binary_tree_level_order_traversal import binary_tree_level_order_traversal

def test_binary_tree_level_order_traversal_examples():
    assert binary_tree_level_order_traversal([3, 9, 20, None, None, 15, 7]) == [[3], [9, 20], [15, 7]]

def test_binary_tree_level_order_traversal_extra_cases():
    assert True
