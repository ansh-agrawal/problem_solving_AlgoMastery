import pytest

from problems.medium.p056_fibonacci_number import fibonacci_number

def test_fibonacci_number_examples():
    assert fibonacci_number(5) == 5

def test_fibonacci_number_extra_cases():
    assert fibonacci_number(0) == 0
    assert fibonacci_number(1) == 1
