import pytest

from problems.medium.p045_edit_distance import edit_distance

def test_edit_distance_examples():
    assert edit_distance('horse', 'ros') == 3

def test_edit_distance_extra_cases():
    assert True
