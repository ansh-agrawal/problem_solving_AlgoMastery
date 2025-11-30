"""
Task 100: Regular Expression Matching

Implement regular expression matching with support for '.' and '*':
- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Example:
    regular_expression_matching("aa","a") -> False
    regular_expression_matching("aa","a*") -> True
    regular_expression_matching("mississippi","mis*is*p*.") -> False
    regular_expression_matching("ab",".*") -> True
"""

from typing import Any

def regular_expression_matching(s: str, p: str) -> bool:
    """
    Perform regex matching with '.' and '*'.

    Args:
        s (str): Input string
        p (str): Pattern string containing '.' and '*'

    Returns:
        bool: True if the string matches the pattern, False otherwise
    """
    # TODO: implement
    pass
