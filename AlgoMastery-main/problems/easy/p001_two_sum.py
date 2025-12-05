"""
Task 1: Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Return the answer as a list of indices (0-indexed).

Example:
    two_sum(nums=[2,7,11,15], target=9) -> [0,1]
    two_sum(nums=[3,2,4], target=6) -> [1,2]

Args:
    nums (list[int]): List of integers (0-indexed)
    target (int): Target sum

Returns:
    list[int]: Indices of the two numbers
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    dict_indices = {}
    for i in range(len(nums)):
        dict_indices[nums[i]] = i
    nums.sort()
    start=0
    end=len(nums)-1
    while start<end:
        if (nums[start]+nums[end])>target:
            end-=1
        elif (nums[start]+nums[end])<target:
            start+=1
        else:
            return [dict_indices[nums[start]],dict_indices[nums[end]]]
    return None

# target=int(input("enter the target number"))
# nums=[]
# n=int(input("enter the number of numbers"))
# for i in range(n):
#     a=int(input("enter the number"))
#     nums.append(a)
# q=two_sum(nums,target)
# print(q)
