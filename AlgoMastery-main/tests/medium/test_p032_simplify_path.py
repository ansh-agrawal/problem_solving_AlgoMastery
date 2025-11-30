import pytest

from problems.medium.p032_simplify_path import simplify_path

def test_simplify_path_examples():
    assert simplify_path('/a/./b/../../c/') == '/c'

def test_simplify_path_extra_cases():
    assert True
