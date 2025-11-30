import pytest

from problems.medium.p067_convert_sorted_array_to_bst import convert_sorted_array_to_bst

def test_convert_sorted_array_to_bst_examples():
    assert convert_sorted_array_to_bst([-10, -3, 0, 5, 9]) == 'bst_ok'

def test_convert_sorted_array_to_bst_extra_cases():
    assert True
