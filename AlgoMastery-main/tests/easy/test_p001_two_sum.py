import pytest

from problems.easy.p001_two_sum import two_sum

def test_two_sum_examples():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_extra_cases():
    assert two_sum([1,2,3], 4) == [0,2]
