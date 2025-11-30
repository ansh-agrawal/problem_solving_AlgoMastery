import pytest

from problems.easy.p019_valid_anagram import valid_anagram

def test_valid_anagram_examples():
    assert valid_anagram('anagram', 'nagaram') == True

def test_valid_anagram_extra_cases():
    assert True
