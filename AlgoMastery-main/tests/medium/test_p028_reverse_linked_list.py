import pytest

from problems.medium.p028_reverse_linked_list import reverse_linked_list

def test_reverse_linked_list_examples():
    assert reverse_linked_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

def test_reverse_linked_list_extra_cases():
    assert reverse_linked_list([1,2]) == [2,1]
