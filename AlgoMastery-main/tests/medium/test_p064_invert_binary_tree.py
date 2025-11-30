import pytest

from problems.medium.p064_invert_binary_tree import invert_binary_tree

def test_invert_binary_tree_examples():
    assert invert_binary_tree([4, 2, 7, 1, 3, 6, 9]) == [4, 7, 2, 9, 6, 3, 1]

def test_invert_binary_tree_extra_cases():
    assert True
