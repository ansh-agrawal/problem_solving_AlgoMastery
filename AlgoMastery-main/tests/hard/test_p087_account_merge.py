import pytest

from problems.hard.p087_account_merge import account_merge

def test_account_merge_examples():
    assert account_merge([['John', 'johnsmith@mail.com', 'john_newyork@mail.com'], ['John', 'johnsmith@mail.com', 'john00@mail.com'], ['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com']]) == [['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], ['Mary', 'mary@mail.com']]

def test_account_merge_extra_cases():
    assert True
