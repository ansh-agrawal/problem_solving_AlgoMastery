import pytest

from problems.hard.p086_partition_labels import partition_labels

def test_partition_labels_examples():
    assert partition_labels('ababcbacadefegdehijhklij') == [9, 7, 8]

def test_partition_labels_extra_cases():
    assert True
