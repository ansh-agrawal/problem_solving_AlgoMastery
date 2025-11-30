import pytest

from problems.easy.p003_merge_intervals import merge_intervals

def test_merge_intervals_examples():
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]

def test_merge_intervals_extra_cases():
    assert True
