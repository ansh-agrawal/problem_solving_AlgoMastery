import pytest

from problems.easy.p015_group_anagrams import group_anagrams

def test_group_anagrams_examples():
    assert group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

def test_group_anagrams_extra_cases():
    assert True
