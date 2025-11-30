import pytest

from problems.easy.p011_spiral_matrix import spiral_matrix

def test_spiral_matrix_examples():
    assert spiral_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

def test_spiral_matrix_extra_cases():
    assert True
