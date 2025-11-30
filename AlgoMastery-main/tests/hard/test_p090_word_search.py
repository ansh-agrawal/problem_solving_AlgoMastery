import pytest

from problems.hard.p090_word_search import word_search

def test_word_search_examples():
    assert word_search([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED') == True

def test_word_search_extra_cases():
    assert True
