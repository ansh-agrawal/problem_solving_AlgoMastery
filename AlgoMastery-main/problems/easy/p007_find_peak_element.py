"""
Task 7: Find Peak Element

Given an array nums, find a peak element and return its index (0-indexed). A peak element is an element that is strictly greater than its neighbors.

Example:
    find_peak_element(nums=[1,2,3,1]) -> 2
    find_peak_element(nums=[1,2,1,3,5,6,4]) -> 5

Args:
    nums (list[int]): List of integers (0-indexed)

Returns:
    int: Index of a peak element
"""

def find_peak_element(nums: list[int]) -> int:
    if len(nums)<=2:
        return max(nums)
    temp=[]
    for i in range(1,len(nums)-1):
        temp_list=[]
        if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
            temp_list.append(nums[i])
            temp_list.append(i)
            temp.append(temp_list)
    max_ele=-1
    max_ele_index=-1
    for i in range(len(temp)):
        if temp[i][0]>max_ele:
            max_ele=temp[i][0]
            max_ele_index=temp[i][1]
    return max_ele_index