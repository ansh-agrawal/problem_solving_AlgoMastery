import pytest

from problems.medium.p029_valid_parentheses import valid_parentheses

def test_valid_parentheses_examples():
    assert valid_parentheses('()[]{}') == True

def test_valid_parentheses_extra_cases():
    assert valid_parentheses('([{}])') is True
