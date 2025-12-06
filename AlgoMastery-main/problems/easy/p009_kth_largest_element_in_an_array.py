"""
Task 9: Kth Largest Element in an Array

Given an array nums and an integer k, return the kth largest element in the array (1-indexed).

Example:
    kth_largest_element_in_an_array(nums=[3,2,1,5,6,4], k=2) -> 5
    kth_largest_element_in_an_array(nums=[3,2,3,1,2,4,5,5,6], k=4) -> 4

Args:
    nums (list[int]): List of integers (0-indexed)
    k (int): The kth position (1-indexed)

Returns:
    int: The kth largest element
"""

def kth_largest_element_in_an_array(nums: list[int], k: int) -> int:
    nums.sort(reverse=True)
    return nums[k-1]
