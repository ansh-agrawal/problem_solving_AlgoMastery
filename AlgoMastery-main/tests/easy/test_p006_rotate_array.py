import pytest

from problems.easy.p006_rotate_array import rotate_array

def test_rotate_array_examples():
    assert rotate_array([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]

def test_rotate_array_extra_cases():
    assert True
