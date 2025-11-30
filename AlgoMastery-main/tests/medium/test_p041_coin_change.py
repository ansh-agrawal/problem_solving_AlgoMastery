import pytest

from problems.medium.p041_coin_change import coin_change

def test_coin_change_examples():
    assert coin_change([1, 2, 5], 11) == 3

def test_coin_change_extra_cases():
    assert True
