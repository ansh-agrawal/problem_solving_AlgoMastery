import pytest
from problems.hard.p101_longest_increasing_path import longest_increasing_path

def test_longest_increasing_path_examples():
    # Example 1
    matrix1 = [
        [9,9,4],
        [6,6,8],
        [2,1,1]
    ]
    assert longest_increasing_path(matrix1) == 4  # Path: [1,2,6,9]

    # Example 2
    matrix2 = [
        [3,4,5],
        [3,2,6],
        [2,2,1]
    ]
    assert longest_increasing_path(matrix2) == 4  # Path: [3,4,5,6]

def test_longest_increasing_path_edge_cases():
    # Single element
    matrix3 = [[7]]
    assert longest_increasing_path(matrix3) == 1

    # All elements equal
    matrix4 = [
        [1,1],
        [1,1]
    ]
    assert longest_increasing_path(matrix4) == 1

    # Increasing row-wise only
    matrix5 = [
        [1,2,3,4]
    ]
    assert longest_increasing_path(matrix5) == 4

    # Increasing column-wise only
    matrix6 = [
        [1],
        [2],
        [3],
        [4]
    ]
    assert longest_increasing_path(matrix6) == 4
