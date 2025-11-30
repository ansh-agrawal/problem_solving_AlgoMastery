"""
Task 25: Copy List with Random Pointer

Given a linked list where each node contains an additional random pointer, return a deep copy of the list. The list is represented as a list of tuples (val, random_index), where random_index is the index of the node pointed to by random (or None).

Example:
    copy_list_with_random_pointer(nodes=[(7,None),(13,0),(11,4),(10,2),(1,0)]) -> [(7,None),(13,0),(11,4),(10,2),(1,0)]

Args:
    nodes (list[tuple[int, Optional[int]]]): List of (val, random_index) tuples (0-indexed)

Returns:
    list[tuple[int, Optional[int]]]: Deep copy of the list in the same format
"""

from typing import Optional

def copy_list_with_random_pointer(nodes: list[tuple[int, Optional[int]]]) -> list[tuple[int, Optional[int]]]:
    """
    Copy List with Random Pointer.

    Args:
        nodes (list[tuple[int, Optional[int]]]): List of (val, random_index) tuples (0-indexed)

    Returns:
        list[tuple[int, Optional[int]]]: Deep copy of the list in the same format
    """
    pass
