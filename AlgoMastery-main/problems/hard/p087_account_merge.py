"""
Task 87: Account Merge

Given a list of accounts where each account is a list of strings: the first element is the name,
and the rest are emails. Merge accounts that have at least one common email, and return the merged accounts.
Each account in the result should have the name first, followed by emails in sorted order.

Example:
    account_merge([["John","johnsmith@mail.com","john_newyork@mail.com"],
                   ["John","johnsmith@mail.com","john00@mail.com"],
                   ["Mary","mary@mail.com"],
                   ["John","johnnybravo@mail.com"]])
    -> [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
        ["Mary","mary@mail.com"],
        ["John","johnnybravo@mail.com"]]
"""

from typing import Any, List

def account_merge(accounts: List[List[str]]) -> List[List[str]]:
    """
    Merge accounts with common emails.

    Args:
        accounts (List[List[str]]): List of accounts (name + emails)

    Returns:
        List[List[str]]: Merged accounts with sorted emails
    """
    # TODO: implement
    pass
