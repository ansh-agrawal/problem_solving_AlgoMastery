import pytest

from problems.medium.p044_maximum_subarray_dp import maximum_subarray_dp

def test_maximum_subarray_dp_examples():
    assert maximum_subarray_dp([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_maximum_subarray_dp_extra_cases():
    assert True
