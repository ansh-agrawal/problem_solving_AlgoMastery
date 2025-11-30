import pytest

from problems.hard.p100_regular_expression_matching import regular_expression_matching

def test_regular_expression_matching_examples():
    assert regular_expression_matching('aa', 'a*') == True

def test_regular_expression_matching_extra_cases():
    assert True
