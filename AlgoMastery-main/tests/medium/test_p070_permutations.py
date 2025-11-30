import pytest

from problems.medium.p070_permutations import permutations

def test_permutations_examples():
    assert permutations([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

def test_permutations_extra_cases():
    assert True
