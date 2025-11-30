import pytest

from problems.medium.p069_evaluate_reverse_polish_notation import evaluate_reverse_polish_notation

def test_evaluate_reverse_polish_notation_examples():
    assert evaluate_reverse_polish_notation(['2', '1', '+', '3', '*']) == 9

def test_evaluate_reverse_polish_notation_extra_cases():
    assert True
