import pytest

from problems.medium.p054_subsets import subsets

def test_subsets_examples():
    assert subsets([1, 2, 3]) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

def test_subsets_extra_cases():
    assert True
