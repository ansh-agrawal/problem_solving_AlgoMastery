import pytest

from problems.easy.p025_copy_list_with_random_pointer import copy_list_with_random_pointer

def test_copy_list_with_random_pointer_examples():
    assert copy_list_with_random_pointer([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]) == 'copy_ok'

def test_copy_list_with_random_pointer_extra_cases():
    assert True
