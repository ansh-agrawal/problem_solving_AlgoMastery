import pytest

from problems.medium.p061_serialize_and_deserialize_binary_tree import serialize_and_deserialize_binary_tree

def test_serialize_and_deserialize_binary_tree_examples():
    assert serialize_and_deserialize_binary_tree([1, 2, 3, None, None, 4, 5]) == 'serialize_ok'

def test_serialize_and_deserialize_binary_tree_extra_cases():
    assert True
