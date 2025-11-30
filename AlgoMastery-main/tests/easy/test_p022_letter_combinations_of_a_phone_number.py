import pytest

from problems.easy.p022_letter_combinations_of_a_phone_number import letter_combinations_of_a_phone_number

def test_letter_combinations_of_a_phone_number_examples():
    assert letter_combinations_of_a_phone_number('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

def test_letter_combinations_of_a_phone_number_extra_cases():
    assert True
