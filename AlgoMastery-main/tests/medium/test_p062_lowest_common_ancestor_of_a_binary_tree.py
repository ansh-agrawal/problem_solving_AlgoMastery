import pytest

from problems.medium.p062_lowest_common_ancestor_of_a_binary_tree import lowest_common_ancestor_of_a_binary_tree

def test_lowest_common_ancestor_of_a_binary_tree_examples():
    assert lowest_common_ancestor_of_a_binary_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1) == 3

def test_lowest_common_ancestor_of_a_binary_tree_extra_cases():
    assert True
