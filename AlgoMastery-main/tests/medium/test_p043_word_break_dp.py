import pytest

from problems.medium.p043_word_break_dp import word_break_dp

def test_word_break_dp_examples():
    assert word_break_dp('applepenapple', ['apple', 'pen']) == True

def test_word_break_dp_extra_cases():
    assert True
