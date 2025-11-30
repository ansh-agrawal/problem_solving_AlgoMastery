import pytest

from problems.hard.p078_insert_interval import insert_interval

def test_insert_interval_examples():
    assert insert_interval([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]

def test_insert_interval_extra_cases():
    assert True
