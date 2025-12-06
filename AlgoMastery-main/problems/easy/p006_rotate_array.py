"""
Task 6: Rotate Array

Given an array nums, rotate the array to the right by k steps (0-indexed).

Example:
    rotate_array(nums=[1,2,3,4,5,6,7], k=3) -> [5,6,7,1,2,3,4]
    rotate_array(nums=[-1,-100,3,99], k=2) -> [3,99,-1,-100]

Args:
    nums (list[int]): List of integers (0-indexed)
    k (int): Number of steps to rotate

Returns:
    list[int]: Rotated array
"""

def rotate_array(nums: list[int], k: int) -> list[int]:
    left=0
    right=len(nums)-k-1
    while left<right:
        nums[left],nums[right] = nums[right],nums[left]
        left+=1
        right-=1
    left=len(nums)-k
    right=len(nums)-1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    nums.reverse()
    return  nums