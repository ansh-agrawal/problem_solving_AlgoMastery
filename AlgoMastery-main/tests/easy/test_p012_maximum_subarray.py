import pytest

from problems.easy.p012_maximum_subarray import maximum_subarray

def test_maximum_subarray_examples():
    assert maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_maximum_subarray_extra_cases():
    assert maximum_subarray([1]) == 1
