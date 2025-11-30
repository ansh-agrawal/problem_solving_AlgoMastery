"""
Task 99: Wildcard Matching

Implement wildcard pattern matching with support for '?' and '*':
- '?' Matches any single character.
- '*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string.

Example:
    wildcard_matching("aa","a") -> False
    wildcard_matching("aa","*") -> True
    wildcard_matching("cb","?a") -> False
    wildcard_matching("adceb","*a*b") -> True
    wildcard_matching("acdcb","a*c?b") -> False
"""

from typing import Any

def wildcard_matching(s: str, p: str) -> bool:
    """
    Perform wildcard pattern matching with '?' and '*'.

    Args:
        s (str): Input string
        p (str): Pattern string containing '?' and '*'

    Returns:
        bool: True if the string matches the pattern, False otherwise
    """
    # TODO: implement
    pass
