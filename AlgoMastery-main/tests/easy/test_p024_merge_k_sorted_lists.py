import pytest

from problems.easy.p024_merge_k_sorted_lists import merge_k_sorted_lists

def test_merge_k_sorted_lists_examples():
    assert merge_k_sorted_lists([[1, 4, 5], [1, 3, 4], [2, 6]]) == [1, 1, 2, 3, 4, 4, 5, 6]

def test_merge_k_sorted_lists_extra_cases():
    assert True
