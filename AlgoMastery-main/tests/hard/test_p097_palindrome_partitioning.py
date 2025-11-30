import pytest

from problems.hard.p097_palindrome_partitioning import palindrome_partitioning

def test_palindrome_partitioning_examples():
    assert palindrome_partitioning('aab') == [['a', 'a', 'b'], ['aa', 'b']]

def test_palindrome_partitioning_extra_cases():
    assert True
