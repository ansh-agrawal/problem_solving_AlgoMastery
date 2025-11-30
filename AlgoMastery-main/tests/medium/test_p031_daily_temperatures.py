import pytest

from problems.medium.p031_daily_temperatures import daily_temperatures

def test_daily_temperatures_examples():
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]

def test_daily_temperatures_extra_cases():
    assert True
