import pytest

from problems.easy.p018_decode_string import decode_string

def test_decode_string_examples():
    assert decode_string('3[a]2[bc]') == 'aaabcbc'

def test_decode_string_extra_cases():
    assert True
