"""
Task 96: Burst Balloons

Given n balloons, indexed from 0 to n-1, each with a number represented by an array nums.
You are asked to burst all the balloons. When you burst balloon i, you gain coins equal to
nums[left] * nums[i] * nums[right], where left and right are adjacent indices of i (if out of bounds, treat as 1).
Return the maximum coins you can collect by bursting the balloons wisely.

Example:
    burst_balloons([3,1,5,8]) -> 167
    burst_balloons([1,5]) -> 10
    burst_balloons([1,2,3,4]) -> 20
"""

from typing import Any, List

def burst_balloons(nums: List[int]) -> int:
    """
    Compute the maximum coins by bursting balloons in optimal order.

    Args:
        nums (List[int]): List of balloon numbers

    Returns:
        int: Maximum coins obtainable
    """
    # TODO: implement
    pass
