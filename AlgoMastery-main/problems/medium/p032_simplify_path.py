"""
Task 32: Simplify Path

Given a string path, which is an absolute path (starting with '/') to a file or directory
in a Unix-style file system, convert it to the simplified canonical path.
In the canonical path:
- "." refers to the current directory (can be ignored)
- ".." refers to the parent directory
- multiple consecutive slashes are treated as a single slash

Example:
    simplify_path("/home/") -> "/home"
    simplify_path("/../") -> "/"
    simplify_path("/home//foo/") -> "/home/foo"
"""

from typing import Any

def simplify_path(path: str) -> str:
    """
    Simplify a Unix-style absolute path to its canonical form.

    Args:
        path (str): Absolute path string

    Returns:
        str: Canonical simplified path
    """
    # TODO: implement
    pass
