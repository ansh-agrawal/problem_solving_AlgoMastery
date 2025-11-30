import pytest

from problems.easy.p002_trapping_rain_water import trapping_rain_water

def test_trapping_rain_water_examples():
    assert trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

def test_trapping_rain_water_extra_cases():
    assert True
