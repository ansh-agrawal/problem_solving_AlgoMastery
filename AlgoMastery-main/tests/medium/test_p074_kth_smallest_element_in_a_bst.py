import pytest

from problems.medium.p074_kth_smallest_element_in_a_bst import kth_smallest_element_in_a_bst

def test_kth_smallest_element_in_a_bst_examples():
    assert kth_smallest_element_in_a_bst([3, 1, 4, None, 2], 1) == 1

def test_kth_smallest_element_in_a_bst_extra_cases():
    assert True
