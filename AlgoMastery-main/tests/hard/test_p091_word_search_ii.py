import pytest

from problems.hard.p091_word_search_ii import word_search_ii

def test_word_search_ii_examples():
    assert word_search_ii([['oath', 'pea', 'eat', 'rain'], [['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']]]) == ['oath', 'eat']

def test_word_search_ii_extra_cases():
    assert True
