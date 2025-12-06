"""
Task 5: Product of Array Except Self

Given an array nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
    product_of_array_except_self(nums=[1,2,3,4]) -> [24,12,8,6]
    product_of_array_except_self(nums=[-1,1,0,-3,3]) -> [0,0,9,0,0]

Args:
    nums (list[int]): List of integers (0-indexed)

Returns:
    list[int]: Product of array except self
"""

def product_of_array_except_self(nums: list[int]) -> list[int]:
    count=0
    prd=1
    ind=-1
    for i in range(len(nums)):
        if nums[i]==0:
            count+=1
            ind=i
        else:
            prd*=nums[i]
    if count>1:
        return [0]*len(nums)
    elif count==1:
        nums=[0]*len(nums)
        nums[ind]=prd
        return nums
    else:
        for i in range(len(nums)):
            nums[i]=int(prd/nums[i])
        return nums
