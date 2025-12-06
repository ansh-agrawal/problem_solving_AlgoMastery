"""
Task 10: 3Sum

Given nums, return all unique triplets [nums[i], nums[j], nums[k]] such that they sum to zero (0-indexed).

Example:
    three_sum(nums=[-1,0,1,2,-1,-4]) -> [[-1,-1,2],[-1,0,1]]

Args:
    nums (list[int]): List of integers (0-indexed)

Returns:
    list[list[int]]: List of triplets that sum to zero
"""

def three_sum(nums: list[int]) -> list[list[int]]:
    triplets = []
    nums.sort()
    # if len(nums)<=2:
    #     return [-1,-1,-1]
    m={}
    for i in range(0,len(nums)-3):
        sum=0
        if m.get(nums[i]) is None:
            m[nums[i]]=i
            start=i+1
            end=len(nums)-1
            sum+=nums[i]
            while start<end:
                temp_triplets = []
                while start< end and nums[start]==nums[start+1]:
                    start+=1
                while start<end and nums[end]==nums[end-1]:
                    end-=1
                if start<end and (nums[start]+nums[end]+sum) == 0:
                    temp_triplets.append(nums[i])
                    temp_triplets.append(nums[start])
                    temp_triplets.append(nums[end])
                    start+=1
                    end-=1
                    triplets.append(temp_triplets)
                elif start<end and (nums[start]+nums[end]-sum) > 0:
                    end-=1
                else:
                    start+=1
    return triplets