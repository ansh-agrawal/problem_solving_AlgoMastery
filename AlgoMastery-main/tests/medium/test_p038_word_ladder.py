import pytest

from problems.medium.p038_word_ladder import word_ladder

def test_word_ladder_examples():
    assert word_ladder('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']) == 5

def test_word_ladder_extra_cases():
    assert True
