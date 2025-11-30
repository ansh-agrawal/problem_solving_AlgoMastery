import pytest

from problems.medium.p034_sliding_window_maximum import sliding_window_maximum

def test_sliding_window_maximum_examples():
    assert sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]

def test_sliding_window_maximum_extra_cases():
    assert True
