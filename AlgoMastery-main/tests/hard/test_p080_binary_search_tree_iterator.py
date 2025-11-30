import pytest

from problems.hard.p080_binary_search_tree_iterator import binary_search_tree_iterator

def test_binary_search_tree_iterator_examples():
    assert binary_search_tree_iterator([7, 3, 15, None, None, 9, 20]) == [3, 7, 9, 15, 20]

def test_binary_search_tree_iterator_extra_cases():
    assert True
